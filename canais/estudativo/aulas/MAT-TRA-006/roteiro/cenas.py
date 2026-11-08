# Estudativo · MAT-TRA-006 — Equações e inequações trigonométricas (Matemática · Trigonometria Avançada · Identidades, adição de arcos e equações).
# Habilidade: resolver sen x = 1/2 em [0, 2π] (π/6 e 5π/6) e ler no ciclo que sen x > 1/2 vale entre esses dois arcos.
# Pré-requisitos: MAT-CON-007 (intervalos, colchete aberto e fechado), MAT-FAT-008 (Bhaskara, Δ primeiro), MAT-TRI-009 (parceiro:
#   180° − ângulo no 2º, 360° − ângulo no 4º), MAT-TRI-010. Usa MAT-TRI-007 (π = 180°, "pi sextos"), MAT-TRI-008 (seno na altura,
#   cosseno na horizontal), MAT-TRI-003 (tabela), MAT-CON-001 (conjunto com chaves). Próxima: MAT-TRA-007.
# Questão inédita, criada para esta aula. Radianos lidos como na MAT-TRI-007 ("pi sextos", "cinco pi sextos"); conversão pelo
#   atalho da MAT-TRI-013: 150° = 5 · 30° → 5π/6; 315° = 7 · 45° → 7π/4; 300° = 5 · 60° → 5π/3.
# Contas: sen x = 1/2 → 30° = π/6 e 180° − 30° = 150° = 5π/6 · sen x > 1/2 → ]π/6, 5π/6[ · ≥ → [π/6, 5π/6].
#   cos x = √2/2 → 45° = π/4 e 360° − 45° = 315° = 7π/4.
#   2 sen² x − 3 sen x + 1 = 0 → y = sen x · Δ = 9 − 8 = 1 · y = (3 ± 1)/4 → 1 ou 1/2 → π/2, π/6, 5π/6.
#   Questão: 2 cos x − 1 = 0 → cos x = 1/2 → 60° = π/3 e 360° − 60° = 300° = 5π/3.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Equações e inequações trigonométricas"

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
    dict(id="s01", block="gancho", text="{a}Seno de xis igual a um meio. [p=0.2] Quase todo mundo responde {b}trinta graus, e para por aí. [p=0.3] Mas, na volta inteira, {c}tem outro ângulo com o mesmo seno, [p=0.2] e quem esquece dele {d}perde metade da questão."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve equações assim na volta inteira, [p=0.2] {b}lê a inequação direto no ciclo [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}radianos, com pi igual a cento e oitenta graus; [p=0.2] {c}o parceiro de cada arco no primeiro quadrante; [p=0.2] e {d}intervalos, com colchete aberto e fechado. [p=0.3] Se faltar alguma, procure no canal."),
    # a equação
    dict(id="s04", block="equacao", text="Resolver seno de xis igual a um meio é perguntar: [p=0.2] {a}em que pontos do ciclo a altura é um meio? [p=0.3] Trace {b}uma linha horizontal na altura um meio. [p=0.2] Ela corta o ciclo {c}em dois pontos."),
    dict(id="s05", block="equacao", text="{a}O primeiro é trinta graus, da tabela: pi sextos. [p=0.3] {b}O outro é o parceiro no segundo quadrante: [p=0.2] cento e oitenta menos trinta, cento e cinquenta graus. [p=0.2] Cento e cinquenta é cinco vezes trinta: {c}cinco pi sextos."),
    dict(id="s06", block="equacao", text="Na volta de zero a dois pi, {a}a solução é pi sextos e cinco pi sextos. [p=0.3] Com cosseno, a linha é {b}vertical, porque o cosseno se lê na horizontal. [p=0.2] Em {c}cosseno de xis igual a raiz de dois dividido por dois, [p=0.2] os pontos são {d}quarenta e cinco e trezentos e quinze graus: [p=0.2] {e}pi quartos e sete pi quartos."),
    # a inequação
    dict(id="s07", block="inequacao", text="E a inequação {a}seno de xis maior que um meio? [p=0.2] Agora a pergunta é: {b}onde a altura passa de um meio? [p=0.3] {c}Acima da linha horizontal. [p=0.2] É o arco {d}entre pi sextos e cinco pi sextos, [p=0.2] {e}sem as pontas, porque nelas o seno é igual a um meio, e não maior."),
    dict(id="s08", block="inequacao", text="Em intervalo: {a}aberto em pi sextos e aberto em cinco pi sextos. [p=0.3] Com {b}maior ou igual, as pontas entram, [p=0.2] e {c}o colchete fecha."),
    # segundo grau disfarçado
    dict(id="s09", block="segundo", text="Às vezes, a equação vem disfarçada de segundo grau: [p=0.2] {a}dois seno ao quadrado de xis, menos três seno de xis, mais um, igual a zero. [p=0.3] {b}Troque seno de xis por uma letra, como ípsilon. [p=0.2] Fica {c}dois ípsilon ao quadrado, menos três ípsilon, mais um, igual a zero."),
    dict(id="s10", block="segundo", text="Por Bhaskara: {a}delta é nove menos oito, um. [p=0.2] {b}Ípsilon é três mais ou menos um, dividido por quatro: [p=0.2] {c}um, ou um meio. [p=0.3] Volte para o seno. [p=0.2] {d}Seno de xis igual a um: pi meios. [p=0.2] {e}Seno de xis igual a um meio: pi sextos e cinco pi sextos. [p=0.2] {f}Três soluções."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}parar no primeiro ângulo. [p=0.2] A tabela só dá {b}pi sextos. [p=0.3] Mas {c}a linha corta o ciclo em dois pontos, [p=0.2] e a questão quer a volta inteira. [p=0.2] {d}Sempre procure o parceiro."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: [p=0.2] {a}no seno, a segunda solução é pi menos a primeira. [p=0.2] {b}No cosseno, é dois pi menos a primeira. [p=0.3] Funciona porque {c}o seno se repete no espelho do eixo vertical, [p=0.2] e {d}o cosseno, no espelho do eixo horizontal."),
    dict(id="s13", block="atalho", text="{a}Não vale quando o valor é um ou menos um. [p=0.2] Aí a linha só encosta no ciclo, [p=0.2] e {b}a solução é um ponto só, [p=0.2] como em seno de xis igual a um, que dá {c}só pi meios."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Resolva {a}dois cosseno de xis menos um igual a zero, [p=0.2] {b}com xis entre zero e dois pi."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] Isole o cosseno: {a}dois cosseno de xis igual a um, [p=0.2] {b}cosseno de xis igual a um meio. [p=0.3] {c}Da tabela, sessenta graus: pi terços."),
    dict(id="s17", block="resposta", text="Pelo atalho do cosseno, {a}trezentos e sessenta menos sessenta, trezentos graus. [p=0.2] Trezentos é cinco vezes sessenta: {b}cinco pi terços. [p=0.3] {c}Solução: pi terços e cinco pi terços."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}trace a linha no ciclo, [p=0.2] {b}ache o ângulo da tabela e o parceiro, [p=0.2] e, na inequação, {c}leia o arco de cima ou de baixo da linha."),
    dict(id="s19", block="fim", text="Na próxima aula, você {a}pratica a trilha inteira: [p=0.2] {b}leis dos senos e dos cossenos, [p=0.2] {c}identidades e equações no ciclo. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
