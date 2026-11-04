# Roteiro — Redação ENEM, Desenvolvimento, Episódio 2 de 7: O tópico frasal — a primeira frase que diz o que o parágrafo vai provar
# Base: Estudos/Enem/estudos/06-redacao/03-desenvolvimento.html — seção 03 + Questões 1 e 3 da seção 12.
#   Modelagem com as quatro frases da tabela da seção 03 (tema de 2020), avaliadas ao vivo no rascunho com as perguntas
#   "que eixo você retoma? o que você vai provar?". Conectivos só com a regra da seção 03 (a série Conectivos aprofunda).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora da SÉRIE: cada parágrafo de desenvolvimento ENTREGA UM ITEM da lista colada na caixa, em cinco etapas.
#   Aqui: o tópico frasal é a ETIQUETA DO ITEM — diz qual item da lista está chegando e o que ele vai provar
#   ("coisa" × "item 1: liquidificador, 3 velocidades").
# Frases-chave (meio e fim, idênticas):
#   1. Tópico frasal é a etiqueta do item: eixo + o que vou provar.  2. Tese + tópicos em sequência: tem que fazer sentido
#   sozinho.  3. Conectivo pela relação, não por hábito.
# FIDELIDADE: lidos EXATAMENTE como no material: as quatro frases da tabela e as avaliações da seção 03 (09–12, 20), o
#   parágrafo e as alternativas da Questão 1 (24–26) e a tese e as alternativas da Questão 3 (27–29). A posição do tópico
#   frasal é "em geral, a primeira" (cena 07): lugar mais comum, não regra. O "teste do tópico frasal" é o mesmo que a série
#   da Competência 3 chama de "revisão de coerência em dois minutos" (cena 15). Números e anos falados por extenso.
# Cores: azul = definição · verde = dica/método · âmbar = armadilha · vermelho = erro · roxo = regra oficial (Cartilha).

