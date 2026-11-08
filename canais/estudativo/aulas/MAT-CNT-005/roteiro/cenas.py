# Estudativo · MAT-CNT-005 — Permutação simples: filas e anagramas (Matemática · Contagem e Probabilidade · Permutações, arranjos e combinações).
# Habilidade: contar os anagramas de AMOR (24) e as filas com duas pessoas sempre juntas.
# Pré-requisitos: MAT-CNT-002 (comece pela casinha mais difícil), MAT-CNT-004 (fatorial). Próxima: MAT-CNT-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; letras narradas como se falam (á, eme, ó, erre).
# Questão inédita, criada para esta aula. Letras repetidas e mesa redonda ficam para MAT-CNT-006.
# AMOR: 4 letras distintas → 4 × 3 × 2 × 1 = 4! = 24. Na tela, a regra pode vir como P = n! (n = quantidade); narrada sem letra.
# 5 amigos, Ana e Bia juntas: bloco + 3 = 4 peças → 4! = 24; × 2! = 48. Erro: 24 (esquece a troca dentro do bloco).
# Atalho: separadas = 5! − juntas = 120 − 48 = 72.
# Questão: BRASIL (6 letras distintas) → 6! = 720 · vogais A e I juntas: bloco + B, R, S, L = 5 peças → 120 × 2 = 240.

TITULO = "Permutação simples: filas e anagramas"

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
    dict(id="s01", block="gancho", text="{a}Amor. [p=0.2] {b}Roma. [p=0.2] {c}Ramo. [p=0.2] {d}Mora. [p=0.3] Todas usam as mesmas letras, só que em outra ordem. [p=0.3] Quantas palavras dá para formar assim, com ou sem sentido? [p=0.3] Contar nos dedos cansa. [p=0.2] Com casinhas, é uma linha: [p=0.2] {e}Vinte e quatro."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você conta filas e anagramas, [p=0.2] inclusive {b}com gente que tem que ficar junta, [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}duas coisas: [p=0.2] {b}começar pela casinha mais difícil [p=0.2] e {c}o fatorial: [p=0.2] o número vezes todos os de baixo, até o um. [p=0.3] Se faltar alguma, procure no canal."),
    # anagrama
    dict(id="s04", block="anagrama", text="{a}Anagrama é cada ordem possível das letras de uma palavra, [p=0.2] contando a própria palavra. [p=0.3] Vale {b}com ou sem sentido: [p=0.2] {c}erre, eme, ó, á também conta, mesmo sem significar nada."),
    dict(id="s05", block="anagrama", text="Amor tem {a}quatro letras diferentes: [p=0.2] {b}á, eme, ó, erre. [p=0.3] Faça {c}quatro casinhas. [p=0.2] Na primeira, cabem {d}quatro letras. [p=0.2] Na segunda, {e}sobram três. [p=0.2] Depois, {f}duas [p=0.2] e {g}uma."),
    dict(id="s06", block="anagrama", text="{a}Quatro vezes três vezes dois vezes um [p=0.2] é {b}quatro fatorial, [p=0.2] que dá {c}vinte e quatro anagramas."),
    dict(id="s07", block="anagrama", text="E se o anagrama tivesse que {a}começar com á? [p=0.2] Comece pela casinha difícil: [p=0.2] {b}a primeira só aceita o á, uma opção. [p=0.3] As outras três letras se arrumam nas casinhas que sobram: [p=0.2] {c}três fatorial dá seis. [p=0.2] São {d}seis anagramas de amor que começam com á."),
    # regra
    dict(id="s08", block="regra", text="Trocar de lugar coisas todas diferentes se chama {a}permutação. [p=0.3] O total é sempre {b}o fatorial da quantidade. [p=0.2] Por quê? [p=0.2] Cada casinha tem uma opção a menos que a anterior, [p=0.2] porque quem já entrou não entra de novo. [p=0.3] Vale para letras, para livros na prateleira [p=0.2] e para {c}pessoas em fila. [p=0.2] Cinco pessoas em fila? [p=0.2] {d}Cinco fatorial dá cento e vinte filas."),
    # juntas
    dict(id="s09", block="juntas", text="Agora, uma regra no meio. [p=0.2] {a}Cinco amigos vão tirar foto em fila, [p=0.2] e {b}Ana e Bia querem ficar sempre juntas. [p=0.3] Quantas filas existem?"),
    dict(id="s10", block="juntas", text="O truque é {a}colar Ana e Bia, como se fossem uma pessoa só: [p=0.2] onde uma vai, a outra vai junto. [p=0.3] A fila agora tem {b}o bloco [p=0.2] e {c}mais três amigos. [p=0.2] São {d}quatro peças: [p=0.2] {e}quatro fatorial dá vinte e quatro."),
    dict(id="s11", block="juntas", text="Mas dentro do bloco {a}elas podem trocar de lugar: [p=0.2] {b}Ana e Bia, [p=0.2] ou {c}Bia e Ana. [p=0.2] São {d}dois fatorial, que dá duas ordens. [p=0.3] {e}Vinte e quatro vezes dois dá quarenta e oito filas."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}esquecer a troca dentro do bloco [p=0.2] e responder {b}vinte e quatro. [p=0.3] Mas a foto com Ana à esquerda de Bia é {c}diferente da foto com Bia à esquerda de Ana. [p=0.2] O bloco sempre {d}multiplica pelas ordens de dentro."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, para quando a prova pede o contrário: [p=0.2] {a}Ana e Bia separadas. [p=0.3] Não conte as separadas. [p=0.2] {b}Conte todas e tire as juntas. [p=0.2] Todas: {c}cinco fatorial dá cento e vinte. [p=0.2] {d}Cento e vinte menos quarenta e oito dá setenta e dois. [p=0.2] É mais rápido que contar as separadas casinha por casinha."),
    dict(id="s14", block="atalho", text="Funciona porque {a}cada fila cai em um grupo só: [p=0.2] ou elas estão juntas, ou separadas. [p=0.3] Não compensa quando a regra é {b}um lugar fixo, como Ana na ponta esquerda da fila: [p=0.2] aí, {c}comece pela casinha da Ana: [p=0.2] uma opção para ela, e quatro fatorial para os outros."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Quantos anagramas tem a palavra Brasil? [p=0.3] E em quantos deles {b}as vogais ficam juntas?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Brasil tem {a}seis letras diferentes: [p=0.2] {b}bê, [p=0.2] erre, [p=0.2] á, [p=0.2] esse, [p=0.2] i, [p=0.2] ele. [p=0.2] Nenhuma repete, então vale o fatorial. [p=0.3] {c}Seis fatorial dá setecentos e vinte anagramas."),
    dict(id="s18", block="resposta", text="Para as vogais juntas, {a}cole o á com o i em um bloco. [p=0.2] Ficam {b}o bloco e mais quatro consoantes: cinco peças. [p=0.2] {c}Cinco fatorial dá cento e vinte. [p=0.3] Dentro do bloco, {d}o á e o i podem trocar de lugar: [p=0.2] {e}cento e vinte vezes dois dá duzentos e quarenta. [p=0.3] Faz sentido ser menos que setecentos e vinte: [p=0.2] ficar junto é uma exigência a mais."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}coisas todas diferentes em fila, use o fatorial. [p=0.3] {b}Tem que ficar junto? Cole em bloco e multiplique pelas trocas de dentro."),
    dict(id="s20", block="fim", text="E se a palavra tiver {a}letras repetidas, como arara? [p=0.3] Ou se a fila virar {b}uma mesa redonda? [p=0.2] É a próxima aula. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
