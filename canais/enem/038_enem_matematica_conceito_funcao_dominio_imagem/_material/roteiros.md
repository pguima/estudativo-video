# Conceito de Função, Domínio e Imagem — série de videoaulas

Material de apoio: `01-matematica/23-conceito-funcao-dominio-imagem.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Resolver equação e inequação do 1º grau, intervalos (]2, 5], colchete aberto no infinito), inverter o sinal ao dividir por negativo | **Equações e inequações do 1º grau** (série 20) | Revisão relâmpago: no "caminho de volta" (f(x) = k) e no domínio por fórmula (√(10 − 2x) exige inverter o sinal). Não reensino. |
| Plano cartesiano (eixos, par ordenado) | Série própria depois: **Plano cartesiano e distância entre pontos** (Geometria Analítica) | O material não cita o 56. No vídeo 4, apresento só o mínimo (eixo x horizontal, eixo y vertical, par (x, y)) em 30 s e prometo a série própria. |
| Funções definidas por partes ("hora ou fração") | Série própria depois: **Função modular e funções por partes** (29) | Aqui, só a ideia de "localizar a faixa" (vídeo 3). A Questão 5 do material 29 usa **a mesma tarifa** (R$ 10,00 + R$ 4,00 por hora ou fração) com outro tempo (4 h 20 min). Mantive a Q2 daqui porque esta série vem antes. A série 29 deve usar outra questão. |
| Táxi P(d) = 5 + 2,5d, gráfico que sobe e desce, h(t) = 20t − 5t² | Séries **Função afim** (24) e **Função quadrática** (25) | Uso esses exemplos só como "máquinas" e como leitura de gráfico. Coeficientes, vértice e raízes ficam para as séries próprias. |

## Plano: 6 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. A ideia de função: quando é e quando não é** | 02, 03 | Q6, Q1 | 8–10 min |
| **2. Domínio, contradomínio, imagem e a notação f(x)** | 04, 05 (até "f(a + b)") | Q4, Q7 | 10–12 min |
| **3. O caminho de volta e as funções por partes** | 05 ("O caminho de volta" e "Funções definidas por partes") | Q9, Q2 | 8–10 min |
| **4. O gráfico: teste da reta vertical e leitura de domínio e imagem** | 06, 07 | Q8 | 10–12 min |
| **5. Domínio pela fórmula e pelo contexto** | 08 | Q3, Q5 | 8–10 min |
| **6. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Vídeo 1: A ideia de função (quando é e quando não é)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Conceito de função, domínio e imagem — Episódio 1 de 6:
A ideia de função, quando é e quando não é
RECORTE: use APENAS as seções 02 e 03 do material de apoio, mais as Questões 6 e 1 da
seção 12. Domínio, imagem e a notação f(x) ficam para o episódio 2; o gráfico, para o
episódio 4. Este é o PRIMEIRO episódio do bloco de Funções: diga isso na abertura.
DURAÇÃO: 8 a 10 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pela bomba de combustível (você escolhe os litros,
   a bomba mostra o valor), pelo taxímetro e pela chamada da escola (cada número da
   lista corresponde a um aluno). Só depois apresente a definição.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (função, regra, entrada, saída, variável independente, variável dependente,
   lei da função, diagrama de flechas, conjunto de partida, conjunto de chegada).
3. Analogias âncora, retomadas ao longo da aula:
   - "função é uma máquina: entra um número, sai um número, e a mesma entrada dá SEMPRE
     a mesma saída";
   - "a data de nascimento: cada pessoa tem UMA só, mas muitas pessoas podem fazer
     aniversário no mesmo dia" (duas flechas chegando pode; duas saindo, não);
   - "a pergunta mágica: se eu souber ISTO, consigo dizer AQUILO sem dúvida?".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: o que é um conjunto
   (uma lista de elementos entre chaves) e substituir um número numa fórmula
   (série de Expressões algébricas).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; em cada exemplo,
   aponte na tela quem é a ENTRADA (x) e quem é a SAÍDA (y) antes de qualquer conta.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Abastecer 10 litros a R$ 6,00 o litro custa R$ 60,00. Sempre.
  Se a bomba às vezes cobrasse 60 e às vezes 70 pelos mesmos 10 litros, você brigaria
  com o frentista. Essa sua revolta tem nome em matemática: função."
- Promessa: "ao final, você vai saber dizer, olhando um texto, uma tabela ou um diagrama
  de flechas, se aquilo é ou não é uma função, e quem depende de quem".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) a máquina: a mesma entrada produz sempre a mesma saída; definição de f : A → B
     ("a cada x de A, um ÚNICO y de B");
  b) variável independente (você escolhe) e dependente (é calculada): a tabela da
     seção 02 (táxi P(d) = 5 + 2,5d; área A(ℓ) = ℓ²; combustível V(L) = 6L; bola
     h(t) = 20t − 5t²), só identificando entrada e saída, sem aprofundar as fórmulas;
  c) quem depende de quem: o lado determina a área, mas a altura não determina o aluno
     (dois alunos podem ter a mesma altura);
  d) o diagrama de flechas e as duas regras: todo elemento de A tem flecha saindo; de
     cada elemento de A sai UMA só flecha; em B não há exigência nenhuma;
  e) os três diagramas da seção 03: o primeiro é função; o segundo não (o 3 ficou sem
     flecha); o terceiro não (do 2 saem duas flechas);
  f) duas flechas chegando é permitido: em f(x) = x², 2 e −2 vão para 4;
  g) na tabela: o mesmo x não pode aparecer em duas linhas com y diferentes.
- Exercício "nós fazemos": peça "pause: a tabela x = 1 → y = 3; x = 2 → y = 5;
  x = 2 → y = 6; x = 3 → y = 7 representa uma função?" (não: o 2 tem duas saídas, 5 e 6).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Função: a cada entrada, uma única saída."
  "Duas flechas chegando pode; duas flechas saindo, não."
  "Todo elemento do conjunto de partida precisa de flecha."
- Erros clássicos:
  • achar que duas flechas chegando ao mesmo y impedem a função;
  • achar que tudo bem um elemento de A ficar sem flecha;
  • inverter quem depende de quem (dizer que o aluno é função da altura).
- Questões no estilo ENEM, nesta ordem:
  • Questão 6 do material (o aluno cuja altura é x): "eu faço", aplicando a pergunta
    mágica a cada alternativa;
  • Questão 1 (secretaria da escola: data de nascimento, disciplinas, lista de
    chamada): "você faz", com pausa.
  Em todas: leia o enunciado, identifique o conjunto de partida, diga "pause o vídeo e
  tente", resolva e explique as alternativas erradas (na Q1, B e D confundem flechas
  chegando com flechas saindo; E ignora os professores com duas disciplinas).
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "se a função f(x) = x² recebe só os números 1, 2 e 3 e
  pode devolver 1, 4, 7 ou 9, o 7 sai alguma vez? Quem nunca sai tem nome. Próximo
  episódio: domínio, contradomínio e imagem."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: uma máquina com funil de entrada e bandeja de saída; números
  entram, a máquina "processa" e devolve sempre o mesmo resultado para a mesma entrada
  (o 10 entra três vezes e sai 60 nas três).
- Os três diagramas de flechas da seção 03, com selo verde "é função" e selo vermelho
  "não é" apontando exatamente o defeito (o 3 sem flecha; o 2 com duas flechas).
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Ficou claro que duas flechas CHEGANDO é permitido e duas SAINDO é proibido?
- Em cada exemplo, a entrada e a saída foram apontadas antes da conta?
- Na Questão 1, a resposta é "I e III" (alternativa C)?
```

