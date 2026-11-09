# Estudativo · FIS-OND-010 — Espectro eletromagnético em ordem (Física · Ondas e Som · Espectro eletromagnético).
# Habilidade: ordenar as ondas do rádio ao raio gama por frequência e comprimento, usar c = λ·f e dizer quais radiações são ionizantes.
# Pré-requisitos: FIS-OND-002 (v = λ·f), MAT-POT-013 (contas em notação científica), QUI-ATO-004 (íon). Próxima: FIS-OND-011.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. FIS-OPT e FIS-OND-003 a 009 NÃO estão em "Já ensinado" desta aula: c é apresentado aqui.
# Ionizante: o ultravioleta de frequência mais alta, raios X e gama (rádio, micro-ondas, infravermelho e visível não ionizam).
# Frase para a ordem R M I V U X G inventada para a aula. FM 100 MHz → 3 m; AM 1.000 kHz → 300 m; X de 10⁻¹⁰ m → 3 × 10¹⁸ Hz.

TITULO = "Espectro eletromagnético em ordem"

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
    dict(id="s01", block="gancho", text="{a}O rádio do carro, [p=0.1] {b}o forno de micro-ondas, [p=0.1] {c}a luz da lâmpada [p=0.1] e {d}o raio X do hospital. [p=0.3] Parecem coisas muito diferentes, [p=0.2] mas {e}são o mesmo tipo de onda."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai pôr essas ondas em ordem, [p=0.2] usar {b}cê igual a lambda vezes efe [p=0.1] e dizer {c}quais delas arrancam elétrons dos átomos."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}a equação da onda, vê igual a lambda vezes efe; [p=0.2] {c}contas em notação científica; [p=0.2] e {d}que um átomo que perde elétrons vira um íon. [p=0.3] Se faltar alguma, procure no canal."),
    # a velocidade da luz
    dict(id="s04", block="luz", text="Você já viu que {a}a onda eletromagnética anda até no vácuo. [p=0.2] É assim que {b}a luz do Sol chega até nós. [p=0.3] Do que ela é feita é assunto do eletromagnetismo. [p=0.2] Aqui, importa uma coisa: {c}no vácuo, todas andam com a mesma velocidade."),
    dict(id="s05", block="luz", text="Essa é {a}a velocidade da luz, letra cê: [p=0.2] {b}trezentos mil quilômetros por segundo, [p=0.1] {c}três vezes dez elevado a oito metros por segundo. [p=0.3] {d}No ar, é quase a mesma."),
    dict(id="s06", block="luz", text="Então, a equação da onda vira {a}cê igual a lambda vezes efe. [p=0.3] Como cê é fixo, {b}quando a frequência sobe, o lambda desce, na mesma proporção. [p=0.2] {c}Frequência dez vezes maior, lambda dez vezes menor."),
    # a ordem
    dict(id="s07", block="ordem", text="Em ordem de frequência, da menor para a maior: [p=0.2] {a}ondas de rádio, [p=0.1] {b}micro-ondas, [p=0.1] {c}infravermelho, [p=0.1] {d}luz visível, [p=0.1] {e}ultravioleta, [p=0.1] {f}raios X [p=0.1] e {g}raios gama. [p=0.3] {h}O lambda vai ao contrário: [p=0.1] o rádio tem as ondas mais compridas, [p=0.1] e o gama, as mais curtas."),
    dict(id="s08", block="ordem", text="A luz visível é {a}uma faixa estreita no meio. [p=0.2] {b}Vai do vermelho, de frequência menor, [p=0.1] {c}ao violeta, de frequência maior. [p=0.3] {d}Infra quer dizer abaixo: o infravermelho fica abaixo do vermelho. [p=0.2] {e}Ultra quer dizer além: o ultravioleta fica além do violeta."),
    dict(id="s09", block="ordem", text="Uma rádio FM transmite em {a}cem megahertz. [p=0.2] Cem megahertz são cem milhões de hertz: {b}um vezes dez elevado a oito. [p=0.3] {c}Lambda é cê dividido por efe: [p=0.1] três vezes dez elevado a oito, dividido por um vezes dez elevado a oito. [p=0.2] {d}Três metros."),
    # ionizante
    dict(id="s10", block="ioniza", text="Agora, o risco. [p=0.2] {a}Quanto maior a frequência, mais energia a radiação entrega a cada átomo que ela atinge. [p=0.2] Energia é assunto de outra aula: aqui, pense num empurrão mais forte. [p=0.3] {b}No ultravioleta de frequência mais alta, essa energia já basta para arrancar elétrons dos átomos. [p=0.2] {c}O átomo vira um íon. [p=0.3] Essas radiações se chamam {d}ionizantes, [p=0.1] e podem danificar as células."),
    dict(id="s11", block="ioniza", text="{a}Rádio, micro-ondas, infravermelho e luz visível não ionizam. [p=0.2] {b}O ultravioleta mais forte, os raios X e os raios gama ionizam. [p=0.3] Os usos e os cuidados com cada uma {c}são o assunto da próxima aula."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: {a}achar que o raio X é mais rápido que a onda de rádio, [p=0.1] porque é mais forte. [p=0.3] {b}No vácuo, todas andam a três vezes dez elevado a oito metros por segundo. [p=0.2] {c}O que muda de uma para outra é a frequência e o lambda, [p=0.1] nunca a velocidade."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] a ordem cabe numa frase. [p=0.2] {a}Rita Mandou Isabel Ver Uma Xícara Grande. [p=0.3] {b}Erre, eme, i, vê, u, xis, gê: [p=0.1] rádio, micro-ondas, infravermelho, visível, ultravioleta, xis e gama. [p=0.3] {c}Da esquerda para a direita, a frequência e o risco sobem, [p=0.1] e o lambda desce. [p=0.2] Funciona porque a ordem é sempre a mesma, do lambda mais comprido ao mais curto. [p=0.3] {d}A frase não ajuda dentro da luz visível: [p=0.1] aí, lembre que o vermelho tem a menor frequência, e o violeta, a maior."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Uma rádio AM transmite em um vezes dez elevado a seis hertz. [p=0.2] {b}Um aparelho de raio X emite com lambda de um vezes dez elevado a menos dez metros. [p=0.3] {c}Qual é o lambda da rádio, e qual é a frequência do raio X? [p=0.2] {d}E qual dos dois é ionizante?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Rádio: três vezes dez elevado a oito, dividido por dez elevado a seis. [p=0.1] {b}Oito menos seis, dois: três vezes dez elevado a dois, [p=0.1] {c}trezentos metros."),
    dict(id="s17", block="resposta", text="{a}Raio X: três vezes dez elevado a oito, dividido por dez elevado a menos dez. [p=0.2] {b}Dividir por dez elevado a menos dez é multiplicar por dez elevado a dez: [p=0.1] oito mais dez, dezoito. [p=0.1] {c}Três vezes dez elevado a dezoito hertz. [p=0.3] {d}Ionizante é o raio X: [p=0.1] {e}frequência muito maior, lambda muito menor."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}no vácuo, todas andam a cê; [p=0.1] {b}cê igual a lambda vezes efe; [p=0.1] {c}do rádio ao gama, a frequência sobe e o lambda desce; [p=0.1] {d}do ultravioleta mais forte em diante, elas ionizam."),
    dict(id="s19", block="fim", text="Na próxima aula, cada faixa ganha o seu uso: [p=0.2] {a}celular, forno, controle remoto, protetor solar e radiografia. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
