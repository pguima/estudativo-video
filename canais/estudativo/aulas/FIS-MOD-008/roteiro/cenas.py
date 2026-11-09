# Estudativo · FIS-MOD-008 — Vida das estrelas e buracos negros (Física · Física Moderna · Astronomia e cosmologia).
# Habilidade: seguir uma estrela da fusão ao fim, conforme a massa, e explicar o buraco negro pela curvatura do espaço na
# relatividade geral.
# Pré-requisitos: FIS-EGF-003 (F = G·M·m/d²), QUI-ELE-013 (fissão e fusão). Próxima: FIS-MOD-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# "Já ensinado" desta aula não tem relatividade restrita (FIS-MOD-005) nem espectro (FIS-OND-010): a relatividade geral é
# apresentada aqui, pela imagem do lençol esticado; a velocidade da luz é dita como fato (300 mil km/s).
# Fatos (valores aproximados, os de livro): Sol com 4,6 bilhões de anos, vida de ~10 bilhões; até ~8 massas solares → anã
# branca (o Sol); acima → supernova → estrela de nêutrons (~20 km) ou, se o que sobra passa de ~3 massas solares, buraco
# negro. Uma colher de chá de estrela de nêutrons pesa bilhões de toneladas. Fusão nas estrelas vai até o ferro.
# Relatividade geral: Einstein, 1915; desvio da luz confirmado no eclipse de 1919, com observação em Sobral (CE).
# Primeira imagem de um buraco negro: 2019 (M87, Event Horizon Telescope).

