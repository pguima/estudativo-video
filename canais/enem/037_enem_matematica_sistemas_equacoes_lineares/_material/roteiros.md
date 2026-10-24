# Sistemas de Equações Lineares — série de videoaulas

Material de apoio: `01-matematica/22-sistemas-equacoes-lineares.html` · Incidência: Alta

## Sobreposições com outras séries

| Tema | Onde já apareceu / onde vai aparecer | O que fiz aqui |
|---|---|---|
| Resolver equação do 1º grau, montar a partir do texto, "releia a pergunta" | **Equações do 1º grau, vídeos 1 e 2** | Revisão relâmpago, com as mesmas analogias (balança, etiqueta do x). |
| Fretes com a mesma tarifa por km que nunca empatam (Q6 de Equações, 0x = −4) | **Equações do 1º grau, vídeo 1** | Retomada no vídeo 3 como "retas paralelas", sem repetir a questão. |
| Classificação SPD / SPI / SI e retas concorrentes, paralelas e coincidentes | Também na **série 34 (Determinantes e sistemas lineares)** | **Fica aqui:** classificação pela conta (0 = 2, 0 = 0), pelas razões entre coeficientes e pelo desenho das retas. Na série 34 entram o determinante (D ≠ 0), Cramer, discussão com dois parâmetros, sistema homogêneo e escalonamento 3 × 3 com classificação: aqui, **só citar**. |
| Ingressos de R$ 40 e R$ 20 | Q1 daqui (400 ingressos, R$ 11.200) × Q1 da série 34 (250 ingressos, R$ 7.400, por Cramer) | Mesmo contexto, números diferentes. Uso a Q1 daqui, resolvida por substituição. |
| Paralelas: Q6 daqui (x + 2y = 4 e 2x + 4y = 10) × Q5 da série 34 (3x − 6y = 9 e −x + 2y = 4) | Série 34 | Mesmo tipo, números diferentes. Uso a Q6 daqui, sem determinante. |
| Retas como funções, ponto de equilíbrio com gráfico | **Conceito de Função** (23) e **Função afim** (24) | Só a ponte no vídeo de revisão. |

## Plano: 5 vídeos

| Vídeo | Seções | Questões | Duração |
|---|---|---|---|
| **1. O que é um sistema, do texto ao sistema e o método da substituição** | 02, 03, 04 | Q1, Q5, Q9 | 10–12 min |
| **2. O método da adição e quando a pergunta já é a soma** | 05 | Q4, Q7 | 8–10 min |
| **3. As três posições de duas retas e classificar sem resolver** | 06, 07 | Q6, Q3 | 10–12 min |
| **4. Três incógnitas: escalonar ou somar tudo** | 08 | Q2, Q8 | 8–10 min |
| **5. Revisão** | 01, 09, 10, 11, 13 | 5 inéditas | 10–12 min |

---

## Vídeo 1: O que é um sistema, do texto ao sistema e o método da substituição

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Álgebra — Sistemas de Equações Lineares — Episódio 1 de 5:
O que é um sistema, do texto ao sistema e o método da substituição
RECORTE: use APENAS as seções 02, 03 e 04 do material de apoio, mais as Questões 1, 5 e
9 da seção 12. Resolver equação do 1º grau e montar equação a partir do texto já foram
ensinados na série de Equações e inequações do 1º grau: aqui, revisão rápida. O método
da adição fica para o episódio 2; as retas, para o episódio 3.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece num sítio com galinhas e coelhos, 10 cabeças e
   28 patas. Mostre que só "10 cabeças" permite muitas respostas ((1, 9), (2, 8),
   (6, 4)...) e que a segunda informação, as patas, escolhe uma só.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (sistema linear, incógnita, par ordenado, solução do sistema, equação das
   quantidades, equação dos valores, substituição).
