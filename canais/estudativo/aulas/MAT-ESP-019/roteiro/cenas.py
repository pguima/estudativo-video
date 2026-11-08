# Estudativo · MAT-ESP-019 — Sólidos inscritos e circunscritos (Matemática · Geometria Espacial · Sólidos compostos e razão entre volumes).
# Habilidade: ligar as medidas de uma esfera dentro de um cubo de aresta 6 (raio 3) e de um cone dentro de um cilindro e achar o volume que sobra.
# Pré-requisitos: MAT-ESP-006 (cubo, diagonal = aresta · √3), MAT-ESP-017 (o que sobra = de fora − de dentro).
#   Usa MAT-ESP-008 (cilindro), MAT-ESP-013 (cone = 1/3 do cilindro), MAT-ESP-014 (esfera 4πr³/3; com π = 3, 4r³). Próxima: MAT-ESP-020.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Pi narrado "pi"; letra r narrada "érre".
# Questão inédita, criada para esta aula. π = 3 em todas as contas (como em MAT-ESP-008).
# Contas: cubo 6³ = 216; esfera r = 3 (π = 3 → 4r³): 4 · 27 = 108; sobra 108 (metade). Com π real, esfera ≈ 113,1 (pouco mais da metade).
#   Erro: raio 6 → 4 · 216 = 864 = 4 · 216. Cilindro r = 2, h = 6: 3 · 4 = 12, · 6 = 72; cone 24; sobra 48 = 2/3 de 72.
#   Atalho: 4 · (a/2)³ = 4 · a³/8 = a³/2. Questão: r = 3, h = 10: 3 · 9 = 27, · 10 = 270; cone 90; sobra 180 = 2/3 de 270.
# Visual:
#   s01, s04-s08: E.cubo aresta 6 com E.esfera dentro (transparente); s05 corte de frente: quadrado com círculo, diâmetro = aresta marcado.
#   s09: E.esfera por fora do cubo, tocando os oito cantos; diagonal do cubo tracejada = diâmetro.
#   s10-s12: E.cilindro raio 2, altura 6 com E.cone dentro (base no fundo, ponta no centro da tampa); sobra hachurada.
#   s14-s15: palco escuro: "cone no cilindro → sobra 2/3", "bola no cubo (π = 3) → sobra 1/2".
#   s07 e s13 na tela: "4 · 27 = 108" e "4 · 216 = 864" (sem 4/3).
#   s16-s19: E.cilindro raio 3, altura 10 com o cone dentro.

