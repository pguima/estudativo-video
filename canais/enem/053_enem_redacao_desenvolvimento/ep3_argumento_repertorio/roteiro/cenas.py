# Roteiro — Redação ENEM, Desenvolvimento, Episódio 3 de 7: Argumento e repertório — explicar e comprovar
# Base: Estudos/Enem/estudos/06-redacao/03-desenvolvimento.html — seções 04 e 05 + Questões 8 e 4 da seção 12.
#   Tipos de argumento e Repertório sociocultural têm séries próprias: aqui só a LISTA de estratégias da Cartilha (sem
#   ensinar cada tipo) e só as três orientações da Cartilha de 2026 contra o repertório de bolso. Contraexemplo "nome da
#   obra sem conteúdo" = frase do meio da Versão 2 da seção 09.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora da SÉRIE: cada parágrafo de desenvolvimento ENTREGA UM ITEM. Hoje, as etapas 2 e 3:
#   argumento = POR QUE ESSE ITEM ESTÁ NA CAIXA · repertório = NOTA FISCAL (QUEM/O QUÊ · CONTEÚDO · FONTE CERTA).
#   Abertura concreta (prompt do usuário): o vendedor do liquidificador — "é ótimo" (afirmação) → "porque tem motor de
#   1000 W" (argumento) → selo do Inmetro (comprovação de fora).
# Frases-chave (meio e fim, idênticas):
#   1. Afirmou? Explique o porquê.  2. Repertório é nota fiscal: nome e conteúdo certos.
#   3. Paráfrase curta, atribuição certa; na dúvida, não atribua.
# FIDELIDADE: só as referências do material (O Alienista / Machado de Assis / Simão Bacamarte / Casa Verde / Itaguaí,
#   Lei nº 10.216/2001, Constituição de 1988, Estatuto da Pessoa Idosa; Aristóteles só como alternativa B da Q4).
#   Lidos EXATAMENTE: tópico e argumento da seção 04, lista de estratégias, definição da Cartilha, 3 orientações de 2026,
#   tabela "Como apresentar" (seção 05), Questões 8 e 4. Q8: "comparação entre situações" é o termo da Cartilha (não
#   chamar de analogia). Nenhum nível ou nota da C3. Números e anos falados por extenso.
# Cores: azul = definição · verde = dica/método · âmbar = armadilha · vermelho = erro · roxo = regra oficial (Cartilha).

