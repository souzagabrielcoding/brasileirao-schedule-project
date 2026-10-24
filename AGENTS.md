@'
# Instruções para agentes de código

## Objetivo do projeto
Desenvolver uma aplicação Python para coletar dados do Campeonato Brasileiro,
analisar partidas e estimar as distâncias percorridas pelos clubes durante
a temporada.

## Ambiente e dependências
- Use `uv` para gerenciar o Python, o ambiente virtual e as dependências.
- Respeite a versão definida em `.python-version` e `pyproject.toml`.
- Execute comandos Python por meio de `uv run`.
- Não instale dependências globalmente.
- Antes de adicionar uma dependência, explique por que ela é necessária.

## Qualidade e testes
- Use Ruff para lint e formatação.
- Use pytest para testes automatizados.
- Antes de concluir uma alteração, execute:
  - `uv run ruff check .`
  - `uv run ruff format --check .`
  - `uv run pytest`
- Crie ou atualize testes para comportamentos novos e corrigidos.
- Não altere testes apenas para esconder falhas de implementação.

## Organização e implementação
- Prefira funções pequenas, com responsabilidades claras.
- Separe coleta, validação, transformação, cálculo e apresentação dos dados.
- Trate dados externos como potencialmente incompletos ou inconsistentes.
- Evite duplicação de código e configurações desnecessárias.
- Não implemente funcionalidades fora do escopo acordado sem consultar o usuário.

## Git e fluxo de trabalho
- Trabalhe em etapas pequenas e verificáveis.
- Antes de alterações relevantes, confira o estado do Git.
- Não descarte nem sobrescreva alterações do usuário sem autorização.
- Não faça commits ou pushes sem autorização explícita.
- Use mensagens de commit curtas e descritivas, preferencialmente em inglês,
  seguindo convenções como `feat:`, `fix:`, `test:` e `docs:`.
- Ao terminar uma etapa, informe os arquivos alterados, as verificações
  executadas e os resultados.

## Documentação
- Mantenha o `README.md` atualizado com objetivo, instalação, uso e limitações.
- Registre no `Diário.md` um resumo curto das etapas concluídas.
- Documente decisões relevantes e suas justificativas.

## Precisão dos dados
- Não invente fontes, resultados, coordenadas ou distâncias.
- Registre a fonte e a data de coleta dos dados utilizados.
- Diferencie distâncias em linha reta de distâncias por estrada ou por rota aérea.
- Explique as hipóteses usadas nos cálculos e os limites das estimativas.
'@ | Set-Content -Path AGENTS.md -Encoding utf8