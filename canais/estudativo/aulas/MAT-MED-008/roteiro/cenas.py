# Estudativo · MAT-MED-008 — Praticando: medidas e unidades (Matemática · Medidas e Unidades · prática).
# Habilidade: converter comprimento, massa, área, volume e tempo em problemas com a unidade trocada no meio.
# Pré-requisitos: MAT-MED-001, MAT-MED-002, MAT-MED-003, MAT-MED-004, MAT-MED-005, MAT-MED-006, MAT-MED-007.
# Próxima: fim da trilha; segue para MAT-RAZ-001 (Razão e Proporção).
# Questões inéditas, criadas para esta aula. Soma de decimais (MAT-FRA-015) não está na cadeia: as contas usam inteiros.

TITULO = "Praticando: medidas e unidades"

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
    dict(id="s01", block="gancho", text="{a}Cinco problemas, criados para esta aula. [p=0.2] Em todos, {b}a unidade muda no meio do caminho. [p=0.3] Em cada um, {c}pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}a escada do metro. [p=0.2] Em comprimento, massa e capacidade, {b}cada degrau vale dez: uma casa da vírgula. [p=0.2] Em área, {c}cada degrau vale cem. [p=0.2] Em volume, {d}mil. [p=0.3] E no tempo, {e}a troca é de sessenta. [p=0.3] Se alguma travar, procure a aula no canal."),
    # problema 1: comprimento
    dict(id="s03", block="questao1", text="{a}Problema um. [p=0.2] Uma pessoa quer caminhar {b}dois vírgula quatro quilômetros por dia [p=0.2] numa pista de {c}quatrocentos metros. [p=0.3] {d}Quantas voltas ela precisa dar?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Primeiro, {a}a mesma unidade. [p=0.2] De quilômetro para metro são {b}três degraus: vezes mil. [p=0.2] A vírgula anda três casas: {c}dois mil e quatrocentos metros. [p=0.3] {d}Dois mil e quatrocentos dividido por quatrocentos: seis voltas. [p=0.3] Quem esquece de converter divide dois vírgula quatro por quatrocentos [p=0.2] e acha {e}menos de uma volta. [p=0.2] Resposta estranha é sinal de unidade trocada."),
    # problema 2: massa
    dict(id="s06", block="questao2", text="{a}Problema dois. [p=0.2] Um elevador de carga aguenta {b}uma tonelada e meia. [p=0.2] Cada caixa pesa {c}trinta quilos. [p=0.3] {d}Quantas caixas ele leva de uma vez, no máximo?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] {a}Uma tonelada são mil quilos: [p=0.2] um pulo de mil, três casas da vírgula. [p=0.2] Uma tonelada e meia, {b}mil e quinhentos quilos. [p=0.3] {c}Mil e quinhentos dividido por trinta: cinquenta caixas. [p=0.3] Confira o tamanho: {d}cinquenta caixas de trinta quilos, [p=0.2] uma tonelada e meia. [p=0.2] Faz sentido."),
    # problema 3: área
    dict(id="s09", block="questao3", text="{a}Problema três. [p=0.2] Uma parede tem {b}dois metros de largura por um metro de altura. [p=0.2] Ela vai ser coberta com azulejos quadrados de {c}vinte centímetros de lado. [p=0.3] {d}Quantos azulejos são necessários?"),
    dict(id="s10", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s11", block="resposta3", text="Vamos lá. [p=0.2] A área da parede é {a}dois vezes um dá dois metros quadrados. [p=0.2] De metro quadrado para centímetro quadrado são dois degraus, {b}cada um vezes cem: [p=0.2] {c}vinte mil centímetros quadrados. [p=0.3] Cada azulejo tem {d}vinte vezes vinte dá quatrocentos centímetros quadrados. [p=0.2] {e}Vinte mil dividido por quatrocentos: cinquenta azulejos."),
    dict(id="s12", block="resposta3", text="O erro clássico aqui é usar {a}a escada do comprimento: [p=0.2] dois metros quadrados viram {b}duzentos centímetros quadrados. [p=0.3] Aí a parede inteira teria {c}menos que um azulejo. [p=0.2] Resposta absurda, sinal de conversão errada."),
    # atalho
    dict(id="s13", block="atalho", text="E aqui cabe um atalho de prova: {a}converta os lados, não a área. [p=0.3] {b}Duzentos centímetros dividido por vinte dá dez azulejos na largura. [p=0.2] {c}Cem dividido por vinte dá cinco na altura. [p=0.2] {d}Dez vezes cinco: cinquenta."),
    dict(id="s14", block="atalho", text="Funciona porque {a}lado é comprimento, e comprimento só anda de dez em dez. [p=0.3] Você foge do vezes cem. [p=0.2] Não compensa quando o problema {b}já dá a área pronta, [p=0.2] como um terreno em hectares. [p=0.2] Aí, {c}use a escada da área."),
    # problema 4: volume
    dict(id="s15", block="questao4", text="{a}Problema quatro. [p=0.2] Um aquário tem {b}cinquenta centímetros de comprimento, [p=0.2] {c}trinta de largura [p=0.2] e {d}quarenta de altura. [p=0.3] {e}Quantos litros cabem nele?"),
    dict(id="s16", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta4", text="Vamos usar o atalho: {a}converta os lados para decímetro, porque um decímetro cúbico é um litro. [p=0.3] Cinquenta centímetros são {b}cinco decímetros. [p=0.2] Trinta centímetros são {c}três. [p=0.2] Quarenta centímetros são {d}quatro. [p=0.3] Volume: {e}cinco vezes três vezes quatro, sessenta decímetros cúbicos. [p=0.2] {f}Sessenta litros."),
    dict(id="s18", block="resposta4", text="Pelo caminho longo: {a}cinquenta vezes trinta vezes quarenta, sessenta mil centímetros cúbicos. [p=0.2] Um degrau em volume é vezes mil, então {b}divida por mil: sessenta decímetros cúbicos. [p=0.2] {c}Mesmos sessenta litros."),
    # problema 5: tempo
    dict(id="s19", block="questao5", text="{a}Último problema. [p=0.2] Uma tarefa começa às {b}oito horas e cinquenta minutos [p=0.2] e leva {c}dois vírgula três horas. [p=0.3] {d}A que horas ela termina?"),
    dict(id="s20", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta5", text="Vamos lá. [p=0.2] Cuidado: {a}zero vírgula três hora não é trinta minutos. [p=0.3] São {b}três décimos de sessenta minutos. [p=0.2] Divide pelo de baixo: sessenta dividido por dez dá seis. [p=0.2] Multiplica pelo de cima: seis vezes três dá dezoito minutos. [p=0.2] A tarefa dura {c}duas horas e dezoito minutos."),
    dict(id="s22", block="resposta5", text="Somando: {a}oito mais dois dá dez horas. [p=0.2] {b}Cinquenta mais dezoito dá sessenta e oito minutos. [p=0.3] Sessenta e oito são {c}sessenta mais oito: [p=0.2] mais uma hora. [p=0.3] Termina às {d}onze horas e oito minutos."),
    dict(id="s23", block="resposta5", text="Quem lê dois vírgula três como {a}duas horas e trinta [p=0.2] chega em {b}onze e vinte. [p=0.3] {c}Doze minutos de erro, por causa de uma vírgula."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}antes de qualquer conta, deixe tudo na mesma unidade, [p=0.2] e {b}confira se a resposta faz sentido."),
    dict(id="s25", block="fim", text="Aqui termina a trilha de medidas. [p=0.2] Na próxima aula começa {a}razão: [p=0.2] você escreve {b}três meninos para cinco meninas como uma fração [p=0.2] e compara {c}cinquenta centímetros com dois metros. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
