# Juros Simples — série de videoaulas

Material de apoio: `01-matematica/13-juros-simples.html` · Incidência: Média

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Fator de multiplicação (1 + i), forma decimal da taxa, "aumento único de 12%" | **Porcentagem** (fator, variações sucessivas) | Revisão relâmpago no vídeo 1. O fator 1 + i·t aparece como "um aumento único", sem reensinar porcentagem. |
| Proporcionalidade entre juros e tempo; regra de três | **Razão, proporção e regra de três** e **Grandezas Proporcionais** | Só uma frase: "é por isso que a regra de três funciona aqui". |
| Taxas proporcionais (24% a.a. = 2% a.m.) | **Taxas equivalentes e inflação** (série própria) | Ensino a proporcional, que é deste assunto, e só aviso: "em juros compostos, dividir por 12 não vale; isso tem série própria". Não mostro 1,02¹² nem taxa equivalente. |
| Montante como reta (y = b + ax) | **Função afim** (série própria) | Uso só a leitura do gráfico (ponto em t = 0 e inclinação). Coeficientes e equação da reta ficam para a série de Função afim, só citada. |
| Montantes formando PA | **Progressão aritmética** (série própria) | Só reconhecer "soma constante = PA" e a razão C·i. Termo geral e soma da PA ficam para a série própria. |
| Contraste com juros compostos (PG, curva) | **Juros compostos e montante** (próxima série) | Só promessa, na ponte do vídeo 3 e na revisão. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. O vocabulário do dinheiro e a fórmula J = C · i · t** | 02, 03 | Q1 | 8–10 min |
| **2. Taxa e tempo na mesma unidade (meses, anos, dias e o boleto atrasado)** | 04, 08 | Q2, Q9, Q5 | 10–12 min |
| **3. O montante é uma reta (gráfico, tabela e PA)** | 05, 07 | Q7, Q6 | 8–10 min |
| **4. Descobrindo capital, taxa ou tempo** | 06 | Q3, Q8, Q4 | 10–12 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Vídeo 1: O vocabulário do dinheiro e a fórmula J = C · i · t

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática Básica — Juros Simples — Episódio 1 de 5:
O vocabulário do dinheiro e a fórmula J = C · i · t
RECORTE: use APENAS as seções 02 e 03 do material de apoio, mais a Questão 1 da seção 12.
O fator de multiplicação (1 + i) e a forma decimal da taxa já foram ensinados na série de
Porcentagem: aqui, revisão rápida. Conversão de unidades de taxa e tempo fica para o
episódio 2: neste episódio, todos os exemplos têm taxa e tempo na mesma unidade.
DURAÇÃO: 8 a 10 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por um empréstimo entre parentes ("te empresto
   R$ 1.500,00 e você me devolve com 2% a mais por mês") e por um aluguel de bicicleta
   cobrado por dia, e só depois apresente a fórmula.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (capital, taxa de juros, a.m., a.a., período, juros, montante, juros
   simples, forma decimal).
3. Analogias âncora, retomadas ao longo da aula:
   - "juros são o aluguel do dinheiro: quem usa o dinheiro de outra pessoa paga por
     cada mês de uso";
   - "em juros simples, o aluguel é sempre o mesmo: todo mês você paga sobre o capital
     inicial, nunca sobre os juros que já acumularam";
   - "a conta de um mês só: calcule os juros de UM período e multiplique pelo número de
     períodos".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: porcentagem na forma
   decimal (2% = 0,02; 1,5% = 0,015) e o fator de aumento 1 + i (série de Porcentagem).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; escreva a taxa sempre
   com a sua unidade (2% a.m.) e o tempo com a sua (6 meses).
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "R$ 2.400,00 aplicados a 1,5% ao mês por 8 meses. A prova coloca
  cinco respostas: R$ 28,80, R$ 36,00, R$ 288,00, R$ 2.688,00 e R$ 2.880,00. Quatro delas
  são a conta certa feita do jeito errado."
- Promessa: "ao final, você vai saber distinguir juros de montante e calcular os dois
  sem errar a vírgula da taxa".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) as cinco palavras (tabela da seção 02): capital, taxa, tempo, juros e montante,
     com o exemplo de R$ 1.500,00 a 2% a.m. por 6 meses;
  b) juros não é montante: "quanto rendeu" pede J; "quanto terá" ou "quanto pagará no
     total" pede M;
  c) as siglas de taxa: a.d., a.m., a.b., a.t., a.s., a.a.;
  d) a definição de juros simples: os juros de cada período são sempre sobre o capital
     inicial;
  e) a fórmula: cada período gera C · i, então t períodos geram J = C · i · t; e
     M = C + J = C · (1 + i · t);
  f) a taxa na forma decimal: 2% → 0,02; 1,5% → 0,015; 18% → 0,18;
  g) o exemplo completo: J = 1.500 · 0,02 · 6 = 180; M = R$ 1.680,00; pelo fator,
     1 + 0,02 · 6 = 1,12 e 1.500 · 1,12 = 1.680 (um aumento único de 12%, como em
     Porcentagem);
  h) a conta de cabeça: 2% de 1.500 é 30; seis meses dão 180.
