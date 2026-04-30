#!/usr/bin/env python3
"""
Progress tracker with learning analytics and markdown learning log.

Tracks:
- Completed exercises per topic
- Difficulty levels per topic
- Mistakes made (bug types, concepts struggled with)
- Strengths (concepts mastered quickly)
- Personalized recommendations
- Generates/updates learning-log.md
"""

import json
import sys
import re
from pathlib import Path
from collections import Counter, defaultdict
from datetime import datetime

PROGRESS_FILE = "progress.json"
LEARNING_LOG = "learning-log.md"

TOPICS = [
    "fundamentals", "oop", "stdlib", "popular",
    "concurrency", "parallel_processing", "performance_optimization",
    "advanced_python", "testing_advanced", "design_patterns",
    "networking", "databases_advanced", "web_frameworks",
    "data_science_ml", "devops_automation_advanced", "open_source_mastery"
]

BUG_TYPES = [
    "type_error",
    "off_by_one",
    "missing_return",
    "shadowing_builtin",
    "mutable_default_arg",
    "wrong_operator",
    "logic_inversion",
    "reference_vs_copy",
    "indentation",
    "syntax_error",
    "concept_misunderstanding",
    "not_pythonic"
]


def load_progress(exercises_dir: str) -> dict:
    path = Path(exercises_dir) / PROGRESS_FILE
    if path.exists():
        return json.loads(path.read_text())
    return _default_progress()


def _default_progress() -> dict:
    return {
        "current_topic": None,
        "topic_difficulty": {t: 1 for t in TOPICS},
        "completed_exercises": [],
        "in_progress": [],
        "total_completed": 0,
        "mistakes": {},
        "strengths": {},
        "attempts_per_exercise": {},
        "time_per_exercise": {},
        "learning_profile": {
            "strongest_topics": [],
            "weakest_topics": [],
            "common_bug_types": [],
            "recommended_focus": []
        }
    }


def save_progress(exercises_dir: str, data: dict) -> None:
    path = Path(exercises_dir) / PROGRESS_FILE
    path.write_text(json.dumps(data, indent=2, default=str))


def load_learning_log(exercises_dir: str) -> str:
    path = Path(exercises_dir) / LEARNING_LOG
    if path.exists():
        return path.read_text()
    return _default_learning_log()


def save_learning_log(exercises_dir: str, content: str) -> None:
    path = Path(exercises_dir) / LEARNING_LOG
    path.write_text(content)


def _default_learning_log() -> str:
    return """# Learning Log

> Personalized tracking of Python skills, strengths, and areas for improvement.
> This file is auto-updated after each exercise batch review.

---

## 🏆 Strengths

<!-- STRENGTHS_START -->
<!-- No strengths recorded yet. Complete some exercises! -->
<!-- STRENGTHS_END -->

---

## 🎯 Focus Areas (Weaknesses)

<!-- WEAKNESSES_START -->
<!-- No weaknesses recorded yet. -->
<!-- WEAKNESSES_END -->

---

## 📊 Progress Overview

<!-- PROGRESS_START -->
| Topic | Level | Exercises Completed | Mistakes | Accuracy |
|-------|-------|---------------------|----------|----------|
<!-- PROGRESS_END -->

---

## 📝 Exercise History

<!-- HISTORY_START -->
| Date | Exercise | Topic | Type | Result | Notes |
|------|----------|-------|------|--------|-------|
<!-- HISTORY_END -->

---

## 💡 Idiomatic Python Reminders

### Common Patterns to Remember
- Use `sum()` built-in instead of manual loops for summation
- Prefer list comprehensions over `for` loops for simple transformations
- Use `with` statement for file/resource management
- Prefer EAFP (Easier to Ask Forgiveness than Permission) over LBYL
- Use `enumerate()` instead of `range(len(...))`
- Use `zip()` for parallel iteration
- Use `dict.get()` instead of `if key in dict: ...`

### Your Personal Reminders
<!-- PERSONAL_REMINDERS_START -->
<!-- No personal reminders yet. -->
<!-- PERSONAL_REMINDERS_END -->

---

## 🎯 Next Recommended Steps

<!-- RECOMMENDATIONS_START -->
<!-- Start practicing to get recommendations! -->
<!-- RECOMMENDATIONS_END -->

---

*Last updated: never*
"""


