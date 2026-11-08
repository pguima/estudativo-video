# Estudativo · MAT-NUM-019 — Praticando: expressões e números inteiros (Matemática · Números e Contas · Números inteiros · prática).
# Habilidade: montar e resolver expressões com parênteses e números negativos, como um saldo que entra no vermelho.
# Pré-requisitos: MAT-NUM-013 a MAT-NUM-018. Próxima: nenhuma na trilha (fim de Números e Contas);
#   na playlist Matemática do Zero vem MAT-DIV-001 (múltiplos e divisores).
# Questões inéditas, criadas para esta aula; nenhuma é de prova real. Termos e métodos das aulas de origem: dívida e pagamento,
#   "tirar uma dívida é como ganhar", blocos cortados nos mais e menos que ligam uma conta na outra, sinal colado, "abre parênteses".
# Multiplicar por dois algarismos (MAT-NUM-008) não está na ficha: só contas de um algarismo vezes outro número (3 × 25, 2 × 10, 2 × 9).
# Q1: −4 °C → 7 °C · 7 − (−4) = 7 + 4 = 11 · na reta: 4 até o zero e 7 depois dele (sinais diferentes, some os tamanhos).
# Q2: 40 − 3 × 25 + 2 × 10 · blocos 40, 75, 20 · 40 − 75 = −35 · −35 + 20 = −15 · atalho entradas e saídas: 60 − 75 = −15.
# Q3: −2 × (5 − 9) − 12 ÷ 3 · 5 − 9 = −4 · −2 × (−4) = 8 · 12 ÷ 3 = 4 · 8 − 4 = 4.
#   Erro: 5 − 9 = 4 → −2 × 4 = −8 → −8 − 4 = −12.
# Q4: −3 + 2 × [4 − (1 − 6)] · 1 − 6 = −5 · 4 − (−5) = 9 · 2 × 9 = 18 · −3 + 18 = 15.
#   Erro: 4 − (−5) feito como 4 − 5 = −1 → 2 × (−1) = −2 → −3 − 2 = −5.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Praticando: expressões e números inteiros"

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
    dict(id="s01", block="gancho", text="{a}Quatro questões criadas para esta aula, [p=0.2] com sinais, parênteses e um saldo que {b}entra no vermelho. [p=0.3] Em cada uma, {c}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}a ordem das operações, [p=0.2] {b}montar a expressão de um problema, [p=0.2] {c}a reta numérica, [p=0.2] {d}dívida e pagamento para somar e subtrair, [p=0.2] e {e}a regra de sinais. [p=0.3] Se alguma travar, procure a aula no canal."),
    # questão 1: reta e subtração
    dict(id="s03", block="q1", text="{a}Questão um. [p=0.2] Numa cidade da serra, {b}a madrugada marcou menos quatro graus. [p=0.2] {c}À tarde, o termômetro chegou a sete graus. [p=0.3] {d}Quantos graus a temperatura subiu?"),
    dict(id="s04", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="r1", text="Quanto subiu é {a}o final menos o começo: [p=0.2] {b}sete menos, abre parênteses, menos quatro, fecha parênteses. [p=0.3] Tirar uma dívida é como ganhar: [p=0.2] {c}sete mais quatro dá onze graus."),
    dict(id="s06", block="r1", text="Na reta, dá para ver sem conta: [p=0.2] {a}do menos quatro até o zero são quatro passos, [p=0.2] {b}e do zero até o sete, mais sete. [p=0.3] {c}Onze passos. [p=0.3] Quem respondeu três {d}fez sete menos quatro, [p=0.2] como se a madrugada tivesse quatro graus acima de zero."),
    # questão 2: montar a expressão do saldo
    dict(id="s07", block="q2", text="{a}Questão dois. [p=0.2] Seu saldo é de {b}quarenta reais. [p=0.2] Você paga {c}três boletos de vinte e cinco reais cada [p=0.2] e recebe {d}duas transferências de dez reais cada. [p=0.3] {e}Monte uma expressão só e calcule o saldo final."),
    dict(id="s08", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="r2", text="A frase primeiro: {a}saldo, menos o que saiu, mais o que entrou. [p=0.3] A expressão: {b}quarenta menos três vezes vinte e cinco, mais duas vezes dez. [p=0.3] Aqui, o parêntese não faz falta, [p=0.2] porque {c}o vezes já vem antes."),
    dict(id="s10", block="r2", text="Em blocos: {a}três vezes vinte e cinco dá setenta e cinco. [p=0.2] {b}Duas vezes dez dá vinte. [p=0.3] {c}Quarenta menos setenta e cinco: [p=0.2] você tinha quarenta e pagou setenta e cinco, [p=0.2] então fica devendo trinta e cinco. [p=0.2] {d}Menos trinta e cinco mais vinte dá menos quinze. [p=0.3] {e}O saldo entrou no vermelho: menos quinze reais."),
    dict(id="s11", block="r2", text="Para conferir, o atalho: {a}separe entradas e saídas. [p=0.2] {b}Entrou quarenta mais vinte, sessenta. [p=0.2] {c}Saíram setenta e cinco. [p=0.2] {d}Sessenta menos setenta e cinco dá menos quinze. [p=0.2] Bateu."),
    # questão 3: sinais e parênteses
    dict(id="s12", block="q3", text="{a}Questão três. [p=0.2] Resolva: {b}menos dois vezes, abre parênteses, cinco menos nove, fecha parênteses, [p=0.2] {c}menos doze dividido por três."),
    dict(id="s13", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="r3", text="{a}Primeiro, o parêntese: [p=0.2] cinco menos nove. [p=0.2] Você tem cinco e gasta nove, então {b}deve quatro: menos quatro. [p=0.3] {c}Corte no menos do meio, que liga uma conta na outra. [p=0.2] O menos do começo é sinal colado: fica no primeiro bloco."),
    dict(id="s15", block="r3", text="Primeiro bloco: {a}menos dois vezes menos quatro. [p=0.2] Sinais iguais: {b}mais oito. [p=0.3] Segundo bloco: {c}doze dividido por três dá quatro. [p=0.3] Junte: {d}oito menos quatro dá quatro."),
    dict(id="s16", block="r3", text="O erro aqui é {a}fazer cinco menos nove igual a quatro, sem sinal. [p=0.2] Aí sai {b}menos dois vezes quatro, menos oito, [p=0.2] e a resposta vira {c}menos doze. [p=0.3] {d}Quando você tira mais do que tem, o resultado é negativo."),
    # questão 4: colchetes e menos antes de parêntese
    dict(id="s17", block="q4", text="{a}Última questão. [p=0.2] Resolva: {b}menos três, mais dois vezes um colchete. [p=0.2] Dentro do colchete, {c}quatro menos um parêntese. [p=0.2] Dentro do parêntese, {d}um menos seis."),
    dict(id="s18", block="q4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="r4", text="De dentro para fora. [p=0.2] {a}Um menos seis dá menos cinco. [p=0.3] O colchete fica com {b}quatro menos, abre parênteses, menos cinco, fecha parênteses. [p=0.2] Tirar uma dívida de cinco é ganhar cinco: [p=0.2] {c}quatro mais cinco dá nove."),
    dict(id="s20", block="r4", text="{a}Dois vezes nove dá dezoito. [p=0.2] {b}Menos três mais dezoito: [p=0.2] deve três e recebe dezoito, {c}sobram quinze. [p=0.3] Resposta: {d}quinze."),
    dict(id="s21", block="r4", text="A pegadinha está no colchete. [p=0.2] Quem {a}joga fora um dos sinais de menos [p=0.2] faz {b}quatro menos cinco, que dá menos um. [p=0.2] Daí sai {c}dois vezes menos um, menos dois, [p=0.2] e a resposta errada {d}menos cinco. [p=0.3] {e}Menos antes de parêntese com número negativo vira mais."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}de dentro para fora, [p=0.2] {b}vezes e dividido antes de mais e menos, [p=0.2] e {c}o sinal se decide a cada passo. [p=0.3] Com isso, você fecha a trilha de números e contas."),
    dict(id="s23", block="fim", text="O próximo assunto é {a}múltiplos e divisores: [p=0.2] você vai dizer se {b}cinquenta e quatro é múltiplo de seis [p=0.2] e {c}listar todos os divisores de trinta e seis. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
