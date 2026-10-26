# Roteiro — Compreensão Global e Tese, Episódio 7 de 7: Revisão geral, pegadinhas e treino (aula para iniciantes)
# Base: Estudos/Enem/estudos/05-linguagens/01-compreensao-global-tese.html — seções 01, 10, 11 e 13
#   (os 6 passos da seção 09 já entraram no ep. 3 e são só relembrados aqui).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora retomadas (uma por episódio, mesmo ícone na tela):
#   ep1 tese = tampo da mesa · ep2 resumo = mensagem de WhatsApp · ep3 armadilhas = roupa do tamanho errado ·
#   ep4 posição da tese = trailer × filme de detetive × foto sem legenda · ep5 palavras-sinal = placas de trânsito ·
#   ep6 tese implícita = o olhar do fotógrafo.
# Verdadeiro ou falso: os 9 erros da seção 11, cada um com lembrete → afirmação → pausa → resposta → por que engana → regra.
#   Itens 4, 6 e 8 viram afirmações VERDADEIRAS (a regra certa), para o aluno não acertar no chute "é tudo falso".
# Questões 1 a 5: INÉDITAS, textos-base escritos para esta aula ("Texto elaborado para fins didáticos" na tela);
#   NÃO usam as Questões 1–9 da seção 12. Gabarito e armadilhas (nomes do ep. 3):
#   Q1 artigo dedutivo ........ C · A redução · B extrapolação · D contradição · E verdade do mundo
#   Q2 "Há quem diga que…" .... A · B contradição (a voz que o autor derruba) · C redução · D tema certo, tese errada · E extrapolação
#   Q3 indutivo ............... D · A redução · B extrapolação · C contradição · E verdade do mundo
#   Q4 crônica (implícita) .... B · A redução · C ao pé da letra = contradição · D extrapolação · E verdade do mundo
#   Q5 divulgação científica .. E · A extrapolação de causa · B verdade do mundo · C contradição · D redução
# Cores: azul = tese/definição · verde = pista/palavra-sinal · amarelo = armadilha · vermelho = erro · roxo = regra.

