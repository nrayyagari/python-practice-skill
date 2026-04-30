# Python Solution Review Guide

Review in this order.

## 0. Severity

Classify findings so the user learns what matters most.

- `blocker`: incorrect behavior, unsafe AWS action, broken idempotency, swallowed
  critical error, test suite cannot run, security-sensitive bug, or API behavior
  that returns the wrong result/status.
- `major`: unclear package boundary, overbroad mock, missing error-path test,
  validation in wrong layer, missing retry/backoff, missing dry-run, or brittle
  framework/AWS behavior.
- `minor`: naming, small simplification, style, formatting, weak but noncritical
  test readability, or a more Pythonic idiom.

Do not let minor style comments bury correctness or production concerns.

## 1. Verification

For package exercises:

```bash
python -m pytest
```

For single-file exercises:

```bash
python <exercise_file.py>
```

Run from the date folder or package folder specified by the exercise.

## 2. Correctness

Check:
- Handles empty inputs and edge cases.
- Does not mutate inputs unless documented.
- Returns useful errors or raises the intended exception.
- Avoids hidden global state.
- Uses filesystem/network/AWS boundaries safely.
- Keeps framework handlers thin when applicable.
- Tests cover success and failure paths.

## 3. Idiomatic Python

Check:
- Clear names.
- Small functions.
- List/dict comprehensions where they improve clarity.
- `enumerate`, `zip`, `sum`, `any`, `all`, `dict.get`, and context managers where appropriate.
- `pathlib` for path-heavy code.
- Specific exceptions instead of bare `except`.
- Type hints on public functions when useful.
- Dataclasses or Pydantic models only where they clarify structure.

## 4. Backend/Framework/AWS Review

Backend:
- Validation happens before side effects.
- Route/controller logic is separated from business logic.
- Errors map to useful response/status behavior.
- Dependencies are injectable and testable.

FastAPI:
- Dependencies are used intentionally, not as hidden globals.
- Pydantic models represent request/response boundaries.
- Tests use dependency overrides when external clients are involved.

Flask:
- App factory pattern is preferred for testability.
- Blueprints split route groups when useful.
- Global mutable state is avoided.
- Tests use Flask test client.

AWS automation:
- No real AWS calls unless requested.
- Paginators are handled.
- Retries have max attempts and testable backoff.
- Dry-run mode exists for destructive actions.
- Operations are idempotent where possible.
- IAM/resource filters are explicit and narrow.

## 5. Learning Log Update

After review, update `/home/laborant/repos/python-practice/learning-log.md` with:
- Date folder.
- Completed exercise names.
- Mistakes observed.
- Clarifying questions user asked.
- Concepts mastered.
- Next recommended topic.

Keep entries specific. Prefer:

```markdown
- Mistake: `boto3-pagination-missing` in S3 inventory exercise. Only processed first page from paginator.
```

Over:

```markdown
- Needs AWS practice.
```

## Hint Policy

| Attempt | Response |
|---------|----------|
| 1st failure | Explain the error/traceback in plain language |
| 2nd failure | Point to the specific line, give a conceptual hint |
| 3rd+ failure | Show a minimal example of the pattern, ask them to apply it |

Do not give the full solution unless the user explicitly asks to see it. When
they do ask, provide the smallest complete solution and explain the key idea.

## Review Response Template

```text
Result: <pass/fail>

Tests:
- <test result>

Findings:
- [<severity>] <specific issue and file/line if available>

Idiomatic Python:
- <improvement>

Backend/framework/AWS note:
- <production implication>

Learning log updated:
- <new mistake/question/strength>

Next:
- <recommended next exercise focus>
```
