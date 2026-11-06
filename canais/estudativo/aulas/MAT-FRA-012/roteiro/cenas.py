# Estudativo · MAT-FRA-012 — Expressões com frações, inclusive negativas (Matemática · Frações e Decimais).
# Habilidade: resolver 1/2 + 2/3 × 3/4 e −2/3 + 1/4, inclusive com número misto.
# Pré-requisitos: MAT-FRA-004 (número misto), MAT-FRA-008 (denominadores diferentes), MAT-FRA-011 (dividir), MAT-NUM-018 (expressões com inteiros). Próxima: MAT-FRA-013.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula.

TITULO = "Expressões com frações, inclusive negativas"

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
    dict(id="s01", block="gancho", text="{a}Um meio mais dois terços vezes três quartos. [p=0.3] Se você fez na ordem em que leu, [p=0.2] deu {b}sete oitavos. [p=0.3] {c}Errado. [p=0.2] A resposta é {d}um."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai resolver contas com várias frações, [p=0.2] {b}negativas [p=0.2] e {c}número misto, [p=0.2] e ainda leva um {d}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Quatro lembretes. [p=0.2] {a}Ordem das operações: parênteses, depois vezes e dividido, por último mais e menos."),
    dict(id="s04", block="lembrete", text="{a}Regra de sinais: multiplicando ou dividindo, sinais iguais dão mais, e sinais diferentes dão menos."),
    dict(id="s05", block="lembrete", text="{a}Número misto, um inteiro junto com uma fração, vira fração assim: [p=0.2] inteiro vezes o de baixo, mais o de cima. [p=0.2] O de baixo se repete. [p=0.3] E somar com denominadores diferentes pede {b}o MMC, o menor múltiplo comum. [p=0.3] Se faltar alguma coisa, procure a aula no canal."),
    # ordem
    dict(id="s06", block="ordem", text="Voltando ao começo. [p=0.2] O vezes vem antes do mais, então {a}separe dois terços vezes três quartos. [p=0.3] Corte em cruz: {b}fica um meio."),
    dict(id="s07", block="ordem", text="Sobrou {a}um meio mais um meio: {b}um. [p=0.3] Quem soma antes {c}muda a conta. [p=0.2] Frações obedecem à mesma ordem de sempre. [p=0.3] E aqueles sete oitavos? [p=0.2] São a resposta de outra conta, {d}com parênteses em um meio mais dois terços. [p=0.2] Parêntese manda fazer a soma primeiro."),
    # negativas
    dict(id="s08", block="negativas", text="E com fração negativa? [p=0.2] {a}Menos dois terços mais um quarto. [p=0.3] Comece como em qualquer soma: MMC de três e quatro, {b}doze."),
    dict(id="s09", block="negativas", text="{a}Menos dois terços vira menos oito doze avos. [p=0.2] {b}Um quarto vira três doze avos. [p=0.3] O sinal vai com o de cima: {c}menos oito mais três. [p=0.3] Você devia oito e pagou três: ainda deve cinco. [p=0.2] {d}Menos cinco doze avos."),
    dict(id="s10", block="negativas", text="Na multiplicação, {a}decida o sinal primeiro. [p=0.2] {b}Menos dois quintos vezes cinco sextos: sinais diferentes, {c}dá menos. [p=0.3] Depois, a conta normal: {d}um terço. [p=0.2] Resposta: {e}menos um terço. [p=0.3] Com sinais iguais, {f}menos um meio vezes menos dois terços dá {g}mais um terço."),
    # misto
    dict(id="s11", block="misto", text="E o número misto? [p=0.2] {a}Transforme em fração antes de qualquer conta. [p=0.3] {b}Dois inteiros e um quarto vezes dois terços. [p=0.3] Dois vezes quatro, oito, mais um: {c}nove quartos."),
    dict(id="s12", block="misto", text="{a}Nove quartos vezes dois terços. [p=0.2] Corte em cruz: {b}nove e três, {c}dois e quatro. [p=0.3] Fica {d}três meios, [p=0.2] que é {e}um inteiro e um meio."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum junta o misto e o sinal. [p=0.2] Veja {a}menos um inteiro e um meio mais três quartos. [p=0.3] Muita gente lê {b}menos um, mais um meio, [p=0.2] e acha que aquilo vale {c}menos um meio."),
    dict(id="s14", block="erro", text="Pense em dívida: quem deve um real e meio deve mais de um real, não cinquenta centavos. [p=0.3] {a}O sinal vale para o misto todo. [p=0.2] Transforme sem o sinal, {b}três meios, [p=0.2] e devolva o sinal: {c}menos três meios. [p=0.3] Com denominador quatro, {d}menos seis quartos mais três quartos: {e}menos três quartos."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho dos blocos, que você já viu com números inteiros: {a}separe a conta nos sinais de mais e de menos. [p=0.3] Cada pedaço vira {b}um bloco, resolvido sozinho. [p=0.2] Só no fim, {c}junte os blocos."),
    dict(id="s16", block="atalho", text="Veja: {a}sete oitavos menos um quarto dividido por dois terços. [p=0.3] {b}Separe no sinal de menos. [p=0.2] O bloco da direita vira {c}um quarto vezes três meios: {d}três oitavos. [p=0.3] Junte: {e}sete oitavos menos três oitavos, {f}quatro oitavos, [p=0.2] que simplifica para {g}um meio."),
    dict(id="s17", block="atalho", text="Funciona porque vezes e dividido vêm antes, então ficam {a}grudados no mesmo bloco. [p=0.3] Só não separe no {b}sinal colado na fração: [p=0.2] o menos do começo da conta, ou logo depois de um vezes ou dividido, é da própria fração. [p=0.2] {c}Menos um meio vezes menos dois terços é um bloco só. [p=0.3] E não serve com {d}parênteses: [p=0.2] o que está dentro deles é um bloco só, mesmo com mais ou menos, e vem primeiro."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Resolva: {a}menos um inteiro e um terço [p=0.2] {b}mais quatro quintos vezes cinco oitavos."),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá, em blocos. [p=0.2] Primeiro bloco: {a}um inteiro e um terço é quatro terços, [p=0.2] então {b}menos quatro terços. [p=0.3] Segundo bloco: {c}quatro quintos vezes cinco oitavos. [p=0.2] Corte em cruz: {d}um meio."),
    dict(id="s21", block="resposta", text="Junte: {a}menos quatro terços mais um meio. [p=0.2] MMC de três e dois: seis. [p=0.2] {b}Menos oito sextos mais três sextos: [p=0.2] {c}menos cinco sextos."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}blocos primeiro, [p=0.2] {b}misto vira fração, [p=0.2] e {c}o sinal do misto vale para ele todo."),
    dict(id="s23", block="fim", text="Na próxima aula, você {a}pratica tudo isso: [p=0.2] {b}cinco situações para pausar e resolver antes de ver a resposta. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
