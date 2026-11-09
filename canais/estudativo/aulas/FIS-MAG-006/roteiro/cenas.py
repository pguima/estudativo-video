# Estudativo · FIS-MAG-006 — Lei de Lenz (Física · Magnetismo · Magnetismo e indução).
# Habilidade: achar o sentido da corrente induzida, lembrando que ela reage à mudança, como no freio magnético.
# Pré-requisitos: FIS-MAG-005. Próxima: FIS-MAG-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Sentido da espira pela mão direita de FIS-MAG-002 (dedos na corrente, polegar no norte):
# vista de frente, corrente anti-horária = face norte; horária = face sul. Conservação de energia (FIS-ENE-005) não está em
# "Já ensinado": o motivo da lei é dito como "o ímã ganharia movimento do nada".

TITULO = "Lei de Lenz"

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
    dict(id="s01", block="gancho", text="{a}Solte um ímã dentro de um cano de cobre. [p=0.2] {b}O cobre não gruda no ímã. [p=0.3] Mesmo assim, {c}o ímã desce devagar, [p=0.2] como se alguém segurasse. [p=0.3] {d}Quem segura é a corrente que o próprio ímã cria no cano."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai achar o sentido da corrente induzida [p=0.2] e {b}entender por que ela sempre freia o movimento."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre {a}duas coisas. [p=0.2] {b}Fluxo mudando numa espira cria corrente, pela lei de Faraday. [p=0.3] E {c}uma espira com corrente vira um ímã: [p=0.2] dedos da mão direita no sentido da corrente, [p=0.1] e o polegar aponta o norte. [p=0.3] Se faltar alguma, procure no canal."),
    # a lei
    dict(id="s04", block="lei", text="A lei de Lenz diz: [p=0.2] {a}a corrente induzida cria um campo que luta contra a mudança do fluxo. [p=0.3] {b}Se o fluxo aumenta, ela tenta diminuir. [p=0.2] {c}Se o fluxo diminui, ela tenta manter. [p=0.3] {d}A espira é do contra."),
    # aproxima
    dict(id="s05", block="aproxima", text="Veja na prática. [p=0.2] {a}O polo norte de um ímã se aproxima de uma espira. [p=0.3] {b}Mais linhas passam por dentro dela: [p=0.1] o fluxo aumenta. [p=0.3] Para lutar contra, {c}a espira vira um ímã com a face norte virada para o ímã. [p=0.2] {d}Norte com norte: ela empurra o ímã para trás."),
    dict(id="s06", block="aproxima", text="E qual é o sentido da corrente? [p=0.2] {a}Para o polegar sair da espira na direção do ímã, [p=0.2] {b}os dedos giram no sentido anti-horário, [p=0.1] para quem olha do lado do ímã. [p=0.3] {c}Face norte, corrente anti-horária."),
    # afasta
    dict(id="s07", block="afasta", text="Agora, {a}o ímã se afasta. [p=0.2] {b}O fluxo diminui. [p=0.3] A espira tenta manter o fluxo, [p=0.2] e {c}vira um ímã com a face sul virada para o ímã. [p=0.2] {d}Sul com norte: ela puxa o ímã de volta."),
    dict(id="s08", block="afasta", text="{a}Face sul, para quem olha do lado do ímã, [p=0.1] {b}corrente no sentido horário. [p=0.3] Repare: {c}chegando, a espira empurra. [p=0.2] {d}Saindo, a espira puxa. [p=0.3] Ela sempre atrapalha o movimento."),
    # por quê
    dict(id="s09", block="porque", text="E por que é sempre contra? [p=0.2] {a}Imagine o contrário: a espira puxando o ímã que chega. [p=0.3] {b}Ele chegaria mais rápido, [p=0.1] {c}a corrente cresceria, [p=0.1] {d}e o puxão também. [p=0.3] {e}O ímã ganharia movimento do nada, [p=0.2] e isso nunca acontece."),
    dict(id="s10", block="porque", text="É por isso que a lei de Faraday {a}tem um sinal de menos: [p=0.2] {b}épsilon igual a menos delta fi, dividido por delta tê. [p=0.3] {c}O menos é a lei de Lenz."),
    # freio
    dict(id="s11", block="freio", text="Agora, o cano de cobre. [p=0.2] {a}Cada pedaço do cano funciona como uma espira. [p=0.3] {b}Abaixo do ímã, o fluxo aumenta, e o cano empurra para cima. [p=0.2] {c}Acima do ímã, o fluxo diminui, e o cano puxa para cima. [p=0.3] {d}As duas forças freiam a queda."),
    dict(id="s12", block="freio", text="{a}É o freio magnético. [p=0.2] {b}Algumas montanhas-russas param assim: [p=0.2] ímãs passam perto de placas de metal, [p=0.2] e {c}o carrinho freia sem nada encostar."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que a espira sempre empurra o ímã. [p=0.3] {b}Ela luta contra a mudança, não contra o ímã. [p=0.3] {c}Com o ímã se afastando, a espira puxa. [p=0.2] {d}Na prova, comece sempre perguntando: o fluxo aumenta ou diminui?"),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova. [p=0.2] {a}Chegou, repele. [p=0.2] {b}Saiu, atrai. [p=0.3] {c}Repelir é pôr na frente do ímã a face igual ao polo dele. [p=0.2] {d}Atrair é pôr a face oposta."),
    dict(id="s15", block="atalho", text="{a}Depois, a face vira sentido: [p=0.2] {b}face norte, anti-horário; [p=0.1] {c}face sul, horário, [p=0.1] sempre olhando do lado do ímã. [p=0.3] {d}Se a figura mostra a espira olhada do outro lado, inverta. [p=0.3] {e}Sem ímã, só um campo mudando? [p=0.2] Fluxo aumentou, a espira cria campo contrário. [p=0.2] Diminuiu, cria campo a favor. [p=0.2] Depois, a mão direita da espira dá o sentido."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}O polo sul de um ímã se afasta de uma espira. [p=0.3] {b}Que face a espira cria do lado do ímã? [p=0.2] {c}E qual é o sentido da corrente, para quem olha do lado do ímã?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}O ímã saiu: [p=0.1] {b}a espira atrai. [p=0.3] {c}Para atrair um sul, a face precisa ser norte. [p=0.3] {d}Face norte, olhando do lado do ímã: [p=0.1] {e}corrente no sentido anti-horário."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}a corrente induzida luta contra a mudança do fluxo, [p=0.2] {b}chegou, repele; saiu, atrai, [p=0.2] e {c}face norte é anti-horário. [p=0.3] Na próxima aula, a indução trabalhando para você: [p=0.2] {d}o transformador, que muda a tensão da rede elétrica."),
    dict(id="s20", block="fim", text="{a}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {b}Bons estudos!"),
]
