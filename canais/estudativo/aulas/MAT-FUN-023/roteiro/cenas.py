# Estudativo · MAT-FUN-023 — Inequações produto e quociente (Matemática · Funções · Função quadrática).
# Habilidade: resolver (x − 1)(x + 2)/(x − 3) ≥ 0 com o quadro de sinais.
# Pré-requisitos: MAT-FUN-011 (zero e sinal da afim; à direita da raiz, sinal do á), MAT-FUN-022 (inequação do 2º grau pela parábola). Próxima: MAT-FUN-028.
# Questão inédita, criada para esta aula. Regra de sinais: MAT-NUM-017. União de intervalos: MAT-CON-008.
# Contas: zeros −2, 1, 3 · x + 2: − + + + · x − 1: − − + + · x − 3: − − − + · resultado: − + − + ·
#   ≥ 0 → [−2, 1] ∪ ]3, +∞[ (3 zera o denominador: sempre aberto).
# Erro: passar (x − 3) multiplicando → (x − 1)(x + 2) ≥ 0 → x ≤ −2 ou x ≥ 1 · x = 2: (1)(4)/(−1) = −4 < 0.
# Atalho: depois da maior raiz, tudo +; troca a cada raiz para a esquerda · não vale com fator do tipo 3 − x nem fator ao quadrado.
# Questão: (x + 3)(x − 2)/(x − 5) ≤ 0 · zeros −3, 2, 5 · sinais − + − + · ≤ 0 → ]−∞, −3] ∪ [2, 5[.
# Visual: quadro de sinais: reta-guia com −2, 1 e 3 alinhados; uma linha por fator com "−" e "+" e bolinha no zero; linha do resultado
#   destacada; bolinha aberta no 3 marcada "divisão por zero"; resposta em E.reta + E.intervalo com dois pedaços.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; a letra a se fala "á".