- Exercício "nós fazemos": peça "pause: R$ 800,00 aplicados a juros simples de 3% ao mês
  durante 5 meses. Quanto rendem e quanto vira o total?" (um mês: 24; cinco meses:
  J = R$ 120,00; M = R$ 920,00; fator 1,15).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Juros são o aluguel do dinheiro, sempre sobre o capital inicial."
  "Juros é o acréscimo; montante é o total."
  "Calcule um período e multiplique pelo tempo."
- Erros clássicos:
  • responder o montante quando pedem os juros (e o contrário);
  • usar 2 em vez de 0,02 na fórmula;
  • trocar 1,5% (0,015) por 15% (0,15) ou por 0,15% (0,0015).
- Questão no estilo ENEM: Questão 1 do material (R$ 2.400,00 a 1,5% a.m. por 8 meses),
  "eu faço": juros de um mês 36, oito meses R$ 288,00 (alternativa C). Explique que B é
  o juro de um único mês, D é o montante, E usa 15% e A usa 0,15%. Depois, "você faz",
  com pausa: "e o montante dessa aplicação?" (R$ 2.688,00).
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "e se a taxa for 18% ao ano e o prazo, 8 meses? Quem
  faz 0,18 vezes 8 descobre que R$ 5.000,00 renderam R$ 7.200,00: mais que o próprio
  capital. Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: uma pilha de notas (o capital) que fica parada, e a cada mês uma
  moedinha de mesmo tamanho (os juros do mês) caindo ao lado; as moedinhas nunca crescem,
  porque são sempre calculadas sobre a pilha original.
- Uma "etiqueta" em cada número da questão: C, i, t, J ou M, com a unidade da taxa e do
  tempo.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Alguém que nunca viu o assunto entenderia a diferença entre juros e montante?
