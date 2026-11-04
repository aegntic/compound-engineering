```markdown
# compound-engineering Development Patterns

> Auto-generated skill from repository analysis

## Overview
This skill teaches the core development patterns and conventions used in the `compound-engineering` TypeScript codebase. It covers file naming, import/export styles, commit message conventions, and testing patterns. By following these guidelines, contributors can ensure consistency and maintainability throughout the project.

## Coding Conventions

### File Naming
- All files use **kebab-case**.
  - Example:  
    ```
    user-profile.ts
    data-fetcher.test.ts
    ```

### Import Style
- Use **relative imports** for modules within the repository.
  - Example:
    ```typescript
    import { fetchData } from './data-fetcher';
    ```

### Export Style
- Use **named exports** for all modules.
  - Example:
    ```typescript
    // In utils.ts
    export function calculateSum(a: number, b: number): number {
      return a + b;
    }
    ```

### Commit Messages
- Follow the **Conventional Commits** standard.
- Use the `feat` prefix for new features.
- Keep commit messages concise (average ~63 characters).
  - Example:
    ```
    feat: add user authentication middleware
    ```

## Workflows

_No automated workflows detected in this repository._

## Testing Patterns

- Test files follow the pattern: `*.test.*`
  - Example:  
    ```
    math-utils.test.ts
    ```
- The testing framework is **unknown** (not detected), but tests are colocated with source files or in the same directory.
- Example test file structure:
  ```typescript
  // math-utils.test.ts
  import { calculateSum } from './math-utils';

  describe('calculateSum', () => {
    it('adds two numbers', () => {
      expect(calculateSum(2, 3)).toBe(5);
    });
  });
  ```

## Commands
| Command | Purpose |
|---------|---------|
| /test   | Run all test files matching `*.test.*` |
| /commit | Create a conventional commit message (e.g., `feat: ...`) |
```
