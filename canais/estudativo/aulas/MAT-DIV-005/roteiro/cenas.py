# Estudativo · MAT-DIV-005 — Calcular o MMC (Matemática · Divisibilidade, MMC e MDC).
# Habilidade: achar o MMC de 4 e 6 listando múltiplos, o de 12, 18 e 30 pela fatoração simultânea e usar MMC × MDC = a × b.
# Pré-requisitos: MAT-DIV-004. Próxima: MAT-DIV-006.
# Fatoração simultânea de 12, 18, 30: ÷2 → 6, 9, 15 · ÷2 → 3, 9, 15 · ÷3 → 1, 3, 5 · ÷3 → 1, 1, 5 · ÷5 → 1, 1, 1 → 180.
# Questão: 6, 8, 10: ÷2 → 3, 4, 5 · ÷2 → 3, 2, 5 · ÷2 → 3, 1, 5 · ÷3 → 1, 1, 5 · ÷5 → 1, 1, 1 → 120.

TITULO = "Como calcular o MMC"

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
    dict(id="s01", block="gancho", text="Qual é o menor número que é múltiplo {a}de doze, {b}de dezoito {c}e de trinta, ao mesmo tempo? [p=0.3] Listando um por um, você ia ficar um bom tempo aqui."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você resolve isso {a}em menos de um minuto, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}duas coisas: [p=0.2] {b}o que são números primos [p=0.2] e {c}o que é o MDC. [p=0.3] Se faltar alguma, procure a aula no canal."),
    # o que é
    dict(id="s04", block="nome", text="MMC quer dizer {a}mínimo múltiplo comum. [p=0.3] O nome já explica tudo, parte por parte."),
    dict(id="s05", block="nome", text="{a}Múltiplo: o resultado de multiplicar o número por outro, como na tabuada, só que sem parar no dez. [p=0.3] {b}Comum: que aparece na lista de todos os números. [p=0.3] {c}Mínimo: o menor deles, sem contar o zero."),
    # listar
    dict(id="s06", block="listar", text="Vamos ver com quatro e seis. [p=0.2] {a}Múltiplos de quatro: quatro, oito, doze, dezesseis, vinte, vinte e quatro. [p=0.3] {b}Múltiplos de seis: seis, doze, dezoito, vinte e quatro."),
    dict(id="s07", block="listar", text="Os dois aparecem em {a}doze e em {b}vinte e quatro. [p=0.3] O menor é {c}doze. [p=0.2] {d}MMC de quatro e seis é doze."),
    dict(id="s08", block="listar", text="Com números pequenos, isso resolve. [p=0.2] Com números grandes, {a}a lista não acaba mais. [p=0.2] E aí entra o método de verdade."),
    # fatoração simultânea
    dict(id="s09", block="fatorar", text="É a {a}fatoração simultânea: fatorar todos os números ao mesmo tempo. [p=0.3] Escreva os números {b}lado a lado. [p=0.2] Doze, dezoito e trinta. [p=0.2] A regra é uma só: [p=0.2] {c}use sempre o menor primo que divida pelo menos um deles. [p=0.2] Quem não for divisível, {d}só desce repetido."),
    dict(id="s10", block="fatorar", text="{a}O dois divide os três números: [p=0.2] {b}seis, nove, quinze. [p=0.3] {c}O dois de novo divide o seis: [p=0.2] {d}três. [p=0.2] Nove e quinze descem repetidos."),
    dict(id="s11", block="fatorar", text="{a}Agora o três: [p=0.2] {b}um, três, cinco. [p=0.3] {c}Três de novo: [p=0.2] {d}um, um, cinco. [p=0.3] {e}Por fim, o cinco: [p=0.2] {f}um, um, um. [p=0.2] Quando tudo vira um, acabou."),
    dict(id="s12", block="fatorar", text="O MMC é {a}a multiplicação de todos os primos que você usou: [p=0.2] {b}dois vezes dois vezes três vezes três vezes cinco. [p=0.3] {c}Cento e oitenta."),
    # diferença
    dict(id="s13", block="diferenca", text="Se você viu a aula de MDC, repare na diferença. [p=0.2] {a}No MDC, só entra o primo que divide todos os números. [p=0.3] {b}No MMC, basta dividir um."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}parar antes da hora. [p=0.3] A pessoa vê {b}um, um, cinco, acha que acabou, e esquece o último {c}cinco. [p=0.2] Ela chega em {d}trinta e seis, que nem é múltiplo de trinta. [p=0.3] Só pare quando {e}todos virarem um."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho, que serve {a}para dois números: [p=0.3] {b}MMC vezes MDC é igual a um número vezes o outro."),
    dict(id="s16", block="atalho", text="Só doze e dezoito, sem o trinta. [p=0.2] Você já sabe que o {a}MDC é seis. [p=0.2] Para achar o MMC, multiplique os dois números e divida pelo MDC. [p=0.3] {b}Doze vezes dezoito, duzentos e dezesseis. [p=0.2] {c}Dividido por seis: [p=0.2] {d}trinta e seis. [p=0.3] Esse é o MMC, sem fatorar nada."),
    dict(id="s17", block="atalho", text="E tem um caso ainda mais rápido: [p=0.2] se o maior número já é múltiplo do menor, ele mesmo é o MMC. [p=0.3] {a}MMC de cinco e vinte? [p=0.2] {b}Vinte."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] {a}Qual é o MMC de seis, oito e dez?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] {a}Por dois: três, quatro, cinco. [p=0.2] {b}Por dois: três, dois, cinco. [p=0.2] {c}Por dois: três, um, cinco. [p=0.2] {d}Por três: um, um, cinco. [p=0.2] {e}Por cinco: um, um, um."),
    dict(id="s21", block="resposta", text="Agora multiplique: {a}dois vezes dois vezes dois vezes três vezes cinco. [p=0.3] {b}Cento e vinte."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}divida pelo menor primo, [p=0.2] {b}quem não divide desce repetido, [p=0.2] {c}e multiplique a coluna quando tudo virar um."),
    dict(id="s23", block="fim", text="Na próxima aula, o {a}MDC em problemas de verdade: dividir coisas em partes iguais, as maiores possíveis. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
