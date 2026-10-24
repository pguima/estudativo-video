# Juros Compostos e Montante — série de videoaulas

Material de apoio: `01-matematica/14-juros-compostos-montante.html` · Incidência: Média

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Fator (1 + i), variações sucessivas (multiplicar fatores), "três aumentos de 10% = 1,1³ = 1,331", voltar ao valor original dividindo pelo fator | **Porcentagem** | Revisão relâmpago. A **Questão 5** (+10%, +20%, −25%) começa igual à Q3 de Porcentagem (1,10 · 1,20 = 1,32): uso, mas digo "o 1,32 você já conhece" e o foco fica no ×0,75 e no resultado negativo. |
| Capital, taxa, montante, J = M − C; juros simples como reta e PA | **Juros simples** (série anterior) | Revisão relâmpago. A comparação reta × curva é o conteúdo novo do vídeo 2. |
| Potências (1,1² = 1,21; propriedades da potência) | **Potenciação e radiciação** | Só revisão das propriedades (aᵐ⁺ⁿ = aᵐ · aⁿ; a²ⁿ = (aⁿ)²), aplicadas a fatores. |
| Converter taxa anual em mensal em compostos; 1,02¹² ≈ 26,8% | **Taxas equivalentes e inflação** (série própria) | Só o aviso "dividir por 12 não funciona aqui; isso tem série própria". Não calculo taxa equivalente nem mostro 1,02¹². |
| t = log(M/C) ÷ log(1 + i) | **Logaritmos** (série própria) | Uso a fórmula como ferramenta pronta, com os logs dados no enunciado. As propriedades ficam para a série própria. |
| Montante como PG e como exponencial; duplicação; decaimento (0,8ᵗ) | **Função exponencial** e **Progressão geométrica** (séries próprias) | Só reconhecer "multiplica pelo mesmo fator = PG / exponencial" e a duplicação sucessiva (Q9). Meia-vida e gráfico da exponencial ficam para as séries próprias. |
| Lucro, desconto, margem sobre custo × venda | **Descontos, acréscimos, lucro e prejuízo** (próxima série) | Só a ponte no fim da revisão. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. Juros sobre juros e a fórmula M = C · (1 + i)ᵗ** | 02, 03 | Q1, Q5 | 10–12 min |
| **2. Simples × compostos: reta e curva, PA e PG** | 04, 08 | Q4, Q8, Q9 | 10–12 min |
| **3. Potências sem calculadora e descobrir o tempo** | 05, 06 | Q6, Q7, Q2 | 10–12 min |
| **4. Trazendo valores para hoje** | 07 | Q3 | 6–8 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Vídeo 1: Juros sobre juros e a fórmula M = C · (1 + i)ᵗ

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática Básica — Juros Compostos e Montante — Episódio 1 de 5:
Juros sobre juros e a fórmula M = C · (1 + i)ᵗ
RECORTE: use APENAS as seções 02 e 03 do material de apoio, mais as Questões 1 e 5 da
seção 12. Capital, taxa, juros e montante foram ensinados na série de Juros simples, e o
fator (1 + i) e as variações sucessivas, na série de Porcentagem: aqui, revisão rápida.
Converter taxa anual em mensal em juros compostos tem série própria (Taxas equivalentes e
inflação): aqui, só o aviso.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pela dívida do cartão de crédito que "cresce
   sozinha" e pela poupança que rende sobre o que já rendeu, e só depois apresente a
   fórmula.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (juros compostos, saldo, capitalizar, incorporar os juros, fator de
   capitalização, expoente).
