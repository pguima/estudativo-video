# Fonte — FireTrace, protótipo de análise de incêndios feito com o Claude Opus 5.5 (Tecnologia 011)

Consulta: **23/10/2026**. Regra do vídeo: só entra o que está na fonte; o que o autor não contou (tempo, prompts,
bibliotecas, código) **não é inventado**. A parte "como se constrói" é hipótese rotulada ("costumam", "tipicamente").
Nenhum quadro ou trecho do vídeo original é usado: a interface aparece só como recriação desenhada em `roteiro/visual.py`.

## 1. Post original — Dilum Sanjaya (@DilumSanjaya), X
URL: https://x.com/DilumSanjaya/status/2108241054298415258 (x.com responde 402; lido via
https://cdn.syndication.twimg.com/tweet-result?id=2108241054298415258&token=a, consultado 2x em 23/10/2026)
- Data: **08/10/2026 17:00 UTC**.
- Texto: "Played around with an idea for a wildfire analysis tool / Visualizes wildfire progression over time, tracks hot
  spots with drones and monitors firefighting efforts / Made with Opus 5.5".
- 2.284 curtidas, 98 respostas (no momento da consulta). Vídeo de 1:55, sem áudio.
- **Não informa**: tempo gasto, prompts, bibliotecas, código, link para demo, origem dos dados (real ou simulado).

### O que aparece no vídeo (assistido localmente só para descrever; nenhum quadro usado)
- App "FireTrace · Wildfire Forensic Analysis"; incidente "Ridgeview Incident", San Gabriel Mountains, CA, 14–18 ago 2024;
  ID CA-LAC-2024-0176; início (est.) Aug 14 2024 14:26; fim Aug 18 2024 11:20; 12,480 acres; causa "Under Investigation".
  Parece cenário de demonstração (o vídeo diz "parece", não afirma).
- Mapa 3D low-poly com alternância 2D/3D; perímetro com marcas de hora desde "Ignition Aug 14, 14:26".
- Linha do tempo com play; eventos-chave: Ignition (est.) 14:26, Rapid growth 16:50, Spot fire (prob.) Aug 15 03:12,
  Ridge crossing Aug 15 17:48, Containment (est.) Aug 18 11:20.
- Gráficos: Fire Area (acres), Rate of Spread, Elevation Profile. Camadas: Terrain (3D), Aerial Imagery, Burn Scar (dNBR),
  Fire Spread (Modeled), Ignition Probability, Weather (wind vectors), Suppression (drops & line). Painel Weather & Fire Behavior.
- Aba Drones: "6 of 6 airborne": FT-01 Kestrel (perimeter mapping), FT-02 Harrier (head fire watch, orbit active fire),
  FT-03 Swift (flank & spot watch), FT-04 Osprey (patrol / structure protection), FT-05 Condor (survey), FT-06 Wren
  (comms relay). Câmera IR "ironbow" com HUD (ALT, GS, BAT, coordenadas); detecções "Hot spot · 983 °C"; gráficos
  altitude, temperatura máx., bateria.
- Aba Resources: 13 unidades (T-910 DC-10 VLAT, T-131 C-130Q, T-162 RJ85, H-743 S-64 Air-Crane, H-531 Bell 205,
  AA-52 King Air 200 Air Attack, E-31/E-32/E-45 engines, WT-12 water tender, C-7/C-14 crews, DZ-4 D6 dozer);
  câmera Chase/Cockpit; Air Ops Log; gráficos Retardant Dropped (gal), Fire Line Built (chains), Personnel Assigned.
- Valores do clima/telemetria mostrados no NOSSO vídeo (16 km/h, 29 °C, 22%, 580 ft, 22 kt, 73%) são ilustrativos,
  inspirados na tela, e rotulados "valores ilustrativos".

## 2. Destaque oficial — Claude (@claudeai), X
URL: https://x.com/claudeai/status/2111177834127601902 (syndication, 23/10/2026)
- 16/10/2026: "Six projects from the last few weeks that caught our attention: A wildfire analysis prototype that maps the
  fire's spread over time and tracks hot spots, made with Opus 5.5." (o FireTrace é o 1º da lista).

