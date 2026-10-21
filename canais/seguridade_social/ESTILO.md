# Canal Seguridade Social (concurso INSS): guia de estilo

Leia antes o [ESTILO_COMUM.md](../../ESTILO_COMUM.md). Aqui está só o que é **próprio deste canal**.
Numeração e ordem dos vídeos: [PLANO_DE_VIDEOS.md](PLANO_DE_VIDEOS.md) (001 → 049, publicados nessa ordem).
Referências: `001_conceito_e_tripe` até `004_financiamento_fontes`.

## Identidade
| Item | Padrão |
|---|---|
| Público | Concurseiro do INSS (Técnico do Seguro Social), banca no estilo Cebraspe (certo/errado) |
| Origem do conteúdo | `Estudos/Seguridade Social/modulos/MNN-<assunto>.md` (1 módulo = 1 vídeo; alguns divididos em 2) |
| Tom | Professor de cursinho: preciso com a lei, foca no que **cai na prova** e nas **pegadinhas da banca** |
| Duração | 5 a 7 min |
| Tema visual | **`motor.set_theme("seguridade")`**: base clara do ENEM com destaque **verde-petróleo #0F766E** (BLUE) e roxo #4F46E5 |
| Pasta | `canais/seguridade_social/NNN_<slug>/` · arquivo final `seguridade_NNN_<slug>.mp4` |
| Série | Cada vídeo é uma **"Aula N"** de um curso contínuo; temporadas = volumes do material = playlists |

## Cores fixas do canal
| Uso | Cor |
|---|---|
| Saúde | `#E5484D` (vermelho) |
| Previdência / prestações / lei | `#0F766E` (verde-petróleo) |
| Assistência / custeio / macete | `#E8A317` (âmbar) |
| Gestão / outras fontes | `#4F46E5` (roxo) |
| Certo / resumo | verde `#16A36A` · Errado / pegadinha: vermelho |

Use sempre essas cores para os três pilares, no vídeo e na capa.

## Roteiro
- Cabeçalho: `# Roteiro — Seguridade Social NNN: <assunto> (Módulo MNN)` + `# Base: <caminho do .md>`.
- **Gancho = a prova**: "Se você vai fazer o concurso do INSS...", "é exatamente aqui que a banca derruba muita gente",
  ou uma pergunta concreta ("de onde vem esse dinheiro?").
- **Base legal sempre citada** e falada por extenso: "artigo cento e noventa e cinco da Constituição",
  "Lei oito mil, duzentos e doze". Na tela: "CF, art. 195", "LEI 8.212/1991 · ART. 11".
- **Macetes com siglas** para decorar (S-P-A, E-T-C-I, F-R-L = "farol") e frase de ouro ("Seguridade é o *gênero*...").
- Marcadores falados: "Guarde esta frase:", "E aqui está o ponto de ouro", "A banca adora...", "Isso cai."
- **Questões certo/errado** no formato da banca: "Questão: <afirmação>. [p=0.5] *Errado!* [p=0.3] <explicação>".
- Antes do resumo: **"rodada de pegadinhas"** (3 afirmações, cada uma com *Certo* / *Errado* + correção).
- Resumo: "Resumindo:" com os pontos-chave e os macetes repetidos.
- CTA começa **anunciando a próxima aula** do plano.
- `PRONUNCIA`: siglas soletradas (`"INSS": "I N S S"`, `"RGPS": "R G P S"`, `"BPC": "B P C"`, `"CSLL": "C S L L"`);
  siglas que se leem como palavra ficam (`"SUS"`, `"LOAS"`, `"COFINS": "Cofins"`).

**CTA (texto fixo):**
> Na próxima aula, <assunto da próxima aula>. [p=0.4]
> Se essa aula te ajudou, deixe o seu *like,* *inscreva-se* no *Estudativo* e ative o *sininho,* para acompanhar **a preparação completa para o INSS.**
> E me conte nos *comentários:* <pergunta>? **Bons estudos, e *até a próxima aula* aqui no Estudativo.**

