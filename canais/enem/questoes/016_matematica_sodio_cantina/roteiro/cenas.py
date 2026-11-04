# Estudativo · Questão 016 — ENEM 2025, 2º dia, caderno amarelo, questão 140: cinco alimentos da cantina, cada pacote com
# um número de porções e o sódio POR PORÇÃO. A estudante escolhe o de menor sódio TOTAL POR PACOTE.
# Batata chips 3 × 170 = 510 · Palitos 4 × 501 = 2.004 · Multigrãos 8 × 264 = 2.112 · Polvilho 6 × 175 = 1.050 ·
# Água e sal 5 × 166 = 830 → 510 mg, batata chips (alternativa A). Enunciado: enunciado/questao.png.
# Caminho: A FERRAMENTA: total = quantidade por unidade × número de unidades → passo 1: separar o que importa (as gramas
# da porção não entram) → passo 2: os cinco totais, com cálculo mental → passo 3: comparar (510 é o menor) → pegadinhas:
# menor POR PORÇÃO (166, água e sal, E) e pacote mais LEVE (80 g, palitos, B) → curiosidade OMS + desafio (água e sal
# com 3 porções) → resumo → aulas.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso (a legenda mostra algarismos).

TITULO = "Questão do ENEM 2025: qual lanche da cantina tem menos sódio no pacote? (por porção × por pacote)"

