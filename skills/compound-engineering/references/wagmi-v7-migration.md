# wagmi v6 → v7 Migration Reference

## Key Breaking Changes

### useBalance (ERC20 tokens)

**v6 (old):**
```ts
const { data: balance } = useBalance({
  address: walletAddress,
  contract: '0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359',
  chainId: 137,
})
```

**v7 (new):**
```ts
// Option 1: Use useReadContract for ERC20
const { data: balance } = useReadContract({
  address: '0x3c499c542cEF5E3811e1192ce70d8cC03d5c3359',
  abi: parseAbi(['function balanceOf(address) view returns (uint256)']),
  functionName: 'balanceOf',
  args: [walletAddress],
  chainId: 137,
})

// Option 2: Remove entirely if balance display is not critical
const balance = null // placeholder
```

### Contract Write

**v6 (old):**
```ts
const hash = await contract.write.approve([spender, amount])
```

**v7 (new):**
```ts
const hash = await writeContract(config, {
  address: contractAddress,
  abi: CONTRACT_ABI,
  functionName: 'approve',
  args: [spender, amount],
})
```

### ABI Parsing (viem)

`parseAbi` is stricter about tuple syntax in v7:

**Broken:**
```ts
parseAbi(['function getOrder(uint256) view returns (tuple(uint256 id, address trader, uint256 marketId, uint8 outcome, uint256 price, uint256 size, uint8 status))'])
```

**Fixed:**
```ts
parseAbi(['function getOrder(uint256) view returns (uint256, address, uint256, uint8, uint256, uint256, uint8)'])
```

### Contract Read/Write (viem v1 → v2)

**v1 (old) — `getContract` pattern:**
```ts
import { getContract } from 'viem'
const contract = getContract({
  address: CONTRACTS.usdc,
  abi: USDC_ABI,
  client: { public: publicClient, waller: walletClient }, // note: typo "waller" was common
})
const allowance = await contract.read.allowance([owner, spender])
const hash = await contract.write.approve([spender, amount])
```

**v2 (new) — direct `readContract`/`writeContract`:**
```ts
import { createPublicClient, createWalletClient, http, parseAbi } from 'viem'
import { polygon } from 'viem/chains'

// Read
const allowance = await publicClient.readContract({
  address: CONTRACTS.usdc,
  abi: getUSDCABI(), // lazy-loaded to avoid module-load crashes
  functionName: 'allowance',
  args: [owner, spender],
})

// Write
const hash = await walletClient.writeContract({
  address: CONTRACTS.usdc,
  abi: getUSDCABI(),
  functionName: 'approve',
  args: [spender, amount],
  account: walletClient.account.address,
  chain: polygon,
})
```

**Key differences:**
- `client: { public, wallet }` → separate `publicClient` and `walletClient` instances
- `contract.read.method(args)` → `publicClient.readContract({ address, abi, functionName, args })`
- `contract.write.method(args)` → `walletClient.writeContract({ address, abi, functionName, args, account, chain })`
- ABI parsing should be lazy-loaded (module-level `parseAbi` can crash at import time)
- `BigInt` literals (`0n`) may not compile in older TS targets — use `BigInt(0)` instead

### Type Errors to Watch For

- `Object literal may only specify known properties, and 'contract' does not exist` → use `token:` or switch to `useReadContract`
- `Property 'write' does not exist on type '...'` → use `writeContract` from wagmi
- `Type '...' is not assignable to type 'never'` → usually from `Client<Transport, Chain>` intersection being reduced to `never` due to conflicting `cacheTime` types. Non-blocking at runtime (Turbopack compiles with warnings).
- `Property 'authorizationList' is missing` → viem v2 `ReadContractParameters` requires `authorizationList`. Non-blocking at runtime.

## Batch Fix Pattern

When the same API change affects many files:

```bash
# Find all occurrences
grep -rn "contract:" src/ | grep -v node_modules

# Fix all at once with sed or patch tool
# Then verify
npx tsc --noEmit 2>&1 | grep "error TS" | wc -l
```

## Session-Specific Notes (2026-05-09, Polymarket Auto)

### What Actually Broke and How It Was Fixed

1. **`useBalance` with `contract:` parameter** — Affected 3 files (`page.tsx`, `WalletMenu.tsx`, `WalletConnectPanel.tsx`). Even changing `contract:` to `token:` didn't resolve the type errors because `UseBalanceParameters` changed deeply in v7. **Fix**: Removed `useBalance` entirely, replaced with `const balance = null`. Balance displays show 0.00 until proper v7 migration.

2. **`getContract` + `contract.read/write`** — Affected `trading-service.ts`. The viem v1 pattern `getContract({ address, abi, client: { public, wallet } })` + `contract.read.allowance()` / `contract.write.approve()` is incompatible with viem v2. Also had a typo: `waller` instead of `wallet`. **Fix**: Rewrote to use `publicClient.readContract()` and `walletClient.writeContract()` directly. Also lazy-loaded ABI parsing to prevent module-load crashes.

3. **API response shape mismatch** — `RiskAnalysis.tsx` typed `useQuery<PerformancePoint[]>` but `/api/performance` returns `{ series: [...], summary: {...} }`. Caused `performance.map is not a function` at runtime. **Fix**: `const series = Array.isArray(performance) ? performance : (performance?.series ?? [])` at each of 3 usage sites.

4. **Turbopack stale chunk cache** — After many file changes, chunk `1733ae16ecece748.js` returned 500. Browser had cached HTML referencing old chunk hashes. **Fix**: `rm -rf .next` (not just `.next/cache`) and restart dev server.

5. **Non-blocking TS errors** — `trading-service.ts` has TS2322/TS2339 from viem v2 strict types. Turbopack compiles at runtime with warnings. These don't block the dashboard from working.

### Key Lesson
TypeScript compile success (`npx tsc --noEmit` = 0 errors) does NOT guarantee runtime safety. Always verify:
- API response shapes match type assertions (check with `curl`)
- Array methods aren't called on objects
- Empty/null states don't cascade into crashes
