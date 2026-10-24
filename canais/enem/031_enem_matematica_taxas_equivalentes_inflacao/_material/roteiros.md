# Taxas Equivalentes e Inflação — série de videoaulas

Material de apoio: `01-matematica/16-taxas-equivalentes-inflacao.html` · Incidência: Média

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Taxa proporcional (2% a.m. = 24% a.a.) | **Juros Simples** (série 13, seção 04) | Revisão relâmpago: "certa em juros simples, errada em compostos". |
| M = C(1 + i)ᵗ, potências 1,1² = 1,21 e 1,1³ = 1,331, taxas diferentes em sequência | **Juros Compostos** (série 14) e **Porcentagem** (09) | Revisão rápida; a seção 05 (taxas acumuladas) vira um bloco curto do vídeo 2. |
| **Questão 4 do material** (inflação de 10% e 20% → 32%) | Mesma conta e quase as mesmas alternativas da **Questão 3 de Porcentagem** (reajustes de 10% e 20% → 32%) | **Não uso.** Entra uma questão nova (inflação de 25% e 20% → 50%), com o texto completo no prompt do vídeo 3. |
| Poder de compra (1 ÷ 1,25 = 0,80) | Mesma conta de "voltar ao valor original" da série de Porcentagem | Apresentada como a mesma ideia com outro nome, como o próprio material faz; a Q5 fica (a pergunta é outra). |
| Taxa de cada período para parcelas e rotativo | **Empréstimos** (17) e **Comparação de propostas** (18) | Só prometido na ponte. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Proporcional × equivalente: trocar o período de uma taxa** | 02, 03 | Q1, Q2, Q9 | 10–12 min |
| **2. Taxa nominal × efetiva e taxas acumuladas** | 04, 05 | Q3 + 1 questão nova ("você faz") | 8–10 min |
| **3. Inflação, inflação acumulada e poder de compra** | 06, 07 | Nova (no lugar da Q4), Q5 | 8–10 min |
| **4. Taxa real e a armadilha da subtração** | 07 (deflacionar), 08, 09 | Q6, Q8, Q7 | 10–12 min |
| **5. Revisão** | 01, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Vídeo 1: Proporcional × equivalente: trocar o período de uma taxa

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática Básica — Taxas Equivalentes e Inflação — Episódio 1 de 5:
Proporcional × equivalente: como trocar o período de uma taxa
RECORTE: use APENAS as seções 02 e 03 do material de apoio, mais as Questões 1, 2 e 9
da seção 12. A taxa proporcional foi ensinada na série de Juros Simples e a fórmula
M = C(1 + i)^t na série de Juros Compostos: aqui, revisão rápida. Taxa nominal fica para
o episódio 2; inflação, para os episódios 3 e 4.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por duas propagandas reais de banco, uma dizendo
   "2% ao mês" e outra "26,8% ao ano", e pela fatura de um cartão de crédito que anuncia
   taxa "de um dígito ao mês"; só depois apresente as definições.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (taxa, período da taxa, a.m., a.s., a.a., taxa proporcional, taxa
   equivalente, fator, regime de juros simples e compostos, raiz).
3. Analogias âncora, retomadas ao longo da aula:
   - "taxas equivalentes são o mesmo destino por caminhos diferentes: mesmo capital,
     mesmo prazo, mesmo montante no fim";
   - "fator primeiro, taxa depois: transforme a taxa em fator (1 + i), faça a conta com o
     fator e, no fim, tire o 1";
   - "a proporcional segue a reta (soma 2% por mês); a equivalente segue a curva
     (multiplica por 1,02 por mês). A diferença entre as duas é o juro sobre juro".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: taxa proporcional
   (2% a.m. = 24% a.a., série de Juros Simples); montante composto M = C(1 + i)^t e as
   potências 1,1² = 1,21 e 1,1³ = 1,331 (série de Juros Compostos).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; escreva o fator ao lado
   de cada taxa (2% → 1,02; 44% → 1,44) e o período ao lado de cada taxa (a.m., a.a.).
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Dez por cento ao mês dá quanto ao ano? Se você disse 120%,
  errou por quase 100 pontos: dá cerca de 214%. É assim que o rotativo do cartão vira
  uma taxa anual de três dígitos."
