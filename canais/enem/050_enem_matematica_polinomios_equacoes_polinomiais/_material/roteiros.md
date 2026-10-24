# Polinômios e Equações Polinomiais — série de videoaulas

Material de apoio: `01-matematica/35-polinomios-equacoes-polinomiais.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Termos semelhantes, distributiva, valor numérico com parênteses, fatoração | **Expressões algébricas e produtos notáveis** | Revisão relâmpago no vídeo 1; não reensino as operações. |
| Caixa recortada de uma folha (área do fundo com (a − 2x)(b − 2x)) | **Expressões algébricas**, Questão 6 (folha de 30 × 20, área do fundo) | **Mantive a Questão 1** deste material: a folha é outra (24 × 15) e a pergunta é o **volume** (grau 3), que é o conteúdo novo. No roteiro, o fundo é tratado como revisão e o foco é multiplicar pela altura x. |
| Bhaskara, soma −b/a e produto c/a, forma fatorada do 2º grau | **Equação do 2º grau e Bhaskara** | Revisão relâmpago. O novo é Girard no 3º grau (sinais −, +, −) e terminar a redução de grau no 2º grau. |
| Raízes como pontos onde o gráfico corta o eixo | **Função quadrática** (parábola) | Citado; aqui o novo é a multiplicidade (toca × atravessa). |
| Unidade imaginária i e raízes conjugadas (Questão 6) | **Números complexos** (próxima série) | Só i² = −1 em uma frase e a regra do par conjugado. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Polinômio, grau, valor numérico e modelagem** | 02, 03 | Q1, Q8 | 8–10 min |
| **2. Divisão, Briot-Ruffini e o teorema do resto** | 04, 05 | Q2, Q9 | 10–12 min |
| **3. Caçando raízes: forma fatorada, candidatas racionais e redução de grau** | 06, 07 | Q3, Q7 | 10–12 min |
| **4. Girard e gráficos: soma, produto, multiplicidade e raízes conjugadas** | 08, 09 | Q4, Q5, Q6 | 10–12 min |
| **5. Revisão** | 01, 10, 11, 13 | 5 inéditas | 10–12 min |

O próprio material avisa que a teoria completa de polinômios cai mais em vestibulares tradicionais do que no ENEM; por isso a revisão dá peso a modelagem e leitura de gráfico.

---

## Vídeo 1: Polinômio, grau, valor numérico e modelagem

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Álgebra — Polinômios e Equações Polinomiais — Episódio 1 de 5:
Polinômio, grau, valor numérico e modelagem
RECORTE: use APENAS as seções 02 e 03 do material de apoio, mais as Questões 1 e 8 da
seção 12. Somar, subtrair e multiplicar expressões (termos semelhantes, distributiva) já
foi ensinado na série de Expressões algébricas e produtos notáveis: aqui, revisão
rápida. A divisão fica para o episódio 2.
DURAÇÃO: 8 a 10 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma folha de papelão retangular com quadrados
   recortados nos cantos, que vira uma caixa sem tampa; o volume dela depende do
   tamanho do recorte, x.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (polinômio, coeficiente, coeficiente dominante, termo independente, grau,
   valor numérico, raiz, polinômios idênticos, polinômio nulo).
3. Analogias âncora, retomadas ao longo da aula:
   - "o grau é o andar mais alto do prédio: o maior expoente que tem coeficiente
     diferente de zero";
   - "P(1) é o raio X dos coeficientes: trocar x por 1 apaga as letras e deixa só a
     soma deles; P(0) apaga tudo o que tem x e deixa só o termo independente";
   - "polinômios idênticos se conferem como duas notas fiscais: item por item,
     coeficiente com coeficiente".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: termos semelhantes e
   distributiva "todos com todos"; parênteses ao substituir um negativo, (−2)² = 4
   (série de Expressões algébricas e produtos notáveis); 1 elevado a qualquer número
   dá 1 (série de Potenciação).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; organize sempre o
   polinômio do maior para o menor expoente antes de ler grau e coeficientes.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "(x² − 3x + 3) elevado a 20, desenvolvido, tem dezenas de
  termos. Quanto dá a soma de todos os coeficientes? Uma linha de conta: 1."
- Promessa: "ao final, você vai reconhecer um polinômio, dizer o grau dele, calcular
  valores numéricos de graça e montar o polinômio do volume de uma caixa".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) o que é polinômio: expoentes naturais; a tabela da seção 02 (4x³ − 78x² + 360x é
     grau 3; (m − 2)x² + 5x − 1 tem grau 2 se m ≠ 2 e grau 1 se m = 2; x² + 1/x e √x + 3
     não são polinômios);
  b) valor numérico e raiz: P(a) é trocar x por a; se P(a) = 0, a é raiz;
  c) os dois valores de graça em P(x) = 2x³ − 5x² + x + 7: P(0) = 7 e P(1) = 2 − 5 + 1 +
     7 = 5; a soma dos coeficientes de (3x − 2)^10 é (3 − 2)^10 = 1;
  d) o grau nas operações: produto soma os graus (3 com 2 dá 5); a soma pode
     derrubar o grau ((x² + 1) + (−x² + 3x) = 3x + 1); potência multiplica o grau
     ((x² − 3x + 3)^20 tem grau 40);
  e) identidade: ax² + (b − 1)x + 3 ≡ 2x² + 5x + c obriga a = 2, b = 6 e c = 3;
  f) modelar: três medidas de 1º grau multiplicadas (comprimento, largura, altura) dão
     um polinômio de grau 3.
- Exercício "nós fazemos": peça "pause: em P(x) = x³ − 4x² + 2x + 5, calcule P(0), P(1)
  e P(−1)" (P(0) = 5; P(1) = 1 − 4 + 2 + 5 = 4; P(−1) = −1 − 4 − 2 + 5 = −2).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Grau é o maior expoente que sobrevive."
  "P(1) soma os coeficientes; P(0) dá o termo independente."
  "Idênticos: coeficiente com coeficiente."
- Erros clássicos:
  • achar que a soma dos coeficientes é P(0).
- Questões no estilo ENEM, nesta ordem:
  • Questão 1 do material (folha de 24 cm por 15 cm, volume da caixa): "eu faço"; o
    fundo (24 − 2x) por (15 − 2x) é revisão de Expressões algébricas; o novo é
    multiplicar pela altura x: 4x³ − 78x² + 360x; confira com x = 1 (22 × 13 × 1 = 286
    e 4 − 78 + 360 = 286); a A tira x uma vez só de cada lado, a B é só o fundo, a C
    erra o sinal do termo do meio, a E esquece de multiplicar o 360 por x;
  • Questão 8 ((x² − 3x + 3)^20, soma dos coeficientes): "você faz", com pausa;
    resposta 1; a B é o grau, a C é P(0), a D soma só os coeficientes positivos de
    dentro, a E é P(−1).
  Em todas: leia o enunciado, decida se dá para substituir um número, resolva, confira e
  explique as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "como saber o resto da divisão de 2x³ − x + 5 por x + 1
  sem fazer a divisão? Trocando x por um único número. Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: a folha de papelão perdendo os quatro quadrados de lado x e se
  dobrando numa caixa; as três medidas (24 − 2x, 15 − 2x e x) aparecem nas arestas e se
  multiplicam no polinômio do volume.
- O "raio X": uma lente passando sobre P(x) e apagando os x quando x = 1, deixando só os
  coeficientes para somar.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Alguém que nunca viu o assunto entenderia cada frase sem pausar para pesquisar?
- A conferência com x = 1 da Questão 1 deu 286 nos dois lados?
- Ficou claro que P(1) é a soma dos coeficientes e P(0) é o termo independente?
```

