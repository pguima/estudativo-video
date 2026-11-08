# Estudativo · MAT-PRO-010 — Soma dos termos de uma PG (Matemática · Progressões · Progressão geométrica).
# Habilidade: somar 1 + 2 + 4 + … + 512 = 1.023 com a fórmula e calcular quantas pessoas uma corrente alcança em 10 rodadas.
# Pré-requisitos: MAT-PRO-008 (razão e termo geral aₙ = a₁ · qⁿ⁻¹). Próxima: MAT-PRO-011.
# Questão inédita, criada para esta aula. Termos narrados como "o primeiro termo", "o décimo termo" (sem "á um"); q narrado "quê"; S narrado "ésse".
# Contas: 1 + 2 + … + 512 (2⁰ a 2⁹, 10 termos) = 1.023 · 2S = 2 + 4 + … + 1.024 · 2S − S = 1.024 − 1 · S₁₀ = 1 · (2¹⁰ − 1)/(2 − 1) = 1.023.
# Fórmula: Sₙ = a₁ · (qⁿ − 1)/(q − 1); a₁ · qⁿ = termo seguinte ao último. Com razão 3, q · S − S = 2S ("sobrariam duas").
# Erro: n = 9 (porque 512 = 2⁹) → 2⁹ − 1 = 511 < 512.
# Atalho: S = (termo seguinte ao último − primeiro)/(q − 1); com q = 2: próximo − primeiro.
# Questão: corrente 3, 6, 12, … (a₁ = 3, q = 2, n = 10) · 3 · (1.024 − 1)/1 = 3.069 · a₁₀ = 3 · 2⁹ = 1.536 · seguinte 3.072 − 3 = 3.069.
# Visual:
#   s01: dez moedas/caixas por dia (E.colunas): 1, 2, 4, … 512, dobrando; total 1.023 aceso.
#   s04-s06: duas linhas empilhadas, S = 1 + 2 + … + 512 e 2S = 2 + 4 + … + 1.024, termos iguais alinhados e riscados; sobram 1.024 e 1.
#   s07-s08: Sₙ = a₁ · (qⁿ − 1)/(q − 1) com legendas (soma, primeiro termo, razão, quantidade de termos); a₁ · qⁿ apontado como "termo seguinte ao último".
#   s11-s12: 2⁹ − 1 = 511 em vermelho ao lado do 512; contagem de expoentes 0 a 9 embaixo da fila.
#   s15-s19: árvore da corrente (você → 3 → 6 → 12…) com a contagem por rodada.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Soma dos termos de uma PG"

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
    dict(id="s01", block="gancho", text="{a}Um real hoje. [p=0.2] {b}Dois reais amanhã. [p=0.2] {c}Quatro no dia seguinte, [p=0.2] sempre dobrando, por {d}dez dias. [p=0.3] Quanto você juntou? [p=0.2] {e}Mil e vinte e três reais. [p=0.3] E dá para saber sem somar os dez valores."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você soma os termos de uma pê gê numa conta só, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}uma coisa: [p=0.2] {b}na pê gê, cada termo é o anterior vezes o mesmo número, a razão. [p=0.2] A letra dela é quê. [p=0.2] E {c}o termo geral: á índice ene igual a á índice um vezes quê elevado ao número de saltos, que é ene menos um. [p=0.3] Se faltar, procure no canal."),
    # o truque
    dict(id="s04", block="truque", text="Os valores são {a}um, [p=0.1] dois, [p=0.1] quatro, [p=0.1] oito, e assim até quinhentos e doze. [p=0.2] Chame a soma de {b}ésse. [p=0.3] Agora, um truque: {c}dobre a soma inteira. [p=0.2] Cada termo dobra e vira {d}o termo seguinte."),
    dict(id="s05", block="truque", text="{a}A soma dobrada vai de dois até mil e vinte e quatro. [p=0.2] Compare as duas linhas. [p=0.2] {b}Do dois ao quinhentos e doze, tudo se repete. [p=0.3] A diferença é só {c}o mil e vinte e quatro, que entrou no fim, [p=0.2] e {d}o um, que saiu do começo."),
    dict(id="s06", block="truque", text="Então, {a}dois ésse menos ésse [p=0.2] é {b}mil e vinte e quatro menos um. [p=0.2] {c}Ésse igual a mil e vinte e três. [p=0.3] Nenhuma soma longa: [p=0.2] {d}o termo seguinte ao último, menos o primeiro."),
    # fórmula
    dict(id="s07", block="formula", text="Com qualquer pê gê, o truque é o mesmo: [p=0.2] {a}multiplique a soma pela razão e tire a soma original. [p=0.3] Daí sai a fórmula. [p=0.2] {b}Ésse índice ene igual a á índice um, vezes, abre parênteses, quê elevado a ene, menos um, fecha parênteses, [p=0.2] {c}tudo dividido por, abre parênteses, quê menos um, fecha parênteses."),
    dict(id="s08", block="formula", text="{a}Ésse índice ene é a soma, e ene é quantos termos você soma. [p=0.2] Á índice um é o primeiro termo, e {b}quê é a razão. [p=0.3] Á índice um vezes quê elevado a ene é {c}o termo seguinte ao último: [p=0.2] o mil e vinte e quatro do exemplo. [p=0.3] E o quê menos um vem da subtração. [p=0.2] {d}Com razão dois, dois ésse menos ésse deixa um ésse só. [p=0.2] Com razão três, três ésse menos ésse deixaria dois ésse, [p=0.2] e aí você divide por dois."),
    dict(id="s09", block="formula", text="Vamos conferir. [p=0.2] Primeiro termo, {a}um. [p=0.2] Razão, {b}dois. [p=0.2] E quantos termos? [p=0.2] Quinhentos e doze é {c}dois elevado a nove. [p=0.2] Pelo termo geral, ene menos um é nove, [p=0.2] então {d}ene é dez."),
    dict(id="s10", block="formula", text="{a}Dois elevado a dez dá mil e vinte e quatro. [p=0.2] {b}Menos um dá mil e vinte e três. [p=0.2] {c}Vezes o primeiro termo, que é um, continua mil e vinte e três. [p=0.2] {d}Dividido por dois menos um, que dá um, continua mil e vinte e três. [p=0.2] Bateu."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}contar errado os termos. [p=0.2] Quinhentos e doze é dois elevado a nove, [p=0.2] e a pessoa usa {b}ene igual a nove. [p=0.3] {c}Dois elevado a nove, menos um, dá quinhentos e onze."),
    dict(id="s12", block="erro", text="Uma soma de números positivos {a}menor que o último termo sozinho? [p=0.2] Impossível. [p=0.3] {b}O expoente nove é da posição dez, porque o primeiro termo tem expoente zero. [p=0.2] Na dúvida, {c}conte as posições a partir do um."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: [p=0.2] {a}o termo seguinte ao último, menos o primeiro, tudo dividido por, abre parênteses, a razão menos um, fecha parênteses. [p=0.3] Com razão dois, o de baixo é um, [p=0.2] e a soma é só {b}o próximo termo menos o primeiro."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o primeiro termo vezes quê elevado a ene é o termo seguinte ao último. [p=0.2] É a mesma fórmula, sem a potência. [p=0.3] Não compensa quando a questão dá {b}só a quantidade de termos, e não o último. [p=0.2] Aí, {c}a fórmula vai direto."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Você manda uma mensagem para {a}três amigos: essa é a primeira rodada. [p=0.2] Em cada rodada seguinte, {b}cada pessoa que recebeu na rodada anterior repassa para duas pessoas novas. [p=0.3] {c}Quantas pessoas recebem a mensagem ao todo, em dez rodadas?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Rodada a rodada: {a}três, depois seis, depois doze. [p=0.2] Uma pê gê com {b}primeiro termo três e razão dois. [p=0.2] Dez rodadas: {c}ene igual a dez."),
    dict(id="s18", block="resposta", text="{a}Dois elevado a dez dá mil e vinte e quatro. [p=0.2] {b}Menos um dá mil e vinte e três. [p=0.2] {c}Vezes três dá três mil e sessenta e nove. [p=0.2] Dividido por dois menos um, que dá um, [p=0.2] {d}continuam três mil e sessenta e nove pessoas."),
    dict(id="s19", block="resposta", text="Pelo atalho: o décimo termo é {a}três vezes dois elevado a nove, que dá mil quinhentos e trinta e seis. [p=0.2] O seguinte seria {b}três mil e setenta e dois. [p=0.2] Tire o primeiro termo, que é três: [p=0.2] {c}sobram três mil e sessenta e nove. [p=0.2] Bateu."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}multiplique a soma pela razão e subtraia. [p=0.2] Sobra {b}o termo seguinte ao último, menos o primeiro, [p=0.2] {c}tudo dividido por, abre parênteses, a razão menos um, fecha parênteses."),
    dict(id="s21", block="fim", text="Na próxima aula, uma soma que {a}não acaba nunca: [p=0.2] {b}um, mais um meio, mais um quarto, e assim por diante. [p=0.3] Infinitos termos, e mesmo assim {c}o total dá dois. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
