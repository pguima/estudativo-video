# Matrizes e Operações — série de videoaulas

Material de apoio: `01-matematica/33-matrizes-operacoes.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Resolver duas equações ao mesmo tempo (igualdade de matrizes: x + y = 7 e x − y = 1) | **Sistemas de equações lineares** (método da adição) | Revisão relâmpago no vídeo 2; não reensino o método. |
| O número ad − bc da inversa 2 × 2 e a forma A · X = B | **Determinantes e sistemas lineares** (próxima série) | Uso a fórmula da inversa e só prometo: "esse número ganha nome na próxima série". |
| Lei de formação a_ij = 2i − j | Volta na **Questão 8 de Determinantes** (versão 3 × 3) | Aqui fica só a montagem da 2 × 3; o determinante dela é assunto da próxima série. |
| Distância entre cidades, leitura de tabelas | Geografia (redes de transporte) e, mais adiante, leitura de tabelas | Só citado na revisão. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Matriz é uma tabela com endereço** | 02, 03, 08 (tabelas e imagens) | Q1, Q5 | 10–12 min |
| **2. Operações casa a casa: igualdade, soma e número × matriz** | 04 | Q8 | 6–8 min |
| **3. Multiplicação de matrizes: linha por coluna** | 05, 08 (A² e rotas) | Q3, Q2, Q7 | 10–12 min |
| **4. O que muda em relação aos números e a matriz inversa** | 06, 07 | Q4, Q9, Q6 | 10–12 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

O material declara incidência Alta, mas na prática o ENEM cobra matriz quase só como leitura de tabela e produto em contexto. Por isso os vídeos 1 e 3 são os que mais importam; o vídeo 2 é curto.

---

## Vídeo 1: Matriz é uma tabela com endereço

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Álgebra — Matrizes e Operações — Episódio 1 de 5:
Matriz é uma tabela com endereço
RECORTE: use APENAS as seções 02 e 03 do material de apoio e a parte da seção 08 sobre
tabelas de distâncias, de jogos e imagens digitais, mais as Questões 1 e 5 da seção 12.
O quadrado da matriz de ligações (A², rotas com escala) fica para o episódio 3.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pela tabela de classificação de um campeonato,
   por uma tabela de distâncias entre cidades num guia rodoviário e pela foto do
   celular ampliada até aparecerem os quadradinhos (pixels). Só depois diga "isso é uma
   matriz".
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (matriz, linha, coluna, ordem m × n, elemento a_ij, lei de formação, matriz
   quadrada, diagonal principal, diagonal secundária, matriz nula, identidade, diagonal,
   triangular, transposta, simétrica, pixel).
3. Analogias âncora, retomadas ao longo da aula:
   - "a_ij é o assento do cinema: primeiro a FILEIRA (linha), depois a POLTRONA
     (coluna). Fileira 2, poltrona 3 não é o mesmo lugar que fileira 3, poltrona 2";
   - "tabela de estrada de mão dupla é um espelho: a diagonal principal é o espelho, e o
     que está de um lado se repete do outro";
   - "no campeonato, a LINHA conta o que o time fez; a COLUNA conta o que fizeram contra
     ele".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: soma e subtração de
   inteiros com sinal (série de Operações e conjuntos numéricos), porque o saldo de gols
   pode ser negativo.
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; ao lado de cada
   matriz na tela, escreva o que é linha e o que é coluna ("linha = time que marcou").
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Numa tabela de gols, quem troca linha por coluna transforma o
  time com o PIOR saldo do campeonato, −3, num líder com +3. A conta estava certa; a
  leitura, não."
- Promessa: "ao final, você vai ler qualquer tabela em forma de matriz sem trocar o
  endereço e vai reconhecer os tipos de matriz que aparecem nos enunciados".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) da tabela à matriz: ordem m × n, sempre linhas primeiro, depois colunas;
  b) o endereço a_ij: linha i, coluna j; a_23 e a_32 são elementos diferentes;
  c) lei de formação: a_ij = 2i − j, ordem 2 × 3, substituindo endereço por endereço
     (a_11 = 1, a_12 = 0, a_13 = −1, a_21 = 3, a_22 = 2, a_23 = 1);
  d) os tipos que aparecem nos enunciados (tabela da seção 03): quadrada com as duas
     diagonais, nula, identidade, diagonal, triangular; a transposta troca linhas por
     colunas, e uma 2 × 3 vira 3 × 2 (linhas 1 2 3 / 4 5 6 viram as colunas 1 4 / 2 5 /
     3 6); a simétrica é igual à transposta (0 8 5 / 8 0 3 / 5 3 0);
  e) o endereço tem significado: distâncias (simétrica, diagonal zero, valor faltando
     se copia do espelho), gols (linha = feitos, coluna = sofridos, saldo = linha −
     coluna; a tabela de gols NÃO é simétrica: 3 a 1 não é 1 a 3);
  f) imagem digital: cada pixel é um elemento; 1 aceso, 0 apagado; trocar 1 por 0
     inverte as cores; a transposta espelha a figura na diagonal.
- Exercício "nós fazemos": peça "pause: na matriz 2 × 2 com a_ij = i + 2j, quanto vale
  a_21? E a_12?" (a_21 = 2 + 2 = 4; a_12 = 1 + 4 = 5: endereços trocados, valores
  diferentes).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Primeiro a linha, depois a coluna."
  "Tabela de mão dupla é simétrica: a diagonal é o espelho."
  "Linha é o que o time fez; coluna é o que ele sofreu."
- Erros clássicos:
  • ler a_23 como linha 3, coluna 2;
  • achar que a transposta de uma 2 × 3 continua 2 × 3;
  • tomar a coluna como gols marcados.
- Questões no estilo ENEM, nesta ordem:
  • Questão 1 do material (torneio de quatro times, maior saldo): "eu faço", montando a
    tabela marcados (linha) × sofridos (coluna) × saldo e conferindo que a soma dos
    saldos é zero; mostre que a C sai de quem fez "coluna − linha" (time 3 com +3) e
    que a B escolhe só quem mais marcou;
  • Questão 5 (distâncias com x e y apagados, trajeto 1 → 3 → 2 → 4): "você faz", com
    pausa; x = 150 e y = 140 pelo espelho; explique que a A trata y como zero, a B
    copia o vizinho da linha, a D usa a distância 1–4 e a E soma a volta.
  Em todas: leia o enunciado, rotule linha e coluna, resolva e explique as alternativas
  erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "se uma matriz tem as notas da prova 1 e outra as da
  prova 2, dá para calcular as médias da turma inteira de uma vez? Dá, e a conta é casa
  com casa. Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: um cursor percorrendo a fileira 2 de uma sala de cinema e parando
  na poltrona 3, enquanto a mesma posição acende numa matriz ao lado (a_23); depois o
  cursor faz o caminho errado (fileira 3, poltrona 2) e acende outro número.
- A tabela de distâncias com a diagonal virando um espelho e os valores apagados
  "refletindo" do outro lado.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Em todo a_ij, o primeiro índice foi tratado como linha?
- Na Questão 1, os saldos são +2, 0, −3 e +1, e a soma dá zero?
- A diferença entre tabela simétrica (distâncias) e não simétrica (gols) ficou clara?
```

