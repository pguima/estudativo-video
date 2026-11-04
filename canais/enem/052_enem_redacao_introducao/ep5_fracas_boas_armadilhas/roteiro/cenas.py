# Roteiro — Redação ENEM, Introdução, Episódio 5 de 7: Introduções fracas × boas, lado a lado — e as armadilhas do primeiro parágrafo
# Base: Estudos/Enem/estudos/06-redacao/02-introducao.html — seções 07 e 08 + Questão 1 da seção 12 (tema de 2025).
# Prompt: _material/prompts_02-introducao.md, "Vídeo 5".
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia da série: a introdução é a ETIQUETA COMPLETA DA ENCOMENDA — MAPA (contextualização) · RUA DE ACESSO (ponte) ·
#   ENDEREÇO + ENTREGA (tese) · LISTA DA CAIXA (antecipação). Repertório de bolso = cartão-postal genérico.
# Lidos EXATAMENTE como no material: as três versões da seção 07 (com o aviso "elaborado para fins didáticos" na tela),
#   o quadro "o que mudou", os exemplos da tabela de armadilhas da seção 08, a Questão 1 e as alternativas.
# Tamanho: "entre um quinto e um quarto do texto" = SUGESTÃO de professores, não regra (dito e mostrado).
# "Parece certo porque..." de cada armadilha: explicação didática deste roteiro (não é citação do material).
# Fidelidade: nenhuma lei, número ou citação fora do material (Lei nº 10.639/2003; Estatuto da Pessoa Idosa; Aristóteles e
#   Platão só como exemplos de repertório de bolso, como na Cartilha de 2026).
# Cores: azul = definição/tema · verde = método · amarelo = armadilha · vermelho = erro · roxo = regra oficial.

