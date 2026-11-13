# Estudativo · QUI-INO-006 — Praticando: ácidos, bases, sais e óxidos (Química · Funções e Reações Inorgânicas · Ácidos, bases, sais e óxidos).
# Habilidade: reconhecer funções inorgânicas em produtos do dia a dia e prever a neutralização.
# Pré-requisitos: QUI-INO-001, 002, 003, 004, 005, 007, 013. Próxima: QUI-INO-008 (balancear por tentativas).
# Aula de prática: cinco questões inéditas no lugar do conteúdo, cobrindo o módulo. Q5: HNO₃ 3 − 1 = 2 forte; H₂CO₃ fraco (exceção); KOH + HNO₃ → KNO₃ + H₂O.
# Fórmula com parênteses não é lida letra a letra: diz-se o nome e a fórmula fica na tela.
# Fatos: HCl comercial = ácido muriático; NaOH = soda cáustica; NaCl = sal de cozinha; CaO = cal viva.
# Al(OH)₃ = hidróxido de alumínio, princípio de antiácidos: Al(OH)₃ + 3 HCl → AlCl₃ + 3 H₂O.
# Ar expirado tem CO₂: CO₂ + H₂O → H₂CO₃ (ácido fraco): repolho vai para o vermelho/rosa; fenolftaleína incolor.
# CaO + H₂O → Ca(OH)₂: base, fenolftaleína rosa. NH₃ + HCl → NH₄⁺ + Cl⁻ (pares HCl/Cl⁻ e NH₄⁺/NH₃).

TITULO = "Praticando: ácidos, bases, sais e óxidos"

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
    dict(id="s01", block="gancho", text="{a}Ácido muriático, soda cáustica, sal de cozinha, cal viva. [p=0.3] {b}Tudo isso cabe em quatro gavetas: [p=0.1] {c}ácido, base, sal e óxido. [p=0.3] {d}Hoje são cinco questões para você treinar com coisas de casa."),
    # lembrete
    dict(id="s02", block="lembrete", text="Antes, as quatro pistas da fórmula. [p=0.2] {a}Começa com agá e solta agá mais na água: ácido. [p=0.2] {b}Termina em ó agá: base. [p=0.2] {c}Dois elementos, um deles oxigênio: óxido. [p=0.2] {d}Metal com o íon negativo de um ácido: sal."),
    # questão 1
    dict(id="s03", block="q1", text="Questão um. [p=0.2] Classifique cada produto em ácido, base, sal ou óxido. [p=0.2] {a}O ácido muriático, agá cê éle. [p=0.2] {b}A soda cáustica, ene á ó agá. [p=0.2] {c}O sal de cozinha, ene á cê éle. [p=0.2] {d}E a cal viva, cê á ó."),
    dict(id="s04", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="r1", text="Vamos lá. [p=0.2] {a}Agá cê éle começa com agá: ácido. [p=0.2] {b}Ene á ó agá termina em ó agá: base. [p=0.3] {c}Ene á cê éle tem o sódio, um metal, e o cloreto, o íon que sobra do ácido clorídrico: [p=0.1] sal. [p=0.3] {d}E cê á ó tem dois elementos, um deles o oxigênio: [p=0.1] {e}óxido, e básico, porque o cálcio é metal."),
    # questão 2
    dict(id="s06", block="q2", text="Questão dois. [p=0.2] {a}Um antiácido tem hidróxido de alumínio, que está na tela. [p=0.2] {b}Ele reage com o ácido clorídrico do estômago. [p=0.3] {c}Qual sal se forma? [p=0.2] E {d}quantas moléculas de água saem para cada hidróxido de alumínio?"),
    dict(id="s07", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="r2", text="Vamos lá. [p=0.2] {a}O alumínio vira á éle três mais. [p=0.2] {b}O ácido dá o cloreto, cê éle menos. [p=0.3] {c}Para zerar as cargas, um alumínio e três cloretos: [p=0.1] {d}á éle cê éle três, o cloreto de alumínio."),
    dict(id="s09", block="r2", text="{a}A base tem três ó agá menos. [p=0.2] {b}Cada um pede um agá mais, de uma molécula de agá cê éle. [p=0.3] {c}Três íons agá mais com três íons ó agá menos: [p=0.1] {d}três moléculas de água. [p=0.3] {e}É uma neutralização: ácido mais base dá sal mais água."),
    # questão 3
    dict(id="s10", block="q3", text="Questão três. [p=0.2] {a}Você sopra por um canudo dentro de um copo de água com repolho roxo. [p=0.2] {b}O ar que sai do pulmão tem gás carbônico. [p=0.3] {c}A cor vai para o lado do vermelho ou do verde? [p=0.3] E {d}num copo de água com cal viva e fenolftaleína, qual é a cor?"),
    dict(id="s11", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="r3", text="Vamos lá. [p=0.2] {a}O gás carbônico é um óxido ácido. [p=0.2] {b}Com a água, ele forma o ácido carbônico. [p=0.3] {c}A água fica um pouco ácida, e o repolho vai para o lado do vermelho."),
    dict(id="s13", block="r3", text="{a}A cal viva é um óxido básico. [p=0.2] {b}Com a água, ela forma o hidróxido de cálcio, uma base. [p=0.3] {c}O pê agá passa de sete, e a fenolftaleína fica rosa."),
    # questão 4
    dict(id="s14", block="q4", text="Questão quatro. [p=0.2] {a}Na reação ene agá três, mais agá cê éle, [p=0.1] {b}que produz ene agá quatro mais e cê éle menos: [p=0.3] {c}quem é o ácido de Brônsted, [p=0.1] e quais são os dois pares conjugados?"),
    dict(id="s15", block="q4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="r4", text="Vamos lá. [p=0.2] {a}O agá cê éle doou o agá mais: [p=0.1] é o ácido. [p=0.2] {b}A amônia recebeu: [p=0.1] é a base. [p=0.3] {c}Tire um agá do agá cê éle: [p=0.1] cê éle menos. [p=0.1] É o primeiro par. [p=0.3] {d}Ponha um agá na amônia: [p=0.1] ene agá quatro mais. [p=0.1] É o segundo par."),
    # questão 5
    dict(id="s17", block="q5", text="Questão cinco. [p=0.2] {a}Compare o ácido nítrico, agá ene ó três, e o ácido carbônico, agá dois cê ó três. [p=0.3] {b}Classifique cada um em forte, moderado ou fraco. [p=0.2] E {c}que sal o ácido nítrico forma com o hidróxido de potássio? Diga o nome."),
    dict(id="s18", block="q5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="r5", text="Vamos lá. [p=0.2] {a}Nítrico: três oxigênios menos um hidrogênio dá dois: forte. [p=0.3] {b}O carbônico é a exceção da regra: é fraco. [p=0.3] {c}O potássio dá o cá mais, e o nítrico dá o nitrato, ene ó três menos: [p=0.1] {d}cá ene ó três, o nitrato de potássio."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}a fórmula diz a função, [p=0.1] {b}ácido mais base dá sal mais água, [p=0.1] {c}quase todo óxido de ametal deixa a água ácida, e o de metal deixa básica."),
    dict(id="s21", block="fim", text="Na próxima aula, começa um módulo novo: [p=0.2] {a}você vai aprender a balancear uma equação por tentativas, [p=0.2] {b}na ordem certa dos elementos. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
