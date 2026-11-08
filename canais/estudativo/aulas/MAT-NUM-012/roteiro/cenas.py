# Estudativo · MAT-NUM-012 — Praticando: números e as quatro operações (Matemática · Números e Contas · As quatro operações · prática).
# Habilidade: ler números grandes, resolver problemas do dia a dia com as quatro contas e usar atalhos como 99 × 7 = 700 − 7 e 48 × 5 = 480 ÷ 2.
# Pré-requisitos: MAT-NUM-001 a MAT-NUM-011. Próxima: MAT-NUM-013 (ordem das operações e parênteses).
# Questões inéditas, criadas para esta aula; nenhuma é de prova real. Sem parênteses nem expressão numa linha só (MAT-NUM-013 vem depois):
#   cada conta é feita em separado. Divisão por dois algarismos na forma curta da chave, com o palpite da MAT-NUM-010 (arredondar o divisor e cobrir o último algarismo).
# Q1: 3.040.500 × 3.004.950 · mesmos dois pontos · milhões 3 = 3 · milhares 040 > 004 → maior 3.040.500 ("três milhões, quarenta mil e quinhentos").
# Q2: 1.000 − 368 = 632 · atalho da MAT-NUM-004 (a distância não muda): tira um dos dois → 999 − 367 = 632, sem empréstimo · prova: 632 + 368 = 1.000.
# Q3: 48 × 5 = 480 ÷ 2 = 240 (MAT-NUM-009) · 99 × 7 = 700 − 7 = 693 (MAT-NUM-007) · 240 + 693 = 933.
# Q4: 1.288 ÷ 23 · 23 × 10 = 230, 23 × 100 = 2.300 → dois algarismos · 128: 12 ÷ 2 = 6 → 23 × 6 = 138 > 128, baixa → 5: 115, sobra 13 ·
#   desce o 8: 138 · 13 ÷ 2 = 6 → 23 × 6 = 138, sobra 0 → 56 · prova real 23 × 56 = 1.288.
# Q5: 500 alunos, ônibus de 42 lugares · 500 ÷ 42: 50 → 1 (42), sobra 8 · desce o 0: 80 → 8 ÷ 4 = 2 → 84 > 80, baixa → 1 (42), sobra 38 ·
#   11 com resto 38 · 11 ônibus levam 462 · ficam 38 alunos → 12 ônibus. Prova real: 42 × 11 + 38 = 462 + 38 = 500.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Praticando: números e as quatro operações"

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
    dict(id="s01", block="gancho", text="{a}Cinco questões criadas para esta aula, [p=0.2] com as quatro contas e os atalhos do módulo. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] {c}Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}ler e comparar números grandes, [p=0.2] {b}somar e subtrair, [p=0.2] {c}multiplicar, [p=0.2] {d}dividir, inclusive por dois algarismos, [p=0.2] e {e}escolher a conta pelo sentido do problema. [p=0.3] Se alguma travar, procure a aula no canal."),
    # questão 1: ler e comparar
    dict(id="s03", block="q1", text="{a}Questão um. [p=0.2] Na tela, {b}os valores de dois prêmios. [p=0.3] {c}Qual é o maior? [p=0.2] {d}Leia esse em voz alta."),
    dict(id="s04", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="r1", text="Vamos lá. [p=0.2] Primeiro, {a}conte os pontos: [p=0.2] cada um tem dois pontos, então o atalho não decide. [p=0.3] {b}Compare grupo por grupo, da esquerda para a direita. [p=0.2] {c}Nos milhões, três e três: empate. [p=0.2] {d}Nos milhares, quarenta contra quatro. [p=0.3] {e}Quarenta mil ganha. [p=0.3] Quem olhou o fim, {f}novecentos e cinquenta, caiu na pegadinha."),
    dict(id="s06", block="r1", text="O maior é {a}três milhões, quarenta mil e quinhentos reais. [p=0.3] {b}Leia um grupo de cada vez, com o nome do grupo no fim: [p=0.2] três milhões, [p=0.2] quarenta mil, [p=0.2] quinhentos."),
    # questão 2: subtrair por cima do zero
    dict(id="s07", block="q2", text="{a}Questão dois. [p=0.2] Você tinha {b}mil reais na conta [p=0.2] e pagou {c}um boleto de trezentos e sessenta e oito reais. [p=0.3] {d}Quanto sobrou?"),
    dict(id="s08", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="r2", text="A conta é {a}mil menos trezentos e sessenta e oito. [p=0.3] Armada, ela pede emprestado {b}por cima de três zeros. [p=0.2] Dá para fugir disso com um atalho. [p=0.3] {c}Tire um de cada número: [p=0.2] fica {d}novecentos e noventa e nove menos trezentos e sessenta e sete."),
    dict(id="s10", block="r2", text="Agora, nenhuma casa pede empréstimo: [p=0.2] {a}nove menos sete, dois. [p=0.2] {b}Nove menos seis, três. [p=0.2] {c}Nove menos três, seis. [p=0.3] Sobraram {d}seiscentos e trinta e dois reais. [p=0.3] Funciona porque {e}a distância entre os números não muda. [p=0.2] Confira com uma soma: {f}seiscentos e trinta e dois mais trezentos e sessenta e oito dá mil."),
    # questão 3: atalhos de multiplicar
    dict(id="s11", block="q3", text="{a}Questão três. [p=0.2] Uma festa vendeu {b}quarenta e oito ingressos de cinco reais [p=0.2] e {c}noventa e nove ingressos de sete reais. [p=0.3] {d}Quanto a festa arrecadou?"),
    dict(id="s12", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="r3", text="São {a}grupos iguais, então é multiplicação. [p=0.3] {b}Quarenta e oito vezes cinco: [p=0.2] vezes cinco é vezes dez, dividido por dois. [p=0.2] {c}Quarenta e oito vezes dez, quatrocentos e oitenta. [p=0.2] {d}A metade, duzentos e quarenta."),
    dict(id="s14", block="r3", text="{a}Noventa e nove vezes sete: [p=0.2] noventa e nove é cem menos um. [p=0.2] {b}Cem vezes sete, setecentos. [p=0.2] {c}Tire um sete: seiscentos e noventa e três. [p=0.3] No fim, {d}junte os dois valores: [p=0.2] duzentos e quarenta mais seiscentos e noventa e três dá {e}novecentos e trinta e três reais."),
    # questão 4: dividir por dois algarismos
    dict(id="s15", block="q4", text="{a}Questão quatro. [p=0.2] Um prêmio de {b}mil duzentos e oitenta e oito reais [p=0.2] vai ser repartido igualmente entre {c}vinte e três pessoas. [p=0.3] {d}Quanto recebe cada uma?"),
    dict(id="s16", block="q4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="r4", text="Repartir igualmente é {a}divisão. [p=0.3] Antes, o tamanho do resultado: [p=0.2] {b}vinte e três vezes dez dá duzentos e trinta, [p=0.2] {c}vezes cem dá dois mil e trezentos. [p=0.2] Mil duzentos e oitenta e oito fica no meio: [p=0.2] {d}o resultado tem dois algarismos."),
    dict(id="s18", block="r4", text="{a}Primeiro pedaço: cento e vinte e oito. [p=0.2] Vinte e três fica perto de vinte. [p=0.2] Cubra o último algarismo: {b}doze dividido por dois dá seis. [p=0.2] {c}Vinte e três vezes seis dá cento e trinta e oito: [p=0.2] passou. [p=0.2] Palpite alto, {d}baixe um. [p=0.3] {e}Vinte e três vezes cinco, cento e quinze. [p=0.2] {f}Sobram treze."),
    dict(id="s19", block="r4", text="{a}Desça o oito: cento e trinta e oito. [p=0.2] {b}Treze dividido por dois dá seis. [p=0.2] Essa você já fez: {c}vinte e três vezes seis, cento e trinta e oito. [p=0.2] {d}Sobra zero. [p=0.3] Cada pessoa recebe {e}cinquenta e seis reais. [p=0.2] Prova real: {f}vinte e três vezes cinquenta e seis dá mil duzentos e oitenta e oito."),
    # questão 5: o resto decide
    dict(id="s20", block="q5", text="{a}Última questão. [p=0.2] Uma escola vai levar {b}quinhentos alunos a um passeio, [p=0.2] em ônibus de {c}quarenta e dois lugares. [p=0.3] {d}Quantos ônibus ela precisa contratar?"),
    dict(id="s21", block="q5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="r5", text="Quantos grupos de quarenta e dois cabem em quinhentos? [p=0.2] {a}É divisão. [p=0.3] {b}Primeiro pedaço: cinquenta. O quarenta e dois cabe uma vez, e sobram oito. [p=0.2] {c}Desça o zero: oitenta. [p=0.2] Quarenta e dois vezes dois daria oitenta e quatro, que passa. [p=0.2] {d}Cabe uma vez, e sobram trinta e oito."),
    dict(id="s23", block="r5", text="Deu {a}onze, com resto trinta e oito. [p=0.3] Aqui mora a pegadinha: {b}muita gente responde onze. [p=0.2] Mas onze ônibus levam {c}quatrocentos e sessenta e dois alunos, [p=0.2] e {d}trinta e oito ficariam na escola. [p=0.3] Eles precisam de mais um ônibus: {e}doze. [p=0.3] {f}O resto não some: a história diz o que fazer com ele."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}leia o problema e escolha a conta pelo sentido, [p=0.2] {b}use o atalho quando o número ajuda [p=0.2] e {c}confira com a conta inversa."),
    dict(id="s25", block="fim", text="Na próxima aula, as contas aparecem {a}juntas, numa linha só, [p=0.2] e você descobre {b}qual fazer primeiro, [p=0.2] com {c}parênteses e colchetes. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
