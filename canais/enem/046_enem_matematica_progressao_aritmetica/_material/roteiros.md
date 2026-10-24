# Progressão Aritmética (PA) — série de videoaulas

Material de apoio: `01-matematica/31-progressao-aritmetica.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Montantes de juros simples formam PA de razão C · i (R$ 1.000,00 a 3%: 1.030, 1.060, 1.090…) | **Juros Simples**, seção 07 e **Questão 7** (identificar o tipo de sequência) | "Você já viu isso disfarçado": no Vídeo 4, revisão relâmpago com o exemplo de lá. A Questão 7 daqui é outra (achar o mês em que o montante chega a R$ 3.080,00), então uso, com foco no "termo zero". |
| PA = função afim nos naturais, razão = coeficiente angular | **Função Afim**, seções 03 e 10 | Revisão relâmpago no Vídeo 1; o gráfico de pontos alinhados é o elo. |
| Juros do SAC caem em PA; total de juros = soma de PA ((400 + 80) · 5 ÷ 2 = 1.200) | **Empréstimos, financiamentos e parcelamentos**, seção 06 | Citado no Vídeo 3 (soma) e no Vídeo 4 (PA disfarçada), com o exemplo de lá. Nenhuma questão de SAC é repetida. |
| PA × PG (diferença constante × quociente constante) | **Progressão Geométrica** (próxima série) e **Função Exponencial** | Só o aviso "(2, 4, 8, 16) não é PA; é assunto do próximo material". |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. O que é PA, a razão e o "n − 1"** | 02, 03, 04 | Q2, Q1 | 10–12 min |
| **2. Contar termos e saltos: meios, postes, múltiplos e três termos** | 05 (média dos vizinhos, notação simétrica), 07 | Q4, Q5, Q6 | 10–12 min |
| **3. A soma de Gauss** | 06, 05 (termos equidistantes) | Q3, Q8, Q9 | 10–12 min |
| **4. A PA disfarçada: juros simples, calendário, SAC** | 08 | Q7 | 6–8 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Vídeo 1: O que é PA, a razão e o "n − 1"

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Sequências — Progressão Aritmética — Episódio 1 de 5:
O que é PA, a razão e o "n − 1"
RECORTE: use APENAS as seções 02, 03 e 04 do material de apoio, mais as Questões 2 e 1
da seção 12. A função afim (coeficiente angular como taxa de variação) já foi ensinada
na série de Função Afim: aqui, revisão rápida. A soma fica para o episódio 3; a PG, para
a próxima série.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma escada de verdade (degraus iguais), por
   um cofrinho que recebe R$ 15,00 a mais a cada mês e por quadradinhos de palitos de
   fósforo. Só depois escreva a_n.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (sequência, termo, posição, índice, a₁, a_n, razão, PA crescente,
   decrescente e constante, termo geral).
3. Analogias âncora, retomadas ao longo da aula:
   - "a PA é uma escada de degraus iguais: a razão é a altura do degrau";
   - "do 1º ao 12º degrau você sobe 11 vezes: n − 1 saltos";
   - "teste a fórmula com n = 1: ela tem de devolver o primeiro termo".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: resolver 6r = 24
   (série de Equações do 1º grau) e "quanto muda a cada unidade" como o coeficiente a
   da reta (série de Função Afim).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; antes de qualquer
   fórmula, escreva na tela a₁, a₂ e a₃ e conte os saltos com o dedo.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Ana deposita R$ 50,00 em janeiro e, a cada mês, R$ 15,00 a
  mais. Quanto em dezembro? Quem faz 50 + 12 · 15 responde R$ 230,00 e erra. A resposta
  é R$ 215,00, e o motivo cabe numa escada."
- Promessa: "ao final, você vai achar o termo 50, 100 ou 1 000 de qualquer PA sem
  listar os anteriores".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) o que é PA: cada termo é o anterior mais a razão r; a tabela da seção 02
     (r = 3; r = −6; r = 0; r = 0,5; e (2, 4, 8, 16), que não é PA);
  b) razão é "segundo menos primeiro": em (40, 34, 28), r = −6, não 6;
  c) o termo geral: a_n = a₁ + (n − 1) · r; do 1º ao 12º há 11 saltos; o 12º termo de
     (50, 65, 80, …) é 50 + 11 · 15 = 215;
  d) a versão a partir de qualquer termo: a_n = a_k + (n − k) · r; achar a razão por
     dois termos: a₄ = 17 e a₁₀ = 41 → 6r = 24, r = 4, a₁ = 5;
  e) padrão de figuras: 4 palitos e +3 por quadrado → a_n = 3n + 1; a figura 50 usa 151
     palitos;
  f) PA é função afim nos naturais: a_n = r · n + (a₁ − r); (5, 8, 11, 14, 17, 20)
     como pontos soltos sobre a reta y = 3n + 2; a razão é a inclinação.
- Exercício "nós fazemos": peça "pause: qual é o 30º termo da PA (7, 11, 15, …)?"
  (r = 4; a₃₀ = 7 + 29 · 4 = 123; teste com n = 1: 7 + 0 · 4 = 7).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Razão é segundo menos primeiro."
  "Do 1º ao n-ésimo termo há n − 1 saltos."
  "PA é uma reta vista só nos números inteiros."
- Erros clássicos:
  • a₁₂ = a₁ + 12r (um salto a mais);
  • razão de (40, 34, 28) = 6 (o sinal some);
  • figura n com 4n palitos (esquecer que os quadrados vizinhos dividem um lado).
- Questões no estilo ENEM, nesta ordem:
  • Questão 2 do material (depósito de dezembro de Ana): "eu faço", mostrando que
    A (165) é só o acréscimo, B (180) usa 12 · 15 sem os 50, D (230) usa 12 saltos e
    E (1 590) é a soma dos 12 depósitos, que não foi pedida;
  • Questão 1 (palitos, figura 50): "você faz", com pausa. Nas erradas: A (101) é de
    quem acha que cada quadrado novo acrescenta 2 palitos e usa 2 · 50 + 1; B (148) usa
    49 quadrados, 3 · 49 + 1; C (150) esquece o palito inicial, 3 · 50; E (200) conta
    4 palitos por quadrado.
  Em todas: leia o enunciado, escreva os três primeiros termos, conte os saltos,
  resolva e explique as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "entre os postes do km 3 e do km 27 vão entrar mais 5
  postes, todos igualmente espaçados. A distância entre eles é 24 ÷ 5? Não. Próximo
  episódio: contar termos e saltos sem errar."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: uma escada de 12 degraus com um bonequinho subindo; um contador de
  "saltos" marca 11 quando ele chega ao 12º degrau, ao lado da conta 50 + 11 · 15.
- Os quadrados de palitos sendo montados um a um, com o palito compartilhado piscando
  em amarelo; depois, os pontos da PA alinhados sobre uma reta tracejada.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Em todo termo geral foram usados n − 1 saltos (e não n)?
- A razão das PAs decrescentes aparece com sinal negativo?
- A explicação da alternativa A da Questão 1 usa 2 · 50 + 1 = 101 (e não 4 + 49 · 2,
  que daria 102)?
```

