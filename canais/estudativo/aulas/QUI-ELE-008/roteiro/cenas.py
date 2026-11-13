# Estudativo · QUI-ELE-008 — Eletrólise ígnea (Química · Eletroquímica e Radioatividade · Eletrólise).
# Habilidade: dizer o que muda da pilha para a eletrólise, escrever o que acontece em cada polo no NaCl fundido e explicar como
# se produz alumínio.
# Pré-requisitos: QUI-ELE-004, QUI-LIG-004. Próxima: QUI-ELE-009 (eletrólise aquosa: NaCl e CuSO₄ em água, galvanoplastia).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Primeira aula do módulo: guarda a linguagem visual da eletrólise.
# Questão inédita, criada para esta aula.
# Fatos: NaCl funde a 801 °C. Cátodo (−): Na⁺ + e⁻ → Na. Ânodo (+): 2 Cl⁻ → Cl₂ + 2 e⁻. Global: 2 NaCl → 2 Na + Cl₂.
# Alumínio (processo Hall-Héroult, 1886): bauxita → alumina, Al₂O₃, que funde a cerca de 2.000 °C (2.072 °C); dissolvida na
# criolita fundida, a cuba trabalha perto de 1.000 °C. Cátodo: Al³⁺ + 3 e⁻ → Al. Ânodo de carbono: O²⁻ vira O₂, que queima o
# carbono a CO₂ (os ânodos se gastam). Reciclar alumínio gasta cerca de 5% da energia de produzir do minério.
# Questão: MgCl₂ fundido → cátodo Mg²⁺ + 2 e⁻ → Mg; ânodo 2 Cl⁻ → Cl₂ + 2 e⁻.
# "Já ensinado" não inclui QUI-ELE-005 (recarga de bateria): a recarga não é citada como conhecida.

