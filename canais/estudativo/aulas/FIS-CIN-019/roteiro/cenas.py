# Estudativo · FIS-CIN-019 — Velocidade angular e velocidade linear (Física · Cinemática · Movimento circular).
# Habilidade: calcular ω = 2π/T e v = ω·R e explicar por que um ponto mais longe do centro anda mais rápido.
# Pré-requisitos: FIS-CIN-018 (T e f), FIS-CIN-005 (MU), MAT-POL-004 (C = 2πr), MAT-TRI-007 (radianos). Próxima: FIS-CIN-020.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula. π = 3.
# Contas: carrossel T = 6 s; borda R = 3 m: v = 2·3·3/6 = 3 m/s; R = 1 m: v = 1 m/s; ω = 2·3/6 = 1 rad/s; v = 1·3 = 3.
# Questão: f = 2 Hz → T = 0,5 s; ω = 6/0,5 = 12 rad/s (= 2·3·2); v = 12·0,3 = 3,6 m/s.

TITULO = "Velocidade angular e velocidade linear"

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
    dict(id="s01", block="gancho", text="Num carrossel, {a}uma criança vai na borda [p=0.1] e {b}outra perto do centro. [p=0.3] {c}As duas dão uma volta no mesmo tempo. [p=0.3] Mas {d}a da borda anda mais rápido. [p=0.3] Como pode?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular {b}a velocidade angular [p=0.2] e {c}a velocidade linear, [p=0.2] e {d}resolver esse mistério."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}o período, o tempo de uma volta; [p=0.2] {c}o comprimento da circunferência, dois pi erre; [p=0.2] e {d}o ângulo de uma volta inteira em radianos, dois pi. [p=0.3] Se faltar alguma, procure no canal."),
    # velocidade linear
    dict(id="s04", block="linear", text="Comece pela {a}velocidade linear, [p=0.1] a de sempre: [p=0.2] {b}distância dividida pelo tempo. [p=0.3] Numa volta, o ponto percorre {c}a circunferência inteira, dois pi erre, [p=0.2] no tempo de {d}um período. [p=0.3] Então {e}vê é dois pi erre dividido por tê, em metros por segundo."),
    dict(id="s05", block="linear", text="O carrossel dá uma volta a cada {a}seis segundos. [p=0.2] Use pi igual a três. [p=0.3] {b}Na borda, a três metros do centro: [p=0.1] dois vezes três vezes três, dezoito metros, [p=0.1] dividido por seis, {c}três metros por segundo. [p=0.3] {d}A um metro do centro: seis metros em seis segundos, [p=0.1] {e}um metro por segundo."),
    dict(id="s06", block="linear", text="{a}Mesmo tempo, caminho três vezes maior. [p=0.3] Por isso a criança da borda anda mais rápido."),
    # velocidade angular
    dict(id="s07", block="angular", text="Mas há algo igual para as duas: [p=0.2] {a}o ângulo que elas giram. [p=0.3] {b}Em seis segundos, as duas giram uma volta inteira, dois pi radianos. [p=0.3] Isso é a {c}velocidade angular, [p=0.1] {d}a letra grega ômega: [p=0.2] {e}o ângulo girado dividido pelo tempo."),
    dict(id="s08", block="angular", text="Numa volta, {a}ômega é dois pi dividido por tê, [p=0.2] em {b}radianos por segundo. [p=0.3] No carrossel, {c}dois vezes três dividido por seis: [p=0.1] {d}um radiano por segundo, [p=0.2] {e}igual para todos os pontos."),
    # v = ωR
    dict(id="s09", block="ligacao", text="Agora, junte as duas. [p=0.2] {a}Vê é dois pi erre dividido por tê. [p=0.2] Separe o erre: [p=0.1] {b}dois pi dividido por tê, vezes erre. [p=0.3] {c}Dois pi dividido por tê é ômega. [p=0.2] Então: {d}vê igual a ômega vezes erre."),
    dict(id="s10", block="ligacao", text="Vê é a velocidade linear, {a}em metros por segundo, [p=0.2] ômega é a angular, {b}em radianos por segundo, [p=0.2] e erre é {c}a distância até o centro, em metros. [p=0.3] Na borda: {d}um vezes três, três metros por segundo. [p=0.2] Bateu. [p=0.3] {e}Ômega igual, erre maior, vê maior: esse é o mistério resolvido."),
    dict(id="s11", block="ligacao", text="E a direção? [p=0.2] Se a criança soltar a mão, ela sai {a}pela tangente: [p=0.2] {b}a reta que só encosta na circunferência, [p=0.1] {c}de lado, formando um ângulo reto com o raio. [p=0.3] {d}A velocidade linear aponta sempre assim."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}dizer que a criança da borda gira mais rápido. [p=0.3] {b}Girar, as duas giram igual: [p=0.2] {c}a mesma velocidade angular. [p=0.2] {d}O que muda é a velocidade linear. [p=0.3] Na prova, leia qual das duas a questão pede."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}no mesmo corpo girando, a velocidade linear é proporcional ao raio. [p=0.3] {b}Dobrou a distância até o centro, dobrou a velocidade. [p=0.2] {c}Ponto a três metros anda três vezes mais rápido que o ponto a um metro, [p=0.1] sem calcular ômega."),
    dict(id="s14", block="atalho", text="Funciona porque {a}ômega é o mesmo para todo o corpo, [p=0.2] e {b}vê é ômega vezes erre. [p=0.3] {c}Não compensa quando os pontos estão em rodas diferentes: [p=0.2] aí, ômega pode mudar, e esse é o assunto da próxima aula."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}A roda de uma bicicleta tem {b}zero vírgula três metro de raio [p=0.2] e gira com frequência de {c}dois hertz. [p=0.3] {d}Qual é a velocidade angular da roda? [p=0.2] {e}E a velocidade linear de um ponto da borda? [p=0.2] Use pi igual a três."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Dois hertz: duas voltas por segundo, [p=0.1] {b}então o período é meio segundo. [p=0.3] {c}Ômega: dois vezes três, seis, [p=0.1] dividido por zero vírgula cinco, [p=0.1] {d}doze radianos por segundo."),
    dict(id="s18", block="resposta", text="{a}Vê igual a ômega vezes erre: [p=0.1] doze vezes zero vírgula três, [p=0.1] {b}três vírgula seis metros por segundo. [p=0.3] {c}Atalho: ômega também é dois pi vezes efe, [p=0.1] dois vezes três vezes dois, doze. [p=0.2] Sem passar pelo período."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}ômega é dois pi dividido por tê, igual para o corpo todo; [p=0.2] {b}vê é ômega vezes erre, [p=0.2] e por isso {c}quem está mais longe do centro anda mais rápido."),
    dict(id="s20", block="fim", text="Na próxima aula, as rodas se ligam: [p=0.2] {a}correias, engrenagens e eixos, [p=0.2] até {b}as marchas da bicicleta. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
