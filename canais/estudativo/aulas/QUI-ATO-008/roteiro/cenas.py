# Estudativo · QUI-ATO-008 — Períodos e famílias (Química · Átomo e Tabela Periódica · Tabela periódica).
# Habilidade: achar o período e a família de um elemento pela distribuição eletrônica e ler uma casa da tabela periódica.
# Pré-requisitos: QUI-ATO-006. Próxima: QUI-ATO-009 (famílias com nome, metais e ametais).
# Primeira aula do módulo Tabela periódica: guarda a linguagem visual da tabela (veja o visual.py). Questão inédita.
# Fatos: 118 elementos, 7 períodos, 18 famílias, ordem de Z (Moseley, 1913, fica de fora); Na: Z 11, massa 22,99, 3s¹;
# Li 2s¹, K 4s¹ na família 1; famílias 13 a 18 = elétrons de valência + 10 (He, com 2, é a exceção da 18);
# numeração antiga 1A a 8A = elétrons de valência; transição (3 a 12): família = elétrons do último s + do d (Fe: 2 + 6 = 8,
# período 4); Cl (17) = 3s² 3p⁵ → período 3, família 17 (7A); Ca (20) = 4s² → período 4, família 2;
# F (9) = 1s² 2s² 2p⁵ → período 2, família 17; N (7) = 1s² 2s² 2p³ → período 2, família 15 (5A): de propósito, Z ≠ família.
# Erro comum: período pelo último subnível escrito (Fe termina em 3d⁶, mas está no período 4). A massa atômica fica para outra aula.

TITULO = "Períodos e famílias"

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
    dict(id="s01", block="gancho", text="{a}A tabela periódica parece uma parede de cento e dezoito quadradinhos para decorar. [p=0.3] {b}Não precisa. [p=0.2] {c}O lugar de cada elemento sai da distribuição dos elétrons."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai achar {a}o período [p=0.1] e {b}a família de um elemento, [p=0.2] e {c}ler uma casa da tabela."),
    # lembrete
    dict(id="s03", block="lembrete", text="Das aulas anteriores: [p=0.1] {a}zê é o número de prótons. [p=0.3] E {b}a camada de valência é a de número maior, [p=0.1] com os elétrons mais de fora."),
    # a ordem da tabela
    dict(id="s04", block="ordem", text="{a}Na tabela, os elementos estão em ordem de zê: [p=0.1] {b}um, dois, três, [p=0.1] da esquerda para a direita, linha por linha. [p=0.3] {c}As linhas deitadas são os períodos: são sete. [p=0.2] {d}As colunas em pé são as famílias, ou grupos: são dezoito."),
    # a casa
    dict(id="s05", block="casa", text="Cada quadradinho é {a}a casa de um elemento. [p=0.2] Na casa do sódio, você lê {b}o símbolo, ene á, [p=0.1] {c}o nome [p=0.1] e {d}o número atômico, onze. [p=0.3] Também aparece {e}um número com vírgula, a massa atômica, [p=0.1] que fica para outra aula."),
    dict(id="s06", block="casa", text="{a}O lugar de cada número muda de uma tabela para outra. [p=0.2] Por isso, {b}leia sempre a legenda que vem junto."),
    # período
    dict(id="s07", block="periodo", text="{a}O período é o número de camadas ocupadas. [p=0.2] Ou seja, {b}o maior número de camada da distribuição. [p=0.3] {c}O sódio termina em três esse um: [p=0.1] {d}três camadas, terceiro período."),
    # família
    dict(id="s08", block="familia", text="{a}A família junta elementos com o mesmo número de elétrons na valência. [p=0.3] {b}O sódio tem um elétron na camada três: [p=0.1] {c}família um. [p=0.2] {d}O lítio e o potássio também têm um só: [p=0.1] {e}estão na mesma coluna."),
    dict(id="s09", block="familia", text="Nas famílias um e dois, {a}o número da família é o número de elétrons na valência. [p=0.3] {b}Da família treze à dezoito, [p=0.1] {c}tire dez: [p=0.1] {d}na família dezessete há sete elétrons na valência. [p=0.2] {e}A exceção é o hélio, com dois, na família dezoito."),
    dict(id="s10", block="familia", text="{a}Muitas tabelas ainda trazem a numeração antiga, com a letra á: [p=0.1] {b}família um á, família dois á, até a família oito á. [p=0.3] {c}Nela, o número já é o de elétrons na valência: [p=0.1] {d}sete á é a família dezessete."),
    dict(id="s11", block="familia", text="{a}As famílias do meio, de três a doze, são os elementos de transição, [p=0.1] com a letra bê na numeração antiga. [p=0.2] {b}A distribuição deles termina em dê. [p=0.3] Para achar a família, {c}some os elétrons do último esse com os do dê. [p=0.2] {d}O ferro termina em quatro esse dois, três dê seis: [p=0.1] {e}dois mais seis, família oito, no quarto período."),
    # exemplo
    dict(id="s12", block="exemplo", text="Vamos a um exemplo completo: [p=0.1] {a}um esse dois, [p=0.1] dois esse dois, [p=0.1] dois pê cinco. [p=0.3] {b}O maior número é dois: segundo período. [p=0.2] {c}Na camada dois, dois mais cinco dá sete: [p=0.1] {d}família dezessete, ou sete á. [p=0.2] {e}Somando tudo, nove elétrons. [p=0.1] É o flúor."),
    # erro
    dict(id="s13", block="erro", text="O erro comum: [p=0.1] {a}tirar o período do último subnível escrito. [p=0.3] {b}O ferro termina em três dê seis, [p=0.1] e quem olha só o fim diz {c}terceiro período. [p=0.3] {d}Errado: o maior número de camada é o quatro, do quatro esse dois. [p=0.2] {e}O ferro está no quarto período. [p=0.2] {f}O período vem da camada de fora, não do último subnível."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho de prova: [p=0.1] {a}ache o maior número de camada: [p=0.1] {b}ele é o período. [p=0.3] {c}Some todos os elétrons dessa camada, onde quer que estejam escritos: [p=0.1] {d}a soma dá a família na numeração antiga. [p=0.3] {e}Três esse dois, três pê cinco: [p=0.1] período três, e dois mais cinco, família sete á."),
    dict(id="s15", block="atalho", text="Funciona porque {a}período e família dependem só da camada de fora. [p=0.3] {b}Não vale para os elementos de transição: [p=0.2] {c}neles, a família soma também os elétrons do dê, [p=0.1] {d}que é de uma camada mais de dentro."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Um elemento tem a distribuição um esse dois, [p=0.1] dois esse dois, [p=0.1] dois pê três. [p=0.3] {b}Em que período e em que família ele está? [p=0.2] E {c}qual é o seu zê?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}O maior número é dois: segundo período. [p=0.2] {b}Na camada dois, dois mais três dá cinco: [p=0.1] {c}família quinze, ou cinco á. [p=0.3] {d}Somando tudo: dois mais dois mais três dá sete. [p=0.2] {e}Zê sete: é o nitrogênio. [p=0.3] {f}Repare: zê sete, família quinze. [p=0.1] O zê não é a família."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}o período é o número de camadas, [p=0.2] {b}a família vem dos elétrons de valência [p=0.2] e {c}a casa traz o símbolo, o nome e o número atômico."),
    dict(id="s20", block="fim", text="Na próxima aula, você conhece {a}as famílias que têm nome, [p=0.1] como os halogênios e os gases nobres, [p=0.2] e separa {b}metais de ametais. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
