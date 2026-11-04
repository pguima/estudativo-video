# Roteiro — Redação ENEM, Introdução, Episódio 4 de 7: A tese e a antecipação — dizer o que você defende e por onde vai provar
# Base: Estudos/Enem/estudos/06-redacao/02-introducao.html — seções 05 e 06 + Questão 5 da seção 12 + QUESTÃO INÉDITA
#   (tema de 2017, texto do prompt do usuário) no lugar da Questão 4, que repete a Questão 8 da série Leitura da Proposta.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia da série: a introdução é a ETIQUETA COMPLETA DA ENCOMENDA (mapa · rua de acesso · endereço + entrega · lista da
#   caixa). Neste episódio: tese = o que você entrega, cobrindo o endereço INTEIRO; antecipação = a LISTA DA CAIXA
#   (liquidificador + jarra; chegou torradeira = reclamação). "Promessa feita é promessa cobrada."
# Lidos EXATAMENTE como no material: os 4 critérios e as 4 frases da tabela da seção 05, as citações da Cartilha da seção 06,
#   os 3 exemplos de antecipação (tabela da seção 06), a tese do estigma (2020, fio das séries 03 e 04) e a Questão 5.
# Questão inédita (marcada na tela "Questão elaborada para fins didáticos"): gabarito B. Questão 5: gabarito D.
# A Cartilha NÃO proíbe a primeira pessoa (dito na cena 12). Impessoalidade e Competência 3 só citadas.
# Cores: azul = definição · verde = método · âmbar = armadilha · vermelho = erro · roxo = regra oficial (Cartilha).

