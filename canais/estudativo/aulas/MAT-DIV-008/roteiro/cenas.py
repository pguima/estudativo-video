# Estudativo · MAT-DIV-008 — Praticando: múltiplos, primos, MMC e MDC (Matemática · Divisibilidade, MMC e MDC).
# Habilidade: fatorar números e decidir entre MMC e MDC em problemas de cortes e encontros.
# Pré-requisitos: MAT-DIV-001 a MAT-DIV-007. Próxima: nenhuma na trilha (fim do módulo); convida para Frações (MAT-FRA-001).
# Questões inéditas, feitas para esta aula; nenhuma é de prova real.
# Q1: 1.278 é par; 1+2+7+8 = 18 → por 6 sim (1.278 ÷ 6 = 213).
# Q2: 266 ÷ 2 = 133 · 133: soma 7, não termina em 0/5 · 133 ÷ 7 = 19 · 266 = 2·7·19; 14 × 19 = 266.
# Q3: 84, 126: ÷2 → 42, 63 · ÷3 → 14, 21 · ÷7 → 2, 3 → MDC 2·3·7 = 42 · 84 ÷ 42 = 2 · 126 ÷ 42 = 3 → 5 pedaços.
# Q4: MDC(8, 12) = 4 · 8 × 12 = 96 · 96 ÷ 4 = 24 h → 6 h do dia seguinte.
# Q5: 18 = 2·3·3 · 24 = 2·2·2·3 → MDC 2·3 = 6 m · 18 × 24 = 432 · 432 ÷ 6 = 72 s.

