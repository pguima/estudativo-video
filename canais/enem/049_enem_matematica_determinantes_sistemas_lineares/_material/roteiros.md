# Determinantes e Sistemas Lineares — série de videoaulas

Material de apoio: `01-matematica/34-determinantes-sistemas-lineares.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Montar e resolver sistemas (substituição, adição), SPD/SPI/SI como retas concorrentes, paralelas e coincidentes, 0 = 0 e 0 = 2, razões entre coeficientes | **Sistemas de equações lineares** (série 22) | Revisão relâmpago de 30 s no vídeo 4. O que é novo é decidir pelo **determinante** (D ≠ 0, D = 0 e D_x ≠ 0), discutir com parâmetro e o sistema homogêneo. |
| **Questão 1** (teatro, inteiras a R$ 40 e meias a R$ 20) | Quase igual à **Questão 1 de Sistemas** (mesmo contexto e mesmos preços, só mudam os totais) | **Não uso como questão.** Os números dela (250 ingressos, R$ 7 400) aparecem só como exemplo de Cramer, que é o da seção 07. No lugar, uma questão nova (camisetas e bonés), com o texto completo no prompt do vídeo 3. |
| **Questão 5** (posição de duas retas, mesmo enunciado e alternativas) | Quase igual à **Questão 6 de Sistemas** (x + 2y = 4 e 2x + 4y = 10, que a série 22 usa como "eu faço") | **Não uso.** A leitura geométrica fica como revisão no vídeo 4, com o foco no critério D = 0 (D_x ≠ 0 → SI), e uma das questões inéditas da revisão cobra o caso de infinitas soluções pelo D. |
| Combinado com o roteiro já escrito da série 22 | `22-sistemas-equacoes-lineares.md` usa a Q1 e a Q6 do material 22 sem determinante | Aqui o novo é só determinante, Cramer, discussão com parâmetro, sistema homogêneo e escalonamento 3 × 3 no caso D = 0; razões entre coeficientes e retas são revisão relâmpago. |
| Inversa 2 × 2 com ad − bc; a_ij = 2i − j | **Matrizes e operações**, vídeos 4 e 1 | Ponte: "o número da inversa ganha nome". A Questão 8 retoma a lei de formação. |
| Bhaskara (x² + x − 6 = 0) e k² = 4 com duas raízes | **Equação do 2º grau e Bhaskara** | Revisão relâmpago. |
| A seção 09 usa como exemplo o mesmo sistema da Questão 4; a seção 02 usa a mesma equação da Questão 2 | (dentro do material) | Nos blocos uso exemplos novos, para que as questões não fiquem "já resolvidas". |
| Área de triângulo por determinante | Geometria Analítica (série própria mais adiante) | Só citada. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. O que é o determinante: 2 × 2, Sarrus, Laplace e o teste da inversa** | 02, 03, 05 | Q2 | 10–12 min |
| **2. Propriedades que poupam conta** | 04 | Q8, Q3 | 6–8 min |
| **3. O sistema como A · X = B e a regra de Cramer** | 06, 07 | Questão nova (camisetas e bonés), Q6 | 8–10 min |
| **4. Uma, infinitas ou nenhuma: classificar e discutir pelo determinante** | 08, 09 | Q4, Q7, Q9 | 10–12 min |
| **5. Revisão** | 01, 10, 11, 13 | 5 inéditas | 10–12 min |

Q1 e Q5 foram descartadas por duplicação com a série de Sistemas (ver tabela acima).

---

## Vídeo 1: O que é o determinante (2 × 2, Sarrus, Laplace e o teste da inversa)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Álgebra — Determinantes e Sistemas Lineares — Episódio 1 de 5:
O que é o determinante: 2 × 2, Sarrus, Laplace e o teste da inversa
RECORTE: use APENAS as seções 02, 03 e 05 do material de apoio, mais a Questão 2 da
seção 12. A inversa 2 × 2 e o número ad − bc já foram vistos na série de Matrizes e
operações: aqui, esse número ganha nome. As propriedades ficam para o episódio 2.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pela chave de um sistema de criptografia (da série
   de Matrizes) que às vezes "não abre": um único número diz se ela serve ou não.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (determinante, ordem, diagonal principal, diagonal secundária, regra de
   Sarrus, desenvolvimento de Laplace, cofator ou "determinante que sobra", matriz
   inversível, matriz singular).
3. Analogias âncora, retomadas ao longo da aula:
   - "o determinante é o teste da chave: diferente de zero, a matriz tem inversa (a
     chave abre); igual a zero, não tem";
   - "o produto da secundária entra 'de casaco': entre parênteses, com o sinal dele, e
     só depois é subtraído";
   - "Sarrus é o time verde contra o time vermelho: as três diagonais que descem para a
     direita somam; as três que descem para a esquerda somam; no fim, verde menos
     vermelho, em bloco".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: regra de sinais na
   multiplicação; a fórmula da inversa 2 × 2 que divide por ad − bc (série de Matrizes
   e operações); soma e produto ou Bhaskara para x² + x − 6 = 0 (série de Equação do 2º
   grau e Bhaskara).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; escreva cada produto
   COMPLETO, com sinal e parênteses, antes de somar ou subtrair.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Determinante de 3, −2, 4 e 5. Metade da turma escreve
  15 − 8 = 7. A resposta é 23. E é esse número que diz se uma matriz tem inversa."
- Promessa: "ao final, você vai calcular determinantes 2 × 2 e 3 × 3 sem errar sinal e
  vai saber, só por ele, se uma matriz tem inversa".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) só matrizes quadradas têm determinante; ordem 1: det[−7] = −7;
  b) ordem 2: ad − bc; o exemplo do material: 3 · 5 − (−2) · 4 = 15 + 8 = 23;
  c) determinante numa equação (exemplo novo, não o da seção 02): o determinante de
     (x 4 / 1 x − 3) é x(x − 3) − 4; igualando a zero, x² − 3x − 4 = 0, raízes 4 e −1;
  d) Sarrus na matriz do material (2 1 3 / 0 4 1 / 5 2 1): repita as duas primeiras
     colunas; verdes 2·4·1 = 8, 1·1·5 = 5, 3·0·2 = 0 (soma 13); vermelhas 3·4·5 = 60,
     2·1·2 = 4, 1·0·1 = 0 (soma 64); det = 13 − 64 = −51; Sarrus só vale para 3 × 3;
  e) Laplace como atalho: cada elemento de uma linha vezes o determinante que sobra ao
     riscar sua linha e sua coluna, com o padrão de sinais + − +; na mesma matriz, pela
     1ª linha: 2·(4 − 2) − 1·(0 − 5) + 3·(0 − 20) = 4 + 5 − 60 = −51; compensa mais
     quando a linha escolhida tem zeros;
  f) o teste da inversa: A tem inversa se, e somente se, det A ≠ 0; det = 0 → matriz
     singular; por isso a fórmula da inversa da série de Matrizes divide por ad − bc;
     det(A⁻¹) = 1 ÷ det A (det A = 4 → det A⁻¹ = 0,25); para achar os x que tornam a
     matriz não inversível, resolva det = 0.
- Exercício "nós fazemos": peça "pause: calcule o determinante de (−2 3 / 4 −5) e o de
  (1 2 0 / 0 1 3 / 2 0 1)" ((−2)(−5) − 3·4 = 10 − 12 = −2; Sarrus: verdes 1 + 12 + 0 =
  13, vermelhas 0 + 0 + 0 = 0, det = 13).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Ordem 2: principal menos secundária, com o sinal dentro do produto."
  "Sarrus: some cada time e subtraia o bloco vermelho inteiro."
  "Determinante zero: a matriz não tem inversa."
- Erros clássicos:
  • escrever 15 − 8 em vez de 15 − (−8);
  • em Sarrus, subtrair só o primeiro produto vermelho;
  • tentar usar Sarrus numa 4 × 4.
- Questão no estilo ENEM: Questão 2 do material (valores de x que tornam a matriz-chave
  inadequada): "você faz", com pausa, depois do exemplo do bloco c; resposta −3 e 2;
  explique que a A esquece o produto da secundária, a B troca os sinais das raízes, a C
  soma o 6 e a E para numa raiz só.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "precisa mesmo fazer Sarrus em (1 0 −1 / 3 2 1 /
  5 4 3)? Dá para ver que o resultado é zero sem conta nenhuma. Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: a matriz 3 × 3 ganhando as duas colunas repetidas à direita; três
  setas verdes descendo para a direita e três vermelhas descendo para a esquerda, cada
  uma soltando o seu produto num placar "verde 13 × vermelho 64".
- O produto da secundária "vestindo um casaco" (parênteses) antes de entrar na subtração.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- O determinante de (3 −2 / 4 5) deu 23 e o de (2 1 3 / 0 4 1 / 5 2 1) deu −51 pelos dois
  caminhos?
- No bloco c, as raízes de x² − 3x − 4 = 0 são 4 e −1?
- Na Questão 2, a resposta é −3 e 2?
```

