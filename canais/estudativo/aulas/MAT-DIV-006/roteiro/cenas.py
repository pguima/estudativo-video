# Estudativo · MAT-DIV-006 — Problemas de MDC: partes iguais, as maiores possíveis (Matemática · Divisibilidade, MMC e MDC).
# Habilidade: cortar fitas de 72 cm e 120 cm em pedaços iguais, os maiores possíveis, reconhecendo pelo texto que o caso é de MDC.
# Pré-requisitos: MAT-DIV-004. Próxima: MAT-DIV-007.
# Ficha: MMC não está em "Já ensinado" aqui (a MAT-DIV-005 não é pré-requisito): só citado como assunto de outra aula.
# Fitas: MDC(72, 120) = 2·2·2·3 = 24 · 72 ÷ 24 = 3 · 120 ÷ 24 = 5 · 3 + 5 = 8 pedaços. Testes: 72 ÷ 30 = 2 resto 12; 12 cm serve (6 e 10 pedaços).
# Bandejas: 30 = 2·3·5 · 45 = 3·3·5 → 3·5 = 15 · 30 ÷ 15 = 2 · 45 ÷ 15 = 3.
# Questão: 63 = 3·3·7 · 84 = 2·2·3·7 → 3·7 = 21 kits · 63 ÷ 21 = 3 · 84 ÷ 21 = 4.

TITULO = "Problemas de MDC: partes iguais, as maiores possíveis"

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
    dict(id="s01", block="gancho", text="Duas fitas: {a}uma de setenta e dois centímetros, {b}outra de cento e vinte. [p=0.3] Você corta em pedaços iguais, os maiores possíveis, sem sobrar nada. [p=0.2] {c}Quantos pedaços saem?"),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você resolve isso {a}sem tentativa e erro, [p=0.2] e leva o {b}atalho de prova: a pista no texto que entrega o MDC."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}uma coisa: [p=0.2] {b}calcular o MDC de dois números. [p=0.3] Se faltar, procure a aula no canal."),
    # por que é MDC
    dict(id="s04", block="fitas", text="Antes da conta, entenda a história. [p=0.2] Para não sobrar nada, o tamanho do pedaço precisa {a}caber certinho em setenta e dois. [p=0.2] E {b}também em cento e vinte. [p=0.3] Caber certinho é ser {c}divisor."),
    dict(id="s05", block="fitas", text="Pedaços de trinta centímetros? [p=0.2] {a}Setenta e dois dividido por trinta deixa resto. [p=0.2] {b}Não serve. [p=0.3] Pedaços de doze? [p=0.2] {c}Serve nas duas fitas. [p=0.2] Mas {d}será que é o maior?"),
    dict(id="s06", block="fitas", text="O pedaço precisa ser {a}divisor das duas medidas, [p=0.2] e o {b}maior possível. [p=0.3] Isso é exatamente o {c}máximo divisor comum."),
    # conta
    dict(id="s07", block="conta", text="{a}Setenta e dois é dois vezes dois vezes dois vezes três vezes três. [p=0.2] {b}Cento e vinte é dois vezes dois vezes dois vezes três vezes cinco. [p=0.3] Em comum: {c}dois vezes dois vezes dois vezes três. [p=0.2] {d}Vinte e quatro centímetros."),
    dict(id="s08", block="conta", text="Só que a pergunta não é o tamanho. [p=0.2] É {a}quantos pedaços. [p=0.3] {b}Setenta e dois dividido por vinte e quatro: três pedaços. [p=0.2] {c}Cento e vinte dividido por vinte e quatro: cinco pedaços. [p=0.3] {d}Três mais cinco: oito pedaços."),
    # bandejas
    dict(id="s09", block="bandejas", text="O mesmo problema aparece com outra roupa. [p=0.2] Uma lanchonete tem {a}trinta pães de queijo e {b}quarenta e cinco coxinhas. [p=0.2] Quer montar {c}o maior número possível de bandejas iguais, sem sobrar nada."),
    dict(id="s10", block="bandejas", text="O número de bandejas precisa dividir {a}trinta e {b}quarenta e cinco. [p=0.3] É divisor comum, e o maior: {c}MDC. [p=0.3] Trinta é dois vezes três vezes cinco. [p=0.2] Quarenta e cinco é três vezes três vezes cinco. [p=0.2] Em comum, três vezes cinco: {d}quinze bandejas."),
    dict(id="s11", block="bandejas", text="Em cada bandeja: {a}trinta dividido por quinze, dois pães. [p=0.2] {b}Quarenta e cinco dividido por quinze, três coxinhas."),
    dict(id="s12", block="bandejas", text="Repare na diferença. [p=0.2] {a}Nas fitas, o MDC deu o tamanho de cada pedaço. [p=0.2] {b}Nas bandejas, deu a quantidade de bandejas. [p=0.3] Pense sempre {c}no que aquele número significa na história."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é {a}parar no MDC. [p=0.2] A pessoa acha {b}vinte e quatro e responde vinte e quatro. [p=0.3] Só que a pergunta era {c}quantos pedaços. [p=0.2] Vinte e quatro é o tamanho. [p=0.2] {d}A resposta é oito. [p=0.3] Antes de terminar, {e}releia o que foi pedido."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho, que é uma pista no texto. [p=0.2] Procure {a}três ideias juntas: [p=0.2] {b}partes iguais, [p=0.2] {c}sem sobra, [p=0.2] {d}o maior possível. [p=0.3] Apareceu isso, {e}é MDC."),
    dict(id="s15", block="atalho", text="Funciona porque cada ideia é um pedaço do nome. [p=0.2] {a}Sem sobra é divisor. [p=0.2] {b}Igual para todos é comum. [p=0.2] {c}O maior possível é máximo."),
    dict(id="s16", block="atalho", text="Quando não compensa? [p=0.2] Se o texto {a}já dá o tamanho do pedaço, não tem MDC: [p=0.2] é {b}só dividir. [p=0.3] E a palavra {c}maior, sozinha, não prova nada. [p=0.2] Confira se a história é mesmo {d}de repartir em partes iguais. [p=0.3] Coisas que se repetem no tempo pedem outra conta, assunto da próxima aula."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Uma loja tem {a}sessenta e três sabonetes e {b}oitenta e quatro cremes. [p=0.2] Quer montar {c}o maior número possível de kits iguais, sem sobrar nada. [p=0.3] {d}Quantos kits, e o que vai em cada um?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Kits iguais, sem sobra, o maior número possível: {a}MDC. [p=0.3] {b}Sessenta e três é três vezes três vezes sete. [p=0.2] {c}Oitenta e quatro é dois vezes dois vezes três vezes sete. [p=0.3] Em comum: {d}três vezes sete. [p=0.2] {e}Vinte e um kits."),
    dict(id="s20", block="resposta", text="Em cada kit: {a}sessenta e três dividido por vinte e um, três sabonetes. [p=0.2] {b}Oitenta e quatro dividido por vinte e um, quatro cremes."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}partes iguais, sem sobra, as maiores possíveis, é MDC. [p=0.2] E {b}sempre confira o que a pergunta quer de verdade."),
    dict(id="s22", block="fim", text="Na próxima aula, o caso contrário: {a}ônibus que saem de tempos em tempos e se encontram de novo. [p=0.2] É o problema de MMC, e você vai ver a diferença para este aqui. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
