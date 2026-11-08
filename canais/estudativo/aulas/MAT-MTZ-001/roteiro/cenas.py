# Estudativo · MAT-MTZ-001 — O que é matriz: soma e multiplicação por número (Matemática · Matrizes e Sistemas).
# Habilidade: montar a matriz 2x2 de aᵢⱼ = i + j, achar a transposta, somar duas matrizes e multiplicar uma por 3.
# Pré-requisitos: MAT-EQU-002 (valor numérico). Próxima: MAT-MTZ-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. aᵢⱼ narrado "a i jota"; a₂₁ narrado "a dois um".
# Soma de frações não está na ficha: todos os elementos são inteiros.

TITULO = "O que é matriz: soma e multiplicação por número"

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
    dict(id="s01", block="gancho", text="{a}Olhe esta tabela de números. [p=0.2] Quanto vale o elemento {b}a dois um? [p=0.3] Se você respondeu {c}cinco, [p=0.2] leu na ordem errada. [p=0.3] A resposta é {d}três."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você monta uma matriz, acha a transposta, soma e multiplica por número, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}uma coisa: [p=0.2] {b}trocar a letra por um número e fazer a conta. [p=0.3] Por exemplo, {c}dois xis menos três, para xis igual a cinco, [p=0.2] dá {d}dez menos três, sete. [p=0.3] Se faltar, procure no canal."),
    # o que é matriz
    dict(id="s04", block="tabela", text="Pense no {a}boletim de dois alunos, em três provas. [p=0.2] {b}Ana tirou sete, cinco e oito. [p=0.2] {c}Bruno tirou seis, nove e quatro."),
    dict(id="s05", block="tabela", text="Tire os nomes, {a}cerque os números com colchetes, [p=0.2] e você tem uma {b}matriz: [p=0.2] números organizados em {c}linhas, que ficam deitadas, [p=0.2] e {d}colunas, que ficam em pé."),
    dict(id="s06", block="tabela", text="Essa matriz tem {a}duas linhas e três colunas. [p=0.2] Por isso, ela é uma matriz {b}dois por três. [p=0.3] {c}Sempre as linhas primeiro, depois as colunas."),
    # endereço
    dict(id="s07", block="endereco", text="Cada número da matriz é um {a}elemento, e cada elemento tem um endereço. [p=0.3] {b}a um três é o elemento da linha um, coluna três: [p=0.2] {c}a nota da Ana na terceira prova, oito."),
    dict(id="s08", block="endereco", text="Os números pequenos dizem {a}primeiro a linha, depois a coluna. [p=0.3] Para falar de qualquer elemento, a linha vira a letra {b}i, [p=0.2] e a coluna vira a letra {c}jota. [p=0.3] {d}a i jota é o elemento da linha i, coluna jota."),
    # lei de formação
    dict(id="s09", block="lei", text="Às vezes, a questão não dá os números. [p=0.2] Ela dá uma {a}regra para montar a matriz. [p=0.3] Por exemplo: matriz dois por dois, com {b}a i jota igual a i mais jota. [p=0.3] É trocar letra por número, como no valor numérico."),
    dict(id="s10", block="lei", text="{a}Linha um, coluna um: um mais um, dois. [p=0.2] {b}Linha um, coluna dois: um mais dois, três. [p=0.2] {c}Linha dois, coluna um: dois mais um, três. [p=0.2] {d}Linha dois, coluna dois: dois mais dois, quatro."),
    # transposta
    dict(id="s11", block="transposta", text="A {a}transposta de uma matriz troca linhas por colunas. [p=0.2] {b}A primeira linha vira a primeira coluna. [p=0.2] {c}A segunda linha vira a segunda coluna. [p=0.3] Ela leva um {d}tê pequeno no alto do nome."),
    dict(id="s12", block="transposta", text="No boletim, {a}cada aluno passa a ser uma coluna. [p=0.2] A matriz dois por três {b}vira três por dois."),
    # somar
    dict(id="s13", block="somar", text="Para {a}somar duas matrizes, [p=0.2] some {b}cada elemento com o elemento do mesmo lugar. [p=0.3] {c}Dois mais um, três. [p=0.2] {d}Três com menos um, dois. [p=0.2] {e}Três mais zero, três. [p=0.2] {f}Quatro mais cinco, nove."),
    dict(id="s14", block="somar", text="Por isso, {a}só dá para somar matrizes do mesmo tamanho. [p=0.2] Uma dois por dois com uma dois por três? [p=0.2] {b}Sobram elementos sem par, e a soma não existe."),
    # número vezes matriz
    dict(id="s15", block="numero", text="E {a}três vezes uma matriz? [p=0.2] O três {b}multiplica cada elemento. [p=0.3] Três vezes dois, três, três, quatro dá {c}seis, nove, nove, doze."),
    # erro
    dict(id="s16", block="erro", text="Agora, cuidado com o erro mais comum: [p=0.2] {a}ler o endereço ao contrário. [p=0.3] {b}a dois um é linha dois, coluna um: [p=0.2] o {c}três. [p=0.3] Quem vai primeiro na coluna pega o {d}cinco, [p=0.2] que é o a um dois. [p=0.3] {e}Linha primeiro, sempre."),
    # atalho
    dict(id="s17", block="atalho", text="Agora o atalho: [p=0.2] {a}se a regra não muda quando você troca i por jota, [p=0.2] {b}a transposta é a própria matriz. [p=0.3] {c}i mais jota dá o mesmo que jota mais i, [p=0.2] então a transposta de dois, três, três, quatro {d}é ela mesma. [p=0.2] Não precisa montar."),
    dict(id="s18", block="atalho", text="Funciona porque a transposta {a}troca o elemento i jota com o elemento jota i. [p=0.3] Se eles são iguais, nada muda. [p=0.3] {b}Não vale para i menos jota: [p=0.2] {c}um menos dois dá menos um, [p=0.2] mas {d}dois menos um dá um."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] A matriz A é dois por dois, com {a}a i jota igual a dois i menos jota. [p=0.3] {b}Calcule A mais a transposta de A."),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] Dois i é duas vezes o número da linha. [p=0.2] {a}Na linha um: dois menos um, um, [p=0.2] e dois menos dois, zero. [p=0.3] {b}Na linha dois: quatro menos um, três, [p=0.2] e quatro menos dois, dois."),
    dict(id="s22", block="resposta", text="A transposta {a}põe as linhas em pé: [p=0.2] um e três em cima, zero e dois embaixo. [p=0.3] Somando lugar com lugar: [p=0.2] {b}dois, três, três, quatro. [p=0.3] {c}A matriz do i mais jota de novo."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}primeiro a linha, depois a coluna. [p=0.2] {b}Na soma, lugar com lugar. [p=0.2] {c}O número multiplica todos os elementos."),
    dict(id="s24", block="fim", text="Na próxima aula, você multiplica {a}uma matriz por outra, linha por coluna, [p=0.2] e descobre que {b}a ordem muda o resultado. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
