# Estudativo · MAT-ARE-008 — Área do círculo, da coroa e do setor (Matemática · Áreas e Perímetros).
# Habilidade: usar A = πr² e achar a área de uma coroa de raios 5 e 3 (16π) e de um setor de 90° e raio 4 (4π).
# Pré-requisitos: MAT-ARE-002 (base vezes altura), MAT-POL-005 (arco como fração da volta, tabela e cruz). Usa MAT-POL-004 (volta 2πr, π como letra). Próxima: MAT-ARE-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas como se falam: "á", "érre". Termos de MAT-POL-004/005: "a volta", "pi", "ângulo central".
# Contas: pizzas 20² = 400 → 400π contra 2 · 10² = 200π (com π = 3: 1.200 contra 600). Coroa 25π − 9π = 16π (erro: (5 − 3)²π = 4π).
#   Setor 90°, r = 4: 16π · 90/360 = 4π. Questão: 120°, r = 6: 36π/3 = 12π = 36 m²; tabela 120 · 36 = 4.320, ÷ 360 = 12.
# Visual:
#   s01, s07: pizza de raio 20 ao lado de duas de raio 10 (E.circulo), as áreas em π.
#   s04-s06: E.circulo cortado em 8 e depois 16 fatias (E.circulo setor); as fatias se encaixam alternadas numa faixa quase retangular,
#            altura r, base πr (metade da volta em cima, metade embaixo); fórmula A = πr² com legendas.
#   s08-s09, s12: coroa de raios 5 e 3 (dois E.circulo concêntricos, anel pintado); no erro, um círculo de raio 2 em vermelho ao lado.
#   s10-s11, s13: setor de 90° e raio 4 (E.circulo setor); tabela 360° → 16π, 90° → x; depois 1/4 da pizza.
#   s15-s18: irrigador no centro, setor de 120° e raio 6 m pintado sobre a grama.