---

## Vídeo 2: Divisão, Briot-Ruffini e o teorema do resto

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Álgebra — Polinômios e Equações Polinomiais — Episódio 2 de 5:
Divisão, Briot-Ruffini e o teorema do resto
RECORTE: use APENAS as seções 04 e 05 do material de apoio, mais as Questões 2 e 9 da
seção 12. Usar uma raiz para resolver equações de grau 3 fica para o episódio 3.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pela divisão com resto dos números (17 balas para
   5 crianças: 17 = 5 · 3 + 2) e só depois passe para polinômios.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (dividendo, divisor, quociente, resto, divisível, dispositivo de
   Briot-Ruffini, raiz do divisor, teorema do resto, teorema de D'Alembert).
3. Analogias âncora, retomadas ao longo da aula:
   - "Briot-Ruffini é uma esteira: desce o primeiro, multiplica pela raiz, soma com o
     próximo, e repete";
   - "o teorema do resto é o atalho do pedágio: em vez de percorrer a divisão inteira,
     substitua a raiz do divisor e pague só o resto";
   - "a raiz do divisor mora do lado oposto: x − 2 mora em 2; x + 3 mora em −3".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: dividendo = divisor ×
   quociente + resto, com resto menor que o divisor (série de Divisibilidade, primos,
   MMC e MDC); valor numérico (episódio 1); resolver um sistema 2 × 2 (série de Sistemas
   de equações lineares).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; antes de todo
   Briot-Ruffini, escreva TODOS os coeficientes, com os zeros dos termos que faltam.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Resto da divisão de 2x³ − x + 5 por x + 1? Sem armar a conta:
  troque x por −1. Dá −2 + 1 + 5 = 4. Pronto."
- Promessa: "ao final, você vai dividir por x − a em uma linha, achar restos sem dividir
  e descobrir o valor de k que deixa um polinômio divisível".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) a relação P(x) = D(x) · Q(x) + R(x), com grau R < grau D; grau Q = grau P − grau D;
     divisor de grau 1 → resto é número; divisor de grau 2 → resto da forma ax + b;
  b) Briot-Ruffini: 2x³ − 3x² − 5x + 6 dividido por x − 2: desce 2; 2·2 − 3 = 1;
     2·1 − 5 = −3; 2·(−3) + 6 = 0; quociente 2x² + x − 3 e resto 0, então 2 é raiz;
  c) as duas armadilhas da esteira: x³ − 4x + 1 tem coeficientes 1, 0, −4, 1 (o zero do
     x² que falta); para x + 3, use −3;
  d) teorema do resto: o resto por x − a é P(a), porque trocar x por a zera o termo
     (x − a) · Q(x); exemplo do gancho: 2x³ − x + 5 por x + 1 → P(−1) = 4;
  e) D'Alembert: divisível por x − a se, e só se, P(a) = 0; x³ + kx − 4 divisível por
     x − 2: 8 + 2k − 4 = 0, k = −2;
  f) resto por um divisor de grau 2, (x − a)(x − b): escreva R(x) = mx + n e use
     P(a) = R(a) e P(b) = R(b), que dão um sistema 2 × 2.
