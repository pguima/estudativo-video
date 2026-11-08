# Estudativo · MAT-RAZ-023 — Praticando: escalas (Matemática · Razão e Proporção · prática).
# Habilidade: calcular distâncias, áreas e volumes reais em plantas, mapas e maquetes.
# Pré-requisitos: MAT-RAZ-020, MAT-RAZ-021, MAT-RAZ-022. Próxima: MAT-POR-001 (fim da trilha Razão e Proporção; começa Porcentagem).
# Questões inéditas, criadas para esta aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Praticando: escalas"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações com mapas, plantas e maquetes, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] A conta de escala é fácil. [p=0.2] O que derruba é {c}a unidade e o quadrado."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}escala é desenho sobre real, na mesma unidade, [p=0.2] {b}do papel para o real multiplica, do real para o papel divide, [p=0.2] {c}escala gráfica se mede com a régua, [p=0.2] e {d}área vai ao quadrado, volume ao cubo. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: distância no mapa
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Num mapa de escala {b}um para quinhentos mil, [p=0.2] duas cidades estão a {c}seis centímetros. [p=0.3] {d}Qual é a distância real, em quilômetros?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Do papel para o real, multiplica: {a}seis vezes quinhentos mil dá três milhões de centímetros. [p=0.3] Ande com a vírgula cinco casas para a esquerda: {b}trinta quilômetros. [p=0.3] Pelo atalho: {c}um centímetro vale cinco quilômetros, [p=0.2] e {d}seis vezes cinco dá trinta."),
    # situação 2: do real para o papel
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] Um corredor tem {b}seis metros de comprimento. [p=0.2] Na planta de escala {c}um para cinquenta, [p=0.3] {d}quantos centímetros ele ocupa?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] Primeiro, a mesma unidade: {a}seis metros são seiscentos centímetros. [p=0.3] Do real para o papel, divide: {b}seiscentos dividido por cinquenta dá doze centímetros. [p=0.3] Confira: o desenho tem que ser {c}menor que o real, e é."),
    dict(id="s09", block="resposta2", text="O erro aqui é {a}dividir seis por cinquenta, sem converter. [p=0.2] Dá {b}zero vírgula doze, [p=0.2] e a pessoa marca doze centésimos de centímetro, um risquinho no papel. [p=0.3] {c}Converta antes de dividir."),
    # situação 3: escala gráfica
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] Num mapa de trilha, a escala gráfica mostra que o trecho de {b}zero a três quilômetros mede dois centímetros. [p=0.3] A trilha mede {c}oito centímetros no mapa. [p=0.3] {d}Qual é o comprimento real da trilha? [p=0.2] E {e}qual é a escala numérica?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] Oito centímetros são {a}quatro trechos de dois. [p=0.2] {b}Quatro vezes três dá doze quilômetros de trilha."),
    dict(id="s13", block="resposta3", text="Para a escala, passe para centímetro: {a}três quilômetros são trezentos mil centímetros. [p=0.2] Divida o real pelo desenho: {b}trezentos mil dividido por dois dá cento e cinquenta mil. [p=0.3] Escala: {c}um para cento e cinquenta mil. [p=0.3] Conferindo: {d}oito vezes cento e cinquenta mil dá um milhão e duzentos mil centímetros, [p=0.2] doze quilômetros. [p=0.2] Bateu."),
    # situação 4: área
    dict(id="s14", block="questao4", text="{a}Situação quatro. [p=0.2] Numa planta de escala {b}um para duzentos, um apartamento é um retângulo de {c}quatro centímetros por três. [p=0.3] {d}Qual é a área real, em metros quadrados?"),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="Vamos lá. [p=0.2] Use o atalho: {a}converta os lados, não a área. [p=0.3] Na escala um para duzentos, um centímetro vale {b}duzentos centímetros, que são dois metros. [p=0.2] {c}Quatro centímetros viram oito metros. [p=0.2] {d}Três centímetros viram seis metros. [p=0.3] {e}Oito vezes seis dá quarenta e oito metros quadrados."),
    dict(id="s17", block="resposta4", text="Pela escala ao quadrado dá o mesmo: [p=0.2] no papel, {a}doze centímetros quadrados. [p=0.2] Vezes duzentos ao quadrado, {b}quarenta mil: [p=0.2] {c}quatrocentos e oitenta mil centímetros quadrados, [p=0.2] que são {d}quarenta e oito metros quadrados. [p=0.3] Quem multiplica doze só por duzentos acha {e}zero vírgula vinte e quatro metro quadrado. [p=0.2] Um apartamento do tamanho de um tapetinho."),
    # situação 5: volume
    dict(id="s18", block="questao5", text="{a}Última situação. [p=0.2] Uma maquete de escala {b}um para vinte mostra um reservatório que, na maquete, guarda {c}dois litros. [p=0.3] {d}Quantos metros cúbicos guarda o reservatório real?"),
    dict(id="s19", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta5", text="Vamos lá. [p=0.2] Litro é medida de volume, e aqui não temos os lados. [p=0.2] Então, {a}escala ao cubo: [p=0.2] {b}vinte vezes vinte vezes vinte, oito mil. [p=0.3] {c}Dois litros vezes oito mil dá dezesseis mil litros."),
    dict(id="s21", block="resposta5", text="Um metro cúbico são mil litros. [p=0.2] {a}Dezesseis mil dividido por mil: dezesseis metros cúbicos. [p=0.3] Repare que a resposta não depende de converter litro para centímetro cúbico: [p=0.2] {b}o volume real é o volume da maquete vezes oito mil, em qualquer unidade."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}tudo na mesma unidade, [p=0.2] {b}comprimento direto, área ao quadrado, volume ao cubo, [p=0.2] e {c}confira se a resposta faz sentido no mundo real."),
    dict(id="s23", block="fim", text="Com esta aula, você fecha a trilha de razão e proporção. [p=0.2] A próxima começa uma trilha nova: {a}porcentagem. [p=0.2] Você vai ver que {b}vinte e cinco por cento é só vinte e cinco em cada cem, [p=0.2] e escrever uma porcentagem {c}como fração e como decimal. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
