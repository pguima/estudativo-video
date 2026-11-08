# Estudativo · MAT-EQU-006 — Praticando: expressões algébricas (Matemática · Equações do 1º Grau · prática).
# Habilidade: traduzir situações para expressões com letra e simplificá-las.
# Pré-requisitos: MAT-EQU-001, MAT-EQU-002, MAT-EQU-003, MAT-EQU-004, MAT-EQU-005. Próxima: MAT-EQU-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis".
# Questões inéditas, criadas para esta aula. Equação ainda não foi ensinada (MAT-EQU-007).
# 1: x + (2x − 3) + (x + 5) = 4x + 2 (x = 10: 10 + 17 + 15 = 42).
# 2: x² − 3x + 2, x = −2 → 4 − (−6) + 2 = 12; perdendo o sinal, 4 − 6 + 2 = 0.
# 3: 4(x − 2) − (2x − 5) = 2x − 3; teste do zero: 4 × (−2) − (−5) = −3; teste do dez: 32 − 15 = 17.
# 4: lado 3x → 3x · 3x = 9x² (x = 10: 30 × 30 = 900; erros 6x e 9x).
# 5: (x + 5)(x + 2) = x² + 7x + 10 (x = 0: 10; x = 10: 15 × 12 = 180).

TITULO = "Praticando: expressões algébricas"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações com letra, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar cinco ferramentas: [p=0.2] {a}traduzir frases, [p=0.2] {b}trocar a letra por número entre parênteses, [p=0.2] {c}juntar termos semelhantes, [p=0.2] {d}abrir parênteses [p=0.2] e {e}multiplicar com letra. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: traduzir e juntar
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Ana tem {b}xis figurinhas. [p=0.2] Bia tem {c}três a menos que o dobro de Ana. [p=0.2] Caio tem {d}cinco a mais que Ana. [p=0.3] {e}Escreva, na forma mais curta, quantas figurinhas eles têm juntos."),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá, pessoa por pessoa. [p=0.2] {a}Ana: xis. [p=0.2] {b}Bia: três a menos que o dobro. [p=0.2] Primeiro o dobro de Ana, dois xis, [p=0.2] e depois tire três: dois xis menos três. [p=0.3] Quem escreveu três menos dois xis inverteu a ordem. [p=0.3] {c}Caio: xis mais cinco. [p=0.3] Juntos: {d}xis mais dois xis menos três mais xis mais cinco."),
    dict(id="s06", block="resposta1", text="Termos com xis: {a}um mais dois mais um dá quatro xis. [p=0.2] Números soltos: {b}menos três mais cinco dá mais dois. [p=0.3] Resposta: {c}quatro xis mais dois. [p=0.2] Esse é o total de figurinhas. [p=0.3] Se Ana tiver dez: [p=0.2] {d}dez mais dezessete mais quinze dá quarenta e dois, [p=0.2] e {e}quatro vezes dez mais dois também."),
    # situação 2: valor numérico
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Calcule {b}xis ao quadrado menos três xis mais dois, [p=0.2] para {c}xis igual a menos dois."),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá, com parênteses: [p=0.2] {a}abre parênteses, menos dois, fecha parênteses, ao quadrado, [p=0.2] menos três vezes, abre parênteses, menos dois, fecha parênteses, [p=0.2] mais dois. [p=0.3] Com o menos dentro do parêntese, expoente par apaga o sinal: {b}a potência dá quatro. [p=0.2] {c}Três vezes menos dois dá menos seis."),
    dict(id="s10", block="resposta2", text="Fica {a}quatro menos, abre parênteses, menos seis, fecha parênteses, mais dois. [p=0.2] Tirar uma dívida é como ganhar: [p=0.2] {b}quatro mais seis mais dois dá {c}doze. [p=0.3] Quem fez quatro menos seis mais dois chegou em {d}zero: [p=0.2] perdeu o sinal pelo caminho."),
    # situação 3: distributiva e menos antes do parêntese
    dict(id="s11", block="questao3", text="{a}Situação três. [p=0.2] Simplifique: {b}quatro, abre parênteses, xis menos dois, fecha parênteses, [p=0.2] {c}menos, abre parênteses, dois xis menos cinco, fecha parênteses."),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] Primeiro parêntese: {a}quatro xis menos oito. [p=0.2] O segundo tem menos sozinho na frente, [p=0.2] então troque todos os sinais: {b}menos dois xis mais cinco. [p=0.3] Junte: {c}quatro xis menos dois xis dá dois xis. [p=0.2] {d}Menos oito mais cinco dá menos três. [p=0.3] Resposta: {e}dois xis menos três."),
    # atalho
    dict(id="s14", block="atalho", text="Aqui cabe um atalho de prova: {a}o teste do zero. [p=0.2] {b}Troque o xis por zero na expressão do começo. [p=0.3] {c}No primeiro parêntese, zero menos dois dá menos dois, [p=0.2] e quatro vezes menos dois dá menos oito. [p=0.2] {d}No segundo, dois vezes zero é zero, e zero menos cinco dá menos cinco. [p=0.2] Menos, abre parênteses, menos cinco, fecha parênteses, dá mais cinco. [p=0.2] Total: {e}menos três. [p=0.3] É o mesmo número solto da resposta: {f}bateu."),
    dict(id="s15", block="atalho", text="Funciona porque {a}zero vezes qualquer número dá zero: [p=0.2] todo termo com xis some, [p=0.2] e sobra {b}só o número solto. [p=0.3] É rápido, mas {c}não confere a parte com xis. [p=0.2] Para isso, {d}use o teste do dez."),
    # situação 4: termo vezes termo
    dict(id="s16", block="questao4", text="{a}Situação quatro. [p=0.2] Uma sala quadrada tem {b}três xis metros de lado. [p=0.3] {c}Escreva a área da sala."),
    dict(id="s17", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta4", text="Vamos lá. [p=0.2] No quadrado, os lados são iguais, [p=0.2] e a área é um lado vezes o outro: {a}três xis vezes três xis. [p=0.3] {b}Três vezes três dá nove. [p=0.2] {c}Xis vezes xis dá xis ao quadrado. [p=0.3] Resposta: {d}nove xis ao quadrado. [p=0.3] Quem somou chegou em {e}seis xis. [p=0.2] Quem esqueceu uma letra ficou com {f}nove xis. [p=0.3] Com dez: {g}trinta vezes trinta dá novecentos, [p=0.2] e {h}nove vezes cem também."),
    # situação 5: duas expressões multiplicadas
    dict(id="s19", block="questao5", text="{a}Última situação, e ela junta tudo. [p=0.2] Um terreno retangular tem {b}frente de xis mais cinco metros [p=0.2] e {c}fundo de xis mais dois metros. [p=0.3] {d}Escreva a área do terreno sem parênteses."),
    dict(id="s20", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta5", text="Vamos lá. [p=0.2] Área de retângulo é um lado vezes o outro: [p=0.2] {a}abre parênteses, xis mais cinco, fecha parênteses, [p=0.2] vezes, abre parênteses, xis mais dois, fecha parênteses. [p=0.3] Pelo atalho: [p=0.2] {b}na frente, xis ao quadrado. [p=0.2] {c}No meio, cinco mais dois: sete xis. [p=0.2] {d}No fim, cinco vezes dois: dez."),
    dict(id="s22", block="resposta5", text="A área é {a}xis ao quadrado mais sete xis mais dez. [p=0.3] Confira com os testes. [p=0.2] {b}Com xis igual a zero, a conta fica cinco vezes dois, que dá dez: o número solto bate. [p=0.2] {c}Com xis igual a dez, a área fica quinze vezes doze, que dá cento e oitenta, [p=0.2] e {d}cem mais setenta mais dez também."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}traduza pedaço por pedaço, [p=0.2] {b}troque a letra sempre com parênteses [p=0.2] e {c}confira com um número."),
    dict(id="s24", block="fim", text="Na próxima aula, a expressão ganha {a}um sinal de igual e vira equação. [p=0.3] Você testa se um número resolve [p=0.2] e conhece {b}a ideia da balança: [p=0.2] {c}fazer o mesmo nos dois lados. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
