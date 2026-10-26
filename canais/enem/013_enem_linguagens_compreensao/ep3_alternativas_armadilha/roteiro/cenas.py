# Roteiro — Compreensão Global e Tese, Episódio 3: As 5 alternativas-armadilha e o método de 6 passos (aula para iniciantes)
# Base: Estudos/Enem/estudos/05-linguagens/01-compreensao-global-tese.html — seções 08 e 09 + Questões 8 e 9 da seção 12
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: a alternativa certa é a ROUPA DO TAMANHO EXATO do texto.
#   redução = roupa apertada (cobre só um pedaço) · extrapolação = roupa larga demais (passa da borda) ·
#   contradição = roupa do avesso (lugar certo, sentido trocado) · tema certo, tese errada = roupa da mesma loja, de outra pessoa ·
#   verdade do mundo = roupa bonita que nem está no seu guarda-roupa.
# Cotidiano antes do nome: a FOFOCA da promoção da Ana, recontada de cinco jeitos errados.
# Mini-exemplos: a tese do celular do ep. 1 ("A escola deve ensinar a usar o celular, não só proibi-lo.").
# Diagrama do alvo: faixa central = "o que o texto afirma"; redução dentro e pequena; extrapolação passa da borda;
#   contradição no lugar com sinal trocado; verdade do mundo fora do diagrama.
# Sequência eu faço → nós fazemos → você faz: armadilhas com o celular → Questão 8 classificada pensando alto
#   → Questão 9: o aluno pausa e classifica antes da revelação.
# Classificação das erradas = resolução do material: Q8 B tema certo/tese errada · C contradição · D redução ·
#   E extrapolação ("principalmente") | Q9 A verdade do mundo · B contradição · D e E extrapolação.
# Frases-chave (meio e fim, idênticas):
#   1. A certa cobre o texto: nem menos, nem mais, nem o contrário.
#   2. Diz isso? Diz só isso? Diz isso tudo?
#   3. Em que linha isso está?
# Cores: azul = tese/definição · verde = pista/palavra-sinal · amarelo = armadilha · vermelho = erro · roxo = fórmula/regra.

