# Estudativo · QUI-INO-005 — Escala de pH e indicadores (Química · Funções e Reações Inorgânicas · Ácidos, bases, sais e óxidos).
# Habilidade: dizer pelo pH se limão, água pura e soda são ácidos, neutros ou básicos e prever a cor da fenolftaleína e do
# repolho roxo.
# Pré-requisitos: QUI-INO-001, QUI-INO-002. Próxima: QUI-INO-013 (Brønsted-Lowry e Lewis).
# Atenção: QUI-INO-003 e QUI-INO-004 NÃO estão em "Já ensinado": a aula não fala de neutralização, sal nem óxido.
# pH = "pê agá". Escala de 0 a 14 (água a 25 °C). Cálculo de pH (logaritmo) é de outra aula (QUI-EQL-003).
# Fatos: limão pH ≈ 2; vinagre ≈ 3; água pura = 7; leite de magnésia ≈ 10; água com sabão em pó ≈ 10; soda cáustica em
# solução ≈ 13 a 14. Cada unidade a menos = 10 vezes mais ácido. Fenolftaleína: incolor abaixo de ≈ 8,2, rosa acima.
# Repolho roxo (antocianinas): vermelho/rosa no ácido, roxo no neutro, azul-esverdeado/verde no básico, amarelo no muito básico.
# Questão inédita.

TITULO = "Escala de pH e indicadores"

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
    dict(id="s01", block="gancho", text="{a}Pingue suco de repolho roxo no vinagre, e {b}ele fica vermelho. [p=0.3] {c}Na água com sabão em pó, ele fica verde. [p=0.3] {d}O repolho está contando se a solução é ácida ou básica."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}ler a escala de pê agá [p=0.2] e {b}prever a cor de dois indicadores: [p=0.1] a fenolftaleína e o repolho roxo."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre: [p=0.1] {a}ácido solta agá mais na água. [p=0.2] {b}Base solta ó agá menos. [p=0.3] {c}E a água pura tem agá mais e ó agá menos na mesma quantidade, bem pouquinho."),
    # escala
    dict(id="s04", block="escala", text="Para dizer quão ácida ou básica é uma solução, existe {a}a escala de pê agá. [p=0.2] {b}Ela vai de zero a catorze."),
    dict(id="s05", block="escala", text="{a}O meio, o sete, é neutro: [p=0.1] é o pê agá da água pura. [p=0.3] {b}Abaixo de sete, a solução é ácida. [p=0.2] {c}Acima de sete, é básica."),
    dict(id="s06", block="escala", text="{a}Quanto mais íons agá mais na água, menor o pê agá. [p=0.3] {b}Quanto mais íons ó agá menos, maior o pê agá. [p=0.3] E {c}cada número a menos na escala deixa a solução dez vezes mais ácida."),
    dict(id="s07", block="escala", text="Veja três exemplos. [p=0.2] {a}O suco de limão tem pê agá perto de dois: [p=0.1] ácido. [p=0.2] {b}A água pura, sete: [p=0.1] neutra. [p=0.2] {c}A soda cáustica dissolvida, perto de catorze: [p=0.1] muito básica."),
    dict(id="s08", block="escala", text="E no dia a dia: [p=0.1] {a}o refrigerante fica perto de três, [p=0.1] {b}o café perto de cinco, [p=0.2] {c}o sangue, um pouco acima de sete, [p=0.1] {d}e a água sanitária perto de doze. [p=0.3] {e}Quase tudo o que você bebe é um pouco ácido."),
    # indicadores
    dict(id="s09", block="fenol", text="Mas ninguém vê o pê agá a olho nu. [p=0.2] Para isso existe o {a}indicador: [p=0.1] {b}uma substância que muda de cor conforme o pê agá. [p=0.2] {c}Umas gotas bastam."),
    dict(id="s10", block="fenol", text="O mais usado no laboratório é a {a}fenolftaleína. [p=0.2] {b}No ácido, ela é incolor. [p=0.2] {c}No neutro, também incolor. [p=0.3] {d}Ela só fica rosa no meio básico, [p=0.1] com pê agá acima de oito, mais ou menos."),
    dict(id="s11", block="repolho", text="{a}O suco de repolho roxo é um indicador caseiro. [p=0.2] {b}No ácido, fica vermelho ou rosa. [p=0.2] {c}No neutro, continua roxo. [p=0.2] {d}No básico, fica azul ou verde. [p=0.2] {e}E, no muito básico, amarelo."),
    dict(id="s12", block="repolho", text="{a}O repolho tem um pigmento que muda de forma com o pê agá, [p=0.1] e cada forma tem uma cor. [p=0.3] {b}Por isso ele mostra várias cores, e a fenolftaleína só duas."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é {a}achar que a fenolftaleína fica vermelha no ácido. [p=0.3] {b}Ela fica incolor. [p=0.3] E {c}incolor não quer dizer ácido: [p=0.1] {d}pode ser ácido, neutro, ou até um pouco básico, como o sangue. [p=0.2] A fenolftaleína não separa um do outro."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho de prova: [p=0.2] {a}fenolftaleína rosa é base, sempre. [p=0.2] {b}Incolor quer dizer só que o pê agá está abaixo de oito, mais ou menos. [p=0.3] {c}Para separar ácido de neutro, use outro indicador, como o repolho."),
    dict(id="s15", block="atalho", text="E cuidado com a escala, que parece ao contrário: [p=0.2] {a}o número menor é o mais ácido. [p=0.3] {b}Pê agá dois é mais ácido que pê agá cinco."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Três copos: [p=0.1] {a}vinagre, com pê agá três; [p=0.2] {b}água com açúcar, com pê agá sete; [p=0.2] {c}e leite de magnésia, com pê agá dez. [p=0.3] {d}Classifique cada um. [p=0.2] E {e}diga a cor da fenolftaleína e do repolho roxo em cada copo."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Vinagre, pê agá três, abaixo de sete: ácido. [p=0.1] {b}Fenolftaleína incolor, repolho vermelho. [p=0.3] {c}Água com açúcar, pê agá sete: neutra. [p=0.1] {d}Fenolftaleína incolor, repolho roxo."),
    dict(id="s19", block="resposta", text="{a}Leite de magnésia, pê agá dez, acima de sete: básico. [p=0.1] {b}Fenolftaleína rosa, repolho verde. [p=0.3] {c}Repare: a fenolftaleína deixou dois copos iguais, [p=0.1] {d}e o repolho separou os três."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}abaixo de sete é ácido, sete é neutro, acima de sete é básico. [p=0.2] {b}Fenolftaleína só fica rosa na base, [p=0.1] e {c}o repolho vai do vermelho ao verde."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai ver {a}outras duas definições de ácido e base: [p=0.2] {b}a de Brônsted e Lowry, com o agá mais que passa de um para o outro, [p=0.1] {c}e a de Lewis, com pares de elétrons. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
