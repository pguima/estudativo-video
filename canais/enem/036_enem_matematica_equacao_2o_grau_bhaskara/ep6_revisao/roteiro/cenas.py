# Roteiro — Equação do 2º Grau e Fórmula de Bhaskara, Episódio 6 de 6: Revisão geral, estratégia de prova, pegadinhas e
#   treino (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/21-equacao-2o-grau-bhaskara.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (as 9 questões do material). As 5 questões são INÉDITAS (marcadas na tela).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (o gancho só acrescenta, depois dela, o que a aula vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 a equação SÓ CONVERSA ARRUMADA (= 0) · o sinal é o SOBRENOME do coeficiente · PRODUTO NULO · nunca dividir por x
#   (tabelinha a | b | c) · ep2 Bhaskara é a CHAVE MESTRA · o Δ é o PORTEIRO (porteiro Δ) · ep3 o JOGO DOS DOIS NÚMEROS
#   (duas cartas viradas) · ep4 a CALÇADA ABRAÇA o jardim · DESCARTAR NÃO É TROCAR O SINAL (jardim com calçada + lixeira) ·
#   ep5 a FANTASIA do y que tem de sair (fantasia do y).
#   (O ep5 foi escrito em paralelo: as analogias dele vêm do cabeçalho do cenas.py dele e do prompt do vídeo 5.)
# O que a prova cobra (seção 01): áreas, movimento, contagem, economia e leitura das raízes; três hábitos: igualar a zero,
#   escolher o caminho (incompleta → fatoração; raízes inteiras → soma e produto; o resto → Bhaskara), voltar ao enunciado.
# Onde aparece (seção 10), com números NOSSOS (não repetem as Q1–Q9): lançamento h = 25t − 5t² = 30 → t² − 5t + 6 = 0 →
#   2 s (subindo) e 3 s (descendo) · Pitágoras com lados x e x + 2 (só citado: o (x + 2)² completo) · lucro
#   L = −x² + 30x − 200 = 0 → 10 e 20 unidades · Função quadrática: as raízes são os cortes da parábola no eixo x (só citada,
#   próxima série a citar; vértice, máximo e gráfico NÃO entram).
# Estratégia (seção 09): testar as alternativas · simplificar antes (4x² + 32x − 80 = 0 ÷ 4 → x² + 8x − 20 = 0) · soma e
#   produto primeiro, Bhaskara depois · reler a pergunta.
# V/F (os 9 erros da seção 11, com números nossos; 6 falsas e 3 verdadeiras — as verdadeiras são as versões CERTAS dos
#   erros 2, 5 e 9): 1 F em x² − 7x + 10 = 0, b = 7 (b = −7) · 2 V no Δ, (−7)² = 49 · 3 F só a raiz é dividida por 2a ·
#   4 F 3x² = 12x ÷ x → x = 4 (some o 0) · 5 V x² = 25 tem duas raízes, 5 e −5 · 6 F a raiz −10 não serve → a resposta é
#   10 (é a outra raiz) · 7 F em x² − 7x + 10 = 0 a soma é −7 (é +7) · 8 F em x⁴ − 5x² + 4 = 0 as raízes são 1 e 4 (essas
#   são o y: x = ±1 e ±2) · 9 V x² + 4x = 140 vira x² + 4x − 140 = 0 antes de Bhaskara.
# QUESTÕES INÉDITAS (conferidas em trabalho/conferir_questoes.py: uma única correta, conferida por substituição;
#   cada errada = um erro clássico; explicações das erradas são NOSSAS):
#   Q1 (moldura) quadro 30 cm × 20 cm, moldura de largura x em volta, área total 1 200 cm²:
#      (30 + 2x)(20 + 2x) = 1 200 → 4x² + 100x − 600 = 0 → ÷ 4: x² + 25x − 150 = 0 → soma −25, produto −150: 5 e −30 →
#      x = 5 cm → A. Conferência 40 · 30 = 1 200. B 10 (moldura de um lado só: (30 + x)(20 + x)) · C 30 (trocou o sinal da
#      raiz −30) · D 35 (parou na raiz do Δ, √1 225) · E 600 (a área da moldura, não a largura).
#   Q2 (parâmetro) 2x² − 12x + k = 0 com uma única raiz (raiz dupla): Δ = 144 − 8k = 0 → k = 18 → D (raiz x = 3).
#      A −18 (−12² = −144) · B 1,5 (não elevou o b ao quadrado) · C 3 (respondeu a raiz dupla, não o k) · E 72 (esqueceu o 4
#      de 4ac).
#   Q3 (equação pelas raízes) a = 1, raízes −3 e 7: S = 4, P = −21 → x² − 4x − 21 = 0 → E. A x² + 4x − 21 (sinal do meio
#      não trocado: "soma = b/a") · B x² − 4x + 21 (produto sem o sinal) · C x² − 10x + 21 (ignorou o sinal do −3) ·
#      D x² − 21x − 4 (trocou o lugar da soma e do produto).
#   Q4 (apertos de mão) n(n − 1)/2 = 28 → n² − n − 56 = 0 → 8 e −7 → n = 8 → B. A 7 (trocou o sinal da raiz −7) ·
#      C 14 (dividiu 28 por 2) · D 28 (respondeu os apertos) · E 56 (parou no 2 · 28).
#   Q5 (lançamento) h = 30t − 5t²; tempo ENTRE passar por 25 m subindo e descendo: 30t − 5t² = 25 → t² − 6t + 5 = 0 →
#      1 s e 5 s → intervalo 4 s → C. A 1 e D 5 (responderam um instante) · B 3 (a média dos instantes: o topo, outra
#      pergunta, assunto da Função quadrática) · E 8 (esqueceu de dividir por 2: raízes 2 e 10).
# Gabaritos: A, D, E, B, C.
# Checklist (seção 13) → episódio: forma geral, sinais e incompletas: ep1 · Bhaskara, origem, Δ e parâmetro: ep2 · soma e
#   produto e forma fatorada: ep3 · modelagem e descarte: ep4 · biquadradas: ep5.
# Meta (prompt e material): 30 questões, pelo menos 21 acertos (70%), com pelo menos dez em que você mesmo monta a equação.
# Ponte (do usuário): Sistemas de equações lineares.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de equação do 2º grau: 9 pegadinhas e 5 questões estilo ENEM | Bhaskara Ep. 6"
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
        "{a}O ENEM raramente escreve: [p=0.2] *resolva xis ao quadrado menos cinco xis mais quatro igual a zero.* [p=0.4] "
        "{b}Ele escreve um *jardim,* [p=0.2] uma *bola,* [p=0.2] um *campeonato* [p=0.2] ou um *lucro.* [p=0.4] {c}Hoje "
        "você treina a *montar, resolver e escolher a raiz certa.* [p=0.4] {d}Nove frases de verdadeiro ou falso [p=0.2] "
        "e cinco questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E onde a equação do segundo grau se esconde? [p=0.4] {a}Em *áreas:* [p=0.2] uma moldura, uma calçada. "
        "[p=0.3] {b}Em *movimento:* [p=0.2] a altura de uma bola. [p=0.3] {c}Em *contagem:* [p=0.2] jogos e apertos de "
        "mão. [p=0.3] {d}Em *economia:* [p=0.2] o lucro zero. [p=0.3] {e}E na *leitura das raízes:* [p=0.2] qual serve "
        "e qual vai para o lixo."),
    dict(id="03", block="tres", text=
        "{t}E três hábitos rendem mais que todos. [p=0.4] {a}Um: [p=0.2] *iguale a zero* antes de qualquer coisa. "
        "[p=0.3] {b}Dois: [p=0.2] *escolha o caminho.* [p=0.2] Incompleta, fatoração. [p=0.2] Raízes inteiras, soma e "
        "produto. [p=0.2] O resto, Bhaskara. [p=0.3] {c}Três: [p=0.2] *volte ao enunciado.* [p=0.2] A raiz negativa de "
        "uma medida não é resposta."),

    # ================= ÍNDICE DA REVISÃO: OS 5 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes, [p=0.2] relembre cada episódio. [p=0.4] {a}Um: [p=0.2] a equação *só conversa arrumada,* [p=0.2] "
        "igual a zero. [p=0.2] O sinal é o *sobrenome* do coeficiente. [p=0.2] Produto deu zero? [p=0.2] *Alguém ali é "
        "zero.* [p=0.2] E nunca divida por xis. [p=0.4] {b}Dois: [p=0.2] Bhaskara é a *chave mestra,* [p=0.2] e o delta "
        "é o *porteiro:* [p=0.2] duas raízes, uma ou nenhuma."),
    dict(id="05", block="indice", text=
        "{a}Três: [p=0.2] o *jogo dos dois números,* [p=0.2] de soma e produto. [p=0.4] {b}Quatro: [p=0.2] a calçada "
        "*abraça* o jardim, [p=0.2] dos dois lados. [p=0.2] E *descartar não é trocar o sinal.* [p=0.4] {c}Cinco: "
        "[p=0.2] na biquadrada, [p=0.2] o xis ao quadrado veste a *fantasia do y,* [p=0.2] e no final [p=0.2] a fantasia "
        "*tem de sair.*"),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="06", block="onde", text=
        "{t}E isso aparece fora da Álgebra? [p=0.4] {a}Na *Física:* [p=0.2] uma bola lançada para cima [p=0.2] tem altura "
        "vinte e cinco tê, menos cinco tê ao quadrado. [p=0.2] Ela passa por *trinta metros* em *dois "
        "segundos,* subindo, [p=0.2] e em *três,* descendo. [p=0.2] Tempo negativo se descarta."),
    dict(id="07", block="onde", text=
        "{b}Na *Geometria,* [p=0.2] Pitágoras com lados xis e xis mais dois [p=0.2] pede o produto notável *completo.* "
        "[p=0.3] {c}Na *Economia,* [p=0.2] o lucro zero mora nas raízes: [p=0.2] *dez e vinte unidades.* [p=0.3] {d}E na "
        "*Função quadrática,* [p=0.2] as raízes são onde a *parábola corta o eixo.*"),

    # ================= ESTRATÉGIA: 4 HÁBITOS (seção 09) =================
    dict(id="08", block="habitos", text=
        "{t}Na prova, [p=0.2] quatro hábitos. [p=0.4] {a}Um: [p=0.2] *teste as alternativas* na equação. [p=0.2] Quem "
        "zerar é raiz. [p=0.3] {b}Dois: [p=0.2] *simplifique antes.* [p=0.2] Divida tudo por um fator comum. [p=0.3] {c}Três: [p=0.2] *soma e produto primeiro,* "
        "[p=0.2] Bhaskara depois. [p=0.3] {d}Quatro: [p=0.2] achou as raízes? [p=0.2] *Releia a pergunta.*"),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="09", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="10", block="vf", text=
        "{t}Um: [p=0.2] em xis ao quadrado, menos sete xis, mais dez, [p=0.2] o bê vale *sete.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o sete parece sozinho. [p=0.3] {g}Mas o sinal é o "
        "*sobrenome* do coeficiente: [p=0.2] *bê igual a menos sete.*"),
    dict(id="11", block="vf", text=
        "{t}Dois: [p=0.2] no delta dessa equação, [p=0.2] bê ao quadrado é *quarenta e nove.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Verdadeiro!* [p=0.3] {e}Parece falso porque muita gente acha *menos* quarenta e nove. [p=0.3] {g}Mas o menos *entra no parêntese:* [p=0.2] *bê ao quadrado nunca é negativo.*"),
    dict(id="12", block="vf", text=
        "{t}Três: [p=0.2] em Bhaskara, [p=0.2] só a *raiz do delta* é dividida por dois á. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque a raiz parece a parte difícil. [p=0.3] {g}Mas o traço da "
        "fração cobre o *numerador inteiro:* [p=0.2] menos bê, mais ou menos a raiz, [p=0.2] *tudo* sobre dois á."),
    dict(id="13", block="vf", text=
        "{t}Quatro: [p=0.2] em três xis ao quadrado igual a doze xis, [p=0.2] divido por xis [p=0.2] e acho *xis igual a "
        "quatro.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o quatro é mesmo uma raiz. [p=0.3] "
        "{g}Mas a divisão *apaga o zero.* [p=0.2] Fatore: [p=0.2] três xis, vezes xis menos quatro. [p=0.2] *Zero ou "
        "quatro.*"),
    dict(id="14", block="vf", text=
        "{t}Cinco: [p=0.2] xis ao quadrado igual a vinte e cinco [p=0.2] tem *duas raízes,* [p=0.2] cinco e menos cinco. "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque a calculadora só mostra o cinco. "
        "[p=0.3] {g}Mas menos cinco ao quadrado [p=0.2] *também* dá vinte e cinco. [p=0.2] Só descarte se o contexto "
        "pedir."),
    dict(id="15", block="vf", text=
        "{t}Seis: [p=0.2] a largura deu menos dez, [p=0.2] que não serve. [p=0.2] Então a resposta é *dez.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque parece um conserto. [p=0.3] {g}Mas "
        "*descartar não é trocar o sinal:* [p=0.2] o menos dez vai *inteiro para a lixeira,* [p=0.2] e a resposta é a "
        "outra raiz."),
    dict(id="16", block="vf", text=
        "{t}Sete: [p=0.2] em xis ao quadrado, menos sete xis, mais dez, [p=0.2] a soma das raízes é *menos sete.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o menos sete está ali na equação. [p=0.3] {g}Mas a "
        "soma é *menos bê sobre á:* [p=0.2] o sinal do meio vem trocado. [p=0.2] *Mais sete,* [p=0.2] dois mais cinco."),
    dict(id="17", block="vf", text=
        "{t}Oito: [p=0.2] em xis à quarta, menos cinco xis ao quadrado, mais quatro, [p=0.2] as raízes são *um e quatro.* "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque um e quatro saem mesmo da conta. [p=0.3] {g}Mas "
        "esses são os valores do *y.* [p=0.2] A fantasia tem de sair: [p=0.2] *xis igual a mais ou menos um, e mais ou "
        "menos dois.*"),
    dict(id="18", block="vf", text=
        "{t}E nove: [p=0.2] antes de Bhaskara, [p=0.2] xis ao quadrado mais quatro xis igual a cento e quarenta [p=0.2] "
        "vira *xis ao quadrado, mais quatro xis, menos cento e quarenta, igual a zero.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Verdadeiro!* [p=0.3] {e}Parece falso porque dá vontade de usar cê igual a cento e quarenta. [p=0.3] {g}Mas a "
        "equação *só conversa arrumada:* [p=0.2] tudo de um lado, zero do outro."),
    dict(id="19", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas. [p=0.2] Em todas: [p=0.2] *iguale a zero, resolva e escolha a raiz que faz sentido.*"),

    # ================= QUESTÃO 1: ÁREA (MOLDURA) =================
    dict(id="20", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Um quadro de *trinta por vinte centímetros* [p=0.2] ganha uma *moldura* de largura "
        "xis, [p=0.2] em volta de todo o quadro. [p=0.2] Com a moldura, [p=0.2] a área total passa a ser *mil e duzentos "
        "centímetros quadrados.* [p=0.3] {b}A largura da moldura, em centímetros, é [p=0.4] {la}A, [p=0.2] cinco. [p=0.2] "
        "{lb}B, [p=0.2] dez. [p=0.2] {lc}C, [p=0.2] trinta. [p=0.2] {ld}D, [p=0.2] trinta e cinco. [p=0.2] {le}E, "
        "[p=0.2] seiscentos. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="21", block="q1", text=
        "{d}A moldura *abraça* o quadro: [p=0.2] cada medida cresce *dois xis.* [p=0.3] {a}Trinta mais dois xis, [p=0.2] "
        "vezes vinte mais dois xis, [p=0.2] igual a mil e duzentos. [p=0.3] {b}Iguale a zero e divida por quatro: "
        "[p=0.2] xis ao quadrado, mais vinte e cinco xis, menos cento e cinquenta. [p=0.3] {c}Soma menos vinte e cinco, "
        "[p=0.2] produto menos cento e cinquenta: [p=0.2] *cinco* e *menos trinta.* [p=0.2] O menos trinta vai para a "
        "lixeira. [p=0.2] {ok}*Letra A!* [p=0.3] {v}Confira: [p=0.2] quarenta vezes trinta, [p=0.2] mil e duzentos. "
        "[p=0.4] {xb}A B pôs a moldura de um lado só. [p=0.2] {xc}A C trocou o sinal do menos trinta. [p=0.2] {xd}A D "
        "parou na raiz do delta, [p=0.2] {xe}e a E deu a *área* da moldura."),

    # ================= QUESTÃO 2: PARÂMETRO (RAIZ DUPLA) =================
    dict(id="22", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Na equação *dois xis ao quadrado, menos doze xis, mais cá, igual a zero,* [p=0.2] o "
        "número cá foi escolhido [p=0.2] para que exista *uma única raiz real.* [p=0.3] {b}O valor de cá é [p=0.4] "
        "{la}A, [p=0.2] menos dezoito. [p=0.2] {lb}B, [p=0.2] um vírgula cinco. [p=0.2] {lc}C, [p=0.2] três. [p=0.2] "
        "{ld}D, [p=0.2] dezoito. [p=0.2] {le}E, [p=0.2] setenta e dois. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="23", block="q2", text=
        "{d}O porteiro deixa passar *uma só:* [p=0.2] *delta igual a zero.* [p=0.3] {a}Delta é "
        "bê ao quadrado, menos quatro á cê: [p=0.2] cento e quarenta e quatro, menos oito cá. [p=0.3] {b}Cento e quarenta "
        "e quatro menos oito cá, igual a zero: [p=0.2] *cá igual a dezoito.* [p=0.2] {ok}*Letra D!* [p=0.3] {v}Confira: "
        "[p=0.2] a raiz dupla é *três.* [p=0.4] {xa}A A fez menos doze ao quadrado negativo. [p=0.2] {xb}A B não elevou "
        "o bê. [p=0.2] {xc}A C respondeu a *raiz,* não o cá. [p=0.2] {xe}E a E esqueceu o quatro."),

    # ================= QUESTÃO 3: SOMA E PRODUTO (EQUAÇÃO PELAS RAÍZES) =================
    dict(id="24", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Uma equação do segundo grau, [p=0.2] com á igual a um, [p=0.2] tem raízes *menos "
        "três e sete.* [p=0.3] {b}Essa equação é [p=0.4] {la}A, [p=0.2] xis ao quadrado, mais quatro xis, menos vinte e "
        "um. [p=0.2] {lb}B, [p=0.2] xis ao quadrado, menos quatro xis, mais vinte e um. [p=0.2] {lc}C, [p=0.2] xis ao "
        "quadrado, menos dez xis, mais vinte e um. [p=0.2] {ld}D, [p=0.2] xis ao quadrado, menos vinte e um xis, menos "
        "quatro. [p=0.2] {le}E, [p=0.2] xis ao quadrado, menos quatro xis, menos vinte e um. [p=0.4] {p}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="25", block="q3", text=
        "{d}O jogo dos dois números, [p=0.2] ao contrário. [p=0.3] {a}Soma: [p=0.2] menos três mais sete, [p=0.2] "
        "*quatro.* [p=0.2] Produto: [p=0.2] menos três vezes sete, [p=0.2] *menos vinte e um.* [p=0.3] {b}A equação é "
        "xis ao quadrado, *menos a soma* xis, *mais o produto:* [p=0.2] menos quatro xis, menos vinte e um. [p=0.2] "
        "{ok}*Letra E!* [p=0.3] {xa}A A não trocou o sinal do meio. [p=0.2] {xb}A B perdeu o sinal do produto. [p=0.2] {xc}A C ignorou "
        "o menos do três, [p=0.2] {xd}e a D trocou a soma de lugar com o produto."),

    # ================= QUESTÃO 4: CONTAGEM (APERTOS DE MÃO) =================
    dict(id="26", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Numa reunião, [p=0.2] cada pessoa apertou a mão de cada uma das outras [p=0.2] "
        "*uma única vez.* [p=0.2] Foram *vinte e oito* apertos de mão. [p=0.3] {b}O número de pessoas na reunião é "
        "[p=0.4] {la}A, [p=0.2] sete. [p=0.2] {lb}B, [p=0.2] oito. [p=0.2] {lc}C, [p=0.2] catorze. [p=0.2] {ld}D, "
        "[p=0.2] vinte e oito. [p=0.2] {le}E, [p=0.2] cinquenta e seis. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="27", block="q4", text=
        "{d}Cada uma das ene pessoas aperta *ene menos um* mãos, [p=0.2] e cada aperto conta "
        "*duas vezes:* [p=0.2] divide por dois. [p=0.3] {a}Ene vezes ene menos um, sobre dois, [p=0.2] igual a vinte e oito. "
        "[p=0.3] {b}Ene ao quadrado, menos ene, menos cinquenta e seis, igual a zero. [p=0.2] Soma um, produto menos "
        "cinquenta e seis: [p=0.2] *oito* e *menos sete.* [p=0.2] {ok}*Oito pessoas. Letra B!* [p=0.3] {v}Confira: "
        "[p=0.2] oito vezes sete, sobre dois, [p=0.2] vinte e oito. [p=0.4] {xa}A A trocou o sinal do menos sete. "
        "[p=0.2] {xc}A C dividiu vinte e oito por dois. [p=0.2] {xd}A D respondeu os apertos, [p=0.2] {xe}e a E parou "
        "no cinquenta e seis."),

    # ================= QUESTÃO 5: LANÇAMENTO VERTICAL =================
    dict(id="28", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Uma bola é lançada para cima, [p=0.2] e sua altura, em metros, é *trinta tê "
        "menos cinco tê ao quadrado,* [p=0.2] com tê em segundos. [p=0.3] {b}Quanto tempo se passa [p=0.2] entre o "
        "instante em que ela passa por *vinte e cinco metros* subindo [p=0.2] e o instante em que passa descendo? "
        "[p=0.4] {la}A, [p=0.2] um segundo. [p=0.2] {lb}B, [p=0.2] três. [p=0.2] {lc}C, [p=0.2] quatro. [p=0.2] {ld}D, "
        "[p=0.2] cinco. [p=0.2] {le}E, [p=0.2] oito. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="29", block="q5", text=
        "{d}Iguale a altura a vinte e cinco. [p=0.3] {a}Trinta tê, menos cinco tê ao quadrado, igual a vinte e cinco. "
        "[p=0.2] Passe tudo para o lado direito [p=0.2] e divida por cinco: [p=0.2] tê ao quadrado, menos seis tê, mais cinco, "
        "igual a zero. [p=0.3] {b}Soma seis, produto cinco: [p=0.2] *um* e *cinco segundos.* [p=0.3] {c}Mas a pergunta "
        "é o *intervalo:* [p=0.2] cinco menos um, [p=0.2] *quatro segundos.* [p=0.2] {ok}*Letra C!* [p=0.4] {xa}A A e "
        "{xd}a D deram um instante só. [p=0.2] {xb}A B é a média dos instantes: [p=0.2] o topo, [p=0.2] que é assunto da "
        "Função quadrática. [p=0.2] {xe}E a E esqueceu de dividir por dois."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="30", block="checklist", text=
        "{t}O checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* "
        "para outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}Forma geral, [p=0.2] sinais [p=0.2] e incompletas: "
        "[p=0.2] episódio um. [p=0.3] {c}Bhaskara, [p=0.2] de onde vem a fórmula, [p=0.2] o delta [p=0.2] e o parâmetro: "
        "[p=0.2] episódio dois."),
    dict(id="31", block="checklist", text=
        "{a}Soma e produto [p=0.2] e a forma fatorada: [p=0.2] episódio três. [p=0.3] {b}Modelar e descartar: [p=0.2] "
        "episódio quatro. [p=0.3] {c}Biquadradas: [p=0.2] episódio cinco. [p=0.4] {d}O que você *não* marcou, [p=0.2] "
        "reveja o episódio correspondente."),

    # ================= META =================
    dict(id="32", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *trinta questões* [p=0.2] {b}e acerte pelo menos *vinte e uma,* [p=0.2] setenta "
        "por cento. [p=0.4] {c}E em pelo menos *dez* delas, [p=0.2] *você mesmo monta a equação* a partir do texto."),

    # ================= PONTE E CTA =================
    dict(id="33", block="ponte", text=
        "{a}O próximo assunto é *Sistemas de equações lineares,* [p=0.3] {b}onde *duas incógnitas* aparecem ao mesmo "
        "tempo."),
    dict(id="34", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual pegadinha te pegou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de equação do segundo grau está completa. [p=0.2] Bons estudos, e *até a próxima aula* "
        "aqui no Estudativo. [p=1.5]"),
]
