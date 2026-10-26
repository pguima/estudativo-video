# Roteiro — Potenciação e Radiciação, Episódio 6 de 7: Dois truques que a prova cobra — racionalização e expoente
# fracionário (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/04-potenciacao-radiciacao.html — seções 09 e 10 (+ Questões 6 e 7 da seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   PORÃO: racionalizar é tirar a raiz do "porão" (o denominador) multiplicando por 1 DISFARÇADO (√2/√2 = 1): o valor não
#     muda, só a aparência.
#   PAR PERFEITO: o conjugado é o mesmo binômio com o sinal do meio trocado; juntos viram diferença de quadrados, e o
#     quadrado desmancha a raiz.
#   TRADUTOR: expoente fracionário traduz raiz ↔ potência: quem está EMBAIXO na fração vira a casinha da raiz (o índice);
#     quem está EM CIMA vira o expoente de dentro.
# Termos definidos na hora: denominador, racionalizar, binômio, conjugado, diferença de quadrados, expoente fracionário,
#   índice, MMC, ordem crescente.
# Exemplos NOSSOS (o material não traz): 4/√2 = 2√2 (atalho do caso 1) · (5 − 2)(5 + 2) = 21 = 25 − 4 (teste da diferença
#   de quadrados) · (√5 − √2)² = 7 − 2√10 (erro do mesmo sinal) · √3 × ∛4 = ⁶√27 × ⁶√16 (erro de olhar o radicando) ·
#   a dedução √2 = 2^(1/2) por (2^(1/2))² = 2¹.
# Nós fazemos: 3/√3 = 3√3/3 = √3 · 27^(1/3) = ∛27 = 3.
# QUESTÃO 6 do material (texto idêntico na tela): 6/(√5 − √2) → ×(√5 + √2)/(√5 + √2) → 6(√5 + √2)/3 = 2√5 + 2√2 → A.
#   O material não explica as erradas. Explicações NOSSAS: D (2√3) = subtraiu dentro da raiz (√5 − √2 virou √3) e
#   racionalizou 6/√3; C ((√5 + √2)/3) = perdeu o 6 do numerador; E (√5 + √2) = só trocou o sinal e subiu o binômio,
#   sem fazer as contas; B (6√5 − 6√2) = sinal do meio errado (não usou o conjugado) e não dividiu pelo 3.
# QUESTÃO 7 do material (texto idêntico na tela): √2 = ⁶√8, ∛3 = ⁶√9, ⁶√10 → 8 < 9 < 10 → A.
#   Contraintuitivo (material): ⁶√10 tem o maior índice e ainda assim é o maior.
#   Explicações NOSSAS: B = ordenou pelo índice ("índice maior dá número menor"); E = só jogou o ⁶√10, de maior índice,
#   para o começo; D = errou a conversão do ∛3 (elevou o 3 ao cubo: ⁶√27, em vez de ao quadrado: ⁶√9);
#   C = inverteu √2 e ∛3, que são muito próximos (1,41 e 1,44), no chute.
# Frases-chave (meio e fim, idênticas):
#   1. Racionalizar é multiplicar por 1 disfarçado.
#   2. Binômio com raiz? Multiplique pelo conjugado.
#   3. Embaixo vira índice; em cima vira expoente.
# Atalhos (verde): "raiz sozinha embaixo: multiplique em cima e embaixo por ela" · "conjugado: o de baixo vira
#   primeiro² − segundo², direto" · "faça a raiz primeiro, os números ficam pequenos" · "mesmo índice: compare só os
#   radicandos" · "o índice multiplicou por k? eleve o radicando a k".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "1/√2 ou √2/2? Racionalização e expoente fracionário do zero | Potenciação Ep. 6"
# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de matemática: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa nas armadilhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, fale devagar e com clareza, número por número. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Sua resposta deu *um sobre raiz de dois.* [p=0.4] {b}Nas alternativas, [p=0.2] está *raiz de dois sobre dois.* "
        "[p=0.4] {c}Você errou? [p=0.4] {d}Não! [p=0.2] É o *mesmo número.* [p=0.5] {e}E outra: [p=0.2] qual é maior, "
        "[p=0.2] raiz de dois [p=0.2] ou raiz cúbica de três? [p=0.5] {f}Hoje você resolve *as duas coisas.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai *tirar a raiz do denominador,* [p=0.3] {b}e vai comparar e multiplicar "
        "raízes de *índices diferentes.* [p=0.3] {c}São dois truques, [p=0.2] e a prova cobra os dois."),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}Do episódio quatro: [p=0.2] raiz de sete, ao quadrado, é *sete.* [p=0.2] O quadrado desfaz a raiz. [p=0.4] {b}Do episódio dois: [p=0.2] potências de mesma base multiplicadas, [p=0.2] *soma os expoentes.* [p=0.4] {c}E o *MMC,* [p=0.2] da série de divisibilidade: [p=0.2] o menor número que está na tabuada dos dois. [p=0.2] O MMC de dois e três é *seis.*"),

    # ================= BLOCO A: POR QUE A PROVA COBRA =================
    dict(id="04", block="porao", text=
        "{t}Por que a prova se importa com raiz *embaixo?* [p=0.4] {a}O número de baixo da fração [p=0.2] se chama *denominador.* [p=0.3] {b}Pense nele como o *porão* da fração. [p=0.4] {c}As alternativas do ENEM quase sempre vêm com o porão *sem raiz.* [p=0.4] {d}E um sobre raiz de dois [p=0.2] vale o mesmo que raiz de dois sobre dois: [p=0.2] *zero vírgula setenta e um.* [p=0.4] {e}Tirar a raiz do porão sem mudar o valor [p=0.2] é *racionalizar.*"),
    dict(id="05", block="disfarce", text=
        "{t}E como mexer na fração sem mudar o valor? [p=0.4] {a}Multiplicando por *um:* [p=0.2] cinco vezes um continua cinco. [p=0.4] {b}Só que o um pode vir *disfarçado:* [p=0.2] três sobre três é um. [p=0.3] {c}Raiz de dois sobre raiz de dois [p=0.2] *também é um.* [p=0.4] {d}É o *um disfarçado:* [p=0.2] muda a aparência, [p=0.2] não o valor."),

    # ================= BLOCO B: CASO 1, UMA RAIZ SOZINHA =================
    dict(id="06", block="caso1", text=
        "{t}Vamos limpar o porão de *um sobre raiz de dois.* [p=0.4] {a}Multiplique pelo um disfarçado: [p=0.2] raiz de dois sobre raiz de dois. [p=0.4] {b}Em cima: [p=0.2] *raiz de dois.* [p=0.4] {c}Embaixo: [p=0.2] raiz de dois vezes raiz de dois, [p=0.2] que é raiz de dois *ao quadrado.* [p=0.2] O quadrado desfaz a raiz: [p=0.2] *dois.* [p=0.4] {d}Raiz de dois sobre dois. [p=0.3] Mesmo valor, [p=0.2] porão limpo."),
    dict(id="07", block="caso1_atalho", text=
        "{t}Atalho: [p=0.2] {a}*raiz sozinha embaixo?* [p=0.2] Multiplique em cima e embaixo [p=0.2] por *ela mesma.* "
        "[p=0.4] {b}Quatro sobre raiz de dois [p=0.2] vira quatro raiz de dois sobre dois, [p=0.3] {c}e quatro dividido "
        "por dois é dois: [p=0.2] *dois raiz de dois.* [p=0.3] {d}Depois, [p=0.2] sempre olhe se dá para simplificar."),

    # ================= BLOCO C: CASO 2, BINÔMIO COM RAIZ =================
    dict(id="08", block="caso2", text=
        "{t}E se o porão tiver *duas* raízes? [p=0.3] {a}Seis sobre raiz de cinco *menos* raiz de dois. [p=0.4] {b}Tente o "
        "truque de antes: [p=0.2] vezes raiz de cinco. [p=0.4] {c}Raiz de cinco vezes raiz de cinco dá cinco, [p=0.2] mas "
        "raiz de dois vezes raiz de cinco [p=0.2] dá *raiz de dez.* [p=0.4] {d}A raiz continua lá! [p=0.3] {e}Precisamos de "
        "outro disfarce."),
    dict(id="09", block="conjugado", text=
        "{t}Primeiro, dois nomes. [p=0.3] {a}Uma conta com *dois termos* ligados por mais ou menos [p=0.2] é um *binômio,* [p=0.2] como raiz de cinco menos raiz de dois. [p=0.4] {b}O *conjugado* dele [p=0.2] é o mesmo binômio [p=0.2] com o *sinal do meio trocado:* [p=0.3] {c}raiz de cinco *mais* raiz de dois. [p=0.4] {d}É o *par perfeito:* [p=0.2] quando os dois se encaixam, [p=0.2] a raiz some."),
    dict(id="10", block="diferenca", text=
        "{t}Por que a raiz some? [p=0.3] {a}Multiplique *xis menos ípsilon* [p=0.2] por *xis mais ípsilon,* [p=0.2] termo "
        "por termo. [p=0.4] {b}Xis vezes xis: [p=0.2] xis ao quadrado. [p=0.3] {c}Os termos do meio, [p=0.2] *mais xis "
        "ípsilon* e *menos xis ípsilon,* [p=0.2] se cancelam. [p=0.4] {d}E sobra *menos ípsilon ao quadrado.* [p=0.4] "
        "{e}Isso é a *diferença de quadrados:* [p=0.2] um quadrado menos outro quadrado."),
    dict(id="11", block="diferenca", text=
        "{t}Teste com números pequenos. [p=0.3] {a}Cinco menos dois, [p=0.2] vezes cinco mais dois: [p=0.2] três vezes sete, [p=0.2] *vinte e um.* [p=0.4] {b}Cinco ao quadrado menos dois ao quadrado: [p=0.2] vinte e cinco menos quatro, [p=0.2] *vinte e um.* [p=0.3] Confere!"),
    dict(id="12", block="encaixe", text=
        "{t}Agora encaixe o par perfeito. [p=0.3] {a}Raiz de cinco menos raiz de dois, [p=0.2] vezes raiz de cinco mais raiz de dois. [p=0.4] {b}Diferença de quadrados: [p=0.2] raiz de cinco ao quadrado, [p=0.2] menos raiz de dois ao quadrado. [p=0.4] {c}O quadrado *desmancha* a raiz: [p=0.2] cinco menos dois, [p=0.2] *três.* [p=0.3] {d}Sem raiz! [p=0.4] {e}Atalho: [p=0.2] com o conjugado, [p=0.2] o porão vira direto [p=0.2] *o primeiro ao quadrado menos o segundo ao quadrado.*"),

    # ================= BLOCO D: O TRADUTOR =================
    dict(id="13", block="tradutor", text=
        "{t}Agora, o segundo truque. [p=0.3] {a}Raiz e potência são como *dois idiomas,* [p=0.2] {b}e existe um *tradutor* "
        "entre eles. [p=0.4] {c}Raiz de dois [p=0.2] é dois elevado a quê? [p=0.4] {d}Raiz de dois, ao quadrado, [p=0.2] "
        "dá dois. [p=0.4] {e}E dois elevado a *um meio,* [p=0.2] ao quadrado, [p=0.2] é potência de potência: [p=0.2] um "
        "meio vezes dois, [p=0.2] dois elevado a *um.* [p=0.2] Também dá dois! [p=0.4] {f}Então raiz de dois [p=0.2] é "
        "*dois elevado a um meio.*"),
    dict(id="14", block="regra", text=
        "{t}Um expoente em forma de fração [p=0.2] se chama *expoente fracionário.* [p=0.4] {a}E o tradutor funciona "
        "assim: [p=0.3] {b}quem está *embaixo* na fração [p=0.2] vira a casinha da raiz, [p=0.2] o *índice.* [p=0.4] {c}Quem "
        "está *em cima* [p=0.2] vira o expoente de dentro. [p=0.4] {d}Raiz cúbica de cinco: [p=0.2] o três vai para "
        "baixo, [p=0.2] *cinco elevado a um terço.*"),
    dict(id="15", block="oito", text=
        "{t}Traduza *oito elevado a dois terços.* [p=0.4] {a}O três, embaixo, [p=0.2] vira o índice. [p=0.2] {b}O dois, em cima, [p=0.2] vira o expoente de dentro: [p=0.2] raiz cúbica de *oito ao quadrado.* [p=0.4] {c}Oito ao quadrado é sessenta e quatro, [p=0.2] e a raiz cúbica dá *quatro.* [p=0.4] {d}Atalho: [p=0.2] faça a *raiz primeiro.* [p=0.2] Raiz cúbica de oito é dois, [p=0.2] dois ao quadrado, [p=0.2] *quatro.* [p=0.3] Números menores, [p=0.2] mesma resposta."),

    # ================= BLOCO E/F: USO 1, MULTIPLICAR ÍNDICES DIFERENTES =================
    dict(id="16", block="multiplicar", text=
        "{t}E por que isso é poderoso? [p=0.3] {a}Virando potência, [p=0.2] *as sete propriedades* do episódio dois [p=0.2] valem para as raízes. [p=0.4] {b}Raiz de dois [p=0.2] vezes raiz cúbica de dois? [p=0.4] {c}Traduza: [p=0.2] dois elevado a um meio, [p=0.2] vezes dois elevado a um terço. [p=0.4] {d}Mesma base: [p=0.2] *soma os expoentes.* [p=0.4] {e}Com o MMC seis, [p=0.2] três sextos mais dois sextos, [p=0.2] *cinco sextos.* [p=0.4] {f}Dois elevado a cinco sextos: [p=0.2] a raiz sexta de dois à quinta."),

    # ================= BLOCO G: USO 2, COMPARAR ÍNDICES DIFERENTES =================
    dict(id="17", block="comparar", text=
        "{t}E para *comparar* raiz de dois [p=0.2] com raiz cúbica de três? [p=0.4] {a}Com índices diferentes, [p=0.2] não dá direto. [p=0.3] {b}Leve os dois para o *mesmo índice,* [p=0.2] pelo MMC dos índices: [p=0.2] o MMC de dois e três é seis. [p=0.4] {c}Um meio é *três sextos:* [p=0.2] raiz de dois vira raiz sexta de dois ao cubo, [p=0.2] *raiz sexta de oito.* [p=0.4] {d}Um terço é *dois sextos:* [p=0.2] raiz cúbica de três vira raiz sexta de três ao quadrado, [p=0.2] *raiz sexta de nove.* [p=0.4] {e}Oito é menor que nove: [p=0.2] raiz de dois é *menor.*"),
    dict(id="18", block="comparar_atalho", text=
        "{t}Dois atalhos. [p=0.3] {a}Com o *mesmo índice,* [p=0.2] compare só os números de dentro. [p=0.4] {b}E: [p=0.2] "
        "*o índice multiplicou por quanto, [p=0.2] o número de dentro é elevado a quanto.* [p=0.4] {c}O índice dois virou "
        "seis: [p=0.2] vezes três, [p=0.2] dois ao cubo, [p=0.2] oito. [p=0.3] {d}O três virou seis: [p=0.2] vezes dois, "
        "[p=0.2] três ao quadrado, [p=0.2] nove."),

    # ================= NÓS FAZEMOS =================
    dict(id="19", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Racionalize *três sobre raiz de três.* [p=0.4] {b}E escreva *vinte e sete elevado a um "
        "terço* [p=0.2] como raiz, [p=0.2] e calcule. [p=0.5] {p}Pause o vídeo e calcule. [p=2.0]"),
    dict(id="20", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Três sobre raiz de três: [p=0.2] vezes raiz de três, em cima e embaixo. [p=0.3] Fica três raiz de três sobre *três.* [p=0.3] {b}Três dividido por três é um: [p=0.2] sobra *raiz de três.* [p=0.5] {c}Vinte e sete elevado a um terço: [p=0.2] o três de baixo vira o índice, [p=0.2] *raiz cúbica de vinte e sete.* [p=0.3] {d}Que número ao cubo dá vinte e sete? [p=0.2] *Três.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="21", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] racionalizar é multiplicar por um disfarçado. [p=0.5] "
        "{b}Dois: [p=0.2] binômio com raiz? [p=0.2] Multiplique pelo conjugado. [p=0.5] {c}Três: [p=0.2] embaixo vira "
        "índice; [p=0.2] em cima vira expoente."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] multiplicar *só o denominador* pela raiz: [p=0.2] "
        "um sobre raiz de dois vira um sobre dois. [p=0.4] {b}Parece certo, [p=0.2] porque a raiz saiu do porão. [p=0.4] "
        "{c}Mas o valor mudou: [p=0.2] zero vírgula cinco não é zero vírgula setenta e um. [p=0.2] Multiplique *em cima e "
        "embaixo.*"),
    dict(id="23", block="erros", text=
        "{a}Segundo: [p=0.2] usar o *mesmo sinal* em vez do conjugado. [p=0.4] {b}Parece certo, [p=0.2] porque no caso um "
        "você multiplicou pelo próprio denominador. [p=0.4] {c}Mas raiz de cinco menos raiz de dois, [p=0.2] ao quadrado, "
        "[p=0.2] dá sete menos *duas raízes de dez.* [p=0.2] A raiz continua lá. [p=0.2] Troque o sinal do meio."),
    dict(id="24", block="erros", text=
        "{a}Terceiro: [p=0.2] comparar índices diferentes [p=0.2] *olhando o número de dentro.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque com o mesmo índice funciona. [p=0.4] {c}Mas raiz de três [p=0.2] é raiz sexta de vinte e sete, "
        "[p=0.2] e raiz cúbica de quatro [p=0.2] é raiz sexta de dezesseis. [p=0.3] O quatro é maior, [p=0.2] e mesmo "
        "assim *raiz de três ganha.*"),

    # ================= QUESTÃO 6 DO MATERIAL =================
    dict(id="25", block="q6", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}Racionalizando o "
        "denominador de *seis sobre raiz de cinco menos raiz de dois,* [p=0.2] obtém-se: [p=0.4] {qa}A: [p=0.2] dois raiz "
        "de cinco mais dois raiz de dois. [p=0.3] {qb}B: [p=0.2] seis raiz de cinco menos seis raiz de dois. [p=0.3] {qc}C: "
        "[p=0.2] raiz de cinco mais raiz de dois, [p=0.2] sobre três. [p=0.3] {qd}D: [p=0.2] dois raiz de três. [p=0.3] "
        "{qe}E: [p=0.2] raiz de cinco mais raiz de dois. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="26", block="q6", text=
        "{t}Binômio com raiz no porão: [p=0.2] *conjugado.* [p=0.3] {a}Multiplique em cima e embaixo por raiz de cinco mais raiz de dois. [p=0.4] {b}Embaixo, [p=0.2] diferença de quadrados: [p=0.2] cinco menos dois, [p=0.2] *três.* [p=0.4] {c}Em cima, [p=0.2] seis vezes o binômio. [p=0.4] {d}Seis dividido por três é *dois:* [p=0.2] dois vezes raiz de cinco mais raiz de dois. [p=0.4] {e}Distribuindo: [p=0.2] dois raiz de cinco mais dois raiz de dois. [p=0.3] {ok}*Letra A!*"),
    dict(id="27", block="q6", text=
        "{t}E as outras? [p=0.3] {xd}A D, [p=0.2] dois raiz de três, [p=0.2] é de quem fez raiz de cinco menos raiz de dois "
        "[p=0.2] virar raiz de três. [p=0.2] Raiz não se subtrai assim. [p=0.4] {xc}A C perdeu o seis de cima. [p=0.4] {xe}A "
        "E só trocou o sinal [p=0.2] e esqueceu as contas. [p=0.4] {xb}E a B errou o sinal do meio, [p=0.2] e não dividiu "
        "por três."),

    # ================= QUESTÃO 7 DO MATERIAL =================
    dict(id="28", block="q7", text=
        "{t}Mais uma do material. [p=0.3] {a}Colocando os números raiz de dois, [p=0.2] raiz cúbica de três [p=0.2] e raiz sexta de dez [p=0.2] em *ordem crescente,* [p=0.2] do menor para o maior, [p=0.2] obtém-se: [p=0.4] {qa}A: [p=0.2] raiz de dois, [p=0.2] raiz cúbica de três, [p=0.2] raiz sexta de dez. [p=0.3] {qb}B: [p=0.2] raiz sexta de dez, [p=0.2] raiz cúbica de três, [p=0.2] raiz de dois. [p=0.3] {qc}C: [p=0.2] raiz cúbica de três, [p=0.2] raiz de dois, [p=0.2] raiz sexta de dez. [p=0.3] {qd}D: [p=0.2] raiz de dois, [p=0.2] raiz sexta de dez, [p=0.2] raiz cúbica de três. [p=0.3] {qe}E: [p=0.2] raiz sexta de dez, [p=0.2] raiz de dois, [p=0.2] raiz cúbica de três. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="29", block="q7", text=
        "{t}Índices diferentes: [p=0.2] *mesmo índice primeiro.* [p=0.3] {a}O MMC de dois, três e seis é *seis.* [p=0.4] {b}Raiz de dois: [p=0.2] índice vezes três, [p=0.2] dois ao cubo, [p=0.2] *raiz sexta de oito.* [p=0.4] {c}Raiz cúbica de três: [p=0.2] vezes dois, [p=0.2] três ao quadrado, [p=0.2] *raiz sexta de nove.* [p=0.4] {d}A raiz sexta de dez já está pronta. [p=0.4] {e}Oito, nove, dez: [p=0.2] raiz de dois, [p=0.2] raiz cúbica de três, [p=0.2] raiz sexta de dez. [p=0.3] {ok}*Letra A!*"),
    dict(id="30", block="q7", text=
        "{t}Repare na *surpresa:* [p=0.3] {a}a raiz sexta de dez [p=0.2] tem o *maior índice,* [p=0.2] e mesmo assim é a "
        "*maior.* [p=0.4] {xb}Quem acha que índice maior sempre dá número menor [p=0.2] marca a B, [p=0.3] {xe}ou a E. "
        "[p=0.4] {xd}A D elevou o três ao cubo, [p=0.2] em vez de ao quadrado. [p=0.4] {xc}E a C trocou, no chute, [p=0.2] "
        "dois números pertinhos: [p=0.2] um vírgula quarenta e um [p=0.2] e um vírgula quarenta e quatro."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="31", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] racionalizar é multiplicar por um disfarçado. "
        "[p=0.5] {b}Dois: [p=0.2] binômio com raiz? [p=0.2] Multiplique pelo conjugado. [p=0.5] {c}Três: [p=0.2] embaixo "
        "vira índice; [p=0.2] em cima vira expoente."),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] a gente *junta tudo,* [p=0.3] {b}caça as *pegadinhas* [p=0.3] {c}e "
        "treina com *questões novas.* [p=0.4] {d}Próximo episódio: [p=0.2] *a revisão.*"),
    dict(id="33", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você achava que raiz sexta de dez era a menor? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
