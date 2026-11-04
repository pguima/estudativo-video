# Roteiro — Redação ENEM, Introdução, Episódio 7 de 7: Revisão geral, pegadinhas e desafio prático
# Base: Estudos/Enem/estudos/06-redacao/02-introducao.html — seções 01 (as três ideias que mais rendem), 11 (os 10 erros)
#   e 13 (checklist de domínio + tarefa "Antes de marcar Dominado"). NENHUMA das Questões 1–9 da seção 12.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias da série (relembradas no mapa, cena 03): introdução = etiqueta completa · contextualização = mapa ·
#   quatro caminhos = quatro portas · ponte = rua de acesso · repertório de bolso = cartão-postal genérico ·
#   teste da retirada · tese = o que você entrega no endereço inteiro · antecipação = lista da caixa ·
#   "promessa feita é promessa cobrada" · "arrume a caixa antes de escrever a etiqueta".
# Lidos EXATAMENTE como no material: as três ideias da seção 01 (cena 05), a correção de cada erro da seção 11 (respostas
#   do V ou F), a instrução do checklist e a tarefa do desafio (seção 13).
# V ou F: os 10 erros da seção 11 viram afirmações; 4 são a regra certa (V) e 6 o erro (F), misturados.
# Questões 1–5: INÉDITAS, temas fictícios marcados na tela "Tema elaborado para fins didáticos"; nenhuma lei, dado ou
#   autor inventado (a única referência é o Estatuto da Pessoa Idosa, com o texto da seção 12 do material).
#   Gabaritos: 1 C · 2 E · 3 B · 4 A · 5 D.
# Desafio: temas reais de 2020, 2022 e 2025; só o planejamento de 2020 é feito ao vivo, com a tese do episódio 4 (do
#   material) e a definição de estigma da série Leitura da Proposta. A porta histórica/legal fica em branco de propósito:
#   o aluno escolhe uma referência que possa verificar (nada inventado).
# Cores: azul = definição/tema · verde = método · amarelo = armadilha · vermelho = erro/penalidade · roxo = regra oficial.

