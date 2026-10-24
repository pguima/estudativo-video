# Função Composta e Função Inversa — série de videoaulas

Material de apoio: `01-matematica/30-funcao-composta-inversa.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| "Caminho de volta" f(x) = k (táxi P = 5 + 2,5d, pagou R$ 30,00) | **Conceito de Função**, seção "o caminho de volta" e **Questão 9** | A Questão 3 daqui (táxi 4,5 + 2,5x) pede a **fórmula** da volta, não um número: uso, apresentada como "lá você voltou com um número; agora você monta a volta inteira". |
| Substituir uma expressão em f (f(2x) com f(x) = x² − 1) | **Conceito de Função**, Questão 7 | Revisão relâmpago antes de montar f(g(x)). |
| Lei afim, F = 1,8C + 32, táxi, taxa de variação | **Função Afim** | Revisão relâmpago; a inversa da afim é "desfazer na ordem contrária". |
| Descontos encadeados ("a ordem não importa") | **Descontos, acréscimos, lucro e prejuízo**, seção 02 | A Questão 6 (cupom × 10%) é o contraponto: dois percentuais comutam, mas cupom em reais + percentual **não**. Digo explicitamente que as duas aulas não se contradizem. |
| Exponencial e logaritmo como par inverso, espelho em y = x | **Função Logarítmica**, seção 02 | Só revisão: o par aparece como exemplo do espelho, sem reensinar logaritmo. |
| Progressão aritmética | Próxima série | Só a ponte no fim da revisão. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Composição: máquinas em fila e a ordem que importa** | 02, 03 | Q2, Q6 | 10–12 min |
| **2. Composição em contexto e a função escondida** | 04, 05 | Q1, Q4 | 8–10 min |
| **3. Função inversa: desfazer o caminho** | 06 (definição e f⁻¹ ≠ 1/f), 07 (receita), 08 (conversões) | Q3, Q8 | 10–12 min |
| **4. Quem tem inversa e o espelho na reta y = x** | 06 (bijetora, restringir domínio), 07 (gráfico), 08 (exp–log), 09 (tabelas) | Q7, Q5, Q9 | 10–12 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Vídeo 1: Composição (máquinas em fila e a ordem que importa)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Função Composta e Função Inversa — Episódio 1 de 5:
Composição: máquinas em fila e a ordem que importa
RECORTE: use APENAS as seções 02 e 03 do material de apoio, mais as Questões 2 e 6 da
seção 12. Calcular f(2x) substituindo a expressão já foi visto na série de Conceito de
Função; produtos notáveis ((a + b)²), na série de Expressões algébricas: aqui, revisão
rápida. Composição em contexto fica para o episódio 2; inversa, para os episódios 3 e 4.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma linha de produção com duas máquinas (a
   primeira corta, a segunda pinta) e pelo caixa de uma loja que aplica um cupom e um
   desconto. Só depois escreva f(g(x)).
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (função composta, f ∘ g, "f bola g", função de dentro, função de fora,
   comutativo, lei da composta).
3. Analogias âncora, retomadas ao longo da aula:
   - "máquinas em fila: o que sai da primeira entra na segunda";
   - "f(g(x)) se lê de dentro para fora: quem age primeiro é a de dentro";
   - "meia e sapato: a ordem muda o resultado".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: calcular f(5) trocando
   o x por 5, substituir uma expressão inteira entre parênteses (série de Conceito de
   Função) e (2x + 1)² = 4x² + 4x + 1 (série de Expressões algébricas e produtos
   notáveis).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; escreva na tela qual
   máquina está agindo em cada passo e coloque SEMPRE a expressão de dentro entre
   parênteses.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Produto de R$ 150,00, um cupom de R$ 20,00 e 10% de desconto.
  Tanto faz a ordem? Não: numa ordem você paga R$ 117,00, na outra R$ 115,00. Hoje você
  descobre por quê, e qual ordem pedir no caixa."
- Promessa: "ao final, você vai calcular f(g(x)) em um número e montar a lei da
  composta, sem trocar a ordem das máquinas".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) definição: (f ∘ g)(x) = f(g(x)), aplica g primeiro e f depois; só faz sentido se
     g(x) estiver no domínio de f;
  b) os valores passando pelas máquinas (seção 02): g(x) = 2x + 1 e f(x) = x² − 1;
     o 2 vira g(2) = 5, que vira f(5) = 24;
  c) "número antes de lei": se a pergunta é só f(g(3)), calcule g(3) e jogue o número
     em f;
  d) a lei da composta: f(g(x)) = (2x + 1)² − 1 = 4x² + 4x; g(f(x)) = 2(x² − 1) + 1 =
     2x² − 1; com x = 2, 24 e 7: f ∘ g ≠ g ∘ f;
  e) composição não é produto: f(2) · g(2) = 3 · 5 = 15, nada a ver com 24.
- Exercício "nós fazemos": peça "pause: com f(x) = 3x e g(x) = x + 4, calcule f(g(1)) e
  g(f(1))" (g(1) = 5 e f(5) = 15; f(1) = 3 e g(3) = 7: ordens diferentes, resultados
  diferentes).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "O que sai de uma máquina entra na outra."
  "Leia de dentro para fora: a de dentro age primeiro."
  "Trocou a ordem, trocou o resultado."
- Erros clássicos:
  • aplicar f primeiro em f(g(x));
  • achar que f ∘ g = g ∘ f;
  • multiplicar f(x) · g(x) em vez de substituir;
  • em f(2x + 1), elevar só o x ao quadrado (2x² + 1 − 1) em vez de (2x + 1)² − 1.
- Questões no estilo ENEM, nesta ordem:
  • Questão 2 do material (f(g(2)) com f(x) = x² − 1 e g(x) = 2x + 3): "eu faço",
    pelo caminho "número antes de lei" (g(2) = 7, f(7) = 48), mostrando que cada
    alternativa errada é um erro clássico (9 = ordem trocada; 10 = soma; 21 = produto;
    24 = (2x + 3)² sem o termo do meio);
  • Questão 6 (cupom de R$ 20,00 × 10% num produto de R$ 150,00): "você faz", com
    pausa. Monte c(p) = p − 20 e d(p) = 0,9p; d(c(150)) = 0,9 · 130 = 117 e
    c(d(150)) = 135 − 20 = 115; a porcentagem antes sai R$ 2,00 mais barato (D).
    Mostre a lei geral: d(c(p)) = 0,9p − 18 e c(d(p)) = 0,9p − 20 — com o cupom antes,
    os 10% incidem sobre um valor menor e o cupom "vale" só R$ 18,00. Faça a ponte:
    "na série de Descontos você viu que dois descontos percentuais podem vir em
    qualquer ordem (0,8 · 0,9 = 0,9 · 0,8). Isso continua certo: multiplicar comuta.
    O que não comuta é misturar um desconto em reais com um percentual."
  Em todas: leia o enunciado, diga "pause o vídeo e tente", resolva e explique as
  alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "uma fábrica faz 40 peças por hora, e cada peça custa
  R$ 3,00 mais um custo fixo. Qual é o custo em função das horas, sem passar pelas
  peças? Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: duas máquinas em fila, g (azul) e f (roxa); o número 2 entra em
  g, sai 5 numa esteira, entra em f e sai 24; depois as máquinas trocam de lugar e o
  mesmo 2 sai 7.
- O caixa da loja: uma etiqueta de R$ 150,00 passando pelo "carimbo do cupom" e pelo
  "carimbo dos 10%" nas duas ordens, com os preços finais lado a lado (117 × 115).
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Em todo f(g(x)), a função g foi aplicada primeiro?
- (2x + 1)² foi desenvolvido com o termo do meio (4x² + 4x + 1)?
- A diferença entre as ordens na Questão 6 é R$ 2,00 (e não R$ 18,00 nem R$ 20,00)?
```

