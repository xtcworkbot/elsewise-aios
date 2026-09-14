#!/usr/bin/env python3
"""Check that this AI operating system is wired correctly.

Run from anywhere: python3 Tools/check.py
It reads files only and changes nothing. Exit code 0 means every check passed.
"""
import json
import re
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]

ROOT_ALLOWED = {
    "CLAUDE.md", "AGENTS.md", "README.md", ".gitignore", ".gitattributes", ".env", ".env.example", ".git",
    ".claude", ".agents", ".codex", ".DS_Store", "Thumbs.db", "desktop.ini",
    "Brain", "Memory", "Context", "Projects", "Decisions", "System",
    "Templates", "Outputs", "Tools", "Scratch", "Archive",
}
SHIPPED_FOLDERS = [
    "Brain", "Memory", "Context", "Projects", "Decisions", "System",
    "Templates", "Outputs", "Tools", "Scratch", "Archive",
]

failures = []
notes = []


def fail(message):
    failures.append(message)


def note(message):
    notes.append(message)


def listed_exactly(name, text):
    return re.search(r"(?<![\w-])" + re.escape(name) + r"(?![\w-])", text) is not None


def check_manuals():
    claude = ROOT / "CLAUDE.md"
    agents = ROOT / "AGENTS.md"
    if not claude.exists() or not agents.exists():
        fail("CLAUDE.md or AGENTS.md is missing.")
        return None
    text = claude.read_text(encoding="utf-8")
    if claude.read_bytes() != agents.read_bytes():
        fail("CLAUDE.md and AGENTS.md are different. Copy CLAUDE.md over AGENTS.md.")
    lines = text.count("\n") + 1
    if lines >= 200:
        fail(f"CLAUDE.md is {lines} lines. Keep it under 200 by moving detail into the file it routes to.")
    if "{{" in text:
        note("Onboarding has not finished. The manual still has names in double curly brackets.")
    return text


def check_manual_paths(text, source, base=None):
    base = base or ROOT
    for raw in sorted(set(re.findall(r"`([^`]+)`", text))):
        candidate = raw.strip()
        if not re.match(r"^\.?[A-Za-z][\w .-]*/", candidate) and not candidate.endswith(".md"):
            continue
        if any(ch in candidate for ch in "<>{}*$") or " " in candidate.split("/")[0]:
            continue
        if candidate.startswith(("python3", "git ", "http")):
            continue
        if "/" not in candidate and candidate not in ("CLAUDE.md", "AGENTS.md", "README.md"):
            continue
        for part in candidate.split():
            if "/" in part or part.endswith(".md"):
                if not (ROOT / part).exists() and not (base / part).exists():
                    fail(f"{source} names {part}, which does not exist.")


def check_root():
    for entry in ROOT.iterdir():
        if entry.name.startswith("."):
            continue
        if entry.name not in ROOT_ALLOWED:
            fail(f"Stray item in the root: {entry.name}. Move it to the right folder.")
    for folder in SHIPPED_FOLDERS:
        if not (ROOT / folder).is_dir():
            fail(f"Folder {folder}/ is missing.")


def check_indexes():
    for folder in SHIPPED_FOLDERS:
        base = ROOT / folder
        if not base.is_dir():
            continue
        index_name = "MEMORY.md" if folder == "Memory" else "_index.md"
        if not (base / index_name).exists():
            fail(f"{folder}/ has no {index_name}.")
        if folder in ("Scratch", "Archive", "Projects", "Outputs"):
            continue
        for sub in base.rglob("*"):
            if not sub.is_dir():
                continue
            parts = sub.relative_to(ROOT).parts
            if any(part.startswith(".") or part in ("__pycache__", "node_modules") for part in parts):
                continue
            if not (sub / "_index.md").exists():
                fail(f"{sub.relative_to(ROOT)}/ has no _index.md saying what it is for.")
    for folder in ("Projects", "Outputs"):
        base = ROOT / folder
        if not base.is_dir():
            continue
        for sub in base.iterdir():
            if sub.is_dir() and not sub.name.startswith(".") and not (sub / "_index.md").exists():
                fail(f"{sub.relative_to(ROOT)}/ has no _index.md. Every project and output folder starts with one from Templates/.")


