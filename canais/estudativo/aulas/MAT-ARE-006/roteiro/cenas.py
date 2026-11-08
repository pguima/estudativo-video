# Estudativo · MAT-ARE-006 — Maior área com perímetro fixo (Matemática · Áreas e Perímetros).
# Habilidade: descobrir que, com 40 m de cerca, o retângulo de maior área é o quadrado de 10 m por 10 m, escrevendo A(x) = x(20 − x) e achando o vértice.
# Pré-requisitos: MAT-ARE-002 (base vezes altura). Usa MAT-ARE-001 (perímetro), MAT-FUN-016 a 018 (parábola, raízes, vértice). Próxima: MAT-ARE-007.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Máximo (MAT-FUN-007) fora da cadeia: dito como "ponto mais alto", como em MAT-FUN-018.
# Letras narradas: "xis", "á de xis" (como "efe de xis"), "á" e "bê" da parábola.
# Visual:
#   s01: três retângulos com a mesma volta de 40 m (19 × 1, 15 × 5, 10 × 10) e a área de cada um.
#   s04-s05: E.retangulo com base x e altura 20 − x (E.segmento com cota); A(x) = x(20 − x) = 20x − x².
#   s06-s09: parábola de A(x) = 20x − x² abrindo para baixo, raízes 0 e 20, vértice (10, 100); pontos (5, 75) e (19, 19) marcados.
#   s10: quadrado 20 × 20 em vermelho, com a volta de 80 m.
#   s13-s17: cercado encostado num muro (lado do muro sem cerca, hachurado): lados x, x e 40 − 2x; resposta 10 × 20, área 200.
#   s17: {c} espelho do cercado do outro lado do muro (quadrado 20 × 20 tracejado, volta 80 m); {d} destaca a metade 10 × 20.