3. Analogias âncora, retomadas ao longo da aula:
   - "a bola de neve: a cada volta ela pega neve sobre a neve que já tinha, e cresce cada
     vez mais rápido";
   - "pense em fatores, não em porcentagens somadas: cada período MULTIPLICA o saldo por
     (1 + i)";
   - "o expoente conta quantas vezes o fator foi aplicado: três anos, três
     multiplicações".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: o fator de aumento
   (10% → 1,10) e as variações sucessivas multiplicando fatores (série de Porcentagem);
   capital, juros e montante (série de Juros simples); potência como multiplicação
   repetida (série de Potenciação).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; escreva primeiro o fator
   de UM período e só depois a potência.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "R$ 1.000,00 a 10% ao mês. Em juros simples, depois de 4 meses,
  R$ 1.400,00. Em juros compostos, R$ 1.464,10. Os mesmos 10%. Quem cria esses R$ 64,10 a
  mais são os juros que passaram a render juros."
- Promessa: "ao final, você vai calcular qualquer montante em juros compostos e
  encadear taxas diferentes sem somar porcentagens".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) definição: os juros de cada período são calculados sobre o saldo anterior, que já
     inclui os juros acumulados;
  b) a tabela da seção 02 (R$ 1.000,00 a 10% a.m.): juros compostos de 100, 110, 121 e
     133,10; saldos 1.100, 1.210, 1.331 e 1.464,10; em juros simples, 100 todo mês;
  c) no primeiro período os dois regimes empatam; a diferença nasce no segundo e cresce
     sem parar;
  d) a fórmula: cada mês multiplica por (1 + i), então t meses multiplicam por
     (1 + i)ᵗ: M = C · (1 + i)ᵗ; o fator de capitalização;
  e) os juros saem por diferença: J = M − C (não há fórmula direta);
  f) o exemplo de R$ 5.000,00 a 2% a.m. por 3 meses: 1,02³ = 1,061208;
     M = R$ 5.306,04; J = R$ 306,04; em simples seriam R$ 300,00; os R$ 6,04 são os
     juros sobre os juros;
  g) taxa e tempo no mesmo período (como em juros simples), mas aqui dividir a taxa
     anual por 12 NÃO funciona ("isso tem série própria"; nas questões deste assunto, a
     taxa já vem no período certo);
  h) taxas diferentes em sequência: multiplique os fatores de cada período (revisão de
     Porcentagem).
- Exercício "nós fazemos": peça "pause: R$ 2.000,00 a juros compostos de 10% ao mês,
  durante 2 meses. Qual é o montante e quanto foi de juros?" (1,1² = 1,21; M = R$ 2.420,00;
  J = R$ 420,00; em simples seriam R$ 400,00).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Juros compostos: juros sobre juros, como bola de neve."
  "Cada período multiplica o saldo por 1 + i."
  "Os juros saem por diferença: montante menos capital."
- Erros clássicos:
  • calcular C · (1 + i · t) quando o regime é composto;
  • somar as taxas dos períodos (10% por 2 anos em compostos é 21%, não 20%);
  • responder o montante quando pedem os juros, ou o contrário;
  • contar um período a mais (três anos são expoente 3).
- Questões no estilo ENEM, nesta ordem:
  • Questão 1 do material (R$ 10.000,00 a 10% a.a. por 3 anos): "eu faço". 1,1³ = 1,331 →
    R$ 13.310,00 (C). B é o montante em juros simples; A são só os juros; E usa
    expoente 4; D é o montante simples de 4 anos;
  • Questão 5 (+10%, +20%, −25%): "você faz", com pausa. Diga "o 1,10 · 1,20 = 1,32 você
    já conhece da série de Porcentagem"; depois 1,32 · 0,75 = 0,99 → perda de 1% (A).
    B soma as taxas (10 + 20 − 25 = 5); D soma só os ganhos; C acerta o tamanho e erra o
    sinal; E acha que ganhos e perda "quase se anulam", mas a perda incide sobre um valor
    maior.
  Em ambas: leia o enunciado, escreva o fator de cada período, resolva e explique as
  alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "se juros compostos são juros sobre juros, eles sempre
  rendem mais que os simples, certo? Errado: existe um prazo em que os simples ganham.
  Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: a tabela da seção 02 sendo montada mês a mês, com duas colunas de
  moedas: na de juros simples, sempre 100 moedas novas; na de juros compostos, 100, 110,
  121, 133,10, com as moedas novas "nascendo" também das moedas de juros anteriores.