TITULO = "Vida das estrelas e buracos negros"

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
    dict(id="s01", block="gancho", text="{a}O ferro do seu sangue foi fabricado dentro de uma estrela, [p=0.2] {b}muito antes de a Terra existir. [p=0.3] {c}E algumas estrelas terminam a vida num lugar de onde {d}nem a luz consegue sair."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai seguir a vida de uma estrela, do nascimento ao fim, [p=0.2] {b}dizer como ela termina pela massa [p=0.2] e {c}explicar o buraco negro."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a gravidade entre dois corpos é proporcional às massas e cai com o quadrado da distância; [p=0.2] e {c}na fusão, núcleos pequenos se juntam e liberam energia. [p=0.3] Se faltar alguma, procure no canal."),
    # nascimento
    dict(id="s04", block="nasce", text="{a}Uma estrela nasce numa nuvem de gás, quase toda de hidrogênio, chamada nebulosa. [p=0.3] {b}A gravidade puxa o gás para o centro, [p=0.1] {c}a nuvem encolhe e esquenta. [p=0.3] {d}Quando o centro passa de dez milhões de graus, [p=0.1] {e}começa a fusão do hidrogênio em hélio. [p=0.2] {f}Nasceu uma estrela."),
    dict(id="s05", block="nasce", text="{a}A vida inteira dela é um cabo de guerra. [p=0.2] {b}A gravidade puxa tudo para dentro. [p=0.2] {c}A energia da fusão empurra para fora. [p=0.3] {d}Enquanto os dois se equilibram, a estrela fica estável. [p=0.3] {e}O Sol está assim há quatro vírgula seis bilhões de anos, [p=0.1] {f}mais ou menos a metade da vida dele."),
    # o fim depende da massa
    dict(id="s06", block="fim_estrela", text="{a}Quando o hidrogênio do centro acaba, [p=0.1] {b}a estrela incha e esfria por fora: [p=0.1] vira uma {c}gigante vermelha. [p=0.3] Daqui para a frente, {d}quem decide o fim é a massa."),
    dict(id="s07", block="fim_estrela", text="{a}Estrela como o Sol, até umas oito vezes a massa dele: [p=0.2] {b}solta as camadas de fora, [p=0.1] e o centro vira {c}uma anã branca, [p=0.1] {d}do tamanho da Terra, que vai esfriando devagar."),
    dict(id="s08", block="fim_estrela", text="{a}Estrela de mais de oito massas solares: [p=0.2] {b}faz fusão até chegar ao ferro, onde a fusão para de dar energia. [p=0.3] {c}O centro desaba, e ela explode numa {d}supernova. [p=0.3] {e}A explosão espalha pelo espaço os elementos que a estrela fabricou. [p=0.2] De explosões de estrelas vem o ferro do seu sangue."),
    dict(id="s09", block="fim_estrela", text="{a}O que sobra no centro pode virar uma estrela de nêutrons: [p=0.2] {b}mais massa que o Sol, numa bola de uns vinte quilômetros. [p=0.2] {c}Uma colher de chá dela pesa bilhões de toneladas. [p=0.3] {d}Se o que sobra tem mais de umas três massas solares, [p=0.2] {e}nada segura o desabamento: [p=0.1] {f}nasce um buraco negro."),
    # buraco negro e relatividade geral
    dict(id="s10", block="buraco", text="Para entender o buraco negro, {a}use a ideia de gravidade que Einstein criou em mil novecentos e quinze. [p=0.3] {b}Pense num lençol esticado. [p=0.2] {c}Ponha uma bola pesada no meio: [p=0.1] o lençol afunda. [p=0.2] {d}Uma bolinha que passa perto faz curva e cai na direção dela."),
    dict(id="s11", block="buraco", text="Na relatividade geral, {a}a massa curva o espaço, como a bola curva o lençol. [p=0.2] {b}E a gravidade é o movimento nessa curva. [p=0.3] {c}Até a luz faz a curva. [p=0.2] {d}Isso foi confirmado num eclipse em mil novecentos e dezenove, [p=0.1] {e}com observações feitas em Sobral, no Ceará."),
    dict(id="s12", block="buraco", text="{a}O buraco negro é uma massa tão concentrada que o lençol vira um poço sem fundo. [p=0.3] {b}Perto dele, existe uma fronteira, o horizonte de eventos. [p=0.2] {c}Quem passa dela não sai mais, [p=0.1] {d}nem a luz, que anda a trezentos mil quilômetros por segundo. [p=0.3] {e}Em dois mil e dezenove, a humanidade viu a primeira imagem de um."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é {a}pensar que o buraco negro é um aspirador que puxa tudo. [p=0.3] {b}Longe dele, a gravidade é a mesma de qualquer corpo de mesma massa. [p=0.2] {c}A força é a constante gê vezes as duas massas, dividido pela distância ao quadrado: [p=0.1] {d}só dependem as massas e a distância. [p=0.3] {e}Se o Sol virasse um buraco negro de mesma massa, [p=0.1] {f}a Terra continuaria na mesma órbita. [p=0.2] {g}Só ficaria escura e gelada."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}a massa decide tudo. [p=0.3] {b}Pouca massa, como o Sol: [p=0.1] gigante vermelha e anã branca. [p=0.2] {c}Muita massa: [p=0.1] supernova e estrela de nêutrons. [p=0.2] {d}Massa enorme: [p=0.1] supernova e buraco negro. [p=0.3] {e}E quanto mais massa, mais curta a vida, [p=0.1] {f}porque a estrela grande queima o combustível muito mais depressa."),
    dict(id="s15", block="atalho", text="{a}Para a gravidade na superfície, use a proporção: [p=0.2] {b}mesma massa e raio dez vezes menor, gravidade cem vezes maior. [p=0.3] {c}É o quadrado da distância, no denominador. [p=0.2] {d}Não compensa se a massa também muda: [p=0.1] aí, faça as duas proporções."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Como termina uma estrela com a massa do Sol? [p=0.3] E {b}se uma estrela encolher até ficar com um raio cem vezes menor, mantendo a massa, [p=0.2] {c}quantas vezes aumenta a gravidade na superfície dela?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Massa do Sol é pouca massa: [p=0.1] {b}ela vira gigante vermelha, [p=0.1] solta as camadas de fora, [p=0.1] {c}e termina como anã branca. [p=0.3] {d}Nada de buraco negro."),
    dict(id="s19", block="resposta", text="{a}A gravidade cai com o quadrado da distância. [p=0.2] {b}Raio cem vezes menor: [p=0.1] {c}cem ao quadrado, [p=0.1] {d}dez mil vezes mais gravidade. [p=0.3] {e}É mais ou menos o que acontece quando uma estrela vira anã branca."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}a estrela vive do equilíbrio entre gravidade e fusão; [p=0.2] {b}a massa decide se ela termina em anã branca, estrela de nêutrons ou buraco negro; [p=0.2] e {c}a massa curva o espaço, e o buraco negro curva tanto que nem a luz sai."),
    dict(id="s21", block="fim", text="Na próxima aula, {a}você vai voltar no tempo até o começo de tudo: [p=0.2] {b}o Big Bang e o Universo que se expande. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
