# Estudativo · MAT-PRO-009 — Atalhos da PG: termo do meio e três termos (Matemática · Progressões · Progressão geométrica).
# Habilidade: achar x em 4, x, 9 com x² = 36 e escrever três termos como x/q, x, x · q.
# Pré-requisitos: MAT-PRO-008 (razão e termo geral da PG), MAT-POT-007 (raiz quadrada). Próxima: MAT-PRO-010.
# Questão inédita, criada para esta aula. Termos como na MAT-PRO-008 (razão "quê", "pê gê") e na MAT-POT-007 (raiz quadrada
#   como "que número, vezes ele mesmo"; raiz por fatoração com "duplas" de primos; o símbolo da raiz escolhe o positivo).
# Atalhos da PA (MAT-PRO-005) fora da ficha: não citados. "Média" explicada na hora no erro comum. Raiz cúbica: MAT-POT-016.
# Gancho e questão pedem termos positivos. Meio: x / 4 = 9 / x → x² = 36 → x = 6 (4, 6, 9, q = 1,5) ou x = −6 (4, −6, 9, q = −1,5).
# Por quê: a, a·q, a·q² → a · a·q² = (a·q)².
# Três termos: produto 216, maior 18 → x³ = 216 → x = 6 · 6q = 18 → q = 3 → 2, 6, 18.
# Erro: média (4 + 9) / 2 = 6,5 · 6,5 / 4 = 1,625 ≠ 9 / 6,5 ≈ 1,38.
# Atalho: 12, x, 75 → 12 = 2·2·3, 75 = 3·5·5 → duplas de 2, 3 e 5 → 2·3·5 = 30 (12 · 75 = 900 = 30²).
# Questão: 2, x, 50 (positivos) → 100 → 10 (×5) · caixa em PG, volume 1.000 cm³, maior 20 cm → x³ = 1.000 → x = 10
#   → q = 2 → 5, 10, 20 (5 · 10 · 20 = 1.000).
# Visual: 4, x, 9 com dois arcos "×q" iguais; x/4 = 9/x virando x · x = 4 · 9 (E.formula); três caixas x/q | x | x·q com o
#   "/q" e o "·q" riscados no produto; fatoração de 12 e 75 em coluna com as duplas circuladas; caixa 5 × 10 × 20 em perspectiva.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Atalhos da PG: termo do meio e três termos"

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
    dict(id="s01", block="gancho", text="{a}Quatro, [p=0.1] xis, [p=0.1] nove formam uma pê gê de termos positivos. [p=0.2] Quanto vale o xis? [p=0.3] Quem tira a média responde {b}seis e meio, e erra. [p=0.3] A resposta é {c}seis, e sai de {d}uma raiz quadrada."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha o termo do meio de uma pê gê, [p=0.2] escreve três termos com uma letra só [p=0.2] e leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de duas coisas: [p=0.2] {a}a razão da pê gê, que é um termo dividido pelo anterior, [p=0.2] e {b}a raiz quadrada: que número, vezes ele mesmo, dá o que está dentro. [p=0.3] Se faltar alguma, procure no canal."),
    # termo do meio
    dict(id="s04", block="meio", text="Na pê gê, {a}a razão é a mesma nos dois saltos. [p=0.2] Então {b}xis dividido por quatro é igual a nove dividido por xis. [p=0.3] Multiplique em cruz: {c}xis vezes xis igual a quatro vezes nove. [p=0.2] {d}Xis ao quadrado igual a trinta e seis."),
    dict(id="s05", block="meio", text="Que número, vezes ele mesmo, dá trinta e seis? [p=0.2] {a}Seis. [p=0.2] A lista fica {b}quatro, [p=0.1] seis, [p=0.1] nove. [p=0.3] Confira a razão: {c}seis dividido por quatro dá um vírgula cinco, [p=0.2] e {d}nove dividido por seis também."),
    dict(id="s06", block="meio", text="Mas atenção: {a}menos seis vezes menos seis também dá trinta e seis. [p=0.2] E {b}quatro, [p=0.1] menos seis, [p=0.1] nove também é uma pê gê, de razão menos um vírgula cinco. [p=0.3] Por isso a pergunta disse {c}termos positivos, como dinheiro ou tamanho: fica o seis. [p=0.2] Se a questão não disser nada, {d}as duas respostas valem."),
    dict(id="s07", block="meio", text="A regra geral: {a}o termo do meio, ao quadrado, é igual ao produto dos vizinhos. [p=0.3] Por quê? [p=0.2] Chame o primeiro de á. [p=0.2] Os três são {b}á, [p=0.1] á vezes quê, [p=0.1] á vezes quê vezes quê. [p=0.3] {c}Os vizinhos multiplicados dão á vezes á vezes quê vezes quê. [p=0.2] Isso é {d}o do meio vezes ele mesmo."),
    # três termos
    dict(id="s08", block="tres", text="Agora, três termos com uma letra só. [p=0.2] {a}Três números em pê gê têm produto duzentos e dezesseis, [p=0.2] e {b}o maior é dezoito. [p=0.2] Quais são?"),
    dict(id="s09", block="tres", text="O truque é {a}chamar o do meio de xis. [p=0.2] O de trás é {b}xis dividido por quê. [p=0.2] O da frente é {c}xis vezes quê. [p=0.3] Na multiplicação, {d}o dividido por quê e o vezes quê se cancelam. [p=0.2] Sobra {e}xis ao cubo igual a duzentos e dezesseis."),
    dict(id="s10", block="tres", text="Que número, repetido três vezes, dá duzentos e dezesseis? [p=0.2] {a}Seis vezes seis dá trinta e seis, e vezes seis dá duzentos e dezesseis. [p=0.2] {b}Xis igual a seis. [p=0.3] O maior é {c}seis vezes quê, igual a dezoito. [p=0.2] Então {d}quê igual a três. [p=0.2] Os números são {e}dois, [p=0.1] seis [p=0.1] e dezoito."),
    dict(id="s11", block="tres", text="Repare: {a}quando o enunciado dá o produto dos três, escreva assim. [p=0.2] A razão some da conta, e o do meio sai {b}com uma raiz cúbica."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}tirar a média: somar os vizinhos e dividir por dois. [p=0.2] Em quatro, [p=0.1] xis, [p=0.1] nove, a pessoa faz {b}quatro mais nove dá treze, e dividido por dois dá seis e meio."),
    dict(id="s13", block="erro", text="Confira a razão: {a}seis e meio dividido por quatro dá um vírgula seis dois cinco. [p=0.2] {b}Nove dividido por seis e meio dá um vírgula três e pouco. [p=0.3] As razões não batem: {c}não é pê gê. [p=0.2] {d}Na pê gê, multiplique os vizinhos e tire a raiz."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho, para vizinhos grandes: {a}fatore em vez de multiplicar. [p=0.3] Em {b}doze, [p=0.1] xis, [p=0.1] setenta e cinco: [p=0.2] {c}doze é dois vezes dois vezes três. [p=0.2] {d}Setenta e cinco é três vezes cinco vezes cinco. [p=0.3] Juntos, formam {e}uma dupla de dois, uma de três e uma de cinco. [p=0.2] A raiz leva um de cada dupla: {f}dois vezes três vezes cinco dá trinta."),
    dict(id="s15", block="atalho", text="Funciona porque {a}a raiz quadrada pede dois grupos iguais, e cada dupla se divide entre eles. [p=0.3] Não compensa com {b}vizinhos pequenos, como quatro e nove: multiplique de cabeça. [p=0.2] E se algum primo {c}ficar sem dupla, a raiz não é exata: [p=0.2] {d}cerque entre dois números inteiros."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Em dois, [p=0.1] xis, [p=0.1] cinquenta, uma pê gê de termos positivos, quanto vale o xis? [p=0.3] E uma caixa tem {b}comprimento, largura e altura em pê gê. [p=0.2] O volume, que é comprimento vezes largura vezes altura, é {c}mil centímetros cúbicos. [p=0.2] A maior medida é {d}vinte centímetros. [p=0.2] {e}Quais são as três medidas?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Dois vezes cinquenta dá cem. [p=0.2] {b}Xis ao quadrado igual a cem, e xis igual a dez. [p=0.2] Confira: {c}de dois para dez, e de dez para cinquenta, multiplica por cinco."),
    dict(id="s19", block="resposta", text="Na caixa, o volume é o produto das três medidas. [p=0.2] Então {a}xis ao cubo igual a mil. [p=0.2] {b}Dez vezes dez vezes dez dá mil: xis igual a dez. [p=0.3] {c}Dez vezes quê igual a vinte, então quê igual a dois. [p=0.2] As medidas são {d}cinco, [p=0.1] dez [p=0.1] e vinte centímetros."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}na pê gê, o do meio ao quadrado é o produto dos vizinhos. [p=0.2] E {b}com o produto dos três, escreva xis dividido por quê, xis e xis vezes quê."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai {a}somar um, mais dois, mais quatro, e assim por diante, até quinhentos e doze, com uma fórmula. [p=0.3] E vai calcular {b}quantas pessoas uma corrente alcança em dez rodadas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