- Promessa: "ao final, você vai converter qualquer taxa composta de mensal para anual e
  de anual para semestral, sem multiplicar nem dividir pelo número de períodos".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) duas formas de comparar taxas (tabela da seção 02): proporcional (juros simples,
     multiplica ou divide) × equivalente (juros compostos, eleva ou tira raiz do fator);
     2% a.m. → 24% a.a. proporcional × 1,02^12 − 1 ≈ 26,8% a.a. equivalente;
  b) definição: equivalentes = mesmo capital, mesmo prazo, mesmo montante; por isso, em
     compostos, 2% a.m. e 24% a.a. NÃO são equivalentes;
  c) a fórmula 1 + i_longo = (1 + i_curto)^n e a tabela de fatores: 1,1² = 1,21 (21% ao
     bimestre, não 20%); 1,1³ = 1,331 (33,1% ao trimestre); 1,2² = 1,44 (44% ao ano);
     1,01^12 ≈ 1,1268 (12,68%); 1,02^12 ≈ 1,268 (26,8%);
  d) o caminho inverso é raiz: 44% a.a. → (1 + i)² = 1,44 → 1 + i = 1,2 → 20% a.s.; a
     proporcional daria 22% a.s., e 1,22² ≈ 1,488, quase 49% no ano;
  e) o efeito cresce com a taxa: 1% a.m. → 12% × 12,68% (perto); 10% a.m. → 1,1^12 ≈
     3,14 → cerca de 214% a.a., não 120%.
- Exercício "nós fazemos": peça "pause: 3% ao mês, em juros compostos, equivale a
  quanto ao bimestre?" (1,03² = 1,0609 → 6,09% ao bimestre, não 6%).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Taxa equivalente: eleve o fator, não multiplique a taxa."
  "Do período longo para o curto: raiz do fator, nunca divisão."
  "No fim, tire o 1 do fator."
- Erros clássicos:
  • 2% ao mês = 24% ao ano em juros compostos (é 1,02^12 − 1 ≈ 26,8%);
  • dividir a taxa anual pelo número de períodos para achar a equivalente (44% ao ano
    equivalem a 20% ao semestre, não 22%);
  • esquecer de tirar 1 do fator (o distrator "126,8%" é exatamente isso).
- Questões no estilo ENEM, nesta ordem:
  • Questão 1 do material (1% ao mês, 1,01^12 ≈ 1,1268): "eu faço", explicando que
    12% é a proporcional, 112,68% é o fator sem tirar 1, 1,27% é vírgula deslocada e
    12,12% vem de multiplicar 1,01 por 12;
  • Questão 2 (33,1% no trimestre → taxa mensal): "nós fazemos", reconhecendo
    1,1 · 1,1 · 1,1 = 1,331;
  • Questão 9 (44% ao ano: qual taxa é equivalente?): "você faz", com pausa; mostre que
    as quatro erradas são todas proporcionais (44 ÷ 12, ÷ 4, ÷ 3, ÷ 2).
  Em todas: leia o enunciado, escreva o fator, resolva, confira a plausibilidade (a
  equivalente anual fica um pouco ACIMA da proporcional) e explique as alternativas
  erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "um contrato diz '24% ao ano, capitalizados
  mensalmente'. Você paga 24% ao ano? Não. Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: o gráfico da seção 02, uma reta tracejada subindo 2% por mês até
  24% e uma curva multiplicando por 1,02 até 26,8%, com a faixa entre as duas pintada e
  rotulada "juro sobre juro".
- Uma "máquina de fatores": a taxa entra, vira fator, o fator é elevado à potência, e na
  saída uma tesoura corta o "1," para virar taxa de novo.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Ficou claro que a proporcional é a correta APENAS em juros simples?