---

## Vídeo 2: Contar termos e saltos (meios, postes, múltiplos e três termos)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Sequências — Progressão Aritmética — Episódio 2 de 5:
Contar termos e saltos: meios, postes, múltiplos e três termos
RECORTE: use APENAS a seção 07 e, da seção 05, só "termo do meio é a média dos vizinhos"
e "notação simétrica para três termos" do material de apoio, mais as Questões 4, 5 e 6
da seção 12. A propriedade dos termos equidistantes fica para o episódio 3 (soma). O
teorema de Pitágoras e a área do triângulo retângulo são usados como ferramentas:
relembre em uma frase.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma cerca de 30 m com estacas a cada 3 m
   (conte com o dedo: 10 intervalos, 11 estacas) e por uma rodovia com postes.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (interpolar, meios aritméticos, extremos, intervalo, múltiplo, média
   aritmética, notação simétrica, hipotenusa, cateto).
3. Analogias âncora, retomadas ao longo da aula:
   - "postes e intervalos: entre 7 postes há 6 vãos";
   - "o '+ 1' conta o primeiro termo, que não é um salto";
   - "chame os três de x − r, x e x + r: na soma, o r se cancela e some".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: o termo geral e o
   "n − 1" (episódio 1), múltiplos de 7 (série de Divisibilidade, primos, MMC/MDC) e
   Pitágoras: hipotenusa² = cateto² + cateto².
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; desenhe SEMPRE a fila
   de termos (bolinhas) e os saltos (arcos) antes de dividir qualquer coisa.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Quantos números múltiplos de 7 existem de 105 até 497? A conta
  (497 − 105) ÷ 7 dá 56. A resposta certa é 57. Um termo some, e a alternativa errada
  está lá esperando."
