---
name: python-practice
description: >
  Generate adaptive Python coding exercises that learn from your mistakes and strengths.
  Delivers 3 exercises per request with personalized difficulty and exercise mix.
  Reviews solutions, tracks progress in a markdown learning log, and adapts over time.
  Emphasizes idiomatic Python and best practices verified via Context7.
  Use whenever the user wants to practice Python, learn Python concepts, debug Python code,
  or mentions Python exercises, challenges, or practice. The skill remembers what you
  struggle with and what you excel at, creating a personalized learning experience
  documented in learning-log.md.
---

# Python Practice — Adaptive Learning

Generate personalized Python exercises that adapt to your strengths and weaknesses.
Each request delivers **3 exercises** as separate files.
Mix of **code completion** and **debugging** adjusted based on your learning profile.
Emphasizes **idiomatic Python** and best practices.

## When to use

- User wants to practice Python or learn a new concept
- User asks for exercises on a specific topic
- User asks you to review their Python code
- User mentions "coding challenge", "exercise", "practice", "debug"
- User says anything about learning or improving Python

## Workflow

### Step 1: Ask for the topic (if not specified)

Present the 4 major topics:

```
Which topic would you like to practice?

1. Fundamentals     — variables, functions, loops, data structures
2. OOP             — classes, inheritance, dunder methods, dataclasses
3. Standard Library — os, datetime, collections, itertools, re, json, etc.
4. Popular Libraries — requests, pandas, numpy, pytest, flask, etc.

(DevOps, Data, AI/ML topics available later as you progress)
```

Wait for user to choose. If they name a topic directly, skip this step.

### Step 2: Check learning profile and adapt

Read `references/topic-catalog.md` for sub-topics and difficulty levels.

Check current state:
```bash
python scripts/progress_tracker.py <exercises_dir> show
```

If user has history, read `references/adaptive-learning.md` and apply:
- Adjust exercise mix based on common bug types
- Adjust difficulty based on mistake ratio
- Add personalized comments referencing strengths/weaknesses

Get personalized recommendations:
```bash
python scripts/progress_tracker.py <exercises_dir> recommend
```

### Step 3: Determine difficulty

```bash
python scripts/progress_tracker.py <exercises_dir> difficulty <topic>
```

- First request on a topic → Level 1
- Second request on same topic → Level 2  
- Third+ request on same topic → Level 3
- Adjust based on learning profile recommendations

Set the topic:
```bash
python scripts/progress_tracker.py <exercises_dir> set-topic <topic>
```

### Step 4: Generate 3 personalized exercise files

Read `references/exercise-templates.md` for file format.
Read `references/learning-log.md` for user's history.

**File naming:**
```
NN_<topic>_<subtopic>_<type>.py
```

**Batch composition (adaptive):**

Default: 2 complete + 1 debug

If user has history of struggling with bugs → 1 complete + 2 debug
If user shows strong performance → 2 complete + 1 debug (harder)
If weak topic identified → focus sub-topics on that area

**Personalization in files:**

When user has learning history, add a note in the docstring:

```python
"""
Exercise 05: Fix the Data Processor
====================================
...

💡 Personalized note: You've shown strength with list comprehensions!
This exercise focuses on error handling — an area to build confidence.
"""
```

Or:

```python
"""
...

⚠️ Watch out: Previous exercises showed type initialization bugs.
Double-check your accumulator variable types!
"""
```

**Idiomatic Python emphasis:**

All exercises should teach or reinforce Pythonic patterns:
- Level 1: basic idioms (enumerate, zip, comprehensions)
- Level 2: intermediate (generators, EAFP, collections)
- Level 3: advanced (decorators, context managers, itertools)

Use Context7 to verify idiomatic patterns when explaining concepts.

**File structure:**
- Module docstring with topic, type, difficulty, reference, personalized note
- Function(s) with `# TODO` (complete) or `# BUG:` (debug)
- Test section at bottom
- 30–80 lines per file

### Step 5: Verify exercises fail correctly

