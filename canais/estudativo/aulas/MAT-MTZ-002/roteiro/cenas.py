# Estudativo · MAT-MTZ-002 — Multiplicar matrizes: linha por coluna (Matemática · Matrizes e Sistemas).
# Habilidade: dizer pelo tamanho se o produto existe, multiplicar duas matrizes 2x2 e mostrar que AB pode ser diferente de BA.
# Pré-requisitos: MAT-MTZ-001 (matriz, tamanho, aᵢⱼ, soma). Próxima: MAT-MTZ-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Matrizes narradas pela ordem de leitura: "um, dois, zero, um" = [1 2; 0 1].

TITULO = "Multiplicar matrizes: linha por coluna"

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
    dict(id="s01", block="gancho", text="{a}Duas matrizes dois por dois. [p=0.2] Para multiplicar, muita gente faz {b}elemento com elemento, como na soma. [p=0.3] {c}Está errado. [p=0.3] Matriz vezes matriz é {d}linha por coluna, [p=0.2] e trocar a ordem {e}pode mudar o resultado."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você multiplica duas matrizes e sabe pelo tamanho se o produto existe, [p=0.2] com um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre {a}duas coisas: [p=0.2] {b}o tamanho de uma matriz é linhas por colunas, [p=0.2] e {c}a i jota é o elemento da linha i, coluna jota. [p=0.3] Se faltar alguma, procure no canal."),
    # lanchonete
    dict(id="s04", block="lanche", text="Por que linha por coluna? [p=0.2] Numa lanchonete, {a}você pede dois sanduíches e três sucos. [p=0.2] {b}O sanduíche custa oito reais, e o suco, cinco."),
    dict(id="s05", block="lanche", text="A conta é {a}dois vezes oito, mais três vezes cinco: [p=0.2] {b}dezesseis mais quinze, trinta e um reais. [p=0.3] Repare: {c}os pedidos estão deitados, numa linha. [p=0.2] {d}Os preços estão em pé, numa coluna."),
    dict(id="s06", block="lanche", text="{a}O primeiro da linha vezes o primeiro da coluna, [p=0.2] {b}mais o segundo vezes o segundo. [p=0.3] Isso é {c}linha vezes coluna, [p=0.2] e é assim que se multiplicam matrizes."),
    # produto
    dict(id="s07", block="produto", text="Vamos multiplicar {a}A, que é um, dois, zero, um, [p=0.2] por {b}B, que é um, zero, três, um. [p=0.3] {c}Cada elemento do resultado vem de uma linha de A com uma coluna de B."),
    dict(id="s08", block="produto", text="{a}Linha um de A com coluna um de B: [p=0.2] um vezes um, mais dois vezes três. [p=0.2] {b}Um mais seis, sete. [p=0.3] Ele vai para {c}a linha um, coluna um."),
    dict(id="s09", block="produto", text="{a}Linha um com coluna dois: [p=0.2] um vezes zero, mais dois vezes um: {b}dois."),
    dict(id="s10", block="produto", text="{a}Linha dois com coluna um: [p=0.2] zero vezes um, mais um vezes três: {b}três. [p=0.3] {c}Linha dois com coluna dois: [p=0.2] zero vezes zero, mais um vezes um: {d}um."),
    dict(id="s11", block="produto", text="{a}A vezes B dá sete, dois, três, um. [p=0.3] É o endereço de novo: {b}a linha i de A com a coluna jota de B dá o elemento i jota."),
    # ordem
    dict(id="s12", block="ordem", text="Agora, troque a ordem: {a}B vezes A. [p=0.2] {b}Linha um de B com coluna um de A: [p=0.2] um vezes um, mais zero vezes zero: um. [p=0.3] Fazendo o resto do mesmo jeito, sai {c}um, dois, três, sete."),
    dict(id="s13", block="ordem", text="{a}A vezes B deu sete, dois, três, um. [p=0.2] {b}B vezes A deu um, dois, três, sete. [p=0.3] Com números, três vezes cinco é cinco vezes três. [p=0.2] {c}Com matrizes, a ordem pode mudar o resultado."),
    # tamanho
    dict(id="s14", block="tamanho", text="E quando o produto existe? [p=0.2] Cada linha de A precisa ter {a}o mesmo tanto de números que cada coluna de B. [p=0.2] Senão, {b}sobra número sem par."),
    dict(id="s15", block="tamanho", text="Ou seja: {a}o número de colunas de A tem que ser igual ao número de linhas de B. [p=0.3] E o resultado fica com {b}as linhas de A e as colunas de B."),
    # erro
    dict(id="s16", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}multiplicar elemento com elemento, como na soma. [p=0.3] Em A vezes B, daria {b}um, zero, zero, um. [p=0.3] {c}Não bate com o sete, dois, três, um. [p=0.3] Na multiplicação, {d}é sempre linha com coluna."),
    # atalho
    dict(id="s17", block="atalho", text="Agora o atalho do tamanho: [p=0.2] {a}escreva os tamanhos lado a lado. [p=0.2] {b}Dois por três, vezes três por quatro. [p=0.3] {c}Os números do meio são iguais? O produto existe. [p=0.3] {d}Os de fora dão o tamanho do resultado: dois por quatro."),
    dict(id="s18", block="atalho", text="Funciona porque {a}os do meio contam os números que vão se encontrar, linha com coluna. [p=0.3] E serve para {b}pegar a ordem trocada: [p=0.2] três por quatro, vezes dois por três? [p=0.2] {c}Quatro e dois são diferentes: não existe."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] {a}A é dois, um, zero, três. [p=0.2] {b}B é um, quatro, dois, zero. [p=0.3] {c}Calcule A vezes B."),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] {a}Linha um com coluna um: [p=0.2] dois vezes um, mais um vezes dois: quatro. [p=0.3] {b}Linha um com coluna dois: [p=0.2] dois vezes quatro, mais um vezes zero: oito."),
    dict(id="s22", block="resposta", text="{a}Linha dois com coluna um: [p=0.2] zero vezes um, mais três vezes dois: seis. [p=0.3] {b}Linha dois com coluna dois: [p=0.2] zero vezes quatro, mais três vezes zero: zero. [p=0.3] {c}Quatro, oito, seis, zero."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}linha da primeira com coluna da segunda, [p=0.2] {b}multiplica par a par e soma, [p=0.2] e {c}a ordem importa."),
    dict(id="s24", block="fim", text="Na próxima aula, você calcula {a}o determinante, um número que resume uma matriz, [p=0.2] até nas {b}três por três, pela regra de Sarrus. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
