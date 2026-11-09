# Estudativo · FIS-CIN-014 — Lançamento vertical para cima (Física · Cinemática · Queda livre e lançamentos).
# Habilidade: achar altura máxima, tempo de subida com t = v0/g e tempo de voo pela simetria.
# Pré-requisitos: FIS-CIN-013 (queda livre), com FIS-CIN-007, 008 e 009 e MAT-FUN-018 (vértice) já ensinadas. Próxima: FIS-CIN-015.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Contas: v0 = 20: 20 → 10 → 0 em 2 s; t = 20/10 = 2 s; H = 400/20 = 20 m = 5·2²; voo = 4 s; s(2) = 20·2 − 5·4 = 20.
# Questão: v0 = 30: t = 3 s, H = 5·9 = 45 m (= 900/20), voo 6 s.

TITULO = "Lançamento vertical para cima"

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
    dict(id="s01", block="gancho", text="{a}Você joga uma bola para cima a vinte metros por segundo. [p=0.3] {b}Quanto tempo ela fica no ar? [p=0.3] {c}Quatro segundos, [p=0.2] e dá para saber de cabeça. [p=0.3] Lá no alto, {d}a velocidade é zero, [p=0.2] mas a gravidade {e}continua puxando."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai achar {b}o tempo de subida, [p=0.2] {c}a altura máxima [p=0.2] e {d}o tempo total no ar."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa da queda livre: [p=0.2] {a}a gravidade muda a velocidade em dez metros por segundo a cada segundo, [p=0.2] e {b}a altura da queda é cinco vezes o tempo ao quadrado. [p=0.3] Se faltar, procure no canal."),
    # subida
    dict(id="s04", block="subida", text="Na subida, a gravidade puxa para baixo e a bola vai para cima. [p=0.2] Então a gravidade {a}freia: [p=0.2] a bola {b}perde dez metros por segundo a cada segundo. [p=0.3] {c}Sai com vinte. [p=0.2] {d}Depois de um segundo, dez. [p=0.2] {e}Depois de dois, zero: [p=0.2] é {f}o ponto mais alto."),
    dict(id="s05", block="subida", text="Escolhendo para cima como positivo, a gravidade, que aponta para baixo, entra com sinal de menos: [p=0.2] {a}vê igual a vê zero menos gê vezes tê. [p=0.3] No alto, {b}vê é zero. [p=0.2] Então {c}gê vezes tê é igual a vê zero, [p=0.2] e {d}o tempo de subida é vê zero dividido por gê. [p=0.3] {e}Vinte dividido por dez, dois segundos."),
    # altura máxima
    dict(id="s06", block="altura", text="E a altura máxima? [p=0.2] Use {a}Torricelli com a velocidade final zero: [p=0.2] {b}zero igual a vê zero ao quadrado menos duas vezes gê vezes agá. [p=0.3] Isolando o agá, {c}agá é vê zero ao quadrado dividido por duas vezes gê. [p=0.3] {d}Quatrocentos dividido por vinte: [p=0.1] {e}vinte metros."),
    dict(id="s07", block="altura", text="Se você marcar a altura em cada instante, sai {a}uma parábola virada para baixo. [p=0.2] {b}O vértice é o ponto mais alto: [p=0.2] em dois segundos, vinte metros."),
    # simetria
    dict(id="s08", block="simetria", text="Agora, a parte bonita: [p=0.2] {a}a descida é uma queda livre que parte do alto. [p=0.3] A bola sobe vinte metros em dois segundos [p=0.2] e {b}desce os mesmos vinte metros nos mesmos dois segundos. [p=0.3] {c}Subida e descida levam o mesmo tempo."),
    dict(id="s09", block="simetria", text="Por isso, {a}o tempo de voo é o dobro do tempo de subida: [p=0.1] {b}quatro segundos. [p=0.3] E a bola {c}volta à sua mão com vinte metros por segundo, [p=0.2] a mesma velocidade da saída, só que {d}para baixo. [p=0.3] {e}Vale em qualquer altura: [p=0.1] passando pelo mesmo ponto, a bola tem na descida a mesma velocidade que tinha na subida, com o sentido trocado."),
    # erro
    dict(id="s10", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que, no ponto mais alto, a aceleração é zero. [p=0.3] {b}A velocidade é zero, sim. [p=0.2] Mas {c}a gravidade não desliga: [p=0.2] a aceleração continua dez metros por segundo ao quadrado, para baixo. [p=0.3] {d}Se ela fosse zero, a bola ficaria parada lá em cima para sempre."),
    # atalho
    dict(id="s11", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}a subida é a queda livre passada de trás para a frente. [p=0.3] {b}Tempo de subida: vê zero dividido por dez. [p=0.2] {c}Altura máxima: cinco vezes esse tempo ao quadrado, como na queda. [p=0.2] {d}Tempo de voo: o dobro."),
    dict(id="s12", block="atalho", text="Com vinte metros por segundo: {a}dois segundos, [p=0.1] {b}cinco vezes dois ao quadrado, vinte metros, [p=0.1] {c}quatro segundos no ar. [p=0.3] {d}Não compensa quando a bola não volta à altura de onde saiu, [p=0.2] como numa pedra jogada do alto de um prédio, que cai até a calçada. [p=0.2] Aí, {e}a descida demora mais, e o tempo de voo não é o dobro."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] {a}Uma pedra é lançada para cima a {b}trinta metros por segundo. [p=0.2] Despreze a resistência do ar. [p=0.3] {c}Qual é a altura máxima? [p=0.2] {d}E quanto tempo ela leva para voltar ao ponto de partida?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] {a}Tempo de subida: trinta dividido por dez, [p=0.1] {b}três segundos. [p=0.3] {c}Altura máxima: cinco vezes três ao quadrado, [p=0.1] cinco vezes nove, [p=0.1] {d}quarenta e cinco metros."),
    dict(id="s16", block="resposta", text="Confira com Torricelli: {a}novecentos dividido por vinte, quarenta e cinco. [p=0.2] Bateu. [p=0.3] {b}Tempo até voltar: o dobro da subida, [p=0.1] {c}seis segundos."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}o tempo de subida é vê zero dividido por gê, [p=0.2] {b}a altura máxima é vê zero ao quadrado dividido por duas vezes gê, [p=0.2] e {c}a descida leva o mesmo tempo da subida."),
    dict(id="s18", block="fim", text="Na próxima aula, o objeto sai {a}na horizontal, de uma mesa ou de um avião: [p=0.2] é {b}o lançamento horizontal, [p=0.2] com uma queda e um movimento para a frente ao mesmo tempo. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