- Os fatores estão certos (1,1² = 1,21; 1,1³ = 1,331; 1,2² = 1,44; 1,1^12 ≈ 3,14)?
- O caminho inverso foi feito com raiz (44% a.a. → 20% a.s.), e não com divisão?
```

---

## Vídeo 2: Taxa nominal × efetiva e taxas acumuladas

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática Básica — Taxas Equivalentes e Inflação — Episódio 2 de 5:
Taxa nominal × taxa efetiva e taxas acumuladas
RECORTE: use APENAS as seções 04 e 05 do material de apoio, mais a Questão 3 da seção 12
e a QUESTÃO NOVA escrita abaixo. Multiplicar fatores de períodos com taxas diferentes já
apareceu nas séries de Porcentagem e de Juros Compostos: a seção 05 é revisão rápida; o
conteúdo novo é a taxa nominal e a taxa média como taxa equivalente.
DURAÇÃO: 8 a 10 minutos

QUESTÃO NOVA (para o "você faz"):
"Duas financeiras anunciam empréstimos com taxa de 36% ao ano. A financeira X capitaliza
os juros semestralmente; a financeira Y, mensalmente. Considere 1,03^12 ≈ 1,426. Qual
delas tem o maior custo efetivo anual, e qual é esse custo?
A) As duas, pois ambas cobram 36% ao ano.
B) A financeira X, com cerca de 39,2% ao ano.
C) A financeira Y, com 36% ao ano.
D) A financeira Y, com cerca de 42,6% ao ano.
E) A financeira Y, com cerca de 142,6% ao ano."
Gabarito: D. Resolução: X → 36% ÷ 2 = 18% ao semestre → 1,18² = 1,3924 → 39,24% ao ano;
Y → 36% ÷ 12 = 3% ao mês → 1,03^12 ≈ 1,426 → cerca de 42,6% ao ano. Quanto mais frequente
a capitalização, maior a taxa efetiva. A toma a nominal pela efetiva; B calcula certo a
efetiva de X, mas ela é a menor; C acerta a financeira e esquece de capitalizar; E é o
fator sem tirar 1.

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pela letra miúda de um contrato ("taxa de 24% a.a.,
   capitalizada mensalmente") e pelo extrato de um fundo de investimento que subiu dois
   meses e caiu no terceiro.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (capitalização, período de capitalização, taxa nominal, taxa efetiva, taxa
   acumulada, taxa média por período).
3. Analogias âncora, retomadas ao longo da aula:
   - "a taxa nominal é o preço da vitrine; a efetiva é o que passa no caixa";
   - "a nominal só serve para uma coisa: dividir pelo número de capitalizações. Depois,
     capitalize";
   - "fator primeiro, taxa depois" (a mesma do episódio 1), agora com fatores
     diferentes em cada período, inclusive menores que 1.
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: taxa equivalente pelo
   fator elevado (episódio 1) e multiplicar fatores de variações sucessivas (série de
   Porcentagem).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; escreva o fator ao lado
   de cada taxa, com sinal (−10% → 0,9).
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Dois contratos anunciam exatamente '24% ao ano'. Um custa
  25,44%; o outro, 26,8%. Mesma propaganda, preços diferentes."
- Promessa: "ao final, você vai transformar qualquer taxa nominal em efetiva e acumular
  taxas de meses diferentes sem somar porcentagens".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) taxa nominal: anunciada num período, capitalizada em outro; a única divisão
     permitida é pela quantidade de capitalizações (24% ÷ 12 = 2% ao mês, que é efetiva);
  b) capitalize pelo prazo: 1,02^12 ≈ 1,268 → efetiva de cerca de 26,8% ao ano;
  c) a tabela da seção 04: 12% a.a. com capitalização mensal → ≈ 12,68%; 24% a.a.
     semestral → 1,12² − 1 = 25,44%; 24% a.a. mensal → ≈ 26,8%; quanto mais frequente a
     capitalização, maior a efetiva; para comparar, converta tudo para efetivas no mesmo
     período;
  d) taxas acumuladas: +10%, +20% e −10% → 1,1 · 1,2 · 0,9 = 1,188 → 18,8% (a soma daria
     20%: a perda incide sobre um valor já maior);
  e) taxa média por período é a equivalente (média geométrica dos fatores): 21% em dois
     meses são 10% ao mês, não 10,5%.
- Exercício "nós fazemos": peça "pause: um fundo rendeu +20%, depois −10%, depois +5%.
  Qual foi o rendimento acumulado?" (1,2 · 0,9 · 1,05 = 1,134 → 13,4%; a soma daria 15%).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Taxa nominal: divida pelas capitalizações e capitalize."
  "Taxas em sequência: multiplique os fatores, inclusive os menores que 1."
  "Taxa média por período é a equivalente, não a média das porcentagens."
- Erros clássicos:
  • tomar a taxa nominal pela efetiva ("12% a.a. capitalizados mensalmente" custam
    cerca de 12,68% ao ano);
  • somar taxas de períodos sucessivos (10% e 20% acumulam 32%, não 30%);
  • esquecer de tirar 1 do fator.
- Questões no estilo ENEM, nesta ordem:
  • Questão 3 do material (18% ao ano com capitalização semestral): "eu faço"; 9% ao
    semestre, 1,09² = 1,1881 → 18,81%; mostre que 9% é só a etapa intermediária e que
    19,56% seria a capitalização mensal, que não é a do contrato;
  • QUESTÃO NOVA (financeiras X e Y, 36% ao ano): "você faz", com pausa, resolvida e
    explicada como no texto acima.
  Em todas: leia o enunciado, identifique a palavra "capitalizado", resolva, confira a
  plausibilidade (a efetiva fica um pouco acima da nominal) e explique as alternativas
  erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "se os preços sobem 25% e o seu salário fica parado,
  você perde 25% do poder de compra? Não. Próximo episódio: inflação."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: uma etiqueta de vitrine "24% a.a." sendo cortada em 12 fatias de
  2%, e cada fatia multiplicando o saldo em sequência até o caixa mostrar "26,8%".
- Um extrato com três meses (+10%, +20%, −10%) em que os fatores 1,1, 1,2 e 0,9 se
  empilham numa multiplicação; ao lado, a soma "20%" riscada em vermelho.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Ficou claro que a divisão da nominal só serve para achar a taxa do período de
  capitalização, e que depois é preciso capitalizar?
- As contas estão certas (1,12² = 1,2544; 1,09² = 1,1881; 1,18² = 1,3924; 1,2 · 0,9 · 1,05
  = 1,134)?
- A QUESTÃO NOVA tem gabarito D?
```

