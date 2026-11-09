# Estudativo · FIS-OND-012 — Praticando: espectro eletromagnético (Física · Ondas e Som · Espectro eletromagnético · prática).
# Habilidade: identificar a radiação de cada situação e calcular frequência e comprimento de onda.
# Pré-requisitos: FIS-OND-010, 011. Próxima: nenhuma (última aula da trilha Ondas e Som).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Prática: cinco questões inéditas, criadas para esta aula. Wi-fi 2,4 GHz → λ = 0,125 m; verde 500 nm → f = 6 × 10¹⁴ Hz;
# luz azul de 7,5 × 10¹⁴ Hz → λ = 4 × 10⁻⁷ m = 400 nm (limite do violeta, ainda visível).

TITULO = "Praticando: espectro eletromagnético"

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
    dict(id="s01", block="gancho", text="Questão de espectro pede {a}uma de duas coisas: [p=0.2] {b}o nome da radiação da situação, [p=0.2] ou {c}uma conta com cê igual a lambda vezes efe. [p=0.3] {d}Até o fim desta aula, você vai resolver cinco questões dos dois tipos."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar as aulas deste módulo: [p=0.2] {a}a ordem do espectro, com cê igual a três vezes dez elevado a oito metros por segundo; [p=0.2] {b}e o uso e o risco de cada faixa. [p=0.3] Se faltar alguma, procure no canal."),
    # método
    dict(id="s03", block="metodo", text="Primeiro, o método: [p=0.1] {a}procure a pista na situação. [p=0.2] {b}Comunicação ou forno: rádio ou micro-ondas. [p=0.1] {c}Calor ou controle remoto: infravermelho. [p=0.1] {d}Pele queimada ou esterilização: ultravioleta. [p=0.1] {e}Atravessa o corpo: raios X. [p=0.1] {f}Núcleo de átomo, como na fonte de cobalto da radioterapia: gama. [p=0.3] {g}Na conta, divida cê pelo que a questão der."),
    # questão 1
    dict(id="s04", block="q1", text="Questão um. [p=0.2] {a}Um roteador de wi-fi trabalha em dois vírgula quatro gigahertz. [p=0.1] Giga é um bilhão. [p=0.3] {b}Qual é o lambda da onda? [p=0.2] {c}Pause e tente. [p=3.0]"),
    dict(id="s05", block="q1", text="{a}Dois vírgula quatro gigahertz são dois vírgula quatro vezes dez elevado a nove hertz. [p=0.2] {b}Três dividido por dois vírgula quatro: um vírgula vinte e cinco. [p=0.2] {c}Dez elevado a oito, dividido por dez elevado a nove: dez elevado a menos um. [p=0.3] {d}Isso dá doze centímetros e meio. [p=0.2] {e}Lambda de centímetros: micro-ondas, como no forno."),
    # questão 2
    dict(id="s06", block="q2", text="Questão dois. [p=0.2] {a}Uma luz verde tem lambda de quinhentos nanômetros. [p=0.1] Nano é um bilionésimo: [p=0.1] {b}cinco vezes dez elevado a menos sete metro. [p=0.3] {c}Qual é a frequência? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s07", block="q2", text="{a}Três dividido por cinco: zero vírgula seis. [p=0.2] {b}Dividir por dez elevado a menos sete é multiplicar por dez elevado a sete: [p=0.1] oito mais sete, quinze. [p=0.1] {c}Zero vírgula seis vezes dez elevado a quinze. [p=0.3] {d}Em notação científica, seis vezes dez elevado a catorze hertz: [p=0.1] a vírgula andou uma casa, e o expoente perdeu um."),
    # questão 3
    dict(id="s08", block="q3", text="Questão três. [p=0.2] Diga a radiação de cada situação. [p=0.2] {a}Um: a câmera que mostra as pessoas no escuro pelo calor do corpo. [p=0.2] {b}Dois: a lâmpada que mata bactérias na água de um aquário. [p=0.2] {c}Três: a fonte de cobalto radioativo que destrói um tumor na radioterapia. [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s09", block="q3", text="{a}Calor do corpo: infravermelho. [p=0.2] {b}Mata bactérias: ultravioleta. [p=0.2] {c}Fonte de cobalto: raios gama, que saem do núcleo. [p=0.3] {d}O primeiro não ioniza; [p=0.1] o terceiro, sim."),
    # questão 4
    dict(id="s10", block="q4", text="Questão quatro. [p=0.2] {a}Compare, no vácuo, as micro-ondas e os raios X. [p=0.3] {b}Qual tem a maior velocidade? [p=0.1] {c}A maior frequência? [p=0.1] {d}O maior lambda? [p=0.2] {e}Pause e tente. [p=3.0]"),
    dict(id="s11", block="q4", text="{a}Velocidade: a mesma, cê, para as duas. [p=0.2] {b}Frequência: o raio X vem depois no espectro, tem a maior. [p=0.2] {c}Lambda: vai ao contrário, maior nas micro-ondas. [p=0.3] {d}Quem marca raio X mais rápido cai na pegadinha."),
    # questão 5
    dict(id="s12", block="q5", text="Questão cinco. [p=0.2] {a}Um laser emite luz com frequência de sete vírgula cinco vezes dez elevado a catorze hertz. [p=0.3] {b}Qual é o lambda, em nanômetros? [p=0.2] {c}E esse laser é visível? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s13", block="q5", text="{a}Três dividido por sete vírgula cinco: zero vírgula quatro. [p=0.2] {b}Oito menos catorze: menos seis. [p=0.1] {c}Zero vírgula quatro vezes dez elevado a menos seis: [p=0.1] quatro vezes dez elevado a menos sete metro. [p=0.3] {d}São quatrocentos nanômetros, [p=0.1] {e}a ponta violeta da luz visível. [p=0.2] Um pouco mais de frequência, e já seria ultravioleta."),
    # fechamento
    dict(id="s14", block="fim", text="Resumindo: {a}para reconhecer, procure a pista do uso; [p=0.2] {b}para calcular, divida cê pelo dado, com cuidado nos expoentes. [p=0.3] {c}Com esta aula, você fechou a trilha de ondas: do pêndulo ao raio gama. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
