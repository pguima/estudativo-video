# Função Logarítmica e aplicações (pH, Richter, decibéis) — série de videoaulas

Material de apoio: `01-matematica/28-funcao-logaritmica-aplicacoes.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Definição de log, propriedades, log 2 e log 3 | **Logaritmos** | Revisão relâmpago. O log do produto é usado no pH (vídeo 2) e o log do quociente na magnitude (vídeo 3). Não reensino. |
| Gráfico da exponencial, assíntota, inequação com base entre 0 e 1 | **Função exponencial, vídeos 1 e 5** | O vídeo 1 desenha o log como espelho da exponencial e reaproveita a regra "base menor que 1 inverte". |
| "Quantas vezes maior" é divisão; diferença de ordens de grandeza é fator 10 | **Notação científica e ordem de grandeza** | Revisão de 30 s no vídeo 2. É a base da regra "diferença de leitura = expoente da razão". |
| Domínio de uma fórmula | **Conceito de função** | Revisão de 30 s no vídeo 1. |
| Função inversa, simetria na reta y = x | **Função composta e inversa** (série futura) | Só cito: "inversa tem série própria". |
| Meia-vida, tempo para dobrar | **Função exponencial** (contando intervalos) e **Logaritmos** (com log, Q1 e Q8) | **Este material não trata disso**, então não entra aqui. Não há questão repetida entre as três séries. |
| pH, decibéis, Richter em Química, Física e Geografia | Sem série própria no canal até agora | Uso **só as fórmulas e os números do material**: pH = −log[H⁺], log E = 4,8 + 1,5M, M_w = (2/3) · log M₀ − 10,7, β = 10 · log(I/I₀), I₀ = 10⁻¹² W/m². |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. A função logarítmica: o espelho da exponencial (gráfico, domínio e sinal)** | 02, 03, 04 | Q7 | 10–12 min |
| **2. Escalas logarítmicas e o pH** | 05, 06 | Q1, Q2, Q6 | 10–12 min |
| **3. Terremotos: amplitude, energia e magnitude de momento** | 07 | Q3, Q8 | 8–10 min |
| **4. Decibéis: por que 80 + 80 não dá 160** | 08 | Q5, Q4, Q9 | 8–10 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Vídeo 1: A função logarítmica: o espelho da exponencial (gráfico, domínio e sinal)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Função Logarítmica e aplicações (pH, Richter, decibéis) —
Episódio 1 de 5: A função logarítmica: o espelho da exponencial (gráfico, domínio e
sinal)
RECORTE: use APENAS as seções 02, 03 e 04 do material de apoio, mais a Questão 7 da
seção 12. A definição de log já foi ensinada na série de Logaritmos; o gráfico da
exponencial e a regra "base entre 0 e 1 inverte a desigualdade", na série de Função
exponencial; domínio, na série de Conceito de função: aqui, revisão rápida. Função
inversa tem série própria (Função composta e inversa): só cite. As escalas (pH,
Richter, decibéis) ficam para os próximos episódios.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por alguém que treina para uma prova e percebe
   que as primeiras horas rendem muitos pontos e as seguintes, cada vez menos (o modelo
   P(t) = 20 · log t do material); só depois mostre a função.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (função logarítmica, funções inversas, domínio, imagem, assíntota vertical,
   crescente, decrescente, sinal, inequação logarítmica).
3. Analogias âncora, retomadas ao longo da aula:
   - "o log é a exponencial vista no espelho da reta y = x: o ponto (a, b) vira (b, a)";
   - "retorno decrescente: para o log subir um degrau, x precisa ser multiplicado por
     10";
   - "dentro do log só entra número estritamente positivo: a porta do log fica fechada
     para o zero e para os negativos".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: log_b a = x ⇔ bˣ = a e
   as condições de existência (série de Logaritmos); o gráfico de 2ˣ passando por
   (0, 1) com assíntota y = 0 (série de Função exponencial); domínio como "os valores
   que podem entrar" (série de Conceito de função).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; em domínio e
   inequações, escreva a condição "> 0" antes de qualquer conta.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Num modelo de desempenho P(t) = 20 · log t, com t em horas de
  treino, 100 horas dão 40 pontos. Para chegar a 60 pontos, você precisa de 200 horas?
  Não: de 1 000. Essa é a cara do logaritmo."
- Promessa: "ao final, você vai desenhar o gráfico do log, ler a base num gráfico,
  achar o domínio de uma expressão e resolver inequações logarítmicas".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) definição: f(x) = log_b x, com b > 0, b ≠ 1, definida para x > 0; domínio ]0, +∞[;
     imagem ℝ;
  b) o espelho: se 2³ = 8, então log_2 8 = 3; cada ponto (a, b) de y = 2ˣ aparece como
     (b, a) em y = log_2 x ((0, 1) ↔ (1, 0); (1, 2) ↔ (2, 1); (3, 8) ↔ (8, 3)); a
     assíntota horizontal da exponencial vira a assíntota vertical do log; domínio e
     imagem trocam de papel (só cite que funções inversas têm série própria);
  c) o gráfico: base maior que 1 sobe, base entre 0 e 1 desce; toda função logarítmica
     passa por (1, 0) e por (b, 1); log_(1/2) x = −log_2 x, espelho no eixo x;
  d) o sinal (tabela da seção 03): com b > 1, negativo entre 0 e 1 (log 0,01 = −2) e
     positivo para x > 1; com 0 < b < 1, o contrário (log_0,5 8 = −3);
  e) retorno decrescente: de 1 para 10, de 10 para 100, de 100 para 1 000, o log sobe
     sempre 1; no modelo P(t) = 20 · log t, de 40 para 60 pontos é de 100 para 1 000
     horas;
  f) domínio (tabela da seção 04): log(2x − 6) → x > 3; log(x² − 9) → x < −3 ou x > 3;
     log_x (5 − x) → 0 < x < 5 e x ≠ 1;
  g) inequações: base maior que 1 mantém o sentido (log_2 x > 3 → x > 8); base entre 0
     e 1 inverte (log_0,5 x > 2 → x < 0,25, e com o domínio: 0 < x < 0,25).
- Exercício "nós fazemos": peça "pause: qual é o domínio de f(x) = log(3x − 12)? E qual
  é a solução de log_3 x < 2?" (3x − 12 > 0 → x > 4; x < 3² = 9, com o domínio:
  0 < x < 9).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Log e exponencial são espelhos na reta y = x."
  "Toda função logarítmica passa por (1, 0) e por (b, 1)."
  "Dentro do log, só número estritamente positivo."
- Erros clássicos:
  • domínio de log(2x − 6): x ≥ 3 (o certo é x > 3: log 0 não existe);
  • log_0,5 x > 2 ⇒ x > 0,25 (o certo é 0 < x < 0,25: base menor que 1 inverte);
  • "o logaritmo cresce cada vez mais rápido" (cresce cada vez mais devagar).
- Questão no estilo ENEM: Questão 7 do material (f(x) = log_b x passa por (25, 2); pede
  x com f(x) = −1): "nós fazemos". Diga "pause o vídeo e tente": b² = 25 → b = 5;
  log_5 x = −1 → x = 5⁻¹ = 0,2. Explique as erradas: −5 faz x = −b (mas x precisa ser
  positivo); 0,04 usa 25 como base (25⁻¹); 0,5 usa a ordenada 2 como base (2⁻¹); 5 é o
  ponto em que f(x) = 1.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "um suco tem pH 3 e a água da chuva tem pH 6. O suco
  é 2 vezes mais ácido? 3 vezes? Mil vezes? Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: o gráfico de y = 2ˣ sendo dobrado sobre a reta tracejada y = x
  como uma folha de papel, cada ponto pulando para a posição trocada e virando
  y = log_2 x; a assíntota horizontal girando até virar vertical.
- Uma escada de log com degraus iguais na altura e cada vez mais compridos na
  horizontal (1, 10, 100, 1 000).
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Os pontos trocados (0, 1) ↔ (1, 0) e (3, 8) ↔ (8, 3) estão corretos no gráfico?
- Nas inequações, o domínio entrou na resposta final (0 < x < 0,25 e 0 < x < 9)?
- A resposta da Questão 7 é 0,2?
```

