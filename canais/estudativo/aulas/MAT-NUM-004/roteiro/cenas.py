# Estudativo · MAT-NUM-004 — Subtrair de cabeça e com a conta armada (Matemática · Números e Contas).
# Habilidade: conferir 13 − 5 com uma soma e calcular 503 − 178 pedindo emprestado, inclusive por cima do zero.
# Pré-requisitos: MAT-NUM-003. Próxima: MAT-NUM-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Contas: 13 − 5 = 8 (8 + 5 = 13) · 52 − 27 = 25 · 503 = 400 + 90 + 13 · 503 − 178 = 325 (325 + 178 = 503) · invertendo as casas dá 475 (475 + 178 = 653) · 403 − 198 = 405 − 200 = 205.
# Questão: 705 − 268 = 437 (437 + 268 = 705); invertendo as casas daria 563.

TITULO = "Subtrair de cabeça e com a conta armada"

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
    dict(id="s01", block="gancho", text="{a}Quinhentos e três menos cento e setenta e oito. [p=0.3] Se deu {b}quatrocentos e setenta e cinco, [p=0.2] {c}você caiu no erro mais comum da subtração."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você subtrai até com zero no caminho, [p=0.2] confere o resultado {b}com uma soma [p=0.2] e ainda leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}uma coisa: [p=0.2] {b}somar com a conta armada. [p=0.3] Lá, dez moedas viravam uma nota de dez. [p=0.2] {c}Hoje, a troca é ao contrário. [p=0.3] Se faltar, procure a aula no canal."),
    # de cabeça
    dict(id="s04", block="cabeca", text="Subtrair é {a}tirar. [p=0.2] Você tem {b}treze reais e gasta {c}cinco. [p=0.3] Quanto sobra? [p=0.2] Use o dez de novo: [p=0.2] {d}cinco é três mais dois. [p=0.2] {e}Treze menos três dá dez. [p=0.2] {f}Dez menos dois dá oito."),
    dict(id="s05", block="cabeca", text="Como saber se está certo? [p=0.2] {a}Some o que sobrou com o que você tirou. [p=0.3] {b}Oito mais cinco dá treze: [p=0.2] voltou ao começo, {c}está certo. [p=0.3] Faz sentido: [p=0.2] o que sobrou mais o que saiu é tudo o que você tinha."),
    # pedir emprestado
    dict(id="s06", block="emprestar", text="Na conta armada, vale o mesmo da soma: [p=0.2] {a}casa embaixo de casa, {b}da direita para a esquerda. [p=0.3] Veja {c}cinquenta e dois menos vinte e sete. [p=0.2] Nas unidades, {d}dois menos sete. [p=0.2] Com duas moedas, não dá para tirar sete."),
    dict(id="s07", block="emprestar", text="Então você {a}pede emprestado ao vizinho, [p=0.2] a casa das dezenas. [p=0.3] Ele entrega {b}uma nota de dez, [p=0.2] que vira dez moedas: [p=0.2] {c}o cinco vira quatro [p=0.2] e {d}o dois vira doze. [p=0.3] O dinheiro é o mesmo. [p=0.2] Só mudou de forma. [p=0.3] A casa passa de nove só por um instante, para fazer a conta."),
    dict(id="s08", block="emprestar", text="{a}Doze menos sete dá cinco. [p=0.2] {b}Quatro menos dois dá dois. [p=0.3] Resultado: {c}vinte e cinco."),
    # por cima do zero
    dict(id="s09", block="zero", text="E quando o vizinho não tem nada? [p=0.2] Volte para {a}quinhentos e três menos cento e setenta e oito. [p=0.3] {b}Três menos oito não dá. [p=0.2] E o vizinho é {c}zero: [p=0.2] não tem nota de dez para emprestar."),
    dict(id="s10", block="zero", text="Então {a}o empréstimo vem lá do cinco, por cima do zero. [p=0.3] Uma nota de cem é trocada por dez notas de dez: [p=0.2] {b}o cinco vira quatro [p=0.2] e {c}o zero vira dez. [p=0.3] Agora o vizinho tem o que emprestar: [p=0.2] {d}o dez vira nove [p=0.2] e {e}o três vira treze."),
    dict(id="s11", block="zero", text="Confira o dinheiro: [p=0.2] {a}quatro notas de cem. [p=0.2] {b}Nove notas de dez. [p=0.2] {c}Treze moedas. [p=0.3] Continua sendo quinhentos e três."),
    dict(id="s12", block="zero", text="{a}Treze menos oito dá cinco. [p=0.2] {b}Nove menos sete dá dois. [p=0.2] {c}Quatro menos um dá três. [p=0.3] Resultado: {d}trezentos e vinte e cinco."),
    dict(id="s13", block="zero", text="Confira com uma soma: [p=0.2] {a}trezentos e vinte e cinco mais cento e setenta e oito [p=0.2] tem que dar {b}quinhentos e três. [p=0.2] E dá."),
    # erro
    dict(id="s14", block="erro", text="De onde veio aquele quatrocentos e setenta e cinco? [p=0.2] A pessoa vê três menos oito e {a}inverte: [p=0.2] faz {b}oito menos três. [p=0.2] Na casa seguinte, faz sete menos zero. [p=0.3] Mas o número que sai é sempre o de baixo. [p=0.3] A soma denuncia: [p=0.2] {c}quatrocentos e setenta e cinco mais cento e setenta e oito [p=0.2] dá {d}seiscentos e cinquenta e três. [p=0.2] {e}Não voltou ao começo."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}deixe redondo o número de baixo. [p=0.2] Veja {b}quatrocentos e três menos cento e noventa e oito. [p=0.3] Some {c}o mesmo tanto em cima e embaixo: [p=0.2] dois em cada um. [p=0.2] Fica {d}quatrocentos e cinco menos duzentos, [p=0.2] que dá {e}duzentos e cinco."),
    dict(id="s16", block="atalho", text="Funciona porque {a}a distância entre os números não muda. [p=0.3] Pense em idade: [p=0.2] {b}a diferença de idade entre duas pessoas é a mesma hoje e daqui a dois anos. [p=0.3] {c}Não compensa se o número de baixo está longe de um redondo. [p=0.2] Aí, {d}arme a conta."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Sua conta no banco tinha {a}setecentos e cinco reais. [p=0.2] Você pagou um boleto de {b}duzentos e sessenta e oito reais. [p=0.3] {c}Quanto sobrou na conta?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Cinco menos oito não dá, [p=0.2] e o vizinho é zero. [p=0.3] {b}O sete vira seis, [p=0.2] {c}o zero vira dez, [p=0.2] {d}o dez vira nove [p=0.2] e {e}o cinco vira quinze."),
    dict(id="s20", block="resposta", text="{a}Quinze menos oito dá sete. [p=0.2] {b}Nove menos seis dá três. [p=0.2] {c}Seis menos dois dá quatro. [p=0.3] Sobraram {d}quatrocentos e trinta e sete reais. [p=0.3] Confira: {e}quatrocentos e trinta e sete mais duzentos e sessenta e oito [p=0.2] dá {f}setecentos e cinco."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}faltou, peça ao vizinho. [p=0.2] {b}Vizinho zero, o empréstimo vem de mais longe. [p=0.2] {c}No fim, confira com uma soma."),
    dict(id="s22", block="fim", text="Na próxima aula, a multiplicação: [p=0.2] {a}vezes como soma repetida [p=0.2] e {b}macetes para as tabuadas do dois, do cinco, do nove e do dez. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
