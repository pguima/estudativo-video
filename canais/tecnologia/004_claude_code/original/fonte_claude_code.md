# Fonte — Claude Code (Anthropic)

Consultado em 15/10/2026, documentação oficial:
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/quickstart
- https://code.claude.com/docs/en/permission-modes

## Fatos usados no roteiro
- "Claude Code is an agentic coding tool that reads your codebase, edits files, runs commands, and integrates with your
  development tools. Available in your terminal, IDE, desktop app, and browser."
- Features/bugs: "Claude Code plans the approach, writes the code across multiple files, and verifies it works."
  Bugs: cole a mensagem de erro ou descreva o sintoma; ele rastreia a causa e corrige.
- Superfícies: terminal (CLI), VS Code (e Cursor), JetBrains, app desktop, web (claude.ai/code), app Claude iOS/Android.
  "Each surface connects to the same underlying Claude Code engine, so your repo's CLAUDE.md files, settings, and MCP
  servers work across all of them."
- Instalar (nativo, recomendado): macOS/Linux/WSL `curl -fsSL https://claude.ai/install.sh | bash`;
  Windows PowerShell `irm https://claude.ai/install.ps1 | iex`. Também Homebrew (`brew install --cask claude-code`) e
  WinGet (`winget install Anthropic.ClaudeCode`). Conferir: `claude --version`. Começar: `cd seu-projeto` + `claude`.
  Login no primeiro uso. Contas: Claude Pro, Max, Team ou Enterprise (recomendado), Console (API, créditos pré-pagos),
  ou provedores de nuvem (Bedrock etc.).
- Primeiras perguntas (quickstart): "what does this project do?", "where is the main entry point?",
  "explain the folder structure". "Claude Code reads your project files as needed."
- Git: "commit my changes with a descriptive message", cria branches, abre pull requests.
- Exemplo: `claude "write tests for the auth module, run them, and fix any failures"`.
- Permissões: Manual (config `default`) pergunta antes da maioria das ações que editam arquivos, rodam comandos ou
  acessam a rede. `Shift+Tab` alterna o modo. `plan`: só lê, bloqueia edições até você aprovar um plano.
  `acceptEdits`: aprova edições. `auto`: um segundo modelo (classificador) revisa as ações no seu lugar.
  `bypassPermissions`: tudo, só em containers/VMs isolados.
- CLAUDE.md: arquivo markdown na raiz do projeto, lido no início de cada sessão (padrões, decisões de arquitetura,
  bibliotecas, checklists). Também lê AGENTS.md. Auto memory: aprende entre sessões.
- Skills: fluxos reutilizáveis, ex. `/review-pr`, `/deploy-staging`. Hooks: comandos antes/depois de ações
  (ex.: formatar após cada edição, lint antes do commit).
- MCP: padrão aberto; ex. ler docs no Google Drive, atualizar tickets no Jira, puxar dados do Slack.
- Agentes em paralelo (subagentes); `claude -p` para scripts/CI, ex.: `tail -200 app.log | claude -p "..."`;
  rotinas agendadas na nuvem (rodam com o computador desligado); GitHub Actions.
- Dicas oficiais: seja específico ("fix the login bug where users see a blank screen after entering wrong credentials"
  em vez de "fix the bug"); divida em passos; deixe o Claude explorar primeiro.
- Bastidor (verdadeiro): os vídeos deste canal são montados com o Claude Code (roteiro, animações em Python, render).