---

## Vídeo 2: Domínio, contradomínio, imagem e a notação f(x)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Conceito de função, domínio e imagem — Episódio 2 de 6:
Domínio, contradomínio, imagem e a notação f(x)
RECORTE: use APENAS a seção 04 e a primeira parte da seção 05 (a tabela de
substituições e o quadro "f(a + b) não é f(a) + f(b)") do material de apoio, mais as
Questões 4 e 7 da seção 12. O "caminho de volta" (f(x) = k) fica para o episódio 3; ler
domínio e imagem no gráfico, para o episódio 4.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma máquina de refrigerante que aceita só
   moedas de R$ 1, R$ 2 e R$ 5 (domínio) e tem no painel botões de vários sabores, mas
   alguns estão sempre esgotados (contradomínio × imagem).
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (domínio, contradomínio, imagem, pré-imagem, ⊂ "está contido em", valor
   numérico, f(x) "f de x").
3. Analogias âncora, retomadas ao longo da aula:
   - "domínio é o que PODE entrar; contradomínio é o cardápio; imagem é o que
     REALMENTE sai da cozinha" (a imagem é sempre parte do cardápio);
   - "o x é uma cadeira vazia: o que vier entre parênteses senta no lugar dele, e
     senta COM os parênteses";
   - "o f não é um número multiplicando o parêntese: é o nome da máquina" (por isso
     f(2x) não é 2·f(x)).
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: (−2)² = 4 e −2² = −4
   (série de Potenciação) e o quadrado da soma (x + 1)² = x² + 2x + 1 (série de
   Expressões algébricas e produtos notáveis).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; ao substituir,
   escreva SEMPRE os parênteses na tela antes de calcular: f(−2) = (−2)² − 1.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Com f(x) = x² − 1, quanto vale f(2 + 3)? Muita gente faz
  f(2) + f(3) = 3 + 8 = 11. A resposta é 24. Hoje você descobre por que essas duas
  contas dão resultados tão diferentes."
