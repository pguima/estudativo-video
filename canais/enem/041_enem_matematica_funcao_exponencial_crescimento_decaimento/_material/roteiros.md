# Função Exponencial: crescimento e decaimento — série de videoaulas

Material de apoio: `01-matematica/26-funcao-exponencial-crescimento-decaimento.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Expoente zero, expoente negativo (2⁻³ = 1/8), mesma base | **Potenciação e radiciação** | Revisão relâmpago nos vídeos 1 e 5 ("expoente negativo inverte, não troca o sinal"). Não reensino as propriedades. |
| Taxa vira fator (1 + i, 1 − i) | **Porcentagem** | Revisão de 30 s no vídeo 2. O novo é escrever a lei Q₀ · aᵗ. |
| M = C · (1 + i)ᵗ, tempo de duplicação constante | **Juros Compostos** | Vídeo 2 trata como "você já viu isso disfarçado": é a mesma exponencial com C no lugar de Q₀. Nenhuma questão de Juros Compostos é reutilizada. |
| Função afim, diferença constante | **Função afim** | Revisão relâmpago no vídeo 4 (teste da diferença × teste da razão). |
| Termo geral da PG, valores em PG | **Progressão geométrica** (série futura) | Só cito: "os valores de uma exponencial em tempos iguais formam uma PG; isso tem série própria". |
| **Q1 (500 bactérias, dobra a cada 20 min, 2 h)** e **Q2 (80 mg, 4 meias-vidas → 5 mg)** | **Q1 de PG é idêntica à Q1 daqui; a Q2 de PG (80 g, meia-vida de 5 anos, 20 anos → 5 g) é quase igual à Q2 daqui** | **Uso aqui**, porque esta série vem antes e é o lar do tema. A série de PG não deve repetir essas duas (pendência no relatório). A Q3 daqui (tabela, fator 0,8) tem o mesmo formato da Q9 de PG, mas números diferentes. |
| Equação que "não fecha" (2ˣ = 10) | **Logaritmos** (próxima série) | Só prometo: "a ferramenta é o logaritmo, próxima série". |

## Plano: 6 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Multiplicar em vez de somar: a função exponencial e seu gráfico** | 02, 03 | Q9 | 8–10 min |
| **2. O modelo Q₀ · aᵗ: da frase do enunciado ao fator** | 04 | Q3, Q6 | 8–10 min |
| **3. Duplicação e meia-vida: conte os intervalos** | 05 | Q1, Q2, Q8 | 10–12 min |
| **4. Exponencial ou afim? O teste da razão** | 06 | Q5 | 6–8 min |
| **5. Equações e inequações exponenciais: mesma base** | 07, 08 | Q4, Q7 | 10–12 min |
| **6. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Vídeo 1: Multiplicar em vez de somar: a função exponencial e seu gráfico

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Função Exponencial: crescimento e decaimento —
Episódio 1 de 6: Multiplicar em vez de somar: a função exponencial e seu gráfico
RECORTE: use APENAS as seções 02 e 03 do material de apoio, mais a Questão 9 da seção
12. Expoente zero e expoente negativo já foram ensinados na série de Potenciação e
radiciação: aqui, revisão rápida. O modelo Q₀ · aᵗ, a meia-vida e as equações ficam
para os próximos episódios.
DURAÇÃO: 8 a 10 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma mesada que dobra toda semana, por um
   boato que se espalha em grupos de mensagens e por um café esfriando na mesa; só
   depois apresente a definição.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (função exponencial, base, expoente, fator, crescente, decrescente, imagem,
   assíntota horizontal, coeficiente).
3. Analogias âncora, retomadas ao longo da aula:
   - "a função afim é uma escada de degraus iguais (soma sempre o mesmo); a exponencial
     é uma escada em que cada degrau é o anterior multiplicado pelo mesmo fator";
   - "expoente negativo é um 'vire de cabeça para baixo', não um sinal de menos no
     resultado: 2⁻² = 1/4, positivo";
   - "a assíntota é uma parede invisível: a curva chega cada vez mais perto e nunca
     encosta".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: a⁰ = 1 e a⁻ⁿ = 1/aⁿ
   (série de Potenciação e radiciação) e a ideia de função como "entra x, sai y" (série
   de Conceito de função).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; ao montar tabelas,
   mostre a multiplicação de uma coluna para a seguinte (×2, ×1/2).
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Uma mesada de R$ 1 que dobra toda semana. Em 10 semanas,
  R$ 1.024. Em 20 semanas, mais de R$ 1 milhão (2²⁰ = 1 048 576). Somar nunca faria
  isso. Multiplicar faz."
- Promessa: "ao final, você vai reconhecer uma função exponencial, saber por que a base
  tem restrições e desenhar o gráfico dela sem decorar nada".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) somar × multiplicar: na afim cada passo soma a mesma quantidade; na exponencial
     cada passo multiplica pelo mesmo fator;
  b) definição: f(x) = aˣ, com a > 0 e a ≠ 1; a variável está no EXPOENTE (diferente
     de x² ou x³, em que ela está na base);
  c) por que as restrições: base 1 dá 1ˣ = 1 sempre (constante); base negativa dá
     contas como (−4)^(1/2), que não são números reais;
  d) a tabela da seção 02: 2ˣ e (1/2)ˣ para x = −2, −1, 0, 1, 2, 3
     (1/4, 1/2, 1, 2, 4, 8 e 4, 2, 1, 1/2, 1/4, 1/8);
  e) aˣ é sempre positivo: imagem ]0, +∞[;
  f) o gráfico: base maior que 1 sobe, base entre 0 e 1 desce; as duas passam por
     (0, 1) porque a⁰ = 1; (1/2)ˣ = 2⁻ˣ, uma é o espelho da outra no eixo y;
  g) a assíntota horizontal y = 0; com coeficiente, y = k · aˣ corta o eixo em (0, k);
     em y = 25 + 65 · 0,8ᵗ, a assíntota sobe para y = 25: é o valor de que a grandeza
     se aproxima com o tempo.
- Exercício "nós fazemos": peça "pause: complete a tabela de 3ˣ para x = −2, −1, 0, 1
  e 2" (1/9, 1/3, 1, 3, 9).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Na exponencial, cada passo multiplica pelo mesmo fator."
  "Base maior que 1 sobe; base entre 0 e 1 desce; todas passam por (0, 1)."
  "A exponencial nunca chega a zero: ela só se aproxima da assíntota."
- Erros clássicos:
  • 2⁻³ = −8 (o certo é 1/8: expoente negativo inverte, o resultado continua positivo);
  • achar que a curva "encosta" no eixo x em algum momento.
- Questão no estilo ENEM: Questão 9 do material (café T(t) = 25 + 65 · 0,8ᵗ): "nós
  fazemos". Diga "pause o vídeo e tente", mostre que 0,8ᵗ vai encolhendo
  (0,8; 0,64; 0,512…), que a parcela 65 · 0,8ᵗ desaparece aos poucos e que sobra 25 °C.
  Explique as erradas: 40 subtrai os dois números do modelo; 65 é a diferença inicial
  entre café e sala; 77 é a temperatura após 1 minuto (25 + 52); 90 é a inicial.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "um carro de R$ 60 mil perde 15% do valor por ano.
  Para achar o preço do ano seguinte, você multiplica por 0,15 ou por 0,85? Próximo
  episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: duas escadas lado a lado, uma com degraus iguais (+2) e outra com
  degraus que dobram (×2), crescendo até a segunda sair da tela.
- O gráfico de 2ˣ e (1/2)ˣ sendo desenhado ponto a ponto a partir da tabela, com o
  ponto (0, 1) piscando e a assíntota tracejada como uma "parede invisível".
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Ficou claro que expoente negativo NÃO dá resultado negativo?
- Os valores da tabela de 2ˣ e (1/2)ˣ estão corretos?
- A resposta da Questão 9 é 25 °C, com a explicação da assíntota?
```

