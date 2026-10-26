# Roteiro — Cartografia, Episódio 2: Coordenadas geográficas e orientação (aula para iniciantes)
# Base: Estudos/Enem/estudos/04-geografia/01-cartografia.html — seções 04 e 05 + Questões 4 e 9 da seção 12
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: BATALHA NAVAL — uma linha e uma coluna acham qualquer ponto.
#   latitude = quanto acima ou abaixo do Equador · longitude = quanto à direita ou à esquerda de Greenwich
# Frases-chave (meio e fim, idênticas):
#   1. Latitude: a partir do Equador, até noventa graus.
#   2. Longitude: a partir de Greenwich, até cento e oitenta graus.
#   3. Um grau de latitude vale cerca de cento e onze quilômetros.

TITULO = "Latitude e Longitude do Zero: a Batalha Naval do Planeta | Cartografia Ep. 2"
PRONUNCIA = {
    "ENEM": "Enem",
    "GPS": "G P S",
    "Greenwich": "Grínuitch",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "Abra o mapa do celular e aperte o botão de localização. [p=0.4] {a}Em um segundo, aparece um pontinho azul: [p=0.2] *você.* "
        "[p=0.5] {b}Com só *dois números,* [p=0.2] o GPS sabe exatamente onde você está, [p=0.2] em qualquer lugar do planeta. [p=0.5] "
        "{c}Que números são esses?"),
    dict(id="02", block="promessa", text=
        "Até o fim desta aula, [p=0.2] {a}você vai conseguir localizar qualquer ponto da Terra, [p=0.3] {b}calcular a distância entre "
        "dois lugares, [p=0.3] {c}e descobrir para que lado fica um lugar, [p=0.2] só olhando esses dois números."),

    # ================= PRÉ-REQUISITOS RELÂMPAGO =================
    dict(id="03", block="grau", text=
        "Antes, duas coisinhas rápidas. [p=0.4] {a}Primeira: *grau.* [p=0.3] Grau é a medida de uma abertura, [p=0.2] como a abertura "
        "dos ponteiros de um relógio. [p=0.4] {b}Uma volta completa tem *trezentos e sessenta graus.* [p=0.3] {c}Meia volta, cento e oitenta. "
        "[p=0.3] {d}E um quarto de volta, [p=0.2] o canto de um quadrado, [p=0.2] noventa."),
    dict(id="04", block="terra", text=
        "{a}Segunda: [p=0.2] a Terra é uma bola, [p=0.2] e ela gira em volta de um eixo, [p=0.2] como um espeto imaginário. [p=0.4] "
        "{b}As pontas desse espeto são os *polos:* [p=0.2] o Polo Norte, em cima, [p=0.2] e o Polo Sul, embaixo."),

    # ================= ÂNCORA: BATALHA NAVAL =================
    dict(id="05", block="batalha", text=
        "{t}Agora, lembra do jogo de batalha naval? [p=0.4] {a}O tabuleiro tem linhas e colunas. [p=0.3] {b}Para atacar, você fala uma linha "
        "e uma coluna: [p=0.2] *B, cinco.* [p=0.4] {c}E pronto: [p=0.2] com só duas informações, você acha *uma* casinha exata. [p=0.4] "
        "{d}A Terra tem um tabuleiro igualzinho, [p=0.2] desenhado por cima dela."),

    # ================= BLOCO A: PARALELOS E LATITUDE =================
    dict(id="06", block="equador", text=
        "{t}Mas onde começa esse tabuleiro? [p=0.4] {a}Imagine um cinto apertado bem no meio da Terra, [p=0.2] a mesma distância dos dois polos. "
        "[p=0.4] {b}Essa linha se chama *Equador.* [p=0.4] {c}Ela corta a Terra em duas metades. [p=0.3] E cada metade se chama *hemisfério:* "
        "[p=0.2] {d}o hemisfério *Norte,* em cima, [p=0.2] e o hemisfério *Sul,* embaixo."),
    dict(id="07", block="paralelos", text=
        "{t}Agora, desenhe outros cintos, [p=0.2] acima e abaixo do Equador, [p=0.2] todos na mesma direção dele. [p=0.4] "
        "{a}Eles vão ficando menores perto dos polos. [p=0.4] {b}Essas linhas se chamam *paralelos,* [p=0.2] porque são paralelas ao Equador. "
        "[p=0.4] {c}Elas são as *linhas* do nosso tabuleiro."),
    dict(id="08", block="latitude", text=
        "{t}E como dizer em qual linha você está? [p=0.4] {a}Pela *latitude.* [p=0.3] Latitude diz *quanto acima ou abaixo* do Equador "
        "fica um lugar. [p=0.4] {b}Ela é medida em graus, [p=0.2] a partir do centro da Terra. [p=0.4] {c}O Equador é *zero grau.* [p=0.3] "
        "{d}E cada polo é *noventa graus:* [p=0.2] noventa norte, [p=0.2] ou noventa sul."),
    dict(id="09", block="latitude", text=
        "{e}Então, um lugar a quarenta graus norte [p=0.2] fica acima do Equador, [p=0.2] a quarenta graus de abertura. [p=0.4] "
        "{f}E é por isso que a latitude sempre vem com uma letra: [p=0.2] *N* para norte, [p=0.2] *S* para sul. [p=0.3] "
        "Sem a letra, você não sabe de que lado está."),

    # ================= BLOCO B: MERIDIANOS E LONGITUDE =================
    dict(id="10", block="meridianos", text=
        "{t}E as colunas do tabuleiro? [p=0.4] {a}Pense nos gomos de uma laranja: [p=0.2] as marcas vão de uma ponta à outra. [p=0.4] "
        "{b}Na Terra, linhas assim vão do Polo Norte ao Polo Sul. [p=0.4] {c}Elas se chamam *meridianos.* [p=0.3] "
        "São as *colunas* do tabuleiro."),
    dict(id="11", block="greenwich", text=
        "{t}Mas aqui tem um problema: [p=0.2] qual meridiano é o zero? [p=0.4] {a}Nos paralelos, o Equador é o meio natural. [p=0.3] "
        "{b}Nos meridianos, *não existe* um meio natural. [p=0.4] {c}Então os países fizeram um acordo: [p=0.2] o zero passa por *Greenwich,* "
        "[p=0.2] um bairro de Londres, onde fica um observatório antigo. [p=0.4] {d}É o *meridiano de Greenwich.*"),
    dict(id="12", block="longitude", text=
        "{t}E como dizer em qual coluna você está? [p=0.4] {a}Pela *longitude.* [p=0.3] Longitude diz *quanto à direita ou à esquerda* "
        "de Greenwich fica um lugar. [p=0.4] {b}Greenwich é zero grau. [p=0.3] {c}E ela vai até *cento e oitenta graus,* [p=0.2] "
        "para *leste,* [p=0.2] ou para *oeste.* [p=0.4] {d}Leste, à direita de Greenwich no mapa; [p=0.2] oeste, à esquerda."),
    dict(id="13", block="ancora", text=
        "{t}Pronto: [p=0.2] o tabuleiro da batalha naval está completo. [p=0.4] {a}A latitude é a linha: [p=0.2] quanto acima ou abaixo do Equador. "
        "[p=0.4] {b}A longitude é a coluna: [p=0.2] quanto à direita ou à esquerda de Greenwich. [p=0.4] {c}E esses são os dois números do GPS."),

    # ================= BLOCO C: POR QUE 90 E 180 =================
    dict(id="14", block="porque", text=
        "{t}Mas por que a latitude para em noventa, [p=0.2] e a longitude vai até cento e oitenta? [p=0.5] {a}A latitude sobe do Equador "
        "até o polo. [p=0.3] Isso é um quarto de volta: [p=0.2] *noventa graus.* [p=0.4] {b}A longitude anda em volta da Terra, [p=0.2] "
        "e a volta inteira tem trezentos e sessenta. [p=0.3] {c}Metade para leste, [p=0.2] metade para oeste: [p=0.2] *cento e oitenta* para cada lado."),

    # ================= BLOCO D: AS LINHAS IMPORTANTES E O BRASIL =================
    dict(id="15", block="linhas", text=
        "{t}Alguns paralelos têm nome próprio. [p=0.4] {a}O maior de todos é o Equador. [p=0.4] {b}Perto de vinte e três graus e meio, "
        "[p=0.2] ao norte e ao sul, [p=0.2] ficam os *trópicos.* [p=0.3] Trópico é o limite até onde o Sol pode ficar *bem em cima da cabeça* ao meio-dia. "
        "[p=0.4] {c}O de cima é o Trópico de Câncer. [p=0.2] O de baixo, o Trópico de Capricórnio."),
    dict(id="16", block="linhas", text=
        "{d}E perto de sessenta e seis graus e meio ficam os *círculos polares.* [p=0.4] A partir deles, [p=0.2] existe pelo menos um dia por ano "
        "com vinte e quatro horas de luz, [p=0.2] ou vinte e quatro horas de escuridão."),
    dict(id="17", block="brasil", text=
        "{t}E onde está o Brasil nesse tabuleiro? [p=0.4] {a}O Equador corta o norte do país, [p=0.2] no Amapá, Roraima, Amazonas e Pará. "
        "[p=0.4] {b}O Trópico de Capricórnio corta São Paulo, Paraná e Mato Grosso do Sul. [p=0.4] {c}A maior parte do país fica no hemisfério *Sul.* "
        "[p=0.4] {d}E o Brasil inteiro fica à esquerda de Greenwich: [p=0.2] todas as nossas longitudes são *oeste.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos parar e juntar tudo em três frases. [p=0.5] {a}Um: [p=0.2] latitude: a partir do Equador, até noventa graus. [p=0.5] "
        "{b}Dois: [p=0.2] longitude: a partir de Greenwich, até cento e oitenta graus. [p=0.5] {c}Três: [p=0.2] um grau de latitude vale "
        "cerca de cento e onze quilômetros. [p=0.4] Calma, que essa terceira eu explico agora."),

    # ================= BLOCO E: DISTÂNCIA NO MERIDIANO =================
    dict(id="19", block="km", text=
        "{t}Quanto vale um grau, em quilômetros? [p=0.4] {a}Dar uma volta inteira na Terra são uns *quarenta mil quilômetros.* [p=0.4] "
        "{b}E uma volta tem trezentos e sessenta graus. [p=0.4] {c}Então cada grau vale quarenta mil dividido por trezentos e sessenta: "
        "[p=0.3] {d}*cento e onze quilômetros,* mais ou menos."),
    dict(id="20", block="subtrai", text=
        "{t}Agora, dois lugares na mesma coluna, [p=0.2] ou seja, no mesmo meridiano. [p=0.4] {a}Um a dois graus sul, [p=0.2] {b}o outro "
        "a vinte e dois graus sul. [p=0.4] {c}Os dois estão do mesmo lado do Equador, [p=0.2] então a diferença é de vinte e dois *menos* dois: "
        "[p=0.2] vinte graus. [p=0.4] {d}Vinte vezes cento e onze: [p=0.2] *dois mil, duzentos e vinte quilômetros.*"),
    dict(id="21", block="soma", text=
        "{t}E se um estiver no Norte e o outro no Sul? [p=0.4] {a}Cinco graus norte, [p=0.2] e quinze graus sul. [p=0.4] {b}Do primeiro até o Equador "
        "são cinco graus. [p=0.3] {c}Do Equador até o segundo, [p=0.2] mais quinze. [p=0.4] {d}O caminho atravessa o Equador, [p=0.2] "
        "então você *soma:* [p=0.2] vinte graus."),
    dict(id="22", block="lonnao", text=
        "{t}E por que essa conta *não* vale para a longitude? [p=0.4] {a}Volte aos gomos da laranja: [p=0.2] eles são largos no meio, [p=0.3] "
        "{b}e vão se *apertando* até se encontrarem nos polos. [p=0.4] {c}Então um grau de longitude é largo no Equador, [p=0.2] "
        "e vai encolhendo até virar *zero* no polo."),

    # ================= BLOCO F: ROSA DOS VENTOS =================
    dict(id="23", block="rosa", text=
        "{t}Agora, a orientação. [p=0.3] Como dizer para que lado alguma coisa fica? [p=0.4] {a}Com a *rosa dos ventos,* [p=0.2] aquela estrela "
        "que aparece no canto dos mapas. [p=0.4] {b}As quatro direções principais são os *pontos cardeais:* [p=0.2] norte, sul, leste e oeste. "
        "[p=0.4] {c}Entre dois cardeais, ficam os *colaterais:* [p=0.2] nordeste, sudeste, sudoeste e noroeste. [p=0.4] "
        "{d}E entre um cardeal e um colateral, [p=0.2] os *subcolaterais,* como nor-nordeste."),

    # ================= BLOCO G: DIREÇÃO PELAS COORDENADAS =================
    dict(id="24", block="direcao", text=
        "{t}E dá para descobrir a direção só pelos números? [p=0.4] Dá, [p=0.2] olhando a linha e a coluna *separadamente.* [p=0.4] "
        "{a}Na latitude: [p=0.2] quanto maior o número sul, [p=0.2] mais para o *sul.* [p=0.4] {b}Na longitude, aqui no lado oeste: [p=0.2] "
        "quanto *menor* o número, [p=0.2] mais perto de Greenwich, [p=0.2] ou seja, mais para o *leste.*"),

    # ================= BLOCO H: CURIOSIDADES =================
    dict(id="25", block="sol", text=
        "{t}Uma curiosidade: [p=0.2] o Sol nasce no leste? [p=0.4] {a}Exatamente no leste, [p=0.2] só em dois dias do ano: [p=0.2] "
        "os *equinócios,* [p=0.2] em março e em setembro, [p=0.2] quando o dia e a noite têm a mesma duração. [p=0.4] {b}No resto do ano, "
        "[p=0.2] ele nasce um pouco para o nordeste, [p=0.2] ou para o sudeste."),
    dict(id="26", block="bussola", text=
        "{t}E a bússola aponta para o Polo Norte? [p=0.4] {a}Quase. [p=0.2] Ela aponta para o *polo magnético,* [p=0.2] que fica perto, "
        "[p=0.2] mas não no mesmo lugar. [p=0.4] {b}A diferença entre os dois nortes se chama *declinação magnética.* [p=0.4] "
        "{c}E ela muda com o tempo: [p=0.2] por isso os mapas de trilha trazem esse número."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="27", block="erro1", text=
        "{t}Agora, os três erros que mais derrubam gente. [p=0.4] {a}Primeiro: [p=0.2] medir a latitude a partir de Greenwich. [p=0.4] "
        "{b}Parece certo, porque Greenwich é o famoso ponto zero. [p=0.4] {c}Mas Greenwich é o zero da *longitude.* [p=0.3] "
        "{d}A latitude começa no *Equador.*"),
    dict(id="28", block="erro2", text=
        "{a}Segundo: [p=0.2] de cinco graus norte a quinze graus sul, [p=0.2] fazer quinze menos cinco, [p=0.2] e dar dez. [p=0.4] "
        "{b}Parece certo, porque a gente sempre subtrai para achar diferença. [p=0.4] {c}Mas os dois estão em lados opostos do Equador. "
        "[p=0.3] {d}Aí você *soma:* [p=0.2] vinte graus."),
    dict(id="29", block="erro3", text=
        "{a}Terceiro: [p=0.2] achar que quarenta graus oeste fica mais a oeste que cinquenta graus oeste. [p=0.4] {b}Parece certo, "
        "porque a gente lê só o número. [p=0.4] {c}Mas o número conta a distância *até Greenwich.* [p=0.3] Quarenta está mais perto. "
        "[p=0.3] {d}Então quarenta oeste fica mais a *leste.*"),

    # ================= QUESTÃO 4 =================
    dict(id="30", block="q4", text=
        "{t}Hora de treinar, no estilo do ENEM. [p=0.4] {e1}Dois povoados, A e B, estão no mesmo meridiano, [p=0.2] cinquenta graus oeste. "
        "[p=0.4] {e2}A está a dois graus sul. [p=0.2] B está a vinte e dois graus sul. [p=0.4] {e3}Um grau de latitude vale cerca de "
        "cento e onze quilômetros. [p=0.3] Qual é a distância entre eles?"),
    dict(id="31", block="q4", text=
        "{t}As alternativas: [p=0.3] {a}A: duzentos e vinte e dois quilômetros. [p=0.3] {b}B: mil, cento e dez. [p=0.3] "
        "{c}C: dois mil, duzentos e vinte. [p=0.3] {d}D: dois mil, seiscentos e sessenta e quatro. [p=0.3] {e}E: cinco mil, quinhentos e cinquenta. "
        "[p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="32", block="q4", text=
        "{t}Os dois estão no Sul: [p=0.2] mesmo hemisfério, [p=0.2] então subtrai. [p=0.3] Vinte e dois menos dois: [p=0.2] vinte graus. "
        "[p=0.4] {a}A usou só os dois graus de A. [p=0.2] Fora. [p=0.3] {b}B usou dez graus, [p=0.2] que não é a diferença. [p=0.2] Fora. "
        "[p=0.3] {d}D *somou,* [p=0.2] vinte e quatro graus. [p=0.2] Fora. [p=0.3] {e}E usou a longitude, cinquenta, [p=0.2] que é igual "
        "para os dois e nem entra na conta. [p=0.2] Fora. [p=0.4] {c}Vinte vezes cento e onze: [p=0.2] *letra C,* dois mil, duzentos e vinte."),

    # ================= QUESTÃO 9 =================
    dict(id="33", block="q9", text=
        "{t}Agora, a segunda. [p=0.3] {e1}Um avião sai de uma fazenda em dez graus sul e cinquenta graus oeste, [p=0.3] {e2}e voa até outra, "
        "em vinte graus sul e quarenta graus oeste. [p=0.4] {e3}Para que lado fica o destino?"),
    dict(id="34", block="q9", text=
        "{t}As alternativas: [p=0.3] {a}A: nordeste. [p=0.2] {b}B: noroeste. [p=0.2] {c}C: sudoeste. [p=0.2] {d}D: sudeste. [p=0.2] "
        "{e}E: leste. [p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="35", block="q9", text=
        "{t}Vamos desenhar numa grade. [p=0.4] {s1}Latitude: de dez para vinte graus sul, [p=0.2] o avião desce: [p=0.2] vai para o *sul.* "
        "[p=0.4] {s2}Longitude: de cinquenta para quarenta graus oeste, [p=0.2] chega mais perto de Greenwich: [p=0.2] vai para o *leste.* "
        "[p=0.4] {r}Sul mais leste: [p=0.2] *sudeste,* letra D."),
    dict(id="36", block="q9", text=
        "{c}A C, sudoeste, [p=0.2] é o erro do quarenta parecer mais a oeste. [p=0.3] Fora. [p=0.3] {a}A A, nordeste, [p=0.2] erra o sentido da latitude. "
        "[p=0.2] Fora. [p=0.3] {b}A B, noroeste, [p=0.2] erra os dois. [p=0.2] Fora. [p=0.3] {e}E a E, leste, [p=0.2] esquece que a latitude também mudou. "
        "[p=0.2] Fora."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="37", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] latitude: a partir do Equador, até noventa graus. [p=0.5] "
        "{b}Dois: [p=0.2] longitude: a partir de Greenwich, até cento e oitenta graus. [p=0.5] {c}Três: [p=0.2] um grau de latitude vale "
        "cerca de cento e onze quilômetros."),

    # ================= PONTE =================
    dict(id="38", block="ponte", text=
        "{t}E agora, uma pergunta para o próximo episódio. [p=0.4] {a}Se a Terra é uma bola, [p=0.2] como dá para desenhá-la numa folha plana? "
        "[p=0.5] {b}Spoiler: [p=0.2] não dá sem *distorcer.* [p=0.4] {c}Esse é o próximo episódio: [p=0.2] *as projeções.*"),
    dict(id="39", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para não perder os próximos episódios. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha caído na pegadinha do quarenta oeste? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
