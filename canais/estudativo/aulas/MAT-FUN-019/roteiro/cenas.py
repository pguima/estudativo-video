# Estudativo · MAT-FUN-019 — Máximo e mínimo em problemas (Matemática · Funções · Função quadrática).
# Habilidade: achar a altura máxima de h(t) = −5t² + 20t e o lucro máximo de L(x) = −x² + 40x − 300, respondendo o x ou o y conforme a pergunta.
# Pré-requisitos: MAT-FUN-018 (vértice: −b/2a, média das raízes, f(xv)). Próxima: MAT-FUN-020.
# Questão inédita, criada para esta aula. yv = −Δ/4a não entra (a MAT-FUN-018 não ensina). "Loja" como na ponte da MAT-FUN-018.
# Bola: a = −5, b = 20, c = 0 · tv = −20/(2·(−5)) = 2 s · h(2) = −20 + 40 = 20 m · raízes 0 e 4 (atalho da MAT-FAT-007: 0 e −b/a).
# Lucro: L(x) = −x² + 40x − 300 · xv = −40/(−2) = 20 caixas · L(20) = −400 + 800 − 300 = 100 reais · erro: responder "lucro de 20 reais".
# Questão: T(t) = t² − 6t + 5 (câmara fria) · a = 1 > 0, mínimo · tv = 3 h · T(3) = 9 − 18 + 5 = −4 graus.
# Visual: E.plano com E.curva de −5t² + 20t de 0 a 4 (eixos tempo/altura), E.ponto no vértice (2, 20) com guias; setas "quando?" no eixo x
#   e "quanto?" no eixo y; parábola de −x² + 40x − 300 de 10 a 30 com vértice (20, 100); parábola de t² − 6t + 5 com vértice (3, −4).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; a letra a se fala "á"; L se fala "ele".

