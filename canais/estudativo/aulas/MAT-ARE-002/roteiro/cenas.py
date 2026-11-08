# Estudativo · MAT-ARE-002 — Área do quadrado e do retângulo (Matemática · Áreas e Perímetros).
# Habilidade: contar quadradinhos, usar base vezes altura e calcular quantos pisos de 0,5 m por 0,5 m cobrem um quarto de 4 m por 3 m (48).
# Pré-requisitos: MAT-ARE-001 (perímetro), MAT-MED-004 (metro quadrado, quadradinhos, escada da área). Próxima: MAT-ARE-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Dividir por decimal (MAT-FRA-018) fora da cadeia: os pisos se contam por lado
# (cada metro tem dois pisos) e por metro quadrado (quatro pisos), nunca dividindo por 0,25.
# Letras narradas como em MAT-ANG-017: "á" (área), "bê" (base), "agá" (altura), "éle" (lado).
# Visual:
#   s01, s09-s11: E.retangulo 4 m × 3 m; E.grade com pisos de 0,5 m (8 × 6); no erro, 24 pisos cobrindo só metade, a outra metade vazia em vermelho.
#   s04: E.grade 4 × 3 de quadradinhos de 1 m² entrando fileira a fileira.
#   s05: base (deitada) e altura (em pé) com E.segmento e cota; fórmula A = b · h com legendas.
#   s07: E.quadrado de lado 5 m com 25 quadradinhos; A = ℓ².
#   s08: tábua 2,5 m × 40 cm → 0,4 m; 2,5 · 0,4 = 1 m².
#   s10: um metro quadrado com 2 × 2 pisos.
#   s14-s17: sala quadrada de 6 m; lajotas de 30 cm (20 × 20); rodapé como contorno traçado.

TITULO = "Área do quadrado e do retângulo"

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
    dict(id="s01", block="gancho", text="{a}Um quarto de quatro metros por três metros. [p=0.2] Pisos quadrados de {b}meio metro de lado. [p=0.3] Quantos pisos? [p=0.3] Muita gente pensa: meio metro de lado, então dois pisos por metro quadrado, [p=0.2] e {c}doze metros quadrados vezes dois dá vinte e quatro. [p=0.3] Com vinte e quatro, {d}metade do chão fica sem piso."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula a área de qualquer retângulo e quadrado, [p=0.2] conta pisos sem errar [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}área é quantos quadradinhos cobrem uma superfície, [p=0.2] e o quadradinho padrão é {c}o metro quadrado, um quadrado de um metro de lado. [p=0.3] Se faltar alguma, procure no canal."),
    # contar
    dict(id="s04", block="contar", text="Perímetro é o contorno. [p=0.2] {a}Área é o que fica dentro. [p=0.3] Cubra o chão do quarto com quadradinhos de um metro: [p=0.2] {b}quatro em cada fileira, [p=0.2] {c}três fileiras. [p=0.2] {d}Três vezes quatro dá doze metros quadrados."),
    dict(id="s05", block="contar", text="Ninguém precisa desenhar os quadradinhos. [p=0.2] {a}O lado deitado diz quantos cabem em cada fileira: é a base. [p=0.2] {b}O lado em pé diz quantas fileiras são: é a altura. [p=0.3] Daí a fórmula: {c}á igual a bê vezes agá. [p=0.2] {d}Á é a área, [p=0.1] {e}bê é a base, [p=0.1] {f}agá é a altura."),
    dict(id="s06", block="contar", text="E a unidade? [p=0.2] {a}Metro vezes metro dá metro quadrado. [p=0.2] Por isso o dois pequeno no alto: [p=0.2] {b}são duas medidas multiplicadas. [p=0.3] Centímetro vezes centímetro, {c}centímetro quadrado."),
    # quadrado
    dict(id="s07", block="quadrado", text="No quadrado, base e altura são iguais: {a}lado vezes lado. [p=0.2] Na fórmula, {b}á igual a éle ao quadrado, [p=0.2] e {c}éle é o lado. [p=0.3] É daí que vem o nome ao quadrado. [p=0.2] Lado de cinco metros: {d}cinco ao quadrado dá vinte e cinco metros quadrados."),
    dict(id="s08", block="quadrado", text="Lados em unidades diferentes? [p=0.2] {a}Converta os lados antes. [p=0.2] Uma tábua de {b}dois vírgula cinco metros por quarenta centímetros. [p=0.3] Quarenta centímetros são {c}zero vírgula quatro metro. [p=0.2] {d}Dois vírgula cinco vezes zero vírgula quatro dá um metro quadrado."),
    # pisos
    dict(id="s09", block="pisos", text="Agora os pisos do começo. [p=0.2] No lado de quatro metros, {a}cada metro tem dois pisos de meio metro, [p=0.2] então cabem {b}oito pisos em cada fileira. [p=0.2] No lado de três metros, {c}cabem seis fileiras."),
    dict(id="s10", block="pisos", text="{a}Oito vezes seis dá quarenta e oito pisos. [p=0.3] Outro jeito de ver: [p=0.2] num metro quadrado cabem {b}duas fileiras de dois pisos: são quatro pisos. [p=0.2] {c}Doze metros quadrados vezes quatro dá quarenta e oito. [p=0.2] Bateu."),
    # erro
    dict(id="s11", block="erro", text="O erro do começo é {a}confundir o lado do piso com a área dele. [p=0.2] Meio metro é {b}o lado. [p=0.2] A área é {c}meio vezes meio, que dá um quarto de metro quadrado. [p=0.3] Com dois pisos por metro quadrado, {d}cada metro quadrado fica com metade vazia, [p=0.2] e os vinte e quatro pisos cobrem {e}só metade do quarto."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho para contar pisos: {a}trabalhe com os lados, não com a área. [p=0.3] {b}Quantos pisos cabem no comprimento? [p=0.2] {c}Quantos cabem na largura? [p=0.2] {d}Multiplique."),
    dict(id="s13", block="atalho", text="Funciona porque {a}o chão vira uma grade: fileiras vezes pisos por fileira, [p=0.2] o mesmo raciocínio dos quadradinhos. [p=0.2] E você foge da {b}divisão por número com vírgula. [p=0.3] {c}Não compensa do mesmo jeito quando o piso não cabe um número exato de vezes no lado: [p=0.2] aí, {d}o pedaço que sobra também leva piso, cortado."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Uma sala quadrada tem {a}seis metros de lado. [p=0.3] {b}Quantas lajotas quadradas de trinta centímetros de lado cobrem o chão? [p=0.2] {c}E quantos metros de rodapé contornam a sala, sem descontar a porta?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] Pelo atalho, {a}lados na mesma unidade: seis metros são seiscentos centímetros. [p=0.2] {b}Seiscentos dividido por trinta dá vinte lajotas em cada fileira, [p=0.2] e {c}são vinte fileiras. [p=0.2] {d}Vinte vezes vinte dá quatrocentas lajotas."),
    dict(id="s17", block="resposta", text="O rodapé é {a}o contorno: o perímetro. [p=0.2] {b}Seis vezes quatro dá vinte e quatro metros. [p=0.3] Mesma sala, duas perguntas: [p=0.2] {c}área para o piso, {d}perímetro para o rodapé."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}área do retângulo é base vezes altura, [p=0.2] {b}a do quadrado é lado ao quadrado, [p=0.2] e {c}para contar pisos, veja quantos cabem em cada lado."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai {a}recortar um paralelogramo e transformar num retângulo, [p=0.2] e descobrir por que {b}o triângulo é metade de um paralelogramo. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
