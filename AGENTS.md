# Codex Agent Notes

## External project notes

This project may have a `.notes` directory that points to external working notes.

Rules for using `.notes`:

- `.notes` is not automatically authoritative.
- Prefer `.notes/00-current/ai-brief.md`, `.notes/00-current/current-state.md`, `.notes/00-current/open-questions.md`, and `.notes/00-current/decisions.md`.
- Treat notes outside `.notes/00-current/` as non-authoritative unless they have explicit metadata such as `status: active` or `status: reference`.
- Treat `.notes/90-archive/`, `.notes/30-someday/`, old plans, drafts and raw imported notes as historical context only.
- Source code, tests, configs, migrations, build scripts and repository files override external notes.
- If an external note conflicts with repository files, do not silently follow the note. Mention the conflict and prefer the repository.
- Do not perform large changes based only on old notes. First verify against current code and current project instructions.
