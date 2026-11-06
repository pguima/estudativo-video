# Estudativo · MAT-FRA-007 — Somar e subtrair com denominadores iguais (Matemática · Frações e Decimais).
# Habilidade: calcular 2/7 + 3/7 e descobrir quanto falta para 1 inteiro em 5/9.
# Pré-requisitos: MAT-FRA-001, MAT-NUM-004. Próxima: MAT-FRA-008.
# Simplificação ainda não foi ensinada (MAT-FRA-003): todos os resultados já estão na forma final.

TITULO = "Somar e subtrair frações com denominadores iguais"

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
    dict(id="s01", block="gancho", text="{a}Dois sétimos {b}mais três sétimos. [p=0.3] Se a sua resposta foi {c}cinco catorze avos, [p=0.2] você somou uma coisa que não se soma."),
    dict(id="s02", block="gancho", text="A boa notícia: a regra certa tem {a}só duas partes. [p=0.3] Até o fim desta aula, você vai somar, subtrair [p=0.2] e descobrir {b}quanto falta para completar um inteiro."),
    # lembrete
    dict(id="s03", block="lembrete", text="Só precisa lembrar de uma coisa. [p=0.2] {a}O denominador, o número de baixo, diz em quantas partes iguais o inteiro foi dividido. [p=0.3] {b}O numerador, o de cima, diz quantas partes você pegou. [p=0.3] Se isso ainda estiver confuso, procure no canal a aula sobre o que é uma fração."),
    # barra
    dict(id="s04", block="barra", text="Imagine {a}uma barra de chocolate cortada em {b}sete pedaços iguais. [p=0.2] Cada pedaço é {c}um sétimo da barra."),
    dict(id="s05", block="barra", text="Você come {a}dois pedaços. [p=0.3] Depois, mais {b}três. [p=0.3] Quantos pedaços comeu?"),
    dict(id="s06", block="barra", text="{a}Cinco pedaços. [p=0.2] Cada pedaço é um sétimo, então são {b}cinco sétimos. [p=0.3] A barra continua cortada em sete, [p=0.2] então o denominador {c}não mudou."),
    # regra
    dict(id="s07", block="regra", text="E essa é toda a regra: {a}soma os de cima [p=0.3] e {b}repete o de baixo."),
    dict(id="s08", block="regra", text="Pense assim: {a}duas maçãs mais três maçãs dá {b}cinco maçãs. [p=0.3] A maçã não muda de tamanho na soma. [p=0.2] O sétimo também não. [p=0.2] {c}Ele só diz o tamanho do pedaço."),
    # exemplos
    dict(id="s09", block="exemplos", text="Vamos treinar. [p=0.2] {a}Três décimos mais quatro décimos. [p=0.3] Três mais quatro, {b}sete. [p=0.2] Repete o dez. [p=0.2] {c}Sete décimos."),
    dict(id="s10", block="exemplos", text="E com três frações, é igual: {a}um onze avos mais dois onze avos mais três onze avos. [p=0.3] Um mais dois mais três, {b}seis. [p=0.2] {c}Seis onze avos."),
    # subtração
    dict(id="s11", block="subtrair", text="Com subtração, a ideia é a mesma. [p=0.2] {a}Cinco oitavos menos dois oitavos. [p=0.3] Você tinha {b}cinco pedaços, [p=0.2] {c}tirou dois, [p=0.2] sobraram três. [p=0.2] {d}Três oitavos."),
    # inteiro
    dict(id="s12", block="inteiro", text="Vamos para a parte que mais aparece em problema: [p=0.2] {a}quanto falta para completar um inteiro? [p=0.3] Se a barra foi cortada em nove, {b}a barra inteira são nove nonos."),
    dict(id="s13", block="inteiro", text="Você tem {a}cinco nonos. [p=0.3] Quanto falta? [p=0.2] {b}Nove menos cinco, quatro. [p=0.2] {c}Faltam quatro nonos."),
    # erro
    dict(id="s14", block="erro", text="Agora, o erro do começo: {a}somar os de baixo também. [p=0.3] Quem faz isso escreve {b}cinco catorze avos, [p=0.2] ou seja, cinco pedaços de uma barra cortada em catorze. [p=0.2] Pedaços bem menores."),
    dict(id="s15", block="erro", text="Olhe para a barra. [p=0.2] {a}Cinco pedaços de sete passam da metade. [p=0.3] {b}Cinco pedaços de catorze não chegam nem na metade, que seria sete. [p=0.3] Você comeu mais da metade, e a conta diz que foi menos. [p=0.2] Sinal claro de erro."),
    # atalho
    dict(id="s16", block="atalho", text="Por fim, dois atalhos. [p=0.2] {a}Primeiro: tampe o denominador com o dedo. [p=0.2] Faça a conta só com os de cima, [p=0.2] destampe, e pronto."),
    dict(id="s17", block="atalho", text="{a}Segundo: quando o de cima fica igual ao de baixo, deu um inteiro. [p=0.3] {b}Três sétimos mais quatro sétimos dá {c}sete sétimos, [p=0.2] que é {d}a barra inteira. [p=0.2] {e}Um."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Uma pessoa pagou {a}dois quintos de uma dívida no primeiro mês [p=0.1] e {b}um quinto no segundo. [p=0.3] {c}Que fração da dívida ainda falta pagar?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] O que já foi pago: {a}dois quintos mais um quinto, {b}três quintos. [p=0.3] A dívida inteira são {c}cinco quintos. [p=0.2] {d}Cinco menos três, dois. [p=0.2] {e}Faltam dois quintos."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: com denominadores iguais, {a}soma ou subtrai os de cima [p=0.2] e {b}repete o de baixo. [p=0.3] E dá um inteiro {c}quando o de cima fica igual ao de baixo."),
    dict(id="s22", block="fim", text="Na próxima aula, os denominadores são {a}diferentes, [p=0.2] e você vai ver por que um meio mais um terço não dá dois quintos. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
