# Estudativo · FIS-OND-011 — Rádio, micro-ondas, raios X e outros usos (Física · Ondas e Som · Espectro eletromagnético).
# Habilidade: ligar cada faixa do espectro ao seu uso e ao seu risco em celular, forno, controle remoto, protetor solar e radiografia.
# Pré-requisitos: FIS-OND-010 (ordem do espectro, ionizante). Próxima: FIS-OND-012.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Forno: 2,45 GHz, λ ≈ 12 cm; furos da grade: poucos milímetros.
# Celular e wi-fi: faixa das micro-ondas (de ~0,7 a ~6 GHz), não ionizante. Osso barra raio X: cálcio, número atômico maior.
# Irradiação de alimentos com gama não deixa o alimento radioativo. Radioatividade é assunto de outra aula.

TITULO = "Rádio, micro-ondas, raios X e outros usos"

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
    dict(id="s01", block="gancho", text="{a}O celular e o raio X do dentista usam ondas da mesma família. [p=0.3] Então, por que o dentista {b}põe um avental de chumbo em você, [p=0.2] e {c}o celular não pede nada?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai ligar cada faixa do espectro {b}ao seu uso [p=0.1] e {c}ao seu risco."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a ordem do espectro, do rádio ao gama; [p=0.2] e {c}que, do ultravioleta mais forte em diante, a radiação é ionizante: arranca elétrons dos átomos. [p=0.3] Se faltar alguma, procure no canal."),
    # rádio e micro-ondas
    dict(id="s04", block="radio", text="{a}As ondas de rádio são as mais compridas, de metros a quilômetros. [p=0.2] Elas levam {b}o som do rádio [p=0.1] e {c}a imagem da televisão aberta. [p=0.3] {d}Não ionizam."),
    dict(id="s05", block="micro", text="{a}As micro-ondas têm lambda de centímetros. [p=0.2] Elas levam {b}o sinal do celular, do wi-fi e do radar. [p=0.3] E fazem {c}o forno: [p=0.1] a onda faz {d}as moléculas de água da comida girarem para lá e para cá, [p=0.1] e esse agito esquenta a comida."),
    dict(id="s06", block="micro", text="{a}O lambda do forno é de uns doze centímetros, [p=0.1] e os furos da grade da porta têm poucos milímetros: [p=0.1] a onda não passa. [p=0.3] {b}Micro-ondas não ionizam. [p=0.2] {c}Desligou o forno, a onda acabou: nada fica na comida. [p=0.3] {d}O celular emite micro-ondas bem mais fracas, [p=0.1] e também não ionizam."),
    # infravermelho
    dict(id="s07", block="infra", text="{a}O infravermelho é o que a pele sente como calor do Sol e da brasa. [p=0.2] Todo corpo quente emite infravermelho: [p=0.1] {b}a câmera térmica enxerga as pessoas no escuro. [p=0.3] E {c}o controle remoto da televisão pisca em infravermelho, [p=0.1] {d}uma luz que o olho não vê, mas muitas câmeras de celular mostram."),
    # visível e ultravioleta
    dict(id="s08", block="ultra", text="{a}A luz visível é a faixa que o olho percebe: [p=0.1] lâmpadas, telas, laser. [p=0.3] Logo acima dela vem {b}o ultravioleta do Sol. [p=0.2] Em excesso, {c}ele queima a pele e pode causar câncer de pele. [p=0.3] {d}O protetor solar barra ou absorve o ultravioleta antes que ele chegue à pele."),
    dict(id="s09", block="ultra", text="O ultravioleta também {a}mata micróbios: [p=0.1] {b}lâmpadas de ultravioleta limpam a água e o material de hospital. [p=0.3] E {c}é ele que faz brilhar os desenhos escondidos nas notas de dinheiro, [p=0.1] sob a luz negra."),
    # raios X e gama
    dict(id="s10", block="xgama", text="{a}Os raios X atravessam a pele e os músculos, [p=0.1] mas {b}são barrados pelos ossos, [p=0.1] que têm muito cálcio, um átomo com mais prótons. [p=0.3] {c}Na imagem, o osso fica claro: ali o raio não chegou. [p=0.3] {d}Os raios X ionizam: [p=0.1] por isso, o exame é rápido, a dose, que é a quantidade de radiação recebida, é pequena, [p=0.1] e {e}o avental de chumbo protege o resto do corpo."),
    dict(id="s11", block="xgama", text="{a}Os raios gama saem do núcleo de alguns átomos, na radioatividade, assunto de outra aula. [p=0.2] São os mais ionizantes. [p=0.2] {b}Na radioterapia, eles destroem células do câncer. [p=0.2] {c}E esterilizam alimentos e material de hospital, [p=0.1] sem deixar nada radioativo."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: {a}achar que toda radiação é perigosa do mesmo jeito. [p=0.2] {b}Radiação é o nome de todas, do rádio ao gama. [p=0.3] {c}O perigo de danificar as células vem das ionizantes. [p=0.2] {d}O forno e o celular usam micro-ondas, que não ionizam."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}ponha a luz visível no meio do espectro. [p=0.3] {b}Abaixo dela, rádio, micro-ondas e infravermelho [p=0.1] comunicam e aquecem. [p=0.2] {c}Acima, ultravioleta, raios X e gama [p=0.1] esterilizam, atravessam e ionizam. [p=0.2] Funciona porque o risco sobe junto com a frequência. [p=0.3] {d}Só tome cuidado com o ultravioleta mais fraco: [p=0.1] ele não ioniza, [p=0.1] mas ainda queima a pele e pode causar câncer."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Ligue cada situação a uma radiação. [p=0.2] {a}Um: o controle remoto da televisão. [p=0.1] {b}Dois: a radiografia do braço quebrado. [p=0.1] {c}Três: o protetor solar. [p=0.1] {d}Quatro: o forno que esquenta a pizza. [p=0.3] {e}E diga: qual delas ioniza?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Controle remoto: infravermelho. [p=0.2] {b}Radiografia: raios X. [p=0.2] {c}Protetor solar: ultravioleta. [p=0.2] {d}Forno: micro-ondas. [p=0.3] {e}Quem ioniza é só o raio X. [p=0.2] O ultravioleta que chega à pele não ioniza, mas queima. [p=0.2] {f}O controle e o forno também não ionizam."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}rádio e micro-ondas comunicam, [p=0.1] {b}infravermelho é calor e controle remoto, [p=0.1] {c}ultravioleta queima e esteriliza, [p=0.1] {d}raios X e gama atravessam e ionizam."),
    dict(id="s18", block="fim", text="Na próxima aula, você pratica: [p=0.2] {a}reconhecer a radiação de cada situação [p=0.1] e {b}calcular a frequência e o lambda. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
