# Empréstimos, Financiamentos e Parcelamentos — série de videoaulas

Material de apoio: `01-matematica/17-emprestimos-financiamentos-parcelamentos.html` · Incidência: Média

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Levar ao futuro × (1 + i)ⁿ e trazer ao presente ÷ (1 + i)ⁿ | **Juros Compostos** (série 14, seção 07 e Q3) | Revisão relâmpago. O novo é a **sequência de parcelas**, cada uma pelo seu prazo, e o rotativo como "levar a dívida ao futuro". |
| **Questão 8 do material** (2.420 ÷ 1,21 = 2.000, quitação antecipada) | Mesma conta e mesmos distratores (÷ 1,1; × 0,9; × 1,21) da **Questão 3 de Juros Compostos** (12.100 ÷ 1,21) | **Não uso.** Entra uma questão nova de quitação de **três** parcelas de R$ 1.331,00, com o texto completo no prompt do vídeo 1. |
| Taxa embutida com entrada | **Juros Simples** (série 13, Q8, pagamento em 2 meses) | Citada no vídeo 2; aqui o formato mais cobrado, uma parcela em 30 dias (com um único período, simples e compostos dão o mesmo). |
| Soma dos juros do SAC como PA | **Progressão aritmética** (31) tem série própria | Uso só a fórmula dada no material, com a promessa da série própria. |
| Taxa mensal de dois dígitos vira anual de três (rotativo) | **Taxas Equivalentes**, vídeo 1 | Só citado. |
| Pagar à vista ou parcelar | **Comparação de propostas** (18) | Só prometido. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Dinheiro em datas diferentes: parcelas, quitação e rotativo** | 03, 09 | Q7, Q6, Nova (no lugar da Q8) | 10–12 min |
| **2. Entrada mais uma parcela e o falso "sem juros"** | 02 (valor financiado, entrada), 04, 05 | Q1 | 6–8 min |
| **3. Sistema de Amortização Constante (SAC)** | 02 (saldo, juros, amortização, parcela), 06 | Q2, Q3 | 8–10 min |
| **4. Sistema Price e SAC × Price** | 07, 08 | Q4, Q9, Q5 | 10–12 min |
| **5. Revisão** | 01, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Vídeo 1: Dinheiro em datas diferentes: parcelas, quitação e rotativo

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática Básica — Empréstimos, Financiamentos e Parcelamentos — Episódio 1 de 5:
Dinheiro em datas diferentes: parcelas, quitação antecipada e rotativo do cartão
RECORTE: use APENAS as seções 03 e 09 do material de apoio, mais as Questões 7 e 6 da
seção 12 e a QUESTÃO NOVA escrita abaixo. NÃO use a Questão 8 do material: ela repete a
conta de uma questão da série de Juros Compostos. Levar um valor ao futuro e trazê-lo ao
presente já foi ensinado na série de Juros Compostos: aqui, revisão rápida. O novo é
somar uma SEQUÊNCIA de parcelas, cada uma pelo seu prazo.
DURAÇÃO: 10 a 12 minutos

QUESTÃO NOVA (use no lugar da Questão 8 do material):
"Um cliente deve as três últimas parcelas de um financiamento, de R$ 1.331,00 cada, com
vencimentos daqui a 1, 2 e 3 meses. O contrato permite quitar a dívida hoje, trazendo
cada parcela ao presente pela taxa do financiamento, 10% ao mês, no regime composto.
Considere 1,1² = 1,21 e 1,1³ = 1,331. Para quitar a dívida hoje, o cliente deve pagar
A) R$ 3.000,00.  B) R$ 3.310,00.  C) R$ 3.593,70.  D) R$ 3.630,00.  E) R$ 3.993,00."
Gabarito: B. Resolução: 1.331 ÷ 1,1 = 1.210; 1.331 ÷ 1,21 = 1.100; 1.331 ÷ 1,331 = 1.000;
total 1.210 + 1.100 + 1.000 = R$ 3.310,00. A desconta as três por 3 meses (3 · 1.000); C
tira 10% de cada parcela uma única vez (3 · 1.197,90), como desconto simples; D desconta
as três por 1 mês só (3 · 1.210); E soma as parcelas sem trazer ao presente (3 · 1.331).

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por um carnê com parcelas e datas de vencimento,
   por um aviso de "quite seu financiamento com desconto" e pela fatura do cartão com o
   botão "pagar o mínimo".
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (valor presente, valor futuro, linha do tempo, data zero, parcela, quitação
   antecipada, fatura, rotativo, cheque especial, saldo não pago).
