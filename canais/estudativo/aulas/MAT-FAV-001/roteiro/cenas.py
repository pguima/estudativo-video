# Estudativo · MAT-FAV-001 — Função definida por partes (Matemática · Funções Avançadas · Função modular e definida por partes).
# Habilidade: calcular f(5) numa função que vale 2x até x = 3 e 9 depois disso e desenhar o gráfico em pedaços, como o de um frete por faixas.
# Pré-requisitos: MAT-CON-007 (intervalos), MAT-FUN-007 (ler um gráfico), MAT-FUN-009 (função afim). Próxima: MAT-FAV-002.
# Questão inédita, criada para esta aula. Parábola (MAT-FUN-016) fora da ficha: não usada; "curva" só como palavra comum.
# Frete: f(x) = 2x se 0 < x ≤ 3; 9 se x > 3 · f(2) = 4 · f(5) = 9 (erro do gancho: 2 · 5 = 10) · f(3) = 6 (erro: 9).
# Gráfico: segmento de (0, 0) aberto até (3, 6) fechado; linha y = 9 a partir de (3, 9) aberto · salto de 6 para 9.
# Atalho: na fronteira x = 3, as duas leis dão 6 e 9 → salto.
# Questão: f(x) = x + 4 se x < 1; 3x se x ≥ 1 · f(−2) = 2 · f(1) = 3 · f(4) = 12 · fronteira: 1 + 4 = 5 e 3 · 1 = 3 → salto;
#   bolinha vazia em (1, 5) e cheia em (1, 3).
# Visual: tabela de faixas do frete com a balança de pesos; chave com as duas leis (x em índigo, condições em cinza); reta numérica
#   das faixas com o x da vez; plano 0..6 × 0..10 com o segmento, a linha deitada e as bolinhas; palco escuro no atalho.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso; "éfe de xis".

TITULO = "Função definida por partes"

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
    dict(id="s01", block="gancho", text="{a}Uma transportadora cobra o frete assim: [p=0.2] {b}até três quilos, dois reais por quilo. [p=0.2] {c}Acima de três quilos, nove reais fixos. [p=0.3] Quanto custa mandar {d}cinco quilos? [p=0.3] Se você fez dois vezes cinco e chegou em {e}dez reais, [p=0.2] errou: depois dos três quilos, a regra é outra."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula valores de uma função com mais de uma regra, [p=0.2] {b}desenha o gráfico em pedaços [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de três coisas: [p=0.2] {a}ler um intervalo, com bolinha cheia e bolinha vazia; [p=0.2] {b}calcular o valor de uma função, como éfe de dois; [p=0.2] e {c}traçar a reta de uma função afim. [p=0.3] Se faltar alguma, procure no canal."),
    # a lei
    dict(id="s04", block="lei", text="O frete é uma {a}função definida por partes: [p=0.2] uma função com mais de uma lei, [p=0.2] e cada lei vale num pedaço dos valores de xis. [p=0.3] Aqui, {b}xis é o peso em quilos, [p=0.2] e {c}éfe de xis é o preço."),
    dict(id="s05", block="lei", text="Na prova, ela aparece com {a}uma chave. [p=0.2] Primeira linha: {b}dois xis, se xis for maior que zero e menor ou igual a três. [p=0.2] Segunda linha: {c}nove, se xis for maior que três. [p=0.3] A condição, do lado direito, {d}diz qual lei usar."),
    # calcular
    dict(id="s06", block="calcular", text="Para calcular, são dois passos. [p=0.2] {a}Primeiro, veja em qual faixa o xis está. [p=0.2] {b}Depois, use só a lei daquela faixa."),
    dict(id="s07", block="calcular", text="{a}Éfe de dois: [p=0.2] dois não passa de três: primeira linha. [p=0.2] {b}Dois vezes dois, quatro reais. [p=0.3] {c}Éfe de cinco: [p=0.2] cinco é maior que três, segunda linha. [p=0.2] {d}Nove reais. [p=0.2] Nem tem conta: a lei é o próprio nove."),
    # gráfico
    dict(id="s08", block="grafico", text="No gráfico, {a}cada lei só aparece na sua faixa. [p=0.3] {b}Dois xis é uma reta. [p=0.2] Mas ela só vale até o três: [p=0.2] {c}um pedaço de reta, que sobe de zero até seis."),
    dict(id="s09", block="grafico", text="{a}O nove é uma reta deitada na altura nove, [p=0.2] e ela só começa {b}depois do três. [p=0.3] Repare no salto: {c}o gráfico pula do seis para o nove."),
    dict(id="s10", block="grafico", text="As bolinhas mostram {a}quem fica com a fronteira. [p=0.2] O três entra na primeira linha, porque lá está {b}menor ou igual. [p=0.2] Então, {c}bolinha cheia em xis três, ípsilon seis. [p=0.2] Na segunda linha, o três não entra: [p=0.2] {d}bolinha vazia em xis três, ípsilon nove. [p=0.3] No zero, {e}a bolinha também é vazia, porque o zero não entra. [p=0.2] É a mesma ideia da bolinha nos intervalos."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}na fronteira. [p=0.2] Quanto custa {b}éfe de três? [p=0.2] Muita gente pensa: três quilos já é pacote grande, {c}nove reais."),
    dict(id="s12", block="erro", text="Mas a condição {a}maior que três não aceita o três. [p=0.2] Quem aceita é {b}menor ou igual a três. [p=0.2] Então, {c}éfe de três é dois vezes três: seis reais. [p=0.3] Na fronteira, {d}quem decide é o sinal que tem o igual."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}na fronteira, calcule as duas leis. [p=0.3] {b}Dois vezes três dá seis. [p=0.2] {c}A outra lei dá nove. [p=0.2] Deu diferente? {d}O gráfico tem um salto ali. [p=0.2] Deu igual? {e}Os pedaços se encontram, sem salto."),
    dict(id="s14", block="atalho", text="Funciona porque cada pedaço de reta {a}só precisa das pontas. [p=0.2] Com a fronteira calculada nas duas leis, [p=0.2] você já tem {b}os pontos que decidem o desenho. [p=0.3] {c}Se algum pedaço não for reta, [p=0.2] marque também alguns pontos no meio."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] A função é: {a}xis mais quatro, se xis for menor que um; [p=0.2] {b}três xis, se xis for maior ou igual a um. [p=0.3] {c}Calcule éfe de menos dois, éfe de um e éfe de quatro. [p=0.2] E {d}o gráfico tem salto em xis igual a um?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Menos dois é menor que um: primeira linha. [p=0.2] Menos dois mais quatro, {b}dois. [p=0.3] {c}O um fica na segunda linha, por causa do maior ou igual. [p=0.2] Três vezes um, {d}três. [p=0.3] {e}Quatro também fica na segunda linha: três vezes quatro, {f}doze."),
    dict(id="s18", block="resposta", text="Na fronteira, calcule as duas leis: [p=0.2] {a}um mais quatro dá cinco, [p=0.2] e {b}três vezes um dá três. [p=0.2] {c}Deu diferente: tem salto. [p=0.2] Bolinha vazia em {d}xis um, ípsilon cinco, [p=0.2] e cheia em {e}xis um, ípsilon três."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}ache a faixa do xis, [p=0.2] {b}use só a lei dela, [p=0.2] e, {c}na fronteira, o sinal com o igual decide."),
    dict(id="s20", block="fim", text="Na próxima aula, você conhece {a}o módulo de um número: [p=0.2] uma função por partes escondida, com o gráfico {b}em forma de vê. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
