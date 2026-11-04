# Roteiro — Redação ENEM, Introdução, Episódio 1 de 7: Da tese ao primeiro parágrafo — os três movimentos da introdução
# Base: Estudos/Enem/estudos/06-redacao/02-introducao.html — seções 01 e 02 + Questão 6 da seção 12.
#   Modelagem com a Versão 3 da seção 07 (só para marcar os movimentos; a análise completa fica no ep. 5) e contraexemplo
#   com a Versão 1 da seção 07. Competências só citadas (C2, C3 e C4, uma frase cada, como na tabela da seção 02).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora da SÉRIE: a introdução é a ETIQUETA COMPLETA DA ENCOMENDA — MAPA = contextualização (de onde parte a
#   entrega) · ENDEREÇO + ENTREGA = tese · LISTA DA CAIXA = antecipação dos argumentos. (A RUA DE ACESSO, a ponte, entra
#   no ep. 3; aqui a etiqueta tem só 3 faixas.) Liga à série Leitura da proposta: frase temática = endereço, tese = o que
#   você entrega.
# Frases-chave (meio e fim, idênticas):
#   1. Mapa, endereço, lista da caixa.  2. De onde parte? O que defende? Por quais caminhos?
#   3. Três movimentos é método, não regra.
# FIDELIDADE: o modelo em três movimentos é MÉTODO DE ESTUDO, não critério do Inep (cenas 11–12, erro 2 e Questão 6).
#   Lidos EXATAMENTE como no material: orientação da Cartilha (07), descrição das redações de nota alta (07), Versão 3
#   (14–15) e Versão 1 (16) da seção 07, Questão 6 (23–24). Números e anos falados por extenso.
# Cores: azul = definição/tema · verde = dica/método · âmbar = armadilha · vermelho = erro/penalidade ·
#   roxo = regra oficial (Cartilha). Peças: mapa azul · tese laranja-telha · lista azul-petróleo.