def check_skills():
    claude_dir = ROOT / ".claude" / "skills"
    codex_dir = ROOT / ".agents" / "skills"
    claude_skills = {p.name for p in claude_dir.iterdir() if p.is_dir()} if claude_dir.exists() else set()
    codex_skills = {p.name for p in codex_dir.iterdir() if p.is_dir()} if codex_dir.exists() else set()
    for name in sorted(claude_skills):
        skill = claude_dir / name / "SKILL.md"
        if not skill.exists():
            fail(f"Claude skill {name} has no SKILL.md.")
            continue
        head = skill.read_text(encoding="utf-8")[:600]
        if f"name: {name}" not in head or "description:" not in head:
            fail(f"Claude skill {name} needs a name and description at the top that match its folder.")
        pointer = codex_dir / name / "SKILL.md"
        if not pointer.exists():
            fail(f"Claude skill {name} has no Codex pointer in .agents/skills/{name}/SKILL.md.")
        elif f".claude/skills/{name}/SKILL.md" not in pointer.read_text(encoding="utf-8"):
            fail(f"Codex pointer for {name} does not point at .claude/skills/{name}/SKILL.md.")
    for name in sorted(codex_skills - claude_skills):
        fail(f"Codex skill {name} has no Claude source in .claude/skills/{name}/.")


def check_agents():
    claude_dir = ROOT / ".claude" / "agents"
    codex_dir = ROOT / ".codex" / "agents"
    claude_agents = {p.stem for p in claude_dir.glob("*.md")} if claude_dir.exists() else set()
    codex_agents = {p.stem for p in codex_dir.glob("*.toml")} if codex_dir.exists() else set()
    for name in sorted(claude_agents - codex_agents):
        fail(f"Agent {name} exists for Claude but has no Codex version in .codex/agents/{name}.toml.")
    for name in sorted(codex_agents - claude_agents):
        fail(f"Agent {name} exists for Codex but has no Claude version in .claude/agents/{name}.md.")


def check_hooks():
    for settings in (ROOT / ".claude" / "settings.json", ROOT / ".codex" / "hooks.json"):
        if not settings.exists():
            fail(f"{settings.relative_to(ROOT)} is missing, so the hooks will not run there.")
            continue
        try:
            data = json.loads(settings.read_text(encoding="utf-8"))
        except json.JSONDecodeError as error:
            fail(f"{settings.relative_to(ROOT)} is not valid JSON: {error}.")
            continue
        for script in re.findall(r"\.claude/hooks/[\w-]+\.py", json.dumps(data)):
            if not (ROOT / script).exists():
                fail(f"{settings.relative_to(ROOT)} runs {script}, which does not exist.")


def check_secrets():
    if not (ROOT / ".env.example").exists():
        fail(".env.example is missing. It explains where keys go.")
    if not (ROOT / ".env").exists():
        note("No .env yet. Run the setup script, or copy .env.example to .env.")
    ignore = ROOT / ".gitignore"
    if not ignore.exists() or ".env" not in ignore.read_text(encoding="utf-8").split():
        fail(".gitignore does not ignore .env, so a key could be committed.")
    tracked = ROOT / ".git" / "index"
    if tracked.exists() and b".env\x00" in tracked.read_bytes().replace(b".env.example\x00", b""):
        fail(".env is tracked by git. Run git rm --cached .env, then commit.")
    for setup in ("Tools/setup.sh", "Tools/setup.ps1", "Tools/setup.cmd"):
        if not (ROOT / setup).exists():
            fail(f"{setup} is missing, so a new computer cannot be set up.")


def check_memory():
    memory = ROOT / "Memory"
    index = memory / "MEMORY.md"
    if not index.exists():
        return
    listed = index.read_text(encoding="utf-8")
    for item in memory.glob("*.md"):
        if item.name == "MEMORY.md":
            continue
        if not listed_exactly(item.name, listed):
            fail(f"Memory/{item.name} is not listed in Memory/MEMORY.md.")
        if not item.name.startswith(("user_", "feedback_", "project_", "reference_")):
            fail(f"Memory/{item.name} should start with user_, feedback_, project_ or reference_.")


def check_projects():
    projects = ROOT / "Projects"
    if not projects.exists():
        return
    listed = (projects / "_index.md").read_text(encoding="utf-8") if (projects / "_index.md").exists() else ""
    for folder in projects.iterdir():
        if folder.is_dir() and not folder.name.startswith(".") and not listed_exactly(folder.name, listed):
            fail(f"Projects/{folder.name}/ is not listed in Projects/_index.md.")


def main():
    text = check_manuals()
    if text:
        check_manual_paths(text, "CLAUDE.md")
    for extra in [ROOT / "System" / "Map.md"] + sorted(ROOT.rglob("_index.md")):
        if extra.exists() and ".git" not in extra.parts and not any(p.startswith(".") for p in extra.relative_to(ROOT).parts):
            check_manual_paths(extra.read_text(encoding="utf-8"), str(extra.relative_to(ROOT)), extra.parent)
    check_root()
    check_indexes()
    check_skills()
    check_agents()
    check_hooks()
    check_secrets()
    check_memory()
    check_projects()

    for message in notes:
        print(f"NOTE  {message}")
    for message in failures:
        print(f"FAIL  {message}")
    if failures:
        print(f"\n{len(failures)} problem(s) found. Fix them, then run this again.")
        return 1
    print("PASS  Every check passed.")
    return 0


if __name__ == "__main__":
    sys.exit(main())
