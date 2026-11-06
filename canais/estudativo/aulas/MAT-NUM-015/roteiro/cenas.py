# Estudativo · MAT-NUM-015 — Números negativos e reta numérica (Matemática · Números e Contas).
# Habilidade: marcar −3, 0 e 4 numa reta, explicar por que −7 < −2 e calcular |−8| = 8 como distância até o zero.
# Pré-requisitos: MAT-NUM-002 (comparar com > e <), MAT-NUM-004 (subtrair). Próxima: MAT-NUM-016.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula.

TITULO = "Números negativos e reta numérica"

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
    dict(id="s01", block="gancho", text="{a}Menos sete é maior ou menor que menos dois? [p=0.3] Sete é maior que dois, então muita gente responde {b}maior. [p=0.3] {c}Errado. [p=0.2] Menos sete é {d}menor."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você marca negativos na reta, [p=0.2] entende o que é {b}módulo [p=0.2] e leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}duas coisas: [p=0.2] {b}subtrair [p=0.2] e {c}usar os sinais de maior e menor, [p=0.2] com a abertura virada para o número maior. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="termometro", text="O que existe abaixo do zero? [p=0.2] Um termômetro marca {a}zero grau. [p=0.2] Esfria {b}três graus. [p=0.2] Ele desce para {c}três abaixo de zero, [p=0.2] e isso se escreve {d}menos três. [p=0.3] No banco é igual: saldo de menos três é {e}dever três reais."),
    # reta
    dict(id="s05", block="reta", text="Deite o termômetro e você tem {a}a reta numérica. [p=0.3] {b}O zero fica no meio. [p=0.2] À direita, {c}os positivos. [p=0.2] À esquerda, {d}os negativos. [p=0.3] Todo passo tem o mesmo tamanho."),
    dict(id="s06", block="reta", text="Vamos marcar. [p=0.2] {a}O zero é o ponto de partida. [p=0.2] {b}Para marcar quatro, ande quatro passos para a direita. [p=0.2] {c}Para marcar menos três, ande três passos para a esquerda. [p=0.3] {d}O sinal diz o lado. [p=0.2] {e}O número diz quantos passos. [p=0.3] Sem sinal na frente, o número é positivo: quatro é o mesmo que mais quatro."),
    dict(id="s07", block="reta", text="Os positivos, os negativos e o zero, [p=0.2] sem nenhuma parte quebrada, [p=0.2] se chamam {a}números inteiros. [p=0.3] {b}Menos dois é inteiro. [p=0.2] Zero e sete também. [p=0.3] E o zero {c}não é positivo nem negativo: [p=0.2] ele separa os lados."),
    # comparar
    dict(id="s08", block="comparar", text="Comparar na reta é fácil: [p=0.2] {a}quem está mais à direita é maior. [p=0.3] Marque {b}menos sete {c}e menos dois. [p=0.3] Menos dois está mais à direita. [p=0.2] Logo, {d}menos sete é menor que menos dois."),
    dict(id="s09", block="comparar", text="Pense no dia a dia: [p=0.2] {a}sete abaixo de zero é mais frio que dois abaixo de zero. [p=0.2] E {b}dever sete reais é pior que dever dois reais."),
    dict(id="s10", block="comparar", text="A regra vale para qualquer comparação. [p=0.2] {a}Quatro é maior que menos três. [p=0.2] {b}Zero é maior que menos um. [p=0.3] Todo negativo fica à esquerda do zero, [p=0.2] então {c}todo negativo é menor que zero e menor que qualquer positivo."),
    # módulo
    dict(id="s11", block="modulo", text="Falta uma palavra: [p=0.2] {a}módulo é a distância de um número até o zero. [p=0.3] Na escrita, ele aparece entre {b}duas barrinhas em pé. [p=0.3] {c}Módulo de menos oito: [p=0.2] conte os passos do menos oito até o zero. [p=0.2] {d}São oito passos. [p=0.2] O módulo é {e}oito. [p=0.3] {f}Módulo de cinco dá cinco. [p=0.2] {g}Módulo de zero dá zero, porque ele já está lá."),
    dict(id="s12", block="modulo", text="Oito também está a oito passos do zero. [p=0.2] Só que do outro lado. [p=0.3] Números assim, com a mesma distância e lados contrários, [p=0.2] são {a}opostos. [p=0.2] {b}O oposto de oito é menos oito. [p=0.2] {c}O oposto de menos três é três."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com um erro comum: [p=0.2] achar que módulo {a}troca o sinal. [p=0.3] Aí, módulo de oito viraria {b}menos oito. [p=0.3] Só que módulo é distância, [p=0.2] e ninguém anda {c}menos oito passos. [p=0.3] Do oito até o zero são {d}oito passos. [p=0.2] Módulo {e}nunca dá negativo."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}entre negativos, a comparação vira ao contrário. [p=0.3] {b}Compare sem o sinal: [p=0.2] sete é maior que dois. [p=0.2] {c}Ponha o menos e inverta: [p=0.2] menos sete é menor que menos dois."),
    dict(id="s15", block="atalho", text="Funciona porque, do lado esquerdo, [p=0.2] {a}quanto mais longe do zero, mais à esquerda o número fica, [p=0.2] e mais à esquerda é menor. [p=0.3] {b}Só vale com dois negativos. [p=0.2] Negativo contra positivo nem precisa de atalho: [p=0.2] {c}o positivo sempre ganha."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] A primeira câmara fria marca {a}menos nove graus. [p=0.2] A segunda marca {b}dois graus. [p=0.2] A terceira marca {c}menos quatro graus. [p=0.3] {d}Ponha as câmaras em ordem, da mais fria para a mais quente. [p=0.2] E diga {e}qual delas está mais perto do zero."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá, na reta. [p=0.2] {a}Menos nove está mais à esquerda: [p=0.2] é a primeira câmara, a mais fria. [p=0.2] Depois vem {b}a terceira, com menos quatro. [p=0.2] Por último, {c}a segunda, com dois graus."),
    dict(id="s19", block="resposta", text="Para ver quem está mais perto, compare as distâncias. [p=0.2] {a}Módulo de menos nove dá nove. [p=0.2] {b}Módulo de menos quatro dá quatro. [p=0.2] {c}Módulo de dois dá dois. [p=0.3] A menor distância é da {d}segunda câmara, a de dois graus."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}o sinal diz o lado, [p=0.2] {b}na reta, mais à direita é maior [p=0.2] e {c}módulo é a distância até o zero."),
    dict(id="s21", block="fim", text="Na próxima aula, você {a}faz conta com esses números: [p=0.2] {b}somar e subtrair inteiros [p=0.2] pensando em {c}dívida e pagamento. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
