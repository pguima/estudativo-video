# Canal ENEM (Física, Matemática, Química, Geografia, Linguagens e Redação): guia de estilo

Leia antes o [ESTILO_COMUM.md](../../ESTILO_COMUM.md). Aqui está só o que é **próprio deste canal**.

> **Desde 2026-10-09: aulas para iniciantes.** Cada assunto vira uma série de episódios de 8–12 min, seguindo
> [PROMPT_AULA_INICIANTE.md](PROMPT_AULA_INICIANTE.md) (gancho, promessa, pré-requisitos relâmpago, uma analogia âncora,
> 3 frases-chave no meio e no fim, erros, questão com "pause o vídeo", ponte para o próximo episódio).
> Série em pasta própria: `NNN_enem_<matéria>_<assunto>/epN_<tema>/` + `PLANO_DA_SERIE.md`. Ex.: `012_enem_geografia_cartografia` (6 eps) e `010_enem_matematica_conjuntos` (5 eps, desde 2026-10-12; vídeo antigo em `_antigo_video_unico/`).
> Cores com função: azul = definição · roxo = regra/fórmula (Matemática) · amarelo = armadilha · verde = atalho/dica · vermelho = erro.
> O que está abaixo (visual, CTA, capa, publicação) continua valendo; o roteiro passa a seguir o modelo novo.
>
> **Imagens (EM TESTE desde 2026-10-09, no ep1 da Cartografia; o usuário decide se vira padrão):**
> - **Ilustrações do cotidiano** (sala de aula, xerox, celular, rua...): geradas pela OpenAI com `_ferramentas/gerar_imagem.py`
>   (chave em `~/.config/ia-imagens.env`), salvas em `<episódio>/assets/ia/`. **Nunca com texto dentro**; rótulos são desenhados por cima.
>   Se a cena precisa de um mapa "no cenário" (ex.: pôster na parede), peça o objeto **em branco** e encaixe o mapa real por cima.
> - **Mapas**: sempre dados reais via `_ferramentas/mapas.py` (Natural Earth; projeções equirretangular, Mercator, Peters).
>   A IA nunca desenha mapa que o aluno vai ler. Em escalas locais/regionais, use região genérica ou mapa de cidade
>   (um país real com "1 cm = 5 km" fica errado).
> **Desde 2026-10-25: Matemática tem design system próprio** — `_ferramentas/matematica.py` (paleta azul-noite com
> âmbar/ciano/menta/coral, quadro de contas, figuras, legenda que vira notação). É o padrão para os vídeos de matemática
> novos (aulas e questões). **Questões resolvidas** ficam separadas das aulas, em `questoes/` (guia: [questoes/ESTILO.md](questoes/ESTILO.md)),
> e sempre terminam convidando para as aulas do assunto no canal. **Estudativo English** (versão em inglês, focada em
> Matemática) = `--lang en` no mesmo projeto; só alguns vídeos ganham versão em inglês ([canal_en.md](canal_en.md)).

Referências: Física `003`–`009` (o 009, Vetores, é o mais recente) · Matemática `010_enem_matematica_conjuntos` · Química `011_enem_quimica_materia` · Geografia `012_enem_geografia_cartografia` · Linguagens `013_enem_linguagens_compreensao` · Redação `014_enem_redacao_leitura_proposta`.

## O que troca entre as matérias
O visual, o tom e a estrutura são os mesmos. Só muda o nome da matéria:

