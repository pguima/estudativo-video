# Estudativo · MAT-ARE-011 — Triângulos de mesma altura: a razão das bases (Matemática · Áreas e Perímetros).
# Habilidade: dizer que a mediana divide o triângulo em duas áreas iguais e que, com bases na razão de 2 para 3, as áreas ficam na mesma razão.
# Pré-requisitos: MAT-ARE-003 (b · h / 2). Usa MAT-ANG-008 (mediana, altura) e MAT-RAZ-001/002 (razão). Próxima: MAT-ARE-012.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Razão das áreas de semelhantes (MAT-ARE-010) fora da cadeia desta aula: não é citada.
# Letras narradas como se falam: "á", "bê", "cê", "dê".
# Contas: BC = 10, h = 6 → 30. BD = 4, DC = 6 → 12 e 18 (2 : 3). Mediana 5 e 5 → 15 e 15. Repartir 30 em 2 : 3 → 6 por parte → 12 e 18.
#   Erro: pé da altura a 3 de B → 9 e 21. Questão: 600 m², frente 50 = 20 + 30 → 120 por parte → 240 e 360.
# Visual:
#   s04-s07: E.triangulo ABC com BC = 10 embaixo; ponto D em BC (BD = 4, DC = 6); AD; uma só altura tracejada de A até a reta BC, servindo aos dois.
#   s08: D vira M, ponto médio; os dois pedaços com formatos diferentes, pintados com a mesma área (15 e 15).
#   s09: barra de 30 dividida em 5 partes de 6: 2 partes (12) e 3 partes (18).
#   s10: altura de A caindo a 3 de B: pedaços 9 e 21, em vermelho a ideia de "metade".
#   s11: o vértice deslizando numa reta paralela à base (tracejada), a área fixa num contador.
#   s13-s16: terreno triangular de 600 m², frente 50 m, cerca do canto até a frente (20 m e 30 m).

TITULO = "Triângulos de mesma altura: a razão das bases"

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
    dict(id="s01", block="gancho", text="{a}Uma linha corta um triângulo em dois pedaços. [p=0.2] Um fica {b}fino e inclinado, [p=0.2] o outro, {c}bem mais aberto. [p=0.3] Parecem muito diferentes, [p=0.2] mas têm {d}exatamente a mesma área."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você reparte a área de um triângulo sem medir altura nenhuma, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}a área do triângulo é base vezes altura, dividido por dois, [p=0.2] e {c}a mediana sai de um vértice e vai até o ponto médio do lado da frente. [p=0.3] Se faltar alguma, procure no canal."),
    # mesma altura
    dict(id="s04", block="altura", text="Pegue um triângulo {a}á bê cê. [p=0.2] Marque um ponto {b}dê no lado bê cê [p=0.2] e ligue esse ponto ao vértice {c}á. [p=0.3] Nasceram {d}dois triângulos: á bê dê e á dê cê."),
    dict(id="s05", block="altura", text="As bases deles estão {a}na mesma reta, a do lado bê cê. [p=0.2] E a altura é {b}a mesma linha para os dois: [p=0.2] a que desce do á até essa reta, em ângulo reto. [p=0.3] Mesmo vértice e bases na mesma reta: {c}mesma altura."),
    dict(id="s06", block="exemplo", text="Digamos que {a}bê cê mede dez e a altura mede seis. [p=0.2] O triângulo inteiro tem {b}dez vezes seis, dividido por dois, que dá trinta. [p=0.3] Se {c}bê dê mede quatro e dê cê mede seis, [p=0.2] o triângulo á bê dê tem {d}quatro vezes seis, dividido por dois, que dá doze, [p=0.2] e o á dê cê tem {e}seis vezes seis, dividido por dois, que dá dezoito."),
    dict(id="s07", block="exemplo", text="Repare: as bases estão na razão {a}quatro para seis, ou dois para três. [p=0.2] As áreas, {b}doze para dezoito. [p=0.2] Dividindo por seis, {c}também dois para três. [p=0.3] {d}Com a mesma altura, a razão das áreas é a razão das bases. [p=0.2] A altura e o dividido por dois {e}aparecem nas duas contas e se cancelam."),
    # mediana
    dict(id="s08", block="mediana", text="E se dê for {a}o ponto médio? [p=0.2] Aí, á dê é {b}a mediana, [p=0.2] e as bases ficam {c}cinco e cinco. [p=0.2] Bases iguais, {d}áreas iguais, [p=0.2] e cada uma dá quinze. [p=0.3] {e}A mediana divide o triângulo em duas áreas iguais, [p=0.2] mesmo com formatos diferentes."),
    # repartir
    dict(id="s09", block="repartir", text="Sabendo a área inteira, dá para {a}repartir pela razão. [p=0.2] Bases dois para três: {b}são cinco partes iguais. [p=0.2] {c}Trinta dividido por cinco dá seis por parte. [p=0.2] {d}Duas partes dão doze. [p=0.2] {e}Três partes dão dezoito."),
    # erro
    dict(id="s10", block="erro", text="O erro mais comum é achar que {a}qualquer linha que sai do vértice divide a área ao meio. [p=0.3] Pegue {b}a altura do mesmo triângulo, que cai a três do bê. [p=0.2] Os pedaços ficam com {c}três vezes seis, dividido por dois, que dá nove, [p=0.2] e {d}sete vezes seis, dividido por dois, que dá vinte e um. [p=0.3] {e}Só a mediana corta a base ao meio, e por isso só ela corta a área ao meio."),
    # atalho
    dict(id="s11", block="atalho", text="Agora o atalho: {a}vértice comum e bases na mesma reta, nem procure a altura. [p=0.2] {b}Compare só as bases. [p=0.3] E vale também: {c}mesma base e o vértice andando numa reta paralela a ela, [p=0.2] a altura não muda, {d}e a área também não."),
    dict(id="s12", block="atalho", text="Funciona porque {a}a altura é a distância do vértice até a reta das bases, [p=0.2] e ela não muda. [p=0.3] {b}Não compensa quando falta o vértice comum ou quando as bases não estão na mesma reta: [p=0.2] aí as alturas podem ser diferentes, e {c}cada área se calcula inteira."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] Um terreno triangular tem {a}seiscentos metros quadrados. [p=0.2] Dois irmãos vão dividi-lo com uma cerca reta, {b}de um canto até a frente, [p=0.2] que mede cinquenta metros. [p=0.3] A cerca chega na frente {c}a vinte metros de uma ponta e a trinta metros da outra. [p=0.3] {d}Quantos metros quadrados ficam para cada irmão?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] Os pedaços têm {a}o mesmo vértice e as bases na frente: mesma altura. [p=0.2] Então as áreas seguem as bases: {b}vinte para trinta, ou dois para três."),
    dict(id="s16", block="resposta", text="{a}Dois mais três dá cinco partes. [p=0.2] {b}Seiscentos dividido por cinco dá cento e vinte por parte. [p=0.2] {c}Duas partes dão duzentos e quarenta metros quadrados. [p=0.2] {d}Três partes dão trezentos e sessenta. [p=0.3] Conferindo: {e}duzentos e quarenta mais trezentos e sessenta dá seiscentos. [p=0.2] Bateu."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}com a mesma altura, [p=0.2] {b}a razão das áreas é a razão das bases. [p=0.2] E {c}a mediana corta a área ao meio."),
    dict(id="s18", block="fim", text="Na próxima aula, você pratica tudo do círculo para cá: [p=0.2] {a}regiões sombreadas [p=0.2] e {b}figuras ampliadas, comparando áreas sem calcular tudo de novo. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
