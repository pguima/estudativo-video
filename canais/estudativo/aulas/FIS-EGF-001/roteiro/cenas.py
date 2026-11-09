# Estudativo · FIS-EGF-001 — Torque e alavancas (Física · Equilíbrio, Gravitação e Fluidos · Equilíbrio, torque e gravitação).
# Habilidade: calcular o torque M = F·d, equilibrar gangorras e alavancas e dizer as duas condições de equilíbrio de um corpo.
# Pré-requisitos: FIS-DIN-001 (força resultante), FIS-DIN-004 (peso P = m·g), MAT-EQU-008 (equação). Próxima: FIS-EGF-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Primeira aula da trilha: o visual.py guarda a linguagem visual da trilha. g = 10 m/s². Nesta aula as forças são sempre
# perpendiculares à barra (braço = distância até o ponto da força); o caso do braço zero (força apontada para o eixo) é citado.

TITULO = "Torque e alavancas"

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
    dict(id="s01", block="gancho", text="{a}Tente abrir uma porta empurrando {b}perto da dobradiça. [p=0.3] Ela quase não se mexe. [p=0.2] Empurre {c}perto da maçaneta, com a mesma força, [p=0.2] e {d}ela gira fácil. [p=0.3] A força foi a mesma. [p=0.2] O que mudou foi {e}a distância."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular o torque de uma força, [p=0.2] {b}equilibrar uma gangorra [p=0.2] e dizer {c}as duas condições para um corpo ficar parado."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas. [p=0.2] {b}A força resultante: se as forças se anulam, um corpo parado continua parado. [p=0.2] E {c}o peso: a massa vezes a gravidade, que aqui vale dez metros por segundo ao quadrado. [p=0.3] Se faltar alguma, procure no canal."),
    # torque
    dict(id="s04", block="torque", text="Uma força pode {a}empurrar um corpo para um lado. [p=0.2] Mas, se o corpo está preso num ponto, [p=0.1] como a porta na dobradiça, [p=0.2] a força também pode {b}fazer o corpo girar. [p=0.3] Esse ponto fixo é {c}o eixo de rotação."),
    dict(id="s05", block="torque", text="A capacidade de uma força fazer girar se chama {a}torque, [p=0.1] ou momento da força. [p=0.3] {b}Torque é a força vezes o braço: [p=0.2] {c}eme igual a efe vezes dê. [p=0.3] {d}Efe é a força, em newtons. [p=0.2] {e}Dê é o braço: a distância do eixo até a linha da força, a reta por onde ela empurra, em metros. [p=0.3] {f}O torque sai em newton vezes metro."),
    dict(id="s06", block="torque", text="Quando a força empurra em ângulo reto com a porta, [p=0.1] o braço é a distância até onde você empurra. [p=0.3] {a}Vinte newtons {b}a oitenta centímetros da dobradiça, zero vírgula oito metro. [p=0.3] {c}Torque: vinte vezes zero vírgula oito, [p=0.1] {d}dezesseis newtons vezes metro. [p=0.3] {e}Perto da dobradiça, a dez centímetros, [p=0.2] o mesmo empurrão dá {f}só dois newtons vezes metro. [p=0.2] Oito vezes menos giro."),
    dict(id="s07", block="torque", text="E tem um caso que engana: [p=0.2] {a}empurrar a porta na direção da dobradiça. [p=0.3] A linha da força passa {b}em cima do eixo, [p=0.2] o braço é zero, [p=0.1] o torque também, [p=0.2] e {c}a porta não gira."),
    # gangorra
    dict(id="s08", block="gangorra", text="{a}Todo torque tem um sentido de giro: [p=0.2] {b}o dos ponteiros do relógio, chamado horário, [p=0.2] ou {c}o contrário, anti-horário. [p=0.3] Numa gangorra, o apoio do meio é o eixo. [p=0.2] {d}O peso de quem senta na esquerda gira a barra para um lado, [p=0.2] e {e}o peso de quem senta na direita, para o outro."),
    dict(id="s09", block="gangorra", text="{a}A gangorra fica em equilíbrio quando os giros empatam: [p=0.2] {b}torque horário igual a torque anti-horário. [p=0.3] {c}Peso vezes distância de um lado, [p=0.1] igual a peso vezes distância do outro."),
    dict(id="s10", block="gangorra", text="{a}Uma criança de trinta quilos senta a dois metros do apoio. [p=0.2] {b}Onde senta, do outro lado, um adulto de sessenta quilos? [p=0.3] {c}Os pesos: trezentos e seiscentos newtons. [p=0.2] {d}Trezentos vezes dois, seiscentos, [p=0.1] igual a {e}seiscentos vezes dê. [p=0.2] {f}Dê igual a um metro. [p=0.3] Quem pesa o dobro senta {g}na metade da distância."),
    # equilíbrio
    dict(id="s11", block="equilibrio", text="Mas parar de girar não basta. [p=0.2] {a}O apoio também empurra a gangorra para cima. [p=0.2] Para ela não subir nem descer, [p=0.2] sem contar o peso da tábua, [p=0.1] {b}essa força tem que valer a soma dos pesos: [p=0.1] {c}novecentos newtons."),
    dict(id="s12", block="equilibrio", text="Então, um corpo fica em equilíbrio com {a}duas condições. [p=0.2] {b}Primeira: força resultante zero, para ele não sair do lugar. [p=0.2] {c}Segunda: torque total zero, para ele não girar. [p=0.3] {d}Faltou uma, e o corpo se mexe."),
    dict(id="s13", block="equilibrio", text="{a}A gangorra é uma alavanca: [p=0.1] uma barra que gira num apoio. [p=0.3] {b}O pé de cabra, {c}o carrinho de mão {d}e o abridor de garrafa funcionam do mesmo jeito. [p=0.3] {e}Braço comprido para a sua força, braço curto para a carga, [p=0.2] e uma força pequena vence uma força grande."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com um erro comum: [p=0.2] {a}medir a distância a partir da ponta da barra. [p=0.3] {b}Numa gangorra de cinco metros, [p=0.1] {c}o apoio está a um metro e meio da ponta esquerda. [p=0.3] {d}Quem senta na ponta direita não está a cinco metros do apoio. [p=0.2] Está a {e}três metros e meio, [p=0.1] porque o braço sempre começa {f}no eixo."),
    # atalho
    dict(id="s15", block="atalho", text="O atalho de prova: [p=0.2] {a}na gangorra, nem calcule o peso. [p=0.3] O peso é a massa vezes dez dos dois lados, [p=0.2] então {b}o dez some da igualdade. [p=0.2] {c}Trinta vezes dois igual a sessenta vezes dê, [p=0.1] e dê dá um metro do mesmo jeito."),
    dict(id="s16", block="atalho", text="E repare na proporção: [p=0.2] {a}o dobro da massa, a metade da distância. [p=0.2] {b}O triplo da massa, um terço da distância. [p=0.3] {c}Cortar o dez só funciona quando todas as forças são pesos. [p=0.2] E a proporção só funciona com duas forças: [p=0.1] com mais, some os torques de cada lado."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Uma barra leve está apoiada num ponto. [p=0.2] {b}De um lado, a trinta centímetros do apoio, há uma caixa de seiscentos newtons. [p=0.3] {c}Do outro, a um metro e meio do apoio, você empurra para baixo. [p=0.3] {d}Que força deixa a barra em equilíbrio? [p=0.2] {e}E qual é o torque do peso da caixa?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Tudo em metro: {a}trinta centímetros são zero vírgula três metro. [p=0.3] {b}O torque da caixa: seiscentos vezes zero vírgula três, [p=0.1] {c}cento e oitenta newtons vezes metro. [p=0.3] {d}Do seu lado, efe vezes um vírgula cinco tem que dar cento e oitenta. [p=0.2] {e}Efe é cento e oitenta dividido por um vírgula cinco: [p=0.1] {f}cento e vinte newtons."),
    dict(id="s20", block="resposta", text="Confira pela proporção: [p=0.2] {a}o seu braço é cinco vezes maior, [p=0.1] então {b}a sua força é cinco vezes menor. [p=0.2] Seiscentos dividido por cinco, {c}cento e vinte."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}torque é força vezes braço, medido a partir do eixo; [p=0.2] {b}em equilíbrio, torque horário igual a anti-horário; [p=0.2] e {c}ficar parado de verdade exige força resultante zero e torque total zero."),
    dict(id="s22", block="fim", text="Na próxima aula, você sai da Terra: [p=0.2] {a}as leis de Kepler, [p=0.1] que descrevem {b}o caminho dos planetas em volta do Sol. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
