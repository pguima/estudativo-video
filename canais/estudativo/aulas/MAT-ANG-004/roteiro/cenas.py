# Estudativo · MAT-ANG-004 — Soma dos ângulos do triângulo e ângulo externo (Matemática · Geometria Plana: Ângulos e Triângulos).
# Habilidade: achar o terceiro ângulo de um triângulo com 50° e 60° e usar que o ângulo externo vale a soma dos dois internos não vizinhos.
# Pré-requisitos: MAT-ANG-003 (alternos internos), MAT-ANG-002 (suplementares, complementares). Próxima: MAT-ANG-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Visual: três pontas de papel juntas numa linha reta; triângulo ABC (A em cima) com a paralela a BC por A e os alternos coloridos;
# triângulo A = 50°, B = 60°, C = 70° com o lado BC prolongado além de C (tracejado) e o externo de 110° em C.

TITULO = "Soma dos ângulos do triângulo e ângulo externo"

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
    dict(id="s01", block="gancho", text="{a}Recorte um triângulo de papel, de qualquer formato. [p=0.2] {b}Rasgue as três pontas [p=0.2] e {c}junte uma ao lado da outra. [p=0.3] Sempre dá {d}uma linha reta. [p=0.2] Triângulo grande, pequeno ou torto: {e}sempre."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você entende por que isso acontece, [p=0.2] {b}acha o ângulo que falta em qualquer triângulo [p=0.2] e leva um {c}atalho para o ângulo externo."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o ângulo raso, a linha reta, mede cento e oitenta graus, [p=0.2] e {c}com retas paralelas, ângulos alternos internos são iguais. [p=0.3] Se faltar alguma, procure no canal."),
    # por que 180
    dict(id="s04", block="prova", text="Pegue {a}um triângulo com vértices á, bê e cê, [p=0.2] com o á em cima. [p=0.3] Pelo á, passe {b}uma reta paralela ao lado de baixo, o lado bê cê."),
    dict(id="s05", block="prova", text="Lá em cima, essa reta e os lados do triângulo formam {a}três ângulos lado a lado, sobre uma linha reta. [p=0.3] O do meio é {b}o próprio ângulo em á."),
    dict(id="s06", block="prova", text="O da esquerda é {a}alterno interno do ângulo em bê, [p=0.2] porque o lado á bê corta as paralelas. [p=0.3] Então {b}ele é igual ao ângulo em bê. [p=0.2] Do mesmo jeito, {c}o da direita é igual ao ângulo em cê."),
    dict(id="s07", block="prova", text="Ou seja, lá em cima aparecem {a}os três ângulos do triângulo, [p=0.2] juntos {b}numa linha reta. [p=0.3] {c}A soma dos ângulos de dentro de qualquer triângulo é cento e oitenta graus. [p=0.2] É o papel rasgado do começo."),
    # terceiro ângulo
    dict(id="s08", block="terceiro", text="Vamos usar. [p=0.2] Um triângulo tem ângulos de {a}cinquenta graus e de sessenta graus. [p=0.2] Quanto mede o terceiro?"),
    dict(id="s09", block="terceiro", text="{a}Some os conhecidos: cinquenta mais sessenta dá cento e dez. [p=0.2] {b}Cento e oitenta menos cento e dez dá setenta graus. [p=0.3] Conferindo: {c}cinquenta mais sessenta mais setenta dá cento e oitenta."),
    dict(id="s10", block="terceiro", text="Num triângulo com {a}um ângulo reto, a conta fica mais curta. [p=0.2] O reto já gasta noventa, [p=0.2] então {b}os outros ângulos somam noventa: são complementares. [p=0.3] Se um mede {c}vinte e cinco graus, o outro mede noventa menos vinte e cinco, que dá {d}sessenta e cinco."),
    # ângulo externo
    dict(id="s11", block="externo", text="Agora, o ângulo externo. [p=0.2] Volte ao triângulo do exemplo, com {a}cinquenta graus em á, sessenta em bê e setenta em cê. [p=0.3] {b}Prolongue o lado bê cê, passando do cê. [p=0.2] Entre esse prolongamento e o lado á cê, nasce {c}o ângulo externo em cê."),
    dict(id="s12", block="externo", text="Ele e o ângulo de dentro, em cê, estão {a}sobre uma linha reta. [p=0.2] Então o externo mede {b}cento e oitenta menos setenta, que dá cento e dez graus."),
    dict(id="s13", block="externo", text="Repare: {a}cento e dez é cinquenta mais sessenta, [p=0.2] a soma dos ângulos {b}em á e em bê, [p=0.2] que não encostam no cê. [p=0.3] {c}O ângulo externo vale a soma dos internos não vizinhos."),
    dict(id="s14", block="externo", text="Faz sentido: [p=0.2] {a}o externo completa cento e oitenta com o ângulo em cê, [p=0.2] e {b}á mais bê também completam cento e oitenta com ele. [p=0.3] Então {c}o externo e a soma de á com bê têm de ser iguais."),
    # erro
    dict(id="s15", block="erro", text="Cuidado com o erro mais comum: {a}usar o externo como se fosse um ângulo de dentro. [p=0.3] Um triângulo tem {b}externo de cento e vinte graus em cê [p=0.2] e {c}cinquenta graus em á. [p=0.2] Quanto mede o ângulo em bê?"),
    dict(id="s16", block="erro", text="Quem erra faz {a}cento e oitenta menos cento e vinte menos cinquenta [p=0.2] e acha {b}dez graus. [p=0.3] Mas o de cento e vinte está fora do triângulo. [p=0.2] O certo: {c}o externo é a soma de á com bê. [p=0.2] {d}Cento e vinte menos cinquenta dá setenta graus."),
    # atalho
    dict(id="s17", block="atalho", text="Esse é o atalho prometido: [p=0.2] {a}externo igual à soma dos internos de longe. [p=0.3] Você pula a etapa de achar {b}o ângulo de dentro, ao lado do externo."),
    dict(id="s18", block="atalho", text="Funciona porque {a}o externo e os internos de longe completam o mesmo cento e oitenta com o ângulo vizinho. [p=0.3] {b}Não compensa quando a pergunta é o próprio ângulo vizinho: [p=0.2] aí, é só {c}cento e oitenta menos o externo."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Num triângulo, o ângulo externo em cê mede {a}cento e cinquenta graus. [p=0.2] Os ângulos de dentro, em á e em bê, medem {b}xis e dois xis. [p=0.3] {c}Quanto mede cada ângulo do triângulo?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] Pelo atalho, {a}o externo é a soma dos internos de longe: [p=0.2] {b}xis mais dois xis igual a cento e cinquenta. [p=0.2] {c}Três xis igual a cento e cinquenta. [p=0.2] {d}Xis igual a cinquenta."),
    dict(id="s22", block="resposta", text="{a}Em á, cinquenta graus. [p=0.2] {b}Em bê, duas vezes cinquenta dá cem graus. [p=0.2] {c}Em cê, cento e oitenta menos cento e cinquenta dá trinta graus. [p=0.3] Conferindo: {d}cinquenta mais cem mais trinta dá cento e oitenta. [p=0.2] Bateu."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}os ângulos de dentro de um triângulo somam cento e oitenta, [p=0.2] e {b}o externo é a soma dos internos de longe."),
    dict(id="s24", block="fim", text="Na próxima aula, você vai {a}dar nome aos triângulos, pelos lados e pelos ângulos, [p=0.2] e achar {b}os ângulos de um triângulo com dois lados iguais. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
