# Estudativo · MAT-ANG-006 — Quando três medidas formam um triângulo (Matemática · Geometria Plana: Ângulos e Triângulos).
# Habilidade: dizer que 2, 3 e 6 não formam triângulo e achar os valores possíveis do terceiro lado quando os outros dois medem 5 e 8 (entre 3 e 13).
# Pré-requisitos: MAT-ANG-005 (triângulos), MAT-EQU-016 (inequação dupla). Próxima: MAT-ANG-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Visual: palitos (E.segmento) de 2, 3 e 6 que não se encontram; 2, 3 e 5 achatados sobre o maior; reta numérica com 3 < x < 13 (bolinhas abertas).

TITULO = "Quando três medidas formam um triângulo"

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
    dict(id="s01", block="gancho", text="{a}Três palitos: de dois, de três e de seis centímetros. [p=0.3] Tente montar um triângulo com eles. [p=0.2] {b}Não fecha. [p=0.3] Os palitos menores {c}não alcançam um ao outro."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você sabe na hora se três medidas formam triângulo, [p=0.2] {b}acha os valores possíveis do terceiro lado [p=0.2] e leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}saber que um triângulo tem três lados que se fecham em três cantos, [p=0.2] e {c}resolver uma inequação dupla, com o xis preso entre dois números. [p=0.3] Se faltar alguma, procure no canal."),
    # por que não fecha
    dict(id="s04", block="palitos", text="Por que não fecha? [p=0.2] Deite {a}o palito de seis centímetros. [p=0.2] De cada ponta dele sai um palito menor: [p=0.2] {b}o de dois de um lado, o de três do outro, [p=0.2] tentando se encontrar lá em cima."),
    dict(id="s05", block="palitos", text="Mesmo {a}esticados ao máximo, deitados sobre o maior, [p=0.2] eles somam {b}cinco centímetros. [p=0.2] {c}Cinco é menos que seis. [p=0.3] Não chegam nem a se tocar. [p=0.2] Levantando, {d}ficam mais longe ainda."),
    dict(id="s06", block="palitos", text="Essa é a condição de existência do triângulo: [p=0.2] {a}cada lado tem que ser menor que a soma dos outros. [p=0.3] É a ideia de que {b}o caminho reto é o mais curto: [p=0.2] ir direto de um canto a outro {c}é sempre mais curto que dar a volta pelo terceiro canto."),
    # caso igual
    dict(id="s07", block="achatado", text="E se a soma der {a}exatamente igual? [p=0.2] Palitos de {b}dois, de três e de cinco centímetros. [p=0.3] Dois mais três dá cinco: [p=0.2] os menores ficam {c}deitados em cima do maior, achatados. [p=0.2] {d}Vira uma linha, não um triângulo."),
    dict(id="s08", block="achatado", text="Então a soma dos menores tem que ser {a}maior que o maior lado. [p=0.2] {b}Igual não serve."),
    # terceiro lado
    dict(id="s09", block="terceiro", text="O caso que mais cai: [p=0.2] você conhece {a}dois lados, de cinco e de oito centímetros, [p=0.2] e quer saber {b}quanto pode medir o terceiro, que vamos chamar de xis."),
    dict(id="s10", block="terceiro", text="{a}O xis tem que ser menor que a soma dos outros, [p=0.2] cinco mais oito: [p=0.2] {b}xis menor que treze."),
    dict(id="s11", block="terceiro", text="{a}O oito tem que ser menor que cinco mais xis. [p=0.2] {b}Tire cinco de cada lado: [p=0.2] {c}três menor que xis. [p=0.3] E o cinco já é menor que o oito: [p=0.2] passa no teste sozinho."),
    dict(id="s12", block="terceiro", text="Juntando as exigências: [p=0.2] {a}três menor que xis, menor que treze. [p=0.3] {b}O terceiro lado fica entre três e treze, sem encostar nas pontas."),
    dict(id="s13", block="terceiro", text="Se o lado for {a}um número inteiro de centímetros, [p=0.2] ele vai de {b}quatro até doze. [p=0.3] Contando: {c}doze menos quatro dá oito, [p=0.2] mais um, porque o quatro também entra: [p=0.2] {d}nove valores."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}deixar as pontas entrarem. [p=0.2] A pessoa responde {b}de três até treze [p=0.2] e conta {c}onze valores."),
    dict(id="s15", block="erro", text="Teste a ponta: {a}lados de três, de cinco e de oito centímetros. [p=0.2] {b}Três mais cinco dá oito, igualzinho ao maior. [p=0.2] É o caso achatado. [p=0.3] {c}O treze também achata: cinco mais oito dá treze."),
    # atalho
    dict(id="s16", block="atalho", text="E o atalho prometido, em duas partes. [p=0.2] {a}Com três medidas, teste só o maior lado: [p=0.2] {b}ele é menor que a soma dos outros? [p=0.2] Se for, forma triângulo."),
    dict(id="s17", block="atalho", text="Funciona porque {a}os lados menores passam no teste sozinhos: [p=0.2] cada um já é menor que o maior lado, [p=0.2] então é menor que o maior somado com qualquer outro."),
    dict(id="s18", block="atalho", text="{a}Com dois lados, o terceiro fica entre a diferença e a soma. [p=0.2] {b}Oito menos cinco dá três. [p=0.2] {c}Oito mais cinco dá treze. [p=0.3] {d}Só não pare no intervalo quando a questão pedir mais, [p=0.2] como o triângulo ser isósceles: [p=0.2] aí, {e}o terceiro lado ainda tem que repetir um dos outros."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Um triângulo tem lados de {a}quatro e de nove centímetros. [p=0.2] O terceiro lado é {b}um número inteiro de centímetros. [p=0.3] {c}Quantos valores ele pode ter?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] {a}Diferença: nove menos quatro dá cinco. [p=0.2] {b}Soma: nove mais quatro dá treze. [p=0.3] {c}Cinco menor que xis, menor que treze. [p=0.3] Sem as pontas, os inteiros vão {d}de seis até doze."),
    dict(id="s22", block="resposta", text="Contando: {a}doze menos seis dá seis, [p=0.2] mais um, porque o seis também entra: [p=0.2] {b}sete valores. [p=0.3] Quem deixa as pontas entrarem conta {c}nove, e erra."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}o maior lado tem que ser menor que a soma dos outros, [p=0.2] e {b}o terceiro lado fica entre a diferença e a soma, sem as pontas."),
    dict(id="s24", block="fim", text="Hoje, três medidas diziam {a}se o triângulo existe. [p=0.2] Na próxima aula, você vê quais informações garantem que {b}dois triângulos são iguais, os casos de congruência, [p=0.2] e usa isso para {c}descobrir um lado ou um ângulo que falta. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
