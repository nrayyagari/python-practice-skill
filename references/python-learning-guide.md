# Python Learning Guide

A comprehensive, structured Python learning path based on the tech-learning-guide framework.
Used by the python-practice skill to design exercises, set expectations, and guide progression.

---

## Section 1 — Overview & Concept Map

Python is a high-level, interpreted language known for readability and versatility. It dominates
web development, data science, automation, DevOps, and AI/ML. Learning Python well means learning
to write **idiomatic, Pythonic code** — not just code that works.

### 🟢 Basics (Learn First)

| Concept | Description |
|---------|-------------|
| Variables & Types | int, float, str, bool, None. Dynamic typing basics. |
| Operators | Arithmetic, comparison, logical, assignment, membership (`in`) |
| Control Flow | if/elif/else, while, for, break, continue, pass |
| Functions | def, return, parameters, arguments, scope |
| Modules | import, from, __name__, creating modules |
| Lists & Tuples | Creation, indexing, slicing, methods, immutability |
| Dictionaries & Sets | Key-value pairs, hashing, set operations |
| Strings | Formatting (f-strings), methods, slicing, encoding |
| File I/O | open, read, write, with statement, pathlib |

### 🔵 Foundational (Day-to-Day Working Knowledge)

| Concept | Description |
|---------|-------------|
| Type Hints | str, int, list[T], dict[K,V], Optional, Union, generics |
| List/Dict Comprehensions | `[x for x in items]`, `{k:v for k,v in pairs}` |
| Generators | yield, generator expressions, lazy evaluation |
| Decorators | @timer, @property, functools.wraps, parameterized decorators |
| Context Managers | __enter__/__exit__, @contextmanager, with |
| OOP | Classes, inheritance, polymorphism, dunder methods, dataclasses |
| Error Handling | try/except/else/finally, custom exceptions, EAFP |
| Iterators | __iter__, __next__, itertools, zip, enumerate |
| Standard Library | os, sys, datetime, collections, json, re, logging |
| Testing | pytest, fixtures, parametrize, mocking with unittest.mock |

### 🔴 Advanced (Production & Scale)

| Concept | Description |
|---------|-------------|
| Concurrency | threading, multiprocessing, asyncio, GIL, locks, queues |
| Parallel Processing | concurrent.futures, Joblib, Dask, process pools |
| Performance | Profiling (cProfile), caching (lru_cache), complexity analysis |
| Metaclasses & Descriptors | __metaclass__, __get__, __set__, __slots__ |
| Design Patterns | Singleton, Factory, Observer, Strategy, DI in Python |
| Network Programming | Sockets, HTTP, WebSockets, async networking |
| Database Patterns | ORM (SQLAlchemy), connection pooling, migrations |
| Web Frameworks | Flask/FastAPI, middleware, auth, REST design |
| Data Science Stack | NumPy, Pandas, Matplotlib, scikit-learn basics |
| DevOps & Packaging | Docker, CI/CD, pytest, poetry, setuptools |

---

## Section 2 — Weekly Learning Schedule

### Phase 1: Core Syntax (Weeks 1–4)

**Week 1: Variables, Types & Operators**
- Day 1: Variables, assignment, dynamic typing
- Day 2: Numbers (int, float), arithmetic, type() and isinstance()
- Day 3: Strings, f-strings, basic methods
- Day 4: Booleans, comparison operators, truthiness
- Day 5: Operators precedence, practical exercises

**Week 2: Control Flow & Functions**
- Day 1: if/elif/else, nested conditions
- Day 2: while loops, break, continue
- Day 3: for loops, range(), iterating over sequences
- Day 4: Functions — def, parameters, return values
- Day 5: Default args, keyword args, *args, **kwargs

**Week 3: Data Structures**
- Day 1: Lists — creation, indexing, methods, mutability
- Day 2: List slicing, list comprehensions
- Day 3: Dictionaries — creation, access, methods
- Day 4: Tuples, sets, frozensets
- Day 5: Dictionary comprehensions, set operations

**Week 4: Modules, File I/O & String Handling**
- Day 1: import, from, __name__, creating modules
- Day 2: Reading files, with statement, pathlib
- Day 3: Writing files, JSON, CSV basics
- Day 4: String methods, formatting, parsing
- Day 5: Putting it together — small file processing script

---

### Phase 2: OOP & Intermediate (Weeks 5–7)

**Week 5: Object-Oriented Programming**
- Day 1: Classes, __init__, self, instance variables
- Day 2: Methods, class variables, @classmethod, @staticmethod
- Day 3: Inheritance, method overriding, super()
- Day 4: Dunder methods — __str__, __repr__, __eq__, __len__
- Day 5: Encapsulation, @property, private variables