def update_learning_log(exercises_dir: str) -> None:
    """Regenerate learning-log.md based on progress data."""
    data = load_progress(exercises_dir)
    log = load_learning_log(exercises_dir)
    
    # Update strengths
    strengths = []
    for ex_file, concepts in data.get("strengths", {}).items():
        for concept in concepts:
            topic = _extract_topic(ex_file)
            strengths.append(f"- **{topic}**: {concept}")
    
    if strengths:
        strengths_section = "\n".join(strengths)
    else:
        strengths_section = "<!-- No strengths recorded yet. Complete some exercises! -->"
    
    log = _replace_section(log, "STRENGTHS_START", "STRENGTHS_END", strengths_section)
    
    # Update weaknesses
    weaknesses = []
    bug_counts = Counter()
    for ex_file, mistakes in data.get("mistakes", {}).items():
        for mistake in mistakes:
            bug_counts[mistake["bug_type"]] += 1
    
    for bug_type, count in bug_counts.most_common(5):
        weaknesses.append(f"- **{bug_type}**: Made {count} mistake{'s' if count > 1 else ''}")
    
    if weaknesses:
        weaknesses_section = "\n".join(weaknesses)
    else:
        weaknesses_section = "<!-- No weaknesses recorded yet. -->"
    
    log = _replace_section(log, "WEAKNESSES_START", "WEAKNESSES_END", weaknesses_section)
    
    # Update progress overview
    progress_rows = []
    topic_stats = defaultdict(lambda: {"completed": 0, "mistakes": 0})
    
    for ex_file in data.get("completed_exercises", []):
        topic = _extract_topic(ex_file)
        topic_stats[topic]["completed"] += 1
    
    for ex_file, mistakes in data.get("mistakes", {}).items():
        topic = _extract_topic(ex_file)
        topic_stats[topic]["mistakes"] += len(mistakes)
    
    for topic in TOPICS:
        stats = topic_stats[topic]
        level = data.get("topic_difficulty", {}).get(topic, 1)
        completed = stats["completed"]
        mistakes = stats["mistakes"]
        accuracy = f"{((completed - mistakes) / completed * 100):.0f}%" if completed > 0 else "N/A"
        progress_rows.append(f"| {topic} | {level} | {completed} | {mistakes} | {accuracy} |")
    
    if progress_rows:
        progress_section = "| Topic | Level | Exercises Completed | Mistakes | Accuracy |\n|-------|-------|---------------------|----------|----------|\n" + "\n".join(progress_rows)
    else:
        progress_section = "| Topic | Level | Exercises Completed | Mistakes | Accuracy |\n|-------|-------|---------------------|----------|----------|"
    
    log = _replace_section(log, "PROGRESS_START", "PROGRESS_END", progress_section)
    
    # Update personal reminders
    reminders = []
    for bug_type, count in bug_counts.most_common(3):
        reminders.append(f"- ⚠️ **{bug_type}**: Watch out for this pattern in future exercises")
    
    if reminders:
        reminders_section = "\n".join(reminders)
    else:
        reminders_section = "<!-- No personal reminders yet. -->"
    
    log = _replace_section(log, "PERSONAL_REMINDERS_START", "PERSONAL_REMINDERS_END", reminders_section)
    
    # Update recommendations
    _update_learning_profile(data)
    recommendations = data["learning_profile"].get("recommended_focus", [])
    if recommendations:
        rec_section = "\n".join(f"{i+1}. {rec}" for i, rec in enumerate(recommendations))
    else:
        rec_section = "<!-- Keep practicing to get personalized recommendations! -->"
    
    log = _replace_section(log, "RECOMMENDATIONS_START", "RECOMMENDATIONS_END", rec_section)
    
    # Update timestamp
    log = re.sub(r"\*Last updated: .*\*", f"*Last updated: {datetime.now().strftime('%Y-%m-%d %H:%M')}*", log)
    
    save_learning_log(exercises_dir, log)


def _extract_topic(filename: str) -> str:
    """Extract topic from filename like '01_fundamentals_vars_complete.py'."""
    parts = filename.lower().split("_")
    for topic in TOPICS:
        if topic in parts:
            return topic
    return "unknown"


def _replace_section(text: str, start_marker: str, end_marker: str, new_content: str) -> str:
    """Replace content between HTML comment markers."""
    pattern = f"(<!-- {start_marker} -->)[\\s\\S]*?(<!-- {end_marker} -->)"
    replacement = f"<!-- {start_marker} -->\n{new_content}\n<!-- {end_marker} -->"
    return re.sub(pattern, replacement, text)


