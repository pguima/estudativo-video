# Nós, os Antigos — Vídeo 01 (piloto): "O Que Vai Sobrar de Nós Daqui a 10.000 Anos?"
# Base: original/fontes.md (cada fato tem fonte; o que é moldura do museu de 2526 está marcado como FICÇÃO em `tela`).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa · números por extenso.
# Estrutura do modelo de episódio: vitrine → estranhamento → ciência → abismo → virada → etiqueta.

TITULO = "O Que Vai Sobrar de Nós Daqui a 10.000 Anos?"

VOZ = dict(
    voiceName="Zephyr",
    tags=["curiosa", "gentil"],
    prompt=("Narre um documentário de ciência animado: voz feminina adulta, calma, curiosa e acolhedora, de uma "
            "curadora de museu que admira o que está mostrando. Tom de quem conta um segredo fascinante, com humor "
            "leve e seco nas frases irônicas. Ritmo tranquilo, sem pressa, com as pausas marcadas. Nada de tom "
            "apocalíptico: mesmo nas partes sombrias, a voz continua serena. Leia apenas o texto, exatamente como "
            "está escrito, sem acrescentar, pular ou repetir nada."),
)

PRONUNCIA = {"Svalbard": "Sválbar", "Onkalo": "Ônkalo", "Crawford": "Cróford", "Voyager": "Vóiajer"}

