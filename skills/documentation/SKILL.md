---
name: documentation
description: Write, edit, or review technical documentation with Diataxis and ASD-STE100 while verifying claims against repository sources and preserving technical meaning.
---

# Documentation

Start with the reader's task. Use Tutorial for a learning exercise, How-to
guide for an operating task, Reference for exact facts, or Explanation for
reasons and relationships. Use the [Diataxis compass](https://diataxis.fr/compass/)
and [application guidance](https://diataxis.fr/how-to-use-diataxis/) when the
purpose is unclear. Split mixed content when this helps the reader. Preserve
useful page URLs and heading links.

Read the repository's contribution and agent guidance first. Find its
architecture decisions and supported interface references.
Verify technical claims against the actual code, configuration, commands,
and supported interfaces. Check historical claims against their source
revision. Record source paths, revision, checks, and corrected differences
in the delivery PR when the repository requires this evidence.

Preserve every fact, quantity, unit, qualifier, obligation, condition,
technical term, command, and identifier. Do not strengthen a recommendation
into an obligation. Do not invent an actor to remove passive voice. Judge
word meaning and part of speech in context. If a substitution changes the
meaning, restructure the sentence or keep the accurate technical term.

For procedures, give prerequisites and conditions before the affected action.
Use the imperative, one instruction per sentence, and at most 20 words per
instruction. For descriptions, use at most 25 words per sentence and six
sentences per paragraph.

Give one topic per paragraph. Put information in
logical order and use one consistent name for each thing. Prefer active voice
when the source identifies the actor. Preserve literal code and output.

Use the [official ASD-STE100 source](https://www.asd-ste100.org/) for definitive
rules and vocabulary. Do not invent dictionary rulings. Do not copy source
documents or dictionaries into this skill or a repository. Preserve quotations,
evidence, generated records, and license notices. Edit maintained generator
prose at its source.

Run the repository's configured writing checks on explicit changed paths.
Inspect the findings and fix real problems. Preserve correct technical text
when a finding is wrong; use a narrow documented exception if needed. A clean
checker report does not establish full STE conformance. Respect repository
boundaries for tests, corpus checks, and publication. Do not add analyzers,
services, or tools to a routine documentation edit.

Keep a small edit small. Do not require routine permission questions,
per-word reports, repeated compliance warnings, or a whole-document rewrite.
Report the useful changes, verification, and material unresolved questions.

## Sources

The meaning-preservation and contextual word-use guidance draws on
[nuelcyoung/asd-ste100](https://github.com/nuelcyoung/asd-ste100).
The logical-order, paragraph-topic, and consistent-name guidance draws on
[TudorAndrei/ste-cli's review skill](https://github.com/TudorAndrei/ste-cli/tree/v0.10.1/skill/ste-review).
Both use the MIT license; see [LICENSE](LICENSE). This skill uses original
wording and includes no STE source document or dictionary.
