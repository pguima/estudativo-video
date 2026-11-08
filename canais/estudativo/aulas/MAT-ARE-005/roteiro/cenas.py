# Estudativo · MAT-ARE-005 — Área do triângulo equilátero e do hexágono regular (Matemática · Áreas e Perímetros).
# Habilidade: usar ℓ²√3/4 e dividir o hexágono regular em 6 triângulos equiláteros: lado 2 dá área 6√3.
# Pré-requisitos: MAT-ANG-017 (h = ℓ√3/2), MAT-ARE-003 (b·h/2), MAT-POL-003 (regular; 120° no hexágono). Próxima: MAT-ARE-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas como em MAT-ANG-017: "éle" (lado), "á" (área). Aproximação √3 ≈ 1,7, a mesma de MAT-ANG-017.
# Visual:
#   s01, s07-s09: E.regular(6) de lado 2, ligado ao centro: seis triângulos que acendem um a um; 60° no centro; 120° de um canto partido em 60° + 60°.
#   s04-s06: equilátero de lado 6 (E.marcas_iguais), altura 3√3 com quadradinho do reto; fórmula ℓ²√3/4 com legenda.
#   s10: E.retangulo 6 × 3√3 em volta do equilátero; 18√3 é o retângulo inteiro (vermelho), o triângulo é metade.
#   s11-s12: ℓ²/4 = (ℓ/2)²: lado 6 → 3² → 9√3; lado 8 → 4² → 16√3; lado 5 → 25√3/4.
#   s13-s16: ladrilho hexagonal de lado 10 cm; 6 × 25√3 = 150√3 ≈ 255 cm².

TITULO = "Área do triângulo equilátero e do hexágono regular"

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
    dict(id="s01", block="gancho", text="{a}Um hexágono regular de lado dois. [p=0.2] Qual é a área? [p=0.3] Parece que precisa de uma fórmula nova. [p=0.2] Não precisa: {b}corte o hexágono em seis triângulos, [p=0.2] e a área sai {c}seis raiz de três: [p=0.2] pouco mais que dez."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula a área de qualquer triângulo equilátero e de qualquer hexágono regular, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}a área do triângulo é base vezes altura, dividido por dois; [p=0.2] {c}a altura do equilátero é éle raiz de três, dividido por dois; [p=0.2] e {d}o polígono regular tem lados iguais e ângulos iguais, com cento e vinte graus em cada canto do hexágono. [p=0.3] Se faltar alguma, procure no canal."),
    # equilátero
    dict(id="s04", block="equilatero", text="Comece pelo equilátero de {a}lado seis. [p=0.2] A base é seis, e a altura é {b}três raiz de três. [p=0.3] {c}Seis vezes três raiz de três dá dezoito raiz de três. [p=0.2] {d}Dividido por dois dá nove raiz de três."),
    dict(id="s05", block="equilatero", text="Com um lado qualquer, éle, a conta é a mesma. [p=0.2] {a}A base é éle. [p=0.2] {b}A altura é éle raiz de três, dividido por dois. [p=0.3] Base vezes altura dá {c}éle ao quadrado raiz de três, dividido por dois. [p=0.2] E a metade disso dá {d}éle ao quadrado raiz de três, dividido por quatro."),
    dict(id="s06", block="equilatero", text="Essa é a fórmula: {a}á igual a éle ao quadrado, vezes raiz de três, dividido por quatro. [p=0.2] {b}Éle é o lado. [p=0.3] Confira com o lado seis: [p=0.2] {c}seis ao quadrado dá trinta e seis, [p=0.2] {d}trinta e seis dividido por quatro dá nove. [p=0.2] {e}Nove raiz de três de novo."),
    # hexágono
    dict(id="s07", block="hexagono", text="Agora o hexágono regular. [p=0.2] {a}Ligue o centro aos seis vértices. [p=0.2] Aparecem {b}seis triângulos iguais, [p=0.2] e a volta em torno do centro se reparte em seis: [p=0.2] {c}trezentos e sessenta dividido por seis dá sessenta graus no centro de cada um."),
    dict(id="s08", block="hexagono", text="E nos cantos do hexágono? [p=0.2] Cada um tem {a}cento e vinte graus, [p=0.2] e a linha que vem do centro {b}divide esse canto ao meio, e cento e vinte dividido por dois dá sessenta. [p=0.3] {c}Três ângulos de sessenta graus: [p=0.2] cada triângulo é {d}equilátero, com o lado igual ao lado do hexágono."),
    dict(id="s09", block="hexagono", text="Então {a}a área do hexágono é seis vezes a área do triângulo. [p=0.3] Lado dois: {b}dois ao quadrado dá quatro, e quatro dividido por quatro dá um. [p=0.2] Cada triângulo tem {c}raiz de três. [p=0.2] O hexágono tem {d}seis raiz de três. [p=0.3] Raiz de três é perto de um vírgula sete. [p=0.2] {e}Seis vezes um vírgula sete dá dez vírgula dois."),
    # erro
    dict(id="s10", block="erro", text="O erro mais comum é {a}dividir por dois em vez de quatro. [p=0.2] No lado seis, a pessoa acha {b}dezoito raiz de três, mais de trinta. [p=0.3] Mas esse é o retângulo em volta do triângulo, com {c}base seis e altura três raiz de três. [p=0.2] O triângulo é {d}metade desse retângulo: [p=0.2] não pode ter a área dele inteira."),
    # atalho
    dict(id="s11", block="atalho", text="Agora o atalho, para lado par: {a}use a metade do lado. [p=0.3] {b}Éle ao quadrado, dividido por quatro, é a metade do lado ao quadrado. [p=0.2] Lado seis: {c}a metade é três, e três ao quadrado dá nove, então a área é nove raiz de três. [p=0.2] Lado oito: {d}a metade é quatro, e quatro ao quadrado dá dezesseis, então a área é dezesseis raiz de três."),
    dict(id="s12", block="atalho", text="Funciona porque {a}quatro é dois ao quadrado: [p=0.2] dividir o quadrado por quatro dá o mesmo que elevar a metade ao quadrado. [p=0.3] {b}Não compensa com lado ímpar: [p=0.2] lado cinco dá {c}vinte e cinco raiz de três, dividido por quatro. [p=0.2] Aí, {d}deixe o quatro embaixo."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] Um piso é feito de ladrilhos em forma de {a}hexágono regular com dez centímetros de lado. [p=0.3] {b}Qual é a área de um ladrilho? [p=0.2] Use {c}raiz de três igual a um vírgula sete."),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] O ladrilho tem {a}seis triângulos equiláteros de lado dez. [p=0.2] Pelo atalho, {b}a metade de dez é cinco, e cinco ao quadrado dá vinte e cinco. [p=0.2] Cada triângulo tem {c}vinte e cinco raiz de três."),
    dict(id="s16", block="resposta", text="{a}Seis vezes vinte e cinco dá cento e cinquenta. [p=0.2] O ladrilho tem {b}cento e cinquenta raiz de três centímetros quadrados. [p=0.3] {c}Cento e cinquenta vezes um vírgula sete dá duzentos e cinquenta e cinco centímetros quadrados."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}equilátero, éle ao quadrado vezes raiz de três, dividido por quatro. [p=0.2] {b}Hexágono regular, seis desses triângulos."),
    dict(id="s18", block="fim", text="Na próxima aula, uma pergunta de quem vai cercar um terreno: [p=0.2] {a}com quarenta metros de cerca, qual retângulo guarda a maior área? [p=0.2] A resposta sai {b}do vértice de uma parábola. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
