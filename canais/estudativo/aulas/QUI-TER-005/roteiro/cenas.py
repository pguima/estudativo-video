# Estudativo · QUI-TER-005 — Colisões e fatores da velocidade (Química · Termoquímica e Cinética · Cinética química).
# Habilidade: explicar pela teoria das colisões por que comprimido em pó reage mais rápido, por que a geladeira conserva e o que
# muda com a concentração.
# Pré-requisitos: QUI-TER-004. Próxima: QUI-TER-006 (energia de ativação e catalisador).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fora de "Já ensinado": energia de ativação (a "energia mínima" ganha nome na próxima aula), catalisador e o elo temperatura =
# agitação das partículas (MIS-003 e FIS-CAL-001 não estão na lista): a aula explica na hora.
# Fatos: cubo 2×2×2 mostra 6 × 4 = 24 faces de cubinho; separado, 8 × 6 = 48. Regra de Van't Hoff (≈ dobra a cada 10 °C) é
# aproximada e só vale se o enunciado der. Palha de aço enferruja antes do prego (superfície); vinagre + casca de ovo solta CO₂.

TITULO = "Colisões e fatores da velocidade"

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
    dict(id="s01", block="gancho", text="{a}Dois comprimidos efervescentes iguais, em dois copos de água. [p=0.2] {b}Um vai inteiro; [p=0.1] {c}o outro, esmagado em pó. [p=0.3] {d}O pó some bem antes, [p=0.1] {e}com a mesma quantidade de remédio. [p=0.2] Por quê?"),
    dict(id="s02", block="gancho", text="Até o fim da aula, você vai explicar isso {a}pela teoria das colisões, [p=0.2] e também {b}por que a geladeira conserva a comida [p=0.1] e {c}o que muda com a concentração."),
    # lembrete
    dict(id="s03", block="lembrete", text="{a}Da aula anterior: a velocidade é quanto a concentração muda por minuto. [p=0.2] {b}E concentração é quanto de substância há em cada litro. [p=0.2] Se faltar alguma, procure no canal."),
    # teoria das colisões
    dict(id="s04", block="colisoes", text="{a}Para reagir, as partículas precisam se encontrar. [p=0.2] {b}Elas estão sempre se mexendo e batendo umas nas outras. [p=0.3] {c}A teoria das colisões diz: [p=0.1] só há reação quando acontece uma batida."),
    dict(id="s05", block="colisoes", text="Mas {a}nem toda batida dá certo. [p=0.2] {b}Ela precisa ser forte o bastante, com uma energia mínima, [p=0.1] {c}e na posição certa, como uma chave entrando na fechadura. [p=0.3] {d}A batida que forma produto se chama colisão efetiva. [p=0.2] {e}As outras só batem e voltam."),
    dict(id="s06", block="colisoes", text="{a}Então, tudo o que aumenta as colisões efetivas por segundo [p=0.1] {b}acelera a reação. [p=0.3] {c}Nesta aula, são três fatores."),
    # superfície de contato
    dict(id="s07", block="superficie", text="{a}Primeiro: a superfície de contato. [p=0.2] {b}No comprimido inteiro, a água só toca a parte de fora. [p=0.1] {c}As partículas do miolo ficam esperando. [p=0.3] {d}Em pó, quase todas ficam expostas ao mesmo tempo: [p=0.1] {e}mais colisões, reação mais rápida."),
    dict(id="s08", block="superficie", text="Conte as faces de um cubo para ver o tamanho do efeito. [p=0.2] {a}Um cubo montado com oito cubinhos mostra vinte e quatro faces de cubinho por fora. [p=0.3] {b}Separe os oito cubinhos: [p=0.1] {c}cada um mostra seis faces, [p=0.1] {d}e oito vezes seis dá quarenta e oito. [p=0.2] {e}O dobro de superfície, com a mesma massa."),
    # temperatura
    dict(id="s09", block="temperatura", text="{a}Segundo: a temperatura. [p=0.2] {b}Temperatura mede o quanto as partículas se agitam. [p=0.1] {c}Mais quente, mais agitação. [p=0.3] {d}Agitadas, as partículas batem mais vezes [p=0.1] {e}e, principalmente, batem com mais força."),
    dict(id="s10", block="temperatura", text="{a}Na geladeira, acontece o contrário. [p=0.2] {b}As reações que estragam a comida, inclusive as dos micróbios, ficam mais lentas. [p=0.3] {c}A geladeira não para essas reações: [p=0.1] {d}só desacelera. [p=0.2] Por isso a comida dura mais, mas não dura para sempre."),
    # concentração
    dict(id="s11", block="concentracao", text="{a}Terceiro: a concentração. [p=0.2] {b}Mais partículas no mesmo litro, mais encontros por segundo. [p=0.3] {c}Ponha uma brasa quase apagada num frasco de gás oxigênio puro, [p=0.1] e ela volta a acender: [p=0.1] {d}há muito mais oxigênio em cada litro do que no ar."),
    dict(id="s12", block="concentracao", text="{a}E isso explica a desaceleração da aula anterior. [p=0.2] {b}Conforme o reagente é gasto, a concentração cai, [p=0.1] {c}as colisões ficam raras [p=0.1] {d}e a velocidade diminui."),
    # erro comum
    dict(id="s13", block="erro", text="{a}O erro comum é achar que esquentar só faz as partículas baterem mais vezes. [p=0.2] {b}Isso conta, mas pouco. [p=0.3] {c}O ganho grande é outro: [p=0.1] {d}muito mais batidas passam a ter a energia mínima. [p=0.2] {e}É por isso que poucos graus a mais aceleram tanto."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho de prova: [p=0.2] {a}em toda questão de velocidade, pergunte se aquilo aumenta ou diminui as colisões efetivas. [p=0.3] {b}Picar, triturar, moer: [p=0.1] mais superfície, mais rápido. [p=0.2] {c}Esquentar: mais rápido. [p=0.1] {d}Concentrar: mais rápido. [p=0.2] {e}Esfriar, diluir, deixar em pedaço grande: mais devagar."),
    dict(id="s15", block="atalho", text="{a}Algumas questões trazem uma regra aproximada: [p=0.1] {b}a cada dez graus Celsius a mais, a velocidade dobra. [p=0.2] {c}De vinte para quarenta graus, são dois saltos de dez: [p=0.1] {d}duas vezes dois, quatro vezes mais rápido. [p=0.3] {e}Use só se o enunciado der essa regra: [p=0.1] ela vale para muitas reações, não para todas."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Diga o fator em cada caso. [p=0.2] {a}Um: a palha de aço enferruja bem mais rápido que um prego de ferro. [p=0.3] {b}Dois: o leite fora da geladeira azeda muito antes. [p=0.3] {c}Três: o vinagre mais concentrado faz a casca de ovo soltar bolhas mais depressa."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="{a}A palha de aço é feita de fios finos: [p=0.1] {b}superfície de contato enorme, muito ferro exposto ao ar e à umidade. [p=0.3] {c}O leite fora da geladeira está mais quente: [p=0.1] {d}temperatura, mais colisões efetivas. [p=0.3] {e}No vinagre mais concentrado, há mais ácido em cada litro: [p=0.1] {f}concentração, mais encontros por segundo."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}reação acontece por colisão efetiva, [p=0.2] {b}e superfície, temperatura e concentração aumentam essas colisões."),
    dict(id="s20", block="fim", text="Na próxima aula, {a}a energia mínima ganha nome: energia de ativação. [p=0.2] E você vai ver {b}como o catalisador acelera a reação sem ser gasto, [p=0.1] {c}igual às enzimas do seu corpo. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
