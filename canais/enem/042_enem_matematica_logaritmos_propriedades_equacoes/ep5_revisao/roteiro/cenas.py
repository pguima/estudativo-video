# Roteiro — Logaritmos: definição, propriedades e equações, Episódio 5 de 5: Revisão geral, estratégia de prova,
#   pegadinhas e treino (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/27-logaritmos-propriedades-equacoes.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (Q1–Q9). As 5 questões são INÉDITAS (números e alternativas do prompt do usuário).
#   pH, Richter e decibéis: só a ponte (próxima série), sem questão de escala.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (números falados por extenso; o gancho só acrescenta, depois delas, o que a
#   aula vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 o log é uma PERGUNTA e um EXPOENTE COM NOME PRÓPRIO · o log decimal CONTA ZEROS (ícone: balão de pergunta) ·
#   ep2 as regras de potência LIDAS DE TRÁS PARA FRENTE · o KIT 2, 3 e 10 · soma dentro do log é PORTA TRANCADA
#       (ícone: régua de cálculo) ·
#   ep3 o ELEVADOR que desce o expoente · a BASE NO PORÃO · ESTIME entre dois inteiros (ícone: elevador) ·
#   ep4 o SEGURANÇA NA PORTA do log (ícone: segurança na porta).
# O que a prova cobra (seção 01): descobrir um tempo · calcular com valores dados (log 72, log 1,5) · equações
#   logarítmicas com as condições de existência · escalas (só citar). O que mais rende: ler log_b a como "b elevado a
#   quanto dá a?" (log₂ 32 = 5, log 0,001 = −3, log₉ 3 = 1/2).
# Onde aparece (seção 10): Química (pH, cada unidade = fator 10) · Física (+10 dB = intensidade ×10) · Geografia (um grau
#   de magnitude = amplitude ×10) · Financeira (t = log(M/C) ÷ log(1 + i)) · Química e Biologia (tempo = log da razão ÷
#   log do fator).
# Estratégia (seção 09): decomponha em 2, 3 e 10 (72 = 2³ · 3², 50 = 100/2, 0,9 = 9/10) · estime (3ᵗ = 50 entre 3 e 4) ·
#   desconfie da alternativa com duas raízes.
# V/F (os 9 erros da seção 11, NA ORDEM do prompt). DESVIO NOSSO (marcado): para o jogo não ter resposta previsível, três
#   frases aparecem na versão CERTA (verdadeiras: 3, 5 e 8); as outras seis são o erro do prompt (falsas):
#   1 F log(M + N) = log M + log N · 2 F log M ÷ log N = log M − log N · 3 V log 72 = log 8 + log 9 ·
#   4 F log₂ 10 = log 2 ÷ log 10 (≈ 3,32, não 0,301) · 5 V log 0,9 é negativo (≈ −0,046) · 6 F log 0 = 0 ·
#   7 F aceitar x = −5 em log x + log(x + 3) = 1 · 8 V log(1 000 · 3ᵗ) = 3 + t · log 3 · 9 F 2¹⁰⁰ tem 30 algarismos (31).
# QUESTÕES INÉDITAS (do prompt; conferidas em trabalho/conferir_questoes.py: uma única correta; cada errada = um erro
#   clássico; a ordem das letras é nossa):
#   Q1 log 0,6 com log 2 = 0,30 e log 3 = 0,48: 0,6 = 6/10 → 0,78 − 1 = −0,22 → D. A 0,78 (é log 6, esqueceu o ÷ 10) ·
#      B 0,22 (erro de sinal) · C 0,144 (log 2 · log 3) · E −0,78 (sinal trocado e esqueceu o ÷ 10).
#   Q2 cultura cresce 25% por hora, dobra em: log 1,25 = log(10/8) = 1 − 3 · 0,30 = 0,10 → t = 0,30 ÷ 0,10 = 3 h → C
#      (confere: 1,25³ ≈ 1,95). A 0,2 h (subtraiu os logs) · B ≈ 0,33 h (inverteu a divisão) · D 4 h (linear:
#      100% ÷ 25%) · E 8 h (2 ÷ 0,25).
#   Q3 lago perde 20% ao mês, metade em: log 0,8 = 0,90 − 1 = −0,10 · log 0,5 = −0,30 → 3 meses → D (confere:
#      0,8³ = 0,512; os dois logs negativos, tempo positivo). A ≈ 0,33 mês (inverteu) · B ≈ 0,43 mês (fator 0,2:
#      log 0,2 = −0,70) · C 2,5 meses (linear 50% ÷ 20%) · E 5 meses (perder tudo, linear).
#   Q4 log₃ x + log₃ (x − 8) = 2: condições x > 8 · x² − 8x − 9 = 0 → 9 ou −1 → {9} → A (confere: log₃ 9 + log₃ 1 =
#      2 + 0). B {−1} (raiz proibida) · C {−1, 9} (não verificou) · D {8,5} (somou os logaritmandos: 2x − 8 = 9) ·
#      E ∅ (descartou também a raiz válida).
#   Q5 algarismos de 3⁵⁰ com log 3 = 0,477: 50 · 0,477 = 23,85 → 24 → B. A 23 (esqueceu o + 1) · C 50 (o expoente) ·
#      D 51 (somou 1 ao expoente) · E 150 (base vezes expoente).
# Gabaritos: D, C, D, A, B.
# Checklist (seção 13) → episódio (como o prompt pede): definição, condições, logs de cabeça, consequências e algarismos
#   → ep1 · propriedades, propriedades falsas e kit → ep2 · mudança de base, equações exponenciais com log e tempo de
#   dobrar ou cair à metade → ep3 · equações logarítmicas e verificação das raízes → ep4.
# Meta (prompt e material): 30 questões, 21 acertos (70%), com pelo menos dez que dão log 2 e log 3 no enunciado.
# Ponte (do usuário): Função logarítmica e aplicações (pH, Richter, decibéis).
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de logaritmos: 9 pegadinhas e 5 questões estilo ENEM · Matemática ENEM, Logaritmos episódio 5"

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
        "{a}No ENEM, [p=0.2] o logaritmo quase nunca é o tema da questão: [p=0.3] ele é a *ferramenta.* [p=0.4] {b}O "
        "enunciado diz \"use log de dois igual a zero vírgula trinta\" [p=0.3] {c}e espera que você descubra *um tempo,* "
        "[p=0.2] *uma contagem* [p=0.2] ou *um expoente.* [p=0.4] {d}Hoje você *treina a ferramenta.* [p=0.4] {e}Nove "
        "frases de verdadeiro ou falso [p=0.2] e cinco questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E o que a prova pede? [p=0.4] {a}*Descobrir um tempo:* [p=0.2] em quantos anos um dinheiro dobra, [p=0.2] em "
        "quantas horas uma cultura cresce. [p=0.3] {b}*Calcular com valores dados:* [p=0.2] log de setenta e dois [p=0.2] "
        "a partir de log de dois e log de três. [p=0.3] {c}*Equações logarítmicas,* [p=0.2] respeitando as condições. "
        "[p=0.3] {d}E as *escalas,* [p=0.2] que são a próxima série."),
    dict(id="03", block="rende", text=
        "{t}E o que mais rende? [p=0.3] *Ler o logaritmo como uma pergunta:* [p=0.2] \"bê elevado a quanto dá a?\" [p=0.4] "
        "{a}Log de trinta e dois na base dois: [p=0.2] dois elevado a quanto dá trinta e dois? [p=0.2] *Cinco.* [p=0.3] "
        "{b}Log de zero vírgula zero zero um: [p=0.2] *menos três.* [p=0.3] {c}Log de três na base nove: [p=0.2] nove "
        "elevado a quanto dá três? [p=0.2] *Um meio,* [p=0.2] a raiz quadrada."),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] relembre cada episódio. [p=0.4] {a}Um: [p=0.2] o logaritmo é uma *pergunta,* "
        "[p=0.2] e a resposta é um *expoente com nome próprio.* [p=0.2] E o log decimal *conta zeros.* [p=0.4] {b}Dois: "
        "[p=0.2] as propriedades são as regras de potência *lidas de trás para frente.* [p=0.2] O *kit dois, três e dez* "
        "monta quase tudo, [p=0.2] e soma dentro do log é *porta trancada.*"),
    dict(id="05", block="indice", text=
        "{a}Três: [p=0.2] o *elevador.* [p=0.2] Aplique log dos dois lados, [p=0.2] e o expoente desce. [p=0.2] Na "
        "mudança de base, [p=0.2] a base vai para o *porão.* [p=0.2] E *estime* entre dois inteiros. [p=0.4] {b}Quatro: "
        "[p=0.2] o *segurança na porta do log:* [p=0.2] só entra número positivo, [p=0.2] e toda raiz mostra documento."),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="06", block="onde", text=
        "{t}E as outras provas? [p=0.4] {a}Na *Química,* [p=0.2] o pH: [p=0.2] cada unidade é um fator *dez* na "
        "concentração. [p=0.3] {b}Na *Física,* [p=0.2] os decibéis: [p=0.2] mais dez decibéis, [p=0.2] intensidade *dez "
        "vezes* maior. [p=0.3] {c}Na *Geografia,* [p=0.2] os terremotos: [p=0.2] um grau a mais, [p=0.2] amplitude *dez "
        "vezes* maior."),
    dict(id="07", block="onde", text=
        "{d}Nos *juros compostos,* [p=0.2] o tempo é log de M sobre C, [p=0.2] dividido por log de um mais i. [p=0.3] "
        "{e}E na *Química e na Biologia,* [p=0.2] meia-vida e culturas: [p=0.2] o tempo é *log da razão, dividido por log "
        "do fator.* [p=0.4] {f}As escalas são o próximo assunto."),

    # ================= ESTRATÉGIA: 3 HÁBITOS (seção 09) =================
    dict(id="08", block="habitos", text=
        "{t}E na hora da prova? [p=0.2] Três hábitos. [p=0.4] {a}Um: [p=0.2] *decomponha antes de calcular.* [p=0.2] Deu "
        "log de dois e log de três? [p=0.2] Escreva tudo com dois, três e dez. [p=0.2] Setenta e dois é dois ao cubo "
        "vezes três ao quadrado; [p=0.2] cinquenta é cem sobre dois. [p=0.4] {b}Dois: [p=0.2] *estime antes de marcar.* "
        "[p=0.2] Três elevado a tê igual a cinquenta? [p=0.2] Fica entre *três e quatro.*"),
    dict(id="09", block="habitos", text=
        "{c}Três: [p=0.2] *desconfie da alternativa com duas raízes.* [p=0.3] Equação logarítmica que vira segundo grau "
        "[p=0.2] pede o teste de cada raiz [p=0.2] nos logaritmandos originais."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="10", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="11", block="vf", text=
        "{t}Um: [p=0.2] log de *M mais N* [p=0.2] é log de M mais log de N. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* "
        "[p=0.3] {e}Engana porque parece a regra do produto. [p=0.3] {g}Mas soma dentro do log é *porta trancada:* "
        "[p=0.2] a regra é só para *M vezes N.*"),
    dict(id="12", block="vf", text=
        "{t}Dois: [p=0.2] log de M *dividido* por log de N [p=0.2] é log de M menos log de N. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque a palavra \"divisão\" aparece nas duas. [p=0.3] {g}Mas a diferença é o log "
        "do *quociente,* [p=0.2] log de M sobre N. [p=0.2] Não é quociente de logs."),
    dict(id="13", block="vf", text=
        "{t}Três: [p=0.2] log de setenta e dois [p=0.2] é log de oito *mais* log de nove. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Verdadeiro!* [p=0.3] {e}Parece falso porque muita gente escreve log de oito *vezes* log de nove. [p=0.3] "
        "{g}Mas é a potência lida de trás para frente: [p=0.2] *produto vira soma.*"),
    dict(id="14", block="vf", text=
        "{t}Quatro: [p=0.2] log de dez na base dois [p=0.2] é log de dois *dividido* por log de dez. [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o dois aparece primeiro. [p=0.3] {g}Mas a base vai para o *porão:* "
        "[p=0.2] log de dez sobre log de dois, [p=0.2] *três vírgula trinta e dois.*"),
    dict(id="15", block="vf", text=
        "{t}Cinco: [p=0.2] log de *zero vírgula nove* [p=0.2] é negativo. [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* "
        "[p=0.3] {e}Parece falso porque log de nove é positivo, [p=0.2] zero vírgula nove cinco quatro. [p=0.3] {g}Mas "
        "zero vírgula nove é nove sobre *dez:* [p=0.2] menos um. [p=0.2] Fica *menos zero vírgula zero quatro seis.*"),
    dict(id="16", block="vf", text=
        "{t}Seis: [p=0.2] log de *zero* [p=0.2] é zero. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque "
        "zero parece dar zero em tudo. [p=0.3] {g}Mas dez elevado a quanto dá zero? [p=0.2] Nenhum expoente. [p=0.2] Log de "
        "zero *não existe;* [p=0.2] quem vale zero é *log de um.*"),
    dict(id="17", block="vf", text=
        "{t}Sete: [p=0.2] em log de xis mais log de xis mais três, igual a um, [p=0.2] as raízes são *dois e menos cinco,* "
        "[p=0.2] e as duas valem. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque as duas saem da conta. "
        "[p=0.3] {g}Mas o *segurança na porta* barra o menos cinco: [p=0.2] log de número negativo não existe. [p=0.2] Só "
        "o *dois.*"),
    dict(id="18", block="vf", text=
        "{t}Oito: [p=0.2] log de *mil vezes três elevado a tê* [p=0.2] é *três, mais tê vezes log de três.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque muita gente escreve *três tê* vezes log de "
        "três. [p=0.3] {g}Mas o mil vira *parcela:* [p=0.2] log de mil é três, [p=0.2] e só o tê desce no elevador."),
    dict(id="19", block="vf", text=
        "{t}E nove: [p=0.2] dois elevado a cem [p=0.2] tem *trinta* algarismos. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* "
        "[p=0.3] {e}Engana porque o log dá trinta vírgula um. [p=0.3] {g}Mas algarismos são a *parte inteira mais um:* "
        "[p=0.2] *trinta e um.*"),
    dict(id="20", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas. [p=0.2] Em todas: [p=0.2] *decomponha,* [p=0.2] *estime* [p=0.2] e só depois resolva."),

    # ================= QUESTÃO 1: LOG POR DECOMPOSIÇÃO =================
    dict(id="21", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Considere log de dois igual a *zero vírgula trinta* [p=0.2] e log de três igual a "
        "*zero vírgula quarenta e oito.* [p=0.3] {b}O valor de *log de zero vírgula seis* é: [p=0.4] {la}A, [p=0.2] zero "
        "vírgula setenta e oito. [p=0.2] {lb}B, [p=0.2] zero vírgula vinte e dois. [p=0.2] {lc}C, [p=0.2] zero vírgula "
        "cento e quarenta e quatro. [p=0.2] {ld}D, [p=0.2] menos zero vírgula vinte e dois. [p=0.2] {le}E, [p=0.2] menos "
        "zero vírgula setenta e oito. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q1", text=
        "{d}Estime primeiro: [p=0.2] zero vírgula seis está entre zero e um, [p=0.2] então o log é *negativo.* [p=0.3] "
        "{a}Decomponha: [p=0.2] zero vírgula seis é *seis sobre dez,* [p=0.2] e seis é dois vezes três. [p=0.3] {b}Zero "
        "vírgula trinta mais zero vírgula quarenta e oito, [p=0.2] menos um: [p=0.2] *menos zero vírgula vinte e dois.* "
        "[p=0.2] {ok}*Letra D!* [p=0.4] {xa}A A é log de *seis,* [p=0.2] esqueceu o dividido por dez. [p=0.2] {xb}A B "
        "errou o sinal. [p=0.2] {xc}A C *multiplicou* os logs, [p=0.2] {xe}e a E trocou o sinal e esqueceu o dez."),

    # ================= QUESTÃO 2: TEMPO DE CRESCIMENTO =================
    dict(id="23", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Uma cultura de bactérias cresce *vinte e cinco por cento por hora.* [p=0.2] Use log "
        "de dois igual a zero vírgula trinta. [p=0.3] {b}A cultura *dobra* em: [p=0.4] {la}A, [p=0.2] zero vírgula duas "
        "hora. [p=0.2] {lb}B, [p=0.2] cerca de zero vírgula trinta e três hora. [p=0.2] {lc}C, [p=0.2] três horas. "
        "[p=0.2] {ld}D, [p=0.2] quatro horas. [p=0.2] {le}E, [p=0.2] oito horas. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="24", block="q2", text=
        "{d}O fator é *um vírgula vinte e cinco:* [p=0.2] um vírgula vinte e cinco elevado a tê, [p=0.2] igual a dois. "
        "[p=0.3] {a}O log do fator sai do kit: [p=0.2] um vírgula vinte e cinco é *dez sobre oito.* [p=0.2] Um, menos três "
        "vezes zero vírgula trinta: [p=0.2] *zero vírgula dez.* [p=0.3] {b}Pelo elevador: [p=0.2] zero vírgula trinta "
        "dividido por zero vírgula dez, [p=0.2] *três horas.* [p=0.2] {ok}*Letra C!* [p=0.2] {v}Confira: [p=0.2] um "
        "vírgula vinte e cinco ao cubo dá quase dois. [p=0.4] {xa}A A *subtraiu* os logs, [p=0.2] {xb}a B *inverteu* a "
        "divisão, [p=0.2] {xd}a D pensou em crescimento *linear,* [p=0.2] {xe}e a E dividiu dois pela taxa."),

    # ================= QUESTÃO 3: TEMPO DE DECAIMENTO =================
    dict(id="25", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Um lago perde *vinte por cento* de um poluente por mês, [p=0.2] sempre sobre o que "
        "restou. [p=0.2] Use log de dois igual a zero vírgula trinta. [p=0.3] {b}Resta a *metade* do poluente em: "
        "[p=0.4] {la}A, [p=0.2] cerca de zero vírgula trinta e três mês. [p=0.2] {lb}B, [p=0.2] cerca de zero vírgula "
        "quarenta e três mês. [p=0.2] {lc}C, [p=0.2] dois meses e meio. [p=0.2] {ld}D, [p=0.2] três meses. [p=0.2] {le}E, "
        "[p=0.2] cinco meses. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q3", text=
        "{d}Perdeu vinte, [p=0.2] o fator é *zero vírgula oito.* [p=0.2] Zero vírgula oito elevado a tê, [p=0.2] igual a "
        "zero vírgula cinco. [p=0.3] {a}Log de zero vírgula oito é oito sobre dez: [p=0.2] zero vírgula noventa menos um, "
        "[p=0.2] *menos zero vírgula dez.* [p=0.2] Log de zero vírgula cinco: [p=0.2] *menos zero vírgula trinta.* [p=0.3] "
        "{b}Menos com menos dá mais: [p=0.2] *três meses.* [p=0.2] {ok}*Letra D!* [p=0.2] {v}Confira: [p=0.2] zero "
        "vírgula oito ao cubo é zero vírgula quinhentos e doze. [p=0.4] {xa}A A inverteu a divisão. [p=0.2] {xb}A B usou "
        "*zero vírgula dois* como fator. [p=0.2] {xc}{xe}A C e a E pensaram em perda linear."),

    # ================= QUESTÃO 4: EQUAÇÃO LOGARÍTMICA =================
    dict(id="27", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}O conjunto solução de *log de xis na base três, mais log de xis menos oito na base "
        "três, igual a dois* [p=0.2] é: [p=0.4] {la}A, [p=0.2] o conjunto com o nove. [p=0.2] {lb}B, [p=0.2] o conjunto "
        "com o menos um. [p=0.2] {lc}C, [p=0.2] o conjunto com menos um e nove. [p=0.2] {ld}D, [p=0.2] o conjunto com oito "
        "e meio. [p=0.2] {le}E, [p=0.2] o conjunto vazio. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="28", block="q4", text=
        "{d}Primeiro o segurança: [p=0.2] xis maior que zero [p=0.2] e xis maior que oito. [p=0.2] Fica *xis maior que "
        "oito.* [p=0.3] {a}Junte os logs: [p=0.2] xis vezes xis menos oito, [p=0.2] igual a três ao quadrado, *nove.* "
        "[p=0.2] Xis ao quadrado menos oito xis menos nove, igual a zero: [p=0.2] *nove* ou *menos um.* [p=0.3] {b}O "
        "menos um não passa na porta. [p=0.2] Só o *nove.* [p=0.2] {ok}*Letra A!* [p=0.4] {xb}A B ficou com a raiz "
        "proibida, [p=0.2] {xc}a C não verificou, [p=0.2] {xd}a D *somou* os logaritmandos, [p=0.2] {xe}e a E jogou fora "
        "também a raiz boa."),

    # ================= QUESTÃO 5: CONTAR ALGARISMOS =================
    dict(id="29", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Use log de três igual a *zero vírgula quatro sete sete.* [p=0.3] {b}O número "
        "*três elevado a cinquenta* tem quantos algarismos? [p=0.4] {la}A, [p=0.2] vinte e três. [p=0.2] {lb}B, [p=0.2] "
        "vinte e quatro. [p=0.2] {lc}C, [p=0.2] cinquenta. [p=0.2] {ld}D, [p=0.2] cinquenta e um. [p=0.2] {le}E, [p=0.2] "
        "cento e cinquenta. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="30", block="q5", text=
        "{d}O expoente desce: [p=0.2] cinquenta vezes zero vírgula quatro sete sete, [p=0.2] *vinte e três vírgula oitenta "
        "e cinco.* [p=0.3] {a}Parte inteira, *vinte e três;* [p=0.2] mais um: [p=0.2] *vinte e quatro algarismos.* "
        "[p=0.2] {ok}*Letra B!* [p=0.4] {xa}A A esqueceu o *mais um.* [p=0.2] {xc}A C confundiu com o expoente, "
        "[p=0.2] {xd}a D somou um ao expoente, [p=0.2] {xe}e a E multiplicou a base pelo expoente."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="31", block="checklist", text=
        "{t}O checklist. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* para outra pessoa, [p=0.2] "
        "sem consultar nada. [p=0.4] {b}Definição, condições, logs de cabeça e algarismos: [p=0.2] episódio um. [p=0.3] "
        "{c}Propriedades, as propriedades falsas e o kit: [p=0.2] episódio dois."),
    dict(id="32", block="checklist", text=
        "{a}Mudança de base, equações exponenciais com log [p=0.2] e o tempo de dobrar ou cair à metade: [p=0.2] episódio "
        "três. [p=0.3] {b}Equações logarítmicas e a verificação das raízes: [p=0.2] episódio quatro. [p=0.4] {c}O que você "
        "*não* marcou, [p=0.2] reveja o episódio correspondente."),

    # ================= META =================
    dict(id="33", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *trinta questões* [p=0.2] {b}e acerte pelo menos *vinte e uma,* [p=0.2] "
        "setenta por cento. [p=0.4] {c}E pelo menos *dez* que dão *log de dois e log de três* no enunciado."),

    # ================= PONTE (frase do usuário) E CTA =================
    dict(id="34", block="ponte", text=
        "{a}O próximo assunto é *Função logarítmica e aplicações:* [p=0.2] pH, Richter, decibéis, [p=0.3] {b}onde estas "
        "contas viram as *escalas do mundo real:* [p=0.3] {c}quantas vezes mais ácido, [p=0.2] quantas vezes mais "
        "energia, [p=0.2] quantas vezes mais barulho."),
    dict(id="35", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] {com}E me conte nos "
        "*comentários:* [p=0.2] qual pegadinha te pegou? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo "
        "tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] "
        "para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}A série de logaritmos está completa. "
        "[p=0.2] Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
