# Estudativo · MAT-FIN-011 — À vista ou a prazo (Matemática · Matemática Financeira).
# Habilidade: comparar R$ 1.000 hoje com R$ 1.100 daqui a 2 meses na mesma data e achar a taxa embutida em R$ 200 à vista ou R$ 100 + R$ 110.
# Pré-requisitos: MAT-FIN-006 (achar o capital ou o tempo), MAT-POR-005 (variação percentual). Próxima: MAT-FIN-012.
# Questão inédita, criada para esta aula. Contas de juros compostos feitas mês a mês, de cabeça.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "À vista ou a prazo"

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
    dict(id="s01", block="gancho", text="{a}Uma loja vende um produto por duzentos reais à vista. [p=0.2] Ou {b}cem de entrada e cento e dez daqui a um mês. [p=0.3] Parece só cinco por cento a mais. [p=0.2] Mas são {c}dez por cento de juros ao mês."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai comparar valores em datas diferentes e achar os juros escondidos numa compra a prazo, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de duas coisas. [p=0.2] {a}Juros compostos: para levar um valor para a frente, multiplique pelo fator; [p=0.2] para trazer para hoje, divida pelo fator, e você acha o valor presente. [p=0.2] E a {b}variação percentual: a diferença dividida pelo valor de antes. [p=0.3] Se faltar alguma, procure no canal."),
    # mesma data
    dict(id="s04", block="datas", text="Primeira ideia: {a}dinheiro em datas diferentes não se compara direto. [p=0.3] Mil reais hoje ou {b}mil e cem daqui a dois meses? [p=0.2] Depende de quanto o seu dinheiro rende enquanto espera."),
    dict(id="s05", block="datas", text="Digamos que você deve mil reais numa compra, [p=0.2] e a loja aceita {a}mil e cem em dois meses. [p=0.2] O seu dinheiro rende {b}cinco por cento ao mês, uma taxa alta, escolhida só para a conta sair redonda. [p=0.3] Leve tudo para {c}a mesma data: daqui a dois meses."),
    dict(id="s06", block="datas", text="Aplicados, os mil reais viram {a}mil e cinquenta no primeiro mês. [p=0.2] No segundo, cinco por cento de mil e cinquenta são cinquenta e dois reais e cinquenta centavos. [p=0.2] Total: {b}mil cento e dois reais e cinquenta centavos."),
    dict(id="s07", block="datas", text="Na data do pagamento, você tem {a}mil cento e dois reais e cinquenta centavos. [p=0.2] E deve {b}mil e cem. [p=0.2] Paga e ainda sobram dois reais e cinquenta centavos. [p=0.3] Com esse rendimento, {c}pagar a prazo é melhor."),
    dict(id="s08", block="datas", text="A regra: {a}leve todos os valores para a mesma data, com a taxa que o seu dinheiro rende. [p=0.2] Só então, {b}compare. [p=0.3] Se o seu dinheiro rendesse {c}um por cento ao mês, os mil virariam só cerca de mil e vinte, [p=0.2] e {d}pagar à vista ganharia."),
    # taxa embutida
    dict(id="s09", block="embutida", text="Agora, os juros escondidos do começo. [p=0.2] {a}Duzentos à vista, ou cem de entrada e cento e dez em um mês. [p=0.3] A entrada você paga {b}hoje, nas duas formas. [p=0.2] Então tire a entrada dos dois lados."),
    dict(id="s10", block="embutida", text="À vista, depois da entrada, faltariam {a}cem reais hoje. [p=0.2] A prazo, você paga {b}cento e dez daqui a um mês. [p=0.3] É como pegar cem emprestados e devolver cento e dez. [p=0.2] Dez dividido por cem: {c}dez por cento ao mês. [p=0.2] Essa é a {d}taxa de juros embutida, a que está escondida no preço a prazo."),
    # erro
    dict(id="s11", block="erro", text="O erro comum é comparar com o preço inteiro. [p=0.2] A pessoa soma {a}cem mais cento e dez dá duzentos e dez, [p=0.2] e calcula {b}dez dividido por duzentos: cinco por cento. [p=0.3] Mas a entrada {c}não foi emprestada. [p=0.2] Os juros só valem sobre o que ficou para depois."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho, para entrada mais uma parcela. [p=0.2] {a}O saldo é o preço à vista menos a entrada. [p=0.2] {b}Divida a parcela pelo saldo. [p=0.2] O que passar de um é a taxa. [p=0.3] {c}Cento e dez dividido por cem dá um vírgula um: dez por cento."),
    dict(id="s13", block="atalho", text="Funciona porque {a}o saldo é o único dinheiro que fica com a loja durante o mês. [p=0.3] Não compensa com várias parcelas, em meses diferentes: [p=0.2] aí, {b}leve tudo para a mesma data e compare."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Uma geladeira custa {a}novecentos reais à vista, [p=0.2] ou {b}duas parcelas de quinhentos: uma no ato e outra em trinta dias. [p=0.3] {c}Qual é a taxa de juros embutida? [p=0.2] E, se o seu dinheiro rende {d}um por cento ao mês, qual forma vale mais a pena?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] A parcela no ato é a entrada. [p=0.2] Saldo: {a}novecentos menos quinhentos dá quatrocentos. [p=0.2] Daqui a um mês, você paga {b}quinhentos por esses quatrocentos. [p=0.3] Cem dividido por quatrocentos: {c}vinte e cinco por cento ao mês."),
    dict(id="s17", block="resposta", text="Vinte e cinco por cento ao mês é muito mais que {a}um por cento. [p=0.2] Melhor {b}pagar à vista. [p=0.3] Quem dividiu cem por novecentos achou cerca de {c}onze por cento, [p=0.2] e errou a taxa."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}compare valores sempre na mesma data, [p=0.2] e {b}os juros valem só sobre o que fica para depois."),
    dict(id="s19", block="fim", text="Na próxima aula, você monta {a}as parcelas de um financiamento, [p=0.2] e descobre por que, na {b}tabela Price, você paga mais juros que na SAC. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
