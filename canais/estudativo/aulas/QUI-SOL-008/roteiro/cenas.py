# Estudativo · QUI-SOL-008 — Pressão de vapor e ponto de ebulição (Química · Soluções · Propriedades coligativas).
# Habilidade: explicar por que a água ferve abaixo de 100 °C na montanha e acima na panela de pressão e por que a água com sal
# ferve depois da pura.
# Pré-requisitos: QUI-MIS-003, QUI-CAL-010, QUI-SOL-001. Próxima: QUI-SOL-009 (congelar mais tarde: contar as partículas).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Primeira aula do módulo de propriedades coligativas. Questão inédita.
# Fatos: a pressão de vapor da água chega a 760 mmHg (1 atm) a 100 °C; em La Paz (cerca de 3 600 m) o ar faz cerca de 0,65 atm e a
# água ferve perto de 88 °C; a panela de pressão chega a cerca de 2 atm e a água ferve perto de 120 °C. Uma colher de sal num
# litro de água sobe a fervura em menos de meio grau (≈ 0,18 °C para 10 g/L). Tonoscopia = abaixamento da pressão de vapor;
# ebulioscopia = aumento da temperatura de ebulição. Soluto não volátil (sal, açúcar).

TITULO = "Pressão de vapor e ponto de ebulição"

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
    dict(id="s01", block="gancho", text="{a}Em La Paz, na Bolívia, a água ferve a uns oitenta e oito graus. [p=0.3] {b}Na panela de pressão, a uns cento e vinte. [p=0.3] {c}E a água com sal ferve numa temperatura um pouco mais alta que a pura. [p=0.3] {d}Três fatos, uma ideia só por trás deles."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai entender {b}a pressão de vapor [p=0.2] e usá-la para {c}explicar os três casos, [p=0.2] com {d}uma pergunta que resolve a prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre: [p=0.1] {a}no líquido, as partículas se agitam mais quando esquentam. [p=0.3] {b}Pressão de um gás é o choque das partículas dele contra uma superfície. [p=0.3] E {c}ao nível do mar, o ar faz uma atmosfera de pressão, [p=0.1] {d}que são setecentos e sessenta milímetros de mercúrio."),
    # pressão de vapor
    dict(id="s04", block="vapor", text="{a}Feche um pouco de água num pote. [p=0.2] {b}As partículas mais agitadas da superfície escapam e viram vapor. [p=0.3] {c}Esse vapor fica preso em cima do líquido, [p=0.1] {d}batendo nas paredes."),
    dict(id="s05", block="vapor", text="{a}A pressão que esse vapor faz se chama pressão de vapor. [p=0.3] Ela mede {b}a vontade do líquido de evaporar. [p=0.3] {c}Esquentou, mais partículas escapam, [p=0.1] {d}e a pressão de vapor sobe."),
    # ebulição
    dict(id="s06", block="ferver", text="Agora, ferver. [p=0.2] {a}Ferver é formar bolhas de vapor dentro do líquido. [p=0.3] {b}Mas o ar de fora aperta a superfície. [p=0.2] {c}A bolha só se forma quando a pressão de vapor empata com a pressão de fora. [p=0.3] {d}A temperatura em que isso acontece se chama ponto de ebulição."),
    dict(id="s07", block="ferver", text="{a}Na praia, a pressão de fora é aquela uma atmosfera. [p=0.2] {b}A pressão de vapor da água só chega a uma atmosfera a cem graus. [p=0.3] {c}Por isso a água ferve a cem graus na praia."),
    # montanha e panela
    dict(id="s08", block="lugares", text="{a}No alto da montanha, há menos ar em cima de você. [p=0.2] {b}A pressão de fora é menor. [p=0.3] {c}A pressão de vapor empata com ela mais cedo, numa temperatura mais baixa. [p=0.3] {d}Em La Paz, a uns oitenta e oito graus. [p=0.2] {e}O feijão demora mais, porque a água não passa disso."),
    dict(id="s09", block="lugares", text="{a}A panela de pressão faz o contrário. [p=0.2] {b}A tampa prende o vapor, e a pressão lá dentro chega perto de duas atmosferas. [p=0.3] {c}Para empatar com ela, a água precisa chegar a uma temperatura maior: [p=0.1] {d}ferve a uns cento e vinte graus. [p=0.2] {e}Mais quente, o feijão cozinha mais rápido."),
    # sal
    dict(id="s10", block="sal", text="E o sal? [p=0.2] {a}Na solução, as partículas de sal ocupam lugar na superfície. [p=0.3] {b}Menos partículas de água conseguem escapar. [p=0.3] {c}A pressão de vapor da solução fica menor que a da água pura. [p=0.3] {d}Esse efeito se chama tonoscopia."),
    dict(id="s11", block="sal", text="{a}Com a pressão de vapor mais baixa, a solução demora mais para empatar com o ar de fora. [p=0.3] {b}Precisa esquentar mais: [p=0.1] {c}ferve acima de cem graus. [p=0.3] {d}A subida do ponto de ebulição se chama ebulioscopia."),
    dict(id="s12", block="sal", text="{a}O que importa é quantas partículas de soluto há, não qual soluto é. [p=0.3] {b}Efeito assim, que depende só da quantidade de partículas, [p=0.1] {c}se chama efeito coligativo. [p=0.3] {d}E ele vale para soluto que não evapora, como sal e açúcar."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum: [p=0.2] {a}dizer que o sal faz a água ferver mais rápido. [p=0.3] {b}É o contrário: ele sobe o ponto de ebulição, [p=0.1] e a água demora um pouco mais. [p=0.3] {c}E uma colher de sal na panela sobe menos de meio grau: [p=0.1] {d}na cozinha, quase não muda nada."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho de prova é uma pergunta: [p=0.2] {a}o que mudou? [p=0.3] {b}Se mudou a pressão de fora, como na montanha e na panela, [p=0.1] {c}não é efeito coligativo. [p=0.3] {d}Se mudou o que está dissolvido, como o sal, [p=0.1] {e}é coligativo."),
    dict(id="s15", block="atalho", text="E a regra das setas: [p=0.2] {a}mais pressão de fora, ferve mais quente. [p=0.2] {b}Menos pressão de fora, ferve mais frio. [p=0.2] {c}Mais soluto, ferve mais quente. [p=0.3] Funciona porque {d}tudo se resume a um empate: pressão de vapor contra pressão de fora. [p=0.3] {e}Não compensa com soluto que evapora, como álcool: [p=0.1] aí a mistura pode ferver abaixo de cem."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Três panelas com um litro de água. [p=0.3] {a}A: água pura, na praia. [p=0.2] {b}B: água com açúcar, na praia. [p=0.2] {c}C: água pura, no alto de uma serra. [p=0.3] {d}Ponha em ordem, da que ferve mais quente para a que ferve mais fria. [p=0.2] {e}E diga em qual delas a diferença é um efeito coligativo."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="{a}A, água pura na praia, ferve a cem graus: é a referência. [p=0.3] {b}B tem soluto, a pressão de vapor cai, [p=0.1] e ela ferve acima de cem. [p=0.3] {c}C está na serra, com menos pressão de fora: ferve abaixo de cem. [p=0.3] {d}A ordem é B, A, C. [p=0.3] {e}Só B é efeito coligativo: em C, quem mudou foi a pressão do ar."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}o líquido ferve quando a pressão de vapor empata com a de fora. [p=0.2] {b}Pressão de fora muda o ponto de ebulição, [p=0.1] e {c}soluto também, porque baixa a pressão de vapor."),
    dict(id="s20", block="fim", text="Na próxima aula, o soluto vai agir no frio: [p=0.2] {a}por que o anticongelante não deixa a água congelar, [p=0.2] e {b}como contar as partículas para comparar soluções. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