---

## Vídeo 2: Operações casa a casa (igualdade, soma e número × matriz)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Álgebra — Matrizes e Operações — Episódio 2 de 5:
Operações casa a casa: igualdade, soma e número vezes matriz
RECORTE: use APENAS a seção 04 do material de apoio, mais a Questão 8 da seção 12.
Resolver duas equações ao mesmo tempo já foi ensinado na série de Sistemas de equações
lineares: aqui, revisão rápida. A multiplicação de duas matrizes fica para o episódio 3.
DURAÇÃO: 6 a 8 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por duas planilhas de notas (prova 1 e prova 2)
   de uma mesma turma, com os mesmos alunos nas linhas e as mesmas disciplinas nas
   colunas.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (matrizes de mesma ordem, elementos correspondentes, igualdade de matrizes,
   matriz oposta, elemento neutro, média ponderada).
3. Analogias âncora, retomadas ao longo da aula:
   - "somar matrizes é sobrepor duas folhas transparentes da mesma planilha: cada casa
     só conversa com a casa que está embaixo dela";
   - "número vezes matriz é aumento geral: TODO mundo recebe, não só a primeira linha";
   - "igualdade de matrizes é um sistema disfarçado: cada casa vira uma equação".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: o endereço a_ij
   (episódio 1); o método da adição para x + y = 7 e x − y = 1 (série de Sistemas de
   equações lineares); multiplicar decimal por inteiro (0,4 · 5 = 2).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; destaque na tela a casa
   que está sendo calculada nas duas matrizes ao mesmo tempo.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Três alunos, duas disciplinas, duas provas: são seis médias
  ponderadas. Com matrizes, você escreve uma conta só, 0,4A + 0,6B, e ainda escapa da
  pegadinha de que 6,0 também aprova."
