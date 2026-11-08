# Estudativo · MAT-MED-002 — Converter massa e capacidade (Matemática · Medidas e Unidades).
# Habilidade: transformar 1,2 t em kg e 750 mL em L usando a mesma escada.
# Pré-requisitos: MAT-MED-001 (escada do metro). Próxima: MAT-MED-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Litro como decímetro cúbico fica para MAT-MED-005.

TITULO = "Converter massa e capacidade"

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
    dict(id="s01", block="gancho", text="Uma garrafa de {a}setecentos e cinquenta mililitros. [p=0.3] Quantos litros? [p=0.3] Se você respondeu {b}sete vírgula cinco, [p=0.2] sua garrafa ficou do tamanho de {c}quase quatro garrafas de refrigerante de dois litros."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você converte massa e capacidade com {b}a mesma escada do metro, [p=0.2] e ainda leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}uma coisa: [p=0.2] {b}a escada do metro. [p=0.2] Cada degrau, uma casa da vírgula. [p=0.2] Unidade menor, número maior. [p=0.3] Se faltar, procure no canal."),
    # massa
    dict(id="s04", block="massa", text="Massa é o que a balança mede, [p=0.2] o que no dia a dia chamamos de peso. [p=0.3] No meio da escada fica o {a}grama. [p=0.2] E os degraus têm {b}os mesmos começos de nome do metro: [p=0.2] {c}quilograma, hectograma, decagrama, grama, decigrama, centigrama e miligrama."),
    dict(id="s05", block="massa", text="{a}Quilo continua sendo mil: [p=0.2] um quilograma tem {b}mil gramas. [p=0.3] {c}Mili continua sendo milésimo: [p=0.2] um grama tem {d}mil miligramas, [p=0.2] a unidade das doses de remédio."),
    dict(id="s06", block="massa", text="Na padaria, você pede {a}zero vírgula três quilo de queijo. [p=0.2] Do quilo ao grama, três degraus para baixo: [p=0.2] {b}trezentos gramas. [p=0.3] E um comprimido de {c}quinhentos miligramas? [p=0.2] Três degraus para cima: [p=0.2] {d}zero vírgula cinco grama, meio grama."),
    dict(id="s07", block="massa", text="Para escolher a unidade, pense no tamanho: [p=0.2] {a}remédio em miligrama, [p=0.2] {b}gente em quilo, [p=0.2] {c}carga de caminhão em tonelada."),
    # tonelada
    dict(id="s08", block="tonelada", text="Para cargas pesadas, existe uma unidade acima do quilo: a {a}tonelada. [p=0.2] Uma tonelada são {b}mil quilos: [p=0.2] três casas acima do quilo, como o quilo fica três casas acima do grama. [p=0.3] Um carro pequeno tem cerca de {c}uma vírgula duas tonelada. [p=0.2] Quantos quilos?"),
    dict(id="s09", block="tonelada", text="São mil, então a vírgula anda {a}três casas para a direita. [p=0.2] {b}Uma casa: doze. [p=0.2] {c}Duas: cento e vinte. [p=0.2] {d}Três: mil e duzentos. [p=0.3] {e}Mil e duzentos quilos. [p=0.2] Unidade menor, número maior. [p=0.3] E o contrário: {f}oitocentos quilos são {g}zero vírgula oito tonelada."),
    # capacidade
    dict(id="s10", block="capacidade", text="Capacidade é {a}quanto cabe dentro de um recipiente. [p=0.2] No meio da escada fica o {b}litro. [p=0.2] Abaixo dele, os mesmos nomes de novo: [p=0.2] {c}decilitro, centilitro e mililitro."),
    dict(id="s11", block="capacidade", text="{a}Um litro tem mil mililitros. [p=0.2] Uma colher de chá tem cerca de {b}cinco mililitros. [p=0.2] Um copo americano, cerca de cento e noventa. [p=0.3] Uma garrafa de {c}dois litros, descendo três degraus, [p=0.2] tem {d}dois mil mililitros."),
    dict(id="s12", block="capacidade", text="Voltando à garrafa: {a}setecentos e cinquenta mililitros em litros. [p=0.2] Do mililitro ao litro, {b}três degraus para cima. [p=0.2] A vírgula escondida anda {c}três casas para a esquerda."),
    dict(id="s13", block="capacidade", text="{a}Uma casa: setenta e cinco. [p=0.2] {b}Duas: sete vírgula cinco. [p=0.2] {c}Três: zero vírgula setenta e cinco. [p=0.3] {d}Zero vírgula setenta e cinco litro: [p=0.2] menos de um litro, como tinha que ser."),
    # erro
    dict(id="s14", block="erro", text="O erro do começo foi {a}parar no segundo degrau. [p=0.2] A pessoa lembra do centímetro, que dá duas casas, [p=0.2] e anda {b}só duas casas no mililitro também. [p=0.3] Mas {c}mili é milésimo: [p=0.2] são três degraus, {d}três casas. [p=0.3] Confira pelo sentido: o litro é maior que o mililitro, [p=0.2] então {e}o número tem que ficar bem menor."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}pule de mil em mil. [p=0.3] Em massa e capacidade, as provas quase só usam {b}tonelada, quilo, grama e miligrama, [p=0.2] e {c}litro e mililitro. [p=0.3] Entre vizinhos dessa lista, {d}é sempre mil: três casas."),
    dict(id="s16", block="atalho", text="{a}Duas toneladas e meia em gramas? [p=0.2] Dois pulos de mil. [p=0.2] {b}Dois mil e quinhentos quilos. [p=0.2] {c}Dois milhões e quinhentos mil gramas."),
    dict(id="s17", block="atalho", text="Funciona porque os degraus do meio {a}quase não aparecem na vida real. [p=0.3] {b}Não compensa quando surgir centilitro ou decagrama: [p=0.2] aí, volte à escada e conte os degraus."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Um caminhão leva {a}três vírgula cinco toneladas de arroz, [p=0.2] em pacotes de {b}cinco quilos. [p=0.3] {c}Quantos pacotes são?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] Primeiro, a mesma unidade: {a}de tonelada para quilo, três casas. [p=0.2] {b}Três mil e quinhentos quilos. [p=0.3] Depois, os pacotes: {c}três mil e quinhentos dividido por cinco, [p=0.2] {d}setecentos pacotes. [p=0.3] Confira: {e}setecentos vezes cinco dá três mil e quinhentos quilos."),
    dict(id="s21", block="resposta", text="Quem divide sem converter acha {a}zero vírgula sete pacote. [p=0.2] Menos de um pacote num caminhão inteiro: [p=0.2] {b}a unidade ficou para trás."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}a escada é a mesma, [p=0.2] e {b}quilo e mili valem sempre mil."),
    dict(id="s23", block="fim", text="Na próxima aula, a escada ganha prefixos {a}gigantes e minúsculos, como giga e nano, [p=0.2] e você usa {b}polegadas e milhas com o fator que o enunciado dá. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