**Week 6: Pythonic Patterns**
- Day 1: List/dict/set comprehensions
- Day 2: Generators and yield
- Day 3: zip, enumerate, reversed
- Day 4: EAFP vs LBYL, try/except patterns
- Day 5: functools — partial, reduce, lru_cache

**Week 7: Error Handling, Testing & Type Hints**
- Day 1: try/except/else/finally, exception hierarchy
- Day 2: Custom exceptions, raising exceptions
- Day 3: Type hints basics — str, int, list[T], Optional
- Day 4: pytest basics — writing and running tests
- Day 5: Fixtures, parametrize, test organization

---

### Phase 3: Standard Library & Ecosystem (Weeks 8–10)

**Week 8: Essential Standard Library**
- Day 1: os, sys, pathlib — file system operations
- Day 2: datetime, time — dates, timestamps, formatting
- Day 3: collections — Counter, defaultdict, deque, namedtuple
- Day 4: itertools and functools deep dive
- Day 5: re (regular expressions) basics

**Week 9: Data Handling & CLI Tools**
- Day 1: json, csv — parsing and writing
- Day 2: argparse — building CLI interfaces
- Day 3: logging — configuration, levels, handlers
- Day 4: requests — HTTP basics
- Day 5: BeautifulSoup — web scraping basics

**Week 10: Intermediate Projects**
- Day 1–2: Build a CLI tool using argparse + logging
- Day 3–4: Build a web scraper using requests + BeautifulSoup
- Day 5: Add tests with pytest, refactor for Pythonic style

---

### Phase 4: Real-World & Open Source (Weeks 11–12)

**Week 11: Reading Codebases**
- Day 1: Clone a Python repo (requests, httpie, rich)
- Day 2: Read README, CONTRIBUTING, project structure
- Day 3: Trace a feature end-to-end
- Day 4: Read tests to understand expected behavior
- Day 5: Find a "good first issue"

**Week 12: Contributing**
- Day 1: Set up dev environment
- Day 2: Write a test for the issue
- Day 3: Implement the fix
- Day 4: Run tests, lint, format
- Day 5: Submit PR, respond to review

---

### Phase 5: Advanced Topics (Weeks 13–16)

**Week 13: Concurrency**
- Day 1: threading basics, locks, race conditions
- Day 2: multiprocessing, process pools, shared memory
- Day 3: asyncio basics, event loop, coroutines
- Day 4: async/await, aiohttp
- Day 5: concurrent.futures — ThreadPoolExecutor, ProcessPoolExecutor

**Week 14: Performance & Design Patterns**
- Day 1: cProfile, line_profiler — finding bottlenecks
- Day 2: Caching strategies — lru_cache, memoization
- Day 3: Algorithmic complexity, Big O basics
- Day 4: Singleton, Factory, Observer patterns in Python
- Day 5: Strategy pattern, dependency injection

**Week 15: Web Frameworks & Databases**
- Day 1: FastAPI basics — routes, models, validation
- Day 2: FastAPI — middleware, dependency injection
- Day 3: SQLAlchemy ORM — models, queries, relationships
- Day 4: Database migrations with Alembic
- Day 5: Building a REST API with FastAPI + SQLAlchemy

**Week 16: Data Science & DevOps**
- Day 1: NumPy arrays, broadcasting, vectorization
- Day 2: Pandas — DataFrame, groupby, merge, pivot
- Day 3: Matplotlib/Seaborn — plotting basics
- Day 4: Docker with Python — Dockerfile, docker-compose
- Day 5: CI/CD — GitHub Actions for Python projects

---

## Section 3 — Local Development Setup

### Prerequisites
- Python 3.10+ (check with `python --version`)
- A code editor (VS Code recommended)
- Git

### Installation

```bash
# Ubuntu/Debian
sudo apt update
sudo apt install python3 python3-pip python3-venv git

# macOS
brew install python git

# Verify
python3 --version  # Should be 3.10+
git --version
```

### Virtual Environment (CRITICAL — always use this)

```bash
# Create
python3 -m venv .venv

# Activate
source .venv/bin/activate  # Linux/macOS
.venv\Scripts\activate     # Windows

# Install packages
pip install pytest requests pandas numpy

# Save dependencies
pip freeze > requirements.txt
```

### VS Code Setup
- Install Python extension (Microsoft)
- Enable type checking: `"python.analysis.typeCheckingMode": "basic"`
- Install extensions: autoDocstring, Python Docstring Generator

### Useful Tools
- `black` — code formatter
- `flake8` or `ruff` — linter
- `mypy` — static type checker
- `pytest` — test runner
- `ipython` — enhanced REPL

```bash
pip install black flake8 mypy pytest ipython
```

### Hello World Verification