SCENES = [
    # ── A VITRINE ─────────────────────────────────────────────
    dict(id="01", block="vitrine",
         tela="Escuro total. Um holofote âmbar acende sobre uma vitrine. Dentro, um bloco de rocha em camadas com um "
              "celular rachado preso no meio. Poeira no ar. Etiqueta: PEÇA Nº 001 · c. 2026 d.C. (FICÇÃO: o museu)",
         text=
        "{a}Esta peça foi encontrada dentro de uma camada de rocha. [p=0.3] "
        "{b}É um retângulo de vidro e metal, [p=0.1] com uma bateria morta por dentro. [p=0.3] "
        "{c}Os Antigos carregavam um destes no bolso [p=0.1] o dia inteiro. [p=0.2] "
        "Dormiam com ele do lado. [p=0.4] "
        "{d}Nós ainda não sabemos direito por quê."),
    dict(id="02", block="vitrine",
         tela="A câmera recua: o salão do museu de 2526, frio e verde-água, cheio de vitrines. A Lume entra flutuando, "
              "com a lanterna da antena acesa. Logo: NÓS, OS ANTIGOS. (FICÇÃO)",
         text=
        "{a}Bem-vindos ao *Museu da Era dos Antigos.* [p=0.2] "
        "{b}Eu sou a Lume, [p=0.1] a curadora. [p=0.3] "
        "{c}E hoje vamos abrir a primeira vitrine: [p=0.2] *o que sobrou deles.*"),

    # ── O ESTRANHAMENTO ──────────────────────────────────────
    dict(id="03", block="estranhamento",
         tela="Reconstituição quente e saturada do século 21: cidades acendendo, estradas se espalhando. Contador '8 "
              "BILHÕES'. Uma balança: de um lado prédios, estradas e máquinas; do outro árvores, animais e pessoas. "
              "Os pratos se equilibram em 2020. Fonte na tela: Nature, 2020.",
         text=
        "{a}Os Antigos viveram entre os séculos vinte e vinte e um. [p=0.2] Eram *oito bilhões.* [p=0.3] "
        "{b}E fabricavam coisas como nenhuma espécie antes deles. [p=0.3] "
        "{c}Por volta de *dois mil e vinte,* [p=0.1] o peso de tudo o que eles tinham construído, [p=0.1] "
        "prédios, [p=0.1] estradas, [p=0.1] máquinas, [p=0.2] {d}ficou igual ao peso de *todos os seres vivos* do "
        "planeta juntos."),
    dict(id="04", block="estranhamento",
         tela="Uma estante infinita de fotos, cartas e músicas vira ícones de arquivo, que viram pontos de "
              "interrogação e somem. Citação: 'idade das trevas digital' — Vint Cerf, 2015. Depois, a Lume diante de "
              "um terminal que mostra 'ARQUIVO ILEGÍVEL'. (A parte de 2526 é FICÇÃO)",
         text=
        "{a}E mesmo assim, [p=0.1] nós sabemos pouco sobre eles. [p=0.3] "
        "{b}Os Antigos guardavam quase tudo em formato digital: [p=0.1] fotos, [p=0.1] cartas, [p=0.1] livros, "
        "[p=0.1] músicas. [p=0.2] {c}E arquivo digital envelhece mal. [p=0.1] A cada troca de máquina, [p=0.1] "
        "um pouco ficava impossível de abrir. [p=0.3] "
        "{d}Em dois mil e quinze, [p=0.1] um dos criadores da internet, [p=0.1] Vint Cerf, [p=0.1] avisou: [p=0.2] "
        "a época deles podia virar uma *idade das trevas digital.* [p=0.4] "
        "{e}Por isso, aqui no museu, [p=0.1] estudamos os Antigos como se estudam as ruínas: [p=0.2] *pelo que fica "
        "no chão.*"),

    # ── A CIÊNCIA: AVANÇAR O RELÓGIO ─────────────────────────
    dict(id="05", block="relogio",
         tela="A câmera atravessa o vidro da vitrine (transição de assinatura) e entra numa cidade do século 21 "
              "vazia. Um relógio gigante no céu começa a girar: 100 ANOS · 1.000 ANOS · 10.000 ANOS.",
         text=
        "{a}Então vamos fazer um experimento. [p=0.2] Imagine que os Antigos saíram de cena [p=0.1] e ninguém "
        "ficou para consertar nada. [p=0.3] "
        "{b}Vamos avançar o relógio. [p=0.3] {c}*Cem anos.* [p=0.3] {d}*Mil anos.* [p=0.3] {e}*Dez mil anos.*"),
    dict(id="06", block="cem_anos",
         tela="Túnel do metrô de Nova York com bombas paradas; a água sobe devagar pelos trilhos (legenda: ~13 milhões de galões por dia, MTA). Depois, corte de um pilar de concreto armado: uma rachadura, a água entra, a barra de aço fica laranja e "
              "incha, o concreto estoura de dentro para fora. Pontes e arranha-céus cedem um a um. Ao lado, um "
              "templo romano continua de pé.",
         text=
        "{a0}Algumas coisas começam a mudar logo. [p=0.2] Embaixo de Nova York, [p=0.1] as bombas do metrô tiram "
        "todo dia [p=0.1] uns *cinquenta milhões de litros* de água [p=0.1] que vaza pelas paredes dos túneis. [p=0.2] "
        "Sem ninguém para cuidar das bombas, [p=0.1] os túneis começam a encher. [p=0.3] "
        "{a}Nos primeiros cem anos, [p=0.1] cai primeiro o que parecia mais forte: [p=0.2] o *concreto armado.* "
        "[p=0.3] {b}Dentro dele há barras de aço. [p=0.1] Quando a água entra por uma rachadura, [p=0.1] o aço "
        "enferruja, [p=0.2] {c}e a ferrugem ocupa *mais espaço* do que o aço ocupava. [p=0.2] "
        "Ela empurra o concreto de dentro para fora, [p=0.1] até ele se partir. [p=0.3] "
        "{d}Pontes, [p=0.1] viadutos [p=0.1] e arranha-céus vão cedendo, [p=0.1] um por um. [p=0.3] "
        "{e}Enquanto isso, [p=0.1] construções romanas de concreto, [p=0.1] *sem aço por dentro,* [p=0.1] "
        "continuam de pé há uns dois mil anos."),
    dict(id="07", block="mil_anos",
         tela="As cidades viram morros cobertos de floresta. Corte para o Ártico: uma montanha de neve com a "
              "entrada de uma mina; dentro, rolos de filme numa estante. Etiqueta: 'Projetado para ~1.000 anos'. "
              "Depois, a câmera desce para um aterro enorme sob a terra.",
         text=
        "{a}Com *mil anos,* [p=0.1] as cidades viraram morros cobertos de mato. [p=0.3] "
        "{b}Os Antigos até tentaram se proteger do esquecimento. [p=0.2] {c}Numa antiga mina de carvão no Ártico, "
        "[p=0.1] em Svalbard, [p=0.1] eles gravaram dados em *filme fotográfico,* [p=0.1] projetado para durar uns "
        "mil anos. [p=0.4] "
        "{d}Só que o que mais sobrevive de uma civilização [p=0.1] quase nunca é o que ela quis guardar. [p=0.3] "
        "{e}É o que ela *jogou fora.*"),
    dict(id="08", block="aterro",
         tela="Corte de um aterro sanitário em camadas. Arqueólogos do fim dos anos 1980, de capacete, perfuram o lixo e "
              "tiram um jornal amarelado, ainda legível, e um cachorro-quente inteiro. Legenda: Garbage Project · "
              "Universidade do Arizona.",
         text=
        "{a}E os Antigos jogavam fora de um jeito muito particular: [p=0.1] em *aterros,* [p=0.1] montanhas de lixo "
        "compactado e coberto de terra. [p=0.3] "
        "{b}No fim dos anos mil novecentos e oitenta, [p=0.1] um arqueólogo dos próprios Antigos, [p=0.1] William "
        "Rathje, [p=0.1] da Universidade do Arizona, [p=0.1] resolveu escavar esses aterros [p=0.1] como se fossem "
        "ruínas. [p=0.3] "
        "{c}Ele encontrou jornais de décadas antes [p=0.1] que ainda dava para ler. [p=0.2] "
        "{d}E cachorros-quentes enterrados havia uns quinze anos [p=0.1] que ainda tinham *cara de cachorro-quente.* "
        "[p=0.3] {e}Lá dentro é tão seco e apertado [p=0.1] que quase nada apodrece."),
    dict(id="09", block="ceramica",
         tela="Mesa de laboratório de 10.000 anos no futuro com cacos organizados e etiquetados: um pedaço de xícara, um "
              "azulejo, um caco de vaso sanitário. Ao lado, para comparar, cacos de potes neolíticos.",
         text=
        "{a}Os arqueólogos conhecem isso há muito tempo. [p=0.2] O achado mais comum em muitas escavações [p=0.1] não "
        "é ouro nem estátua. [p=0.3] {b}É *caco de cerâmica.* [p=0.3] "
        "{c}Barro cozido não apodrece como madeira [p=0.1] e não enferruja como metal. [p=0.2] E pote quebrado ninguém "
        "reaproveita: [p=0.1] vai direto para o lixo. [p=0.3] "
        "{d}Então, daqui a dez mil anos, [p=0.1] os Antigos vão ser lembrados por cacos de xícaras, [p=0.1] de azulejos "
        "[p=0.1] e de *privadas.* [p=0.3] {e}Muitas, [p=0.1] muitas privadas."),
    dict(id="10", block="dez_mil",
         tela="O relógio marca 10.000 ANOS. O Monte Rushmore no meio de uma floresta densa, os quatro rostos quase "
              "intactos, um passarinho pousado num nariz. Régua: '≈ 2,5 cm a cada 10.000 anos' (estimativa do Serviço "
              "de Parques dos EUA).",
         text=
        "{a}Com *dez mil anos,* [p=0.1] algumas coisas quase não mudaram. [p=0.3] "
        "{b}No monte Rushmore, [p=0.1] nos Estados Unidos, [p=0.1] os Antigos esculpiram no granito os rostos de quatro "
        "presidentes. [p=0.2] {c}Pela estimativa dos geólogos do parque, [p=0.1] a rocha perde só uns *dois centímetros "
        "e meio* [p=0.1] a cada dez mil anos. [p=0.3] "
        "{d}Os quatro rostos vão continuar lá, [p=0.1] sérios, [p=0.1] olhando para uma floresta [p=0.1] sem ninguém."),
    dict(id="11", block="plastico",
         tela="Montanha de plástico crescendo com contador '8,3 BILHÕES DE TONELADAS (até 2015)'. Gráfico de pizza do "
              "lixo: 79% aterros e natureza · 9% reciclado · resto queimado. O plástico se quebra em pedaços cada vez "
              "menores. Praia do Havaí: uma fogueira derrete plástico sobre areia, conchas e lava; vira uma pedra "
              "manchada. Rótulo: PLASTIGLOMERADO (2014). A pedra afunda em camadas de sedimento.",
         text=
        "{a}E o lixo deles também continua lá. [p=0.2] Só até dois mil e quinze, [p=0.1] eles tinham fabricado "
        "mais de *oito bilhões de toneladas de plástico.* [p=0.3] "
        "{b}Da parte que virou lixo, [p=0.1] *setenta e nove por cento* foi parar em aterros [p=0.1] ou na "
        "natureza. [p=0.3] "
        "{c}Plástico não apodrece como madeira. [p=0.1] Ele só se quebra em pedaços cada vez menores. [p=0.3] "
        "{d}E às vezes, [p=0.2] *vira pedra.* [p=0.3] "
        "{e}Em dois mil e catorze, [p=0.1] numa praia do Havaí, [p=0.1] geólogos descreveram uma rocha nova: "
        "[p=0.2] plástico derretido em fogueiras, [p=0.1] misturado com areia, [p=0.1] conchas [p=0.1] e pedaços de "
        "lava. [p=0.2] {f}Deram o nome de *plastiglomerado.* [p=0.3] "
        "{g}Ele é mais pesado que o plástico sozinho. [p=0.1] Afunda, [p=0.1] é enterrado [p=0.1] e pode entrar "
        "para o registro das rochas."),
    dict(id="12", block="frango",
         tela="Escavação de 10.000 anos no futuro: arqueólogos-robô limpam camadas e só encontram ossos de frango, "
              "milhares. Comparação de esqueletos: frango medieval pequeno × frango de corte enorme ('2× MAIOR'). "
              "Contador '≈ 23 BILHÕES VIVOS AO MESMO TEMPO'. Selo: A ERA DO FRANGO. Lume levanta a sobrancelha.",
         text=
        "{a}Agora, [p=0.1] um detalhe que sempre surpreende os visitantes. [p=0.3] "
        "{b}O fóssil mais comum dos Antigos [p=0.1] não é um osso humano. [p=0.4] {c}É um *osso de frango.* [p=0.4] "
        "{d}Em dois mil e dezoito, [p=0.1] pesquisadores britânicos mostraram que o frango criado pelos Antigos "
        "era um animal novo: [p=0.2] {e}pelo menos o *dobro do tamanho* do frango da Idade Média, [p=0.1] com "
        "esqueleto, [p=0.1] química dos ossos [p=0.1] e genética diferentes de todos os ancestrais. [p=0.3] "
        "{f}E havia cerca de *vinte e três bilhões* deles vivos ao mesmo tempo. [p=0.4] "
        "{g}Para um paleontólogo do futuro, [p=0.2] esta pode muito bem ser *a era do frango.*"),
    dict(id="13", block="plutonio",
         tela="Globo de 1950: cogumelos atômicos de testes em vários pontos; uma poeira dourada sobe, dá a volta no "
              "planeta e cai com a chuva. Corte de um lago: uma faixa fina e dourada no sedimento. Relógio de "
              "meia-vida: Pu-239 ≈ 24.100 ANOS. Pin no mapa: Lago Crawford, Canadá. Carimbo 'ANTROPOCENO?' e, em "
              "cima, 'REJEITADO · 2024'.",
         text=
        "{a}Mas existe uma marca que nenhum cientista do futuro vai deixar passar. [p=0.3] "
        "{b}A partir dos anos *mil novecentos e cinquenta,* [p=0.1] os testes de bombas atômicas espalharam "
        "*plutônio* pelo planeta inteiro. [p=0.2] {c}Ele caiu com a chuva [p=0.1] e assentou no fundo dos lagos e "
        "dos mares, [p=0.1] numa camada fina, [p=0.1] no mundo todo. [p=0.3] "
        "{d}O plutônio duzentos e trinta e nove leva uns *vinte e quatro mil anos* para perder metade da "
        "radioatividade. [p=0.2] {e}Dez mil anos depois, [p=0.1] a camada continua lá, [p=0.1] fácil de detectar. "
        "[p=0.3] "
        "{f}Num lago do Canadá, [p=0.1] o lago Crawford, [p=0.1] os geólogos dos Antigos chegaram a propor essa "
        "camada como o começo de uma nova época da Terra: [p=0.2] o *Antropoceno.* [p=0.3] "
        "{g}Em dois mil e vinte e quatro, [p=0.1] a proposta foi rejeitada. [p=0.3] "
        "Os Antigos não conseguiam concordar nem sobre isso."),
    dict(id="14", block="ar",
         tela="Antártida: um cilindro de gelo sai de uma perfuração; close nas bolhas de ar presas dentro. Gráfico "
              "subindo: ~280 ppm antes da indústria → 430,5 ppm (pico de maio de 2025, Mauna Loa, NOAA). A curva fica "
              "quase vertical no fim.",
         text=
        "{a}E tem uma marca ainda mais discreta: [p=0.2] *o ar.* [p=0.3] "
        "{b}Na Antártida, [p=0.1] cada camada de neve que vira gelo [p=0.1] prende bolhinhas do ar daquela época. "
        "[p=0.3] {c}Antes das fábricas, [p=0.1] o ar tinha cerca de *duzentas e oitenta* partes por milhão de gás "
        "carbônico. [p=0.2] {d}Em maio de dois mil e vinte e cinco, [p=0.1] o pico passou de *quatrocentas e trinta.* "
        "[p=0.3] {e}Quem perfurar o gelo desta época [p=0.1] vai encontrar, [p=0.1] presa em bolhas, [p=0.1] a "
        "respiração de uma civilização com pressa."),
    dict(id="15", block="aviso",
         tela="Corte do subsolo da Finlândia: túneis a centenas de metros de profundidade, cápsulas de cobre "
              "descendo. Rótulo: ONKALO · licença em out/2026. Depois, um deserto do Novo México com espinhos de "
              "pedra gigantes (o 'Landscape of Thorns' dos estudos de marcadores) e uma placa onde surgem as frases "
              "do aviso, em várias línguas e em pictogramas.",
         text=
        "{a}E há uma mensagem que os Antigos escreveram *de propósito* para o futuro. [p=0.3] "
        "{b}Eles enterravam o lixo nuclear mais perigoso em túneis a centenas de metros de profundidade. [p=0.2] "
        "{c}Na Finlândia, [p=0.1] o primeiro depósito desse tipo, [p=0.1] chamado Onkalo, [p=0.1] recebeu licença "
        "para funcionar em *outubro de dois mil e vinte e seis.* [p=0.3] "
        "{d}Mas como avisar alguém, [p=0.1] daqui a milhares de anos, [p=0.1] para não cavar ali? [p=0.2] "
        "Nenhuma língua dura tanto. [p=0.3] "
        "{e}Nos Estados Unidos, [p=0.1] um relatório de mil novecentos e noventa e três [p=0.1] rascunhou o texto "
        "de um aviso assim. [p=0.2] {f}Ele começa desse jeito: [p=0.4] "
        "*Este lugar não é um lugar de honra.* [p=0.3] *Nada de valor está aqui.* [p=0.5] "
        "{g}É estranho e bonito ao mesmo tempo: [p=0.2] uma das primeiras cartas dos Antigos para o futuro [p=0.1] "
        "foi um pedido [p=0.2] para não chegar perto."),

    # ── O ABISMO ─────────────────────────────────────────────
    dict(id="16", block="abismo",
         tela="O relógio dispara: 1.000.000 DE ANOS. Corte geológico: a cidade inteira vira uma faixa fina e escura "
              "entre camadas enormes de rocha. Retratos simples de Gavin Schmidt (NASA) e Adam Frank. Pergunta na "
              "tela: 'Daria para perceber?'. A faixa da nossa época fica lado a lado com faixas de eventos naturais "
              "antigos, quase iguais.",
         text=
        "{a}Agora vamos mais longe. [p=0.2] *Um milhão de anos.* [p=0.4] "
        "{b}As cidades viraram uma camada de entulho prensado. [p=0.1] O plástico virou uma lâmina escura entre as "
        "rochas. [p=0.3] "
        "{c}Em dois mil e dezoito, [p=0.1] dois cientistas, [p=0.1] Gavin Schmidt, [p=0.1] da NASA, [p=0.1] e Adam "
        "Frank, [p=0.2] fizeram uma pergunta incômoda: [p=0.2] {d}se uma civilização industrial tivesse existido "
        "na Terra há milhões de anos, [p=0.1] nós conseguiríamos perceber? [p=0.4] "
        "{e}A resposta deles: [p=0.2] *não seria fácil.* [p=0.3] "
        "{f}Com tempo suficiente, [p=0.1] uma civilização inteira pode virar só uma faixa estranha na rocha: "
        "[p=0.2] uma mudança no carbono, [p=0.1] restos de plástico, [p=0.1] elementos raros, [p=0.2] "
        "{g}que de longe se parece com outras mudanças naturais do passado da Terra. [p=0.5] "
        "{h}Oito bilhões de pessoas. [p=0.3] Um século de pressa. [p=0.3] E no fim, [p=0.2] *uma faixa fina de "
        "rocha diferente.*"),
    dict(id="17", block="longe",
         tela="A câmera sobe da Terra para a Lua: pegadas de bota nítidas na poeira, sem vento. Satélites apagados girando bem acima do equador ('órbita cemitério'). Depois, uma sonda "
              "Voyager se afasta com o Disco de Ouro brilhando ('feito para ~1 bilhão de anos'). Por fim, a Terra "
              "pequena, cercada por uma bolha transparente de ondas de rádio ('> 100 anos-luz').",
         text=
        "{a}Os rastros mais nítidos dos Antigos [p=0.1] vão estar longe daqui. [p=0.3] "
        "{b}Na Lua, [p=0.1] onde não existe vento nem chuva, [p=0.1] as *pegadas dos astronautas* podem durar "
        "milhões de anos. [p=0.3] "
        "{c}A uns trinta e seis mil quilômetros de altura, [p=0.1] satélites mortos, [p=0.1] empurrados para uma órbita "
        "chamada *cemitério,* [p=0.1] podem ficar girando por milhões de anos. [p=0.3] "
        "{d}Duas sondas, [p=0.1] as Voyager, [p=0.1] levam um *disco de ouro* com sons e imagens da Terra, [p=0.1] "
        "feito para durar cerca de *um bilhão de anos* entre as estrelas. [p=0.3] "
        "{e}E as transmissões de rádio dos Antigos [p=0.1] já formam uma bolha em volta da Terra [p=0.1] com mais "
        "de *cem anos-luz* de raio."),

    # ── A VIRADA ─────────────────────────────────────────────
    dict(id="18", block="virada",
         tela="Volta ao corte geológico, agora em close na faixa da nossa época, que vira uma página em branco. "
              "Três controles deslizantes: PLÁSTICO · CARBONO · BOMBAS. Mãos do século 21 começam a mexer neles. "
              "Cenas reais e simples: um rolo de filme guardado, uma cápsula de cobre descendo no túnel, cientistas "
              "medindo o sedimento. (A ideia de 'escolher a camada' é a mensagem do vídeo)",
         text=
        "{a}Só que tem uma coisa que os Antigos demoraram a perceber. [p=0.4] "
        "{b}A camada que eles iam deixar [p=0.2] *ainda não estava escrita.* [p=0.4] "
        "{c}Toda camada de rocha é só um registro de escolhas. [p=0.2] {d}Mais plástico [p=0.1] ou menos. [p=0.2] "
        "Mais carbono [p=0.1] ou menos. [p=0.2] Mais bombas [p=0.1] ou menos. [p=0.4] "
        "{e}E eles começaram a escolher. [p=0.2] "
        "{e2}Quando descobriram que um gás das geladeiras e dos sprays estava abrindo um buraco na camada de "
        "ozônio, [p=0.1] eles assinaram um acordo, [p=0.1] o *Protocolo de Montreal,* [p=0.1] em mil novecentos e "
        "oitenta e sete. [p=0.2] E a camada começou a se recuperar. [p=0.3] "
        "{f}Gravaram arquivos para durar séculos. [p=0.2] Enterraram o lixo "
        "mais perigoso bem fundo, [p=0.1] com avisos para quem viesse depois. [p=0.2] {g}E passaram a medir o que "
        "estavam deixando no chão, [p=0.2] justamente para poder mudar."),
    dict(id="19", block="virada",
         tela="A Lume volta para o salão e olha a vitrine da Peça Nº 001 com carinho. O holofote âmbar esquenta. "
              "(FICÇÃO: o olhar do museu)",
         text=
        "{a}Os Antigos eram brilhantes [p=0.1] e completamente perdidos [p=0.1] ao mesmo tempo. [p=0.4] "
        "{b}Mas foram a primeira civilização que *sabia* que estava virando rocha. [p=0.4] "
        "{c}E isso deu a eles uma chance que nenhum povo antes teve: [p=0.3] *decidir o que ia sobrar.*"),

    # ── A ETIQUETA ───────────────────────────────────────────
    dict(id="20", block="etiqueta",
         tela="A Lume fecha a vitrine. Close na etiqueta de museu, escrita à máquina, linha por linha: PEÇA Nº 001 · "
              "Retângulo de vidro e metal · Século 21 d.C. · a frase final. (FICÇÃO)",
         text=
        "{a}Então, [p=0.1] vamos à etiqueta da *peça número um.* [p=0.3] "
        "{b}Retângulo de vidro e metal. [p=0.2] Século vinte e um. [p=0.4] "
        "{c}*Os Antigos guardavam o mundo inteiro aqui dentro.* [p=0.3] *Não sobrou nada aqui dentro.* [p=0.3] "
        "{d}*Sobrou o que eles fizeram lá fora.*"),
    dict(id="21", block="proxima",
         tela="A Lume caminha até a próxima vitrine, coberta por um pano. Por baixo, a silhueta de um celular "
              "brilhando. Texto: PRÓXIMA PEÇA · Nº 002. Pergunta na tela: 'Que objeto da sua casa deveria entrar no "
              "museu?'",
         text=
        "{a}Na próxima vitrine: [p=0.2] por que os Antigos passavam horas por dia [p=0.1] encarando retângulos "
        "brilhantes. [p=0.4] "
        "{b}E você? [p=0.2] Que objeto da sua casa deveria entrar no museu? [p=0.2] {c}Escreve aqui nos "
        "comentários. [p=0.2] Eu leio todos."),
]
