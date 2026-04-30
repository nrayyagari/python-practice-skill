# Exercise Templates

## Date Folder Layout

All generated exercises belong under:

```text
/home/laborant/repos/python-practice/<D-mmm-YY>/
```

Examples:

```text
/home/laborant/repos/python-practice/3-may-26/
/home/laborant/repos/python-practice/30-apr-26/
```

If the user asks for more exercises on the same day, append to that same folder
and continue numbering.

## Single Exercise File Format

Each file contains ONE exercise only.

```python
"""
Exercise NN: Brief Title
========================
Topic: <topic_name>
Difficulty: N/5
Type: complete | debug
Domain: foundations | backend | fastapi | flask | aws | cli | data

Instructions:
<Clear explanation of what to do>
"""

# TODO or # BUG comments below
```

**Difficulty Scale (per exercise):**
- **1/5** — Single concept, very straightforward
- **2/5** — Simple combination of 2 concepts
- **3/5** — Requires planning, multiple steps
- **4/5** — Complex scenario, edge cases
- **5/5** — Production-like mini-project

---

## Package Exercise Format

Use this for backend, FastAPI, Flask, AWS automation, CLI, and capstone tasks.

```text
<D-mmm-YY>/NN_<topic>_<subtopic>/
  README.md
  pyproject.toml
  src/<package_name>/...
  tests/...
```

README template:

```markdown
# Exercise NN: <Title>

Goal: <one sentence>

Run:

```bash
python -m pytest
```

Expected now: tests fail.

Constraints:
- Keep the public API small.
- Prefer standard library unless the exercise requires a framework/library.
- Return useful errors.
- Use fakes for external systems unless real integration is requested.
- Keep AWS exercises dry-run/idempotent by default.
```

---

## Complete Exercise Template

```python
"""
Exercise 01: Calculate Discount
================================
Topic: Fundamentals / Functions
Type: complete
Difficulty: 1
Reference: https://python.swaroopch.com/functions.html

Instructions:
Implement the function below to calculate a percentage discount.
The function should return the final price after discount.
Handle edge case: if discount_percent is negative, return original price.

Idiomatic hint: Use a conditional expression for the edge case.
"""


def calculate_discount(original_price: float, discount_percent: float) -> float:
    """
    Calculate the final price after applying a percentage discount.

    >>> calculate_discount(100.0, 20.0)
    80.0
    >>> calculate_discount(50.0, 0.0)
    50.0
    >>> calculate_discount(100.0, -10.0)
    100.0
    """
    # TODO: Implement this function
    # Hint: Think about using a conditional expression or EAFP pattern
    pass


# ═══════════════════════════════════════════════════════════════
# TESTS — Do not modify below this line
# ═══════════════════════════════════════════════════════════════

def test():
    assert calculate_discount(100.0, 20.0) == 80.0
    assert calculate_discount(50.0, 0.0) == 50.0
    assert calculate_discount(100.0, -10.0) == 100.0
    assert calculate_discount(0.0, 50.0) == 0.0
    print("All tests passed!")


if __name__ == "__main__":
    test()
```

---

## Debug Exercise Template

```python
"""
Exercise 02: Fix the Average Calculator
========================================
Topic: Fundamentals / Functions
Type: debug
Difficulty: 1
Reference: https://python.swaroopch.com/functions.html

Instructions:
This function is supposed to calculate the average of a list of numbers.
It has bugs. Find and fix them.
Run the file to see which tests fail.

Idiomatic hint: Python has built-in functions that can make this cleaner.
"""


def calculate_average(numbers: list[float]) -> float:
    """
    Calculate the average of a list of numbers.
    Returns 0.0 if the list is empty.

    >>> calculate_average([10.0, 20.0, 30.0])
    20.0
    >>> calculate_average([])
    0.0
    >>> calculate_average([5.0])
    5.0
    """
    if len(numbers) == 0:
        return 0.0

    total = []

    for num in numbers:
        total += num

    return total / len(numbers) + 1


# ═══════════════════════════════════════════════════════════════
# TESTS — Do not modify below this line
# ═══════════════════════════════════════════════════════════════

def test():
    assert calculate_average([10.0, 20.0, 30.0]) == 20.0
    assert calculate_average([]) == 0.0
    assert calculate_average([5.0]) == 5.0
    assert calculate_average([1.0, 2.0, 3.0, 4.0]) == 2.5
    print("All tests passed!")


if __name__ == "__main__":
    test()
```