- Uma bola de neve rolando e crescendo, com o fator ×1,1 escrito a cada volta.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Ficou claro por que os juros de cada mês CRESCEM em juros compostos?
- As contas (1.464,10; 1,061208; 5.306,04; 2.420; 13.310; 0,99) estão corretas?
- O expoente é sempre o número de períodos de capitalização?
```

---

## Vídeo 2: Simples × compostos (reta e curva, PA e PG)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática Básica — Juros Compostos e Montante — Episódio 2 de 5:
Simples × compostos — reta e curva, PA e PG
RECORTE: use APENAS as seções 04 e 08 do material de apoio, mais as Questões 4, 8 e 9 da
seção 12. O montante simples como reta e como PA foi ensinado na série de Juros simples:
aqui, revisão rápida. Função exponencial e progressão geométrica têm séries próprias:
aqui, só reconhecer "multiplica pelo mesmo fator" e citar. Decaimento (fator menor que
1) fica só citado.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por duas propostas de empréstimo "com a mesma taxa"
   e pela pergunta de um cliente: "qual é mais barata?". Depois, por um investimento que
   "dobra a cada 7 anos".
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (reta, curva exponencial, progressão geométrica, razão da PG, tempo de
   duplicação, decaimento).
3. Analogias âncora, retomadas ao longo da aula:
   - "a reta é uma escada de degraus iguais; a curva é uma escada em que cada degrau é
     10% mais alto que o anterior";
   - "o cruzamento em t = 1: antes de um período, a reta fica por cima; depois, a curva
     dispara";
   - "dobrar, dobrar, dobrar: três duplicações multiplicam por 8, não por 3".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: montante simples como
   reta e PA de razão C · i (série de Juros simples) e M = C · (1 + i)ᵗ (episódio 1).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; compare SEMPRE os dois
   fatores lado a lado (simples 1 + i · t; compostos (1 + i)ᵗ).
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Um banco oferece duas modalidades de empréstimo com a mesma
  taxa de 10% ao mês, uma simples e uma composta. Quase todo mundo diz 'a composta é
  sempre mais cara'. Para um empréstimo de 15 dias, é o contrário."
- Promessa: "ao final, você vai saber qual regime rende mais em cada prazo, reconhecer a
  reta e a curva e calcular duplicações sucessivas".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) a tabela comparativa da seção 04: juros sobre o capital × sobre o saldo; soma C · i
     × multiplica por 1 + i; PA × PG; reta × curva exponencial;
  b) o gráfico da seção 04: R$ 100,00 a 10% a.a.; reta e curva partem do mesmo ponto e se
     encontram em t = 1; em 10 anos, 259 contra 200;
  c) quem rende mais depende do prazo: antes de um período, simples (meio ano a 10% a.a.:
     1,05 contra cerca de 1,0488); em um período, empate (1,10); depois, compostos;
  d) por isso juros de mora de poucos dias são cobrados em simples (ligação com a série
     de Juros simples);
  e) montante como PG de razão 1 + i e como exponencial de base maior que 1 (só cite:
     "PG e função exponencial têm séries próprias");
  f) a marca da exponencial: tempo de duplicação constante; dobra em 7 anos, dobra de
     novo nos 7 seguintes; em 21 anos, × 2³ = 8;
  g) decaimento, só citado: um bem que perde 20% ao ano vale V₀ · 0,8ᵗ.
- Exercício "nós fazemos": peça "pause: R$ 1.000,00 a 20% ao ano por 2 anos. Quanto dá em
  juros simples e quanto em juros compostos?" (simples: 1 + 0,2 · 2 = 1,40 → R$ 1.400,00;
  compostos: 1,2² = 1,44 → R$ 1.440,00).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Simples soma; composto multiplica."
  "Antes de um período, o simples rende mais; depois, o composto."
  "Cada duplicação multiplica por 2: três duplicações, vezes 8."
- Erros clássicos:
  • achar que juros compostos sempre rendem mais (só depois do primeiro período);
  • decidir pela regra geral sem fazer a conta (taxa maior nem sempre rende mais);
  • multiplicar pelo número de duplicações em vez de elevar 2 a esse número.
- Questões no estilo ENEM, nesta ordem:
  • Questão 4 do material (10% a.m., simples × compostos): "eu faço", comparando os
    fatores em meio mês (1,05 × cerca de 1,049), um mês (1,10 × 1,10) e dois meses
    (1,20 × 1,21) → alternativa C. A é a crença comum; B ignora que os regimes são
    diferentes; D inverte as faixas; E vale só para prazos menores que um mês;
  • Questão 8 (R$ 50.000,00 por 2 anos: I simples a 22% a.a.; II compostos a 20% a.a.):
    "nós fazemos". I: 50.000 · 0,22 · 2 = R$ 22.000,00; II: 50.000 · (1,44 − 1) =
    R$ 22.000,00 → empate (E). A calcula a II como simples (R$ 20.000,00); C e D concluem
    pela regra geral sem conta; B inverte a comparação errada da A;
  • Questão 9 (dobra a cada 7 anos, R$ 5.000,00, 21 anos): "você faz", com pausa.
    5.000 · 2³ = R$ 40.000,00 (D). A multiplica por 3; B soma 5.000 por período, como em
    juros simples; C multiplica por 2 · 3; E soma o capital de novo ao montante.
  Em todas: leia o enunciado, diga "pause o vídeo e tente", resolva e explique as
  alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "a prova não deixa você calcular 1,05 elevado a 12 na
  mão. Ela dá uma pista, tipo '1,05⁶ ≈ 1,34'. O que fazer com ela? Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: o gráfico da seção 04, com a reta (azul) e a curva (roxa) partindo
  de 100; um zoom entre t = 0 e t = 1 mostrando a reta ligeiramente acima; o ponto de
  encontro em t = 1 destacado; depois a curva disparando até 259 contra 200 em t = 10.
- Uma pilha de notas que vira 2, depois 4, depois 8 pilhas, uma duplicação a cada 7 anos
  (Questão 9).
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Ficou claro que, para prazos menores que um período, os juros simples rendem mais?
- As contas (1,05 × 1,049; 1.400 × 1.440; 22.000 × 22.000; 40.000) estão corretas?
- PG e exponencial foram apenas citadas, sem invadir as séries próprias?
```

