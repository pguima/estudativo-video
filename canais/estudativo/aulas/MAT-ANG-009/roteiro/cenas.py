# Estudativo · MAT-ANG-009 — Praticando: ângulos e triângulos (Matemática · Geometria Plana: Ângulos e Triângulos · prática).
# Habilidade: resolver questões que juntam paralelas, soma dos ângulos, triângulos isósceles e pontos notáveis.
# Pré-requisitos: MAT-ANG-001 a MAT-ANG-008 e MAT-ANG-020. Próxima: MAT-ANG-010.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questões inéditas, criadas para esta aula. Letras narradas como se falam: "á", "bê", "cê", "dê", "eme", "gê", "érre", "ésse".
# Figuras:
#   Q1: retas paralelas r (em cima) e s (embaixo); triângulo ABC com A em r e B, C em s. Em A, ângulo entre r e AB (à esquerda) = 2x + 15;
#       ângulo entre r e AC (à direita) = 65°; ângulo B do triângulo = 55°. Atalho: os três ângulos em A formam um ângulo raso.
#   Q2: isósceles ABC (AB = AC, tracinhos), BC prolongado além de C, ângulo externo em C = 115°.
#   Q3: dois triângulos isósceles candidatos, 5-5-11 (não fecha) e 11-11-5.
#   Q4: isósceles ABC (AB = AC), base BC = 16, bissetriz de A até D na base.
#   Q5: mediana AM com baricentro G; AG = 3x − 2 e GM = x + 1.