- Todas as contas (180; 1.680; 120; 920; 288; 2.688) estão corretas?
- A taxa aparece sempre na forma decimal dentro da fórmula?
```

---

## Vídeo 2: Taxa e tempo na mesma unidade (meses, anos, dias e o boleto atrasado)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática Básica — Juros Simples — Episódio 2 de 5:
Taxa e tempo na mesma unidade — meses, anos, dias e o boleto atrasado
RECORTE: use APENAS as seções 04 e 08 do material de apoio (inclusive "Prazos em dias: o
ano comercial"), mais as Questões 2, 9 e 5 da seção 12. A escada do tempo (1 ano = 12
meses; o tempo não é decimal) já foi ensinada na série de Unidades: aqui, revisão rápida.
Taxas equivalentes em juros compostos têm série própria (Taxas equivalentes e
inflação): aqui, só o aviso de que dividir por 12 não vale lá.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pela conta de luz paga com atraso (o boleto que
   diz "multa de 2% e juros de 1% ao mês") e pelo contrato de empréstimo que fala em "taxa
   anual" para um prazo de meses.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (taxas proporcionais, ano comercial, ano civil, prazo misto, multa, juros de
   mora, "pro rata die").
3. Analogias âncora, retomadas ao longo da aula:
   - "taxa e tempo falam a mesma língua: taxa mensal conversa com meses, taxa anual
     conversa com anos";
   - "traduza só um dos dois: leve a taxa até o tempo OU o tempo até a taxa, nunca os
     dois";
   - "a multa é o ingresso, os juros de mora são o taxímetro: a multa é cobrada uma vez,
     os juros correm a cada dia".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: J = C · i · t e a conta
   de um mês (episódio 1); 1 ano = 12 meses e "meses não são décimos de ano" (série de
   Unidades: 1 ano e 3 meses são 15 meses, ou 1,25 ano, não 1,3).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; ANTES de qualquer conta,
   escreva na tela "taxa: ___ ao ___ / tempo: ___ ___" e iguale as duas unidades.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "R$ 5.000,00 a 18% ao ano, durante 8 meses. Quem faz 0,18 vezes 8
  descobre que o empréstimo rendeu R$ 7.200,00, mais que o próprio capital. A conta
  certa dá R$ 600,00. A diferença está numa única palavra: 'ao ano'."
- Promessa: "ao final, você vai igualar taxa e tempo em qualquer questão, inclusive com
  prazo em dias, e calcular o valor de um boleto pago com atraso".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) a regra que mais derruba: J = C · i · t só funciona com i e t na mesma unidade;
  b) taxas proporcionais (só em juros simples): 24% a.a. ÷ 12 = 2% a.m.; 2% a.m. = 6%
     a.t. = 12% a.s. = 24% a.a.; aviso: "em juros compostos, dividir por 12 não vale;
     isso tem série própria";
  c) período maior, taxa maior: para passar de mensal a anual, multiplique; de anual a
     mensal, divida;
  d) o ano comercial: mês de 30 dias e ano de 360 dias, salvo aviso de "ano civil" ou
     "365 dias";
  e) o exemplo de 45 dias: R$ 3.000,00 a 24% a.a.: em anos, 3.000 · 0,24 · 45/360 = 90;
     em meses, 2% a.m. e 1,5 mês, 3.000 · 0,02 · 1,5 = 90;
  f) converta o que for mais fácil: 8 meses a 18% a.a. fica melhor como 1,5% a.m. · 8;
  g) o boleto atrasado (seção 08): a multa é fixa, cobrada uma vez; os juros de mora são
     proporcionais aos dias; exemplo da conta de R$ 450,00 com 10 dias de atraso:
     multa 9,00 + juros 1,50 = R$ 460,50.
- Exercício "nós fazemos": peça "pause: R$ 1.200,00 a juros simples de 36% ao ano,
  durante 4 meses. Quanto rendem?" (36% a.a. = 3% a.m.; um mês: 36; quatro meses:
  R$ 144,00).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Taxa e tempo falam a mesma língua."
  "Traduza só um dos dois."
  "A multa é o ingresso; os juros de mora são o taxímetro."
- Erros clássicos:
  • usar taxa anual com tempo em meses (18% · 8);
  • converter a taxa E o tempo: o resultado sai 12 vezes errado, para mais ou para menos
    (exemplo na tela: R$ 1.000,00 a 2% a.m. por 2 anos dá J = 1.000 · 0,02 · 24 = 480;
    quem usa 24% a.a. com 24 meses acha 5.760, 12 vezes mais; quem usa 2% com 2 acha 40,
    12 vezes menos);
  • dividir 2% a.m. por 12 para ter a taxa anual (é 24%: período maior, taxa maior);
  • ler "1 ano e 3 meses" como 1,3 ano;
  • no boleto: esquecer a multa ou os juros, cobrar o mês inteiro por poucos dias, ou
    tratar a taxa mensal como diária.
- Questões no estilo ENEM, nesta ordem:
  • Questão 2 do material (R$ 5.000,00 a 18% a.a. por 8 meses): "eu faço". 1,5% a.m. · 8
    → R$ 600,00 (A). D (7.200) usa 18% com 8; E (12.200) é o montante dessa conta
    errada; B (900) é um ano inteiro de juros; C (5.600) é o montante correto, mas a
    pergunta é pelos juros. Mostre a conferência de ordem de grandeza;
  • Questão 9 (R$ 10.000,00 a 2% a.m., 1 ano e 3 meses): "nós fazemos". 15 meses;
    M = 10.000 · 1,30 = R$ 13.000,00 (D). E lê "1,3 ano" (15,6 meses); C usa só 12 meses;
    B trata 2% como taxa anual em 1,25 ano; A são só os juros;
  • Questão 5 (boleto de R$ 300,00, 15 dias de atraso): "você faz", com pausa.
    Multa 6,00 + juros 300 · 0,01 · 15/30 = 1,50 → R$ 307,50 (D). A cobra só os juros;
    C só a multa; B cobra o mês inteiro de juros e esquece a multa; E trata 1% como taxa
    diária (juros de 45).
  Em todas: leia o enunciado, sublinhe as unidades, iguale, resolva e explique as
  alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "R$ 1.000,00 a 5% ao mês: 1.050, 1.100, 1.150... Se você
  desenhar esses pontos num gráfico, que forma aparece? Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: duas "fichas" na tela, TAXA e TEMPO, cada uma com uma bandeirinha
  da sua unidade (mês, ano, dia); quando as bandeiras são diferentes, a fórmula fica
  travada com um cadeado amarelo; quando uma ficha é traduzida, as bandeiras ficam iguais
  e o cadeado abre.
- O boleto: um ingresso (multa, valor fixo) e um taxímetro girando a cada dia (juros de
  mora), somados no total.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Em cada conta, taxa e tempo estão na mesma unidade ANTES da fórmula?
- O erro de converter os dois foi mostrado nos dois sentidos (12 vezes mais e 12 vezes
  menos), com as contas 480, 5.760 e 40 corretas?
- Ficou claro que taxas proporcionais só valem em juros simples?
```

