# Estudativo · FIS-MOD-006 — Semicondutores e transistores (Física · Física Moderna · Quantização, dualidade e relatividade).
# Habilidade: explicar a dopagem, o diodo que conduz num sentido só e o transistor como chave.
# Pré-requisitos: FIS-ELE-010 (R = ρ·L/A, resistividade), QUI-ATO-006 (camada de valência). Próxima: FIS-MOD-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# Fatos: silício tem 4 elétrons na camada de valência; fósforo e arsênio, 5 (tipo n); boro, 3 (tipo p). Dopagem típica:
# ordem de um átomo em um milhão (varia de 10⁻⁸ a 10⁻³). Transistor: Bell Labs, 1947 (Bardeen, Brattain e Shockley).
# Celulares atuais têm mais de dez bilhões de transistores no processador. Diodo: conduz do p para o n (polarização direta).
# Sentido da corrente: o convencional, de FIS-ELE-008 (do + para o −, por fora da pilha).

TITULO = "Semicondutores e transistores"

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
    dict(id="s01", block="gancho", text="{a}O processador do seu celular tem mais de dez bilhões de chaves minúsculas, [p=0.2] {b}ligando e desligando bilhões de vezes por segundo. [p=0.3] {c}E elas são feitas de silício, [p=0.1] o elemento que está na areia."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai explicar a dopagem, [p=0.2] {b}o diodo, que só deixa a corrente passar num sentido, [p=0.2] e {c}o transistor, que funciona como chave."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a resistividade, rô, diz o quanto um material atrapalha a corrente; [p=0.2] e {c}os elétrons da camada de valência, a última camada do átomo. [p=0.3] Se faltar alguma, procure no canal."),
    # condutor, isolante, semicondutor
    dict(id="s04", block="materiais", text="{a}No metal, sobram elétrons livres para andar: [p=0.1] a resistividade é baixa, e ele é {b}condutor. [p=0.3] {c}Na borracha, quase nenhum elétron anda: [p=0.1] resistividade enorme, {d}isolante. [p=0.3] {e}No meio do caminho fica o semicondutor, [p=0.2] e o mais usado é {f}o silício."),
    dict(id="s05", block="materiais", text="{a}O silício tem quatro elétrons na camada de valência. [p=0.2] {b}No cristal, cada átomo divide esses quatro com quatro vizinhos. [p=0.3] {c}Todo mundo fica preso nessas ligações, [p=0.2] e {d}sobram pouquíssimos elétrons livres. [p=0.2] Por isso, o silício puro conduz mal."),
    # dopagem
    dict(id="s06", block="dopagem", text="O truque é a {a}dopagem: [p=0.2] misturar ao silício {b}pouquíssimos átomos de outro elemento, [p=0.1] coisa de um para cada milhão. [p=0.3] {c}Se o átomo tem cinco elétrons na valência, como o fósforo, [p=0.2] {d}quatro entram nas ligações, e {e}um sobra livre. [p=0.3] {f}Sobra elétron, que é negativo: [p=0.1] {g}é o silício tipo ene."),
    dict(id="s07", block="dopagem", text="{a}Se o átomo tem três elétrons, como o boro, [p=0.2] {b}falta um para fechar as ligações. [p=0.3] {c}Fica um buraco, que se chama lacuna. [p=0.2] {d}Um elétron vizinho pula para a lacuna, e a lacuna anda no sentido contrário ao do elétron, [p=0.2] {e}como uma carga positiva andando. [p=0.3] {f}É o silício tipo pê."),
    # diodo
    dict(id="s08", block="diodo", text="Agora, junte um pedaço pê com um pedaço ene. [p=0.2] Isso é {a}o diodo. [p=0.3] {b}Ligue o pê no positivo da pilha e o ene no negativo: [p=0.2] {c}a corrente passa. [p=0.3] {d}Inverta a pilha: [p=0.2] {e}a corrente para. [p=0.3] {f}O diodo é uma rua de mão única para a corrente."),
    dict(id="s09", block="diodo", text="{a}No desenho do circuito, o diodo é uma seta com uma barra. [p=0.2] {b}A seta aponta o sentido em que a corrente passa, [p=0.1] {c}e a barra marca o lado ene. [p=0.3] {d}A lâmpada de LED é um diodo que solta luz quando a corrente passa."),
    # transistor
    dict(id="s10", block="transistor", text="{a}Agora, três camadas: ene, pê, ene. [p=0.2] Isso é {b}o transistor. [p=0.3] {c}Entre as duas pontas, a corrente principal só passa se chegar {d}uma corrente pequena na camada do meio, a base. [p=0.3] {e}Sem corrente na base, a chave fica aberta, como um interruptor desligado: nada passa. [p=0.1] {f}Com corrente na base, a chave fecha."),
    dict(id="s11", block="transistor", text="{a}Uma corrente pequena controla uma grande: [p=0.2] o transistor também {b}amplifica, como no rádio. [p=0.3] {c}E chave aberta e chave fechada são o zero e o um do computador. [p=0.3] {d}O transistor foi inventado em mil novecentos e quarenta e sete, nos Estados Unidos. [p=0.2] {e}Hoje, bilhões deles cabem num chip do tamanho de uma unha."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}achar que o silício tipo pê tem carga positiva. [p=0.3] {b}Não tem. [p=0.2] {c}Cada átomo de boro é neutro: tem tantos elétrons quanto prótons. [p=0.2] {d}Então o cristal continua neutro. [p=0.3] {e}O pê e o ene dizem quem carrega a corrente: [p=0.2] {f}a lacuna, que anda como positiva, [p=0.1] {g}ou o elétron livre, que é negativo."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}conte os elétrons da valência do dopante e compare com os quatro do silício. [p=0.3] {b}Cinco é um a mais: sobra elétron, tipo ene. [p=0.2] {c}Três é um a menos: falta elétron, tipo pê. [p=0.3] {d}Funciona com qualquer elemento, até os que você nunca viu na prova."),
    dict(id="s14", block="atalho", text="{a}E para o diodo: siga a seta do símbolo. [p=0.2] {b}Saia do positivo da pilha e siga o fio: [p=0.1] se você chega pela base da seta, a corrente passa; [p=0.1] se chega pela barra, para. [p=0.3] {c}Não basta quando há vários diodos: [p=0.1] {d}aí, siga o caminho da corrente um por um."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}O arsênio tem cinco elétrons na camada de valência. [p=0.2] {b}Silício dopado com arsênio é tipo pê ou tipo ene? [p=0.3] E {c}num circuito com pilha, diodo e lâmpada, [p=0.1] {d}o lado pê do diodo está ligado ao negativo da pilha. [p=0.2] {e}A lâmpada acende?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Cinco elétrons, um a mais que o silício: [p=0.2] {b}sobra elétron livre, tipo ene."),
    dict(id="s18", block="resposta", text="{a}O diodo só conduz com o pê no positivo. [p=0.2] {b}Aqui, o pê está no negativo: [p=0.2] {c}a corrente para, [p=0.1] {d}e a lâmpada fica apagada. [p=0.3] {e}Vire a pilha, e ela acende."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}cinco elétrons no dopante dão tipo ene, três dão tipo pê; [p=0.2] {b}o diodo conduz só do pê para o ene; [p=0.2] e {c}no transistor, uma corrente pequena na base liga e desliga a corrente grande."),
    dict(id="s20", block="fim", text="Na próxima aula, {a}você pratica a Física Moderna inteira: [p=0.2] {b}fóton, efeito fotoelétrico, espectros e relatividade, em questões. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