---

## Vídeo 2: Propriedades que poupam conta

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Álgebra — Determinantes e Sistemas Lineares — Episódio 2 de 5:
Propriedades que poupam conta
RECORTE: use APENAS a seção 04 do material de apoio, mais as Questões 8 e 3 da seção 12.
A lei de formação a_ij = 2i − j já apareceu na série de Matrizes e operações: aqui, só
relembre como montar.
DURAÇÃO: 6 a 8 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma planilha em que uma linha é cópia da outra
   ("informação repetida não acrescenta nada") e por um aparelho de som com vários
   botões de volume.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (linhas proporcionais, combinação de linhas, matriz triangular, matriz
   diagonal, transposta, ordem n).
3. Analogias âncora, retomadas ao longo da aula:
   - "linhas 'parentes' (iguais, proporcionais ou uma feita das outras) zeram o
     determinante: é informação repetida";
   - "cada linha é um botão de volume: multiplicar UMA linha por k multiplica o det por
     k; multiplicar a matriz INTEIRA aperta os n botões, e o det vai a k^n";
   - "trocar duas linhas de lugar é como virar no espelho: o valor fica, o sinal troca".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: Sarrus (episódio 1);
   montar a matriz pela lei de formação (série de Matrizes e operações); potência
   (2³ = 8).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; antes de qualquer
   Sarrus, pergunte em voz alta: "tem alguma propriedade aqui?".
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Uma matriz 3 × 3 tem determinante 5. Dobre todos os números
  dela. O novo determinante é 10? Não: é 40."
