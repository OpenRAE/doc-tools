# Contributing

## Before you open a pull request

- Open an issue first. Give it acceptance criteria.
- Deliver one issue in one pull request.
- Base the pull request on `dev`. `main` holds the released code.
- Use a Conventional Commit title, for example `fix(installer): reject a partial download`.
  release-please uses the titles on `main` to make releases.
- Do not add a new checker, rule engine, or service without an accepted issue.

## Set up

Prerequisites: Python 3.12 or newer, [uv](https://docs.astral.sh/uv/), and [pre-commit](https://pre-commit.com/).

```shell
git clone https://github.com/OpenRAE/doc-tools.git
cd doc-tools
uv sync
pre-commit install
```

## Check a change

Run the test files that your change affects:

```shell
uv run pytest tests/test_ste_tools.py
```

Check the Markdown files that you changed:

```shell
bash tools/ste-lint.sh README.md docs/reference.md
vale sync
vale README.md docs/reference.md
```

CI runs all hooks, tests, documentation checks, CodeQL, and SonarCloud.

## Write documentation

Use the `documentation` skill in `skills/documentation/`.
Write in ASD-STE100 Simplified Technical English.
Give each page one Diataxis purpose.
Check each claim against the code.

## Change a pin

To change the ste-cli version, change `VERSION` and all four SHA-256 values in `tools/install-ste.sh`.
Copy the values from the release `checksums.txt` file.
Compare them with the GitHub release asset digests.
Change the version in `tools/ste-lint.sh` and `.ste.yml`.
