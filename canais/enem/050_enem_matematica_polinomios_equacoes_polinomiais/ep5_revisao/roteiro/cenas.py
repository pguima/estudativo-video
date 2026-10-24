# Roteiro — Polinômios e Equações Polinomiais, Episódio 5 de 5: Revisão geral, estratégia de prova, pegadinhas e treino
#   (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/35-polinomios-equacoes-polinomiais.html — seções 01, 10, 11 e 13.
#   NÃO usa a seção 12 (Q1–Q9). As 5 questões são INÉDITAS (dados, alternativas e motivos das erradas do PROMPT).
#   Números complexos: só i² = −1 e a ponte (série própria, a próxima).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (números e símbolos falados por extenso).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 o GRAU é o ANDAR MAIS ALTO do prédio · o RAIO X do P(1) (soma dos coeficientes) · as NOTAS FISCAIS conferidas item
#       por item (identidade) (ícone: caixa de papelão) ·
#   ep2 a ESTEIRA de Briot-Ruffini · o ATALHO DO PEDÁGIO (teorema do resto) · a raiz do divisor MORA DO LADO OPOSTO
#       (ícone: esteira) ·
#   ep3 raiz e fator como ESPELHOS · o MOLHO DE CHAVES das candidatas · cada raiz DERRUBA UM ANDAR (ícone: molho de chaves) ·
#   ep4 MENOS, MAIS, MENOS de Girard · a BOLA que QUICA ou ATRAVESSA · as raízes conjugadas como PAR DE MEIAS (ícone: bola).
# Prática de recuperação: a cena 04 abre com uma pergunta e pausa antes do índice; cada V/F e cada questão têm pausa.
# O que a prova cobra (seção 01): modelar (volume, área, lucro) · valor numérico e raízes · leitura de gráficos · relações
#   entre raízes e coeficientes. O material avisa: a teoria completa cai mais em vestibulares tradicionais.
# Onde aparece (seção 10): Geometria Espacial (volume de caixas) · Economia (raízes do lucro = equilíbrio) · Física (MUV,
#   "volta à origem" é raiz) · Números complexos (pares conjugados).
# Estratégia (seção 10): 4 hábitos — raiz? substitua · raiz dada é convite a Briot-Ruffini · soma ou produto? Girard ·
#   gráfico? P(0) de cada alternativa, depois raízes e multiplicidades.
# V/F (os 9 erros da seção 11, NA ORDEM do prompt). DESVIO NOSSO (marcado, como nas revisões anteriores): para o jogo não
#   ter resposta previsível, três frases aparecem na versão CERTA (verdadeiras: 2, 5 e 7); as outras seis são o erro
#   (falsas). Números nossos, conferidos em trabalho/conferir_questoes.py:
#   1 F raiz −2 → fator (x − 2) (certo x + 2) · 2 V em x³ − 4x + 1 a esteira usa 1, 0, −4, 1 · 3 F por x + 3 usa-se 3
#   (certo −3: em x³ − 4x + 1 o resto é −14, com 3 daria 16) · 4 F resto por x − a é P(−a) (x² + 3x + 1 por x − 2: P(2) =
#   11, e P(−2) = −1) · 5 V no 3º grau o produto é −d/a (x³ − 6x² + 11x − 6: 1 · 2 · 3 = 6) · 6 F as raízes bastam
#   (x² − 3x + 2 e 2x² − 6x + 4 têm raízes 1 e 2) · 7 V uma raiz dupla só toca ((x − 2)² nunca fica negativo) ·
#   8 F 1 − i sozinha (vem com 1 + i) · 9 F soma dos coeficientes = P(0) (2x² − 3x + 5: P(1) = 4, P(0) = 5).
# QUESTÕES INÉDITAS (dados exatos do prompt; conferidas em trabalho/conferir_questoes.py):
#   Q1 x²(x + 1) = 12 → x³ + x² − 12 = 0; candidata 2: 8 + 4 − 12 = 0; esteira 1, 1, 0, −12 com 2 → 1, 3, 6 e resto 0;
#      x² + 3x + 6: Δ = 9 − 24 < 0 → C (2 m). A 3 é a altura · B 4 a área da base · D 6 lê um coeficiente como raiz ·
#      E 12 toma o termo independente como raiz.
#   Q2 P(−2) = 16 − 12 − 2 + 2 = 4; esteira 1, 0, −3, 1, 2 com −2 → 1, −2, 1, −1 e resto 4 → A. B 8 = P(2) · C 2 = P(0) ·
#      D 1 = P(1) · E −20 esqueceu o 0 (tratou como x³ − 3x² + x + 2).
#   Q3 x³ − 9x² + 26x − 24: soma dos pares = 26 = metade da área total → 52 → E; arestas 2, 3, 4: 6 + 8 + 12 = 26.
#      C 26 esqueceu de dobrar · B 24 é o volume · A 9 a soma das arestas distintas · D 36 todas as 12 arestas (4 · 9).
#   Q4 P = a(x − 1)²(x + 3); P(0) = 3a = −6 → a = −2 → E. A P(0) = 3 (sem o a) · B troca os sinais (P(0) = 6) ·
#      C inverte as multiplicidades (P(0) = 18) · D erra o sinal de a (P(0) = 6).
#   Q5 (x − 1)(x − 2i)(x + 2i) = (x − 1)(x² + 4) = x³ − x² + 4x − 4 → A. B usa (2i)(−2i) = −4 (i² = 1) · C troca o sinal da
#      raiz 1 · D esquece a raiz 1 (grau 2) · E esquece o conjugado −2i (coeficientes não reais).
#   Em cada questão a pergunta "qual ferramenta resolve?" vem antes da conta (prompt: "qual das três frases do gancho").
#   A Q3 é Girard (hábito três), não uma das três frases: o vídeo diz isso.
# Gabaritos: C, A, E, E, A (letras e alternativas do prompt).
# Atalhos (verde): os 4 hábitos (cenas 08 e 09) · "teste as candidatas do termo independente" na Q1 · "o resto é o P da raiz
#   do divisor" na Q2 · "Girard: nem resolva" na Q3 · "P(0) primeiro" na Q4 · "o par de meias" na Q5.
# Checklist (seção 13) → episódio (como o prompt pede): grau, P(0), P(1), identidade e modelagem → ep1 · divisão,
#   Briot-Ruffini e restos → ep2 · forma fatorada, candidatas e redução de grau → ep3 · Girard, gráfico e conjugadas → ep4.
# Meta (prompt e material): 25 questões, 18 acertos, com pelo menos cinco de modelagem ou leitura de gráfico.
# Ponte (do usuário): Números complexos.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de polinômios: P(a), teorema do resto, Girard e as pegadinhas · Matemática ENEM, Polinômios ep. 5"

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
        "{a}Três frases resolvem quase toda questão de polinômio: [p=0.4] {b}*a* é raiz se *P de a* é igual a zero; "
        "[p=0.4] {c}o resto por *x menos a* é *P de a;* [p=0.4] {d}e uma raiz conhecida *baixa o grau* até o segundo. "
        "[p=0.5] {e}Hoje você treina as três."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E o que a prova pede? [p=0.4] {a}*Modelar:* [p=0.2] o volume de uma caixa, [p=0.2] uma área, [p=0.2] um "
        "lucro. [p=0.3] {b}*Valor numérico e raízes:* [p=0.2] o lucro se anula, [p=0.2] a altura volta a zero. [p=0.3] "
        "{c}*Ler gráficos:* [p=0.2] onde a curva corta ou toca o eixo. [p=0.3] {d}E as *relações entre raízes e "
        "coeficientes:* [p=0.2] a soma e o produto, sem resolver."),
    dict(id="03", block="rende", text=
        "{t}E um aviso do próprio material: [p=0.3] {a}a teoria completa de polinômios [p=0.2] cai mais nos "
        "*vestibulares tradicionais.* [p=0.4] {b}No ENEM, [p=0.2] o polinômio aparece como *modelo.* [p=0.2] E o que "
        "se pede é *usar a ferramenta certa.*"),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] tente lembrar: [p=0.2] *qual número você põe no lugar do x* [p=0.2] para achar a "
        "soma dos coeficientes? [p=1.2] {a}Um: [p=0.2] a *caixa de papelão.* [p=0.2] O grau é o *andar mais alto do "
        "prédio,* [p=0.2] o *P de um* é o *raio X* [p=0.2] que soma os coeficientes, [p=0.2] e a identidade confere as "
        "*notas fiscais item por item.* [p=0.4] {b}Dois: [p=0.2] a *esteira* de Briot-Ruffini, [p=0.2] o *atalho do "
        "pedágio,* [p=0.2] que dá o resto sem dividir, [p=0.2] e a raiz do divisor que *mora do lado oposto.*"),
    dict(id="05", block="indice", text=
        "{a}Três: [p=0.2] o *molho de chaves* das candidatas. [p=0.2] Raiz e fator são *espelhos,* [p=0.2] e cada raiz "
        "achada *derruba um andar.* [p=0.4] {b}Quatro: [p=0.2] a *bola.* [p=0.2] O *menos, mais, menos* de Girard, "
        "[p=0.2] a raiz que *quica ou atravessa* o eixo, [p=0.2] e as raízes conjugadas, [p=0.2] que andam como um *par "
        "de meias.*"),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="06", block="onde", text=
        "{t}E nas outras áreas? [p=0.4] {a}Na *Geometria Espacial,* [p=0.2] o volume de uma caixa [p=0.2] é o produto "
        "de três fatores do primeiro grau: [p=0.2] um polinômio de *grau três.* [p=0.3] {b}Na *Economia,* [p=0.2] as "
        "raízes do lucro [p=0.2] são os *pontos de equilíbrio.*"),
    dict(id="07", block="onde", text=
        "{c}Na *Física,* [p=0.2] a posição no movimento uniformemente variado é um polinômio, [p=0.2] e *voltar à "
        "origem* é achar uma raiz. [p=0.3] {d}E nos *Números complexos,* [p=0.2] as raízes não reais [p=0.2] vêm em "
        "*pares conjugados.*"),

    # ================= ESTRATÉGIA: 4 HÁBITOS (seção 10) =================
    dict(id="08", block="habitos", text=
        "{t}E na hora da prova? [p=0.2] Quatro hábitos. [p=0.4] {a}Um: [p=0.2] *raiz? Substitua.* [p=0.2] Calcular P de a "
        "é mais rápido que dividir. [p=0.4] {b}Dois: [p=0.2] uma raiz dada é um *convite a Briot-Ruffini.* [p=0.2] "
        "Divida por ela [p=0.2] e resolva o segundo grau que sobra."),
    dict(id="09", block="habitos", text=
        "{c}Três: [p=0.2] pediu *soma ou produto?* [p=0.2] *Girard.* [p=0.2] Nem resolva a equação. [p=0.4] {d}Quatro: "
        "[p=0.2] *gráfico?* [p=0.2] Calcule o *P de zero* de cada alternativa [p=0.2] e compare com o ponto do eixo "
        "vertical. [p=0.2] Depois, as raízes [p=0.2] e as multiplicidades."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="10", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="11", block="vf", text=
        "{t}Um: [p=0.2] se *menos dois* é raiz, [p=0.2] o fator é *x menos dois.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque o dois aparece nos dois lugares. [p=0.3] {g}Mas raiz e fator são "
        "*espelhos:* [p=0.2] sinais opostos. [p=0.2] Raiz menos dois, [p=0.2] fator *x mais dois.*"),
    dict(id="12", block="vf", text=
        "{t}Dois: [p=0.2] em *x ao cubo menos quatro x mais um,* [p=0.2] a esteira usa os coeficientes *um, zero, menos "
        "quatro e um.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque o x ao quadrado nem "
        "aparece. [p=0.3] {g}Mas na esteira, [p=0.2] *todo andar tem lugar:* [p=0.2] o que falta entra com *zero.*"),
    dict(id="13", block="vf", text=
        "{t}Três: [p=0.2] para dividir por *x mais três,* [p=0.2] a esteira usa o *três.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque o três está escrito ali. [p=0.3] {g}Mas a raiz do divisor *mora do lado "
        "oposto:* [p=0.2] x mais três zera em *menos três.*"),
    dict(id="14", block="vf", text=
        "{t}Quatro: [p=0.2] o resto da divisão por *x menos a* [p=0.2] é *P de menos a.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque tem um menos no divisor. [p=0.3] {g}Mas o atalho do pedágio usa a *raiz "
        "do divisor:* [p=0.2] x menos a zera em *a.* [p=0.2] O resto é *P de a.*"),
    dict(id="15", block="vf", text=
        "{t}Cinco: [p=0.2] no terceiro grau, [p=0.2] o produto das raízes é *menos d sobre a.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque no segundo grau era *c sobre a,* sem o menos. [p=0.3] "
        "{g}Mas no terceiro, [p=0.2] os sinais de Girard são *menos, mais, menos:* [p=0.2] o produto leva o último "
        "menos."),
    dict(id="16", block="vf", text=
        "{t}Seis: [p=0.2] sabendo as raízes, [p=0.2] o polinômio está *identificado.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque as raízes parecem dizer tudo. [p=0.3] {g}Mas falta o *coeficiente "
        "dominante:* [p=0.2] *x ao quadrado menos três x mais dois* [p=0.2] e o *dobro* dele [p=0.2] têm as mesmas "
        "raízes, um e dois."),
    dict(id="17", block="vf", text=
        "{t}Sete: [p=0.2] uma raiz de *multiplicidade dois* [p=0.2] só *toca* o eixo, [p=0.2] sem atravessar. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque parece que toda raiz corta o eixo. [p=0.3] "
        "{g}Mas a bola *quica:* [p=0.2] *x menos dois, ao quadrado,* [p=0.2] nunca fica negativo."),
    dict(id="18", block="vf", text=
        "{t}Oito: [p=0.2] com coeficientes reais, [p=0.2] *um menos i* pode ser raiz *sozinha.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o enunciado só cita uma. [p=0.3] {g}Mas raízes não reais andam "
        "como um *par de meias:* [p=0.2] se um menos i é raiz, [p=0.2] *um mais i* também é."),
    dict(id="19", block="vf", text=
        "{t}E nove: [p=0.2] a soma dos coeficientes [p=0.2] é o *P de zero.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* "
        "[p=0.3] {e}Engana porque o zero parece o ponto de partida. [p=0.3] {g}Mas P de zero é só o *termo "
        "independente.* [p=0.2] A soma é o *raio X:* [p=0.2] *P de um.*"),
    dict(id="20", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas. [p=0.2] Em todas: [p=0.2] *escolha a ferramenta,* [p=0.2] resolva [p=0.2] e *confira.*"),

    # ================= QUESTÃO 1: MODELAGEM COM RAIZ POR TESTE =================
    dict(id="21", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Um reservatório em forma de bloco [p=0.2] tem base quadrada de lado *x metros* "
        "[p=0.2] e altura *x mais um metros.* [p=0.2] Seu volume é *doze metros cúbicos.* [p=0.3] {b}O lado da base "
        "mede: [p=0.4] {la}A, [p=0.2] três metros. [p=0.2] {lb}B, [p=0.2] quatro metros. [p=0.2] {lc}C, [p=0.2] dois "
        "metros. [p=0.2] {ld}D, [p=0.2] seis metros. [p=0.2] {le}E, [p=0.2] doze metros. [p=0.4] {p}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="22", block="q1", text=
        "{d}Qual frase resolve? [p=0.2] Testar a raiz [p=0.2] e depois *baixar o grau.* [p=0.3] {a}x ao quadrado vezes "
        "x mais um, igual a doze: [p=0.2] *x ao cubo mais x ao quadrado menos doze, igual a zero.* [p=0.2] Teste o "
        "*dois:* [p=0.2] oito mais quatro menos doze, *zero.* [p=0.3] {b}Na esteira, [p=0.2] *um, um, zero, menos "
        "doze,* [p=0.2] com o dois: [p=0.2] sobra *x ao quadrado mais três x mais seis,* [p=0.2] com delta negativo. "
        "[p=0.2] Não há outra raiz real. [p=0.2] {ok}*Letra C!* [p=0.4] {xa}A A é a altura, [p=0.2] {xb}a B é a área "
        "da base, [p=0.2] {xd}a D leu um coeficiente como raiz, [p=0.2] {xe}e a E tomou o termo independente."),

    # ================= QUESTÃO 2: TEOREMA DO RESTO =================
    dict(id="23", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}O resto da divisão de *x à quarta menos três x ao quadrado mais x mais dois* "
        "[p=0.2] por *x mais dois* é: [p=0.4] {la}A, [p=0.2] quatro. [p=0.2] {lb}B, [p=0.2] oito. [p=0.2] {lc}C, "
        "[p=0.2] dois. [p=0.2] {ld}D, [p=0.2] um. [p=0.2] {le}E, [p=0.2] menos vinte. [p=0.4] {p}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="24", block="q2", text=
        "{d}Qual frase resolve? [p=0.2] *O resto é P da raiz do divisor.* [p=0.2] E x mais dois zera em *menos dois.* "
        "[p=0.3] {a}P de menos dois: [p=0.2] dezesseis, menos doze, menos dois, mais dois: [p=0.2] *quatro.* [p=0.3] "
        "{v}Na esteira, com o *zero* do x ao cubo: [p=0.2] um, menos dois, um, menos um [p=0.2] e resto *quatro.* "
        "[p=0.2] {ok}*Letra A!* [p=0.4] {xb}A B usou P de dois. [p=0.2] {xc}A C é P de zero, [p=0.2] {xd}a D é P de "
        "um, [p=0.2] {xe}e a E esqueceu o zero na esteira."),

    # ================= QUESTÃO 3: GIRARD NO BLOCO =================
    dict(id="25", block="q3", text=
        "{t}Questão três. [p=0.3] {a}As arestas de uma caixa, em centímetros, [p=0.2] são as raízes de *x ao cubo "
        "menos nove x ao quadrado mais vinte e seis x menos vinte e quatro.* [p=0.3] {b}A área total da caixa, em "
        "centímetros quadrados, é: [p=0.4] {la}A, [p=0.2] nove. [p=0.2] {lb}B, [p=0.2] vinte e quatro. [p=0.2] "
        "{lc}C, [p=0.2] vinte e seis. [p=0.2] {ld}D, [p=0.2] trinta e seis. [p=0.2] {le}E, [p=0.2] cinquenta e dois. "
        "[p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q3", text=
        "{d}Aqui não é nenhuma das três frases: [p=0.2] é o *hábito três,* [p=0.2] Girard. [p=0.2] Nem resolva. "
        "[p=0.3] {a}A área total soma *dois de cada face:* [p=0.2] o dobro da soma dos produtos dois a dois. [p=0.2] "
        "Pelo menos, mais, menos, [p=0.2] essa soma é *vinte e seis.* [p=0.2] Dobrando, [p=0.2] *cinquenta e dois.* "
        "[p=0.3] {v}Conferindo: [p=0.2] as arestas são dois, três e quatro, [p=0.2] e seis mais oito mais doze dá vinte "
        "e seis. [p=0.2] {ok}*Letra E!* [p=0.4] {xc}A C esqueceu de dobrar. [p=0.2] {xb}A B é o volume, [p=0.2] {xa}a "
        "A é a soma das arestas, [p=0.2] {xd}e a D é o comprimento de todas as doze arestas."),

    # ================= QUESTÃO 4: LEI A PARTIR DO GRÁFICO =================
    dict(id="27", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Um polinômio de grau três [p=0.2] apenas *toca* o eixo horizontal em *x igual a "
        "um,* [p=0.2] *atravessa* esse eixo em *x igual a menos três* [p=0.2] e corta o eixo vertical em *zero, menos "
        "seis.* [p=0.3] {b}A lei é: [p=0.3] {la}A, [p=0.2] {lb}B, [p=0.2] {lc}C, [p=0.2] {ld}D [p=0.2] {le}ou E. "
        "[p=0.2] Estão na tela. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="28", block="q4", text=
        "{d}Qual frase resolve? [p=0.2] A raiz vira fator, [p=0.2] e o *hábito quatro:* [p=0.2] P de zero. [p=0.3] "
        "{a}Toca em um: [p=0.2] a bola quica, [p=0.2] *x menos um, ao quadrado.* [p=0.2] Atravessa em menos três: "
        "[p=0.2] *x mais três.* [p=0.2] E falta o *a* na frente. [p=0.3] {b}P de zero: [p=0.2] a vezes um vezes três, "
        "[p=0.2] *três a, igual a menos seis.* [p=0.2] Então *a é menos dois.* [p=0.2] {ok}*Letra E!* [p=0.4] {xa}A A "
        "esqueceu o coeficiente dominante. [p=0.2] {xb}A B trocou os sinais das raízes, [p=0.2] {xc}a C inverteu as "
        "multiplicidades, [p=0.2] {xd}e a D errou o sinal do a."),

    # ================= QUESTÃO 5: RAÍZES CONJUGADAS =================
    dict(id="29", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Um polinômio de grau três, [p=0.2] com coeficientes reais e coeficiente "
        "dominante *um,* [p=0.2] tem raízes *um* e *dois i.* [p=0.2] Lembrando: [p=0.2] *i ao quadrado é menos um.* "
        "[p=0.3] {b}Ele é: [p=0.3] {la}A, [p=0.2] {lb}B, [p=0.2] {lc}C, [p=0.2] {ld}D [p=0.2] {le}ou E, [p=0.2] na "
        "tela. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="30", block="q5", text=
        "{d}Qual frase resolve? [p=0.2] Raiz vira fator, [p=0.2] e o *par de meias:* [p=0.2] se dois i é raiz, [p=0.2] "
        "*menos dois i* também é. [p=0.3] {a}Dois i vezes menos dois i: [p=0.2] *menos quatro i ao quadrado,* [p=0.2] "
        "que dá *mais quatro.* [p=0.2] Fica *x ao quadrado mais quatro.* [p=0.2] Vezes *x menos um:* [p=0.2] *x ao cubo "
        "menos x ao quadrado mais quatro x menos quatro.* [p=0.2] {ok}*Letra A!* [p=0.4] {xb}A B fez i ao quadrado "
        "igual a um. [p=0.2] {xc}A C trocou o sinal da raiz um, [p=0.2] {xd}a D esqueceu a raiz um, [p=0.2] {xe}e a E "
        "esqueceu o conjugado."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="31", block="checklist", text=
        "{t}O checklist. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* para outra pessoa, [p=0.2] "
        "sem consultar nada. [p=0.4] {b}Grau, P de zero, P de um, [p=0.2] identidade e modelagem: [p=0.2] episódio "
        "um. [p=0.3] {c}Divisão, Briot-Ruffini e restos: [p=0.2] episódio dois."),
    dict(id="32", block="checklist", text=
        "{a}Forma fatorada, candidatas [p=0.2] e redução de grau: [p=0.2] episódio três. [p=0.3] {b}Girard, gráfico e "
        "conjugadas: [p=0.2] episódio quatro. [p=0.4] {c}O que você *não* marcou, [p=0.2] reveja o episódio "
        "correspondente."),

    # ================= META =================
    dict(id="33", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *vinte e cinco questões* [p=0.2] {b}e acerte pelo menos *dezoito.* [p=0.4] "
        "{c}Com pelo menos *cinco* de modelagem [p=0.2] ou leitura de gráfico."),

    # ================= PONTE (frase do usuário) E CTA =================
    dict(id="34", block="ponte", text=
        "{a}O próximo assunto é *Números complexos,* [p=0.3] {b}que explica de vez as raízes não reais que apareceram "
        "aqui, [p=0.3] {c}como *um menos i* e *dois i.*"),
    dict(id="35", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] {com}E me conte nos "
        "*comentários:* [p=0.2] qual pegadinha te pegou? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo "
        "tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] "
        "para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}A série de polinômios está completa. [p=0.2] "
        "Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
