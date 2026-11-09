# Estudativo · FIS-EGF-008 — Flutuar ou afundar (Física · Equilíbrio, Gravitação e Fluidos · Hidrostática).
# Habilidade: comparar densidades, achar a fração submersa pela razão das densidades e calcular o peso aparente.
# Pré-requisitos: FIS-EGF-007 (empuxo), MAT-RAZ-001 (razão), MAT-RAZ-017 (densidade). Próxima: FIS-EGF-009.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Gelo ≈ 0,9 g/cm³ e água 1 (no mar, 0,92/1,03 ≈ 89%: "cerca de nove décimos"). Aço ≈ 7,8 g/cm³. "Balança de gancho" no lugar
# de dinamômetro (força elástica, FIS-DIN-005, não está em "Já ensinado"). Questão: 0,75·2 L = 1,5 L dentro; 1,5 kg = 15 N.

TITULO = "Flutuar ou afundar"

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
    dict(id="s01", block="gancho", text="{a}Um navio de aço, de milhares de toneladas, boia. [p=0.2] {b}Um prego de aço afunda na hora. [p=0.3] {c}O material é o mesmo. [p=0.2] {d}O que decide não é o peso: [p=0.1] {e}é a densidade."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai dizer se um corpo boia ou afunda, [p=0.2] {b}achar quanto dele fica debaixo d'água [p=0.2] e {c}calcular o peso aparente."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas. [p=0.2] {b}O empuxo: dê vê gê, com a densidade do líquido e o volume que está dentro. [p=0.2] E {c}a razão: a divisão de uma grandeza pela outra. [p=0.3] Se faltar alguma, procure no canal."),
    # peso contra empuxo
    dict(id="s04", block="disputa", text="{a}Prenda um corpo todo debaixo d'água e solte. [p=0.2] {b}Duas forças agem nele: o peso, para baixo, [p=0.1] {c}e o empuxo, para cima. [p=0.3] {d}O peso é a densidade do corpo vezes o volume vezes gê. [p=0.2] {e}O empuxo é a densidade do líquido vezes o mesmo volume vezes gê."),
    dict(id="s05", block="disputa", text="{a}Volume e gê são iguais nas duas contas. [p=0.2] Quem decide é {b}a densidade. [p=0.3] {c}Corpo mais denso que o líquido: o peso ganha, e ele afunda. [p=0.2] {d}Menos denso: o empuxo ganha, e ele sobe. [p=0.2] {e}Densidade igual: ele fica parado onde estiver, [p=0.1] como um peixe."),
    dict(id="s06", block="disputa", text="{a}E o navio? [p=0.2] {b}Ele é oco: [p=0.1] por dentro, tem muito ar. [p=0.3] {c}A densidade que conta é a do navio inteiro: [p=0.1] a massa de tudo, dividida pelo volume todo. [p=0.2] {d}Essa densidade média é menor que a da água. [p=0.2] {e}O prego é aço maciço, [p=0.1] quase oito vezes mais denso que a água."),
    # fração submersa
    dict(id="s07", block="fracao", text="{a}Quem boia sobe até ficar só uma parte dentro. [p=0.2] {b}Ali, o empuxo diminui até empatar com o peso: [p=0.1] {c}a força resultante é zero, e ele fica parado. [p=0.3] {d}Iguale peso e empuxo, corte o gê, [p=0.2] e sai {e}a fração submersa: [p=0.1] {f}a densidade do corpo dividida pela densidade do líquido."),
    dict(id="s08", block="fracao", text="{a}O gelo tem densidade de zero vírgula nove. [p=0.1] A água, um. [p=0.2] {b}Zero vírgula nove sobre um: [p=0.1] {c}nove décimos do iceberg ficam debaixo d'água. [p=0.2] {d}Só um décimo aparece. [p=0.3] {e}A ponta do iceberg é mesmo só a ponta."),
    # peso aparente
    dict(id="s09", block="aparente", text="{a}E o corpo que afunda? [p=0.2] {b}O empuxo continua lá, [p=0.1] e alivia o peso. [p=0.3] {c}Pendure uma pedra numa balança de gancho e mergulhe a pedra: [p=0.1] {d}a balança marca menos. [p=0.2] {e}Essa leitura é o peso aparente: [p=0.1] {f}o peso menos o empuxo."),
    dict(id="s10", block="aparente", text="{a}Uma pedra pesa trinta newtons fora da água [p=0.1] e tem volume de um litro. [p=0.3] {b}Um litro de água deslocado: dez newtons de empuxo. [p=0.2] {c}Peso aparente: trinta menos dez, [p=0.1] {d}vinte newtons. [p=0.3] {e}É por isso que, na piscina, você levanta um amigo com facilidade."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que o corpo pesado afunda e o leve boia. [p=0.3] {b}Um tronco de cem quilos boia. [p=0.2] {c}Uma moeda de cinco gramas afunda. [p=0.3] {d}Não importa quanto o corpo pesa, [p=0.1] {e}e sim se ele é mais ou menos denso que o líquido."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho de prova: [p=0.2] {a}na água, com a densidade em grama por centímetro cúbico, a fração submersa sai direto. [p=0.3] {b}Madeira de zero vírgula seis: [p=0.1] {c}seis décimos dentro. [p=0.2] {d}Cortiça de zero vírgula dois: dois décimos dentro. [p=0.3] Funciona porque {e}a densidade da água vale um, e dividir por um não muda nada."),
    dict(id="s13", block="atalho", text="{a}No óleo, ou na água do mar, a densidade não é um: [p=0.2] {b}aí, faça a divisão."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Um bloco de madeira de dois litros [p=0.1] {b}e densidade zero vírgula setenta e cinco grama por centímetro cúbico [p=0.1] {c}boia na água. [p=0.3] {d}Que fração dele fica submersa? [p=0.2] {e}E quantos litros ficam fora da água?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}A fração submersa: zero vírgula setenta e cinco sobre um, [p=0.1] {b}três quartos. [p=0.3] {c}Três quartos de dois litros: um litro e meio dentro. [p=0.2] {d}Fora, meio litro."),
    dict(id="s17", block="resposta", text="Confira: {a}um litro e meio de água deslocada dá quinze newtons de empuxo. [p=0.2] {b}Zero vírgula setenta e cinco grama por centímetro cúbico é o mesmo que zero vírgula setenta e cinco quilo por litro: [p=0.1] em dois litros, um quilo e meio. [p=0.2] {c}O bloco pesa quinze newtons. [p=0.2] {d}Empatou: ele boia parado."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}mais denso que o líquido afunda, menos denso boia; [p=0.2] {b}quem boia fica com a fração submersa igual à razão das densidades; [p=0.2] e {c}o peso aparente é o peso menos o empuxo."),
    dict(id="s19", block="fim", text="Na próxima aula, você pratica {a}a hidrostática toda: [p=0.2] {b}pressão, prensa hidráulica e empuxo, em questões inéditas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
