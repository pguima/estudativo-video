# Roteiro — Notação Científica e Ordem de Grandeza, Episódio 6 de 6: Revisão geral, pegadinhas e treino nas áreas do ENEM
# Base: Estudos/Enem/estudos/01-matematica/05-notacao-cientifica-ordem-grandeza.html — seções 01, 11 e 13.
#   NÃO usa as Questões 1–9 da seção 12. As 5 questões são INÉDITAS (marcadas na tela, com "dados aproximados").
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# CORREÇÃO do gancho: o material e o prompt dizem "quatro áreas", mas Matemática, Física, Química, Biologia e Humanas são
#   TRÊS das quatro áreas do ENEM (Linguagens fica fora). A fala diz "Matemática, Ciências da Natureza e até Humanas".
# Analogias âncora retomadas (uma frase cada, com o ícone do episódio, ANTES de cobrar):
#   ep1 PLACA DE CARRO (um só jeito) + expoente = contador de casas da vírgula + zeros à esquerda = CADEIRAS VAZIAS ·
#   ep2 duas PISTAS + GANGORRA · ep3 NOTAS de valores diferentes + quantas LUAS cabem na Terra ·
#   ep4 meio do caminho multiplicando = 3,16 + conta de GUARDANAPO · ep5 GRADE de quadradinhos e cubo de cubinhos.
# V/F (os 9 erros da seção 11; 6 falsas e 3 verdadeiras):
#   1 F (25·10³ é notação científica) · 2 V (40·10⁶ ainda precisa renormalizar) · 3 F (3·10⁵ + 8·10⁴ = 11·10⁹) ·
#   4 F (no produto os expoentes se multiplicam) · 5 F (1 m² = 100 cm²) · 6 V (OG de 7,2·10⁵ é 10⁶) ·
#   7 F (10⁻³ é negativo) · 8 F ("quantas vezes maior" é subtração) · 9 V (√(1,6·10⁻⁵): reescreva como 16·10⁻⁶).
# QUESTÕES INÉDITAS (conferidas em Python: uma única correta; cada errada = um erro clássico). Dados aproximados.
#   Q1 BIOLOGIA (divisão + renormalização) bactéria 2·10⁻⁶ m ÷ vírus 8·10⁻⁸ m = 0,25·10² → 2,5·10¹ → B.
#      A 0,25·10² (valor certo, não renormalizou) · C 4·10⁻² (dividiu o vírus pela bactéria) · D 1,6·10⁻¹³ (multiplicou) ·
#      E 2,5·10⁻¹⁵ (errou o sinal: −6 − 8 = −14).
#   Q2 FÍSICA (multiplicação + "quantas vezes") Terra–Sol = 3·10⁸ m/s · 5·10² s = 15·10¹⁰ = 1,5·10¹¹ m;
#      ÷ Terra–Lua 3,75·10⁸ m = 0,4·10³ = 4·10² → D. Estimativa: 3 ordens, coeficiente de cima menor → menos de mil.
#      A 2,5·10⁻³ (dividiu ao contrário) · B 1·10³ (parou na diferença dos expoentes) · C 4·10⁴ (gangorra para o lado
#      errado) · E 4·10⁸ (multiplicou os expoentes no produto: 15·10¹⁶).
#   Q3 QUÍMICA (soma com expoentes diferentes) 4·10⁻⁵ g + 6·10⁻⁶ g = 4·10⁻⁵ + 0,6·10⁻⁵ = 4,6·10⁻⁵ → C.
#      Estimativa: um pouco mais que o maior. A 1·10⁻¹⁰ (somou coeficientes e expoentes) · B 2,4·10⁻¹⁰ (multiplicou) ·
#      D 1·10⁻⁴ (somou 4 + 6 sem igualar) · E 6,4·10⁻⁴ (gangorra ao contrário: 6·10⁻⁶ = 60·10⁻⁵).
#   Q4 HUMANAS (ordem de grandeza, critério 3,16) verba R$ 3 400 000 000 = 3,4·10⁹; 3,4 ≥ 3,16 → 10¹⁰ → E.
#      A 10⁸ (contou só os 8 zeros) · B 10⁹ (repetiu o expoente escrito / usou 5 como corte) · C 3,4·10⁹ (deu o número,
#      não a ordem) · D 3·10⁹ (só arredondou: não é potência de 10).
#   Q5 MATEMÁTICA (área com prefixos) 3,5 km² = 3,5·(10³)² m² = 3,5·10⁶ m² → A.
#      B 3,5·10³ (não elevou ao quadrado) · C 3,5·10⁹ (elevou ao cubo) · D 3,5·10² (deu em hectares: 350 ha) ·
#      E 3,5·10⁻⁶ (dividiu em vez de multiplicar).
# Checklist (seção 13, 13 itens) → episódio para rever: 1, 2, 11 ep1 · 3, 5 ep2 · 4, 10 ep3 · 6, 12, 13 ep4 · 7, 8, 9 ep5.
# Meta: 30 questões, pelo menos 21 acertos (70%), incluindo Física e Química.
# Ponte: Razão, proporção e regra de três.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de notação científica: 9 pegadinhas e 5 questões em todas as áreas do ENEM · Matemática ENEM, episódio 6"

# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, numa aula de revisão animada, conversando "
            "de perto com um aluno que está treinando para o ENEM: voz calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas de verdadeiro ou falso com suspense, "
            "como num jogo; mostre surpresa nas pegadinhas; comemore os acertos com entusiasmo; dê ênfase forte às "
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
        "{a}Este assunto é *raro:* [p=0.3] ele aparece em quase toda a prova. [p=0.3] {b}Na Matemática, [p=0.2] nas Ciências "
        "da Natureza, [p=0.2] que são Física, Química e Biologia, [p=0.2] e até nas *Humanas.* [p=0.4] {c}Hoje você treina "
        "com uma questão de cada área: [p=0.3] {d}nove pegadinhas [p=0.2] e cinco questões no estilo do ENEM."),

    # ================= ONDE APARECE (seção 01) =================
    dict(id="02", block="onde", text=
        "{t}Onde ele aparece? [p=0.3] {a}Na Matemática: [p=0.2] contas e comparações. [p=0.3] {b}Na Física: "
        "[p=0.2] distâncias no espaço e energia. [p=0.3] {c}Na Química: [p=0.2] quantidades minúsculas. "
        "[p=0.3] {d}Na Biologia: [p=0.2] células e vírus. [p=0.3] {e}E nas Humanas: [p=0.2] população e verbas. [p=0.4] {f}E tem um detalhe de estratégia: [p=0.2] quando "
        "as alternativas estão em *escalas diferentes,* [p=0.2] acertar só a potência de dez [p=0.2] já elimina *quatro.*"),

    # ================= O QUE MAIS RENDE =================
    dict(id="03", block="rendem", text=
        "{t}Pouco tempo? [p=0.2] Garanta três coisas. [p=0.4] {a}Um: [p=0.2] *somar* com expoentes diferentes. "
        "[p=0.3] {b}Dois: [p=0.2] converter *área e volume.* "
        "[p=0.3] {c}Três: [p=0.2] o critério real da *ordem de grandeza,* [p=0.2] que não é o expoente escrito."),

    # ================= ÍNDICE DA REVISÃO: OS 5 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] uma frase por episódio. [p=0.4] {a}Um: [p=0.2] notação científica é como *placa de "
        "carro:* [p=0.2] só existe um jeito certo, [p=0.2] com um único algarismo, diferente de zero, antes da vírgula. "
        "[p=0.2] O expoente conta as casas que a vírgula andou, [p=0.2] e zeros à esquerda são *cadeiras vazias.* [p=0.4] "
        "{b}Dois: [p=0.2] coeficiente numa pista, [p=0.2] expoente na outra. [p=0.2] E a *gangorra:* [p=0.2] se o número da "
        "frente sobe dez vezes, [p=0.2] o expoente desce um, [p=0.2] e o valor não muda."),
    dict(id="05", block="indice", text=
        "{a}Três: [p=0.2] dez elevado a cinco e dez elevado a quatro são *notas de valores diferentes:* [p=0.2] antes de "
        "somar, [p=0.2] troque tudo pela mesma nota. [p=0.2] E *quantas vezes* é quantas Luas cabem na Terra: [p=0.2] "
        "divisão. [p=0.4] {b}Quatro: [p=0.2] o meio do caminho entre um e dez, [p=0.2] multiplicando, [p=0.2] não é cinco: "
        "[p=0.2] é *três vírgula dezesseis.* [p=0.2] E a conta de *guardanapo* acerta a escala. [p=0.4] {c}E cinco: [p=0.2] "
        "área é uma *grade* de quadradinhos, [p=0.2] e volume, [p=0.2] um cubo de cubinhos."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="06", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}São nove frases. "
        "[p=0.2] Quase todas são pegadinhas, [p=0.2] mas não todas. [p=0.4] {b}Em cada uma, [p=0.2] pause e "
        "responda antes de mim."),
    dict(id="07", block="vf", text=
        "{t}Um: [p=0.2] vinte e cinco vezes dez elevado a três [p=0.2] está em notação científica. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque tem número vezes potência de dez. [p=0.3] {g}Mas a placa exige *um* "
        "algarismo antes da vírgula. [p=0.2] Gangorra: [p=0.2] *dois vírgula cinco* vezes dez elevado a quatro."),
    dict(id="08", block="vf", text=
        "{t}Dois: [p=0.2] multiplicou e chegou em quarenta vezes dez elevado a seis? [p=0.2] Ainda falta um passo. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque a conta está certa. "
        "[p=0.3] {g}Mas quarenta não cabe na placa: [p=0.2] *renormalize,* [p=0.2] ou seja, "
        "ajuste com a gangorra. [p=0.2] Quatro vezes dez elevado a sete."),
    dict(id="09", block="vf", text=
        "{t}Três: [p=0.2] três vezes dez elevado a cinco, [p=0.2] *mais* oito vezes dez elevado a quatro, [p=0.2] dá onze "
        "vezes dez elevado a nove. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque parece somar tudo. "
        "[p=0.3] {g}São notas diferentes: [p=0.2] oito vezes dez a quatro [p=0.2] é zero vírgula oito vezes dez a "
        "cinco. [p=0.2] Total: [p=0.2] *três vírgula oito* vezes dez elevado a cinco."),
    dict(id="10", block="vf", text=
        "{t}Quatro: [p=0.2] num produto, [p=0.2] os expoentes se *multiplicam.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* "
        "[p=0.3] {e}Engana porque produto lembra multiplicar. [p=0.3] {g}No produto, [p=0.2] *soma.* "
        "[p=0.2] Na divisão, [p=0.2] subtrai. [p=0.2] Multiplica só na potência de potência."),
    dict(id="11", block="vf", text=
        "{t}Cinco: [p=0.2] um metro quadrado [p=0.2] tem *cem* centímetros quadrados. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque um metro tem cem centímetros. [p=0.3] {g}Mas a grade tem cem quadradinhos em "
        "*cem fileiras:* [p=0.2] *dez mil.* [p=0.2] Área, [p=0.2] ao quadrado; [p=0.2] volume, [p=0.2] ao cubo."),
    dict(id="12", block="vf", text=
        "{t}Seis: [p=0.2] a ordem de grandeza de sete vírgula dois vezes dez elevado a cinco [p=0.2] é dez elevado a "
        "*seis.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque o expoente escrito é cinco. "
        "[p=0.3] {g}Mas sete vírgula dois passou de três vírgula dezesseis: [p=0.2] *sobe uma ordem.*"),
    dict(id="13", block="vf", text=
        "{t}Sete: [p=0.2] dez elevado a menos três [p=0.2] é um número *negativo.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* "
        "[p=0.3] {e}Engana porque o menos está à vista. [p=0.3] {g}É *zero vírgula zero zero um:* "
        "[p=0.2] pequeno e positivo. [p=0.2] O sinal do expoente diz para que lado a vírgula anda."),
    dict(id="14", block="vf", text=
        "{t}Oito: [p=0.2] *quantas vezes maior* [p=0.2] se resolve com subtração. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* "
        "[p=0.3] {e}Engana porque maior lembra diferença. [p=0.3] {g}*Quantas vezes* é quantas Luas cabem na Terra: "
        "[p=0.2] *divisão.* [p=0.2] *Quanto maior* é que é subtração."),
    dict(id="15", block="vf", text=
        "{t}E nove: [p=0.2] para tirar a raiz de um vírgula seis vezes dez elevado a menos cinco, [p=0.2] reescreva como "
        "dezesseis vezes dez elevado a menos seis. [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque "
        "o número mudou. [p=0.3] {g}Mas foi a gangorra: [p=0.2] o valor é o mesmo, [p=0.2] e agora o expoente é "
        "*par.* [p=0.2] A raiz dá quatro vezes dez elevado a menos três."),
    dict(id="16", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas, [p=0.2] uma de cada área."),

    # ================= QUESTÃO 1: BIOLOGIA =================
    dict(id="17", block="q1", text=
        "{t}Questão um, [p=0.2] de *Biologia.* [p=0.3] {a}Uma bactéria mede cerca de *dois vezes dez elevado a menos seis* "
        "metro. [p=0.3] {b}Um vírus mede cerca de *oito vezes dez elevado a menos oito* metro. [p=0.3] {c}Em notação "
        "científica, [p=0.2] quantas vezes a bactéria é maior que o vírus? [p=0.4] {la}A, [p=0.2] zero vírgula vinte e cinco "
        "vezes dez elevado a dois. [p=0.2] {lb}B, [p=0.2] dois vírgula cinco vezes dez elevado a um. [p=0.2] {lc}C, [p=0.2] "
        "quatro vezes dez elevado a menos dois. [p=0.2] {ld}D, [p=0.2] um vírgula seis vezes dez elevado a menos treze. "
        "[p=0.2] {le}E, [p=0.2] dois vírgula cinco vezes dez elevado a menos quinze. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="18", block="q1", text=
        "{t}Quantas vezes: [p=0.2] *divisão.* [p=0.3] {a}Números da frente: [p=0.2] dois "
        "dividido por oito, [p=0.2] zero vírgula vinte e cinco. [p=0.3] {b}Expoentes: [p=0.2] menos seis, [p=0.2] *menos* "
        "menos oito, [p=0.2] dá *mais dois.* [p=0.3] {c}Zero vírgula vinte e cinco não cabe na placa. [p=0.2] Gangorra: "
        "[p=0.2] *dois vírgula cinco vezes dez elevado a um.* [p=0.2] {ok}*Letra B!* [p=0.4] "
        "{xa}A A tem o valor certo, [p=0.2] mas não renormalizou. [p=0.2] {xc}A C dividiu o vírus pela bactéria. [p=0.2] "
        "{xd}A D multiplicou. [p=0.2] {xe}E a E errou o sinal: [p=0.2] fez menos seis menos oito."),

    # ================= QUESTÃO 2: FÍSICA =================
    dict(id="19", block="q2", text=
        "{t}Questão dois, [p=0.2] de *Física.* [p=0.3] {a}A luz percorre *três vezes dez elevado a oito* metros por segundo "
        "[p=0.2] e leva *cinco vezes dez elevado a dois* segundos do Sol até a Terra. [p=0.3] {b}A "
        "distância da Terra à Lua é de cerca de *três vírgula setenta e cinco vezes dez elevado a oito* metros. [p=0.3] "
        "{c}A distância da Terra ao Sol é quantas vezes a distância da Terra à Lua? [p=0.4] {la}A, [p=0.2] dois vírgula "
        "cinco vezes dez elevado a menos três. [p=0.2] {lb}B, [p=0.2] um vezes dez elevado a três. [p=0.2] {lc}C, [p=0.2] "
        "quatro vezes dez elevado a quatro. [p=0.2] {ld}D, [p=0.2] quatro vezes dez elevado a dois. [p=0.2] {le}E, [p=0.2] "
        "quatro vezes dez elevado a oito. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="20", block="q2", text=
        "{t}Primeiro, [p=0.2] a distância: [p=0.2] velocidade vezes tempo. [p=0.3] {a}Três vezes cinco, [p=0.2] quinze; "
        "[p=0.2] oito mais dois, [p=0.2] dez. [p=0.2] Quinze vezes dez elevado a dez; [p=0.2] renormalizando, [p=0.2] *um "
        "vírgula cinco vezes dez elevado a onze* metros. [p=0.3] {b}Agora, [p=0.2] o guardanapo: [p=0.2] onze menos oito, "
        "[p=0.2] três ordens, [p=0.2] perto de *mil.* [p=0.2] Mas um vírgula cinco é menor que três vírgula setenta e cinco, "
        "[p=0.2] então dá *menos* de mil. [p=0.3] {c}A conta confirma: [p=0.2] zero vírgula quatro vezes dez elevado a três, "
        "[p=0.2] *quatrocentas vezes.* [p=0.2] {ok}*Letra D!* [p=0.4] {xb}A B parou na diferença dos expoentes. [p=0.2] "
        "{xa}A A dividiu ao contrário. [p=0.2] {xc}A C girou a gangorra para o lado errado. [p=0.2] {xe}E a E multiplicou "
        "os expoentes na primeira conta."),

    # ================= QUESTÃO 3: QUÍMICA =================
    dict(id="21", block="q3", text=
        "{t}Questão três, [p=0.2] de *Química.* [p=0.3] {a}Numa amostra de água, [p=0.2] um laboratório "
        "encontrou *quatro vezes dez elevado a menos cinco* grama de chumbo [p=0.2] {b}e *seis vezes dez elevado a menos "
        "seis* grama de mercúrio. [p=0.3] {c}A massa total desses dois metais, [p=0.2] em gramas, [p=0.2] é: [p=0.4] {la}A, "
        "[p=0.2] um vezes dez elevado a menos dez. [p=0.2] {lb}B, [p=0.2] dois vírgula quatro vezes dez elevado a menos dez. "
        "[p=0.2] {lc}C, [p=0.2] quatro vírgula seis vezes dez elevado a menos cinco. [p=0.2] {ld}D, [p=0.2] um vezes dez "
        "elevado a menos quatro. [p=0.2] {le}E, [p=0.2] seis vírgula quatro vezes dez elevado a menos quatro. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q3", text=
        "{t}Estimativa primeiro: [p=0.2] o total tem que ser *um pouco mais* que o maior, [p=0.2] quatro vezes dez a menos "
        "cinco. [p=0.3] {a}A e B são minúsculas demais. [p=0.2] D e E chegam a dez vezes dez a menos cinco, [p=0.2] ou mais: "
        "[p=0.2] grandes demais. [p=0.3] {b}Confirmando: [p=0.2] notas diferentes, [p=0.2] iguale pelo maior expoente. "
        "[p=0.2] Seis vezes dez a menos seis [p=0.2] é zero vírgula seis vezes dez a menos cinco. [p=0.3] {c}Quatro mais "
        "zero vírgula seis: [p=0.2] *quatro vírgula seis vezes dez elevado a menos cinco.* [p=0.2] {ok}*Letra C!* [p=0.4] "
        "{xd}A D somou quatro mais seis sem igualar. [p=0.2] {xa}A A somou também os expoentes. [p=0.2] {xb}A B multiplicou. "
        "[p=0.2] {xe}E a E girou a gangorra ao contrário."),

    # ================= QUESTÃO 4: HUMANAS =================
    dict(id="23", block="q4", text=
        "{t}Questão quatro, [p=0.2] de *Humanas.* [p=0.3] {a}Um programa social recebeu uma verba de *três bilhões e "
        "quatrocentos milhões* de reais. [p=0.3] {b}A ordem de "
        "grandeza dessa verba, [p=0.2] em reais, [p=0.2] é: [p=0.4] {la}A, [p=0.2] dez elevado a oito. [p=0.2] {lb}B, "
        "[p=0.2] dez elevado a nove. [p=0.2] {lc}C, [p=0.2] três vírgula quatro vezes dez elevado a nove. [p=0.2] {ld}D, "
        "[p=0.2] três vezes dez elevado a nove. [p=0.2] {le}E, [p=0.2] dez elevado a dez. [p=0.4] {p}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="24", block="q4", text=
        "{t}Primeiro, [p=0.2] a placa: [p=0.2] *três vírgula quatro vezes dez elevado a "
        "nove.* [p=0.3] {a}Agora, [p=0.2] o critério: [p=0.2] três vírgula quatro passou de *três vírgula dezesseis?* "
        "[p=0.2] Passou, [p=0.2] por pouco. [p=0.3] {b}Então sobe uma ordem: [p=0.2] *dez elevado a dez.* [p=0.2] "
        "{ok}*Letra E!* [p=0.4] {xb}A B repetiu o expoente escrito, [p=0.2] ou usou o cinco como corte. [p=0.2] {xa}A A "
        "contou só os zeros. [p=0.2] {xc}A C é o próprio número, [p=0.2] e não a ordem. [p=0.2] {xd}E a D só arredondou: "
        "[p=0.2] também não é potência de dez."),

    # ================= QUESTÃO 5: MATEMÁTICA =================
    dict(id="25", block="q5", text=
        "{t}E a questão cinco, [p=0.2] de *Matemática.* [p=0.3] {a}Um parque tem área de *três vírgula cinco* quilômetros "
        "quadrados. [p=0.3] {b}Essa área, [p=0.2] em metros quadrados, [p=0.2] é: [p=0.4] {la}A, [p=0.2] três vírgula cinco "
        "vezes dez elevado a seis. [p=0.2] {lb}B, [p=0.2] três vírgula cinco vezes dez elevado a três. [p=0.2] {lc}C, "
        "[p=0.2] três vírgula cinco vezes dez elevado a nove. [p=0.2] {ld}D, [p=0.2] três vírgula cinco vezes dez elevado a "
        "dois. [p=0.2] {le}E, [p=0.2] três vírgula cinco vezes dez elevado a menos seis. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q5", text=
        "{t}Um quilômetro tem *mil* metros: [p=0.2] dez elevado a três. [p=0.3] {a}Mas é área: [p=0.2] a grade tem mil "
        "quadradinhos em *mil fileiras.* [p=0.2] O fator vai *ao quadrado:* [p=0.2] dez elevado a seis. [p=0.3] {b}Três "
        "vírgula cinco vezes dez elevado a seis metros quadrados. [p=0.2] {ok}*Letra A!* [p=0.4] {xb}A B esqueceu de elevar "
        "ao quadrado. [p=0.2] {xc}A C elevou ao cubo, [p=0.2] como se fosse volume. [p=0.2] {xd}A D deu a resposta em "
        "*hectares,* [p=0.2] e não em metros quadrados. [p=0.2] {xe}E a E dividiu em vez de "
        "multiplicar."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="27", block="checklist", text=
        "{t}Agora, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* para "
        "outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}A forma exata, [p=0.2] converter [p=0.2] e "
        "os algarismos significativos: [p=0.2] episódio um. [p=0.3] {c}Multiplicar, [p=0.2] dividir, [p=0.2] "
        "renormalizar [p=0.2] e a raiz com expoente par: [p=0.2] episódio dois. [p=0.3] {d}Somar igualando os expoentes "
        "[p=0.2] e *quantas vezes* contra *quanto:* [p=0.2] episódio três."),
    dict(id="28", block="checklist", text=
        "{a}O critério do três vírgula dezesseis, [p=0.2] a estimativa [p=0.2] e as escalas que vale ter "
        "na cabeça: [p=0.2] episódio quatro. [p=0.3] {b}Os prefixos, [p=0.2] área e volume, [p=0.2] litro e hectare: "
        "[p=0.2] episódio cinco. [p=0.4] {c}O que você *não* marcou, [p=0.2] reveja o episódio correspondente."),

    # ================= META =================
    dict(id="29", block="meta", text=
        "{t}E antes de considerar este assunto dominado, [p=0.2] uma meta: [p=0.3] {a}resolva *trinta* questões [p=0.2] "
        "{b}e acerte pelo menos *vinte e uma,* [p=0.2] setenta por cento. [p=0.4] {c}Inclua questões de *Física* e de *Química:* "
        "[p=0.2] é onde este conteúdo mais aparece."),

    # ================= PONTE E CTA =================
    dict(id="30", block="ponte", text=
        "{a}O próximo assunto é *razão, proporção e regra de três.* [p=0.4] {b}A ferramenta mais usada de *toda* a "
        "Matemática do ENEM."),
    dict(id="31", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual das cinco áreas foi a mais difícil para você? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de notação científica está completa. [p=0.2] Bons estudos, e *até a próxima aula* aqui no "
        "Estudativo. [p=1.5]"),
]
