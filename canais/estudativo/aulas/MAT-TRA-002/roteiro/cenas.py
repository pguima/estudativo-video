# Estudativo · MAT-TRA-002 — Lei dos cossenos (Matemática · Trigonometria Avançada · Lei dos senos e dos cossenos).
# Habilidade: achar o terceiro lado de um triângulo com lados 3 e 5 e ângulo de 120° entre eles (7).
# Pré-requisitos: MAT-ANG-015 (Pitágoras), MAT-TRI-002 (cosseno no triângulo retângulo), MAT-TRI-009 (cos 120° = −cos 60° = −1/2).
#   Usa MAT-TRA-001 (par lado–ângulo de frente), MAT-NUM-016 (tirar uma dívida é ganhar), MAT-TRI-003 (cos 60° = 1/2). Próxima: MAT-TRA-003.
# Questão inédita, criada para esta aula. Cosseno narrado por extenso; na tela, cos. "Bê cê" narrado como letras.
# A fórmula é apresentada como Pitágoras com um ajuste (sem a demonstração completa): 90° zera o ajuste; agudo encolhe; obtuso estica.
# Contas: x² = 9 + 25 − 2 · 3 · 5 · cos 120° = 34 − 30 · (−1/2) = 34 + 15 = 49 → 7 · Pitágoras √34 ≈ 5,8 < 7 (obtuso estica).
# Erro: cos 120° = +1/2 → 34 − 15 = 19 → √19 ≈ 4,4 (menor que √34: impossível para ângulo aberto).
# Atalho: 60° → a² = b² + c² − bc · 120° → a² = b² + c² + bc (2 · 1/2 = 1).
# Questão: 5 e 8 com 60° → 25 + 64 − 40 = 49 → 7 · √89 ≈ 9,4 > 7 (agudo encolhe).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Lei dos cossenos"

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
    dict(id="s01", block="gancho", text="{a}Dois lados de um triângulo medem três e cinco, [p=0.2] e o ângulo entre eles é de {b}cento e vinte graus. [p=0.3] {c}Quanto mede o terceiro lado? [p=0.3] A lei dos senos não começa aqui: [p=0.2] {d}não tem nenhum par completo, de lado e ângulo de frente."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha esse lado com a lei dos cossenos, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}o teorema de Pitágoras; [p=0.2] {c}o cosseno, que no triângulo retângulo é o cateto adjacente dividido pela hipotenusa; [p=0.2] e {d}o sinal dele acima de noventa graus: [p=0.2] cosseno de cento e vinte é menos um meio, negativo. [p=0.3] Se faltar alguma, procure no canal."),
    # a regra
    dict(id="s04", block="regra", text="A lei dos cossenos é {a}Pitágoras com um ajuste. [p=0.3] O lado de frente para o ângulo, ao quadrado, [p=0.2] é {b}a soma dos quadrados dos outros dois lados, [p=0.2] {c}menos duas vezes esses dois lados, vezes o cosseno do ângulo entre eles."),
    dict(id="s05", block="regra", text="Nos livros: [p=0.2] {a}á ao quadrado igual a bê ao quadrado mais cê ao quadrado, menos dois bê cê, cosseno de á. [p=0.3] {b}O lado á fica de frente para o ângulo á. [p=0.2] {c}Bê e cê são os lados que formam o ângulo."),
    # por que é Pitágoras com ajuste
    dict(id="s06", block="ajuste", text="Por que um ajuste? [p=0.2] Com {a}noventa graus, o cosseno é zero. [p=0.2] O ajuste some, e sobra {b}o próprio Pitágoras. [p=0.3] {c}Feche o ângulo: o cosseno fica positivo, o ajuste tira, e o lado encolhe. [p=0.3] {d}Abra o ângulo além de noventa: o cosseno fica negativo, o ajuste soma, e o lado cresce."),
    # o exemplo
    dict(id="s07", block="conta", text="Agora, o triângulo do começo. [p=0.2] {a}Xis ao quadrado igual a três ao quadrado, mais cinco ao quadrado, menos dois vezes três vezes cinco, vezes cosseno de cento e vinte. [p=0.3] {b}Nove mais vinte e cinco dá trinta e quatro. [p=0.2] {c}Dois vezes três vezes cinco dá trinta."),
    dict(id="s08", block="conta", text="{a}Cosseno de cento e vinte é menos um meio, [p=0.2] e {b}trinta vezes menos um meio dá menos quinze. [p=0.3] Fica {c}trinta e quatro menos, abre parênteses, menos quinze, fecha parênteses. [p=0.2] Tirar uma dívida é ganhar: [p=0.2] {d}trinta e quatro mais quinze, quarenta e nove. [p=0.3] {e}Xis é a raiz de quarenta e nove: sete."),
    dict(id="s09", block="conta", text="Confira: o ângulo é aberto, então o lado tem que passar do Pitágoras. [p=0.2] {a}Raiz de trinta e quatro é quase seis. [p=0.2] {b}Sete passou. [p=0.2] Faz sentido."),
    # erro
    dict(id="s10", block="erro", text="O erro mais comum é {a}perder o sinal do cosseno. [p=0.2] A pessoa usa {b}cosseno de cento e vinte igual a um meio, positivo, [p=0.2] e faz {c}trinta e quatro menos quinze, dezenove. [p=0.3] {d}A raiz de dezenove é pouco mais de quatro: [p=0.2] menor que o Pitágoras, com o ângulo aberto. [p=0.2] {e}Não pode."),
    # atalho
    dict(id="s11", block="atalho", text="Agora o atalho, para os ângulos que mais caem. [p=0.2] {a}Com sessenta graus, o cosseno é um meio, [p=0.2] e dois vezes um meio dá um. [p=0.2] O ajuste vira {b}menos o produto dos dois lados. [p=0.3] {c}Com cento e vinte graus, o cosseno é menos um meio, [p=0.2] e o ajuste vira {d}mais o produto."),
    dict(id="s12", block="atalho", text="No exemplo: {a}nove mais vinte e cinco, mais três vezes cinco: [p=0.2] quarenta e nove, sem fração nenhuma. [p=0.3] Funciona porque {b}o dois da fórmula cancela o meio do cosseno. [p=0.3] {c}Com outros ângulos, como quarenta e cinco graus, não compensa: [p=0.2] aí, faça a fórmula inteira."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] Dois lados de um triângulo medem {a}cinco e oito, [p=0.2] com {b}sessenta graus entre eles. [p=0.3] {c}Quanto mede o terceiro lado?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] Sessenta graus: {a}vale o atalho do menos o produto. [p=0.3] {b}Vinte e cinco mais sessenta e quatro dá oitenta e nove. [p=0.2] {c}Menos cinco vezes oito, quarenta: [p=0.2] {d}quarenta e nove. [p=0.2] {e}A raiz dá sete."),
    dict(id="s16", block="resposta", text="Confira: o ângulo é fechado, então o lado fica abaixo do Pitágoras. [p=0.2] {a}Raiz de oitenta e nove passa de nove. [p=0.2] {b}Sete ficou abaixo. [p=0.2] Faz sentido."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}é Pitágoras com um ajuste, [p=0.2] {b}menos duas vezes o produto dos lados vezes o cosseno, [p=0.2] e {c}o sinal do cosseno decide se o lado cresce ou encolhe."),
    dict(id="s18", block="fim", text="Na próxima aula, você aprende a {a}olhar os dados e escolher a lei certa, [p=0.2] acha {b}a distância entre dois pontos separados por um lago [p=0.2] e descobre, {c}só pelos lados, se o triângulo tem um ângulo obtuso. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
