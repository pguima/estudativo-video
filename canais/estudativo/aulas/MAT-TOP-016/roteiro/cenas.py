# Estudativo · MAT-TOP-016 — Troncos de pirâmide e de cone (Matemática · Tópicos Avançados · Troncos e transformações geométricas).
# Habilidade: cortar um cone de volume 81 a 1/3 da altura, a partir do vértice, e achar o volume do tronco subtraindo o cone menor (81 − 3 = 78).
# Pré-requisitos: MAT-ESP-020 (razão entre volumes: k³, "cá"). Usa MAT-ESP-011 e MAT-ESP-013 (volume da pirâmide e do cone: área da
#   base vezes a altura, dividido por três) e MAT-POT-007 (raiz quadrada). Próxima: MAT-TOP-017.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Letra k narrada "cá"; h narrada "agá".
# Questão inédita, criada para esta aula. Fórmula do tronco: V = h/3 · (B + r{B·b} + b), com B e b as áreas das bases.
# Contas: (1/3)³ = 1/27; 81/27 = 3; 81 − 3 = 78. Pirâmide: 36 · 9 / 3 = 108; k = 6/9 = 2/3; 108 · 8/27 = 32; 108 − 32 = 76;
#   direto: lado 4, altura 6: 16 · 6 / 3 = 32. Fórmula: h = 3, r{36 · 16} = 24, 3/3 · (36 + 24 + 16) = 76. Erro: 81/3 = 27, 81 − 27 = 54.
#   Questão: (1/4)³ = 1/64; 640/64 = 10; 640 − 10 = 630. r{25 · 9} = 15; 6/3 · (25 + 15 + 9) = 2 · 49 = 98.