3. Analogias âncora, retomadas ao longo da aula:
   - "duas incógnitas pedem duas pistas: cada informação do texto vira uma equação";
   - "o molde de quase toda questão: uma equação CONTA (cabeças, ingressos, veículos) e
     a outra SOMA VALORES (patas, reais, rodas)";
   - "substituir é trocar a peça pelo seu equivalente: m vale 30 − c, então onde estava
     m entra (30 − c), com parênteses e tudo";
   - "tudo de um tipo: finja que todos são motos e veja quantas rodas faltam".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: o roteiro de resolução
   e a etiqueta do x (série de Equações do 1º grau); a distributiva (série de Expressões
   Algébricas).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; escreva as etiquetas
   das incógnitas com unidade no canto da tela e confira o par nas DUAS equações.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "'Pedro tem o dobro das moedas de Júlia.' Metade das pessoas
  escreve 2P = J, e está errado. Teste com Júlia tendo 5: Pedro tem 10, e 10 = 2 · 5. A
  tradução certa é P = 2J."
- Promessa: "ao final, você vai transformar um texto em sistema e resolvê-lo pela
  substituição sem perder sinal".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) definição: equações que valem AO MESMO TEMPO; a solução é um par (x, y) que satisfaz
     todas;
  b) galinhas e coelhos: g + c = 10 e 2g + 4c = 28; o par (6, 4) confere nas duas
     (6 + 4 = 10 e 12 + 16 = 28);
  c) testar é permitido: um par que satisfaz só uma equação é o distrator típico;
  d) o molde quantidades × valores (tabela da seção 03): ingressos, carros e motos, prova
     com +5 e −2 (a + e = 20 e 5a − 2e = 51 → 13 acertos e 7 erros), cafés;
  e) frases de comparação: "o dobro de" (P = 2J) e "se Pedro der 6 a Júlia, ficam
     iguais" (P − 6 = J + 6: quem dá perde, quem recebe ganha);
  f) substituição: c + m = 30 e 4c + 2m = 100 → m = 30 − c → 4c + 2(30 − c) = 100 →
     2c = 40 → c = 20, m = 10; conferência: 80 + 20 = 100 rodas;
  g) o atalho "tudo de um tipo": 30 motos dariam 60 rodas; faltam 40; cada troca de moto
     por carro acrescenta 2; 40 ÷ 2 = 20 carros.
- Exercício "nós fazemos": peça "pause: num estacionamento há 25 veículos, entre carros e
  motos, com 70 rodas. Quantos são os carros?" (c + m = 25 e 4c + 2m = 70 → 10 carros e
  15 motos; pelo atalho: 50 rodas se fossem todas motos, faltam 20, 20 ÷ 2 = 10).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Uma equação por informação."
  "Uma equação conta, a outra soma valores."
  "Substituiu? Ponha parênteses."
- Erros clássicos:
  • "P tem o dobro de J" escrito 2P = J (teste com números pequenos);
  • 2(30 − c) = 60 − c (o coeficiente multiplica tudo: 60 − 2c);
  • "der 6 moedas" escrito P − 6 = J (quem recebe também muda);
  • responder a outra incógnita (inteiras ou meias? carros ou motos?).
- Questões no estilo ENEM, nesta ordem:
  • Questão 1 do material (400 ingressos, R$ 40,00 e R$ 20,00, total R$ 11.200,00):
    "eu faço". i = 400 − m → 16 000 − 40m + 20m = 11 200 → m = 240 meias (D);
    conferência: 6 400 + 4 800 = 11 200. Explique: B é o número de inteiras; C divide
    11 200 por 60, conta sem sentido no problema; E supõe todos pagando inteira
    (11 200 ÷ 40) e A é 400 − 280, consequência desse erro;
  • Questão 5 (Pedro e Júlia, troca de 6 moedas): "nós fazemos". P = 2J e P − 6 = J + 6
    → J = 12, P = 24 (D); depois da troca, 18 cada. Explique: B é o número de Júlia (e o
    que sai para Pedro com P − 6 = J); C é a quantidade depois da troca; E é o total; A é
    só o número de moedas transferidas;
  • Questão 9 (carro no km 20 a 60 km/h; ônibus no km 200 a 120 km/h, em sentido
    contrário): "você faz", com pausa. Diga que "a posição de cada um" é uma equação e
    que se encontrar é ter a MESMA posição no MESMO instante: 20 + 60t = 200 − 120t →
    180t = 180 → t = 1 h, no km 80 (B); conferência: 200 − 120 = 80. Explique: C é o
    ponto médio (só valeria com velocidades iguais); D troca as velocidades; A é o
    deslocamento do carro; E é a distância inicial.
  Em todas: leia o enunciado, escreva as etiquetas, uma equação por informação, resolva,
  confira nas duas equações e responda o que foi pedido.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "dois sanduíches e um suco custam R$ 31,00; um sanduíche
  e dois sucos, R$ 26,00. Quanto custa um de cada? Dá para responder em uma linha, sem
  descobrir o preço de nenhum. Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: o cercado com 10 cabeças; uma tabela de tentativas (1, 9), (2, 8)
  ... (6, 4) com o contador de patas, e só o (6, 4) acendendo verde em 28.
