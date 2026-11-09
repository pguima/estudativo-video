# Estudativo · FIS-CAL-016 — Praticando: propagação e termodinâmica (Física · Calor e Termodinâmica · prática).
# Habilidade: identificar a propagação do calor e aplicar as leis da termodinâmica em motores, geladeiras e usinas.
# Pré-requisitos: FIS-CAL-009, 010, 011, 012, 013, 014, 015, 017. Próxima: nenhuma (última aula da trilha).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questões inéditas, criadas para esta aula.
# Situações: 1 condução, convecção e irradiação (panela) · 2 trabalho no ciclo pela área (kPa × L = J) · 3 primeira lei na isobárica ·
# 4 rendimento e teste de Carnot (motor impossível; o erro de usar Celsius aprova o motor) · 5 geladeira (Qq = Qf + τ).

TITULO = "Praticando: propagação e termodinâmica"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações, [p=0.2] criadas para esta aula, [p=0.2] {b}da cozinha até o motor. [p=0.3] Em cada uma, {c}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}os três jeitos de o calor passar, [p=0.2] {b}tau igual a pê vezes delta vê, [p=0.2] {c}quê igual a tau mais delta U, [p=0.2] {d}o rendimento [p=0.2] e {e}o limite de Carnot. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: panela
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Uma panela de alumínio com água está no fogo. [p=0.3] {b}Que processo leva o calor da chama através do fundo da panela? [p=0.2] {c}Que processo espalha esse calor por toda a água? [p=0.2] E {d}como o calor da chama chega à mão de quem está ao lado do fogão?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá, com as duas perguntas do atalho. [p=0.2] {a}No fundo da panela, o metal é sólido e não anda: [p=0.2] {b}é condução. [p=0.3] {c}Na água, a de baixo esquenta, fica menos densa e sobe, [p=0.2] e {d}a de cima, mais fria, desce. [p=0.2] A matéria anda: [p=0.1] {e}é convecção. [p=0.3] {f}Quem responde só convecção esquece que o calor precisa atravessar o metal primeiro. [p=0.3] {g}E a mão ao lado do fogão? [p=0.2] O ar entre ela e a chama não leva esse calor: [p=0.2] {h}ele chega como luz, por irradiação."),
    # situação 2: ciclo
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] Um gás faz um ciclo em forma de retângulo no gráfico pê vê, no sentido horário. [p=0.3] {b}A pressão vai de cem a trezentos quilopascals, [p=0.2] e {c}o volume, de dois a cinco litros. [p=0.3] {d}Qual é o trabalho em cada volta?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] {a}No ciclo, o trabalho é a área de dentro. [p=0.3] {b}Altura: trezentos menos cem, duzentos quilopascals. [p=0.2] {c}Base: cinco menos dois, três litros. [p=0.3] {d}Quilopascal vezes litro dá joule direto: [p=0.2] {e}seiscentos joules."),
    dict(id="s09", block="resposta2", text="{a}Quem calcula só a área embaixo do caminho de cima, trezentos vezes três, acha novecentos joules: [p=0.2] esse é só o trabalho da ida. [p=0.3] {b}Sentido horário, o trabalho é positivo. [p=0.2] E como no ciclo delta U é zero, {c}o gás também recebe seiscentos joules de calor, no saldo de cada volta."),
    # situação 3: isobárica
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] Um gás recebe {b}mil joules de calor [p=0.2] e se expande {c}de dois para seis litros, [p=0.2] {d}a pressão constante de cem quilopascals. [p=0.3] {e}Quanto vale delta U?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] Pressão constante: {a}isobárica, então nenhum termo some. [p=0.3] {b}Tau: cem vezes quatro litros, quatrocentos joules. [p=0.3] {c}Delta U é quê menos tau: [p=0.2] {d}mil menos quatrocentos, seiscentos joules. [p=0.3] {e}O saldo é positivo: o gás esquentou. [p=0.3] {f}Quem responde mil joules esqueceu o trabalho, [p=0.2] como se o volume não tivesse mudado."),
    # situação 4: motor e Carnot
    dict(id="s13", block="questao4", text="{a}Situação quatro. [p=0.2] Em cada ciclo, um motor {b}recebe mil e quinhentos joules de uma fonte a quatrocentos e vinte e sete graus Celsius [p=0.2] e {c}joga seiscentos e setenta e cinco joules numa fonte a setenta e sete graus. [p=0.3] {d}Qual é o rendimento? [p=0.2] {e}O motor é possível?"),
    dict(id="s14", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta4", text="Vamos lá. [p=0.2] {a}Um menos quê frio sobre quê quente. [p=0.2] {b}Seiscentos e setenta e cinco dividido por mil e quinhentos: zero vírgula quarenta e cinco. [p=0.3] {c}Um menos zero vírgula quarenta e cinco: [p=0.1] {d}cinquenta e cinco por cento."),
    dict(id="s16", block="resposta4", text="Agora, o limite. [p=0.2] {a}A diferença das temperaturas: quatrocentos e vinte e sete menos setenta e sete, trezentos e cinquenta. [p=0.2] {b}A quente em kelvin: setecentos. [p=0.3] {c}Trezentos e cinquenta dividido por setecentos, cinquenta por cento. [p=0.3] {d}Cinquenta e cinco é mais que cinquenta: [p=0.2] {e}o motor é impossível. [p=0.3] {f}Quem usa graus Celsius acha um limite de cerca de oitenta e dois por cento, [p=0.2] e aprova um motor que não pode existir."),
    # situação 5: geladeira
    dict(id="s17", block="questao5", text="{a}Última situação. [p=0.2] Uma geladeira {b}retira quatrocentos joules do interior em cada ciclo, [p=0.2] e {c}a grade de trás solta quinhentos joules na cozinha. [p=0.3] {d}Quanto trabalho o compressor gasta em cada ciclo?"),
    dict(id="s18", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta5", text="Vamos lá. [p=0.2] {a}O lado quente é a soma das outras duas setas: [p=0.2] {b}quinhentos é igual a quatrocentos mais tau. [p=0.3] {c}Tau é cem joules. [p=0.3] {d}A cozinha recebe mais calor do que a geladeira tira, [p=0.2] e é por isso que a porta aberta não refresca nada."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}pergunte se o calor precisa de matéria e se a matéria anda; [p=0.2] {b}no gráfico pê vê, trabalho é área; [p=0.2] {c}na dúvida do sinal, use a caixa; [p=0.2] e {d}teste toda máquina contra Carnot, em kelvin."),
    dict(id="s21", block="fim", text="Com isso, você {a}fecha a trilha de calor e termodinâmica. [p=0.3] {b}Continue pela playlist Física do Zero. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
