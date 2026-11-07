# 0001: Share existing documentation tools in one package

Status: accepted

## Context

BigRAE, RAE, and LilRAE need the same documentation checks and agent guidance.
LilRAE has STE checks for ste-cli. RAE has Vale style rules.
A user-level documentation skill exists.
Copies in each repository change separately.

## Decision

- Put the existing LilRAE STE wrapper, installer, configuration, and tests in this repository.
- Keep ste-cli as the only STE checker. Pin its version and archive digests.
- Ship the RAE Vale rules that help all three consumers as the `DocTools` style.
- Keep product terms, heading exceptions, and duplicate checks in the consumers.
- Ship the existing skill without a new authoring workflow.
- Use the normal client mechanisms: a Claude Code plugin marketplace and the Codex skill installer.
- Publish a tagged archive, `DocTools.zip`, and `SHA256SUMS` for each release.
- Consumers pin a version and its SHA-256.

## Consequences

- A rule change happens in one place. Consumers adopt it when they change the pin.
- The marketplace is one JSON file. It adds no service or hook.
- Consumers keep their Vale installation and site generator.
- A consumer must update its pin to get a fix.
