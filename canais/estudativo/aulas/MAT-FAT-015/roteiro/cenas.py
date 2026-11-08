# Estudativo · MAT-FAT-015 — Soma vezes diferença e cubo da soma: (a + b)(a − b) e (a + b)³ (Matemática · Fatoração e Equação do 2º Grau).
# Habilidade: abrir (x + 5)(x − 5) sem multiplicar tudo, calcular 101 · 99 de cabeça e abrir (x + 1)³ como (x + 1)²(x + 1).
# Pré-requisitos: MAT-FAT-001 (quadrado da soma), MAT-EQU-005 (chuveirinho), MAT-POT-003 (mesma base). Próxima: MAT-FAT-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis".
# Questão inédita, criada para esta aula.
# (x + 5)(x − 5) = x² − 25 (x = 10: 15 × 5 = 75) · 101 × 99 = 9.999 · (x + 1)³ = x³ + 3x² + 3x + 1 (x = 10: 1.331; erro x³ + 1 = 1.001).
# Atalho: 52 × 48 = 2.500 − 4 = 2.496; não compensa em 53 × 46 (meio 49,5). Questão: (x + 4)(x − 4) = x² − 16; 34 × 26 = 900 − 16 = 884.

TITULO = "Soma vezes diferença e cubo da soma"

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
    dict(id="s01", block="gancho", text="{a}Cento e um vezes noventa e nove. [p=0.3] Sem conta armada, sem calculadora: [p=0.2] {b}nove mil novecentos e noventa e nove. [p=0.3] E dá para chegar nisso em poucos segundos."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você faz essa conta de cabeça, [p=0.2] multiplica {b}a soma pela diferença sem chuveirinho [p=0.2] e abre {c}o cubo de uma soma."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre do {a}quadrado da soma: [p=0.2] quadrado do primeiro, mais duas vezes o primeiro vezes o segundo, mais quadrado do segundo. [p=0.3] E do {b}chuveirinho: todo termo multiplica todo termo. [p=0.3] Se faltar alguma, procure no canal."),
    # soma vezes diferença
    dict(id="s04", block="soma", text="Comece com {a}abre parênteses, xis mais cinco, fecha parênteses, [p=0.2] vezes, {b}abre parênteses, xis menos cinco, fecha parênteses. [p=0.3] São os mesmos termos, [p=0.2] {c}um parêntese com mais e o outro com menos."),
    dict(id="s05", block="soma", text="Pelo chuveirinho: {a}xis vezes xis, xis ao quadrado. [p=0.2] {b}Xis vezes menos cinco, menos cinco xis. [p=0.2] {c}Cinco vezes xis, mais cinco xis. [p=0.2] {d}Cinco vezes menos cinco, menos vinte e cinco."),
    dict(id="s06", block="soma", text="Olhe o meio: {a}menos cinco xis mais cinco xis dá zero. [p=0.2] {b}Os termos do meio se anulam. [p=0.3] Sobra {c}xis ao quadrado menos vinte e cinco. [p=0.3] Teste com dez: [p=0.2] {d}quinze vezes cinco dá setenta e cinco. [p=0.2] {e}Cem menos vinte e cinco também."),
    # regra
    dict(id="s07", block="regra", text="Esse é o produto notável da {a}soma vezes a diferença: [p=0.2] {b}o quadrado do primeiro termo [p=0.2] {c}menos o quadrado do segundo. [p=0.3] O meio sempre some, porque {d}um parêntese acrescenta exatamente o que o outro tira."),
    dict(id="s08", block="regra", text="Volte ao gancho. [p=0.2] {a}Cento e um é cem mais um. [p=0.2] {b}Noventa e nove é cem menos um. [p=0.3] Soma vezes diferença: {c}cem ao quadrado menos um ao quadrado. [p=0.2] {d}Dez mil menos um: nove mil novecentos e noventa e nove."),
    # cubo
    dict(id="s09", block="cubo", text="Agora o cubo. [p=0.2] {a}Abre parênteses, xis mais um, fecha parênteses, ao cubo, [p=0.2] é esse parêntese aparecendo três vezes na multiplicação. [p=0.3] Pela regra da mesma base, {b}o cubo é o quadrado vezes mais um parêntese, [p=0.2] porque {c}dois mais um dá três."),
    dict(id="s10", block="cubo", text="O quadrado você já sabe abrir: {a}xis ao quadrado mais dois xis mais um. [p=0.2] Falta {b}multiplicar por xis mais um, pelo chuveirinho. [p=0.3] {c}Tudo vezes xis: xis ao cubo mais dois xis ao quadrado mais xis. [p=0.2] {d}Tudo vezes um: xis ao quadrado mais dois xis mais um."),
    dict(id="s11", block="cubo", text="Juntando os semelhantes: {a}xis ao cubo mais três xis ao quadrado mais três xis mais um. [p=0.3] Teste com dez: [p=0.2] {b}onze ao cubo dá mil trezentos e trinta e um. [p=0.2] {c}Mil mais trezentos mais trinta mais um: mil trezentos e trinta e um. [p=0.2] Bateu."),
    dict(id="s12", block="cubo", text="Com quaisquer termos, {a}o padrão é o da tela: [p=0.2] cubo do primeiro, mais três vezes o quadrado do primeiro vezes o segundo, [p=0.2] mais três vezes o primeiro vezes o quadrado do segundo, mais cubo do segundo. [p=0.3] Mas não precisa decorar: [p=0.2] {b}o quadrado vezes mais um parêntese sempre chega lá."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é {a}elevar cada termo ao cubo [p=0.2] e escrever {b}xis ao cubo mais um. [p=0.3] Com dez, isso dá {c}mil e um, [p=0.2] e o certo é {d}mil trezentos e trinta e um. [p=0.2] {e}Os termos do meio sumiram."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho, para multiplicar números {a}à mesma distância de um número redondo. [p=0.2] {b}Cinquenta e dois vezes quarenta e oito. [p=0.2] O meio é {c}cinquenta, e a distância é {d}dois. [p=0.3] {e}Cinquenta ao quadrado menos dois ao quadrado: [p=0.2] {f}dois mil e quinhentos menos quatro dá dois mil quatrocentos e noventa e seis."),
    dict(id="s15", block="atalho", text="Funciona porque é a soma vezes a diferença: {a}cinquenta mais dois, vezes cinquenta menos dois. [p=0.3] {b}Não compensa quando o meio não é redondo, [p=0.2] como em {c}cinquenta e três vezes quarenta e seis. [p=0.2] Aí, faça a conta normal."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Escreva sem parênteses: {a}abre parênteses, xis mais quatro, fecha parênteses, vezes, abre parênteses, xis menos quatro, fecha parênteses. [p=0.3] Depois, calcule {b}trinta e quatro vezes vinte e seis de cabeça."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Soma vezes diferença: {a}xis ao quadrado menos dezesseis. [p=0.3] Trinta e quatro é {b}trinta mais quatro, [p=0.2] e vinte e seis é {c}trinta menos quatro. [p=0.2] O xis vale trinta: {d}novecentos menos dezesseis dá oitocentos e oitenta e quatro."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}soma vezes diferença é o quadrado do primeiro menos o quadrado do segundo, [p=0.2] e {b}o cubo é o quadrado vezes mais um parêntese."),
    dict(id="s20", block="fim", text="Até aqui, você abriu parênteses. [p=0.2] Na próxima aula, faz o caminho de volta: [p=0.2] {a}fatorar, colocando em evidência o que se repete, [p=0.2] como em {b}seis xis ao quadrado mais nove xis. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
