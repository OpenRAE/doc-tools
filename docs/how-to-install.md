# Install and upgrade the package

Use this guide to install doc-tools in a consumer repository.
Do not copy the package files into the consumer repository.

## Prerequisites

- Linux or macOS on x64 or arm64.
- `bash`, `curl`, `tar`, and `sha256sum` or `shasum`.
- Vale 3, if you use the Vale style. Install Vale with your existing method.

## Install the STE checks

1. Select a release on the [releases page](https://github.com/OpenRAE/doc-tools/releases).
2. Read the release `SHA256SUMS` file.
3. Record the version and the archive SHA-256 in a reviewed file in your repository.
4. Download and verify the archive with the recorded values:

   ```shell
   VERSION=0.1.0
   SHA256=<recorded archive SHA-256>
   ARCHIVE="doc-tools-${VERSION}.tar.gz"
   curl --proto '=https' --fail --silent --show-error --location -o "$ARCHIVE" \
     "https://github.com/OpenRAE/doc-tools/releases/download/v${VERSION}/${ARCHIVE}"
   echo "${SHA256}  ${ARCHIVE}" | sha256sum -c -
   ```

   On macOS, use `shasum -a 256 -c -` in place of `sha256sum -c -`.

5. Extract the archive into a directory that Git ignores:

   ```shell
   mkdir -p ".tools/doc-tools/${VERSION}"
   tar -xzf "$ARCHIVE" -C ".tools/doc-tools/${VERSION}" --strip-components=1
   ```

6. Check explicit Markdown paths:

   ```shell
   bash ".tools/doc-tools/${VERSION}/tools/ste-lint.sh" docs/index.md docs/guide.md
   ```

The first check installs ste-cli in the package directory.
The installer verifies the ste-cli archive before it extracts the binary.
A checksum mismatch stops the installation and the check.

## Add the Vale style

1. Add the release `DocTools.zip` URL to `Packages` in `.vale.ini`:

   ```ini
   Packages = https://github.com/OpenRAE/doc-tools/releases/download/v0.1.0/DocTools.zip
   ```

2. Add `DocTools` to `BasedOnStyles`.
3. Run `vale sync`.

If your configuration uses the Google style, set `Google.Contractions = NO`.
STE rule STE-4.2 rejects contractions.

## Install the skill

The skill and the STE checks install separately.
Remove an older personal skill named `documentation` before you install this skill.
Two skills with the same name can both show.

### Claude Code

Add the marketplace at a release tag, then install the plugin:

```text
/plugin marketplace add OpenRAE/doc-tools#v0.1.0
/plugin install doc-tools@openrae-doc-tools
```

To share the marketplace with a repository team, run this command in the repository.
Then commit the `.claude/settings.json` file that it writes:

```shell
claude plugin marketplace add OpenRAE/doc-tools#v0.1.0 --scope project
```

### Codex

Run the script of the preinstalled `skill-installer` skill with the repository, path, and release tag:

```shell
python3 "${CODEX_HOME:-$HOME/.codex}/skills/.system/skill-installer/scripts/install-skill-from-github.py" \
  --repo OpenRAE/doc-tools --path skills/documentation --ref v0.1.0
```

You can also give the same repository, path, and tag to `$skill-installer` in a Codex session.
The installer writes the skill to `$CODEX_HOME/skills/documentation`.
It stops if that directory exists. Remove the old directory to upgrade or roll back.

## Upgrade

1. Read the release notes and the new `SHA256SUMS` file.
2. Record the new version and SHA-256 in your repository.
3. Install the new version in a new directory. Keep the old directory.
4. Change the Vale `Packages` URL and run `vale sync`.
5. Change the marketplace tag or the `$skill-installer` reference, then update the skill.
6. Run your documentation checks.
7. Remove the old directory after the checks pass.

## Roll back

1. Restore the previous version and SHA-256 in your repository.
2. Restore the previous Vale `Packages` URL and run `vale sync`.
3. Restore the previous marketplace tag or skill reference, then update the skill.
4. Run your documentation checks.

The previous package directory stays usable until you remove it.