VOZ = dict(
    tags=["amigavel", "curiosa", "confiante"],
    prompt=("Narre como um professor de matemática de cursinho, explicando uma questão do ENEM para um aluno: voz "
            "masculina adulta, calorosa, clara e envolvente, com bastante variação de entonação. Comece já com energia, "
            "sem introdução. Nas contas, fale devagar e com clareza, número por número. Faça as perguntas com "
            "curiosidade genuína, mostre surpresa na resposta e comemore o resultado. Respeite as pausas entre as "
            "frases. Leia apenas o texto, exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(pad_inicio=0.0, pad_fim=1.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Questão cento e quarenta do ENEM dois mil e vinte e cinco. [p=0.2] Na cantina de uma escola, [p=0.1] há "
        "*cinco* alimentos, [p=0.1] vendidos em pacotes com quantidades diferentes de porções. [p=0.3] {b}O rótulo de "
        "cada um diz quantas porções vêm no pacote [p=0.1] e quanto *sódio* tem em *cada porção.* [p=0.3] {c}Uma "
        "estudante escolhe sempre o alimento com a *menor quantidade total de sódio por pacote.* [p=0.3] {d}Qual ela "
        "deve escolher? [p=0.3] Nessa aula, você vai resolver passo a passo, [p=0.1] e ver as *duas pegadinhas* que "
        "essa questão esconde."),
    dict(id="02", block="ferramenta", text=
        "{a}Primeiro, a ferramenta: [p=0.1] a diferença entre *por porção* [p=0.1] e *por pacote.* [p=0.3] {b}O rótulo "
        "fala de *uma* porção. [p=0.2] Mas o pacote tem *várias* porções iguais, [p=0.1] e cada uma traz a mesma "
        "quantidade de sódio. [p=0.3] {c}Então o total do pacote é uma *multiplicação:* [p=0.2] sódio por porção, "
        "[p=0.1] vezes o número de porções. [p=0.3] {d}Um exemplo: [p=0.1] um pacote com duas porções de cem "
        "miligramas [p=0.1] tem cem vezes dois, [p=0.1] *duzentos* miligramas de sódio."),
    dict(id="03", block="dados", text=
        "{a}Passo um: [p=0.1] separar o que importa. [p=0.3] {b}Em cada rótulo, [p=0.1] usamos *dois* números: "
        "[p=0.1] quantas porções tem o pacote [p=0.1] e quantos miligramas de sódio tem cada porção. [p=0.3] "
        "{c}E as *gramas* da porção? [p=0.2] Cinquenta gramas, [p=0.1] vinte gramas... [p=0.2] Elas dizem o *peso* da "
        "comida, [p=0.1] não o sódio. [p=0.2] Para essa pergunta, [p=0.1] *não entram na conta.*"),
    dict(id="04", block="contas", text=
        "{a}Passo dois: [p=0.1] o sódio total de cada pacote. [p=0.3] {b}Batata chips: [p=0.1] três porções de cento "
        "e setenta. [p=0.2] Três vezes cento e setenta, [p=0.1] *quinhentos e dez* miligramas. [p=0.3] {c}Palitos "
        "salgados: [p=0.1] quatro vezes quinhentos e um. [p=0.2] Quatro vezes quinhentos dá dois mil, [p=0.1] mais "
        "quatro: [p=0.1] *dois mil e quatro.* [p=0.3] {d}Biscoito multigrãos: [p=0.1] oito vezes duzentos e sessenta "
        "e quatro. [p=0.2] Oito vezes duzentos, [p=0.1] mil e seiscentos. [p=0.1] Oito vezes sessenta e quatro, "
        "[p=0.1] quinhentos e doze. [p=0.2] Total: [p=0.1] *dois mil cento e doze.* [p=0.3] {e}Biscoito de polvilho: "
        "[p=0.1] seis vezes cento e setenta e cinco. [p=0.2] Seiscentos, [p=0.1] mais quatrocentos e cinquenta: "
        "[p=0.1] *mil e cinquenta.* [p=0.3] {f}Biscoito de água e sal: [p=0.1] cinco vezes cento e sessenta e seis. "
        "[p=0.2] Quinhentos, [p=0.1] mais trezentos e trinta: [p=0.1] *oitocentos e trinta.*"),
    dict(id="05", block="comparar", text=
        "{a}Passo três: [p=0.1] comparar os cinco totais. [p=0.3] {b}Em ordem, do menor para o maior: [p=0.1] "
        "quinhentos e dez, [p=0.1] oitocentos e trinta, [p=0.1] mil e cinquenta, [p=0.1] dois mil e quatro [p=0.1] e "
        "dois mil cento e doze. [p=0.3] {c}O menor é *quinhentos e dez* miligramas: [p=0.1] a *batata chips.* [p=0.2] "
        "Alternativa *A.*"),
    dict(id="06", block="pegadinha", text=
        "{a}Agora, as pegadinhas. [p=0.2] A primeira: [p=0.1] olhar só o número *por porção.* [p=0.3] {b}O menor valor "
        "por porção é cento e sessenta e seis, [p=0.1] do biscoito de água e sal. [p=0.2] Quem para aí [p=0.1] marca a "
        "alternativa E. [p=0.3] {c}Mas esse pacote tem *cinco* porções, [p=0.1] e chega a oitocentos e trinta. "
        "[p=0.2] A batata tem *só três* porções, [p=0.1] e fica em quinhentos e dez. [p=0.3] {d}A segunda: [p=0.1] "
        "escolher o pacote mais *leve.* [p=0.2] Os palitos pesam só oitenta gramas no total, [p=0.1] e mesmo assim "
        "têm *dois mil e quatro* miligramas de sódio. [p=0.2] Pacote leve [p=0.1] não quer dizer pouco sódio."),
    dict(id="07", block="generaliza", text=
        "{a}Uma curiosidade: [p=0.1] a Organização Mundial da Saúde recomenda que um adulto consuma *menos de dois "
        "mil miligramas* de sódio por dia. [p=0.2] Sozinhos, [p=0.1] o pacote de palitos e o de biscoito multigrãos [p=0.1] já passam disso. [p=0.3] {b}Agora é "
        "com você: [p=0.1] e se o biscoito de água e sal viesse com *três* porções, [p=0.1] em vez de cinco? [p=0.2] "
        "A estudante mudaria de escolha? [p=0.2] Deixe sua resposta nos comentários."),
    dict(id="08", block="resumo", text=
        "{a}Vamos recapitular o caminho. [p=0.2] {b}Primeiro, separamos os dados que importam: [p=0.1] porções e "
        "sódio por porção. [p=0.2] {c}Depois, multiplicamos para achar o total de cada pacote. [p=0.2] {d}O menor total "
        "é quinhentos e dez: [p=0.1] batata chips. [p=0.2] {e}E cuidado: [p=0.1] nem o menor valor por porção, [p=0.1] "
        "nem o pacote mais leve [p=0.1] respondem a pergunta."),
    dict(id="09", block="aulas", text=
        "{a}Cada ferramenta dessa questão [p=0.1] tem uma *aula completa* aqui no Estudativo: [p=0.3] "
        "{b}*razão e proporção,* [p=0.2] {c}*grandezas proporcionais* [p=0.2] {d}e *comparação de propostas.* [p=0.3] "
        "{e}Se quiser aprender cada assunto desde o começo, [p=0.1] procure essas aulas aqui no canal. [p=0.4] "
        "{f}E se essa questão te ajudou, [p=0.1] inscreva-se no *Estudativo* [p=0.1] para não perder a próxima questão."),
]