- Na substituição, a peça "m" saindo da segunda equação e a peça "(30 − c)" encaixando
  no lugar, com os parênteses piscando.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- As respostas são 240 meias (D), 24 moedas (D) e km 80 (B), todas conferidas nas duas
  equações?
- A tradução "o dobro de" foi testada com números?
- Na substituição, o 2(30 − c) virou 60 − 2c na tela?
```

---

## Vídeo 2: O método da adição e quando a pergunta já é a soma

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Álgebra — Sistemas de Equações Lineares — Episódio 2 de 5:
O método da adição e quando a pergunta já é a soma
RECORTE: use APENAS a seção 05 do material de apoio, mais as Questões 4 e 7 da seção 12.
Montar o sistema e a substituição são do episódio 1 (revisão rápida).
DURAÇÃO: 8 a 10 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece com duas notas fiscais de lanchonete lado a lado
   (2 sanduíches + 1 suco = R$ 31,00; 1 sanduíche + 2 sucos = R$ 26,00) e junte as duas
   compras numa só sacola: 3 sanduíches + 3 sucos = R$ 57,00.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (método da adição, coeficientes opostos, eliminar uma incógnita, multiplicar
   uma equação).
3. Analogias âncora, retomadas ao longo da aula:
   - "somar equações é juntar duas notas fiscais: soma-se o que foi comprado e soma-se o
     que foi pago";
   - "coeficientes opostos se anulam como +2 e −2 numa balança: a incógnita some";
   - "multiplicar a equação é comprar o mesmo pedido 3 vezes: TUDO triplica, inclusive o
     valor pago";
   - "antes de resolver, olhe o que foi pedido: às vezes a sacola já é a resposta".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: o molde quantidades ×
   valores e a conferência nas duas equações (episódio 1).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; alinhe as equações uma
   embaixo da outra, com x embaixo de x e y embaixo de y, e mostre a multiplicação
   chegando também ao lado direito.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "2 sanduíches e 1 suco: R$ 31,00. 1 sanduíche e 2 sucos:
  R$ 26,00. Quanto custam um sanduíche e um suco juntos? R$ 19,00, e você vai descobrir
  isso sem calcular o preço de nenhum dos dois."
- Promessa: "ao final, você vai resolver sistemas pela adição e reconhecer quando a
  pergunta sai somando as equações".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) coeficientes já opostos: 3x + 2y = 16 e 5x − 2y = 16 → 8x = 32 → x = 4 → y = 2;
  b) multiplicando antes: 2x + 3y = 12 (× 3) e 3x + 2y = 13 (× 2) → 6x + 9y = 36 e
     6x + 4y = 26 → 5y = 10 → y = 2 → x = 3;
  c) multiplique a equação inteira: 2x + 3y = 12 vira 6x + 9y = 36, e não "= 12";
  d) às vezes a pergunta é a soma: no mesmo sistema, somando sem multiplicar,
     5x + 5y = 25 → x + y = 5;
  e) como escolher o método: coeficiente 1 → substituição; coeficientes opostos ou
     fáceis de igualar → adição; pergunta sobre x + y → some antes de tudo.
- Exercício "nós fazemos": peça "pause: resolva x + 2y = 11 e 3x − 2y = 1"
  (somando: 4x = 12 → x = 3 → 2y = 8 → y = 4; conferência: 9 − 8 = 1).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Some as equações para uma incógnita sumir."
  "Multiplicou? Multiplique a equação inteira."
  "Antes de resolver, olhe o que foi pedido."
- Erros clássicos:
  • multiplicar só o lado esquerdo;
  • resolver tudo quando a pergunta é x + y;
  • somar quando deveria subtrair (os coeficientes iguais, e não opostos, pedem
    subtração).
- Questões no estilo ENEM, nesta ordem:
  • Questão 4 do material (cafés de R$ 30,00 e R$ 45,00, 60 kg a R$ 40,00): "eu faço".
    a + b = 60 e 30a + 45b = 2 400. Pela adição: multiplique a primeira por 30
    (30a + 30b = 1 800) e subtraia: 15b = 600 → b = 40 kg, a = 20 kg (B). Mostre também
    a substituição do material (15a = 300) para comparar os dois caminhos. Conferência:
    600 + 1 800 = 2 400. Explique: D é o café caro; C supõe partes iguais (preço médio
    R$ 37,50); A usa 40 − 30 como quantidade; E é 60 − 10;
  • Questão 7 (sanduíches e sucos): "você faz", com pausa. Somando: 3S + 3J = 57 →
    S + J = 19 (C). Se quiser os preços: subtraindo, S − J = 5 → S = 12, J = 7. Explique:
    A é o suco, B é o sanduíche, E é a soma das duas compras (três de cada), D divide 57
    por 2.
  Em todas: leia o enunciado, alinhe as equações, escolha o método, resolva, confira e
  responda o que foi pedido.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "e quando a conta termina em 0 = 2? Você errou alguma
  coisa ou o sistema está te dizendo algo? Próximo episódio: as três posições de duas
  retas."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: duas notas fiscais deslizando e se juntando numa só sacola, com os
  itens e os valores somando (3 sanduíches, 3 sucos, R$ 57,00); depois a sacola se
  dividindo por 3.
- Na multiplicação, um "× 3" envolvendo a equação inteira como um laço, até o lado
  direito.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- A Questão 4 deu 20 kg (B) e a Questão 7 deu R$ 19,00 (C)?
- Toda multiplicação de equação chegou ao lado direito?
- O exemplo 2x + 3y = 12 e 3x + 2y = 13 deu x = 3, y = 2 e x + y = 5?
```

