# Estudativo · MAT-FUN-007 — Ler um gráfico: máximos, zeros e crescimento (Matemática · Funções · O que é função).
# Habilidade: olhar o gráfico da temperatura de um dia e dizer a máxima, quando marcou zero, quando subiu, quando desceu, o domínio e a imagem.
# Pré-requisitos: MAT-FUN-004 (domínio e imagem), MAT-FUN-006 (gráfico de uma função). Próxima: MAT-FUN-008.
# Questão inédita, criada para esta aula. Pares narrados como "xis quinze, ípsilon oito", como na MAT-FUN-001.
# Temperatura (x = hora, y = graus), pontos ligados por trechos sem ondas: (0, −2), (6, −4), (9, 0), (15, 8), (21, 0), (24, −3).
#   Máximo 8 às 15 h · mínimo −4 às 6 h · zeros às 9 h e 21 h · cresce de 6 a 15 · decresce de 0 a 6 e de 15 a 24 ·
#   domínio [0, 24] · imagem [−4, 8] · erro: de 6 h a 9 h está negativa e subindo (−4 → 0).
# Questão: saldo de uma lojinha (x = meses desde a abertura, y = mil reais): (0, 2), (3, −4), (5, 0), (9, 6), (12, 3).
#   Maior saldo 6 no mês 9 · zeros nos meses 1 e 5 · cresce de 3 a 9 · imagem [−4, 6].
# Visual: plano (E.plano) com o gráfico da temperatura (E.curva, função por trechos); ponto máximo e mínimo com guias (E.ponto);
#   zeros marcados no eixo x; trecho que sobe pintado de verde e trechos que descem de outra cor; "sombra" do gráfico
#   projetada no eixo x (domínio) e no eixo y (imagem); depois o gráfico do saldo da lojinha.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Ler um gráfico: máximos, zeros e crescimento"

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
    dict(id="s01", block="gancho", text="{a}Este gráfico mostra a temperatura de um dia de inverno numa cidade da serra. [p=0.3] Qual foi a máxima? [p=0.2] Muita gente responde {b}quinze. [p=0.3] Mas quinze é {c}a hora. [p=0.2] A máxima foi {d}oito graus."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você lê um gráfico como esse inteiro: [p=0.2] {b}máxima, {c}zeros, {d}quando sobe e quando desce, [p=0.2] e ainda leva um {e}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o gráfico de uma função, em que cada ponto tem o xis, a entrada, e o ípsilon, a saída, [p=0.2] e {c}domínio e imagem, escritos com colchetes. [p=0.3] Se faltar alguma, procure no canal."),
    # ler um ponto
    dict(id="s04", block="ler", text="Primeiro, os eixos. [p=0.2] No {a}eixo xis, deitado, está a hora do dia, [p=0.2] de zero a vinte e quatro. [p=0.2] No {b}eixo ípsilon, em pé, está a temperatura, em graus. [p=0.3] Cada ponto da curva diz: {c}nesta hora, fazia esta temperatura."),
    dict(id="s05", block="ler", text="Qual era a temperatura às seis da manhã? [p=0.2] {a}Saia do seis no eixo xis [p=0.2] e {b}desça até encontrar a curva. [p=0.2] Depois, {c}vá de lado até o eixo ípsilon: [p=0.2] {d}menos quatro graus."),
    # máximo e mínimo
    dict(id="s06", block="maximo", text="{a}O ponto mais alto da curva é o máximo. [p=0.3] Ele fica em {b}xis quinze, ípsilon oito. [p=0.3] Repare que ele dá {c}duas informações. [p=0.2] {d}O valor máximo é o ípsilon: oito graus. [p=0.2] {e}O momento em que ele acontece é o xis: quinze horas."),
    dict(id="s07", block="maximo", text="Com o ponto mais baixo é igual: [p=0.2] o {a}mínimo. [p=0.2] Ele fica em {b}xis seis, ípsilon menos quatro. [p=0.3] {c}A mínima do dia foi menos quatro graus, [p=0.2] {d}às seis da manhã."),
    # zeros
    dict(id="s08", block="zeros", text="E quando o termômetro marcou zero grau? [p=0.3] Zero é a altura do {a}próprio eixo xis. [p=0.2] Então procure {b}onde a curva toca o eixo xis. [p=0.3] Ela toca em {c}nove e em {d}vinte e um. [p=0.3] Fez zero grau {e}às nove da manhã e às nove da noite."),
    dict(id="s09", block="zeros", text="Esses xis em que o ípsilon vale zero se chamam {a}zeros da função. [p=0.2] Um gráfico pode ter {b}um zero, vários, [p=0.2] ou {c}nenhum, se a curva nunca encostar no eixo."),
    # crescimento
    dict(id="s10", block="cresce", text="Agora, quando esquentou e quando esfriou? [p=0.3] Leia o gráfico como se lê um texto: [p=0.2] {a}da esquerda para a direita. [p=0.3] {b}Onde a curva sobe, a função é crescente. [p=0.2] {c}Onde desce, é decrescente. [p=0.2] E {d}onde fica na horizontal, é constante."),
    dict(id="s11", block="cresce", text="Neste dia, {a}a temperatura caiu da meia-noite até as seis. [p=0.2] {b}Subiu das seis até as quinze. [p=0.2] E {c}voltou a cair das quinze até a meia-noite seguinte. [p=0.3] Crescente {d}de seis a quinze. [p=0.2] Decrescente {e}de zero a seis e de quinze a vinte e quatro."),
    # domínio e imagem
    dict(id="s12", block="dominio", text="Por fim, domínio e imagem. [p=0.2] O {a}domínio são as entradas que o gráfico usa: [p=0.2] as horas, {b}de zero a vinte e quatro. [p=0.2] Em colchetes, {c}fechado no zero e fechado no vinte e quatro."),
    dict(id="s13", block="dominio", text="A {a}imagem são as saídas que aparecem: [p=0.2] as temperaturas que o dia alcançou. [p=0.3] Vai da mínima até a máxima: [p=0.2] {b}de menos quatro a oito, [p=0.2] {c}fechado nas pontas."),
    # erro
    dict(id="s14", block="erro", text="Agora, cuidado com um erro muito comum: [p=0.2] {a}achar que abaixo do eixo a função está descendo. [p=0.3] Olhe {b}das seis às nove. [p=0.2] A temperatura está {c}negativa o tempo todo, [p=0.2] mas vai de {d}menos quatro para zero. [p=0.2] Ela está {e}subindo. [p=0.3] {f}Negativo diz onde a curva está. [p=0.2] {g}Crescente diz para onde ela vai."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho para domínio e imagem: [p=0.2] {a}a sombra do gráfico. [p=0.3] Acenda uma lanterna em cima da curva: [p=0.2] {b}a sombra no eixo xis é o domínio. [p=0.2] Acenda de lado: [p=0.2] {c}a sombra no eixo ípsilon é a imagem."),
    dict(id="s16", block="atalho", text="Funciona porque cada ponto da curva {a}projeta o seu xis no chão e o seu ípsilon na parede. [p=0.3] {b}Não compensa quando a curva termina com bolinha aberta: [p=0.2] aí aquela ponta {c}fica de fora, [p=0.2] e o colchete daquele lado é aberto, como nos intervalos."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Este gráfico mostra o saldo de uma lojinha, em mil reais, [p=0.2] nos {b}doze meses depois que ela abriu. [p=0.3] {c}Qual foi o maior saldo, e em que mês? [p=0.2] {d}Em que meses o saldo foi zero? [p=0.2] {e}Em que período ele cresceu? [p=0.2] E {f}qual é a imagem?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] O ponto mais alto é {a}xis nove, ípsilon seis. [p=0.2] O maior saldo foi {b}seis mil reais, [p=0.2] {c}no mês nove. [p=0.3] A curva toca o eixo xis {d}no mês um e no mês cinco: [p=0.2] ali o saldo foi zero."),
    dict(id="s20", block="resposta", text="Da esquerda para a direita, a curva {a}desce até o mês três [p=0.2] e {b}sobe do mês três até o mês nove. [p=0.2] Cresceu {c}de três a nove. [p=0.3] Na sombra do eixo ípsilon, {d}o mais baixo é menos quatro e o mais alto é seis. [p=0.2] Imagem: {e}de menos quatro a seis, fechado nas pontas."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}o valor é o ípsilon, o momento é o xis, [p=0.2] {b}zero é onde a curva toca o eixo xis [p=0.2] e {c}crescente se lê da esquerda para a direita."),
    dict(id="s22", block="fim", text="Na próxima aula, você {a}pratica tudo desta trilha até aqui, [p=0.2] em fórmulas, tabelas e gráficos, [p=0.2] e treina a pergunta que mais derruba: [p=0.2] {b}ela pede o xis ou o ípsilon? [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
