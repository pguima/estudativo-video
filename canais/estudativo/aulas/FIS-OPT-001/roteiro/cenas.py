# Estudativo · FIS-OPT-001 — Luz em linha reta: sombra e câmara escura (Física · Óptica · Reflexão e espelhos).
# Habilidade: explicar sombra, penumbra e eclipses e calcular altura na câmara escura por semelhança.
# Pré-requisitos: MAT-ANG-013 (semelhança: sombras e triângulos encaixados). Próxima: FIS-OPT-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Primeira aula da trilha Óptica: o visual.py guarda a linguagem visual da trilha. Questão inédita, criada para esta aula.
# Divisão com resultado decimal (MAT-FRA-017) não está em "Já ensinado": as contas da câmara fecham em centímetros inteiros.

TITULO = "Luz em linha reta: sombra e câmara escura"

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
    dict(id="s01", block="gancho", text="{a}Uma caixa de sapato com um furinho [p=0.2] mostra {b}uma árvore inteira lá dentro, [p=0.2] {c}de cabeça para baixo. [p=0.3] E com uma conta de proporção, você descobre {d}o tamanho dessa imagem, [p=0.2] e até a altura da árvore, sem subir nela."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai explicar {b}a sombra e a penumbra, [p=0.2] {c}os eclipses [p=0.2] e calcular {d}o tamanho da imagem na câmara escura."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}uma coisa: [p=0.2] {b}semelhança de triângulos. [p=0.2] Triângulos com os mesmos ângulos têm os lados proporcionais. [p=0.3] {c}Um poste de dois metros faz sombra de três metros. [p=0.2] {d}Um prédio, na mesma hora, faz sombra de trinta: [p=0.2] ele tem {e}vinte metros. [p=0.3] Se faltar, procure no canal."),
    # luz em linha reta
    dict(id="s04", block="reta", text="Num meio que é igual em todo lugar, como o ar parado, [p=0.2] {a}a luz anda em linha reta. [p=0.3] É por isso que {b}você não enxerga o que está atrás de uma parede."),
    dict(id="s05", block="reta", text="Na Física, o caminho da luz é desenhado como {a}uma reta com uma seta: [p=0.2] {b}o raio de luz. [p=0.2] A seta mostra para onde a luz vai. [p=0.3] A luz sai de uma fonte. [p=0.2] {c}Uma fonte bem pequena, quase um ponto, é a fonte pontual. [p=0.2] {d}Uma fonte grande, como uma luminária comprida, é a fonte extensa."),
    # sombra e penumbra
    dict(id="s06", block="sombra", text="Coloque {a}uma bola entre uma lâmpada pequena e a parede. [p=0.3] {b}Os raios que passam raspando na bola marcam a borda. [p=0.2] Atrás da bola, nenhum raio chega: [p=0.2] {c}é a sombra. [p=0.2] Com fonte pontual, a borda da sombra é nítida."),
    dict(id="s07", block="sombra", text="Agora troque por {a}uma fonte extensa. [p=0.2] Cada ponto da fonte faz a sua própria sombra, um pouco deslocada. [p=0.3] {b}No meio, não chega luz de ponto nenhum: sombra. [p=0.2] {c}Na borda, chega luz de só uma parte da fonte: [p=0.2] é {d}a penumbra, uma faixa meio escura."),
    # eclipses
    dict(id="s08", block="eclipse", text="O eclipse é uma sombra gigante. [p=0.3] No eclipse do Sol, {a}a Lua fica entre o Sol e a Terra, [p=0.2] e {b}a sombra da Lua cai sobre a Terra. [p=0.3] {c}Quem está na sombra vê o eclipse total. [p=0.2] {d}Quem está na penumbra vê o Sol só em parte coberto."),
    dict(id="s09", block="eclipse", text="No eclipse da Lua, {a}quem fica no meio é a Terra: [p=0.2] {b}a Lua entra na sombra da Terra e escurece. [p=0.3] {c}O astro do meio é sempre o que faz a sombra. [p=0.2] {d}O nome do eclipse é o do astro que some."),
    # câmara escura
    dict(id="s10", block="camara", text="Voltando à caixa do começo. [p=0.2] {a}Câmara escura é uma caixa fechada com um furinho numa das faces. [p=0.3] {b}A luz do topo da árvore passa pelo furo, em linha reta, [p=0.2] e chega {c}embaixo, no fundo da caixa. [p=0.2] {d}A luz do pé da árvore chega em cima. [p=0.3] Por isso, a imagem sai {e}invertida."),
    dict(id="s11", block="camara", text="Os raios se cruzam no furo e formam {a}dois triângulos semelhantes, [p=0.2] um fora e um dentro da caixa. [p=0.3] Então, {b}a altura da imagem dividida pela altura do objeto [p=0.2] é igual à {c}profundidade da caixa dividida pela distância até o objeto."),
    dict(id="s12", block="camara", text="Em letras: {a}i dividido por ó é igual a pê linha dividido por pê. [p=0.3] {b}O i é a altura da imagem, [p=0.1] {c}o ó é a altura do objeto, [p=0.1] {d}o pê linha é a profundidade da caixa [p=0.1] e {e}o pê é a distância da árvore até o furo."),
    dict(id="s13", block="camara", text="Uma árvore de {a}seis metros, [p=0.1] a {b}trinta metros da caixa, [p=0.1] e uma caixa de {c}vinte centímetros. [p=0.3] Passe tudo para centímetro: {d}seis metros são seiscentos centímetros; [p=0.2] trinta metros, três mil. [p=0.3] {e}A imagem dividida por seiscentos é igual a vinte dividido por três mil. [p=0.2] Seiscentos vezes vinte, dividido por três mil: [p=0.2] {f}quatro centímetros."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}misturar as unidades. [p=0.3] A pessoa escreve {b}vinte dividido por trinta, com centímetro em cima e metro embaixo, [p=0.2] e acha que {c}a imagem tem quatro metros. [p=0.3] {d}Uma imagem de quatro metros dentro de uma caixa de sapato? [p=0.2] Não cabe. [p=0.3] {e}Em cada fração, use a mesma unidade em cima e embaixo."),
    # atalho
    dict(id="s15", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}divida a distância pela profundidade. [p=0.3] {b}Três mil dividido por vinte dá cento e cinquenta. [p=0.2] Isso quer dizer que {c}a imagem é cento e cinquenta vezes menor que a árvore. [p=0.3] {d}Seiscentos centímetros dividido por cento e cinquenta: quatro centímetros."),
    dict(id="s16", block="atalho", text="Funciona porque {a}os dois triângulos são semelhantes: [p=0.2] tudo encolhe na mesma razão. [p=0.3] {b}E dá para ver sem conta: [p=0.2] aproxime a caixa da árvore, e a imagem cresce. [p=0.3] {c}Se a divisão não for exata, monte a proporção e resolva como equação."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Uma câmara escura tem {a}quinze centímetros de profundidade [p=0.2] e está a {b}dezoito metros de um poste. [p=0.3] {c}A imagem do poste tem cinco centímetros. [p=0.3] {d}Qual é a altura do poste? [p=0.2] E {e}a imagem é direita ou invertida?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Dezoito metros são mil e oitocentos centímetros. [p=0.2] Pelo atalho, {b}mil e oitocentos dividido por quinze dá cento e vinte: [p=0.2] o poste é cento e vinte vezes maior que a imagem. [p=0.3] {c}Cinco vezes cento e vinte, seiscentos centímetros: [p=0.2] {d}o poste tem seis metros."),
    dict(id="s20", block="resposta", text="E a imagem é {a}invertida, [p=0.2] porque {b}os raios se cruzam no furo: [p=0.2] o que está em cima vai para baixo."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}a luz anda em linha reta; [p=0.2] {b}sombra é onde nenhum raio chega, penumbra é onde chega só uma parte; [p=0.2] e {c}na câmara escura, a imagem é invertida e encolhe na razão da profundidade pela distância."),
    dict(id="s22", block="fim", text="Na próxima aula, a luz {a}bate e volta: [p=0.2] você vai entender {b}a reflexão e o espelho plano, [p=0.2] e por que a sua imagem parece estar atrás do espelho. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