---

## Vídeo 3: Inflação, inflação acumulada e poder de compra

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática Básica — Taxas Equivalentes e Inflação — Episódio 3 de 5:
Inflação, inflação acumulada e poder de compra
RECORTE: use APENAS as seções 06 e 07 do material de apoio (sem a parte "Deflacionar",
que fica para o episódio 4), mais a Questão 5 da seção 12 e a QUESTÃO NOVA escrita
abaixo. NÃO use a Questão 4 do material: ela repete uma questão da série de Porcentagem.
DURAÇÃO: 8 a 10 minutos

QUESTÃO NOVA (use no lugar da Questão 4 do material):
"Em um país, a inflação foi de 25% em um ano e de 20% no ano seguinte. A inflação
acumulada nesses dois anos foi de
A) 5%.  B) 22,5%.  C) 45%.  D) 50%.  E) 150%."
Gabarito: D. Resolução: 1,25 · 1,20 = 1,50 → 50%. Com um produto de R$ 100,00: vai a
R$ 125,00 e depois a R$ 150,00, porque os 20% do segundo ano incidem sobre um preço que
já subiu. A é a diferença entre as taxas; B é a média das taxas; C soma as taxas; E é o
fator 1,50 escrito como porcentagem.

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma cesta de compras de supermercado que
   custava R$ 500,00 e passou a custar R$ 540,00, e por uma nota de R$ 100,00 que
   compra cada vez menos itens.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (inflação, índice de preços, cesta fixa, IPCA, IBGE, inflação acumulada,
   deflação, poder de compra).