---

## Vídeo 2: Escalas logarítmicas e o pH

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Função Logarítmica e aplicações (pH, Richter, decibéis) —
Episódio 2 de 5: Escalas logarítmicas e o pH
RECORTE: use APENAS as seções 05 e 06 do material de apoio (e o quadro "O que rende
mais aqui" da seção 01), mais as Questões 1, 2 e 6 da seção 12. Use SOMENTE as
fórmulas e os valores do material (pH = −log[H⁺], [H⁺] = 10⁻ᵖᴴ mol/L, neutro pH 7 a
25 °C, pH + pOH = 14 só citado); não acrescente outras fórmulas de Química. "Quantas
vezes maior é divisão" e ordem de grandeza já foram ensinados na série de Notação
científica; o log do produto, na série de Logaritmos: aqui, revisão rápida. Richter e
decibéis ficam para os episódios 3 e 4.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pelo suco de limão (pH perto de 2), pelo café
   (pH perto de 5) e pela água da chuva; só depois apresente a fórmula.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (escala logarítmica, leitura, grandeza, razão, concentração, íon hidrogênio
   H⁺, mol/L, pH, ácido, neutro).
3. Analogias âncora, retomadas ao longo da aula:
   - "a escala logarítmica é uma régua de zeros: cada passo igual na régua é um fator
     10 na grandeza";
   - "diferença de leitura vira expoente da razão";
   - "o pH é uma escala de cabeça para baixo: menor pH, mais ácido".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: "quantas vezes maior"
   é divisão e duas ordens de grandeza de diferença são fator 100 (série de Notação
   científica); log(M · N) = log M + log N e log 2 ≈ 0,30 (série de Logaritmos).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; escreva "mol/L" ao lado
   de toda concentração e, em toda comparação, escreva primeiro a DIFERENÇA das
   leituras.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "pH 2 e pH 5. Diferença de 3. Quem responde '3 vezes mais
  ácido' erra por muito: a concentração de H⁺ é 1 000 vezes maior."
- Promessa: "ao final, você vai comparar duas leituras de uma escala logarítmica e
  calcular o pH de uma solução, mesmo com um 2 ou um 5 na frente da potência de 10".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) o problema: o ouvido percebe intensidades de cerca de 10⁻¹² a 1 W/m², um fator de
     um trilhão; numa régua comum, tudo ficaria espremido perto do zero; a escala
     logarítmica troca cada fator 10 por um passo igual;
  b) a regra que resolve quase tudo (base 10): G₂ ÷ G₁ = 10^(E₂ − E₁);
  c) a tabela da seção 05: diferença 0,3 → cerca de 2; 1 → 10; 1,5 → cerca de 32;
     2 → 100; 3 → 1 000;
  d) diferença não é razão: dividir as leituras (5 ÷ 2 = 2,5) ou parar na diferença (3)
     são os dois distratores clássicos;
  e) pH = −log[H⁺] ⇔ [H⁺] = 10⁻ᵖᴴ mol/L; o sinal de menos existe porque as
     concentrações são potências negativas de 10; neutro: pH 7 a 25 °C;
  f) a tabela da seção 06: 10⁻³ → pH 3; 2 · 10⁻⁵ → −(0,30 − 5) = 4,7;
     5 · 10⁻⁴ → −(0,70 − 4) = 3,3;
  g) o atalho: se [H⁺] = k · 10⁻ⁿ com 1 < k < 10, o pH = n − log k fica entre n − 1 e n;
  h) menor pH, mais ácido: cada unidade a menos multiplica [H⁺] por 10 (limão × café:
     cerca de 1 000 vezes).
