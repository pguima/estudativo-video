# Estudativo · QUI-INO-009 — Síntese, análise e combustão (Química · Funções e Reações Inorgânicas · Reações e balanceamento).
# Habilidade: classificar uma reação em síntese ou análise e prever os produtos da combustão completa e incompleta.
# Pré-requisitos: QUI-INO-008. Próxima: QUI-INO-010 (simples troca e fila de reatividade).
# "Já ensinado" NÃO tem ácidos, bases, íons nem parênteses: nenhuma substância é chamada de ácido ou base.
# Fatos: 2 H₂ + O₂ → 2 H₂O; N₂ + 3 H₂ → 2 NH₃ (amônia, matéria-prima dos adubos nitrogenados); 2 H₂O₂ → 2 H₂O + O₂ (a água oxigenada
# borbulha no machucado: as bolhas são oxigênio); CaCO₃ → CaO + CO₂ com calor (calcário vira cal). Pirólise (calor),
# fotólise (luz), eletrólise (corrente). CH₄ = metano, do gás natural. CH₄ + 2 O₂ → CO₂ + 2 H₂O; 2 CH₄ + 3 O₂ → 2 CO + 4 H₂O;
# CH₄ + O₂ → C + 2 H₂O. Chama azul = completa; amarela com fuligem = incompleta. CO não tem cheiro e toma o lugar do
# oxigênio no sangue. C + O₂ → CO₂ é síntese e combustão ao mesmo tempo.
# Questão inédita: 2 HgO → 2 Hg + O₂ (análise, óxido de mercúrio com calor); CaO + CO₂ → CaCO₃ (síntese);
# butano C₄H₁₀ (botijão): completa → CO₂ + H₂O; incompleta → CO (ou C) + H₂O.

