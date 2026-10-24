# Progressão Geométrica (PG) e Soma dos Infinitos Termos — série de videoaulas

Material de apoio: `01-matematica/32-progressao-geometrica-soma-infinita.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| **Questão 1** (500 bactérias que dobram a cada 20 min, 2 h → 32 000) | Idêntica à **Questão 1 de Função Exponencial** | **Não uso.** O exemplo da seção 03 (os mesmos números) entra só como "você já viu isso na série de Função Exponencial", para mostrar a contagem a partir do instante zero. No lugar, uma questão nova de termo geral por dois termos (Vídeo 1). |
| **Questão 2** (80 g, meia-vida de 5 anos, 20 anos → 5 g) | Quase igual à **Questão 2 de Função Exponencial** (80 mg, meia-vida de 8 dias, 32 dias → 5 mg: mesmas 4 meias-vidas, mesmo resultado) | **Não uso.** Meia-vida vira revisão relâmpago no Vídeo 4, e entra uma questão nova de depreciação percentual. |
| Questão 9 (tabela 1 000, 1 200, 1 440, 1 728 → 1 000 · 1,2ⁿ) | Mesma estrutura da Questão 3 de Função Exponencial (tabela de valores com fator 0,8) | Uso (números, sentido e contexto diferentes), apresentada como "agora com o olhar de PG". |
| Montantes de juros compostos formam PG de razão 1 + i; dobra a cada 7 anos → ×2³ | **Juros Compostos**, seções 04 e 08 | "Você já viu isso disfarçado": revisão relâmpago no Vídeo 4. |
| Porcentagem vira fator (1 + i, 1 − i) | **Porcentagem** e **Função Exponencial** | Revisão relâmpago no Vídeo 1. |
| Dízima periódica e fração geratriz (regra prática dos noves) | **Frações, decimais e dízimas** (seção 09) | Só a justificativa nova: a dízima é uma soma infinita de PG. A regra prática não é reensinada. |
| PA (termo geral, n − 1, termos equidistantes) | **Progressão Aritmética** | Revisão relâmpago e comparação lado a lado. |
| Matrizes e operações | Próxima série | Só a ponte no fim da revisão. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. O que é PG, a razão como fator e o termo geral** | 02, 03, 04 | Q7, nova (algas), Q9 | 10–12 min |
| **2. Propriedades e soma finita** | 05, 06 | Q4, Q5 | 10–12 min |
| **3. Soma infinita: infinitas parcelas, um número finito** | 07, 08 (a bola) | Q8, Q6, Q3 | 10–12 min |
| **4. A PG disfarçada: juros compostos, meia-vida, depreciação** | 08 (tabela), 09 (estratégia 1) | nova (depreciação) | 6–8 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

As Questões 1 e 2 do material ficam de fora por duplicarem questões de Função Exponencial.

---

## Vídeo 1: O que é PG, a razão como fator e o termo geral

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Sequências — Progressão Geométrica — Episódio 1 de 5:
O que é PG, a razão como fator e o termo geral
RECORTE: use APENAS as seções 02, 03 e 04 do material de apoio, mais as Questões 7 e 9
da seção 12 e a questão nova escrita abaixo (ela NÃO está no material). NÃO use as
Questões 1 e 2 do material. Fator 1 + i (série de Porcentagem), função exponencial
(série de Função Exponencial) e termo geral da PA (série de Progressão Aritmética) já
foram ensinados: aqui, revisão rápida. O exemplo das 500 bactérias da seção 03 já foi
resolvido na série de Função Exponencial: cite-o como "você já viu isso", sem refazer
como questão.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma folha de papel dobrada ao meio várias
   vezes (2, 4, 8, 16 camadas) e pela população de uma cidade que cresce 5% ao ano. Só
   depois escreva a_n.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (progressão geométrica, razão q, quociente, PG crescente, decrescente,
   alternante e constante, fator, termo geral, termo zero).
3. Analogias âncora, retomadas ao longo da aula:
   - "a PG é uma máquina de multiplicar: cada termo passa pela mesma máquina ×q";
   - "do 1º ao n-ésimo termo, a máquina age n − 1 vezes; contando do instante zero, age
     t vezes";
   - "na PA a distância entre termos se divide; na PG se tira a raiz".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: potência como
   multiplicação repetida (2⁶ = 64; série de Potenciação), "crescer 5% é multiplicar por
   1,05" (série de Porcentagem) e o "n − 1" da PA (série de Progressão Aritmética).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; antes de qualquer
   potência, escreva na tela "fator = …" e "quantas vezes o fator age = …".
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Duas sequências começam no 2. Uma soma 6 a cada passo:
  2, 8, 14, 20, 26. A outra só dobra: 2, 4, 8, 16, 32. No 5º termo, quem dobra já passou
  na frente. E nunca mais é alcançada."
- Promessa: "ao final, você vai reconhecer uma PG, transformar porcentagem em razão e
  achar qualquer termo sem listar os anteriores".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) o que é PG: cada termo é o anterior vezes q; a tabela da seção 02 (q = 2;
     q = 1/2; q = −3, alternante; q = 1; q = 1,05);
  b) razão é quociente, não diferença: em (80, 40, 20), q = 40 ÷ 80 = 0,5, não −40;
  c) porcentagem vira razão: crescer i% → q = 1 + i; cair i% → q = 1 − i (5% ao ano →
     1,05; perder 15% → 0,85);
  d) termo geral a_n = a₁ · q^(n−1) e a versão a_n = a_k · q^(n−k);
  e) contar do instante zero: depois de t períodos, a₀ · q^t. "Você já viu isso na
     série de Função Exponencial: 500 bactérias que dobram a cada 20 min, em 2 h, são
     6 duplicações, 500 · 2⁶ = 32 000." Mostre que a_n com n − 1 e a₀ com t são a mesma
     conta, só mudando quem é o "primeiro";
  f) razão a partir de dois termos: a₂ = 6 e a₅ = 162 → q³ = 27 → q = 3;
  g) PG é exponencial nos naturais: PA (2, 8, 14, …) × PG (2, 4, 8, …), 32 contra 26 no
     5º termo e 64 contra 32 no 6º; o teste da tabela (quociente constante = PG;
     diferença constante = PA).
- Exercício "nós fazemos": peça "pause: um aplicativo tem 2 000 usuários e cresce 10% ao
  mês. Qual é a razão e quantos usuários terá daqui a 3 meses?" (q = 1,1;
  2 000 · 1,1³ = 2 000 · 1,331 = 2 662).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Na PG, o que se repete é a divisão de um termo pelo anterior."
  "Crescer i% é multiplicar por 1 + i."
  "O expoente é o número de vezes que o fator age."
- Erros clássicos:
  • a_n = a₁ · qⁿ (uma multiplicação a mais);
  • razão de (80, 40, 20) = −40;
  • "dobra 6 vezes" = 500 · 2 · 6 (produto pelo número de vezes, em vez de potência);
  • 5% ao ano com q = 0,05.
- Questões no estilo ENEM, nesta ordem:
  • Questão 7 do material (40 000 habitantes, 5% ao ano, 4 anos, 1,05⁴ ≈ 1,2155):
    "eu faço", mostrando que C (48 000) é o crescimento linear e E (168 000) multiplica
    por 1,05 e por 4;
  • Questão nova, "nós fazemos". Leia exatamente este texto:
    "Em um tanque de cultivo, a massa de algas é medida ao fim de cada semana, e os
    valores formam uma progressão geométrica. Ao fim da 2ª semana havia 6 g de algas
    e, ao fim da 5ª semana, 162 g. Mantido esse padrão, ao fim da 7ª semana a massa de
    algas será de
    A) 266 g  B) 486 g  C) 972 g  D) 1 458 g  E) 4 374 g"
    Resolução: da 2ª à 5ª semana o fator age 3 vezes: q³ = 162 ÷ 6 = 27, q = 3. Da 5ª
    à 7ª, mais 2 vezes: 162 · 3² = 162 · 9 = 1 458 g (D). A: trata como PA
    (3r = 156, r = 52; 162 + 2 · 52 = 266). B: multiplica uma vez só (é a 6ª semana).
    C: multiplica a razão pelo número de semanas, 162 · 3 · 2, em vez de elevar.
    E: multiplica três vezes (seria a 8ª semana);
  • Questão 9 do material (tabela de clientes 1 000, 1 200, 1 440, 1 728): "você faz",
    com pausa; divida cada valor pelo anterior (1,2 sempre) e teste as leis em n = 0,
    1 e 2 (a lei linear acerta n = 1 e erra n = 2: 1 400 ≠ 1 440).
  Em todas: leia o enunciado, escreva o fator e quantas vezes ele age, resolva e
  explique as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "uma mensagem vai para 3 pessoas no primeiro dia, e
  cada uma repassa para 3 novas no dia seguinte. Em 6 dias, quantas pessoas receberam
  ao todo? Não é 3⁶. Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: uma corrida entre a PA (2, 8, 14, …), andando em passos iguais
  sobre uma reta, e a PG (2, 4, 8, …), subindo por uma curva; um placar mostra 26 × 32
  no 5º termo e 32 × 64 no 6º.
- A "máquina ×q": cada termo entra numa caixa roxa "×3" e sai multiplicado, com um
  contador de quantas vezes a máquina agiu.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Em todo termo geral, o expoente é o número de vezes que o fator age (n − 1 a partir
  de a₁; t a partir de a₀)?
- As Questões 1 e 2 do material NÃO foram usadas como questões?
- A questão das algas dá 1 458 g (q = 3, duas multiplicações a partir da 5ª semana)?
```

