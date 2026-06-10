# Utility for randomizing songs

## Разработка

Проект использует `uv` для окружения, lock-файла и запуска dev-инструментов.

```powershell
uv sync --project .dev
uv run --project .dev pytest
uv run --project .dev ruff check .
```

## Установка CLI для локальной разработки

Для рабочего editable-окружения запускай из корня проекта:

```powershell
uv tool install --editable .dev --force
```