---

## Vídeo 3: Potências sem calculadora e descobrir o tempo

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática Básica — Juros Compostos e Montante — Episódio 3 de 5:
Potências sem calculadora e como descobrir o tempo
RECORTE: use APENAS as seções 05 e 06 do material de apoio, mais as Questões 6, 7 e 2 da
seção 12. As propriedades das potências foram ensinadas na série de Potenciação: aqui,
revisão rápida. Logaritmos têm série própria: aqui, use a fórmula
t = log(M/C) ÷ log(1 + i) como ferramenta pronta, com os logaritmos dados no enunciado, e
diga "por que o log 'derruba' o expoente fica para a série de Logaritmos".
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece pela dívida de R$ 2.000,00 no cartão a 5% ao mês
   ("quanto vira em um ano se ninguém pagar?") e pela pergunta "em quanto tempo meu
   dinheiro dobra?".
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (potência, expoente, quebrar o expoente, combinar potências, tentativa,
   logaritmo dado, regra do 72, estimativa).
3. Analogias âncora, retomadas ao longo da aula:
   - "multiplicar por 1,1 é somar a décima parte: 1,331 + 0,1331 = 1,4641";
   - "dobrar o tempo é elevar o fator ao quadrado, não dobrar o fator";
   - "a regra do 72 é o radar: em segundos, ela diz se a resposta está perto de 7 anos ou
     de 25".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: M = C · (1 + i)ᵗ
   (episódio 1) e as propriedades aᵐ⁺ⁿ = aᵐ · aⁿ e (aⁿ)² = a²ⁿ (série de Potenciação).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; trabalhe com fatores
   até o fim e só converta em reais na última linha.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "O enunciado diz: '1,05⁶ ≈ 1,34'. A pergunta é sobre 12 meses.
  Quem faz 2 vezes 1,34 erra. Quem faz 1,34 ao quadrado acerta. Essa é a diferença entre
  pensar em juros simples e pensar em juros compostos."
