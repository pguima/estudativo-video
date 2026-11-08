# Estudativo · MAT-ANG-019 — Praticando: Pitágoras e relações métricas (Matemática · Geometria Plana: Ângulos e Triângulos · prática).
# Habilidade: escolher entre Pitágoras, atalhos e relações métricas e achar medidas em figuras e situações reais.
# Pré-requisitos: MAT-ANG-015, MAT-ANG-016, MAT-ANG-017, MAT-ANG-018. Próxima: nenhuma na trilha; a seguinte na playlist Matemática do Zero é MAT-POL-001.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questões inéditas, criadas para esta aula. Letras narradas como se falam: "agá", "eme", "ene".
# Aproximações usadas (as mesmas de MAT-POT-009): √2 ≈ 1,4 e √3 ≈ 1,7.
# Visual:
#   Q1: terreno retangular 20 m × 21 m visto de cima, cerca na diagonal (29 m).
#   Q2: antena vertical de 12 m, cabo até o chão a 9 m do pé (15 m).
#   Q3: mesa quadrada de lado 80 cm com a diagonal 80√2 ≈ 113 cm e uma régua de 120 cm passando dos cantos.
#   Q4: triângulo equilátero de lado 30 cm (placa), altura 15√3 ≈ 26 cm, base partida em 15 e 15.
#   Q5: triângulo retângulo com a altura h partindo a hipotenusa em 9 e 16; os dois triângulos pequenos (9-12-15 e 12-16-20) e o grande (15-20-25).

