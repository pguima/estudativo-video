# Estudativo · FIS-OPT-009 — Lupa, microscópio e telescópio (Física · Óptica · Refração, lentes e olho humano).
# Habilidade: dizer que imagem cada lente forma em lupa, câmera, microscópio e luneta.
# Pré-requisitos: FIS-OPT-007 (equação das lentes, aumento). Próxima: FIS-OPT-010 (prática).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. O olho (FIS-OPT-008) não está em "Já ensinado": não é usado.
# Microscópio: aumento total = produto dos aumentos (40 × 10 = 400). Luneta: aumento visual = f objetiva ÷ f ocular (aumento
# do ângulo, não A = i/o; dito como "quantas vezes o astro parece maior"). Binóculo tem prismas que desviram a imagem.

TITULO = "Lupa, câmera, microscópio e luneta"

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
    dict(id="s01", block="gancho", text="{a}O microscópio e a luneta são feitos do mesmo jeito: duas lentes convergentes. [p=0.3] {b}Um mostra uma célula. [p=0.2] {c}O outro mostra as crateras da Lua. [p=0.3] A diferença está em {d}qual das lentes tem o foco curto."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai dizer que imagem cada lente forma {b}na lupa, [p=0.1] {c}na câmera, [p=0.1] {d}no microscópio [p=0.1] e {e}na luneta."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}uma coisa: [p=0.2] {b}na lente convergente, objeto longe dá imagem real, invertida e menor; [p=0.2] {c}entre o foco e o ponto de duas distâncias focais, real, invertida e maior; [p=0.2] {d}e dentro do foco, virtual, direita e maior. [p=0.3] Se faltar, procure no canal."),
    # lupa e câmera
    dict(id="s04", block="simples", text="{a}A lupa é uma lente convergente com o objeto dentro do foco. [p=0.3] {b}A imagem é virtual, direita e maior, [p=0.2] do mesmo lado do objeto. [p=0.3] {c}Por isso a lupa fica perto da letra: [p=0.2] longe dela, a imagem vira real e invertida."),
    dict(id="s05", block="simples", text="{a}Na câmera, o objeto está longe, além de duas distâncias focais. [p=0.3] {b}A imagem é real, invertida e menor, [p=0.2] e {c}se forma no sensor, do outro lado da lente. [p=0.3] {d}Para focar, a lente anda um pouco para a frente ou para trás, [p=0.2] até a imagem cair bem no sensor."),
    # imagem que vira objeto
    dict(id="s06", block="duas", text="O microscópio e a luneta usam {a}duas lentes, uma atrás da outra. [p=0.3] E o truque é este: [p=0.2] {b}a imagem real da primeira lente {c}serve de objeto para a segunda. [p=0.3] {d}A lente perto do objeto se chama objetiva. [p=0.2] {e}A lente perto do olho se chama ocular."),
    # microscópio
    dict(id="s07", block="micro", text="{a}No microscópio, a objetiva tem o foco bem curto. [p=0.3] {b}A lâmina fica um pouco além do foco dela, entre o foco e o ponto de duas distâncias focais. [p=0.3] {c}Imagem real, invertida e maior, dentro do tubo."),
    dict(id="s08", block="micro", text="{a}A ocular funciona como uma lupa sobre essa imagem: [p=0.2] {b}ela fica dentro do foco da ocular. [p=0.3] {c}Sai uma imagem virtual e maior ainda. [p=0.3] {d}No final, a imagem é virtual, invertida em relação à lâmina e muito maior."),
    dict(id="s09", block="micro", text="{a}O aumento total é o produto dos aumentos. [p=0.2] {b}Objetiva que aumenta quarenta vezes, ocular que aumenta dez: [p=0.2] {c}quarenta vezes dez, quatrocentas vezes."),
    # luneta
    dict(id="s10", block="luneta", text="{a}Na luneta, é a objetiva que tem o foco longo. [p=0.3] {b}A Lua está muito longe, [p=0.2] então {c}a imagem é real, invertida e menor, [p=0.2] {d}e se forma perto do foco da objetiva."),
    dict(id="s11", block="luneta", text="{a}A ocular, de foco curto, é a lupa sobre essa imagem. [p=0.3] {b}No final: virtual e invertida. [p=0.3] {c}A imagem é muito menor que a Lua, mas fica bem perto do olho: [p=0.2] por isso a Lua parece maior."),
    dict(id="s12", block="luneta", text="{a}Quantas vezes maior ela parece? [p=0.2] {b}Divida o foco da objetiva pelo da ocular. [p=0.3] {c}Objetiva de cem centímetros, ocular de dois: [p=0.2] {d}cinquenta vezes. [p=0.3] {e}Alguns telescópios trocam a objetiva por um espelho côncavo, [p=0.2] que também forma a imagem real perto do foco."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é achar que {a}a imagem final é direita porque a ocular é uma lupa. [p=0.3] {b}A lupa não desvira nada: [p=0.2] {c}ela mostra de pé aquilo que recebe. [p=0.3] {d}E ela recebe uma imagem que já veio invertida da objetiva. [p=0.2] {e}Por isso a imagem final é invertida."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}conte as imagens reais. [p=0.3] {b}Cada imagem real de uma lente convergente vira tudo de cabeça para baixo. [p=0.3] {c}Lupa: nenhuma real, imagem direita. [p=0.2] {d}Câmera e projetor: uma real, invertida. [p=0.2] {e}Microscópio e luneta: uma real no meio, e a lupa não desvira: invertida."),
    dict(id="s15", block="atalho", text="Funciona porque {a}imagem real se forma com os raios cruzados, [p=0.2] e {b}a imagem virtual da lupa fica de pé em relação ao que ela recebe. [p=0.3] {c}Não serve quando o aparelho tem prismas que desviram a imagem, [p=0.2] como o binóculo."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Um microscópio tem {a}objetiva que aumenta quarenta vezes [p=0.2] e {b}ocular que aumenta quinze vezes. [p=0.3] {c}Qual é o aumento total? [p=0.2] E {d}a imagem final é real ou virtual, direita ou invertida?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}O aumento total é o produto: [p=0.2] {b}quarenta vezes quinze, seiscentas vezes. [p=0.3] {c}A ocular é uma lupa: a imagem final é virtual. [p=0.3] {d}E existe uma imagem real no meio: [p=0.2] {e}a imagem final é invertida."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}lupa, virtual e direita; [p=0.2] {b}câmera, real e invertida; [p=0.2] {c}microscópio e luneta, a objetiva forma uma imagem real, e a ocular é uma lupa sobre ela, com imagem final virtual e invertida."),
    dict(id="s20", block="fim", text="Na próxima aula, {a}é hora de praticar: [p=0.2] {b}questões de espelhos, lentes e olho, resolvidas passo a passo. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
