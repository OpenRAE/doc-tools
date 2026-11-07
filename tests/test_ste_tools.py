"""Exercise the pinned upstream prose checker, not copies of its rules.

Source: OpenRAE/lilrae@28fc8f18c0866066ee450ae6e28ed234e93ca6b4
tests/test_documentation_checks.py (MIT). The package-boundary tests are new.
"""

from __future__ import annotations

import json
import os
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).parents[1]
LINT = ROOT / "tools/ste-lint.sh"

NEGATIVE = (
    "You can't start the lab until you have read all of the instructions "
    "and verified every prerequisite on the host that will run the lab for this exercise.\n\n"
    "The lab has a network. It has a server. It has a client. "
    "It has a router. It has a log. It has a clock. It has a disk.\n"
)
CORRECTED = (
    "Read the instructions. Verify the prerequisites on the lab host. "
    "Then start the lab.\n\n"
    "The lab has a network, a server, a client, and a router.\n\n"
    "It also has a log, a clock, and a disk.\n"
)
SELECTED_RULES = {"STE-4.2", "STE-5.1", "STE-6.6"}


def _run(*args: str, text: str | None = None, cwd: Path | None = None) -> subprocess.CompletedProcess[str]:
    return subprocess.run(
        ["bash", str(LINT), *args],
        input=text,
        text=True,
        capture_output=True,
        check=False,
        cwd=cwd,
    )


def _rule_ids(result: subprocess.CompletedProcess[str]) -> set[str]:
    return {finding["rule_id"] for finding in json.loads(result.stdout)["findings"]}


def test_selected_rules_fail_and_corrected_sample_passes() -> None:
    failed = _run("--format", "json", "-", text=NEGATIVE)
    assert failed.returncode == 1, failed.stderr
    report = json.loads(failed.stdout)
    assert _rule_ids(failed) == SELECTED_RULES
    assert all(finding["line"] > 0 for finding in report["findings"])

    corrected = _run("--format", "json", "-", text=CORRECTED)
    assert corrected.returncode == 0, corrected.stderr
    assert json.loads(corrected.stdout)["findings"] == []


def test_markdown_literals_are_preserved(tmp_path: Path) -> None:
    original = "Run `tool start --help`.\n\n```shell\n# You can't rewrite literal commands.\ntool start --help\n```\n"
    sample = tmp_path / "literal.md"
    sample.write_text(original)
    result = _run(str(sample))
    assert result.returncode == 0, result.stderr
    assert sample.read_text() == original


def test_no_paths_cannot_start_a_corpus_walk() -> None:
    result = _run()
    assert result.returncode == 2
    assert "Usage" in result.stderr


def test_package_config_applies_from_a_consumer_directory(tmp_path: Path) -> None:
    """A caller's working directory and its .ste.yml do not change the rules."""
    (tmp_path / ".ste.yml").write_text("disable_rules:\n  - STE-4.2\n  - STE-5.1\n  - STE-6.6\n")
    sample = tmp_path / "page with spaces.md"
    sample.write_text(NEGATIVE)
    hostile = _run("--format", "json", sample.name, cwd=tmp_path)
    assert hostile.returncode == 1, hostile.stderr
    assert _rule_ids(hostile) == SELECTED_RULES

    (tmp_path / ".ste.yml").write_text(": : malformed [\n")
    malformed = _run("--format", "json", sample.name, cwd=tmp_path)
    assert malformed.returncode == 1, malformed.stderr
    assert _rule_ids(malformed) == SELECTED_RULES


def test_missing_input_fails() -> None:
    result = _run("does-not-exist.md")
    assert result.returncode != 0


@pytest.mark.skipif(shutil.which("sha256sum") is None, reason="Linux installer contract")
def test_installer_rejects_bad_download_before_execution(tmp_path: Path) -> None:
    tools = tmp_path / "tools"
    tools.mkdir()
    shutil.copy(ROOT / "tools/install-ste.sh", tools)
    shutil.copy(ROOT / "tools/ste-lint.sh", tools)
    fake_bin = tmp_path / "bin"
    fake_bin.mkdir()
    curl = fake_bin / "curl"
    curl.write_text('#!/bin/sh\nwhile [ "$1" != "-o" ]; do shift; done\nprintf bad > "$2"\n')
    curl.chmod(0o755)
    env = {**os.environ, "PATH": f"{fake_bin}:{os.environ['PATH']}"}
    sample = tmp_path / "page.md"
    sample.write_text(NEGATIVE)

    for script, args in (("install-ste.sh", []), ("ste-lint.sh", [str(sample)])):
        result = subprocess.run(
            ["bash", str(tools / script), *args],
            env=env,
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode != 0
        assert "checksum" in result.stderr.lower()
        assert "STE-" not in result.stdout
    assert not list(tmp_path.glob(".tools/**/ste"))
