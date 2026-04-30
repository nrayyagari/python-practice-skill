# Exercise Templates

## Single Exercise File Format

Each file contains ONE exercise only.

```python
"""
Exercise NN: Brief Title
========================
Topic: <major_topic> / <sub_topic>
Type: complete | debug
Difficulty: 1 | 2 | 3
Reference: https://python.swaroopch.com/<chapter>.html

Instructions:
<Clear explanation of what to do>
"""

# TODO or # BUG comments below
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

💡 Idiomatic hint: Use a conditional expression for the edge case.
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
    # 💡 Hint: Think about using a conditional expression or EAFP pattern
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
It has bugs. Find and fix them. There are 2 bugs.
Hints are in the comments marked with # BUG:.

💡 Idiomatic hint: Python has built-in functions that can make this cleaner.
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

    # BUG 1: Wrong initial value type. What should total be?
    total = []

    for num in numbers:
        # BUG 2: This operation is incorrect for the type of total.
        total += num

    # BUG 3: Wrong divisor — should this be len(numbers) or something else?
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

Include these bug types across exercises:

| Bug | Marker | Example |
|-----|--------|---------|
| Wrong type initialization | `# BUG: Should this be [] or 0?` | `total = []` for sum |
| Off-by-one | `# BUG: Check the boundary` | `range(len(items) + 1)` |
| Missing return | `# BUG: Is the result returned?` | computes but no `return` |
| Shadowing builtins | `# BUG: Avoid shadowing built-ins` | `sum = 0` |
| Mutable default arg | `# BUG: When is this evaluated?` | `def f(x=[])` |
| Wrong operator | `# BUG: Should this be + or *?` | using `+` for lists instead of `.append()` |
| Logic inversion | `# BUG: Is the condition correct?` | `if x > 0:` instead of `if x < 0:` |
| Reference vs copy | `# BUG: Is this a copy or reference?` | `a = b` for lists |
| Not Pythonic | `# BUG: Can you use a built-in instead?` | manual loop instead of `sum()` |

---

## Quality Checklist

Before delivering exercises to the user:
- [ ] Exactly 3 exercise files generated
- [ ] Mix includes at least 1 debug and 1 complete
- [ ] Files are numbered sequentially (check existing files first)
- [ ] Each file is 30–80 lines
- [ ] Running each file shows test failures (expected — not solved)
- [ ] Debug exercises have `# BUG:` or `# FIXME:` comments
- [ ] Instructions are in the file's docstring
- [ ] Difficulty level is appropriate for user's progress on this topic
- [ ] Idiomatic Python hints included where relevant
- [ ] Personalized notes from learning profile added to docstrings
