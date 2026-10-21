# Roteiro — Matéria, Substâncias e Misturas, Episódio 1: O que é matéria e o que é substância pura (aula para iniciantes)
# Base: Estudos/Enem/estudos/02-quimica/01-materia-substancias-misturas.html — seção 02 (1ª parte), seção 03 + Questão 3 da seção 12
# Fora do recorte: ponto de fusão/ebulição em detalhe (ep. 5), modelos atômicos (série própria), alotropia (ep. 2).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora:
#   LEGO: átomo = peça · elemento químico = COR da peça · molécula = montagem · simples = uma cor só · composta = cores diferentes.
#   NARIZ × IMPRESSÃO DIGITAL: propriedade geral (todo mundo tem) × específica (identifica).
# Ritual de classificação (sempre igual na tela): olhe a fórmula → conte as LETRAS (maiúsculas) → uma: simples · duas ou mais: composta.
# Frases-chave (meio e fim, idênticas):
#   1. Matéria é tudo que tem massa e ocupa espaço.
#   2. Conte as letras, não os números.
#   3. Uma letra: simples. Duas ou mais: composta.
# Cores: azul = definição · roxo = regra · amarelo = armadilha · verde = atalho/dica · vermelho = erro.
# Fórmulas escritas como se leem ("O dois", "H dois O", "F e", "N a C l"); na tela aparecem como O₂, H₂O, Fe, NaCl.

