# Diário de Desenvolvimento — Brasileirão Schedule Project

## Etapas concluídas

### 1. Preparação das ferramentas
Git, uv e Python 3.15.1 instalados e validados.

### 2. Inicialização do projeto
Projeto criado com uv, versão do Python fixada e ambiente virtual `.venv` funcionando.

### 3. Controle de versão
Repositório Git inicializado, remoto `origin` configurado, identidade local definida e primeiro commit criado. A branch foi renomeada para `main` e publicada no GitHub.

### 4. Ferramentas de qualidade
Ruff e pytest instalados e validados. Regras de lint e formatação configuradas. O teste inicial de infraestrutura passou.

## Etapa 5 — Documentação e organização

**Status:** Em andamento.

### 5.1 Revisão do README
- Conteúdo inicial criado com objetivo, escopo, tecnologias e status.
- Identificada uma possível inconsistência na exibição de caracteres acentuados no PowerShell.
- Próximo passo: verificar os bytes do arquivo antes de decidir como corrigir a codificação.

### Estado do Git
As alterações em `pyproject.toml` e `uv.lock`, além do diretório `tests/`, ainda não foram commitadas. O último commit é `586595d`, publicado na branch `main`.

### Próximos passos
1. Corrigir ou validar a codificação do README.
2. Revisar a documentação e criar instruções permanentes para o agente do Antigravity.
3. Executar as verificações finais.
4. Criar um commit com as configurações de qualidade do projeto.
5. Definir a fonte dos dados e a metodologia de cálculo das distâncias.

## 6. Ambiente de notebooks e inventário de dependências

- `ipykernel` adicionado ao grupo de desenvolvimento para executar notebooks no ambiente virtual do projeto.
- Kernel Jupyter registrado com o nome interno `brasileirao-schedule` e o nome de exibição `Brasileirão Schedule Project (.venv)`.
- Pasta `notebooks/` criada para exploração e prototipagem.
- Arquivo `DEPENDENCIES.md` criado para documentar as dependências diretas, suas finalidades e as ferramentas de desenvolvimento.
- `uv tree` executado para inspecionar as dependências diretas e transitivas.

### Próximos passos
1. Confirmar o nome e a localização do notebook de exploração.
2. Baixar o CSV para `data/raw/` e inspecionar os dados no notebook.
3. Definir a lógica de cálculo dos deslocamentos.
4. Transformar a lógica validada em módulos Python e testes automatizados.