---

## Vídeo 3: As três posições de duas retas e classificar sem resolver

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Álgebra — Sistemas de Equações Lineares — Episódio 3 de 5:
Concorrentes, paralelas ou coincidentes: classificar sem resolver
RECORTE: use APENAS as seções 06 e 07 do material de apoio, mais as Questões 6 e 3 da
seção 12. O quadro "O determinante, para quem já viu" da seção 07 deve ser só CITADO em
uma frase ("isso tem série própria: Determinantes e sistemas lineares"); não calcule
determinante nem use a regra de Cramer. O caso dos fretes que nunca empatam já apareceu
na série de Equações do 1º grau: retome como revisão.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece com dois trilhos de trem (paralelos, nunca se
   encontram), um cruzamento de duas ruas (um único ponto em comum) e uma rua desenhada
   duas vezes no mapa, uma sobre a outra (todos os pontos em comum).
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (retas concorrentes, paralelas, coincidentes, sistema possível e determinado
   (SPD), sistema impossível (SI), sistema possível e indeterminado (SPI), razão entre
   coeficientes, parâmetro).
3. Analogias âncora, retomadas ao longo da aula:
   - "cada equação é uma estrada de soluções; a solução do sistema é o cruzamento";
   - "0 = 2 é a conta dizendo 'esses trilhos nunca se encontram'; 0 = 0 é a conta
     dizendo 'é a mesma estrada desenhada duas vezes'";
   - "múltipla só do lado esquerdo: paralelas; múltipla inteira: a mesma reta".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: o método da adição
   (episódio 2) e os fretes 40 + 3x e 3x + 36 que nunca empatam (série de Equações do
   1º grau: 0x = −4).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; escreva as três razões
   a₁/a₂, b₁/b₂ e c₁/c₂ lado a lado na tela antes de concluir.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Você resolve um sistema, as letras somem e sobra 0 = 2. A
  maioria apaga tudo achando que errou a conta. Não errou: a conta acabou de dizer que
  não existe resposta."
