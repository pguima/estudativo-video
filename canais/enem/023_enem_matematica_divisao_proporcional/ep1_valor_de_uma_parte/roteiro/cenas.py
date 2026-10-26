# Roteiro — Divisão Proporcional, Episódio 1 de 5: O valor de uma parte (o procedimento único da divisão proporcional)
# Base: Estudos/Enem/estudos/01-matematica/08-divisao-proporcional.html — seções 02, 03, 04 e 10 (+ Questões 1, 9 e 6 da seção 12).
# O truque do k já foi apresentado na série de Razão (pacotinhos): aqui ele vira o procedimento principal.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora (a mesma da série de Razão): o total vira PACOTINHOS iguais; pesos 2, 3 e 4 = 9 pacotinhos;
#   o k é o valor de UM pacotinho. Toda conta termina com "a soma das partes dá o total?" (a balança de caixa).
# Exemplos (regra do PLANO): o bloco a) é a própria Questão 1 (R$ 3 600 em 2, 3, 4), por desenho do usuário ("eu faço").
#   Bloco e) herança por idades 15, 20 e 25 com OUTRO total (R$ 180 000 → k = 3 000 → 45, 60 e 75 mil; diferença 30 mil),
#   para a Questão 9 (R$ 240 000, "nós fazemos") não virar repetição e o aluno participar.
#   Bloco g) total pela parte com pesos 1, 2, 4 e a MAIOR parte R$ 1 200 → k = 300 → total R$ 2 100 (a Questão 6 usa 3, 5, 7
#   e a menor parte R$ 1 800, e fica como "você faz").
#   Bloco d) simplificar pelo MDC: R$ 5 000 em 12, 18 e 30 → MDC 6 → 2, 3, 5 → k = 500 → 1 000, 1 500 e 2 500.
# Nós fazemos (do prompt): R$ 1 500 em 1, 2 e 3 → k = 250 → 250, 500 e 750.
# QUESTÃO 1 (eu faço; texto do material na tela): k = 400 → maior parte 4 · 400 = 1 600 → D. E (1 800) = dividiu por 2 (material).
#   Explicações NOSSAS: A (800) = a MENOR parte (respondeu a parte errada); B (1 200) = dividiu pelo número de pessoas
#   (3 600 ÷ 3) — também é a parte do meio; C (1 440) = somou os pesos errado (10 em vez de 9: 360 · 4).
# QUESTÃO 9 (nós fazemos): k = 4 000; curto (25 − 15) · 4 000 = 40 000 → B; longo 100 000 − 60 000. Material: C e E são partes
#   individuais. NOSSAS: D (80 000) = a parte do meio; A (20 000) = diferença entre idades vizinhas (5 · 4 000).
# QUESTÃO 6 (você faz): menor peso 3 → 3k = 1 800 → k = 600 → total 15 · 600 = 9 000 → C. Conferência 1 800 + 3 000 + 4 200.
#   O material não explica as erradas; NOSSAS: A (5 400) = 1 800 · 3, tratou a parte como se fosse o k; E (12 600) = 1 800 · 7,
#   mesmo erro com o maior peso; B (7 200) = 600 · 12, somou só os outros pesos (5 + 7); D (10 800) não fecha na conferência.
# Frases-chave (meio e fim, idênticas): 1. Some os pesos, divida o total, multiplique cada peso. 2. O k é o valor de um pacotinho.
#   3. A soma das partes tem que dar o total.
# Atalhos (verde): "some, divida, multiplique" · "pesos grandes? divida todos pelo MDC antes" · "diferença = diferença dos pesos × k"
#   · "conhece uma parte? ela dá o k".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Divisão proporcional do zero: o valor de uma parte (o truque do k) | Divisão Proporcional Ep. 1"
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
        "{a}Lucro entre sócios, [p=0.2] {b}verba entre setores, [p=0.2] {c}herança, [p=0.2] {d}bônus: [p=0.4] todas essas "
        "questões se resolvem com o *mesmo procedimento,* [p=0.3] {e}e ele cabe em *uma linha.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai *repartir qualquer valor* em partes proporcionais [p=0.4] {b}e responder "
        "*exatamente a parte* que a questão pede."),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}O *truque do k,* [p=0.2] da série de Razão: [p=0.2] razão três para "
        "cinco são *pacotinhos:* [p=0.2] três para um, cinco para o outro. [p=0.4] {b}A soma dos de cima sobre a soma dos de "
        "baixo [p=0.2] mantém a mesma razão. [p=0.4] {c}E o *MDC,* [p=0.2] da série de Divisibilidade, [p=0.2] é o maior número "
        "que divide todos ao mesmo tempo."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Pense em três situações. [p=0.3] {a}Um prêmio repartido conforme a *pontuação* de cada um. [p=0.4] {b}Uma herança "
        "repartida conforme a *idade* dos herdeiros. [p=0.4] {c}Amigos que dividem a conta conforme o que *cada um consumiu.* "
        "[p=0.4] {d}Em nenhuma delas é justo dividir em partes iguais. [p=0.3] Quem tem mais, [p=0.2] leva mais."),
    dict(id="05", block="definicao", text=
        "{t}Isso tem nome: [p=0.2] {a}*divisão proporcional.* [p=0.2] É repartir um total [p=0.2] de acordo com números que "
        "dizem quanto cada um merece. [p=0.4] {b}Esses números se chamam *pesos.* [p=0.4] {c}Peso dois, peso três, peso quatro: "
        "[p=0.2] quem tem peso quatro leva o dobro de quem tem peso dois."),

    # ================= BLOCO A: O PROCEDIMENTO =================
    dict(id="06", block="passo", text=
        "{t}Vamos fazer juntos. [p=0.3] {a}*Três mil e seiscentos reais* em partes proporcionais a *dois, três e quatro.* "
        "[p=0.4] {b}Passo um: [p=0.2] *some os pesos.* [p=0.2] Dois mais três mais quatro: [p=0.2] *nove.* [p=0.4] {c}Por "
        "quê? [p=0.2] Porque o total vai virar *nove pacotinhos iguais.* [p=0.3] Um leva dois, [p=0.2] outro leva três, "
        "[p=0.2] outro leva quatro."),
    dict(id="07", block="passo", text=
        "{t}Passo dois: [p=0.2] {a}*divida o total pela soma.* [p=0.3] Três mil e seiscentos dividido por nove: [p=0.2] "
        "*quatrocentos.* [p=0.4] {b}Esse é o *k:* [p=0.2] o valor de *um* pacotinho. [p=0.4] {c}Cada pacotinho vale "
        "quatrocentos reais."),
    dict(id="08", block="passo", text=
        "{t}Passo três: [p=0.2] {a}*multiplique o k por cada peso.* [p=0.3] Dois vezes quatrocentos: [p=0.2] *oitocentos.* "
        "[p=0.3] {b}Três vezes quatrocentos: [p=0.2] *mil e duzentos.* [p=0.3] {c}Quatro vezes quatrocentos: [p=0.2] *mil e "
        "seiscentos.* [p=0.4] {d}E agora, a conferência: [p=0.2] *a soma das partes dá o total?* [p=0.3] Oitocentos mais mil e "
        "duzentos mais mil e seiscentos: [p=0.2] *três mil e seiscentos.* [p=0.2] {e}Fechou!"),
    dict(id="09", block="atalho", text=
        "{t}Esse é o procedimento inteiro, [p=0.2] e ele cabe em uma linha. [p=0.4] {a}*k igual ao total dividido pela soma dos "
        "pesos.* [p=0.4] {b}Atalho para guardar: [p=0.2] *some, divida, multiplique.* [p=0.3] {c}E no fim, [p=0.2] sempre, "
        "[p=0.2] *feche o caixa:* [p=0.2] some as partes."),

    # ================= BLOCO B: O K SIGNIFICA ALGO =================
    dict(id="10", block="significa", text=
        "{t}E o k não é um número solto. [p=0.3] {a}Ele é o valor de *um ponto de peso.* [p=0.4] {b}Se os pesos forem *dias "
        "trabalhados,* [p=0.2] o k é o valor de *um dia.* [p=0.4] {c}Se forem *pontos* num concurso, [p=0.2] o k é quanto "
        "vale *um ponto.* [p=0.4] {d}Pergunte sempre: [p=0.2] *um pacotinho de quê?*"),

    # ================= BLOCO C: POR QUE FUNCIONA =================
    dict(id="11", block="porque", text=
        "{t}Mas por que dividir pela *soma* funciona? [p=0.4] {a}Cada parte dividida pelo seu peso [p=0.2] dá o mesmo k: "
        "[p=0.2] oitocentos sobre dois, [p=0.2] mil e duzentos sobre três, [p=0.2] mil e seiscentos sobre quatro. [p=0.2] "
        "Sempre quatrocentos. [p=0.4] {b}E a propriedade da série de Razão diz: [p=0.2] juntando tudo, [p=0.2] o total sobre a "
        "soma dos pesos [p=0.2] *também dá k.* [p=0.4] {c}É por isso que a conta começa pela soma."),

    # ================= BLOCO D: EQUIVALENTES E MDC =================
    dict(id="12", block="equivalentes", text=
        "{t}Uma surpresa agradável. [p=0.3] {a}Repartir em *dois para três* [p=0.2] é a mesma coisa que repartir em *quatro "
        "para seis,* [p=0.2] ou em *vinte para trinta.* [p=0.4] {b}Os pacotinhos mudam de tamanho, [p=0.2] mas cada um "
        "continua levando a *mesma fração* do total. [p=0.4] {c}As partes finais são *idênticas.*"),
    dict(id="13", block="mdc", text=
        "{t}E isso vira um atalho. [p=0.3] {a}*Cinco mil reais* em partes proporcionais a *doze, dezoito e trinta.* [p=0.4] "
        "{b}Números grandes? [p=0.2] *Simplifique pelo MDC:* [p=0.2] divida todos pelo maior número que divide os três. "
        "[p=0.3] O MDC é *seis.* [p=0.2] Os pesos viram *dois, três e cinco.* [p=0.4] {c}Soma dez, [p=0.2] k igual a "
        "quinhentos: [p=0.2] *mil, mil e quinhentos, e dois mil e quinhentos.* [p=0.3] {d}A soma dá cinco mil. [p=0.2] Fechou."),

    # ================= BLOCO E: HERANÇA (DIRETA) =================
    dict(id="14", block="heranca", text=
        "{t}Agora uma herança. [p=0.3] {a}*Cento e oitenta mil reais* para três herdeiros, [p=0.2] proporcionalmente às "
        "idades: [p=0.2] *quinze, vinte e vinte e cinco anos.* [p=0.4] {b}Soma das idades: [p=0.2] sessenta. [p=0.2] Cento e "
        "oitenta mil dividido por sessenta: [p=0.2] *k igual a três mil.* [p=0.2] Três mil por ano de idade. [p=0.4] {c}Partes: "
        "[p=0.2] *quarenta e cinco mil,* [p=0.2] *sessenta mil* [p=0.2] e *setenta e cinco mil.* [p=0.4] {d}Divisão *direta:* "
        "[p=0.2] o mais velho, [p=0.2] com o maior peso, [p=0.2] leva a maior parte. [p=0.3] E a soma fecha nos cento e "
        "oitenta mil."),

    # ================= BLOCO F: A DIFERENÇA =================
    dict(id="15", block="diferenca", text=
        "{t}E se a questão pedir só a *diferença* entre a maior e a menor parte? [p=0.4] {a}Não precisa calcular as duas. "
        "[p=0.3] {b}A diferença dos pesos: [p=0.2] vinte e cinco menos quinze, [p=0.2] *dez pacotinhos.* [p=0.3] {c}Dez vezes o "
        "k, [p=0.2] dez vezes três mil: [p=0.2] *trinta mil.* [p=0.4] {d}Confira: [p=0.2] setenta e cinco mil menos quarenta e "
        "cinco mil, [p=0.2] trinta mil. [p=0.3] {e}Atalho: [p=0.2] *diferença das partes é a diferença dos pesos vezes o k.*"),

    # ================= BLOCO G: O TOTAL PELA PARTE =================
    dict(id="16", block="total", text=
        "{t}E quando a questão *não dá o total?* [p=0.4] {a}Pesos *um, dois e quatro,* [p=0.2] e a *maior* parte foi de *mil "
        "e duzentos reais.* [p=0.4] {b}A maior parte tem peso quatro: [p=0.2] quatro pacotinhos valem mil e duzentos. [p=0.2] "
        "Um pacotinho, [p=0.2] *k igual a trezentos.* [p=0.4] {c}O total tem sete pacotinhos: [p=0.2] sete vezes trezentos, "
        "[p=0.2] *dois mil e cem.* [p=0.4] {d}Confira: [p=0.2] trezentos, seiscentos e mil e duzentos [p=0.2] dão dois mil e "
        "cem. [p=0.3] {e}Atalho: [p=0.2] *conhece uma parte? Ela dá o k.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="17", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Divida *mil e quinhentos reais* em partes proporcionais a *um, dois e três.* [p=0.4] {b}*Pause "
        "o vídeo e calcule.* [p=2.0]"),
    dict(id="18", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Soma dos pesos: [p=0.2] *seis.* [p=0.3] {b}Mil e quinhentos dividido por seis: [p=0.2] "
        "*k igual a duzentos e cinquenta.* [p=0.4] {c}Partes: [p=0.2] *duzentos e cinquenta,* [p=0.2] *quinhentos* [p=0.2] e "
        "*setecentos e cinquenta.* [p=0.4] {d}Fechando o caixa: [p=0.2] a soma dá *mil e quinhentos.* [p=0.2] Certo!"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] some os pesos, [p=0.2] divida o total, [p=0.2] multiplique "
        "cada peso. [p=0.5] {b}Dois: [p=0.2] o k é o valor de um pacotinho. [p=0.5] {c}Três: [p=0.2] a soma das partes tem que "
        "dar o total."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] dividir o total pelo *número de pessoas.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque são três pessoas. [p=0.4] {c}Mas são *nove pacotinhos,* [p=0.2] não três. [p=0.3] "
        "Divida pela *soma dos pesos.*"),
    dict(id="21", block="erros", text=
        "{a}Segundo: [p=0.2] responder *uma parte* quando a questão pede a *diferença,* [p=0.2] ou o contrário. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque a conta estava perfeita. [p=0.4] {c}Mas a pergunta era outra. [p=0.3] *Sublinhe* o "
        "que foi pedido antes de calcular."),
    dict(id="22", block="erros", text=
        "{a}Terceiro: [p=0.2] *não simplificar* pesos grandes [p=0.2] e se perder na conta. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque os números do enunciado são aqueles. [p=0.4] {c}Mas dividir todos pelo MDC [p=0.2] dá exatamente as *mesmas "
        "partes,* [p=0.2] com contas muito mais leves."),

    # ================= QUESTÃO 1 (EU FAÇO) =================
    dict(id="23", block="q1", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.2] Eu faço essa. [p=0.4] {a}Um "
        "prêmio de *três mil e seiscentos reais* [p=0.2] será dividido entre três participantes [p=0.2] em partes diretamente "
        "proporcionais a *dois, três e quatro.* [p=0.3] {b}O participante que receber a *maior* quantia ficará com: [p=0.4] "
        "{qa}A: [p=0.2] oitocentos reais. [p=0.3] {qb}B: [p=0.2] mil e duzentos. [p=0.3] {qc}C: [p=0.2] mil quatrocentos e "
        "quarenta. [p=0.3] {qd}D: [p=0.2] mil e seiscentos. [p=0.3] {qe}E: [p=0.2] mil e oitocentos."),
    dict(id="24", block="q1", text=
        "{t}Primeiro, [p=0.2] {a}sublinhe o que foi pedido: [p=0.2] a *maior* quantia. [p=0.4] {b}Some os pesos: [p=0.2] "
        "nove. [p=0.2] Divida: [p=0.2] *k igual a quatrocentos.* [p=0.4] {c}A maior parte é do maior peso: [p=0.2] quatro "
        "vezes quatrocentos, [p=0.2] *mil e seiscentos.* [p=0.3] {ok}*Letra D!* [p=0.4] {d}E o caixa fecha: [p=0.2] "
        "oitocentos, mil e duzentos e mil e seiscentos [p=0.2] dão três mil e seiscentos."),
    dict(id="25", block="q1", text=
        "{t}E as outras? [p=0.3] {xa}A A é a *menor* parte: [p=0.2] conta certa, [p=0.2] pergunta errada. [p=0.4] {xb}A B "
        "dividiu pelo *número de pessoas:* [p=0.2] três mil e seiscentos dividido por três. [p=0.4] {xc}A C somou os pesos "
        "errado: [p=0.2] dez em vez de nove. [p=0.4] {xe}E a E dividiu o total *por dois.*"),

    # ================= QUESTÃO 9 (NÓS FAZEMOS) =================
    dict(id="26", block="q9", text=
        "{t}Essa a gente faz junto. [p=0.3] {a}Uma herança de *duzentos e quarenta mil reais* [p=0.2] foi dividida entre três "
        "herdeiros [p=0.2] em partes diretamente proporcionais às suas idades: [p=0.2] *quinze, vinte e vinte e cinco anos.* "
        "[p=0.3] {b}A *diferença* entre a maior e a menor parte recebida foi de: [p=0.4] {qa}A: [p=0.2] vinte mil. [p=0.3] "
        "{qb}B: [p=0.2] quarenta mil. [p=0.3] {qc}C: [p=0.2] sessenta mil. [p=0.3] {qd}D: [p=0.2] oitenta mil. [p=0.3] {qe}E: "
        "[p=0.2] cem mil. [p=0.4] {p}*Pause e me diga:* [p=0.2] qual é o k? [p=2.0]"),
    dict(id="27", block="q9", text=
        "{t}Se você achou *quatro mil,* [p=0.2] acertou: [p=0.2] {a}soma das idades sessenta, [p=0.2] duzentos e quarenta mil "
        "dividido por sessenta. [p=0.4] {b}Caminho curto: [p=0.2] diferença dos pesos, [p=0.2] vinte e cinco menos quinze, "
        "[p=0.2] dez. [p=0.2] Dez vezes quatro mil: [p=0.2] *quarenta mil.* [p=0.3] {ok}*Letra B!* [p=0.4] {c}Caminho longo, "
        "para conferir: [p=0.2] as partes são sessenta, oitenta e cem mil. [p=0.2] A soma fecha nos duzentos e quarenta mil, "
        "[p=0.2] {d}e cem menos sessenta [p=0.2] dá quarenta mil."),
    dict(id="28", block="q9", text=
        "{t}E as armadilhas? [p=0.3] {xc}A C e {xe}a E são as *partes* da menor e da maior: [p=0.2] quem calcula tudo certo "
        "[p=0.2] e responde a pergunta errada. [p=0.4] {xd}A D é a parte do meio. [p=0.4] {xa}E a A pegou a diferença entre "
        "idades *vizinhas,* [p=0.2] cinco anos, [p=0.2] e não entre a maior e a menor."),

    # ================= QUESTÃO 6 (VOCÊ FAZ) =================
    dict(id="29", block="q6", text=
        "{t}Agora é com você. [p=0.3] {a}Um valor foi dividido entre três pessoas [p=0.2] em partes diretamente proporcionais "
        "a *três, cinco e sete.* [p=0.3] {b}Sabendo que a *menor parte* foi de *mil e oitocentos reais,* [p=0.2] o valor "
        "*total* dividido foi de: [p=0.4] {qa}A: [p=0.2] cinco mil e quatrocentos. [p=0.3] {qb}B: [p=0.2] sete mil e duzentos. "
        "[p=0.3] {qc}C: [p=0.2] nove mil. [p=0.3] {qd}D: [p=0.2] dez mil e oitocentos. [p=0.3] {qe}E: [p=0.2] doze mil e "
        "seiscentos. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="30", block="q6", text=
        "{t}Vamos resolver. [p=0.3] {a}A menor parte é do menor peso, [p=0.2] o três. [p=0.2] Três pacotinhos valem mil e "
        "oitocentos: [p=0.2] *k igual a seiscentos.* [p=0.4] {b}O total tem três mais cinco mais sete, [p=0.2] quinze "
        "pacotinhos. [p=0.2] Quinze vezes seiscentos: [p=0.2] *nove mil.* [p=0.3] {ok}*Letra C!* [p=0.4] {c}Fechando o caixa: "
        "[p=0.2] mil e oitocentos, três mil e quatro mil e duzentos [p=0.2] somam nove mil."),
    dict(id="31", block="q6", text=
        "{t}E as outras? [p=0.3] {xa}A A multiplicou mil e oitocentos por três: [p=0.2] tratou a parte como se fosse o k. "
        "[p=0.4] {xe}A E fez o mesmo erro com o sete. [p=0.4] {xb}A B esqueceu o peso da menor parte: [p=0.2] seiscentos vezes "
        "doze. [p=0.4] {xd}E a D não fecha o caixa com nenhuma conta."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="32", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] some os pesos, [p=0.2] divida o total, [p=0.2] "
        "multiplique cada peso. [p=0.5] {b}Dois: [p=0.2] o k é o valor de um pacotinho. [p=0.5] {c}Três: [p=0.2] a soma das "
        "partes tem que dar o total."),

    # ================= PONTE E CTA =================
    dict(id="33", block="ponte", text=
        "{a}E quando quem tem o *menor* número deve receber *mais,* [p=0.2] como no bônus para quem faltou menos? [p=0.4] "
        "{b}Aí entra a *divisão inversa,* [p=0.2] e um erro que quase todo mundo comete. [p=0.4] {c}Próximo episódio."),
    dict(id="34", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quanto deu o k do exercício para você? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
