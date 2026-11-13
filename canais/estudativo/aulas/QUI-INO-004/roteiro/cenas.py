# Estudativo · QUI-INO-004 — Óxidos: ácidos, básicos e neutros (Química · Funções e Reações Inorgânicas · Ácidos, bases, sais e óxidos).
# Habilidade: classificar CO₂, SO₃, CaO e CO em óxido ácido, básico ou neutro e escrever a reação do SO₃ com a água.
# Pré-requisitos: QUI-INO-001, QUI-INO-002. Próxima: QUI-INO-005 (escala de pH e indicadores).
# Atenção: QUI-INO-003 (neutralização e sais) NÃO está em "Já ensinado" desta aula: a aula não fala de sal nem de neutralização.
# Fórmula com parênteses não é lida letra a letra: diz-se o nome e a fórmula fica na tela.
# Fatos: água com gás tem CO₂ dissolvido e é levemente ácida: CO₂ + H₂O → H₂CO₃. SO₃ + H₂O → H₂SO₄.
# CaO = cal viva (cal virgem); CaO + H₂O → Ca(OH)₂ (cal hidratada, ou cal apagada). Neutros: CO, NO, N₂O.
# CO = monóxido de carbono, tóxico. Prefixos: mono = 1, di = 2, tri = 3. Anfóteros (ZnO, Al₂O₃) ficam de fora.
# Na₂O + H₂O → 2 NaOH (exemplo). Questão inédita: K₂O básico; SO₂ ácido (SO₂ + H₂O → H₂SO₃); NO neutro.

TITULO = "Óxidos: ácidos, básicos e neutros"

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
    dict(id="s01", block="gancho", text="{a}A água com gás é um pouco ácida. [p=0.3] E {b}ninguém colocou ácido nela. [p=0.3] Só colocaram {c}gás carbônico. [p=0.3] {d}Um gás virou ácido dentro da água."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}reconhecer um óxido, [p=0.2] {b}dizer se ele é ácido, básico ou neutro, [p=0.2] e {c}escrever o que ele forma com a água."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre: [p=0.1] {a}ácido solta agá mais na água, e a fórmula começa com agá. [p=0.2] {b}Base solta ó agá menos, e a fórmula termina em ó agá. [p=0.3] E {c}na tabela periódica, os metais ficam à esquerda e no meio; [p=0.1] {d}os ametais, no canto de cima, à direita."),
    # o que é óxido
    dict(id="s04", block="oxido", text="{a}Óxido é um composto de dois elementos só, [p=0.1] {b}e um deles é o oxigênio. [p=0.3] {c}Cê ó dois, [p=0.1] {d}ésse ó três, [p=0.1] {e}cê á ó [p=0.1] {f}e cê ó são óxidos."),
    dict(id="s05", block="oxido", text="O nome conta os oxigênios: [p=0.1] {a}mono é um, di é dois, tri é três. [p=0.3] {b}Cê ó dois é o dióxido de carbono, o gás carbônico. [p=0.2] {c}Ésse ó três, o trióxido de enxofre. [p=0.2] {d}Cê ó, o monóxido de carbono. [p=0.2] {e}Com metal, diz-se só óxido de, e o metal: [p=0.1] cê á ó é o óxido de cálcio, a cal viva."),
    # óxido ácido
    dict(id="s06", block="acido", text="Para classificar, ponha o óxido na água e veja o que se forma. [p=0.3] {a}Óxido de ametal, como o de carbono ou o de enxofre, forma ácido. [p=0.2] Ele é um {b}óxido ácido."),
    dict(id="s07", block="acido", text="Veja a reação mais cobrada. [p=0.2] {a}Ésse ó três, [p=0.1] {b}mais agá dois ó, [p=0.1] {c}produz agá dois ésse ó quatro, [p=0.1] {d}o ácido sulfúrico. [p=0.3] {e}É assim que a fumaça com enxofre deixa a chuva ácida, assunto de outra aula."),
    dict(id="s08", block="acido", text="{a}E o gás carbônico com a água forma o ácido carbônico, agá dois cê ó três. [p=0.3] {b}Esse é o ácido da água com gás."),
    # óxido básico
    dict(id="s09", block="basico", text="{a}Óxido de metal, como o de cálcio, forma base. [p=0.2] Ele é um {b}óxido básico. [p=0.3] {c}Cê á ó, mais agá dois ó, {d}produz o hidróxido de cálcio. [p=0.3] {e}É a cal viva virando cal hidratada, a da obra."),
    dict(id="s10", block="basico", text="{a}Com o óxido de sódio, ene á dois ó, é igual. [p=0.2] {b}Com a água, ele forma o hidróxido de sódio, a soda cáustica. [p=0.3] {c}Metal no óxido, base na água, [p=0.1] com poucas exceções, assunto de outra aula."),
    # óxido neutro
    dict(id="s11", block="neutro", text="{a}E alguns óxidos de ametal não reagem com a água: [p=0.1] {b}não formam ácido, nem base. [p=0.2] São os {c}óxidos neutros. [p=0.3] Decore três: [p=0.1] {d}cê ó, [p=0.1] {e}ene ó [p=0.1] {f}e ene dois ó."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}chamar o cê ó de ácido, porque o carbono é ametal. [p=0.3] {b}O cê ó dois é ácido. [p=0.2] {c}Já o cê ó, com um oxigênio só, não reage com a água: [p=0.1] {d}é neutro. [p=0.2] {e}Neutro, mas muito tóxico: é o gás que mata em garagem fechada."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho de prova para escrever o ácido: [p=0.2] {a}junte os átomos do óxido com os da água, [p=0.1] {b}e ponha os agás na frente. [p=0.3] {c}Ésse ó três mais agá dois ó: [p=0.1] {d}dois hidrogênios, um enxofre, três mais um oxigênios: [p=0.1] {e}agá dois ésse ó quatro."),
    dict(id="s14", block="atalho", text="Funciona porque {a}a água entra inteira na molécula do ácido: [p=0.1] nenhum átomo some. [p=0.3] {b}No óxido básico, os ó agá vão para o fim: [p=0.1] {c}é o hidróxido do metal. [p=0.2] {d}E não compensa com os neutros: [p=0.1] eles não reagem."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Classifique em ácido, básico ou neutro: [p=0.2] {a}cá dois ó, [p=0.2] {b}ésse ó dois [p=0.2] {c}e ene ó. [p=0.3] E {d}escreva o ácido que o ésse ó dois forma com a água."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}O potássio é metal: cá dois ó é básico. [p=0.2] {b}O enxofre é ametal, e ésse ó dois não está entre os três neutros: [p=0.1] é ácido. [p=0.2] {c}Ene ó é um dos três neutros."),
    dict(id="s18", block="resposta", text="{a}Ésse ó dois mais agá dois ó: [p=0.1] {b}dois hidrogênios, [p=0.1] {c}um enxofre, [p=0.1] {d}dois mais um, três oxigênios. [p=0.3] {e}Agá dois ésse ó três."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}óxido de ametal forma ácido, [p=0.1] {b}óxido de metal forma base, [p=0.1] e {c}cê ó, ene ó e ene dois ó são neutros."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai medir quão ácida ou básica é uma solução: [p=0.2] {a}a escala de pê agá, [p=0.2] {b}e os indicadores, que mudam de cor. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