- Promessa: "ao final, você vai dizer se um sistema tem uma, nenhuma ou infinitas
  soluções, muitas vezes sem resolver nada".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) as três posições (tabela da seção 06): x + y = 5 e x − y = −1 → concorrentes, SPD,
     (2, 3); x + 2y = 4 e 2x + 4y = 10 → paralelas, SI, chega-se a 0 = 2;
     x + 2y = 4 e 2x + 4y = 8 → coincidentes, SPI, chega-se a 0 = 0;
  b) no contexto de preços: mesma tarifa por unidade e taxas diferentes = retas
     paralelas (os fretes da série de Equações do 1º grau);
  c) classificar sem resolver pelas razões: a₁/a₂ ≠ b₁/b₂ → SPD; a₁/a₂ = b₁/b₂ ≠ c₁/c₂ →
     SI; as três iguais → SPI;
  d) em palavras: múltipla só do lado esquerdo → paralelas; múltipla inteira → mesma reta;
  e) parâmetro: 2x + 3y = 5 e 4x + ky = 10 → 2/4 = 3/k = 5/10 → k = 6 para infinitas
     soluções; com qualquer outro k, uma única solução;
  f) o determinante, só citado em uma frase, com a série de Determinantes.
- Exercício "nós fazemos": peça "pause: classifique x − 3y = 2 e −2x + 6y = −4; e se o
  lado direito da segunda fosse 5?" (razões 1/(−2) = (−3)/6 = 2/(−4) = −1/2: SPI,
  coincidentes; com 5, a razão 2/5 ≠ −1/2: SI, paralelas).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Concorrentes: uma solução. Paralelas: nenhuma. Coincidentes: infinitas."
  "0 = 2 é impossível; 0 = 0 é infinitas."
  "Múltipla só à esquerda, paralelas; múltipla inteira, a mesma reta."
- Erros clássicos:
  • 0 = 2 significa "errei a conta" (é sistema impossível);
  • 0 = 0 significa "solução zero" (são infinitas soluções);
  • olhar só os coeficientes e esquecer o lado direito ao classificar.
- Questões no estilo ENEM, nesta ordem:
  • Questão 6 do material (r: x + 2y = 4; s: 2x + 4y = 10): "eu faço". O lado esquerdo
    de s é o dobro do de r, mas 2 · 4 = 8 ≠ 10; razões 1/2 = 2/4 ≠ 4/10: paralelas
    distintas, sem solução (E). Pela adição: 2r − s dá 0 = −2, ou s − 2r dá 0 = 2, um
    absurdo. Explique: B valeria se o lado direito fosse 8; A e C ignoram a mesma
    inclinação; D falha no teste direto (0 + 0 ≠ 4);
  • Questão 3 (2x + 3y = 5 e 4x + ky = 10 com "infinitas soluções"): "você faz", com
    pausa. Fator 2 (4 = 2 · 2 e 10 = 2 · 5) → k = 6 (A). Explique: E descreve os casos
    de solução única; B troca o sinal; C copia o 3 sem multiplicar; D multiplica por 4;
    com −6, 3 ou 12 as retas são concorrentes.
  Em todas: leia o enunciado, escreva as razões, decida e explique as alternativas
  erradas.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "Ana e Beto pesam 125 kg juntos; Beto e Caio, 145 kg;
  Ana e Caio, 140 kg. Quanto pesa o Beto? Três incógnitas, e um atalho que resolve em
  duas linhas. Próximo episódio."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: um plano cartesiano com as três situações lado a lado: duas retas
  se cruzando em (2, 3), dois trilhos paralelos (selo "0 = 2") e duas retas que se
  sobrepõem e piscam como uma só (selo "0 = 0").
- As três razões aparecendo em três "caixinhas" lado a lado, com sinais de = ou ≠
  surgindo entre elas.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- A Questão 6 deu "paralelas distintas, sem solução" (E) e a Questão 3 deu k = 6 (A)?
