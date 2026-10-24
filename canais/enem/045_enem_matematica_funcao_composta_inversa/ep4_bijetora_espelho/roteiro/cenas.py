# Roteiro — Função Composta e Função Inversa, Episódio 4 de 5: quem tem inversa e o espelho na reta y = x
# Base: Estudos/Enem/estudos/01-matematica/30-funcao-composta-inversa.html — seção 06 (bijetora, restringir o domínio),
#   seção 07 (gráfico da inversa), seção 08 (par exponencial–logaritmo), estratégia 3 da seção 09 (tabelas)
#   + Questões 7, 5 e 9 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   ARMÁRIO DE CHAVES: cada chave abre um só armário, e todo armário tem chave → dá para voltar do armário à chave.
#   "Para voltar, cada saída precisa ter UM dono e todo endereço precisa existir."
#   FOLHA DOBRADA NA DIAGONAL com tinta fresca: o gráfico da inversa é o espelho em y = x, (a, b) vira (b, a).
#   TABELA: a inversa se lê de baixo para cima (procure o número nas SAÍDAS).
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte.
# Exemplos do material: x² em ℝ ((−3)² = 3² = 9), 2ˣ de ℝ em ℝ (nenhum x dá −1), x² em [0, +∞[ com inversa √x,
#   f(1) = 3 → (1, 3) vira (3, 1), o par 2ˣ / log₂ x com (0, 1) ↔ (1, 0) e domínio/imagem trocados.
# Nós fazemos (prompt): (3, 8) em y = 2ˣ → (8, 3) em y = log₂ x, porque log₂ 8 = 3.
# TABELA PRÓPRIA no bloco g e no erro 3 (para não entregar a Questão 9, "você faz"): 4 colunas,
#   x: 1 2 3 4 · h(x): 3 1 4 2 · k(x): 2 4 1 3 → h⁻¹(4) = 3 (o 4 está na coluna x = 3); h(k(1)) = h(2) = 1.
#   Erro 3: procurar o 4 nas ENTRADAS dá h(4) = 2 (errado; certo 3).
# Erro 2 usa o ponto (1, 3) do bloco e: no eixo y daria (−1, 3); trocando os sinais, (−1, −3). Certo: (3, 1).
# QUESTÃO 7 ("eu faço"): D (x³ + 1). Erradas como no material: A x² e B |x| (2 e −2 dão a mesma saída); C 2ˣ é injetora
#   mas não sobrejetora em ℝ (nenhum x dá −1); E constante 5 (impossível saber de onde veio). Volta x = ∛(y − 1);
#   conferido com x = 2 → y = 9 → ∛8 = 2.
# QUESTÃO 5 ("nós fazemos"): B (7, 3). Erradas como no material: A é o ponto do próprio f; C e E refletem na origem
#   (trocam sinais); D toma f⁻¹ por 1/f.
# QUESTÃO 9 ("você faz", com pausa): g(3) = 5; o 5 está na linha de f na coluna x = 2 → B (2). Erradas como no material:
#   A f(3) = 1 (ignorou g); C f(5) = 3 (usou f no lugar de f⁻¹); D g(5) = 4 (g duas vezes); E parou em g(3) = 5.
# Atalhos (verde): "teste x e −x" (injetora) · "troque as coordenadas de lugar" (espelho) · "inversa em tabela: leia de
#   baixo para cima" · "para conferir a volta, ida e volta com um número" (Q7, acréscimo nosso).
# Frases-chave (meio e fim, idênticas): 1. Só tem inversa quem é bijetora: cada saída com um dono, e todas existindo.
#   2. O gráfico da inversa é o espelho em y = x: (a, b) vira (b, a). 3. Em tabela, procure o número nas saídas.
# Narração sem o símbolo ℝ: "os números reais" / "todos os reais". Contas conferidas em trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Quem tem inversa? Bijetora e o espelho na reta y = x · Matemática ENEM, Composta e Inversa ep. 4"

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
        "{a}Se eu te disser que um número ao quadrado deu *nove,* [p=0.3] {b}você não sabe se ele era *três* [p=0.2] ou "
        "*menos três.* [p=0.4] {c}Essa dúvida tem nome, [p=0.2] {d}e é ela que decide se uma função pode ser *desfeita.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, você vai dizer se uma função *tem inversa,* [p=0.3] {b}achar pontos e o gráfico da inversa *pelo "
        "espelho* [p=0.3] {c}e ler inversas em *tabelas.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}Do episódio passado: [p=0.2] a *inversa* desfaz o caminho. [p=0.2] "
        "Se *f de um* é *três,* [p=0.2] a inversa leva o três de volta ao um. [p=0.4] {b}Da série de Conceito de Função: "
        "[p=0.2] *domínio* é o que pode entrar; [p=0.2] *imagem* é o que de fato sai. [p=0.4] {c}E das séries de "
        "Exponencial e Logaritmo: [p=0.2] *dois ao cubo é oito* [p=0.2] e *log de oito na base dois é três* [p=0.2] "
        "dizem a mesma coisa."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Pense num armário de chaves. [p=0.3] {a}Cada chave abre *um só* armário. [p=0.3] {b}E *todo* armário tem a sua "
        "chave. [p=0.4] {c}Achou um armário aberto? [p=0.2] Você sabe qual chave foi usada. [p=0.4] {d}É "
        "isso que uma função precisa ter [p=0.2] para dar para *voltar.*"),

    # ================= BLOCO A: INJETORA =================
    dict(id="05", block="injetora", text=
        "{t}E se *duas chaves* abrissem o mesmo armário? [p=0.4] {a}Olhando o armário, [p=0.2] não daria para saber qual "
        "chave veio. [p=0.4] {b}Uma função é *injetora* [p=0.2] quando entradas diferentes [p=0.2] dão saídas "
        "*diferentes.* [p=0.4] {c}E *x ao quadrado,* nos números reais, [p=0.2] *não é:* [p=0.2] menos três ao quadrado é "
        "nove, [p=0.2] e três ao quadrado também é nove. [p=0.3] {d}O nove tem *dois donos.* [p=0.2] É a dúvida do "
        "gancho."),
    dict(id="06", block="injetora", text=
        "{t}Como testar rápido? [p=0.3] {a}Atalho: [p=0.2] *teste um número e o oposto dele.* [p=0.2] Dois e menos dois. "
        "[p=0.4] {b}Se der a *mesma saída,* [p=0.2] a função não é injetora. [p=0.4] {c}Em x ao quadrado, [p=0.2] dois e "
        "menos dois dão *quatro.*"),

    # ================= BLOCO B: SOBREJETORA =================
    dict(id="07", block="sobrejetora", text=
        "{t}E se existisse um armário *sem chave?* [p=0.4] {a}O *contradomínio* [p=0.2] é o conjunto de saídas que a "
        "função *promete:* [p=0.4] {b}Uma função é *sobrejetora* [p=0.2] quando "
        "*toda* saída do contradomínio é atingida. [p=0.4] {c}Agora *dois elevado a x,* [p=0.2] prometendo todos os reais. "
        "[p=0.2] Que x dá *menos um?* [p=0.4] {d}*Nenhum.* [p=0.2] Dois elevado a qualquer coisa é sempre *positivo.* "
        "[p=0.2] O menos um fica sozinho: [p=0.2] *ninguém chega* nele."),

    # ================= BLOCO C: BIJETORA =================
    dict(id="08", block="bijetora", text=
        "{t}Então, quem tem inversa? [p=0.4] {a}Quem é as duas coisas ao mesmo tempo: [p=0.2] injetora *e* sobrejetora. "
        "[p=0.2] Isso se chama *bijetora.* [p=0.4] {b}Para voltar, [p=0.2] cada saída precisa ter *um dono* [p=0.3] {c}e "
        "todo endereço precisa *existir.* [p=0.4] {d}Faltou uma das duas? [p=0.2] *Não existe inversa.*"),

    # ================= BLOCO D: RESTRINGIR O DOMÍNIO =================
    dict(id="09", block="restringir", text=
        "{t}Mas dá para *salvar* o x ao quadrado? [p=0.4] {a}*Restringir o domínio* [p=0.2] é deixar entrar só "
        "uma parte dos números. [p=0.4] {b}Deixe entrar só o *zero e os positivos.* [p=0.2] Agora o menos três nem entra: "
        "[p=0.2] o nove tem *um dono só,* o três. [p=0.4] {c}E a volta existe: [p=0.2] é a *raiz quadrada.* [p=0.4] {d}É "
        "por isso que *raiz de nove é três,* [p=0.2] e não menos três: [p=0.2] a raiz devolve só o valor *não negativo.*"),

    # ================= BLOCO E: O ESPELHO =================
    dict(id="10", block="espelho", text=
        "{t}E o *gráfico* da inversa, onde fica? [p=0.4] {a}Pegue uma folha com um desenho de *tinta fresca.* [p=0.3] "
        "{b}Dobre a folha na *diagonal* [p=0.2] e aperte. [p=0.4] {c}A tinta marca o outro lado: [p=0.2] um desenho "
        "*simétrico,* [p=0.2] quer dizer, igual, mas espelhado. [p=0.4] {d}Essa diagonal é a *reta y igual a x:* [p=0.2] "
        "onde as duas coordenadas são iguais: [p=0.2] um, um; [p=0.2] dois, dois."),
    dict(id="11", block="espelho", text=
        "{t}Por que o espelho é *essa* reta? [p=0.4] {a}Se *f de um é três,* [p=0.2] o gráfico de f tem o ponto *um, "
        "três.* [p=0.4] {b}A inversa faz o caminho contrário: [p=0.2] *f inversa de três é um.* [p=0.2] Ponto *três, um.* "
        "[p=0.4] {c}Trocar entrada e saída [p=0.2] é *trocar as coordenadas de lugar,* [p=0.2] e isso é refletir "
        "na *reta y igual a x.* [p=0.4] {d}Não no eixo y, [p=0.2] nem na origem."),
    dict(id="12", block="atalho", text=
        "{t}Para achar um ponto da inversa, [p=0.3] {a}atalho: [p=0.2] *troque as duas coordenadas de lugar.* "
        "[p=0.4] {b}O ponto *a, b* da função [p=0.2] vira o ponto *b, a* da inversa. [p=0.4] {c}Nenhum sinal muda. "
        "[p=0.2] Só a *ordem.*"),

    # ================= BLOCO F: O PAR EXPONENCIAL–LOGARITMO =================
    dict(id="13", block="par", text=
        "{t}E qual par de inversas o ENEM mais cobra? [p=0.4] {a}*Dois elevado a x* [p=0.2] e *log de x na base dois.* "
        "[p=0.4] {b}Pinte a curva de dois elevado a x. [p=0.2] Dobre a folha na diagonal. [p=0.3] {c}A tinta desenha a "
        "curva do *logaritmo.* [p=0.4] {d}O ponto *zero, um* da exponencial [p=0.2] vira o ponto *um, zero* do logaritmo."),
    dict(id="14", block="par", text=
        "{t}E tem mais. [p=0.4] {a}A exponencial aceita *qualquer* x: [p=0.2] domínio, todos os reais. "
        "[p=0.2] E só solta *positivos:* [p=0.2] imagem, acima de zero. [p=0.4] {b}O logaritmo é "
        "o contrário: [p=0.2] só aceita *positivos,* [p=0.2] e solta *qualquer* real. [p=0.4] {c}Domínio e imagem *trocam "
        "de lugar.* [p=0.2] E isso vale para qualquer par de inversas."),

    # ================= NÓS FAZEMOS =================
    dict(id="15", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}O gráfico de *y igual a dois elevado a x* [p=0.2] passa pelo ponto *três, oito.* [p=0.4] "
        "{b}Que ponto do gráfico de *log de x na base dois* [p=0.2] corresponde a ele? [p=0.4] {c}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="16", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Troque as coordenadas de lugar: [p=0.2] *três, oito* vira *oito, três.* [p=0.4] "
        "{b}Confere? [p=0.2] Dois elevado a quanto dá oito? [p=0.2] *Três.* [p=0.4] "
        "{c}Então o ponto é *oito, três.* [p=0.2] O espelho funcionou."),

    # ================= BLOCO G: TABELAS =================
    dict(id="17", block="tabela", text=
        "{t}E quando a função vem numa *tabela?* [p=0.4] {a}A linha de cima tem as *entradas,* [p=0.2] "
        "a de baixo, as *saídas* da função h. [p=0.4] {b}Quanto vale *h inversa de quatro?* [p=0.4] {c}A pergunta é: "
        "[p=0.2] *qual entrada dá quatro?* [p=0.2] Então procure o quatro *nas saídas.* [p=0.3] Ele está na coluna do "
        "*três.* [p=0.4] {d}h inversa de quatro é *três.* [p=0.2] A inversa se lê *de baixo para cima.*"),
    dict(id="18", block="tabela", text=
        "{t}E uma composta em tabela? [p=0.3] {a}*De dentro para fora,* [p=0.2] como no primeiro episódio. [p=0.4] "
        "{b}Para *h de k de um:* [p=0.2] primeiro k de um, [p=0.2] na linha do k: [p=0.2] *dois.* [p=0.4] {c}Depois h de "
        "dois, [p=0.2] na linha do h: [p=0.2] *um.* [p=0.4] {d}Atalho de tabela: [p=0.2] função normal, [p=0.2] *de cima "
        "para baixo;* [p=0.2] inversa, [p=0.2] *de baixo para cima.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] só tem inversa quem é bijetora: [p=0.2] cada saída com "
        "um dono, [p=0.2] e todas existindo. [p=0.5] {b}Dois: [p=0.2] o gráfico da inversa é o espelho em y igual a x: "
        "[p=0.2] a, b vira b, a. [p=0.5] {c}Três: [p=0.2] em tabela, procure o número nas saídas."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que *x ao quadrado* tem inversa *raiz de x* "
        "[p=0.2] em todos os reais. [p=0.4] {b}Parece certo, [p=0.2] porque a raiz desfaz o quadrado [p=0.2] nas contas "
        "do dia a dia. [p=0.4] {c}Mas o nove tem dois donos. [p=0.2] A volta só existe com o domínio *de zero para cima.*"),
    dict(id="21", block="erros", text=
        "{a}Segundo: [p=0.2] refletir o ponto *um, três* no *eixo y,* [p=0.2] e achar *menos um, três.* [p=0.2] Ou trocar "
        "os sinais. [p=0.4] {b}Parece certo, [p=0.2] porque espelho lembra virar para o "
        "outro lado. [p=0.4] {c}Mas o espelho da inversa é a *diagonal:* [p=0.2] só a *ordem* troca. [p=0.2] *Três, um.*"),
    dict(id="22", block="erros", text=
        "{a}Terceiro: [p=0.2] para *h inversa de quatro,* [p=0.2] procurar o quatro *nas entradas* [p=0.2] e responder h "
        "de quatro, [p=0.2] que é *dois.* [p=0.4] {b}Parece certo, [p=0.2] porque a gente sempre lê a tabela de cima para "
        "baixo. [p=0.4] {c}Mas a inversa pergunta *qual entrada dá quatro:* [p=0.2] procure nas *saídas.* [p=0.2] A "
        "resposta é *três.*"),

    # ================= QUESTÃO 7 (EU FAÇO) =================
    dict(id="23", block="q7", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material. [p=0.2] Esta, [p=0.2] eu resolvo com você. "
        "[p=0.4] {a}Um programa de computador só consegue *desfazer* uma função f, de reais em reais, [p=0.2] recuperando "
        "cada entrada a partir da saída, [p=0.2] quando f é *bijetora.* [p=0.2] Entre as funções abaixo, [p=0.2] a única "
        "que o programa consegue desfazer é: [p=0.4] {qa}A: [p=0.2] x ao quadrado. [p=0.3] {qb}B: [p=0.2] módulo de x. "
        "[p=0.3] {qc}C: [p=0.2] dois elevado a x. [p=0.3] {qd}D: [p=0.2] x ao cubo, mais um. [p=0.3] {qe}E: [p=0.2] f de "
        "x igual a cinco, para todo x. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="24", block="q7", text=
        "{t}Testando *com números.* [p=0.4] {xa}A A, x ao quadrado: [p=0.2] dois e menos dois dão *quatro.* "
        "[p=0.2] Dois donos. [p=0.4] {xb}A B, módulo de x: [p=0.2] dois e menos dois dão *dois.* [p=0.2] Dois donos de "
        "novo. [p=0.4] {xc}A C, dois elevado a x: [p=0.2] essa é injetora, [p=0.2] cada x dá uma saída diferente. "
        "[p=0.2] Mas *nenhum x dá menos um.* [p=0.2] Não é sobrejetora. [p=0.4] {xe}A E, sempre cinco: [p=0.2] saiu "
        "cinco? [p=0.2] Impossível saber de onde veio."),
    dict(id="25", block="q7", text=
        "{t}Sobrou a D: [p=0.2] *x ao cubo, mais um.* [p=0.4] {a}Ela é *sempre crescente:* [p=0.2] x maior, saída maior. "
        "[p=0.2] Ninguém repete. [p=0.4] {b}E atinge *todos* os reais, [p=0.2] até os negativos: [p=0.2] menos dois ao "
        "cubo, mais um, [p=0.2] dá *menos sete.* [p=0.4] {c}A volta existe: [p=0.2] tire o um, [p=0.2] e faça a *raiz "
        "cúbica.* [p=0.4] {d}Atalho: [p=0.2] confira com um número. [p=0.2] Dois ao cubo, mais um, é nove. [p=0.2] Nove "
        "menos um, oito; [p=0.2] raiz cúbica de oito, *dois.* [p=0.2] Voltou! [p=0.3] {ok}*Letra D!*"),

    # ================= QUESTÃO 5 (NÓS FAZEMOS) =================
    dict(id="26", block="q5", text=
        "{t}A próxima, [p=0.2] *a gente faz junto.* [p=0.4] {a}Uma função f, de reais em reais, [p=0.2] é crescente e "
        "invertível, [p=0.2] e seu gráfico passa pelo ponto *três, sete.* [p=0.2] O gráfico da função inversa [p=0.2] "
        "certamente passa pelo ponto: [p=0.4] {qa}A: [p=0.2] três, sete. [p=0.3] {qb}B: [p=0.2] sete, três. [p=0.3] "
        "{qc}C: [p=0.2] menos três, menos sete. [p=0.3] {qd}D: [p=0.2] três, um sétimo. [p=0.3] {qe}E: [p=0.2] menos sete, "
        "menos três. [p=0.5] {p}*Pause e tente.* [p=2.0]"),
    dict(id="27", block="q5", text=
        "{t}O que o ponto diz? [p=0.3] {a}*f de três é sete.* [p=0.4] {b}Então a inversa leva o sete de volta: [p=0.2] "
        "*f inversa de sete é três.* [p=0.2] Ponto *sete, três.* [p=0.4] {c}Troca de lugar, [p=0.2] espelho na diagonal. "
        "[p=0.3] {ok}*Letra B!* [p=0.4] {xa}A A [p=0.2] é o ponto da própria f. [p=0.3] {xc}A C [p=0.2] {xe}e a E "
        "[p=0.2] trocam os sinais: [p=0.2] isso é refletir na origem, [p=0.2] nada a ver com inverter. [p=0.3] {xd}E a D "
        "[p=0.2] confunde *f inversa* com *um sobre f.*"),

    # ================= QUESTÃO 9 (VOCÊ FAZ) =================
    dict(id="28", block="q9", text=
        "{t}E a última é *sua.* [p=0.4] {a}Um sistema de senhas transforma cada dígito de um a cinco em duas etapas. "
        "[p=0.2] Primeiro aplica o embaralhamento *g;* [p=0.2] depois aplica o código *f.* [p=0.2] As duas funções estão "
        "na tabela. [p=0.2] Um técnico precisa calcular *f inversa de g de três.* [p=0.2] Esse valor é: [p=0.4] {qa}A: "
        "[p=0.2] um. [p=0.3] {qb}B: [p=0.2] dois. [p=0.3] {qc}C: [p=0.2] três. [p=0.3] {qd}D: [p=0.2] quatro. [p=0.3] "
        "{qe}E: [p=0.2] cinco. [p=0.5] {p}*Pause e resolva.* [p=2.0]"),
    dict(id="29", block="q9", text=
        "{t}Conferindo. [p=0.2] *De dentro para fora.* [p=0.4] {a}Primeiro, *g de três:* [p=0.2] na linha do g, [p=0.2] "
        "embaixo do três, [p=0.2] está o *cinco.* [p=0.4] {b}Agora *f inversa de cinco:* [p=0.2] qual entrada de f dá "
        "cinco? [p=0.2] Procure o cinco *na linha do f.* [p=0.3] Ele está na coluna do *dois.* [p=0.4] {ok}*Letra B!*"),
    dict(id="30", block="q9", text=
        "{t}E as erradas? [p=0.3] {xa}A A [p=0.2] aplicou f direto no três, [p=0.2] ignorando o g: [p=0.2] f de três é "
        "um. [p=0.4] {xc}A C [p=0.2] usou *f* no lugar de *f inversa:* [p=0.2] f de cinco é três. [p=0.4] {xd}A D "
        "[p=0.2] aplicou g duas vezes: [p=0.2] g de cinco é quatro. [p=0.4] {xe}E a E [p=0.2] parou no g de três, "
        "[p=0.2] o cinco, [p=0.2] e esqueceu a inversa."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="31", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] só tem inversa quem é bijetora: [p=0.2] cada "
        "saída com um dono, [p=0.2] e todas existindo. [p=0.5] {b}Dois: [p=0.2] o gráfico da inversa é o espelho em y "
        "igual a x: [p=0.2] a, b vira b, a. [p=0.5] {c}Três: [p=0.2] em tabela, procure o número nas saídas."),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos *composta e inversa,* [p=0.3] {b}caçamos as *pegadinhas* "
        "[p=0.2] {c}e treinamos para o *ENEM.*"),
    dict(id="33", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual dos três testes você vai usar primeiro na prova: [p=0.2] o dos dois donos, o do espelho ou o da tabela? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
