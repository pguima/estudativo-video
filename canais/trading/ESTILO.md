# Canal Trading (ICT / Smart Money): guia de estilo

Leia antes o [ESTILO_COMUM.md](../../ESTILO_COMUM.md). Aqui está só o que é **próprio deste canal**.
Referências: `001_2tVWDa3uXQw` (Fair Value Gap) e `002_videoplayback1` (Candle Range Theory, o padrão atual).

## Identidade
| Item | Padrão |
|---|---|
| Público | Trader iniciante/intermediário de day trade (índice, Nasdaq, forex) |
| Origem do conteúdo | Aulas em inglês de ICT/Smart Money, **roteiro reescrito do zero** com estrutura própria |
| Tom | Mentor experiente, direto, firme; fala em 1ª pessoa ("eu quero ver", "eu espero") e com "você" |
| Duração | 8 a 9 min |
| Tema visual | **`motor.set_theme("escuro")`** (fundo #0D1117, cartões #161B22). O 001 foi feito no tema claro; do 002 em diante, escuro |
| Pasta | `canais/trading/NNN_<slug>/` · arquivo final `<assunto>_PTBR.mp4` |

## Roteiro
- **Gancho = a dor do trader**: uma cena em que ele perde dinheiro ("você vende... só que o preço nunca volta",
  "é estopado logo antes do movimento"). Depois, a promessa: "hoje você vai aprender a não fazer isso".
- **Mapa da aula** curto ("Nesta aula, eu vou te mostrar... Primeiro... Depois... E só se...").
- Conteúdo em **passos numerados** ("Passo um:", "Passo dois:") e **regras** ("Regra número um", "Regra de ouro").
- **Exemplos completos no gráfico**, sempre fechando com: entrada → stop → alvo → "Deixe correr." `[p=2.8]` → "*Alvo atingido.*"
- Bordões do canal: "pavio não é fechamento", "você não força", "faltou um? então você pula a operação".
- Fechamento: **checklist ou fluxo completo** → CTA.
- `PRONUNCIA`: siglas soletradas (`"CRT": "C R T"`, `"FVG": "F V G"`, `"CISD": "C I S D"`, `"ICT": "I C T"`, `"2R": "dois R"`).
  Termos em inglês que a voz erra: grafia fonética (`"Consequent": "Cónsequent"`, `"Encroachment": "Encróutchment"`).
  Prefira "CE / ponto de 50%". Termos técnicos ficam em inglês (Fair Value Gap, CISD, PDH/PDL), com tradução na 1ª vez.

**CTA (texto fixo):**
> Se essa aula te ajudou, deixe o seu *like,* *inscreva-se* no canal, e ative o *sininho,* para não perder as próximas aulas.
> E me conte nos *comentários:* <pergunta sobre a estratégia>? **Bons trades, e *até a próxima.***

Despedida na tela: **"Bons trades!"**

## Visual
- **Gráficos de candles** (`motor.Chart`) são o centro de quase toda cena; use zoom de câmera (`Chart.view`)
  em gráficos longos. Candles gerados com `K()` e `walk()` (seed fixa para ser reproduzível).
- Verde = candle de alta / compra / alvo · vermelho = baixa / venda / stop · âmbar = níveis marcados
  (máxima/mínima do dia anterior, linhas tracejadas) · azul = conceito/passo · roxo = sessão de Londres.
- `title_chip` no topo de cada bloco: "PASSO 1 / O CANDLE DIÁRIO", "REGRA DE OURO / PAVIO NÃO É FECHAMENTO",
  "EXEMPLO 1 / CONTINUAÇÃO", "RESUMO / O FLUXO COMPLETO".
- Pílulas de rótulo sobre o gráfico ("MÁXIMA DO DIA ANTERIOR", "PDH", "CISD", "ENTRADA", "STOP", "ALVO 2R").
- CTA com `b_cta` próprio do vídeo (mesmo layout do `aula.cta`), botão "INSCRITO" escurecendo para #30363D.

## Capa
- Tema escuro. Painel com gráfico de candles à direita (x=1040, 820x840) com nível tracejado âmbar e setas.
- Texto à esquerda: dúvida ou dor ("REVERSÃO OU CONTINUAÇÃO?", "PARE DE MUDAR DE IDEIA", "1 CANDLE DECIDE SEU DIA").
- Pílula embaixo com o nome da estratégia ("CANDLE RANGE THEORY · CRT").
- **Sem selo de canal no topo** (diferente de ENEM e Seguridade).

## Publicação
- Título: nome da estratégia + sigla + promessa ("Candle Range Theory (CRT): Reversão ou Continuação? Estratégia Completa").
- Descrição inclui bloco **📋 O fluxo** (passos numerados) e **sempre** o aviso:
  `⚠️ Aviso: conteúdo exclusivamente educacional. Não é recomendação de investimento. Operar no mercado financeiro envolve risco de perda de capital. Os exemplos são ilustrativos.`
- Hashtags: `#<Estratégia> #<Sigla> #DayTrade` (ex.: `#CandleRangeTheory #CRT #DayTrade`).
- Playlist: **"ICT / Smart Money do Zero"**. Cards e tela final apontam para os outros vídeos de ICT.
- Seção "Sobre originalidade" explicando que o roteiro e o visual foram refeitos.
- Publicar em dia útil, 18h–20h.