- Exercício "nós fazemos": peça "pause: uma solução tem pH 4 e outra, pH 6. Quantas
  vezes mais H⁺ tem a primeira?" (diferença 2 → 10² = 100 vezes).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Numa escala de base 10, a diferença de leitura é o expoente da razão."
  "Menor pH, mais ácido: cada unidade a menos é 10 vezes mais H⁺."
  "Se [H⁺] = k · 10⁻ⁿ, o pH fica entre n − 1 e n."
- Erros clássicos:
  • pH 2 e pH 5: 3 vezes mais ácido (o certo é 10³ = 1 000 vezes);
  • pH maior = mais ácido (o sinal de menos inverte a relação);
  • log(2 · 10⁻⁵) = log 2 · (−5) (o certo é 0,30 − 5: log do produto é soma).
- Questões no estilo ENEM, nesta ordem:
  • Questão 1 do material (suco pH 3, chuva pH 6): "eu faço". 10⁻³ ÷ 10⁻⁶ = 10³ = 1 000.
    Explique: 2 divide os pHs; 3 para na diferença; 30 multiplica a diferença por 10;
    1 000 000 usa só o pH da chuva como expoente;
  • Questão 2 ([H⁺] = 2 · 10⁻⁴ mol/L, log 2 = 0,30): "nós fazemos". pH = −(0,30 − 4) =
    3,7; o atalho já diz "entre 3 e 4". Explique: 3,4 desconta 2 · log 2; 4,0 ignora o
    fator 2; 4,3 soma o log 2 (erro no sinal); 4,6 erra o sinal e dobra o log 2;
  • Questão 6 (piscina, pH entre 7,2 e 7,8, maior [H⁺]): "você faz", com pausa.
    10^(−7,2) (o menor pH dá a maior concentração; −7,2 > −7,8). Explique: 10^(−7,8)
    inverte a relação; 10^(−0,6) usa a largura da faixa; 10^(7,2) e 10^(7,8) esquecem o
    sinal e dariam concentrações absurdas.
  Escreva os expoentes como "10 elevado a −7,2" na narração, para não confundir.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "um terremoto de magnitude 7 contra um de magnitude 5:
  a energia é 2 vezes maior? 100 vezes? 1 000 vezes? Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: uma régua de pH de 0 a 14 em que cada passo para a esquerda faz
  uma pilha de "bolinhas de H⁺" ficar 10 vezes maior; o limão em 2 e o café em 5, com
  a pilha do limão 1 000 vezes maior.
