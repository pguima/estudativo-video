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

### Short nativo vertical (desde 2026-10-23; modelo `012_short_tv_sem_anuncios`, Tecnativo English)
Short com roteiro e visual próprios, renderizado direto em 1080x1920 (não é recorte). Mesmo pipeline:
```bash
P=canais/tecnologia/NNN_short_slug     # roteiro/cenas_en.py (+ RITMO) e roteiro/visual.py vertical
python _ferramentas/gerar_voz_local.py $P 99 1 --lang en          # uma parte só
python _ferramentas/transcrever_palavras.py $P/analise/nova_voz_palavras_en.json $P/audio_en/nova_voz/parte_1.wav --lang en
python _ferramentas/voz_externa.py $P $P/analise/nova_voz_palavras_en.json $P/audio_en/nova_voz/parte_1.wav --lang en
python _ferramentas/render.py $P --vertical --lang en --stills 1,10,20
python _ferramentas/render.py $P --vertical --lang en --video --final --jobs 4
```
- `--vertical` troca `motor.W/H` para 1080x1920. Zona útil y=200–1560 (a interface do Shorts cobre o rodapé e a direita).
- `RITMO = dict(gap_bloco=0.0, pad_inicio=0.05, pad_fim=0.9)` no `cenas_en.py`: sem respiro entre blocos.
- Voz: tags `animada` + `confiante`, prompt de Short. Se ficar lenta, cortar o miolo das pausas > 0,3 s pelos tempos
  do Whisper e `atempo=1.12` (não usar `silenceremove`: come o começo das palavras).
- `SOM = dict(intro=False, ganho_trilha=0.40, lufs=-14, bpm=124, sfx={...})`: batida do 1º ao último segundo, -14 LUFS.
- Retenção: gancho visual + falado no 1º segundo, virada até 3 s, algo novo a cada 2–4 s, legenda grande de 1–3
  palavras (palavra falada em amarelo, números em algarismos), revelação no meio e final que volta à imagem do começo.
- Imagens reais só com crédito na tela e de fonte com licença clara (no 012: fotos do próprio autor, repositório MIT).
- Versão em português de um Short que nasceu em inglês: `roteiro/cenas.py` (mesmos ids/cues) + `roteiro/textos.py`
  com `TEXTOS = {"texto em inglês": "texto em português"}` (o `idioma.py` aplica na versão pt quando o arquivo existe).
  Render sem `--lang` (saídas em `audio/`, `trabalho/`, `final/<arquivo>.mp4`, `youtube/`). Números no formato BR
  via `PT = idioma.LANG == "pt"` no visual.py.

## Versão em inglês: canal **Tecnativo English** (desde 2026-10-23)
O mesmo vídeo, refeito em inglês para o canal irmão (**@TecnativoEN**). O visual (`visual.py`), a trilha e os efeitos são
os mesmos; mudam a narração, a legenda, os textos da tela, as capas e a publicação. Tudo do inglês fica **ao lado** do
português, sem mexer nele (`_ferramentas/idioma.py`):

| Português (padrão) | Inglês (`--lang en`) |
|---|---|
| `roteiro/cenas.py` | `roteiro/cenas_en.py`: **mesmos ids, blocks e `{cues}`**, texto adaptado (não traduzido palavra a palavra), números por extenso |
| textos no `visual.py` / `capa.py` | `roteiro/textos_en.py`: `TEXTOS = {"texto PT exatamente como no código": "EN"}` (`None` = falta traduzir, `""` = some) |
| `audio/`, `trabalho/`, `som/` | `audio_en/`, `trabalho_en/`, `som_en/` |
| `final/tecnologia_NNN_x.mp4` | `final/tecnologia_NNN_x_en.mp4` |
| `youtube/` (capas + publicacao.md) | `youtube_en/` |

```bash
P=canais/tecnologia/NNN_slug
python _ferramentas/idioma.py extrair $P            # cria/completa roteiro/textos_en.py com os textos da tela → traduzir
python _ferramentas/idioma.py faltando $P           # o que ainda falta (palavras soltas em tuplas às vezes escapam: conferir nas prévias)
python _ferramentas/tempos_sinteticos.py $P --lang en && python _ferramentas/render.py $P --lang en --stills 10,60,120   # prévia sem voz
python _ferramentas/gerar_voz_local.py $P <cena_de_corte> --lang en                     # Gemini TTS Studio, voz Neno, en-US
python _ferramentas/transcrever_palavras.py $P/analise/nova_voz_palavras_en.json $P/audio_en/nova_voz/parte_1.wav $P/audio_en/nova_voz/parte_2.wav --lang en
python _ferramentas/voz_externa.py $P $P/analise/nova_voz_palavras_en.json $P/audio_en/nova_voz/parte_1.wav $P/audio_en/nova_voz/parte_2.wav --lang en
python _ferramentas/render.py $P --lang en --video --final --jobs 4
python _ferramentas/idioma.py capa $P               # capas traduzidas em youtube_en/
```
- **Tradução:** inglês americano natural, não literal. Datas `Aug 14, 2024` / `10/08/2026` (mês/dia), horas `2:26 PM`,
  milhar com vírgula (`9,400`), decimal com ponto. Medidas: mantenha a da fonte e, se for métrica, dê a imperial junto
  quando ajudar (`2 x 2 in`, `~0.5 mi`). Fontes em português: marcar `(in Portuguese)`.
- Card de tradução de post em inglês (como no 011) some na versão EN (`""`).
- Cuidado: a troca vale para **toda** string igual no código, inclusive em lógica (`nm.startswith("PER")`): confira que a tradução não quebra a condição.
- **CTA (texto fixo):**
  > If this video showed you something new, leave a *like,* *subscribe* to the channel and turn on the *notification bell,*
  > so you don't miss the next tools. And tell me in the *comments:* <question>? *See you in the next video.*
  Os rótulos do CTA (LIKE, SUBSCRIBE, BELL) e "See you in the next video!" vêm de `idioma.COMUNS`.
- **Publicação:** `youtube_en/publicacao.md` todo em inglês. Hashtags `#Tech #AI #Programming` + 1 da ferramenta.
  Idioma do vídeo: **English (United States)**. Playlist: "AI Tools for Developers".

## Publicação
- Hashtags: `#Tecnologia #InteligenciaArtificial #Programacao` + 1 da ferramenta.
- Playlist: **"Ferramentas de IA para devs"** (ajustar conforme o tema).