- Promessa: "ao final, você vai usar as potências que o enunciado der, descobrir o tempo
  por tentativa ou por logaritmo e estimar com a regra do 72".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) técnica 1, multiplicar passo a passo: 1,1² = 1,21; 1,1³ = 1,331; 1,1⁴ = 1,4641;
     1,1⁵ = 1,61051;
  b) técnica 2, quebrar o expoente: (1 + i)²ⁿ = [(1 + i)ⁿ]²; com 1,03¹⁰ ≈ 1,34, vinte
     meses dão 1,34² ≈ 1,80 (exato: 1,7956);
  c) técnica 3, combinar potências: (1 + i)ᵃ⁺ᵇ = (1 + i)ᵃ · (1 + i)ᵇ; 1,1⁷ ≈ 1,61 · 1,21
     ≈ 1,95;
  d) dobrar o tempo não dobra o fator: 1,34² ≈ 1,80, nem 2 · 1,34 nem 1,68;
  e) descobrir o tempo por tentativa: a 10% a.m., para passar de 1,6 vez o capital,
     1,1⁴ ≈ 1,46 não basta e 1,1⁵ ≈ 1,61 basta → 5 meses;
  f) com logaritmos dados: t = log(M/C) ÷ log(1 + i); dobrar a 10% a.a.:
     0,301 ÷ 0,041 ≈ 7,3 anos; o enunciado sempre dá os logs;
  g) a regra do 72: tempo para dobrar ≈ 72 ÷ taxa em %; 10% → cerca de 7,2; 6% → 12;
     8% → 9; boa entre 2% e 20%;
  h) o tempo de dobrar não vale para triplicar: use log 3; dobrar duas vezes é
     quadruplicar.
- Exercício "nós fazemos": peça "pause: considere 1,02¹⁰ ≈ 1,22. Qual é o fator de 20
  meses a 2% ao mês? E, pela regra do 72, em quanto tempo um capital dobra a 9% ao ano?"
  (1,22² = 1,4884 ≈ 1,49; 72 ÷ 9 = 8 anos).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Dobrar o tempo é elevar o fator ao quadrado."
  "O tempo está no expoente: tentativa, logaritmo ou regra do 72."
  "Divida pelo log do fator, nunca pela taxa."
- Erros clássicos:
  • dobrar o fator quando o tempo dobra (2 · 1,34);
  • somar as taxas de dois períodos (34% + 34% = 68%);
  • dividir log 2 pela taxa em vez de dividir por log (1 + i);
  • usar o tempo de dobrar para triplicar.
- Questões no estilo ENEM, nesta ordem:
  • Questão 6 do material (R$ 2.000,00 no cartão a 5% a.m.; 1,05⁶ ≈ 1,34; 12 meses):
    "eu faço". 1,34² = 1,7956 → cerca de R$ 3.590,00 (D). A usa só o fator de 6 meses;
    B é juros simples (60%); C soma as taxas dos dois semestres (68%); E multiplica o
    fator por 2;
  • Questão 7 (R$ 1.000,00 a 10% a.m.; 1,1⁴ ≈ 1,46 e 1,1⁵ ≈ 1,61; meta R$ 1.600,00):
    "nós fazemos", por tentativa → 5 meses (B). C é juros simples (1.000 + 100 · 6);
    A para em 1,46; D conta um mês a mais; E divide 1.600 por 100;
  • Questão 2 (triplicar a 20% a.a.; log 2 ≈ 0,30, log 3 ≈ 0,48, log 1,2 ≈ 0,08): "você
    faz", com pausa. t = 0,48 ÷ 0,08 = 6 anos (B); conferência: 1,2⁶ ≈ 2,99. A é o tempo
    para dobrar (o log 2 foi dado para atrair esse erro); C supõe o dobro do tempo de
    dobrar (isso seria quadruplicar); D é triplicar em juros simples; E é o erro simples
    de fazer J = 3C.
  Em todas: leia o enunciado, procure as potências ou logs fornecidos, resolva e explique
  as alternativas erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "e o caminho de volta? Você quer ter R$ 12.100,00 daqui a
  2 anos. Quanto precisa aplicar HOJE? Tirar 10% duas vezes não funciona. Próximo
  episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: um bloco "1,34" que é copiado e multiplicado por ele mesmo (×),
  enquanto uma versão errada (1,34 + 1,34) aparece riscada em vermelho ao lado.
