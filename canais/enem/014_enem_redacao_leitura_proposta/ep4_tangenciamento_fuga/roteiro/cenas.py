# Roteiro — Redação ENEM, Leitura da Proposta, Episódio 4 de 6: Abordagem completa, tangenciamento e fuga ao tema (aula para iniciantes)
# Base: Estudos/Enem/estudos/06-redacao/01-leitura-da-proposta.html — seção 08 + Questões 2 e 6 da seção 12.
#   Competência 2 e "Situações que zeram" só no necessário (terão séries próprias).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora da série (encomenda):
#   abordagem completa = entrega no endereço exato · tangenciamento = bairro certo, sem rua e número: chegou perto, não chegou
#   · fuga ao tema = entrega em outra cidade.
# Lidos EXATAMENTE como no material: definições e consequências da tabela (cenas 07, 09, 11), teses 1–3 (14–17),
#   comentário da Cartilha sobre a tese 1 (15), "tangenciar é silencioso" (18–19), Q2 e Q6 (enunciados e alternativas).
# GANCHO: o pedido falava em "até 360 pontos"; pela regra do material (C2, C3 e C5 limitadas a 40, cada uma vale até 200),
#   a perda máxima é 3 × (200 − 40) = 480. Usamos 480 e mostramos a conta.
# Teses do exercício (cenas 21–22): INÉDITAS, marcadas na tela "elaboradas para fins didáticos".
# "Etarismo": definido com uma frase simples (palavra que aparece na tese 3 do material).
# Frases-chave (meio e fim, idênticas):
#   1. Endereço exato: completa. Bairro certo, casa errada: tangencia. Outra cidade: fuga.
#   2. Tangenciar limita C2, C3 e C5 a 40; fugir zera.
#   3. Confira o tema na tese, antes de desenvolver.
# Cores: azul = definição · verde = abordagem completa/método · amarelo = tangenciamento/armadilha · vermelho = fuga/erro
#   · roxo = regra oficial.

