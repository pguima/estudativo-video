# Roteiro — Função Logarítmica, Episódio 1 de 5: o espelho da exponencial (gráfico, domínio e sinal)
# Base: Estudos/Enem/estudos/01-matematica/28-funcao-logaritmica-aplicacoes.html — seções 02, 03 e 04 + Questão 7.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O ESPELHO: o log é a exponencial vista no espelho da reta y = x; o ponto (a, b) vira (b, a).
#   RETORNO DECRESCENTE: para o log subir um degrau, x precisa ser multiplicado por 10 (a escada 1, 10, 100, 1 000).
#   A PORTA DO LOG: dentro do log só entra número estritamente positivo; a porta fica fechada para o zero e os negativos.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Escalas (pH, Richter, decibéis): próximos episódios. Função inversa: só citada (série própria).
# Concreto (regra 1): quem treina para uma prova; o modelo P(t) = 20 · log t do material (1 h → 0, 10 h → 20,
#   100 h → 40, 1 000 h → 60 pontos).
# Nós fazemos (prompt): domínio de log(3x − 12) → x > 4; log_3 x < 2 → x < 9, com o domínio: 0 < x < 9.
# Erros (prompt): x ≥ 3 no domínio de log(2x − 6) · log_0,5 x > 2 ⇒ x > 0,25 · "o log cresce cada vez mais rápido".
# QUESTÃO 7 ("nós fazemos", com pausa): gabarito C (0,2). Erradas = material (A −5 faz x = −b; B 0,04 = 25⁻¹;
#   D 0,5 = 2⁻¹; E 5 é onde f(x) = 1). Conferência NOSSA (marcada): 0,2 está entre 0 e 1, onde o log de base 5 é negativo.
# Acréscimos NOSSOS (marcados): quatro cenas verdes de ATALHO — "desenhar o log: troque x e y da tabela da
#   exponencial" (cena 08), "ler a base: procure a altura 1; o x desse ponto é a base" (cena 11, com base 3 para não entregar a base 5 da Q7), "domínio: escreva
#   '> 0' antes de qualquer conta; base com x, mais duas condições" (cena 16) e "inequação em 4 passos: domínio, tire
#   o log, base menor que 1 vira o sinal, cruze com o domínio" (cena 19).
# Frases-chave (meio e fim, idênticas): 1. Log e exponencial são espelhos na reta y = x.
#   2. Toda função logarítmica passa por (1, 0) e por (b, 1).
#   3. Dentro do log, só número estritamente positivo.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Função logarítmica do zero: o espelho da exponencial, gráfico e domínio | Função Logarítmica Ep. 1"
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
        "{a}Num modelo de desempenho, [p=0.2] P de t igual a *vinte vezes log de t,* [p=0.2] com t em horas de treino, "
        "[p=0.3] {b}*cem horas* dão *quarenta pontos.* [p=0.5] {c}Para chegar a *sessenta pontos,* [p=0.2] você precisa "
        "de *duzentas horas?* [p=0.6] {d}Não: [p=0.2] de *mil.* [p=0.5] {e}Essa é a *cara do logaritmo.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o primeiro episódio da série de *Função logarítmica.* [p=0.4] {a}Ao final, [p=0.2] você vai *desenhar "
        "o gráfico do log,* [p=0.3] {b}*ler a base* num gráfico, [p=0.3] {c}achar o *domínio* de uma expressão [p=0.3] "
        "{d}e resolver *inequações logarítmicas.*"),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Da série de Logaritmos: [p=0.2] log na base b de a igual a x [p=0.2] quer "
        "dizer *b elevado a x igual a a.* [p=0.2] E a base é positiva e diferente de um. [p=0.4] {b}Da série de Função "
        "exponencial: [p=0.2] o gráfico de dois elevado a x passa por *zero, um* [p=0.2] e gruda no eixo x, [p=0.2] a "
        "*assíntota.* [p=0.4] {c}E, de Conceito de função: [p=0.2] *domínio* são os valores que *podem entrar.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Pense em alguém treinando para uma prova. [p=0.4] {a}As *primeiras horas* rendem muito: [p=0.2] de uma para "
        "dez horas, [p=0.2] *vinte pontos.* [p=0.4] {b}Mas para ganhar *mais vinte,* [p=0.2] é preciso ir de dez para "
        "*cem* horas. [p=0.4] {c}Cada hora a mais [p=0.2] rende *menos* que a anterior. [p=0.4] {d}Esse jeito de crescer "
        "tem nome: [p=0.2] *logaritmo.*"),

    # ================= BLOCO A: DEFINIÇÃO =================
    dict(id="05", block="definicao", text=
        "{t}Então, o que é uma função logarítmica? [p=0.4] {a}É toda função *f de x igual a log na base b de x,* "
        "[p=0.2] com b positivo e diferente de um. [p=0.4] {b}O x precisa ser *maior que zero.* [p=0.3] Por isso, "
        "[p=0.2] o *domínio* é de zero, aberto, até o infinito. [p=0.4] {c}E o que sai? [p=0.2] A *imagem,* [p=0.2] os "
        "valores que saem da função, [p=0.2] são *todos os números reais:* [p=0.2] negativos, zero e positivos."),

    # ================= BLOCO B: O ESPELHO =================
    dict(id="06", block="espelho", text=
        "{t}E de onde vem essa função? [p=0.4] {a}Se dois elevado a três é oito, [p=0.2] então log na base dois de oito "
        "[p=0.2] é *três.* [p=0.4] {b}O log *desfaz* o que a exponencial faz. [p=0.3] Funções assim, [p=0.2] em que uma "
        "desfaz a outra, [p=0.2] se chamam *funções inversas.* [p=0.4] {c}Elas têm série própria. [p=0.2] Aqui, só o "
        "*desenho.*"),
    dict(id="07", block="espelho", text=
        "{t}Pegue o gráfico de dois elevado a x [p=0.2] e a reta *y igual a x,* tracejada. [p=0.4] {a}Agora *dobre a "
        "folha* sobre essa reta. [p=0.4] {b}Cada ponto *troca as coordenadas:* [p=0.2] zero, um [p=0.2] vira *um, zero.* "
        "[p=0.3] Um, dois [p=0.2] vira *dois, um.* [p=0.3] Três, oito [p=0.2] vira *oito, três.* [p=0.4] {c}E a assíntota "
        "deitada, [p=0.2] o eixo x, [p=0.2] *gira* e fica em pé: [p=0.2] vira o eixo y. [p=0.3] É uma *assíntota "
        "vertical:* [p=0.2] uma reta em pé da qual a curva chega perto, [p=0.2] sem tocar. [p=0.4] {d}Domínio e imagem "
        "também *trocam de papel.*"),
    dict(id="08", block="atalho_esp", text=
        "{t}Atalho para desenhar o log. [p=0.4] {a}Faça a tabela da *exponencial.* [p=0.4] {b}*Troque as colunas:* "
        "[p=0.2] o que era x vira y, [p=0.2] e o que era y vira x. [p=0.4] {c}Pronto: [p=0.2] você tem os pontos do *log,* "
        "[p=0.2] sem calcular nenhum logaritmo."),

    # ================= BLOCO C: O GRÁFICO =================
    dict(id="09", block="grafico", text=
        "{t}E como fica o gráfico? [p=0.4] {a}Com base *maior que um,* [p=0.2] a curva *sobe:* [p=0.2] é *crescente.* "
        "[p=0.2] x aumenta, [p=0.2] y aumenta. [p=0.4] {b}Com base *entre zero e um,* [p=0.2] a curva *desce:* [p=0.2] é "
        "*decrescente.* [p=0.4] {c}E as duas ficam *coladas no eixo y,* [p=0.2] sem tocar."),
    dict(id="10", block="grafico", text=
        "{t}Existe algum ponto por onde *toda* função logarítmica passa? [p=0.4] {a}Existem *dois.* [p=0.3] O *um, zero:* "
        "[p=0.2] o log de um é zero, [p=0.2] porque qualquer base elevada a zero dá um. [p=0.4] {b}E o *b, um:* [p=0.2] o "
        "log da própria base é um. [p=0.4] {c}E repare: [p=0.2] log na base um meio de x [p=0.2] é *menos* log na base dois "
        "de x. [p=0.3] Uma é o *espelho* da outra no eixo x."),
    dict(id="11", block="atalho_base", text=
        "{t}Atalho para *ler a base* num gráfico. [p=0.4] {a}Procure o ponto em que a curva tem *altura um.* [p=0.4] "
        "{b}O x desse ponto [p=0.2] *é a base.* [p=0.4] {c}Se a curva passa por *três, um,* [p=0.2] a base é três."),

    # ================= BLOCO D: O SINAL =================
    dict(id="12", block="sinal", text=
        "{t}Quando o log dá *negativo?* [p=0.4] {a}O *sinal* de uma função diz onde ela é positiva [p=0.2] e onde é "
        "negativa. [p=0.4] {b}Com base maior que um: [p=0.2] entre zero e um, [p=0.2] o log é *negativo.* [p=0.3] Log de "
        "zero vírgula zero um [p=0.2] é *menos dois.* [p=0.3] E para x maior que um, [p=0.2] *positivo.* [p=0.4] {c}Com "
        "base entre zero e um, [p=0.2] é *o contrário.* [p=0.3] Log na base zero vírgula cinco de oito [p=0.2] é *menos "
        "três.*"),

    # ================= BLOCO E: RETORNO DECRESCENTE =================
    dict(id="13", block="escada", text=
        "{t}Por que o log cresce *cada vez mais devagar?* [p=0.4] {a}De um para dez, [p=0.2] o log sobe *um.* [p=0.3] De "
        "dez para cem, [p=0.2] sobe *mais um.* [p=0.3] De cem para mil, [p=0.2] *mais um.* [p=0.4] {b}É o *retorno "
        "decrescente:* [p=0.2] para o log subir um degrau, [p=0.2] x precisa ser *multiplicado por dez.* [p=0.4] {c}No "
        "treino: [p=0.2] quarenta pontos são cem horas. [p=0.2] Sessenta pontos [p=0.2] são *mil horas.*"),

    # ================= BLOCO F: DOMÍNIO =================
    dict(id="14", block="dominio", text=
        "{t}O que pode *entrar* no log? [p=0.4] {a}Dentro do log, [p=0.2] só entra número *estritamente positivo.* "
        "[p=0.3] A *porta do log* fica fechada para o zero [p=0.2] e para os negativos. [p=0.4] {b}Então, no log de dois "
        "x menos seis, [p=0.2] escreva primeiro: [p=0.2] *dois x menos seis maior que zero.* [p=0.4] {c}Dois x maior que "
        "seis, [p=0.2] *x maior que três.*"),
    dict(id="15", block="dominio", text=
        "{t}E quando aparece um x ao quadrado? [p=0.4] {a}No log de x ao quadrado menos nove, [p=0.2] a condição é *x ao "
        "quadrado maior que nove.* [p=0.3] Isso vale para *x menor que menos três* [p=0.2] ou *x maior que três.* [p=0.3] "
        "Teste o zero: [p=0.2] dá menos nove. [p=0.2] *Porta fechada.* [p=0.4] {b}E se o x estiver *na base?* [p=0.2] No "
        "log na base x de cinco menos x, [p=0.2] são *três* condições: [p=0.2] cinco menos x positivo, [p=0.2] x positivo "
        "[p=0.2] e x diferente de um. [p=0.3] {c}Resposta: [p=0.2] x entre zero e cinco, [p=0.2] *sem o um.*"),
    dict(id="16", block="atalho_dom", text=
        "{t}Atalho para o domínio. [p=0.4] {a}Antes de qualquer conta, [p=0.2] escreva *maior que zero* [p=0.2] para o "
        "que está dentro do log. [p=0.4] {b}Tem x na base? [p=0.2] Mais duas condições: [p=0.2] *maior que zero* [p=0.2] "
        "e *diferente de um.* [p=0.4] {c}Só depois resolva."),

    # ================= BLOCO G: INEQUAÇÕES =================
    dict(id="17", block="ineq", text=
        "{t}E as inequações? [p=0.4] {a}Uma *inequação logarítmica* [p=0.2] compara um log com um número, [p=0.2] usando "
        "maior ou menor. [p=0.4] {b}Log na base dois de x maior que três. [p=0.3] Base maior que um: [p=0.2] o sentido se "
        "*mantém.* [p=0.3] x maior que dois ao cubo, [p=0.2] *x maior que oito.* [p=0.4] {c}E todo número maior que oito "
        "[p=0.2] já é positivo. [p=0.2] O domínio está garantido."),
    dict(id="18", block="ineq", text=
        "{t}E com base menor que um? [p=0.4] {a}Log na base zero vírgula cinco de x maior que dois. [p=0.3] É a mesma regra "
        "da exponencial: [p=0.2] base entre zero e um *inverte* o sentido. [p=0.3] x *menor* que zero vírgula cinco ao "
        "quadrado, [p=0.2] *zero vírgula vinte e cinco.* [p=0.4] {b}Mas a porta do log está fechada para o zero e os "
        "negativos. [p=0.4] {c}Resposta final: [p=0.2] x *entre zero e zero vírgula vinte e cinco.*"),
    dict(id="19", block="atalho_ineq", text=
        "{t}Atalho: [p=0.2] toda inequação logarítmica em *quatro passos.* [p=0.4] {a}Um: [p=0.2] escreva o *domínio.* "
        "[p=0.3] {b}Dois: [p=0.2] *tire o log,* [p=0.2] trocando por base elevada ao número. [p=0.3] {c}Três: [p=0.2] base "
        "menor que um? [p=0.2] *Vire o sinal.* [p=0.3] {d}Quatro: [p=0.2] *cruze* com o domínio."),

    # ================= NÓS FAZEMOS =================
    dict(id="20", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Qual é o *domínio* de f de x igual a log de três x menos doze? [p=0.4] {b}E qual é a solução "
        "de log na base três de x *menor que dois?* [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="21", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Três x menos doze maior que zero. [p=0.2] Três x maior que doze, [p=0.2] *x maior que "
        "quatro.* [p=0.4] {b}Agora a inequação. [p=0.2] Base três, maior que um: [p=0.2] o sentido se mantém. [p=0.2] x "
        "menor que três ao quadrado, [p=0.2] *x menor que nove.* [p=0.4] {c}E o domínio entra: [p=0.2] x precisa ser "
        "positivo. [p=0.3] Resposta: [p=0.2] *x entre zero e nove.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="22", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] log e exponencial são espelhos na reta y igual a x. "
        "[p=0.5] {b}Dois: [p=0.2] toda função logarítmica passa por um, zero [p=0.2] e por b, um. [p=0.5] {c}Três: "
        "[p=0.2] dentro do log, [p=0.2] só número estritamente positivo."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="23", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] dizer que o domínio de log de dois x menos seis "
        "[p=0.2] é *x maior ou igual a três.* [p=0.4] {b}Parece certo, [p=0.2] porque o três *resolve a conta* do zero. "
        "[p=0.4] {c}Mas com x igual a três, [p=0.2] sobra *log de zero,* [p=0.2] que não existe. [p=0.3] O certo é *x maior "
        "que três.*"),
    dict(id="24", block="erros", text=
        "{a}Segundo: [p=0.2] log na base zero vírgula cinco de x maior que dois [p=0.2] dar *x maior que zero vírgula "
        "vinte e cinco.* [p=0.4] {b}Parece certo, [p=0.2] porque com base dois, [p=0.2] ou dez, [p=0.2] o sinal fica onde "
        "está. [p=0.4] {c}Mas base menor que um *inverte.* [p=0.3] O certo é *x entre zero e zero vírgula vinte e cinco.*"),
    dict(id="25", block="erros", text=
        "{a}Terceiro: [p=0.2] achar que o logaritmo cresce *cada vez mais rápido.* [p=0.4] {b}Parece certo, [p=0.2] porque "
        "a curva *sobe para sempre,* [p=0.2] sem teto. [p=0.4] {c}Mas cada degrau custa *dez vezes mais x.* [p=0.3] Ele "
        "cresce *cada vez mais devagar.*"),

    # ================= QUESTÃO 7 (NÓS FAZEMOS) =================
    dict(id="26", block="q7", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] Esta, [p=0.2] a gente resolve *junto.* [p=0.4] {a}O gráfico de "
        "uma função f de x igual a log na base b de x, [p=0.2] com b positivo e diferente de um, [p=0.2] passa pelo ponto "
        "*vinte e cinco, dois.* [p=0.3] O valor de x para o qual f de x é igual a *menos um* é: [p=0.3] {qa}A: [p=0.2] "
        "menos cinco. [p=0.2] {qb}B: [p=0.2] zero vírgula zero quatro. [p=0.2] {qc}C: [p=0.2] zero vírgula dois. [p=0.2] "
        "{qd}D: [p=0.2] zero vírgula cinco. [p=0.2] {qe}E: [p=0.2] cinco. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="27", block="q7", text=
        "{t}Vamos juntos. [p=0.3] {a}O ponto diz: [p=0.2] log na base b de vinte e cinco é dois. [p=0.2] Então *b ao "
        "quadrado é vinte e cinco.* [p=0.4] {b}b seria cinco ou menos cinco, [p=0.2] mas a base é *positiva:* [p=0.2] *b "
        "igual a cinco.* [p=0.4] {c}Agora, log na base cinco de x igual a menos um: [p=0.2] x é cinco elevado a menos um, "
        "[p=0.2] *um quinto,* [p=0.2] *zero vírgula dois.* [p=0.3] Positivo, [p=0.2] e entre zero e um, [p=0.2] onde o log "
        "é negativo. [p=0.3] {ok}*Letra C!*"),
    dict(id="28", block="q7", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A faz x igual a *menos a base,* [p=0.2] como se o expoente negativo trocasse o "
        "sinal. [p=0.2] Mas x precisa ser positivo. [p=0.4] {xb}A B usa *vinte e cinco* como base. [p=0.4] {xd}A D usa o "
        "*dois,* [p=0.2] a altura do ponto, [p=0.2] como base. [p=0.4] {xe}E a E é o ponto em que f de x vale *um,* [p=0.2] "
        "não menos um."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="29", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] log e exponencial são espelhos na reta y igual a x. "
        "[p=0.5] {b}Dois: [p=0.2] toda função logarítmica passa por um, zero [p=0.2] e por b, um. [p=0.5] {c}Três: "
        "[p=0.2] dentro do log, [p=0.2] só número estritamente positivo."),

    # ================= PONTE E CTA =================
    dict(id="30", block="ponte", text=
        "{a}Um suco tem *pH três,* [p=0.2] e a água da chuva tem *pH seis.* [p=0.4] {b}O suco é *duas* vezes mais ácido? "
        "[p=0.3] *Três* vezes? [p=0.3] *Mil* vezes? [p=0.4] {c}Próximo episódio."),
    dict(id="31", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] em que outra situação mais esforço rende cada vez menos? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
