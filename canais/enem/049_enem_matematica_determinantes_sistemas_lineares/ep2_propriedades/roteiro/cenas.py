# Roteiro — Determinantes e Sistemas Lineares, Episódio 2 de 5: propriedades que poupam conta
# Base: Estudos/Enem/estudos/01-matematica/34-determinantes-sistemas-lineares.html — seção 04 + Questões 8 e 3 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   LINHAS PARENTES: iguais, proporcionais ou uma feita das outras zeram o determinante — é informação repetida.
#   OS BOTÕES DE VOLUME: cada linha é um botão; girar UM botão ×k multiplica o det por k; a matriz INTEIRA ×k gira os
#     n botões, e o det vai a k^n.
#   O ESPELHO: trocar duas linhas de lugar mantém o valor e troca o sinal.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Revisão rápida: Sarrus (ep. 1), lei de formação a_ij (série de Matrizes), 2³ = 8.
# Blocos = seção 04. O bloco b usa a matriz (1 0 −1 / 3 2 1 / 5 4 3), como o prompt pede (é a Q8, "eu faço").
#   A confirmação por Sarrus dessa matriz fica SÓ na resolução da Q8 (o prompt pedia nos dois lugares; evitar a mesma
#   conta duas vezes num vídeo de 6–8 min).
# Exemplos NOSSOS (marcados), para não entregar a Questão 3 ("você faz", det A = 5 → det(2A) = 40):
#   bloco c: uma matriz com det 7 → trocar linhas dá −7; uma linha × 3 dá 21;
#   bloco d e erro clássico: 3 × 3 com det A = 7 → det(2A) = 2³ · 7 = 56 (o erro dá 14); a animação dos três botões
#     (contador 7 → 14 → 28 → 56) fica no bloco d; o contador 5 → 10 → 20 → 40 aparece só na resolução da Q3.
#   bloco e: a triangular (2 9 4 / 0 5 7 / 0 0 1) → 2 · 5 · 1 = 10 (diferente do "nós fazemos").
#   O gancho do usuário (mantido igual) já diz "5 → 40": a Q3 vira reforço; o novo nela são as alternativas erradas.
# Nós fazemos (prompt): (3 7 1 / 0 2 5 / 0 0 4) → 3 · 2 · 4 = 24; 2 × 2 com det 3 → det(3A) = 3² · 3 = 27.
# Acréscimos NOSSOS (marcados): cena verde de ATALHO "antes de qualquer Sarrus, pergunte: tem alguma propriedade
#   aqui?" (zeros · linhas parentes · triangular) e cena verde "triangular: multiplique a diagonal".
# QUESTÃO 8 (eu faço): a_ij = 2i − j → (1 0 −1 / 3 2 1 / 5 4 3); cada linha é a anterior + (2, 2, 2) → L3 = 2L2 − L1 →
#   det = 0 (C). Sarrus: descendo 6 + 0 − 12 = −6; subindo −10 + 4 + 0 = −6; −6 − (−6) = 0. Erradas = material
#   (B −6 só a parte que desce; A −12 soma as duas partes; D 6 usa só a parte que sobe com o menos; E 12 soma as duas e
#   troca o sinal).
# QUESTÃO 3 (você faz): det(2A) = 2³ · 5 = 40 (D). A 10 = uma linha só; B 20 = 2², como se fosse 2 × 2; C 30 = vezes 2
#   e vezes a ordem 3; E 125 = 5³.
# Frases-chave (meio e fim, idênticas): 1. Linhas parentes zeram o determinante.
#   2. Matriz inteira vezes k: o determinante vai vezes k elevado a n. 3. Triangular: multiplique a diagonal.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Propriedades do determinante: a resposta sem fazer Sarrus · Matemática ENEM, Determinantes episódio 2"

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
        "{a}Uma matriz *três por três* [p=0.2] tem determinante *cinco.* [p=0.4] {b}Dobre *todos* os números dela. "
        "[p=0.4] {c}O novo determinante é *dez?* [p=0.5] {d}Não: [p=0.3] é *quarenta.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o segundo episódio da série de *Determinantes e sistemas lineares.* [p=0.4] {a}Ao final, [p=0.2] "
        "você vai reconhecer *em segundos* [p=0.2] quando o determinante é *zero* [p=0.4] {b}e *quanto ele muda* "
        "[p=0.2] quando a matriz muda, [p=0.2] *sem fazer Sarrus.*"),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes. [p=0.3] {a}Do episódio um: [p=0.2] no *Sarrus,* [p=0.2] as três diagonais que *descem* "
        "[p=0.2] menos as três que *sobem.* [p=0.4] {b}Da série de Matrizes: [p=0.2] *a, i, j* é a casa da linha i, "
        "coluna j; [p=0.2] a lei de formação diz o que pôr em cada casa. [p=0.4] {c}E *dois ao cubo* [p=0.2] é dois "
        "vezes dois vezes dois: [p=0.2] *oito.*"),

    # ================= CONCRETO =================
    dict(id="04", block="planilha", text=
        "{t}Imagine uma planilha de três linhas. [p=0.4] {a}A segunda linha é *cópia* da primeira. [p=0.4] {b}Ela "
        "trouxe alguma informação nova? [p=0.3] *Nenhuma.* [p=0.4] {c}Para o determinante, [p=0.2] informação "
        "repetida [p=0.2] *vale zero.*"),

    # ================= BLOCO A: ZERO NA HORA =================
    dict(id="05", block="zero", text=
        "{t}Quando o determinante é zero *sem conta nenhuma?* [p=0.4] {a}Primeiro: [p=0.2] uma linha, ou coluna, "
        "[p=0.2] *só de zeros.* [p=0.4] {b}Segundo: [p=0.2] duas linhas *iguais* [p=0.2] ou *proporcionais.* [p=0.4] "
        "{c}*Linhas proporcionais:* [p=0.2] uma é a outra [p=0.2] *vezes um número.* [p=0.3] Um, dois, três [p=0.2] e "
        "dois, quatro, seis: [p=0.2] *vezes dois.* [p=0.4] {d}São *linhas parentes:* [p=0.2] informação repetida."),

    # ================= BLOCO B: UMA LINHA FEITA DAS OUTRAS =================
    dict(id="06", block="combinacao", text=
        "{t}E se o parentesco estiver *escondido?* [p=0.4] {a}*Combinação de linhas:* [p=0.2] uma linha montada com "
        "as outras, [p=0.2] somando e multiplicando. [p=0.4] {b}Olhe: [p=0.2] um, zero, menos um; [p=0.2] três, "
        "dois, um; [p=0.2] cinco, quatro, três. [p=0.4] {c}Cada linha é a anterior [p=0.2] *mais dois, dois, dois.* "
        "[p=0.4] {d}Então a terceira [p=0.2] é *duas vezes a segunda menos a primeira.* [p=0.4] {e}Linha parente: "
        "[p=0.2] *determinante zero,* [p=0.2] sem conta."),
    dict(id="07", block="atalho_prop", text=
        "{t}Atalho. [p=0.4] {a}Antes de qualquer Sarrus, [p=0.2] pergunte em voz alta: [p=0.2] *tem alguma "
        "propriedade aqui?* [p=0.4] {b}Linha de zeros? [p=0.2] Linhas parentes? [p=0.2] Zeros embaixo da diagonal? "
        "[p=0.4] {c}Se tiver, [p=0.2] a conta *encolhe* ou *some.*"),

    # ================= BLOCO C: O ESPELHO E O BOTÃO =================
    dict(id="08", block="espelho", text=
        "{t}E o que *muda* o valor? [p=0.4] {a}Pegue uma matriz com determinante *sete.* [p=0.4] {b}Troque duas "
        "linhas de lugar. [p=0.3] É como virar no *espelho:* [p=0.4] {c}o valor fica, [p=0.2] o sinal troca. "
        "[p=0.2] *Menos sete.*"),
    dict(id="09", block="botao", text=
        "{t}Agora pense num *aparelho de som* [p=0.2] com um botão de volume para cada linha. [p=0.4] {a}Gire *um* "
        "botão, [p=0.2] vezes três: [p=0.2] multiplicar *uma linha* por três. [p=0.4] {b}O determinante vai *vezes "
        "três:* [p=0.2] de sete [p=0.2] para *vinte e um.*"),

    # ================= BLOCO D: A ARMADILHA DO kA =================
    dict(id="10", block="kA", text=
        "{t}E se você dobrar a matriz *inteira?* [p=0.4] {a}*Ordem n:* [p=0.2] o número de linhas da matriz "
        "quadrada. [p=0.2] Numa três por três, [p=0.2] *n é três.* [p=0.4] {b}Dobrar a matriz inteira [p=0.2] é "
        "girar *os três botões.* [p=0.4] {c}Primeiro botão: [p=0.2] sete vira *catorze.* [p=0.3] Segundo: [p=0.2] "
        "*vinte e oito.* [p=0.3] Terceiro: [p=0.2] *cinquenta e seis.* [p=0.4] {d}É *dois ao cubo* [p=0.2] vezes "
        "sete. [p=0.3] Determinante de k A [p=0.2] é *k elevado a n* [p=0.2] vezes o determinante de A."),

    # ================= BLOCO E: O QUE NÃO MUDA E A TRIANGULAR =================
    dict(id="11", block="nao_muda", text=
        "{t}E o que *não muda?* [p=0.4] {a}Somar a uma linha [p=0.2] um múltiplo de outra: [p=0.2] *não muda.* "
        "[p=0.4] {b}*Transposta:* [p=0.2] a matriz com as linhas viradas colunas. [p=0.2] Mesmo determinante. "
        "[p=0.4] {c}E o determinante de A vezes B [p=0.2] é o de A [p=0.2] *vezes* o de B."),
    dict(id="12", block="triangular", text=
        "{t}E o atalho mais bonito. [p=0.4] {a}*Matriz triangular:* [p=0.2] só zeros *abaixo* da diagonal "
        "principal. [p=0.2] *Diagonal:* [p=0.2] zeros em todo lugar *fora* dela. [p=0.4] {b}Nas duas, [p=0.2] o "
        "determinante é o *produto da diagonal.* [p=0.4] {c}Dois, cinco, um: [p=0.2] *dez.* [p=0.2] Sem Sarrus."),

    # ================= NÓS FAZEMOS =================
    dict(id="13", block="exercicio", text=
        "{t}Sua vez, [p=0.2] duas perguntas. [p=0.3] {a}Quanto vale o determinante de [p=0.2] três, sete, um; "
        "[p=0.2] zero, dois, cinco; [p=0.2] zero, zero, quatro? [p=0.4] {b}E, [p=0.2] se uma matriz *dois por dois* "
        "tem determinante três, [p=0.2] quanto vale o de *três A?* [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="14", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Zeros embaixo da diagonal: [p=0.2] *triangular.* [p=0.2] Três vezes dois vezes "
        "quatro: [p=0.2] *vinte e quatro.* [p=0.4] {b}Agora, [p=0.2] dois por dois: [p=0.2] *n é dois.* [p=0.3] "
        "Três ao quadrado, [p=0.2] nove, [p=0.2] vezes três: [p=0.2] *vinte e sete.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="15", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] linhas parentes zeram o determinante. [p=0.5] "
        "{b}Dois: [p=0.2] matriz inteira vezes k: [p=0.2] o determinante vai vezes k elevado a n. [p=0.5] {c}Três: "
        "[p=0.2] triangular: [p=0.2] multiplique a diagonal."),

    # ================= ERRO CLÁSSICO =================
    dict(id="16", block="erros", text=
        "{t}Agora, o erro clássico. [p=0.4] {a}Dizer que o determinante de dois A [p=0.2] é *duas vezes* o de A: "
        "[p=0.2] sete vira *catorze.* [p=0.4] {b}Parece certo, [p=0.2] porque com *números* [p=0.2] dobrar tudo "
        "dobra o resultado. [p=0.4] {c}Mas cada linha é um botão, [p=0.2] e são *três.* [p=0.2] O fator é *oito:* "
        "[p=0.2] *cinquenta e seis.*"),

    # ================= QUESTÃO 8: EU FAÇO =================
    dict(id="17", block="q8", text=
        "{t}Agora, [p=0.2] uma questão no estilo do ENEM. [p=0.4] {a}A matriz quadrada A, de ordem três, [p=0.2] "
        "é definida por *a, i, j igual a dois i menos j.* [p=0.4] {b}O determinante de A é: [p=0.3] {qa}A: menos "
        "doze. [p=0.2] {qb}B: menos seis. [p=0.2] {qc}C: zero. [p=0.2] {qd}D: seis. [p=0.2] {qe}E: doze."),
    dict(id="18", block="q8", text=
        "{t}Essa, [p=0.2] *eu faço.* [p=0.4] {a}Primeiro, monto a matriz. [p=0.2] Linha um: [p=0.2] dois menos um, "
        "*um;* [p=0.2] dois menos dois, *zero;* [p=0.2] dois menos três, *menos um.* [p=0.4] {b}Linha dois: [p=0.2] "
        "*três, dois, um.* [p=0.3] Linha três: [p=0.2] *cinco, quatro, três.* [p=0.4] {c}Tem propriedade aqui? "
        "[p=0.3] *Tem:* [p=0.2] cada linha é a anterior mais dois, dois, dois. [p=0.4] {d}Linha parente: [p=0.2] "
        "determinante *zero.* [p=0.3] {ok}*Letra C!*"),
    dict(id="19", block="q8", text=
        "{t}Confiro por Sarrus. [p=0.4] {a}As que descem: [p=0.2] seis, mais zero, menos doze: [p=0.2] *menos seis.* "
        "[p=0.4] {b}As que sobem: [p=0.2] menos dez, mais quatro, mais zero: [p=0.2] *menos seis.* [p=0.4] {c}Menos "
        "seis *menos* menos seis: [p=0.2] *zero.* [p=0.3] Confere."),
    dict(id="20", block="q8", text=
        "{t}E as armadilhas? [p=0.3] {xb}A B fica só com a parte que *desce.* [p=0.4] {xa}A A *soma* as duas partes, "
        "[p=0.2] em vez de subtrair. [p=0.4] {xd}A D usa só a parte que *sobe,* [p=0.2] com o sinal de menos. "
        "[p=0.4] {xe}E a E soma as duas [p=0.2] e ainda *troca o sinal.*"),

    # ================= QUESTÃO 3: VOCÊ FAZ =================
    dict(id="21", block="q3", text=
        "{t}Agora, [p=0.2] *você faz.* [p=0.4] {a}Uma matriz A, de ordem três, [p=0.2] tem determinante *cinco.* "
        "[p=0.2] Um programa gera *dois A,* [p=0.2] multiplicando todos os elementos por dois. [p=0.4] {b}O "
        "determinante de dois A é: [p=0.3] {qa}A: dez. [p=0.2] {qb}B: vinte. [p=0.2] {qc}C: trinta. [p=0.2] {qd}D: "
        "quarenta. [p=0.2] {qe}E: cento e vinte e cinco. [p=0.4] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="22", block="q3", text=
        "{t}Vamos conferir. [p=0.3] {a}Matriz inteira, [p=0.2] ordem três: [p=0.2] *três botões.* [p=0.3] Cinco, "
        "dez, vinte, [p=0.2] *quarenta.* [p=0.3] Dois ao cubo vezes cinco. [p=0.3] {ok}*Letra D!* [p=0.4] {xa}A A "
        "gira *um botão só.* [p=0.3] {xb}A B usa dois ao *quadrado,* [p=0.2] como se fosse dois por dois. [p=0.3] "
        "{xc}A C multiplica por dois [p=0.2] e pela *ordem três.* [p=0.3] {xe}E a E eleva o *cinco* ao cubo."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="23", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] linhas parentes zeram o determinante. [p=0.5] "
        "{b}Dois: [p=0.2] matriz inteira vezes k: [p=0.2] o determinante vai vezes k elevado a n. [p=0.5] {c}Três: "
        "[p=0.2] triangular: [p=0.2] multiplique a diagonal."),

    # ================= PONTE E CTA =================
    dict(id="24", block="ponte", text=
        "{a}O determinante *diferente de zero* [p=0.2] garante que a matriz tem *inversa.* [p=0.4] {b}Num problema "
        "de *ingressos,* [p=0.2] ele garante o quê? [p=0.4] {c}Que existe *uma única resposta.* [p=0.4] {d}E ele "
        "ainda *calcula* essa resposta: [p=0.2] *regra de Cramer,* [p=0.2] próximo episódio."),
    dict(id="25", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você teria respondido dez no gancho? [p=0.5] "
        "{anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no "
        "*Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