TITULO = "Aristóteles na Introdução? 3 Versões, Só 1 Funciona | Introdução da Redação Ep. 5"
# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo da folha em branco: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Nesta aula você compara introduções fracas e boas, como um "
            "detetive: leia os trechos de redação com calma e clareza, como quem lê um texto de verdade, faça as "
            "perguntas com suspense, mostre surpresa ao revelar cada pegadinha e entusiasmo quando a versão boa aparece. "
            "Ritmo didático e tranquilo, sem pressa, respeitando as pausas entre as frases. "
            "Leia apenas o texto, exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Três introduções para o *mesmo tema* do ENEM. [p=0.4] {b}Uma é *genérica.* [p=0.3] {c}Outra cita "
        "*Aristóteles.* [p=0.3] {d}A terceira não cita filósofo nenhum. [p=0.4] {e}Qual é a melhor? [p=0.5] {f}Quase todo "
        "mundo *erra.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai saber dizer *exatamente* por que uma introdução é fraca, [p=0.3] {b}e como "
        "*consertá-la.*"),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Antes, [p=0.2] uma revisão relâmpago. [p=0.3] {a}A introdução é a *etiqueta completa da encomenda.* [p=0.3] "
        "{b}O *mapa* é a contextualização: [p=0.2] de onde parte a discussão. [p=0.3] {c}A *rua de acesso* é a ponte, "
        "[p=0.2] que leva a referência até o recorte do tema. [p=0.3] {d}Tirou a referência e nada mudou? [p=0.2] Ela não "
        "trabalhava: [p=0.2] é o *teste da retirada.* [p=0.3] {e}O *endereço com a entrega* é a tese, [p=0.2] a sua posição. "
        "[p=0.3] {f}E a *lista da caixa* anuncia os dois eixos [p=0.2] que o desenvolvimento vai cumprir."),

    # ================= CONCRETO: TRÊS ETIQUETAS =================
    dict(id="04", block="etiquetas", text=
        "{t}Agora imagine três etiquetas para o *mesmo endereço.* [p=0.4] {a}A primeira diz só: [p=0.2] para alguém, em algum "
        "lugar. [p=0.4] {b}A segunda tem um *cartão-postal* bonito colado, [p=0.2] que serviria para qualquer cidade. "
        "[p=0.4] {c}A terceira tem mapa, [p=0.2] rua, [p=0.2] endereço [p=0.2] e lista da caixa. [p=0.4] {d}Qual encomenda "
        "chega? [p=0.3] Só a terceira. [p=0.3] {e}Com as introduções, [p=0.2] é igual."),
    dict(id="05", block="tema", text=
        "{a}O tema é do ENEM de dois mil e vinte e quatro: [p=0.2] *Desafios para a valorização da herança africana no "
        "Brasil.* [p=0.4] {b}As três versões foram elaboradas para fins didáticos. [p=0.3] {c}Vou ler cada uma [p=0.2] e "
        "marcar na etiqueta [p=0.2] o que tem, [p=0.2] e o que falta."),

    # ================= VERSÃO 1: GENÉRICA =================
    dict(id="06", block="v1", text=
        "{t}Versão um. [p=0.4] {a}Desde os primórdios da humanidade, a cultura é fundamental para todos os povos. [p=0.4] "
        "{b}Nesse sentido, a herança africana também é importante e deve ser valorizada. [p=0.4] {c}Portanto, é necessário "
        "discutir esse tema. [p=0.8]"),
    dict(id="07", block="v1", text=
        "{a}Parece bonita, não parece? [p=0.2] Soa formal. [p=0.4] {m}Mas olhe o mapa: [p=0.2] a primeira frase serviria para "
        "*qualquer tema.* [p=0.3] É uma *introdução genérica:* [p=0.2] caberia em qualquer redação. [p=0.4] {t2}E a tese? "
        "[p=0.2] Deve ser valorizada... [p=0.2] quase ninguém discordaria. [p=0.2] Não é contestável. [p=0.4] {l}Na lista da "
        "caixa, [p=0.2] *nada* é antecipado. [p=0.4] {f}E a última frase só anuncia que vai haver discussão. [p=0.4] "
        "{r}Resultado: [p=0.2] argumentação previsível na C dois, [p=0.2] e projeto de texto pouco visível na C três."),

    # ================= VERSÃO 2: REPERTÓRIO DE BOLSO =================
    dict(id="08", block="v2", text=
        "{t}Versão dois. [p=0.4] {a}Segundo Aristóteles, o homem é um animal político. [p=0.4] {b}Dessa forma, a valorização "
        "da herança africana no Brasil é um desafio que precisa ser enfrentado por toda a sociedade. [p=0.8]"),
    dict(id="09", block="v2", text=
        "{a}Essa parece ótima: [p=0.2] tem filósofo! [p=0.4] {b}Mas a citação não se liga ao recorte. [p=0.3] É o "
        "cartão-postal genérico, [p=0.2] o que a Cartilha de dois mil e vinte e seis chama de *repertório de bolso:* [p=0.2] "
        "uma referência decorada, [p=0.2] que serve para qualquer tema. [p=0.4] {x}Faça o teste da retirada: [p=0.2] apague "
        "Aristóteles. [p=0.4] {y}O texto muda? [p=0.3] Não muda nada. [p=0.4] {c}E a tese só *repete o tema,* [p=0.2] com "
        "outras palavras. [p=0.4] {d}Atenção: [p=0.2] o problema não é o autor. [p=0.2] É o *encaixe.*"),

    # ================= VERSÃO 3: BOA =================
    dict(id="10", block="v3", text=
        "{t}Versão três. [p=0.4] {a}Sancionada em dois mil e três, a Lei número dez mil seiscentos e trinta e nove tornou "
        "obrigatório o ensino de história e cultura afro-brasileira nas escolas do país, reconhecendo a contribuição "
        "africana na formação nacional. [p=0.4] {b}Mais de duas décadas depois, porém, essa herança ainda é frequentemente "
        "reduzida a estereótipos ou lembrada apenas em datas comemorativas. [p=0.4] {c}Esse quadro decorre, sobretudo, da "
        "aplicação irregular da lei nas escolas e da pouca visibilidade da cultura afro-brasileira nos meios de "
        "comunicação, [p=0.2] obstáculos que precisam ser enfrentados para que essa herança seja, de fato, valorizada no "
        "Brasil. [p=0.8]"),
    dict(id="11", block="v3", text=
        "{a}Sem filósofo nenhum, [p=0.2] e é a melhor. [p=0.4] {m}Mapa: [p=0.2] uma lei *legítima* [p=0.2] e *pertinente.* "
        "[p=0.3] Legitimar um repertório é usar uma fonte real, [p=0.2] que dá para conferir; [p=0.2] pertinente é ligada ao "
        "tema. [p=0.4] {r}Rua de acesso: [p=0.2] a segunda frase faz a ponte: [p=0.2] o que a lei prevê, [p=0.2] contra o que "
        "acontece. [p=0.4] {e}Endereço: [p=0.2] a tese cobre o recorte inteiro: [p=0.2] desafios, [p=0.2] valorização, "
        "[p=0.2] herança africana, [p=0.2] Brasil. [p=0.4] {l}E a lista da caixa: [p=0.2] dois eixos, [p=0.2] a *escola* "
        "[p=0.2] e a *mídia.*"),
    dict(id="12", block="mudou", text=
        "{t}O que mudou da versão um para a três? [p=0.4] {a}Contexto genérico [p=0.2] virou referência verificável, ligada "
        "ao recorte. [p=0.4] {b}Importância [p=0.2] virou posição contestável. [p=0.4] {c}Nenhum caminho [p=0.2] virou dois "
        "eixos anunciados."),

    # ================= NÓS FAZEMOS =================
    dict(id="13", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Olhe de novo a versão um. [p=0.3] {b}Qual peça da etiqueta você consertaria *primeiro,* "
        "[p=0.2] e como? [p=0.3] {p}Pause e responda. [p=2.0]"),
    dict(id="14", block="exercicio", text=
        "{a}Uma boa resposta: [p=0.2] comece pelo *endereço,* [p=0.2] a tese. [p=0.3] Sem posição, [p=0.2] não há o que "
        "contextualizar. [p=0.4] {b}Depois, [p=0.2] troque o desde os primórdios por uma referência ligada ao recorte, "
        "[p=0.2] como a lei. [p=0.3] {c}Faça a ponte, [p=0.3] {d}e anuncie os dois eixos. [p=0.4] {e}Foi exatamente o "
        "caminho que levou à versão três."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="15", block="recap", text=
        "{t}Três frases para guardar. [p=0.3] {a}Serve para qualquer tema? [p=0.2] Não serve para o seu. [p=0.5] "
        "{b}Citação decorada não trabalha; [p=0.2] referência com ponte trabalha. [p=0.5] {c}Pergunta não é tese; [p=0.2] "
        "argumento fica para o desenvolvimento."),

    # ================= AS 7 ARMADILHAS (SEÇÃO 08) =================
    dict(id="16", block="armadilhas", text=
        "{t}Agora, [p=0.2] as sete armadilhas do primeiro parágrafo. [p=0.3] Quatro aparecem na *abertura.* [p=0.4] {a1}Um: "
        "[p=0.2] a *abertura universal.* [p=0.2] Desde os primórdios... [p=0.2] Hoje em dia, muito se fala sobre... [p=0.3] "
        "{p1}Parece um começo seguro, [p=0.2] mas não informa nada sobre o recorte."),
    dict(id="17", block="armadilhas", text=
        "{a2}Dois: [p=0.2] a *citação decorada,* [p=0.2] a frase de pensador encaixada em qualquer tema. [p=0.3] {p2}Parece "
        "erudição, [p=0.2] mas é repertório de bolso, [p=0.2] que tende a não ser produtivo. [p=0.4] {a3}Três: [p=0.2] a "
        "*autoria duvidosa:* [p=0.2] uma frase famosa, atribuída a alguém sem certeza. [p=0.3] {p3}Parece citação de "
        "respeito, [p=0.2] mas repertório precisa ser legitimado."),
    dict(id="18", block="armadilhas", text=
        "{a4}Quatro: [p=0.2] o *dado sem fonte.* [p=0.2] Pesquisas mostram que noventa por cento... [p=0.3] {p4}Parece "
        "preciso, [p=0.2] mas número que não se pode verificar fragiliza o argumento. [p=0.4] {k}O conserto das quatro é o "
        "mesmo: [p=0.2] uma referência real, [p=0.2] ligada ao recorte."),
    dict(id="19", block="armadilhas", text=
        "{t}As outras três aparecem no *fechamento* da introdução. [p=0.4] {a5}Cinco: [p=0.2] a *pergunta sem resposta.* "
        "[p=0.2] É a pergunta retórica, [p=0.2] feita só para impressionar: [p=0.2] Até quando isso vai continuar? [p=0.3] "
        "{p5}Parece um final forte, [p=0.2] mas a pergunta não substitui a tese."),
    dict(id="20", block="armadilhas", text=
        "{a6}Seis: [p=0.2] a introdução que *já argumenta,* [p=0.2] com exemplos e explicações que seriam do desenvolvimento. "
        "[p=0.3] {p6}Parece caprichada, [p=0.2] mas a introdução incha, [p=0.2] e os eixos se repetem depois. [p=0.4] "
        "{a7}Sete: [p=0.2] a tese que *tangencia.* [p=0.2] Tangenciar é ficar só no assunto amplo, [p=0.2] sem o recorte "
        "completo. [p=0.3] {p7}Parece estar no tema, [p=0.2] mas compromete o texto inteiro desde o início."),
    dict(id="21", block="tamanho", text=
        "{t}E o tamanho? [p=0.3] {a}*Não há tamanho oficial.* [p=0.4] {b}Muitos professores sugerem que a introdução ocupe "
        "algo entre *um quinto e um quarto* do texto, [p=0.3] porque o desenvolvimento precisa de mais linhas. [p=0.4] "
        "{c}É sugestão, [p=0.2] não regra. [p=0.3] {d}Mas, se a sua passou disso, [p=0.2] provavelmente está argumentando "
        "antes da hora."),

    # ================= QUESTÃO 1 (TEMA DE 2025) =================
    dict(id="22", block="q1", text=
        "{t}Agora, [p=0.2] uma questão no estilo do ENEM. [p=0.3] {a}Para o tema do ENEM dois mil e vinte e cinco, [p=0.2] "
        "Perspectivas acerca do envelhecimento na sociedade brasileira, [p=0.3] a introdução que contextualiza o tema, "
        "[p=0.2] apresenta uma tese sobre o recorte completo [p=0.2] e antecipa os argumentos é: [p=0.4] {A}A: [p=0.2] "
        "Desde sempre, os seres humanos envelhecem. Isso é algo natural e que acontece com todos. Portanto, é importante "
        "refletir sobre o envelhecimento. [p=0.4] {B}B: [p=0.2] O envelhecimento das células é estudado pela biologia há "
        "séculos. Os cientistas descobriram que o corpo perde funções com o tempo. Esse processo atinge todos os seres "
        "vivos."),
    dict(id="23", block="q1", text=
        "{C}C: [p=0.2] O Estatuto da Pessoa Idosa assegura às pessoas com sessenta anos ou mais direitos como saúde, "
        "dignidade e convivência comunitária. No Brasil, contudo, a velhice ainda é vista sobretudo como perda, o que "
        "alimenta o etarismo e atrasa a adaptação das cidades a uma população que envelhece, [p=0.2] dois desafios que "
        "mostram a urgência de novas perspectivas sobre a velhice. [p=0.4] {D}D: [p=0.2] Segundo Platão, a sociedade ideal "
        "é governada pelos sábios. Assim, o envelhecimento é um tema que merece a atenção de todos. [p=0.4] {E}E: [p=0.2] "
        "No Japão, a população idosa é numerosa e o país criou diversos serviços para ela. Por isso, o envelhecimento "
        "japonês é um exemplo de organização para o mundo. [p=0.4] {p}Pause o vídeo e tente! [p=2.0]"),
    dict(id="24", block="q1", text=
        "{ok}Letra *C.* [p=0.3] Vamos passar pela etiqueta. [p=0.3] {c1}Mapa: [p=0.2] o Estatuto da Pessoa Idosa, [p=0.2] "
        "uma lei pertinente. [p=0.3] {c2}Rua de acesso: [p=0.2] no Brasil, contudo. [p=0.3] {c3}Endereço: [p=0.2] uma tese "
        "sobre as perspectivas acerca do envelhecimento. [p=0.3] {c4}E a lista: [p=0.2] dois eixos, [p=0.2] o etarismo, "
        "[p=0.2] que é o preconceito contra os mais velhos, [p=0.2] e a adaptação das cidades."),
    dict(id="25", block="q1", text=
        "{xa}A A é genérica: [p=0.2] serve para qualquer tema [p=0.2] e não tem tese contestável. [p=0.4] {xb}A B é a "
        "pegadinha: [p=0.2] fica no processo biológico, universal, [p=0.2] e esse é o *exemplo oficial* de tangenciamento "
        "para esse tema. [p=0.4] {xd}A D usa Platão de forma genérica, [p=0.2] como repertório de bolso, [p=0.2] e não toma "
        "posição. [p=0.4] {xe}E a E sai do Brasil: [p=0.2] o recorte é a sociedade *brasileira.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="26", block="recap", text=
        "{t}Para fechar, [p=0.2] as mesmas três frases. [p=0.3] {a}Serve para qualquer tema? [p=0.2] Não serve para o seu. "
        "[p=0.5] {b}Citação decorada não trabalha; [p=0.2] referência com ponte trabalha. [p=0.5] {c}Pergunta não é tese; "
        "[p=0.2] argumento fica para o desenvolvimento."),

    # ================= PONTE E CTA =================
    dict(id="27", block="ponte", text=
        "{a}Chega de ver os outros escreverem. [p=0.4] {b}No próximo episódio, [p=0.2] você monta uma introdução *comigo,* "
        "[p=0.2] do zero, [p=0.3] {c}com um tema real do ENEM. [p=0.4] {d}Separe papel, [p=0.2] caneta [p=0.2] e duas cores."),
    dict(id="28", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual armadilha você já usou numa introdução? [p=0.5] "
        "{anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no "
        "*Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