- Promessa: "ao final, você vai reconhecer em segundos quando o determinante é zero e
  quanto ele muda quando a matriz muda, sem fazer Sarrus".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) det = 0 na hora: linha (ou coluna) de zeros; duas linhas iguais ou proporcionais;
  b) uma linha feita das outras: em (1 0 −1 / 3 2 1 / 5 4 3), cada linha é a anterior
     mais (2, 2, 2), e L3 = 2L2 − L1; confirmação por Sarrus: (6 + 0 − 12) −
     (−10 + 4 + 0) = −6 + 6 = 0;
  c) mudanças que alteram o valor: trocar duas linhas muda o sinal; multiplicar uma
     linha por k multiplica o det por k;
  d) a armadilha do det(kA) = k^n · det A: numa 3 × 3 com det A = 5, det(2A) = 2³ · 5 =
     40;
  e) o que não muda e atalhos: somar a uma linha um múltiplo de outra; transpor;
     det(AB) = det A · det B; matriz triangular ou diagonal: produto da diagonal
     principal.
- Exercício "nós fazemos": peça "pause: quanto vale o determinante de (3 7 1 / 0 2 5 /
  0 0 4)? E, se uma matriz 2 × 2 tem det 3, quanto vale det(3A)?" (triangular: 3·2·4 =
  24; det(3A) = 3² · 3 = 27).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Linhas parentes zeram o determinante."
  "Matriz inteira vezes k: o determinante vai vezes k elevado a n."
  "Triangular: multiplique a diagonal."
- Erros clássicos:
  • det(2A) = 2 · det A (o certo é 2^n · det A; numa 3 × 3, o fator é 8).
- Questões no estilo ENEM, nesta ordem:
  • Questão 8 do material (a_ij = 2i − j, ordem 3): "eu faço"; monte a matriz, veja a
    progressão das linhas e conclua det = 0 sem conta; depois confirme por Sarrus e
    mostre de onde vem cada distrator (−6 é só a parte verde; −12 soma as partes em vez
    de subtrair; 6 e 12 são erros de sinal);
  • Questão 3 (det A = 5, ordem 3, det(2A)): "você faz", com pausa; resposta 40; a A
    multiplica uma linha só (10), a B usa 2² (20), a C multiplica por 2 e por 3 (30), a
    E eleva o 5 ao cubo (125).
  Em todas: procure a propriedade antes da conta e explique as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "o determinante diferente de zero garante que a matriz
  tem inversa. Num problema de ingressos, ele garante o quê? Que existe uma única
  resposta. E ele ainda calcula essa resposta: regra de Cramer, próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: três botões de volume ao lado das três linhas de uma matriz; girar
  um botão "×2" dobra o det; girar os três ao mesmo tempo mostra o contador indo de 5
  para 10, 20 e 40.
