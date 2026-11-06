# Estudativo · MAT-NUM-010 — Dividir por dois algarismos (Matemática · Números e Contas).
# Habilidade: calcular 1.035 ÷ 23 estimando cada algarismo do resultado.
# Pré-requisitos: MAT-NUM-008 (multiplicar por dois algarismos), MAT-NUM-009 (dividir por um algarismo). Próxima: MAT-NUM-011.
# Questão inédita, criada para esta aula. Conta na forma curta da chave, a mesma de MAT-FRA-017 e MAT-FRA-018; os testes do palpite ficam ao lado da conta, nunca sob o dividendo.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Dividir por dois algarismos"

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
    dict(id="s01", block="gancho", text="{a}Mil e trinta e cinco reais para {b}vinte e três pessoas. [p=0.3] Ninguém decorou a tabuada do vinte e três. [p=0.3] E você não precisa dela: [p=0.2] basta {c}um bom palpite e uma conferida."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai dividir por dois algarismos, [p=0.2] um palpite de cada vez, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}duas coisas: [p=0.2] {b}dividir por um algarismo, com resto, [p=0.2] e {c}multiplicar por dois algarismos. [p=0.3] Se faltar alguma, procure no canal."),
    # estimar
    dict(id="s04", block="estimar", text="O segredo é {a}estimar: [p=0.2] calcular por cima, como quem olha o carrinho do mercado e diz: [p=0.2] deve dar uns cem reais. [p=0.3] Aqui, {b}o vinte e três fica perto de vinte. [p=0.2] Use o número redondo só para pensar. [p=0.2] A conta continua com vinte e três."),
    # exemplo, palpite alto
    dict(id="s05", block="conta", text="{a}Arme a chave. [p=0.2] Pegue o primeiro pedaço do dividendo em que o divisor caiba. [p=0.2] {b}Um não dá. [p=0.2] {c}Dez não dá. [p=0.2] {d}Cento e três dá."),
    dict(id="s06", block="conta", text="Quantas vezes o vinte e três cabe aí? [p=0.3] Pense em notas de dez. [p=0.2] {a}Cento e três reais são dez notas e um troco. [p=0.2] {b}Vinte reais são duas notas. [p=0.2] {c}Dez dividido por dois dá cinco. [p=0.3] Na prática, {d}com o divisor já arredondado, cubra o último algarismo de cada número. [p=0.2] Esse cinco é o {e}palpite."),
    dict(id="s07", block="conta", text="Palpite se confere. [p=0.2] {a}Vinte e três vezes cinco dá cento e quinze. [p=0.3] {b}Passou de cento e três. [p=0.2] Palpite alto: {c}baixe um. [p=0.2] {d}Vinte e três vezes quatro dá noventa e dois. [p=0.3] Cabe. [p=0.2] {e}Quatro no quociente, [p=0.2] e de noventa e dois para cento e três {f}sobram onze."),
    dict(id="s08", block="conta", text="{a}Desça o cinco: cento e quinze. [p=0.3] Cubra de novo: {b}onze dividido por dois dá cinco. [p=0.2] Essa você já conferiu: {c}vinte e três vezes cinco dá cento e quinze. [p=0.2] {d}Cinco no quociente, [p=0.2] e {e}sobra zero."),
    dict(id="s09", block="conta", text="Resultado: {a}quarenta e cinco reais para cada pessoa. [p=0.3] Prova real: {b}vinte e três vezes quarenta e cinco dá mil e trinta e cinco. [p=0.2] Fecha."),
    # erro: palpite baixo
    dict(id="s10", block="erro", text="O palpite também pode vir baixo, e aí mora o erro comum. [p=0.2] {a}Setecentos e cinquenta e seis dividido por vinte e oito. [p=0.2] O primeiro pedaço é setenta e cinco. [p=0.2] Vinte e oito fica perto de {b}trinta. [p=0.3] Cubra o último algarismo de setenta e cinco e de trinta: {c}sete dividido por três dá dois. [p=0.2] {d}Vinte e oito vezes dois dá cinquenta e seis, [p=0.2] e {e}sobram dezenove."),
    dict(id="s11", block="erro", text="{a}Desça o seis: cento e noventa e seis. [p=0.2] {b}Dezenove dividido por três dá seis. [p=0.2] {c}Vinte e oito vezes seis dá cento e sessenta e oito. [p=0.2] De cento e sessenta e oito para cento e noventa e seis, {d}sobram vinte e oito."),
    dict(id="s12", block="erro", text="O erro é parar aí: {a}vinte e seis, com resto vinte e oito. [p=0.3] Mas {b}o resto é igual ao divisor, [p=0.2] e resto tem que ser menor. [p=0.2] Ainda cabe mais um vinte e oito. [p=0.2] Palpite baixo: {c}suba um. [p=0.2] {d}Sete no quociente, [p=0.2] {e}sobra zero, [p=0.2] e o resultado é {f}vinte e sete."),
    dict(id="s13", block="erro", text="As regras cabem em uma linha: [p=0.2] {a}passou do número, baixe um. [p=0.2] {b}Resto igual ou maior que o divisor, suba um. [p=0.2] E confira de novo. [p=0.3] Cada palpite é um algarismo só: [p=0.2] {c}se der mais que nove, comece do nove."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}saber o tamanho do resultado antes de dividir. [p=0.3] {b}Vinte e três vezes dez dá duzentos e trinta. [p=0.2] {c}Vezes cem dá dois mil e trezentos. [p=0.3] {d}Mil e trinta e cinco fica entre esses valores, [p=0.2] então o vinte e três cabe {e}mais de dez vezes e menos de cem: [p=0.2] o resultado tem dois algarismos."),
    dict(id="s15", block="atalho", text="Funciona porque {a}vezes dez e vezes cem saem de cabeça [p=0.2] e marcam os limites do resultado. [p=0.3] Em prova, isso {b}elimina as alternativas de tamanho errado. [p=0.2] {c}Não compensa quando todas têm o mesmo tamanho: [p=0.2] aí, arme a conta."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Um sítio colheu {a}mil e quatrocentas laranjas [p=0.2] e coloca {b}vinte e seis em cada caixa. [p=0.3] {c}Quantas caixas cheias ele fecha, e quantas laranjas sobram?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] O primeiro pedaço é {a}cento e quarenta. [p=0.2] Vinte e seis fica perto de {b}trinta. [p=0.2] {c}Catorze dividido por três dá quatro. [p=0.2] {d}Vinte e seis vezes quatro dá cento e quatro, [p=0.2] e {e}sobram trinta e seis. [p=0.3] Resto maior que o divisor: {f}suba um. [p=0.2] {g}Vinte e seis vezes cinco dá cento e trinta, [p=0.2] e {h}sobram dez."),
    dict(id="s19", block="resposta", text="{a}Desça o zero: cem. [p=0.2] {b}Dez dividido por três dá três. [p=0.2] {c}Vinte e seis vezes três dá setenta e oito, [p=0.2] e {d}sobram vinte e dois. [p=0.3] São {e}cinquenta e três caixas cheias, [p=0.2] e {f}sobram vinte e duas laranjas."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}arredonde o divisor, [p=0.2] {b}dê o palpite [p=0.2] e {c}confira multiplicando."),
    dict(id="s21", block="fim", text="Você já sabe fazer as quatro contas. [p=0.2] Falta saber qual delas usar. [p=0.3] Na próxima aula, você vai {a}escolher a conta certa pelas palavras do problema. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
