# Python Topics Catalog

Based on [A Byte of Python](https://python.swaroopch.com/) by Swaroop C H.
Learning path is split into phases, moving from syntax → OOP → stdlib → real-world.

---

## Phase 1: Core Python Syntax

Goal: Be comfortable writing small scripts. Every concept gets BOTH completion AND debug exercises.

### 01_basics
Variables, types (int, float, str, bool), print, input, string formatting, comments.

### 02_operators_expressions
Arithmetic, comparison, logical, assignment, shortcut operators, operator precedence, evaluation order.

### 03_control_flow
if/elif/else, while, for, break, continue, range, pass, truth value testing.

### 04_functions
Defining functions, local/global scope, default arguments, keyword arguments, return, docstrings.

### 05_modules
import, from...import, __name__ == '__main__', creating modules, module search path, packages.

### 06_data_structures
Lists, tuples, dictionaries, sets, sequences, slicing, references vs copies, string methods, comprehensions.

---

## Phase 2: OOP & Intermediate Concepts

Goal: Write well-structured, reusable code. Introduction to Pythonic patterns.

### 07_oop
Classes, __init__, self, class vs instance variables, inheritance, polymorphism, method overriding, @classmethod, @staticmethod, encapsulation, dunder methods (__str__, __repr__, __eq__, __len__, __add__, etc.).

### 08_io
File reading/writing, with statement, JSON, CSV, pathlib, binary files.

### 09_exceptions
try/except/else/finally, raising exceptions, custom exceptions, EAFP philosophy.

### 10_more_pythonic
Decorators, generators, iterators, list/dict/set comprehensions, lambda, map/filter/reduce, context managers, namedtuple, dataclasses.

---

## Phase 3: Standard Library & Ecosystem

Goal: Use Python for real tasks. Explore domains: DevOps, Data, AI/ML.

### 11_stdlib_essentials
os, sys, pathlib, datetime, collections (Counter, defaultdict, deque), itertools, functools, re, json, argparse, logging, typing.

### 12_data_handling
Requests, BeautifulSoup, pandas basics, CSV/Excel processing, SQL with sqlite3.

### 13_devops_automation
Subprocess, pathlib for file ops, paramiko/pexpect basics, docker SDK basics, environment variable management, config parsing.

### 14_ml_ai_foundation
NumPy basics, matplotlib/seaborn basics, scikit-learn intro (train_test_split, fit/predict), Jupyter notebook basics.

---

## Phase 4: Real-World & Open Source

Goal: Read, understand, and contribute to real codebases.

### 15_reading_code
Analyzing open-source repos: reading README, understanding project structure, tracing function calls, reading tests.

### 16_contributing
Forking, cloning, setting up dev environment, writing tests, making PRs, code review etiquette.

---

## Exercise Mix Rules

For every topic, generate a mix of:
- **60% completion exercises** — function stub with `# TODO`, user implements
- **40% debug exercises** — broken code with bugs, user fixes

Comments are the primary instruction mechanism. Each exercise file should have:
1. A header comment explaining the topic
2. Inline comments before each exercise explaining what to do
3. Docstrings with examples

---

## Default Progressive Path

If user has no preference, start at Phase 1 and move sequentially.
Do NOT skip phases. User must demonstrate comfort before advancing.

Current exercise numbering:
- Phase 1: 01_ through 06_
- Phase 2: 07_ through 10_
- Phase 3: 11_ through 14_
- Phase 4: 15_ through 16_