- Exercício "nós fazemos": peça "pause: divida x³ − 4x + 1 por x − 1 com Briot-Ruffini
  e confira o resto pelo teorema" (coeficientes 1, 0, −4, 1; desce 1; 1 + 0 = 1;
  1 − 4 = −3; −3 + 1 = −2; quociente x² + x − 3, resto −2; P(1) = 1 − 4 + 1 = −2).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "O resto por x − a é P(a)."
  "Desce, multiplica pela raiz, soma."
  "Não pule o zero; x + 3 usa −3."
- Erros clássicos:
  • fazer Briot-Ruffini sem o coeficiente 0;
  • dividir por x + 3 usando 3;
  • achar que o resto por x − a é P(−a).
- Questões no estilo ENEM, nesta ordem:
  • Questão 2 do material (x³ − 2x² + kx + 6 divisível por x − 3): "eu faço"; P(3) = 0
    dá 27 − 18 + 3k + 6 = 0, k = −5; a A para em 3k = −15, a B usa P(−3), a D erra o
    sinal no fim, a E combina os dois erros;
  • Questão 9 (restos 3 por x − 1 e −6 por x + 2; resto por (x − 1)(x + 2)): "você faz",
    com pausa e uma dica antes ("o resto tem grau no máximo 1: mx + n"); m + n = 3 e
    −2m + n = −6 dão m = 3 e n = 0, resto 3x; a A soma os restos, a C multiplica, a D
    toma o segundo resto como termo independente, a E associa cada resto à raiz errada
    (−3x − 3).
  Em todas: leia o enunciado, identifique a raiz do divisor, resolva e explique as
  alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "o lucro de uma fábrica é x³ − 6x² + 11x − 6 e você
  sabe que ele zera em x = 1. Como achar os outros dois valores que zeram o lucro? Com
  a esteira de hoje. Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: o dispositivo de Briot-Ruffini como uma esteira; o número desce,
  é multiplicado pela raiz (seta curva) e cai somado na casa seguinte, até o resto
  acender na ponta (verde se for zero).
