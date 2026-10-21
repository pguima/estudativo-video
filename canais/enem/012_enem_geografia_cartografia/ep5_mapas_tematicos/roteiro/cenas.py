# Roteiro — Cartografia, Episódio 5: Mapas temáticos, anamorfoses e como ler qualquer mapa (aula para iniciantes)
# Base: Estudos/Enem/estudos/04-geografia/01-cartografia.html — seção 09 + Questão 6 da seção 12
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: a anamorfose é um MAPA DE BALÕES: cada país enche ou murcha conforme o dado,
#   mas continua no mesmo lugar.
# Frases-chave (meio e fim, idênticas):
#   1. A resposta costuma estar na legenda.
#   2. Anamorfose: o tamanho é um dado, não o território.
#   3. Projeção mantém a realidade; anamorfose distorce de propósito.

TITULO = "Anamorfose e mapas temáticos do zero: leia qualquer mapa do ENEM — Cartografia, episódio 5"

PRONUNCIA = {
    "ENEM": "Enem",
    "PIB": "P I B",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "E se o tamanho de cada país no mapa [p=0.2] fosse o número de *pessoas* que vivem nele? [p=0.5] {a}O Canadá quase sumiria. "
        "[p=0.4] {b}E a Índia ficaria *gigante.* [p=0.5] {c}Esse mapa existe. [p=0.3] E cai no ENEM."),
    dict(id="02", block="promessa", text=
        "Até o fim desta aula, [p=0.2] {a}você vai saber ler qualquer mapa da prova em *quatro passos,* [p=0.3] "
        "{b}e nunca mais vai confundir anamorfose com projeção."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "Antes, duas lembranças rápidas. [p=0.3] {a}Do episódio três: [p=0.2] uma projeção *equivalente* [p=0.2] é a que mantém as "
        "*áreas reais* dos países. [p=0.4] {b}E do episódio um: [p=0.2] a *escala* diz quanto o mundo encolheu para caber no papel."),

    # ================= BLOCO A: MAPA TEMÁTICO =================
    dict(id="04", block="previsao", text=
        "{t}Sabe o mapa da previsão do tempo, [p=0.2] pintado de azul onde vai chover? [p=0.4] {a}Ou o mapa da eleição, "
        "[p=0.2] com cada estado de uma cor? [p=0.4] {b}Ou o mapa de trânsito do celular, [p=0.2] com as ruas vermelhas onde está parado? "
        "[p=0.4] {c}Os três têm uma coisa em comum."),
    dict(id="05", block="tematico", text=
        "{t}Eles pegam um mapa comum, [p=0.2] o desenho do território, [p=0.3] {a}e pintam por cima um *assunto:* [p=0.2] chuva, voto, trânsito. "
        "[p=0.4] {b}Esse mapa de fundo se chama *base cartográfica.* [p=0.4] {c}E o mapa com o assunto por cima [p=0.2] se chama *mapa temático.* "
        "[p=0.4] {d}Pode ser clima, população, desmatamento: [p=0.2] qualquer tema."),

    dict(id="05b", block="tematico", text=
        "{e}E repare: [p=0.2] nos três mapas do começo, [p=0.2] o desenho do território é o *mesmo.* [p=0.4] {f}O que muda é o assunto pintado por cima. "
        "[p=0.4] É por isso que, numa questão, [p=0.2] a primeira pergunta é: [p=0.2] *qual é o tema deste mapa?*"),

    # ================= BLOCO B: A LEGENDA =================
    dict(id="06", block="legenda", text=
        "{t}Mas como saber o que cada cor quer dizer? [p=0.4] {a}Pela *legenda:* [p=0.2] aquele quadrinho no canto que explica cada cor e cada símbolo. "
        "[p=0.4] {b}A legenda é *parte* do mapa. [p=0.3] Sem ela, as cores não dizem nada."),
    dict(id="07", block="tipos", text=
        "{t}E existem três jeitos principais de pintar um tema. [p=0.4] {a}Primeiro: [p=0.2] a *gradação.* [p=0.3] É a cor indo do clarinho "
        "ao escuro: [p=0.2] quanto mais escuro, *mais* daquilo. [p=0.3] Serve para quantidades, como a chuva."),
    dict(id="08", block="tipos", text=
        "{b}Segundo: [p=0.2] *cores diferentes* para coisas que não têm ordem. [p=0.3] Como os tipos de clima: [p=0.2] um não é \"mais\" que o outro. "
        "[p=0.4] {c}Terceiro: [p=0.2] *símbolos proporcionais:* [p=0.2] bolinhas que crescem com o tamanho do número, [p=0.2] "
        "como a população de cada cidade."),

    # ================= BLOCO C: ANAMORFOSE =================
    dict(id="09", block="balao", text=
        "{t}Agora, o mapa do começo. [p=0.3] {a}Imagine que cada país é um *balão,* [p=0.2] preso no seu lugar. [p=0.4] "
        "{b}Você enche cada balão conforme um número: [p=0.2] por exemplo, quantas pessoas moram lá. [p=0.4] {c}Os países com muita gente *incham.* "
        "[p=0.3] {d}Os com pouca gente *murcham.*"),
    dict(id="10", block="morph", text=
        "{t}Veja o mapa-múndi virando um mapa de população. [p=0.6] {a}A Índia e a China *incham:* [p=0.2] são os países mais populosos. "
        "[p=0.5] {b}O Canadá, a Rússia e a Austrália *murcham:* [p=0.2] são enormes em território, [p=0.2] mas têm pouca gente para tanto espaço."),
    dict(id="11", block="morph", text=
        "{c}Esse mapa se chama *anamorfose,* [p=0.2] ou *cartograma.* [p=0.4] {d}O tamanho de cada país passa a representar um *dado.* "
        "[p=0.4] {e}A posição continua a mesma: [p=0.2] a Índia continua ao lado da China. [p=0.4] {f}Só as formas se deformam, [p=0.2] *de propósito.*"),
    dict(id="11b", block="morph", text=
        "{g}E o Brasil? [p=0.3] Ele tem muita gente: [p=0.2] mais de duzentos milhões de pessoas. [p=0.4] {h}Mas tem tanto território "
        "[p=0.2] que, no mapa de população, [p=0.2] ele até *encolhe* um pouco. [p=0.4] {i}O balão do Brasil enche menos do que o tamanho dele no mapa comum."),
    dict(id="12", block="pib", text=
        "{t}E o dado pode ser outro. [p=0.3] {a}Pode ser o *PIB:* [p=0.2] a soma de tudo o que um país produz em um ano, [p=0.2] "
        "uma medida da riqueza. [p=0.4] {b}Num mapa de PIB, [p=0.2] os países ricos incham, [p=0.2] {c}e boa parte da África murcha. "
        "[p=0.4] {d}A anamorfose faz você *enxergar* a desigualdade."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="13", block="recap", text=
        "{t}Vamos juntar tudo em três frases. [p=0.5] {a}Um: [p=0.2] a resposta costuma estar na legenda. [p=0.5] {b}Dois: [p=0.2] "
        "anamorfose: o tamanho é um dado, não o território. [p=0.5] {c}Três: [p=0.2] projeção mantém a realidade; [p=0.2] "
        "anamorfose distorce de propósito. [p=0.4] Essa terceira, eu explico agora."),

    # ================= BLOCO D: ANAMORFOSE NÃO É PROJEÇÃO =================
    dict(id="14", block="naoproj", text=
        "{t}Então a anamorfose é uma projeção? [p=0.4] {a}Não. [p=0.3] Lembra: [p=0.2] a projeção é o jeito de passar a Terra para o papel, "
        "[p=0.2] {b}e ela *tenta* manter a realidade: [p=0.2] a área, a forma ou a distância. [p=0.4] {c}A anamorfose faz o contrário: "
        "[p=0.2] *abandona* a área real, [p=0.2] de propósito, [p=0.2] para mostrar um dado. [p=0.4] {d}Se a questão diz que a área "
        "corresponde ao PIB ou à população, [p=0.2] é anamorfose."),

    # ================= BLOCO E: ROTEIRO DE LEITURA =================
    dict(id="15", block="roteiro", text=
        "{t}E como ler *qualquer* mapa da prova, sem se perder? [p=0.4] São quatro passos. [p=0.4] {a}Um: [p=0.2] *título e fonte:* "
        "[p=0.2] o que o mapa quer mostrar, e de quando. [p=0.4] {b}Dois: [p=0.2] *a legenda:* [p=0.2] o que cada cor ou símbolo significa. "
        "[p=0.2] É aqui que a resposta costuma estar."),
    dict(id="16", block="roteiro", text=
        "{c}Três: [p=0.2] *a escala:* [p=0.2] grande ou pequena, [p=0.2] o que dá e o que não dá para concluir com aquele detalhe. [p=0.4] "
        "{d}Quatro: [p=0.2] *orientação e projeção:* [p=0.2] onde fica o norte, [p=0.2] e se dá para comparar as áreas."),

    # ================= APLICANDO O ROTEIRO =================
    dict(id="17", block="aplica", text=
        "{t}Vamos aplicar num mapa inventado. [p=0.4] {a}Passo um, o título: [p=0.2] \"Chuva por ano em um estado fictício, [p=0.2] "
        "dados de dois mil e vinte e cinco\". [p=0.3] Já sei o assunto e o ano. [p=0.4] {b}Passo dois, a legenda: [p=0.2] do claro ao escuro, "
        "[p=0.2] menos chuva até mais chuva. [p=0.3] É gradação."),
    dict(id="18", block="aplica", text=
        "{c}Então a região mais escura, no litoral, [p=0.2] é a que mais chove. [p=0.4] {d}Passo três, a escala: [p=0.2] um mapa de um estado, "
        "[p=0.2] escala pequena. [p=0.2] Dá para comparar regiões, [p=0.2] não ruas. [p=0.4] {e}Passo quatro: [p=0.2] o norte está para cima. "
        "[p=0.4] {f}Pronto: [p=0.2] mapa lido, sem adivinhar nada."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erro1", text=
        "{t}Agora, os três erros que mais derrubam gente. [p=0.4] {a}Primeiro: [p=0.2] confundir anamorfose com projeção equivalente. [p=0.4] "
        "{b}Parece certo, porque as duas falam de *área.* [p=0.4] {c}Mas a equivalente *mantém* a área real. [p=0.3] {d}A anamorfose *troca* "
        "a área por um dado."),
    dict(id="20", block="erro2", text=
        "{a}Segundo: [p=0.2] achar que o país maior na anamorfose é o que tem mais território. [p=0.4] {b}Parece certo, porque num mapa comum "
        "é assim. [p=0.4] {c}Mas ali o tamanho é o *dado:* [p=0.2] a Índia fica enorme por causa da população, [p=0.2] não do território."),
    dict(id="21", block="erro3", text=
        "{a}Terceiro: [p=0.2] ignorar a legenda e tentar adivinhar pelas cores. [p=0.4] {b}Parece certo, porque a gente acha que vermelho "
        "é sempre ruim, e verde, bom. [p=0.4] {c}Mas cada mapa escolhe as suas cores. [p=0.3] {d}Quem manda é a *legenda.*"),

    # ================= QUESTÃO 6 =================
    dict(id="22", block="questao", text=
        "{t}Hora de treinar, no estilo do ENEM. [p=0.4] {e1}Num mapa-múndi, a área de cada país foi desenhada proporcional ao número de habitantes. "
        "[p=0.4] {e2}A Índia e a China aparecem enormes; [p=0.2] o Canadá, a Rússia e a Austrália, [p=0.2] faixas estreitas, "
        "[p=0.2] mas todos na mesma posição. [p=0.4] {e3}Esse tipo de representação é..."),
    dict(id="23", block="questao", text=
        "{t}As alternativas. [p=0.3] {a}A: [p=0.2] uma anamorfose, em que a área expressa o valor de um dado, e não o território. [p=0.4] "
        "{b}B: [p=0.2] uma projeção equivalente, que mantém as áreas reais. [p=0.4] {c}C: [p=0.2] uma projeção conforme, que preserva as formas. "
        "[p=0.4] {d}D: [p=0.2] um mapa de escala grande, que mostra os países populosos com mais detalhe. [p=0.4] "
        "{e}E: [p=0.2] uma projeção azimutal equidistante. [p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="24", block="questao", text=
        "{t}Vamos eliminar. [p=0.3] {b}B é o oposto: [p=0.2] na equivalente, o Canadá e a Rússia seriam *enormes.* [p=0.2] Fora. [p=0.4] "
        "{c}C não explica por que a Índia, perto do Equador, cresceu. [p=0.2] Fora. [p=0.4] {d}D confunde escala com tamanho do desenho: "
        "[p=0.2] o mapa-múndi inteiro tem escala pequena. [p=0.2] Fora."),
    dict(id="25", block="questao", text=
        "{e}E fala de distâncias a partir de um ponto, [p=0.2] que não têm nada a ver com população. [p=0.2] Fora. [p=0.4] {a}Resposta: [p=0.2] "
        "*letra A.* [p=0.3] {x}O tamanho é o dado: [p=0.2] anamorfose."),

    dict(id="25b", block="dica", text=
        "{t}E uma dica para a prova: [p=0.3] {a}sempre que o enunciado disser que o tamanho é *proporcional* a um dado, [p=0.2] "
        "como população, PIB ou emissões, [p=0.4] {b}pense nos balões. [p=0.3] {c}É anamorfose. [p=0.4] {d}E se disser que as áreas são as *reais,* "
        "[p=0.2] aí é projeção equivalente."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="26", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] a resposta costuma estar na legenda. [p=0.5] {b}Dois: [p=0.2] "
        "anamorfose: o tamanho é um dado, não o território. [p=0.5] {c}Três: [p=0.2] projeção mantém a realidade; [p=0.2] "
        "anamorfose distorce de propósito."),

    # ================= PONTE =================
    dict(id="27", block="ponte", text=
        "{t}Você já viu os cinco temas de Cartografia. [p=0.4] {a}No último episódio, [p=0.2] vamos juntar tudo, [p=0.3] {b}caçar as pegadinhas "
        "[p=0.2] e treinar com questões misturadas."),
    dict(id="28", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para não perder o último episódio. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] que dado você gostaria de ver num mapa de balões? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
