# Estudativo · FIS-CIN-015 — Lançamento horizontal (Física · Cinemática · Queda livre e lançamentos).
# Habilidade: separar o movimento em queda na vertical e velocidade constante na horizontal para achar tempo de voo e alcance.
# Pré-requisitos: FIS-CIN-013 (queda livre), FIS-CIN-005 (MU). Próxima: FIS-CIN-003 (decompor vetor).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Vetores (FIS-CIN-002) e Pitágoras não estão em "Já ensinado": a aula fala em "movimento de lado" e "para baixo", sem somar
# velocidades; a velocidade de chegada fica como assunto de outra aula.
# Contas: penhasco 20 m: 20 = 5t² → t = 2 s; alcance 15·2 = 30 m. Estroboscópio a cada 1 s: x = 0, 15, 30; quedas 0, 5, 20.
# Avião: 500 = 5t² → t = 10 s; 100·10 = 1000 m. Dobro da velocidade: 30·2 = 60 m. Questão: 1,25 = 5t² → t² = 0,25 → t = 0,5 s; 2·0,5 = 1 m.

TITULO = "Lançamento horizontal"

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
    dict(id="s01", block="gancho", text="Na beira de uma mesa, {a}uma bola é empurrada para a frente [p=0.2] e {b}outra cai solta, [p=0.1] no mesmo instante. [p=0.3] {c}Qual chega primeiro ao chão? [p=0.3] {d}Chegam juntas. [p=0.2] Andar para a frente não muda nada na queda."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai achar {b}quanto tempo um objeto lançado na horizontal fica no ar [p=0.2] e {c}a que distância ele cai."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a queda livre, altura igual a cinco vezes o tempo ao quadrado; [p=0.2] e {c}o movimento uniforme, distância igual a velocidade vezes tempo. [p=0.3] Se faltar alguma, procure no canal."),
    # dois movimentos
    dict(id="s04", block="dois", text="Lançamento horizontal é quando o objeto {a}sai na horizontal, [p=0.2] de uma altura, [p=0.1] como a bola que rola para fora da mesa ou a caixa solta de um avião. [p=0.3] A ideia da aula é ver {b}dois movimentos ao mesmo tempo, [p=0.2] e cada um cuida da sua vida."),
    dict(id="s05", block="dois", text="{a}Na horizontal, nada empurra nem freia a bola, se o ar for desprezado. [p=0.2] Então a velocidade para a frente {b}não muda: [p=0.2] é {c}movimento uniforme. [p=0.3] {d}Para baixo, a bola faz {e}a mesma queda livre da bola solta."),
    dict(id="s06", block="dois", text="Veja as fotos da bola a cada segundo, lançada a quinze metros por segundo. [p=0.2] {a}Na horizontal, ela anda quinze metros por segundo, sempre igual. [p=0.3] {b}Para baixo, cai cinco metros no primeiro segundo e vinte no total depois de dois, como na queda livre. [p=0.3] Juntando os dois, o caminho vira {c}uma curva, uma parábola."),
    # método
    dict(id="s07", block="metodo", text="Daí sai o método, em dois passos. [p=0.2] {a}Primeiro, o tempo, pela altura: [p=0.2] {b}agá igual a cinco tê ao quadrado. [p=0.3] {c}Depois, o alcance, pela horizontal: [p=0.2] {d}a distância é a velocidade de lançamento vezes esse tempo. [p=0.3] Alcance é {e}a distância, no chão, entre o ponto de lançamento e onde o objeto cai."),
    dict(id="s08", block="metodo", text="Uma pedra é lançada na horizontal do alto de um penhasco de {a}vinte metros, a {b}quinze metros por segundo. [p=0.3] {c}Tempo: vinte igual a cinco tê ao quadrado, [p=0.1] tê ao quadrado é quatro, [p=0.1] {d}tê é dois segundos. [p=0.3] {e}Alcance: quinze vezes dois, [p=0.1] {f}trinta metros."),
    # erro
    dict(id="s09", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}soltar a carga em cima do alvo. [p=0.3] {b}Um avião voa a cem metros por segundo, a quinhentos metros de altura, [p=0.2] e solta uma caixa {c}bem em cima de uma clareira."),
    dict(id="s10", block="erro", text="{a}A caixa leva dez segundos para cair, [p=0.2] porque quinhentos dividido por cinco é cem, e a raiz de cem é dez. [p=0.3] Nesse tempo, ela continua andando para a frente com o avião: [p=0.2] {b}cem vezes dez, mil metros. [p=0.3] {c}Cai um quilômetro depois da clareira. [p=0.2] {d}O certo é soltar um quilômetro antes."),
    # atalho
    dict(id="s11", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}a altura manda no tempo. [p=0.3] O tempo no ar é {b}o da queda livre da mesma altura, [p=0.2] não importa a velocidade para a frente. [p=0.3] Por isso, {c}com o dobro da velocidade, o tempo é o mesmo [p=0.2] e {d}o alcance dobra: [p=0.1] a pedra do penhasco, a trinta metros por segundo, cairia a sessenta metros."),
    dict(id="s12", block="atalho", text="Funciona porque {a}o que acontece na horizontal não muda a queda. [p=0.3] {b}Não compensa quando a questão pede a velocidade com que o objeto chega ao chão: [p=0.2] aí é preciso juntar as duas velocidades, [p=0.1] {c}assunto de outra aula."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] {a}Uma bola rola sobre uma mesa de {b}um metro e vinte e cinco centímetros de altura [p=0.2] e sai pela borda a {c}dois metros por segundo. [p=0.3] {d}A que distância da mesa ela toca o chão?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] Primeiro, o tempo: {a}um vírgula vinte e cinco igual a cinco tê ao quadrado. [p=0.3] {b}Dividindo por cinco, tê ao quadrado é zero vírgula vinte e cinco, [p=0.2] e {c}tê é zero vírgula cinco segundo: [p=0.1] meio segundo."),
    dict(id="s16", block="resposta", text="{a}Depois, o alcance: dois metros por segundo vezes meio segundo, [p=0.2] {b}um metro. [p=0.3] A bola toca o chão a um metro do pé da mesa."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}na vertical, queda livre, e ela dá o tempo; [p=0.2] {b}na horizontal, velocidade constante, e ela dá o alcance."),
    dict(id="s18", block="fim", text="Na próxima aula, você vai aprender a {a}separar uma seta, como a velocidade, em uma parte horizontal e uma vertical, [p=0.2] {b}com seno e cosseno. [p=0.3] É o que falta para o lançamento inclinado. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