3. Analogias âncora, retomadas ao longo da aula:
   - "a inflação é uma escada rolante de preços: se ela fica mais lenta, os preços
     continuam subindo, só que mais devagar. Preço descendo é deflação";
   - "poder de compra é uma divisão: o mesmo dinheiro dividido pelo fator dos preços";
   - "fator primeiro, taxa depois" (a mesma dos episódios anteriores): inflações se
     acumulam multiplicando fatores.
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: variação percentual
   (novo ÷ antigo − 1) e "voltar ao valor original dividindo pelo fator" (série de
   Porcentagem: subir 25% e descer 20% volta ao ponto de partida).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; escreva o fator ao lado
   de cada taxa de inflação e diga em voz alta se a conta pede o que se PERDEU ou o que
   RESTOU.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Se os preços dobram, inflação de 100%, o seu dinheiro vira pó?
  Não: ele passa a comprar metade. A perda é de 50%, não de 100%."
- Promessa: "ao final, você vai calcular inflação acumulada e a perda de poder de compra
  sem confundir as duas".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) inflação e índice de preços: a cesta de R$ 500,00 que passa a R$ 540,00 →
     540 ÷ 500 = 1,08 → inflação de 8%; no Brasil, o índice oficial é o IPCA, do IBGE;
  b) inflação acumulada multiplica fatores: 5% e 4% → 1,05 · 1,04 = 1,092 → 9,2%, não 9%;
  c) inflação menor não é preço menor: de 8% para 4%, os preços ainda sobem; preço
     caindo é deflação (taxa negativa); um gráfico de taxas descendo não é um gráfico de
     preços descendo;
  d) poder de compra = 1 ÷ (1 + π): inflação de 25% → 0,80 (perda de 20%); de 100% →
     0,50 (perda de 50%); de 10% → ≈ 0,909 (perda de ≈ 9,1%);
  e) por que a perda é menor que a inflação: é a mesma conta de "voltar ao valor
     original" (subir 25% e descer 20% volta ao início).
- Exercício "nós fazemos": peça "pause: num período de inflação de 60%, um salário ficou
  congelado. Quanto ele perdeu de poder de compra?" (1 ÷ 1,6 = 0,625 → perda de 37,5%).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Inflação se acumula multiplicando fatores."
  "Poder de compra: divida pelo fator da inflação."
  "Inflação caindo não é preço caindo."
- Erros clássicos:
  • somar inflações de períodos sucessivos;
  • igualar a perda de poder de compra à inflação (inflação de 25% tira 20%);
  • achar que inflação caindo significa preços caindo.
