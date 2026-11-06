# Estudativo · MAT-DIV-003 — Números primos e fatoração (Matemática · Divisibilidade, MMC e MDC).
# Habilidade: descobrir que 91 não é primo e escrever 360 como 2 · 2 · 2 · 3 · 3 · 5 pelo método das divisões sucessivas.
# Pré-requisitos: MAT-DIV-002, MAT-NUM-010. Próxima: MAT-DIV-004.
# 91 = 7 × 13 (soma 10, não passa em 3) · 360 → 180 → 90 → 45 → 15 → 5 → 1 = 2·2·2·3·3·5; 8 × 9 = 72; 72 × 5 = 360.
# Atalho: 97 ÷ 7 = 13 resto 6 (13 > 7) · 97 ÷ 11 = 8 resto 9 (8 < 11) → primo. Sem raiz quadrada: ainda não ensinada.
# Questão: 126 → 63 → 21 → 7 → 1 = 2·3·3·7; 2 × 9 = 18; 18 × 7 = 126.

TITULO = "Números primos e fatoração"

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
    dict(id="s01", block="gancho", text="{a}Noventa e um é um número primo? [p=0.3] Ele tem cara de primo, e muita gente diz que sim. [p=0.2] {b}E erra."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você descobre {a}por que ele não é, [p=0.2] aprende a {b}desmontar qualquer número em primos [p=0.2] e ainda leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}duas coisas: [p=0.2] {b}as regras de divisibilidade [p=0.2] e {c}a divisão por dois algarismos. [p=0.3] Se faltar alguma, procure a aula no canal."),
    # o que é primo
    dict(id="s04", block="primo", text="Pense em cadeiras arrumadas em fileiras iguais. [p=0.2] Com {a}doze cadeiras, você tem várias arrumações: [p=0.2] {b}duas fileiras de seis, [p=0.2] {c}três fileiras de quatro."),
    dict(id="s05", block="primo", text="Com {a}sete cadeiras, não tem jeito: [p=0.2] {b}ou uma fileira de sete, {c}ou sete fileiras de uma. [p=0.3] O sete só se divide por um e por ele mesmo."),
    dict(id="s06", block="primo", text="Esse é o {a}número primo: tem {b}exatamente dois divisores, o um e ele mesmo. [p=0.3] {c}Sete é primo. [p=0.2] {d}Doze não é: [p=0.2] tem seis divisores, e número assim se chama {e}composto."),
    dict(id="s07", block="primo", text="{a}Atenção a estes casos. [p=0.3] {b}O um não é primo, porque tem um divisor só. [p=0.2] {c}O dois é primo, e é o único primo par: [p=0.2] qualquer outro par também se divide por dois."),
    dict(id="s08", block="primo", text="Os primeiros primos são {a}dois, três, cinco, sete, onze, treze, dezessete, dezenove, vinte e três e vinte e nove. [p=0.3] Vale ter essa lista na cabeça."),
    # testar 91
    dict(id="s09", block="teste", text="Como testar {a}noventa e um? [p=0.2] Tente dividir pelos primos, em ordem. [p=0.3] {b}Por dois? Não, é ímpar. [p=0.2] {c}Por três? A soma dos algarismos dá dez, não. [p=0.2] {d}Por cinco? Não termina em zero nem em cinco."),
    dict(id="s10", block="teste", text="{a}Por sete? [p=0.2] Noventa e um dividido por sete dá {b}treze, sem resto. [p=0.3] Aí está: {c}noventa e um é sete vezes treze. [p=0.2] Tem divisor além do um e dele mesmo, então {d}não é primo."),
    # fatorar
    dict(id="s11", block="fatorar", text="Todo número composto pode ser {a}desmontado em primos. [p=0.3] Cada número de uma multiplicação se chama {b}fator. [p=0.2] E {c}fatorar é escrever o número como multiplicação só de primos."),
    dict(id="s12", block="fatorar", text="O método é o das {a}divisões sucessivas: [p=0.2] divida {b}pelo menor primo que conseguir, [p=0.2] repita com o resultado [p=0.2] e {c}pare quando chegar em um."),
    dict(id="s13", block="fatorar", text="Vamos com {a}trezentos e sessenta. [p=0.2] É par. [p=0.2] {b}Por dois, cento e oitenta. [p=0.2] {c}Por dois de novo, noventa. [p=0.2] {d}Por dois, quarenta e cinco."),
    dict(id="s14", block="fatorar", text="Quarenta e cinco é ímpar, então o dois não serve mais. [p=0.2] A soma dos algarismos dá nove: {a}por três, quinze. [p=0.2] {b}Por três de novo, cinco. [p=0.2] {c}Por cinco, um. [p=0.2] Chegou em um, acabou."),
    dict(id="s15", block="fatorar", text="A resposta é {a}a coluna dos divisores: [p=0.2] {b}dois vezes dois vezes dois vezes três vezes três vezes cinco. [p=0.3] Para conferir, multiplique: [p=0.2] {c}oito vezes nove, setenta e dois. [p=0.2] {d}Vezes cinco, trezentos e sessenta."),
    # erro
    dict(id="s16", block="erro", text="O erro mais comum é {a}parar em números que não são primos. [p=0.2] A pessoa escreve {b}trezentos e sessenta igual a dez vezes trinta e seis, e acha que fatorou. [p=0.3] A conta está certa, mas {c}dez e trinta e seis ainda se desmontam. [p=0.2] Fatorar só termina quando {d}todo fator é primo."),
    # atalho
    dict(id="s17", block="atalho", text="Agora o atalho, para testar se um número é primo sem perder tempo: [p=0.2] {a}pare quando o resultado da divisão ficar menor que o divisor."),
    dict(id="s18", block="atalho", text="Teste {a}noventa e sete. [p=0.2] Dois, três e cinco não dividem. [p=0.2] {b}Por sete, dá treze e sobra resto. [p=0.2] Treze ainda é maior que sete: continue. [p=0.2] {c}Por onze, dá oito e sobra resto. [p=0.2] {d}Oito é menor que onze: pare. [p=0.3] {e}Noventa e sete é primo."),
    dict(id="s19", block="atalho", text="Funciona porque divisores vêm {a}em pares: [p=0.2] se existisse um divisor maior, o par dele seria menor, e você {b}já teria testado. [p=0.3] E só precisa testar primos, porque quem não se divide por dois também não se divide por quatro."),
    dict(id="s20", block="atalho", text="Quando não compensa? [p=0.2] {a}Se o número é par, termina em cinco ou a soma dá múltiplo de três, [p=0.2] {b}as regras já resolveram. [p=0.3] E em {c}números enormes, o teste fica longo demais para fazer à mão."),
    # questão
    dict(id="s21", block="questao", text="Hora de testar. [p=0.2] {a}Escreva cento e vinte e seis como multiplicação de primos."),
    dict(id="s22", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s23", block="resposta", text="Vamos lá. [p=0.2] É par: {a}por dois, sessenta e três. [p=0.2] Seis mais três dá nove: {b}por três, vinte e um. [p=0.2] {c}Por três, sete. [p=0.2] {d}Por sete, um."),
    dict(id="s24", block="resposta", text="Resposta: {a}dois vezes três vezes três vezes sete. [p=0.3] Conferindo: {b}dois vezes nove, dezoito. [p=0.2] {c}Vezes sete, cento e vinte e seis."),
    # fechamento
    dict(id="s25", block="fim", text="Resumindo: {a}primo tem exatamente dois divisores, [p=0.2] e {b}fatorar é dividir pelo menor primo até chegar em um."),
    dict(id="s26", block="fim", text="Na próxima aula, a fatoração vira ferramenta para achar o {a}MDC, o maior divisor que dois números têm em comum. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