TITULO = "Síntese, análise e combustão"

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
    dict(id="s01", block="gancho", text="{a}A chama do fogão deve ser azul. [p=0.3] {b}Quando ela fica amarela e solta fuligem, [p=0.1] {c}o fogão está fazendo outra reação. [p=0.3] {d}E essa reação pode soltar um gás que mata, sem cheiro nenhum."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}classificar uma reação em síntese ou análise [p=0.2] e {b}prever o que sai de uma queima, completa ou incompleta."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre: [p=0.1] {a}reagentes ficam à esquerda da seta, produtos à direita. [p=0.3] E {b}balancear é acertar os coeficientes, [p=0.1] na ordem metal, ametal, carbono, hidrogênio e oxigênio."),
    # síntese
    dict(id="s04", block="sintese", text="{a}Síntese é quando duas ou mais substâncias formam uma só. [p=0.2] {b}Como peças que se encaixam. [p=0.3] {c}Dois agá dois, mais ó dois, produz dois agá dois ó: [p=0.1] {d}hidrogênio e oxigênio viram água."),
    dict(id="s05", block="sintese", text="Outro exemplo: [p=0.1] {a}ene dois, mais três agá dois, produz dois ene agá três. [p=0.2] {b}É a amônia, matéria-prima dos adubos. [p=0.3] {c}Duas substâncias entram, uma só sai: [p=0.1] {d}síntese, também chamada de adição."),
    # análise
    dict(id="s06", block="analise", text="{a}Análise é o contrário: [p=0.1] {b}uma substância se quebra em duas ou mais. [p=0.2] Também se chama decomposição. [p=0.3] {c}A água oxigenada, agá dois ó dois, se quebra em água e gás oxigênio. [p=0.2] {d}É a água oxigenada borbulhando no machucado: [p=0.1] as bolhas são oxigênio."),
    dict(id="s07", block="analise", text="{a}Muitas análises precisam de energia. [p=0.2] {b}O calcário, cê á cê ó três, aquecido, [p=0.1] {c}vira cal, cê á ó, e gás carbônico. [p=0.3] {d}Com calor, a análise se chama pirólise. [p=0.2] {e}Com luz, fotólise. [p=0.2] {f}Com corrente elétrica, eletrólise."),
    # combustão
    dict(id="s08", block="combustao", text="{a}Combustão é a queima. [p=0.2] {b}Um combustível reage com o oxigênio, que se chama comburente, [p=0.1] {c}e libera calor e luz."),
    dict(id="s09", block="combustao", text="{a}Com oxigênio de sobra, a combustão é completa. [p=0.2] {b}Num combustível feito de carbono e hidrogênio, [p=0.1] {c}os produtos são gás carbônico e água. [p=0.3] {d}Cê agá quatro, o metano do gás natural, mais dois ó dois, [p=0.1] {e}produz cê ó dois, mais dois agá dois ó."),
    dict(id="s10", block="combustao", text="{a}Com pouco oxigênio, a combustão é incompleta. [p=0.2] {b}O carbono não chega a cê ó dois. [p=0.2] {c}Sai cê ó, o monóxido de carbono, [p=0.1] {d}ou até cê, o carbono puro: a fuligem. [p=0.3] {e}A água continua saindo."),
    dict(id="s11", block="combustao", text="{a}Dois cê agá quatro, mais três ó dois, [p=0.1] produz dois cê ó, mais quatro agá dois ó. [p=0.3] {b}Entra menos oxigênio do que na completa, [p=0.1] {c}e cada carbono sai com um oxigênio só. [p=0.3] {d}É o gás que sai junto com a chama amarela: [p=0.1] não tem cheiro e toma o lugar do oxigênio no sangue."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}achar que toda queima solta gás carbônico. [p=0.3] {b}Na incompleta, sai monóxido de carbono, ou fuligem. [p=0.3] {c}E é o monóxido que envenena quem fica num lugar fechado com o fogo aceso."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho de prova: [p=0.1] {a}conte as substâncias diferentes de cada lado, sem olhar os coeficientes. [p=0.2] {b}Várias viram uma: síntese. [p=0.2] {c}Uma vira várias: análise. [p=0.2] {d}Um combustível com ó dois, soltando calor: combustão. [p=0.3] E, na queima completa, {e}todo carbono vira cê ó dois e todo hidrogênio vira agá dois ó."),
    dict(id="s14", block="atalho", text="Funciona porque o tipo depende de {a}quantas substâncias entram e quantas saem. [p=0.3] {b}Só cuidado: uma queima pode ser síntese ao mesmo tempo. [p=0.1] {c}Cê mais ó dois produz cê ó dois. [p=0.2] {d}Se o enunciado fala em queima, a resposta é combustão."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Classifique: [p=0.1] {a}dois agá gê ó, o óxido de mercúrio, aquecido, produz dois agá gê, mais ó dois. [p=0.3] {b}Cê á ó, mais cê ó dois, produz cê á cê ó três. [p=0.3] E {c}quais são os produtos da queima completa e da incompleta do butano, cê quatro agá dez, o outro gás do botijão?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}O óxido de mercúrio é uma substância que vira duas: [p=0.1] {b}análise, e pirólise, porque foi com calor. [p=0.3] {c}A cal com o gás carbônico são duas que viram uma: [p=0.1] {d}síntese."),
    dict(id="s18", block="resposta", text="{a}O butano é de carbono e hidrogênio. [p=0.2] {b}Na queima completa, sai gás carbônico e água. [p=0.2] {c}Na incompleta, sai monóxido de carbono, ou fuligem, e água."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}na síntese, várias viram uma; [p=0.1] {b}na análise, uma vira várias; [p=0.1] e {c}a queima completa dá gás carbônico e água, a incompleta dá monóxido ou fuligem."),
    dict(id="s20", block="fim", text="Na próxima aula, um elemento toma o lugar de outro: [p=0.2] {a}a simples troca, [p=0.1] {b}e a fila que diz por que o zinco reage com ácido e o cobre não. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
