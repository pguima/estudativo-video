# Estudativo · MAT-ESP-015 — Partes da esfera: hemisfério, fuso e seção (Matemática · Geometria Espacial · Esfera).
# Habilidade: achar o volume de um hemisfério, a área de um fuso de 30° e o raio do círculo cortado a 3 cm do centro de uma esfera de raio 5 (4 cm).
# Pré-requisitos: MAT-ESP-014 (A = 4πr², V = 4πr³/3, "círculo do meio", atalho π = 3), MAT-ANG-015 (Pitágoras), MAT-RAZ-006 (tabela e cruz). Usa MAT-ARE-008 (setor proporcional ao ângulo; ângulo como fração da volta). Próxima: MAT-ESP-016.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Ternos pitagóricos (MAT-ANG-016) não entram: Pitágoras com conta.
# Questão inédita, criada para esta aula.
# Contas: hemisfério r = 3: esfera 36π, metade 18π = 2π·27/3. Área do hemisfério fechado: 2πr² + πr² = 3πr² = 27π (r = 3).
#   Fuso 30°, r = 6: 4π·36 = 144π; 360x = 30·144π = 4.320π → x = 12π (= 144π/12). Seção: 5² − 3² = 25 − 9 = 16 → 4. Erro: 25 + 9 = 34, √34 ≈ 5,83 > 5.
#   Questão: r = 10, 6 gomos: 360/6 = 60° = 1/6; 4·3·100 = 1.200 cm²; 1.200/6 = 200 cm². Corte a 6: 100 − 36 = 64 → 8 cm.
# Visual:
#   s01, s11-s13: E.esfera (laranja) cortada por um plano a 3 do centro; triângulo retângulo 3-4-5 dentro (centro, centro do corte, borda).
#   s04-s06: E.esfera partida em dois hemisférios; meia casca = 2 círculos, tampa = 1 círculo.
#   s07-s10: E.esfera com gomos (fusos) de polo a polo, ângulo de 30° visto de cima; tabela 360° → 144π, 30° → x.
#   s14: corte "maior que o círculo do meio" em vermelho. s15-s16: palco escuro com os círculos contados (4, 2, 3).

