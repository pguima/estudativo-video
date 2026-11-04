# Roteiro — Redação ENEM, Desenvolvimento, Episódio 5 de 7: O parágrafo-modelo comentado e do fraco ao bom
# Base: Estudos/Enem/estudos/06-redacao/03-desenvolvimento.html — seções 08 e 09 + Questão 7 da seção 12.
#   Eu faço: o parágrafo-modelo da seção 08 lido frase por frase com a tabela "Frase | Função | O que observar";
#   as duas colunas D1 (desinformação) × D2 (mídia); as Versões 1 e 2 da seção 09 com o checklist da entrega; a Versão 3
#   (= o modelo) e "O que mudou". Nós fazemos: escrever a frase [2] que falta na Versão 1.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora da SÉRIE: cada parágrafo de desenvolvimento ENTREGA UM ITEM da lista colada na caixa, em cinco etapas —
#   ETIQUETA DO ITEM (tópico frasal) · POR QUE ESTÁ NA CAIXA (argumento) · NOTA FISCAL (repertório) · PRODUTO
#   FUNCIONANDO na casa do cliente (análise) · RECIBO ASSINADO (fechamento). Aqui: três entregadores do mesmo item (o que
#   só repete "é um ótimo produto", o que mostra a nota fiscal e vai embora, o que faz a entrega completa) = as três versões.
# Frases-chave (meio e fim, idênticas):
#   1. Cinco frases, cinco trabalhos.  2. Repetir não é explicar; mencionar não é usar.
#   3. Dois parágrafos, a mesma arquitetura, a mesma tese.
# FIDELIDADE: lidos EXATAMENTE como no material: a tese (05), o parágrafo-modelo [1]–[5] (07–13), a tabela (14), a
#   Versão 1 (17), a Versão 2 (19), "O que mudou" (23) e a Questão 7 (30–33), sempre com "elaborado para fins didáticos"
#   na tela. Só as referências do material: O Alienista (Machado de Assis, Simão Bacamarte, Casa Verde, Itaguaí) e a
#   Lei nº 10.436/2002 (Questão 7). "Teste da retirada" com o mesmo nome da série Introdução (ep. 3). Nenhum nível ou nota
#   da C3. Números e anos falados por extenso.
# Cores: azul = definição · verde = dica/método · âmbar = armadilha · vermelho = erro · roxo = regra oficial (Cartilha).

