# Roteiro — Função logarítmica e aplicações (pH, Richter, decibéis), Episódio 5 de 5: Revisão geral, estratégia de
#   prova, pegadinhas e treino (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/28-funcao-logaritmica-aplicacoes.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (Q1–Q9). As 5 questões são INÉDITAS (números e alternativas do prompt do usuário).
#   Só as fórmulas do material: pH = −log[H⁺] · M = log(A/A₀) · log E = 4,8 + 1,5M · M_w = (2/3) · log M₀ − 10,7 ·
#   β = 10 · log(I/I₀), I₀ = 10⁻¹² W/m².
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (números por extenso; o gancho só acrescenta, depois delas, o que a aula
#   vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 o ESPELHO na reta y = x · o RETORNO DECRESCENTE · a PORTA do log fechada para o zero e os negativos
#       (ícone: espelho na reta y = x) ·
#   ep2 a RÉGUA DE ZEROS · diferença de leitura = EXPOENTE DA RAZÃO · o pH DE CABEÇA PARA BAIXO (ícone: régua de pH) ·
#   ep3 os DOIS PLACARES do terremoto · a CONSTANTE QUE SE CANCELA · DESFAZER DE FORA PARA DENTRO (ícone: dois placares) ·
#   ep4 cada 10 dB, UM ZERO A MAIS · o 10 QUE COME UM ZERO · os COPOS DE ÁGUA NO BALDE (ícone: medidor de decibéis).
# O que a prova cobra (seção 01): comparar numa escala (a campeã) · calcular com a fórmula dada · ler o gráfico ·
#   domínio. O que mais rende: diferença de leituras = expoente da razão (pH 3 × pH 6 → 10³; decibéis: 40 dB → 10⁴).
# Onde aparece (seção 10): Química (chuva ácida abaixo de 5,6) · Física (+10 dB = ×10; volume percebido não é
#   proporcional) · Geografia (danos dependem também da profundidade e das construções) · Biologia (sangue perto de 7,4).
# CORREÇÃO DO MATERIAL E DO PROMPT (hábito 1 da seção 09): "divida a diferença pelo coeficiente (10 nos decibéis, 1,5 na
#   energia...)" só vale nos DECIBÉIS, onde o 10 multiplica o log. Na ENERGIA (log E = 4,8 + 1,5M) o coeficiente
#   MULTIPLICA: de 5 para 7, 1,5 · 2 = 3 → 10³ = 1 000 vezes (dividir daria 10^(2/1,5) ≈ 22). É o que o ep. 3 já ensina
#   ("multiplique a diferença pelo coeficiente e eleve 10"). O vídeo diz: decibéis, divida por 10; energia, multiplique
#   por 1,5; pH e amplitude, a diferença já é o expoente.
# V/F (os 9 erros da seção 11, NA ORDEM do prompt). DESVIO NOSSO (marcado): para o jogo não ter resposta previsível, três
#   frases aparecem na versão CERTA (verdadeiras: 4, 6 e 9); as outras seis são o erro do prompt (falsas):
#   1 F pH 2 e pH 5: 3 vezes mais ácido (1 000) · 2 F +1 dB = ×10 (+10 dB) · 3 F 80 + 80 = 160 dB (≈ 83) ·
#   4 V +2 graus: energia ×1 000 · 5 F pH maior = mais ácido · 6 V log(2 · 10⁻⁵) = 0,30 − 5 · 7 F domínio de
#   log(2x − 6): x ≥ 3 (x > 3) · 8 F log₀,₅ x > 2 ⇒ x > 0,25 (0 < x < 0,25) · 9 V o log cresce cada vez mais devagar.
# QUESTÕES INÉDITAS (do prompt; conferidas em trabalho/conferir_questoes.py: uma única correta; cada errada = um erro
#   clássico; a ordem das letras é nossa):
#   Q1 domínio de log(x² − 16): x² > 16 → x < −4 ou x > 4 → E. A x > 4 (esqueceu o ramo negativo) · B x > 16 (comparou
#      x com 16) · C −4 < x < 4 (inverteu a região) · D x ≤ −4 ou x ≥ 4 (aceitou o zero dentro do log).
#   Q2 refrigerante pH 2,5 × iogurte pH 4,5: diferença 2 → 10² → D (100 vezes MAIOR: menor pH, mais H⁺). A 1,8 vez
#      (dividiu os pHs) · B 2 vezes (parou na diferença) · C 20 vezes (diferença × 10) · E 100 vezes menor (inverteu).
#   Q3 [H⁺] = 4 · 10⁻⁶, log 2 = 0,30: atalho do ep. 2 (k · 10⁻ⁿ → entre n − 1 e n: entre 5 e 6) · log 4 = 0,60 →
#      pH = 6 − 0,60 = 5,4 → A (abaixo de 5,6: chuva ácida). B 5,7 (log 2 no lugar de log 4) · C 6,0 (ignorou o 4) ·
#      D 6,3 (somou log 2) · E 6,6 (somou log 4: sinal).
#   Q4 M = log(A/A₀), magnitudes 4 e 7: amplitude, coeficiente 1 → 10³ → D (1 000 vezes). A 1,75 (dividiu as
#      magnitudes) · B 3 (parou na diferença) · C 30 (diferença × 10) · E ≈ 31 600 (razão das ENERGIAS, 10^4,5).
#   Q5 show, I = 10⁻¹ W/m²: I ÷ I₀ = 10¹¹ → 10 · 11 = 110 dB → C (bem acima de 85 dB). A −10 (não dividiu por I₀) ·
#      B 11 (esqueceu o fator 10) · D 120 (só o expoente de I₀) · E 130 (somou os expoentes em módulo, 1 + 12).
# Gabaritos: E, D, A, D, C.
# Atalhos (verde): os 3 hábitos (cenas 08 e 09) e o atalho do pH na Q3 (já ensinado no ep. 2).
# Checklist (seção 13) → episódio (como o prompt pede): lei, domínio, imagem, gráficos, (1, 0) e (b, 1), sinal e
#   inequações → ep1 · diferença em razão, pH e acidez → ep2 · amplitude × energia e fórmula de magnitude → ep3 ·
#   decibéis e soma de fontes → ep4.
# Meta (prompt e material): 30 questões, 21 acertos (70%), com pelo menos dez de comparação em escala.
# Ponte (do usuário): Função modular e funções definidas por partes.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de função logarítmica: pH, terremotos e decibéis em 5 questões | Função Logarítmica Ep. 5"
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
        "{a}Acidez, [p=0.2] terremotos [p=0.2] e barulho: [p=0.3] três assuntos de três áreas diferentes, [p=0.3] {b}uma "
        "única regra matemática. [p=0.4] {c}Hoje você treina a regra que o ENEM mais cobra quando o assunto é logaritmo: "
        "[p=0.3] *\"quantas vezes maior\".* [p=0.4] {d}Nove frases de verdadeiro ou falso [p=0.2] e cinco questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E o que a prova pede? [p=0.4] {a}*Comparar* numa escala: [p=0.2] quantas vezes mais ácido, [p=0.2] mais "
        "energia. [p=0.2] É a pergunta campeã. [p=0.3] {b}*Calcular com a fórmula dada.* [p=0.3] "
        "{c}*Ler o gráfico* da função logarítmica. [p=0.3] {d}E achar o *domínio.*"),
    dict(id="03", block="rende", text=
        "{t}E o que mais rende? [p=0.3] Uma regra só: [p=0.2] *a diferença entre duas leituras é o expoente da razão.* "
        "[p=0.4] {a}pê agá três contra pê agá seis: [p=0.2] diferença três, [p=0.2] dez ao cubo, *mil vezes.* [p=0.4] "
        "{b}Nos decibéis, [p=0.2] divida por dez antes: [p=0.2] quarenta decibéis a mais dão *dez elevado a quatro.*"),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] relembre cada episódio. [p=0.4] {a}Um: [p=0.2] o log é a exponencial no *espelho* da "
        "reta y igual a xis. [p=0.2] Ele tem *retorno decrescente,* [p=0.2] e a *porta* do log é fechada para o zero e os "
        "negativos. [p=0.4] {b}Dois: [p=0.2] a *régua de zeros.* [p=0.2] A diferença de leitura é o *expoente da razão,* "
        "[p=0.2] e o pê agá é *de cabeça para baixo.*"),
    dict(id="05", block="indice", text=
        "{a}Três: [p=0.2] os *dois placares* do terremoto. [p=0.2] Na comparação, [p=0.2] a *constante se cancela;* "
        "[p=0.2] e para voltar, [p=0.2] *desfaça de fora para dentro.* [p=0.4] {b}Quatro: [p=0.2] cada dez decibéis, "
        "[p=0.2] *um zero a mais.* [p=0.2] O dez da fórmula *come um zero,* [p=0.2] e intensidades se somam como *copos "
        "de água num balde.*"),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="06", block="onde", text=
        "{t}E as outras provas? [p=0.4] {a}Na *Química,* [p=0.2] chuva com pê "
        "agá abaixo de *cinco vírgula seis* é considerada ácida. [p=0.3] {b}Na *Física,* [p=0.2] o nível sonoro: [p=0.2] "
        "mais dez decibéis, [p=0.2] intensidade dez vezes maior. [p=0.2] E o volume que você sente *não é proporcional* a ela."),
    dict(id="07", block="onde", text=
        "{c}Na *Geografia,* [p=0.2] os terremotos: [p=0.2] os danos dependem "
        "também da *profundidade* e das *construções.* [p=0.3] {d}E na *Biologia,* [p=0.2] o sangue fica perto de pê agá "
        "*sete vírgula quatro:* [p=0.2] uma pequena variação de pê agá [p=0.2] é uma *grande* variação de agá mais."),

    # ================= ESTRATÉGIA: 3 HÁBITOS (seção 09) =================
    dict(id="08", block="habitos", text=
        "{t}E na hora da prova? [p=0.2] Três hábitos. [p=0.4] {a}Um: [p=0.2] *\"quantas vezes\" pede razão,* não "
        "diferença. [p=0.2] Ache a diferença e ajuste pelo coeficiente: [p=0.2] {a2}nos decibéis, "
        "*divida por dez;* [p=0.2] na energia do terremoto, *multiplique por um vírgula cinco;* [p=0.2] no pê agá e na "
        "amplitude, [p=0.2] a diferença *já é* o expoente. [p=0.3] {a3}Depois, eleve dez ao resultado."),
    dict(id="09", block="habitos", text=
        "{b}Dois: [p=0.2] para calcular a leitura, [p=0.2] *isole o log* e opere na ordem certa; [p=0.2] para voltar, "
        "desfaça de fora para dentro. [p=0.4] {c}Três: [p=0.2] *confira o sentido.* [p=0.2] No pê agá, [p=0.2] menor "
        "leitura é *mais* agá mais. [p=0.2] Nas outras escalas, [p=0.2] maior leitura, grandeza maior."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="10", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="11", block="vf", text=
        "{t}Um: [p=0.2] uma solução de pê agá dois [p=0.2] é *três vezes* mais ácida que uma de pê agá cinco. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o três está na diferença. [p=0.3] {g}Mas a "
        "diferença é o *expoente:* [p=0.2] dez ao cubo, [p=0.2] *mil vezes.*"),
    dict(id="12", block="vf", text=
        "{t}Dois: [p=0.2] *um* decibel a mais [p=0.2] deixa a intensidade dez vezes maior. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque, no pê agá, um passo já vale dez vezes. [p=0.3] {g}Mas o dez da fórmula "
        "*come um zero:* [p=0.2] são *dez* decibéis para cada dez vezes."),
    dict(id="13", block="vf", text=
        "{t}Três: [p=0.2] duas máquinas de oitenta decibéis, juntas, [p=0.2] fazem *cento e sessenta.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque parece uma soma comum. [p=0.3] {g}Mas quem se soma é a "
        "intensidade, [p=0.2] os *copos no balde.* [p=0.2] Dobrar dá só uns *três decibéis* a mais: [p=0.2] cerca de "
        "oitenta e três."),
    dict(id="14", block="vf", text=
        "{t}Quatro: [p=0.2] dois graus a mais de magnitude [p=0.2] deixam a *energia* mil vezes maior. [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque, na amplitude, dois graus dão só cem vezes. [p=0.3] "
        "{g}Mas é o *outro placar:* [p=0.2] um vírgula cinco vezes dois é três, [p=0.2] *dez ao cubo.*"),
    dict(id="15", block="vf", text=
        "{t}Cinco: [p=0.2] quanto *maior* o pê agá, [p=0.2] mais ácida a solução. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* "
        "[p=0.3] {e}Engana porque número maior parece \"mais\". [p=0.3] {g}Mas a escala é *de cabeça para baixo:* [p=0.2] "
        "o sinal de menos inverte. [p=0.2] *Menor* pê agá, mais ácido."),
    dict(id="16", block="vf", text=
        "{t}Seis: [p=0.2] log de dois vezes dez elevado a menos cinco [p=0.2] é *zero vírgula trinta, menos cinco.* "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque muita gente *multiplica:* [p=0.2] log "
        "de dois vezes menos cinco. [p=0.3] {g}Mas log do produto é *soma:* [p=0.2] dá menos quatro vírgula setenta."),
    dict(id="17", block="vf", text=
        "{t}Sete: [p=0.2] o domínio de log de dois xis menos seis [p=0.2] é *xis maior ou igual a três.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o \"igual\" parece inofensivo. [p=0.3] {g}Mas com xis "
        "igual a três, [p=0.2] dentro do log fica *zero,* [p=0.2] e a porta é fechada para o zero. [p=0.2] *Xis maior que "
        "três.*"),
    dict(id="18", block="vf", text=
        "{t}Oito: [p=0.2] log de xis na base zero vírgula cinco, maior que dois, [p=0.2] dá *xis maior que zero vírgula "
        "vinte e cinco.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque parece a conta de sempre. [p=0.3] {g}Mas base *menor que um* inverte o sentido, [p=0.2] e o domínio continua valendo: [p=0.2] "
        "*xis entre zero e zero vírgula vinte e cinco.*"),
    dict(id="19", block="vf", text=
        "{t}E nove: [p=0.2] o logaritmo cresce [p=0.2] *cada vez mais devagar.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Verdadeiro!* [p=0.3] {e}Parece falso porque o gráfico nunca para de subir. [p=0.3] {g}Mas é o *retorno "
        "decrescente:* [p=0.2] para subir um degrau, [p=0.2] xis precisa ser multiplicado pela base."),
    dict(id="20", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas. [p=0.2] Em todas: [p=0.2] *escreva a diferença das leituras* antes de qualquer conta [p=0.2] "
        "e *confira o sentido* no fim."),

    # ================= QUESTÃO 1: DOMÍNIO =================
    dict(id="21", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Para quais valores reais de xis [p=0.2] a função *f de xis igual a log de xis ao "
        "quadrado menos dezesseis* [p=0.2] está definida? [p=0.4] {la}A, [p=0.2] xis maior que quatro. [p=0.2] {lb}B, "
        "[p=0.2] xis maior que dezesseis. [p=0.2] {lc}C, [p=0.2] xis entre menos quatro e quatro. [p=0.2] {ld}D, [p=0.2] "
        "xis menor ou igual a menos quatro, [p=0.2] ou maior ou igual a quatro. [p=0.2] {le}E, [p=0.2] xis menor que menos "
        "quatro, [p=0.2] ou maior que quatro. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q1", text=
        "{d}A porta do log: [p=0.2] xis ao quadrado menos dezesseis, [p=0.2] *maior que zero.* [p=0.2] Xis ao quadrado "
        "maior que dezesseis. [p=0.3] {a}Isso vale para xis *maior que quatro* [p=0.2] e também para xis *menor que menos "
        "quatro:* [p=0.2] menos cinco ao quadrado é vinte e cinco. [p=0.2] {ok}*Letra E!* [p=0.4] {xa}A A esqueceu o "
        "ramo *negativo.* [p=0.2] {xb}A B comparou xis com dezesseis. [p=0.2] {xc}A C *inverteu* a região, [p=0.2] {xd}e "
        "a D deixou entrar o *zero:* [p=0.2] com xis igual a quatro, dentro do log fica zero."),

    # ================= QUESTÃO 2: COMPARAR ACIDEZ =================
    dict(id="23", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Um refrigerante tem pê agá *dois vírgula cinco,* [p=0.2] e um iogurte, pê agá "
        "*quatro vírgula cinco.* [p=0.3] {b}A concentração de agá mais no refrigerante, [p=0.2] em relação à do iogurte, "
        "é: [p=0.4] {la}A, [p=0.2] um vírgula oito vez maior. [p=0.2] {lb}B, [p=0.2] duas vezes maior. [p=0.2] {lc}C, "
        "[p=0.2] vinte vezes maior. [p=0.2] {ld}D, [p=0.2] cem vezes maior. [p=0.2] {le}E, [p=0.2] cem vezes menor. "
        "[p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="24", block="q2", text=
        "{d}Escreva a diferença primeiro: [p=0.2] quatro vírgula cinco menos dois vírgula cinco, [p=0.2] *dois.* [p=0.3] "
        "{a}No pê agá, [p=0.2] a diferença já é o expoente: [p=0.2] dez ao quadrado, *cem vezes.* [p=0.3] {b}E o sentido? "
        "[p=0.2] O refrigerante tem o pê agá *menor,* [p=0.2] então tem *mais* agá mais. [p=0.2] {ok}*Letra D!* [p=0.4] "
        "{xa}A A *dividiu* os pê agás, [p=0.2] {xb}a B parou na diferença, [p=0.2] {xc}a C multiplicou por dez, "
        "[p=0.2] {xe}e a E inverteu o sentido."),

    # ================= QUESTÃO 3: pH COM COEFICIENTE =================
    dict(id="25", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Uma amostra de água de chuva tem *agá mais igual a quatro vezes dez elevado a menos "
        "seis* mol por litro. [p=0.2] Use log de dois igual a zero vírgula trinta. [p=0.3] {b}O pê agá da amostra é: "
        "[p=0.4] {la}A, [p=0.2] cinco vírgula quatro. [p=0.2] {lb}B, [p=0.2] cinco vírgula sete. [p=0.2] {lc}C, [p=0.2] "
        "seis. [p=0.2] {ld}D, [p=0.2] seis vírgula três. [p=0.2] {le}E, [p=0.2] seis vírgula seis. [p=0.4] {p}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="26", block="q3", text=
        "{d}Atalho do episódio dois: [p=0.2] quatro vezes dez à menos seis [p=0.2] tem pê agá *entre cinco e seis.* "
        "[p=0.2] Só sobram A e B. [p=0.3] {a}Log de quatro é duas vezes log de dois: [p=0.2] *zero vírgula sessenta.* "
        "[p=0.2] pê agá é menos o log: [p=0.2] seis menos zero vírgula sessenta, [p=0.2] *cinco vírgula quatro.* [p=0.2] "
        "{ok}*Letra A!* [p=0.2] {v}E abaixo de cinco vírgula seis: [p=0.2] é *chuva ácida.* [p=0.4] {xb}A B usou log de "
        "*dois* no lugar de log de quatro. [p=0.2] {xc}A C ignorou o quatro, [p=0.2] {xd}{xe}e a D e a E *somaram* o log: "
        "[p=0.2] erro de sinal."),

    # ================= QUESTÃO 4: AMPLITUDE × ENERGIA =================
    dict(id="27", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Com *M igual a log de A sobre A zero,* [p=0.2] compare um tremor de magnitude "
        "*quatro* [p=0.2] e outro de magnitude *sete.* [p=0.3] {b}A *amplitude* registrada no segundo, [p=0.2] em relação "
        "ao primeiro, é: [p=0.4] {la}A, [p=0.2] um vírgula setenta e cinco vez maior. [p=0.2] {lb}B, [p=0.2] três vezes "
        "maior. [p=0.2] {lc}C, [p=0.2] trinta vezes maior. [p=0.2] {ld}D, [p=0.2] mil vezes maior. [p=0.2] {le}E, [p=0.2] "
        "cerca de trinta e um mil e seiscentas vezes maior. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="28", block="q4", text=
        "{d}A diferença: [p=0.2] sete menos quatro, [p=0.2] *três graus.* [p=0.3] {a}A pergunta é a *amplitude:* [p=0.2] "
        "o placar de dez em dez. [p=0.2] A diferença já é o expoente: [p=0.2] dez ao cubo, *mil vezes.* [p=0.2] {ok}*Letra "
        "D!* [p=0.4] {xe}A E caiu no *outro placar:* [p=0.2] é a razão das *energias,* [p=0.2] dez elevado a quatro "
        "vírgula cinco. [p=0.3] {xa}A A dividiu as magnitudes, [p=0.2] {xb}a B parou na diferença, [p=0.2] {xc}e a C "
        "multiplicou por dez."),

    # ================= QUESTÃO 5: CALCULAR DECIBÉIS =================
    dict(id="29", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Num show, [p=0.2] a intensidade sonora perto do palco é *dez elevado a menos "
        "um* watt por metro quadrado. [p=0.3] {b}Com *beta igual a dez vezes log de I sobre I zero,* [p=0.2] e I zero "
        "igual a dez à menos doze, [p=0.2] o nível sonoro é: [p=0.4] {la}A, [p=0.2] menos dez decibéis. [p=0.2] {lb}B, "
        "[p=0.2] onze. [p=0.2] {lc}C, [p=0.2] cento e dez. [p=0.2] {ld}D, [p=0.2] cento e vinte. [p=0.2] {le}E, [p=0.2] "
        "cento e trinta. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="30", block="q5", text=
        "{d}Isole o log e opere na ordem: [p=0.2] I sobre I zero, [p=0.2] dez à menos um dividido por dez à menos doze, "
        "[p=0.2] *dez elevado a onze.* [p=0.3] {a}Log dá onze; [p=0.2] vezes dez, [p=0.2] *cento e dez decibéis.* [p=0.2] "
        "{ok}*Letra C!* [p=0.2] {v}Bem acima dos oitenta e cinco do limite trabalhista. [p=0.4] {xa}A A não dividiu por I "
        "zero. [p=0.2] {xb}A B esqueceu o fator *dez.* [p=0.2] {xd}A D usou só o expoente de I zero, [p=0.2] {xe}e a E "
        "somou sem sinal."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="31", block="checklist", text=
        "{t}O checklist. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* para outra pessoa, [p=0.2] "
        "sem consultar nada. [p=0.4] {b}Lei, domínio, imagem, os gráficos espelhados, [p=0.2] os pontos um zero e bê um, "
        "[p=0.2] sinal e inequações: [p=0.2] episódio um. [p=0.3] {c}Diferença de leituras em razão, [p=0.2] pê agá e "
        "comparação de acidez: [p=0.2] episódio dois."),
    dict(id="32", block="checklist", text=
        "{a}Amplitude contra energia [p=0.2] e a fórmula da magnitude: [p=0.2] episódio três. [p=0.3] {b}Decibéis e a "
        "soma de fontes: [p=0.2] episódio quatro. [p=0.4] {c}O que você *não* marcou, [p=0.2] reveja o episódio "
        "correspondente."),

    # ================= META =================
    dict(id="33", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *trinta questões* [p=0.2] {b}e acerte pelo menos *vinte e uma,* [p=0.2] "
        "setenta por cento. [p=0.4] {c}E pelo menos *dez* de comparação em escala: [p=0.2] pê agá, Richter e decibéis."),

    # ================= PONTE (frase do usuário) E CTA =================
    dict(id="34", block="ponte", text=
        "{a}O próximo assunto é *Função modular e funções definidas por partes:* [p=0.3] {b}conta de água, [p=0.2] "
        "estacionamento [p=0.2] e imposto por faixas, [p=0.3] {c}regras que *mudam de fórmula* conforme o valor de "
        "entrada."),
    dict(id="35", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] {com}E me conte nos "
        "*comentários:* [p=0.2] qual pegadinha te pegou? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo "
        "tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] "
        "para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}A série de função logarítmica está completa. "
        "[p=0.2] Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