- A conversão de 2 · 10⁻⁴ em pH, com log 2 e log 10⁻⁴ aparecendo como duas parcelas.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Em toda comparação, a diferença das leituras virou EXPOENTE de 10?
- Nenhuma fórmula de Química além das do material foi acrescentada?
- As respostas são 100 (exercício), 1 000 vezes (Q1), 3,7 (Q2) e 10 elevado a −7,2 (Q6)?
```

---

## Vídeo 3: Terremotos: amplitude, energia e magnitude de momento

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Função Logarítmica e aplicações (pH, Richter, decibéis) —
Episódio 3 de 5: Terremotos: amplitude, energia e magnitude de momento
RECORTE: use APENAS a seção 07 do material de apoio (e o hábito 2 da seção 09), mais as
Questões 3 e 8 da seção 12. Use SOMENTE as três fórmulas do material:
M = log A − log A₀ = log(A/A₀); log E = 4,8 + 1,5M (E em joules);
M_w = (2/3) · log M₀ − 10,7 (M₀ em dina·cm). Não acrescente outras fórmulas de
sismologia. A regra "diferença de leitura = expoente da razão" é do episódio 2: aqui,
revisão rápida.
DURAÇÃO: 8 a 10 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pela manchete "terremoto de magnitude 7 na escala
   Richter" e pelo sismógrafo riscando o papel; só depois apresente as fórmulas.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (sismógrafo, amplitude, amplitude de referência, magnitude, energia liberada,
   momento sísmico, magnitude de momento).
3. Analogias âncora, retomadas ao longo da aula:
   - "dois placares no mesmo terremoto: por grau, a amplitude sobe ×10 e a energia
     sobe ×32";
   - "na comparação, a constante se cancela: o 4,8 está nos dois lados e some";
   - "para voltar da magnitude ao momento sísmico, desfaça de fora para dentro, como
     quem tira as roupas na ordem inversa em que vestiu".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: G₂ ÷ G₁ = 10^(E₂ − E₁)
   (episódio 2); log(A/A₀) = log A − log A₀ (série de Logaritmos); 10^1,5 ≈ 31,6.
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; na fórmula de M_w,
   multiplique primeiro e subtraia depois, dizendo isso em voz alta.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "De magnitude 5 para 7, o sismógrafo registra uma amplitude
  100 vezes maior. Mas a energia liberada é 1 000 vezes maior. Duas respostas
  diferentes para a mesma pergunta, e as duas estão nas alternativas."
- Promessa: "ao final, você vai comparar terremotos pela amplitude e pela energia sem
  confundir os fatores, e calcular uma magnitude por fórmula dada".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) magnitude pela amplitude: M = log(A/A₀); um grau a mais, amplitude 10 vezes maior;
  b) energia: log E = 4,8 + 1,5M; um grau a mais, energia 10^1,5 ≈ 32 vezes maior; dois
     graus, 10³ = 1 000 vezes;
  c) comparação: subtraindo as duas relações, o 4,8 se cancela; divida a diferença de
     log pelo coeficiente certo e eleve 10;
  d) magnitude de momento: M_w = (2/3) · log M₀ − 10,7, a escala usada hoje pelos
     sismólogos, embora o noticiário diga "escala Richter"; com M₀ = 10²⁴:
     (2/3) · 24 − 10,7 = 16 − 10,7 = 5,3;
  e) o caminho inverso: some 10,7, multiplique por 3/2 e eleve 10 ao resultado;
  f) amplitude × energia: de 5 para 7, amplitude ×100 e energia ×1 000; leia qual das
     duas o enunciado pede.
- Exercício "nós fazemos": peça "pause: qual é a magnitude de momento de um terremoto
  com M₀ = 10²¹ dina·cm?" ((2/3) · 21 − 10,7 = 14 − 10,7 = 3,3).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Um grau a mais: amplitude ×10, energia cerca de ×32."
  "Na comparação, a constante se cancela: divida a diferença pelo coeficiente e eleve
  10."
  "Na fórmula, multiplique primeiro e subtraia depois; para voltar, desfaça de fora para
  dentro."
- Erros clássicos:
  • +2 graus: energia ×100 (o certo é ×1 000: na energia, o fator por grau é 10^1,5);
  • subtrair 10,7 antes de multiplicar por 2/3.
- Questões no estilo ENEM, nesta ordem:
  • Questão 3 do material (log E = 4,8 + 1,5M, magnitudes 5 e 7): "eu faço".
    1,5 · (7 − 5) = 3 → 10³ = 1 000 vezes. Explique: 3 esquece de elevar 10; 100 é a
    razão das amplitudes; 10 000 eleva ao quadrado a razão das amplitudes; 63 000
    mantém o 4,8 no expoente (10^4,8 ≈ 63 000), que se cancela;
  • Questão 8 (M_w com M₀ = 10²⁷ dina·cm): "você faz", com pausa. (2/3) · 27 − 10,7 =
    18 − 10,7 = 7,3. Explique: 10,9 subtrai antes de multiplicar; 18,0 esquece o −10,7;
    28,7 soma 10,7; 29,8 inverte a fração (3/2 · 27 − 10,7).
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "duas máquinas de 80 dB funcionando juntas fazem
  160 dB? Se fizessem, uma oficina seria mais barulhenta que um avião. Próximo
  episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: dois placares lado a lado ("amplitude" e "energia") enquanto a
  magnitude sobe de 5 para 6 e para 7: o primeiro multiplica por 10 a cada grau, o
  segundo por cerca de 32, chegando a ×100 e ×1 000.
- A fórmula de M_w com as operações numeradas (1º multiplica, 2º subtrai) e, no caminho
  inverso, as mesmas operações desfeitas em ordem contrária.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- A diferença entre o fator da amplitude (×10) e o da energia (cerca de ×32) ficou
  clara?
- Nenhuma fórmula além das três do material foi usada?
- As respostas são 3,3 (exercício), 1 000 vezes (Q3) e 7,3 (Q8)?
```