3. Analogias âncora, retomadas ao longo da aula:
   - "valores em datas diferentes são moedas de países diferentes: antes de somar, faça
     o câmbio para a mesma data";
   - "para o futuro, multiplique pelo fator; para o presente, divida. Cada parcela viaja
     pelo SEU prazo";
   - "juros são o aluguel do dinheiro: só se paga aluguel do que ainda está com você"
     (o saldo não pago, não a fatura inteira).
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: M = C(1 + i)^t e
   C = M ÷ (1 + i)^t, e as potências 1,1² = 1,21 e 1,1³ = 1,331 (série de Juros
   Compostos).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; desenhe a linha do tempo
   (traço horizontal, datas 0, 1, 2, 3, setas) antes de qualquer conta.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Duas parcelas de R$ 1.210,00 somam R$ 2.420,00, certo? Na
  calculadora, sim. No tempo, a 10% ao mês, elas valem hoje R$ 2.100,00. Somar parcelas
  de datas diferentes é somar real com dólar."
- Promessa: "ao final, você vai calcular quanto vale hoje uma sequência de parcelas,
  quanto custa quitar uma dívida antes do prazo e quanto cresce o rotativo do cartão".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) R$ 1.000,00 hoje não valem o mesmo que R$ 1.000,00 daqui a um mês, porque o dinheiro
     de hoje pode render juros;
  b) levar e trazer: valor hoje = valor futuro ÷ (1 + i)^n; R$ 2.662,00 em 3 meses a 10%
     → 2.662 ÷ 1,331 = R$ 2.000,00;
  c) sequência de parcelas: cada uma volta pelo seu prazo (a de 1 mês ÷ 1,1, a de
     2 meses ÷ 1,21); duas de R$ 1.210,00 → 1.100 + 1.000 = R$ 2.100,00; esse é o valor
     justo para comprar à vista ou quitar antes;
  d) rotativo: fatura de R$ 2.000,00, pagou R$ 500,00, juros de 12% ao mês → saldo de
     1.500 → próxima fatura 1.500 · 1,12 = R$ 1.680,00; sem pagar nada por 3 meses,
     1.500 · 1,12³ ≈ 1.500 · 1,405 ≈ R$ 2.107,50; três meses a 12% somam cerca de 40,5%,
     não 36%; o cheque especial funciona igual sobre o saldo negativo (taxas mensais
     assim viram taxas anuais de três dígitos, como na série de Taxas Equivalentes).
- Exercício "nós fazemos": peça "pause: quanto valem hoje uma parcela de R$ 1.100,00
  daqui a 1 mês e outra de R$ 1.210,00 daqui a 2 meses, a 10% ao mês?" (1.100 ÷ 1,1 =
  1.000; 1.210 ÷ 1,21 = 1.000; total R$ 2.000,00).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Só se somam valores na mesma data."
  "Para o futuro, multiplique pelo fator; para o presente, divida."
  "Juros incidem sobre o que ainda se deve."
- Erros clássicos:
  • somar parcelas de datas diferentes (duas de 1.210 a 10% valem 2.100 hoje, não 2.420);
  • descontar todas as parcelas pelo mesmo prazo;
  • juros simples no rotativo (dois meses a 10% multiplicam por 1,21, não por 1,20).