---

## Vídeo 2: O modelo Q₀ · aᵗ: da frase do enunciado ao fator

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Função Exponencial: crescimento e decaimento —
Episódio 2 de 6: O modelo Q₀ · aᵗ: da frase do enunciado ao fator
RECORTE: use APENAS a seção 04 do material de apoio (e o quadro "O que rende mais aqui"
da seção 01), mais as Questões 3 e 6 da seção 12. Fatores 1 + i e 1 − i já foram
ensinados na série de Porcentagem; M = C · (1 + i)ᵗ já foi ensinado na série de Juros
Compostos: aqui, revisão rápida e a revelação de que é a mesma lei. Duplicação e
meia-vida ficam para o episódio 3.
DURAÇÃO: 8 a 10 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pelo carro que perde valor todo ano, pela cidade
   que cresce e pela cultura de bactérias que triplica; só depois escreva a lei.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (valor inicial Q₀, fator, taxa, crescimento, decaimento, depreciação, lei).
3. Analogias âncora, retomadas ao longo da aula:
   - "a lei é uma receita com dois ingredientes: de onde começa (Q₀) e por quanto
     multiplica a cada passo (a)";
   - "o fator é o que SOBRA: quem perde 15% fica com 85%";
   - "juros compostos são a exponencial de terno e gravata: M = C · (1 + i)ᵗ é
     Q₀ · aᵗ com outro nome".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: aumento de i% é
   multiplicar por 1 + i e desconto de i% é multiplicar por 1 − i (série de
   Porcentagem); M = C · (1 + i)ᵗ (série de Juros Compostos).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; ao testar uma lei,
   substitua t = 0, 1 e 2 na tela, um de cada vez.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Um carro de R$ 60 mil perde 15% do valor por ano. Quem
  multiplica por 0,15 conclui que, depois de um ano, ele vale R$ 9 mil. O certo é
  R$ 51 mil. Um número errado na lei e a questão inteira vai embora."