TITULO = "Praticando: Pitágoras e relações métricas"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, a primeira tarefa é {b}escolher a ferramenta. [p=0.2] {c}Pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="As ferramentas: [p=0.2] {a}Pitágoras, somando para a hipotenusa e subtraindo para o cateto; [p=0.2] {b}os ternos três, quatro e cinco, [p=0.1] e cinco, doze e treze; [p=0.2] {c}a diagonal do quadrado e a altura do equilátero; [p=0.2] e {d}as relações métricas. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: Pitágoras na conta
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Um terreno retangular mede {b}vinte metros por vinte e um. [p=0.2] Uma cerca reta vai {c}de um canto ao canto oposto. [p=0.3] {d}Quantos metros tem a cerca?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] A cerca é {a}a hipotenusa, e os lados do terreno são os catetos. [p=0.2] Vinte metros e vinte e um metros {b}não formam terno conhecido: [p=0.2] vai na conta. [p=0.3] {c}Quatrocentos mais quatrocentos e quarenta e um dá oitocentos e quarenta e um."),
    dict(id="s06", block="resposta1", text="A raiz {a}fica entre vinte e trinta. [p=0.2] Vinte ao quadrado dá quatrocentos. [p=0.2] Trinta ao quadrado dá novecentos. [p=0.3] {b}Termina em um, então a raiz termina em um ou em nove. [p=0.2] Está bem mais perto de novecentos: {c}vinte e nove. [p=0.2] Conferindo: {d}vinte e nove ao quadrado dá oitocentos e quarenta e um. [p=0.3] A cerca tem {e}vinte e nove metros, [p=0.2] bem menos que {f}os quarenta e um da volta pelos lados."),
    # situação 2: terno
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Uma antena de {b}doze metros está em pé no chão. [p=0.2] Um cabo vai do alto dela até um ponto do chão {c}a nove metros do pé. [p=0.3] {d}Quanto mede o cabo?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] O cabo fica de frente para o ângulo reto: {a}é a hipotenusa. [p=0.2] {b}Nove e doze divididos por três dão três e quatro. [p=0.2] Terno {c}três, quatro e cinco. [p=0.2] {d}Cinco vezes três dá quinze: o cabo mede quinze metros. [p=0.3] Na conta: {e}oitenta e um mais cento e quarenta e quatro dá duzentos e vinte e cinco, [p=0.2] e {f}a raiz é quinze."),
    # situação 3: diagonal do quadrado
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] Uma mesa quadrada tem {b}oitenta centímetros de lado. [p=0.2] Você quer deitar sobre ela {c}uma régua de cento e vinte centímetros, de canto a canto, sem sobrar para fora. [p=0.3] {d}A régua cabe?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] De canto a canto é {a}a diagonal do quadrado: lado vezes raiz de dois. [p=0.2] {b}Oitenta raiz de dois. [p=0.2] Com raiz de dois perto de um vírgula quatro, [p=0.2] {c}oitenta vezes um vírgula quatro dá cento e doze. [p=0.2] Como raiz de dois passa um pouco de um vírgula quatro, [p=0.2] a diagonal tem pouco mais de cento e doze centímetros. [p=0.3] {d}A régua tem cento e vinte: não cabe, sobra para fora."),
    dict(id="s13", block="atalho", text="E um atalho para decidir sem arredondar: {a}compare os quadrados. [p=0.2] {b}A diagonal ao quadrado dá seis mil e quatrocentos mais seis mil e quatrocentos, que dá doze mil e oitocentos. [p=0.2] {c}Cento e vinte ao quadrado dá catorze mil e quatrocentos. [p=0.2] {d}A régua é maior."),
    dict(id="s14", block="atalho", text="Funciona porque, {a}entre medidas positivas, a maior tem o maior quadrado. [p=0.3] {b}Não serve quando a pergunta pede o valor da medida: [p=0.2] aí, {c}aproxime a raiz."),
    # situação 4: altura do equilátero
    dict(id="s15", block="questao4", text="{a}Situação quatro. [p=0.2] Uma placa tem forma de {b}triângulo equilátero, com trinta centímetros de lado. [p=0.3] {c}Qual a altura da placa?"),
    dict(id="s16", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta4", text="Vamos lá. [p=0.2] Altura do equilátero: {a}metade do lado, vezes raiz de três. [p=0.2] {b}Metade de trinta é quinze: quinze raiz de três centímetros. [p=0.3] Com raiz de três perto de um vírgula sete, [p=0.2] {c}quinze vezes um vírgula sete dá vinte e cinco vírgula cinco. [p=0.2] Raiz de três passa um pouco de um vírgula sete, [p=0.2] então {d}a altura fica perto de vinte e seis centímetros. [p=0.3] Quem esquece o dividido por dois acha {e}mais de cinquenta, [p=0.2] uma altura {f}maior que o próprio lado: impossível."),
    # situação 5: relações métricas
    dict(id="s18", block="questao5", text="{a}Última situação, e ela junta tudo. [p=0.2] Num triângulo retângulo, a altura relativa à hipotenusa parte a hipotenusa em {b}nove e dezesseis. [p=0.3] {c}Quanto medem a altura e os catetos?"),
    dict(id="s19", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta5", text="Vamos lá. [p=0.2] Com os pedaços, a relação é {a}agá ao quadrado igual a eme vezes ene. [p=0.2] {b}Nove vezes dezesseis dá cento e quarenta e quatro. [p=0.2] {c}A altura é doze."),
    dict(id="s21", block="resposta5", text="A altura e cada pedaço formam {a}um triângulo retângulo pequeno, [p=0.2] em que o cateto do grande é a hipotenusa. [p=0.3] {b}Nove e doze: terno três, quatro e cinco, multiplicado por três. [p=0.2] {c}Um cateto mede quinze. [p=0.2] {d}Doze e dezesseis: o mesmo terno vezes quatro. [p=0.2] {e}O outro cateto mede vinte."),
    dict(id="s22", block="resposta5", text="Conferindo com a outra relação: [p=0.2] a hipotenusa é {a}nove mais dezesseis, que dá vinte e cinco. [p=0.2] {b}Vinte e cinco vezes doze dá trezentos. [p=0.2] {c}Quinze vezes vinte também dá trezentos. [p=0.2] Bateu."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}ache o ângulo reto e a hipotenusa, [p=0.2] {b}teste os ternos antes da conta [p=0.2] e {c}confira se a hipotenusa ficou o maior lado."),
    dict(id="s24", block="fim", text="Com isso, você fecha {a}a trilha de ângulos e triângulos. [p=0.2] A próxima começa {b}os polígonos, pelos quadriláteros: [p=0.2] {c}paralelogramo, retângulo, losango e trapézio, [p=0.2] e o que vale para os lados, os ângulos e as diagonais de cada um. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