TITULO = "Sólidos inscritos e circunscritos"

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
    dict(id="s01", block="gancho", text="{a}Uma bola encaixada numa caixa cúbica de seis centímetros, [p=0.2] encostando em todas as paredes. [p=0.3] Quanto da caixa fica {b}vazio? [p=0.3] Com pi igual a três, {c}metade da caixa."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você liga as medidas de um sólido dentro do outro, [p=0.2] calcula {b}o que sobra [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}quatro coisas: [p=0.2] {b}o volume do cubo é a aresta ao cubo; [p=0.2] {c}o da esfera é quatro pi érre ao cubo, dividido por três, [p=0.2] que, com pi igual a três, vira quatro érre ao cubo; [p=0.2] {d}o cilindro é a área do fundo vezes a altura, e o cone de mesma base e mesma altura tem um terço disso; [p=0.2] e {e}o que sobra é o de fora menos o de dentro, como no cubo de metal com furo. [p=0.3] Se faltar alguma, procure no canal."),
    # inscrito e circunscrito
    dict(id="s04", block="conceito", text="{a}Inscrito quer dizer por dentro, encostando o máximo possível. [p=0.2] A bola {b}inscrita no cubo toca as seis faces, bem no meio de cada uma. [p=0.3] E o cubo, por fora, é {c}circunscrito à bola. [p=0.3] Na prova, {d}o maior que cabe é o inscrito, [p=0.2] e {e}a menor caixa que guarda é a circunscrita."),
    dict(id="s05", block="esfera", text="O segredo é {a}uma frase antes de qualquer conta: [p=0.2] qual medida de um é igual a qual medida do outro. [p=0.3] Olhe a bola de frente, {b}cortada ao meio. [p=0.2] Ela vai de uma parede até a parede do lado oposto. [p=0.2] Então {c}o diâmetro da bola é igual à aresta do cubo."),
    dict(id="s06", block="esfera", text="Aresta seis, {a}diâmetro seis, [p=0.2] e {b}raio três, a metade."),
    dict(id="s07", block="esfera", text="Hora das contas. [p=0.2] {a}Cubo: seis vezes seis vezes seis dá duzentos e dezesseis centímetros cúbicos. [p=0.3] {b}Bola, com pi igual a três: quatro érre ao cubo. [p=0.2] {c}Três ao cubo dá vinte e sete. [p=0.2] {d}Quatro vezes vinte e sete dá cento e oito centímetros cúbicos."),
    dict(id="s08", block="esfera", text="{a}O que sobra é o de fora menos o de dentro: [p=0.2] {b}duzentos e dezesseis menos cento e oito dá cento e oito centímetros cúbicos. [p=0.3] {c}Metade da caixa fica vazia. [p=0.2] Com o pi de verdade, a bola ocupa {d}um pouco mais que a metade."),
    dict(id="s09", block="circunscrita", text="E se for {a}a bola por fora, encostando nos oito cantos do cubo? [p=0.2] Aí a medida que bate é outra: [p=0.2] {b}o diâmetro da bola é a diagonal do cubo, [p=0.2] que você já sabe calcular: {c}aresta vezes raiz de três."),
    # cone no cilindro
    dict(id="s10", block="cone", text="Agora, {a}um cone dentro de um cilindro. [p=0.2] O cone usa {b}o fundo do cilindro como base [p=0.2] e encosta a ponta {c}no centro da tampa. [p=0.3] A frase aqui é: {d}mesmo raio e mesma altura."),
    dict(id="s11", block="cone", text="Cilindro de {a}raio dois centímetros e altura seis, com pi igual a três. [p=0.2] {b}Fundo: dois ao quadrado dá quatro, e três vezes quatro dá doze. [p=0.2] {c}Doze vezes seis dá setenta e dois: o cilindro. [p=0.3] O cone é um terço disso: {d}setenta e dois dividido por três dá vinte e quatro."),
    dict(id="s12", block="cone", text="Sobra {a}setenta e dois menos vinte e quatro, que dá quarenta e oito centímetros cúbicos. [p=0.3] Repare: {b}quarenta e oito é dois terços de setenta e dois."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é {a}usar a aresta como raio. [p=0.2] Com raio seis, a bola daria {b}quatro vezes seis ao cubo: [p=0.2] quatro vezes duzentos e dezesseis, que dá {c}oitocentos e sessenta e quatro. [p=0.3] {d}Quatro vezes a caixa inteira! [p=0.2] Uma bola maior que a caixa onde ela cabe. [p=0.2] {e}A aresta é o diâmetro: divida por dois."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}decore a fração que sobra. [p=0.3] {b}Cone no cilindro de mesma base e mesma altura: sobram dois terços. [p=0.2] {c}Bola no cubo, com pi igual a três: sobra metade. [p=0.2] Calcule só o de fora, e {d}tire a fração."),
    dict(id="s15", block="atalho", text="Funciona porque {a}o cone é sempre um terço do cilindro. [p=0.2] E na bola, {b}o raio é metade da aresta: [p=0.2] com pi igual a três, ela é quatro érre ao cubo, [p=0.2] e {c}a metade, ao cubo, dá um oitavo. [p=0.2] {d}Quatro oitavos é metade. [p=0.3] {e}Não compensa quando o cone é mais baixo que o cilindro, [p=0.2] ou quando a prova manda usar pi igual a três vírgula catorze. [p=0.2] Aí, {f}faça as duas contas."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Uma peça de madeira tem forma de {a}cilindro, com raio de três centímetros e altura de dez. [p=0.3] Um torneiro tira dela {b}o maior cone com a mesma base e a mesma altura. [p=0.2] {c}Use pi igual a três. [p=0.3] {d}Quantos centímetros cúbicos de madeira viram serragem?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] A frase: {a}mesmo raio e mesma altura. [p=0.2] Fundo: {b}três ao quadrado dá nove, e três vezes nove dá vinte e sete. [p=0.2] Cilindro: {c}vinte e sete vezes dez dá duzentos e setenta centímetros cúbicos."),
    dict(id="s19", block="resposta", text="O cone é um terço: {a}duzentos e setenta dividido por três dá noventa. [p=0.2] Serragem: {b}duzentos e setenta menos noventa dá cento e oitenta centímetros cúbicos. [p=0.3] Pelo atalho, {c}dois terços de duzentos e setenta: [p=0.2] dividido por três dá noventa, {d}vezes dois dá cento e oitenta. [p=0.2] Bateu."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}primeiro, a frase que diz qual medida é igual a qual. [p=0.2] {b}Depois, o de fora menos o de dentro."),
    dict(id="s21", block="fim", text="Na próxima aula, {a}sólidos de mesma forma e tamanhos diferentes. [p=0.2] Você vai ver por que {b}dobrar todas as medidas multiplica o volume por oito, [p=0.2] e por que {c}a ponta de um cone cortado na metade da altura tem só um oitavo do volume. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