## 3. OFICIAL — Anthropic, "Introducing Claude Opus 5.5"
URL: https://www.anthropic.com/news/claude-opus-5-5 (WebFetch, 23/10/2026)
- Lançamento: **22/09/2026**. "the first model in our new Claude 5.5 family".
- "It performs at the level of Claude Fable 5.1 on most work and costs 40% less to run than Opus 5."
- "Opus 5.5 is particularly good at long and sprawling jobs like codebase-wide migrations and audits."
- "A different tester had several Claude models build a game from a single prompt; Opus 5.5 scored higher than any other
  model on the strength of its graphics and polish."
- Outros (não usados na fala): US$ 4 / US$ 20 por milhão de tokens; saída >30% mais rápida que o Opus 5; ID `claude-opus-5-5`.
- A página **não** faz afirmações específicas sobre 3D ou design de interface.

## 4. Análise — Pasquale Pillitteri, 17/10/2026 (fonte secundária)
URL: https://pasqualepillitteri.it/pt/news/24751/claude-opus-5-5-prototipo-incendios-florestais-dilum-sanjaya (Apify web-fetch)
- Sanjaya: engenheiro de software e "creative coder", ~67 mil seguidores no X; publica demos visuais com modelos novos
  (também com Gemini, Kimi etc.). Mantém "AI Lab" em dilum.dev (~60 experimentos); **o projeto do incêndio não consta**.
- "Nem o site de Sanjaya nem o seu GitHub (116 repositórios) contêm uma ligação para código ou demonstração."
- Sanjaya não diz se os dados são reais ou simulados; o papel do Opus 5.5 é declaração dele; a republicação da @claudeai é
  "montra e não uma avaliação independente".
- Usado no vídeo só como apoio aos cuidados (que também conferimos: dilum.dev baixado em 23/10/2026, sem menção a
  fire/wildfire; o post não traz link).

## 5. Mais detalhes do autor?
- Busca na web (23/10/2026) por "Dilum Sanjaya FireTrace": só a cobertura do pasqualepillitteri.it (várias línguas).
- dilum.dev: nenhuma menção ao projeto. Respostas no fio: não foi possível ler (x.com 402); a syndication não traz
  respostas. **Não há detalhes técnicos publicados pelo autor** que tenhamos encontrado.

## 6. Mundo real (fontes oficiais; pesquisa delegada e conferida em 23/10/2026)
- **NASA FIRMS** — https://www.earthdata.nasa.gov/data/tools/firms
  "Global data are available within 3 hours of satellite observation; some U.S. and Canada active fire detections are
  available in real-time." Sensores MODIS (1 km) e VIIRS (375 m, melhor à noite).
- **NIROPS (USDA Forest Service)** — "Fire Imaging Technologies for Wildland Fire Operations – Users Guide" (fev/2020):
  https://www.nifc.gov/sites/default/files/document-media/Fire%20Imaging%20Technologies%20Users%20Guide.pdf
  "NIROPS provides a once-per-24-hour update of the fire's heat perimeter and distribution of heat within the perimeter."
  "NIROPS is typically flown at night when there is the greatest temperature contrast between the fire and the ground."
  (O prazo "0400 MDT" do guia de 2020 não foi confirmado para 2026 → não usado.)
- **Drones (USDA Forest Service)** — https://www.fs.usda.gov/about-agency/features/mechanized-birds-wildland-firefighting-drone-intelligence (03/10/2022)
  "...infrared, that allow the team to see through smoke and, at night, see heat signatures" /
  "this drone can pick up a 2-inch-by-2-inch spot fire from a half-mile away" (≈5 x 5 cm a ≈800 m).
- (não usado na fala) DOI, FY20: 1.887 voos de drone em apoio a incêndios, 400+ h, 21 estados —
  https://www.doi.gov/sites/default/files/fy20-doi-uas-flight-use-report-final.pdf
- **INPE · Programa Queimadas** — https://data.inpe.br/queimadas/faq/
  "fire pixel" = "foco de calor"; "o INPE processa automaticamente mais de 200 imagens por dia especificamente para
  detectar focos de queima da vegetação". (Satélite de referência AQUA/MODIS; troca para VIIRS não confirmada → não usado.)

## Decisões
- "Parece cenário de demonstração": hipótese, dita como "pelo jeito"/"parece".
- "WebGL (ex.: three.js)": só na tela, como "tipicamente"; a fala diz "tipicamente desenhado com WebGL".
- Narração acelerada 7% (atempo 1.07) para caber em < 6 min; originais em `audio/nova_voz/parte_*_original.wav`.
