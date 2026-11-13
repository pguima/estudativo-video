# Estudativo · QUI-INO-002 — Bases: dissociação, nomes e força (Química · Funções e Reações Inorgânicas · Ácidos, bases, sais e óxidos).
# Habilidade: escrever a dissociação de NaOH e de Ca(OH)₂, dar nome à base e dizer pela família do metal se ela é forte.
# Pré-requisitos: QUI-LIG-001, QUI-INO-007. Próxima: QUI-INO-003 (neutralização e sais).
# Atenção: QUI-INO-001 (ácidos) NÃO está em "Já ensinado" desta aula: a aula não usa ácido nem H⁺.
# Fórmulas narradas: NaOH = "ene á ó agá", KOH = "cá ó agá", OH⁻ = "ó agá menos", Na⁺ = "ene á mais", Ca²⁺ = "cê á dois mais".
# Fórmula com parênteses NÃO é lida letra a letra (a voz embaralharia): diz-se o nome e a fórmula fica na tela.
# Parênteses são ensinados aqui (QUI-MIS-001 deixou para outra aula): o índice fora vale para o grupo inteiro.
# Fatos: NaOH = soda cáustica (desentupidor: dissolve gordura e cabelo). Bases de metais alcalinos (família 1) e
# alcalinoterrosos (família 2) são fortes, exceto Mg(OH)₂ e Be(OH)₂. Mg(OH)₂ = leite de magnésia, antiácido, fraca e pouco
# solúvel. Al³⁺ (família 13) forma Al(OH)₃. Ferro tem cargas 2+ e 3+: hidróxido de ferro II e de ferro III.
# Questão inédita: Ba(OH)₂ → Ba²⁺ + 2 OH⁻, forte (bário, família 2).

