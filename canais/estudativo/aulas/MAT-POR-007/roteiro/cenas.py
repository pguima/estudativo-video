# Estudativo · MAT-POR-007 — Lucro sobre o custo e sobre a venda (Matemática · Porcentagem).
# Habilidade: dizer que R$ 20 de lucro são 25% sobre R$ 80 de custo e 20% sobre R$ 100 de venda e achar o preço com 30% de margem.
# Pré-requisitos: MAT-POR-003 (quantos por cento e total), MAT-POR-006 (preço antes), MAT-FRA-015 (subtrair decimais), MAT-NUM-011 (qual conta). Próxima: MAT-POR-008.
# Questão inédita, criada para esta aula. Margem trabalhada nos dois sentidos: sobre o custo (fator) e sobre a venda (dividir).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Lucro sobre o custo e sobre a venda"

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
    dict(id="s01", block="gancho", text="Você comprou um produto por {a}oitenta reais e vendeu por {b}cem. [p=0.3] Lucro de {c}vinte reais. [p=0.2] Mas quantos por cento? [p=0.3] Uma pessoa diz {d}vinte e cinco. [p=0.2] Outra diz {e}vinte. [p=0.3] E ninguém errou."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai saber de onde sai cada número, [p=0.2] calcular o preço que dá o lucro que você quer [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas. [p=0.2] {b}Achar quantos por cento, dividindo a parte pelo total. [p=0.2] E {c}achar o preço de antes, dividindo pelo fator. [p=0.3] Se faltar alguma, procure no canal."),
    # nomes
    dict(id="s04", block="nomes", text="Primeiro, três nomes. [p=0.2] {a}Custo é quanto você pagou. [p=0.2] {b}Venda é quanto você recebeu. [p=0.2] E {c}lucro é a diferença: venda menos custo. [p=0.3] {d}Cem menos oitenta dá vinte reais."),
    # sobre o custo e sobre a venda
    dict(id="s05", block="sobre", text="O lucro é a parte. [p=0.2] A dúvida é {a}qual é o total. [p=0.3] Se o total é o custo, divida {b}vinte por oitenta: zero vírgula vinte e cinco. [p=0.2] São {c}vinte e cinco por cento sobre o custo."),
    dict(id="s06", block="sobre", text="Se o total é a venda, divida {a}vinte por cem: zero vírgula vinte. [p=0.2] São {b}vinte por cento sobre a venda. [p=0.3] Então procure no enunciado {c}a palavra que vem depois de sobre: [p=0.2] ela diz quem vai embaixo na divisão."),
    dict(id="s07", block="sobre", text="Repare que {a}o lucro sobre o custo dá mais, [p=0.2] porque o custo é o número menor. [p=0.3] E quando a venda fica {b}abaixo do custo, a diferença se chama {c}prejuízo. [p=0.2] A conta é a mesma: [p=0.2] {d}comprou por oitenta, vendeu por sessenta, prejuízo de vinte, vinte e cinco por cento sobre o custo."),
    # preço com margem
    dict(id="s08", block="margem", text="E o caminho inverso? [p=0.2] Uma peça custa {a}setenta reais [p=0.2] e você quer {b}margem de lucro de trinta por cento. [p=0.2] Margem de lucro é {c}o lucro contado em por cento. [p=0.3] {d}Por quanto vender?"),
    dict(id="s09", block="margem", text="Se for {a}sobre o custo, é um aumento de trinta por cento no custo: [p=0.2] {b}fator um vírgula três. [p=0.2] {c}Setenta vezes um vírgula três dá noventa e um reais."),
    dict(id="s10", block="margem", text="Se for {a}sobre a venda, o lucro é trinta por cento do preço de venda. [p=0.2] Então o custo é o resto: {b}setenta por cento da venda. [p=0.3] Você tem a parte e quer o total: [p=0.2] {c}setenta dividido por zero vírgula sete. [p=0.2] {d}Setecentos dividido por sete dá cem reais."),
    dict(id="s11", block="margem", text="Confira: {a}lucro de trinta reais, [p=0.2] e {b}trinta é trinta por cento de cem. [p=0.2] Bateu. [p=0.3] A mesma {c}margem de trinta por cento deu noventa e um ou cem reais. [p=0.2] Na prova, {d}procure se é sobre o custo ou sobre a venda. [p=0.2] Se o texto não disser, {e}o mais comum nos problemas é sobre o custo, [p=0.2] mas não é regra: leia o enunciado inteiro."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é usar o fator de aumento {a}quando o problema pede sobre a venda. [p=0.2] A pessoa vende a peça por {b}noventa e um reais. [p=0.2] O lucro, vinte e um, é só {c}cerca de vinte e três por cento da venda. [p=0.3] {d}Não chega aos trinta."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}pense em partes. [p=0.2] Lucro de vinte com custo de oitenta é {b}um quarto do custo. [p=0.3] Então o custo tem {c}quatro partes, o lucro {d}uma, [p=0.2] e a venda, {e}cinco."),
    dict(id="s14", block="atalho", text="Sobre o custo: {a}uma parte de quatro, vinte e cinco por cento. [p=0.2] Sobre a venda: {b}uma parte de cinco, vinte por cento. [p=0.3] Funciona porque {c}o lucro é o mesmo, só muda o total. [p=0.2] Não compensa quando a porcentagem {d}não vira fração simples, como vinte e três por cento: [p=0.2] aí, {e}divida."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma loja compra um tênis por {a}cento e vinte reais [p=0.2] e quer lucro de {b}quarenta por cento sobre o preço de venda. [p=0.3] {c}Por quanto deve vender?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] O lucro é quarenta por cento da venda, então {a}o custo é sessenta por cento da venda. [p=0.2] {b}Cento e vinte dividido por zero vírgula seis. [p=0.2] {c}Mil e duzentos dividido por seis dá duzentos reais."),
    dict(id="s18", block="resposta", text="Confira: {a}lucro de oitenta reais, [p=0.2] e {b}quarenta por cento de duzentos é oitenta. [p=0.2] Bateu. [p=0.3] Quem usou o fator de aumento achou {c}cento e sessenta e oito, e errou."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}lucro é venda menos custo, [p=0.2] e {b}a porcentagem depende de quem vai embaixo: o custo ou a venda."),
    dict(id="s20", block="fim", text="Na próxima aula, você descobre {a}quanto de desconto existe de verdade no leve três, pague dois. [p=0.2] {b}E não é cinquenta por cento. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
