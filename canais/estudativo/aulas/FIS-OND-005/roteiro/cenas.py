# Estudativo · FIS-OND-005 — Praticando: ondas e seus fenômenos (Física · Ondas e Som · Ondas e seus fenômenos · prática).
# Habilidade: calcular com v = λ·f e reconhecer cada fenômeno ondulatório descrito em uma situação.
# Pré-requisitos: FIS-OND-001, 002, 003, 004. Próxima: FIS-OND-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Prática: cinco questões inéditas, criadas para esta aula. Corda fina: onda mais rápida que na grossa (mesma tração).
# Rádio atrás do morro: λ de rádio vai de metros (FM) a centenas de metros (AM).

TITULO = "Praticando: ondas e seus fenômenos"

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
    dict(id="s01", block="gancho", text="Questão de ondas quase sempre pede {a}uma de duas coisas: [p=0.2] {b}uma conta com vê igual a lambda vezes efe, [p=0.2] ou {c}o nome do fenômeno. [p=0.3] {d}Até o fim desta aula, você vai resolver cinco questões dos dois tipos."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar as aulas deste módulo: [p=0.2] {a}pêndulo e mola, [p=0.1] {b}a equação da onda, [p=0.1] {c}reflexão, refração e difração, [p=0.1] {d}e interferência e polarização. [p=0.3] Se faltar alguma, procure no canal."),
    # método
    dict(id="s03", block="metodo", text="Primeiro, o método. [p=0.2] Diante de uma situação, pergunte {a}o que a onda fez. [p=0.2] {b}Voltou? Reflexão. [p=0.2] {c}Trocou de meio? Refração, e a frequência fica. [p=0.2] {d}Contornou ou se espalhou? Difração. [p=0.2] {e}Encontrou outra onda? Interferência. [p=0.3] E na conta, {f}a frequência é da fonte, e a velocidade é do meio."),
    # questão 1
    dict(id="s04", block="q1", text="Questão um. [p=0.2] {a}Um relógio de pêndulo está atrasando: [p=0.1] {b}cada ida e volta demora mais do que devia. [p=0.3] {c}O que resolve: trocar a bola por uma mais pesada, [p=0.1] alongar o fio [p=0.1] ou encurtar o fio? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s05", block="q1", text="{a}A massa não entra no período do pêndulo: [p=0.1] trocar a bola não adianta. [p=0.2] {b}O período cresce com o comprimento do fio. [p=0.2] Para diminuir o período, {c}encurte o fio. [p=0.3] {d}E, para cortar o período pela metade, o fio teria que ficar com um quarto do tamanho."),
    # questão 2
    dict(id="s06", block="q2", text="Questão dois. [p=0.2] {a}No mar, três cristas seguidas ocupam doze metros. [p=0.2] {b}Uma boia sobe e desce com período de dois segundos. [p=0.3] {c}Qual é a velocidade da onda? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s07", block="q2", text="{a}Da primeira à terceira crista, são dois lambdas: [p=0.1] {b}lambda é seis metros. [p=0.3] {c}Período de dois segundos: [p=0.1] efe é um dividido por dois, meio hertz. [p=0.2] {d}Seis vezes zero vírgula cinco: três metros por segundo. [p=0.3] {e}Ou direto: lambda dividido por tê, seis dividido por dois."),
    # questão 3
    dict(id="s08", block="q3", text="Questão três. [p=0.2] {a}Uma onda passa de uma corda grossa para uma fina, [p=0.1] onde anda duas vezes mais rápido. [p=0.2] {b}Na grossa, a frequência é de dez hertz, e o lambda, de quarenta centímetros. [p=0.3] {c}E na corda fina? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s09", block="q3", text="{a}Trocou de meio: refração. [p=0.2] {b}A frequência fica: dez hertz. [p=0.2] {c}A velocidade dobrou, então o lambda dobra: oitenta centímetros. [p=0.3] {d}Conferindo: zero vírgula quatro vezes dez, quatro metros por segundo na grossa; [p=0.1] zero vírgula oito vezes dez, oito na fina. [p=0.1] O dobro."),
    # questão 4
    dict(id="s10", block="q4", text="Questão quatro. [p=0.2] Diga o fenômeno de cada situação. [p=0.2] {a}Um: o morcego acha o inseto pelo eco do som que ele mesmo emite. [p=0.2] {b}Dois: o rádio do carro continua pegando atrás de um morro. [p=0.2] {c}Três: no lago, as ondas mudam de direção ao chegar à parte rasa. [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s11", block="q4", text="{a}O eco é a onda que volta: reflexão. [p=0.2] {b}A onda de rádio contorna o morro: difração. [p=0.1] O lambda dela é grande, de metros a centenas de metros. [p=0.3] {c}A onda mudou de velocidade e de direção: refração."),
    # questão 5
    dict(id="s12", block="q5", text="Questão cinco. [p=0.2] {a}Duas fontes, juntas, fazem ondas de quatro centímetros de lambda num tanque. [p=0.2] {b}Um ponto P está a vinte centímetros de uma fonte e a vinte e seis da outra. [p=0.3] {c}Ali, a água balança muito ou fica parada? [p=0.2] {d}Pause e tente. [p=3.0]"),
    dict(id="s13", block="q5", text="{a}A diferença é vinte e seis menos vinte: seis centímetros. [p=0.2] {b}Meio lambda, dois centímetros. [p=0.2] {c}Seis dividido por dois, três: ímpar. [p=0.3] {d}Interferência destrutiva: em P, a água quase não balança."),
    # fechamento
    dict(id="s14", block="fim", text="Resumindo: {a}na conta, vê igual a lambda vezes efe, com a frequência presa à fonte; [p=0.2] {b}no fenômeno, olhe o que a onda fez."),
    dict(id="s15", block="fim", text="Na próxima aula, a onda vira {c}som: [p=0.2] {d}grave e agudo, forte e fraco, e o timbre de cada instrumento. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
