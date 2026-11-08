# Estudativo · MAT-ESP-001 — Sólidos, poliedros e relação de Euler (Matemática · Geometria Espacial).
# Habilidade: separar poliedros de corpos redondos, contar faces, arestas e vértices e usar V − A + F = 2 para achar A = 12 num sólido com V = 8 e F = 6.
# Pré-requisitos: MAT-POL-002 (polígono, vértice, contagem dupla das diagonais). Próxima: MAT-ESP-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Letra A narrada "á".
# Define aqui prisma, paralelepípedo (bloco), cubo, pirâmide, cilindro, cone e esfera: as aulas seguintes da trilha usam esses nomes.

TITULO = "Sólidos, poliedros e relação de Euler"

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
    dict(id="s01", block="gancho", text="{a}Um dado tem seis faces e oito pontas. [p=0.3] Quantas dobras ele tem, entre uma face e outra? [p=0.3] Dá para responder {b}sem contar nenhuma. [p=0.2] Basta {c}uma conta com três números, que vale para muitos sólidos."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você separa os sólidos em dois grupos, [p=0.2] conta faces, arestas e vértices [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}polígono é uma figura plana e fechada, feita só de lados retos, com cantos chamados vértices; [p=0.2] e {c}na conta das diagonais, cada uma entrava duas vezes, uma por ponta. [p=0.3] Se faltar alguma, procure no canal."),
    # dois grupos
    dict(id="s04", block="grupos", text="Uma figura plana cabe numa folha de papel. [p=0.2] {a}Um sólido ocupa espaço: [p=0.2] tem comprimento, largura e altura. [p=0.3] Como {b}uma caixa de sapato, [p=0.1] {c}uma lata [p=0.1] ou {d}uma bola."),
    dict(id="s05", block="grupos", text="Os sólidos se dividem em dois grupos. [p=0.2] {a}Poliedro é o sólido feito só de faces planas, e cada face é um polígono. [p=0.2] Como {b}o dado e a caixa de sapato."),
    dict(id="s06", block="grupos", text="{a}Corpo redondo é o sólido que tem alguma parte curva. [p=0.2] Os famosos são três: [p=0.2] {b}o cilindro, como a lata; [p=0.1] {c}o cone, como a casquinha de sorvete; [p=0.1] e {d}a esfera, como a bola. [p=0.3] Um teste rápido: {e}corpo redondo rola na mesa, se você deitar do jeito certo."),
    # prisma e pirâmide
    dict(id="s07", block="tipos", text="Entre os poliedros, dois tipos aparecem muito. [p=0.2] {a}O prisma tem duas bases iguais, uma de frente para a outra, [p=0.2] ligadas por retângulos. [p=0.3] {b}A caixa de sapato é um prisma chamado paralelepípedo, ou bloco. [p=0.2] E {c}o cubo é o bloco com todas as faces quadradas."),
    dict(id="s08", block="tipos", text="{a}A pirâmide tem uma base só, [p=0.2] e as outras faces são triângulos que {b}se encontram num ponto lá em cima. [p=0.3] {c}A base dá o sobrenome: [p=0.2] base quadrada, {d}pirâmide quadrangular; [p=0.1] base triangular, {e}pirâmide triangular."),
    # partes
    dict(id="s09", block="partes", text="Agora, as partes de um poliedro, no {a}cubo. [p=0.2] {b}Face é cada polígono da casca. [p=0.2] {c}Aresta é o encontro de duas faces: a dobra. [p=0.2] {d}Vértice é a ponta, onde as arestas se juntam."),
    dict(id="s10", block="partes", text="No desenho, o cubo aparece {a}em perspectiva, como numa foto. [p=0.2] As arestas que ficam {b}escondidas atrás aparecem tracejadas. [p=0.2] Elas contam do mesmo jeito."),
    dict(id="s11", block="partes", text="Contando no cubo: [p=0.2] {a}quatro vértices em cima e quatro embaixo dá oito. [p=0.2] Arestas: {b}quatro em cima, quatro embaixo e quatro em pé dá doze. [p=0.2] E {c}seis faces."),
    # Euler
    dict(id="s12", block="euler", text="Repare numa conta curiosa: [p=0.2] {a}vértices, menos arestas, mais faces. [p=0.2] No cubo, {b}oito menos doze mais seis dá dois."),
    dict(id="s13", block="euler", text="Na pirâmide quadrangular: [p=0.2] {a}cinco vértices, quatro embaixo e a ponta; [p=0.2] {b}oito arestas, quatro na base e quatro subindo; [p=0.2] {c}cinco faces, a base e quatro triângulos. [p=0.3] {d}Cinco menos oito mais cinco dá dois de novo."),
    dict(id="s14", block="euler", text="Essa é a {a}relação de Euler: [p=0.2] {b}vê menos á mais efe igual a dois. [p=0.2] {c}Vê é o número de vértices, [p=0.1] {d}á, o de arestas, [p=0.1] e {e}efe, o de faces. [p=0.3] Ela vale nos {f}poliedros convexos, sem nenhuma parte afundada, que são os que caem em prova."),
    dict(id="s15", block="euler", text="Ela serve para achar o número que falta. [p=0.2] Um poliedro tem {a}oito vértices e seis faces. [p=0.2] {b}Oito menos á mais seis igual a dois. [p=0.2] {c}Catorze menos á igual a dois. [p=0.2] {d}Á igual a doze arestas, as do dado do começo."),
    # erro
    dict(id="s16", block="erro", text="O erro mais comum é {a}contar as arestas face por face. [p=0.2] O cubo tem seis faces de quatro lados, [p=0.2] e a pessoa faz {b}seis vezes quatro, que dá vinte e quatro arestas. [p=0.3] Mas {c}cada aresta é a dobra entre duas faces: [p=0.2] ela entrou na conta {d}uma vez por face. [p=0.2] Vinte e quatro é {e}o dobro do certo."),
    # atalho
    dict(id="s17", block="atalho", text="E daí sai o atalho: {a}some os lados de todas as faces e divida por dois. [p=0.3] Um poliedro de {b}vinte faces, todas triangulares: [p=0.2] {c}vinte vezes três dá sessenta lados. [p=0.2] {d}Sessenta dividido por dois dá trinta arestas."),
    dict(id="s18", block="atalho", text="Funciona porque {a}cada aresta é lado de exatamente duas faces, [p=0.2] como a diagonal que tinha duas pontas. [p=0.3] {b}Não compensa quando você não sabe a forma das faces: [p=0.2] aí, {c}use Euler. [p=0.3] E o atalho e Euler, juntos, resolvem tudo: [p=0.2] no poliedro de vinte faces, {d}vê menos trinta mais vinte igual a dois. [p=0.2] Então {e}vê vale doze vértices."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Uma caixa de presente é {a}um prisma de base hexagonal: [p=0.2] duas bases de seis lados, ligadas por retângulos. [p=0.3] {b}Quantas faces ela tem? [p=0.2] {c}Quantos vértices? [p=0.2] E, pela relação de Euler, {d}quantas arestas?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] Faces: {a}a base de cima, a de baixo e um retângulo para cada lado do hexágono. [p=0.2] {b}Dois mais seis dá oito faces. [p=0.3] Vértices: {c}seis em cada base, então seis vezes dois dá doze."),
    dict(id="s22", block="resposta", text="Euler: {a}doze menos á mais oito igual a dois. [p=0.2] {b}Vinte menos á igual a dois. [p=0.2] {c}Á igual a dezoito arestas. [p=0.3] Conferindo pelo atalho: [p=0.2] {d}as bases têm doze lados, e os seis retângulos, vinte e quatro. [p=0.2] {e}Trinta e seis dividido por dois dá dezoito. [p=0.2] Bateu."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}poliedro só tem faces planas, e corpo redondo tem parte curva. [p=0.2] E, nos poliedros, {b}vê menos á mais efe dá dois."),
    dict(id="s24", block="fim", text="Na próxima aula, você {a}desmonta esses sólidos e abre no papel: as planificações. [p=0.2] E descobre {b}qual face de um cubo fica de frente para qual, olhando só o molde. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