- Promessa: "ao final, você vai contar termos, saltos e postes sem errar por um, e
  resolver problemas de três números em PA em uma linha".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) interpolar k meios: a PA fica com k + 2 termos e k + 1 saltos;
  b) os postes do km 3 ao km 27 com 5 postes no meio: 7 postes, 6 intervalos,
     6r = 24, r = 4 km;
  c) contar termos: múltiplos de 7 entre 100 e 500; o primeiro é 105, o último 497;
     497 = 105 + (n − 1) · 7 → n = 57; o atalho n = (último − primeiro) ÷ r + 1;
  d) postes × intervalos fora da fórmula: cerca de 30 m, estacas a cada 3 m → 10
     intervalos e 11 estacas;
  e) termo do meio = média dos vizinhos: 2b = a + c; (x, 10, 16) → x = 4;
  f) notação simétrica: x − r, x, x + r; soma 3x; com soma 36, o do meio é 12 na hora.
- Exercício "nós fazemos": peça "pause: quantos múltiplos de 6 há entre 50 e 200?"
  (primeiro 54, último 198: (198 − 54) ÷ 6 + 1 = 24 + 1 = 25).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "k meios entre dois números: k + 2 termos e k + 1 saltos."
  "Contar termos: (último − primeiro) ÷ razão, mais 1."
  "Três em PA: x − r, x e x + r."
- Erros clássicos:
  • 5 meios entre 3 e 27: r = 24/5 (o certo é 24/6);
  • esquecer o "+ 1" na contagem de múltiplos;
  • contar intervalos quando se pede objetos (ou o contrário).
- Questões no estilo ENEM, nesta ordem:
  • Questão 4 do material (postes do km 3 ao km 27): "eu faço", listando os 7 postes
    (3, 7, 11, 15, 19, 23, 27) e mostrando de onde vem cada errada (÷ 8, ÷ 7, ÷ 5, ÷ 4);
  • Questão 5 (ingressos múltiplos de 7 de 100 a 500): "nós fazemos";
  • Questão 6 (terreno triangular retângulo em PA, perímetro 36 m): "você faz", com
    pausa: x = 12; (12 + r)² = 12² + (12 − r)² → 48r = 144 → r = 3; lados 9, 12, 15;
    área 54 m².
  Em todas: leia o enunciado, desenhe a fila de termos, resolva e explique as
  alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "um menino somou 1 + 2 + 3 + … + 100 em segundos, sem
  calculadora. O truque dele soma qualquer PA. Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: uma rodovia com os postes do km 3 e do km 27; cinco postes novos
  caem do céu e se espalham; os 6 vãos acendem um a um com "4 km" em cada.
- Uma fila de bolinhas com arcos entre elas, com dois contadores lado a lado:
  "bolinhas (termos)" e "arcos (saltos)", sempre com um de diferença.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Termos e saltos foram contados separadamente em cada problema?
