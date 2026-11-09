# Estudativo · FIS-CIN-006 — Encontro e ultrapassagem (Física · Cinemática · Movimento uniforme e variado).
# Habilidade: achar onde e quando dois móveis se encontram igualando as funções horárias ou, pelo atalho, somando ou subtraindo
# as velocidades, inclusive com trem e túnel.
# Pré-requisitos: FIS-CIN-005 (função horária), MAT-EQU-008 (letra dos dois lados). Próxima: FIS-CIN-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. "esse á" e "esse bê" = posição do móvel A e do móvel B.

TITULO = "Encontro e ultrapassagem"

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
    dict(id="s01", block="gancho", text="{a}Duas cidades ficam a trezentos quilômetros uma da outra. [p=0.2] {b}Ao mesmo tempo, um carro sai de uma a sessenta quilômetros por hora, [p=0.2] e {c}outro sai da outra a noventa, vindo de frente. [p=0.3] Em quanto tempo eles se encontram? [p=0.3] {d}Dá para responder de cabeça: duas horas."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai achar onde e quando dois corpos se encontram, [p=0.2] {b}pela fórmula [p=0.1] e {c}pelo atalho, [p=0.2] inclusive com {d}trem e túnel."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a função horária, esse igual a esse zero mais vê tê; [p=0.2] e {c}resolver equação com a letra dos dois lados. [p=0.3] Se faltar alguma, procure no canal."),
    # encontro de frente
    dict(id="s04", block="frente", text="Na Física, {a}móvel é qualquer corpo que se move. [p=0.2] E dois móveis se encontram quando estão {b}na mesma posição, [p=0.1] {c}no mesmo instante. [p=0.3] Então a regra é uma só: [p=0.2] {d}escreva a função de cada um e iguale as posições."),
    dict(id="s05", block="frente", text="Ponha a origem na primeira cidade, {a}com o sentido positivo para a outra. [p=0.2] {b}O carro A sai do zero a sessenta: [p=0.1] esse á igual a sessenta tê. [p=0.3] {c}O carro B sai do quilômetro trezentos e vem no sentido contrário, então a velocidade dele é negativa: [p=0.2] esse bê igual a trezentos menos noventa tê."),
    dict(id="s06", block="frente", text="{a}Iguale: sessenta tê igual a trezentos menos noventa tê. [p=0.2] {b}Some noventa tê aos dois lados: cento e cinquenta tê igual a trezentos. [p=0.2] {c}Tê igual a duas horas. [p=0.3] E onde? [p=0.1] Ponha o tempo em qualquer uma das funções: [p=0.2] {d}sessenta vezes dois, quilômetro cento e vinte."),
    # perseguição
    dict(id="s07", block="atras", text="Agora, {a}no mesmo sentido. [p=0.2] Um caminhão anda a {b}oitenta quilômetros por hora. [p=0.2] {c}Um carro está sessenta quilômetros atrás dele, a cem. [p=0.3] Quando o carro alcança o caminhão? [p=0.2] Alcançar é o começo da ultrapassagem."),
    dict(id="s08", block="atras", text="Ponha a origem onde o carro está. [p=0.2] {a}Carro: esse igual a cem tê. [p=0.1] {b}Caminhão: esse igual a sessenta mais oitenta tê. [p=0.3] {c}Iguale e tire oitenta tê dos dois lados: vinte tê igual a sessenta. [p=0.2] {d}Três horas. [p=0.2] {e}Onde? Cem vezes três: trezentos quilômetros de onde o carro estava."),
    # trem e túnel
    dict(id="s09", block="trem", text="E quando o tamanho do móvel conta? [p=0.2] {a}Um trem de duzentos metros [p=0.1] atravessa {b}um túnel de quatrocentos, [p=0.1] a {c}vinte metros por segundo. [p=0.3] Atravessar é {d}da frente do trem entrar até a traseira sair."),
    dict(id="s10", block="trem", text="Siga a traseira do trem. [p=0.2] {a}Ela precisa andar o túnel inteiro [p=0.1] {b}mais o próprio trem: seiscentos metros. [p=0.3] {c}Seiscentos dividido por vinte: trinta segundos."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: {a}esquecer o comprimento do trem. [p=0.3] {b}Quatrocentos dividido por vinte dá vinte segundos. [p=0.2] Nesse instante, {c}a frente está saindo, [p=0.1] mas {d}o trem inteiro ainda está dentro do túnel."),
    # atalho
    dict(id="s12", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}a velocidade relativa. [p=0.2] {b}Sentidos opostos, um indo na direção do outro: some as velocidades. [p=0.2] {c}Mesmo sentido, subtraia. [p=0.3] {d}O tempo de encontro é a distância entre eles dividida por essa velocidade."),
    dict(id="s13", block="atalho", text="Nas cidades: {a}sessenta mais noventa, cento e cinquenta. [p=0.2] {b}Trezentos dividido por cento e cinquenta: duas horas. [p=0.3] No caminhão: {c}cem menos oitenta, vinte. [p=0.2] {d}Sessenta dividido por vinte: três horas. [p=0.3] Os mesmos resultados, sem montar equação."),
    dict(id="s14", block="atalho", text="Funciona porque {a}é como olhar de dentro de um dos móveis: [p=0.2] é a ideia de referencial. [p=0.2] De dentro do caminhão, {b}o carro se aproxima a só vinte quilômetros por hora. [p=0.3] {c}Não compensa quando os móveis saem em instantes diferentes: [p=0.2] aí, monte as funções."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Numa pista reta, a ciclista A está na posição {a}zero, a oito metros por segundo. [p=0.2] O ciclista B está na posição {b}cento e vinte metros, a cinco metros por segundo, no mesmo sentido. [p=0.3] {c}Quando e onde A alcança B?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Esse á igual a oito tê. [p=0.1] {b}Esse bê igual a cento e vinte mais cinco tê. [p=0.2] {c}Iguale e tire cinco tê: três tê igual a cento e vinte. [p=0.2] {d}Quarenta segundos."),
    dict(id="s18", block="resposta", text="Onde? {a}Oito vezes quarenta: na posição trezentos e vinte metros. [p=0.3] Pelo atalho: {b}oito menos cinco, três metros por segundo de diferença. [p=0.2] {c}Cento e vinte dividido por três: os mesmos quarenta segundos."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}encontro é a mesma posição no mesmo instante: iguale as funções. [p=0.2] {b}De frente, some as velocidades; [p=0.1] {c}um atrás do outro, subtraia. [p=0.2] {d}E o trem atravessa o túnel mais ele mesmo."),
    dict(id="s20", block="fim", text="Na próxima aula, a velocidade {a}deixa de ser constante: [p=0.2] você vai conhecer {b}a aceleração. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
