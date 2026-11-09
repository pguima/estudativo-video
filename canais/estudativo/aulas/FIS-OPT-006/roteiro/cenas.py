# Estudativo · FIS-OPT-006 — Lentes: formar imagens (Física · Óptica · Refração, lentes e olho humano).
# Habilidade: separar lente convergente de divergente pela forma e achar a imagem com os raios notáveis.
# Pré-requisitos: FIS-OPT-004 (Snell: no vidro o raio se aproxima da normal), FIS-OPT-003 (raios notáveis dos espelhos). Próxima: FIS-OPT-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Bordas finas = convergente vale para lente de índice maior que o meio (vidro no ar),
# dito na aula. O ponto a 2f faz o papel do C do espelho (ponto antiprincipal, nome não usado).

TITULO = "Lentes: convergente, divergente e a imagem"

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
    dict(id="s01", block="gancho", text="{a}Com uma lupa perto do livro, a letra aparece grande e de pé. [p=0.3] {b}Com a mesma lupa, de braço esticado, a paisagem aparece pequena e de cabeça para baixo. [p=0.3] {c}A lente é a mesma. [p=0.2] O que mudou foi {d}a distância."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai separar {b}lente convergente de divergente pela forma [p=0.2] e achar {c}a imagem com os raios notáveis."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}entrando no vidro, o raio se aproxima da normal, e saindo, se afasta; [p=0.2] e {c}os raios notáveis dos espelhos, com imagem real onde os raios se cruzam e virtual onde se cruzam os prolongamentos. [p=0.3] Se faltar alguma, procure no canal."),
    # tipos
    dict(id="s04", block="tipos", text="{a}Lente é um vidro transparente com pelo menos uma face curva. [p=0.2] {b}A luz refrata duas vezes: ao entrar e ao sair. [p=0.3] E a forma decide o que ela faz com os raios."),
    dict(id="s05", block="tipos", text="{a}Lente mais grossa no meio, de bordas finas: [p=0.2] {b}junta os raios. [p=0.2] É a {c}convergente. [p=0.3] {d}Lente mais fina no meio, de bordas grossas: [p=0.2] {e}espalha os raios. [p=0.2] É a {f}divergente. [p=0.3] {g}Isso vale para lente de vidro no ar, com índice maior que o do meio: [p=0.2] num meio mais refringente que a lente, tudo se inverte."),
    dict(id="s06", block="tipos", text="{a}O meio da lente é o centro óptico, ó, [p=0.2] e a reta que passa por ele, de frente para a lente, é o eixo principal. [p=0.2] {b}A lente tem dois focos, F, um de cada lado, à mesma distância. [p=0.3] {c}Na convergente, raios paralelos se encontram no foco do outro lado. [p=0.3] {d}Na divergente, eles saem se abrindo, como se viessem do foco do lado de onde a luz chegou."),
    # raios notáveis
    dict(id="s07", block="raios", text="Os raios notáveis da lente são três. [p=0.3] {a}Um: chegou paralelo ao eixo, sai passando pelo foco. [p=0.2] Na divergente, {b}sai como se viesse do foco, e o prolongamento é que passa por ele. [p=0.3] {c}Dois: passou pelo centro óptico, segue reto, sem desviar."),
    dict(id="s08", block="raios", text="{a}Três: chegou passando pelo foco, ou mirando nele, sai paralelo ao eixo. [p=0.3] {b}Igual nos espelhos: com dois raios saindo da ponta do objeto, [p=0.2] {c}o cruzamento é a ponta da imagem."),
    # convergente: casos
    dict(id="s09", block="convergente", text="Convergente, com {a}o objeto longe, além de duas distâncias focais. [p=0.3] {b}Raio paralelo, sai pelo foco. [p=0.2] {c}Raio pelo centro, segue reto. [p=0.3] {d}Eles se cruzam do outro lado da lente: [p=0.2] imagem {e}real, [p=0.1] {f}invertida [p=0.1] e {g}menor. [p=0.3] {h}É o que faz a câmera do celular."),
    dict(id="s10", block="convergente", text="{a}Objeto entre o foco e a lente: [p=0.2] {b}os raios saem se abrindo, [p=0.2] e {c}os prolongamentos se cruzam do mesmo lado do objeto. [p=0.3] Imagem {d}virtual, [p=0.1] {e}direita [p=0.1] e {f}maior. [p=0.3] {g}É a lupa perto do livro."),
    dict(id="s11", block="convergente", text="{a}O ponto a duas distâncias focais faz o papel do centro de curvatura do espelho. [p=0.3] {b}Objeto entre ele e o foco: [p=0.2] imagem real, invertida e maior. [p=0.2] {c}É o projetor."),
    # divergente
    dict(id="s12", block="divergente", text="Na divergente, {a}o raio paralelo sai se abrindo, como se viesse do foco. [p=0.3] {b}O raio pelo centro segue reto. [p=0.3] {c}Os raios nunca se cruzam: só os prolongamentos, do lado do objeto. [p=0.3] Imagem sempre {d}virtual, [p=0.1] {e}direita [p=0.1] e {f}menor, [p=0.2] como no espelho convexo."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é achar que {a}o tipo da lente decide o tipo da imagem. [p=0.3] {b}A convergente pode dar imagem real ou virtual. [p=0.2] {c}Quem decide é onde o objeto está em relação ao foco. [p=0.3] {d}A lupa do gancho é a prova: perto, aumenta; [p=0.2] longe, inverte."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova para a forma. [p=0.2] O nome da lente diz como é cada face: plana, côncava ou convexa. [p=0.2] {a}Olhe a última palavra do nome. [p=0.3] {b}Biconvexa, plano-convexa, côncavo-convexa: [p=0.2] {c}terminou em convexa, é convergente. [p=0.3] {d}Bicôncava, plano-côncava, convexo-côncava: [p=0.2] {e}terminou em côncava, é divergente."),
    dict(id="s15", block="atalho", text="Funciona porque {a}a última palavra é a face que manda: [p=0.2] ela é a mais curva, e decide se o meio fica grosso ou fino. [p=0.3] {b}Só vale com a lente num meio de índice menor, como o vidro no ar. [p=0.3] E {c}para a imagem, a regra dos espelhos continua: [p=0.2] {d}com uma lente só, real é invertida, virtual é direita."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Num projetor, {a}o slide fica entre o foco e o ponto a duas distâncias focais de uma lente convergente. [p=0.3] {b}Como é a imagem na tela? [p=0.2] E {c}como o slide deve ser colocado para a imagem sair de pé?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Objeto entre o foco e o ponto de duas distâncias focais: [p=0.2] imagem {b}real, [p=0.1] {c}invertida [p=0.1] e {d}maior. [p=0.3] {e}Real, porque ela aparece numa tela: só imagem real pode ser projetada. [p=0.3] E como ela sai invertida, {f}o slide entra de cabeça para baixo."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}bordas finas, convergente; bordas grossas, divergente; [p=0.2] {b}com dois raios notáveis, você acha a imagem; [p=0.2] e {c}a divergente sempre dá imagem virtual, direita e menor."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai {a}calcular a imagem da lente com a mesma equação dos espelhos [p=0.2] e descobrir {b}o que é o grau dos óculos. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
