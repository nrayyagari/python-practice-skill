# Exercise Templates

## File Structure

Each exercise file follows this pattern:

```python
"""
Exercise NN: Topic Name
=======================
Topics: comma-separated list
"""


def function_one(args) -> return_type:
    """
    Clear description of what to do.

    >>> function_one(example_input)
    expected_output
    """
    # TODO: Implement this
    pass


def function_two(args) -> return_type:
    """
    Another clear description.

    >>> function_two(example_input)
    expected_output
    """
    # TODO: Implement this
    pass


def test():
    assert function_one(...) == ...
    assert function_two(...) == ...
    print("All tests passed!")


if __name__ == "__main__":
    test()
```

## Rules

1. Each function teaches ONE concept
2. Include 4–6 functions per exercise file
3. Add edge cases in tests: empty inputs, negative numbers, boundary conditions
4. Do NOT provide solutions — only `pass` or minimal stubs
5. Import statements go at the top
6. Type hints are encouraged
7. Keep each file under 150 lines
8. Number files sequentially: `01_basics.py`, `02_functions.py`, etc.

## Quality Checklist

Before delivering exercises to the user:

- [ ] All functions have `TODO` markers
- [ ] Doctests show realistic examples
- [ ] Test function covers all implemented functions
- [ ] Running the file with `python` shows failures (as expected — not yet implemented)
- [ ] No accidental solutions left in stubs
- [ ] File is under 150 lines