- Questões no estilo ENEM, nesta ordem:
  • Questão 7 do material (fatura de R$ 1.000,00, pagou R$ 200,00, 10% ao mês, dois
    meses): "eu faço"; 800 · 1,21 = R$ 968,00; mostre que E aplica juros sobre a fatura
    inteira e D soma de volta o que já foi pago;
  • Questão 6 (duas parcelas de R$ 1.210,00 em 30 e 60 dias): "nós fazemos";
  • QUESTÃO NOVA (três parcelas de R$ 1.331,00): "você faz", com pausa, resolvida e
    explicada como no texto acima.
  Em todas: desenhe a linha do tempo, identifique quanto se deve em cada data, resolva,
  confira a plausibilidade (o valor hoje é MENOR que a soma das parcelas) e explique as
  alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "geladeira: R$ 1.900,00 à vista ou 2 × R$ 1.000,00, a
  primeira no ato. Os R$ 100,00 a mais são 5% de juros? São mais que o dobro disso.
  Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: uma linha do tempo com as parcelas como moedinhas em cada data;
  cada moedinha "viaja" de volta até a data zero passando por um guichê de câmbio que a
  divide por 1,1, 1,21 ou 1,331, e só lá elas se juntam numa pilha.
- A fatura do cartão: a parte paga sai da conta, e só o saldo não pago entra numa
  máquina que o multiplica por 1,12 a cada mês.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Cada parcela foi trazida ao presente pelo SEU prazo, e não todas pelo mesmo?
- As contas estão certas (2.662 ÷ 1,331 = 2.000; 800 · 1,21 = 968; QUESTÃO NOVA = 3.310)?
- A Questão 8 do material ficou de fora?
```

---

## Vídeo 2: Entrada mais uma parcela e o falso "sem juros"

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática Básica — Empréstimos, Financiamentos e Parcelamentos — Episódio 2 de 5:
Entrada mais uma parcela: a taxa embutida e o falso "sem juros"
RECORTE: use APENAS as seções 04 e 05 do material de apoio e, da seção 02, só os termos
"valor financiado" e "entrada", mais a Questão 1 da seção 12. A taxa embutida numa compra
com entrada já apareceu na série de Juros Simples (com pagamento em 2 meses): aqui, o
formato mais cobrado, uma única parcela em 30 dias. A decisão entre pagar à vista ou
parcelar fica para a série de Comparação de propostas.
DURAÇÃO: 6 a 8 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pelo cartaz de uma loja de eletrodomésticos
   ("R$ 1.900,00 à vista ou 2 × R$ 1.000,00, a primeira no ato") e por um anúncio
   "10× sem juros" com "ou R$ 900,00 à vista" em letra pequena.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (preço à vista, entrada, valor financiado, taxa embutida, juros embutidos,
   desconto à vista).
3. Analogias âncora, retomadas ao longo da aula:
   - "a entrada não viaja: ela é paga hoje, não é emprestada e não paga aluguel";
   - "a loja te 'empresta' só o que faltou pagar: o valor financiado é o preço à vista
     menos a entrada";
   - "o 'sem juros' com desconto à vista é um preço com fantasia: o preço real é o à
     vista, e a diferença são juros".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: "que porcentagem a parte
   representa? Divida pela base" (série de Porcentagem) e a linha do tempo do episódio 1.
   Com uma única parcela daqui a um período, juros simples e compostos dão o mesmo
   resultado (série de Juros Compostos), então a conta não depende do regime.
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; escreva sempre, na tela,
   "valor financiado = à vista − entrada" antes de dividir.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "R$ 100,00 de diferença numa geladeira de R$ 1.900,00 parece
  5%. Mas esses R$ 100,00 são o preço de adiar só R$ 900,00 por um mês: 11,1% ao mês."
- Promessa: "ao final, você vai descobrir a taxa escondida em qualquer 'entrada mais uma
  parcela' e desmascarar o 'sem juros'".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) o método em três linhas: a entrada é paga hoje, então não é financiada; o valor
     financiado é à vista − entrada; taxa = (parcela − financiado) ÷ financiado;
  b) a geladeira: financiado = 1.900 − 1.000 = 900; paga 1.000 depois de um mês; juros
     de 100 → 100 ÷ 900 ≈ 11,1% ao mês;
  c) os denominadores errados: 100 ÷ 1.900 ≈ 5,3% e 100 ÷ 2.000 = 5% escondem uma taxa
     mensal alta;
  d) o "sem juros" com desconto à vista: 10 × sem juros totalizando R$ 1.000,00 contra
     R$ 900,00 à vista → o preço real é R$ 900,00 e há R$ 100,00 de juros embutidos; o
     "sem juros" só é verdadeiro quando à vista e parcelado são iguais;
  e) com várias parcelas, o ENEM dá um fator ou pede só a comparação (série de
     Comparação de propostas).
- Exercício "nós fazemos": peça "pause: R$ 1.100,00 à vista ou 2 × R$ 600,00, a primeira
  no ato e a segunda em 30 dias. Qual é a taxa mensal embutida?" (financiado =
  1.100 − 600 = 500; juros = 600 − 500 = 100; 100 ÷ 500 = 20% ao mês).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "A entrada não é financiada: divida os juros só pelo que ficou para depois."
  "Taxa embutida = juros ÷ valor financiado."
  "Se existe desconto à vista, o 'sem juros' tem juros."
- Erros clássicos:
  • calcular a taxa sobre o preço total (a entrada não é financiada);
  • acreditar no "sem juros" quando há desconto à vista.
- Questões no estilo ENEM, nesta ordem:
  • "eu faço": o exemplo da geladeira (bloco b), já resolvido;
  • "nós fazemos": o exercício acima;
  • Questão 1 do material (2 × R$ 500,00 "sem juros" ou R$ 900,00 à vista): "você faz",
    com pausa; financiado = 400, juros = 100 → 25% ao mês; mostre que B, C e D dividem
    os R$ 100,00 por 1.000, 900 e 500, todos maiores que o valor realmente financiado, e
    que A acredita no anúncio.
  Em todas: desenhe a linha do tempo, separe a entrada, resolva, confira a
  plausibilidade e explique as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "num financiamento de R$ 10.000,00 em 5 parcelas, a
  dívida cai R$ 2.000,00 por mês. E os juros, caem também? Próximo episódio: SAC."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: a etiqueta da geladeira se partindo em duas; a parcela da entrada
  fica parada na data zero (selo "não viaja"), e só o pedaço de R$ 900,00 vai para a
  data de 30 dias e volta como R$ 1.000,00, com o "+100" destacado sobre os 900.
- Três frações lado a lado (100/2.000, 100/1.900, 100/900), as duas primeiras em
  vermelho e a última em verde.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Em todas as contas, o denominador foi o valor financiado (à vista − entrada)?
- A Questão 1 deu 25% (100 ÷ 400)?
- Ficou claro que o "sem juros" só é verdade quando à vista e parcelado são iguais?
```

