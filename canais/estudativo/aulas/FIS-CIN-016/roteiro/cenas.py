# Estudativo · FIS-CIN-016 — Lançamento oblíquo (Física · Cinemática · Queda livre e lançamentos).
# Habilidade: decompor a velocidade inicial e calcular altura e alcance, sabendo que, para saída e chegada na mesma altura, sem
# resistência do ar, 45° dá o maior alcance e ângulos complementares dão o mesmo alcance.
# Pré-requisitos: FIS-CIN-014 (vertical), FIS-CIN-015 (horizontal), FIS-CIN-003 (decompor), MAT-TRI-001/003. Próxima: FIS-CIN-017.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Contas (v0 = 50, cos = 0,8, sen = 0,6): vx = 40, vy = 30; t_sub = 3 s; H = 5·9 = 45 m (= 900/20); voo 6 s; A = 40·6 = 240 m = 40·30/5.
# Complementar (cos = 0,6, sen = 0,8): vx = 30, vy = 40; voo 8 s; A = 30·8 = 240 m; H = 80 m.
# v0 = 20: 30° → vx = 17,32, vy = 10, A = 34,6 m; 45° → vx = vy = 14,14, A = 40 m; 60° → A = 34,6 m.
# Questão (v0 = 25, cos = 0,6, sen = 0,8): vx = 15, vy = 20; t_sub = 2 s; H = 20 m; voo 4 s; A = 60 m = 15·20/5; complementar: sen 0,6 e cos 0,8.

