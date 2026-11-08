# Estudativo · MAT-CON-001 — Conjuntos: pertence, está contido e vazio (Matemática · Conjuntos).
# Habilidade: escrever as vogais entre chaves, usar ∈ e ⊂ sem trocar um pelo outro e dizer que {1, 2, 3} tem 8 subconjuntos.
# Pré-requisitos: MAT-NUM-002 (comparar com > e <), MAT-POT-001 (potência). Próxima: MAT-CON-002.
# Questão inédita, criada para esta aula. Sem negativos, frações nem decimais: fora da ficha desta aula.
# Contas: subconjuntos de {1, 2, 3} = 3 de um elemento + 3 de dois + o próprio + o vazio = 8 = 2³ · vogais: 2⁵ = 32 · questão: P = {2, 5, 7, 9}, 2⁴ = 16.
# Visual: V = {a, e, i, o, u} entre chaves; símbolos ∈, ∉, ⊂ e ∅; lista dos 8 subconjuntos em quatro grupos; árvore "entra ou fica fora".
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Conjuntos: pertence, está contido e vazio"

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
    dict(id="s01", block="gancho", text="{a}Quantos subconjuntos tem o conjunto com um, dois e três? [p=0.3] Muita gente lista os pedaços e responde {b}seis. [p=0.3] Faltou contar o vazio e o próprio conjunto. [p=0.2] A resposta é {c}oito."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você escreve qualquer conjunto, [p=0.2] usa {b}pertence e está contido sem trocar um pelo outro [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}comparar números com maior e menor [p=0.2] e {c}potência, como dois elevado a três, que é dois vezes dois vezes dois. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é conjunto
    dict(id="s04", block="conjunto", text="O que é um conjunto? [p=0.2] É {a}um grupo de coisas, com uma regra clara para saber quem está dentro. [p=0.3] Cada coisa do grupo se chama {b}elemento. [p=0.3] Pense nas {c}vogais: á, é, i, ó, u."),
    dict(id="s05", block="conjunto", text="Para escrever, dê ao conjunto um nome com {a}letra maiúscula, [p=0.2] e ponha os elementos {b}entre chaves, separados por vírgula. [p=0.3] {c}Vê, de vogais, é igual a: abre chave, á, é, i, ó, u, fecha chave. [p=0.3] {d}A ordem não importa, [p=0.2] e {e}elemento repetido conta uma vez só."),
    dict(id="s06", block="regra", text="Também dá para descrever pela regra. [p=0.2] {a}O conjunto dos algarismos maiores que seis [p=0.2] tem {b}sete, oito e nove. [p=0.3] E um conjunto pode não ter elemento nenhum: [p=0.2] {c}os algarismos maiores que nove. [p=0.2] Não existe nenhum."),
    dict(id="s07", block="regra", text="Esse é o {a}conjunto vazio. [p=0.2] Ele se escreve com {b}chaves sem nada dentro, [p=0.2] ou com {c}um zero cortado por um risco."),
    # pertence
    dict(id="s08", block="pertence", text="Vamos aos símbolos. [p=0.2] Para ligar {a}um elemento a um conjunto, use {b}pertence. [p=0.3] {c}A letra á pertence ao conjunto das vogais. [p=0.3] {d}A letra bê não pertence: [p=0.2] é o mesmo símbolo, {e}cortado por um risco."),
    # contido
    dict(id="s09", block="contido", text="Para ligar {a}um conjunto a outro conjunto, use {b}está contido. [p=0.3] O conjunto com as letras {c}á e é está contido nas vogais, [p=0.2] porque {d}cada elemento dele também está nas vogais. [p=0.3] Ele é um {e}subconjunto das vogais: um pedaço do conjunto."),
    dict(id="s10", block="contido", text="Dois casos surpreendem. [p=0.2] {a}Todo conjunto está contido nele mesmo, [p=0.2] porque cada elemento dele está nele. [p=0.3] E {b}o vazio está contido em qualquer conjunto, [p=0.2] porque ele não tem nenhum elemento que fique de fora."),
    # contando subconjuntos
    dict(id="s11", block="contar", text="Voltando ao começo: os subconjuntos do conjunto com {a}um, dois e três. [p=0.3] Com um elemento só, {b}são três. [p=0.2] Com dois elementos, {c}mais três. [p=0.3] Agora, os que costumam faltar: [p=0.2] {d}o próprio conjunto [p=0.2] e {e}o vazio. [p=0.3] Total: {f}oito subconjuntos."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}trocar os símbolos. [p=0.2] A pessoa escreve que {b}a letra á está contida nas vogais. [p=0.3] Só que a letra sozinha é {c}elemento, e elemento pertence. [p=0.3] Já o conjunto que tem só a letra á, entre chaves, [p=0.2] {d}é um conjunto: ele está contido."),
    dict(id="s13", block="erro", text="Antes de escrever, pergunte: [p=0.2] {a}o que está à esquerda é elemento ou conjunto? [p=0.3] {b}Elemento pertence. [p=0.2] {c}Conjunto está contido. [p=0.3] E lembre que o vazio também é conjunto, [p=0.2] mesmo quando aparece como {d}o zero cortado."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}contar subconjuntos sem listar. [p=0.3] Cada elemento tem {b}duas escolhas: entra ou fica de fora. [p=0.3] Com três elementos, são {c}dois vezes dois vezes dois: [p=0.2] {d}dois elevado a três, oito."),
    dict(id="s15", block="atalho", text="Funciona porque cada jeito de escolher forma {a}um subconjunto diferente. [p=0.3] {b}Se todos ficam de fora, sai o vazio. [p=0.2] {c}Se todos entram, sai o próprio conjunto. [p=0.3] Nas vogais, são cinco elementos: [p=0.2] {d}dois elevado a cinco, trinta e dois subconjuntos."),
    dict(id="s16", block="atalho", text="Não compensa quando a questão pede {a}quais são os subconjuntos: [p=0.2] aí, você precisa listar. [p=0.3] E {b}conte só os elementos diferentes, [p=0.2] porque repetido não vale duas vezes."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] O conjunto pê tem {a}dois, cinco, sete e nove. [p=0.3] {b}O cinco pertence ou está contido em pê? [p=0.2] {c}E o conjunto com cinco e sete? [p=0.3] {d}Quantos subconjuntos pê tem?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] O cinco sozinho é elemento: {a}cinco pertence a pê. [p=0.3] O conjunto com cinco e sete é conjunto, [p=0.2] e cada elemento dele está em pê: {b}ele está contido em pê."),
    dict(id="s20", block="resposta", text="Pê tem quatro elementos: {a}dois elevado a quatro. [p=0.2] {b}Dois, quatro, oito, dezesseis. [p=0.3] São {c}dezesseis subconjuntos, [p=0.2] contando o vazio e o próprio pê."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}elemento pertence, [p=0.2] {b}conjunto está contido [p=0.2] e {c}dois elevado ao número de elementos conta os subconjuntos."),
    dict(id="s22", block="fim", text="Na próxima aula, você junta e separa conjuntos: [p=0.2] {a}união, interseção, diferença e complementar, [p=0.2] sem {b}confundir a palavra e com a palavra ou. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