- Questões no estilo ENEM, nesta ordem:
  • QUESTÃO NOVA (inflação de 25% e de 20%): "eu faço", com o produto de R$ 100,00 e os
    distratores explicados como no texto acima;
  • Questão 5 do material (preços subiram 25%, salário parado): "você faz", com pausa;
    mostre a conferência com 100 unidades de R$ 1,00 que viram 80 unidades, e que a E
    (80%) é o que restou, não o que se perdeu.
  Em todas: leia o enunciado, escreva os fatores, resolva, confira a plausibilidade (a
  perda de poder de compra fica ABAIXO da inflação) e explique as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "seu dinheiro rendeu 26% num ano de inflação de 20%.
  Você ficou 6% mais rico? Próximo episódio: taxa real."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: um carrinho de supermercado com 100 itens de R$ 1,00; os preços
  sobem para R$ 1,25 e 20 itens saem do carrinho, sobrando 80 (selo "perda de 20%, não
  de 25%").
- Uma escada rolante de preços que desacelera (de 8% para 4%) mas continua subindo; ao
  lado, a palavra "DEFLAÇÃO" aparece só quando a escada inverte o sentido.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- A Questão 4 do material ficou de fora e a QUESTÃO NOVA dá 50%?
- A perda de poder de compra foi calculada como 1 − 1/(1 + π) em todos os exemplos?
- Ficou clara a diferença entre o que se perdeu (20%) e o que restou (80%)?
```

---

## Vídeo 4: Taxa real e a armadilha da subtração

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática Básica — Taxas Equivalentes e Inflação — Episódio 4 de 5:
Taxa real de juros e a armadilha da subtração
RECORTE: use APENAS a parte "Deflacionar" da seção 07 e as seções 08 e 09 do material de
apoio, mais as Questões 6, 8 e 7 da seção 12. Inflação e poder de compra (episódio 3)
são pré-requisitos.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma manchete de jornal ("juros de 12% e
   inflação de 5%: ganho real de 7%"), por um extrato da poupança que "rendeu" e por um
   aviso de reajuste salarial da categoria.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (taxa nominal ou aparente, taxa real, deflacionar, valor em dinheiro da data
   antiga, aumento real, aproximação).
3. Analogias âncora, retomadas ao longo da aula:
   - "a escada rolante de preços (episódio 3): o quanto você subiu DE VERDADE é o que
     você andou acima da escada. Andar mais devagar que a escada é descer";
   - "taxa real: divida os fatores, nunca subtraia as taxas";
   - "deflacionar é traduzir um valor de hoje para o dinheiro de antigamente, dividindo
     pelo fator da inflação".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: fator da inflação e
   poder de compra = 1 ÷ (1 + π) (episódio 3).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; escreva sempre os três
   fatores (nominal, inflação, real) lado a lado na tela.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "A poupança rendeu 8% e a inflação foi de 10%. Seu saldo cresceu,
  e mesmo assim você ficou mais pobre. Hoje você descobre quanto."
- Promessa: "ao final, você vai calcular a taxa real de qualquer rendimento ou reajuste e
  saber quando a subtração engana".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) deflacionar: salário de R$ 2.000,00 → R$ 2.400,00 com inflação de 20% →
     2.400 ÷ 1,20 = 2.000 → mesmo poder de compra; o aumento nominal só repôs a inflação;
  b) nominal × real e a relação (1 + i_nominal) = (1 + i_real) · (1 + π), ou
     1 + i_real = (1 + i_nominal) ÷ (1 + π);
  c) a figura da seção 08: R$ 100,00 viram R$ 105,00 só para manter o poder de compra, e
     o ganho real de 10% incide sobre os R$ 105,00 → R$ 115,50 (por isso os fatores se
     multiplicam e as taxas não se somam);
  d) exemplo 1: rendeu 15,5% com inflação de 5% → 1,155 ÷ 1,05 = 1,10 → ganho real de
     10%; exemplo 2: rendeu 8% com inflação de 10% → 1,08 ÷ 1,10 ≈ 0,982 → taxa real de
     ≈ −1,8% (perda);
  e) a aproximação i_real ≈ i_nominal − π: com 1% e 0,5% ao mês, o erro é desprezível
     (0,4975% contra 0,5%); com 26% e 20%, dá 6% contra os 5% exatos, um ponto inteiro;
     na prova, use a conta exata e a subtração só para conferir a ordem de grandeza.
- Exercício "nós fazemos": peça "pause: uma aplicação rendeu 32% num ano de inflação de
  10%. Qual foi a taxa real?" (1,32 ÷ 1,10 = 1,20 → 20%; a subtração daria 22%).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Taxa real: divida o fator nominal pelo fator da inflação."
  "Subtrair as taxas é só uma estimativa; na prova, divida."
  "Rendimento abaixo da inflação é perda, mesmo com saldo maior."
- Erros clássicos:
  • taxa real = nominal − inflação (26% com inflação de 20% dá 5% real, não 6%);
  • achar que rendimento positivo é sempre ganho (render 8% com inflação de 10% é perder
    poder de compra).
- Questões no estilo ENEM, nesta ordem:
  • Questão 6 do material (rendeu 26%, inflação de 20%): "eu faço"; 1,26 ÷ 1,20 = 1,05;
    mostre que C é a subtração, A a divisão invertida, D soma e E multiplica os fatores;
  • Questão 8 (eletrodoméstico de R$ 200,00 para R$ 276,00, inflação de 20%): "nós
    fazemos", pelos dois caminhos (deflacionar 276 ÷ 1,20 = 230 → 230 ÷ 200 = 1,15; ou
    1,38 ÷ 1,20 = 1,15);
  • Questão 7 (reajuste de 6% com inflação de 10%, 1,06 ÷ 1,10 ≈ 0,964): "você faz",
    com pausa; perda de cerca de 3,6%; a D (perda de 4%) é a subtração, que exagera a
    perda.
  Em todas: leia o enunciado, escreva os três fatores, resolva, confira a plausibilidade
  (a taxa real fica um pouco ABAIXO da diferença nominal − inflação) e explique as
  alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "no último episódio deste assunto, juntamos tudo,
  caçamos as pegadinhas e treinamos com questões inéditas."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: a barra de R$ 100,00 crescendo em duas etapas, primeiro até
  R$ 105,00 (pintada de cinza, "só acompanhou a inflação") e depois até R$ 115,50
  (pintada de verde, "ganho real de 10% sobre 105").
- Uma pessoa andando numa escada rolante: quando ela anda mais rápido que a escada,
  sobe de verdade; quando anda mais devagar, a placa "taxa real negativa" acende.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Em todas as contas, a taxa real saiu da DIVISÃO dos fatores?
- As contas estão certas (1,155 ÷ 1,05 = 1,10; 1,26 ÷ 1,20 = 1,05; 276 ÷ 1,20 = 230;
  1,32 ÷ 1,10 = 1,20)?
- A Questão 7 terminou em PERDA de cerca de 3,6%, e não em ganho nem em perda de 4%?
```

---

## Vídeo 5: Revisão (Taxas equivalentes e inflação no ENEM)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula de REVISÃO para o YouTube sobre:

TEMA: Matemática Básica — Taxas Equivalentes e Inflação — Episódio 5 de 5:
Revisão geral, estratégia de prova, pegadinhas e treino para o ENEM
RECORTE: use as seções 01, 10, 11 e 13 do material de apoio.
NÃO reutilize as Questões 1 a 9 da seção 12 nem as questões novas dos episódios 2
(financeiras X e Y) e 3 (inflação de 25% e 20%), já resolvidas nos episódios anteriores.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que assistiu aos episódios 1 a 4, mas ainda é iniciante e pode ter esquecido
partes. Relembre cada conceito em uma frase simples antes de cobrá-lo.

REGRAS DE EXPLICAÇÃO
1. Cada conceito é relembrado com a mesma analogia âncora usada no seu episódio:
   o mesmo destino por caminhos diferentes; fator primeiro, taxa depois (tire o 1 no
   fim); a reta da proporcional × a curva da equivalente; a nominal como preço de vitrine
   e a efetiva como preço do caixa; a escada rolante de preços; poder de compra como
   divisão; deflacionar como tradução para o dinheiro de antigamente.
2. Prática de recuperação: antes de explicar, PERGUNTE e peça para o aluno pausar.
3. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
4. Uma ideia por cena. Frases curtas. Tom de conversa, falando com "você".

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "A prova quase nunca escreve a palavra 'equivalente'. Ela
  pergunta qual aplicação rende mais, se o salário ganhou da inflação, quanto custou de
  verdade um empréstimo. Por trás de tudo, uma ideia só: fatores."
- O que a prova cobra (seção 01): trocar o período de uma taxa composta sem multiplicar
  nem dividir pelo número de períodos; separar inflação de ganho real, combinando as
  taxas por multiplicação de fatores; usar as potências dadas no enunciado.
- Onde aparece nas outras áreas e no cotidiano (a partir das seções 03, 06 e 07): o
  rotativo do cartão (taxa mensal de um dígito, anual de três); o IPCA do IBGE e os
  gráficos de inflação em Ciências Humanas (taxa caindo ≠ preço caindo); reajuste de
  salário e poder de compra; e a ponte para Empréstimos e Comparação de propostas.
- A estratégia de prova em 3 hábitos (seção 10): converter tudo para fatores antes de
  pensar; identificar o regime e o tipo de taxa ("capitalizado" anuncia nominal); usar
  as aproximações dadas e conferir a plausibilidade.
- "Verdadeiro ou falso? Pause e responda": transforme em afirmações os 9 erros da
  seção 11 (2% a.m. = 24% a.a. em compostos; dividir a taxa anual por 12; nominal tomada
  pela efetiva; esquecer de tirar 1; somar inflações; perda de poder de compra igual à
  inflação; taxa real = nominal − inflação; rendimento positivo é sempre ganho; inflação
  caindo = preços caindo). Para cada um: pausa → resposta → por que a pegadinha engana →
  a regra certa em uma frase.
- 5 questões INÉDITAS no estilo ENEM, criadas por você, com situações hipotéticas e
  5 alternativas cada:
  1) taxa equivalente: 5% ao mês em compostos para trimestral, dado 1,05³ ≈ 1,158
     (resposta ≈ 15,8%; distratores: 15% proporcional, 115,8% fator sem tirar 1, 1,58%
     vírgula deslocada, 5% repetindo a mensal);
  2) nominal → efetiva: 30% ao ano capitalizados semestralmente (15% ao semestre,
     1,15² = 1,3225 → 32,25%; distratores: 30% nominal, 15% taxa do semestre, 132,25%
     fator, 60% somando duas vezes 30%);
  3) poder de compra: inflação de 50% com renda parada (1 ÷ 1,5 ≈ 0,667 → perda de
     ≈ 33,3%; distratores: 50% igual à inflação, 66,7% o que restou, 25% metade da
     inflação, 150% o fator);
  4) reajuste × inflação: reajuste de 8% num ano de inflação de 20% (1,08 ÷ 1,20 = 0,90
     → perda real de 10%; distratores: perda de 12% pela subtração, ganho de 8%, perda
     de 28% somando, ganho de 10% com sinal trocado);
  5) gráfico de inflação em queda: taxas anuais de 6%, 4% e 2% em três anos seguidos,
     dado 1,06 · 1,04 · 1,02 ≈ 1,124 (os preços SUBIRAM cerca de 12,4% no acumulado;
     distratores: "os preços caíram", "os preços voltaram ao nível inicial", 12% somando
     as taxas, "subiram 2%" usando só o último ano).
  As alternativas erradas devem ser exatamente os erros clássicos. Leia, peça a pausa,
  escreva os fatores, resolva, confira a plausibilidade e explique cada alternativa.