- Uma casa vazia piscando em amarelo onde falta o coeficiente zero.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- O Briot-Ruffini do bloco b deu 2, 1, −3 e resto 0?
- Em todo divisor x + a, a raiz usada foi −a?
- Na Questão 9, a resposta é 3x e o sistema m + n = 3, −2m + n = −6 foi resolvido certo?
```

---

## Vídeo 3: Caçando raízes (forma fatorada, candidatas racionais e redução de grau)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Álgebra — Polinômios e Equações Polinomiais — Episódio 3 de 5:
Caçando raízes: forma fatorada, candidatas racionais e redução de grau
RECORTE: use APENAS as seções 06 e 07 do material de apoio, mais as Questões 3 e 7 da
seção 12. Bhaskara, soma e produto e a forma fatorada do 2º grau já foram ensinados na
série de Equação do 2º grau e Bhaskara: aqui, revisão rápida. Girard no 3º grau e
gráficos ficam para o episódio 4.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pelo lucro de uma pequena fábrica, que se anula
   em certas produções, e por um molho de chaves em que só algumas podem abrir a porta.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (equação polinomial, teorema fundamental da álgebra, raiz complexa, forma
   fatorada, fator, multiplicidade, raiz simples, raiz dupla, raiz racional, candidata).
3. Analogias âncora, retomadas ao longo da aula:
   - "raiz e fator são espelhos: a raiz −2 vira o fator (x + 2); a raiz 3 vira (x − 3)";
   - "caçar raízes é testar as chaves do molho: as candidatas são os divisores do termo
     independente divididos pelos divisores do coeficiente dominante";
   - "cada raiz achada derruba um andar do prédio: Briot-Ruffini baixa o grau até chegar
     no 2º grau, e aí Bhaskara termina".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: Briot-Ruffini e P(a) = 0
   (episódio 2); Bhaskara, soma e produto e a forma a(x − x₁)(x − x₂) (série de Equação
   do 2º grau e Bhaskara); divisores de um número (série de Divisibilidade).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; toda raiz encontrada é
   conferida substituindo no polinômio original.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Não existe uma 'Bhaskara do 3º grau' que se use na prova. Mesmo
  assim, x³ − 2x² − 5x + 6 = 0 se resolve em um minuto: teste uma chave, baixe um grau e
  termine com Bhaskara."
- Promessa: "ao final, você vai achar todas as raízes de uma equação de grau 3 com
  coeficientes inteiros e escrever o polinômio na forma fatorada sem errar sinal".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) o teorema fundamental (versão de prova): grau n ≥ 1 → exatamente n raízes
     complexas, contadas com multiplicidade; algumas reais, outras não;
  b) a forma fatorada P(x) = a_n(x − r₁)(x − r₂)…(x − r_n): raízes −2, 1 e 3 com a_n = 1
     dão (x + 2)(x − 1)(x − 3) = x³ − 2x² − 5x + 6; e não esqueça o a_n: as raízes de
     2x² − 2 são ±1, mas o polinômio é 2(x − 1)(x + 1);
  c) multiplicidade: em (x + 1)²(x − 3), −1 é raiz dupla e 3 é simples: três raízes
     contadas, dois valores distintos;
  d) as candidatas racionais: p divide o termo independente e q divide o coeficiente
     dominante; com dominante 1, só inteiros divisores do termo independente;
  e) o roteiro de 4 passos no polinômio x³ − 2x² − 5x + 6: candidatas ±1, ±2, ±3, ±6;
     P(1) = 0; Briot-Ruffini com 1 dá 1, −1, −6 e resto 0; x² − x − 6 = 0 dá 3 e −2;
     conjunto solução {−2, 1, 3};
  f) os atalhos de teste: teste 1 primeiro (é só somar os coeficientes); depois −1
     (troca o sinal dos termos de grau ímpar).
- Exercício "nós fazemos": peça "pause: resolva x³ − 7x + 6 = 0" (soma dos coeficientes
  1 + 0 − 7 + 6 = 0, então 1 é raiz; Briot-Ruffini com 1 nos coeficientes 1, 0, −7, 6 dá
  1, 1, −6 e resto 0; x² + x − 6 = 0 dá 2 e −3; conjunto solução {−3, 1, 2}).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Raiz e fator têm sinais opostos."
  "Candidatas: divisores do termo independente sobre divisores do dominante."
  "Achou uma raiz, Briot-Ruffini derruba um grau."
- Erros clássicos:
  • raiz −2 virar o fator (x − 2);
  • esquecer o coeficiente dominante na forma fatorada.
- Questões no estilo ENEM, nesta ordem:
  • Questão 3 do material (lucro x³ − 6x² + 11x − 6, raiz conhecida 1): "eu faço";
    Briot-Ruffini dá 1, −5, 6 e resto 0; x² − 5x + 6 tem raízes 2 e 3 (soma 5, produto
    6); confira L(2) = 0 e L(3) = 0; a B troca os sinais, a C lê coeficientes como
    raízes, a D erra a primeira soma da esteira (−7), a E troca o sinal do 6;
  • Questão 7 (2x³ − 3x² − 3x + 2 = 0): "você faz", com pausa; candidatas ±1, ±2, ±1/2;
    P(−1) = 0; Briot-Ruffini com −1 dá 2, −5, 2; 2x² − 5x + 2 = 0, Δ = 9, raízes 2 e
    1/2; conjunto {−1, 1/2, 2}; a A troca todos os sinais, a B testa só inteiros e para,
    a C lista candidatas sem testar (P(1) = −2 e P(−2) = −20), a D inclui o 1, que não
    é raiz.
  Em todas: liste as candidatas, teste, reduza o grau, termine no 2º grau, confira e
  explique as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "as arestas de um bloco retangular são as raízes de
  2x³ − 14x² + 28x − 16 = 0. Dá para achar o volume sem descobrir nenhuma aresta? Dá.
  Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: um molho de chaves com as candidatas (±1, ±2, ±3, ±6); cada chave
  testada na fechadura P(x); a que gira (P = 0) abre a porta e o prédio do polinômio
  perde um andar (grau 3 → grau 2).
- Um espelho entre "raiz −2" e "fator (x + 2)", invertendo o sinal.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- (x + 2)(x − 1)(x − 3) foi desenvolvido corretamente em x³ − 2x² − 5x + 6?
- Toda raiz encontrada foi conferida no polinômio original?
- Na Questão 7, o conjunto solução é {−1, 1/2, 2}?
```

