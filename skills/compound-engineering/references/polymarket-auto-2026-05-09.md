# Session Notes: Polymarket Auto Dashboard (2026-05-09)

## Project Context
- **Repo**: `~/AE/01_Laboratory/polymarket-auto`
- **Stack**: Next.js 16.1.3 + Turbopack, React 18, TypeScript, Tailwind, wagmi v7, viem v2, Prisma + SQLite
- **Purpose**: Autonomous Polymarket trading dashboard with AI-powered edge detection
- **Stakes**: Production demo for $10M contract — zero tolerance for visible bugs

## What Was Fixed This Session

### 1. 60+ TypeScript Compile Errors → 0
Systematic triage using `npx tsc --noEmit 2>&1 | grep "error TS" | sed 's/.*error //' | sort | uniq -c | sort -rn` to find highest-count patterns first.

Key fixes across 17 files:
- Missing imports, variable name mismatches, framer-motion ease types, recharts data annotations, declaration order issues, API response shape mismatches

### 2. Trading Tab Runtime Crash
**Error**: `InvalidParameterError: Invalid ABI parameter` from `trading-service.ts` at module load time.
**Fix**: Rewrote with viem v2 API (`readContract`/`writeContract`), lazy-loaded ABI parsing, removed tuple from ABI.

### 3. Risk & Strategy Tab Runtime Crash
**Error**: `TypeError: performance.map is not a function` — API returns `{ series, summary }` not array.
**Fix**: `const series = Array.isArray(performance) ? performance : (performance?.series ?? [])` at 3 sites.

### 4. wagmi v6 → v7 Partial Migration
Removed all `useBalance` with `contract:` parameter. Balance shows 0.00 until proper v7 migration.

## Verification
- Production build: `npx next build` → ✓ Compiled successfully, 19/19 pages
- All 6 API routes return 200
- All 4 tabs render without crashes
- 0 TypeScript errors in source files