---

## Vídeo 4: Decibéis: por que 80 + 80 não dá 160

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Função Logarítmica e aplicações (pH, Richter, decibéis) —
Episódio 4 de 5: Decibéis: por que 80 + 80 não dá 160
RECORTE: use APENAS a seção 08 do material de apoio (e o hábito 1 da seção 09), mais as
Questões 5, 4 e 9 da seção 12. Use SOMENTE a fórmula e os valores do material:
β = 10 · log(I/I₀), I₀ = 10⁻¹² W/m², 85 dB como limite das normas trabalhistas
brasileiras para 8 horas sem proteção, e a tabela +3 dB (cerca de ×2), +10 dB (×10),
+20 dB (×100), +40 dB (×10 000). Não acrescente outras fórmulas de Física. A regra da
diferença de leitura é do episódio 2: aqui, revisão rápida.
DURAÇÃO: 8 a 10 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma biblioteca, uma avenida movimentada, uma
   britadeira e uma oficina com várias máquinas; só depois apresente a fórmula.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (intensidade sonora, W/m², limiar da audição, limiar da dor, nível sonoro,
   decibel, fonte sonora).
3. Analogias âncora, retomadas ao longo da aula:
   - "cada 10 dB é um zero a mais na intensidade";
   - "o fator 10 da fórmula 'come' um zero da diferença: divida por 10 antes de
     elevar";
   - "intensidades se somam como copos de água num balde; decibéis não, são só a
     etiqueta do balde".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: log 10ⁿ = n e
   10 · log 2 ≈ 3 (série de Logaritmos); a regra G₂ ÷ G₁ = 10^(E₂ − E₁) (episódio 2);
   divisão de potências de 10 subtrai expoentes (série de Notação científica).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; escreva "W/m²" ao lado
   de toda intensidade e "dB" ao lado de todo nível.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Uma máquina faz 80 dB. Ligue outra igual ao lado. O barulho
  vai para 160 dB? Não: vai para cerca de 83 dB. Para chegar a 90 dB, você precisaria
  de dez máquinas."
