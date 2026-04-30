# Python Practice Topic Catalog

Use this catalog to choose topics and difficulty. The default goal is broad
Python fluency, with backend, frameworks, AWS automation, CLIs, and data
utilities as application tracks.

## Topic List

### 1. Foundations

Core Python syntax and built-in behavior.

Sub-topics:
- variables, types, operators
- control flow
- functions, args, kwargs, scope
- modules and imports
- lists, dicts, tuples, sets
- comprehensions
- strings and formatting
- exceptions
- file I/O basics

### 2. OOP And Design

Object-oriented Python and maintainable package boundaries.

Sub-topics:
- classes and objects
- `__init__`, instance variables, class variables
- methods, classmethods, staticmethods
- inheritance and composition
- dunder methods
- dataclasses
- properties
- abstract base classes
- protocols and structural typing
- dependency boundaries

### 3. Standard Library

Production-useful built-in modules.

Sub-topics:
- `pathlib`, `os`, `sys`, `shutil`
- `datetime`, `zoneinfo`, `time`
- `collections`
- `itertools`, `functools`
- `json`, `csv`
- `re`
- `argparse`
- `logging`
- `subprocess`
- `concurrent.futures`
- `asyncio` basics

### 4. Testing And Quality

Confidence-building Python workflows.

Sub-topics:
- pytest basics
- fixtures
- parametrization
- monkeypatch
- mocking with `unittest.mock`
- fakes vs mocks
- testing exceptions
- testing CLIs and HTTP boundaries
- type hints
- protocols
- lint-friendly design

### 5. Backend Python

Backend design independent of any one framework.

Sub-topics:
- HTTP request/response mental model
- routing
- validation
- service layer boundaries
- repository/client interfaces
- error-to-status mapping
- configuration
- middleware concepts
- background tasks
- pagination
- authentication/authorization concepts

### 6. FastAPI

Modern typed API development.

Sub-topics:
- path operations
- request and response models
- Pydantic validation
- dependency injection
- routers
- exception handlers
- middleware
- background tasks
- testing with dependency overrides
- async vs sync handlers

### 7. Flask

Small web apps and service foundations.

Sub-topics:
- app factory pattern
- blueprints
- request and response handling
- config
- error handlers
- before/after request hooks
- testing Flask apps
- separating routes from services
- avoiding global mutable state

### 8. CLI And Automation

Practical scripts and developer tools.

Sub-topics:
- argparse
- environment variables
- config files
- exit codes
- stdout/stderr behavior
- file walking
- subprocess boundaries
- logging
- dry-run behavior
- idempotent scripts

### 9. AWS Automation

Python for AWS operational workflows.

Sub-topics:
- boto3 client/resource mental model
- sessions and regions
- paginators
- waiters
- retries and throttling
- IAM-safe filtering
- dry-run planning
- idempotent create/update/delete flows
- S3 inventory-style tasks
- EC2/resource cleanup-style tasks
- Lambda packaging/config-style tasks
- CloudWatch logs/metrics collection-style tasks

### 10. Data Utilities

Useful data transformation without becoming a pure data-science track.

Sub-topics:
- CSV/JSON transforms
- report generation
- grouping and aggregation
- pandas basics when useful
- validation and cleaning
- streaming large files
- simple charts only when needed

### 11. Advanced Python

Use after the basics are stable.

Sub-topics:
- decorators
- context managers
- descriptors
- metaclasses intro
- generators
- async programming
- packaging with `pyproject.toml`
- performance profiling
- caching
- plugin-style architecture

## Difficulty Levels

Level 1:
- Single concept.
- Small functions or scripts.
- Clear tests.
- Standard library preferred.

Level 2:
- Combine 2-3 concepts.
- Add error handling and edge cases.
- Introduce pytest or module boundaries.

Level 3:
- Realistic script, CLI, backend handler, framework slice, or AWS automation task.
- Multiple functions/classes.
- Tests cover failure paths.

Level 4:
- Small project or package.
- Framework or AWS-shaped boundaries.
- Config, testing, errors, and idempotency matter.

## Topic Selection Rules

For broad Python fluency, rotate through:
- Foundations
- OOP and package design
- Standard library
- Testing
- CLI/automation
- Backend slices

For backend Python, rotate through:
- Backend Python
- FastAPI
- Flask
- Testing and quality
- OOP/design boundaries

For AWS automation, rotate through:
- CLI and automation
- AWS automation
- Testing with fakes/mocks
- Error handling and retries
- Data/report utilities

For FastAPI:
- Teach typed boundaries, dependency injection, validation, and tests.
- Avoid making every exercise async unless async behavior is the point.

For Flask:
- Teach app factory, blueprints, request handling, config, and tests.
- Avoid global mutable state unless the exercise is about fixing it.
