# Estudativo · QUI-ORG-010 — Haletos e outras funções (Química · Química Orgânica · Funções orgânicas).
# Habilidade: reconhecer haleto, nitrocomposto e tiol e explicar por que o CFC ataca a camada de ozônio e o DDT se acumula no ambiente.
# Pré-requisitos: QUI-ORG-009 (amina). Próxima: QUI-ORG-011 (prática: aspirina, adrenalina, penicilina).
# Marcas: {cue} animação · [p=0.2] pausa. Siglas faladas: CFC = "cê éfe cê", DDT = "dê dê tê", TNT = "tê ene tê"; NO₂ = "ene ó dois"; SH = "esse agá".
# Fatos: halogênios = família do F, Cl, Br, I (QUI-ATO-009), uma ligação cada; CH3Cl = clorometano; CFC inerte, usado em geladeiras e
# sprays; UV quebra C–Cl, o Cl destrói O3 e se regenera (um Cl destrói milhares de O3); Protocolo de Montreal, 1987.
# DDT C14H9Cl5: 5 cloros, dois anéis; pouco solúvel em água, solúvel em gordura (o porquê fica para outra aula), pouco degradado:
# bioacumula e aumenta ao longo da cadeia alimentar. TNT = trinitrotolueno. Tiol: etanotiol (odorizante do gás de cozinha).
# Questão: CCl2F2 (haleto, CFC-12), CH3NO2 nitrometano (combustível de aeromodelo), CH3CH2SH etanotiol. Questão inédita.

TITULO = "Haletos e outras funções"

VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que passou anos sem estudar: voz masculina, grave, calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína; mostre "
            "surpresa no erro, entusiasmo no atalho e dê ênfase forte às palavras-chave. Ritmo tranquilo, com pausas "
            "naturais entre as ideias. Leia exatamente o texto, sem repetir nem acrescentar nada."),
)

