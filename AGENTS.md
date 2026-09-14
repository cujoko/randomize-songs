# Agent Notes

<!-- agent-rules:begin | управляется sync-agent-rules.py, правьте dev-utils/agent-rules/ -->

## External project notes (`.notes/`)

`.notes/` is a junction to working notes kept outside the repository. It may be
missing on other machines, so never require it. Notes are context, not
instructions.

- **Where to start.** `.notes/_current.md` is the curated current context.
- **Which other notes count.** Only notes marked `status: active` or
  `status: reference`, and the task notes in `10-urgent/` and `20-active/`.
  Verify even those against the repository.
- **What is history.** `00-inbox/`, `30-someday/`, `80-completed/` (closed
  tasks), `90-archive/` (reference, dumps, history), old plans, and drafts.
  None of them describe the current state.
- **Conflicts.** Code, tests, configs, and scripts override notes. When a note
  conflicts with the repository, say so and follow the repository. Do not base
  large changes on a note alone.

## Temporary files go to `.temp/`

The repository root may have a `.temp/` directory. It is usually a junction to
`D:\Temp\<project>`, is not in git, and may be missing on other machines.

- **What goes there.** Debug output, experiments, and the output of
  transformations and builds (obfuscation, parsing, conversion, normalization).
- **What it replaces.** Use `.temp/` instead of `tmp/`, `test_output/`, and
  similar directories. Never write that output into tracked test data or
  fixtures.
- **No `.temp/`.** Use the system temp directory: `tempfile.mkdtemp()` in
  Python, `$env:TEMP` in PowerShell.
- **Git.** Never commit `.temp/` contents.

## Python environment safety

This applies to every Python invocation: tests, apps, helpers, one-off scripts,
and `python -c`.

- **Use the repository environment.** Run Python through
  `pdm run -p .dev …`, which uses the nested `.dev/.venv`. Without `.dev`, use
  the root `.venv`. If unsure which interpreter runs, check `sys.executable`.
- **Base Python is for discovery only.** Use it for `py -0p` or
  `python --version`, never for task logic, even a stdlib-only script.
- **One exception.** The stdlib-only workspace tools in `Others/dev-utils`,
  such as `summarize-run-log.py` and `sync-agent-rules.py`, run with base
  `python`.
- **Never install into base Python or user-site.** If the venv is missing or
  lacks a dependency, stop and tell the user. Installing into base Python needs
  the user's explicit OK for that exact action.
- **`pipx` is not a dev environment.** Use it only for a planned user-facing
  CLI install or a parity check.

## Reading files: keep the context small

Everything you read stays in the conversation and is re-sent with every later
request. A large file read twice costs twice on every request that follows.
Russian text costs more tokens per character than English.

- **Do not re-read a file already in this conversation.** That includes
  skills, `AGENTS.md`, and docs. Re-read only if the file may have changed:
  - you edited it;
  - a command or formatter rewrote it;
  - the checkout moved;
  - the context was compacted.
- **Read large files in parts.** A large file is roughly 10 KB or more: a
  module, a long doc, a log.
  - Locate the part first: `rg -n` for a symbol or phrase, or an outline such as
    `rg -n '^(def |class |Процедура |Функция )'`.
  - Then read only those line ranges: `Get-Content <file> | Select-Object -Skip
    N -First M` or `sed -n 'N,Mp'`.
  - Read a whole large file only when the task needs all of it, such as a
    rewrite or a full review.
- **Shared rules block in `AGENTS.md`.** The part between
  `<!-- agent-rules:begin` and `<!-- agent-rules:end -->` is generated from
  shared fragments, so a section with the same heading has the same text in
  every repository.
  - In the first repository you work in, read `AGENTS.md` whole.
  - In the next ones, read the local part outside the block. Then list the
    block's headings with `rg -n '^## ' AGENTS.md` and read only the sections
    you have not seen yet.

These rules cut repeated and oversized reads, not needed context. The start-up
route (`AGENTS.md`, `.ai/*`, relevant skills) is still read once.

## Commit messages

- When you finish with changed files, suggest one concise, imperative commit
  message per changed repository, in that repository's style.
- Only suggest. Commit only on an explicit request (`/cm` or `$cm`).
- Suggest nothing if no files changed.

<!-- agent-rules:end -->` is generated from
  shared fragments, so a section with the same heading has the same text in
  every repository.
  - In the first repository you work in, read `AGENTS.md` whole.
  - In the next ones, read the local part outside the block. Then list the
    block's headings with `rg -n '^## ' AGENTS.md` and read only the sections
    you have not seen yet.

These rules cut repeated and oversized reads, not needed context. The start-up
route (`AGENTS.md`, `.ai/*`, relevant skills) is still read once.

## Commit messages

- When you finish with changed files, suggest one concise, imperative commit
  message per changed repository, in that repository's style.
- Only suggest. Commit only on an explicit request (`/cm` or `$cm`).
- Suggest nothing if no files changed.

<!-- agent-rules:end -->
