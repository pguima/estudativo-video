# Roteiro — Operações e Conjuntos Numéricos, Episódio 4: Diagrama de Venn — a questão "ponto garantido" do ENEM (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/01-operacoes-e-conjuntos-numericos.html — seção 10 + Questões 1, 2 e 9 da seção 12
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: a FESTA DE CASAMENTO. Quem é amigo dos dois foi contado duas vezes, uma na lista da noiva
#   e outra na do noivo. Por isso a gente desconta uma vez.
# Regra visual: toda questão é resolvida DESENHANDO o Venn; cada região se pinta e recebe o número quando é calculada.
#   A fórmula vem depois, como conferência. A palavra "apenas" aparece sublinhada em amarelo sempre que surgir.
# Frases-chave (meio e fim, idênticas):
#   1. Quem está nos dois foi contado duas vezes: desconte uma.
#   2. Preencha de dentro para fora.
#   3. "Apenas A" é só o pedaço de A que não toca em ninguém.
# Contas conferidas:
#   Q1: 500 − 90 = 410 · 320 + 250 = 570 · 570 − 410 = 160 (C). Só A 160, só B 90, nenhum 90 → 160+160+90+90 = 500.
#   Q9: 120 − 40 = 80 (C). Só Q 50, nenhum 30 → 80+40+50+30 = 200.
#   Q2: miolo 10 · pares 20, 10, 5 · sozinhos 20, 15, 15 · soma 95 · nenhum 5 (B). Fórmula: 150 − 65 + 10 = 95.

