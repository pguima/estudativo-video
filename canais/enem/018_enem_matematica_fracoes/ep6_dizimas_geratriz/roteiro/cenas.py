# Roteiro — Frações, Decimais e Dízimas, Episódio 6 de 8: Decimal exato ou dízima? E a fração geratriz (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/03-fracoes-decimais-dizimas.html — seções 08 e 09 + Questões 3 e 4 da seção 12
#   + questão extra do sensor (de outro material da série, enviada completa no prompt).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora: o nosso sistema é feito de 10, e 10 = 2 × 5 (só 2 e 5 "cabem" em 10, 100, 1000) · a geratriz é a "MÃE"
#   da dízima · no método algébrico, DUAS FITAS com a mesma cauda infinita: subtraindo uma da outra, a cauda some.
# Contas conferidas em Python:
#   1/4 = 0,25 · 1/3 = 0,333… · 3/8 = 0,375 (8 = 2³) · 7/20 = 0,35 (20 = 2²·5) · 9/40 = 0,225 (40 = 2³·5) ·
#   5/12 = 0,41666… (12 = 2²·3) · 2/7 = 0,285714… · 6/12 = 1/2 = 0,5 · 40 → 20 → 10 → 5 → 1 · 12 → 6 → 3 (sobra 3)
#   0,777… = 7/9 (10x − x = 7) · 0,8333… = 75/90 = 5/6 (100x − 10x = 75; ÷15) · 0,2323… = 23/99 ·
#   1,2454545… = (1245 − 12)/990 = 1233/990 = 411/330 = 137/110 (÷3 duas vezes = ÷9) · 0,999… = 9/9 = 1 · 1/3 × 3 = 1.
#   Q3 (material): exatos 3/8, 7/20, 9/40 → 3 → C.
#   Sensor (extra): (83 − 8)/90 = 75/90 = 5/6 → A · B 83/100 = 0,83 (parou o 3) · C 833/999 = 0,833833… (repete o 833 todo) ·
#     D 25/3 = 8,333… (é o 10x, não o x) · E 4/5 = 0,8 (ignorou a parte que repete). B e C pedidas no prompt; D e E são minhas.
#   Q4 (material): 1233/990 → irredutível 137/110 → B · A 1233/990 = armadilha de quem não simplificou.
# Frases-chave (meio e fim, idênticas):
#   1. Denominador só com 2 e 5: acaba. Outro primo: dízima.
#   2. Simplifique antes de aplicar o critério.
#   3. Geratriz: 9 para cada algarismo que repete, 0 para cada um que não repete.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Decimal exato ou dízima? E como achar a fração geratriz | Frações Ep. 6"
# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de matemática: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa e suspense nas armadilhas; comemore os acertos com entusiasmo; dê ênfase forte "
            "às palavras-chave. Nas contas, fale devagar e com clareza, número por número. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Zero vírgula nove, nove, nove, [p=0.2] repetindo para sempre. [p=0.4] {b}É *quase* um? [p=0.6] {c}Não. [p=0.3] "
        "É *exatamente* um. [p=0.5] {d}Ao final deste vídeo, [p=0.2] você vai conseguir *provar* isso, [p=0.3] {e}e de quebra "
        "vai transformar *qualquer dízima* em fração."),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai saber *de antemão* [p=0.2] se uma fração vira decimal exato ou dízima, [p=0.4] {b}e "
        "achar a *fração geratriz* de qualquer dízima."),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}Número *primo* é o que só divide por um e por ele mesmo, [p=0.2] como "
        "dois, três, cinco e sete. [p=0.3] {b}*Fatorar* é escrever o número como multiplicação de primos: [p=0.2] doze é dois "
        "vezes dois vezes três. [p=0.4] {c}Fração *irredutível* é a que não dá mais para simplificar, [p=0.2] como no episódio "
        "um. [p=0.3] {d}E *racional* é todo número que vira fração."),

    # ================= CONCRETO: DIVIDIR DE VERDADE =================
    dict(id="04", block="dividir", text=
        "{t}Vamos dividir de verdade. [p=0.3] {a}Um dividido por quatro. [p=0.3] {b}Um não dá para dividir por quatro, [p=0.2] "
        "então põe zero, vírgula, [p=0.2] e o um vira dez. [p=0.4] {c}Dez dividido por quatro: [p=0.2] dois, [p=0.2] e sobra "
        "dois. [p=0.3] {d}O dois vira vinte. [p=0.2] Vinte dividido por quatro: [p=0.2] cinco, [p=0.2] e sobra *zero.* [p=0.4] "
        "{e}Acabou: [p=0.2] *zero vírgula vinte e cinco.*"),
    dict(id="05", block="dividir", text=
        "{t}Agora, um dividido por três. [p=0.3] {a}O um vira dez. [p=0.2] Dez dividido por três: [p=0.2] três, [p=0.2] e "
        "sobra *um.* [p=0.4] {b}O um vira dez de novo. [p=0.2] Três, [p=0.2] e sobra *um.* [p=0.4] {c}De novo. [p=0.2] E de "
        "novo. [p=0.4] {d}O resto *um* volta sempre. [p=0.3] {e}Essa divisão *nunca acaba:* [p=0.2] zero vírgula três, três, "
        "três, [p=0.2] para sempre."),
    dict(id="06", block="dividir", text=
        "{t}Esses dois resultados têm nome. [p=0.3] {a}Quando a divisão acaba, [p=0.2] é um *decimal exato.* [p=0.4] {b}Quando "
        "um pedaço se repete para sempre, [p=0.2] é uma *dízima periódica.* [p=0.3] {c}Os três pontinhos: [p=0.2] continua igual, "
        "sem parar."),

    # ================= BLOCO A: O CRITÉRIO =================
    dict(id="07", block="dez", text=
        "{t}Será que dá para saber *antes* de dividir [p=0.2] se vai acabar? [p=0.5] {a}Dá. [p=0.2] E o segredo está no *dez.* "
        "[p=0.4] {b}O nosso sistema de números é feito de dez, [p=0.2] e dez é *dois vezes cinco.* [p=0.4] {c}Por isso, só "
        "denominadores feitos de dois e de cinco [p=0.2] *cabem* certinho em dez, cem, mil. [p=0.4] {d}Qualquer outro primo "
        "*não cabe,* [p=0.2] e a divisão fica repetindo para sempre."),
    dict(id="08", block="criterio", text=
        "{t}Então, o critério. [p=0.3] {a}Com a fração já simplificada, [p=0.2] fatore o denominador. [p=0.4] {b}Só dois e cinco? "
        "[p=0.2] *Decimal exato.* [p=0.4] {c}Apareceu qualquer outro primo? [p=0.2] *Dízima.* [p=0.4] {d}Três oitavos: [p=0.2] "
        "oito é dois vezes dois vezes dois. [p=0.2] Exato. [p=0.3] {e}Sete vinte avos: [p=0.2] vinte é dois, dois e cinco. "
        "[p=0.2] Exato."),
    dict(id="09", block="criterio", text=
        "{a}Nove quarenta avos: [p=0.2] quarenta é dois, dois, dois e cinco. [p=0.2] Exato. [p=0.4] {b}Cinco doze avos: [p=0.2] "
        "doze tem o *três.* [p=0.2] Dízima. [p=0.4] {c}Dois sétimos: [p=0.2] o sete é primo, [p=0.2] e não é dois nem cinco. "
        "[p=0.2] Dízima."),
    dict(id="10", block="criterio", text=
        "{t}E um atalho para fatorar rápido. [p=0.4] {a}Pegue o denominador [p=0.2] e vá dividindo por dois e por cinco, "
        "[p=0.2] enquanto der. [p=0.4] {b}Quarenta, vinte, dez, cinco, [p=0.2] *um.* [p=0.2] Chegou no um? [p=0.2] Acaba. "
        "[p=0.4] {c}Doze, seis, [p=0.2] *três.* [p=0.2] Travou num número diferente de um? [p=0.2] Dízima."),

    # ================= BLOCO B: SIMPLIFIQUE ANTES =================
    dict(id="11", block="simplificar", text=
        "{t}E esta aqui? [p=0.2] Seis doze avos. [p=0.4] {a}Doze tem o três, [p=0.2] então *parece* dízima. [p=0.5] {b}Mas "
        "simplifique antes: [p=0.2] seis doze avos é *um meio.* [p=0.4] {c}E um meio dá zero vírgula cinco: [p=0.2] decimal "
        "*exato.* [p=0.4] {d}O três do doze era de mentira: [p=0.2] ele cancelava com o três do seis. [p=0.3] {e}O critério só "
        "vale na fração *irredutível.*"),

    # ================= BLOCO C: ANATOMIA DA DÍZIMA =================
    dict(id="12", block="anatomia", text=
        "{t}Agora, vamos abrir uma dízima por dentro. [p=0.3] {a}Dois vírgula três, quatro, cinco, quatro, cinco, [p=0.2] e "
        "assim por diante. [p=0.4] {b}O que vem antes da vírgula [p=0.2] é a *parte inteira:* [p=0.2] o dois. [p=0.4] {c}O "
        "pedaço que se repete [p=0.2] se chama *período:* [p=0.2] aqui, o quarenta e cinco."),
    dict(id="13", block="anatomia", text=
        "{t}E sobrou alguém. [p=0.3] {a}O três vem depois da vírgula, [p=0.2] mas *não* se repete. [p=0.4] {b}Ele é a *parte "
        "não periódica:* [p=0.2] o que está entre a vírgula e o período."),
    dict(id="14", block="anatomia", text=
        "{t}E isso separa as dízimas em dois tipos. [p=0.3] {a}Zero vírgula sete, sete, sete: [p=0.2] repete logo depois da "
        "vírgula. [p=0.2] É uma dízima *simples.* [p=0.4] {b}Zero vírgula oito, três, três, três: [p=0.2] o oito *não* repete. "
        "[p=0.2] Tem parte não periódica. [p=0.2] É uma dízima *composta.*"),
    dict(id="15", block="anatomia", text=
        "{t}E aqui vem a boa notícia. [p=0.3] {a}*Toda* dízima periódica é racional: [p=0.2] existe uma fração exata que "
        "gera aquela repetição. [p=0.4] {b}Essa fração se chama *fração geratriz.* [p=0.4] {c}Pense nela como a *mãe* da "
        "dízima. [p=0.3] Vamos encontrar essa mãe."),

    # ================= BLOCO D: MÉTODO NA DÍZIMA SIMPLES =================
    dict(id="16", block="simples", text=
        "{t}Como achar a mãe de zero vírgula sete, sete, sete? [p=0.4] {a}Chame esse número de *xis.* [p=0.4] {b}Multiplicar "
        "por dez [p=0.2] empurra a vírgula uma casa para a direita. [p=0.3] {c}Então dez xis é sete vírgula sete, sete, sete. "
        "[p=0.4] {d}Repare: [p=0.2] os dois números têm a *mesma cauda* infinita de setes."),
    dict(id="17", block="simples", text=
        "{t}Pense em duas *fitas* com a mesma cauda. [p=0.4] {a}Quando você subtrai uma da outra, [p=0.3] {b}a cauda *some.* "
        "[p=0.5] {c}Dez xis menos xis [p=0.2] dá *nove xis.* [p=0.2] E sete vírgula sete, sete, menos zero vírgula sete, sete, "
        "[p=0.2] dá *sete.* [p=0.4] {d}Nove xis igual a sete. [p=0.2] Dividindo os dois lados por nove: [p=0.2] xis é *sete "
        "nonos.* [p=0.4] {e}Confira: [p=0.2] sete dividido por nove dá zero vírgula sete, sete, sete."),

    # ================= BLOCO E: MÉTODO NA DÍZIMA COMPOSTA =================
    dict(id="18", block="composta", text=
        "{t}E se a dízima for composta? [p=0.3] Zero vírgula oito, três, três, três. [p=0.4] {a}Aqui o oito atrapalha. [p=0.2] "
        "Então, primeiro, [p=0.2] jogue o oito para antes da vírgula: [p=0.2] *dez xis* é oito vírgula três, três, três. [p=0.4] "
        "{b}Depois, [p=0.2] jogue também *um* período: [p=0.2] *cem xis* é oitenta e três vírgula três, três, três."),
    dict(id="19", block="composta", text=
        "{t}Agora as duas fitas têm a mesma cauda de três. [p=0.4] {a}Cem xis menos dez xis: [p=0.2] *noventa xis.* [p=0.3] "
        "{b}Oitenta e três menos oito: [p=0.2] *setenta e cinco.* [p=0.2] A cauda some. [p=0.4] {c}Xis é setenta e cinco "
        "noventa avos. [p=0.3] {d}Dividindo em cima e embaixo por quinze: [p=0.2] *cinco sextos.* [p=0.4] {e}Confira: [p=0.2] "
        "cinco dividido por seis [p=0.2] dá zero vírgula oito, três, três, três."),

    # ================= BLOCO F: A REGRA PRÁTICA =================
    dict(id="20", block="regra", text=
        "{t}O método explica tudo. [p=0.2] Mas existe uma regra que faz em *um passo.* [p=0.4] {a}No *numerador:* [p=0.2] "
        "escreva o número todo, sem a vírgula, [p=0.2] e tire a parte que *não* repete, [p=0.2] ou seja, [p=0.2] tudo o que vem antes do período. [p=0.5] {b}No *denominador:* [p=0.2] um "
        "*nove* para cada algarismo do período, [p=0.3] {c}seguido de um *zero* para cada algarismo da parte não periódica."),
    dict(id="21", block="atalho_simples", text=
        "{t}Nas dízimas simples, [p=0.2] o atalho é: [p=0.2] *noves embaixo.* [p=0.4] {a}Zero vírgula sete, sete: [p=0.2] um "
        "algarismo repete, [p=0.2] um nove. [p=0.2] *Sete nonos.* [p=0.4] {b}Zero vírgula vinte e três, vinte e três: [p=0.2] "
        "dois algarismos repetem, [p=0.2] dois noves. [p=0.2] *Vinte e três, noventa e nove avos.* [p=0.4] {c}O período vai em "
        "cima, [p=0.2] os noves embaixo."),
    dict(id="22", block="atalho_composta", text=
        "{t}E numa composta de verdade: [p=0.2] um vírgula dois, quatro, cinco, quatro, cinco. [p=0.4] {a}Numerador: [p=0.2] "
        "sem vírgula, [p=0.2] mil duzentos e quarenta e cinco, [p=0.2] menos o que não repete, [p=0.2] doze. [p=0.2] Dá *mil "
        "duzentos e trinta e três.* [p=0.4] {b}Denominador: [p=0.2] o período tem dois algarismos, [p=0.2] dois noves. [p=0.2] "
        "Um algarismo não repete, [p=0.2] um zero. [p=0.2] *Novecentos e noventa.* [p=0.4] {c}Dividindo em cima e embaixo por "
        "nove: [p=0.2] *cento e trinta e sete, cento e dez avos.*"),

    # ================= BLOCO G: 0,999… = 1 =================
    dict(id="23", block="noves", text=
        "{t}E agora, [p=0.2] a prova que eu prometi. [p=0.3] {a}Xis é zero vírgula nove, nove, nove. [p=0.3] {b}Dez xis é nove "
        "vírgula nove, nove, nove. [p=0.4] {c}As fitas têm a mesma cauda. [p=0.2] Dez xis menos xis: [p=0.2] *nove xis igual a "
        "nove.* [p=0.4] {d}Então xis é *um.* [p=0.4] {e}E pela regra: [p=0.2] um nove no período, [p=0.2] nove nonos: [p=0.2] "
        "*um.* [p=0.4] {f}Não é arredondamento. [p=0.2] É o *mesmo número,* [p=0.2] escrito de dois jeitos."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="24", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] denominador só com dois e cinco: [p=0.2] acaba. [p=0.2] Outro "
        "primo: [p=0.2] dízima. [p=0.5] {b}Dois: [p=0.2] simplifique antes de aplicar o critério. [p=0.5] {c}Três: [p=0.2] "
        "geratriz: [p=0.2] nove para cada algarismo que repete, [p=0.2] zero para cada um que não repete."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="25", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] aplicar o critério *sem simplificar.* [p=0.4] {b}Parece "
        "certo, [p=0.2] porque o denominador está ali, [p=0.2] é só fatorar. [p=0.4] {c}Mas um fator pode cancelar. [p=0.2] Seis "
        "doze avos é um meio: [p=0.2] exato."),
    dict(id="26", block="erros", text=
        "{a}Segundo: [p=0.2] achar que dízima periódica é *irracional.* [p=0.4] {b}Parece certo, [p=0.2] porque ela nunca acaba. "
        "[p=0.4] {c}Mas ela *repete,* [p=0.2] e toda dízima que repete tem uma mãe: [p=0.2] a fração geratriz. [p=0.2] É "
        "racional."),
    dict(id="27", block="erros", text=
        "{a}Terceiro: [p=0.2] parar na geratriz *sem simplificar,* [p=0.2] quando a questão pede a irredutível. [p=0.4] {b}Parece "
        "certo, [p=0.2] porque a fração vale o mesmo. [p=0.4] {c}Mas a alternativa sem simplificar está lá, [p=0.2] esperando. "
        "[p=0.2] Simplifique até o fim."),
    dict(id="28", block="erros", text=
        "{a}Quarto: [p=0.2] achar que zero vírgula nove, nove, nove é *quase* um. [p=0.4] {b}Parece certo, [p=0.2] porque "
        "sempre falta um pedacinho. [p=0.4] {c}Mas os noves nunca param: [p=0.2] não falta nada. [p=0.2] Nove nonos: [p=0.2] "
        "*exatamente* um."),

    # ================= QUESTÃO 3 (EU FAÇO) =================
    dict(id="29", block="q3", text=
        "{t}Agora, questões no estilo do ENEM. [p=0.3] Esta eu resolvo com você. [p=0.4] {a}Considere as frações: [p=0.2] três "
        "oitavos, [p=0.2] cinco doze avos, [p=0.2] sete vinte avos, [p=0.2] dois sétimos [p=0.2] e nove quarenta avos. [p=0.4] "
        "{b}Quantas delas resultam em decimal exato? [p=0.4] {c}A: [p=0.2] uma. [p=0.2] {d}B: [p=0.2] duas. [p=0.2] {e}C: "
        "[p=0.2] três. [p=0.2] {f}D: [p=0.2] quatro. [p=0.2] {g}E: [p=0.2] cinco."),
    dict(id="30", block="q3", text=
        "{t}Primeiro: [p=0.2] todas já estão irredutíveis. [p=0.4] {a}Agora, fatore cada denominador. [p=0.3] {b}Oito: [p=0.2] "
        "só dois. [p=0.2] Exato. [p=0.3] {c}Doze: [p=0.2] tem o três. [p=0.2] Dízima. [p=0.3] {d}Vinte: [p=0.2] dois e cinco. "
        "[p=0.2] Exato. [p=0.3] {e}Sete: [p=0.2] dízima. [p=0.3] {f}Quarenta: [p=0.2] dois e cinco. [p=0.2] Exato. [p=0.4] "
        "{g}Três exatos. [p=0.2] {ok}*Letra C!*"),

    # ================= QUESTÃO EXTRA DO SENSOR (NÓS FAZEMOS) =================
    dict(id="31", block="sensor", text=
        "{t}Esta a gente faz junto. [p=0.4] {a}Um sensor registra uma medida de zero vírgula oito, três, três, três metro, "
        "[p=0.2] com o algarismo três repetindo indefinidamente. [p=0.4] {b}Essa medida corresponde exatamente à fração: "
        "[p=0.4] {c}A: [p=0.2] cinco sextos. [p=0.2] {d}B: [p=0.2] oitenta e três centésimos. [p=0.2] {e}C: [p=0.2] oitocentos "
        "e trinta e três, novecentos e noventa e nove avos. [p=0.2] {f}D: [p=0.2] vinte e cinco terços. [p=0.2] {g}E: [p=0.2] "
        "quatro quintos."),
    dict(id="32", block="sensor", text=
        "{t}Me ajuda: [p=0.2] simples ou composta? [p=0.4] {a}O oito não repete, [p=0.2] o três repete: [p=0.2] *composta.* "
        "[p=0.4] {b}Numerador: [p=0.2] oitenta e três menos oito, [p=0.2] setenta e cinco. [p=0.3] {c}Denominador: [p=0.2] um "
        "nove e um zero, [p=0.2] noventa. [p=0.4] {d}Setenta e cinco noventa avos, [p=0.2] que simplifica para *cinco sextos.* "
        "[p=0.3] {ok}*Letra A!*"),
    dict(id="33", block="sensor", text=
        "{t}E de onde vêm as outras? [p=0.4] {a}A B, [p=0.2] oitenta e três centésimos, [p=0.2] é zero vírgula oitenta e três, "
        "[p=0.2] *parou* o três. [p=0.4] {b}A C, [p=0.2] com novecentos e noventa e nove embaixo, [p=0.2] repete o oitocentos e "
        "trinta e três *inteiro,* [p=0.2] como se fosse simples."),

    # ================= QUESTÃO 4 (VOCÊ FAZ) =================
    dict(id="34", block="q4", text=
        "{t}Agora é com você. [p=0.4] {a}Um equipamento registra a medida um vírgula dois, quatro, cinco, quatro, cinco, "
        "[p=0.2] em que o bloco quarenta e cinco se repete indefinidamente. [p=0.4] {b}A fração irredutível correspondente a "
        "essa medida é: [p=0.4] {c}A: [p=0.2] mil duzentos e trinta e três, novecentos e noventa avos. [p=0.2] {d}B: [p=0.2] "
        "cento e trinta e sete, cento e dez avos. [p=0.2] {e}C: [p=0.2] mil duzentos e quarenta e cinco, novecentos e noventa "
        "e nove avos. [p=0.2] {f}D: [p=0.2] duzentos e quarenta e nove, duzentos avos. [p=0.2] {g}E: [p=0.2] quarenta e cinco, "
        "noventa e nove avos. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="35", block="q4", text=
        "{t}Vamos conferir. [p=0.3] {a}Parte não periódica: [p=0.2] dois. [p=0.2] Período: [p=0.2] quarenta e cinco. [p=0.4] "
        "{b}Numerador: [p=0.2] mil duzentos e quarenta e cinco menos doze, [p=0.2] mil duzentos e trinta e três. [p=0.4] "
        "{c}Denominador: [p=0.2] dois noves e um zero, [p=0.2] novecentos e noventa. [p=0.4] {d}Mas a questão pede a "
        "*irredutível.* [p=0.3] Dividindo por três, [p=0.2] e por três de novo: [p=0.2] *cento e trinta e sete, cento e dez "
        "avos.* [p=0.3] {ok}*Letra B!*"),
    dict(id="36", block="q4", text=
        "{t}E repare na letra A. [p=0.3] {a}Mil duzentos e trinta e três, novecentos e noventa avos [p=0.2] é o *mesmo* número. "
        "[p=0.4] {b}Mas não é irredutível. [p=0.3] {c}É a armadilha de quem parou *antes* de simplificar."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="37", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] denominador só com dois e cinco: [p=0.2] acaba. [p=0.2] "
        "Outro primo: [p=0.2] dízima. [p=0.5] {b}Dois: [p=0.2] simplifique antes de aplicar o critério. [p=0.5] {c}Três: "
        "[p=0.2] geratriz: [p=0.2] nove para cada algarismo que repete, [p=0.2] zero para cada um que não repete."),

    # ================= PONTE E CTA =================
    dict(id="38", block="ponte", text=
        "{a}Fração, decimal e porcentagem [p=0.2] são *três idiomas* do mesmo número. [p=0.4] {b}Existe uma tabela que, se você "
        "decorar, [p=0.2] economiza minutos em porcentagem, [p=0.2] probabilidade e estatística. [p=0.4] {c}Próximo episódio."),
    dict(id="39", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você acreditava que zero vírgula nove, nove, nove era *quase* um? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
