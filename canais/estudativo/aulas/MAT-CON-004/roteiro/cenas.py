# Estudativo · MAT-CON-004 — Naturais, inteiros e racionais (Matemática · Conjuntos · Conjuntos numéricos).
# Habilidade: dizer que −3 é inteiro e não natural, que 0,75 e 0,4545… são racionais porque viram fração e escrever ℕ ⊂ ℤ ⊂ ℚ.
# Pré-requisitos: MAT-CON-001 (pertence, contido), MAT-FRA-020 (dízimas), MAT-NUM-015 (negativos e reta). Próxima: MAT-CON-005.
# Questão inédita, criada para esta aula. Converter dízima em fração fica para a MAT-CON-005: aqui só se usa 5/11 = 0,4545… (visto na MAT-FRA-020).
# Contas: 0,75 = 75/100 = 3/4 (÷25) · 5 ÷ 11 = 0,4545… · 5 = 5/1 · −3 = −3/1 · atalho: 12/4 = 3.
# Questão: −7 ∈ ℤ, ℚ, ∉ ℕ · 0,6 = 6/10 = 3/5 ∈ ℚ · 0,333… = 1/3 ∈ ℚ · 18/6 = 3 ∈ ℕ, ℤ, ℚ.
# Visual: os símbolos ℕ, ℤ, ℚ com as listas; três círculos um dentro do outro (ℕ dentro de ℤ dentro de ℚ) com números nas faixas.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Naturais, inteiros e racionais"

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
    dict(id="s01", block="gancho", text="{a}Menos três é um número natural? [p=0.3] E {b}zero vírgula quatro cinco quatro cinco, que não acaba nunca, [p=0.2] pode ser uma fração? [p=0.3] A primeira resposta é {c}não. [p=0.2] A segunda é {d}sim."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você coloca cada número na sua família, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}pertence e está contido, [p=0.2] {c}os negativos na reta [p=0.2] e {d}dízima, o decimal com um trecho que se repete sem fim. [p=0.3] Se faltar alguma, procure no canal."),
    # naturais
    dict(id="s04", block="naturais", text="A primeira família é a dos números de contar: [p=0.2] {a}zero, um, dois, três, e assim sem fim. [p=0.3] O zero entra: é quanto tem quem não tem nada. [p=0.3] São os {b}naturais, [p=0.2] e o nome do conjunto é {c}um ene maiúsculo, com traço duplo."),
    # inteiros
    dict(id="s05", block="inteiros", text="Junte os negativos e você tem os {a}inteiros: [p=0.2] {b}os naturais e também menos um, menos dois, menos três, e assim por diante. [p=0.3] O nome é {c}zê, da palavra alemã para número."),
    dict(id="s06", block="inteiros", text="{a}Menos três pertence aos inteiros, [p=0.2] mas {b}não pertence aos naturais. [p=0.2] Ninguém conta menos três objetos. [p=0.3] Em símbolos: {c}menos três pertence a zê, [p=0.2] e {d}não pertence a ene, com o símbolo cortado."),
    # racionais
    dict(id="s07", block="racionais", text="E os números quebrados? [p=0.2] Um número é {a}racional quando pode ser escrito como fração, [p=0.2] com {b}inteiro em cima e inteiro embaixo, [p=0.2] e o de baixo {c}nunca pode ser zero. [p=0.3] O nome é {d}quê, de quociente, o resultado de uma divisão."),
    dict(id="s08", block="racionais", text="{a}Zero vírgula setenta e cinco é setenta e cinco centésimos. [p=0.2] Dividindo em cima e embaixo por vinte e cinco, {b}três quartos. [p=0.3] Virou fração: {c}racional. [p=0.3] Todo decimal que acaba vira fração com um seguido de zeros embaixo, como dez, cem ou mil, [p=0.2] então {d}todo decimal exato é racional."),
    dict(id="s09", block="racionais", text="E a dízima? [p=0.2] {a}Cinco dividido por onze dá zero vírgula quatro cinco quatro cinco, sem fim. [p=0.3] Ela {b}nasceu de uma fração. [p=0.2] Então é {c}racional, mesmo sem acabar."),
    dict(id="s10", block="racionais", text="E os inteiros? [p=0.2] {a}Cinco é a fração com cinco em cima e um embaixo, [p=0.2] porque cinco dividido por um dá cinco. [p=0.2] {b}Menos três é a fração com menos três em cima e um embaixo. [p=0.3] O de cima pode ser negativo, porque menos três também é inteiro, [p=0.2] e dividir por um não muda o número. [p=0.3] Então {c}todo inteiro também é racional."),
    dict(id="s11", block="reta", text="Na reta, os inteiros são os pontos de {a}passo inteiro. [p=0.2] Os racionais ocupam também {b}os espaços entre eles. [p=0.3] {c}Três quartos fica entre zero e um. [p=0.2] {d}Menos zero vírgula cinco fica no meio do caminho entre menos um e zero: [p=0.2] é a fração com menos um em cima e dois embaixo. [p=0.3] Nenhum deles é inteiro, mas {e}ambos são racionais."),
    # escada
    dict(id="s12", block="escada", text="Daí sai uma escada: [p=0.2] {a}todo natural é inteiro, [p=0.2] e {b}todo inteiro é racional. [p=0.3] Em símbolos: {c}ene está contido em zê, que está contido em quê. [p=0.3] No desenho, {d}um círculo dentro do outro."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é achar que {a}decimal que não acaba não pode ser fração. [p=0.3] Mas zero vírgula quatro cinco quatro cinco {b}é cinco onze avos. [p=0.2] Divida e confira. [p=0.3] {c}Não acabar não tira ninguém dos racionais. [p=0.3] Números que não viram fração existem, sim, [p=0.2] e são {d}assunto de outra aula."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho para classificar: {a}suba a escada de baixo para cima. [p=0.3] Pergunte: {b}é natural? [p=0.2] Se não, {c}é inteiro? [p=0.2] Se não, {d}vira fração? [p=0.3] {e}No primeiro sim, pare: [p=0.2] o número já está também em todos os conjuntos de fora."),
    dict(id="s15", block="atalho", text="Funciona porque cada conjunto {a}está contido no seguinte. [p=0.3] {b}Não compensa julgar pela aparência: [p=0.2] {c}doze quartos parece fração, mas é três, um natural. [p=0.2] {d}Simplifique antes de classificar."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Diga a que conjuntos pertence cada número: [p=0.2] {a}menos sete, [p=0.2] {b}zero vírgula seis, [p=0.2] {c}zero vírgula três três três, sem fim, [p=0.2] e {d}dezoito sextos."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Menos sete não é natural, mas é inteiro. [p=0.2] Então é {b}inteiro e racional. [p=0.3] {c}Zero vírgula seis fica entre zero e um, então não é inteiro. [p=0.2] Mas é seis décimos, ou três quintos: [p=0.2] {d}só racional."),
    dict(id="s19", block="resposta", text="{a}Um dividido por três dá zero vírgula três três três, sem fim. [p=0.2] Veio de um terço: {b}racional. [p=0.3] E a pegadinha: {c}dezoito sextos é três. [p=0.2] {d}Natural, inteiro e racional."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}natural conta, [p=0.2] {b}inteiro ganha os negativos [p=0.2] e {c}racional é tudo que vira fração, [p=0.2] até a dízima."),
    dict(id="s21", block="fim", text="Na próxima aula, você faz o caminho de volta: [p=0.2] pega {a}uma dízima e descobre a fração que gerou ela, [p=0.2] a {b}fração geratriz. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
