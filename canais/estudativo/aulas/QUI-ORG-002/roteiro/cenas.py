# Estudativo · QUI-ORG-002 — Classificar carbonos e cadeias (Química · Química Orgânica · Cadeias carbônicas e hidrocarbonetos).
# Habilidade: dizer se um carbono é primário, secundário ou terciário e classificar a cadeia em aberta ou fechada, ramificada,
# insaturada, heterogênea ou aromática.
# Pré-requisitos: QUI-ORG-001 (bastão: ponta e dobra = carbono; 4 ligações). Próxima: QUI-ORG-003 (prefixo, infixo e sufixo; pent-2-eno).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Exemplos: 2-metilbutano (C1, C4, C5 primários; C3 secundário; C2 terciário); 3-metilbut-1-eno (aberta, ramificada, insaturada,
# homogênea; 3 pontas); etanol CH3–CH2–OH (homogênea: O na ponta); CH3–O–CH3 (heterogênea: O entre carbonos).
# Questão: metilciclo-hexano: mista (anel + parte aberta; o material chama o tolueno de mista), ramificada, saturada, homogênea, não aromática; 1 primário, 5 secundários, 1 terciário.
# Atalho: carbono terciário ou quaternário = galho. Falha quando o galho sai de um heteroátomo (trimetilamina, N(CH3)3).