TITULO = "10 Pegadinhas do 1º Parágrafo da Redação: Você Cai? | Introdução da Redação Ep. 7"
# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo da folha em branco: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Esta é a aula de revisão do primeiro parágrafo, com clima de "
            "desafio e de jogo: faça as perguntas com suspense, revele as respostas com entusiasmo, mostre surpresa nas "
            "pegadinhas e comemore os acertos. Ritmo didático e tranquilo, sem pressa, respeitando as pausas entre as "
            "frases. Leia apenas o texto, exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}O primeiro parágrafo é a *promessa* do seu texto. [p=0.4] {b}Vamos ver se você sabe fazer uma promessa [p=0.2] "
        "que o corretor consegue *cobrar.*"),
    dict(id="02", block="hook", text=
        "{a}Nesta revisão: [p=0.2] {b}as três ideias que mais rendem, [p=0.2] {c}um verdadeiro ou falso com *dez "
        "pegadinhas,* [p=0.2] {d}cinco questões inéditas [p=0.2] {e}e um desafio com três temas reais. [p=0.4] {f}Pegue papel "
        "e caneta."),

    # ================= O MAPA DA SÉRIE =================
    dict(id="03", block="mapa", text=
        "{t}Primeiro, [p=0.2] as imagens da série. [p=0.3] {a}A introdução é a *etiqueta completa* da encomenda. [p=0.4] "
        "{b}A contextualização é o *mapa,* [p=0.2] com *quatro portas* de entrada. [p=0.4] {c}A ponte é a *rua de acesso,* "
        "[p=0.2] {d}e o repertório de bolso é o *cartão-postal genérico,* [p=0.2] que o teste da retirada denuncia. [p=0.4] "
        "{e}A tese é o que você *entrega* no endereço inteiro, [p=0.2] {f}e a antecipação é a *lista da caixa:* [p=0.2] "
        "promessa feita é promessa cobrada. [p=0.4] {g}E na oficina: [p=0.2] arrume a caixa antes de escrever a etiqueta."),

    # ================= AS TRÊS IDEIAS =================
    dict(id="04", block="ideias", text=
        "{t}Agora, [p=0.2] um teste de memória. [p=0.3] {a}Quais são as *três ideias* que mais rendem na introdução? [p=0.3] "
        "{p}Pause e tente lembrar. [p=2.0]"),
    dict(id="05", block="ideias", text=
        "{a}Um: [p=0.2] a contextualização só ajuda se tiver uma *ponte explícita* para o recorte do tema. [p=0.4] {b}Dois: "
        "[p=0.2] a tese é uma *posição,* [p=0.2] não a repetição da frase temática. [p=0.4] {c}Três: [p=0.2] anunciar *dois "
        "eixos* na introdução torna o projeto de texto visível."),

    # ================= VERDADEIRO OU FALSO =================
    dict(id="06", block="vf", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso.* [p=0.3] Dez frases, [p=0.2] dez pausas. [p=0.4] {q}Primeira: [p=0.2] abrir "
        "com desde os primórdios da humanidade é um bom jeito de contextualizar qualquer tema. [p=0.2] {p}Pause. [p=2.0] "
        "{r}*Falso!* [p=0.3] {w}Engana porque soa elegante [p=0.2] e serve para tudo. [p=0.3] {k}Mas desde os primórdios não "
        "informa nada: [p=0.2] contextualize o recorte, [p=0.2] não a humanidade."),
    dict(id="07", block="vf", text=
        "{q}Segunda: [p=0.2] se você tira a referência da introdução e nada muda, [p=0.2] ela não estava trabalhando. [p=0.2] "
        "{p}Pause. [p=2.0] {r}*Verdadeiro!* [p=0.3] {w}Parece exagero, [p=0.2] porque a citação deixa o texto bonito. [p=0.3] "
        "{k}Mas citar e abandonar não serve: [p=0.2] faça a ponte entre a referência e o tema."),
    dict(id="08", block="vf", text=
        "{q}Terceira: [p=0.2] uma frase de pensador decorada serve para abrir qualquer redação. [p=0.2] {p}Pause. [p=2.0] "
        "{r}*Falso!* [p=0.3] {w}Engana porque um nome famoso parece dar peso. [p=0.3] {k}Mas isso é repertório de bolso: "
        "[p=0.2] escolha uma referência ligada ao recorte. [p=0.2] A Cartilha alerta para o uso genérico desde dois mil e "
        "vinte e cinco."),
    dict(id="09", block="vf", text=
        "{q}Quarta: [p=0.2] um número sem fonte, [p=0.2] tipo pesquisas mostram que noventa por cento, [p=0.2] deixa a "
        "introdução mais forte. [p=0.2] {p}Pause. [p=2.0] {r}*Falso!* [p=0.3] {w}Engana porque o número parece preciso. "
        "[p=0.3] {k}Mas use só o que você pode verificar: [p=0.2] repertório precisa ser legitimado."),
    dict(id="10", block="vf", text=
        "{q}Quinta: [p=0.2] é um tema muito importante *não* é tese. [p=0.2] {p}Pause. [p=2.0] {r}*Verdadeiro!* [p=0.3] "
        "{w}Parece tese, [p=0.2] porque a frase usa as palavras da prova. [p=0.3] {k}Mas é um tema importante não é ponto "
        "de vista: [p=0.2] tome posição contestável."),
    dict(id="11", block="vf", text=
        "{q}Sexta: [p=0.2] uma tese que deixa um bloco da frase temática de fora [p=0.2] já compromete o texto na "
        "introdução. [p=0.2] {p}Pause. [p=2.0] {r}*Verdadeiro!* [p=0.3] {w}Parece exagero, [p=0.2] porque falta só um "
        "pedacinho. [p=0.3] {k}Mas o tangenciamento começa na introdução: [p=0.2] confira cada bloco da frase temática."),
    dict(id="12", block="vf", text=
        "{q}Sétima: [p=0.2] anunciar os eixos na introdução é desperdiçar linhas. [p=0.2] {p}Pause. [p=2.0] {r}*Falso!* "
        "[p=0.3] {w}Engana porque os eixos vão aparecer de novo no desenvolvimento. [p=0.3] {k}Mas antecipar os dois "
        "argumentos torna o projeto de texto visível: [p=0.2] é a C três."),
    dict(id="13", block="vf", text=
        "{q}Oitava: [p=0.2] a antecipação deve ser escrita *depois* de planejar os parágrafos de desenvolvimento. [p=0.2] "
        "{p}Pause. [p=2.0] {r}*Verdadeiro!* [p=0.3] {w}Parece estranho, [p=0.2] porque a introdução é o primeiro parágrafo "
        "lido. [p=0.3] {k}Mas promessa sem entrega rompe a coerência: [p=0.2] planeje primeiro, [p=0.2] prometa depois."),
    dict(id="14", block="vf", text=
        "{q}Nona: [p=0.2] quanto mais exemplos e explicações na introdução, [p=0.2] melhor. [p=0.2] {p}Pause. [p=2.0] "
        "{r}*Falso!* [p=0.3] {w}Engana porque parece mostrar que você sabe muito. [p=0.3] {k}Mas introdução longa rouba "
        "linhas dos argumentos: [p=0.2] deixe exemplos e explicações para o desenvolvimento."),
    dict(id="15", block="vf", text=
        "{q}Décima: [p=0.2] a introdução precisa ter exatamente três frases, [p=0.2] senão perde pontos. [p=0.2] {p}Pause. "
        "[p=2.0] {r}*Falso!* [p=0.3] {w}Engana porque o modelo aparece nas redações de nota alta. [p=0.3] {k}Mas é "
        "*método:* [p=0.2] o Inep avalia por competências. [p=0.2] O que conta é proposição, [p=0.2] projeto [p=0.2] e "
        "repertório pertinente."),

    # ================= QUESTÃO 1: QUAL PORTA? =================
    dict(id="16", block="q1", text=
        "{t}Agora, [p=0.2] cinco questões inéditas. [p=0.3] {r}Lembrando: [p=0.2] quatro portas para o mesmo tema: [p=0.2] "
        "lei ou obra, [p=0.2] história, [p=0.2] dado [p=0.2] e conceito. [p=0.4] {a}Questão um. [p=0.2] Tema: [p=0.2] "
        "Desafios para o descarte correto do lixo eletrônico no Brasil. [p=0.3] A introdução começa assim: [p=0.2] {s}chama-se "
        "lixo eletrônico todo aparelho elétrico ou eletrônico descartado, [p=0.2] do celular quebrado à geladeira velha. "
        "[p=0.3] {e}Essa contextualização recorre principalmente a quê?"),
    dict(id="17", block="q1", text=
        "{A}A: [p=0.2] um dado estatístico, [p=0.2] para dimensionar o problema. [p=0.4] {B}B: [p=0.2] um contexto histórico, "
        "[p=0.2] para explicar a origem do problema. [p=0.4] {C}C: [p=0.2] um conceito, [p=0.2] para esclarecer o que está em "
        "jogo. [p=0.4] {D}D: [p=0.2] uma lei, [p=0.2] para mostrar o que está garantido. [p=0.4] {E}E: [p=0.2] uma frase de "
        "pensador, [p=0.2] para dar autoridade. [p=0.4] {p}Pause e tente! [p=2.0]"),
    dict(id="18", block="q1", text=
        "{ok}Letra *C:* [p=0.2] a frase define o que é lixo eletrônico. [p=0.3] É a porta do conceito. [p=0.4] {xa}A A não "
        "serve: [p=0.2] não há número nenhum. [p=0.3] {xb}A B também não: [p=0.2] não há data nem fato do passado. [p=0.3] "
        "{xd}A D e a E descrevem fontes que não aparecem no trecho."),

    # ================= QUESTÃO 2: A PONTE =================
    dict(id="19", block="q2", text=
        "{r}Lembrando: [p=0.2] a ponte é a rua: [p=0.2] leva do mapa até a porta. [p=0.4] {a}Questão dois. [p=0.2] Tema: "
        "[p=0.2] Desafios para garantir a convivência comunitária da pessoa idosa no Brasil. [p=0.3] {s}A introdução começa: "
        "[p=0.2] o Estatuto da Pessoa Idosa assegura às pessoas com sessenta anos ou mais direitos como saúde, dignidade e "
        "convivência comunitária. [p=0.3] {e}Qual frase faz a ponte?"),
    dict(id="20", block="q2", text=
        "{A}A: [p=0.2] nesse sentido, [p=0.2] o Brasil é um país muito grande. [p=0.4] {B}B: [p=0.2] dessa forma, [p=0.2] a "
        "velhice sempre foi estudada pelos filósofos. [p=0.4] {C}C: [p=0.2] por isso, [p=0.2] todos os idosos brasileiros já "
        "convivem plenamente em comunidade. [p=0.4] {D}D: [p=0.2] pesquisas mostram que noventa por cento dos idosos vivem "
        "sozinhos. [p=0.4] {E}E: [p=0.2] na prática, contudo, [p=0.2] muitos idosos brasileiros passam os dias isolados em "
        "casa, [p=0.2] longe da convivência que a lei promete. [p=0.4] {p}Pause e tente! [p=2.0]"),
    dict(id="21", block="q2", text=
        "{ok}Letra *E:* [p=0.2] contrapõe a lei à realidade, [p=0.2] e a tese pode vir em seguida. [p=0.4] {xa}A A traz uma "
        "informação sem relação com o recorte. [p=0.3] {xb}A B é o cartão-postal: [p=0.2] salta para o assunto amplo. "
        "[p=0.3] {xc}A C elimina o problema que você ia discutir. [p=0.3] {xd}E a D é dado sem fonte."),

    # ================= QUESTÃO 3: A TESE =================
    dict(id="22", block="q3", text=
        "{r}Lembrando: [p=0.2] tese é clara, [p=0.2] contestável, [p=0.2] completa [p=0.2] e argumentável. [p=0.4] {a}Questão "
        "três. [p=0.2] Tema: [p=0.2] Desafios para a redução do desperdício de água nas cidades brasileiras. [p=0.3] {e}Qual "
        "frase é uma tese clara, [p=0.2] contestável [p=0.2] e completa?"),
    dict(id="23", block="q3", text=
        "{A}A: [p=0.2] a água é um recurso muito importante para todos. [p=0.4] {B}B: [p=0.2] nas cidades brasileiras, "
        "[p=0.2] o desperdício de água persiste pela falta de manutenção das redes de distribuição [p=0.2] e pela pouca "
        "conscientização sobre o consumo doméstico. [p=0.4] {C}C: [p=0.2] até quando vamos desperdiçar água? [p=0.4] {D}D: "
        "[p=0.2] este texto vai discutir os desafios para a redução do desperdício de água nas cidades brasileiras. [p=0.4] "
        "{E}E: [p=0.2] em todo o mundo, [p=0.2] a água é essencial para a vida. [p=0.4] {p}Pause e tente! [p=2.0]"),
    dict(id="24", block="q3", text=
        "{ok}Letra *B:* [p=0.2] toma posição, [p=0.2] cobre os blocos [p=0.2] e já anuncia dois eixos. [p=0.4] {xa}A A só "
        "declara importância. [p=0.3] {xc}A C é pergunta retórica: [p=0.2] pergunta não é tese. [p=0.3] {xd}A D só anuncia "
        "o tema. [p=0.3] {xe}E a E tangencia: [p=0.2] fica no assunto amplo, [p=0.2] sem desafios, [p=0.2] sem desperdício "
        "[p=0.2] e sem Brasil."),

    # ================= QUESTÃO 4: FORMA DE ANTECIPAR =================
    dict(id="25", block="q4", text=
        "{r}Lembrando: [p=0.2] três formas de colar a lista na caixa: [p=0.2] dois substantivos, [p=0.2] causa e "
        "consequência, [p=0.2] ou dois agentes. [p=0.4] {a}Questão quatro. [p=0.2] Tema: [p=0.2] Desafios para combater o "
        "sedentarismo entre jovens no Brasil. [p=0.3] {s}A tese termina assim: [p=0.2] um problema que envolve tanto a escola "
        "quanto as famílias. [p=0.3] {e}Que forma de antecipar foi usada?"),
    dict(id="26", block="q4", text=
        "{A}A: [p=0.2] dois agentes. [p=0.4] {B}B: [p=0.2] dois substantivos coordenados. [p=0.4] {C}C: [p=0.2] causa e "
        "consequência. [p=0.4] {D}D: [p=0.2] uma pergunta retórica, [p=0.2] que substitui a tese. [p=0.4] {E}E: [p=0.2] "
        "nenhuma: [p=0.2] a frase não antecipa eixos. [p=0.4] {p}Pause e tente! [p=2.0]"),
    dict(id="27", block="q4", text=
        "{ok}Letra *A:* [p=0.2] tanto a escola quanto as famílias. [p=0.2] Cada agente vira um parágrafo. [p=0.4] {xb}A B "
        "seria algo como: [p=0.2] pela falta disso e pela falta daquilo. [p=0.3] {xc}A C precisaria de um encadeamento: "
        "[p=0.2] isso causa aquilo. [p=0.3] {xd}A D não cabe: [p=0.2] não há pergunta. [p=0.3] {xe}E a E erra: [p=0.2] os "
        "dois eixos estão ali."),

    # ================= QUESTÃO 5: PROMESSA NÃO CUMPRIDA =================
    dict(id="28", block="q5", text=
        "{r}Lembrando: [p=0.2] promessa feita é promessa cobrada. [p=0.4] {a}Questão cinco. [p=0.2] Tema: [p=0.2] Caminhos "
        "para ampliar a doação de sangue no Brasil. [p=0.3] {i}O primeiro parágrafo de desenvolvimento vai tratar do medo e "
        "da desinformação sobre a doação; [p=0.3] {ii}o segundo, [p=0.2] da falta de postos de coleta fora dos grandes "
        "centros. [p=0.3] {e}Qual tese promete um eixo que esse desenvolvimento *não* cumpre?"),
    dict(id="29", block="q5", text=
        "{A}A: [p=0.2] ampliar a doação exige vencer a desinformação [p=0.2] e levar postos de coleta para fora dos grandes "
        "centros. [p=0.4] {B}B: [p=0.2] a doação esbarra no medo, [p=0.2] alimentado pela desinformação, [p=0.2] e na "
        "escassez de postos fora das capitais. [p=0.4] {C}C: [p=0.2] o problema envolve tanto a informação da população "
        "quanto a distribuição dos postos de coleta. [p=0.4] {D}D: [p=0.2] a doação esbarra na desinformação [p=0.2] e no "
        "preço dos exames de sangue. [p=0.4] {E}E: [p=0.2] é preciso combater o medo de doar [p=0.2] e espalhar os postos "
        "pelo interior. [p=0.4] {p}Pause e tente! [p=2.0]"),
    dict(id="30", block="q5", text=
        "{ok}Letra *D:* [p=0.2] prometeu o preço dos exames, [p=0.2] e o segundo parágrafo entrega os postos de coleta. "
        "[p=0.3] O leitor percebe a quebra, [p=0.2] e quem sofre é a coerência: [p=0.2] a C três. [p=0.4] {xo}As outras "
        "quatro anunciam exatamente os dois eixos planejados, [p=0.2] com formas diferentes de antecipar."),

    # ================= DESAFIO PRÁTICO =================
    dict(id="31", block="desafio", text=
        "{t}Agora, [p=0.2] o *desafio.* [p=0.3] {a}Três temas reais: [p=0.2] dois mil e vinte, [p=0.2] vinte e dois [p=0.2] "
        "e vinte e cinco. [p=0.4] {b}Para cada um, [p=0.2] escreva *duas* introduções: [p=0.3] {c}uma com contextualização "
        "histórica ou legal [p=0.2] {d}e outra com dado ou conceito, [p=0.3] {e}sempre com ponte, [p=0.2] tese e dois eixos. "
        "[p=0.4] {f}Depois, [p=0.2] aplique o teste da retirada ao repertório [p=0.2] e confira se a tese cobre todos os "
        "blocos."),
    dict(id="32", block="modelo", text=
        "{t}Eu faço o planejamento do primeiro, [p=0.2] como modelo. [p=0.3] {a}Dois mil e vinte: [p=0.2] O estigma associado "
        "às doenças mentais na sociedade brasileira. [p=0.4] {b}Blocos: [p=0.2] o estigma, [p=0.2] associado às doenças "
        "mentais, [p=0.2] na sociedade brasileira. [p=0.4] {c}A tese, [p=0.2] você já conhece do episódio quatro."),
    dict(id="33", block="modelo", text=
        "{a}No Brasil, o estigma associado às doenças mentais persiste em razão da desinformação sobre os transtornos [p=0.2] "
        "e de representações midiáticas que associam o adoecimento psíquico à violência. [p=0.5] {b}Eixo A: [p=0.2] "
        "desinformação. [p=0.3] {c}Eixo B: [p=0.2] mídia. [p=0.3] {d}A caixa está arrumada."),
    dict(id="34", block="modelo", text=
        "{t}Agora, [p=0.2] as duas portas. [p=0.3] {a}Introdução um, [p=0.2] porta do conceito: [p=0.2] estigma é uma marca "
        "negativa que a sociedade cola numa pessoa. [p=0.4] {b}Ponte: [p=0.2] na sociedade brasileira, [p=0.2] essa marca "
        "ainda recai sobre quem tem um transtorno mental. [p=0.4] {c}Introdução dois, [p=0.2] porta histórica ou legal: "
        "[p=0.2] aqui eu deixo em branco de propósito. [p=0.3] {d}Use uma referência que *você* conheça e possa verificar. "
        "[p=0.2] Eu não vou inventar uma para você."),
    dict(id="35", block="modelo", text=
        "{t}Conferência. [p=0.3] {a}Teste da retirada: [p=0.2] se eu apago a definição, [p=0.2] a ponte perde o sentido? "
        "[p=0.3] Perde: [p=0.2] *essa marca* depende dela. [p=0.2] Então ela trabalha. [p=0.4] {b}O estigma? [p=0.2] Tem. "
        "[p=0.3] {c}Doenças mentais? [p=0.2] Tem. [p=0.3] {d}Sociedade brasileira? [p=0.2] Tem. [p=0.4] {e}Agora é com você: "
        "[p=0.2] termine dois mil e vinte, [p=0.2] e faça vinte e dois e vinte e cinco."),

    # ================= CHECKLIST DE DOMÍNIO =================
    dict(id="36", block="dominio", text=
        "{t}Para fechar, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria explicar em voz alta "
        "para outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}O que não marcou, [p=0.2] reveja o episódio "
        "correspondente."),
    dict(id="37", block="dominio", text=
        "{e1}Episódio um: [p=0.2] os três movimentos e a pergunta de cada um, [p=0.2] que é método e não critério oficial, "
        "[p=0.2] e a competência de cada movimento. [p=0.4] {e2}Episódio dois: [p=0.2] as quatro portas [p=0.2] e o risco "
        "típico de cada uma. [p=0.4] {e3}Episódio três: [p=0.2] a frase-ponte [p=0.2] e o teste da retirada."),
    dict(id="38", block="dominio", text=
        "{e4}Episódio quatro: [p=0.2] tese, importância ou repetição do tema; [p=0.2] a tese clara, contestável e completa; "
        "[p=0.2] as três formas de antecipar; [p=0.2] e por que promessa não cumprida afeta a C três. [p=0.4] {e5}Episódio "
        "cinco: [p=0.2] as armadilhas de abertura. [p=0.4] {e6}Episódio seis: [p=0.2] montar uma introdução completa em até "
        "*dez minutos* de rascunho."),

    # ================= PONTE E CTA =================
    dict(id="39", block="ponte", text=
        "{a}A etiqueta está pronta, [p=0.2] e a lista da caixa promete *dois itens.* [p=0.4] {b}O próximo assunto é "
        "*Desenvolvimento:* [p=0.2] tópico frasal, [p=0.2] argumento, [p=0.2] repertório, [p=0.2] análise e fechamento. "
        "[p=0.4] {c}Ele mostra como *entregar* cada item que você prometeu."),
    dict(id="40", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantas das dez você acertou no verdadeiro ou falso? [p=0.5] "
        "{anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no "
        "*Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
