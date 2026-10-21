# Roteiro — Cartografia, Episódio 4: Curvas de nível, perfil topográfico e declividade (aula para iniciantes)
# Base: Estudos/Enem/estudos/04-geografia/01-cartografia.html — seção 08 + Questões 7 e 8 da seção 12
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: curvas de nível são os DEGRAUS de uma escada vistos de cima: todo degrau tem a mesma altura.
#   Degraus colados = escada íngreme; degraus espaçados = rampa suave.
# Frases-chave (meio e fim, idênticas):
#   1. Curva de nível liga pontos de mesma altitude.
#   2. Curvas próximas: terreno íngreme.
#   3. Declividade: desnível dividido pela distância, vezes cem, na mesma unidade.

TITULO = "Curvas de nível do zero: leia morros e vales no mapa — Cartografia, episódio 4"

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "Como saber se um terreno é *perigoso* para construir uma casa, [p=0.3] {a}olhando só para um papel plano? [p=0.5] "
        "{b}Sem subir o morro, [p=0.2] sem medir nada no local. [p=0.5] {c}Os técnicos da Defesa Civil fazem isso *todo dia.* "
        "[p=0.4] {d}E hoje você vai aprender como."),
    dict(id="02", block="promessa", text=
        "Até o fim desta aula, [p=0.2] {a}você vai conseguir ler o relevo num mapa, [p=0.3] {b}achar morros e vales, [p=0.3] "
        "{c}e calcular o quanto uma encosta é inclinada. [p=0.3] Encosta é o lado de um morro, a parte em rampa."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="altitude", text=
        "Antes, três coisinhas rápidas. [p=0.3] {a}Primeira: *altitude.* [p=0.3] É a altura de um lugar em relação ao *nível do mar.* "
        "[p=0.4] {b}A praia está perto de zero. [p=0.3] {c}Um morro de trezentos metros de altitude [p=0.2] fica trezentos metros acima do mar."),
    dict(id="04", block="escala", text=
        "{a}Segunda: a escala, do primeiro episódio. [p=0.3] Num mapa de um para cinquenta mil, [p=0.2] {b}um centímetro vale cinquenta mil centímetros. "
        "[p=0.4] {c}Corte cinco zeros: [p=0.2] meio quilômetro. [p=0.3] {d}Ou seja, *quinhentos metros.*"),
    dict(id="05", block="porcento", text=
        "{a}Terceira: porcentagem. [p=0.3] Vinte por cento quer dizer [p=0.2] *vinte em cada cem.* [p=0.4] "
        "{b}Uma rua com vinte por cento de inclinação [p=0.2] sobe vinte metros a cada cem metros andados para a frente."),

    # ================= BLOCO A: O QUE É CURVA DE NÍVEL =================
    dict(id="06", block="fatias", text=
        "{t}Agora, a pergunta: [p=0.2] como desenhar um morro numa folha plana? [p=0.4] {a}Imagine um morro de areia na praia. [p=0.4] "
        "{b}Agora fatie esse morro com cortes deitados, [p=0.2] todos com a *mesma* distância de altura: [p=0.2] cem metros, duzentos, trezentos. "
        "[p=0.4] {c}Cada corte deixa uma borda em volta do morro."),
    dict(id="07", block="fatias", text=
        "{d}Agora suba e olhe de cima, como um passarinho. [p=0.4] {e}As bordas viram anéis, um dentro do outro. [p=0.4] "
        "{f}Cada anel se chama *curva de nível:* [p=0.2] uma linha que liga pontos de *mesma altitude.* [p=0.4] "
        "Ela também tem um nome difícil: [p=0.2] *isoípsa.*"),
    dict(id="08", block="equidistancia", text=
        "{t}E a distância de altura entre uma curva e a próxima? [p=0.4] {a}Ela se chama *equidistância.* [p=0.3] {b}E é sempre a mesma no mapa inteiro: "
        "[p=0.2] se uma curva é cem e a outra é duzentos, [p=0.2] a equidistância é cem metros. [p=0.4] {c}A diferença de altura entre "
        "dois pontos se chama *desnível.*"),

    # ================= BLOCO B: PRÓXIMAS x ESPAÇADAS =================
    dict(id="09", block="escada", text=
        "{t}Mas como o mapa mostra se o morro é íngreme? [p=0.4] {a}Pense numa escada vista de cima. [p=0.3] Todo degrau tem a *mesma altura.* "
        "[p=0.4] {b}Se os degraus estão *colados,* [p=0.2] você sobe muito andando pouco: [p=0.2] a escada é *íngreme.* [p=0.4] "
        "{c}Se estão *espaçados,* [p=0.2] você anda muito para subir o mesmo tanto: [p=0.2] é uma rampa *suave.*"),
    dict(id="10", block="declive", text=
        "{t}As curvas de nível são os degraus. [p=0.4] {a}Curvas *próximas:* [p=0.2] o terreno sobe rápido. [p=0.2] *Declive forte.* "
        "[p=0.4] {b}Curvas *espaçadas:* [p=0.2] o terreno sobe devagar. [p=0.2] *Declive suave.* [p=0.4] {c}*Declive* é a inclinação do terreno, "
        "[p=0.2] o quanto ele sobe ou desce."),

    # ================= BLOCO C: MORRO x DEPRESSÃO =================
    dict(id="11", block="morro", text=
        "{t}E curvas fechadas, em anel, [p=0.2] são sempre um morro? [p=0.4] {a}Olhe os números. [p=0.3] Se eles *crescem* para dentro: "
        "[p=0.2] cem, duzentos, trezentos... [p=0.2] {b}é um *morro.* [p=0.4] {c}Se *diminuem* para dentro, [p=0.2] {d}é um buraco: "
        "[p=0.2] uma *depressão.*"),

    # ================= BLOCO D: VALE =================
    dict(id="12", block="vale", text=
        "{t}E onde passa um rio? [p=0.4] {a}Num vale, [p=0.2] que é a parte baixa entre dois morros. [p=0.4] {b}No mapa, o vale aparece "
        "como curvas em formato de *V.* [p=0.4] {c}E a ponta do V aponta para os números *maiores,* [p=0.2] morro acima. [p=0.4] "
        "{d}O rio corre no meio do V, [p=0.2] descendo."),
    dict(id="13", block="vale", text=
        "{e}E o rio tem duas pontas com nome. [p=0.3] *Montante* é para onde fica a nascente, [p=0.2] rio acima. [p=0.4] "
        "{f}*Jusante* é para onde ele corre, [p=0.2] rio abaixo."),

    # ================= BLOCO E: NUNCA SE CRUZAM =================
    dict(id="14", block="cruzam", text=
        "{t}E duas curvas de nível podem se cruzar? [p=0.4] {a}Se cruzassem, [p=0.2] o ponto do cruzamento estaria em duas curvas ao mesmo tempo. "
        "[p=0.4] {b}Teria cem metros *e* duzentos metros de altitude. [p=0.4] {c}Impossível. [p=0.3] {d}Num paredão de pedra, em pé, "
        "elas podem até *encostar.* [p=0.3] Cruzar, *nunca.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="15", block="recap", text=
        "{t}Vamos juntar tudo em três frases. [p=0.5] {a}Um: [p=0.2] curva de nível liga pontos de mesma altitude. [p=0.5] "
        "{b}Dois: [p=0.2] curvas próximas: terreno íngreme. [p=0.5] {c}Três: [p=0.2] declividade: desnível dividido pela distância, "
        "vezes cem, na mesma unidade. [p=0.4] Essa terceira vem agora."),

    # ================= BLOCO F: PERFIL TOPOGRÁFICO =================
    dict(id="16", block="perfil", text=
        "{t}E como ver o morro de *lado,* a partir do mapa? [p=0.4] {a}Imagine cortar o morro com uma faca, [p=0.2] do ponto A ao ponto B, "
        "[p=0.2] e olhar o corte. [p=0.4] {b}No mapa, você traça uma linha de A até B. [p=0.4] {c}Em cada lugar em que a linha cruza uma curva, "
        "[p=0.2] você marca a altura dessa curva."),
    dict(id="17", block="perfil", text=
        "{d}Ligando os pontos, aparece o desenho do morro visto de lado. [p=0.4] {e}Esse desenho se chama *perfil topográfico.* [p=0.4] "
        "{f}E repare: [p=0.2] onde as curvas estavam coladas, [p=0.2] o perfil fica *em pé.* [p=0.3] Onde estavam espaçadas, [p=0.2] fica *deitado.*"),

    # ================= BLOCO G: DECLIVIDADE =================
    dict(id="18", block="declividade", text=
        "{t}E dá para medir a inclinação com um número? [p=0.4] {a}Dá: [p=0.2] é a *declividade.* [p=0.3] {b}Você divide o desnível [p=0.2] "
        "pela distância andada na horizontal, [p=0.2] {c}e multiplica por cem, [p=0.2] para virar porcentagem. [p=0.4] "
        "{d}E um cuidado de ouro: [p=0.2] as duas medidas precisam estar na *mesma unidade.* [p=0.3] Metro com metro."),
    dict(id="19", block="conta", text=
        "{t}Vamos fazer uma. [p=0.3] {a}Num mapa de um para cinquenta mil, [p=0.2] dois pontos estão a quatro centímetros. [p=0.4] "
        "{b}Cada centímetro vale quinhentos metros, [p=0.2] então quatro centímetros são *dois mil metros.* [p=0.4] {c}Um ponto está na curva de duzentos metros, "
        "[p=0.2] o outro na de seiscentos. [p=0.3] {d}O desnível é seiscentos *menos* duzentos: [p=0.2] *quatrocentos metros.*"),
    dict(id="20", block="conta", text=
        "{e}Agora, metro com metro: [p=0.2] quatrocentos dividido por dois mil [p=0.2] dá zero vírgula dois. [p=0.4] {f}Vezes cem: [p=0.2] "
        "*vinte por cento.* [p=0.4] {g}Igual àquela rua: [p=0.2] sobe vinte metros a cada cem andados."),

    # ================= BLOCO H: POR QUE IMPORTA =================
    dict(id="21", block="risco", text=
        "{t}E por que isso importa fora da prova? [p=0.4] {a}Encostas muito íngremes, ocupadas por casas, [p=0.2] são áreas de risco de *deslizamento,* "
        "[p=0.2] principalmente com chuva forte. [p=0.4] {b}Por isso, uma lei federal, [p=0.2] a Lei seis mil, setecentos e sessenta e seis, "
        "de mil novecentos e setenta e nove, [p=0.3] {c}proíbe lotear terrenos com declividade de *trinta por cento ou mais,* "
        "[p=0.2] salvo exigências específicas. [p=0.4] {d}É exatamente essa conta que a Defesa Civil faz."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erro1", text=
        "{t}Agora, os quatro erros que mais derrubam gente. [p=0.4] {a}Primeiro: [p=0.2] ler curvas próximas como terreno plano. [p=0.4] "
        "{b}Parece certo, porque linhas juntinhas parecem um lugar \"tranquilo\". [p=0.4] {c}Mas lembre da escada: [p=0.2] degraus colados "
        "[p=0.2] são escada *íngreme.*"),
    dict(id="23", block="erro2", text=
        "{a}Segundo: [p=0.2] usar a altitude do ponto mais alto, seiscentos, [p=0.2] em vez do desnível. [p=0.4] {b}Parece certo, "
        "porque seiscentos é o número que aparece no mapa. [p=0.4] {c}Mas a inclinação depende de quanto você *subiu:* [p=0.2] "
        "seiscentos menos duzentos, [p=0.2] quatrocentos."),
    dict(id="24", block="erro3", text=
        "{a}Terceiro: [p=0.2] dividir metros por centímetros. [p=0.4] {b}Parece certo, porque os dois números já estão ali, prontos. [p=0.4] "
        "{c}Mas quatrocentos *metros* dividido por quatro *centímetros* não faz sentido. [p=0.3] {d}Converta antes: [p=0.2] metro com metro."),
    dict(id="25", block="erro4", text=
        "{a}Quarto: [p=0.2] achar que curvas de nível podem se cruzar. [p=0.4] {b}Parece certo, porque no desenho são só linhas. [p=0.4] "
        "{c}Mas cada linha é uma altitude. [p=0.3] Um ponto não pode ter duas."),

    # ================= QUESTÃO 7 =================
    dict(id="26", block="q7", text=
        "{t}Hora de treinar, no estilo do ENEM. [p=0.4] {e1}O esquema mostra as curvas de nível de um morro, [p=0.2] de cem em cem metros, até o cume. "
        "[p=0.4] {e2}A trilha um sobe pelo lado oeste, [p=0.2] onde as curvas estão muito próximas. [p=0.3] {e3}A trilha dois sobe pelo leste, "
        "[p=0.2] onde estão espaçadas. [p=0.3] As duas saem da curva de cem metros e chegam ao cume."),
    dict(id="27", block="q7", text=
        "{t}As alternativas. [p=0.3] {a}A: [p=0.2] a trilha dois é a mais íngreme, pois cruza curvas mais largas. [p=0.4] {b}B: [p=0.2] as duas têm "
        "a mesma inclinação, pois vencem o mesmo desnível. [p=0.4] {c}C: [p=0.2] a trilha dois vence um desnível maior, pois o caminho é mais longo. "
        "[p=0.4] {d}D: [p=0.2] o lado oeste é o mais suave, pois as curvas estão próximas. [p=0.4] {e}E: [p=0.2] a trilha um é a mais íngreme, "
        "pois vence o mesmo desnível numa distância bem menor. [p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="28", block="q7", text=
        "{t}Vamos eliminar. [p=0.3] {a}A inverte a regra: [p=0.2] curvas largas são terreno suave. [p=0.2] Fora. [p=0.3] {b}B esquece que a inclinação "
        "depende também da distância. [p=0.2] Fora. [p=0.3] {c}C confunde caminho com desnível: [p=0.2] as duas sobem de cem até o cume. [p=0.2] Fora. "
        "[p=0.3] {d}D inverte de novo: [p=0.2] curvas próximas são íngremes. [p=0.2] Fora. [p=0.4] {e}Resposta: [p=0.2] *letra E.*"),

    # ================= QUESTÃO 8 =================
    dict(id="29", block="q8", text=
        "{t}Agora, a segunda. [p=0.3] {e1}Numa carta de um para cinquenta mil, [p=0.2] {e2}dois pontos de uma encosta, nas curvas de duzentos e de seiscentos metros, "
        "[p=0.2] {e3}estão a quatro centímetros. [p=0.3] Qual é a declividade?"),
    dict(id="30", block="q8", text=
        "{t}As alternativas: [p=0.3] {a}A: zero vírgula dois por cento. [p=0.2] {b}B: dois por cento. [p=0.2] {c}C: vinte por cento. "
        "[p=0.2] {d}D: trinta por cento. [p=0.2] {e}E: duzentos por cento. [p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="31", block="q8", text=
        "{t}É a nossa conta: [p=0.2] dois mil metros na horizontal, [p=0.2] quatrocentos de desnível, [p=0.2] vinte por cento. [p=0.4] "
        "{a}A dividiu metros por centímetros. [p=0.2] Fora. [p=0.3] {b}B errou a conversão, [p=0.2] usou vinte mil metros. [p=0.2] Fora. "
        "[p=0.3] {d}D usou seiscentos em vez do desnível. [p=0.2] Fora. [p=0.3] {e}E usou só duzentos metros de distância. [p=0.2] Fora. "
        "[p=0.4] {c}Resposta: [p=0.2] *letra C.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="32", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] curva de nível liga pontos de mesma altitude. [p=0.5] "
        "{b}Dois: [p=0.2] curvas próximas: terreno íngreme. [p=0.5] {c}Três: [p=0.2] declividade: desnível dividido pela distância, "
        "vezes cem, na mesma unidade."),

    # ================= PONTE =================
    dict(id="33", block="ponte", text=
        "{t}E se o tamanho de um país no mapa [p=0.2] não fosse o território, [p=0.3] {a}mas a quantidade de gente que mora lá? [p=0.5] "
        "{b}Próximo episódio: [p=0.2] *mapas temáticos e anamorfoses.*"),
    dict(id="34", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para não perder os próximos episódios. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] a rua da sua casa tem mais ou menos de trinta por cento? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