- Checklist de domínio (seção 13): leia os itens e diga "marque só o que você
  conseguiria explicar em voz alta para outra pessoa, sem consultar nada; o que não
  marcou, reveja o episódio correspondente" (proporcional × equivalente e potências →
  episódio 1; nominal × efetiva e acumuladas → episódio 2; inflação e poder de compra →
  episódio 3; deflacionar, taxa real e aproximação → episódio 4).
- Meta antes de considerar dominado (a do material): resolver 20 questões e acertar pelo
  menos 14 (70%), priorizando as de taxa real e reajuste salarial e as de comparação
  entre taxas de períodos diferentes.
- Encerramento e ponte: "o próximo assunto é Empréstimos, financiamentos e
  parcelamentos: os juros escondidos no 'sem juros', a tabela do SAC e a da Price."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Use um cronômetro visual nas pausas; um selo "PEGADINHA" em amarelo nos erros; um
  ícone de fator "(1 + i)" em cada questão inédita; os 4 ícones dos episódios (reta ×
  curva, etiqueta de vitrine, carrinho de supermercado, escada rolante) como índice
  visual da revisão.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Cada conceito foi relembrado antes de ser cobrado?
- As 5 questões inéditas têm uma única alternativa correta e contas corretas?
- Na questão 5, ficou claro que inflação positiva em queda ainda é preço subindo?
```

---

## Cuidados ao revisar os roteiros

- **Perda de poder de compra × inflação (vídeo 3):** inflação de 25% tira **20%** (1 ÷ 1,25 = 0,80); inflação de 100% tira **50%**. A IA costuma dizer "perde 25%" e contradiz o próprio exemplo.
- **Taxa real (vídeo 4):** 1,26 ÷ 1,20 = **1,05 → 5%**, não 6%; 1,06 ÷ 1,10 ≈ **0,964 → perda de ≈ 3,6%**, não 4%. Se a IA usar a subtração "para simplificar", ela cai exatamente no distrator.
- **Taxa nominal (vídeo 2):** dividir 24% por 12 só dá a taxa **do período de capitalização** (2% ao mês); a efetiva anual é 1,02¹² − 1 ≈ **26,8%**. A IA às vezes chama os 2% de "taxa mensal equivalente a 24% ao ano", o que inverte a lição do vídeo 1.
- **Gancho do vídeo 1:** 1,1¹² ≈ 3,14 significa cerca de **214% ao ano** (tirando o 1), não 314%.
