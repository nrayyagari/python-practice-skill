# Python Practice Tracks

Use this file to choose applied exercise framing. The default goal is broad
Python fluency. Pick a track based on the user's request and learning log.

## Core Python Fluency

Purpose: become able to build small correct Python programs without friction.

Practice:
- functions and data structures
- exceptions
- comprehensions and iteration
- modules and imports
- files and JSON
- dataclasses and simple classes
- type hints
- pytest basics

Example exercises:
- Config parser with validation.
- Log summarizer with tests.
- Dataclass vs dict modeling drill.
- Exception design drill.
- CSV/JSON transformer.

## Backend Services

Purpose: build production-shaped backend Python independent of one framework.

Practice:
- request validation
- service boundaries
- persistence/client protocols
- error-to-status mapping
- pagination
- dependency injection
- tests around boundaries

Example exercises:
- Service layer for a user lookup API.
- Error mapping from domain errors to HTTP responses.
- Pagination helper with tests.
- Validation boundary refactor.

## FastAPI

Purpose: build typed APIs with clean dependency boundaries.

Practice:
- path operations
- Pydantic models
- dependency injection
- routers
- exception handlers
- middleware
- background tasks
- test dependency overrides

Example exercises:
- FastAPI route with service dependency override.
- Request/response model validation.
- Router split with error handler.
- Background task scheduling boundary.

## Flask

Purpose: build small services and understand classic WSGI app structure.

Practice:
- app factory
- blueprints
- config
- request/response handling
- error handlers
- test clients
- avoiding global mutable state

Example exercises:
- Flask app factory with blueprint.
- Refactor route logic into service function.
- Error handler for domain exception.
- Config-driven endpoint test.

## CLI And Automation

Purpose: build useful scripts and developer tools.

Practice:
- argparse
- env vars
- config files
- logging
- exit codes
- subprocess wrappers
- dry-run mode
- idempotency

Example exercises:
- Deployment log classifier.
- Dry-run file cleanup tool.
- JSON report generator.
- Command runner with timeout and testable boundary.

## AWS Automation

Purpose: write safe Python automation for AWS-shaped workflows.

Practice:
- boto3-shaped clients
- sessions and regions
- paginators
- waiters
- retries and throttling
- IAM-safe filtering
- dry-run planning
- idempotent operations
- test fakes for AWS clients

Example exercises:
- S3 bucket inventory collector using a fake paginator.
- EC2 cleanup planner with dry-run output.
- Lambda config diff reporter.
- CloudWatch log group retention updater with idempotency.
- Retry wrapper for throttled API calls.

Use real AWS calls only when the user explicitly asks and credentials/safety are
clear. Default to fake boto3-shaped clients so exercises are safe and repeatable.

## Data Utilities

Purpose: handle operational data and reports.

Practice:
- CSV/JSON transforms
- grouping and aggregation
- streaming files
- pandas basics when useful
- validation and reporting

Example exercises:
- CI failure report from CSV.
- AWS inventory summary from JSON.
- Streaming log filter.
- Pandas groupby report.

## Capstone Track

Use capstones when the user wants to integrate multiple skills.

Suggested order:
1. CLI utility package.
2. Automation runner with dry-run mode.
3. Flask API.
4. FastAPI API.
5. AWS inventory tool.
6. Backend worker/service boundary.

Each capstone should have phases, tests, and a learning-log checkpoint.
