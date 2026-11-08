# Estudativo · MAT-CNT-006 — Permutação com repetição e em círculo (Matemática · Contagem e Probabilidade · Permutações, arranjos e combinações).
# Habilidade: contar os anagramas de ARARA (10) e as formas de 5 pessoas sentarem numa mesa redonda (24).
# Pré-requisitos: MAT-CNT-005 (permutação simples). Próxima: MAT-CNT-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; letras narradas como se falam (á, erre, ene, bê).
# Questão inédita, criada para esta aula. Corte de fatoriais como em MAT-CNT-004.
# ANA com ás coloridos: 3! = 6; cada anagrama real aparece 2! = 2 vezes → 6 ÷ 2 = 3 (ANA, AAN, NAA).
# ARARA: A × 3, R × 2 → 5!/(3! · 2!) = (5 × 4 = 20) ÷ 2 = 10. Erro: 5!/3! = 20 (esquece o R).
# Mesa de 5: fila 5! = 120; cada arrumação aparece 5 vezes (giros) → 120 ÷ 5 = 24 = 4!. Atalho: fixe uma pessoa → (n − 1)!.
# Questão: BANANA (A × 3, N × 2, B × 1) → 6!/3! = 6 × 5 × 4 = 120; ÷ 2 = 60 · mesa de 6 → 5! = 120.

TITULO = "Permutação com repetição e em círculo"

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
    dict(id="s01", block="gancho", text="{a}Quantos anagramas tem a palavra arara? [p=0.3] Cinco letras, então {b}cinco fatorial, que dá cento e vinte? [p=0.3] {c}Não. [p=0.2] São só {d}dez."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você conta anagramas com letras repetidas, [p=0.2] {b}pessoas em volta de uma mesa redonda [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}a permutação: [p=0.2] coisas todas diferentes em fila dão {b}o fatorial da quantidade. [p=0.3] E vai {c}cortar fatoriais numa divisão. [p=0.3] Se faltar alguma, procure no canal."),
    # repetição: exemplo pequeno
    dict(id="s04", block="ana", text="Comece pequeno: [p=0.2] {a}a palavra ana. [p=0.3] Finja que os ás são diferentes: [p=0.2] {b}um vermelho e um azul. [p=0.2] Com três letras diferentes, seriam {c}três fatorial, que dá seis anagramas."),
    dict(id="s05", block="ana", text="Agora apague as cores. [p=0.2] {a}Á vermelho, ene, á azul [p=0.2] e {b}á azul, ene, á vermelho [p=0.2] viram {c}a mesma palavra. [p=0.3] Cada anagrama de verdade foi contado {d}duas vezes: [p=0.2] uma para cada ordem dos ás."),
    dict(id="s06", block="ana", text="Então divida: {a}seis dividido por dois dá três. [p=0.3] São eles: [p=0.2] {b}á, ene, á. [p=0.2] {c}Á, á, ene. [p=0.2] {d}Ene, á, á."),
    # regra
    dict(id="s07", block="regra", text="A regra: {a}faça a conta como se tudo fosse diferente [p=0.2] e {b}divida pelo fatorial de cada repetição. [p=0.3] Letra que aparece três vezes: {c}divide por três fatorial. [p=0.2] Letra que aparece duas vezes: {d}divide por dois fatorial. [p=0.3] Por que fatorial? [p=0.2] Três ás coloridos trocam de lugar de três fatorial jeitos, [p=0.2] e todos esses jeitos dão a mesma palavra."),
    # arara
    dict(id="s08", block="arara", text="Em arara, o á aparece {a}três vezes, [p=0.2] e o erre aparece {b}duas. [p=0.3] Fica {c}cinco fatorial dividido por três fatorial vezes dois fatorial."),
    dict(id="s09", block="arara", text="Corte como você já sabe: [p=0.2] {a}cinco fatorial dividido por três fatorial deixa cinco vezes quatro, [p=0.2] que dá {b}vinte. [p=0.3] {c}Vinte dividido por dois fatorial, que é dois, [p=0.2] dá {d}dez anagramas."),
    # erro
    dict(id="s10", block="erro", text="O erro comum é {a}dividir só por uma repetição. [p=0.2] A pessoa vê os três ás, [p=0.2] faz {b}cinco fatorial dividido por três fatorial [p=0.2] e para em {c}vinte. [p=0.3] Mas {d}os erres também trocam de lugar sem mudar a palavra. [p=0.2] {e}Toda letra repetida divide. [p=0.2] Sem dividir pelo erre, cada palavra aparece duas vezes, uma para cada ordem dos erres."),
    # mesa redonda
    dict(id="s11", block="mesa", text="Agora, a mesa redonda. [p=0.2] {a}Cinco pessoas vão sentar em volta de uma mesa redonda. [p=0.3] Ali, o que importa é {b}quem está à direita e quem está à esquerda de cada um."),
    dict(id="s12", block="mesa", text="Imagine todo mundo {a}levantando e sentando uma cadeira para a direita, junto. [p=0.3] {b}Cada pessoa continua com o mesmo vizinho à direita e o mesmo vizinho à esquerda. [p=0.2] Para a mesa, {c}é a mesma arrumação. [p=0.2] Gire de novo, e de novo: [p=0.2] depois de cinco giros, todo mundo volta ao lugar."),
    dict(id="s13", block="mesa", text="Em fila, seriam {a}cinco fatorial, que dá cento e vinte. [p=0.3] Mas cada arrumação da mesa aparece ali {b}cinco vezes, uma para cada giro. [p=0.3] {c}Cento e vinte dividido por cinco dá vinte e quatro."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}fixe uma pessoa. [p=0.3] Ela senta em qualquer lugar e {b}vira a referência. [p=0.2] As outras quatro fazem uma fila a partir dela: [p=0.2] {c}quatro fatorial dá vinte e quatro. [p=0.3] Mesma resposta, sem dividir."),
    dict(id="s15", block="atalho", text="Funciona porque {a}fixar uma pessoa elimina os giros. [p=0.3] Por isso, mesa redonda é {b}o fatorial de um a menos: [p=0.2] oito pessoas, sete fatorial. [p=0.3] {c}Não vale se as cadeiras forem numeradas: [p=0.2] aí, girar muda a arrumação, [p=0.2] e a conta volta a ser {d}a de fila."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Quantos anagramas tem a palavra banana? [p=0.3] E de quantas formas {b}seis amigos podem sentar em volta de uma mesa redonda?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Banana tem {a}seis letras: [p=0.2] o á aparece três vezes, [p=0.2] o ene, duas vezes, [p=0.2] e o bê, uma. [p=0.3] {b}Seis fatorial dividido por três fatorial deixa seis vezes cinco vezes quatro, [p=0.2] que dá {c}cento e vinte. [p=0.2] {d}Dividido por dois dá sessenta anagramas."),
    dict(id="s19", block="resposta", text="Na mesa, {a}fixe um amigo. [p=0.2] Os outros cinco fazem fila a partir dele: [p=0.2] {b}cinco fatorial dá cento e vinte formas. [p=0.3] Em fila, seriam seis fatorial, que dá setecentos e vinte: [p=0.2] seis vezes mais."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}letra repetida, divida pelo fatorial da repetição. [p=0.3] {b}Mesa redonda, fixe uma pessoa e faça a fila com as outras."),
    dict(id="s21", block="fim", text="Até aqui, {a}todo mundo entrava na fila. [p=0.3] Na próxima aula, você escolhe {b}só alguns: [p=0.2] o pódio, com três corredores entre oito, [p=0.2] e testa {c}se trocar a ordem muda o resultado. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
