# Roteiro — Matéria, Substâncias e Misturas, Episódio 6: Revisão geral, roteiro de prova e treino (aula de revisão)
# Base: Estudos/Enem/estudos/02-quimica/01-materia-substancias-misturas.html — seções 01, 10, 11 e 13
# NÃO reutiliza as Questões 1 a 9 da seção 12: as 5 questões abaixo são inéditas.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Âncoras retomadas: LEGO e cores (ep. 1) · mesmas peças, montagens diferentes: trepa-trepa × baralho (ep. 2)
#   · água com açúcar × salada de frutas (ep. 3) · a foto e a receita (ep. 4) · cabines de pedágio (ep. 5)
# Questões inéditas (gabarito): 1 B · 2 E · 3 A · 4 D · 5 C
#   Q3: copo com água, 2 cubos de gelo, sal dissolvido e areia → fases: gelo, água salgada, areia (3);
#       componentes: água, sal, areia (3).
#   Q5: −20 °C · bromo (PF −7, PE 59) sólido · cloro (−101, −34) gás · mercúrio (−39, 357) líquido ·
#       etanol (−114, 78) líquido · água (0, 100) sólida → só mercúrio e etanol.
# Cores: azul = definição · roxo = regra · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão: matéria, substâncias e misturas em 1 vídeo — Química ENEM, episódio 6"

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Este é o primeiro assunto de Química, [p=0.2] e ele monta o vocabulário de todo o resto. [p=0.4] "
        "{b}Hoje, você vai sair com um *roteiro de três perguntas* [p=0.2] que classifica qualquer material da prova."),

    # ================= COMO O ENEM COBRA =================
    dict(id="02", block="enem", text=
        "{t}Como esse assunto aparece no ENEM? [p=0.4] {a}Em primeiro lugar, [p=0.2] a *curva de aquecimento:* [p=0.2] o item mais cobrado. "
        "[p=0.4] {b}Depois, a contagem de fases e componentes. [p=0.3] {c}A classificação de materiais do dia a dia: [p=0.2] "
        "ar, água mineral, aço, leite. [p=0.3] {d}A alotropia do carbono, [p=0.2] em textos de nanotecnologia. [p=0.3] "
        "{e}E tabelas de ponto de fusão e de ebulição."),

    # ================= O ROTEIRO DE 3 PERGUNTAS =================
    dict(id="03", block="roteiro", text=
        "{t}Agora, o roteiro. [p=0.3] {a}Pergunta um: [p=0.2] tem *uma* substância ou mais de uma? [p=0.4] {b}Lembra do LEGO: "
        "[p=0.2] um tipo só de montagem [p=0.2] é *substância pura.* [p=0.3] Dois tipos ou mais: [p=0.2] *mistura.*"),
    dict(id="04", block="roteiro", text=
        "{a}Pergunta dois, se for pura: [p=0.2] um elemento ou mais? [p=0.3] Uma cor de peça só: [p=0.2] *simples.* [p=0.2] "
        "Duas cores ou mais: [p=0.2] *composta.* [p=0.5] {b}Pergunta três, se for mistura: [p=0.2] quantas fases? [p=0.3] "
        "Uma, como a água com açúcar: [p=0.2] *homogênea.* [p=0.3] Duas ou mais, como a salada de frutas: [p=0.2] *heterogênea.*"),
    dict(id="05", block="roteiro", text=
        "{t}Teste com quatro materiais: [p=0.2] {m}água destilada, [p=0.2] ar, [p=0.2] granito [p=0.2] e ozônio. [p=0.4] "
        "{p}*Pause e passe cada um pelo roteiro.* [p=2.0]"),
    dict(id="06", block="roteiro", text=
        "{a}Água destilada: [p=0.2] uma substância só, [p=0.2] H dois O. [p=0.2] Pura. [p=0.2] Duas cores: [p=0.2] *composta.* [p=0.4] "
        "{b}Ar: [p=0.2] vários gases, [p=0.2] mistura. [p=0.2] Gases nunca formam camadas: [p=0.2] *homogênea.* [p=0.4] "
        "{c}Granito: [p=0.2] três minerais, [p=0.2] mistura. [p=0.2] Três fases que você vê: [p=0.2] *heterogênea.* [p=0.4] "
        "{d}Ozônio: [p=0.2] só O três. [p=0.2] Pura, [p=0.2] uma cor: [p=0.2] *simples.*"),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="07", block="vf", text=
        "{t}Agora, verdadeiro ou falso. [p=0.3] Nove afirmações. [p=0.3] {a}Em cada uma, [p=0.2] pause e responda [p=0.2] "
        "antes de eu falar."),
    dict(id="08", block="vf", text=
        "{a}Um: [p=0.2] O dois é substância composta, [p=0.2] porque tem dois átomos. [p=0.3] {p}Pause. [p=2.0] {r}*Falso.* [p=0.3] "
        "{w}Engana porque dois átomos parece coisa composta. [p=0.3] {k}Mas conta-se cor, não peça: [p=0.2] um elemento, *simples.*"),
    dict(id="09", block="vf", text=
        "{a}Dois: [p=0.2] três cubos de gelo na água formam quatro fases. [p=0.3] {p}Pause. [p=2.0] {r}*Falso.* [p=0.3] "
        "{w}Engana porque a foto mostra três pedaços. [p=0.3] {k}Mas a mesma coisa, no mesmo estado, é uma fase só. [p=0.2] *Duas fases.*"),
    dict(id="10", block="vf", text=
        "{a}Três: [p=0.2] fases e componentes são sempre o mesmo número. [p=0.3] {p}Pause. [p=2.0] {r}*Falso.* [p=0.3] "
        "{w}Engana porque, em água e óleo, os dois dão dois. [p=0.3] {k}Mas a foto e a receita são contagens independentes: "
        "[p=0.2] *conte duas vezes.*"),
    dict(id="11", block="vf", text=
        "{a}Quatro: [p=0.2] temperatura constante numa mudança de estado prova que é puro. [p=0.3] {p}Pause. [p=2.0] {r}*Falso.* [p=0.3] "
        "{w}Engana porque o patamar é a marca da pureza. [p=0.3] {k}Mas eutéticas e azeotrópicas param numa cabine. "
        "[p=0.2] *Puro para nas duas.*"),
    dict(id="12", block="vf", text=
        "{a}Cinco: [p=0.2] o ar é substância pura. [p=0.3] {p}Pause. [p=2.0] {r}*Falso.* [p=0.3] {w}Engana porque ele é invisível e uniforme. "
        "[p=0.3] {k}Mas são vários gases: [p=0.2] *mistura homogênea.*"),
    dict(id="13", block="vf", text=
        "{a}Seis: [p=0.2] água mineral é substância pura. [p=0.3] {p}Pause. [p=2.0] {r}*Falso.* [p=0.3] {w}Engana porque é transparente "
        "e parece só água. [p=0.3] {k}Mas o rótulo mostra sais dissolvidos: [p=0.2] *mistura.* [p=0.2] Só a destilada se aproxima de pura."),
    dict(id="14", block="vf", text=
        "{a}Sete: [p=0.2] O dois e O três são a mesma substância. [p=0.3] {p}Pause. [p=2.0] {r}*Falso.* [p=0.3] {w}Engana porque "
        "os dois são oxigênio. [p=0.3] {k}Mas montagens diferentes [p=0.2] são *substâncias diferentes:* [p=0.2] alótropos."),
    dict(id="15", block="vf", text=
        "{a}Oito: [p=0.2] leite e sangue são misturas homogêneas. [p=0.3] {p}Pause. [p=2.0] {r}*Falso.* [p=0.3] {w}Engana porque "
        "a olho nu parecem uma coisa só. [p=0.3] {k}Mas no microscópio aparecem os pedaços: [p=0.2] *heterogêneas.*"),
    dict(id="16", block="vf", text=
        "{a}Nove: [p=0.2] a curva de aquecimento diz se a substância é simples ou composta. [p=0.3] {p}Pause. [p=2.0] {r}*Falso.* [p=0.3] "
        "{w}Engana porque ela já diz se é puro. [p=0.3] {k}Mas H dois O e O dois têm o mesmo tipo de curva: [p=0.2] *só a fórmula decide.*"),
    dict(id="17", block="vf_placar", text=
        "{t}Todas as nove eram falsas. [p=0.3] {a}Quantas você acertou? [p=0.4] {b}Cada erro aponta o episódio que vale rever."),

    # ================= QUESTÃO INÉDITA 1: CLASSIFICAÇÃO =================
    dict(id="18", block="q1", text=
        "{t}Agora, cinco questões novas, [p=0.2] no estilo do ENEM. [p=0.4] {e1}Primeira. [p=0.2] Considere: [p=0.2] um, água destilada. "
        "[p=0.2] Dois, o ar comprimido de um cilindro de mergulho. [p=0.2] Três, o aço inox de uma panela. [p=0.2] Quatro, água com óleo. "
        "[p=0.2] Cinco, leite. [p=0.3] {e2}São misturas homogêneas apenas: [p=0.3] {a}A: [p=0.2] um, dois e três. [p=0.2] {b}B: [p=0.2] "
        "dois e três. [p=0.2] {c}C: [p=0.2] dois, três e cinco. [p=0.2] {d}D: [p=0.2] três. [p=0.2] {e}E: [p=0.2] dois. [p=0.4] "
        "{p}*Pause e resolva.* [p=1.5]"),
    dict(id="19", block="q1", text=
        "{t}O roteiro. [p=0.3] {s}A água destilada é pura: [p=0.2] fica de fora. [p=0.3] O ar é mistura de gases: [p=0.2] homogênea. "
        "[p=0.3] O aço é liga: [p=0.2] homogênea. [p=0.3] Água com óleo e leite: [p=0.2] heterogêneas. [p=0.3] {ok}*Letra B.* [p=0.4] "
        "{xc}A C achou o leite homogêneo. [p=0.3] {xd}A D tratou o ar como puro. [p=0.3] {xe}A E, o aço como puro. [p=0.3] "
        "{xa}E a A colocou a água destilada entre as misturas."),

    # ================= QUESTÃO INÉDITA 2: SIMPLES × COMPOSTA E ALOTROPIA =================
    dict(id="20", block="q2", text=
        "{t}Segunda. [p=0.3] {e1}Um texto sobre nanotecnologia cita: [p=0.2] grafeno, [p=0.2] ozônio, [p=0.2] metano, C H quatro, "
        "[p=0.2] diamante [p=0.2] e gás nitrogênio, [p=0.2] N dois. [p=0.3] {e2}É correto afirmar: [p=0.3] {a}A: [p=0.2] o ozônio é composto, "
        "porque tem três átomos. [p=0.3] {b}B: [p=0.2] grafeno e diamante são a mesma substância. [p=0.3] {c}C: [p=0.2] grafeno e diamante "
        "diferem por causa de impurezas. [p=0.3] {d}D: [p=0.2] o metano é um alótropo do carbono. [p=0.3] {e}E: [p=0.2] grafeno e diamante "
        "são alótropos, [p=0.2] e só o metano, entre os cinco, é substância composta. [p=0.4] {p}*Pause e resolva.* [p=1.5]"),
    dict(id="21", block="q2", text=
        "{t}Conte as cores. [p=0.3] {s}Grafeno e diamante: [p=0.2] só carbono, [p=0.2] trepa-trepa contra baralho: [p=0.2] alótropos. "
        "[p=0.3] Ozônio e nitrogênio: [p=0.2] uma cor só. [p=0.3] Metano: [p=0.2] carbono e hidrogênio, [p=0.2] composta. [p=0.3] "
        "{ok}*Letra E.* [p=0.4] {xa}A A contou peças. [p=0.3] {xb}A B tratou alótropos como a mesma substância. [p=0.3] {xc}A C "
        "culpou impurezas. [p=0.3] {xd}E a D esqueceu que alótropo é substância *simples.*"),

    # ================= QUESTÃO INÉDITA 3: FASES E COMPONENTES =================
    dict(id="22", block="q3", text=
        "{t}Terceira. [p=0.3] {e1}Num copo há água, [p=0.2] dois cubos de gelo, [p=0.2] sal totalmente dissolvido [p=0.2] e areia no fundo. "
        "[p=0.3] {e2}Os números de fases e de componentes são: [p=0.3] {a}A: [p=0.2] três e três. [p=0.2] {b}B: [p=0.2] quatro e três. "
        "[p=0.2] {c}C: [p=0.2] três e quatro. [p=0.2] {d}D: [p=0.2] quatro e quatro. [p=0.2] {e}E: [p=0.2] três e dois. [p=0.4] "
        "{p}*Pause e resolva.* [p=1.5]"),
    dict(id="23", block="q3", text=
        "{t}A foto: [p=0.2] {f}gelo, [p=0.2] água salgada [p=0.2] e areia. [p=0.2] Três fases. [p=0.3] O sal dissolvido não aparece na foto. "
        "[p=0.4] {r}A receita: [p=0.2] água, [p=0.2] sal [p=0.2] e areia. [p=0.2] O gelo é água. [p=0.2] Três componentes. [p=0.3] "
        "{ok}*Letra A.* [p=0.4] {xb}A B contou cada cubo como uma fase. [p=0.3] {xc}A C contou o gelo como outro componente. [p=0.3] "
        "{xd}A D fez os dois erros. [p=0.3] {xe}E a E esqueceu o sal: [p=0.2] ele some da foto, [p=0.2] mas está na receita."),

    # ================= QUESTÃO INÉDITA 4: CURVA COM UM PATAMAR =================
    dict(id="24", block="q4", text=
        "{t}Quarta. [p=0.3] {e1}Um líquido desconhecido foi congelado e depois aquecido. [p=0.3] {e2}Na fusão, a temperatura subiu sem parar. "
        "[p=0.3] Na ebulição, ficou constante em setenta e oito graus. [p=0.3] {e3}Ele é: [p=0.3] {a}A: [p=0.2] substância pura. [p=0.2] "
        "{b}B: [p=0.2] mistura eutética. [p=0.2] {c}C: [p=0.2] mistura comum. [p=0.2] {d}D: [p=0.2] mistura azeotrópica. [p=0.2] "
        "{e}E: [p=0.2] substância composta. [p=0.4] {p}*Pause e resolva.* [p=1.5]"),
    dict(id="25", block="q4", text=
        "{t}O ritual. [p=0.3] {s}Um patamar só, [p=0.2] na ebulição. [p=0.2] Parou numa cabine, [p=0.2] a de ferver: [p=0.2] *azeotrópica.* "
        "[p=0.3] {ok}*Letra D.* [p=0.4] {xa}A A achou que um patamar prova pureza. [p=0.3] {xb}A B trocou os nomes: [p=0.2] eutética é na fusão. "
        "[p=0.3] {xc}A C esqueceu que há um patamar. [p=0.3] {xe}E a E pediu ao gráfico o que ele não diz."),

    # ================= QUESTÃO INÉDITA 5: ESTADO FÍSICO COM NEGATIVOS =================
    dict(id="26", block="q5", text=
        "{t}Última. [p=0.3] {e1}Pontos de fusão e de ebulição: [p=0.3] bromo, [p=0.2] menos sete e cinquenta e nove. [p=0.3] Cloro, "
        "[p=0.2] menos cento e um e menos trinta e quatro. [p=0.3] Mercúrio, [p=0.2] menos trinta e nove e trezentos e cinquenta e sete. "
        "[p=0.3] Etanol, [p=0.2] menos cento e catorze e setenta e oito. [p=0.3] Água, [p=0.2] zero e cem. [p=0.4] {e2}A menos vinte graus, "
        "[p=0.2] estão líquidos apenas: [p=0.3] {a}A: [p=0.2] etanol. [p=0.2] {b}B: [p=0.2] bromo, mercúrio e etanol. [p=0.2] {c}C: [p=0.2] "
        "mercúrio e etanol. [p=0.2] {d}D: [p=0.2] cloro, mercúrio e etanol. [p=0.2] {e}E: [p=0.2] mercúrio, etanol e água. [p=0.4] "
        "{p}*Pause e desenhe a régua.* [p=1.5]"),
    dict(id="27", block="q5", text=
        "{t}A régua. [p=0.3] {s1}Bromo: [p=0.2] menos vinte é mais frio que menos sete. [p=0.2] Sólido. [p=0.3] {s2}Cloro: [p=0.2] "
        "menos vinte é mais quente que menos trinta e quatro. [p=0.2] Gás. [p=0.3] {s3}Mercúrio e etanol: [p=0.2] líquidos. [p=0.3] "
        "{s4}Água: [p=0.2] abaixo de zero, [p=0.2] gelo. [p=0.3] {ok}*Letra C.* [p=0.4] {xb}A B e a D [p=0.2] erraram o sinal: [p=0.2] "
        "no bromo e no cloro. [p=0.3] {xa}A A esqueceu o mercúrio. [p=0.3] {xe}E a E esqueceu que a água congela."),

    # ================= CHECKLIST =================
    dict(id="28", block="checklist", text=
        "{t}Agora, o checklist. [p=0.3] Marque só o que você conseguiria explicar em voz alta para outra pessoa, [p=0.2] sem consultar nada. "
        "[p=0.4] {a}Distingo propriedades gerais de específicas. [p=0.2] Separo simples de composta pelos elementos. [p=0.3] "
        "{b}Explico alotropia, [p=0.2] com o oxigênio e o carbono. [p=0.3] {c}Classifico misturas pelas fases, [p=0.2] e sei que mistura de gases "
        "é homogênea. [p=0.2] Classifico ar, água mineral, ligas e granito. [p=0.3] {d}Conto fases e componentes separadamente. [p=0.3] "
        "{e}Uso PF e PE para achar o estado. [p=0.2] Leio a curva, [p=0.2] e distingo eutética de azeotrópica. [p=0.3] {f}E aplico o roteiro "
        "de três perguntas."),
    dict(id="29", block="checklist", text=
        "{t}O que você não marcou, [p=0.2] reveja o episódio certo. [p=0.3] {a}Propriedades e simples ou composta: [p=0.2] episódio um. [p=0.3] "
        "{b}Alotropia: [p=0.2] dois. [p=0.3] {c}Misturas: [p=0.2] três. [p=0.3] {d}Fases e componentes: [p=0.2] quatro. [p=0.3] "
        "{e}PF, PE e curva de aquecimento: [p=0.2] cinco."),

    # ================= META =================
    dict(id="30", block="meta", text=
        "{t}E a meta, [p=0.2] antes de considerar o assunto dominado: [p=0.3] {a}resolver *trinta* questões [p=0.2] e acertar pelo menos "
        "*vinte e uma.* [p=0.3] Setenta por cento. [p=0.4] {b}Comece pelas de curva de aquecimento e de contagem de fases: [p=0.2] "
        "juntas, [p=0.2] elas são a maior parte deste assunto na prova."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{t}Fechamos o primeiro assunto de Química. [p=0.4] {a}O próximo é *separação de misturas,* [p=0.2] a continuação direta: "
        "[p=0.3] {b}tudo o que você classificou aqui como mistura, [p=0.2] lá você aprende a separar."),
    dict(id="32", block="cta", text=
        "Se essa revisão te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Química do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantas das nove pegadinhas você acertou? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
