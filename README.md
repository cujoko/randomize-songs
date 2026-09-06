# Utility for randomizing songs

## Разработка

Проект использует `uv` для окружения, lock-файла и запуска dev-инструментов.
Корневой пакет собирается через hatchling; `.dev` — editable-обёртка с
`pdm-backend` (`package-dir = ../src`) для pipx / `uv sync`.

```powershell
uv sync --project .dev
uv run --project .dev pytest
uv run --project .dev ruff check .
```

Публикация идёт из корня (`uv build` / CI), не из `.dev`.

## Установка CLI для локальной разработки

Через общий pipx-скрипт (предпочтительно):

```powershell
C:\Dev\Others\dev-utils\install-pipx-editable.ps1
```

Либо напрямую через uv:

```powershell
uv tool install --editable .dev --force
```
