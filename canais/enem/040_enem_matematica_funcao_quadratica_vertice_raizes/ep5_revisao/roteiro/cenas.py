# Roteiro — Função Quadrática: vértice, raízes, máximo e mínimo, Episódio 5 de 5: Revisão geral, estratégia de prova,
#   pegadinhas e treino (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/25-funcao-quadratica-vertice-raizes.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (Q1–Q9, nem a Q7 descartada) nem a questão nova do ep. 1. As 5 questões são INÉDITAS (marcadas).
#   Lançamento oblíquo (Física): só citado.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (o gancho só acrescenta, depois delas, o que a aula vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 a parábola SORRINDO (mínimo) ou TRISTE (máximo) · o Δ CONTA OS TOQUES NO CHÃO · o a ANDA COM O x² (ícone: as duas
#       parábolas) ·
#   ep2 o ESPELHO DOBRADO (vértice no meio das raízes) · x do vértice = ONDE/QUANDO, y do vértice = QUANTO · o GRÁFICO NÃO
#       É O CAMINHO (ícone: a folha dobrada) ·
#   ep3 o CABO DE GUERRA da otimização · RAÍZES DE CABEÇA, VÉRTICE NO MEIO (ícone: o cercado no muro) ·
#   ep4 as TRÊS FOTOS DA MESMA PESSOA (três crachás) · "PARÁBOLA TRISTE É POSITIVA NO MEIO" · NUNCA DIVIDA POR x.
#   Os eps. 4 e 5 foram feitos em paralelo: as analogias do ep. 4 vêm do cabeçalho do cenas.py dele.
# O que a prova cobra (seção 01): maximizar/minimizar (vértice) · trajetórias · ler e montar a lei · sinal. O que mais
#   rende: xV = −b/2a; o x do vértice diz ONDE o ótimo acontece, o y diz QUANTO ele vale.
# Onde aparece (seção 10): MUV s = s0 + v0t + at²/2 (altura máxima = vértice; s × t parábola, v × t reta) · Economia (o
#   lucro máximo é o vértice de L = R − C, não o da receita) · Geometria (sem muro, perímetro fixo → quadrado) · energia
#   cinética Ec = mv²/2 (ramo de parábola). Lançamento oblíquo: só citado.
# Estratégia (seção 09): sublinhe se pedem x ou y do vértice · raízes primeiro, vértice no meio · teste as alternativas
#   (sinal de a, c, raízes).
# V/F (os 9 erros da seção 11, com números NOSSOS; 6 falsas e 3 verdadeiras — as verdadeiras são as versões CERTAS dos
#   erros 2, 6 e 7):
#   1 F x² − 6x + 1: xV = b/2a = −3 (é −b/2a = 3) · 2 V x² − 10x + 9 (raízes 1 e 9): xV = 5, não 10 (−b/a é a soma) ·
#   3 F h(t) = 50t − 5t²: a altura máxima é 5 (5 s é o instante; h(5) = 125 m) · 4 F h(t) = 24t − 4t²: a = 24 (a = −4) ·
#   5 F 2x² − 8x + 3 tem máximo (a > 0: mínimo, −5 em x = 2) · 6 V x² + 2x + 5: Δ = −16 e é positiva para todo x ·
#   7 V x² > 6x ⇔ x < 0 ou x > 6 · 8 F 48 m de tela + muro: o quadrado 16 × 16 dá a maior área (x(48 − 2x): 12 × 24 =
#   288 m² > 256) · 9 F o gráfico altura × tempo de uma bola jogada para cima é o caminho dela.
# QUESTÕES INÉDITAS (conferidas em trabalho/conferir_questoes.py: uma única correta; cada errada = um erro clássico; as
#   explicações das erradas são NOSSAS):
#   Q1 (altura máxima) foguete de garrafa PET, h(t) = 40t − 5t²: tV = 4 s, h(4) = 80 m → C. A 4 (o instante) · B 8 (a
#      volta ao solo) · D 160 (esqueceu o termo quadrático: 40 · 4) · E 320 (os dois: 40 · 8).
#   Q2 (receita máxima) pizzaria: 200 pizzas/semana a R$ 50,00; cada R$ 1,00 de desconto → +10 pizzas; o forno assa até
#      400 por semana. R(x) = (50 − x)(200 + 10x) = −10x² + 300x + 10 000, raízes 50 e −20 → desconto 15 → preço R$ 35,00
#      (350 pizzas ≤ 400: o vértice CABE; receita R$ 12.250,00) → D. A R$ 15,00 (o desconto no lugar do preço) · B R$ 20,00
#      (−b/a: desconto 30) · C R$ 25,00 (trocou a raiz −20 por 0: meio de 0 e 50) · E R$ 65,00 (sinal de xV trocado).
#   Q3 (área com muro) 120 m de tela, um lado no muro: A(x) = x(120 − 2x), raízes 0 e 60 → x = 30, frente 60 → 1 800 m²
#      → E. A 30 (a lateral: x no lugar do y) · B 60 (a frente) · C 900 (quadrado de 30 cercando 4 lados) · D 1 600
#      (quadrado de 40 com muro).
#   Q4 (lei pelo gráfico) arco que toca o chão em x = −1 e x = 3, topo 8 m: f(x) = a(x + 1)(x − 3), f(1) = −4a = 8 →
#      a = −2 → −2x² + 4x + 6 → A. B −2x² − 4x + 6 (raízes com sinal trocado: 1 e −3) · C x² − 2x − 3 (esqueceu o a) ·
#      D 2x² − 4x − 6 (sinal de a ignorado: boca para cima) · E −2x² + 4x + 8 (o topo 8 usado como c).
#   Q5 (sinal, a < 0) estufa: T(t) = −t² + 12t + 8 (t em horas a partir das 6 h), acima de 28 °C → t² − 12t + 20 < 0 →
#      2 < t < 10 → entre 8 h e 16 h → B. A antes das 8 h ou depois das 16 h (sinal invertido entre as raízes) · C a partir
#      das 8 h (tratou como reta: só uma raiz) · D entre 8 h e 12 h (parou no vértice) · E entre 6 h e 18 h (−b/a = 12).
# Gabaritos: C, D, E, A, B. O vértice da Q2 cabe nas restrições (350 ≤ 400).
# Checklist (seção 13) → episódio (como o prompt pede): coeficientes, concavidade, raízes e Δ → ep1 · vértice, simetria,
#   imagem e lançamentos → ep2 · otimização e "o vértice cabe no problema" → ep3 · formas da lei, sinal e inequações → ep4.
# Meta (prompt e material): 30 questões, 21 acertos (70%), com pelo menos dez de otimização em contexto.
# Ponte (do usuário): Função exponencial.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de função quadrática: 9 pegadinhas e 5 questões estilo ENEM | Função Quadrática Ep. 5"
# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, numa aula de revisão animada, conversando "
            "de perto com um aluno que está treinando para o ENEM: voz calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas de verdadeiro ou falso com suspense, "
            "como num jogo; mostre surpresa nas pegadinhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, fale devagar e com clareza, passo a passo. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO (frase do usuário) =================
    dict(id="01", block="hook", text=
        "{a}Nas questões de parábola, [p=0.2] o ENEM coloca *de propósito* as duas respostas nas alternativas: [p=0.3] "
        "{b}o *xis do vértice* [p=0.2] e o *ípsilon do vértice.* [p=0.4] {c}Quem sabe *qual das duas foi pedida* [p=0.2] "
        "já ganhou metade da questão. [p=0.4] {d}Hoje: [p=0.2] nove frases de verdadeiro ou falso [p=0.2] e cinco "
        "questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E o que a prova pede? [p=0.4] {a}*Maximizar ou minimizar:* [p=0.2] preço, área, custo. [p=0.3] {b}*Trajetórias:* [p=0.2] a altura de uma bola. [p=0.3] {c}*Ler e "
        "montar a lei,* [p=0.2] como num arco de ponte. [p=0.3] {d}E o *sinal:* [p=0.2] quando o lucro é positivo."),
    dict(id="03", block="rende", text=
        "{t}E o que mais rende? [p=0.4] {a}Saber de cor: [p=0.2] *xis do vértice igual a menos bê sobre dois a.* [p=0.4] "
        "{b}O *xis* do vértice diz *onde* o ótimo acontece: [p=0.2] qual preço, qual medida, qual instante. [p=0.3] "
        "{c}O *ípsilon* diz *quanto* ele vale: [p=0.2] qual receita, qual área, qual altura."),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] relembre cada episódio. [p=0.4] {a}Um: [p=0.2] a parábola *sorrindo* tem mínimo; "
        "[p=0.2] a *triste* tem máximo. [p=0.2] O *delta conta os toques no chão,* [p=0.2] e o *a anda com o xis "
        "ao quadrado.* [p=0.4] {b}Dois: [p=0.2] o *espelho dobrado.* [p=0.2] O vértice mora *no meio das raízes;* "
        "[p=0.2] o xis responde *onde,* o ípsilon responde *quanto;* [p=0.2] e o *gráfico não é o caminho.*"),
    dict(id="05", block="indice", text=
        "{a}Três: [p=0.2] o *cercado no muro* [p=0.2] e o *cabo de guerra:* [p=0.2] uma coisa sobe, a outra desce, "
        "[p=0.2] e o produto tem um topo. [p=0.4] {b}Quatro: [p=0.2] as *três fotos da mesma pessoa.* [p=0.2] *Parábola "
        "triste é positiva no meio,* [p=0.2] e *nunca divida por xis.*"),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="06", block="onde", text=
        "{t}E as outras provas? [p=0.4] {a}Na *Física,* [p=0.2] no movimento com aceleração, [p=0.2] *a altura máxima é o vértice.* [p=0.3] {b}Na "
        "*Economia,* [p=0.2] o lucro máximo é o vértice do *lucro,* [p=0.2] receita menos custo, [p=0.2] e não o da "
        "receita."),
    dict(id="07", block="onde", text=
        "{c}Na *Geometria:* [p=0.2] sem muro, com perímetro fixo, [p=0.2] a maior área é a do *quadrado.* [p=0.3] {d}E a "
        "*energia cinética,* [p=0.2] eme vê ao quadrado sobre dois, [p=0.2] desenha um pedaço de parábola. [p=0.3] {e}O "
        "lançamento oblíquo fica para a Física."),

    # ================= ESTRATÉGIA: 3 HÁBITOS (seção 09) =================
    dict(id="08", block="habitos", text=
        "{t}E na hora da prova? [p=0.2] Três hábitos. [p=0.4] {a}Um: [p=0.2] *sublinhe o que é pedido.* [p=0.2] \"Qual "
        "preço\", \"em que instante\": [p=0.2] xis do vértice. [p=0.2] \"Qual a receita máxima\", \"qual a altura\": "
        "[p=0.2] ípsilon do vértice. [p=0.3] {b}Dois: [p=0.2] *raízes primeiro, vértice no meio.*"),
    dict(id="09", block="habitos", text=
        "{c}Três: [p=0.2] *teste as alternativas no gráfico.* [p=0.2] Confira o *sinal de a,* [p=0.2] o *cê* [p=0.2] e "
        "as *raízes.* "),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="10", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="11", block="vf", text=
        "{t}Um: [p=0.2] em xis ao quadrado menos seis xis mais um, [p=0.2] o xis do vértice é *bê sobre dois a:* "
        "[p=0.2] *menos três.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque a fórmula parece "
        "completa. [p=0.3] {g}Mas faltou o *menos:* [p=0.2] menos bê sobre dois a. [p=0.2] O vértice está no *três.*"),
    dict(id="12", block="vf", text=
        "{t}Dois: [p=0.2] xis ao quadrado menos dez xis mais nove [p=0.2] tem raízes um e nove. [p=0.2] O xis do vértice "
        "é *cinco.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque menos bê sobre a dá "
        "*dez.* [p=0.3] {g}Mas dez é a *soma* das raízes. [p=0.2] O vértice é a *média:* [p=0.2] metade disso."),
    dict(id="13", block="vf", text=
        "{t}Três: [p=0.2] agá de tê igual a cinquenta tê menos cinco tê ao quadrado. [p=0.2] A altura máxima é "
        "*cinco.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque é a primeira conta que sai. "
        "[p=0.3] {g}Mas cinco segundos é o *quando.* [p=0.2] A altura é o *quanto:* [p=0.2] agá de cinco, [p=0.2] "
        "*cento e vinte e cinco metros.*"),
    dict(id="14", block="vf", text=
        "{t}Quatro: [p=0.2] em agá igual a vinte e quatro tê menos quatro tê ao quadrado, [p=0.2] o a vale *vinte e "
        "quatro.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque é o primeiro número da lei. [p=0.3] "
        "{g}Mas o *a anda com o tê ao quadrado,* [p=0.2] esteja onde estiver: [p=0.2] *a igual a menos quatro.*"),
    dict(id="15", block="vf", text=
        "{t}Cinco: [p=0.2] dois xis ao quadrado menos oito xis mais três [p=0.2] tem *máximo.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o a positivo parece \"subir até um máximo\". [p=0.3] {g}Mas a "
        "positivo *sorri:* [p=0.2] boca para cima, [p=0.2] o vértice é o *fundo.* [p=0.2] É *mínimo.*"),
    dict(id="16", block="vf", text=
        "{t}Seis: [p=0.2] xis ao quadrado mais dois xis mais cinco tem delta negativo [p=0.2] e é *positiva para todo "
        "xis.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque muita gente pensa: delta "
        "negativo, função negativa. [p=0.3] {g}Mas delta negativo é *zero toques no chão.* [p=0.2] A parábola fica "
        "toda de um lado: [p=0.2] *o lado do sinal de a.*"),
    dict(id="17", block="vf", text=
        "{t}Sete: [p=0.2] xis ao quadrado maior que seis xis [p=0.2] vale para *xis menor que zero ou xis maior que "
        "seis.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque, dividindo por xis, sobra "
        "só xis maior que seis. [p=0.3] {g}Mas *nunca divida por xis:* [p=0.2] ele pode ser negativo. "),
    dict(id="18", block="vf", text=
        "{t}Oito: [p=0.2] com *quarenta e oito metros de tela* e um lado no muro, [p=0.2] a maior área é a do "
        "*quadrado:* [p=0.2] dezesseis por dezesseis. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque "
        "o quadrado é o campeão sem muro. [p=0.3] {g}Com muro, *monte a área:* [p=0.2] doze por vinte e quatro, "
        "[p=0.2] *duzentos e oitenta e oito,* [p=0.2] contra duzentos e cinquenta e seis."),
    dict(id="19", block="vf", text=
        "{t}E nove: [p=0.2] o gráfico *altura por tempo* de uma bola jogada para cima [p=0.2] é o *caminho* dela. "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o desenho tem a forma de um arco. [p=0.3] "
        "{g}Mas a bola sobe e desce *em linha reta.* [p=0.2] O *gráfico não é o caminho:* [p=0.2] é a altura em cada "
        "instante."),
    dict(id="20", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas. [p=0.2] Em todas, [p=0.2] *sublinhe o que é pedido.*"),

    # ================= QUESTÃO 1: ALTURA MÁXIMA =================
    dict(id="21", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Numa feira de ciências, [p=0.2] um foguete de garrafa PET é lançado *verticalmente* "
        "do chão. [p=0.2] A altura, em metros, é *agá de tê igual a quarenta tê menos cinco tê ao quadrado,* [p=0.2] "
        "com tê em segundos. [p=0.3] {b}A *altura máxima* é: [p=0.4] {la}A, [p=0.2] quatro metros. [p=0.2] {lb}B, "
        "[p=0.2] oito. [p=0.2] {lc}C, [p=0.2] oitenta. [p=0.2] {ld}D, [p=0.2] cento e sessenta. [p=0.2] {le}E, "
        "[p=0.2] trezentos e vinte. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q1", text=
        "{d}Sublinhe: [p=0.2] *altura máxima,* [p=0.2] o ípsilon do vértice. [p=0.3] {a}O a é *menos cinco,* [p=0.2] "
        "o bê é quarenta. [p=0.2] Tê do vértice: [p=0.2] quarenta sobre dez, [p=0.2] *quatro segundos.* [p=0.3] {b}Agora "
        "o quanto: [p=0.2] cento e sessenta menos oitenta, [p=0.2] *oitenta metros.* [p=0.2] {ok}*Letra C!* [p=0.2] "
        "{v}Confira: [p=0.2] volta ao chão em oito, [p=0.2] e quatro é o meio. [p=0.4] {xa}A A é o *instante.* [p=0.2] "
        "{xb}A B é a *volta ao chão.* [p=0.2] {xd}A D esqueceu o termo ao quadrado, [p=0.2] {xe}e a E ainda usou o "
        "oito."),

    # ================= QUESTÃO 2: RECEITA MÁXIMA =================
    dict(id="23", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Uma pizzaria vende *duzentas pizzas por semana* a *cinquenta reais.* [p=0.2] Para "
        "cada real de desconto, [p=0.2] vende *dez pizzas a mais.* [p=0.2] O forno assa até quatrocentas. "
        "[p=0.3] {b}Para a *maior receita,* [p=0.2] o *preço* deve ser: [p=0.4] {la}A, [p=0.2] quinze reais. [p=0.2] "
        "{lb}B, [p=0.2] vinte. [p=0.2] {lc}C, [p=0.2] vinte e cinco. [p=0.2] {ld}D, [p=0.2] trinta e cinco. [p=0.2] "
        "{le}E, [p=0.2] sessenta e cinco. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="24", block="q2", text=
        "{d}Sublinhe: [p=0.2] pedem o *preço,* [p=0.2] não o desconto. [p=0.3] {a}Com xis reais de desconto: [p=0.2] "
        "receita igual a *cinquenta menos xis, vezes duzentos mais dez xis.* [p=0.3] {b}Raízes de cabeça: [p=0.2] "
        "*cinquenta e menos vinte.* [p=0.2] O meio: [p=0.2] *quinze de desconto.* [p=0.2] Preço: [p=0.2] *trinta e "
        "cinco.* [p=0.2] {ok}*Letra D!* [p=0.2] {v}Cabe no forno? [p=0.2] Trezentas e cinquenta pizzas: [p=0.2] cabe. "
        "[p=0.4] {xa}A A respondeu o *desconto.* [p=0.2] {xb}A B usou *menos bê sobre a.* [p=0.2] {xc}A C trocou o "
        "menos vinte por zero. [p=0.2] {xe}E a E *trocou o sinal* do vértice."),

    # ================= QUESTÃO 3: CERCADO NO MURO =================
    dict(id="25", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Um criador tem *cento e vinte metros de tela* [p=0.2] para um cercado retangular. "
        "[p=0.2] Um lado fica *encostado no muro,* sem tela. [p=0.3] {b}A *maior área* possível, em metros quadrados, "
        "é: [p=0.4] {la}A, [p=0.2] trinta. [p=0.2] {lb}B, [p=0.2] sessenta. [p=0.2] {lc}C, [p=0.2] novecentos. [p=0.2] "
        "{ld}D, [p=0.2] mil e seiscentos. [p=0.2] {le}E, [p=0.2] mil e oitocentos. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q3", text=
        "{d}Lateral xis, [p=0.2] duas laterais; [p=0.2] a frente fica com *cento e vinte menos dois xis.* [p=0.3] "
        "{a}Área: [p=0.2] xis vezes cento e vinte menos dois xis. [p=0.2] Raízes: [p=0.2] *zero e sessenta.* [p=0.2] "
        "Meio: [p=0.2] *trinta.* [p=0.3] {b}Frente de sessenta, [p=0.2] área *mil e oitocentos.* [p=0.2] {ok}*Letra E!* "
        "[p=0.4] {xd}A D é o *quadrado com muro:* [p=0.2] quarenta por quarenta, [p=0.2] menor. [p=0.2] {xc}A C cercou "
        "os quatro lados. [p=0.2] {xa}A A e {xb}a B pararam nas *medidas:* [p=0.2] o xis, não o ípsilon."),

    # ================= QUESTÃO 4: A LEI PELO GRÁFICO =================
    dict(id="27", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}O arco de um portão é uma parábola. [p=0.2] Num sistema de eixos, [p=0.2] ele "
        "toca o chão em *xis igual a menos um* [p=0.2] e *xis igual a três,* [p=0.2] e sua altura máxima é *oito "
        "metros.* [p=0.3] {b}A lei do arco é: [p=0.4] {la}A, [p=0.2] menos dois xis ao quadrado, mais quatro xis, mais "
        "seis. [p=0.2] {lb}B, [p=0.2] menos dois xis ao quadrado, menos quatro xis, mais seis. [p=0.2] {lc}C, [p=0.2] "
        "xis ao quadrado, menos dois xis, menos três. [p=0.2] {ld}D, [p=0.2] dois xis ao quadrado, menos quatro xis, "
        "menos seis. [p=0.2] {le}E, [p=0.2] menos dois xis ao quadrado, mais quatro xis, mais oito. [p=0.4] {p}*Pause "
        "e tente.* [p=2.0]"),
    dict(id="28", block="q4", text=
        "{d}Use o hábito três: [p=0.2] teste as alternativas. [p=0.3] {a}Arco tem topo: [p=0.2] *a negativo.* [p=0.2] "
        "{xc}Caem a C {xd}e a D. [p=0.3] {b}Raízes menos um e três: [p=0.2] o vértice no meio, [p=0.2] em *xis igual a "
        "um.* [p=0.2] {xb}A B tem as raízes com o sinal trocado. [p=0.3] {c}Sobram A e E. [p=0.2] Ponha xis igual a "
        "um: [p=0.2] a A dá *oito;* [p=0.2] {xe}a E dá *dez.* [p=0.2] Ela usou o topo como cê. [p=0.2] {ok}*Letra A!*"),

    # ================= QUESTÃO 5: O SINAL COM a NEGATIVO =================
    dict(id="29", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Numa estufa, [p=0.2] a temperatura é *tê de tê igual a menos tê ao quadrado, "
        "mais doze tê, mais oito,* [p=0.2] em graus, [p=0.2] com tê em horas a partir das seis da manhã. [p=0.3] {b}A "
        "temperatura fica *acima de vinte e oito graus:* [p=0.4] {la}A, [p=0.2] antes das oito ou depois das dezesseis "
        "horas. [p=0.2] {lb}B, [p=0.2] entre oito e dezesseis horas. [p=0.2] {lc}C, [p=0.2] a partir das oito horas. "
        "[p=0.2] {ld}D, [p=0.2] entre oito e doze horas. [p=0.2] {le}E, [p=0.2] entre seis e dezoito horas. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="30", block="q5", text=
        "{d}Iguale a vinte e oito: [p=0.2] tê ao quadrado menos doze tê mais vinte, [p=0.2] igual a zero. [p=0.2] "
        "Soma doze, produto vinte: [p=0.2] *dois e dez.* [p=0.3] {a}O a é negativo: [p=0.2] *parábola triste é positiva "
        "no meio.* [p=0.2] Acima de vinte e oito *entre as raízes.* [p=0.3] {b}Duas a dez horas depois das seis: "
        "[p=0.2] *das oito às dezesseis.* [p=0.2] {ok}*Letra B!* [p=0.4] {xa}A A inverteu o sinal. [p=0.2] {xc}A C "
        "tratou como reta. [p=0.2] {xd}A D parou no vértice, [p=0.2] {xe}e a E usou *menos bê sobre a.*"),

    # ================= CHECKLIST (seção 13) =================
    dict(id="31", block="checklist", text=
        "{t}O checklist. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* para outra pessoa, [p=0.2] "
        "sem consultar nada. [p=0.4] {b}Coeficientes, concavidade, raízes e delta: [p=0.2] episódio um. [p=0.3] "
        "{c}Vértice, simetria, imagem e lançamentos: [p=0.2] episódio dois."),
    dict(id="32", block="checklist", text=
        "{a}Otimização [p=0.2] e *o vértice cabe no problema?* [p=0.2] Episódio três. [p=0.3] {b}Formas da lei, sinal e "
        "inequações: [p=0.2] episódio quatro. [p=0.4] {c}O que você *não* marcou, [p=0.2] reveja o episódio "
        "correspondente."),

    # ================= META =================
    dict(id="33", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *trinta questões* [p=0.2] {b}e acerte pelo menos *vinte e uma,* [p=0.2] "
        "setenta por cento. [p=0.4] {c}E pelo menos *dez de otimização* em contexto: [p=0.2] preço, área, altura."),

    # ================= PONTE E CTA =================
    dict(id="34", block="ponte", text=
        "{a}O próximo assunto é *Função exponencial* e crescimento ou decaimento. [p=0.4] {b}Na afim, [p=0.2] cada passo "
        "*soma* a mesma quantidade; [p=0.3] {c}na quadrática, [p=0.2] o passo muda; [p=0.3] {d}e na exponencial, "
        "[p=0.2] cada passo *multiplica* pelo mesmo fator, [p=0.2] porque a variável sobe para o expoente."),
    dict(id="35", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] {com}E me conte nos "
        "*comentários:* [p=0.2] qual pegadinha te pegou? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo "
        "tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] "
        "para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}A série de função quadrática está completa. "
        "[p=0.2] Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
