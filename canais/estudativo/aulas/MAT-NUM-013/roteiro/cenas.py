# Estudativo · MAT-NUM-013 — Ordem das operações e parênteses (Matemática · Números e Contas).
# Habilidade: calcular 2 + 3 × 4 explicando por que dá 14, e não 20, e resolver 20 − [3 × (4 + 1)] de dentro para fora.
# Pré-requisitos: MAT-NUM-009 (dividir por um algarismo). Próxima: MAT-NUM-014.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula.

TITULO = "Ordem das operações e parênteses"

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
    dict(id="s01", block="gancho", text="{a}Dois mais três vezes quatro. [p=0.3] Se você fez na ordem em que leu, [p=0.2] deu {b}vinte. [p=0.3] {c}Errado. [p=0.2] A resposta é {d}catorze."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve contas com {b}parênteses e colchetes, [p=0.2] e ainda leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você só precisa das {a}quatro operações: [p=0.2] somar, subtrair, multiplicar e dividir. [p=0.3] Se faltar alguma, procure no canal."),
    # por que o vezes vem antes
    dict(id="s04", block="envelopes", text="Por que catorze? [p=0.3] Imagine {a}dois reais soltos na carteira [p=0.2] e {b}três envelopes com quatro reais em cada um. [p=0.3] {c}Quanto dinheiro você tem?"),
    dict(id="s05", block="envelopes", text="Os envelopes guardam {a}três vezes quatro, que dá doze reais. [p=0.2] Com os reais soltos, {b}catorze. [p=0.3] Quem soma primeiro faz {c}cinco vezes quatro, [p=0.2] como se os reais soltos também tivessem virado envelopes. [p=0.3] Aí aparecem {d}seis reais que nunca existiram."),
    dict(id="s06", block="envelopes", text="O vezes é {a}uma soma empacotada: [p=0.2] quatro mais quatro mais quatro. [p=0.3] O dividido também trabalha com pacotes iguais. [p=0.2] Por isso, {b}primeiro se resolvem os pacotes, [p=0.2] e só depois se soma o que está solto."),
    # regra
    dict(id="s07", block="regra", text="Conta com mais de uma operação se chama {a}expressão. [p=0.3] Toda expressão segue a mesma ordem: [p=0.2] {b}parênteses, [p=0.2] {c}depois vezes e dividido, [p=0.2] {d}por último mais e menos."),
    dict(id="s08", block="regra", text="Parêntese serve para {a}mandar fazer primeiro o que está dentro dele. [p=0.3] {b}Dois mais três entre parênteses, vezes quatro: [p=0.2] agora, sim, {c}dá vinte. [p=0.3] Sem parêntese, vale a ordem normal. [p=0.2] Com ele, o que está dentro passa na frente."),
    dict(id="s09", block="regra", text="Veja a ordem com o dividido. [p=0.2] {a}Sete mais doze dividido por três. [p=0.3] O dividido vem antes: {b}doze dividido por três dá quatro. [p=0.2] Depois, {c}sete mais quatro dá onze."),
    dict(id="s10", block="regra", text="Veja agora com tudo junto. [p=0.2] {a}Trinta menos, abre parênteses, dois mais quatro, fecha parênteses, vezes três. [p=0.3] {b}Primeiro o parêntese: dois mais quatro dá seis. [p=0.2] {c}Depois o vezes: seis vezes três dá dezoito. [p=0.2] {d}Por último, trinta menos dezoito dá doze."),
    # colchetes
    dict(id="s11", block="colchetes", text="E parêntese dentro de parêntese? [p=0.2] Para não confundir, o de fora vira {a}colchete, [p=0.2] um parêntese de cantos retos. [p=0.3] Veja {b}vinte menos um colchete. [p=0.2] Dentro do colchete, {c}três vezes um parêntese. [p=0.2] Dentro do parêntese, {d}quatro mais um."),
    dict(id="s12", block="colchetes", text="Resolva {a}de dentro para fora. [p=0.2] {b}Quatro mais um dá cinco. [p=0.2] O colchete fica com {c}três vezes cinco, que dá quinze. [p=0.2] Sobrou {d}vinte menos quinze, [p=0.2] que dá {e}cinco."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com um erro muito comum: [p=0.2] achar que o vezes {a}sempre vem antes do dividido. [p=0.3] Veja {b}doze dividido por dois vezes três. [p=0.3] Quem faz o vezes primeiro {c}chega em dois."),
    dict(id="s14", block="erro", text="Mas vezes e dividido estão {a}no mesmo degrau. [p=0.2] Entre eles, vale {b}da esquerda para a direita. [p=0.2] {c}Doze dividido por dois dá seis. [p=0.2] {d}Seis vezes três dá dezoito. [p=0.3] Mais e menos também ficam no mesmo degrau: [p=0.2] {e}dez menos três mais dois dá nove."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}os blocos. [p=0.2] {b}Separe a expressão nos sinais de mais e de menos. [p=0.2] Cada pedaço é um bloco, resolvido sozinho. [p=0.2] Só no fim, {c}junte os blocos."),
    dict(id="s16", block="atalho", text="Veja: {a}seis vezes cinco menos oito dividido por dois mais um. [p=0.3] São três blocos: [p=0.2] {b}seis vezes cinco dá trinta. [p=0.2] {c}Oito dividido por dois dá quatro. [p=0.2] {d}O último bloco é o um. [p=0.3] Junte: {e}trinta menos quatro mais um dá vinte e sete."),
    dict(id="s17", block="atalho", text="Funciona porque vezes e dividido vêm antes, [p=0.2] então ficam {a}grudados no mesmo bloco. [p=0.3] Só {b}não corte dentro de parênteses: [p=0.2] o que está lá dentro é um bloco só, mesmo com mais ou menos, e vem primeiro. [p=0.3] E {c}não compensa em conta só de vezes e dividido: [p=0.2] aí é tudo um bloco, da esquerda para a direita."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Resolva {a}quarenta menos um colchete. [p=0.2] Dentro do colchete, {b}cinco vezes um parêntese. [p=0.2] Dentro do parêntese, {c}dois mais quatro."),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá, de dentro para fora. [p=0.2] {a}Dois mais quatro dá seis. [p=0.2] {b}Cinco vezes seis dá trinta. [p=0.2] {c}Quarenta menos trinta dá {d}dez. [p=0.3] Quem começou por quarenta menos cinco saiu da ordem: o colchete vem antes."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}parênteses, [p=0.2] {b}depois vezes e dividido, [p=0.2] {c}por último mais e menos. [p=0.3] No mesmo degrau, {d}da esquerda para a direita."),
    dict(id="s22", block="fim", text="Na próxima aula, o caminho é o inverso: [p=0.2] você {a}lê um problema de compra [p=0.2] e {b}monta a expressão do troco. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
