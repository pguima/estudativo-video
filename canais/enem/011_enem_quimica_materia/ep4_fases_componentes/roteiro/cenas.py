# Roteiro — Matéria, Substâncias e Misturas, Episódio 4: Fases e componentes (aula para iniciantes)
# Base: Estudos/Enem/estudos/02-quimica/01-materia-substancias-misturas.html — seção 05 + Questões 1, 4 e 9 da seção 12
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: contar FASES = tirar uma FOTO e contar as partes que o olho distingue;
#                  contar COMPONENTES = ler a LISTA DE INGREDIENTES (a receita). Duas contagens diferentes.
# Ritual visível em toda contagem: coluna FOTO (fases, de cima para baixo no recipiente) → coluna RECEITA (substâncias)
#   → só então as alternativas.
# Correção física em relação ao material: o gelo (0,92) é MAIS denso que o óleo (0,8). No pote com água, óleo, areia e gelo,
#   o gelo atravessa o óleo e fica na divisa, boiando na água (o material lista o gelo no topo). A contagem (4 fases) não muda.
# Frases-chave (meio e fim, idênticas):
#   1. Fase é a foto; componente é a receita.
#   2. Pedaços da mesma coisa no mesmo estado: uma fase só.
#   3. Os dois números são independentes: conte duas vezes.
# Cores: azul = definição · roxo = regra · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Água com 3 cubos de gelo: quantas fases? Fases e componentes do zero — Química ENEM, episódio 4"

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Um copo com água [p=0.2] e três cubos de gelo. [p=0.4] {b}Quantas fases? [p=0.8] {c}Se você respondeu *quatro,* "
        "[p=0.3] {d}você caiu na pegadinha mais comum deste assunto."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai contar *fases* e *componentes* de qualquer recipiente da prova [p=0.3] "
        "{b}sem cair em armadilha. [p=0.4] {c}Com duas contagens: [p=0.2] uma *foto* [p=0.2] e uma *receita.*"),

    # ================= PRÉ-REQUISITOS (até 30 s) =================
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembranças rápidas. [p=0.3] {a}*Substância* é um material com um tipo só de montagem: "
        "[p=0.2] água é uma substância, [p=0.2] álcool é outra. [p=0.4] {b}Mistura *homogênea* parece uma coisa só. "
        "[p=0.2] *Heterogênea* mostra partes diferentes."),
    dict(id="04", block="prereq", text=
        "{t}E *densidade* [p=0.2] é o quanto de massa cabe num mesmo espaço. [p=0.4] {a}A regra é simples: [p=0.2] "
        "o mais denso *afunda,* [p=0.2] o menos denso *flutua.*"),

    # ================= SISTEMA =================
    dict(id="05", block="sistema", text=
        "{t}Primeiro, uma palavra que a prova adora: [p=0.2] *sistema.* [p=0.4] {a}Sistema é aquilo que você está observando: "
        "[p=0.2] o conteúdo do copo, [p=0.2] do pote, [p=0.2] do recipiente. [p=0.4] {b}A pergunta é sempre sobre um sistema."),

    # ================= BLOCO A: FASE =================
    dict(id="06", block="fase", text=
        "{t}Como contar as fases de um sistema? [p=0.4] {a}Tire uma *foto.* [p=0.4] {b}*Fase* é cada parte com a mesma aparência "
        "do começo ao fim. [p=0.4] {c}Num copo com água e óleo, [p=0.2] a foto mostra duas partes: [p=0.2] fase um, o óleo. "
        "[p=0.3] Fase dois, a água. [p=0.4] {d}Contar fases é contar o que o olho distingue na foto."),

    # ================= BLOCO B: COMPONENTE =================
    dict(id="07", block="componente", text=
        "{t}E o que é componente? [p=0.4] {a}Agora esqueça a foto [p=0.2] e pegue a *receita.* [p=0.4] {b}*Componente* "
        "é cada substância presente no sistema. [p=0.3] É a lista de ingredientes. [p=0.4] {c}Água e óleo: [p=0.2] "
        "dois ingredientes, [p=0.2] dois componentes."),
    dict(id="08", block="colunas", text=
        "{t}São duas contagens diferentes. [p=0.3] {a}A foto conta fases. [p=0.3] {b}A receita conta componentes. [p=0.4] "
        "{c}Por isso, em toda questão, [p=0.2] você vai preencher duas colunas: [p=0.2] primeiro a *foto,* de cima para baixo. "
        "[p=0.3] Depois a *receita.* [p=0.4] {d}Só então olhe as alternativas."),

    # ================= BLOCO C: OS CUBOS DE GELO =================
    dict(id="09", block="gelo", text=
        "{t}Agora, o copo do começo. [p=0.4] {a}Na foto, [p=0.2] você vê três cubos separados. [p=0.3] {b}São três fases? [p=0.4] "
        "{c}Não. [p=0.3] Os três cubos são da mesma substância, [p=0.2] água, [p=0.2] no mesmo estado, [p=0.2] sólido. [p=0.4] "
        "{d}Pedaços da mesma coisa no mesmo estado [p=0.2] contam como *uma fase só.* [p=0.4] {e}Os três cubos ganham o mesmo número: "
        "[p=0.2] fase um, o gelo. [p=0.3] {f}Fase dois, a água líquida. [p=0.3] *Duas fases.*"),
    dict(id="10", block="gelo", text=
        "{t}E a receita? [p=0.4] {a}Gelo é água congelada. [p=0.3] A mesma substância. [p=0.4] {b}Um ingrediente só: [p=0.2] "
        "H dois O. [p=0.3] *Um componente.* [p=0.4] {c}Duas fases, [p=0.2] um componente."),

    # ================= BLOCO D: NÚMEROS INDEPENDENTES =================
    dict(id="11", block="independentes", text=
        "{t}Então fases e componentes andam sempre juntos? [p=0.4] {a}Não. [p=0.2] Os dois números são *independentes:* "
        "[p=0.2] um não decide o outro. [p=0.4] {b}Veja água com álcool. [p=0.3] Na foto, [p=0.2] uma parte só, transparente. "
        "[p=0.2] *Uma fase.* [p=0.4] {c}Na receita, [p=0.2] água e álcool. [p=0.2] *Dois componentes.*"),
    dict(id="12", block="tabela", text=
        "{t}Mais dois, para fixar. [p=0.3] {a}O ar: [p=0.2] *uma fase,* [p=0.2] porque mistura de gases é homogênea. [p=0.3] "
        "E *vários componentes:* [p=0.2] nitrogênio, oxigênio e outros gases. [p=0.5] {b}O granito: [p=0.2] *três fases* na foto, "
        "[p=0.2] os pontinhos de três cores. [p=0.3] E *três componentes:* [p=0.2] quartzo, feldspato e mica."),

    # ================= BLOCO E: CAMADAS PELA DENSIDADE =================
    dict(id="13", block="camadas", text=
        "{t}E quando o recipiente tem várias camadas, [p=0.2] como saber a ordem? [p=0.4] {a}Pela densidade. [p=0.3] "
        "Um pote com água, óleo, areia [p=0.2] e um cubo de gelo. [p=0.4] {b}A areia é a mais densa: [p=0.2] *afunda.* [p=0.4] "
        "{c}O óleo tem densidade zero vírgula oito, [p=0.2] menor que a da água: [p=0.2] fica *por cima* dela. [p=0.4] "
        "{d}E o gelo? [p=0.2] Zero vírgula nove dois. [p=0.3] Mais leve que a água, [p=0.2] mas mais pesado que o óleo. [p=0.4] "
        "{e}Ele atravessa o óleo [p=0.2] e para na divisa, [p=0.2] boiando na água."),
    dict(id="14", block="camadas", text=
        "{t}Agora, o ritual. [p=0.3] {a}Foto, de cima para baixo: [p=0.2] {f1}óleo, [p=0.3] {f2}gelo, [p=0.3] {f3}água, [p=0.3] "
        "{f4}areia. [p=0.3] *Quatro fases.* [p=0.5] {b}Receita: [p=0.2] {r1}óleo, [p=0.3] {r2}água, [p=0.3] {r3}areia. [p=0.4] "
        "{c}E o gelo? [p=0.2] É água: [p=0.2] não entra de novo na lista. [p=0.3] *Três componentes.*"),

    # ================= BLOCO F: O BRONZE =================
    dict(id="15", block="bronze", text=
        "{t}E um metal pode enganar? [p=0.4] {a}O bronze é uma *liga homogênea:* [p=0.2] uma mistura de metais [p=0.2] "
        "que derrete junto e endurece como uma coisa só. [p=0.4] {b}Na foto, [p=0.2] um bloco de cor única: [p=0.2] *uma fase.* [p=0.4] "
        "{c}Na receita, [p=0.2] cobre e estanho: [p=0.2] *dois componentes.* [p=0.4] {d}Uma fase, [p=0.2] dois componentes."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="16", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] fase é a foto; [p=0.2] componente é a receita. [p=0.5] "
        "{b}Dois: [p=0.2] pedaços da mesma coisa no mesmo estado: [p=0.2] uma fase só. [p=0.5] {c}Três: [p=0.2] "
        "os dois números são independentes: [p=0.2] conte duas vezes."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="17", block="erro1", text=
        "{t}Agora, os quatro erros que mais derrubam gente. [p=0.4] {a}Primeiro: [p=0.2] contar cada cubo de gelo como uma fase. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque os cubos estão separados, [p=0.2] e você vê três coisas. [p=0.4] {c}Mas é a mesma "
        "substância, [p=0.2] no mesmo estado: [p=0.2] *uma fase só.*"),
    dict(id="18", block="erro2", text=
        "{a}Segundo: [p=0.2] achar que fases e componentes são sempre o mesmo número. [p=0.4] {b}Parece certo, [p=0.2] porque em "
        "água e óleo [p=0.2] os dois dão dois. [p=0.4] {c}Mas água com álcool tem uma fase e dois componentes. [p=0.3] "
        "*Conte duas vezes.*"),
    dict(id="19", block="erro3", text=
        "{a}Terceiro: [p=0.2] contar o gelo e a água como dois componentes. [p=0.4] {b}Parece certo, [p=0.2] porque um é sólido "
        "[p=0.2] e o outro é líquido. [p=0.4] {c}Mas a receita não liga para o estado: [p=0.2] é a mesma substância. [p=0.3] "
        "*Um componente.*"),
    dict(id="20", block="erro4", text=
        "{a}Quarto: [p=0.2] contar os dois metais de uma liga como duas fases. [p=0.4] {b}Parece certo, [p=0.2] porque são dois "
        "ingredientes. [p=0.4] {c}Mas a foto mostra um bloco uniforme: [p=0.2] *uma fase.* [p=0.3] Os dois metais entram só na receita."),

    # ================= QUESTÃO 1 =================
    dict(id="21", block="q1", text=
        "{t}Agora, três questões no estilo do ENEM. [p=0.4] {e1}Primeira: [p=0.2] um copo contém água líquida [p=0.2] "
        "e três cubos de gelo. [p=0.3] {e2}Esse sistema apresenta: [p=0.4] {a}A: [p=0.2] um componente e uma fase. [p=0.3] "
        "{b}B: [p=0.2] um componente e duas fases. [p=0.3] {c}C: [p=0.2] um componente e quatro fases. [p=0.3] {d}D: [p=0.2] "
        "dois componentes e duas fases. [p=0.3] {e}E: [p=0.2] quatro componentes e quatro fases. [p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="22", block="q1", text=
        "{t}As colunas. [p=0.3] {f}Foto: [p=0.2] gelo, [p=0.2] uma fase. [p=0.2] Água líquida, [p=0.2] outra. [p=0.3] *Duas fases.* [p=0.4] "
        "{r}Receita: [p=0.2] só água. [p=0.3] *Um componente.* [p=0.3] {ok}*Letra B.* [p=0.5] {x}A C [p=0.2] contou cada cubo como uma fase. "
        "[p=0.3] {xd}A D [p=0.2] contou o gelo como outro componente. [p=0.3] {xe}A E [p=0.2] fez os dois erros. [p=0.3] {xa}E a A [p=0.2] "
        "juntou gelo e água numa fase só, [p=0.2] como se a foto fosse a receita."),

    # ================= QUESTÃO 4 =================
    dict(id="23", block="q4", text=
        "{t}Segunda. [p=0.3] {e1}Num recipiente foram colocados [p=0.2] água líquida, [p=0.2] óleo de cozinha, [p=0.2] areia [p=0.2] "
        "e um cubo de gelo. [p=0.3] {e2}Depois de alguns instantes, [p=0.2] o número de fases é: [p=0.4] {a}A: [p=0.2] dois. [p=0.2] "
        "{b}B: [p=0.2] três. [p=0.2] {c}C: [p=0.2] quatro. [p=0.2] {d}D: [p=0.2] cinco. [p=0.2] {e}E: [p=0.2] seis. [p=0.5] "
        "{p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="24", block="q4", text=
        "{t}É o pote que você já viu. [p=0.3] {f}Foto, de cima para baixo: [p=0.2] óleo, [p=0.2] gelo, [p=0.2] água, [p=0.2] areia. "
        "[p=0.3] *Quatro fases.* [p=0.3] {ok}*Letra C.* [p=0.5] {r}E cuidado: [p=0.2] a receita tem só três ingredientes. [p=0.3] "
        "{xb}Quem marcou B, três, [p=0.2] respondeu componentes quando a questão pedia fases. [p=0.4] {xa}A A esqueceu os sólidos. "
        "[p=0.3] {xd}E a D e a E [p=0.2] inventam fases que a foto não mostra."),

    # ================= QUESTÃO 9 =================
    dict(id="25", block="q9", text=
        "{t}Terceira, a mais difícil. [p=0.4] {e1}Num béquer foram colocados [p=0.2] um pedaço de bronze, [p=0.2] liga homogênea de cobre "
        "e estanho, [p=0.2] água líquida e areia. [p=0.3] {e2}Os números de fases e de componentes são, [p=0.2] respectivamente: [p=0.4] "
        "{a}A: [p=0.2] três e três. [p=0.2] {b}B: [p=0.2] três e quatro. [p=0.2] {c}C: [p=0.2] quatro e três. [p=0.2] "
        "{d}D: [p=0.2] quatro e quatro. [p=0.2] {e}E: [p=0.2] dois e quatro. [p=0.5] {p}*Pause o vídeo e tente.* [p=1.5]"),
    dict(id="26", block="q9", text=
        "{t}As colunas. [p=0.3] {f}Foto: [p=0.2] água, [p=0.2] areia [p=0.2] e o bronze, [p=0.2] um bloco uniforme. [p=0.3] "
        "*Três fases.* [p=0.4] {r}Receita: [p=0.2] cobre, [p=0.2] estanho, [p=0.2] água [p=0.2] e areia. [p=0.3] *Quatro componentes.* "
        "[p=0.3] {ok}*Letra B.*"),
    dict(id="27", block="q9", text=
        "{xa}A A [p=0.2] contou o bronze como um componente só: [p=0.2] esqueceu a receita da liga. [p=0.4] {xd}A D [p=0.2] "
        "contou os dois metais como duas fases. [p=0.4] {xc}A C [p=0.2] trocou as duas colunas. [p=0.4] {xe}E a E [p=0.2] "
        "juntou o bronze e a areia numa fase só, [p=0.2] só porque os dois são sólidos."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] fase é a foto; [p=0.2] componente é a receita. [p=0.5] "
        "{b}Dois: [p=0.2] pedaços da mesma coisa no mesmo estado: [p=0.2] uma fase só. [p=0.5] {c}Três: [p=0.2] "
        "os dois números são independentes: [p=0.2] conte duas vezes."),

    # ================= PONTE =================
    dict(id="29", block="ponte", text=
        "{t}E se eu te der um material desconhecido, [p=0.2] {a}só um termômetro [p=0.2] {b}e um relógio? [p=0.4] "
        "{c}Dá para saber se ele é puro. [p=0.5] {d}No próximo episódio: [p=0.2] *a curva de aquecimento,* [p=0.2] "
        "o item mais cobrado deste assunto."),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Química do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] antes desta aula, você respondia quatro fases? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
