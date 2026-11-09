# Estudativo · FIS-ELE-009 — Resistência e primeira lei de Ohm (Física · Eletricidade · Corrente, Ohm e circuitos).
# Habilidade: usar U = R·i, com a tensão como ddp, e reconhecer no gráfico um resistor ôhmico.
# Pré-requisitos: FIS-ELE-008 (corrente), FIS-ELE-004 (ddp), MAT-FUN-013 (função linear). Próxima: FIS-ELE-010.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Potência e efeito Joule com fórmula são de outras aulas: aqui só "esquenta".
# Gráfico U (vertical) × i (horizontal): ôhmico = reta pela origem; filamento de lâmpada = curva que fica mais inclinada
# (R cresce com a temperatura). Ω escrito na fonte pesada. Contas: 220/11 = 20 A; 10/2 = 20/4 = 5 Ω; 12/0,5 = 24 Ω;
# 36/24 = 1,5 A.

TITULO = "Resistência e primeira lei de Ohm"

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
    dict(id="s01", block="gancho", text="{a}O chuveiro elétrico tem uma peça chamada resistência. [p=0.2] Quando ela queima, {b}a água sai fria. [p=0.3] Mas {c}o que é resistência, [p=0.1] e como ela controla a corrente?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai usar {b}U igual a R vezes i [p=0.2] e {c}reconhecer num gráfico um resistor ôhmico."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}corrente é a carga que passa por segundo, em ampère; [p=0.2] e {c}a tensão U é a diferença de potencial, em volt. [p=0.3] Se faltar alguma, procure no canal."),
    # tensão e resistência
    dict(id="s04", block="resistencia", text="A tensão é o que {a}empurra a corrente. [p=0.2] Sem diferença de potencial entre as pontas de um fio, [p=0.1] {b}não há corrente. [p=0.3] Pense num cano de água: [p=0.1] {c}a tensão é o desnível, [p=0.1] e {d}a corrente é quanta água passa por segundo."),
    dict(id="s05", block="resistencia", text="Mas cada material {a}dificulta a passagem de um jeito. [p=0.2] Os elétrons esbarram nos átomos, [p=0.1] e {b}a peça esquenta. [p=0.3] Essa dificuldade é a {c}resistência elétrica, a letra R. [p=0.2] Uma peça feita para ter resistência é um {d}resistor, [p=0.1] como o do chuveiro."),
    # lei de Ohm
    dict(id="s06", block="ohm", text="Para muitos resistores, vale a {a}primeira lei de Ohm: [p=0.2] {b}U igual a R vezes i. [p=0.3] {c}U é a tensão, em volt; [p=0.2] {d}R é a resistência; [p=0.2] {e}i é a corrente, em ampère. [p=0.3] A unidade de R é {f}volt por ampère, que se chama ohm, [p=0.1] com a letra grega ômega."),
    dict(id="s07", block="ohm", text="Um chuveiro de {a}duzentos e vinte volts tem resistência de {b}onze ohms. [p=0.3] {c}Duzentos e vinte é onze vezes i: [p=0.2] {d}i é duzentos e vinte dividido por onze, [p=0.1] {e}vinte ampères."),
    dict(id="s08", block="ohm", text="Com a resistência fixa, {a}tensão e corrente são diretamente proporcionais. [p=0.2] {b}Dobrou a tensão? A corrente dobra. [p=0.2] Triplicou? Triplica. [p=0.3] Um resistor assim se chama {c}ôhmico."),
    # gráfico
    dict(id="s09", block="grafico", text="No gráfico da tensão pela corrente, [p=0.2] {a}o resistor ôhmico é uma reta que passa pela origem: [p=0.1] {b}é a função linear, U igual a R vezes i. [p=0.3] {c}Dois ampères, dez volts; [p=0.1] {d}quatro ampères, vinte volts. [p=0.2] {e}R é dez dividido por dois, cinco ohms, [p=0.1] em qualquer ponto da reta."),
    dict(id="s10", block="grafico", text="Já {a}o filamento de uma lâmpada esquenta muito, [p=0.1] e {b}a resistência dele muda. [p=0.3] Quanto mais quente, maior a resistência, [p=0.1] e {c}o gráfico vira uma curva cada vez mais inclinada: [p=0.1] {d}é um resistor não ôhmico. [p=0.3] Nele, não existe um R só: [p=0.2] {e}em cada ponto, R é a tensão dividida pela corrente daquele ponto."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que a resistência cresce com a tensão. [p=0.3] Vendo {b}R igual a U dividido por i, a pessoa pensa: [p=0.1] dobrou o U, dobrou o R. [p=0.3] {c}Mas, no resistor ôhmico, a corrente dobra junto, [p=0.1] e {d}R fica igual. [p=0.2] {e}No resistor ôhmico, R depende da peça, não da tensão."),
    # atalho
    dict(id="s12", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}o triângulo do U R i. [p=0.2] {b}U em cima, R e i embaixo. [p=0.3] {c}Tampe o que você quer achar. [p=0.2] {d}Tampou o U, sobra R vezes i; [p=0.2] {e}tampou o R, sobra U dividido por i; [p=0.2] {f}tampou o i, sobra U dividido por R."),
    dict(id="s13", block="atalho", text="Funciona porque {a}é a mesma fórmula, isolada de três jeitos. [p=0.3] {b}No resistor não ôhmico, não use o R de um ponto em outro: [p=0.2] lá, o triângulo vale ponto a ponto."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Um resistor ôhmico recebe {a}doze volts e é percorrido por {b}meio ampère. [p=0.3] {c}Qual é a resistência? [p=0.2] {d}E qual será a corrente se a tensão subir para trinta e seis volts?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}R é U dividido por i: [p=0.1] {b}doze dividido por zero vírgula cinco, [p=0.2] {c}vinte e quatro ohms. [p=0.3] Dividir por meio é dobrar."),
    dict(id="s17", block="resposta", text="{a}A tensão triplicou: de doze para trinta e seis. [p=0.2] {b}No resistor ôhmico, a corrente triplica também: [p=0.1] {c}um vírgula cinco ampère. [p=0.3] {d}Confira: trinta e seis dividido por vinte e quatro, um vírgula cinco."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}U é R vezes i; [p=0.2] {b}a resistência se mede em ohm; [p=0.2] e {c}o resistor ôhmico é uma reta pela origem no gráfico da tensão pela corrente."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai ver {a}a segunda lei de Ohm: [p=0.2] {b}como o comprimento, a espessura e o material do fio mudam a resistência. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