- A contagem de múltiplos de 7 dá 57 (com o "+ 1")?
- Os lados do triângulo são 9, 12 e 15, e a área é 54 m²?
```

---

## Vídeo 3: A soma de Gauss

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Sequências — Progressão Aritmética — Episódio 3 de 5:
A soma de Gauss: somar dezenas de termos em uma linha
RECORTE: use APENAS a seção 06 e, da seção 05, só "termos equidistantes dos extremos
têm a mesma soma" do material de apoio, mais as Questões 3, 8 e 9 da seção 12. A
estratégia 3 da seção 09 (soma = número de termos × termo médio) também entra. Na série
de Empréstimos e financiamentos, o total de juros do SAC já foi calculado como soma de
PA: cite como exemplo, sem refazer.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pela história do menino Gauss somando de 1 a 100
   e por um teatro com fileiras cada vez maiores. Só depois escreva S_n.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (soma dos n primeiros termos, S_n, extremos, termos equidistantes, média dos
   extremos, termo médio).
3. Analogias âncora, retomadas ao longo da aula:
   - "o truque de Gauss: junte o primeiro com o último, o segundo com o penúltimo;
     todos os pares dão a mesma soma";
   - "duas escadas encaixadas formam um retângulo: por isso se divide por 2";
   - "soma = quantos termos × a média entre o primeiro e o último".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: o termo geral
   (episódio 1) e média aritmética de dois números ((20 + 68) ÷ 2 = 44).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; antes de somar,
   escreva na tela "termo ou soma?" e, se o último termo não foi dado, calcule-o
   primeiro pelo termo geral.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "1 + 2 + 3 + … + 100. Um menino de dez anos deu a resposta em
  segundos: 5 050. Ele não era mais rápido nas contas; ele só juntou os números do
  jeito certo."
- Promessa: "ao final, você vai somar qualquer PA em uma linha e distinguir, no
  enunciado, quando a pergunta é o termo e quando é a soma".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) Gauss: 50 pares de soma 101 → 5 050;
  b) as duas escadas: 1 + 2 + … + 6 duas vezes formam 6 colunas de 7; 2S = 6 · 7; em
     geral, 2S = n · (a₁ + a_n);
  c) a fórmula S_n = (a₁ + a_n) · n ÷ 2, lida como "número de termos × média dos
     extremos";
  d) o teatro da seção 06: a₂₅ = 20 + 24 · 2 = 68; S = 44 · 25 = 1 100;
  e) somas para decorar: 1 + 2 + … + n = n(n + 1)/2; os n primeiros ímpares somam n²
     (os 10 primeiros, 100);
  f) termos equidistantes: a₃ + a₁₈ = a₁ + a₂₀ (índices somando 21); basta um par
     para ter a soma;
  g) o atalho do termo médio: (8, 11, 14, 17, 20) soma 5 · 14 = 70;
  h) você já viu isso disfarçado: na série de Empréstimos, os juros do SAC (400, 320,
     240, 160, 80) somaram (400 + 80) · 5 ÷ 2 = 1.200.
- Exercício "nós fazemos": peça "pause: quanto dá a soma dos 20 primeiros termos de
  (5, 8, 11, …)?" (a₂₀ = 5 + 19 · 3 = 62; S = (5 + 62) · 20 ÷ 2 = 67 · 10 = 670).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Primeiro com último: todos os pares dão a mesma soma."
  "Soma é número de termos vezes a média dos extremos."
  "'No 12º' é termo; 'em 12' ou 'ao todo' é soma."
- Erros clássicos:
  • S_n = n(a₁ + a_n), sem dividir por 2;
  • responder a_n quando pedem S_n (ou o contrário);
  • calcular o último termo com n saltos em vez de n − 1.
- Questões no estilo ENEM, nesta ordem:
  • Questão 3 do material (teatro de 25 fileiras): "eu faço", mostrando B (um salto a
    mais: 70), C (500 + 650), D (todas com 68) e E (sem dividir por 2);
  • Questão 8 (atleta, 2 km + 0,5 km por dia, 12 dias): "nós fazemos";
  • Questão 9 (a₃ + a₁₈ = 50, soma de 20 termos): "você faz", com pausa; mostre que não
    é preciso achar a₁ nem r.
  Em todas: leia o enunciado, sublinhe a palavra que decide "termo ou soma", resolva e
  explique as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "juros simples, calendário, prestação de financiamento:
  a PA aparece em muito lugar sem dizer o nome. E você já esbarrou nela em outras
  séries. Próximo episódio: a PA disfarçada."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: os números de 1 a 100 em fila; o 1 e o 100 se dão as mãos (101),
  depois o 2 e o 99, e assim por diante, até 50 pares iguais empilhados; depois, duas
  escadas de bloquinhos (1 a 6) encaixando-se num retângulo 6 × 7.
- O teatro visto de cima, com as fileiras crescendo de 2 em 2 e um contador de cadeiras.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Em toda soma, o último termo foi calculado com n − 1 saltos antes de usar a fórmula?
- Todas as somas foram divididas por 2?
- A Questão 8 dá 57 km e a Questão 9 dá 500?
```

