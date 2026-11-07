"""Check the skill, plugin, and Vale package layouts that agent clients and Vale read."""

from __future__ import annotations

import json
import re
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
SKILL = ROOT / "skills/documentation"
STYLE = ROOT / "vale/DocTools"


def _frontmatter(text: str) -> dict[str, str]:
    match = re.match(r"^---\n(.*?)\n---\n", text, re.DOTALL)
    assert match, "SKILL.md needs YAML frontmatter"
    fields = {}
    for line in match.group(1).splitlines():
        key, _, value = line.partition(":")
        fields[key.strip()] = value.strip()
    return fields


def test_skill_has_client_frontmatter_and_license() -> None:
    text = (SKILL / "SKILL.md").read_text()
    fields = _frontmatter(text)
    assert fields["name"] == "documentation"
    assert fields["description"]
    assert "](LICENSE)" in text
    notice = (SKILL / "LICENSE").read_text()
    assert notice.startswith("MIT License")
    assert "Nuel Young Chukwunalu" in notice
    assert "Tudor Andrei Dumitrascu" in notice


def test_claude_marketplace_lists_the_root_plugin() -> None:
    marketplace = json.loads((ROOT / ".claude-plugin/marketplace.json").read_text())
    plugin = json.loads((ROOT / ".claude-plugin/plugin.json").read_text())
    assert marketplace["owner"]["name"]
    [entry] = marketplace["plugins"]
    assert entry["name"] == plugin["name"]
    assert entry["source"] == "./"
    assert "version" not in entry
    assert "version" not in plugin
    assert (ROOT / "skills" / "documentation" / "SKILL.md").is_file()


def test_vale_style_rules_are_portable() -> None:
    names = sorted(path.name for path in STYLE.glob("*.yml"))
    assert names == ["AvoidDismissive.yml", "AvoidHype.yml", "HeadingPunctuation.yml", "PlainWords.yml"]
    # Sentence length belongs to ste-cli; "terminate" is a technical term in cloud APIs.
    assert "terminate" not in (STYLE / "PlainWords.yml").read_text()


@pytest.mark.skipif(shutil.which("vale") is None, reason="Vale is not installed")
def test_vale_style_reports_and_accepts_samples(tmp_path: Path) -> None:
    styles = tmp_path / "styles"
    shutil.copytree(STYLE, styles / "DocTools")
    (tmp_path / ".vale.ini").write_text(
        f"StylesPath = {styles}\nMinAlertLevel = error\n\n[*.md]\nBasedOnStyles = DocTools\n"
    )
    bad = tmp_path / "bad.md"
    bad.write_text("# Setup:\n\nSimply leverage this powerful tool in order to start.\n")
    good = tmp_path / "good.md"
    good.write_text("# Setup\n\nUse this tool to start.\n")

    def vale(path: Path) -> subprocess.CompletedProcess[str]:
        return subprocess.run(
            ["vale", "--output=JSON", path.name], cwd=tmp_path, capture_output=True, text=True, check=False
        )

    failed = vale(bad)
    assert failed.returncode == 1, failed.stderr
    checks = {alert["Check"] for alert in json.loads(failed.stdout)["bad.md"]}
    assert checks == {
        "DocTools.AvoidDismissive",
        "DocTools.AvoidHype",
        "DocTools.HeadingPunctuation",
        "DocTools.PlainWords",
    }
    passed = vale(good)
    assert passed.returncode == 0, passed.stdout + passed.stderr
