# Roteiro — Cartografia, Episódio 1: Escala (modelo "aula para iniciantes")
# Base: Estudos/Enem/estudos/04-geografia/01-cartografia.html — seções 02 e 03 + erro do mapa ampliado (seção 11)
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: escala = o ZOOM do mapa (aproximado = escala grande · afastado = escala pequena)
# Frases-chave (meio e fim, idênticas):
#   1. Escala diz quantas vezes o mundo encolheu para caber no papel.
#   2. Para passar de centímetros para quilômetros, corte cinco zeros.
#   3. Escala grande é zoom aproximado; escala pequena é zoom afastado.

TITULO = "Escala do mapa do zero: o zoom que o ENEM cobra — Cartografia, episódio 1"

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "Imagine um mapa *enorme,* pendurado na parede da escola. [p=0.3] Dois metros de largura. [p=0.5] "
        "{a}Agora imagine outro mapa, pequeno, do tamanho de uma folha, [p=0.2] mostrando só o seu bairro. [p=0.5] "
        "{b}Qual dos dois tem a escala *maior?* [p=0.8] {c}Se você respondeu o da parede... [p=0.4] caiu na pegadinha mais comum dos mapas. "
        "[p=0.5] {d}A escala maior é a do mapa *pequeno.*"),
    dict(id="02", block="promessa", text=
        "Calma, que até o fim desta aula isso vai fazer todo o sentido. [p=0.4] {a}Você vai conseguir ler a escala de qualquer mapa, "
        "[p=0.3] {b}descobrir a distância de verdade a partir do papel, [p=0.3] {c}e saber qual mapa usar em cada situação. "
        "[p=0.4] Sem decorar nada: [p=0.2] só entendendo."),

    # ================= PRÉ-REQUISITOS RELÂMPAGO =================
    dict(id="03", block="fracao", text=
        "Antes, três coisinhas rápidas que a gente vai usar. [p=0.4] {a}Primeira: *fração.* [p=0.3] É um número com uma parte em cima "
        "e outra embaixo, [p=0.2] como um sobre quatro. [p=0.4] {b}O número de baixo se chama *denominador:* [p=0.2] "
        "ele diz em quantos pedaços você cortou a pizza."),
    dict(id="04", block="pizza", text=
        "{a}Segunda: qual fração é maior? [p=0.3] Um sobre quatro é um pedaço de uma pizza cortada em quatro. [p=0.4] "
        "{b}Um sobre doze é um pedaço de uma pizza cortada em doze. [p=0.4] {c}Qual pedaço é maior? [p=0.5] O primeiro, claro. [p=0.4] "
        "{d}Quanto *maior* o número de baixo, [p=0.2] *menor* o pedaço."),
    dict(id="05", block="cmkm", text=
        "{a}Terceira: centímetros e quilômetros. [p=0.3] Cem centímetros fazem um metro. [p=0.4] {b}Mil metros fazem um quilômetro. "
        "[p=0.4] {c}Então um quilômetro tem cem vezes mil: [p=0.3] *cem mil centímetros.* [p=0.4] Guarde esse número: [p=0.2] cem mil."),

    # ================= BLOCO 1: O QUE É ESCALA =================
    dict(id="06", block="planta", text=
        "{t}Agora sim. [p=0.3] Como é que uma cidade inteira cabe numa folha de papel? [p=0.6] {a}Pense na planta de um apartamento, "
        "[p=0.2] aquele desenho do folheto de imóvel. [p=0.4] {b}O quarto de verdade tem três metros. [p=0.4] {c}No desenho, "
        "ele tem três centímetros. [p=0.4] {d}O desenho é o quarto *encolhido,* [p=0.2] na mesma proporção em tudo."),
    dict(id="07", block="planta", text=
        "{t}E quantas vezes ele encolheu? [p=0.4] {a}Três metros são trezentos centímetros. [p=0.3] {b}Trezentos centímetros viraram três. "
        "[p=0.4] {c}Então cada centímetro do desenho vale *cem* centímetros de verdade. [p=0.5] {d}Isso é a *escala:* [p=0.3] "
        "o número que diz quantas vezes o mundo encolheu para caber no papel."),
    dict(id="08", block="numerica", text=
        "{t}E ela aparece escrita assim: [p=0.3] {a}um, dois pontos, cem. [p=0.4] Lê-se: [p=0.2] *um para cem.* [p=0.4] "
        "{b}O um é o mapa. [p=0.3] {c}O cem é o mundo real. [p=0.4] {d}Esse jeito de escrever, com números, [p=0.2] "
        "se chama *escala numérica.*"),

    # ================= BLOCO 2: CENTÍMETROS EM QUILÔMETROS =================
    dict(id="09", block="cemmil", text=
        "{t}E num mapa de cidade? [p=0.3] {a}Lá você vai ver algo como: [p=0.2] um para cem mil. [p=0.4] {b}Um centímetro no mapa "
        "vale cem mil centímetros no chão. [p=0.4] {c}Mas ninguém pensa em cem mil centímetros. [p=0.3] Lembra do número que eu pedi "
        "para guardar? [p=0.4] {d}Cem mil centímetros é *um quilômetro.* [p=0.4] Um centímetro no mapa, [p=0.2] um quilômetro de verdade."),
    dict(id="10", block="atalho", text=
        "{t}E daí sai um atalho. [p=0.3] {a}Para passar de centímetros para quilômetros, [p=0.2] *corte cinco zeros.* [p=0.4] "
        "{b}Por que cinco? [p=0.3] Porque cem mil tem cinco zeros. [p=0.5] {c}Num mapa de um para quinhentos mil, "
        "[p=0.2] corte cinco zeros do quinhentos mil, [p=0.3] {d}e sobra cinco. [p=0.4] "
        "{e}Cada centímetro do mapa vale *cinco quilômetros.*"),

    # ================= BLOCO 3: DISTÂNCIA REAL =================
    dict(id="11", block="conta", text=
        "{t}E como descobrir a distância de verdade entre duas cidades? [p=0.5] {a}Primeiro, você mede no mapa com a régua: "
        "[p=0.2] *oito centímetros.* [p=0.4] {b}O mapa é de um para quinhentos mil, [p=0.2] então cada centímetro vale "
        "cinco quilômetros. [p=0.4] {c}São oito centímetros, [p=0.2] ou seja, oito pedaços de cinco. "
        "[p=0.4] {d}Por isso, a conta é de *vezes:* [p=0.2] oito vezes cinco. [p=0.4] {e}*Quarenta quilômetros.*"),

    # ================= BLOCO 4: ESCALA GRANDE x PEQUENA =================
    dict(id="12", block="zoom", text=
        "{t}Agora, a pergunta do começo. [p=0.3] Para entender, abra o celular na cabeça, no aplicativo de mapas. [p=0.4] "
        "{a}Quando você *aproxima* o zoom, [p=0.2] aparece a sua rua, as casas, os detalhes. [p=0.4] {b}Quando você *afasta* o zoom, "
        "[p=0.2] aparece o país inteiro, e as ruas somem. [p=0.4] {c}A escala é exatamente isso: [p=0.3] *o zoom do mapa.*"),
    dict(id="13", block="grande", text=
        "{t}E qual zoom tem a escala *maior?* [p=0.4] {a}Compare um para cinco mil com um para cinco milhões. [p=0.4] "
        "{b}Escala é uma fração: [p=0.2] um sobre cinco mil, [p=0.2] e um sobre cinco milhões. [p=0.4] {c}Lembra da pizza? "
        "[p=0.3] Número de baixo menor, pedaço maior. [p=0.4] {d}Então um para cinco mil é a escala *maior.*"),
    dict(id="14", block="regra", text=
        "{t}E isso dá a regra que parece invertida. [p=0.4] {a}Número de baixo *pequeno:* [p=0.2] *escala grande.* [p=0.2] "
        "Zoom aproximado: [p=0.2] pouca área, muito detalhe. [p=0.5] {b}Número de baixo *grande:* [p=0.2] *escala pequena.* "
        "[p=0.2] Zoom afastado: [p=0.2] muita área, pouco detalhe."),
    dict(id="15", block="usos", text=
        "{t}Na prática: [p=0.3] {a}a planta de uma casa, um para quinhentos: [p=0.2] escala grande, [p=0.2] você vê cada cômodo. "
        "[p=0.4] {b}O mapa de uma cidade, um para cinquenta mil: [p=0.2] escala média. [p=0.4] {c}O *mapa-múndi,* que é o mapa do "
        "mundo inteiro, [p=0.2] um para cinquenta milhões: [p=0.2] escala pequena."),
    dict(id="16", block="parede", text=
        "{t}E o mapa de dois metros da parede? [p=0.4] {a}Ele mostra o mundo inteiro. [p=0.3] {b}Então cada centímetro dele "
        "vale centenas de quilômetros. [p=0.4] {c}É zoom afastado: [p=0.2] escala *pequena.* [p=0.4] {d}O tamanho do papel não importa. "
        "[p=0.3] O que importa é *quanto do mundo* cabe em cada centímetro."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Vamos parar e juntar o que você já sabe, em três frases. [p=0.5] {a}Um: [p=0.2] escala diz quantas vezes o mundo "
        "encolheu para caber no papel. [p=0.5] {b}Dois: [p=0.2] para passar de centímetros para quilômetros, corte cinco zeros. "
        "[p=0.5] {c}Três: [p=0.2] escala grande é zoom aproximado; [p=0.2] escala pequena é zoom afastado."),

    # ================= BLOCO 5: ESCALA GRÁFICA =================
    dict(id="18", block="grafica", text=
        "{t}Mas e quando o mapa não tem número nenhum? [p=0.5] {a}Olhe no cantinho do aplicativo de mapas: [p=0.2] tem uma barrinha, "
        "[p=0.2] com algo escrito como quinhentos metros. [p=0.4] {b}Isso é a *escala gráfica:* [p=0.2] uma régua desenhada "
        "no próprio mapa. [p=0.4] {c}Você mede a barrinha, [p=0.2] {d}e vê quantas barrinhas cabem entre os dois lugares."),

    # ================= BLOCO 6: MAPA AMPLIADO =================
    dict(id="19", block="ampliado", text=
        "{t}E se você ampliar um mapa no xerox, para o dobro do tamanho? [p=0.5] {a}O desenho dobra. [p=0.3] {b}E a barrinha "
        "da escala gráfica dobra junto. [p=0.3] Ela continua *certa.* [p=0.4] {c}Mas o número impresso, um para um milhão, "
        "[p=0.2] continua lá, igualzinho. [p=0.4] {d}E agora ele está *errado.*"),
    dict(id="20", block="ampliado", text=
        "{t}Por quê? [p=0.3] {a}Antes, um centímetro do mapa valia dez quilômetros. [p=0.4] {b}Depois de ampliar, "
        "esses mesmos dez quilômetros ocupam *dois* centímetros. [p=0.4] {c}Então cada centímetro passa a valer cinco quilômetros. "
        "[p=0.4] {d}A escala certa virou um para *quinhentos mil.* [p=0.4] {e}Por isso os mapas do celular usam a barrinha: "
        "[p=0.2] ela acompanha o zoom."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erro1", text=
        "{t}Agora, os três erros que mais derrubam gente. [p=0.4] {a}Primeiro: [p=0.2] achar que um para cinco milhões é escala grande. "
        "[p=0.4] {b}Parece certo, porque cinco milhões é um número enorme. [p=0.4] {c}Mas ele é o número de *baixo* da fração: "
        "[p=0.2] quanto maior, menor o pedaço. [p=0.4] {d}Escala *pequena,* zoom afastado."),
    dict(id="22", block="erro2", text=
        "{a}Segundo erro: [p=0.2] esquecer de converter. [p=0.4] {b}Oito vezes quinhentos mil dá quatro milhões. [p=0.3] "
        "Parece a resposta, porque a conta está certa. [p=0.4] {c}Mas são quatro milhões de *centímetros.* [p=0.4] "
        "{d}Corte cinco zeros: [p=0.2] *quarenta quilômetros.*"),
    dict(id="23", block="erro3", text=
        "{a}Terceiro erro: [p=0.2] confiar no número de um mapa ampliado. [p=0.4] {b}Parece certo, porque o número está impresso ali. "
        "[p=0.4] {c}Mas ele foi escrito para o tamanho *original.* [p=0.4] {d}No mapa ampliado, confie na *barrinha.*"),

    # ================= QUESTÃO ESTILO ENEM =================
    dict(id="24", block="questao", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.4] {e1}A prefeitura vai instalar *bocas de lobo,* [p=0.2] aqueles bueiros "
        "da beira da calçada, [p=0.2] rua por rua, num bairro que alaga. [p=0.4] {e2}Ela tem dois mapas do mesmo tamanho: "
        "[p=0.2] um de um para dois mil, [p=0.2] e outro de um para dois milhões. [p=0.4] {e3}Qual é o mais adequado?"),
    dict(id="25", block="questao", text=
        "{t}As alternativas: [p=0.3] {a}A: [p=0.2] um para dois milhões, por ser escala maior e mais detalhada. [p=0.4] "
        "{b}B: [p=0.2] um para dois milhões, porque mostra mais área com o mesmo detalhe. [p=0.4] {c}C: [p=0.2] um para dois mil, "
        "por ser escala pequena. [p=0.4] {d}D: [p=0.2] um para dois mil, por ser escala maior, com mais detalhe. [p=0.4] "
        "{e}E: [p=0.2] tanto faz, a escala não muda o detalhe. [p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="26", block="questao", text=
        "{t}Vamos eliminar. [p=0.3] {a}A diz que um para dois milhões é escala maior. [p=0.3] É o erro clássico do número de baixo grande. "
        "[p=0.2] Fora. [p=0.4] {b}B diz que mostra mais área com o mesmo detalhe. [p=0.3] Mas, no mesmo papel, mais área significa "
        "*menos* detalhe. [p=0.2] Fora. [p=0.4] {e}E diz que tanto faz. [p=0.2] Pelo mesmo motivo: [p=0.2] fora."),
    dict(id="27", block="questao", text=
        "{c}Sobram C e D, [p=0.2] e as duas escolhem o mapa certo: [p=0.2] um para dois mil. [p=0.4] Mas a C chama esse mapa "
        "de escala *pequena.* [p=0.3] E número de baixo pequeno é escala *grande.* [p=0.2] Fora. [p=0.4] {d}Resposta: [p=0.2] *letra D.* "
        "[p=0.4] {x}Em um para dois mil, um centímetro vale vinte metros: [p=0.2] cada rua aparece."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] escala diz quantas vezes o mundo encolheu para caber no papel. "
        "[p=0.5] {b}Dois: [p=0.2] para passar de centímetros para quilômetros, corte cinco zeros. [p=0.5] {c}Três: [p=0.2] "
        "escala grande é zoom aproximado; [p=0.2] escala pequena é zoom afastado."),

    # ================= PONTE =================
    dict(id="29", block="ponte", text=
        "{t}No próximo episódio: [p=0.3] {a}como achar *qualquer* ponto da Terra usando só dois números. [p=0.4] "
        "{b}As *coordenadas geográficas.* [p=0.4] E você vai ver que elas são bem mais fáceis do que parecem."),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para não perder os próximos episódios. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você também achava que o mapa da parede tinha escala grande? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