- O determinante foi só citado, sem cálculo nem regra de Cramer?
- Ficou claro que 0 = 2 é SI e 0 = 0 é SPI?
```

---

## Vídeo 4: Três incógnitas: escalonar ou somar tudo

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula para o YouTube sobre:

TEMA: Matemática — Álgebra — Sistemas de Equações Lineares — Episódio 4 de 5:
Três incógnitas: escalonar ou somar tudo
RECORTE: use APENAS a seção 08 do material de apoio, mais as Questões 2 e 8 da
seção 12. Substituição e adição são dos episódios 1 e 2 (revisão rápida). Escalonamento
geral de sistemas 3 × 3, classificação 3 × 3 e regra de Sarrus ficam para a série de
Determinantes e sistemas lineares: aqui, só o sistema já escalonado e o atalho da soma.
DURAÇÃO: 8 a 10 minutos

PÚBLICO
Alguém que NUNCA estudou o assunto, terminou o ensino médio há anos ou tem base fraca
em matemática. Assuma que a pessoa não sabe nenhum termo técnico. Se ela se perder
em qualquer momento, a aula falhou.

REGRAS DE EXPLICAÇÃO
1. Concreto antes do abstrato: comece com três amigos subindo numa balança de farmácia
   em duplas e anotando os três resultados.
2. Todo termo técnico ganha uma definição em uma frase simples na primeira vez em que
   aparece (sistema 3 × 3, equações independentes, escalonamento, sistema escalonado,
   substituição de baixo para cima).
3. Analogias âncora, retomadas ao longo da aula:
   - "o sistema escalonado é uma escada: comece pelo degrau de baixo (uma incógnita só) e
     suba substituindo";
   - "nas pesagens em dupla, cada pessoa subiu na balança duas vezes: some tudo e divida
     por 2";
   - "cada um é o total menos a dupla em que ele não está".
4. Revise os pré-requisitos em até 30 segundos antes de usá-los: substituição (episódio
   1) e subtrair uma equação da outra (episódio 2).
5. Abra cada bloco com uma pergunta que gere curiosidade e só depois responda.
6. Uma ideia por cena. Frases curtas. Nunca dois conceitos novos na mesma cena.
7. Contas sempre passo a passo, narrando o PORQUÊ de cada passo; ao somar as três
   equações, conte em voz alta quantas vezes cada incógnita aparece.
8. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
9. Tom de conversa, falando com "você". Sem jargão acadêmico e sem pressa.

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Ana e Beto, 125 kg. Beto e Caio, 145 kg. Ana e Caio, 140 kg.
  Muita gente divide 125 por 2 e diz que Beto pesa 62,5 kg. Ele pesa 65."
- Promessa: "ao final, você vai resolver sistemas com três incógnitas pela escada e pelo
  atalho da soma".
- Pré-requisitos relâmpago.
- Blocos (um conceito por bloco):
  a) três incógnitas pedem três equações independentes;
  b) sistema escalonado: x + y + z = 6, y + z = 5, z = 3 → z = 3, y = 2, x = 1, de baixo
     para cima;
  c) o atalho da soma: A + B = 13, B + C = 15, A + C = 14 → 2(A + B + C) = 42 →
     A + B + C = 21 → C = 8, A = 6, B = 7;
  d) a regra: cada incógnita é o total menos a equação que não a contém;
  e) quando usar: cada incógnita aparece o mesmo número de vezes (pesagens em dupla,
     combos, distâncias entre três cidades); o escalonamento geral fica para a série de
     Determinantes.
- Exercício "nós fazemos": peça "pause: A + B = 9, B + C = 11 e A + C = 10. Quanto vale
  cada um?" (soma 30 → total 15 → A = 4, B = 5, C = 6; conferência: 4 + 5 = 9).
- Mini-recapitulação no meio do vídeo (3 frases-chave):
  "Sistema escalonado: resolva de baixo para cima."
  "Em duplas, cada um aparece duas vezes: some e divida por 2."
  "Cada um é o total menos a dupla em que ele não está."
- Erros clássicos:
  • somar as três pesagens e esquecer de dividir por 2;
  • dividir uma pesagem por 2, como se os dois da dupla pesassem o mesmo;
  • responder um resultado intermediário (como m + 2d) no lugar da incógnita pedida.
- Questões no estilo ENEM, nesta ordem:
  • Questão 2 do material (pesagens de Ana, Beto e Caio): "eu faço". 125 + 145 + 140 =
    410 → total 205 → B = 205 − 140 = 65 kg (C); Ana 60 e Caio 80; conferência:
    60 + 65 = 125. Explique: A é Ana e E é Caio; B e D dividem uma pesagem por 2
    (125 ÷ 2 e 145 ÷ 2);
  • Questão 8 (20 questões de 1, 2 e 3 pontos, 37 pontos, médias = difíceis + 2): "você
    faz", com pausa. f + m + d = 20, f + 2m + 3d = 37, m = d + 2; subtraindo a primeira
    da segunda, m + 2d = 17; com m = d + 2, 3d = 15 → d = 5, m = 7 (B), f = 8;
    conferência: 8 + 7 + 5 = 20 e 8 + 14 + 15 = 37. Explique: A é o número de difíceis;
    C, o de fáceis; D, os pontos das difíceis (5 · 3); E é o intermediário m + 2d.
  Em todas: leia o enunciado, escreva as etiquetas, uma equação por informação, resolva,
  confira e responda o que foi pedido.
- Recapitulação final com as MESMAS 3 frases-chave do meio.
- Ponte para o próximo episódio: "no último episódio deste assunto, juntamos tudo,
  caçamos as pegadinhas e vemos sistemas na Física, na Química e na Geometria."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Animação principal: três bonequinhos subindo na balança em duplas; quando as três
  pesagens se somam, cada bonequinho aparece duas vezes na pilha, e a pilha se divide ao
  meio.
- A escada do sistema escalonado, com z = 3 no degrau de baixo e as setas subindo.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- A Questão 2 deu 65 kg (C) e a Questão 8 deu 7 questões médias (B)?
- A soma das três pesagens foi dividida por 2, e não por 3?
- O escalonamento geral 3 × 3 ficou só citado, como assunto da série de Determinantes?
```