- Promessa: "ao final, você vai somar matrizes, multiplicar por número e resolver
  igualdades de matrizes sem errar uma casa".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) igualdade: mesma ordem e casas correspondentes iguais; a matriz com x + y, 3, 2,
     x − y igual à matriz 7, 3, 2, 1 vira x + y = 7 e x − y = 1, logo x = 4 e y = 3;
  b) adição e subtração casa com casa, só entre matrizes de mesma ordem:
     (1 4 / 2 0) + (3 −1 / 5 2) = (4 3 / 7 2);
  c) número vezes matriz: 3 · (1 4 / 2 0) = (3 12 / 6 0), todas as casas;
  d) a média ponderada da turma: M = 0,4A + 0,6B, calculada posição por posição;
  e) propriedades como nos números (comutativa, associativa, matriz nula como neutro,
     oposta −A) e a equação 2X + A = B resolvida como no 1º grau: X = (B − A) ÷ 2,
     casa a casa.
- Exercício "nós fazemos": peça "pause: com A = (2 5 / 1 3) e B = (4 1 / 3 7), quanto
  é 2A − B?" (2A = (4 10 / 2 6); 2A − B = (0 9 / −1 −1)).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Soma e igualdade: casa com casa, na mesma ordem."
  "Número vezes matriz atinge todas as casas."
  "Igualdade de matrizes vira um sistema."
- Erros clássicos:
  • multiplicar só a primeira linha em 3 · A;
  • tentar somar matrizes de ordens diferentes.
- Questão no estilo ENEM: Questão 8 do material (médias com pesos 0,4 e 0,6), em três
  tempos: "eu faço" a casa m_11 (2 + 4,2 = 6,2); "nós fazemos" m_12 e m_21 (6,2 e 5,8);
  "você faz" as outras três (6,4; 6,0; 5,4), com pausa, e a contagem final: 4 médias
  maiores ou iguais a 6,0. Explique as erradas: A conta alunos aprovados nas duas
  disciplinas; B conta as médias abaixo de 6; C troca os pesos; E usa a média simples.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "uma filial compra 10 kg de arroz, 5 kg de feijão e
  4 L de óleo; o fornecedor cobra R$ 5, R$ 9 e R$ 8. Como fazer essa conta para várias
  filiais e vários fornecedores de uma vez? Multiplicando matrizes, e essa conta NÃO é
  casa com casa. Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: duas folhas transparentes (matrizes A e B) deslizando uma sobre a
  outra; cada casa acende junto com a de baixo, e o resultado aparece numa terceira
  folha.