- A régua da tentativa: 1,1¹, 1,1², 1,1³, 1,1⁴, 1,1⁵ acendendo um a um até passar da
  linha da meta 1,6.
- Um "radar" verde da regra do 72 apontando a ordem de grandeza nas questões de tempo.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Em todos os casos de "dobrar o tempo", o fator foi ELEVADO AO QUADRADO?
- As contas (1,4641; 1,61051; 1,7956; 1,95; 7,3; 1,4884; 6 anos) estão corretas?
- Os logaritmos foram usados só como valores dados, sem ensinar suas propriedades?
```

---

## Vídeo 4: Trazendo valores para hoje

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática Básica — Juros Compostos e Montante — Episódio 4 de 5:
Trazendo valores para hoje — quanto aplicar agora para ter tanto depois
RECORTE: use APENAS a seção 07 do material de apoio, mais a Questão 3 da seção 12.
"Voltar ao valor original dividindo pelo fator" foi ensinado na série de Porcentagem:
aqui, revisão rápida. Comparar pagamentos em datas diferentes volta nas séries de
Empréstimos, financiamentos e parcelamentos e de Comparação de propostas: aqui, só cite.
DURAÇÃO: 6 a 8 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece por uma família que quer trocar de carro daqui a
   2 anos e precisa saber quanto depositar hoje.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (valor presente, valor futuro, trazer para hoje, descontar pelo fator).
3. Analogias âncora, retomadas ao longo da aula:
   - "o filme ao contrário: ir para o futuro é multiplicar pelo fator; voltar para hoje é
     dividir pelo mesmo fator";
   - "tirar 10% não desfaz um aumento de 10%" (a mesma armadilha de Porcentagem);
   - "o número de hoje é sempre MENOR que o de amanhã".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: M = C · (1 + i)ᵗ
   (episódio 1) e "para voltar ao valor original, divida pelo fator" (série de
   Porcentagem: 1 ÷ 1,25 = 0,80).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; calcule primeiro o fator
   e só depois divida.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Para ter R$ 11.025,00 daqui a 2 anos, a 5% ao ano, quanto
  aplicar hoje? Quem tira 5% duas vezes chega a R$ 9.950,06 e fica devendo. A resposta
  certa é redonda: R$ 10.000,00."
- Promessa: "ao final, você vai trazer qualquer valor do futuro para hoje com uma
  divisão".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) a fórmula do valor presente: isolar o capital, C = M ÷ (1 + i)ᵗ;
  b) o exemplo do material: 1,05² = 1,1025; 11.025 ÷ 1,1025 = R$ 10.000,00;
  c) trazer para hoje é dividir pelo fator: tirar 5% duas vezes (11.025 · 0,95² =
     9.950,06) dá menos que o certo, porque retirar i% não desfaz um aumento de i%;
  d) a conferência: o valor de hoje é menor que o futuro; multiplicando de volta pelo
     fator, tem de dar o valor futuro;
  e) para que serve: comparar pagamentos em datas diferentes (só cite as séries de
     Empréstimos e de Comparação de propostas).
- Exercício "nós fazemos": peça "pause: quanto aplicar hoje, a juros compostos de 10% ao
  ano, para ter R$ 4.840,00 daqui a 2 anos?" (1,1² = 1,21; 4.840 ÷ 1,21 = R$ 4.000,00;
  conferência: 4.000 · 1,21 = 4.840 ✓).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Para o futuro, multiplique; para hoje, divida pelo mesmo fator."
  "Tirar 10% não desfaz um aumento de 10%."
  "Confira multiplicando de volta."
- Erros clássicos:
  • tirar i% por período em vez de dividir por (1 + i)ᵗ;
  • dividir pelo fator de juros simples (1 + i · t);
  • trazer só um período quando são vários;
  • multiplicar pelo fator em vez de dividir (projetar para o futuro).
- Questão no estilo ENEM: Questão 3 do material (R$ 12.100,00 em 2 anos a 10% a.a.):
  "eu faço", com a conferência no fim. 12.100 ÷ 1,21 = R$ 10.000,00 (A). B divide por
  1,20, o fator de juros simples; D desconta só um ano (12.100 ÷ 1,1); C retira 10% uma
  única vez; E multiplica pelo fator em vez de dividir. Antes de resolver, diga "pause o
  vídeo e tente".
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "no último episódio deste assunto, juntamos tudo,
  caçamos as pegadinhas e treinamos com questões no formato do ENEM."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: uma linha do tempo com "hoje" e "daqui a 2 anos"; uma seta para a
  direita com "× 1,21" e uma seta para a esquerda com "÷ 1,21"; o caminho errado
  "× 0,9 × 0,9" chegando a um ponto abaixo do certo, em vermelho.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Ficou claro que trazer para hoje é DIVIDIR pelo fator?
- As contas (10.000; 9.950,06; 4.000; 10.083,33 como erro da alternativa B) estão
  corretas?
- A conferência "multiplicar de volta" foi feita?
```

