# Roteiro — Matéria, Substâncias e Misturas, Episódio 3: Misturas homogêneas e heterogêneas (aula para iniciantes)
# Base: Estudos/Enem/estudos/02-quimica/01-materia-substancias-misturas.html — seções 04 e 09 + Questão 7 da seção 12
# Fora do recorte: contar fases e componentes em detalhe (ep. 4) e métodos de separação (série própria).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: homogênea = ÁGUA COM AÇÚCAR (você vê UMA coisa só) · heterogênea = SALADA DE FRUTAS (você vê os pedaços)
#   · às vezes é preciso um MICROSCÓPIO para ver os pedaços (leite, sangue).
# Ritual (sempre igual): é uma substância só ou mais de uma? → se for mais de uma, quantas fases eu vejo (inclusive no microscópio)?
# Quadro de classificação (pura / homogênea / heterogênea) que se preenche ao longo do vídeo.
# Frases-chave (meio e fim, idênticas):
#   1. Uma fase: homogênea. Duas ou mais: heterogênea.
#   2. Mistura de gases é sempre homogênea.
#   3. Liga metálica é mistura, não substância pura.
# Cores: azul = definição · roxo = regra · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Ar, Água Mineral e Ouro 18k São Puros? Misturas do Zero | Matéria e Misturas Ep. 3"
PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}O ar que você respira. [p=0.3] {b}A água mineral da garrafinha. [p=0.3] {c}Um anel de ouro dezoito quilates. [p=0.5] "
        "{d}Algum desses é uma *substância pura?* [p=0.5] {e}A resposta é não. [p=0.2] *Nenhum dos três.* [p=0.4] "
        "{f}E o ENEM sabe que muita gente erra isso."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai olhar para qualquer material do dia a dia [p=0.2] {b}e dizer: [p=0.2] "
        "é *substância pura,* [p=0.2] *mistura homogênea* [p=0.2] ou *mistura heterogênea.* [p=0.4] {c}Com um ritual de duas perguntas."),

    # ================= PRÉ-REQUISITOS (até 30 s) =================
    dict(id="03", block="prereq", text=
        "{t}Antes, uma lembrança rápida. [p=0.3] {a}*Substância pura* é o material com um único tipo de constituinte: "
        "[p=0.2] no LEGO, [p=0.2] um tipo só de montagem. [p=0.3] Água destilada: [p=0.2] só montagens de água. [p=0.4] "
        "{b}E *mistura* é o contrário: [p=0.2] duas ou mais substâncias juntas no mesmo lugar. [p=0.3] {c}Água com açúcar: "
        "[p=0.2] montagens de água [p=0.2] e de açúcar."),

    # ================= BLOCO A: FASE E MISTURA HOMOGÊNEA =================
    dict(id="04", block="fase", text=
        "{t}Antes de dividir as misturas em grupos, [p=0.2] uma palavra nova: [p=0.2] *fase.* [p=0.4] {a}Fase é cada parte do material "
        "[p=0.2] que tem a mesma aparência do começo ao fim. [p=0.4] {b}Num copo de água e óleo, [p=0.2] o óleo, em cima, é uma fase. "
        "[p=0.3] A água, embaixo, é outra. [p=0.4] {c}Contar fases é contar quantas partes diferentes você enxerga."),
    dict(id="05", block="homogenea", text=
        "{t}Agora, o que acontece quando você mexe açúcar na água? [p=0.4] {a}Ele some. [p=0.4] {b}Você olha o copo [p=0.2] e vê *uma coisa só:* "
        "[p=0.2] transparente, igual em todo canto. [p=0.3] Uma fase. [p=0.4] {c}Isso é uma *mistura homogênea:* [p=0.2] aspecto uniforme, "
        "[p=0.2] uma única fase. [p=0.4] {d}Homogêneo quer dizer *igual por inteiro.*"),
    dict(id="06", block="solucao", text=
        "{t}E essa mistura tem um apelido. [p=0.3] {a}Toda mistura homogênea também se chama *solução.* [p=0.4] "
        "{b}Água com sal é uma solução. [p=0.3] {c}E o ar, [p=0.2] como você vai ver daqui a pouco, [p=0.2] também."),

    # ================= BLOCO B: MISTURA HETEROGÊNEA =================
    dict(id="07", block="heterogenea", text=
        "{t}E quando dá para ver os pedaços? [p=0.4] {a}Pense numa *salada de frutas:* [p=0.2] banana, maçã, uva. [p=0.3] "
        "Você vê cada pedaço diferente. [p=0.4] {b}Isso é uma *mistura heterogênea:* [p=0.2] duas ou mais fases que dá para distinguir. "
        "[p=0.4] {c}Hetero quer dizer *diferente.*"),
    dict(id="08", block="hetero_ex", text=
        "{t}No dia a dia: [p=0.3] {a}água e óleo. [p=0.2] Mesmo mexendo, o óleo volta para cima. [p=0.3] Eles são *imiscíveis,* "
        "[p=0.2] ou seja, [p=0.2] não se misturam. [p=0.4] {b}E a pia de granito da cozinha: [p=0.2] olhe de perto. [p=0.3] "
        "Pontinhos pretos, brancos, rosados. [p=0.3] São três minerais diferentes: [p=0.2] quartzo, feldspato e mica. [p=0.3] "
        "{c}Duas fases ou mais: [p=0.2] *heterogênea.*"),
    dict(id="09", block="ritual", text=
        "{t}Então, para classificar qualquer material, [p=0.2] use sempre o mesmo ritual. [p=0.4] {a}Primeira pergunta: [p=0.2] "
        "é *uma substância só,* [p=0.2] ou mais de uma? [p=0.3] Uma só: [p=0.2] substância pura. [p=0.4] {b}Mais de uma: [p=0.2] mistura. "
        "[p=0.2] Aí vem a segunda pergunta: [p=0.2] *quantas fases eu vejo?* [p=0.4] {c}Uma: [p=0.2] homogênea. [p=0.2] Duas ou mais: "
        "[p=0.2] heterogênea. [p=0.4] {d}E atenção: [p=0.2] vale olhar *até no microscópio.*"),

    # ================= BLOCO C: MISTURA DE GASES =================
    dict(id="10", block="gases", text=
        "{t}E o ar, [p=0.2] que tem vários gases? [p=0.4] {a}Setenta e oito por cento é gás nitrogênio. [p=0.3] Vinte e um por cento, "
        "[p=0.2] gás oxigênio. [p=0.3] E um por cento, [p=0.2] outros gases. [p=0.4] {b}Várias substâncias: [p=0.2] é *mistura.* [p=0.4] "
        "{c}Mas você já viu o ar separado em camadas? [p=0.3] Nunca. [p=0.4] {d}Gases se misturam em qualquer quantidade [p=0.2] "
        "e nunca formam camadas. [p=0.3] Por isso, [p=0.2] *toda mistura de gases é homogênea.*"),

    # ================= BLOCO D: FUMAÇA E NEBLINA =================
    dict(id="11", block="fumaca", text=
        "{t}Mas e a fumaça? [p=0.2] E a neblina? [p=0.4] {a}Na fumaça, [p=0.2] tem pedacinhos *sólidos* de fuligem [p=0.2] espalhados no ar. "
        "[p=0.4] {b}Na neblina, [p=0.2] tem gotinhas de água *líquida* [p=0.2] espalhadas no ar. [p=0.4] {c}Não são só gases: "
        "[p=0.2] tem sólido ou líquido no meio. [p=0.3] Por isso, [p=0.2] *heterogêneas.* [p=0.4] {d}A regra continua: "
        "[p=0.2] mistura *só* de gases [p=0.2] é homogênea."),

    # ================= BLOCO E: LEITE E SANGUE =================
    dict(id="12", block="leite", text=
        "{t}E o leite? [p=0.3] Branco por igual. [p=0.2] Homogêneo, certo? [p=0.5] {a}Coloque uma gota no microscópio. [p=0.4] "
        "{b}Aparecem bolinhas de gordura boiando num líquido. [p=0.3] Duas fases. [p=0.4] {c}O leite é *heterogêneo.* [p=0.4] "
        "{d}Lembra da salada de frutas? [p=0.2] Às vezes, [p=0.2] é preciso um *microscópio* para ver os pedaços."),
    dict(id="13", block="sangue", text=
        "{t}Com o sangue, [p=0.2] acontece o mesmo. [p=0.4] {a}A olho nu, [p=0.2] um líquido vermelho, uniforme. [p=0.4] "
        "{b}No microscópio, [p=0.2] aparecem os glóbulos vermelhos, [p=0.2] como pequenos discos, [p=0.2] boiando num líquido amarelado, "
        "[p=0.2] o plasma. [p=0.4] {c}O sangue também é *heterogêneo.*"),

    # ================= BLOCO F: LIGAS METÁLICAS =================
    dict(id="14", block="ligas", text=
        "{t}E um metal pode ser mistura? [p=0.4] {a}Pode. [p=0.3] Derreta dois metais, [p=0.2] misture [p=0.2] e deixe esfriar. [p=0.4] "
        "{b}O resultado é uma *liga metálica:* [p=0.2] uma mistura de metal com outros elementos, [p=0.2] que endurece por inteiro. [p=0.4] "
        "{c}Olhe uma panela de inox: [p=0.2] brilho igual em toda parte. [p=0.3] Uma fase só. [p=0.4] {d}Por isso, [p=0.2] "
        "liga metálica é mistura *homogênea.*"),
    dict(id="15", block="ligas_ex", text=
        "{t}Ela tem até um nome: [p=0.2] *solução sólida.* [p=0.3] Uma solução que, [p=0.2] em vez de líquida, [p=0.2] é sólida. [p=0.4] "
        "{a}As que caem na prova: [p=0.2] *aço,* [p=0.2] ferro e carbono. [p=0.3] {b}*Aço inox,* [p=0.2] ferro, carbono, cromo e níquel. "
        "[p=0.3] {c}*Bronze,* [p=0.2] cobre e estanho. [p=0.3] {d}*Latão,* [p=0.2] cobre e zinco. [p=0.3] {e}E o *ouro dezoito quilates,* "
        "[p=0.2] ouro com cobre e prata."),

    # ================= BLOCO G: QUILATE =================
    dict(id="16", block="quilate", text=
        "{t}E o que quer dizer dezoito quilates? [p=0.4] {a}*Quilate* mede quanto de ouro tem na peça, [p=0.2] contando em vinte e quatro partes. "
        "[p=0.4] {b}Imagine a joia dividida em vinte e quatro pedaços iguais. [p=0.4] {c}No ouro dezoito quilates, [p=0.2] dezoito pedaços são de ouro. "
        "[p=0.3] Os outros seis, [p=0.2] de outros metais. [p=0.4] {d}Dezoito de vinte e quatro: [p=0.2] *setenta e cinco por cento* de ouro. "
        "[p=0.4] {e}Ouro vinte e quatro quilates é ouro puro. [p=0.3] Mas é mole demais para joia: [p=0.2] os outros metais dão resistência."),

    # ================= BLOCO H: DOIS ENGANOS DO COTIDIANO =================
    dict(id="17", block="enganos", text=
        "{t}Agora, [p=0.2] dois enganos do cotidiano. [p=0.4] {a}O ar é puro? [p=0.3] Não. [p=0.2] É mistura de gases. [p=0.3] "
        "Ar puro, na propaganda, [p=0.2] quer dizer ar *limpo,* [p=0.2] não substância pura. [p=0.5] {b}E a água mineral? [p=0.3] "
        "Leia o rótulo: [p=0.2] cálcio, [p=0.2] magnésio, [p=0.2] sódio. [p=0.3] São sais dissolvidos. [p=0.3] "
        "{c}Água mineral é *mistura homogênea.*"),
    dict(id="18", block="destilada", text=
        "{t}Então, [p=0.2] existe água pura? [p=0.4] {a}A *água destilada* [p=0.2] é a que mais se aproxima de uma substância pura. [p=0.5] "
        "{b}E o soro fisiológico do hospital? [p=0.3] É água [p=0.2] com zero vírgula nove por cento de sal. [p=0.3] {c}*Mistura homogênea.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] uma fase: homogênea. [p=0.2] Duas ou mais: heterogênea. [p=0.5] "
        "{b}Dois: [p=0.2] mistura de gases é sempre homogênea. [p=0.5] {c}Três: [p=0.2] liga metálica é mistura, [p=0.2] não substância pura."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erro1", text=
        "{t}Agora, [p=0.2] os quatro erros que mais derrubam gente. [p=0.4] {a}Primeiro: [p=0.2] o ar é substância pura. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque ele é invisível, [p=0.2] uniforme, [p=0.2] e a gente fala em ar puro. [p=0.4] "
        "{c}Mas são vários gases: [p=0.2] *mistura homogênea.*"),
    dict(id="21", block="erro2", text=
        "{a}Segundo: [p=0.2] água mineral é substância pura. [p=0.4] {b}Parece certo, [p=0.2] porque ela é transparente [p=0.2] "
        "e vem da natureza. [p=0.4] {c}Mas tem sais dissolvidos: [p=0.2] *mistura homogênea.*"),
    dict(id="22", block="erro3", text=
        "{a}Terceiro: [p=0.2] leite e sangue são homogêneos. [p=0.4] {b}Parece certo, [p=0.2] porque a olho nu [p=0.2] eles parecem uma coisa só. "
        "[p=0.4] {c}Mas no microscópio aparecem as fases: [p=0.2] *heterogêneos.*"),
    dict(id="23", block="erro4", text=
        "{a}Quarto: [p=0.2] ouro dezoito quilates é ouro puro. [p=0.4] {b}Parece certo, [p=0.2] porque é ouro de verdade, "
        "[p=0.2] vendido em joalheria. [p=0.4] {c}Mas só dezoito das vinte e quatro partes são de ouro: [p=0.2] *liga metálica,* "
        "[p=0.2] mistura homogênea."),

    # ================= EXERCÍCIO RÁPIDO =================
    dict(id="24", block="exercicio", text=
        "{t}Sua vez. [p=0.3] Classifique estes quatro. [p=0.4] {a}Água com gás, [p=0.2] na garrafa fechada. [p=0.3] {b}Aço. [p=0.3] "
        "{c}Água e areia. [p=0.3] {d}Gás oxigênio. [p=0.4] {p}*Pause o vídeo e classifique.* [p=1.5]"),
    dict(id="25", block="exercicio", text=
        "{t}Conferindo. [p=0.3] {a}Água com gás, [p=0.2] fechada: [p=0.2] o gás está dissolvido na água, [p=0.2] uma fase. "
        "[p=0.2] *Homogênea.* [p=0.4] {b}Aço: [p=0.2] liga metálica. [p=0.2] *Homogênea.* [p=0.4] {c}Água e areia: [p=0.2] "
        "a areia vai para o fundo, [p=0.2] duas fases. [p=0.2] *Heterogênea.* [p=0.4] {d}Gás oxigênio: [p=0.2] uma substância só. "
        "[p=0.2] *Substância pura.*"),

    # ================= QUESTÃO 7 =================
    dict(id="26", block="questao", text=
        "{t}Agora, [p=0.2] uma questão no estilo do ENEM. [p=0.4] {e1}Considere os materiais: [p=0.2] água mineral, [p=0.2] "
        "ouro dezoito quilates, [p=0.2] gás oxigênio, [p=0.2] ar filtrado [p=0.2] e granito. [p=0.4] {e2}Entre eles, [p=0.2] é substância pura:"),
    dict(id="27", block="questao", text=
        "{a}A: [p=0.2] apenas a água mineral. [p=0.4] {b}B: [p=0.2] apenas o ouro dezoito quilates. [p=0.4] {c}C: [p=0.2] apenas o gás oxigênio. "
        "[p=0.4] {d}D: [p=0.2] a água mineral e o gás oxigênio. [p=0.4] {e}E: [p=0.2] o ouro dezoito quilates e o granito. [p=0.5] "
        "{p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="28", block="questao", text=
        "{t}Vamos com o ritual, [p=0.2] um por um. [p=0.4] {m1}Água mineral: [p=0.2] água e sais. [p=0.2] Mais de uma substância, [p=0.2] "
        "uma fase. [p=0.2] Mistura homogênea. [p=0.4] {m2}Ouro dezoito quilates: [p=0.2] ouro, cobre e prata. [p=0.2] Liga, "
        "[p=0.2] mistura homogênea. [p=0.4] {m3}Gás oxigênio: [p=0.2] só O dois. [p=0.2] *Substância pura.*"),
    dict(id="29", block="questao", text=
        "{m4}Ar filtrado: [p=0.2] o filtro tira a poeira, [p=0.2] mas não separa os gases. [p=0.3] Continua mistura homogênea. [p=0.4] "
        "{m5}Granito: [p=0.2] três minerais que dá para ver. [p=0.2] Mistura heterogênea. [p=0.4] {r}Só o gás oxigênio é puro. "
        "[p=0.3] {ok}*Letra C.*"),
    dict(id="30", block="questao", text=
        "{t}E por que tanta gente marca a D? [p=0.4] {d}Porque trata a água mineral como água pura. [p=0.3] Ela é transparente, "
        "[p=0.2] parece só água. [p=0.4] Mas o rótulo não mente: [p=0.2] tem sais dissolvidos. [p=0.4] {a}A letra A cai na mesma armadilha. "
        "[p=0.4] {b}A B e a E [p=0.2] tratam o ouro dezoito quilates como puro, [p=0.2] e a E ainda erra no granito."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="31", block="recap", text=
        "{t}Para fechar, [p=0.2] as mesmas três frases. [p=0.5] {a}Um: [p=0.2] uma fase: homogênea. [p=0.2] Duas ou mais: heterogênea. [p=0.5] "
        "{b}Dois: [p=0.2] mistura de gases é sempre homogênea. [p=0.5] {c}Três: [p=0.2] liga metálica é mistura, [p=0.2] não substância pura."),

    # ================= PONTE =================
    dict(id="32", block="ponte", text=
        "{t}Um copo com água [p=0.2] e três cubos de gelo. [p=0.4] {a}Quantas fases? [p=0.6] {b}Se você respondeu quatro, [p=0.3] "
        "o próximo episódio é para você: [p=0.3] {c}*fases e componentes.*"),
    dict(id="33", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Química do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você achava que a água mineral era pura? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
