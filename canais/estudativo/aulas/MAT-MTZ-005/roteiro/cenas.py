# Estudativo · MAT-MTZ-005 — Praticando: matrizes e determinantes (Matemática · Matrizes e Sistemas · prática).
# Habilidade: operar com matrizes, calcular determinantes e achar a inversa de uma matriz 2x2.
# Pré-requisitos: MAT-MTZ-001, MAT-MTZ-002, MAT-MTZ-003, MAT-MTZ-004. Próxima: MAT-MTZ-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Cinco questões inéditas, criadas para esta aula. Matrizes narradas pela ordem de leitura, linha por linha.
# Equação (achar k) não está na ficha: nenhuma questão pede para resolver equação.

TITULO = "Praticando: matrizes e determinantes"

VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que passou anos sem estudar: voz masculina, grave, calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína; mostre "
            "surpresa no erro, entusiasmo no atalho e dê ênfase forte às palavras-chave. Ritmo tranquilo, com pausas "
            "naturais entre as ideias. Leia exatamente o texto, sem repetir nem acrescentar nada."),
)

SCENES = [
    # abertura
    dict(id="s01", block="gancho", text="{a}Cinco questões de matrizes e determinantes, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}o endereço a i jota, linha antes da coluna; [p=0.2] {b}a multiplicação linha por coluna; [p=0.2] {c}o determinante, o que desce menos o que sobe; [p=0.2] e {d}a receita da inversa. [p=0.3] Se faltar alguma, procure no canal."),
    # questão 1
    dict(id="s03", block="questao1", text="{a}Questão um. [p=0.2] A matriz A é dois por dois, com {b}a i jota igual a i vezes jota. [p=0.2] B é {c}um, menos um, zero, dois. [p=0.3] {d}Calcule a transposta de A, mais três vezes B."),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Montando A: {a}um vezes um, um; um vezes dois, dois; [p=0.2] dois vezes um, dois; dois vezes dois, quatro. [p=0.3] E a transposta? [p=0.2] {b}I vezes jota dá o mesmo que jota vezes i, [p=0.2] então {c}a transposta é a própria A. [p=0.2] Nem precisa montar."),
    dict(id="s06", block="resposta1", text="Três vezes B: {a}três, menos três, zero, seis. [p=0.3] Somando lugar com lugar: [p=0.2] {b}um mais três, quatro; [p=0.2] {c}dois com menos três, menos um; [p=0.2] {d}dois mais zero, dois; [p=0.2] {e}quatro mais seis, dez."),
    # questão 2
    dict(id="s07", block="questao2", text="{a}Questão dois. [p=0.2] {b}A é um, dois, três, menos um. [p=0.2] {c}B é dois, zero, um, quatro. [p=0.3] {d}Calcule A vezes B."),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Linha por coluna. [p=0.2] {a}Linha um com coluna um: [p=0.2] um vezes dois, mais dois vezes um: quatro. [p=0.3] {b}Linha um com coluna dois: [p=0.2] um vezes zero, mais dois vezes quatro: oito."),
    dict(id="s10", block="resposta2", text="{a}Linha dois com coluna um: [p=0.2] três vezes dois dá seis, [p=0.2] menos um vezes um dá menos um: [p=0.2] seis menos um, cinco. [p=0.3] {b}Linha dois com coluna dois: [p=0.2] três vezes zero dá zero, [p=0.2] menos um vezes quatro dá menos quatro. [p=0.3] {c}Quatro, oito, cinco, menos quatro."),
    # atalho
    dict(id="s11", block="atalho", text="Agora um atalho de prova: [p=0.2] {a}em questão com alternativas, você não precisa calcular o produto inteiro. [p=0.3] {b}Procure um elemento que muda de uma alternativa para outra [p=0.2] e {c}calcule só ele: uma linha com uma coluna."),
    dict(id="s12", block="atalho", text="Funciona porque {a}cada elemento do produto depende só de uma linha e de uma coluna. [p=0.3] {b}Se duas alternativas tiverem esse mesmo elemento, [p=0.2] calcule mais um para desempatar."),
    # questão 3
    dict(id="s13", block="questao3", text="{a}Questão três. [p=0.2] Calcule o determinante de {b}um, zero, dois; [p=0.2] menos um, três, um; [p=0.2] dois, um, zero."),
    dict(id="s14", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta3", text="É Sarrus. [p=0.2] {a}Copie as duas primeiras colunas. [p=0.2] Descendo: {b}um vezes três vezes zero, zero; [p=0.2] {c}zero vezes um vezes dois, zero; [p=0.2] {d}dois vezes menos um vezes um, menos dois. [p=0.2] Total descendo: {e}menos dois."),
    dict(id="s16", block="resposta3", text="Subindo: {a}dois vezes três vezes dois, doze; [p=0.2] {b}um vezes um vezes um, um; [p=0.2] {c}zero vezes menos um vezes zero, zero. [p=0.2] Total subindo: {d}treze. [p=0.3] {e}Menos dois, menos treze: [p=0.2] menos quinze."),
    # questão 4
    dict(id="s17", block="questao4", text="{a}Questão quatro. [p=0.2] {b}A matriz três, um, cinco, dois tem inversa? [p=0.2] {c}Se tiver, ache a inversa."),
    dict(id="s18", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta4", text="Primeiro, o determinante: [p=0.2] {a}três vezes dois, menos um vezes cinco: [p=0.2] seis menos cinco, um. [p=0.3] Não é zero: {b}a inversa existe. [p=0.2] E com determinante um, ela sai de cabeça: [p=0.2] {c}troque a principal, dois e três; [p=0.2] {d}mude o sinal da secundária, menos um e menos cinco."),
    dict(id="s20", block="resposta4", text="A inversa é {a}dois, menos um, menos cinco, três. [p=0.3] Conferindo a primeira conta: [p=0.2] {b}três vezes dois, mais um vezes menos cinco: [p=0.2] seis menos cinco, um. [p=0.2] {c}Bateu."),
    # questão 5
    dict(id="s21", block="questao5", text="{a}Última questão, rápida. [p=0.2] {b}A é dois por três, e B é três por dois. [p=0.3] {c}Existe A vezes B? [p=0.2] E {d}B vezes A? [p=0.2] Se existirem, de que tamanho?"),
    dict(id="s22", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s23", block="resposta5", text="Escreva os tamanhos lado a lado. [p=0.2] {a}A vezes B: dois por três, vezes três por dois. [p=0.2] {b}Os do meio, três e três, são iguais: existe. [p=0.2] {c}Os de fora dão dois por dois. [p=0.3] {d}B vezes A: três por dois, vezes dois por três. [p=0.2] {e}Dois e dois: existe, e é três por três. [p=0.3] Os dois produtos existem, [p=0.2] mas {f}nem têm o mesmo tamanho."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}linha antes da coluna, [p=0.2] {b}produto é linha por coluna, [p=0.2] {c}determinante é o que desce menos o que sobe, [p=0.2] e {d}determinante zero não tem inversa."),
    dict(id="s25", block="fim", text="Na próxima aula, você resolve {a}sistemas com três equações e três letras, [p=0.2] eliminando {b}uma letra de cada vez. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