TITULO = "Diagrama de Venn: a Palavra \"Apenas\" Muda Tudo | Matemática Básica Ep. 4"
PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Esta é a questão mais *previsível* de Matemática do ENEM. [p=0.4] {b}Cai quase todo ano, [p=0.2] "
        "{c}só precisa de soma e subtração, [p=0.3] {d}e muita gente erra por *uma palavra:* [p=0.3] {e}*apenas.*"),
    dict(id="02", block="promessa", text=
        "{a}Até o fim desta aula, [p=0.2] você vai resolver qualquer questão de Venn [p=0.2] {b}com dois ou três grupos, "
        "[p=0.3] {c}sem decorar fórmula."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}O pré-requisito de hoje é o mais tranquilo da série: [p=0.3] {a}soma e subtração. [p=0.4] "
        "{b}Aqui você não precisa de *nenhuma conta difícil.* [p=0.3] {c}O que você precisa é de um *desenho.*"),

    # ================= BLOCO A: O DIAGRAMA =================
    dict(id="04", block="festa", text=
        "{t}Imagine um casamento. [p=0.3] {a}A noiva fez uma lista com *trinta* amigos. [p=0.3] {b}O noivo, "
        "uma lista com *vinte e cinco.* [p=0.4] {c}Mas *cinco* pessoas são amigas dos dois. [p=0.4] "
        "{d}Quantos convites imprimir?"),
    dict(id="05", block="festa", text=
        "{t}Cada lista é um *conjunto:* [p=0.2] um grupo com algo em comum. [p=0.4] {a}Cada pessoa da lista é um "
        "*elemento* do conjunto. [p=0.4] {b}E para enxergar os dois grupos juntos, [p=0.2] a gente desenha um "
        "*diagrama de Venn.*"),
    dict(id="06", block="festa", text=
        "{t}Um círculo para os amigos da noiva. [p=0.3] {a}Outro para os do noivo. [p=0.4] {b}E os dois círculos "
        "se *sobrepõem* no meio. [p=0.3] {c}Esse pedaço do meio [p=0.2] é quem está nos *dois* grupos: [p=0.2] "
        "os cinco amigos do casal."),

    # ================= BLOCO B: AS OPERAÇÕES =================
    dict(id="07", block="operacoes", text=
        "{t}E esses pedaços têm nomes. [p=0.4] {a}Quem vai receber convite? [p=0.3] Quem está na lista da noiva, "
        "[p=0.2] ou na do noivo, [p=0.2] ou nas duas. [p=0.4] {b}Isso é a *união:* [p=0.2] tudo o que está pintado. "
        "[p=0.3] {c}O símbolo parece um *U.*"),
    dict(id="08", block="operacoes", text=
        "{t}E quem está nas duas listas *ao mesmo tempo?* [p=0.4] {a}Isso é a *interseção:* [p=0.2] só o pedaço do meio. "
        "[p=0.3] {b}O símbolo é o U *de cabeça para baixo.*"),
    dict(id="09", block="operacoes", text=
        "{t}E quem é amigo *só* da noiva? [p=0.4] {a}Isso é a *diferença:* [p=0.2] noiva menos noivo. [p=0.3] "
        "{b}É o círculo da noiva [p=0.2] sem o pedaço do meio."),
    dict(id="10", block="operacoes", text=
        "{t}E quem *não* é amigo da noiva? [p=0.4] {a}O retângulo em volta é todo mundo que está sendo contado. "
        "[p=0.4] {b}Tudo o que fica *fora* do círculo da noiva [p=0.2] é o *complementar* da noiva."),

    # ================= BLOCO C: POR QUE SUBTRAIR =================
    dict(id="11", block="contagem", text=
        "{t}Agora, os convites. [p=0.3] {a}Antes, um símbolo: [p=0.2] *n de A* [p=0.2] quer dizer o *número de elementos* "
        "do grupo A. [p=0.4] {b}Quantas pessoas tem ali."),
    dict(id="12", block="contagem", text=
        "{t}Muita gente faz: [p=0.2] trinta mais vinte e cinco, [p=0.2] *cinquenta e cinco.* [p=0.4] {a}Mas olhe os cinco "
        "do meio. [p=0.3] {b}Eles foram contados *duas vezes:* [p=0.2] uma na lista da noiva [p=0.2] e outra na do noivo. "
        "[p=0.4] {c}Por isso a gente *desconta uma vez.* [p=0.3] {d}Cinquenta e cinco menos cinco: [p=0.2] *cinquenta convites.*"),
    dict(id="13", block="contagem", text=
        "{t}E isso vira a fórmula: [p=0.3] {a}o número da união [p=0.2] é o número de A, [p=0.2] mais o número de B, "
        "[p=0.2] menos o número da interseção. [p=0.4] {b}Só dá para somar direto [p=0.2] quando os grupos não têm "
        "*ninguém em comum.* [p=0.3] {c}Esses grupos se chamam *disjuntos.*"),

    # ================= BLOCO D: OS "NENHUM" =================
    dict(id="14", block="nenhum", text=
        "{t}E quem não está em nenhum círculo? [p=0.4] {a}Imagine que a cidade tem *oitenta* pessoas. [p=0.3] "
        "{b}Cinquenta foram convidadas. [p=0.3] {c}As outras *trinta* ficam fora dos dois círculos, [p=0.2] "
        "mas dentro do retângulo. [p=0.4] {d}Muita questão pede justamente esses: [p=0.2] os *nenhum.*"),

    # ================= BLOCO E: TRÊS CONJUNTOS =================
    dict(id="15", block="tres", text=
        "{t}E com *três* grupos? [p=0.4] {a}O desenho ganha um terceiro círculo, [p=0.2] e sete pedaços. [p=0.4] "
        "{b}No centro, o *miolo:* [p=0.2] quem está nos três. [p=0.3] {c}Em volta, [p=0.2] quem está em exatamente dois. "
        "[p=0.3] {d}E nas pontas, [p=0.2] quem está em um só."),
    dict(id="16", block="tres", text=
        "{t}E aqui está o segredo: [p=0.2] preencha *de dentro para fora.* [p=0.4] {a}Por quê? [p=0.3] {b}Porque o miolo "
        "aparece em *todos* os dados do enunciado. [p=0.3] {c}Se você começa pelas pontas, [p=0.2] acaba contando "
        "o miolo duas, três vezes."),
    dict(id="17", block="tres", text=
        "{t}O método tem quatro passos. [p=0.3] {a}Um: [p=0.2] o *miolo,* quem está nos três. [p=0.4] {b}Dois: [p=0.2] "
        "os pedaços de dois grupos, [p=0.2] descontando o miolo. [p=0.4] {c}Três: [p=0.2] os pedaços sozinhos, "
        "[p=0.2] descontando tudo o que já foi posto. [p=0.4] {d}Quatro: [p=0.2] some os sete pedaços [p=0.2] "
        "e compare com o total."),
    dict(id="18", block="tres", text=
        "{t}Existe uma fórmula para três grupos, [p=0.2] mas use só para *conferir.* [p=0.4] {a}Soma os três grupos, "
        "[p=0.3] {b}subtrai os pares, [p=0.3] {c}soma o trio."),

    # ================= BLOCO G: "APENAS" =================
    dict(id="19", block="apenas", text=
        "{t}E a palavra que mais derruba gente: [p=0.2] *apenas.* [p=0.4] {a}Os amigos da noiva [p=0.2] são o círculo "
        "*inteiro:* [p=0.2] trinta. [p=0.4] {b}Os amigos *apenas* da noiva [p=0.2] são só o pedaço que não toca em ninguém: "
        "[p=0.2] trinta menos cinco, [p=0.2] *vinte e cinco.* [p=0.4] {c}Sempre que ler *apenas,* [p=0.2] sublinhe."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos juntar tudo em três frases. [p=0.5] {a}Um: [p=0.2] quem está nos dois foi contado duas vezes: "
        "[p=0.2] desconte uma. [p=0.5] {b}Dois: [p=0.2] preencha de dentro para fora. [p=0.5] {c}Três: [p=0.2] "
        "apenas A é só o pedaço de A que não toca em ninguém."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erro1", text=
        "{t}Agora, os quatro erros que mais derrubam gente. [p=0.4] {a}Primeiro: [p=0.2] somar os dois grupos "
        "e esquecer de subtrair a interseção. [p=0.4] {b}Parece certo, [p=0.2] porque juntar é somar. [p=0.4] "
        "{c}Mas quem está no meio entrou duas vezes. [p=0.3] *Desconte uma.*"),
    dict(id="22", block="erro2", text=
        "{a}Segundo: [p=0.2] preencher de fora para dentro. [p=0.4] {b}Parece certo, [p=0.2] porque o enunciado "
        "dá primeiro os grupos inteiros. [p=0.4] {c}Mas o miolo está escondido dentro de todos eles. [p=0.3] "
        "*Comece pelo miolo.*"),
    dict(id="23", block="erro3", text=
        "{a}Terceiro: [p=0.2] responder o círculo inteiro quando a questão diz *apenas.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque o número do círculo está ali, prontinho no enunciado. [p=0.4] {c}Mas apenas é *sem* as interseções."),
    dict(id="24", block="erro4", text=
        "{a}Quarto: [p=0.2] esquecer quem não está em nenhum grupo. [p=0.4] {b}Parece certo, [p=0.2] porque eles "
        "não aparecem nos círculos. [p=0.4] {c}Mas eles estão no total. [p=0.3] *Fora dos círculos, dentro do retângulo.*"),

    # ================= QUESTÃO 1 =================
    dict(id="25", block="q1", text=
        "{t}Hora de treinar, no estilo do ENEM. [p=0.4] {e1}Uma operadora entrevistou quinhentos assinantes "
        "sobre dois serviços de streaming. [p=0.4] {e2}Trezentos e vinte assinam o serviço A, [p=0.2] "
        "duzentos e cinquenta assinam o B, [p=0.3] {e3}e noventa não assinam nenhum dos dois. [p=0.4] "
        "{e4}Quantos assinantes têm os dois serviços?"),
    dict(id="26", block="q1", text=
        "{t}As alternativas: [p=0.2] {a}A, setenta. [p=0.2] {b}B, noventa. [p=0.2] {c}C, cento e sessenta. "
        "[p=0.2] {d}D, cento e oitenta. [p=0.2] {e}E, duzentos e trinta. [p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="27", block="q1", text=
        "{t}Primeiro, a pista. [p=0.3] {a}Trezentos e vinte mais duzentos e cinquenta [p=0.2] dá *quinhentos e setenta.* "
        "[p=0.4] {b}Mais gente do que os quinhentos entrevistados! [p=0.4] {c}Impossível, [p=0.2] a não ser que alguém "
        "tenha sido contado duas vezes. [p=0.3] {d}Esse excesso é a interseção."),
    dict(id="28", block="q1", text=
        "{t}Agora, o desenho. [p=0.3] {a}Os noventa que não assinam nada [p=0.2] ficam *fora* dos círculos. [p=0.4] "
        "{b}Então quem está nos círculos é quinhentos menos noventa: [p=0.2] *quatrocentos e dez.* [p=0.4] "
        "{c}Quinhentos e setenta menos quatrocentos e dez: [p=0.2] *cento e sessenta* no meio. [p=0.4] {r}*Letra C.*"),
    dict(id="29", block="q1", text=
        "{t}Conferindo o desenho: [p=0.2] {a}só A, [p=0.2] trezentos e vinte menos cento e sessenta, [p=0.2] cento e sessenta. "
        "[p=0.3] {b}Só B, [p=0.2] noventa. [p=0.3] {c}Somando tudo com os noventa de fora: [p=0.2] quinhentos. [p=0.2] Bateu."),
    dict(id="30", block="q1", text=
        "{t}E as erradas? [p=0.3] {a}Setenta [p=0.2] é quinhentos e setenta menos quinhentos: [p=0.2] esqueceu os noventa "
        "que estão fora. [p=0.4] {b}Noventa [p=0.2] é o número de quem não assina nada, [p=0.2] copiado do enunciado. "
        "[p=0.4] {d}Cento e oitenta [p=0.2] é quem *não* assina o A: [p=0.2] o complementar, [p=0.2] a pergunta errada. "
        "[p=0.4] {e}E duzentos e trinta [p=0.2] tira os noventa do círculo A, [p=0.2] uma conta sem desenho."),

    # ================= QUESTÃO 9 =================
    dict(id="31", block="q9", text=
        "{t}Segunda questão. [p=0.3] {e1}Uma pesquisa com duzentos consumidores mostrou que [p=0.2] cento e vinte compram "
        "o produto P, [p=0.2] noventa compram o Q, [p=0.2] e quarenta compram os dois. [p=0.4] {e2}Quantos compram "
        "*apenas* o produto P? [p=0.4] {a}A, quarenta. [p=0.2] {b}B, cinquenta. [p=0.2] {c}C, oitenta. [p=0.2] "
        "{d}D, cento e vinte. [p=0.2] {e}E, cento e setenta. [p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="32", block="q9", text=
        "{t}Viu o *apenas?* [p=0.3] Sublinhe. [p=0.4] {a}De dentro para fora: [p=0.2] o meio, quarenta. [p=0.4] "
        "{b}Só P: [p=0.2] cento e vinte menos quarenta, [p=0.2] *oitenta.* [p=0.3] {r}*Letra C.* [p=0.4] "
        "{c}E de quebra: [p=0.2] só Q, cinquenta; [p=0.2] nenhum, trinta. [p=0.3] Oitenta, mais quarenta, mais cinquenta, "
        "mais trinta: [p=0.2] duzentos."),
    dict(id="33", block="q9", text=
        "{t}As erradas: [p=0.2] {d}cento e vinte é a pegadinha: [p=0.2] o círculo P inteiro, [p=0.2] ignorando o apenas. "
        "[p=0.4] {a}Quarenta é o meio. [p=0.3] {b}Cinquenta é apenas Q. [p=0.3] {e}E cento e setenta é a união inteira."),

    # ================= QUESTÃO 2 =================
    dict(id="34", block="q2", text=
        "{t}Agora, três grupos. [p=0.3] {e1}Numa escola com cem alunos: [p=0.2] sessenta jogam futebol, [p=0.2] "
        "cinquenta jogam vôlei, [p=0.2] quarenta fazem natação. [p=0.4] {e2}Trinta jogam futebol e vôlei, [p=0.2] "
        "vinte, futebol e natação, [p=0.2] quinze, vôlei e natação, [p=0.3] {e3}e dez fazem os três. [p=0.4] "
        "{e4}Quantos não praticam nenhum dos três?"),
    dict(id="35", block="q2", text=
        "{t}As alternativas: [p=0.2] {a}A, zero. [p=0.2] {b}B, cinco. [p=0.2] {c}C, dez. [p=0.2] {d}D, quinze. "
        "[p=0.2] {e}E, vinte. [p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="36", block="q2", text=
        "{t}De dentro para fora. [p=0.3] {m}Passo um, o miolo: [p=0.2] *dez* fazem os três. [p=0.4] "
        "{p1}Passo dois, os pares. [p=0.2] Futebol e vôlei: [p=0.2] trinta menos os dez do miolo, [p=0.2] *vinte.* [p=0.3] "
        "{p2}Futebol e natação: [p=0.2] vinte menos dez, [p=0.2] *dez.* [p=0.3] {p3}Vôlei e natação: [p=0.2] quinze menos dez, "
        "[p=0.2] *cinco.*"),
    dict(id="37", block="q2", text=
        "{s1}Passo três, os sozinhos. [p=0.2] Só futebol: [p=0.2] sessenta menos vinte, menos dez, menos dez: [p=0.2] *vinte.* "
        "[p=0.4] {s2}Só vôlei: [p=0.2] cinquenta menos vinte, menos cinco, menos dez: [p=0.2] *quinze.* [p=0.4] "
        "{s3}Só natação: [p=0.2] quarenta menos dez, menos cinco, menos dez: [p=0.2] *quinze.*"),
    dict(id="38", block="q2", text=
        "{t}Passo quatro: [p=0.2] some os sete pedaços. [p=0.3] {a}Dez, vinte, dez, cinco, vinte, quinze, quinze: "
        "[p=0.2] *noventa e cinco.* [p=0.4] {b}De cem alunos, [p=0.2] sobram *cinco* fora dos círculos. [p=0.3] {r}*Letra B.* "
        "[p=0.4] {c}E a fórmula confere: [p=0.2] cento e cinquenta, [p=0.2] menos sessenta e cinco, [p=0.2] mais dez: "
        "[p=0.2] noventa e cinco."),
    dict(id="39", block="q2", text=
        "{t}E as erradas? [p=0.3] {a}Zero: [p=0.2] somou os três grupos, [p=0.2] deu cento e cinquenta, passou de cem, "
        "[p=0.2] e achou que não sobra ninguém. [p=0.4] {d}Quinze: [p=0.2] subtraiu os pares [p=0.2] e esqueceu de somar o trio "
        "de volta. [p=0.4] {c}Dez [p=0.2] é o miolo, [p=0.2] a pergunta errada. [p=0.4] {e}E vinte [p=0.2] é só futebol: "
        "[p=0.2] outra região do desenho."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="40", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] quem está nos dois foi contado duas vezes: "
        "[p=0.2] desconte uma. [p=0.5] {b}Dois: [p=0.2] preencha de dentro para fora. [p=0.5] {c}Três: [p=0.2] "
        "apenas A é só o pedaço de A que não toca em ninguém."),

    # ================= PONTE =================
    dict(id="41", block="ponte", text=
        "{t}No último episódio deste assunto, [p=0.2] juntamos tudo: [p=0.3] {a}sinais, [p=0.2] {b}conjuntos numéricos, "
        "[p=0.2] {c}intervalos [p=0.2] {d}e Venn, [p=0.3] {e}com as pegadinhas e questões novas."),
    dict(id="42", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha caído na pegadinha do apenas? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