---

## Vídeo 2: Composição em contexto e a função escondida

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Função Composta e Função Inversa — Episódio 2 de 5:
Composição em contexto: grandezas encadeadas e a função escondida
RECORTE: use APENAS as seções 04 e 05 do material de apoio, mais as Questões 1 e 4 da
seção 12. A ideia de custo fixo + custo por unidade já foi ensinada na série de Função
Afim: aqui, revisão rápida.
DURAÇÃO: 8 a 10 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pelo balão meteorológico subindo (quanto mais
   tempo, mais alto; quanto mais alto, mais frio) e por uma fábrica com um relógio na
   parede e uma pilha de peças.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (grandeza, grandeza intermediária, função de dentro, função de fora,
   substituir, incógnita).
3. Analogias âncora, retomadas ao longo da aula:
   - "máquinas em fila" (a mesma do episódio 1);
   - "a grandeza intermediária é a ponte: você atravessa por ela e ela some da
     resposta";
   - "a de dentro recebe o que você TEM; a de fora entrega o que você QUER".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: f(g(x)) de dentro para
   fora (episódio 1) e custo = fixo + preço por unidade × quantidade (série de Função
   Afim).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; escreva a UNIDADE de
   cada grandeza (minutos, km, °C, peças, reais) ao lado dela e confira a lei final com
   um número.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Um balão sobe 0,2 km por minuto, e a cada quilômetro o ar
  esfria 6 °C. Que temperatura ele encontra aos 10 minutos? Dá para responder com uma
  fórmula só, em que a altitude nem aparece."
