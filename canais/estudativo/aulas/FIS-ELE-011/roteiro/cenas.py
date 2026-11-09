# Estudativo · FIS-ELE-011 — Resistores em série (Física · Eletricidade · Corrente, Ohm e circuitos).
# Habilidade: calcular a resistência equivalente somando, sabendo que a corrente é a mesma e a tensão se divide.
# Pré-requisitos: FIS-ELE-009 (U = R·i, tensão como ddp). Próxima: FIS-ELE-012.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fato do gancho: nos pisca-piscas antigos, as lâmpadas ficavam em série, e uma queimada apagava a fileira toda.
# Req = R1 + R2 sai de U = R1·i + R2·i = (R1 + R2)·i (fator comum, MAT-FAT-002). Atalho: divisor de tensão por partes (frações).
# Contas: 2 + 4 = 6 Ω; 12/6 = 2 A; 2·2 = 4 V; 4·2 = 8 V; 4 + 8 = 12; 2/6 = 1/3 → 4 V; 2/3 de 12 = 8 V.
#   Questão: 3 + 5 + 12 = 20 Ω; 40/20 = 2 A; 12·2 = 24 V; 12/20 = 3/5; 3/5 de 40 = 24; 6 + 10 + 24 = 40.

TITULO = "Resistores em série"

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
    dict(id="s01", block="gancho", text="{a}Nos pisca-piscas antigos de Natal, [p=0.2] {b}bastava uma lâmpada queimar [p=0.1] para {c}a fileira inteira apagar. [p=0.3] {d}A culpa era do jeito de ligar: [p=0.1] em série."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular {b}a resistência equivalente de resistores em série, [p=0.2] {c}a corrente [p=0.1] e {d}a tensão em cada um."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a primeira lei de Ohm, em que a tensão u, em volt, é a resistência erre, em ohm, vezes a corrente i, em ampère; [p=0.2] e {c}que a tensão é uma diferença de potencial entre dois pontos. [p=0.3] Se faltar alguma, procure no canal."),
    # série
    dict(id="s04", block="serie", text="{a}Resistor é a peça feita para ter resistência. [p=0.2] Ligar em série é ligar {b}um atrás do outro, [p=0.1] no mesmo fio, [p=0.2] de modo que {c}a corrente só tem um caminho."),
    dict(id="s05", block="serie", text="Daí sai a primeira regra: [p=0.2] {a}a corrente é a mesma em todos. [p=0.3] Pense numa {b}fila única, sem desvio: [p=0.2] quem passa pelo primeiro {c}passa, obrigatoriamente, pelos outros. [p=0.3] {d}Nenhuma carga se perde no caminho."),
    dict(id="s06", block="serie", text="Segunda regra: [p=0.2] {a}a tensão da pilha se divide. [p=0.3] Cada resistor fica com {b}um pedaço, [p=0.2] e {c}os pedaços somam a tensão total."),
    # equivalente
    dict(id="s07", block="equivalente", text="Com isso, sai a {a}resistência equivalente: [p=0.2] o único resistor que, no lugar de todos, {b}deixa passar a mesma corrente com a mesma tensão. [p=0.3] {c}A tensão total é erre um vezes i, mais erre dois vezes i. [p=0.2] {d}Coloque o i em evidência: [p=0.1] erre um mais erre dois, tudo vezes i."),
    dict(id="s08", block="equivalente", text="Então, {a}em série, a equivalente é a soma: [p=0.2] {b}erre equivalente igual a erre um, mais erre dois, mais erre três, [p=0.1] quantos houver. [p=0.3] {c}Ela é sempre maior que o maior resistor."),
    # exemplo
    dict(id="s09", block="exemplo", text="Um exemplo. [p=0.2] Uma pilha de {a}doze volts liga {b}dois ohms e quatro ohms em série. [p=0.3] {c}A equivalente é seis ohms. [p=0.2] {d}A corrente é doze dividido por seis: [p=0.1] {e}dois ampères, a mesma nos dois."),
    dict(id="s10", block="exemplo", text="Agora, a tensão em cada um, com u igual a erre vezes i. [p=0.2] {a}No de dois ohms: dois vezes dois, quatro volts. [p=0.2] {b}No de quatro ohms: quatro vezes dois, oito volts. [p=0.3] {c}Quatro mais oito, doze: [p=0.1] a tensão da pilha. [p=0.3] Repare: {d}o resistor maior fica com a maior tensão."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que a corrente vai se gastando, [p=0.2] e que {b}sai do último resistor menos corrente do que entra no primeiro. [p=0.3] {c}Não: a corrente é a mesma do começo ao fim. [p=0.2] {d}O que cai de um resistor para o outro é o potencial: [p=0.1] cada um fica com um pedaço da tensão."),
    dict(id="s12", block="erro", text="E é por isso que o pisca-pisca apagava: [p=0.2] {a}lâmpada queimada é fio cortado. [p=0.2] {b}Sem caminho, a corrente para em todas."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho: [p=0.2] {a}em série, a tensão se divide na proporção das resistências. [p=0.3] {b}Dois e quatro ohms: [p=0.1] são seis partes. [p=0.2] {c}O de dois fica com dois sextos, [p=0.1] um terço dos doze volts: {d}quatro volts. [p=0.2] {e}O de quatro fica com dois terços: oito volts. [p=0.3] {f}Sem calcular a corrente."),
    dict(id="s14", block="atalho", text="Funciona porque {a}a corrente é a mesma em todos, [p=0.2] então a tensão em cada um é proporcional à resistência dele. [p=0.3] {b}Não compensa quando a questão pede a corrente também: [p=0.2] aí, faça pela lei de Ohm, que a corrente já sai no caminho."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma fonte de {a}quarenta volts liga em série {b}três ohms, [p=0.1] cinco ohms [p=0.1] e doze ohms. [p=0.3] {c}Qual é a corrente? [p=0.2] E {d}qual é a tensão no resistor de doze ohms?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}A equivalente é três mais cinco mais doze: [p=0.1] vinte ohms. [p=0.2] {b}A corrente é quarenta dividido por vinte: [p=0.1] {c}dois ampères. [p=0.3] {d}No de doze ohms: doze vezes dois, [p=0.1] {e}vinte e quatro volts."),
    dict(id="s18", block="resposta", text="{a}Pelo atalho: doze de vinte partes, [p=0.1] três quintos de quarenta: [p=0.1] vinte e quatro de novo. [p=0.3] {b}Os outros ficam com seis e dez volts, [p=0.2] e {c}seis mais dez mais vinte e quatro dá quarenta."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: em série, {a}a corrente é a mesma, [p=0.2] {b}a tensão se divide [p=0.2] e {c}a resistência equivalente é a soma."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai ligar resistores {a}lado a lado, em paralelo, [p=0.2] e ver por que, ali, {b}a equivalente diminui. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
