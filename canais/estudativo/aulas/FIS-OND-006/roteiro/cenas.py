# Estudativo · FIS-OND-006 — Som: altura, intensidade e timbre (Física · Ondas e Som · Som e efeito Doppler).
# Habilidade: separar grave de fraco, usar decibéis, com 10 dB a mais valendo 10 vezes a intensidade, e dizer por que dois instrumentos soam diferentes.
# Pré-requisitos: FIS-OND-002 (v = λ·f, amplitude), MAT-EXP-014 (escala de decibéis). Próxima: FIS-OND-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Lá do afinador = 440 Hz. 10·log 2 ≈ 3 dB (MAT-EXP-009 em "Já ensinado").
# Harmônicos são da FIS-OND-007: aqui só citados como "assunto da próxima aula". Valores de dB típicos: conversa 60, trânsito 80.

TITULO = "Som: altura, intensidade e timbre"

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
    dict(id="s01", block="gancho", text="{a}Você abaixa o volume do celular [p=0.1] e diz que o som ficou {b}mais baixo. [p=0.3] Para a Física, {c}não ficou. [p=0.2] Ficou {d}mais fraco. [p=0.3] Na Física, {e}som alto é som agudo, como um apito."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai separar {b}grave de fraco, [p=0.2] usar {c}os decibéis [p=0.1] e dizer {d}por que um violão e um piano soam diferentes na mesma nota."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}amplitude, lambda e frequência de uma onda; [p=0.2] e {c}a escala de decibéis, em que dez a mais vale dez vezes mais. [p=0.3] Se faltar alguma, procure no canal."),
    # som
    dict(id="s04", block="som", text="O som é {a}uma onda mecânica e longitudinal: [p=0.2] o ar é empurrado e puxado, para a frente e para trás. [p=0.2] No ar, ele anda a cerca de {b}trezentos e quarenta metros por segundo. [p=0.3] O ouvido humano escuta de {c}vinte hertz [p=0.1] a {d}vinte mil hertz. [p=0.2] {e}Abaixo disso é infrassom. [p=0.1] {f}Acima, ultrassom, como o do exame de ultrassonografia."),
    # altura
    dict(id="s05", block="altura", text="A primeira qualidade do som é {a}a altura. [p=0.2] Ela depende {b}só da frequência. [p=0.3] {c}Frequência alta: som agudo, ou alto. [p=0.2] {d}Frequência baixa: som grave, ou baixo. [p=0.3] {e}O apito é agudo; [p=0.1] {f}o bumbo é grave."),
    dict(id="s06", block="altura", text="Na música, cada nota é uma frequência. [p=0.2] {a}O lá do afinador tem quatrocentos e quarenta hertz. [p=0.2] {b}Dobre a frequência, oitocentos e oitenta hertz: [p=0.1] é o mesmo lá, mais agudo."),
    # intensidade
    dict(id="s07", block="intensidade", text="A segunda é {a}a intensidade: [p=0.2] o som forte ou fraco, que o botão de volume muda. [p=0.3] Ela depende {b}da amplitude da onda: [p=0.2] {c}onda mais alta no desenho, som mais forte."),
    dict(id="s08", block="intensidade", text="O nível do som é medido em {a}decibéis, com o símbolo dê bê. [p=0.2] É uma escala de logaritmo: [p=0.2] {b}cada dez decibéis a mais, a intensidade fica dez vezes maior. [p=0.3] {c}Conversa: sessenta decibéis. [p=0.1] {d}Trânsito pesado: oitenta. [p=0.2] São vinte decibéis a mais: [p=0.1] {e}dez vezes dez, cem vezes mais intenso."),
    dict(id="s09", block="intensidade", text="{a}Quando a prova dá a fórmula, ela é esta: [p=0.2] {b}o nível em decibéis é dez vezes o logaritmo de i dividido por i zero. [p=0.2] {c}I é a intensidade do som que chega ao ouvido, [p=0.1] e i zero, a do som mais fraco que se ouve, o de zero decibel. [p=0.2] A unidade de i é assunto de outra aula. [p=0.3] Mas {d}a regra do dez resolve quase tudo."),
    # timbre
    dict(id="s10", block="timbre", text="A terceira é {a}o timbre. [p=0.2] Um violão e um piano tocam {b}a mesma nota, com a mesma força. [p=0.2] Mesma frequência, mesma intensidade, [p=0.1] e mesmo assim você sabe quem é quem. [p=0.3] {c}O que muda é o formato da onda."),
    dict(id="s11", block="timbre", text="A corda do violão não vibra numa onda só. [p=0.2] {a}Junto da frequência principal, vêm outras mais agudas, os harmônicos. [p=0.2] {b}A mistura de cada instrumento é diferente, [p=0.1] e o desenho da onda também. [p=0.2] {c}Esse desenho é o timbre. [p=0.2] Os harmônicos são assunto da próxima aula."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: {a}somar decibéis como se fossem intensidade. [p=0.2] Uma máquina faz oitenta decibéis. [p=0.2] {b}Duas máquinas iguais não fazem cento e sessenta. [p=0.3] {c}O dobro da intensidade dá só uns três decibéis a mais: [p=0.1] {d}cerca de oitenta e três. [p=0.2] Cento e sessenta seria cem milhões de vezes a intensidade de uma máquina só."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}conte as dezenas de decibéis. [p=0.2] {b}Cada dez a mais é um zero a mais na intensidade. [p=0.3] {c}De sessenta para noventa, são três dezenas: [p=0.1] {d}mil vezes. [p=0.3] Funciona porque a escala é um logaritmo de base dez. [p=0.2] {e}Não compensa quando a diferença não é múltiplo de dez, como sete decibéis: [p=0.1] aí, use a fórmula do enunciado."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Um show chega a cento e dez decibéis, [p=0.1] e uma conversa, a sessenta. [p=0.2] {b}Quantas vezes o som do show é mais intenso? [p=0.3] {c}E se a cantora passa de uma nota de duzentos e vinte hertz para uma de quatrocentos e quarenta, [p=0.1] o som fica mais forte ou mais agudo?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Cento e dez menos sessenta: cinquenta decibéis. [p=0.2] {b}São cinco dezenas: um seguido de cinco zeros. [p=0.2] {c}Cem mil vezes mais intenso. [p=0.3] {d}E a frequência dobrou: [p=0.1] {e}o som fica mais agudo, não mais forte. [p=0.2] A força depende da amplitude, não da frequência."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}altura é frequência: agudo ou grave; [p=0.2] {b}intensidade é amplitude: forte ou fraco, em decibéis; [p=0.2] e {c}timbre é o formato da onda."),
    dict(id="s18", block="fim", text="Na próxima aula, você vai ver de onde vêm {a}os harmônicos: [p=0.2] {b}nas cordas, {c}nos tubos [p=0.1] e na {d}ressonância, que faz uma taça quebrar com a voz. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
