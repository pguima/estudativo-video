# Roteiro — Redação ENEM, Desenvolvimento, Episódio 4 de 7: Análise e fechamento — o "e daí?"
# Base: Estudos/Enem/estudos/06-redacao/03-desenvolvimento.html — seções 06 e 07 + Questões 2 e 5 da seção 12.
#   Modelagem ao vivo: os três degraus da figura da seção 06 com O Alienista. Exemplo × contraexemplo: citar × argumentar
#   e o fechamento bom × os três ruins da tabela da seção 07. Exercício "nós fazemos" com a Versão 2 da seção 09
#   (repertório solto) e a frase [4] do parágrafo-modelo da seção 08. Autoria e níveis da C3 só citados (série própria).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora da SÉRIE: cada parágrafo de desenvolvimento ENTREGA UM ITEM da lista colada na caixa, em cinco etapas.
#   Aqui, as duas últimas: análise = o PRODUTO FUNCIONANDO NA CASA DO CLIENTE (no Brasil de hoje) · fechamento = a
#   ASSINATURA DO RECIBO, que amarra o item entregue à tese. A pergunta do cliente: "E DAÍ?".
# Frases-chave (meio e fim, idênticas):
#   1. Citar é o primeiro degrau; argumentar é o terceiro.  2. Pergunte "e daí?" antes de fechar.
#   3. Fechamento retoma o eixo e liga à tese, sem informação nova.
# FIDELIDADE: comentário da Cartilha sobre a Constituição de 1988 com as palavras do material (07). "Mini-conclusão" é nome
#   de método, não termo oficial (15). Lidos EXATAMENTE como no material: degraus da seção 06 (09–11), perguntas de análise
#   (12–13), tabela de fechamentos (16–17), conectivos (18), Versão 2 da seção 09 (20), frase [4] da seção 08 (21),
#   Questão 2 (25–28) e Questão 5 (30–32). A análise da Questão 2 (29) é elaborada para fins didáticos, sem dado novo.
#   Nenhum nível ou nota da C3. Números e anos falados por extenso.
# Cores: azul = definição · verde = dica/método · âmbar = armadilha · vermelho = erro · roxo = regra oficial (Cartilha).

