# Logaritmos: definição, propriedades e equações — série de videoaulas

Material de apoio: `01-matematica/27-logaritmos-propriedades-equacoes.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Potências, expoente negativo, propriedades aᵐ · aⁿ = aᵐ⁺ⁿ | **Potenciação e radiciação** | Revisão relâmpago nos vídeos 1 e 2: as propriedades do log são "as de potência lidas de trás para frente". |
| Potências de 10, 10⁻ⁿ com n casas decimais, "cada ordem é ×10" | **Notação científica e ordem de grandeza** | Revisão relâmpago no vídeo 1 (log decimal "conta zeros" e conta algarismos). |
| Equações exponenciais de mesma base; 2ˣ = 10 "não fecha" | **Função exponencial, vídeo 5** | O vídeo 1 abre exatamente nessa pergunta deixada em aberto. |
| t = log(M/C) ÷ log(1 + i) e regra do 72 | **Juros Compostos** | Lá a fórmula veio pronta; no vídeo 3 mostro de onde ela vem. A regra do 72 entra só como conferência da Q1 (72 ÷ 8 = 9). Nenhuma questão de Juros Compostos é reutilizada (a Q1 daqui, a 8% para dobrar, é diferente das de lá). |
| Equação do 2º grau | **Equação do 2º grau (Bhaskara)** | Revisão de 30 s no vídeo 4. |
| pH, Richter, decibéis | **Função logarítmica e aplicações** (próxima série) | Só prometo. Nenhuma questão de escala aqui. |
| Meia-vida e tempo de dobrar com log | Função logarítmica não trata disso | Fica **aqui** (Q1 e Q8, vídeo 3). A série de Função exponencial resolve meia-vida só contando intervalos; aqui entra o caso que não fecha. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Logaritmo é um expoente: definição, condições e consequências** | 02, 03 | Q4 | 8–10 min |
| **2. As três propriedades e o kit log 2 e log 3** | 04, 06 | Q2, Q9, Q7 | 10–12 min |
| **3. Tirando a incógnita do expoente: equações com log e mudança de base** | 05, 07 | Q5, Q6, Q1, Q8 | 10–12 min |
| **4. Equações logarítmicas e a condição de existência** | 08 | Q3 | 6–8 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Vídeo 1: Logaritmo é um expoente: definição, condições e consequências

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Logaritmos: definição, propriedades e equações —
Episódio 1 de 5: Logaritmo é um expoente: definição, condições e consequências
RECORTE: use APENAS as seções 02 e 03 do material de apoio, mais a Questão 4 da seção
12. Potências e expoente negativo já foram ensinados na série de Potenciação e
radiciação; potências de 10 e "1 seguido de n zeros", na série de Notação científica:
aqui, revisão rápida. As propriedades ficam para o episódio 2. O logaritmo natural (ln)
é só citado.
DURAÇÃO: 8 a 10 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pela pergunta que a série de Função exponencial
   deixou aberta: "2 elevado a quanto dá 10?". Mostre que 2³ = 8 e 2⁴ = 16, e que a
   resposta está entre 3 e 4. Só depois dê nome a esse número.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (logaritmo, base, logaritmando, logaritmo decimal, logaritmo natural,
   condição de existência, algarismo).
3. Analogias âncora, retomadas ao longo da aula:
   - "logaritmo é uma pergunta: log_b a quer saber 'b elevado a quanto dá a?'";
   - "o logaritmo é só um expoente com nome próprio";
   - "o log decimal conta zeros: log 1 000 = 3, log 0,01 = −2".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: 2⁵ = 32, 3⁻² = 1/9,
   9^(1/2) = 3, a⁰ = 1 (série de Potenciação e radiciação); 10ⁿ é 1 seguido de n zeros
   e 10⁻ⁿ tem n casas decimais (série de Notação científica).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; todo logaritmo é lido
   em voz alta como pergunta antes de ser respondido.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Quantos algarismos tem 2¹⁰⁰? Ninguém faz essa conta na mão.
  Mas com um único número, log 2 ≈ 0,301, você responde em dez segundos. Ao final
  desta aula, você também."
- Promessa: "ao final, você vai ler qualquer logaritmo como uma pergunta, saber quando
  ele existe e usar o log para contar algarismos".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) a pergunta aberta: 2ˣ = 10 não fecha em potência inteira de 2;
  b) definição: log_b a = x ⇔ bˣ = a; b é a base, a é o logaritmando, x é o logaritmo;
  c) a tabela da seção 02, cada linha como pergunta: log_2 32 = 5; log_3 (1/9) = −2;
     log_9 3 = 1/2; log 1 000 = 3; log 0,01 = −2;
  d) notações: sem base escrita, log é decimal (base 10), o mais usado na prova; ln é
     o logaritmo natural, de base e ≈ 2,718 (só citar);
  e) condições de existência: a > 0, b > 0, b ≠ 1; por que o logaritmando é positivo
     (base positiva elevada a qualquer expoente dá positivo; não existe 10ˣ = 0 nem
     10ˣ = −5); o LOGARITMO, porém, pode ser negativo (log 0,01 = −2);
  f) consequências imediatas (tabela da seção 03): log_b 1 = 0; log_b b = 1;
     log_b bⁿ = n (log 10⁻⁷ = −7); b^(log_b a) = a (10^(log 7) = 7); log_b a = log_b c
     ⇔ a = c;
  g) contar algarismos: um número entre 10³⁰ e 10³¹ tem log entre 30 e 31 e é escrito
     com 31 algarismos; algarismos = parte inteira do log + 1.
- Exercício "nós fazemos": peça "pause: quanto vale log_5 125? E log 0,0001?"
  (5³ = 125 → 3; 10⁻⁴ = 0,0001 → −4).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Logaritmo é expoente: log_b a pergunta 'b elevado a quanto dá a?'."
  "O logaritmando é sempre positivo; o logaritmo pode ser negativo."
  "Algarismos = parte inteira do log + 1."
- Erros clássicos:
  • log 0 = 0 (log 0 não existe; quem vale zero é log 1);
  • 2¹⁰⁰ tem 30 algarismos (são 31: 10³⁰ já tem 31 algarismos).
- Questão no estilo ENEM: Questão 4 do material (algarismos de 2¹⁰⁰, log 2 ≈ 0,301):
  "nós fazemos". Diga "pause o vídeo e tente": log 2¹⁰⁰ = 100 · 0,301 = 30,1, logo
  10³⁰ < 2¹⁰⁰ < 10³¹, 31 algarismos. (Aqui use a regra "expoente desce multiplicando"
  só como aviso: "isso é do próximo episódio; confie por enquanto".) Explique as
  erradas: 30 esquece de somar 1; 100 confunde algarismos com o expoente; 101 soma 1 a
  esse expoente; 200 multiplica a base pelo expoente. Antes, mostre o caso pequeno:
  10³ = 1 000 tem log 3 e 4 algarismos.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "se log 2 ≈ 0,30 e log 3 ≈ 0,48, quanto vale log 6?
  E log 72? Sem calculadora. Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: a expressão log_2 32 se transformando num balão de pergunta
  "2 elevado a quanto dá 32?", e os 2 se multiplicando na tela até chegar a 32
  (cinco vezes); depois, a seta de ida e volta entre log_b a = x e bˣ = a.
- Uma régua de potências de 10 (0,01; 0,1; 1; 10; 100; 1 000) com os logs −2, −1, 0, 1,
  2, 3 embaixo, e um contador de algarismos acendendo.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Ficou claro que o LOGARITMANDO é positivo, mas o LOGARITMO pode ser negativo?
- Os valores da tabela (5, −2, 1/2, 3, −2) estão corretos?
- A Questão 4 termina em 31 algarismos, com a explicação do "+1"?
```