```python
# hello.py
def greet(name: str) -> str:
    return f"Hello, {name}!"

if __name__ == "__main__":
    print(greet("Python"))
```

```bash
python hello.py
# Output: Hello, Python!
```

---

## Section 4 — Concept Deep-Dives

### 🟢 Variables & Types

**What it is**: Python variables are names bound to objects. Types are checked at runtime.

**Why it matters**: Understanding mutability (lists vs tuples) prevents subtle bugs.

**How it works**:
```python
# Variables are references
a = [1, 2, 3]
b = a        # b references the same list
b.append(4)  # a is now [1, 2, 3, 4]!

# To copy: use slicing or copy module
b = a[:]     # Shallow copy
```

**Common pitfalls**:
- Thinking `a = b` copies the object (it copies the reference)
- Using mutable default arguments: `def f(x=[])`

---

### 🟢 Control Flow

**What it is**: if/else, loops, and iteration control.

**Why it matters**: Every program needs decision-making and repetition.

**How it works**:
```python
# Pythonic iteration
items = [1, 2, 3, 4, 5]

# Bad
for i in range(len(items)):
    print(items[i])

# Good
for item in items:
    print(item)

# With index
for i, item in enumerate(items):
    print(f"{i}: {item}")
```

**Common pitfalls**:
- Modifying a list while iterating over it
- `for` loop `else` clause (executes if no break)

---

### 🟢 Functions

**What it is**: Reusable blocks of code with parameters and return values.

**Why it matters**: Functions are the primary unit of organization in Python.

**How it works**:
```python
def process_data(items: list[int], multiplier: int = 2) -> list[int]:
    """Return items multiplied by multiplier."""
    return [item * multiplier for item in items]

# *args and **kwargs
def flexible(*args: int, **kwargs: str) -> None:
    print(f"Positional: {args}")
    print(f"Keyword: {kwargs}")

flexible(1, 2, 3, name="Alice", age="30")
```

**Common pitfalls**:
- Mutable default arguments
- Not returning values (implicit None)
- Shadowing built-in names

---

### 🔵 List & Dict Comprehensions

**What it is**: Concise syntax for creating lists and dicts from iterables.

**Why it matters**: More readable, often faster, and quintessentially Pythonic.

**How it works**:
```python
# List comprehension
squares = [x**2 for x in range(10)]

# With condition
evens = [x for x in range(10) if x % 2 == 0]

# Dict comprehension
word_lengths = {word: len(word) for word in ["hello", "world"]}

# Nested
matrix = [[i*j for j in range(3)] for i in range(3)]
```

**Common pitfalls**:
- Overly complex comprehensions (hard to read)
- Not using them when appropriate (verbose loops)

---

### 🔵 Generators

**What it is**: Functions that yield values lazily, one at a time.

**Why it matters**: Memory-efficient for large datasets. Core to Python's iteration model.

**How it works**:
```python
def fibonacci(n: int):
    """Generate first n Fibonacci numbers."""
    a, b = 0, 1
    for _ in range(n):
        yield a
        a, b = b, a + b

# Usage
for num in fibonacci(10):
    print(num)

# Generator expression
sum(x**2 for x in range(1000000))  # Memory efficient!
```

**Common pitfalls**:
- Generators can only be iterated once
- Trying to index a generator

---

### 🔵 Decorators

**What it is**: Functions that wrap other functions to add behavior.

**Why it matters**: Cross-cutting concerns (logging, caching, auth) without code duplication.

**How it works**:
```python
import functools
import time

def timer(func):
    """Print execution time of a function."""
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        start = time.time()
        result = func(*args, **kwargs)
        print(f"{func.__name__} took {time.time() - start:.2f}s")
        return result
    return wrapper

@timer
def slow_function():
    time.sleep(1)
```

**Common pitfalls**:
- Forgetting @functools.wraps (loses metadata)
- Not preserving function signature

---

### 🔵 OOP

**What it is**: Organizing code into classes that combine data and behavior.

**Why it matters**: Essential for building maintainable, reusable code.

**How it works**:
```python
from dataclasses import dataclass
from typing import List

@dataclass
class Book:
    title: str
    author: str
    pages: int

class Library:
    def __init__(self):
        self.books: List[Book] = []
    
    def add_book(self, book: Book) -> None:
        self.books.append(book)
    
    def get_by_author(self, author: str) -> List[Book]:
        return [b for b in self.books if b.author == author]
```

**Common pitfalls**:
- Using classes when a simple function would do
- Forgetting `self` in method definitions
- Not calling `super().__init__()` in subclasses

---

### 🔴 Concurrency

**What it is**: Running multiple tasks simultaneously or in overlapping periods.

**Why it matters**: I/O-bound and CPU-bound programs need different concurrency models.