TITULO = "Máximo e mínimo em problemas"

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
    dict(id="s01", block="gancho", text="Uma bola é chutada para cima. [p=0.2] {a}A altura dela, em metros, é agá de tê igual a menos cinco tê ao quadrado mais vinte tê. [p=0.3] {b}Qual é a altura máxima? [p=0.3] Se você respondeu {c}dois, [p=0.2] respondeu quando ela chega lá, e não a que altura."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha o maior e o menor valor de uma função num problema, [p=0.2] responde {b}exatamente o que foi perguntado [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}uma coisa só: o vértice. [p=0.2] {b}O xis do vértice é menos bê dividido por dois á, ou a média das raízes. [p=0.2] {c}O ípsilon do vértice sai trocando esse xis na função. [p=0.3] Se faltar, procure no canal."),
    # ideia
    dict(id="s04", block="ideia", text="Por que o vértice resolve problemas? [p=0.2] Com {a}á negativo, a parábola abre para baixo: [p=0.2] sobe, faz a curva e desce. [p=0.2] O vértice é {b}o ponto mais alto. [p=0.2] Ali está {c}o máximo da função."),
    dict(id="s05", block="ideia", text="Com {a}á positivo, ela abre para cima, como um sorriso. [p=0.2] O vértice é {b}o ponto mais baixo: [p=0.2] {c}o mínimo. [p=0.3] Então, antes de qualquer conta, {d}olhe o sinal do á."),
    # bola
    dict(id="s06", block="bola", text="Na bola, {a}tê é o tempo em segundos, e agá é a altura em metros. [p=0.2] {b}Á vale menos cinco, bê vale vinte, e não tem cê. [p=0.2] Á negativo: {c}a curva tem um ponto mais alto."),
    dict(id="s07", block="bola", text="{a}O tê do vértice é menos bê dividido por dois á. [p=0.2] {b}Menos bê é menos vinte. [p=0.2] {c}Dois á é dois vezes menos cinco: menos dez. [p=0.2] {d}Menos vinte dividido por menos dez: dois segundos."),
    dict(id="s08", block="bola", text="A altura nesse instante é {a}agá de dois. [p=0.2] {b}Dois ao quadrado é quatro, que vezes menos cinco dá menos vinte. [p=0.2] {c}Vinte vezes dois dá quarenta. [p=0.2] {d}Menos vinte mais quarenta: vinte metros."),
    dict(id="s09", block="bola", text="E aqui está o segredo dos problemas. [p=0.2] {a}O xis do vértice diz quando, ou quanto você usa. [p=0.2] {b}O ípsilon do vértice diz o valor máximo, ou mínimo. [p=0.3] A altura máxima é {c}vinte metros, [p=0.2] e a bola chega lá {d}aos dois segundos."),
    # lucro
    dict(id="s10", block="lucro", text="Segundo problema. [p=0.2] Uma loja vende xis caixas por dia. [p=0.2] {a}O lucro, em reais, é ele de xis igual a menos xis ao quadrado mais quarenta xis menos trezentos. [p=0.3] {b}Quantas caixas dão o maior lucro? [p=0.2] {c}E qual é esse lucro?"),
    dict(id="s11", block="lucro", text="{a}Á vale menos um: tem máximo. [p=0.2] {b}Xis do vértice: menos bê é menos quarenta, e dois á é menos dois. [p=0.2] Menos quarenta dividido por menos dois dá vinte. [p=0.3] {c}Ele de vinte: vinte ao quadrado é quatrocentos, e com o menos na frente fica menos quatrocentos. [p=0.2] Mais oitocentos, menos trezentos: [p=0.2] {d}cem reais."),
    dict(id="s12", block="lucro", text="Respostas: {a}vinte caixas por dia, [p=0.2] e {b}lucro máximo de cem reais. [p=0.3] A pergunta {c}quantas caixas pede o xis. [p=0.2] A pergunta {d}qual é o lucro pede o ípsilon."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é {a}parar no xis do vértice. [p=0.2] A pessoa acha vinte e responde que {b}o lucro máximo é vinte reais. [p=0.3] Mas vinte é {c}a quantidade de caixas. [p=0.2] O lucro é {d}o valor da função nesse ponto: cem reais. [p=0.2] {e}Antes de responder, releia: a pergunta quer o xis ou o ípsilon?"),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho da bola: {a}o ponto mais alto fica no meio do voo. [p=0.2] Sem cê, uma raiz é zero, [p=0.2] e a outra é {b}menos bê dividido por á: menos vinte dividido por menos cinco dá quatro. [p=0.3] {c}A bola sai do chão no zero e volta no quatro. [p=0.2] {d}O topo é na metade: dois segundos."),
    dict(id="s15", block="atalho", text="Funciona porque {a}a parábola é simétrica, e o vértice fica no meio das raízes. [p=0.3] {b}Não compensa quando existe cê, como no lucro: [p=0.2] aí, achar as raízes pede Bhaskara, [p=0.2] e {c}menos bê dividido por dois á sai numa conta só."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Uma câmara fria é ligada. [p=0.2] {a}Tê horas depois, a temperatura dela, em graus, [p=0.2] é {b}tê ao quadrado menos seis tê mais cinco. [p=0.3] {c}Qual é a menor temperatura? [p=0.2] {d}E depois de quantas horas ela acontece?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Á vale um, positivo: a curva tem um ponto mais baixo. [p=0.2] {b}Tê do vértice: seis dividido por dois dá três horas. [p=0.3] {c}Temperatura nesse instante: nove menos dezoito mais cinco. [p=0.2] {d}Menos quatro graus."),
    dict(id="s19", block="resposta", text="A menor temperatura é {a}menos quatro graus, [p=0.2] e ela acontece {b}três horas depois de ligar. [p=0.3] Quem respondeu três graus {c}parou no xis do vértice."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}o sinal do á diz se é máximo ou mínimo, [p=0.2] {b}o xis do vértice diz quando, ou quanto usar, [p=0.2] e {c}o ípsilon do vértice diz o valor máximo ou mínimo."),
    dict(id="s21", block="fim", text="Na próxima aula, a função não vem pronta: {a}você monta a função a partir da história. [p=0.2] Um ingresso em que {b}cada real de desconto vende dez ingressos a mais. [p=0.2] {c}Qual preço dá o maior dinheiro no caixa? [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
