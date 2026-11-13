# Estudativo · QUI-MIS-003 — Estados físicos e mudanças de estado (Química · Matéria e Misturas · Matéria, substâncias e estados físicos).
# Habilidade: nomear as seis mudanças de estado, dizer em quais o material absorve calor e explicar sólido, líquido e gás
# pela agitação das partículas.
# Pré-requisitos: QUI-MIS-001. Próxima: QUI-MIS-004 (curva de aquecimento: pura ou mistura).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Nomes usados (os mesmos das aulas seguintes): fusão, solidificação, vaporização (evaporação, ebulição, calefação),
# condensação (ou liquefação), sublimação e ressublimação (gás → sólido). Absorvem calor: fusão, vaporização, sublimação.
# Fatos: naftalina sublima; gelo seco é gás carbônico sólido e sublima; o gelo que cresce na parede do congelador vem do vapor
# do ar (ressublimação); a "fumaça" branca da chaleira é água líquida em gotinhas: o vapor de água é invisível.
# Só MIS-001 está ensinada: sem números de temperatura (a curva é a próxima aula), sem "substância pura".

TITULO = "Estados físicos e mudanças de estado"

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
    dict(id="s01", block="gancho", text="{a}A roupa seca no varal sem a água ferver. [p=0.3] {b}A bolinha de naftalina some do armário sem nunca virar líquido. [p=0.3] {c}E a fumacinha branca da chaleira não é gás. [p=0.3] {d}O que está acontecendo?"),
    dict(id="s02", block="gancho", text="{a}Nesta aula, você vai entender {b}sólido, líquido e gás pelas partículas, [p=0.2] {c}dar nome às seis mudanças de estado [p=0.2] e dizer {d}em quais o material recebe calor."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula passada, você só precisa de uma ideia: [p=0.2] {a}tudo é feito de partículas. [p=0.2] {b}Na água, cada partícula é uma molécula, agá dois ó. [p=0.3] E agora, uma ideia nova: [p=0.1] {c}elas nunca ficam paradas, estão sempre se mexendo."),
    # estados
    dict(id="s04", block="estados", text="{a}No sólido, as partículas estão presas umas às outras, bem juntinhas. [p=0.2] {b}Elas só tremem no lugar. [p=0.3] Por isso {c}o gelo tem forma própria: não escorre."),
    dict(id="s05", block="estados", text="{a}No líquido, elas se agitam mais. [p=0.2] Continuam perto, mas {b}escorregam umas sobre as outras. [p=0.3] Por isso a água {c}toma a forma do copo, [p=0.1] mas continua com o mesmo volume."),
    dict(id="s06", block="estados", text="{a}No gás, a agitação é tão grande que as partículas se soltam [p=0.1] e {b}voam para todo lado, bem afastadas. [p=0.3] {c}O gás ocupa todo o espaço que encontrar: [p=0.1] é por isso que o cheiro do café se espalha pela casa."),
    dict(id="s07", block="estados", text="E o que muda a agitação? [p=0.2] {a}O calor. [p=0.2] Calor é energia que passa do que está mais quente para o que está mais frio. [p=0.3] {b}Quando o material recebe calor, as partículas se agitam mais. [p=0.2] {c}Quando perde calor, se agitam menos."),
    # mudanças
    dict(id="s08", block="mudancas", text="Agora, os nomes. [p=0.2] {a}De sólido para líquido é a fusão: [p=0.1] o gelo derretendo. [p=0.3] {b}O caminho de volta, de líquido para sólido, é a solidificação: [p=0.1] a água virando gelo no congelador."),
    dict(id="s09", block="mudancas", text="{a}De líquido para gás é a vaporização. [p=0.3] {b}O caminho de volta, de gás para líquido, é a condensação, também chamada de liquefação: [p=0.2] {c}o espelho do banheiro embaçado depois do banho."),
    dict(id="s10", block="mudancas", text="E há um caminho direto, que pula o líquido. [p=0.2] {a}De sólido direto para gás é a sublimação: [p=0.1] {b}a naftalina e o gelo seco, que é gás carbônico congelado. [p=0.3] {c}De gás direto para sólido é a ressublimação: [p=0.1] {d}a camada de gelo que cresce na parede do congelador, vinda do vapor do ar."),
    dict(id="s11", block="mudancas", text="A vaporização tem três jeitos. [p=0.2] {a}A evaporação é lenta e acontece só na superfície, sem ferver: [p=0.1] é a roupa no varal. [p=0.3] {b}A ebulição é rápida, com bolhas no líquido todo: [p=0.1] a panela fervendo. [p=0.3] {c}E a calefação é a gota que pula e chia na chapa muito quente."),
    # calor
    dict(id="s12", block="calor", text="Em quais mudanças o material recebe calor? [p=0.2] Pense na agitação. [p=0.3] {a}Para ir de sólido a líquido, ou de líquido a gás, [p=0.1] as partículas precisam se agitar mais. [p=0.2] {b}Então o material absorve calor. [p=0.3] {c}Absorvem calor a fusão, a vaporização e a sublimação. [p=0.3] {d}É por isso que o suor refresca: [p=0.1] para evaporar, ele tira calor da sua pele."),
    dict(id="s13", block="calor", text="{a}As outras três, solidificação, condensação e ressublimação, liberam calor. [p=0.3] {b}É o calor que a água solta ao condensar no espelho, [p=0.1] {c}e o que ela perde para o congelador ao virar gelo."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com um erro clássico: [p=0.2] {a}achar que a fumacinha branca da chaleira é vapor de água. [p=0.3] {b}O vapor de água é invisível."),
    dict(id="s15", block="erro", text="{a}O que você vê é o vapor que saiu e encontrou o ar frio: [p=0.2] {b}ele condensa em gotinhas de água líquida, tão pequenas que flutuam. [p=0.3] {c}Aquela nuvem branca já é líquido. [p=0.2] {d}Bem no bico da chaleira, onde ainda está quente, você quase não vê nada."),
    # atalho
    dict(id="s16", block="atalho", text="O atalho de prova é uma {a}escada: [p=0.2] {b}sólido embaixo, líquido no meio, gás em cima. [p=0.3] {c}Subir a escada é absorver calor. [p=0.2] {d}Descer é liberar."),
    dict(id="s17", block="atalho", text="{a}Fusão, vaporização e sublimação sobem. [p=0.2] {b}Solidificação, condensação e ressublimação descem. [p=0.3] Funciona porque {c}cada degrau para cima pede mais agitação, e agitação custa energia."),
    dict(id="s18", block="atalho", text="{a}A escada não diz em que temperatura cada mudança acontece. [p=0.2] Isso fica para a próxima aula."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Diga o nome de cada mudança, e se ela absorve ou libera calor. [p=0.3] {a}Um: a poça some do chão depois da chuva. [p=0.2] {b}Dois: a naftalina diminui no armário. [p=0.2] {c}Três: a água vira gelo na forminha do congelador."),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s21", block="resposta", text="{a}A poça: de líquido para gás, sem ferver. [p=0.2] {b}É vaporização, na forma de evaporação. [p=0.2] {c}Sobe a escada: absorve calor."),
    dict(id="s22", block="resposta", text="{a}A naftalina: de sólido direto para gás. [p=0.2] {b}Sublimação, que também sobe: absorve. [p=0.3] {c}A forminha: de líquido para sólido. [p=0.2] {d}Solidificação, que desce: libera calor. [p=0.3] {e}Quem disse que o congelador dá frio para a água inverteu: [p=0.1] {f}é a água que perde calor para ele."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: [p=0.1] {a}a agitação das partículas define o estado; [p=0.2] {b}são seis mudanças, em pares de ida e volta; [p=0.2] e {c}subir a escada absorve calor, descer libera."),
    dict(id="s24", block="fim", text="Na próxima aula, você vai aquecer gelo e acompanhar o termômetro: [p=0.2] {a}a curva de aquecimento, [p=0.1] que mostra se um material é puro ou é mistura. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