---

## Vídeo 4: Girard e gráficos (soma, produto, multiplicidade e raízes conjugadas)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Álgebra — Polinômios e Equações Polinomiais — Episódio 4 de 5:
Girard e gráficos: soma, produto, multiplicidade e raízes conjugadas
RECORTE: use APENAS as seções 08 e 09 do material de apoio, mais as Questões 4, 5 e 6 da
seção 12. Soma −b/a e produto c/a do 2º grau já foram ensinados na série de Equação do
2º grau e Bhaskara: aqui, revisão rápida. A unidade imaginária i terá série própria (a
próxima, Números complexos): aqui, só i² = −1 e a regra do par conjugado.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por um bloco retangular (uma caixa de sapato) com
   arestas a, b e c, e por uma bola quicando no chão × uma bola atravessando o chão de
   um vidro.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (relações de Girard, soma dos produtos dois a dois, multiplicidade par,
   multiplicidade ímpar, unidade imaginária, raiz não real, conjugado).
3. Analogias âncora, retomadas ao longo da aula:
   - "Girard no 3º grau tem sinais alternados: menos, mais, menos, sempre dividindo
     pelo a";
   - "raiz de multiplicidade par quica no eixo (toca e volta); ímpar atravessa";
   - "raízes não reais andam em dupla, como par de meias: se 1 − i é raiz de um
     polinômio de coeficientes reais, 1 + i vem junto".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: soma −b/a e produto c/a
   do 2º grau (série de Equação do 2º grau e Bhaskara); forma fatorada e multiplicidade
   (episódio 3); onde a parábola corta o eixo x (série de Função quadrática); i² = −1,
   em uma frase, com a promessa "isso tem série própria, a próxima".
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; ao usar Girard, escreva
   a, b, c e d com os sinais antes de qualquer fração.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "As arestas de um bloco são as raízes de 2x³ − 14x² + 28x − 16 =
  0. O volume é 8 metros cúbicos, e você descobre isso sem achar nenhuma aresta."
