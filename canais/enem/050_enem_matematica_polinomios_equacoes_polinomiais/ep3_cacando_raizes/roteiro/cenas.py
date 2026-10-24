# Roteiro — Polinômios e Equações Polinomiais, Episódio 3 de 5: caçando raízes (forma fatorada, candidatas racionais
#   e redução de grau)
# Base: Estudos/Enem/estudos/01-matematica/35-polinomios-equacoes-polinomiais.html — seções 06 e 07 + Questões 3 e 7.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O ESPELHO: raiz e fator têm sinais opostos — a raiz −2 vira o fator (x + 2); a raiz 3 vira (x − 3).
#   O MOLHO DE CHAVES: as candidatas são os divisores do termo independente sobre os divisores do dominante; a chave
#     que gira (P = 0) abre a porta.
#   O PRÉDIO (do ep. 1): cada raiz achada derruba um andar — Briot-Ruffini baixa o grau até o 2º, e Bhaskara termina.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Revisão rápida: Briot-Ruffini e P(a) = 0 (ep. 2); Bhaskara, soma e produto e a(x − x₁)(x − x₂) (série de Equação do
#   2º grau); divisores de um número (série de Divisibilidade).
# Blocos = seções 06 e 07, com os exemplos do material (x³ − 2x² − 5x + 6, 2x² − 2, (x + 1)²(x − 3)).
# Exemplo NOSSO (marcado): no bloco das candidatas com dominante diferente de 1, listamos as candidatas de um polinômio
#   com termo independente 4 e dominante 3 (±1, ±2, ±4, ±1/3, ±2/3, ±4/3), sem resolver nada — os números da Questão 7
#   ("você faz": termo 2, dominante 2) ficam só para ela.
# Cuidado do roteiros.md: no "nós fazemos" (x³ − 7x + 6) o ZERO do x² aparece na esteira de Briot-Ruffini.
# Erro 1: a raiz −2 virando (x − 2) é mostrado SEM desenvolver o produto: (x − 2)(x − 1)(x − 3) dá exatamente o
#   polinômio da Questão 3 e entregaria as raízes dela antes da hora.
# Acréscimos NOSSOS (marcados): cena verde de ATALHO "o espelho: troque o sinal e confira com o número no lugar do x";
#   cena verde dos testes rápidos (1 = soma dos coeficientes; −1 = troca o sinal dos termos de grau ímpar), que é o
#   bloco f do prompt; conferência de P(−1) = 8 no polinômio do cabeçalho.
# QUESTÃO 3 (eu faço): Briot-Ruffini com 1 → 1, −5, 6 e resto 0; x² − 5x + 6 → 2 e 3 (A). Erradas = material
#   (B troca os sinais; C lê os coeficientes 5 e 6 do quociente como raízes; D erra a 1ª soma, −7, e resolve
#   x² − 7x + 6 → 1 e 6; E troca o sinal do 6 e resolve x² − 5x − 6 → −1 e 6).
# QUESTÃO 7 (você faz): candidatas ±1, ±2, ±1/2; P(1) = −2; P(−1) = 0; Briot-Ruffini com −1 → 2, −5, 2; Δ = 9;
#   raízes 2 e 1/2; {−1, 1/2, 2} (E). Erradas = material (A troca os sinais; B só inteiros e para; C lista candidatas
#   sem testar: P(1) = −2 e P(−2) = −20; D inclui o 1 e perde o −1).
# Nós fazemos (prompt): x³ − 7x + 6 = 0 → {−3, 1, 2}.
# Frases-chave (meio e fim, idênticas): 1. Raiz e fator têm sinais opostos.
#   2. Candidatas: divisores do termo independente sobre divisores do dominante. 3. Achou uma raiz, Briot-Ruffini
#   derruba um grau.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Caçando raízes: equação do 3º grau sem fórmula · Matemática ENEM, Polinômios episódio 3"

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
        "{a}Não existe uma *Bhaskara do terceiro grau* [p=0.2] que se use na prova. [p=0.4] {b}Mesmo assim, [p=0.2] "
        "*x ao cubo, menos dois x ao quadrado, menos cinco x, mais seis, igual a zero* [p=0.2] se resolve em *um "
        "minuto:* [p=0.4] {c}*teste uma chave,* [p=0.2] {d}*baixe um grau* [p=0.2] {e}e *termine com Bhaskara.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o terceiro episódio da série de *Polinômios.* [p=0.4] {a}Ao final, [p=0.2] você vai *achar todas as "
        "raízes* de uma equação de *grau três* com coeficientes inteiros [p=0.3] {b}e escrever o polinômio na *forma "
        "fatorada* [p=0.2] *sem errar sinal.*"),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Do episódio dois: [p=0.2] se *P de a é zero,* [p=0.2] a é raiz, "
        "[p=0.2] e o *Briot-Ruffini* divide por x menos a. [p=0.4] {b}Da série de Equação do segundo grau: [p=0.2] "
        "*Bhaskara,* [p=0.2] *soma e produto* [p=0.2] e a forma *a vezes x menos x um, vezes x menos x dois.* [p=0.4] "
        "{c}E da Divisibilidade: [p=0.2] os *divisores* de seis são um, dois, três e seis."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Pense numa pequena *fábrica.* [p=0.4] {a}O lucro depende de quanto ela produz, [p=0.2] e em algumas "
        "produções [p=0.2] ele *zera.* [p=0.4] {b}Achar essas produções [p=0.2] é achar as *raízes* de um polinômio. "
        "[p=0.4] {c}E o jeito de achar é como abrir uma porta com um *molho de chaves:* [p=0.2] só *algumas* podem "
        "servir. [p=0.3] {d}Você testa uma por uma."),

    # ================= BLOCO A: O TEOREMA FUNDAMENTAL =================
    dict(id="05", block="tfa", text=
        "{t}Quantas raízes uma equação pode ter? [p=0.4] {a}*Equação polinomial:* [p=0.2] um polinômio *igual a zero.* "
        "[p=0.4] {b}O *teorema fundamental da álgebra* garante: [p=0.2] grau *n* tem *exatamente n raízes.* [p=0.4] "
        "{c}Grau três, [p=0.2] *três* raízes. [p=0.4] {d}Algumas podem ser *reais;* [p=0.2] outras, *complexas,* "
        "[p=0.2] números com a unidade *i,* [p=0.2] assunto da próxima série."),

    # ================= BLOCO B: A FORMA FATORADA =================
    dict(id="06", block="fatorada", text=
        "{t}E como as raízes montam o polinômio? [p=0.4] {a}*Forma fatorada:* [p=0.2] o polinômio escrito como uma "
        "*multiplicação.* [p=0.2] Cada pedaço é um *fator.* [p=0.4] {b}Raízes *menos dois,* [p=0.2] *um* [p=0.2] e "
        "*três:* [p=0.3] {c}x mais dois, [p=0.2] vezes x menos um, [p=0.2] vezes x menos três. [p=0.4] {d}Desenvolva: "
        "[p=0.2] *x ao cubo, menos dois x ao quadrado, menos cinco x, mais seis.* [p=0.3] É o polinômio do gancho."),
    dict(id="07", block="espelho", text=
        "{t}Repare no *sinal.* [p=0.4] {a}A raiz é *menos dois,* [p=0.2] mas o fator é *x mais dois.* [p=0.4] {b}A "
        "raiz é *três,* [p=0.2] e o fator é *x menos três.* [p=0.4] {c}Raiz e fator são *espelhos:* [p=0.2] o sinal "
        "*inverte.* [p=0.4] {d}Faz sentido: [p=0.2] x mais dois só dá *zero* quando x é *menos dois.*"),
    dict(id="08", block="dominante", text=
        "{t}E falta uma peça. [p=0.4] {a}Dois x ao quadrado menos dois [p=0.2] tem raízes *um* e *menos um.* [p=0.4] "
        "{b}Mas o polinômio *não é* x menos um, vezes x mais um. [p=0.3] {c}É *dois* vezes isso. [p=0.4] {d}Na frente "
        "dos fatores [p=0.2] vai o *coeficiente dominante,* [p=0.2] o número do *maior* expoente."),
    dict(id="09", block="atalho_espelho", text=
        "{t}Atalho. [p=0.4] {a}Para escrever o fator, [p=0.2] *troque o sinal* da raiz. [p=0.4] {b}Para conferir, "
        "[p=0.2] ponha a raiz no lugar do x: [p=0.2] o fator tem que dar *zero.* [p=0.4] {c}E não esqueça o número "
        "*da frente.*"),

    # ================= BLOCO C: MULTIPLICIDADE =================
    dict(id="10", block="multiplicidade", text=
        "{t}E se uma raiz aparecer *duas vezes?* [p=0.4] {a}Em x mais um, ao quadrado, vezes x menos três, [p=0.3] "
        "{b}o fator x mais um aparece *duas vezes.* [p=0.4] {c}*Multiplicidade:* [p=0.2] quantas vezes a raiz "
        "aparece. [p=0.2] Menos um é *raiz dupla;* [p=0.2] três é *raiz simples,* [p=0.2] aparece uma vez. [p=0.4] "
        "{d}São *três* raízes contadas, [p=0.2] mas só *dois* valores diferentes."),

    # ================= BLOCO D: AS CANDIDATAS =================
    dict(id="11", block="candidatas", text=
        "{t}Mas quais chaves vale a pena testar? [p=0.4] {a}*Raiz racional:* [p=0.2] uma raiz que é *inteiro* ou "
        "*fração.* [p=0.2] *Candidata:* [p=0.2] um número que *pode* ser raiz. [p=0.4] {b}A regra: [p=0.2] em cima, "
        "um divisor do *termo independente;* [p=0.2] embaixo, um divisor do *coeficiente dominante.* [p=0.4] {c}Termo "
        "independente quatro e dominante três, [p=0.2] por exemplo: [p=0.2] *mais ou menos* um, dois, quatro, "
        "[p=0.2] e um terço, dois terços, quatro terços. [p=0.4] {d}E se o dominante é *um,* [p=0.2] sobram só os "
        "*inteiros* que dividem o termo independente."),

    # ================= BLOCO E: O ROTEIRO DE 4 PASSOS =================
    dict(id="12", block="passo1", text=
        "{t}Vamos ao polinômio do gancho, [p=0.2] em *quatro passos.* [p=0.4] {a}Passo um, [p=0.2] as chaves: "
        "[p=0.2] o dominante é um, [p=0.2] então são os divisores de seis, [p=0.2] *mais ou menos* um, dois, três "
        "e seis. [p=0.4] {b}Passo dois, [p=0.2] testar: [p=0.2] P de um é um, menos dois, menos cinco, mais seis: "
        "[p=0.3] *zero!* [p=0.3] {c}A chave *girou.* [p=0.2] *Um é raiz.*"),
    dict(id="13", block="passo3", text=
        "{t}Passo três: [p=0.2] *derrubar um andar.* [p=0.4] {a}Briot-Ruffini com um, [p=0.2] nos coeficientes um, "
        "menos dois, menos cinco e seis. [p=0.4] {b}Desce o *um.* [p=0.3] Um vezes um, mais menos dois: [p=0.2] *menos "
        "um.* [p=0.3] Um vezes menos um, mais menos cinco: [p=0.2] *menos seis.* [p=0.3] Um vezes menos seis, mais "
        "seis: [p=0.2] *zero,* [p=0.2] o resto. [p=0.4] {c}Sobra *x ao quadrado menos x menos seis.* [p=0.3] O prédio "
        "caiu do terceiro para o *segundo* andar."),
    dict(id="14", block="passo4", text=
        "{t}Passo quatro: [p=0.2] terminar no segundo grau. [p=0.4] {a}Dois números com *soma um* e *produto menos "
        "seis:* [p=0.2] *três* e *menos dois.* [p=0.4] {b}Conferindo no polinômio original: [p=0.2] P de três é vinte e "
        "sete, menos dezoito, menos quinze, mais seis: [p=0.2] *zero.* [p=0.3] P de menos dois: [p=0.2] menos oito, "
        "menos oito, mais dez, mais seis: [p=0.2] *zero.* [p=0.4] {c}Conjunto solução: [p=0.2] *menos dois, um e "
        "três.*"),
    dict(id="15", block="atalho_testes", text=
        "{t}Atalho. [p=0.4] {a}Qual chave testar primeiro? [p=0.2] O *um:* [p=0.2] P de um é só a *soma dos "
        "coeficientes.* [p=0.3] Deu zero, [p=0.2] um é raiz na hora. [p=0.4] {b}Depois, o *menos um:* [p=0.2] troque "
        "o sinal dos termos de grau *ímpar.* [p=0.4] {c}No polinômio do gancho: [p=0.2] menos um, menos dois, mais "
        "cinco, mais seis: [p=0.2] *oito.* [p=0.2] Menos um *não* é raiz."),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Resolva *x ao cubo, menos sete x, mais seis, igual a zero.* [p=0.4] {b}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Soma dos coeficientes: [p=0.2] um, mais *zero,* menos sete, mais seis: [p=0.2] "
        "*zero.* [p=0.2] Um é raiz. [p=0.4] {b}Cuidado: [p=0.2] não tem x ao quadrado, [p=0.2] então entra um *zero* "
        "na esteira: [p=0.2] um, zero, menos sete, seis. [p=0.4] {c}Briot-Ruffini com um: [p=0.2] *um, um, menos "
        "seis,* [p=0.2] e resto zero. [p=0.4] {d}x ao quadrado mais x menos seis: [p=0.2] *dois* e *menos três.* "
        "[p=0.3] Conjunto solução: [p=0.2] *menos três, um e dois.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] raiz e fator têm sinais opostos. [p=0.5] {b}Dois: "
        "[p=0.2] candidatas: [p=0.2] divisores do termo independente sobre divisores do dominante. [p=0.5] {c}Três: "
        "[p=0.2] achou uma raiz, [p=0.2] Briot-Ruffini derruba um grau."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] a raiz *menos dois* virar o fator *x menos dois.* "
        "[p=0.4] {b}Parece certo, [p=0.2] porque a gente *copia* o número que viu. [p=0.4] {c}Mas x menos dois só "
        "zera em *mais dois.* [p=0.2] O fator certo é *x mais dois.*"),
    dict(id="20", block="erros", text=
        "{t}Segundo erro. [p=0.4] {a}*Esquecer o coeficiente dominante:* [p=0.2] escrever dois x ao quadrado menos "
        "dois como x menos um, vezes x mais um. [p=0.4] {b}Parece certo, [p=0.2] porque as *raízes* estão certas. "
        "[p=0.4] {c}Mas esse produto dá x ao quadrado menos um. [p=0.2] Falta o *dois* na frente."),

    # ================= QUESTÃO 3: EU FAÇO =================
    dict(id="21", block="q3", text=
        "{t}Agora, [p=0.2] uma questão no estilo do ENEM. [p=0.4] {a}O lucro de uma pequena fábrica, [p=0.2] em "
        "milhares de reais, [p=0.2] é *L de x igual a x ao cubo, menos seis x ao quadrado, mais onze x, menos seis,* "
        "[p=0.2] com x de zero a quatro centenas de unidades. [p=0.4] {b}O lucro é *nulo* quando x é *um.* [p=0.2] Os "
        "*outros* valores que zeram o lucro são: [p=0.3] {qa}A: dois e três. [p=0.2] {qb}B: menos dois e menos três. "
        "[p=0.2] {qc}C: cinco e seis. [p=0.2] {qd}D: um e seis. [p=0.2] {qe}E: menos um e seis."),
    dict(id="22", block="q3", text=
        "{t}Essa, [p=0.2] *eu faço.* [p=0.4] {a}A chave *um* já foi dada. [p=0.2] Briot-Ruffini com um, [p=0.2] nos "
        "coeficientes um, menos seis, onze e menos seis. [p=0.4] {b}Desce o um. [p=0.2] Um vezes um, menos seis: "
        "[p=0.2] *menos cinco.* [p=0.2] Um vezes menos cinco, mais onze: [p=0.2] *seis.* [p=0.2] Um vezes seis, menos "
        "seis: [p=0.2] *zero.* [p=0.4] {c}Sobra x ao quadrado menos cinco x mais seis: [p=0.2] soma cinco, produto "
        "seis: [p=0.2] *dois* e *três.* [p=0.4] {d}Confiro: [p=0.2] L de dois e L de três dão *zero.* [p=0.3] "
        "{ok}*Letra A!*"),
    dict(id="23", block="q3", text=
        "{t}E as armadilhas? [p=0.3] {xb}A B troca os *sinais* das raízes ao ler os fatores. [p=0.4] {xc}A C lê os "
        "*coeficientes* do quociente, [p=0.2] cinco e seis, [p=0.2] como se fossem raízes. [p=0.4] {xd}A D erra a "
        "primeira soma da esteira: [p=0.2] *menos sete* [p=0.2] no lugar de menos cinco. [p=0.4] {xe}E a E troca o "
        "sinal do *seis* [p=0.2] e resolve x ao quadrado menos cinco x, *menos* seis."),

    # ================= QUESTÃO 7: VOCÊ FAZ =================
    dict(id="24", block="q7", text=
        "{t}Agora, [p=0.2] *você faz.* [p=0.4] {a}Um estudante listou as possíveis raízes racionais de *dois x ao cubo, "
        "menos três x ao quadrado, menos três x, mais dois, igual a zero,* [p=0.2] e testou cada uma. [p=0.3] O "
        "conjunto solução é: [p=0.3] {qa}A: menos dois, menos um meio e um. [p=0.2] {qb}B: menos um e dois. [p=0.2] "
        "{qc}C: menos dois, menos um, um e dois. [p=0.2] {qd}D: um meio, um e dois. [p=0.2] {qe}E: menos um, um meio "
        "e dois. [p=0.4] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="25", block="q7", text=
        "{t}Vamos conferir. [p=0.3] {a}As chaves: [p=0.2] em cima, divisores de *dois;* [p=0.2] embaixo, divisores de "
        "*dois.* [p=0.2] *Mais ou menos* um, dois e um meio. [p=0.4] {b}P de um: [p=0.2] *menos dois.* [p=0.2] Não "
        "gira. [p=0.3] P de menos um: [p=0.2] menos dois, menos três, mais três, mais dois: [p=0.2] *zero!* [p=0.4] "
        "{c}Briot-Ruffini com menos um: [p=0.2] *dois, menos cinco, dois,* [p=0.2] e resto zero. [p=0.4] {d}Dois x ao "
        "quadrado menos cinco x mais dois: [p=0.2] delta é vinte e cinco menos dezesseis, *nove.* [p=0.2] Cinco mais ou "
        "menos três, sobre quatro: [p=0.2] *dois* e *um meio.* [p=0.3] {ok}*Letra E!*"),
    dict(id="26", block="q7", text=
        "{t}E as outras? [p=0.3] {xa}A A troca os sinais de *todas* as raízes. [p=0.4] {xb}A B testa só os *inteiros* "
        "e para: [p=0.2] mas grau três tem *três* raízes. [p=0.4] {xc}A C lista candidatas *sem testar:* [p=0.2] P de um "
        "dá menos dois, [p=0.2] e P de menos dois dá menos vinte. [p=0.4] {xd}E a D põe o *um,* [p=0.2] que não é raiz, "
        "[p=0.2] e perde o menos um."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="27", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] raiz e fator têm sinais opostos. [p=0.5] "
        "{b}Dois: [p=0.2] candidatas: [p=0.2] divisores do termo independente sobre divisores do dominante. [p=0.5] "
        "{c}Três: [p=0.2] achou uma raiz, [p=0.2] Briot-Ruffini derruba um grau."),

    # ================= PONTE E CTA =================
    dict(id="28", block="ponte", text=
        "{a}As arestas de um *bloco retangular* [p=0.2] são as raízes de *dois x ao cubo, menos quatorze x ao "
        "quadrado, mais vinte e oito x, menos dezesseis, igual a zero.* [p=0.5] {b}Dá para achar o *volume* sem "
        "descobrir nenhuma aresta? [p=0.4] {c}Dá. [p=0.3] *Próximo episódio.*"),
    dict(id="29", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual chave você testa primeiro? [p=0.5] "
        "{anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no "
        "*Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
