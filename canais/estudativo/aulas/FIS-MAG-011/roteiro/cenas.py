# Estudativo · FIS-MAG-011 — Praticando: usinas e matriz elétrica (Física · Magnetismo · Usinas e matriz elétrica · prática).
# Habilidade: resolver questões de transformação de energia e escolha de fonte elétrica.
# Pré-requisitos: FIS-MAG-009, FIS-MAG-010. Próxima: nenhuma (fim da trilha).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Prática: cinco questões inéditas, criadas para esta aula. Rendimento da máquina térmica (FIS-CAL-014): útil sobre o calor
# recebido. Transformador, Lenz e quilowatt-hora não estão em "Já ensinado": as questões ficam em potência, em watt.

TITULO = "Praticando: usinas e matriz elétrica"

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
    dict(id="s01", block="gancho", text="Questão de usina {a}quase nunca pede conta difícil. [p=0.2] {b}Ela pede o caminho da energia [p=0.1] e {c}a escolha da fonte certa. [p=0.3] {d}Até o fim desta aula, você vai resolver cinco questões assim, [p=0.2] do começo ao fim."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar as duas últimas aulas: [p=0.2] {a}a cadeia de energia de cada usina, [p=0.1] {b}a potência da queda d'água, [p=0.1] {c}o rendimento [p=0.1] {d}e a intermitência. [p=0.3] Se faltar alguma, procure no canal."),
    # método
    dict(id="s03", block="metodo", text="Primeiro, o método. [p=0.2] {a}Toda cadeia termina igual: [p=0.1] movimento, gerador, eletricidade. [p=0.3] {b}Então, comece do fim [p=0.1] e pergunte: o que gira a turbina? [p=0.3] {c}Água, vapor ou vento. [p=0.2] {d}Só o painel solar foge da regra: [p=0.1] a luz vira eletricidade direto."),
    # questão 1
    dict(id="s04", block="q1", text="Questão um. [p=0.2] {a}Numa hidrelétrica, qual é a sequência de transformações da energia, [p=0.1] da represa até a rede? [p=0.2] {b}E numa usina nuclear, o que muda nessa história? [p=0.2] {c}Pause e tente. [p=3.0]"),
    dict(id="s05", block="q1", text="{a}No alto da represa, a água parada tem energia potencial gravitacional. [p=0.3] {b}Descendo, ela vira cinética. [p=0.2] {c}Nas pás, ela passa para o giro da turbina: [p=0.1] cinética da turbina. [p=0.2] {d}E o gerador transforma o giro em energia elétrica. [p=0.3] {e}Potencial, cinética da água, cinética da turbina, elétrica."),
    dict(id="s06", block="q1", text="{a}Na nuclear, o começo é outro: [p=0.2] {b}o reator só produz calor, [p=0.1] como a chama de uma termelétrica. [p=0.3] {c}O calor ferve a água, [p=0.1] {d}o vapor gira a turbina, [p=0.1] {e}e o fim é o mesmo: giro da turbina, eletricidade. [p=0.3] {f}Como o núcleo do átomo dá esse calor é assunto da aula de fissão."),
    # questão 2
    dict(id="s07", block="q2", text="Questão dois. [p=0.2] {a}Uma hidrelétrica tem vazão de cinquenta metros cúbicos por segundo [p=0.1] e queda de oitenta metros. [p=0.3] {b}O rendimento é de oitenta e cinco por cento. [p=0.3] {c}Qual é a potência elétrica? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s08", block="q2", text="{a}O atalho da água: [p=0.1] dez mil vezes a vazão vezes a altura. [p=0.3] {b}Cinquenta vezes oitenta, quatro mil. [p=0.2] {c}Dez mil vezes quatro mil: [p=0.1] quarenta milhões de watts, quarenta megawatts. [p=0.3] {d}Oitenta e cinco por cento disso: [p=0.1] {e}trinta e quatro megawatts."),
    # questão 3
    dict(id="s09", block="q3", text="Questão três. [p=0.2] {a}Uma termelétrica recebe da queima seiscentos megawatts de calor [p=0.1] e entrega duzentos e dez megawatts de energia elétrica. [p=0.3] {b}Qual é o rendimento? [p=0.2] {c}E quanto calor vai embora para o ambiente? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s10", block="q3", text="{a}Rendimento é útil dividido pelo total: [p=0.1] duzentos e dez dividido por seiscentos. [p=0.3] {b}Corte o zero: vinte e um dividido por sessenta, [p=0.1] {c}zero vírgula trinta e cinco: [p=0.1] trinta e cinco por cento. [p=0.3] {d}O resto vai embora: [p=0.1] seiscentos menos duzentos e dez, [p=0.1] {e}trezentos e noventa megawatts, [p=0.1] trezentos e noventa milhões de joules por segundo. [p=0.2] É a segunda lei."),
    # questão 4
    dict(id="s11", block="q4", text="Questão quatro. [p=0.2] {a}Uma empresa quer um megawatt de painéis solares ao meio-dia. [p=0.3] {b}Chegam mil watts de luz por metro quadrado, [p=0.1] e o rendimento dos painéis é de vinte por cento. [p=0.3] {c}Quantos metros quadrados de painel ela precisa? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s12", block="q4", text="{a}Cada metro quadrado entrega vinte por cento de mil watts: [p=0.1] {b}duzentos watts. [p=0.3] {c}Um megawatt é um milhão de watts. [p=0.2] {d}Um milhão dividido por duzentos: [p=0.1] {e}cinco mil metros quadrados, [p=0.1] uns dois terços de um campo de futebol. [p=0.3] {f}E isso só ao meio-dia: à noite, zero."),
    # questão 5
    dict(id="s13", block="q5", text="Questão cinco. [p=0.2] {a}Uma cidade quer uma fonte para a hora de mais consumo, que é à noite. [p=0.3] {b}Ela não pode queimar combustível. [p=0.3] {c}As opções: [p=0.1] solar, eólica, termelétrica a gás e hidrelétrica com represa. [p=0.3] {d}Qual escolher? [p=0.2] {e}Pause e tente. [p=3.0]"),
    dict(id="s14", block="q5", text="{a}Elimine pela intermitência: [p=0.1] {b}a solar não gera à noite, [p=0.1] {c}e a eólica depende do vento. [p=0.3] {d}Elimine pela queima: [p=0.1] a termelétrica a gás sai. [p=0.3] {e}Sobra a hidrelétrica: [p=0.1] a represa guarda a água, [p=0.1] e ela gera quando a cidade precisar."),
    # fechamento
    dict(id="s15", block="fim", text="Resumindo: {a}comece a cadeia pelo que gira a turbina, [p=0.2] {b}use dez mil vezes vazão vezes altura para a água, [p=0.2] e {c}escolha a fonte pelas perguntas: gera quando eu quero? queima combustível? [p=0.3] {d}Com isso, você fecha a trilha de eletromagnetismo e usinas."),
    dict(id="s16", block="fim", text="{a}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {b}Bons estudos!"),
]