- No 3 · A, um "carimbo ×3" batendo em cada casa, uma por uma, até a última.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- As seis médias da Questão 8 estão corretas (6,2; 6,2; 5,8; 6,4; 6,0; 5,4)?
- O 6,0 foi contado como aprovado ("maior ou igual")?
- Ficou claro que só a soma (não a multiplicação de matrizes) é casa com casa?
```

---

## Vídeo 3: Multiplicação de matrizes (linha por coluna)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Álgebra — Matrizes e Operações — Episódio 3 de 5:
Multiplicação de matrizes: linha por coluna
RECORTE: use APENAS a seção 05 do material de apoio e a parte da seção 08 sobre a matriz
de ligações (A² conta rotas com uma escala), mais as Questões 3, 2 e 7 da seção 12.
As propriedades (AB ≠ BA) e a inversa ficam para o episódio 4.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pelo cupom do supermercado: quantidade de cada
   item vezes o preço de cada item, tudo somado no total. Só depois mostre as matrizes.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (produto de matrizes, linha vezes coluna, ordem do produto, matriz de
   ligações, escala, A²).
3. Analogias âncora, retomadas ao longo da aula:
   - "linha vezes coluna é o caixa do supermercado: cada quantidade encontra o seu
     preço, e o caixa soma tudo num número só";
   - "a regra do dominó: em (2 × 3) · (3 × 2), os números de DENTRO precisam encaixar
     como peças de dominó; os de FORA dão o tamanho do resultado";
   - "o endereço do resultado diz quem multiplica quem: c_21 é a linha 2 da primeira
     com a coluna 1 da segunda".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: o endereço a_ij e
   "linha = o que, coluna = o quê" (episódio 1).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; destaque na tela a
   linha da primeira matriz e a coluna da segunda, em cores diferentes, a cada produto.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "10 · 5 + 5 · 9 + 4 · 8 = 127. É o gasto de uma filial de
  restaurante num fornecedor. Essa conta de cupom de supermercado é, sozinha, toda a
  multiplicação de matrizes."
- Promessa: "ao final, você vai saber se um produto de matrizes existe, qual o tamanho
  dele e o que cada número do resultado significa no problema".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) por que a regra é "estranha": a filial (10, 5, 4) e o fornecedor (5, 9, 8) dão 127;
  b) a regra: c_ij = linha i de A vezes coluna j de B, termo a termo, somando. Exemplo
     com A = (1 2 3 / 0 1 4) e B = (2 4 / 1 0 / 0 5): c_11 = 1·2 + 2·1 + 3·0 = 4;
     c_12 = 1·4 + 2·0 + 3·5 = 19; c_21 = 0·2 + 1·1 + 4·0 = 1;
     c_22 = 0·4 + 1·0 + 4·5 = 20;
  c) quando existe e que tamanho tem: A (m × n) · B (n × p) = C (m × p); 2 × 3 vezes
     3 × 2 dá 2 × 2; 3 × 2 vezes 3 × 2 não existe;
  d) calcule só o elemento pedido: "quanto a filial 2 gasta no fornecedor 1" é só c_21;
  e) matriz de ligações: a_ij = 1 se há voo direto de i para j; (A²)_ij soma um 1 para
     cada cidade k que liga i a k e k a j, ou seja, conta as rotas com uma escala.
- Exercício "nós fazemos": peça "pause: quanto é (2 1 / 0 3) vezes a coluna (1 / 4)?
  E qual é a ordem do resultado?" ((2 × 2) · (2 × 1) = 2 × 1; resultado (2·1 + 1·4 /
  0·1 + 3·4) = (6 / 12)).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Linha da primeira vezes coluna da segunda, e soma."
  "Os números de dentro encaixam; os de fora dão o tamanho."
  "c_ij é a linha i com a coluna j."
- Erros clássicos:
  • multiplicar posição com posição, como na soma;
  • achar que (2 × 3) · (2 × 3) existe.
- Questões no estilo ENEM, nesta ordem:
  • Questão 3 do material (A 2 × 3, B 3 × 4, C 4 × 2): "eu faço", em dois passos
    (2 × 3)(3 × 4) = 2 × 4 e (2 × 4)(4 × 2) = 2 × 2; mostre que a A para no primeiro
    produto e que a D exige ordens iguais sem necessidade;
  • Questão 2 (duas filiais, dois fornecedores): "nós fazemos"; Q · P dá 127, 131, 110 e
    108; cada filial escolhe o seu mais barato: 127 + 108 = 235; a A mistura
    fornecedores (215), o que o enunciado proíbe; C, D e E escolhem errado;
  • Questão 7 (voos entre quatro cidades): "você faz", com pausa; (A²)_14 = 2, as rotas
    1 → 2 → 4 e 1 → 3 → 4; a A lê o voo direto, a B confunde com rotas de duas escalas
    (há uma só: 1 → 2 → 3 → 4), a D soma as duas contagens e a E soma a linha 1 inteira
    de A² (4).
  Em todas: confira as ordens, rotule linha e coluna, resolva e explique as alternativas
  erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "com números, 2 × 3 é igual a 3 × 2. Com matrizes,
  AB é igual a BA? E dá para 'desfazer' uma multiplicação, como a divisão desfaz a
  multiplicação? Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: a linha de A "deitada" girando 90° e encaixando ao lado da coluna
  de B; os pares se multiplicam um a um e caem numa soma, que vira o número do
  resultado, na casa que acende no endereço certo.
- As ordens escritas como peças de dominó: (2 × 3)(3 × 2) encaixa; (3 × 2)(3 × 2) não
  encaixa e a peça é rejeitada com um selo vermelho.
- Um mapa com quatro cidades e setas de voo; as duas rotas com escala de 1 para 4
  acendem uma de cada vez.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Os quatro elementos do exemplo da seção 05 (4, 19, 1, 20) estão corretos?
- Na Questão 2, a resposta é 235 e a alternativa 215 foi explicada como proibida?
- A regra da ordem (dentro iguais, fora dá o tamanho) foi aplicada nos dois passos da
  Questão 3?
```