---

## Vídeo 4: A PA disfarçada (juros simples, calendário, SAC)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Sequências — Progressão Aritmética — Episódio 4 de 5:
A PA disfarçada: juros simples, calendário e financiamentos
RECORTE: use APENAS a seção 08 do material de apoio, mais a Questão 7 da seção 12.
Juros simples já tiveram série própria (Juros Simples), e o SAC apareceu na série de
Empréstimos e financiamentos: aqui, o tom é "você já viu isso disfarçado"; revise em
uma frase cada um, sem reensinar.
DURAÇÃO: 6 a 8 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por um extrato de aplicação a juros simples, uma
   folha de calendário e um boleto de financiamento que diminui todo mês.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (capital, taxa, montante, juros simples, depreciação linear, amortização,
   termo zero).
3. Analogias âncora, retomadas ao longo da aula:
   - "a escada de degraus iguais" (a mesma do episódio 1): juros simples sobem sempre o
     mesmo degrau, C · i;
   - "o termo zero é o chão: o dinheiro aplicado HOJE ainda não subiu nenhum degrau";
   - "a semana é uma PA de razão 7".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: juros simples
   J = C · i · t e montante M = C + J (série de Juros Simples) e o termo geral
   (episódio 1).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; defina SEMPRE, em voz
   alta, o que é o termo 1 (o fim do 1º mês? o dia de hoje?) antes de usar a fórmula.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Você já estudou PA sem saber: na série de Juros Simples, os
  montantes de R$ 1.000,00 a 3% ao mês eram 1.030, 1.060, 1.090… Degraus de R$ 30,00.
  Hoje você reconhece a PA escondida em qualquer enunciado."
- Promessa: "ao final, você vai identificar a PA em juros simples, calendários,
  depreciação, treinos e financiamentos, e não errar o 'mês 1'".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) a tabela da seção 08: juros simples (razão C · i: R$ 60,00 ao mês para
     R$ 2.000,00 a 3%), depreciação linear (razão negativa), calendário (razão 7),
     treino progressivo, padrões de figuras;
  b) juros simples como PA: montante ao fim do mês n = C + n · C · i; o capital C é o
     termo ZERO (instante da aplicação), não o termo 1;
  c) calendário: se o dia 3 é segunda, as segundas são 3, 10, 17, 24, 31; para datas
     distantes, divida a distância em dias por 7 e olhe o resto;
  d) SAC (só citado, da série de Empréstimos): o saldo cai sempre a mesma amortização,
     então os juros e as parcelas caem em PA (juros 400, 320, 240, 160, 80);
  e) a ponte com a função afim: razão = taxa de variação; montante de juros simples é
     uma reta, como na série de Função Afim.
- Exercício "nós fazemos": peça "pause: num mês, o dia 4 é uma terça-feira. Que dia da
  semana é o dia 29?" (29 − 4 = 25 dias; 25 = 3 · 7 + 4; terça + 4 dias = sábado).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Aumento constante é PA, mesmo sem o nome."
  "Juros simples: o capital é o termo zero."
  "A semana é uma PA de razão 7: olhe o resto da divisão."
- Erros clássicos:
  • tratar o capital como o termo 1 e usar M_n = C + (n − 1) · C · i;
  • contar o próprio dia de partida no calendário (usar 26 em vez de 25 dias);
  • tratar os juros do SAC como constantes.
