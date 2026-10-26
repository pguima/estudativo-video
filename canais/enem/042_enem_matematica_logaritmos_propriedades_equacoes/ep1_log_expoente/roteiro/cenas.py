# Roteiro — Logaritmos, Episódio 1 de 5: logaritmo é um expoente (definição, condições e consequências)
# Base: Estudos/Enem/estudos/01-matematica/27-logaritmos-propriedades-equacoes.html — seções 02 e 03 + Questão 4.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A PERGUNTA: log_b a quer saber "b elevado a quanto dá a?" — todo log é lido em voz alta como pergunta.
#   O EXPOENTE COM NOME PRÓPRIO: o logaritmo é só um expoente que ganhou nome.
#   O LOG DECIMAL CONTA ZEROS: log 1 000 = 3, log 0,01 = −2 (régua de potências de 10).
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Propriedades operatórias: só no episódio 2 (na Q4, "o expoente desce multiplicando" entra como aviso, como o prompt pede).
# Ordem: o bloco d (notações: log sem base = decimal; ln só citado) entra NO MEIO da tabela da seção 02, logo antes de
#   log 1 000 e log 0,01, para que a pessoa saiba qual é a base quando ela não está escrita.
# DESVIOS DO PROMPT (para não entregar a Questão 4, que tem "pause o vídeo e tente"):
#   - bloco g: o exemplo "entre 10³⁰ e 10³¹ → 31 algarismos" (que é exatamente a conta da Q4) virou um exemplo NOSSO:
#     um número entre 10⁷ e 10⁸ (25 000 000) tem log entre 7 e 8 e 8 algarismos;
#   - erro 2: "2¹⁰⁰ tem 30 algarismos" virou um exemplo NOSSO com o mesmo raciocínio: 2³⁰ = 1 073 741 824 tem log
#     30 · 0,301 ≈ 9,03 e 10 algarismos, não 9. A Q4 continua sendo resolvida só depois da pausa.
# Nós fazemos (prompt): log_5 125 = 3 · log 0,0001 = −4.
# Erros (prompt): log 0 = 0 (log 0 não existe; quem vale zero é log 1) · parte inteira do log sem somar 1 (2³⁰, acima).
# QUESTÃO 4 ("nós fazemos", com pausa): gabarito B (31). Erradas = material e prompt (A 30 esquece o +1; C 100 confunde
#   algarismos com o expoente; D 101 soma 1 ao expoente; E 200 multiplica a base pelo expoente). Caso pequeno antes:
#   10³ = 1 000 tem log 3 e 4 algarismos.
# Acréscimos NOSSOS (marcados): três cenas verdes de ATALHO — "o log decimal conta zeros" (cena 10: 1 seguido de n zeros
#   → n; n casas decimais até o 1 → −n), "o número já é potência da base? o log é o expoente" (cena 15) e
#   "algarismos = parte inteira + 1" com 4 500 (cena 18). A definição de "parte inteira" (o número antes da vírgula).
# Frases-chave (meio e fim, idênticas): 1. Logaritmo é expoente: log_b a pergunta "b elevado a quanto dá a?".
#   2. O logaritmando é sempre positivo; o logaritmo pode ser negativo.  3. Algarismos = parte inteira do log + 1.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Logaritmo do zero: o expoente com nome próprio e como contar algarismos | Logaritmos Ep. 1"
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
        "{a}Quantos algarismos tem *dois elevado a cem?* [p=0.5] {b}Ninguém faz essa conta na mão. [p=0.5] {c}Mas com um "
        "único número, [p=0.2] *log de dois,* [p=0.2] aproximadamente *zero vírgula trezentos e um,* [p=0.3] você "
        "responde em *dez segundos.* [p=0.5] {d}Ao final desta aula, [p=0.2] *você também.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o primeiro episódio da série de *Logaritmos.* [p=0.4] {a}Ao final, [p=0.2] você vai *ler qualquer "
        "logaritmo como uma pergunta,* [p=0.3] {b}saber *quando ele existe* [p=0.3] {c}e usar o log para *contar "
        "algarismos.*"),
    dict(id="03", block="prereq", text=
        "{t}Quatro lembretes rápidos, da série de Potenciação. [p=0.3] {a}Dois elevado a cinco [p=0.2] é *trinta e dois.* "
        "[p=0.3] {b}Três elevado a menos dois [p=0.2] *inverte:* [p=0.2] *um nono.* [p=0.3] {c}Expoente *um meio* [p=0.2] "
        "é raiz quadrada: [p=0.2] nove elevado a um meio [p=0.2] é *três.* [p=0.3] {d}E qualquer base elevada a zero "
        "[p=0.2] dá *um.*"),
    dict(id="04", block="prereq10", text=
        "{t}E, da série de Notação científica: [p=0.3] {a}dez elevado a n [p=0.2] é *um seguido de n zeros.* [p=0.4] "
        "{b}E dez elevado a menos n [p=0.2] tem *n casas decimais:* [p=0.2] dez elevado a menos dois [p=0.2] é *zero "
        "vírgula zero um.*"),

    # ================= BLOCO A: A PERGUNTA ABERTA =================
    dict(id="05", block="aberta", text=
        "{t}Na série de Função exponencial, [p=0.2] ficou uma pergunta no ar: [p=0.3] *dois elevado a quanto dá dez?* "
        "[p=0.5] {a}Dois ao cubo [p=0.2] é *oito.* [p=0.2] Pouco. [p=0.4] {b}Dois à quarta [p=0.2] é *dezesseis.* "
        "[p=0.2] Passou. [p=0.4] {c}A resposta está *entre três e quatro.* [p=0.3] Não é um número inteiro. [p=0.4] "
        "{d}Mas esse número *existe,* [p=0.2] e tem nome: [p=0.2] *logaritmo.*"),

    # ================= BLOCO B: DEFINIÇÃO =================
    dict(id="06", block="definicao", text=
        "{t}Então, o que é um logaritmo? [p=0.4] {a}*Logaritmo é o expoente que falta.* [p=0.4] {b}Log de a na base b "
        "[p=0.2] igual a x [p=0.2] quer dizer: [p=0.2] *b elevado a x dá a.* [p=0.4] {c}O *b* é a *base:* [p=0.2] o "
        "número que vai ser elevado. [p=0.3] {d}O *a* é o *logaritmando:* [p=0.2] o número que você quer alcançar. "
        "[p=0.3] {e}E o *x* é o *logaritmo:* [p=0.2] o expoente que leva até lá."),
    dict(id="07", block="pergunta", text=
        "{t}O jeito de nunca errar: [p=0.2] *leia todo log como uma pergunta.* [p=0.4] {a}Log de trinta e dois na base "
        "dois [p=0.2] pergunta: [p=0.2] *dois elevado a quanto dá trinta e dois?* [p=0.4] {b}Vamos multiplicar: "
        "[p=0.2] dois, quatro, oito, dezesseis, *trinta e dois.* [p=0.4] {c}Foram *cinco* dois. [p=0.2] O log vale "
        "*cinco.* [p=0.4] {d}Ida e volta: [p=0.2] log é cinco [p=0.2] porque dois elevado a cinco dá trinta e dois. "
        "[p=0.3] O logaritmo é só *um expoente com nome próprio.*"),

    # ================= BLOCO C: A TABELA =================
    dict(id="08", block="tabela", text=
        "{t}E quando a resposta é *negativa* ou *fração?* [p=0.4] {a}Log de um nono na base três: [p=0.2] *três elevado "
        "a quanto dá um nono?* [p=0.3] Um nono é uma base *invertida:* [p=0.2] *menos dois.* [p=0.4] {b}Log de três na "
        "base nove: [p=0.2] *nove elevado a quanto dá três?* [p=0.3] Três é a *raiz* de nove: [p=0.2] *um meio.*"),

    # ================= BLOCO D: NOTAÇÕES =================
    dict(id="09", block="notacao", text=
        "{t}E quando a base *nem aparece?* [p=0.4] {a}Log sem base escrita [p=0.2] é o *logaritmo decimal:* [p=0.2] "
        "base *dez.* [p=0.3] É o mais usado na prova. [p=0.4] {b}Log de mil: [p=0.2] *dez elevado a quanto dá mil?* "
        "[p=0.2] *Três.* [p=0.4] {c}Log de zero vírgula zero um: [p=0.2] *dez elevado a quanto dá um centésimo?* [p=0.2] "
        "*Menos dois.* [p=0.4] {d}Você ainda vai ver o *ln,* [p=0.2] o *logaritmo natural,* [p=0.2] de base e, [p=0.2] "
        "um número perto de dois vírgula setecentos e dezoito. [p=0.3] Por enquanto, [p=0.2] *só o nome.*"),
    dict(id="10", block="atalho_zeros", text=
        "{t}Atalho: [p=0.2] o log decimal *conta zeros.* [p=0.4] {a}Um seguido de cinco zeros? [p=0.2] Log *cinco.* "
        "[p=0.4] {b}Número com três casas decimais, [p=0.2] terminando no um? [p=0.2] Log *menos três.* [p=0.4] {c}Na "
        "régua: [p=0.2] cada passo para a direita [p=0.2] *multiplica por dez* [p=0.2] e *soma um* no log."),

    # ================= BLOCO E: CONDIÇÕES DE EXISTÊNCIA =================
    dict(id="11", block="existe", text=
        "{t}Todo logaritmo *existe?* [p=0.4] {a}Não. [p=0.2] A *condição de existência* [p=0.2] é a regra que diz "
        "*quando* o log existe. [p=0.4] {b}Primeira: [p=0.2] o *logaritmando é positivo.* [p=0.4] {c}Por quê? [p=0.2] "
        "Base positiva elevada a qualquer expoente [p=0.2] dá *positivo.* [p=0.3] Não existe dez elevado a x [p=0.2] "
        "igual a *zero,* [p=0.2] nem igual a *menos cinco.* [p=0.4] {d}Então *log de zero* [p=0.2] e *log de menos "
        "cinco* [p=0.2] *não existem.*"),
    dict(id="12", block="existe2", text=
        "{t}E a base? [p=0.4] {a}Precisa ser *positiva* [p=0.2] e *diferente de um.* [p=0.4] {b}Com base um, [p=0.2] um "
        "elevado a qualquer coisa [p=0.2] *dá um:* [p=0.2] a pergunta não tem resposta. [p=0.4] {c}Agora, atenção: "
        "[p=0.2] o *logaritmo,* [p=0.2] a resposta, [p=0.2] *pode* ser negativo. [p=0.4] Log de zero vírgula zero um "
        "[p=0.2] é *menos dois.* [p=0.3] {d}Positivo é o número *de dentro.*"),

    # ================= BLOCO F: CONSEQUÊNCIAS =================
    dict(id="13", block="conseq", text=
        "{t}Da definição saem *cinco consequências.* [p=0.4] {a}Log de um, [p=0.2] em qualquer base, [p=0.2] é *zero:* "
        "[p=0.2] toda base elevada a zero dá um. [p=0.4] {b}Log da própria base [p=0.2] é *um:* [p=0.2] log de dez é um. "
        "[p=0.4] {c}E log de uma *potência da base* [p=0.2] é o *expoente:* [p=0.2] log de dez elevado a menos sete "
        "[p=0.2] é *menos sete.*"),
    dict(id="14", block="conseq2", text=
        "{t}As outras duas. [p=0.4] {a}Dez elevado a log de sete [p=0.2] é *sete:* [p=0.2] você eleva a base ao "
        "expoente que *dá sete.* [p=0.4] {b}E se log de x [p=0.2] é igual a log de cinco, [p=0.2] então *x é cinco:* "
        "[p=0.2] expoentes iguais, [p=0.2] potências iguais."),
    dict(id="15", block="atalho_pot", text=
        "{t}Atalho: [p=0.2] o número *já é potência da base?* [p=0.4] {a}Então o log é *o expoente.* [p=0.3] Sem conta. "
        "[p=0.4] {b}Log de dois elevado a nove, [p=0.2] na base dois: [p=0.2] *nove.* [p=0.4] {c}Log de cem, [p=0.2] que "
        "é dez ao quadrado: [p=0.2] *dois.*"),

    # ================= BLOCO G: CONTAR ALGARISMOS =================
    dict(id="16", block="algarismos", text=
        "{t}E como o log *conta algarismos?* [p=0.4] {a}*Algarismo* [p=0.2] é cada símbolo de zero a nove [p=0.2] usado "
        "para escrever um número. [p=0.4] {b}Dez tem log *um,* [p=0.2] e *dois* algarismos. [p=0.3] Cem tem log *dois,* "
        "[p=0.2] e *três.* [p=0.3] Mil tem log *três,* [p=0.2] e *quatro.* [p=0.4] {c}O número de algarismos [p=0.2] é "
        "sempre *um a mais* que o log."),
    dict(id="17", block="algarismos2", text=
        "{t}E um número *entre* duas potências de dez? [p=0.4] {a}Vinte e cinco milhões [p=0.2] fica entre dez elevado a "
        "sete [p=0.2] e dez elevado a oito. [p=0.4] {b}O log dele [p=0.2] fica *entre sete e oito:* [p=0.2] sete "
        "vírgula alguma coisa. [p=0.4] {c}A *parte inteira* é o número antes da vírgula: [p=0.2] *sete.* [p=0.3] "
        "{d}Sete mais um: [p=0.2] *oito algarismos.*"),
    dict(id="18", block="atalho_alg", text=
        "{t}Atalho para contar algarismos. [p=0.4] {a}Ache o log. [p=0.3] {b}Pegue a *parte inteira.* [p=0.3] {c}*Some "
        "um.* [p=0.4] {d}Quatro mil e quinhentos: [p=0.2] log entre três e quatro, [p=0.2] três vírgula alguma coisa. "
        "[p=0.3] Três mais um: [p=0.2] *quatro algarismos.* [p=0.3] Confira: [p=0.2] quatro, cinco, zero, zero."),

    # ================= NÓS FAZEMOS =================
    dict(id="19", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Quanto vale *log de cento e vinte e cinco na base cinco?* [p=0.4] {b}E *log de zero "
        "vírgula zero zero zero um?* [p=0.4] {c}Leia como pergunta. [p=0.3] *Pause e tente.* [p=2.0]"),
    dict(id="20", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Cinco elevado a quanto dá cento e vinte e cinco? [p=0.3] Cinco, vinte e cinco, "
        "cento e vinte e cinco: [p=0.2] *três* cincos. [p=0.2] Log *três.* [p=0.4] {b}Dez elevado a quanto dá zero "
        "vírgula zero zero zero um? [p=0.3] São *quatro* casas decimais: [p=0.2] log *menos quatro.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="21", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] logaritmo é expoente: [p=0.2] log de a na base b "
        "[p=0.2] pergunta: [p=0.2] b elevado a quanto dá a? [p=0.5] {b}Dois: [p=0.2] o logaritmando é sempre positivo; "
        "[p=0.2] o logaritmo pode ser negativo. [p=0.5] {c}Três: [p=0.2] algarismos: [p=0.2] parte inteira do log, "
        "[p=0.2] mais um."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="22", block="erros", text=
        "{t}Agora, os dois erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] dizer que *log de zero é zero.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque com o zero [p=0.2] quase tudo dá zero: [p=0.2] zero vezes cinco, [p=0.2] raiz "
        "de zero. [p=0.4] "
        "{c}Mas dez elevado a quanto dá zero? [p=0.2] *Nenhum* expoente. [p=0.2] Log de zero *não existe.* [p=0.3] Quem "
        "vale zero é *log de um.*"),
    dict(id="23", block="erros", text=
        "{a}Segundo: [p=0.2] dois elevado a trinta [p=0.2] tem log de trinta vezes zero vírgula trezentos e um, [p=0.2] "
        "nove vírgula zero três. [p=0.3] E alguém responde: [p=0.2] *nove algarismos.* [p=0.4] {b}Parece certo, [p=0.2] "
        "porque o nove *está ali,* [p=0.2] na frente da vírgula. [p=0.4] {c}Mas faltou somar um. [p=0.2] Dois elevado a "
        "trinta [p=0.2] é *um bilhão e setenta e três milhões e pouco:* [p=0.2] *dez* algarismos."),

    # ================= QUESTÃO 4 (NÓS FAZEMOS) =================
    dict(id="24", block="q4", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] Esta, [p=0.2] a gente resolve *junto.* [p=0.4] {a}Um professor "
        "desafiou a turma [p=0.2] a descobrir quantos algarismos tem o número *dois elevado a cem,* [p=0.2] escrito no "
        "sistema decimal, [p=0.2] sem calculá-lo. [p=0.3] Dado que log de dois [p=0.2] é aproximadamente zero vírgula "
        "trezentos e um, [p=0.2] a resposta correta é: [p=0.3] {qa}A: [p=0.2] trinta. [p=0.2] {qb}B: [p=0.2] trinta e "
        "um. [p=0.2] {qc}C: [p=0.2] cem. [p=0.2] {qd}D: [p=0.2] cento e um. [p=0.2] {qe}E: [p=0.2] duzentos. [p=0.5] "
        "{p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="25", block="q4", text=
        "{t}Vamos juntos. [p=0.3] {a}Primeiro, o caso pequeno: [p=0.2] dez ao cubo, [p=0.2] *mil,* [p=0.2] tem log três "
        "[p=0.2] e *quatro* algarismos. [p=0.4] {b}Agora, o log de dois elevado a cem. [p=0.3] O expoente *desce "
        "multiplicando:* [p=0.2] cem vezes zero vírgula trezentos e um, [p=0.2] *trinta vírgula um.* [p=0.3] Isso é do "
        "próximo episódio: [p=0.2] *confie por enquanto.* [p=0.4] {c}Então dois elevado a cem [p=0.2] fica entre dez "
        "elevado a trinta [p=0.2] e dez elevado a trinta e um. [p=0.4] {d}Parte inteira, *trinta.* [p=0.2] Mais um: "
        "[p=0.2] *trinta e um algarismos.* [p=0.3] {ok}*Letra B!*"),
    dict(id="26", block="q4", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A pega a parte inteira [p=0.2] e *esquece de somar um.* [p=0.4] {xc}A C "
        "confunde o número de algarismos [p=0.2] com o *expoente,* [p=0.2] cem. [p=0.4] {xd}A D soma um [p=0.2] a esse "
        "expoente. [p=0.4] {xe}E a E *multiplica a base pelo expoente:* [p=0.2] dois vezes cem."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="27", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] logaritmo é expoente: [p=0.2] log de a na base b "
        "[p=0.2] pergunta: [p=0.2] b elevado a quanto dá a? [p=0.5] {b}Dois: [p=0.2] o logaritmando é sempre positivo; "
        "[p=0.2] o logaritmo pode ser negativo. [p=0.5] {c}Três: [p=0.2] algarismos: [p=0.2] parte inteira do log, "
        "[p=0.2] mais um."),

    # ================= PONTE E CTA =================
    dict(id="28", block="ponte", text=
        "{a}Se log de dois [p=0.2] é aproximadamente *zero vírgula trinta* [p=0.2] e log de três, [p=0.2] *zero vírgula "
        "quarenta e oito,* [p=0.3] {b}quanto vale *log de seis?* [p=0.3] E *log de setenta e dois?* [p=0.4] {c}Sem "
        "calculadora. [p=0.3] Próximo episódio."),
    dict(id="29", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual foi o log que você leu como pergunta pela primeira vez? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
