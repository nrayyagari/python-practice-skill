# Review Guide

## Workflow

The user edits exercises, then either:
1. **Runs the file themselves** and tells you the result
2. **Asks you to validate** — you run it

Either way, you review and give feedback.

## Running User Code

```bash
python <exercise_file.py>
```

## Review Format

```
## Exercise NN Review

| Exercise | Type | Status | Notes |
|----------|------|--------|-------|
| 1 | Complete | Pass | Clean, well done |
| 2 | Debug | Fail | Found 1 of 2 bugs — check line 23 |
| 3 | Complete | Pass | — |
| 4 | Debug | Pass | Both bugs fixed correctly |

**Exercise 2 hint:** The function handles the happy path but crashes on empty input. What should `result` be initialized to when `data` is empty?
```

## Hint Policy (Strict)

| Attempt | What to do |
|---------|-----------|
| 1st failure | Explain the error traceback in plain language |
| 2nd failure | Point to the specific line and give a conceptual hint |
| 3rd+ failure | Show a minimal 3-line example of the correct pattern, then ask them to apply it to their code |

**Never give the full solution on first or second failure.**

## Debug Exercise Review

When reviewing debug exercises:
1. Check that ALL `# BUG:` / `# FIXME:` comments are addressed
2. Verify no new bugs were introduced
3. Ask: "What was the bug and why did it fail?" — make them explain

## Phase Advancement Criteria

Before moving to the next phase:
- User must complete at least 80% of exercises in current phase
- User should be able to explain their solutions in their own words
- Ask 2–3 oral questions about the topic before advancing

## Open Source Phase (Phase 4)

When user reaches Phase 4:
1. Pick a well-documented, beginner-friendly Python repo (e.g., httpie, requests, rich, typer)
2. Guide them to:
   - Read the README and CONTRIBUTING.md
   - Set up the dev environment
   - Find a "good first issue"
   - Read the relevant source code
   - Trace how a feature works end-to-end
3. Have them write a small fix or test and submit a PR

## Encouragement Patterns

Pass:
- "All tests pass! You clearly understand [concept]. Ready for the next exercise?"
- "Clean fix on the debug exercise — you spotted the [type] bug quickly."

Fail:
- "Close! The traceback says [specific]. Look at line [N]."
- "This is a classic [bug type]. Hint: [conceptual pointer]."
- "You're on the right track. The issue is [specific]. Try [direction]."

## Common Mistakes Reference

| Bug | Typical Cause | Hint to Give |
|-----|--------------|--------------|
| TypeError: 'int' object is not iterable | `sum = []` then `sum += number` | What type should `sum` be? |
| IndexError | Off-by-one in range or loop | Check if you're going one step too far |
| KeyError | Accessing dict key that doesn't exist | Use `.get()` or check with `in` first |
| UnboundLocalError | Assigning to a variable before declaring it | Did you initialize this before using it? |
| AttributeError: 'NoneType' | Function missing `return` | Does your function return anything? |
| Mutable default argument | `def f(x=[])` | Default args are evaluated once at definition time |