- As linhas (1 0 −1), (3 2 1) e (5 4 3) com setas "+ (2, 2, 2)" entre elas e um selo
  verde "det = 0, sem conta".
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- L3 = 2L2 − L1 confere: 2·(3, 2, 1) − (1, 0, −1) = (5, 4, 3)?
- det(2A) = 40 e det(3A) = 27 (na 2 × 2 do exercício) estão corretos?
- Antes de cada Sarrus, a aula perguntou se havia propriedade?
```

---

## Vídeo 3: O sistema como A · X = B e a regra de Cramer

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Álgebra — Determinantes e Sistemas Lineares — Episódio 3 de 5:
O sistema como A · X = B e a regra de Cramer
RECORTE: use APENAS as seções 06 e 07 do material de apoio, mais a Questão 6 da seção 12
e a QUESTÃO NOVA escrita abaixo (ela não está no material). NÃO use a Questão 1 do
material como questão: o problema de inteiras e meias já foi resolvido por substituição
na série de Sistemas de equações lineares. Os números da seção 07 (250 ingressos,
R$ 7 400) servem só para mostrar o MÉTODO novo; ao apresentá-los, diga "é o mesmo tipo
do problema dos ingressos da série de Sistemas, agora por outro caminho". Montar
sistemas a partir do texto é revisão da série de Sistemas.
DURAÇÃO: 8 a 10 minutos

QUESTÃO NOVA (use exatamente este texto)
Uma loja vendeu, em um dia, 50 peças entre camisetas, a R$ 30,00 cada, e bonés, a
R$ 25,00 cada, arrecadando R$ 1 400,00. O número de bonés vendidos foi
A) 25.   B) 30.   C) 20.   D) cerca de 47.   E) 56.
Gabarito: C. Resolução: x camisetas e y bonés; x + y = 50 e 30x + 25y = 1 400.
D = 1·25 − 1·30 = −5; D_y = 1·1 400 − 30·50 = 1 400 − 1 500 = −100; y = −100 ÷ (−5) =
20. Conferência: 30 camisetas e 20 bonés dão 900 + 500 = 1 400. A A divide as peças ao
meio; a B é o número de camisetas; a D supõe que todos compraram camiseta (1 400 ÷ 30);
a E supõe que todos compraram boné (1 400 ÷ 25).

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma bilheteria de teatro e por uma lanchonete
   com três itens de preço fixo; só depois escreva as matrizes.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (matriz dos coeficientes, coluna das incógnitas, coluna dos termos
   independentes, matriz completa ou ampliada, forma matricial, regra de Cramer, D, D_x,
   D_y, D_z).
3. Analogias âncora, retomadas ao longo da aula:
   - "D_x é troca de figurinha: a coluna de x sai e entra a coluna das respostas";
   - "o D principal é o chão de todas as frações: fica sempre embaixo";
   - "Cramer é ferramenta de precisão: se a questão pede UMA incógnita, bastam dois
     determinantes".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: montar um sistema
   "quantidades e valores" (série de Sistemas de equações lineares); multiplicação linha
   por coluna (série de Matrizes e operações); determinante 2 × 2 e Sarrus (episódio 1).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; ao dividir dois
   negativos, diga em voz alta "negativo dividido por negativo dá positivo" e sempre
   confira a solução nas equações originais.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Numa lanchonete com suco, sanduíche e salada, a questão pede
  só o preço da salada. Com dois determinantes você chega lá, sem descobrir os outros
  preços."
- Promessa: "ao final, você vai escrever um sistema como multiplicação de matrizes e vai
  achar a incógnita pedida pela regra de Cramer, sabendo quando ela compensa".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) do sistema à forma matricial: x + y = 250 e 40x + 20y = 7 400 viram
     (1 1 / 40 20) · (x / y) = (250 / 7 400); multiplicando linha por coluna, as
     equações reaparecem; matriz completa = A com a coluna B ao lado;
  b) se det A ≠ 0, existe a inversa e a solução é única: X = A⁻¹ · B; Cramer faz essa
     conta sem montar a inversa;
  c) a regra: x = D_x ÷ D, trocando em A a coluna de x pela coluna dos termos
     independentes; o mesmo para y e z;
  d) o exemplo da seção 07, como demonstração do método: D = 20 − 40 = −20;
     D_x = 5 000 − 7 400 = −2 400, x = 120; D_y = 7 400 − 10 000 = −2 600, y = 130;
     conferência 120 + 130 = 250 e 4 800 + 2 600 = 7 400;
  e) quando vale a pena: num 3 × 3, Cramer completo exige quatro determinantes; se a
     pergunta é uma incógnita só, calcule D e o determinante dela; se pede todas,
     substituição ou escalonamento costumam ser mais rápidos.
- Exercício "nós fazemos": peça "pause: no sistema 2x + y = 7 e x − y = 2, calcule D,
  D_x e x" (D = 2·(−1) − 1·1 = −3; D_x = 7·(−1) − 1·2 = −9; x = 3; e y = 1 por D_y =
  2·2 − 7·1 = −3; conferência 6 + 1 = 7 e 3 − 1 = 2).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "D_x: a coluna de x sai, entra a coluna das respostas."
  "x é D_x dividido por D: o D principal fica embaixo."
  "Pediu uma incógnita só? Calcule só D e o dela."
- Erros clássicos:
  • trocar a LINHA de x em vez da coluna;
  • escrever x = D ÷ D_x.
- Questões no estilo ENEM, nesta ordem:
  • QUESTÃO NOVA (camisetas e bonés), "eu faço", por Cramer, calculando só D e D_y;
  • Questão 6 do material (suco, sanduíche e salada): "nós fazemos"; monte o sistema
    x + y + z = 16, 2x + y = 15, x + 2z = 14 (os zeros nas casas vazias!); calcule D
    junto com o aluno por Sarrus (2 − 5 = −3); depois peça "pause e calcule D_z" (29 −
    44 = −15) e conclua z = 5; confira com suco R$ 4 e sanduíche R$ 7; a A é o módulo
    de D, a E é o módulo de D_z sem dividir, a B e a D são as outras incógnitas.
  Em todas: nomeie as incógnitas, resolva, confira nas equações originais e explique as
  alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "e quando D dá zero? A divisão por zero não existe. Isso
  quer dizer que o sistema não tem solução? Nem sempre: às vezes ele tem infinitas.
  Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: a matriz A com a coluna de x destacada; a coluna das respostas
  (250 / 7 400) desliza e "empurra" a coluna de x para fora, formando D_x; ao final, a
  fração D_x sobre D com o D principal "no chão".
- Na Questão 6, os zeros das casas vazias aparecendo em amarelo ("não esqueça o zero").
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- A Questão 1 do material NÃO foi apresentada como questão, e a questão nova foi usada
  com o texto exato?
- Em todos os Cramer, o D principal ficou no denominador e os sinais das divisões estão
  certos (−2 400 ÷ (−20) = 120; −100 ÷ (−5) = 20; −15 ÷ (−3) = 5)?
- As soluções foram conferidas nas equações originais?
```

