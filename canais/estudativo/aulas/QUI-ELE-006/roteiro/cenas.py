# Estudativo · QUI-ELE-006 — Corrosão e proteção dos metais (Química · Eletroquímica e Radioatividade · Pilhas e corrosão).
# Habilidade: explicar a ferrugem como uma pilha e escolher o metal de sacrifício para proteger o casco de um navio.
# Pré-requisitos: QUI-ELE-004. Próxima: QUI-ELE-007 (praticando: pilhas e corrosão).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Potenciais de redução (V): Mg −2,37 · Zn −0,76 · Fe −0,44 · Sn −0,14 · Pb −0,13 · Cu +0,34 · Ag +0,80 · O₂ + 2 H₂O + 4 e⁻ → 4 OH⁻ +0,40.
# Ferrugem: ânodo no meio da gota (Fe → Fe²⁺ + 2 e⁻), cátodo na borda, onde chega mais oxigênio (O₂ + 2 H₂O + 4 e⁻ → 4 OH⁻);
# Fe²⁺ + OH⁻ → Fe(OH)₂ → ao ar, Fe(OH)₃ → Fe₂O₃ · n H₂O, a ferrugem. Sem água ou sem oxigênio, não enferruja.
# Sal da maresia: deixa a água conduzir muito melhor (como a ponte salina). Galvanizado = aço com camada de zinco.
# Folha de flandres (lata) = aço com estanho: riscada, o ferro vira ânodo e corrói mais depressa.
# Casco de navio: blocos de zinco (ou liga de alumínio) presos ao aço, trocados de tempos em tempos.
# Questão: tubulação enterrada; candidatos cobre, chumbo, magnésio, prata → só o magnésio (−2,37 < −0,44).

