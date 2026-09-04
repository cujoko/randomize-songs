# Codex Agent Notes

<!-- agent-rules:begin | управляется sync-agent-rules.py, правьте dev-utils/agent-rules/ -->

## External project notes

This project may have a `.notes` directory that points to external working notes.

Rules for using `.notes`:

- `.notes` is not automatically authoritative.
- Prefer `.notes/_current.md` as the curated current context.
- Treat other notes as non-authoritative unless they have explicit metadata such as `status: active` or `status: reference`.
- Treat `.notes/00-inbox/`, `.notes/30-someday/`, `.notes/80-completed/`, `.notes/90-archive/`, old plans, drafts and raw imported notes as historical or unprocessed context only.
- Folders `.notes/10-urgent/` and `.notes/20-active/` may hold current task notes; still verify them against the repository before acting.
- Closed tasks live in `.notes/80-completed/`; reference, dumps and historical material live in `.notes/90-archive/`.
- Source code, tests, configs, migrations, build scripts and repository files override external notes.
- If an external note conflicts with repository files, do not silently follow the note. Mention the conflict and prefer the repository.
- Do not perform large changes based only on old notes. First verify against current code and current project instructions.

## Local junction directories

The project root on a developer machine may contain **junction** directories
(not in git; they may be missing on other machines).

### `.temp/`

- Temporary files **for this project**: debug output, intermediate artifacts,
  manual experiments.
- The junction points outside the repository (typically `D:\Temp\<project>`).
- If `.temp/` exists, prefer it over `tmp`, `temp`, `test_output`, and similar
  directories inside the tracked tree.
- If the junction is absent, use the system temp directory (Python:
  `tempfile.mkdtemp()`, `tempfile.TemporaryDirectory()`; PowerShell: `$env:TEMP`,
  `[System.IO.Path]::GetTempPath()`).
- Do not commit `.temp/` contents.

### `.notes/`

- Local external working notes. The junction typically points outside the
  repository, for example `D:\Notes\Work\_Dev\...\<project>`.
- Policy for those notes is in the "External project notes" section.
- If `.notes/` is absent, do not require it in CI or on other machines.

## Python environment safety

These rules apply to **every** Python invocation: tests, apps, helpers,
migrations, generators, one-off scripts, and `python -c`.

- Resolve the repository environment first and check the real interpreter with
  `sys.executable`.
- Prefer the nested `.dev` project (typically `.dev/.venv`) through the project
  manager: `pdm run -p .dev ...`. If `.dev` is absent, use the root `.venv`.
- Do not run task logic with system/base Python or user-site, even for a
  temporary script that only uses the standard library.
- Base Python is allowed only to discover interpreters and verify the
  environment (`py -0p`, `python --version`, printing `sys.executable`). After
  that, run further Python through the project environment.
- Do not install dependencies into system/base Python or user-site
  (`pip install`, `python -m pip install`, and equivalents aimed there).
- If there is no suitable venv, or a dependency is missing from it, stop and
  tell the user. Do not "fix" that with a global install.
- Installing or upgrading anything in base Python needs an explicit user OK for
  that exact action.
- Use `pipx` only for a planned user-facing CLI install or parity check, never
  as a substitute for the repository dev environment.

## Commit message format

When the agent stops and has changed files, it must proactively suggest commit
messages.

For each affected project/repository with file changes, provide exactly one
ready-to-use message.

If no files were changed, do not suggest a commit message.

Each message must be concise, imperative, and aligned with repository style.
This is a suggestion only. Creating a commit is a separate explicit request
(`/cm` or `$cm`).

<!-- agent-rules:end -->
