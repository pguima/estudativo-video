# Estudativo · MAT-MTZ-004 — Matriz inversa (Matemática · Matrizes e Sistemas).
# Habilidade: dizer que uma matriz com determinante 0 não tem inversa e achar a inversa de [2 1; 1 1], que é [1 −1; −1 2].
# Pré-requisitos: MAT-MTZ-002 (linha por coluna), MAT-MTZ-003 (determinante). Próxima: MAT-MTZ-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Matrizes narradas pela ordem de leitura, linha por linha.
# "Inverso de um número" não está em "Já ensinado": explicado na hora (dois vezes um meio dá um).

TITULO = "Matriz inversa"

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
    dict(id="s01", block="gancho", text="{a}Qual é a inversa da matriz dois, um, um, um? [p=0.3] Se você inverteu cada número e achou {b}um meio, um, um, um, [p=0.2] errou. [p=0.3] A inversa é {c}um, menos um, menos um, dois."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha a inversa de uma matriz dois por dois, [p=0.2] sabe quando ela não existe, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre {a}duas coisas: [p=0.2] {b}multiplicar matrizes é linha por coluna, [p=0.2] e {c}o determinante da dois por dois é a principal menos a secundária. [p=0.3] Se faltar alguma, procure no canal."),
    # identidade
    dict(id="s04", block="identidade", text="Com números, {a}dois vezes um meio dá um. [p=0.2] Por isso, um meio é o {b}inverso de dois: [p=0.2] multiplicado por ele, dá um. [p=0.3] E o um é especial: {c}multiplicar por um não muda nada."),
    dict(id="s05", block="identidade", text="Nas matrizes, o papel do um é da {a}matriz identidade: [p=0.2] {b}um na diagonal principal e zero no resto. [p=0.3] Ela leva a letra {c}I. [p=0.2] Multiplicar uma matriz pela identidade {d}não muda a matriz."),
    dict(id="s06", block="identidade", text="Então, a {a}inversa de A é a matriz que, multiplicada por A, {b}dá a identidade. [p=0.3] Ela se escreve {c}A elevado a menos um."),
    # regra
    dict(id="s07", block="regra", text="Na dois por dois, a inversa sai em {a}três passos. [p=0.2] {b}Um: troque de lugar os números da diagonal principal. [p=0.2] {c}Dois: troque o sinal dos números da secundária. [p=0.2] {d}Três: divida tudo pelo determinante."),
    dict(id="s08", block="regra", text="Com dois, um, um, um: [p=0.2] {a}o determinante é dois vezes um, menos um vezes um: um. [p=0.3] {b}Trocando a principal, dois e um viram um e dois. [p=0.2] {c}Trocando o sinal da secundária, os uns viram menos um. [p=0.2] {d}Dividir por um não muda nada: [p=0.2] a inversa é {e}um, menos um, menos um, dois."),
    # conferir
    dict(id="s09", block="confere", text="Confira multiplicando, linha por coluna. [p=0.2] {a}Dois vezes um, mais um vezes menos um: um. [p=0.2] {b}Dois vezes menos um, mais um vezes dois: zero. [p=0.2] {c}Um vezes um, mais um vezes menos um: zero. [p=0.2] {d}Um vezes menos um, mais um vezes dois: um. [p=0.3] {e}Deu a identidade."),
    # determinante zero
    dict(id="s10", block="zero", text="E quando a inversa não existe? [p=0.2] Com números, {a}o zero não tem inverso: [p=0.2] nenhum número vezes zero dá um. [p=0.3] Nas matrizes, o aviso vem do {b}determinante. [p=0.2] {c}Determinante zero, sem inversa: [p=0.2] o passo três pediria uma divisão por zero, que não existe."),
    dict(id="s11", block="zero", text="Veja {a}dois, quatro, um, dois. [p=0.2] {b}Dois vezes dois, menos quatro vezes um: [p=0.2] quatro menos quatro, zero. [p=0.3] {c}Essa matriz não tem inversa."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}inverter cada número. [p=0.3] {b}Um meio, um, um, um não é a inversa de dois, um, um, um. [p=0.3] Multiplique: a primeira conta já dá {c}dois vezes um meio, mais um vezes um: dois. [p=0.3] {d}Não deu a identidade."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho de prova: [p=0.2] {a}calcule o determinante antes de tudo. [p=0.3] {b}Deu zero? Pare: não existe inversa. [p=0.3] {c}Deu um? A inversa sai de cabeça: [p=0.2] troca a principal e muda o sinal da secundária."),
    dict(id="s14", block="atalho", text="Funciona porque {a}dividir por um não muda nada. [p=0.3] {b}Com outro determinante, como dois, [p=0.2] ainda falta dividir cada número por ele: [p=0.2] {c}aí não dá para pular o passo três."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Ache a inversa da matriz dois, três, um, um, [p=0.2] {b}se ela existir."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Determinante: dois vezes um, menos três vezes um: menos um. [p=0.2] Não é zero, então {b}a inversa existe. [p=0.3] {c}Troque a principal: um e dois. [p=0.2] {d}Mude o sinal da secundária: menos três e menos um."),
    dict(id="s18", block="resposta", text="Falta dividir por {a}menos um, [p=0.2] e dividir por menos um {b}troca o sinal de tudo. [p=0.3] A inversa é {c}menos um, três, um, menos dois. [p=0.3] Confira a primeira conta: {d}dois vezes menos um, mais três vezes um: um."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}determinante zero, sem inversa. [p=0.2] Senão, {b}troca a principal, muda o sinal da secundária [p=0.2] e {c}divide pelo determinante."),
    dict(id="s20", block="fim", text="A próxima aula é de {a}prática: [p=0.2] você usa tudo de matrizes e determinantes em {b}questões no estilo de prova. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