---

## Vídeo 4: Uma, infinitas ou nenhuma (classificar e discutir pelo determinante)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Álgebra — Determinantes e Sistemas Lineares — Episódio 4 de 5:
Uma, infinitas ou nenhuma: classificar e discutir pelo determinante
RECORTE: use APENAS as seções 08 e 09 do material de apoio, mais as Questões 4, 7 e 9 da
seção 12. NÃO use a Questão 5 do material (é quase igual a uma questão da série de
Sistemas). A classificação SPD/SPI/SI pelas retas concorrentes, paralelas e coincidentes
e a leitura de 0 = 0 e 0 = 2 já foram ensinadas na série de Sistemas de equações
lineares: aqui, revisão de no máximo 30 segundos. O foco novo é decidir pelo
determinante, discutir com parâmetro e o sistema homogêneo.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pelo técnico que ajusta dois botões (k e m) de uma
   máquina de misturas e quer saber em que posições o problema tem resposta.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (SPD, SPI, SI, parâmetro, discussão do sistema, equações compatíveis,
   equações contraditórias, equação redundante, escalonamento, sistema homogêneo,
   solução trivial).
3. Analogias âncora, retomadas ao longo da aula:
   - "D ≠ 0 é sinal verde: uma solução só, e pronto. D = 0 é sinal amarelo: pare e olhe
     as equações";
   - "com D = 0, as equações são gêmeas (uma é múltipla inteira da outra: infinitas
     soluções) ou brigadas (múltiplas só no lado esquerdo: nenhuma)";
   - "o sistema homogêneo sempre tem a porta (0, 0) aberta: ele nunca é impossível".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: as três posições de duas
   retas e as três classificações (série de Sistemas de equações lineares); determinante
   2 × 2 e Laplace (episódio 1); k² = 4 tem duas raízes (série de Equação do 2º grau).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; em toda discussão,
   escreva na tela a tabela "condição → classificação".
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Um estudante achou o terno (1, 2, 3) num sistema 3 × 3 e
  cravou: solução única. Errou: o sistema tem infinitas soluções. E o determinante
  avisava."