- Promessa: "ao final, você vai separar domínio, contradomínio e imagem sem confundir e
  calcular f de qualquer coisa: de um número negativo, de 2x, de x + 1".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) os três conjuntos de f : A → B: domínio D(f) = A, contradomínio CD(f) = B e
     imagem Im(f), com Im(f) ⊂ CD(f);
  b) o exemplo da seção 04: f(x) = x², A = {1, 2, 3}, B = {1, 4, 7, 9}; f(1) = 1,
     f(2) = 4, f(3) = 9; Im = {1, 4, 9}; o 7 está no cardápio, mas nunca sai;
  c) imagem e pré-imagem: "9 é a imagem de 3; 3 é a pré-imagem de 9";
  d) a notação f(x) e o valor numérico: a tabela da seção 05 (f(3) = 8; f(−2) = 3;
     f(2x) = 4x² − 1; f(x + 1) = x² + 2x);
  e) f(a + b) não é f(a) + f(b): f(5) = 24, mas f(2) + f(3) = 11; e f(2x) ≠ 2f(x).
- Exercício "nós fazemos": peça "pause: g(x) = 2x + 1, com domínio A = {0, 1, 2} e
  contradomínio B = {0, 1, 2, 3, 4, 5}. Qual é a imagem?" (g(0) = 1, g(1) = 3,
  g(2) = 5 → Im = {1, 3, 5}).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Domínio é o que entra; imagem é o que realmente sai."
  "A imagem é parte do contradomínio, não necessariamente ele todo."
  "Substitua o x pelo que estiver entre parênteses, com parênteses."
- Erros clássicos:
  • achar que imagem e contradomínio são a mesma coisa;
  • f(2x) = 2f(x);
  • f(a + b) = f(a) + f(b);
  • calcular −2² em vez de (−2)² ao substituir um número negativo.
- Questões no estilo ENEM, nesta ordem:
  • Questão 4 do material (g(x) = x² em A = {−2, −1, 0, 1, 2}): "eu faço", calculando
    as cinco imagens e lembrando que repetições não se escrevem duas vezes num
    conjunto; A é o contradomínio, C é o domínio, D esquece g(0) = 0, E calcula −2²;
  • Questão 7 (f(2x) com f(x) = x² − 1): "você faz", com pausa; mostre a conferência
    com x = 1 (f(2) = 3, e só a alternativa C dá 3).
  Em todas: leia o enunciado, diga "pause o vídeo e tente", resolva e explique as
  alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "até aqui, a questão dava a entrada e pedia a saída.
  E quando ela dá a SAÍDA, 'paguei R$ 30,00 no táxi', e pede quantos quilômetros eu
  andei? Próximo episódio: o caminho de volta."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: dois balões (A à esquerda, B à direita) com flechas de 1, 2 e 3
  indo para 1, 4 e 9; o 7 fica apagado, com a etiqueta "no cardápio, mas nunca sai";
  depois um terceiro balão menor, a imagem, "recortado" de dentro de B.
