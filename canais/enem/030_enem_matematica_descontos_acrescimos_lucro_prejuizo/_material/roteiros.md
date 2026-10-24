# Descontos, Acréscimos, Lucro e Prejuízo — série de videoaulas

Material de apoio: `01-matematica/15-descontos-acrescimos-lucro-prejuizo.html` · Incidência: Média

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Fator (1 + i), descontos sucessivos, voltar ao valor original, +20% e −20% não se anulam (seção 02 e parte da 06) | **Porcentagem** (série 09) | Revisão relâmpago de 30 s no início do vídeo 2. O foco é o novo: **base custo × base venda**, margem e markup, formação de preço, imposto sobre a venda, promoções, faixas e remarcações. |
| **Questão 3 do material** (30% de liquidação + 10% no Pix → 37%) | Igual à **Questão 6 de Porcentagem** (30% + 10% no caixa → 37%) | **Não uso.** No lugar dela entra uma questão nova (etiqueta de R$ 300,00, −20%, −5% no Pix, +10% de frete), com o texto completo no prompt do vídeo 2. |
| Questão 6 (R$ 102,00 depois de 15% de desconto) | Mesma ideia do exemplo "R$ 150,00 com 20% de desconto" de Porcentagem (seção 07), que lá não era questão | Mantida como "nós fazemos", apresentada como revisão aplicada. |
| Desconto por faixa | **Função modular e funções definidas por partes** (29) | Só citada ("isso tem série própria"). |
| Desconto à vista, "parcelado sem juros" | **Empréstimos** (17) e **Comparação de propostas** (18) | Só citado e prometido. |

## Plano: 4 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Lucro e prejuízo: porcentagem de quê? Margem e formação do preço** | 03, 04, 05 | Q1, Q2, Q7 | 10–12 min |
| **2. Descontos encadeados, preço original, promoções e faixas** | 02, 06, 07 | Nova (no lugar da Q3), Q6, Q5, Q8 | 10–12 min |
| **3. Remarcações, liquidações e o lucro que sobra** | 08 | Q9, Q4 | 6–8 min |
| **4. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Vídeo 1: Lucro e prejuízo: porcentagem de quê? Margem e formação do preço

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática Básica — Descontos, Acréscimos, Lucro e Prejuízo — Episódio 1 de 4:
Lucro e prejuízo: porcentagem de quê? Margem e formação do preço
RECORTE: use APENAS as seções 03, 04 e 05 do material de apoio, mais as Questões 1, 2 e 7
da seção 12. Calcular "quanto por cento" e o fator de multiplicação já foram ensinados na
série de Porcentagem: aqui, revisão rápida. Descontos encadeados e promoções ficam para o
episódio 2; remarcações, para o episódio 3.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma situação de balcão (uma mochila comprada
   no atacado por R$ 80,00 e vendida na loja por R$ 100,00; uma artesã que precisa
   decidir o preço de uma peça; um revendedor de aplicativo que paga taxa sobre cada
   venda) e só depois apresente as definições.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (preço de custo, preço de venda, lucro, prejuízo, base da porcentagem, margem
   sobre o custo ou markup, margem sobre a venda, comissão, lucro líquido).
3. Analogias âncora, retomadas ao longo da aula:
   - "toda porcentagem tem dono: antes de calcular, pergunte 'por cento DE QUÊ?' — do
     custo, da venda, da etiqueta";
   - "o preço de venda é uma pizza: uma fatia é lucro, o resto paga o custo. A fatia do
     lucro nunca pode ser a pizza inteira, por isso a margem sobre a venda nunca chega a
     100%";
   - "markup é o que se põe EM CIMA do custo (pode ser 150%, 300%); margem sobre a venda
     é o pedaço DENTRO do preço".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: "que porcentagem a parte
   representa? Divida a parte pelo todo" e o fator 1 + p/100 (série de Porcentagem).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; escreva na tela, ao
   lado de cada porcentagem, a sua base ("25% do CUSTO", "20% da VENDA"). No fim de cada
   conta, confira em reais: lucro em reais dividido pela base pedida.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Comprei por R$ 80,00 e vendi por R$ 100,00. Lucrei 25% ou 20%?
  As duas respostas estão certas, e o ENEM coloca as duas nas alternativas. Só uma
  responde à pergunta que ele fez."