- Promessa: "ao final, você vai calcular decibéis, comparar dois sons em 'quantas
  vezes' e somar fontes sonoras sem cair na pegadinha".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) a fórmula: β = 10 · log(I/I₀), com I₀ = 10⁻¹² W/m²; exemplo do material: som de
     10⁻⁵ W/m² → 10 · log 10⁷ = 70 dB;
  b) do limiar da audição ao da dor, a intensidade cresce um trilhão de vezes, mas a
     escala vai só de 0 a 120 dB; 85 dB é o limite trabalhista para 8 horas sem
     proteção;
  c) a tabela da seção 08: +3 dB → cerca de ×2; +10 dB → ×10; +20 dB → ×100;
     +40 dB → ×10 000;
  d) comparar: ache a diferença, divida por 10 (o coeficiente da fórmula) e eleve 10;
  e) decibéis não se somam: duas fontes iguais dobram a intensidade e somam cerca de
     3 dB (80 → perto de 83 dB); para ganhar 10 dB, dez fontes iguais.
- Exercício "nós fazemos": peça "pause: um som de intensidade 10⁻⁶ W/m² tem quantos
  decibéis?" (10⁻⁶ ÷ 10⁻¹² = 10⁶; 10 · 6 = 60 dB).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Cada 10 dB a mais, intensidade ×10."
  "Para comparar, divida a diferença por 10 e eleve 10 ao resultado."
  "Intensidades se somam; decibéis, não: dobrar a intensidade soma cerca de 3 dB."
- Erros clássicos:
  • +1 dB = intensidade ×10 (o certo é +10 dB);
  • 80 dB + 80 dB = 160 dB (o certo é cerca de 83 dB).
- Questões no estilo ENEM, nesta ordem:
  • Questão 5 do material (britadeira, I = 10⁻⁴ W/m²): "eu faço".
    10 · log(10⁻⁴ ÷ 10⁻¹²) = 10 · log 10⁸ = 80 dB. Explique: −40 dB esquece de dividir
    por I₀; 8 dB esquece o fator 10; 120 dB usa só o expoente de I₀; 160 dB soma os
    expoentes em módulo (4 + 12). Comente: 80 dB está abaixo de 85 dB, mas perto;
  • Questão 4 (avenida 80 dB, biblioteca 40 dB): "nós fazemos". 40 ÷ 10 = 4 →
    10⁴ = 10 000 vezes. Explique: 2 divide os níveis; 4 esquece de elevar 10; 40 usa a
    diferença como razão; 10⁴⁰ esquece de dividir por 10;
  • Questão 9 (oficina: uma máquina de 70 dB; quantas no total para 80 dB): "você
    faz", com pausa. +10 dB = ×10 na intensidade → 10 máquinas no total. Explique: 2
    supõe que dobrar soma 10 dB (com 2 seriam cerca de 73 dB); 4 supõe que cada máquina
    extra soma 3 dB; 8 divide 80 por 10; 11 conta "10 a mais" esquecendo que a original
    já conta (com 11, cerca de 80,4 dB).
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "no último episódio deste assunto, juntamos pH,
  terremotos e decibéis, caçamos as pegadinhas e treinamos com questões de Química,
  Física e Geografia."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: um medidor de decibéis subindo de 10 em 10 enquanto uma pilha de
  "ondas" de intensidade ganha um zero a mais a cada passo; depois, uma segunda máquina
  sendo ligada e o medidor indo de 80 só até 83 (com um "160" riscado em vermelho).
- Um balde de intensidade recebendo dez copos iguais, e só então o medidor mostra
  +10 dB.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- A diferença em dB foi dividida por 10 antes de virar expoente?
