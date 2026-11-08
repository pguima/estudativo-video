# Estudativo · MAT-FAT-002 — Fator comum e agrupamento (Matemática · Fatoração e Equação do 2º Grau).
# Habilidade: colocar em evidência 6x² + 9x = 3x(2x + 3) e fatorar ax + ay + bx + by por agrupamento.
# Pré-requisitos: MAT-DIV-004 (MDC), MAT-EQU-005 (multiplicar termos), MAT-EQU-004 (distributiva, combo). Próxima: MAT-FAT-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis".
# Questão inédita, criada para esta aula. Combo dos três amigos como em MAT-EQU-004.
# 6x² + 9x = 3x(2x + 3) · erro x² + x = x·x (x = 10: 110 contra 100) · ax + ay + bx + by = (x + y)(a + b) (a=2, b=3, x=10, y=1: 55 = 11 × 5).
# Atalho: x² + 5x − 2x − 10 = x(x + 5) − 2(x + 5) = (x + 5)(x − 2) (x = 10: 120 = 15 × 8).
# Questão: x² + 4x + 3x + 12 = (x + 4)(x + 3) (x = 10: 182 = 14 × 13).

TITULO = "Fator comum e agrupamento"

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
    dict(id="s01", block="gancho", text="{a}Seis xis ao quadrado mais nove xis. [p=0.3] Até agora, você abria parênteses. [p=0.2] Hoje, faz o caminho de volta: [p=0.2] {b}três xis, abre parênteses, dois xis mais três, fecha parênteses."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você transforma soma em multiplicação, [p=0.2] e leva um {b}atalho para o sinal de menos."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}duas coisas. [p=0.2] {b}O MDC, o maior número que divide todos. [p=0.2] E {c}a distributiva: o número de fora multiplica cada termo de dentro. [p=0.3] Se faltar alguma, procure no canal."),
    # ideia
    dict(id="s04", block="ideia", text="Lembra dos {a}três amigos com o mesmo combo? [p=0.2] A conta {b}três, abre parênteses, xis mais quatro, fecha parênteses, [p=0.2] virou {c}três xis mais doze. [p=0.3] Fatorar é a volta: [p=0.2] olhar para {d}três xis mais doze e enxergar o três que se repete."),
    dict(id="s05", block="ideia", text="{a}Fatorar é escrever como multiplicação. [p=0.2] Você já fez isso com números: {b}doze é dois vezes dois vezes três. [p=0.3] Cada pedaço de uma multiplicação se chama {c}fator. [p=0.2] E o que divide todos os termos é o {d}fator comum."),
    # método
    dict(id="s06", block="metodo", text="Vamos fatorar {a}seis xis ao quadrado mais nove xis. [p=0.3] {b}Primeiro, os números: o MDC de seis e nove é três. [p=0.2] {c}Depois, as letras: os termos têm xis, [p=0.2] e o menor expoente é um. [p=0.2] Então entra {d}um xis só. [p=0.3] O fator comum é {e}três xis."),
    dict(id="s07", block="metodo", text="{a}Em seguida, divida cada termo por três xis. [p=0.2] {b}Seis xis ao quadrado dividido por três xis: [p=0.2] seis dividido por três dá dois, [p=0.2] e na mesma base os expoentes subtraem. [p=0.2] Fica {c}dois xis. [p=0.3] {d}Nove xis dividido por três xis: três. [p=0.3] Resultado: {e}três xis, abre parênteses, dois xis mais três, fecha parênteses."),
    dict(id="s08", block="metodo", text="Esse jeito de escrever se chama {a}colocar em evidência: [p=0.2] o fator comum vai para a frente. [p=0.3] Para conferir, {b}abra com a distributiva. [p=0.2] {c}Três xis vezes dois xis dá seis xis ao quadrado. [p=0.2] {d}Três xis vezes três dá nove xis. [p=0.2] Bateu."),
    # erro
    dict(id="s09", block="erro", text="Cuidado com o termo que {a}sai inteiro. [p=0.2] Em {b}xis ao quadrado mais xis, o fator comum é xis. [p=0.2] Xis ao quadrado dividido por xis dá xis. [p=0.2] E {c}xis dividido por xis dá um, não zero. [p=0.3] Muita gente escreve {d}xis vezes xis, e o um some. [p=0.2] Com dez: {e}cem mais dez dá cento e dez, [p=0.2] e xis vezes xis daria {f}cem. [p=0.2] O certo é {g}xis, abre parênteses, xis mais um, fecha parênteses."),
    # agrupamento
    dict(id="s10", block="agrupar", text="E quando nada se repete em todos os termos? [p=0.2] Veja {a}á xis mais á ípsilon mais bê xis mais bê ípsilon. [p=0.3] A letra a não está nos últimos termos. [p=0.2] O xis não está no segundo. [p=0.3] A saída é {b}agrupar: fatorar em pares."),
    dict(id="s11", block="agrupar", text="{a}No primeiro par, a letra a é comum: [p=0.2] {b}á, abre parênteses, xis mais ípsilon, fecha parênteses. [p=0.3] {c}No segundo par, a letra bê é comum: [p=0.2] {d}bê, abre parênteses, xis mais ípsilon, fecha parênteses."),
    dict(id="s12", block="agrupar", text="Repare: {a}o mesmo parêntese apareceu nos pares. [p=0.2] Ele vira o fator comum, como uma caixa fechada. [p=0.3] {b}Coloque a caixa em evidência: [p=0.2] {c}abre parênteses, xis mais ípsilon, fecha parênteses, vezes, abre parênteses, á mais bê, fecha parênteses."),
    dict(id="s13", block="agrupar", text="Teste com números: {a}a letra a vale dois, bê vale três, xis vale dez e ípsilon vale um. [p=0.2] {b}Vinte mais dois mais trinta mais três dá cinquenta e cinco. [p=0.2] {c}Onze vezes cinco também dá cinquenta e cinco."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho, para quando o segundo par começa com {a}sinal de menos. [p=0.2] {b}Xis ao quadrado mais cinco xis menos dois xis menos dez. [p=0.3] {c}Primeiro par: xis, abre parênteses, xis mais cinco, fecha parênteses. [p=0.2] No segundo par, {d}tire o menos dois junto: [p=0.2] {e}menos dois, abre parênteses, xis mais cinco, fecha parênteses."),
    dict(id="s15", block="atalho", text="O parêntese bateu, e a resposta é {a}xis mais cinco, vezes xis menos dois. [p=0.3] Funciona porque, {b}ao tirar o menos dois, cada termo de dentro troca de sinal: [p=0.2] menos dois xis vira xis, e menos dez vira mais cinco. [p=0.2] É isso que deixa o parêntese igual ao primeiro. [p=0.3] {c}Se nem assim os parênteses baterem, troque a ordem dos termos. [p=0.2] Se ainda não der, essa expressão não fatora por agrupamento."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Fatore: {a}xis ao quadrado mais quatro xis mais três xis mais doze."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá, em pares. [p=0.2] {a}Primeiro par: xis, abre parênteses, xis mais quatro, fecha parênteses. [p=0.2] {b}Segundo par: o MDC de três e doze é três. [p=0.2] Fica três, abre parênteses, xis mais quatro, fecha parênteses. [p=0.3] Resposta: {c}xis mais quatro, vezes xis mais três."),
    dict(id="s19", block="resposta", text="Confira com dez: [p=0.2] {a}cem mais quarenta mais trinta mais doze dá cento e oitenta e dois. [p=0.2] {b}Catorze vezes treze também. [p=0.3] São {c}os quatro pedaços do piso, montados de volta."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}ache o que se repete em todos os termos [p=0.2] e {b}coloque em evidência. [p=0.2] {c}Se nada se repete em todos, agrupe em pares."),
    dict(id="s21", block="fim", text="Na próxima aula, você fatora com os produtos notáveis: [p=0.2] {a}xis ao quadrado menos quarenta e nove [p=0.2] vira {b}xis mais sete, vezes xis menos sete. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
