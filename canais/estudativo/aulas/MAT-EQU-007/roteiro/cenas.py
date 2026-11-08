# Estudativo · MAT-EQU-007 — O que é equação: fazer o mesmo nos dois lados (Matemática · Equações do 1º Grau).
# Habilidade: testar se x = 4 resolve 2x + 1 = 9 e resolver x + 7 = 12, 3x = 12 e x/4 = 5 com a ideia da balança.
# Pré-requisitos: MAT-EQU-002 (valor numérico), MAT-FRA-004 (frações maiores que 1), MAT-NUM-017 (multiplicar e dividir inteiros). Próxima: MAT-EQU-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "O que é equação: fazer o mesmo nos dois lados"

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
    dict(id="s01", block="gancho", text="{a}Dois xis mais um igual a nove. [p=0.3] Alguém diz que {b}xis vale quatro. [p=0.3] Será verdade? [p=0.2] Dá para saber em cinco segundos, {c}sem resolver nada."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai conferir e resolver equações com uma {b}balança, [p=0.2] e ainda leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}trocar a letra por um número e fazer a conta, [p=0.2] e {c}multiplicar e dividir, inclusive com sinal de menos. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é equação e como testar
    dict(id="s04", block="testar", text="Primeiro, o que é uma equação. [p=0.2] É uma conta com {a}um sinal de igual [p=0.2] e {b}uma letra no lugar de um número que você não conhece. [p=0.3] {c}Dois xis é dois vezes xis. [p=0.3] Resolver a equação é achar {d}o número que deixa os lados iguais."),
    dict(id="s05", block="testar", text="Vamos testar o quatro. [p=0.2] {a}Troque o xis por quatro. [p=0.2] {b}Dois vezes quatro dá oito. [p=0.2] {c}Oito mais um dá nove. [p=0.3] {d}Nove igual a nove: [p=0.2] o quatro {e}resolve a equação."),
    dict(id="s06", block="testar", text="E o três? [p=0.2] {a}Dois vezes três dá seis. Mais um dá sete. [p=0.3] {b}Sete não é nove. [p=0.2] O três {c}não serve. [p=0.3] Esse teste se chama {d}conferir substituindo, [p=0.2] e você vai usar em toda equação daqui para frente."),
    # a balança
    dict(id="s07", block="balanca", text="Mas como achar o número sem chutar? [p=0.3] Pense numa {a}balança de pratos, equilibrada. [p=0.2] O sinal de igual é {b}o equilíbrio: [p=0.2] o lado esquerdo pesa o mesmo que o direito."),
    dict(id="s08", block="balanca", text="Ela só continua equilibrada se você {a}fizer o mesmo nos dois lados. [p=0.3] {b}Tirou um peso de um prato? [p=0.2] Tire o mesmo peso do outro. [p=0.3] Essa é a regra de todas as equações."),
    dict(id="s09", block="somar", text="Veja {a}xis mais sete igual a doze. [p=0.3] Num prato, {b}uma caixa de peso desconhecido, que é o xis, [p=0.2] e {c}sete pesos de um quilo. [p=0.2] No outro prato, {d}doze pesos."),
    dict(id="s10", block="somar", text="Para deixar a caixa sozinha, {a}tire sete pesos do prato dela. [p=0.2] Para manter o equilíbrio, {b}tire sete do outro prato também. [p=0.3] Sobra {c}xis igual a cinco. [p=0.3] Conferindo: {d}cinco mais sete dá doze. [p=0.2] Bateu."),
    dict(id="s11", block="vezes", text="Agora, {a}três xis igual a doze: [p=0.2] {b}três caixas iguais num prato [p=0.2] e {c}doze pesos no outro. [p=0.3] {d}Divida cada prato em três partes iguais. [p=0.2] Uma caixa pesa {e}doze dividido por três: [p=0.2] {f}xis igual a quatro. [p=0.2] Conferindo: {g}três vezes quatro dá doze."),
    dict(id="s12", block="dividir", text="E {a}xis sobre quatro igual a cinco. [p=0.2] Xis sobre quatro quer dizer {b}xis dividido por quatro: [p=0.2] {c}um quarto da caixa pesa cinco quilos. [p=0.3] A caixa inteira são {d}quatro desses pedaços. [p=0.2] Então {e}multiplique cada prato por quatro: [p=0.2] {f}xis igual a vinte. [p=0.2] Conferindo: {g}vinte dividido por quatro dá cinco."),
    dict(id="s13", block="padrao", text="Repare no padrão. [p=0.2] {a}Número somando, subtraia. [p=0.2] {b}Número multiplicando a letra, divida. [p=0.2] {c}Número dividindo, multiplique. [p=0.2] {d}Número subtraindo, some. [p=0.3] E sempre {e}nos dois lados."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}usar a conta errada para tirar o número. [p=0.2] Em três xis igual a doze, a pessoa {b}subtrai três de cada lado [p=0.2] e escreve {c}xis igual a nove."),
    dict(id="s15", block="erro", text="Mas o três não está somando: [p=0.2] ele {a}multiplica o xis. [p=0.3] E a conferência denuncia: [p=0.2] {b}três vezes nove dá vinte e sete, [p=0.2] {c}e não doze. [p=0.3] Antes de mexer, pergunte: {d}esse número soma ou multiplica?"),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho: {a}em questão com alternativas, teste as alternativas. [p=0.3] Em vez de resolver, {b}substitua cada resposta na equação [p=0.2] e veja {c}qual deixa os lados iguais."),
    dict(id="s17", block="atalho", text="Funciona porque {a}conferir é mais rápido que resolver, [p=0.2] como você fez com o quatro no começo. [p=0.3] {b}Não compensa quando as alternativas têm números grandes ou quebrados: [p=0.2] aí, {c}use a balança."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Resolva {a}xis menos seis igual a nove. [p=0.3] {b}Quanto vale xis?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] O seis está {a}subtraindo, então some seis. [p=0.2] {b}Nos dois lados. [p=0.3] À esquerda, menos seis mais seis {c}dá zero, e sobra o xis. [p=0.2] À direita, {d}nove mais seis dá quinze. [p=0.3] {e}Xis igual a quinze. [p=0.3] Na balança, não dá para desenhar um peso negativo, [p=0.2] mas a regra não muda: com sinal de menos também, faça o mesmo nos dois lados."),
    dict(id="s21", block="resposta", text="Conferindo: {a}quinze menos seis dá nove. [p=0.2] Bateu. [p=0.3] Quem subtraiu seis achou {b}três, [p=0.2] mas três menos seis {c}dá menos três. [p=0.2] Não dá nove."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}equação é uma balança. [p=0.2] {b}Faça o mesmo nos dois lados [p=0.2] e {c}confira substituindo."),
    dict(id="s23", block="fim", text="Na próxima aula, a equação ganha {a}mais de um passo [p=0.2] e {b}xis nos dois pratos da balança. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