---

## Vídeo 3: Sistema de Amortização Constante (SAC)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática Básica — Empréstimos, Financiamentos e Parcelamentos — Episódio 3 de 5:
O Sistema de Amortização Constante (SAC)
RECORTE: use APENAS a seção 06 do material de apoio e, da seção 02, os termos saldo
devedor, juros da parcela, amortização e parcela, com as três relações; mais as Questões
2 e 3 da seção 12. A soma dos juros usa a fórmula da soma de uma progressão aritmética,
que tem série própria (Progressão aritmética): aqui, só a fórmula, como está no material.
O sistema Price fica para o episódio 4.
DURAÇÃO: 8 a 10 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pelo extrato de um financiamento imobiliário, em
   que cada boleto vem um pouco mais barato que o anterior, e pela pergunta "por que a
   minha parcela diminui?".
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (saldo devedor, juros da parcela, amortização, parcela ou prestação, SAC,
   progressão aritmética).
3. Analogias âncora, retomadas ao longo da aula:
   - "no SAC, a dívida é fatiada em fatias iguais: a fatia (amortização) é sempre a
     mesma, e o juro emagrece porque a dívida emagrece";
   - "juros são o aluguel do dinheiro (episódio 1): só se paga aluguel do que ainda se
     deve, o saldo do início do mês";
   - "a escadinha dos juros: eles descem sempre o mesmo degrau, taxa × amortização".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: porcentagem de um valor
   (4% de 10.000 = 400, série de Porcentagem).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; monte a tabela linha a
   linha, sempre na ordem saldo → juros → amortização → parcela → novo saldo.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Você paga uma parcela de R$ 2.400,00 e a sua dívida cai só
  R$ 2.000,00. Para onde foram os outros R$ 400,00? Foram o aluguel do dinheiro."