- Promessa: "ao final, você vai calcular lucro e prejuízo na base certa e formar o preço
  de venda para qualquer margem, sem cair na armadilha da base".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) custo (C), venda (V) e lucro L = V − C; se L < 0, prejuízo de C − V; em reais não há
     ambiguidade;
  b) o mesmo lucro em duas bases: R$ 20,00 é 20 ÷ 80 = 25% do custo e 20 ÷ 100 = 20% da
     venda; sem aviso, a convenção é o custo, mas o ENEM costuma dizer a base;
  c) prejuízo também tem base: comprou por 120, vendeu por 90 → prejuízo de 30 = 25% do
     custo e cerca de 33,3% da venda;
  d) markup × margem sobre a venda: "vender pelo dobro" é 100% sobre o custo e 50% sobre
     a venda; a margem sobre a venda é sempre a menor das duas e nunca chega a 100%;
  e) converter as margens: sobre a venda = sobre o custo ÷ (1 + sobre o custo)
     (0,25 ÷ 1,25 = 0,20); sobre o custo = sobre a venda ÷ (1 − sobre a venda)
     (0,20 ÷ 0,80 = 0,25);
  f) formar o preço: custo R$ 72,00 e margem de 20% → sobre o custo, multiplique
     (72 · 1,20 = R$ 86,40); sobre a venda, divida (72 ÷ 0,80 = R$ 90,00), porque, se 20%
     do preço é lucro, os outros 80% são o custo; conferir: 18 ÷ 90 = 20%;
  g) imposto e comissão sobre a venda funcionam igual: se 15% do preço vai embora, o
     comerciante fica com 85%; para receber R$ 510,00, vende por 510 ÷ 0,85 = R$ 600,00.
- Exercício "nós fazemos": peça "pause: um produto custa R$ 50,00 e é vendido por
  R$ 80,00. Qual é o lucro sobre o custo e qual é o lucro sobre a venda?" (lucro de
  R$ 30,00; 30 ÷ 50 = 60% sobre o custo; 30 ÷ 80 = 37,5% sobre a venda; confira pela
  conversão: 0,6 ÷ 1,6 = 0,375).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Toda porcentagem tem dono: escreva a base antes de calcular."
  "Margem sobre o custo, multiplique; margem sobre a venda, divida por 1 − m."
  "Lucro sobre a venda nunca chega a 100%."
- Erros clássicos:
  • lucro sobre a venda dividindo pelo custo (R$ 20,00 em venda de R$ 100,00 é 20% da
    venda e 25% do custo);
  • margem sobre a venda multiplicando o custo (custo 60 com 25% sobre a venda dá 80,
    não 75);
  • descontar imposto da margem em pontos percentuais (imposto sobre a venda e lucro
    sobre o custo têm bases diferentes: calcule em reais);
  • margem sobre a venda acima de 100% (impossível: elimine a alternativa).
- Questões no estilo ENEM, nesta ordem:
  • Questão 1 do material (mochila de R$ 120,00 vendida por R$ 150,00): "eu faço",
    mostrando que a A é a base venda, a C confunde R$ 30,00 com 30%, e D e E são as
    razões custo/venda e venda/custo (o fator 1,25 lido como 125%);
  • Questão 2 (artesã, custo R$ 60,00, lucro de 25% do preço): "nós fazemos", com a
    conferência 20 ÷ 80 = 25%;
  • Questão 7 (compra 400, vende 600, 10% de imposto e 5% de comissão sobre a venda):
    "você faz", com pausa; mostre que a C (35%) subtrai pontos percentuais de bases
    diferentes e que a A divide pela venda.
  Em todas: leia o enunciado, sublinhe a base de cada porcentagem, resolva, confira em
  reais e explique as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "uma loja dá 20% de liquidação, mais 5% no Pix, e cobra
  10% de frete. No fim, você paga 15% a menos? Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: o mesmo lucro de R$ 20,00 como uma barrinha colocada primeiro em
  cima da barra do custo (80 → "25%") e depois dentro da barra da venda (100 → "20%"),
  com a etiqueta "DONO: custo" / "DONO: venda" trocando.