TITULO = "Classificar carbonos e cadeias"

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
    dict(id="s01", block="gancho", text="{a}Aberta, [p=0.1] ramificada, [p=0.1] insaturada, [p=0.1] heterogênea. [p=0.3] Parece uma lista para decorar. [p=0.2] {b}Mas cada palavra responde a uma pergunta simples sobre o desenho da molécula."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}classificar cada carbono [p=0.1] e {c}classificar uma cadeia com quatro perguntas, [p=0.2] com {d}um atalho para a mais cobrada."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula passada, você precisa de duas coisas. [p=0.2] {a}Na fórmula em bastão, cada ponta e cada dobra é um carbono. [p=0.2] {b}E o carbono faz quatro ligações."),
    # carbonos
    dict(id="s04", block="carbonos", text="{a}A cadeia carbônica é o esqueleto da molécula: [p=0.1] os carbonos ligados uns aos outros [p=0.1] e os átomos que ficam entre eles. [p=0.3] {b}Para classificar um carbono, conte só os carbonos vizinhos dele. [p=0.2] {c}Hidrogênio e oxigênio não entram nessa conta."),
    dict(id="s05", block="carbonos", text="{a}Preso a um carbono só, ele é primário. [p=0.2] {b}A dois, secundário. [p=0.2] {c}A três, terciário. [p=0.2] {d}E a quatro, quaternário."),
    dict(id="s06", block="carbonos", text="{a}Neste bastão, as três pontas são carbonos primários. [p=0.3] {b}Este, com dois vizinhos, é secundário. [p=0.3] {c}E este, de onde sai o galho, tem três vizinhos: [p=0.1] terciário."),
    # a cadeia: quatro perguntas
    dict(id="s07", block="cadeia", text="A cadeia se classifica com quatro perguntas. [p=0.3] {a}Primeira: [p=0.1] a cadeia tem anel? [p=0.2] {b}Sem anel, ela é aberta, ou acíclica. [p=0.2] {c}Com anel, fechada, ou cíclica. [p=0.2] {d}E o anel com uma parte aberta presa a ele forma a cadeia mista."),
    dict(id="s08", block="cadeia", text="{a}Segunda: [p=0.1] a cadeia tem galhos? [p=0.2] {b}Se os carbonos formam uma fila só, com duas pontas, ela é normal. [p=0.2] {c}Numa cadeia aberta com mais de duas pontas, ela é ramificada. [p=0.3] {d}A fila desenhada em zigue-zague continua sem galho. [p=0.2] {e}E, num anel, um carbono preso por fora já é um galho."),
    dict(id="s09", block="cadeia", text="{a}Terceira: [p=0.1] há ligação dupla ou tripla entre carbonos? [p=0.2] {b}Se não há, ela é saturada: [p=0.1] os carbonos estão cheios de hidrogênios. [p=0.2] {c}Se há, é insaturada."),
    dict(id="s10", block="cadeia", text="{a}Quarta: [p=0.1] há outro átomo entre dois carbonos? [p=0.2] {b}Átomo que não é carbono nem hidrogênio se chama heteroátomo, [p=0.1] como o oxigênio ou o nitrogênio. [p=0.2] {c}Se ele está entre dois carbonos, a cadeia é heterogênea. [p=0.2] {d}Se não está, homogênea."),
    dict(id="s11", block="cadeia", text="{a}E existe um anel especial: [p=0.1] seis carbonos com ligações dupla e simples alternadas, [p=0.1] o anel do benzeno. [p=0.3] {b}A cadeia com esse anel é aromática. [p=0.2] {c}O nome do benzeno e dos outros hidrocarbonetos fica para a próxima aula."),
    # exemplo
    dict(id="s12", block="exemplo", text="Faça as quatro perguntas neste bastão. [p=0.2] {a}Não tem anel: aberta. [p=0.2] {b}Tem três pontas: ramificada. [p=0.2] {c}Tem uma dupla entre carbonos: insaturada. [p=0.2] {d}Só tem carbono e hidrogênio: homogênea."),
    # erro comum
    dict(id="s13", block="erro", text="{a}O erro mais comum está na quarta pergunta. [p=0.2] Veja o álcool comum, {b}cê agá três, cê agá dois, ó agá. [p=0.3] {c}Muita gente vê o oxigênio e diz: heterogênea."),
    dict(id="s14", block="erro", text="{a}Mas o oxigênio está na ponta, preso a um carbono só. [p=0.2] {b}Ele não fica entre dois carbonos, então a cadeia é homogênea. [p=0.3] {c}Já em cê agá três, ó, cê agá três, o oxigênio está no meio: [p=0.1] {d}aí, sim, heterogênea."),
    # atalho
    dict(id="s15", block="atalho", text="{a}O atalho para a pergunta dos galhos, a mais cobrada: [p=0.2] {b}procure um carbono terciário ou quaternário. [p=0.3] {c}Se achar, a cadeia é ramificada. [p=0.2] {d}Se só tem primários e secundários, é normal."),
    dict(id="s16", block="atalho", text="{a}Funciona porque, numa fila sem galhos, cada carbono tem no máximo dois vizinhos: [p=0.1] o da frente e o de trás. [p=0.3] {b}O terceiro vizinho é sempre um galho. [p=0.3] {c}E vale até no anel: [p=0.1] o carbono que segura o galho tem três vizinhos."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Classifique a cadeia deste bastão nas quatro perguntas. [p=0.2] {b}E diga quantos carbonos são primários, secundários e terciários."),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="{a}Tem anel e uma parte aberta presa a ele: mista. [p=0.1] Alguns livros dizem só fechada. [p=0.2] {b}Tem um carbono terciário, o que segura o galho: ramificada. [p=0.2] {c}Sem dupla: saturada. [p=0.2] {d}Só carbono e hidrogênio: homogênea. [p=0.2] {e}E não é aromática, porque o anel não tem as duplas alternadas."),
    dict(id="s20", block="resposta", text="Os carbonos: [p=0.1] {a}o do galho tem um vizinho, primário. [p=0.2] {b}O que segura o galho tem três, terciário. [p=0.2] {c}E os outros cinco do anel têm dois cada, secundários. [p=0.3] {d}Um primário, cinco secundários e um terciário."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: [p=0.1] {a}o carbono se classifica pelos carbonos vizinhos, [p=0.2] e {b}a cadeia, por quatro perguntas: [p=0.1] anel, galho, dupla e heteroátomo."),
    dict(id="s22", block="fim", text="Na próxima aula, você vai dar nome aos hidrocarbonetos, [p=0.1] {a}com prefixo, infixo e sufixo, [p=0.2] e chegar a nomes como {b}pent dois eno. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