- Promessa: "ao final, você vai montar a tabela do SAC, calcular qualquer parcela sem
  montar todas e somar os juros do contrato inteiro de uma vez".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) as três relações que valem em qualquer sistema: juros = i · saldo anterior;
     parcela = amortização + juros; novo saldo = saldo anterior − amortização (o saldo cai
     pela amortização, não pela parcela inteira);
  b) SAC: amortização = valor financiado ÷ número de parcelas; R$ 10.000,00 em 5
     parcelas a 4% ao mês → 2.000 por mês;
  c) a tabela da seção 06, linha a linha: juros 400, 320, 240, 160, 80; parcelas 2.400,
     2.320, 2.240, 2.160, 2.080; total de juros 1.200 e total pago 11.200;
  d) atalhos: os juros caem i · amortização = 4% · 2.000 = 80 por mês, e a parcela também;
     saldo no início da parcela k = financiado − (k − 1) · amortização;
  e) total de juros como soma de PA: (primeiro + último) × quantidade ÷ 2 =
     (400 + 80) · 5 ÷ 2 = 1.200 (PA tem série própria).
- Exercício "nós fazemos": peça "pause: R$ 12.000,00 em 4 parcelas pelo SAC, a 5% ao mês.
  Quanto vale a primeira parcela e quanto vale a última?" (amortização 3.000; primeira:
  juros 600 → R$ 3.600,00; última: saldo 3.000, juros 150 → R$ 3.150,00; total de juros
  (600 + 150) · 4 ÷ 2 = R$ 1.500,00).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "No SAC, a amortização é fixa e os juros caem junto com o saldo."
  "O saldo cai pela amortização, não pela parcela inteira."
  "Juros do SAC somam como PA: primeiro mais último, vezes quantidade, dividido por 2."
- Erros clássicos:
  • abater a parcela inteira do saldo (os juros não reduzem a dívida);
  • calcular os juros do SAC sobre o valor inicial em todo mês (eles caem em PA; somá-los
    como constantes superestima o custo).
- Questões no estilo ENEM, nesta ordem:
  • Questão 2 do material (R$ 60.000,00 em 10 parcelas, 1% ao mês, primeira parcela):
    "eu faço"; 6.000 + 600 = R$ 6.600,00; mostre que A e B são só uma das partes, C
    calcula juros sobre a amortização e E cobra os juros dos 10 meses de uma vez;
  • Questão 3 (total de juros do mesmo financiamento): "você faz", com pausa; juros
    600, 540, …, 60 → (600 + 60) · 10 ÷ 2 = R$ 3.300,00; mostre que A esquece que o
    último mês ainda tem juros de 60 e que C trata os juros como constantes.
  Em todas: monte a primeira linha da tabela, resolva, confira a plausibilidade e
  explique as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "e se o banco quiser que todas as parcelas sejam
  iguais? Quem paga mais juros no total, o SAC ou esse outro sistema? Próximo episódio:
  Price."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: uma barra da dívida de R$ 10.000,00 dividida em 5 fatias iguais de
  R$ 2.000,00; a cada mês uma fatia sai, e ao lado aparece uma faixa laranja de juros
  (4% do que sobrou) cada vez mais fina.
- A tabela da seção 06 sendo preenchida linha por linha, com a coluna dos juros descendo
  de 80 em 80 como uma escadinha.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Os juros de cada mês foram calculados sobre o saldo do INÍCIO do mês?