---

## Vídeo 3: O montante é uma reta (gráfico, tabela e PA)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática Básica — Juros Simples — Episódio 3 de 5:
O montante é uma reta — gráfico, tabela e progressão aritmética
RECORTE: use APENAS as seções 05 e 07 do material de apoio, mais as Questões 7 e 6 da
seção 12. Função afim e progressão aritmética têm séries próprias: aqui, use só o que o
material traz (o ponto em t = 0 é o capital, a inclinação são os juros de um período,
soma constante é PA) e diga "isso tem série própria" para o resto. Juros compostos são a
próxima série: só prometa o contraste.
DURAÇÃO: 8 a 10 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pelo extrato mensal de uma aplicação (1.050,
   1.100, 1.150...) e por uma escada em que todos os degraus têm a mesma altura.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (gráfico, eixo, inclinação, ponto inicial, função afim, progressão
   aritmética, razão da PA).
3. Analogias âncora, retomadas ao longo da aula:
   - "o montante sobe uma escada de degraus iguais: cada degrau são os juros de um
     mês";
   - "a reta começa no capital: o ponto onde ela corta o eixo vertical é o dinheiro do
     dia zero";
   - "para achar a taxa, divida o degrau pelo capital, nunca pelo montante".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: M = C + C · i · t e a
   conta de um mês (episódio 1); como ler um ponto num gráfico (eixo horizontal = tempo,
   eixo vertical = montante).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; em gráficos, sempre
   escreva primeiro "capital = valor em t = 0" e "juros por mês = variação ÷ tempo".
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Um gráfico com uma reta e dois pontos. Só isso. E dele dá para
  tirar o capital, os juros de cada mês e a taxa da aplicação, sem nenhuma fórmula nova."
- Promessa: "ao final, você vai ler capital e taxa num gráfico ou numa tabela e reconhecer
  a sequência dos montantes".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) o montante como função do tempo: M(t) = C + (C · i) · t;
  b) o exemplo do material: R$ 1.000,00 a 5% a.m.; a reta parte de 1.000 e sobe R$ 50,00
     por mês; a distância até a linha tracejada do capital são os juros acumulados;
  c) a mesma forma de uma função afim (y = b + a · x): o capital é onde a reta corta o
     eixo vertical, e C · i é a inclinação (só cite: "função afim tem série própria");
  d) juros iguais em tempos iguais: qualquer intervalo de 2 meses soma R$ 100,00, no
     começo ou no fim;
  e) ler o gráfico: dois pontos dão os juros por período (inclinação) e o capital
     (t = 0); a taxa é a inclinação dividida pelo capital;
  f) o dobro do tempo dá o dobro dos juros: por isso a regra de três funciona aqui, e só
     aqui;
  g) juros simples como PA (seção 07): R$ 1.000,00 a 3% a.m. → 1.030, 1.060, 1.090,
     1.120...; razão = C · i = 30 (só cite: "PA tem série própria");
  h) onde o mercado usa juros simples: mora de contas atrasadas, empréstimos informais,
     cobranças por dia; bancos e cartões usam juros compostos (próxima série).
