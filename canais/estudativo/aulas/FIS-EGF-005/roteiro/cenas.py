# Estudativo · FIS-EGF-005 — Lei de Stevin (Física · Equilíbrio, Gravitação e Fluidos · Hidrostática).
# Habilidade: calcular p = p0 + d·g·h, com o atalho de 1 atm a cada 10 m de água, e resolver vasos comunicantes.
# Pré-requisitos: FIS-EGF-004 (pressão, 1 atm ≈ 10⁵ Pa), MAT-RAZ-017 (densidade). Próxima: FIS-EGF-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# g = 10 m/s², água = 1.000 kg/m³ = 1 g/cm³. 1.000·10·10 = 10⁵ Pa. Mercúrio 13,6 g/cm³: 1 atm real (101.325 Pa) ≈ 76 cm.
# Tubo em U: 0,8·10 = 1·h → h = 8 cm. Questão: 1.000·10·15 = 1,5 × 10⁵ Pa → 2,5 atm no total.

TITULO = "Lei de Stevin"

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
    dict(id="s01", block="gancho", text="{a}A dez metros de profundidade, [p=0.1] {b}a pressão sobre um mergulhador já dobrou. [p=0.3] {c}Uma coluna de dez metros de água aperta tanto quanto toda a coluna de ar em cima de nós."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular a pressão dentro de um líquido, [p=0.2] {b}com um atalho que dispensa a conta, [p=0.2] e {c}entender por que a água fica no mesmo nível em vasos ligados."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas. [p=0.2] {b}A pressão: força sobre área, em pascal, [p=0.1] e uma atmosfera vale cerca de cem mil pascals. [p=0.2] E {c}a densidade: massa sobre volume. [p=0.1] A da água é mil quilos por metro cúbico. [p=0.3] Se faltar alguma, procure no canal."),
    # de onde vem
    dict(id="s04", block="coluna", text="{a}Por que a pressão aumenta com a profundidade? [p=0.2] {b}Porque toda a água que está em cima pesa. [p=0.3] {c}Pense numa coluna de água de altura agá, em cima de um pedaço de área á. [p=0.2] {d}A pressão que ela faz é o peso da coluna dividido pela área."),
    dict(id="s05", block="coluna", text="{a}O peso é a massa vezes gê. [p=0.2] {b}A massa é a densidade vezes o volume, [p=0.1] {c}e o volume é a área vezes a altura. [p=0.3] {d}Divida pela área, e ela some. [p=0.2] {e}Sobra a pressão da coluna: dê vezes gê vezes agá."),
    dict(id="s06", block="coluna", text="{a}Somando a pressão do ar na superfície, pê zero, [p=0.2] você tem a lei de Stevin: [p=0.2] {b}pê igual a pê zero mais dê vezes gê vezes agá. [p=0.3] {c}Dê é a densidade do líquido, em quilograma por metro cúbico. [p=0.1] {d}Gê é dez. [p=0.1] {e}Agá é a profundidade, em metros, contada da superfície para baixo."),
    dict(id="s07", block="coluna", text="{a}Na água, a dez metros: [p=0.2] {b}mil vezes dez vezes dez, [p=0.1] {c}cem mil pascals. [p=0.2] {d}Uma atmosfera a mais. [p=0.3] {e}Com o ar em cima, a pressão total a dez metros é de duas atmosferas."),
    dict(id="s08", block="coluna", text="{a}Repare no que não entrou na conta: [p=0.2] {b}a largura do recipiente. [p=0.3] {c}Num copo, num balde ou numa piscina, [p=0.2] {d}na mesma profundidade, a pressão é a mesma. [p=0.2] Só a altura de líquido em cima importa."),
    # vasos comunicantes
    dict(id="s09", block="vasos", text="{a}Isso explica os vasos comunicantes: [p=0.1] recipientes ligados por baixo. [p=0.3] {b}Se a água estivesse mais alta num lado, [p=0.1] {c}a pressão embaixo seria maior desse lado, [p=0.1] e a água correria para o outro. [p=0.3] {d}Ela só para quando os níveis ficam iguais, [p=0.1] qualquer que seja o formato dos vasos."),
    dict(id="s10", block="vasos", text="{a}Com dois líquidos que não se misturam, num tubo em U, [p=0.1] como água e óleo, [p=0.2] {b}os níveis ficam diferentes. [p=0.3] {c}Na altura da separação, a pressão dos dois lados é igual, [p=0.1] e o ar em cima também. [p=0.2] {d}Então, com as alturas medidas a partir da separação, [p=0.1] dê um vezes agá um é igual a dê dois vezes agá dois."),
    dict(id="s11", block="vasos", text="{a}Óleo de densidade zero vírgula oito grama por centímetro cúbico, [p=0.1] {b}numa coluna de dez centímetros. [p=0.2] {c}Água, de densidade um grama por centímetro cúbico, [p=0.1] o mesmo que mil quilos por metro cúbico. [p=0.3] {d}Zero vírgula oito vezes dez [p=0.1] igual a um vezes agá. [p=0.2] {e}A água fica oito centímetros acima da separação. [p=0.2] {f}O líquido menos denso fica mais alto."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}esquecer a pressão do ar. [p=0.3] {b}A trinta metros, a água sozinha faz três atmosferas. [p=0.2] {c}Mas a pressão total no mergulhador é de quatro, [p=0.1] {d}porque a atmosfera continua lá em cima. [p=0.3] {e}Leia o que a questão pede: [p=0.1] {f}a pressão total, ou só a do líquido."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho de prova: [p=0.2] {a}na água, cada dez metros de profundidade somam uma atmosfera. [p=0.3] {b}Vinte metros: três atmosferas no total. [p=0.2] {c}Quarenta metros: cinco. [p=0.3] Funciona porque {d}mil vezes dez vezes dez dá cem mil pascals, [p=0.1] o valor de uma atmosfera."),
    dict(id="s14", block="atalho", text="{a}Não vale para outro líquido. [p=0.2] {b}O mercúrio é treze vírgula seis vezes mais denso que a água: [p=0.1] {c}nele, uma coluna de uns setenta e cinco centímetros já faz uma atmosfera. [p=0.2] {d}Aí, use a fórmula."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Um mergulhador está a quinze metros de profundidade. [p=0.2] {b}Use a densidade da água, mil quilos por metro cúbico. [p=0.3] {c}Qual é a pressão total sobre ele, em atmosferas? [p=0.2] {d}E quantas vezes isso é maior que a pressão na superfície?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Pela fórmula: mil vezes dez vezes quinze, [p=0.1] {b}cento e cinquenta mil pascals, [p=0.1] {c}uma atmosfera e meia só de água. [p=0.3] {d}Pelo atalho, sem conta: quinze metros são dez mais cinco, [p=0.1] uma atmosfera e meia. [p=0.3] {e}Mais a do ar: duas atmosferas e meia. [p=0.2] {f}Duas vezes e meia a pressão da superfície."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}num líquido, a pressão é pê zero mais dê gê agá; [p=0.2] {b}na água, uma atmosfera a cada dez metros; [p=0.2] e {c}na mesma profundidade do mesmo líquido, a pressão é a mesma, qualquer que seja o formato do recipiente."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai ver {a}como um elevador de oficina levanta um carro com a força de um braço: [p=0.2] {b}o princípio de Pascal. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
