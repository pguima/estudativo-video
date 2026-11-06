# Estudativo · MAT-FRA-004 — Frações maiores que 1 e número misto (Matemática · Frações e Decimais).
# Habilidade: transformar 7/3 em 2 1/3 e voltar.
# Pré-requisitos: MAT-FRA-001. Próxima: MAT-FRA-005.
# Simplificação não está na cadeia desta aula: todos os restos dão fração já na forma final.

TITULO = "Frações maiores que 1 e número misto"

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
    dict(id="s01", block="gancho", text="Uma barra tem {a}três pedaços. [p=0.3] Como alguém pode comer {b}sete terços? [p=0.3] Parece erro de digitação, [p=0.2] mas é só {c}um jeito de contar mais de uma barra."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}transformar sete terços em dois inteiros e um terço, [p=0.2] {b}voltar para sete terços, [p=0.2] e ainda leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}saber o que é uma fração [p=0.2] e {c}dividir com resto, como dezessete dividido por cinco, que dá três e sobram dois. [p=0.3] Se faltar alguma, procure a aula no canal."),
    # barras
    dict(id="s04", block="barras", text="Pegue {a}três barras de chocolate iguais, [p=0.2] cada uma cortada em {b}três pedaços. [p=0.2] Cada pedaço é {c}um terço."),
    dict(id="s05", block="barras", text="Sete terços são {a}sete desses pedaços. [p=0.3] Três pedaços completam {b}uma barra. [p=0.2] Mais três completam {c}outra. [p=0.2] E sobra {d}um pedaço."),
    dict(id="s06", block="barras", text="Você tem {a}duas barras inteiras e mais um terço. [p=0.3] É a mesma quantidade, escrita de dois jeitos: {b}sete terços, [p=0.2] ou {c}dois inteiros e um terço."),
    # nomes
    dict(id="s07", block="nomes", text="Esses jeitos têm nome. [p=0.2] Quando o de cima é maior ou igual ao de baixo, é uma {a}fração imprópria: [p=0.2] ela vale um inteiro ou mais. [p=0.3] Quando o de cima é menor, é uma {b}fração própria: [p=0.2] vale menos que um inteiro."),
    dict(id="s08", block="nomes", text="E um inteiro junto com uma fração é um {a}número misto. [p=0.2] Lê-se {b}dois inteiros e um terço. [p=0.3] Você já usou um sem saber: {c}uma receita com duas xícaras e meia."),
    # ida
    dict(id="s09", block="ida", text="Para ir da fração ao número misto, lembre que {a}o traço é uma divisão. [p=0.2] Faça {b}sete dividido por três. [p=0.3] Dá {c}dois, [p=0.2] e {d}sobra um."),
    dict(id="s10", block="ida", text="Cada número tem seu lugar. [p=0.2] {a}O resultado vira o inteiro. [p=0.2] {b}O resto vira o de cima. [p=0.2] {c}O de baixo continua igual, [p=0.2] porque o tamanho do pedaço não mudou."),
    dict(id="s11", block="ida", text="Mais um: {a}onze quartos. [p=0.2] Onze dividido por quatro: {b}dá dois, sobram três. [p=0.3] {c}Dois inteiros e três quartos."),
    dict(id="s12", block="ida", text="E quando a divisão não tem resto? [p=0.2] {a}Doze quartos: doze dividido por quatro, três, sem sobra. [p=0.3] {b}O resultado é um número inteiro, [p=0.2] e não precisa de fração nenhuma."),
    # volta
    dict(id="s13", block="volta", text="Para voltar, pense nos pedaços. [p=0.2] Cada barra tem três pedaços, então {a}duas barras têm dois vezes três: seis. [p=0.3] Com {b}o pedaço que sobrou, {c}seis mais um, sete. [p=0.2] {d}Sete terços."),
    dict(id="s14", block="volta", text="A regra é esta: {a}inteiro vezes o de baixo, [p=0.2] {b}mais o de cima. [p=0.2] {c}O de baixo continua igual. [p=0.3] É a mesma {d}prova real da divisão: [p=0.2] resultado vezes divisor, mais o resto."),
    dict(id="s15", block="volta", text="Treine com {a}três inteiros e dois quintos. [p=0.2] Três vezes cinco, {b}quinze. [p=0.2] Mais dois, {c}dezessete. [p=0.2] {d}Dezessete quintos."),
    # erro
    dict(id="s16", block="erro", text="Cuidado com o erro mais comum. [p=0.2] A pessoa vê dois inteiros e um terço e {a}soma o inteiro com o de cima: [p=0.2] dois mais um, {b}três terços."),
    dict(id="s17", block="erro", text="Mas {a}três terços é uma barra só, [p=0.2] e você tinha {b}mais de duas. [p=0.3] Cada inteiro vale {c}três pedaços, não um. [p=0.2] Por isso o inteiro {d}multiplica antes de somar."),
    # atalho
    dict(id="s18", block="atalho", text="E o atalho prometido: {a}a tabuada do de baixo. [p=0.3] Veja {b}vinte e três quartos. [p=0.2] Sem armar conta, ache na tabuada do quatro o maior resultado que não passa de vinte e três: {c}quatro vezes cinco, vinte."),
    dict(id="s19", block="atalho", text="{a}O cinco é o inteiro. [p=0.2] De vinte para vinte e três, {b}faltam três, e esse é o de cima. [p=0.2] {c}Cinco inteiros e três quartos."),
    dict(id="s20", block="atalho", text="Funciona porque dividir é {a}ver quantas vezes o de baixo cabe no de cima. [p=0.3] Não compensa fora da tabuada, como em {b}trezentos e sete sétimos: [p=0.2] aí, {c}arme a conta."),
    # questão
    dict(id="s21", block="questao", text="Hora de testar. [p=0.2] Uma pizzaria corta cada pizza em {a}oito fatias. [p=0.2] Em uma noite, vendeu {b}dezenove fatias. [p=0.3] {c}Quantas pizzas foram vendidas, em número misto?"),
    dict(id="s22", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s23", block="resposta", text="Vamos lá. [p=0.2] Cada fatia é um oitavo, então são {a}dezenove oitavos. [p=0.3] Tabuada do oito: {b}oito vezes dois, dezesseis. [p=0.2] De dezesseis para dezenove, {c}faltam três. [p=0.3] {d}Dois inteiros e três oitavos de pizza."),
    dict(id="s24", block="resposta", text="Confira voltando: {a}dois vezes oito, dezesseis. [p=0.2] {b}Mais três, dezenove. [p=0.2] Bateu."),
    # fechamento
    dict(id="s25", block="fim", text="Resumindo: {a}para ir, divide, e o resto vira o de cima. [p=0.2] {b}Para voltar, inteiro vezes o de baixo, mais o de cima."),
    dict(id="s26", block="fim", text="Na próxima aula, você vai {a}comparar frações e marcar cada uma na reta, [p=0.2] inclusive as maiores que um, como {b}cinco meios. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
