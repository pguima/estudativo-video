# Estudativo · MAT-POR-008 — Promoções: leve 3, pague 2 (Matemática · Porcentagem).
# Habilidade: dizer que leve 3, pague 2 equivale a cerca de 33% de desconto.
# Pré-requisitos: MAT-POR-003 (quantos por cento), MAT-FRA-020 (dízimas). Próxima: MAT-POR-009.
# Questão inédita, criada para esta aula. Sem fatores e sem subtrair decimais: esta cadeia não tem MAT-POR-004 nem MAT-FRA-015.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Promoções: leve 3, pague 2"

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
    dict(id="s01", block="gancho", text="Uma loja anuncia {a}leve três, pague dois. [p=0.2] A loja do lado dá {b}trinta por cento de desconto em tudo. [p=0.3] Você precisa de três pacotes. [p=0.2] {c}Qual sai mais barato?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai transformar qualquer promoção de leve e pague em porcentagem de desconto, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas. [p=0.2] {b}Achar quantos por cento, dividindo a parte pelo total. [p=0.2] E {c}reconhecer uma dízima, o decimal que se repete sem fim. [p=0.3] Se faltar alguma, procure no canal."),
    # com preço
    dict(id="s04", block="preco", text="Vamos com preço. [p=0.2] Cada pacote custa {a}seis reais. [p=0.2] Três pacotes, sem promoção: {b}dezoito reais. [p=0.2] Com a promoção, você paga só dois pacotes: {c}doze reais."),
    dict(id="s05", block="preco", text="Você economizou {a}seis reais. [p=0.3] Quantos por cento? [p=0.2] A economia é a parte. [p=0.2] O total é {b}o preço cheio de tudo o que você levou: dezoito. [p=0.3] {c}Seis dividido por dezoito: um terço. [p=0.3] Como em qualquer desconto, {d}a economia vai sobre o preço cheio."),
    dict(id="s06", block="preco", text="Um terço em decimal: {a}um dividido por três dá zero vírgula três, três, três... [p=0.2] uma {b}dízima de período três. [p=0.3] Em porcentagem, {c}trinta e três vírgula três, três, três por cento. [p=0.2] Ou seja, {d}cerca de trinta e três por cento de desconto."),
    # sem preço
    dict(id="s07", block="regra", text="Repare que o preço do pacote {a}não importou. [p=0.2] De cada três pacotes, {b}um saiu de graça. [p=0.3] {c}Um de três: um terço, cerca de trinta e três por cento."),
    dict(id="s08", block="regra", text="A regra: {a}o desconto é o que sai de graça dividido pelo que você leva. [p=0.3] {b}Leve quatro, pague três: [p=0.1] um de graça em quatro, um quarto, {c}vinte e cinco por cento."),
    dict(id="s09", block="regra", text="E a famosa {a}segunda unidade pela metade do preço? [p=0.2] Você leva duas unidades, e sai de graça {b}meia unidade. [p=0.2] {c}Zero vírgula cinco dividido por dois: zero vírgula vinte e cinco, vinte e cinco por cento. [p=0.3] Parece muito, mas {d}empata com o leve quatro, pague três."),
    dict(id="s10", block="regra", text="Voltando ao começo: {a}cerca de trinta e três por cento contra {b}trinta. [p=0.2] Para quem precisa de três pacotes, {c}o leve três, pague dois ganha, por pouco."),
    # erro
    dict(id="s11", block="erro", text="O erro comum é dividir {a}pelo que você paga. [p=0.2] Um de graça para dois pagos dá {b}um meio: cinquenta por cento. [p=0.3] Mas cinquenta por cento de desconto seria pagar {c}nove reais pelos três pacotes, [p=0.2] e você pagou doze. [p=0.2] O total é sempre {d}tudo o que você leva."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: {a}guarde três frações. [p=0.2] {b}Um terço, cerca de trinta e três por cento. [p=0.2] {c}Um quarto, vinte e cinco. [p=0.2] {d}Um quinto, vinte. [p=0.3] Leve cinco, pague quatro? [p=0.2] {e}Um de graça em cinco: vinte por cento, na hora."),
    dict(id="s13", block="atalho", text="Funciona porque {a}a fração que sai de graça já é o desconto: [p=0.2] só falta passar para porcentagem. [p=0.3] Não compensa quando os produtos {b}têm preços diferentes, [p=0.2] porque em geral o de graça é o mais barato. [p=0.2] Aí, {c}faça a conta com os preços: a economia dividida pelo preço cheio."),
    dict(id="s14", block="atalho", text="Por exemplo: leve três, pague dois, com produtos de {a}dez, dez e quatro reais. [p=0.2] O de quatro sai de graça. [p=0.2] Preço cheio, {b}vinte e quatro reais. [p=0.2] {c}Quatro dividido por vinte e quatro: um sexto, [p=0.1] {d}cerca de dezessete por cento. [p=0.2] Bem longe dos trinta e três."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Você precisa de {a}quatro caixas de leite. [p=0.2] Um mercado faz {b}leve quatro, pague três. [p=0.2] Outro dá {c}trinta por cento de desconto. [p=0.3] {d}Qual você escolhe?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Leve quatro, pague três: {a}uma caixa de graça em quatro, um quarto, vinte e cinco por cento. [p=0.3] {b}Vinte e cinco é menos que trinta. [p=0.2] Desta vez, {c}o desconto de trinta por cento ganha."),
    dict(id="s18", block="resposta", text="Confira com um preço: caixa de {a}cinco reais. [p=0.2] Quatro caixas, {b}vinte reais. [p=0.2] No primeiro mercado, você paga três caixas: {c}quinze reais. [p=0.2] No segundo, tira trinta por cento de vinte, que é seis: {d}catorze reais."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}o que sai de graça, dividido pelo que você leva. [p=0.2] {b}Leve três, pague dois: cerca de trinta e três por cento."),
    dict(id="s20", block="fim", text="Na próxima aula, você {a}pratica tudo de porcentagem até aqui: [p=0.2] {b}descontos, aumentos, preço de antes e lucro, [p=0.2] em problemas de compra e venda. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
