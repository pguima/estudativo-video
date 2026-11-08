# Estudativo · MAT-ANG-001 — Ângulos: medir em graus e classificar (Matemática · Geometria Plana: Ângulos e Triângulos).
# Habilidade: dizer que o ponteiro às 3 horas forma 1/4 de volta, ou 90°, e classificar um ângulo em agudo, reto, obtuso ou raso.
# Pré-requisitos: MAT-FRA-002 (fração de uma quantidade). Próxima: MAT-ANG-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Visual: relógio desenhado (mostrador com 12, 3, 6 e 9 marcando quatro partes) e E.angulo para cada tipo.
# Divisão por 12 e simplificação ainda não foram ensinadas: o 90° sai de 1/4 de 360 e os 30° por hora saem de 90 ÷ 3.

TITULO = "Ângulos: medir em graus e classificar"

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
    dict(id="s01", block="gancho", text="{a}Três horas em ponto. [p=0.3] {b}Os ponteiros do relógio formam um canto perfeito, [p=0.2] igual ao {c}canto de uma folha de papel. [p=0.3] Quanto mede essa abertura? [p=0.3] E será que, num {d}relógio de parede, ela é maior que num relógio de pulso?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai medir ângulos em graus, [p=0.2] {b}dar nome a cada tipo de ângulo [p=0.2] e ainda leva um {c}atalho de prova para relógios."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}uma coisa: [p=0.2] {b}calcular a fração de uma quantidade. [p=0.2] Divide pelo de baixo, multiplica pelo de cima. [p=0.3] Se faltar, procure a aula no canal."),
    # o que é ângulo
    dict(id="s04", block="ideia", text="Primeiro, o que é um ângulo? [p=0.2] Pegue {a}duas linhas que saem do mesmo ponto, [p=0.2] como os ponteiros, presos no centro do relógio."),
    dict(id="s05", block="ideia", text="{a}O ponto de onde elas saem é o vértice. [p=0.2] {b}As linhas são os lados. [p=0.3] E {c}o ângulo é a abertura entre os lados: [p=0.2] o quanto um lado girou em relação ao outro."),
    # graus
    dict(id="s06", block="graus", text="Para medir essa abertura, usamos {a}o grau. [p=0.2] Por uma combinação muito antiga, {b}uma volta inteira vale trezentos e sessenta graus. [p=0.3] Na tela, o grau é {c}essa bolinha pequena no alto do número."),
    dict(id="s07", block="graus", text="Então, para medir um pedaço de volta, {a}calcule a fração de trezentos e sessenta. [p=0.3] {b}Meia volta: [p=0.2] trezentos e sessenta dividido por dois dá {c}cento e oitenta graus."),
    dict(id="s08", block="graus", text="{a}Um quarto de volta: [p=0.2] trezentos e sessenta dividido por quatro dá noventa. [p=0.2] Vezes um, dá {b}noventa graus. [p=0.3] É {c}o canto da folha de papel."),
    # relógio
    dict(id="s09", block="relogio", text="Volte ao relógio. [p=0.2] O doze, o três, o seis e o nove {a}cortam o mostrador em quatro partes iguais."),
    dict(id="s10", block="relogio", text="Às três horas, {a}o ponteiro grande está no doze, [p=0.2] e {b}o pequeno está no três. [p=0.3] Entre eles fica {c}uma dessas quatro partes: [p=0.2] um quarto de volta. [p=0.2] {d}Noventa graus."),
    dict(id="s11", block="relogio", text="Um detalhe: os ponteiros também separam {a}o outro lado do relógio, a parte maior. [p=0.3] Quando a pergunta fala do ângulo entre os ponteiros, {b}vale o menor."),
    # classificar
    dict(id="s12", block="tipos", text="Com o noventa como régua, todo ângulo ganha um nome. [p=0.2] {a}Exatamente noventa graus: ângulo reto. [p=0.2] Na figura, ele ganha {b}um quadradinho no canto, no lugar do arco."),
    dict(id="s13", block="tipos", text="{a}Menor que noventa: ângulo agudo, [p=0.2] mais fechado que o canto da folha. [p=0.2] Como os ponteiros {b}à uma hora."),
    dict(id="s14", block="tipos", text="{a}Maior que noventa e menor que cento e oitenta: ângulo obtuso, [p=0.2] mais aberto que o canto da folha. [p=0.2] Como os ponteiros {b}às quatro horas."),
    dict(id="s15", block="tipos", text="{a}Exatamente cento e oitenta graus: ângulo raso. [p=0.2] É meia volta. [p=0.2] Os lados formam {b}uma linha reta, como os ponteiros {c}às seis horas."),
    # erro
    dict(id="s16", block="erro", text="Agora, cuidado com um erro muito comum: {a}achar que lados maiores fazem um ângulo maior. [p=0.3] O relógio de parede tem {b}ponteiros enormes. [p=0.2] O de pulso, {c}ponteiros pequenininhos."),
    dict(id="s17", block="erro", text="Às três horas, {a}cada um deles marca o mesmo canto: noventa graus. [p=0.3] {b}O ângulo mede a abertura, não o comprimento dos lados. [p=0.2] Esticar os lados {c}não muda nada."),
    # atalho
    dict(id="s18", block="atalho", text="E o atalho prometido: [p=0.2] {a}cada hora do relógio vale trinta graus. [p=0.3] Um quarto de volta tem três horas, [p=0.2] e {b}noventa dividido por três dá trinta."),
    dict(id="s19", block="atalho", text="Então {a}conte as horas entre os ponteiros, pelo lado mais curto, e multiplique por trinta. [p=0.2] Às duas horas, {b}duas vezes trinta dá sessenta graus. [p=0.2] Às quatro, {c}quatro vezes trinta dá cento e vinte. [p=0.2] Às dez, do dez até o doze são só duas horas: {d}sessenta graus de novo."),
    dict(id="s20", block="atalho", text="Funciona porque {a}o mostrador está cortado em doze partes iguais, uma para cada hora. [p=0.3] {b}Só vale em hora cheia. [p=0.2] Às três e meia, o ponteiro pequeno já saiu do três, [p=0.2] e {c}a conta muda."),
    # questão
    dict(id="s21", block="questao", text="Hora de testar. [p=0.2] {a}Às cinco horas em ponto, [p=0.2] quanto mede o menor ângulo entre os ponteiros? [p=0.3] {b}E qual é o nome desse ângulo?"),
    dict(id="s22", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s23", block="resposta", text="Vamos lá. [p=0.2] Do doze até o cinco, são {a}cinco horas. [p=0.2] {b}Cinco vezes trinta dá cento e cinquenta graus. [p=0.3] É maior que noventa e menor que cento e oitenta: [p=0.2] {c}ângulo obtuso."),
    dict(id="s24", block="resposta", text="Conferindo por outro caminho: [p=0.2] {a}às seis horas, seria meia volta, cento e oitenta graus. [p=0.2] Às cinco, {b}falta uma hora, ou seja, trinta graus. [p=0.2] Cento e oitenta menos trinta dá {c}cento e cinquenta. [p=0.2] Bateu."),
    # fechamento
    dict(id="s25", block="fim", text="Resumindo: {a}uma volta tem trezentos e sessenta graus, [p=0.2] {b}o canto da folha tem noventa, [p=0.2] e {c}o noventa separa o agudo do obtuso."),
    dict(id="s26", block="fim", text="Na próxima aula, você vê {a}pares de ângulos que completam um canto reto ou uma linha reta, [p=0.2] e o que acontece {b}quando duas retas se cruzam. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