- Promessa: "ao final, você vai tirar soma e produto das raízes direto dos coeficientes,
  escolher a lei de um gráfico pelas raízes e completar as raízes não reais".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) Girard no 3º grau, para ax³ + bx² + cx + d = 0: soma = −b/a; soma dos produtos dois
     a dois = c/a; produto = −d/a; conferência em x³ − 2x² − 5x + 6, de raízes −2, 1 e 3:
     soma 2, pares −2 − 6 + 3 = −5, produto −6;
  b) a leitura geométrica: arestas de um bloco = raízes; produto = volume; soma dos
     produtos dois a dois = metade da área total; soma = um quarto do comprimento de
     todas as arestas;
  c) o gráfico conta as raízes reais: onde a curva encontra o eixo horizontal; em
     (x + 1)²(x − 3), a curva toca em −1 e atravessa em 3; P(0) = 1 · (−3) = −3;
  d) fatos que eliminam alternativas: grau n → no máximo n encontros com o eixo; grau
     ímpar com coeficientes reais → pelo menos uma raiz real; dominante positivo e grau
     ímpar → começa embaixo e termina em cima;
  e) as raízes conjugadas: com coeficientes reais, a + bi traz a − bi; o par 1 ± i gera
     (x − 1 + i)(x − 1 − i) = x² − 2x + 2, de coeficientes reais.
- Exercício "nós fazemos": peça "pause: as raízes de x³ − 6x² + 11x − 6 = 0 são 1, 2 e 3
  (o lucro da Questão 3). Confira as três relações de Girard" (soma 6 = −(−6)/1; pares
  2 + 3 + 6 = 11 = 11/1; produto 6 = −(−6)/1).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Girard no 3º grau: menos, mais, menos, sempre dividindo por a."
  "Multiplicidade par toca; ímpar atravessa."
  "Raiz não real chega com o conjugado."
- Erros clássicos:
  • usar d/a como produto no 3º grau (o certo é −d/a);
  • achar que toda raiz atravessa o eixo;
  • aceitar 1 − i sozinha como raiz de um polinômio de coeficientes reais.
