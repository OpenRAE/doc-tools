# Security policy

## Report a vulnerability

Do not put vulnerability details in public issues, pull requests, or discussions.

Report privately through GitHub private vulnerability reporting:

- Open a report: https://github.com/OpenRAE/doc-tools/security/advisories/new
- Published advisories: https://github.com/OpenRAE/doc-tools/security/advisories

If private reporting is not available to you, contact the maintainer privately.
Use the contact path on the [Brad Edwards GitHub profile](https://github.com/Brad-Edwards).

Include these details:

- the affected file, command, or release
- the version or commit
- the steps to reproduce the problem
- the expected and actual behavior
- the effect

## Scope

These areas are in scope:

- download and checksum verification in `tools/install-ste.sh`
- path and option handling in `tools/ste-lint.sh`
- release assets and their SHA-256 sums
- repository workflows that handle untrusted input

Problems in ste-cli or Vale belong to those projects.

## Response

The maintainer reviews reports when time permits.
Reproducible problems in current releases get priority.
Do not publish exploit details before the maintainer can prepare a fix.
