# Roteiro — Operações e Conjuntos Numéricos, Episódio 5: Revisão geral, pegadinhas e treino para o ENEM
# Base: Estudos/Enem/estudos/01-matematica/01-operacoes-e-conjuntos-numericos.html — seções 01, 11 e 13,
#   restritas aos temas dos episódios 1 a 4. As questões da seção 12 NÃO são usadas: as 5 questões são INÉDITAS.
# Marcações: {cue} animação · *texto* destaque · [p=2.0] pausa (com cronômetro na tela)
# Analogias retomadas: ordem = fila do pronto-socorro · sinais = dinheiro e dívida · conjuntos = bonecas russas ·
#   intervalos = colchete que abraça ou empurra · Venn = convidados contados duas vezes.
# Questões inéditas (contas conferidas):
#   Q1  20 − 3·(−4) − (−2)² = 20 + 12 − 4 = 28 (D). A −72 furou a fila · B 4 esqueceu −(−12) · C 12 dois erros ·
#       E 36 achou (−2)² = −4.
#   Q2  √25, √8, 0,1212…, 3,14, π, √(9/4): racionais = 5; 0,1212…; 3,14; 1,5 → 4 (D). A 1 raiz e dízima "irracionais" ·
#       B 2 toda raiz "irracional" · C 3 dízima "irracional" (ou 3,14 confundido com π) · E 5 só o π irracional.
#   Q3  "a partir de 50 e abaixo de 200" = [50, 200[ (C). A [50, 200] incluiu o 200 · B ]50, 200[ "a partir" ≠ "acima" ·
#       D ]50, 200] trocou as duas pontas · E [50, +∞] esqueceu o limite e fechou o infinito.
#   Q4  300 moradores, academia 180, piscina 140, nenhum 60 → 240 nos círculos → 320 − 240 = 80 (C).
#       A 20 esqueceu os nenhum · B 60 copiou o nenhum · D 100 apenas academia · E 240 a união.
#   Q5  50 alunos, M 25, F 20, Q 15, MF 8, MQ 6, FQ 5, os três 3. Miolo 3 · pares 5, 3, 2 · apenas M 14, F 10, Q 7 ·
#       soma 44 · nenhum 6. Apenas M = 14 (B). A 11 de fora para dentro · C 17 descontou só um par ·
#       D 22 descontou só o miolo · E 25 ignorou o "apenas".

