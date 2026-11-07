# Plan rules

Repository-specific constraints every /implement plan must satisfy. One bullet per rule.
- Plans MUST keep ste-cli as the only STE checker and Vale as the only style checker. Do not add a linter, rule engine, configuration schema, or service.
- Plans that change the ste-cli version MUST change every pinned SHA-256 and verify each value against the release `checksums.txt` file and the GitHub asset digests.
- Plans that touch `.github/workflows/**` MUST pass `actionlint`.
- Plans MUST keep consumer-specific vocabulary and rules out of this repository.