- Ficou claro que intensidades se somam e decibéis não?
- As respostas são 60 dB (exercício), 80 dB (Q5), 10 000 vezes (Q4) e 10 máquinas (Q9)?
```

---

## Vídeo 5: Revisão (Função logarítmica e escalas no ENEM)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula de REVISÃO para o YouTube sobre:

TEMA: Matemática — Funções — Função Logarítmica e aplicações (pH, Richter, decibéis) —
Episódio 5 de 5: Revisão geral, estratégia de prova, pegadinhas e treino para o ENEM
RECORTE: use as seções 01, 09, 10, 11 e 13 do material de apoio.
NÃO reutilize as Questões 1 a 9 da seção 12 (já resolvidas nos episódios anteriores).
Use SOMENTE as fórmulas do material (pH = −log[H⁺]; M = log(A/A₀); log E = 4,8 + 1,5M;
M_w = (2/3) · log M₀ − 10,7; β = 10 · log(I/I₀) com I₀ = 10⁻¹² W/m²).
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que assistiu aos episódios 1 a 4, mas ainda é iniciante e pode ter esquecido
partes. Relembre cada conceito em uma frase simples antes de cobrá-lo.

REGRAS DE EXPLICAÇÃO
1. Cada conceito é relembrado com a mesma analogia âncora usada no seu episódio:
   o espelho na reta y = x; o retorno decrescente; a porta do log fechada para o zero
   e os negativos; a régua de zeros; diferença de leitura como expoente da razão; o pH
   de cabeça para baixo; os dois placares do terremoto; a constante que se cancela;
   desfazer de fora para dentro; cada 10 dB um zero a mais; o fator 10 que come um
   zero; os copos de água no balde.
2. Prática de recuperação: antes de explicar, PERGUNTE e peça para o aluno pausar.
3. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
4. Uma ideia por cena. Frases curtas. Tom de conversa, falando com "você".

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Acidez, terremotos e barulho: três assuntos de três áreas
  diferentes, uma única regra matemática. Hoje você treina a regra que o ENEM mais
  cobra quando o assunto é logaritmo: 'quantas vezes maior'."
- O que a prova cobra (seção 01): comparar valores numa escala logarítmica (a pergunta
  campeã), calcular com a fórmula dada, ler o gráfico de uma função logarítmica e achar
  o domínio. O que rende mais: a diferença entre duas leituras é o expoente da razão
  (pH 3 × pH 6: 10³; nos decibéis, divida por 10 antes: 40 dB a mais dão 10⁴).
- Onde aparece nas outras áreas (seção 10): Química (pH de soluções, chuva ácida, solos;
  chuva com pH abaixo de 5,6 é considerada ácida), Física (nível sonoro e poluição
  sonora; a percepção de "volume" não é proporcional à intensidade), Geografia
  (terremotos e placas tectônicas; os danos dependem também da profundidade e das
  construções), Biologia (pH do sangue perto de 7,4; pequenas variações de pH são
  grandes variações de [H⁺]).
- A estratégia de prova em 3 hábitos (seção 09): "quantas vezes" pede razão (diferença
  das leituras ÷ coeficiente — 10 nos decibéis, 1,5 na energia, 1 no pH e na amplitude
  — e eleve 10); para calcular a leitura, isole o log e opere na ordem certa; confira o
  sentido (no pH, menor leitura é mais H⁺; nas outras, maior leitura é grandeza maior).
- "Verdadeiro ou falso? Pause e responda": transforme em afirmações os 9 erros da
  seção 11 (pH 2 e pH 5: 3 vezes mais ácido; +1 dB = intensidade ×10; 80 dB + 80 dB =
  160 dB; +2 graus: energia ×100; pH maior = mais ácido; log(2 · 10⁻⁵) = log 2 · (−5);
  domínio de log(2x − 6): x ≥ 3; log_0,5 x > 2 ⇒ x > 0,25; o logaritmo cresce cada vez
  mais rápido). Para cada um: pausa → resposta → por que a pegadinha engana → a regra
  certa em uma frase.
- 5 questões INÉDITAS no estilo ENEM, criadas por você, com situações hipotéticas e
  5 alternativas cada:
  1) domínio: para quais valores reais de x a função f(x) = log(x² − 16) está definida?
     Correta: x < −4 ou x > 4. Erradas: x > 4 (esqueceu o ramo negativo), x > 16
     (comparou x com 16), −4 < x < 4 (inverteu a região), x ≤ −4 ou x ≥ 4 (aceitou o
     zero dentro do log);
  2) comparar acidez: um refrigerante tem pH 2,5 e um iogurte, pH 4,5; a concentração de
     H⁺ no refrigerante, em relação à do iogurte, é. Correta: 100 vezes maior (10²).
     Erradas: 1,8 vez maior (dividiu os pHs), 2 vezes maior (parou na diferença),
     20 vezes maior (multiplicou a diferença por 10), 100 vezes menor (inverteu o
     sentido da escala);
  3) pH com coeficiente: uma amostra de água de chuva tem [H⁺] = 4 · 10⁻⁶ mol/L; use
     log 2 = 0,30. Correta: 5,4 (log 4 = 0,60; pH = 6 − 0,60; fica entre 5 e 6).
     Erradas: 5,7 (usou log 2 no lugar de log 4), 6,0 (ignorou o 4), 6,3 (somou log 2:
     sinal e coeficiente errados), 6,6 (somou log 4: erro de sinal). Comente: como
     5,4 < 5,6, essa chuva é considerada ácida;
  4) amplitude × energia: com M = log(A/A₀), um tremor de magnitude 4 e outro de
     magnitude 7; a amplitude registrada no segundo, em relação ao primeiro, é.
     Correta: 1 000 vezes maior (10³). Erradas: 1,75 vez (dividiu as magnitudes),
     3 vezes (parou na diferença), 30 vezes (multiplicou a diferença por 10), cerca de
     31 600 vezes (calculou a razão das ENERGIAS, 10^(1,5 · 3) = 10^4,5);
  5) calcular decibéis: num show, a intensidade sonora perto do palco é 10⁻¹ W/m²; com
     β = 10 · log(I/I₀) e I₀ = 10⁻¹² W/m², o nível é. Correta: 110 dB (10 · log 10¹¹).
     Erradas: −10 dB (não dividiu por I₀), 11 dB (esqueceu o fator 10), 120 dB (usou só
     o expoente de I₀), 130 dB (somou os expoentes em módulo, 1 + 12). Comente: bem
     acima dos 85 dB do limite trabalhista.
  As alternativas erradas devem ser exatamente os erros clássicos. Leia, peça a pausa,
  escreva a diferença das leituras antes de qualquer conta, resolva, confira o sentido
  e explique cada alternativa.
- Checklist de domínio (seção 13): leia os itens e diga "marque só o que você
  conseguiria explicar em voz alta para outra pessoa, sem consultar nada; o que não
  marcou, reveja o episódio correspondente" (lei, domínio, imagem, gráficos simétricos,
  pontos (1, 0) e (b, 1), sinal e inequações → episódio 1; diferença de leituras em
  razão, pH e comparação de acidez → episódio 2; amplitude × energia e fórmula de
  magnitude → episódio 3; decibéis e soma de fontes → episódio 4).
- Meta antes de considerar dominado: resolver 30 questões e acertar pelo menos 21
  (70%), com pelo menos dez de comparação em escala (pH, Richter, decibéis).
- Encerramento e ponte: "o próximo assunto é Função modular e funções definidas por
  partes: conta de água, estacionamento e imposto por faixas, regras que mudam de
  fórmula conforme o valor de entrada."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Use um cronômetro visual nas pausas; um selo "PEGADINHA" em amarelo nos erros; um
  ícone de área (gráfico, gota, sismógrafo, alto-falante) em cada questão inédita; os 4
  ícones dos episódios (espelho na reta y = x, régua de pH, dois placares, medidor de
  decibéis) como índice visual da revisão.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Cada conceito foi relembrado antes de ser cobrado?
- As 5 questões inéditas têm uma única alternativa correta e contas corretas
  (x < −4 ou x > 4; 100 vezes maior; 5,4; 1 000 vezes; 110 dB)?
- Nenhuma fórmula de Química, Física ou Geografia além das do material foi usada?
```

---

## Cuidados ao revisar os roteiros

- **Decibéis (vídeo 4 e inédita 5):** a diferença em dB é **dividida por 10** antes de virar expoente (40 dB a mais → 10⁴, não 10⁴⁰). Duas fontes iguais somam cerca de **3 dB** (80 → 83), não 80 nem 10. Na Q9, a resposta é **10** máquinas no total, não 11.
- **Amplitude × energia (vídeo 3 e inédita 4):** por grau, amplitude ×10 e energia ×10^1,5 ≈ 32. De 5 para 7: amplitude ×100, energia ×1 000. A IA costuma usar ×10 por grau também para a energia.
- **Sentido do pH (vídeo 2, Q6 e inédita 3):** menor pH é **mais** H⁺. Na piscina, a maior concentração é 10 elevado a **−7,2**. Em 4 · 10⁻⁶, o pH é 6 − 0,60 = **5,4** (entre 5 e 6), não 6,6.
- **Ordem das operações em M_w (vídeo 3, Q8):** (2/3) · 27 = 18 e **depois** − 10,7 = 7,3. A IA às vezes subtrai primeiro (10,9). E não deve inventar fórmulas de Química, Física ou sismologia além das do material (por exemplo, cálculos com pOH ou com energia em decibéis).
