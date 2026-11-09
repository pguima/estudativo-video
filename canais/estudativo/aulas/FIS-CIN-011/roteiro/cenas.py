# Estudativo · FIS-CIN-011 — Gráfico posição por tempo (Física · Cinemática · Gráficos do movimento).
# Habilidade: tirar a velocidade da inclinação do gráfico s × t e reconhecer repouso, ida, volta e encontro em retas e parábolas.
# Pré-requisitos: FIS-CIN-008 (função do 2º grau), MAT-FUN-007 (ler gráfico), MAT-FUN-010 (taxa de variação). Próxima: FIS-CIN-012.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. FIS-CIN-006 (encontro) NÃO está em "Já ensinado": o encontro é definido aqui.
# Parábola do exemplo: s = 8t − t² (a = −2 m/s², v0 = 8 m/s), vértice em t = 4 s, s = 16 m.

TITULO = "Gráfico posição por tempo"

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
    dict(id="s01", block="gancho", text="{a}Duas retas num gráfico da posição pelo tempo. [p=0.2] {b}Uma sobe devagar. [p=0.1] {c}A outra sobe quase em pé. [p=0.3] Qual carro é o mais rápido? [p=0.3] {d}O da reta mais inclinada. [p=0.2] Nesse gráfico, {e}a inclinação é a velocidade."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai tirar a velocidade do gráfico [p=0.2] e reconhecer {b}repouso, [p=0.1] {c}ida, [p=0.1] {d}volta [p=0.1] e {e}encontro, em retas e parábolas."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}ler um gráfico, vendo quando ele sobe e quando desce; [p=0.2] {c}a taxa de variação, delta ípsilon dividido por delta xis; [p=0.2] e {d}as funções da posição, a do movimento uniforme e a do eme u vê. [p=0.3] Se faltar alguma, procure no canal."),
    # ler o gráfico
    dict(id="s04", block="ler", text="No gráfico esse por tê, {a}o tempo fica no eixo deitado, [p=0.1] e {b}a posição, no eixo em pé. [p=0.3] {c}Cada ponto diz onde o corpo estava em cada instante. [p=0.2] {d}No instante dois segundos, este corpo estava na posição vinte metros."),
    dict(id="s05", block="ler", text="No movimento uniforme, {a}esse igual a dez mais cinco tê. [p=0.2] É uma função afim, então o gráfico é {b}uma reta. [p=0.3] {c}Ela corta o eixo da posição no esse zero: dez metros."),
    dict(id="s06", block="ler", text="E a velocidade? [p=0.2] {a}É a taxa de variação da reta: [p=0.2] {b}delta esse dividido por delta tê. [p=0.3] {c}De zero a quatro segundos, [p=0.1] {d}a posição vai de dez a trinta. [p=0.2] {e}Vinte metros em quatro segundos: cinco metros por segundo. [p=0.2] O mesmo número colado no tê."),
    # ida, repouso, volta
    dict(id="s07", block="passeio", text="Agora, um passeio inteiro. [p=0.2] {a}De zero a quatro segundos, a reta sobe: [p=0.1] {b}a posição aumenta, e o corpo vai. [p=0.3] {c}De quatro a seis, a reta fica deitada: [p=0.1] {d}a posição não muda, é repouso. [p=0.3] {e}De seis a dez, a reta desce: [p=0.1] {f}a posição diminui, e o corpo volta."),
    dict(id="s08", block="passeio", text="{a}Subindo, velocidade positiva. [p=0.1] {b}Deitada, velocidade zero. [p=0.1] {c}Descendo, velocidade negativa. [p=0.3] Na volta, {d}de vinte a zero metros em quatro segundos: menos cinco metros por segundo."),
    # encontro
    dict(id="s09", block="encontro", text="E o encontro? [p=0.2] {a}Dois corpos no mesmo gráfico. [p=0.2] {b}Onde as linhas se cruzam, eles estão na mesma posição, no mesmo instante: [p=0.2] {c}é o encontro. [p=0.3] {d}Olhe para baixo, para saber quando; [p=0.2] {e}olhe para o lado, para saber onde."),
    # parábola
    dict(id="s10", block="parabola", text="No eme u vê, a posição tem {a}tê ao quadrado: [p=0.2] o gráfico é {b}uma parábola. [p=0.3] {c}Aceleração positiva, ela abre para cima; [p=0.2] {d}negativa, abre para baixo. [p=0.3] {e}A inclinação muda a cada ponto: [p=0.2] ficando mais em pé, a velocidade aumenta em módulo; [p=0.2] ficando mais deitada, ela diminui."),
    dict(id="s11", block="parabola", text="E no {a}vértice, o ponto mais alto ou mais baixo, [p=0.2] a curva fica deitada por um instante: [p=0.2] {b}a velocidade é zero. [p=0.3] É ali que o corpo {c}para e vira: [p=0.2] {d}antes ia, depois volta. [p=0.3] Repare: antes do vértice, o corpo freia; depois, acelera, já na volta."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: {a}ler o gráfico como o desenho do caminho. [p=0.3] {b}A reta sobe, e a pessoa acha que o carro {c}subiu uma ladeira. [p=0.3] {d}Não: o carro pode estar numa rua plana. [p=0.2] {e}O que sobe é o número da posição, com o tempo passando."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}para comparar velocidades, compare as inclinações, sem conta. [p=0.2] {b}Mais em pé, mais rápido. [p=0.1] {c}Retas paralelas, a mesma velocidade. [p=0.3] {d}E, para o valor, escolha dois pontos que caem bem na grade."),
    dict(id="s14", block="atalho", text="Funciona porque {a}a inclinação é delta esse dividido por delta tê: a própria velocidade. [p=0.3] {b}Não compensa comparar no olho quando os gráficos têm escalas diferentes: [p=0.2] aí, faça a conta. [p=0.2] {c}E, na parábola, a conta entre dois pontos dá só a velocidade média do trecho."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] No gráfico, {a}o carro A sai da posição zero, [p=0.1] e {b}o carro B sai da posição sessenta metros. [p=0.3] {c}Qual é a velocidade de cada um? [p=0.2] {d}Quando e onde eles se encontram?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}A vai de zero a oitenta metros em oito segundos: dez metros por segundo. [p=0.3] {b}B vai de sessenta a vinte metros em oito segundos. [p=0.2] {c}Vinte menos sessenta, menos quarenta, dividido por oito: menos cinco metros por segundo. [p=0.2] {d}B volta."),
    dict(id="s18", block="resposta", text="{a}As retas se cruzam no instante quatro segundos, [p=0.2] {b}na posição quarenta metros. [p=0.3] Confira: {c}A anda dez vezes quatro, quarenta. [p=0.2] {d}B: sessenta menos cinco vezes quatro, quarenta. [p=0.2] Bateu."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}no gráfico esse por tê, a inclinação é a velocidade; [p=0.2] {b}sobe, vai; [p=0.1] deitada, repouso; [p=0.1] desce, volta; [p=0.2] {c}cruzou, encontrou."),
    dict(id="s20", block="fim", text="Na próxima aula, o eixo em pé vira velocidade: [p=0.2] {a}a inclinação dá a aceleração, [p=0.2] e {b}a área embaixo da linha dá o deslocamento. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