- A tabela confere (juros 400, 320, 240, 160, 80; total 1.200)?
- A Questão 3 deu R$ 3.300,00, com o último termo da PA igual a 60?
```

---

## Vídeo 4: Sistema Price e SAC × Price

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática Básica — Empréstimos, Financiamentos e Parcelamentos — Episódio 4 de 5:
O sistema Price (parcelas fixas) e a comparação SAC × Price
RECORTE: use APENAS as seções 07 e 08 do material de apoio, mais as Questões 4, 9 e 5
da seção 12. As três relações (juros, amortização, novo saldo) e o SAC são do episódio 3.
A fórmula da parcela da Price NÃO é cobrada: a prova dá o fator ou a parcela.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por um carnê de crediário com 12 parcelas iguais e
   pela pergunta "se a parcela é sempre igual, a dívida cai sempre o mesmo valor?".
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (sistema Price ou francês, parcela fixa, fator da Price, amortização
   crescente, crediário, financiamento imobiliário).
3. Analogias âncora, retomadas ao longo da aula:
   - "na Price, a parcela é uma caixa de tamanho fixo: dentro dela, o juro vai encolhendo
     e a amortização vai ocupando o espaço que sobra";
   - "no SAC, fatias iguais de dívida (episódio 3); na Price, caixas iguais de
     pagamento";
   - "antes de calcular juros, pergunte: quanto se deve AGORA?".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: as três relações e a
   tabela do SAC (episódio 3).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; na Price, sempre na
   ordem juros = taxa × saldo → amortização = parcela − juros → novo saldo.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Mesma dívida, mesma taxa, mesmo prazo. Num sistema você paga
  R$ 1.200,00 de juros; no outro, R$ 1.231,35. A taxa é igual. O que muda?"
- Promessa: "ao final, você vai calcular a parcela da Price com o fator dado, separar
  juros e amortização e dizer quando o SAC ou a Price paga menos".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) Price: todas as parcelas iguais; parcela = valor financiado × fator dado;
     R$ 10.000,00 em 5 parcelas a 4%, fator 0,224627 → parcela ≈ R$ 2.246,27;
  b) a tabela da seção 07, só as duas primeiras linhas: juros 400 e amortização 1.846,27
     (saldo 8.153,73); juros 326,15 e amortização 1.920,12 (saldo 6.233,61); os juros
     caem e a amortização cresce; o último mês absorve o arredondamento;
  c) a primeira linha é igual nos dois sistemas: juros de 400 no SAC e na Price; o que
     muda é a amortização (fixa no SAC; parcela − juros na Price);
  d) lado a lado (tabela da seção 08): amortização constante × crescente; parcela
     decrescente × constante; primeira parcela 2.400 no SAC × 2.246,27 na Price; total de
     juros 1.200 × 1.231,35;
  e) por que o SAC paga menos: a taxa é a mesma; o SAC abate a dívida mais depressa no
     começo, então o saldo sobre o qual incidem os juros fica menor mais cedo; SAC é comum
     no imobiliário, Price no crediário e no crédito pessoal (parcela previsível).
- Exercício "nós fazemos": peça "pause: R$ 5.000,00 pela Price em 5 parcelas de
  R$ 1.091,77, a 3% ao mês. Quanto da primeira parcela é juros, quanto amortiza e qual é
  o saldo depois dela?" (juros 3% · 5.000 = 150; amortização 1.091,77 − 150 = 941,77;
  saldo 5.000 − 941,77 = R$ 4.058,23).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Na Price, a parcela é fixa e a amortização cresce."
  "Na primeira parcela, os juros são iguais nos dois sistemas: taxa × valor financiado."
  "Mesma taxa, mas o SAC paga menos juros porque abate a dívida mais cedo."
- Erros clássicos:
  • achar que, na Price, a amortização é constante (constante é a parcela);
  • achar que SAC e Price custam os mesmos juros;
  • abater a parcela inteira do saldo (só a amortização abate).
- Questões no estilo ENEM, nesta ordem:
  • Questão 4 do material (R$ 20.000,00 em 12 parcelas, 2% ao mês, fator 0,0946): "eu
    faço"; parcela R$ 1.892,00, com a conferência de plausibilidade (sem juros seria
    20.000 ÷ 12 ≈ 1.666,67; com juros tem de ser um pouco maior);
  • Questão 9 (saldo após a primeira parcela do mesmo financiamento): "nós fazemos";
    juros 400, amortização 1.492, saldo R$ 18.508,00; mostre que B abate a parcela
    inteira e C usa a amortização do SAC;
  • Questão 5 (afirmação correta sobre SAC e Price): "você faz", com pausa; para cada
    alternativa errada, diga qual troca de sistema ela faz.
  Em todas: leia o enunciado, identifique o sistema, resolva, confira a plausibilidade
  e explique as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "no último episódio deste assunto, juntamos tudo,
  caçamos as pegadinhas e treinamos com questões inéditas."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: o gráfico da seção 08, com as parcelas mês a mês nos dois sistemas
  lado a lado; em azul, a parte que abate a dívida; em laranja, os juros. No SAC, as
  barras descem; na Price, as caixas têm a mesma altura, e o azul vai tomando o lugar
  do laranja.
- Uma caixa de tamanho fixo (a parcela da Price) sendo preenchida mês a mês: o bloco
  laranja (juros) encolhe e o azul (amortização) cresce.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Ficou claro que a fórmula da Price não é cobrada e que o fator vem dado?
- As contas estão certas (10.000 · 0,224627 ≈ 2.246,27; 20.000 · 0,0946 = 1.892;
  20.000 − 1.492 = 18.508)?
- A comparação diz que a primeira parcela do SAC é MAIOR e o total de juros do SAC é
  MENOR?
```

