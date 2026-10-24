# Brasileirão Schedule Project

Aplicação Python para coletar dados do Campeonato Brasileiro e estimar as distâncias percorridas pelos clubes durante a temporada.

## Objetivo

Analisar o calendário de partidas e estimar os deslocamentos de cada clube, considerando jogos realizados e previstos.

## Escopo inicial

- Coletar dados da competição e do calendário de partidas.
- Validar e padronizar os dados coletados.
- Identificar os clubes, suas cidades e os locais das partidas.
- Calcular as distâncias associadas aos deslocamentos.
- Projetar a distância total ao final da temporada.
- Gerar resultados organizados e reproduzíveis.

## Tecnologias

- Python 3.15.1
- [uv](https://docs.astral.sh/uv/) para gerenciamento do ambiente e das dependências.
- Git e GitHub para controle de versão.
- Ruff para lint e formatação.
- pytest para testes automatizados.

## Pré-requisitos

- Git instalado.
- uv instalado.

A versão do Python está definida em `.python-version`. O uv utiliza essa configuração para preparar o ambiente do projeto.

## Configuração do ambiente

Clone o repositório e entre na pasta do projeto:

```powershell
git clone https://github.com/souzagabrielcoding/brasileirao-schedule-project.git
cd brasileirao-schedule-project
```

Sincronize o ambiente e as dependências:

```powershell
uv sync
```

## Verificações de qualidade

Execute o lint:

```powershell
uv run ruff check .
```

Verifique a formatação:

```powershell
uv run ruff format --check .
```

Execute os testes:

```powershell
uv run pytest
```

## Execução

A aplicação ainda está em fase de configuração inicial. A fonte dos dados, a metodologia de cálculo das distâncias e o fluxo de execução serão definidos antes da implementação funcional.

## Estrutura do projeto

```text
brasileirao-schedule-project/
├── src/
├── tests/
├── .gitignore
├── .python-version
├── AGENTS.md
├── Diário.md
├── README.md
├── pyproject.toml
└── uv.lock
```

## Decisões pendentes

- Fonte dos dados do campeonato e do calendário.
- Cadastro das cidades dos clubes e dos estádios.
- Método de cálculo das distâncias: linha reta, estrada ou rota aérea.
- Tratamento de partidas em campo neutro e mudanças de estádio.
- Escopo da temporada e forma de projetar os deslocamentos futuros.

## Desenvolvimento

Consulte `AGENTS.md` para as regras de desenvolvimento e `Diário.md` para o histórico das etapas.