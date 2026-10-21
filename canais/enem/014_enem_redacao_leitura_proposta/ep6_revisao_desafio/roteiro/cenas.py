# Roteiro — Redação ENEM, Leitura da Proposta, Episódio 6 de 6: Revisão geral, pegadinhas e desafio prático
# Base: Estudos/Enem/estudos/06-redacao/01-leitura-da-proposta.html — seções 01, 11 e 13 (+ tabela de temas da seção 03 para o
#   desafio e a leitura de "Caminhos para combater…" da seção 04, já vista no ep. 2). NENHUMA das Questões 1–9 da seção 12.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias da série (relembradas no mapa, cena 04): frase temática = endereço completo · blocos = partes do endereço ·
#   foco = escolher a porta · motivadores = GPS · cópia = linha fantasma · tangenciar = bairro certo, casa errada ·
#   fuga = outra cidade · 6 passos = checklist do piloto.
# Lidos EXATAMENTE como no material: os três hábitos (cena 03), as regras da seção 11 (respostas do V ou F), a tarefa do
#   desafio e a instrução do checklist (seção 13).
# V ou F: os 10 erros da seção 11 viram afirmações; 4 são a regra certa (V) e 6 o erro (F), para o aluno não chutar.
# Questões 1–5: INÉDITAS, temas fictícios marcados na tela "tema elaborado para fins didáticos"; cada alternativa errada é
#   um erro clássico da série. Gabaritos: 1 B · 2 C · 3 C · 4 B · 5 A.
# Desafio: os 5 temas da seção 03; 2016 resolvido ao vivo como modelo (pergunta e tese elaboradas para fins didáticos).
# Cores: azul = definição/tema · verde = método · amarelo = armadilha · vermelho = erro/penalidade · roxo = regra oficial.

TITULO = "Revisão: as pegadinhas da leitura da proposta e o desafio dos 5 temas — Redação ENEM, episódio 6"

# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo da folha em branco: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Esta é a aula de revisão, com clima de desafio e de jogo: "
            "faça as perguntas com suspense, revele as respostas com entusiasmo, mostre surpresa nas pegadinhas e "
            "comemore os acertos. Ritmo didático e tranquilo, sem pressa, respeitando as pausas entre as frases. "
            "Leia apenas o texto, exatamente como está escrito, sem acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Ler a proposta leva *poucos minutos* [p=0.3] {b}e decide se o seu texto pode chegar a *mil* [p=0.3] {c}ou fica "
        "preso em *quarenta pontos* em três competências. [p=0.5] {d}Vamos ver se você está pronto."),

    # ================= OS TRÊS HÁBITOS =================
    dict(id="02", block="habitos", text=
        "{t}Primeiro, [p=0.2] um teste de memória. [p=0.3] {a}Quais são os *três hábitos* que mais rendem na leitura da "
        "proposta? [p=0.3] {p}Pause e tente lembrar. [p=2.0]"),
    dict(id="03", block="habitos", text=
        "{a}Um: [p=0.2] decomponha a frase temática em blocos [p=0.2] e anote o que cada um obriga o texto a discutir. "
        "[p=0.4] {b}Dois: [p=0.2] use os textos motivadores para *entender,* [p=0.2] não para *preencher:* [p=0.2] linhas "
        "copiadas não contam [p=0.2] e a cópia baixa a nota. [p=0.4] {c}Três: [p=0.2] teste a tese contra a frase temática "
        "*antes de escrever:* [p=0.2] se algum bloco ficou de fora, [p=0.2] o texto corre o risco de tangenciar."),

    # ================= O MAPA DA SÉRIE =================
    dict(id="04", block="mapa", text=
        "{t}E as imagens que a gente usou na série? [p=0.3] {a}A frase temática é um *endereço completo,* [p=0.2] e os "
        "blocos são as partes do endereço. [p=0.4] {b}O foco é *escolher a porta,* [p=0.2] sem trocar de endereço. [p=0.4] "
        "{c}Os motivadores são *GPS,* [p=0.2] {d}e linha copiada é *linha fantasma.* [p=0.4] {e}Tangenciar é bairro certo, "
        "[p=0.2] casa errada; [p=0.2] fugir é *outra cidade.* [p=0.4] {f}E os seis passos são o *checklist do piloto.*"),

    # ================= VERDADEIRO OU FALSO =================
    dict(id="05", block="vf", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso.* [p=0.3] Dez frases, [p=0.2] dez pausas. [p=0.4] {q}Primeira: [p=0.2] dá para "
        "descobrir o tema lendo só os textos motivadores. [p=0.2] {p}Pause. [p=2.0] {r}*Falso!* [p=0.3] {w}Engana porque os "
        "motivadores falam do mesmo problema. [p=0.3] {k}Mas a frase temática é a referência: [p=0.2] o recorte está nela."),
    dict(id="06", block="vf", text=
        "{q}Segunda: [p=0.2] um texto só sobre o assunto amplo tangencia, [p=0.2] e fica limitado a quarenta em C dois, C três "
        "e C cinco. [p=0.2] {p}Pause. [p=2.0] {r}*Verdadeiro!* [p=0.3] {w}Parece exagero, porque o texto fala do assunto. "
        "[p=0.3] {k}Mas cada bloco da frase temática precisa ser discutido."),
    dict(id="07", block="vf", text=
        "{q}Terceira: [p=0.2] no Brasil é só um enfeite da frase. [p=0.2] {p}Pause. [p=2.0] {r}*Falso!* [p=0.3] {w}Engana "
        "porque aparece quase sempre, [p=0.2] no fim. [p=0.3] {k}Mas é exigência: [p=0.2] tratar só de outro país foi exemplo "
        "oficial de tangenciamento em dois mil e vinte e cinco."),
    dict(id="08", block="vf", text=
        "{q}Quarta: [p=0.2] escolher só duas causas para discutir é um foco legítimo. [p=0.2] {p}Pause. [p=2.0] "
        "{r}*Verdadeiro!* [p=0.3] {w}Parece corte, [p=0.2] porque ficou muita coisa de fora. [p=0.3] {k}Mas selecionar causas "
        "é legítimo; [p=0.2] retirar um delimitador, não. [p=0.2] É escolher a porta, sem trocar de endereço."),
    dict(id="09", block="vf", text=
        "{q}Quinta: [p=0.2] dizer que é um tema importante já é ter uma tese. [p=0.2] {p}Pause. [p=2.0] {r}*Falso!* [p=0.3] "
        "{w}Engana porque a frase usa as palavras da prova. [p=0.3] {k}Mas é um tema importante não é ponto de vista: "
        "[p=0.2] tome posição sobre o recorte."),
    dict(id="10", block="vf", text=
        "{q}Sexta: [p=0.2] uma linha com um pedaço copiado deixa de contar inteira. [p=0.2] {p}Pause. [p=2.0] "
        "{r}*Verdadeiro!* [p=0.3] {w}Parece injusto, [p=0.2] porque o resto da linha é seu. [p=0.3] {k}Mas linhas copiadas, "
        "mesmo em parte, não contam: [p=0.2] é a linha fantasma."),
    dict(id="11", block="vf", text=
        "{q}Sétima: [p=0.2] uma redação feita só com as ideias da coletânea chega ao topo da competência três. [p=0.2] "
        "{p}Pause. [p=2.0] {r}*Falso!* [p=0.3] {w}Engana porque são fontes oficiais da prova. [p=0.3] {k}Mas argumentos "
        "limitados aos motivadores ficam nos *níveis médios* da C três."),
    dict(id="12", block="vf", text=
        "{q}Oitava: [p=0.2] gráficos e imagens também mostram o problema. [p=0.2] {p}Pause. [p=2.0] {r}*Verdadeiro!* [p=0.3] "
        "{w}Muita gente pula, achando que só o texto escrito conta. [p=0.3] {k}Interprete o que eles mostram, [p=0.2] em vez de "
        "transcrever."),
    dict(id="13", block="vf", text=
        "{q}Nona: [p=0.2] tangenciar zera a redação. [p=0.2] {p}Pause. [p=2.0] {r}*Falso!* [p=0.3] {w}Engana porque os dois "
        "são erros de tema. [p=0.3] {k}Mas quem zera é a fuga; [p=0.2] o tangenciamento limita três competências, [p=0.2] e a "
        "C um e a C quatro continuam avaliadas normalmente."),
    dict(id="14", block="vf", text=
        "{q}Décima: [p=0.2] o melhor momento de conferir o tema é no fim, [p=0.2] na folha definitiva. [p=0.2] {p}Pause. "
        "[p=2.0] {r}*Falso!* [p=0.3] {w}Engana porque parece revisão caprichada. [p=0.3] {k}Mas confira na tese, antes de "
        "desenvolver: [p=0.2] corrigir o recorte no rascunho custa minutos; [p=0.2] na folha definitiva, [p=0.2] a nota."),

    # ================= QUESTÃO 1: ASSUNTO × TEMA =================
    dict(id="15", block="q1", text=
        "{t}Agora, cinco questões inéditas. [p=0.3] {r}Lembrando: [p=0.2] o assunto é a cidade, [p=0.2] o tema é o endereço "
        "completo. [p=0.4] {a}Questão um. [p=0.2] Considere a frase temática: [p=0.2] Desafios para a inclusão digital de "
        "idosos no Brasil. [p=0.3] Assinale o assunto amplo e o tema. [p=0.4] {A}A: [p=0.2] assunto, a frase inteira; "
        "[p=0.2] tema, inclusão digital. [p=0.4] {B}B: [p=0.2] assunto, inclusão digital; [p=0.2] tema, a frase inteira. "
        "[p=0.4] {C}C: [p=0.2] assunto, inclusão digital; [p=0.2] tema, os idosos precisam de apoio do Estado para usar a "
        "internet. [p=0.4] {D}D: [p=0.2] assunto, idosos; [p=0.2] tema, inclusão digital. [p=0.4] {E}E: [p=0.2] assunto e "
        "tema são a mesma coisa. [p=0.4] {p}Pause e tente! [p=2.0]"),
    dict(id="16", block="q1", text=
        "{ok}Letra *B.* [p=0.3] O tema é o recorte inteiro que a prova dá. [p=0.4] {xa}A A inverte os dois. [p=0.3] {xc}A C "
        "confunde tema com *tese:* [p=0.2] aquilo é uma posição. [p=0.3] {xd}A D fica só no núcleo [p=0.2] e perde os outros "
        "blocos. [p=0.3] {xe}E a E esquece que o tema é um recorte do assunto."),

    # ================= QUESTÃO 2: A TESE QUE COBRE OS BLOCOS =================
    dict(id="17", block="q2", text=
        "{r}Lembrando: [p=0.2] tese é posição, mais dois eixos, mais todos os blocos. [p=0.4] {a}Questão dois. [p=0.2] Tema: "
        "[p=0.2] Caminhos para combater o desperdício de alimentos no Brasil. [p=0.3] Qual tese cobre todos os blocos? "
        "[p=0.4] {A}A: [p=0.2] o desperdício de alimentos é um problema que afeta o mundo inteiro. [p=0.4] {B}B: [p=0.2] o "
        "desperdício de alimentos no Brasil é um tema muito importante, que deve ser discutido."),
    dict(id="18", block="q2", text=
        "{C}C: [p=0.2] no Brasil, o desperdício de alimentos persiste pela falta de informação sobre o reaproveitamento [p=0.2] "
        "e pela falta de incentivo à doação, [p=0.2] e combatê-lo exige educação alimentar e regras que facilitem doar. [p=0.4] "
        "{D}D: [p=0.2] no Brasil, muitos alimentos são jogados fora todos os dias. [p=0.4] {E}E: [p=0.2] este texto vai "
        "discutir caminhos para combater o desperdício de alimentos no Brasil. [p=0.4] {p}Pause e tente! [p=2.0]"),
    dict(id="19", block="q2", text=
        "{ok}Letra *C:* [p=0.2] tem combater, [p=0.2] desperdício [p=0.2] e Brasil, [p=0.2] toma posição [p=0.2] e anuncia "
        "dois eixos. [p=0.4] {xa}A A fica no assunto amplo, [p=0.2] sem Brasil e sem caminhos. [p=0.3] {xb}A B repete o tema. "
        "[p=0.3] {xd}A D é um fato, [p=0.2] sem posição e sem caminhos. [p=0.3] {xe}E a E só anuncia."),

    # ================= QUESTÃO 3: MOTIVADORES × CÓPIA =================
    dict(id="20", block="q3", text=
        "{r}Lembrando: [p=0.2] o motivador é GPS, [p=0.2] e linha copiada é linha fantasma. [p=0.4] {a}Questão três. "
        "[p=0.2] Tema: [p=0.2] Desafios para o acesso à leitura no Brasil. [p=0.3] Um texto motivador diz: [p=0.2] bibliotecas "
        "públicas de várias cidades reduziram o horário por falta de servidores. [p=0.3] Qual uso está de acordo com a "
        "Cartilha? [p=0.4] {A}A: [p=0.2] copiar a frase na introdução, [p=0.2] porque ela resume bem o problema. [p=0.4] "
        "{B}B: [p=0.2] copiar só metade da frase [p=0.2] e completar a linha com palavras suas."),
    dict(id="21", block="q3", text=
        "{C}C: [p=0.2] retomar a ideia com outra estrutura [p=0.2] e acrescentar uma causa própria. [p=0.4] {D}D: [p=0.2] "
        "ignorar o texto, [p=0.2] porque a frase temática já basta. [p=0.4] {E}E: [p=0.2] construir todos os argumentos só "
        "com os textos motivadores. [p=0.4] {p}Pause e tente! [p=2.0]"),
    dict(id="22", block="q3", text=
        "{ok}Letra *C:* [p=0.2] paráfrase, [p=0.2] mais algo seu. [p=0.4] {xa}A A é cópia: [p=0.2] linha fantasma. [p=0.3] "
        "{xb}A B também: [p=0.2] meia linha copiada, [p=0.2] linha inteira fora. [p=0.3] {xd}A D abandona o GPS. [p=0.3] "
        "{xe}E a E fica presa à coletânea: [p=0.2] níveis médios."),

    # ================= QUESTÃO 4: COMPLETA × TANGENCIA × FUGA =================
    dict(id="23", block="q4", text=
        "{r}Lembrando: [p=0.2] endereço exato, completa; [p=0.2] bairro certo, casa errada, tangencia; [p=0.2] outra cidade, "
        "fuga. [p=0.4] {a}Questão quatro. [p=0.2] Tema: [p=0.2] Desafios para a valorização dos professores da educação básica "
        "no Brasil. [p=0.3] {i}A redação um fala só dos professores da Finlândia, [p=0.2] sem ligar ao Brasil. [p=0.3] {ii}A "
        "dois discute salários e falta de reconhecimento dos professores brasileiros, [p=0.2] e como superar isso. [p=0.3] "
        "{iii}A três fala do uso de redes sociais por adolescentes."),
    dict(id="24", block="q4", text=
        "{A}A: [p=0.2] a um foge ao tema; [p=0.2] a dois é completa; [p=0.2] a três foge. [p=0.4] {B}B: [p=0.2] a um tangencia, "
        "com C dois, C três e C cinco limitadas a quarenta; [p=0.2] a dois é completa; [p=0.2] a três foge e zera. [p=0.4] "
        "{C}C: [p=0.2] a um tangencia e recebe zero; [p=0.2] a dois é completa; [p=0.2] a três foge. [p=0.4] {D}D: [p=0.2] a "
        "um tangencia, com as cinco competências limitadas a quarenta; [p=0.2] a dois é completa; [p=0.2] a três foge. "
        "[p=0.4] {E}E: [p=0.2] a um e a três tangenciam; [p=0.2] a dois é completa. [p=0.4] {p}Pause e tente! [p=2.0]"),
    dict(id="25", block="q4", text=
        "{ok}Letra *B.* [p=0.3] {xa}A A chama de fuga um texto que está na cidade certa. [p=0.3] {xc}A C acha que tangenciar "
        "zera. [p=0.3] {xd}A D estende o teto às cinco competências. [p=0.3] {xe}E a E não vê que a três nem fala de "
        "professores."),

    # ================= QUESTÃO 5: FOCO × CORTE =================
    dict(id="26", block="q5", text=
        "{r}Lembrando: [p=0.2] o foco escolhe a porta, [p=0.2] mas não troca de endereço. [p=0.4] {a}Questão cinco. [p=0.2] "
        "Tema: [p=0.2] Desafios para a mobilidade urbana de pessoas com deficiência no Brasil. [p=0.3] Qual plano faz um foco "
        "legítimo? [p=0.4] {A}A: [p=0.2] discutir só a falta de rampas e o transporte público inadequado no Brasil, [p=0.2] e "
        "como superá-los. [p=0.4] {B}B: [p=0.2] discutir o trânsito das grandes cidades, [p=0.2] sem falar de pessoas com "
        "deficiência."),
    dict(id="27", block="q5", text=
        "{C}C: [p=0.2] discutir a mobilidade de pessoas com deficiência em outros países. [p=0.4] {D}D: [p=0.2] tratar de "
        "todas as causas possíveis, [p=0.2] porque escolher só duas seria tangenciar. [p=0.4] {E}E: [p=0.2] discutir as "
        "dificuldades de pessoas com deficiência no mercado de trabalho brasileiro. [p=0.4] {p}Pause e tente! [p=2.0]"),
    dict(id="28", block="q5", text=
        "{ok}Letra *A:* [p=0.2] escolheu dois eixos [p=0.2] e manteve todos os blocos. [p=0.4] {xb}A B corta o grupo. [p=0.3] "
        "{xc}A C corta o lugar. [p=0.3] {xd}A D confunde foco com corte. [p=0.3] {xe}E a E troca o núcleo: [p=0.2] a "
        "mobilidade urbana ficou de fora."),

    # ================= DESAFIO PRÁTICO =================
    dict(id="29", block="desafio", text=
        "{t}Agora, [p=0.2] o *desafio.* [p=0.3] {a}Pegue os cinco temas da nossa tabela: [p=0.2] dois mil e dezesseis, "
        "[p=0.2] dezessete, [p=0.2] vinte, [p=0.2] vinte e dois [p=0.2] e vinte e cinco. [p=0.4] {b}Para cada um, [p=0.2] em "
        "no máximo *cinco minutos:* [p=0.3] {c}divida a frase temática em blocos, [p=0.2] {d}escreva a pergunta-problema [p=0.2] "
        "{e}e uma tese provisória com dois eixos. [p=0.4] {f}Depois, [p=0.2] ponha cada tese ao lado da frase temática [p=0.2] "
        "e marque os blocos que ela cobre. [p=0.3] Se faltar algum, [p=0.2] *reescreva.*"),
    dict(id="30", block="modelo", text=
        "{t}Eu faço o primeiro, [p=0.2] como modelo. [p=0.3] {a}Dois mil e dezesseis: [p=0.2] Caminhos para combater a "
        "intolerância religiosa no Brasil. [p=0.4] {b}Blocos: [p=0.2] caminhos para combater, [p=0.2] que pede reconhecer o "
        "problema e discutir formas de enfrentá-lo; [p=0.3] {c}intolerância religiosa, [p=0.2] o núcleo; [p=0.3] {d}e no "
        "Brasil, [p=0.2] o lugar."),
    dict(id="31", block="modelo", text=
        "{a}Pergunta: [p=0.2] por que a intolerância religiosa persiste no Brasil, [p=0.2] e como combatê-la? [p=0.5] "
        "{b}Tese: [p=0.2] no Brasil, a intolerância religiosa persiste pelo desconhecimento sobre as diferentes crenças "
        "[p=0.2] e pela falta de punição aos ataques, [p=0.3] e combatê-la exige educação para o respeito à diversidade "
        "[p=0.2] e punição efetiva."),
    dict(id="32", block="modelo", text=
        "{t}Conferência. [p=0.3] {a}Caminhos para combater? [p=0.2] Tem. [p=0.3] {b}Intolerância religiosa? [p=0.2] Tem. "
        "[p=0.3] {c}No Brasil? [p=0.2] Tem. [p=0.3] {d}Dois eixos: [p=0.2] desconhecimento e falta de punição. [p=0.4] "
        "{e}Agora é com você: [p=0.2] os outros quatro, [p=0.2] cinco minutos cada."),

    # ================= CHECKLIST DE DOMÍNIO =================
    dict(id="33", block="dominio", text=
        "{t}Para fechar, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria explicar em voz alta "
        "para outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}O que não marcou, [p=0.2] reveja o episódio "
        "correspondente."),
    dict(id="34", block="dominio", text=
        "{e1}Episódio um: [p=0.2] as três partes da proposta, [p=0.2] as exigências do comando, [p=0.2] e assunto, tema e "
        "tese com um exemplo real. [p=0.4] {e2}Episódio dois: [p=0.2] núcleo e delimitadores, [p=0.2] o que pedem desafios "
        "para, [p=0.2] caminhos para [p=0.2] e perspectivas acerca de, [p=0.2] foco versus tema, [p=0.2] e a pergunta-problema."),
    dict(id="35", block="dominio", text=
        "{e3}Episódio três: [p=0.2] os três passos da Cartilha nos motivadores, [p=0.2] o que acontece com linhas copiadas, "
        "[p=0.2] e a paráfrase com algo seu. [p=0.4] {e4}Episódio quatro: [p=0.2] completa, tangencia e fuga, [p=0.2] com as "
        "consequências. [p=0.4] {e5}Episódio cinco: [p=0.2] a tese provisória que cobre todos os blocos, [p=0.2] e a "
        "conferência antes de desenvolver."),

    # ================= PONTE E CTA =================
    dict(id="36", block="ponte", text=
        "{a}O próximo assunto é *Introdução:* [p=0.2] contextualização e apresentação da tese. [p=0.4] {b}Ele começa exatamente "
        "onde este termina: [p=0.3] {c}na tese que cobre o recorte, [p=0.2] {d}que vai virar o *primeiro parágrafo* da sua "
        "redação."),
    dict(id="37", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *a Redação do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantas das dez você acertou no verdadeiro ou falso? "
        "[p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
