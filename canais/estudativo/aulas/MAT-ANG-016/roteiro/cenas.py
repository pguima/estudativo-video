# Estudativo · MAT-ANG-016 — Ternos pitagóricos e Pitágoras em problemas (Matemática · Geometria Plana: Ângulos e Triângulos).
# Habilidade: reconhecer 3-4-5 e 5-12-13 e seus múltiplos sem conta e achar a altura que uma escada de 5 m alcança com o pé a 3 m da parede (4 m).
# Pré-requisitos: MAT-ANG-015 (Pitágoras). Usa também MAT-POT-004 (potência de um produto) e MAT-DIV-004 (fator comum). Próxima: MAT-ANG-017.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas como se falam: "á", "bê", "cê".
# Visual:
#   s01: triângulo retângulo com catetos 30 e 40 e a hipotenusa 50 aparecendo sem conta.
#   s05-s06: tabela de ternos: 3-4-5 e 5-12-13; embaixo, os múltiplos 6-8-10, 9-12-15, 30-40-50 e 10-24-26.
#   s07: 6² = 4 · 9, 8² = 4 · 16, 10² = 4 · 25 empilhados.
#   s10-s12: parede vertical, chão, escada de 5 m com o pé a 3 m da parede; quadradinho do reto entre parede e chão.
#   s13-s14: triângulo com catetos 3 e 5 e hipotenusa √34 (entre 5 e 6), em vermelho o "4" riscado.
#   s15: escada de 2,5 m com o pé a 1,5 m: ×2 → 5 e 3 → 4 → ÷2 → 2 m.
#   s17-s20: terreno retangular visto de cima, frente 10 m, diagonal 26 m, lado x.

