# Estudativo · MAT-ESP-010 — Praticando: sólidos, prismas e cilindros (Matemática · Geometria Espacial · Prismas e cilindros · prática).
# Habilidade: ler uma planificação ou uma vista e calcular volume, capacidade e área em caixas, latas e reservatórios.
# Pré-requisitos: MAT-ESP-001 a MAT-ESP-009. Próxima: MAT-ESP-011.
# Questões inéditas, criadas para esta aula. Marcas: {cue} animação · [p=0.2] pausa. Números por extenso.

TITULO = "Praticando: sólidos, prismas e cilindros"

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
    dict(id="s01", block="gancho", text="{a}Quatro situações com latas, caixas e reservatórios, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}descobrir o sólido pelo molde ou pela vista, [p=0.2] {b}volume é a área da base vezes a altura, [p=0.2] {c}área total é a soma das faces [p=0.2] e {d}um metro cúbico guarda mil litros. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: molde do cilindro
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Um molde tem {b}dois círculos iguais [p=0.2] e {c}um retângulo de vinte e quatro centímetros por quinze. [p=0.2] Os círculos encostam no lado de vinte e quatro. [p=0.3] {d}Que sólido ele monta, e quantos mililitros cabem nele? [p=0.2] Use pi igual a três."),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Dois círculos e um retângulo montam {a}um cilindro. [p=0.2] O lado de vinte e quatro dá a volta no círculo: [p=0.2] {b}é dois pi érre, com érre igual ao raio da tampa. [p=0.3] {c}Duas vezes três vezes érre dá seis érre, igual a vinte e quatro. [p=0.2] Então {d}o raio é quatro. [p=0.2] A altura é {e}o outro lado, quinze."),
    dict(id="s06", block="resposta1", text="Fundo: {a}três vezes quatro ao quadrado dá quarenta e oito. [p=0.2] {b}Vezes quinze dá setecentos e vinte centímetros cúbicos: [p=0.2] {c}setecentos e vinte mililitros. [p=0.3] A armadilha era {d}usar vinte e quatro como raio. [p=0.2] Ele é a volta inteira, não o raio."),
    # situação 2: molde do prisma
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Outro molde tem {b}dois triângulos retângulos, com catetos de três e quatro centímetros e hipotenusa de cinco, [p=0.2] e {c}três retângulos de dez centímetros de altura. [p=0.3] {d}Qual o volume da peça montada? [p=0.2] {e}E quanto papel o molde gasta?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] Duas figuras iguais e retângulos: {a}é um prisma triangular. [p=0.2] Num triângulo retângulo, os catetos fazem o papel de base e altura: [p=0.2] {b}três vezes quatro dividido por dois dá seis. [p=0.3] Volume: {c}seis vezes dez dá sessenta centímetros cúbicos."),
    dict(id="s10", block="resposta2", text="No papel, {a}as duas bases dão doze. [p=0.2] Para os retângulos, o atalho dos prismas: [p=0.2] {b}perímetro da base vezes a altura. [p=0.2] {c}Três mais quatro mais cinco dá doze, [p=0.2] e {d}doze vezes dez dá cento e vinte. [p=0.3] Papel: {e}cento e vinte mais doze dá cento e trinta e dois centímetros quadrados."),
    dict(id="s11", block="resposta2", text="O atalho funciona porque {a}os três retângulos têm a mesma altura, [p=0.2] e lado a lado formam um retângulo só. [p=0.3] Mas ele {b}deixa as bases de fora: [p=0.2] quem para no cento e vinte {c}esquece os dois triângulos."),
    # situação 3: vista da caixa-d'água
    dict(id="s12", block="questao3", text="{a}Situação três. [p=0.2] Uma caixa-d'água, vista {b}de cima, é um círculo de dois metros de diâmetro. [p=0.2] Vista {c}de frente, é um retângulo de um vírgula dois metro de altura. [p=0.3] {d}Quantos litros ela guarda? [p=0.2] Use pi igual a três."),
    dict(id="s13", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="resposta3", text="Vamos lá. [p=0.2] Círculo de cima e retângulo de frente: {a}é um cilindro em pé. [p=0.2] Diâmetro dois, {b}raio um. [p=0.3] Fundo: {c}três vezes um ao quadrado dá três metros quadrados. [p=0.2] {d}Vezes um vírgula dois dá três vírgula seis metros cúbicos. [p=0.2] {e}Vezes mil dá três mil e seiscentos litros."),
    dict(id="s15", block="resposta3", text="Quem usa o diâmetro como raio acha {a}quatro vezes o certo: [p=0.2] {b}catorze mil e quatrocentos litros. [p=0.3] Raio é {c}a metade do diâmetro, sempre."),
    # situação 4: reservatório, nível e tempo
    dict(id="s16", block="questao4", text="{a}Última situação. [p=0.2] Um reservatório em forma de bloco tem {b}fundo de quatro metros por dois. [p=0.2] Uma bomba joga {c}quarenta litros por minuto nele. [p=0.3] {d}Quanto tempo leva para o nível subir cinquenta centímetros?"),
    dict(id="s17", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta4", text="Vamos lá. [p=0.2] A água forma {a}uma camada em forma de bloco. [p=0.2] {b}Cinquenta centímetros são zero vírgula cinco metro. [p=0.2] {c}Quatro vezes dois vezes zero vírgula cinco dá quatro metros cúbicos, [p=0.2] {d}quatro mil litros."),
    dict(id="s19", block="resposta4", text="Tempo é volume dividido pela vazão: [p=0.2] {a}quatro mil dividido por quarenta dá cem minutos. [p=0.2] {b}Sessenta minutos são uma hora, e sobram quarenta: [p=0.2] {c}uma hora e quarenta minutos. [p=0.3] Não é {d}um vírgula quatro hora: [p=0.2] o tempo anda de sessenta em sessenta."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}descubra o sólido pelo molde ou pela vista, [p=0.2] {b}ache o raio e a altura certos [p=0.2] e {c}confira a unidade antes de responder."),
    dict(id="s21", block="fim", text="Na próxima aula, o sólido termina em ponta: {a}a pirâmide. [p=0.2] Você vai ver por que o volume dela é {b}um terço do volume do prisma de mesma base e mesma altura. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
