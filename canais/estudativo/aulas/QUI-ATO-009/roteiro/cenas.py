# Estudativo · QUI-ATO-009 — Famílias com nome, metais e ametais (Química · Átomo e Tabela Periódica · Tabela periódica).
# Habilidade: dizer o que os metais alcalinos, os halogênios e os gases nobres têm em comum, classificar um elemento em metal ou
# ametal e prever a carga do seu íon.
# Pré-requisitos: QUI-ATO-008. Próxima: QUI-ATO-010 (raio atômico).
# Questão inédita, criada para esta aula. A regra do octeto, com esse nome, fica para a QUI-LIG-001: aqui só "a última camada
# igual à de um gás nobre".
# Fatos: gases nobres (18) com 8 elétrons na valência, He com 2; alcalinos (1): Li, Na, K, Rb, Cs, Fr, reagem com violência na
# água, íon 1+; alcalinoterrosos (2): Be, Mg, Ca, Sr, Ba, Ra, íon 2+; calcogênios (16): O, S, íon 2−; halogênios (17):
# F, Cl, Br, I, íon 1−; flúor na pasta de dente (fluoreto), cloro no tratamento da água; H na coluna 1 não é metal alcalino;
# Fe forma Fe²⁺ e Fe³⁺. Atalho: ametal → família − 18 (17 − 18 = −1; 16 − 18 = −2).

TITULO = "Famílias com nome, metais e ametais"

VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que passou anos sem estudar: voz masculina, grave, calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína; mostre "
            "surpresa no erro, entusiasmo no atalho e dê ênfase forte às palavras-chave. Ritmo tranquilo, com pausas "
            "naturais entre as ideias. Leia exatamente o texto, sem repetir nem acrescentar nada."),
)

SCENES = [
    # gancho
    dict(id="s01", block="gancho", text="{a}Um pedaço de sódio jogado na água reage com violência, [p=0.1] e pode até explodir. [p=0.3] {b}O neônio, do letreiro luminoso, quase não reage com nada. [p=0.3] {c}A diferença está nos elétrons da última camada."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}reconhecer as famílias que têm nome, [p=0.2] {b}separar metal de ametal [p=0.2] e {c}prever a carga do íon de um elemento."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula anterior: [p=0.1] {a}a família vem dos elétrons de valência. [p=0.3] E da aula de íons: [p=0.1] {b}perder elétrons deixa o átomo positivo, [p=0.1] {c}ganhar deixa negativo."),
    # gases nobres
    dict(id="s04", block="nobres", text="Comece pela última coluna, {a}a família dezoito: os gases nobres. [p=0.2] {b}Hélio, neônio, argônio e outros. [p=0.3] {c}Eles têm oito elétrons na valência, [p=0.1] {d}ou dois, no caso do hélio: um arranjo muito estável. [p=0.3] Por isso, {e}quase não reagem com outros átomos."),
    dict(id="s05", block="nobres", text="{a}Os outros átomos tendem a ganhar ou perder elétrons até ficar com a última camada igual à de um gás nobre. [p=0.3] {b}Essa ideia é a base das ligações químicas, assunto de outra aula."),
    # famílias de metais
    dict(id="s06", block="metais_fam", text="{a}Na família um ficam os metais alcalinos: [p=0.1] {b}lítio, sódio, potássio e outros. [p=0.3] {c}Eles têm um elétron só na valência, [p=0.1] e o perdem com muita facilidade. [p=0.2] {d}Por isso reagem com violência na água. [p=0.3] {e}Perdendo um elétron, viram íon com carga um mais."),
    dict(id="s07", block="metais_fam", text="{a}Na família dois ficam os metais alcalinoterrosos, [p=0.1] como {b}o magnésio e o cálcio, o dos ossos. [p=0.3] {c}Dois elétrons na valência: [p=0.1] {d}perdem esses dois elétrons e viram íon com carga dois mais."),
    # famílias de ametais
    dict(id="s08", block="ametais_fam", text="{a}Na família dezessete ficam os halogênios: [p=0.1] {b}flúor, cloro, bromo e iodo. [p=0.2] {c}Compostos de flúor vão na pasta de dente, [p=0.1] e compostos de cloro limpam a água da torneira. [p=0.3] {d}Eles têm sete elétrons na valência: [p=0.1] {e}falta um para oito. [p=0.2] {f}Ganham um elétron e viram íon com carga um menos."),
    dict(id="s09", block="ametais_fam", text="{a}Na família dezesseis ficam os calcogênios, como {b}o oxigênio e o enxofre. [p=0.3] {c}Seis elétrons na valência: [p=0.1] ganham dois, [p=0.1] {d}e a carga é dois menos."),
    # metais e ametais
    dict(id="s10", block="classes", text="A tabela também se divide em {a}metais e ametais. [p=0.2] {b}Os metais são a maior parte, à esquerda e no meio. [p=0.3] {c}Têm brilho, conduzem calor e eletricidade [p=0.1] e {d}podem virar fio ou chapa. [p=0.3] {e}Com poucos elétrons na valência, eles perdem elétrons: [p=0.1] viram cátions."),
    dict(id="s11", block="classes", text="{a}Os ametais ficam no canto de cima, à direita, antes da coluna dos gases nobres. [p=0.2] {b}Não têm o brilho do metal e conduzem mal. [p=0.3] {c}Com muitos elétrons na valência, eles ganham elétrons: [p=0.1] viram ânions."),
    # erro
    dict(id="s12", block="erro", text="O erro comum: [p=0.1] {a}chamar o hidrogênio de metal alcalino, [p=0.1] porque ele fica na coluna um. [p=0.3] {b}Ele tem um elétron na valência, [p=0.1] {c}mas é um gás, e não é metal. [p=0.3] {d}Muitas tabelas desenham o hidrogênio separado, justamente para evitar essa confusão."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho para a carga do íon: [p=0.2] {a}metal das famílias um e dois: [p=0.1] {b}a carga é o número da família, positiva. [p=0.2] {c}O alumínio, da família treze, tem três elétrons na valência: [p=0.1] carga três mais. [p=0.3] {d}Ametal: [p=0.1] {e}faça a família menos dezoito. [p=0.2] {f}Dezessete menos dezoito dá menos um. [p=0.2] {g}Dezesseis menos dezoito dá menos dois."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o metal perde o que tem na valência, [p=0.1] e {b}o ametal ganha o que falta para chegar a oito. [p=0.3] {c}Não serve para os metais do meio da tabela, [p=0.1] que formam íons com cargas variadas: [p=0.1] {d}o ferro forma ferro dois mais e ferro três mais."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}O magnésio está na família dois, [p=0.1] e {b}o bromo, na família dezessete. [p=0.3] {c}Cada um é metal ou ametal? [p=0.2] E {d}qual é a carga do íon de cada um?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Magnésio, família dois: [p=0.1] {b}metal alcalinoterroso. [p=0.2] {c}Perde dois elétrons: carga dois mais. [p=0.3] {d}Bromo, família dezessete: [p=0.1] {e}ametal, um halogênio. [p=0.2] {f}Dezessete menos dezoito dá menos um: [p=0.1] carga um menos."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}alcalinos têm um elétron na valência, [p=0.1] halogênios têm sete, [p=0.1] e gases nobres têm oito, um arranjo estável. [p=0.2] {b}Metal perde e vira cátion. [p=0.1] {c}Ametal ganha e vira ânion."),
    dict(id="s19", block="fim", text="Na próxima aula, você descobre {a}qual átomo é maior [p=0.1] {b}só pela posição na tabela. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
