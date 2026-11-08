# Estudativo · MAT-ANG-017 — Diagonal do quadrado e altura do triângulo equilátero (Matemática · Geometria Plana: Ângulos e Triângulos).
# Habilidade: usar d = ℓ√2 e h = ℓ√3/2: um quadrado de lado 5 tem diagonal 5√2 ≈ 7 e um equilátero de lado 6 tem altura 3√3.
# Pré-requisitos: MAT-ANG-008 (altura; no isósceles a linha do topo é altura e mediana), MAT-ANG-015 (Pitágoras), MAT-POT-009 (simplificar radicais). Usa os múltiplos de MAT-ANG-016. Próxima: MAT-ANG-018.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas como se falam: "dê", "éle", "agá".
# Aproximações usadas (as mesmas de MAT-POT-009): √2 ≈ 1,4 e √3 ≈ 1,7.
# Visual:
#   s01-s06: quadrado de lado 5 (E.poligono, quatro retos) com a diagonal; um dos triângulos retângulos em destaque (catetos 5 e 5, hipotenusa d).
#   s07-s08: quadrado de lado 1 com diagonal √2, depois ampliado para lado 5 e lado 10; fórmula d = ℓ√2 com legendas.
#   s09-s13: equilátero de lado 6 (E.marcas_iguais), altura do topo com quadradinho do reto e a base partida em 3 e 3; metade da figura em destaque.
#   s12: equilátero de lado 2 (metade da base 1, altura √3) ao lado do de lado 6 (altura 3√3).
#   s14: altura errada 6√3 ≈ 10,4 desenhada passando do topo, em vermelho.
#   s17-s20: quadrado e equilátero lado a lado com o mesmo lado; diagonal 4√2.

