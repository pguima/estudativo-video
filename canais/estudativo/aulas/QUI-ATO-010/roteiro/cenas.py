# Estudativo · QUI-ATO-010 — Raio atômico (Química · Átomo e Tabela Periódica · Tabela periódica).
# Habilidade: ordenar Na, Mg e K pelo raio atômico e dizer por que o Na⁺ é menor que o Na.
# Pré-requisitos: QUI-ATO-008. Próxima: QUI-ATO-011 (energia de ionização e eletronegatividade).
# Questão inédita, criada para esta aula.
# Fatos: Li (2 camadas), Na (3), K (4) na família 1; Na (Z 11) e Mg (Z 12) no período 3; Mg < Na < K;
# Na⁺ perde o 3s¹ e fica com 2 camadas, 11 prótons para 10 elétrons; Cl⁻ > Cl; Mg (período 3) e Ca (período 4) na família 2,
# K e Ca no período 4: Mg < Ca < K; Ca²⁺ perde o 4s² (a camada 4). Os maiores átomos ficam no canto de baixo à esquerda (Cs, Fr).

TITULO = "Raio atômico"

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
    dict(id="s01", block="gancho", text="{a}O magnésio tem mais prótons e mais elétrons que o sódio. [p=0.3] {b}Mesmo assim, o átomo de magnésio é menor. [p=0.3] {c}Mais partículas, tamanho menor: [p=0.1] por quê?"),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}ordenar átomos pelo tamanho, [p=0.1] olhando a tabela, [p=0.2] e explicar {b}por que o íon de sódio é menor que o átomo de sódio."),
    # lembrete
    dict(id="s03", block="lembrete", text="Das aulas anteriores: [p=0.1] {a}o período é o número de camadas, [p=0.1] e {b}a família é a coluna. [p=0.3] E {c}cargas opostas se atraem: [p=0.1] o núcleo positivo puxa os elétrons."),
    # o raio
    dict(id="s04", block="raio", text="{a}O raio atômico mede o tamanho do átomo: [p=0.1] {b}a distância do núcleo até a última camada. [p=0.3] {c}Quanto mais longe a última camada, maior o átomo."),
    # na família
    dict(id="s05", block="familia", text="Desça a família um: {a}lítio, sódio, potássio. [p=0.3] {b}Cada período a mais é uma camada a mais. [p=0.2] {c}O lítio tem duas camadas, [p=0.1] o sódio, três, [p=0.1] e o potássio, quatro. [p=0.3] {d}Descendo a família, o raio aumenta."),
    # no período
    dict(id="s06", block="periodo", text="Agora ande no terceiro período, {a}do sódio para o magnésio. [p=0.2] {b}Sódio e magnésio têm três camadas. [p=0.2] {c}Mas o magnésio tem um próton a mais no núcleo. [p=0.3] {d}Mais carga positiva puxa a eletrosfera para mais perto. [p=0.2] {e}Indo para a direita no período, o raio diminui."),
    # ordenar
    dict(id="s07", block="ordem", text="Vamos ordenar {a}sódio, magnésio e potássio. [p=0.2] {b}Magnésio e sódio estão no mesmo período: [p=0.1] {c}o magnésio, mais à direita, é menor. [p=0.3] {d}Sódio e potássio estão na mesma família: [p=0.1] {e}o potássio, mais embaixo, é maior. [p=0.3] {f}Do menor para o maior: magnésio, sódio, potássio."),
    # o íon
    dict(id="s08", block="ion", text="E o íon de sódio? [p=0.2] {a}O sódio tem um elétron só na camada três. [p=0.2] {b}Para virar o íon sódio um mais, ele perde justamente esse elétron. [p=0.3] {c}A camada três some inteira. [p=0.2] {d}Sobram duas camadas, [p=0.1] e {e}os onze prótons puxam só dez elétrons. [p=0.3] {f}O íon fica bem menor que o átomo."),
    dict(id="s09", block="ion", text="{a}Com o ânion acontece o contrário. [p=0.2] {b}Os elétrons a mais têm carga igual, se empurram e espalham a eletrosfera: [p=0.1] {c}o cloro com carga menos um é maior que o cloro."),
    # erro
    dict(id="s10", block="erro", text="O erro comum: [p=0.1] {a}achar que o raio cresce sempre junto com o zê. [p=0.3] {b}O magnésio tem zê doze, [p=0.1] o sódio tem zê onze, [p=0.1] {c}e o magnésio é menor. [p=0.2] {d}No mesmo período, mais prótons deixam o átomo menor."),
    # atalho
    dict(id="s11", block="atalho", text="O atalho de prova: [p=0.1] {a}desenhe na tabela uma seta para o canto de baixo, à esquerda. [p=0.3] {b}O raio cresce nessa direção: [p=0.1] {c}para baixo e para a esquerda. [p=0.2] {d}Nesse canto ficam os maiores átomos, como o césio."),
    dict(id="s12", block="atalho", text="Funciona porque {a}descer acrescenta camada, [p=0.1] e {b}ir para a direita acrescenta prótons na mesma camada. [p=0.3] {c}Não compensa quando um átomo está, ao mesmo tempo, {d}mais embaixo e mais à direita que o outro. [p=0.2] Aí, as duas regras brigam, [p=0.1] e {e}a questão precisa dar mais informação."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] {a}Ordene magnésio, cálcio e potássio, do menor para o maior raio. [p=0.3] {b}Magnésio e cálcio estão na família dois. [p=0.1] {c}Cálcio e potássio, no quarto período. [p=0.3] E {d}quem é maior: o átomo de cálcio ou o íon cálcio dois mais?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] {a}O cálcio está embaixo do magnésio: [p=0.1] {b}o cálcio é maior. [p=0.2] {c}O potássio está à esquerda do cálcio: [p=0.1] {d}o potássio é maior. [p=0.3] {e}Do menor para o maior: magnésio, cálcio, potássio. [p=0.3] {f}E o átomo de cálcio é maior que o cálcio dois mais, [p=0.1] que perdeu a última camada."),
    # fechamento
    dict(id="s16", block="fim", text="Resumindo: [p=0.1] {a}o raio cresce descendo a família [p=0.1] e {b}diminui para a direita no período. [p=0.2] {c}O cátion é menor que o átomo, [p=0.1] e {d}o ânion é maior."),
    dict(id="s17", block="fim", text="Na próxima aula, {a}duas propriedades que andam ao contrário do raio: [p=0.2] {b}energia de ionização e eletronegatividade. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
