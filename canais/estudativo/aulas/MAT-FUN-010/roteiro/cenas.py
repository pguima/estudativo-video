# Estudativo · MAT-FUN-010 — Coeficientes: taxa de variação e valor inicial (Matemática · Funções · Função afim).
# Habilidade: ler em f(x) = 40 + 0,5x o valor inicial e quanto sobe por unidade, calcular a = Δy/Δx e dizer se a reta sobe, desce ou é constante.
# Pré-requisitos: MAT-FUN-009 (lei e gráfico da função afim), MAT-RAZ-015 (taxas). Próxima: MAT-FUN-011.
# Questão inédita, criada para esta aula. Letras narradas: "á", "bê", "xis", "ípsilon"; Δ = "delta". Termos como na MAT-FUN-009:
#   "á é o número que multiplica o xis", "bê é o número sozinho". Taxa = razão de tipos diferentes, "por" = dividido (MAT-RAZ-015).
# Locadora: f(x) = 40 + 0,5x (x em km, f em reais) · f(0) = 40 · pontos (10, 45) e (30, 55): Δy = 10, Δx = 20, a = 0,5.
# Desce: bateria f(x) = 100 − 5x (por cento, x em horas), a = −5 · constante: f(x) = 30, a = 0.
# Erro: tomar a = 40 por ser o primeiro número (40x + 0,5) → 10 km daria 400,50 em vez de 45.
# Questão: vela f(x) = 20 − 2x (cm, x em horas) · inicial 20 · a = −2, desce · conferência (1, 18) e (4, 12): Δy = −6, Δx = 3, a = −2.
# Visual: fórmula com "valor inicial" e "taxa de variação" apontando para 40 e 0,5; plano (E.plano) com a reta da locadora cruzando
#   o eixo y em 40 (E.reta_pontos); degrau Δx (deitado) e Δy (em pé) entre (10, 45) e (30, 55); três mini-gráficos: sobe, desce, horizontal.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Coeficientes: taxa de variação e valor inicial"

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
    dict(id="s01", block="gancho", text="Uma locadora cobra o aluguel de um carro pela fórmula {a}efe de xis igual a quarenta mais zero vírgula cinco xis. [p=0.3] Sem fazer conta nenhuma, dá para responder {b}quanto você paga antes de rodar [p=0.2] e {c}quanto cada quilômetro acrescenta. [p=0.3] Esses números da fórmula {d}contam a história inteira."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você lê esses dois números em qualquer função afim, [p=0.2] {b}calcula quanto a reta sobe a cada passo [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a função afim, efe de xis igual a á xis mais bê, [p=0.2] em que o á multiplica o xis e o bê fica sozinho, [p=0.2] e {c}taxa, em que a palavra por quer dizer dividido. [p=0.3] Se faltar alguma, procure no canal."),
    # valor inicial
    dict(id="s04", block="inicial", text="Na locadora, xis é a distância rodada, em quilômetros, [p=0.2] e efe de xis é o preço, em reais. [p=0.3] Quanto custa {a}sem rodar nada? [p=0.2] Quando o xis vale zero, [p=0.2] a conta {b}zero vírgula cinco vezes zero dá zero. [p=0.2] Sobram {c}quarenta reais."),
    dict(id="s05", block="inicial", text="Esse é o {a}valor inicial: o ípsilon quando o xis é zero. [p=0.2] Na fórmula, é {b}o bê, o número sozinho. [p=0.2] No gráfico, é {c}onde a reta corta o eixo ípsilon. [p=0.3] Nos livros, o bê também se chama {d}coeficiente linear."),
    # taxa de variação
    dict(id="s06", block="taxa", text="E o zero vírgula cinco? [p=0.2] {a}Um quilômetro: quarenta reais e cinquenta centavos. [p=0.2] {b}Dois quilômetros: quarenta e um reais. [p=0.2] {c}Três quilômetros: quarenta e um reais e cinquenta centavos. [p=0.3] A cada quilômetro a mais, o preço {d}sobe cinquenta centavos. [p=0.2] É o á, o número que multiplica o xis."),
    dict(id="s07", block="taxa", text="O á é uma {a}taxa: zero vírgula cinco real por quilômetro. [p=0.2] Ele diz {b}quanto o ípsilon muda quando o xis anda um. [p=0.3] Por isso se chama {c}taxa de variação. [p=0.2] Nos livros, também aparece como {d}coeficiente angular."),
    # delta
    dict(id="s08", block="delta", text="E se você só tiver {a}dois pontos da reta, sem a fórmula? [p=0.3] Com dez quilômetros, o preço foi {b}quarenta e cinco reais. [p=0.2] Com trinta quilômetros, {c}cinquenta e cinco."),
    dict(id="s09", block="delta", text="Entra um símbolo novo: {a}o triângulo delta. [p=0.2] Ele quer dizer {b}variação: quanto mudou, o final menos o inicial. [p=0.3] {c}Delta ípsilon: cinquenta e cinco menos quarenta e cinco dá dez reais. [p=0.2] {d}Delta xis: trinta menos dez dá vinte quilômetros."),
    dict(id="s10", block="delta", text="A taxa é {a}reais por quilômetro, [p=0.2] e por quer dizer dividido: [p=0.2] {b}á igual a delta ípsilon dividido por delta xis. [p=0.3] {c}Dez dividido por vinte dá zero vírgula cinco. [p=0.2] {d}O mesmo número da fórmula."),
    # sobe, desce, constante
    dict(id="s11", block="sinal", text="O sinal do á diz {a}para onde a reta vai. [p=0.3] {b}Á positivo, a reta sobe: [p=0.2] é a locadora, que cobra mais a cada quilômetro. [p=0.3] {c}Á negativo, a reta desce. [p=0.2] A bateria de um celular, em por cento, {d}é cem menos cinco xis, [p=0.2] com xis em horas. [p=0.2] O á é {e}menos cinco: [p=0.2] a carga perde cinco a cada hora."),
    dict(id="s12", block="sinal", text="E {a}á igual a zero? [p=0.2] Então o xis some da fórmula. [p=0.2] Uma {b}assinatura de trinta reais, não importa quanto você use: [p=0.2] {c}efe de xis igual a trinta. [p=0.3] A reta fica {d}na horizontal: [p=0.2] a função é constante."),
    # erro
    dict(id="s13", block="erro", text="Agora, cuidado com o erro mais comum: [p=0.2] {a}achar que o á é o primeiro número da fórmula. [p=0.3] Em quarenta mais zero vírgula cinco xis, {b}o á não é quarenta. [p=0.2] Quem usa quarenta como taxa [p=0.2] calcula {c}dez quilômetros por quatrocentos reais e cinquenta centavos, [p=0.2] e não por quarenta e cinco reais. [p=0.3] {d}O á é sempre quem está colado no xis, [p=0.2] em qualquer posição."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho para achar o á no gráfico: [p=0.2] {a}quanto sobe, dividido por quanto anda. [p=0.3] Saia do ponto da esquerda, {b}ande para a direita até chegar no xis do outro ponto [p=0.2] e {c}suba até ele. [p=0.2] A subida dividida pela andada é o á. [p=0.3] Se o outro ponto estiver mais baixo, {d}você desce, e a subida conta como negativa."),
    dict(id="s15", block="atalho", text="Funciona porque {a}a subida é o delta ípsilon e a andada é o delta xis. [p=0.3] {b}Não compensa contar quadradinhos quando os eixos têm escalas diferentes, [p=0.2] como {c}um quadradinho valendo dez no xis e um no ípsilon. [p=0.2] Aí, {d}leia os valores nos eixos e faça a conta."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] A altura de uma vela acesa, em centímetros, [p=0.2] é {a}efe de xis igual a vinte menos dois xis, [p=0.2] com xis em horas. [p=0.3] {b}Qual era a altura antes de acender? [p=0.2] {c}Quanto ela muda por hora? [p=0.2] {d}A reta sobe ou desce? [p=0.3] E {e}confira o á com os pontos de uma hora e de quatro horas."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] O valor inicial é {a}o bê: vinte centímetros. [p=0.2] O á é {b}menos dois, colado no xis. [p=0.2] A vela {c}perde dois centímetros por hora. [p=0.2] Á negativo: {d}a reta desce."),
    dict(id="s19", block="resposta", text="Para conferir: {a}com uma hora, vinte menos dois dá dezoito. [p=0.2] {b}Com quatro horas, vinte menos oito dá doze. [p=0.3] {c}Delta ípsilon: doze menos dezoito dá menos seis. [p=0.2] {d}Delta xis: quatro menos um dá três. [p=0.2] {e}Menos seis dividido por três: menos dois. [p=0.2] Bateu."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}o bê é de onde a reta parte, [p=0.2] {b}o á é quanto ela sobe a cada passo, [p=0.2] e {c}o sinal do á diz se ela sobe, desce ou fica parada."),
    dict(id="s21", block="fim", text="Na próxima aula, você descobre {a}onde a reta corta o eixo xis [p=0.2] e {b}para quais xis a função fica positiva ou negativa. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