- Exercício "nós fazemos": peça "pause: num gráfico de juros simples, o montante vale
  R$ 2.500,00 no mês 0 e R$ 2.750,00 no mês 5. Qual é a taxa mensal?" (juros em 5 meses:
  250; por mês: 50; taxa: 50 ÷ 2.500 = 0,02 = 2% a.m.).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "O montante sobe uma escada de degraus iguais."
  "A reta começa no capital."
  "Taxa é o degrau dividido pelo capital."
- Erros clássicos:
  • dividir os juros pelo montante final em vez do capital;
  • esquecer de dividir a variação pelo número de meses (usar a variação total como se
    fosse de um mês);
  • confundir a razão da PA (C · i, em reais) com a taxa (em %).
- Questões no estilo ENEM, nesta ordem:
  • Questão 7 do material (R$ 5.000,00 a 2% a.m., sequência dos montantes): "eu faço".
    5.100, 5.200, 5.300: PA de razão 100 (E). A descreve juros compostos (PG de razão
    1,02, próxima série); B confunde a razão com a taxa; C e D misturam os dois tipos de
    progressão com a razão do outro;
  • Questão 6 (gráfico: montante de R$ 1.600,00 em t = 0 e R$ 2.000,00 em t = 10 meses):
    "você faz", com pausa. Capital 1.600; juros de 400 em 10 meses = 40 por mês;
    i = 40 ÷ 1.600 = 2,5% a.m. (B). D é 400 ÷ 1.600, sem dividir pelos 10 meses; A e C
    repetem as duas contas sobre o montante final de 2.000; E confunde R$ 40,00 por mês
    com 40%.
  Em ambas: leia o enunciado, descreva o gráfico ou a sequência na tela, resolva e
  explique as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "R$ 1.200,00 viraram R$ 1.500,00 em 10 meses. Qual foi a
  taxa anual? E em quanto tempo um capital triplica a 2% ao mês? Próximo episódio:
  descobrindo capital, taxa ou tempo."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: a reta do montante sendo desenhada como uma escada de degraus
  iguais (cada degrau rotulado "R$ 50,00"), com uma linha tracejada no nível do capital e
  a distância entre as duas pintada como "juros acumulados".