- Promessa: "ao final, você vai juntar duas fórmulas de um enunciado numa só e
  descobrir uma função escondida dentro de uma composta".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) a estratégia: identificar a grandeza que aparece nas duas fórmulas e substituí-la;
  b) o balão (seção 04): h(t) = 0,2t e T(h) = 25 − 6h; T(h(t)) = 25 − 1,2t; aos
     10 min, 13 °C; a altitude sumiu;
  c) a tabela das cadeias (tempo → peças → custo; tempo → altitude → temperatura;
     dólar → real → imposto) e a dica "a de dentro recebe o que você tem";
  d) caso 1, conheço a de fora (seção 05): f(x) = 3x − 2 e f(g(x)) = 6x + 7; trate g(x)
     como incógnita: 3g(x) − 2 = 6x + 7 → g(x) = 2x + 3;
  e) caso 2, conheço a de dentro: g(x) = x + 1 e f(g(x)) = x² + 2x; troque u = x + 1,
     x = u − 1: f(u) = u² − 1;
  f) "sempre confira": monte de novo a composta com a função encontrada.
- Exercício "nós fazemos": peça "pause: uma gráfica imprime p(t) = 50t páginas em
  t minutos, e o custo de p páginas é C(p) = 20 + 0,1p reais. Qual é o custo em função
  do tempo, e quanto custam 10 minutos de impressão?" (C(p(t)) = 20 + 5t; aos 10 min,
  500 páginas, R$ 70,00 pelos dois caminhos).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "A grandeza que aparece nas duas fórmulas é a ponte."
  "Substitua a ponte e ela some da resposta."
  "Achou a função escondida? Monte a composta de novo e confira."
- Erros clássicos:
  • compor na ordem errada (aplicar a fórmula das peças ao custo);
  • somar os coeficientes em vez de multiplicar (40 + 3 em vez de 40 · 3);
  • esquecer o custo fixo;
  • parar em 3g(x) = 6x + 9 sem dividir por 3, ou passar o −2 sem trocar o sinal.