TITULO = "As 3 Perguntas que o 1º Parágrafo da Redação Precisa Responder | Introdução da Redação Ep. 1"
# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo da folha em branco: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa nas armadilhas ('Parece certo... mas não é!'); comemore os acertos com "
            "entusiasmo ('Letra B!'); dê ênfase forte às palavras-chave. Quando ler a introdução no rascunho, leia como "
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
        "{a}O primeiro parágrafo é o *mais lido* da sua redação. [p=0.4] {b}Uma introdução que serviria para *qualquer "
        "tema* [p=0.2] desperdiça essas linhas. [p=0.4] {c}Uma introdução bem montada [p=0.2] já mostra ao corretor [p=0.2] "
        "*para onde o seu texto vai.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai saber quais são as *três tarefas* do primeiro parágrafo [p=0.3] {b}e que "
        "*pergunta do leitor* cada uma responde. [p=0.4] {c}E calma: [p=0.2] cada palavra nova vai ser explicada, [p=0.2] "
        "uma de cada vez."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Antes, [p=0.2] uma revisão relâmpago da série *Leitura da proposta.* [p=0.3] {a}O *tema* é o recorte exato que a "
        "prova dá: [p=0.2] o endereço de entrega. [p=0.3] {b}A *tese* é a sua posição sobre ele: [p=0.2] o que você entrega. "
        "[p=0.3] {c}E a gente terminou com uma *tese provisória* com *dois eixos:* [p=0.2] eixo é cada caminho que sustenta "
        "a sua posição. [p=0.4] {d}Se você viu a série de Linguagens sobre compreensão global e tese, [p=0.2] já conhece essa "
        "ideia. [p=0.3] {e}Agora, [p=0.2] vamos escrever a *etiqueta inteira.*"),

    # ================= A ETIQUETA COMPLETA =================
    dict(id="04", block="etiqueta", text=
        "{t}Pense numa encomenda que chega certinho. [p=0.3] {a}A etiqueta dela tem *tudo:* [p=0.3] {b}um *mapa* da região, "
        "[p=0.2] que mostra de onde parte a entrega; [p=0.3] {c}o *endereço,* [p=0.2] com o que vai ser entregue; [p=0.3] "
        "{d}e uma *lista* colada na caixa, [p=0.2] dizendo quais itens vão chegar. [p=0.4] {e}Com essa etiqueta, [p=0.2] "
        "ninguém se perde."),
    dict(id="05", block="etiqueta", text=
        "{t}A *introdução,* [p=0.2] o primeiro parágrafo da redação, [p=0.2] é essa *etiqueta completa.* [p=0.4] {a}O mapa é "
        "a *contextualização:* [p=0.2] o trecho que situa o problema. [p=0.4] {b}O endereço, com o que você entrega, [p=0.2] "
        "é a *tese.* [p=0.4] {c}E a lista da caixa é a *antecipação dos argumentos:* [p=0.2] o anúncio dos eixos [p=0.2] que "
        "o *desenvolvimento* vai provar. [p=0.4] {d}Desenvolvimento é o miolo da redação: [p=0.2] os parágrafos entre a "
        "introdução e a conclusão."),

    # ================= BLOCO A: A INTRODUÇÃO É AVALIADA? =================
    dict(id="06", block="avalia", text=
        "{t}Mas espera: [p=0.2] a introdução ganha nota *sozinha?* [p=0.4] {a}Não. [p=0.2] Nenhum *descritor* oficial avalia "
        "a introdução isoladamente. [p=0.2] {d0}Descritor é a frase da grade de correção que descreve cada nível de nota. "
        "[p=0.4] {b}O *Inep,* [p=0.2] o órgão do governo que faz o ENEM, [p=0.2] corrige o *texto inteiro* pelas cinco "
        "competências. [p=0.4] {c}Só que é na introdução que o corretor começa a perceber três coisas: [p=0.3] {d}o seu "
        "*ponto de vista;* [p=0.3] {e}o seu *projeto de texto,* [p=0.2] que é o plano da redação; [p=0.3] {f}e o seu "
        "*primeiro repertório,* [p=0.2] o conhecimento de fora que você traz."),

    # ================= BLOCOS B E C: A CARTILHA =================
    dict(id="07", block="cartilha", text=
        "{t}E o que diz a *Cartilha do Participante,* [p=0.2] o guia oficial da redação, [p=0.2] publicado pelo Inep? "
        "[p=0.4] {a}Ela resume a tarefa assim: [p=0.3] {b}inicie o texto apresentando seu ponto de vista, [p=0.2] {b2}desenvolva "
        "justificativas para comprová-lo [p=0.2] {b3}e elabore uma conclusão. [p=0.5] {c}E nos comentários das redações de "
        "nota alta, [p=0.2] a Cartilha de dois mil e vinte e seis repete a mesma descrição: [p=0.3] {d}na introdução, [p=0.2] "
        "são apresentadas *a contextualização,* [p=0.2] {d2}*a tese* [p=0.2] {d3}*e a antecipação dos argumentos.*"),

    # ================= BLOCO D: TRÊS PERGUNTAS DO LEITOR =================
    dict(id="08", block="perguntas", text=
        "{t}Então: [p=0.2] um parágrafo, [p=0.2] *três perguntas do leitor.* [p=0.4] {a}Primeira: [p=0.2] *de onde parte a "
        "discussão?* [p=0.3] {a2}Quem responde é a contextualização, [p=0.2] o *mapa.* [p=0.4] {b}Segunda: [p=0.2] *o que o "
        "autor defende?* [p=0.3] {b2}Quem responde é a tese: [p=0.2] o *endereço,* [p=0.2] com o que você entrega. [p=0.4] "
        "{c}Terceira: [p=0.2] *por quais caminhos ele vai provar isso?* [p=0.3] {c2}Quem responde é a antecipação: [p=0.2] "
        "a *lista da caixa.*"),

    # ================= BLOCO E: MOVIMENTO × COMPETÊNCIA =================
    dict(id="09", block="tabela", text=
        "{t}E cada movimento mexe com uma competência. [p=0.3] {a}A contextualização situa o problema com repertório "
        "pertinente: [p=0.2] *C dois.* [p=0.4] {b}A tese toma posição sobre o recorte completo: [p=0.2] *C dois* e *C três.* "
        "[p=0.4] {c}A antecipação anuncia os eixos: [p=0.2] é o projeto de texto, [p=0.2] *C três.* [p=0.4] {d}E ligar as "
        "partes com conectivos, [p=0.2] palavras como *porém* e *assim,* [p=0.2] é coesão: [p=0.2] *C quatro.* [p=0.4] {e}Cada "
        "competência vai ganhar a sua própria série."),

    # ================= BLOCO F: MÉTODO, NÃO REGRA =================
    dict(id="10", block="metodo", text=
        "{t}Agora, [p=0.2] um aviso importante. [p=0.3] {a}Essas três partes são um *método de estudo,* [p=0.2] *não* um "
        "critério do Inep. [p=0.4] {b}A Cartilha não exige número fixo de frases, [p=0.2] {b2}nem ordem obrigatória, [p=0.2] "
        "{b3}nem tamanho para a introdução. [p=0.4] {c}Esta barra mostra só a proporção *típica* de cada parte: [p=0.2] "
        "*não é regra.*"),
    dict(id="11", block="metodo", text=
        "{a}O que os descritores pedem [p=0.2] é que o texto tenha proposição, argumentação e conclusão, [p=0.2] na C dois, "
        "[p=0.2] {a2}e um projeto de texto perceptível, [p=0.2] na C três. [p=0.4] {b}Uma introdução que contextualiza e "
        "apresenta a tese, [p=0.2] mesmo sem anunciar eixos, [p=0.2] *pode funcionar.* [p=0.4] {c}O modelo só *reduz o "
        "risco* de você esquecer alguma coisa."),

    # ================= EU FAÇO: A VERSÃO 3 NO RASCUNHO =================
    dict(id="12", block="eufaco", text=
        "{t}Agora eu faço, [p=0.2] ao vivo, [p=0.2] no rascunho. [p=0.3] {a}O tema é de dois mil e vinte e quatro: [p=0.2] "
        "*Desafios para a valorização da herança africana no Brasil.* [p=0.4] {b}E esta é uma introdução boa, [p=0.2] "
        "elaborada para fins didáticos. [p=0.3] Vou ler devagar."),
    dict(id="13", block="eufaco", text=
        "{s1}Sancionada em dois mil e três, [p=0.2] a Lei número dez mil seiscentos e trinta e nove tornou obrigatório o ensino "
        "de história e cultura afro-brasileira nas escolas do país, [p=0.2] reconhecendo a contribuição africana na formação "
        "nacional. [p=0.4] {s2}Mais de duas décadas depois, porém, [p=0.2] essa herança ainda é frequentemente reduzida a "
        "estereótipos [p=0.2] ou lembrada apenas em datas comemorativas. [p=0.6] {m}Estas duas frases respondem: [p=0.2] *de "
        "onde parte a discussão?* [p=0.3] Uma lei, [p=0.2] e o que acontece na prática. [p=0.3] É o *mapa.*"),
    dict(id="14", block="eufaco", text=
        "{s3}Esse quadro decorre, sobretudo, [p=0.2] da aplicação irregular da lei nas escolas [p=0.2] e da "
        "pouca visibilidade da cultura afro-brasileira nos meios de comunicação, [p=0.2] obstáculos que precisam ser enfrentados para que "
        "essa herança seja, de fato, valorizada no Brasil. [p=0.6] {te}Esta frase responde: [p=0.2] *o que o autor "
        "defende?* [p=0.2] Que dois obstáculos impedem a valorização. [p=0.2] É o *endereço.* [p=0.4] {li}E ela já nomeia os "
        "dois eixos: [p=0.2] {l1}a escola [p=0.2] {l2}e a mídia. [p=0.3] É a *lista da caixa.* [p=0.4] {v}Essa "
        "versão volta no episódio cinco, [p=0.2] com a análise completa."),

    # ================= EXEMPLO × CONTRAEXEMPLO =================
    dict(id="15", block="lado", text=
        "{t}Agora compare com esta outra, [p=0.2] para o mesmo tema. [p=0.3] {a}Desde os primórdios da humanidade, [p=0.2] a "
        "cultura é fundamental para todos os povos. [p=0.2] Nesse sentido, [p=0.2] a herança africana também é importante e "
        "deve ser valorizada. [p=0.2] Portanto, [p=0.2] é necessário discutir esse tema. [p=0.5] {b}Tem mapa? [p=0.2] Não: "
        "[p=0.2] serve para *qualquer tema.* [p=0.3] {c}Tem endereço? [p=0.2] Não: [p=0.2] quase ninguém discordaria. "
        "[p=0.3] {d}Tem lista? [p=0.2] Também não: [p=0.2] ela só *anuncia* que vai ter discussão."),

    # ================= RECAPITULAÇÃO DO MEIO =================
    dict(id="16", block="recap", text=
        "{t}Três frases para guardar. [p=0.3] {a}Mapa, endereço, lista da caixa. [p=0.6] {b}De onde parte? [p=0.2] O que "
        "defende? [p=0.2] Por quais caminhos? [p=0.6] {c}Três movimentos é *método,* não regra. [p=0.5]"),

    # ================= NÓS FAZEMOS =================
    dict(id="17", block="exercicio", text=
        "{t}Sua vez. [p=0.2] Aqui está a mesma introdução boa, [p=0.2] agora *sem as cores.* [p=0.3] {a}Pause o vídeo [p=0.2] "
        "e marque no seu papel onde começa cada movimento: [p=0.2] o mapa, [p=0.2] o endereço [p=0.2] e a lista. [p=0.3] "
        "{p}Pause agora. [p=2.0]"),
    dict(id="18", block="exercicio", text=
        "{a}Conferindo. [p=0.3] O mapa vai de *Sancionada em dois mil e três* [p=0.2] até *datas comemorativas.* [p=0.4] "
        "{b}O endereço começa em *Esse quadro decorre.* [p=0.4] {c}E a lista são os dois obstáculos: [p=0.2] *a aplicação "
        "irregular da lei* [p=0.2] e *a pouca visibilidade na mídia.* [p=0.4] {d}Repare: [p=0.2] tese e lista estão na *mesma frase.* "
        "[p=0.2] Movimento não é frase."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{a}Erro um: [p=0.2] achar que a introdução *não é avaliada.* [p=0.4] {b}Parece certo, [p=0.2] porque nenhum "
        "descritor avalia a introdução sozinha. [p=0.4] {c}Mas o texto inteiro é corrigido, [p=0.2] e é na introdução que o "
        "corretor começa a ver o seu ponto de vista, [p=0.2] o projeto [p=0.2] e o repertório."),
    dict(id="20", block="erros", text=
        "{a}Erro dois: [p=0.2] achar que a introdução precisa ter *exatamente três frases.* [p=0.4] {b}Parece certo, [p=0.2] "
        "porque o modelo tem três movimentos. [p=0.4] {c}Mas movimento não é frase: [p=0.2] a Cartilha não exige número de "
        "frases, [p=0.2] ordem [p=0.2] nem tamanho."),
    dict(id="21", block="erros", text=
        "{a}Erro três: [p=0.2] começar sem tese, [p=0.2] *só apresentando o tema.* [p=0.4] {b}Parece certo, [p=0.2] porque "
        "introduzir parece ser só apresentar o assunto. [p=0.4] {c}Mas a Cartilha orienta: [p=0.2] inicie o texto "
        "*apresentando seu ponto de vista.*"),

    # ================= QUESTÃO 6 =================
    dict(id="22", block="q6", text=
        "{t}Agora, [p=0.2] uma questão no estilo do ENEM. [p=0.3] {a}Um estudante afirma: [p=0.2] a introdução precisa ter "
        "exatamente três frases, [p=0.2] contexto, tese e antecipação, [p=0.2] senão o Inep desconta pontos. [p=0.3] De acordo "
        "com a Cartilha do Participante, [p=0.2] essa afirmação está: [p=0.4] {A}A: [p=0.2] correta, pois o modelo em três "
        "frases é critério da Competência dois. [p=0.4] {B}B: [p=0.2] incorreta: [p=0.2] o modelo em três movimentos é um "
        "método útil, [p=0.2] aparece nos comentários de redações de nota alta, [p=0.2] mas a avaliação se faz pelas "
        "competências, [p=0.2] sem número fixo de frases."),
    dict(id="23", block="q6", text=
        "{C}C: [p=0.2] correta, pois cada frase ausente reduz quarenta pontos na Competência três. [p=0.4] {D}D: [p=0.2] "
        "incorreta, pois a introdução não deve conter tese, [p=0.2] que só aparece na conclusão. [p=0.4] {E}E: [p=0.2] correta "
        "apenas para textos com mais de vinte e cinco linhas. [p=0.4] {p}Pause o vídeo e tente! [p=2.0]"),
    dict(id="24", block="q6", text=
        "{ok}Letra *B!* [p=0.3] A Cartilha comenta introduções de nota alta com contextualização, tese e antecipação, [p=0.2] "
        "mas avalia por competências e níveis, [p=0.2] sem exigir número de frases. [p=0.4] {xa}A A [p=0.2] {xc}e a C inventam "
        "critérios e *descontos:* [p=0.2] {niv}a correção é por *níveis descritos,* [p=0.2] não por subtração de pontos. "
        "[p=0.4] {xd}A D contraria a própria Cartilha, [p=0.2] que orienta iniciar o texto apresentando o ponto de vista. "
        "[p=0.3] {xe}E a E inventa uma condição."),

    # ================= RECAPITULAÇÃO FINAL E PONTE =================
    dict(id="25", block="recap", text=
        "{t}Para fechar, [p=0.2] as mesmas três frases. [p=0.3] {a}Mapa, endereço, lista da caixa. [p=0.6] {b}De onde parte? "
        "[p=0.2] O que defende? [p=0.2] Por quais caminhos? [p=0.6] {c}Três movimentos é *método,* não regra. [p=0.5]"),
    dict(id="26", block="ponte", text=
        "{a}Toda entrega começa num *mapa.* [p=0.3] {b}Mas que mapa? [p=0.4] {c}Uma lei, [p=0.2] {c2}um fato histórico, "
        "[p=0.2] {c3}um número [p=0.2] {c4}ou um conceito. [p=0.4] {d}Próximo episódio: [p=0.2] os *quatro caminhos* da "
        "contextualização."),

    # ================= CTA =================
    dict(id="27", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual das três perguntas do leitor a sua introdução costuma esquecer? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