TITULO = "Corrosão e proteção dos metais"

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
    dict(id="s01", block="gancho", text="{a}Muitos navios de aço, que é ferro com um pouco de carbono, levam presos no casco {b}blocos de zinco. [p=0.3] {c}Com os anos, os blocos vão sendo comidos pela água do mar, [p=0.1] e o casco fica inteiro. [p=0.3] {d}Por que o zinco se gasta no lugar do ferro?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai explicar {b}a ferrugem como uma pilha [p=0.2] e {c}escolher o metal que se sacrifica para proteger o ferro. [p=0.2] E ainda leva um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de duas coisas. [p=0.2] {a}Na pilha, o ânodo se oxida e se gasta, [p=0.1] e o cátodo recebe os elétrons. [p=0.3] E {b}na escada de potenciais, quem está mais embaixo se oxida. [p=0.2] Se faltar alguma, procure no canal."),
    # ferrugem
    dict(id="s04", block="ferrugem", text="Comece com uma gota de água sobre uma chapa de ferro. [p=0.2] {a}Ali se forma uma pilha, que ninguém montou. [p=0.3] {b}No meio da gota, o ferro se oxida: [p=0.1] {c}cada átomo perde dois elétrons e vira ferro dois mais. [p=0.2] {d}Esse é o ânodo."),
    dict(id="s05", block="ferrugem", text="{a}Os elétrons andam pela própria chapa até a borda da gota, [p=0.1] onde chega mais ar. [p=0.3] {b}Lá, o oxigênio e a água recebem esses elétrons [p=0.1] {c}e formam íons hidróxido, ó agá menos. [p=0.2] {d}A borda é o cátodo."),
    dict(id="s06", block="ferrugem", text="{a}O ferro dois mais e o hidróxido se encontram na água. [p=0.2] {b}Com mais oxigênio do ar, viram um óxido de ferro com água presa nele, [p=0.1] {c}o pó marrom que você conhece: a ferrugem."),
    dict(id="s07", block="ferrugem", text="{a}Por isso, ferro seco não enferruja, [p=0.1] {b}e ferro sem oxigênio também não. [p=0.3] {c}Precisa de água e de oxigênio juntos. [p=0.3] {d}E na praia, é mais rápido: [p=0.1] {e}o sal faz a água conduzir muito melhor, como na ponte salina."),
    # proteção por barreira
    dict(id="s08", block="barreira", text="Como proteger? [p=0.2] {a}O primeiro jeito é tapar: [p=0.1] {b}tinta, graxa ou uma camada de outro metal, [p=0.1] para a água e o ar não chegarem ao ferro. [p=0.3] {c}Funciona enquanto a camada estiver inteira."),
    # sacrifício
    dict(id="s09", block="sacrificio", text="O segundo jeito é mais esperto: {a}o metal de sacrifício. [p=0.2] Ligue ao ferro {b}um metal que se oxide mais fácil que ele. [p=0.3] {c}Os dois formam uma pilha, [p=0.1] {d}e o outro metal vira o ânodo: [p=0.1] {e}ele se oxida no lugar do ferro."),
    dict(id="s10", block="sacrificio", text="{a}O ferro vira o cátodo, que só recebe elétrons, [p=0.1] {b}e fica protegido. [p=0.3] {c}O metal de sacrifício se gasta [p=0.1] e precisa ser trocado de tempos em tempos. [p=0.2] {d}É o bloco de zinco do navio."),
    dict(id="s11", block="sacrificio", text="Como escolher? [p=0.2] Pela escada. [p=0.2] {a}O ferro está em menos zero vírgula quarenta e quatro. [p=0.3] {b}O zinco está em menos zero vírgula setenta e seis. [p=0.2] {c}O magnésio, em menos dois vírgula trinta e sete. [p=0.2] {d}Ambos estão abaixo do ferro: servem. [p=0.3] {e}Cobre e prata estão acima: não servem."),
    # galvanizado e flandres
    dict(id="s12", block="camadas", text="{a}O aço galvanizado, das telhas e dos pregos, é coberto de zinco. [p=0.2] {b}Ele protege duas vezes: [p=0.1] tapa, e, se riscar, ainda se sacrifica."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que qualquer camada de metal protege. [p=0.3] {b}A lata de conserva é aço coberto de estanho, [p=0.1] {c}que está acima do ferro, em menos zero vírgula catorze. [p=0.3] {d}Riscou, o ferro vira o ânodo da pilha, [p=0.1] {e}e enferruja mais rápido do que sem estanho nenhum."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}metal de sacrifício é o que está abaixo do ferro na escada. [p=0.3] {b}Quem está mais embaixo se oxida no lugar do outro. [p=0.3] {c}Não precisa calcular a dê dê pê: [p=0.1] {d}basta comparar com menos zero vírgula quarenta e quatro."),
    dict(id="s15", block="atalho", text="Funciona porque {a}o mais embaixo é o que perde elétrons com mais facilidade. [p=0.3] {b}Não compensa ir até o fim da escada: [p=0.1] {c}sódio e potássio estão lá embaixo, [p=0.1] {d}mas reagem com a própria água e sumiriam na hora."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Uma tubulação de ferro vai ficar enterrada em solo úmido. [p=0.3] {b}Os candidatos a metal de sacrifício são: [p=0.1] {c}cobre, chumbo, magnésio e prata. [p=0.3] {d}O chumbo está em menos zero vírgula treze. [p=0.2] {e}Qual metal protege, e quem se oxida?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Compare com o ferro, menos zero vírgula quarenta e quatro. [p=0.3] {b}Cobre e prata estão acima, positivos. [p=0.2] {c}O chumbo, em menos zero vírgula treze, também está acima: [p=0.1] o número é menos negativo. [p=0.3] {d}Só o magnésio está abaixo. [p=0.2] {e}Ele se oxida, e o ferro fica protegido."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}a ferrugem é uma pilha, com o ferro de ânodo; [p=0.1] {b}e o metal de sacrifício, abaixo do ferro na escada, se oxida no lugar dele."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai juntar tudo isso {a}em questões de prova: [p=0.1] {b}dê dê pê, polos e proteção dos metais. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
