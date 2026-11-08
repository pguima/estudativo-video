# Estudativo · MAT-EST-011 — Moda e mediana (Matemática · Estatística · Mediana, moda e dispersão).
# Habilidade: ordenar os dados, achar a mediana de 3, 8, 5 e 9 (6,5) e a moda de uma lista.
# Pré-requisitos: MAT-EST-002 (tabela de frequência), MAT-EST-008 (média aritmética). Próxima: MAT-EST-012.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Listas só na tela (vírgula entre números funde a leitura da voz).
# Dados (tela):
#   Gancho: notas 7, 2, 9, 4, 5 → o do meio fora de ordem é 9 (errado); em ordem 2, 4, 5, 7, 9 → mediana 5.
#   Par: 3, 8, 5, 9 → em ordem 3, 5, 8, 9 → (5 + 8)/2 = 13/2 = 6,5.
#   Moda: 6, 7, 8, 7, 5, 7, 9, 8 → 7 aparece 3 vezes, 8 aparece 2 → moda 7.
#   Erro: (menor + maior)/2 = (3 + 9)/2 = 6 ≠ 6,5.
#   Atalho: posição (n + 1)/2: n = 11 → 6º (5 antes, 5 depois); n = 10 → 5,5 → média do 5º e do 6º.
#   Tabela (MAT-EST-002): ônibus 8, carro 5, bicicleta 4, a pé 3 → moda ônibus.
#   Questão: 7, 4, 9, 6, 9, 3, 8, 10 → em ordem 3, 4, 6, 7, 8, 9, 9, 10; (8 + 1)/2 = 4,5 → 4º e 5º: 7 e 8 → 7,5; moda 9.
# Visual:
#   s01-s02: cinco notas soltas, dedo no 9 (vermelho); as notas se ordenam e o 5 acende (verde).
#   s04-s06: E.reta com os pontos em ordem; metade de cada lado; os quatro números com 5 e 8 no meio → 6,5.
#   s04: fila de pessoas por altura com a do meio acesa.
#   s07-s08: lista da moda com o 7 destacado três vezes; "bimodal" e "sem moda".
#   s09: E.tabela de transporte (ônibus 8, carro 5, bicicleta 4, a pé 3) com a linha do ônibus acesa.
#   s10: 3 e 9 nas pontas com "6" em vermelho; 6,5 em verde.
#   s11-s12: régua de 11 posições com a 6ª acesa; régua de 10 com 5ª e 6ª acesas.

