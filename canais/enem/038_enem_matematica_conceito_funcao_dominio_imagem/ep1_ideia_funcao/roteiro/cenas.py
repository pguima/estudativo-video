# Roteiro — Conceito de Função, Domínio e Imagem, Episódio 1 de 6: a ideia de função (quando é e quando não é)
# Base: Estudos/Enem/estudos/01-matematica/23-conceito-funcao-dominio-imagem.html — seções 02 e 03 + Questões 6 e 1 (seção 12).
# PRIMEIRO episódio do bloco de Funções (dito na abertura, cena 02).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A MÁQUINA: entra um número, sai um número, e a mesma entrada dá SEMPRE a mesma saída (o 10 entra três vezes, sai 60).
#   A DATA DE NASCIMENTO: cada pessoa tem UMA só, mas muitas pessoas fazem aniversário no mesmo dia
#     (duas flechas chegando pode; duas saindo, não).
#   A PERGUNTA MÁGICA: "se eu souber ISTO, consigo dizer AQUILO sem dúvida?".
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Diagramas da seção 03 (iguais ao material): A = {1, 2, 3}, B = {a, b, c}.
#   1º: 1→a, 2→a, 3→b (É função) · 2º: 1→a, 2→b, 3 sem flecha (não é) · 3º: 1→a, 2→b e 2→c, 3→c (não é).
# Nós fazemos (prompt): tabela 1→3, 2→5, 2→6, 3→7 → não é função (o 2 tem duas saídas, 5 e 6).
# QUESTÃO 6 ("eu faço", com pausa): gabarito A (o aluno cuja altura é x). Explicações das erradas = material.
# QUESTÃO 1 ("você faz", com pausa): gabarito C (I e III). Explicações das erradas = material (A descarta III sem motivo;
#   B e D aceitam II, confundindo flechas chegando com flechas saindo; E ignora os professores com duas disciplinas).
# Acréscimos NOSSOS: atalho verde "a pergunta mágica" (cena 09) e atalho verde "na tabela, cace o x repetido" (cena 15).
# Frases-chave (meio e fim, idênticas): 1. Função: a cada entrada, uma única saída.
#   2. Duas flechas chegando pode; duas flechas saindo, não. 3. Todo elemento do conjunto de partida precisa de flecha.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Função do zero: quando é e quando NÃO é | Funções Ep. 1"
# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de matemática: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína, como quem prepara "
            "uma revelação; mostre surpresa nas armadilhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, fale devagar e com clareza, número por número. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Abastecer *dez litros* a *seis reais* o litro [p=0.2] custa *sessenta reais.* [p=0.3] *Sempre.* [p=0.5] "
        "{b}Se a bomba às vezes cobrasse sessenta [p=0.2] e às vezes setenta [p=0.2] pelos mesmos dez litros, [p=0.3] "
        "você brigaria com o frentista. [p=0.5] {c}Essa sua revolta tem nome em matemática: [p=0.3] *função.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o *primeiro episódio* do bloco de *Funções.* [p=0.4] {a}Ao final desta aula, [p=0.2] você vai saber "
        "dizer, [p=0.2] olhando um texto, [p=0.2] uma tabela [p=0.2] ou um diagrama de flechas, [p=0.3] {b}se aquilo é "
        "ou não é uma função, [p=0.3] {c}e quem depende de quem."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Um *conjunto* é só uma lista de elementos [p=0.2] entre chaves. "
        "[p=0.4] {b}E, da série de Expressões algébricas: [p=0.2] "
        "*substituir* um número numa fórmula. [p=0.2] Seis vezes L, "
        "com L igual a dez: [p=0.2] *sessenta.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Olhe três coisas do dia a dia. [p=0.3] {a}A *bomba de combustível:* [p=0.2] você escolhe os litros, "
        "[p=0.2] a bomba mostra o valor. [p=0.4] {b}O *taxímetro:* [p=0.2] o carro anda, [p=0.2] o preço sobe. "
        "[p=0.4] {c}A *chamada da escola:* [p=0.2] cada número da lista [p=0.2] corresponde a um aluno. [p=0.4] "
        "{d}Nas três, [p=0.2] uma coisa *entra* [p=0.2] e outra *sai.*"),

    # ================= BLOCO A: A MÁQUINA =================
    dict(id="05", block="maquina", text=
        "{t}O que faz a bomba ser confiável? [p=0.4] {a}Pense numa *máquina.* [p=0.2] Entra um número, [p=0.2] sai "
        "um número. [p=0.4] {b}Coloque o *dez:* [p=0.2] sai *sessenta.* [p=0.3] De novo: [p=0.2] "
        "sessenta. [p=0.2] De novo: [p=0.2] sessenta. [p=0.4] {c}A mesma entrada [p=0.2] dá *sempre* a mesma saída. "
        "[p=0.3] Isso é uma *função.*"),
    dict(id="06", block="definicao", text=
        "{t}Agora, com nome. [p=0.3] {a}Uma *função* é uma *regra* [p=0.2] que pega cada elemento de um conjunto *A* "
        "[p=0.2] e associa a ele *um único* elemento de um conjunto *B.* [p=0.4] {b}O conjunto A é o *conjunto de "
        "partida:* [p=0.2] de onde saem as entradas. [p=0.2] O B é o *conjunto de chegada:* [p=0.2] onde ficam as "
        "saídas. [p=0.4] {c}A gente escreve assim: [p=0.2] *f, de A em B.* [p=0.3] A palavra que manda: [p=0.2] *único.*"),

    # ================= BLOCO B: INDEPENDENTE E DEPENDENTE =================
    dict(id="07", block="variaveis", text=
        "{t}Quem escolhe e quem é calculado? [p=0.4] {a}A entrada se chama *variável independente:* [p=0.2] é o *x,* "
        "[p=0.2] você escolhe. [p=0.3] A saída é a *variável dependente:* [p=0.2] o *y,* [p=0.2] calculado a partir "
        "do x. [p=0.4] {b}A fórmula que liga os dois [p=0.2] é a *lei da função.* [p=0.4] {c}No táxi, [p=0.2] entra a "
        "*distância,* [p=0.2] sai o *preço.* [p=0.2] No quadrado, [p=0.2] entra o *lado,* [p=0.2] sai a *área.* "
        "[p=0.3] {d}Na bola jogada para cima, "
        "[p=0.2] entra o *tempo,* [p=0.2] sai a *altura.*"),

    # ================= BLOCO C: QUEM DEPENDE DE QUEM =================
    dict(id="08", block="depende", text=
        "{t}E como saber quem depende de quem? [p=0.4] {a}Sabendo o *lado* de um quadrado, [p=0.2] você sabe a área? "
        "[p=0.3] Sabe. [p=0.2] Lado três, [p=0.2] área nove. [p=0.3] A área é *função* do lado. "
        "[p=0.5] {b}Agora: [p=0.2] sabendo a *altura* de um aluno, [p=0.2] você sabe *qual* é o aluno? [p=0.4] {c}Não. "
        "[p=0.2] Dois alunos podem ter um metro e setenta. [p=0.3] O aluno *não é* função da altura."),
    dict(id="09", block="magica", text=
        "{t}Guarde a ferramenta. [p=0.3] {a}A *pergunta mágica:* [p=0.3] *se eu souber isto, [p=0.2] consigo dizer "
        "aquilo sem dúvida?* [p=0.5] {b}Se a resposta é *sim,* [p=0.2] é função. [p=0.3] {c}Se pode dar *duas "
        "respostas,* [p=0.2] não é."),

    # ================= BLOCO D: O DIAGRAMA DE FLECHAS =================
    dict(id="10", block="flechas", text=
        "{t}E como desenhar uma função? [p=0.4] {a}Com um *diagrama de flechas:* [p=0.2] o conjunto A de um lado, "
        "[p=0.2] o B do outro, [p=0.2] e uma flecha de cada entrada [p=0.2] até a sua saída. [p=0.4] {b}Duas regras. [p=0.3] Primeira: [p=0.2] *todo* elemento de A tem flecha saindo. [p=0.3] "
        "{c}Segunda: [p=0.2] de cada elemento de A [p=0.2] sai *uma só* flecha. [p=0.4] {d}E o B? [p=0.2] *Nenhuma "
        "exigência.* [p=0.2] Pode receber várias flechas, [p=0.2] ou nenhuma."),

    # ================= BLOCO E: OS TRÊS DIAGRAMAS =================
    dict(id="11", block="diagramas", text=
        "{t}Vamos testar três diagramas. [p=0.3] {a}No primeiro: [p=0.2] o um vai para o a, [p=0.2] o dois também vai "
        "para o a, [p=0.2] e o três vai para o b. [p=0.4] {b}Todo mundo tem flecha? [p=0.2] Tem. [p=0.2] Alguém tem "
        "duas? [p=0.2] Não. [p=0.3] {c}*É função,* [p=0.2] mesmo com duas flechas chegando no a."),
    dict(id="12", block="diagramas", text=
        "{t}No segundo: [p=0.2] um para a, [p=0.2] dois para b. [p=0.2] E o três? [p=0.3] {a}Ficou *sem flecha.* "
        "[p=0.3] *Não é função.* [p=0.5] {b}No terceiro: [p=0.2] do *dois* saem *duas* flechas, [p=0.2] uma para o b "
        "[p=0.2] e outra para o c. [p=0.3] {c}Uma entrada com duas saídas. [p=0.3] *Não é função.*"),

    # ================= BLOCO F: DUAS FLECHAS CHEGANDO =================
    dict(id="13", block="chegando", text=
        "{t}Mas duas flechas chegando no mesmo lugar [p=0.2] não estraga nada? [p=0.4] {a}Não estraga. [p=0.3] Na regra "
        "*x ao quadrado,* [p=0.2] o dois vira quatro, [p=0.2] e o *menos dois* também vira quatro. [p=0.4] {b}Cada "
        "entrada continua com *uma* saída. [p=0.4] {c}É como a *data de nascimento:* [p=0.2] cada pessoa tem *uma "
        "só,* [p=0.2] mas muitas pessoas fazem aniversário no mesmo dia. [p=0.4] {d}Duas flechas *chegando:* "
        "[p=0.2] pode. [p=0.2] Duas *saindo:* [p=0.2] não."),

    # ================= BLOCO G: NA TABELA =================
    dict(id="14", block="tabela", text=
        "{t}E quando a prova dá uma *tabela?* [p=0.4] {a}A regra é a mesma: [p=0.2] x são as entradas, "
        "[p=0.2] y as saídas. [p=0.4] {b}O que *não* pode: [p=0.2] o *mesmo x* aparecer em duas linhas [p=0.2] "
        "com *y diferentes.* [p=0.4] {c}O mesmo y em duas linhas? [p=0.2] Tudo bem: [p=0.2] flechas chegando."),
    dict(id="15", block="atalho", text=
        "{t}E como olhar uma tabela rápido? [p=0.3] {a}Atalho: [p=0.2] *cace o x repetido.* [p=0.4] {b}Passe o dedo só "
        "na coluna do x. [p=0.2] Nenhum repetido? [p=0.2] É função. [p=0.4] "
        "{c}Achou um repetido? [p=0.2] Olhe os dois y. [p=0.2] Se forem *diferentes,* [p=0.2] não é."),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Esta tabela: [p=0.2] x igual a um, [p=0.2] y igual a três. [p=0.2] x igual a dois, "
        "[p=0.2] y igual a cinco. [p=0.2] x igual a dois, [p=0.2] y igual a seis. [p=0.2] x igual a três, [p=0.2] y "
        "igual a sete. [p=0.4] {b}Ela representa uma função? [p=0.3] {c}*Pause e tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Caçando o x repetido: [p=0.2] um, [p=0.2] dois, [p=0.2] *dois de novo.* [p=0.4] "
        "{b}E os y do dois? [p=0.2] *Cinco* e *seis.* [p=0.2] Diferentes. [p=0.4] {c}O dois tem *duas saídas.* "
        "[p=0.3] *Não é função.* "),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] função: a cada entrada, uma única saída. [p=0.5] "
        "{b}Dois: [p=0.2] duas flechas chegando pode; [p=0.2] duas flechas saindo, não. [p=0.5] {c}Três: [p=0.2] todo "
        "elemento do conjunto de partida precisa de flecha."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que *duas flechas chegando* no mesmo y "
        "[p=0.2] impedem a função. [p=0.4] {b}Parece certo, [p=0.2] porque a palavra *único* fica martelando. "
        "[p=0.4] {c}Mas o único é a saída de *cada entrada.* [p=0.2] Duas entradas com a mesma saída: [p=0.2] "
        "*pode.*"),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] achar que tudo bem um elemento de A [p=0.2] ficar *sem flecha.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque ninguém ficou com duas saídas. [p=0.4] {c}Mas a regra pede *todo* elemento do conjunto de "
        "partida com flecha. [p=0.2] Um sem flecha: [p=0.2] *não é função.*"),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] *inverter* quem depende de quem, [p=0.2] e dizer que o aluno é função da altura. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque cada aluno *tem* uma altura. [p=0.4] {c}Mas isso diz que a *altura* é "
        "função do aluno. [p=0.2] O contrário, não. [p=0.2] Pergunta mágica *na ordem certa.*"),

    # ================= QUESTÃO 6 (EU FAÇO) =================
    dict(id="22", block="q6", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] Esta, [p=0.2] eu resolvo com você. "
        "[p=0.4] {a}Em uma turma, [p=0.2] há alunos com a mesma altura. [p=0.2] Em qual das situações [p=0.2] a "
        "grandeza y *não* é função da grandeza x? [p=0.4] {qa}A: [p=0.2] y é o aluno da turma cuja altura é x "
        "centímetros. [p=0.3] {qb}B: [p=0.2] y é a área de um quadrado de lado x centímetros. [p=0.3] {qc}C: [p=0.2] y "
        "é o preço pago por x quilogramas de arroz. [p=0.3] {qd}D: [p=0.2] y é a temperatura registrada no instante x. "
        "[p=0.3] {qe}E: [p=0.2] y é o perímetro de um quadrado de lado x centímetros. [p=0.5] {p}*Pause o vídeo e "
        "tente.* [p=2.0]"),
    dict(id="23", block="q6", text=
        "{t}Pergunta mágica em cada uma. [p=0.4] {a}Na A: [p=0.2] sabendo a "
        "*altura,* [p=0.2] eu digo *qual aluno* sem dúvida? [p=0.3] Não: [p=0.2] a turma tem alunos com a mesma "
        "altura. [p=0.4] {b}Uma entrada, [p=0.2] duas saídas. [p=0.3] {ok}*Letra A!*"),
    dict(id="24", block="q6", text=
        "{t}E as outras? [p=0.3] {xb}Na B, [p=0.2] o lado determina a área: [p=0.2] x vezes x. [p=0.3] {xe}Na E, "
        "[p=0.2] o lado determina o perímetro: [p=0.2] quatro vezes x. [p=0.3] {xc}Na C, [p=0.2] a quantidade de arroz "
        "determina o preço. [p=0.4] {xd}E na D, [p=0.2] o instante determina a temperatura registrada. [p=0.3] {a}A "
        "mesma temperatura em instantes diferentes? [p=0.2] Flechas *chegando:* [p=0.2] *pode.*"),

    # ================= QUESTÃO 1 (VOCÊ FAZ) =================
    dict(id="25", block="q1", text=
        "{t}E esta é *sua.* [p=0.3] {a}A secretaria de uma escola analisou três relações. [p=0.3] Um: [p=0.2] cada "
        "aluno matriculado associado à sua *data de nascimento.* [p=0.3] Dois: [p=0.2] cada professor associado às "
        "*disciplinas* que leciona, [p=0.2] sabendo que alguns lecionam duas. [p=0.3] Três: [p=0.2] cada *número da "
        "lista de chamada* associado ao aluno que tem esse número. [p=0.4] {b}Considerando o primeiro conjunto como "
        "domínio, [p=0.2] o de partida, [p=0.2] são funções: [p=0.3] {qa}A: [p=0.2] "
        "apenas um. [p=0.2] {qb}B: [p=0.2] apenas dois. [p=0.2] {qc}C: [p=0.2] um e três. [p=0.2] {qd}D: [p=0.2] dois e "
        "três. [p=0.2] {qe}E: [p=0.2] um, dois e três. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="26", block="q1", text=
        "{t}Conferindo. [p=0.3] {a}Na um, [p=0.2] o conjunto de partida são os *alunos.* [p=0.2] "
        "Cada aluno tem *uma só* data de nascimento. [p=0.2] *É função.* [p=0.4] {b}Na dois, [p=0.2] partida são os *professores.* [p=0.2] Um professor com duas "
        "disciplinas [p=0.2] tem *duas flechas saindo:* [p=0.2] *não é.* [p=0.4] {c}Na três, [p=0.2] partida são os "
        "*números da chamada.* [p=0.2] Cada número, [p=0.2] um aluno: [p=0.2] *é função.* [p=0.4] {ok}Um e três: "
        "[p=0.2] *letra C!*"),
    dict(id="27", block="q1", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A descarta a três [p=0.2] sem motivo nenhum. [p=0.4] {xb}A B [p=0.2] {xd}e a "
        "D [p=0.2] aceitam a dois: [p=0.2] confundem flechas *chegando,* [p=0.2] que pode, [p=0.2] com flechas "
        "*saindo,* [p=0.2] que não pode. [p=0.4] {xe}E a E ignora os professores com duas disciplinas."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] função: a cada entrada, uma única saída. "
        "[p=0.5] {b}Dois: [p=0.2] duas flechas chegando pode; [p=0.2] duas flechas saindo, não. [p=0.5] {c}Três: "
        "[p=0.2] todo elemento do conjunto de partida precisa de flecha."),

    # ================= PONTE E CTA =================
    dict(id="29", block="ponte", text=
        "{a}Se a função *x ao quadrado* [p=0.2] recebe só os números *um, dois e três,* [p=0.3] {b}e pode devolver "
        "*um, quatro, sete ou nove,* [p=0.3] o *sete* sai alguma vez? [p=0.5] {c}Quem nunca sai tem nome. [p=0.4] "
        "{d}Próximo episódio: [p=0.2] domínio, [p=0.2] contradomínio [p=0.2] e imagem."),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] que máquina do seu dia a dia é uma função? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