- Um triângulo de inclinação desenhado entre dois pontos do gráfico da Questão 6
  (10 meses na horizontal, R$ 400,00 na vertical).
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Ficou claro que a taxa é a inclinação dividida pelo CAPITAL, e não pelo montante?
- As contas (50 por mês; 2% no exercício; razão 100; 2,5% na Questão 6) estão corretas?
- Função afim e PA foram apenas citadas, sem invadir as séries próprias?
```

---

## Vídeo 4: Descobrindo capital, taxa ou tempo

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática Básica — Juros Simples — Episódio 4 de 5:
Descobrindo capital, taxa ou tempo (e em quanto tempo o dinheiro dobra)
RECORTE: use APENAS a seção 06 do material de apoio (inclusive "Em quanto tempo o capital
dobra ou triplica"), mais as Questões 3, 8 e 4 da seção 12. A ideia de "isolar a letra"
de uma fórmula de três termos já apareceu na série de Velocidade, densidade e vazão
(achar a taxa, o numerador ou o denominador): aqui, a mesma ideia com quatro letras.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pela loja que anuncia "R$ 1.000,00 à vista ou
   R$ 400,00 de entrada e R$ 660,00 daqui a dois meses" e pela pergunta "em quanto
   tempo meu dinheiro dobra?".
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (isolar, incógnita, dobrar, triplicar, entrada, valor financiado, taxa
   embutida).
3. Analogias âncora, retomadas ao longo da aula:
   - "a fórmula J = C · i · t é uma mesa de quatro pernas: dadas três, a quarta sai
     dividindo os juros pelas outras duas";
   - "o montante já tem o capital dentro: triplicar é ganhar DUAS vezes o capital em
     juros, não três";
   - "a entrada não é empréstimo: a loja só financia o que falta pagar".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: J = C · i · t e
   M = C + J (episódio 1), taxa e tempo na mesma unidade (episódio 2) e taxa é o degrau
   dividido pelo capital (episódio 3).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; antes de dividir,
   escreva na tela o que é C, i, t e J; e ao final, transforme meses em "anos e meses"
   com divisão inteira (100 meses = 8 · 12 + 4 = 8 anos e 4 meses).
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "A 2% ao mês, em juros simples, em quanto tempo o dinheiro
  triplica? Quem pensa 'três vezes o capital em juros' responde 12 anos e meio. A
  resposta é 8 anos e 4 meses."
- Promessa: "ao final, você vai descobrir qualquer uma das quatro letras, inclusive a
  taxa escondida numa compra parcelada e o tempo para dobrar ou triplicar".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) as três fórmulas isoladas (tabela da seção 06): C = J ÷ (i · t); i = J ÷ (C · t);
     t = J ÷ (C · i);
  b) achar o capital: juros de R$ 360,00 em 8 meses a 1,5% a.m. → 360 ÷ 0,12 = 3.000;
  c) achar a taxa: R$ 1.000,00 rendem R$ 240,00 em 6 meses → 240 ÷ 6.000 = 0,04 = 4% a.m.;
     na taxa, divida pelo capital, nunca pelo montante;
  d) achar o tempo: R$ 2.000,00 a 2,5% a.m. para render R$ 400,00 → 400 ÷ 50 = 8 meses;
  e) dobrar e triplicar: dobrar é J = C; triplicar é J = 2C; o capital se cancela e
     sobra i · t = k − 1; a 4% a.m., dobrar leva 25 meses e triplicar, 50;
  f) a taxa embutida numa compra a prazo: a entrada não é financiada; capital = preço à
     vista − entrada.
- Exercício "nós fazemos": peça "pause: R$ 1.500,00 renderam R$ 180,00 em 4 meses, a juros
  simples. Qual é a taxa mensal? E, numa outra aplicação a 5% ao mês, em quanto tempo um
  capital dobraria?" (i = 180 ÷ 6.000 = 0,03 = 3% a.m.; dobrar a 5%: 0,05 · t = 1 →
  t = 20 meses).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Dadas três letras, a quarta sai dividindo os juros pelas outras duas."
  "Triplicar é ganhar duas vezes o capital em juros."
  "A entrada não é empréstimo."
- Erros clássicos:
  • dividir pelo montante ao achar a taxa (dá uma taxa menor que a real);
  • triplicar o capital com J = 3C (dá um tempo 50% maior);
  • ler 100 ÷ 12 ≈ 8,33 como "8 anos e 3 meses" (0,33 ano são 4 meses);
  • incluir a entrada no valor financiado.
- Questões no estilo ENEM, nesta ordem:
  • Questão 3 do material (R$ 1.200,00 viram R$ 1.500,00 em 10 meses; taxa anual):
    "eu faço". J = 300; i = 300 ÷ 12.000 = 2,5% a.m.; anual: 30% (E). B é a mensal (a
    pergunta é a anual); D é 300 ÷ 1.200, sem dividir pelo tempo; A e C dividem pelo
    montante (2% a.m. e 24% a.a.);
  • Questão 8 (geladeira: R$ 1.000,00 à vista ou R$ 400,00 + R$ 660,00 em 2 meses):
    "nós fazemos". C = 600; J = 60; i = 60 ÷ 1.200 = 5% a.m. (A). D esquece de dividir
    pelos 2 meses (60 ÷ 600 = 10%); B faz 60 ÷ 1.000, usando o preço total como se tudo
    fosse financiado E esquecendo de dividir pelos 2 meses (com a divisão, daria 3%,
    que nem está nas alternativas); C e E calculam sobre a entrada, com e sem a divisão
    pelo tempo (60 ÷ 800 = 7,5% e 60 ÷ 400 = 15%);
  • Questão 4 (triplicar a 2% a.m.): "você faz", com pausa. J = 2C → 0,02 · t = 2 →
    t = 100 meses = 8 anos e 4 meses (C). A (50 meses) é o tempo para dobrar; D (150
    meses) usa J = 3C; B lê 8,33 anos como 8 anos e 3 meses; E trata a taxa mensal como
    anual.
  Em todas: leia o enunciado, etiquete C, i, t e J, resolva e explique as alternativas
  erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "no último episódio deste assunto, juntamos tudo,
  caçamos as pegadinhas e treinamos com questões no formato do ENEM."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: uma mesa de quatro pernas (C, i, t, J); uma perna some e é
  reconstruída pela divisão de J pelas outras duas.
- Triplicar: três pilhas de notas iguais; a primeira é o capital (verde, "já estava lá")
  e só as outras duas são juros.
- Na Questão 8, uma linha do tempo com a entrada no dia 0 (riscada como "não
  financiada") e o pagamento de R$ 660,00 no mês 2.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Em toda taxa calculada, o denominador é o capital (vezes o tempo), e não o montante?
- A conversão 100 meses = 8 anos e 4 meses está correta e explicada?
- A explicação da alternativa B da Questão 8 diz que ela usa o preço total E esquece de
  dividir pelos 2 meses?
```