---

## Vídeo 5: Revisão (Sistemas lineares no ENEM)

```
Você é um professor de cursinho popular, famoso por fazer qualquer pessoa entender
qualquer assunto. Crie uma videoaula de REVISÃO para o YouTube sobre:

TEMA: Matemática — Álgebra — Sistemas de Equações Lineares — Episódio 5 de 5:
Revisão geral, estratégia de prova, pegadinhas e treino para o ENEM
RECORTE: use as seções 01, 09, 10, 11 e 13 do material de apoio.
NÃO reutilize as Questões 1 a 9 da seção 12 (já trabalhadas nos episódios anteriores).
Determinante, Cramer e discussão de sistemas com parâmetros são da série de
Determinantes e sistemas lineares; função afim e retas como funções, das próximas séries:
aqui, só cite a ponte.
DURAÇÃO: 10 a 12 minutos

PÚBLICO
Alguém que assistiu aos episódios 1 a 4, mas ainda é iniciante e pode ter esquecido
partes. Relembre cada conceito em uma frase simples antes de cobrá-lo.

REGRAS DE EXPLICAÇÃO
1. Cada conceito é relembrado com a mesma analogia âncora usada no seu episódio:
   duas incógnitas pedem duas pistas; uma equação conta e a outra soma valores; trocar
   a peça pelo equivalente, com parênteses; tudo de um tipo; juntar as notas fiscais;
   multiplicar o pedido inteiro; a estrada de soluções e o cruzamento; 0 = 2 são trilhos
   que nunca se encontram; a escada do sistema escalonado; cada um sobe duas vezes na
   balança.
2. Prática de recuperação: antes de explicar, PERGUNTE e peça para o aluno pausar.
3. Para cada erro comum: mostre o erro, explique por que ele PARECE certo e então corrija.
4. Uma ideia por cena. Frases curtas. Tom de conversa, falando com "você".

ESTRUTURA OBRIGATÓRIA
- 0:00 Gancho (até 30s): "Ingressos inteiros e meias, carros e motos, café caro e café
  barato: o ENEM adora duas condições valendo ao mesmo tempo. A conta é curta; o que
  decide a questão é a tradução."
- O que a prova cobra (seção 01): quantidade e valor, cabeças e patas, misturas,
  combinações de compras e interpretação gráfica; o hábito que mais rende: nomear as
  incógnitas com unidade e olhar se a pergunta é uma combinação como x + y.
- Onde aparece nas outras áreas (seção 10): Física (encontro de móveis: s_A = 20 + 80t e
  s_B = 200 − 100t se igualam em t = 1 h, no km 100), Química (massa de soluto antes =
  massa de soluto depois, a "equação dos valores"), Geometria analítica (o ponto comum
  de duas retas) e Função afim (ponto de equilíbrio entre dois planos: próximas séries).
- A estratégia de prova em 4 hábitos (seção 09): uma equação por informação; escolher o
  método pelo formato; conferir na equação que não foi usada por último; responder a
  pergunta, não a incógnita.
- "Verdadeiro ou falso? Pause e responda": transforme em afirmações os 9 erros da
  seção 11 ("P tem o dobro de J" → 2P = J; 2(30 − c) = 60 − c; multiplicar só o lado
  esquerdo; responder a outra incógnita; "der 6 moedas" → P − 6 = J; resolver tudo
  quando pedem x + y; 0 = 2 significa "errei a conta"; 0 = 0 significa "solução zero";
  somar as três duplas e não dividir por 2). Para cada um: pausa → resposta → por que a
  pegadinha engana → a regra certa em uma frase.
- 5 questões INÉDITAS no estilo ENEM, criadas por você, com situações hipotéticas e
  5 alternativas cada:
  1) quantidade e valor: cédulas ou produtos de dois preços, com total de itens e total
     em reais;
  2) frase de comparação: "o triplo de" ou "se um der k ao outro";
  3) combo: a pergunta é a soma de um item de cada (somar as equações);
  4) classificação: duas retas dadas por equações, concorrentes, paralelas ou
     coincidentes, ou o valor de um coeficiente para infinitas soluções;
  5) três incógnitas simétricas (pesagens, combos ou distâncias dois a dois).
  As alternativas erradas devem ser exatamente os erros clássicos (tradução invertida,
  a outra incógnita, a soma das duas compras, 0 = 2 tratado como erro de conta, total sem
  dividir por 2). Leia, peça a pausa, escreva as etiquetas, resolva, confira nas duas
  equações e explique cada alternativa.
- Checklist de domínio (seção 13): leia os itens e diga "marque só o que você
  conseguiria explicar em voz alta para outra pessoa, sem consultar nada; o que não
  marcou, reveja o episódio correspondente" (solução, montagem, tradução, substituição,
  tudo de um tipo, encontro → episódio 1; adição e x + y → episódio 2; SPD/SI/SPI, razões,
  0 = 2 e 0 = 0 → episódio 3; 3 × 3 escalonado e simétrico → episódio 4).
- Meta antes de considerar dominado: resolver 30 questões e acertar pelo menos 21 (70%),
  com pelo menos quinze de montagem a partir de texto (ingressos, misturas, combos).
- Encerramento e ponte: "o próximo assunto é Conceito de função: domínio, contradomínio
  e imagem, que abre o bloco de Funções e transforma as retas deste assunto em funções:
  uma coisa que determina a outra."

DIREÇÃO VISUAL
- O texto na tela é curto (palavras-chave), nunca a cópia da narração.
- Use um cronômetro visual nas pausas; um selo "PEGADINHA" em amarelo nos erros; um
  ícone de etiqueta com as duas incógnitas em cada questão inédita; os 4 ícones dos
  episódios (cercado de galinhas e coelhos, duas notas fiscais, trilhos paralelos,
  balança com duplas) como índice visual da revisão.
- Cores com função: azul = definição, roxo = regra/fórmula, amarelo = armadilha,
  verde = atalho/dica, vermelho = erro.

ANTES DE ENTREGAR, VERIFIQUE
- Cada conceito foi relembrado antes de ser cobrado?
- As 5 questões inéditas têm uma única alternativa correta e contas corretas,
  conferidas nas equações originais?
- Determinante e Cramer ficaram só citados?
```

---

## Cuidados ao revisar os roteiros

- **Tradução invertida:** "Pedro tem o dobro de Júlia" é **P = 2J**. A IA de vídeo às vezes escreve 2P = J na tela enquanto a narração diz o certo. Confira a tela do gancho do vídeo 1 e a Questão 5.
- **Substituição com parênteses:** 4c + 2(30 − c) = 100 → **4c + 60 − 2c** = 100 → c = 20. Se aparecer 60 − c, o resultado vira c = 13,3 e a aula se contradiz.
- **Questão 6 (paralelas):** 2 · (x + 2y = 4) dá 2x + 4y = 8. Comparando com 2x + 4y = 10, sai 0 = 2 (ou 0 = −2, conforme a ordem da subtração). As duas formas indicam SI. A IA às vezes conclui "coincidentes" porque os coeficientes da esquerda são proporcionais.
- **Fronteira com a série 34:** se a IA calcular D = a₁b₂ − a₂b₁ ou usar Cramer nos vídeos 3 e 4, corte. Na Questão 2, a soma das pesagens (410) se divide por **2** (total 205), e não por 3.
