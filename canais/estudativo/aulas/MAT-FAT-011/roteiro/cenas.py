# Estudativo · MAT-FAT-011 — Soma e produto: raízes de cabeça (Matemática · Fatoração e Equação do 2º Grau).
# Habilidade: achar as raízes de x² − 7x + 12 = 0 sem fórmula, escrever x² + 5x + 6 como (x + 2)(x + 3) e montar a equação de raízes 2 e 5.
# Pré-requisitos: MAT-FAT-008 (Bhaskara), MAT-EQU-005 (chuveirinho). Próxima: MAT-FAT-012.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis"; o coeficiente a se fala "á".

TITULO = "Soma e produto: raízes de cabeça"

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
    dict(id="s01", block="gancho", text="{a}Xis ao quadrado menos sete xis mais doze igual a zero. [p=0.3] Pense em {b}dois números que somados dão sete [p=0.2] e multiplicados dão doze. [p=0.3] {c}Três e quatro. [p=0.2] Essas são as raízes, {d}sem delta e sem fórmula."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha raízes de cabeça, [p=0.2] {b}fatora o trinômio [p=0.2] e {c}monta a equação a partir das raízes."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}o chuveirinho: cada termo de um parêntese multiplica cada termo do outro. [p=0.2] E {b}a fórmula de Bhaskara, para quando o macete não servir. [p=0.3] Se faltar alguma, procure no canal."),
    # de onde vem
    dict(id="s04", block="origem", text="De onde vem isso? [p=0.2] Pegue {a}xis menos três, vezes xis menos quatro. [p=0.3] Pelo chuveirinho: {b}xis ao quadrado, menos quatro xis, menos três xis, mais doze. [p=0.2] Juntando: {c}xis ao quadrado menos sete xis mais doze."),
    dict(id="s05", block="origem", text="Repare: {a}o sete é três mais quatro, [p=0.2] e {b}o doze é três vezes quatro. [p=0.3] E essa multiplicação dá zero quando {c}xis vale três ou quatro, [p=0.2] porque {d}algum fator vale zero."),
    # regra
    dict(id="s06", block="regra", text="A regra, quando o á vale um: [p=0.2] {a}a soma das raízes é o bê com o sinal trocado. [p=0.2] {b}O produto das raízes é o cê. [p=0.3] Com o á diferente de um, {c}divida a equação inteira pelo á antes."),
    # sinais
    dict(id="s07", block="sinais", text="Com sinais, comece {a}pelo produto. [p=0.2] {b}Produto positivo: as raízes têm o mesmo sinal. [p=0.2] {c}Produto negativo: sinais contrários. [p=0.3] Depois, a soma diz {d}qual sinal ganha."),
    dict(id="s08", block="sinais", text="Em {a}xis ao quadrado mais cinco xis mais seis igual a zero: [p=0.2] {b}soma menos cinco, produto seis. [p=0.2] Produto positivo e soma negativa: {c}as duas raízes são negativas. [p=0.3] {d}Menos dois e menos três: somados dão menos cinco, multiplicados dão seis."),
    # fatorar
    dict(id="s09", block="fatorar", text="E isso fatora o trinômio. [p=0.2] Cada raiz vira {a}um parêntese: xis menos a raiz. [p=0.3] Xis menos, abre parênteses, menos dois, fecha parênteses, é {b}xis mais dois. [p=0.2] Então {c}xis ao quadrado mais cinco xis mais seis é xis mais dois, vezes xis mais três."),
    dict(id="s10", block="fatorar", text="Teste com dez: [p=0.2] {a}cem mais cinquenta mais seis, cento e cinquenta e seis. [p=0.2] {b}Doze vezes treze, também. [p=0.2] Bateu."),
    # montar
    dict(id="s11", block="montar", text="E o caminho de volta: {a}a equação de raízes dois e cinco. [p=0.2] {b}Soma sete, produto dez. [p=0.2] O bê é a soma com sinal trocado, e o cê é o produto: [p=0.2] {c}xis ao quadrado menos sete xis mais dez igual a zero. [p=0.3] Conferindo o dois: {d}quatro menos catorze mais dez, zero."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}esquecer de trocar o sinal da soma. [p=0.2] Em xis ao quadrado mais cinco xis mais seis, a pessoa procura números que somam {b}mais cinco: [p=0.2] {c}dois e três. [p=0.3] Teste o dois: {d}quatro mais dez mais seis, vinte. [p=0.2] Não deu zero. [p=0.2] {e}A soma é o bê com o sinal trocado."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho de prova: {a}liste os pares que dão o produto. [p=0.2] Em xis ao quadrado menos sete xis mais doze: [p=0.2] {b}um e doze, [p=0.1] dois e seis, [p=0.1] três e quatro. [p=0.3] {c}Só três e quatro somam sete."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o produto tem poucos pares de inteiros, e a soma tem infinitos. [p=0.3] {b}Não compensa quando as raízes não são inteiras, [p=0.2] como em {c}xis ao quadrado menos dois xis menos um. [p=0.2] {d}Se nenhum par servir em poucos segundos, vá de Bhaskara."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Ache de cabeça as raízes de {a}xis ao quadrado mais dois xis menos quinze igual a zero. [p=0.3] Depois, {b}monte a equação de raízes menos um e quatro."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Soma menos dois, produto menos quinze. [p=0.2] Produto negativo: {b}sinais contrários. [p=0.2] Pares de quinze: {c}um e quinze, três e cinco. [p=0.3] Para a soma dar menos dois, o menos vai no número mais longe do zero: {d}três e menos cinco."),
    dict(id="s18", block="resposta", text="Na segunda parte: {a}menos um mais quatro, soma três. [p=0.2] {b}Menos um vezes quatro, produto menos quatro. [p=0.3] Bê é a soma com sinal trocado: {c}xis ao quadrado menos três xis menos quatro igual a zero."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}com á igual a um, a soma das raízes é menos bê [p=0.2] e {b}o produto é cê. [p=0.2] {c}Comece pelo produto."),
    dict(id="s20", block="fim", text="Na próxima aula, a equação do segundo grau sai de {a}problemas: [p=0.2] {b}dois números seguidos com produto cento e cinquenta e seis, [p=0.2] e {c}a altura de uma bola que sobe e cai. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
