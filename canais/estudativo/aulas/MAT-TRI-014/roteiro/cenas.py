# Estudativo · MAT-TRI-014 — Mexer na onda: y = a + b · cos(cx) (Matemática · Trigonometria · Ciclo e funções trigonométricas).
# Habilidade: dizer o que a, b e c fazem com a onda e ler em y = 1 + 2 · cos(2x) o máximo 3, o mínimo −1 e o período π.
# Pré-requisitos: MAT-TRI-011 (onda do cosseno: período 2π, imagem [−1, 1]; número na frente estica a altura). Usa também MAT-EQU-007 (fazer o mesmo nos dois lados). Próxima: MAT-TRI-012.
# Questão inédita, criada para esta aula. Letras narradas "á", "bê", "cê", "xis"; cosseno e seno por extenso; π narrado "pi"; π/2 narrado "pi meios", como na MAT-TRI-007.
# b: 2 cos x → [−2, 2], amplitude 2 · a: 1 + 2 cos x → topo 2 → 3, fundo −2 → −1, linha do meio y = 1.
# c: cos(2x) fecha a volta quando 2x = 2π → x = π · período 2π ÷ c.
# Juntando: y = 1 + 2 cos(2x) · máximo 1 + 2 = 3 · mínimo 1 − 2 = −1 · período π · imagem [−1, 3].
# Erro: período 2π · 2 = 4π (multiplicar pelo c).
# Atalho: máx = a + b, mín = a − b, período = 2π ÷ c · b negativo: use b sem sinal (3 − 2 cos x: máx 5, mín 1, amplitude 2; a onda vira de cabeça para baixo) · c negativo: período com |c|.
# Questão: y = 2 + 3 sen(4x) · máx 5 · mín −1 · período 2π/4 = π/2 (90°) · imagem [−1, 5].
# Visual (E.plano, E.curva):
#   s01: a fórmula grande com á, bê e cê coloridos em cores diferentes.
#   s04: y = a + b · cos(cx) com uma etiqueta embaixo de cada letra.
#   s05: cos x apagada ao fundo e 2 cos x por cima; seta vertical da linha do meio ao topo = "amplitude".
#   s06: 2 cos x subindo inteira 1 unidade; linha do meio tracejada em y = 1; topo 3 e fundo −1 marcados.
#   s07-s08: cos x e cos(2x) lado a lado no mesmo eixo; duas ondas cabendo onde cabia uma; 2x = 2π → x = π.
#   s09: gráfico final de 1 + 2 cos(2x) com máximo, mínimo, período e a sombra de −1 a 3.
#   s11: "4π" riscado em vermelho.
#   s12-s13: os três cartões do atalho; 3 − 2 cos x de cabeça para baixo.
#   s13.f: cartão "cê negativo: período com o cê sem sinal" (ex.: cos(−2x) = cos(2x), período π).
#   s14-s16: gráfico de 2 + 3 sen(4x).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Mexer na onda: y = a + b · cos(cx)"

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
    dict(id="s01", block="gancho", text="{a}Ípsilon igual a um, mais duas vezes o cosseno de dois xis. [p=0.3] Parece assustador, [p=0.2] mas {b}cada número ali tem uma tarefa só. [p=0.3] Quem conhece as tarefas lê o máximo, o mínimo e o período {c}em segundos."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você sabe o que cada número faz com a onda [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}uma coisa: [p=0.2] {b}o gráfico do cosseno é uma onda que começa no alto, [p=0.2] vai de menos um a um [p=0.2] e se repete a cada dois pi. [p=0.3] {c}Um número na frente estica a altura. [p=0.3] Se faltar, procure no canal."),
    # forma geral
    dict(id="s04", block="forma", text="A forma geral é {a}ípsilon igual à letra á, mais bê vezes o cosseno de cê xis. [p=0.3] {b}Três letras e três tarefas. [p=0.2] E tudo o que vale aqui {c}vale igual para o seno."),
    # bê
    dict(id="s05", block="be", text="Comece pelo {a}bê, o número na frente do cosseno. [p=0.2] Você já conhece: {b}ele estica a altura. [p=0.2] {c}Duas vezes o cosseno de xis vai de menos dois a dois. [p=0.3] A distância do meio da onda até o topo se chama {d}amplitude. [p=0.2] Aqui, {e}a amplitude é dois."),
    # á
    dict(id="s06", block="a", text="Em seguida, o {a}á, o número somado. [p=0.2] Ele {b}empurra a onda inteira para cima, [p=0.2] ou para baixo, se for negativo. [p=0.3] Em {c}um mais duas vezes o cosseno de xis, cada ponto sobe um. [p=0.2] {d}O topo sai do dois e vai para três. [p=0.2] {e}O fundo sai do menos dois e vai para menos um. [p=0.3] E {f}o meio da onda, que era o eixo xis, sobe para a altura um."),
    # cê
    dict(id="s07", block="ce", text="Por fim, o {a}cê, que multiplica o xis lá dentro. [p=0.2] Em {b}cosseno de dois xis, o ângulo anda duas vezes mais rápido. [p=0.3] A onda fecha uma volta quando {c}o que está dentro do parêntese chega a dois pi."),
    dict(id="s08", block="ce", text="{a}Dois xis igual a dois pi. [p=0.2] Divida cada lado por dois: {b}xis igual a pi. [p=0.3] {c}O período cai pela metade, de dois pi para pi. [p=0.2] {d}Cabem duas ondas onde antes cabia uma. [p=0.3] Em geral, {e}o período é dois pi dividido por cê. [p=0.2] {f}O cê aperta ou alarga a onda, mas não mexe na altura."),
    # juntando
    dict(id="s09", block="juntando", text="Juntando tudo, em {a}um mais duas vezes o cosseno de dois xis: [p=0.2] {b}máximo: um mais dois dá três. [p=0.2] {c}Mínimo: um menos dois dá menos um. [p=0.2] {d}Período, pi. [p=0.3] E a imagem vai {e}de menos um a três."),
    # erro
    dict(id="s10", block="erro", text="O erro mais comum é {a}multiplicar o período pelo cê. [p=0.2] Com cê igual a dois, a pessoa faz dois pi vezes dois [p=0.2] e responde {b}quatro pi."),
    dict(id="s11", block="erro", text="Mas um cê maior faz o ângulo {a}correr mais. [p=0.2] Ele chega a dois pi {b}mais cedo, [p=0.2] e a onda se repete {c}em menos tempo. [p=0.3] {d}Cê maior, onda mais apertada: [p=0.2] por isso o período {e}é dividido pelo cê."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho, com {a}três contas: [p=0.2] {b}máximo é á mais bê, [p=0.2] {c}mínimo é á menos bê, [p=0.2] e {d}período é dois pi dividido por cê."),
    dict(id="s13", block="atalho", text="Funciona porque o cosseno {a}vai de menos um a um: [p=0.2] no topo, a onda vale á mais bê vezes um, [p=0.2] e no fundo, á mais bê vezes menos um. [p=0.3] {b}Cuidado quando o bê vem negativo, [p=0.2] como em {c}três menos duas vezes o cosseno de xis. [p=0.2] {d}Use o bê sem o sinal: [p=0.2] máximo cinco, mínimo um, amplitude dois. [p=0.2] O sinal de menos {e}só vira a onda de cabeça para baixo. [p=0.3] {f}Com o cê negativo, o ângulo só anda para trás, e a onda se repete no mesmo ritmo: [p=0.2] no período, use o cê sem o sinal também."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Ípsilon igual a dois, mais três vezes o seno de quatro xis. [p=0.3] {b}Qual é o máximo, o mínimo e o período?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] Á vale dois, bê vale três e cê vale quatro. [p=0.3] {a}Máximo: dois mais três dá cinco. [p=0.2] {b}Mínimo: dois menos três dá menos um. [p=0.2] {c}Período: dois pi dividido por quatro, [p=0.2] que dá {d}pi meios, ou noventa graus. [p=0.3] Imagem {e}de menos um a cinco."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}o á sobe ou desce a onda, [p=0.2] {b}o bê estica a altura [p=0.2] e {c}o cê aperta a onda e divide o período."),
    dict(id="s18", block="fim", text="Na próxima aula, essa onda {a}sai do papel: [p=0.2] {b}a altura da maré num porto. [p=0.2] Você lê {c}a maré alta, a maré baixa e de quantas em quantas horas ela se repete. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
