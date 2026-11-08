# Estudativo · MAT-ARE-003 — Área do paralelogramo e do triângulo (Matemática · Áreas e Perímetros).
# Habilidade: mostrar por que o triângulo é metade de um paralelogramo e calcular a área de um triângulo de base 10 e altura 6 (30).
# Pré-requisitos: MAT-ANG-008 (altura: em ângulo reto, pode cair fora), MAT-ARE-002 (base vezes altura). Próxima: MAT-ARE-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Divisão com resultado decimal (MAT-FRA-017) fora da cadeia: 35/2 é dito "dezessete e meio".
# Visual:
#   s01, s09: E.triangulo de base 10 e altura 6 dentro do E.retangulo 10 × 6 (as duas sobras laterais somam a outra metade).
#   s04-s06: E.paralelogramo base 8, lado inclinado 5, altura 4 (desloca 3), altura tracejada com quadradinho do reto;
#            o triângulo da ponta esquerda desliza para a direita e forma o retângulo 8 × 4.
#   s07-s08: triângulo + cópia girada 180° encostada no lado → paralelogramo de mesma base e altura.
#   s10: obtusângulo com a altura caindo fora (lado prolongado tracejado, como em MAT-ANG-008); triângulo retângulo de catetos 6 e 8.
#   s11: o mesmo paralelogramo com o lado 5 riscado em vermelho (40) e a altura 4 em verde (32).
#   s14-s17: bandeirinha triangular de base 30 cm e altura 45 cm (altura do bico até a base, em ângulo reto).

TITULO = "Área do paralelogramo e do triângulo"

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
    dict(id="s01", block="gancho", text="{a}Um triângulo de base dez e altura seis. [p=0.3] A área é {b}dez vezes seis, que dá sessenta? [p=0.3] Sessenta é {c}o retângulo inteiro em volta dele. [p=0.2] O triângulo ocupa {d}só a metade, e a metade de sessenta dá trinta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula a área de qualquer paralelogramo e de qualquer triângulo, [p=0.2] entende de onde vem cada fórmula [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}a área do retângulo é base vezes altura, [p=0.2] e {c}a altura de um triângulo sai de um vértice e chega na reta do lado da frente em ângulo reto, [p=0.2] às vezes caindo fora dele. [p=0.3] Se faltar alguma, procure no canal."),
    # paralelogramo
    dict(id="s04", block="paralelogramo", text="Comece pelo paralelogramo, que tem {a}dois pares de lados paralelos. [p=0.2] A base mede {b}oito centímetros. [p=0.2] Do alto, desça uma linha {c}em ângulo reto até a base: [p=0.2] essa é a altura, {d}quatro centímetros."),
    dict(id="s05", block="paralelogramo", text="{a}Recorte o triângulo dessa ponta [p=0.2] e {b}encaixe do outro lado. [p=0.3] Nada sobrou, nada faltou, [p=0.2] e a figura virou {c}um retângulo de base oito e altura quatro. [p=0.3] O pedaço se encaixa porque {d}os lados opostos do paralelogramo são iguais e paralelos."),
    dict(id="s06", block="paralelogramo", text="Então a área do paralelogramo é a mesma do retângulo: [p=0.2] {a}base vezes altura. [p=0.2] {b}Oito vezes quatro dá trinta e dois centímetros quadrados. [p=0.3] Aqui, a altura é {c}a distância entre os lados paralelos, medida em ângulo reto."),
    # triângulo
    dict(id="s07", block="triangulo", text="Agora o triângulo. [p=0.2] Pegue {a}um triângulo e uma cópia dele. [p=0.2] {b}Gire a cópia de cabeça para baixo [p=0.2] e {c}encoste num lado do primeiro. [p=0.3] Juntos, eles formam {d}um paralelogramo com a mesma base e a mesma altura."),
    dict(id="s08", block="triangulo", text="Cada triângulo é {a}metade desse paralelogramo. [p=0.2] Daí a fórmula: {b}á igual a bê vezes agá, dividido por dois. [p=0.2] {c}Bê é a base, [p=0.2] {d}agá é a altura que chega nessa base em ângulo reto."),
    dict(id="s09", block="triangulo", text="Base dez e altura seis: [p=0.2] {a}dez vezes seis dá sessenta. [p=0.2] {b}Dividido por dois dá trinta. [p=0.3] É o trinta do começo."),
    dict(id="s10", block="triangulo", text="A fórmula vale {a}para qualquer triângulo. [p=0.2] No obtusângulo, {b}a altura cai fora, [p=0.2] mas a conta é a mesma. [p=0.3] No triângulo retângulo, {c}os lados do ângulo reto já são base e altura. [p=0.2] Lados seis e oito: {d}seis vezes oito dá quarenta e oito, [p=0.2] dividido por dois dá vinte e quatro."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}usar o lado inclinado no lugar da altura. [p=0.2] No paralelogramo de base oito, o lado inclinado mede {b}cinco. [p=0.2] Oito vezes cinco dá {c}quarenta. [p=0.3] Mas o lado inclinado é {d}maior que a altura, que mede quatro. [p=0.2] A área certa é {e}trinta e dois. [p=0.2] Altura é sempre {f}a medida em ângulo reto."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: {a}divida por dois antes de multiplicar. [p=0.3] Base dez, altura seis: [p=0.2] {b}metade de dez dá cinco, [p=0.2] {c}cinco vezes seis dá trinta. [p=0.2] Números menores, conta de cabeça."),
    dict(id="s13", block="atalho", text="Funciona porque {a}tirar a metade de um dos números dá o mesmo que tirar a metade do produto. [p=0.2] {b}Escolha o número par para dividir. [p=0.3] {c}Não compensa quando base e altura são ímpares, [p=0.2] como sete e cinco: [p=0.2] aí, {d}multiplique primeiro. [p=0.2] Sete vezes cinco dá trinta e cinco, [p=0.1] e a metade dá {e}dezessete e meio."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Uma bandeirinha de festa é um triângulo com {a}base de trinta centímetros e altura de quarenta e cinco. [p=0.3] {b}Quantos centímetros quadrados de tecido tem uma bandeirinha? [p=0.2] {c}E quantos metros quadrados têm vinte bandeirinhas iguais?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá, pelo atalho. [p=0.2] {a}Metade de trinta dá quinze. [p=0.2] {b}Quinze vezes quarenta e cinco dá seiscentos e setenta e cinco centímetros quadrados. [p=0.3] {c}Seiscentos e setenta e cinco vezes vinte dá treze mil e quinhentos centímetros quadrados."),
    dict(id="s17", block="resposta", text="Do centímetro quadrado ao metro quadrado, {a}quatro casas para a esquerda, [p=0.2] e {b}treze mil e quinhentos centímetros quadrados dão um vírgula trinta e cinco metro quadrado. [p=0.3] Repare: o quarenta e cinco é {c}a medida em ângulo reto, do bico até a base, [p=0.2] e não o lado da bandeirinha."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}paralelogramo, base vezes altura. [p=0.2] {b}Triângulo, a metade disso. [p=0.2] E {c}a altura é sempre a medida em ângulo reto."),
    dict(id="s19", block="fim", text="Na próxima aula, a mesma ideia de juntar duas cópias resolve {a}o trapézio, [p=0.2] e um retângulo em volta resolve {b}o losango. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
