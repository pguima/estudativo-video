# Fonte — MCP (Model Context Protocol)

Consultado em 15/10/2026, documentação oficial:
- https://modelcontextprotocol.io/docs/getting-started/intro
- https://modelcontextprotocol.io/docs/learn/architecture (versão do protocolo 2026-07-28)
- https://code.claude.com/docs/en/mcp
Conhecimento geral: criado e aberto pela Anthropic em novembro de 2024.

## Fatos usados no roteiro
- "MCP (Model Context Protocol) is an open-source standard for connecting AI applications to external systems."
  Conecta a fontes de dados (arquivos locais, bancos), ferramentas (buscadores, calculadoras) e fluxos (prompts).
- "Think of MCP like a USB-C port for AI applications."
- Exemplos oficiais: agentes acessando Google Calendar e Notion; Claude Code gerando um app web a partir de um design
  do Figma; chatbots corporativos ligados a vários bancos; modelos criando designs 3D no Blender e imprimindo em 3D.
- Benefícios: devs (menos tempo e complexidade), apps de IA (ecossistema de dados e ferramentas), usuários (IA mais capaz).
- Suporte: Claude, ChatGPT, Visual Studio Code, Cursor, MCPJam "and many others" — "build once and integrate everywhere".
- Participantes: Host (app de IA, ex. Claude Code, Claude Desktop, VS Code), Client (um por servidor, conexão dedicada),
  Server (programa que fornece contexto). Ex.: VS Code + servidor do Sentry + servidor de arquivos locais.
- Camadas: dados (JSON-RPC 2.0) e transporte. Transportes: stdio (local, mesma máquina) e Streamable HTTP (remoto,
  autenticação; OAuth recomendado).
- Primitivos do servidor: Tools (funções executáveis: operações de arquivo, chamadas de API, consultas ao banco),
  Resources (dados de contexto: conteúdo de arquivos, registros, respostas de API), Prompts (modelos reutilizáveis).
  Ex.: servidor de banco de dados = tools para consultar, resource com o esquema, prompt com exemplos.
- Métodos: */list para descobrir, tools/call para executar. Exemplo oficial: weather_current, location "San Francisco".
- O app junta as tools de todos os servidores; quando o modelo decide usar uma, o app intercepta, encaminha ao servidor
  certo e devolve o resultado ao modelo.
- Notificações: ex. notifications/tools/list_changed quando as ferramentas mudam.
- Primitivo do cliente: Elicitation — o servidor pede informação ou confirmação ao usuário.
- Claude Code: `claude mcp add --transport http notion https://mcp.notion.com/mcp`; `/mcp` para autenticar (OAuth) e
  ver status; escopos local (padrão), project (.mcp.json, compartilhado), user (todos os projetos).
- Segurança: "Verify you trust each server before connecting it. Servers that fetch external content can expose you to
  prompt injection risk." Claude Code pede aprovação antes de usar servidores de projeto (.mcp.json).
- Ligações com o canal: REA (TECH//001) é um servidor MCP; Claude Code (TECH//004) é um host.
