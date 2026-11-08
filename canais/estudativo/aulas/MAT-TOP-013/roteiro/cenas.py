# Estudativo · MAT-TOP-013 — Praticando: distâncias, circunferências e cônicas (Matemática · Tópicos Avançados · prática).
# Habilidade: calcular distâncias no plano, comparar circunferências e tirar da equação os elementos de uma cônica.
# Pré-requisitos: MAT-TOP-007 (distância de ponto a reta), MAT-TOP-008 (alinhamento pelo determinante, Sarrus da MAT-MTZ-003),
#   MAT-TOP-009 (posição entre circunferências), MAT-TOP-010 (parábola x² = 8y: foco (0, 2)), MAT-TOP-011 (elipse), MAT-TOP-012 (hipérbole).
#   Próxima: MAT-TOP-014.
# Questões inéditas, criadas para esta aula. Marcas: {cue} animação · [p=0.2] pausa. Números por extenso.
# Contas: 1) |4·2 + 3·3 + 3| = 20; r{16 + 9} = 5; 20 ÷ 5 = 4.
#   2) (1, 1), (3, 5), (4, 8): descendo 5 + 4 + 24 = 33; subindo 20 + 8 + 3 = 31; 33 − 31 = 2 ≠ 0. Inclinações 4/2 = 2 e 3/1 = 3.
#   3) centros (1, 2) e (7, 10): r{36 + 64} = 10; raios 2 e 8; 2 + 8 = 10 → tangentes externas.
#   4) x²/100 + y²/36 = 1: a = 10, b = 6, c² = 64, c = 8; soma = 2a = 20.
#   5) x² = 12y: foco (0, 3), diretriz y = −3 (12 ÷ 4 = 3). y²/9 − x²/16 = 1: hipérbole em pé, c² = 25, focos (0, ±5).