- Promessa: "ao final, você vai classificar qualquer sistema pelo determinante, sem
  resolver, e discutir um sistema com letras no lugar dos números".
- Pré-requisitos relâmpago (revisão das retas em no máximo 30 segundos).
- Blocos (um conceito por bloco):
  a) a tabela da seção 08: D ≠ 0 → SPD; D = 0 e equações compatíveis → SPI; D = 0 e
     contraditórias → SI; nas retas, paralelas e coincidentes têm a mesma inclinação, e
     por isso D = 0;
  b) D = 0 não é "impossível": x + 2y = 3 e 2x + 4y = 6 (gêmeas, SPI) × x + 2y = 3 e
     2x + 4y = 7 (brigadas, SI); em 2 × 2, D = 0 com D_x ou D_y ≠ 0 → SI;
  c) discussão com parâmetro em dois passos, com um exemplo NOVO (não o da seção 09):
     x + 3y = 2 e 3x + ky = m; passo 1: D = k − 9, então k ≠ 9 → SPD para qualquer m;
     passo 2: com k = 9, a 2ª equação é 3x + 9y = m, que tem os coeficientes triplos da
     1ª; m = 6 → SPI; m ≠ 6 → SI;
  d) em 3 × 3, no caso D = 0, substitua o parâmetro e escalone: uma linha "0 = 0" é
     equação redundante (SPI, se não houver contradição); "0 = número não nulo" é SI;
  e) o sistema homogêneo: todos os termos independentes iguais a zero; (0, 0, …) é
     sempre solução (a trivial); há outras soluções exatamente quando D = 0.
- Exercício "nós fazemos": peça "pause: classifique 2x − y = 1 e 4x − 2y = 5" (D =
  2·(−2) − (−1)·4 = 0; o dobro da 1ª daria 2, não 5: brigadas, SI; confirmação:
  D_x = 1·(−2) − (−1)·5 = 3 ≠ 0).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "D diferente de zero: uma solução só."
  "D igual a zero: gêmeas dão infinitas, brigadas dão nenhuma."
  "Homogêneo nunca é impossível."
- Erros clássicos:
  • D = 0 ⟹ impossível;
  • "achei uma solução, então é SPD";
  • "homogêneo pode ser impossível";
  • k² = 4 ⟹ só k = 2.
- Questões no estilo ENEM, nesta ordem:
  • Questão 4 do material (x + 2y = 3 e 2x + ky = m, quando não há solução): "eu faço",
    pelos dois passos; resposta k = 4 e m ≠ 6; a B é o caso SPI, a C o caso SPD, a D
    soma no determinante (k + 4), a E exige equações idênticas;
  • Questão 7 (homogêneo x + ky = 0 e kx + 4y = 0): "nós fazemos"; D = 4 − k² = 0, k = 2
    ou k = −2; com k = 2, (2, −1) é uma solução não trivial; a A esquece o quadrado, a B
    esquece a raiz negativa, a C dá D = 4, a D resolve k² = 16;
  • Questão 9 (o terno (1, 2, 3) que satisfaz as três equações): "você faz", com pausa;
    1ª + 2ª = 3ª, equação redundante; D = 0 por Laplace; há solução e não é única: SPI;
    outra solução: (−0,5; 2,5; 4); a A conclui unicidade, a C confunde D = 0 com
    impossível, a D não satisfaz a 1ª equação, a E diz que repetição gera
    impossibilidade.
  Em todas: calcule D primeiro, decida se precisa olhar as equações e explique as
  alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "no último episódio deste assunto, juntamos tudo,
  caçamos as pegadinhas e treinamos com questões inéditas."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: um semáforo ao lado de cada sistema; com D ≠ 0 acende o verde
  ("uma solução"); com D = 0 acende o amarelo e as duas equações aparecem lado a lado,
  ou como gêmeas (mesma camiseta, mesma reta) ou brigadas (retas paralelas que nunca se
  encontram).
