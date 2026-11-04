# Roteiro — Redação ENEM, Desenvolvimento, Episódio 7 de 7: Revisão geral, pegadinhas e desafio prático
# Base: Estudos/Enem/estudos/06-redacao/03-desenvolvimento.html — seções 01 (as três ideias que mais rendem), 11 (os 10
#   erros que mais custam pontos) e 13 (checklist de domínio + tarefa "Antes de marcar Dominado"). NENHUMA das Questões
#   1–9 da seção 12.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora da SÉRIE (relembrada no mapa, cena 03, e antes de cada questão): cada parágrafo de desenvolvimento
#   ENTREGA UM ITEM da lista colada na caixa — ETIQUETA DO ITEM (tópico frasal) · POR QUE ESTÁ NA CAIXA (argumento) · NOTA
#   FISCAL (repertório) · PRODUTO FUNCIONANDO na casa do cliente (análise) · RECIBO ASSINADO (fechamento); "e daí?" = a
#   pergunta do cliente; rascunho de cinco linhas = lista de compras.
# Índice visual: os 6 ícones dos episódios (caixa aberta · etiqueta · nota fiscal · escada do "e daí?" · parágrafo
#   numerado · caderno de oficina).
# Lidos EXATAMENTE como no material: as três ideias da seção 01 (cena 05), a correção de cada erro da seção 11 (respostas
#   do V ou F), a tese e os dois tópicos frasais da seção 03 (teste ao vivo, cena 33), a instrução do checklist e a tarefa
#   do desafio (seção 13).
# V ou F: os 10 erros da seção 11 viram afirmações; 4 são a regra certa (V: 2, 6, 8, 10) e 6 o erro (F), misturados.
# Questões 1–5: INÉDITAS, temas fictícios marcados na tela "Tema elaborado para fins didáticos"; nenhuma lei, dado, obra ou
#   autor inventado. As únicas referências são do material: Lei nº 10.436/2002 (Q2, com o texto da Questão 7 da seção 12)
#   e Cinema Paradiso, de Giuseppe Tornatore (Q3, com o conteúdo da Questão 2 da seção 12). As demais usam causa e
#   consequência. As alternativas erradas são os erros clássicos (tópico vago ou informativo, citar e abandonar,
#   fechamento vago, assunto novo no fim, pergunta retórica, "em primeiro lugar" no 2º parágrafo, "por outro lado" sem
#   contraste). Gabaritos: 1 C · 2 B · 3 D · 4 A · 5 E.
# Desafio: só o teste final (tese + dois tópicos frasais) é feito ao vivo, com a redação do estigma (ENEM 2020).
# Números e anos falados por extenso. Cinco partes = MÉTODO, não critério do Inep. Nenhum nível da C3.
# Cores: azul = definição/tema · verde = método · âmbar = armadilha · vermelho = erro/penalidade · roxo = regra oficial.

