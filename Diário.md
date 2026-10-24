# Diário de Desenvolvimento — Brasileirão Schedule Project

## Objetivo
Criar uma aplicação Python para coletar dados do Campeonato Brasileiro e estimar as distâncias percorridas pelos clubes durante a temporada.

## Etapas concluídas

### 1. Preparação do ambiente
- Git instalado e validado.
- uv instalado e validado.
- Python 3.15.1 instalado e selecionado para o projeto.

### 2. Inicialização do projeto
- Projeto inicializado com uv no diretório do repositório.
- Ambiente virtual `.venv` criado e validado.
- Versão do Python fixada em `.python-version`.
- Dependências e configurações centralizadas em `pyproject.toml` e `uv.lock`.

### 3. Controle de versão
- Repositório Git inicializado.
- Identidade local do Git configurada.
- Repositório remoto do GitHub configurado.
- Primeiro commit criado.
- Branch principal renomeada para `main` e publicada no GitHub.

### 4. Ferramentas de qualidade
- Ruff e pytest adicionados como dependências de desenvolvimento.
- Regras iniciais de lint e formatação configuradas.
- Diretório `tests/` criado com um teste inicial de configuração.
- Ruff e pytest executados com sucesso após a formatação.

### 5. Organização e documentação
- README inicial criado com objetivo, escopo, tecnologias e status.
- `.gitignore` configurado para ignorar ambiente virtual, caches, arquivos de build e segredos.
- `AGENTS.md` criado com orientações para desenvolvimento, testes, documentação e Git.
- Codificação do README verificada: os bytes dos caracteres acentuados são compatíveis com UTF-8; a leitura com `Get-Content -Encoding utf8` exibiu o texto corretamente.

## Decisões técnicas atuais
- `uv` será utilizado para gerenciar o ambiente Python e as dependências.
- Ruff será utilizado para lint e formatação.
- pytest será utilizado para testes automatizados.
- A metodologia de cálculo das distâncias ainda não foi definida.
- A fonte dos dados do campeonato ainda não foi escolhida.

## Pendências
1. Revisar e completar as instruções de uso do README.
2. Confirmar o estado final do Git e revisar os arquivos alterados.
3. Executar as verificações de qualidade.
4. Criar um commit das alterações de configuração e documentação, após revisão.
5. Definir fonte dos dados, localidades dos clubes e estádios, metodologia de distância e escopo da temporada.
