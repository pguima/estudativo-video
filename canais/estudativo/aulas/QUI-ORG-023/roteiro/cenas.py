# Estudativo · QUI-ORG-023 — Saponificação e biodiesel (Química · Química Orgânica · Reações orgânicas).
# Habilidade: diferenciar óleo de gordura, escrever como a gordura com base vira sabão e explicar a transesterificação que
# produz biodiesel.
# Pré-requisitos: QUI-ORG-013, QUI-ORG-022. Próxima: QUI-ORG-024 (praticando reações orgânicas).
# Marcas: {cue} animação · [p=0.2] pausa. Fórmulas por extenso: NaOH = "ene á ó agá".
# Fatos: óleo e gordura são triglicerídeos (triésteres do glicerol, propano-1,2,3-triol, a glicerina) com três ácidos graxos;
# óleo tem mais duplas nas cadeias (insaturado) e é líquido a 25 °C; gordura tem cadeias mais saturadas e é sólida.
# Saponificação: triglicerídeo + 3 NaOH → 3 sabões (sais de sódio dos ácidos graxos) + glicerol. Transesterificação:
# triglicerídeo + 3 metanol (ou etanol), com catalisador básico → 3 ésteres (biodiesel) + glicerol. No Brasil, o diesel
# vendido leva biodiesel misturado (14% em 2024; a mistura sobe por lei): a aula diz só "o diesel do posto leva biodiesel".
# Questão inédita: óleo de soja + etanol (transesterificação) × óleo + KOH (saponificação).

TITULO = "Saponificação e biodiesel"

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
    dict(id="s01", block="gancho", text="{a}Sabão caseiro se faz com óleo de cozinha usado e soda cáustica. [p=0.3] {b}E o diesel do posto leva biodiesel, feito principalmente de óleo de soja. [p=0.3] {c}Mesmo óleo, dois produtos: [p=0.2] {d}só muda o que entra na reação."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}diferenciar óleo de gordura, [p=0.2] {c}escrever como o óleo ou a gordura vira sabão [p=0.2] e {d}explicar o biodiesel. [p=0.2] E ainda leva um {e}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre de duas aulas. [p=0.2] {a}Na hidrólise, éster mais água dá ácido mais álcool. [p=0.3] E {b}o sabão tem uma ponta que gosta de água e {c}uma cauda longa que gosta de gordura."),
    # óleo e gordura
    dict(id="s04", block="trigli", text="Óleo e gordura são {a}a mesma família de moléculas. [p=0.2] {b}No centro, um álcool com três ó agá, o glicerol, também chamado glicerina. [p=0.3] {c}Em cada ó agá, um ácido de cadeia longa, o ácido graxo, preso por uma ligação de éster. [p=0.3] {d}Três ésteres numa molécula só: é o triglicerídeo."),
    dict(id="s05", block="trigli", text="A diferença está nas cadeias. [p=0.2] {a}No óleo, elas têm mais ligações duplas, que entortam a cadeia. [p=0.2] {b}As moléculas se encaixam mal, e o óleo fica líquido à temperatura ambiente. [p=0.3] {c}Na gordura, as cadeias têm pouca ou nenhuma dupla: [p=0.2] {d}são retas, se empilham bem, e a gordura fica sólida."),
    # saponificação
    dict(id="s06", block="sabao", text="Agora, o sabão. [p=0.2] {a}Junte óleo ou gordura com uma base forte, como o ene á ó agá, a soda cáustica, e aqueça. [p=0.3] {b}Cada ligação de éster se quebra, como na hidrólise. [p=0.3] {c}Mas o ácido graxo não fica solto: [p=0.2] {d}ele reage com a base e vira um sal de sódio."),
    dict(id="s07", block="sabao", text="{a}Esse sal é o sabão. [p=0.2] {b}E o glicerol fica livre. [p=0.3] A conta: [p=0.1] {c}um triglicerídeo mais três ene á ó agá [p=0.2] {d}dão três sabões {e}mais um glicerol. [p=0.3] {f}O nome dessa reação é saponificação, de sabão."),
    # biodiesel
    dict(id="s08", block="biodiesel", text="E o biodiesel? [p=0.2] {a}Junte o óleo com um álcool pequeno, como o metanol ou o etanol, [p=0.2] e um ajudante, o catalisador, que acelera a reação sem ser gasto. [p=0.3] {b}Cada ligação de éster troca de álcool: [p=0.2] {c}sai o glicerol, {d}entra o metanol."),
    dict(id="s09", block="biodiesel", text="{a}Os ácidos graxos continuam como ésteres, agora de metanol. [p=0.2] {b}Esses ésteres são o biodiesel. [p=0.3] {c}Um triglicerídeo mais três metanóis dão três ésteres mais um glicerol. [p=0.3] {d}Como é um éster que vira outro éster, o nome é transesterificação."),
    # erro
    dict(id="s10", block="erro", text="O erro mais comum é {a}confundir as duas, porque {b}as duas soltam glicerol. [p=0.3] {c}Olhe o produto principal. [p=0.2] {d}Sabão é sal: veio de uma base. [p=0.2] {e}Biodiesel é éster: veio de um álcool."),
    # atalho
    dict(id="s11", block="atalho", text="O atalho de prova: [p=0.2] {a}o que entra decide o que sai. [p=0.3] {b}Entra água, sai ácido: é hidrólise. [p=0.2] {c}Entra base, sai sal: é saponificação. [p=0.2] {d}Entra álcool, sai outro éster: é transesterificação. [p=0.3] {e}E, do triglicerídeo, o glicerol sai sempre."),
    dict(id="s12", block="atalho", text="{a}Funciona porque o pedaço do ácido graxo é sempre o mesmo: [p=0.2] só muda o parceiro que fica com ele."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] {a}Uma usina mistura óleo de soja com etanol e um catalisador. [p=0.3] {b}Que reação é essa, e o que se forma? [p=0.3] {c}E se, no lugar do etanol, entrasse hidróxido de potássio, cá ó agá?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s15", block="resposta", text="{a}Entrou álcool: transesterificação. [p=0.2] {b}Saem ésteres de etanol, que são o biodiesel, [p=0.2] {c}e o glicerol."),
    dict(id="s16", block="resposta", text="{a}Com cá ó agá, entrou base: saponificação. [p=0.2] {b}Saem sais de potássio dos ácidos graxos, um sabão, [p=0.2] {c}e, de novo, o glicerol."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: [p=0.1] {a}à temperatura ambiente, o óleo, com mais duplas, é líquido, e a gordura, com menos, é sólida. [p=0.2] {b}Com base, a gordura vira sabão e glicerol. [p=0.2] {c}Com álcool, o óleo vira biodiesel e glicerol."),
    dict(id="s18", block="fim", text="Na próxima aula, você vai praticar {a}todas as reações deste módulo, [p=0.2] em processos {b}da indústria e do corpo humano. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
