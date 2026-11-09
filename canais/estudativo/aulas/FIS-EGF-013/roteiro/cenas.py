# Estudativo · FIS-EGF-013 — Satélites e marés (Física · Equilíbrio, Gravitação e Fluidos · Equilíbrio, torque e gravitação).
# Habilidade: achar a velocidade de um satélite igualando gravidade e força centrípeta e explicar as marés.
# Pré-requisitos: FIS-EGF-003 (gravitação), FIS-DIN-010 (força centrípeta, a = v²/R). Próxima: FIS-EGF-014.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fatos: Estação Espacial a cerca de 400 km; g lá = 10·(6400/6800)² ≈ 8,9 m/s². Órbita rasante na Terra: v = √(gR) = 8 km/s,
# período 2π·6,4×10⁶/8000 ≈ 84 min. Geoestacionário: cerca de 36 mil km de altura, sobre o equador, uma volta por dia.
# Maré do Sol ≈ 46% da maré da Lua; marés altas a cada 12 h 25 min, mais ou menos. v²·r = G·M constante (mesmo planeta).

TITULO = "Satélites e marés"

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
    dict(id="s01", block="gancho", text="{a}A Estação Espacial gira a uns quatrocentos quilômetros de altura. [p=0.2] Lá, a gravidade ainda vale {b}quase nove metros por segundo ao quadrado. [p=0.3] {c}Então, por que ela não cai? [p=0.3] {d}Ela cai. [p=0.2] O tempo todo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai achar a velocidade de um satélite [p=0.2] e {b}explicar por que o mar sobe e desce duas vezes por dia."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas. [p=0.2] {b}A gravitação: a força cai com o quadrado da distância entre os centros. [p=0.2] E {c}a força centrípeta: para girar em círculo, a aceleração aponta para o centro e vale vê ao quadrado sobre érre. [p=0.3] Se faltar alguma, procure no canal."),
    # o canhão de Newton
    dict(id="s04", block="canhao", text="Imagine {a}um canhão no alto de uma montanha. [p=0.2] {b}A bala lenta cai perto. [p=0.2] {c}A mais rápida cai mais longe. [p=0.3] {d}Rápida o bastante, ela continua caindo, [p=0.1] mas o chão curvo da Terra se afasta na mesma medida. [p=0.2] {e}Ela nunca chega ao chão: entrou em órbita."),
    # velocidade orbital
    dict(id="s05", block="orbita", text="{a}Num satélite em órbita circular, só a gravidade puxa, [p=0.1] e para o centro da Terra. [p=0.2] {b}Ela faz o papel de força centrípeta. [p=0.3] {c}Rente à Terra, a aceleração da gravidade é gê. [p=0.2] Então, {d}vê ao quadrado sobre érre é igual a gê."),
    dict(id="s06", block="orbita", text="{a}Isolando: vê é a raiz de gê vezes érre. [p=0.3] {b}Gê é a gravidade na altura da órbita, em metros por segundo ao quadrado: [p=0.1] rente ao planeta, é a da superfície. [p=0.1] {c}Érre é o raio da órbita, do centro do planeta até o satélite, em metros. [p=0.3] {d}Repare: a massa do satélite não entra. [p=0.2] {e}Um parafuso e a Estação Espacial, na mesma órbita, andam na mesma velocidade."),
    dict(id="s07", block="orbita", text="{a}Na Terra, gê vale dez, e érre, seis mil e quatrocentos quilômetros, [p=0.1] {b}seis vírgula quatro vezes dez elevado a seis metros. [p=0.3] {c}Gê vezes érre: sessenta e quatro milhões. [p=0.2] {d}A raiz: oito mil metros por segundo. [p=0.3] {e}Oito quilômetros por segundo! [p=0.2] Uma volta na Terra em cerca de uma hora e meia."),
    dict(id="s08", block="orbita", text="{a}Mais longe da Terra, a gravidade fica mais fraca, [p=0.1] e o satélite {b}precisa de menos velocidade. [p=0.3] {c}Com a fórmula de Newton no lugar de gê, [p=0.1] vê ao quadrado fica igual a gê maiúsculo vezes eme maiúsculo, sobre érre. [p=0.3] {d}Raio quatro vezes maior, vê ao quadrado quatro vezes menor, [p=0.1] e {e}vê, duas vezes menor."),
    dict(id="s09", block="orbita", text="{a}O caso mais famoso é o satélite geoestacionário, [p=0.1] o da antena parabólica. [p=0.2] {b}Ele dá uma volta por dia, junto com a Terra, em cima da linha do equador, [p=0.2] e por isso {c}parece parado no céu. [p=0.2] Para isso, {d}fica a uns trinta e seis mil quilômetros de altura."),
    # marés
    dict(id="s10", block="mares", text="E as marés? [p=0.2] {a}A Lua puxa a Terra inteira, [p=0.1] mas {b}não puxa tudo igual. [p=0.3] {c}A água do lado virado para a Lua está mais perto: é puxada com mais força. [p=0.2] {d}O centro da Terra, com menos. [p=0.2] {e}A água do lado oposto, com menos ainda."),
    dict(id="s11", block="mares", text="{a}O resultado é que o oceano se estica em dois montes: [p=0.2] {b}um do lado da Lua, [p=0.1] {c}outro do lado oposto. [p=0.3] {d}A Terra gira por baixo deles uma vez por dia, [p=0.2] e cada praia passa {e}por uma maré alta a cada doze horas e pouco: [p=0.1] duas altas e duas baixas por dia."),
    dict(id="s12", block="mares", text="{a}O Sol também faz maré, mais fraca: [p=0.1] de tão longe, ele puxa quase igual os dois lados da Terra. [p=0.3] {b}Na lua cheia e na lua nova, Sol e Lua ficam alinhados, [p=0.1] e as marés {c}se somam: ficam maiores. [p=0.3] {d}Na lua crescente e na minguante, eles puxam em ângulo reto, [p=0.1] e as marés {e}ficam menores."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}dizer que o astronauta flutua porque lá não tem gravidade. [p=0.3] {b}A quatrocentos quilômetros, a gravidade é quase nove. [p=0.2] {c}Ele flutua porque cai junto com a nave, [p=0.1] com a mesma aceleração. [p=0.2] {d}Nada empurra um contra o outro, [p=0.1] e a sensação é de não ter peso."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho de prova: [p=0.2] {a}para comparar órbitas, use vê ao quadrado vezes érre constante. [p=0.3] {b}Raio nove vezes maior, velocidade três vezes menor. [p=0.2] {c}Raio dezesseis vezes maior, quatro vezes menor. [p=0.3] {d}Vale para tudo que gira em volta do mesmo planeta, [p=0.1] porque gê maiúsculo e a massa dele não mudam."),
    dict(id="s15", block="atalho", text="{a}Só cuidado com a altura: [p=0.2] {b}o atalho usa o raio da órbita, a partir do centro. [p=0.2] {c}Se a questão der a altura, some antes o raio do planeta."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Num planeta, a gravidade na superfície vale quatro metros por segundo ao quadrado, [p=0.2] {b}e o raio é de quatro mil quilômetros. [p=0.3] {c}Qual é a velocidade de um satélite numa órbita rente à superfície? [p=0.2] {d}E se o satélite tiver o dobro da massa?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}O raio em metros: quatro vezes dez elevado a seis. [p=0.2] {b}Gê vezes érre: quatro vezes quatro vezes dez elevado a seis, [p=0.1] {c}dezesseis milhões. [p=0.2] {d}A raiz de dezesseis milhões: [p=0.1] {e}quatro mil metros por segundo, [p=0.1] quatro quilômetros por segundo."),
    dict(id="s19", block="resposta", text="{a}E com o dobro da massa? [p=0.2] {b}A mesma velocidade. [p=0.2] A massa do satélite não entra na conta."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}em órbita, a gravidade faz o papel de força centrípeta; [p=0.2] {b}rente ao planeta, vê é a raiz de gê vezes érre; [p=0.2] e {c}a maré vem da Lua puxar cada lado da Terra com uma força diferente."),
    dict(id="s21", block="fim", text="Na próxima aula, {a}você pratica tudo isso: [p=0.2] {b}alavancas, planetas e satélites, em questões inéditas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
