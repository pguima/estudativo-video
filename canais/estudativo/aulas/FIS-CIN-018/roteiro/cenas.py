# Estudativo · FIS-CIN-018 — Período, frequência e rpm (Física · Cinemática · Movimento circular).
# Habilidade: usar T = 1/f, entendendo o que cada letra mede, e converter rotações por minuto em hertz.
# Pré-requisitos: FIS-CIN-001 (grandezas e SI), com frações, decimais, MAT-MED-006 (tempo) e MAT-RAZ-025 (fatores) já ensinados.
# Próxima: FIS-CIN-019. Movimento uniforme (FIS-CIN-005) NÃO está em "Já ensinado": a aula não usa velocidade.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Contas: 1200/60 = 20 Hz; 1/20 = 0,05 s; carrossel T = 4 s → f = 1/4 = 0,25 Hz; 10 voltas em 5 s = 2 Hz → T = 0,5 s;
# erro: 1200·60 = 72000; atalho 60/1200 = 0,05 s; 2 Hz · 60 = 120 rpm. Questão: 3000/60 = 50 Hz; T = 1/50 = 0,02 s = 60/3000.

TITULO = "Período, frequência e rpm"

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
    dict(id="s01", block="gancho", text="{a}Um ventilador gira a mil e duzentas rotações por minuto. [p=0.3] {b}Quantas voltas ele dá em um segundo? [p=0.3] {c}Vinte. [p=0.2] E cada volta dura {d}cinco centésimos de segundo. [p=0.3] Rápido demais para o olho acompanhar."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai entender {b}o período, [p=0.2] {c}a frequência [p=0.2] e {d}passar de rotações por minuto para hertz."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}um minuto tem sessenta segundos; [p=0.2] e {c}a unidade de tempo do Sistema Internacional, o esse i, é o segundo. [p=0.3] Se faltar alguma, procure no canal."),
    # período
    dict(id="s04", block="periodo", text="Muita coisa gira e repete o mesmo movimento: [p=0.2] roda, ventilador, ponteiro de relógio. [p=0.3] {a}O tempo de uma volta completa se chama período, [p=0.2] e a letra é {b}tê maiúsculo. [p=0.2] Período é tempo, então a unidade é {c}o segundo."),
    dict(id="s05", block="periodo", text="{a}O ponteiro dos segundos leva sessenta segundos para dar uma volta: [p=0.2] {b}período de sessenta segundos. [p=0.3] {c}Um carrossel que dá uma volta a cada quatro segundos [p=0.2] tem {d}período de quatro segundos."),
    # frequência
    dict(id="s06", block="frequencia", text="A frequência é a pergunta ao contrário: [p=0.2] {a}quantas voltas cabem em um segundo? [p=0.3] A letra é {b}efe. [p=0.2] Para calcular, {c}divida o número de voltas pelo tempo. [p=0.3] {d}Dez voltas em cinco segundos: [p=0.1] {e}duas voltas por segundo."),
    dict(id="s07", block="frequencia", text="No esse i, voltas por segundo têm nome próprio: [p=0.2] {a}hertz, com o símbolo agá zê. [p=0.3] {b}Duas voltas por segundo são dois hertz. [p=0.2] O nome homenageia um físico alemão, {c}Heinrich Hertz."),
    # T = 1/f
    dict(id="s08", block="inverso", text="Período e frequência são {a}inversos. [p=0.2] Se a roda dá {b}duas voltas por segundo, [p=0.2] {c}cada volta leva meio segundo. [p=0.3] Daí a fórmula: {d}tê igual a um dividido por efe, [p=0.2] e também {e}efe igual a um dividido por tê."),
    dict(id="s09", block="inverso", text="No carrossel, {a}o período é quatro segundos. [p=0.2] {b}Efe é um dividido por quatro: [p=0.1] {c}um quarto de volta por segundo, [p=0.1] zero vírgula vinte e cinco hertz. [p=0.3] {d}Um é grande quando o outro é pequeno: [p=0.2] quanto mais voltas por segundo, menos tempo cada volta leva. [p=0.3] {e}Repare na unidade: [p=0.1] um dividido por segundo é o hertz, [p=0.1] e um dividido por hertz volta a ser segundo."),
    # rpm
    dict(id="s10", block="rpm", text="Motores e máquinas usam outra unidade: [p=0.2] {a}rotações por minuto, o erre pê eme. [p=0.3] Ela {b}não é do esse i, [p=0.2] então, antes da conta, {c}passe para hertz."),
    dict(id="s11", block="rpm", text="Como um minuto tem sessenta segundos, {a}divida por sessenta. [p=0.3] {b}Mil e duzentas voltas em um minuto [p=0.1] são {c}mil e duzentas voltas em sessenta segundos. [p=0.2] {d}Em um segundo, cabe um sessenta avos disso: [p=0.2] {e}mil e duzentos dividido por sessenta, vinte hertz. [p=0.3] {f}E o período é um vinte avos de segundo, zero vírgula zero cinco. [p=0.3] {g}No caminho de volta, multiplique: [p=0.1] dois hertz são duas voltas por segundo, [p=0.1] cento e vinte por minuto."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}multiplicar por sessenta em vez de dividir. [p=0.3] {b}Mil e duzentos vezes sessenta dá setenta e dois mil hertz. [p=0.3] {c}Absurdo: [p=0.2] em um segundo cabem menos voltas do que em um minuto inteiro. [p=0.3] {d}De rpm para hertz, o número tem que diminuir."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}rpm dividido por sessenta dá hertz, [p=0.2] e {b}hertz vezes sessenta dá rpm. [p=0.3] E o período sai direto: [p=0.2] {c}sessenta dividido pelo rpm, em segundos. [p=0.3] {d}Sessenta dividido por mil e duzentos, zero vírgula zero cinco segundo."),
    dict(id="s14", block="atalho", text="Funciona porque {a}as voltas de um minuto dividem sessenta segundos em partes iguais. [p=0.3] {b}Não compensa quando a frequência já vem em hertz: [p=0.2] aí, {c}use direto tê igual a um dividido por efe."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}A broca de uma furadeira gira a {b}três mil rotações por minuto. [p=0.3] {c}Qual é a frequência em hertz? [p=0.2] {d}E o período?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Três mil dividido por sessenta: [p=0.1] corte um zero de cada lado, trezentos dividido por seis, [p=0.1] {b}cinquenta hertz. [p=0.3] {c}Período: um dividido por cinquenta, [p=0.1] {d}dois centésimos de segundo, zero vírgula zero dois."),
    dict(id="s18", block="resposta", text="Pelo atalho, {a}sessenta dividido por três mil dá o mesmo: [p=0.2] {b}zero vírgula zero dois segundo. [p=0.2] São cinquenta voltas a cada segundo."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}período é o tempo de uma volta, [p=0.2] {b}frequência é quantas voltas por segundo, [p=0.2] {c}um é o inverso do outro, [p=0.2] e {d}de rpm para hertz, divida por sessenta."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai descobrir {a}por que a ponta da hélice anda mais rápido que o meio, [p=0.2] com {b}a velocidade angular e a velocidade linear. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