- Questões no estilo ENEM, nesta ordem:
  • Questão 4 do material (bloco com arestas raízes de 2x³ − 14x² + 28x − 16 = 0):
    "eu faço"; volume = produto = −(−16)/2 = 8; conferência 2(x − 1)(x − 2)(x − 4),
    arestas 1, 2 e 4; a A é a soma (7), a C é c/a (14, metade da área), a D esquece de
    dividir por 2 (16), a E é a área total (28);
  • Questão 5 (grau 3, atravessa em −1, toca em 2, corta o eixo y em (0, 4)): "nós
    fazemos"; P = a(x + 1)(x − 2)², P(0) = 4a = 4, a = 1; a A troca os sinais das
    raízes, a B inverte as multiplicidades, a C tem P(0) = −4, a D tem grau 2;
  • Questão 6 (grau 3, raízes 2 e 1 − i): "você faz", com pausa; o conjugado 1 + i entra;
    fator x² − 2x + 2; P = (x − 2)(x² − 2x + 2) = x³ − 4x² + 6x − 4; a A troca os sinais
    das raízes, a C calcula (1 − i)(1 + i) como 0, a D usa x² + 2, a E deixa de fora a
    raiz 2.
  Em todas: leia o enunciado, pergunte "é soma, produto ou gráfico?", resolva e explique
  as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "no último episódio deste assunto, juntamos tudo,
  caçamos as pegadinhas e treinamos com questões inéditas."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: o gráfico de (x + 1)²(x − 3) sendo desenhado; em −1 uma bola quica
  no eixo e volta (selo "par: toca"); em 3 a bola atravessa o eixo (selo "ímpar:
  atravessa"); o ponto (0, −3) acende no eixo vertical.
- Um bloco retangular com as arestas 1, 2 e 4 crescendo até o volume 8, ao lado da
  fração −d/a.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Os sinais de Girard (−b/a, c/a, −d/a) foram usados corretamente em todas as contas?
- Na Questão 5, a lei escolhida é (x + 1)(x − 2)² com P(0) = 4?
- Na Questão 6, (1 − i)(1 + i) deu 2, porque i² = −1?
```

---

## Vídeo 5: Revisão (Polinômios no ENEM)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula de REVISÃO para o YouTube sobre:

TEMA: Matemática — Álgebra — Polinômios e Equações Polinomiais — Episódio 5 de 5:
Revisão geral, estratégia de prova, pegadinhas e treino para o ENEM
RECORTE: use as seções 01, 10, 11 e 13 do material de apoio.
NÃO reutilize as Questões 1 a 9 da seção 12 (já resolvidas nos episódios anteriores).
Os números complexos terão série própria (a próxima): aqui, só cite a ponte.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que assistiu aos episódios 1 a 4, mas ainda é iniciante e pode ter esquecido
partes. Relembre cada conceito em uma frase simples antes de cobrá-lo.

REGRAS DE EXPLICAÇÃO
1. Cada conceito é relembrado com a mesma analogia âncora usada no seu episódio:
   o grau como andar mais alto do prédio; o raio X do P(1); as notas fiscais conferidas
   item por item; a esteira de Briot-Ruffini; o atalho do pedágio (teorema do resto);
   a raiz do divisor que mora do lado oposto; raiz e fator como espelhos; o molho de
   chaves das candidatas; cada raiz derrubando um andar; menos, mais, menos de Girard;
   a bola que quica ou atravessa; as raízes conjugadas como par de meias.
2. Prática de recuperação: antes de explicar, PERGUNTE e peça para o aluno pausar.
3. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
4. Uma ideia por cena. Frases curtas. Tom de conversa, falando com "você".

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Três frases resolvem quase toda questão de polinômio: a é raiz
  se P(a) = 0; o resto por x − a é P(a); e uma raiz conhecida baixa o grau até o 2º.
  Hoje você treina as três."
- O que a prova cobra (seção 01): modelar (volume, área, lucro), valor numérico e
  raízes, leitura de gráficos, relações entre raízes e coeficientes; o próprio material
  avisa que a teoria completa cai mais em vestibulares tradicionais.
- Onde aparece nas outras áreas (seção 10): Geometria Espacial (volume de caixas e
  blocos), Economia (raízes do lucro como pontos de equilíbrio), Física (posição no MUV,
  "volta à origem" é raiz), Números complexos (pares conjugados).
- A estratégia de prova em 4 hábitos (seção 10): raiz? substitua; raiz dada é convite a
  Briot-Ruffini; pediu soma ou produto? Girard; gráfico? teste P(0) de cada alternativa
  e depois as raízes e multiplicidades.
- "Verdadeiro ou falso? Pause e responda": transforme em afirmações os 9 erros da seção
  11 (raiz −2 dá o fator (x − 2); Briot-Ruffini dispensa o coeficiente 0; para dividir
  por x + 3 usa-se 3; o resto por x − a é P(−a); o produto das raízes do 3º grau é d/a;
  as raízes bastam para identificar o polinômio, sem o coeficiente dominante; toda raiz
  atravessa o eixo; 1 − i pode ser raiz sozinha; a soma dos coeficientes é P(0)). Para
  cada um: pausa → resposta → por que a pegadinha engana → a regra certa em uma frase.
- 5 questões INÉDITAS no estilo ENEM, com 5 alternativas cada (as erradas são os erros
  clássicos). Use exatamente estes dados e confira as contas na tela:
  1) Modelagem com raiz por teste: um reservatório em forma de bloco tem base quadrada
     de lado x metros e altura (x + 1) metros, e seu volume é 12 m³. O lado da base
     mede: A) 3 m B) 4 m C) 2 m D) 6 m E) 12 m. Gabarito C (x²(x + 1) = 12 →
     x³ + x² − 12 = 0; candidata 2: 8 + 4 − 12 = 0; Briot-Ruffini com 2 nos coeficientes
     1, 1, 0, −12 dá 1, 3, 6 e resto 0; x² + 3x + 6 tem Δ = 9 − 24 < 0, sem outra raiz
     real); A é a altura; B é a área da base; D lê um coeficiente do quociente como
     raiz; E toma o termo independente como raiz.
  2) Teorema do resto: o resto da divisão de x⁴ − 3x² + x + 2 por x + 2 é: A) 4 B) 8
     C) 2 D) 1 E) −20. Gabarito A (P(−2) = 16 − 12 − 2 + 2 = 4; pela esteira, com
     coeficientes 1, 0, −3, 1, 2: 1, −2, 1, −1 e resto 4); B usa P(2); C é P(0); D é
     P(1), a soma dos coeficientes; E esquece o coeficiente 0 e trata o polinômio como
     x³ − 3x² + x + 2.
  3) Girard no bloco: as arestas, em cm, de uma caixa são as raízes de x³ − 9x² + 26x −
     24 = 0. A área total da caixa, em cm², é: A) 9 B) 24 C) 26 D) 36 E) 52. Gabarito E
     (soma dos produtos dois a dois = 26 = metade da área total; arestas 2, 3 e 4
     conferem: 6 + 8 + 12 = 26); C esquece de dobrar; B é o volume; A é a soma das
     arestas distintas; D é o comprimento de todas as arestas (4 · 9).
  4) Lei a partir do gráfico: um polinômio de grau 3 apenas toca o eixo horizontal em
     x = 1, atravessa esse eixo em x = −3 e corta o eixo vertical em (0, −6). A lei é:
     A) (x − 1)²(x + 3) B) −2(x + 1)²(x − 3) C) −2(x − 1)(x + 3)² D) 2(x − 1)²(x + 3)
     E) −2(x − 1)²(x + 3). Gabarito E (P = a(x − 1)²(x + 3); P(0) = 3a = −6, a = −2); A
     esquece o coeficiente dominante (P(0) = 3); B troca os sinais das raízes; C inverte
     as multiplicidades; D erra o sinal de a (P(0) = 6).
  5) Raízes conjugadas: um polinômio de grau 3, com coeficientes reais e coeficiente
     dominante 1, tem raízes 1 e 2i (i² = −1). Ele é: A) x³ − x² + 4x − 4
     B) x³ − x² − 4x + 4 C) x³ + x² + 4x + 4 D) x² + 4 E) x² − (1 + 2i)x + 2i. Gabarito
     A ((x − 1)(x − 2i)(x + 2i) = (x − 1)(x² + 4)); B calcula (2i)(−2i) como −4, como se
     i² fosse 1; C troca o sinal da raiz 1; D esquece a raiz 1; E esquece o conjugado
     −2i (e fica com coeficientes não reais).
  Leia, peça a pausa, pergunte qual das três frases do gancho resolve, resolva, confira
  e explique cada alternativa.
- Checklist de domínio (seção 13): leia os itens e diga "marque só o que você
  conseguiria explicar em voz alta para outra pessoa, sem consultar nada; o que não
  marcou, reveja o episódio correspondente" (grau, P(0), P(1), identidade e modelagem:
  episódio 1; divisão, Briot-Ruffini e restos: episódio 2; forma fatorada, candidatas e
  redução de grau: episódio 3; Girard, gráfico e conjugadas: episódio 4).
- Meta antes de considerar dominado: resolver 25 questões e acertar pelo menos 18, com
  pelo menos cinco de modelagem ou leitura de gráfico.
- Encerramento e ponte: "o próximo assunto é Números complexos, que explica de vez as
  raízes não reais que apareceram aqui, como 1 − i e 2i."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Use um cronômetro visual nas pausas; um selo "PEGADINHA" em amarelo nos erros; um
  ícone de caixa ou gráfico em cada questão inédita; os 4 ícones dos episódios (caixa de
  papelão, esteira, molho de chaves, bola quicando) como índice visual da revisão.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Cada conceito foi relembrado antes de ser cobrado?
- As 5 questões inéditas têm uma única alternativa correta e contas corretas?
- Na questão 2, a raiz usada para x + 2 foi −2 e o coeficiente 0 do x³ foi escrito?
```

---

## Cuidados ao revisar os roteiros

- **Sinais de Girard no 3º grau:** soma −b/a, pares c/a, produto **−d/a**. Na Questão 4 o produto é −(−16)/2 = 8; se a IA usar d/a, aparece −8, que nem está nas alternativas, e ela tende a "ajustar" a conta.
- **Raiz do divisor:** para x + 3 usa-se −3; para x + 2, −2. Na Questão 2, P(−3) = 0 leva a k = −13 (distrator B); a resposta é k = −5, com P(3).
- **Coeficiente zero:** em x³ − 4x + 1 e x³ − 7x + 6 (exercícios dos vídeos 2 e 3) e na questão inédita 2 da revisão, o zero precisa aparecer na esteira. Confira a tela.
- **Questão 6 e a inédita 5:** usam i² = −1 antes da série de Números complexos. (1 − i)(1 + i) = 1 − i² = 2 e (2i)(−2i) = −4i² = 4; com i² = 1 a IA chega nos distratores C e B, respectivamente.
