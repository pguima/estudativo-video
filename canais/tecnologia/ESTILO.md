# Canal Tecnologia (IA, desenvolvimento, ferramentas): guia de estilo

Leia antes o [ESTILO_COMUM.md](../../ESTILO_COMUM.md). Aqui está só o que é **próprio deste canal**.
Este canal tem uma **linguagem visual própria**, futurista, que **não usa** o visual claro dos outros canais.
Referência: `001_rea_engenharia_reversa`.

## Identidade
| Item | Padrão |
|---|---|
| Público | Devs, estudantes de programação e curiosos por IA (PT-BR) |
| Conteúdo | Ferramentas, projetos open source, IA e desenvolvimento de software — 1 ferramenta/tema por vídeo |
| Tom | Entusiasmado, mas preciso: mostra o que a ferramenta faz com **exemplos concretos e números reais** da fonte; nada inventado |
| Duração | 5 a 8 min |
| Tema visual | **`import tech`** (`_ferramentas/tech.py`): tema `"tech"` escuro, neon, HUD |
| Pasta | `canais/tecnologia/NNN_<slug>/` · arquivo final `tecnologia_NNN_<slug>.mp4` |
| Fonte | Sempre guardar em `original/fonte_<tema>.md` o que foi lido (README, site, data da consulta) |

## Linguagem visual (tech.py)
- **Fundo animado** (`tech.background(c, t)`): espaço azul-escuro, matriz de pontos, duas órbitas de luz (ciano e violeta)
  que flutuam, **grade em perspectiva** rolando para a câmera, partículas subindo, scanlines e vinheta.
- **Moldura HUD** (`tech.overlay`): cantos em colchete ciano; no topo direito, ponto vermelho piscando + `TECH//NNN · TEMA`
  + contador `T+mm:ss`; `SYS.ONLINE` embaixo à esquerda.
- **Painéis** (`panel`): vidro escuro com **cantos chanfrados** (sup.-esq. e inf.-dir.), borda neon em gradiente, halo,
  etiqueta mono opcional (ex.: `app.exe`, `README.md`). Nunca cartão branco arredondado.
- **Títulos** (`head`): alinhados à **esquerda**, `// KICKER` em mono colorido + título Inter Black branco + traço neon com
  cursor piscando. Nunca a pílula centralizada dos outros canais.
- **Chips** (`chip`): mono, caixa alta, chanfrados; vazados (contorno) ou cheios para ênfase.
- **Código e terminal**: `terminal()` com bolinhas vermelha/âmbar/verde; `typed()` digita com cursor ciano;
  `code_lines()` com realce (palavra-chave violeta, nome ciano, texto branco).
- **Diagramas**: nós hexagonais (`node`) com halo pulsante e conexões (`link`) com **pulsos de dados** viajando.
- **Legenda** (`tech.caption`): branca; palavras `*destacadas*` em **ciano com brilho**.
- **CTA** (`tech.cta`): três painéis neon (Curtir ciano, Inscreva-se rosa, Sininho âmbar), painel violeta com a pergunta,
  despedida **"Até o próximo vídeo!"** com traço neon.
- Ganchos no `visual.py`: `BACKGROUND, CAPTION, OVERLAY = tech.background, tech.caption, tech.overlay`
  e `tech.SERIE = "TECH//NNN · TEMA"`.

## Cores
| Uso | Cor |
|---|---|
| Principal / IA / destaque | ciano `#22D3EE` |
| Protocolos, agentes, interpretação | violeta `#A78BFA` |
| Exemplos, ação, "reverso" | magenta `#F472B6` |
| Certo, sucesso, local/seguro, evidência | verde-limão `#4ADE80` |
| Atenção, comercial, limitações | âmbar `#FBBF24` |
| Erro, proibido, risco | rosa `#FB7185` |
Texto: branco `#EAF2FF`, secundário `#A9B8D0`, apagado `#62708A`. Fontes: **Inter** (títulos/texto) + **Consolas** (`mono`/`monob`).

**Glifos:** Consolas e Inter **não têm** ✓ ✗ ★ ◉ ○ ➤ ⌕ ↳ ⏱ ⇆ (saem quadradinhos). Use `check_icon()` desenhado, `→`, `+`, `[x]`.

