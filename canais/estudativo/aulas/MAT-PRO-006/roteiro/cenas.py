# Estudativo · MAT-PRO-006 — Soma dos termos de uma PA (Matemática · Progressões · Sequências e PA).
# Habilidade: somar 1 + 2 + … + 100 = 5.050 pela ideia de Gauss e calcular o total de 30 dias com Sₙ = (a₁ + aₙ) · n / 2.
# Pré-requisitos: MAT-PRO-004 (razão e termo geral). Próxima: MAT-PRO-007.
# Questão inédita, criada para esta aula. Termos como na MAT-PRO-004: razão, saltos, termo geral; PA = "pê á"; Sₙ = "ésse índice ene".
# A história de Gauss é contada como história ("conta a história"), sem data nem detalhes que não sejam estáveis.
# "Média" explicada na hora: o valor que todos teriam se fossem iguais.
# Gauss: 50 pares de 101 → 5.050 · teste ímpar: 1 + 2 + 3 + 4 + 5 = 15 = (1 + 5) · 5 / 2.
# 30 dias: a₁ = 5, r = 2 · a₃₀ = 5 + 29 · 2 = 63 · S₃₀ = (5 + 63) · 30 / 2 = 68 · 15 = 1.020.
# Erro: (5 + 30) · 30 / 2 = 35 · 15 = 525. Atalho: média 68 / 2 = 34 · 34 · 30 = 1.020 · 101 / 2 = 50,5 → 101 · 50.
# Questão: 20 fileiras, 12 cadeiras na 1ª, +2 por fileira · a₂₀ = 12 + 19 · 2 = 50 · S = 62 · 10 = 620.
# Visual: 1 + 2 + … + 100 com arcos ligando as pontas (1 e 100, 2 e 99, 3 e 98), cada arco "101"; a soma escrita duas vezes
#   (em ordem e de trás para frente) em duas linhas, com colunas "101"; fórmula Sₙ = (a₁ + aₙ) · n / 2 (E.formula) com
#   cada letra apontada; colunas (E.colunas) dos 30 depósitos subindo e uma linha na altura 34 (média).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Soma dos termos de uma PA"

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
    dict(id="s01", block="gancho", text="{a}Um mais dois mais três, e assim por diante, até cem. [p=0.3] Conta a história que um professor passou essa soma para a turma, para ter uma hora de sossego. [p=0.3] Em poucos minutos, um menino respondeu: {b}cinco mil e cinquenta. [p=0.2] O nome dele era {c}Gauss, e ele virou um dos maiores matemáticos da história."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você soma qualquer pê á com a ideia dele, [p=0.2] usa a fórmula da soma [p=0.2] e leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de uma coisa: [p=0.2] {a}o termo geral da pê á, para achar o último termo. [p=0.2] É o primeiro termo, mais um salto de razão para cada passo. [p=0.3] Se faltar, procure no canal."),
    # ideia de Gauss
    dict(id="s04", block="gauss", text="A ideia é {a}juntar as pontas. [p=0.2] {b}Um mais cem dá cento e um. [p=0.2] {c}Dois mais noventa e nove também dá cento e um. [p=0.2] {d}Três mais noventa e oito, de novo. [p=0.3] Um lado sobe um, o outro desce um, e {e}a soma do par não muda."),
    dict(id="s05", block="gauss", text="De um a cem são cem números, então são {a}cinquenta pares. [p=0.2] {b}Cinquenta vezes cento e um dá cinco mil e cinquenta. [p=0.3] Sem somar um número de cada vez."),
    # fórmula
    dict(id="s06", block="dobro", text="E se a quantidade de termos for ímpar? [p=0.2] Um deles fica sem par. [p=0.3] Então escreva a soma {a}duas vezes: uma na ordem, outra de trás para frente. [p=0.3] Cada coluna dá {b}primeiro mais último. [p=0.2] São {c}tantas colunas quantos são os termos. [p=0.2] Isso é a soma em dobro, então {d}divida por dois."),
    dict(id="s07", block="formula", text="Daí sai a fórmula: {a}ésse índice ene igual a, abre parênteses, á índice um mais á índice ene, fecha parênteses, vezes ene, dividido por dois. [p=0.3] {b}Ésse índice ene é a soma dos termos. [p=0.1] {c}Á índice um é o primeiro. [p=0.1] {d}Á índice ene é o último. [p=0.1] {e}Ene é quantos termos são. [p=0.3] Em palavras: {f}primeiro mais último, vezes a quantidade, dividido por dois."),
    dict(id="s08", block="formula", text="Teste com poucos termos: {a}um mais dois mais três mais quatro mais cinco dá quinze. [p=0.2] Pela fórmula: {b}um mais cinco dá seis. [p=0.2] {c}Seis vezes cinco dá trinta. [p=0.2] {d}Dividido por dois dá quinze. [p=0.2] Bateu, mesmo com quantidade ímpar."),
    # 30 dias
    dict(id="s09", block="dias", text="Agora, uma situação real. [p=0.2] Uma pessoa guarda {a}cinco reais no primeiro dia, [p=0.2] e a cada dia {b}dois reais a mais que no dia anterior. [p=0.3] {c}Quanto ela junta em trinta dias?"),
    dict(id="s10", block="dias", text="A fórmula pede o último termo, então ache primeiro. [p=0.2] {a}Do primeiro ao trigésimo dia são vinte e nove saltos. [p=0.2] {b}Vinte e nove vezes dois dá cinquenta e oito. [p=0.2] {c}Mais cinco dá sessenta e três reais no último dia."),
    dict(id="s11", block="dias", text="Agora a soma: {a}cinco mais sessenta e três dá sessenta e oito. [p=0.2] {b}Vezes trinta, dividido por dois. [p=0.2] Divida o trinta primeiro, que é mais fácil: dá quinze. [p=0.2] {c}Sessenta e oito vezes quinze dá mil e vinte reais."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}pôr o número de dias no lugar do último termo. [p=0.2] A pessoa faz {b}cinco mais trinta, vezes trinta, dividido por dois, [p=0.2] e acha {c}quinhentos e vinte e cinco reais."),
    dict(id="s13", block="erro", text="Mas trinta é {a}a posição do último dia, não o que se guardou nele. [p=0.2] {b}No último dia, ela guardou sessenta e três. [p=0.3] É a velha confusão entre posição e valor. [p=0.2] {c}Primeiro ache o último termo, depois some."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}a soma é a média vezes a quantidade. [p=0.3] A média é o valor que todos teriam se fossem iguais, [p=0.2] e na pê á é {b}primeiro mais último, dividido por dois. [p=0.2] Nos trinta dias: {c}sessenta e oito dividido por dois dá trinta e quatro. [p=0.2] {d}Trinta e quatro vezes trinta dá mil e vinte."),
    dict(id="s15", block="atalho", text="Funciona porque {a}o que falta nos primeiros dias sobra nos últimos. [p=0.2] É como se ela guardasse trinta e quatro reais todo dia. [p=0.3] Não compensa quando {b}primeiro mais último dá ímpar, como o cento e um de Gauss: [p=0.2] a média vira {c}cinquenta vírgula cinco. [p=0.2] Aí, {d}divida a quantidade por dois: cento e um vezes cinquenta."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Um auditório tem {a}vinte fileiras de cadeiras. [p=0.2] A primeira fileira tem {b}doze cadeiras, [p=0.2] e cada fileira tem {c}duas cadeiras a mais que a da frente. [p=0.3] {d}Quantas cadeiras há no auditório?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Primeiro, a última fileira: {a}dezenove saltos de dois dá trinta e oito. [p=0.2] {b}Doze mais trinta e oito dá cinquenta cadeiras. [p=0.3] Agora a soma: {c}doze mais cinquenta dá sessenta e dois. [p=0.2] {d}Vinte dividido por dois dá dez. [p=0.2] {e}Sessenta e dois vezes dez dá seiscentas e vinte cadeiras."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}ache o último termo, [p=0.2] {b}some as pontas, [p=0.2] {c}multiplique pela quantidade e divida por dois."),
    dict(id="s20", block="fim", text="Na próxima aula, é {a}hora de praticar: [p=0.2] figuras, calendários e pagamentos, [p=0.2] com tudo o que você viu de sequências e de pê á. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
