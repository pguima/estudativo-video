# Publicação no YouTube — Tecnologia · vídeo 005: MCP explicado

**Arquivo do vídeo:** `final/tecnologia_005_mcp_explicado.mp4` (5:28, 1920x1080, tema futurista escuro)
**Canal:** Tecnologia (IA, desenvolvimento, ferramentas)
**Narração:** Gemini TTS
**Fonte:** modelcontextprotocol.io (introdução e arquitetura) e documentação do Claude Code, consultadas em 15/10/2026 — ver `original/fonte_mcp.md`

## Capa (escolha 1)
| Arquivo | Ideia |
|---|---|
| `capa_A_usb_c_da_ia.jpg` | **Recomendada.** "O USB-C da INTELIGÊNCIA ARTIFICIAL" (apps → MCP → ferramentas) |
| `capa_B_o_que_e_mcp.jpg` | Curiosidade/busca: "Afinal, o que é esse MCP?" (tools/list → tools/call) |
| `capa_C_mcp.jpg` | Nome do protocolo: "MCP · Model Context Protocol · explicado" |

Use o "Testar e comparar" com as três.

---

## Título (escolha 1; até 70 caracteres)
1. **MCP Explicado: o USB-C da Inteligência Artificial** ← recomendado (com capa A)
2. Afinal, o Que é MCP? O Protocolo que Conecta a IA a Tudo (com capa B)
3. Model Context Protocol (MCP) Explicado do Zero (com capa C)
4. Como a IA Usa Ferramentas: MCP, Host, Cliente e Servidor

---

## Descrição (copie e cole)

```
Você ouve falar de MCP em todo lugar — mas o que é, afinal? Neste vídeo, você entende o Model Context Protocol, o padrão aberto (criado pela Anthropic em 2024) que conecta aplicativos de IA como Claude, ChatGPT, VS Code e Cursor a dados e ferramentas. A documentação oficial resume assim: o MCP é como uma porta USB-C para a IA.

📌 O que você vai aprender:
✅ Por que um padrão transforma 12 integrações em 7 peças
✅ A comparação oficial com o USB-C
✅ Exemplos reais: agenda, Notion, Figma, bancos de dados e até impressão 3D
✅ As 3 peças da arquitetura: host, cliente e servidor
✅ Servidor local (stdio) × remoto (HTTP + OAuth)
✅ Os 3 primitivos: tools, resources e prompts
✅ Como a conversa acontece por dentro (tools/list e tools/call)
✅ Como usar no Claude Code (claude mcp add e /mcp)
✅ Segurança: em quem confiar e o que é injeção de prompt

⏱️ Capítulos
00:00 12 integrações ou 7 peças?
00:19 O que é o MCP
00:33 O roteiro do vídeo
00:46 O USB-C da IA
01:02 Multiplicar × somar
01:20 Exemplos da documentação
01:40 Host, cliente e servidor
01:58 Local ou remoto
02:17 Tools, resources e prompts
02:39 Exemplo: servidor de banco de dados
02:52 A conversa por dentro (JSON-RPC)
03:15 Onde entra a IA
03:30 Avisos e perguntas ao usuário
03:44 Quem fala MCP
03:56 Na prática, no Claude Code
04:15 O MCP neste canal
04:29 Segurança
04:52 Resumo

🔗 Links oficiais
Documentação do MCP: https://modelcontextprotocol.io
MCP no Claude Code: https://code.claude.com/docs/en/mcp

📋 Resumo rápido:
• MCP = o USB-C da IA: um padrão aberto para conectar apps a dados e ferramentas
• Host, cliente e servidor
• Tools, resources e prompts
• Construa uma vez, integre em todo lugar
• Só conecte servidores em que você confia

👍 Se o vídeo te mostrou algo novo, deixe seu like, inscreva-se e ative o sininho para não perder as próximas ferramentas.
💬 Comente: qual ferramenta você conectaria primeiro à sua IA?

#Tecnologia #InteligenciaArtificial #Programacao #MCP
```

---

## Tags
```
mcp, model context protocol, o que é mcp, mcp explicado, servidor mcp, mcp server, anthropic, claude, claude code, chatgpt, vs code, cursor, agentes de ia, ia para programadores, json-rpc, tools, oauth, injeção de prompt, integração de ia, ferramentas de ia, inteligência artificial, programação
```

## Hashtags
`#Tecnologia #InteligenciaArtificial #Programacao #MCP`

---

## Comentário fixado
```
🔌 Cola do vídeo:
🧩 MCP = padrão aberto para conectar apps de IA a dados e ferramentas ("o USB-C da IA")
➕ Sem padrão: apps × ferramentas. Com MCP: apps + servidores
🏗️ Host (o app) · Cliente (1 por servidor) · Servidor (oferece as ferramentas)
🛠️ Primitivos: tools (ações) · resources (dados) · prompts (modelos)
💬 Por dentro: tools/list → tools/call → resultado
💻 Claude Code: claude mcp add --transport http <nome> <url>  e  /mcp
⚠️ Só conecte servidores em que você confia (cuidado com injeção de prompt)

👇 Qual ferramenta você conectaria primeiro à sua IA?
```

---

## Configurações no YouTube Studio
| Campo | Valor |
|---|---|
| Público | **Não, não é conteúdo para crianças** |
| Categoria | **Ciência e tecnologia** |
| Idioma do vídeo / título | Português (Brasil) |
| Legendas | Já estão na imagem; ative também as automáticas |
| Conteúdo alterado ou sintético | Narração com voz sintética (Gemini TTS): para narrador genérico normalmente não é obrigatório; marque "Sim" se quiser total segurança |
| Data de publicação | 18h–21h em dia útil |

## Playlist
**"Ferramentas de IA para devs"**.

## Tela final (últimos 17 s, a partir de 05:11)
- **Inscrever-se** à esquerda
- **Vídeo**: o 004 (Claude Code), para quem quer colocar o MCP em prática

## Cards
- 04:15 · card para o vídeo 001 (REA), "um servidor MCP de engenharia reversa".
- 04:20 · card para o vídeo 004 (Claude Code), "é um host".

## Ideias de Shorts
- 00:00–00:33 · "12 integrações ou 7? O que o MCP resolve"
- 00:46–01:20 · "O MCP é o USB-C da inteligência artificial"
- 04:29–04:52 · "Uma receita de bolo que tenta hackear a sua IA (injeção de prompt)"
