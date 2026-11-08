# Estudativo · MAT-TOP-019 — Combinação com repetição (Matemática · Tópicos Avançados · Binômio, distribuição binomial e casa dos pombos).
# Habilidade: contar de quantos jeitos escolher 3 doces entre 4 sabores, podendo repetir, e achar as soluções inteiras não negativas de x + y + z = 10.
# Pré-requisitos: MAT-CNT-009 (combinações em problemas de escolha). Usa MAT-CNT-008 (combinação = arranjo ÷ fatorial dos escolhidos;
#   escolher quem entra = escolher quem fica de fora) e MAT-CNT-001 (princípio multiplicativo). Próxima: MAT-TOP-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; "!" narrado como "fatorial"; letras "ene", "pê", "zê".
# Questão inédita, criada para esta aula. Método das bolinhas e barras contado como combinação (escolher os lugares), sem permutação
#   com repetição, que não está na ficha.
# Contas: 4 sabores, 3 doces: 6 lugares, C(6, 3) = 6 · 5 · 4 / 3! = 120 / 6 = 20. Erros: C(4, 3) = 4; 4³ = 64.
#   x + y + z = 10: 12 lugares, C(12, 2) = 12 · 11 / 2 = 66. Positivos: sobram 7, C(9, 2) = 9 · 8 / 2 = 36.
#   Questão: 5 sabores, 2 bolas: C(6, 2) = 15 = 5 + C(5, 2); x + y + z = 6: C(8, 2) = 28.

TITULO = "Combinação com repetição: bolinhas e barras"

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
    dict(id="s01", block="gancho", text="Uma doceria tem {a}quatro sabores de brigadeiro. [p=0.2] Você vai levar {b}três doces, e pode repetir o sabor. [p=0.3] Quantas escolhas diferentes existem? [p=0.2] Não é {c}quatro, [p=0.2] nem {d}sessenta e quatro. [p=0.2] São {e}vinte."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você conta escolhas em que pode repetir, [p=0.2] resolve equações como xis mais ípsilon mais zê igual a dez [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}na combinação, a ordem não importa: faça o arranjo e divida pelo fatorial de quantos foram escolhidos; [p=0.2] e {c}escolher quem entra é o mesmo que escolher quem fica de fora. [p=0.3] Se faltar alguma, procure no canal."),
    # por que não é quatro
    dict(id="s04", block="problema", text="Por que não é quatro? [p=0.2] Quatro é {a}a combinação de quatro sabores, três a três: [p=0.2] só escolhas com {b}três sabores diferentes. [p=0.3] Mas aqui pode repetir: [p=0.2] {c}três de chocolate vale, [p=0.2] e {d}dois de coco com um de limão também."),
    # bolinhas e barras
    dict(id="s05", block="bolinhas", text="O truque é escrever cada escolha {a}com bolinhas e barras. [p=0.2] {b}Cada bolinha é um doce. [p=0.2] {c}As barras separam os sabores: [p=0.2] com quatro sabores, são {d}três barras, que fazem quatro espaços."),
    dict(id="s06", block="bolinhas", text="{a}Duas bolinhas, barra, uma bolinha, barra, barra: [p=0.2] dois de chocolate, um de morango, nenhum de coco, nenhum de limão. [p=0.3] {b}Barra, barra, barra, três bolinhas: [p=0.2] três de limão."),
    dict(id="s07", block="bolinhas", text="Toda escolha vira {a}uma fila de seis símbolos: três bolinhas e três barras. [p=0.2] E toda fila assim vira uma escolha. [p=0.3] Então, basta contar as filas: [p=0.2] {b}escolher, entre seis lugares, os três das bolinhas."),
    dict(id="s08", block="bolinhas", text="A ordem dos lugares escolhidos não importa: é uma combinação. [p=0.2] {a}Seis vezes cinco vezes quatro, cento e vinte, [p=0.2] {b}dividido por três fatorial, que é seis: [p=0.2] {c}vinte escolhas."),
    # regra e equação
    dict(id="s09", block="regra", text="A regra: com {a}ene tipos e pê objetos, [p=0.2] são {b}pê bolinhas e ene menos uma barras. [p=0.3] {c}Escolha os lugares das bolinhas entre todos os lugares: pê mais ene menos um."),
    dict(id="s10", block="regra", text="Agora, a equação {a}xis mais ípsilon mais zê igual a dez, [p=0.2] com {b}números inteiros, sem negativos: zero, um, dois, e assim por diante. [p=0.3] É distribuir {c}dez bolinhas em três caixas, a do xis, a do ípsilon e a do zê. [p=0.2] São {d}dez bolinhas e duas barras: doze lugares."),
    dict(id="s11", block="regra", text="Escolher os lugares das dez bolinhas é o mesmo que escolher {a}os lugares das duas barras. [p=0.2] {b}Doze vezes onze, cento e trinta e dois, dividido por dois fatorial: [p=0.2] {c}sessenta e seis soluções."),
    # erro
    dict(id="s12", block="erro", text="Agora, cuidado com o erro mais comum: [p=0.2] {a}usar o princípio multiplicativo: quatro vezes quatro vezes quatro, sessenta e quatro. [p=0.3] Essa conta trata {b}chocolate e depois coco, e coco e depois chocolate, [p=0.2] como escolhas diferentes. [p=0.3] Na sacola, a ordem {c}não importa: é a mesma escolha."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, para quando cada um precisa receber {a}pelo menos um: [p=0.2] {b}dê um para cada antes de contar. [p=0.3] Em xis mais ípsilon mais zê igual a dez, com cada letra valendo pelo menos um: [p=0.2] {c}dê um a cada letra, e sobram sete. [p=0.2] {d}Sete bolinhas e duas barras: nove lugares. [p=0.2] {e}Nove vezes oito, dividido por dois: trinta e seis."),
    dict(id="s14", block="atalho", text="Funciona porque, depois de garantir um para cada, {a}o que sobra pode ser distribuído livremente, até com zero. [p=0.3] {b}Não compensa quando o zero é permitido: [p=0.2] aí, conte direto."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma sorveteria tem {a}cinco sabores, e a casquinha leva {b}duas bolas, podendo repetir o sabor. [p=0.2] Quantas casquinhas diferentes existem? [p=0.3] E {c}quantas soluções inteiras, sem negativos, tem xis mais ípsilon mais zê igual a seis?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Duas bolinhas e quatro barras: seis lugares. [p=0.2] {b}Escolha os lugares das duas bolinhas: seis vezes cinco, dividido por dois, quinze. [p=0.3] Confira: {c}cinco casquinhas de um sabor só, [p=0.2] mais {d}dez com dois sabores diferentes: quinze."),
    dict(id="s18", block="resposta", text="Na equação, {a}seis bolinhas e duas barras: oito lugares. [p=0.2] {b}Oito vezes sete, dividido por dois: vinte e oito soluções."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}pode repetir e a ordem não importa? Bolinhas e barras. [p=0.2] {b}Com ene tipos, são ene menos uma barras, [p=0.2] e {c}a resposta é escolher os lugares das bolinhas, ou das barras."),
    dict(id="s20", block="fim", text="Na próxima aula, você pratica o módulo inteiro: [p=0.2] {a}binômio de Newton, a chance de um número exato de acertos, [p=0.2] {b}casa dos pombos, inclusão e exclusão, e as bolinhas e barras. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
