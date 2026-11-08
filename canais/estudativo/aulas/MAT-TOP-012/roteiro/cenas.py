# Estudativo · MAT-TOP-012 — Hipérbole e como reconhecer cada cônica (Matemática · Tópicos Avançados · Noções de cônicas).
# Habilidade: ler em x²/9 − y²/16 = 1 os focos (±5, 0) e as assíntotas y = ±4x/3 e dizer pela equação se a cônica é parábola, elipse ou hipérbole.
# Pré-requisitos: MAT-ANA-004 (reta reduzida y = mx + n, "eme" = quanto sobe a cada passo), MAT-TOP-011 (elipse, a² = b² + c²). Próxima: MAT-TOP-013.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas "á", "bê", "cê", "eme", "xis", "ípsilon". Frações lidas com "dividido por".
# Contas: vértice (3, 0): até (−5, 0) = 8, até (5, 0) = 2, 8 − 2 = 6 = 2a. x = 0: −y²/16 = 1 → y² = −16 (não existe).
#   c² = 9 + 16 = 25 → c = 5. Assíntotas: sobe 4 a cada 3 → y = 4x/3 e y = −4x/3. Erro: 16 − 9 = 7, r{7} ≈ 2,6 < 3.
#   Questão: x²/36 − y²/64 = 1 → a = 6, b = 8, c² = 100, c = 10, focos (±10, 0); assíntotas y = ±8x/6 = ±4x/3.
#   Reconhecer: x²/16 + y²/7 = 1 (elipse), y² = 12x (parábola), y²/4 − x²/5 = 1 (hipérbole).

