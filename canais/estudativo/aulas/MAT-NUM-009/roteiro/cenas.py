# Estudativo · MAT-NUM-009 — Dividir por um algarismo, com e sem resto (Matemática · Números e Contas).
# Habilidade: dizer que 17 ÷ 5 dá 3 com resto 2, tirar a prova real e calcular 612 ÷ 3 sem esquecer o zero em 204.
# Pré-requisitos: MAT-NUM-004 (subtrair), MAT-NUM-006 (tabuada), MAT-NUM-007 (multiplicar por um algarismo). Próxima: MAT-NUM-010.
# Questão inédita, criada para esta aula. Conta na forma curta da chave, a mesma de MAT-FRA-017: sob o dividendo só o resto com o algarismo que desce.
# Sem multiplicar por dois algarismos: MAT-NUM-008 não está na ficha desta aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Dividir por um algarismo, com e sem resto"

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
    dict(id="s01", block="gancho", text="{a}Seiscentos e doze reais para {b}três pessoas. [p=0.3] Se deu {c}vinte e quatro reais para cada uma, [p=0.2] sumiu dinheiro: [p=0.2] {d}três vezes vinte e quatro dá só setenta e dois. [p=0.3] Faltou {e}um zero no resultado."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai dividir com e sem resto, [p=0.2] tirar a prova real [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}três coisas: [p=0.2] {b}a tabuada, [p=0.2] {c}subtrair [p=0.2] e {d}multiplicar por um algarismo. [p=0.3] Se faltar alguma, procure no canal."),
    # nomes e resto
    dict(id="s04", block="nomes", text="Dividir é repartir em partes iguais, ou ver quantas vezes um número cabe no outro. [p=0.2] Você tem {a}dezessete garrafas [p=0.2] e {b}caixas que levam cinco. [p=0.3] Fecham {c}três caixas, com quinze garrafas, [p=0.2] e {d}sobram duas."),
    dict(id="s05", block="nomes", text="Cada número tem um nome. [p=0.2] {a}Dividendo é o que vai ser dividido: dezessete. [p=0.2] {b}Divisor é o que divide: cinco. [p=0.2] {c}Quociente é o resultado: três. [p=0.2] {d}Resto é o que sobra: dois. [p=0.3] {e}Dezessete dividido por cinco dá três, com resto dois."),
    dict(id="s06", block="nomes", text="O resto tem uma regra: [p=0.2] {a}ele é sempre menor que o divisor. [p=0.2] Se sobrassem cinco garrafas, {b}daria para fechar mais uma caixa."),
    # prova real
    dict(id="s07", block="prova", text="Para conferir, existe a {a}prova real: [p=0.2] {b}quociente vezes divisor, mais o resto, [p=0.2] tem que dar o dividendo. [p=0.3] {c}Três caixas de cinco são quinze garrafas. [p=0.2] {d}Com as garrafas soltas, dezessete. [p=0.3] Fecha, porque você só juntou tudo de novo."),
    # conta na chave
    dict(id="s08", block="chave", text="Com número maior, usamos {a}a conta na chave, esse canto desenhado aqui. [p=0.3] {b}O dividendo fica à esquerda, [p=0.2] {c}o divisor dentro da chave [p=0.2] e {d}o quociente embaixo dele."),
    dict(id="s09", block="chave", text="{a}Setenta e oito reais para três pessoas. [p=0.3] Comece pela esquerda: [p=0.2] {b}sete dividido por três dá dois, [p=0.2] porque três vezes dois dá seis. [p=0.2] De seis para sete, {c}sobra um. [p=0.3] Essa conta você faz de cabeça: [p=0.2] embaixo, só escreve o que sobrou."),
    dict(id="s10", block="chave", text="{a}Desça o oito: o um vira dezoito. [p=0.3] Por que descer? [p=0.2] Aquele sete são {b}sete notas de dez reais. [p=0.2] Cada pessoa levou duas, e {c}sobrou uma nota. [p=0.2] Ela vira {d}dez moedas de um real, [p=0.2] que se juntam às {e}oito moedas: dezoito."),
    dict(id="s11", block="chave", text="{a}Dezoito dividido por três dá seis, [p=0.2] e {b}sobra zero. [p=0.3] Resultado: {c}vinte e seis reais para cada pessoa. [p=0.3] Sobrou zero, então a divisão é {d}exata: não tem resto. [p=0.2] Prova real: {e}três vezes vinte e seis dá setenta e oito."),
    # o zero no meio
    dict(id="s12", block="zero", text="Voltando ao começo: {a}seiscentos e doze dividido por três. [p=0.3] {b}Seis dividido por três dá dois, [p=0.2] e {c}sobra zero. [p=0.2] Desça o um: {d}um dividido por três não dá."),
    dict(id="s13", block="zero", text="Não pule essa casa: {a}escreva zero no quociente. [p=0.3] {b}Desça o dois: doze. [p=0.2] {c}Doze dividido por três dá quatro, [p=0.2] e {d}sobra zero. [p=0.3] Resultado: {e}duzentos e quatro. [p=0.2] Prova real: {f}três vezes duzentos e quatro dá seiscentos e doze."),
    # erro
    dict(id="s14", block="erro", text="O erro comum é {a}pular esse zero. [p=0.2] Ele diz que {b}nenhuma dezena deu para repartir. [p=0.2] Sem ele, o dois cai na casa das dezenas, [p=0.2] e {c}duzentos vira vinte. [p=0.3] A regra: {d}desceu um algarismo, escreva um algarismo no quociente, [p=0.2] nem que seja zero."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}vezes cinco é vezes dez, dividido por dois. [p=0.3] É a ideia da tabuada do cinco, agora com número maior. [p=0.2] {b}Quarenta e seis vezes cinco. [p=0.2] {c}Faça vezes dez: quatrocentos e sessenta. [p=0.2] {d}Tire a metade: duzentos e trinta."),
    dict(id="s16", block="atalho", text="Funciona porque {a}cinco é a metade de dez. [p=0.3] Só vale para vezes cinco, [p=0.2] e {b}não compensa quando a metade não sai de cabeça: [p=0.2] aí, arme a conta."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Uma padaria assou {a}quatrocentos e vinte e três pães [p=0.2] e coloca {b}quatro pães em cada saco. [p=0.3] {c}Quantos sacos cheios ela fecha, e quantos pães sobram?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Quatro dividido por quatro dá um, [p=0.2] e {b}sobra zero. [p=0.2] Desça o dois: {c}dois dividido por quatro não dá. [p=0.2] {d}Escreva zero no quociente."),
    dict(id="s20", block="resposta", text="{a}Desça o três: vinte e três. [p=0.2] {b}Vinte e três dividido por quatro dá cinco, [p=0.2] e {c}sobram três. [p=0.3] São {d}cento e cinco sacos cheios, [p=0.2] e {e}sobram três pães. [p=0.3] Prova real: {f}quatro vezes cento e cinco dá quatrocentos e vinte. [p=0.2] {g}Com os três pães, quatrocentos e vinte e três."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}comece pela esquerda, [p=0.2] {b}desça um algarismo de cada vez [p=0.2] e {c}não pule o zero."),
    dict(id="s22", block="fim", text="Até aqui, o divisor tinha um algarismo, e a tabuada bastava. [p=0.2] Na próxima aula, {a}o divisor tem dois algarismos, [p=0.2] e você aprende a {b}estimar cada algarismo do resultado. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
