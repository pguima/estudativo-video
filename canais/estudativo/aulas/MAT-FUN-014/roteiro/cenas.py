# Estudativo · MAT-FUN-014 — Custo, receita e lucro: o ponto de equilíbrio (Matemática · Funções · Função afim).
# Habilidade: montar C(x) = 2.000 + 30x e R(x) = 50x, achar o equilíbrio em 100 peças e ler no gráfico qual de dois planos compensa.
# Pré-requisitos: MAT-EQU-014 (comparar dois planos), MAT-FUN-010 (valor inicial e quanto sobe por unidade). Próxima: MAT-FUN-015.
# Questão inédita, criada para esta aula. Valores da fábrica e da doceira inventados; planos A e B são os da MAT-EQU-014.
# Função linear (MAT-FUN-013) fora da ficha: a receita é descrita como "começa no zero", sem o termo.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; C, R e L se falam "cê", "erre" e "éle".
# Visual: plano com C(x) e R(x) cruzando em (100, 5000), faixa vermelha antes (prejuízo) e verde depois (lucro); depois, planos A e B cruzando em (40, 60).

TITULO = "Custo, receita e lucro: o ponto de equilíbrio"

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
    dict(id="s01", block="gancho", text="Uma pequena fábrica vende cada peça por {a}cinquenta reais. [p=0.2] Para fazer cada uma, gasta {b}trinta. [p=0.3] Sobram vinte por peça. [p=0.2] Então, vendendo cinquenta peças no mês, ela lucra mil reais? [p=0.3] {c}Não. [p=0.2] Ela tem prejuízo de mil."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você monta as funções de custo e de receita, acha o ponto de equilíbrio [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de duas coisas: [p=0.2] {a}igualar as contas de dois planos para achar o empate, [p=0.2] e {b}ler numa função afim o valor inicial e a taxa de variação, quanto ela sobe por unidade. [p=0.3] Se faltar alguma, procure no canal."),
    # custo
    dict(id="s04", block="custo", text="O que faltou no gancho? [p=0.2] {a}O aluguel e as máquinas. [p=0.2] A fábrica paga {b}dois mil reais por mês, mesmo sem fazer peça nenhuma. [p=0.3] Esse é o {c}custo fixo."),
    dict(id="s05", block="custo", text="Cada peça gasta mais trinta reais de material: {a}o custo por peça. [p=0.3] Com xis peças no mês, o custo é {b}cê de xis igual a dois mil mais trinta xis. [p=0.2] {c}Valor inicial, dois mil. [p=0.2] E a taxa de variação é {d}trinta: o custo sobe trinta reais a cada peça."),
    # receita
    dict(id="s06", block="receita", text="{a}Receita é o dinheiro que entra com as vendas. [p=0.2] Cada peça vendida rende cinquenta: {b}erre de xis igual a cinquenta xis. [p=0.3] Sem venda, sem receita: {c}o valor inicial é zero."),
    # lucro
    dict(id="s07", block="lucro", text="E o lucro é {a}o que entra menos o que sai: [p=0.2] {b}éle de xis igual a erre de xis menos cê de xis. [p=0.3] Cinquenta xis menos, abre parênteses, dois mil mais trinta xis, fecha parênteses. [p=0.2] O menos troca os sinais de dentro: {c}éle de xis igual a vinte xis menos dois mil."),
    dict(id="s08", block="lucro", text="Com cinquenta peças: {a}vinte vezes cinquenta dá mil. [p=0.2] Menos dois mil, {b}menos mil reais. [p=0.3] Lucro negativo é {c}prejuízo. [p=0.2] É o que aconteceu no gancho."),
    # equilíbrio
    dict(id="s09", block="equilibrio", text="Quando a fábrica para de perder dinheiro? [p=0.2] Quando {a}a receita fica igual ao custo. [p=0.2] É o {b}ponto de equilíbrio, igual ao empate dos dois planos. [p=0.3] {c}Cinquenta xis igual a dois mil mais trinta xis."),
    dict(id="s10", block="equilibrio", text="Tire trinta xis de cada lado: {a}vinte xis igual a dois mil. [p=0.2] Divida por vinte: {b}xis igual a cem peças. [p=0.3] Conferindo: {c}a receita é cinco mil reais. [p=0.2] {d}O custo, dois mil mais três mil, também cinco mil. [p=0.2] Bateu: lucro zero."),
    # gráfico
    dict(id="s11", block="grafico", text="No gráfico, são {a}duas retas. [p=0.2] O custo {b}começa no dois mil. [p=0.2] A receita {c}começa no zero, mas sobe mais rápido. [p=0.3] Elas se cruzam em {d}xis cem, ípsilon cinco mil."),
    dict(id="s12", block="grafico", text="{a}Antes do cruzamento, o custo fica por cima: prejuízo. [p=0.2] {b}Depois, a receita fica por cima: lucro. [p=0.3] A leitura é simples: {c}a reta de cima é a que vale mais naquele xis."),
    # planos
    dict(id="s13", block="planos", text="Com dois planos, a leitura é a mesma. [p=0.2] O plano A, {a}quarenta mais zero vírgula cinco xis, [p=0.2] e o plano B, {b}vinte mais xis, [p=0.2] se cruzam em {c}xis quarenta, ípsilon sessenta. [p=0.3] Aqui você quer pagar menos: {d}compensa a reta de baixo. [p=0.2] Até quarenta minutos, o B. [p=0.2] {e}Depois, o A."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}confundir receita com lucro. [p=0.2] Vendendo cento e vinte peças, a receita é {b}seis mil reais, [p=0.2] e a pessoa diz que lucrou seis mil. [p=0.3] Mas o custo é {c}dois mil mais três mil e seiscentos: cinco mil e seiscentos. [p=0.2] O lucro de verdade é {d}quatrocentos reais."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}custo fixo dividido pelo que sobra em cada peça. [p=0.2] Sobram {b}cinquenta menos trinta: vinte reais. [p=0.2] {c}Dois mil dividido por vinte dá cem peças."),
    dict(id="s16", block="atalho", text="Funciona porque cada peça vendida {a}paga vinte reais do custo fixo. [p=0.2] Com cem peças, os dois mil estão pagos. [p=0.3] Não compensa quando {b}o preço ou o custo mudam com a quantidade, como num desconto para quem compra muito. [p=0.2] Aí, monte as funções e iguale."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar, com valores inventados. [p=0.2] Uma doceira tem {a}custo fixo de novecentos reais por mês [p=0.1] e gasta {b}quatro reais em cada bolo. [p=0.2] Ela vende cada bolo por {c}dez reais. [p=0.3] {d}Qual é o ponto de equilíbrio? [p=0.2] E quantos bolos ela precisa vender para lucrar seiscentos reais?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Custo: {a}novecentos mais quatro xis. [p=0.2] Receita: {b}dez xis. [p=0.2] Lucro: {c}seis xis menos novecentos. [p=0.3] Pelo atalho, sobram seis reais por bolo, e {d}novecentos dividido por seis dá cento e cinquenta bolos."),
    dict(id="s20", block="resposta", text="Para lucrar seiscentos: {a}seis xis menos novecentos igual a seiscentos. [p=0.2] Some novecentos dos dois lados: {b}seis xis igual a mil e quinhentos. [p=0.2] {c}Xis igual a duzentos e cinquenta bolos. [p=0.3] Conferindo: receita, dois mil e quinhentos. [p=0.2] Custo, novecentos mais mil: mil e novecentos. [p=0.2] {d}Sobram seiscentos. Bateu."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}lucro é receita menos custo, [p=0.2] e {b}o equilíbrio é onde as retas se cruzam."),
    dict(id="s22", block="fim", text="Na próxima aula, você pratica tudo da função afim: [p=0.2] {a}montar a lei, ler os coeficientes e comparar duas retas no gráfico. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