---

## Vídeo 4: O que muda em relação aos números e a matriz inversa

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Álgebra — Matrizes e Operações — Episódio 4 de 5:
O que muda em relação aos números e a matriz inversa
RECORTE: use APENAS as seções 06 e 07 do material de apoio, mais as Questões 4, 9 e 6 da
seção 12. O número ad − bc será chamado de determinante e estudado na série seguinte,
Determinantes e sistemas lineares: aqui, só a fórmula da inversa 2 × 2.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por ações em que a ordem importa (calçar a meia e
   depois o sapato × o sapato e depois a meia) e por um cadeado de segredo: quem tranca
   precisa de uma chave para destrancar.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (comutativa, associativa, distributiva, matriz identidade, matriz inversa,
   matriz-chave, codificar, decodificar).
3. Analogias âncora, retomadas ao longo da aula:
   - "multiplicar matrizes é como meia e sapato: a ordem muda o resultado";
   - "a identidade é o número 1 das matrizes: multiplicar por ela não muda nada";
   - "a inversa é a chave do cadeado: A tranca a mensagem, A⁻¹ destranca. Receita 2 × 2:
     troca a diagonal, muda o sinal da secundária, divide por ad − bc".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: multiplicação linha por
   coluna (episódio 3); a identidade e a transposta (episódio 1).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; toda inversa calculada
   é conferida na tela, multiplicando pela original até aparecer a identidade.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Nos números, se um produto dá zero, um dos fatores é zero. Nas
  matrizes, não: (1 1 / 1 1) vezes (1 −1 / −1 1) dá a matriz nula, e nenhuma das duas é
  nula."
