# Estudativo · QUI-LIG-011 — Gelo que boia e inseto sobre a água (Química · Ligações Químicas · Polaridade e forças intermoleculares).
# Habilidade: explicar pelas ligações de hidrogênio por que o gelo boia, por que um inseto anda sobre a água e como a água sobe
# por um tubo fino.
# Pré-requisitos: QUI-LIG-009, MAT-RAZ-017. Próxima: QUI-LIG-012 (praticando: polaridade e forças intermoleculares).
# Atenção: LIG-010 (pontos de ebulição) NÃO está em "Já ensinado": nada de comparar pontos de ebulição.
# Marcas: {cue} animação · [p=0.2] pausa. Questão inédita, criada para esta aula.
# Fatos: densidade do gelo ≈ 0,92 g/cm³ (0,917); a maioria dos sólidos afunda no próprio líquido (parafina, por exemplo);
# no gelo comum cada molécula faz 4 ligações de H (rede de anéis de 6, com vãos); aço ≈ 7,8 g/cm³ ("quase oito vezes"), um
# clipe pode ficar na superfície; detergente diminui a tensão superficial; capilaridade: adesão ao vidro + coesão; papel-toalha.
# Contas: 920 g / 1000 cm³ = 0,92 g/cm³; 460 g de água = 460 cm³; 460 / 0,92 = 500 cm³; 500 − 460 = 40 cm³.