---

## Vídeo 2: Propriedades e soma finita

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Sequências — Progressão Geométrica — Episódio 2 de 5:
Propriedades que poupam conta e a soma finita da PG
RECORTE: use APENAS as seções 05 e 06 do material de apoio, mais as Questões 4 e 5 da
seção 12. As propriedades da PA (média dos vizinhos, termos equidistantes, notação
x − r, x, x + r) já foram ensinadas na série de Progressão Aritmética: aqui, mostre a
versão multiplicativa ao lado. A equação do 2º grau usada na Questão 5 é da série de
Equação do 2º grau: relembre em uma frase. A soma infinita fica para o episódio 3.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pela corrente de mensagens no celular e pela lenda
   do tabuleiro de xadrez (1 grão, 2, 4, 8…). Só depois escreva S_n.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (média geométrica, notação simétrica, termos equidistantes, soma finita,
   S_n).
3. Analogias âncora, retomadas ao longo da aula:
   - "a PG é a PA com a soma trocada por multiplicação: média vira média geométrica,
     soma dos equidistantes vira produto";
   - "chame os três de x/q, x e x·q: no produto, o q se cancela e some";
   - "multiplicar a soma por q empurra todas as parcelas um degrau; subtraindo, sobra
     só a última menos a primeira".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: termo geral da PG
   (episódio 1), a notação x − r, x, x + r da PA (série de Progressão Aritmética) e a
   fórmula de Bhaskara (série de Equação do 2º grau).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; antes de somar,
   escreva "termo ou soma?" e liste os primeiros termos para conferir o resultado.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Um grão de trigo na primeira casa do xadrez, dois na segunda,
  quatro na terceira… Na 64ª casa, a soma passa de 18 quintilhões de grãos: centenas de
  vezes a produção mundial de trigo de um ano. E a fórmula que faz essa conta cabe numa
  linha."