TITULO = "Lançamento oblíquo"

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
    dict(id="s01", block="gancho", text="Dois chutes saem com a mesma velocidade: [p=0.2] {a}um a trinta graus, [p=0.1] {b}outro a sessenta. [p=0.3] {c}Qual vai mais longe? [p=0.3] {d}Nenhum: [p=0.1] sem o ar atrapalhar, os dois caem no mesmo ponto. [p=0.3] E {e}o mais longe de todos sai a quarenta e cinco graus."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular {b}a altura máxima [p=0.2] e {c}o alcance de um lançamento inclinado, [p=0.2] e {d}entender esses ângulos."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}decompor um vetor com seno e cosseno; [p=0.2] {c}o lançamento para cima, com tempo de subida vê zero dividido por gê; [p=0.2] e {d}o lançamento horizontal, com os dois movimentos separados. [p=0.3] Se faltar alguma, procure no canal."),
    # decompor
    dict(id="s04", block="decompor", text="No lançamento oblíquo, o objeto sai {a}inclinado, fazendo um ângulo com o chão. [p=0.3] O primeiro passo é {b}decompor a velocidade de saída. [p=0.3] {c}A parte horizontal é vê zero vezes o cosseno do ângulo. [p=0.2] {d}A parte vertical é vê zero vezes o seno."),
    dict(id="s05", block="decompor", text="Uma bola sai a {a}cinquenta metros por segundo, [p=0.2] num ângulo de {b}cosseno zero vírgula oito e seno zero vírgula seis. [p=0.3] {c}Horizontal: cinquenta vezes zero vírgula oito, quarenta metros por segundo. [p=0.2] {d}Vertical: cinquenta vezes zero vírgula seis, trinta metros por segundo."),
    # vertical
    dict(id="s06", block="vertical", text="Daqui em diante, {a}cada parte cuida da sua vida, como no lançamento horizontal. [p=0.3] {b}Na vertical, é um lançamento para cima a trinta metros por segundo. [p=0.3] {c}Tempo de subida: trinta dividido por dez, três segundos. [p=0.2] {d}Altura máxima: cinco vezes três ao quadrado, quarenta e cinco metros. [p=0.2] {e}Tempo de voo: o dobro, seis segundos."),
    # horizontal
    dict(id="s07", block="horizontal", text="{a}Na horizontal, nada freia a bola: [p=0.2] ela anda {b}quarenta metros por segundo durante os seis segundos. [p=0.3] {c}Alcance: quarenta vezes seis, [p=0.1] {d}duzentos e quarenta metros."),
    # erro
    dict(id="s08", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que, no ponto mais alto, a velocidade é zero. [p=0.3] {b}Só a parte vertical zera. [p=0.2] {c}A horizontal continua quarenta metros por segundo, [p=0.2] porque a bola continua indo para a frente. [p=0.3] {d}Lá em cima, a velocidade é só a horizontal."),
    # ângulos
    dict(id="s09", block="angulos", text="Agora, os ângulos. [p=0.2] Troque o ângulo pelo {a}complementar, o que soma noventa graus com ele: [p=0.2] o seno e o cosseno {b}trocam de lugar. [p=0.3] {c}A horizontal vira trinta, e a vertical, quarenta. [p=0.3] {d}O voo dura oito segundos, [p=0.1] e o alcance é {e}trinta vezes oito, duzentos e quarenta metros. [p=0.2] {f}O mesmo! [p=0.2] Só que a bola sobe mais e demora mais."),
    dict(id="s10", block="angulos", text="Funciona porque {a}o alcance depende da parte horizontal vezes a vertical. [p=0.2] {b}Trocar a ordem não muda o produto. [p=0.3] E, com a mesma velocidade de saída, esse produto é o maior possível quando {c}as duas partes são iguais, [p=0.2] o que acontece a {d}quarenta e cinco graus. [p=0.3] {e}Saindo a vinte metros por segundo, a trinta ou a sessenta graus, a bola vai a uns trinta e cinco metros. [p=0.2] A quarenta e cinco graus, vai a quarenta."),
    # atalho
    dict(id="s11", block="atalho", text="Agora, o atalho de prova. [p=0.2] Com gê igual a dez, [p=0.2] {a}o alcance é a velocidade horizontal vezes a vertical, dividido por cinco. [p=0.3] {b}Quarenta vezes trinta, mil e duzentos, [p=0.1] dividido por cinco: {c}duzentos e quarenta. [p=0.3] Funciona porque {d}o tempo de voo é duas vezes a vertical dividida por dez, ou seja, a vertical dividida por cinco."),
    dict(id="s12", block="atalho", text="{a}Não compensa quando a bola cai numa altura diferente da saída, [p=0.2] como num chute do alto de um morro. [p=0.2] Aí, nem o atalho, nem os quarenta e cinco graus valem: [p=0.2] {b}calcule o tempo pela altura da descida, até o ponto onde a bola cai."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] {a}Uma bola é chutada do chão a {b}vinte e cinco metros por segundo, [p=0.2] num ângulo de {c}cosseno zero vírgula seis e seno zero vírgula oito. [p=0.3] {d}Qual é a altura máxima e qual é o alcance? [p=0.2] {e}E que outro ângulo daria o mesmo alcance?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] {a}Horizontal: vinte e cinco vezes zero vírgula seis, quinze. [p=0.2] {b}Vertical: vinte e cinco vezes zero vírgula oito, vinte. [p=0.3] {c}Subida: vinte dividido por dez, dois segundos. [p=0.2] {d}Altura máxima: cinco vezes dois ao quadrado, vinte metros."),
    dict(id="s16", block="resposta", text="{a}Voo: quatro segundos. [p=0.2] {b}Alcance: quinze vezes quatro, sessenta metros. [p=0.2] {c}Pelo atalho, quinze vezes vinte, dividido por cinco: sessenta. [p=0.3] E {d}o mesmo alcance sai do ângulo complementar, [p=0.1] o de seno zero vírgula seis e cosseno zero vírgula oito."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}decomponha a velocidade, [p=0.2] {b}use a vertical para o tempo e a altura, [p=0.2] {c}e a horizontal para o alcance. [p=0.3] Saindo e chegando na mesma altura, {d}quarenta e cinco graus vai mais longe."),
    dict(id="s18", block="fim", text="Na próxima aula, você vai {a}praticar tudo isso: [p=0.2] {b}gráficos, queda e lançamentos, [p=0.1] em questões novas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
