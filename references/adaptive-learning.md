# Adaptive Exercise Generation

The skill learns from the user's mistakes and strengths over time to provide personalized exercises.

## Learning Profile

The progress tracker maintains a `learning_profile`:

```json
{
  "learning_profile": {
    "strongest_topics": ["fundamentals", "oop"],
    "weakest_topics": ["stdlib"],
    "common_bug_types": ["type_error", "off_by_one", "missing_return"],
    "recommended_focus": [
      "Practice more debug exercises targeting: type_error, off_by_one",
      "Review topics: stdlib"
    ]
  }
}
```

## How It Works

### 1. Recording Mistakes

During review, when a user makes a mistake, record it:

```bash
python scripts/progress_tracker.py <dir> mistake <file> <bug_type> <description>
```

Example:
```bash
python scripts/progress_tracker.py python-exercises/ mistake \
  02_fundamentals_funcs_debug.py type_error \
  "Initialized total as [] instead of 0"
```

### 2. Recording Strengths

When a user demonstrates mastery, record it:

```bash
python scripts/progress_tracker.py <dir> strength <file> <concept>
```

Example:
```bash
python scripts/progress_tracker.py python-exercises/ strength \
  01_fundamentals_vars_complete.py "list_comprehensions"
```

### 3. Automatic Analysis

The tracker automatically updates the learning profile by analyzing:
- **Bug type frequency**: Which bugs occur most often
- **Topic weakness ratio**: mistakes / completions per topic
- **Exercise attempts**: How many tries before success
- **Time spent**: Patterns in completion time

### 4. Personalized Recommendations

Get adaptive suggestions:

```bash
python scripts/progress_tracker.py <dir> recommend
```

Returns:
```json
{
  "focus_areas": ["Practice more debug exercises targeting: type_error"],
  "suggested_exercise_mix": {"complete": 1, "debug": 2},
  "difficulty_adjustment": {
    "fundamentals": "ready_to_advance",
    "oop": "maintain",
    "stdlib": "consider_lowering"
  }
}
```

## Adaptive Exercise Rules

### Exercise Mix Adjustment

Based on learning profile, adjust the 3-exercise batch:

| Pattern | Complete | Debug | Reasoning |
|---------|----------|-------|-----------|
| User struggles with bugs | 1 | 2 | More practice identifying/fixing bugs |
| User strong, few mistakes | 2 | 1 | More challenging completion exercises |
| New topic, no data | 2 | 1 | Default balanced mix |
| Weak topic identified | 1 | 2 | Extra practice on weak area |

### Difficulty Adjustment

| Pattern | Action |
|---------|--------|
| Avg mistakes > 1.5 per exercise | Consider staying at current level or lowering |
| Avg mistakes < 0.5 per exercise | Ready to advance difficulty |
| 0.5–1.5 mistakes per exercise | Maintain current difficulty |

### Topic Selection

When user doesn't specify a topic, suggest based on profile:

1. If weakest_topics exists → recommend weakest topic first
2. If no weak topics → suggest advancing to next major topic
3. If user is advanced → suggest mixing topics or open source

### Personalized Comments in Exercises

When generating exercises for a user with history, add personalized comments:

```python
"""
Exercise 05: Fix the Data Processor
====================================
...

Note: You've shown strength with list comprehensions!
This exercise focuses on error handling — an area to build confidence.
"""
```

Or for weak areas:

```python
"""
...

Note: This exercise targets 'type initialization' — 
remember to check what type your accumulator variable should be!
"""
```

## Review Adaptations

During review, reference the user's history:

- **For recurring mistakes**: "I see you've had trouble with type initialization before. Let's look at line 12 again — what type should `total` be?"

- **For strengths**: "Great use of list comprehension — that's become one of your strengths!"

- **For improvement**: "Nice! Last time this bug type took 2 attempts, but you got it on the first try this time."

## Long-term Goals

Over time, the skill should:

1. **Identify patterns**: "You often miss edge cases with empty inputs"
2. **Celebrate growth**: "Your accuracy on debug exercises improved from 40% to 80%!"
3. **Suggest challenges**: "You're ready for exercises that combine OOP with error handling"
4. **Recommend reading**: "Since you mastered functions, check out this open-source project's function design"
5. **Prepare for open source**: "Your debugging skills are strong — let's practice reading real code next"
