# Estudativo · MAT-FIN-004 — Juros compostos: mês a mês e a fórmula (Matemática · Matemática Financeira).
# Habilidade: acompanhar R$ 1.000 a 10% em 1.100, 1.210 e 1.331 e calcular M = 1.000 · 1,02⁶ com a tabela do enunciado.
# Pré-requisitos: MAT-FIN-001 (juros simples), MAT-POR-010 (aumentos sucessivos), MAT-POT-002 (potência de decimal). Próxima: MAT-FIN-005.
# Questão inédita, criada para esta aula. Tabelas de potência como as que a prova costuma dar (valores arredondados a 4 casas).
# Fator como em MAT-POR-004: cem mais a taxa, passado para decimal.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Juros compostos: mês a mês e a fórmula"

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
    dict(id="s01", block="gancho", text="{a}Mil reais, a {b}dez por cento ao mês, por três meses. [p=0.3] Em juros simples, viram {c}mil e trezentos. [p=0.3] Em juros compostos, viram {d}mil trezentos e trinta e um. [p=0.3] De onde saíram esses trinta e um reais?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular juros compostos mês a mês e pela fórmula, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}juros simples, [p=0.2] {c}multiplicar os fatores em aumentos seguidos [p=0.2] e {d}calcular potência de decimal, como zero vírgula três ao quadrado. [p=0.3] Se faltar alguma, procure no canal."),
    # mês a mês
    dict(id="s04", block="mes", text="Nos juros compostos, {a}os juros de cada mês entram na conta do mês seguinte. [p=0.2] É o famoso {b}juro sobre juro. [p=0.3] São os juros mais usados por bancos, em aplicações e em dívidas."),
    dict(id="s05", block="mes", text="{a}Primeiro mês: dez por cento de mil dá cem. [p=0.2] Montante: {b}mil e cem. [p=0.3] {c}Segundo mês: os dez por cento valem sobre mil e cem. [p=0.2] São cento e dez de juros. [p=0.2] Montante: {d}mil duzentos e dez."),
    dict(id="s06", block="mes", text="{a}Terceiro mês: dez por cento de mil duzentos e dez dá cento e vinte e um. [p=0.2] Montante: {b}mil trezentos e trinta e um. [p=0.3] Nos simples, os juros seriam cem todo mês. [p=0.2] Aqui, {c}os juros crescem. [p=0.2] Cem. [p=0.2] Depois cento e dez. [p=0.2] Depois cento e vinte e um."),
    # fator
    dict(id="s07", block="fator", text="Com fatores, sai mais rápido. [p=0.2] Somar dez por cento é {a}multiplicar por um vírgula um: [p=0.1] cem mais a taxa, cento e dez por cento. [p=0.3] Três meses são {b}três aumentos seguidos de dez por cento. [p=0.2] E aumentos seguidos se juntam {c}multiplicando os fatores."),
    dict(id="s08", block="fator", text="{a}Mil vezes um vírgula um, vezes um vírgula um, vezes um vírgula um. [p=0.3] O mesmo número multiplicado várias vezes é {b}uma potência: um vírgula um ao cubo. [p=0.2] {c}Um vírgula um ao cubo dá um vírgula trezentos e trinta e um. [p=0.2] {d}Vezes mil dá mil trezentos e trinta e um."),
    # fórmula
    dict(id="s09", block="formula", text="Daí sai a fórmula: {a}eme igual a cê vezes o fator elevado a tê. [p=0.3] {b}Eme é o montante. [p=0.1] {c}Cê é o capital. [p=0.1] {d}Tê é o número de períodos. [p=0.3] E o fator é {e}um mais i: [p=0.1] o mesmo cem mais a taxa, escrito em decimal. [p=0.3] Atenção à ordem: só o fator é elevado a tê. [p=0.2] Depois, o resultado multiplica o capital."),
    dict(id="s10", block="formula", text="Em prova, a potência costuma ser difícil, e o enunciado {a}dá uma tabela. [p=0.3] Mil reais a {b}dois por cento ao mês, por {c}seis meses. [p=0.2] Fator: cem mais dois dá cento e dois por cento: {d}um vírgula zero dois. [p=0.2] Montante: {e}mil vezes um vírgula zero dois elevado a seis."),
    dict(id="s11", block="formula", text="Ninguém faz essa potência à mão. [p=0.2] {a}A tabela diz: um vírgula zero dois elevado a seis vale cerca de um vírgula um dois seis dois. [p=0.3] {b}Vezes mil, a vírgula anda três casas. [p=0.2] {c}Cerca de mil cento e vinte e seis reais e vinte centavos."),
    # erro
    dict(id="s12", block="erro", text="O erro comum aqui é {a}multiplicar o fator pelo tempo. [p=0.2] {b}Um vírgula zero dois vezes seis dá seis vírgula um dois. [p=0.2] Montante de {c}seis mil cento e vinte reais, [p=0.1] em seis meses, a dois por cento. [p=0.3] Absurdo. [p=0.2] O tempo é {d}o expoente: quantas vezes o fator se repete."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, para a taxa de dez por cento: [p=0.2] {a}multiplicar por um vírgula um é somar a décima parte. [p=0.3] {b}Mil e cem, mais cento e dez, dá mil duzentos e dez. [p=0.2] {c}Somando cento e vinte e um, mil trezentos e trinta e um."),
    dict(id="s14", block="atalho", text="Funciona porque {a}um vírgula um é o inteiro mais um décimo. [p=0.3] Não compensa com taxa quebrada ou muitos meses, [p=0.1] como {b}dois por cento por seis meses. [p=0.2] Aí, {c}use a tabela."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Quatro mil reais ficam aplicados a {b}três por cento ao mês, em juros compostos, [p=0.1] uma taxa alta, só de exemplo, [p=0.1] por {c}quatro meses. [p=0.3] A tabela dá: {d}um vírgula zero três elevado a quatro, cerca de um vírgula um dois cinco cinco. [p=0.3] {e}Qual é o montante? E quanto foi de juros?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Fator: cem mais três dá cento e três por cento, {a}um vírgula zero três. [p=0.2] Montante: {b}quatro mil vezes um vírgula zero três elevado a quatro. [p=0.3] Pela tabela, {c}quatro mil vezes um vírgula um dois cinco cinco. [p=0.2] Vezes mil dá mil cento e vinte e cinco e meio. [p=0.2] {d}Vezes quatro dá quatro mil quinhentos e dois reais."),
    dict(id="s18", block="resposta", text="Os juros são o montante menos o capital: [p=0.2] {a}quatro mil quinhentos e dois menos quatro mil dá [p=0.1] {b}quinhentos e dois reais. [p=0.3] Nos simples, seriam {c}quatrocentos e oitenta. [p=0.2] O juro sobre juro rendeu {d}vinte e dois a mais."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}nos compostos, os juros rendem sobre o montante. [p=0.2] {b}Eleve o fator ao número de períodos [p=0.1] {c}e multiplique pelo capital."),
    dict(id="s20", block="fim", text="Então os compostos sempre rendem mais? [p=0.2] Na próxima aula, você descobre {a}quem ganha em um mês, em menos de um mês e em dois anos. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
