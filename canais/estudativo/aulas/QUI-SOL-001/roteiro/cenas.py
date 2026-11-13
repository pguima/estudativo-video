# Estudativo · QUI-SOL-001 — Solução, coloide e suspensão (Química · Soluções · Concentração, diluição e titulação).
# Habilidade: apontar soluto e solvente e dizer se um material é solução, coloide ou suspensão usando o efeito Tyndall.
# Pré-requisitos: QUI-MIS-002, QUI-LIG-008. Próxima: QUI-SOL-002 (solubilidade e curvas de solubilidade).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Primeira aula da trilha Soluções. Questão inédita.
# Fatos: solução = partículas do tamanho de moléculas e íons (menos de 1 nm), coloide = aglomerados de 1 a 1000 nm,
# suspensão = partículas maiores, que se veem e assentam. Leite, gelatina, neblina e maionese são coloides. O feixe de luz
# fica visível no coloide (efeito Tyndall, de John Tyndall, século 19) e também na suspensão; só a suspensão assenta.
# No ar, o nitrogênio (78%) é o solvente. Tamanho em nanômetro fica fora da fala: a aula usa "do tamanho de uma molécula".

TITULO = "Solução, coloide e suspensão"

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
    dict(id="s01", block="gancho", text="{a}Dois copos. [p=0.2] Num, água com sal. [p=0.1] {b}No outro, água com um pouco de leite. [p=0.3] Os dois parecem uma coisa só. [p=0.3] Mas aponte {c}uma lanterna de laser para cada um: [p=0.2] {d}na água com sal, o feixe some. [p=0.2] {e}No leite, ele aparece inteiro, como um fio de luz."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai saber por quê, [p=0.2] vai apontar {b}quem dissolve e quem é dissolvido [p=0.2] e separar {c}solução, coloide e suspensão. [p=0.2] Com {d}um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre de duas coisas. [p=0.2] {a}Mistura homogênea tem uma fase só: você não enxerga partes diferentes. [p=0.2] {b}Heterogênea tem mais de uma, como água e óleo. [p=0.3] E {c}semelhante dissolve semelhante: [p=0.1] a água dissolve o sal, mas não o óleo."),
    # soluto e solvente
    dict(id="s04", block="soluto", text="Comece pelo café adoçado. [p=0.2] {a}O açúcar some na água: ele foi dissolvido. [p=0.3] Quem se dissolve se chama {b}soluto. [p=0.2] Quem dissolve se chama {c}solvente. [p=0.3] No café, {d}o soluto é o açúcar, [p=0.1] e o solvente é a água."),
    dict(id="s05", block="soluto", text="{a}Na dúvida, o solvente costuma ser o que está em maior quantidade. [p=0.3] Por isso a água quase sempre é o solvente, [p=0.2] e é tão boa nisso que ganhou o apelido de {b}solvente universal. [p=0.3] E {c}a mistura do soluto com o solvente, numa fase só, é a {d}solução."),
    dict(id="s06", block="soluto", text="Solução não precisa ser líquida. [p=0.2] {a}O ar é uma solução de gases: [p=0.1] a maior parte é nitrogênio, o solvente, [p=0.2] e o oxigênio está dissolvido nele."),
    # os três tipos
    dict(id="s07", block="tipos", text="O que separa os três tipos de mistura é {a}o tamanho das partículas espalhadas no líquido. [p=0.3] {b}Na solução, elas são do tamanho de uma molécula. [p=0.2] Ninguém enxerga, nem com microscópio, [p=0.1] e {c}elas nunca assentam no fundo."),
    dict(id="s08", block="tipos", text="{a}Na suspensão, é o contrário. [p=0.2] Pense em água com terra. [p=0.2] {b}As partículas são grãos grandes, que se veem a olho nu. [p=0.3] Deixe o copo parado, e {c}elas assentam no fundo. [p=0.3] Por isso o rótulo de alguns remédios diz: {d}agite antes de usar."),
    dict(id="s09", block="tipos", text="{a}O coloide fica no meio. [p=0.2] {b}No leite, há gotinhas de gordura, cada uma com muitíssimas moléculas juntas. [p=0.3] São pequenas demais para o olho, [p=0.1] e {c}pequenas demais para assentar. [p=0.3] Por isso o leite parece homogêneo, [p=0.1] mas {d}no microscópio as gotinhas aparecem. [p=0.3] {e}Gelatina, neblina e maionese também são coloides."),
    # Tyndall
    dict(id="s10", block="tyndall", text="E aí entra a luz. [p=0.2] {a}Um feixe atravessa a solução sem ser visto, [p=0.2] porque as partículas são pequenas demais para desviar a luz. [p=0.3] {b}No coloide, as gotinhas espalham a luz para os lados, [p=0.2] e {c}o caminho do feixe aparece."),
    dict(id="s11", block="tyndall", text="Isso se chama {a}efeito Tíndal. [p=0.3] Você já viu: [p=0.1] {b}é o farol do carro desenhado na neblina, [p=0.2] ou {c}o raio de sol entrando por uma fresta, cheio de poeira."),
    dict(id="s12", block="tyndall", text="{a}A suspensão também mostra o feixe, porque os grãos são grandes. [p=0.3] Mas ela se entrega de outro jeito: [p=0.1] {b}com o tempo, assenta."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum: [p=0.2] {a}achar que tudo o que parece homogêneo é solução. [p=0.3] {b}O leite parece, [p=0.1] e a pessoa marca solução. [p=0.3] {c}Mas o feixe de luz aparece no leite: [p=0.2] {d}é um coloide. [p=0.3] {e}O olho não basta. Quem decide é a luz."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho de prova são duas perguntas, nesta ordem. [p=0.2] {a}Primeira: com o tempo, assenta? [p=0.2] {b}Se assenta, é suspensão. [p=0.3] {c}Segunda: o feixe de luz aparece? [p=0.2] {d}Se aparece, é coloide. [p=0.2] {e}Se não aparece, é solução."),
    dict(id="s15", block="atalho", text="A ordem importa {a}porque a suspensão também mostra o feixe. [p=0.3] Comece pelo fundo do copo, [p=0.1] e o feixe só precisa separar as outras duas. [p=0.3] {b}Não compensa quando a mistura é escura, como tinta: [p=0.2] a luz nem atravessa. [p=0.2] Aí, olhe só se assenta."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Três copos que parecem uma coisa só, e um feixe de laser em cada um. [p=0.3] {a}No copo um, o feixe não aparece, e nada assenta. [p=0.2] {b}No copo dois, o feixe aparece, e nada assenta depois de um dia. [p=0.2] {c}No copo três, o feixe aparece, e em uma hora se forma uma camada no fundo. [p=0.3] {d}Classifique os três. [p=0.2] E, se o copo um é água com açúcar, {e}qual é o soluto?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Pergunta um, assenta? [p=0.2] {a}Só o copo três: é suspensão. [p=0.3] Pergunta dois, o feixe aparece? [p=0.2] {b}No copo dois, sim: é coloide. [p=0.2] {c}No copo um, não: é solução. [p=0.3] E na água com açúcar, {d}o soluto é o açúcar, [p=0.1] {e}e a água é o solvente."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}o soluto se dissolve no solvente, [p=0.1] {b}a suspensão assenta, [p=0.1] {c}o coloide mostra o feixe de luz, [p=0.1] {d}e a solução não mostra nada."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai ver que a água não dissolve sal sem fim: [p=0.2] {a}existe um limite, a solubilidade, [p=0.2] e {b}ele muda com a temperatura. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