- Uma porta com o letreiro (0, 0) sempre aberta no sistema homogêneo.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- A revisão das retas ficou em no máximo 30 segundos e a Questão 5 do material não foi
  usada?
- No exemplo novo, D = k − 9 e a fronteira entre SPI e SI é m = 6?
- Na Questão 7, as duas raízes k = 2 e k = −2 foram dadas?
```

---

## Vídeo 5: Revisão (Determinantes e sistemas lineares no ENEM)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula de REVISÃO para o YouTube sobre:

TEMA: Matemática — Álgebra — Determinantes e Sistemas Lineares — Episódio 5 de 5:
Revisão geral, estratégia de prova, pegadinhas e treino para o ENEM
RECORTE: use as seções 01, 10, 11 e 13 do material de apoio.
NÃO reutilize as Questões 1 a 9 da seção 12 (resolvidas nos episódios anteriores ou
descartadas por repetirem a série de Sistemas). A área de triângulo por determinante
terá série própria na Geometria Analítica: aqui, só cite.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que assistiu aos episódios 1 a 4, mas ainda é iniciante e pode ter esquecido
partes. Relembre cada conceito em uma frase simples antes de cobrá-lo.

REGRAS DE EXPLICAÇÃO
1. Cada conceito é relembrado com a mesma analogia âncora usada no seu episódio:
   o teste da chave (det ≠ 0, a inversa existe); o produto da secundária "de casaco";
   o time verde contra o time vermelho de Sarrus; as linhas parentes que zeram o det;
   os botões de volume (k^n); a troca de figurinha do D_x; o D principal como chão da
   fração; o semáforo (verde = uma solução, amarelo = olhe as equações); equações gêmeas
   e brigadas; a porta (0, 0) do homogêneo.
2. Prática de recuperação: antes de explicar, PERGUNTE e peça para o aluno pausar.
3. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
4. Uma ideia por cena. Frases curtas. Tom de conversa, falando com "você".

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "No ENEM, o sistema vem numa história de ingressos ou de
  lanchonete. O determinante é o atalho para duas perguntas: qual é o valor pedido e se
  existe uma resposta só."
- O que a prova cobra (seção 01): determinante, regra de Cramer e classificação; o que
  rende mais: D ≠ 0 garante solução única, D = 0 exige olhar as equações.
- Onde aparece nas outras áreas (seção 10): Geometria Analítica (área e alinhamento de
  três pontos), Química (balanceamento como sistema homogêneo), Física (malhas de
  circuitos), Economia (misturas, cestas e combos).
- A estratégia de prova em 3 hábitos (seção 10): procurar a propriedade antes de fazer
  Sarrus; calcular só o necessário (uma incógnita por Cramer, ou só classificar);
  conferir a resposta nas equações originais.
- "Verdadeiro ou falso? Pause e responda": transforme em afirmações os 9 erros da seção
  11 (|3 −2; 4 5| = 15 − 8; em Sarrus subtrai-se só o 1º produto; det(2A) = 2 · det A;
  D = 0 é impossível; achou uma solução, é SPD; D_x troca a linha de x; x = D ÷ D_x;
  homogêneo pode ser impossível; k² = 4 dá só k = 2). Para cada um: pausa → resposta →
  por que a pegadinha engana → a regra certa em uma frase.
- 5 questões INÉDITAS no estilo ENEM, com 5 alternativas cada (as erradas são os erros
  clássicos). Use exatamente estes dados e confira as contas na tela:
  1) O determinante de (4 −3 / 2 5) é: A) 14 B) −14 C) 26 D) −26 E) 9. Gabarito C
     (4·5 − (−3)·2 = 20 + 6 = 26); A escreve 20 − 6; D faz secundária menos principal;
     B combina os dois erros; E soma a diagonal principal.
  2) Uma matriz A de ordem 2 tem det A = 4. O determinante de 3A é: A) 7 B) 12 C) 36
     D) 64 E) 108. Gabarito C (3² · 4 = 36); B multiplica só por 3; E usa 3³, como se
     fosse 3 × 3; D eleva o 4 ao cubo; A soma 3 + 4.
  3) Três cadernos e duas canetas custam R$ 34,00; dois cadernos e cinco canetas custam
     R$ 30,00. O preço de uma caneta é: A) R$ 0,50 B) R$ 2,00 C) R$ 10,00 D) R$ 11,00
     E) R$ 22,00. Gabarito B (3c + 2p = 34 e 2c + 5p = 30; D = 15 − 4 = 11;
     D_p = 3·30 − 2·34 = 22; p = 2; o caderno custa R$ 10,00 e 20 + 10 = 30 confere);
     C é a outra incógnita; E é D_p sem dividir; D é o próprio D; A inverte a fração
     (D ÷ D_p).
  4) Sobre o sistema 2x + y = 4 e 6x + ky = 12, é correto afirmar que ele: A) é
     impossível para k = 3 B) tem infinitas soluções para k = 3 C) tem solução única
     para qualquer k D) tem infinitas soluções para k = −3 E) é impossível para todo
     k ≠ 3. Gabarito B (D = 2k − 6 = 0 só em k = 3; aí a 2ª equação é o triplo inteiro
     da 1ª, inclusive 3·4 = 12: gêmeas); A confunde D = 0 com impossível; C ignora o
     caso D = 0; D erra o sinal; E troca o caso SPD pelo SI.
  5) O sistema homogêneo x + y = 0 e 3x + ky = 0 admite soluções além de (0, 0) quando:
     A) k = 3 B) k = −3 C) k = 0 D) k ≠ 3 E) nunca, pois um homogêneo só tem a solução
     (0, 0). Gabarito A (D = k − 3 = 0); B erra o sinal; C dá D = −3 ≠ 0 (só a
     trivial); D é justamente o caso de solução única; E esquece que D = 0 libera
     outras soluções.
  Leia, peça a pausa, calcule D primeiro, resolva, confira nas equações e explique cada
  alternativa.
- Checklist de domínio (seção 13): leia os itens e diga "marque só o que você
  conseguiria explicar em voz alta para outra pessoa, sem consultar nada; o que não
  marcou, reveja o episódio correspondente" (2 × 2, Sarrus, Laplace e inversa:
  episódio 1; propriedades: episódio 2; A · X = B e Cramer: episódio 3; classificação,
  parâmetro e homogêneo: episódio 4).
- Meta antes de considerar dominado: resolver 25 questões e acertar pelo menos 18, com
  pelo menos seis de classificação ou discussão de sistemas.
- Encerramento e ponte: "o próximo assunto é Polinômios e equações polinomiais: a busca
  por soluções sai de várias incógnitas do 1º grau e vai para uma incógnita só, de grau
  alto."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Use um cronômetro visual nas pausas; um selo "PEGADINHA" em amarelo nos erros; um
  ícone de calculadora em cada questão inédita; os 4 ícones dos episódios (chave,
  botões de volume, figurinha trocada, semáforo) como índice visual da revisão.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Cada conceito foi relembrado antes de ser cobrado?
- As 5 questões inéditas têm uma única alternativa correta e contas corretas?
- Na questão 4, ficou claro que nenhum valor de k torna o sistema impossível?
```

---

## Cuidados ao revisar os roteiros

- **Sinal do segundo produto:** em |3 −2; 4 5| a conta é 15 − (−8) = 23. A IA de vídeo costuma escrever "15 − 8 = 7" na tela mesmo narrando certo; confira cada determinante 2 × 2 escrito.
- **Sarrus:** o menos vale para a soma inteira das três diagonais vermelhas (13 − 64 = −51). Se aparecer 13 − 60 + 4 + 0, está errado.
- **Cramer:** D fica sempre no denominador, e as divisões de negativo por negativo dão positivo (−2 400 ÷ −20 = 120). Confira também que o roteiro do vídeo 3 não transforma a Questão 1 do material em questão (ela repete a série de Sistemas).
- **D = 0:** a IA tende a dizer "D = 0, logo impossível". No vídeo 4 e na questão inédita 4 da revisão, D = 0 leva a SPI.