---

## Vídeo 5: Revisão (Juros compostos no ENEM)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula de REVISÃO para o YouTube sobre:

TEMA: Matemática Básica — Juros Compostos e Montante — Episódio 5 de 5:
Revisão geral, estratégia de prova, pegadinhas e treino para o ENEM
RECORTE: use as seções 01, 09, 10, 11 e 13 do material de apoio.
NÃO reutilize as Questões 1 a 9 da seção 12 (já resolvidas nos episódios anteriores).
Taxas equivalentes, logaritmos, PG e função exponencial têm séries próprias: aqui, só
cite as pontes.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que assistiu aos episódios 1 a 4, mas ainda é iniciante e pode ter esquecido
partes. Relembre cada conceito em uma frase simples antes de cobrá-lo.

REGRAS DE EXPLICAÇÃO
1. Cada conceito é relembrado com a mesma analogia âncora usada no seu episódio:
   a bola de neve; fatores, não porcentagens somadas; o expoente que conta as
   multiplicações; a escada de degraus iguais contra a escada de degraus crescentes; o
   cruzamento em t = 1; dobrar, dobrar, dobrar (×8); somar a décima parte; dobrar o tempo
   é elevar ao quadrado; a regra do 72 como radar; o filme ao contrário.
2. Prática de recuperação: antes de explicar, PERGUNTE e peça para o aluno pausar.
3. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
4. Uma ideia por cena. Frases curtas. Tom de conversa, falando com "você".

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Poupança, cartão de crédito, cheque especial, financiamento.
  Tudo funciona em juros compostos. E o ENEM sabe que você está sem calculadora: por isso
  ele entrega as potências e os logaritmos. Hoje você aprende a usá-los."
- O que a prova cobra (seção 01): montante com a potência dada; tempo por tentativa ou
  com logaritmos; trazer um valor futuro para hoje; comparar simples e compostos (números
  ou gráfico); encadear taxas diferentes multiplicando fatores.
- Onde aparece nas outras áreas (seção 10): Biologia (populações e bactérias com taxa
  fixa), Química (decaimento radioativo, fator 1/2 por meia-vida), Geografia (projeções
  de população e PIB), Álgebra e Funções (PG, exponencial e logaritmo, séries próprias),
  inflação (série de Taxas equivalentes e inflação).
- A estratégia de prova em 4 hábitos (seção 09): procurar as potências no enunciado;
  eliminar pelo simples (para prazos maiores que um período, a resposta composta é maior
  que a simples); estimar com a regra do 72; trabalhar com fatores até o fim.
