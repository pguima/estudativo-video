# Estudativo · QUI-ELE-007 — Praticando: pilhas e corrosão (Química · Eletroquímica e Radioatividade · Pilhas e corrosão). Prática.
# Habilidade: calcular ddp, identificar polos e escolher a proteção de um metal em questões de prova.
# Pré-requisitos: QUI-ELE-001, 002, 015, 003, 004, 005, 006. Próxima: QUI-ELE-008 (eletrólise ígnea).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Quatro questões inéditas, criadas para esta aula.
# Q1: K₂Cr₂O₇ (dicromato de potássio, "cá dois cê erre dois ó sete"): 2(+1) + 2x + 7(−2) = 0 → 2x = 12 → x = +6;
#     no bafômetro antigo vira Cr³⁺: +6 → +3, se reduz, é o agente oxidante.
# Q2: Cu + Ag⁺ → Cu²⁺ + Ag: Cu perde 2, Ag⁺ ganha 1 → Cu + 2 Ag⁺ → Cu²⁺ + 2 Ag (carga +2 = +2).
# Q3: pilha Cu/Ag: 0,80 − 0,34 = 0,46 V; ânodo Cu (−) perde massa; cátodo Ag (+); e⁻ do cobre para a prata.
#     Armadilha: multiplicar o potencial da prata pelo 2 → 2 × 0,80 − 0,34 = 1,26 (errado).
# Q4: CuSO₄ em tanque de ferro: Cu²⁺ (+0,34) acima do Fe (−0,44) → reage, o tanque corrói (0,34 + 0,44 = 0,78 > 0).
#     Proteção do ferro: zinco (−0,76, abaixo) sim; estanho (−0,14, acima) não.