TITULO = "Área do círculo, da coroa e do setor"

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
    dict(id="s01", block="gancho", text="{a}Uma pizza grande, com {b}vinte centímetros de raio. [p=0.2] Ou {c}duas pizzas pequenas, de dez centímetros de raio cada uma. [p=0.3] Parece a mesma coisa. [p=0.3] Mas a grande tem {d}o dobro de pizza das pequenas juntas."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula a área de um círculo, [p=0.2] de um anel [p=0.2] e de uma fatia, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}a volta da circunferência mede dois pi érre; [p=0.2] {c}o arco é a mesma fração da volta que o ângulo central; [p=0.2] e {d}a área do retângulo é base vezes altura. [p=0.3] Se faltar alguma, procure no canal."),
    # de onde vem a fórmula
    dict(id="s04", block="formula", text="{a}A área do círculo é a região de dentro, pintada. [p=0.2] Para medir, {b}corte o círculo em muitas fatias finas, como uma pizza. [p=0.3] Depois, {c}encaixe as fatias lado a lado: [p=0.2] uma com a ponta para cima, a seguinte com a ponta para baixo."),
    dict(id="s05", block="formula", text="A figura vira {a}quase um retângulo. [p=0.2] Quanto mais fatias, mais reta ela fica. [p=0.3] {b}A altura é o raio, o comprimento de cada fatia. [p=0.2] {c}A base é metade da borda da pizza: [p=0.2] metade da volta, {d}pi érre."),
    dict(id="s06", block="formula", text="Base vezes altura: {a}pi érre vezes érre. [p=0.2] Daí a fórmula: {b}á igual a pi érre ao quadrado. [p=0.3] {c}Á é a área, [p=0.2] {d}érre é o raio, [p=0.2] e {e}pi é o mesmo pi da volta, perto de três vírgula catorze."),
    dict(id="s07", block="formula", text="Voltando às pizzas. [p=0.2] Raio vinte: {a}vinte ao quadrado dá quatrocentos, então a área é quatrocentos pi. [p=0.3] Raio dez: {b}dez ao quadrado dá cem, então cada pequena tem cem pi. [p=0.2] {c}Juntas, duzentos pi. [p=0.3] Quatrocentos pi é {d}o dobro. [p=0.2] O raio entra {e}ao quadrado, e é isso que engana o olho."),
    # coroa
    dict(id="s08", block="coroa", text="{a}Coroa é o anel entre duas circunferências com o mesmo centro, [p=0.2] como {b}um disco com um furo redondo no meio. [p=0.3] A área dela é {c}o círculo de fora menos o furo."),
    dict(id="s09", block="coroa", text="Raios {a}cinco e três. [p=0.2] {b}Círculo de fora: pi vezes cinco ao quadrado dá vinte e cinco pi. [p=0.2] {c}Furo: pi vezes três ao quadrado dá nove pi. [p=0.3] {d}Vinte e cinco pi menos nove pi dá dezesseis pi. [p=0.2] O pi se comporta {e}como uma letra: termos semelhantes."),
    # setor
    dict(id="s10", block="setor", text="{a}Setor é uma fatia do círculo: [p=0.2] a região entre dois raios e o arco. [p=0.3] Como no arco, {b}dobrou o ângulo central, a área dobra. [p=0.2] Área e ângulo são {c}diretamente proporcionais."),
    dict(id="s11", block="setor", text="Setor de {a}noventa graus e raio quatro. [p=0.2] {b}Círculo inteiro: pi vezes quatro ao quadrado dá dezesseis pi. [p=0.3] Na tabela, {c}trezentos e sessenta graus para dezesseis pi; [p=0.2] {d}noventa graus para xis. [p=0.2] Cruz: {e}trezentos e sessenta xis igual a noventa vezes dezesseis pi, que dá mil quatrocentos e quarenta pi. [p=0.2] {f}Xis igual a quatro pi."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum está na coroa: {a}subtrair os raios antes. [p=0.2] Cinco menos três dá dois, [p=0.2] e a pessoa faz {b}pi vezes dois ao quadrado, que dá quatro pi. [p=0.3] Mas um anel de largura dois {c}não é um círculo de raio dois. [p=0.2] {d}Calcule cada círculo inteiro e só depois subtraia, [p=0.2] e o anel dá dezesseis pi."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, para o setor: [p=0.2] {a}transforme o ângulo em fração da volta, como você fez no arco. [p=0.3] {b}Noventa graus é um quarto da volta. [p=0.2] {c}Um quarto de dezesseis pi dá quatro pi. [p=0.2] Sem cruz."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o setor é a mesma fração do círculo que o ângulo é da volta. [p=0.3] {b}Não compensa com ângulo quebrado, como cinquenta graus: [p=0.2] aí, {c}monte a tabela."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Um irrigador de jardim {a}gira cento e vinte graus [p=0.2] e molha até {b}seis metros de distância. [p=0.3] {c}Que área de grama ele molha? [p=0.2] {d}Use pi igual a três."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] A região molhada é {a}um setor de raio seis. [p=0.2] {b}Círculo inteiro: pi vezes seis ao quadrado dá trinta e seis pi. [p=0.3] {c}Cento e vinte graus é um terço da volta. [p=0.2] {d}Um terço de trinta e seis pi dá doze pi, [p=0.2] que com pi igual a três fica {e}doze vezes três, e dá trinta e seis metros quadrados."),
    dict(id="s18", block="resposta", text="Pela tabela, sai o mesmo. [p=0.2] {a}Trezentos e sessenta graus para trinta e seis pi; [p=0.2] {b}cento e vinte graus para xis. [p=0.2] {c}Trezentos e sessenta xis igual a cento e vinte vezes trinta e seis pi, que dá quatro mil trezentos e vinte pi. [p=0.2] Dividindo por trezentos e sessenta, {d}xis igual a doze pi. [p=0.2] Bateu."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}círculo, pi érre ao quadrado. [p=0.2] {b}Coroa, o círculo de fora menos o de dentro. [p=0.2] {c}Setor, a fração do círculo que o ângulo é da volta."),
    dict(id="s20", block="fim", text="Na próxima aula, você junta e recorta figuras: [p=0.2] {a}um retângulo com meio círculo em cima, com área e contorno, [p=0.2] e {b}a área sombreada numa malha quadriculada. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
