# Estudativo · FIS-DIN-010 — Força centrípeta (Física · Dinâmica · Força centrípeta).
# Habilidade: calcular a aceleração centrípeta v²/R e apontar qual força faz o papel de centrípeta em cada situação.
# Pré-requisitos: FIS-DIN-002 (F = m·a), FIS-CIN-019 (ω e v = ω·R). Próxima: FIS-DIN-011.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Peso, normal, tração e atrito (FIS-DIN-004, 005, 007) NÃO estão em "Já ensinado" desta aula: as forças que fazem o papel de
# centrípeta são ditas pelo que fazem (o fio puxa, o chão segura o pneu, a Terra atrai a Lua) e o cálculo de cada uma fica
# para as aulas seguintes. Proporcional ao quadrado: MAT-RAZ-010. a = ω²·R sai de v = ω·R.

TITULO = "Força centrípeta"

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
    dict(id="s01", block="gancho", text="{a}Numa curva fechada, você sente o corpo ser jogado para fora da curva. [p=0.3] {b}Mas não existe nenhuma força empurrando você para fora. [p=0.3] {c}Existe uma puxando para dentro."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular {b}a aceleração centrípeta [p=0.2] e apontar {c}qual força faz esse papel em cada situação."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}força resultante igual a massa vezes aceleração; [p=0.2] e {c}a velocidade linear no círculo, vê igual a ômega vezes erre. [p=0.3] Se faltar alguma, procure no canal."),
    # aceleração na curva
    dict(id="s04", block="curva", text="{a}Um carro faz uma curva sempre a sessenta quilômetros por hora. [p=0.2] {b}O velocímetro não muda. [p=0.3] Mas a velocidade é um vetor, [p=0.2] e {c}a direção dela muda o tempo todo. [p=0.3] {d}Mudou a velocidade, tem aceleração."),
    dict(id="s05", block="curva", text="{a}Essa aceleração aponta para o centro da curva. [p=0.2] Por isso se chama {b}centrípeta, [p=0.1] que quer dizer {c}que busca o centro. [p=0.3] Ela não muda o valor da velocidade: [p=0.2] {d}só vira a direção."),
    # fórmula
    dict(id="s06", block="formula", text="O valor dela é {a}vê ao quadrado dividido por erre. [p=0.3] {b}Vê é a velocidade, em metros por segundo. [p=0.2] {c}Erre é o raio da curva, em metros. [p=0.3] Confira pela unidade: {d}metro ao quadrado por segundo ao quadrado, dividido por metro: [p=0.2] {e}metro por segundo ao quadrado. [p=0.2] É mesmo uma aceleração."),
    dict(id="s07", block="formula", text="Se a questão der {a}a velocidade angular, ômega, [p=0.2] troque vê por ômega vezes erre: [p=0.2] {b}a aceleração centrípeta fica ômega ao quadrado vezes erre. [p=0.3] {c}Um cavalinho de carrossel, com ômega de zero vírgula cinco radiano por segundo e raio de quatro metros: [p=0.2] {d}zero vírgula vinte e cinco vezes quatro, um metro por segundo ao quadrado."),
    dict(id="s08", block="formula", text="E a força? [p=0.2] Segunda lei: {a}efe centrípeta é eme vezes vê ao quadrado, dividido por erre. [p=0.3] {b}Um carro de mil quilogramas, a vinte metros por segundo, [p=0.2] numa curva de {c}cinquenta metros de raio. [p=0.3] {d}Quatrocentos dividido por cinquenta: oito metros por segundo ao quadrado. [p=0.2] {e}Vezes mil: oito mil newtons."),
    # quem faz o papel
    dict(id="s09", block="papel", text="{a}Força centrípeta não é uma força nova. [p=0.2] {b}É o nome do papel: a resultante que aponta para o centro. [p=0.3] {c}Alguma força de verdade tem que fazer esse papel."),
    dict(id="s10", block="papel", text="{a}Uma pedra girando presa num fio: [p=0.2] {b}quem puxa para o centro é o fio. [p=0.3] {c}O carro na curva: [p=0.1] {d}é o chão, que segura o pneu de lado, [p=0.2] o atrito, assunto de outra aula. [p=0.3] {e}A Lua em volta da Terra: [p=0.1] {f}é a atração da Terra, assunto da gravitação."),
    dict(id="s11", block="papel", text="{a}E se o fio da pedra arrebenta? [p=0.3] Sem força para o centro, vale a primeira lei: [p=0.2] {b}a pedra segue reto, pela reta que só encosta no círculo naquele ponto, [p=0.2] {c}e não para fora, como muita gente desenha."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}desenhar uma força para fora, a tal centrífuga. [p=0.3] Na curva, {b}seu corpo tenta seguir reto, por inércia, [p=0.2] e {c}o carro vira para dentro. [p=0.3] {d}A porta é que vem até você, [p=0.2] e empurra você {e}para o centro."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}a velocidade está ao quadrado. [p=0.3] {b}Dobrou a velocidade, a força fica quatro vezes maior. [p=0.2] {c}Triplicou, nove vezes. [p=0.3] {d}Dobrou o raio, com a mesma velocidade, a força cai pela metade."),
    dict(id="s14", block="atalho", text="Funciona porque {a}a força é proporcional ao quadrado da velocidade [p=0.2] e inversamente proporcional ao raio. [p=0.3] {b}Não compensa quando massa, velocidade e raio mudam juntos: [p=0.2] aí, {c}faça a conta inteira."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Uma pedra de meio quilograma gira presa num fio de dois metros, [p=0.2] a {b}quatro metros por segundo. [p=0.3] {c}Qual é a força do fio? [p=0.2] E {d}se a velocidade dobrar?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Quem faz a centrípeta é {a}o fio. [p=0.2] {b}Vê ao quadrado: dezesseis. [p=0.1] {c}Dividido por dois: oito metros por segundo ao quadrado. [p=0.2] {d}Vezes meio quilograma: quatro newtons."),
    dict(id="s18", block="resposta", text="Velocidade dobrada? [p=0.2] Pelo atalho, {a}quatro vezes mais: [p=0.1] {b}dezesseis newtons. [p=0.3] Confira: {c}oito ao quadrado é sessenta e quatro, [p=0.1] dividido por dois, trinta e dois, [p=0.1] vezes meio, dezesseis. [p=0.2] Bateu."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}em toda curva há aceleração para o centro, vê ao quadrado sobre erre; [p=0.2] {b}a força centrípeta é a resultante para o centro; [p=0.2] e {c}sempre alguma força de verdade faz esse papel."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai descobrir {a}a velocidade máxima de uma curva, [p=0.2] {b}com chão seco ou molhado, [p=0.2] e por que {c}as pistas de corrida são inclinadas. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
