---
name: python-practice
description: >
  Generate interactive Python coding exercises with built-in tests, review completed
  solutions, and track learning progress across topics. Use whenever the user wants
  to practice Python, learn a new Python concept, do coding exercises, improve their
  Python skills, or says anything about Python practice, coding challenges, Python
  exercises, or learning Python. Also trigger when the user asks for exercises in a
  specific Python topic like decorators, OOP, generators, error handling, file I/O,
  data structures, or testing.
---

# Python Practice

Generate hands-on Python exercises with self-checking tests. Create exercise files in
a dedicated folder, review the user's solutions, and maintain a progress tracker.

## When to use

- User wants to practice Python
- User asks for exercises on a specific topic
- User wants to learn a new Python concept
- User asks you to review their Python code
- User mentions "coding challenge", "exercise", "practice" in the context of Python

## Workflow

### 1. Assess current level and topic

Ask the user (or infer from context):
- What Python topic do they want to practice?
- What difficulty: beginner, intermediate, or advanced?

**Topic catalog:** Read `references/topic-catalog.md` for the full list of 12 topics,
difficulty levels, and the default progressive learning path.

### 2. Generate exercises

Create a folder for the exercises if it doesn't exist:
```
<workspace>/python-exercises/
```

Or use an existing `python-exercises/` folder if found in the workspace.

**Exercise template:** Read `references/exercise-templates.md` for the exact file
structure, rules, and quality checklist.

Key requirements:
- Name files sequentially: `01_topic.py`, `02_topic.py`, etc.
- Provide 4–6 functions to implement, each with a clear docstring, doctest examples,
  and a `# TODO: Implement this` marker.
- Include a `test()` function at the bottom with assertions.
- Add `if __name__ == "__main__": test()` so they can run it immediately.

### 3. Run and verify

After creating exercises, run each one to confirm the tests fail as expected (since the
functions are not yet implemented). If a test passes unexpectedly, the exercise is too
easy — rewrite it.

### 4. Review user's completed work

When the user asks you to check their work:
1. Run the file: `python <exercise_file.py>`
2. If tests pass: confirm success, explain what they did well.
3. If tests fail: identify which assertion failed, explain the error, give a hint.

**Review guide:** Read `references/review-guide.md` for the review format, hint policy,
common mistakes to watch for, and encouragement patterns.

### 5. Track progress

Use the progress tracker script to maintain state:

```bash
python scripts/progress_tracker.py <exercises_dir> <command> [args]
```

Commands:
- `show` — display current progress
- `start <exercise_file>` — mark exercise as in-progress
- `complete <exercise_file> <topic>` — mark exercise and topic as done
- `next-topic <topic>` — set the next topic to study

The script reads/writes `progress.json` in the exercises directory:

```json
{
  "current_exercise": "02_functions.py",
  "completed": ["01_basics.py"],
  "in_progress": ["02_functions.py"],
  "topics_covered": ["basics"],
  "next_topic": "data_structures"
}
```

Show the user their progress when they ask.

## Multi-file exercise sets

When generating a batch of exercises (e.g., a full learning path):
1. Create a `README.py` or `README.md` in the folder explaining the order.
2. Number files sequentially.
3. Make later exercises depend on earlier concepts where appropriate.

## Interactive help

When the user asks for help mid-exercise:
- **"I'm stuck"** → Give a targeted hint, not the full solution.
- **"Explain this concept"** → Teach with a minimal example, relate back to their exercise.
- **"Show me the solution"** → Only after 2+ attempts. Walk through line by line.
- **"Give me a harder exercise"** → Add edge cases or combine multiple concepts.
- **"Give me an easier one"** → Reduce to a single concept, add more scaffolding.

## Example interaction

**User:** "I want to practice decorators"

**You:** Generate `04_decorators.py` with functions like `timer`, `retry`, `cache_results`,
`require_types`. Tell the user: "Run `python 04_decorators.py` to see which tests fail,
then fill in the implementations."

**User:** "check my 04_decorators.py"

**You:** Run the file, see `cache_results` fails because it doesn't preserve function
metadata. Report: "`cache_results` works but doesn't preserve `__name__` — wrap your
inner function with `@functools.wraps(func)`."
