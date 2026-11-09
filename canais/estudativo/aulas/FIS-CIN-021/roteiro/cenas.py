# Estudativo · FIS-CIN-021 — Praticando: movimento circular (Física · Cinemática · prática). Última aula da trilha.
# Habilidade: resolver questões de rotação, polias e bicicleta com frequência, período e velocidades.
# Pré-requisitos: FIS-CIN-018, FIS-CIN-019, FIS-CIN-020. Próxima: nenhuma na trilha (fim de Cinemática).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questões inéditas, criadas para esta aula. π = 3.
# Contas: Q1 600/60 = 10 Hz; T = 0,1 s. Q2 T = 120 s; ω = 6/120 = 0,05 rad/s; v = 0,05·20 = 1 m/s (= 2·3·20/120).
# Q3 3000·2 = f·6 → f = 1000 rpm. Q4 coroa 45, catraca 15 → 3 Hz; v = 2·3·3·0,3 = 5,4 m/s; 5,4·3,6 = 19,44 km/h.

TITULO = "Praticando: movimento circular"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações, [p=0.2] criadas para esta aula, [p=0.2] com rotação, polias, bicicleta e até a Terra. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar: [p=0.2] {a}tê igual a um dividido por efe, e rpm dividido por sessenta dá hertz; [p=0.2] {b}ômega igual a dois pi dividido por tê, e vê igual a ômega vezes erre; [p=0.2] {c}e, nas ligações, correia com velocidade linear igual e eixo com angular igual. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Na centrifugação, o cesto de uma máquina de lavar gira a {b}seiscentas rotações por minuto. [p=0.3] {c}Qual é a frequência em hertz? [p=0.2] {d}E o período?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}Seiscentos dividido por sessenta: [p=0.1] {b}dez hertz, dez voltas por segundo. [p=0.3] {c}Período: um dividido por dez, [p=0.1] {d}zero vírgula um segundo. [p=0.2] Pelo atalho, sessenta dividido por seiscentos, o mesmo."),
    # situação 2
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] Uma roda-gigante tem {b}vinte metros de raio [p=0.2] e dá uma volta a cada {c}dois minutos. [p=0.3] {d}Qual é a velocidade de uma cabine, em metros por segundo? [p=0.2] Use pi igual a três."),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] Primeiro, o tempo no esse i: {a}dois minutos são cento e vinte segundos. [p=0.3] {b}Ômega: dois vezes três dividido por cento e vinte, [p=0.1] {c}zero vírgula zero cinco radiano por segundo. [p=0.3] {d}Vê: zero vírgula zero cinco vezes vinte, [p=0.1] {e}um metro por segundo. [p=0.2] Devagar, como um passeio."),
    dict(id="s09", block="resposta2", text="Pelo caminho direto, {a}a cabine percorre dois pi erre, cento e vinte metros, em cento e vinte segundos: [p=0.2] {b}um metro por segundo. [p=0.2] Os dois caminhos sempre batem."),
    # situação 3
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] O motor de um liquidificador tem uma polia de {b}dois centímetros de raio, a {c}três mil rotações por minuto. [p=0.2] Uma correia liga essa polia a outra, de {d}seis centímetros. [p=0.3] {e}Quantas rotações por minuto faz a polia maior?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] {a}Correia: efe vezes erre igual dos dois lados. [p=0.3] {b}Três mil vezes dois é igual a efe vezes seis. [p=0.2] {c}Seis mil dividido por seis: mil rotações por minuto. [p=0.3] {d}Raio três vezes maior, gira três vezes mais devagar. [p=0.2] E nem foi preciso converter as unidades."),
    # atalho
    dict(id="s13", block="atalho", text="Aqui cabe o atalho: [p=0.2] antes de qualquer conta, {a}pergunte como as rodas estão ligadas. [p=0.3] {b}Ligadas pela borda, por correia, corrente ou dente? [p=0.2] Velocidade linear igual. [p=0.2] {c}Presas no mesmo eixo? [p=0.2] Velocidade angular igual. [p=0.3] Essa pergunta resolve metade da questão."),
    # situação 4
    dict(id="s14", block="questao4", text="{a}Situação quatro. [p=0.2] Uma bicicleta tem coroa de {b}quarenta e cinco dentes e catraca de {c}quinze. [p=0.2] A roda tem {d}zero vírgula três metro de raio, [p=0.1] e o ciclista dá {e}uma pedalada por segundo. [p=0.3] {f}Qual é a velocidade da bicicleta em metros por segundo? [p=0.2] Pi igual a três."),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="Vamos lá. [p=0.2] {a}Corrente: quarenta e cinco dividido por quinze, três voltas da catraca por pedalada. [p=0.2] {b}Eixo: a roda também dá três voltas, [p=0.1] três hertz. [p=0.3] {c}Vê igual a dois pi vezes efe vezes erre: [p=0.1] {d}dois vezes três vezes três vezes zero vírgula três, [p=0.1] {e}cinco vírgula quatro metros por segundo."),
    dict(id="s17", block="resposta4", text="{a}Vezes três vírgula seis, quase vinte quilômetros por hora. [p=0.3] Para ir mais rápido sem pedalar mais depressa, [p=0.2] {b}troque para uma catraca menor, [p=0.1] ou uma coroa maior."),
    # situação 5
    dict(id="s18", block="questao5", text="{a}Última situação, e ela não tem conta. [p=0.2] {b}A Terra dá uma volta em torno do próprio eixo por dia. [p=0.3] Uma pessoa está {c}na linha do equador, [p=0.1] e outra {d}perto do polo. [p=0.3] {e}Quem tem a maior velocidade angular? [p=0.2] {f}E a maior velocidade linear?"),
    dict(id="s19", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta5", text="Vamos lá. [p=0.2] As duas giram com a Terra, {a}como pontos do mesmo corpo: [p=0.2] uma volta por dia para as duas, [p=0.1] {b}a mesma velocidade angular. [p=0.3] Mas a do equador está {c}muito mais longe do eixo, [p=0.2] então {d}a velocidade linear dela é maior. [p=0.3] É a criança da borda do carrossel, em tamanho de planeta."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}rpm dividido por sessenta dá hertz, [p=0.2] {b}vê é ômega vezes erre, [p=0.2] e {c}a ligação diz o que é igual: [p=0.1] borda na correia, giro no eixo."),
    dict(id="s22", block="fim", text="{a}Com esta aula, você fecha a Cinemática: [p=0.2] {b}o movimento, do uniforme ao circular. [p=0.3] {c}O próximo passo é entender o que muda o movimento, as forças, em outra trilha do curso. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
