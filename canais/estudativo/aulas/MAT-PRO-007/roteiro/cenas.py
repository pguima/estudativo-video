# Estudativo · MAT-PRO-007 — Praticando: sequências e PA (Matemática · Progressões · Sequências e PA · prática).
# Habilidade: achar padrões, termos e somas em sequências de figuras, calendários e pagamentos.
# Pré-requisitos: MAT-PRO-001 a MAT-PRO-006. Próxima: MAT-PRO-008.
# Questões inéditas, criadas para esta aula. Termos como nas aulas da trilha: posição e termo, lei de formação, "o aumento
#   vira o número do ene" (MAT-PRO-002), "resto zero é o fim de uma volta" (MAT-PRO-003), razão "erre" e saltos (MAT-PRO-004),
#   "último menos primeiro, dividido pela razão, mais um" (MAT-PRO-005), "primeiro mais último, vezes a quantidade,
#   dividido por dois" e média (MAT-PRO-006). PA = "pê á".
# 1 · Triângulos de palitos, alternados, vizinhos dividem um palito: 3, 5, 7 · lei 2n + 1 · figura 30: 61
#     · dez primeiras juntas: a₁₀ = 21 · (3 + 21) · 10 / 2 = 24 · 5 = 120.
# 2 · Curso começa numa segunda, que é o dia 1 · dia 200: 200 ÷ 7 = 28 r 4 → seg, ter, qua, qui → quinta
#     (posição: resto 1 = segunda, resto 0 = domingo; armadilha "daqui a 200 dias" daria sexta).
# 3 · 12 parcelas, 1ª de R$ 100, +R$ 20 · a₁₂ = 100 + 11 · 20 = 320 · S = (100 + 320) · 12 / 2 = 420 · 6 = 2.520
#     · atalho média 210 · 12 = 2.520.
# 4 · Postos de água no km 3, a cada 4 km, último no km 39 · (39 − 3) / 4 + 1 = 9 + 1 = 10 · 6º posto: 3 + 5 · 4 = 23.
# Visual: fileira de triângulos de palitos (1, 2, 3 triângulos) com contagem; roda dos sete dias com o dia 1 na segunda;
#   colunas (E.colunas) das 12 parcelas com a linha da média 210; estrada com postos de 4 em 4 km (postes e espaços).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Praticando: sequências e PA"

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
    dict(id="s01", block="gancho", text="{a}Quatro situações do dia a dia, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}a lei de uma fileira de figuras, [p=0.2] {b}o resto da divisão nos padrões que se repetem, [p=0.2] {c}o termo geral da pê á [p=0.2] e {d}a soma da pê á. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: figuras
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Uma fileira de triângulos de palitos, um com a ponta para cima, o outro para baixo, encaixados. [p=0.2] Triângulos vizinhos {b}dividem um palito. [p=0.2] As figuras têm {c}três, [p=0.1] cinco [p=0.1] e sete palitos. [p=0.3] {d}Quantos palitos tem a figura trinta? [p=0.2] E {e}quantos palitos são necessários para montar as dez primeiras figuras, todas juntas?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] De uma figura para a próxima, {a}entram dois palitos. [p=0.2] O aumento vira o número do ene: {b}dois ene. [p=0.2] Na figura um, dois ene dá dois, mas são três. [p=0.2] Falta um: {c}pê igual a dois ene mais um. [p=0.3] Figura trinta: {d}dois vezes trinta dá sessenta, e mais um dá sessenta e um palitos."),
    dict(id="s06", block="resposta1", text="As dez primeiras juntas pedem {a}uma soma. [p=0.2] As quantidades formam uma pê á de razão dois. [p=0.2] A figura dez tem {b}dois vezes dez mais um, que dá vinte e um. [p=0.3] {c}Três mais vinte e um dá vinte e quatro. [p=0.2] {d}Vezes dez dá duzentos e quarenta, e dividido por dois dá cento e vinte palitos."),
    # situação 2: calendário
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Um curso tem aula todo dia. [p=0.2] O {b}dia um do curso foi uma segunda-feira. [p=0.3] {c}Em que dia da semana cai o dia duzentos?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] O bloco é a semana: {a}sete dias, começando na segunda. [p=0.2] Aqui o número é {b}a posição do dia no curso, como a posição das letras. [p=0.3] {c}Duzentos dividido por sete dá vinte e oito, com resto quatro. [p=0.2] Resto quatro é a quarta casa do bloco: [p=0.2] {d}segunda, terça, quarta, quinta. [p=0.2] {e}O dia duzentos é uma quinta-feira."),
    dict(id="s10", block="resposta2", text="Cuidado com a leitura. [p=0.2] {a}Daqui a duzentos dias, contando a partir da segunda, daria sexta. [p=0.3] A diferença é que {b}o dia um já é a segunda. [p=0.2] Quem pergunta a posição conta a segunda como casa um. [p=0.2] E aqui, {c}resto zero seria o fim da volta: o domingo."),
    # situação 3: pagamentos
    dict(id="s11", block="questao3", text="{a}Situação três. [p=0.2] Uma pessoa combina pagar uma dívida em {b}doze parcelas mensais. [p=0.2] A primeira é de {c}cem reais, [p=0.2] e cada parcela é {d}vinte reais maior que a anterior. [p=0.3] {e}Qual é o valor da última parcela? [p=0.2] E {f}quanto ela paga no total?"),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] Da primeira à décima segunda parcela, {a}onze saltos de vinte. [p=0.2] {b}Onze vezes vinte dá duzentos e vinte. [p=0.2] {c}Mais cem dá trezentos e vinte reais na última."),
    dict(id="s14", block="resposta3", text="No total: {a}cem mais trezentos e vinte dá quatrocentos e vinte. [p=0.2] {b}Doze dividido por dois dá seis. [p=0.2] {c}Quatrocentos e vinte vezes seis dá dois mil quinhentos e vinte reais."),
    # atalho
    dict(id="s15", block="atalho", text="Aqui cabe o atalho da média: {a}quatrocentos e vinte dividido por dois dá duzentos e dez. [p=0.2] É como se ela pagasse {b}doze parcelas iguais de duzentos e dez. [p=0.2] {c}Duzentos e dez vezes doze dá dois mil quinhentos e vinte. [p=0.3] Funciona porque {d}o que as primeiras parcelas têm a menos, as últimas têm a mais. [p=0.2] E só vale quando {e}as parcelas sobem sempre do mesmo tanto."),
    # situação 4: contar termos
    dict(id="s16", block="questao4", text="{a}Última situação. [p=0.2] Numa corrida, há postos de água {b}a cada quatro quilômetros. [p=0.2] O primeiro fica no {c}quilômetro três, [p=0.2] e o último, no {d}quilômetro trinta e nove. [p=0.3] {e}Quantos postos há? [p=0.2] E {f}em que quilômetro fica o sexto posto?"),
    dict(id="s17", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta4", text="Vamos lá. [p=0.2] Último menos primeiro: {a}trinta e nove menos três dá trinta e seis. [p=0.2] {b}Dividido por quatro dá nove saltos. [p=0.2] {c}Mais um dá dez postos. [p=0.3] Quem para no nove esquece {d}o posto do quilômetro três, que não precisou de salto."),
    dict(id="s19", block="resposta4", text="O sexto posto está a {a}cinco saltos do primeiro. [p=0.2] {b}Cinco vezes quatro dá vinte. [p=0.2] {c}Três mais vinte dá quilômetro vinte e três."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}veja o que se repete e o que se soma. [p=0.2] {b}Separe a posição do valor. [p=0.2] E {c}lembre que os termos são os saltos mais um."),
    dict(id="s21", block="fim", text="Na próxima aula, a sequência {a}multiplica em vez de somar, como três, [p=0.1] seis, [p=0.1] doze: [p=0.2] {b}a progressão geométrica. [p=0.3] Você vai achar a razão, {c}calcular o oitavo termo com uma fórmula [p=0.2] e reconhecer nela {d}o montante dos juros compostos, mês a mês. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
