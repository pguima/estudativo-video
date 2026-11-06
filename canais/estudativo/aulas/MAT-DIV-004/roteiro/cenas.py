# Estudativo · MAT-DIV-004 — Calcular o MDC (Matemática · Divisibilidade, MMC e MDC).
# Habilidade: achar o MDC de 12 e 18 listando divisores e o de 72 e 120 pela fatoração.
# Pré-requisitos: MAT-DIV-003. Próxima: MAT-DIV-005.
# D(12) = 1, 2, 3, 4, 6, 12 · D(18) = 1, 2, 3, 6, 9, 18 → comuns 1, 2, 3, 6 → MDC 6.
# 72 → 36 → 18 → 9 → 3 → 1 = 2·2·2·3·3 · 120 → 60 → 30 → 15 → 5 → 1 = 2·2·2·3·5 → pares 2, 2, 2, 3 → 24 (72 ÷ 24 = 3; 120 ÷ 24 = 5). 120 tem 16 divisores.
# Erro: 2·2·2·3·3 = 72; 120 ÷ 72 = 1 resto 48. Atalho: 72, 120 → 36, 60 → 18, 30 → 9, 15 → 3, 5. Não compensa: 91 = 7·13, 65 = 5·13 → 13.
# Questão: 48 = 2·2·2·2·3 · 60 = 2·2·3·5 → 2·2·3 = 12.
# Coerência com a MAT-DIV-005: "no MDC, só entra o primo que divide todos os números".