Run each generated file:
```bash
python <exercise_file.py>
```

Tests should fail. If any pass unexpectedly, rewrite.

### Step 6: Deliver to user

```
I've created 3 exercises for you on <topic> (Level <N>):

📊 Your learning profile:
- Strongest areas: <list>
- Focus areas: <list>

Exercises:
- NN_<topic>_<sub>_<type>.py  — <description>
- NN_<topic>_<sub>_<type>.py  — <description>
- NN_<topic>_<sub>_<type>.py  — <description>

Edit each file, then run: python <file.py>
Let me know when you're done or if you want me to check your work!
```

### Step 7: User works and requests review

User edits files, runs them, then either:
- Reports results themselves
- Asks you to validate

### Step 8: Review and record learning data

Run all 3 files. Read `references/review-guide.md` for review format.

**After review, record data:**

For each exercise:
```bash
python scripts/progress_tracker.py <dir> complete <file> <attempts>
```

For each mistake found:
```bash
python scripts/progress_tracker.py <dir> mistake <file> <bug_type> "description"
```

For strengths demonstrated:
```bash
python scripts/progress_tracker.py <dir> strength <file> "concept"
```

Update learning log:
```bash
python scripts/progress_tracker.py <dir> update-log
```

**Review with idiomatic Python check:**

When a solution works but isn't idiomatic:
- Praise the working solution first
- Suggest the Pythonic alternative
- Explain WHY it's better (often more readable, efficient, or robust)
- Use Context7 to verify best practices

### Step 9: Show learning log

After each batch, show the user their updated `learning-log.md`:

```bash
cat <exercises_dir>/learning-log.md
```

This markdown file shows:
- 🏆 Strengths
- 🎯 Focus Areas (Weaknesses)
- 📊 Progress Overview
- 📝 Exercise History
- 💡 Idiomatic Python Reminders (personalized)
- 🎯 Next Recommended Steps

### Step 10: Adaptive next steps

After recording data, the learning profile auto-updates.

Get recommendations:
```bash
python scripts/progress_tracker.py <dir> recommend
```

Use this to suggest next actions:
- If weak areas detected → "Let's do another batch focusing on debug exercises"
- If strong performance → "Ready for Level 2? These combine concepts"
- If ready to advance → "You've mastered this! Want to try OOP next?"

## Long-term Adaptation

Over multiple sessions, the skill learns:

| Timeframe | Adaptation |
|-----------|-----------|
| After 1 batch | Basic difficulty adjustment |
| After 3 batches | Bug type pattern recognition |
| After 5 batches | Topic strength/weakness identification |
| After 10 batches | Personalized exercise mix, targeted weak areas |
| After 20 batches | Mastery recommendations, open source readiness |

## Learning Log

The `learning-log.md` file in the exercises directory is the user's personal dashboard.

It is auto-generated and updated after each review. It includes:
- Strengths tracked over time
- Weaknesses with specific bug types
- Progress table per topic
- Exercise history
- Personalized Pythonic reminders
- Next steps

Encourage the user to read it regularly:
```
Your learning log is ready! View it with:
cat python-exercises/learning-log.md
```

## Interactive help

- **"I'm stuck"** → Targeted hint based on your mistake history
- **"Explain this concept"** → Reference your strengths for analogies, use Context7 for accuracy
- **"Show me my progress"** → Display learning-log.md
- **"Why are you giving me these exercises?"** → Explain the adaptive logic
- **"Give me harder/easier"** → Override difficulty or mix
- **"Focus on my weak areas"** → Generate exercises targeting weak topics
- **"Challenge me"** → Generate exercises targeting strong topics with twists
- **"Is this Pythonic?"** → Review code against idiomatic patterns, use Context7

## Open Source Phase

When user's profile shows:
- 3+ topics at Level 3 with <0.3 mistake ratio
- Strong debug skills (catches bugs quickly)
- Good comprehension (explains solutions clearly)
- Comfortable with idiomatic Python

Suggest Phase 4: Read real Python open-source repos.
