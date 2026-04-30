# Review Guide

## User Workflow

1. User asks for exercises on a topic
2. You generate 3 exercise files
3. User edits files (completing code or fixing bugs)
4. User runs: `python <file.py>`
5. User reports results OR asks you to check
6. You review and record learning data
7. You update `learning-log.md` with findings

## Running User Code

```bash
python <exercise_file.py>
```

Run all 3 files from the batch.

## Review Format

```
## Exercise Batch Review

### 01_fundamentals_vars_complete.py
| Test | Status | Notes |
|------|--------|-------|
| test_1 | Pass | Correct |
| test_2 | Pass | Good edge case handling |

💪 Recording strength: quick completion of variable assignments

### 02_fundamentals_funcs_debug.py
| Test | Status | Notes |
|------|--------|-------|
| test_1 | Pass | Bug 1 fixed correctly |
| test_2 | Fail | Bug 2 not yet found — check line 18 |

📝 Recording mistake: type_error — initialized total as [] instead of 0

**Hint for 02:** The function works for the happy path but fails on empty input. What should happen when `numbers` is `[]`?

### 03_fundamentals_lists_complete.py
| Test | Status | Notes |
|------|--------|-------|
| test_1 | Pass | Clean list comprehension |
| test_2 | Pass | — |

💪 Recording strength: list comprehensions

**Summary:** 2/3 exercises complete. Fix bug in #02 and you're ready for the next batch!

📊 Your learning profile has been updated in `learning-log.md`.
```

## Recording Learning Data

After each review, record data using the progress tracker:

### Mark exercise complete
```bash
python scripts/progress_tracker.py <dir> complete <file> <attempts>
```

### Record a mistake
```bash
python scripts/progress_tracker.py <dir> mistake <file> <bug_type> "description"
```

Example bug types: `type_error`, `off_by_one`, `missing_return`, `shadowing_builtin`, `not_pythonic`

### Record a strength
```bash
python scripts/progress_tracker.py <dir> strength <file> "concept"
```

### Update learning log
```bash
python scripts/progress_tracker.py <dir> update-log
```

## Hint Policy (Strict)

| Attempt | Response |
|---------|----------|
| 1st failure | Explain the error/traceback in plain language |
| 2nd failure | Point to the specific line, give a conceptual hint |
| 3rd+ failure | Show a 3-line minimal example of the correct pattern, ask them to apply it |

**Never give the full solution before the 3rd attempt.**

## Debug Exercise Review

For debug exercises, ask:
1. "What bug did you find?" — make them explain
2. "Why did it cause the test to fail?" — ensure understanding
3. Verify all `# BUG:` / `# FIXME:` comments are addressed

## Idiomatic Python Review

When reviewing complete exercises, also check for Pythonic style:

### Common Non-Idiomatic Patterns to Flag

| Non-Idiomatic | Idiomatic |
|--------------|-----------|
| `for i in range(len(items)): print(items[i])` | `for item in items: print(item)` |
| `result = []; for x in items: result.append(f(x))` | `result = [f(x) for x in items]` |
| `i = 0; for item in items: print(i, item); i += 1` | `for i, item in enumerate(items):` |
| `for i in range(len(a)): print(a[i], b[i])` | `for x, y in zip(a, b): print(x, y)` |
| `if key in d: return d[key]; else return default` | `return d.get(key, default)` |
| `f = open('file'); data = f.read(); f.close()` | `with open('file') as f: data = f.read()` |
| Manual sum loop | `sum(items)` |
| `def f(x=[]): ...` | `def f(x=None): if x is None: x = []` |

When you spot non-idiomatic code:
- "Your solution works! Here's a more Pythonic way: [show pattern]"
- "This is a good opportunity to learn [idiom]. In Python, we typically write it as: [example]"

## Difficulty Escalation Review

When user completes a batch and asks for more on the SAME topic:
- Increase difficulty level by 1
- More complex scenarios, more edge cases
- Combine concepts from previous batches

When user completes Level 3 on a topic:
- Congratulate them
- Suggest moving to a related sub-topic or next major topic
- Offer to mix topics for variety

## Phase & Topic Advancement

Track in progress.json and learning-log.md.

Advance topic when:
- User has completed at least 6 exercises (2 batches) at Level 3
- User demonstrates understanding through oral explanation
- Accuracy > 80% on current topic

## Encouragement

Pass:
- "All 3 exercises pass! You're clearly comfortable with [topic]. Ready for Level [N+1]?"
- "Clean fixes on the debug exercises — you spotted the [type] bugs quickly."
- "Great use of [idiom] — that's the Pythonic way!"

Partial pass:
- "2 out of 3 done! One more bug to find in [file]. Hint: [direction]."

Fail:
- "The traceback in [file] says [specific]. Look at line [N]."
- "This is a classic [bug type]. Think about [concept]."
- "You're on the right track. The issue is [specific]. Try [direction]."

## Using the Learning Log

After each batch, point the user to their `learning-log.md`:

```
Your learning log has been updated! Check it out:
cat python-exercises/learning-log.md

It shows:
- Your strengths so far
- Areas to focus on
- Personalized reminders
- Next recommended steps
```

## Context7 Integration

When explaining concepts or idioms, use Context7 to verify:
- Python built-in function signatures and best practices
- Standard library module documentation
- Idiomatic patterns from official Python docs

Query Context7 for:
- `Python list comprehensions best practices`
- `Python EAFP vs LBYL`
- `Python context managers`
- `Python itertools recipes`

Use the verified information when:
- Explaining why a pattern is idiomatic
- Suggesting better alternatives to user's code
- Teaching new concepts in exercises
