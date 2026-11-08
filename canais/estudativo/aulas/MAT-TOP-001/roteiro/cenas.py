# Estudativo · MAT-TOP-001 — Números binomiais e triângulo de Pascal (Matemática · Tópicos Avançados · Binômio, distribuição binomial e casa dos pombos).
# Habilidade: calcular o binomial de 5 sobre 2 (10) e montar no triângulo de Pascal a linha 1, 4, 6, 4, 1.
# Pré-requisitos: MAT-CNT-008 (combinação: arranjo dividido por p!). Próxima: MAT-TOP-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; "!" narrado como "fatorial".
# Questão inédita, criada para esta aula. Binomial narrado "binomial de cinco sobre dois" (não é fração: o gancho mostra isso).
# Linhas e posições do triângulo contam a partir do zero. Soma da linha = 2^n só com potência (MAT-POT-001) e princípio multiplicativo.

TITULO = "Números binomiais e triângulo de Pascal"

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
    dict(id="s01", block="gancho", text="{a}Cinco em cima, dois embaixo, entre parênteses e sem tracinho no meio. [p=0.3] Quem lê como fração pensa em {b}cinco meios. [p=0.3] Mas isso não é fração. [p=0.2] É um {c}número binomial, [p=0.2] e ele vale {d}dez."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula números binomiais, [p=0.2] monta o {b}triângulo de Pascal [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}a combinação: [p=0.2] escolher alguns quando a ordem não importa. [p=0.2] {b}Faça o arranjo e divida pelo fatorial de quantos foram escolhidos. [p=0.3] Se faltar, procure no canal."),
    # o número binomial
    dict(id="s04", block="binomial", text="O número binomial é {a}só outro jeito de escrever a combinação. [p=0.2] {b}Em cima, o total. [p=0.2] {c}Embaixo, quantos você escolhe. [p=0.3] Lê-se {d}binomial de cinco sobre dois: [p=0.2] de quantos jeitos dá para escolher dois entre cinco."),
    dict(id="s05", block="binomial", text="Pense em {a}cinco amigos e dois ingressos para um show. [p=0.2] {b}Cinco vezes quatro dá vinte. [p=0.2] {c}Vinte dividido por dois fatorial dá dez. [p=0.3] São {d}dez duplas possíveis."),
    dict(id="s06", block="binomial", text="Três casos saem de cabeça. [p=0.2] {a}Escolher zero: um jeito só, não levar ninguém. [p=0.2] {b}Escolher todos: também um jeito. [p=0.2] {c}Escolher um: tantos jeitos quanto o total. [p=0.3] E vale a troca da aula de combinação: [p=0.2] {d}escolher os dois que vão é o mesmo que escolher os três que ficam."),
    # o triângulo
    dict(id="s07", block="triangulo", text="Agora, escreva os binomiais em linhas. [p=0.2] {a}Na linha quatro, ficam quatro sobre zero, quatro sobre um, e assim até quatro sobre quatro. [p=0.3] As linhas começam no zero: {b}a do topo é a linha zero, só com o um. [p=0.2] {c}A linha um: um, um. [p=0.2] {d}A linha dois: um, dois, um. [p=0.3] Pelos casos de cabeça, {e}toda linha começa e termina em um."),
    dict(id="s08", block="triangulo", text="E o meio? [p=0.2] {a}Cada número é a soma dos dois que estão em cima dele. [p=0.3] {b}Um mais dois dá três: [p=0.2] a linha três é um, três, três, um. [p=0.2] {c}Três mais três dá seis: [p=0.2] a linha quatro é {d}um, quatro, seis, quatro, um. [p=0.3] Esse é o {e}triângulo de Pascal."),
    dict(id="s09", block="triangulo", text="Por que a soma funciona? [p=0.2] Volte aos cinco amigos e {a}separe a Ana. [p=0.2] Ou a Ana {b}vai, [p=0.2] e você escolhe só mais um entre os outros quatro: {c}quatro jeitos. [p=0.2] Ou a Ana {d}não vai, [p=0.2] e você escolhe os dois entre os quatro: {e}seis jeitos. [p=0.3] {f}Quatro mais seis dá dez, [p=0.2] e os dois vizinhos de cima formam o dez da linha cinco."),
    dict(id="s10", block="triangulo", text="Para achar um binomial no triângulo, {a}o número de cima diz a linha, [p=0.2] e {b}o de baixo diz a posição, [p=0.2] sempre contando a partir do zero. [p=0.3] {c}Binomial de quatro sobre dois: linha quatro, posição dois. [p=0.2] {d}Seis."),
    # erro
    dict(id="s11", block="erro", text="O erro comum é {a}contar as linhas a partir do um. [p=0.2] A pessoa procura o binomial de quatro sobre dois {b}na quarta linha de cima para baixo: [p=0.2] um, três, três, um. [p=0.2] E responde {c}três. [p=0.3] Mas a linha do topo é a {d}linha zero. [p=0.2] Confira com a conta: {e}quatro vezes três, dividido por dois, dá seis."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: {a}some uma linha inteira. [p=0.2] {b}Um mais quatro mais seis mais quatro mais um dá dezesseis, [p=0.2] que é {c}dois elevado a quatro. [p=0.3] Na linha ene, a soma é {d}dois elevado a ene."),
    dict(id="s13", block="atalho", text="Funciona porque a linha quatro conta {a}todos os grupos que dá para formar com quatro pessoas, de qualquer tamanho. [p=0.2] E cada pessoa {b}entra ou não entra: [p=0.2] duas opções para cada uma, {c}dois vezes dois vezes dois vezes dois. [p=0.3] Esse total inclui o grupo vazio, sem ninguém: [p=0.2] {f}se o grupo não pode ficar vazio, tire um. [p=0.3] Compensa quando a pergunta é {d}quantos grupos no total. [p=0.2] {e}Para um tamanho só, faça a combinação."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}A linha cinco é um, cinco, dez, dez, cinco, um. [p=0.3] {b}Monte a linha seis. [p=0.2] Depois, {c}confira o binomial de seis sobre dois pela conta [p=0.2] e {d}a soma da linha pelo atalho."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] As pontas são {a}um. [p=0.2] No meio, {b}um mais cinco, seis; [p=0.2] {c}cinco mais dez, quinze; [p=0.2] {d}dez mais dez, vinte. [p=0.3] Depois, a linha se repete ao contrário, como na troca de quem vai por quem fica: [p=0.2] {e}um, seis, quinze, vinte, quinze, seis, um."),
    dict(id="s17", block="resposta", text="{a}Seis vezes cinco dá trinta, [p=0.2] e dividido por dois fatorial dá {b}quinze: [p=0.2] bate com a posição dois. [p=0.3] E a soma: {c}dois elevado a seis dá sessenta e quatro. [p=0.2] {d}Some a linha e confira: sessenta e quatro."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}o binomial é a combinação escrita em pé, [p=0.2] e no triângulo, {b}cada número é a soma dos dois de cima."),
    dict(id="s19", block="fim", text="Na próxima aula, esses números resolvem {a}abre parênteses, xis mais dois, fecha parênteses, elevado a quatro, [p=0.2] sem multiplicar parêntese por parêntese: [p=0.2] é o {b}binômio de Newton. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