---

## Vídeo 5: Revisão (Empréstimos, financiamentos e parcelamentos no ENEM)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula de REVISÃO para o YouTube sobre:

TEMA: Matemática Básica — Empréstimos, Financiamentos e Parcelamentos — Episódio 5 de 5:
Revisão geral, estratégia de prova, pegadinhas e treino para o ENEM
RECORTE: use as seções 01, 10, 11 e 13 do material de apoio.
NÃO reutilize as Questões 1 a 9 da seção 12 nem a questão nova do episódio 1 (três
parcelas de R$ 1.331,00), já resolvidas nos episódios anteriores.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que assistiu aos episódios 1 a 4, mas ainda é iniciante e pode ter esquecido
partes. Relembre cada conceito em uma frase simples antes de cobrá-lo.

REGRAS DE EXPLICAÇÃO
1. Cada conceito é relembrado com a mesma analogia âncora usada no seu episódio:
   o câmbio entre datas (moedas de países diferentes); multiplicar para o futuro e
   dividir para o presente; juros como aluguel do que ainda se deve; a entrada que não
   viaja; o "sem juros" fantasiado; as fatias iguais do SAC; a escadinha dos juros; a
   caixa de tamanho fixo da Price.
2. Prática de recuperação: antes de explicar, PERGUNTE e peça para o aluno pausar.
3. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
4. Uma ideia por cena. Frases curtas. Tom de conversa, falando com "você".

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Toda compra a prazo é um empréstimo disfarçado. Hoje você
  aprende a tirar a fantasia de qualquer anúncio de loja ou contrato de banco."
- O que a prova cobra (seção 01): taxa embutida em "entrada + uma parcela"; valor hoje
  de parcelas futuras e quitação antecipada; composição das parcelas no SAC e na Price;
  crescimento da dívida no cartão e no cheque especial.
- Onde aparece no cotidiano e nas outras séries (a partir das seções 05, 08 e 09):
  financiamento imobiliário (SAC), crediário e crédito pessoal (Price), cartão de
  crédito e cheque especial (Taxas equivalentes), soma de juros do SAC (Progressão
  aritmética, série própria) e a decisão à vista × a prazo (Comparação de propostas).
- A estratégia de prova em 3 hábitos (seção 10): desenhar a linha do tempo; juros só
  sobre o saldo devedor; no SAC montar a primeira linha, na Price usar o fator.
- "Verdadeiro ou falso? Pause e responda": transforme em afirmações os 9 erros da
  seção 11 (taxa sobre o preço total; acreditar no "sem juros" com desconto à vista;
  somar parcelas de datas diferentes; descontar todas pelo mesmo prazo; abater a parcela
  inteira; juros do SAC sobre o valor inicial; amortização constante na Price; SAC e Price
  com os mesmos juros; juros simples no rotativo). Para cada um: pausa → resposta → por
  que a pegadinha engana → a regra certa em uma frase.
