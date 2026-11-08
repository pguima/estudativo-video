# Estudativo · MAT-ESP-003 — Vistas e projeções (Matemática · Geometria Espacial).
# Habilidade: desenhar a vista de cima e a de frente de um objeto e escolher qual sombra ele projeta.
# Pré-requisitos: MAT-ESP-001 (cubo, cilindro, cone, pirâmide; arestas). Próxima: MAT-ESP-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Pilha de cubinhos (s07–s09): fileira da frente com três cubinhos (esquerda, meio, direita); um cubinho atrás do da esquerda;
# dois cubinhos sobre o da frente à esquerda (torre de três). Vista de frente: alturas 3, 1, 1. Vista de cima: quatro quadradinhos em L.

TITULO = "Vistas e projeções"

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
    dict(id="s01", block="gancho", text="{a}Meio-dia, sol bem em cima da cabeça. [p=0.2] {b}Uma lata deitada no chão faz sombra de que forma? [p=0.3] Muita gente responde {c}círculo. [p=0.2] A sombra é {d}um retângulo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você desenha um objeto visto de cima e de frente, [p=0.2] acerta a sombra que ele faz [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}uma coisa: [p=0.2] {b}reconhecer os sólidos, como o cubo, o cilindro, o cone e a pirâmide. [p=0.3] Se faltar, procure no canal."),
    # o que é vista
    dict(id="s04", block="vista", text="{a}Vista é o desenho do que você enxerga olhando o objeto bem reto, sem inclinar a cabeça. [p=0.2] O resultado é {b}uma figura plana, sem perspectiva. [p=0.3] As mais cobradas são {c}a vista de frente {d}e a vista de cima."),
    dict(id="s05", block="vista", text="{a}Uma lata em pé. [p=0.2] De frente, você vê {b}um retângulo: a altura e a largura da lata. [p=0.2] De cima, só a tampa: {c}um círculo."),
    dict(id="s06", block="vista", text="{a}Um cone em pé, com a ponta para cima. [p=0.2] De frente, {b}um triângulo. [p=0.2] De cima, {c}um círculo com um ponto no meio: [p=0.2] {d}a ponta, vista de cima."),
    # pilha de cubinhos
    dict(id="s07", block="pilha", text="Agora uma pilha de {a}cubinhos iguais. [p=0.2] Na frente, {b}três cubinhos em fila. [p=0.2] {c}Atrás do da esquerda, mais um. [p=0.2] E, em cima do da frente à esquerda, {d}mais dois, formando uma torre de três."),
    dict(id="s08", block="pilha", text="De frente, {a}a torre aparece com três quadradinhos de altura, [p=0.2] e {b}os outros com um só. [p=0.3] {c}O cubinho de trás some: [p=0.2] fica escondido atrás da torre."),
    dict(id="s09", block="pilha", text="De cima, {a}a altura some. [p=0.2] {b}A torre vira um quadradinho só. [p=0.2] E aparece {c}o cubinho de trás, que de frente estava escondido. [p=0.3] Ficam {d}quatro quadradinhos, em forma de éle."),
    # sombra
    dict(id="s10", block="sombra", text="E a sombra? [p=0.2] Com a luz {a}bem em cima, caindo reta no chão, [p=0.2] {b}a sombra tem a forma da vista de cima. [p=0.3] Com a luz {c}bem de frente, e uma parede atrás, [p=0.2] {d}a sombra na parede tem a forma da vista de frente."),
    dict(id="s11", block="sombra", text="Essa sombra feita por luz reta se chama {a}projeção. [p=0.3] Na lata deitada, olhando de cima, você vê {b}o comprimento e a largura da lata: [p=0.2] {c}um retângulo. [p=0.2] O círculo só aparece {d}olhando para a tampa."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}responder pela forma famosa do objeto. [p=0.2] Lata é redonda, então a sombra seria {b}um círculo. [p=0.3] Mas a sombra {c}depende de onde vem a luz e de como o objeto está. [p=0.2] Lata em pé, sol em cima: {d}círculo. [p=0.2] Lata deitada, sol em cima: {e}retângulo."),
    # atalho
    dict(id="s13", block="atalho", text="E o atalho: {a}cada vista apaga uma direção. [p=0.3] {b}De frente, some a profundidade: ficam a largura e a altura. [p=0.2] {c}De cima, some a altura: ficam a largura e a profundidade."),
    dict(id="s14", block="atalho", text="Em pilha de cubinhos, isso vira regra rápida. [p=0.2] {a}Vista de cima: um quadradinho em cada lugar do chão que tem cubo. [p=0.2] {b}Vista de frente: em cada posição, da esquerda para a direita, vale a torre mais alta, esteja na frente ou no fundo."),
    dict(id="s15", block="atalho", text="Funciona porque a luz reta {a}achata o objeto contra o chão ou a parede: [p=0.2] o que está atrás {b}cai em cima do que está na frente. [p=0.3] {c}Não compensa com luz inclinada, como a do fim da tarde: [p=0.2] aí, {d}a sombra estica e muda de tamanho."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Uma pirâmide quadrangular em pé, com a ponta bem acima do centro da base. [p=0.3] {b}Como é a vista de cima? [p=0.2] E, com a luz bem de frente, {c}que forma tem a sombra na parede atrás dela?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] De cima, {a}a base aparece inteira: um quadrado. [p=0.2] E as quatro arestas que sobem até a ponta {b}aparecem como as diagonais do quadrado, [p=0.2] com {c}a ponta bem no centro, onde elas se cruzam."),
    dict(id="s19", block="resposta", text="Com a luz de frente, {a}some a profundidade. [p=0.2] Ficam a largura da base, embaixo, e a altura, até a ponta: [p=0.2] {b}a sombra é um triângulo. [p=0.3] {c}Mesmo sólido, duas formas: depende de onde você olha."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}a vista é o objeto achatado, visto bem reto, [p=0.2] e {b}a sombra de luz reta tem a forma da vista daquela direção."),
    dict(id="s21", block="fim", text="Na próxima aula, você volta para dentro da caixa: [p=0.2] olhando {a}as arestas de uma caixa, descobre quais são paralelas e quais se cruzam, [p=0.2] e conhece {b}um tipo de reta que só existe no espaço. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