- Promessa: "ao final, você vai transformar qualquer frase de enunciado (dobra, cresce
  3%, perde 15%) numa lei pronta para usar".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) a lei geral Q(t) = Q₀ · aᵗ: Q₀ é o valor em t = 0; a é o fator por unidade de
     tempo; fator maior que 1, crescimento; entre 0 e 1, decaimento;
  b) a tabela de tradução da seção 04, linha a linha: população de 200 mil cresce 3% ao
     ano → 1,03 → P = 200 000 · 1,03ᵗ; carro de R$ 60 mil perde 15% ao ano → 0,85 →
     V = 60 000 · 0,85ᵗ; 500 bactérias que triplicam a cada hora → 3 → N = 500 · 3ᵗ;
     R$ 1 000 a juros compostos de 2% ao mês → 1,02 → M = 1 000 · 1,02ᵗ;
  c) "você já viu isso disfarçado": a última linha é a fórmula da série de Juros
     Compostos; C é o Q₀ e 1 + i é o fator;
  d) perder 15% não é fator 0,15; crescer 3% não é fator 3 nem 0,03;
  e) achar Q₀ e a a partir de dois pontos: f(0) = 3 dá Q₀ = 3; f(2) = 12 dá
     3 · a² = 12, a² = 4, a = 2 (a base é positiva).
- Exercício "nós fazemos": peça "pause: uma cidade de 50 000 habitantes cresce 2% ao
  ano. Escreva a lei e calcule a população daqui a 2 anos" (P = 50 000 · 1,02ᵗ;
  50 000 · 1,0404 = 52 020 habitantes).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Com o valor inicial e o fator, a lei sai sozinha."
  "O fator é o que sobra: perder 15% é multiplicar por 0,85."
  "Juros compostos são a mesma exponencial com outro nome."
- Erros clássicos:
  • perde 15% ⇒ fator 0,15 (o certo é 0,85);
  • cresce 3% ⇒ fator 3 (o certo é 1,03: taxa vira fator somando 1);
  • 3 · 2ˣ = 6ˣ (o coeficiente não entra na base; 3 · 2ˣ fica assim).
- Questões no estilo ENEM, nesta ordem:
  • Questão 3 do material (máquina agrícola: 50 000, 40 000, 32 000, 25 600): "eu faço".
    Divida cada valor pelo anterior (sempre 0,8: perda de 20% ao ano) e teste t = 0.
    Explique as erradas: A acerta t = 0 e t = 1, mas dá 30 000 em t = 2; B usa a taxa
    de perda (0,2) como fator; C começa em 40 000; D escreve 0,8t (produto), que dá 0
    em t = 0;
  • Questão 6 (f(x) = k · aˣ pelos pontos (0, 3) e (2, 12), pede f(3)): "você faz", com
    pausa. Resposta 24. Explique: 16,5 liga os pontos por uma reta; 18 troca a
    potência por produto (3 · 2 · 3); 36 supõe a = 3; 48 multiplica 12 por a² = 4,
    como se houvesse dois passos de x = 2 para x = 3.
  Em todas: leia o enunciado, ache Q₀ e o fator, escreva a lei, confira em t = 0.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "1 000 bactérias que dobram a cada 30 minutos: depois
  de 3 horas, são 6 000? Nem perto. Próximo episódio: duplicação e meia-vida."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: uma "máquina de tradução" que recebe a frase do enunciado
  ("perde 15% ao ano") e cospe o fator (0,85) e a lei pronta; a barra de 100% do carro
  perdendo um pedaço de 15% e o pedaço que SOBRA (85%) ficando em destaque.
