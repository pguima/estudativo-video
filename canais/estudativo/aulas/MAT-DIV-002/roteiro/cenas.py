# Estudativo · MAT-DIV-002 — Regras de divisibilidade (Matemática · Divisibilidade, MMC e MDC).
# Habilidade: saber sem dividir se 4.572 é divisível por 2, 3, 4, 5, 6, 9 ou 10.
# Pré-requisitos: MAT-DIV-001, MAT-NUM-003. Próxima: MAT-DIV-003.
# 4.572: termina em 2 → por 2 sim, por 5 e 10 não · 72 ÷ 4 = 18 → por 4 sim · 4+5+7+2 = 18 → por 3 e 9 sim · par e por 3 → por 6 sim.
# Conferência: 4.572 ÷ 2 = 2.286 · ÷ 3 = 1.524 · ÷ 4 = 1.143 · ÷ 6 = 762 · ÷ 9 = 508.
# Questão: 7.290: termina em 0 → 2, 5 e 10 · 7+2+9+0 = 18 → 3 e 9 · par e por 3 → 6 · 90 ÷ 4 = 22 resto 2 → não por 4.

TITULO = "Regras de divisibilidade"

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
    dict(id="s01", block="gancho", text="O número {a}quatro mil quinhentos e setenta e dois se divide por nove? [p=0.3] Dá para saber {b}em poucos segundos, sem armar a conta."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você testa esse número contra {a}sete divisores, sem dividir nada, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}duas coisas: [p=0.2] {b}o que é um divisor [p=0.2] e {c}como somar de cabeça. [p=0.3] Se faltar alguma, procure a aula no canal."),
    # o que é
    dict(id="s04", block="nome", text="{a}Divisível é a palavra para divisão sem resto. [p=0.2] Dizer que doze é divisível por três é dizer que três é divisor de doze. [p=0.3] E uma regra de divisibilidade é um teste que {b}responde isso sem dividir."),
    # final do número
    dict(id="s05", block="final", text="Comece pelas regras que {a}olham só o último algarismo. [p=0.3] {b}Por dez: termina em zero. [p=0.2] {c}Por cinco: termina em zero ou cinco. [p=0.2] {d}Por dois: termina em algarismo par, [p=0.2] ou seja, zero, dois, quatro, seis ou oito."),
    dict(id="s06", block="final", text="Por que basta o final? [p=0.2] Pense em {a}notas de dez reais. [p=0.2] Qualquer quantidade delas se divide certinho por dois, por cinco e por dez. [p=0.3] Quem decide é {b}o trocado, que é o último algarismo."),
    dict(id="s07", block="final", text="Teste em {a}quatro mil quinhentos e setenta e dois. [p=0.2] Termina em {b}dois. [p=0.3] É {c}divisível por dois. [p=0.2] {d}Não é por cinco, {e}nem por dez."),
    # por quatro
    dict(id="s08", block="quatro", text="{a}Por quatro, olhe o número formado pelos últimos dois algarismos. [p=0.3] Se ele for divisível por quatro, o número inteiro também é."),
    dict(id="s09", block="quatro", text="O motivo é parecido: {a}cem reais se dividem certinho por quatro, [p=0.2] vinte e cinco para cada. [p=0.3] Só falta decidir {b}o final. [p=0.3] Nosso número termina em {c}setenta e dois. [p=0.2] Setenta e dois dividido por quatro dá {d}dezoito. [p=0.2] {e}Divisível por quatro."),
    # por três e por nove
    dict(id="s10", block="soma", text="{a}Por três e por nove, a regra é outra: [p=0.2] {b}some todos os algarismos. [p=0.3] Se a soma for divisível por três, o número também é. [p=0.2] O mesmo vale para o nove."),
    dict(id="s11", block="soma", text="{a}Quatro mais cinco mais sete mais dois: [p=0.2] {b}dezoito. [p=0.3] Dezoito se divide por três {c}e por nove. [p=0.3] Então {d}o número inteiro também."),
    dict(id="s12", block="soma", text="E por que a soma funciona? [p=0.2] {a}Dez é nove mais um. [p=0.2] {b}Cem é noventa e nove mais um. [p=0.2] {c}Mil é novecentos e noventa e nove mais um. [p=0.3] Nove, noventa e nove e novecentos e noventa e nove se dividem certinho por nove e por três. [p=0.3] Deixe essa parte de lado: {d}cada casa vale só o seu algarismo. [p=0.2] Por isso a soma decide."),
    # por seis
    dict(id="s13", block="seis", text="{a}Por seis, não tem regra nova. [p=0.2] Seis é dois vezes três, então o número precisa {b}passar nas duas regras. [p=0.3] {c}É par. [p=0.2] E a soma deu {d}dezoito, que se divide por três. [p=0.2] {e}Divisível por seis."),
    dict(id="s14", block="placar", text="Placar final: {a}dois, sim. [p=0.1] {b}Três, sim. [p=0.1] {c}Quatro, sim. [p=0.1] {d}Cinco, não. [p=0.1] {e}Seis, sim. [p=0.1] {f}Nove, sim. [p=0.1] {g}Dez, não. [p=0.3] Só não é divisível por cinco e por dez."),
    # erro
    dict(id="s15", block="erro", text="O erro mais comum é {a}olhar o final no teste do três. [p=0.2] A pessoa pensa: {b}termina em três, então se divide por três. [p=0.3] Mas {c}vinte e três termina em três e deixa resto. [p=0.2] E {d}doze termina em dois e se divide. [p=0.3] No três e no nove, quem manda é {e}a soma, nunca o final."),
    # atalho
    dict(id="s16", block="atalho", text="Aqui está o atalho: [p=0.2] {a}os noves fora. [p=0.3] Na hora de somar, {b}risque os algarismos que juntos dão nove."),
    dict(id="s17", block="atalho", text="{a}Quatro com cinco, nove, risca. [p=0.2] {b}Sete com dois, nove, risca. [p=0.2] {c}Não sobrou nada, [p=0.2] então o número é {d}divisível por nove, e você nem somou até o fim."),
    dict(id="s18", block="atalho", text="Funciona porque {a}tirar nove da soma não muda a resposta: [p=0.2] se sobrar algum algarismo, é só testar o que sobrou. [p=0.3] E como nove é múltiplo de três, riscar {b}vale também para o teste do três."),
    dict(id="s19", block="atalho", text="Quando não compensa? [p=0.2] {a}Quando nenhum grupo de algarismos dá nove, [p=0.2] ou quando o número é curto: {b}some e pronto. [p=0.3] E ele não serve para {c}dois, quatro, cinco ou dez, que olham o final."),
    # questão
    dict(id="s20", block="questao", text="Hora de testar. [p=0.2] Entre {a}dois, três, quatro, cinco, seis, nove e dez, [p=0.2] {b}quais dividem sete mil duzentos e noventa?"),
    dict(id="s21", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="resposta", text="Vamos lá. [p=0.2] Termina em zero: {a}passa por dois, cinco e dez. [p=0.3] Noves fora: {b}sete com dois, risca. [p=0.2] {c}O nove sozinho, risca. [p=0.2] Só sobrou o zero, que não soma nada, então {d}passa por três e por nove. [p=0.3] É par e passou no três: {e}passa por seis."),
    dict(id="s23", block="resposta", text="Falta o quatro. [p=0.2] O final é {a}noventa. [p=0.2] Noventa dividido por quatro dá vinte e dois, e {b}sobram dois. [p=0.3] {c}Só não é divisível por quatro."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}dois, cinco e dez olham o último algarismo, [p=0.2] {b}quatro olha os últimos dois algarismos, [p=0.2] {c}três e nove olham a soma, [p=0.2] {d}e seis junta a regra do dois com a do três."),
    dict(id="s25", block="fim", text="A próxima aula é sobre {a}números primos e fatoração, e essas regras vão trabalhar o tempo todo por lá. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