TITULO = "Eletrólise ígnea"

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
    dict(id="s01", block="gancho", text="{a}O alumínio é o metal mais comum da crosta da Terra. [p=0.3] {b}Mas, no século dezenove, chegou a valer mais que o ouro. [p=0.3] {c}Ninguém conseguia tirá-lo do minério em grande quantidade. [p=0.3] {d}O que mudou foi uma corrente elétrica."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai dizer {b}o que muda da pilha para a eletrólise, [p=0.2] {c}o que sai em cada polo no sal derretido [p=0.1] e {d}como se faz o alumínio. [p=0.2] E ainda leva um {e}macete de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de duas coisas. [p=0.2] {a}Na pilha, a reação acontece sozinha e empurra elétrons pelo fio: [p=0.1] {b}oxidação no ânodo, redução no cátodo. [p=0.3] E {c}um composto iônico, como o sal, só conduz corrente derretido ou dissolvido. [p=0.2] É quando os íons ficam livres. [p=0.2] Se faltar alguma, procure no canal."),
    # pilha x eletrólise
    dict(id="s04", block="ideia", text="A pilha usa uma reação que acontece sozinha {a}para fazer corrente. [p=0.3] {b}A eletrólise faz o contrário: [p=0.1] {c}usa uma corrente de fora, de um gerador, [p=0.1] {d}para forçar uma reação que não aconteceria sozinha. [p=0.3] {e}Na pilha, a química vira eletricidade. [p=0.1] {f}Na eletrólise, a eletricidade vira química."),
    dict(id="s05", block="ideia", text="{a}Eletrólise ígnea quer dizer com fogo: [p=0.1] a substância está derretida, sem água. [p=0.3] {b}O sal de cozinha derrete a oitocentos e um graus. [p=0.3] {c}Derretido, os íons sódio mais e cloreto menos ficam livres para andar."),
    # a cuba
    dict(id="s06", block="cuba", text="{a}Num tanque, a cuba, mergulhe duas placas no sal derretido [p=0.1] e ligue cada uma num polo do gerador, a fonte de corrente. [p=0.3] {b}O gerador empurra elétrons para uma das placas: [p=0.1] ela fica negativa. [p=0.2] {c}E puxa elétrons da outra: [p=0.1] ela fica positiva."),
    dict(id="s07", block="cuba", text="{a}Os íons positivos, sódio mais, são atraídos pela placa negativa. [p=0.2] {b}Os negativos, cloreto menos, pela positiva. [p=0.3] {c}Opostos se atraem, como você viu na carga elétrica."),
    # polos
    dict(id="s08", block="polos", text="{a}Na placa negativa, cada sódio mais recebe um elétron [p=0.1] {b}e vira sódio metálico. [p=0.2] {c}Recebeu elétron: é redução. [p=0.1] {d}Então essa placa é o cátodo. [p=0.3] {e}O sódio sai líquido e é recolhido."),
    dict(id="s09", block="polos", text="{a}Na placa positiva, cada cloreto menos entrega um elétron. [p=0.2] {b}Dois cloros se juntam [p=0.1] {c}e sai gás cloro, cê ele dois. [p=0.2] {d}Perdeu elétron: é oxidação, [p=0.1] {e}e a placa é o ânodo."),
    dict(id="s10", block="polos", text="{a}Repare no que mudou. [p=0.2] {b}Ânodo continua sendo oxidação, e cátodo, redução. [p=0.3] {c}Mas os sinais trocaram: [p=0.1] {d}na eletrólise, o cátodo é o negativo, [p=0.1] {e}e o ânodo, o positivo."),
    # alumínio
    dict(id="s11", block="aluminio", text="Agora, o alumínio. [p=0.2] {a}O minério é a bauxita, de onde se tira a alumina, á ele dois ó três. [p=0.3] {b}O problema: ela só derrete perto de dois mil graus. [p=0.3] {c}O truque de mil oitocentos e oitenta e seis foi dissolvê-la noutro mineral derretido, a criolita, [p=0.1] {d}e a mistura fica perto de mil graus."),
    dict(id="s12", block="aluminio", text="{a}Derretida, a alumina solta íons alumínio três mais e íons óxido, dois menos. [p=0.3] No cátodo, cada alumínio três mais recebe três elétrons [p=0.1] {b}e vira alumínio líquido, no fundo da cuba. [p=0.3] {c}No ânodo, feito de carvão, o oxigênio da alumina se solta [p=0.1] {d}e queima o próprio carvão, que vira gás carbônico. [p=0.2] {e}Por isso, os ânodos se gastam e são trocados."),
    dict(id="s13", block="aluminio", text="{a}Isso gasta uma montanha de energia elétrica. [p=0.2] {b}Reciclar uma latinha usa só cerca de cinco por cento dessa energia. [p=0.2] {c}Por isso, no Brasil, quase toda lata de alumínio volta para a fábrica."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que o cátodo é sempre o positivo, porque era assim na pilha. [p=0.3] {b}O sinal vem de quem manda os elétrons. [p=0.2] {c}Na pilha, quem manda é o ânodo: negativo. [p=0.2] {d}Na eletrólise, quem manda é o gerador, e a placa que recebe os elétrons, o cátodo, é a negativa."),
    # macete
    dict(id="s15", block="atalho", text="Agora, o macete de prova: [p=0.2] {a}cátion vai para o cátodo, [p=0.1] {b}ânion vai para o ânodo. [p=0.3] {c}O começo da palavra é igual. [p=0.3] {d}E por isso, no sal derretido, [p=0.1] {e}o metal sai no cátodo, e o ametal, no ânodo."),
    dict(id="s16", block="atalho", text="Funciona porque, {a}no sal derretido, o cátion de metal só tem como ganhar elétrons, virando metal. [p=0.2] {b}O ânion é negativo e só pode perder. [p=0.3] {c}Não compensa quando há água junto: [p=0.1] {d}aí, a água disputa os polos, e isso é assunto da próxima aula."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}O magnésio, usado em ligas leves de carros e aviões, vem da eletrólise ígnea do cloreto de magnésio. [p=0.3] {b}O magnésio dois mais e o cloreto menos estão derretidos. [p=0.2] {c}O que sai no cátodo, o que sai no ânodo, [p=0.1] {d}e qual polo é o negativo?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}O cátion, magnésio dois mais, vai para o cátodo: [p=0.1] {b}recebe dois elétrons e vira magnésio metálico. [p=0.3] {c}O ânion, cloreto, vai para o ânodo: [p=0.1] {d}dois cloretos perdem um elétron cada e formam gás cloro. [p=0.3] {e}E o negativo é o cátodo, ligado ao polo negativo do gerador."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}na eletrólise, a corrente de fora força a reação; [p=0.1] {b}o cátion vai ao cátodo, negativo, e vira metal; [p=0.1] {c}o ânion vai ao ânodo, positivo."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai pôr água nessa cuba: [p=0.2] {a}o sal dissolvido não dá sódio, [p=0.1] {b}e você vai prever o que sai em cada polo. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