---

## Idiomatic Python Checklist

When generating exercises (complete type), ensure the intended solution can use these patterns:

### Level 1 — Basic Idioms
- List comprehensions instead of simple for-loops
- `enumerate()` instead of `range(len(...))`
- `zip()` for parallel iteration
- `with` statement for file operations
- `dict.get()` instead of `if key in dict`
- Tuple unpacking

### Level 2 — Intermediate Idioms
- Generator expressions for lazy evaluation
- `sum()`, `min()`, `max()` with generator expressions
- EAFP (Easier to Ask Forgiveness than Permission) pattern
- `collections.Counter` for counting
- `collections.defaultdict` for grouping
- String methods (`join`, `split`, `strip`) instead of manual loops

### Level 3 — Advanced Idioms
- Decorators for cross-cutting concerns
- Context managers (`@contextmanager`)
- `functools.lru_cache` for memoization
- `itertools` for combinatorial operations
- Type hints throughout
- Abstract base classes

---

## Difficulty Levels

### Level 1 — Foundation
- Single concept
- Straightforward logic
- 1–2 functions to implement/fix
- 30–50 lines total
- Clear docstring examples
- Focus: basic syntax + simple idioms

### Level 2 — Combination
- Combine 2–3 concepts
- Requires planning before coding
- 2–3 functions, possibly interdependent
- 50–70 lines total
- Include edge cases in tests
- Focus: intermediate idioms (comprehensions, zip, enumerate)

### Level 3 — Real-World
- Mini-project or realistic scenario
- Multiple functions working together
- Error handling required
- 60–80 lines total
- May require understanding a small domain
- Focus: advanced idioms + best practices

---

## Debug Bug Patterns

Include these bug types across exercises (NO explicit hints in comments):

| Bug | Example |
|-----|---------|
| Wrong type initialization | `total = []` for sum (should be `0`) |
| Off-by-one | `range(len(items) + 1)` |
| Missing return | computes but no `return` |
| Shadowing builtins | `sum = 0` |
| Mutable default arg | `def f(x=[])` |
| Wrong operator | using `+` for lists instead of `.append()` |
| Logic inversion | `if x > 0:` instead of `if x < 0:` |
| Reference vs copy | `a = b` for lists |
| Not Pythonic | manual loop instead of `sum()` |

**Rule: Do NOT put `# BUG:` or `# FIXME:` comments in the code.**

---

## Backend/API Exercise Patterns

Use small functions and tests before full frameworks:
- Validate request-like dictionaries or Pydantic models.
- Convert domain errors to response-shaped results.
- Separate route/controller logic from service logic.
- Keep persistence or client calls behind tiny protocols/fakes.

FastAPI exercises can include:
- routers
- dependencies
- Pydantic request/response models
- `TestClient`
- dependency overrides

Flask exercises can include:
- app factory
- blueprints
- test client
- config
- error handlers

## AWS Automation Exercise Patterns

Default to fake boto3-shaped clients. Do not require real AWS credentials unless
the user explicitly asks for integration.

Good AWS exercise shapes:
- paginator handling
- retry wrapper with testable sleep/backoff
- dry-run cleanup planner
- idempotent tag updater
- report generator from AWS-shaped responses
- region/session configuration boundary

Every AWS automation exercise should include at least one safety constraint:
- dry-run mode
- explicit allowlist/filter
- max attempts
- idempotency check
- no real network calls

## Quality Checklist

Before delivering exercises to the user:
- [ ] Output count matches selected mode.
- [ ] Default batch includes at least 1 debug and 1 completion exercise.
- [ ] Files are in `/home/laborant/repos/python-practice/<D-mmm-YY>/`.
- [ ] Files are numbered sequentially within the date folder.
- [ ] Running tests shows failures (expected because not solved).
- [ ] Debug exercises do not reveal exact fixes in comments.
- [ ] Instructions are in the file docstring or README.
- [ ] Difficulty follows the root learning log.
- [ ] Exercise targets recurring mistakes/questions when relevant.
- [ ] No real AWS calls by default.
- [ ] Framework dependency appears only when framework behavior is the point.
- [ ] Tests include at least one edge case.
- [ ] FastAPI/Flask exercises include test client or dependency boundary.
- [ ] AWS exercises include pagination, retry, dry-run, or idempotency when relevant.