TITULO = "Tangenciar o Tema Custa Até 480 Pontos (e Quase Ninguém Percebe) | Proposta de Redação Ep. 4"
# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo da folha em branco: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa e suspense nas armadilhas; comemore os acertos com entusiasmo; dê ênfase "
            "forte às palavras-chave. Quando comparar as teses com o tema, soe como quem está raciocinando de verdade. "
            "Ritmo didático e tranquilo, sem pressa, respeitando as pausas entre as frases. Leia apenas o texto, "
            "exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Quem *foge* ao tema [p=0.2] geralmente percebe. [p=0.5] {b}Quem *tangencia* [p=0.2] quase nunca percebe, "
        "[p=0.3] {c}e pode perder até *quatrocentos e oitenta pontos* [p=0.2] sem saber por quê. [p=0.5] "
        "{d}Três partes da nota presas em quarenta, [p=0.2] em vez de duzentos: [p=0.3] {e}cento e sessenta a menos em cada uma. "
        "[p=0.3] {f}Três vezes cento e sessenta: [p=0.2] *quatrocentos e oitenta.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai saber a diferença entre *as três situações,* [p=0.4] {b}o que cada uma "
        "*custa,* [p=0.4] {c}e como se *proteger* antes de escrever."),
    dict(id="03", block="prereq", text=
        "{t}Lembrando, em trinta segundos. [p=0.3] {a}O *assunto* é a cidade: [p=0.2] o campo geral. [p=0.3] {b}O *tema* é o "
        "endereço exato, [p=0.2] o recorte que a prova dá. [p=0.4] {c}E o tema vem na *frase temática,* [p=0.2] que a gente "
        "desmonta em blocos: [p=0.2] {d}cada bloco, [p=0.2] uma exigência."),

    # ================= AS TRÊS ENTREGAS (CONCRETO) =================
    dict(id="04", block="entregas", text=
        "{t}Agora imagine três entregadores, [p=0.2] com a mesma encomenda. [p=0.4] {a}O primeiro para *na porta certa:* "
        "[p=0.2] rua, número, bairro. [p=0.2] Entregue! [p=0.5] {b}O segundo chega ao *bairro certo,* [p=0.2] mas sem rua e "
        "sem número. [p=0.3] Chegou perto... [p=0.3] não chegou. [p=0.5] {c}E o terceiro? [p=0.3] Foi parar em *outra cidade.*"),
    dict(id="05", block="entregas", text=
        "{t}Na redação, [p=0.2] acontece igualzinho. [p=0.4] {a}E cada entrega tem um nome oficial: [p=0.3] "
        "{b}*abordagem completa,* [p=0.3] {c}*tangenciamento* [p=0.3] {d}e *fuga ao tema.*"),

    # ================= COMPETÊNCIAS (O PLACAR) =================
    dict(id="06", block="placar0", text=
        "{t}Mas antes, [p=0.2] como a nota é dada? [p=0.4] {a}A nota da redação é dividida em cinco partes, [p=0.2] chamadas "
        "*competências.* [p=0.4] {b}Cada uma vale até *duzentos* pontos. [p=0.3] {c}Cinco vezes duzentos: [p=0.2] *mil.* "
        "[p=0.4] {d}Guarde este placar: [p=0.2] ele vai mudar em cada entrega."),

    # ================= BLOCO A: ABORDAGEM COMPLETA =================
    dict(id="07", block="completa", text=
        "{t}Então, [p=0.2] o que é entregar no endereço exato? [p=0.4] {a}É a *abordagem completa:* [p=0.3] {b}o texto "
        "discute o recorte da frase temática. [p=0.4] {c}A consequência? [p=0.2] *Avaliação normal* nas cinco competências. "
        "[p=0.3] {d}Nenhum teto. [p=0.2] Cada parte pode chegar a duzentos."),

    # ================= BLOCO B: TANGENCIAMENTO =================
    dict(id="08", block="tangencia", text=
        "{t}E quando o texto chega perto, [p=0.2] mas não chega? [p=0.4] {a}Isso é *tangenciar.* [p=0.3] {b}Pense numa reta "
        "que só *encosta* no círculo, [p=0.2] e segue em frente."),
    dict(id="09", block="tangencia", text=
        "{t}A Cartilha define assim: [p=0.3] {a}abordagem *parcial,* [p=0.2] baseada somente no *assunto mais amplo* [p=0.2] "
        "a que o tema está vinculado. [p=0.4] {b}Assunto amplo é a cidade inteira: [p=0.2] o campo geral, [p=0.2] sem o recorte. "
        "[p=0.3] {c}É o bairro certo, [p=0.2] sem rua e sem número."),
    dict(id="10", block="tangencia", text=
        "{t}E quanto custa? [p=0.4] {a}As competências *dois, três e cinco* [p=0.2] não passam de *quarenta* pontos. [p=0.4] "
        "{b}Repare: [p=0.2] elas batem no teto. [p=0.4] {c}Já a um e a quatro [p=0.2] *não são limitadas* por essa regra: "
        "[p=0.2] continuam sendo avaliadas normalmente."),

    # ================= BLOCO C: FUGA AO TEMA =================
    dict(id="11", block="fuga", text=
        "{t}E a cidade errada? [p=0.4] {a}É a *fuga ao tema:* [p=0.3] {b}nem o tema específico, [p=0.2] nem o assunto mais "
        "geral são abordados. [p=0.4] {c}A consequência: [p=0.2] *nota zero.* [p=0.3] {d}Ou seja, [p=0.2] a redação inteira "
        "vale zero: [p=0.2] o texto não é avaliado em *nenhuma* competência."),

    # ================= BLOCO D: EU FAÇO (TEMA 2025) =================
    dict(id="12", block="eufaco", text=
        "{t}Agora, [p=0.2] vou fazer na sua frente. [p=0.4] {a}Tema do ENEM de dois mil e vinte e cinco: [p=0.3] "
        "*Perspectivas acerca do envelhecimento na sociedade brasileira.* [p=0.5] {b}Os blocos: [p=0.2] perspectivas, "
        "[p=0.2] envelhecimento, [p=0.2] sociedade brasileira. [p=0.4] {c}Vou testar três teses [p=0.2] contra esses blocos."),
    dict(id="13", block="eufaco", text=
        "{t}Tese um. [p=0.3] {a}O envelhecimento é um processo biológico universal, [p=0.2] marcado pela perda gradual de "
        "funções das células. [p=0.5] {b}Fala de envelhecimento? [p=0.2] Fala. [p=0.3] {c}De como a velhice é *vista?* "
        "[p=0.3] Não. [p=0.3] {d}Do *Brasil?* [p=0.3] Também não."),
    dict(id="14", block="eufaco", text=
        "{a}Ficou no assunto amplo. [p=0.3] {b}E a própria Cartilha cita justamente o envelhecimento tratado só como "
        "processo biológico universal [p=0.2] como *exemplo de tangenciamento.* [p=0.4] {c}Bairro certo, [p=0.2] sem número."),
    dict(id="15", block="eufaco", text=
        "{t}Tese dois. [p=0.3] {a}O uso excessivo de celulares [p=0.2] prejudica a concentração dos estudantes. [p=0.5] "
        "{b}Envelhecimento? [p=0.3] Nenhuma palavra. [p=0.3] {c}É *outro assunto.* [p=0.3] {d}Um texto inteiro desenvolvido "
        "a partir dela [p=0.2] *fugiria ao tema.* [p=0.3] Outra cidade."),
    dict(id="16", block="eufaco", text=
        "{t}Tese três. [p=0.3] {a}No Brasil, [p=0.2] a velhice ainda é vista sobretudo como perda, [p=0.2] visão que alimenta "
        "o etarismo [p=0.2] e atrasa a adaptação das cidades e dos serviços [p=0.2] a uma população que envelhece. [p=0.5] "
        "{b}*Etarismo* é o preconceito contra as pessoas [p=0.2] por causa da idade."),
    dict(id="17", block="eufaco", text=
        "{t}Vamos conferir os blocos. [p=0.3] {a}Perspectivas: [p=0.2] como a velhice é vista. [p=0.2] Tem! [p=0.3] "
        "{b}Envelhecimento: [p=0.2] tem! [p=0.3] {c}Sociedade brasileira: [p=0.2] tem! [p=0.4] {d}E ainda anuncia *dois eixos* "
        "para o desenvolvimento, [p=0.2] dois caminhos que o texto vai seguir: [p=0.2] o etarismo [p=0.2] e a adaptação das "
        "cidades e dos serviços. [p=0.4] {e}Endereço exato!"),

    # ================= BLOCO E: TANGENCIAR É SILENCIOSO =================
    dict(id="18", block="silencio", text=
        "{t}E por que tangenciar é tão perigoso? [p=0.4] {a}Porque é *silencioso.* [p=0.3] {b}Quem foge ao tema geralmente "
        "percebe; [p=0.3] quem tangencia, [p=0.2] quase nunca."),
    dict(id="19", block="silencio", text=
        "{a}O texto pode ter boa norma, [p=0.2] {b}bons conectivos, [p=0.2] {c}e um repertório interessante. [p=0.4] "
        "{d}Só que sobre o *assunto,* [p=0.3] e não sobre o *recorte.* [p=0.4] {e}Uma caixa linda, [p=0.2] bem embalada, "
        "[p=0.2] no endereço errado."),

    # ================= BLOCO F: QUANDO CONFERIR =================
    dict(id="20", block="conferir", text=
        "{t}Então, [p=0.2] quando conferir? [p=0.4] {a}Primeiro, [p=0.2] *na tese,* [p=0.2] antes do desenvolvimento. "
        "[p=0.4] {b}E de novo [p=0.2] *no fim do rascunho.* [p=0.4] {c}Duas paradas para olhar a etiqueta [p=0.2] antes de "
        "entregar."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="21", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] endereço exato: completa. [p=0.2] Bairro certo, casa errada: "
        "tangencia. [p=0.2] Outra cidade: fuga. [p=0.5] {b}Dois: [p=0.2] tangenciar limita C dois, C três e C cinco a "
        "quarenta; [p=0.2] fugir zera. [p=0.5] {c}Três: [p=0.2] confira o tema na tese, [p=0.2] antes de desenvolver."),

    # ================= NÓS FAZEMOS =================
    dict(id="22", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Tema de dois mil e dezenove: [p=0.3] *Democratização do acesso ao cinema no Brasil.* [p=0.4] "
        "{b}Três teses. [p=0.3] {t1}Um: [p=0.2] o cinema é uma arte capaz de emocionar [p=0.2] e de registrar a cultura de um "
        "povo. [p=0.4] {t2}Dois: [p=0.2] no Brasil, [p=0.2] ir ao cinema ainda é privilégio de poucos, [p=0.2] e democratizar "
        "esse acesso exige levar exibições a bairros e cidades que não têm salas. [p=0.4] {t3}Três: [p=0.2] as redes sociais "
        "mudaram a forma como os jovens se informam. [p=0.5] {p}Pause o vídeo [p=0.2] e classifique cada uma. [p=2.0]"),
    dict(id="23", block="exercicio", text=
        "{t}Conferindo. [p=0.3] {r1}A um fala de cinema, [p=0.2] mas sem acesso e sem Brasil: [p=0.2] *tangencia.* [p=0.4] "
        "{r2}A dois cobre democratização, [p=0.2] acesso, [p=0.2] cinema [p=0.2] e Brasil: [p=0.2] *completa.* [p=0.4] "
        "{r3}A três nem fala de cinema: [p=0.2] *fuga.*"),

    # ================= ERROS CLÁSSICOS =================
    dict(id="24", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que tangenciar *zera* a redação. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque as duas coisas são chamadas de erro de tema. [p=0.4] {c}Mas quem zera é a *fuga.* "
        "[p=0.2] O tangenciamento limita três competências."),
    dict(id="25", block="erros", text=
        "{a}Segundo: [p=0.2] achar que o tangenciamento limita *as cinco* competências. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque o texto inteiro errou o recorte. [p=0.4] {c}Mas o teto de quarenta vale só para a *dois,* a *três* e a "
        "*cinco.* [p=0.2] A um e a quatro não são limitadas por essa regra."),
    dict(id="26", block="erros", text=
        "{a}Terceiro: [p=0.2] chamar de fuga um texto que fala do assunto, [p=0.2] mas fora do recorte de *lugar.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque falar de outro país [p=0.2] parece fugir do Brasil. [p=0.4] {c}Mas ele está na "
        "cidade certa: [p=0.2] é *tangenciamento.*"),

    # ================= QUESTÃO 2 =================
    dict(id="27", block="q2", text=
        "{t}Agora, questões no estilo do ENEM. [p=0.4] {a}Para o tema do ENEM de dois mil e vinte e cinco, [p=0.2] "
        "Perspectivas acerca do envelhecimento na sociedade brasileira, [p=0.3] um participante dedicou todos os parágrafos "
        "[p=0.2] a mostrar como o *Japão* se adaptou ao envelhecimento da população, [p=0.3] sem relacionar essa experiência "
        "à realidade brasileira. [p=0.4] {b}Segundo a Cartilha do Participante, [p=0.2] essa redação:"),
    dict(id="28", block="q2", text=
        "{a}A: [p=0.2] fugiu ao tema e recebe nota zero, [p=0.2] pois tratou de outro país. [p=0.5] {b}B: [p=0.2] abordou o "
        "tema de forma completa, [p=0.2] pois o envelhecimento é o núcleo da frase temática. [p=0.5] {c}C: [p=0.2] tangenciou "
        "o tema [p=0.2] e fica limitada a quarenta pontos nas cinco competências. [p=0.5] {d}D: [p=0.2] tangenciou o tema, "
        "[p=0.2] pois tratou o envelhecimento só fora do contexto brasileiro; [p=0.2] C dois, C três e C cinco não passam de "
        "quarenta pontos. [p=0.5] {e}E: [p=0.2] será penalizada apenas na Competência um, [p=0.2] por não usar exemplos "
        "nacionais. [p=0.5] {p}*Pause o vídeo e tente!* [p=2.0]"),
    dict(id="29", block="q2", text=
        "{t}Vamos à entrega. [p=0.3] {a}O texto chegou à cidade certa: [p=0.2] envelhecimento. [p=0.3] {b}Mas esqueceu um "
        "bloco: [p=0.2] *sociedade brasileira.* [p=0.4] {c}A Cartilha de dois mil e vinte e seis cita como exemplo de "
        "tangenciamento, [p=0.2] no tema de dois mil e vinte e cinco, [p=0.2] tratar o envelhecimento só fora do contexto "
        "brasileiro."),
    dict(id="30", block="q2", text=
        "{xa}A A confunde com fuga: [p=0.2] o texto trata do assunto. [p=0.4] {xb}A B ignora o recorte de lugar. [p=0.4] "
        "{xc}A C estende o limite à um e à quatro, [p=0.2] que não são limitadas por essa regra. [p=0.4] {xe}E a E erra a "
        "competência: [p=0.2] a abordagem do tema é avaliada na dois. [p=0.5] {ok}*Letra D!*"),

    # ================= QUESTÃO 6 =================
    dict(id="31", block="q6", text=
        "{t}Próxima. [p=0.3] {a}Para o tema do ENEM de dois mil e dezenove, [p=0.2] Democratização do acesso ao cinema no "
        "Brasil, [p=0.2] considere três redações. [p=0.4] {i}Um: [p=0.2] discute apenas a história do cinema mundial e as "
        "escolas cinematográficas, [p=0.2] sem tratar de acesso. [p=0.4] {ii}Dois: [p=0.2] discute a importância da leitura "
        "de livros na formação dos jovens, [p=0.2] sem mencionar cinema. [p=0.4] {iii}Três: [p=0.2] discute a concentração "
        "das salas de exibição nas capitais [p=0.2] e o preço dos ingressos como barreiras de acesso no país. [p=0.4] "
        "{b}Segundo a Cartilha do Participante, [p=0.2] essas redações configuram, respectivamente:"),
    dict(id="32", block="q6", text=
        "{a}A: [p=0.2] tangenciamento, [p=0.2] fuga ao tema [p=0.2] e abordagem completa. [p=0.5] {b}B: [p=0.2] fuga ao "
        "tema, [p=0.2] tangenciamento [p=0.2] e abordagem completa. [p=0.5] {c}C: [p=0.2] abordagem completa, [p=0.2] fuga "
        "ao tema [p=0.2] e tangenciamento. [p=0.5] {d}D: [p=0.2] tangenciamento, [p=0.2] tangenciamento [p=0.2] e abordagem "
        "completa. [p=0.5] {e}E: [p=0.2] fuga ao tema, [p=0.2] fuga ao tema [p=0.2] e tangenciamento. [p=0.5] "
        "{p}*Pause o vídeo e tente!* [p=2.0]"),
    dict(id="33", block="q6", text=
        "{t}Três redações, [p=0.2] três destinos. [p=0.4] {r1}A um trata do assunto amplo, [p=0.2] cinema, [p=0.2] sem o "
        "recorte: [p=0.2] bairro certo, sem número. [p=0.2] *Tangencia.* [p=0.4] {r2}A dois não aborda nem o tema nem o "
        "assunto: [p=0.2] outra cidade. [p=0.2] *Fuga.* [p=0.4] {r3}A três discute o recorte: [p=0.2] endereço exato. "
        "[p=0.2] *Completa.*"),
    dict(id="34", block="q6", text=
        "{xb}A B inverte a um e a dois. [p=0.4] {xc}A C considera completa uma redação que ignora o acesso. [p=0.4] "
        "{xd}A D não percebe que a dois abandona até o assunto. [p=0.4] {xe}E a E trata a um como fuga, [p=0.2] embora ela "
        "fale de cinema. [p=0.5] {ok}*Letra A!*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="35", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] endereço exato: completa. [p=0.2] Bairro certo, casa "
        "errada: tangencia. [p=0.2] Outra cidade: fuga. [p=0.5] {b}Dois: [p=0.2] tangenciar limita C dois, C três e C cinco "
        "a quarenta; [p=0.2] fugir zera. [p=0.5] {c}Três: [p=0.2] confira o tema na tese, [p=0.2] antes de desenvolver."),

    # ================= PONTE E CTA =================
    dict(id="36", block="ponte", text=
        "{a}Agora você tem *todas as ferramentas.* [p=0.4] {b}No próximo episódio, [p=0.2] eu faço a leitura completa de "
        "uma proposta real, [p=0.2] do zero até a tese, [p=0.2] na sua frente, [p=0.2] {c}em *seis passos.*"),
    dict(id="37", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] como você classificou as três teses do cinema? "
        "[p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
