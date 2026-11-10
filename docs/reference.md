# Package reference

## Files

| Path | Content |
| --- | --- |
| `tools/install-ste.sh` | Installs ste-cli 0.10.1 in `.tools/ste/0.10.1/` below the package root. |
| `tools/ste-lint.sh` | Runs `ste lint` with the package configuration on explicit paths. |
| `.ste.yml` | ste-cli configuration. |
| `vale/DocTools/` | Vale style rules. The release asset `DocTools.zip` contains this directory. |
| `skills/documentation/` | Agent skill and its license notice. |
| `.claude-plugin/` | Claude Code marketplace `openrae-doc-tools`. Its plugin `doc-tools` has `skills/documentation/` as its root. |
| `tests/` | Behavior tests for the checks, the style, and the package layout. |

## `tools/ste-lint.sh`

```text
bash tools/ste-lint.sh [ste lint options] FILE [FILE ...]
```

- The script runs `ste lint --config <package>/.ste.yml --no-baseline --fail-over 0`.
- The script adds your options and paths after these options.
- `-` reads text from standard input.
- A `.ste.yml` file in the working directory does not change the configuration.
- The script installs ste-cli first when the binary is missing.

| Exit status | Meaning |
| --- | --- |
| 0 | No findings. |
| 1 | Findings, a failed installation, or a checksum mismatch. |
| 2 | No path, an unsupported platform, or no SHA-256 tool. |

Other ste-cli errors return the ste-cli exit status.

## `tools/install-ste.sh`

The installer downloads the ste-cli release archive for the host platform.
It compares the archive SHA-256 with a pinned value before extraction.
It extracts only the `ste` binary. It writes the binary to a private temporary file and renames it.
It uses an installed binary without a new download.

| Platform | Archive SHA-256 |
| --- | --- |
| Linux x64 | `d4a9fa77dec2b4623db324fc0951a0a0af6284de3cb42d1717c174bc5762e937` |
| Linux arm64 | `f788410fab9302606c80a15cb30925d40cff010e49f7279da17c71db0ec0e08e` |
| macOS x64 | `267f11730731a3942e38c148ff80c652800986cf913097e1388d600820b1d374` |
| macOS arm64 | `9365f616fe7053f8d9b1ec5d40cc92d74ef964ddcd07d24b727cec5937bb6c51` |

CI runs the tests on Linux x64 and macOS arm64.
The pins come from the release `checksums.txt` file and the GitHub release asset digests.

## `.ste.yml`

| Key | Value | Effect |
| --- | --- | --- |
| `mode` | `flavored` | Uses the flavored rule set. |
| `dictionary` | `false` | Turns off the dictionary rule. |
| `analyzer` | `false` | Turns off the grammar analyzer. |
| `fail_over` | `-1` | Reports without a score limit. The wrapper sets `--fail-over 0`. |
| `rules` | `STE-4.2`, `STE-5.1`, `STE-6.6` at `error` | Contractions, sentence length, and paragraph length. |
| `disable_rules` | 17 rule IDs | Turns off the listed rules. |

## Vale rules

| Rule | Check |
| --- | --- |
| `DocTools.AvoidDismissive` | Words such as `simply`, `just`, and `easy`. |
| `DocTools.AvoidHype` | Promotional words such as `powerful` and `seamless`. |
| `DocTools.HeadingPunctuation` | A heading that ends with `.`, `!`, `?`, `:`, or `;`. |
| `DocTools.PlainWords` | Long forms such as `in order to` and `utilize`. |

All rules use the `error` level.

## Sources

| Asset | Source | License |
| --- | --- | --- |
| `tools/install-ste.sh`, `tools/ste-lint.sh`, `.ste.yml` | [OpenRAE/lilrae@28fc8f1](https://github.com/OpenRAE/lilrae/tree/28fc8f18c0866066ee450ae6e28ed234e93ca6b4) | MIT |
| `tests/test_ste_tools.py` | LilRAE `tests/test_documentation_checks.py` at the same revision, with new boundary tests | MIT |
| `vale/DocTools/` | [OpenRAE/rae@f30ed4b](https://github.com/OpenRAE/rae/tree/f30ed4b249f9a2b6cdae151e98d324d085762b2d) `styles/RAES/` | MIT |
| `skills/documentation/` | The existing user-level `documentation` skill | MIT notices in `skills/documentation/LICENSE` |
| ste-cli binary | [TudorAndrei/ste-cli v0.10.1](https://github.com/TudorAndrei/ste-cli/tree/v0.10.1), downloaded at install time | MIT |

Changes from the sources:

- The installer extracts only `ste`. It writes a private temporary file and renames it, so parallel installs succeed.
- The installer `curl` command uses `--proto '=https'`, so a redirect to a plain HTTP URL fails.
- `PlainWords` does not change `terminate` to `stop`. Cloud APIs use both words with different meanings.
- The skill has no LilRAE file list.

These items stay in the consumer repositories:

| Item | Reason |
| --- | --- |
| RAE `HeadingCase` | It lists RAE product names. Google style has the same check. |
| RAE `SentenceLength` | STE-5.1 has the same check. |
| RAE `ReadingLevel` | The grade limit is a RAE choice. |
| RAE vocabulary and style guide | They contain RAE product terms and contracts. |
| LilRAE `.ste-required.txt` and CI corpus reports | They list LilRAE pages and LilRAE CI scope. |
| Vale installation and site generators | Each repository keeps its existing method. |