- Promessa: "ao final, você vai saber quais regras dos números valem para matrizes e vai
  calcular a inversa de uma 2 × 2 para decifrar um código".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) AB ≠ BA em geral: (1 2 / 0 1)(1 0 / 3 1) = (7 2 / 3 1), mas
     (1 0 / 3 1)(1 2 / 0 1) = (1 2 / 3 7); às vezes um dos produtos nem existe (A 2 × 3
     e B 3 × 4: existe AB, não BA);
  b) produto nulo sem fator nulo; por isso não se "corta" A em AB = AC;
  c) a tabela de propriedades da seção 06: A · I = I · A = A; associativa; distributiva
     mantendo o lado; (AB)^t = B^t A^t, com a ordem invertida; (A + B)² = A² + AB + BA +
     B², e não A² + 2AB + B²;
  d) a inversa: A · A⁻¹ = A⁻¹ · A = I; só existe para quadradas, e nem toda quadrada tem;
  e) a receita 2 × 2 com A = (3 1 / 5 2): ad − bc = 6 − 5 = 1; A⁻¹ = (2 −1 / −5 3);
     conferência (3 1 / 5 2)(2 −1 / −5 3) = (1 0 / 0 1); se ad − bc = 0, não há inversa
     ("esse número tem nome e série própria: determinante");
  f) códigos: a mensagem vira colunas de números, multiplica-se pela chave A, e quem
     recebe multiplica por A⁻¹; erro de sinal na inversa decifra lixo.
- Exercício "nós fazemos": peça "pause: calcule a inversa de (2 1 / 3 2) e confira"
  (ad − bc = 4 − 3 = 1; inversa (2 −1 / −3 2); o produto com a original dá (1 0 / 0 1)).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "A ordem dos fatores altera o produto."
  "Produto zero não exige fator zero."
  "Inversa 2 × 2: troca a diagonal, muda o sinal da secundária, divide por ad − bc."
- Erros clássicos:
  • supor AB = BA;
  • concluir de AB = 0 que A = 0 ou B = 0;
  • calcular a inversa só trocando a diagonal, sem mudar sinais nem dividir.
- Questões no estilo ENEM, nesta ordem:
  • Questão 4 do material (AB − BA): "eu faço"; resultado (6 0 / 0 −6); a A supõe
    AB = BA, a C calcula BA − AB, a D é A − B;
  • Questão 9 (a única propriedade verdadeira): "nós fazemos"; A · I = I · A = A; cada
    falsa é derrubada por um bloco desta aula;
  • Questão 6 (decifrar E = (17 / 29) com a chave (3 1 / 5 2)): "você faz", com pausa;
    M = A⁻¹ · E = (5 / 2), com conferência 3·5 + 1·2 = 17 e 5·5 + 2·2 = 29; a B troca os
    sinais da diagonal principal (−5 e −2), a C só troca a diagonal (63 e 172), a E
    multiplica de novo por A (80 e 143) e a A inverte a ordem.
  Em todas: leia o enunciado, resolva, confira e explique as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "no último episódio deste assunto, juntamos tudo,
  caçamos as pegadinhas e treinamos com questões inéditas."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: a receita da inversa em três movimentos sobre a matriz
  (3 1 / 5 2): os elementos 3 e 2 trocam de lugar; 1 e 5 ganham um sinal de menos;
  tudo é dividido por 1; em seguida, o produto com a original vira a identidade com um
  selo verde "confere".
- Um cadeado com a mensagem: a matriz A tranca, a matriz A⁻¹ destranca; com a inversa
  errada, a mensagem sai embaralhada.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- AB = (7 2 / 3 1) e BA = (1 2 / 3 7) estão corretos?
