# Estudativo · FIS-OPT-003 — Espelhos esféricos (Física · Óptica · Reflexão e espelhos).
# Habilidade: achar a imagem com os raios notáveis em espelhos côncavos e convexos.
# Pré-requisitos: FIS-OPT-002 (lei da reflexão, imagem virtual). Próxima: FIS-OPT-011 (equação dos espelhos e aumento).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Os raios notáveis valem para espelhos pouco abertos (aproximação de Gauss), dito na aula.
# A equação de Gauss e o aumento são da FIS-OPT-011: aqui só a posição e o tipo da imagem, pelos raios.

TITULO = "Espelhos esféricos: côncavo e convexo"

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
    dict(id="s01", block="gancho", text="{a}O espelho de maquiagem aumenta o seu rosto. [p=0.3] {b}O espelho da saída da garagem mostra a rua inteira, mas tudo pequeno. [p=0.3] Os dois são {c}pedaços de uma esfera. [p=0.2] Só muda {d}o lado que brilha."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai achar a imagem {b}num espelho côncavo [p=0.2] e {c}num convexo, [p=0.2] só com {d}dois raios de luz."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a lei da reflexão, com o ângulo de reflexão igual ao de incidência, medidos da normal; [p=0.2] e {c}a imagem virtual, formada pelos prolongamentos dos raios. [p=0.3] Se faltar alguma, procure no canal."),
    # côncavo e convexo
    dict(id="s04", block="tipos", text="Pegue {a}uma bola oca, espelhada por dentro e por fora, [p=0.2] e {b}corte uma tampinha dela. [p=0.3] Se o lado que reflete é {c}o de dentro, a cavidade, o espelho é côncavo. [p=0.2] {d}Côncavo lembra caverna. [p=0.3] Se é {e}o de fora, a barriga, o espelho é convexo."),
    dict(id="s05", block="tipos", text="O centro da bola é {a}o centro de curvatura, C. [p=0.2] O meio do espelho é {b}o vértice, V. [p=0.2] {c}A reta que passa por C e por V é o eixo principal. [p=0.3] E {d}na metade do caminho entre C e V fica o foco, F. [p=0.2] {e}A distância do foco ao vértice é a distância focal: [p=0.2] metade do raio de curvatura, a distância de C até V."),
    # raios notáveis
    dict(id="s06", block="raios", text="Por que esse ponto se chama foco? [p=0.2] {a}Raios que chegam paralelos ao eixo, como os do Sol, [p=0.2] {b}refletem e passam todos pelo foco. [p=0.3] {c}É assim que um forno solar esquenta a panela. [p=0.2] Isso vale bem para espelhos pouco abertos, uma tampinha pequena da esfera, como os das questões."),
    dict(id="s07", block="raios", text="Daí saem {a}os raios notáveis do côncavo. [p=0.3] {b}Um: chegou paralelo ao eixo, reflete passando pelo foco. [p=0.3] {c}Dois: chegou passando pelo foco, reflete paralelo. [p=0.3] {d}Três: chegou passando pelo centro, volta pelo mesmo caminho, [p=0.2] porque toda reta que sai do centro chega ao espelho a noventa graus: [p=0.2] ela é a própria normal."),
    dict(id="s08", block="raios", text="{a}Bastam dois desses raios, saindo da ponta do objeto. [p=0.3] {b}Onde os raios refletidos se cruzam, fica a ponta da imagem."),
    # côncavo: casos
    dict(id="s09", block="concavo", text="Objeto {a}mais longe que o centro de curvatura. [p=0.3] {b}Raio paralelo, reflete pelo foco. [p=0.2] {c}Raio pelo foco, reflete paralelo. [p=0.3] {d}Eles se cruzam de verdade, na frente do espelho: [p=0.2] a imagem é {e}real, [p=0.1] {f}invertida [p=0.1] e {g}menor."),
    dict(id="s10", block="concavo", text="Agora, {a}o objeto entre o foco e o espelho. [p=0.3] {b}Os raios refletidos se abrem e não se cruzam. [p=0.3] {c}Os prolongamentos se cruzam atrás do espelho: [p=0.2] a imagem é {d}virtual, [p=0.1] {e}direita [p=0.1] e {f}maior. [p=0.3] {g}É o espelho de maquiagem."),
    dict(id="s11", block="concavo", text="No meio do caminho estão os outros casos. [p=0.2] {a}Objeto no centro: imagem real, invertida, do mesmo tamanho. [p=0.2] {b}Entre o centro e o foco: real, invertida e maior. [p=0.2] {c}Bem no foco, os raios saem paralelos e não formam imagem nítida."),
    # convexo
    dict(id="s12", block="convexo", text="No convexo, {a}o foco fica atrás do espelho. [p=0.3] {b}O raio paralelo reflete se abrindo, [p=0.2] como se viesse do foco: [p=0.2] {c}o prolongamento é que passa por F. [p=0.3] {d}O raio que mira o centro volta pelo mesmo caminho."),
    dict(id="s13", block="convexo", text="{a}Os raios refletidos sempre se abrem. [p=0.2] Então a imagem do convexo é sempre {b}virtual, [p=0.1] {c}direita [p=0.1] e {d}menor, [p=0.2] esteja o objeto onde estiver. [p=0.3] {e}Imagem menor cabe mais coisa: [p=0.2] por isso ele é usado no retrovisor e na saída da garagem."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é achar que {a}o côncavo sempre aumenta. [p=0.3] Olhe {b}a parte de dentro de uma colher, com o braço esticado: [p=0.2] você aparece {c}pequeno e de cabeça para baixo. [p=0.3] {d}Objeto longe, além do centro: imagem real, invertida e menor. [p=0.2] {e}Quem decide é a posição do objeto."),
    # atalho
    dict(id="s15", block="atalho", text="Agora, o atalho de prova. [p=0.2] {a}No côncavo, o foco é a fronteira da natureza: [p=0.2] {b}objeto mais longe que o foco, imagem real e invertida; [p=0.2] {c}entre o foco e o espelho, virtual, direita e maior. [p=0.3] {d}O centro é a fronteira do tamanho: [p=0.2] {e}além do centro, menor; [p=0.2] {f}entre o centro e o foco, maior."),
    dict(id="s16", block="atalho", text="E mais: {a}num espelho só, real é sempre invertida, [p=0.2] e {b}virtual é sempre direita. [p=0.3] Funciona porque a imagem real se forma com os raios cruzados, [p=0.2] e a cruz troca o de cima com o de baixo. [p=0.3] {c}No convexo, nem precisa pensar: virtual, direita e menor."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Um objeto está {a}entre o centro de curvatura e o foco de um espelho côncavo. [p=0.3] {b}Como é a imagem? [p=0.3] E {c}se o espelho fosse convexo?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}O objeto está mais longe que o foco: [p=0.2] a imagem é {b}real e invertida. [p=0.3] {c}E está mais perto que o centro: [p=0.2] a imagem é {d}maior. [p=0.3] No convexo, {e}virtual, direita e menor, como sempre."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}o foco fica na metade do caminho entre o centro e o espelho; [p=0.2] {b}com dois raios notáveis, você acha a imagem; [p=0.2] e {c}o convexo sempre dá imagem virtual, direita e menor."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai {a}calcular onde fica a imagem [p=0.2] e {b}quantas vezes ela é maior, [p=0.2] com a equação dos espelhos. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
