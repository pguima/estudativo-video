# Roteiro — Polinômios e Equações Polinomiais, Episódio 4 de 5: Girard e gráficos (soma, produto, multiplicidade e
#   raízes conjugadas)
# Base: Estudos/Enem/estudos/01-matematica/35-polinomios-equacoes-polinomiais.html — seções 08 e 09 + Questões 4, 5 e 6.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na revisão):
#   OS SINAIS ALTERNADOS: Girard no 3º grau é "menos, mais, menos, sempre dividindo pelo a".
#   A BOLA NO CHÃO: raiz de multiplicidade par QUICA no eixo (toca e volta); ímpar ATRAVESSA (como a bola que passa
#     por um vidro).
#   O PAR DE MEIAS: raízes não reais andam em dupla: se 1 − i é raiz (coeficientes reais), 1 + i vem junto.
#   A CAIXA DE SAPATO: arestas = raízes; produto = volume.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Revisão rápida: soma −b/a e produto c/a do 2º grau (série de Equação do 2º grau); forma fatorada e multiplicidade
#   (episódio 3); onde a parábola corta o eixo x (série de Função quadrática); i² = −1 (série de Números complexos).
# Exemplos do material: bloco a (x³ − 2x² − 5x + 6, raízes −2, 1, 3) e bloco c ((x + 1)²(x − 3), P(0) = −3).
# Exemplos NOSSOS (marcados):
#   - bloco b (leitura geométrica): a caixa de sapato 2 × 3 × 5 (volume 30; metade da área 31; um quarto das arestas
#     10), porque o material só dá a regra. Não usamos 1, 2, 3 (é o "nós fazemos") nem 1, 2, 4 (é a Q4).
#   - bloco e (conjugadas): a CONTA do produto do par usa 2 ± i (soma 4, produto 4 − i² = 5 → x² − 4x + 5). O prompt
#     pedia o par 1 ± i → x² − 2x + 2, que é exatamente o passo-chave da Questão 6 ("você faz"). O par 1 − i aparece
#     só na analogia do par de meias (sem a multiplicação); a conta 1 − i² = 2 fica para a resolução da Q6.
#   - erro 3: "grau 2 com raízes 3 e 1 − i" (impossível com coeficientes reais) — exemplo nosso.
# Acréscimos NOSSOS (marcados): cena verde de ATALHO "escreva a, b, c, d com os sinais antes de qualquer fração";
#   cena verde "lendo o gráfico: conte os encontros, veja toca ou atravessa, leia P(0)"; cena verde "par conjugado:
#   x² − (soma)x + (produto)".
# QUESTÃO 4 (eu faço): produto = −d/a = −(−16)/2 = 8 (B). Conferência 2(x − 1)(x − 2)(x − 4). Erradas = material
#   (A soma 7; C c/a 14, metade da área; D esquece de dividir por 2, 16; E área total 28).
# QUESTÃO 5 (nós fazemos): P = a(x + 1)(x − 2)², P(0) = 4a = 4, a = 1 (E). Erradas = material (A troca os sinais das
#   raízes; B inverte as multiplicidades, P(0) = −2; C tem P(0) = −4; D tem grau 2).
# QUESTÃO 6 (você faz): o conjugado 1 + i entra; soma 2, produto (1 − i)(1 + i) = 1 − i² = 2; fator x² − 2x + 2;
#   P = (x − 2)(x² − 2x + 2) = x³ − 4x² + 6x − 4 (B). Erradas = material (A sinais trocados; C (1 − i)(1 + i) = 0;
#   D x² + 2; E grau 2, sem a raiz 2). Conferência nossa: Girard (soma 4, produto 4) e P(2) = 0.
# Nós fazemos (prompt): x³ − 6x² + 11x − 6, raízes 1, 2, 3: soma 6, pares 11, produto 6.
# Frases-chave (meio e fim, idênticas): 1. Girard no 3º grau: menos, mais, menos, sempre dividindo por a.
#   2. Multiplicidade par toca; ímpar atravessa. 3. Raiz não real chega com o conjugado.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Girard e gráficos: soma e produto das raízes sem resolver | Polinômios Ep. 4"
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
        "{a}As arestas de um bloco são as raízes de *dois x ao cubo, menos catorze x ao quadrado, mais vinte e oito x, "
        "menos dezesseis, igual a zero.* [p=0.5] {b}O volume é *oito metros cúbicos,* [p=0.3] {c}e você descobre isso "
        "*sem achar nenhuma aresta.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o quarto episódio da série de *Polinômios.* [p=0.4] {a}Ao final, [p=0.2] você vai tirar *soma e "
        "produto das raízes* direto dos coeficientes, [p=0.3] {b}escolher a *lei de um gráfico* pelas raízes [p=0.3] "
        "{c}e completar as *raízes não reais.*"),
    dict(id="03", block="prereq", text=
        "{t}Quatro lembretes rápidos. [p=0.3] {a}Do segundo grau: [p=0.2] soma, *menos b sobre a;* [p=0.2] produto, "
        "*c sobre a.* [p=0.4] {b}Do episódio três: [p=0.2] fator que aparece *duas vezes,* [p=0.2] *multiplicidade "
        "dois.* [p=0.4] {c}Da Função quadrática: [p=0.2] raiz é onde a curva *encontra o eixo x.* [p=0.4] {d}E um número novo: [p=0.2] *i,* [p=0.2] com *i ao quadrado "
        "igual a menos um.* [p=0.2] Isso tem série própria, [p=0.2] *a próxima.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Pense numa *caixa de sapato.* [p=0.4] {a}Ela tem três medidas: [p=0.2] *a, b e c.* [p=0.2] O volume é "
        "*a vezes b vezes c.* [p=0.4] {b}Agora, duas bolas. [p=0.3] Uma cai no chão e *quica:* [p=0.2] encosta e "
        "*volta.* [p=0.4] {c}A outra cai num *vidro fino* [p=0.2] e *atravessa.* [p=0.4] {d}Hoje, a caixa vira "
        "*equação,* [p=0.2] e as bolas viram *gráfico.*"),

    # ================= BLOCO A: GIRARD =================
    dict(id="05", block="girard", text=
        "{t}Dá para saber a *soma das raízes* sem achar nenhuma delas? [p=0.5] {a}Dá. [p=0.2] *Relações de Girard:* "
        "[p=0.2] as contas que ligam os *coeficientes* às *raízes.* [p=0.4] {b}Para a x ao cubo, mais b x ao quadrado, "
        "mais c x, mais d, igual a zero: [p=0.3] {c}a *soma* das três raízes é *menos b sobre a.* [p=0.4] {d}A *soma dos "
        "produtos dois a dois* [p=0.2] é *c sobre a:* [p=0.2] você multiplica as raízes em pares e soma. [p=0.4] {e}E o "
        "*produto* das três é *menos d sobre a.* [p=0.4] {f}Menos, [p=0.2] mais, [p=0.2] menos."),
    dict(id="06", block="girard_teste", text=
        "{t}Será que funciona mesmo? [p=0.4] {a}Pegue *x ao cubo, menos dois x ao quadrado, menos cinco x, mais seis,* "
        "[p=0.2] de raízes *menos dois, um e três.* [p=0.4] {b}Os coeficientes, *com os sinais:* "
        "[p=0.2] a é um, [p=0.2] b é menos dois, [p=0.2] c é menos cinco, [p=0.2] d é seis. [p=0.4] {c}Soma: [p=0.2] "
        "*dois.* [p=0.2] Menos b sobre a: [p=0.2] *dois.* [p=0.4] {d}Pares: [p=0.2] menos dois, menos seis, mais três: "
        "[p=0.2] *menos cinco,* [p=0.2] o c sobre a. [p=0.4] {e}Produto: [p=0.2] *menos seis,* [p=0.2] o menos d sobre "
        "a. [p=0.3] Bateu tudo."),
    dict(id="07", block="atalho_sinais", text=
        "{t}Atalho. [p=0.4] {a}Antes de qualquer fração, [p=0.2] escreva *a, b, c e d com os sinais.* [p=0.4] {b}Depois "
        "aplique o *menos, mais, menos.* [p=0.2] O sinal do coeficiente e o sinal da fórmula *não se confundem.*"),

    # ================= BLOCO B: A CAIXA =================
    dict(id="08", block="caixa", text=
        "{t}E a caixa de sapato? [p=0.4] {a}Se as arestas são as raízes, [p=0.2] *o produto das raízes é o volume.* "
        "[p=0.4] {b}A soma dos produtos dois a dois [p=0.2] é *metade da área total.* [p=0.4] {c}E a soma das raízes "
        "[p=0.2] é *um quarto* do comprimento de todas as arestas. [p=0.4] {d}Numa caixa de *dois, três e cinco:* "
        "[p=0.2] volume *trinta;* [p=0.2] pares, *trinta e um,* [p=0.2] metade da área; [p=0.2] e soma *dez,* "
        "[p=0.2] um quarto das arestas."),

    # ================= BLOCO C: O GRÁFICO =================
    dict(id="09", block="grafico", text=
        "{t}E o gráfico, [p=0.2] o que ele conta? [p=0.4] {a}As *raízes reais* [p=0.2] são os pontos onde a curva "
        "*encontra o eixo horizontal.* [p=0.4] {b}Veja *x mais um, ao quadrado, vezes x menos três.* [p=0.4] {c}Em "
        "*menos um,* [p=0.2] a bola *quica:* [p=0.2] a curva toca o eixo e volta. [p=0.4] {d}Em *três,* [p=0.2] a bola "
        "*atravessa.* [p=0.4] {e}E no eixo vertical: [p=0.2] P de zero é um vezes menos três: [p=0.2] *menos três.*"),
    dict(id="10", block="multiplicidade", text=
        "{t}Por que ela quica em menos um? [p=0.4] {a}*Multiplicidade par:* [p=0.2] o fator aparece um número *par* de "
        "vezes. [p=0.2] Ao quadrado, [p=0.2] ele *nunca é negativo.* [p=0.2] O sinal não muda: [p=0.2] a curva *toca e "
        "volta.* [p=0.4] {b}*Multiplicidade ímpar:* [p=0.2] o fator aparece um número *ímpar* de vezes. [p=0.2] Ele "
        "*troca de sinal,* [p=0.2] e a curva *atravessa.*"),

    # ================= BLOCO D: FATOS QUE ELIMINAM =================
    dict(id="11", block="fatos", text=
        "{t}E como o gráfico elimina alternativas? [p=0.4] {a}Grau *n:* [p=0.2] *no máximo n encontros* com o eixo. "
        "[p=0.4] {b}Grau *ímpar,* [p=0.2] com coeficientes reais: [p=0.2] *pelo menos uma raiz real.* [p=0.2] A curva "
        "vai de um lado ao outro do eixo. [p=0.4] {c}E grau ímpar com o coeficiente dominante *positivo:* [p=0.2] a "
        "curva *começa embaixo* [p=0.2] e *termina em cima.*"),
    dict(id="12", block="atalho_grafico", text=
        "{t}Atalho. [p=0.4] {a}Diante de um gráfico, [p=0.2] três leituras: [p=0.2] *conte os encontros* com o eixo, "
        "[p=0.3] {b}veja em cada um se *toca ou atravessa,* [p=0.3] {c}e leia *P de zero* no eixo vertical."),

    # ================= BLOCO E: CONJUGADAS =================
    dict(id="13", block="conjugadas", text=
        "{t}E quando a raiz *não é real?* [p=0.4] {a}*Unidade imaginária:* [p=0.2] o número *i,* [p=0.2] que ao "
        "quadrado dá *menos um.* [p=0.4] {b}*Raiz não real:* [p=0.2] uma raiz que usa o i, [p=0.2] como *um menos i.* "
        "[p=0.4] {c}*Conjugado:* [p=0.2] o mesmo número, [p=0.2] *i com sinal trocado.* [p=0.4] {d}A regra: [p=0.2] com "
        "coeficientes reais, [p=0.2] raízes não reais andam *em dupla,* [p=0.2] como *par de meias.* [p=0.3] Se um menos "
        "i é raiz, [p=0.2] *um mais i vem junto.*"),
    dict(id="14", block="conjugadas_conta", text=
        "{t}E o par gera o quê? [p=0.4] {a}Pegue o par *dois mais i* e *dois menos i.* [p=0.4] {b}Soma: [p=0.2] os i "
        "se cancelam: [p=0.2] *quatro.* [p=0.4] {c}Produto: [p=0.2] quatro, menos i ao quadrado. [p=0.2] Como i ao "
        "quadrado é menos um, [p=0.2] quatro *mais* um: [p=0.2] *cinco.* [p=0.4] {d}O par gera *x ao quadrado, menos "
        "quatro x, mais cinco.* [p=0.2] Coeficientes *reais.* [p=0.2] O i sumiu."),
    dict(id="15", block="atalho_par", text=
        "{t}Atalho. [p=0.4] {a}Para um par conjugado: [p=0.2] *x ao quadrado, menos a soma vezes x, mais o produto.* "
        "[p=0.4] {b}No produto, [p=0.2] o *menos i ao quadrado* vira *mais um.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}As raízes de *x ao cubo, menos seis x ao quadrado, mais onze x, menos seis* [p=0.2] são "
        "*um, dois e três:* [p=0.2] o lucro da Questão três. [p=0.4] {b}Confira as *três relações de Girard.* [p=0.4] "
        "{c}*Pause e tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}a é um, [p=0.2] b é menos seis, [p=0.2] c é onze, [p=0.2] d é menos seis. "
        "[p=0.4] {b}Soma: [p=0.2] *seis;* [p=0.2] menos b sobre a: [p=0.2] *seis.* [p=0.4] {c}Pares: [p=0.2] dois, mais "
        "três, mais seis: [p=0.2] *onze;* [p=0.2] c sobre a: [p=0.2] *onze.* [p=0.4] {d}Produto: [p=0.2] *seis;* "
        "[p=0.2] menos d sobre a: [p=0.2] *seis.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] Girard no terceiro grau: [p=0.2] menos, mais, menos, "
        "[p=0.2] sempre dividindo por a. [p=0.5] {b}Dois: [p=0.2] multiplicidade par toca; [p=0.2] ímpar atravessa. "
        "[p=0.5] {c}Três: [p=0.2] raiz não real chega com o conjugado."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os erros clássicos. [p=0.4] {a}O primeiro: [p=0.2] usar *d sobre a* como produto no terceiro grau. "
        "[p=0.2] Em x ao cubo, menos dois x ao quadrado, menos cinco x, mais seis, [p=0.2] a pessoa diz *seis.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque no segundo grau o produto é *c sobre a,* [p=0.2] sem menos. [p=0.4] {c}Mas no "
        "terceiro grau os sinais *alternam:* [p=0.2] o produto é *menos d sobre a,* [p=0.2] *menos seis.*"),
    dict(id="20", block="erros", text=
        "{t}O segundo: [p=0.2] {a}achar que *toda raiz atravessa* o eixo. [p=0.2] Em x mais um, ao quadrado, vezes x "
        "menos três, [p=0.2] desenhar a curva *cruzando* em menos um. [p=0.4] {b}Parece certo, [p=0.2] porque raiz "
        "parece sinônimo de *cortar o eixo.* [p=0.4] {c}Mas o fator ao quadrado *não troca de sinal:* [p=0.2] em menos "
        "um, a curva *toca e volta.*"),
    dict(id="21", block="erros", text=
        "{t}O terceiro: [p=0.2] {a}aceitar *um menos i sozinha.* [p=0.2] Dizer que um polinômio de *grau dois,* com "
        "coeficientes reais, [p=0.2] tem raízes *três* e *um menos i.* [p=0.4] {b}Parece certo, [p=0.2] porque são só "
        "*duas raízes* para um grau dois. [p=0.4] {c}Mas um menos i *traz o um mais i:* [p=0.2] seriam *três* raízes. "
        "[p=0.2] O grau teria de ser *pelo menos três.*"),

    # ================= QUESTÃO 4: EU FAÇO =================
    dict(id="22", block="q4", text=
        "{t}Agora, [p=0.2] uma questão no estilo do ENEM. [p=0.4] {a}As medidas, em metros, das três arestas de um "
        "bloco retangular [p=0.2] são as raízes de *dois x ao cubo, menos catorze x ao quadrado, mais vinte e oito x, "
        "menos dezesseis, igual a zero.* [p=0.4] {b}O volume do bloco, em metros cúbicos, é: [p=0.3] {qa}A: sete. "
        "[p=0.2] {qb}B: oito. [p=0.2] {qc}C: catorze. [p=0.2] {qd}D: dezesseis. [p=0.2] {qe}E: vinte e oito."),
    dict(id="23", block="q4", text=
        "{t}Essa, [p=0.2] *eu faço.* [p=0.4] {a}É soma, produto ou gráfico? [p=0.2] Volume é *produto* das arestas: "
        "[p=0.2] produto das raízes. [p=0.4] {b}Os coeficientes, com os sinais: [p=0.2] a é dois, [p=0.2] b é menos "
        "catorze, [p=0.2] c é vinte e oito, [p=0.2] d é menos dezesseis. [p=0.4] {c}Produto: [p=0.2] *menos d sobre a:* "
        "[p=0.2] menos, menos dezesseis, sobre dois: [p=0.2] *oito.* [p=0.3] {ok}*Letra B!* [p=0.4] {d}Confiro: "
        "[p=0.2] a equação é *dois vezes x menos um, x menos dois, x menos quatro.* [p=0.2] Arestas um, dois e quatro: "
        "[p=0.2] volume *oito.*"),
    dict(id="24", block="q4", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A é a *soma* das raízes: [p=0.2] menos b sobre a, sete. [p=0.4] {xc}A C é "
        "*c sobre a,* catorze: [p=0.2] a metade da área total. [p=0.4] {xd}A D esquece de *dividir por dois.* [p=0.4] "
        "{xe}E a E é a *área total* do bloco: [p=0.2] duas vezes catorze."),

    # ================= QUESTÃO 5: NÓS FAZEMOS =================
    dict(id="25", block="q5", text=
        "{t}Agora, [p=0.2] *nós fazemos.* [p=0.4] {a}O gráfico mostra um polinômio P de *grau três.* [p=0.2] Ele "
        "*cruza* o eixo horizontal em *menos um,* [p=0.2] *só toca* esse eixo em *dois* [p=0.2] e corta o eixo vertical "
        "em *zero, quatro.* [p=0.4] {b}A lei de P é: [p=0.3] {qa}A, [p=0.2] {qb}B, [p=0.2] {qc}C, [p=0.2] {qd}D [p=0.2] "
        "{qe}ou E, [p=0.2] na tela. [p=0.3] {p}*Pense comigo.* [p=1.5]"),
    dict(id="26", block="q5", text=
        "{t}É soma, produto ou gráfico? [p=0.2] *Gráfico.* [p=0.4] {a}Cruza em menos um: [p=0.2] multiplicidade "
        "*ímpar,* [p=0.2] fator *x mais um.* [p=0.4] {b}Toca em dois: [p=0.2] multiplicidade *par,* [p=0.2] fator *x "
        "menos dois, ao quadrado.* [p=0.4] {c}Um mais dois: [p=0.2] *grau três.* [p=0.2] Fechou. [p=0.2] P é *a vezes x "
        "mais um, vezes x menos dois ao quadrado.* [p=0.4] {d}P de zero: [p=0.2] a vezes um vezes quatro, [p=0.2] "
        "*quatro a.* [p=0.2] Igual a quatro: [p=0.2] *a é um.* [p=0.3] {ok}*Letra E!*"),
    dict(id="27", block="q5", text=
        "{t}E as outras? [p=0.3] {xa}A A troca os *sinais* das raízes: [p=0.2] daria um e menos dois. [p=0.4] {xb}A B "
        "*inverte as multiplicidades:* [p=0.2] tocaria em menos um, [p=0.2] cruzaria em dois, [p=0.2] e P de zero daria "
        "menos dois. [p=0.4] {xc}A C tem o *sinal* errado: [p=0.2] P de zero, menos quatro. [p=0.4] {xd}E a D é de *grau "
        "dois.*"),

    # ================= QUESTÃO 6: VOCÊ FAZ =================
    dict(id="28", block="q6", text=
        "{t}Agora, [p=0.2] *você faz.* [p=0.4] {a}Um polinômio P de *grau três,* com coeficientes reais e coeficiente "
        "dominante um, [p=0.2] tem como raízes *dois* e *um menos i,* [p=0.2] em que i ao quadrado é menos um. [p=0.4] "
        "{b}Então, P de x é: [p=0.3] {qa}A, [p=0.2] {qb}B, [p=0.2] {qc}C, [p=0.2] {qd}D [p=0.2] {qe}ou E, [p=0.2] na "
        "tela. [p=0.4] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="29", block="q6", text=
        "{t}Vamos conferir. [p=0.3] {a}Coeficientes reais: [p=0.2] o par de meias. [p=0.2] *Um mais i* entra. "
        "[p=0.4] {b}Soma do par: [p=0.2] *dois.* [p=0.2] Produto: [p=0.2] um, menos i ao quadrado: [p=0.2] um *mais* "
        "um, [p=0.2] *dois.* [p=0.4] {c}O par gera *x ao quadrado, menos dois x, mais dois.* [p=0.4] {d}Vezes *x menos "
        "dois:* [p=0.2] *x ao cubo, menos quatro x ao quadrado, mais seis x, menos quatro.* [p=0.3] {ok}*Letra B!* "
        "[p=0.4] {e}Girard confere: [p=0.2] soma das raízes, quatro; [p=0.2] menos b sobre a, *quatro.*"),
    dict(id="30", block="q6", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A usa as raízes com os *sinais trocados.* [p=0.4] {xc}A C calcula o produto "
        "do par como *zero,* [p=0.2] como se i ao quadrado fosse *mais um.* [p=0.4] {xd}A D usa o fator *x ao quadrado "
        "mais dois:* [p=0.2] esquece que a soma do par é dois. [p=0.4] {xe}E a E tem *grau dois:* [p=0.2] deixa de fora "
        "a raiz dois."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="31", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] Girard no terceiro grau: [p=0.2] menos, mais, "
        "menos, [p=0.2] sempre dividindo por a. [p=0.5] {b}Dois: [p=0.2] multiplicidade par toca; [p=0.2] ímpar "
        "atravessa. [p=0.5] {c}Três: [p=0.2] raiz não real chega com o conjugado."),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] *juntamos tudo,* [p=0.3] {b}caçamos as *pegadinhas* [p=0.3] {c}e "
        "treinamos com *questões inéditas.*"),
    dict(id="33", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha visto a bola que quica no eixo? [p=0.5] "
        "{anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no "
        "*Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