TITULO = "Maior área com perímetro fixo"

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
    dict(id="s01", block="gancho", text="{a}Quarenta metros de cerca para fechar um cercado retangular. [p=0.3] {b}Dezenove metros por um dá dezenove metros quadrados de área. [p=0.2] {c}Quinze por cinco dá setenta e cinco. [p=0.3] Mesma cerca, {d}áreas bem diferentes. [p=0.2] Qual é a maior possível?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha o retângulo de maior área para uma cerca dada, [p=0.2] montando uma função e achando o vértice, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}a área do retângulo é base vezes altura; [p=0.2] {c}o perímetro é a soma da volta inteira; [p=0.2] e {d}o xis do vértice da parábola é a média das raízes, ou menos bê dividido por dois á. [p=0.3] Se faltar alguma, procure no canal."),
    # montar a função
    dict(id="s04", block="funcao", text="Quarenta metros de volta inteira são {a}vinte de meia volta. [p=0.2] Então {b}base mais altura dá vinte. [p=0.3] Chame a base de {c}xis. [p=0.2] A altura é {d}o que falta para vinte: vinte menos xis."),
    dict(id="s05", block="funcao", text="A área é base vezes altura: [p=0.2] {a}á de xis igual a xis vezes vinte menos xis, com o vinte menos xis entre parênteses. [p=0.3] É uma função: {b}cada base dá uma área. [p=0.2] Fazendo a distributiva, {c}vinte xis menos xis ao quadrado."),
    # parábola
    dict(id="s06", block="parabola", text="Tem xis ao quadrado, então o gráfico é {a}uma parábola. [p=0.2] O número na frente do xis ao quadrado é {b}menos um: [p=0.2] a parábola {c}abre para baixo. [p=0.3] O vértice é {d}o ponto mais alto: a maior área possível."),
    dict(id="s07", block="parabola", text="As raízes vêm de graça. [p=0.2] Um produto só dá zero quando um fator vale zero: [p=0.2] {a}xis igual a zero, ou xis igual a vinte. [p=0.3] Faz sentido: {b}com base zero ou altura zero, o retângulo fica achatado, sem área nenhuma."),
    dict(id="s08", block="parabola", text="O xis do vértice é {a}a média das raízes: [p=0.2] {b}zero mais vinte dá vinte, dividido por dois dá dez. [p=0.3] Pela fórmula, o mesmo. [p=0.2] Aqui, o á da fórmula não é a área: [p=0.2] {c}é o número na frente do xis ao quadrado, menos um, [p=0.2] e o bê é o número na frente do xis, vinte. [p=0.2] {d}Menos vinte dividido por menos dois dá dez."),
    dict(id="s09", block="parabola", text="Base dez, altura {a}vinte menos dez, que dá dez. [p=0.2] {b}É um quadrado! [p=0.2] Área: {c}dez vezes dez dá cem metros quadrados. [p=0.3] Mais que os setenta e cinco do quinze por cinco, [p=0.2] e {d}nenhum retângulo com essa cerca passa de cem."),
    # erro
    dict(id="s10", block="erro", text="O erro mais comum é {a}usar a volta inteira no lugar da meia volta. [p=0.2] A pessoa escreve {b}xis vezes quarenta menos xis, [p=0.2] acha o vértice em {c}vinte [p=0.2] e responde um quadrado de vinte por vinte. [p=0.3] Mas a volta desse quadrado tem {d}oitenta metros: [p=0.2] o dobro da cerca. [p=0.2] Confira sempre {e}o perímetro da resposta."),
    # atalho
    dict(id="s11", block="atalho", text="Agora o atalho: {a}quando a cerca dá a volta inteira, o maior retângulo é o quadrado. [p=0.3] {b}O lado é o perímetro dividido por quatro: [p=0.2] {c}quarenta dividido por quatro dá dez."),
    dict(id="s12", block="atalho", text="Funciona porque {a}as raízes são sempre zero e a meia volta, [p=0.2] e o vértice fica bem no meio: [p=0.2] {b}base e altura ficam iguais. [p=0.3] {c}Não compensa quando a cerca não dá a volta inteira, [p=0.2] como num cercado encostado num muro. [p=0.2] Aí, {d}monte a função."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] Um cercado retangular fica {a}encostado num muro, [p=0.2] e o muro faz um dos lados. [p=0.2] Os outros três lados usam {b}quarenta metros de cerca. [p=0.3] {c}Quais medidas dão a maior área, e que área é essa?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] Chame de xis {a}cada lado que sai do muro. [p=0.2] Esses lados gastam dois xis de cerca, [p=0.2] e o lado de frente para o muro fica com {b}o que sobra, quarenta menos dois xis. [p=0.3] A área: {c}á de xis igual a xis vezes quarenta menos dois xis."),
    dict(id="s16", block="resposta", text="As raízes: {a}xis igual a zero, [p=0.2] ou quarenta menos dois xis igual a zero, que dá {b}xis igual a vinte. [p=0.2] {c}A média dá dez. [p=0.3] Os lados que saem do muro medem {d}dez metros, [p=0.2] e o da frente, {e}quarenta menos vinte, que dá vinte metros."),
    dict(id="s17", block="resposta", text="Área: {a}dez vezes vinte dá duzentos metros quadrados. [p=0.3] {b}Não é um quadrado! [p=0.2] Por quê? [p=0.2] {c}Espelhe o cercado do outro lado do muro. [p=0.2] Fica um retângulo com a volta inteira de cerca, e a cerca dobra para oitenta metros. [p=0.2] Com a volta inteira, o maior é o quadrado, de vinte por vinte. [p=0.2] O seu cercado é {d}a metade dele, com dez por vinte. [p=0.3] Conferindo a cerca: {e}dez mais dez mais vinte dá quarenta. [p=0.2] Bateu."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}escreva a área em função de um lado [p=0.2] e {b}ache o vértice. [p=0.2] {c}Com a volta inteira de cerca, a resposta é o quadrado."),
    dict(id="s19", block="fim", text="Na próxima aula, é hora de praticar: [p=0.2] {a}escolher a fórmula certa para cada figura, [p=0.2] {b}converter unidades [p=0.2] e calcular {c}o custo de piso, cerca e pintura. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