TITULO = "10 Pegadinhas do Parágrafo de Desenvolvimento: Você Cai? | Desenvolvimento da Redação Ep. 7"
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
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}É no desenvolvimento que a tese é *provada,* [p=0.3] {b}ou só *repetida.* [p=0.5] {c}Vamos ver se os seus "
        "parágrafos *entregam* [p=0.2] o que a introdução prometeu."),
    dict(id="02", block="hook", text=
        "{a}Nesta revisão: [p=0.2] {b}as três ideias que mais rendem, [p=0.2] {c}um verdadeiro ou falso com *dez "
        "pegadinhas,* [p=0.2] {d}cinco questões inéditas [p=0.2] {e}e um desafio prático. [p=0.4] {f}Pegue papel e caneta."),

    # ================= O MAPA DA SÉRIE =================
    dict(id="03", block="mapa", text=
        "{t}Primeiro, [p=0.2] as imagens da série. [p=0.3] {a}Cada parágrafo *entrega um item* da lista colada na caixa. "
        "[p=0.4] {b}A *etiqueta* do item é o tópico frasal. [p=0.3] {c}*Por que* ele está na caixa é o argumento, [p=0.2] "
        "e a *nota fiscal,* [p=0.2] o repertório. [p=0.4] {d}O *produto funcionando* é a análise, [p=0.2] e o *recibo "
        "assinado,* [p=0.2] o fechamento. [p=0.3] A pergunta do cliente é sempre: [p=0.2] *e daí?* [p=0.4] {e}O "
        "parágrafo-modelo juntou tudo, [p=0.3] {f}e o rascunho de cinco linhas virou a *lista de compras.*"),

    # ================= AS TRÊS IDEIAS =================
    dict(id="04", block="ideias", text=
        "{t}Agora, [p=0.2] um teste de memória. [p=0.3] {a}Quais são as *três ideias* que mais rendem no desenvolvimento? "
        "[p=0.3] {p}Pause e tente lembrar. [p=2.0]"),
    dict(id="05", block="ideias", text=
        "{a}Um: [p=0.2] cada parágrafo de desenvolvimento cumpre *um eixo* anunciado na introdução. [p=0.4] {b}Dois: [p=0.2] "
        "o repertório só é produtivo se vier seguido de *análise.* [p=0.4] {c}Três: [p=0.2] a última frase responde ao "
        "*e daí?,* [p=0.2] ligando o parágrafo de volta à tese."),

    # ================= VERDADEIRO OU FALSO =================
    dict(id="06", block="vf", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso.* [p=0.4] {q}Primeira: [p=0.2] *a saúde mental é importante* [p=0.2] já "
        "funciona como tópico frasal. [p=0.2] {p}Pause e responda. [p=2.0] {r}*Falso!* [p=0.3] {w}Engana porque a frase "
        "fala do tema. [p=0.3] {k}Mas não diz o que será provado: [p=0.2] anuncie o argumento e o eixo."),
    dict(id="07", block="vf", text=
        "{q}Segunda: [p=0.2] repetir a mesma opinião com outras palavras [p=0.2] ainda não é argumentar. [p=0.2] "
        "{p}Pause. [p=2.0] {r}*Verdadeiro!* [p=0.3] {w}Parece argumento, [p=0.2] porque o parágrafo fica cheio. [p=0.3] "
        "{k}Mas é preciso dizer *por que* a afirmação procede."),
    dict(id="08", block="vf", text=
        "{q}Terceira: [p=0.2] se o parágrafo cita uma obra famosa, [p=0.2] o repertório já está produtivo. [p=0.2] "
        "{p}Pause. [p=2.0] {r}*Falso!* [p=0.3] {w}Engana porque um nome famoso impressiona. [p=0.3] {k}Mas repertório "
        "mencionado sem uso tende a não ser produtivo: [p=0.2] resuma o conteúdo e analise."),
    dict(id="09", block="vf", text=
        "{q}Quarta: [p=0.2] depois do repertório, [p=0.2] pode ir direto para o fechamento. [p=0.2] {p}Pause. [p=2.0] "
        "{r}*Falso!* [p=0.3] {w}Engana porque a referência parece falar sozinha. [p=0.3] {k}Mas é na análise que aparece a "
        "autoria: [p=0.2] pergunte *e daí?* à referência."),
    dict(id="10", block="vf", text=
        "{q}Quinta: [p=0.2] *assim, isso é um problema muito grave* [p=0.2] é um bom fechamento. [p=0.2] {p}Pause. [p=2.0] "
        "{r}*Falso!* [p=0.3] {w}Engana porque tem conectivo de fechamento. [p=0.3] {k}Mas não amarra nada: [p=0.2] ligue o "
        "eixo à tese. [p=0.2] Recibo sem assinatura não vale."),
    dict(id="11", block="vf", text=
        "{q}Sexta: [p=0.2] a última frase do parágrafo não deve trazer informação nova. [p=0.2] {p}Pause. [p=2.0] "
        "{r}*Verdadeiro!* [p=0.3] {w}Parece desperdício [p=0.2] não aproveitar mais uma ideia. [p=0.3] {k}Mas o assunto "
        "novo no fim fica sem desenvolvimento."),
    dict(id="12", block="vf", text=
        "{q}Sétima: [p=0.2] tratar os dois eixos no mesmo parágrafo economiza linhas. [p=0.2] {p}Pause. [p=2.0] "
        "{r}*Falso!* [p=0.3] {w}Engana porque parece eficiente. [p=0.3] {k}Mas a progressão fica confusa e um eixo some: "
        "[p=0.2] um parágrafo, [p=0.2] *um eixo.*"),
    dict(id="13", block="vf", text=
        "{q}Oitava: [p=0.2] o segundo parágrafo não deve repetir o argumento do primeiro. [p=0.2] {p}Pause. [p=2.0] "
        "{r}*Verdadeiro!* [p=0.3] {w}Parece exagero, [p=0.2] porque repetir dá a impressão de reforçar. [p=0.3] {k}Mas "
        "repetição desnecessária pesa na C três: [p=0.2] cada parágrafo acrescenta algo novo."),
    dict(id="14", block="vf", text=
        "{q}Nona: [p=0.2] uma citação longa e decorada vale mais do que uma paráfrase. [p=0.2] {p}Pause. [p=2.0] "
        "{r}*Falso!* [p=0.3] {w}Engana porque parece mostrar que você sabe muito. [p=0.3] {k}Mas o melhor é paráfrase curta "
        "e atribuição correta: [p=0.2] gaste as linhas na análise."),
    dict(id="15", block="vf", text=
        "{q}Décima: [p=0.2] as cinco partes do parágrafo são *método,* [p=0.2] e não regra oficial do Inep. [p=0.2] "
        "{p}Pause. [p=2.0] {r}*Verdadeiro!* [p=0.3] {w}Parece regra, [p=0.2] porque o modelo vem sempre na mesma ordem. "
        "[p=0.3] {k}Mas os descritores avaliam desenvolvimento e organização: [p=0.2] a ordem pode variar; [p=0.2] o "
        "*raciocínio* não pode faltar."),

    # ================= QUESTÃO 1: O TÓPICO FRASAL DO EIXO =================
    dict(id="16", block="q1", text=
        "{t}Agora, [p=0.2] cinco questões inéditas. [p=0.3] {r}Lembrando: [p=0.2] o tópico frasal é a *etiqueta:* [p=0.2] "
        "anuncia o eixo e o que o parágrafo vai provar. [p=0.4] {a}Questão um. [p=0.2] Tema: [p=0.2] Desafios para ampliar "
        "o uso do transporte coletivo nas cidades brasileiras. [p=0.3] {s}Eixos da tese: [p=0.2] a baixa frequência dos "
        "ônibus [p=0.2] e a insegurança nos pontos. [p=0.3] {e}Qual frase funciona como tópico frasal do *primeiro* eixo?"),
    dict(id="17", block="q1", text=
        "{A}A: [p=0.2] o transporte coletivo é muito importante para as cidades. [p=0.4] {B}B: [p=0.2] existem vários meios "
        "de transporte coletivo, [p=0.2] como o ônibus e o metrô. [p=0.4] {C}C: [p=0.2] em primeiro lugar, [p=0.2] a baixa "
        "frequência dos ônibus afasta passageiros do transporte coletivo. [p=0.4] {D}D: [p=0.2] será que um dia o ônibus "
        "vai chegar no horário? [p=0.4] {E}E: [p=0.2] por outro lado, [p=0.2] a insegurança nos pontos também é um "
        "problema. [p=0.4] {p}Pause o vídeo e tente! [p=2.0]"),
    dict(id="18", block="q1", text=
        "{ok}Letra *C!* [p=0.3] Conectivo de ordenação, [p=0.2] o eixo um [p=0.2] e uma afirmação a provar. [p=0.4] {xa}A A é "
        "vaga. [p=0.3] {xb}A B só informa: [p=0.2] não defende nada. [p=0.3] {xd}A D é pergunta retórica. [p=0.3] {xe}E a E "
        "usa *por outro lado* sem contraste, [p=0.2] e no eixo errado."),

    # ================= QUESTÃO 2: A PARTE QUE FALTA =================
    dict(id="19", block="q2", text=
        "{r}Lembrando: [p=0.2] depois da nota fiscal, [p=0.2] o cliente quer ver o *produto funcionando:* [p=0.2] a "
        "análise. [p=0.4] {a}Questão dois. [p=0.2] Tema: [p=0.2] Desafios para a inclusão de trabalhadores surdos no "
        "Brasil. [p=0.3] {s1}Em primeiro lugar, [p=0.2] a falta de intérpretes de Libras nas empresas prejudica "
        "trabalhadores surdos. [p=0.3] {s2}Isso ocorre porque, [p=0.2] sem quem domine a língua de sinais, [p=0.2] o "
        "funcionário surdo não acompanha reuniões. [p=0.3] {s3}A Lei dez mil quatrocentos e trinta e seis, [p=0.2] de dois "
        "mil e dois, [p=0.2] reconhece a Língua Brasileira de Sinais como meio legal de comunicação e expressão. [p=0.3] "
        "{s4}Dessa forma, [p=0.2] sem intérpretes, [p=0.2] o trabalhador surdo continua à margem da empresa. [p=0.4] {e}O "
        "que mais falta a esse parágrafo?"),
    dict(id="20", block="q2", text=
        "{A}A: [p=0.2] um tópico frasal, [p=0.2] pois o parágrafo não anuncia o argumento. [p=0.4] {B}B: [p=0.2] a análise, "
        "[p=0.2] que confrontaria a lei com a realidade das empresas. [p=0.4] {C}C: [p=0.2] um argumento, [p=0.2] pois "
        "falta explicar por que a afirmação procede. [p=0.4] {D}D: [p=0.2] um fechamento, [p=0.2] pois o parágrafo não "
        "volta à tese. [p=0.4] {E}E: [p=0.2] uma pergunta retórica no final, [p=0.2] para envolver o leitor. [p=0.4] "
        "{p}Pause o vídeo e tente! [p=2.0]"),
    dict(id="21", block="q2", text=
        "{ok}Letra *B!* [p=0.3] O parágrafo cita a lei [p=0.2] e salta direto para o fechamento: [p=0.2] *citou e "
        "abandonou.* [p=0.4] {xa}A A ignora a frase um, [p=0.2] a etiqueta. [p=0.3] {xc}A C ignora a frase dois, [p=0.2] o "
        "porquê. [p=0.3] {xd}A D ignora a frase quatro, [p=0.2] o recibo. [p=0.3] {xe}E pergunta retórica não amarra nada."),

    # ================= QUESTÃO 3: ANÁLISE OU SÓ MENÇÃO =================
    dict(id="22", block="q3", text=
        "{r}Lembrando: [p=0.2] parar na referência é *citar;* [p=0.2] chegar ao que ela prova é *argumentar.* [p=0.4] "
        "{a}Questão três. [p=0.2] Tema: [p=0.2] Desafios para manter espaços de cultura nas pequenas cidades brasileiras. "
        "[p=0.3] {s}A nota fiscal: [p=0.2] no filme Cinema Paradiso, [p=0.2] de Giuseppe Tornatore, [p=0.2] a sala de "
        "cinema é o centro da vida cultural de uma pequena cidade. [p=0.3] {e}Qual frase, logo depois, faz *análise,* "
        "[p=0.2] e não só menção?"),
    dict(id="23", block="q3", text=
        "{A}A: [p=0.2] esse filme é muito bonito e vale a pena assistir. [p=0.4] {B}B: [p=0.2] o diretor do filme é Giuseppe "
        "Tornatore. [p=0.4] {C}C: [p=0.2] dessa forma, [p=0.2] isso é um problema muito grave. [p=0.4] {D}D: [p=0.2] em "
        "muitas pequenas cidades brasileiras, porém, [p=0.2] não há espaço parecido, [p=0.2] e os moradores ficam sem um "
        "ponto de encontro e de cultura. [p=0.4] {E}E: [p=0.2] além disso, [p=0.2] a internet mudou a forma de ver filmes. "
        "[p=0.4] {p}Pause o vídeo e tente! [p=2.0]"),
    dict(id="24", block="q3", text=
        "{ok}Letra *D!* [p=0.3] Leva a referência para o Brasil de hoje [p=0.2] e mostra a consequência: [p=0.2] o produto "
        "funcionando. [p=0.4] {xa}A A só elogia a obra. [p=0.3] {xb}A B repete a atribuição, [p=0.2] sem uso. [p=0.3] {xc}A C "
        "pula a análise [p=0.2] e fecha de forma vaga. [p=0.3] {xe}E a E abre assunto novo."),

    # ================= QUESTÃO 4: O FECHAMENTO =================
    dict(id="25", block="q4", text=
        "{r}Lembrando: [p=0.2] o fechamento é o *recibo assinado:* [p=0.2] liga o eixo à tese, [p=0.2] sem informação nova. "
        "[p=0.4] {a}Questão quatro. [p=0.2] Tema: [p=0.2] Desafios para reduzir o descarte irregular de lixo nas cidades "
        "brasileiras. [p=0.3] {s}Eixos da tese: [p=0.2] a falta de coleta seletiva nos bairros [p=0.2] e a pouca "
        "informação sobre a separação do lixo. [p=0.3] {i}O parágrafo tratou do primeiro eixo. [p=0.3] {e}Qual frase o "
        "fecha?"),
    dict(id="26", block="q4", text=
        "{A}A: [p=0.2] desse modo, [p=0.2] enquanto a coleta seletiva não chegar aos bairros, [p=0.2] o descarte irregular "
        "continuará a marcar as cidades brasileiras. [p=0.4] {B}B: [p=0.2] assim, [p=0.2] isso é algo muito triste e "
        "preocupante. [p=0.4] {C}C: [p=0.2] será que um dia as cidades vão ficar limpas? [p=0.4] {D}D: [p=0.2] além disso, "
        "[p=0.2] a poluição do ar também prejudica as cidades. [p=0.4] {E}E: [p=0.2] em primeiro lugar, [p=0.2] a coleta "
        "seletiva é responsabilidade de todos. [p=0.4] {p}Pause o vídeo e tente! [p=2.0]"),
    dict(id="27", block="q4", text=
        "{ok}Letra *A!* [p=0.3] Conectivo de fechamento, [p=0.2] o eixo da coleta [p=0.2] e a ligação com a tese. [p=0.4] "
        "{xb}A B é vaga. [p=0.3] {xc}A C é pergunta retórica. [p=0.3] {xd}A D abre assunto novo no fim. [p=0.3] {xe}E a E "
        "reinicia o parágrafo com *em primeiro lugar.*"),

    # ================= QUESTÃO 5: ABRINDO O SEGUNDO EIXO =================
    dict(id="28", block="q5", text=
        "{r}Lembrando: [p=0.2] cada parágrafo entrega *um* item. [p=0.4] {a}Questão cinco. [p=0.2] Tema: [p=0.2] Os "
        "desafios do uso excessivo do celular entre estudantes brasileiros. [p=0.3] {s}Eixos da tese: [p=0.2] a falta de "
        "limites nas famílias [p=0.2] e aplicativos pensados para prender a atenção. [p=0.3] {i}O primeiro parágrafo já "
        "tratou dos limites. [p=0.3] {e}Qual frase abre o *segundo?*"),
    dict(id="29", block="q5", text=
        "{A}A: [p=0.2] em primeiro lugar, [p=0.2] a falta de limites nas famílias favorece o uso excessivo do celular. "
        "[p=0.4] {B}B: [p=0.2] por outro lado, [p=0.2] a falta de limites em casa também é um problema. [p=0.4] {C}C: "
        "[p=0.2] o celular é muito importante na vida dos jovens. [p=0.4] {D}D: [p=0.2] existem muitos aplicativos, [p=0.2] "
        "como jogos e redes sociais. [p=0.4] {E}E: [p=0.2] além disso, [p=0.2] aplicativos pensados para prender a atenção "
        "fazem o estudante perder a noção do tempo. [p=0.4] {p}Pause o vídeo e tente! [p=2.0]"),
    dict(id="30", block="q5", text=
        "{ok}Letra *E!* [p=0.3] Conectivo de adição, [p=0.2] o segundo eixo [p=0.2] e uma afirmação a provar. [p=0.4] {xa}A "
        "A repete o primeiro eixo, [p=0.2] e com *em primeiro lugar.* [p=0.3] {xb}A B usa *por outro lado* sem contraste. "
        "[p=0.3] {xc}A C é vaga. [p=0.3] {xd}E a D só informa."),

    # ================= DESAFIO PRÁTICO =================
    dict(id="31", block="desafio", text=
        "{t}Agora, [p=0.2] o *desafio.* [p=0.3] {a}Retome uma introdução que você escreveu na série Introdução. [p=0.4] "
        "{b}Escreva os *dois* parágrafos de desenvolvimento. [p=0.4] {c}Planeje cada um em cinco linhas: [p=0.2] a lista "
        "de compras. [p=0.3] {d}Redija. [p=0.3] {e}E marque no texto cada parte: [p=0.2] tópico, [p=0.2] argumento, [p=0.2] "
        "repertório, [p=0.2] análise [p=0.2] e fechamento."),
    dict(id="32", block="desafio", text=
        "{a}No fim, [p=0.2] duas conferências. [p=0.3] {b}O *teste da retirada* com cada repertório: [p=0.2] se a nota "
        "fiscal sai e nada muda, [p=0.2] ela não trabalhava. [p=0.4] {c}E o *teste do tópico frasal:* [p=0.2] leia em "
        "sequência só a tese e os dois tópicos frasais."),
    dict(id="33", block="teste", text=
        "{t}Esse último eu faço ao vivo, [p=0.2] com a redação do estigma. [p=0.3] {a}A tese: [p=0.2] No Brasil, o estigma "
        "associado às doenças mentais persiste em razão da desinformação sobre os transtornos [p=0.2] e de representações "
        "midiáticas que associam o adoecimento psíquico à violência. [p=0.4] {b}Tópico um: [p=0.2] Em primeiro lugar, "
        "[p=0.2] a desinformação sobre os transtornos mentais sustenta o estigma que os cerca. [p=0.4] {c}Tópico dois: "
        "[p=0.2] Além disso, [p=0.2] representações midiáticas que associam o adoecimento psíquico à violência reforçam o "
        "preconceito."),
    dict(id="34", block="teste", text=
        "{a}Formam um raciocínio completo? [p=0.4] {b}A posição: [p=0.2] o estigma persiste. [p=0.3] {c}Razão um: [p=0.2] "
        "a desinformação. [p=0.3] {d}Razão dois: [p=0.2] a mídia. [p=0.4] {e}Sim: [p=0.2] o projeto de texto está "
        "*visível.* [p=0.4] {f}Agora é com você."),

    # ================= CHECKLIST DE DOMÍNIO =================
    dict(id="35", block="dominio", text=
        "{t}Para fechar, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria explicar em voz alta "
        "para outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}O que não marcou, [p=0.2] reveja o episódio "
        "correspondente."),
    dict(id="36", block="dominio", text=
        "{e1}Episódio um, [p=0.2] a anatomia do parágrafo: [p=0.2] as cinco partes, [p=0.2] suas perguntas [p=0.2] e por que "
        "é método. [p=0.4] {e2}Episódio dois, [p=0.2] o tópico frasal: [p=0.2] retomar um eixo [p=0.2] e escolher o "
        "conectivo pelo sentido. [p=0.4] {e3}Episódio três, [p=0.2] argumento e repertório: [p=0.2] causa e consequência, "
        "[p=0.2] as estratégias da Cartilha [p=0.2] e o repertório em paráfrase, [p=0.2] bem atribuído."),
    dict(id="37", block="dominio", text=
        "{e4}Episódio quatro, [p=0.2] análise e fechamento: [p=0.2] ligar a referência ao Brasil de hoje [p=0.2] e o eixo à "
        "tese. [p=0.4] {e5}Episódio cinco, [p=0.2] do fraco ao bom: [p=0.2] de só opinião a argumento, [p=0.2] e o "
        "repertório solto corrigido. [p=0.4] {e6}Episódio seis, [p=0.2] a oficina: [p=0.2] cinco linhas de rascunho [p=0.2] "
        "e dois parágrafos com eixos diferentes e equilibrados."),

    # ================= PONTE E CTA =================
    dict(id="38", block="ponte", text=
        "{a}Os dois itens foram *entregues.* [p=0.4] {b}Falta o último passo: [p=0.2] conferir a entrega [p=0.2] e dizer o "
        "que fazer com o problema. [p=0.4] {c}O próximo assunto é *Conclusão:* [p=0.2] agente, [p=0.2] ação, [p=0.2] meio, "
        "[p=0.2] finalidade [p=0.2] e detalhamento."),
    dict(id="39", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantas das dez você acertou no verdadeiro ou falso? [p=0.5] "
        "{anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no "
        "*Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