def mark_complete(exercises_dir: str, exercise_file: str, attempts: int = 1, time_spent: float = 0) -> dict:
    data = load_progress(exercises_dir)
    if exercise_file in data["in_progress"]:
        data["in_progress"].remove(exercise_file)
    if exercise_file not in data["completed_exercises"]:
        data["completed_exercises"].append(exercise_file)
        data["total_completed"] = len(data["completed_exercises"])
    data["attempts_per_exercise"][exercise_file] = attempts
    data["time_per_exercise"][exercise_file] = time_spent
    _update_learning_profile(data)
    save_progress(exercises_dir, data)
    update_learning_log(exercises_dir)
    return data


def mark_in_progress(exercises_dir: str, exercise_file: str) -> dict:
    data = load_progress(exercises_dir)
    if exercise_file not in data["in_progress"]:
        data["in_progress"].append(exercise_file)
    save_progress(exercises_dir, data)
    return data


def record_mistake(exercises_dir: str, exercise_file: str, bug_type: str, description: str) -> dict:
    data = load_progress(exercises_dir)
    if bug_type not in BUG_TYPES:
        bug_type = "concept_misunderstanding"
    if exercise_file not in data["mistakes"]:
        data["mistakes"][exercise_file] = []
    data["mistakes"][exercise_file].append({
        "bug_type": bug_type,
        "description": description,
        "timestamp": datetime.now().isoformat()
    })
    _update_learning_profile(data)
    save_progress(exercises_dir, data)
    update_learning_log(exercises_dir)
    return data


def record_strength(exercises_dir: str, exercise_file: str, concept: str) -> dict:
    data = load_progress(exercises_dir)
    if exercise_file not in data["strengths"]:
        data["strengths"][exercise_file] = []
    data["strengths"][exercise_file].append(concept)
    _update_learning_profile(data)
    save_progress(exercises_dir, data)
    update_learning_log(exercises_dir)
    return data


def get_difficulty(exercises_dir: str, topic: str) -> int:
    data = load_progress(exercises_dir)
    return data["topic_difficulty"].get(topic, 1)


def bump_difficulty(exercises_dir: str, topic: str) -> dict:
    data = load_progress(exercises_dir)
    current = data["topic_difficulty"].get(topic, 1)
    if current < 3:
        data["topic_difficulty"][topic] = current + 1
    save_progress(exercises_dir, data)
    update_learning_log(exercises_dir)
    return data


def set_topic(exercises_dir: str, topic: str) -> dict:
    data = load_progress(exercises_dir)
    data["current_topic"] = topic
    save_progress(exercises_dir, data)
    return data


def _update_learning_profile(data: dict) -> None:
    """Analyze mistakes and strengths to build learning profile."""
    profile = data.setdefault("learning_profile", {})
    
    # Analyze bug types
    all_bugs = []
    for exercise_mistakes in data.get("mistakes", {}).values():
        for mistake in exercise_mistakes:
            all_bugs.append(mistake["bug_type"])
    
    bug_counter = Counter(all_bugs)
    profile["common_bug_types"] = [b for b, _ in bug_counter.most_common(5)]
    
    # Identify weak topics
    topic_mistakes = defaultdict(int)
    for ex_file, mistakes in data.get("mistakes", {}).items():
        topic = _extract_topic(ex_file)
        topic_mistakes[topic] += len(mistakes)
    
    # Identify strong topics
    topic_completions = defaultdict(int)
    for ex_file in data.get("completed_exercises", []):
        topic = _extract_topic(ex_file)
        topic_completions[topic] += 1
    
    profile["weakest_topics"] = []
    profile["strongest_topics"] = []
    
    for topic in TOPICS:
        mistakes = topic_mistakes.get(topic, 0)
        completions = topic_completions.get(topic, 0)
        if completions > 0:
            ratio = mistakes / completions
            if ratio > 0.5:
                profile["weakest_topics"].append(topic)
            elif ratio < 0.2 and completions >= 3:
                profile["strongest_topics"].append(topic)
    
    # Generate recommendations
    profile["recommended_focus"] = []
    
    if profile["common_bug_types"]:
        profile["recommended_focus"].append(
            f"Practice more debug exercises targeting: {', '.join(profile['common_bug_types'][:3])}"
        )
    
    if profile["weakest_topics"]:
        profile["recommended_focus"].append(
            f"Review topics: {', '.join(profile['weakest_topics'])}"
        )
    
    if not profile["recommended_focus"]:
        profile["recommended_focus"].append("Great progress! Consider advancing to the next topic.")