- A "cadeira vazia": o x some da fórmula e no lugar aparece um parêntese vazio, onde se
  encaixam (−2), (2x) e (x + 1).
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- f(−2) foi calculado como (−2)² − 1 = 3 (e não −5)?
- Ficou claro que a imagem pode ser MENOR que o contradomínio?
- Todas as contas de substituição estão corretas, incluindo f(x + 1) = x² + 2x?
```

---

## Vídeo 3: O caminho de volta e as funções por partes

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Conceito de função, domínio e imagem — Episódio 3 de 6:
O caminho de volta (f(x) = k) e as funções definidas por partes
RECORTE: use APENAS os trechos "O caminho de volta: f(x) = k" e "Funções definidas
por partes" da seção 05 do material de apoio, mais as Questões 9 e 2 da seção 12.
Resolver a equação do 1º grau já foi ensinado na série de Equações e inequações do
1º grau: aqui, revisão rápida. Funções por partes terão série própria (Função modular e
funções por partes): aqui, só a ideia de localizar a faixa.
DURAÇÃO: 8 a 10 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pelo recibo de um táxi (você sabe quanto pagou e
   quer descobrir quanto andou) e pela placa de um estacionamento ("1ª hora R$ 10,00;
   hora adicional ou fração R$ 4,00").
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (caminho de ida, caminho de volta, equação f(x) = k, função definida por
   partes, faixa, "hora ou fração").
3. Analogias âncora, retomadas ao longo da aula:
   - "caminho de ida: dão o x, você calcula f(x). Caminho de volta: dão o y, você monta
     a equação f(x) = k" (como ler um mapa de ida ou de volta);
   - "na função por partes, a regra muda conforme a faixa, como a tarifa de água: antes
     de calcular, descubra em que gaveta o x está";
   - "'ou fração' é o relógio do estacionamento: começou a hora, pagou a hora inteira".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: resolver 5 + 2,5d = 30
   tirando 5 dos dois lados e depois dividindo por 2,5 (série de Equações e inequações
   do 1º grau) e a notação f(x) (episódio 2).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; antes de cada conta,
   escreva na margem da tela "dão o x" ou "dão o y".
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "O táxi cobra P(d) = 5 + 2,5d. Você pagou R$ 30,00. Quem calcula
  P(30) acha R$ 80,00, o preço de uma corrida de 30 km, e marca a alternativa errada.
  A pergunta era outra: quantos quilômetros custam R$ 30,00?"
- Promessa: "ao final, você vai saber quando calcular f(x) e quando resolver f(x) = k, e
  vai calcular qualquer tarifa por faixa sem cair no 'ou fração'".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) ida × volta: P(10) = 5 + 25 = 30 (dão o x); 5 + 2,5d = 30 → d = 10 km (dão o y);
  b) por que P(30) = 80 responde a outra pergunta;
  c) funções definidas por partes: a regra muda conforme o intervalo do x;
  d) o estacionamento da seção 05: até 1 h, R$ 10,00; com 2 h 15 min, a 1ª hora, mais
     1 hora adicional completa, mais uma fração que conta como hora: 10 + 2 · 4 = 18;
  e) outras funções por partes do dia a dia: contas de água e energia por faixa,
     impostos por alíquota (só citar; série própria depois).
- Exercício "nós fazemos": peça "pause: uma academia cobra R$ 50,00 de matrícula mais
  R$ 80,00 por mês, C(m) = 50 + 80m. Uma pessoa pagou R$ 530,00 no total. Quantos meses
  ela frequentou?" (é caminho de volta: 80m = 480 → m = 6 meses).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Dão o x: calcule. Dão o y: resolva a equação."
  "Em função por partes, primeiro ache a faixa."
  "Hora ou fração: começou a hora, paga a hora."
- Erros clássicos:
  • calcular f(30) quando o enunciado dá f(x) = 30;
  • ignorar a fração de hora;
  • cobrar a fração proporcionalmente ao tempo quando a regra diz "ou fração";
  • cobrar a primeira hora como se fosse adicional.
- Questões no estilo ENEM, nesta ordem:
  • Questão 9 do material (táxi, pagou R$ 30,00): "eu faço"; explique que E calcula
    P(30) = 80, C divide 30 por 2,5 e esquece a parte fixa, D soma os 5 reais em vez de
    subtrair, A divide 30 pela tarifa fixa;
  • Questão 2 (estacionamento, 3 h 20 min): "você faz", com pausa. Depois da 1ª hora
    restam 2 h 20 min = 2 horas adicionais completas + 1 fração = 3 horas adicionais:
    10 + 3 · 4 = R$ 22,00. Explique as erradas: A (R$ 18,00) ignora a fração;
    B (R$ 18,80) lê 3 h 20 min como 3,2 h e cobra proporcionalmente; C (R$ 19,33) cobra
    proporcionalmente 2,33 h; E (R$ 26,00) cobra a 1ª hora também como adicional.
  Em todas: leia o enunciado, diga "pause o vídeo e tente", escreva "dão o x" ou "dão o
  y" na margem, resolva e confira substituindo.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "uma circunferência desenhada no papel é gráfico de
  função? Existe um teste de um segundo, feito com uma régua em pé. Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: a máquina do episódio 1 funcionando ao contrário: a saída R$ 30,00
  entra pela bandeja e a máquina "rebobina" até revelar a entrada 10 km.
- Uma linha do tempo do estacionamento dividida em blocos de 1 hora: a 1ª hora em azul
  (R$ 10,00) e cada hora adicional em roxo (R$ 4,00); o bloco que só começou acende
  inteiro, com o selo "fração = hora cheia".
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- A Questão 2 deu R$ 22,00 (3 horas adicionais), e não R$ 18,00 (que é o exemplo de
  2 h 15 min da seção 05)?
- Em cada questão ficou claro se o enunciado deu a entrada ou a saída?
- O exercício da academia dá 6 meses (80 · 6 + 50 = 530)?
```