O canal se chama **Estudativo** desde 2026-10-19 (mesmo canal das aulas ENEM). No `cenas.py`: `"{sub}*inscreva-se* no *Estudativo* [p=0.2] "`
e `"{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"`. Na tela: `cta(..., pergunta, canal="no Estudativo")`.

Despedida na tela: **"Bons estudos!"**.

**PDF do canal (desde a Aula 10, 17/10/2026):** a apostila completa
(`canais/seguridade_social/material/Seguridade-Social-Apostila-Completa-INSS.pdf`, 633 p., gerada por
`Estudos/Seguridade Social/tools/build_pdf.py`) é oferecida com link na descrição.
- No CTA, entre o anúncio da próxima aula e o like, uma frase `{pdf}` (ex.: "E se você quer estudar tudo isso com calma,
  deixei na *descrição* o link do *PDF completo* de Seguridade Social...") com o cartão `pdf_card()` do `010/roteiro/visual.py`.
- Na descrição, logo antes de "📌 O que você vai aprender", a linha
  `📘 PDF completo de Seguridade Social para o INSS (39 módulos, pegadinhas e simulados comentados): [LINK DO PDF]`.

**Voz (desde a Aula 10):** mais emoção. No `cenas.py`, `VOZ = dict(tags=["alegre", "curiosa"], prompt=...)`
(professor apaixonado, entonação variada, surpresa nas pegadinhas, firmeza no "Errado!", sem acelerar);
o `gerar_voz_local.py` envia isso como `tags` + `customPrompt`. Escrever o roteiro com perguntas e exclamações ajuda.

## Visual
- Área de conteúdo `CARD_R = (140, 150, 1640, 690)`; componentes de `aula.py`.
- Títulos: "INCISO I / EMPREGADOR E EMPRESA", "PONTO DE OURO / ...", "PEGADINHAS / CERTO OU ERRADO?",
  "RESUMO / O QUE LEVAR PARA A PROVA", "QUESTÃO DE PROVA / ...".
- **Questão C/E**: cartão grande com pílula "C / E", a afirmação linha a linha, `result_box` CERTO (verde) ou ERRADO (vermelho)
  e a explicação numa pílula embaixo (função `ce()` do 004 — reaproveitar).
- **Tag de inciso** (algarismo romano em caixa colorida, função `inciso_tag`) e letras grandes para os macetes.
- Texto de lei aparece em cartão, com as palavras-chave destacadas.

## Capa
- **Selo no topo**: pílula verde-petróleo `"SEGURIDADE SOCIAL · INSS"` (x=84, y=90).
- Texto à esquerda: 2 linhas em preto + palavra-chave em caixa colorida ("INSS?", "ART. 195", "SOCIAL") + subtítulo cinza.
- Cartão à direita com o **macete** ou o esquema (letras E-T-C-I, F-R-L, direta x indireta).
- Ganchos: pergunta curiosa (A), macete (B), direto ao ponto com o nome do tema (C).

## Publicação
- Cabeçalho: `# Publicação no YouTube — Seguridade Social · Aula N (vídeo NNN)` + linha **Fonte:** módulo e dispositivos legais.
- Título: gancho + base legal + "INSS" (ex.: "De Onde Vem o Dinheiro do INSS? Financiamento da Seguridade (Art. 195)",
  "... | Aula 4 INSS").
- Descrição começa com "**Aula N da preparação completa de Seguridade Social para o concurso do INSS.**"
  e termina com `➡️ Próxima aula: ...`.
- Hashtags: `#INSS #SeguridadeSocial #ConcursoINSS` (sempre as mesmas).
- Tags sempre com: inss, concurso inss, técnico do seguro social, seguridade social, direito previdenciário, cebraspe inss, questões inss, pegadinhas inss, concurso público.
- Playlists: **"Seguridade Social para o INSS — Temporada N: <nome>"** + **"Curso Completo"**.
- Tela final: vídeo da aula anterior até a próxima sair; card para a aula que introduziu o conceito.
- Comentário fixado = "📋 Cola de revisão da Aula N".
- Publicar 19h–21h em dia útil ou sábado de manhã.
