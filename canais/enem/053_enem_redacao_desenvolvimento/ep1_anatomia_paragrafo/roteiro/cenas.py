# Roteiro — Redação ENEM, Desenvolvimento, Episódio 1 de 7: Onde a tese é provada — as cinco partes do parágrafo
# Base: Estudos/Enem/estudos/06-redacao/03-desenvolvimento.html — seções 01 e 02 + Questão 6 da seção 12.
#   Modelagem com o parágrafo-modelo da seção 08 (só as cinco partes coloridas; a análise frase por frase fica no ep. 5)
#   e contraexemplo com a Versão 1 da seção 09 (só opinião). C2 e C3 só citadas (uma frase cada, sem níveis).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora da SÉRIE: cada parágrafo de desenvolvimento ENTREGA UM ITEM da lista colada na caixa, em cinco etapas —
#   ETIQUETA DO ITEM (tópico frasal) · POR QUE ESTÁ NA CAIXA (argumento) · NOTA FISCAL (repertório) · PRODUTO
#   FUNCIONANDO na casa do cliente (análise) · RECIBO ASSINADO (fechamento). Liga à série Introdução (a lista "contém 2
#   itens") e à série de Linguagens (tese = tampo da mesa, argumentos = pernas).
# Frases-chave (meio e fim, idênticas):
#   1. Cada parágrafo entrega um item da lista.  2. Etiqueta, por quê, nota fiscal, produto funcionando, recibo.
#   3. Cinco partes é método; o raciocínio é que não pode faltar.
# FIDELIDADE: as cinco partes são MÉTODO DE ESTUDO, não critério do Inep (cenas 13–14, erro 2 e Questão 6). C3 e C2 com as
#   palavras do material; nenhum nível ou nota. Lidos EXATAMENTE como no material: parágrafo-modelo da seção 08 (16–17),
#   Versão 1 da seção 09 (18) e Questão 6 (25–27). Números e anos falados por extenso.
# Cores: azul = definição · verde = dica/método · âmbar = armadilha · vermelho = erro · roxo = regra oficial (Cartilha).