TITULO = "Sua Redação Só Tem Opinião? Argumento e Repertório que Convencem | Desenvolvimento da Redação Ep. 3"
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
        "{a}Opinião, [p=0.2] todo mundo tem. [p=0.5] {b}*Argumento* é a razão [p=0.2] que faz o outro *aceitar* a sua "
        "opinião. [p=0.5] {c}Hoje você vai ver a *frase* [p=0.2] que transforma uma coisa na outra."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai *explicar* uma afirmação com *causa e consequência* [p=0.4] {b}e "
        "apresentar um *repertório* com nome, [p=0.2] conteúdo [p=0.2] e atribuição corretos. [p=0.4] {c}E calma: [p=0.2] "
        "cada palavra nova vai ser explicada, [p=0.2] uma de cada vez."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Antes, [p=0.2] uma revisão relâmpago do episódio dois. [p=0.3] {a}O *tópico frasal* é a frase, [p=0.2] em "
        "geral a primeira do parágrafo, [p=0.2] que anuncia o que ele vai provar. [p=0.3] {b}Na nossa entrega, [p=0.2] ele "
        "é a *etiqueta do item.* [p=0.4] {c}E a gente parou nesta etiqueta, [p=0.2] do eixo da desinformação: [p=0.3] "
        "{d}Em primeiro lugar, [p=0.2] a desinformação sobre os transtornos mentais sustenta o estigma que os cerca."),

    # ================= CONCRETO ANTES DO ABSTRATO: O VENDEDOR =================
    dict(id="04", block="vendedor", text=
        "{t}Agora imagine uma loja. [p=0.3] {a}O vendedor diz: [p=0.2] este liquidificador é *ótimo.* [p=0.3] Isso é uma "
        "*afirmação.* [p=0.2] Você já acredita? [p=0.4] {b}Aí ele explica: [p=0.2] *porque* tem motor de mil watts. "
        "[p=0.3] Agora você tem uma *razão.* [p=0.4] {c}E por fim ele mostra o *selo do Inmetro:* [p=0.2] uma prova que "
        "vem *de fora* da loja. [p=0.4] {d}Afirmar, [p=0.2] explicar, [p=0.2] comprovar. [p=0.3] É isso que o seu "
        "parágrafo faz."),
    dict(id="05", block="analogia", text=
        "{t}Lembra da nossa entrega? [p=0.2] Cada parágrafo entrega um item, [p=0.2] em cinco etapas. [p=0.4] {a}Hoje "
        "são as etapas dois e três. [p=0.3] {b}O *argumento* é o *por que* esse item está na caixa. [p=0.4] {c}E o "
        "*repertório* é a *nota fiscal:* [p=0.2] a prova que vem de fora, [p=0.2] com nome e conteúdo certos."),

    # ================= BLOCO A: DEPOIS DE AFIRMAR, EXPLICAR =================
    dict(id="06", block="argumento", text=
        "{t}Então, [p=0.2] o que vem depois da etiqueta? [p=0.4] {a}Depois de afirmar, [p=0.2] o parágrafo precisa "
        "*explicar:* [p=0.3] {b}por que a afirmação do tópico frasal *procede?* [p=0.4] {c}Essa explicação é o "
        "*argumento:* [p=0.2] a razão que torna a sua tese aceitável. [p=0.4] {d}É o motor de mil watts do "
        "liquidificador."),
    dict(id="07", block="eufaco", text=
        "{t}Agora eu faço, [p=0.2] ao vivo, [p=0.2] no rascunho. [p=0.3] Primeiro, [p=0.2] a etiqueta. [p=0.2] {s1}Em "
        "primeiro lugar, [p=0.2] a desinformação sobre os transtornos mentais sustenta o estigma que os cerca. [p=0.5] "
        "{m}Agora eu me pergunto: [p=0.2] *por quê?* [p=0.3] O que acontece quando ninguém fala do assunto? [p=0.5] "
        "{s2}Como pouco se discute saúde mental nas escolas e nas famílias, [p=0.2] sintomas como a tristeza persistente "
        "ou a ansiedade intensa [p=0.2] costumam ser interpretados como fraqueza de caráter, [p=0.2] e não como condições "
        "que têm tratamento."),
    dict(id="08", block="eufaco", text=
        "{t}Repare no que essa frase faz. [p=0.3] {a}Ela tem uma relação de *causa e consequência:* [p=0.2] uma coisa "
        "*provoca* a outra. [p=0.4] {b}A causa: [p=0.2] *como* pouco se discute saúde mental. [p=0.4] {c}A consequência: "
        "[p=0.2] os sintomas *costumam ser interpretados* como fraqueza. [p=0.4] {d}Ou seja: [p=0.2] a falta de "
        "informação *produz* a leitura preconceituosa."),
    dict(id="09", block="solto", text=
        "{t}Agora compare. [p=0.3] {a}À esquerda, [p=0.2] só o tópico frasal. [p=0.2] Ele afirma, [p=0.2] e fica *solto* "
        "no ar. [p=0.4] {b}À direita, [p=0.2] o tópico com o argumento embaixo. [p=0.2] Agora a afirmação tem um "
        "*porquê.* [p=0.4] {c}Sem essa frase, [p=0.2] o tópico frasal ficaria como *afirmação solta.* [p=0.3] {d}Seria o "
        "vendedor dizendo ótimo [p=0.2] e indo embora."),

    # ================= BLOCO B: AS ESTRATÉGIAS DA CARTILHA (SÓ A LISTA) =================
    dict(id="10", block="estrategias", text=
        "{t}E com o que se sustenta um argumento? [p=0.4] {a}A *Cartilha do Participante,* [p=0.2] o guia oficial da "
        "redação, [p=0.2] lista *estratégias argumentativas:* [p=0.2] recursos para sustentar uma ideia. [p=0.4] "
        "{e1}Exemplos, [p=0.2] {e2}dados estatísticos, [p=0.2] {e3}pesquisas, [p=0.2] {e4}fatos comprováveis, [p=0.2] "
        "{e5}citações ou depoimentos de pessoas especializadas, [p=0.2] {e6}pequenas narrativas ilustrativas, [p=0.2] "
        "{e7}alusões históricas [p=0.2] {e8}e comparações entre fatos, situações, épocas ou lugares. [p=0.4] {s}Cada tipo "
        "tem série própria: [p=0.2] *Tipos de argumento.* [p=0.2] Aqui, [p=0.2] você só precisa conhecer a lista."),

    # ================= BLOCO C: O REPERTÓRIO =================
    dict(id="11", block="repertorio", text=
        "{t}E a nota fiscal? [p=0.2] O que conta como prova de fora? [p=0.4] {a}Esse é o *repertório sociocultural:* "
        "[p=0.2] o conhecimento que você traz de fora da prova. [p=0.4] {b}Na definição da Cartilha, [p=0.2] é uma "
        "informação, [p=0.2] um fato, [p=0.2] uma citação [p=0.2] ou uma experiência vivida [p=0.2] que, relacionada ao "
        "tema, [p=0.2] contribui como argumento. [p=0.4] {c}No parágrafo, [p=0.2] ele *comprova* [p=0.2] ou *ilustra* o "
        "argumento."),
    dict(id="12", block="nota", text=
        "{t}Pense numa nota fiscal de verdade. [p=0.4] {a}Ela diz *quem* "
        "vendeu [p=0.2] e *o quê.* [p=0.3] {b}Diz o *conteúdo:* [p=0.2] o que, exatamente, foi entregue. [p=0.3] {c}E "
        "precisa vir da *fonte certa.* [p=0.4] {d}Com o repertório é igual: [p=0.2] nome, [p=0.2] conteúdo [p=0.2] e "
        "atribuição corretos. [p=0.3] {e}*Atribuição* é dizer de quem é a ideia: [p=0.2] o autor ou a origem certa."),

    # ================= BLOCO D: AS TRÊS ORIENTAÇÕES CONTRA O REPERTÓRIO DE BOLSO =================
    dict(id="13", block="bolso", text=
        "{t}Mas tem uma nota fiscal *falsa* que aparece muito. [p=0.4] {a}É o *repertório de bolso:* [p=0.2] uma citação "
        "decorada, [p=0.2] pronta, [p=0.2] que a pessoa encaixa em *qualquer* tema. [p=0.4] {b}Para evitar isso, [p=0.2] "
        "a Cartilha de dois mil e vinte e seis dá três orientações. [p=0.4] {o1}Um: [p=0.2] escolher referências "
        "específicas que realmente tenham relação com o tema. [p=0.4] {o2}Dois: [p=0.2] articular o repertório às ideias "
        "usadas para defender o ponto de vista. [p=0.2] Articular é *amarrar.* [p=0.4] {o3}Três: [p=0.2] mostrar que "
        "entende o conteúdo citado e que ele fortalece a tese."),

    # ================= BLOCO E: COMO APRESENTAR =================
    dict(id="14", block="apresentar", text=
        "{t}Então, [p=0.2] como se apresenta uma referência? [p=0.4] {a}Primeiro modelo: [p=0.2] *quem ou o quê,* "
        "[p=0.2] mais o *conteúdo exato.* [p=0.4] {b}Em O Alienista, [p=0.2] de Machado de Assis, [p=0.2] o médico Simão "
        "Bacamarte recolhe à Casa Verde a maior parte da população de Itaguaí. [p=0.4] {c}Repare: [p=0.2] tem a obra, "
        "[p=0.2] o autor [p=0.2] e o que acontece nela. [p=0.4] {d}E é uma obra de *domínio público:* [p=0.2] um clássico "
        "livre, [p=0.2] que qualquer pessoa pode ler e conferir."),
    dict(id="15", block="apresentar", text=
        "{t}Agora compare com esta frase. [p=0.3] {a}Machado de Assis escreveu O Alienista, [p=0.2] obra muito importante "
        "da literatura brasileira. [p=0.4] {b}Tem nome? [p=0.2] Tem. [p=0.3] {c}Tem conteúdo? [p=0.2] *Não.* [p=0.2] A "
        "frase não diz o que a obra *mostra.* [p=0.4] {d}É uma nota fiscal sem a lista do que foi entregue."),
    dict(id="16", block="apresentar", text=
        "{t}O segundo modelo serve para leis: [p=0.2] {a}a *lei,* [p=0.2] mais o que ela *determina.* [p=0.4] {b}A Lei "
        "número dez mil duzentos e dezesseis, [p=0.2] de dois mil e um, [p=0.2] que trata dos direitos das pessoas com "
        "transtornos mentais, [p=0.2] redirecionou o modelo de assistência em saúde mental. [p=0.5] {c}O terceiro serve "
        "para fatos: [p=0.2] o *fato histórico,* [p=0.2] mais uma *data segura,* [p=0.2] uma data de que você tem "
        "certeza. [p=0.4] {d}Promulgada em mil novecentos e oitenta e oito, [p=0.2] a Constituição Federal, [p=0.2] e a "
        "frase continua. [p=0.3] {e}Promulgada quer dizer [p=0.2] oficialmente publicada."),

    # ================= BLOCO F: PREFIRA A PARÁFRASE =================
    dict(id="17", block="parafrase", text=
        "{t}E aquelas frases famosas, [p=0.2] entre aspas? [p=0.4] {a}*Citação* é copiar as palavras exatas de alguém, "
        "[p=0.2] entre aspas. [p=0.3] {b}*Paráfrase* é dizer a mesma ideia [p=0.2] com as *suas* palavras. [p=0.4] "
        "{c}Citações longas entre aspas ocupam linhas [p=0.2] e raramente são lembradas com exatidão. [p=0.4] {d}Então: "
        "[p=0.2] parafraseie a ideia, [p=0.2] atribua corretamente [p=0.2] e gaste as linhas na *análise.*"),
    dict(id="18", block="parafrase", text=
        "{t}E se você não lembra direito quem disse? [p=0.4] {a}Se não tiver certeza da autoria [p=0.2] ou do conteúdo, "
        "[p=0.2] *não atribua.* [p=0.4] {b}Apresente a ideia como *argumento seu.* [p=0.4] {c}Uma ideia sua, bem "
        "explicada, [p=0.2] vale mais do que uma nota fiscal com o nome errado."),

    # ================= NÓS FAZEMOS =================
    dict(id="19", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Olhe esta frase: [p=0.2] A Lei número dez mil duzentos e dezesseis, [p=0.2] de dois mil e "
        "um, [p=0.2] é muito importante. [p=0.4] {b}Tem o nome. [p=0.2] Mas e o conteúdo? [p=0.4] {c}Pause o vídeo [p=0.2] "
        "e reescreva usando o modelo: [p=0.2] *lei,* [p=0.2] mais *o que ela determina.* [p=0.3] {p}Pause agora. [p=2.0]"),
    dict(id="20", block="exercicio", text=
        "{a}Conferindo. [p=0.3] {s}A Lei número dez mil duzentos e dezesseis, [p=0.2] de dois mil e um, [p=0.2] que trata "
        "dos direitos das pessoas com transtornos mentais, [p=0.2] redirecionou o modelo de assistência em saúde mental. "
        "[p=0.4] {b}O muito importante virou *o que a lei faz.* [p=0.3] {c}A sua versão não precisa ser igual: [p=0.2] "
        "precisa dizer o que a lei *determina,* [p=0.2] só com o que você tem certeza."),

    # ================= RECAPITULAÇÃO DO MEIO =================
    dict(id="21", block="recap", text=
        "{t}Três frases para guardar. [p=0.3] {a}Afirmou? [p=0.2] Explique o porquê. [p=0.6] {b}Repertório é nota fiscal: "
        "[p=0.2] nome e conteúdo certos. [p=0.6] {c}Paráfrase curta, [p=0.2] atribuição certa; [p=0.2] na dúvida, [p=0.2] "
        "não atribua. [p=0.5]"),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erros", text=
        "{a}Erro um: [p=0.2] afirmar e passar *direto* para o exemplo, [p=0.2] sem explicar. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque o exemplo parece provar tudo sozinho. [p=0.4] {c}Mas opinião repetida não é argumento: [p=0.2] "
        "diga *por que* a afirmação procede."),
    dict(id="23", block="erros", text=
        "{a}Erro dois: [p=0.2] citar o *nome* da obra [p=0.2] sem dizer o que ela mostra. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque um nome famoso impressiona. [p=0.4] {c}Mas repertório mencionado sem uso tende a não ser "
        "produtivo: [p=0.2] resuma o *conteúdo* [p=0.2] e use."),
    dict(id="24", block="erros", text=
        "{a}Erro três: [p=0.2] decorar uma citação longa [p=0.2] e errar palavras ou autoria. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque aspas parecem prova de estudo. [p=0.4] {c}Mas o certo é *paráfrase curta* [p=0.2] e atribuição "
        "correta. [p=0.2] Gaste as linhas na análise."),

    # ================= QUESTÃO 8 =================
    dict(id="25", block="q8", text=
        "{t}Agora, [p=0.2] duas questões no estilo do ENEM. [p=0.3] {a}Em um parágrafo sobre o tema do ENEM de dois mil e "
        "vinte e cinco, [p=0.2] lê-se: [p=0.3] Assim como as cidades brasileiras foram redesenhadas, [p=0.2] ao longo do "
        "século vinte, [p=0.2] para a circulação dos automóveis, [p=0.2] precisam agora ser adaptadas para quem caminha "
        "mais devagar. [p=0.4] {b}A estratégia argumentativa predominante nesse trecho é a: [p=0.3] {A}A: [p=0.2] citação "
        "de autoridade. [p=0.3] {B}B: [p=0.2] apresentação de dado estatístico. [p=0.3] {C}C: [p=0.2] narrativa "
        "ilustrativa."),
    dict(id="26", block="q8", text=
        "{D}D: [p=0.2] comparação entre situações. [p=0.3] {E}E: [p=0.2] definição de conceito. [p=0.4] {p}Pause o vídeo "
        "e tente! [p=2.0]"),
    dict(id="27", block="q8", text=
        "{ok}Letra *D!* [p=0.3] Assim como, [p=0.2] precisam agora: [p=0.2] o trecho *compara* duas situações, [p=0.2] a "
        "adaptação ao automóvel [p=0.2] e a adaptação ao envelhecimento. [p=0.3] É uma das estratégias da lista da "
        "Cartilha. [p=0.4] {xa}Não há especialista citado: [p=0.2] fora a A. [p=0.3] {xb}Não há número: [p=0.2] fora a B. "
        "[p=0.3] {xc}Não há história com personagens: [p=0.2] fora a C. [p=0.3] {xe}E nenhum termo é definido: [p=0.2] "
        "fora a E."),

    # ================= QUESTÃO 4 =================
    dict(id="28", block="q4", text=
        "{t}Questão quatro. [p=0.2] Tema do ENEM de dois mil e vinte e cinco: [p=0.2] Perspectivas acerca do envelhecimento "
        "na sociedade brasileira. [p=0.4] {a}O trecho de desenvolvimento em que o repertório é usado de forma produtiva é: "
        "[p=0.4] {A}A: [p=0.2] O Estatuto da Pessoa Idosa atribui à família, [p=0.2] à sociedade e ao poder público "
        "[p=0.2] o dever de assegurar à pessoa idosa direitos como a convivência comunitária. [p=0.3] Muitas cidades, "
        "porém, [p=0.2] não têm calçadas acessíveis nem espaços de convivência, [p=0.2] o que confina idosos em casa "
        "[p=0.2] e transforma esse direito em promessa."),
    dict(id="29", block="q4", text=
        "{B}B: [p=0.2] Segundo Aristóteles, [p=0.2] o homem é um animal político. [p=0.2] Portanto, [p=0.2] o "
        "envelhecimento deve ser discutido por todos. [p=0.4] {C}C: [p=0.2] O Estatuto da Pessoa Idosa é uma lei "
        "brasileira. [p=0.2] Ele é muito importante para o país. [p=0.4] {D}D: [p=0.2] Como diz o ditado, [p=0.2] quem "
        "espera sempre alcança. [p=0.2] Por isso, [p=0.2] os idosos devem ter paciência. [p=0.4] {E}E: [p=0.2] Conforme o "
        "texto motivador da prova, [p=0.2] a população idosa cresceu no Brasil. [p=0.4] {p}Pause o vídeo e tente! "
        "[p=2.0]"),
    dict(id="30", block="q4", text=
        "{ok}Letra *A!* [p=0.3] Olhe as três marcas. [p=0.3] {m1}Primeiro, [p=0.2] ela apresenta o *conteúdo* da lei: "
        "[p=0.2] o dever de assegurar a convivência comunitária. [p=0.4] {m2}Depois, [p=0.2] *confronta* esse direito com "
        "a realidade das cidades: [p=0.2] sem calçadas acessíveis, [p=0.2] sem espaços de convivência. [p=0.4] {m3}E "
        "mostra a *consequência:* [p=0.2] o confinamento dos idosos em casa. [p=0.4] {f}Tudo ligado a uma perspectiva "
        "sobre o envelhecimento no Brasil."),
    dict(id="31", block="q4", text=
        "{xb}A B é o *repertório de bolso* citado pela Cartilha de dois mil e vinte e seis. [p=0.4] {xc}A C menciona a "
        "lei [p=0.2] sem dizer o que ela determina nem usá-la. [p=0.4] {xd}A D usa um ditado sem relação com o "
        "argumento, [p=0.2] e chega a uma conclusão desrespeitosa à espera dos idosos. [p=0.4] {xe}E a E apenas retoma a "
        "*coletânea,* [p=0.2] os textos motivadores da prova: [p=0.2] isso não é repertório sociocultural."),

    # ================= RECAPITULAÇÃO FINAL E PONTE =================
    dict(id="32", block="recap", text=
        "{t}Para fechar, [p=0.2] as mesmas três frases. [p=0.3] {a}Afirmou? [p=0.2] Explique o porquê. [p=0.6] "
        "{b}Repertório é nota fiscal: [p=0.2] nome e conteúdo certos. [p=0.6] {c}Paráfrase curta, [p=0.2] atribuição "
        "certa; [p=0.2] na dúvida, [p=0.2] não atribua. [p=0.5]"),
    dict(id="33", block="ponte", text=
        "{a}Mas mostrar a nota fiscal *não basta.* [p=0.4] {b}O cliente quer ver o *produto funcionando* na casa dele. "
        "[p=0.4] {c}Próximo episódio: [p=0.2] a *análise* e o *fechamento,* [p=0.2] as duas partes que mais separam um "
        "parágrafo médio de um excelente."),

    # ================= CTA =================
    dict(id="34", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual referência você já citou só pelo nome, [p=0.2] sem dizer o "
        "conteúdo? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os "
        "*flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos "
        "por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