- Questões no estilo ENEM, nesta ordem:
  • Questão 1 do material (n(t) = 40t peças; C(n) = 500 + 3n): "eu faço", com a
    conferência em 2 horas (80 peças, R$ 740,00);
  • Questão 4 (f(x) = 3x − 2 e f(g(x)) = 6x + 7): "você faz", com pausa e com a
    conferência f(2x + 3) = 6x + 7.
  Em todas: leia o enunciado, sublinhe a grandeza-ponte (ou a função desconhecida),
  resolva, confira com um número e explique as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "a corrida de táxi custa 4,5 + 2,5x reais. Você tem
  R$ 37,00: quantos quilômetros pode andar? E qual fórmula faz essa conta para qualquer
  valor? Próximo episódio: a função que desfaz."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: três caixas em fila "tempo → altitude → temperatura"; a caixa do
  meio (altitude) brilha como ponte e depois some, deixando a seta direta
  "tempo → temperatura" com 25 − 1,2t.
- No caso 1, a expressão g(x) desenhada como uma caixa fechada com "?" que vai sendo
  aberta conforme se isola.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- A grandeza intermediária foi identificada e eliminada em cada exemplo?
- Cada lei encontrada foi conferida com um número?
- A Questão 1 dá 500 + 120t (e a ordem errada, 20 000 + 120t, foi explicada)?
```

---

## Vídeo 3: Função inversa (desfazer o caminho)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Função Composta e Função Inversa — Episódio 3 de 5:
Função inversa: desfazer o caminho
RECORTE: use APENAS a seção 06 (só a definição, f⁻¹(f(x)) = x e o quadro "f⁻¹ não é
1/f"), a seção 07 (só a receita, o exemplo com fração e a inversa da função afim) e a
seção 08 (só as conversões: Celsius–Fahrenheit e táxi) do material de apoio, mais as
Questões 3 e 8 da seção 12. Bijetora, gráfico da inversa, par exponencial–logaritmo e
tabelas ficam para o episódio 4. Na série de Conceito de Função você já fez o "caminho
de volta" com um número (táxi de R$ 30,00): aqui, a fórmula inteira da volta.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma receita de bolo feita "de trás para
   frente" (para desfazer, desfaça primeiro o último passo) e por um termômetro de
   viagem que mostra °F.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (função inversa, f⁻¹, "f inversa", entrada, saída, isolar, trocar os nomes,
   pôr em evidência).
3. Analogias âncora, retomadas ao longo da aula:
   - "a inversa é o caminho de volta: entrada vira saída e saída vira entrada";
   - "desfaça na ordem contrária, como tirar o sapato antes da meia";
   - "o ⁻¹ não é expoente: f⁻¹ desfaz, 1/f vira de cabeça para baixo".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: isolar a incógnita numa
   equação do 1º grau (série de Equações e inequações do 1º grau), F = 1,8C + 32 (série
   de Função Afim) e "meia e sapato" (episódio 1).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; toda inversa
   encontrada é testada com um ponto: se f(a) = b, a inversa tem de dar f⁻¹(b) = a.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Em Nova York, o termômetro marca 98,6 °F. Você está com
  febre? Não: são exatamente 37 °C. Para saber, você precisa da fórmula que faz o
  caminho de volta."
- Promessa: "ao final, você vai calcular a inversa de qualquer função afim, inverter
  uma fração e nunca mais confundir f⁻¹ com 1/f".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) definição: se f(a) = b, então f⁻¹(b) = a; f⁻¹(f(x)) = x e f(f⁻¹(x)) = x
     ("ida e volta = ficar parado");
  b) f⁻¹ não é 1/f: f(x) = x + 3 tem inversa x − 3, e 1/(x + 3) é outra coisa;
     f(x) = 2x tem inversa x/2, e 1/(2x) também é outra coisa (com x = 4, x/2 = 2 e
     1/(2x) = 0,125: não são parecidas);
  c) a receita em três passos: escreva y = f(x); isole x; troque os nomes. Exemplo:
     y = 2x + 1 → x = (y − 1)/2 → f⁻¹(x) = (x − 1)/2; teste: f(1) = 3 e f⁻¹(3) = 1;
  d) inversa da afim y = ax + b: (x − b)/a, desfazendo na ordem contrária (primeiro
     tira o b, depois divide pelo a); se f cresce, f⁻¹ também cresce;
  e) conversões: C = (F − 32)/1,8; 98,6 °F → 66,6 ÷ 1,8 = 37 °C; táxi:
     x = (P − 4,5)/2,5; R$ 37,00 → 13 km;
  f) inversa com fração: f(x) = (2x + 1)/(x − 3); multiplicar cruzado, juntar os
     termos com x de um lado, pôr x em evidência: x(y − 2) = 3y + 1.
- Exercício "nós fazemos": peça "pause: calcule a inversa de f(x) = 3x − 6 e teste com
  um ponto" (x = (y + 6)/3, f⁻¹(x) = (x + 6)/3; teste: f(4) = 6 e f⁻¹(6) = 4).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "A inversa troca entrada e saída."
  "Desfaça na ordem contrária: primeiro o último passo."
  "f⁻¹ desfaz; 1/f só vira de cabeça para baixo."
- Erros clássicos:
  • f⁻¹(x) = 1/f(x);
  • inversa de 2x + 1 = (x + 1)/2 (somar em vez de subtrair) ou dividir antes de
    subtrair (x/2 − 1);
  • trocar as letras sem isolar nada.
- Questões no estilo ENEM, nesta ordem:
  • Questão 3 do material (táxi, x em função de P): "eu faço", com o teste de R$ 37,00
    → 13 km e a conferência 4,5 + 2,5 · 13 = 37;
  • Questão 8 (inversa de (2x + 1)/(x − 3)): "você faz", com pausa, e com a
    conferência f(4) = 9 e (3 · 9 + 1)/(9 − 2) = 28/7 = 4.
  Em todas: leia o enunciado, resolva, teste com um ponto e explique as alternativas
  erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "f(x) = x² leva 3 em 9 e −3 em 9. Se eu te disser que
  a saída foi 9, de onde veio? Nem toda função pode ser desfeita. Próximo episódio:
  quem tem inversa, e o espelho que desenha o gráfico dela."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: uma esteira "×2 e depois +1" levando 1 até 3; em seguida, a
  esteira roda ao contrário, com as etapas invertidas e na ordem contrária ("−1 e
  depois ÷2"), levando 3 de volta a 1.
- Um termômetro com escala dupla °C/°F, com o ponteiro indo de 98,6 °F para 37 °C.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Toda inversa foi testada com um ponto (f(a) = b → f⁻¹(b) = a)?
- A inversa de 2x + 1 é (x − 1)/2, e não (x + 1)/2?
- Ficou claro que x/2 e 1/(2x) são funções diferentes (sem dizer que são "parecidas")?
```

