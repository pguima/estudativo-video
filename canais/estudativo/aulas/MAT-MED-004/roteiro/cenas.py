# Estudativo · MAT-MED-004 — Converter área (Matemática · Medidas e Unidades).
# Habilidade: explicar o que é 1 m², ver que um retângulo de 3 m por 2 m cabe em 6 quadradinhos de 1 m², transformar 3 m² em cm² e 2,5 ha em m².
# Pré-requisitos: MAT-MED-001 (escada do metro), MAT-POT-001 (ao quadrado). Próxima: MAT-MED-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Fórmula de área (base vezes altura) é de MAT-ARE-002: aqui só se contam quadradinhos.

TITULO = "Converter área"

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
    dict(id="s01", block="gancho", text="{a}Um metro quadrado tem quantos centímetros quadrados? [p=0.3] Se você respondeu {b}cem, [p=0.2] errou feio. [p=0.3] São {c}dez mil."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai entender o que é área, [p=0.2] converter metros quadrados e hectares [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a escada do metro, em que cada degrau é uma casa da vírgula, [p=0.2] e {c}o quadrado de um número, como dez ao quadrado: dez vezes dez dá cem. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é área
    dict(id="s04", block="area", text="Comprimento mede {a}uma linha. [p=0.2] {b}Área mede uma superfície: [p=0.2] um piso, uma parede, um terreno. [p=0.3] Medir área é contar {c}quantos quadradinhos iguais cobrem essa superfície."),
    dict(id="s05", block="area", text="O quadradinho padrão é o {a}metro quadrado: [p=0.2] {b}um quadrado com um metro de cada lado. [p=0.3] Ele se escreve com {c}um dois pequeno no alto do eme, [p=0.2] o mesmo do ao quadrado. [p=0.3] Para coisas pequenas, existe o {d}centímetro quadrado: [p=0.2] um quadradinho de um centímetro de lado, do tamanho de uma unha."),
    dict(id="s06", block="area", text="Um quarto mede {a}três metros por dois metros. [p=0.2] Cubra o chão com quadradinhos de um metro: [p=0.2] {b}três em cada fileira, [p=0.2] {c}duas fileiras. [p=0.3] {d}Três vezes dois dá seis quadradinhos. [p=0.2] A área é {e}seis metros quadrados."),
    # metro quadrado em centímetro quadrado
    dict(id="s07", block="cm2", text="E em centímetros quadrados? [p=0.2] Olhe para {a}um só metro quadrado. [p=0.2] O lado tem um metro, que são {b}cem centímetros. [p=0.3] Cabem {c}cem quadradinhos de um centímetro em cada fileira, [p=0.2] e são {d}cem fileiras."),
    dict(id="s08", block="cm2", text="{a}Cem vezes cem: dez mil. [p=0.2] {b}Um metro quadrado tem dez mil centímetros quadrados. [p=0.3] No comprimento, do metro ao centímetro é vezes cem. [p=0.2] Na área, {c}é vezes cem ao quadrado."),
    dict(id="s09", block="cm2", text="Por isso, na escada da área, {a}cada degrau vale cem: duas casas da vírgula. [p=0.3] Do metro quadrado ao centímetro quadrado, {b}dois degraus, quatro casas."),
    dict(id="s10", block="cm2", text="{a}Três metros quadrados em centímetros quadrados. [p=0.2] Quatro casas para a direita: [p=0.2] {b}trinta mil centímetros quadrados. [p=0.3] E o contrário: {c}cinquenta mil centímetros quadrados. [p=0.2] Quatro casas para a esquerda: {d}cinco metros quadrados."),
    # hectare
    dict(id="s11", block="hectare", text="No campo, a unidade é o {a}hectare: [p=0.2] {b}um quadrado de cem metros de lado. [p=0.2] É {c}um pouco maior que um campo de futebol."),
    dict(id="s12", block="hectare", text="São cem fileiras de cem quadradinhos de um metro: {a}dez mil metros quadrados. [p=0.3] Então {b}dois vírgula cinco hectares são dois vírgula cinco vezes dez mil. [p=0.2] Quatro casas para a direita: {c}vinte e cinco mil metros quadrados."),
    dict(id="s13", block="hectare", text="E o quilômetro quadrado? [p=0.2] É um quadrado de mil metros de lado: [p=0.2] {a}mil vezes mil dá um milhão de metros quadrados. [p=0.3] Em hectares de dez mil, são {b}cem hectares."),
    # erro
    dict(id="s14", block="erro", text="O erro comum é o do começo: {a}usar a escada do comprimento na área. [p=0.2] A pessoa anda duas casas e escreve {b}três metros quadrados igual a trezentos centímetros quadrados. [p=0.3] Mas um só metro quadrado já tem {c}dez mil. [p=0.2] O resultado ficou {d}cem vezes menor. [p=0.3] Lembre do desenho: [p=0.2] são {e}cem fileiras de cem, e não uma fileira só."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}eleve o fator ao quadrado. [p=0.3] Do metro ao centímetro, o comprimento é {b}vezes cem. [p=0.2] Na área, {c}cem ao quadrado: dez mil. [p=0.3] Do quilômetro ao metro, o comprimento é vezes mil. [p=0.2] Na área, {d}mil ao quadrado: um milhão."),
    dict(id="s16", block="atalho", text="Funciona porque a área tem {a}duas direções, comprimento e largura, [p=0.2] e cada uma ganha o fator. [p=0.3] {b}Não compensa quando o enunciado dá os lados: [p=0.2] aí, {c}converta os lados primeiro e conte os quadradinhos."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Um sítio tem {a}três vírgula dois hectares. [p=0.2] {b}Quantos metros quadrados são? [p=0.3] E uma lajota tem {c}dois mil e quinhentos centímetros quadrados. [p=0.2] {d}Quantos metros quadrados ela tem?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Um hectare são dez mil metros quadrados: {a}quatro casas para a direita. [p=0.2] {b}Trinta e dois mil metros quadrados."),
    dict(id="s20", block="resposta", text="Na lajota, a unidade fica maior, então o número diminui: [p=0.2] {a}quatro casas para a esquerda. [p=0.2] {b}Zero vírgula vinte e cinco metro quadrado. [p=0.3] Menos de um metro quadrado, {c}como uma lajota tem que ser."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}área conta quadradinhos, [p=0.2] e {b}na escada da área, cada degrau vale duas casas."),
    dict(id="s22", block="fim", text="Na próxima aula, você vai encher uma caixa de {a}cubinhos [p=0.2] e descobrir quantos {b}litros cabem em um metro cúbico. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
