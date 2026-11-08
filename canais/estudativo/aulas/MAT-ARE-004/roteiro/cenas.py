# Estudativo · MAT-ARE-004 — Área do trapézio e do losango (Matemática · Áreas e Perímetros).
# Habilidade: usar (B + b) · h / 2 e D · d / 2, como no trapézio de bases 10 e 6 e altura 4 (32).
# Pré-requisitos: MAT-ARE-003 (paralelogramo b·h, triângulo b·h/2, duas cópias). Usa MAT-POL-001 (bases do trapézio; diagonais do losango). Próxima: MAT-ARE-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas: "bê grande" (B), "bê pequeno" (b), "dê grande" (D), "dê pequeno" (d), "agá" (h).
# Visual:
#   s01, s04-s08, s12-s13: E.trapezio bases 10 e 6, altura 4 (tracejada, quadradinho do reto).
#   s05-s06: cópia girada 180° encostada ao lado → paralelogramo de base 10 + 6 = 16 e altura 4.
#   s08: uma diagonal corta o trapézio em dois triângulos de altura 4 (20 + 12).
#   s09-s11: losango de diagonais 8 e 6 cruzadas em ângulo reto; E.retangulo 8 × 6 em volta; 4 triângulos dentro e 4 iguais fora.
#   s12: E.retangulo 10 × 4 cobrindo o trapézio (área 40 < 64, o 64 riscado em vermelho).
#   s13: base média 8 no meio da altura; as pontas que sobram completam as que faltam.
#   s15-s18: terreno trapézio bases 25 m e 15 m, altura 12 m; pipa losango de diagonais 50 cm e 30 cm.

TITULO = "Área do trapézio e do losango"

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
    dict(id="s01", block="gancho", text="{a}Um trapézio com base maior dez, base menor seis e altura quatro. [p=0.3] São {b}duas bases de tamanhos diferentes. [p=0.2] Qual delas entra na conta da área? [p=0.3] {c}As duas, [p=0.2] e a área dá {d}trinta e dois."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula a área de qualquer trapézio e losango, [p=0.2] sabe de onde vem cada fórmula [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}a área do paralelogramo é base vezes altura, e a do triângulo é a metade disso; [p=0.2] {c}os lados paralelos do trapézio são as bases; [p=0.2] e {d}as diagonais do losango se cruzam em ângulo reto e se cortam ao meio. [p=0.3] Se faltar alguma, procure no canal."),
    # trapézio
    dict(id="s04", block="trapezio", text="No trapézio, chame {a}a base maior de bê grande [p=0.2] e {b}a base menor de bê pequeno. [p=0.2] {c}A altura é a distância entre as bases, medida em ângulo reto."),
    dict(id="s05", block="trapezio", text="Faça como no triângulo: [p=0.2] {a}pegue uma cópia, [p=0.2] {b}gire de cabeça para baixo [p=0.2] e {c}encoste ao lado. [p=0.3] Juntos, os trapézios formam {d}um paralelogramo. [p=0.2] Embaixo, a base grande de um continua na base pequena do outro: [p=0.2] a base do paralelogramo é {e}bê grande mais bê pequeno."),
    dict(id="s06", block="trapezio", text="A área do paralelogramo é {a}bê grande mais bê pequeno, vezes a altura. [p=0.2] Cada trapézio é {b}a metade. [p=0.3] A fórmula: {c}á igual a bê grande mais bê pequeno, entre parênteses, vezes agá, dividido por dois."),
    dict(id="s07", block="trapezio", text="Base maior dez, base menor seis e altura quatro. [p=0.2] {a}Dez mais seis dá dezesseis. [p=0.2] {b}Dezesseis vezes quatro dá sessenta e quatro. [p=0.2] {c}Dividido por dois dá trinta e dois."),
    dict(id="s08", block="trapezio", text="Confira por outro caminho: [p=0.2] {a}uma diagonal corta o trapézio em dois triângulos de altura quatro. [p=0.2] {b}Dez vezes quatro, dividido por dois, dá vinte. [p=0.2] {c}Seis vezes quatro, dividido por dois, dá doze. [p=0.2] {d}Vinte mais doze dá trinta e dois. [p=0.2] Bateu."),
    # losango
    dict(id="s09", block="losango", text="Agora o losango. [p=0.2] Ele tem {a}duas diagonais: a maior, dê grande, [p=0.2] e a menor, dê pequeno. [p=0.3] Elas se cruzam em ângulo reto [p=0.1] e {b}cortam o losango em quatro triângulos iguais."),
    dict(id="s10", block="losango", text="Desenhe {a}um retângulo em volta, com os lados do tamanho das diagonais. [p=0.2] Nele cabem {b}oito triângulos: [p=0.2] {c}quatro dentro do losango e quatro iguais a eles do lado de fora. [p=0.3] O losango é {d}metade do retângulo."),
    dict(id="s11", block="losango", text="A fórmula: {a}á igual a dê grande vezes dê pequeno, dividido por dois. [p=0.3] Diagonais de {b}oito e seis: [p=0.2] {c}oito vezes seis dá quarenta e oito, [p=0.2] {d}dividido por dois dá vinte e quatro."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}esquecer o dividido por dois. [p=0.2] No trapézio do começo, a pessoa para no {b}sessenta e quatro. [p=0.3] Mas um retângulo de {c}dez por quatro cobre o trapézio inteiro, e tem só quarenta. [p=0.2] A área do trapézio {d}não pode passar disso."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}a base do meio. [p=0.3] Tire a média das bases: [p=0.2] {b}dez mais seis dá dezesseis, e a metade dá oito. [p=0.2] {c}Oito vezes quatro dá trinta e dois. [p=0.2] O trapézio vale {d}um retângulo com a base do meio."),
    dict(id="s14", block="atalho", text="Funciona porque {a}bê grande mais bê pequeno, dividido por dois, já é a média das bases: [p=0.2] é a mesma conta da fórmula, só que com a divisão feita antes. [p=0.3] {b}Não compensa quando a soma das bases é ímpar e a altura é par, [p=0.2] como base maior sete, base menor quatro e altura seis. [p=0.2] Aí, {c}tire a metade da altura: [p=0.2] onze vezes três dá trinta e três."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Um terreno tem forma de trapézio, com {a}base maior de vinte e cinco metros e base menor de quinze metros, [p=0.2] e {b}doze metros de distância entre elas. [p=0.3] {c}Qual é a área? [p=0.3] E uma pipa em forma de losango tem {d}diagonais de cinquenta e trinta centímetros. [p=0.2] {e}Quanto papel ela usa?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Os doze metros são {a}a distância entre as bases: a altura. [p=0.2] Pela base do meio, {b}vinte e cinco mais quinze dá quarenta, e a metade dá vinte. [p=0.2] {c}Vinte vezes doze dá duzentos e quarenta metros quadrados."),
    dict(id="s18", block="resposta", text="Na pipa, {a}cinquenta vezes trinta dá mil e quinhentos. [p=0.2] {b}Dividido por dois dá setecentos e cinquenta centímetros quadrados de papel."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}trapézio, soma das bases vezes altura, dividido por dois. [p=0.2] {b}Losango, diagonal vezes diagonal, dividido por dois."),
    dict(id="s20", block="fim", text="Na próxima aula, você calcula a área do {a}triângulo equilátero com uma fórmula só, [p=0.2] e descobre que {b}o hexágono regular é feito de seis desses triângulos. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