---

## Vídeo 4: O gráfico (teste da reta vertical e leitura de domínio e imagem)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Conceito de função, domínio e imagem — Episódio 4 de 6:
O gráfico: teste da reta vertical e leitura de domínio, imagem e comportamento
RECORTE: use APENAS as seções 06 e 07 do material de apoio, mais a Questão 8 da
seção 12. O plano cartesiano terá série própria (Plano cartesiano e distância entre
pontos, em Geometria Analítica): aqui, apresente só o mínimo necessário em 30 s.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pelo gráfico de temperatura do aplicativo de
   previsão do tempo (horas embaixo, temperatura na lateral) e pergunte "qual foi a
   máxima do dia e a que horas ela aconteceu?".
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (plano cartesiano, eixo horizontal/eixo x, eixo vertical/eixo y, par
   ordenado, gráfico de uma função, projeção, intervalo [a, b], máximo, mínimo,
   crescente, decrescente, zero ou raiz).
3. Analogias âncora, retomadas ao longo da aula:
   - "o domínio é a SOMBRA da curva no chão (eixo x); a imagem é a sombra na PAREDE
     (eixo y)";
   - "o teste da régua em pé: passe uma régua vertical pelo gráfico; se em algum lugar
     ela tocar a curva duas vezes, aquele x teria duas saídas, e não é função";
   - "pergunta de 'quando' se responde no chão (x); pergunta de 'quanto' se responde
     na parede (y)".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: o par ordenado (x, y)
   (primeiro anda na horizontal, depois na vertical; série própria de Plano cartesiano
   depois) e a notação de intervalo [−1, 6] (colchete fechado: a ponta entra; série de
   Equações e inequações do 1º grau).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Leituras de gráfico sempre passo a passo, narrando o PORQUÊ: diga em voz alta em qual
   eixo você está olhando antes de dizer cada número.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Uma questão pergunta em que intervalo a função cresce. A curva
  sobe da altura 1 até a altura 4, e muita gente marca 'entre 1 e 4'. Errado: a resposta
  certa fala do x, e não da altura. Hoje você aprende a não cair nessa troca."
- Promessa: "ao final, você vai olhar um gráfico e dizer se ele é de uma função, qual é
  o domínio, qual é a imagem, onde está o máximo e onde a curva sobe ou desce".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) o gráfico de f é o conjunto dos pontos (x, f(x));
  b) o teste da reta vertical: a curva da esquerda passa, a circunferência da direita
     não (a mesma vertical corta duas vezes);
  c) horizontal pode cortar várias vezes: a parábola cortada duas vezes por uma
     horizontal continua sendo função (é o "duas flechas chegando" do episódio 1);
  d) domínio e imagem como sombras: no gráfico da seção 07, domínio [−1, 6] e imagem
     [1, 4]; a imagem vai do ponto mais baixo ao mais alto, que não precisam estar nas
     pontas;
  e) a tabela de leitura da seção 07: máximo 4 em x = 2; mínimo 1 em x = −1; cresce em
     [−1, 2], decresce em [2, 6]; não há zeros (a curva fica toda acima do eixo x);
     f(4) = 3 (suba de x = 4 até a curva e leia a altura);
  f) intervalos de crescimento se dão em x.
- Exercício "nós fazemos": peça "pause: o gráfico de uma função é formado por dois
  segmentos, de (0, 2) a (3, 5) e de (3, 5) a (6, −1), com as pontas incluídas. Qual é o
  domínio e qual é a imagem?" (domínio [0, 6]; imagem [−1, 5]: o mais baixo é −1, na
  ponta direita, e o mais alto é 5, no meio).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Régua em pé tocando duas vezes: não é função."
  "Domínio é a sombra no chão; imagem é a sombra na parede."
  "Cresce e decresce se responde em x."
