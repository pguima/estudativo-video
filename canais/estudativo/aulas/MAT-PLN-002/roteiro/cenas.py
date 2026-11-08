# Estudativo · MAT-PLN-002 — Divisão de polinômios e teorema do resto (Matemática · Polinômios · Operações e divisão de polinômios).
# Habilidade: dividir x² + 3x + 5 por x − 1 (quociente x + 4, resto 9) e achar o mesmo resto pelo atalho P(1) = 9.
# Pré-requisitos: MAT-PLN-001 (grau, P(x), valor numérico). Próxima: MAT-PLN-003.
# Equação (MAT-EQU-007) não está na ficha: "o número que zera o divisor" é achado de cabeça, sem resolver equação.
# Questão inédita, criada para esta aula. Nome do método: "método da chave", como na conta de números (MAT-NUM-009).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis"; a letra a se fala "á".

TITULO = "Divisão de polinômios e teorema do resto"

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
    dict(id="s01", block="gancho", text="{a}Xis ao quadrado mais três xis mais cinco, dividido por xis menos um. [p=0.3] A conta dá {b}quociente xis mais quatro e resto nove. [p=0.3] Mas esse nove sai {c}em três segundos, sem dividir nada."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você divide polinômios pelo método da chave [p=0.2] e acha o resto pelo atalho do {b}teorema do resto."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}duas coisas: [p=0.2] {b}o valor numérico, em que P de um é trocar o xis por um, [p=0.2] e {c}a divisão com resto: dezessete dividido por cinco dá três, e sobram dois. [p=0.3] Se faltar alguma, procure no canal."),
    # a ideia
    dict(id="s04", block="ideia", text="Na divisão de números, {a}dezessete é igual a cinco vezes três, mais dois. [p=0.2] {b}Dividendo é igual a divisor vezes quociente, mais resto. [p=0.2] E o resto é {c}menor que o divisor, senão caberia mais uma vez."),
    dict(id="s05", block="ideia", text="Com polinômios é igual: [p=0.2] {a}P de xis é igual ao divisor vezes o quociente, mais o resto. [p=0.2] Só que aqui, menor quer dizer {b}de grau menor. [p=0.3] Dividindo por xis menos um, que tem grau um, [p=0.2] {c}o resto não tem xis: é só um número."),
    # o método da chave
    dict(id="s06", block="chave", text="Monte {a}a chave, como na conta de números. [p=0.2] O método tem {b}três passos que se repetem: [p=0.2] {c}dividir, multiplicar e subtrair."),
    dict(id="s07", block="chave", text="{a}Dividir: só o primeiro termo de cada um. [p=0.2] Xis ao quadrado dividido por xis dá {b}xis. [p=0.2] É o primeiro pedaço do quociente. [p=0.3] {c}Multiplicar: xis vezes xis menos um dá xis ao quadrado menos xis."),
    dict(id="s08", block="chave", text="{a}Subtrair: tire esse resultado de cima, trocando os sinais dele. [p=0.2] {b}O xis ao quadrado desaparece. [p=0.2] {c}Três xis menos, abre parênteses, menos xis, fecha parênteses: quatro xis. [p=0.2] {d}Desça o cinco: fica quatro xis mais cinco."),
    dict(id="s09", block="chave", text="Repita com o que sobrou. [p=0.2] {a}Quatro xis dividido por xis: mais quatro. [p=0.2] {b}Quatro vezes xis menos um: quatro xis menos quatro. [p=0.2] {c}Trocando os sinais e somando: cinco mais quatro, nove."),
    dict(id="s10", block="chave", text="{a}Nove não tem xis: o grau ficou menor que o do divisor, e a conta para. [p=0.2] {b}Quociente xis mais quatro, resto nove. [p=0.3] Confira: {c}xis menos um, vezes xis mais quatro, dá xis ao quadrado mais três xis menos quatro. [p=0.2] {d}Mais nove: volta o polinômio do começo."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}esquecer de trocar os sinais na subtração. [p=0.2] A pessoa faz {b}três xis menos xis e escreve dois xis. [p=0.2] Repetindo o erro no fim, sai {c}quociente xis mais dois e resto três."),
    dict(id="s12", block="erro", text="{a}A conferência denuncia: não volta o polinômio do começo. [p=0.2] {b}Subtrair o parêntese inteiro é trocar todos os sinais dele."),
    # teorema do resto
    dict(id="s13", block="teorema", text="E o resto sem dividir? [p=0.2] Volte para {a}P de xis igual a xis menos um, vezes o quociente, mais o resto. [p=0.3] Troque o xis por {b}um, o número que zera o xis menos um. [p=0.2] {c}Um menos um dá zero, e zero vezes qualquer coisa dá zero. [p=0.2] Sobra {d}P de um igual ao resto."),
    dict(id="s14", block="teorema", text="{a}Um mais três mais cinco: nove. [p=0.2] O mesmo resto, sem chave. [p=0.3] Esse é o {b}teorema do resto: [p=0.2] {c}o resto da divisão por xis menos á é P de á."),
    dict(id="s15", block="teorema", text="E com mais no divisor? [p=0.2] Pergunte {a}que número zera o divisor. [p=0.2] {b}Xis mais dois zera com menos dois, [p=0.2] e o resto é {c}P de menos dois."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho de prova: {a}divisível quer dizer resto zero. [p=0.2] Para saber se um polinômio é divisível por xis menos á, [p=0.2] {b}basta ver se P de á dá zero. [p=0.3] Em {c}xis ao cubo menos oito, dividido por xis menos dois: [p=0.2] {d}dois ao cubo dá oito, e oito menos oito, zero. [p=0.2] {e}Divisível, sem armar a conta."),
    dict(id="s17", block="atalho", text="Funciona porque, com resto zero, {a}a divisão é exata, como doze dividido por três. [p=0.3] Mas {b}o atalho dá só o resto. [p=0.2] Se a questão pedir o quociente, {c}arme a chave. [p=0.2] E ele vale para {d}divisor do tipo xis mais ou menos um número."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Qual é o resto da divisão de {a}xis ao cubo mais dois xis ao quadrado menos cinco [p=0.2] por {b}xis mais dois?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] {a}Xis mais dois zera com xis igual a menos dois: [p=0.2] o resto é P de menos dois. [p=0.3] {b}Abre parênteses, menos dois, fecha parênteses, ao cubo: menos oito. [p=0.2] {c}Dois vezes, abre parênteses, menos dois, fecha parênteses, ao quadrado: dois vezes quatro, oito. [p=0.2] {d}Menos oito mais oito menos cinco: resto menos cinco."),
    dict(id="s21", block="resposta", text="Quem usou {a}mais dois no lugar de menos dois [p=0.2] calculou {b}oito mais oito menos cinco, onze. [p=0.2] {c}O número é o que zera o divisor: o sinal troca."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}na chave, divida, multiplique e subtraia, trocando os sinais, [p=0.2] e {b}o resto da divisão por xis menos á é P de á."),
    dict(id="s23", block="fim", text="Na próxima aula, você divide por xis menos um número {a}só com os coeficientes, [p=0.2] numa tabelinha chamada {b}Briô-Rufíni. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
