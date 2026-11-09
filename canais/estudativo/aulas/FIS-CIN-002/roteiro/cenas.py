# Estudativo · FIS-CIN-002 — Vetores: somar e subtrair (Física · Cinemática · Grandezas e vetores).
# Habilidade: achar o vetor resultante de dois vetores no mesmo sentido, em sentidos opostos e perpendiculares, como no barco que atravessa o rio.
# Pré-requisitos: FIS-CIN-001 (vetor), MAT-NUM-016 (inteiros), MAT-ANG-016 (ternos pitagóricos). Próxima: FIS-CIN-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Regra de desenho: ponta de um com o começo do outro (método do polígono, sem o nome).

TITULO = "Vetores: somar e subtrair"

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
    dict(id="s01", block="gancho", text="{a}Um barco atravessa um rio a quatro metros por segundo, [p=0.2] e {b}a correnteza empurra de lado, a três metros por segundo. [p=0.3] Para quem está na margem, com que velocidade ele anda? [p=0.3] {c}Sete? [p=0.2] {d}Um? [p=0.3] {e}Nem sete nem um: cinco."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai juntar dois vetores {b}no mesmo sentido, [p=0.2] {c}em sentidos opostos [p=0.2] e {d}em ângulo reto, como no barco."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o vetor, a seta que tem módulo, direção e sentido; [p=0.2] e {c}Pitágoras no triângulo retângulo, como o três, quatro, cinco. [p=0.3] Se faltar alguma, procure no canal."),
    # resultante
    dict(id="s04", block="resultante", text="Quando dois vetores agem juntos, eles podem ser trocados por {a}um só, [p=0.2] que faz o mesmo efeito. [p=0.2] Esse vetor se chama {b}resultante. [p=0.3] E existe um desenho que serve para todos os casos: [p=0.2] {c}ponha o começo do segundo vetor na ponta do primeiro. [p=0.2] A resultante vai {d}do começo do primeiro até a ponta do segundo."),
    # mesmo sentido e opostos
    dict(id="s05", block="fila", text="Primeiro caso: {a}mesmo sentido. [p=0.2] Uma balsa anda a {b}dois metros por segundo, [p=0.2] e você caminha no convés a {c}um metro por segundo, para a frente. [p=0.3] Ponta com começo, as setas ficam {d}em fila. [p=0.2] {e}A resultante é a soma: três metros por segundo."),
    dict(id="s06", block="fila", text="Segundo caso: {a}sentidos opostos. [p=0.2] Agora você caminha {b}para trás no convés, a um metro por segundo. [p=0.3] {c}A sua seta volta por cima da outra. [p=0.2] A resultante é {d}a diferença: dois menos um, um metro por segundo, [p=0.2] {e}no sentido do maior, o da balsa."),
    dict(id="s07", block="fila", text="Dá para fazer isso com {a}sinais, como nos números inteiros. [p=0.2] {b}Para a direita é mais; [p=0.1] {c}para a esquerda é menos. [p=0.3] {d}Mais dois, somado com menos um, dá mais um. [p=0.2] O sinal da resposta diz o sentido."),
    # ângulo reto
    dict(id="s08", block="reto", text="Terceiro caso: {a}em ângulo reto, [p=0.2] o do barco. [p=0.2] {b}O barco aponta para a outra margem a quatro metros por segundo. [p=0.2] {c}A correnteza empurra rio abaixo a três. [p=0.3] Ponta com começo: {d}as duas setas formam os catetos de um triângulo retângulo. [p=0.2] E a resultante fecha o triângulo: {e}é a hipotenusa."),
    dict(id="s09", block="reto", text="Pitágoras: [p=0.1] {a}a hipotenusa ao quadrado é a soma dos quadrados dos catetos. [p=0.3] {b}Três ao quadrado, nove. [p=0.1] {c}Quatro ao quadrado, dezesseis. [p=0.2] {d}Nove mais dezesseis, vinte e cinco. [p=0.2] {e}A raiz de vinte e cinco é cinco. [p=0.3] {f}O barco anda a cinco metros por segundo, na diagonal, [p=0.2] e chega à outra margem mais abaixo do ponto em frente."),
    # subtrair
    dict(id="s10", block="subtrair", text="E subtrair um vetor? [p=0.2] {a}É somar o oposto: [p=0.2] {b}a mesma seta, com o sentido virado. [p=0.3] Uma bola vai {c}até uma parede a cinco metros por segundo [p=0.2] e {d}volta a cinco. [p=0.3] Indo para a parede é mais; [p=0.1] voltando, é menos. [p=0.2] Quanto a velocidade mudou? [p=0.2] Mudança é {e}final menos inicial: [p=0.2] menos cinco, somado com o oposto de mais cinco, [p=0.1] que é menos cinco: [p=0.2] {f}menos dez. [p=0.3] {g}Mudou dez metros por segundo, e não zero."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: {a}somar os módulos sempre. [p=0.3] No barco, {b}quatro mais três dá sete. [p=0.2] Mas sete só acontece com {c}as setas em fila, no mesmo sentido. [p=0.3] {d}A resultante fica sempre entre a diferença e a soma: [p=0.2] {e}entre um e sete. [p=0.2] {f}Em ângulo reto, só Pitágoras dá o valor certo: cinco."),
    # atalho
    dict(id="s12", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}decore os ternos pitagóricos. [p=0.2] {b}Três, quatro, cinco. [p=0.1] {c}Seis, oito, dez. [p=0.1] {d}Cinco, doze, treze. [p=0.3] Vetores de seis e de oito em ângulo reto? [p=0.2] {e}Dez, sem conta nenhuma."),
    dict(id="s13", block="atalho", text="Funciona porque {a}o terno é Pitágoras já feito: [p=0.2] seis ao quadrado mais oito ao quadrado dá cem, e a raiz de cem é dez. [p=0.3] {b}Não compensa quando os números não formam um terno, como vetores de um e de dois. [p=0.2] Aí, faça Pitágoras: {c}a resultante é raiz de cinco."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Um drone voa {a}para o norte a doze metros por segundo, [p=0.2] e o vento o empurra {b}para o leste a cinco. [p=0.3] {c}Qual é a velocidade resultante? [p=0.3] E se o vento empurrasse {d}para o sul?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] Norte e leste fazem {a}ângulo reto. [p=0.2] {b}Cinco, doze, treze: [p=0.2] {c}treze metros por segundo. [p=0.3] Pela conta: [p=0.1] {d}vinte e cinco mais cento e quarenta e quatro, cento e sessenta e nove, [p=0.2] e {e}a raiz de cento e sessenta e nove é treze."),
    dict(id="s17", block="resposta", text="Com o vento para o sul, {a}os sentidos são opostos. [p=0.2] {b}Doze menos cinco: [p=0.2] {c}sete metros por segundo, [p=0.1] para o norte, o sentido do maior."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}mesmo sentido, soma; [p=0.2] {b}sentidos opostos, subtrai e fica o sentido do maior; [p=0.2] {c}ângulo reto, Pitágoras."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai ver que {a}estar parado ou em movimento depende de quem olha, [p=0.2] e separar {b}a distância que você anda do deslocamento. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