TITULO = "As 5 Pegadinhas da Tese no ENEM + 5 Questões Inéditas | Interpretação Ep. 7"
PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Quase toda questão de Linguagens, [p=0.2] e muitas de Humanas e de Natureza, [p=0.3] {b}termina perguntando "
        "*o que o texto diz como um todo.* [p=0.5] {c}Este é o assunto que *mais rende ponto* [p=0.2] na prova inteira."),
    dict(id="02", block="promessa", text=
        "{t}Hoje, a revisão dos seis episódios. [p=0.3] {a}A mesa, [p=0.2] {b}o WhatsApp, [p=0.2] {c}a roupa, [p=0.2] "
        "{d}o trailer, [p=0.2] {e}as placas [p=0.2] {f}e o fotógrafo. [p=0.4] {g}E a regra é esta: [p=0.2] eu *pergunto* antes "
        "de explicar, [p=0.2] e você pausa e responde."),

    # ================= COMO O ENEM COBRA =================
    dict(id="03", block="cobra", text=
        "{t}Primeiro, como o ENEM pergunta. [p=0.3] {a}O comando direto: [p=0.2] *a tese defendida é.* [p=0.3] {b}O resumo. "
        "[p=0.3] {c}O título. [p=0.3] {d}A função de um parágrafo. [p=0.3] {e}E a tese implícita, [p=0.2] em crônicas e charges."),
    dict(id="04", block="habitos", text=
        "{t}E três hábitos rendem mais que todo o resto. [p=0.4] {a}Um: [p=0.2] separar *assunto* de *tese,* [p=0.2] "
        "o tampo da mesa. [p=0.4] "
        "{b}Dois: [p=0.2] formular a tese *antes* de ler as alternativas, [p=0.2] numa frase, [p=0.2] como uma mensagem de WhatsApp. "
        "[p=0.4] {c}Três: [p=0.2] reconhecer as *armadilhas,* [p=0.2] as roupas do tamanho errado."),

    # ================= VERDADEIRO OU FALSO =================
    dict(id="05", block="vf", text=
        "{t}Agora, nove afirmações. [p=0.3] {a}Pause em cada uma [p=0.2] e responda em voz alta."),
    dict(id="06", block="vf", text=
        "{t}Lembra da mesa? [p=0.2] O tampo é a tese. [p=0.4] {q}Pedem a tese do texto do celular, [p=0.2] e você responde: "
        "[p=0.2] *celular na escola.* [p=0.2] Certo ou errado? [p=0.3] {p}Pause. [p=2.0]"),
    dict(id="07", block="vf", text=
        "{r}*Errado.* [p=0.3] {a}Engana porque tem as palavras do texto. [p=0.4] {b}Mas *tese tem verbo e posição:* [p=0.2] "
        "deve ser ensinado, [p=0.2] não só proibido."),
    dict(id="08", block="vf", text=
        "{t}As pernas da mesa são os exemplos e argumentos. [p=0.4] {q}Verdadeiro ou falso: [p=0.2] *o exemplo mais marcante "
        "costuma ser a ideia central.* [p=0.3] {p}Pause. [p=2.0]"),
    dict(id="09", block="vf", text=
        "{r}*Falso.* [p=0.3] {a}Engana porque é o trecho que fica na memória. [p=0.4] {b}Mas *exemplo é perna, não tampo.* "
        "[p=0.2] Marcar o exemplo é a armadilha da *redução.*"),
    dict(id="10", block="vf", text=
        "{t}A tese pode vir no começo, [p=0.2] como num trailer, [p=0.2] ou só no fim, [p=0.2] como num filme de detetive. "
        "[p=0.4] {q}Verdadeiro ou falso: [p=0.2] *a primeira frase do texto é sempre a tese.* [p=0.3] {p}Pause. [p=2.0]"),
    dict(id="11", block="vf", text=
        "{r}*Falso.* [p=0.3] {a}Engana porque muito texto começa mesmo pela tese. [p=0.4] {b}Mas a primeira frase pode ser a "
        "opinião que o autor vai derrubar. [p=0.3] *Leia até o primeiro mas:* [p=0.2] é a placa de curva."),
    dict(id="12", block="vf", text=
        "{t}A roupa larga demais [p=0.2] é a que passa da borda do texto. [p=0.4] {q}Verdadeiro ou falso: [p=0.2] "
        "*alternativa com sempre, todos ou deve-se merece desconfiança.* [p=0.3] {p}Pause. [p=2.0]"),
    dict(id="13", block="vf", text=
        "{r}*Verdadeiro.* [p=0.3] {a}A pegadinha: [p=0.2] essas palavras soam completas. [p=0.4] {b}Confira se o texto "
        "vai tão longe. [p=0.2] Se não vai, [p=0.2] é *extrapolação.*"),
    dict(id="14", block="vf", text=
        "{t}Agora, a roupa do mesmo tecido, [p=0.2] com outro corte. [p=0.4] {q}Verdadeiro ou falso: [p=0.2] *se a alternativa "
        "usa as palavras do texto, ela está certa.* [p=0.3] {p}Pause. [p=2.0]"),
    dict(id="15", block="vf", text=
        "{r}*Falso.* [p=0.3] {a}Engana porque você reconhece as palavras. [p=0.4] {b}Mas confira *o que se afirma com elas.* "
        "[p=0.2] Mesmo assunto com outra posição [p=0.2] é *tema certo, tese errada.*"),
    dict(id="16", block="vf", text=
        "{t}E a roupa que nem é do seu armário. [p=0.4] {q}Verdadeiro ou falso: [p=0.2] *uma alternativa verdadeira no mundo "
        "pode estar errada na questão.* [p=0.3] {p}Pause. [p=2.0]"),
    dict(id="17", block="vf", text=
        "{r}*Verdadeiro.* [p=0.3] {a}A pegadinha: [p=0.2] você *sabe* que aquilo é verdade. [p=0.4] {b}Mas só vale o texto. [p=0.2] Pergunte: [p=0.2] *em que linha isso está?*"),
    dict(id="18", block="vf", text=
        "{t}O fotógrafo não diz a opinião; [p=0.2] ela está na escolha. [p=0.4] {q}Verdadeiro ou falso: [p=0.2] *num texto "
        "irônico, o elogio deve ser lido ao pé da letra.* [p=0.3] {p}Pause. [p=2.0]"),
    dict(id="19", block="vf", text=
        "{r}*Falso.* [p=0.3] {a}Engana porque você está repetindo o que está escrito. [p=0.4] {b}Mas *elogio irônico é crítica.* "
        "[p=0.2] Ao pé da letra, [p=0.2] você marca o contrário: [p=0.2] uma *contradição.*"),
    dict(id="20", block="vf", text=
        "{q}Verdadeiro ou falso: [p=0.2] *um texto sem nenhuma frase de opinião pode ter tese.* [p=0.3] {p}Pause. [p=2.0]"),
    dict(id="21", block="vf", text=
        "{r}*Verdadeiro.* [p=0.3] {a}A pegadinha: [p=0.2] não achei nenhum eu acho, [p=0.2] então não tem tese. "
        "[p=0.4] {b}A opinião está na *seleção,* [p=0.2] no *contraste* [p=0.2] e no *tom.*"),
    dict(id="22", block="vf", text=
        "{t}E a última. [p=0.3] {q}Verdadeiro ou falso: [p=0.2] *para ganhar tempo, leia as alternativas antes de ter a sua tese.* "
        "[p=0.3] {p}Pause. [p=2.0]"),
    dict(id="23", block="vf", text=
        "{r}*Falso.* [p=0.3] {a}Engana porque parece economizar tempo. [p=0.4] {b}Mas, sem a sua frase de WhatsApp pronta, "
        "[p=0.2] *todas parecem plausíveis.* [p=0.3] *Formule primeiro, compare depois.*"),

    # ================= O MÉTODO =================
    dict(id="24", block="passos", text=
        "{t}Agora, cinco questões *novas,* [p=0.3] com os seis passos do episódio três: [p=0.3] {a}o comando, [p=0.2] {b}a fonte, [p=0.2] {c}a leitura marcando "
        "as viradas, [p=0.2] {d}a sua tese, [p=0.2] {e}eliminar pelo tipo de erro, [p=0.2] {f}e a palavra que decide."),

    # ================= QUESTÃO 1: DEDUTIVO =================
    dict(id="25", block="q1", text=
        "{t}Questão um. [p=0.3] {a}O comando: [p=0.2] *a tese defendida no texto é a de que.* [p=0.3] Leio pensando alto. [p=0.4] "
        "{f1}Ler em voz alta para crianças pequenas é um dos investimentos mais baratos e eficazes que uma família pode fazer. [p=0.3] "
        "{c1}Opinião logo na primeira frase. [p=0.2] Pode ser trailer. [p=0.4] "
        "{f2}A leitura compartilhada amplia o vocabulário antes da alfabetização. [p=0.3] "
        "{f3}Também cria um momento de atenção exclusiva, cada vez mais raro na rotina das telas. [p=0.3] "
        "{f4}E não exige nada além de um livro e quinze minutos por dia. [p=0.4] "
        "{c2}O resto sustenta a primeira: [p=0.2] *texto dedutivo.*"),
    dict(id="26", block="q1", text=
        "{t}Minha tese, antes das alternativas: [p=0.2] *ler para crianças é barato e dá resultado.* [p=0.4] "
        "{a}A: [p=0.2] a leitura compartilhada amplia o vocabulário antes da alfabetização. [p=0.3] "
        "{b}B: [p=0.2] as famílias devem proibir as telas para que as crianças leiam mais. [p=0.3] "
        "{c}C: [p=0.2] ler em voz alta para crianças pequenas é um investimento barato e eficaz. [p=0.3] "
        "{d}D: [p=0.2] ler para crianças exige tempo e dinheiro que poucas famílias têm. [p=0.3] "
        "{e}E: [p=0.2] crianças que leem mais tiram notas melhores na escola. [p=0.4] {p}*Pause e dê o nome de cada armadilha.* [p=2.0]"),
    dict(id="27", block="q1", text=
        "{t}Vamos conferir. [p=0.3] {d}A D diz o oposto: [p=0.2] *contradição.* [p=0.3] {b}A B pede proibir telas, [p=0.2] "
        "e o texto não propõe isso: [p=0.2] *extrapolação.* [p=0.3] {a}A A é verdadeira, [p=0.2] mas é uma perna só: [p=0.2] "
        "*redução.* [p=0.3] {e}A E pode até ser verdade, [p=0.2] mas em que linha está? [p=0.2] *Verdade do mundo.* [p=0.3] "
        "{ok}Sobra a C. [p=0.2] *Letra C.*"),

    # ================= QUESTÃO 2: HÁ QUEM DIGA =================
    dict(id="28", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}O comando: [p=0.2] *o autor defende que.* [p=0.4] "
        "{f1}Há quem diga que o jovem de hoje não lê. [p=0.3] {c1}*Há quem diga:* [p=0.2] a voz do outro. [p=0.4] "
        "{f2}Mas basta ver as filas de autógrafos nas feiras de livros, os clubes de leitura nas redes e os romances que viralizam entre "
        "adolescentes. [p=0.3] {c2}A placa de curva: [p=0.2] *mas.* [p=0.4] "
        "{f3}O jovem lê, e muito; o que mudou foi o que ele lê e onde conversa sobre isso. [p=0.3] "
        "{f4}Quem procura o leitor só na biblioteca é que não o encontra."),
    dict(id="29", block="q2", text=
        "{t}Minha tese: [p=0.2] *o jovem lê; [p=0.2] mudaram o quê e o onde.* [p=0.4] "
        "{a}A: [p=0.2] os jovens continuam lendo; mudaram o que leem e onde conversam sobre leitura. [p=0.3] "
        "{b}B: [p=0.2] o jovem de hoje lê pouco, porque prefere as redes sociais aos livros. [p=0.3] "
        "{c}C: [p=0.2] as feiras de livros reúnem filas enormes de jovens atrás de autógrafos. [p=0.3] "
        "{d}D: [p=0.2] o interesse dos jovens pela leitura depende, sobretudo, das bibliotecas escolares. [p=0.3] "
        "{e}E: [p=0.2] as bibliotecas deveriam ser substituídas por clubes de leitura nas redes. [p=0.4] {p}*Pause.* [p=2.0]"),
    dict(id="30", block="q2", text=
        "{t}Conferindo. [p=0.3] {b}A B é a primeira frase, [p=0.2] a que o autor derruba: [p=0.2] *contradição.* [p=0.3] "
        "{c}A C é só um exemplo: [p=0.2] *redução.* [p=0.3] {d}A D fala de leitura e de biblioteca, [p=0.2] mas defende outra "
        "coisa: [p=0.2] *tema certo, tese errada.* [p=0.3] {e}A E propõe trocar bibliotecas: [p=0.2] *extrapolação.* [p=0.3] "
        "{ok}*Letra A.*"),

    # ================= QUESTÃO 3: INDUTIVO =================
    dict(id="31", block="q3", text=
        "{t}Questão três. [p=0.3] {a}O comando: [p=0.2] *a ideia central do texto é a de que.* [p=0.4] "
        "{f1}Num bairro, uma praça ganhou bancos e iluminação e passou a receber feiras aos domingos. [p=0.3] "
        "{f2}Em outro, uma rua fechada para carros nos fins de semana virou ponto de encontro de famílias. [p=0.3] "
        "{c2}Casos, [p=0.2] e nenhuma opinião ainda. [p=0.4] "
        "{f3}Num terceiro, um viaduto ganhou quadra e grafites e deixou de ser evitado à noite. [p=0.3] "
        "{f4}Quando a cidade cuida do espaço público, as pessoas voltam a ocupá-lo. [p=0.4] "
        "{c4}A tese no fim, [p=0.2] como filme de detetive: [p=0.2] *indutivo.*"),
    dict(id="32", block="q3", text=
        "{t}Minha tese é a última frase. [p=0.4] "
        "{a}A: [p=0.2] uma praça reformada passou a receber feiras aos domingos. [p=0.3] "
        "{b}B: [p=0.2] todas as cidades devem fechar ruas para carros nos fins de semana. [p=0.3] "
        "{c}C: [p=0.2] reformar espaços públicos afasta os moradores, que preferem lugares fechados. [p=0.3] "
        "{d}D: [p=0.2] espaços públicos bem cuidados voltam a ser ocupados pelas pessoas. [p=0.3] "
        "{e}E: [p=0.2] praças arborizadas ajudam a reduzir a temperatura das cidades. [p=0.4] {p}*Pause.* [p=2.0]"),
    dict(id="33", block="q3", text=
        "{t}Conferindo. [p=0.3] {c}A C é o oposto: [p=0.2] *contradição.* [p=0.3] {b}A B tem todas e devem: [p=0.2] *extrapolação.* "
        "[p=0.3] {a}A A é um caso só: [p=0.2] *redução.* [p=0.3] {e}A E não está em linha nenhuma: [p=0.2] *verdade do mundo.* "
        "[p=0.3] {ok}*Letra D.*"),

    # ================= QUESTÃO 4: CRÔNICA =================
    dict(id="34", block="q4", text=
        "{t}Questão quatro: [p=0.2] uma crônica. [p=0.3] {a}O comando: [p=0.2] *a crônica sugere que.* [p=0.2] Sugere: [p=0.2] "
        "tese implícita. [p=0.4] "
        "{f1}O condomínio instalou um aplicativo para tudo: reservar a churrasqueira, avisar da encomenda, reclamar do barulho. [p=0.3] "
        "{f2}Ontem, o elevador parou entre dois andares, comigo e com o vizinho do 302. [p=0.3] "
        "{f3}Em vinte minutos, descobri que ele é professor, torce para o meu time e mora ali há oito anos. [p=0.3] "
        "{c3}Oito anos, [p=0.2] e nunca tinham conversado. [p=0.4] "
        "{f4}Quando a porta abriu, ele suspirou: — A gente devia quebrar o elevador mais vezes."),
    dict(id="35", block="q4", text=
        "{t}Olhar de fotógrafo: [p=0.2] {a}lado a lado, [p=0.2] um aplicativo para *tudo* [p=0.2] e oito anos sem conhecer o vizinho. "
        "[p=0.4] {b}Minha tese: [p=0.2] *a praticidade não aproximou ninguém; [p=0.2] foi preciso um imprevisto.* "
        "[p=0.4] {c}A: [p=0.2] os vizinhos descobriram que torcem para o mesmo time. [p=0.3] "
        "{d}B: [p=0.2] a praticidade do aplicativo não aproximou os vizinhos, que só se conheceram por causa de um imprevisto. [p=0.3] "
        "{e}C: [p=0.2] quebrar o elevador mais vezes é um bom jeito de os vizinhos se conhecerem. [p=0.3] "
        "{f}D: [p=0.2] os condomínios deveriam proibir aplicativos para obrigar os moradores a conversar. [p=0.3] "
        "{g}E: [p=0.2] o uso excessivo do celular está ligado a sintomas de ansiedade. [p=0.4] {p}*Pause.* [p=2.0]"),
    dict(id="36", block="q4", text=
        "{t}Conferindo. [p=0.3] {c}A C lê a piada ao pé da letra: [p=0.2] *contradição.* [p=0.3] {d}A D quer proibir aplicativos: "
        "[p=0.2] *extrapolação.* [p=0.3] {a}A A é um detalhe: [p=0.2] *redução.* [p=0.3] {e}A E fala de ansiedade, [p=0.2] "
        "que o texto nem cita: [p=0.2] *verdade do mundo.* [p=0.3] {ok}*Letra B.*"),

    # ================= QUESTÃO 5: DIVULGAÇÃO CIENTÍFICA =================
    dict(id="37", block="q5", text=
        "{t}Questão cinco: [p=0.2] divulgação científica. [p=0.3] {a}O comando: [p=0.2] "
        "*de acordo com o texto.* [p=0.4] "
        "{f1}Um levantamento com três mil adultos observou que quem caminhava ao ar livre pelo menos três vezes por semana relatava, "
        "em média, menos dificuldade para dormir. [p=0.3] {c1}Observou. [p=0.2] Uma *relação.* [p=0.4] "
        "{f2}Os autores alertam que o estudo mostra uma relação, e não prova que a caminhada melhore o sono: quem dorme bem pode "
        "simplesmente ter mais disposição para sair de casa. [p=0.3] {c2}O texto avisa: [p=0.2] *não é causa.*"),
    dict(id="38", block="q5", text=
        "{t}Minha tese: [p=0.2] *há relação, [p=0.2] mas não está provado que uma coisa causa a outra.* [p=0.4] "
        "{a}A: [p=0.2] caminhar ao ar livre faz as pessoas dormirem melhor. [p=0.3] "
        "{b}B: [p=0.2] a luz do sol regula o relógio biológico e melhora o sono. [p=0.3] "
        "{c}C: [p=0.2] o levantamento mostrou que não há relação entre caminhar e dormir bem. [p=0.3] "
        "{d}D: [p=0.2] três mil adultos participaram do levantamento. [p=0.3] "
        "{e}E: [p=0.2] o estudo encontrou uma relação entre caminhar e dormir melhor, mas não provou que uma coisa cause a outra. "
        "[p=0.4] {p}*Pause.* [p=2.0]"),
    dict(id="39", block="q5", text=
        "{t}Conferindo. [p=0.3] {a}A A transforma *relação* em *causa:* [p=0.2] *extrapolação.* [p=0.3] "
        "{b}A B pode estar certa na biologia, [p=0.2] mas não no texto: [p=0.2] *verdade do mundo.* [p=0.3] "
        "{c}A C diz o contrário: [p=0.2] *contradição.* [p=0.3] {d}A D é só um dado: [p=0.2] *redução.* [p=0.3] {ok}*Letra E.*"),

    # ================= OUTRAS ÁREAS =================
    dict(id="40", block="areas", text=
        "{t}E isso não fica só em Linguagens. [p=0.4] {a}Em *Humanas,* [p=0.2] trechos de historiadores e filósofos: [p=0.2] "
        "a tese está lá. [p=0.4] {b}Em *Natureza,* [p=0.2] divulgação científica: [p=0.2] cuidado com a relação que vira *causa.* "
        "[p=0.4] {c}E na *Redação:* [p=0.2] a tese que você aprendeu a achar [p=0.2] é a que vai "
        "precisar *escrever.*"),

    # ================= CHECKLIST =================
    dict(id="41", block="checklist", text=
        "{t}Agora, o checklist. [p=0.3] {a}Marque só o que você conseguiria explicar em voz alta para outra pessoa, [p=0.2] "
        "*sem consultar nada.* [p=0.4] {e1}Tema, assunto e tese, [p=0.2] o teste da discordância e o do apagamento: [p=0.2] "
        "episódio um. [p=0.3] {e2}O resumo em uma frase: [p=0.2] episódio dois. [p=0.3] {e3}As armadilhas, [p=0.2] a tese antes "
        "das alternativas [p=0.2] e os comandos: [p=0.2] episódio três. [p=0.3] {e4}Dedutivo, indutivo e a primeira frase: "
        "[p=0.2] episódio quatro. [p=0.3] {e5}Título, marcas e função do parágrafo: [p=0.2] episódio cinco. [p=0.3] "
        "{e6}A tese implícita: [p=0.2] episódio seis. [p=0.4] {b}O que você não marcou, [p=0.2] *reveja o episódio correspondente.*"),
    dict(id="42", block="meta", text=
        "{t}E a meta antes de considerar dominado: [p=0.3] {a}resolva *vinte e cinco* questões de interpretação [p=0.2] "
        "{b}e acerte pelo menos *dezoito,* [p=0.2] setenta por cento. [p=0.4] {c}Em cada erro, [p=0.2] anote *qual armadilha* "
        "você marcou. [p=0.4] {d}O padrão dos seus erros [p=0.2] mostra o que treinar."),

    # ================= PONTE =================
    dict(id="43", block="ponte", text=
        "{t}E assim fechamos a compreensão global. [p=0.4] {a}O próximo assunto é *informações explícitas e implícitas.* [p=0.3] "
        "{b}Saímos do texto inteiro [p=0.2] e descemos para a frase, [p=0.3] {c}para ver o que está escrito, [p=0.2] "
        "o que está sugerido [p=0.2] {d}e até onde o leitor pode concluir."),
    dict(id="44", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *Linguagens do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantas das cinco questões você acertou? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
