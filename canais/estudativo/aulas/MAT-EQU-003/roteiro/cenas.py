# Estudativo · MAT-EQU-003 — Juntar termos semelhantes (Matemática · Equações do 1º Grau).
# Habilidade: reduzir 3x + 5x − 2 a 8x − 2.
# Pré-requisitos: MAT-EQU-001 (a letra no lugar de um número), MAT-NUM-016 (somar e subtrair inteiros). Próxima: MAT-EQU-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis".
# Questão inédita, criada para esta aula.
# Sem potência, regra de sinais ou valor numérico com negativo: fora da ficha (MAT-POT-001, MAT-NUM-017 e MAT-EQU-002 não estão em "Já ensinado").
# Por isso x + x² ≠ 2x³ fica para MAT-EQU-005; aqui x² só é citado como assunto de outra aula. Testes só com x = 10.
# 3x + 2 em 10 = 32, 5x = 50 · 5x + 6 − 2x + 1 = 3x + 7 (em 10: 37; erro 7x + 7 = 77) · x − 4x = −3x.
# Questão: 6x + 7 − x − 2 = 5x + 5 (em 10: 55).

TITULO = "Juntar termos semelhantes"

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
    dict(id="s01", block="gancho", text="{a}Três xis mais dois. [p=0.3] Muita gente simplifica para {b}cinco xis. [p=0.3] {c}Errado. [p=0.2] E um número só basta para provar."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você encurta expressões juntando o que é parecido, [p=0.2] com um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}duas coisas. [p=0.2] {b}Número colado na letra é vezes: três xis é três vezes xis, [p=0.2] e xis sozinho é um vezes xis. [p=0.3] E {c}somar e subtrair com sinal, pensando em dívida e pagamento. [p=0.3] Se faltar alguma, procure no canal."),
    # caixas de ovos
    dict(id="s04", block="caixas", text="Imagine {a}caixas de ovos, todas com a mesma quantidade. [p=0.2] Você não sabe quantos ovos vêm em cada uma, [p=0.2] então chama essa quantidade de {b}xis. [p=0.3] {c}Três caixas são três xis ovos. [p=0.2] {d}Cinco caixas são cinco xis."),
    dict(id="s05", block="caixas", text="Juntando, você tem {a}oito caixas: oito xis. [p=0.3] Na conta, {b}três xis mais cinco xis dá oito xis. [p=0.2] {c}Soma o número que multiplica a letra, [p=0.2] e {d}a letra fica igual. [p=0.3] Caixa mais caixa continua sendo caixa."),
    dict(id="s06", block="caixas", text="Só que {a}dois ovos quebraram. [p=0.2] Fica {b}três xis mais cinco xis menos dois. [p=0.3] Juntando as caixas: {c}oito xis menos dois. [p=0.2] O menos dois {d}não entra na conta das caixas: [p=0.2] são ovos soltos."),
    # regra
    dict(id="s07", block="regra", text="Cada pedaço da expressão, separado por mais ou por menos, se chama {a}termo. [p=0.2] {b}Termos com a mesma letra são semelhantes, e só eles se juntam. [p=0.3] {c}Número sem letra só se junta com número sem letra. [p=0.3] {d}Com expoente na letra, como xis ao quadrado, a regra exige também o mesmo expoente. [p=0.2] Isso é assunto de outra aula."),
    # por que não vira cinco xis
    dict(id="s08", block="prova", text="E o três xis mais dois do começo? [p=0.2] São {a}três caixas e dois ovos soltos. [p=0.2] Não dá {b}cinco caixas. [p=0.3] Teste com um número: [p=0.2] se cada caixa tem {c}dez ovos, [p=0.2] três xis mais dois dá {d}trinta e dois ovos. [p=0.2] Cinco xis daria {e}cinquenta. [p=0.3] {f}Três xis mais dois já é a resposta final: não há o que juntar."),
    # mais termos
    dict(id="s09", block="exemplo", text="Veja uma mais bagunçada: [p=0.2] {a}cinco xis mais seis menos dois xis mais um. [p=0.3] {b}Os termos com xis: cinco xis e menos dois xis. [p=0.2] {c}Cinco menos dois dá três xis. [p=0.3] {d}Os números soltos: seis e um. [p=0.2] {e}Seis mais um dá sete. [p=0.3] Resultado: {f}três xis mais sete."),
    dict(id="s10", block="exemplo", text="Pode dar negativo também. [p=0.2] {a}Xis menos quatro xis: [p=0.2] você tem {b}um xis e tira quatro. [p=0.2] Como na dívida: {c}menos três xis. [p=0.3] E {d}menos dois xis menos três xis [p=0.2] é uma dívida de dois xis e outra de três xis: {e}menos cinco xis."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com um erro comum: [p=0.2] {a}esquecer o sinal que está na frente do termo. [p=0.2] Em cinco xis mais seis menos dois xis mais um, [p=0.2] a pessoa junta {b}cinco xis com dois xis e escreve sete xis mais sete. [p=0.3] Teste com dez: [p=0.2] a expressão original dá {c}trinta e sete. [p=0.2] Sete xis mais sete daria {d}setenta e sete. [p=0.3] {e}O menos estava ali: aqueles dois xis saem, não entram."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho: {a}marque cada termo com o sinal da frente. [p=0.2] {b}Circule os termos com xis, [p=0.2] {c}sublinhe os números soltos [p=0.2] e {d}leve junto o sinal de cada um. [p=0.3] Depois, é só juntar o que tem a mesma marca. [p=0.3] Na expressão bagunçada, {e}os circulados são cinco xis e menos dois xis. [p=0.2] {f}Os sublinhados são seis e um."),
    dict(id="s13", block="atalho", text="Funciona porque {a}a ordem dos termos não muda o resultado, [p=0.2] desde que {b}cada termo leve o próprio sinal. [p=0.3] É o mesmo raciocínio de separar entradas e saídas de dinheiro. [p=0.3] {c}Com poucos termos, não compensa: [p=0.2] junte de olho."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Simplifique: {a}seis xis mais sete menos xis menos dois."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] Termos com xis: {a}seis xis e menos xis. [p=0.2] Lembre que xis sozinho é um vezes xis: [p=0.2] {b}seis menos um dá cinco xis. [p=0.3] Números soltos: {c}sete menos dois dá cinco. [p=0.3] Resposta: {d}cinco xis mais cinco."),
    dict(id="s17", block="resposta", text="Confira com dez: [p=0.2] {a}sessenta mais sete menos dez menos dois dá cinquenta e cinco. [p=0.2] {b}Cinco vezes dez mais cinco também. [p=0.2] {c}Bateu."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}só se junta o que é semelhante, [p=0.2] {b}cada termo com o seu sinal."),
    dict(id="s19", block="fim", text="Na próxima aula, você {a}abre parênteses com um número na frente, [p=0.2] como {b}menos dois, abre parênteses, xis menos cinco, fecha parênteses, [p=0.2] sem errar {c}o sinal. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