- Promessa: "ao final, você vai somar qualquer PG finita e resolver problemas de três
  números em PG em poucas linhas".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) média geométrica dos vizinhos: b² = a · c; (4, x, 25) com termos positivos →
     x² = 100 → x = 10;
  b) notação simétrica x/q, x, x·q: produto x³; com produto 216, x = 6 na hora;
  c) equidistantes têm o mesmo produto: a₁ · a_n = a₂ · a_(n−1) (lado a lado com a soma
     da PA);
  d) a soma finita S_n = a₁ · (qⁿ − 1)/(q − 1), com q ≠ 1; de onde vem (multiplicar
     por q e subtrair); se q = 1, S_n = n · a₁;
  e) a corrente da seção 06: 3 · (3⁶ − 1)/2 = 3 · 728/2 = 1 092; só no 6º dia são
     729;
  f) o tabuleiro: 2⁶⁴ − 1 ≈ 1,8 · 10¹⁹ grãos.
- Exercício "nós fazemos": peça "pause: quanto dá 2 + 6 + 18 + … com 6 termos?"
  (q = 3; S₆ = 2 · (3⁶ − 1)/(3 − 1) = 2 · 728/2 = 728; confira somando: 2 + 6 + 18 +
  54 + 162 + 486 = 728).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Na PG, o termo do meio ao quadrado é o produto dos vizinhos."
  "Três em PG: x/q, x e x·q."
  "Soma finita: a₁ vezes (qⁿ − 1), dividido por (q − 1)."
