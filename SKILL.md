---
name: python-practice
description: Generate interactive Python coding exercises with built-in tests, review completed solutions, and track learning progress across topics. Use whenever the user wants to practice Python, learn a new Python concept, do coding exercises, improve their Python skills, or says anything about Python practice, coding challenges, Python exercises, or learning Python. Also trigger when the user asks for exercises in a specific Python topic like decorators, OOP, generators, error handling, file I/O, data structures, or testing.
---

# Python Practice

Generate hands-on Python exercises with self-checking tests. Create exercise files in a dedicated folder, review the user's solutions, and maintain a progress tracker.

## When to use

- User wants to practice Python
- User asks for exercises on a specific topic
- User wants to learn a new Python concept
- User asks you to review their Python code
- User mentions "coding challenge", "exercise", "practice" in the context of Python

## Workflow

### 1. Assess current level and topic

Ask the user (or infer from context):
- What Python topic do they want to practice? (or pick one based on their level)
- What difficulty: beginner, intermediate, or advanced?

**Topic catalog:**
- `basics` — variables, types, conditionals, loops, string formatting
- `functions` — default args, *args, **kwargs, closures, recursion, lambdas
- `data_structures` — lists, dicts, sets, tuples, comprehensions
- `file_io` — reading/writing files, JSON, CSV, pathlib
- `oop` — classes, inheritance, dunder methods, properties
- `error_handling` — try/except, custom exceptions, EAFP vs LBYL
- `iterators_generators` — yield, generator expressions, itertools
- `decorators` — function decorators, functools, parameterized decorators
- `context_managers` — __enter__/__exit__, @contextmanager
- `testing` — pytest, unittest, mocking, parametrize
- `concurrency` — threading, asyncio, multiprocessing
- `advanced` — metaclasses, descriptors, import hooks

**Progressive path (default if no topic specified):**
basics → functions → data_structures → file_io → oop → error_handling → iterators_generators → decorators → context_managers → testing

### 2. Generate exercises

Create a folder for the exercises if it doesn't exist:
```
<workspace>/python-exercises/
```

Or use an existing `python-exercises/` folder if found in the workspace.

For each exercise file:
1. Name it sequentially: `01_topic.py`, `02_topic.py`, etc.
2. Include a module docstring explaining the topic
3. Provide 4–6 functions to implement, each with:
   - A clear docstring explaining the problem
   - Doctest examples showing expected input/output
   - A `# TODO: Implement this` marker
4. Include a `test()` function at the bottom with assertions
5. Add `if __name__ == "__main__": test()` so they can run it immediately

**Exercise template:**
```python
"""
Exercise NN: Topic Name
=======================
Topics: comma-separated list
"""


def function_name(args) -> return_type:
    """
    Clear description of what to do.

    >>> function_name(example_input)
    expected_output
    """
    # TODO: Implement this
    pass


def test():
    assert function_name(...) == ...
    print("All tests passed!")


if __name__ == "__main__":
    test()
```

**Rules for exercises:**
- Each function should teach ONE concept
- Include edge cases in the test function (empty inputs, negative numbers, etc.)
- Do NOT provide the solution — only `pass` or a partial stub
- Import statements should be at the top
- Type hints are encouraged
- Keep each file under 150 lines

### 3. Run and verify

After creating exercises, run each one to confirm the tests fail as expected (since the functions are not yet implemented). If a test passes unexpectedly, the exercise is too easy — rewrite it.

### 4. Review user's completed work

When the user asks you to check their work:
1. Run the file: `python <exercise_file.py>`
2. If tests pass: confirm success, explain what they did well
3. If tests fail:
   - Identify which assertion failed
   - Explain the error in plain language
   - Give a hint (not the full solution) pointing toward the fix
   - If they're stuck after 2 hints, show a minimal correct example

**Review format:**
```
## Exercise NN Review

| Function | Status | Notes |
|----------|--------|-------|
| func_a | Pass | Clean implementation |
| func_b | Fail | Off-by-one error in loop range |
| func_c | Not done | — |

**func_b hint:** Your loop includes the endpoint when it shouldn't. Remember that `range(a, b)` goes up to `b-1`.
```

### 5. Track progress

Maintain a `progress.json` file in the exercises folder:

```json
{
  "current_exercise": "02_functions.py",
  "completed": ["01_basics.py"],
  "in_progress": ["02_functions.py"],
  "topics_covered": ["basics"],
  "next_topic": "data_structures"
}
```

Update it after each review session. Show the user their progress when they ask.

## Multi-file exercise sets

When generating a batch of exercises (e.g., a full learning path):
1. Create a `README.py` or `README.md` in the folder explaining the order
2. Number files sequentially
3. Make later exercises depend on earlier concepts (e.g., exercise 05 imports functions from exercise 03)

## Interactive features

When the user asks for help mid-exercise:
- **"I'm stuck"** → Give a targeted hint, not the full solution
- **"Explain this concept"** → Teach the concept with a minimal example, then relate it back to their exercise
- **"Show me the solution"** → Only after they've made 2+ attempts. Walk through the solution line by line explaining the reasoning.
- **"Give me a harder exercise"** → Add edge cases, require error handling, or combine multiple concepts
- **"Give me an easier one"** → Reduce to a single concept, add more scaffolding

## Example: Generating an exercise

**User says:** "I want to practice decorators"

**You generate:** `04_decorators.py` with functions like:
- `timer` — measure function execution time
- `retry` — retry on failure N times
- `cache_results` — simple memoization
- `require_types` — validate argument types

Each has tests. You tell the user: "Run `python 04_decorators.py` to see which tests fail, then fill in the implementations."

## Example: Reviewing completed work

**User says:** "check my 02_functions.py"

**You do:**
1. Run the file
2. See that `sum_all` fails with `TypeError`
3. Report: "`sum_all` has a bug — you're initializing `sum` as a list `[]` but trying to add integers to it. Initialize it as `0` instead."
4. After they fix it, run again
5. Report: "All tests pass now! Good work. Ready for exercise 03?"
