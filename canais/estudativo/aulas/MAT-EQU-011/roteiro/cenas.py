# Estudativo · MAT-EQU-011 — Isolar uma letra numa fórmula (Matemática · Equações do 1º Grau).
# Habilidade: passar v = d/t para d = v · t.
# Pré-requisitos: MAT-EQU-008 (letra dos dois lados). Próxima: MAT-EQU-012.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Letras apresentadas uma vez (vê de velocidade, dê de distância, tê de tempo) e depois chamadas pelo nome.

TITULO = "Isolar uma letra numa fórmula"

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
    dict(id="s01", block="gancho", text="Uma fórmula que aparece muito em prova: {a}velocidade igual a distância dividida pelo tempo. [p=0.3] Mas a pergunta quer {b}a distância, e não a velocidade. [p=0.3] Precisa decorar outra fórmula? [p=0.2] {c}Não. [p=0.2] A balança vira a fórmula para você."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você deixa qualquer letra sozinha numa fórmula simples, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}uma coisa só: [p=0.2] {b}resolver equação fazendo o mesmo nos dois lados. [p=0.2] Não precisa saber nada de física. [p=0.3] Se faltar, procure no canal."),
    # o que cada letra é
    dict(id="s04", block="letras", text="Primeiro, o que cada letra é. [p=0.2] Cada uma é a primeira letra de uma palavra. [p=0.2] {a}A letra vê, de velocidade: quantos quilômetros o carro anda em uma hora. [p=0.2] {b}A letra dê, de distância: o caminho que ele percorre. [p=0.2] {c}A letra tê, de tempo: quanto dura a viagem. [p=0.3] Daqui em diante, eu chamo cada letra pelo nome."),
    dict(id="s05", block="letras", text="Um carro anda {a}cento e oitenta quilômetros em {b}duas horas. [p=0.3] Em cada hora, anda {c}noventa. [p=0.2] Velocidade: {d}noventa quilômetros por hora. [p=0.3] Foi o que a fórmula fez: [p=0.1] {e}a distância dividida pelo tempo."),
    # isolar o dê
    dict(id="s06", block="isolar", text="Isolar uma letra é {a}deixar ela sozinha de um lado do igual. [p=0.3] Na fórmula, a distância está {b}dividida pelo tempo. [p=0.2] Lembra de xis sobre quatro igual a cinco, o xis dividido por quatro? [p=0.2] Você tirou o quatro {c}multiplicando cada lado por quatro."),
    dict(id="s07", block="isolar", text="Com letra, é igual: {a}multiplique cada lado pelo tempo. [p=0.3] À direita, {b}dividir pelo tempo e multiplicar pelo tempo se anulam, [p=0.2] e sobra {c}a distância sozinha. [p=0.2] À esquerda, fica {d}a velocidade vezes o tempo."),
    dict(id="s08", block="isolar", text="Por que se anulam? [p=0.2] Pense em números. [p=0.2] {a}Dez dividido por dois dá cinco. [p=0.2] {b}Cinco vezes dois volta a dez. [p=0.3] Multiplicar desfaz o que a divisão fez, [p=0.2] {c}seja qual for o número. [p=0.2] Por isso dá para fazer com uma letra, sem saber quanto ela vale."),
    dict(id="s09", block="isolar", text="Resultado: {a}distância igual a velocidade vezes tempo. [p=0.2] Repare que os lados trocaram de lugar. [p=0.1] Pode: trocar os pratos de lugar não tira a balança do equilíbrio. [p=0.2] O ponto no meio, na tela, {b}é sinal de vezes. [p=0.3] Confira com o carro: {c}noventa vezes duas horas dá cento e oitenta quilômetros. [p=0.2] Bateu."),
    dict(id="s10", block="isolar", text="Agora use. [p=0.2] Um carro a {a}oitenta quilômetros por hora viaja {b}três horas. [p=0.2] Distância: {c}oitenta vezes três dá duzentos e quarenta quilômetros. [p=0.3] Conferindo na fórmula do começo: [p=0.2] {d}duzentos e quarenta dividido por três dá oitenta, a velocidade. [p=0.2] Bateu."),
    # isolar o tê
    dict(id="s11", block="tempo", text="E se a pergunta for o tempo? [p=0.2] Parta de {a}distância igual a velocidade vezes tempo. [p=0.2] O tempo está multiplicado pela velocidade, então {b}divida cada lado pela velocidade. [p=0.3] {c}Tempo igual a distância dividida pela velocidade. [p=0.2] Com o primeiro carro: {d}cento e oitenta dividido por noventa dá duas horas."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}escrever distância igual a velocidade dividida pelo tempo. [p=0.2] A pessoa lembra que o tempo muda de lugar, [p=0.1] mas não lembra como. [p=0.3] {b}Teste com o carro: noventa dividido por dois dá quarenta e cinco, [p=0.2] {c}e não cento e oitenta. [p=0.2] Na dúvida, {d}teste a fórmula com números que você conhece."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}o triângulo. [p=0.2] Escreva {b}a letra da distância em cima, [p=0.2] porque na fórmula do começo ela está em cima da fração. [p=0.2] {c}Velocidade e tempo vão embaixo, lado a lado. [p=0.3] {d}Cubra a letra que você quer. [p=0.2] O que sobra é a conta."),
    dict(id="s14", block="atalho", text="{a}Cobriu a distância: sobra velocidade vezes tempo. [p=0.2] {b}Cobriu a velocidade: sobra a distância dividida pelo tempo. [p=0.2] {c}Cobriu o tempo: sobra a distância dividida pela velocidade. [p=0.3] Funciona porque o triângulo é {d}a fórmula desenhada: [p=0.2] lado a lado quer dizer vezes, [p=0.1] e uma letra em cima da outra quer dizer dividido."),
    dict(id="s15", block="atalho", text="{a}Não compensa quando a fórmula tem soma ou subtração, [p=0.2] ou mais de três letras. [p=0.2] Aí, {b}volte para a balança."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Um caminhão viajou {a}trezentos quilômetros [p=0.1] a {b}setenta e cinco quilômetros por hora. [p=0.3] {c}Quantas horas durou a viagem?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Ponha os números em {a}distância igual a velocidade vezes tempo: [p=0.2] {b}trezentos igual a setenta e cinco vezes o tempo. [p=0.3] {c}Divida cada lado por setenta e cinco. [p=0.2] {d}Trezentos dividido por setenta e cinco dá quatro. [p=0.2] {e}Quatro horas."),
    dict(id="s19", block="resposta", text="Conferindo: {a}setenta e cinco vezes quatro dá trezentos. [p=0.2] Bateu. [p=0.3] Pelo triângulo, {b}cobrindo o tempo, [p=0.1] sai a mesma conta: a distância dividida pela velocidade."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}isolar é deixar a letra sozinha, [p=0.2] {b}com a mesma balança das equações, [p=0.2] e {c}teste a fórmula com números."),
    dict(id="s21", block="fim", text="Na próxima aula, você {a}pratica todos os tipos de equação que viu até aqui, [p=0.2] {b}conferindo cada resposta. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