---

## Vídeo 2: As três propriedades e o kit log 2 e log 3

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Logaritmos: definição, propriedades e equações —
Episódio 2 de 5: As três propriedades e o kit log 2 e log 3
RECORTE: use APENAS as seções 04 e 06 do material de apoio, mais as Questões 2, 9 e 7 da
seção 12. As propriedades de potência e a fatoração em primos já foram ensinadas nas
séries de Potenciação e radiciação e de Divisibilidade, primos, MMC/MDC: aqui, revisão
rápida. A mudança de base fica para o episódio 3.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pela régua de cálculo, que multiplicava números
   somando comprimentos antes das calculadoras (o trecho de 1 a 2 emendado ao de 1 a 3
   chega ao 6); só depois escreva as propriedades.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (propriedade operatória, produto, quociente, potência, decomposição em
   fatores primos, régua de cálculo).
3. Analogias âncora, retomadas ao longo da aula:
   - "as propriedades do log são as regras de potência lidas de trás para frente: lá
     se somam expoentes quando se multiplica; aqui, o log do produto é a soma";
   - "o kit 2, 3 e 10: todo número feito de 2, 3 e 5 sai do kit, porque 5 = 10 ÷ 2";
   - "soma dentro do log é porta trancada: não tem regra".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: aᵐ · aⁿ = aᵐ⁺ⁿ,
   aᵐ ÷ aⁿ = aᵐ⁻ⁿ e (aᵐ)ⁿ = aᵐ·ⁿ (série de Potenciação e radiciação); 72 = 2³ · 3²
   (série de Divisibilidade, primos, MMC/MDC); log é expoente (episódio 1).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; antes de usar o kit,
   escreva a decomposição do número na tela; depois, confira se o resultado está entre
   os inteiros certos (72 está entre 10 e 100, então o log está entre 1 e 2).
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "log(10 + 10) é log 10 + log 10? Teste: log 20 ≈ 1,30, mas
  log 10 + log 10 = 2. A regra que 'parece óbvia' está errada, e a alternativa com ela
  sempre aparece."