---

## Vídeo 4: Quem tem inversa e o espelho na reta y = x

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Função Composta e Função Inversa — Episódio 4 de 5:
Quem tem inversa e o espelho na reta y = x
RECORTE: use APENAS a seção 06 (bijetora: injetora e sobrejetora; restringir o domínio),
a seção 07 (o gráfico da inversa), a seção 08 (o par exponencial–logaritmo) e a
estratégia 3 da seção 09 (tabelas) do material de apoio, mais as Questões 7, 5 e 9 da
seção 12. O par exponencial–logaritmo já foi ensinado nas séries de Função Exponencial
e de Função Logarítmica: aqui, só como exemplo do espelho, sem reensinar logaritmo.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por um armário de chaves (cada chave abre um só
   armário, e todo armário tem chave: dá para voltar do armário à chave) e por uma
   folha de papel dobrada na diagonal, com tinta fresca.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (injetora, sobrejetora, bijetora, contradomínio, restringir o domínio,
   reta y = x, simétrico, domínio e imagem).
3. Analogias âncora, retomadas ao longo da aula:
   - "para voltar, cada saída precisa ter UM dono e todo endereço precisa existir";
   - "o gráfico da inversa é o espelho na diagonal y = x: o ponto (a, b) vira (b, a)";
   - "em tabela, a inversa se lê de baixo para cima: procure o número nas SAÍDAS".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: o que é a inversa
   (episódio 3), domínio e imagem (série de Conceito de Função) e 2³ = 8 ⇔ log₂ 8 = 3
   (séries de Função Exponencial e de Função Logarítmica).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; em cada função
   candidata, teste com números concretos (duas entradas com a mesma saída? uma saída
   que nunca aparece?).
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Se eu te disser que um número ao quadrado deu 9, você não
  sabe se ele era 3 ou −3. Essa dúvida tem nome, e é ela que decide se uma função pode
  ser desfeita."
