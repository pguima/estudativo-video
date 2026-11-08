# Estudativo · MAT-ANA-005 — Retas paralelas e perpendiculares (Matemática · Geometria Analítica · Equação da reta).
# Habilidade: usar que paralelas têm o mesmo m e perpendiculares têm m₁ · m₂ = −1 e achar a paralela a y = 2x que passa por (0, 3).
# Pré-requisitos: MAT-ANA-004 (reduzida y = mx + n). Usa também MAT-FRA-009 (multiplicar frações). Próxima: MAT-ANA-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas: "eme" (m), "ene" (n), "erre" (reta r). Na tela, m₁ · m₂ = −1; na voz, "o produto das inclinações".
# Evitado "três meios" (soa "três e meio"): os exemplos do atalho usam inteiros e frações de numerador um.

TITULO = "Retas paralelas e perpendiculares"

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
    dict(id="s01", block="gancho", text="{a}Ípsilon igual a dois xis mais um [p=0.2] e {b}ípsilon igual a menos um meio xis mais quatro. [p=0.3] Essas retas se cruzam em {c}ângulo reto, um canto perfeito de esquadro. [p=0.3] E dá para saber {d}sem desenhar nada: [p=0.2] basta olhar {e}o dois e o menos um meio."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você reconhece retas paralelas e perpendiculares pelo eme [p=0.2] e {b}acha a equação de cada uma, [p=0.2] com um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}uma coisa: [p=0.2] {b}a equação reduzida, ípsilon igual a eme xis mais ene, [p=0.2] em que {c}o eme é a inclinação [p=0.2] e {d}o ene é o corte no eixo ípsilon. [p=0.3] Se faltar, procure no canal."),
    # paralelas
    dict(id="s04", block="paralelas", text="Retas {a}paralelas nunca se encontram, [p=0.2] como os trilhos de um trem. [p=0.3] Para isso, elas {b}precisam ter a mesma inclinação. [p=0.2] Se uma subisse mais que a outra, {c}em algum momento elas se cruzariam."),
    dict(id="s05", block="paralelas", text="Então, {a}paralelas têm o mesmo eme, [p=0.2] e só o ene muda. [p=0.3] Se o ene também for igual, {b}é a mesma reta, desenhada duas vezes."),
    dict(id="s06", block="paralelas", text="A paralela a {a}ípsilon igual a dois xis que passa por {b}xis zero, ípsilon três: [p=0.2] o eme é {c}dois, igual ao da reta dada. [p=0.2] O ponto está no eixo ípsilon, então {d}o ene é três. [p=0.3] {e}Ípsilon igual a dois xis mais três: [p=0.2] {f}três unidades acima da reta dada."),
    # perpendiculares
    dict(id="s07", block="perpendiculares", text="E retas {a}perpendiculares, que se cruzam em ângulo reto? [p=0.3] Pegue a reta de eme dois: {b}anda um, sobe dois. [p=0.2] Agora, {c}gire esse degrau um quarto de volta, [p=0.2] como quem vira um esquadro."),
    dict(id="s08", block="perpendiculares", text="Depois do giro, {a}o que era subida vira andada, [p=0.2] e {b}o que era andada vira descida. [p=0.3] O degrau novo {c}anda dois e desce um. [p=0.2] {d}Eme igual a menos um dividido por dois, que dá menos um meio."),
    dict(id="s09", block="perpendiculares", text="Repare no que aconteceu com o dois: [p=0.2] {a}ele virou de cabeça para baixo, um meio, [p=0.2] e {b}trocou de sinal. [p=0.3] Multiplique as inclinações: {c}dois vezes menos um meio dá menos um. [p=0.3] {d}Em retas perpendiculares, o produto das inclinações dá menos um, [p=0.2] desde que nenhuma delas seja uma reta em pé, que não tem eme."),
    dict(id="s10", block="perpendiculares", text="Vamos achar a perpendicular a {a}ípsilon igual a dois xis mais um [p=0.2] que passa por {b}xis dois, ípsilon zero. [p=0.2] O eme é {c}menos um meio. [p=0.2] Troque o ponto: {d}zero igual a menos um meio vezes dois, mais ene. [p=0.2] {e}Zero igual a menos um mais ene, [p=0.2] e o ene dá um. [p=0.3] {f}Ípsilon igual a menos um meio xis mais um."),
    # erro
    dict(id="s11", block="erro", text="Agora, cuidado com o erro mais comum: [p=0.2] {a}trocar só o sinal. [p=0.3] Para a perpendicular à reta de eme dois, a pessoa usa {b}eme igual a menos dois. [p=0.2] Mas {c}dois vezes menos dois dá menos quatro. [p=0.2] O produto não deu menos um. [p=0.3] No desenho, {d}as retas se cruzam tortas, sem canto reto. [p=0.2] {e}Troque o sinal e também vire o número."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: [p=0.2] {a}inverte e troca o sinal. [p=0.3] {b}Dois vira menos um meio. [p=0.2] {c}Menos três vira um terço. [p=0.2] {d}Menos um quarto vira quatro."),
    dict(id="s13", block="atalho", text="Funciona porque {a}um número vezes ele mesmo de cabeça para baixo dá um, [p=0.2] e {b}a troca de sinal deixa o produto negativo: menos um. [p=0.3] {c}Não funciona com a reta deitada, de eme zero, como ípsilon igual a três: [p=0.2] zero não vira de cabeça para baixo. [p=0.2] A perpendicular a ela é {d}uma reta em pé, como xis igual a dois, que não tem eme. [p=0.2] Nesse par não existe produto de inclinações: é o caso em que a regra não vale."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] A reta erre é {a}ípsilon igual a menos três xis mais cinco. [p=0.3] {b}Ache a paralela a erre que passa por xis um, ípsilon quatro. [p=0.2] E {c}a perpendicular a erre que passa por xis três, ípsilon dois."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] Paralela: {a}o mesmo eme, menos três. [p=0.2] Troque o ponto: {b}quatro igual a menos três mais ene, [p=0.2] e o ene dá sete. [p=0.3] {c}Ípsilon igual a menos três xis mais sete."),
    dict(id="s17", block="resposta", text="Perpendicular: {a}menos três, invertido e com o sinal trocado, vira um terço. [p=0.2] Troque o ponto: {b}dois igual a um terço vezes três, mais ene. [p=0.2] {c}Dois igual a um mais ene, [p=0.2] e o ene dá um. [p=0.3] {d}Ípsilon igual a um terço xis mais um. [p=0.2] Conferindo: {e}menos três vezes um terço dá menos um. [p=0.2] Bateu."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}paralelas têm o mesmo eme, [p=0.2] {b}em perpendiculares o produto das inclinações dá menos um, [p=0.2] e {c}para achar a perpendicular, inverta e troque o sinal."),
    dict(id="s19", block="fim", text="Na próxima aula, você acha {a}o ponto exato onde duas retas se cruzam, [p=0.2] resolvendo {b}um sistema de equações. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