- Erros clássicos:
  • ler a imagem no eixo x;
  • achar que a imagem vai de uma ponta à outra do gráfico (o máximo pode estar no
    meio);
  • responder o intervalo de crescimento com valores de y;
  • achar que uma reta horizontal cortando duas vezes desqualifica a função.
- Questões no estilo ENEM, nesta ordem:
  • o gráfico da seção 07: "eu faço", lendo domínio, imagem, máximo, mínimo e
    crescimento;
  • o exercício dos dois segmentos: "nós fazemos" (acima);
  • Questão 8 do material (segmentos de (−2, 1) a (1, 4) e de (1, 4) a (5, 0)): "você
    faz", com pausa. Imagem [0, 4]. Explique as erradas: A é o domínio [−2, 5]; B
    considera só o primeiro segmento; C e D misturam valores de x e de y.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "e quando não há gráfico, só a fórmula? Em
  f(x) = 1/(x − 3), por que o 3 não pode entrar? E numa caixa de papelão, por que o x não
  pode passar de 10 cm? Próximo episódio: domínio pela fórmula e pelo contexto."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: uma lanterna acima da curva projeta a sombra no eixo x (faixa azul
  de −1 a 6, "domínio"); depois uma lanterna à direita projeta a sombra no eixo y (faixa
  verde de 1 a 4, "imagem").
- Uma régua vertical deslizando da esquerda para a direita sobre a curva e sobre a
  circunferência; na circunferência, os dois pontos de contato piscam em vermelho.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- A imagem da Questão 8 é [0, 4] (o ponto mais baixo é (5, 0), não (−2, 1))?
- Os intervalos de crescimento foram dados em x?
- O par ordenado foi explicado sem transformar a aula numa aula de Geometria Analítica?
```

---

## Vídeo 5: Domínio pela fórmula e pelo contexto

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Conceito de função, domínio e imagem — Episódio 5 de 6:
Domínio pela fórmula e pelo contexto
RECORTE: use APENAS a seção 08 do material de apoio, mais as Questões 3 e 5 da
seção 12. Resolver inequações do 1º grau (inclusive inverter o sinal ao dividir por
negativo) já foi ensinado na série de Equações e inequações do 1º grau: aqui, revisão
rápida.
DURAÇÃO: 8 a 10 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pela planilha que mostra "#DIV/0!" quando se
   divide por zero e pela calculadora que dá "erro" na raiz de um número negativo; depois,
   uma folha de papelão sendo recortada para virar caixa.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (domínio de uma fórmula, denominador, radicando, raiz quadrada, ℝ,
   restrição, contexto, número natural, ponto isolado).
3. Analogias âncora, retomadas ao longo da aula:
   - "as duas proibições da calculadora: dividir por zero e tirar raiz quadrada de
     número negativo";
   - "o domínio é o porteiro: só deixa entrar o x com o qual a conta existe E que faz
     sentido no problema";
   - "a corrente arrebenta no elo mais fraco: com várias condições, vale a mais
     restritiva".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: resolver inequação do
   1º grau e inverter o sinal ao dividir por negativo (série de Equações e inequações do
   1º grau) e o que é domínio (episódio 2).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; teste SEMPRE os
   extremos substituindo na fórmula (x = 2 em √(x − 2) dá √0 = 0: pode).
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "De uma folha de 30 cm por 20 cm, você recorta quadradinhos nos
  cantos para montar uma caixa. A fórmula do volume aceita x = 12 cm. A folha, não: com
  12 cm, um dos lados some antes. Hoje você aprende a ouvir as duas, a fórmula e o
  problema."
- Promessa: "ao final, você vai achar o domínio de fórmulas com fração e raiz e cortar o
  domínio pelo contexto: medidas positivas, contagens inteiras, tempo não negativo".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) domínio pela fórmula: o maior conjunto de números reais com o qual a conta existe;
  b) restrição 1, denominador ≠ 0: f(x) = 1/(x − 3) → x ≠ 3;
  c) restrição 2, radicando ≥ 0: g(x) = √(x − 2) → x ≥ 2;
  d) as duas juntas: h(x) = 5/√x → x > 0 (raiz exige x ≥ 0 e denominador exige x ≠ 0);
     sem restrição: p(x) = 3x² − x + 7 → ℝ;
  e) domínio pelo contexto: contagens (só naturais; gráfico de pontos isolados), tempo e
     distância (não negativos, às vezes limitados), medidas (positivas);
  f) a caixa: 20 − 2x > 0 dá x < 10 e vence 30 − 2x > 0 (x < 15): vale a mais forte.
- Exercício "nós fazemos": peça "pause: qual é o domínio de g(x) = √(10 − 2x)?"
  (10 − 2x ≥ 0 → −2x ≥ −10 → x ≤ 5: dividiu por −2, o sinal inverteu; confira: x = 5 dá
  √0 = 0, x = 6 dá √(−2), proibido).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Denominador não pode ser zero; raiz quadrada não aceita negativo."
  "O contexto corta ainda mais: medida positiva, contagem inteira."
  "Com várias condições, vale a mais restritiva."
- Erros clássicos:
  • esquecer o contexto (a fórmula aceita valores que o problema não aceita);
  • excluir à toa um extremo que funciona (o 2 em √(x − 2));
  • usar só uma das condições quando há duas;
  • desenhar linha contínua num problema de contagem.
- Questões no estilo ENEM, nesta ordem:
  • Questão 3 do material (planilha com √(x − 2)/(x − 5)): "eu faço"; resposta
    x ≥ 2 e x ≠ 5. Explique: C exclui o 2 à toa (√0/−3 = 0, sem erro); A esquece o
    denominador; B esquece a raiz; E exclui o trecho entre 2 e 5, onde a conta funciona
    (x = 3 dá √1/−2);
  • Questão 5 (caixa de 30 cm por 20 cm): "você faz", com pausa; resposta 0 < x < 10.
    Explique: A usa só o lado de 30 cm; D esquece que se recorta x dos dois lados; C
    ignora o tamanho da folha; E é o trecho em que 20 − 2x é negativo.
  Em todas: leia o enunciado, diga "pause o vídeo e tente", teste os extremos e explique
  as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "no último episódio deste assunto, juntamos tudo, vemos
  como funções aparecem em Física, Química, Biologia e Geografia e caçamos as
  pegadinhas."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: a folha de 30 cm × 20 cm com quadradinhos de lado x crescendo nos
  cantos; quando x chega a 10 cm, o lado de 20 cm desaparece (selo vermelho "a caixa não
  existe"), enquanto o lado de 30 cm ainda sobra.
- Uma reta numérica com o porteiro: bolinha fechada em 2, bolinha aberta (furo) em 5.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- No exercício √(10 − 2x), o sinal foi invertido ao dividir por −2 (x ≤ 5)?
- Ficou claro por que o 2 entra e o 5 não entra na Questão 3?
- A condição mais restritiva da caixa (x < 10) foi justificada com o lado de 20 cm?
```

