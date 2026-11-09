# Estudativo · FIS-OPT-002 — Reflexão e espelho plano (Física · Óptica · Reflexão e espelhos).
# Habilidade: usar a lei da reflexão, achar a imagem simétrica e a altura mínima do espelho para uma pessoa se ver inteira.
# Pré-requisitos: FIS-OPT-001 (luz em linha reta), MAT-ANG-001 (ângulos em graus). Próxima: FIS-OPT-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Alturas em centímetros: divisão com resultado decimal (MAT-FRA-017) não está em "Já ensinado".
# Atalho explicado pela semelhança com razão 1/2 (MAT-ANG-012): o espelho fica no meio do caminho entre o olho e a imagem.

TITULO = "Reflexão e espelho plano"

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
    dict(id="s01", block="gancho", text="Para se ver {a}de corpo inteiro no espelho, [p=0.2] você precisa de um espelho {b}do seu tamanho? [p=0.3] {c}Não. [p=0.2] Basta {d}metade da sua altura. [p=0.2] E {e}a distância até o espelho não muda nada."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai usar {b}a lei da reflexão, [p=0.2] achar {c}a imagem num espelho plano [p=0.2] e calcular {d}o tamanho mínimo do espelho."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a luz anda em linha reta, desenhada como um raio com seta; [p=0.2] e {c}ângulos em graus, com o ângulo reto de noventa graus. [p=0.3] Se faltar alguma, procure no canal."),
    # reflexão
    dict(id="s04", block="reflexao", text="Quando a luz bate numa superfície e {a}volta para o mesmo meio, [p=0.2] isso é {b}reflexão. [p=0.3] Numa superfície bem lisa, como o espelho, [p=0.2] {c}raios que chegam paralelos voltam paralelos. [p=0.3] {d}Numa superfície áspera, como o papel, cada raio volta para um lado. [p=0.2] É essa reflexão espalhada que deixa você ver um objeto {e}de qualquer canto da sala."),
    # a lei
    dict(id="s05", block="lei", text="Para medir a reflexão, traçamos {a}a normal: [p=0.2] uma reta {b}a noventa graus do espelho, [p=0.2] no ponto onde o raio bate."),
    dict(id="s06", block="lei", text="{a}O ângulo entre o raio que chega e a normal é o ângulo de incidência, i. [p=0.3] {b}O ângulo entre o raio que volta e a normal é o ângulo de reflexão, r. [p=0.3] A lei da reflexão diz: {c}r é igual a i. [p=0.3] E {d}os dois raios e a normal ficam no mesmo plano, como se estivessem desenhados na mesma folha."),
    dict(id="s07", block="lei", text="Cuidado com o erro mais comum: [p=0.2] {a}medir o ângulo a partir do espelho. [p=0.3] Se o raio faz {b}trinta graus com o espelho, [p=0.2] o ângulo de incidência é {c}noventa menos trinta: sessenta graus. [p=0.3] {d}Os ângulos da lei são sempre medidos a partir da normal."),
    # imagem
    dict(id="s08", block="imagem", text="Agora, por que a imagem parece estar {a}atrás do espelho? [p=0.3] {b}Os raios de um ponto batem no espelho e voltam se abrindo. [p=0.3] O olho não sabe que a luz refletiu: [p=0.2] {c}ele segue os raios para trás, em linha reta. [p=0.3] {d}Esses prolongamentos se encontram atrás do espelho, [p=0.2] e é ali que você vê a imagem."),
    dict(id="s09", block="imagem", text="Nenhuma luz passa atrás do espelho. [p=0.2] Por isso essa imagem se chama {a}virtual: [p=0.2] ela é formada pelos prolongamentos dos raios, e não pelos raios de verdade."),
    dict(id="s10", block="imagem", text="No espelho plano, a imagem é {a}simétrica: [p=0.2] {b}fica atrás do espelho, à mesma distância que o objeto está na frente, [p=0.2] {c}tem o mesmo tamanho [p=0.2] e {d}fica de pé, o que a Física chama de imagem direita. [p=0.3] Mas ela troca {e}o lado direito com o esquerdo. [p=0.2] Por isso {f}a palavra ambulância vem escrita ao contrário na frente do carro: [p=0.2] assim, o motorista da frente lê certo no retrovisor."),
    dict(id="s11", block="imagem", text="Se você está a {a}dois metros do espelho, [p=0.2] sua imagem está {b}dois metros atrás dele. [p=0.3] Entre você e a sua imagem, {c}são quatro metros."),
    # altura mínima
    dict(id="s12", block="altura", text="Voltando ao gancho. [p=0.2] {a}Uma pessoa de cento e oitenta centímetros, com os olhos a cento e setenta do chão. [p=0.3] Para ela ver o próprio pé, {b}a luz do pé bate no espelho e sobe até o olho. [p=0.3] Para ver o topo da cabeça, {c}a luz da cabeça bate no espelho e desce até o olho."),
    dict(id="s13", block="altura", text="O espelho só precisa existir {a}entre esses dois pontos. [p=0.3] E a distância entre eles é {b}metade da altura da pessoa: [p=0.2] {c}cento e oitenta dividido por dois, noventa centímetros. [p=0.3] {d}A borda de baixo fica na metade da altura dos olhos: [p=0.2] {e}cento e setenta dividido por dois, oitenta e cinco centímetros do chão."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova, e o motivo dele. [p=0.3] {a}Olhe a pessoa e a imagem dela. [p=0.2] {b}O espelho fica bem no meio do caminho entre o olho e a imagem. [p=0.3] {c}Os raios que vão do olho até a imagem formam um triângulo, [p=0.2] e o espelho corta esse triângulo {d}na metade da distância."),
    dict(id="s15", block="atalho", text="Pela semelhança, {a}o pedaço cortado tem metade da altura. [p=0.3] Afaste-se do espelho, e {b}a imagem se afasta junto: [p=0.2] {c}o espelho continua no meio, e a metade não muda. [p=0.3] Então: {d}altura mínima é a altura da pessoa dividida por dois. [p=0.2] {e}Para a borda de baixo, use metade da altura dos olhos."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Uma pessoa tem {a}cento e sessenta centímetros [p=0.2] e {b}os olhos a cento e cinquenta do chão. [p=0.3] {c}Qual a altura mínima do espelho para ela se ver inteira? [p=0.2] E {d}a que altura do chão fica a borda de baixo?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] A altura mínima é {a}metade da altura da pessoa: [p=0.2] {b}cento e sessenta dividido por dois, oitenta centímetros. [p=0.3] A borda de baixo fica na {c}metade da altura dos olhos: [p=0.2] {d}cento e cinquenta dividido por dois, setenta e cinco centímetros do chão. [p=0.3] {e}E a distância até o espelho não entrou na conta."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}o ângulo de reflexão é igual ao de incidência, medidos da normal; [p=0.2] {b}a imagem do espelho plano é virtual, simétrica, do mesmo tamanho; [p=0.2] e {c}para se ver inteiro, basta um espelho com metade da sua altura."),
    dict(id="s20", block="fim", text="Na próxima aula, o espelho {a}fica curvo: [p=0.2] {b}o espelho de maquiagem, que aumenta, [p=0.2] e {c}o retrovisor, que mostra mais da rua. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