- A fórmula M = C · (1 + i)ᵗ "tirando a fantasia" e revelando Q₀ · aᵗ por baixo.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- O fator foi sempre apresentado como "o que sobra" (0,85, e não 0,15)?
- A conta do exercício (52 020) e a da Questão 6 (24) estão corretas?
- A ligação com Juros Compostos foi feita sem reensinar o conteúdo daquela série?
```

---

## Vídeo 3: Duplicação e meia-vida: conte os intervalos

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Função Exponencial: crescimento e decaimento —
Episódio 3 de 6: Duplicação e meia-vida: conte os intervalos
RECORTE: use APENAS a seção 05 do material de apoio, mais as Questões 1, 2 e 8 da
seção 12. A lei Q₀ · aᵗ é do episódio 2: aqui, revisão rápida. A progressão
geométrica tem série própria: só cite. A Questão 7 (dose de remédio) fica para o
episódio 5.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma cultura de bactérias num laboratório, por
   um remédio que vai saindo do corpo e pelo césio-137 do acidente de Goiânia (1987);
   só depois apresente as fórmulas.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (tempo de duplicação, meia-vida, isótopo radioativo, decaimento, número de
   intervalos, datação por carbono-14).
3. Analogias âncora, retomadas ao longo da aula:
   - "o expoente é um contador de intervalos: quantas vezes o relógio 'apitou' desde o
     começo";
   - "meia-vida é cortar a pizza que SOBROU, não a pizza inteira: metade, depois metade
     da metade";
   - "duplicações se multiplicam, não se somam: 6 dobras são ×64, não ×12".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: Q₀ · aᵗ (episódio 2) e
   as potências 2⁶ = 64 e (1/2)⁴ = 1/16 (série de Potenciação e radiciação).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; converta as unidades
   ANTES de contar os intervalos (horas em minutos, anos em anos) e escreva a unidade
   ao lado de cada número.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Um material radioativo perde metade a cada 30 anos. Depois
  de 60 anos, acabou? Não: ainda resta um quarto. Depois de 90, um oitavo. Ele nunca
  chega a zero."
- Promessa: "ao final, você vai resolver qualquer questão de 'dobra a cada' ou de
  'meia-vida' contando intervalos, sem fórmula decorada".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) duplicação a cada T: Q(t) = Q₀ · 2^(t/T); o expoente t/T conta os intervalos;
  b) o exemplo do material: 1 000 bactérias que dobram a cada 30 min, depois de 3 h:
     180 ÷ 30 = 6 duplicações; 1 000 · 2⁶ = 64 000;
  c) meia-vida T: Q(t) = Q₀ · (1/2)^(t/T);
  d) césio-137 (meia-vida de cerca de 30 anos): em 90 anos, 3 meias-vidas, resta
     (1/2)³ = 1/8;
  e) as barras da meia-vida: 100% → 50% → 25%; cada intervalo corta a metade do que
     existe NAQUELE momento;
  f) o caminho inverso: dada a fração que resta (1/8, 1/16), descubra quantas
     meias-vidas passaram e multiplique pela duração de cada uma;
  g) só cite: os valores a cada intervalo formam uma progressão geométrica (série
     própria).
- Exercício "nós fazemos": peça "pause: uma amostra de 120 g tem meia-vida de 10 anos.
  Quanto resta depois de 30 anos?" (30 ÷ 10 = 3 meias-vidas; 120 → 60 → 30 → 15 g).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Primeiro conte os intervalos, depois escreva a potência."
  "Cada meia-vida corta pela metade o que existe naquele momento."
  "Duplicações se multiplicam: 6 dobras são ×64, não ×12."
- Erros clássicos:
  • 2 meias-vidas ⇒ sobra 0% (o certo é 25%);
  • dobra 6 vezes ⇒ ×12 (o certo é ×2⁶ = ×64);
  • contar o instante inicial como um intervalo (7 duplicações em vez de 6).
- Questões no estilo ENEM, nesta ordem:
  • Questão 1 do material (500 bactérias, dobra a cada 20 min, 2 h): "eu faço".
    120 ÷ 20 = 6; 500 · 64 = 32 000. Explique: 3 000 é 500 · 6 (linear); 6 000 é
    500 · 2 · 6; 16 000 conta 5 duplicações; 64 000 conta 7;
  • Questão 2 (iodo-131, meia-vida de 8 dias, 80 mg, 32 dias): "nós fazemos".
    4 meias-vidas: 80 → 40 → 20 → 10 → 5 mg. Explique: 2,5 aplica uma a mais; 10 para
    na terceira; 20 divide 80 por 4 em vez de por 2⁴; 40 aplica uma só;
  • Questão 8 (carbono-14, meia-vida de cerca de 5 730 anos, resta 1/16): "você faz",
    com pausa. 1/16 = (1/2)⁴ → 4 · 5 730 = 22 920 anos. Explique: 1 432,5 divide por 4;
    11 460 e 17 190 contam 2 e 3 meias-vidas; 91 680 trata o 16 como número de
    meias-vidas.
  Em todas: converta as unidades, escreva o número de intervalos, depois a potência, e
  confira a plausibilidade.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "o perfil A ganha 300 seguidores por semana. O perfil
  B só dobra, mas começa com 100. Quem vence, e quando? Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: um relógio que "apita" a cada intervalo, com um contador de
  intervalos subindo (1, 2, 3…) e a população dobrando a cada apito; depois, barras da
  meia-vida encolhendo pela metade (100%, 50%, 25%, 12,5%) sem nunca sumir.
- Uma pizza sendo cortada: metade, depois metade do que sobrou.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Em todas as questões, o número de intervalos foi escrito ANTES da potência?
- As respostas são 32 000, 5 mg e 22 920 anos, com as alternativas erradas explicadas?
- Ficou claro que a quantidade nunca chega a zero?
```

---