TITULO = "Hipérbole: focos, assíntotas e como reconhecer cada cônica"

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
    dict(id="s01", block="gancho", text="Troque {a}um sinal só. [p=0.2] {b}Com mais, a equação desenha uma elipse. [p=0.3] {c}Com menos, a figura se abre em dois pedaços, [p=0.2] que nunca se encontram. [p=0.3] É {d}a hipérbole."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha os focos de uma hipérbole e as retas que guiam os seus dois pedaços, [p=0.2] diz pela equação qual figura ela desenha [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}na elipse, os denominadores são os semieixos ao quadrado, e á ao quadrado é bê ao quadrado mais cê ao quadrado; [p=0.2] e {c}na reta ípsilon igual a eme xis, o eme diz quanto a reta sobe a cada passo para a direita. [p=0.3] Se faltar alguma, procure no canal."),
    # a definição
    dict(id="s04", block="definicao", text="Na elipse, {a}a soma das distâncias até os focos era fixa. [p=0.3] Na hipérbole, {b}fixa é a diferença: [p=0.2] a distância até o foco mais longe, {c}menos a distância até o foco mais perto."),
    dict(id="s05", block="definicao", text="Com os focos em {a}xis menos cinco e xis cinco, [p=0.2] pegue o ponto {b}xis três, ípsilon zero. [p=0.2] Até o foco longe, {c}oito. [p=0.2] Até o perto, {d}dois. [p=0.2] {e}Oito menos dois, seis. [p=0.3] Todo ponto da hipérbole dá {f}esse mesmo seis."),
    # a equação
    dict(id="s06", block="equacao", text="A equação reduzida é {a}a da elipse, com menos no meio: [p=0.2] {b}xis ao quadrado dividido por nove, menos ípsilon ao quadrado dividido por dezesseis, igual a um. [p=0.3] Aqui, {c}á ao quadrado é nove, e á é três. [p=0.2] {d}Bê ao quadrado é dezesseis, e bê é quatro."),
    dict(id="s07", block="equacao", text="No eixo xis, {a}o ípsilon vale zero: [p=0.2] xis ao quadrado dá nove, e {b}xis é três ou menos três. [p=0.2] São os vértices, as pontas dos dois pedaços. [p=0.3] {c}Seis de um vértice ao outro: a diferença das distâncias é duas vezes o á."),
    dict(id="s08", block="equacao", text="E no eixo ípsilon? [p=0.2] {a}O xis vale zero, [p=0.2] e sobra {b}menos ípsilon ao quadrado dividido por dezesseis igual a um. [p=0.2] Ípsilon ao quadrado daria {c}menos dezesseis. [p=0.2] Nenhum número ao quadrado é negativo. [p=0.3] Por isso a hipérbole {d}não corta o eixo ípsilon, e fica partida em dois."),
    # focos e assíntotas
    dict(id="s09", block="caixa", text="Para achar os focos, monte {a}uma caixa: [p=0.2] {b}três para cada lado do centro, que é o á, [p=0.2] e {c}quatro para cima e para baixo, que é o bê."),
    dict(id="s10", block="caixa", text="{a}A diagonal da caixa, do centro até o canto, é a hipotenusa de catetos três e quatro: [p=0.2] {b}cinco. [p=0.3] Esse é o cê. [p=0.2] Aqui, {c}cê ao quadrado é á ao quadrado mais bê ao quadrado: [p=0.2] nove mais dezesseis, vinte e cinco. [p=0.3] Focos em {d}xis menos cinco e xis cinco."),
    dict(id="s11", block="caixa", text="Agora, {a}prolongue as diagonais. [p=0.3] Os dois pedaços chegam {b}cada vez mais perto dessas retas, [p=0.2] mas nunca encostam. [p=0.2] Elas se chamam {c}assíntotas."),
    dict(id="s12", block="caixa", text="Cada assíntota passa pelo centro, então é ípsilon igual a eme xis. [p=0.2] A diagonal {a}sobe quatro a cada três passos: [p=0.2] {b}eme é quatro terços. [p=0.3] As assíntotas são {c}ípsilon igual a quatro xis dividido por três, [p=0.2] e {d}ípsilon igual a menos quatro xis dividido por três."),
    # reconhecer
    dict(id="s13", block="reconhecer", text="Parábola, elipse e hipérbole são chamadas de {a}cônicas. [p=0.2] Para saber qual é, olhe os quadrados. [p=0.3] {b}Só uma letra ao quadrado, como em xis ao quadrado igual a oito ípsilon: [p=0.2] {c}parábola."),
    dict(id="s14", block="reconhecer", text="{a}Xis ao quadrado e ípsilon ao quadrado somando: [p=0.2] {b}elipse. [p=0.2] Se os denominadores forem iguais, {c}é uma circunferência. [p=0.3] {d}Os dois ao quadrado, com um sinal de menos entre eles: [p=0.2] {e}hipérbole."),
    dict(id="s15", block="reconhecer", text="E na hipérbole, {a}a letra que vem com o sinal de mais diz o eixo dos focos. [p=0.3] {b}Ípsilon ao quadrado dividido por nove, menos xis ao quadrado dividido por dezesseis, igual a um: [p=0.2] {c}os pedaços se abrem para cima e para baixo, [p=0.2] e os focos ficam no eixo ípsilon."),
    # erro
    dict(id="s16", block="erro", text="Agora, cuidado com o erro mais comum: [p=0.2] {a}levar a conta da elipse para a hipérbole. [p=0.2] A pessoa faz {b}cê ao quadrado igual a dezesseis menos nove, que dá sete. [p=0.3] A raiz de sete dá {c}uns dois vírgula seis."),
    dict(id="s17", block="erro", text="Só que o foco fica {a}dentro da curva, além do vértice. [p=0.2] {b}O cê tem que passar de três. [p=0.3] Na elipse, o maior é o á, e o cê sai de uma subtração. [p=0.2] {c}Na hipérbole, o maior é o cê, e ele sai de uma soma."),
    # atalho
    dict(id="s18", block="atalho", text="Agora o atalho: {a}a caixa resolve tudo. [p=0.3] O número embaixo do termo com mais {b}é o á ao quadrado. [p=0.2] O número embaixo do termo com menos {c}é o bê ao quadrado. [p=0.3] {d}A diagonal da caixa dá o cê, [p=0.2] e {e}as diagonais prolongadas são as assíntotas."),
    dict(id="s19", block="atalho", text="Funciona porque o canto da caixa fica a {a}á passos para o lado e bê passos para cima do centro. [p=0.2] A diagonal é a hipotenusa: {b}cê ao quadrado igual a á ao quadrado mais bê ao quadrado. [p=0.3] {c}Não compensa quando a questão só pede o nome da figura: [p=0.2] aí, {d}basta olhar os sinais."),
    # questão
    dict(id="s20", block="questao", text="Hora de testar. [p=0.2] Primeira: na hipérbole {a}xis ao quadrado dividido por trinta e seis, menos ípsilon ao quadrado dividido por sessenta e quatro, igual a um, [p=0.2] onde ficam os focos, e quais são as assíntotas? [p=0.3] Segunda: que figura desenha {b}cada uma das três equações da tela?"),
    dict(id="s21", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="resposta", text="Vamos lá. [p=0.2] {a}O á é a raiz de trinta e seis, seis. [p=0.2] {b}O bê é a raiz de sessenta e quatro, oito. [p=0.3] {c}Seis ao quadrado mais oito ao quadrado dá cem, e cê dá dez: [p=0.2] focos em {d}xis menos dez e xis dez. [p=0.3] {e}A caixa sobe oito a cada seis passos: [p=0.2] eme é oito sextos, que simplifica para {f}quatro terços. [p=0.2] As mesmas assíntotas do exemplo da aula."),
    dict(id="s23", block="resposta", text="{a}Xis ao quadrado e ípsilon ao quadrado somando: elipse. [p=0.3] {b}Só o ípsilon ao quadrado: parábola. [p=0.3] {c}Os dois ao quadrado, com menos: hipérbole, [p=0.2] aberta para cima e para baixo, porque o mais está no ípsilon."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}na hipérbole, cê ao quadrado é á ao quadrado mais bê ao quadrado, [p=0.2] {b}as assíntotas são as diagonais da caixa, [p=0.2] e {c}os sinais dizem qual cônica é."),
    dict(id="s25", block="fim", text="Na próxima aula, você pratica tudo: {a}distância de ponto a reta, circunferências, [p=0.2] e {b}as três cônicas, direto da equação. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