- Promessa: "ao final, você vai usar as três propriedades e calcular o log de muitos
  números só com log 2 e log 3".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) produto vira soma: log_b (M · N) = log_b M + log_b N (vem de bˣ · bʸ = bˣ⁺ʸ); a
     régua de cálculo;
  b) quociente vira diferença: log_b (M/N) = log_b M − log_b N;
  c) expoente desce multiplicando: log_b Mᵏ = k · log_b M; vale para raiz:
     log √2 = log 2^(1/2) = (1/2) · log 2;
  d) o que as propriedades NÃO dizem: log(M + N) não tem regra; (log M)/(log N) não é
     log M − log N; o teste com números (log 20 ≈ 1,30 contra 2);
  e) o kit (tabela da seção 06), com log 2 ≈ 0,301 e log 3 ≈ 0,477: log 4 = 0,602;
     log 5 = 1 − 0,301 = 0,699; log 6 = 0,778; log 9 = 0,954; log 12 = 1,079;
     log 1,5 = 0,176; log 0,9 = 0,954 − 1 = −0,046; log 0,2 = 0,301 − 1 = −0,699;
  f) números menores que 1 têm log negativo: se log 0,9 saiu positivo, houve erro de
     sinal (isso decide as questões de decaimento do episódio 3).
- Exercício "nós fazemos": peça "pause: com log 2 = 0,30 e log 3 = 0,48, calcule
  log 18" (18 = 2 · 3²; 0,30 + 2 · 0,48 = 1,26; confere: 18 está entre 10 e 100).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Produto vira soma, quociente vira diferença, expoente desce multiplicando."
  "Soma dentro do log não tem regra."
  "Número entre 0 e 1 tem log negativo."
- Erros clássicos:
  • log(M + N) = log M + log N (só vale para M · N);
  • log M ÷ log N = log M − log N (a diferença é do log do quociente);
  • log 72 = log 8 · log 9 (o certo é log 8 + log 9);
  • log 0,9 > 0 (o certo é log 0,9 ≈ −0,046).
- Questões no estilo ENEM, nesta ordem:
  • Questão 2 do material (log 72 com log 2 = 0,30 e log 3 = 0,48): "eu faço".
    72 = 2³ · 3² → 0,90 + 0,96 = 1,86. Explique: 0,78 é log 6; 0,864 multiplica
    log 8 · log 9; 0,96 é só log 9; 1,38 é log 24 (esqueceu o expoente 2 do 3);
  • Questão 9 (log 2 = a, log 3 = b, pede log 1,5): "nós fazemos". log(3/2) = b − a.
    Explique: a − b é log(2/3), negativo; a + b é log 6; b/a é log_2 3; 1 + b − a é
    log 15 (confundiu 1,5 com 15);
  • Questão 7 (afirmações I a IV, verdadeiras e falsas): "você faz", com pausa.
    Verdadeiras: II e IV. Teste I com a = b = 10 e III com a = 100, b = 10.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "1,08ᵗ = 2: o t está preso no expoente e 2 não é
  potência de 1,08. Como derrubar esse t? Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: a régua de cálculo com o trecho de 1 a 2 sendo emendado ao de 1 a
  3 e chegando exatamente no 6; depois, a propriedade de potência bˣ · bʸ = bˣ⁺ʸ
  "girando" e virando log(M · N) = log M + log N.