TITULO = "O Mesmo Parágrafo do Fraco ao Bom: o Parágrafo-Modelo Comentado | Desenvolvimento da Redação Ep. 5"
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
    # ================= GANCHO, AS TRÊS ENTREGAS E PROMESSA =================
    dict(id="01", block="hook", text=
        "{a}Este é o primeiro parágrafo de desenvolvimento [p=0.2] da redação que começamos na série de *Introdução.* "
        "[p=0.4] {b}*Cinco frases.* [p=0.4] {c}Cada uma tem um *trabalho,* [p=0.3] {d}e se uma faltar, [p=0.2] você vai "
        "*perceber.*"),
    dict(id="02", block="entregas", text=
        "{t}Antes, [p=0.2] imagine três entregadores [p=0.2] levando o *mesmo* item. [p=0.4] {a}O primeiro só repete: "
        "[p=0.2] é um ótimo produto, [p=0.2] é um ótimo produto. [p=0.2] E vai embora. [p=0.4] {b}O segundo mostra a *nota "
        "fiscal* [p=0.2] e também vai embora. [p=0.4] {c}O terceiro faz a entrega *completa:* [p=0.2] etiqueta, [p=0.2] por "
        "quê, [p=0.2] nota fiscal, [p=0.2] produto funcionando [p=0.2] e recibo assinado. [p=0.4] {d}Hoje, [p=0.2] esses "
        "três entregadores [p=0.2] viram *três parágrafos.*"),
    dict(id="03", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai *reconhecer as cinco partes* em qualquer parágrafo [p=0.3] {b}e saber "
        "*consertar* um parágrafo fraco. [p=0.4] {c}E calma: [p=0.2] cada palavra nova vai ser explicada, [p=0.2] uma de "
        "cada vez."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="04", block="prereq", text=
        "{t}Revisão relâmpago dos episódios anteriores. [p=0.3] {a}Todo parágrafo de desenvolvimento tem *cinco partes.* "
        "[p=0.3] {b}O *tópico frasal* anuncia o que o parágrafo vai provar. [p=0.3] {c}A *análise* mostra o que a "
        "referência revela sobre o problema. [p=0.3] {d}E o *fechamento* responde ao *e daí?,* [p=0.2] ligando tudo à "
        "tese."),
    dict(id="05", block="prereq", text=
        "{t}E esta é a tese que guardamos na série *Introdução,* [p=0.2] para o tema de dois mil e vinte. [p=0.3] {a}No "
        "Brasil, [p=0.2] o estigma associado às doenças mentais persiste [p=0.2] em razão da desinformação sobre os "
        "transtornos [p=0.2] e de representações midiáticas que associam o adoecimento psíquico à violência. [p=0.4] "
        "{b}Dois eixos: [p=0.2] a *desinformação* [p=0.2] {c}e a *mídia.*"),

    # ================= BLOCO A — EU FAÇO: O PARÁGRAFO-MODELO, FRASE POR FRASE =================
    dict(id="06", block="eufaco", text=
        "{t}Então, [p=0.2] o que cada uma dessas cinco frases está fazendo ali? [p=0.4] {a}Vamos ler o "
        "*parágrafo-modelo:* [p=0.2] um parágrafo pronto, [p=0.2] feito para você observar *como* ele foi construído. "
        "[p=0.4] {b}Ele foi elaborado para fins didáticos [p=0.2] e cumpre o eixo da *desinformação.* [p=0.3] {c}Uma "
        "frase de cada vez."),
    dict(id="07", block="eufaco", text=
        "{s1}Frase um. [p=0.2] Em primeiro lugar, [p=0.2] a desinformação sobre os transtornos mentais sustenta o estigma "
        "que os cerca. [p=0.5] {f}Função: [p=0.2] *tópico frasal.* [p=0.3] {o1}Repare no começo: [p=0.2] *em primeiro "
        "lugar* é um conectivo de *ordenação,* [p=0.2] uma expressão que marca a posição na sequência. [p=0.4] {o2}E repare "
        "no assunto: [p=0.2] é o *eixo um* da tese, [p=0.2] a desinformação. [p=0.3] {e}É a *etiqueta* do item."),
    dict(id="08", block="eufaco", text=
        "{s2}Frase dois. [p=0.2] Como pouco se discute saúde mental nas escolas e nas famílias, [p=0.2] sintomas como a "
        "tristeza persistente ou a ansiedade intensa [p=0.2] costumam ser interpretados como fraqueza de caráter, [p=0.2] e "
        "não como condições que têm tratamento. [p=0.5] {f}Função: [p=0.2] *argumento.* [p=0.3] {o1}Aqui tem uma *causa:* "
        "[p=0.2] como pouco se discute. [p=0.3] {o2}E tem um *efeito:* [p=0.2] a tristeza é lida como fraqueza. [p=0.3] "
        "{e}É o *porquê* de o item estar na caixa."),
    dict(id="09", block="eufaco", text=
        "{s3}Frase três. [p=0.2] Essa confusão tem raízes antigas: [p=0.2] em O Alienista, [p=0.2] Machado de Assis "
        "satiriza o médico Simão Bacamarte, [p=0.2] que, com critérios arbitrários, [p=0.2] recolhe à Casa Verde a maior "
        "parte da população de Itaguaí, [p=0.2] mostrando como o rótulo de louco podia servir para excluir. [p=0.5] "
        "{f}Função: [p=0.2] *repertório.* [p=0.3] {e}A *nota fiscal* do item."),
    dict(id="10", block="eufaco", text=
        "{t}Mas por que essa nota fiscal vale? [p=0.4] {o1}Primeiro: [p=0.2] é uma obra de *domínio público,* [p=0.2] um "
        "clássico que qualquer pessoa pode ler e conferir. [p=0.4] {o2}Segundo: [p=0.2] a atribuição está *correta:* "
        "[p=0.2] O Alienista é mesmo de Machado de Assis. [p=0.4] {o3}Terceiro: [p=0.2] o conteúdo vem em *paráfrase.* "
        "[p=0.3] Paráfrase é contar, com as suas palavras, [p=0.2] o que a obra mostra. [p=0.4] {e}A frase não só diz o nome "
        "do livro: [p=0.2] ela conta o que *acontece* nele."),
    dict(id="11", block="eufaco", text=
        "{s4}Frase quatro. [p=0.2] Mais de um século depois, [p=0.2] os critérios mudaram, [p=0.2] mas a lógica persiste: "
        "[p=0.2] quem sofre psiquicamente ainda é visto como alguém a ser afastado, [p=0.2] e não cuidado, [p=0.2] o que "
        "leva muitos a adiar a busca por ajuda por medo do julgamento. [p=0.5] {f}Função: [p=0.2] *análise.*"),
    dict(id="12", block="eufaco", text=
        "{t}E o que essa frase faz que a anterior não fazia? [p=0.4] {o1}Ela *atualiza* a referência: [p=0.2] *mais de um "
        "século depois.* [p=0.3] Atualizar é trazer o que a obra mostra [p=0.2] para o Brasil de *hoje.* [p=0.4] {o2}E ela "
        "mostra a *consequência concreta:* [p=0.2] muita gente adia a busca por ajuda. [p=0.4] {e}É o *produto "
        "funcionando* na casa do cliente."),
    dict(id="13", block="eufaco", text=
        "{s5}Frase cinco. [p=0.2] Dessa forma, [p=0.2] enquanto a informação não substituir o preconceito, [p=0.2] o "
        "estigma continuará a afastar os brasileiros do tratamento. [p=0.5] {f}Função: [p=0.2] *fechamento.* [p=0.3] "
        "{o1}Ela retoma o eixo, [p=0.2] a *informação,* [p=0.2] {o2}e o liga à tese: [p=0.2] o *estigma.* [p=0.3] {o3}E "
        "repare: [p=0.2] *nenhuma* informação nova. [p=0.3] {e}É o *recibo assinado.*"),
    dict(id="14", block="tabela", text=
        "{t}Agora, [p=0.2] tudo numa tabela só. [p=0.3] {a}Frase, [p=0.2] função [p=0.2] e o que observar. [p=0.4] "
        "{b}Cinco frases, [p=0.2] cinco funções diferentes. [p=0.3] {c}Nenhuma faz o trabalho da outra."),

    # ================= BLOCO B — DOIS PARÁGRAFOS, A MESMA ARQUITETURA =================
    dict(id="15", block="arquitetura", text=
        "{t}E o segundo parágrafo? [p=0.2] Começa do zero? [p=0.4] {a}Não. [p=0.2] Ele usa a *mesma arquitetura:* [p=0.2] "
        "a mesma sequência de cinco partes. [p=0.4] {b}O primeiro desenvolvimento cumpre o eixo da *desinformação.* [p=0.3] "
        "{c}O segundo, [p=0.2] o eixo da *mídia.* [p=0.4] {d}Cada um abre com um conectivo de *progressão,* [p=0.2] que "
        "mostra que o texto avança: [p=0.2] {d1}em primeiro lugar, [p=0.2] {d2}além disso."),
    dict(id="16", block="arquitetura", text=
        "{a}E cada um *fecha* apontando para a tese. [p=0.4] {b}Repare nas duas setas. [p=0.3] Quando os dois fechamentos "
        "convergem para a mesma posição, [p=0.2] {c}o leitor percebe o *projeto de texto:* [p=0.2] o plano que liga a "
        "redação inteira. [p=0.4] {d}Item A, [p=0.2] item B, [p=0.2] a mesma caixa."),

    # ================= BLOCO C — VERSÃO 1: SÓ OPINIÃO =================
    dict(id="17", block="v1", text=
        "{t}E como fica este mesmo eixo [p=0.2] quando o parágrafo dá errado? [p=0.4] {a}Versão um: [p=0.2] *só "
        "opinião.* [p=0.3] {b}Em primeiro lugar, [p=0.2] a desinformação é um grande problema. [p=0.2] Muitas pessoas não "
        "sabem nada sobre doenças mentais e isso é muito ruim. [p=0.2] As pessoas deveriam se informar mais. [p=0.2] Dessa "
        "forma, [p=0.2] a desinformação precisa acabar."),
    dict(id="18", block="v1", text=
        "{a}Tem tópico frasal? [p=0.2] Tem. [p=0.2] Tem fechamento? [p=0.2] Tem. [p=0.4] "
        "{b}Mas o meio *repete* a mesma ideia com outras palavras: [p=0.3] {c}não há explicação de causa, [p=0.2] "
        "{d}nenhum repertório [p=0.2] {e}e nenhuma análise. [p=0.4] {f}Pelos descritores, [p=0.2] as frases da grade de "
        "correção, [p=0.2] isso tende a informações pouco desenvolvidas, [p=0.2] com *argumentação previsível:* [p=0.2] a "
        "que só diz o óbvio, [p=0.2] sem explicar nem provar. [p=0.4] {g}É o entregador que só repete: [p=0.2] ótimo "
        "produto."),

    # ================= BLOCO D — VERSÃO 2: REPERTÓRIO SOLTO =================
    dict(id="19", block="v2", text=
        "{t}Então basta colocar uma referência? [p=0.4] {a}Versão dois: [p=0.2] *repertório solto.* [p=0.3] {b}Em "
        "primeiro lugar, [p=0.2] a desinformação sustenta o estigma. [p=0.2] Machado de Assis escreveu O Alienista, [p=0.2] "
        "obra muito importante da literatura brasileira. [p=0.2] Dessa forma, [p=0.2] o estigma das doenças mentais "
        "continua no Brasil."),
    dict(id="20", block="v2", text=
        "{a}A referência é *legítima* [p=0.2] e até *pertinente:* [p=0.2] a obra existe e tem a ver com o tema. [p=0.4] "
        "{b}Mas ela é apenas *mencionada.* [p=0.3] O texto não diz o que a obra mostra, [p=0.2] nem como isso se liga ao "
        "problema. [p=0.4] {c}Lembra do *teste da retirada,* [p=0.2] da série Introdução? [p=0.3] Se a referência sai e "
        "nada muda, [p=0.2] ela não estava trabalhando. [p=0.4] {x}Vamos tirar."),
    dict(id="21", block="v2", text=
        "{a}Em primeiro lugar, [p=0.2] a desinformação sustenta o estigma. [p=0.3] Dessa forma, [p=0.2] o estigma das "
        "doenças mentais continua no Brasil. [p=0.5] {b}Fez falta? [p=0.3] *Nenhuma.* [p=0.4] {c}É o tipo de uso que a "
        "Cartilha do Participante, [p=0.2] o guia oficial da redação, [p=0.2] considera *não produtivo:* [p=0.2] repertório "
        "que está no texto, [p=0.2] mas não trabalha pelo argumento. [p=0.4] {d}É o entregador que mostra a nota fiscal "
        "[p=0.2] e vai embora."),

    # ================= BLOCO E — VERSÃO 3 E O QUE MUDOU =================
    dict(id="22", block="tres", text=
        "{t}E a versão três? [p=0.4] {a}É o *parágrafo-modelo* que você acabou de ler: [p=0.2] a mesma obra, [p=0.2] "
        "agora resumida, [p=0.2] atualizada e ligada à tese. [p=0.4] {b}Agora, [p=0.2] as três lado a lado. "
        "[p=0.3] {c}A versão um entrega só duas etapas. [p=0.3] {d}A versão dois cita a obra, [p=0.2] mas a nota fiscal "
        "não trabalha. [p=0.3] {e}A versão três entrega *tudo.*"),
    dict(id="23", block="mudou", text=
        "{t}O que mudou, exatamente? [p=0.4] {a}A repetição [p=0.2] virou *explicação causal.* [p=0.4] {b}A menção [p=0.2] "
        "virou *conteúdo da referência.* [p=0.4] {c}E o salto direto para o fechamento [p=0.2] virou *análise* que conecta "
        "passado e presente."),

    # ================= NÓS FAZEMOS =================
    dict(id="24", block="exercicio", text=
        "{t}Sua vez. [p=0.2] Aqui está a versão um de novo. [p=0.3] {a}Falta o porquê. [p=0.3] {b}Pause o vídeo [p=0.2] e escreva a frase *dois* que falta: [p=0.2] o *porquê,* "
        "[p=0.2] com causa e consequência. [p=0.3] {p}Pause agora. [p=2.0]"),
    dict(id="25", block="exercicio", text=
        "{a}Agora compare com a frase dois do modelo, [p=0.2] {s}aqui na tela. [p=0.6] {b}A sua frase tem uma "
        "*causa?* [p=0.3] {c}E um *efeito?* [p=0.3] {d}Então você explicou, [p=0.2] em vez de repetir. [p=0.2] Não precisa "
        "ser igual: [p=0.2] precisa fazer o *mesmo trabalho.*"),

    # ================= RECAPITULAÇÃO DO MEIO =================
    dict(id="26", block="recap", text=
        "{t}Três frases para guardar. [p=0.3] {a}Cinco frases, [p=0.2] cinco trabalhos. [p=0.6] {b}Repetir não é explicar; "
        "[p=0.2] mencionar não é usar. [p=0.6] {c}Dois parágrafos, [p=0.2] a mesma arquitetura, [p=0.2] a mesma tese. "
        "[p=0.5]"),

    # ================= ERROS CLÁSSICOS =================
    dict(id="27", block="erros", text=
        "{a}Erro um: [p=0.2] *misturar os dois eixos* no mesmo parágrafo. [p=0.4] {b}Parece certo, [p=0.2] porque o "
        "parágrafo fica mais cheio de ideias. [p=0.4] {c}Mas cada parágrafo entrega *um* item: [p=0.2] a desinformação num, "
        "[p=0.2] a mídia no outro."),
    dict(id="28", block="erros", text=
        "{a}Erro dois: [p=0.2] *repetir* no segundo parágrafo o argumento do primeiro. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque insistir na ideia parece reforçar a tese. [p=0.4] {c}Mas o segundo parágrafo entrega o *outro* item: "
        "[p=0.2] mesma arquitetura, [p=0.2] eixo novo."),
    dict(id="29", block="erros", text=
        "{a}Erro três: [p=0.2] achar que um parágrafo *com citação* já é bom. [p=0.4] {b}Parece certo, [p=0.2] porque "
        "citar uma obra famosa impressiona. [p=0.4] {c}Mas mencionar não é usar: [p=0.2] a referência precisa de conteúdo "
        "e de análise. [p=0.2] Faça o teste da retirada."),

    # ================= QUESTÃO 7 =================
    dict(id="30", block="q7", text=
        "{t}Agora, [p=0.2] uma questão no estilo do ENEM, [p=0.2] sobre o tema de dois mil e dezessete: [p=0.2] a formação "
        "educacional de surdos. [p=0.3] {a}Estas frases estão fora de ordem. [p=0.2] Libras é a Língua Brasileira de "
        "Sinais. [p=0.3] {f1}Um: [p=0.2] Assim, [p=0.2] sem professores preparados em Libras, [p=0.2] a escola continua "
        "excluindo quem deveria acolher. [p=0.3] {f2}Dois: [p=0.2] Em primeiro lugar, [p=0.2] a falta de formação dos "
        "professores em Libras [p=0.2] compromete a educação de estudantes surdos. [p=0.3] {f3}Três: [p=0.2] A Lei número "
        "dez mil quatrocentos e trinta e seis, de dois mil e dois, [p=0.2] reconhece a Língua Brasileira de Sinais [p=0.2] "
        "como meio legal de comunicação e expressão."),
    dict(id="31", block="q7", text=
        "{f4}Quatro: [p=0.2] Isso ocorre porque, [p=0.2] sem domínio da língua de sinais, [p=0.2] o docente não consegue "
        "explicar os conteúdos ao aluno surdo. [p=0.3] {f5}Cinco: [p=0.2] Apesar desse reconhecimento, [p=0.2] muitas "
        "escolas ainda não contam com professores ou intérpretes capazes de usá-la, [p=0.2] o que deixa o aluno surdo à "
        "margem das aulas. [p=0.4] {q}A sequência que segue o modelo [p=0.2] tópico frasal, [p=0.2] argumento, [p=0.2] "
        "repertório, [p=0.2] análise [p=0.2] e fechamento é: [p=0.3] {A}A: [p=0.2] dois, quatro, três, cinco, um. [p=0.3] "
        "{B}B: [p=0.2] três, dois, quatro, um, cinco. [p=0.3] {C}C: [p=0.2] dois, três, um, quatro, cinco. [p=0.3] {D}D: "
        "[p=0.2] um, dois, três, quatro, cinco. [p=0.3] {E}E: [p=0.2] quatro, dois, cinco, três, um. [p=0.4] {p}Pause o "
        "vídeo, [p=0.2] numere as frases no seu papel e tente! [p=2.0]"),
    dict(id="32", block="q7", text=
        "{ok}Letra *A!* [p=0.3] A ordem certa é dois, quatro, três, cinco e um. [p=0.4] {e1}A frase dois anuncia o "
        "argumento: [p=0.2] é a *etiqueta.* [p=0.3] {e2}A frase quatro explica o porquê, [p=0.2] com *isso ocorre porque:* "
        "[p=0.2] é o argumento. [p=0.3] {e3}A frase três traz a lei: [p=0.2] é a *nota fiscal.* [p=0.3] {e4}A frase cinco "
        "confronta a lei com a realidade: [p=0.2] é o *produto funcionando.* [p=0.3] {e5}E a frase um fecha com *assim:* "
        "[p=0.2] é o *recibo.*"),
    dict(id="33", block="q7", text=
        "{t}E por que a cinco só pode vir *depois* da lei? [p=0.4] {a}Porque *apesar desse reconhecimento* retoma algo já "
        "dito: [p=0.3] {b}o reconhecimento da Libras, [p=0.2] pela lei da frase três. [p=0.4] {c}Sem a lei "
        "antes, [p=0.2] essa expressão aponta para o nada. [p=0.4] {xb}A B começa pelo repertório [p=0.2] e põe o "
        "fechamento antes da análise. [p=0.3] {xc}A C põe o fechamento no meio. [p=0.3] {xd}A D começa pelo fechamento. "
        "[p=0.3] {xe}E a E abre com *isso ocorre porque,* [p=0.2] que retoma uma afirmação ainda não feita."),

    # ================= RECAPITULAÇÃO FINAL E PONTE =================
    dict(id="34", block="recap", text=
        "{t}Para fechar, [p=0.2] as mesmas três frases. [p=0.3] {a}Cinco frases, [p=0.2] cinco trabalhos. [p=0.6] "
        "{b}Repetir não é explicar; [p=0.2] mencionar não é usar. [p=0.6] {c}Dois parágrafos, [p=0.2] a mesma arquitetura, "
        "[p=0.2] a mesma tese. [p=0.5]"),
    dict(id="35", block="ponte", text=
        "{a}O primeiro parágrafo está *pronto.* [p=0.4] {b}O segundo, [p=0.2] sobre a *mídia,* [p=0.2] vamos escrever "
        "juntos, [p=0.2] {c}do rascunho ao texto, [p=0.2] no próximo episódio."),

    # ================= CTA =================
    dict(id="36", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual das três versões parece mais com os parágrafos que você escreve? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
