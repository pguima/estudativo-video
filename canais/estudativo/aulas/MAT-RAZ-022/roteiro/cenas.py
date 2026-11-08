# Estudativo · MAT-RAZ-022 — Escala ao quadrado, escala ao cubo (Matemática · Razão e Proporção).
# Habilidade: calcular a área real numa planta de 1:100 e o volume real numa maquete de 1:50, sem aplicar a escala direto.
# Pré-requisitos: MAT-MED-004 (área), MAT-MED-005 (volume e litros), MAT-RAZ-010 (proporcional ao quadrado), MAT-RAZ-020 (escala). Próxima: MAT-RAZ-023.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Escala ao quadrado, escala ao cubo"

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
    dict(id="s01", block="gancho", text="Numa planta de escala {a}um para cem, uma sala ocupa {b}vinte centímetros quadrados. [p=0.3] Quem multiplica por cem acha {c}dois mil centímetros quadrados. [p=0.2] Isso é {d}zero vírgula dois metro quadrado: [p=0.2] uma sala menor que o tampo de uma mesa."),
    dict(id="s02", block="gancho", text="A sala de verdade tem {a}vinte metros quadrados. [p=0.3] {b}Até o fim desta aula, você vai calcular área e volume reais sem cair nessa, [p=0.2] e ainda leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}ler uma escala, [p=0.2] {c}saber que dobrar o lado de um quadrado quadruplica a área, [p=0.2] e {d}converter metro quadrado e metro cúbico. [p=0.3] Se faltar alguma, procure no canal."),
    # área
    dict(id="s04", block="area", text="Na planta, a sala é um retângulo de {a}cinco centímetros por quatro. [p=0.2] Área de retângulo é {b}um lado vezes o outro: [p=0.2] {c}vinte centímetros quadrados no papel."),
    dict(id="s05", block="area", text="Agora, o caminho seguro: {a}passe os lados para o real primeiro. [p=0.3] Na escala um para cem, um centímetro vale um metro. [p=0.2] {b}Cinco centímetros viram cinco metros. [p=0.2] {c}Quatro centímetros viram quatro metros. [p=0.3] {d}Cinco vezes quatro dá vinte metros quadrados."),
    dict(id="s06", block="area", text="Por que multiplicar a área por cem deu errado? [p=0.2] Cada lado ficou {a}cem vezes maior. [p=0.2] A área usa dois lados, então cresce {b}cem vezes cem: [p=0.2] {c}dez mil vezes. [p=0.3] É a mesma ideia do quadrado: dobrar o lado quadruplica a área."),
    dict(id="s07", block="area", text="Confira: {a}vinte vezes dez mil dá duzentos mil centímetros quadrados. [p=0.2] Um metro quadrado tem dez mil centímetros quadrados, [p=0.2] então são {b}vinte metros quadrados. [p=0.3] {c}Para área, use a escala ao quadrado."),
    dict(id="s08", block="area", text="Na escala um para cem, isso fica bonito: [p=0.2] {a}um centímetro quadrado no papel vale um metro quadrado. [p=0.3] Por isso {b}vinte centímetros quadrados viraram vinte metros quadrados."),
    # volume
    dict(id="s09", block="volume", text="E o volume? [p=0.2] Numa maquete de escala {a}um para cinquenta, uma caixa-d'água é um cubinho de {b}dois centímetros de cada lado. [p=0.3] Volume de bloco é {c}comprimento vezes largura vezes altura: [p=0.2] {d}oito centímetros cúbicos."),
    dict(id="s10", block="volume", text="Caminho seguro de novo: {a}os lados primeiro. [p=0.2] Dois centímetros vezes cinquenta dá {b}cem centímetros, que é um metro. [p=0.3] A caixa real é um cubo de um metro de lado: {c}um metro cúbico, [p=0.2] ou {d}mil litros."),
    dict(id="s11", block="volume", text="O volume usa três medidas, então cresce {a}cinquenta vezes cinquenta vezes cinquenta: [p=0.2] {b}cinquenta ao cubo, cento e vinte e cinco mil. [p=0.3] {c}Oito vezes cento e vinte e cinco mil dá um milhão de centímetros cúbicos. [p=0.2] De novo, {d}um metro cúbico. [p=0.3] {e}Para volume, use a escala ao cubo."),
    dict(id="s12", block="volume", text="Na mesma maquete, então, {a}a altura de uma parede fica cinquenta vezes menor, [p=0.2] {b}a área de uma parede, dois mil e quinhentos vezes menor, [p=0.2] e {c}o volume, cento e vinte e cinco mil vezes menor."),
    # erro
    dict(id="s13", block="erro", text="Cuidado: o mesmo erro aparece no volume. [p=0.2] Quem faz {a}oito vezes cinquenta acha {b}quatrocentos centímetros cúbicos. [p=0.2] Isso é {c}zero vírgula quatro litro: uma caixa-d'água que cabe num copo grande."),
    dict(id="s14", block="erro", text="A escala direta só vale para {a}comprimento: lado, altura, distância. [p=0.2] Para área, {b}ao quadrado. [p=0.2] Para volume, {c}ao cubo."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}converta os lados, não a área. [p=0.3] Se a prova dá as medidas do desenho, passe cada uma para o real e só depois multiplique. [p=0.2] {b}Não tem quadrado nem cubo para esquecer."),
    dict(id="s16", block="atalho", text="Funciona porque lado é comprimento, e {a}para comprimento a escala vale direto. [p=0.3] Não compensa quando a prova dá {b}só a área do desenho, como a de um lago de forma torta. [p=0.2] Aí, {c}multiplique pela escala ao quadrado."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Numa planta de escala {a}um para mil, um terreno de forma irregular ocupa {b}seis centímetros quadrados. [p=0.3] {c}Qual é a área real do terreno, em metros quadrados?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Só temos a área, então {a}escala ao quadrado: mil vezes mil dá um milhão. [p=0.2] {b}Seis vezes um milhão dá seis milhões de centímetros quadrados. [p=0.3] Dividindo por dez mil: {c}seiscentos metros quadrados."),
    dict(id="s20", block="resposta", text="Outro caminho: um centímetro vale {a}dez metros. [p=0.2] Então um centímetro quadrado vale {b}dez vezes dez dá cem metros quadrados. [p=0.2] {c}Seis vezes cem dá seiscentos. [p=0.2] Bateu."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}comprimento, escala direta. [p=0.2] {b}Área, escala ao quadrado. [p=0.2] {c}Volume, escala ao cubo. [p=0.2] E, se der, {d}converta os lados primeiro."),
    dict(id="s22", block="fim", text="Na próxima aula, você {a}pratica tudo de escala: [p=0.2] {b}distâncias, áreas e volumes em plantas, mapas e maquetes. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