- Questões no estilo ENEM:
  • Questão 7 do material (R$ 2.000,00 a 3% ao mês, montante de R$ 3.080,00): "você
    faz", com pausa. Resolva com o termo zero (2 000 + 60n = 3 080 → n = 18, B) e
    mostre por que C (19) aparece: quem chama 2 000 de termo 1 usa
    2 000 + (n − 1) · 60. Explique também A (17: parte de 2 060 e esquece o + 1),
    D (36: juro de R$ 30,00 ao mês) e E (51: divide o montante inteiro por 60).
    Conferência: 18 meses × R$ 60,00 = R$ 1.080,00 de juros.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "no último episódio deste assunto, juntamos tudo,
  caçamos as pegadinhas e treinamos para o ENEM."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: um extrato bancário cujas linhas viram degraus de uma escada
  (2.000 no chão, marcado "mês 0", depois 2.060, 2.120, …), com o degrau 18 acendendo
  em 3.080.
- Uma folha de calendário com as segundas-feiras se acendendo de 7 em 7.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Ficou claro que, nos juros simples, o capital é o termo zero (e a Questão 7 dá 18)?
- O exercício do calendário conta 25 dias (de 4 a 29) e chega ao sábado?
- Juros Simples e SAC foram citados como revisão, sem reensinar?
```

---

## Vídeo 5: Revisão (Progressão aritmética no ENEM)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula de REVISÃO para o YouTube sobre:

TEMA: Matemática — Sequências — Progressão Aritmética — Episódio 5 de 5:
Revisão geral, estratégia de prova, pegadinhas e treino para o ENEM
RECORTE: use as seções 01, 09, 10, 11 e 13 do material de apoio.
NÃO reutilize as Questões 1 a 9 da seção 12 (já resolvidas nos episódios anteriores).
Progressão geométrica terá série própria: aqui, só cite a ponte.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que assistiu aos episódios 1 a 4, mas ainda é iniciante e pode ter esquecido
partes. Relembre cada conceito em uma frase simples antes de cobrá-lo.

REGRAS DE EXPLICAÇÃO
1. Cada conceito é relembrado com a mesma analogia âncora usada no seu episódio:
   a escada de degraus iguais; do 1º ao 12º degrau, 11 saltos; teste com n = 1; postes
   e intervalos; o "+ 1" que conta o primeiro; x − r, x, x + r; o truque de Gauss; as
   duas escadas que formam um retângulo; soma = termos × média; o termo zero dos juros
   simples; a semana como PA de razão 7.
2. Prática de recuperação: antes de explicar, PERGUNTE e peça para o aluno pausar.
3. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
4. Uma ideia por cena. Frases curtas. Tom de conversa, falando com "você".

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "O nome 'progressão aritmética' pode nem aparecer na prova. O
  que aparece é palito de fósforo, fileira de teatro, depósito que aumenta todo mês. E
  quase todo distrator é feito de um único erro: o n − 1."
- O que a prova cobra (seção 01): padrões de figuras, termo distante, soma de muitos
  termos, contagem; e as duas habilidades que rendem mais: o "n − 1" e a soma pela
  média.
- Onde aparece nas outras áreas (seção 10): Matemática Financeira (juros simples),
  Física (velocidades no MUV; distâncias 1, 3, 5, 7… em segundos sucessivos a partir do
  repouso), Química (séries homólogas: +CH₂, +14 u), Geografia (cerca de 6,5 °C a menos
  a cada 1 000 m de altitude).
- A estratégia de prova em 3 hábitos (seção 09): escrever os três primeiros termos;
  decidir "termo ou soma?"; usar a média na soma.
- "Verdadeiro ou falso? Pause e responda": transforme em afirmações os 9 erros da
  seção 11. Para cada um: pausa → resposta → por que a pegadinha engana →
  a regra certa em uma frase.
- 5 questões INÉDITAS no estilo ENEM, criadas por você, com situações hipotéticas e
  5 alternativas cada (use estes números e confira as contas):
  1) padrão de triângulos de palitos em fila (a figura 1 tem 3 palitos e cada triângulo
     novo acrescenta 2): a_n = 2n + 1; figura 40 → 81 palitos (erradas: 120, três por
     triângulo; 80, esquece o palito inicial; 83, usa 40 saltos, 3 + 40 · 2; 79, usa
     39 triângulos, 2 · 39 + 1);
  2) termo × soma: poupança com R$ 30,00 no 1º mês e R$ 10,00 a mais a cada mês; total
     depositado em 10 meses: a₁₀ = 120, S = (30 + 120) · 10 ÷ 2 = R$ 750,00 (erradas:
     R$ 120,00, só o 10º depósito; R$ 1.500,00, sem dividir por 2; R$ 800,00, com
     a₁₀ = 130 por usar 10 saltos; R$ 300,00, 30 · 10, sem os aumentos);
  3) postes a cada 40 m ao longo de 1 km, com poste nas duas pontas: 25 intervalos e
     26 postes (erradas: 25; 24; 40; 27);
  4) interpolar 4 meios aritméticos entre 10 e 35: 5 saltos, r = 5, PA (10, 15, 20,
     25, 30, 35) (erradas: r = 6,25, dividir por 4; r ≈ 4,17, dividir por 6; r = 25;
     r = 7);
  5) PA de 15 termos cujo 8º termo (o do meio) vale 12: soma = 15 · 12 = 180 (erradas:
     90, dividir por 2 sem necessidade; 168, usar 14 termos; 192, usar 16 termos; 360,
     acha a soma dos extremos (2 · 12 = 24) e esquece de dividir por 2, 15 · 24).
  As alternativas erradas devem ser exatamente os erros clássicos (um salto a mais,
  esquecer o "+ 1", não dividir por 2, responder termo quando se pede soma, contar
  intervalos no lugar de objetos). Leia, peça a pausa, escreva os primeiros termos,
  resolva e explique cada alternativa.
- Checklist de domínio (seção 13): leia os itens e diga "marque só o que você
  conseguiria explicar em voz alta para outra pessoa, sem consultar nada; o que não
  marcou, reveja o episódio correspondente" (razão, termo geral, figuras e PA como
  afim: episódio 1; média dos vizinhos, três termos, interpolação e contagem:
  episódio 2; soma e equidistantes: episódio 3; juros simples, calendário e treinos:
  episódio 4).
- Meta antes de considerar dominado: resolver 30 questões e acertar pelo menos 21
  (70%), com pelo menos dez de contexto (padrões, cotidiano, contagem).
- Encerramento e ponte: "o próximo assunto é Progressão geométrica e soma dos
  infinitos termos: o crescimento deixa de ser por soma e passa a ser por
  multiplicação."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Use um cronômetro visual nas pausas; um selo "PEGADINHA" em amarelo nos erros; os
  4 ícones dos episódios (escada de degraus, fila de postes, pares de Gauss, extrato
  bancário) como índice visual da revisão.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Cada conceito foi relembrado antes de ser cobrado?
- As 5 questões inéditas têm uma única alternativa correta e contas corretas?
- Na questão 3, a resposta é 26 postes (25 intervalos + 1)?
```