- Erros clássicos:
  • total da corrente = 3⁶ (só o último dia);
  • esquecer de dividir por q − 1;
  • usar a fórmula da soma da PA numa PG.
- Questões no estilo ENEM, nesta ordem:
  • Questão 4 do material (corrente de mensagens, 6 dias): "eu faço", listando
    3, 9, 27, 81, 243, 729 e explicando cada errada (18 linear; 729 só o 6º dia;
    2 184 sem dividir por 2; 2 187 = 3⁷);
  • Questão 5 (idades em PG, produto 216 e soma 19): "você faz", com pausa:
    x = 6; 6/q + 6 + 6q = 19 → 6q² − 13q + 6 = 0 → q = 3/2 ou q = 2/3; crescente →
    q = 3/2; idades 4, 6 e 9; o mais velho tem 9 anos (C).
  Em todas: leia o enunciado, decida "termo ou soma?", resolva e explique as
  alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "pinte metade de um quadrado, depois metade do que
  sobrou, e assim para sempre. Infinitas pinceladas. A área pintada fica infinita?
  Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: a árvore da corrente de mensagens (3 → 9 → 27 …), com um
  contador "neste dia" e outro "ao todo"; no 6º dia, 729 × 1 092.
- A dedução da soma: duas linhas de parcelas (S e q·S) deslizando uma sobre a outra, as
  parcelas iguais se apagando e sobrando só a última e a primeira.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- A soma da corrente é 1 092 (e o 3⁶ = 729 foi identificado como só o último dia)?
