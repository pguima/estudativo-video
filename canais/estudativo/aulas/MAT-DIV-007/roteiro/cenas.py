# Estudativo · MAT-DIV-007 — Problemas de MMC: encontros que se repetem (Matemática · Divisibilidade, MMC e MDC).
# Habilidade: calcular quando dois ônibus que saem a cada 12 e 18 minutos se encontram de novo e diferenciar esse caso de um problema de MDC.
# Pré-requisitos: MAT-DIV-005, MAT-DIV-006. Próxima: MAT-DIV-008.
# Ônibus: 12, 24, 36, 48 · 18, 36, 54 → 36. Fatoração simultânea: ÷2 → 6, 9 · ÷2 → 3, 9 · ÷3 → 1, 3 · ÷3 → 1, 1 → 2·2·3·3 = 36.
# MDC(12, 18) = 6; 12 × 18 = 216; 216 ÷ 6 = 36. Encontros: 36, 72, 108. Lâmpadas: MMC(6, 8) = 24. Quantos encontros em 3 h: 180 ÷ 36 = 5.
# Treino: 40 lápis e 60 canetas (MDC, sem calcular na tela) · academia a cada 3 e 4 dias (MMC, sem calcular na tela).
# Questão: 15, 20: ÷2 → 15, 10 · ÷2 → 15, 5 · ÷3 → 5, 5 · ÷5 → 1, 1 → 2·2·3·5 = 60.

