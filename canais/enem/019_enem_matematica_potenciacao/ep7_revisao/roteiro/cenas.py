# Roteiro — Potenciação e Radiciação, Episódio 7 de 7: Revisão geral, pegadinhas e treino para o ENEM (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/04-potenciacao-radiciacao.html — seções 01, 11 e 13.
#   NÃO usa as Questões 1–9 da seção 12. As 5 questões são INÉDITAS (marcadas na tela).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora retomadas (uma frase cada, com o ícone do episódio, ANTES de cobrar):
#   ep1 PAPEL DOBRADO (3 dobras = 8 camadas) + ESCADA QUE DESCE DIVIDINDO (a⁰ = 1, negativo inverte) ·
#   ep2 FILAS DE FATORES (junta = soma, cancela = subtrai, copia = multiplica) + MESMA FRUTA + TESTE COM 2 E 3 ·
#   ep3 CONTADOR DE ZEROS · ep4 SETAS DE IDA E VOLTA (raiz desfaz a potência; índice par devolve o positivo) ·
#   ep5 PORTA DA RAIZ (saem em dupla) + MAÇÃS COM MAÇÃS · ep6 UM DISFARÇADO + TRADUTOR (embaixo = índice, em cima = expoente).
# Jogo das 7 cartas (seção 03): produto soma · quociente subtrai · potência de potência multiplica · (a·b)ⁿ = aⁿ·bⁿ ·
#   (a/b)ⁿ = aⁿ/bⁿ · a⁰ = 1 · a⁻ⁿ = 1/aⁿ.
# V/F (os 10 erros da seção 11; 7 falsas e 3 verdadeiras): 1 F (2³ = 6) · 2 F (a⁰ = 0) · 3 V (2⁻³ é positivo) ·
#   4 F (−3² = 9) · 5 F (2² + 2³ = 2⁵) · 6 V ((2³)² = 2⁶) · 7 F (√(9+16) = √9 + √16) · 8 F (√(x²) = x) ·
#   9 V (∛−8 = −2 existe; √−4 não) · 10 F (2√3 + 3√2 = 5√5).
# QUESTÕES INÉDITAS (todas conferidas em Python: uma única correta; cada errada = um erro clássico):
#   Q1 (mesma base) (27² · 9) / 3⁶ = 3⁶ · 3² / 3⁶ = 3² = 9 → C.
#      A 3 (somou na potência de potência: 27² = 3⁵) · B 6 (fez 3² = 3 · 2) · D 243 (leu (3³)² como a torre 3^(3²) = 3⁹) ·
#      E 729 (multiplicou os expoentes no produto: 3⁶ · 3² = 3¹²).
#   Q2 (base 10, "por unidade") 3,6·10⁷ parafusos em caixas de 1,2·10³ → 3·10⁴ → B.
#      A 3·10⁻⁴ (subtraiu ao contrário: 3 − 7) · C 3·10¹⁰ (somou os expoentes) · D 4,32·10¹⁰ (multiplicou em vez de dividir) ·
#      E 2,4·10⁴ (subtraiu os números da frente: 3,6 − 1,2).
#   Q3 (expoente negativo com fração) (2/5)⁻² + 2⁻² = 25/4 + 1/4 = 26/4 = 13/2 → C.
#      A −13/2 (deixou negativo) · B 9/4 (fez 2⁻² = −4: 25/4 − 4) · D 41/100 (não inverteu a 1ª: 4/25 + 1/4) ·
#      E 104/25 (não inverteu nada: 4/25 + 4).
#   Q4 (simplificar e somar radicais) √75 + √12 = 5√3 + 2√3 = 7√3 → B.
#      A √87 (somou os radicandos) · C 7√6 (somou coeficientes E radicandos, o "5√5") · D 29√3 (tirou 25 e 4 sem tirar a
#      raiz) · E 30 (multiplicou: √75 · √12 = √900).
#   Q5 (racionalização) 10/√5 = 10√5/5 = 2√5 → A.
#      B 10√5 (esqueceu de dividir por 5) · C 2 (multiplicou só o denominador, mudou o valor) · D √2 (pôs tudo dentro da
#      raiz: √(10/5)) · E 2√5/5 (fez √5 · √5 = 25).
# Checklist (seção 13, 13 itens) → episódio para rever: 1–3 ep1 · 4–6 ep2 · 7 ep3 · 8–9 ep4 · 10–11 ep5 · 12–13 ep6.
# Meta: 30 questões, pelo menos 21 acertos (70%), priorizando simplificação de radicais e expressões com mesma base.
# Ponte: Notação científica e ordem de grandeza (depende das potências de 10).
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de potenciação e radiciação: 10 pegadinhas e 5 questões estilo ENEM · Matemática ENEM, episódio 7"

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
    "pH": "pê agá",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Potência e raiz quase nunca são o *tema* da questão. [p=0.4] {b}São a *língua* em que a questão está escrita. "
        "[p=0.5] {c}Hoje você confere se já é *fluente:* [p=0.3] {d}dez pegadinhas [p=0.2] e cinco questões no estilo do ENEM."),

    # ================= ONDE APARECEM (seção 01) =================
    dict(id="02", block="onde", text=
        "{t}Onde essa língua aparece na prova? [p=0.3] Da mais frequente para a menos. [p=0.4] {a}Primeiro, a *notação "
        "científica:* [p=0.2] população, distâncias, massas. [p=0.3] {b}Depois, a geometria: [p=0.2] Pitágoras, áreas e "
        "volumes, [p=0.2] cheios de raiz quadrada. [p=0.3] {c}Os juros compostos, [p=0.2] que são uma potência. [p=0.3] "
        "{d}Logaritmo, pH e escala Richter: [p=0.2] o logaritmo é a pergunta ao contrário da potência, [p=0.2] qual expoente "
        "dá esse número. [p=0.3] {e}E a Física e a Química, [p=0.2] com meia-vida e ordens de grandeza."),

    # ================= ÍNDICE DA REVISÃO: OS 6 ÍCONES =================
    dict(id="03", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] uma frase por episódio. [p=0.4] {a}Um: [p=0.2] potência é dobrar papel: [p=0.2] três "
        "dobras, [p=0.2] *oito* camadas. [p=0.2] E a escada que desce dividindo mostrou que expoente zero dá um, [p=0.2] e que "
        "o negativo *inverte.* [p=0.4] {b}Dois: [p=0.2] potência é uma fila de fatores. [p=0.2] Multiplicar junta as filas, "
        "[p=0.2] dividir cancela, [p=0.2] e só se junta fila da *mesma fruta.* [p=0.4] {c}Três: [p=0.2] o expoente do dez é "
        "um *contador de zeros.*"),
    dict(id="04", block="indice", text=
        "{a}Quatro: [p=0.2] a raiz é o *caminho de volta* da potência, [p=0.2] e a raiz de índice par devolve sempre o "
        "positivo. [p=0.4] {b}Cinco: [p=0.2] a raiz é uma porta em que os fatores só saem *em dupla,* [p=0.2] e só se somam "
        "maçãs com maçãs. [p=0.4] {c}E seis: [p=0.2] racionalizar é multiplicar por *um disfarçado,* [p=0.2] e o expoente "
        "fracionário é um tradutor: [p=0.2] embaixo vira índice, [p=0.2] em cima vira expoente."),

    # ================= O QUE MAIS RENDE + JOGO DAS 7 CARTAS =================
    dict(id="05", block="rendem", text=
        "{t}E se você só tiver tempo para duas coisas? [p=0.4] {a}As *sete propriedades,* [p=0.2] a ponto de aplicar sem "
        "pensar, [p=0.3] {b}e a *simplificação de radicais.* [p=0.4] {c}O resto é apoio."),
    dict(id="06", block="jogo", text=
        "{t}Então, [p=0.2] jogo das sete cartas. [p=0.3] {a}Cada carta tem o começo de uma propriedade: [p=0.2] complete a "
        "regra. [p=0.4] {b}Mesma base multiplicando. [p=0.2] {c}Mesma base dividindo. [p=0.2] {d}Potência de potência. "
        "[p=0.2] {e}Produto elevado. [p=0.2] {f}Fração elevada. [p=0.2] {g}Expoente zero. [p=0.2] {h}E expoente negativo. "
        "[p=0.4] {p}*Pause e complete.* [p=2.0]"),
    dict(id="07", block="jogo", text=
        "{t}Virando as cartas! [p=0.3] {a}Multiplicou, [p=0.2] *soma* os expoentes. [p=0.3] {b}Dividiu, [p=0.2] *subtrai.* "
        "[p=0.3] {c}Potência de potência, [p=0.2] *multiplica.* [p=0.3] {d}No produto, [p=0.2] o expoente vai para cada fator. "
        "[p=0.3] {e}Na fração, [p=0.2] para cima e para baixo. [p=0.3] {f}Expoente zero, [p=0.2] *um.* [p=0.3] {g}E expoente "
        "negativo, [p=0.2] *inverte.* [p=0.4] {h}Atalho: [p=0.2] as duas primeiras só valem com a *mesma base.*"),

    # ================= VERDADEIRO OU FALSO: OS 10 ERROS =================
    dict(id="08", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}São dez frases. [p=0.2] Quase todas são pegadinhas, [p=0.2] mas "
        "não todas. [p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="09", block="vf", text=
        "{t}Um: [p=0.2] dois elevado a três é *seis.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o dois e "
        "o três estão ali. [p=0.3] {g}Mas três dobras de papel dão dois vezes dois vezes dois: [p=0.2] *oito.*"),
    dict(id="10", block="vf", text=
        "{t}Dois: [p=0.2] qualquer número elevado a zero dá *zero.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana "
        "porque o zero costuma zerar tudo. [p=0.3] {g}Desça a escada: [p=0.2] dois, [p=0.2] dividido por dois, [p=0.2] *um.* "
        "[p=0.2] Vale para toda base, [p=0.2] menos o zero."),
    dict(id="11", block="vf", text=
        "{t}Três: [p=0.2] dois elevado a menos três é um número *positivo.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* "
        "[p=0.3] {e}Parece falso porque o sinal de menos está ali, [p=0.2] bem à vista. [p=0.3] {g}Mas o menos do expoente "
        "só manda inverter: [p=0.2] *um oitavo.*"),
    dict(id="12", block="vf", text=
        "{t}Quatro: [p=0.2] menos três ao quadrado, [p=0.2] sem parêntese, [p=0.2] dá *nove.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque menos com menos dá mais. [p=0.3] {g}Mas sem parêntese, [p=0.2] o expoente não "
        "pega o sinal: [p=0.2] *menos nove.* [p=0.2] Só com parêntese dá nove."),
    dict(id="13", block="vf", text=
        "{t}Cinco: [p=0.2] dois ao quadrado *mais* dois ao cubo [p=0.2] é dois elevado a cinco. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque parece a regra de somar os expoentes. [p=0.3] {g}Teste: [p=0.2] quatro mais "
        "oito dá doze; [p=0.2] dois elevado a cinco dá trinta e dois. [p=0.2] Somar expoentes só vale no *produto.*"),
    dict(id="14", block="vf", text=
        "{t}Seis: [p=0.2] dois ao cubo, [p=0.2] tudo elevado ao quadrado, [p=0.2] é dois elevado a *seis.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque dá vontade de somar: [p=0.2] três mais dois, [p=0.2] cinco. "
        "[p=0.3] {g}Mas a fila de três fatores é *copiada* duas vezes: [p=0.2] seis fatores. [p=0.2] Potência de potência "
        "*multiplica.*"),
    dict(id="15", block="vf", text=
        "{t}Sete: [p=0.2] raiz de nove mais dezesseis [p=0.2] é raiz de nove mais raiz de dezesseis. [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque, na multiplicação, [p=0.2] a raiz se distribui. [p=0.3] {g}Teste: "
        "[p=0.2] raiz de vinte e cinco dá cinco; [p=0.2] três mais quatro dá sete. [p=0.2] Na soma, [p=0.2] a raiz *não* se "
        "distribui."),
    dict(id="16", block="vf", text=
        "{t}Oito: [p=0.2] raiz de *xis* ao quadrado é sempre *xis.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana "
        "porque a raiz parece desfazer o quadrado direto. [p=0.3] {g}Teste com menos cinco: [p=0.2] ao quadrado, [p=0.2] vinte "
        "e cinco; [p=0.2] a raiz devolve *cinco,* positivo. [p=0.2] É o *módulo* de xis: [p=0.2] o valor sem sinal."),
    dict(id="17", block="vf", text=
        "{t}Nove: [p=0.2] a raiz cúbica de menos oito *existe,* [p=0.2] e dá menos dois. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Verdadeiro!* [p=0.3] {e}Parece falso porque raiz de negativo costuma não existir. [p=0.3] {g}Mas menos dois ao "
        "cubo dá menos oito. [p=0.2] Quem não existe, [p=0.2] nos números reais, [p=0.2] é a raiz *quadrada* de menos quatro."),
    dict(id="18", block="vf", text=
        "{t}E dez: [p=0.2] dois raiz de três *mais* três raiz de dois [p=0.2] dá cinco raiz de cinco. [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque parece só somar tudo o que aparece. [p=0.3] {g}Mas são frutas "
        "diferentes. [p=0.2] Só se somam raízes com o mesmo *índice,* [p=0.2] o numerozinho da casinha, [p=0.2] e o mesmo "
        "*radicando,* [p=0.2] o número de dentro."),
    dict(id="19", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Sete falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] as cinco "
        "questões, [p=0.2] todas inéditas, [p=0.2] no estilo do ENEM."),

    # ================= QUESTÃO 1: MESMA BASE =================
    dict(id="20", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Simplificando a expressão [p=0.2] vinte e sete ao quadrado, [p=0.2] vezes nove, [p=0.2] "
        "dividido por três elevado a seis, [p=0.2] obtém-se: [p=0.4] {la}A, [p=0.2] três. [p=0.2] {lb}B, [p=0.2] seis. "
        "[p=0.2] {lc}C, [p=0.2] nove. [p=0.2] {ld}D, [p=0.2] duzentos e quarenta e três. [p=0.2] {le}E, [p=0.2] setecentos "
        "e vinte e nove. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="21", block="q1", text=
        "{t}Primeiro, [p=0.2] tudo na *mesma fruta:* [p=0.2] base três. [p=0.3] {a}Vinte e sete é três ao cubo; [p=0.2] ao "
        "quadrado, [p=0.2] potência de potência, [p=0.2] três elevado a seis. [p=0.3] {b}Nove é três ao quadrado. [p=0.3] "
        "{c}Em cima, [p=0.2] seis mais dois, [p=0.2] três elevado a oito. [p=0.2] Dividindo por três elevado a seis, [p=0.2] "
        "sobra três ao quadrado: [p=0.2] *nove.* [p=0.2] {ok}*Letra C!* [p=0.4] {xa}A A somou na potência de potência. "
        "[p=0.2] {xd}A D leu como torre. [p=0.2] {xe}A E multiplicou os expoentes no produto. [p=0.2] {xb}E a B fez três ao "
        "quadrado como três vezes dois."),

    # ================= QUESTÃO 2: POTÊNCIAS DE 10 "POR UNIDADE" =================
    dict(id="22", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Uma fábrica produziu *três vírgula seis vezes dez elevado a sete* parafusos. [p=0.3] "
        "{b}Eles foram embalados em caixas com *um vírgula dois vezes dez elevado a três* parafusos cada. [p=0.3] {c}Quantas "
        "caixas foram usadas? [p=0.4] {la}A, [p=0.2] três vezes dez elevado a menos quatro. [p=0.2] {lb}B, [p=0.2] três vezes "
        "dez elevado a quatro. [p=0.2] {lc}C, [p=0.2] três vezes dez elevado a dez. [p=0.2] {ld}D, [p=0.2] quatro vírgula "
        "trinta e dois vezes dez elevado a dez. [p=0.2] {le}E, [p=0.2] dois vírgula quatro vezes dez elevado a quatro. "
        "[p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="23", block="q2", text=
        "{t}Quantas caixas? [p=0.2] Parafusos *por caixa:* [p=0.2] é *divisão.* [p=0.3] {a}Números com números: [p=0.2] três "
        "vírgula seis dividido por um vírgula dois, [p=0.2] *três.* [p=0.3] {b}Potências com potências: [p=0.2] dividiu, "
        "[p=0.2] subtrai: [p=0.2] sete menos três, [p=0.2] *quatro.* [p=0.3] {c}Três vezes dez elevado a quatro: [p=0.2] "
        "trinta mil caixas. [p=0.2] {ok}*Letra B!* [p=0.4] {xd}A D multiplicou. [p=0.2] {xc}A C somou os expoentes. [p=0.2] "
        "{xa}A A subtraiu ao contrário. [p=0.2] {xe}E a E subtraiu os números da frente."),

    # ================= QUESTÃO 3: EXPOENTE NEGATIVO COM FRAÇÃO =================
    dict(id="24", block="q3", text=
        "{t}Questão três. [p=0.3] {a}O valor de [p=0.2] dois quintos elevado a menos dois, [p=0.2] *mais* dois elevado a "
        "menos dois, [p=0.2] é: [p=0.4] {la}A, [p=0.2] menos treze meios. [p=0.2] {lb}B, [p=0.2] nove quartos. [p=0.2] "
        "{lc}C, [p=0.2] treze meios. [p=0.2] {ld}D, [p=0.2] quarenta e um centésimos. [p=0.2] {le}E, [p=0.2] cento e quatro "
        "vinte e cinco avos. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="25", block="q3", text=
        "{t}Expoente negativo: [p=0.2] inverte e tira o menos. [p=0.3] {a}Dois quintos vira cinco meios; [p=0.2] ao "
        "quadrado, [p=0.2] *vinte e cinco quartos.* [p=0.3] {b}Dois elevado a menos dois [p=0.2] vira um sobre dois ao "
        "quadrado: [p=0.2] *um quarto.* [p=0.3] {c}Somando, [p=0.2] vinte e seis quartos, [p=0.2] que simplifica para *treze "
        "meios.* [p=0.2] {ok}*Letra C!* [p=0.4] {xa}A A deixou o resultado negativo. [p=0.2] {xb}A B achou que dois elevado a "
        "menos dois é menos quatro. [p=0.2] {xd}A D não inverteu a primeira fração. [p=0.2] {xe}E a E não inverteu nada."),

    # ================= QUESTÃO 4: SIMPLIFICAR E SOMAR RADICAIS =================
    dict(id="26", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}O valor de [p=0.2] raiz de setenta e cinco [p=0.2] *mais* raiz de doze [p=0.2] é: "
        "[p=0.4] {la}A, [p=0.2] raiz de oitenta e sete. [p=0.2] {lb}B, [p=0.2] sete raiz de três. [p=0.2] {lc}C, [p=0.2] "
        "sete raiz de seis. [p=0.2] {ld}D, [p=0.2] vinte e nove raiz de três. [p=0.2] {le}E, [p=0.2] trinta. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="27", block="q4", text=
        "{t}Simplifique antes de dizer que não dá. [p=0.3] {a}Setenta e cinco é vinte e cinco vezes três: [p=0.2] o vinte e "
        "cinco sai da porta como *cinco.* [p=0.2] Cinco raiz de três. [p=0.3] {b}Doze é quatro vezes três: [p=0.2] *dois* "
        "raiz de três. [p=0.3] {c}Agora é maçã com maçã: [p=0.2] cinco mais dois, [p=0.2] *sete raiz de três.* [p=0.2] "
        "{ok}*Letra B!* [p=0.4] {xa}A A somou os radicandos. [p=0.2] {xc}A C somou também os de dentro. [p=0.2] {xd}A D tirou "
        "o vinte e cinco e o quatro sem tirar a raiz. [p=0.2] {xe}E a E multiplicou em vez de somar."),

    # ================= QUESTÃO 5: RACIONALIZAÇÃO =================
    dict(id="28", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Num projeto, [p=0.2] uma peça mede *dez sobre raiz de cinco* centímetros. [p=0.3] "
        "{b}Escrita sem raiz no denominador, [p=0.2] essa medida é: [p=0.4] {la}A, [p=0.2] dois raiz de cinco. [p=0.2] "
        "{lb}B, [p=0.2] dez raiz de cinco. [p=0.2] {lc}C, [p=0.2] dois. [p=0.2] {ld}D, [p=0.2] raiz de dois. [p=0.2] {le}E, "
        "[p=0.2] dois raiz de cinco sobre cinco. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="29", block="q5", text=
        "{t}Tire a raiz do porão [p=0.2] com o *um disfarçado:* [p=0.2] raiz de cinco sobre raiz de cinco. [p=0.3] {a}Em "
        "cima, [p=0.2] dez raiz de cinco. [p=0.2] Embaixo, [p=0.2] raiz de cinco vezes raiz de cinco, [p=0.2] *cinco.* "
        "[p=0.3] {b}Dez dividido por cinco: [p=0.2] *dois raiz de cinco.* [p=0.2] {ok}*Letra A!* [p=0.4] {xc}A C multiplicou "
        "só embaixo, [p=0.2] e mudou o valor. [p=0.2] {xb}A B esqueceu de dividir por cinco. [p=0.2] {xe}A E fez raiz de "
        "cinco vezes raiz de cinco igual a vinte e cinco. [p=0.2] {xd}E a D pôs tudo dentro da raiz."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="30", block="checklist", text=
        "{t}Agora, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* para "
        "outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}Expoente zero, [p=0.2] expoente negativo [p=0.2] e o sinal da "
        "base negativa: [p=0.2] episódio um. [p=0.3] {c}As sete propriedades, [p=0.2] a mesma base [p=0.2] e a soma que não "
        "tem regra: [p=0.2] episódio dois. [p=0.3] {d}Potências de dez: [p=0.2] episódio três."),
    dict(id="31", block="checklist", text=
        "{a}Quando a raiz existe [p=0.2] e o módulo: [p=0.2] episódio quatro. [p=0.3] {b}Simplificar [p=0.2] e somar "
        "radicais: [p=0.2] episódio cinco. [p=0.3] {c}Racionalizar [p=0.2] e o expoente fracionário: [p=0.2] episódio seis. "
        "[p=0.4] {d}O que você *não* marcou, [p=0.2] reveja o episódio correspondente."),

    # ================= META =================
    dict(id="32", block="meta", text=
        "{t}E antes de considerar este assunto dominado, [p=0.2] uma meta: [p=0.3] {a}resolva *trinta* questões [p=0.2] "
        "{b}e acerte pelo menos *vinte e uma,* [p=0.2] setenta por cento. [p=0.4] {c}Priorize as de simplificar radicais "
        "[p=0.2] e as de colocar tudo na mesma base. [p=0.2] São as que mais aparecem *dentro* de outras questões."),

    # ================= PONTE E CTA =================
    dict(id="33", block="ponte", text=
        "{a}O próximo assunto é *notação científica e ordem de grandeza.* [p=0.4] {b}E ele depende *inteiramente* das "
        "potências de dez que você dominou aqui. [p=0.3] {c}O contador de zeros vai trabalhar muito."),
    dict(id="34", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantas das dez pegadinhas você acertou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de potenciação e radiciação está completa. [p=0.2] Bons estudos, e *até a próxima aula* aqui no "
        "Estudativo. [p=1.5]"),
]
