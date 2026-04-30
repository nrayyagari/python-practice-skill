# Review Guide

## Running User Code

Always execute the user's exercise file to verify:
```bash
python <exercise_file.py>
```

## Review Format

Present results in a table:

```
## Exercise NN Review

| Function | Status | Notes |
|----------|--------|-------|
| func_a   | Pass   | Clean implementation |
| func_b   | Fail   | Off-by-one error in loop range |
| func_c   | Not done | — |
```

## Hint Policy

| Attempt | Response |
|---------|----------|
| 1st failure | Explain the error in plain language |
| 2nd failure | Give a targeted hint pointing toward the fix |
| 3rd+ failure | Show a minimal correct example, then ask them to apply it |

Never give the full solution on the first failure.

## Common Mistakes to Watch For

- `sum = []` instead of `sum = 0` (shadowing builtins, wrong type)
- Modifying a dict while iterating over it
- Forgetting to return values from functions
- Off-by-one errors in ranges
- Calling `.upper()` on non-string values
- Returning the closure function object instead of calling it

## Encouragement Patterns

When tests pass:
- "All tests pass! Ready for the next exercise?"
- "Clean implementation — especially liked the use of [specific technique]."
- "Well done. This concept often trips people up, but you nailed it."

When tests fail:
- "Close! The issue is [specific]. Try [hint]."
- "This is a common mistake — [explanation]."
- "You're on the right track. The problem is [specific]."