TITULO = "Praticando: distâncias, circunferências e cônicas"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações no plano, criadas para esta aula: [p=0.2] {b}distâncias, pontos alinhados, circunferências {c}e as três cônicas. [p=0.3] Em cada uma, {d}pause o vídeo e resolva antes de ver a resposta. [p=0.2] Errar aqui não custa nada."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}as ferramentas do módulo: [p=0.2] {b}a fórmula da distância de ponto a reta; [p=0.2] {c}o determinante, que dá zero quando os pontos estão alinhados; [p=0.2] {d}a distância entre os centros, comparada com os raios; [p=0.2] e {e}as contas de cada cônica. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1
    dict(id="s03", block="questao1", text="Situação um. [p=0.2] Uma torre de celular fica no ponto {a}xis dois, ípsilon três, [p=0.2] e uma estrada reta é {b}quatro xis mais três ípsilon mais três igual a zero, [p=0.2] com medidas em quilômetros. [p=0.3] {c}Qual é a menor distância da torre até a estrada?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Em cima, {a}troque o ponto na equação da reta: [p=0.2] {b}quatro vezes dois, oito; [p=0.2] {c}três vezes três, nove; [p=0.2] {d}oito mais nove mais três, vinte. [p=0.2] Em módulo, {e}continua vinte."),
    dict(id="s06", block="resposta1", text="Embaixo, {a}a raiz de quatro ao quadrado mais três ao quadrado: [p=0.2] raiz de vinte e cinco, {b}cinco. [p=0.3] {c}Vinte dividido por cinco: quatro quilômetros. [p=0.3] É a distância pelo caminho que {d}chega na estrada em ângulo reto."),
    # situação 2
    dict(id="s07", block="questao2", text="Situação dois. [p=0.2] Os pontos {a}xis um, ípsilon um; [p=0.2] {b}xis três, ípsilon cinco; [p=0.2] e {c}xis quatro, ípsilon oito [p=0.2] estão alinhados?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] Monte o determinante: {a}cada ponto numa linha, com uma coluna de uns no fim. [p=0.2] {b}Copie as duas primeiras colunas ao lado, para o Sarrus."),
    dict(id="s10", block="resposta2", text="{a}Descendo: cinco, mais quatro, mais vinte e quatro, dá trinta e três. [p=0.3] {b}Subindo: vinte, mais oito, mais três, dá trinta e um. [p=0.3] {c}Trinta e três menos trinta e um: dois. [p=0.2] Não deu zero: {d}os pontos não estão alinhados."),
    # atalho
    dict(id="s11", block="atalho", text="Dá para conferir sem determinante, {a}pela inclinação. [p=0.3] {b}Do primeiro ao segundo ponto, o xis anda dois e o ípsilon sobe quatro: [p=0.2] inclinação dois. [p=0.3] {c}Do segundo ao terceiro, o xis anda um e o ípsilon sobe três: [p=0.2] inclinação três. [p=0.3] {d}Inclinações diferentes: o caminho dobra no meio, e os pontos não ficam numa reta só."),
    dict(id="s12", block="atalho", text="Funciona porque, numa reta, {a}a inclinação é a mesma em qualquer trecho. [p=0.3] {b}Não compensa quando a questão pede o determinante, [p=0.2] ou quando ele aparece com uma letra no meio, para você achar o valor que alinha os pontos."),
    # situação 3
    dict(id="s13", block="questao3", text="Situação três. [p=0.2] As circunferências {a}xis menos um, ao quadrado, mais ípsilon menos dois, ao quadrado, igual a quatro, [p=0.2] e {b}xis menos sete, ao quadrado, mais ípsilon menos dez, ao quadrado, igual a sessenta e quatro. [p=0.3] {c}Qual é a posição de uma em relação à outra?"),
    dict(id="s14", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta3", text="Vamos lá. [p=0.2] {a}Centros: xis um, ípsilon dois, [p=0.2] e {b}xis sete, ípsilon dez. [p=0.2] {c}Raios: a raiz de quatro, dois, [p=0.2] e a raiz de sessenta e quatro, oito."),
    dict(id="s16", block="resposta3", text="{a}Distância entre os centros: sete menos um dá seis, dez menos dois dá oito. [p=0.2] {b}Seis ao quadrado mais oito ao quadrado dá cem, e a raiz dá dez. [p=0.3] {c}A soma dos raios: dois mais oito, dez. [p=0.2] Distância igual à soma: {d}tangentes externas, encostadas por fora num ponto só."),
    # situação 4
    dict(id="s17", block="questao4", text="Situação quatro. [p=0.2] A elipse é {a}xis ao quadrado dividido por cem, mais ípsilon ao quadrado dividido por trinta e seis, igual a um. [p=0.3] {b}Onde ficam os focos? [p=0.2] E {c}quanto dá a soma das distâncias de um ponto dela até os dois focos?"),
    dict(id="s18", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta4", text="Vamos lá. [p=0.2] {a}O maior denominador, cem, está embaixo do xis: [p=0.2] á é dez, e a elipse se estica na horizontal. [p=0.2] {b}Bê é a raiz de trinta e seis, seis. [p=0.3] {c}Cê ao quadrado: cem menos trinta e seis, sessenta e quatro. [p=0.2] Cê é oito: focos em {d}xis menos oito e xis oito."),
    dict(id="s20", block="resposta4", text="A soma das distâncias é {a}o tamanho do barbante: [p=0.2] a largura da elipse, {b}duas vezes o á. [p=0.2] {c}Vinte."),
    # situação 5
    dict(id="s21", block="questao5", text="Última situação. [p=0.2] Que cônica é cada equação, [p=0.2] e onde fica o foco? [p=0.3] {a}Xis ao quadrado igual a doze ípsilon. [p=0.3] {b}Ípsilon ao quadrado dividido por nove, menos xis ao quadrado dividido por dezesseis, igual a um."),
    dict(id="s22", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s23", block="resposta5", text="Vamos lá. [p=0.2] {a}Só o xis ao quadrado: parábola. [p=0.2] Em xis ao quadrado igual a oito ípsilon, o foco ficava em ípsilon dois: [p=0.2] {b}um quarto de oito. [p=0.3] Aqui, {c}um quarto de doze, três. [p=0.2] Foco em {d}xis zero, ípsilon três, [p=0.2] e diretriz {e}ípsilon igual a menos três."),
    dict(id="s24", block="resposta5", text="{a}Os dois ao quadrado, com menos: hipérbole. [p=0.2] {b}O mais está no ípsilon: ela se abre para cima e para baixo. [p=0.3] {c}Cê ao quadrado: nove mais dezesseis, vinte e cinco. [p=0.2] Cê é cinco: focos em {d}ípsilon menos cinco e ípsilon cinco."),
    # fechamento
    dict(id="s25", block="fim", text="Resumindo: {a}para distâncias, Pitágoras e a fórmula do ponto à reta; [p=0.2] {b}para circunferências, centros e raios; [p=0.2] e {c}para as cônicas, olhe os sinais e faça a conta do cê."),
    dict(id="s26", block="fim", text="Na próxima aula, começa um assunto novo: [p=0.2] {a}contar em outras bases, [p=0.2] como a {b}binária dos computadores, e a de sessenta, das horas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