- O kit: três caixinhas (2, 3, 10) e cada número da tabela sendo montado com elas, como
  peças de encaixe.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- As propriedades falsas foram derrubadas com um teste numérico?
- Os valores do kit (0,602; 0,699; 0,778; 0,954; 1,079; 0,176; −0,046; −0,699) estão
  corretos, com o sinal negativo nos números menores que 1?
- As respostas são 1,26 (exercício), 1,86 (Q2), b − a (Q9) e II e IV (Q7)?
```

---

## Vídeo 3: Tirando a incógnita do expoente: equações com log e mudança de base

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Logaritmos: definição, propriedades e equações —
Episódio 3 de 5: Tirando a incógnita do expoente: equações com log e mudança de base
RECORTE: use APENAS as seções 05 e 07 do material de apoio, mais as Questões 5, 6, 1 e 8
da seção 12. Equações exponenciais de mesma base e o fator de crescimento ou de
decaimento já foram ensinados na série de Função exponencial; a fórmula
t = log(M/C) ÷ log(1 + i) e a regra do 72 apareceram prontas na série de Juros
Compostos: aqui, revisão rápida e a origem da fórmula.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por perguntas de tempo ("em quantos anos meu
   dinheiro dobra?", "em quantas horas a cultura chega a 50 000?", "quando o
   equipamento vale a metade?"); só depois mostre a técnica.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (aplicar log dos dois lados, isolar a potência, mudança de base, numerador,
   denominador, estimativa).
3. Analogias âncora, retomadas ao longo da aula:
   - "o log é um elevador que traz o expoente para o térreo: aplique log dos dois lados
     e o t desce multiplicando";
   - "na mudança de base, a base vai para o porão: log_b a = log a ÷ log b";
   - "estime antes de calcular: se 3³ = 27 e 3⁴ = 81, a resposta de 3ᵗ = 50 mora entre
     3 e 4".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: log Mᵏ = k · log M e o
   kit log 2 e log 3 (episódio 2); fator 1,08 para 8% e 0,9 para perder 10% (série de
   Função exponencial); a fórmula de tempo e a regra do 72 (série de Juros Compostos).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; antes de toda divisão
   de logs, diga qual fica em cima e por quê, e no fim compare com a estimativa.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Um capital a 5% ao ano demora quanto para dobrar? Em juros
  simples, 20 anos. Em juros compostos, cerca de 14,2. Para achar esse 14,2 você
  precisa derrubar um t do expoente. Hoje você aprende a derrubar."
- Promessa: "ao final, você vai resolver qualquer equação exponencial que não fecha na
  mesma base, com os logs que o enunciado der".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) exemplo 1: 2ˣ = 10 → x · log 2 = log 10 → x = 1 ÷ 0,301 ≈ 3,32; no gráfico, a reta
     y = 10 encontra y = 2ˣ entre x = 3 (8) e x = 4 (16);
  b) mudança de base: log_b a = log a ÷ log b; exemplos log_2 10 = 1 ÷ 0,301 ≈ 3,32 e
     log_4 32 = log_2 32 ÷ log_2 4 = 5/2 = 2,5;
  c) quem fica em cima: o logaritmando no numerador, a base no denominador; conferência
     log_2 8 = 0,903 ÷ 0,301 = 3 (invertida, daria 1/3);
  d) exemplo 2: capital que dobra a 5% ao ano: 1,05ᵗ = 2 → t = 0,301 ÷ 0,0212 ≈ 14,2
     anos; em juros simples, 20 anos (100% ÷ 5%); "é daqui que vem a fórmula da série
     de Juros Compostos";
  e) isole a potência primeiro: 1 000 · 3ᵗ = 50 000 → 3ᵗ = 50; aplicar log direto exige
     lembrar que log(1 000 · 3ᵗ) = 3 + t · log 3, e não 3 · t · log 3;
  f) decaimento: o fator é menor que 1, os dois logs da divisão são negativos e o tempo
     sai positivo.
- Exercício "nós fazemos": peça "pause: resolva 2ˣ = 5, com log 2 = 0,30" (log 5 =
  1 − 0,30 = 0,70; x = 0,70 ÷ 0,30 ≈ 2,33; confere: 2² = 4 < 5 < 8 = 2³).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Aplique log dos dois lados e o expoente desce."
  "Isole a potência antes de aplicar o log."
  "Na mudança de base, a base vai para baixo."
- Erros clássicos:
  • log_2 10 = log 2 ÷ log 10 (o certo é log 10 ÷ log 2);
  • log(1 000 · 3ᵗ) = 3t · log 3 (o certo é 3 + t · log 3: o 1 000 vira parcela);
  • log 0,9 positivo na conta de decaimento.
- Questões no estilo ENEM, nesta ordem:
  • Questão 5 do material (fungos: 4ᵗ = 32): "eu faço", pelos dois caminhos (mudança de
    base, 5/2 = 2,5, e mesma base, 2^(2t) = 2⁵). Conferência: 16 vezes em 2 semanas,
    64 em 3. Explique: 0,4 inverte a fração; 2 para na última semana inteira; 8 divide
    32 por 4; 28 subtrai;
  • Questão 6 (bactérias: 1 000 · 3ᵗ = 50 000, log 2 = 0,30, log 3 = 0,48): "nós
    fazemos". 3ᵗ = 50; log 50 = log(100/2) = 2 − 0,30 = 1,70; t = 1,70 ÷ 0,48 ≈ 3,54.
    Explique: 0,28 inverte; 1,22 subtrai os logs; 16,7 divide 50 por 3 (linear); 104
    divide 50 por log 3 sem tirar o log de 50;
  • Questão 1 (capital a 8% ao ano dobra; log 2 = 0,30, log 1,08 = 0,033): "você faz",
    com pausa. t = 0,30 ÷ 0,033 ≈ 9,1 anos; confira pela regra do 72 (72 ÷ 8 = 9).
    Explique: 0,11 inverte; 0,27 subtrai os logs; 12,5 é juros simples; 25 divide 2 pela
    taxa;
  • Questão 8 (equipamento perde 10% ao ano, vale a metade; log 2 = 0,301,
    log 3 = 0,477): "você faz", com pausa. 0,9ᵗ = 0,5; log 0,9 = 2 · 0,477 − 1 = −0,046;
    log 0,5 = −0,301; t = −0,301 ÷ (−0,046) ≈ 6,5 anos. Explique: 0,15 inverte a
    divisão; 0,32 usa log 9 = 0,954 no lugar de log 0,9 (0,301 ÷ 0,954 ≈ 0,32, deixando
    o sinal de lado); 5 anos supõe perda linear (50% ÷ 10%); 10 anos confunde metade
    com perder tudo, também linear.
  Em todas: isole a potência, aplique log, diga quem fica em cima, compare com a
  estimativa.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "log_2 x + log_2 (x − 2) = 3 tem duas raízes no papel,
  mas só uma vale. Qual, e por quê? Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: um elevador com o rótulo "log" que desce o t do expoente até a
  linha do número (1,05ᵗ = 2 → t · log 1,05 = log 2); depois, a fração log a ÷ log b
  com a base caindo para o "porão".
- O gráfico de y = 2ˣ com a reta y = 10 cruzando entre x = 3 e x = 4, e o valor 3,32
  marcado.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Em todas as divisões de logs, o logaritmando ficou em cima?
- Na Questão 8, os dois logs são negativos e o tempo sai positivo (cerca de 6,5 anos)?
- As respostas são 2,5; 3,54; cerca de 9 anos; 6,5 anos, e a estimativa foi feita antes?
```

