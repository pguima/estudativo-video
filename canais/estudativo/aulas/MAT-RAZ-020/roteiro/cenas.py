# Estudativo · MAT-RAZ-020 — O que é escala: medida real e do desenho (Matemática · Razão e Proporção).
# Habilidade: ler 1:100, descobrir quantos km valem 3 cm num mapa de 1:50.000 e quantos cm uma parede de 4 m ocupa numa planta de 1:50.
# Pré-requisitos: MAT-RAZ-002 (proporção e produto cruzado). Usa também MAT-RAZ-001 e MAT-MED-001 (escada do metro). Próxima: MAT-RAZ-021.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "O que é escala: medida real e do desenho"

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
    dict(id="s01", block="gancho", text="Num mapa, duas cidades estão a {a}três centímetros uma da outra. [p=0.3] No mundo real, são {b}quilômetros. [p=0.3] O que liga o papel ao mundo de verdade é {c}um número pequeno, escrito no canto do mapa."),
    dict(id="s02", block="gancho", text="Esse número é a {a}escala. [p=0.2] {b}Até o fim desta aula, você vai ler qualquer escala e ir do papel para o real e do real para o papel, [p=0.2] com um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}razão, que compara duas medidas na mesma unidade, [p=0.2] {c}proporção, com o produto cruzado, [p=0.2] e {d}a escada do metro. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é escala
    dict(id="s04", block="escala", text="{a}Escala é a razão entre a medida no desenho e a medida real, [p=0.2] {b}as duas na mesma unidade. [p=0.3] Desenho em cima, real embaixo."),
    dict(id="s05", block="escala", text="Numa planta de casa você encontra {a}um, dois pontos, cem. [p=0.2] Lê-se {b}um para cem. [p=0.3] Cada {c}um centímetro no papel vale {d}cem centímetros na casa de verdade. [p=0.2] E cem centímetros é {e}um metro. [p=0.3] Por isso essa escala é a preferida das plantas: [p=0.2] {f}um centímetro no papel, um metro na casa, de cabeça."),
    dict(id="s06", block="escala", text="Repare: a escala não tem unidade. [p=0.2] Um para cem vale para {a}qualquer unidade, desde que seja a mesma em cima e embaixo: [p=0.2] um metro no papel valeria cem metros de verdade. [p=0.3] Na prova, quase sempre é {b}centímetro, a unidade da régua."),
    # do papel para o real
    dict(id="s07", block="real", text="Agora o mapa do começo. [p=0.2] A escala é {a}um para cinquenta mil, [p=0.2] e as cidades estão a {b}três centímetros. [p=0.3] Monte a proporção: {c}um sobre cinquenta mil igual a três sobre xis."),
    dict(id="s08", block="real", text="Produto cruzado: {a}xis é três vezes cinquenta mil dá [p=0.2] {b}cento e cinquenta mil centímetros. [p=0.3] Na prática, do papel para o real, {c}multiplique pelo número de baixo da escala."),
    dict(id="s09", block="real", text="Mas centímetro não é a resposta. [p=0.2] Suba a escada: {a}dividido por cem dá mil e quinhentos metros. [p=0.2] {b}Dividido por mil dá um vírgula cinco quilômetro. [p=0.3] Três centímetros no mapa, {c}um quilômetro e meio em linha reta."),
    # do real para o papel
    dict(id="s10", block="papel", text="E o caminho contrário? [p=0.2] Uma parede de {a}quatro metros, numa planta de {b}um para cinquenta. [p=0.3] Quantos centímetros ela ocupa no papel?"),
    dict(id="s11", block="papel", text="Primeiro, a mesma unidade: {a}quatro metros são quatrocentos centímetros. [p=0.3] Do real para o papel, a medida encolhe: {b}divida pelo número de baixo. [p=0.2] {c}Quatrocentos dividido por cinquenta dá oito centímetros. [p=0.3] Confira: {d}oito vezes cinquenta dá quatrocentos. [p=0.2] Bateu."),
    dict(id="s12", block="papel", text="Pela proporção dá o mesmo: [p=0.2] {a}um sobre cinquenta igual a xis sobre quatrocentos. [p=0.2] {b}Cinquenta vezes xis é quatrocentos, e xis é oito."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: {a}esquecer a escada. [p=0.2] A pessoa faz três vezes cinquenta mil, acha cento e cinquenta mil, [p=0.2] e responde {b}cento e cinquenta mil quilômetros."),
    dict(id="s14", block="erro", text="Isso é {a}mais que três voltas ao redor da Terra! [p=0.3] A conta da escala {b}sempre sai na unidade do desenho, aqui, centímetro. [p=0.2] Só depois você {c}converte."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}quanto vale um centímetro. [p=0.3] Na escala um para ene, um centímetro vale ene centímetros. [p=0.2] Para ler em metros, {b}ande com a vírgula duas casas para a esquerda. [p=0.2] Para ler em quilômetros, {c}cinco casas."),
    dict(id="s16", block="atalho", text="Um para cinquenta mil: duas casas, e {a}um centímetro vale quinhentos metros. [p=0.3] Cinco casas, e vale {b}zero vírgula cinco quilômetro. [p=0.2] Então três centímetros valem {c}um vírgula cinco quilômetro, de cabeça."),
    dict(id="s17", block="atalho", text="Funciona porque {a}um metro tem cem centímetros, [p=0.2] e {b}um quilômetro tem cem mil centímetros. [p=0.3] Não compensa no caminho contrário, do real para o papel: [p=0.2] aí, {c}passe a medida real para centímetro e divida."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Num mapa de escala {a}um para duzentos mil, [p=0.2] duas cidades estão a {b}sete centímetros. [p=0.3] {c}Qual é a distância real, em quilômetros?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] Do papel para o real, multiplica: {a}sete vezes duzentos mil dá um milhão e quatrocentos mil centímetros. [p=0.3] Vírgula cinco casas para a esquerda: {b}catorze quilômetros. [p=0.3] Pelo atalho: {c}um centímetro vale dois quilômetros, [p=0.2] e {d}sete vezes dois dá catorze."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}desenho sobre real, na mesma unidade. [p=0.2] {b}Do papel para o real, multiplica. [p=0.2] {c}Do real para o papel, divide. [p=0.2] E {d}converta no fim."),
    dict(id="s22", block="fim", text="Na próxima aula, o contrário: {a}quatro centímetros representam dez quilômetros, e você descobre a escala. [p=0.2] E ainda aprende a {b}medir com a régua na escala gráfica. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
