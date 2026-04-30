---
name: python-practice
description: >
  Generate interactive Python coding exercises with a mix of "complete the code"
  and "debug this code" problems. Reviews completed solutions and tracks progress
  through a phased learning path (Core Syntax → OOP → Standard Library → Open Source).
  Use whenever the user wants to practice Python, learn a Python concept, do coding
  exercises, debug Python code, improve Python skills, or mentions anything about
  Python practice, coding challenges, Python exercises, or learning Python.
  Also trigger for specific topics: variables, functions, loops, data structures,
  OOP, file I/O, exceptions, decorators, generators, standard library, or open source.
---

# Python Practice

Generate hands-on Python exercises following [A Byte of Python](https://python.swaroopch.com/).
Each exercise file mixes **code completion** (fill in the blank) with **debugging**
(broken code to fix). User edits the file, runs it, and you review.

Ultimate goal: read and contribute to real Python open-source projects.

## When to use

- User wants to practice Python or learn a new concept
- User asks for exercises on a specific topic
- User asks you to review their Python code
- User mentions "coding challenge", "exercise", "practice", "debug", "fix this code"
- User wants to learn from open-source repos

## Workflow

### 1. Assess topic and phase

Read `references/topic-catalog.md` for the full phased learning path.

**Phases:**
- **Phase 1** — Core Syntax (basics → operators → control flow → functions → modules → data structures)
- **Phase 2** — OOP & Intermediate (classes → I/O → exceptions → decorators/generators)
- **Phase 3** — Standard Library & Ecosystem (stdlib → data handling → DevOps → ML/AI)
- **Phase 4** — Real-World & Open Source (reading codebases → contributing)

Ask the user:
- What topic do they want to practice? (or pick the next one in their path)
- Are they ready to advance to the next phase? (check progress.json)

### 2. Generate exercises

Find or create the exercises folder:
```
<workspace>/python-exercises/
```

Read `references/exercise-templates.md` for the exact file structure, rules, and debug patterns.

**Key requirements:**
- Name files sequentially: `01_basics.py`, `02_operators.py`, etc.
- Mix: ~60% completion exercises, ~40% debug exercises
- Comments are instructions — explain what to do, not how
- Every debug exercise has a `# BUG:` or `# FIXME:` comment
- 4–6 exercises per file, 80–150 lines total
- Include reference to the swaroopch chapter in the header
- A `test()` function with assertions at the bottom

### 3. Verify exercises fail correctly

Run the generated file:
```bash
python <exercise_file.py>
```

Tests should fail (since exercises aren't solved yet). If any pass unexpectedly, rewrite.

### 4. User works, then requests review

The user edits the file and either:
- Runs it themselves and reports results
- Asks you to validate

### 5. Review

Run the file. Read `references/review-guide.md` for:
- Review format (table with exercise type, status, notes)
- Hint policy (progressive — never give full solution immediately)
- Debug exercise review checklist
- Phase advancement criteria

**Review output format:**
```
## Exercise NN Review

| Exercise | Type | Status | Notes |
|----------|------|--------|-------|
| 1 | Complete | Pass | Clean implementation |
| 2 | Debug | Fail | Found 1 of 2 bugs — check line 23 |

**Exercise 2 hint:** ...
```

### 6. Track progress

Use the progress tracker script:
```bash
python scripts/progress_tracker.py <exercises_dir> <command> [args]
```

Commands: `show`, `start <file>`, `complete <file> <topic>`, `next-topic <topic>`

Updates `progress.json`:
```json
{
  "current_exercise": "02_operators.py",
  "completed": ["01_basics.py"],
  "in_progress": ["02_operators.py"],
  "topics_covered": ["basics"],
  "phase": 1,
  "next_topic": "control_flow"
}
```

### 7. Phase advancement

Before moving to the next phase:
- User must complete 80%+ of current phase exercises
- User explains solutions in their own words
- Ask 2–3 oral questions about the topic

## Phase 4: Open Source

When user reaches Phase 4:
1. Pick a beginner-friendly Python repo (httpie, requests, rich, typer, etc.)
2. Guide them to read README, CONTRIBUTING.md, set up dev env
3. Have them trace a feature end-to-end through the codebase
4. Find a "good first issue" and implement a fix or test
5. Review their PR before they submit

## Interactive help

- **"I'm stuck"** → Targeted hint, not full solution
- **"Explain this concept"** → Minimal example + relate to their exercise
- **"Show me the solution"** → Only after 2+ attempts. Walk through reasoning.
- **"Give me harder exercises"** → More edge cases, combine concepts
- **"Give me an easier one"** → Single concept, more scaffolding