---

## Vídeo 4: Equações logarítmicas e a condição de existência

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Funções — Logaritmos: definição, propriedades e equações —
Episódio 4 de 5: Equações logarítmicas e a condição de existência
RECORTE: use APENAS a seção 08 do material de apoio (e o hábito 3 da seção 09), mais a
Questão 3 da seção 12. A equação do 2º grau já foi ensinada na série de Equação do
2º grau: aqui, revisão rápida.
DURAÇÃO: 6 a 8 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma "porta com segurança" que só deixa
   entrar números positivos, e mostre um candidato a solução sendo barrado; só depois
   apresente as equações.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (equação logarítmica, condição de existência, raiz, raiz estranha, conjunto
   solução, conjunto vazio).
3. Analogias âncora, retomadas ao longo da aula:
   - "a condição de existência é o segurança na porta do log: só entra número positivo";
   - "toda raiz precisa mostrar documento: substitua nos logaritmandos ORIGINAIS antes
     de aceitar";
   - "junte os logs como quem junta peças: até sobrar um só de cada lado".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: definição de log e
   condições de existência (episódio 1); log M + log N = log(M · N) (episódio 2);
   resolver x² + 3x − 10 = 0 (série de Equação do 2º grau).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; escreva as condições
   de existência no canto da tela no começo e use-as no fim.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Numa equação logarítmica que vira equação do 2º grau, a
  alternativa com as duas raízes SEMPRE está lá. E quase sempre está errada."