- Na Questão 5, a notação é x/q, x, x·q e as idades 4, 6, 9 somam 19 e multiplicam 216?
- A fórmula da soma foi usada com q ≠ 1?
```

---

## Vídeo 3: Soma infinita (infinitas parcelas, um número finito)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Sequências — Progressão Geométrica — Episódio 3 de 5:
Soma infinita: infinitas parcelas, um número finito
RECORTE: use APENAS a seção 07 e, da seção 08, só a bola que quica e o quadro "Subidas
e descidas" do material de apoio, mais as Questões 8, 6 e 3 da seção 12. A regra
prática da fração geratriz já foi ensinada na série de Frações, decimais e dízimas: aqui,
só a justificativa pela soma infinita.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma barra de chocolate em que você come
   metade, depois metade do que sobrou, e assim por diante; e por uma bola de borracha
   solta de 8 m.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (soma infinita, somas parciais, convergir, limite, |q| < 1, dízima periódica,
   período).
3. Analogias âncora, retomadas ao longo da aula:
   - "metade do que sobrou: você nunca passa do chocolate inteiro, mas chega tão perto
     quanto quiser";
   - "a fórmula a₁/(1 − q) só funciona com freio: a razão entre −1 e 1";
   - "a bola cai uma vez de 8 m; depois disso, cada altura é percorrida duas vezes".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: a soma finita
   (episódio 2), 1 − 3/4 = 1/4 e dividir por uma fração (série de Frações), e a regra
   prática 0,2727… = 27/99 (série de Frações, decimais e dízimas).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; antes de usar a
   fórmula, escreva na tela "q = … está entre −1 e 1? ✓".
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Uma bola solta de 8 metros quica para sempre, cada vez a 3/4
  da altura anterior. Infinitos quiques. Quanto ela percorre ao todo? Exatamente
  56 metros. Nem um centímetro a mais."
- Promessa: "ao final, você vai somar infinitos termos, transformar dízimas em fração e
  resolver o problema da bola sem cair nos distratores".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) por que a soma pode ser finita: com |q| < 1, qⁿ fica perto de zero e some da
     fórmula da soma finita;
  b) a fórmula S∞ = a₁/(1 − q) e o que ela significa (o limite das somas parciais,
     nunca atingido com um número finito de parcelas);
  c) o quadrado pintado: 1/2 + 1/4 + 1/8 + … = (1/2)/(1 − 1/2) = 1;
  d) só vale com razão entre −1 e 1: com q = 2, a "fórmula" daria −1 para 1 + 2 + 4 + …,
     um absurdo;
  e) dízima como PG: 0,2727… = 0,27 + 0,0027 + … → a₁ = 0,27, q = 0,01 →
     0,27/0,99 = 27/99 = 3/11; "a regra dos noves que você aprendeu na série de
     Frações tem esta explicação";
  f) a bola: descidas 8 + 6 + 4,5 + … = 8/(1/4) = 32; subidas 6 + 4,5 + … = 6/(1/4) =
     24; total 56; a fórmula total = h + 2 · qh/(1 − q).
- Exercício "nós fazemos": peça "pause: quanto dá 9 + 3 + 1 + 1/3 + …?" (q = 1/3, entre
  −1 e 1; S = 9/(1 − 1/3) = 9/(2/3) = 13,5).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Com razão entre −1 e 1, a soma infinita é a₁ sobre (1 − q)."
  "Razão fora disso: a soma não para de crescer."
  "Bola: a primeira queda uma vez; o resto, duas."
- Erros clássicos:
  • S∞ = a₁/q (denominador errado);
  • somar a PG infinita com q = 2;
  • bola: total = 8/(1 − q), esquecendo as subidas;
  • 0,2727… = 27/100 (truncar a dízima).
- Questões no estilo ENEM, nesta ordem:
  • Questão 8 do material (logotipo fractal, 12 cm² e razão 1/4): "eu faço" (16 cm²),
    mostrando que B (15,75) soma só três etapas e E (48) divide pela razão;
  • Questão 6 (0,272727…): "nós fazemos", com a conferência 3 ÷ 11 = 0,2727…;
  • Questão 3 (a bola de 8 m, 3/4): "você faz", com pausa, separando descidas (32) e
    subidas (24).
  Em todas: leia o enunciado, procure "indefinidamente", "até parar" ou "para sempre",
  confira a razão, resolva e explique as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "juros compostos, remédio que cai à metade, carro que
  perde valor todo ano: você já esbarrou na PG em outras séries sem que ela dissesse o
  nome. Próximo episódio: a PG disfarçada."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: um quadrado de área 1 sendo pintado por metades sucessivas, com
  um contador de área pintada (0,5; 0,75; 0,875; …) que se aproxima de 1 sem passar.
- A bola quicando, com as descidas em azul e as subidas em verde empilhando-se em duas
  barras (32 m e 24 m) que se juntam em 56 m.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- A condição |q| < 1 foi conferida antes de cada soma infinita?
- A bola dá 56 m (32 de descidas + 24 de subidas), com a queda inicial contada uma vez?
- A dízima 0,2727… virou 27/99 = 3/11 (e não 27/100)?
```

---

