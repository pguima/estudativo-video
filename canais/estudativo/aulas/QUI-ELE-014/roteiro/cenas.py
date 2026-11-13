# Estudativo · QUI-ELE-014 — Praticando: eletrólise e radioatividade (Química · Eletroquímica e Radioatividade · Radioatividade).
# Prática. Habilidade: resolver contas de Faraday, decaimento e meia-vida em questões de prova.
# Pré-requisitos: QUI-ELE-008, 009, 010, 011, 012, 013. Próxima: nenhuma (última da trilha).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Quatro questões inéditas, criadas para esta aula.
# Q1: CaCl₂ fundido → cátodo Ca (Ca²⁺ + 2 e⁻ → Ca), ânodo Cl₂. Em água → cátodo H₂ (família 2 perde para a água), ânodo Cl₂.
# Q2: 3,175 g de Cu ÷ 63,5 = 0,05 mol Cu → × 2 = 0,1 mol e⁻ → 0,1 × 96.500 = 9.650 C → t = 9.650 ÷ 5 = 1.930 s.
#     Erro (sem o 2): 0,05 mol e⁻ → 4.825 C → 965 s, a metade.
# Q3: ²²⁶₈₈Ra → ⁴₂α + ²²²₈₆Rn (radônio, gás). Depois, ²¹⁴₈₂Pb → ⁰₋₁β + ²¹⁴₈₃Bi (bismuto).
# Q4: Cs-137, meia-vida de cerca de 30 anos (30,2). 100 g em 1987; em 2077 passaram 90 anos = 3 meias-vidas → 12,5 g.
#     Erro: 100 − 3 × 50 → "acabou". Fato: em Goiânia, a cápsula tinha cerca de 19 g de cloreto de césio-137; os 100 g são da questão.

