# Estudativo · MAT-MTZ-008 — Sistema como matriz e regra de Cramer (Matemática · Matrizes e Sistemas).
# Habilidade: escrever um sistema como AX = B e resolver 2x + y = 5, x + y = 3 por determinantes (x = 2, y = 1).
# Pré-requisitos: MAT-MTZ-004 (inversa), MAT-MTZ-006 (escalonamento); usa MAT-MTZ-002 e 003 (já ensinados). Próxima: MAT-MTZ-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Discussão de sistema (MAT-MTZ-007) não está na ficha: D = 0 é citado como outra aula.
# "D xis" e "D ípsilon" narrados como se escrevem: Dx e Dy na tela.

TITULO = "Sistema como matriz e regra de Cramer"

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
    dict(id="s01", block="gancho", text="{a}Dois xis mais ípsilon igual a cinco; [p=0.2] xis mais ípsilon igual a três. [p=0.3] Dá para resolver esse sistema {b}só com determinantes, [p=0.2] sem somar nem substituir nada. [p=0.3] {c}Xis igual a dois, ípsilon igual a um."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você escreve um sistema como multiplicação de matrizes, [p=0.2] resolve pela regra de Cramer [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre {a}duas coisas: [p=0.2] {b}multiplicar matrizes é linha por coluna, [p=0.2] e {c}o determinante da dois por dois é a principal menos a secundária. [p=0.3] Se faltar alguma, procure no canal."),
    # forma de matriz
    dict(id="s04", block="forma", text="Separe o sistema em três partes. [p=0.2] {a}Os números da frente das letras formam a matriz A: [p=0.2] dois, um, um, um. [p=0.3] {b}As letras formam a coluna X: xis e ípsilon. [p=0.3] {c}Os números depois do igual formam a coluna B: cinco e três."),
    dict(id="s05", block="forma", text="Agora, {a}A vezes X, linha por coluna. [p=0.2] {b}Linha um: dois vezes xis, mais um vezes ípsilon. [p=0.2] {c}Linha dois: um vezes xis, mais um vezes ípsilon. [p=0.3] {d}É o sistema de volta. [p=0.2] Por isso, ele se escreve {e}A vezes X igual a B."),
    # Cramer
    dict(id="s06", block="cramer", text="A regra de Cramer usa {a}três determinantes. [p=0.3] {b}D, o determinante de A: [p=0.2] dois vezes um, menos um vezes um: {c}um."),
    dict(id="s07", block="cramer", text="{a}D xis: troque a coluna do xis pela coluna B. [p=0.2] Fica {b}cinco, um, três, um. [p=0.3] {c}Cinco vezes um, menos um vezes três: dois."),
    dict(id="s08", block="cramer", text="{a}D ípsilon: troque a coluna do ípsilon pela coluna B. [p=0.2] Fica {b}dois, cinco, um, três. [p=0.3] {c}Dois vezes três, menos cinco vezes um: um."),
    dict(id="s09", block="cramer", text="{a}Xis é D xis dividido por D: dois dividido por um, dois. [p=0.3] {b}Ípsilon é D ípsilon dividido por D: um dividido por um, um. [p=0.3] {c}Confira: duas vezes dois, mais um, cinco. [p=0.2] Bateu."),
    # pela inversa
    dict(id="s10", block="inversa", text="Tem outro caminho, com a inversa. [p=0.2] Essa matriz A {a}é a mesma da aula de inversa, [p=0.2] e a inversa dela é {b}um, menos um, menos um, dois. [p=0.3] Multiplicando pela inversa, o A some, [p=0.2] e {c}X é a inversa vezes B. [p=0.3] {d}Linha um: cinco menos três, dois. [p=0.2] {e}Linha dois: menos cinco mais seis, um."),
    dict(id="s11", block="inversa", text="E se {a}D der zero? [p=0.2] Cramer não funciona: {b}dividiria por zero. [p=0.3] Aí o sistema tem infinitas soluções ou nenhuma, [p=0.2] e isso é {c}assunto de outra aula."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}trocar a coluna errada. [p=0.3] Quem troca a coluna do ípsilon achando que é a do xis [p=0.2] acha {b}xis igual a um. [p=0.3] Mas, com xis igual a um, a segunda equação dá ípsilon igual a dois, [p=0.2] e a primeira fica {c}dois mais dois, quatro, e não cinco. [p=0.3] {d}A primeira coluna é do xis; a segunda, do ípsilon."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: [p=0.2] {a}se a pergunta quer só uma letra, calcule só dois determinantes: [p=0.2] D e o daquela letra. [p=0.3] Funciona porque {b}cada letra tem a sua fração, separada das outras. [p=0.3] {c}No três por três, Cramer pede quatro Sarrus: [p=0.2] aí, escalonar costuma ser mais rápido."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Pela regra de Cramer, resolva: [p=0.2] {a}três xis mais dois ípsilon igual a doze; [p=0.2] {b}xis menos ípsilon igual a menos um."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}D: três vezes menos um, menos dois vezes um: [p=0.2] menos três menos dois, menos cinco. [p=0.3] {b}D xis: doze vezes menos um, menos dois vezes menos um: [p=0.2] menos doze mais dois, menos dez. [p=0.3] {c}D ípsilon: três vezes menos um, menos doze vezes um: [p=0.2] menos três menos doze, menos quinze."),
    dict(id="s17", block="resposta", text="{a}Xis: menos dez dividido por menos cinco, dois. [p=0.2] {b}Ípsilon: menos quinze dividido por menos cinco, três. [p=0.2] Sinais iguais na divisão dão positivo. [p=0.3] {c}Confira: três vezes dois, mais duas vezes três: doze. [p=0.2] Bateu."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}o sistema é A vezes X igual a B. [p=0.2] {b}Cada letra é o seu determinante dividido por D. [p=0.2] E {c}com D zero, Cramer não serve."),
    dict(id="s19", block="fim", text="A próxima aula é de {a}prática: [p=0.2] você resolve e discute sistemas de até três equações [p=0.2] em {b}questões no estilo de prova. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