TITULO = "Seu Parágrafo Prova a Tese ou Só Repete? As 5 Partes do Desenvolvimento | Desenvolvimento da Redação Ep. 1"
# Estilo da voz (gerar_voz_local.py): o mesmo da série Introdução
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo da folha em branco: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa nas armadilhas ('Parece certo... mas não é!'); comemore os acertos com "
            "entusiasmo ('Letra E!'); dê ênfase forte às palavras-chave. Quando ler o parágrafo no rascunho, leia como "
            "quem lê um texto bonito, e quando pensar em voz alta, soe como quem está raciocinando de verdade. Ritmo "
            "didático e tranquilo, sem pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente "
            "como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO E PROMESSA =================
    dict(id="01", block="hook", text=
        "{a}Na introdução, [p=0.2] você *prometeu.* [p=0.4] {b}Nos parágrafos de desenvolvimento, [p=0.2] você *prova,* "
        "[p=0.3] {c}ou só repete a promessa com outras palavras. [p=0.5] {d}A diferença está em *quatro movimentos* "
        "[p=0.2] depois da primeira frase."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai saber as *cinco partes* de um parágrafo de desenvolvimento [p=0.3] "
        "{b}e *que pergunta* cada uma responde. [p=0.4] {c}E calma: [p=0.2] cada palavra nova vai ser explicada, [p=0.2] "
        "uma de cada vez."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Antes, [p=0.2] uma revisão relâmpago da série *Introdução.* [p=0.3] {a}A tese é a sua posição sobre o tema, "
        "[p=0.2] e uma boa tese anuncia *dois eixos:* [p=0.2] eixo é cada caminho que sustenta essa posição. [p=0.4] "
        "{b}Promessa feita [p=0.2] é *promessa cobrada:* [p=0.2] cada eixo anunciado precisa ser provado. [p=0.4] {c}E a "
        "gente guardou esta tese, [p=0.2] do tema de dois mil e vinte, [p=0.2] com dois eixos: [p=0.2] {d}a "
        "*desinformação* [p=0.2] {e}e a *mídia.*"),

    # ================= A ENTREGA (CONCRETO ANTES DO ABSTRATO) =================
    dict(id="04", block="entrega", text=
        "{t}Agora imagine duas entregas. [p=0.3] {a}Na primeira, [p=0.2] o entregador deixa a caixa *fechada* na calçada "
        "[p=0.2] e vai embora. [p=0.4] {b}Na segunda, [p=0.2] ele *abre* a caixa, [p=0.2] {c}mostra o produto, [p=0.2] "
        "{d}prova que ele *funciona* [p=0.2] {e}e pede a *assinatura do recibo.* [p=0.4] {f}Qual das duas você "
        "chamaria de entrega?"),
    dict(id="05", block="analogia", text=
        "{t}Na série Introdução, [p=0.2] você colou na caixa a lista: [p=0.2] *contém dois itens.* [p=0.4] {a}Agora a "
        "caixa abre. [p=0.3] {b}Cada *parágrafo de desenvolvimento,* [p=0.2] um dos parágrafos entre a introdução e a "
        "conclusão, [p=0.2] *entrega um item.* [p=0.4] {c}O primeiro parágrafo entrega o item A. [p=0.2] {d}O segundo, "
        "[p=0.2] o item B."),
    dict(id="06", block="analogia", text=
        "{t}E toda entrega tem *cinco etapas.* [p=0.3] {a}A *etiqueta* do item, [p=0.2] {b}*por que* ele está na caixa, "
        "[p=0.2] {c}a *nota fiscal* que comprova, [p=0.2] {d}o *produto funcionando* na casa do cliente [p=0.2] {e}e a "
        "*assinatura do recibo,* [p=0.2] que liga tudo de volta à tese. [p=0.5] {f}Lembra da série de Linguagens? [p=0.2] "
        "Lá, a tese era o *tampo da mesa,* [p=0.2] e os argumentos eram as *pernas.* [p=0.3] {g}Aqui, [p=0.2] você aprende "
        "a construir *cada perna.*"),

    # ================= BLOCO A: O QUE O ENEM COBRA AQUI =================
    dict(id="07", block="cobra", text=
        "{t}Mas por que o desenvolvimento pesa tanto? [p=0.4] {a}A redação é corrigida por cinco *competências:* [p=0.2] "
        "cinco critérios de correção. [p=0.3] Duas se decidem, sobretudo, aqui. [p=0.4] {b}A *Competência três* avalia se o "
        "texto seleciona, relaciona, organiza e interpreta informações, fatos e opiniões [p=0.2] em defesa de um ponto de "
        "vista. [p=0.4] {c}A *Competência dois* avalia se o *repertório sociocultural,* [p=0.2] o conhecimento de fora da "
        "prova, [p=0.2] é legitimado, pertinente e produtivo."),
    dict(id="08", block="cobra", text=
        "{a}E a *Cartilha do Participante,* [p=0.2] o guia oficial da redação, [p=0.2] associa os níveis mais altos da C "
        "três ao desenvolvimento dos argumentos com explicitação da sua relevância [p=0.2] {b}e à *autoria:* [p=0.2] quando "
        "dá para perceber o *seu* raciocínio, [p=0.2] e não só informação juntada. [p=0.4] {c}Cada competência vai ganhar "
        "a sua própria série."),

    # ================= BLOCO B: AS TRÊS IDEIAS QUE MAIS RENDEM =================
    dict(id="09", block="ideias", text=
        "{t}Se você guardar só três ideias desta série, [p=0.2] guarde estas. [p=0.4] {a}Um: [p=0.2] cada parágrafo de "
        "desenvolvimento cumpre *um eixo* anunciado na introdução. [p=0.4] {b}Dois: [p=0.2] o repertório só é produtivo "
        "se vier seguido de *análise.* [p=0.4] {c}Três: [p=0.2] a última frase responde ao *e daí?,* [p=0.2] ligando o "
        "parágrafo de volta à tese."),

    # ================= BLOCO C: AS CINCO PARTES E SUAS PERGUNTAS =================
    dict(id="10", block="partes", text=
        "{t}Agora, [p=0.2] as cinco partes, [p=0.2] uma de cada vez. [p=0.3] {a}O *tópico frasal* é a frase, [p=0.2] em "
        "geral a primeira, [p=0.2] que anuncia o que o parágrafo vai provar. [p=0.2] Ele *afirma.* [p=0.2] Pergunta: [p=0.2] "
        "o que eu afirmo? [p=0.4] {b}O *argumento* explica *por que* essa afirmação procede. [p=0.2] Pergunta: [p=0.2] por "
        "que procede? [p=0.4] {c}O *repertório* é o conhecimento de fora que *comprova.* [p=0.2] Pergunta: [p=0.2] o que "
        "comprova?"),
    dict(id="11", block="partes", text=
        "{d}A *análise* interpreta a referência à luz do problema. [p=0.2] Pergunta: [p=0.2] o que isso mostra? [p=0.4] "
        "{e}E o *fechamento,* [p=0.2] a última frase, [p=0.2] liga tudo de volta à tese. [p=0.2] Pergunta: [p=0.2] e daí? "
        "[p=0.5] {f}Cinco partes, [p=0.2] cinco perguntas. [p=0.2] E cada uma é uma etapa da entrega."),

    # ================= BLOCO D: O PESO DE CADA PARTE =================
    dict(id="12", block="peso", text=
        "{t}E elas têm o mesmo tamanho? [p=0.4] {a}Não. [p=0.2] Estas barras mostram o peso *típico* de cada parte [p=0.2] "
        "num parágrafo bem desenvolvido. [p=0.4] {b}A *análise* costuma ser a mais longa, [p=0.2] porque é nela que aparece "
        "a *autoria.* [p=0.4] {c}É o produto funcionando: [p=0.2] a parte que o cliente mais quer ver. [p=0.3] {d}E repare "
        "no aviso: [p=0.2] proporção típica, [p=0.2] *não é regra.*"),

    # ================= BLOCOS E E F: A ESCADA E MÉTODO, NÃO REGRA =================
    dict(id="13", block="metodo", text=
        "{t}De onde vêm essas cinco partes? [p=0.4] {a}De uma *escada de quatro degraus:* [p=0.2] {a1}afirmar, [p=0.2] "
        "{a2}explicar, [p=0.2] {a3}fundamentar [p=0.2] {a4}e ligar. [p=0.4] {b}A fundamentação se divide em duas: [p=0.2] "
        "*repertório* e *análise.* [p=0.3] Por isso, quatro degraus viram cinco partes. [p=0.4] {c}Na série da Competência "
        "três, [p=0.2] você vê como o corretor pontua isso."),
    dict(id="14", block="metodo", text=
        "{t}Agora, [p=0.2] um aviso importante. [p=0.3] {a}As cinco partes são um *método de estudo,* [p=0.2] *não* um "
        "critério do Inep, [p=0.2] o órgão que faz o ENEM. [p=0.4] {b}As partes podem mudar de ordem: [p=0.2] o repertório "
        "pode vir antes da explicação. [p=0.3] {c}Duas partes podem caber numa mesma frase. [p=0.3] {d}E não há número "
        "oficial de parágrafos. [p=0.4] {e}O modelo com *dois* parágrafos de desenvolvimento é o mais comum [p=0.2] porque "
        "cabe bem na folha. [p=0.4] {f}Os descritores, [p=0.2] as frases da grade de correção, [p=0.2] avaliam se as "
        "informações estão relacionadas ao tema, [p=0.2] organizadas, [p=0.2] desenvolvidas [p=0.2] e a serviço de um "
        "ponto de vista."),

    # ================= EU FAÇO: O PARÁGRAFO-MODELO NO RASCUNHO =================
    dict(id="15", block="eufaco", text=
        "{t}Agora eu faço, [p=0.2] ao vivo, [p=0.2] no rascunho. [p=0.3] {a}Este é o primeiro parágrafo de desenvolvimento "
        "da redação do estigma: [p=0.2] o eixo da *desinformação.* [p=0.3] {b}Foi elaborado para fins didáticos. [p=0.3] "
        "Vou ler devagar."),
    dict(id="16", block="eufaco", text=
        "{s1}Em primeiro lugar, [p=0.2] a desinformação sobre os transtornos mentais sustenta o estigma que os cerca. "
        "[p=0.4] {s2}Como pouco se discute saúde mental nas escolas e nas famílias, [p=0.2] sintomas como a tristeza "
        "persistente ou a ansiedade intensa [p=0.2] costumam ser interpretados como fraqueza de caráter, [p=0.2] e não como "
        "condições que têm tratamento. [p=0.4] {s3}Essa confusão tem raízes antigas: [p=0.2] em O Alienista, [p=0.2] "
        "Machado de Assis satiriza o médico Simão Bacamarte, [p=0.2] que, com critérios arbitrários, [p=0.2] recolhe à "
        "Casa Verde a maior parte da população de Itaguaí, [p=0.2] mostrando como o rótulo de louco podia servir para "
        "excluir."),
    dict(id="17", block="eufaco", text=
        "{s4}Mais de um século depois, [p=0.2] os critérios mudaram, [p=0.2] mas a lógica persiste: [p=0.2] quem sofre "
        "psiquicamente ainda é visto como alguém a ser afastado, [p=0.2] e não cuidado, [p=0.2] o que leva muitos a adiar a "
        "busca por ajuda por medo do julgamento. [p=0.4] {s5}Dessa forma, [p=0.2] enquanto a informação não substituir o "
        "preconceito, [p=0.2] o estigma continuará a afastar os brasileiros do tratamento. [p=0.6] {m}Agora, [p=0.2] as "
        "cores. [p=0.3] {c1}A primeira frase *afirma:* [p=0.2] etiqueta. [p=0.3] {c2}A segunda explica o *porquê.* [p=0.3] "
        "{c3}A terceira traz a *nota fiscal:* [p=0.2] O Alienista. [p=0.3] {c4}A quarta mostra o produto funcionando [p=0.2] "
        "no Brasil de *hoje.* [p=0.3] {c5}E a quinta assina o *recibo.* [p=0.4] {v}A análise frase por frase [p=0.2] volta "
        "no episódio cinco."),

    # ================= EXEMPLO × CONTRAEXEMPLO =================
    dict(id="18", block="lado", text=
        "{t}Agora compare com este outro parágrafo, [p=0.2] para o mesmo eixo. [p=0.3] {a}Em primeiro lugar, [p=0.2] a "
        "desinformação é um grande problema. [p=0.2] Muitas pessoas não sabem nada sobre doenças mentais e isso é muito "
        "ruim. [p=0.2] As pessoas deveriam se informar mais. [p=0.2] Dessa forma, [p=0.2] a desinformação precisa acabar. "
        "[p=0.5] {b}Tem etiqueta? [p=0.2] Tem. [p=0.2] Tem recibo? [p=0.2] Tem. [p=0.4] {c}Mas o meio só *repete* a mesma "
        "opinião: [p=0.2] {d}sem porquê, [p=0.2] {e}sem nota fiscal, [p=0.2] {f}sem produto funcionando. [p=0.4] {g}É a "
        "caixa deixada *fechada* na calçada."),

    # ================= RECAPITULAÇÃO DO MEIO =================
    dict(id="19", block="recap", text=
        "{t}Três frases para guardar. [p=0.3] {a}Cada parágrafo entrega um item da lista. [p=0.6] {b}Etiqueta, [p=0.2] por "
        "quê, [p=0.2] nota fiscal, [p=0.2] produto funcionando, [p=0.2] recibo. [p=0.6] {c}Cinco partes é *método;* [p=0.2] "
        "o raciocínio é que não pode faltar. [p=0.5]"),

    # ================= NÓS FAZEMOS =================
    dict(id="20", block="exercicio", text=
        "{t}Sua vez. [p=0.2] Aqui está o mesmo parágrafo, [p=0.2] agora *sem as cores.* [p=0.3] {a}Pause o vídeo [p=0.2] e "
        "escreva, ao lado de cada frase, [p=0.2] qual etapa da entrega ela é: [p=0.2] etiqueta, [p=0.2] por quê, [p=0.2] "
        "nota fiscal, [p=0.2] produto funcionando [p=0.2] ou recibo. [p=0.3] {p}Pause agora. [p=2.0]"),
    dict(id="21", block="exercicio", text=
        "{a}Conferindo. [p=0.3] {s1}Frase um, [p=0.2] *Em primeiro lugar:* [p=0.2] a etiqueta. [p=0.3] {s2}Frase dois, "
        "[p=0.2] *Como pouco se discute:* [p=0.2] o porquê. [p=0.3] {s3}Frase três, [p=0.2] *O Alienista:* [p=0.2] a nota "
        "fiscal. [p=0.3] {s4}Frase quatro, [p=0.2] *Mais de um século depois:* [p=0.2] o produto funcionando. [p=0.3] "
        "{s5}Frase cinco, [p=0.2] *Dessa forma:* [p=0.2] o recibo. [p=0.4] {d}Acertou as cinco? [p=0.2] Então você já "
        "enxerga a *arquitetura* do parágrafo."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erros", text=
        "{a}Erro um: [p=0.2] achar que desenvolver é *dar mais opiniões.* [p=0.4] {b}Parece certo, [p=0.2] porque o "
        "parágrafo fica mais cheio. [p=0.4] {c}Mas opinião repetida não é argumento: [p=0.2] depois de afirmar, [p=0.2] é "
        "preciso explicar, [p=0.2] comprovar [p=0.2] e analisar."),
    dict(id="23", block="erros", text=
        "{a}Erro dois: [p=0.2] achar que a ordem das cinco partes é *obrigatória.* [p=0.4] {b}Parece certo, [p=0.2] porque "
        "o modelo vem sempre na mesma sequência. [p=0.4] {c}Mas é método: [p=0.2] a ordem pode variar, [p=0.2] duas partes "
        "cabem numa frase. [p=0.2] O que não pode faltar é o *raciocínio.*"),
    dict(id="24", block="erros", text=
        "{a}Erro três: [p=0.2] gastar o parágrafo com a referência [p=0.2] e *não analisar.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque citar uma obra famosa impressiona. [p=0.4] {c}Mas o repertório só é produtivo com análise: [p=0.2] "
        "é na análise que aparece a autoria."),

    # ================= QUESTÃO 6 =================
    dict(id="25", block="q6", text=
        "{t}Agora, [p=0.2] uma questão no estilo do ENEM. [p=0.3] {a}Sobre a estrutura tópico frasal, [p=0.2] argumento, "
        "[p=0.2] repertório, [p=0.2] análise [p=0.2] e fechamento, [p=0.2] é correto afirmar que: [p=0.4] {A}A: [p=0.2] é "
        "exigida pela Cartilha do Participante, [p=0.2] e a falta de qualquer parte zera a Competência três. [p=0.4] {B}B: "
        "[p=0.2] vale só para o primeiro parágrafo de desenvolvimento. [p=0.4] {C}C: [p=0.2] proíbe que o repertório "
        "apareça antes da explicação do argumento."),
    dict(id="26", block="q6", text=
        "{D}D: [p=0.2] dispensa o repertório, [p=0.2] desde que o parágrafo tenha análise. [p=0.4] {E}E: [p=0.2] é um "
        "método de estudo: [p=0.2] as partes podem variar de ordem, [p=0.2] mas os descritores avaliam se as informações "
        "estão relacionadas ao tema, [p=0.2] organizadas e desenvolvidas em defesa de um ponto de vista. [p=0.4] {p}Pause o "
        "vídeo e tente! [p=2.0]"),
    dict(id="27", block="q6", text=
        "{ok}Letra *E!* [p=0.3] A estrutura é um método [p=0.2] que ajuda a cumprir o que os descritores da C três "
        "avaliam. [p=0.2] Não há na Cartilha uma ordem obrigatória de frases. [p=0.4] {xa}A A inventa uma regra [p=0.2] e "
        "uma *punição.* [p=0.3] {xb}A B restringe o método sem motivo. [p=0.3] {xc}A C transforma sugestão em *proibição.* "
        "[p=0.3] {xd}E a D contraria a C dois: [p=0.2] o repertório produtivo é o que o descritor do nível mais alto "
        "menciona."),

    # ================= RECAPITULAÇÃO FINAL E PONTE =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, [p=0.2] as mesmas três frases. [p=0.3] {a}Cada parágrafo entrega um item da lista. [p=0.6] "
        "{b}Etiqueta, [p=0.2] por quê, [p=0.2] nota fiscal, [p=0.2] produto funcionando, [p=0.2] recibo. [p=0.6] {c}Cinco "
        "partes é *método;* [p=0.2] o raciocínio é que não pode faltar. [p=0.5]"),
    dict(id="29", block="ponte", text=
        "{a}Toda entrega começa pela *etiqueta* do item. [p=0.4] {b}Se ela estiver vaga, [p=0.2] ninguém sabe o que "
        "chegou. [p=0.4] {c}Próximo episódio: [p=0.2] o *tópico frasal.*"),

    # ================= CTA =================
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual das cinco etapas da entrega o seu parágrafo costuma esquecer? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