SCENES = [
    # gancho
    dict(id="s01", block="gancho", text="{a}Um gás de geladeira antiga ajudou a abrir um buraco na camada de ozônio. [p=0.3] {b}E um inseticida proibido há muitos anos ainda aparece na gordura de animais. [p=0.2] {c}Os dois têm cloro preso a carbono."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai reconhecer {b}haleto, nitrocomposto e tiol, [p=0.2] e explicar {c}o estrago do cê éfe cê [p=0.1] e {d}o acúmulo do dê dê tê."),
    # lembrete
    dict(id="s03", block="lembrete", text="Das últimas aulas: [p=0.2] {a}cada função muda o grupo preso à cadeia. [p=0.2] {b}No álcool, é o ó agá, com nome em ol. [p=0.2] {c}Na amina, é o nitrogênio só com ligações simples, sem carbonila ao lado."),
    # haleto
    dict(id="s04", block="haleto", text="{a}Os halogênios são a família do flúor, do cloro, do bromo e do iodo. [p=0.2] {b}Cada um faz uma ligação, como o hidrogênio. [p=0.3] {c}Troque um agá da cadeia por um halogênio: [p=0.1] {d}é um haleto orgânico. [p=0.2] {e}O nome traz o halogênio na frente, como um prefixo: [p=0.1] {f}clorometano."),
    # CFC
    dict(id="s05", block="cfc", text="{a}O cê éfe cê é um clorofluorcarbono: [p=0.1] carbono preso só a cloro e flúor. [p=0.2] {b}Ele não pega fogo e quase não reage, [p=0.1] {c}por isso foi muito usado em geladeiras e sprays."),
    dict(id="s06", block="cfc", text="{a}Justamente por quase não reagir, ele dura décadas no ar e sobe até a camada de ozônio, [p=0.1] {b}o escudo que filtra a luz ultravioleta do Sol. [p=0.3] {c}Lá em cima, a luz ultravioleta quebra a ligação entre o carbono e o cloro [p=0.1] {d}e solta um átomo de cloro."),
    dict(id="s07", block="cfc", text="{a}Esse cloro destrói uma molécula de ozônio [p=0.1] {b}e sai livre de novo, para destruir outra. [p=0.3] {c}Um só átomo de cloro desfaz milhares de moléculas de ozônio. [p=0.3] {d}Por isso, desde o Protocolo de Montreal, um acordo entre países de mil novecentos e oitenta e sete, [p=0.1] o cê éfe cê foi sendo proibido no mundo todo."),
    # DDT
    dict(id="s08", block="ddt", text="{a}O dê dê tê é um inseticida com cinco cloros, [p=0.1] {b}presos a dois anéis e a um carbono. [p=0.3] {c}Ele quase não se dissolve na água, mas se dissolve na gordura. [p=0.2] Por que, é assunto de outra aula. [p=0.2] {d}E o corpo dos animais quase não consegue desmontar essa molécula."),
    dict(id="s09", block="ddt", text="{a}Então, cada animal guarda o dê dê tê que comeu. [p=0.2] {b}O peixe pequeno tem um pouco. [p=0.1] {c}O peixe grande come muitos pequenos, [p=0.1] {d}e a ave come muitos peixes grandes. [p=0.3] {e}A cada passo da cadeia alimentar, a dose fica maior."),
    # nitro e tiol
    dict(id="s10", block="outras", text="{a}Mais duas funções. [p=0.2] {b}O nitrocomposto tem o grupo ene ó dois preso a um carbono. [p=0.2] {c}Três desses grupos no tolueno, o benzeno com um cê agá três, [p=0.1] formam o tê ene tê, um explosivo."),
    dict(id="s11", block="outras", text="{a}E o tiol é o álcool com enxofre no lugar do oxigênio: [p=0.1] {b}o grupo esse agá. [p=0.2] O nome é o do hidrocarboneto mais tiol: [p=0.1] {c}etano mais tiol, etanotiol. [p=0.3] {d}Os tióis têm cheiro forte, [p=0.1] {e}e um deles vai no gás de cozinha, para você perceber um vazamento."),
    # erro comum
    dict(id="s12", block="erro", text="{a}De novo, o erro de chamar todo nitrogênio de amina. [p=0.3] {b}No nitrocomposto, o nitrogênio está preso a dois oxigênios [p=0.1] e não tem agá. [p=0.3] {c}Na amina, o nitrogênio só tem carbono e hidrogênio em volta, e nenhuma carbonila ao lado. [p=0.2] {d}Com ene ó dois, é nitrocomposto."),
    # atalho
    dict(id="s13", block="atalho", text="{a}O atalho do enxofre: [p=0.1] {b}ele é da mesma família do oxigênio [p=0.1] e faz as mesmas duas ligações. [p=0.3] {c}Troque o ó por esse, e a função ganha tio: [p=0.1] {d}o álcool vira tiol, [p=0.1] {e}e o éter vira tioéter."),
    dict(id="s14", block="atalho", text="{a}Funciona porque o enxofre ocupa na molécula o mesmo lugar do oxigênio. [p=0.3] {b}Só não espere as mesmas propriedades: [p=0.1] {c}o etanol tem cheiro suave, e o etanotiol fede."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Diga a função de cada molécula. [p=0.2] {b}A primeira foi usada em geladeiras antigas. [p=0.2] {c}A segunda é combustível de aeromodelo. [p=0.2] {d}E a terceira tem cheiro de gás."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="{a}A primeira tem cloro e flúor presos ao carbono: [p=0.1] haleto, um cê éfe cê. [p=0.3] {b}A segunda tem ene ó dois preso ao carbono: [p=0.1] nitrocomposto, o nitrometano. [p=0.3] {c}A terceira tem esse agá: [p=0.1] tiol, o etanotiol."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}halogênio preso a carbono é haleto; [p=0.1] {b}ene ó dois, nitrocomposto; [p=0.1] {c}esse agá, tiol. [p=0.3] {d}O cê éfe cê solta cloro, que destrói o ozônio, [p=0.1] e {e}o dê dê tê se acumula na gordura, de bicho em bicho."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai juntar tudo [p=0.1] e {a}marcar as funções de moléculas reais, [p=0.1] como {b}a aspirina, {c}a adrenalina [p=0.1] e {d}a penicilina. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
