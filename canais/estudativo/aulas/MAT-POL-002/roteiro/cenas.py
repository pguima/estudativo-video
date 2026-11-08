# Estudativo · MAT-POL-002 — Soma dos ângulos e diagonais de um polígono (Matemática · Geometria Plana: Polígonos e Círculo).
# Habilidade: dividir um polígono em triângulos a partir de um vértice e calcular que o hexágono tem 720° de soma dos ângulos internos e 9 diagonais.
# Pré-requisitos: MAT-POL-001 (quadriláteros, diagonal), MAT-ANG-004 (soma 180° no triângulo). Próxima: MAT-POL-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Soma dos ângulos e diagonais de um polígono"

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
    dict(id="s01", block="gancho", text="{a}Um hexágono tem seis lados. [p=0.2] Quantas diagonais ele tem? [p=0.3] Muita gente faz a conta e responde {b}dezoito. [p=0.3] {c}É o dobro do certo. [p=0.2] E o motivo é que {d}cada diagonal foi contada duas vezes."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha a soma dos ângulos de qualquer polígono, [p=0.2] {b}conta as diagonais sem desenhar [p=0.2] e leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}os ângulos de dentro de um triângulo somam cento e oitenta graus, [p=0.2] e {c}diagonal é o segmento que liga vértices que não são vizinhos. [p=0.3] Se faltar alguma, procure no canal."),
    # polígono
    dict(id="s04", block="poligono", text="{a}Polígono é uma figura fechada feita só de segmentos de reta, os lados. [p=0.2] O nome conta os lados: [p=0.2] {b}três lados, triângulo; [p=0.1] quatro, quadrilátero; [p=0.1] {c}cinco, pentágono; [p=0.1] seis, hexágono; [p=0.1] {d}oito, octógono; [p=0.1] dez, decágono."),
    dict(id="s05", block="poligono", text="Nesta aula, os polígonos são {a}convexos: [p=0.2] {b}sem nenhuma ponta virada para dentro. [p=0.2] São os que mais aparecem em prova."),
    # triângulos
    dict(id="s06", block="triangulos", text="Volte ao hexágono. [p=0.2] {a}Escolha um vértice. [p=0.2] Dele, trace {b}todas as diagonais que der. [p=0.3] O hexágono fica cortado em {c}quatro triângulos."),
    dict(id="s07", block="triangulos", text="Repare que {a}os ângulos dos triângulos encaixam certinho nos ângulos do hexágono. [p=0.2] Nada sobra, nada falta. [p=0.3] Então a soma é {b}quatro vezes cento e oitenta, [p=0.2] que dá {c}setecentos e vinte graus."),
    dict(id="s08", block="triangulos", text="Por que quatro triângulos, e não seis? [p=0.2] {a}Cada lado que não encosta no vértice escolhido ganha um triângulo só dele. [p=0.3] Fica de fora {b}o par de lados que encostam no vértice. [p=0.2] Seis lados, menos esse par: {c}quatro triângulos."),
    # fórmula da soma
    dict(id="s09", block="formula", text="Com qualquer polígono é assim. [p=0.2] Chame de {a}ene o número de lados. [p=0.2] O corte dá {b}ene menos dois triângulos. [p=0.2] Então a soma dos ângulos internos é {c}ene menos dois, vezes cento e oitenta."),
    dict(id="s10", block="formula", text="Quadrilátero: {a}quatro menos dois dá dois triângulos, [p=0.2] e {b}duas vezes cento e oitenta dá trezentos e sessenta graus. [p=0.3] Pentágono: {c}cinco menos dois dá três triângulos, [p=0.2] e {d}três vezes cento e oitenta dá quinhentos e quarenta graus."),
    # diagonais
    dict(id="s11", block="diagonais", text="Agora as diagonais. [p=0.2] Fique no mesmo vértice do hexágono. [p=0.2] Ele {a}não liga diagonal com ele mesmo, [p=0.2] {b}nem com os vizinhos, porque aí seria um lado. [p=0.3] {c}Seis menos três dá três diagonais saindo de cada vértice."),
    dict(id="s12", block="diagonais", text="São {a}seis vértices, cada um com três diagonais: [p=0.2] {b}seis vezes três dá dezoito. [p=0.3] Mas a diagonal que vai de á até dê {c}é a mesma que vai de dê até á. [p=0.2] Cada uma entrou na conta uma vez em cada ponta. [p=0.2] {d}Dezoito dividido por dois dá nove diagonais."),
    dict(id="s13", block="diagonais", text="Em fórmula: {a}ene vezes, abre parênteses, ene menos três, fecha parênteses, dividido por dois. [p=0.2] Ene é o número de vértices, igual ao de lados. [p=0.2] Ene menos três é {b}quantas diagonais saem de cada vértice. [p=0.2] E o dividido por dois {c}desconta a contagem dupla."),
    # erro
    dict(id="s14", block="erro", text="Voltando ao erro do começo. [p=0.2] Quem responde dezoito {a}esqueceu de dividir por dois. [p=0.3] Teste num quadrilátero, que dá para contar no dedo: [p=0.2] de cada vértice, quatro menos três dá uma diagonal, [p=0.2] e {b}quatro vezes um dá quatro. [p=0.2] Mas {c}o quadrilátero só tem duas diagonais. [p=0.2] {d}Quatro dividido por dois dá dois: agora bateu."),
    # atalho
    dict(id="s15", block="atalho", text="E o atalho prometido, para a soma dos ângulos: [p=0.2] {a}cada lado a mais soma cento e oitenta. [p=0.3] {b}Triângulo, cento e oitenta. [p=0.1] {c}Quadrilátero, trezentos e sessenta. [p=0.1] {d}Pentágono, quinhentos e quarenta. [p=0.1] {e}Hexágono, setecentos e vinte."),
    dict(id="s16", block="atalho", text="Funciona porque {a}um lado a mais é um triângulo a mais no corte. [p=0.3] {b}Não compensa com muitos lados, como num polígono de vinte lados. [p=0.2] Aí, use a conta: {c}vinte menos dois dá dezoito, [p=0.2] e {d}dezoito vezes cento e oitenta dá três mil duzentos e quarenta graus."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Um octógono tem {a}oito lados. [p=0.3] {b}Quanto somam os seus ângulos internos? [p=0.2] {c}E quantas diagonais ele tem?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Oito menos dois dá seis triângulos. [p=0.2] {b}Seis vezes cento e oitenta dá mil e oitenta graus. [p=0.3] Conferindo pelo atalho: [p=0.2] {c}o hexágono tem setecentos e vinte; [p=0.2] setecentos e vinte mais cento e oitenta dá novecentos; [p=0.2] novecentos mais cento e oitenta dá mil e oitenta. [p=0.2] Bateu."),
    dict(id="s20", block="resposta", text="Diagonais: {a}de cada vértice saem oito menos três, que dá cinco. [p=0.2] {b}Oito vezes cinco dá quarenta. [p=0.2] {c}Quarenta dividido por dois dá vinte diagonais."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}corte o polígono em triângulos a partir de um vértice. [p=0.2] São {b}ene menos dois triângulos, de cento e oitenta graus cada. [p=0.2] E, {c}nas diagonais, divida por dois."),
    dict(id="s22", block="fim", text="Na próxima aula, os polígonos com {a}todos os lados e todos os ângulos iguais. [p=0.2] Você vai achar {b}cada ângulo do octógono [p=0.2] e descobrir {c}por que hexágonos cobrem um piso sem buracos. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