| Item | Física | Matemática | Química | Geografia | Linguagens | Redação |
|---|---|---|---|---|---|---|
| Material | `Estudos/Enem/estudos/03-fisica/` | `Estudos/Enem/estudos/01-matematica/` | `Estudos/Enem/estudos/02-quimica/` | `Estudos/Enem/estudos/04-geografia/` | `Estudos/Enem/estudos/05-linguagens/` | `Estudos/Enem/estudos/06-redacao/` |
| Pasta / arquivo | `NNN_enem_fisica_<assunto>` · `enem_fisica_<assunto>.mp4` | `NNN_enem_matematica_<assunto>` · `enem_matematica_<assunto>.mp4` | `NNN_enem_quimica_<assunto>` · `enem_quimica_<assunto>.mp4` | `NNN_enem_geografia_<assunto>` · `enem_geografia_<assunto>.mp4` | `NNN_enem_linguagens_<assunto>` · `enem_linguagens_<assunto>.mp4` | `NNN_enem_redacao_<assunto>` · `enem_redacao_<assunto>.mp4` |
| Primeira cena / selo da capa | `"FÍSICA ENEM"` | `"MATEMÁTICA ENEM"` | `"QUÍMICA ENEM"` | `"GEOGRAFIA ENEM"` | `"LINGUAGENS ENEM"` | `"REDAÇÃO ENEM"` |
| CTA | "...toda a **Física** do ENEM do zero" | "...toda a **Matemática** do ENEM do zero" | "...toda a **Química** do ENEM do zero" | "...toda a **Geografia** do ENEM do zero" | "...acompanhar **Linguagens** do ENEM do zero" | "...acompanhar **a Redação** do ENEM do zero" |
| Hashtags | `#ENEM #FisicaENEM #<Assunto>` | `#ENEM #MatematicaENEM #<Assunto>` | `#ENEM #QuimicaENEM #<Assunto>` | `#ENEM #GeografiaENEM #<Assunto>` | `#ENEM #LinguagensENEM #InterpretacaoDeTexto` | `#ENEM #RedacaoENEM #<Assunto>` |
| Playlist | "Física ENEM do Zero" | "Matemática ENEM do Zero" | "Química ENEM do Zero" | "Geografia ENEM do Zero" | "Linguagens ENEM do Zero" | "Redação ENEM do Zero" |

A numeração `NNN` é única dentro de `canais/enem/` (as três matérias seguem a mesma sequência).
Química: no roteiro, fórmulas escritas como se fala ("O dois", "H dois O", "C O dois"); na tela, com subscrito (O₂, H₂O),
que a Inter tem. Na narração, "graus" por extenso; na tela, "°C".
Linguagens (desde 2026-10-13): texto-base sempre IDÊNTICO ao material; na leitura, o texto fica inteiro na tela com marca-texto acompanhando a voz.
Cores: azul = tese/definição · verde = pista/palavra-sinal (mas, porém) · amarelo = armadilha · vermelho = erro · roxo = regra.
Geografia: escalas faladas por extenso ("um para duzentos e cinquenta mil"); na tela, `1 : 250 000`. Mapas são estilizados
(contornos em `visual.py` do 012: AFRICA, GREENLAND, BRASIL, EUROPA; globo com paralelos e meridianos) — sem dados externos.
Símbolos que a fonte Inter não tem (ℕ ℤ ℚ ℝ 𝕀 ⊂ ∪ ∩, subscrito ᵧ): usar o `ftext` do `visual.py` do 010, que cai para a
Segoe UI Symbol só nesses caracteres. Nunca usar esses símbolos em `head`, `pill`, `cards_row` ou `errors_list` (saem como quadradinho).

