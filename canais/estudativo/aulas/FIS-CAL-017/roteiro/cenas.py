# Estudativo · FIS-CAL-017 — Geladeira e entropia (Física · Calor e Termodinâmica · Termodinâmica e máquinas térmicas).
# Habilidade: explicar a geladeira como máquina térmica invertida e dizer o que a entropia mede.
# Pré-requisitos: FIS-CAL-015 (Carnot). Próxima: FIS-CAL-016 (prática da trilha).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Qq, Qf e τ como valores positivos, como na FIS-CAL-014. Entropia só como conceito (a fórmula ΔS = Q/T não entra).
# O ciclo do gás da geladeira usa compressão e expansão adiabáticas (FIS-CAL-013). FIS-CAL-010 (convecção) NÃO está em
# "Já ensinado": a circulação do ar dentro da geladeira não é explicada aqui.

TITULO = "Geladeira e entropia"

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
    dict(id="s01", block="gancho", text="{a}Num dia de calor, alguém deixa a porta da geladeira aberta para refrescar a cozinha. [p=0.3] {b}Funciona? [p=0.3] {c}Não. [p=0.2] {d}A cozinha esquenta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai explicar {b}a geladeira como uma máquina térmica ao contrário [p=0.2] e dizer {c}o que a entropia mede."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a máquina térmica, que recebe quê quente, faz o trabalho tau e joga quê frio na fonte fria; [p=0.2] e {c}que o calor só passa sozinho do quente para o frio, um jeito de dizer a segunda lei. [p=0.3] Se faltar alguma, procure no canal."),
    # máquina invertida
    dict(id="s04", block="invertida", text="{a}Dentro da geladeira está frio, [p=0.2] e {b}a cozinha está quente. [p=0.3] Sozinho, o calor iria {c}da cozinha para dentro. [p=0.3] A geladeira faz o caminho contrário: [p=0.2] {d}tira calor de dentro e joga na cozinha. [p=0.3] {e}Do frio para o quente, isso não acontece sozinho: [p=0.2] {f}precisa de trabalho."),
    dict(id="s05", block="invertida", text="{a}Então as setas da máquina térmica se invertem. [p=0.3] {b}O motor da geladeira, o compressor, dá um trabalho tau. [p=0.2] {c}Ela retira um quê frio do interior. [p=0.2] E {d}joga um quê quente na cozinha. [p=0.3] {e}Tudo o que entra, sai: [p=0.2] {f}quê quente é igual a quê frio mais tau."),
    # como funciona
    dict(id="s06", block="ciclo", text="Por dentro dos canos, {a}circula um gás. [p=0.3] {b}O compressor aperta esse gás de repente, [p=0.2] e {c}ele esquenta, como na compressão adiabática. [p=0.3] {d}Quente, ele passa pela grade atrás da geladeira e entrega calor para a cozinha. [p=0.3] É por isso que {e}aquela grade fica morna."),
    dict(id="s07", block="ciclo", text="{a}Depois, o gás atravessa um cano bem fino e se expande de repente. [p=0.2] {b}Ele esfria muito, [p=0.2] fica mais frio que o interior, [p=0.2] e {c}nos canos do congelador retira calor dos alimentos. [p=0.3] {d}E o ciclo recomeça."),
    # porta aberta
    dict(id="s08", block="porta", text="Agora, a porta aberta. [p=0.2] {a}A geladeira tira calor da cozinha pela porta [p=0.2] e {b}devolve esse calor para a mesma cozinha, pela grade de trás. [p=0.3] {c}E ainda soma o trabalho do motor. [p=0.3] {d}Sai mais calor do que entra: [p=0.2] {e}a cozinha esquenta."),
    dict(id="s09", block="porta", text="Com números: [p=0.2] {a}tira trezentos joules, [p=0.1] {b}o motor gasta cem, [p=0.2] {c}e a grade solta quatrocentos. [p=0.3] {d}A cozinha ganha cem joules a cada volta. [p=0.3] {e}O ar-condicionado funciona porque {f}a parte quente fica do lado de fora da casa."),
    # entropia
    dict(id="s10", block="entropia", text="E a entropia? [p=0.2] {a}Pingue uma gota de tinta num copo de água. [p=0.2] {b}Ela se espalha sozinha. [p=0.3] {c}Você nunca vê a tinta voltar a ser uma gota. [p=0.3] {d}Um café quente esfria até a temperatura da sala, [p=0.2] e {e}nunca esquenta sozinho."),
    dict(id="s11", block="entropia", text="{a}A entropia mede o quanto a energia e a matéria estão espalhadas, [p=0.2] o quanto estão desorganizadas. [p=0.3] {b}Nos processos que acontecem sozinhos, a entropia total sempre aumenta. [p=0.3] {c}Esse é outro jeito de dizer a segunda lei."),
    dict(id="s12", block="entropia", text="{a}A geladeira diminui a entropia lá dentro, [p=0.2] porque tira calor de lá. [p=0.3] {b}Mas, para isso, solta na cozinha o calor de dentro mais o trabalho do motor, [p=0.2] e {c}a entropia lá fora aumenta mais. [p=0.3] {d}Somando tudo, geladeira, cozinha e o resto, a entropia do universo cresce. [p=0.3] {e}Energia espalhada é energia mais difícil de aproveitar."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que a geladeira produz frio. [p=0.3] {b}Frio não é uma coisa que se fabrica. [p=0.2] {c}A geladeira tira calor de dentro e leva para fora. [p=0.3] {d}O frio é só o lugar que ficou com menos calor."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}desenhe as três setas. [p=0.3] {b}Na máquina térmica, o calor desce do quente para o frio e sai trabalho. [p=0.2] {c}Na geladeira, o calor sobe do frio para o quente e entra trabalho. [p=0.3] {d}Nas duas, quê quente é a soma das outras duas: [p=0.2] {e}o lado quente sempre tem o maior número."),
    dict(id="s15", block="atalho", text="Funciona porque {a}a energia não some: tudo o que entra, sai. [p=0.3] {b}Não compensa quando a questão pede só a ideia, sem números: [p=0.2] aí, {c}lembre só o sentido das setas."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Em cada ciclo, uma geladeira {a}retira seiscentos joules do interior, [p=0.2] e {b}o compressor gasta duzentos joules. [p=0.3] {c}Quanto calor vai para a cozinha? [p=0.2] E {d}a entropia do universo aumenta, diminui ou fica igual?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}O lado quente é a soma: [p=0.2] {b}seiscentos mais duzentos, [p=0.1] {c}oitocentos joules para a cozinha. [p=0.3] {d}E a entropia do universo aumenta. [p=0.2] {e}Dentro da geladeira ela diminui, [p=0.2] mas lá fora aumenta mais."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}a geladeira é uma máquina térmica ao contrário, [p=0.2] {b}que gasta trabalho para levar calor do frio para o quente; [p=0.2] e {c}a entropia mede o espalhamento, que sempre cresce no total."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai {a}praticar tudo da trilha de calor, [p=0.2] {b}da panela no fogo até o motor e a geladeira. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