- A pizza do preço de venda: a fatia do lucro crescendo, mas nunca passando da pizza
  inteira; ao lado, uma pilha "em cima do custo" que pode crescer sem limite (markup).
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- A base de cada porcentagem aparece escrita na tela em todas as contas?
- A margem sobre a venda foi calculada DIVIDINDO por 1 − m (72 ÷ 0,80 = 90; 60 ÷ 0,75 = 80)?
- A Questão 7 deu 27,5% (110 ÷ 400), com imposto e comissão calculados sobre os R$ 600,00?
```

---

## Vídeo 2: Descontos encadeados, preço original, promoções e faixas

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática Básica — Descontos, Acréscimos, Lucro e Prejuízo — Episódio 2 de 4:
Descontos encadeados, preço original, promoções e descontos por faixa
RECORTE: use APENAS as seções 02, 06 e 07 do material de apoio, mais as Questões 6, 5 e
8 da seção 12 e a QUESTÃO NOVA escrita abaixo. NÃO use a Questão 3 do material: ela é
igual a uma questão já resolvida na série de Porcentagem. Fatores, descontos sucessivos,
voltar ao valor original e "+20% e −20% não se anulam" já foram ensinados na série de
Porcentagem: aqui, revisão em 30 segundos. O conteúdo novo é o contexto comercial com
acréscimo no meio (frete, imposto), o desconto total equivalente, as promoções
traduzidas em desconto efetivo e os descontos por faixa.
DURAÇÃO: 10 a 12 minutos

QUESTÃO NOVA (use no lugar da Questão 3 do material):
"Um produto tem preço de etiqueta de R$ 300,00. Na liquidação, há 20% de desconto; quem
paga com Pix ganha mais 5% de desconto sobre o valor já reduzido; e a entrega acrescenta
10% de frete sobre o valor pago pelo produto. O cliente que compra com Pix e com entrega
paga, no total,
A) R$ 228,00.  B) R$ 247,50.  C) R$ 250,80.  D) R$ 255,00.  E) R$ 258,00."
Gabarito: C. Resolução: 300 · 0,80 · 0,95 · 1,10 = 300 · 0,836 = R$ 250,80. A esquece o
frete (300 · 0,80 · 0,95 = 228); B soma os descontos (25%) e depois aplica o frete
(300 · 0,75 · 1,10 = 247,50); D soma tudo (−20 − 5 + 10 = −15%, 300 · 0,85 = 255); E
calcula o frete sobre a etiqueta (228 + 30 = 258), e não sobre o valor pago.

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por um carrinho de compras on-line (preço de
   etiqueta, cupom de liquidação, desconto no Pix, frete na tela final), por um cartaz
   de supermercado "leve 3, pague 2" e por uma loja de material de construção com
   "desconto progressivo".
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (fator, descontos encadeados, desconto total equivalente, desconto efetivo,
   promoção por quantidade, desconto por faixa ou progressivo).
3. Analogias âncora, retomadas ao longo da aula:
   - "cada desconto ou acréscimo é um carimbo no preço: carimbos se MULTIPLICAM, não se
     somam, e a ordem dos carimbos não muda o resultado";
   - "o desconto efetivo é a conta do caixa: quanto você paga dividido pelo que você
     leva";
   - "desconto por faixa é como encher andares de um prédio: cada andar do valor tem a
     sua taxa, e a taxa do último andar não desce para os de baixo".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los (série de Porcentagem):
   acréscimo de p% → × (1 + p/100); desconto de p% → × (1 − p/100); vários em sequência
   → produto dos fatores; voltar ao valor anterior → divida pelo fator
   (R$ 84,00 com 30% off → 84 ÷ 0,70 = 120); 20% e mais 10% dão 0,8 · 0,9 = 0,72, ou
   seja, 28%, não 30%.
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; escreva o fator ao lado
   de cada porcentagem e diga sobre que valor ela incide ("10% do valor JÁ descontado").
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Na mesma loja, 'segunda unidade com 50% de desconto' e '30% em
  cada unidade'. Qual é a melhor? A de 50% parece imbatível, mas dá só 25% de desconto.
  Hoje você aprende a desmascarar promoção."
- Promessa: "ao final, você vai encadear descontos e acréscimos, recuperar o preço
  original, comparar promoções e calcular descontos por faixa".
- Pré-requisitos relâmpago (revisão da série de Porcentagem).
- Blocos (um conceito por bloco):
  a) encadeados com acréscimo no meio: R$ 200,00 com 20% de liquidação, mais 10% no Pix,
     mais 10% de frete → 200 · 0,80 · 0,90 = 144 → 144 · 1,10 = R$ 158,40; em outra
     ordem (200 · 1,10 · 0,80 · 0,90) dá o mesmo;
  b) desconto total equivalente = 1 − (produto dos fatores): dois de 10% → 19%;
     25% e 20% → 1 − 0,75 · 0,8 = 40%;
  c) voltar ao preço: depois de +25%, basta −20% (1,25 · 0,8 = 1); subir 20% e descontar
     20% termina 4% abaixo (só cite: já visto em Porcentagem);
  d) promoções em desconto efetivo (tabela da seção 07): leve 3, pague 2 → 33,3%; leve 4,
     pague 3 → 25%; segunda com 50% → 1,5 de cada 2 → 25%; segunda grátis → 50%;
     segunda com 30% → 15%;
  e) a promoção só vale para a quantidade certa: com 4 unidades no "leve 3, pague 2", a
     quarta sai pelo preço cheio;
  f) desconto por faixa: nada até R$ 200,00, 5% entre 200 e 400, 10% acima de 400; numa
     compra de R$ 500,00, o desconto é 0 + 10 + 10 = R$ 20,00; aplicar 10% sobre tudo
     daria R$ 50,00, mais que o dobro do correto (funções por partes têm série própria).
- Exercício "nós fazemos": peça "pause: na promoção 'leve 5, pague 4', qual é o desconto
  efetivo?" (paga 4 de cada 5 → 1 − 4/5 = 20%).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Descontos e acréscimos em sequência: multiplique os fatores."
  "Para voltar ao preço original, divida pelo fator."
  "Toda promoção vira desconto efetivo antes da comparação."
- Erros clássicos:
  • somar descontos sucessivos (30% e 10% dão 37%, não 40%);
  • voltar ao preço original somando o desconto (R$ 102,00 após 15% de desconto vinham
    de 102 ÷ 0,85 = 120);
  • ler "50% na segunda" como 50% de desconto (é 25% sobre o par);
  • aplicar a taxa da faixa mais alta sobre o valor todo.
- Questões no estilo ENEM, nesta ordem:
  • QUESTÃO NOVA (etiqueta de R$ 300,00, liquidação, Pix e frete): "eu faço", com o
    fator total 0,836 e cada distrator explicado como no texto acima;
  • Questão 6 do material (camiseta de R$ 102,00 depois de 15% de desconto): "nós
    fazemos";
  • Questão 5 (6 unidades de R$ 12,00 em três lojas): "você faz", com pausa; calcule em
    reais (I: 48,00; II: 54,00; III: 50,40) e mostre de onde vem cada ordem errada;
  • Questão 8 (desconto progressivo em compra de R$ 600,00): "você faz", com pausa;
    mostre a compra dividida em três andares (200 + 200 + 200).
  Em todas: leia o enunciado, escreva os fatores, resolva, confira em reais e explique
  as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "uma loja coloca 50% sobre o custo na etiqueta e, na
  liquidação, dá um terço de desconto. Ela ainda lucra? Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: a tela final de um carrinho de compras em que cada linha (cupom,
  Pix, frete) "carimba" o preço com o seu fator (× 0,80, × 0,95, × 1,10) e o total vai
  mudando; depois os carimbos trocam de ordem e o total continua igual.
- Os pares de produtos da promoção "segunda com 50%": dois pacotes, um inteiro e um pela
  metade, e a conta 1,5 de 2 = 75% virando "desconto efetivo 25%".
- O prédio das faixas: três andares coloridos (0%, 5%, 10%) sendo preenchidos pela
  compra.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- A Questão 3 do material ficou de fora e a QUESTÃO NOVA dá R$ 250,80?
- A ordem da Questão 5 é I (R$ 48,00), III (R$ 50,40), II (R$ 54,00)?
- O desconto por faixa da Questão 8 é R$ 30,00 (pagou R$ 570,00), com cada taxa aplicada
  só à sua parte?
```

