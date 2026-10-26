# Roteiro — Frações, Decimais e Dízimas, Episódio 3 de 8: As quatro operações com frações (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/03-fracoes-decimais-dizimas.html — seção 06 (SEM o quadro "do restante", que tem
#   episódio próprio; potência só com expoente POSITIVO: o (2/3)^−2 do material fica para Potenciação) + Questão 9 da seção 12.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   SOMA: não dá para somar fatias de tamanhos diferentes; primeiro recorte todas as pizzas no MESMO tamanho de fatia
#     (o denominador comum, pelo MMC).
#   MULTIPLICAÇÃO: multiplicar é tirar uma fração DE outra — metade de 1/3 da barra de chocolate (retoma "de = vezes" do ep1).
#   DIVISÃO: dividir é perguntar quantas vezes uma cabe na outra (quantos copos de 2/5 de litro cabem em 3/4 de litro?).
# Pré-requisitos: MMC = "o reencontro" (série 015) · simplificar pelo MDC (ep1) · potência 2³ = 2 · 2 · 2.
# Atalhos (verde, pedido de 22/10): varal do MMC (6, 4, 3 → 2, 2, 3 → MMC = 12) · converter "divide pelo de baixo,
#   multiplica pelo de cima" (ep1) · borboleta para DUAS frações (a/b + c/d = (a·d + b·c)/(b·d)) · corte em cruz ·
#   na divisão, corte em cruz depois de inverter.
# Contas (todas conferidas): 1/2 + 1/3 = 3/6 + 2/6 = 5/6 (2/5 < 1/2 < 5/6) · 1/6 + 1/4 + 1/3 = 2/12 + 3/12 + 4/12 = 9/12 = 3/4 ·
#   exemplo próprio de subtração: 3/4 − 1/6 = 9/12 − 2/12 = 7/12 · 1/2 · 1/3 = 1/6 (barra 3 × 2) · 4/9 · 3/8 = 1/6
#   (corta 4 com 8 → 1 e 2; 3 com 9 → 1 e 3; sem cortar: 12/72 = 1/6) · 1 ÷ 1/2 = 2 · 3/4 ÷ 2/5 = 3/4 · 5/2 = 15/8
#   (= 0,75 ÷ 0,4 = 1,875: quase 2 copos) · (2/3)³ = 2³/3³ = 8/27 · exercício: 2/3 + 1/4 = 8/12 + 3/12 = 11/12 ·
#   5/6 ÷ 1/3 = 5/6 · 3/1 = 15/6 = 5/2.
# QUESTÃO 9 (lida exatamente como no material): gabarito B (falta 1/4). A 1/6 e C 1/3 = repetiram uma turma ·
#   D 3/4 = o que foi ARRECADADO, não o que falta · E 1/13: o material diz "quem somou termo a termo", mas somar termo a
#   termo dá 3/13 (e faltaria 10/13), não 1/13. No vídeo: o 13 da alternativa E vem de somar os DENOMINADORES (6 + 4 + 3);
#   é a pista da soma termo a termo — dito sem afirmar que a conta dá 1/13.
# Frases-chave (meio e fim, idênticas):
#   1. Somar e subtrair: mesmo denominador antes, pelo MMC.
#   2. Multiplicar: corte em cruz antes, multiplique depois.
#   3. Dividir: conserva a primeira, inverte a segunda.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "1/2 + 1/3 dá 2/5? As quatro operações com frações sem calculadora | Frações Ep. 3"
# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de fração: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa nas armadilhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, fale devagar e com clareza, número por número. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
    "MMC": "M M C",
    "MDC": "M D C",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Um meio mais um terço [p=0.2] dá *dois quintos?* [p=0.5] {b}Parece lógico: [p=0.2] um mais um, dois; [p=0.2] dois "
        "mais três, cinco. [p=0.4] {c}E está *errado.* [p=0.5] {d}Vou te provar com uma pizza, [p=0.2] em dez segundos."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai fazer as *quatro operações* com frações [p=0.3] {b}sem calculadora, [p=0.4] "
        "{c}e sem cair nas pegadinhas."),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}O *MMC,* [p=0.2] da série anterior, [p=0.2] é o reencontro: [p=0.2] o menor "
        "número que está na tabuada de todos ao mesmo tempo. [p=0.4] {b}Simplificar, [p=0.2] do episódio um, [p=0.2] é dividir em "
        "cima e embaixo pelo mesmo número. [p=0.4] {c}E *potência* é multiplicação repetida: [p=0.2] dois ao cubo é dois vezes "
        "dois vezes dois, [p=0.2] oito."),

    # ================= BLOCO A: A PROVA VISUAL =================
    dict(id="04", block="prova", text=
        "{t}Então, a prova. [p=0.3] {a}Pegue *meia* pizza. [p=0.4] {b}Agora, junte mais *um terço* de outra pizza. [p=0.4] "
        "{c}Você ficou com *mais* que meia pizza, [p=0.2] certo? [p=0.2] Já tinha a metade, [p=0.2] e ainda ganhou mais. [p=0.5] "
        "{d}Agora olhe dois quintos: [p=0.2] dois pedaços de uma pizza cortada em cinco. [p=0.4] {e}Isso é *menos* que a metade! "
        "[p=0.5] {f}A soma não pode ser dois quintos."),
    dict(id="05", block="prova", text=
        "{t}E quanto dá, então? [p=0.3] {a}Recorte as duas em *seis* fatias. [p=0.4] {b}A metade vira *três sextos.* [p=0.3] "
        "{c}O terço vira *dois sextos.* [p=0.4] {d}Três sextos mais dois sextos: [p=0.2] *cinco sextos.* [p=0.4] {e}Agora sim, "
        "[p=0.2] mais que a metade. [p=0.4] {f}Guarde esse teste rápido: [p=0.2] antes de aceitar o resultado de uma conta, "
        "[p=0.2] compare com a *metade.* [p=0.2] Ele pega muito erro na prova."),

    # ================= BLOCO B: SOMA E SUBTRAÇÃO =================
    dict(id="06", block="soma", text=
        "{t}Esse é o segredo da soma. [p=0.3] {a}Não dá para somar fatias de *tamanhos diferentes.* [p=0.4] {b}Primeiro, [p=0.2] "
        "recorte todas as pizzas no *mesmo tamanho de fatia.* [p=0.4] {c}Esse tamanho comum se chama *denominador comum:* [p=0.2] "
        "o mesmo número embaixo de todas as frações. [p=0.4] {d}E quem acha esse número [p=0.2] é o *MMC.*"),
    dict(id="07", block="soma", text=
        "{t}Vou fazer na sua frente. [p=0.3] {a}Um sexto, [p=0.2] mais um quarto, [p=0.2] mais um terço. [p=0.4] {b}Três pizzas "
        "cortadas de jeitos diferentes: [p=0.2] em seis, [p=0.2] em quatro [p=0.2] e em três. [p=0.4] {c}Qual é o MMC de seis, "
        "quatro e três? [p=0.4] {d}O atalho é o varal: [p=0.2] divide os três juntos por dois, [p=0.2] por dois de novo, [p=0.2] "
        "e por três. [p=0.4] {e}Dois vezes dois vezes três: [p=0.2] *doze.* [p=0.3] Todo mundo vai virar *doze* fatias."),
    dict(id="08", block="soma", text=
        "{t}Agora, converter cada fração para doze avos. [p=0.3] {a}O atalho do episódio um: [p=0.2] divide pelo de baixo, "
        "[p=0.2] multiplica pelo de cima. [p=0.4] {b}Um sexto: [p=0.2] doze dividido por seis, [p=0.2] dois. [p=0.2] Vezes um, "
        "[p=0.2] *dois doze avos.* [p=0.4] {c}Um quarto: [p=0.2] doze dividido por quatro, [p=0.2] três. [p=0.2] *Três doze avos.* "
        "[p=0.4] {d}Um terço: [p=0.2] doze dividido por três, [p=0.2] quatro. [p=0.2] *Quatro doze avos.*"),
    dict(id="09", block="soma", text=
        "{t}Com as fatias do mesmo tamanho, [p=0.2] agora sim, [p=0.2] soma só em cima. [p=0.4] {a}Dois mais três mais quatro: "
        "[p=0.2] *nove doze avos.* [p=0.4] {b}E simplifica: [p=0.2] dividindo por três, [p=0.2] *três quartos.* [p=0.4] "
        "{c}Repare: [p=0.2] o denominador *não* se soma. [p=0.2] O doze é só o tamanho da fatia."),
    dict(id="10", block="soma", text=
        "{t}E a subtração é igualzinha. [p=0.3] {a}Três quartos menos um sexto. [p=0.4] {b}MMC de quatro e seis: [p=0.2] "
        "doze. [p=0.3] {c}Três quartos vira nove doze avos. [p=0.2] Um sexto vira dois doze avos. [p=0.4] {d}Agora tira só em "
        "cima: [p=0.2] nove menos dois, [p=0.2] *sete doze avos.* [p=0.4] {e}Sete e doze não têm divisor comum, [p=0.2] então "
        "já está simplificada."),
    dict(id="11", block="soma", text=
        "{t}E um atalho extra, [p=0.2] quando são só *duas* frações: [p=0.2] a *borboleta.* [p=0.4] {a}Um meio mais um terço. "
        "[p=0.3] {b}Em cima: [p=0.2] um vezes três, [p=0.2] mais dois vezes um, [p=0.2] cinco. [p=0.4] {c}Embaixo: [p=0.2] dois "
        "vezes três, [p=0.2] seis. [p=0.4] {d}*Cinco sextos,* [p=0.2] sem procurar MMC. [p=0.3] {e}Depois, [p=0.2] é só conferir "
        "se dá para simplificar."),

    # ================= BLOCO C: MULTIPLICAÇÃO =================
    dict(id="12", block="mult", text=
        "{t}Agora, a multiplicação. [p=0.3] Quanto é *metade de um terço* da barra? [p=0.4] {a}Olha a barra de chocolate, "
        "[p=0.2] em seis quadradinhos. [p=0.3] {b}Um terço é esta coluna. [p=0.4] {c}A metade dela: [p=0.2] *um* quadradinho. "
        "[p=0.3] {d}De seis. [p=0.2] *Um sexto.* [p=0.5] {e}Lembra do episódio um? [p=0.2] O *de* é vezes: [p=0.2] um meio vezes "
        "um terço, [p=0.2] um sexto."),
    dict(id="13", block="mult", text=
        "{t}E a regra é a mais fácil de todas. [p=0.4] {a}Numerador vezes numerador, [p=0.3] {b}denominador vezes denominador. "
        "[p=0.4] {c}Um vezes um, [p=0.2] um. [p=0.2] Dois vezes três, [p=0.2] seis. [p=0.4] {d}Na multiplicação, [p=0.2] *não "
        "precisa* de denominador comum. [p=0.4] {e}E se aparecer um número inteiro, [p=0.2] como o três? [p=0.2] Escreva três "
        "sobre um, [p=0.2] e siga a mesma regra."),
    dict(id="14", block="mult", text=
        "{t}Mas tem um atalho que salva contas enormes: [p=0.3] *simplificar em cruz,* [p=0.2] antes de multiplicar. [p=0.4] "
        "{a}Simplificar em cruz é dividir um número de cima [p=0.2] e um de baixo, [p=0.2] em diagonal, [p=0.2] pelo mesmo número. "
        "[p=0.4] {b}Quatro nonos vezes três oitavos. [p=0.4] {c}O quatro e o oito: [p=0.2] divide os dois por quatro, [p=0.2] "
        "vira um e dois. [p=0.4] {d}O três e o nove: [p=0.2] divide por três, [p=0.2] vira um e três. [p=0.4] {e}Sobra um terço "
        "vezes um meio: [p=0.2] *um sexto.*"),
    dict(id="15", block="mult", text=
        "{t}E sem cortar? [p=0.3] {a}Quatro vezes três, [p=0.2] doze. [p=0.2] Nove vezes oito, [p=0.2] setenta e dois. [p=0.4] "
        "{b}Doze setenta e dois avos, [p=0.2] que você ainda teria de simplificar. [p=0.4] {c}Dá o mesmo um sexto, [p=0.2] mas com "
        "números *muito* maiores. [p=0.3] {d}Corte antes, [p=0.2] multiplique depois."),

    # ================= BLOCO D: DIVISÃO =================
    dict(id="16", block="div", text=
        "{t}E a divisão? [p=0.3] Dividir é perguntar: [p=0.2] *quantas vezes uma cabe na outra?* [p=0.4] {a}Quantas metades de "
        "pizza cabem numa pizza inteira? [p=0.4] {b}Duas! [p=0.3] {c}Então, um dividido por um meio [p=0.2] dá *dois.* [p=0.3] "
        "{d}O resultado ficou *maior,* [p=0.2] e está certo."),
    dict(id="17", block="div", text=
        "{t}Mas por que inverter? [p=0.3] {a}Em uma pizza inteira, [p=0.2] cabem dois meios. [p=0.3] {b}Em três pizzas, "
        "[p=0.2] cabem seis. [p=0.4] {c}Dividir por um meio [p=0.2] é o mesmo que *multiplicar por dois.* [p=0.4] {d}E o dois "
        "é exatamente o um meio *de cabeça para baixo:* [p=0.2] dois sobre um. [p=0.4] {e}É por isso que a regra manda inverter."),
    dict(id="18", block="div", text=
        "{t}A regra é esta: [p=0.3] {a}*conserva* a primeira, [p=0.3] {b}*inverte* a segunda, [p=0.3] {c}e *multiplica.* [p=0.4] "
        "{d}Inverter é trocar o de cima com o de baixo: [p=0.2] o inverso de dois quintos [p=0.2] é cinco meios."),
    dict(id="19", block="div", text=
        "{t}Vamos usar. [p=0.3] Quantos copos de *dois quintos* de litro [p=0.2] cabem em *três quartos* de litro? [p=0.4] "
        "{a}Três quartos dividido por dois quintos. [p=0.3] {b}Conserva o três quartos, [p=0.2] inverte o dois quintos: [p=0.2] "
        "cinco meios. [p=0.4] {c}Três vezes cinco, [p=0.2] quinze. [p=0.2] Quatro vezes dois, [p=0.2] oito. [p=0.3] {d}*Quinze "
        "oitavos.* [p=0.4] {e}Quinze oitavos é um inteiro e sete oitavos: [p=0.2] quase *dois* copos. [p=0.3] Faz sentido!"),
    dict(id="20", block="div", text=
        "{t}E o atalho da divisão: [p=0.3] {a}*depois* de inverter, [p=0.2] você já está numa multiplicação. [p=0.4] {b}Então "
        "pode simplificar em cruz também. [p=0.4] {c}Só nunca corte *antes* de inverter."),

    # ================= BLOCO E: POTÊNCIA =================
    dict(id="21", block="potencia", text=
        "{t}E a potência de uma fração? [p=0.3] {a}Dois terços ao cubo. [p=0.4] {b}O expoente, [p=0.2] aquele numerozinho no alto, "
        "[p=0.2] vai *nos dois termos:* [p=0.2] em cima e embaixo. [p=0.4] {c}Dois ao cubo, [p=0.2] oito. [p=0.3] {d}Três ao cubo, "
        "[p=0.2] três vezes três vezes três, [p=0.2] vinte e sete. [p=0.4] {e}*Oito vinte e sete avos.*"),
    dict(id="22", block="potencia", text=
        "{t}E o atalho da potência: [p=0.3] {a}faça a conta de cima e a de baixo *separadas,* [p=0.2] cada uma com a sua "
        "tabuada. [p=0.4] {b}E confira: [p=0.2] fração menor que um, [p=0.2] elevada a uma potência, [p=0.2] fica *menor* "
        "ainda. [p=0.4] {c}Dois terços é mais da metade; [p=0.2] oito vinte e sete avos é menos de um terço. [p=0.4] "
        "{d}Cuidado com a pegadinha: [p=0.2] elevar só o de cima [p=0.2] dá oito terços, [p=0.2] que é maior que dois!"),

    # ================= NÓS FAZEMOS =================
    dict(id="23", block="exercicio", text=
        "{t}Sua vez. [p=0.3] Duas contas. [p=0.4] {a}Primeira: [p=0.2] *dois terços mais um quarto.* [p=0.4] {b}Segunda: [p=0.2] "
        "*cinco sextos dividido por um terço.* [p=0.4] {c}Pause o vídeo e calcule. [p=2.0]"),
    dict(id="24", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Dois terços mais um quarto: [p=0.2] o MMC de três e quatro é doze. [p=0.3] Dois terços vira "
        "oito doze avos. [p=0.2] Um quarto vira três doze avos. [p=0.3] {b}Oito mais três: [p=0.2] *onze doze avos.* [p=0.5] "
        "{c}Cinco sextos dividido por um terço: [p=0.2] conserva, [p=0.2] inverte: [p=0.2] cinco sextos vezes três. [p=0.4] "
        "{d}Quinze sextos, [p=0.2] que simplifica por três: [p=0.2] *cinco meios.* [p=0.4] {e}Faz sentido? [p=0.2] Cinco "
        "meios é dois e meio: [p=0.2] um terço cabe duas vezes e meia em cinco sextos."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="25", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] somar e subtrair: [p=0.2] mesmo denominador antes, [p=0.2] pelo "
        "MMC. [p=0.5] {b}Dois: [p=0.2] multiplicar: [p=0.2] corte em cruz antes, [p=0.2] multiplique depois. [p=0.5] {c}Três: "
        "[p=0.2] dividir: [p=0.2] conserva a primeira, [p=0.2] inverte a segunda."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="26", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] somar numerador com numerador [p=0.2] e denominador com "
        "denominador. [p=0.2] Um meio mais um terço, [p=0.2] dois quintos. [p=0.4] {b}Parece certo, [p=0.2] porque na "
        "multiplicação é exatamente assim. [p=0.4] {c}Mas na soma, [p=0.2] primeiro o mesmo tamanho de fatia: [p=0.2] o MMC."),
    dict(id="27", block="erros", text=
        "{a}Segundo: [p=0.2] na divisão, [p=0.2] inverter a *primeira* fração, [p=0.2] em vez da segunda. [p=0.4] {b}Parece "
        "certo, [p=0.2] porque você lembra que tem que inverter alguma coisa. [p=0.4] {c}Mas a primeira se *conserva.* [p=0.2] "
        "Quem inverte é a segunda."),
    dict(id="28", block="erros", text=
        "{a}Terceiro: [p=0.2] multiplicar sem simplificar, [p=0.2] e se perder em números enormes. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque a resposta até sai igual. [p=0.4] {c}Mas número grande é conta errada esperando para acontecer. "
        "[p=0.2] *Corte em cruz antes.*"),

    # ================= QUESTÃO 9 =================
    dict(id="29", block="questao", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.4] {a}Três turmas participaram de uma campanha de arrecadação. [p=0.3] "
        "{b}A turma A arrecadou um sexto da meta, [p=0.2] a turma B arrecadou um quarto [p=0.2] e a turma C, [p=0.2] um terço. "
        "[p=0.4] {c}Que fração da meta ainda falta arrecadar?"),
    dict(id="30", block="questao", text=
        "{a}A: [p=0.2] um sexto. [p=0.4] {b}B: [p=0.2] um quarto. [p=0.4] {c}C: [p=0.2] um terço. [p=0.4] {d}D: [p=0.2] três "
        "quartos. [p=0.4] {e}E: [p=0.2] um treze avos. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="31", block="questao", text=
        "{t}Vamos resolver. [p=0.3] {a}Primeiro, [p=0.2] quanto já foi arrecadado: [p=0.2] um sexto mais um quarto mais um terço. "
        "[p=0.4] {b}É a conta que a gente acabou de fazer: [p=0.2] MMC doze, [p=0.2] dois mais três mais quatro, [p=0.2] nove doze "
        "avos, [p=0.2] *três quartos.* [p=0.4] {c}Mas a pergunta é quanto *falta.* [p=0.3] {d}A meta inteira é um. [p=0.2] Um menos "
        "três quartos: [p=0.2] *um quarto.* [p=0.3] {e}Ou, pelo atalho: [p=0.2] a meta inteira são doze doze avos. [p=0.2] "
        "Doze menos nove, [p=0.2] três doze avos, [p=0.2] um quarto. [p=0.3] {ok}*Letra B!*"),
    dict(id="32", block="questao", text=
        "{t}E as outras? [p=0.3] {xd}A D é três quartos: [p=0.2] o que já foi *arrecadado,* [p=0.2] e não o que falta. [p=0.4] "
        "{xa}A A e a C [p=0.2] só repetem a fração de uma das turmas. [p=0.4] {xe}E repare no *treze* da E: [p=0.2] seis mais "
        "quatro mais três. [p=0.3] Ele vem de *somar os denominadores,* [p=0.2] a pista de quem somou termo a termo."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="33", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] somar e subtrair: [p=0.2] mesmo denominador antes, [p=0.2] "
        "pelo MMC. [p=0.5] {b}Dois: [p=0.2] multiplicar: [p=0.2] corte em cruz antes, [p=0.2] multiplique depois. [p=0.5] "
        "{c}Três: [p=0.2] dividir: [p=0.2] conserva a primeira, [p=0.2] inverte a segunda."),

    # ================= PONTE E CTA =================
    dict(id="34", block="ponte", text=
        "{a}Existe um tipo de questão de fração [p=0.2] que derruba quase todo mundo. [p=0.4] {b}E a culpa é de duas palavras: "
        "[p=0.3] *do restante.* [p=0.5] {c}Próximo episódio."),
    dict(id="35", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha caído no um meio mais um terço igual a dois quintos? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