- Promessa: "ao final, você vai dizer se uma função tem inversa, achar pontos e o
  gráfico da inversa pelo espelho e ler inversas em tabelas".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) injetora: entradas diferentes, saídas diferentes; contraexemplo x² em ℝ
     ((−3)² = 3² = 9);
  b) sobrejetora: toda saída do contradomínio é atingida; contraexemplo 2ˣ de ℝ em ℝ
     (nenhum x dá −1);
  c) bijetora = as duas; só ela tem inversa;
  d) restringir o domínio salva a inversa: x² em [0, +∞[ tem inversa √x, e é por isso
     que a raiz quadrada devolve só o valor não negativo;
  e) o espelho: se f(1) = 3, então f⁻¹(3) = 1; (1, 3) vira (3, 1), reflexo na reta
     y = x (não no eixo y nem na origem);
  f) o par mais cobrado: y = 2ˣ e y = log₂ x são espelhos; (0, 1) de um corresponde a
     (1, 0) do outro; domínio e imagem trocam de lugar (ℝ e ]0, +∞[);
  g) tabelas: para f⁻¹(b), procure b na linha das saídas e leia a entrada; para
     compostas em tabela, de dentro para fora.
- Exercício "nós fazemos": peça "pause: o gráfico de y = 2ˣ passa por (3, 8). Que
  ponto do gráfico de y = log₂ x corresponde a ele?" ((8, 3), porque log₂ 8 = 3).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Só tem inversa quem é bijetora: cada saída com um dono, e todas existindo."
  "O gráfico da inversa é o espelho em y = x: (a, b) vira (b, a)."
  "Em tabela, procure o número nas saídas."
- Erros clássicos:
  • achar que x² tem inversa √x em ℝ (só com domínio x ≥ 0);
  • refletir o gráfico da inversa no eixo y (ou trocar os sinais do ponto);
  • em tabela, procurar b nas entradas para calcular f⁻¹(b).
- Questões no estilo ENEM, nesta ordem:
  • Questão 7 do material (qual função o programa consegue desfazer): "eu faço",
    testando cada alternativa com números (x² e |x|: 2 e −2 dão a mesma saída; 2ˣ:
    nenhum x dá −1; constante 5: impossível saber de onde veio; x³ + 1: sempre
    crescente e atinge todos os reais, com volta x = ∛(y − 1));
  • Questão 5 (f passa por (3, 7)): "nós fazemos";
  • Questão 9 (tabela, f⁻¹(g(3))): "você faz", com pausa (g(3) = 5; na linha de f, o 5
    está na coluna x = 2; resposta 2).
  Em todas: leia o enunciado, resolva e explique as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "no último episódio deste assunto, juntamos composta e
  inversa, caçamos as pegadinhas e treinamos para o ENEM."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: o plano cartesiano com a diagonal y = x tracejada; a curva de 2ˣ
  é pintada, o papel "dobra" na diagonal e a tinta marca a curva de log₂ x; os pontos
  (0, 1) e (1, 0), (3, 8) e (8, 3) se acendem aos pares.
