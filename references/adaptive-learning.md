# Adaptive Learning Rules

This skill adapts by reading and updating `/home/laborant/repos/python-practice/learning-log.md`.
No tracker script, `progress.json`, score database, or hidden dynamic profile.

The goal is broad Python fluency first. Backend services, FastAPI, Flask, AWS
automation, CLIs, and data utilities are application tracks for that fluency.

## What To Track

Track three signals:
- Mistakes in submitted solutions.
- Clarifying questions the user repeatedly asks while solving.
- Domain interest shown by the user's requested exercises.

Mistakes show behavior. Questions show mental model gaps. Use both.

## Mistake Categories

Language:
- `missing-return`
- `type-confusion`
- `mutable-default-arg`
- `late-binding-closure`
- `shadowing-builtin`
- `not-pythonic-loop`
- `unnecessary-global`
- `copy-vs-reference`

Errors and APIs:
- `exception-swallowed`
- `bare-except`
- `wrong-error-type`
- `error-message-not-actionable`
- `validation-after-side-effect`
- `api-boundary-blurry`

Files and automation:
- `path-string-not-pathlib`
- `file-not-closed`
- `json-edge-case-missing`
- `cli-exit-code-wrong`
- `logging-instead-of-returning`
- `script-not-idempotent`

Testing:
- `fixture-scope-confusion`
- `mock-too-broad`
- `assertion-too-weak`
- `test-coupled-to-order`
- `missing-error-path-test`
- `monkeypatch-overuse`

Backend/frameworks:
- `fastapi-dependency-confusion`
- `fastapi-response-model-missing`
- `flask-global-state`
- `flask-app-factory-missing`
- `validation-in-wrong-layer`
- `http-status-mismatch`

AWS automation:
- `boto3-pagination-missing`
- `aws-retry-missing`
- `iam-action-too-broad`
- `dry-run-missing`
- `region-assumption`
- `idempotency-missing`

## Clarifying Question Categories

Record the actual user question when useful, then tag it.

Common tags:
- `dataclass-choice`
- `typing-protocol`
- `exception-design`
- `pytest-fixtures`
- `mock-vs-fake`
- `pathlib-purpose`
- `fastapi-dependencies`
- `fastapi-validation`
- `flask-blueprints`
- `aws-pagination`
- `aws-idempotency`
- `aws-retries`
- `backend-boundaries`

## Adaptation Logic

If same mistake appears twice:
- Generate one focused drill on that concept.
- Add one applied exercise in user's target domain.

If same clarifying question appears twice:
- Start next batch with a small comment block explaining the mental model.
- Include one exercise that forces the distinction.

Question-to-exercise mapping:
- `dataclass-choice` -> compare dict, dataclass, and plain class for a config model.
- `typing-protocol` -> define a small consumer-owned protocol and test with a fake.
- `exception-design` -> convert swallowed errors into actionable domain exceptions.
- `pytest-fixtures` -> choose fixture scope and isolate state across tests.
- `mock-vs-fake` -> replace brittle mocks with a tiny fake implementation.
- `fastapi-dependencies` -> inject service/client through dependency overrides in tests.
- `flask-blueprints` -> split routes into blueprint plus app factory.
- `aws-pagination` -> collect all pages from a boto3-shaped paginator.
- `aws-idempotency` -> run automation twice and assert no duplicate side effects.
- `aws-retries` -> add retry with max attempts and testable sleep/backoff boundary.

If user succeeds twice in a row on a topic:
- Increase level or move toward backend, tooling, AWS automation, data utility,
  or framework framing based on user interest.

If user struggles with tests:
- Keep the implementation small.
- Add one pytest concept per exercise.
- Prefer fakes over heavy mocks unless mocking is the point.

If user targets backend Python:
- Rotate through validation, service boundaries, persistence interfaces,
  framework routing, error handling, and tests.

If user targets AWS automation:
- Rotate through boto3-shaped clients, pagination, retries, dry-run behavior,
  idempotency, IAM-safe filtering, and reporting.

If user targets broad Python fluency:
- Rotate through language fundamentals, OOP, standard library, files, tests,
  CLIs, packages, and applied mini-projects.

## Learning Log Entry Format

```markdown
## YYYY-MM-DD

Focus: <topic/domain>
Date folder: <D-mmm-YY>

Completed:
- <exercise path> — <result>

Mistakes:
- `<tag>`: <specific observation>

Clarifying Questions:
- `<tag>`: "<question>" — <short answer or follow-up need>

Strengths:
- <specific strength>

Next Batch:
- <recommended topic, level, and domain framing>
```