## Vídeo 4: Exponencial ou afim? O teste da razão

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Função Exponencial: crescimento e decaimento —
Episódio 4 de 6: Exponencial ou afim? O teste da razão
RECORTE: use APENAS a seção 06 do material de apoio (e o hábito 2 da seção 09, "teste
a lei em três pontos"), mais a Questão 5 da seção 12. A função afim já foi ensinada na
série de Função afim: aqui, revisão rápida. A progressão geométrica tem série própria:
só cite.
DURAÇÃO: 6 a 8 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por dois perfis de rede social, um que ganha
   sempre o mesmo número de seguidores e outro que dobra; só depois mostre as tabelas.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (diferença constante, razão constante, teste da razão, modelo afim, modelo
   exponencial, progressão geométrica).
3. Analogias âncora, retomadas ao longo da aula:
   - "a tartaruga e a lebre ao contrário: a reta sai na frente, mas a curva sempre
     alcança e passa";
   - "na afim o que se repete é a SUBTRAÇÃO entre vizinhos; na exponencial, a DIVISÃO";
   - "duas leis podem concordar em dois pontos e brigar no terceiro: teste sempre
     três".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: função afim como
   "soma sempre o mesmo valor" (série de Função afim) e a lei Q₀ · aᵗ (episódio 2).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; nas tabelas, escreva
   a diferença e a razão entre cada par de vizinhos.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Uma reta começa em 20 e uma curva começa em 1. Até o passo 6,
  a reta está na frente: 80 contra 64. No passo 7, a curva já passou: 128 contra 90.
  E nunca mais perde."
- Promessa: "ao final, você vai olhar uma tabela e dizer em segundos se o crescimento é
  afim ou exponencial, e achar o fator".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) a tabela da seção 06: afim 100, 150, 200, 250, 300 (diferença +50) × exponencial
     100, 150, 225, 337,5, 506,25 (razão ×1,5); as duas começam iguais e têm o mesmo
     primeiro passo;
  b) o teste da razão: divida cada valor pelo anterior; razão sempre igual = exponencial,
     e essa razão é o fator a; diferença sempre igual = afim;
  c) a corrida da reta (20 + 10t) contra a curva (2ᵗ): t = 6 (80 contra 64) e t = 7
     (90 contra 128); toda exponencial crescente ultrapassa qualquer afim;
  d) teste três pontos: lembre a Questão 3 do episódio 2, em que a reta acertava t = 0
     e t = 1 e errava t = 2;
  e) só cite: valores de uma exponencial em tempos iguais formam uma progressão
     geométrica (série própria).
- Exercício "nós fazemos": peça "pause: a tabela 80, 120, 180, 270 é afim ou
  exponencial? Qual é o próximo valor?" (diferenças 40, 60, 90, não constantes; razões
  sempre 1,5: exponencial; próximo valor 405).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Diferença constante é afim; razão constante é exponencial."
  "Toda exponencial crescente acaba ultrapassando qualquer reta."
  "Teste sempre três pontos, não dois."
- Erros clássicos:
  • dois pontos certos ⇒ lei certa (reta e curva podem coincidir em dois pontos);
  • confundir o ganho de uma semana com o total acumulado.
- Questão no estilo ENEM: Questão 5 do material (perfil A: 1 000 + 300t; perfil B:
  100 · 2ᵗ): "nós fazemos". Diga "pause o vídeo e tente", monte a tabela para t = 3, 4
  e 5 (A: 1 900, 2 200, 2 500; B: 800, 1 600, 3 200) e conclua: 5 semanas. Explique as
  erradas: 3 semanas confunde ganho semanal com total (B já ganha 400 contra 300, mas
  tem muito menos); 4 semanas compara B com os 1 000 iniciais de A, esquecendo que A
  também cresce; 6 semanas conta hoje como primeira semana; "nunca" ignora que a
  exponencial sempre ultrapassa a reta.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "se P(t) = 1 000 · 3^(t/2), quando a população chega
  a 81 000? Dá para achar t sem tentar um por um. Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: uma corrida entre uma tartaruga sobre a reta e uma lebre sobre a
  curva, com o placar a cada passo; no passo 7, a ultrapassagem com um selo verde.
- Setas entre colunas vizinhas da tabela mostrando "−" (diferença) e "÷" (razão), com
  a que se repete acendendo.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- As tabelas da corrida (80 × 64 e 90 × 128) e da Questão 5 estão corretas?
- O teste da razão foi mostrado com divisão entre vizinhos, e não entre o valor e o
  primeiro termo?
