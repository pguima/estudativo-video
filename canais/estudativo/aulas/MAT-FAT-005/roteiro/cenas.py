# Estudativo · MAT-FAT-005 — Racionalizar denominadores: pela raiz e pelo conjugado (Matemática · Fatoração e Equação do 2º Grau).
# Habilidade: transformar 1/√2 em √2/2 multiplicando em cima e embaixo pela raiz e 2/(√3 − 1) em √3 + 1 pelo conjugado.
# Pré-requisitos: MAT-FAT-015 (soma vezes diferença), MAT-FRA-003 (equivalentes), MAT-POT-009 (radicais). Próxima: MAT-FAT-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. "Número racional" explicado na hora. FAT-004 fora de "Já ensinado": simplificação dita como em FRA-003.
# 1/√2 = √2/2 (≈ 0,707; √2 ≈ 1,4) · 6/√3 = 6√3/3 = 2√3 · (√3 − 1)·√3 = 3 − √3 · (√3 − 1)(√3 + 1) = 2 → 2/(√3 − 1) = √3 + 1.
# Erro: 1/√2 → 1/2 = 0,5 contra ≈ 0,7. Atalho: 1/√5 = √5/5; (√5 + √2)(√5 − √2) = 3.
# Questão: 4/(√5 + 1) = 4(√5 − 1)/4 = √5 − 1; errado: (√5 + 1)·√5 = 5 + √5.

TITULO = "Racionalizar denominadores"

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
    dict(id="s01", block="gancho", text="{a}Um dividido por raiz de dois. [p=0.3] Raiz de dois vale perto de {b}um vírgula quatro, [p=0.2] e dividir por um número quebrado assim, à mão, dá trabalho. [p=0.3] Mas essa fração é igual a {c}raiz de dois dividido por dois: [p=0.2] a metade de um vírgula quatro, {d}perto de zero vírgula sete."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você tira a raiz de baixo da fração, [p=0.2] até quando ela vem com {b}uma soma ou uma subtração."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}três coisas. [p=0.2] {b}Multiplicar em cima e embaixo pelo mesmo número não muda a fração. [p=0.2] {c}Raiz de dois vezes raiz de dois dá dois. [p=0.2] E {d}soma vezes diferença dá quadrado menos quadrado. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="nome", text="Tirar a raiz do denominador tem nome: {a}racionalizar. [p=0.2] Vem de {b}número racional, aquele que pode ser escrito como fração de números inteiros. [p=0.2] Raiz de dois não pode. [p=0.3] Racionalizar é deixar {c}o de baixo sem raiz, sem mudar o valor."),
    # raiz sozinha
    dict(id="s05", block="raiz", text="O primeiro caso é a {a}raiz sozinha embaixo. [p=0.2] Em {b}um dividido por raiz de dois, [p=0.2] multiplique {c}em cima e embaixo por raiz de dois. [p=0.3] Multiplicar em cima e embaixo pelo mesmo número {d}não muda o valor da fração."),
    dict(id="s06", block="raiz", text="{a}Em cima: um vezes raiz de dois, raiz de dois. [p=0.2] {b}Embaixo: raiz de dois vezes raiz de dois, dois. [p=0.3] Fica {c}raiz de dois dividido por dois. [p=0.2] Sem raiz embaixo."),
    dict(id="s07", block="raiz", text="Outro: {a}seis dividido por raiz de três. [p=0.2] {b}Multiplique em cima e embaixo por raiz de três: [p=0.2] {c}seis raiz de três, dividido por três. [p=0.3] E ainda simplifica: {d}seis dividido por três dá dois. [p=0.2] Resposta: {e}dois raiz de três."),
    # conjugado
    dict(id="s08", block="conjugado", text="O segundo caso tem {a}soma ou subtração embaixo: [p=0.2] {b}dois dividido por, abre parênteses, raiz de três menos um, fecha parênteses. [p=0.3] Multiplicar por raiz de três não resolve: [p=0.2] embaixo ficaria {c}três menos raiz de três, ainda com raiz."),
    dict(id="s09", block="conjugado", text="A saída é o {a}conjugado: os mesmos termos, com o sinal do meio trocado. [p=0.2] O conjugado de raiz de três menos um é {b}raiz de três mais um. [p=0.3] Embaixo, aparece {c}soma vezes diferença: [p=0.2] {d}raiz de três ao quadrado menos um ao quadrado. [p=0.2] {e}Três menos um: dois."),
    dict(id="s10", block="conjugado", text="{a}Em cima, dois vezes, abre parênteses, raiz de três mais um, fecha parênteses. [p=0.3] Embaixo ficou dois. [p=0.2] {b}Divida em cima e embaixo por dois. [p=0.2] Resposta: {c}raiz de três mais um."),
    dict(id="s11", block="conjugado", text="Para conferir, {a}a resposta vezes o de baixo original tem que dar o de cima. [p=0.2] {b}Raiz de três mais um, vezes raiz de três menos um: [p=0.2] {c}três menos um dá dois. [p=0.2] Bateu."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}multiplicar só embaixo. [p=0.2] A pessoa pega um dividido por raiz de dois [p=0.2] e escreve {b}um dividido por dois. [p=0.3] Mas um meio é {c}zero vírgula cinco, [p=0.2] e a fração original vale {d}perto de zero vírgula sete. [p=0.3] {e}Se o de baixo foi multiplicado, o de cima tem que acompanhar."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}você sabe o de baixo final antes de fazer conta. [p=0.3] {b}Raiz sozinha: embaixo fica o número de dentro. [p=0.2] Um dividido por raiz de cinco vira {c}raiz de cinco dividido por cinco. [p=0.3] {d}Com conjugado: embaixo fica o quadrado do primeiro menos o quadrado do segundo. [p=0.2] Com raiz de cinco mais raiz de dois embaixo, o de baixo final é {e}cinco menos dois: três."),
    dict(id="s14", block="atalho", text="Funciona porque {a}raiz vezes raiz devolve o número de dentro, [p=0.2] e {b}soma vezes diferença apaga o meio. [p=0.3] {c}Não compensa racionalizar quando as alternativas deixam a raiz embaixo: [p=0.2] aí, compare do jeito que está."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Racionalize {a}quatro dividido por, abre parênteses, raiz de cinco mais um, fecha parênteses."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] O conjugado é {a}raiz de cinco menos um. [p=0.2] Embaixo, pelo atalho: {b}cinco menos um dá quatro. [p=0.2] Em cima: {c}quatro, abre parênteses, raiz de cinco menos um, fecha parênteses. [p=0.3] {d}Divida em cima e embaixo por quatro. [p=0.2] Resposta: {e}raiz de cinco menos um."),
    dict(id="s18", block="resposta", text="Quem multiplicou só por raiz de cinco ficou com {a}cinco mais raiz de cinco embaixo: [p=0.2] {b}a raiz continuou lá."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}raiz sozinha, multiplique pela própria raiz. [p=0.2] {b}Com soma ou subtração, pelo conjugado. [p=0.2] E {c}sempre em cima e embaixo."),
    dict(id="s20", block="fim", text="Na próxima aula, você {a}pratica tudo desta parte do curso: [p=0.2] {b}abrir produtos notáveis, [p=0.2] {c}fatorar, [p=0.2] {d}simplificar frações com letra [p=0.2] e {e}racionalizar. [p=0.3] {f}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {g}Bons estudos!"),
]
