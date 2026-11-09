# Estudativo · FIS-ELE-016 — Praticando: resistores e circuitos (Física · Eletricidade · Corrente, Ohm e circuitos · prática).
# Habilidade: resolver circuitos com associações, medidores e curto-circuito.
# Pré-requisitos: FIS-ELE-008 a FIS-ELE-015. Próxima: FIS-ELE-017.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questões inéditas, criadas para esta aula.
# Q1: segunda lei + paralelo de iguais. Q2: mista + medidores ideais. Q3: curto. Q4: ponte de Wheatstone. Q5: casa em paralelo + disjuntor.
# Contas: Q1 20/2 = 10 Ω; 10/2 = 5 Ω = 20/4. Q2 12·6/18 = 72/18 = 4 Ω; 4 + 4 = 8 Ω; 24/8 = 3 A; 4·3 = 12 V; 24 − 12 = 12 V;
#   12/6 = 2 A; 12/12 = 1 A; 2 + 1 = 3. Q3 3·10 = 30 Ω; 30/30 = 1 A; 20 Ω; 30/20 = 1,5 A. Q4 5·Rx = 10·15 = 150 → Rx = 30 Ω;
#   5/10 = 15/30. Q5 220/22 = 10 A; 10 + 10 = 20 A > 15 A.

TITULO = "Praticando: resistores e circuitos"

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
    dict(id="s01", block="gancho", text="{a}Cinco questões inéditas, criadas para esta aula, [p=0.2] com {b}tudo o que você viu sobre resistores e circuitos. [p=0.3] Em cada uma, {c}pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Antes, as ferramentas. [p=0.2] {a}A tensão é a resistência vezes a corrente. [p=0.2] {b}Em série, a corrente é a mesma, e as resistências somam. [p=0.2] {c}Em paralelo, a tensão é a mesma: [p=0.1] produto pela soma, ou o valor dividido pela quantidade, para iguais. [p=0.3] E, {d}no fio, o comprimento está em cima, e a área, embaixo."),
    # questão 1
    dict(id="s03", block="questao1", text="{a}Questão um. [p=0.2] {b}Um fio de vinte ohms é cortado em dois pedaços iguais. [p=0.2] {c}Os pedaços são ligados lado a lado, em paralelo. [p=0.3] {d}Qual é a nova resistência?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}Cada pedaço tem metade do comprimento: [p=0.1] {b}metade da resistência, dez ohms. [p=0.3] {c}Dois iguais em paralelo: dez dividido por dois, [p=0.1] {d}cinco ohms. [p=0.3] {e}Um quarto do fio inteiro: [p=0.1] metade pelo corte, e metade de novo pelo paralelo."),
    # questão 2
    dict(id="s06", block="questao2", text="{a}Questão dois. [p=0.2] Uma fonte de {b}vinte e quatro volts liga {c}um resistor de quatro ohms [p=0.2] em série com {d}doze ohms e seis ohms em paralelo. [p=0.3] {e}Um amperímetro ideal está no ramo dos seis ohms, [p=0.1] e {f}um voltímetro ideal, nas pontas do resistor de quatro. [p=0.3] {g}O que cada um marca?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] {a}Doze e seis em paralelo: setenta e dois dividido por dezoito, quatro ohms. [p=0.2] {b}Mais quatro, em série: oito ohms. [p=0.2] {c}Corrente total: vinte e quatro dividido por oito, três ampères."),
    dict(id="s09", block="resposta2", text="{a}O voltímetro mede a tensão no resistor de quatro ohms: [p=0.1] quatro vezes três, {b}doze volts. [p=0.3] {c}Sobram doze volts no paralelo. [p=0.2] {d}O amperímetro mede a corrente no ramo de seis ohms: [p=0.1] doze dividido por seis, {e}dois ampères. [p=0.3] {f}O ramo de doze ohms leva um ampère: dois mais um, os três da fonte."),
    # questão 3
    dict(id="s10", block="questao3", text="{a}Questão três. [p=0.2] {b}Três resistores de dez ohms estão em série, numa pilha de trinta volts. [p=0.3] {c}Um fio é ligado nas pontas de um deles. [p=0.3] {d}O que acontece com a corrente?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] {a}Antes: trinta ohms, [p=0.1] trinta dividido por trinta, um ampère. [p=0.3] {b}O fio põe esse resistor em curto: [p=0.1] as duas pontas dele ficam com a mesma letra, e {c}ele sai do circuito. [p=0.3] {d}Sobram vinte ohms: [p=0.1] trinta dividido por vinte, {e}um vírgula cinco ampère. [p=0.2] {f}A corrente passou de um para um vírgula cinco ampère."),
    # atalho
    dict(id="s13", block="atalho", text="Uma pausa para o atalho que mais salva tempo: [p=0.2] {a}antes de calcular, estime. [p=0.3] {b}Em série, a equivalente é maior que o maior resistor. [p=0.2] {c}Em paralelo, é menor que o menor. [p=0.3] {d}Se a conta cair fora disso, há um erro, [p=0.2] e {e}várias alternativas caem sem conta nenhuma."),
    # questão 4
    dict(id="s14", block="questao4", text="{a}Questão quatro. [p=0.2] Numa ponte de Wheatstone, {b}o galvanômetro marca zero. [p=0.3] Num lado do losango, ficam {c}cinco ohms em cima e dez ohms embaixo. [p=0.2] No outro, {d}quinze ohms em cima e um desconhecido, erre xis, embaixo. [p=0.3] {e}Quanto vale erre xis?"),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="Vamos lá. [p=0.2] {a}Galvanômetro em zero: ponte em equilíbrio. [p=0.2] {b}O de cinco é oposto ao erre xis, [p=0.1] e o de dez, ao de quinze. [p=0.2] {c}Cinco vezes erre xis igual a dez vezes quinze, cento e cinquenta. [p=0.3] {d}Erre xis vale trinta ohms. [p=0.3] {e}Confira: cinco está para dez assim como quinze está para trinta."),
    # questão 5
    dict(id="s17", block="questao5", text="{a}Questão cinco, sobre a casa. [p=0.2] Num circuito de {b}duzentos e vinte volts, protegido por {c}um disjuntor de quinze ampères, [p=0.2] ligam-se {d}dois aquecedores de vinte e dois ohms, em paralelo. [p=0.3] {e}O disjuntor desarma?"),
    dict(id="s18", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta5", text="Vamos lá. [p=0.2] {a}Em paralelo, cada aquecedor recebe os duzentos e vinte volts. [p=0.2] {b}Duzentos e vinte dividido por vinte e dois: dez ampères em cada um. [p=0.3] {c}Um só ligado, dez ampères: o disjuntor aguenta. [p=0.2] {d}Os dois juntos: vinte ampères, [p=0.1] {e}mais que quinze: desarma."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}reduza o circuito por partes, [p=0.2] {b}ache a corrente total e volte, [p=0.2] {c}fio sem resistor tira o que ele liga do circuito, [p=0.2] e {d}ponte em equilíbrio é produto cruzado."),
    dict(id="s21", block="fim", text="Na próxima aula, começa um assunto novo: [p=0.2] {a}a potência elétrica, [p=0.2] e por que {b}todo resistor esquenta quando a corrente passa. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