- A resposta da Questão 5 é 5 semanas?
```

---

## Vídeo 5: Equações e inequações exponenciais: mesma base

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Função Exponencial: crescimento e decaimento —
Episódio 5 de 6: Equações e inequações exponenciais: mesma base
RECORTE: use APENAS as seções 07 e 08 do material de apoio, mais as Questões 4 e 7 da
seção 12. Escrever números como potência da mesma base já foi ensinado na série de
Potenciação e radiciação: aqui, revisão rápida. Equações que não fecham na mesma base
(2ˣ = 10) ficam para a série de Logaritmos: só prometa.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma pergunta real ("quando a população de
   aves chega a 81 000?", "quando o remédio cai a 50 mg/L?") e só depois mostre a
   técnica.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (equação exponencial, mesma base, isolar a potência, colocar em evidência,
   inequação, sentido da desigualdade, injetora).
3. Analogias âncora, retomadas ao longo da aula:
   - "duas potências de mesma base iguais são como duas fotos idênticas do mesmo
     objeto: os expoentes também têm de ser iguais";
   - "isole a potência como quem tira a embalagem antes de comparar dois produtos";
   - "base entre 0 e 1 é uma ladeira descendo: quanto mais alto o valor, mais para trás
     (menor x) você está; por isso a desigualdade vira".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: 4 = 2², 8 = 2³,
   32 = 2⁵, 9 = 3², 27 = 3³, 81 = 3⁴, 1/8 = 2⁻³ e (aᵐ)ⁿ = aᵐ·ⁿ (série de Potenciação e
   radiciação); o gráfico crescente/decrescente (episódio 1).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; antes de igualar
   expoentes, diga em voz alta "cada lado é UMA potência só, da mesma base?".
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "1 000 · 3^(t/2) = 81 000. Quem compara os expoentes direto
  se perde. Quem divide por 1 000 primeiro chega a 3^(t/2) = 3⁴ e resolve de cabeça:
  t = 8."
- Promessa: "ao final, você vai resolver equações e inequações exponenciais pondo tudo
  na mesma base, e saber quando a desigualdade vira".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) a ideia: mesma base dos dois lados → expoentes iguais (a exponencial é injetora:
     valores diferentes de x dão potências diferentes);
  b) a tabela da seção 07: 2^(x+1) = 32 = 2⁵ → x = 4; 9ˣ = 27 → 3^(2x) = 3³ → x = 3/2;
     4ˣ = 1/8 → 2^(2x) = 2⁻³ → x = −3/2;
  c) isole a potência: 1 000 · 3^(t/2) = 81 000 → 3^(t/2) = 81 = 3⁴ → t/2 = 4 → t = 8;
  d) duas potências somadas: 2ˣ + 2^(x+1) = 24 → 2ˣ(1 + 2) = 24 → 2ˣ = 8 → x = 3;
  e) quando a base não fecha (2ˣ = 10): a ferramenta é o logaritmo, próxima série;
  f) inequações: base maior que 1 mantém o sentido (2ˣ > 16 = 2⁴ → x > 4); base entre
     0 e 1 inverte ((1/3)ˣ > 9 = (1/3)⁻² → x < −2), com o motivo no gráfico;
  g) em contexto: remédio de 400 mg/L que cai à metade a cada 4 h fica acima de
     50 mg/L enquanto 400 · (1/2)^(t/4) > 50, ou seja, (1/2)^(t/4) > (1/2)³, t < 12 h.
- Exercício "nós fazemos": peça "pause: resolva 8ˣ = 32" (2^(3x) = 2⁵ → 3x = 5 →
  x = 5/3).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Mesma base dos dois lados: iguale os expoentes."
  "Isole a potência antes de comparar expoentes."
  "Base entre 0 e 1 inverte a desigualdade."
- Erros clássicos:
  • igualar expoentes com coeficiente na frente (em 1 000 · 3ᵗ = 81 000, divida por
    1 000 antes);
  • (1/3)ˣ > 9 ⇒ x > −2 (o certo é x < −2);
  • 2^(x+1) tratado como 2ˣ + 1 (o certo é 2 · 2ˣ).
- Questões no estilo ENEM, nesta ordem:
  • Questão 4 do material (aves: P(t) = 1 000 · 3^(t/2) chega a 81 000): "eu faço".
    Resposta 8 anos. Explique: 4 anos esquece a divisão do expoente por 2; 27 divide 81
    por 3; 54 trata o expoente como produto (3 · t/2 = 81); 162 iguala o expoente ao
    valor (t/2 = 81);
  • Questão 7 (remédio: 400 mg/L, cai à metade a cada 4 h, nova dose a 50 mg/L): "você
    faz", com pausa. Mostre os dois caminhos: contar meias-vidas (400 → 200 → 100 → 50,
    3 · 4 = 12 h) e a equação 400 · (1/2)^(t/4) = 50 → (1/2)^(t/4) = (1/2)³ → t = 12.
    Explique: 7 h supõe queda linear de 50 mg/L por hora; 8 h para em 100 mg/L; 16 h
    aplica uma meia-vida a mais; 32 h trata o 8 (400 ÷ 50) como número de meias-vidas,
    quando 8 = 2³ indica três.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "no último episódio deste assunto, juntamos tudo,
  caçamos as pegadinhas e treinamos com questões que misturam Biologia, Química e
  Física."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: os dois lados da equação sendo "traduzidos" para a mesma base
  (81 vira 3⁴, com os quatro 3 se juntando), e depois uma balança em que os expoentes
  ficam iguais.
- No bloco das inequações: o gráfico de (1/3)ˣ como uma ladeira descendo, com uma seta
  mostrando que "mais alto" corresponde a "mais à esquerda", e o sinal > girando para <.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- A potência foi isolada antes de igualar expoentes em todos os exemplos?
- A inversão do sentido com base entre 0 e 1 foi justificada pelo gráfico?
- As respostas são x = 5/3, 8 anos e 12 h?
```