TITULO = "Revisão: as pegadinhas de sinais, conjuntos, intervalos e Venn — Matemática ENEM, episódio 5"

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO E COMO CAI =================
    dict(id="01", block="hook", text=
        "{a}Este assunto quase não cai *sozinho* no ENEM. [p=0.4] {b}Mas aparece *dentro* de quase todas as outras questões. "
        "[p=0.4] {c}É aqui que se perde ponto [p=0.2] em questão que você *sabia* resolver."),
    dict(id="02", block="como_cai", text=
        "{t}E ele aparece de três jeitos. [p=0.3] {a}Um: [p=0.2] o diagrama de Venn com *pessoas,* [p=0.2] que cai quase todo ano. "
        "[p=0.4] {b}Dois: [p=0.2] contas com sinais *dentro* de uma questão de outro assunto. [p=0.4] {c}Três: [p=0.2] "
        "*classificar e ordenar* números: [p=0.2] racional, irracional, quem é maior."),
    dict(id="03", block="indice", text=
        "{t}Hoje, a revisão dos quatro episódios. [p=0.3] {a}A fila, [p=0.2] {b}as bonecas, [p=0.2] {c}os colchetes [p=0.2] "
        "{d}e os círculos. [p=0.4] {e}E a regra é esta: [p=0.2] eu *pergunto* antes de explicar. [p=0.3] Você pausa e responde. "
        "[p=0.3] Lembrar puxando da memória [p=0.2] é o que fixa de verdade."),

    # ================= VERDADEIRO OU FALSO =================
    dict(id="04", block="vf1", text=
        "{t}Lembra da fila do pronto-socorro? [p=0.3] Parênteses, potência, vezes e dividir, mais e menos. [p=0.4] "
        "{q}Verdadeiro ou falso: [p=0.2] *menos três ao quadrado é igual a nove.* [p=0.4] {p}Pause e responda. [p=2.0]"),
    dict(id="05", block="vf1", text=
        "{r}*Falso.* [p=0.3] {a}Engana porque o menos está colado no três, [p=0.2] e menos com menos dá mais. [p=0.4] "
        "{b}Mas sem parênteses, [p=0.2] a potência é atendida antes, [p=0.2] e só pega o três. [p=0.3] {c}*Menos nove.* "
        "[p=0.3] Só menos três entre parênteses, ao quadrado, dá nove."),
    dict(id="06", block="vf2", text=
        "{t}Agora, as bonecas russas: [p=0.2] naturais dentro dos inteiros, dentro dos racionais, dentro dos reais. "
        "[p=0.3] E o teste: [p=0.2] acaba, repete, ou nem acaba nem repete? [p=0.4] {q}Verdadeiro ou falso: "
        "[p=0.2] *toda dízima periódica é irracional.* [p=0.4] {p}Pause e responda. [p=2.0]"),
    dict(id="07", block="vf2", text=
        "{r}*Falso.* [p=0.3] {a}Engana porque ela nunca termina. [p=0.4] {b}Mas ela *repete,* [p=0.2] e o que repete tem fração "
        "que o gera. [p=0.3] {c}Zero vírgula três, três, três é um terço. [p=0.2] *Racional.*"),
    dict(id="08", block="vf3", text=
        "{t}E a raiz quadrada é o caminho de volta do quadrado. [p=0.3] Quadrado perfeito [p=0.2] é um inteiro vezes ele mesmo, "
        "[p=0.2] como quarenta e nove, [p=0.2] sete vezes sete. [p=0.4] "
        "{q}Verdadeiro ou falso: [p=0.2] *todo número com raiz é irracional.* [p=0.4] {p}Pause e responda. [p=2.0]"),
    dict(id="09", block="vf3", text=
        "{r}*Falso.* [p=0.3] {a}Engana porque os irracionais famosos são raízes, [p=0.2] como a raiz de dois. [p=0.4] "
        "{b}Mas raiz de quadrado perfeito é exata: [p=0.2] raiz de quarenta e nove é sete. [p=0.3] {c}*Racional.*"),
    dict(id="10", block="vf4", text=
        "{t}Agora, a festa: [p=0.2] quem é amigo dos dois [p=0.2] foi contado duas vezes. [p=0.4] {q}Verdadeiro ou falso: "
        "[p=0.2] *o número da união é sempre o número de A mais o número de B.* [p=0.4] {p}Pause e responda. [p=2.0]"),
    dict(id="11", block="vf4", text=
        "{r}*Falso.* [p=0.3] {a}Engana porque juntar parece somar. [p=0.4] {b}Mas quem está no meio [p=0.2] entrou nas duas listas. "
        "[p=0.3] {c}Desconte a interseção uma vez. [p=0.3] {d}Só dá para somar direto [p=0.2] quando os grupos são disjuntos: "
        "[p=0.2] sem ninguém em comum."),
    dict(id="12", block="vf5", text=
        "{t}E os colchetes: [p=0.2] virado para o número, [p=0.2] o braço abraça e o número entra. [p=0.3] Virado para fora, "
        "[p=0.2] empurra. [p=0.4] {q}Verdadeiro ou falso: [p=0.2] *de menos infinito até cinco, [p=0.2] com os dois colchetes "
        "fechados, [p=0.2] está certo.* [p=0.4] {p}Pause e responda. [p=2.0]"),
    dict(id="13", block="vf5", text=
        "{r}*Falso.* [p=0.3] {a}Engana porque o outro lado está fechado, [p=0.2] e parece que tem que combinar. [p=0.4] "
        "{b}Mas infinito não é número, [p=0.2] e não dá para abraçar o que nunca acaba. [p=0.3] {c}O lado do infinito "
        "é *sempre aberto.*"),
    dict(id="14", block="vf6", text=
        "{t}E no Venn, cada pedaço tem nome: [p=0.2] o meio é quem está nos dois grupos; [p=0.2] as pontas, "
        "quem está em um só. [p=0.4] {q}Último: [p=0.2] verdadeiro ou falso: [p=0.2] *apenas A é o círculo A inteiro.* [p=0.4] {p}Pause e responda. [p=2.0]"),
    dict(id="15", block="vf6", text=
        "{r}*Falso.* [p=0.3] {a}Engana porque o número do círculo está pronto no enunciado. [p=0.4] {b}Mas apenas A [p=0.2] "
        "é só o pedaço de A que não toca em ninguém: [p=0.2] sem as interseções. [p=0.3] {c}Leu apenas? [p=0.2] *Sublinhe.*"),

    # ================= QUESTÃO 1: SINAIS E ORDEM =================
    dict(id="16", block="q1", text=
        "{t}Agora, cinco questões novas, no estilo do ENEM. [p=0.4] {e1}Primeira. [p=0.2] O resultado de uma empresa no mês, "
        "em milhares de reais, [p=0.2] é dado por: [p=0.3] {e2}vinte, [p=0.2] menos três vezes, entre parênteses, menos quatro, "
        "[p=0.3] menos, entre parênteses, menos dois, ao quadrado. [p=0.4] {e3}Qual é o resultado?"),
    dict(id="17", block="q1", text=
        "{a}A: menos setenta e dois. [p=0.3] {b}B: quatro. [p=0.3] {c}C: doze. [p=0.3] {d}D: vinte e oito. [p=0.3] "
        "{e}E: trinta e seis. [p=0.4] {p}*Pause e resolva.* [p=2.0]"),
    dict(id="18", block="q1", text=
        "{t}Pela fila. [p=0.3] {a}Potência primeiro: [p=0.2] menos dois ao quadrado, [p=0.2] expoente par: [p=0.2] *mais quatro.* "
        "[p=0.4] {b}Depois o vezes: [p=0.2] três vezes menos quatro, [p=0.2] *menos doze.* [p=0.4] {c}Sobra: [p=0.2] vinte, "
        "menos, menos doze, menos quatro. [p=0.3] Cancelar dívida é ganhar: [p=0.2] vinte mais doze menos quatro. "
        "[p=0.3] {r}*Vinte e oito.* [p=0.2] Letra D."),
    dict(id="19", block="q1", text=
        "{t}E as erradas? [p=0.3] {a}Menos setenta e dois [p=0.2] furou a fila: [p=0.2] fez vinte menos três primeiro. "
        "[p=0.4] {b}Quatro [p=0.2] esqueceu que menos com menos doze vira mais doze. [p=0.4] {e}Trinta e seis [p=0.2] "
        "achou que menos dois ao quadrado dá menos quatro. [p=0.4] {c}E doze [p=0.2] cometeu esses dois últimos erros juntos."),

    # ================= QUESTÃO 2: CLASSIFICAÇÃO =================
    dict(id="20", block="q2", text=
        "{t}Segunda. [p=0.3] {e1}Considere os números: [p=0.2] raiz de vinte e cinco, [p=0.2] raiz de oito, [p=0.2] "
        "zero vírgula um, dois, um, dois, repetindo, [p=0.2] três vírgula catorze, [p=0.2] pi, [p=0.2] e raiz de nove quartos. "
        "[p=0.4] {e2}Quantos são *racionais?* [p=0.4] {a}A: um. [p=0.2] {b}B: dois. [p=0.2] {c}C: três. [p=0.2] {d}D: quatro. "
        "[p=0.2] {e}E: cinco. [p=0.4] {p}*Pause e classifique.* [p=2.0]"),
    dict(id="21", block="q2", text=
        "{t}O teste, um por um. [p=0.3] {n1}Raiz de vinte e cinco: [p=0.2] cinco. [p=0.2] Racional. [p=0.3] {n2}Raiz de oito: "
        "[p=0.2] oito não é quadrado perfeito. [p=0.2] Irracional. [p=0.3] {n3}Zero vírgula um, dois, um, dois: [p=0.2] repete. "
        "[p=0.2] Racional."),
    dict(id="22", block="q2", text=
        "{n4}Três vírgula catorze: [p=0.2] acaba. [p=0.2] Racional. [p=0.2] É só uma aproximação do pi, [p=0.2] não o pi. "
        "[p=0.3] {n5}Pi: [p=0.2] irracional. [p=0.3] {n6}Raiz de nove quartos: [p=0.2] três meios, [p=0.2] um vírgula cinco. "
        "[p=0.2] Racional. [p=0.4] {r}*Quatro racionais.* [p=0.2] Letra D."),
    dict(id="23", block="q2", text=
        "{t}As erradas: [p=0.3] {b}dois [p=0.2] é de quem acha que toda raiz é irracional. [p=0.4] {a}Um [p=0.2] ainda "
        "acha que a dízima é irracional. [p=0.4] {c}Três [p=0.2] errou só a dízima, [p=0.2] ou achou que três vírgula catorze "
        "é o pi. [p=0.4] {e}E cinco [p=0.2] acha que só o pi é irracional."),

    # ================= QUESTÃO 3: INTERVALO =================
    dict(id="24", block="q3", text=
        "{t}Terceira. [p=0.3] {e1}Um aplicativo dá desconto em compras *a partir de* cinquenta reais [p=0.2] e *abaixo de* "
        "duzentos reais. [p=0.4] {e2}Qual intervalo representa os valores com desconto? [p=0.4] {a}A: fechado no cinquenta "
        "e fechado no duzentos. [p=0.3] {b}B: aberto nos dois. [p=0.3] {c}C: fechado no cinquenta e aberto no duzentos. "
        "[p=0.3] {d}D: aberto no cinquenta e fechado no duzentos. [p=0.3] {e}E: fechado no cinquenta, até mais infinito, "
        "fechado. [p=0.4] {p}*Pause e escolha.* [p=2.0]"),
    dict(id="25", block="q3", text=
        "{t}A partir de cinquenta: [p=0.2] o cinquenta entra. [p=0.2] Braço abraçando, bolinha cheia. [p=0.4] "
        "{a}Abaixo de duzentos: [p=0.2] o duzentos fica de fora. [p=0.2] Braço empurrando, bolinha vazia. [p=0.3] "
        "{r}*Letra C.*"),
    dict(id="26", block="q3", text=
        "{t}As erradas: [p=0.2] {a}A colocou o duzentos para dentro. [p=0.3] {b}B confundiu a partir de com acima de. "
        "[p=0.3] {d}D trocou as duas pontas. [p=0.3] {e}E esqueceu o limite de duzentos [p=0.2] e ainda fechou o infinito."),

    # ================= QUESTÃO 4: VENN COM NENHUM =================
    dict(id="27", block="q4", text=
        "{t}Quarta. [p=0.3] {e1}Num condomínio com trezentos moradores, [p=0.2] cento e oitenta usam a academia, [p=0.2] "
        "cento e quarenta usam a piscina, [p=0.2] e sessenta não usam nenhuma das duas. [p=0.4] {e2}Quantos usam as duas? "
        "[p=0.4] {a}A: vinte. [p=0.2] {b}B: sessenta. [p=0.2] {c}C: oitenta. [p=0.2] {d}D: cem. [p=0.2] {e}E: duzentos e quarenta. "
        "[p=0.4] {p}*Pause e desenhe.* [p=2.0]"),
    dict(id="28", block="q4", text=
        "{t}O desenho. [p=0.3] {a}Os sessenta de fora [p=0.2] ficam fora dos círculos. [p=0.3] {b}Nos círculos: [p=0.2] "
        "trezentos menos sessenta, [p=0.2] *duzentos e quarenta.* [p=0.4] {c}Cento e oitenta mais cento e quarenta [p=0.2] "
        "dá trezentos e vinte. [p=0.3] Passou de duzentos e quarenta: [p=0.2] alguém foi contado duas vezes. [p=0.4] "
        "{d}Trezentos e vinte menos duzentos e quarenta: [p=0.2] *oitenta* no meio. [p=0.2] {r}Letra C."),
    dict(id="29", block="q4", text=
        "{t}As erradas: [p=0.2] {a}vinte esqueceu os sessenta de fora. [p=0.3] {b}Sessenta copiou o nenhum. [p=0.3] "
        "{d}Cem é *apenas* academia: [p=0.2] outra região. [p=0.3] {e}E duzentos e quarenta é a união inteira."),

    # ================= QUESTÃO 5: VENN DE TRÊS COM APENAS =================
    dict(id="30", block="q5", text=
        "{t}Última. [p=0.3] {e1}Numa turma de cinquenta alunos, [p=0.2] vinte e cinco gostam de Matemática, [p=0.2] "
        "vinte de Física [p=0.2] e quinze de Química. [p=0.4] {e2}Oito gostam de Matemática e Física, [p=0.2] seis de Matemática "
        "e Química, [p=0.2] cinco de Física e Química, [p=0.2] e três gostam das três. [p=0.4] {e3}Quantos gostam *apenas* de "
        "Matemática?"),
    dict(id="31", block="q5", text=
        "{a}A: onze. [p=0.2] {b}B: catorze. [p=0.2] {c}C: dezessete. [p=0.2] {d}D: vinte e dois. [p=0.2] {e}E: vinte e cinco. "
        "[p=0.4] {p}*Pause e preencha de dentro para fora.* [p=2.0]"),
    dict(id="32", block="q5", text=
        "{t}De dentro para fora. [p=0.3] {m}O miolo: [p=0.2] *três.* [p=0.4] {p1}Matemática e Física: [p=0.2] oito menos três, "
        "[p=0.2] *cinco.* [p=0.3] {p2}Matemática e Química: [p=0.2] seis menos três, [p=0.2] *três.* [p=0.4] {s1}Apenas Matemática: "
        "[p=0.2] vinte e cinco menos cinco, menos três, menos três: [p=0.2] *catorze.* [p=0.3] {r}Letra B."),
    dict(id="33", block="q5", text=
        "{t}E o desenho fecha? [p=0.3] {a}Física e Química só: [p=0.2] dois. [p=0.2] Apenas Física, dez. [p=0.2] Apenas Química, "
        "sete. [p=0.4] {b}Somando as sete regiões: [p=0.2] quarenta e quatro. [p=0.3] Sobram seis que não gostam de nenhuma. "
        "[p=0.3] Bateu."),
    dict(id="34", block="q5", text=
        "{t}As erradas: [p=0.2] {e}vinte e cinco ignorou o apenas: [p=0.2] é o círculo inteiro. [p=0.4] {a}Onze preencheu de "
        "fora para dentro: [p=0.2] tirou oito e seis, [p=0.2] e o miolo saiu duas vezes. [p=0.4] {c}Dezessete descontou só "
        "um par. [p=0.3] {d}E vinte e dois descontou só o miolo."),

    # ================= CHECKLIST =================
    dict(id="35", block="checklist", text=
        "{t}Agora, o checklist. [p=0.3] Marque só o que você conseguiria *explicar em voz alta* para outra pessoa, "
        "[p=0.2] sem consultar nada. [p=0.4] {a}Aplico a ordem das operações [p=0.2] e sei que menos três ao quadrado "
        "não é igual a menos três, entre parênteses, ao quadrado. [p=0.3] {b}Sei a fila dos conjuntos [p=0.2] e por que os "
        "irracionais ficam fora dela."),
    dict(id="36", block="checklist", text=
        "{c}Classifico qualquer número pelo decimal. [p=0.3] {d}Reconheço raiz exata pelos quadrados perfeitos. [p=0.3] "
        "{e}Leio intervalos [p=0.2] e lembro que o infinito é sempre aberto. [p=0.3] {f}Resolvo Venn de dois e de três grupos, "
        "de dentro para fora. [p=0.3] {g}E percebo a diferença entre A e *apenas* A."),
    dict(id="37", block="checklist", text=
        "{t}O que você não marcou, [p=0.2] reveja o episódio certo. [p=0.3] {a}Ordem e sinais: [p=0.2] episódio um. "
        "[p=0.3] {b}Conjuntos, decimais e raízes: [p=0.2] episódio dois. [p=0.3] {c}Intervalos: [p=0.2] episódio três. "
        "[p=0.3] {d}Venn e apenas: [p=0.2] episódio quatro."),
    dict(id="38", block="meta", text=
        "{t}E a meta antes de considerar o assunto dominado: [p=0.3] {a}resolver *trinta* questões [p=0.2] e acertar pelo menos "
        "*vinte e uma.* [p=0.2] Setenta por cento. [p=0.4] {b}Porque teoria assistida não é conteúdo dominado. [p=0.3] "
        "{c}*Só a questão prova isso.*"),

    # ================= PONTE E CTA =================
    dict(id="39", block="ponte", text=
        "{t}Fechamos o primeiro assunto. [p=0.3] {a}O próximo é [p=0.2] *divisibilidade, números primos, MMC e MDC.* [p=0.4] "
        "{b}E frações, potências e notação científica [p=0.2] têm séries próprias logo depois."),
    dict(id="40", block="cta", text=
        "Se essa revisão te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantas das cinco questões você acertou? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
