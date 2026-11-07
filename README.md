# doc-tools

doc-tools is a small, versioned set of documentation checks and agent guidance.
BigRAE, RAE, and LilRAE use it. It contains these parts:

| Part | Path | Use |
| --- | --- | --- |
| STE checks | `tools/ste-lint.sh`, `tools/install-ste.sh`, `.ste.yml` | Check explicit Markdown paths with the pinned upstream ste-cli. |
| Vale style | `vale/DocTools/` | Add portable style rules to a Vale configuration. |
| Agent skill | `skills/documentation/` | Guide agents that write or review documentation. |

The package does not contain the ASD-STE100 specification or its dictionary.
A clean check result does not prove full STE conformance.

## Quick start

Check one file from a clone of this repository:

```shell
bash tools/ste-lint.sh docs/how-to-install.md
```

Install the skill in Claude Code:

```text
/plugin install doc-tools --marketplace OpenRAE/doc-tools
```

## Documentation

- [Install and upgrade the package](docs/how-to-install.md) (how-to guide)
- [Package reference](docs/reference.md) (reference)
- [Package architecture](docs/architecture.md) (explanation)
- [Decision records](docs/decisions/) (explanation)

## Project

- [Contributing](CONTRIBUTING.md)
- [Security policy](SECURITY.md)
- [Support](SUPPORT.md)
- [Code of conduct](CODE_OF_CONDUCT.md)
- [Third-party notices](THIRD_PARTY_NOTICES.md)

doc-tools uses the [MIT License](LICENSE).