## Identidade
| Item | Padrão |
|---|---|
| Público | Estudante do ensino médio / vestibulando, começando do zero |
| Origem do conteúdo | Material de estudos do usuário: `Estudos/Enem/estudos/03-fisica/NN-<assunto>.html` (citar no cabeçalho do `cenas.py`) |
| Tom | Professor próximo e paciente; explica com coisas do dia a dia (Wi-Fi, micro-ondas, sirene, celular) |
| Duração | 7 a 9 min |
| Tema visual | **`motor.set_theme("claro")`** (off-white, cartões brancos, azul #3B6CF6) |
| Pasta | `canais/enem/NNN_enem_fisica_<assunto>/` · arquivo final `enem_fisica_<assunto>.mp4` |
| Componentes | `from aula import *` (questão/resolução, frações, ondas, lista de erros, CTA) |

## Roteiro
- Cabeçalho: `# Roteiro — ENEM Física NN: <assunto>` + `# Base: <caminho do HTML>`.
- `TITULO = "<Assunto> — Física ENEM"` (ou "... — Física ENEM do zero").
- **Gancho = surpresa ou dado curioso** do cotidiano ("Você sabia que metade dos erros de Física no ENEM não é de conceito?",
  "o rádio e o raio X... são a mesma onda").
- **Mapa da aula**: "Nesta aula: [p=0.2] {a}... {b}... {c}... {d}..." (3 ou 4 itens).
- Blocos curtos: conceito → **fórmula** → **exemplo resolvido** ("Exemplo:" com conta falada passo a passo) → aplicação no dia a dia.
- Marcadores falados: "Guarde esta regra:", "E uma pegadinha clássica:", "Uma dica para não inverter...",
  "E agora, a ideia mais importante da aula."
- Antes do CTA: bloco **"Os erros que mais custam pontos"** (lista de 4–5 erros).
- `PRONUNCIA`: `"ENEM": "Enem"`, unidades e siglas por extenso (`"kWh": "quilowatt-hora"`, `"UV": "U V"`, `"SI": "S I"`).

**CTA (texto fixo; o canal se chama Estudativo desde 2026-10-19):**
> Se essa aula te ajudou, deixe o seu *like,* *inscreva-se* no *Estudativo* e ative o *sininho,* para acompanhar **toda a <Matéria> do ENEM do zero.**
> E me conte nos *comentários:* <pergunta sobre o assunto>? **Bons estudos, e *até a próxima aula* aqui no Estudativo.**

No `cenas.py`: `"{sub}*inscreva-se* no *Estudativo* [p=0.2] "` e `"{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"`.
Na tela: `cta(..., pergunta, canal="no Estudativo")` (o cartão do meio mostra "INSCREVA-SE / no Estudativo").

Despedida na tela: **"Bons estudos!"** (padrão do `aula.cta`).

**Flashcards (Anki), obrigatório desde 2026-10-23 em TODAS as aulas ENEM:** depois da pergunta dos comentários e antes do {bye}:
`"{anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "`
Na tela: `cta(..., canal="no Estudativo", anki=C["NN.anki"])` (cartão verde "Flashcards do ENEM (Anki) · link na descrição do vídeo").
No `publicacao.md`: linha "📚 Flashcards do ENEM (Anki): [LINK DOS FLASHCARDS]" logo no início da descrição. O espaço reservado fica assim até o usuário mandar o link; depois, trocar em todos os publicacao.md (grep "LINK DOS FLASHCARDS").

## Visual
- Primeira cena: `head(... "FÍSICA ENEM", "<ASSUNTO EM CAIXA ALTA>")`.
- Área de conteúdo padrão `CARD_R = (140, 150, 1640, 690)`.
- Cor do título por tipo de bloco: **azul** = conceito/exemplo · **âmbar** = dica / ideia-chave ·
  **vermelho** = pegadinha / erros · **verde** = resposta / "não ionizante"-tipo "está tudo bem" · **roxo** = visão geral (espectro, mapa).
  O assunto pode ter cores próprias (ex.: cada faixa do espectro tem a sua), mas mantenha-as iguais no vídeo e na capa.
- Questões: `stmt_card` ("QUESTÃO") à esquerda + `sol_card` ("RESOLUÇÃO") à direita + `result_box` com a resposta.
- Fórmulas e números em notação matemática na tela (c = λ · f, 3 · 10⁸ m/s), com `frac` / `seq`.
- Ondas desenhadas com `aula.wave` animadas pela fase (movimento contínuo e suave).
- Lista de erros: `errors_list` (✗ errado em preto · ✓ certo em verde).

## Capa
- Tema claro, **selo no topo**: pílula azul `"FÍSICA ENEM · <ASSUNTO>"` (x=84, y=90).
- Texto à esquerda em 3 níveis: 2 linhas em preto + palavra-chave numa caixa colorida + subtítulo cinza
  terminando em "no ENEM" ou "espectro eletromagnético" etc.
- Cartão à direita com uma ilustração simples do tema (faixas do espectro, celular, folha).
- Ganchos: surpresa conceitual (A), dúvida popular (B), curiosidade (C).

## Publicação
- Cabeçalho: `# Publicação no YouTube — Física ENEM · <Assunto> (vídeo NNN)`.
- Título: gancho + "| Física ENEM" ou "| <Assunto> ENEM" (ex.: "Rádio e Raio X São a Mesma Onda | Espectro Eletromagnético ENEM").
- Descrição: "Nesta aula de Física para o ENEM, você aprende..." · resumo com fórmulas · CTA "para acompanhar toda a Física do ENEM do zero".
- Hashtags: `#ENEM #FisicaENEM #<Assunto>`.
- Tags sempre com: enem, física enem, fisica para o enem, enem 2026, física do zero, aula de física, revisão enem, vestibular.
- Playlist: **"Física ENEM do Zero"**. Cards ligam aos vídeos do mesmo bloco (ex.: Ondas 004–008).
- Comentário fixado = "📋 Cola de revisão desta aula".
- Publicar fim de tarde/noite (18h–21h) ou domingo.

## Shorts (desde 2026-10-17)
- Recortados do vídeo final do episódio, sem re-render: `<episódio>/shorts/shortN_<tema>.py` (ffmpeg) + `shortN_publicacao.md`.
  Modelo: `010_enem_matematica_conjuntos/ep1_ordem_e_sinais/shorts/` — `short_base.py` (layout + ffmpeg, função `gerar`)
  e um arquivo curto por Short com trechos e as 2 linhas do topo (a fonte da linha encolhe sozinha se não couber).
- 1080x1920, até ~45 s. Selo "MATEMÁTICA ENEM" (matéria do canal) + pergunta-gancho fixa no topo, recorte da aula no meio
  (bordas esfumadas), legenda queimada recortada e ampliada logo abaixo, rodapé "Aula completa no canal · <playlist> · Episódio N".
- Se o trecho começa no meio de um raciocínio, abrir com o gancho do início do episódio (cortes no silêncio entre frases,
  usando os tempos de `audio/tempos.json`).
- Publicação: título com `#shorts`, "Vídeo relacionado" = episódio completo, comentário fixado com a pergunta do gancho.

### Short-convite de série (desde 2026-10-20)
- Para anunciar uma série pronta: `<série>/convite_short/convite.py` (PIL + ffmpeg, frame a frame) com narração própria
  (`gerar_voz.py` → Gemini TTS local) e um trecho mudo de cada episódio num cartão. Modelo: `010_enem_matematica_conjuntos/convite_short/`.
- Ordem: gancho (dor) → "PRONTAS!" + nome da série + bolinhas dos episódios → 1 bloco por episódio (pílula EPISÓDIO N, título 2 linhas,
  trecho, trilha 1–5) → logo Estudativo + busca digitando "Estudativo" + playlist + INSCREVA-SE + sininho + "Bons estudos!".
- ~40 s, legenda palavra a palavra (laranja = palavra dita) em y≈1530, fora da área dos botões das redes. Mesmo arquivo para YouTube, Reels e TikTok.

## Atalhos e macetes em exatas (desde 2026-10-22, pedido do usuário)
- Matemática, Física e Química: todo procedimento ganha o seu **atalho de prova** (cor verde), priorizando o método mais rápido.
  Ex.: MMC e MDC pela **decomposição simultânea** (um varal só: MMC = todos os primos; MDC = só os primos que dividiram todos juntos).
- Toda fórmula de outro assunto que aparecer (ex.: perímetro numa questão de MDC) ganha uma explicação rápida na hora,
  em uma ou duas frases, sem virar aula paralela.
