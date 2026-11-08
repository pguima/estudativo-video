# Estudativo · MAT-FAT-003 — Fatorar com produtos notáveis (Matemática · Fatoração e Equação do 2º Grau).
# Habilidade: escrever x² − 49 como (x + 7)(x − 7), x² + 6x + 9 como (x + 3)² e calcular 1.001² − 999² = 4.000 de cabeça.
# Pré-requisitos: MAT-FAT-002 (fator comum), MAT-FAT-015 (soma vezes diferença), MAT-FAT-001 (quadrado da soma). Próxima: MAT-FAT-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis".
# Questão inédita, criada para esta aula. Sem a palavra "raiz" (radiciação não está em "Já ensinado").
# 4x² − 25 = (2x + 5)(2x − 5) · x² − 10x + 25 = (x − 5)² · x² + 5x + 9 não é quadrado perfeito · 2x² − 50 = 2(x + 5)(x − 5) (x = 10: 150).
# Erro: x² − 49 = (x − 7)²? x = 10: 51 contra 9. Atalho: 1.001² − 999² = 2.000 × 2 = 4.000.
# Questão: 3x² − 12 = 3(x + 2)(x − 2) (x = 10: 288 = 3 × 12 × 8).

TITULO = "Fatorar com produtos notáveis"

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
    dict(id="s01", block="gancho", text="{a}Mil e um ao quadrado, [p=0.2] {b}menos novecentos e noventa e nove ao quadrado. [p=0.3] Parece conta de calculadora. [p=0.2] Mas dá {c}quatro mil, e sai de cabeça."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você fatora usando os produtos notáveis, [p=0.2] e essa conta vira o {b}atalho da aula."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}três coisas: [p=0.2] {b}o quadrado da soma e o da diferença, [p=0.2] {c}a soma vezes a diferença [p=0.2] e {d}colocar em evidência. [p=0.3] Se faltar alguma, procure no canal."),
    # diferença de dois quadrados
    dict(id="s04", block="diferenca", text="Pela soma vezes a diferença, {a}xis mais sete, vezes xis menos sete, [p=0.2] dá {b}xis ao quadrado menos quarenta e nove. [p=0.3] Fatorar é ler essa igualdade {c}de trás para a frente."),
    dict(id="s05", block="diferenca", text="Olhe para {a}xis ao quadrado menos quarenta e nove. [p=0.2] São {b}dois quadrados, com menos entre eles. [p=0.3] {c}Xis ao quadrado é o quadrado de xis. [p=0.2] {d}Quarenta e nove é o quadrado de sete. [p=0.3] Então fica {e}xis mais sete, vezes xis menos sete."),
    dict(id="s06", block="diferenca", text="Essa é a {a}diferença de dois quadrados. [p=0.2] {b}Descubra o que foi elevado ao quadrado em cada termo [p=0.2] e escreva {c}a soma vezes a diferença. [p=0.3] Vale com número na frente: [p=0.2] em {d}quatro xis ao quadrado menos vinte e cinco dá [p=0.2] quatro xis ao quadrado é dois xis vezes dois xis, e vinte e cinco é cinco vezes cinco. [p=0.2] Fica {e}dois xis mais cinco, vezes dois xis menos cinco."),
    # trinômio quadrado perfeito
    dict(id="s07", block="trinomio", text="Agora, uma expressão de três termos: {a}xis ao quadrado mais seis xis mais nove. [p=0.2] Expressão com três termos se chama {b}trinômio. [p=0.3] {c}O primeiro é o quadrado de xis. [p=0.2] {d}O último é o quadrado de três. [p=0.2] E o do meio? [p=0.2] {e}Duas vezes xis vezes três dá seis xis. [p=0.2] Bateu."),
    dict(id="s08", block="trinomio", text="Quando o meio bate, é um {a}trinômio quadrado perfeito: [p=0.2] o quadrado de uma soma. [p=0.2] {b}Fica xis mais três, ao quadrado. [p=0.3] Com menos no meio, vira quadrado da diferença: [p=0.2] {c}xis ao quadrado menos dez xis mais vinte e cinco [p=0.2] é {d}xis menos cinco, ao quadrado."),
    dict(id="s09", block="trinomio", text="E se o meio não bater? [p=0.2] Em {a}xis ao quadrado mais cinco xis mais nove, [p=0.2] duas vezes xis vezes três dá seis xis, {b}e o meio é cinco xis. [p=0.2] {c}Não é quadrado perfeito. [p=0.2] Confira sempre o meio antes de escrever o quadrado."),
    # fator comum antes
    dict(id="s10", block="primeiro", text="Uma regra de ouro: {a}antes de tudo, procure fator comum. [p=0.2] Em {b}dois xis ao quadrado menos cinquenta dá [p=0.2] cinquenta não é o quadrado de nenhum número inteiro. [p=0.3] Mas {c}o dois é comum: [p=0.2] dois, abre parênteses, xis ao quadrado menos vinte e cinco, fecha parênteses. [p=0.3] Aí sim: {d}dois, vezes o parêntese xis mais cinco, vezes o parêntese xis menos cinco."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}trocar a diferença de quadrados pelo quadrado da diferença: [p=0.2] escrever xis ao quadrado menos quarenta e nove como {b}xis menos sete, ao quadrado. [p=0.3] Com dez: {c}cem menos quarenta e nove dá cinquenta e um. [p=0.2] Dez menos sete, ao quadrado, daria {d}nove. [p=0.3] O quadrado da diferença {e}tem termo do meio, e essa expressão não tem."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho, que é o gancho. [p=0.2] {a}Mil e um ao quadrado menos novecentos e noventa e nove ao quadrado [p=0.2] é uma {b}diferença de dois quadrados. [p=0.3] Então vira {c}soma vezes diferença. [p=0.2] {d}Mil e um mais novecentos e noventa e nove dá dois mil. [p=0.2] {e}Mil e um menos novecentos e noventa e nove dá dois. [p=0.2] {f}Dois mil vezes dois: quatro mil."),
    dict(id="s13", block="atalho", text="Funciona porque {a}a fatoração troca dois quadrados enormes por uma soma e uma subtração fáceis. [p=0.3] {b}Não serve para soma de quadrados, com mais entre eles: [p=0.2] essa não vira soma vezes diferença. [p=0.2] E com {c}números pequenos, como cinco ao quadrado menos três ao quadrado, [p=0.2] a conta direta já é rápida."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Fatore até o fim: {a}três xis ao quadrado menos doze."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] Primeiro, o fator comum: {a}três, abre parênteses, xis ao quadrado menos quatro, fecha parênteses. [p=0.3] Dentro, uma diferença de quadrados: {b}quatro é o quadrado de dois. [p=0.2] Resposta: {c}três, vezes o parêntese xis mais dois, vezes o parêntese xis menos dois."),
    dict(id="s17", block="resposta", text="Confira com dez: [p=0.2] {a}trezentos menos doze dá duzentos e oitenta e oito. [p=0.2] {b}Três vezes doze vezes oito também. [p=0.3] Quem parou no primeiro passo {c}não terminou: ainda dava para fatorar."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}dois quadrados com menos entre eles viram soma vezes diferença, [p=0.2] e {b}três termos com o meio certo viram um quadrado."),
    dict(id="s19", block="fim", text="Na próxima aula, a fatoração mostra para que serve: [p=0.2] {a}simplificar frações com letra, [p=0.2] como {b}xis ao quadrado menos nove, dividido por xis menos três. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
