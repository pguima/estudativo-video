# Estudativo · QUI-MIS-005 — Praticando: substâncias, misturas e estados físicos (Química · Matéria e Misturas · Matéria, substâncias e estados físicos).
# Habilidade: classificar materiais do dia a dia e ler gráficos de aquecimento em questões de prova.
# Pré-requisitos: QUI-MIS-001, QUI-MIS-002, QUI-MIS-003, QUI-MIS-004. Próxima: QUI-MIS-006 (separar sólidos).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Prática: quatro questões inéditas, criadas para esta aula.
# Cobertura: Q1 desenho de bolinhas (MIS-001/002, alótropos misturados), Q2 fases e componentes com gelo (MIS-002/003),
# Q3 espelho embaçado (MIS-003), Q4 curva da solda sem chumbo (MIS-004, eutética, 217 °C).
# Fatos: gelo é água no estado sólido, então água com gelo é uma substância só em duas fases; solda de estanho e chumbo
# funde a 183 °C; a solda sem chumbo de estanho, prata e cobre (eutética) funde a cerca de 217 °C.

TITULO = "Praticando: substâncias, misturas e estados físicos"

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
    dict(id="s01", block="gancho", text="{a}Quatro questões, [p=0.1] {b}cada uma com uma pegadinha que derruba muita gente. [p=0.3] {c}Pegue papel e caneta: [p=0.1] você tenta primeiro, e depois a gente resolve junto."),
    dict(id="s02", block="gancho", text="Você vai precisar de {a}substância e mistura, [p=0.1] {b}fases, [p=0.1] {c}mudanças de estado [p=0.1] e {d}curva de aquecimento. [p=0.3] Se faltar alguma dessas aulas, procure no canal."),
    # Q1
    dict(id="s03", block="q1", text="{a}Questão um. [p=0.2] Os quadros mostram as moléculas de quatro sistemas. [p=0.2] {b}No quadro á, só moléculas de ó dois. [p=0.2] {c}No quadro bê, só agá dois ó. [p=0.2] {d}No quadro cê, agá dois ó e ó dois misturados. [p=0.2] {e}No quadro dê, ó dois e ó três. [p=0.3] {f}Qual é substância composta? E quais são misturas?"),
    dict(id="s04", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="q1", text="{a}Conte os tipos de molécula em cada quadro. [p=0.2] {b}O quadro á tem um tipo, com um elemento só: substância simples. [p=0.2] {c}O quadro bê tem um tipo, com dois elementos: [p=0.1] é a substância composta."),
    dict(id="s06", block="q1", text="{a}O quadro cê tem dois tipos: mistura. [p=0.3] {b}E o quadro dê é a pegadinha. [p=0.2] Ó dois e ó três são do mesmo elemento, [p=0.1] {c}mas são dois tipos de molécula, duas substâncias. [p=0.2] {d}Então o quadro dê também é mistura: uma mistura de alótropos."),
    # Q2
    dict(id="s07", block="q2", text="{a}Questão dois. [p=0.2] {b}Um copo tem água com sal dissolvido, [p=0.1] {c}duas pedras de gelo [p=0.1] {d}e uma camada de óleo. [p=0.3] {e}Quantas fases e quantos componentes?"),
    dict(id="s08", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="q2", text="Fases: [p=0.1] {a}a água com sal é uma. [p=0.2] {b}O óleo é outra. [p=0.2] {c}E o gelo é a terceira. [p=0.3] {d}As duas pedras contam uma vez só, porque são a mesma parte, com o mesmo aspecto: [p=0.1] {e}três fases."),
    dict(id="s10", block="q2", text="Componentes: [p=0.1] {a}água, sal e óleo. [p=0.3] {b}E o gelo? [p=0.2] {c}Gelo é água no estado sólido: [p=0.1] não é um componente novo. [p=0.3] {d}Três componentes. [p=0.2] {e}Quem contou o gelo chegou a quatro."),
    # Q3
    dict(id="s11", block="q3", text="{a}Questão três. [p=0.2] {b}Depois de um banho quente, o espelho do banheiro fica embaçado. [p=0.3] {c}Qual mudança de estado aconteceu no espelho? [p=0.2] {d}E ela absorve ou libera calor?"),
    dict(id="s12", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="q3", text="{a}O vapor de água do banho, que é invisível, encostou no espelho frio [p=0.1] {b}e virou gotinhas de água líquida. [p=0.3] {c}De gás para líquido: [p=0.1] {d}condensação."),
    dict(id="s14", block="q3", text="{a}Na escada, ela desce: [p=0.1] {b}libera calor. [p=0.3] {c}O espelho recebe esse calor e até esquenta um pouco. [p=0.3] {d}A pegadinha é dizer evaporação: [p=0.1] a evaporação aconteceu no chuveiro, não no espelho."),
    # Q4
    dict(id="s15", block="q4", text="{a}Questão quatro. [p=0.2] O gráfico mostra o aquecimento de uma solda sem chumbo, de estanho, prata e cobre. [p=0.2] {b}A linha deita nos duzentos e dezessete graus. [p=0.2] {c}Depois, a fervura acontece com a temperatura subindo. [p=0.3] {d}Qual é o ponto de fusão? [p=0.2] {e}E a solda é substância pura ou mistura?"),
    dict(id="s16", block="q4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="q4", text="{a}O patamar está nos duzentos e dezessete graus, no trecho de baixo: [p=0.1] {b}esse é o ponto de fusão. [p=0.3] {c}A ebulição sobe: não tem patamar."),
    dict(id="s18", block="q4", text="{a}Só o patamar da fusão: [p=0.1] {b}é uma mistura eutética, a que funde bem. [p=0.3] {c}A pegadinha é ver o patamar e dizer substância pura. [p=0.2] {d}Pura precisaria de dois patamares."),
    # fechamento
    dict(id="s19", block="fim", text="As quatro pegadinhas, em uma frase cada: [p=0.2] {a}mesmo elemento não garante substância pura; [p=0.2] {b}gelo é água; [p=0.2] {c}o embaçado é condensação; [p=0.2] {d}e um patamar só não é pura."),
    dict(id="s20", block="fim", text="Na próxima aula, você começa a separar misturas: [p=0.2] {a}da peneira ao ímã, os métodos para sólidos. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