TITULO = "O₂ tem 2 átomos e não é composta? Matéria e substância simples × composta do zero — Química ENEM, episódio 1"

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}O gás oxigênio, [p=0.2] aquele do cilindro do hospital, [p=0.2] tem *dois* átomos. [p=0.4] {b}O enxofre tem *oito.* [p=0.4] "
        "{c}A água tem *três.* [p=0.5] {d}Mesmo assim, [p=0.2] só a água é chamada de *composta.* [p=0.4] {e}Por quê? [p=0.5] "
        "{f}E se você nem sabe o que é átomo, [p=0.2] calma: [p=0.2] é a primeira coisa que eu vou explicar."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai olhar para *qualquer* fórmula química [p=0.2] {b}e dizer, em *dois segundos,* "
        "[p=0.2] se a substância é simples ou composta. [p=0.4] {c}Sem decorar lista nenhuma."),

    # ================= PRÉ-REQUISITOS (até 45 s) =================
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembranças rápidas. [p=0.3] {a}Primeira: [p=0.2] tudo o que existe é feito de pecinhas pequenas demais para ver, "
        "[p=0.2] chamadas *átomos.* [p=0.4] {b}Pense nelas como *peças de LEGO.*"),
    dict(id="04", block="prereq", text=
        "{t}Segunda: [p=0.2] existem tipos diferentes de átomo. [p=0.3] {a}Cada tipo é um *elemento químico:* [p=0.2] oxigênio, "
        "[p=0.2] hidrogênio, [p=0.2] ferro. [p=0.4] {b}No LEGO, [p=0.2] o elemento é a *cor* da peça. [p=0.4] "
        "{c}E cada elemento tem um *símbolo:* [p=0.2] O, de oxigênio. [p=0.2] H, de hidrogênio."),
    dict(id="05", block="prereq", text=
        "{t}Terceira: [p=0.2] a *fórmula química* é a etiqueta que diz quais peças formam um material. [p=0.4] {a}H dois O: [p=0.2] a água. "
        "[p=0.4] {b}O número pequeno, embaixo, [p=0.2] se chama *índice:* [p=0.2] ele conta as peças daquela cor. [p=0.2] Dois hidrogênios. "
        "[p=0.4] {c}Sem número, [p=0.2] é uma peça só: [p=0.2] um oxigênio. [p=0.4] {d}As *letras* dizem as cores. [p=0.2] Os *números* contam as peças."),

    # ================= BLOCO A: MATÉRIA =================
    dict(id="06", block="materia", text=
        "{t}Primeira pergunta: [p=0.2] o que é *matéria?* [p=0.4] {a}Pegue um copo d'água. [p=0.3] {b}Coloque numa balança: [p=0.2] "
        "o ponteiro se mexe. [p=0.3] A água tem *massa,* [p=0.2] que é a quantidade de matéria, [p=0.2] o que a balança mede. [p=0.4] "
        "{c}E a água ocupa um lugar dentro do copo: [p=0.2] onde ela está, [p=0.2] não cabe outra coisa. [p=0.5] "
        "{d}Então, [p=0.2] *matéria é tudo que tem massa e ocupa espaço.*"),
    dict(id="07", block="materia_nao", text=
        "{t}E o que *não* é matéria? [p=0.4] {a}A *luz* da lanterna. [p=0.3] {b}O *som* da música. [p=0.3] {c}O *calor* do fogão. [p=0.4] "
        "{d}Você não pesa a luz numa balança, [p=0.2] nem guarda o som num pote. [p=0.3] Eles não têm massa: [p=0.2] *não são matéria.* [p=0.5] "
        "{e}Já o ar, [p=0.2] mesmo invisível, [p=0.2] é matéria: [p=0.2] ele enche a bexiga e ocupa o espaço dentro dela."),

    # ================= BLOCO B: PROPRIEDADES =================
    dict(id="08", block="prop_gerais", text=
        "{t}E como saber *qual* material está na sua frente? [p=0.4] {a}Toda matéria tem características, [p=0.2] "
        "que a química chama de *propriedades.* [p=0.4] {b}Algumas valem para *tudo:* [p=0.2] a massa, [p=0.2] e o volume, "
        "[p=0.2] que é o espaço ocupado. [p=0.4] {c}Um prego tem massa. [p=0.2] A água tem massa. [p=0.2] O ar tem massa. [p=0.4] "
        "{d}Por isso, saber que algo tem massa [p=0.2] não diz *o que* ele é. [p=0.3] {e}Essas são as propriedades *gerais.*"),
    dict(id="09", block="prop_especificas", text=
        "{t}Outras propriedades mudam de um material para outro. [p=0.4] {a}A temperatura em que ele derrete: [p=0.2] o *ponto de fusão.* "
        "[p=0.3] {b}A temperatura em que ele ferve: [p=0.2] o *ponto de ebulição.* [p=0.3] {c}E a *densidade:* [p=0.2] "
        "quanto pesa um mesmo volume do material. [p=0.4] {d}A água pura ferve a cem graus, [p=0.2] ao nível do mar. [p=0.3] "
        "O álcool, a setenta e oito. [p=0.4] {e}Essas são as propriedades *específicas.*"),
    dict(id="10", block="prop_digital", text=
        "{t}Pense assim: [p=0.2] *todo mundo tem nariz.* [p=0.3] {a}Ter nariz não identifica ninguém: [p=0.2] é *geral.* [p=0.4] "
        "{b}Mas a sua *impressão digital* [p=0.2] só você tem: [p=0.2] é *específica.* [p=0.4] {c}As propriedades específicas "
        "[p=0.2] são a impressão digital do material. [p=0.3] {d}São elas que *identificam* o que ele é."),

    # ================= BLOCO C: SUBSTÂNCIA PURA =================
    dict(id="11", block="molecula", text=
        "{t}E o que é uma *substância?* [p=0.4] {a}Volte ao LEGO. [p=0.3] Peças encaixadas formam uma montagem. [p=0.3] "
        "{b}Na química, [p=0.2] essa montagem se chama *molécula.* [p=0.4] {c}Um copo de água pura [p=0.2] tem bilhões de montagens, "
        "[p=0.2] {d}e todas *iguais:* [p=0.2] duas peças de hidrogênio [p=0.2] e uma de oxigênio."),
    dict(id="12", block="pura", text=
        "{t}Agora, [p=0.2] água com sal misturado. [p=0.4] {a}Lá dentro tem montagens de água [p=0.2] e também pedaços de sal. "
        "[p=0.3] *Dois* tipos. [p=0.4] {b}Quando o material tem *um único tipo* de montagem, [p=0.2] ele é uma *substância pura.* [p=0.4] "
        "{c}Quando tem dois tipos ou mais, [p=0.2] é uma *mistura.* [p=0.4] {d}Hoje, o foco são as substâncias puras. [p=0.2] "
        "As misturas vão ganhar episódio próprio."),

    # ================= BLOCO D: SUBSTÂNCIA SIMPLES =================
    dict(id="13", block="simples", text=
        "{t}E as substâncias puras se dividem em dois grupos. [p=0.4] {a}Pense no gás do cilindro de oxigênio do hospital. "
        "[p=0.3] {b}Fórmula: [p=0.2] O dois. [p=0.3] {c}Duas peças, [p=0.2] as duas vermelhas. [p=0.2] *Uma cor só.* [p=0.5] "
        "{d}Montagem com uma cor só, [p=0.2] não importa quantas peças: [p=0.2] *substância simples.*"),
    dict(id="14", block="simples_ex", text=
        "{t}Mais exemplos. [p=0.3] {a}O ozônio, [p=0.2] O três: [p=0.2] três peças, uma cor. [p=0.3] {b}O nitrogênio do ar, [p=0.2] N dois. "
        "[p=0.3] {c}O enxofre, [p=0.2] S oito: [p=0.2] oito peças, [p=0.2] e ainda uma cor só. [p=0.3] {d}O hélio do balão de festa: "
        "[p=0.2] uma peça sozinha. [p=0.3] {e}E o ferro do prego. [p=0.4] {f}Todas *simples:* [p=0.2] um único elemento."),
    dict(id="15", block="maiuscula", text=
        "{t}Mas repare no símbolo do ferro: [p=0.2] F e. [p=0.3] F maiúsculo, [p=0.2] e minúsculo. [p=0.4] {a}São duas letras, "
        "[p=0.2] mas *um elemento só.* [p=0.4] {b}Muitos símbolos têm uma segunda letra, [p=0.2] e ela é sempre *minúscula.* [p=0.4] "
        "{c}Então, o atalho: [p=0.2] cada letra *maiúscula* começa um elemento novo. [p=0.3] {d}Quando eu disser *conte as letras,* "
        "[p=0.2] conte as maiúsculas."),

    # ================= BLOCO E: SUBSTÂNCIA COMPOSTA =================
    dict(id="16", block="composta", text=
        "{t}E quando a montagem usa cores *diferentes?* [p=0.4] {a}A água: [p=0.2] H dois O. [p=0.3] Duas peças brancas [p=0.2] e uma vermelha. "
        "[p=0.2] *Duas cores.* [p=0.4] {b}O gás carbônico, [p=0.2] que sai da sua respiração: [p=0.2] C O dois. [p=0.2] Carbono e oxigênio. "
        "[p=0.4] {c}Montagem com duas cores ou mais: [p=0.2] *substância composta.*"),
    dict(id="17", block="composta_ex", text=
        "{t}Mais dois. [p=0.3] {a}O sal de cozinha: [p=0.2] N a C l. [p=0.3] Duas maiúsculas: [p=0.2] sódio e cloro. [p=0.4] "
        "{b}No sal, [p=0.2] as peças não formam montagens pequenas: [p=0.2] formam um bloco enorme, todo encaixado. [p=0.3] "
        "Mas as cores se contam do mesmo jeito. [p=0.4] {c}E a glicose, [p=0.2] o açúcar da uva: [p=0.2] C seis, H doze, O seis. "
        "[p=0.3] Vinte e quatro peças, [p=0.2] *três* cores. [p=0.4] {d}Todas *compostas.*"),

    # ================= BLOCO F: O CRITÉRIO =================
    dict(id="18", block="ritual", text=
        "{t}Agora, o ritual para classificar qualquer fórmula. [p=0.4] {a}Um: [p=0.2] olhe a fórmula. [p=0.3] {b}Dois: [p=0.2] "
        "conte as *letras,* [p=0.2] que são os elementos. [p=0.2] *Não* os números. [p=0.4] {c}Três: [p=0.2] uma letra, [p=0.2] *simples.* "
        "[p=0.2] Duas ou mais, [p=0.2] *composta.*"),
    dict(id="19", block="ritual_gancho", text=
        "{t}Testando no gancho do começo. [p=0.3] {a}O dois: [p=0.2] uma letra. [p=0.2] Simples. [p=0.3] {b}S oito: [p=0.2] uma letra. "
        "[p=0.2] Simples. [p=0.3] {c}H dois O: [p=0.2] duas letras. [p=0.2] Composta. [p=0.4] {d}O número de peças não importa. [p=0.2] "
        "O critério é o número de *elementos,* [p=0.2] nunca o número de átomos."),

    # ================= BLOCO G: COMO SE SEPARA =================
    dict(id="20", block="separar", text=
        "{t}E dá para separar um material em partes mais simples? [p=0.4] {a}Uma mistura, sim, [p=0.2] e sem desmontar nada: "
        "[p=0.2] por *processos físicos,* [p=0.2] como filtrar ou destilar. [p=0.4] {b}Uma substância composta, [p=0.2] só desmontando as peças: "
        "[p=0.2] por um *processo químico.* [p=0.4] {c}Por exemplo, a *eletrólise:* [p=0.2] passar corrente elétrica pela água "
        "[p=0.2] para quebrá-la em hidrogênio e oxigênio. [p=0.4] {d}E a substância simples? [p=0.2] Já tem uma cor só. [p=0.2] "
        "Não se separa em nada mais simples."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="21", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] matéria é tudo que tem massa e ocupa espaço. [p=0.5] "
        "{b}Dois: [p=0.2] conte as letras, não os números. [p=0.5] {c}Três: [p=0.2] uma letra: simples. [p=0.2] Duas ou mais: composta."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erro1", text=
        "{t}Agora, os três erros que mais derrubam gente. [p=0.4] {a}Primeiro: [p=0.2] O dois é composta. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque tem dois átomos, [p=0.2] e composto lembra coisa com mais de uma parte. [p=0.4] {c}Mas as duas peças têm a mesma cor. "
        "[p=0.2] Uma letra: [p=0.2] *simples.*"),
    dict(id="23", block="erro2", text=
        "{a}Segundo: [p=0.2] substância simples é um átomo sozinho. [p=0.4] {b}Parece certo, [p=0.2] porque simples lembra pequeno, "
        "[p=0.2] uma coisa só. [p=0.4] {c}Mas o enxofre, S oito, [p=0.2] tem oito átomos [p=0.2] e é simples. [p=0.3] "
        "Simples quer dizer *um elemento,* [p=0.2] não uma peça."),
    dict(id="24", block="erro3", text=
        "{a}Terceiro: [p=0.2] usar massa ou volume para identificar um material. [p=0.4] {b}Parece certo, [p=0.2] porque são as medidas "
        "que a gente mais conhece. [p=0.4] {c}Mas um quilo de ferro e um quilo de algodão [p=0.2] têm a mesma massa. [p=0.3] "
        "Massa e volume são *gerais.* [p=0.3] Para identificar, [p=0.2] use as *específicas:* [p=0.2] a impressão digital."),

    # ================= EXERCÍCIO RÁPIDO =================
    dict(id="25", block="exercicio", text=
        "{t}Sua vez. [p=0.3] Classifique estas quatro. [p=0.4] {a}H dois. [p=0.3] {b}C H quatro, [p=0.2] o metano, do gás natural. "
        "[p=0.3] {c}O três. [p=0.3] {d}N a C l. [p=0.4] {p}*Pause o vídeo e classifique.* [p=1.5]"),
    dict(id="26", block="exercicio", text=
        "{t}Conferindo. [p=0.3] {a}H dois: [p=0.2] uma letra. [p=0.2] *Simples.* [p=0.3] {b}C H quatro: [p=0.2] C e H, duas letras. "
        "[p=0.2] *Composta.* [p=0.3] {c}O três: [p=0.2] uma letra. [p=0.2] *Simples.* [p=0.3] {d}N a C l: [p=0.2] duas maiúsculas. "
        "[p=0.2] *Composta.*"),

    # ================= QUESTÃO 3 =================
    dict(id="27", block="questao", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.4] {e1}Considere as seguintes espécies químicas, [p=0.2] ou seja, estas sete fórmulas: "
        "[p=0.4] {e2}O dois, [p=0.2] O três, [p=0.2] H dois O, [p=0.2] N a C l, [p=0.2] N dois, [p=0.2] C O dois [p=0.2] e F e. [p=0.4] "
        "{e3}O número de substâncias simples nessa lista é:"),
    dict(id="28", block="questao", text=
        "{a}A: [p=0.2] dois. [p=0.3] {b}B: [p=0.2] três. [p=0.3] {c}C: [p=0.2] quatro. [p=0.3] {d}D: [p=0.2] cinco. [p=0.3] "
        "{e}E: [p=0.2] sete. [p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="29", block="questao", text=
        "{t}Vamos com o ritual, [p=0.2] uma por uma. [p=0.3] {s1}O dois: [p=0.2] uma letra. [p=0.2] Simples. [p=0.3] {s2}O três: "
        "[p=0.2] uma letra. [p=0.2] Simples. [p=0.3] {s3}H dois O: [p=0.2] duas. [p=0.2] Composta. [p=0.3] {s4}N a C l: [p=0.2] duas. "
        "[p=0.2] Composta."),
    dict(id="30", block="questao", text=
        "{s5}N dois: [p=0.2] uma. [p=0.2] Simples. [p=0.3] {s6}C O dois: [p=0.2] duas. [p=0.2] Composta. [p=0.3] {s7}F e: [p=0.2] "
        "uma maiúscula só. [p=0.2] Simples. [p=0.4] {r}*Quatro* simples: [p=0.2] O dois, O três, N dois e o ferro. [p=0.3] {ok}*Letra C.*"),
    dict(id="31", block="questao", text=
        "{t}E por que tanta gente marca a letra A, dois? [p=0.4] {a}Porque elimina o O dois e o N dois [p=0.2] por terem *dois átomos.* "
        "[p=0.3] Contou peças, [p=0.2] e não cores. [p=0.4] {b}A letra B, três, [p=0.2] vem de quem conta as duas letras do ferro "
        "[p=0.2] como dois elementos. [p=0.4] {e}A E, sete, [p=0.2] é de quem confunde pura com simples: [p=0.2] as sete são puras, "
        "[p=0.2] mas só quatro são simples. [p=0.4] {d}E a D, cinco, [p=0.2] não sai de nenhuma regra."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="32", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] matéria é tudo que tem massa e ocupa espaço. [p=0.5] "
        "{b}Dois: [p=0.2] conte as letras, não os números. [p=0.5] {c}Três: [p=0.2] uma letra: simples. [p=0.2] Duas ou mais: composta."),

    # ================= PONTE =================
    dict(id="33", block="ponte", text=
        "{t}E se o *mesmo* elemento [p=0.2] pudesse formar substâncias completamente diferentes? [p=0.5] {a}O grafite do seu lápis "
        "[p=0.2] e um diamante [p=0.2] são feitos da mesma coisa. [p=0.5] {b}No próximo episódio: [p=0.2] *alotropia.*"),
    dict(id="34", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Química do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] antes desta aula, você achava que O dois era composta? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