TITULO = "Praticando: pilhas e corrosão"

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
    dict(id="s01", block="gancho", text="{a}Quatro questões, [p=0.1] e cada uma usa uma ferramenta do módulo: [p=0.2] {b}Nox, {c}balanceamento, {d}pilha {e}e corrosão. [p=0.3] Resolva comigo, [p=0.1] e no fim você tem o módulo inteiro na mão."),
    # lembrete
    dict(id="s02", block="lembrete", text="As ferramentas: [p=0.2] {a}a soma dos Nox fecha em zero, ou na carga do íon. [p=0.2] {b}Nox subiu, a substância se oxidou e é o redutor. [p=0.2] {c}Elétrons perdidos igualam os ganhos. [p=0.2] {d}Dê dê pê é o maior potencial menos o menor. [p=0.2] {e}E o metal de sacrifício fica abaixo do ferro. [p=0.2] Se faltar alguma, procure no canal."),
    # questão 1
    dict(id="s03", block="q1", text="Questão um. [p=0.2] {a}O dicromato de potássio, cá dois cê erre dois ó sete, é um sal laranja. [p=0.2] {b}O cê erre é o cromo. [p=0.3] {c}Qual é o Nox do cromo? [p=0.2] {d}No bafômetro antigo, ele vira cromo três mais, verde. [p=0.2] {e}O cromo se oxida ou se reduz?"),
    dict(id="s04", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="r1", text="Vamos lá. [p=0.2] {a}Dois potássios dão mais dois. [p=0.1] {b}Sete oxigênios dão menos catorze. [p=0.2] {c}Para fechar em zero, os cromos somam mais doze. [p=0.3] {d}Mas são dois cromos: [p=0.1] {e}doze dividido por dois, cada um é mais seis."),
    dict(id="s06", block="r1", text="{a}De mais seis para mais três, o Nox desceu: [p=0.1] {b}o cromo se reduz. [p=0.2] {c}Então o dicromato é o agente oxidante. [p=0.3] {d}A pegadinha é parar no doze: [p=0.1] {e}o índice dois vale para o cromo também."),
    # questão 2
    dict(id="s07", block="q2", text="Questão dois. [p=0.2] {a}Um fio de cobre numa solução de nitrato de prata se cobre de cristais de prata. [p=0.3] {b}Cobre e íon prata, de carga mais um, [p=0.1] dão íon cobre, de carga dois mais, e prata. [p=0.3] {c}Balanceie pela oxirredução."),
    dict(id="s08", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="r2", text="Vamos lá. [p=0.2] {a}O cobre vai de zero a mais dois: perde dois. [p=0.2] {b}A prata vai de mais um a zero: ganha um. [p=0.3] {c}Cruze: um cobre e dois íons prata. [p=0.3] {d}Um cobre e dois íons prata [p=0.1] dão um íon cobre e duas pratas metálicas."),
    dict(id="s10", block="r2", text="{a}Confira pela carga: [p=0.1] {b}dois íons de carga mais um, à esquerda, dão mais dois. [p=0.2] {c}À direita, um íon de carga dois mais. [p=0.2] {d}Fechou."),
    # questão 3
    dict(id="s11", block="q3", text="Questão três. [p=0.2] {a}Agora, a mesma reação vira pilha: [p=0.1] cobre de um lado, prata do outro. [p=0.3] {b}O cobre tem potencial de mais zero vírgula trinta e quatro, [p=0.1] {c}a prata, de mais zero vírgula oitenta. [p=0.3] {d}Qual é a dê dê pê? [p=0.2] {e}Quem é o polo negativo, [p=0.1] {f}e qual placa perde massa?"),
    dict(id="s12", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="r3", text="Vamos lá. [p=0.2] {a}A prata está mais alta: se reduz, é o cátodo, o polo positivo. [p=0.3] {b}O cobre se oxida: é o ânodo, o polo negativo. [p=0.3] {c}Zero vírgula oitenta menos zero vírgula trinta e quatro [p=0.1] {d}dá zero vírgula quarenta e seis volt."),
    dict(id="s14", block="r3", text="{a}A placa que perde massa é a de cobre, o ânodo, [p=0.1] {b}e os elétrons vão do cobre para a prata. [p=0.3] {c}E a armadilha: [p=0.1] {d}o dois do balanceamento não multiplica o potencial. [p=0.2] {e}Quem faz duas vezes zero vírgula oitenta acha um vírgula vinte e seis, e erra."),
    # questão 4
    dict(id="s15", block="q4", text="Questão quatro. [p=0.2] {a}Uma fábrica quer guardar sulfato de cobre num tanque de ferro. [p=0.3] {b}Pode? [p=0.2] {c}E, para proteger um cano de ferro enterrado com um metal de sacrifício, [p=0.1] {d}é melhor o zinco, com menos zero vírgula setenta e seis, [p=0.1] {e}ou o estanho, com menos zero vírgula catorze?"),
    dict(id="s16", block="q4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="r4", text="Vamos lá. [p=0.2] {a}O íon cobre, em mais zero vírgula trinta e quatro, está acima do ferro, em menos zero vírgula quarenta e quatro. [p=0.3] {b}O íon de cima reage com o metal de baixo: [p=0.1] {c}o ferro do tanque vai sendo corroído, e o cobre se deposita na parede. [p=0.2] {d}Não pode."),
    dict(id="s18", block="r4", text="{a}Para o sacrifício, o metal tem de estar abaixo do ferro. [p=0.2] {b}O zinco está: ele protege. [p=0.2] {c}O estanho está acima: [p=0.1] {d}ligado ao ferro, faria o ferro virar o ânodo e enferrujar mais rápido."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo o módulo: [p=0.1] {a}o Nox mostra quem perde e quem ganha elétrons, [p=0.1] os elétrons perdidos igualam os ganhos, [p=0.1] {b}e a escada de potenciais diz quem se oxida, a dê dê pê e quem se sacrifica."),
    dict(id="s20", block="fim", text="Na próxima aula, a corrente vem de fora {a}e força uma reação que não aconteceria sozinha: [p=0.2] {b}é a eletrólise, que faz o alumínio da latinha. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