- A inversa (2 −1 / −5 3) foi conferida multiplicando pela original?
- Na Questão 6, a resposta é 5 e 2, de cima para baixo?
```

---

## Vídeo 5: Revisão (Matrizes no ENEM)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula de REVISÃO para o YouTube sobre:

TEMA: Matemática — Álgebra — Matrizes e Operações — Episódio 5 de 5:
Revisão geral, estratégia de prova, pegadinhas e treino para o ENEM
RECORTE: use as seções 01, 09, 10, 11 e 13 do material de apoio.
NÃO reutilize as Questões 1 a 9 da seção 12 (já resolvidas nos episódios anteriores).
Determinantes e sistemas na forma A · X = B terão série própria (a próxima): aqui, só
cite a ponte.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que assistiu aos episódios 1 a 4, mas ainda é iniciante e pode ter esquecido
partes. Relembre cada conceito em uma frase simples antes de cobrá-lo.

REGRAS DE EXPLICAÇÃO
1. Cada conceito é relembrado com a mesma analogia âncora usada no seu episódio:
   o assento do cinema (fileira antes da poltrona); a tabela de mão dupla como espelho;
   linha = o que o time fez, coluna = o que sofreu; as folhas transparentes da soma; o
   aumento geral do número vezes matriz; o caixa do supermercado (linha vezes coluna);
   a regra do dominó das ordens; meia e sapato (a ordem importa); a identidade como o
   número 1; a inversa como chave do cadeado.
2. Prática de recuperação: antes de explicar, PERGUNTE e peça para o aluno pausar.
3. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
4. Uma ideia por cena. Frases curtas. Tom de conversa, falando com "você".

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "No ENEM, a matriz quase nunca vem com esse nome. Ela vem como
  tabela de jogos, de distâncias, de compras ou como foto digital. Hoje você treina a
  reconhecer o disfarce."
- O que a prova cobra (seção 01): ler o endereço, multiplicar com sentido, decidir se a
  conta existe, imagens e códigos; o que rende mais: saber o que cada elemento do
  produto representa.
- Onde aparece nas outras áreas (seção 10): tecnologia (pixels), economia (planilhas de
  quantidade × preço), nutrição (porções × nutrientes), Geografia (tabelas de distância
  e redes) e sistemas lineares na forma A · X = B (próxima série).
- A estratégia de prova em 4 hábitos (seção 09): rotular linhas e colunas antes de
  calcular; conferir as ordens antes de multiplicar; calcular só o elemento pedido;
  conferir a inversa multiplicando.
- "Verdadeiro ou falso? Pause e responda": transforme em afirmações os 9 erros da seção
  11 (a_23 é linha 3, coluna 2; multiplicar é posição com posição; (2 × 3) · (2 × 3)
  existe; AB = BA; AB = 0 obriga um fator nulo; a inversa é só trocar a diagonal; a
  transposta de uma 2 × 3 é 2 × 3; coluna = gols marcados; 3 · A multiplica só a
  primeira linha). Para cada um: pausa → resposta → por que a pegadinha engana → a
  regra certa em uma frase.
- 5 questões INÉDITAS no estilo ENEM, com 5 alternativas cada (as erradas são os erros
  clássicos). Use exatamente estes dados e confira as contas na tela:
  1) Leitura de tabela: V = (12 8 15 / 10 14 6 / 7 11 13), em que v_ij é o número de
     unidades vendidas pelo vendedor i no mês j. Total vendido no mês 2 pelos três
     vendedores: A) 14 B) 30 C) 33 D) 35 E) 96. Gabarito C (coluna 2: 8 + 14 + 11 = 33);
     B soma a linha 2; A é só v_22; D soma a linha 1; E soma a tabela inteira.
  2) Equação de matrizes: 2X + A = B, com A = (1 4 / 2 0) e B = (5 6 / 4 8). A soma dos
     elementos de X é: A) 4,5 B) 8 C) 9 D) 15 E) 16. Gabarito B (X = (B − A) ÷ 2 =
     (2 1 / 1 4)); E esquece de dividir por 2; D faz (B + A) ÷ 2; C faz B − 2A; A faz
     B ÷ 2 − A.
  3) Produto em contexto: Q = (2 1 / 1 3) dá as porções de arroz (coluna 1) e de feijão
     (coluna 2) nas refeições 1 e 2 (linhas); N = (3 28 / 7 15) dá, por porção, os gramas
     de proteína (coluna 1) e de carboidrato (coluna 2) do arroz (linha 1) e do feijão
     (linha 2). A proteína da refeição 2, em gramas, é: A) 10 B) 13 C) 16 D) 24 E) 73.
     Gabarito D (linha 2 de Q vezes coluna 1 de N: 1·3 + 3·7 = 24); A soma as proteínas
     sem as porções; B é a refeição 1; C troca as porções entre os alimentos
     (1·7 + 3·3); E usa a coluna dos carboidratos.
  4) Quando o produto existe: A é 3 × 2, B é 2 × 4 e C é 3 × 4. A única operação possível
     é: A) B · A B) A + B C) A · B + C D) C · A E) A · C. Gabarito C (A · B é 3 × 4 e
     pode ser somada com C); nas outras, os números de dentro não encaixam ou as ordens
     não são iguais.
  5) Código com inversa: chave A = (2 1 / 5 3), mensagem recebida E = (7 / 18). Os
     números originais, de cima para baixo: A) 1 e 3 B) 3 e 1 C) −3 e −1 D) 39 e 71
     E) 32 e 89. Gabarito B (ad − bc = 6 − 5 = 1; A⁻¹ = (3 −1 / −5 2); M = (21 − 18 /
     −35 + 36) = (3 / 1); conferência 2·3 + 1 = 7 e 5·3 + 3·1 = 18); C troca os sinais da
     diagonal principal; D só troca a diagonal; E multiplica de novo por A; A inverte a
     ordem.
  Leia, peça a pausa, rotule linha e coluna, resolva, confira e explique cada
  alternativa.
- Checklist de domínio (seção 13): leia os itens e diga "marque só o que você
  conseguiria explicar em voz alta para outra pessoa, sem consultar nada; o que não
  marcou, reveja o episódio correspondente" (endereço, tipos, tabelas: episódio 1;
  soma, número e igualdade: episódio 2; produto e A²: episódio 3; propriedades e
  inversa: episódio 4).
- Meta antes de considerar dominado: resolver 25 questões e acertar pelo menos 18, com
  pelo menos oito de leitura de tabela e cinco de produto em contexto.
- Encerramento e ponte: "o próximo assunto é Determinantes e sistemas lineares: o número
  ad − bc da inversa ganha nome e passa a decidir se um sistema tem uma solução, nenhuma
  ou infinitas."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Use um cronômetro visual nas pausas; um selo "PEGADINHA" em amarelo nos erros; um
  ícone de tabela em cada questão inédita; os 4 ícones dos episódios (poltrona de
  cinema, folhas transparentes, cupom de supermercado, cadeado) como índice visual da
  revisão.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Cada conceito foi relembrado antes de ser cobrado?
- As 5 questões inéditas têm uma única alternativa correta e contas corretas?
- Na questão 5, a inversa (3 −1 / −5 2) foi conferida e a resposta é 3 e 1?
```

