# Estudativo · MAT-NUM-016 — Somar e subtrair inteiros (Matemática · Números e Contas).
# Habilidade: calcular (−8) + 5, 3 − (−5) e 5 − 8 + 3 − 2 pensando em dívida e pagamento.
# Pré-requisitos: MAT-NUM-015 (negativos e reta numérica). Próxima: MAT-NUM-017.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula.

TITULO = "Somar e subtrair inteiros"

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
    dict(id="s01", block="gancho", text="{a}Três menos, abre parênteses, menos cinco, fecha parênteses. [p=0.3] Se deu {b}menos dois, [p=0.2] você caiu na armadilha. [p=0.3] A resposta é {c}oito."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você soma e subtrai inteiros pensando em {b}dívida e pagamento, [p=0.2] com um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}duas coisas: [p=0.2] {b}a reta numérica [p=0.2] e {c}o oposto: [p=0.2] o número do outro lado do zero, à mesma distância. [p=0.2] O oposto de cinco é menos cinco. [p=0.3] Se faltar alguma, procure no canal."),
    # dívida e pagamento
    dict(id="s04", block="divida", text="Pense assim: {a}número negativo é dívida. [p=0.2] {b}Número positivo é pagamento, dinheiro que entra. [p=0.3] Veja {c}menos oito mais cinco. [p=0.2] Você deve oito reais e paga cinco."),
    dict(id="s05", block="divida", text="Na reta, você {a}sai do menos oito [p=0.2] e {b}anda cinco para a direita. [p=0.3] A dívida é maior que o pagamento, então {c}você ainda deve. [p=0.3] Quanto? A diferença: {d}oito menos cinco dá três. [p=0.2] Como ainda é dívida, o resultado é {e}menos três."),
    dict(id="s06", block="divida", text="Se o pagamento for maior, sobra dinheiro. [p=0.2] {a}Menos três mais sete: [p=0.2] deve três e paga sete. [p=0.2] A diferença é quatro, e ficou {b}mais quatro."),
    dict(id="s07", block="divida", text="E dívida com dívida? [p=0.2] {a}Menos quatro menos seis: [p=0.2] você deve quatro e faz {b}mais uma dívida de seis. [p=0.2] Na reta, {c}só anda para a esquerda. [p=0.2] As dívidas se somam: {d}menos dez."),
    dict(id="s08", block="divida", text="A regra, então: [p=0.2] {a}sinais iguais, some e mantenha o sinal. [p=0.3] {b}Sinais diferentes, olhe os números sem o sinal: tire o menor do maior [p=0.2] e fique com {c}o sinal de quem for maior, dívida ou pagamento."),
    # tirar uma dívida
    dict(id="s09", block="tirar", text="Voltando ao começo: {a}três menos, abre parênteses, menos cinco, fecha parênteses. [p=0.3] O parêntese só impede que os sinais encostem. [p=0.2] Tirar um número negativo é {b}tirar uma dívida. [p=0.3] Imagine que seu saldo é três porque você tem {c}oito reais no bolso [p=0.2] e {d}uma dívida de cinco."),
    dict(id="s10", block="tirar", text="A loja {a}cancela essa dívida. [p=0.2] Seu saldo pula para {b}oito. [p=0.3] {c}Tirar uma dívida é como ganhar esse dinheiro."),
    dict(id="s11", block="tirar", text="Por isso, {a}subtrair um número é somar o oposto dele. [p=0.3] {b}Tirar menos cinco vira somar cinco: três mais cinco, {c}que dá oito. [p=0.3] Confira com uma soma: {d}oito mais uma dívida de cinco dá três. [p=0.3] Na reta, tirar dívida {e}anda para a direita: você sai do três e dá cinco passos até o oito."),
    dict(id="s12", block="tirar", text="E o menos dois do começo? [p=0.2] A pessoa {a}fez três menos cinco [p=0.2] e {b}jogou fora um dos sinais de menos. [p=0.3] Aquela conta seria gastar cinco reais. [p=0.2] Aqui acontece o contrário: a dívida {c}simplesmente deixou de existir."),
    # em fila
    dict(id="s13", block="fila", text="E várias contas em fila? [p=0.2] {a}Cinco menos oito mais três menos dois. [p=0.3] Pense assim: você tem cinco reais, gasta oito, recebe três e gasta dois. [p=0.2] Vá da esquerda para a direita, acompanhando o saldo. [p=0.2] {b}Cinco menos oito dá menos três. [p=0.2] {c}Menos três mais três dá zero. [p=0.2] {d}Zero menos dois dá menos dois."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com um erro comum: [p=0.2] em {a}menos oito mais cinco, [p=0.2] a pessoa vê o menos e soma tudo: {b}menos treze. [p=0.3] Você pagou cinco reais e {c}a dívida aumentou? [p=0.2] Não faz sentido. [p=0.2] {d}Pagamento diminui a dívida: a conta certa é a diferença."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}separe entradas e saídas. [p=0.2] Na mesma conta em fila, {b}junte os positivos: cinco mais três dá oito. [p=0.2] {c}Junte os negativos: saída de oito mais saída de dois dá dez. [p=0.2] No fim, {d}oito que entraram menos dez que saíram dá {e}menos dois."),
    dict(id="s16", block="atalho", text="Funciona porque {a}a ordem em que o dinheiro entra e sai não muda o saldo final, [p=0.2] desde que {b}cada número leve o sinal que está na frente dele. [p=0.3] {c}Com dois números só, não compensa: [p=0.2] faça direto."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Seu saldo está em {a}menos doze reais. [p=0.2] Você {b}deposita vinte reais [p=0.2] e {c}gasta quinze reais. [p=0.2] Depois, o banco {d}cancela uma dívida de seis reais que estava nesse saldo. [p=0.3] {e}Qual é o saldo final?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Menos doze mais vinte dá oito. [p=0.2] {b}Oito menos quinze dá menos sete. [p=0.3] Cancelar é tirar uma dívida: {c}menos sete menos, abre parênteses, menos seis, fecha parênteses. [p=0.2] Isso vira {d}menos sete mais seis, [p=0.2] e o saldo final é {e}menos um real."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}dívida com dívida, soma. [p=0.2] {b}Dívida com pagamento, diferença. [p=0.2] E {c}tirar uma dívida é como ganhar."),
    dict(id="s21", block="fim", text="Na próxima aula, você {a}multiplica e divide com sinal [p=0.2] e entende {b}a regra de sinais [p=0.2] com essa mesma ideia de {c}cancelar dívida. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
