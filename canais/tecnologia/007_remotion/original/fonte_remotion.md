# Fonte — Remotion (vídeos com React)

Consultado em 17/10/2026:
- https://github.com/remotion-dev/remotion (README)
- https://www.remotion.dev/ (site oficial, números e preços)
- https://github.com/remotion-dev/remotion/blob/main/LICENSE.md (licença)
- https://www.remotion.dev/docs/the-fundamentals (conceitos)
- https://www.remotion.dev/docs/render (formas de renderizar)
- https://www.remotion.dev/docs/ai/skills (Agent Skills)

## Fatos usados no roteiro
- Lema: "Make videos programmatically with React." Tópicos: javascript, react, video.
- GitHub: ~64,6 mil estrelas, 5,1 mil forks. Site: "5M+ installs per month", "300+ contributors",
  "1000 pages of docs", "35 templates & examples", "10K+ Discord members", "Over 300 customers".
- README: agentic video creation (ideia → vídeo com um agente de código), edição interativa (arrastar e soltar),
  criação programática (conectar a dados), automação (design systems reutilizáveis, render em lote na sua infraestrutura).
- Começar: `npx create-video@latest` (precisa de Node.js). `bun create video` oferece adicionar as skills.
- Fundamentos: o Remotion dá um número de quadro e uma tela em branco; você desenha com React.
  `const frame = useCurrentFrame();` Composição registrada em Root.tsx:
  `durationInFrames={150} fps={30} width={1920} height={1080}`. Primeiro quadro = 0, último = durationInFrames - 1.
  Componentes para texto, imagem, vídeo, áudio e formas. (interpolate, spring e Sequence: API padrão do Remotion.)
- Renderizar: botão Render no Remotion Studio; CLI `npx remotion render HelloWorld`; API de SSR em Node;
  AWS Lambda; GitHub Actions; Google Cloud Run (alfa). Também áudio, sequência de imagens, still, GIF e vídeo transparente.
- Agent Skills: `npx skills add remotion-dev/skills` — "best practices for working in Remotion projects";
  úteis para Claude Code, Codex, Kimi Code ou Cursor.
- Licença (não é open source tradicional — "Remotion License"):
  Free License para indivíduos, sem fins lucrativos, avaliação e empresas com fins lucrativos de até 3 funcionários;
  uso comercial permitido ("non-commercially or commercially for the purpose of creating videos and images").
  Proibido copiar/modificar o código do Remotion para vender, alugar ou licenciar como derivado.
  Company License obrigatória para empresas de 4+ pessoas. Preços no site: Creators US$ 25/mês por assento;
  Automators US$ 0,01 por render (mínimo US$ 100/mês); Enterprise a partir de US$ 500/mês.
  A licença deve mudar um pouco no Remotion 5.0.
