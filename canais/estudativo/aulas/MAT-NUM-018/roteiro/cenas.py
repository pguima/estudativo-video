# Estudativo · MAT-NUM-018 — Expressões com inteiros (Matemática · Números e Contas).
# Habilidade: resolver −3 + 2 × (−4) respeitando a ordem das operações.
# Pré-requisitos: MAT-NUM-013 (ordem das operações), MAT-NUM-017 (regra de sinais). Próxima: MAT-NUM-019.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula.

TITULO = "Expressões com inteiros"

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
    dict(id="s01", block="gancho", text="{a}Menos três mais dois vezes menos quatro. [p=0.3] Se você fez na ordem em que leu, [p=0.2] deu {b}quatro. [p=0.3] {c}Errado. [p=0.2] A resposta é {d}menos onze."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve expressões com negativos sem se perder nos sinais, [p=0.2] com um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Dois lembretes. [p=0.2] {a}Ordem das operações: parênteses, depois vezes e dividido, por último mais e menos. [p=0.3] {b}Regra de sinais: multiplicando ou dividindo, sinais iguais dão mais, e sinais diferentes dão menos. [p=0.3] Se faltar alguma, procure no canal."),
    # sinais
    dict(id="s04", block="sinais", text="Numa expressão com negativos, o menos tem {a}dois papéis. [p=0.2] Às vezes é {b}uma operação: tirar. [p=0.2] Às vezes é {c}um sinal colado no número, [p=0.2] dizendo que ele é negativo. [p=0.3] {d}Em dez menos três, o menos é operação. [p=0.2] {e}Em menos três sozinho, é sinal colado."),
    dict(id="s05", block="sinais", text="E o parêntese em volta do {a}menos quatro? [p=0.2] Ali dentro não tem conta nenhuma. [p=0.2] Ele só {b}separa o vezes do menos, [p=0.2] para os sinais não encostarem."),
    # resolver
    dict(id="s06", block="resolver", text="A ordem é a de sempre: {a}o vezes vem antes do mais. [p=0.3] {b}Dois vezes menos quatro: [p=0.2] sinais diferentes, {c}menos oito. [p=0.3] Fica {d}menos três, mais, abre parênteses, menos oito, fecha parênteses. [p=0.2] Uma dívida de três e outra de oito: [p=0.2] {e}menos onze."),
    dict(id="s07", block="resolver", text="Em dinheiro, faz sentido. [p=0.2] Você {a}deve três reais. [p=0.2] Depois, {b}leva fiado duas coisas de quatro reais cada. [p=0.3] {c}Primeiro você descobre quanto aumentou a dívida. [p=0.2] Só depois {d}junta com o que já devia. [p=0.3] Na ordem em que leu, a dívida de três entraria no vezes sem ter nada a ver com ele."),
    dict(id="s08", block="resolver", text="Quando o parêntese tem conta dentro, ela vem primeiro. [p=0.2] {a}Menos dois mais sete entre parênteses, vezes menos três. [p=0.3] Dentro: deve dois e paga sete, {b}sobra cinco. [p=0.2] Fora: {c}cinco vezes menos três. [p=0.2] Sinais diferentes: {d}menos quinze."),
    dict(id="s09", block="resolver", text="Vezes e dividido na mesma conta? [p=0.2] {a}Da esquerda para a direita. [p=0.2] {b}Menos doze dividido por dois vezes menos três. [p=0.3] {c}Menos doze dividido por dois dá menos seis. [p=0.2] {d}Menos seis vezes menos três dá mais dezoito. [p=0.3] Resolva um passo por linha e copie o resto igual, com sinal e tudo. [p=0.2] Muito erro é só sinal que sumiu na cópia."),
    # erro
    dict(id="s10", block="erro", text="Cuidado com {a}o menos antes de um parêntese. [p=0.2] {b}Dez menos, abre parênteses, três menos oito, fecha parênteses. [p=0.3] Muita gente ignora o parêntese e faz {c}dez menos três menos oito. [p=0.2] Dá {d}menos um. [p=0.2] Errado."),
    dict(id="s11", block="erro", text="O parêntese vem primeiro: {a}três menos oito dá menos cinco. [p=0.2] Fica {b}dez menos, abre parênteses, menos cinco, fecha parênteses. [p=0.2] Tirar uma dívida é como ganhar: [p=0.2] {c}dez mais cinco dá quinze."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: {a}os blocos, com um cuidado. [p=0.2] {b}Separe a expressão nos sinais de mais e de menos que ligam uma conta na outra. [p=0.3] {c}Sinal colado não corta: [p=0.2] o menos do começo da conta, ou logo depois de um vezes ou dividido, é do próprio número."),
    dict(id="s13", block="atalho", text="Veja: {a}menos doze dividido por três, menos dois vezes, abre parênteses, menos cinco, fecha parênteses. [p=0.3] Corte no menos do meio. [p=0.2] Primeiro bloco: {b}menos doze dividido por três dá menos quatro. [p=0.2] Segundo bloco: {c}dois vezes menos cinco dá menos dez. [p=0.3] Junte: {d}menos quatro menos, abre parênteses, menos dez, fecha parênteses. [p=0.2] Tirar uma dívida de dez é ganhar dez: {e}mais seis."),
    dict(id="s14", block="atalho", text="Funciona porque vezes e dividido vêm antes, [p=0.2] então ficam {a}grudados no mesmo bloco. [p=0.3] E {b}não serve dentro de parênteses: [p=0.2] o que está lá dentro é um bloco só, mesmo com mais ou menos, e vem primeiro. [p=0.3] {c}Não compensa em conta com uma operação só: [p=0.2] faça direto."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Resolva: {a}menos cinco [p=0.2] {b}mais três vezes menos dois [p=0.2] {c}menos, abre parênteses, quatro menos nove, fecha parênteses."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá, em blocos. [p=0.2] Primeiro bloco: {a}menos cinco. [p=0.2] Segundo bloco: {b}três vezes menos dois dá menos seis. [p=0.2] Terceiro bloco, o parêntese: {c}quatro menos nove dá menos cinco."),
    dict(id="s18", block="resposta", text="Junte: {a}menos cinco, mais uma dívida de seis, dá menos onze. [p=0.3] Falta subtrair o resultado do parêntese, que é uma dívida de cinco. [p=0.2] Tirar essa dívida é {b}ganhar cinco: [p=0.2] {c}menos onze mais cinco. [p=0.2] Resposta: {d}menos seis."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}a ordem é a de sempre, [p=0.2] {b}o sinal se decide a cada passo [p=0.2] e {c}menos antes de parêntese pede atenção."),
    dict(id="s20", block="fim", text="Na próxima aula, você {a}pratica: [p=0.2] {b}monta e resolve expressões com negativos, [p=0.2] como um saldo que {c}entra no vermelho. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