TITULO = "Inequações produto e quociente"

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
    dict(id="s01", block="gancho", text="{a}Xis menos um, vezes xis mais dois, dividido por xis menos três, maior ou igual a zero. [p=0.3] O reflexo é {b}passar o xis menos três multiplicando para o outro lado. [p=0.2] Só que ele {c}pode ser negativo, [p=0.2] e aí a desigualdade vira sem você ver."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve produtos e divisões com o quadro de sinais, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas. [p=0.2] {b}O zero da função afim e o sinal dela: à direita da raiz, o sinal do á; à esquerda, o contrário. [p=0.2] {c}A regra de sinais: sinais iguais dão mais, diferentes dão menos. [p=0.2] E {d}a união de intervalos. [p=0.3] Se faltar alguma, procure no canal."),
    # ideia
    dict(id="s04", block="ideia", text="A ideia é simples. [p=0.2] {a}O sinal de um produto só depende do sinal de cada fator. [p=0.2] E {b}a divisão segue a mesma regra de sinais da multiplicação. [p=0.3] Então não precisa abrir nada: {c}basta saber onde cada fator é positivo e onde é negativo."),
    # quadro
    dict(id="s05", block="quadro", text="{a}Passo um: o zero de cada fator. [p=0.2] {b}Xis menos um zera no um. [p=0.2] {c}Xis mais dois zera no menos dois. [p=0.2] {d}Xis menos três zera no três. [p=0.3] Esses números {e}cortam a reta em quatro pedaços."),
    dict(id="s06", block="quadro", text="{a}Passo dois: o quadro. [p=0.2] Uma linha para cada fator, com os zeros em ordem: {b}o menos dois, [p=0.2] o um [p=0.2] e o três. [p=0.3] Os três fatores têm á igual a um, positivo. [p=0.2] Então cada um é {c}menos antes da sua raiz [p=0.2] e {d}mais depois dela."),
    dict(id="s07", block="quadro", text="{a}Passo três: multiplique os sinais em cada pedaço, de cima para baixo. [p=0.2] {b}Antes do menos dois: menos, menos e menos. Dá menos. [p=0.2] {c}Entre menos dois e um: mais, menos e menos. Dá mais. [p=0.2] {d}Entre um e três: mais, mais e menos. Dá menos. [p=0.2] {e}Depois do três: tudo mais."),
    dict(id="s08", block="quadro", text="{a}Passo quatro: escolha os pedaços. [p=0.2] Maior ou igual a zero pede {b}os pedaços com mais: [p=0.2] entre menos dois e um, e depois do três. [p=0.3] Falta conferir as pontas. [p=0.2] {c}O menos dois e o um zeram a parte de cima. [p=0.2] A fração vale zero, e zero serve: {d}bolinha fechada."),
    dict(id="s09", block="quadro", text="Já {a}o três zera a parte de baixo, [p=0.2] e {b}divisão por zero não existe. [p=0.2] Então o três {c}fica sempre de fora, mesmo com o tracinho. [p=0.3] Resposta: {d}de menos dois a um, fechado nas pontas, [p=0.2] união com {e}de três até mais infinito, aberto."),
    # erro
    dict(id="s10", block="erro", text="Voltando ao erro do começo. [p=0.2] Quem passa o xis menos três multiplicando fica com {a}xis menos um, vezes xis mais dois, maior ou igual a zero. [p=0.2] Pela parábola, {b}xis menor ou igual a menos dois, ou xis maior ou igual a um. [p=0.3] Teste o {c}dois, que estaria nessa resposta. [p=0.2] {d}Um vezes quatro, dividido por menos um: menos quatro. [p=0.2] {e}Negativo. [p=0.2] {f}Nunca passe multiplicando o que tem xis: monte o quadro."),
    # atalho
    dict(id="s11", block="atalho", text="Agora o atalho, sem quadro: [p=0.2] {a}depois da maior raiz, tudo é mais. [p=0.2] Daí para a esquerda, {b}o sinal troca a cada raiz. [p=0.3] Aqui: {c}mais depois do três, [p=0.2] menos entre um e três, [p=0.2] mais entre menos dois e um, [p=0.2] e menos antes do menos dois."),
    dict(id="s12", block="atalho", text="Funciona porque, à direita de todas as raízes, {a}cada fator é positivo. [p=0.2] E ao passar por uma raiz, {b}só um fator muda de sinal. [p=0.3] {c}Não vale quando algum fator tem o xis com sinal de menos, como três menos xis, [p=0.2] ou quando {d}um fator aparece ao quadrado, que não troca de sinal. [p=0.2] Aí, {e}faça o quadro."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] Resolva {a}xis mais três, vezes xis menos dois, dividido por xis menos cinco, menor ou igual a zero."),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] Os zeros são {a}o menos três, [p=0.2] o dois [p=0.2] e o cinco. [p=0.2] Todo fator tem o xis com sinal de mais: vale o atalho. [p=0.2] {b}Mais depois do cinco, [p=0.2] menos entre dois e cinco, [p=0.2] mais entre menos três e dois, [p=0.2] menos antes do menos três."),
    dict(id="s16", block="resposta", text="Menor ou igual a zero pede {a}os pedaços com menos. [p=0.2] {b}O menos três e o dois zeram a parte de cima: fechados. [p=0.2] {c}O cinco zera a parte de baixo: aberto. [p=0.3] Resposta: {d}de menos infinito até menos três, fechado no menos três, [p=0.2] união com {e}de dois a cinco, fechado no dois e aberto no cinco."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}ache o zero de cada fator, [p=0.2] {b}multiplique os sinais no quadro [p=0.2] e {c}deixe sempre de fora o zero da parte de baixo."),
    dict(id="s18", block="fim", text="Na próxima aula, {a}duas inequações valem ao mesmo tempo: [p=0.2] {b}xis menos um maior que zero, e xis ao quadrado menos cinco xis mais seis menor que zero. [p=0.2] Você resolve cada uma e {c}empilha as retas. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