---

## Vídeo 3: Remarcações, liquidações e o lucro que sobra

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática Básica — Descontos, Acréscimos, Lucro e Prejuízo — Episódio 3 de 4:
Remarcações, liquidações e o lucro que sobra
RECORTE: use APENAS a seção 08 do material de apoio e a estratégia "trabalhe com um preço
de 100" da seção 09, mais as Questões 9 e 4 da seção 12. Lucro sobre o custo (episódio 1)
e fatores encadeados (episódio 2) são pré-requisitos: aqui, juntos.
DURAÇÃO: 6 a 8 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma loja de tênis em queima de estoque, com a
   etiqueta antiga riscada e a nova por cima, e por um lojista que vende dois celulares
   usados pelo mesmo preço.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (remarcação, etiqueta, liquidação, fator sobre o custo, resultado global).
3. Analogias âncora, retomadas ao longo da aula:
   - "leve tudo para a régua do custo: comece no custo e vá multiplicando os fatores até
     o preço final; o que passar de 1 é lucro, o que faltar é prejuízo";
   - "o custo vale 100: com 100 no começo, cada fator vira um número visível
     (100 → 160 → 112) e a resposta sai em porcentagem direto";
   - "no 'lucro em um, prejuízo em outro', o item do prejuízo era o mais caro: os mesmos
     20% pesam mais reais nele".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: lucro sobre o custo
   (episódio 1), multiplicar fatores e voltar ao valor dividindo pelo fator (episódio 2
   e série de Porcentagem).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; mostre sempre os dois
   caminhos (fatores e reais) e confira um pelo outro.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Uma loja põe 50% de lucro na etiqueta. Na liquidação, dá só
  33% de desconto. Sobrou 17% de lucro? Sobrou zero. Ela vendeu pelo preço de custo."
