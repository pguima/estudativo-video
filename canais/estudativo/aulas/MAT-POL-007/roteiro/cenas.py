# Estudativo · MAT-POL-007 — Tangente, corda e posições relativas (Matemática · Geometria Plana: Polígonos e Círculo).
# Habilidade: dizer se uma reta é externa, tangente ou secante, usar que a tangente faz 90° com o raio e achar com Pitágoras a corda a 5 cm do centro num círculo de raio 13 (24 cm).
# Pré-requisitos: MAT-ANG-008 (no isósceles, a linha do topo é altura e mediana), MAT-ANG-015 (Pitágoras e o atalho da soma vezes diferença), MAT-POL-004 (raio). Próxima: MAT-POL-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas como se falam: "pê".
# Visual: E.circulo com E.segmento para retas e distâncias; E.angulo (quadradinho do reto).
#   s04-s07: raio 5 e três retas paralelas a 7 (externa), 5 (tangente) e 3 (secante) do centro, com a distância tracejada em ângulo reto.
#   s08-s09: roda parada no chão; raio até o ponto de contato, com o quadradinho do reto.
#   s10-s11: ponto P a 10 do centro, raio 6 até o ponto de tangência, tangente 8 (triângulo 6-8-10).
#   s12-s16: raio 13, corda a 5 do centro; perpendicular do centro corta a corda ao meio (E.marcas_iguais), triângulo 5-12-13; corda 24.
#   Questão: raio 10, corda 16 (metade 8), distância 6; reta a 12 do centro, externa.