- 5 questões INÉDITAS no estilo ENEM, criadas por você, com situações hipotéticas e
  5 alternativas cada:
  1) entrada + uma parcela: R$ 2.400,00 à vista ou entrada de R$ 1.000,00 mais
     R$ 1.540,00 em 30 dias (financiado 1.400, juros 140 → 10% ao mês; distratores:
     140 ÷ 2.400 ≈ 5,8%; 140 ÷ 2.540 ≈ 5,5%; 140 ÷ 1.540 ≈ 9,1%; 0% "porque não diz
     juros");
  2) parcela k do SAC: R$ 24.000,00 em 12 parcelas a 2% ao mês, valor da 5ª parcela
     (amortização 2.000; saldo no início da 5ª = 24.000 − 4 · 2.000 = 16.000; juros 320
     → R$ 2.320,00; distratores: 2.480 com juros sobre o valor inicial; 2.280 subtraindo
     5 amortizações; 320 só os juros; 2.000 só a amortização);
  3) saldo na Price: R$ 8.000,00 em 12 parcelas de R$ 733,44, a 1,5% ao mês, saldo após
     a primeira (juros 120; amortização 613,44; saldo R$ 7.386,56; distratores:
     7.266,56 abatendo a parcela inteira; 7.333,33 com a amortização do SAC; 8.120,00
     somando os juros; 613,44 a amortização);
  4) cheque especial: saldo negativo de R$ 1.000,00 a 8% ao mês, sem pagamentos, por
     2 meses (1.000 · 1,08² = R$ 1.166,40; distratores: 1.160,00 em juros simples;
     1.080,00 um mês só; 1.259,71 contando um mês a mais, 1.000 · 1,08³; 2.166,40
     somando de novo o saldo inicial);
  5) "sem juros" com desconto à vista: R$ 1.500,00 em 5 × sem juros ou R$ 1.350,00 à
     vista; qual afirmação é correta (há R$ 150,00 de juros embutidos e o preço real é
     R$ 1.350,00; distratores: "não há juros, pois o anúncio diz 'sem juros'"; "não há
     juros, pois o total parcelado é igual ao preço de etiqueta"; "o preço real é
     R$ 1.500,00 e o desconto à vista é de 15%"; "há R$ 150,00 de juros, mas eles só são
     cobrados de quem atrasa").
  As alternativas erradas devem ser exatamente os erros clássicos. Leia, peça a pausa,
  desenhe a linha do tempo, resolva, confira a plausibilidade e explique cada
  alternativa.
- Checklist de domínio (seção 13): leia os itens e diga "marque só o que você
  conseguiria explicar em voz alta para outra pessoa, sem consultar nada; o que não
  marcou, reveja o episódio correspondente" (valor no tempo, quitação e rotativo →
  episódio 1; entrada + parcela e "sem juros" → episódio 2; SAC → episódio 3; Price e
  comparação → episódio 4).
- Meta antes de considerar dominado (a do material): resolver 20 questões e acertar pelo
  menos 14 (70%), priorizando as de entrada + parcela e as de tabela do SAC.
- Encerramento e ponte: "o próximo assunto é Comparação de propostas e tomada de
  decisão, que fecha a Matemática Financeira: à vista ou parcelado, plano A ou plano B."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Use um cronômetro visual nas pausas; um selo "PEGADINHA" em amarelo nos erros; uma
  linha do tempo em miniatura em cada questão inédita; os 4 ícones dos episódios (guichê
  de câmbio, etiqueta partida, fatias da dívida, caixa da Price) como índice visual da
  revisão.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Cada conceito foi relembrado antes de ser cobrado?
- As 5 questões inéditas têm uma única alternativa correta e contas corretas?
- Na questão do SAC, o saldo no início da 5ª parcela subtraiu 4 amortizações (k − 1)?
```

---

## Cuidados ao revisar os roteiros

- **Questão 1 (vídeo 2):** o denominador é o **valor financiado, R$ 400,00** (900 − 500), e a taxa é **25% ao mês**. A IA tende a dividir por 900 (11,1%), que é justamente o distrator C, e a confundir com o exemplo da geladeira, que dá 11,1%.
- **Rotativo (vídeo 1):** 1,12³ = 1,404928, então 1.500 · 1,12³ = **R$ 2.107,39**; o material arredonda o fator para 1,405 e escreve ≈ R$ 2.107,50. As duas versões servem, desde que a IA não misture "1,405" com "2.107,39" na mesma cena.
- **SAC (vídeo 3):** na Q3, a PA dos juros vai de **600 até 60** (10 termos), e o total é **R$ 3.300,00**. Se a IA terminar a PA em zero, sai R$ 3.000,00, o distrator A.
- **Price (vídeo 4):** a amortização **cresce** e os juros **caem**. A IA às vezes descreve a Price como "amortização constante", que é o SAC (é o distrator B da Q5).
