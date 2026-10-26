# Roteiro — Cartografia, Episódio 3: Projeções cartográficas (aula para iniciantes)
# Base: Estudos/Enem/estudos/04-geografia/01-cartografia.html — seções 06 e 07 + Questão 5 da seção 12
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: achatar a Terra é como achatar a casca de uma laranja: ou ela rasga, ou estica.
#   Toda projeção escolhe ONDE esticar.
# Frases-chave (meio e fim, idênticas):
#   1. Todo mapa distorce alguma coisa.
#   2. Conforme guarda a forma; equivalente guarda a área. Nunca as duas.
#   3. Mercator infla os polos; Peters acerta as áreas e estica as formas.

TITULO = "Por Que Todo Mapa Mente: Mercator x Peters | Cartografia Ep. 3"
PRONUNCIA = {
    "ENEM": "Enem",
    "ONU": "O N U",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "Olhe o mapa-múndi da sua escola. [p=0.3] {a}Lá em cima, a Groenlândia. [p=0.3] {b}Aqui embaixo, a África. [p=0.4] "
        "{c}Parecem do mesmo tamanho. [p=0.5] {d}Só que a África é cerca de *catorze vezes* maior. [p=0.5] "
        "{e}Por que o mapa da sua escola *mentiu* para você?"),
    dict(id="02", block="promessa", text=
        "Até o fim desta aula, [p=0.2] {a}você vai entender por que *nenhum* mapa é perfeito, [p=0.3] {b}reconhecer os tipos de projeção, "
        "[p=0.3] {c}e saber por que escolher um mapa é uma decisão *política.*"),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prelat", text=
        "Antes, duas coisinhas rápidas. [p=0.3] {a}Lembra da *latitude,* do episódio passado? [p=0.2] É o quanto um lugar fica acima "
        "ou abaixo do Equador, em graus. [p=0.4] {b}*Alta latitude* é perto dos polos. [p=0.3] {c}*Baixa latitude* é perto do Equador."),
    dict(id="04", block="preforma", text=
        "{a}Segunda: [p=0.2] *área* e *forma* são coisas diferentes. [p=0.3] Área é o *tamanho:* [p=0.2] quanto chão cabe dentro. "
        "[p=0.4] {b}Forma é o *contorno:* [p=0.2] o desenho da borda. [p=0.4] {c}Um quadrado e um retângulo comprido podem ter a mesma área, "
        "[p=0.2] e formas bem diferentes."),

    # ================= BLOCO A: O PROBLEMA =================
    dict(id="05", block="laranja", text=
        "{t}Agora, a pergunta: [p=0.2] dá para desenhar a Terra numa folha, sem errar nada? [p=0.5] {a}Pegue uma laranja e descasque, "
        "[p=0.2] tentando tirar a casca inteira. [p=0.4] {b}Agora tente achatar essa casca na mesa. [p=0.5] {c}Ou ela *rasga,* "
        "[p=0.3] {d}ou ela *estica.* [p=0.4] Uma bola não vira uma folha sem estragar alguma coisa."),
    dict(id="06", block="projecao", text=
        "{t}Com a Terra é igual. [p=0.3] {a}Todo jeito de passar a Terra redonda para o papel plano se chama *projeção.* [p=0.4] "
        "{b}E toda projeção tem que esticar em algum lugar. [p=0.4] {c}A diferença entre elas é *onde* esticar. [p=0.4] "
        "{d}É por isso que *todo mapa distorce alguma coisa.*"),

    # ================= BLOCO B: AS TRÊS SUPERFÍCIES =================
    dict(id="07", block="lampada", text=
        "{t}E como se faz uma projeção? [p=0.4] {a}Imagine um globo de vidro, transparente, com as linhas desenhadas. [p=0.3] "
        "{b}Acenda uma lâmpada lá dentro. [p=0.4] {c}As linhas fazem *sombra* num papel encostado no globo. [p=0.4] "
        "{d}E esse papel pode ser enrolado de *três* jeitos."),
    dict(id="08", block="superficies", text=
        "{c}Primeiro: [p=0.2] enrolado como um *tubo,* [p=0.2] encostando no Equador. [p=0.3] É a projeção *cilíndrica.* [p=0.4] "
        "As linhas viram retas, [p=0.2] e ela serve para o mapa-múndi."),
    dict(id="09", block="superficies", text=
        "{k}Segundo: [p=0.2] enrolado como um *chapéu de festa,* [p=0.2] encostando num paralelo. [p=0.3] É a projeção *cônica.* [p=0.4] "
        "Boa para países no meio do caminho entre o Equador e o polo, [p=0.2] como os Estados Unidos e os da Europa."),
    dict(id="10", block="superficies", text=
        "{z}Terceiro: [p=0.2] uma folha *reta,* [p=0.2] encostando num ponto só, [p=0.2] como o polo. [p=0.3] É a projeção *azimutal,* "
        "[p=0.2] também chamada de plana. [p=0.4] Ótima para as regiões polares. [p=0.3] A bandeira da ONU usa uma assim."),
    dict(id="11", block="toque", text=
        "{t}E onde o mapa erra *menos?* [p=0.4] {a}Onde o papel *encosta* no globo. [p=0.3] Ali, papel e globo são quase a mesma coisa. "
        "[p=0.4] {b}Quanto mais longe do toque, [p=0.2] mais a sombra precisa esticar, [p=0.2] {c}e maior a distorção."),

    # ================= BLOCO C: O QUE CADA PROJEÇÃO CONSERVA =================
    dict(id="12", block="conserva", text=
        "{t}Se vai ter que esticar, [p=0.2] o que você *protege?* [p=0.4] {a}Voltando à laranja: [p=0.2] você pode proteger o desenho da borda, "
        "[p=0.3] ou o tamanho de cada pedaço. [p=0.4] {b}Cada projeção escolhe o que salvar."),
    dict(id="13", block="conserva", text=
        "{c}A projeção *conforme* protege a *forma.* [p=0.3] Os contornos e os ângulos saem certos, [p=0.2] pelo menos em pedaços pequenos. "
        "[p=0.4] {c2}O preço: [p=0.2] as *áreas* ficam erradas."),
    dict(id="14", block="conserva", text=
        "{e}A projeção *equivalente* protege a *área:* [p=0.2] o tamanho de cada país fica na proporção certa. [p=0.4] "
        "{e2}O preço: [p=0.2] as *formas* saem esticadas ou achatadas."),
    dict(id="15", block="conserva", text=
        "{d}E tem mais duas. [p=0.3] A *equidistante* acerta as *distâncias* a partir de um ponto, [p=0.2] como o centro da bandeira da ONU. "
        "[p=0.4] {f}E a *afilática* não acerta nada perfeitamente: [p=0.2] erra um pouco em tudo, [p=0.2] para o erro total ficar pequeno. "
        "[p=0.3] É a mais comum nos atlas."),
    dict(id="16", block="regra", text=
        "{t}E a regra de ouro: [p=0.3] {a}é *impossível* guardar forma e área ao mesmo tempo. [p=0.4] {b}Na laranja: [p=0.2] se a casca "
        "não pode rasgar e você quer o contorno perfeito, [p=0.3] {c}ela tem que esticar *o tamanho.* [p=0.4] Ou um, ou outro."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Vamos juntar tudo em três frases. [p=0.5] {a}Um: [p=0.2] todo mapa distorce alguma coisa. [p=0.5] {b}Dois: [p=0.2] "
        "conforme guarda a forma; [p=0.2] equivalente guarda a área. [p=0.2] Nunca as duas. [p=0.5] {c}Três: [p=0.2] Mercator infla os polos; "
        "[p=0.2] Peters acerta as áreas e estica as formas. [p=0.4] Essa terceira, eu explico agora."),

    # ================= BLOCO D: MERCATOR =================
    dict(id="18", block="mercator", text=
        "{t}Em mil quinhentos e sessenta e nove, [p=0.2] o geógrafo Mercator criou um mapa para os *navegadores.* [p=0.4] "
        "{a}É uma projeção cilíndrica e *conforme.* [p=0.4] {b}A grande vantagem: [p=0.2] uma rota com a bússola sempre na mesma direção "
        "[p=0.2] vira uma linha *reta* no mapa. [p=0.3] Perfeito para quem estava no meio do oceano."),
    dict(id="19", block="mercator", text=
        "{c}Mas por que ela incha os polos? [p=0.4] {d}No globo, os meridianos se encontram nos polos, [p=0.2] como os gomos da laranja. "
        "[p=0.4] {e}No mapa cilíndrico, eles viram retas em pé, [p=0.2] *paralelas.* [p=0.4] {f}Então, perto dos polos, [p=0.2] "
        "tudo fica esticado para os lados."),
    dict(id="20", block="mercator", text=
        "{g}E para não deformar o contorno, [p=0.2] a Mercator estica para cima *na mesma medida.* [p=0.5] {h}A sessenta graus de latitude, "
        "[p=0.2] a largura dobra, [p=0.2] e a altura dobra também. [p=0.3] {i}Duas vezes duas: [p=0.2] a área aparece *quatro vezes* maior. "
        "[p=0.4] {j}A setenta graus, [p=0.2] mais de oito vezes."),
    dict(id="21", block="truesize", text=
        "{t}Agora veja a Groenlândia, [p=0.2] lá em cima, em alta latitude, [p=0.2] toda inflada. [p=0.4] {a}Vamos arrastar ela até "
        "o Equador, [p=0.2] perto da África... [p=0.6] {b}Ela *encolhe.* [p=0.4] {c}Esse é o tamanho de verdade dela."),

    # ================= BLOCO E: PETERS =================
    dict(id="22", block="peters", text=
        "{t}Nos anos setenta, [p=0.2] o historiador Arno Peters espalhou pelo mundo um mapa diferente. [p=0.4] {a}Também cilíndrico, "
        "[p=0.2] mas *equivalente.* [p=0.4] {b}Os países aparecem com as áreas *reais:* [p=0.2] a África grande, [p=0.2] a Europa menor. "
        "[p=0.4] {c}O preço: [p=0.2] as formas ficam *esticadas* para cima e para baixo."),
    dict(id="23", block="lado", text=
        "{t}Coloque os dois lado a lado. [p=0.3] {a}A Mercator acerta as formas, [p=0.2] e erra as áreas. [p=0.4] "
        "{b}A Peters acerta as áreas, [p=0.2] e erra as formas. [p=0.4] {c}Nenhuma das duas é o mapa certo. [p=0.3] Cada uma serve para uma coisa."),

    # ================= BLOCO F: A POLÍTICA DOS MAPAS =================
    dict(id="24", block="politica", text=
        "{t}Mas quem decidiu que a Europa fica no meio do mapa, [p=0.2] e o norte, em cima? [p=0.5] {a}Ninguém descobriu isso na natureza. "
        "[p=0.3] São *convenções:* [p=0.2] combinados. [p=0.4] {b}E a Mercator, centrada na Europa, [p=0.2] ainda deixa os países ricos do norte "
        "maiores do que são. [p=0.4] {c}Isso é chamado de visão *eurocêntrica:* [p=0.2] olhar o mundo com a Europa no centro. "
        "[p=0.3] O mapa de Peters veio como uma crítica a isso."),
    dict(id="25", block="sulcima", text=
        "{t}Então, um mapa com o *sul em cima* está errado? [p=0.4] {a}Não. [p=0.3] Ele é tão correto quanto o tradicional. [p=0.4] "
        "{b}No espaço, não existe em cima nem embaixo. [p=0.4] {c}Todo mapa é uma *escolha:* [p=0.2] de projeção, [p=0.2] de centro, "
        "[p=0.2] e de qual lado fica para cima."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="26", block="erro1", text=
        "{t}Agora, os três erros que mais derrubam gente. [p=0.4] {a}Primeiro: [p=0.2] achar que a Mercator mostra as áreas reais. [p=0.4] "
        "{b}Parece certo, porque é o mapa que a gente vê a vida inteira. [p=0.4] {c}Mas ela é *conforme:* [p=0.2] guarda a forma, "
        "[p=0.2] {d}e infla as áreas perto dos polos."),
    dict(id="27", block="erro2", text=
        "{a}Segundo: [p=0.2] dizer que a Peters preserva as formas. [p=0.4] {b}Parece certo, porque ela é a projeção \"mais justa\". [p=0.4] "
        "{c}Mas ela é *equivalente:* [p=0.2] acerta a área, [p=0.2] {d}e estica as formas."),
    dict(id="28", block="erro3", text=
        "{a}Terceiro: [p=0.2] achar que a distorção é maior onde o cilindro *toca* o globo. [p=0.4] {b}Parece certo, porque é ali que "
        "\"acontece\" a projeção. [p=0.4] {c}Mas é o contrário: [p=0.2] onde toca, a distorção é *menor.* [p=0.3] {d}Ela cresce longe do toque."),

    # ================= QUESTÃO 5 =================
    dict(id="29", block="questao", text=
        "{t}Hora de treinar, no estilo do ENEM. [p=0.4] {e1}Em muitos mapas escolares, a Groenlândia aparece do tamanho da África, "
        "[p=0.2] {e2}embora a África seja cerca de catorze vezes maior. [p=0.4] {e3}Essa distorção acontece porque esses mapas usam uma projeção..."),
    dict(id="30", block="questao", text=
        "{t}As alternativas. [p=0.3] {a}A: [p=0.2] equivalente, que preserva as formas e reduz as áreas perto do Equador. [p=0.4] "
        "{b}B: [p=0.2] azimutal centrada no Polo Norte, que amplia as áreas perto do ponto de contato. [p=0.4] {c}C: [p=0.2] cilíndrica, "
        "que exagera as áreas perto do Equador, onde o cilindro toca o globo. [p=0.4] {d}D: [p=0.2] cônica, que é fiel nas latitudes médias. "
        "[p=0.4] {e}E: [p=0.2] cilíndrica conforme, que preserva as formas, mas amplia cada vez mais as áreas em direção aos polos. "
        "[p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="31", block="questao", text=
        "{t}Vamos eliminar. [p=0.3] {a}A troca tudo: [p=0.2] a equivalente preserva a *área,* não a forma. [p=0.2] Fora. [p=0.4] "
        "{b}B diz que a distorção é maior perto do ponto de contato. [p=0.2] É o contrário. [p=0.2] Fora. [p=0.4] "
        "{c}C coloca o exagero no Equador, [p=0.2] justamente onde o cilindro toca, [p=0.2] e a distorção é menor. [p=0.2] Fora."),
    dict(id="32", block="questao", text=
        "{d}D fala da cônica, [p=0.2] que não é a do mapa-múndi escolar, [p=0.2] e não explica a Groenlândia inflada. [p=0.2] Fora. [p=0.4] "
        "{e}Resposta: [p=0.2] *letra E.* [p=0.3] {x}A Mercator: [p=0.2] cilíndrica, conforme, [p=0.2] e cada vez mais inflada rumo aos polos."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="33", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] todo mapa distorce alguma coisa. [p=0.5] {b}Dois: [p=0.2] "
        "conforme guarda a forma; [p=0.2] equivalente guarda a área. [p=0.2] Nunca as duas. [p=0.5] {c}Três: [p=0.2] Mercator infla os polos; "
        "[p=0.2] Peters acerta as áreas e estica as formas."),

    # ================= PONTE =================
    dict(id="34", block="ponte", text=
        "{t}Até agora, o mapa foi plano, [p=0.2] como uma folha. [p=0.4] {a}Mas o terreno tem morros e vales. [p=0.4] "
        "{b}Como mostrar *altura* num papel? [p=0.4] {c}Próximo episódio: [p=0.2] *curvas de nível.*"),
    dict(id="35", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para não perder os próximos episódios. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você também achava que a Groenlândia era do tamanho da África? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
