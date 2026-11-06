# Estudativo · MAT-DIV-001 — Múltiplos e divisores (Matemática · Divisibilidade, MMC e MDC).
# Habilidade: dizer se 54 é múltiplo de 6 e listar em pares todos os divisores de 36.
# Pré-requisitos: MAT-NUM-009. Próxima: MAT-DIV-002.
# Contas: 54 ÷ 6 = 9 · 54 ÷ 7 = 7 resto 5 · 36 = 1×36 = 2×18 = 3×12 = 4×9 = 6×6 (36 ÷ 5 = 7 resto 1) → 9 divisores.
# Questão: 28 = 1×28 = 2×14 = 4×7 (3, 5 e 6 deixam resto; o 7 já apareceu) → 1, 2, 4, 7, 14, 28 → 6 divisores.

TITULO = "Múltiplos e divisores"

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
    dict(id="s01", block="gancho", text="Quantos divisores tem {a}o número trinta e seis? [p=0.3] Se você tentou contar de cabeça, é bem provável que {b}tenha esquecido algum."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você lista {a}todos, sem esquecer nenhum, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}uma coisa: [p=0.2] fazer uma divisão e ver se sobrou resto. [p=0.3] {b}Dezessete dividido por cinco dá três, [p=0.2] {c}e sobram dois. [p=0.3] Se isso estiver enferrujado, procure a aula no canal."),
    # múltiplo
    dict(id="s04", block="multiplo", text="Comece por uma cena do dia a dia. [p=0.2] Você tem {a}cinquenta e quatro ovos e {b}caixas de seis. [p=0.3] Dá para encher as caixas sem sobrar nenhum ovo?"),
    dict(id="s05", block="multiplo", text="Faça a divisão: {a}cinquenta e quatro dividido por seis dá nove, [p=0.2] e {b}o resto é zero. [p=0.3] São {c}nove caixas cheias, sem sobra."),
    dict(id="s06", block="multiplo", text="Quando a divisão fecha assim, a matemática tem um nome para isso: [p=0.2] {a}cinquenta e quatro é múltiplo de seis. [p=0.3] Múltiplo é o resultado de multiplicar o número por outro, como na tabuada, só que sem parar no dez. [p=0.3] {b}Seis vezes nove, cinquenta e quatro."),
    dict(id="s07", block="multiplo", text="E com sete? [p=0.2] {a}Cinquenta e quatro dividido por sete dá sete, [p=0.2] e {b}sobram cinco. [p=0.3] Sobrou, então {c}cinquenta e quatro não é múltiplo de sete."),
    dict(id="s08", block="multiplo", text="A lista de múltiplos nunca termina: {a}seis, doze, dezoito, vinte e quatro, [p=0.2] e assim por diante, {b}sem fim."),
    # divisor
    dict(id="s09", block="divisor", text="A mesma história tem outro lado. [p=0.2] Se cinquenta e quatro é múltiplo de seis, então {a}seis é divisor de cinquenta e quatro. [p=0.3] Divisor é o número que divide outro {b}sem deixar resto."),
    dict(id="s10", block="divisor", text="É a mesma ideia, {a}dita de outro jeito. [p=0.3] Só que, ao contrário dos múltiplos, {b}os divisores acabam. [p=0.2] Nenhum divisor passa do próprio número."),
    # divisores em pares
    dict(id="s11", block="pares", text="Vamos aos divisores de trinta e seis. [p=0.2] Imagine {a}trinta e seis cadeiras, arrumadas em fileiras iguais. [p=0.3] Cada arrumação é {b}uma multiplicação, [p=0.2] e cada multiplicação entrega {c}um par de divisores de uma vez."),
    dict(id="s12", block="pares", text="Comece do um e vá subindo. [p=0.2] {a}Uma fileira de trinta e seis. [p=0.2] {b}Duas fileiras de dezoito. [p=0.2] {c}Três de doze. [p=0.2] {d}Quatro de nove."),
    dict(id="s13", block="pares", text="E cinco fileiras? [p=0.2] {a}Trinta e seis dividido por cinco deixa resto. [p=0.2] {b}Não serve. [p=0.3] {c}Seis fileiras de seis: [p=0.2] aqui o número se repete, então o seis {d}conta uma vez só."),
    dict(id="s14", block="pares", text="Juntando tudo, em ordem: [p=0.2] {a}um, dois, três, quatro, seis, nove, doze, dezoito e trinta e seis. [p=0.3] {b}Nove divisores. [p=0.2] Repare que {c}o um e o próprio número sempre entram, e são os mais esquecidos."),
    # erro
    dict(id="s15", block="erro", text="O erro mais comum é {a}trocar as palavras. [p=0.2] A pessoa diz que {b}cinquenta e quatro é divisor de seis. [p=0.3] Mas cinquenta e quatro {c}não cabe dentro de seis. [p=0.2] É o contrário."),
    dict(id="s16", block="erro", text="Para não confundir: {a}múltiplo é o grande, que vem da multiplicação. [p=0.2] {b}Divisor é o pequeno, que cabe certinho dentro dele. [p=0.3] {c}Seis é divisor de cinquenta e quatro. [p=0.2] {d}Cinquenta e quatro é múltiplo de seis."),
    # atalho
    dict(id="s17", block="atalho", text="Agora o atalho: [p=0.2] {a}pare quando os pares se encontrarem. [p=0.3] Você não precisou testar até trinta e seis. [p=0.2] {b}Parou no seis."),
    dict(id="s18", block="atalho", text="Funciona porque a coluna da esquerda {a}sobe, enquanto a da direita {b}desce. [p=0.3] Quando elas se encontram, todo divisor maior {c}já apareceu na direita. [p=0.3] Testar o nove, por exemplo, só repetiria o par quatro vezes nove."),
    dict(id="s19", block="atalho", text="Quando não compensa? [p=0.2] {a}Se a pergunta é só se um número divide o outro, [p=0.2] não liste nada: {b}faça aquela divisão e pronto. [p=0.3] E em {c}números muito grandes, testar um por um cansa, e aí entram regras mais rápidas."),
    # questão
    dict(id="s20", block="questao", text="Hora de testar. [p=0.2] {a}Liste, em pares, todos os divisores de vinte e oito."),
    dict(id="s21", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="resposta", text="Vamos lá. [p=0.2] {a}Um vezes vinte e oito. [p=0.2] {b}Dois vezes catorze. [p=0.2] O três {c}deixa resto, não serve. [p=0.2] {d}Quatro vezes sete."),
    dict(id="s23", block="resposta", text="Cinco e seis {a}também deixam resto. [p=0.2] Depois vem o sete, que {b}já apareceu, então pare. [p=0.3] Em ordem: {c}um, dois, quatro, sete, catorze e vinte e oito. [p=0.2] {d}Seis divisores."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}divisão sem resto [p=0.2] quer dizer que um número é {b}múltiplo e o outro é {c}divisor. [p=0.2] Para listar todos, {d}use pares e pare quando eles se encontrarem."),
    dict(id="s25", block="fim", text="Na próxima aula, as {a}regras de divisibilidade: como saber, sem fazer a conta, se um número se divide por dois, por três, por nove e outros. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