---

## Vídeo 6: Revisão (Conceito de função no ENEM)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula de REVISÃO para o YouTube sobre:

TEMA: Matemática — Funções — Conceito de função, domínio e imagem — Episódio 6 de 6:
Revisão geral, estratégia de prova, pegadinhas e treino para o ENEM
RECORTE: use as seções 01, 09, 10, 11 e 13 do material de apoio.
NÃO reutilize as Questões 1 a 9 da seção 12 (já resolvidas nos episódios anteriores).
Função afim, quadrática e exponencial terão séries próprias: aqui, só cite a ponte.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que assistiu aos episódios 1 a 5, mas ainda é iniciante e pode ter esquecido
partes. Relembre cada conceito em uma frase simples antes de cobrá-lo.

REGRAS DE EXPLICAÇÃO
1. Cada conceito é relembrado com a mesma analogia âncora usada no seu episódio:
   a máquina (mesma entrada, mesma saída); a data de nascimento (duas flechas chegando
   pode, duas saindo não); o cardápio × o que sai da cozinha (contradomínio × imagem);
   a cadeira vazia do x; o caminho de ida e o de volta; a gaveta da função por partes;
   a régua em pé; a sombra no chão e na parede; o porteiro do domínio.
2. Prática de recuperação: antes de explicar, PERGUNTE e peça para o aluno pausar.
3. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
4. Uma ideia por cena. Frases curtas. Tom de conversa, falando com "você".

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Função é a habilidade de Matemática que mais aparece FORA da
  Matemática: todo gráfico de Física, Química, Biologia e Geografia é uma função. Quem
  domina este assunto ganha pontos em quatro provas."
- O que a prova cobra (seção 01): calcular valores, fazer o caminho de volta, ler
  gráficos, decidir o domínio e reconhecer funções; e o que mais rende: separar entrada
  (x, eixo horizontal, domínio) de saída (y, eixo vertical, imagem).
- Onde aparece nas outras áreas (seção 10): Física (um gráfico v × t não mostra onde o
  móvel está), Química (curva de solubilidade: cada temperatura, uma solubilidade),
  Biologia (o ponto máximo é o "ótimo"), Geografia (climogramas e séries históricas:
  não extrapole para fora do período mostrado).
