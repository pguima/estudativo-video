# Estudativo · FIS-CIN-005 — Movimento uniforme: a função horária (Física · Cinemática · Movimento uniforme e variado).
# Habilidade: escrever s = s0 + v·t, entendendo cada letra, e achar posição ou tempo em trajetos com velocidade constante.
# Pré-requisitos: FIS-CIN-004 (posição e deslocamento), MAT-RAZ-016 (km/h ↔ m/s com 3,6), MAT-FUN-010 (valor inicial e taxa). Próxima: FIS-CIN-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. "sorvete" é o apelido de sala de aula de s = s0 + vt.

TITULO = "Movimento uniforme: a função horária"

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
    dict(id="s01", block="gancho", text="{a}Um carro passa pelo quilômetro vinte de uma estrada, [p=0.2] sempre a {b}oitenta quilômetros por hora. [p=0.3] Onde ele estará {c}três horas depois? [p=0.3] {d}No quilômetro duzentos e quarenta? [p=0.3] {e}Não. [p=0.2] No duzentos e sessenta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai escrever a fórmula que dá a posição em qualquer instante, [p=0.2] e achar {b}a posição [p=0.1] ou {c}o tempo, sem errar."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}deslocamento, a posição final menos a inicial; [p=0.2] {c}a função afim, com o valor inicial e a taxa de variação; [p=0.2] e {d}passar de quilômetro por hora para metro por segundo, dividindo por três vírgula seis. [p=0.3] Se faltar alguma, procure no canal."),
    # MU
    dict(id="s04", block="mu", text="Movimento uniforme é o movimento com {a}velocidade constante: [p=0.2] o corpo anda {b}distâncias iguais em tempos iguais. [p=0.3] {c}A oitenta quilômetros por hora, são oitenta quilômetros em cada hora: [p=0.2] {d}oitenta, cento e sessenta, duzentos e quarenta."),
    dict(id="s05", block="mu", text="Então, em três horas, o carro {a}anda duzentos e quarenta. [p=0.2] Mas ele {b}não saiu do zero: saiu do quilômetro vinte. [p=0.3] {c}Vinte mais duzentos e quarenta: quilômetro duzentos e sessenta. [p=0.3] {d}Duzentos e quarenta é o quanto ele andou. [p=0.1] {e}Duzentos e sessenta é onde ele está."),
    # fórmula
    dict(id="s06", block="formula", text="Essa conta vira a função horária: [p=0.2] {a}esse igual a esse zero mais vê tê. [p=0.3] {b}Esse é a posição no instante tê. [p=0.2] {c}Esse zero é a posição inicial, quando o cronômetro marca zero. [p=0.2] {d}Vê é a velocidade, [p=0.1] e {e}tê é o tempo. [p=0.3] No Sistema Internacional: {f}metro, metro por segundo e segundo."),
    dict(id="s07", block="formula", text="Repare: {a}vê vezes tê é o quanto o corpo andou. [p=0.2] {b}A posição é onde ele começou, mais o que andou. [p=0.3] Para decorar, leia as letras em voz alta: [p=0.2] {c}esse, esse zero, vê, tê: sorvete."),
    dict(id="s08", block="formula", text="{a}É uma função afim, como efe de xis igual a bê mais á xis. [p=0.2] {b}O esse zero é o valor inicial: o número sozinho. [p=0.2] {c}O vê é a taxa de variação: o número colado no tê. [p=0.3] {d}Em esse igual a dez mais cinco tê, [p=0.2] o corpo começa na posição dez metros e anda a cinco metros por segundo."),
    # tempo
    dict(id="s09", block="tempo", text="E para achar o tempo? [p=0.2] Volte ao carro: {a}esse igual a vinte mais oitenta tê, em quilômetros e horas. [p=0.2] Quando ele chega ao {b}quilômetro trezentos e quarenta? [p=0.3] {c}Troque o esse por trezentos e quarenta. [p=0.2] {d}Tire vinte dos dois lados: trezentos e vinte igual a oitenta tê. [p=0.2] {e}Divida por oitenta: quatro horas."),
    dict(id="s10", block="tempo", text="E se o corpo anda {a}no sentido em que as posições diminuem? [p=0.2] Aí a velocidade é {b}negativa, [p=0.1] e o movimento se chama {c}retrógrado. [p=0.3] Quando as posições aumentam, ele é {d}progressivo. [p=0.3] {e}Em esse igual a cem menos cinco tê, [p=0.1] o corpo sai da posição cem metros e volta cinco metros a cada segundo."),
    dict(id="s11", block="tempo", text="Ele passa pela origem quando {a}o esse vale zero: [p=0.2] {b}zero igual a cem menos cinco tê. [p=0.2] {c}Cinco tê igual a cem: [p=0.2] {d}vinte segundos."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: {a}misturar unidades na fórmula. [p=0.3] Um ônibus parte da posição {b}cinquenta metros, a {c}cinquenta e quatro quilômetros por hora. [p=0.2] Onde ele está depois de {d}dez segundos? [p=0.3] Quem faz {e}cinquenta mais cinquenta e quatro vezes dez acha quinhentos e noventa. [p=0.2] Errado."),
    dict(id="s13", block="erro", text="{a}Cinquenta e quatro dividido por três vírgula seis dá quinze metros por segundo. [p=0.3] {b}Cinquenta mais quinze vezes dez: [p=0.2] {c}duzentos metros. [p=0.3] {d}Antes de usar a fórmula, deixe tudo nas mesmas unidades."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}a função horária já entrega as respostas sem conta. [p=0.2] {b}Número sozinho: posição inicial. [p=0.1] {c}Número colado no tê: velocidade. [p=0.1] {d}Sinal desse número: progressivo ou retrógrado. [p=0.3] {e}Em esse igual a oito menos três tê: começa em oito metros, [p=0.1] velocidade de menos três metros por segundo, [p=0.1] retrógrado."),
    dict(id="s15", block="atalho", text="Funciona porque {a}a fórmula tem sempre a mesma forma: [p=0.2] posição inicial mais velocidade vezes tempo. [p=0.3] {b}Se a prova escrever fora da ordem, como menos três tê mais oito, [p=0.2] o número colado no tê continua sendo a velocidade. [p=0.3] {c}Não serve se a velocidade muda: [p=0.1] aí a fórmula é outra, assunto de outra aula."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] A função horária de um ciclista é {a}esse igual a quarenta mais cinco tê, [p=0.1] em metros e segundos. [p=0.3] {b}Qual é a posição inicial? [p=0.1] E a velocidade, em metros por segundo e em quilômetros por hora? [p=0.2] {c}Em que instante ele passa pela posição cento e quarenta metros?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}O número sozinho, quarenta: posição inicial de quarenta metros. [p=0.2] {b}O número colado no tê, cinco: cinco metros por segundo, progressivo. [p=0.3] {c}Em quilômetros por hora, multiplique por três vírgula seis: dezoito."),
    dict(id="s19", block="resposta", text="Agora, {a}troque o esse por cento e quarenta. [p=0.2] {b}Tire quarenta dos dois lados: cem igual a cinco tê. [p=0.2] {c}Divida por cinco: vinte segundos."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}a posição é onde o corpo começou mais o que ele andou: [p=0.2] {b}esse igual a esse zero mais vê tê, [p=0.2] {c}com tudo nas mesmas unidades."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai descobrir {a}onde e quando dois carros se encontram, [p=0.2] {b}com uma conta de cabeça. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
