# Estudativo · MAT-TOP-007 — Distância de ponto a reta (Matemática · Tópicos Avançados · Distância de ponto a reta e área por determinante).
# Habilidade: calcular a distância de (1, 2) à reta 3x + 4y − 1 = 0 pela fórmula (2).
# Pré-requisitos: MAT-ANA-001 (distância entre dois pontos), MAT-ANA-005 (perpendiculares), MAT-FAV-002 (módulo). Próxima: MAT-TOP-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Pares narrados "xis um, ípsilon dois" (MAT-ANA-001); equação geral como na MAT-ANA-004
# ("tudo de um lado, zero do outro"; á, bê e cê). Sem índice x₀ na fala, para não confundir com o ponto (0, 0).
# Conferência do gancho: na vertical x = 1, a reta passa em y = −1/2, então descer reto mede 2,5; o pé da perpendicular é (−0,2; 0,4).

TITULO = "Distância de ponto a reta"

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
    dict(id="s01", block="gancho", text="Uma casa fica no ponto {a}xis um, ípsilon dois. [p=0.2] Perto dela passa uma estrada reta: {b}três xis mais quatro ípsilon menos um igual a zero. [p=0.3] Descendo na vertical até a estrada, {c}são dois e meio. [p=0.2] Mas existe um caminho mais curto: {d}dois. [p=0.3] E uma fórmula acha esse número {e}em uma linha."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula a distância de um ponto a uma reta [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}três coisas: [p=0.2] {b}a equação geral da reta, com tudo de um lado e zero do outro; [p=0.2] {c}retas perpendiculares, que se cruzam em ângulo reto; [p=0.2] e {d}o módulo, que tira o sinal: módulo de menos sete é sete. [p=0.3] Se faltar alguma, procure no canal."),
    # o menor caminho
    dict(id="s04", block="caminho", text="A distância de um ponto a uma reta é {a}o menor caminho entre eles. [p=0.2] E o menor caminho {b}chega na reta em ângulo reto: [p=0.2] é o segmento perpendicular. [p=0.3] {c}Qualquer outro caminho vira a hipotenusa de um triângulo retângulo, [p=0.2] e {d}a hipotenusa é sempre maior que o cateto."),
    # fórmula
    dict(id="s05", block="formula", text="Achar o ponto onde essa perpendicular toca a reta dá trabalho. [p=0.2] A fórmula pula essa parte. [p=0.3] Escreva a reta na {a}equação geral: á xis mais bê ípsilon mais cê igual a zero. [p=0.3] {b}Em cima, troque o xis e o ípsilon do ponto na equação da reta, [p=0.2] e {c}tire o módulo, porque distância nunca é negativa. [p=0.2] {d}Embaixo, a raiz de á ao quadrado mais bê ao quadrado."),
    dict(id="s06", block="formula", text="No gancho, {a}á vale três, bê vale quatro e cê vale menos um. [p=0.3] {b}Em cima: três vezes um, mais quatro vezes dois, menos um. [p=0.2] {c}Três mais oito menos um dá dez. [p=0.3] {d}Embaixo: três ao quadrado mais quatro ao quadrado dá vinte e cinco, [p=0.2] e a raiz dá cinco. [p=0.3] {e}Dez dividido por cinco: distância dois."),
    # por que funciona
    dict(id="s07", block="sentido", text="Faça um teste: [p=0.2] se o ponto estiver {a}em cima da reta, ele cumpre a equação, [p=0.2] e o número de cima dá {b}zero. [p=0.2] Distância zero: faz sentido. [p=0.3] {c}Quanto mais longe da reta, maior o número de cima. [p=0.2] E {d}o de baixo acerta a escala, conforme a inclinação da reta."),
    dict(id="s08", block="sentido", text="Confira com uma reta fácil: {a}ípsilon igual a três, a reta deitada. [p=0.2] Na geral, {b}ípsilon menos três igual a zero: [p=0.2] á vale zero, bê vale um e cê vale menos três. [p=0.3] Para o ponto {c}xis um, ípsilon sete: [p=0.2] em cima, sete menos três, quatro. [p=0.2] Embaixo, {d}a raiz de zero mais um, que é um. [p=0.3] Distância {e}quatro: [p=0.2] é só contar no quadriculado, de sete até três."),
    # erro
    dict(id="s09", block="erro", text="O erro comum é {a}usar a reta fora da equação geral. [p=0.2] Com {b}ípsilon igual a dois xis mais três, [p=0.2] a pessoa usa á igual a dois, bê igual a um e cê igual a três. [p=0.3] Teste com o ponto xis zero, ípsilon três, que está em cima da reta: [p=0.2] a conta de cima dá {c}seis, e não zero. [p=0.3] O ípsilon estava do outro lado do igual. [p=0.2] Passe tudo para um lado: {d}dois xis menos ípsilon mais três igual a zero. [p=0.3] Agora, {e}á vale dois, bê vale menos um, e cê vale três, [p=0.2] e a conta de cima dá zero."),
    # atalho
    dict(id="s10", block="atalho", text="Agora o atalho, para a {a}distância entre duas retas paralelas. [p=0.2] Com o mesmo á e o mesmo bê, [p=0.2] como {b}três xis mais quatro ípsilon menos um igual a zero [p=0.2] e {c}três xis mais quatro ípsilon mais nove igual a zero, [p=0.3] {d}subtraia os cês e divida pela mesma raiz. [p=0.2] {e}Menos um menos nove dá menos dez: módulo, dez. [p=0.2] Dez dividido por cinco: {f}dois."),
    dict(id="s11", block="atalho", text="Funciona porque, num ponto da primeira reta, {a}três xis mais quatro ípsilon vale um. [p=0.2] Na conta de cima com a segunda reta, sobra {b}um mais nove, dez: [p=0.2] a diferença dos cês. [p=0.3] {c}Só vale com á e bê iguais nas duas. [p=0.2] Se vier {d}seis xis mais oito ípsilon, divida a equação toda por dois antes."),
    # questão
    dict(id="s12", block="questao", text="Hora de testar. [p=0.2] Qual a distância do ponto {a}xis dois, ípsilon menos um, [p=0.2] até a reta {b}cinco xis mais doze ípsilon mais quinze igual a zero?"),
    dict(id="s13", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="resposta", text="Vamos lá. [p=0.2] {a}Em cima: cinco vezes dois, mais doze vezes, abre parênteses, menos um, fecha parênteses, mais quinze. [p=0.2] {b}Dez menos doze mais quinze dá treze. [p=0.3] {c}Embaixo: vinte e cinco mais cento e quarenta e quatro dá cento e sessenta e nove, [p=0.2] e a raiz é treze. [p=0.3] {d}Treze dividido por treze: distância um."),
    # fechamento
    dict(id="s15", block="fim", text="Resumindo: {a}reta na equação geral, [p=0.2] {b}em cima, troque o ponto e tire o módulo, [p=0.2] e {c}embaixo, a raiz de á ao quadrado mais bê ao quadrado."),
    dict(id="s16", block="fim", text="Na próxima aula, uma conta só diz se {a}três pontos estão na mesma reta: [p=0.2] {b}o determinante. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