TITULO = "Gelo que boia e inseto sobre a água"

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
    dict(id="s01", block="gancho", text="{a}Quase todo material encolhe quando congela, [p=0.1] e {b}o pedaço sólido afunda no próprio líquido. [p=0.3] {c}A água faz o contrário: o gelo boia. [p=0.3] {d}Se não boiasse, os lagos congelariam de baixo para cima."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai explicar {b}por que o gelo boia, [p=0.1] {c}por que um inseto anda sobre a água [p=0.1] e {d}como a água sobe por um tubo fino. [p=0.2] As três respostas têm o mesmo nome: {e}ligação de hidrogênio."),
    # lembrete
    dict(id="s03", block="lembrete", text="Duas ideias de aulas anteriores. [p=0.2] {a}Densidade é a massa dividida pelo volume. [p=0.1] {b}O que tem densidade menor que a da água, um grama por centímetro cúbico, boia nela. [p=0.3] E {c}entre as moléculas de água há ligações de hidrogênio: [p=0.1] {d}o hidrogênio de uma gruda no oxigênio da vizinha. [p=0.2] Se alguma travar, procure no canal."),
    # gelo
    dict(id="s04", block="gelo", text="{a}Na água líquida, essas ligações se formam e se desfazem o tempo todo. [p=0.2] {b}As moléculas escorregam umas pelas outras e ficam bem juntinhas."),
    dict(id="s05", block="gelo", text="{a}Ao congelar, cada molécula prende quatro vizinhas, em posições fixas. [p=0.3] {b}Elas formam uma rede de anéis de seis lados, [p=0.1] {c}com espaços vazios no meio. [p=0.3] {d}A mesma massa passa a ocupar mais volume."),
    dict(id="s06", block="gelo", text="Faça a conta da densidade. [p=0.2] {a}Um litro de gelo, ou mil centímetros cúbicos, tem massa de cerca de novecentos e vinte gramas. [p=0.3] {b}Novecentos e vinte dividido por mil dá zero vírgula noventa e dois grama por centímetro cúbico. [p=0.3] {c}Menor que um: o gelo boia. [p=0.3] {d}E o lago? [p=0.1] {e}O gelo fica em cima, como uma tampa, [p=0.1] e {f}a água de baixo continua líquida, com os peixes vivos."),
    # tensão superficial
    dict(id="s07", block="tensao", text="{a}Dentro da água, cada molécula é puxada pelas vizinhas de todos os lados, [p=0.1] e os puxões se equilibram. [p=0.3] {b}Na superfície, não há vizinhas em cima: [p=0.1] {c}as moléculas são puxadas para baixo e para os lados. [p=0.3] {d}A superfície fica esticada, como uma película. [p=0.2] {e}É a tensão superficial, alta na água por causa das ligações de hidrogênio."),
    dict(id="s08", block="tensao", text="{a}Um inseto leve não pesa o bastante para furar essa película. [p=0.3] {b}Até um clipe de aço, quase oito vezes mais denso que a água, pode ficar por cima, se for posto com cuidado. [p=0.3] {c}Pingue detergente, e o clipe afunda: [p=0.1] {d}o detergente se mete entre as moléculas da superfície e enfraquece a película."),
    # capilaridade
    dict(id="s09", block="tubo", text="{a}E o tubo fino? [p=0.2] {b}O vidro tem oxigênios na superfície. [p=0.1] A água faz ligações de hidrogênio com eles [p=0.1] e {c}sobe pela parede. [p=0.2] {d}Como as moléculas se seguram umas nas outras, puxam junto a água do meio. [p=0.3] {e}Quanto mais fino o tubo, mais alto ela sobe. [p=0.2] {f}É a capilaridade, a mesma que faz o papel-toalha puxar a água."),
    # erro
    dict(id="s10", block="erro", text="Cuidado com o erro comum: [p=0.2] {a}achar que o gelo boia porque tem ar preso dentro. [p=0.3] {b}Um gelo bem transparente, sem nenhuma bolha, boia do mesmo jeito. [p=0.2] {c}Os espaços vazios são da rede de moléculas, [p=0.1] {d}muito menores que qualquer bolha."),
    # atalho
    dict(id="s11", block="atalho", text="O atalho de prova: [p=0.1] {a}a questão fala de um comportamento estranho da água? [p=0.2] {b}Gelo que boia, película na superfície, água subindo no tubo? [p=0.3] {c}A resposta quase sempre passa pelas ligações de hidrogênio. [p=0.3] Funciona porque {d}é a força que a água tem de sobra. [p=0.2] {e}Se a questão der números, a explicação continua a mesma: [p=0.1] só falta fazer a conta da densidade."),
    # questão
    dict(id="s12", block="questao", text="Hora de testar. [p=0.2] {a}Uma forminha de gelo recebe quatrocentos e sessenta gramas de água. [p=0.3] {b}Que volume essa água ocupa, líquida? [p=0.2] {c}E depois de congelar, com densidade zero vírgula noventa e dois grama por centímetro cúbico? [p=0.3] {d}Por que o volume mudou?"),
    dict(id="s13", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s14", block="resposta", text="Vamos lá. [p=0.2] {a}Água líquida: um grama por centímetro cúbico. [p=0.1] {b}Quatrocentos e sessenta gramas ocupam quatrocentos e sessenta centímetros cúbicos. [p=0.3] {c}No gelo, o volume é a massa dividida pela densidade: [p=0.1] {d}quatrocentos e sessenta dividido por zero vírgula noventa e dois dá quinhentos centímetros cúbicos. [p=0.3] {e}Quarenta centímetros cúbicos a mais."),
    dict(id="s15", block="resposta", text="{a}Por quê? [p=0.1] Ao congelar, {b}cada molécula prende quatro vizinhas na rede de anéis, [p=0.1] {c}com espaços vazios. [p=0.2] {d}Mesma massa, mais volume. [p=0.2] {e}É por isso que a garrafa cheia esquecida no congelador estoura."),
    # fechamento
    dict(id="s16", block="fim", text="Resumindo: [p=0.1] {a}no gelo, as ligações de hidrogênio montam uma rede com espaços, e ele boia. [p=0.1] {b}Na superfície, elas formam uma película. [p=0.1] {c}No tubo fino, puxam a água para cima."),
    dict(id="s17", block="fim", text="Na próxima aula, você pratica a trilha toda: [p=0.1] {a}prevê se uma substância se dissolve e qual ferve mais alto, {b}a partir da estrutura da molécula. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