TITULO = "Diagonal do quadrado e altura do triângulo equilátero"

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
    dict(id="s01", block="gancho", text="{a}Um quadrado de lado cinco. [p=0.2] Quanto mede {b}a diagonal, a linha de um canto ao canto oposto? [p=0.3] Muita gente responde {c}dez. [p=0.2] O certo é {d}cinco raiz de dois, um pouco mais que sete."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha a diagonal de qualquer quadrado [p=0.2] e {b}a altura de qualquer triângulo equilátero [p=0.2] numa conta só."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}o teorema de Pitágoras; [p=0.2] {c}no isósceles, a linha que sai do topo é altura e mediana ao mesmo tempo; [p=0.2] e {d}simplificar raiz, como raiz de setenta e dois virar seis raiz de dois. [p=0.3] Se faltar alguma, procure no canal."),
    # diagonal
    dict(id="s04", block="diagonal", text="A diagonal corta o quadrado em {a}dois triângulos retângulos. [p=0.2] Os catetos são {b}dois lados do quadrado, [p=0.2] e {c}a diagonal é a hipotenusa."),
    dict(id="s05", block="diagonal", text="Lado cinco: {a}vinte e cinco mais vinte e cinco dá cinquenta. [p=0.2] {b}A diagonal ao quadrado é cinquenta. [p=0.3] Cinquenta é {c}vinte e cinco vezes dois. [p=0.2] O vinte e cinco tem raiz exata, cinco, e sai da raiz: [p=0.2] {d}cinco raiz de dois."),
    dict(id="s06", block="diagonal", text="Com raiz de dois perto de um vírgula quatro, [p=0.2] {a}cinco vezes um vírgula quatro dá sete. [p=0.2] {b}Pouco mais de sete, [p=0.2] menos que os dez da volta pelos lados."),
    dict(id="s07", block="diagonal", text="E com qualquer lado? [p=0.2] Num quadrado de {a}lado um, a diagonal ao quadrado é {b}um mais um, que dá dois: [p=0.2] diagonal {c}raiz de dois. [p=0.3] Os outros quadrados são esse, ampliado. [p=0.2] E, como você viu nos ternos, {d}multiplicar os lados pelo mesmo número mantém Pitágoras."),
    dict(id="s08", block="diagonal", text="Então, lado cinco, diagonal {a}cinco raiz de dois. [p=0.2] Lado dez, diagonal {b}dez raiz de dois. [p=0.3] Na fórmula: {c}dê igual a éle raiz de dois. [p=0.2] {d}Dê é a diagonal, [p=0.2] {e}éle é o lado."),
    # altura
    dict(id="s09", block="altura", text="No triângulo equilátero, {a}os três lados são iguais. [p=0.2] Como ele tem dois lados iguais, e mais um, [p=0.2] vale para ele o que vale no isósceles: [p=0.2] a linha que sai do topo {b}é altura e mediana. [p=0.2] Ela {c}chega na base em ângulo reto e corta a base ao meio."),
    dict(id="s10", block="altura", text="Com lado seis, {a}a base fica com três de cada lado. [p=0.2] Nasce um triângulo retângulo com {b}hipotenusa seis, o lado do equilátero, [p=0.2] {c}um cateto três, a metade da base, [p=0.2] e {d}o outro cateto, a altura."),
    dict(id="s11", block="altura", text="Falta um cateto: subtração. [p=0.2] {a}Trinta e seis menos nove dá vinte e sete. [p=0.2] Vinte e sete é {b}nove vezes três. [p=0.2] O nove sai da raiz como três: [p=0.2] {c}a altura é três raiz de três."),
    dict(id="s12", block="altura", text="Num equilátero de {a}lado dois, a metade da base é um. [p=0.2] {b}Quatro menos um dá três: [p=0.2] altura {c}raiz de três. [p=0.3] O de lado seis é três vezes maior, [p=0.2] e a altura também: {d}três raiz de três. [p=0.3] Ou seja, a altura é {e}a metade do lado, vezes raiz de três."),
    dict(id="s13", block="altura", text="Na fórmula: {a}agá igual a éle raiz de três, dividido por dois. [p=0.2] {b}Agá é a altura, [p=0.2] {c}éle é o lado. [p=0.3] Lado seis: {d}seis raiz de três, dividido por dois, dá três raiz de três."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}esquecer o dividido por dois. [p=0.2] Com lado seis, a pessoa acha altura {b}seis raiz de três, [p=0.2] que passa de {c}dez. [p=0.3] Só que a altura é cateto de um triângulo com hipotenusa seis: [p=0.2] {d}não pode passar de seis. [p=0.2] {e}Três raiz de três dá um pouco mais que cinco, e esse cabe."),
    # atalho
    dict(id="s15", block="atalho", text="O atalho para não trocar as fórmulas: [p=0.2] {a}o quadrado leva raiz de dois. [p=0.2] {b}O triângulo leva raiz de três, [p=0.2] e {c}vem dividido por dois, porque a altura parte a base em duas metades."),
    dict(id="s16", block="atalho", text="Por que esses números? [p=0.2] {a}No quadrado, somam-se dois lados iguais: um mais um dá dois. [p=0.2] {b}No equilátero de lado dois, sai a metade: quatro menos um dá três. [p=0.3] {c}Não serve em retângulo comprido nem em triângulo que não seja equilátero. [p=0.2] Aí, {d}Pitágoras completo."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Um quadrado e um triângulo equilátero têm {a}o mesmo lado. [p=0.2] A diagonal do quadrado mede {b}quatro raiz de dois centímetros. [p=0.3] {c}Quanto mede a altura do triângulo?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] A diagonal é {a}o lado vezes raiz de dois. [p=0.2] Se deu quatro raiz de dois, {b}o lado mede quatro centímetros."),
    dict(id="s20", block="resposta", text="No triângulo, {a}a metade do lado é dois. [p=0.2] {b}A altura é dois raiz de três centímetros, [p=0.2] um pouco menos que {c}três e meio. [p=0.3] Conferindo por Pitágoras: {d}dezesseis menos quatro dá doze, [p=0.2] e {e}doze é quatro vezes três: dois raiz de três. [p=0.2] Bateu."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}diagonal do quadrado, lado vezes raiz de dois. [p=0.2] {b}Altura do equilátero, metade do lado vezes raiz de três."),
    dict(id="s22", block="fim", text="Na próxima aula, você traça {a}a altura que sai do ângulo reto e cai na hipotenusa, [p=0.2] e acha essa altura com {b}duas relações novas, [p=0.2] como {c}a altura de dois vírgula quatro no triângulo três, quatro e cinco. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