---

## Vídeo 5: Revisão (Juros simples no ENEM)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula de REVISÃO para o YouTube sobre:

TEMA: Matemática Básica — Juros Simples — Episódio 5 de 5:
Revisão geral, estratégia de prova, pegadinhas e treino para o ENEM
RECORTE: use as seções 01, 09, 10, 11 e 13 do material de apoio.
NÃO reutilize as Questões 1 a 9 da seção 12 (já resolvidas nos episódios anteriores).
Juros compostos, taxas equivalentes, função afim e PA têm séries próprias: aqui, só cite
as pontes.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que assistiu aos episódios 1 a 4, mas ainda é iniciante e pode ter esquecido
partes. Relembre cada conceito em uma frase simples antes de cobrá-lo.

REGRAS DE EXPLICAÇÃO
1. Cada conceito é relembrado com a mesma analogia âncora usada no seu episódio:
   juros como aluguel do dinheiro, sempre sobre o capital inicial; a conta de um mês só;
   taxa e tempo falando a mesma língua; traduzir só um dos dois; a multa como ingresso e
   os juros de mora como taxímetro; a escada de degraus iguais; a reta que começa no
   capital; a mesa de quatro pernas; o montante que já tem o capital dentro; a entrada
   que não é empréstimo.
2. Prática de recuperação: antes de explicar, PERGUNTE e peça para o aluno pausar.
3. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
4. Uma ideia por cena. Frases curtas. Tom de conversa, falando com "você".

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Boleto atrasado, compra parcelada, empréstimo entre parentes. O
  ENEM nunca pergunta 'calcule os juros simples'. Ele conta uma história, e a conversão
  de unidade está escondida no meio."
- O que a prova cobra (seção 01): juros ou montante com conversão de unidade; descobrir
  taxa, capital ou prazo; multa e juros de mora; gráfico ou tabela de montante
  (crescimento linear); taxa embutida numa compra com entrada.
- Onde aparece nas outras áreas (seção 10): função afim (série própria), progressão
  aritmética (série própria), Física (movimento uniforme: s = s₀ + v · t, com o capital no
  papel da posição inicial), porcentagem e regra de três, Ciências Humanas (endividamento,
  crédito e juros de mora).
- A estratégia de prova em 4 hábitos (seção 09): sublinhar as unidades antes de tudo;
  perguntar "juros ou montante?"; usar o valor de um período; conferir a ordem de
  grandeza.
- "Verdadeiro ou falso? Pause e responda": transforme em afirmações os 9 erros da
  seção 11. Para cada um: pausa → resposta → por que a pegadinha engana → a regra certa
  em uma frase. No erro "converter a taxa e também o tempo", diga que o resultado sai
  12 vezes errado, para mais ou para menos, conforme o sentido.