def get_personalized_recommendations(exercises_dir: str) -> dict:
    data = load_progress(exercises_dir)
    profile = data.get("learning_profile", {})
    
    return {
        "focus_areas": profile.get("recommended_focus", []),
        "suggested_exercise_mix": _suggest_exercise_mix(data),
        "difficulty_adjustment": _suggest_difficulty(data)
    }


def _suggest_exercise_mix(data: dict) -> dict:
    profile = data.get("learning_profile", {})
    mix = {"complete": 2, "debug": 1}
    
    if profile.get("common_bug_types"):
        mix = {"complete": 1, "debug": 2}
    
    if len(profile.get("strongest_topics", [])) >= 2:
        mix = {"complete": 2, "debug": 1}
    
    return mix


def _suggest_difficulty(data: dict) -> dict:
    adjustments = {}
    for topic in TOPICS:
        current = data.get("topic_difficulty", {}).get(topic, 1)
        topic_exercises = [ex for ex in data.get("completed_exercises", []) if _extract_topic(ex) == topic]
        topic_mistakes = sum(
            len(data.get("mistakes", {}).get(ex, [])) 
            for ex in topic_exercises
        )
        
        if len(topic_exercises) >= 3:
            avg_mistakes = topic_mistakes / len(topic_exercises)
            if avg_mistakes > 1.5 and current > 1:
                adjustments[topic] = "consider_lowering"
            elif avg_mistakes < 0.5 and current < 3:
                adjustments[topic] = "ready_to_advance"
            else:
                adjustments[topic] = "maintain"
        else:
            adjustments[topic] = "not_enough_data"
    
    return adjustments


def main():
    if len(sys.argv) < 3:
        print("Usage: python progress_tracker.py <exercises_dir> <command> [args...]")
        print("Commands:")
        print("  show                              — display progress")
        print("  complete <file> [attempts] [time] — mark exercise as done")
        print("  start <file>                      — mark exercise as in-progress")
        print("  mistake <file> <bug_type> <desc>  — record a mistake")
        print("  strength <file> <concept>         — record a strength")
        print("  difficulty <topic>                — get current difficulty")
        print("  bump <topic>                      — increase difficulty")
        print("  set-topic <topic>                 — set current topic")
        print("  recommend                         — get recommendations")
        print("  update-log                        — regenerate learning-log.md")
        sys.exit(1)

    exercises_dir = sys.argv[1]
    command = sys.argv[2]

    if command == "show":
        print(json.dumps(load_progress(exercises_dir), indent=2, default=str))
    elif command == "complete" and len(sys.argv) >= 4:
        attempts = int(sys.argv[4]) if len(sys.argv) > 4 else 1
        time_spent = float(sys.argv[5]) if len(sys.argv) > 5 else 0
        result = mark_complete(exercises_dir, sys.argv[3], attempts, time_spent)
        print(json.dumps(result, indent=2, default=str))
    elif command == "start" and len(sys.argv) >= 4:
        result = mark_in_progress(exercises_dir, sys.argv[3])
        print(json.dumps(result, indent=2, default=str))
    elif command == "mistake" and len(sys.argv) >= 6:
        result = record_mistake(exercises_dir, sys.argv[3], sys.argv[4], sys.argv[5])
        print(json.dumps(result, indent=2, default=str))
    elif command == "strength" and len(sys.argv) >= 5:
        result = record_strength(exercises_dir, sys.argv[3], sys.argv[4])
        print(json.dumps(result, indent=2, default=str))
    elif command == "difficulty" and len(sys.argv) >= 4:
        print(get_difficulty(exercises_dir, sys.argv[3]))
    elif command == "bump" and len(sys.argv) >= 4:
        result = bump_difficulty(exercises_dir, sys.argv[3])
        print(json.dumps(result, indent=2, default=str))
    elif command == "set-topic" and len(sys.argv) >= 4:
        result = set_topic(exercises_dir, sys.argv[3])
        print(json.dumps(result, indent=2, default=str))
    elif command == "recommend":
        result = get_personalized_recommendations(exercises_dir)
        print(json.dumps(result, indent=2, default=str))
    elif command == "update-log":
        update_learning_log(exercises_dir)
        print("Learning log updated!")
    else:
        print("Invalid command or missing arguments.")
        sys.exit(1)


if __name__ == "__main__":
    main()