- Diagrama de flechas: x² com 3 e −3 apontando para o mesmo 9 (selo amarelo "dois
  donos"), e 2ˣ com o −1 sozinho, sem flecha chegando (selo amarelo "ninguém chega").
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- A reflexão do gráfico da inversa é na reta y = x (e não no eixo y)?
- Na Questão 7, ficou claro por que 2ˣ é injetora mas não sobrejetora em ℝ?
- Na Questão 9, f⁻¹(5) foi lida procurando o 5 nas saídas de f (resposta 2)?
```

---

## Vídeo 5: Revisão (Função composta e função inversa no ENEM)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula de REVISÃO para o YouTube sobre:

TEMA: Matemática — Funções — Função Composta e Função Inversa — Episódio 5 de 5:
Revisão geral, estratégia de prova, pegadinhas e treino para o ENEM
RECORTE: use as seções 01, 09, 10, 11 e 13 do material de apoio.
NÃO reutilize as Questões 1 a 9 da seção 12 (já resolvidas nos episódios anteriores).
Progressão aritmética terá série própria: aqui, só cite a ponte.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que assistiu aos episódios 1 a 4, mas ainda é iniciante e pode ter esquecido
partes. Relembre cada conceito em uma frase simples antes de cobrá-lo.

REGRAS DE EXPLICAÇÃO
1. Cada conceito é relembrado com a mesma analogia âncora usada no seu episódio:
   máquinas em fila; de dentro para fora; meia e sapato; a grandeza-ponte que some;
   "a de dentro recebe o que você tem"; o caminho de volta; desfazer na ordem
   contrária; f⁻¹ desfaz, 1/f vira de cabeça para baixo; cada saída com um dono; o
   espelho em y = x; em tabela, procure nas saídas.
2. Prática de recuperação: antes de explicar, PERGUNTE e peça para o aluno pausar.
3. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
4. Uma ideia por cena. Frases curtas. Tom de conversa, falando com "você".

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "O ENEM quase nunca escreve f ∘ g. Ele escreve 'o custo
  depende das peças, que dependem do tempo' ou 'quanto ele andou, se pagou R$ 37,00'.
  Hoje você treina para reconhecer composta e inversa sem o símbolo."
- O que a prova cobra (seção 01): encadear modelos, inverter fórmulas, ler tabelas
  encadeadas ou códigos, reconhecer o gráfico da inversa; e as duas habilidades que
  rendem mais: a ordem (a de dentro age primeiro) e inverter é trocar entrada e saída.
- Onde aparece nas outras áreas (seção 10): Física (escalas termométricas; grandezas em
  cadeia), Química (pH = −log[H⁺] e [H⁺] = 10^−pH), Matemática Financeira (câmbio e
  impostos), Linguagens e TIC (codificar e decodificar).
- A estratégia de prova em 3 hábitos (seção 09): identificar a grandeza intermediária;
  testar as alternativas com um ponto; em tabelas, ir de dentro para fora.
- "Verdadeiro ou falso? Pause e responda": transforme em afirmações os 9 erros da
  seção 11. Para cada um: pausa → resposta → por que a pegadinha engana →
  a regra certa em uma frase.
- 5 questões INÉDITAS no estilo ENEM, criadas por você, com situações hipotéticas e
  5 alternativas cada (use estes números e confira as contas):
  1) câmbio e imposto encadeados: um produto de US$ 50,00, dólar a R$ 5,00 e imposto
     de 60% sobre o valor em reais: r(d) = 5d, F(r) = 1,6r, F(r(d)) = 8d → R$ 400,00
     (erradas: R$ 250,00, sem imposto; R$ 280,00, imposto calculado em dólar e somado
     sem converter, 250 + 30; R$ 80,00, imposto aplicado sem converter, 1,6 · 50;
     R$ 330,00, de quem soma 5 + 1,6 em vez de multiplicar, 6,6 · 50);
  2) composta em um ponto com ordem trocada: f(x) = x + 5 e g(x) = x²; f(g(3)) = 14
     (erradas: g(f(3)) = 64; f(3) · g(3) = 72; f(3) + g(3) = 17; g(3) = 9);
  3) inverter a conversão: F = 1,8C + 32, termômetro marcando 104 °F → C = 72 ÷ 1,8 =
     40 °C (erradas: (104 + 32) ÷ 1,8 ≈ 75,6; 104 ÷ 1,8 − 32 ≈ 25,8; 1,8 · 104 + 32 =
     219,2; 104 − 32 = 72, sem dividir);
  4) ponto da inversa: f invertível passa por (−2, 5) → f⁻¹ passa por (5, −2)
     (erradas: (−2, 5); (2, −5); (−5, 2); (5, −1/2), de quem usa 1/f);
  5) tabela: x = 1, 2, 3, 4; f(x) = 2, 4, 1, 3; g(x) = 3, 1, 4, 2; calcule f⁻¹(g(4)):
     g(4) = 2; o 2 está nas saídas de f na coluna x = 1 → resposta 1. Alternativas:
     A) 1 (certa); B) 2, de quem para em g(4); C) 3, de quem ignora g e calcula f(4);
     D) 4, de quem usa f no lugar de f⁻¹, f(g(4)) = f(2); E) "não é possível calcular,
     porque f não tem inversa" (falso: na tabela, cada saída de f aparece uma única
     vez, então f é bijetora).
  As alternativas erradas devem ser exatamente os erros clássicos (ordem trocada,
  produto no lugar de composição, desfazer na ordem errada, inversa como 1/f, procurar
  nas entradas da tabela). Leia, peça a pausa, resolva, teste com um ponto e explique
  cada alternativa.
- Checklist de domínio (seção 13): leia os itens e diga "marque só o que você
  conseguiria explicar em voz alta para outra pessoa, sem consultar nada; o que não
  marcou, reveja o episódio correspondente" (ordem e lei da composta: episódio 1;
  contexto e função escondida: episódio 2; calcular inversas: episódio 3; bijetora,
  gráfico e tabelas: episódio 4).
- Meta antes de considerar dominado: resolver 25 questões e acertar pelo menos 18, com
  pelo menos oito de contexto (fórmulas encadeadas ou conversões a inverter).
- Encerramento e ponte: "o próximo assunto é Progressão aritmética: uma função afim
  vista só nos números naturais, em que cada termo soma sempre o mesmo tanto."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Use um cronômetro visual nas pausas; um selo "PEGADINHA" em amarelo nos erros; os
  4 ícones dos episódios (duas máquinas em fila, ponte que some, esteira rodando ao
  contrário, espelho na diagonal) como índice visual da revisão.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Cada conceito foi relembrado antes de ser cobrado?
- As 5 questões inéditas têm uma única alternativa correta e contas corretas?
- Na questão 3, a conversão inversa subtrai 32 ANTES de dividir por 1,8?
```

---

## Cuidados ao revisar os roteiros

- **Ordem da composição:** em f(g(2)) com f(x) = x² − 1 e g(x) = 2x + 3, o certo é g(2) = 7 e f(7) = **48**. Se a IA chegar a 9, inverteu a ordem; se chegar a 24, desenvolveu (2x + 3)² sem o termo do meio.
- **Questão 6 (cupom × 10%):** a diferença entre as ordens é **R$ 2,00** (117 − 115). A IA tende a dizer que "a ordem não importa", porque a série de Descontos ensina isso para dois percentuais; confira se o roteiro faz a distinção (percentual com percentual comuta; reais com percentual, não).
- **Inversa da afim:** desfazer 2x + 1 é **subtrair 1 e depois dividir por 2**, (x − 1)/2. Atenção a "x/2 − 1" (ordem errada) e "(x + 1)/2" (sinal errado).
- **Gráfico da inversa:** reflexão na reta **y = x**; (3, 7) vira (7, 3). A IA às vezes descreve "espelho no eixo y".

## Erros encontrados no material

- **Seção 06, quadro "f⁻¹ não é 1/f":** o material diz que, para f(x) = 2x, a inversa x/2 e 1/(2x) "por coincidência, nesse caso parecem próximas". Não parecem: com x = 4, x/2 = 2 e 1/(2x) = 0,125; uma é reta, a outra é hipérbole. Imprecisão pequena, mas que reforça justamente a confusão que o quadro quer evitar. No Vídeo 3 o roteiro mostra que são funções diferentes, sem a frase.