TITULO = "Problemas de MMC: encontros que se repetem"

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
    dict(id="s01", block="gancho", text="Dois ônibus saem juntos do terminal. [p=0.2] {a}Um passa a sair a cada doze minutos. [p=0.2] {b}O outro, a cada dezoito. [p=0.3] {c}Quando saem juntos de novo?"),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você responde isso {a}e para de confundir MMC com MDC, [p=0.2] com um {b}atalho de prova: a pista no texto."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}duas coisas: [p=0.2] {b}calcular o MMC [p=0.2] e {c}reconhecer um problema de MDC. [p=0.3] Se faltar alguma, procure a aula no canal."),
    # linha do tempo
    dict(id="s04", block="tempo", text="Monte a linha do tempo. [p=0.2] {a}O primeiro ônibus sai aos doze, vinte e quatro, trinta e seis e quarenta e oito minutos. [p=0.3] {b}O segundo sai aos dezoito, trinta e seis e cinquenta e quatro."),
    dict(id="s05", block="tempo", text="Cada ônibus só sai nos {a}múltiplos do seu intervalo. [p=0.2] Sair junto é estar nas duas listas: {b}múltiplo comum. [p=0.2] E a primeira vez é {c}o menor deles. [p=0.3] {d}Mínimo múltiplo comum."),
    dict(id="s06", block="tempo", text="A primeira coincidência é em {a}trinta e seis minutos. [p=0.2] Se saíram juntos {b}às sete horas, [p=0.2] saem juntos de novo {c}às sete e trinta e seis."),
    dict(id="s07", block="tempo", text="E não para por aí. [p=0.2] Eles voltam a se encontrar {a}aos setenta e dois, [p=0.2] {b}aos cento e oito, [p=0.2] e assim por diante. [p=0.3] O MMC é {c}o intervalo entre um encontro e outro."),
    dict(id="s08", block="conta", text="Sem lista, use a fatoração simultânea. [p=0.2] {a}Doze e dezoito, lado a lado. [p=0.2] {b}Por dois: seis e nove. [p=0.2] {c}Por dois: três e nove. [p=0.2] {d}Por três: um e três. [p=0.2] {e}Por três: um e um. [p=0.3] {f}Dois vezes dois vezes três vezes três: trinta e seis."),
    dict(id="s09", block="conta", text="Com dois números, também vale o atalho da aula de MMC: [p=0.2] {a}doze vezes dezoito, duzentos e dezesseis. [p=0.2] {b}Dividido pelo MDC, que é seis: [p=0.2] {c}trinta e seis."),
    # diferença
    dict(id="s10", block="diferenca", text="Veja os mesmos números em outra história. [p=0.2] {a}Duas cordas, de doze e de dezoito metros, [p=0.2] cortadas em {b}pedaços iguais, os maiores possíveis, sem sobra."),
    dict(id="s11", block="diferenca", text="Aqui o pedaço precisa caber nas cordas: é {a}divisor comum, o maior. [p=0.2] {b}MDC de doze e dezoito: seis metros."),
    dict(id="s12", block="diferenca", text="Mesmos números, respostas diferentes. [p=0.2] {a}Trinta e seis nos ônibus. [p=0.2] {b}Seis nas cordas. [p=0.3] Quem decide é a história, não a conta."),
    dict(id="s13", block="diferenca", text="{a}MDC reparte: uma coisa é dividida em partes iguais. [p=0.3] {b}MMC repete: coisas acontecem em ciclos e voltam a coincidir."),
    # treino de decisão
    dict(id="s14", block="decidir", text="Treine o olho, sem calcular nada. [p=0.2] {a}Quarenta lápis e sessenta canetas em estojos iguais, o maior número possível, sem sobra: [p=0.2] {b}reparte, MDC. [p=0.3] {c}Dois amigos vão à academia, um a cada três dias, outro a cada quatro, e se encontraram hoje. Quando se encontram lá de novo? [p=0.2] {d}Repete, MMC."),
    # erro
    dict(id="s15", block="erro", text="O erro mais comum é {a}usar o MDC no problema dos ônibus. [p=0.2] A pessoa responde {b}seis minutos. [p=0.3] Mas aos seis minutos {c}nenhum ônibus voltou a sair. [p=0.2] O encontro não pode vir antes da próxima saída de cada um."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho, que é uma pista no texto: [p=0.2] {a}a cada, [p=0.2] {b}ao mesmo tempo, [p=0.2] {c}juntos de novo. [p=0.3] Apareceu isso, {d}é MMC."),
    dict(id="s17", block="atalho", text="Funciona porque cada pista é um pedaço do nome. [p=0.2] {a}A cada é múltiplo. [p=0.2] {b}Junto é comum. [p=0.2] {c}A primeira vez de novo é mínimo."),
    dict(id="s19", block="atalho", text="Quando não compensa? [p=0.2] Quando a pergunta {a}vai além do próximo encontro. [p=0.2] Se pedir quantos encontros os ônibus têm em três horas, o MMC é só o começo: [p=0.2] {b}cento e oitenta minutos divididos por trinta e seis, {c}cinco encontros, sem contar a saída do começo. [p=0.3] E {d}a cada, sozinho, não basta: [p=0.2] com um ônibus só, não existe encontro, e não existe MMC."),
    # questão
    dict(id="s20", block="questao", text="Hora de testar. [p=0.2] {a}Uma máquina passa por manutenção a cada quinze dias. [p=0.2] {b}Outra, a cada vinte. [p=0.2] Hoje, pararam juntas. [p=0.3] {c}É MMC ou MDC? [p=0.2] {d}Daqui a quantos dias param juntas de novo?"),
    dict(id="s21", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="resposta", text="Vamos lá. [p=0.2] A cada, juntas, de novo: {a}MMC. [p=0.3] {b}Por dois: quinze e dez. [p=0.2] {c}Por dois: quinze e cinco. [p=0.2] {d}Por três: cinco e cinco. [p=0.2] {e}Por cinco: um e um."),
    dict(id="s23", block="resposta", text="Multiplique a coluna: {a}dois vezes dois vezes três vezes cinco. [p=0.3] {b}Sessenta dias."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}reparte em partes iguais, MDC. [p=0.2] {b}Repete e volta a coincidir, MMC."),
    dict(id="s25", block="fim", text="Na próxima aula, é a sua vez: {a}cinco questões para praticar múltiplos, primos, MMC e MDC. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
