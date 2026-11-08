# Agent instructions

- Use `OpenRAE/doc-tools` for all GitHub, issue, and pull request operations.
- Base work on `dev`. Do not merge into `dev` or `main`.
- Keep the package small. Do not add a checker, rule engine, schema, or service without an accepted issue.
- ste-cli owns the STE checks. Vale owns the style checks. Do not copy their rules into scripts.
- Keep product vocabulary and repository-specific rules in the consumer repositories.
- Write documentation in ASD-STE100 Simplified Technical English with the `documentation` skill in `skills/documentation/`.
- Run only the test files that a change affects. CI runs the full checks.
- Ground Control reads `.ground-control.yaml` and `.gc/plan-rules.md`.