TITULO = "Partes da esfera: hemisfério, fuso e seção"

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
    dict(id="s01", block="gancho", text="{a}Uma laranja de cinco centímetros de raio. [p=0.2] Você corta {b}reto, a três centímetros do centro. [p=0.3] Qual o raio do círculo que aparece no corte? [p=0.3] {c}Quatro centímetros, [p=0.2] e quem dá essa resposta é Pitágoras."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula as partes da esfera: [p=0.2] a metade, o gomo e o corte, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}a área e o volume da esfera; [p=0.2] {c}o teorema de Pitágoras; [p=0.2] e {d}a regra de três direta, com a tabela e a cruz. [p=0.3] Se faltar alguma, procure no canal."),
    # hemisfério
    dict(id="s04", block="hemisferio", text="{a}Corte a esfera bem no meio. [p=0.2] Saem {b}duas metades iguais, os hemisférios, [p=0.2] como uma tigela fechada por uma tampa reta. [p=0.3] O volume é {c}metade do volume da esfera."),
    dict(id="s05", block="hemisferio", text="Com {a}raio três, a esfera tem trinta e seis pi. [p=0.2] {b}Metade dá dezoito pi. [p=0.3] Na fórmula, {c}dois pi érre ao cubo, dividido por três."),
    dict(id="s06", block="hemisferio", text="E a área? [p=0.2] O hemisfério tem {a}metade da casca, [p=0.2] que vale {b}dois círculos do meio, [p=0.2] e mais {c}a tampa reta, outro círculo. [p=0.3] Ficam {d}três pi érre ao quadrado. [p=0.2] Com raio três, {e}três vezes nove dá vinte e sete pi."),
    # fuso
    dict(id="s07", block="fuso", text="Agora {a}o fuso. [p=0.2] É {b}a casca de um gomo, como os gomos de uma bola de praia. [p=0.2] Ele vai do ponto mais alto ao mais baixo da bola [p=0.2] e abre num {c}ângulo, como uma fatia de pizza vista de cima."),
    dict(id="s08", block="fuso", text="{a}Dobrou o ângulo, o gomo dobra: [p=0.2] área e ângulo são {b}diretamente proporcionais. [p=0.2] A volta toda, {c}trezentos e sessenta graus, é a esfera inteira. [p=0.3] Então, {d}regra de três."),
    dict(id="s09", block="fuso", text="Fuso de {a}trinta graus numa esfera de raio seis. [p=0.2] {b}Esfera inteira: seis ao quadrado dá trinta e seis, [p=0.2] e quatro pi vezes trinta e seis dá cento e quarenta e quatro pi. [p=0.3] Na tabela, {c}trezentos e sessenta graus para cento e quarenta e quatro pi; [p=0.2] {d}trinta graus para xis."),
    dict(id="s10", block="fuso", text="Cruz: {a}trezentos e sessenta xis igual a trinta vezes cento e quarenta e quatro pi, [p=0.2] que dá quatro mil trezentos e vinte pi. [p=0.2] Dividindo por trezentos e sessenta, {b}xis igual a doze pi. [p=0.3] Com o gomo inteiro, a casca e a parte de dentro, como um gomo de laranja, o pedaço se chama {c}cunha. [p=0.2] Ela vale a mesma fração do volume: [p=0.2] trinta graus são {d}um doze avos da volta, [p=0.2] então essa cunha é um doze avos da esfera."),
    # seção
    dict(id="s11", block="corte", text="Por último, {a}o corte. [p=0.2] Corte a esfera com uma faca reta, em qualquer lugar: [p=0.2] {b}aparece sempre um círculo. [p=0.2] Pelo centro, é {c}o círculo do meio, o maior. [p=0.2] Longe do centro, {d}um círculo menor."),
    dict(id="s12", block="corte", text="Na laranja de raio cinco, cortada a três do centro: [p=0.2] ligue {a}o centro da laranja ao centro do corte, que dá três. [p=0.2] Depois, {b}o centro do corte à borda do corte: é o raio que você quer. [p=0.2] E feche com {c}o centro da laranja até a borda: cinco, o raio da esfera."),
    dict(id="s13", block="corte", text="É {a}um triângulo retângulo, e o raio da esfera é a hipotenusa. [p=0.2] {b}Cinco ao quadrado dá vinte e cinco. [p=0.2] {c}Três ao quadrado dá nove. [p=0.2] {d}Vinte e cinco menos nove dá dezesseis, [p=0.2] e {e}a raiz de dezesseis é quatro. [p=0.3] O corte tem {f}quatro centímetros de raio."),
    # erro comum
    dict(id="s14", block="erro", text="O erro mais comum é {a}somar os quadrados. [p=0.2] Vinte e cinco mais nove dá trinta e quatro, [p=0.2] e a raiz de trinta e quatro {b}passa de cinco. [p=0.3] Um corte maior que o círculo do meio? [p=0.2] {c}Impossível. [p=0.2] O raio da esfera é a hipotenusa, o lado maior: [p=0.2] {d}subtraia."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho, para a área do hemisfério: {a}conte círculos. [p=0.2] {b}A esfera inteira vale quatro círculos do meio. [p=0.2] {c}A meia casca vale dois. [p=0.2] {d}Com a tampa, três. [p=0.3] Área do hemisfério fechado: {e}três pi érre ao quadrado, sem decorar fórmula nova."),
    dict(id="s16", block="atalho", text="Funciona porque {a}tudo é medido no mesmo círculo, de área pi érre ao quadrado. [p=0.3] {b}Cuidado com a tigela aberta ou a cúpula sem piso: [p=0.2] não tem tampa, [p=0.2] então {c}são só dois círculos."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Uma bola de plástico tem {a}dez centímetros de raio e {b}seis gomos iguais. [p=0.2] {c}Use pi igual a três. [p=0.3] {d}Quanto plástico tem um gomo? [p=0.2] E se você cortar a bola reto, {e}a seis centímetros do centro, [p=0.2] {f}qual o raio do círculo do corte?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Seis gomos iguais dividem a volta: [p=0.2] {a}trezentos e sessenta dividido por seis dá sessenta graus, [p=0.2] ou {b}um sexto da bola. [p=0.3] Bola inteira: {c}quatro vezes três vezes cem dá mil e duzentos centímetros quadrados. [p=0.2] {d}Um sexto de mil e duzentos dá duzentos centímetros quadrados por gomo."),
    dict(id="s20", block="resposta", text="No corte: {a}dez ao quadrado dá cem, [p=0.2] e {b}seis ao quadrado dá trinta e seis. [p=0.2] {c}Cem menos trinta e seis dá sessenta e quatro, [p=0.2] e {d}a raiz de sessenta e quatro é oito. [p=0.3] {e}Oito centímetros de raio, menor que dez: faz sentido."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}hemisfério, metade do volume e três círculos de área; [p=0.2] {b}fuso, a fração do ângulo; [p=0.2] {c}corte, Pitágoras com o raio da esfera na hipotenusa."),
    dict(id="s22", block="fim", text="Na próxima aula, você pratica tudo isso: [p=0.2] {a}escolhe a fórmula de cada sólido, pirâmide, cone ou esfera, [p=0.2] em questões de {b}casquinha, tenda, bola e reservatório. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