TITULO = "Ternos pitagóricos e Pitágoras em problemas"

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
    dict(id="s01", block="gancho", text="{a}Catetos de trinta e de quarenta metros. [p=0.2] Sem nenhuma conta, {b}a hipotenusa mede cinquenta. [p=0.3] Não é chute: [p=0.2] é um {c}trio de números que se repete na prova o tempo todo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você reconhece esses trios de olho [p=0.2] e usa Pitágoras em {b}problemas do dia a dia, como uma escada encostada na parede."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}uma coisa só: [p=0.2] {b}o teorema de Pitágoras. [p=0.2] {c}Á ao quadrado igual a bê ao quadrado mais cê ao quadrado, [p=0.2] com o á na hipotenusa, o lado de frente para o ângulo reto. [p=0.3] Se faltar, procure no canal."),
    # ternos
    dict(id="s04", block="ternos", text="Lembra dos catetos {a}três e quatro, com hipotenusa {b}cinco? [p=0.2] Tudo número inteiro. [p=0.3] Três números inteiros que cabem certinho em Pitágoras formam {c}um terno pitagórico. [p=0.2] Terno quer dizer {d}trio."),
    dict(id="s05", block="ternos", text="O mais famoso é {a}três, quatro e cinco: [p=0.2] {b}nove mais dezesseis dá vinte e cinco. [p=0.3] O segundo é {c}cinco, doze e treze: [p=0.2] {d}vinte e cinco mais cento e quarenta e quatro dá cento e sessenta e nove. [p=0.3] Em cada terno, {e}o maior número é a hipotenusa."),
    # múltiplos
    dict(id="s06", block="multiplos", text="E o melhor: {a}multiplique os três números pelo mesmo valor, e continua valendo. [p=0.3] Três, quatro e cinco vezes dois dá {b}seis, oito e dez. [p=0.2] Vezes três dá {c}nove, doze e quinze. [p=0.2] Vezes dez dá {d}trinta, quarenta e cinquenta, o do começo. [p=0.3] Cinco, doze e treze vezes dois vira um triângulo com {e}lados de dez, de vinte e quatro e de vinte e seis."),
    dict(id="s07", block="multiplos", text="Por quê? [p=0.2] Dobrar um lado {a}multiplica o quadrado dele por quatro. [p=0.2] {b}Seis ao quadrado é quatro vezes nove. [p=0.2] {c}Oito ao quadrado é quatro vezes dezesseis. [p=0.2] {d}Dez ao quadrado é quatro vezes vinte e cinco. [p=0.3] A igualdade inteira foi multiplicada por quatro, [p=0.2] então {e}continua valendo."),
    dict(id="s08", block="multiplos", text="Para reconhecer, {a}divida os três pelo mesmo número. [p=0.2] {b}Lados de quinze, de vinte e de vinte e cinco: [p=0.2] tudo dividido por cinco dá {c}três, quatro e cinco. [p=0.3] É terno, e a conta já está feita."),
    # escada
    dict(id="s09", block="escada", text="Nos problemas, o trabalho é {a}achar o triângulo retângulo escondido. [p=0.2] Procure {b}o ângulo reto, [p=0.2] e a hipotenusa é {c}o lado de frente para ele."),
    dict(id="s10", block="escada", text="Uma {a}escada de cinco metros está encostada numa parede. [p=0.2] {b}O pé dela fica a três metros da parede. [p=0.3] {c}Até que altura a escada alcança?"),
    dict(id="s11", block="escada", text="{a}Parede e chão formam o ângulo reto. [p=0.2] {b}A escada fica de frente para ele: é a hipotenusa, cinco. [p=0.2] {c}Um cateto é a distância no chão, três. [p=0.2] Falta {d}o cateto da parede."),
    dict(id="s12", block="escada", text="{a}Três e cinco, com o cinco na hipotenusa: [p=0.2] é o terno {b}três, quatro e cinco. [p=0.2] {c}A escada alcança quatro metros. [p=0.3] Conferindo por Pitágoras: {d}vinte e cinco menos nove dá dezesseis, [p=0.2] e {e}a raiz de dezesseis é quatro."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é {a}ver um três e um cinco e completar sempre com quatro. [p=0.3] Se três e cinco forem {b}os catetos, [p=0.2] a hipotenusa ao quadrado é {c}nove mais vinte e cinco, que dá trinta e quatro."),
    dict(id="s14", block="erro", text="{a}Trinta e quatro não tem raiz exata: [p=0.2] a hipotenusa fica {b}entre cinco e seis. [p=0.3] O terno só vale com {c}o maior número na hipotenusa. [p=0.2] Antes de completar, veja {d}quem está de frente para o ângulo reto."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho, para medidas com vírgula. [p=0.2] Escada de {a}dois vírgula cinco metros, [p=0.2] com o pé a {b}um vírgula cinco metro da parede. [p=0.3] {c}Multiplique as medidas por dois. [p=0.2] Ficam cinco e três. [p=0.2] O terno completa com {d}quatro. [p=0.2] {e}Quatro dividido por dois dá dois: a escada alcança dois metros."),
    dict(id="s16", block="atalho", text="Funciona pelo mesmo motivo dos múltiplos: [p=0.2] {a}multiplicar ou dividir os três lados pelo mesmo número mantém Pitágoras. [p=0.3] {b}Não compensa quando nenhum terno aparece. [p=0.2] Catetos {c}dois e três dão hipotenusa raiz de treze, [p=0.2] e aí {d}a conta é o caminho."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Num terreno retangular, {a}os cantos são ângulos retos. [p=0.2] A linha de um canto ao canto oposto mede {b}vinte e seis metros, [p=0.2] e a frente mede {c}dez metros. [p=0.3] {d}Quanto mede o lado do terreno? [p=0.2] Tente sem fazer quadrados."),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Essa linha corta o terreno em {a}dois triângulos retângulos [p=0.2] e fica {b}de frente para o ângulo reto: é a hipotenusa. [p=0.3] {c}Dividindo dez e vinte e seis por dois, ficam cinco e treze. [p=0.2] É o terno {d}cinco, doze e treze. [p=0.2] {e}Doze vezes dois dá vinte e quatro: o lado mede vinte e quatro metros."),
    dict(id="s20", block="resposta", text="Conferindo por Pitágoras: [p=0.2] {a}vinte e seis ao quadrado dá seiscentos e setenta e seis. [p=0.2] {b}Dez ao quadrado dá cem. [p=0.2] {c}Seiscentos e setenta e seis menos cem dá quinhentos e setenta e seis, [p=0.2] e {d}vinte e quatro ao quadrado também dá quinhentos e setenta e seis. [p=0.2] Bateu."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: decore os ternos {a}três, quatro e cinco, [p=0.2] e {b}cinco, doze e treze, [p=0.2] {c}procure os múltiplos [p=0.2] e {d}confira se o maior está na hipotenusa."),
    dict(id="s22", block="fim", text="Na próxima aula, Pitágoras entra em {a}duas figuras que caem sempre: [p=0.2] {b}a diagonal do quadrado [p=0.2] e {c}a altura do triângulo equilátero. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
