# Estudativo · MAT-POL-010 — Eixos de simetria e dobraduras (Matemática · Geometria Plana: Polígonos e Círculo).
# Habilidade: achar os eixos de simetria de uma figura, dizer que o hexágono regular tem 6 e prever o desenho de um papel dobrado, cortado e aberto.
# Pré-requisitos: MAT-POL-003 (polígono regular). Usa também MAT-POL-001 (retângulo, quadrado, paralelogramo). Próxima: MAT-POL-011.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas como se falam: "á".
# Visual: E.poligono / E.regular / E.retangulo / E.circulo com eixos tracejados na cor da matéria; dobra animada (metade girando sobre o eixo).
#   s01: folha dobrada duas vezes, um furo, folha aberta com quatro furos.
#   s05: pontos e seus pares espelhados, ligados por segmentos que cruzam o eixo em ângulo reto.
#   s06-s08: letra A (1 eixo), retângulo (2), quadrado (4), triângulo equilátero (3), círculo (vários eixos pelo centro), hexágono regular (3 + 3 = 6).
#   s09: retângulo dobrado na diagonal, com as pontas sobrando para fora.
#   s12-s14: folha dobrada uma vez (2 camadas), duas vezes (4); corte longe da dobra e corte encostado na dobra (meio coração vira coração).
#   Questão: pentágono regular (5 eixos, de cada vértice ao meio do lado da frente); folha dobrada três vezes, 8 furos.

TITULO = "Eixos de simetria e dobraduras"

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
    dict(id="s01", block="gancho", text="{a}Dobre uma folha ao meio, [p=0.2] e {b}de novo ao meio. [p=0.2] Faça {c}um furo só. [p=0.3] Ao abrir, aparecem {d}quatro furos. [p=0.3] Quem entende por quê {e}acerta questão de dobradura sem desenhar tudo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha os eixos de simetria de uma figura, [p=0.2] {b}prevê o desenho de uma dobradura [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}uma coisa: [p=0.2] {b}polígono regular tem todos os lados iguais e todos os ângulos iguais, [p=0.2] como o quadrado e o hexágono regular. [p=0.3] Se faltar, procure no canal."),
    # eixo
    dict(id="s04", block="eixo", text="{a}Eixo de simetria é uma linha que divide a figura em duas metades espelhadas. [p=0.3] O teste é {b}dobrar na linha: [p=0.2] se uma metade {c}cai exatamente em cima da outra, é eixo."),
    dict(id="s05", block="eixo", text="Pense num {a}espelho em pé sobre a linha. [p=0.2] Cada ponto de um lado tem {b}um par do outro lado, [p=0.2] na mesma distância da linha. [p=0.2] E o caminho entre o ponto e o par {c}cruza a linha em ângulo reto."),
    dict(id="s06", block="exemplos", text="{a}A letra á maiúscula tem um eixo: [p=0.2] a linha em pé, bem no meio. [p=0.3] {b}O retângulo tem dois: [p=0.2] a linha em pé e a deitada, pelo meio dos lados. [p=0.3] {c}O quadrado tem quatro: [p=0.2] essas duas linhas e {d}as diagonais."),
    dict(id="s07", block="exemplos", text="{a}O triângulo equilátero tem três eixos: [p=0.2] cada um sai de um vértice e chega no meio do lado da frente. [p=0.3] E {b}o círculo tem infinitos: [p=0.2] {c}qualquer linha que passa pelo centro é eixo."),
    dict(id="s08", block="exemplos", text="E o {a}hexágono regular? [p=0.2] Há {b}três eixos que ligam vértices opostos, [p=0.2] e {c}três que ligam os pontos médios de lados opostos. [p=0.2] {d}Três mais três dá seis eixos."),
    # erro
    dict(id="s09", block="erro", text="O erro mais comum é {a}achar que a diagonal do retângulo é eixo. [p=0.2] Ela divide o retângulo em {b}triângulos iguais, sim. [p=0.3] Mas dobre na diagonal: [p=0.2] {c}as pontas não se encontram, e sobram pedaços para fora. [p=0.3] {d}Partes iguais não bastam: elas precisam se encaixar na dobra."),
    # atalho
    dict(id="s10", block="atalho", text="Agora o atalho prometido: {a}polígono regular tem tantos eixos quanto lados. [p=0.3] {b}Triângulo equilátero, três. [p=0.2] {c}Quadrado, quatro. [p=0.2] {d}Hexágono regular, seis. [p=0.2] {e}Octógono regular, oito."),
    dict(id="s11", block="atalho", text="Funciona porque, no regular, {a}todo vértice e todo meio de lado ficam na passagem de um eixo, [p=0.2] e tudo é igual dos dois lados da dobra. [p=0.3] No hexágono, {b}seis vértices, de par em par, dão três eixos, [p=0.2] e {c}seis lados, de par em par, dão mais três. [p=0.3] {d}Não vale para polígono que não é regular. [p=0.2] O retângulo tem quatro lados e {e}só dois eixos; [p=0.2] o paralelogramo comum, {f}nenhum."),
    # dobradura
    dict(id="s12", block="dobra", text="Vamos à dobradura. [p=0.2] {a}A dobra funciona como um eixo de simetria. [p=0.3] Quando você corta o papel dobrado, {b}corta todas as camadas juntas. [p=0.2] Ao abrir, {c}o corte aparece espelhado do outro lado da dobra."),
    dict(id="s13", block="dobra", text="Cada dobra {a}dobra o número de camadas. [p=0.2] {b}Uma dobra dá duas camadas. [p=0.2] {c}Duas dobras dão quatro camadas. [p=0.3] Um furo longe das dobras atravessa todas as camadas, [p=0.2] e por isso {d}um furo virou quatro."),
    dict(id="s14", block="dobra", text="E se o corte {a}encostar na dobra? [p=0.2] Aí as cópias {b}se juntam numa figura só, simétrica, [p=0.2] e a dobra vira o eixo dela. [p=0.3] É assim que se recorta um coração: [p=0.2] {c}desenhe metade, com o meio na dobra, [p=0.2] {d}corte e abra."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Quantos eixos de simetria tem um pentágono regular? [p=0.3] E {b}uma folha é dobrada ao meio três vezes. [p=0.2] Você faz {c}um furo longe das dobras. [p=0.2] {d}Quantos furos aparecem ao abrir?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] O pentágono regular tem cinco lados: {a}cinco eixos. [p=0.2] Como cinco é ímpar, {b}cada eixo sai de um vértice e chega no meio do lado da frente, [p=0.2] como no triângulo equilátero."),
    dict(id="s18", block="resposta", text="Na folha, cada dobra dobra as camadas. [p=0.2] {a}A primeira dobra dá duas. [p=0.2] {b}Na segunda, duas vezes duas dá quatro. [p=0.2] {c}Na terceira, quatro vezes duas dá oito. [p=0.3] O furo atravessa as oito camadas e vira {d}oito furos."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}eixo é onde a dobra encaixa as metades, [p=0.2] {b}polígono regular tem tantos eixos quanto lados, [p=0.2] e {c}cada dobra do papel é um espelho."),
    dict(id="s20", block="fim", text="Na próxima aula, a figura sai do lugar: [p=0.2] você vai {a}espelhar, girar e deslizar figuras na malha, [p=0.2] e descobrir para onde vai {b}o ponto xis dois, ípsilon três, refletido no eixo ípsilon. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