## Vídeo 4: A PG disfarçada (juros compostos, meia-vida, depreciação)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Sequências — Progressão Geométrica — Episódio 4 de 5:
A PG disfarçada: juros compostos, meia-vida e depreciação
RECORTE: use APENAS a tabela e o exemplo de meia-vida da seção 08 e a estratégia 1 da
seção 09 do material de apoio, mais a questão nova escrita abaixo (ela NÃO está no
material). NÃO use a Questão 2 do material. Juros compostos (série de Juros Compostos)
e meia-vida (série de Função Exponencial) já foram ensinados: aqui, o tom é "você já viu
isso disfarçado"; revise em uma frase cada um, sem reensinar.
DURAÇÃO: 6 a 8 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por um extrato de poupança, a bula de um remédio
   ("meia-vida de 8 horas") e um anúncio de carro usado.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (juros compostos, montante, meia-vida, depreciação percentual, período).
3. Analogias âncora, retomadas ao longo da aula:
   - "a máquina ×q" (a mesma do episódio 1): juros compostos passam pela máquina
     ×(1 + i), a meia-vida pela ×1/2, a depreciação pela ×(1 − i);
   - "conte os períodos antes de qualquer conta: tempo total ÷ duração de um período";
   - "o fator é o que SOBRA: quem perde 20% fica com 80%".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: M = C(1 + i)^t (série
   de Juros Compostos), meia-vida (série de Função Exponencial) e o termo geral contado
   do instante zero, a₀ · q^t (episódio 1).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; converta tudo para a
   mesma unidade de tempo antes de dividir.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Você já estudou PG sem saber: na série de Juros Compostos, um
  saldo que dobra a cada 7 anos ficava 8 vezes maior em 21 anos, não 3. Hoje você vê a
  mesma máquina em remédios, populações e carros usados."
- Promessa: "ao final, você vai reconhecer a PG em qualquer enunciado de crescimento ou
  queda percentual e contar os períodos sem errar".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) a tabela da seção 08: juros compostos (q = 1 + i), meia-vida (q = 1/2 por
     meia-vida), crescimento populacional (q = 1 + i), depreciação percentual
     (q = 1 − i);
  b) meia-vida como revisão: 80 g com meia-vida de 5 anos, em 20 anos → 4 meias-vidas
     → 80 · (1/2)⁴ = 5 g ("é o mesmo raciocínio da série de Função Exponencial");
  c) contar períodos: "meia-vida de 8 h, em 2 dias" → 48 ÷ 8 = 6 meias-vidas; o
     expoente é quantas vezes o fator age;
  d) depreciação percentual × linear: perder 20% ao ano não é perder o mesmo valor
     todo ano (isso seria PA, da série de Função Afim);
  e) "termo, soma finita ou soma infinita?" (estratégia 2 da seção 09) como pergunta
     final de leitura.
- Exercício "nós fazemos": peça "pause: um carro de R$ 50.000,00 perde 10% do valor ao
  ano. Qual é a razão da PG e quanto ele vale em 2 anos?" (q = 0,9;
  50 000 · 0,81 = R$ 40.500,00).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Porcentagem fixa por período é PG."
  "Conte os períodos: tempo total dividido pela duração de um período."
  "O fator é o que sobra: perder 20% é multiplicar por 0,8."
- Erros clássicos:
  • usar a taxa no lugar do fator (q = 0,2 para "perde 20%");
  • tratar a queda percentual como linear (subtrair sempre o mesmo valor);
  • contar um período a mais ou a menos.
- Questões no estilo ENEM:
  • Questão nova, "você faz", com pausa. Leia exatamente este texto:
    "Um carro novo custa R$ 80.000,00 e, segundo uma projeção, perde 20% do seu valor a
    cada ano, sempre em relação ao valor do ano anterior. Três anos após a compra, o
    valor projetado do carro será de
    A) R$ 640,00  B) R$ 32.000,00  C) R$ 40.960,00  D) R$ 51.200,00
    E) R$ 64.000,00"
    Resolução: q = 1 − 0,20 = 0,8; três períodos a partir do instante zero:
    80 000 · 0,8³ = 80 000 · 0,512 = R$ 40.960,00 (C). Conferência ano a ano:
    80 000 → 64 000 → 51 200 → 40 960. A: usa a taxa como fator, 80 000 · 0,2³.
    B: depreciação linear, tirando R$ 16.000,00 todo ano. D: aplica o "n − 1" onde ele
    não cabe e para em 2 anos. E: aplica a queda uma vez só.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "no último episódio deste assunto, juntamos tudo,
  caçamos as pegadinhas e treinamos para o ENEM."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: três esteiras lado a lado passando pela "máquina ×q": um cofre
  (×1,05), um frasco de remédio (×1/2) e um carro (×0,8), cada uma com seu contador de
  períodos.
