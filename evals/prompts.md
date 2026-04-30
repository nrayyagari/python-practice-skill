# Python Practice Skill Eval Prompts

Use these prompts to spot-check behavior after skill changes.

## Generate Beginner Exercises

Prompt:
```text
I want to practice Python functions and lists. Give me beginner exercises.
```

Expected:
- Creates exercises under `/home/laborant/repos/python-practice/<D-mmm-YY>/`.
- Uses `Difficulty: 1/5` or `Difficulty: 2/5`.
- Includes tests that fail before user work.
- Does not include full solutions.

## Generate Advanced Backend Exercises

Prompt:
```text
Give me advanced backend Python practice around validation, service boundaries, and pytest.
```

Expected:
- Chooses backend/testing framing.
- Uses `Difficulty: 3/5` or higher.
- Creates package or module exercises with tests.
- Keeps dependencies light unless framework behavior is the point.

## Review Broken Solution

Prompt:
```text
Review my solution for today's Python exercise.
```

Expected:
- Runs the exercise verification command.
- Reports correctness before style.
- Updates `/home/laborant/repos/python-practice/learning-log.md`.
- Gives hints or findings without rewriting the whole solution unless asked.

## Adapt From Learning Log

Prompt:
```text
Use my learning log and make the next Python batch.
```

Expected:
- Reads the root learning log.
- Targets repeated mistakes or clarifying questions.
- Explains why the exercises were selected.

## Append Same-Day Exercises

Prompt:
```text
Add more Python exercises for today.
```

Expected:
- Uses the existing date folder if present.
- Continues numbering from the highest existing exercise number.
- Does not create a second folder for the same date.