TITULO = "Troncos de pirâmide e de cone: volume sem decorar"

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
    dict(id="s01", block="gancho", text="Um cone tem volume {a}oitenta e um. [p=0.2] Corte esse cone {b}a um terço da altura, contando da ponta. [p=0.3] A ponta que sai fica com um terço do volume, vinte e sete? [p=0.2] {c}Não: só três. [p=0.3] E o resto, {d}o tronco, fica com setenta e oito."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula o volume de troncos de cone e de pirâmide [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o volume do cone e o da pirâmide são a área da base vezes a altura, dividido por três; [p=0.2] e {c}em sólidos semelhantes, se as medidas são multiplicadas por cá, o volume é multiplicado por cá ao cubo. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="tronco", text="Corte um cone {a}com um plano paralelo à base. [p=0.2] Em cima, sai {b}um cone menor. [p=0.2] Embaixo, fica {c}o tronco de cone: [p=0.2] um sólido com {d}duas bases redondas, uma grande e uma pequena. [p=0.3] É o formato de {e}um balde, ou de um copo descartável."),
    dict(id="s05", block="tronco", text="Com a pirâmide, é igual. [p=0.2] {a}O corte paralelo à base deixa um tronco de pirâmide, [p=0.2] com {b}duas bases do mesmo formato, uma maior que a outra."),
    # o método
    dict(id="s06", block="metodo", text="Como achar o volume do tronco? [p=0.2] {a}O volume do sólido inteiro, {b}menos o volume da ponta que saiu."),
    dict(id="s07", block="metodo", text="No cone do começo, o corte foi {a}a um terço da altura, a partir da ponta. [p=0.2] A ponta é {b}um cone semelhante ao grande, [p=0.2] com {c}cá igual a um terço. [p=0.3] {d}Um terço ao cubo é um vinte e sete avos. [p=0.2] {e}Oitenta e um dividido por vinte e sete: três."),
    dict(id="s08", block="metodo", text="{a}O tronco fica com oitenta e um menos três: [p=0.2] {b}setenta e oito."),
    # pirâmide
    dict(id="s09", block="piramide", text="Agora, uma pirâmide de {a}base quadrada, com lado seis e altura nove. [p=0.2] Volume: {b}seis vezes seis, trinta e seis, [p=0.2] vezes nove, dividido por três: {c}cento e oito."),
    dict(id="s10", block="piramide", text="Agora, corte a ponta {a}a seis de altura, contando do vértice. [p=0.2] {b}Cá é seis nonos, que simplifica para dois terços. [p=0.2] {c}Dois terços ao cubo: oito vinte e sete avos. [p=0.2] {d}Cento e oito vezes oito vinte e sete avos: trinta e dois. [p=0.3] {e}Tronco: cento e oito menos trinta e dois, setenta e seis."),
    dict(id="s11", block="piramide", text="Confira sem o cá: [p=0.2] a pirâmide de cima tem {a}lado quatro, que é dois terços de seis, e altura seis. [p=0.2] {b}Dezesseis vezes seis, dividido por três: trinta e dois. [p=0.2] Bateu."),
    # erro
    dict(id="s12", block="erro", text="Agora, cuidado com o erro mais comum: [p=0.2] {a}achar que cortar a um terço da altura tira um terço do volume. [p=0.2] A pessoa faz {b}oitenta e um dividido por três, vinte e sete, [p=0.2] e responde {c}cinquenta e quatro para o tronco."),
    dict(id="s13", block="erro", text="Mas a ponta encolhe {a}nas três direções: [p=0.2] na altura, na largura e na profundidade. [p=0.2] {b}Um terço, vezes um terço, vezes um terço: um vinte e sete avos. [p=0.3] A ponta é pequena, e quase todo o volume {c}fica no tronco."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho, para quando a questão dá {a}só o tronco: [p=0.2] a área da base grande, {b}bê maiúsculo; [p=0.2] a da base pequena, {c}bê minúsculo; [p=0.2] e a altura do tronco, {d}agá. [p=0.3] O volume é {e}agá dividido por três, vezes a soma de três áreas: [p=0.2] a grande, a pequena, {f}e a raiz da grande vezes a pequena."),
    dict(id="s15", block="atalho", text="Na pirâmide da aula: {a}base grande trinta e seis, base pequena dezesseis, [p=0.2] e altura do tronco nove menos seis, três. [p=0.3] {b}A raiz de trinta e seis vezes dezesseis é seis vezes quatro, vinte e quatro. [p=0.2] {c}Três dividido por três dá um, [p=0.2] vezes trinta e seis mais vinte e quatro mais dezesseis: [p=0.2] {d}setenta e seis, de novo."),
    dict(id="s16", block="atalho", text="Funciona porque a fórmula é {a}a mesma subtração, já feita, [p=0.2] sem precisar da altura do sólido inteiro. [p=0.3] {b}Não compensa quando a questão já dá o sólido inteiro e o corte: [p=0.2] aí, {c}subtrair a ponta é mais rápido."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar, em duas partes. [p=0.2] {a}Um cone de seiscentos e quarenta mililitros é cortado a um quarto da altura, a partir da ponta. [p=0.2] Quanto cabe no tronco? [p=0.3] E {b}um tronco de pirâmide tem bases de áreas vinte e cinco e nove, e altura seis. [p=0.2] Qual é o volume?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Cá é um quarto, e um quarto ao cubo é um sessenta e quatro avos. [p=0.2] {b}Seiscentos e quarenta dividido por sessenta e quatro: dez mililitros na ponta. [p=0.2] {c}No tronco, seiscentos e trinta mililitros."),
    dict(id="s20", block="resposta", text="No tronco de pirâmide, {a}a raiz de vinte e cinco vezes nove é cinco vezes três, quinze. [p=0.2] {b}Seis dividido por três dá dois. [p=0.2] {c}Dois vezes, abre parênteses, vinte e cinco mais quinze mais nove: [p=0.2] dois vezes quarenta e nove, {d}noventa e oito."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}tronco é o sólido inteiro menos a ponta; [p=0.2] {b}a ponta encolhe com cá ao cubo; [p=0.2] e, {c}sem o sólido inteiro, use a fórmula do tronco."),
    dict(id="s22", block="fim", text="Na próxima aula, você amplia uma figura {a}a partir de um ponto, como a luz de um projetor, [p=0.2] e vê por que dobrar os comprimentos {b}deixa a área quatro vezes maior. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