TITULO = "Citar Não É Argumentar: a Análise e o Fechamento do Parágrafo | Desenvolvimento da Redação Ep. 4"
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
        "{a}Você cita *Machado de Assis,* [p=0.3] {b}escreve: [p=0.2] dessa forma, [p=0.2] o problema é grave, [p=0.3] "
        "{c}e acha que *argumentou.* [p=0.5] {d}Faltou o *meio do caminho.* [p=0.4] {e}E é justamente o meio [p=0.2] "
        "que vale mais."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai escrever a *análise* [p=0.2] que faz a referência trabalhar, [p=0.3] "
        "{b}e a *frase final* [p=0.2] que devolve o parágrafo para a tese. [p=0.4] {c}E calma: [p=0.2] cada palavra nova "
        "vai ser explicada, [p=0.2] uma de cada vez."),

    # ================= PRÉ-REQUISITOS =================
    dict(id="03", block="prereq", text=
        "{t}Antes, [p=0.2] uma revisão relâmpago do episódio três. [p=0.3] {a}O *argumento* explica *por que* a "
        "afirmação do parágrafo procede: [p=0.2] é o porquê de o item estar na caixa. [p=0.4] {b}O *repertório* é o "
        "conhecimento de fora da prova que *comprova:* [p=0.2] a nota fiscal. [p=0.4] {c}Hoje, [p=0.2] as duas últimas "
        "etapas da entrega."),

    # ================= A ENTREGA (CONCRETO ANTES DO ABSTRATO) =================
    dict(id="04", block="entrega", text=
        "{t}Imagine dois entregadores. [p=0.3] {a}O primeiro mostra a *nota fiscal* do liquidificador [p=0.2] e vai "
        "embora. [p=0.4] {b}O segundo entra, [p=0.2] *liga* o liquidificador na cozinha do cliente [p=0.3] {c}e mostra "
        "que ele resolve o problema *dele.* [p=0.4] {d}Depois, [p=0.2] o cliente *assina o recibo.* [p=0.4] {e}Qual dos "
        "dois provou que o item serve?"),
    dict(id="05", block="analogia", text=
        "{t}No parágrafo, [p=0.2] é igual. [p=0.3] {a}A *análise* é o produto funcionando na casa do cliente: [p=0.2] a "
        "referência trabalhando no *Brasil de hoje.* [p=0.4] {b}O *fechamento* é a assinatura do recibo: [p=0.2] amarra "
        "o item entregue à *tese.* [p=0.4] {c}E, entre a nota fiscal e o recibo, [p=0.2] o cliente sempre pergunta: "
        "[p=0.2] *e daí?*"),

    # ================= BLOCO A: O QUE É ANÁLISE =================
    dict(id="06", block="analise", text=
        "{t}Mas o que transforma uma citação em argumento? [p=0.4] {a}A *análise,* [p=0.2] também chamada de "
        "*aprofundamento.* [p=0.3] É interpretar o repertório à luz do problema. [p=0.4] {b}Ou seja: [p=0.2] dizer o que "
        "ele mostra sobre a realidade *brasileira* [p=0.3] {c}e por que isso *sustenta a tese.* [p=0.4] {d}É na análise "
        "que aparece a *autoria:* [p=0.2] quando dá para perceber o *seu* raciocínio. [p=0.4] {e}Como o corretor pontua "
        "a autoria, [p=0.2] você vê na série da Competência três."),
    dict(id="07", block="analise", text=
        "{t}E a Cartilha do Participante, [p=0.2] o guia oficial da redação, [p=0.2] elogia exatamente isso. [p=0.4] "
        "{a}Ao comentar um uso produtivo da *Constituição de mil novecentos e oitenta e oito,* [p=0.3] {b}ela destaca que "
        "o texto estabelece uma relação lógica [p=0.2] entre o *antecedente histórico,* [p=0.2] o fato do passado, "
        "[p=0.2] {c}e a *realidade atual,* [p=0.3] {d}evidenciando a *distância* entre os direitos previstos [p=0.2] e "
        "sua efetivação. [p=0.4] {e}Passado ligado ao presente: [p=0.2] isso é análise."),

    # ================= BLOCO B: EU FAÇO — OS TRÊS DEGRAUS =================
    dict(id="08", block="escada", text=
        "{t}Agora eu faço, [p=0.2] ao vivo, [p=0.2] no rascunho. [p=0.3] A análise é uma *escada de três degraus.* "
        "[p=0.4] {a}Degrau um: [p=0.2] o que a referência mostra. [p=0.3] {b}Degrau dois: [p=0.2] como isso aparece no "
        "Brasil hoje. [p=0.3] {c}Degrau três: [p=0.2] o que isso prova para a tese."),
    dict(id="09", block="escada", text=
        "{a}Minha referência: [p=0.2] *O Alienista,* [p=0.2] de Machado de Assis. [p=0.3] O médico Simão Bacamarte "
        "recolhe à Casa Verde [p=0.2] a maior parte da população de Itaguaí. [p=0.4] {b}O que isso mostra? [p=0.3] Deixa "
        "eu pensar... [p=0.3] {c}O rótulo de *louco* [p=0.2] servia para *excluir.* [p=0.4] {d}Primeiro degrau. [p=0.2] "
        "Se eu parar aqui, [p=0.2] eu só *citei.* [p=0.4] {e}E o cliente pergunta: [p=0.2] *e daí?*"),
    dict(id="10", block="escada", text=
        "{a}Então eu subo. [p=0.2] Isso ainda acontece no Brasil de *hoje?* [p=0.3] {b}Acontece: [p=0.2] quem sofre "
        "psiquicamente ainda é *afastado,* [p=0.2] e não cuidado. [p=0.4] {c}Esse é o segundo degrau: [p=0.2] a "
        "*atualização da referência,* [p=0.2] ou seja, [p=0.2] trazer a obra para o presente."),
    dict(id="11", block="escada", text=
        "{a}Falta o último. [p=0.2] O que isso prova para a minha tese? [p=0.4] {b}Que o *medo do julgamento* [p=0.2] "
        "adia a busca por tratamento. [p=0.4] {c}Terceiro degrau: [p=0.2] agora sim, [p=0.2] eu *argumentei.* [p=0.4] "
        "{d}Parar no primeiro degrau é *citar.* [p=0.2] Chegar ao terceiro é *argumentar.*"),

    # ================= BLOCO C: AS QUATRO PERGUNTAS =================
    dict(id="12", block="perguntas", text=
        "{t}E se você travar no meio da escada? [p=0.4] {a}Faça à referência *quatro perguntas.* [p=0.4] {b}Primeira: "
        "[p=0.2] *por que* isso acontece? [p=0.2] Ela produz a *causa* do problema, [p=0.2] a origem dele. [p=0.4] "
        "{c}Segunda: [p=0.2] isso ainda vale no Brasil de hoje? [p=0.2] Como? [p=0.3] Ela produz a *atualização* da "
        "referência."),
    dict(id="13", block="perguntas", text=
        "{d}Terceira: [p=0.2] *quem* é afetado, [p=0.2] e de que forma? [p=0.3] Ela produz a *consequência* concreta: "
        "[p=0.2] o efeito na vida real das pessoas. [p=0.4] {e}Quarta: [p=0.2] o que isso *prova* sobre a tese? [p=0.3] "
        "Ela produz a ligação com o seu ponto de vista. [p=0.4] {f}As respostas são a matéria-prima da sua análise."),

    # ================= BLOCO D: O SINAL DE QUE FALTA ANÁLISE =================
    dict(id="14", block="sinal", text=
        "{t}E como saber se falta análise no *seu* parágrafo? [p=0.4] {a}Olhe a frase que vem logo depois do repertório. "
        "[p=0.3] {b}Se ela já é o fechamento, [p=0.2] tipo: [p=0.2] dessa forma, [p=0.2] o problema é grave, [p=0.3] "
        "{c}faltou o *meio do caminho.* [p=0.4] {d}A saída: [p=0.2] pergunte *e daí?* à referência [p=0.2] {e}e escreva "
        "a resposta *antes* de fechar."),

    # ================= BLOCO E: O FECHAMENTO =================
    dict(id="15", block="fechamento", text=
        "{t}E a última frase do parágrafo, [p=0.2] o que ela precisa fazer? [p=0.4] {a}O *fechamento* é a última frase. "
        "[p=0.2] Ela amarra o que foi desenvolvido ao ponto de vista do texto, [p=0.2] a tese. [p=0.4] {b}É a assinatura "
        "do recibo. [p=0.4] {c}Muitos cursos chamam essa frase de *mini-conclusão.* [p=0.3] {d}Mas atenção: [p=0.2] "
        "mini-conclusão é nome de *método,* [p=0.2] não é termo oficial."),
    dict(id="16", block="fechamento", text=
        "{t}Veja um fechamento bom, [p=0.2] do eixo da desinformação. [p=0.3] {a}Dessa forma, [p=0.2] enquanto a "
        "informação não substituir o preconceito, [p=0.2] o estigma continuará a afastar os brasileiros do tratamento. "
        "[p=0.5] {b}Ele *retoma o eixo:* [p=0.2] a falta de informação. [p=0.3] {c}E o *liga à tese:* [p=0.2] o estigma "
        "que afasta do tratamento. [p=0.4] {d}Recibo assinado."),
    dict(id="17", block="fechamento", text=
        "{t}Agora, [p=0.2] três fechamentos ruins. [p=0.3] {a}Assim, [p=0.2] isso é um problema muito grave. [p=0.3] É "
        "*vago:* [p=0.2] isso e grave não dizem nada sobre a tese. [p=0.4] {b}Além disso, [p=0.2] a falta de psicólogos "
        "nas escolas também é um problema. [p=0.3] Esse *abre assunto novo* [p=0.2] no lugar de fechar. [p=0.4] {c}Será "
        "que um dia isso vai mudar? [p=0.3] Essa é uma *pergunta retórica:* [p=0.2] uma pergunta feita sem esperar "
        "resposta. [p=0.2] Ela não amarra o argumento."),

    # ================= BLOCO F: OS CONECTIVOS DE FECHAMENTO =================
    dict(id="18", block="conectivos", text=
        "{t}E que palavra abre o fechamento? [p=0.4] {a}Um *conectivo conclusivo.* [p=0.2] Conectivo é a palavra que "
        "liga as ideias; [p=0.2] o conclusivo avisa que o raciocínio chegou ao fim. [p=0.4] {b}Dessa forma, [p=0.2] "
        "assim, [p=0.2] desse modo, [p=0.2] logo, [p=0.2] por conseguinte. [p=0.4] {c}Só um cuidado: [p=0.2] evite usar "
        "no fim de cada parágrafo [p=0.2] o *portanto* que vai abrir a conclusão. [p=0.4] {d}Assim, você não repete a "
        "marca, [p=0.2] e a conclusão continua soando como *conclusão.*"),

    # ================= RECAPITULAÇÃO DO MEIO =================
    dict(id="19", block="recap", text=
        "{t}Três frases para guardar. [p=0.3] {a}Citar é o primeiro degrau; [p=0.2] argumentar é o terceiro. [p=0.6] "
        "{b}Pergunte *e daí?* antes de fechar. [p=0.6] {c}Fechamento retoma o eixo e liga à tese, [p=0.2] sem informação "
        "nova. [p=0.5]"),

    # ================= NÓS FAZEMOS =================
    dict(id="20", block="exercicio", text=
        "{t}Sua vez. [p=0.2] Este parágrafo foi elaborado para fins didáticos. [p=0.3] {a}Em primeiro lugar, [p=0.2] a "
        "desinformação sustenta o estigma. [p=0.3] {b}Machado de Assis escreveu O Alienista, [p=0.2] obra muito "
        "importante da literatura brasileira. [p=0.3] {c}Dessa forma, [p=0.2] o estigma das doenças mentais continua no "
        "Brasil. [p=0.5] {d}A obra foi só *mencionada.* [p=0.2] E daí? [p=0.4] {e}Pause o vídeo [p=0.2] e escreva, "
        "[p=0.2] com as quatro perguntas, [p=0.2] uma frase de análise [p=0.2] entre a referência e o fechamento. [p=0.3] "
        "{p}Pause agora. [p=2.0]"),
    dict(id="21", block="exercicio", text=
        "{a}Agora compare com a frase quatro do parágrafo-modelo, [p=0.2] onde a mesma obra aparece resumida. [p=0.4] "
        "{s}Mais de um século depois, [p=0.2] os critérios mudaram, [p=0.2] mas a lógica persiste: [p=0.2] quem sofre "
        "psiquicamente ainda é visto como alguém a ser afastado, [p=0.2] e não cuidado, [p=0.2] o que leva muitos a "
        "adiar a busca por ajuda por medo do julgamento. [p=0.5] {b}Repare: [p=0.2] *mais de um século depois* atualiza "
        "a referência. [p=0.4] {c}E *adiar a busca por ajuda* [p=0.2] é a consequência concreta. [p=0.4] {d}Se a sua "
        "frase fez isso, [p=0.2] você subiu a escada."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erros", text=
        "{a}Erro um: [p=0.2] pular da referência direto para o fechamento. [p=0.4] {b}Parece certo, [p=0.2] porque uma "
        "obra famosa parece provar tudo sozinha. [p=0.4] {c}Mas a referência não fala sozinha: [p=0.2] pergunte *e daí?* "
        "[p=0.2] e escreva a análise. [p=0.2] É nela que aparece a autoria."),
    dict(id="23", block="erros", text=
        "{a}Erro dois: [p=0.2] fechar com *isso é muito grave.* [p=0.4] {b}Parece certo, [p=0.2] porque tem conectivo e "
        "soa como conclusão. [p=0.4] {c}Mas isso é muito grave não amarra nada: [p=0.2] ligue o *eixo* à *tese.*"),
    dict(id="24", block="erros", text=
        "{a}Erro três: [p=0.2] abrir um assunto novo na última frase. [p=0.4] {b}Parece certo, [p=0.2] porque parece que "
        "você está acrescentando mais um argumento. [p=0.4] {c}Mas o assunto novo fica sem desenvolvimento. [p=0.2] O "
        "fechamento não traz *informação nova.*"),

    # ================= QUESTÃO 2 =================
    dict(id="25", block="q2", text=
        "{t}Agora, [p=0.2] uma questão no estilo do ENEM. [p=0.3] {a}Leia o parágrafo, [p=0.2] escrito para o tema do "
        "ENEM de dois mil e dezenove: [p=0.2] Democratização do acesso ao cinema no Brasil. [p=0.4] {s1}Em primeiro "
        "lugar, [p=0.2] a concentração das salas de exibição limita o acesso ao cinema. [p=0.3] {s2}Segundo o filme "
        "Cinema Paradiso, [p=0.2] de Giuseppe Tornatore, [p=0.2] a sala de cinema pode ser o centro da vida cultural de "
        "uma pequena cidade. [p=0.3] {s3}Dessa forma, [p=0.2] a concentração das salas é um problema."),
    dict(id="26", block="q2", text=
        "{b}Considerando o modelo de parágrafo estudado, [p=0.2] o que mais falta a esse trecho é: [p=0.4] {A}A: [p=0.2] "
        "um tópico frasal, [p=0.2] pois o parágrafo não indica seu argumento. [p=0.4] {B}B: [p=0.2] a análise, [p=0.2] "
        "que relacionaria a referência à realidade brasileira, [p=0.2] cidades do interior sem salas, [p=0.2] e "
        "mostraria por que isso sustenta a tese. [p=0.4] {C}C: [p=0.2] um fechamento, [p=0.2] pois o parágrafo termina "
        "sem retomar a ideia."),
    dict(id="27", block="q2", text=
        "{D}D: [p=0.2] um repertório, [p=0.2] pois filmes não são aceitos como repertório. [p=0.4] {E}E: [p=0.2] uma "
        "proposta de intervenção completa, [p=0.2] obrigatória em cada parágrafo. [p=0.4] {p}Pause o vídeo e tente! "
        "[p=2.0]"),
    dict(id="28", block="q2", text=
        "{ok}Letra *B!* [p=0.3] O parágrafo tem tópico frasal, [p=0.2] repertório e fechamento, [p=0.2] mas salta da "
        "referência direto para a conclusão. [p=0.3] Falta a análise: [p=0.2] explicar o que o filme mostra [p=0.2] e como "
        "isso se aplica ao Brasil, [p=0.2] onde muitas cidades não têm sala. [p=0.2] É isso que tornaria o repertório "
        "produtivo. [p=0.4] {xa}A A [p=0.2] {xc}e a C ignoram que o "
        "tópico frasal e o fechamento existem. [p=0.2] O fechamento é fraco, [p=0.2] mas existe. [p=0.4] {xd}A D "
        "contraria a Cartilha, [p=0.2] que aceita filmes como repertório. [p=0.4] {xe}E a E inventa uma exigência: "
        "[p=0.2] a proposta é avaliada no texto como um todo, [p=0.2] e não por parágrafo."),
    dict(id="29", block="q2", text=
        "{a}Então, [p=0.2] como seria essa análise? [p=0.3] Aqui vai *uma* possibilidade, [p=0.2] elaborada para fins "
        "didáticos. [p=0.4] {b}No Brasil, [p=0.2] porém, [p=0.2] muitas cidades do interior não têm sala de cinema. "
        "[p=0.3] {c}Sem ela, [p=0.2] seus moradores ficam sem esse centro de vida cultural, [p=0.2] e o acesso ao cinema "
        "fica longe de ser democrático. [p=0.4] {d}Filme, [p=0.2] Brasil de hoje, [p=0.2] tese: [p=0.2] os três "
        "degraus."),

    # ================= QUESTÃO 5 =================
    dict(id="30", block="q5", text=
        "{t}Mais uma. [p=0.3] {a}Um parágrafo de desenvolvimento discutiu como a ausência de creches públicas [p=0.2] "
        "sobrecarrega as mulheres com o cuidado dos filhos, [p=0.2] tema do ENEM de dois mil e vinte e três. [p=0.4] "
        "{b}A frase que melhor fecha esse parágrafo é: [p=0.4] {A}A: [p=0.2] Além disso, [p=0.2] a violência urbana "
        "também afeta as mulheres brasileiras. [p=0.4] {B}B: [p=0.2] Será que um dia essa realidade vai mudar? [p=0.4] "
        "{C}C: [p=0.2] Desse modo, [p=0.2] sem uma rede pública que divida o cuidado, [p=0.2] esse trabalho continua "
        "recaindo sobre as mulheres [p=0.2] e permanece invisível."),
    dict(id="31", block="q5", text=
        "{D}D: [p=0.2] Assim, [p=0.2] isso é algo muito triste e preocupante. [p=0.4] {E}E: [p=0.2] Em primeiro lugar, "
        "[p=0.2] as creches são instituições de ensino. [p=0.4] {p}Pause o vídeo e tente! [p=2.0]"),
    dict(id="32", block="q5", text=
        "{ok}Letra *C!* [p=0.3] Ela usa conectivo conclusivo, [p=0.2] retoma o eixo, [p=0.2] a falta de rede pública de "
        "cuidado, [p=0.2] e o liga à tese: [p=0.2] o trabalho de cuidado da mulher permanece invisível. [p=0.2] Sem "
        "informação nova. [p=0.4] {xa}A A abre um assunto novo, [p=0.2] fora do eixo. [p=0.3] {xb}A B é pergunta "
        "retórica [p=0.2] e não amarra o argumento. [p=0.3] {xd}A D é vaga: [p=0.2] isso e triste não dizem nada sobre a "
        "tese. [p=0.3] {xe}E a E reinicia o parágrafo [p=0.2] com um conectivo de abertura e uma definição óbvia."),

    # ================= RECAPITULAÇÃO FINAL E PONTE =================
    dict(id="33", block="recap", text=
        "{t}Para fechar, [p=0.2] as mesmas três frases. [p=0.3] {a}Citar é o primeiro degrau; [p=0.2] argumentar é o "
        "terceiro. [p=0.6] {b}Pergunte *e daí?* antes de fechar. [p=0.6] {c}Fechamento retoma o eixo e liga à tese, "
        "[p=0.2] sem informação nova. [p=0.5]"),
    dict(id="34", block="ponte", text=
        "{a}Agora você já tem as *cinco peças.* [p=0.4] {b}No próximo episódio, [p=0.2] um parágrafo completo comentado "
        "*frase por frase* [p=0.3] {c}e o mesmo parágrafo em *três versões,* [p=0.2] da pior à melhor."),

    # ================= CTA =================
    dict(id="35", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] em qual degrau da escada a sua análise costuma parar? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
