# Topic Catalog

## Major Topics

When the user asks for exercises, present these 4 major categories:

### 1. Fundamentals
Core Python syntax and built-in features.

**Sub-topics:**
- Variables, types, operators
- Control flow (if/else, loops)
- Functions (def, args, kwargs, scope)
- Modules and imports
- Data structures (lists, dicts, tuples, sets, comprehensions)
- String manipulation and formatting
- File I/O basics

**Difficulty progression:**
- Level 1: Single concept, straightforward implementation
- Level 2: Combine 2 concepts, add error handling
- Level 3: Real-world scenario, edge cases, performance considerations

### 2. OOP
Object-oriented programming and Pythonic patterns.

**Sub-topics:**
- Classes and objects
- __init__, self, instance variables
- Class variables and methods
- Inheritance and polymorphism
- Dunder methods (__str__, __repr__, __eq__, __len__, etc.)
- Encapsulation and property decorators
- Abstract base classes
- Dataclasses

**Difficulty progression:**
- Level 1: Basic class with methods
- Level 2: Inheritance, method overriding, class methods
- Level 3: Complex hierarchies, mixins, metaclasses intro

### 3. Standard Library
Python's built-in modules for common tasks.

**Sub-topics:**
- os, sys, pathlib
- datetime, time
- collections (Counter, defaultdict, deque, namedtuple)
- itertools, functools
- re (regular expressions)
- json, csv
- argparse, logging
- typing module
- unittest / pytest basics

**Difficulty progression:**
- Level 1: Use a single module for a simple task
- Level 2: Combine multiple stdlib modules
- Level 3: Build a small CLI tool or utility using stdlib

### 4. Popular Libraries
Widely-used third-party libraries.

**Sub-topics:**
- requests (HTTP)
- BeautifulSoup / lxml (web scraping)
- pandas (data manipulation)
- numpy (numerical computing)
- matplotlib / seaborn (visualization)
- pytest (advanced testing)
- click / argparse (CLI building)
- sqlalchemy (databases)
- flask / fastAPI (web frameworks intro)

**Difficulty progression:**
- Level 1: Basic usage of the library
- Level 2: Combine library with Python fundamentals
- Level 3: Build a small project using the library

---

## Exercise Delivery Rules

### Batch Size
Always generate **3 exercises per request**.

### Difficulty Escalation
Track difficulty per topic in progress.json:
```json
{
  "topic_difficulty": {
    "fundamentals": 1,
    "oop": 1
  }
}
```

- First request on a topic → Level 1
- Second request on same topic → Level 2
- Third+ request on same topic → Level 3

### File Naming
One file per exercise:
```
01_fundamentals_vars_debug.py
02_fundamentals_funcs_complete.py
03_fundamentals_lists_debug.py
04_fundamentals_files_complete.py
05_fundamentals_dicts_debug.py
06_fundamentals_comprehensions_complete.py
```

Format: `NN_<topic>_<subtopic>_<type>.py`

- `NN` — global sequential number across all exercises
- `topic` — fundamentals / oop / stdlib / popular
- `subtopic` — brief descriptor
- `type` — `complete` (fill in code) or `debug` (fix broken code)

### Exercise Mix per Batch
Each batch of 3 should have:
- At least 1 debug exercise
- At least 1 complete exercise
- Mix of sub-topics within the major topic

### File Size
Each exercise file: 30–80 lines.
