#!/usr/bin/env python3
"""Static checks for the PUBLIC Skill package; no network or private database access."""
from pathlib import Path
import re

BASE = Path(__file__).resolve().parents[1]
REQUIRED = [
    "SKILL.md",
    "README.md",
    "references/framework.md",
    "references/communication.md",
    "references/privacy-safety.md",
    "examples/demo-01.md",
    "examples/demo-02.md",
    "tests/check_public.py",
]

for relative in REQUIRED:
    path = BASE / relative
    assert path.is_file(), f"Missing file: {relative}"

skill = (BASE / "SKILL.md").read_text(encoding="utf-8")
assert skill.startswith("---\n"), "SKILL frontmatter missing"
assert "name: amber-lens-public" in skill
for marker in ("Look", "Explore", "Notice", "Select"):
    assert marker in skill, f"Missing LENS step: {marker}"

# Ignore Git metadata and Python caches when run from a checked-out repository.
files = [
    p for p in BASE.rglob("*")
    if p.is_file()
    and ".git" not in p.relative_to(BASE).parts
    and "__pycache__" not in p.relative_to(BASE).parts
]
allowed = {".md", ".py"}
private_marker = "_".join(("PRIVATE", "COURSE", "BODY"))
for file in files:
    relative = file.relative_to(BASE)
    assert file.suffix in allowed, f"Unexpected asset: {relative}"
    assert file.stat().st_size < 100_000, f"Unexpectedly large file: {relative}"
    data = file.read_text(encoding="utf-8")
    assert not re.search(r"sk-[A-Za-z0-9]{20,}", data), "Potential API secret"
    assert private_marker not in data, "Unexpected private content marker"

assert len(files) == len(REQUIRED), f"Unexpected file count: {len(files)}"
print(f"PASS: {len(files)} public-only text files, frontmatter, references, examples, no oversized assets.")