TITULO = "Como calcular o MDC"

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
    dict(id="s01", block="gancho", text="Qual é o maior número que divide {a}setenta e dois {b}e cento e vinte, sem deixar resto? [p=0.3] Só o cento e vinte tem {c}dezesseis divisores. [p=0.2] Listar tudo cansa."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você acha esse número {a}com poucas contas, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa de {a}uma coisa: [p=0.2] {b}fatorar, ou seja, escrever um número como multiplicação de primos. [p=0.3] Se faltar, procure a aula no canal."),
    # o que é
    dict(id="s04", block="nome", text="Esse número se chama {a}MDC: máximo divisor comum. [p=0.3] O nome já explica tudo, parte por parte."),
    dict(id="s05", block="nome", text="{a}Divisor: o número que divide outro sem deixar resto. [p=0.3] {b}Comum: que aparece na lista de todos os números. [p=0.3] {c}Máximo: o maior deles."),
    # listar
    dict(id="s06", block="listar", text="Para que serve? [p=0.2] Você tem {a}doze laranjas e {b}dezoito maçãs, e quer montar o maior número possível de sacolas iguais, sem sobrar fruta. [p=0.3] O número de sacolas precisa dividir doze {c}e também dezoito."),
    dict(id="s07", block="listar", text="Liste os divisores. [p=0.2] {a}De doze: um, dois, três, quatro, seis e doze. [p=0.3] {b}De dezoito: um, dois, três, seis, nove e dezoito."),
    dict(id="s08", block="listar", text="Nas duas listas aparecem {a}um, dois, três e seis. [p=0.3] O maior é {b}seis. [p=0.2] {c}MDC de doze e dezoito é seis. [p=0.3] São {d}seis sacolas, cada uma com duas laranjas e três maçãs."),
    dict(id="s09", block="listar", text="Com números pequenos, isso resolve. [p=0.2] Com números maiores, {a}a lista cansa. [p=0.2] E é aí que a fatoração entra."),
    # fatorar
    dict(id="s10", block="fatorar", text="{a}Primeiro, fatore cada número. [p=0.2] {b}Setenta e dois: por dois, trinta e seis. [p=0.2] Por dois, dezoito. [p=0.2] Por dois, nove. [p=0.2] Por três, três. [p=0.2] Por três, um. [p=0.3] Ficou {c}dois vezes dois vezes dois vezes três vezes três."),
    dict(id="s11", block="fatorar", text="{a}Cento e vinte: por dois, sessenta. [p=0.2] Por dois, trinta. [p=0.2] Por dois, quinze. [p=0.2] Por três, cinco. [p=0.2] Por cinco, um. [p=0.3] Ficou {b}dois vezes dois vezes dois vezes três vezes cinco."),
    dict(id="s12", block="fatorar", text="Vem a regra do MDC: [p=0.2] {a}só entra o primo que divide todos os números. [p=0.3] Na prática, ele precisa aparecer {b}nas duas fatorações."),
    dict(id="s13", block="fatorar", text="Forme pares, um primo de cada número. [p=0.2] {a}Dois com dois. [p=0.2] {b}Dois com dois. [p=0.2] {c}Dois com dois. [p=0.2] {d}Três com três. [p=0.3] Sobraram {e}um três no setenta e dois [p=0.2] e {f}o cinco no cento e vinte. [p=0.2] Sem par, {g}ficam de fora."),
    dict(id="s14", block="fatorar", text="O MDC é a multiplicação {a}dos primos que formaram par: [p=0.2] {b}dois vezes dois vezes dois vezes três. [p=0.3] {c}Vinte e quatro."),
    dict(id="s15", block="fatorar", text="Para conferir: {a}setenta e dois dividido por vinte e quatro dá três. [p=0.2] {b}Cento e vinte dividido por vinte e quatro dá cinco. [p=0.2] Nenhum resto."),
    # erro
    dict(id="s16", block="erro", text="O erro mais comum é {a}levar um primo que ficou sem par. [p=0.2] Setenta e dois tem o três repetido, e a pessoa escreve {b}o três duas vezes no MDC. [p=0.2] Dá {c}setenta e dois. [p=0.3] Mas {d}cento e vinte dividido por setenta e dois deixa resto. [p=0.3] Cada primo entra {e}só as vezes que aparece nas duas fatorações."),
    # atalho
    dict(id="s17", block="atalho", text="Agora o atalho: {a}divida os números ao mesmo tempo. [p=0.2] Escreva {b}lado a lado e use só primos que dividam todos."),
    dict(id="s18", block="atalho", text="{a}Por dois: trinta e seis e sessenta. [p=0.2] {b}Por dois: dezoito e trinta. [p=0.2] {c}Por dois: nove e quinze. [p=0.2] {d}Por três: três e cinco. [p=0.3] {e}Três e cinco só têm o um em comum: pare. [p=0.2] Multiplique a coluna: {f}dois vezes dois vezes dois vezes três. [p=0.2] {g}Vinte e quatro."),
    dict(id="s19", block="atalho", text="Funciona porque {a}cada primo usado divide todos os números, [p=0.2] que é a regra do MDC. [p=0.3] Você faz {b}uma conta só, em vez de duas fatorações."),
    dict(id="s20", block="atalho", text="Quando não compensa? [p=0.2] Quando {a}nenhuma regra de divisibilidade mostra um primo comum, [p=0.2] como em {b}noventa e um e sessenta e cinco. [p=0.3] Aí é melhor fatorar cada um: {c}sete vezes treze [p=0.2] e {d}cinco vezes treze. [p=0.2] {e}MDC treze."),
    # questão
    dict(id="s21", block="questao", text="Hora de testar. [p=0.2] {a}Qual é o MDC de quarenta e oito e sessenta?"),
    dict(id="s22", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s23", block="resposta", text="Vamos lá. [p=0.2] {a}Quarenta e oito é dois vezes dois vezes dois vezes dois vezes três. [p=0.3] {b}Sessenta é dois vezes dois vezes três vezes cinco."),
    dict(id="s24", block="resposta", text="Formam par: {a}dois com dois, [p=0.2] {b}dois com dois, [p=0.2] {c}três com três. [p=0.3] {d}Dois vezes dois vezes três. [p=0.2] {e}Doze."),
    # fechamento
    dict(id="s25", block="fim", text="Resumindo: {a}fatore cada número, [p=0.2] {b}junte os primos que aparecem em todos [p=0.2] {c}e multiplique."),
    dict(id="s26", block="fim", text="Na próxima aula, o outro lado da moeda: [p=0.2] o {a}MMC, o menor múltiplo que os números têm em comum. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
