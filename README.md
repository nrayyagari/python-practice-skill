# Python Practice Skill

Adaptive Python practice skill for broad practical Python fluency: foundations,
OOP, standard library, testing, CLIs, automation, backend services, FastAPI,
Flask, AWS automation, data utilities, and production scripting.

## Sources

- Python documentation: https://docs.python.org/3/
- pytest documentation: https://docs.pytest.org/
- FastAPI documentation: https://fastapi.tiangolo.com/
- Flask documentation: https://flask.palletsprojects.com/
- Boto3 documentation: https://boto3.amazonaws.com/v1/documentation/api/latest/index.html

## Install

Install from the public GitHub repo:

```bash
python ~/.codex/skills/.system/skill-installer/scripts/install-skill-from-github.py \
  --repo nrayyagari/python-practice-skill \
  --path .
```

Restart Codex after installing the skill.

For local development, copy or symlink this directory into your agent skills
directory:

```bash
ln -s /home/laborant/repos/python-practice-skill /home/laborant/.agents/skills/python-practice
```

## Practice Workspace

Clone the exercise workspace on a new VM:

```bash
git clone https://github.com/nrayyagari/python-practice.git /home/laborant/repos/python-practice
```

## Behavior

The skill creates focused Python exercises in
`/home/laborant/repos/python-practice`, using dated folders like `3-may-26`.
More exercises requested on the same day go into the same folder. It reviews
solutions with `pytest`, tracks recurring mistakes and clarifying questions in
the root `learning-log.md`, and adapts future work toward practical Python
fluency. Backend, FastAPI, Flask, AWS automation, CLI, and data utility work are
application tracks, not the whole curriculum.

Exercises use `Difficulty: N/5`. The skill gives hints by default and provides a
full solution only when explicitly asked.