TITULO = "Praticando: eletrólise e radioatividade"

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
    dict(id="s01", block="gancho", text="{a}Quatro questões para fechar a trilha: [p=0.2] {b}uma de eletrólise, {c}uma de Faraday, {d}uma de decaimento {e}e uma de meia-vida. [p=0.3] Resolva comigo, e no fim você tem a trilha inteira na mão."),
    # lembrete
    dict(id="s02", block="lembrete", text="As ferramentas: [p=0.2] {a}cátion vai ao cátodo, o negativo; [p=0.1] na água, nas famílias um e dois e no alumínio, sai hidrogênio no cátodo. [p=0.2] No ânodo, ânion com oxigênio dá oxigênio; sem oxigênio, sai o próprio ânion, como o cloro. [p=0.3] {b}Carga é corrente vezes tempo, e noventa e seis mil e quinhentos coulombs são um mol de elétrons. [p=0.3] {c}A alfa tira quatro da massa e dois do número atômico; [p=0.1] a beta sobe o número atômico em um. [p=0.3] {d}E cada meia-vida corta pela metade o que sobrou. [p=0.2] Se faltar alguma, procure no canal."),
    # questão 1
    dict(id="s03", block="q1", text="Questão um. [p=0.2] {a}O cálcio metálico se faz pela eletrólise do cloreto de cálcio derretido. [p=0.3] {b}O que sai no cátodo e no ânodo? [p=0.2] {c}E se o mesmo sal estivesse dissolvido em água?"),
    dict(id="s04", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="r1", text="Vamos lá. [p=0.2] {a}Derretido, não há água para disputar. [p=0.1] {b}O cálcio dois mais vai ao cátodo e vira cálcio metálico. [p=0.2] {c}O cloreto vai ao ânodo e sai gás cloro."),
    dict(id="s06", block="r1", text="{a}Na água, o cálcio é da família dois: [p=0.1] {b}perde a disputa, e sai gás hidrogênio no cátodo. [p=0.3] {c}O cloreto não tem oxigênio: [p=0.1] {d}continua saindo cloro no ânodo. [p=0.3] {e}Só o cátodo mudou."),
    # questão 2
    dict(id="s07", block="q2", text="Questão dois. [p=0.2] {a}Quanto tempo uma corrente de cinco ampères leva {b}para depositar três vírgula cento e setenta e cinco gramas de cobre? [p=0.3] {c}Um mol de cobre tem sessenta e três vírgula cinco gramas, [p=0.1] {d}e o íon é o cobre dois mais."),
    dict(id="s08", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="r2", text="Vamos lá, pelo caminho de volta. [p=0.2] {a}Três vírgula cento e setenta e cinco é um vigésimo de sessenta e três vírgula cinco: [p=0.1] {b}zero vírgula zero cinco mol de cobre. [p=0.3] {c}Cada cobre pede dois elétrons: [p=0.1] {d}zero vírgula um mol de elétrons."),
    dict(id="s10", block="r2", text="{a}Um décimo de mol de elétrons é um décimo de noventa e seis mil e quinhentos: [p=0.1] {b}nove mil seiscentos e cinquenta coulombs. [p=0.3] {c}O tempo é a carga dividida pela corrente: [p=0.1] {d}nove mil seiscentos e cinquenta dividido por cinco {e}dá mil novecentos e trinta segundos. [p=0.3] {f}Quem esquece a carga dois do íon acha a metade: novecentos e sessenta e cinco segundos."),
    # questão 3
    dict(id="s11", block="q3", text="Questão três. [p=0.2] {a}O rádio duzentos e vinte e seis, com número atômico oitenta e oito, solta uma alfa. [p=0.3] {b}Que massa e que número atômico tem o núcleo que sobra? [p=0.3] {c}E o chumbo duzentos e catorze, com número atômico oitenta e dois, solta uma beta: [p=0.1] {d}que núcleo ele vira?"),
    dict(id="s12", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="r3", text="Vamos lá. [p=0.2] {a}A alfa tira quatro da massa: [p=0.1] duzentos e vinte e seis menos quatro, {b}duzentos e vinte e dois. [p=0.2] {c}E tira dois do número atômico: [p=0.1] {d}oitenta e seis. [p=0.3] {e}É o radônio, um gás radioativo."),
    dict(id="s14", block="r3", text="{a}A beta não mexe na massa: continua duzentos e catorze. [p=0.2] {b}O número atômico sobe um: oitenta e três. [p=0.3] {c}É o bismuto duzentos e catorze."),
    # questão 4
    dict(id="s15", block="q4", text="Questão quatro. [p=0.2] {a}O césio cento e trinta e sete, do acidente de Goiânia, tem meia-vida de cerca de trinta anos. [p=0.3] {b}Imagine cem gramas dele em mil novecentos e oitenta e sete. [p=0.2] {c}Quanto restará em dois mil e setenta e sete?"),
    dict(id="s16", block="q4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="r4", text="Vamos lá. [p=0.2] {a}De mil novecentos e oitenta e sete a dois mil e setenta e sete, [p=0.1] {b}passam noventa anos. [p=0.2] {c}Noventa dividido por trinta: [p=0.1] {d}três meias-vidas."),
    dict(id="s18", block="r4", text="{a}Cem vira cinquenta, que vira vinte e cinco, [p=0.1] {b}que vira doze e meio: restam doze vírgula cinco gramas. [p=0.3] {c}A armadilha é tirar cinquenta a cada trinta anos [p=0.1] {d}e achar que acabou em sessenta. [p=0.2] {e}Cada meia-vida corta a metade do que sobrou."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo a trilha: [p=0.1] {a}na eletrólise, a carga conta os elétrons, e a carga do íon diz quantos cada átomo pede; [p=0.1] {b}no núcleo, as somas de cima e de baixo fecham; [p=0.1] {c}e o tempo se conta em metades."),
    dict(id="s20", block="fim", text="Você chegou ao fim da trilha de eletroquímica e radioatividade. [p=0.2] {a}Revise as aulas que ficaram difíceis, na playlist da trilha. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