TITULO = "Moda e mediana"

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
    dict(id="s01", block="gancho", text="{a}Cinco notas na tela. [p=0.2] Qual é a nota do meio? [p=0.3] Se você apontou {b}o nove, que está no meio da lista, [p=0.2] caiu numa armadilha. [p=0.3] {c}Antes de achar o meio, a lista precisa estar em ordem."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha o valor do meio e o valor mais comum de qualquer lista [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}a média aritmética, que é a soma dividida pela quantidade, [p=0.2] e {c}a frequência absoluta, que conta quantas vezes cada valor aparece. [p=0.3] Se faltar alguma, procure no canal."),
    # mediana, quantidade ímpar
    dict(id="s04", block="mediana", text="A {a}mediana é o valor do meio, [p=0.2] com os dados {b}em ordem, do menor para o maior. [p=0.3] Ela deixa {c}metade dos dados de cada lado. [p=0.3] Pense numa fila de pessoas organizada por altura: [p=0.2] {d}a altura de quem está no meio da fila é a mediana."),
    dict(id="s05", block="mediana", text="Nas notas do começo, já em ordem, [p=0.2] {a}o valor do meio é o terceiro: [p=0.2] {b}cinco. [p=0.3] {c}Duas notas abaixo dele, duas acima. [p=0.2] O nove era só o que estava no meio da bagunça."),
    # mediana, quantidade par
    dict(id="s06", block="par", text="E com quantidade par? [p=0.2] Veja {a}os quatro números na tela. [p=0.2] Em ordem, {b}não sobra um no meio: sobram o cinco e o oito. [p=0.3] A mediana é {c}a média dos números do meio. [p=0.2] {d}Cinco mais oito dá treze. [p=0.2] {e}Treze dividido por dois dá seis vírgula cinco. [p=0.3] Repare: {f}a mediana nem precisa estar na lista."),
    # moda
    dict(id="s07", block="moda", text="A {a}moda é o valor que mais aparece. [p=0.2] Como a roupa da moda: {b}a que você mais vê na rua. [p=0.3] Na lista da tela, {c}o sete aparece três vezes, mais que qualquer outro. [p=0.2] {d}A moda é sete. [p=0.3] Para achar, {e}conte quantas vezes cada valor aparece, como na tabela de frequência."),
    dict(id="s08", block="moda", text="Uma lista pode ter {a}duas modas, se dois valores empatam no topo. [p=0.2] E pode {b}não ter moda, se todos aparecem o mesmo número de vezes. [p=0.3] A moda serve até para {c}dado que não é número: [p=0.2] o transporte mais usado, {d}a cor de camiseta mais vendida."),
    dict(id="s09", block="moda", text="Numa tabela de frequência, a moda é ainda mais rápida: [p=0.2] {a}é o valor da linha com a maior frequência absoluta. [p=0.2] Na pesquisa de transporte com vinte pessoas, {b}ônibus aparece oito vezes, mais que os outros. [p=0.2] {c}A moda é ônibus."),
    # erro
    dict(id="s10", block="erro", text="Agora, um erro comum: [p=0.2] achar a mediana {a}pelo menor e pelo maior valor. [p=0.2] Nos quatro números, {b}três mais nove dá doze, que dividido por dois dá seis. [p=0.3] Mas a mediana é {c}seis vírgula cinco. [p=0.2] A mediana não olha só as pontas: [p=0.2] {d}ela olha a posição de todos os dados."),
    # atalho
    dict(id="s11", block="atalho", text="Atalho para listas grandes: {a}a posição do meio. [p=0.2] {b}Some um à quantidade de dados e divida por dois. [p=0.3] Com onze dados, {c}onze mais um dá doze, e doze dividido por dois dá seis. [p=0.2] {d}A mediana é o sexto valor."),
    dict(id="s12", block="atalho", text="Funciona porque o sexto deixa {a}cinco antes e cinco depois. [p=0.3] Se der {b}número quebrado, como cinco e meio com dez dados, [p=0.2] {c}a mediana é a média do quinto e do sexto. [p=0.3] {d}Em lista curta, não compensa: olhe e ache o meio."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] {a}As notas de oito alunos estão na tela. [p=0.3] {b}Qual é a mediana? [p=0.2] {c}E qual é a moda?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] {a}Primeiro, coloque em ordem. [p=0.2] São oito dados: {b}oito mais um dá nove, e nove dividido por dois dá quatro e meio. [p=0.3] A mediana é a média do {c}quarto e do quinto valor: o sete e o oito. [p=0.2] {d}Sete mais oito dá quinze, e quinze dividido por dois dá sete vírgula cinco."),
    dict(id="s16", block="resposta", text="{a}A moda é nove: [p=0.2] é {b}a única nota que aparece duas vezes. [p=0.3] E confira a mediana: [p=0.2] {c}quatro notas ficam abaixo de sete vírgula cinco e quatro ficam acima. [p=0.2] Metade de cada lado, como deve ser."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: [p=0.2] {a}para a mediana, ordene e pegue o meio; [p=0.2] {b}para a moda, procure o que mais aparece."),
    dict(id="s18", block="fim", text="Na próxima aula, os dados vêm {a}numa tabela, com a nota e o número de alunos. [p=0.2] Você vai achar {b}média, mediana e moda sem escrever a lista inteira. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