TITULO = "Opinião Não É Tese: Como Escrever a Tese da Redação do ENEM | Introdução da Redação Ep. 4"
# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo da folha em branco: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Nesta aula você ensina a transformar uma opinião em tese: "
            "faça as perguntas com curiosidade, avalie as frases ao vivo como quem pensa em voz alta, mostre surpresa na "
            "torradeira que chegou no lugar da jarra e comemore quando a tese fica completa. Ritmo didático e tranquilo, "
            "sem pressa, respeitando as pausas entre as frases. "
            "Leia apenas o texto, exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}A herança africana deve ser valorizada. [p=0.4] {b}Isso é *tese?* [p=0.5] {c}Tem posição, [p=0.2] mas quase "
        "ninguém discordaria, [p=0.3] {d}e não diz o que *impede* a valorização. [p=0.4] {e}Hoje você aprende a diferença "
        "entre ter *opinião* [p=0.2] e ter *tese.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai escrever uma tese *clara,* [p=0.2] *contestável* [p=0.2] e *completa,* [p=0.3] "
        "{b}já com os *dois eixos* que o resto do texto vai cumprir."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Antes, [p=0.2] uma revisão relâmpago. [p=0.3] {a}Na série Leitura da proposta, [p=0.2] você dividiu a frase "
        "temática em *blocos,* [p=0.2] e viu que deixar um bloco de fora é *tangenciar.* [p=0.4] {b}No episódio passado, "
        "[p=0.2] a *ponte* levou a referência até o recorte. [p=0.4] {c}E quem viu a série de Linguagens já conhece o "
        "*teste da discordância:* [p=0.2] contestável é aquilo de que alguém poderia discordar."),

    # ================= A CAIXA (CONCRETO) =================
    dict(id="04", block="caixa", text=
        "{t}Agora, [p=0.2] imagine uma caixa que chega na sua casa. [p=0.3] {a}Colada nela, [p=0.2] uma lista: [p=0.2] "
        "contém um liquidificador e uma jarra. [p=0.4] {b}Você abre... [p=0.4] {c}e, no lugar da jarra, [p=0.2] tem uma "
        "*torradeira.* [p=0.4] {d}Mesmo que a torradeira seja ótima, [p=0.2] você reclama. [p=0.3] Por quê? [p=0.3] "
        "{e}Porque a lista *prometeu* outra coisa."),
    dict(id="05", block="caixa", text=
        "{a}Na nossa etiqueta, [p=0.2] a *tese* é o que você entrega no endereço, [p=0.2] e ela tem de cobrir o endereço "
        "*inteiro.* [p=0.4] {b}A *antecipação* é a lista da caixa: [p=0.2] cada item listado vai ser entregue por um "
        "parágrafo de desenvolvimento. [p=0.4] {c}Por isso, [p=0.2] *promessa feita é promessa cobrada.*"),

    # ================= OS 4 CRITÉRIOS =================
    dict(id="06", block="criterios", text=
        "{t}Comecemos pela tese. [p=0.3] {d}Tese é a *posição* que o texto vai defender sobre o tema. [p=0.4] {q}Mas o que "
        "faz uma tese ser *boa?* [p=0.3] O material dá quatro critérios."),
    dict(id="07", block="criterios", text=
        "{a}Um: [p=0.2] *clara:* [p=0.2] dá para resumir numa frase. [p=0.4] {b}Dois: [p=0.2] *contestável:* [p=0.2] "
        "alguém poderia defender outra posição. [p=0.4] {c}Três: [p=0.2] *completa* em relação ao recorte: [p=0.2] cobre "
        "todos os blocos da frase temática. [p=0.4] {d}Quatro: [p=0.2] *argumentável:* [p=0.2] dá para sustentar com fatos "
        "e raciocínio em dois parágrafos."),

    # ================= EU FAÇO: A TABELA DE 2024 =================
    dict(id="08", block="eufaco", text=
        "{t}Vamos testar ao vivo, [p=0.2] com o tema de dois mil e vinte e quatro: [p=0.2] {tema}Desafios para a "
        "valorização da herança africana no Brasil. [p=0.4] {f1}Primeira frase: [p=0.2] A herança africana é um tema muito "
        "importante. [p=0.4] {x1}Tem posição? [p=0.2] Não: [p=0.2] só afirma a importância. [p=0.3] Sem posição, [p=0.2] "
        "não há o que contestar [p=0.2] nem o que argumentar. [p=0.3] {v1}*Não é tese.*"),
    dict(id="09", block="eufaco", text=
        "{f2}Segunda: [p=0.2] A herança africana deve ser valorizada. [p=0.4] {x2}Clara? [p=0.2] Sim. [p=0.3] "
        "{y2}Contestável? [p=0.2] Quase ninguém a contestaria. [p=0.3] {z2}E não diz o que *impede* a valorização: [p=0.2] "
        "faltam os desafios. [p=0.3] {v2}Tese *fraca.*"),
    dict(id="10", block="eufaco", text=
        "{f3}Terceira: [p=0.2] A cultura africana é rica e diversa. [p=0.4] {x3}Fala do assunto, [p=0.2] mas cadê "
        "desafios? [p=0.2] Cadê valorização? [p=0.2] Cadê Brasil? [p=0.3] {v3}*Não* para este tema."),
    dict(id="11", block="eufaco", text=
        "{f4}Quarta: [p=0.2] A valorização da herança africana no Brasil é dificultada pela aplicação irregular do ensino "
        "de cultura afro-brasileira [p=0.2] e pela pouca visibilidade dessa cultura na mídia. [p=0.5] {x4}Posição contestável, [p=0.2] {y4}cobre o "
        "recorte [p=0.2] {z4}e anuncia dois eixos. [p=0.3] {v4}*Sim:* [p=0.2] isso é tese."),

    # ================= PRIMEIRA PESSOA =================
    dict(id="12", block="pessoa", text=
        "{q}E dá para escrever a tese em *primeira pessoa,* [p=0.2] com eu acredito? [p=0.3] {a}A Cartilha *não proíbe.* "
        "[p=0.3] {b}Mas o *registro impessoal,* [p=0.2] aquele que não fala de si mesmo, [p=0.2] é o mais usado. [p=0.3] "
        "{c}No lugar de acredito que, [p=0.2] use é preciso reconhecer que, [p=0.2] evidencia-se que, [p=0.2] {d}ou "
        "simplesmente a afirmação direta. [p=0.3] {e}A série Impessoalidade aprofunda esse ponto."),

    # ================= ANTECIPAR =================
    dict(id="13", block="antecipar", text=
        "{t}Agora, [p=0.2] a lista da caixa. [p=0.3] {a}Antecipar é anunciar, [p=0.2] de forma breve, [p=0.2] os *eixos* "
        "que cada parágrafo de desenvolvimento vai sustentar. [p=0.3] {b}Eixo é cada caminho do seu argumento. [p=0.4] "
        "{c}E a Cartilha elogia isso. [p=0.2] Ao comentar redações de nota alta, [p=0.2] ela destaca introduções que "
        "delimitam a tese [p=0.2] {d}antecipando, assim, os dois eixos argumentativos que serão desenvolvidos, [p=0.4] "
        "{e}ou que antecipam as causas a discutir, [p=0.2] anunciando, portanto, o seu projeto de texto."),
    dict(id="14", block="mapa", text=
        "{a}Pense na introdução como o *mapa do texto.* [p=0.3] {b}A tese anuncia o eixo A [p=0.2] e o eixo B. [p=0.3] "
        "{c}O primeiro parágrafo de desenvolvimento cumpre o eixo A; [p=0.2] {d}o segundo, [p=0.2] o eixo B; [p=0.3] {e}e a "
        "conclusão retoma os dois na proposta de intervenção. [p=0.4] {f}Esse plano visível é o *projeto de texto,* "
        "[p=0.2] avaliado na *Competência três.*"),
    dict(id="15", block="formas", text=
        "{t}E dá para antecipar de *três formas.* [p=0.3] {a}Com dois substantivos coordenados: [p=0.2] dificultada pela "
        "aplicação irregular da lei e pela pouca visibilidade na mídia. [p=0.4] {b}Com causa e consequência: [p=0.2] pois o "
        "apagamento escolar alimenta preconceitos que, por sua vez, afastam os jovens dessas tradições. [p=0.4] {c}Ou com "
        "dois agentes: [p=0.2] problema que envolve tanto a escola quanto os meios de comunicação."),
    dict(id="16", block="cobrada", text=
        "{a}Só que tem um porém. [p=0.3] {b}Se a introdução anuncia dois eixos [p=0.2] e o desenvolvimento trata de um "
        "terceiro assunto, [p=0.2] {c}o leitor percebe a quebra, [p=0.2] e a *coerência* sofre, [p=0.2] na C três. [p=0.4] "
        "{d}Coerência é o texto fazer sentido como um todo. [p=0.4] {e}Por isso, [p=0.2] escreva a antecipação *depois* "
        "de planejar os parágrafos no rascunho, [p=0.2] *nunca antes.*"),

    # ================= A TESE QUE VIRA FIO DAS PRÓXIMAS SÉRIES =================
    dict(id="17", block="estigma", text=
        "{t}Agora, [p=0.2] uma tese para guardar. [p=0.3] {a}Tema de dois mil e vinte: [p=0.2] O estigma associado às "
        "doenças mentais na sociedade brasileira. [p=0.3] {s}Estigma é uma marca negativa que a sociedade cola numa "
        "pessoa. [p=0.4] {b}A tese: [p=0.2] No Brasil, o estigma associado às doenças mentais persiste em razão da "
        "desinformação sobre os transtornos [p=0.2] e de representações midiáticas que associam o adoecimento psíquico à "
        "violência. [p=0.5] {c}Eixo A: [p=0.2] desinformação. [p=0.3] {d}Eixo B: [p=0.2] representações midiáticas. "
        "[p=0.4] {e}*Guarde esta tese.* [p=0.2] Nas séries de Desenvolvimento e de Conclusão, [p=0.2] vamos terminar esta "
        "redação."),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Pegue a tese fraca: [p=0.2] A herança africana deve ser valorizada. [p=0.3] {b}Reescreva "
        "acrescentando *dois eixos:* [p=0.2] o que impede essa valorização? [p=0.3] {p}Pause e escreva. [p=2.5]"),
    dict(id="19", block="exercicio", text=
        "{a}Uma resposta possível é a tese boa da tabela: [p=0.2] {b}A valorização da herança africana no Brasil é "
        "dificultada pela aplicação irregular do ensino de cultura afro-brasileira [p=0.2] e pela pouca visibilidade dessa cultura na mídia. "
        "[p=0.4] {c}Se a sua nomeou dois obstáculos [p=0.2] e manteve todos os blocos, [p=0.2] você acertou."),

    # ================= 3 FRASES-CHAVE (MEIO) =================
    dict(id="20", block="recap", text=
        "{t}Três frases para guardar. [p=0.3] {a}Tese: [p=0.2] clara, contestável, completa, argumentável. [p=0.4] "
        "{b}Antecipar é colar a lista na caixa. [p=0.4] {c}Promessa feita é promessa cobrada. [p=0.5]"),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{a}Erro um: [p=0.2] a tese que só declara importância. [p=0.3] {b}Parece certo porque usa as palavras do tema "
        "[p=0.2] e soa séria. [p=0.3] {c}Mas importância não é posição: [p=0.2] diga o que você defende."),
    dict(id="22", block="erros", text=
        "{a}Erro dois: [p=0.2] a tese que esquece um bloco da frase temática. [p=0.3] {b}Parece certo porque fala do "
        "assunto direitinho. [p=0.3] {c}Mas, sem um bloco, [p=0.2] o texto tangencia desde a introdução: [p=0.2] confira "
        "bloco a bloco."),
    dict(id="23", block="erros", text=
        "{a}Erro três: [p=0.2] anunciar um eixo que o texto não desenvolve. [p=0.3] {b}Parece certo porque a introdução "
        "ficou bonita e completa. [p=0.3] {c}Mas a promessa é cobrada: [p=0.2] planeje os parágrafos antes de anunciar."),

    # ================= QUESTÃO INÉDITA (2017) =================
    dict(id="24", block="qi", text=
        "{t}Agora, [p=0.2] questão. [p=0.3] {a}Para o tema do Enem dois mil e dezessete, [p=0.2] Desafios para a formação "
        "educacional de surdos no Brasil, [p=0.3] a frase que apresenta uma tese e antecipa os dois eixos do "
        "desenvolvimento é: [p=0.4] {A}A: [p=0.2] A educação de surdos é um assunto que merece a atenção de todos. [p=0.4] "
        "{B}B: [p=0.2] No Brasil, a formação educacional de surdos esbarra na escassez de escolas bilíngues e na falta de "
        "professores fluentes em Libras."),
    dict(id="25", block="qi", text=
        "{C}C: [p=0.2] Até quando os surdos vão esperar por uma escola de qualidade? [p=0.4] {D}D: [p=0.2] Em vários "
        "países, pessoas surdas enfrentam dificuldades na escola. [p=0.4] {E}E: [p=0.2] Este texto vai discutir os "
        "desafios para a formação educacional de surdos no Brasil. [p=0.4] {p}Pause o vídeo e tente! [p=2.5]"),
    dict(id="26", block="qi", text=
        "{ok}Letra *B.* [p=0.3] Ela toma posição [p=0.2] e nomeia os eixos: [p=0.2] escolas bilíngues [p=0.2] e "
        "professores fluentes em Libras, [p=0.2] a Língua Brasileira de Sinais. [p=0.4] {xa}A A declara importância. "
        "[p=0.3] {xc}A C é uma *pergunta retórica,* [p=0.2] feita sem esperar resposta, [p=0.2] e pergunta não substitui "
        "a tese. [p=0.3] {xd}A D sai do Brasil [p=0.2] e fica no assunto amplo. [p=0.3] {xe}E a E anuncia o tema [p=0.2] "
        "sem dizer o que o texto defende."),

    # ================= QUESTÃO 5 (PROMESSA NÃO CUMPRIDA) =================
    dict(id="27", block="q5", text=
        "{t}Mais uma. [p=0.3] {a}A introdução de uma redação anuncia que o texto discutirá [p=0.2] a falta de salas de "
        "cinema fora das capitais [p=0.2] e o preço dos ingressos. [p=0.4] {b}O primeiro parágrafo de desenvolvimento trata "
        "da falta de salas; [p=0.3] {c}o segundo, [p=0.2] da qualidade dos roteiros dos filmes nacionais. [p=0.4] {d}Esse "
        "descompasso afeta principalmente:"),
    dict(id="28", block="q5", text=
        "{A}A: [p=0.2] a Competência um, pois houve mudança de registro. [p=0.4] {B}B: [p=0.2] a Competência quatro, pois "
        "faltam conectivos entre os parágrafos. [p=0.4] {C}C: [p=0.2] a Competência cinco, que avalia apenas a introdução. "
        "[p=0.4] {D}D: [p=0.2] a Competência três, pois o projeto de texto anunciado na introdução não é cumprido pelo "
        "desenvolvimento. [p=0.4] {E}E: [p=0.2] nenhuma competência, já que a introdução não é avaliada pelo Inep. [p=0.4] "
        "{p}Pause e tente! [p=2.5]"),
    dict(id="29", block="q5", text=
        "{ok}Letra *D.* [p=0.3] A lista prometeu o preço dos ingressos, [p=0.2] {tr}e chegou a qualidade dos roteiros: "
        "[p=0.2] a torradeira no lugar da jarra. [p=0.3] É falha de projeto de texto, [p=0.2] na C três. [p=0.4] {xa}A A "
        "{xb}e a B citam problemas que o enunciado não descreve. [p=0.3] {xc}A C erra a competência: [p=0.2] a C cinco "
        "avalia a proposta de intervenção. [p=0.3] {xe}E a E é falsa: [p=0.2] o texto inteiro é avaliado, [p=0.2] e o "
        "projeto de texto envolve a introdução."),

    # ================= 3 FRASES-CHAVE (FIM) =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, [p=0.2] as mesmas três frases. [p=0.3] {a}Tese: [p=0.2] clara, contestável, completa, "
        "argumentável. [p=0.4] {b}Antecipar é colar a lista na caixa. [p=0.4] {c}Promessa feita é promessa cobrada. [p=0.5]"),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}Agora você tem todas as peças: [p=0.2] mapa, [p=0.2] rua, [p=0.2] endereço [p=0.2] e lista. [p=0.4] {b}No "
        "próximo episódio, [p=0.2] *três introduções* para o mesmo tema, [p=0.2] da pior à melhor, [p=0.3] {c}e as "
        "armadilhas que mais aparecem no primeiro parágrafo."),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] como ficou a sua tese com dois eixos para a herança africana? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do "
        "ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. "
        "[p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