---

## Vídeo 6: Revisão (Função exponencial no ENEM)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula de REVISÃO para o YouTube sobre:

TEMA: Matemática — Funções — Função Exponencial: crescimento e decaimento —
Episódio 6 de 6: Revisão geral, estratégia de prova, pegadinhas e treino para o ENEM
RECORTE: use as seções 01, 09, 10, 11 e 13 do material de apoio.
NÃO reutilize as Questões 1 a 9 da seção 12 (já resolvidas nos episódios anteriores).
Logaritmos terão série própria (a próxima): aqui, só cite a ponte.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que assistiu aos episódios 1 a 5, mas ainda é iniciante e pode ter esquecido
partes. Relembre cada conceito em uma frase simples antes de cobrá-lo.

REGRAS DE EXPLICAÇÃO
1. Cada conceito é relembrado com a mesma analogia âncora usada no seu episódio:
   a escada que multiplica e a parede invisível da assíntota; o expoente negativo que
   vira de cabeça para baixo; a receita de dois ingredientes (Q₀ e a); o fator é o que
   sobra; juros compostos como a exponencial de terno e gravata; o expoente como
   contador de intervalos; a pizza que sobrou; a tartaruga e a lebre ao contrário;
   as duas fotos idênticas (mesma base); a ladeira descendo que inverte a desigualdade.
2. Prática de recuperação: antes de explicar, PERGUNTE e peça para o aluno pausar.
3. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
4. Uma ideia por cena. Frases curtas. Tom de conversa, falando com "você".

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "A exponencial é a função das manchetes: vírus, bactérias,
  dívidas, remédios, radioatividade. O ENEM quase nunca escreve 'resolva a equação';
  ele conta uma história. Hoje você treina para traduzir a história."
- O que a prova cobra (seção 01): crescimento por fator, decaimento e meia-vida,
  reconhecer o modelo numa tabela ou gráfico e descobrir o tempo; o que rende mais é
  traduzir a frase no fator certo ("dobra a cada 20 min" → 2 por período; "cresce 3% ao
  ano" → 1,03; "perde 15% ao ano" → 0,85; "meia-vida de 8 dias" → 1/2 a cada 8 dias).
- Onde aparece nas outras áreas (seção 10): Biologia (bactérias e populações, curva em
  J; com recursos limitados, curva em S), Química (decaimento radioativo e carbono-14,
  meia-vida de cerca de 5 730 anos), Física (resfriamento até a temperatura ambiente),
  Matemática Financeira (juros compostos, fator 1 + i) e Geografia (Malthus: população
  em PG, alimentos em PA, a comparação exponencial × afim).
- A estratégia de prova em 3 hábitos (seção 09): contar os intervalos antes de qualquer
  conta (convertendo unidades primeiro); testar a lei em t = 0, 1 e 2; quando a conta
  não fecha na mesma base e o enunciado dá log 2 ou log 3, procurar o logaritmo.
- "Verdadeiro ou falso? Pause e responda": transforme em afirmações os 9 erros da
  seção 11 (perde 15% ⇒ fator 0,15; cresce 3% ⇒ fator 3; 2 meias-vidas ⇒ sobra 0%;
  dobra 6 vezes ⇒ ×12; 2⁻³ = −8; 3 · 2ˣ = 6ˣ; (1/3)ˣ > 9 ⇒ x > −2; igualar expoentes
  com coeficiente na frente; dois pontos certos ⇒ lei certa). Para cada um: pausa →
  resposta → por que a pegadinha engana → a regra certa em uma frase.
- 5 questões INÉDITAS no estilo ENEM, criadas por você, com situações hipotéticas e
  5 alternativas cada:
  1) depreciação: um celular de R$ 2.000,00 perde 20% do valor por ano, sempre sobre o
     valor do ano anterior; valor após 2 anos. Correta: R$ 1.280,00 (2 000 · 0,8²).
     Erradas: R$ 80,00 (fator 0,2), R$ 1.200,00 (perda linear de 40%), R$ 1.600,00 (só
     um ano), R$ 2.880,00 (fator 1,2);
  2) meia-vida de um medicamento: 240 mg no sangue, meia-vida de 6 h; quanto resta
     após 24 h. Correta: 15 mg (4 meias-vidas). Erradas: 0 mg (subtraiu 50% duas
     vezes), 7,5 mg (5 meias-vidas), 30 mg (3 meias-vidas), 60 mg (dividiu por 4, o
     número de meias-vidas);
  3) qual lei: quantidade de um poluente num tanque (mg), a cada hora: 64, 48, 36, 27.
     Correta: N = 64 · 0,75ᵗ. Erradas: N = 64 − 16t (acerta t = 0 e t = 1, dá 32 em
     t = 2), N = 64 · 0,25ᵗ (taxa no lugar do fator), N = 48 · 0,75ᵗ (começa em t = 1),
     N = 64 · 0,75t (produto, dá 0 em t = 0);
  4) equação com coeficiente: peixes num lago, P(t) = 200 · 2^(t/3), t em meses; quando
     chega a 6 400. Correta: 15 meses (6 400 ÷ 200 = 32 = 2⁵; t/3 = 5). Erradas: cerca
     de 1,7 mês (dividiu 5 por 3), 5 meses (esqueceu a divisão por 3), 48 meses
     (tratou a potência como produto, 2 · t/3 = 32), 96 meses (igualou o expoente ao
     valor, t/3 = 32);
  5) resfriamento e inequação: forno desligado, T(t) = 20 + 160 · 0,5^(t/10), t em
     minutos; por quanto tempo a temperatura fica acima de 40 °C. Correta: menos de
     30 min (160 · 0,5^(t/10) > 20 → 0,5^(t/10) > 1/8 = 0,5³ → t/10 < 3). Erradas:
     menos de 3 min (esqueceu o ÷10), menos de 20 min (não subtraiu os 20 °C do
     ambiente antes de isolar a potência), mais de 30 min (não inverteu o sentido),
     "sempre, porque nunca cai abaixo de 40 °C" (confundiu com a assíntota, que é
     20 °C). Comente: a temperatura tende a 20 °C, a da cozinha.
  As alternativas erradas devem ser exatamente os erros clássicos. Leia, peça a pausa,
  escreva o fator e o número de intervalos, resolva, confira a plausibilidade e
  explique cada alternativa.
