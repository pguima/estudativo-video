# Estudativo · MAT-RAZ-010 — Proporcional ao quadrado (Matemática · Razão e Proporção).
# Habilidade: explicar por que dobrar o lado quadruplica a área.
# Pré-requisitos: MAT-MED-004 (converter área), MAT-POT-004 (potência de um produto), MAT-RAZ-005 (teste do dobro). Próxima: MAT-RAZ-011.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Regra de três não está no "Já ensinado": a aula não usa.
# Lado 3 → 9 m²; lado 6 → 36 m² = 4 · 9 (erro: 18). (2 · L)² = 2² · L² = 4 · L². Lado 9 → 81 = 9 · 9. Lado 1,5 → 2,25 = 9/4.
# Retângulo 3 × 2 = 6; 6 × 4 = 24 = 4 · 6; só a largura: 6 × 2 = 12 = 2 · 6.
# Erro: foto 10 × 15 = 150 cm²; ampliada 3 vezes: 30 × 45 = 1.350 = 9 · 150 (erro: 3 · 150 = 450).
# Questão: lado 4 → 16 m²; triplo do lado: 16 · 9 = 144 = 12 · 12.

TITULO = "Proporcional ao quadrado"

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
    dict(id="s01", block="gancho", text="{a}Uma sala quadrada de três metros de lado leva nove metros quadrados de piso. [p=0.3] {b}Outra sala tem o dobro do lado. [p=0.2] Dezoito metros quadrados? [p=0.3] {c}Não. [p=0.2] {d}Trinta e seis."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você explica por que dobrar o lado quadruplica a área, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}três coisas: [p=0.2] {b}um metro quadrado é um quadradinho de um metro de lado, [p=0.2] {c}o teste do dobro, [p=0.2] e {d}o expoente de fora do parêntese vai para cada número da multiplicação. [p=0.3] Se faltar alguma, procure no canal."),
    # área do quadrado
    dict(id="s04", block="area", text="Área é {a}quantos quadradinhos cabem na figura. [p=0.3] Num quadrado de três metros de lado, cabem {b}três fileiras de três quadradinhos: [p=0.2] {c}três vezes três dá nove metros quadrados. [p=0.3] Por isso a área do quadrado é {d}lado vezes lado, [p=0.2] ou seja, {e}o lado ao quadrado."),
    dict(id="s05", block="area", text="Agora dobre o lado: {a}seis metros. [p=0.2] {b}Seis vezes seis dá trinta e seis metros quadrados. [p=0.3] Olhe o desenho: {c}cabem quatro quadrados iguais ao primeiro. [p=0.2] {d}Trinta e seis é quatro vezes nove."),
    dict(id="s06", block="area", text="Por que quatro? [p=0.2] Porque o lado aparece {a}duas vezes na conta. [p=0.3] {b}A largura dobrou, e a altura também dobrou. [p=0.2] {c}Duas vezes duas dá quatro."),
    dict(id="s07", block="area", text="Com potência, fica mais claro. [p=0.2] O lado novo é {a}dois vezes o lado. [p=0.2] A área nova é {b}abre parênteses, dois vezes o lado, fecha parênteses, ao quadrado. [p=0.3] O expoente vai para cada número: {c}dois ao quadrado vezes o lado ao quadrado. [p=0.2] {d}Quatro vezes a área antiga."),
    # a regra
    dict(id="s08", block="regra", text="Pelo teste do dobro, {a}dobrou o lado, e a área nem dobrou nem caiu pela metade. [p=0.2] Então a área {b}não é proporcional ao lado. [p=0.3] Mas ela segue uma regra fixa: [p=0.2] é {c}proporcional ao quadrado do lado. [p=0.2] Quando o lado ao quadrado fica quatro vezes maior, a área também fica."),
    dict(id="s09", block="regra", text="Quer dizer: {a}multiplicou o lado por um número, [p=0.2] {b}a área fica multiplicada por esse número ao quadrado. [p=0.3] {c}Lado vezes três: área vezes nove. [p=0.2] Um quadrado de nove metros de lado tem {d}oitenta e um metros quadrados, [p=0.1] nove vezes os nove do começo."),
    dict(id="s10", block="regra", text="E para menos também. [p=0.2] {a}Lado pela metade: [p=0.2] um meio ao quadrado é {b}um quarto. [p=0.2] {c}A área cai para um quarto. [p=0.2] Não é a metade."),
    dict(id="s11", block="regra", text="Vale para {a}qualquer figura ampliada por inteiro. [p=0.3] {b}Um retângulo de três metros por dois tem seis metros quadrados. [p=0.2] {c}Dobrando a largura e a altura, seis por quatro: vinte e quatro. [p=0.2] {d}Quatro vezes a área. [p=0.3] Na física, a distância que um carro leva para frear também segue {e}o quadrado da velocidade, [p=0.2] mas isso fica para outra aula."),
    # erro comum
    dict(id="s12", block="erro", text="O erro comum é {a}multiplicar a área pelo mesmo número do lado. [p=0.3] {b}Uma foto de dez por quinze centímetros tem cento e cinquenta centímetros quadrados. [p=0.2] Ampliada com o triplo de cada lado, a pessoa diz {c}quatrocentos e cinquenta."),
    dict(id="s13", block="erro", text="Mas a foto nova mede {a}trinta por quarenta e cinco. [p=0.2] {b}Mil trezentos e cinquenta centímetros quadrados. [p=0.3] {c}Nove vezes a área antiga, porque três ao quadrado é nove."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: [p=0.2] {a}ache o fator do lado e eleve ao quadrado. [p=0.3] Lado vezes dois, {b}área vezes quatro. [p=0.2] Lado vezes três, {c}área vezes nove. [p=0.2] Lado vezes dez, {d}área vezes cem. [p=0.3] Funciona porque o fator {e}entra duas vezes: uma na largura, outra na altura."),
    dict(id="s15", block="atalho", text="{a}Só vale quando todas as medidas mudam pelo mesmo fator. [p=0.3] Se só a largura dobra, {b}seis por dois, [p=0.2] a área vai de seis para {c}doze: [p=0.2] aí ela só dobra. [p=0.3] E o volume de uma caixa ampliada segue o cubo, {d}assunto de outra aula."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Um piso quadrado de quatro metros de lado usou dezesseis metros quadrados de porcelanato. [p=0.3] {b}Outro piso quadrado tem o triplo do lado. [p=0.2] {c}Quantos metros quadrados de porcelanato ele usa?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Lado vezes três, então {a}área vezes três ao quadrado, nove. [p=0.2] {b}Dezesseis vezes nove: cento e quarenta e quatro metros quadrados. [p=0.3] Conferindo: o lado novo é {c}doze metros, [p=0.2] e {d}doze vezes doze dá cento e quarenta e quatro. [p=0.2] Bateu."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}área é lado vezes lado, [p=0.2] então {b}o fator do lado entra duas vezes: [p=0.2] {c}dobra o lado, quadruplica a área."),
    dict(id="s20", block="fim", text="Na próxima aula, você lê {a}uma fórmula inteira como proporcionalidade, [p=0.2] e diz o que acontece com o resultado quando {b}uma letra dobra e outra cai pela metade. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