- A estratégia de prova em 4 hábitos (seção 09): identificar os eixos e as unidades
  antes de tudo; perguntar "dão o x ou o y?"; em função por partes, localizar a faixa;
  para domínio, testar os extremos das alternativas.
- "Verdadeiro ou falso? Pause e responda": transforme em afirmações os 9 erros da
  seção 11 (duas flechas chegando; elemento sem flecha; imagem = contradomínio;
  f(2x) = 2f(x); f(a + b) = f(a) + f(b); f(30) quando f(x) = 30; imagem no eixo x;
  imagem = valores das pontas; esquecer o contexto). Para cada um: pausa → resposta →
  por que a pegadinha engana → a regra certa em uma frase.
- 5 questões INÉDITAS no estilo ENEM, criadas por você, com situações hipotéticas e
  5 alternativas cada:
  1) reconhecer função numa tabela ou em situações do cotidiano (com uma alternativa que
     confunde "várias entradas com a mesma saída" com "uma entrada com duas saídas");
  2) imagem e máximo lidos num gráfico de outra área (por exemplo, temperatura ao longo
     de um dia), com o máximo no meio do gráfico e não na ponta;
  3) o caminho de volta numa tarifa "fixo + por unidade" (com uma alternativa que é
     f(k) em vez da solução de f(x) = k);
  4) uma função por partes (tarifa por faixa ou "hora ou fração");
  5) domínio pelo contexto (medida que precisa ser positiva ou contagem inteira).
  As alternativas erradas devem ser exatamente os erros clássicos (domínio no lugar da
  imagem, contradomínio no lugar da imagem, f(k) no lugar de x, ignorar a fração,
  esquecer uma condição do domínio). Leia, peça a pausa, diga "dão o x ou o y?",
  resolva, confira e explique cada alternativa.
- Checklist de domínio (seção 13): leia os itens e diga "marque só o que você
  conseguiria explicar em voz alta para outra pessoa, sem consultar nada; o que não
  marcou, reveja o episódio correspondente" (definição e flechas: episódio 1; domínio,
  imagem e f(x): episódio 2; f(x) = k e por partes: episódio 3; gráfico: episódio 4;
  domínio por fórmula e contexto: episódio 5).
- Meta antes de considerar dominado: resolver 30 questões e acertar pelo menos 21
  (70%), com pelo menos dez de leitura de gráficos de outras áreas (Física, Química,
  Geografia).
- Encerramento e ponte: "o próximo assunto é Função afim: gráfico, coeficientes e
  aplicações, a primeira família de funções do bloco. Aquele táxi P(d) = 5 + 2,5d vai
  ganhar nome e sobrenome."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Use um cronômetro visual nas pausas; um selo "PEGADINHA" em amarelo nos erros; um
  ícone da área (termômetro, tubo de ensaio, folha, mapa) em cada gráfico de outra área;
  os 5 ícones dos episódios (máquina, cardápio, máquina ao contrário, régua em pé,
  porteiro) como índice visual da revisão.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Cada conceito foi relembrado antes de ser cobrado?
- As 5 questões inéditas têm uma única alternativa correta e contas corretas?
- Na questão de função por partes, a regra "ou fração" (ou a faixa) foi aplicada
  corretamente?
```

---

## Cuidados ao revisar os roteiros

- **Números negativos (vídeo 2):** f(−2) com f(x) = x² − 1 é (−2)² − 1 = **3**. A IA às vezes escreve −2² − 1 = −5. A mesma confusão estraga a Q4: g(−2) = (−2)² = 4, não −4.
- **Estacionamento (vídeo 3):** o exemplo da seção 05 (2 h 15 min) dá **R$ 18,00** e a Q2 (3 h 20 min) dá **R$ 22,00**. Com os dois números tão parecidos, a IA pode trocar um pelo outro ou contar só 2 horas adicionais na Q2.
- **Imagem × domínio no gráfico (vídeo 4):** no gráfico da seção 07 a imagem é [1, 4]. Na Q8 é **[0, 4]**: o ponto mais baixo é (5, 0), na ponta, e não (−2, 1). A IA tende a repetir o [1, 4] da seção.
- **Extremo que entra (vídeo 5):** na Q3, x = 2 **pertence** ao domínio (√0 = 0 não dá erro). A resposta é x ≥ 2 e x ≠ 5. Se a IA "arredondar" para x > 2, ela valida o distrator C.