- Checklist de domínio (seção 13): leia os itens e diga "marque só o que você
  conseguiria explicar em voz alta para outra pessoa, sem consultar nada; o que não
  marcou, reveja o episódio correspondente" (base, gráfico e assíntota → episódio 1;
  taxa em fator e lei por dois pontos → episódio 2; duplicação e meia-vida →
  episódio 3; afim × exponencial → episódio 4; equações, evidência e inequações →
  episódio 5; reconhecer quando precisa de logaritmo → próxima série).
- Meta antes de considerar dominado: resolver 30 questões e acertar pelo menos 21
  (70%), com pelo menos dez de meia-vida ou duplicação em contexto.
- Encerramento e ponte: "e quando a equação é 2ˣ = 10, que não fecha em base nenhuma?
  O próximo assunto é Logaritmos: definição, propriedades e equações, a ferramenta que
  tira a incógnita do expoente."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Use um cronômetro visual nas pausas; um selo "PEGADINHA" em amarelo nos erros; um
  ícone de área (bactéria, átomo, termômetro, cifrão) em cada questão inédita; os 5
  ícones dos episódios (escada que multiplica, máquina de tradução, relógio que apita,
  tartaruga e lebre, balança dos expoentes) como índice visual da revisão.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Cada conceito foi relembrado antes de ser cobrado?
- As 5 questões inéditas têm uma única alternativa correta e contas corretas
  (R$ 1.280,00; 15 mg; 64 · 0,75ᵗ; 15 meses; menos de 30 min)?
- Na questão 5, a potência foi isolada (subtraindo 20) antes de comparar, e o sentido
  foi invertido por causa da base 0,5?
```

---

## Cuidados ao revisar os roteiros

- **Contagem de intervalos (vídeo 3):** em 2 h com duplicação a cada 20 min são **6** duplicações (500 · 2⁶ = 32 000). A IA às vezes conta o instante inicial e chega a 7 (64 000), que é justamente a alternativa E.
- **Expoente negativo e coeficiente (vídeos 1 e 2):** 2⁻² = 1/4 (positivo) e 3 · 2ˣ **não** é 6ˣ. Confira se a narração não "simplifica" 3 · 2³ como 6³ = 216 (o certo é 24, a resposta da Q6).
- **Inequação com base entre 0 e 1 (vídeo 5 e questão inédita 5 da revisão):** (1/3)ˣ > 9 dá x **<** −2; no forno, 0,5^(t/10) > 0,5³ dá t/10 **<** 3. A IA costuma manter o sentido. Na questão do forno, confira também se ela subtrai os 20 °C **antes** de dividir por 160.
- **Questão 5 (vídeo 4):** na semana 4, B (1 600) ainda perde para A (2 200). A resposta é **5** semanas (3 200 contra 2 500), não 4.
