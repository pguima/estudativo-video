# Estudativo · FIS-CIN-009 — Torricelli e distância de frenagem (Física · Cinemática · Movimento uniforme e variado).
# Habilidade: usar v² = v0² + 2·a·Δs quando o tempo não aparece e calcular a distância de parada com o tempo de reação,
# lembrando que dobrar a velocidade quadruplica a frenagem.
# Pré-requisitos: FIS-CIN-008 (função da posição), MAT-RAZ-010 (proporcional ao quadrado), MAT-POT-007 (raiz), MAT-EQU-011 (isolar). Próxima: FIS-CIN-010.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. "freada" = módulo da aceleração na frenagem. Tempo de reação típico: perto de 1 s.

TITULO = "Torricelli e distância de frenagem"

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
    dict(id="s01", block="gancho", text="{a}Um carro a {b}dez metros por segundo freia e para em {c}dez metros. [p=0.3] Com o dobro da velocidade, {d}vinte metros por segundo, [p=0.2] e a mesma freada, de quanto espaço ele precisa? [p=0.3] {e}Vinte metros? [p=0.2] {f}Não: quarenta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai resolver o movimento com aceleração {b}sem saber o tempo, [p=0.2] e calcular {c}a distância que um carro precisa para parar."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}as funções do eme u vê, a da velocidade e a da posição; [p=0.2] {c}a ideia de que dobrar o lado de um quadrado quadruplica a área; [p=0.2] e {d}a raiz quadrada. [p=0.3] Se faltar alguma, procure no canal."),
    # Torricelli
    dict(id="s04", block="torricelli", text="Nas fórmulas do eme u vê, {a}o tempo aparece em todas. [p=0.2] Mas muita questão {b}não dá o tempo nem pergunta por ele. [p=0.3] Para esses casos existe a equação de {c}Torricelli: [p=0.2] {d}vê ao quadrado igual a vê zero ao quadrado mais dois á delta esse."),
    dict(id="s05", block="torricelli", text="{a}Vê é a velocidade final, [p=0.1] {b}vê zero, a inicial, [p=0.1] em metro por segundo. [p=0.2] {c}Á é a aceleração, em metro por segundo ao quadrado. [p=0.2] {d}Delta esse é o deslocamento, em metro. [p=0.3] {e}Ela sai das outras duas, quando se tira o tê da conta. [p=0.2] {f}Use quando o tempo não aparece."),
    dict(id="s06", block="torricelli", text="Um carro está a {a}dez metros por segundo e acelera {b}dois metros por segundo ao quadrado ao longo de {c}vinte e quatro metros. [p=0.3] Qual é a velocidade no fim? [p=0.2] {d}Dez ao quadrado, cem. [p=0.1] {e}Dois vezes dois vezes vinte e quatro, noventa e seis. [p=0.2] {f}Vê ao quadrado é cento e noventa e seis, [p=0.2] e {g}a raiz é catorze metros por segundo."),
    # frenagem
    dict(id="s07", block="frenagem", text="Na freada, {a}o carro para: a velocidade final é zero. [p=0.2] E {b}a aceleração é negativa: contrária à velocidade, que aqui é positiva. [p=0.3] O carro a {c}vinte metros por segundo, freando com {d}menos cinco metros por segundo ao quadrado: [p=0.2] {e}zero igual a quatrocentos menos dez delta esse. [p=0.2] {f}Dez delta esse igual a quatrocentos: [p=0.1] {g}quarenta metros."),
    dict(id="s08", block="frenagem", text="{a}Isole o delta esse com a velocidade final zero: [p=0.2] {b}a distância de frenagem é vê zero ao quadrado dividido pelo dobro do módulo da aceleração. [p=0.3] {c}A velocidade está ao quadrado. [p=0.2] Como no lado do quadrado: [p=0.1] {d}dobrou a velocidade, a frenagem fica quatro vezes maior. [p=0.2] {e}Triplicou, nove vezes."),
    # reação
    dict(id="s09", block="reacao", text="Mas o carro não começa a frear no instante em que o motorista vê o perigo. [p=0.2] Existe {a}o tempo de reação, [p=0.1] em geral perto de {b}um segundo. [p=0.3] Nesse tempo, {c}o pé ainda está indo para o freio, e o carro segue com a mesma velocidade: [p=0.2] {d}é movimento uniforme. [p=0.2] {e}Distância de reação: velocidade vezes tempo."),
    dict(id="s10", block="reacao", text="{a}Distância de parada é a reação mais a frenagem. [p=0.3] A vinte metros por segundo, com um segundo de reação: [p=0.2] {b}vinte metros de reação, [p=0.1] {c}mais quarenta de frenagem: [p=0.2] {d}sessenta metros para parar."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: {a}esquecer o tempo de reação. [p=0.3] Quem só faz Torricelli responde {b}quarenta metros, [p=0.2] e o carro {c}para vinte metros além do que a conta previa."),
    # atalho
    dict(id="s12", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}multiplicou a velocidade por um número, a frenagem fica multiplicada por esse número ao quadrado. [p=0.3] {b}Dez metros por segundo, dez metros de frenagem. [p=0.2] {c}Vinte, quarenta. [p=0.1] {d}Trinta, noventa. [p=0.2] Sem refazer a conta."),
    dict(id="s13", block="atalho", text="Funciona porque {a}a velocidade entra ao quadrado na frenagem. [p=0.3] Mas {b}não vale para a distância de parada inteira: [p=0.2] {c}a reação só dobra quando a velocidade dobra. [p=0.2] {d}E só vale com a mesma freada: [p=0.1] na pista molhada, a conta muda."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Um carro a {a}quinze metros por segundo precisa de {b}quinze metros para frear. [p=0.3] O motorista tem {c}um segundo de reação. [p=0.3] {d}Qual é a distância de parada? [p=0.2] {e}E a trinta metros por segundo, com a mesma freada?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] A quinze: {a}quinze metros de reação, [p=0.1] {b}mais quinze de frenagem: [p=0.2] {c}trinta metros."),
    dict(id="s17", block="resposta", text="A trinta, a velocidade dobrou. [p=0.2] {a}Reação: trinta vezes um, trinta metros. [p=0.2] {b}Frenagem: quatro vezes quinze, sessenta. [p=0.2] {c}Parada: noventa metros. [p=0.3] {d}A velocidade dobrou, e a distância de parada triplicou."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}sem o tempo, Torricelli; [p=0.2] {b}parada é reação mais frenagem; [p=0.2] {c}dobrou a velocidade, a frenagem quadruplica."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai {a}praticar com questões de vetores e movimentos [p=0.2] e {b}escolher a equação certa para cada uma. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