TITULO = "Bases: dissociação, nomes e força"

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
    dict(id="s01", block="gancho", text="{a}A soda cáustica desentope a pia porque {b}dissolve gordura e cabelo. [p=0.3] Na água, ela solta {c}um íon feito de um oxigênio e um hidrogênio, presos. [p=0.3] {d}É esse íon que faz da soda uma base."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}escrever o que acontece com uma base na água, [p=0.2] {b}dar nome a ela [p=0.2] e {c}dizer, só pela família do metal, se ela é forte."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre da ligação iônica. [p=0.2] {a}O sódio, da família um, perde um elétron e vira ene á mais. [p=0.2] {b}O cálcio, da família dois, perde dois e vira cê á dois mais. [p=0.3] {c}Num composto iônico, os íons já existem, presos uns aos outros."),
    # hidróxido
    dict(id="s04", block="hidroxido", text="Agora, um íon diferente. [p=0.2] {a}Um oxigênio preso a um hidrogênio, [p=0.1] {b}com um elétron a mais. [p=0.3] É o {c}ó agá menos, o hidróxido. [p=0.3] {d}Ele é um íon de dois átomos, que andam sempre juntos."),
    dict(id="s05", block="hidroxido", text="A soda cáustica é o {a}ene á ó agá: [p=0.1] {b}o íon ene á mais preso ao íon ó agá menos. [p=0.3] {c}Na água, esses íons, que já existiam, só se separam: [p=0.2] {d}ene á ó agá produz ene á mais {e}e ó agá menos."),
    dict(id="s06", block="hidroxido", text="Separar íons que já estavam lá se chama {a}dissociação. [p=0.3] E daí vem a definição do químico Arrhenius: [p=0.2] {b}base é a substância que, na água, solta ó agá menos como único íon negativo. [p=0.3] Por isso, {c}na fórmula dessas bases, o ó agá vem no fim, depois do metal."),
    # nomes
    dict(id="s07", block="nomes", text="O nome é fácil: {a}hidróxido de, e o nome do metal. [p=0.2] {b}Ene á ó agá é o hidróxido de sódio. [p=0.2] {c}Cá ó agá, o hidróxido de potássio. [p=0.3] {d}Se o metal tem mais de uma carga, como o ferro, ela vem em algarismo romano: [p=0.1] hidróxido de ferro dois, ou hidróxido de ferro três."),
    # parênteses
    dict(id="s08", block="parenteses", text="E quando a carga do metal é dois mais? [p=0.2] {a}O cálcio, cê á dois mais, precisa de dois ó agá menos para as cargas somarem zero. [p=0.3] {b}A fórmula do hidróxido de cálcio põe o ó agá entre parênteses, com o dois do lado de fora."),
    dict(id="s09", block="parenteses", text="{a}O índice fora dos parênteses vale para o grupo inteiro: [p=0.2] {b}dois oxigênios e dois hidrogênios, [p=0.1] {c}e um cálcio. [p=0.3] Na água, o hidróxido de cálcio {d}produz um íon cê á dois mais {e}e dois íons ó agá menos."),
    # força
    dict(id="s10", block="forca", text="E a força? [p=0.2] {a}Base forte é a que se dissocia quase toda e solta muito ó agá menos. [p=0.3] A regra vem da tabela periódica. [p=0.2] {b}Metal da família um, a dos alcalinos, como sódio e potássio: [p=0.1] base forte. [p=0.2] {c}Da família dois, a dos alcalinoterrosos, como cálcio e bário: [p=0.1] forte também. [p=0.3] {d}Os outros metais formam bases fracas."),
    dict(id="s11", block="forca", text="Mas guarde uma exceção. [p=0.2] {a}O magnésio é da família dois, [p=0.1] e mesmo assim {b}o hidróxido de magnésio é fraco, e quase não se dissolve. [p=0.3] {c}É o leite de magnésia, que se toma contra a azia. [p=0.2] {d}Uma base forte, como a soda, feriria a boca. [p=0.2] O berílio, bem raro, também é exceção."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}desmontar o hidróxido. [p=0.2] A pessoa escreve que o ene á ó agá solta {b}ene á mais, [p=0.1] um ó negativo {c}e um agá mais. [p=0.3] {d}Errado: o ó agá não se parte na dissociação. [p=0.2] {e}Ele sai inteiro, como um íon só, com uma carga negativa."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho de prova: [p=0.2] {a}o número de ó agá é a carga do metal. [p=0.3] E a carga sai da família: [p=0.2] {b}família um, uma carga, um ó agá. [p=0.2] {c}Família dois, duas cargas, dois ó agá. [p=0.3] {d}O alumínio, da família treze, perde três elétrons e vira á éle três mais: [p=0.1] o hidróxido de alumínio tem três ó agá."),
    dict(id="s14", block="atalho", text="Funciona porque {a}cada ó agá menos cancela uma carga positiva do metal. [p=0.3] {b}Não compensa com metal de carga variável, como o ferro: [p=0.1] {c}aí, a carga vem escrita no nome, em algarismo romano."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}O hidróxido de bário, que está na tela, é usado em laboratório. [p=0.2] {b}O bário é da família dois. [p=0.3] {c}Escreva o que ele produz na água. [p=0.2] E {d}diga se ele é uma base forte ou fraca."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Família dois, carga dois mais: [p=0.1] {b}o íon é bê á dois mais. [p=0.2] {c}O dois fora dos parênteses diz que são dois hidróxidos: [p=0.1] {d}dois íons ó agá menos. [p=0.3] {e}E o bário não é magnésio nem berílio: [p=0.1] {f}base forte."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}base solta ó agá menos na água, [p=0.1] {b}o nome é hidróxido de, e o metal, [p=0.1] e {c}famílias um e dois dão bases fortes, menos magnésio e berílio."),
    dict(id="s19", block="fim", text="Na próxima aula, um ácido encontra uma base: [p=0.2] {a}o agá mais e o ó agá menos viram água, [p=0.2] {b}e o que sobra é um sal. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