- 5 questões INÉDITAS no estilo ENEM, criadas por você, com situações hipotéticas e
  5 alternativas cada:
  1) juros de uma aplicação com taxa anual e prazo em meses (pedindo os juros, com o
     montante entre as alternativas);
  2) prazo em dias com ano comercial;
  3) conta de água paga com atraso, com multa e juros de mora;
  4) leitura de uma tabela de montantes mês a mês para achar a taxa;
  5) tempo para dobrar ou triplicar um capital.
  As alternativas erradas devem ser exatamente os erros clássicos (taxa anual com tempo
  em meses, montante no lugar de juros, vírgula da taxa, dividir pelo montante, J = 3C,
  1 ano e 3 meses como 1,3 ano, esquecer a multa). Leia, peça a pausa, escreva a unidade
  da taxa e a do tempo, resolva, confira a ordem de grandeza e explique cada
  alternativa.
- Checklist de domínio (seção 13): leia os itens e diga "marque só o que você
  conseguiria explicar em voz alta para outra pessoa, sem consultar nada; o que não
  marcou, reveja o episódio correspondente" (indique qual: vocabulário e fórmula →
  episódio 1; unidades, dias e boleto → 2; gráfico e PA → 3; isolar letras, dobrar e
  compra a prazo → 4).
- Meta antes de considerar dominado: resolver 20 questões de juros simples e acertar
  pelo menos 14 (70%), de preferência com conversão de unidade, boleto atrasado ou
  gráfico.
- Encerramento e ponte: "o próximo assunto é Juros compostos e montante: juros sobre
  juros, a curva no lugar da reta e a PG no lugar da PA."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Use um cronômetro visual nas pausas; um selo "PEGADINHA" em amarelo nos erros; um
  ícone de contexto (boleto, cofrinho, loja, gráfico) em cada questão inédita; os 4
  ícones dos episódios (pilha de notas com moedinhas iguais, fichas de unidade com
  bandeirinhas, escada de degraus iguais, mesa de quatro pernas) como índice visual da
  revisão.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Cada conceito foi relembrado antes de ser cobrado?
- As 5 questões inéditas têm uma única alternativa correta e contas corretas?
- Na questão de dias, foi usado o ano comercial (mês de 30 dias, ano de 360)?
```

---

## Cuidados ao revisar os roteiros

- **Vídeo 2, sentido da conversão:** mensal → anual **multiplica** (2% a.m. = 24% a.a.); anual → mensal **divide**. A IA costuma escrever "2% a.m. ÷ 12" ou "18% a.a. × 12". E o erro de converter os dois não é "sempre 12 vezes menor" (como diz o material): depende do sentido.
- **Vídeo 4, Questão 4:** 100 meses = **8 anos e 4 meses** (8 · 12 = 96; sobram 4). A IA tende a escrever 8,33 anos = "8 anos e 3 meses", que é justamente o distrator B.
- **Vídeo 4, Questão 8:** a taxa é 60 ÷ (600 · 2) = 5%, sobre o valor **financiado** (1.000 − 400), não sobre o preço de R$ 1.000,00 nem sobre a entrada. Confira também a explicação corrigida da alternativa B.
- **Vídeo 3:** a taxa é a inclinação dividida pelo **capital** (valor em t = 0), não pelo montante final; na Questão 6, 40 ÷ 1.600 = 2,5%, e 40 ÷ 2.000 = 2% é distrator.

## Erros encontrados no material

- **Questão 8, explicação da alternativa B:** o material diz que 6% "calcula os juros sobre o preço total de R$ 1.000,00, como se tudo fosse financiado". Com o preço total **e** a divisão pelos 2 meses, daria 60 ÷ 2.000 = 3%. Os 6% vêm de 60 ÷ 1.000, usando o preço total **e** esquecendo de dividir pelo tempo. O prompt do vídeo 4 usa essa explicação.
- **Seção 11, erro "converter a taxa e também o tempo":** o material diz que o resultado sai "12 vezes menor" nos dois casos. Depende do sentido: com R$ 1.000,00 a 2% a.m. por 2 anos (J correto = 480), usar 24% a.a. com 24 meses dá 5.760 (12 vezes **maior**), e usar 2% com 2 dá 40 (12 vezes **menor**). O prompt do vídeo 2 mostra os dois sentidos.
