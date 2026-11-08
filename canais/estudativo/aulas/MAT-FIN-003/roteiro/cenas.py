# Estudativo · MAT-FIN-003 — Conta atrasada: multa com juros (Matemática · Matemática Financeira).
# Habilidade: calcular uma conta de R$ 200 paga com 10 dias de atraso, com multa de 2% e mora por dia.
# Pré-requisitos: MAT-FIN-001 (juros simples, taxa e tempo na mesma unidade). Próxima: MAT-FIN-004.
# Questão inédita, criada para esta aula. Boleto e taxas fictícios. Mês comercial de 30 dias, explicado na hora.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Conta atrasada: multa com juros"

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
    dict(id="s01", block="gancho", text="Uma conta de {a}duzentos reais, paga com {b}dez dias de atraso. [p=0.3] No boleto: {c}multa de dois por cento [p=0.1] e {d}juros de mora de três por cento ao mês. [p=0.3] Quanto você paga? [p=0.3] Se deu {e}duzentos e quarenta e dois, [p=0.2] você pagou trinta e seis reais a mais do que devia."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai conferir qualquer conta atrasada, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}uma coisa só: [p=0.2] {b}juros simples, com taxa e tempo na mesma unidade. [p=0.3] Se faltar, procure no canal."),
    # duas cobranças
    dict(id="s04", block="duas", text="Conta atrasada tem {a}duas cobranças diferentes. [p=0.3] A {b}multa é uma punição pelo atraso. [p=0.2] Ela é cobrada {c}uma vez só, [p=0.1] não importa se o atraso foi de um dia ou de um mês. [p=0.2] Em muitas contas de consumo, ela é de dois por cento."),
    dict(id="s05", block="duas", text="Os {a}juros de mora são o aluguel do dinheiro pelos dias de atraso. [p=0.2] Mora quer dizer {b}demora. [p=0.2] Esses juros {c}crescem a cada dia, [p=0.1] e são juros simples, sobre o valor da conta. [p=0.3] Por isso, quanto antes você paga, menos mora."),
    # multa
    dict(id="s06", block="multa", text="{a}Multa: dois por cento de duzentos. [p=0.2] Um por cento é dois reais, então dois por cento são {b}quatro reais."),
    # mora
    dict(id="s07", block="mora", text="Agora a mora. [p=0.2] Na conta de luz e no condomínio, ela costuma ser de um por cento ao mês. [p=0.2] As taxas desta aula são maiores, escolhidas para a conta sair redonda. [p=0.3] A taxa está {a}ao mês, mas o atraso está em dias. [p=0.2] Taxa e tempo precisam da mesma unidade. [p=0.3] Em contas e bancos, se usa {b}o mês comercial, de trinta dias. [p=0.2] {c}Três por cento ao mês, dividido por trinta, [p=0.1] dá {d}zero vírgula um por cento ao dia."),
    dict(id="s08", block="mora", text="{a}Zero vírgula um por cento de duzentos. [p=0.2] Um por cento é dois reais, [p=0.1] e zero vírgula um por cento é {b}a décima parte: vinte centavos por dia. [p=0.3] {c}Em dez dias, dois reais de mora."),
    dict(id="s09", block="mora", text="Dá para conferir pelo mês: [p=0.2] dez dias são {a}um terço do mês. [p=0.2] Um terço de três por cento é {b}um por cento. [p=0.2] E um por cento de duzentos são os mesmos {c}dois reais."),
    # total
    dict(id="s10", block="total", text="Total: {a}duzentos reais da conta. [p=0.2] {b}Mais quatro de multa. [p=0.2] {c}Mais dois de mora. [p=0.3] {d}Duzentos e seis reais."),
    dict(id="s11", block="total", text="Repare no que muda com o tempo. [p=0.2] Com {a}trinta dias de atraso, a mora seria um mês inteiro: seis reais. [p=0.2] A multa continua {b}quatro. [p=0.3] A conta iria a {c}duzentos e dez reais."),
    # erro
    dict(id="s12", block="erro", text="O erro do gancho é {a}cobrar a multa todo dia. [p=0.2] Quatro reais vezes dez dias, {b}quarenta reais. [p=0.2] Com a mora, a conta iria a {c}duzentos e quarenta e dois. [p=0.3] A multa entra {d}uma vez só. [p=0.2] O que cresce com o tempo é {e}só a mora."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}some as porcentagens antes. [p=0.3] {b}Dois por cento de multa, mais um por cento de mora nos dez dias: três por cento. [p=0.2] {c}Três por cento de duzentos dá seis reais. [p=0.2] {d}Duzentos e seis, numa conta só."),
    dict(id="s14", block="atalho", text="Funciona porque multa e mora são calculadas {a}sobre o mesmo valor: a conta original. [p=0.3] Não compensa quando o boleto já traz {b}a mora em reais por dia, [p=0.1] como {c}sete centavos por dia. [p=0.2] Aí, {d}multiplique pelos dias e some."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma conta de internet de {a}cento e cinquenta reais [p=0.1] foi paga com {b}vinte dias de atraso. [p=0.3] {c}Multa de dois por cento [p=0.1] e mora de {d}um vírgula cinco por cento ao mês. [p=0.3] {e}Quanto foi pago?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Multa: dois por cento de cento e cinquenta dá três reais. [p=0.3] Mora ao dia: {b}um vírgula cinco dividido por trinta dá zero vírgula zero cinco por cento. [p=0.2] {c}Em vinte dias, um por cento. [p=0.2] {d}Um por cento de cento e cinquenta dá um real e cinquenta centavos."),
    dict(id="s18", block="resposta", text="Total: {a}cento e cinquenta e quatro reais e cinquenta centavos. [p=0.3] Pelo atalho: {b}dois por cento mais um por cento dá três por cento. [p=0.2] {c}Três por cento de cento e cinquenta dá quatro reais e cinquenta. [p=0.2] Bateu."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}multa, uma vez só. [p=0.2] {b}Mora, por dia, em juros simples. [p=0.2] E {c}tudo sobre o valor da conta."),
    dict(id="s20", block="fim", text="Na próxima aula, {a}os juros compostos: [p=0.2] você descobre por que mil reais a dez por cento ao mês viram {b}mil trezentos e trinta e um em três meses, [p=0.1] e não mil e trezentos. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
