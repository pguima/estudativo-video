# Estudativo · MAT-MTZ-003 — Determinante de 2ª e 3ª ordem (Matemática · Matrizes e Sistemas).
# Habilidade: calcular o determinante de [1 2; 3 4], que dá −2, e o de uma matriz 3x3 pela regra de Sarrus.
# Pré-requisitos: MAT-MTZ-001 (matriz, aᵢⱼ). Próxima: MAT-MTZ-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Multiplicação de matrizes (MAT-MTZ-002) não está na ficha: não é usada.
# Matrizes narradas pela ordem de leitura, linha por linha.

TITULO = "Determinante de 2ª e 3ª ordem"

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
    dict(id="s01", block="gancho", text="{a}Um, dois, três, quatro. [p=0.2] O determinante dessa matriz é {b}dois ou menos dois? [p=0.3] Quem faz a conta na ordem errada acha {c}dois. [p=0.3] A resposta é {d}menos dois."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula o determinante de matrizes dois por dois e três por três, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre {a}duas coisas: [p=0.2] {b}matriz é uma tabela de números em linhas e colunas, [p=0.2] e {c}a i jota é o elemento da linha i, coluna jota. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="oque", text="O determinante é {a}um número calculado a partir de uma matriz. [p=0.2] Ele só existe na {b}matriz quadrada: [p=0.2] a que tem {c}o mesmo número de linhas e de colunas, como dois por dois ou três por três. [p=0.3] Para que ele serve? [p=0.2] Você vê na {d}aula de matriz inversa."),
    dict(id="s05", block="oque", text="Numa matriz quadrada, há duas diagonais. [p=0.2] {a}A diagonal principal desce da esquerda para a direita: um e quatro. [p=0.3] {b}A diagonal secundária sobe da esquerda para a direita: três e dois."),
    # dois por dois
    dict(id="s06", block="dois", text="A regra da dois por dois: [p=0.2] {a}multiplique a principal, [p=0.2] {b}multiplique a secundária, [p=0.2] e {c}faça a principal menos a secundária."),
    dict(id="s07", block="dois", text="{a}Um vezes quatro, quatro. [p=0.2] {b}Três vezes dois, seis. [p=0.2] {c}Quatro menos seis, menos dois. [p=0.3] Na tela, o determinante aparece entre {d}duas barras em pé, no lugar dos colchetes."),
    # com negativo
    dict(id="s08", block="negativo", text="Com número negativo, {a}cuidado com o sinal. [p=0.2] Veja {b}três, menos dois, cinco, um. [p=0.3] {c}Principal: três vezes um, três. [p=0.2] {d}Secundária: cinco vezes menos dois, menos dez. [p=0.3] {e}Três menos, abre parênteses, menos dez, fecha parênteses: [p=0.2] três mais dez, {f}treze."),
    # Sarrus
    dict(id="s09", block="sarrus", text="E na três por três? [p=0.2] Use {a}a regra de Sarrus. [p=0.2] Primeiro, {b}copie as duas primeiras colunas ao lado da matriz."),
    dict(id="s10", block="sarrus", text="{a}Agora, três diagonais descendo, como a principal. [p=0.2] {b}Dois vezes um vezes dois, quatro. [p=0.2] {c}Um vezes quatro vezes um, quatro. [p=0.2] {d}Três vezes zero vezes zero, zero. [p=0.2] Somando, {e}oito."),
    dict(id="s11", block="sarrus", text="{a}Depois, três diagonais subindo, como a secundária. [p=0.2] {b}Um vezes um vezes três, três. [p=0.2] {c}Zero vezes quatro vezes dois, zero. [p=0.2] {d}Dois vezes zero vezes um, zero. [p=0.2] Somando, {e}três."),
    dict(id="s12", block="sarrus", text="{a}Descendo menos subindo: [p=0.2] oito menos três, {b}cinco. [p=0.3] É a mesma ideia da dois por dois: {c}o que desce, menos o que sobe."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}fazer a secundária menos a principal. [p=0.3] Em um, dois, três, quatro, {b}seis menos quatro dá dois, com o sinal trocado. [p=0.3] {c}A principal vem primeiro: a que desce."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: [p=0.2] {a}se tudo abaixo da diagonal principal for zero, [p=0.2] {b}o determinante é só o produto da diagonal. [p=0.3] Em dois, cinco, sete; zero, três, um; zero, zero, quatro: [p=0.2] {c}dois vezes três vezes quatro, vinte e quatro."),
    dict(id="s15", block="atalho", text="Funciona porque, no Sarrus, {a}todas as outras diagonais passam por um zero, [p=0.2] e qualquer número vezes zero dá zero. [p=0.3] {b}Vale também se o zerado for tudo acima da diagonal. [p=0.3] {c}Com o zero fora desse lugar, faça o Sarrus inteiro. [p=0.3] E uma {d}linha inteira de zeros? [p=0.2] Toda diagonal passa por ela: {e}o determinante é zero."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Calcule o determinante da matriz {a}um, dois, zero; [p=0.2] três, um, dois; [p=0.2] zero, um, um."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Copie as duas primeiras colunas. [p=0.2] Descendo: {b}um vezes um vezes um, um; [p=0.2] {c}dois vezes dois vezes zero, zero; [p=0.2] {d}zero vezes três vezes um, zero. [p=0.2] Total descendo: {e}um."),
    dict(id="s19", block="resposta", text="Subindo: {a}zero vezes um vezes zero, zero; [p=0.2] {b}um vezes dois vezes um, dois; [p=0.2] {c}um vezes três vezes dois, seis. [p=0.2] Total subindo: {d}oito. [p=0.3] {e}Um menos oito: menos sete."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}na dois por dois, principal menos secundária. [p=0.2] {b}Na três por três, Sarrus: o que desce menos o que sobe."),
    dict(id="s21", block="fim", text="Na próxima aula, você usa o determinante para achar {a}a matriz inversa, [p=0.2] e descobre por que {b}determinante zero é um problema. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
