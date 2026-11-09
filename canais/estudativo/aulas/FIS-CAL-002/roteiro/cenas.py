# Estudativo · FIS-CAL-002 — Dilatação térmica (Física · Calor e Termodinâmica · Temperatura e dilatação).
# Habilidade: usar ΔL = L0·α·ΔT com o atalho β = 2α e γ = 3α e explicar juntas de dilatação, lâmina bimetálica e a anomalia da água.
# Pré-requisitos: FIS-CAL-001 (temperatura, ΔC = ΔK), MAT-POT-005 (potências de 10), QUI-LIG-011 (gelo boia). Próxima: FIS-CAL-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita. Valores de tabela arredondados: aço α = 1,2·10⁻⁵ °C⁻¹, alumínio α = 2,4·10⁻⁵ °C⁻¹.
# β = 2α e γ = 3α são aproximações (as dilatações são muito pequenas): dito como "na prática".

TITULO = "Dilatação térmica"

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
    dict(id="s01", block="gancho", text="{a}Repare numa ponte de concreto: [p=0.2] de tempos em tempos, ela tem {b}uma fresta, [p=0.2] às vezes coberta por uma peça de metal. [p=0.3] Não é defeito. [p=0.2] Sem ela, no verão, {c}a ponte racharia."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular quanto um material {b}cresce quando esquenta [p=0.2] e explicar {c}três fenômenos que caem muito em prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a variação de temperatura, [p=0.1] que é igual em Celsius e em Kelvin; [p=0.2] e {c}as potências de dez, como dez elevado a menos três, que é um milésimo. [p=0.3] Se faltar alguma, procure no canal."),
    # por que dilata
    dict(id="s04", block="ideia", text="Por que as coisas crescem quando esquentam? [p=0.2] Temperatura é agitação das partículas. [p=0.3] {a}Mais agitadas, elas precisam de mais espaço [p=0.2] e {b}se afastam umas das outras. [p=0.3] O material inteiro {c}aumenta um pouquinho. [p=0.2] Isso é a {d}dilatação térmica."),
    # a fórmula
    dict(id="s05", block="formula", text="Numa barra, o que importa é o aumento do {a}comprimento. [p=0.2] A fórmula é {b}delta éle igual a éle zero vezes alfa vezes delta tê."),
    dict(id="s06", block="formula", text="{a}Delta éle é quanto a barra cresceu. [p=0.2] {b}O éle zero é o comprimento inicial, [p=0.1] e o delta éle sai na mesma unidade dele. [p=0.2] {c}Delta tê é a variação de temperatura. [p=0.3] E {d}alfa é o coeficiente de dilatação linear: [p=0.2] quanto cada metro do material cresce a cada grau. [p=0.2] A unidade dele é {e}por grau Celsius."),
    dict(id="s07", block="formula", text="Cada material tem o seu alfa, e ele é minúsculo. [p=0.2] No aço, {a}um vírgula dois vezes dez elevado a menos cinco por grau Celsius. [p=0.3] Por isso, {b}a dilatação é pequena, [p=0.2] mas {c}a força que ela faz é enorme."),
    # exemplo
    dict(id="s08", block="exemplo", text="Vamos calcular. [p=0.2] {a}Um trilho de aço de vinte metros [p=0.1] esquenta {b}cinquenta graus Celsius num dia de sol. [p=0.3] Quanto ele cresce?"),
    dict(id="s09", block="exemplo", text="{a}Delta éle é vinte, vezes cinquenta, vezes o alfa. [p=0.3] Junte primeiro os números redondos: {b}vinte vezes cinquenta dá mil, [p=0.1] que é {c}dez elevado a três. [p=0.3] {d}Dez elevado a três vezes dez elevado a menos cinco dá dez elevado a menos dois. [p=0.3] Fica {e}um vírgula dois vezes dez elevado a menos dois metros, [p=0.2] ou seja, {f}um vírgula dois centímetros."),
    dict(id="s10", block="exemplo", text="Parece pouco, [p=0.2] mas um trilho preso nas duas pontas, sem folga, {a}entorta. [p=0.3] Por isso, trilhos, pontes e calçadas têm {b}juntas de dilatação: [p=0.2] as frestas que deixam o material crescer sem quebrar."),
    # área e volume
    dict(id="s11", block="atalho", text="Agora, o atalho. [p=0.2] Uma chapa cresce em {a}duas direções, [p=0.1] e um bloco, em {b}três. [p=0.3] Por isso, na prática, o coeficiente de área, {c}beta, é dois alfa, [p=0.2] e o de volume, {d}gama, é três alfa."),
    dict(id="s12", block="atalho", text="As fórmulas têm a mesma cara: [p=0.2] {a}a variação da área é a área inicial, vezes beta, vezes delta tê; [p=0.2] {b}a variação do volume é o volume inicial, vezes gama, vezes delta tê. [p=0.3] Você só decora uma e {c}troca a letra. [p=0.3] {d}Não confunda: [p=0.1] se a questão já dá o beta ou o gama, use direto, sem multiplicar de novo."),
    # lâmina bimetálica
    dict(id="s13", block="fenomenos", text="As juntas são o primeiro fenômeno. [p=0.2] O segundo é {a}a lâmina bimetálica. [p=0.2] São {b}duas tiras de metais diferentes, coladas. [p=0.3] Ao esquentar, {c}a de alfa maior cresce mais [p=0.2] e {d}a lâmina se curva para o lado da que cresce menos. [p=0.3] Ela abre e fecha contatos em {e}ferros de passar e pisca-piscas."),
    # anomalia
    dict(id="s14", block="fenomenos", text="O terceiro: {a}a água é do contra. [p=0.2] {b}Entre zero e quatro graus Celsius, ao esquentar, ela encolhe. [p=0.3] A {c}quatro graus, ela ocupa o menor volume [p=0.1] e é a mais densa."),
    dict(id="s15", block="fenomenos", text="Num lago no inverno, {a}a água a quatro graus desce para o fundo. [p=0.2] A de cima esfria mais e {b}congela na superfície. [p=0.2] Como {c}o gelo boia, ele vira uma tampa, [p=0.2] e {d}os peixes continuam vivos lá embaixo."),
    # erro
    dict(id="s16", block="erro", text="Agora, o erro que mais derruba aluno: [p=0.2] {a}uma chapa com um furo no meio. [p=0.2] Esquentando a chapa, {b}o furo diminui? [p=0.3] {c}Não. [p=0.2] {d}O furo aumenta, [p=0.1] como se fosse feito do mesmo material da chapa. [p=0.3] {e}É por isso que se esquenta a tampa de metal de um pote de vidro para abrir: [p=0.2] o metal dilata mais que o vidro, e a tampa folga."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Uma barra de alumínio de {a}dois metros [p=0.1] tem alfa igual a {b}dois vírgula quatro vezes dez elevado a menos cinco por grau Celsius. [p=0.3] Ela vai de {c}vinte a setenta graus Celsius. [p=0.3] {d}Quanto ela cresce? [p=0.2] E {e}qual é o beta desse alumínio?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Delta tê é {a}setenta menos vinte, que dá cinquenta. [p=0.3] {b}Dois vezes cinquenta dá cem, [p=0.1] que é {c}dez elevado a dois. [p=0.2] {d}Dez elevado a dois vezes dez elevado a menos cinco dá dez elevado a menos três. [p=0.3] Fica {e}dois vírgula quatro vezes dez elevado a menos três metros, [p=0.2] ou seja, {f}dois vírgula quatro milímetros."),
    dict(id="s20", block="resposta", text="E o beta é {a}dois alfa: [p=0.2] {b}quatro vírgula oito vezes dez elevado a menos cinco por grau Celsius."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}delta éle igual a éle zero, alfa, delta tê; [p=0.2] {b}área, dois alfa; volume, três alfa; [p=0.2] e {c}o furo cresce junto com a chapa."),
    dict(id="s22", block="fim", text="Na próxima aula, você vai calcular {a}quanto calor é preciso para esquentar alguma coisa, [p=0.2] e descobrir por que {b}a areia da praia queima o pé e a água do mar não. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
