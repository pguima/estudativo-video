# Estudativo · MAT-EXP-007 — Praticando: função exponencial (Matemática · Exponencial e Logaritmo · prática).
# Habilidade: montar modelos de crescimento e meia-vida e resolver equações exponenciais.
# Pré-requisitos: MAT-EXP-001, MAT-EXP-002, MAT-EXP-003, MAT-EXP-004, MAT-EXP-005, MAT-EXP-006. Próxima: MAT-EXP-008.
# Questões inéditas, criadas para esta aula. Situação 2 junta meia-vida e inequação; situação 3 junta duplicação e equação.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Praticando: função exponencial"

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
    dict(id="s01", block="gancho", text="{a}Quatro situações, [p=0.2] criadas para esta aula. [p=0.3] Elas juntam tudo da função exponencial: [p=0.2] {b}crescimento, meia-vida e equação. [p=0.3] Em cada uma, {c}pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}a lei com o fator na base e o tempo no expoente, [p=0.2] {b}dividir o tempo pela meia-vida ou pelo tempo de dobrar, [p=0.2] {c}igualar as bases [p=0.2] e {d}o apelido ípsilon. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: decaimento
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Uma máquina de {b}oitenta mil reais perde {c}vinte por cento do valor a cada ano. [p=0.3] {d}Escreva a lei do valor, [p=0.1] diga se a função cresce ou decresce [p=0.1] e {e}calcule o valor depois de dois anos."),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Tirar vinte por cento é multiplicar pelo fator de desconto {a}zero vírgula oito. [p=0.2] A lei: {b}vê igual a oitenta mil vezes zero vírgula oito elevado a tê, [p=0.1] com tê em anos. [p=0.3] Base entre zero e um: {c}a função decresce."),
    dict(id="s06", block="resposta1", text="Em dois anos: {a}zero vírgula oito ao quadrado dá zero vírgula sessenta e quatro. [p=0.2] {b}Oitenta mil vezes zero vírgula sessenta e quatro dá cinquenta e um mil e duzentos reais."),
    dict(id="s07", block="resposta1", text="Cuidado com a conta apressada: [p=0.2] {a}vinte por cento ao ano, em dois anos, quarenta por cento. [p=0.2] Daria {b}quarenta e oito mil reais. [p=0.3] Errado. [p=0.2] No segundo ano, os vinte por cento valem sobre {c}sessenta e quatro mil, e não sobre oitenta mil."),
    # situação 2: meia-vida e inequação
    dict(id="s08", block="questao2", text="{a}Situação dois. [p=0.2] Uma pessoa toma {b}duzentos miligramas de um remédio com meia-vida de {c}quatro horas. [p=0.3] {d}Quanto resta depois de doze horas? [p=0.2] E {e}durante quanto tempo restam mais de vinte e cinco miligramas?"),
    dict(id="s09", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s10", block="resposta2", text="Vamos lá. [p=0.2] {a}Doze dividido por quatro dá três meias-vidas. [p=0.2] {b}Duzentos. [p=0.1] Cem. [p=0.1] Cinquenta. [p=0.1] Vinte e cinco miligramas. [p=0.3] Na fórmula: {c}quê igual a duzentos vezes um meio elevado a tê dividido por quatro, com a divisão toda no expoente."),
    dict(id="s11", block="resposta2", text="Para a segunda pergunta, monte a inequação: [p=0.2] {a}essa mesma conta, maior que vinte e cinco. [p=0.3] {b}Divida cada lado por duzentos. [p=0.2] Vinte e cinco dividido por duzentos dá {c}um oitavo, [p=0.2] que é {d}um meio ao cubo."),
    dict(id="s12", block="resposta2", text="Base um meio, entre zero e um: {a}vira o sinal. [p=0.2] {b}Tê dividido por quatro menor que três, [p=0.2] e {c}tê menor que doze. [p=0.3] Restam mais de vinte e cinco miligramas {d}nas primeiras doze horas. [p=0.2] Faz sentido: na hora doze, chegou exatamente a vinte e cinco."),
    # situação 3: duplicação e equação
    dict(id="s13", block="questao3", text="{a}Situação três. [p=0.2] Uma colônia começa com {b}cem bactérias e dobra a cada {c}três horas. [p=0.3] {d}Em quantas horas ela chega a três mil e duzentas bactérias?"),
    dict(id="s14", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta3", text="Vamos lá. [p=0.2] A equação: {a}cem vezes dois elevado a tê dividido por três, com a divisão toda no expoente, igual a três mil e duzentos. [p=0.3] {b}Divida cada lado por cem: [p=0.1] a potência fica igual a trinta e dois. [p=0.2] E trinta e dois é {c}dois elevado a cinco."),
    dict(id="s16", block="resposta3", text="Iguale os expoentes: {a}tê dividido por três igual a cinco. [p=0.2] Multiplique por três: {b}tê igual a quinze horas."),
    # atalho
    dict(id="s17", block="atalho", text="Aqui cabe um atalho de prova: {a}conte as dobras. [p=0.2] {b}Cem. [p=0.1] Duzentos. [p=0.1] Quatrocentos. [p=0.1] Oitocentos. [p=0.1] Mil e seiscentos. [p=0.1] Três mil e duzentos. [p=0.3] {c}Cinco dobras, [p=0.2] e {d}cinco vezes três dá quinze horas."),
    dict(id="s18", block="atalho", text="Funciona porque cada dobra é {a}um degrau do expoente. [p=0.3] Não compensa com muitas dobras, [p=0.1] como {b}de cem até cento e dois mil e quatrocentos: [p=0.2] são dez linhas de conta. [p=0.2] Aí, {c}iguale as bases."),
    # situação 4: troca de variável
    dict(id="s19", block="questao4", text="{a}Última situação, só de equação. [p=0.2] Resolva {b}nove elevado a xis, [p=0.1] menos quatro vezes três elevado a xis, [p=0.1] mais três, [p=0.1] igual a zero."),
    dict(id="s20", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta4", text="Vamos lá. [p=0.2] Nove é três ao quadrado, então {a}nove elevado a xis é o quadrado de três elevado a xis. [p=0.2] Apelido: {b}ípsilon igual a três elevado a xis. [p=0.2] Fica {c}ípsilon ao quadrado, [p=0.1] menos quatro ípsilon, [p=0.1] mais três, [p=0.1] igual a zero."),
    dict(id="s22", block="resposta4", text="Soma quatro e produto três são {a}os números um e três. [p=0.3] Volte para o xis. [p=0.2] {b}Três elevado a xis igual a três dá xis igual a um. [p=0.2] E {c}três elevado a xis igual a um? [p=0.2] Expoente zero dá um: {d}xis igual a zero."),
    dict(id="s23", block="resposta4", text="Desta vez, {a}nenhuma raiz se descarta: [p=0.1] um e três são positivos. [p=0.3] Conferindo o zero: {b}um menos quatro mais três dá zero. [p=0.2] Conferindo o um: {c}nove menos doze mais três dá zero. [p=0.2] Bateu."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}o fator vai na base e o tempo no expoente, [p=0.2] {b}iguale as bases para achar o expoente [p=0.2] e {c}confira se a resposta faz sentido."),
    dict(id="s25", block="fim", text="Na próxima aula, a pergunta {a}dois elevado a quê dá oito ganha um nome: [p=0.2] {b}logaritmo. [p=0.3] Você aprende a ler o logaritmo de oito na base dois, igual a três, como dois ao cubo igual a oito. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