- "Verdadeiro ou falso? Pause e responda": transforme em afirmações os 9 erros da
  seção 11. Para cada um: pausa → resposta → por que a pegadinha engana → a regra certa
  em uma frase.
- 5 questões INÉDITAS no estilo ENEM, criadas por você, com situações hipotéticas e
  5 alternativas cada:
  1) montante de uma aplicação com potência fácil de fazer à mão (ex.: 1,1² ou 1,05²),
     pedindo os juros, com o montante e os juros simples entre as alternativas;
  2) dívida com potência dada no enunciado e prazo que exige elevar ao quadrado ou
     combinar potências;
  3) tempo para dobrar ou triplicar com logaritmos fornecidos;
  4) valor presente: quanto aplicar hoje para ter um valor no futuro;
  5) comparação entre uma proposta a juros simples e outra a juros compostos, num prazo
     em que a resposta não seja óbvia pela regra geral.
  As alternativas erradas devem ser exatamente os erros clássicos (somar taxas, fórmula
  de juros simples, montante no lugar de juros, dobrar o fator em vez de elevar ao
  quadrado, tirar i% para trazer a hoje, dividir log 2 pela taxa, usar log 2 para
  triplicar). Leia, peça a pausa, escreva o fator de um período, resolva, elimine pelo
  simples e explique cada alternativa.
- Checklist de domínio (seção 13): leia os itens e diga "marque só o que você
  conseguiria explicar em voz alta para outra pessoa, sem consultar nada; o que não
  marcou, reveja o episódio correspondente" (indique qual: juros sobre juros, fórmula e
  taxas em sequência → episódio 1; simples × compostos, PG e duplicação → 2; potências,
  tentativa, logaritmos e regra do 72 → 3; valor presente → 4).
- Meta antes de considerar dominado: resolver 20 questões de juros compostos e acertar
  pelo menos 14 (70%), incluindo questões com logaritmos fornecidos e com comparação entre
  regimes.
- Encerramento e ponte: "o próximo assunto é Descontos, acréscimos, lucro e prejuízo: a
  matemática do balcão, com os mesmos fatores, e uma pergunta nova que derruba muita
  gente: porcentagem de quê, do custo ou da venda?"

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Use um cronômetro visual nas pausas; um selo "PEGADINHA" em amarelo nos erros; um
  ícone de contexto (cofrinho, cartão de crédito, gráfico, relógio) em cada questão
  inédita; os 4 ícones dos episódios (bola de neve, reta e curva se cruzando, bloco 1,34
  ao quadrado, linha do tempo com seta para trás) como índice visual da revisão.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Cada conceito foi relembrado antes de ser cobrado?
- As 5 questões inéditas têm uma única alternativa correta e contas corretas?
- Na questão de comparação entre regimes, a conta foi feita, e não só a regra geral?
```

---

## Cuidados ao revisar os roteiros

- **Vídeo 3, "dobrar o tempo":** 12 meses com 1,05⁶ ≈ 1,34 é **1,34² ≈ 1,80**, não 2 · 1,34 = 2,68 nem 1,68. A IA costuma escrever "o dobro do fator". O mesmo vale para o exercício: 1,22² = 1,4884.
- **Vídeo 3, logaritmo:** o denominador é **log(1 + i)** (log 1,2 ≈ 0,08), não a taxa (0,2). Com 0,30 ÷ 0,2 sairia 1,5 ano, que é absurdo. E para triplicar usa-se **log 3**, não log 2.
- **Vídeo 2, prazo menor que um período:** antes de t = 1, os juros **simples** rendem mais (meio período a 10%: 1,05 contra cerca de 1,0488). A IA tende a dizer que os compostos "sempre" rendem mais, que é o distrator A da Questão 4.
- **Vídeo 1, Questão 5:** 1,10 · 1,20 · 0,75 = **0,99** (perda de 1%), não ganho de 5% (soma) nem de 1% (sinal trocado).
