# Estudativo · QUI-ORG-005 — Praticando: cadeias e hidrocarbonetos (Química · Química Orgânica · Cadeias carbônicas e hidrocarbonetos).
# Habilidade: classificar e nomear moléculas de combustíveis e fármacos em questões de prova.
# Pré-requisitos: QUI-ORG-001 a 004. Próxima: QUI-ORG-006 (álcool, fenol e éter).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Prática: 4 questões inéditas, criadas para esta aula.
# Q1: gás do isqueiro = butano e isobutano (2-metilpropano), os dois C4H10 (2·4+2 = 10). A isomeria fica para a QUI-ORG-014.
# Q2: limoneno (óleo da casca da laranja), C10H16: 2·10+2 = 22; −2 do anel, −2 −2 das duas duplas = 16. Mista, ramificada,
#     insaturada, homogênea, não aromática. "O anel tira dois" é dito aqui pela primeira vez, com o motivo.
# Q3: éter dietílico (anestésico desde 1846) CH3–CH2–O–CH2–CH3: aberta, normal, saturada, heterogênea; os 4 carbonos são primários.
# Q4: tolueno (solvente de tintas) = metilbenzeno, C7H8 (5 H no anel + 3 no metil).

TITULO = "Praticando: cadeias e hidrocarbonetos"

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
    dict(id="s01", block="gancho", text="{a}Isqueiro, [p=0.1] {b}casca de laranja, [p=0.1] {c}anestesia [p=0.1] {d}e tinta. [p=0.3] Em cada um, uma molécula que cai em prova. [p=0.2] {e}Hoje são quatro questões, e você resolve todas com o que já viu nesta trilha."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar [p=0.1] {a}os hidrogênios escondidos do bastão, [p=0.1] {b}as quatro perguntas da cadeia [p=0.1] e {c}as regras do nome. [p=0.2] Se faltar alguma aula, procure no canal. [p=0.2] {d}Em cada questão, pause e tente antes de ver a resposta."),
    # questão 1
    dict(id="s03", block="q1", text="{a}Questão um. [p=0.2] O gás do isqueiro é uma mistura de duas moléculas de quatro carbonos: [p=0.1] {b}o butano, em fila, [p=0.1] {c}e este outro, com um galho. [p=0.3] {d}Qual é a fórmula molecular de cada um? [p=0.2] {e}E qual é o nome oficial do ramificado?"),
    dict(id="s04", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="r1", text="{a}As duas moléculas têm quatro carbonos e só ligações simples. [p=0.2] Pelo atalho, {b}o dobro de quatro é oito, mais dois, dez: [p=0.1] {c}as duas são cê quatro agá dez. [p=0.3] {d}No ramificado, a maior fila tem três carbonos: propano. [p=0.2] {e}O galho de um carbono fica no carbono dois: [p=0.1] {f}dois metilpropano, ou só metilpropano, porque o galho não tem outro lugar."),
    dict(id="s06", block="r1", text="{a}Mesma fórmula, desenhos diferentes. [p=0.2] Isso tem nome, e é assunto de outra aula."),
    # questão 2
    dict(id="s07", block="q2", text="{a}Questão dois. [p=0.2] {b}O limoneno dá o cheiro da casca da laranja. [p=0.3] {c}Qual é a fórmula molecular dele? [p=0.2] {d}E como se classifica a cadeia?"),
    dict(id="s08", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="r2", text="Conte os carbonos: [p=0.1] {a}seis no anel, [p=0.1] {b}um no galho de cima [p=0.1] {c}e três no galho de baixo. [p=0.2] {d}Dá dez carbonos."),
    dict(id="s10", block="r2", text="Os hidrogênios pelo atalho: [p=0.1] {a}o dobro de dez é vinte, mais dois, vinte e dois. [p=0.3] {b}O anel tira dois, como uma dupla: [p=0.1] fechar o anel liga duas pontas, e cada uma perde um hidrogênio. [p=0.3] {c}E cada uma das duas duplas tira mais dois. [p=0.2] {d}Vinte e dois menos seis dá dezesseis: [p=0.1] {e}cê dez agá dezesseis."),
    dict(id="s11", block="r2", text="A cadeia: [p=0.1] {a}tem anel com partes abertas presas a ele: mista. [p=0.1] Alguns livros dizem só fechada. [p=0.2] {b}Tem galhos: ramificada. [p=0.2] {c}Tem duplas entre carbonos: insaturada. [p=0.2] {d}Só carbono e hidrogênio: homogênea. [p=0.2] {e}E não é aromática, porque o anel tem uma dupla só."),
    # questão 3
    dict(id="s12", block="q3", text="{a}Questão três. [p=0.2] {b}O éter comum já foi usado como anestésico nas cirurgias: [p=0.1] {c}cê agá três, cê agá dois, ó, cê agá dois, cê agá três. [p=0.3] {d}Classifique a cadeia [p=0.1] {e}e diga se cada carbono é primário, secundário ou terciário."),
    dict(id="s13", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="r3", text="{a}Sem anel: aberta. [p=0.2] {b}Duas pontas: normal. [p=0.2] {c}Sem dupla: saturada. [p=0.2] {d}E o oxigênio está entre dois carbonos: heterogênea."),
    dict(id="s15", block="r3", text="{a}Nos carbonos, mora a pegadinha. [p=0.2] {b}O cê agá dois está preso ao oxigênio, mas o oxigênio não conta. [p=0.2] {c}Ele tem um só carbono vizinho: [p=0.1] {d}é primário. [p=0.3] {e}Os quatro carbonos são primários."),
    # questão 4
    dict(id="s16", block="q4", text="{a}Questão quatro. [p=0.2] {b}O tolueno, um solvente de tintas, é um anel de benzeno com um galho de um carbono. [p=0.3] {c}Qual é o nome oficial dele? [p=0.2] {d}E a fórmula molecular?"),
    dict(id="s17", block="q4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="r4", text="{a}O galho de um carbono é um metil, [p=0.1] e a cadeia principal é o benzeno. [p=0.2] {b}O nome é metilbenzeno, sem número: [p=0.1] {c}com um galho só, qualquer carbono do anel pode ser o carbono um."),
    dict(id="s19", block="r4", text="{a}A fórmula: [p=0.1] sete carbonos. [p=0.2] {b}No anel, cada carbono tem a dupla e uma simples: [p=0.1] falta um, um hidrogênio. [p=0.2] {c}Menos o que segura o galho, que já tem as quatro ligações. [p=0.3] {d}Cinco hidrogênios no anel [p=0.1] {e}e três no metil: [p=0.1] {f}cê sete agá oito."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo o método: [p=0.1] {a}conte os carbonos de ponta e de dobra, [p=0.1] {b}confira os hidrogênios pelo atalho, [p=0.1] {c}faça as quatro perguntas da cadeia [p=0.1] e {d}dê o nome pela maior fila."),
    dict(id="s21", block="fim", text="Na próxima aula, começam as funções orgânicas: [p=0.2] {a}o álcool, o fenol e o éter, como o da questão três, [p=0.1] {b}todos com oxigênio. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
