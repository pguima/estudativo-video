# Estudativo · MAT-EQU-005 — Multiplicar termos com letra e duas expressões (Matemática · Equações do 1º Grau).
# Habilidade: calcular 3x · 2x = 6x² e abrir (x + 2)(x + 3) em x² + 5x + 6.
# Pré-requisitos: MAT-EQU-004 (distributiva), MAT-POT-003 (potências de mesma base). Próxima: MAT-EQU-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis".
# Questão inédita, criada para esta aula. Área explicada na hora (piso de lajotas, como em MAT-POT-001): não está em "Já ensinado".
# 3x · 2x = 6x² (x = 10: 30 × 20 = 600; erros 5x e 6x) · 2x² · 4x = 8x³ · x + x² em 10 = 110, 2x³ = 2.000.
# (x + 2)(x + 3) = x² + 3x + 2x + 6 = x² + 5x + 6 (x = 10: 12 × 13 = 156; erro x² + 6 = 106).
# Atalho (x + a)(x + b) = x² + (a + b)x + ab; não vale com número na frente do x. Questão: (x + 4)(x − 1) = x² + 3x − 4.

TITULO = "Multiplicar termos com letra e duas expressões"

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
    dict(id="s01", block="gancho", text="{a}Três xis vezes dois xis. [p=0.3] Se deu {b}cinco xis, você somou. [p=0.2] Se deu {c}seis xis, perdeu um xis no caminho. [p=0.3] A resposta é {d}seis xis ao quadrado."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você multiplica termos com letra [p=0.2] e abre {b}dois parênteses multiplicados, [p=0.2] com um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Três lembretes. [p=0.2] {a}Xis vezes xis é xis ao quadrado: a base aparece duas vezes. [p=0.2] {b}Na mesma base, multiplicando, repete a base e soma os expoentes. [p=0.2] E {c}o número de fora multiplica cada termo de dentro. [p=0.3] Se faltar alguma, procure no canal."),
    # termo vezes termo
    dict(id="s04", block="termos", text="Três xis vezes dois xis é {a}três vezes xis vezes dois vezes xis. [p=0.3] Na multiplicação, {b}a ordem não muda o resultado. [p=0.2] Então junte {c}números com números [p=0.2] e {d}letras com letras."),
    dict(id="s05", block="termos", text="{a}Três vezes dois dá seis. [p=0.2] {b}Xis vezes xis dá xis ao quadrado. [p=0.3] Resultado: {c}seis xis ao quadrado. [p=0.3] Teste com dez: [p=0.2] {d}trinta vezes vinte dá seiscentos. [p=0.2] {e}Seis vezes cem também dá seiscentos."),
    dict(id="s06", block="termos", text="Com expoente, a regra de mesma base resolve. [p=0.2] {a}Dois xis ao quadrado vezes quatro xis. [p=0.2] {b}Dois vezes quatro dá oito. [p=0.2] {c}Xis ao quadrado vezes xis, que tem expoente um: [p=0.2] os expoentes somam dois mais um, que dá três. [p=0.3] {d}Fica xis ao cubo. [p=0.3] Resultado: {e}oito xis ao cubo."),
    # somar não é multiplicar
    dict(id="s07", block="contraste", text="Cuidado para não misturar com a soma. [p=0.2] {a}Três xis mais dois xis dá cinco xis: [p=0.2] são termos semelhantes, e a letra fica igual. [p=0.3] {b}Três xis vezes dois xis dá seis xis ao quadrado: [p=0.2] na multiplicação, a letra ganha expoente."),
    dict(id="s08", block="contraste", text="E {a}xis mais xis ao quadrado? [p=0.2] Muita gente escreve {b}dois xis ao cubo. [p=0.3] Mas xis e xis ao quadrado {c}não são semelhantes: [p=0.2] a letra é a mesma, e o expoente é diferente. [p=0.3] Teste com dez: [p=0.2] {d}dez mais cem dá cento e dez. [p=0.2] Dois xis ao cubo daria {e}dois mil. [p=0.3] Na soma, {f}só se junta mesma letra com mesmo expoente. [p=0.2] Xis mais xis ao quadrado {g}fica como está."),
    # piso
    dict(id="s09", block="piso", text="E dois parênteses multiplicados? [p=0.2] {a}Abre parênteses, xis mais dois, fecha parênteses, [p=0.2] vezes, {b}abre parênteses, xis mais três, fecha parênteses. [p=0.3] Para ver o que acontece, pense em {c}um piso retangular."),
    dict(id="s10", block="piso", text="O número de lajotas que cobre um piso é a {a}área dele. [p=0.2] Um piso de {b}três fileiras de quatro lajotas [p=0.2] tem {c}três vezes quatro: doze lajotas. [p=0.3] Área de retângulo é {d}um lado vezes o outro."),
    dict(id="s11", block="piso", text="Monte um piso com {a}xis mais dois de um lado [p=0.2] e {b}xis mais três do outro. [p=0.2] A área é {c}a nossa conta. [p=0.3] {d}Corte o piso nas emendas: [p=0.2] ficam {e}quatro pedaços."),
    dict(id="s12", block="piso", text="{a}Xis vezes xis dá xis ao quadrado. [p=0.2] {b}Xis vezes três dá três xis. [p=0.2] {c}Dois vezes xis dá dois xis. [p=0.2] {d}Dois vezes três dá seis. [p=0.3] Somando os pedaços: {e}xis ao quadrado mais três xis mais dois xis mais seis."),
    dict(id="s13", block="piso", text="Juntando os semelhantes: {a}xis ao quadrado mais cinco xis mais seis. [p=0.3] Teste com dez: [p=0.2] a área fica {b}doze vezes treze, que dá cento e cinquenta e seis. [p=0.2] Pela expressão: {c}cem mais cinquenta mais seis, também cento e cinquenta e seis. [p=0.2] {d}Bateu."),
    # chuveirinho
    dict(id="s14", block="chuveirinho", text="Sem desenho, o jeito é o {a}chuveirinho. [p=0.2] O nome vem das setas: de cada termo saem setas para todos os termos do outro parêntese, como a água de um chuveiro. [p=0.3] {b}Cada termo do primeiro parêntese multiplica cada termo do segundo. [p=0.3] {c}Xis vezes xis. [p=0.2] {d}Xis vezes três. [p=0.2] {e}Dois vezes xis. [p=0.2] {f}Dois vezes três. [p=0.3] São {g}os mesmos quatro pedaços do piso."),
    # erro
    dict(id="s15", block="erro", text="O erro mais comum é {a}multiplicar só primeiro com primeiro e último com último: [p=0.2] {b}xis ao quadrado mais seis. [p=0.3] No piso, isso {c}apaga as faixas do meio. [p=0.2] Com dez, daria {d}cento e seis, [p=0.2] e não cento e cinquenta e seis."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho, para parênteses do tipo {a}xis mais um número. [p=0.3] {b}Na frente, xis ao quadrado. [p=0.2] {c}No meio, a soma dos números: dois mais três dá cinco, então cinco xis. [p=0.2] {d}No fim, a multiplicação dos números: dois vezes três dá seis."),
    dict(id="s17", block="atalho", text="Funciona porque {a}as faixas do meio são dois xis e três xis, [p=0.2] e {b}o cantinho é dois vezes três. [p=0.3] {c}Vale com sinal de menos, levando o sinal junto. [p=0.2] {d}Não vale se o xis tiver número na frente, [p=0.2] como em dois xis mais um: [p=0.2] aí, use o chuveirinho."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Multiplique {a}abre parênteses, xis mais quatro, fecha parênteses, [p=0.2] vezes, {b}abre parênteses, xis menos um, fecha parênteses."),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá, pelo chuveirinho. [p=0.2] {a}Xis vezes xis: xis ao quadrado. [p=0.2] {b}Xis vezes menos um: menos xis. [p=0.2] {c}Quatro vezes xis: quatro xis. [p=0.2] {d}Quatro vezes menos um: menos quatro."),
    dict(id="s21", block="resposta", text="Juntando: {a}menos xis mais quatro xis dá três xis. [p=0.2] Resposta: {b}xis ao quadrado mais três xis menos quatro. [p=0.3] Pelo atalho: {c}quatro menos um dá três, [p=0.2] e {d}quatro vezes menos um dá menos quatro. [p=0.2] {e}Bateu."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}na multiplicação, a letra ganha expoente, [p=0.2] e no chuveirinho {b}todo termo multiplica todo termo."),
    dict(id="s23", block="fim", text="Na próxima aula, você {a}pratica tudo isso: [p=0.2] {b}traduz situações em expressões com letra [p=0.2] e {c}simplifica até o fim. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