- Promessa: "ao final, você vai resolver equações logarítmicas em quatro passos e nunca
  mais aceitar uma raiz proibida".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) o roteiro da seção 08: 1) escreva as condições de existência; 2) junte os logs com
     as propriedades; 3) elimine o log pela definição ou pela igualdade de
     logaritmandos; 4) resolva e descarte o que viola as condições;
  b) tipo 1, pela definição: log_3 (x − 1) = 2 → x − 1 = 3² → x = 10;
  c) tipo 2, mesma base dos dois lados: log_2 (3x − 1) = log_2 (x + 5) → 3x − 1 = x + 5
     → x = 3;
  d) tipo 3, juntando com as propriedades: log x + log(x + 3) = 1 → x(x + 3) = 10 →
     x² + 3x − 10 = 0 → raízes 2 e −5; −5 é descartada, porque log(−5) não existe.
- Exercício "nós fazemos": peça "pause: resolva log_2 (x + 3) = 4" (x + 3 = 2⁴ = 16 →
  x = 13; confere: 13 + 3 = 16 > 0).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Escreva as condições de existência antes de começar."
  "Junte os logs até sobrar um só de cada lado."
  "Toda raiz precisa passar no teste do logaritmando positivo."
- Erros clássicos:
  • aceitar x = −5 em log x + log(x + 3) = 1 (verifique cada raiz nos logaritmandos
    originais);
  • somar os logaritmandos em vez de multiplicá-los.
- Questão no estilo ENEM: Questão 3 do material (log_2 x + log_2 (x − 2) = 3): "você
  faz", com pausa. Condições: x > 0 e x > 2. x² − 2x = 8 → x = 4 ou x = −2; só 4 vale.
  Conferência: log_2 4 + log_2 2 = 2 + 1 = 3. Explique: {−2, 4} esquece de verificar;
  {−2} fica justamente com a raiz proibida; {5} soma os logaritmandos
  (log_2 (2x − 2) = 3); ∅ descarta também a raiz válida.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "no último episódio deste assunto, juntamos tudo,
  caçamos as pegadinhas e treinamos com tempos de crescimento, decaimento e contas com
  log 2 e log 3."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: um segurança na porta do log conferindo o "documento" de cada
  raiz; o 4 entra com selo verde, o −2 é barrado com selo vermelho "log(−2) não
  existe".
- O roteiro de 4 passos como uma lista que vai sendo riscada durante a resolução.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- As condições de existência foram escritas no começo e usadas no fim?
- As raízes foram testadas nos logaritmandos ORIGINAIS (x e x − 2), e não na equação do
  2º grau?