- A queda do carro ano a ano em barras (80 000, 64 000, 51 200, 40 960), com a reta da
  queda linear tracejada por cima para comparar.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Juros compostos e meia-vida foram citados como revisão, sem reensinar?
- A questão do carro dá R$ 40.960,00 (três períodos, fator 0,8)?
- O número de períodos foi calculado com as unidades convertidas?
```

---

## Vídeo 5: Revisão (Progressão geométrica no ENEM)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula de REVISÃO para o YouTube sobre:

TEMA: Matemática — Sequências — Progressão Geométrica — Episódio 5 de 5:
Revisão geral, estratégia de prova, pegadinhas e treino para o ENEM
RECORTE: use as seções 01, 09, 10, 11 e 13 do material de apoio.
NÃO reutilize as Questões 1 a 9 da seção 12 (as usadas já foram resolvidas nos
episódios anteriores; as Questões 1 e 2 também não devem aparecer, porque repetem
questões da série de Função Exponencial).
Matrizes terão série própria: aqui, só cite a ponte.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que assistiu aos episódios 1 a 4, mas ainda é iniciante e pode ter esquecido
partes. Relembre cada conceito em uma frase simples antes de cobrá-lo.

REGRAS DE EXPLICAÇÃO
1. Cada conceito é relembrado com a mesma analogia âncora usada no seu episódio:
   a máquina de multiplicar ×q; o expoente é quantas vezes o fator age; na PA divide,
   na PG tira a raiz; a PG como PA com a soma trocada por multiplicação; x/q, x, x·q;
   as parcelas que deslizam e se cancelam; metade do que sobrou; a fórmula com freio
   (|q| < 1); a bola que cai uma vez e depois faz tudo duas vezes; o fator é o que
   sobra.
2. Prática de recuperação: antes de explicar, PERGUNTE e peça para o aluno pausar.
3. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
4. Uma ideia por cena. Frases curtas. Tom de conversa, falando com "você".

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Bactérias, remédios, dinheiro, uma bola quicando: o ENEM usa a
  PG para tudo que cresce ou diminui por um fator fixo. Hoje você treina para
  reconhecer qual das três perguntas ele está fazendo: termo, soma ou soma infinita."
- O que a prova cobra (seção 01): crescimento por fator, decaimento, soma finita, soma
  infinita; e as duas habilidades que rendem mais: contar os períodos e reconhecer a
  soma infinita.
- Onde aparece nas outras áreas (seção 10): Química (radioatividade), Biologia (divisão
  celular, 2ⁿ; pirâmide de energia, razão aproximada 0,1), Matemática Financeira (juros
  compostos), Física (cada +10 dB multiplica a intensidade por 10: níveis em PA,
  intensidades em PG).
- A estratégia de prova em 3 hábitos (seção 09): contar os períodos com calma; decidir
  termo, soma finita ou soma infinita; usar as potências que o enunciado dá.
- "Verdadeiro ou falso? Pause e responda": transforme em afirmações os 9 erros da
  seção 11. Para cada um: pausa → resposta → por que a pegadinha engana →
  a regra certa em uma frase.
- 5 questões INÉDITAS no estilo ENEM, criadas por você, com situações hipotéticas e
  5 alternativas cada (use estes números e confira as contas):
  1) medicamento com 320 mg no sangue e meia-vida de 6 h; quanto resta após 1 dia:
     24 ÷ 6 = 4 meias-vidas → 320 · (1/2)⁴ = 20 mg (erradas: 10 mg, uma a mais; 40 mg,
     uma a menos; 80 mg, 320 ÷ 4; 160 mg, uma meia-vida só);
  2) soma finita: na 1ª semana, 2 pessoas entram num grupo; cada pessoa que entra
     convida 2 novas na semana seguinte; total ao fim da 5ª semana: 2 + 4 + 8 + 16 + 32
     = 2 · (2⁵ − 1)/(2 − 1) = 62 (erradas: 32, só a 5ª semana; 10, linear; 64, 2⁶;
     126, seis semanas);
  3) bola solta de 9 m que sobe a 2/3 da altura anterior: descidas 9/(1/3) = 27;
     subidas 6/(1/3) = 18; total 45 m (erradas: 27, só descidas; 18, só subidas;
     36, dobra as subidas e esquece a queda inicial; 54, dobra as descidas);
  4) tabela de valores 600, 540, 486, 437,4 nos anos 0, 1, 2, 3: quociente 0,9 →
     V = 600 · 0,9ⁿ (erradas: 600 − 60n, que dá 480 no ano 2; 600 · 0,1ⁿ; 600 · 0,9n,
     que dá 0 no ano 0; 540 · 0,9ⁿ, que começa no valor errado);
  5) dízima 0,363636… como soma infinita: a₁ = 0,36, q = 0,01 → 0,36/0,99 = 36/99 =
     4/11 (erradas: 36/100; 36/90 = 2/5; 36/999 = 4/111; 1/3, uma aproximação).
  As alternativas erradas devem ser exatamente os erros clássicos (período a mais ou a
  menos, só o último termo no lugar da soma, taxa no lugar do fator, esquecer as
  subidas, truncar a dízima). Leia, peça a pausa, escreva o fator e o número de
  períodos, resolva e explique cada alternativa.
- Checklist de domínio (seção 13): leia os itens e diga "marque só o que você
  conseguiria explicar em voz alta para outra pessoa, sem consultar nada; o que não
  marcou, reveja o episódio correspondente" (razão, fator 1 ± i, termo geral e tabela
  PA × PG: episódio 1; b² = ac, três termos e soma finita: episódio 2; soma infinita,
  dízimas e bola: episódio 3; meia-vida, juros e depreciação: episódio 4).
- Meta antes de considerar dominado: resolver 30 questões e acertar pelo menos 21
  (70%), com pelo menos oito de soma infinita ou de decaimento (meia-vida, quiques).
- Encerramento e ponte: "o próximo assunto é Matrizes e operações, que abre a parte de
  álgebra linear: tabelas de números com endereço, e uma multiplicação feita linha por
  coluna."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Use um cronômetro visual nas pausas; um selo "PEGADINHA" em amarelo nos erros; os
  4 ícones dos episódios (máquina ×q, árvore da corrente, bola quicando, carro com
  etiqueta de preço caindo) como índice visual da revisão.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Cada conceito foi relembrado antes de ser cobrado?
- As 5 questões inéditas têm uma única alternativa correta e contas corretas?
- Na questão 3, a queda inicial foi contada uma vez só (total 45 m)?
```

---

## Cuidados ao revisar os roteiros

- **n − 1 × instante zero:** "500 bactérias que dobram a cada 20 min, em 2 h" são **6** duplicações (500 · 2⁶), porque se conta a partir do instante zero. A IA às vezes aplica o "n − 1" da PA e usa 2⁵. A regra: o expoente é o número de vezes que o fator age.
- **Soma infinita só com |q| < 1:** confira que a IA não aplica a₁/(1 − q) a uma PG de razão maior que 1, e que o denominador é (1 − q), não q (12 ÷ 1/4 = 48 é o distrator da Questão 8).
- **Bola:** total = 8 + 2 · 24 = **56 m**. Erros típicos da IA: 64 (dobrar também a primeira queda) ou 32 (só descidas).
- **Questão 5:** com a notação x/q, x, x·q, a equação é 6q² − 13q + 6 = 0 (raízes 3/2 e 2/3). A IA às vezes escreve 6q + 6 + 6q = 19, que perde o termo 6/q.
