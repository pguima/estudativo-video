# Estudativo · MAT-ANG-020 — Pontos notáveis e baricentro (Matemática · Geometria Plana: Ângulos e Triângulos).
# Habilidade: ligar altura, mediana, bissetriz e mediatriz a ortocentro, baricentro, incentro e circuncentro e usar que o baricentro divide a mediana em 2 para 1, como 6 e 3 numa mediana de 9.
# Pré-requisitos: MAT-ANG-008 (altura, mediana, bissetriz e mediatriz), MAT-RAZ-002 (proporção e produto cruzado). Próxima: MAT-ANG-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas como se falam: "á", "bê", "cê", "eme", "gê" (G = baricentro).
# Figuras: E.triangulo com as três medianas (ou alturas, bissetrizes, mediatrizes) se cruzando num ponto marcado.
# s06: E.circulo inscrito com centro no incentro; s07: E.circulo passando pelos três vértices com centro no circuncentro.
# s08: obtusângulo com as alturas prolongadas e o ortocentro fora.
# s11: mediana AM = 9 dividida em três pedaços iguais (AG = 6, GM = 3). s16: moedas nos vértices e gangorra A—M.

TITULO = "Pontos notáveis e baricentro"

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
    dict(id="s01", block="gancho", text="{a}Um triângulo de papelão equilibra na ponta de um lápis, [p=0.2] mas só {b}num ponto exato. [p=0.3] E esse ponto dá para achar {c}com uma conta de cabeça."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você liga cada linha do triângulo ao seu ponto especial, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}altura, mediana, bissetriz e mediatriz, [p=0.2] e {c}proporção, com a cruz para achar o termo que falta. [p=0.3] Se faltar alguma, procure no canal."),
    # pontos notáveis
    dict(id="s04", block="encontro", text="Todo triângulo tem {a}três medianas, uma saindo de cada vértice. [p=0.2] E acontece algo curioso: [p=0.2] {b}elas se cruzam num ponto só. [p=0.3] O mesmo vale para as alturas, [p=0.1] para as bissetrizes [p=0.1] e para as mediatrizes. [p=0.2] Cada encontro é um {c}ponto notável."),
    dict(id="s05", block="baricentro", text="{a}As medianas se encontram no baricentro. [p=0.2] Bari quer dizer {b}peso: [p=0.2] é o ponto de equilíbrio do papelão. [p=0.3] Ele fica {c}sempre dentro do triângulo."),
    dict(id="s06", block="incentro", text="{a}As bissetrizes se encontram no incentro. [p=0.2] In, de {b}dentro: [p=0.2] ele é o centro do círculo que cabe {c}dentro do triângulo, encostando nos três lados. [p=0.2] Também fica sempre dentro."),
    dict(id="s07", block="circuncentro", text="{a}As mediatrizes se encontram no circuncentro. [p=0.2] Circun, de {b}em volta: [p=0.2] ele é o centro do círculo que passa {c}pelos três vértices. [p=0.3] Lembra que todo ponto da mediatriz fica à mesma distância das pontas do lado? [p=0.2] Por isso, {d}o circuncentro fica à mesma distância dos três vértices."),
    dict(id="s08", block="ortocentro", text="{a}As alturas se encontram no ortocentro. [p=0.2] Orto quer dizer {b}reto, como o ângulo da altura. [p=0.3] No obtusângulo, duas alturas caem fora. [p=0.2] Prolongando as três, elas se cruzam {c}fora do triângulo: [p=0.2] o ortocentro fica fora. [p=0.2] O circuncentro, nesse caso, {d}sai também."),
    dict(id="s09", block="equilatero", text="E no equilátero? [p=0.2] Cada linha que sai de um vértice faz os quatro papéis, [p=0.2] então {a}os quatro pontos viram um ponto só."),
    # baricentro: dois para um
    dict(id="s10", block="dois_um", text="O fato que mais cai: {a}o baricentro divide cada mediana na razão de dois para um. [p=0.3] {b}O pedaço que encosta no vértice é o dobro do pedaço que encosta no lado."),
    dict(id="s11", block="dois_um", text="Numa mediana de {a}nove, [p=0.2] pense em três pedaços iguais: {b}nove dividido por três dá três. [p=0.3] {c}Dois pedaços ficam com o vértice: seis. [p=0.2] {d}Um pedaço fica com o lado: três. [p=0.3] Seis é o dobro de três: {e}dois para um."),
    dict(id="s12", block="dois_um", text="E de trás para frente? [p=0.2] O baricentro {a}gê está a doze do vértice á. [p=0.3] Monte a proporção: {b}doze está para xis, assim como dois está para um. [p=0.2] Cruz: {c}dois xis igual a doze, [p=0.2] xis igual a seis. [p=0.3] A mediana inteira: {d}doze mais seis dá dezoito."),
    # erro comum
    dict(id="s13", block="erro", text="O erro mais comum é {a}inverter os pedaços: [p=0.2] colocar {b}três perto do vértice e seis perto do lado. [p=0.3] Pense no papelão: {c}a ponta do vértice é fina, e o lado é largo. [p=0.2] O equilíbrio fica {d}mais perto do lado, onde tem mais papelão."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho prometido: {a}divida a mediana por três. [p=0.2] O resultado é {b}o pedaço do lado. [p=0.2] O dobro dele é {c}o pedaço do vértice. [p=0.3] Mediana de trinta? {d}Dez e vinte, de cabeça."),
    dict(id="s15", block="atalho", text="Por que dois para um? [p=0.2] Uma imagem ajuda a lembrar, [p=0.1] sem ser prova. [p=0.2] Ponha {a}uma moeda igual em cada vértice: [p=0.2] as três se equilibram no baricentro, como o papelão. [p=0.3] As moedas do bê e do cê se equilibram {b}no ponto médio eme, [p=0.2] como se estivessem juntas ali."),
    dict(id="s16", block="atalho", text="Sobra uma gangorra: {a}uma moeda no á e duas no eme. [p=0.3] Na gangorra, o lado mais pesado senta mais perto do apoio. [p=0.2] Duas moedas pesam o dobro de uma, [p=0.2] então {b}o braço da moeda sozinha precisa ser o dobro. [p=0.3] Não compensa tentar isso {c}com os outros pontos notáveis: [p=0.2] o dois para um {d}é só do baricentro."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar, em duas partes. [p=0.2] {a}Primeira: o baricentro de um triângulo está a sete centímetros do ponto médio eme. [p=0.2] {b}Quanto mede a mediana á eme?"),
    dict(id="s18", block="questao", text="{a}Segunda: uma prefeitura quer construir um posto de saúde {b}à mesma distância de três bairros. [p=0.3] Pensando nos bairros como vértices de um triângulo, [p=0.2] {c}qual ponto notável ela deve usar?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] Sete é {a}o pedaço do lado, o menor. [p=0.2] O do vértice é o dobro: {b}catorze. [p=0.3] Mediana: {c}sete mais catorze dá vinte e um centímetros."),
    dict(id="s21", block="resposta", text="Mesma distância dos três vértices: {a}circuncentro, o encontro das mediatrizes. [p=0.3] Quem respondeu baricentro {b}confundiu equilíbrio com distância. [p=0.2] Fora do equilátero, o baricentro {c}não fica à mesma distância dos vértices."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}medianas no baricentro, [p=0.2] {b}bissetrizes no incentro, [p=0.2] {c}mediatrizes no circuncentro, [p=0.2] {d}alturas no ortocentro. [p=0.3] E {e}o baricentro corta a mediana em dois para um."),
    dict(id="s23", block="fim", text="Na próxima aula, você pratica {a}tudo de ângulos e triângulos: [p=0.2] {b}paralelas, soma dos ângulos, isósceles e pontos notáveis, [p=0.2] juntos em questões. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
