# Estudativo · MAT-PLN-005 — Multiplicidade, gráfico e sinal de um polinômio (Matemática · Polinômios · Raízes e relações de Girard).
# Habilidade: ler em y = (x − 1)²(x + 2) que o gráfico toca o eixo em 1 e corta em −2 e resolver (x − 1)²(x + 2) > 0 (x > −2 e x ≠ 1).
# Pré-requisitos: MAT-FUN-007 (zeros de um gráfico), MAT-FUN-023 (quadro de sinais), MAT-PLN-004 (forma fatorada). Próxima: MAT-PLN-006.
# Em MAT-FUN-023, o atalho "o sinal troca a cada raiz" já avisava que não vale com fator ao quadrado: esta aula completa o aviso.
# Questão inédita, criada para esta aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis", y "ípsilon".

TITULO = "Multiplicidade, gráfico e sinal de um polinômio"

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
    dict(id="s01", block="gancho", text="{a}Ípsilon igual a xis menos um, ao quadrado, vezes xis mais dois. [p=0.3] {b}No menos dois, o gráfico atravessa o eixo xis. [p=0.2] {c}No um, ele só encosta e volta. [p=0.3] E dá para saber isso {d}sem marcar ponto nenhum."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você lê o gráfico e o sinal de um polinômio direto da forma fatorada, [p=0.2] com um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}três coisas: [p=0.2] {b}a forma fatorada, em que cada raiz vira um parêntese; [p=0.2] {c}os zeros de um gráfico, onde ele encontra o eixo xis; [p=0.2] e {d}o quadro de sinais de uma multiplicação. [p=0.3] Se faltar alguma, procure no canal."),
    # multiplicidade
    dict(id="s04", block="mult", text="Em xis menos um, ao quadrado, vezes xis mais dois, [p=0.2] {a}o parêntese xis menos um aparece duas vezes. [p=0.2] Então {b}o um é raiz dupla: [p=0.2] tem {c}multiplicidade dois. [p=0.3] {d}O menos dois aparece uma vez: raiz simples, multiplicidade um."),
    dict(id="s05", block="mult", text="{a}Multiplicidade é quantas vezes o parêntese da raiz aparece. [p=0.2] Na forma fatorada, ela é {b}o expoente do parêntese."),
    # sinal
    dict(id="s06", block="sinal", text="Para entender o gráfico, estude o sinal. [p=0.2] {a}Xis menos um, ao quadrado, nunca é negativo, [p=0.2] porque {b}todo número ao quadrado dá zero ou positivo. [p=0.3] Então, fora do um, {c}o sinal do produto é o sinal de xis mais dois."),
    dict(id="s07", block="sinal", text="{a}Antes do menos dois, xis mais dois é negativo: o produto é negativo. [p=0.2] {b}Depois do menos dois, positivo. [p=0.3] E {c}no um, o produto vale zero, mas não troca de sinal: [p=0.2] {d}positivo antes, positivo depois."),
    # gráfico
    dict(id="s08", block="grafico", text="No gráfico, isso vira {a}duas cenas. [p=0.2] {b}No menos dois, o sinal troca: o gráfico vem de baixo e cruza o eixo. [p=0.3] {c}No um, o sinal não troca: o gráfico desce, encosta no eixo e volta a subir."),
    dict(id="s09", block="grafico", text="A regra: {a}multiplicidade ímpar, o gráfico corta o eixo. [p=0.2] {b}Multiplicidade par, só toca e volta. [p=0.3] E o gráfico passa por {c}xis zero, ípsilon dois, [p=0.2] porque {d}menos um, ao quadrado, vezes dois dá dois."),
    # inequação
    dict(id="s10", block="inequacao", text="Resolva, então, {a}xis menos um, ao quadrado, vezes xis mais dois, maior que zero. [p=0.2] O gráfico tem que estar {b}acima do eixo. [p=0.3] Isso acontece {c}depois do menos dois, [p=0.2] {d}exceto no um, onde ele vale zero. [p=0.3] Resposta: {e}xis maior que menos dois e xis diferente de um."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}trocar o sinal em toda raiz. [p=0.2] A pessoa põe mais depois do um, {b}menos entre menos dois e um, [p=0.2] e mais antes do menos dois. [p=0.3] Teste o {c}zero, que fica entre menos dois e um: [p=0.2] {d}dá dois, positivo. [p=0.2] {e}Raiz dupla não troca o sinal."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho do sinal, sem quadro: [p=0.2] {a}depois da maior raiz, comece com mais. [p=0.2] Andando para a esquerda, {b}raiz de multiplicidade ímpar troca o sinal, [p=0.2] e {c}raiz de multiplicidade par mantém. [p=0.3] Aqui: {d}mais depois do um, [p=0.2] {e}mais entre menos dois e um, [p=0.2] {f}menos antes do menos dois."),
    dict(id="s13", block="atalho", text="Funciona porque, depois da maior raiz, {a}todo parêntese é positivo. [p=0.2] Ao passar por uma raiz, {b}só o parêntese dela muda de sinal, [p=0.2] uma vez para cada repetição. [p=0.3] {c}Não vale com parêntese do tipo três menos xis, [p=0.2] nem com número negativo na frente de tudo: [p=0.2] aí, faça o quadro."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Resolva {a}xis mais um, vezes xis menos três, ao quadrado, menor ou igual a zero."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] Raízes: {a}menos um, simples, [p=0.2] e {b}três, dupla. [p=0.3] {c}Depois do três: mais. [p=0.2] {d}O três é raiz dupla, mantém: mais entre menos um e três. [p=0.2] {e}O menos um é raiz simples, troca: menos antes do menos um."),
    dict(id="s17", block="resposta", text="Menor ou igual a zero pede {a}o pedaço com menos e os zeros. [p=0.2] {b}Xis menor ou igual a menos um. [p=0.2] E {c}o três também, porque ali o produto vale zero. [p=0.3] Resposta: {d}xis menor ou igual a menos um, ou xis igual a três. [p=0.2] Quem esqueceu o três {e}perdeu o ponto onde o gráfico só encosta."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}o expoente do parêntese é a multiplicidade, [p=0.2] {b}ímpar corta, par encosta, [p=0.2] e {c}o sinal só troca nas raízes de multiplicidade ímpar."),
    dict(id="s19", block="fim", text="Na próxima aula, você descobre {a}a soma e o produto das raízes [p=0.2] de um polinômio de grau três {b}sem resolver a equação. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