- Promessa: "ao final, você vai saber se uma remarcação seguida de liquidação ainda dá
  lucro e por que lucro e prejuízo de mesma porcentagem não empatam".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) a régua do custo: etiqueta com 50% sobre o custo e liquidação de 1/3 →
     1,5 · 2/3 = 1 → vendido exatamente pelo custo; um desconto de 33,3% anulou uma
     margem de 50% (a assimetria de sempre, agora com dinheiro de comerciante);
  b) o truque do 100: custo 100 → etiqueta 150 → liquidação 100;
  c) lucro em um, prejuízo em outro: dois itens vendidos pelo mesmo preço, um com p% de
     lucro e outro com p% de prejuízo sobre o custo → o resultado global é SEMPRE
     prejuízo; descubra cada custo dividindo o preço pelo fator e compare os totais.
- Exercício "nós fazemos": peça "pause: um produto custa R$ 40,00, vai para a etiqueta
  com 50% sobre o custo e entra numa liquidação de 30% sobre a etiqueta. Lucro ou
  prejuízo, e de quanto sobre o custo?" (1,5 · 0,7 = 1,05 → lucro de 5%; em reais:
  40 → 60 → 42, lucro de R$ 2,00, e 2 ÷ 40 = 5%).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Leve tudo para a régua do custo e multiplique os fatores."
  "Desconto menor pode anular margem maior."
  "Lucro de p% e prejuízo de p% no mesmo preço dão prejuízo."
- Erros clássicos:
  • achar que lucro de p% e prejuízo de p% se anulam (os custos são diferentes);
  • subtrair porcentagens de bases diferentes (margem de 60% menos liquidação de 30%
    não dá 30% de lucro);
  • ler o fator como lucro (fator 1,12 é lucro de 12%, não de 112%).
- Questões no estilo ENEM, nesta ordem:
  • Questão 9 do material (tênis de R$ 50,00, etiqueta com 60%, liquidação de 30%): "eu
    faço", pelos fatores (1,6 · 0,7 = 1,12) e em reais (50 → 80 → 56, lucro de R$ 6,00);
    mostre que B subtrai 60 − 30, C faz 60 · 0,7, D ignora a liquidação e E lê o fator;
  • Questão 4 (dois aparelhos de R$ 600,00, +20% e −20% sobre o custo): "você faz", com
    pausa; custos 600 ÷ 1,2 = 500 e 600 ÷ 0,8 = 750; custo total 1.250, venda 1.200 →
    prejuízo de R$ 50,00; explique que C e D aplicam 1,2 · 0,8 = 0,96 como se fosse um
    único produto reajustado duas vezes.
  Em todas: leia o enunciado, escreva os fatores sobre o custo, resolva, confira em
  reais e explique as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "no último episódio deste assunto, juntamos tudo,
  caçamos as pegadinhas e treinamos com questões inéditas."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: uma régua horizontal marcada "custo = 1"; uma seta sobe até 1,5
  (etiqueta) e outra desce até 1 (liquidação), com a etiqueta riscada de queima de
  estoque.
