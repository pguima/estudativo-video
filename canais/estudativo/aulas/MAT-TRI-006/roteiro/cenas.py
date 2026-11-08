# Estudativo · MAT-TRI-006 — Praticando: razões trigonométricas (Matemática · Trigonometria · prática).
# Habilidade: escolher a razão certa e resolver problemas de altura, rampa e distância com e sem ângulo notável.
# Pré-requisitos: MAT-TRI-001, MAT-TRI-002, MAT-TRI-003, MAT-TRI-004, MAT-TRI-005. Próxima: MAT-TRI-007.
# Questões inéditas, criadas para esta aula. Valores de 37° como em MAT-TRI-002 (tg ≈ 0,75). √3 ≈ 1,7. Seno, cosseno e tangente narrados por extenso.

TITULO = "Praticando: razões trigonométricas"

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
    dict(id="s01", block="gancho", text="{a}Quatro situações, criadas para esta aula: [p=0.2] uma sombra, uma escada, um farol e uma antena. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}as três perguntas: [p=0.2] qual o ângulo, que lado eu conheço, que lado eu quero. [p=0.2] Depois, {b}seno, cosseno ou tangente, [p=0.2] e {c}a tabela de trinta, quarenta e cinco e sessenta graus. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: sombra, sem ângulo notável
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Um poste projeta no chão {b}uma sombra de doze metros. [p=0.2] Os raios de sol chegam fazendo {c}trinta e sete graus com o chão. [p=0.2] Use {d}tangente de trinta e sete graus, cerca de zero vírgula setenta e cinco. [p=0.3] {e}Qual a altura do poste?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}O ângulo de trinta e sete graus fica na ponta da sombra. [p=0.2] {b}A sombra encosta nele: adjacente, doze. [p=0.2] {c}O poste fica de frente: oposto. [p=0.2] {d}Oposto e adjacente: tangente."),
    dict(id="s06", block="resposta1", text="{a}Zero vírgula setenta e cinco igual a xis dividido por doze. [p=0.2] {b}Xis igual a zero vírgula setenta e cinco vezes doze, que dá nove metros. [p=0.3] Um jeito mais rápido: {c}zero vírgula setenta e cinco é três quartos, [p=0.2] e {d}três quartos de doze dá nove."),
    # situação 2: escada, achar o ângulo
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Uma escada de {b}seis metros está apoiada numa parede. [p=0.2] O pé da escada fica a {c}três metros da parede. [p=0.3] {d}Que ângulo a escada faz com o chão?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] O ângulo procurado fica {a}no pé da escada. [p=0.2] {b}A escada é a hipotenusa: seis. [p=0.2] {c}Os três metros do chão encostam no ângulo: adjacente. [p=0.2] {d}Adjacente e hipotenusa: cosseno. [p=0.2] {e}Três dividido por seis dá um meio."),
    dict(id="s10", block="resposta2", text="Que ângulo tem cosseno um meio? [p=0.2] {a}Sessenta graus. [p=0.3] Cuidado com a armadilha: [p=0.2] quem vê um meio e lembra só do seno responde {b}trinta graus. [p=0.2] Mas {c}seno de trinta é um meio; [p=0.2] {d}cosseno um meio é sessenta. [p=0.2] Sempre veja {e}qual razão você montou."),
    # situação 3: farol, distância inacessível
    dict(id="s11", block="questao3", text="{a}Situação três. [p=0.2] De um barco, uma pessoa vê o topo de um farol sob {b}trinta graus. [p=0.2] O farol tem {c}vinte metros de altura. [p=0.3] {d}A que distância o barco está do pé do farol? [p=0.2] Use raiz de três perto de um vírgula sete."),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] {a}O ângulo de trinta fica no barco. [p=0.2] {b}O farol fica de frente: oposto, vinte. [p=0.2] {c}A distância encosta no ângulo: adjacente. [p=0.2] Oposto e adjacente: tangente. [p=0.3] Mas aqui {d}o atalho da metade do equilátero é mais rápido."),
    dict(id="s14", block="resposta3", text="{a}De frente para o trinta, o menor lado: o farol, vinte metros. [p=0.2] {b}De frente para o sessenta, o menor vezes raiz de três. [p=0.2] {c}A distância é vinte raiz de três. [p=0.2] {d}Vinte vezes um vírgula sete dá trinta e quatro: pouco mais de trinta e quatro metros."),
    dict(id="s15", block="resposta3", text="Pela tangente, sai o mesmo: [p=0.2] {a}raiz de três dividido por três igual a vinte dividido por xis. [p=0.2] {b}Multiplique cada lado por três e por xis: raiz de três vezes xis igual a sessenta. [p=0.2] {c}Xis igual a sessenta dividido por raiz de três. [p=0.2] Tirando a raiz de baixo, {d}sessenta raiz de três dividido por três, que dá vinte raiz de três."),
    # situação 4: antena, hipotenusa
    dict(id="s16", block="questao4", text="{a}Última situação. [p=0.2] Uma antena de {b}quinze metros vai ser presa por um cabo, [p=0.2] esticado do topo até o chão. [p=0.2] O cabo faz {c}trinta graus com o chão. [p=0.3] {d}Quanto mede o cabo?"),
    dict(id="s17", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta4", text="Vamos lá. [p=0.2] {a}O cabo é a hipotenusa, e é o que falta. [p=0.2] {b}A antena fica de frente para o ângulo de trinta: oposto, quinze. [p=0.2] {c}Oposto e hipotenusa: seno. [p=0.2] {d}Um meio igual a quinze dividido por xis. [p=0.2] {e}Xis igual a trinta metros."),
    dict(id="s19", block="resposta4", text="Pelo atalho, {a}a hipotenusa é o dobro do lado de frente para o trinta: [p=0.2] {b}duas vezes quinze dá trinta. [p=0.3] Quem multiplicou {c}quinze por um meio achou sete e meio, [p=0.2] um cabo {d}mais curto que a antena. [p=0.2] Impossível: {e}com a hipotenusa procurada, divida."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}dê nome aos lados a partir do ângulo; [p=0.2] {b}com ângulo da tabela, use a tabela ou o atalho; [p=0.2] {c}fora da tabela, use o valor que a prova der; [p=0.2] e {d}confira se a resposta faz sentido."),
    dict(id="s21", block="fim", text="Na próxima aula, a trigonometria sai do triângulo. [p=0.2] Você mede ângulos numa unidade nova, {a}o radiano, [p=0.2] e transforma {b}sessenta graus em pi terços. [p=0.3] E conhece {c}o ciclo trigonométrico, onde trezentos e noventa graus caem no mesmo ponto que trinta. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