- As respostas são x = 13 (exercício) e {4} (Questão 3)?
```

---

## Vídeo 5: Revisão (Logaritmos no ENEM)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula de REVISÃO para o YouTube sobre:

TEMA: Matemática — Funções — Logaritmos: definição, propriedades e equações —
Episódio 5 de 5: Revisão geral, estratégia de prova, pegadinhas e treino para o ENEM
RECORTE: use as seções 01, 09, 10, 11 e 13 do material de apoio.
NÃO reutilize as Questões 1 a 9 da seção 12 (já resolvidas nos episódios anteriores).
As escalas de pH, Richter e decibéis terão série própria (a próxima): aqui, só cite a
ponte, sem resolver questões de escala.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que assistiu aos episódios 1 a 4, mas ainda é iniciante e pode ter esquecido
partes. Relembre cada conceito em uma frase simples antes de cobrá-lo.

REGRAS DE EXPLICAÇÃO
1. Cada conceito é relembrado com a mesma analogia âncora usada no seu episódio:
   o logaritmo como pergunta e como expoente com nome próprio; o log decimal que conta
   zeros; as regras de potência lidas de trás para frente; o kit 2, 3 e 10; a soma
   dentro do log como porta trancada; o elevador que desce o expoente; a base no
   porão; a estimativa entre dois inteiros; o segurança na porta do log.
2. Prática de recuperação: antes de explicar, PERGUNTE e peça para o aluno pausar.
3. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
4. Uma ideia por cena. Frases curtas. Tom de conversa, falando com "você".

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "No ENEM, o logaritmo quase nunca é o tema da questão: ele é a
  ferramenta. O enunciado diz 'use log 2 = 0,30' e espera que você descubra um tempo,
  uma contagem ou um expoente. Hoje você treina a ferramenta."
- O que a prova cobra (seção 01): descobrir um tempo; calcular com valores dados
  (log 72, log 1,5 a partir de log 2 e log 3); resolver equações logarítmicas simples
  respeitando as condições de existência; interpretar escalas (só citar: próxima
  série). O que rende mais: ler log_b a como "b elevado a quanto dá a?".
- Onde aparece nas outras áreas (seção 10): Química (pH = −log[H⁺]: cada unidade é um
  fator 10), Física (decibéis: +10 dB, intensidade 10 vezes maior), Geografia
  (magnitude de terremotos: um grau a mais, amplitude 10 vezes maior), Matemática
  Financeira (t = log(M/C) ÷ log(1 + i)), Química e Biologia (meia-vida e culturas:
  tempo = log da razão ÷ log do fator). Diga que as escalas são o próximo assunto.
- A estratégia de prova em 3 hábitos (seção 09): decomponha antes de calcular (tudo em
  2, 3 e 10: 72 = 2³ · 3², 50 = 100/2, 0,9 = 9/10); estime a resposta antes de marcar
  (3ᵗ = 50 fica entre 3 e 4); desconfie da alternativa com duas raízes.
- "Verdadeiro ou falso? Pause e responda": transforme em afirmações os 9 erros da
  seção 11 (log(M + N) = log M + log N; log M ÷ log N = log M − log N;
  log 72 = log 8 · log 9; log_2 10 = log 2 ÷ log 10; log 0,9 > 0; log 0 = 0; aceitar
  x = −5 em log x + log(x + 3) = 1; log(1 000 · 3ᵗ) = 3t · log 3; 2¹⁰⁰ tem 30
  algarismos). Para cada um: pausa → resposta → por que a pegadinha engana → a regra
  certa em uma frase.
- 5 questões INÉDITAS no estilo ENEM, criadas por você, com situações hipotéticas e
  5 alternativas cada:
  1) log por decomposição: com log 2 = 0,30 e log 3 = 0,48, calcule log 0,6.
     Correta: −0,22 (0,6 = 6/10; 0,78 − 1). Erradas: −0,78 (sinal trocado e esqueceu o
     ÷10), 0,144 (multiplicou log 2 · log 3), 0,22 (erro de sinal), 0,78 (é log 6,
     esqueceu o ÷10);
  2) tempo de crescimento: uma cultura cresce 25% por hora; em quanto tempo dobra?
     Dê só log 2 = 0,30 e peça para obter log 1,25 = log(10/8) = 1 − 3 · 0,30 = 0,10.
     Correta: 3 h (0,30 ÷ 0,10; confere: 1,25³ ≈ 1,95). Erradas: 0,2 h (subtraiu os
     logs), cerca de 0,33 h (inverteu a divisão), 4 h (crescimento linear: 100% ÷ 25%),
     8 h (dividiu 2 pela taxa 0,25);
  3) tempo de decaimento: um lago perde 20% de um poluente por mês, sempre sobre o que
     restou; em quanto tempo resta a metade? Use log 2 = 0,30.
     Correta: 3 meses (0,8ᵗ = 0,5; log 0,8 = 0,90 − 1 = −0,10; log 0,5 = −0,30;
     confere: 0,8³ = 0,512). Erradas: cerca de 0,33 mês (inverteu a divisão), cerca de
     0,43 mês (usou a taxa 0,2 como fator: log 0,2 = −0,70), 2,5 meses (perda linear:
     50% ÷ 20%), 5 meses (confundiu metade com perder tudo, linear);
  4) equação logarítmica: conjunto solução de log_3 x + log_3 (x − 8) = 2.
     Correta: {9} (x² − 8x − 9 = 0 → 9 ou −1; condições x > 8; confere:
     log_3 9 + log_3 1 = 2 + 0). Erradas: {−1} (ficou com a raiz proibida), {−1, 9}
     (não verificou), {8,5} (somou os logaritmandos: 2x − 8 = 9), ∅ (descartou também a
     raiz válida);
  5) contar algarismos: quantos algarismos tem 3⁵⁰? Use log 3 = 0,477.
     Correta: 24 (50 · 0,477 = 23,85). Erradas: 23 (esqueceu o +1), 50 (confundiu com
     o expoente), 51 (somou 1 ao expoente), 150 (multiplicou a base pelo expoente).
  As alternativas erradas devem ser exatamente os erros clássicos. Leia, peça a pausa,
  decomponha, estime, resolva e explique cada alternativa.
- Checklist de domínio (seção 13): leia os itens e diga "marque só o que você
  conseguiria explicar em voz alta para outra pessoa, sem consultar nada; o que não
  marcou, reveja o episódio correspondente" (definição, condições, logs de cabeça,
  consequências e algarismos → episódio 1; propriedades, propriedades falsas e kit
  log 2 e log 3 → episódio 2; mudança de base, equações exponenciais com log e tempo
  de dobrar ou cair à metade → episódio 3; equações logarítmicas e verificação das
  raízes → episódio 4).
- Meta antes de considerar dominado: resolver 30 questões e acertar pelo menos 21
  (70%), com pelo menos dez que dão log 2 e log 3 no enunciado.
- Encerramento e ponte: "o próximo assunto é Função logarítmica e aplicações (pH,
  Richter, decibéis), onde estas contas viram as escalas do mundo real: quantas vezes
  mais ácido, quantas vezes mais energia, quantas vezes mais barulho."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Use um cronômetro visual nas pausas; um selo "PEGADINHA" em amarelo nos erros; um
  ícone de área (tubo de ensaio, cifrão, gota, lápis) em cada questão inédita; os 4
  ícones dos episódios (balão de pergunta, régua de cálculo, elevador, segurança na
  porta) como índice visual da revisão.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Cada conceito foi relembrado antes de ser cobrado?
- As 5 questões inéditas têm uma única alternativa correta e contas corretas
  (−0,22; 3 h; 3 meses; {9}; 24 algarismos)?
- Nas questões 2 e 3, o log do fator (log 1,25 = 0,10 e log 0,8 = −0,10) foi obtido do
  log 2 com o sinal certo?
```

---

## Cuidados ao revisar os roteiros

- **Sinal em decaimento (vídeo 3, Q8, e inédita 3):** log 0,9 = 0,954 − 1 = **−0,046** e log 0,8 = **−0,10**. A IA costuma escrever log 0,9 ≈ 0,954 (esquece o −1) ou apresentar o tempo como negativo. Os dois logs da divisão são negativos e o tempo sai positivo (cerca de 6,5 anos; 3 meses).
- **Mudança de base:** log_2 10 = log 10 ÷ log 2 = 1 ÷ 0,301 ≈ **3,32**, não 0,301. Confira em toda fração de logs se o logaritmando está no numerador (log_4 32 = 2,5, não 0,4).
- **Distrator B da Q8:** a explicação do material ("usa log 9 = 0,954 no lugar de log 0,9") só leva a 0,32 se o sinal do −0,301 for ignorado (0,301 ÷ 0,954 ≈ 0,32). Deixei isso explícito no roteiro; a IA não deve escrever "−0,32 ano" como alternativa.
- **Contar algarismos (vídeo 1 e inédita 5):** 2¹⁰⁰ tem **31** algarismos (log = 30,1) e 3⁵⁰ tem **24** (log = 23,85). A IA às vezes responde a parte inteira (30, 23).