TITULO = "As Alternativas Erradas do ENEM Seguem 5 Moldes | Interpretação Ep. 3"
PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}As alternativas erradas do ENEM *não são aleatórias.* [p=0.4] {b}Quase todas seguem *cinco moldes.* [p=0.4] "
        "{c}Quem conhece os moldes [p=0.2] elimina alternativas em segundos."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai reconhecer cada tipo de armadilha, [p=0.3] {b}e aplicar um *método de seis passos* "
        "[p=0.2] em qualquer questão de interpretação."),

    # ================= PRÉ-REQUISITOS (até 30 s) =================
    dict(id="03", block="prereq", text=
        "{t}Duas lembranças rápidas. [p=0.3] {a}Episódio um: [p=0.2] a *tese* é o que o texto afirma, [p=0.2] como: [p=0.2] "
        "a escola deve ensinar a usar o celular, [p=0.2] não só proibi-lo. [p=0.4] {b}Episódio dois: [p=0.2] o *resumo* em uma frase: "
        "[p=0.2] assunto, [p=0.2] mais o que o texto afirma, [p=0.2] mais o porquê. [p=0.4] {c}Guarde essa tese do celular: "
        "[p=0.2] ela vai servir de exemplo."),

    # ================= DISTRATOR E A ROUPA =================
    dict(id="04", block="roupa", text=
        "{t}Antes, um nome. [p=0.3] {a}Cada alternativa errada se chama *distrator:* [p=0.2] uma alternativa feita para parecer certa. "
        "[p=0.4] {b}E como saber qual é a certa? [p=0.4] {c}Pense numa roupa. [p=0.3] {d}A alternativa certa é a roupa do *tamanho exato* "
        "do texto: [p=0.3] nem apertada, [p=0.2] nem larga, [p=0.2] nem do avesso."),
    dict(id="05", block="fofoca", text=
        "{t}E como os distratores são feitos? [p=0.4] {a}Pense numa fofoca. [p=0.3] {b}Sua vizinha conta: [p=0.2] a Ana foi promovida "
        "no trabalho, [p=0.2] mas vai ter que mudar de cidade. [p=0.4] {c}Agora veja como cinco pessoas recontam essa notícia, "
        "[p=0.2] cada uma errando de um jeito."),

    # ================= A) REDUÇÃO =================
    dict(id="06", block="reducao", text=
        "{t}Primeira pessoa: [p=0.2] a Ana vai mudar de cidade. [p=0.4] {a}Mentira? [p=0.2] Não. [p=0.2] Mas e a promoção? [p=0.3] "
        "Ficou de fora. [p=0.4] {b}Isso é a *redução:* [p=0.2] pegar uma parte como se fosse o todo. [p=0.4] {c}É a roupa *apertada:* "
        "[p=0.2] cobre só um pedaço."),
    dict(id="07", block="reducao", text=
        "{t}Como reconhecer? [p=0.3] {a}A redução é *verdadeira,* [p=0.2] mas corresponde a um trecho só. [p=0.4] {b}Na tese do celular: "
        "[p=0.2] o aluno usa o celular às escondidas. [p=0.4] {c}Está no texto, [p=0.2] mas é um exemplo, [p=0.2] uma perna da mesa. "
        "[p=0.2] *Só um pedaço.*"),

    # ================= B) EXTRAPOLAÇÃO =================
    dict(id="08", block="extrapolacao", text=
        "{t}Segunda pessoa, a que aumenta: [p=0.2] a Ana virou diretora da empresa inteira, [p=0.2] e vai morar no exterior. [p=0.4] "
        "{a}Começou na notícia, [p=0.2] mas foi muito além dela. [p=0.4] {b}Isso é a *extrapolação:* [p=0.2] dizer mais do que o texto "
        "autoriza. [p=0.4] {c}É a roupa *larga demais:* [p=0.2] passa da borda."),
    dict(id="09", block="extrapolacao", text=
        "{t}Como reconhecer? [p=0.3] {a}Desconfie de palavras como: [p=0.2] *sempre,* [p=0.2] *todos,* [p=0.2] *principalmente,* "
        "[p=0.2] *deve-se.* [p=0.4] {b}Na tese do celular: [p=0.2] todas as escolas devem liberar o celular o tempo todo. [p=0.4] "
        "{c}O texto disse todas? [p=0.2] O tempo todo? [p=0.2] Não. [p=0.2] *Foi além.*"),

    # ================= C) CONTRADIÇÃO =================
    dict(id="10", block="contradicao", text=
        "{t}Terceira pessoa, a que conta ao contrário: [p=0.2] a Ana foi rebaixada. [p=0.4] {a}O assunto é o mesmo, [p=0.2] o emprego "
        "da Ana. [p=0.2] Mas o sentido virou. [p=0.4] {b}Isso é a *contradição:* [p=0.2] dizer o oposto do texto. [p=0.4] "
        "{c}É a roupa *do avesso:* [p=0.2] está no lugar certo, [p=0.2] mas com o sentido trocado."),
    dict(id="11", block="contradicao", text=
        "{t}Como reconhecer? [p=0.3] {a}Muitas vezes, [p=0.2] a contradição é a opinião que o próprio autor *derruba.* [p=0.4] "
        "{b}Na tese do celular: [p=0.2] a escola deve proibir o celular. [p=0.4] {c}Para pegar essa armadilha, [p=0.2] confira as frases "
        "de *mas,* [p=0.2] *porém,* [p=0.2] *engano.* [p=0.3] É ali que o autor vira o jogo."),

    # ================= D) TEMA CERTO, TESE ERRADA =================
    dict(id="12", block="temacerto", text=
        "{t}Quarta pessoa: [p=0.2] a Ana pediu para mudar de emprego. [p=0.4] {a}Fala da Ana, [p=0.2] fala de trabalho, [p=0.2] "
        "fala de mudança. [p=0.3] Mas afirma *outra coisa.* [p=0.4] {b}Esse é o *tema certo, tese errada:* [p=0.2] o mesmo assunto, "
        "[p=0.2] defendendo outra posição. [p=0.4] {c}É a roupa da *mesma loja,* [p=0.2] mas de outra pessoa."),
    dict(id="13", block="temacerto", text=
        "{t}Como reconhecer? [p=0.3] {a}Ela usa as palavras-chave do texto, [p=0.2] com *outro verbo.* [p=0.4] {b}Na tese do celular: "
        "[p=0.2] a escola deve comprar celulares para os alunos. [p=0.4] {c}Escola, [p=0.2] celular, [p=0.2] aluno. [p=0.2] Tudo igual. "
        "[p=0.3] Só que o texto falava em *ensinar,* [p=0.2] não em comprar."),

    # ================= E) VERDADE DO MUNDO =================
    dict(id="14", block="verdade", text=
        "{t}Quinta pessoa: [p=0.2] mudar de cidade custa caro. [p=0.4] {a}É verdade? [p=0.2] Pode ser. [p=0.3] Mas a vizinha disse isso? "
        "[p=0.2] Não. [p=0.4] {b}Essa é a *verdade do mundo:* [p=0.2] uma informação correta na vida real, [p=0.2] mas que não está "
        "no texto. [p=0.4] {c}É a roupa bonita [p=0.2] que nem está no seu guarda-roupa."),
    dict(id="15", block="verdade", text=
        "{t}Como reconhecer? [p=0.3] {a}Na tese do celular: [p=0.2] o uso exagerado do celular pode atrapalhar o sono. [p=0.4] "
        "{b}Até pode ser verdade. [p=0.3] Mas o texto não fala disso. [p=0.4] {c}Faça sempre a pergunta: [p=0.2] *em que linha isso está?*"),

    # ================= O ALVO =================
    dict(id="16", block="alvo", text=
        "{t}Agora, as cinco juntas, num desenho. [p=0.3] {a}No centro, [p=0.2] a faixa do que o texto afirma: [p=0.2] ali mora a certa. "
        "[p=0.4] {b}A redução fica dentro, [p=0.2] mas pequena. [p=0.3] {c}A extrapolação passa da borda. [p=0.3] {d}A contradição está "
        "no lugar, [p=0.2] com o sinal trocado. [p=0.3] {e}O tema certo fica ao lado, [p=0.2] defendendo outra coisa. [p=0.3] "
        "{f}E a verdade do mundo [p=0.2] fica *fora* do desenho."),

    # ================= F) AS TRÊS PERGUNTAS =================
    dict(id="17", block="perguntas", text=
        "{t}E na prova, [p=0.2] como testar uma alternativa rápido? [p=0.4] {a}Com três perguntas. [p=0.4] {b}Um: [p=0.2] o texto diz isso? "
        "[p=0.3] Se não diz, [p=0.2] é contradição ou verdade do mundo. [p=0.4] {c}Dois: [p=0.2] diz *só* isso? [p=0.3] Se diz mais coisa, "
        "[p=0.2] é redução. [p=0.4] {d}Três: [p=0.2] diz isso *tudo?* [p=0.3] Se não vai tão longe, [p=0.2] é extrapolação."),

    # ================= G) UMA PALAVRA ESTRAGA =================
    dict(id="18", block="palavra", text=
        "{t}E um último cuidado. [p=0.3] {a}A alternativa mais longa [p=0.2] e mais completa [p=0.2] pode estar quase perfeita. [p=0.4] "
        "{b}Até o final, [p=0.2] que diz: [p=0.2] e, por isso, deve ser proibido. [p=0.4] {c}O acréscimo errado costuma estar no *fim.* "
        "[p=0.3] {d}Por isso, [p=0.2] *leia a alternativa até o fim.* [p=0.2] Uma palavra estraga tudo."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] a certa cobre o texto: [p=0.2] nem menos, [p=0.2] nem mais, [p=0.2] "
        "nem o contrário. [p=0.5] {b}Dois: [p=0.2] diz isso? [p=0.2] Diz só isso? [p=0.2] Diz isso tudo? [p=0.5] {c}Três: [p=0.2] "
        "em que linha isso está?"),

    # ================= O MÉTODO DE 6 PASSOS =================
    dict(id="20", block="metodo", text=
        "{t}Agora, o método de seis passos. [p=0.4] {a}Um: [p=0.2] leia o *comando* primeiro. [p=0.2] Comando é a pergunta que vem antes "
        "das alternativas. [p=0.2] Ele diz o que procurar. [p=0.4] {b}Dois: [p=0.2] olhe título, [p=0.2] fonte e data. [p=0.4] "
        "{c}Três: [p=0.2] leia o texto inteiro, [p=0.2] marcando as viradas, [p=0.2] como mas e porém, [p=0.2] e as conclusões, "
        "[p=0.2] como portanto e assim."),
    dict(id="21", block="metodo", text=
        "{a}Quatro: [p=0.2] diga a tese com as suas palavras, [p=0.2] *antes* de olhar as alternativas. [p=0.4] {b}Cinco: [p=0.2] "
        "elimine pelo tipo de erro. [p=0.2] Primeiro as contradições, [p=0.2] que são as mais fáceis. [p=0.2] Depois as extrapolações. "
        "[p=0.2] Depois as reduções. [p=0.4] {c}Seis: [p=0.2] sobraram duas? [p=0.2] Volte ao texto [p=0.2] e ache a palavra que decide."),

    # ================= DOIS AVISOS =================
    dict(id="22", block="avisos", text=
        "{t}E dois avisos rápidos. [p=0.3] {a}Primeiro: [p=0.2] não responda com a sua opinião. [p=0.3] A pergunta é o que o *texto* "
        "defende. [p=0.3] {b}A certa pode ser uma ideia da qual você discorda, [p=0.2] e a errada, [p=0.2] uma da qual você concorda."),
    dict(id="23", block="avisos", text=
        "{a}Segundo: [p=0.2] leia o comando com precisão. [p=0.4] {b}De acordo com o texto: [p=0.2] pede o que está escrito. [p=0.4] "
        "{c}Infere-se: [p=0.2] pede uma conclusão. [p=0.2] *Inferir* é tirar uma conclusão que o texto permite, [p=0.2] mesmo sem "
        "escrever com todas as letras. [p=0.4] {d}O autor defende: [p=0.2] pede a tese. [p=0.3] Comandos diferentes, [p=0.2] "
        "respostas diferentes."),

    # ================= QUESTÃO 8 (EU FAÇO) =================
    dict(id="24", block="questao8", text=
        "{t}Agora, eu faço, [p=0.2] com os seis passos. [p=0.4] {a}Passo um, [p=0.2] o comando: [p=0.2] *A tese do texto está expressa em.* "
        "[p=0.3] Ele pede a tese. [p=0.4] {b}Passo dois: [p=0.2] não há título, [p=0.2] e o texto foi feito para a aula. [p=0.3] "
        "{c}Passo três, [p=0.2] a leitura. [p=0.4] {f1}Barulho costuma ser tratado como incômodo menor, [p=0.2] assunto de reclamação "
        "entre vizinhos. [p=0.4] {f2}É um erro de escala. [p=0.4] {c2}Olha a virada! [p=0.2] Erro de escala: [p=0.2] tratar como "
        "pequeno [p=0.2] algo que é grande."),
    dict(id="25", block="questao8", text=
        "{f3}O ruído constante do trânsito e das obras atravessa paredes, [p=0.2] interrompe o sono e eleva o estresse de quem não tem "
        "como se mudar para uma rua mais calma [p=0.2] — em geral, [p=0.2] quem mora perto das grandes avenidas porque ali o aluguel é "
        "mais barato. [p=0.4] {c3}Exemplos do estrago, [p=0.2] e de *quem* sofre mais."),
    dict(id="26", block="questao8", text=
        "{f4}Tratar o barulho como questão de saúde pública, [p=0.2] com medição, fiscalização e planejamento urbano, [p=0.2] é reconhecer "
        "que o silêncio também está mal distribuído. [p=0.4] {c4}A conclusão. [p=0.3] Mal distribuído: [p=0.2] uns têm silêncio, "
        "[p=0.2] outros não. [p=0.4] {d}Passo quatro, [p=0.2] a tese com minhas palavras: [p=0.2] barulho é problema de saúde, "
        "[p=0.2] pesa mais para os mais pobres, [p=0.2] e o governo precisa agir."),
    dict(id="27", block="questao8", text=
        "{t}Só agora, as alternativas. [p=0.4] {a}A: [p=0.2] O ruído urbano é um problema de saúde pública que atinge a população de "
        "forma desigual e exige ação do poder público. [p=0.4] {b}B: [p=0.2] Conflitos entre vizinhos causados por barulho devem ser "
        "resolvidos com diálogo. [p=0.4] {c}C: [p=0.2] Quem mora perto das grandes avenidas deveria se mudar para ruas mais calmas. "
        "[p=0.4] {d}D: [p=0.2] O ruído do trânsito interrompe o sono dos moradores. [p=0.4] {e}E: [p=0.2] O barulho das cidades é "
        "causado principalmente pelas obras da construção civil."),
    dict(id="28", block="questao8", text=
        "{t}Passo cinco: [p=0.2] contradições primeiro. [p=0.4] {c}C: [p=0.2] mandar o morador se mudar? [p=0.2] O texto diz que ele "
        "*não tem como* se mudar. [p=0.2] Roupa do avesso: [p=0.2] *contradição.* [p=0.4] {e}Agora, extrapolação. [p=0.2] E: "
        "[p=0.2] *principalmente* as obras? [p=0.2] O texto põe trânsito e obras lado a lado. [p=0.2] Passou da borda: "
        "[p=0.2] *extrapolação.*"),
    dict(id="29", block="questao8", text=
        "{d}Depois, redução. [p=0.2] D: [p=0.2] o ruído interrompe o sono. [p=0.2] Está no texto, [p=0.2] mas é um efeito só. "
        "[p=0.2] Roupa apertada: [p=0.2] *redução.* [p=0.4] {b}B: [p=0.2] vizinhos e barulho, [p=0.2] as palavras do texto. [p=0.2] "
        "Mas o texto critica justamente tratar o barulho como briga de vizinhos. [p=0.2] *Tema certo, tese errada.* [p=0.4] "
        "{a}Sobra a A, [p=0.2] igual à minha tese. [p=0.3] {ok}*Letra A.*"),

    # ================= QUESTÃO 9 (VOCÊ FAZ) =================
    dict(id="30", block="questao9", text=
        "{t}Agora, você faz. [p=0.3] {a}O comando: [p=0.2] *De acordo com o texto, a principal contribuição das cisternas é.* [p=0.3] "
        "De acordo com o texto: [p=0.2] vale o que está escrito. [p=0.4] {b}Cisterna é um tanque que guarda a água da chuva. [p=0.4] "
        "{f1}A cisterna ao lado da casa mudou menos a paisagem do semiárido do que a rotina de quem vive nele. [p=0.4] {c1}Semiárido: "
        "[p=0.2] a região seca do interior do Nordeste. [p=0.3] {c1b}E repare: [p=0.2] mudou *menos* a paisagem [p=0.2] do que a rotina."),
    dict(id="31", block="questao9", text=
        "{f2}A água da chuva, guardada no período chuvoso, [p=0.2] passa a estar a poucos passos da cozinha nos meses secos, [p=0.2] "
        "e a longa caminhada até o açude [p=0.2] — tarefa que costumava recair sobre mulheres e crianças — [p=0.2] deixa de ser diária. "
        "[p=0.4] {c2}Açude é um grande reservatório de água. [p=0.3] A caminhada *deixa de ser diária.* [p=0.4] {f3}A tecnologia é simples; "
        "[p=0.2] o que ela devolve é tempo: [p=0.2] para a escola, para o trabalho, para o descanso. [p=0.4] {c3}A conclusão: "
        "[p=0.2] *tempo.*"),
    dict(id="32", block="questao9", text=
        "{t}As alternativas. [p=0.3] {a}A: [p=0.2] reduzir as doenças ligadas ao consumo de água contaminada. [p=0.4] {b}B: [p=0.2] "
        "transformar a paisagem do semiárido. [p=0.4] {c}C: [p=0.2] liberar tempo, sobretudo de mulheres e crianças, antes gasto na "
        "busca de água. [p=0.4] {d}D: [p=0.2] substituir os açudes como fonte de água da região. [p=0.4] {e}E: [p=0.2] acabar com os "
        "efeitos da seca no semiárido. [p=0.5] {p}*Pause o vídeo.* [p=0.2] Ache a certa, [p=0.2] e dê o nome da armadilha de cada "
        "errada. [p=1.5]"),
    dict(id="33", block="questao9", text=
        "{t}Vamos conferir. [p=0.3] {b}B: [p=0.2] transformar a paisagem? [p=0.2] A primeira frase diz que mudou *menos* a paisagem. "
        "[p=0.2] *Contradição.* [p=0.4] {d}D: [p=0.2] substituir os açudes? [p=0.2] O texto diz que a caminhada deixa de ser diária, "
        "[p=0.2] não que o açude perde a função. [p=0.2] *Extrapolação.* [p=0.4] {e}E: [p=0.2] acabar com a seca? [p=0.2] Muito além do "
        "texto. [p=0.2] *Extrapolação* de novo."),
    dict(id="34", block="questao9", text=
        "{a}E a A, [p=0.2] a mais traiçoeira. [p=0.3] Cisterna bem cuidada pode mesmo reduzir doenças. [p=0.3] Mas em que linha isso está? "
        "[p=0.3] Em nenhuma. [p=0.2] *Verdade do mundo.* [p=0.4] {c}Sobra a C: [p=0.2] o tempo, [p=0.2] que antes ia na caminhada "
        "de mulheres e crianças. [p=0.3] {ok}*Letra C.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="35", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] a certa cobre o texto: [p=0.2] nem menos, [p=0.2] nem mais, "
        "[p=0.2] nem o contrário. [p=0.5] {b}Dois: [p=0.2] diz isso? [p=0.2] Diz só isso? [p=0.2] Diz isso tudo? [p=0.5] {c}Três: "
        "[p=0.2] em que linha isso está?"),

    # ================= PONTE =================
    dict(id="36", block="ponte", text=
        "{t}Você já tem o método. [p=0.3] {a}Mas onde, exatamente, a tese fica no texto? [p=0.4] {b}No começo, [p=0.2] no fim, "
        "[p=0.2] ou em lugar nenhum? [p=0.4] {c}Próximo episódio: [p=0.2] *onde a tese se esconde.*"),
    dict(id="37", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *Linguagens do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantas armadilhas da questão das cisternas você acertou? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