TITULO = "Praticando: múltiplos, primos, MMC e MDC"

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
    dict(id="s01", block="gancho", text="Em problema de MMC e MDC, muita gente acerta a conta [p=0.2] e {a}erra a escolha. [p=0.3] Resolve direitinho o problema errado."),
    dict(id="s02", block="gancho", text="Você vai treinar isso, e o resto do módulo, em {a}cinco questões criadas para esta aula. [p=0.3] Em cada uma: {b}pause, resolva e volte para conferir."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}regras de divisibilidade, [p=0.2] {b}fatoração, [p=0.2] {c}MDC [p=0.2] e {d}MMC. [p=0.3] Se travar em alguma, procure a aula no canal."),
    # questão 1
    dict(id="s04", block="q1", text="Questão um. [p=0.2] {a}Mil duzentas e setenta e oito balas vão ser divididas igualmente entre {b}seis crianças. [p=0.3] {c}Sem fazer a divisão, diga se sobra bala."),
    dict(id="s05", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s06", block="r1", text="Para dividir por seis, o número precisa {a}ser par e passar no teste do três. [p=0.3] Termina em oito: {b}é par. [p=0.2] Noves fora: {c}um com oito, risca. [p=0.2] {d}Dois com sete, risca. [p=0.2] Não sobrou nada, então passa no três."),
    dict(id="s07", block="r1", text="Passou nos testes: {a}não sobra bala. [p=0.3] Dito de outro jeito, {b}mil duzentos e setenta e oito é múltiplo de seis, [p=0.2] e seis é divisor dele."),
    # questão 2
    dict(id="s08", block="q2", text="Questão dois. [p=0.2] {a}Escreva duzentos e sessenta e seis como multiplicação de primos."),
    dict(id="s09", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s10", block="r2", text="É par: {a}por dois, cento e trinta e três. [p=0.3] Esse tem cara de primo, então teste. [p=0.2] {b}Não é par. [p=0.2] {c}A soma dos algarismos dá sete, o três não serve. [p=0.2] {d}Não termina em zero nem em cinco. [p=0.2] {e}Por sete: dezenove, sem resto."),
    dict(id="s11", block="r2", text="Dezenove é primo: {a}por dezenove, um. [p=0.3] Resposta: {b}dois vezes sete vezes dezenove. [p=0.3] Conferindo: {c}dois vezes sete, catorze. [p=0.2] {d}Catorze vezes dezenove, duzentos e sessenta e seis."),
    # questão 3
    dict(id="s12", block="q3", text="Questão três. [p=0.2] Duas tábuas, {a}de oitenta e quatro e de cento e vinte e seis centímetros, [p=0.2] vão ser cortadas em {b}pedaços iguais, os maiores possíveis, sem sobra. [p=0.3] {c}Quantos pedaços saem, no total?"),
    dict(id="s13", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="r3", text="Pedaços iguais, sem sobra, os maiores possíveis: {a}MDC. [p=0.3] Divida ao mesmo tempo. [p=0.2] {b}Por dois: quarenta e dois e sessenta e três. [p=0.2] {c}Por três: catorze e vinte e um. [p=0.2] {d}Por sete: dois e três. [p=0.3] {e}Dois vezes três vezes sete: quarenta e dois centímetros."),
    dict(id="s15", block="r3", text="Mas a pergunta é quantos pedaços. [p=0.2] {a}Oitenta e quatro dividido por quarenta e dois: dois pedaços. [p=0.2] {b}Cento e vinte e seis dividido por quarenta e dois: três. [p=0.3] {c}No total, cinco pedaços. [p=0.3] Repare: {d}o dois e o três que sobraram no fim da divisão já eram essa resposta."),
    # questão 4
    dict(id="s16", block="q4", text="Questão quatro. [p=0.2] Uma pessoa toma {a}um remédio a cada oito horas [p=0.2] e {b}outro a cada doze. [p=0.3] {c}Às seis da manhã, tomou os remédios juntos. [p=0.2] {d}Quando toma juntos de novo?"),
    dict(id="s17", block="q4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="r4", text="A cada, juntos, de novo: {a}MMC. [p=0.3] Com dois números, cabe o atalho: multiplique e divida pelo MDC. [p=0.2] {b}O MDC de oito e doze é quatro. [p=0.2] {c}Oito vezes doze, noventa e seis. [p=0.2] {d}Dividido por quatro, vinte e quatro."),
    dict(id="s19", block="r4", text="São {a}vinte e quatro horas depois: [p=0.2] {b}às seis da manhã do dia seguinte."),
    # questão 5
    dict(id="s20", block="q5", text="Última questão, e é a da escolha. [p=0.2] Os números são os mesmos: {a}dezoito e vinte e quatro. [p=0.3] {b}Caso A: cordas de dezoito e de vinte e quatro metros, cortadas em pedaços iguais, os maiores possíveis, sem sobra. [p=0.2] Qual é o tamanho do pedaço?"),
    dict(id="s21", block="q5", text="{a}Caso B: um sinal toca a cada dezoito segundos, outro a cada vinte e quatro. [p=0.2] Tocaram juntos agora. [p=0.2] Quando tocam juntos de novo? [p=0.3] {b}Decida entre MMC e MDC em cada caso, e resolva."),
    dict(id="s22", block="q5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s23", block="r5", text="O caso A {a}reparte: é MDC. [p=0.3] {b}Dezoito é dois vezes três vezes três. [p=0.2] {c}Vinte e quatro é dois vezes dois vezes dois vezes três. [p=0.2] Em comum: {d}dois vezes três. [p=0.2] {e}Seis metros."),
    dict(id="s24", block="r5", text="O caso B {a}repete: é MMC. [p=0.3] {b}Dezoito vezes vinte e quatro, quatrocentos e trinta e dois. [p=0.2] {c}Dividido pelo MDC, que é seis: [p=0.2] {d}setenta e dois segundos."),
    # atalho
    dict(id="s25", block="atalho", text="Para fechar, um atalho que confere a sua escolha: {a}a régua. [p=0.3] {b}O MDC nunca passa do menor número. [p=0.2] {c}O MMC nunca fica abaixo do maior. [p=0.3] {d}Seis é menor que dezoito. [p=0.2] {e}Setenta e dois é maior que vinte e quatro. [p=0.2] Tudo no lugar."),
    dict(id="s26", block="atalho", text="Funciona porque {a}o MDC divide os números, e nenhum divisor passa do próprio número. [p=0.3] {b}Já o MMC é múltiplo deles, e um múltiplo não fica abaixo do número."),
    dict(id="s27", block="atalho", text="Quando não compensa? [p=0.2] Ela {a}denuncia o método trocado, mas não a conta errada. [p=0.3] Se você errasse o MDC e achasse {b}doze, a régua deixaria passar. [p=0.2] Para pegar esse erro, {c}divida os números pelo MDC: não pode sobrar resto."),
    # fechamento
    dict(id="s28", block="fim", text="Resumindo: {a}reparte, MDC. [p=0.2] {b}Repete, MMC. [p=0.2] E {c}fatorar resolve as duas contas. [p=0.3] Com isso, você fechou o módulo."),
    dict(id="s29", block="fim", text="O próximo passo é seguir para {a}Frações, [p=0.2] onde o MDC ajuda a simplificar e o MMC ajuda a somar. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
