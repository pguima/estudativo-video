# Estudativo · FIS-CAL-010 — Convecção e irradiação (Física · Calor e Termodinâmica · Propagação de calor).
# Habilidade: dizer qual processo age na geladeira, nas brisas, na garrafa térmica e no efeito estufa.
# Pré-requisitos: FIS-CAL-009 (condução), FIS-EGF-008 (flutuar ou afundar: densidade). Próxima: FIS-CAL-011.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fora de "Já ensinado": dilatação (FIS-CAL-002) e ondas eletromagnéticas. A expansão do ar é dita como fato, na hora
# ("as partículas se afastam"); o infravermelho é apresentado como "luz que o olho não vê", sem a teoria das ondas.

TITULO = "Convecção e irradiação"

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
    dict(id="s01", block="gancho", text="{a}Por que o ar-condicionado fica no alto da parede? [p=0.3] E {b}como o calor do Sol chega até aqui, [p=0.2] se no caminho {c}não tem nem ar?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai dizer qual processo leva o calor {b}na geladeira, [p=0.2] {c}nas brisas, [p=0.2] {d}na garrafa térmica [p=0.2] e {e}no efeito estufa."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a condução, em que o calor passa de partícula em partícula, sem a matéria sair do lugar; [p=0.2] e {c}a densidade: o que é menos denso sobe, e o que é mais denso afunda. [p=0.3] Se faltar alguma, procure no canal."),
    # convecção
    dict(id="s04", block="conveccao", text="Pense num {a}aquecedor no chão de um quarto frio. [p=0.2] {b}O ar perto dele esquenta. [p=0.2] As partículas se agitam mais e se afastam: [p=0.2] {c}o mesmo ar passa a ocupar mais espaço. [p=0.3] Mesma massa em mais espaço é {d}densidade menor."),
    dict(id="s05", block="conveccao", text="Então {a}o ar quente sobe, [p=0.2] como uma rolha na água. [p=0.2] {b}O ar frio, mais denso, desce e ocupa o lugar. [p=0.2] Lá embaixo, {c}ele esquenta e sobe também. [p=0.3] Forma uma roda de ar girando: {d}a corrente de convecção."),
    dict(id="s06", block="conveccao", text="Na convecção, {a}a própria matéria anda e leva o calor junto. [p=0.3] Por isso, {b}ela só acontece em líquidos e gases, os fluidos. [p=0.2] {c}Num sólido, as partículas estão presas no lugar."),
    dict(id="s07", block="conveccao", text="{a}Daí, o ar-condicionado no alto: [p=0.2] o ar gelado desce sozinho e esfria a sala toda. [p=0.3] {b}E o congelador da geladeira, no alto: [p=0.2] o ar frio desce pelas prateleiras, [p=0.2] e {c}o ar mais quente sobe até o congelador para esfriar. [p=0.3] {d}As prateleiras são grades para esse ar passar."),
    # brisas
    dict(id="s08", block="brisas", text="As brisas do litoral são convecção em tamanho grande. [p=0.3] {a}Durante o dia, a areia esquenta mais rápido que o mar, [p=0.2] porque a água precisa de muito calor para mudar de temperatura. [p=0.3] {b}O ar sobre a areia esquenta e sobe. [p=0.2] {c}O ar mais frio do mar vem ocupar o lugar: [p=0.2] é {d}a brisa marítima, do mar para a terra."),
    dict(id="s09", block="brisas", text="{a}À noite, tudo se inverte. [p=0.2] {b}A areia esfria mais rápido, e o mar fica mais quente. [p=0.2] {c}O ar sobe sobre o mar, [p=0.2] e {d}a brisa terrestre sopra da terra para o mar."),
    # irradiação
    dict(id="s10", block="irradiacao", text="E o Sol? [p=0.2] Entre o Sol e a Terra existe {a}o vácuo: [p=0.2] espaço sem matéria nenhuma. [p=0.2] {b}Sem matéria, não há condução nem convecção. [p=0.3] O calor chega {c}por irradiação: [p=0.2] ele viaja como a luz, [p=0.2] {d}sem precisar de matéria."),
    dict(id="s11", block="irradiacao", text="{a}Todo corpo irradia, [p=0.2] e {b}quanto mais quente, mais irradia. [p=0.3] Os corpos na temperatura do dia a dia irradiam {c}infravermelho, [p=0.2] uma luz que o olho não vê. [p=0.2] As ondas de luz são assunto de outra aula. [p=0.3] {d}Superfície escura absorve mais essa energia. [p=0.2] {e}Superfície clara ou espelhada reflete mais."),
    # garrafa térmica
    dict(id="s12", block="garrafa", text="A garrafa térmica {a}bloqueia os três processos. [p=0.3] Ela tem {b}parede dupla, com vácuo no meio: [p=0.2] sem matéria, {c}a condução e a convecção não atravessam. [p=0.3] {d}As paredes são espelhadas: [p=0.2] refletem a irradiação de volta. [p=0.3] E {e}a tampa impede o ar de entrar e sair, que seria convecção."),
    dict(id="s13", block="garrafa", text="{a}Ela segura o café quente [p=0.2] e {b}o suco gelado do mesmo jeito: [p=0.2] a garrafa não produz frio nem calor, [p=0.2] {c}só atrasa a troca."),
    # efeito estufa
    dict(id="s14", block="estufa", text="E o efeito estufa? [p=0.2] {a}A luz do Sol atravessa a atmosfera [p=0.1] e {b}esquenta o chão. [p=0.3] {c}O chão aquecido irradia infravermelho para cima. [p=0.3] Alguns gases do ar, como {d}o gás carbônico e o vapor de água, [p=0.2] {e}seguram parte desse infravermelho e devolvem para baixo."),
    dict(id="s15", block="estufa", text="{a}Entra fácil, sai difícil. [p=0.3] {b}Sem esse efeito, a Terra seria fria demais para a vida. [p=0.3] O problema é {c}o excesso: [p=0.2] mais gás carbônico no ar segura mais calor, [p=0.2] e {d}o planeta esquenta. [p=0.3] {e}Num carro fechado ao sol, acontece parecido: [p=0.2] a luz entra pelo vidro, e o ar quente não tem por onde sair."),
    # erro
    dict(id="s16", block="erro", text="Cuidado com uma frase muito repetida: [p=0.2] {a}o calor sobe. [p=0.3] {b}Quem sobe é o ar quente, [p=0.2] empurrado pela diferença de densidade. [p=0.3] {c}O calor vai do quente para o frio, para qualquer lado. [p=0.2] {d}O ferro de passar esquenta a roupa que está embaixo dele: [p=0.2] ali, o calor desce."),
    # atalho
    dict(id="s17", block="atalho", text="Agora, o atalho de prova: {a}duas perguntas. [p=0.3] {b}Primeira: precisa de matéria? [p=0.2] Se o calor passa pelo vácuo ou chega de longe, sem nada esquentar no caminho, [p=0.1] {c}é irradiação. [p=0.3] {d}Segunda: a matéria anda junto? [p=0.2] Se um líquido ou um gás circula levando o calor, [p=0.1] {e}é convecção. [p=0.3] {f}Se não anda, é condução."),
    dict(id="s18", block="atalho", text="Funciona porque {a}são só três jeitos de o calor passar, [p=0.2] e cada pergunta elimina um. [p=0.3] {b}Não compensa quando a situação mistura processos, como na garrafa térmica: [p=0.2] aí, {c}olhe cada parte do objeto separadamente."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Você está numa sala, {a}de frente para uma lareira acesa. [p=0.3] {b}Que processo esquenta o seu rosto, a dois metros do fogo? [p=0.3] E {c}que processo leva a fumaça e o ar quente para cima, pela chaminé?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] {a}Primeira pergunta: precisa de matéria? [p=0.2] O ar entre você e o fogo não leva esse calor até o seu rosto. [p=0.2] Ele chega direto, como luz: [p=0.2] {b}é irradiação. [p=0.3] Tanto que {c}uma pessoa na frente bloqueia o calor, como faz uma sombra."),
    dict(id="s22", block="resposta", text="{a}Na chaminé, o ar e a fumaça esquentam, [p=0.1] {b}ficam menos densos e sobem, [p=0.2] levando o calor junto. [p=0.2] A matéria anda: [p=0.1] {c}é convecção."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}na convecção, o fluido circula levando o calor; [p=0.2] {b}na irradiação, o calor viaja como luz, até no vácuo; [p=0.2] e {c}na condução, ele passa pela matéria parada."),
    dict(id="s24", block="fim", text="Na próxima aula, o gás vai {a}fazer força: [p=0.2] você vai calcular {b}o trabalho de um gás que empurra um pistão. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
