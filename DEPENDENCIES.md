# Inventário de Dependências

Arquivo gerado automaticamente a partir de `pyproject.toml` e `uv.lock`.
Não edite manualmente: execute `uv run python scripts/update_dependencies.py`.

| Pacote | Versão resolvida | Grupo |
|---|---|---|
| `geopy` | 2.5.0 | dev |
| `ipykernel` | 7.4.0 | dev |
| `pandas` | 3.1.0 | dev |
| `pytest` | 9.1.1 | dev |
| `ruff` | 0.17.2 | dev |

## Reprodução do ambiente

```powershell
uv sync
```

## Ver dependências transitivas

```powershell
uv tree
```