**How it works**:
```python
import asyncio

async def fetch_data(url: str) -> str:
    await asyncio.sleep(1)  # Simulated I/O
    return f"Data from {url}"

async def main():
    urls = ["url1", "url2", "url3"]
    tasks = [fetch_data(url) for url in urls]
    results = await asyncio.gather(*tasks)
    print(results)

asyncio.run(main())
```

**Key distinction**:
- **threading**: For I/O-bound tasks (network, disk). Limited by GIL for CPU.
- **multiprocessing**: For CPU-bound tasks. Spawns separate processes.
- **asyncio**: For many I/O-bound tasks. Single-threaded, cooperative multitasking.

**Common pitfalls**:
- Using threading for CPU-bound work (GIL prevents parallel execution)
- Not awaiting coroutines
- Race conditions without locks

---

## Section 5 — Popular Libraries & Ecosystem

### Web & HTTP
- **requests** — The standard for HTTP. `requests.get(url)`
- **FastAPI** — Modern, fast web framework with automatic API docs
- **Flask** — Lightweight, flexible web framework

### Data Science
- **NumPy** — N-dimensional arrays, broadcasting, vectorized operations
- **Pandas** — DataFrames for tabular data manipulation
- **Matplotlib / Seaborn** — Plotting and visualization
- **scikit-learn** — Machine learning algorithms and utilities

### Testing
- **pytest** — Powerful testing framework with fixtures and plugins
- **Hypothesis** — Property-based testing
- **unittest.mock** — Mocking and patching (stdlib)

### DevOps & Tooling
- **Docker** — Containerize Python apps
- **Poetry** — Modern dependency management and packaging
- **Black / Ruff** — Code formatting and linting
- **mypy** — Static type checking

### Databases
- **SQLAlchemy** — SQL toolkit and ORM
- **psycopg2** — PostgreSQL adapter
- **redis-py** — Redis client
- **pymongo** — MongoDB client

### Async
- **aiohttp** — Async HTTP client/server
- **asyncpg** — Async PostgreSQL

---

## Section 6 — Project Ideas

### Small — CLI Task Manager (1–2 weeks)
**What**: A command-line todo app with add, list, complete, delete commands.
**Concepts**: argparse, file I/O, JSON, functions, error handling
**Why**: Practices core Python with a practical, usable tool.

### Medium — Web Scraper + API (3–4 weeks)
**What**: Scrape a website periodically, store in SQLite, expose via FastAPI.
**Concepts**: requests, BeautifulSoup, SQLite, FastAPI, async, testing
**Why**: Combines multiple real-world skills into one project.

### Stretch — Microservice with Async & Caching (open-ended)
**What**: A small microservice that fetches data from multiple APIs, caches results, serves via FastAPI.
**Concepts**: asyncio, aiohttp, Redis caching, Docker, testing, CI/CD
**Why**: Production-level concerns: performance, reliability, deployment.

---

## Section 7 — What's Next

After completing this guide:

### Adjacent Technologies
- **Rust** — For performance-critical Python extensions
- **Go** — For systems programming and microservices
- **JavaScript/TypeScript** — If doing full-stack web

### Advanced Python Topics
- **Cython** — Writing C extensions for Python
- **PyPy** — Alternative Python interpreter for speed
- **MicroPython** — Python for embedded systems

### Community Resources
- **PyCon** — Annual Python conference (talks on YouTube)
- **Real Python** — High-quality tutorials
- **Python Discord** — Active community for help

---

## Section 8 — Resources

### Official Docs
- [Python Docs](https://docs.python.org/3/) — Comprehensive, searchable
- [PEP 8](https://peps.python.org/pep-0008/) — Style guide
- [Typing Docs](https://docs.python.org/3/library/typing.html) — Type hints

### Books
- *Fluent Python* by Luciano Ramalho — Deep dive into Pythonic code
- *Python Cookbook* by David Beazley — Practical recipes
- *Effective Python* by Brett Slatkin — 90 specific ways to write better Python

### Online Courses
- **Real Python** — Membership with paths and tutorials
- **Talk Python Training** — Podcast + courses by Michael Kennedy
- **Coursera: Python for Everybody** — Dr. Chuck's beginner-friendly course

### YouTube
- **Corey Schafer** — Excellent tutorials on Python + libraries
- **ArjanCodes** — Software design with Python
- **mCoding** — Python internals and advanced topics

### Practice
- **LeetCode** — Algorithm practice (use Python)
- **Exercism** — Mentored coding exercises
- **Codewars** — Gamified coding challenges
- **This skill!** — python-practice generates personalized exercises

---

*This guide serves as the reference document for the python-practice skill's exercise generation and topic progression.*
