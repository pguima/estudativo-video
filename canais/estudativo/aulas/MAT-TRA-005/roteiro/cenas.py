# Estudativo · MAT-TRA-005 — Adição de arcos e arco duplo (Matemática · Trigonometria Avançada · Identidades, adição de arcos e equações).
# Habilidade: calcular sen 75° = sen(45° + 30°) = (√6 + √2)/4 e usar sen 2x = 2 sen x cos x.
# Pré-requisitos: MAT-TRA-004 (identidades, tudo em seno e cosseno). Usa MAT-TRI-003 (tabela de 30°, 45° e 60°), MAT-POT-009
#   (√2 · √3 = √6; √2 + √3 não vira √5), MAT-TRI-010 (cos a partir do sen, "o um com o mesmo denominador"), MAT-FRA-009
#   (multiplicar frações), MAT-TRI-008 (sen 180° = 0, sen 90° = 1). Próxima: MAT-TRA-006.
# FORA da ficha: MAT-FRA-007/008 (somar frações) e MAT-TRI-009. √6/4 + √2/4 explicado como "pedaços do mesmo tamanho, junte em
#   cima"; 1 − 25/169 como na MAT-TRI-010 (um inteiro = 169/169).
# Questão inédita, criada para esta aula. Raízes em fração narradas "raiz de dois dividido por dois", como na MAT-TRI-003.
# A música "Minha terra tem palmeiras onde canta o sabiá" é o macete popular de cursinho para sen(a + b).
# Contas: sen 45 + sen 30 = √2/2 + 1/2 ≈ 1,2 > 1 · sen 75 = √2/2 · √3/2 + 1/2 · √2/2 = √6/4 + √2/4 = (√6 + √2)/4 ≈ (2,4 + 1,4)/4 = 0,95
#   (exato ≈ 0,966) · sen 2x com sen 3/5, cos 4/5 → 2 · 3 · 4 / 25 = 24/25 · erro: sen 180° = 0 ≠ 2 sen 90° = 2.
#   Questão: sen x = 5/13 → cos² = 169/169 − 25/169 = 144/169 → cos = 12/13 → sen 2x = 2 · 5 · 12 / 169 = 120/169.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Adição de arcos e arco duplo"

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
    dict(id="s01", block="gancho", text="{a}Seno de setenta e cinco graus. [p=0.2] Não está na tabela. [p=0.3] A tentação é {b}somar seno de quarenta e cinco com seno de trinta. [p=0.2] {c}Só que isso dá mais que um, [p=0.2] e {d}o seno nunca passa de um. [p=0.3] Alguma coisa está errada."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula o seno de uma soma de arcos, [p=0.2] usa o {b}arco duplo [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}a tabela de trinta, quarenta e cinco e sessenta graus; [p=0.2] {c}multiplicar raízes, como raiz de dois vezes raiz de três, que dá raiz de seis; [p=0.2] e {d}a relação fundamental, que dá o cosseno quando você sabe o seno. [p=0.3] Se faltar alguma, procure no canal."),
    # as fórmulas
    dict(id="s04", block="formula", text="O seno de uma soma {a}não é a soma dos senos. [p=0.3] A fórmula certa mistura seno e cosseno: [p=0.2] {b}seno de á mais bê é seno de á vezes cosseno de bê, [p=0.2] {c}mais seno de bê vezes cosseno de á."),
    dict(id="s05", block="formula", text="Na subtração, {a}só o sinal do meio muda. [p=0.3] E o cosseno tem a sua: [p=0.2] {b}cosseno de á mais bê é cosseno de á vezes cosseno de bê, [p=0.2] menos seno de á vezes seno de bê. [p=0.2] {c}No cosseno, o sinal do meio é o contrário do de dentro."),
    # seno de 75
    dict(id="s06", block="conta", text="Agora, seno de setenta e cinco: [p=0.2] {a}seno de quarenta e cinco mais trinta. [p=0.3] Primeira parte: {b}seno de quarenta e cinco vezes cosseno de trinta. [p=0.2] Em cima, {c}raiz de dois vezes raiz de três, raiz de seis. [p=0.2] Embaixo, {d}dois vezes dois, quatro."),
    dict(id="s07", block="conta", text="Segunda parte: {a}seno de trinta vezes cosseno de quarenta e cinco. [p=0.2] Em cima, um vezes raiz de dois; [p=0.2] embaixo, dois vezes dois: {b}raiz de dois dividido por quatro. [p=0.3] As duas partes são quartos: {c}pedaços do mesmo tamanho, então junte em cima. [p=0.2] {d}Seno de setenta e cinco é raiz de seis mais raiz de dois, tudo dividido por quatro."),
    dict(id="s08", block="conta", text="Repare: {a}raiz de seis mais raiz de dois não vira raiz de oito. [p=0.2] Fica assim mesmo. [p=0.3] Com raiz de seis perto de dois vírgula quatro e raiz de dois perto de um vírgula quatro, [p=0.2] {b}dá cerca de zero vírgula noventa e cinco. [p=0.2] {c}Quase um, mas menor: faz sentido, porque setenta e cinco graus está perto de noventa."),
    # arco duplo
    dict(id="s09", block="duplo", text="E o arco duplo? [p=0.2] {a}Dois xis é xis mais xis. [p=0.2] Na fórmula da soma, fica {b}seno de xis vezes cosseno de xis, mais seno de xis vezes cosseno de xis: [p=0.2] {c}duas vezes a mesma coisa. [p=0.3] {d}Seno de dois xis é dois, vezes seno de xis, vezes cosseno de xis."),
    dict(id="s10", block="duplo", text="Exemplo: {a}seno de xis igual a três quintos, e cosseno, quatro quintos. [p=0.2] {b}Seno de dois xis: dois vezes três quintos vezes quatro quintos. [p=0.2] Em cima, {c}dois vezes três vezes quatro, vinte e quatro. [p=0.2] Embaixo, cinco vezes cinco, vinte e cinco: [p=0.2] {d}vinte e quatro vinte e cinco avos. [p=0.3] Do mesmo jeito, {e}cosseno de dois xis é cosseno ao quadrado menos seno ao quadrado."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é o do começo: {a}abrir o seno como se fosse um parêntese de conta. [p=0.2] {b}O seno da soma não é a soma dos senos, [p=0.2] e {c}seno de dois xis não é duas vezes seno de xis. [p=0.3] Teste com noventa graus: [p=0.2] {d}seno de cento e oitenta é zero, [p=0.2] mas {e}duas vezes seno de noventa dá dois."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho para não esquecer: {a}a música. [p=0.3] {b}Minha terra tem palmeiras, onde canta o sabiá: [p=0.2] {c}seno á, cosseno bê, seno bê, cosseno á. [p=0.3] Para o cosseno, {d}cosseno com cosseno, seno com seno, e o sinal trocado."),
    dict(id="s13", block="atalho", text="Funciona porque {a}o ritmo guarda a ordem das letras, [p=0.2] e a ordem importa na subtração. [p=0.3] {b}Para o arco duplo, não precisa de música nova: [p=0.2] é a fórmula da soma {c}com os dois arcos iguais."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] O seno de xis vale {a}cinco treze avos, [p=0.2] com xis {b}no primeiro quadrante. [p=0.3] {c}Calcule o seno de dois xis."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] Primeiro, o cosseno, pela relação fundamental. [p=0.2] {a}Seno ao quadrado: vinte e cinco cento e sessenta e nove avos. [p=0.2] {b}Um inteiro são cento e sessenta e nove cento e sessenta e nove avos; [p=0.2] tirando vinte e cinco, {c}sobra cento e quarenta e quatro. [p=0.2] {d}O cosseno é doze treze avos, positivo no primeiro quadrante."),
    dict(id="s17", block="resposta", text="{a}Seno de dois xis: dois vezes cinco treze avos vezes doze treze avos. [p=0.2] Em cima, {b}dois vezes cinco vezes doze, cento e vinte. [p=0.2] Embaixo, {c}treze vezes treze, cento e sessenta e nove. [p=0.3] {d}Cento e vinte cento e sessenta e nove avos."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}seno da soma mistura seno e cosseno, [p=0.2] {b}o cosseno troca o sinal do meio [p=0.2] e {c}seno de dois xis é dois seno de xis cosseno de xis."),
    dict(id="s19", block="fim", text="Na próxima aula, o caminho é o inverso: [p=0.2] você sabe o seno e procura o arco. [p=0.2] Resolve {a}seno de xis igual a um meio na volta inteira, [p=0.2] e lê no ciclo {b}onde o seno passa de um meio. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