---

## Cuidados ao revisar os roteiros

- **Multiplicação casa a casa:** a IA às vezes "multiplica" matrizes posição com posição (como na soma). Confira no vídeo 3 que (1 2 3 / 0 1 4) · (2 4 / 1 0 / 0 5) dá (4 19 / 1 20), e que no vídeo 2 só a soma e o número vezes matriz são feitos casa a casa.
- **Questão 7 (rotas):** a resposta é 2 (rotas 1 → 2 → 4 e 1 → 3 → 4). O valor 1 é o número de rotas com **duas** escalas, não "uma das escalas"; e 4 é a soma da linha 1 de A², não o elemento (A²)₁₄.
- **Questão 2:** a resposta é 235 (cada filial no seu fornecedor mais barato: 127 + 108). A IA tende a escolher 215 (o item mais barato de cada fornecedor), que o enunciado proíbe.
- **Inversa:** troca a **diagonal principal**, muda o sinal da **secundária**. Em (3 1 / 5 2) a inversa é (2 −1 / −5 3); se aparecer (−2 1 / 5 −3) ou (2 1 / 5 3), está errado.
- A seção 02 do material cita "no cabeçalho, a₂₃ = 9 e a₃₂ = 3", que vem de uma imagem que a IA de vídeo talvez não veja; por isso o vídeo 1 usa o exemplo próprio a_ij = i + 2j.
