# Estudativo · QUI-ORG-004 — Nomear cadeias ramificadas (Química · Química Orgânica · Cadeias carbônicas e hidrocarbonetos).
# Habilidade: achar a cadeia principal, numerar e chegar a 2,3-dimetilbutano.
# Pré-requisitos: QUI-ORG-003 (prefixo, infixo, sufixo; numerar pela ponta mais perto). Próxima: QUI-ORG-005 (prática: combustíveis e fármacos).
# Marcas: {cue} animação · [p=0.2] pausa. Nomes falados com vírgula de respiro: 2,3-dimetilbutano = "dois, três, dimetilbutano".
# Exemplos: 2-metilpentano; 2,3-dimetilbutano (C6H14: 6 carbonos, nome com "butano"); 3-etil-2-metilpentano (ordem alfabética, só na tela);
# erro: CH3–CH(C2H5)–CH2–CH3 lido como "2-etilbutano" é o 3-metilpentano (etil no C2 sempre esconde cadeia maior).
# Questão: iso-octano (CH3)3C–CH2–CH(CH3)2 = 2,2,4-trimetilpentano (pelo outro lado daria 2,4,4). O iso-octano é o padrão 100 da octanagem.
# Questão inédita, criada para esta aula.

TITULO = "Nomear cadeias ramificadas"

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
    dict(id="s01", block="gancho", text="{a}Esta molécula tem seis carbonos, [p=0.2] mas o nome dela termina em butano, que é quatro. [p=0.3] {b}Dois, três, dimetilbutano. [p=0.3] {c}Onde foram parar os outros carbonos?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}achar a cadeia principal, [p=0.1] {c}numerar do lado certo [p=0.1] e {d}montar o nome inteiro, [p=0.2] com {e}um atalho para não errar a numeração."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula passada: [p=0.2] {a}o prefixo conta os carbonos, como em metano, etano, propano, butano, pentano e hexano. [p=0.2] {b}O pedaço an quer dizer só ligações simples. [p=0.2] {c}E a numeração começa pela ponta mais perto da dupla ou da tripla."),
    # cadeia principal e galhos
    dict(id="s04", block="principal", text="{a}Numa cadeia ramificada, o nome nasce da cadeia principal: [p=0.2] {b}a maior fila de carbonos seguidos que você consegue traçar. [p=0.3] {c}Ela pode fazer curva: [p=0.1] não precisa estar desenhada reta."),
    dict(id="s05", block="principal", text="{a}O que fica de fora da cadeia principal é o galho, [p=0.1] que muitas provas chamam de radical. [p=0.2] {b}O nome do galho usa o mesmo prefixo, com il no fim. [p=0.2] {c}Um carbono é metil. [p=0.1] {d}Dois carbonos, etil."),
    # exemplo em quatro passos
    dict(id="s06", block="passos", text="Veja os passos neste bastão. [p=0.2] {a}Passo um: [p=0.1] a maior fila tem cinco carbonos, pent. [p=0.2] {b}Passo dois: [p=0.1] sobra um carbono de fora, um metil."),
    dict(id="s07", block="passos", text="{a}Passo três: [p=0.1] numere pela ponta mais perto do galho. [p=0.2] {b}O metil fica no carbono dois. [p=0.3] {c}Passo quatro: [p=0.1] escreva a posição, um tracinho e o nome do galho, [p=0.1] {d}e, por último, o nome da cadeia, tudo junto. [p=0.2] {e}Dois metilpentano."),
    # o 2,3-dimetilbutano
    dict(id="s08", block="dimetil", text="Volte à molécula do começo. [p=0.2] {a}A maior fila tem quatro carbonos: but. [p=0.2] {b}Os outros dois são galhos de um carbono: [p=0.1] dois grupos metil. [p=0.3] {c}De qualquer ponta, eles ficam no carbono dois e no três."),
    dict(id="s09", block="dimetil", text="{a}Galhos iguais se juntam com di, para dois, [p=0.1] e tri, para três. [p=0.2] {b}As posições vão na frente, separadas por vírgula. [p=0.3] {c}Dois, três, dimetilbutano. [p=0.3] {d}Por isso o nome tem butano: [p=0.1] os outros dois carbonos estão nos galhos."),
    dict(id="s10", block="dimetil", text="{a}E se os galhos forem diferentes? [p=0.2] {b}Eles entram em ordem alfabética: [p=0.1] etil antes de metil. [p=0.2] {c}O di e o tri não contam para essa ordem."),
    # erro comum
    dict(id="s11", block="erro", text="{a}O erro mais comum é pegar a fila mais óbvia, a que corre na horizontal. [p=0.2] {b}Neste bastão, ela tem quatro carbonos, [p=0.1] e quem para ali vê um etil no carbono dois: [p=0.1] {c}dois etilbutano."),
    dict(id="s12", block="erro", text="{a}Mas a fila que entra no galho tem cinco carbonos. [p=0.2] {b}A cadeia principal é essa, e sobra só um metil: [p=0.1] {c}três metilpentano. [p=0.3] {d}Desconfie de todo etil no carbono dois: [p=0.1] ele sempre esconde uma cadeia maior."),
    # atalho
    dict(id="s13", block="atalho", text="{a}O atalho da numeração: [p=0.2] {b}antes de contar, ache o galho mais perto de uma ponta. [p=0.2] {c}Essa ponta é o carbono um. [p=0.3] {d}Se der empate, olhe o galho seguinte, [p=0.1] lembrando que dois galhos no mesmo carbono contam duas vezes. [p=0.2] {e}Vence a ponta que chega mais cedo nele."),
    dict(id="s14", block="atalho", text="{a}Funciona porque a regra pede os menores números, [p=0.1] e quem decide é o primeiro galho em que as duas pontas diferem. [p=0.3] {b}Só não vale quando a cadeia tem dupla ou tripla: [p=0.1] {c}aí, a dupla tem preferência na numeração, e isso fica para outra aula."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Este é o iso-octano, a referência da nota cem na octanagem, que mede a qualidade da gasolina. [p=0.3] {b}Qual é o nome oficial dele?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="{a}A maior fila tem cinco carbonos: pentano. [p=0.2] {b}Sobram três galhos de um carbono: trimetil. [p=0.3] {c}As duas pontas chegam a um galho já no carbono dois: empate. [p=0.2] {d}Pela esquerda, o galho seguinte também está no carbono dois. [p=0.2] {e}Pela direita, só no quatro. [p=0.2] Vence a esquerda."),
    dict(id="s18", block="resposta", text="{a}Dois, dois, quatro, trimetilpentano. [p=0.2] {b}O número se repete porque esse carbono tem dois galhos. [p=0.3] {c}Pela direita, daria dois, quatro, quatro: [p=0.1] {d}o segundo número fica maior, então está errado."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}ache a maior fila, [p=0.1] {b}dê nome aos galhos com il, [p=0.1] {c}numere pela ponta mais perto de um galho [p=0.1] e {d}junte tudo, com o nome da cadeia no fim."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai praticar tudo isso [p=0.1] {a}em moléculas de combustíveis e de remédios, do jeito que cai na prova. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
