# Estudativo · MAT-EQU-001 — A letra no lugar de um número (Matemática · Equações do 1º Grau).
# Habilidade: ler 2x + 3 sabendo que 2x é 2 vezes x e escrever 'o dobro de um número mais 3' em linguagem matemática.
# Pré-requisitos: MAT-NUM-014 (montar a expressão de um problema). Próxima: MAT-EQU-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis".
# Questão inédita, criada para esta aula. Preços do estacionamento inventados para a conta.
# Sem negativo, potência ou fração: fora da ficha desta aula.
# Contas: x = 5 → 2x = 10 (25 é o erro) · 2 × 5 + 3 = 13 · 2 × 8 + 3 = 19 · x = 10: 2x + 3 = 23, 2(x + 3) = 26, x + 2 = 12.
# Teste com 2: 2x = 4 e x + 2 = 4 (coincidência). Questão: 3x − 4; x = 10 → 26.

TITULO = "A letra no lugar de um número"

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
    dict(id="s01", block="gancho", text="{a}Se xis vale cinco, [p=0.2] quanto vale {b}dois xis? [p=0.3] Se você pensou em {c}vinte e cinco, [p=0.2] juntou os algarismos. [p=0.3] A resposta é {d}dez."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você lê uma conta com letra [p=0.2] e escreve uma frase em linguagem matemática, [p=0.2] com um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}duas coisas. [p=0.2] {b}Expressão é uma conta com mais de uma operação. [p=0.2] E {c}a ordem: parênteses, depois vezes e dividido, por último mais e menos. [p=0.3] Se faltar alguma, procure no canal."),
    # por que uma letra
    dict(id="s04", block="estacionamento", text="Imagine {a}um estacionamento que cobra três reais na entrada [p=0.2] e {b}mais dois reais por hora. [p=0.3] Ficou {c}cinco horas? [p=0.2] {d}Dois vezes cinco mais três: treze reais. [p=0.3] Ficou {e}oito horas? [p=0.2] {f}Dois vezes oito mais três: dezenove."),
    dict(id="s05", block="estacionamento", text="Repare que {a}a conta é sempre a mesma. [p=0.2] Só muda {b}o número de horas. [p=0.3] Então, em vez de escrever uma conta para cada dia, [p=0.2] a gente põe {c}uma letra no lugar desse número. [p=0.2] A mais usada é {d}o xis."),
    dict(id="s06", block="estacionamento", text="O preço fica {a}dois vezes xis mais três. [p=0.3] {b}A letra guarda o lugar de um número. [p=0.2] Pode ser um número que muda, como as horas, [p=0.2] ou um número que você ainda não sabe."),
    # ler
    dict(id="s07", block="ler", text="Aqui entra um costume da matemática. [p=0.2] Entre um número e uma letra, {a}o vezes fica escondido. [p=0.3] Em vez de dois vezes xis, escreve-se só {b}dois xis, [p=0.2] com o número colado na frente da letra. [p=0.3] Motivo: {c}o sinal de vezes parece um xis, [p=0.2] e a conta viraria uma confusão."),
    dict(id="s08", block="ler", text="Por isso, {a}dois xis é dois vezes xis. [p=0.2] {b}Quando xis vale cinco, a conta é dois vezes cinco: dez. [p=0.3] Não é vinte e cinco: [p=0.2] {c}a letra não é um algarismo para colar no dois. [p=0.3] E {d}xis sozinho é um vezes xis: [p=0.2] o número um está ali, só não se escreve."),
    dict(id="s09", block="ler", text="Para ler {a}dois xis mais três, [p=0.2] use a ordem das operações. [p=0.2] {b}Primeiro o vezes: duas vezes o número. [p=0.2] {c}Depois o mais: mais três. [p=0.3] Em palavras: {d}o dobro de um número [p=0.2] mais três. [p=0.2] Dobro é {e}duas vezes."),
    # escrever
    dict(id="s10", block="escrever", text="O caminho de volta é {a}escrever a frase em linguagem matemática. [p=0.2] Troque {b}pedaço por pedaço. [p=0.3] {c}Um número: xis. [p=0.2] {d}O dobro de um número: dois xis. [p=0.2] {e}Mais três: mais três. [p=0.3] Resultado: {f}dois xis mais três."),
    dict(id="s11", block="escrever", text="Outra palavra que aparece muito: [p=0.2] {a}triplo é três vezes. [p=0.2] O triplo de um número é {b}três xis. [p=0.3] E {c}um número mais quatro é {d}xis mais quatro."),
    dict(id="s12", block="escrever", text="Cuidado com uma frase parecida: [p=0.2] {a}o dobro da soma de um número com três. [p=0.3] Aqui, o dobro vale para {b}a soma inteira, [p=0.2] e a soma inteira vai {c}entre parênteses: [p=0.2] {d}dois, abre parênteses, xis mais três, fecha parênteses. [p=0.3] Entre o dois e o parêntese, o vezes também fica escondido. [p=0.3] A pista é a palavra soma: [p=0.2] sem ela, o dobro pega só o número. [p=0.3] Com o número dez, a primeira frase dá {e}vinte e três [p=0.2] e esta dá {f}vinte e seis."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com um erro muito comum: [p=0.2] escrever o dobro de um número como {a}xis mais dois. [p=0.3] Dobro não é somar dois. [p=0.2] {b}É multiplicar por dois. [p=0.3] Teste com o número dez: [p=0.2] o dobro de dez é {c}vinte. [p=0.2] Xis mais dois daria {d}doze."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}o teste do dez. [p=0.2] Escreveu a expressão? [p=0.2] {b}Troque o xis por dez [p=0.2] e {c}confira se dá o mesmo que a frase."),
    dict(id="s15", block="atalho", text="Em dois xis mais três: [p=0.2] {a}a frase diz o dobro de dez mais três, que dá vinte e três. [p=0.2] {b}A expressão dá dois vezes dez mais três, também vinte e três. [p=0.2] {c}Bateu."),
    dict(id="s16", block="atalho", text="Funciona porque {a}o xis é um número. [p=0.2] Se a expressão está certa, ela acerta {b}qualquer número que você puser. [p=0.3] Só {c}não teste com o número dois: [p=0.2] o dobro dele e ele mais dois dão o mesmo quatro, [p=0.2] e o erro passa escondido. [p=0.3] E {d}não compensa em frase de uma conta só, [p=0.2] como um número mais quatro: escreva direto."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Escreva em linguagem matemática: [p=0.2] {a}pense em um número, calcule o triplo dele e tire quatro. [p=0.3] Depois, {b}confira com o teste do dez."),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá, pedaço por pedaço. [p=0.2] {a}Um número: xis. [p=0.2] {b}O triplo dele: três xis. [p=0.2] {c}Tire quatro: menos quatro. [p=0.3] Resposta: {d}três xis menos quatro."),
    dict(id="s20", block="resposta", text="O teste: [p=0.2] o triplo de dez dá trinta. [p=0.2] {a}Tirando quatro, fica vinte e seis. [p=0.2] {b}Três vezes dez menos quatro também dá vinte e seis. [p=0.2] {c}Bateu."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}a letra guarda o lugar de um número, [p=0.2] e {b}número colado na letra é vezes."),
    dict(id="s22", block="fim", text="Na próxima aula, você {a}troca a letra por números, [p=0.2] {b}até negativos, [p=0.2] e descobre por que {c}o parêntese é obrigatório nessa troca. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
