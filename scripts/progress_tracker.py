#!/usr/bin/env python3
"""
Progress tracker for python-practice skill.

Reads/writes progress.json in the exercises directory.
"""

import json
import sys
from pathlib import Path

PROGRESS_FILE = "progress.json"


def load_progress(exercises_dir: str) -> dict:
    path = Path(exercises_dir) / PROGRESS_FILE
    if path.exists():
        return json.loads(path.read_text())
    return {
        "current_exercise": None,
        "completed": [],
        "in_progress": [],
        "topics_covered": [],
        "next_topic": None,
        "phase": 1
    }


def save_progress(exercises_dir: str, data: dict) -> None:
    path = Path(exercises_dir) / PROGRESS_FILE
    path.write_text(json.dumps(data, indent=2))


def mark_complete(exercises_dir: str, exercise_file: str, topic: str) -> dict:
    data = load_progress(exercises_dir)
    if exercise_file in data["in_progress"]:
        data["in_progress"].remove(exercise_file)
    if exercise_file not in data["completed"]:
        data["completed"].append(exercise_file)
    if topic not in data["topics_covered"]:
        data["topics_covered"].append(topic)
    data["current_exercise"] = None
    save_progress(exercises_dir, data)
    return data


def mark_in_progress(exercises_dir: str, exercise_file: str) -> dict:
    data = load_progress(exercises_dir)
    if exercise_file not in data["in_progress"]:
        data["in_progress"].append(exercise_file)
    data["current_exercise"] = exercise_file
    save_progress(exercises_dir, data)
    return data


def set_next_topic(exercises_dir: str, topic: str) -> dict:
    data = load_progress(exercises_dir)
    data["next_topic"] = topic
    save_progress(exercises_dir, data)
    return data


def advance_phase(exercises_dir: str) -> dict:
    data = load_progress(exercises_dir)
    data["phase"] = data.get("phase", 1) + 1
    save_progress(exercises_dir, data)
    return data


def main():
    if len(sys.argv) < 3:
        print("Usage: python progress_tracker.py <exercises_dir> <command> [args...]")
        print("Commands: show, complete <file> <topic>, start <file>, next-topic <topic>, advance-phase")
        sys.exit(1)

    exercises_dir = sys.argv[1]
    command = sys.argv[2]

    if command == "show":
        print(json.dumps(load_progress(exercises_dir), indent=2))
    elif command == "complete" and len(sys.argv) >= 5:
        result = mark_complete(exercises_dir, sys.argv[3], sys.argv[4])
        print(json.dumps(result, indent=2))
    elif command == "start" and len(sys.argv) >= 4:
        result = mark_in_progress(exercises_dir, sys.argv[3])
        print(json.dumps(result, indent=2))
    elif command == "next-topic" and len(sys.argv) >= 4:
        result = set_next_topic(exercises_dir, sys.argv[3])
        print(json.dumps(result, indent=2))
    elif command == "advance-phase":
        result = advance_phase(exercises_dir)
        print(json.dumps(result, indent=2))
    else:
        print("Invalid command or missing arguments.")
        sys.exit(1)


if __name__ == "__main__":
    main()