- Dois celulares lado a lado com o mesmo preço (R$ 600,00), cada um com o seu custo
  escondido aparecendo (R$ 500,00 e R$ 750,00) e uma balança pendendo para o prejuízo.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- O exemplo da etiqueta com 50% e liquidação de 1/3 termina em fator 1 (nem lucro, nem
  prejuízo)?
- A Questão 9 deu 12% e a Questão 4 deu prejuízo de R$ 50,00?
- Ficou claro por que o item do prejuízo pesa mais (custo maior)?
```

---

## Vídeo 4: Revisão (Descontos, acréscimos, lucro e prejuízo no ENEM)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula de REVISÃO para o YouTube sobre:

TEMA: Matemática Básica — Descontos, Acréscimos, Lucro e Prejuízo — Episódio 4 de 4:
Revisão geral, estratégia de prova, pegadinhas e treino para o ENEM
RECORTE: use as seções 01, 09, 10, 11 e 13 do material de apoio.
NÃO reutilize as Questões 1 a 9 da seção 12 nem a questão nova do episódio 2 (etiqueta de
R$ 300,00 com Pix e frete), já resolvidas nos episódios anteriores.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que assistiu aos episódios 1 a 3, mas ainda é iniciante e pode ter esquecido
partes. Relembre cada conceito em uma frase simples antes de cobrá-lo.

REGRAS DE EXPLICAÇÃO
1. Cada conceito é relembrado com a mesma analogia âncora usada no seu episódio:
   toda porcentagem tem dono; o preço de venda como pizza (a fatia do lucro nunca é a
   pizza inteira); markup em cima do custo × margem dentro do preço; os carimbos que se
   multiplicam; o desconto efetivo como conta do caixa; o prédio das faixas; a régua do
   custo; o custo que vale 100.
2. Prática de recuperação: antes de explicar, PERGUNTE e peça para o aluno pausar.
3. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
4. Uma ideia por cena. Frases curtas. Tom de conversa, falando com "você".

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Quase todo erro deste assunto é a conta certa feita sobre a
  base errada. Hoje você treina a única pergunta que importa: porcentagem de quê?"
- O que a prova cobra (seção 01): lucro e prejuízo em reais e em porcentagem, sobre o
  custo ou sobre a venda; preço de venda para uma margem; descontos e acréscimos
  encadeados; promoções traduzidas em desconto; descontos por faixa.
- Onde aparece nas outras áreas (seção 10): Ciências Humanas (carga tributária e
  imposto embutido no preço: o imposto é porcentagem do preço final ou do preço sem
  imposto?); leitura de gráficos e infográficos (variação percentual sobre qual valor);
  Matemática Financeira (desconto à vista e "parcelado sem juros", que voltam em
  Empréstimos e em Comparação de propostas); funções definidas por partes (descontos e
  tarifas por faixa, série própria).
- A estratégia de prova em 4 hábitos (seção 09): escrever a base ao lado de cada
  porcentagem; trabalhar com um preço de 100; desconfiar da soma de porcentagens de bases
  diferentes; conferir com o valor em reais no fim.
- "Verdadeiro ou falso? Pause e responda": transforme em afirmações os 9 erros da
  seção 11 (lucro sobre a venda dividindo pelo custo; margem sobre a venda multiplicando
  o custo; somar descontos sucessivos; voltar ao preço somando o desconto; "50% na
  segunda" como 50%; taxa da faixa mais alta sobre tudo; lucro e prejuízo de p% se
  anulam; descontar imposto da margem em pontos percentuais; margem sobre a venda acima
  de 100%). Para cada um: pausa → resposta → por que a pegadinha engana → a regra certa
  em uma frase.
- 5 questões INÉDITAS no estilo ENEM, criadas por você, com situações hipotéticas e
  5 alternativas cada:
  1) lucro sobre a VENDA: um item comprado por R$ 150,00 e vendido por R$ 200,00
     (resposta 25%; distratores: 33,3% sobre o custo, 50% lendo R$ 50,00 como 50%,
     75% = custo ÷ venda, 133% = venda ÷ custo);
  2) preço com taxa sobre a venda: uma doceira quer receber R$ 45,00 líquidos por bolo
     e o aplicativo de entrega fica com 25% do preço de venda (resposta R$ 60,00 =
     45 ÷ 0,75; distratores: 45 · 1,25 = 56,25; 45 + 25 = 70,00; 45 · 0,75 = 33,75;
     45 ÷ 0,25 = 180,00);
  3) comparar promoções para 4 unidades: "leve 4, pague 3", "segunda unidade com 30% de
     desconto" e "20% em tudo" (descontos efetivos 25%, 15% e 20%; a melhor é "leve 4,
     pague 3"; distrator: ler "30% na segunda" como 30% sobre tudo);
  4) desconto por faixa: nada até R$ 100,00, 10% entre R$ 100,00 e R$ 300,00, 20% acima
     de R$ 300,00, numa compra de R$ 450,00 (desconto 0 + 20 + 30 = R$ 50,00, paga
     R$ 400,00; distratores: 20% sobre tudo → 360,00; 30% sobre tudo → 315,00; só a
     faixa mais alta → 420,00; 20% sobre tudo o que passa de 100 → 380,00);
  5) remarcação e liquidação: etiqueta com 80% sobre o custo e liquidação de 40% sobre a
     etiqueta (1,8 · 0,6 = 1,08 → lucro de 8% sobre o custo; distratores: 40% = 80 − 40;
     48% = 80 · 0,6; 108% lendo o fator; "prejuízo, porque o desconto foi grande").
  As alternativas erradas devem ser exatamente os erros clássicos. Leia, peça a pausa,
  escreva a base de cada porcentagem, resolva, confira em reais e explique cada
  alternativa.
- Checklist de domínio (seção 13): leia os itens e diga "marque só o que você
  conseguiria explicar em voz alta para outra pessoa, sem consultar nada; o que não
  marcou, reveja o episódio correspondente" (bases, margem e formação de preço →
  episódio 1; fatores, preço original, promoções e faixas → episódio 2; remarcações e
  lucro/prejuízo cruzados → episódio 3).
- Meta antes de considerar dominado (a do material): resolver 20 questões de lucro,
  prejuízo e descontos e acertar pelo menos 14 (70%), escolhendo questões que misturem
  duas bases diferentes (lucro sobre o custo e imposto sobre a venda, por exemplo).
- Encerramento e ponte: "o próximo assunto é Taxas equivalentes e inflação: por que 10%
  ao mês não é 120% ao ano, e por que render 10% num ano de inflação de 10% não deixa
  ninguém mais rico."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Use um cronômetro visual nas pausas; um selo "PEGADINHA" em amarelo nos erros; uma
  etiqueta de preço com a pergunta "DE QUÊ?" em cada questão inédita; os 3 ícones dos
  episódios (pizza do preço, carimbos no carrinho, régua do custo) como índice visual
  da revisão.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Cada conceito foi relembrado antes de ser cobrado?
- As 5 questões inéditas têm uma única alternativa correta e contas corretas?
- Os 9 erros da seção 11 apareceram no "verdadeiro ou falso"?
```

---

## Cuidados ao revisar os roteiros

- **Margem sobre a venda (vídeo 1):** a IA tende a multiplicar. Custo R$ 72,00 com 20% sobre a venda dá **72 ÷ 0,80 = R$ 90,00**, não 72 · 1,20 = 86,40; na Q2, **60 ÷ 0,75 = R$ 80,00**, não 75. Confira sempre o lucro em reais dividido pelo preço de venda.
- **Questão 7 (vídeo 1):** imposto e comissão são **15% dos R$ 600,00 = R$ 90,00**; o lucro líquido é 510 − 400 = R$ 110,00 = **27,5% do custo**. A IA costuma fazer 50% − 15% = 35% (é o distrator C).
- **Questão 5 (vídeo 2):** "segunda unidade com 50%" é **25%** de desconto efetivo. Ordem certa: **I (R$ 48,00), III (R$ 50,40), II (R$ 54,00)**. Se a IA tratar a loja II como 50%, a ordem sai invertida.
- **Questão 4 (vídeo 3):** prejuízo de **R$ 50,00** (custos 500 + 750 = 1.250 contra 1.200 de venda). R$ 48,00 é o distrator de quem faz 1.200 · 0,96.
