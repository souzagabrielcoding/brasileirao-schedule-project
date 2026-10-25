
from pathlib import Path
import tomllib

ROOT = Path(__file__).resolve().parents[1]
PROJECT_FILE = ROOT / "pyproject.toml"
LOCK_FILE = ROOT / "uv.lock"
OUTPUT_FILE = ROOT / "DEPENDENCIES.md"


def normalize(name: str) -> str:
    return name.lower().replace("_", "-").replace(".", "-")


def main() -> None:
    with PROJECT_FILE.open("rb") as file:
        project_data = tomllib.load(file)

    with LOCK_FILE.open("rb") as file:
        lock_data = tomllib.load(file)

    project = project_data["project"]
    groups = project_data.get("dependency-groups", {})

    locked_versions = {
        normalize(package["name"]): package["version"]
        for package in lock_data.get("package", [])
    }

    # Dependências diretas declaradas no projeto.
    dependencies = {}

    for dependency in project.get("dependencies", []):
        name = dependency.split(";")[0].strip()
        name = name.split("[")[0].strip()
        name = name.split("<")[0].split(">")[0].split("=")[0].strip()
        dependencies[normalize(name)] = "Produção"

    for group, packages in groups.items():
        for package in packages:
            name = package.split(";")[0].strip()
            name = name.split("[")[0].strip()
            name = name.split("<")[0].split(">")[0].split("=")[0].strip()
            dependencies[normalize(name)] = group

    lines = [
        "# Inventário de Dependências",
        "",
        "Arquivo gerado automaticamente a partir de `pyproject.toml` e `uv.lock`.",
        "Não edite manualmente: execute `uv run python scripts/update_dependencies.py`.",
        "",
        "| Pacote | Versão resolvida | Grupo |",
        "|---|---|---|",
    ]

    for name in sorted(dependencies):
        version = locked_versions.get(name, "Não encontrado no lock")
        group = dependencies[name]
        lines.append(f"| `{name}` | {version} | {group} |")

    lines.extend(
        [
            "",
            "## Reprodução do ambiente",
            "",
            "```powershell",
            "uv sync",
            "```",
            "",
            "## Ver dependências transitivas",
            "",
            "```powershell",
            "uv tree",
            "```",
            "",
        ]
    )

    OUTPUT_FILE.write_text("\n".join(lines), encoding="utf-8")
    print(f"Inventário atualizado: {OUTPUT_FILE}")


if __name__ == "__main__":
    main()