TITULO = "Tangente, corda e posições relativas"

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
    dict(id="s01", block="gancho", text="{a}Uma circunferência de raio treze centímetros. [p=0.2] {b}Uma corda passa a cinco centímetros do centro. [p=0.3] {c}Quanto mede essa corda? [p=0.3] Muita gente faz Pitágoras e responde {d}doze. [p=0.2] A resposta certa é {e}vinte e quatro."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você diz como uma reta fica diante de uma circunferência, [p=0.2] {b}acha tangentes e cordas com Pitágoras [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}o raio vai do centro até a circunferência; [p=0.2] {c}no triângulo isósceles, a linha que sai do topo e chega na base em ângulo reto corta a base ao meio; [p=0.2] e {d}o teorema de Pitágoras. [p=0.3] Se faltar alguma, procure no canal."),
    # posições relativas
    dict(id="s04", block="posicoes", text="Uma reta pode ficar de {a}três jeitos diante de uma circunferência. [p=0.2] Quem decide é {b}a distância do centro até a reta. [p=0.3] Essa distância é {c}o caminho mais curto, [p=0.2] que chega na reta {d}em ângulo reto, como a altura de um triângulo."),
    dict(id="s05", block="posicoes", text="Pegue uma circunferência de {a}raio cinco. [p=0.2] Uma reta a {b}sete do centro: [p=0.2] sete é mais que o raio, então ela passa longe. [p=0.2] É uma reta {c}externa: não toca a circunferência."),
    dict(id="s06", block="posicoes", text="Uma reta a {a}cinco do centro, igual ao raio, [p=0.2] {b}só encosta, num ponto. [p=0.2] É a reta {c}tangente. [p=0.3] Uma reta a {d}três do centro, menos que o raio, [p=0.2] entra e {e}corta a circunferência em dois pontos. [p=0.2] É a reta {f}secante."),
    dict(id="s07", block="posicoes", text="A regra: {a}distância maior que o raio, externa. [p=0.2] {b}Igual ao raio, tangente. [p=0.2] {c}Menor que o raio, secante."),
    # tangente
    dict(id="s08", block="tangente", text="A tangente tem uma propriedade que cai muito em prova. [p=0.2] Pense numa {a}roda parada no chão. [p=0.2] O chão é {b}tangente à roda. [p=0.3] E o raio que vai do centro até o ponto de contato {c}fica em pé: [p=0.2] faz {d}noventa graus com o chão."),
    dict(id="s09", block="tangente", text="Por quê? [p=0.2] O ponto de contato é {a}o ponto da reta mais perto do centro: [p=0.2] ele está a um raio, e o resto da reta fica do lado de fora. [p=0.3] E o caminho mais curto até uma reta {b}chega em ângulo reto. [p=0.2] Então, {c}a tangente faz noventa graus com o raio no ponto de contato."),
    dict(id="s10", block="tangente", text="Esse ângulo reto cria {a}triângulos retângulos. [p=0.2] De um ponto {b}pê, a dez centímetros do centro, [p=0.2] sai uma tangente até uma circunferência de {c}raio seis. [p=0.3] O raio e a tangente são os catetos, [p=0.2] e o segmento de pê até o centro, de frente para o ângulo reto, é {d}a hipotenusa."),
    dict(id="s11", block="tangente", text="{a}Dez ao quadrado dá cem. [p=0.2] {b}Seis ao quadrado dá trinta e seis. [p=0.2] {c}Cem menos trinta e seis dá sessenta e quatro. [p=0.2] A raiz dá oito: {d}a tangente mede oito centímetros."),
    # corda
    dict(id="s12", block="corda", text="Na reta secante, o pedaço que fica dentro da circunferência é {a}uma corda: [p=0.2] o segmento que liga dois pontos da circunferência. [p=0.3] {b}A maior corda é o diâmetro, que passa pelo centro."),
    dict(id="s13", block="corda", text="Ligue o centro {a}às duas pontas da corda: [p=0.2] são dois raios, do mesmo tamanho. [p=0.2] Nasce um {b}triângulo isósceles, com o topo no centro e a corda como base. [p=0.3] Na aula das linhas do triângulo, você viu que, no isósceles, a linha do topo que chega na base em ângulo reto também corta a base ao meio. [p=0.3] Então a linha que sai do centro e chega na corda em ângulo reto {c}corta a corda ao meio."),
    dict(id="s14", block="corda", text="Volte ao começo: {a}raio treze, corda a cinco do centro. [p=0.2] Ligue o centro {b}a uma ponta da corda: esse raio é a hipotenusa. [p=0.2] Os catetos são {c}a distância, cinco, [p=0.2] e {d}a metade da corda."),
    dict(id="s15", block="corda", text="{a}Treze ao quadrado dá cento e sessenta e nove. [p=0.2] {b}Cinco ao quadrado dá vinte e cinco. [p=0.2] {c}Cento e sessenta e nove menos vinte e cinco dá cento e quarenta e quatro. [p=0.2] {d}A raiz é doze: essa é a metade. [p=0.2] {e}A corda inteira mede vinte e quatro centímetros."),
    # erro
    dict(id="s16", block="erro", text="O erro mais comum é {a}parar no doze. [p=0.2] O triângulo vai {b}da ponta da corda só até o meio dela, [p=0.2] então Pitágoras dá {c}a metade. [p=0.3] {d}Antes de responder, dobre."),
    # atalho
    dict(id="s17", block="atalho", text="Agora o atalho, o mesmo da aula de Pitágoras: [p=0.2] {a}soma vezes diferença. [p=0.3] {b}Treze mais cinco dá dezoito. [p=0.2] {c}Treze menos cinco dá oito. [p=0.2] {d}Dezoito vezes oito dá cento e quarenta e quatro. [p=0.2] A raiz dá {e}doze, e a corda mede {f}vinte e quatro."),
    dict(id="s18", block="atalho", text="Funciona porque {a}raio ao quadrado menos distância ao quadrado é uma diferença de dois quadrados, [p=0.2] e ela é {b}a soma vezes a diferença. [p=0.3] {c}Não serve quando o que falta é o raio: [p=0.2] ele é a hipotenusa, e aí {d}os quadrados se somam."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Uma circunferência tem {a}raio de dez centímetros, [p=0.2] e uma corda dela mede {b}dezesseis. [p=0.3] {c}A que distância do centro fica essa corda? [p=0.3] E {d}uma reta a doze centímetros do centro é externa, tangente ou secante?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] O raio é a hipotenusa, [p=0.2] e {a}a metade da corda é oito. [p=0.3] Pelo atalho: {b}dez mais oito dá dezoito. [p=0.2] {c}Dez menos oito dá dois. [p=0.2] {d}Dezoito vezes dois dá trinta e seis. [p=0.2] A raiz dá {e}seis centímetros."),
    dict(id="s22", block="resposta", text="Conferindo: {a}seis ao quadrado mais oito ao quadrado dá cem, [p=0.2] que é dez ao quadrado. [p=0.3] Na segunda parte, {b}doze é mais que o raio. [p=0.2] A reta passa longe: {c}é externa."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}compare a distância com o raio, [p=0.2] {b}a tangente faz noventa graus com o raio, [p=0.2] e, {c}na corda, Pitágoras dá a metade."),
    dict(id="s24", block="fim", text="Na próxima aula, {a}duas cordas se cruzam dentro da circunferência, [p=0.2] e os pedaços de uma, {b}multiplicados, dão o mesmo que os pedaços da outra. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
