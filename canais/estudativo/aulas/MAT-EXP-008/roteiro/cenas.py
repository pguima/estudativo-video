# Estudativo · MAT-EXP-008 — O que é logaritmo (Matemática · Exponencial e Logaritmo).
# Habilidade: ler log₂ 8 = 3 como 2³ = 8, calcular log 1.000 e log₉ 27, usar log 1 = 0 e dizer por que base e logaritmando têm restrições.
# Pré-requisitos: MAT-EXP-004 (igualar as bases). Próxima: MAT-EXP-009.
# Ensina a abreviação "log" só na tela; a narração diz sempre "logaritmo de ... na base ...". Base dez: "a base escondida".
# Introduz o termo "condição de existência", usado em MAT-EXP-012. Questão inédita, criada para esta aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "O que é logaritmo"

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
    dict(id="s01", block="gancho", text="{a}Dois elevado a quê dá oito? [p=0.3] {b}Três. [p=0.3] Você acabou de calcular um logaritmo, [p=0.2] mesmo sem saber o nome. [p=0.3] Logaritmo assusta pelo nome, [p=0.2] mas {c}é só um expoente."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você lê e calcula logaritmos, sabe quando um logaritmo existe [p=0.2] e leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de três coisas: [p=0.2] {a}potência, inclusive com expoente negativo e em fração, [p=0.2] {b}igualar as bases numa equação exponencial, [p=0.2] e {c}o gráfico da exponencial, que nunca encosta no eixo xis. [p=0.3] Se faltar alguma, procure no canal."),
    # definição
    dict(id="s04", block="definicao", text="O logaritmo responde a uma pergunta: [p=0.2] {a}a base elevada a quê dá esse número? [p=0.3] Dois elevado a três dá oito. [p=0.2] Então {b}o logaritmo de oito na base dois é três."),
    dict(id="s05", block="definicao", text="Na tela, logaritmo vira {a}log, com as três primeiras letras. [p=0.2] {b}A base vai pequena, embaixo. [p=0.2] O número de dentro, o oito, se chama {c}logaritmando. [p=0.2] E o resultado, o três, é {d}o logaritmo: o expoente que faltava."),
    dict(id="s06", block="definicao", text="Todo logaritmo {a}se lê como uma potência. [p=0.2] {b}Logaritmo de oito na base dois igual a três [p=0.2] é o mesmo que {c}dois ao cubo igual a oito. [p=0.3] {d}A base continua base. [p=0.2] {e}O logaritmo vira o expoente. [p=0.2] E {f}o logaritmando é o resultado da potência."),
    # base dez
    dict(id="s07", block="dez", text="Quando a base {a}não aparece escrita, ela é dez. [p=0.3] {b}Logaritmo de mil: [p=0.2] dez elevado a quê dá mil? [p=0.2] {c}Dez ao cubo. [p=0.2] Então {d}o logaritmo de mil é três."),
    # base nove
    dict(id="s08", block="nove", text="E quando a resposta não sai de cabeça? [p=0.2] {a}Logaritmo de vinte e sete na base nove. [p=0.3] Chame o resultado de xis e leia como potência: [p=0.2] {b}nove elevado a xis igual a vinte e sete. [p=0.3] É uma equação exponencial, e você já sabe resolver."),
    dict(id="s09", block="nove", text="{a}Nove é três ao quadrado, e vinte e sete é três ao cubo. [p=0.2] Fica {b}três elevado a dois xis igual a três ao cubo. [p=0.2] {c}Dois xis igual a três, [p=0.2] e {d}xis igual a três dividido por dois, ou um vírgula cinco. [p=0.3] O logaritmo nem sempre é um número inteiro."),
    # logaritmo de um
    dict(id="s10", block="um", text="Agora, {a}o logaritmo de um, em qualquer base. [p=0.2] Que expoente faz a base dar um? [p=0.2] {b}O zero: todo número diferente de zero, elevado a zero, dá um. [p=0.3] Então {c}o logaritmo de um é sempre zero. [p=0.3] E o logaritmo da própria base é {d}um, porque dois elevado a um dá dois."),
    # restrições
    dict(id="s11", block="restricao", text="Por que o logaritmo não aceita qualquer número? [p=0.2] Tente {a}o logaritmo de menos oito na base dois. [p=0.2] Dois elevado a quê dá menos oito? [p=0.3] Você viu no gráfico: [p=0.1] {b}a exponencial de base positiva nunca dá zero nem negativo. [p=0.2] Então {c}esse logaritmo não existe."),
    dict(id="s12", block="restricao", text="E a base segue as regras da exponencial: {a}positiva e diferente de um. [p=0.3] Com base um, {b}um elevado a qualquer expoente dá um. [p=0.2] O logaritmo de cinco na base um {c}não teria resposta. [p=0.2] E o de um, na base um, {d}aceitaria qualquer expoente."),
    dict(id="s13", block="restricao", text="Essas regras têm nome: {a}condição de existência. [p=0.3] {b}O logaritmando é positivo. [p=0.2] {c}A base é positiva e diferente de um."),
    # erro
    dict(id="s14", block="erro", text="O erro comum é {a}dividir. [p=0.2] No logaritmo de oito na base dois, a pessoa faz {b}oito dividido por dois, que dá quatro. [p=0.3] Mas {c}dois elevado a quatro dá dezesseis, e não oito. [p=0.3] O logaritmo é {d}um expoente: [p=0.1] conte quantas vezes a base se multiplica. [p=0.2] Dois vezes dois vezes dois {e}são três vezes."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho, para a base dez: {a}conte os zeros. [p=0.3] {b}Cem tem dois zeros, e o logaritmo dá dois. [p=0.2] {c}Um milhão tem seis zeros, e o logaritmo dá seis. [p=0.3] Com vírgula, {d}conte as casas e ponha o sinal de menos: [p=0.2] {e}o logaritmo de zero vírgula zero zero um dá menos três."),
    dict(id="s16", block="atalho", text="Funciona porque {a}dez elevado a um expoente positivo escreve zeros, [p=0.2] e o expoente negativo conta casas depois da vírgula. [p=0.3] Só vale para {b}um seguido de zeros, ou com o um na última casa. [p=0.2] No {c}logaritmo de quinhentos, não há o que contar: [p=0.2] ele fica entre dois e três, e o valor é assunto de outra aula."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Calcule {a}o logaritmo de oito na base quatro [p=0.2] e {b}o logaritmo de zero vírgula zero um, com a base escondida. [p=0.3] E diga se existe {c}o logaritmo de menos nove na base três."),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Leia como potência: {a}quatro elevado a xis igual a oito. [p=0.2] Base comum: dois. [p=0.2] {b}Dois elevado a dois xis igual a dois ao cubo. [p=0.2] {c}Dois xis igual a três, [p=0.1] e xis igual a três dividido por dois, ou um vírgula cinco."),
    dict(id="s20", block="resposta", text="No segundo, a base é dez: {a}duas casas depois da vírgula, [p=0.2] então dá {b}menos dois. [p=0.2] Conferindo: dez elevado a menos dois dá um centésimo, ou seja, {c}zero vírgula zero um. [p=0.3] E o terceiro {d}não existe: [p=0.2] três elevado a qualquer expoente dá um número positivo."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}logaritmo é o expoente que falta. [p=0.2] {b}Leia como potência, [p=0.2] e {c}lembre: logaritmando positivo, base positiva e diferente de um."),
    dict(id="s22", block="fim", text="Na próxima aula, você conhece {a}as propriedades dos logaritmos: [p=0.2] {b}multiplicação vira soma, divisão vira subtração [p=0.2] e {c}o expoente sai multiplicando. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