TITULO = "O Tópico Frasal: a 1ª Frase Que Diz o Que o Parágrafo Vai Provar | Desenvolvimento da Redação Ep. 2"
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
        "{a}Leia só a *tese* [p=0.2] {b}e a *primeira frase* de cada parágrafo. [p=0.4] {c}Se essas três frases não "
        "formam um raciocínio, [p=0.3] {d}o corretor também não vai achar o seu."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai escrever *primeiras frases* [p=0.2] {b}que retomam um *eixo* da tese "
        "[p=0.3] {c}e dizem *o que* o parágrafo vai provar. [p=0.4] {d}E calma: [p=0.2] cada palavra nova vai ser "
        "explicada."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Antes, [p=0.2] uma revisão relâmpago. [p=0.3] {a}No episódio um: [p=0.2] cada parágrafo de desenvolvimento "
        "*entrega um item,* [p=0.2] em cinco etapas. [p=0.4] {b}E a tese do estigma, [p=0.2] de dois mil e vinte, "
        "[p=0.2] tem *dois eixos:* [p=0.2] eixo é cada caminho que sustenta a sua posição. [p=0.3] {c}A "
        "*desinformação* [p=0.2] {d}e a *mídia.*"),

    # ================= AS DUAS ETIQUETAS (CONCRETO ANTES DO ABSTRATO) =================
    dict(id="04", block="etiquetas", text=
        "{t}Imagine uma caixa [p=0.2] com dois itens dentro. [p=0.3] {a}No primeiro, [p=0.2] a "
        "etiqueta diz só: [p=0.2] *coisa.* [p=0.4] {b}No segundo, [p=0.2] diz: [p=0.2] *item um,* [p=0.1] liquidificador, "
        "[p=0.1] três velocidades. [p=0.4] {c}Qual dos dois você sabe o que é [p=0.2] antes mesmo de abrir?"),
    dict(id="05", block="analogia", text=
        "{t}A segunda diz *qual item* chegou [p=0.2] e *o que* ele promete. [p=0.4] {a}No parágrafo de "
        "desenvolvimento, [p=0.2] essa etiqueta se chama *tópico frasal.* [p=0.4] {b}Ele diz qual item da lista está "
        "chegando [p=0.2] {c}e o que ele vai provar."),

    # ================= BLOCO A: DEFINIÇÃO =================
    dict(id="06", block="definicao", text=
        "{t}Mas o que é um tópico frasal? [p=0.4] {a}É a frase, [p=0.2] em geral a primeira do parágrafo, [p=0.2] que "
        "anuncia o *argumento* que ele vai desenvolver. [p=0.3] {g}Argumento é a razão que sustenta a sua posição. "
        "[p=0.4] {b}Ela faz duas coisas: [p=0.3] {c}retoma *um dos eixos* da introdução [p=0.3] {d}e diz *o que* o "
        "parágrafo vai provar sobre ele."),
    dict(id="07", block="definicao", text=
        "{t}Repare no *em geral.* [p=0.4] {a}A primeira frase é o lugar *mais comum,* [p=0.2] {b}não uma regra "
        "oficial: [p=0.3] {c}como as cinco partes, [p=0.2] é *método de estudo.* [p=0.4] {d}Mas abrir pela etiqueta "
        "ajuda o leitor a saber logo o que chegou."),

    # ================= BLOCO B: EU FAÇO — AS QUATRO FRASES DA TABELA =================
    dict(id="08", block="eufaco", text=
        "{t}Agora eu faço, [p=0.2] ao vivo, [p=0.2] no rascunho. [p=0.3] {a}Tema do ENEM dois mil e vinte: [p=0.2] *O "
        "estigma associado às doenças mentais na sociedade brasileira.* [p=0.4] {b}Estigma é uma marca de preconceito "
        "colada em alguém. [p=0.4] {c}Quatro candidatas, [p=0.2] duas perguntas. [p=0.3] {q1}Que eixo você retoma? "
        "[p=0.3] {q2}O que você vai provar?"),
    dict(id="09", block="eufaco", text=
        "{a}Primeira candidata. [p=0.3] {s}A saúde mental é muito importante. [p=0.4] {q1}Que eixo ela retoma? [p=0.2] "
        "Nenhum. [p=0.3] {q2}O que ela vai provar? [p=0.2] Nada. [p=0.4] {v}Avaliação: "
        "[p=0.2] *vaga.* [p=0.2] Não anuncia argumento nem eixo. [p=0.3] {e}É a etiqueta *coisa.*"),
    dict(id="10", block="eufaco", text=
        "{a}Segunda. [p=0.3] {s}Existem muitas doenças mentais, [p=0.1] como a depressão e a ansiedade. [p=0.4] "
        "{m}Parece melhor, [p=0.2] porque traz exemplos. [p=0.3] {q1}Mas que eixo ela retoma? [p=0.2] Nenhum. [p=0.3] "
        "{q2}O que defende? [p=0.2] Nada. [p=0.4] {v}Avaliação: [p=0.2] *informativa.* [p=0.2] Descreve o assunto, "
        "[p=0.2] não defende nada. [p=0.3] {e}Etiqueta em branco."),
    dict(id="11", block="eufaco", text=
        "{a}Terceira. [p=0.3] {s}Em primeiro lugar, [p=0.2] a desinformação sobre os transtornos mentais sustenta o "
        "estigma que os cerca. [p=0.4] {c}Começa com um *conectivo,* [p=0.2] que liga partes do texto. [p=0.2] Este é "
        "de *ordenação:* [p=0.2] marca a posição na sequência. [p=0.4] {q1}Que eixo? [p=0.2] A *desinformação,* "
        "[p=0.2] o eixo um. [p=0.3] {q2}O que vai provar? [p=0.2] Que ela *sustenta* o estigma. [p=0.4] {v}Avaliação: "
        "[p=0.2] *boa.*"),
    dict(id="12", block="eufaco", text=
        "{a}Quarta. [p=0.3] {s}Além disso, [p=0.2] representações midiáticas que associam o adoecimento psíquico à "
        "violência [p=0.2] reforçam o preconceito. [p=0.4] {c}*Além disso* é de *adição:* [p=0.2] acrescenta mais uma "
        "razão. [p=0.4] {q1}Que eixo? [p=0.2] A *mídia,* [p=0.2] o eixo dois. [p=0.3] {q2}O que vai provar? [p=0.2] "
        "Uma *causa:* [p=0.2] essas imagens *reforçam* o preconceito. [p=0.4] {v}Avaliação: [p=0.2] *boa.*"),

    # ================= EXEMPLO × CONTRAEXEMPLO =================
    dict(id="13", block="lado", text=
        "{t}Agora, [p=0.2] lado a lado. [p=0.3] {a}As duas primeiras são etiquetas *em branco.* [p=0.4] {b}As duas "
        "boas têm três peças: [p=0.2] {b1}conectivo, [p=0.2] {b2}eixo da tese [p=0.2] {b3}e afirmação a provar. "
        "[p=0.4] {c}O tema é o mesmo; [p=0.2] muda o *trabalho* da frase."),

    # ================= BLOCO C: O TESTE DO TÓPICO FRASAL =================
    dict(id="14", block="teste", text=
        "{t}E como saber se os seus tópicos funcionam? [p=0.4] {a}Com o *teste do tópico frasal.* [p=0.3] {b}Esconda o "
        "resto [p=0.2] {c}e leia em sequência só a tese e os tópicos frasais. [p=0.4] {d}Se essas três frases formam "
        "um raciocínio completo, [p=0.2] a posição e as duas razões, [p=0.3] {e}o *projeto de texto* está visível: "
        "[p=0.3] {f}o plano da redação para defender a tese."),
    dict(id="15", block="teste", text=
        "{t}Vamos testar. [p=0.3] {a}A tese, [p=0.2] em resumo: [p=0.2] o estigma persiste pela desinformação e pela "
        "mídia. [p=0.4] {b}Tópico um: [p=0.2] a desinformação sustenta o estigma. [p=0.3] {c}Tópico dois: [p=0.2] a "
        "mídia reforça o preconceito. [p=0.4] {d}Uma posição, [p=0.2] duas razões: [p=0.2] faz sentido *sozinho.* "
        "[p=0.4] {e}Com os tópicos vagos, [p=0.3] {f}o raciocínio *some.* [p=0.4] {g}É a mesma *revisão de coerência "
        "em dois minutos* da série da Competência três."),

    # ================= BLOCO D: O CONECTIVO DE ABERTURA =================
    dict(id="16", block="conectivo", text=
        "{t}E a expressão que abre o parágrafo? [p=0.2] Faz diferença? [p=0.4] {a}Faz. [p=0.2] É o *conectivo de "
        "abertura:* [p=0.3] {b}em primeiro lugar, [p=0.2] {c}além disso, [p=0.2] {d}ademais, [p=0.2] {e}por outro "
        "lado. [p=0.4] {f}Ele marca a *progressão* entre os parágrafos: [p=0.2] o texto andando para a frente. [p=0.4] "
        "{g}E isso é avaliado na *Competência quatro.*"),
    dict(id="17", block="conectivo", text=
        "{t}Então, [p=0.2] qualquer um serve? [p=0.4] {a}Não. [p=0.2] Escolha pela *relação de sentido,* [p=0.2] não "
        "por hábito. [p=0.4] {b}*Em primeiro lugar* ordena. [p=0.3] {c}*Além disso* e *ademais* acrescentam. [p=0.4] "
        "{d}*Por outro lado* anuncia *contraste:* [p=0.2] uma ideia na direção oposta, [p=0.2] não simples acréscimo. "
        "[p=0.4] {e}A série de *Conectivos* aprofunda essa escolha."),

    # ================= RECAPITULAÇÃO DO MEIO =================
    dict(id="18", block="recap", text=
        "{t}Três frases para guardar. [p=0.3] {a}Tópico frasal é a etiqueta do item: [p=0.2] eixo mais o que vou provar. "
        "[p=0.6] {b}Tese mais tópicos em sequência: [p=0.2] tem que fazer sentido sozinho. [p=0.6] {c}Conectivo pela "
        "relação, [p=0.2] não por hábito. [p=0.5]"),

    # ================= NÓS FAZEMOS =================
    dict(id="19", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Pegue a tese do estigma. [p=0.3] {b}Pause o vídeo [p=0.2] e escreva um tópico frasal para "
        "o *eixo dois,* [p=0.2] a mídia, [p=0.2] {c}começando com um conectivo de *adição.* [p=0.3] {p}Pause agora. "
        "[p=2.0]"),
    dict(id="20", block="exercicio", text=
        "{a}Conferindo, [p=0.2] com a frase boa da tabela. [p=0.3] {s}Além disso, [p=0.2] representações midiáticas "
        "que associam o adoecimento psíquico à violência [p=0.2] reforçam o preconceito. [p=0.4] {k1}Conectivo de "
        "adição? [p=0.3] {k2}Eixo dois? [p=0.3] {k3}O que vai provar? [p=0.4] {d}Se a sua frase tem essas três peças, "
        "[p=0.2] ela *funciona.*"),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{a}Erro um: [p=0.2] um tópico que só *descreve* o assunto, [p=0.2] como: [p=0.2] existem muitas doenças mentais. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque é verdade [p=0.2] e fala do tema. [p=0.4] {c}Mas não "
        "defende nada. [p=0.2] Anuncie o argumento [p=0.2] e o eixo."),
    dict(id="22", block="erros", text=
        "{a}Erro dois: [p=0.2] usar *em primeiro lugar* no *segundo* parágrafo. [p=0.4] {b}Parece certo, [p=0.2] porque é o "
        "conectivo de abertura mais conhecido. [p=0.4] {c}Mas ele ordena: [p=0.2] anuncia o *primeiro* item. [p=0.2] No "
        "segundo parágrafo, [p=0.2] use um de adição, [p=0.2] como *além disso.*"),
    dict(id="23", block="erros", text=
        "{a}Erro três: [p=0.2] usar *por outro lado* sem contraste. [p=0.4] {b}Parece certo, [p=0.2] porque soa como mais "
        "uma coisa a dizer. [p=0.4] {c}Mas por outro lado anuncia *contraste.* [p=0.2] Se você só está acrescentando, "
        "[p=0.2] o conectivo é de *adição.*"),

    # ================= QUESTÃO 1 =================
    dict(id="24", block="q1", text=
        "{t}Agora, [p=0.2] duas questões no estilo do ENEM. [p=0.3] {a}Questão um, [p=0.2] tema de dois mil e vinte e três. "
        "[p=0.2] Leia o parágrafo. [p=0.4] {s1}Um: [p=0.2] No Brasil, [p=0.2] a Constituição de mil "
        "novecentos e oitenta e oito declara homens e mulheres iguais em direitos e obrigações. [p=0.4] {s2}Dois: [p=0.2] Na "
        "prática, porém, [p=0.2] o cuidado com filhos, idosos e doentes continua recaindo sobre as mulheres, [p=0.2] sem "
        "remuneração nem reconhecimento. [p=0.4] {s3}Três: [p=0.2] Além disso, [p=0.2] a herança de uma divisão de tarefas "
        "que atribui o cuidado ao feminino [p=0.2] torna esse trabalho invisível. [p=0.4] {s4}Quatro: [p=0.2] Essa herança "
        "se manifesta desde a infância, [p=0.2] quando meninas são cobradas pelas tarefas domésticas [p=0.2] de que os "
        "meninos são dispensados."),
    dict(id="25", block="q1", text=
        "{a}A frase que funcionaria melhor como tópico frasal [p=0.2] de um parágrafo sobre o eixo *herança cultural* é a: "
        "[p=0.4] {A}A: [p=0.2] um, [p=0.2] pois apresenta um repertório legal. [p=0.3] {B}B: [p=0.2] dois, [p=0.2] pois "
        "contrapõe a lei à realidade. [p=0.3] {C}C: [p=0.2] quatro, [p=0.2] pois traz um exemplo do cotidiano. [p=0.3] "
        "{D}D: [p=0.2] três, [p=0.2] pois anuncia o argumento a ser desenvolvido [p=0.2] e abre com conectivo de "
        "progressão. [p=0.3] {E}E: [p=0.2] nenhuma, [p=0.2] pois tópico frasal só pode ser uma pergunta. [p=0.4] {p}Pause o "
        "vídeo e tente! [p=2.0]"),
    dict(id="26", block="q1", text=
        "{ok}Letra *D!* [p=0.3] {a}A frase três afirma o que o eixo herança cultural precisa provar: [p=0.2] a divisão "
        "de tarefas torna o cuidado invisível. [p=0.3] {b}E abre com *além disso,* [p=0.2] marca de progressão. "
        "[p=0.4] {xa}A um [p=0.2] {xb}e a dois [p=0.2] formam a fundamentação e o contraste de outro eixo: [p=0.2] lei "
        "contra realidade. [p=0.3] {xc}A quatro é exemplo: [p=0.2] sustenta a três, [p=0.2] não a anuncia. [p=0.3] "
        "{xe}E a E inventa uma regra."),

    # ================= QUESTÃO 3 =================
    dict(id="27", block="q3", text=
        "{t}Próxima questão, [p=0.2] tema de dois mil e vinte e um. [p=0.3] {a}A tese é: [p=0.2] A "
        "falta de registro civil torna parte dos brasileiros invisível para o Estado, [p=0.2] situação mantida pela "
        "distância dos cartórios [p=0.2] e pela desinformação sobre a gratuidade do registro. [p=0.4] {r}Registro civil é "
        "o registro oficial do nascimento. [p=0.4] {e1}Eixo um: [p=0.2] a *distância "
        "dos cartórios.* [p=0.3] {e2}Eixo dois: [p=0.2] a *desinformação sobre a gratuidade.*"),
    dict(id="28", block="q3", text=
        "{a}O tópico frasal mais adequado para o *segundo* parágrafo de desenvolvimento é: [p=0.4] {A}A: [p=0.2] Em primeiro "
        "lugar, [p=0.2] a distância dos cartórios dificulta o registro em regiões isoladas. [p=0.3] {B}B: [p=0.2] A "
        "cidadania é um direito de todos os seres humanos. [p=0.3] {C}C: [p=0.2] Por fim, [p=0.2] cabe ao governo resolver "
        "o problema do registro civil. [p=0.3] {D}D: [p=0.2] Muitos países têm sistemas eficientes de registro de "
        "nascimento. [p=0.3] {E}E: [p=0.2] Além disso, [p=0.2] a desinformação sobre a gratuidade do registro afasta "
        "famílias de baixa renda dos cartórios. [p=0.4] {p}Pause o vídeo e tente! [p=2.0]"),
    dict(id="29", block="q3", text=
        "{ok}Letra *E!* [p=0.3] {a}O segundo eixo da tese é a desinformação sobre a gratuidade. [p=0.2] A E retoma "
        "esse eixo, [p=0.2] afirma algo a provar [p=0.2] e usa um conectivo de adição. [p=0.4] {xa}A A repete o "
        "primeiro eixo [p=0.2] e ainda usa *em primeiro lugar.* [p=0.3] {xb}A B é genérica. [p=0.3] {xc}A C antecipa a "
        "*proposta,* [p=0.2] a solução, [p=0.2] papel da conclusão. [p=0.3] {xd}E a D sai do *recorte* brasileiro."),

    # ================= RECAPITULAÇÃO FINAL E PONTE =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, [p=0.2] as mesmas três frases. [p=0.3] {a}Tópico frasal é a etiqueta do item: [p=0.2] eixo mais o "
        "que vou provar. [p=0.6] {b}Tese mais tópicos em sequência: [p=0.2] tem que fazer sentido sozinho. [p=0.6] "
        "{c}Conectivo pela relação, [p=0.2] não por hábito. [p=0.5]"),
    dict(id="31", block="ponte", text=
        "{a}A etiqueta diz *o que* chegou. [p=0.4] {b}Agora é preciso dizer *por que* esse item está na caixa [p=0.2] {c}e "
        "mostrar a *nota fiscal.* [p=0.4] {d}Próximo episódio: [p=0.2] *argumento e repertório.*"),

    # ================= CTA =================
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual conectivo você costuma usar para abrir o segundo parágrafo? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