## Som (padrão desde 2026-10-23)
- **Todo vídeo do canal tem trilha eletrônica + efeitos sonoros** de `_ferramentas/som_tech.py` (sintetizados, sem direitos).
  O `render.py --final` aplica sozinho quando o `visual.py` usa `import tech` (gera `som/trilha.wav`, `som/sfx.wav` e mixa).
  Para refazer só o som: `python3 _ferramentas/som_tech.py <proj>`.
- **Trilha:** ~112 BPM, ré menor (Dm Bb F C), arpejo pluck com eco, baixo pulsando, pad, bumbo 4/4, palmas, chimbal.
  1ª cena = intro (sem bateria); do 2º bloco ao CTA = batida completa; CTA e fontes = sem bumbo, fade-out.
  Fica ~10 dB abaixo da voz e abaixa mais quando a voz entra (ducking). Final ≈ -17 LUFS.
- **Efeitos:** whoosh digital em cada troca de cena, "lock" no título HUD, "pop" de interface em cada `{cue}`,
  clique/sininho/brilho no CTA. Nos elementos especiais, ajuste no `visual.py`:
  `SOM = dict(sfx={"05.c": ["typing@+0.2", "pop@+1.4"], "10.f": "deny", "03.b": None})` (modelo: `010_claude_duet`).
  Efeitos: pop, click, whoosh, lock, typing, notif, data, glitch, impact, confirm, alert, deny, bell, shimmer.
  Use typing em texto digitado, notif em notificações, lock/alert/deny em cuidados e proibições, confirm no resumo, impact na revelação do nome.
- Vídeo jornalístico/minidoc (ex.: `009_tse`): trilha "plantão de notícias" do `009/som/gerar_som.py` no lugar da eletrônica.
  `SOM = None` desliga o som (só narração).

## Roteiro
- Estrutura: **gancho (uma dor/curiosidade) → o que é → como funciona → o que faz → exemplos reais → como usar → cuidados/limites → resumo → CTA.**
- Nomes de ferramentas e comandos aparecem **na tela exatamente como se digitam** (`npx rea-agents setup`).
- Sempre citar **licença**, se é open source e o **uso responsável/legal** quando o tema pedir.
- Números da fonte, por extenso na fala ("duzentas e cinquenta mil estrelas") e em algarismos na tela.

**CTA (texto fixo):**
> Se esse vídeo te mostrou algo novo, deixe o seu *like,* *inscreva-se* no canal e ative o *sininho,* para não perder as próximas ferramentas.
> E me conte nos *comentários:* <pergunta>? *Até o próximo vídeo.*

## Capa
- Mesmo fundo do vídeo (grade + órbitas) com os cantos HUD; chip ciano no topo: `"IA · ENGENHARIA REVERSA"` (trocar pelo tema).
- Texto à esquerda em Inter Black branco com brilho + **palavra-chave numa caixa neon chanfrada** (ajusta o tamanho para caber).
- Painel chanfrado à direita (x=1140, 680x800) com código/hex, resultado ou diagrama.
- Ganchos: "a IA faz X" (A), um resultado concreto e surpreendente (B), nome da ferramenta grande (C).

## Shorts (desde 2026-10-19)
- Recortados do vídeo final, sem re-render: `<vídeo>/shorts/shortN_<tema>.py` (ffmpeg) + `shortN_publicacao.md`.
  Modelo: `001_rea_engenharia_reversa/shorts/`: `short_base.py` (layout escuro/neon + ffmpeg, função `gerar`; trocar `SRC`,
  `SELO` = `TECH//NNN · TEMA` e `RODAPE`) e um arquivo curto por Short com trechos e as 2 linhas do topo.
- 1080x1920, 30–45 s. Chip HUD `TECH//NNN · TEMA` + pergunta-gancho fixa (Inter Black branco com palavra-chave neon e brilho),
  recorte (60, 50, 1800, 800) do vídeo no meio, legenda recortada logo abaixo, rodapé "Vídeo completo no canal" + `// <tema>` em mono ciano.
- Trechos curtos ganham uma frase de apresentação da ferramenta (ex.: "Esse é o REA...") ou o gancho do início do vídeo.
  Cortes no silêncio: confirmar com `silencedetect` quando os tempos de `audio/tempos.json` se encostam.
- Publicação: título com `#shorts`, "Vídeo relacionado" = vídeo completo, comentário fixado com uma pergunta.

## Publicação
- Hashtags: `#Tecnologia #InteligenciaArtificial #Programacao` + 1 da ferramenta.
- Playlist: **"Ferramentas de IA para devs"** (ajustar conforme o tema).
