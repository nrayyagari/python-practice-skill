# Exercise Templates

## File Structure

```python
"""
Exercise NN: Topic Name
=======================
Phase: N

Learning objective: One-sentence summary.
Reference: https://python.swaroopch.com/<chapter>.html
"""


# ═══════════════════════════════════════════════════════════════
# EXERCISE 1: Complete the function
# ═══════════════════════════════════════════════════════════════
# Instructions: Implement the function below so it passes the test.

def function_name(args) -> return_type:
    """
    Description of what the function should do.

    >>> function_name(example_input)
    expected_output
    """
    # TODO: Implement this function
    pass


# ═══════════════════════════════════════════════════════════════
# EXERCISE 2: Debug this code
# ═══════════════════════════════════════════════════════════════
# Instructions: This function has bugs. Find and fix them.
# Hints are in the comments.

def buggy_function(args) -> return_type:
    """
    Description of what the function should do.

    >>> buggy_function(example_input)
    expected_output
    """
    # BUG: This line is incorrect. Think about what type `data` is.
    result = data + []  # <-- FIX ME
    return result


# ═══════════════════════════════════════════════════════════════
# EXERCISE 3: Complete the function
# ═══════════════════════════════════════════════════════════════

def another_function(args) -> return_type:
    """..."""
    # TODO: Implement this function
    pass


# ═══════════════════════════════════════════════════════════════
# EXERCISE 4: Debug this code
# ═══════════════════════════════════════════════════════════════
# Instructions: The logic is almost right but fails edge cases.

def another_buggy_function(args) -> return_type:
    """..."""
    # BUG: Off-by-one error. Check the range boundary.
    for i in range(len(items) + 1):  # <-- FIX ME
        ...


# ═══════════════════════════════════════════════════════════════
# TESTS
# ═══════════════════════════════════════════════════════════════
# Run this file to check your work: python NN_topic.py

def test():
    # Exercise 1 tests
    assert function_name(...) == ...

    # Exercise 2 tests (buggy_function should pass after fixes)
    assert buggy_function(...) == ...

    # Exercise 3 tests
    assert another_function(...) == ...

    # Exercise 4 tests
    assert another_buggy_function(...) == ...

    print("All tests passed!")


if __name__ == "__main__":
    test()
```

## Rules

1. **File size**: 80–150 lines maximum
2. **Exercise count**: 4–6 exercises per file (mix of complete + debug)
3. **Instruction style**: Comments above each exercise, NOT in the SKILL.md
4. **Difficulty ramp**: Easier exercises first, harder ones last
5. **Debug exercises must have `# BUG:` or `# FIXME:` comments**
6. **No accidental solutions left in stubs**
7. **Tests must fail before user edits, pass after**

## Debug Exercise Patterns

Common bug types to include:
- **Type errors**: Wrong initial value (e.g., `sum = []` instead of `sum = 0`)
- **Off-by-one**: Wrong range boundaries
- **Mutating while iterating**: Modifying a list/dict while looping over it
- **Shadowing builtins**: Naming a variable `sum`, `list`, `dict`, etc.
- **Missing return**: Function computes result but doesn't return it
- **Logic errors**: Wrong operator, inverted condition, wrong variable used
- **Reference vs copy**: `a = b` instead of `a = b[:]` for lists
- **Indentation**: Wrong scope for return/loop body

## Quality Checklist

Before delivering to user:
- [ ] Mix is ~60% completion, ~40% debug
- [ ] Every debug exercise has a `# BUG:` or `# FIXME:` comment
- [ ] Comments explain what to do, not how to do it
- [ ] Running the file shows failures (as expected)
- [ ] File is under 150 lines
- [ ] Reference to swaroopch chapter included in header