---

## Cuidados ao revisar os roteiros

- **O "n − 1":** o 12º termo de (50, 65, 80, …) é 50 + **11** · 15 = 215. Confira cada termo geral do roteiro: a IA escorrega para 12 · 15 (230), que é justamente o distrator.
- **Questão 7 (juros simples):** a resposta é **18**, porque R$ 2.000,00 é o valor no instante zero (montante do mês n = 2 000 + 60n). Se a IA usar a₁ = 2 000 e a fórmula com n − 1, chega a 19 e "confirma" o distrator C.
- **Interpolação:** 5 meios entre 3 e 27 são **7 termos e 6 saltos** (r = 4). A IA às vezes divide por 5.
- **Soma:** toda soma usa ÷ 2 (S = 44 · 25 = 1 100 no teatro; 9,5 · 6 = 57 no treino). Desconfie de 2 200 ou 114.

## Erros encontrados no material

- **Questão 1, explicação da alternativa A (101):** o material diz que "A usa razão 2". Pelo termo geral, razão 2 daria 4 + 49 · 2 = **102**, não 101. O valor 101 vem da forma simplificada com 2 no lugar de 3: 2 · 50 + 1 (quem acha que cada quadrado novo acrescenta 2 palitos). Explicação corrigida no prompt do Vídeo 1.
