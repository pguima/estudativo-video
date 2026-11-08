# Estudativo · MAT-ESP-006 — Cubo e bloco: área e diagonal (Matemática · Geometria Espacial).
# Habilidade: calcular a área de uma caixa para saber quanta tinta gastar e achar a diagonal do cubo de aresta 2 (2√3).
# Pré-requisitos: MAT-ANG-017 (d = ℓ√2), MAT-ESP-002 (planificação), MAT-ESP-005 (bloco, arestas á, bê, cê). Usa MAT-ANG-015 (Pitágoras), MAT-ARE-002 (base vezes altura) e MAT-POT-009 (raiz de doze vira dois raiz de três). Próxima: MAT-ESP-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Letra A narrada "á".

TITULO = "Cubo e bloco: área e diagonal"

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
    dict(id="s01", block="gancho", text="{a}Uma caixa de três metros por dois, com um metro de altura, vai ser pintada por fora, inteira. [p=0.3] Muita gente calcula {b}o volume, seis metros cúbicos, e para aí. [p=0.3] Mas a tinta {c}não enche a caixa: cobre a casca. [p=0.2] O que importa é {d}a área: vinte e dois metros quadrados."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula a área de qualquer caixa, [p=0.2] acha {b}a maior vareta que cabe dentro de um cubo [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}a planificação abre o sólido no plano, face por face; [p=0.2] {c}a área do retângulo é base vezes altura; [p=0.2] e {d}a diagonal do quadrado é o lado vezes raiz de dois. [p=0.3] Se faltar alguma, procure no canal."),
    # área total
    dict(id="s04", block="area", text="Abra a caixa no plano: {a}seis retângulos. [p=0.2] E eles vêm {b}em pares iguais, de faces que ficam de frente uma para a outra: [p=0.2] {c}chão e teto, [p=0.1] {d}frente e fundo, [p=0.1] {e}e os lados, esquerdo e direito."),
    dict(id="s05", block="area", text="Na caixa de três por dois por um: [p=0.2] {a}chão e teto, três vezes dois dá seis cada um. [p=0.2] {b}Frente e fundo, três vezes um dá três cada um. [p=0.2] {c}Os lados, dois vezes um dá dois cada um."),
    dict(id="s06", block="area", text="Uma face de cada par: {a}seis mais três mais dois dá onze. [p=0.2] Cada uma tem uma gêmea, então {b}onze vezes dois dá vinte e dois metros quadrados. [p=0.3] Essa é a {c}área total: a soma das áreas de todas as faces."),
    dict(id="s07", block="area", text="Na fórmula, com arestas á, bê e cê: [p=0.2] {a}área total igual a duas vezes, abre parênteses, á bê mais á cê mais bê cê, fecha parênteses. [p=0.2] {b}Cada produto é a área de uma face, [p=0.2] e {c}o dois conta a gêmea. [p=0.3] No cubo, são {d}seis quadrados iguais: seis á ao quadrado."),
    dict(id="s08", block="area", text="E a tinta? [p=0.2] Se uma lata pinta {a}dez metros quadrados, [p=0.2] {b}vinte e dois dividido por dez dá dois vírgula dois: mais de duas latas. [p=0.2] Ninguém vende pedaço de lata: {c}são três latas."),
    # diagonal
    dict(id="s09", block="diagonal", text="Agora, {a}a diagonal do bloco: [p=0.2] o segmento que vai de um canto de baixo até o canto de cima mais distante, [p=0.2] {b}atravessando a caixa por dentro. [p=0.3] É {c}a maior vareta que cabe lá dentro."),
    dict(id="s10", block="diagonal", text="Num cubo de {a}aresta dois. [p=0.2] Primeiro, {b}a diagonal do chão, que é um quadrado: [p=0.2] lado vezes raiz de dois. [p=0.2] Aqui, {c}dois raiz de dois."),
    dict(id="s11", block="diagonal", text="Essa diagonal do chão, {a}a aresta em pé e a diagonal do cubo formam um triângulo retângulo. [p=0.2] O ângulo reto fica {b}no pé da aresta em pé, que sobe reta do chão. [p=0.2] E {c}a diagonal do cubo é a hipotenusa."),
    dict(id="s12", block="diagonal", text="Pitágoras: [p=0.2] {a}dois raiz de dois, ao quadrado, dá oito. [p=0.2] {b}Dois ao quadrado dá quatro. [p=0.2] {c}Oito mais quatro dá doze. [p=0.3] Doze é {d}quatro vezes três, e o quatro sai da raiz como dois: [p=0.2] a diagonal é {e}dois raiz de três. [p=0.2] Dá um pouco menos que três e meio."),
    dict(id="s13", block="diagonal", text="Repare que o oito era {a}dois ao quadrado mais dois ao quadrado. [p=0.2] Então a diagonal ao quadrado é {b}a soma dos quadrados das três arestas. [p=0.3] Na fórmula: {c}dê igual à raiz de á ao quadrado mais bê ao quadrado mais cê ao quadrado. [p=0.2] {d}Dê é a diagonal, [p=0.1] e {e}á, bê e cê, as arestas."),
    # erro
    dict(id="s14", block="erro", text="O erro comum na pintura é {a}somar só três faces. [p=0.2] Na caixa do começo, a pessoa acha {b}onze metros quadrados [p=0.2] e compra {c}duas latas. [p=0.3] Mas a caixa tem {d}seis faces: a área certa é o dobro, vinte e dois. [p=0.2] Duas latas pintam vinte metros quadrados, e {e}ficam dois sem tinta: lá vai você de volta à loja."),
    # atalho
    dict(id="s15", block="atalho", text="E o atalho da diagonal: {a}quadrado, raiz de dois; [p=0.2] {b}cubo, raiz de três. [p=0.3] {c}A diagonal do cubo é a aresta vezes raiz de três. [p=0.2] Aresta dois: {d}dois raiz de três, numa conta só."),
    dict(id="s16", block="atalho", text="Funciona porque, no cubo, {a}as três arestas são iguais: [p=0.2] á ao quadrado, três vezes, {b}dá três á ao quadrado, [p=0.2] e {c}a raiz disso é á raiz de três. [p=0.3] {d}Não serve no bloco de arestas diferentes. [p=0.2] Aí, {e}some os três quadrados."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Uma caixa de presente é {a}um cubo de trinta centímetros de aresta. [p=0.3] {b}Quanto papel cobre a caixa inteira, sem sobra? [p=0.2] E {c}uma vareta de cinquenta centímetros cabe lá dentro, de canto a canto? [p=0.3] Use {d}raiz de dois perto de um vírgula quatro e raiz de três perto de um vírgula sete."),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Papel: {a}seis faces de trinta por trinta. [p=0.2] {b}Trinta vezes trinta dá novecentos. [p=0.2] {c}Novecentos vezes seis dá cinco mil e quatrocentos centímetros quadrados."),
    dict(id="s20", block="resposta", text="Vareta: a diagonal do cubo é {a}trinta raiz de três. [p=0.2] {b}Trinta vezes um vírgula sete dá cinquenta e um. [p=0.2] Cinquenta e um passa de cinquenta: {c}a vareta cabe, por pouco. [p=0.3] Deitada no chão, {d}não caberia: [p=0.2] {e}trinta vezes um vírgula quatro dá só quarenta e dois."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}a área total soma as seis faces, que vêm em pares. [p=0.2] E {b}a diagonal do cubo é a aresta vezes raiz de três."),
    dict(id="s22", block="fim", text="Na próxima aula, {a}o prisma, com base triangular e com base hexagonal. [p=0.2] O volume continua sendo {b}a área da base vezes a altura, [p=0.2] e a área total, {c}a soma das faces. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
