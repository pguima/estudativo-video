# Estudativo · FIS-DIN-013 — Praticando: atrito, planos e curvas (Física · Dinâmica · Força centrípeta · prática).
# Habilidade: resolver questões de atrito, plano inclinado, sistemas de blocos e curvas.
# Pré-requisitos: FIS-DIN-007, FIS-DIN-008, FIS-DIN-009, FIS-DIN-010, FIS-DIN-011, FIS-DIN-012. Próxima: nenhuma (fim da trilha).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questões inéditas, criadas para esta aula.
# g = 10 m/s². Rampa da situação 2 com sen θ = 0,8 e cos θ = 0,6 (ângulo de cerca de 53°), dado da questão.

TITULO = "Praticando: atrito, planos e curvas"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações, criadas para esta aula, [p=0.2] com {b}atrito, rampa, blocos ligados e curvas. [p=0.3] Em cada uma, {c}pause o vídeo e resolva antes de ver a resposta. [p=0.2] É o fechamento da Dinâmica."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}quatro ferramentas: [p=0.2] {b}atrito, mi vezes ene; [p=0.2] {c}na rampa, o seno puxa e o cosseno aperta; [p=0.2] {d}blocos ligados como um corpo só; [p=0.2] e {e}na curva, a resultante para o centro é eme vê ao quadrado sobre erre."),
    # situação 1: atrito
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] {b}Uma caixa de trinta quilogramas, parada, [p=0.2] com {c}mi estático zero vírgula quatro e mi cinético zero vírgula três. [p=0.3] {d}Alguém empurra com cento e cinquenta newtons. [p=0.2] {e}A caixa se move? [p=0.1] {f}Com que aceleração?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}Normal igual ao peso, trezentos newtons. [p=0.2] {b}Limite do estático: cento e vinte. [p=0.2] {c}Cento e cinquenta passa do limite: a caixa se move. [p=0.3] {d}Andando, vale o cinético: zero vírgula três vezes trezentos, noventa. [p=0.2] {e}Resultante: cento e cinquenta menos noventa, sessenta. [p=0.2] {f}Sessenta dividido por trinta: dois metros por segundo ao quadrado."),
    # situação 2: rampa
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] {b}Um bloco desce uma rampa com seno de teta zero vírgula oito [p=0.1] e cosseno zero vírgula seis. [p=0.3] {c}O mi cinético é zero vírgula cinco. [p=0.3] {d}Qual é a aceleração?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] A massa nem foi dada, e não precisa: [p=0.2] {a}á é gê vezes, abre parênteses, seno de teta menos mi vezes cosseno de teta, fecha parênteses. [p=0.3] {b}Zero vírgula cinco vezes zero vírgula seis: zero vírgula três. [p=0.2] {c}Zero vírgula oito menos zero vírgula três: zero vírgula cinco. [p=0.2] {d}Vezes dez: cinco metros por segundo ao quadrado. [p=0.3] {e}Quem troca seno por cosseno acha dois metros por segundo ao quadrado, e erra."),
    # situação 3: polia
    dict(id="s09", block="questao3", text="{a}Situação três. [p=0.2] {b}Um bloco de três quilogramas na mesa, com mi cinético zero vírgula cinco, [p=0.2] {c}ligado por um fio e uma polia a um bloco de dois quilogramas pendurado. [p=0.3] O sistema está andando. [p=0.2] {d}Qual é a aceleração? [p=0.1] E {e}a tração?"),
    dict(id="s10", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s11", block="resposta3", text="Vamos lá, como um corpo só. [p=0.2] {a}A favor: o peso pendurado, vinte newtons. [p=0.2] {b}Contra: o atrito, zero vírgula cinco vezes trinta, quinze. [p=0.3] {c}Á é vinte menos quinze, dividido por cinco: um metro por segundo ao quadrado. [p=0.3] {d}Tração, pelo bloco da mesa: tê menos quinze é igual a três vezes um. [p=0.2] {e}Tê vale dezoito newtons, menos que o peso pendurado, como devia. [p=0.3] Confira no pendurado: {f}vinte menos dezoito, dois, dividido por dois, um. [p=0.2] Bateu."),
    # atalho
    dict(id="s12", block="atalho", text="Uma pausa para o atalho que une as três primeiras: [p=0.2] {a}escreva a aceleração como forças a favor menos forças contra, [p=0.2] {b}dividido pelas massas que andam. [p=0.3] {c}Atrito, parte do peso na rampa e peso pendurado entram todos nessa mesma linha. [p=0.3] {d}Só antes, no atrito, confira se o corpo sai do lugar."),
    # situação 4: curva plana
    dict(id="s13", block="questao4", text="{a}Situação quatro. [p=0.2] {b}Uma curva plana de quarenta e cinco metros de raio, [p=0.2] com {c}mi estático zero vírgula cinco. [p=0.3] {d}Qual é a velocidade máxima, em quilômetros por hora?"),
    dict(id="s14", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta4", text="Vamos lá. [p=0.2] {a}O atrito estático faz a centrípeta: [p=0.1] {b}vê ao quadrado é mi vezes gê vezes erre. [p=0.2] {c}Zero vírgula cinco vezes dez vezes quarenta e cinco: duzentos e vinte e cinco. [p=0.2] {d}Raiz: quinze metros por segundo. [p=0.2] {e}Vezes três vírgula seis: cinquenta e quatro quilômetros por hora."),
    # situação 5: lombada
    dict(id="s16", block="questao5", text="{a}Última situação. [p=0.2] {b}Um carro passa pelo topo de uma lombada de quarenta metros de raio. [p=0.3] {c}Qual é a maior velocidade sem as rodas perderem o contato com o chão?"),
    dict(id="s17", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta5", text="Vamos lá. [p=0.2] {a}No topo, o centro fica embaixo: pê menos ene é eme vê ao quadrado sobre erre. [p=0.3] {b}Perder o contato é a normal chegar a zero. [p=0.2] Aí, {c}vê é a raiz de gê vezes erre, a mesma conta do topo do looping. [p=0.3] {d}Raiz de dez vezes quarenta, raiz de quatrocentos: [p=0.1] {e}vinte metros por segundo, setenta e dois quilômetros por hora."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}desenhe as forças, [p=0.2] {b}na rampa decomponha o peso, [p=0.2] {c}nos blocos junte tudo num corpo só [p=0.2] e {d}na curva marque o centro."),
    dict(id="s20", block="fim", text="Com isso, {a}você fechou a Dinâmica: [p=0.2] {b}as três leis de Newton, o atrito, as rampas e as curvas. [p=0.3] A trilha seguinte é a de energia, que começa pelo trabalho de uma força. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