TITULO = "Praticando: ângulos e triângulos"

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
    dict(id="s01", block="gancho", text="{a}Cinco questões de ângulos e triângulos, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}ângulos nas paralelas, [p=0.2] {b}a soma de cento e oitenta graus, [p=0.2] {c}o triângulo isósceles, [p=0.2] {d}o teste para saber se três medidas fecham um triângulo, [p=0.2] {e}a congruência [p=0.2] e {f}o baricentro. [p=0.3] Se alguma travar, procure a aula no canal."),
    # questão 1: paralelas e soma dos ângulos
    dict(id="s03", block="questao1", text="{a}Questão um. [p=0.2] As retas {b}érre e ésse são paralelas. [p=0.2] O triângulo á bê cê tem {c}o vértice á na reta érre [p=0.1] e a base bê cê na reta ésse."),
    dict(id="s04", block="questao1", text="No á, o lado á bê faz com a reta érre um ângulo de {a}dois xis mais quinze. [p=0.2] O lado á cê faz {b}sessenta e cinco graus. [p=0.2] E o ângulo em bê do triângulo mede {c}cinquenta e cinco graus. [p=0.3] {d}Quanto vale xis? [p=0.2] {e}E quanto mede o ângulo em á do triângulo?"),
    dict(id="s05", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s06", block="resposta1", text="Vamos lá. [p=0.2] O lado á bê é uma transversal das paralelas. [p=0.2] O ângulo de dois xis mais quinze e o ângulo em bê são {a}alternos internos, [p=0.2] os do zê: {b}são iguais. [p=0.3] {c}Dois xis mais quinze igual a cinquenta e cinco. [p=0.2] Tirando quinze de cada lado, {d}dois xis igual a quarenta. [p=0.2] {e}Xis igual a vinte."),
    dict(id="s07", block="resposta1", text="Pelo mesmo motivo, o ângulo em cê é alterno do sessenta e cinco: {a}vale sessenta e cinco graus. [p=0.3] Cinquenta e cinco mais sessenta e cinco dá cento e vinte. [p=0.2] {b}Cento e oitenta menos cento e vinte dá sessenta: o ângulo em á mede sessenta graus."),
    # atalho
    dict(id="s08", block="atalho", text="Aqui cabe um atalho: {a}olhe só para o ponto á. [p=0.2] Os três ângulos ali formam {b}a reta érre, um ângulo raso. [p=0.3] O dois xis mais quinze vale cinquenta e cinco. [p=0.2] {c}Cento e oitenta menos cinquenta e cinco menos sessenta e cinco dá sessenta graus, [p=0.2] sem passar pela base."),
    dict(id="s09", block="atalho", text="Funciona porque {a}os ângulos da reta de cima copiam os ângulos da base. [p=0.2] É a mesma ideia que mostrou que a soma do triângulo dá cento e oitenta. [p=0.3] Não compensa quando {b}as retas não são paralelas: [p=0.2] aí os ângulos {c}não se copiam."),
    # questão 2: isósceles e ângulo externo
    dict(id="s10", block="questao2", text="{a}Questão dois. [p=0.2] No triângulo isósceles á bê cê, {b}á bê é igual a á cê. [p=0.2] Prolongando a base para além do cê, [p=0.2] o {c}ângulo externo no cê mede cento e quinze graus. [p=0.3] {d}Quanto mede cada ângulo do triângulo?"),
    dict(id="s11", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta2", text="Vamos lá. [p=0.2] O externo e o interno do cê formam um ângulo raso: [p=0.2] {a}cento e oitenta menos cento e quinze dá sessenta e cinco graus. [p=0.3] No isósceles, {b}os ângulos da base são iguais: o bê também mede sessenta e cinco graus. [p=0.3] Os ângulos da base somam cento e trinta graus. [p=0.2] Sobra o á: {c}cento e oitenta menos cento e trinta dá cinquenta graus."),
    dict(id="s13", block="resposta2", text="Para conferir, use o ângulo externo: [p=0.2] ele vale {a}a soma dos internos de longe. [p=0.2] {b}Cinquenta mais sessenta e cinco dá cento e quinze. [p=0.2] Bateu."),
    # questão 3: isósceles e existência do triângulo
    dict(id="s14", block="questao3", text="{a}Questão três. [p=0.2] Um terreno tem a forma de um triângulo isósceles. [p=0.2] Dois dos lados medem {b}cinco metros e onze metros. [p=0.3] {c}Quanto mede o terceiro lado? [p=0.2] {d}E qual é o perímetro, a volta inteira do terreno?"),
    dict(id="s15", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta3", text="Vamos lá. [p=0.2] No isósceles, o terceiro lado repete um dos outros: [p=0.2] {a}cinco ou onze. [p=0.3] Teste o cinco: {b}cinco mais cinco dá dez, menos que onze. [p=0.2] Os lados curtos não alcançam: {c}não fecha triângulo."),
    dict(id="s17", block="resposta3", text="Teste o onze: {a}onze mais cinco dá dezesseis, mais que onze. [p=0.2] Fecha. [p=0.3] O terceiro lado mede {b}onze metros. [p=0.2] Perímetro é a soma dos lados: {c}onze mais onze mais cinco dá vinte e sete metros. [p=0.3] Quem respondeu vinte e um {d}não testou se o triângulo existe."),
    # questão 4: congruência e bissetriz no isósceles
    dict(id="s18", block="questao4", text="{a}Questão quatro. [p=0.2] De novo um isósceles, {b}com á bê igual a á cê, [p=0.2] e a base bê cê com {c}dezesseis centímetros. [p=0.3] A bissetriz do ângulo em á corta a base no ponto {d}dê. [p=0.2] {e}Quanto mede bê dê? [p=0.2] {f}E o ângulo que a bissetriz faz com a base?"),
    dict(id="s19", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta4", text="Vamos lá. [p=0.2] Compare os triângulos {a}á bê dê e á cê dê. [p=0.2] {b}Lado: á bê igual a á cê. [p=0.2] {c}Ângulo: a bissetriz dividiu o á ao meio. [p=0.2] {d}Lado: á dê é o mesmo nos dois. [p=0.3] Lado, ângulo, lado: {e}congruentes."),
    dict(id="s21", block="resposta4", text="Então bê dê é igual a dê cê: {a}dezesseis dividido por dois dá oito centímetros. [p=0.3] E os ângulos no dê são iguais e somam cento e oitenta graus: [p=0.2] {b}noventa graus cada. [p=0.3] É o atalho do isósceles: {c}a linha do topo é bissetriz, mediana e altura ao mesmo tempo."),
    # questão 5: baricentro com equação
    dict(id="s22", block="questao5", text="{a}Última questão. [p=0.2] Na mediana á eme, o baricentro é o ponto {b}gê. [p=0.3] O pedaço á gê mede {c}três xis menos dois. [p=0.2] O pedaço gê eme mede {d}xis mais um. [p=0.3] {e}Quanto mede a mediana inteira?"),
    dict(id="s23", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s24", block="resposta5", text="Vamos lá. [p=0.2] O pedaço do vértice é {a}o dobro do pedaço do lado. [p=0.3] {b}Três xis menos dois igual a duas vezes, abre parênteses, xis mais um. [p=0.2] Distribuindo: {c}três xis menos dois igual a dois xis mais dois."),
    dict(id="s25", block="resposta5", text="Tire dois xis de cada lado e some dois: [p=0.2] {a}xis igual a quatro. [p=0.3] Então á gê mede {b}três vezes quatro menos dois, que dá dez. [p=0.2] E gê eme mede {c}quatro mais um, que dá cinco. [p=0.3] Dez é o dobro de cinco: confere. [p=0.2] A mediana mede {d}quinze."),
    dict(id="s26", block="resposta5", text="Cuidado com a armadilha: [p=0.2] quem achou xis e parou {a}respondeu quatro. [p=0.2] A pergunta era {b}a mediana inteira."),
    # fechamento
    dict(id="s27", block="fim", text="Resumindo: {a}desenhe a figura, [p=0.2] {b}marque o que é igual [p=0.2] e {c}confira se a resposta faz sentido."),
    dict(id="s28", block="fim", text="Na próxima aula, começa uma parte nova: [p=0.2] {a}o Teorema de Tales. [p=0.2] Retas paralelas cortam duas transversais, [p=0.2] e você acha {b}xis com pedaços de três e seis numa reta, [p=0.2] quatro e xis na outra. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
