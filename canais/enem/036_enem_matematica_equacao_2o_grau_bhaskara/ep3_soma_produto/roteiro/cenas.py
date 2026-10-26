# Roteiro — Equação do 2º Grau e Fórmula de Bhaskara, Episódio 3 de 6: soma e produto (raízes de cabeça e a equação a
#   partir das raízes).
# Base: Estudos/Enem/estudos/01-matematica/21-equacao-2o-grau-bhaskara.html — seção 06 + Questões 3 e 4 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O JOGO DOS DOIS NÚMEROS: em x² − Sx + P = 0, procure dois números de soma S e produto P (duas cartas viradas com "?").
#   O SINAL DO MEIO VEM TROCADO: na equação aparece −7x, mas a soma é +7.
#   O PRODUTO ENTREGA OS SINAIS (o semáforo): produto negativo, uma raiz de cada lado do zero; produto positivo, as duas do
#   mesmo lado, e a soma diz qual.
# Frases do usuário mantidas IGUAIS: gancho, promessa ("Ao final, ..."), as 3 frases-chave e a ponte.
# Exemplos (todos conferidos em trabalho/conferir_contas.py):
#   Concreto: soma 7, produto 10 → 2 e 5 → x² − 7x + 10 = 0. Tabela da seção 06: x² + x − 12 (S −1, P −12 → 3 e −4) ·
#   x² + 8x + 15 (S −8, P 15 → −3 e −5) · 2x² − 7x + 3 (S 7/2, P 3/2 → 3 e 1/2). Caminho inverso (do prompt): 3 e −5 →
#   x² + 2x − 15 (é a Questão 3, que é "eu faço": repetir é permitido). Forma fatorada: 2(x − 3)(x − 1/2) = (x − 3)(2x − 1).
#   Quando desistir (NOSSO): x² − 3x − 5 (pares de produto −5: 5 e −1, soma 4; −5 e 1, soma −4 → nenhum dá 3; Δ = 29).
#   Erro 2 (NOSSO, usa o "nós fazemos" já resolvido): raízes 2 e 6 montadas com +Sx → x² + 8x + 12, raízes −2 e −6.
#   Erro 3 (NOSSO): x² − 6x + 4 (pares de produto 4: 1 e 4, soma 5; 2 e 2, soma 4 → nenhum; Δ = 20, raízes 3 ± √5).
#   A ANIMAÇÃO da bola (cartas "soma 4, produto 3" e a linha do tempo 1 s / 3 s) só aparece na resolução da Questão 4,
#   depois da pausa, para não entregar a "você faz". O gancho cita a bola sem dar os instantes.
# Nós fazemos (prompt): x² − x − 20 → S = 1, P = −20 → 5 e −4 · raízes 2 e 6 → S 8, P 12 → x² − 8x + 12 = 0.
# QUESTÃO 3 (eu faço, texto idêntico): S = −2, P = −15 → x² + 2x − 15 = 0 → D; forma fatorada (x − 3)(x + 5).
#   Erradas (do material e do prompt): A usa +Sx (raízes −3 e 5) · B erra o sinal do produto (Δ = −56, sem raiz real) ·
#   C usa as raízes 3 e 5 · E troca soma e produto.
# QUESTÃO 4 (você faz, texto idêntico): 20t − 5t² = 15 → 5t² − 20t + 15 = 0 → t² − 4t + 3 = 0 → 1 e 3 → 2 s → B.
#   Teste t = 2: 40 − 20 = 20 m. Erradas (do material): A e C respondem um instante só; D é o voo inteiro (h = 0 em t = 4);
#   E é falsa (em t = 2 a bola está a 20 m). Altura máxima: só citada como assunto da série de Função Quadrática.
# Acréscimos nossos (verde): "comece pelo produto, depois escolha a soma"; "a ≠ 1? as relações valem com −b/a e c/a";
#   o semáforo dos sinais elimina alternativas; "confira multiplicando e somando".
# Frases-chave (meio e fim, idênticas): 1. Soma é −b/a; produto é c/a. 2. Dois números de soma S e produto P.
#   3. Raízes dadas: x² − Sx + P = 0.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Soma e produto: raízes de cabeça sem Bhaskara | Bhaskara Ep. 3"
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
        "{a}Uma bola passa pelos *quinze metros* de altura *duas vezes:* [p=0.2] {b}uma subindo [p=0.2] e outra descendo. "
        "[p=0.4] {c}Descobrir esses dois instantes leva *três segundos,* [p=0.2] sem Bhaskara, [p=0.2] {d}se você conhecer "
        "*o jogo dos dois números.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai achar *raízes de cabeça,* [p=0.3] {b}saber os *sinais* delas sem resolver [p=0.3] "
        "{c}e *montar a equação* a partir das raízes."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Da série de Expressões Algébricas: [p=0.2] *x ao quadrado, mais "
        "cinco x, mais seis* [p=0.2] é *x mais dois, vezes, x mais três:* [p=0.2] dois e três somam cinco e multiplicam "
        "seis. [p=0.4] {b}E do episódio um, o *produto nulo:* [p=0.2] se uma multiplicação deu zero, "
        "[p=0.2] alguém ali é zero."),

    # ================= CONCRETO: O JOGO =================
    dict(id="04", block="jogo", text=
        "{t}Uma adivinhação. [p=0.3] {a}Pensei em *dois números.* [p=0.3] {b}Somados, dão *sete.* [p=0.3] "
        "{c}Multiplicados, dão *dez.* [p=0.4] {d}Quais são? [p=1.2] {e}*Dois e cinco!* [p=0.2] Dois mais cinco, sete; "
        "[p=0.2] dois vezes cinco, dez."),
    dict(id="05", block="jogo", text=
        "{t}E a equação? [p=0.4] {a}Olhe *x ao quadrado, menos sete x, mais dez, igual a zero.* [p=0.4] {b}Troque o x "
        "por dois: [p=0.2] quatro, menos catorze, mais dez: [p=0.2] *zero.* [p=0.3] {c}Por cinco, [p=0.2] também *zero.* "
        "[p=0.4] {d}Os dois números do jogo [p=0.2] são as *raízes* da equação."),
    dict(id="06", block="relacoes", text=
        "{t}Coincidência? [p=0.4] {a}Não. [p=0.2] Chame as raízes de *x um* e *x dois.* [p=0.3] {b}A *soma das "
        "raízes* é x um mais x dois. [p=0.2] Ela vale *menos b sobre a.* [p=0.4] {c}O *produto das raízes* é x um vezes "
        "x dois. [p=0.2] Ele vale *c sobre a.* [p=0.4] {d}Essas duas fórmulas têm nome: [p=0.2] *relações de Girard.* "),
    dict(id="07", block="relacoes", text=
        "{t}E quando o a é um? [p=0.4] {a}A equação fica *x ao quadrado, menos S x, mais P, igual a zero.* [p=0.4] "
        "{b}Em x ao quadrado, menos sete x, mais dez: [p=0.2] *o sinal do meio vem trocado.* [p=0.2] Na equação aparece "
        "*menos sete,* [p=0.2] mas a soma é *mais sete.* [p=0.4] {c}E o último número é o produto: [p=0.2] "
        "dez."),
    dict(id="08", block="relacoes", text=
        "{a}*Atalho:* [p=0.2] comece pelo *produto.* [p=0.3] {b}Pares que dão dez: [p=0.2] um e dez, [p=0.2] dois e "
        "cinco. [p=0.4] {c}Qual *soma* sete? [p=0.2] Dois e cinco. [p=0.4] {d}E confira: [p=0.2] multiplique e some."),

    # ================= BLOCO B: A TABELA =================
    dict(id="09", block="tabela", text=
        "{t}E com sinais negativos? [p=0.4] {a}*x ao quadrado, mais x, menos doze.* [p=0.3] {b}A soma é *menos um,* "
        "[p=0.2] o sinal do meio trocado. [p=0.2] O produto é *menos doze.* [p=0.4] {c}Dois números que multiplicam menos "
        "doze [p=0.2] e somam menos um: [p=0.2] *três e menos quatro.*"),
    dict(id="10", block="tabela", text=
        "{a}*x ao quadrado, mais oito x, mais quinze.* [p=0.3] {b}Soma *menos oito,* [p=0.2] produto *quinze.* [p=0.4] "
        "{c}Produto positivo e soma negativa: [p=0.2] *menos três e menos cinco.*"),
    dict(id="11", block="tabela", text=
        "{t}E quando o a não é um? [p=0.4] {a}*Dois x ao quadrado, menos sete x, mais três.* [p=0.3] {b}Soma, menos b "
        "sobre a: [p=0.2] *sete meios.* [p=0.2] Produto, c sobre a: [p=0.2] *três meios.* [p=0.4] {c}As raízes: [p=0.2] "
        "*três e um meio.* [p=0.3] {d}Some e multiplique: [p=0.2] *bate.*"),

    # ================= BLOCO C: OS SINAIS =================
    dict(id="12", block="sinais", text=
        "{t}E dá para saber os sinais das raízes *sem resolver?* [p=0.4] {a}Dá. [p=0.2] *O produto entrega os sinais.* "
        "[p=0.4] {b}Produto *negativo:* [p=0.2] um número positivo vezes um negativo. [p=0.2] *Uma raiz de cada lado do "
        "zero.*"),
    dict(id="13", block="sinais", text=
        "{a}Produto *positivo:* [p=0.2] as duas do *mesmo lado.* [p=0.3] {b}E a soma diz qual. [p=0.2] Soma positiva: "
        "[p=0.2] *as duas positivas.* [p=0.4] {c}Soma negativa: [p=0.2] *as duas negativas.*"),
    dict(id="14", block="sinais", text=
        "{a}*Atalho de prova:* [p=0.2] se as raízes têm sinais opostos, [p=0.2] *risque* toda alternativa com as duas "
        "positivas. [p=0.2] {b}Antes de qualquer conta."),

    # ================= BLOCO D: O CAMINHO INVERSO =================
    dict(id="15", block="inverso", text=
        "{t}E se a questão der as raízes [p=0.2] e pedir a equação? [p=0.4] {a}Raízes *três e menos cinco.* [p=0.3] "
        "{b}Soma: [p=0.2] *menos dois.* [p=0.2] Produto: [p=0.2] *menos quinze.* "
        " [p=0.4] {c}Encaixe em *x ao quadrado, menos S x, mais P:* [p=0.2] menos, menos dois x, "
        "[p=0.2] vira *mais dois x.* [p=0.4] {d}Resultado: [p=0.2] *x ao quadrado, mais dois x, menos quinze, igual a "
        "zero.*"),

    # ================= BLOCO E: A FORMA FATORADA =================
    dict(id="16", block="fatorada", text=
        "{t}Existe outro caminho? [p=0.4] {a}A *forma fatorada:* [p=0.2] escrever a equação como *multiplicação,* "
        "[p=0.2] usando as raízes. [p=0.3] {b}É *a, vezes, x menos x um, vezes, x menos x dois.* [p=0.4] {c}Em dois x ao "
        "quadrado, menos sete x, mais três: [p=0.2] *dois, vezes, x menos três, vezes, x menos um meio.* [p=0.4] {d}O dois "
        "entra no último parêntese: [p=0.2] *x menos três, vezes, dois x menos um.* [p=0.3] {e}Pelo produto nulo: [p=0.2] "
        "três e um meio."),

    # ================= BLOCO F: QUANDO DESISTIR =================
    dict(id="17", block="desistir", text=
        "{t}E quando o jogo não funciona? [p=0.4] {a}*x ao quadrado, menos três x, menos cinco:* [p=0.2] soma três, "
        "[p=0.2] produto menos cinco. [p=0.4] {b}Cinco e menos um somam quatro; [p=0.2] menos cinco e um, menos quatro. "
        "[p=0.2] *Nenhum* par dá três. [p=0.4] {c}Se o par não aparece *em poucos segundos,* [p=0.2] *vá para Bhaskara.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Ache de cabeça as raízes de *x ao quadrado, menos x, menos vinte, igual a zero.* [p=0.4] "
        "{b}E monte a equação de raízes *dois e seis.* [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Soma *um,* [p=0.2] o sinal do meio trocado; [p=0.2] produto *menos vinte:* [p=0.2] "
        "sinais opostos. [p=0.4] {b}*Cinco e menos quatro.* [p=0.4] {c}Agora, raízes dois e seis: [p=0.2] soma *oito,* "
        "produto *doze.* [p=0.4] {d}*x ao quadrado, menos oito x, mais doze, igual a zero.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] soma é menos b sobre a; [p=0.2] produto é c sobre a. "
        "[p=0.5] {b}Dois: [p=0.2] dois números de soma S e produto P. [p=0.5] {c}Três: [p=0.2] raízes dadas: [p=0.2] x "
        "ao quadrado, menos S x, mais P, igual a zero."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] soma das raízes igual a *b sobre a.* [p=0.2] Em "
        "x ao quadrado, menos sete x, mais dez, [p=0.2] daria *menos sete.* [p=0.4] {b}Parece certo: [p=0.2] o número "
        "escrito é o menos sete. [p=0.4] {c}Mas a soma é *menos b sobre a:* [p=0.2] *mais sete.*"),
    dict(id="22", block="erros", text=
        "{a}Segundo: [p=0.2] montar a equação com *mais S x.* [p=0.2] Raízes dois e seis [p=0.2] viram *x ao quadrado, "
        "mais oito x, mais doze.* [p=0.4] {b}Parece certo: [p=0.2] a soma é mesmo oito. [p=0.4] {c}Mas essa "
        "equação tem raízes *menos dois e menos seis.* [p=0.2] O certo é *menos S x:* [p=0.2] menos oito x."),
    dict(id="23", block="erros", text=
        "{a}Terceiro: [p=0.2] insistir no jogo quando as raízes *não são inteiras,* [p=0.2] como em x ao quadrado, "
        "menos seis x, mais quatro. [p=0.4] {b}Parece certo: [p=0.2] o jogo funcionou nos outros exemplos. [p=0.4] {c}Mas um e quatro somam cinco, [p=0.2] dois e dois somam quatro. [p=0.2] Nenhum par serve: "
        "[p=0.2] *Bhaskara,* [p=0.2] e as raízes são *três mais ou menos raiz de cinco.*"),

    # ================= QUESTÃO 3 (EU FAÇO) =================
    dict(id="24", block="q3", text=
        "{t}Uma questão do nosso material. [p=0.2] *Eu faço com você.* [p=0.4] {a}Um "
        "professor pediu aos alunos uma equação do segundo grau, [p=0.2] com coeficiente de x ao quadrado igual a um, "
        "[p=0.2] cujas raízes fossem *três e menos cinco.* [p=0.2] A equação correta é: [p=0.4] {qa}A: [p=0.2] x ao "
        "quadrado, menos dois x, menos quinze. [p=0.3] {qb}B: [p=0.2] x ao quadrado, mais dois x, mais quinze. [p=0.3] "
        "{qc}C: [p=0.2] x ao quadrado, menos oito x, mais quinze. [p=0.3] {qd}D: [p=0.2] x ao quadrado, mais dois x, "
        "menos quinze. [p=0.3] {qe}E: [p=0.2] x ao quadrado, mais quinze x, menos dois. [p=0.4] {p}*Pause o vídeo e "
        "tente.* [p=2.0]"),
    dict(id="25", block="q3", text=
        "{t}Vamos lá. [p=0.3] {a}É o *caminho inverso:* [p=0.2] soma *menos dois,* [p=0.2] produto *menos quinze.* [p=0.4] "
        "{b}x ao quadrado, menos S x, mais P: [p=0.2] *x ao quadrado, mais dois x, menos quinze.* [p=0.4] {c}Confira pela "
        "forma fatorada: [p=0.2] *x menos três, vezes, x mais cinco* [p=0.2] dá exatamente isso. [p=0.3] {ok}*Letra D!*"),
    dict(id="26", block="q3", text=
        "{t}E as erradas? [p=0.3] {xa}A A usa *mais S x:* [p=0.2] as raízes dela são menos três e cinco. [p=0.4] {xb}A B "
        "erra o sinal do produto: [p=0.2] *não tem raiz real.* [p=0.4] {xc}A C usa as raízes *três e cinco,* [p=0.2] sem o "
        "menos. [p=0.4] {xe}E a E *troca* a soma pelo produto."),

    # ================= QUESTÃO 4 (VOCÊ FAZ) =================
    dict(id="27", block="q4", text=
        "{t}E a bola do começo da aula. [p=0.2] *Você faz.* [p=0.4] {a}Uma bola é lançada verticalmente para cima, "
        "[p=0.2] e sua altura, em metros, [p=0.2] t segundos após o lançamento, [p=0.2] é dada por *h igual a vinte t, "
        "menos cinco t ao quadrado.* [p=0.3] Durante quanto tempo [p=0.2] a bola permanece *acima de quinze metros* de "
        "altura? [p=0.4] {qa}A: [p=0.2] um segundo. [p=0.3] {qb}B: [p=0.2] dois segundos. [p=0.3] {qc}C: [p=0.2] três "
        "segundos. [p=0.3] {qd}D: [p=0.2] quatro segundos. [p=0.3] {qe}E: [p=0.2] nenhum: a bola não chega a quinze "
        "metros. [p=0.4] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="28", block="q4", text=
        "{t}Vamos conferir. [p=0.3] {a}Iguale a altura a quinze: [p=0.2] *vinte t, menos cinco t ao quadrado, igual a "
        "quinze.* [p=0.4] {b}Arrume e troque os sinais: [p=0.2] *cinco t ao quadrado, menos vinte t, mais quinze, igual a "
        "zero.* [p=0.2] Divida tudo por cinco: [p=0.2] *t ao quadrado, menos quatro t, mais três.* [p=0.4] {c}O jogo: "
        "[p=0.2] soma *quatro,* produto *três.* [p=0.4] {d}*Um e três.* [p=0.4] {e}Passa por quinze metros subindo, em "
        "um segundo, [p=0.2] e descendo, em três. [p=0.2] Fica acima de um a três: [p=0.2] *dois segundos.* "
        "[p=0.3] {ok}*Letra B!*"),
    dict(id="29", block="q4", text=
        "{t}Teste t igual a dois: [p=0.2] *vinte metros,* acima de quinze. [p=0.4] "
        "{xa}A A e a C respondem *um instante só,* [p=0.2] {xc}não o intervalo. [p=0.4] {xd}A D é o *voo inteiro:* "
        "[p=0.2] a altura volta a zero em quatro segundos. [p=0.4] {xe}E a E é falsa: [p=0.2] em dois segundos, a bola "
        "está a vinte metros. [p=0.4] {f}E a *altura máxima?* [p=0.2] Fica para a série de *Função "
        "Quadrática.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] soma é menos b sobre a; [p=0.2] produto é c sobre "
        "a. [p=0.5] {b}Dois: [p=0.2] dois números de soma S e produto P. [p=0.5] {c}Três: [p=0.2] raízes dadas: [p=0.2] x "
        "ao quadrado, menos S x, mais P, igual a zero."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}Uma *calçada* em volta de um jardim [p=0.2] dá uma equação com raízes *dois e menos dez.* [p=0.4] {b}A "
        "resposta é dois, [p=0.2] é dez [p=0.2] ou é menos dez? [p=0.5] {c}Próximo episódio: [p=0.2] *do texto à "
        "equação.*"),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você achou o dois e o cinco antes de mim? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
