# Roteiro — Função Exponencial: crescimento e decaimento, Episódio 6 de 6: Revisão geral, estratégia de prova,
#   pegadinhas e treino (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/26-funcao-exponencial-crescimento-decaimento.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (Q1–Q9). As 5 questões são INÉDITAS (números e alternativas do prompt do usuário).
#   Logaritmo: só a ponte (próxima série).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (o gancho só acrescenta, depois delas, o que a aula vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 a ESCADA QUE MULTIPLICA e a PAREDE INVISÍVEL (assíntota) · o expoente negativo VIRA DE CABEÇA PARA BAIXO ·
#   ep2 a RECEITA de dois ingredientes (Q₀ e a) · o fator é O QUE SOBRA · juros compostos = a exponencial de TERNO E
#       GRAVATA (ícone: a máquina de tradução) ·
#   ep3 o RELÓGIO QUE APITA (o expoente conta intervalos) · a PIZZA QUE SOBROU ·
#   ep4 a TARTARUGA E A LEBRE ao contrário · o teste da razão ·
#   ep5 as DUAS FOTOS IDÊNTICAS (mesma base) · TIRE A EMBALAGEM (isole a potência) · a LADEIRA descendo inverte a
#       desigualdade (ícone: a balança dos expoentes).
# O que a prova cobra (seção 01): crescimento por fator · decaimento e meia-vida · reconhecer o modelo (tabela/gráfico) ·
#   descobrir o tempo. O que mais rende: traduzir a frase no fator ("dobra a cada 20 min" → 2 por período; "cresce 3% ao
#   ano" → 1,03; "perde 15% ao ano" → 0,85; "meia-vida de 8 dias" → 1/2 a cada 8 dias).
# Onde aparece (seção 10): Biologia (curva em J; com recursos limitados, curva em S) · Química (carbono-14, meia-vida de
#   cerca de 5 730 anos) · Física (resfriamento até a temperatura ambiente) · Financeira (1 + i) · Geografia (Malthus:
#   população em PG, alimentos em PA).
# Estratégia (seção 09): conte os intervalos (convertendo unidades) · teste a lei em t = 0, 1 e 2 · não fechou na mesma
#   base e o enunciado deu log 2 ou log 3 → logaritmo.
# V/F (os 9 erros da seção 11, com números NOSSOS; 6 falsas e 3 verdadeiras — as verdadeiras são as versões CERTAS dos
#   erros 2, 3 e 7):
#   1 F perde 10% ao ano → fator 0,1 (é 0,9) · 2 V cresce 5% ao ano → fator 1,05 · 3 V 3 meias-vidas → sobra 12,5% ·
#   4 F dobra 5 vezes → ×10 (×2⁵ = ×32) · 5 F 2⁻² = −4 (= 1/4) · 6 F 5 · 2³ = 10³ = 1 000 (= 40) ·
#   7 V (1/2)ˣ > 8 → x < −3 · 8 F 100 · 3ᵗ = 2 700 → 300ᵗ = 2 700 (divida por 100: 3ᵗ = 27, t = 3) ·
#   9 F tabela 10, 20, 40: a lei 10 + 10t acerta t = 0 e t = 1, então é a certa (em t = 2 dá 30; a certa é 10 · 2ᵗ).
# QUESTÕES INÉDITAS (do prompt; conferidas em trabalho/conferir_questoes.py: uma única correta; cada errada = um erro
#   clássico; as letras foram ordenadas por nós):
#   Q1 (depreciação) celular de R$ 2.000,00, perde 20% ao ano sobre o valor anterior, 2 anos: 2 000 · 0,8² = R$ 1.280,00
#      → C. A R$ 80,00 (fator 0,2) · B R$ 1.200,00 (perda linear de 40%) · D R$ 1.600,00 (um ano só) · E R$ 2.880,00
#      (fator 1,2).
#   Q2 (meia-vida) 240 mg, meia-vida de 6 h, 24 h → 4 meias-vidas → 15 mg → B. A 7,5 mg (5 meias-vidas) · C 30 mg (3) ·
#      D 60 mg (dividiu por 4) · E 0 mg (subtraiu 50% duas vezes).
#   Q3 (qual lei) poluente 64, 48, 36, 27 mg por hora → N = 64 · 0,75ᵗ → E. A 64 − 16t (acerta t = 0 e 1, dá 32 em
#      t = 2) · B 64 · 0,25ᵗ (taxa no lugar do fator) · C 48 · 0,75ᵗ (começa em t = 1) · D 64 · 0,75t (produto: dá 0 em
#      t = 0).
#   Q4 (coeficiente) peixes P(t) = 200 · 2^(t/3), t em meses, chega a 6 400: 6 400 ÷ 200 = 32 = 2⁵ → t/3 = 5 → 15 meses
#      → C. A ≈ 1,7 mês (dividiu 5 por 3) · B 5 meses (esqueceu o ÷ 3) · D 48 meses (potência como produto: 2 · t/3 = 32)
#      · E 96 meses (igualou o expoente ao valor: t/3 = 32).
#   Q5 (resfriamento e inequação) T(t) = 20 + 160 · 0,5^(t/10), acima de 40 °C: 160 · 0,5^(t/10) > 20 → 0,5^(t/10) > 1/8
#      = 0,5³ → t/10 < 3 → menos de 30 min → D. A menos de 3 min (esqueceu o ÷ 10) · B menos de 20 min (não subtraiu os
#      20 °C antes de isolar a potência) · C mais de 30 min (não inverteu o sentido) · E sempre (confundiu com a
#      assíntota, que é 20 °C, a da cozinha).
# Gabaritos: C, B, E, C, D.
# Checklist (seção 13) → episódio (como o prompt pede): base, gráfico e assíntota → ep1 · taxa em fator e lei por dois
#   pontos → ep2 · duplicação e meia-vida → ep3 · afim × exponencial → ep4 · equações, evidência e inequações → ep5 ·
#   reconhecer quando precisa de logaritmo → próxima série.
# Meta (prompt e material): 30 questões, 21 acertos (70%), com pelo menos dez de meia-vida ou duplicação em contexto.
# Ponte (do usuário): Logaritmos.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de função exponencial: 9 pegadinhas e 5 questões estilo ENEM | Função Exponencial Ep. 6"
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
        "{a}A exponencial é a função das manchetes: [p=0.3] {b}vírus, [p=0.15] bactérias, [p=0.15] dívidas, [p=0.15] "
        "remédios, [p=0.15] radioatividade. [p=0.4] {c}O ENEM quase nunca escreve \"resolva a equação\"; [p=0.3] "
        "ele *conta uma história.* [p=0.4] {d}Hoje você treina para *traduzir a história.* [p=0.4] {e}Nove frases de "
        "verdadeiro ou falso [p=0.2] e cinco questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E o que a prova pede? [p=0.4] {a}*Crescimento por fator:* [p=0.2] bactérias, populações, seguidores. [p=0.3] "
        "{b}*Decaimento e meia-vida:* [p=0.2] remédios, radioatividade, depreciação. [p=0.3] {c}*Reconhecer o modelo* "
        "numa tabela ou num gráfico. [p=0.3] {d}E *descobrir o tempo.*"),
    dict(id="03", block="rende", text=
        "{t}E o que mais rende? [p=0.3] *Traduzir a frase no fator certo.* [p=0.4] {a}\"Dobra a cada vinte minutos\": "
        "[p=0.2] fator *dois* por período. [p=0.3] {b}\"Cresce três por cento ao ano\": [p=0.2] *um vírgula zero três.* "
        "[p=0.3] {c}\"Perde quinze por cento\": [p=0.2] *zero vírgula oitenta e cinco.* [p=0.3] {d}\"Meia-vida de oito "
        "dias\": [p=0.2] *um meio* a cada oito dias. [p=0.4] {e}Com o fator e o valor inicial, [p=0.2] a lei sai sozinha."),

    # ================= ÍNDICE DA REVISÃO: OS 5 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] relembre cada episódio. [p=0.4] {a}Um: [p=0.2] a *escada que multiplica* [p=0.2] e "
        "a *parede invisível,* [p=0.2] que a curva nunca toca. [p=0.2] E o expoente negativo *vira a fração de cabeça para "
        "baixo.* [p=0.4] {b}Dois: [p=0.2] a *receita* de dois ingredientes, [p=0.2] de onde começa e por quanto "
        "multiplica. [p=0.2] O fator é *o que sobra,* [p=0.2] e os juros compostos são a exponencial *de terno e "
        "gravata.*"),
    dict(id="05", block="indice", text=
        "{a}Três: [p=0.2] o *relógio que apita.* [p=0.2] O expoente conta *quantos intervalos* passaram, [p=0.2] e a "
        "meia-vida corta *a pizza que sobrou.* [p=0.4] {b}Quatro: [p=0.2] a *tartaruga e a lebre ao contrário:* [p=0.2] "
        "a reta sai na frente, [p=0.2] mas a curva alcança e passa. [p=0.4] {c}Cinco: [p=0.2] as *duas fotos idênticas,* "
        "[p=0.2] mesma base, expoentes iguais; [p=0.2] e a *ladeira descendo,* que inverte a desigualdade."),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="06", block="onde", text=
        "{t}E as outras provas? [p=0.4] {a}Na *Biologia,* [p=0.2] bactérias e populações: [p=0.2] a curva em *jota.* "
        "[p=0.2] Com recursos limitados, [p=0.2] ela vira um *esse.* [p=0.3] {b}Na *Química,* [p=0.2] o decaimento "
        "radioativo [p=0.2] e o *carbono catorze,* [p=0.2] com meia-vida de uns cinco mil e setecentos anos."),
    dict(id="07", block="onde", text=
        "{c}Na *Física,* [p=0.2] o café esfriando [p=0.2] até a temperatura da sala. [p=0.3] {d}Nos *juros compostos,* "
        "[p=0.2] o fator é um mais i. [p=0.3] {e}E na *Geografia,* [p=0.2] Malthus: [p=0.2] a população multiplica, "
        "[p=0.2] os alimentos só somam. [p=0.2] É a exponencial contra a afim."),

    # ================= ESTRATÉGIA: 3 HÁBITOS (seção 09) =================
    dict(id="08", block="habitos", text=
        "{t}E na hora da prova? [p=0.2] Três hábitos. [p=0.4] {a}Um: [p=0.2] *conte os intervalos antes de qualquer "
        "conta.* [p=0.2] Duas horas, dobrando a cada vinte minutos: [p=0.2] cento e vinte dividido por vinte, [p=0.2] "
        "*seis.* [p=0.2] E converta as unidades primeiro. [p=0.4] {b}Dois: [p=0.2] *teste a lei em zero, um e dois.* "
        "[p=0.2] Uma reta acerta dois pontos [p=0.2] e erra o terceiro."),
    dict(id="09", block="habitos", text=
        "{c}Três: [p=0.2] a conta *não fechou* na mesma base, [p=0.2] e o enunciado deu *log de dois* ou *log de três?* "
        "[p=0.3] É a vez do *logaritmo,* [p=0.2] o assunto da próxima série."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="10", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="11", block="vf", text=
        "{t}Um: [p=0.2] um carro perde *dez por cento* do valor por ano. [p=0.2] O fator é *zero vírgula um.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o dez por cento está escrito ali. [p=0.3] {g}Mas o "
        "fator é *o que sobra:* [p=0.2] perdeu dez, ficou com noventa. [p=0.2] Fator *zero vírgula nove.*"),
    dict(id="12", block="vf", text=
        "{t}Dois: [p=0.2] uma cidade cresce *cinco por cento* ao ano. [p=0.2] O fator é *um vírgula zero cinco.* "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque muita gente escreve *cinco* como "
        "fator. [p=0.3] {g}Mas taxa vira fator *somando um:* [p=0.2] os cem por cento que já existiam, [p=0.2] mais os "
        "cinco."),
    dict(id="13", block="vf", text=
        "{t}Três: [p=0.2] depois de *três meias-vidas,* [p=0.2] sobra *doze e meio por cento.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque três metades \"somam\" cento e cinquenta por cento, "
        "[p=0.2] e não sobraria nada. [p=0.3] {g}Mas cada meia-vida corta *a pizza que sobrou:* [p=0.2] cinquenta, "
        "[p=0.2] vinte e cinco, [p=0.2] doze e meio."),
    dict(id="14", block="vf", text=
        "{t}Quatro: [p=0.2] uma população *dobra cinco vezes.* [p=0.2] Ela fica *dez vezes* maior. [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque cinco vezes dois parece a conta. [p=0.3] {g}Mas duplicações "
        "*se multiplicam:* [p=0.2] dois, quatro, oito, dezesseis, [p=0.2] *trinta e dois.*"),
    dict(id="15", block="vf", text=
        "{t}Cinco: [p=0.2] dois elevado a *menos dois* [p=0.2] é *menos quatro.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque o sinal de menos parece passar para o resultado. [p=0.3] {g}Mas o "
        "expoente negativo *vira a fração de cabeça para baixo:* [p=0.2] *um quarto.* [p=0.2] Continua positivo."),
    dict(id="16", block="vf", text=
        "{t}Seis: [p=0.2] cinco vezes dois ao cubo [p=0.2] é *dez ao cubo,* [p=0.2] mil. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque cinco vezes dois é dez, [p=0.2] e a conta parece andar junto. [p=0.3] "
        "{g}Mas o número da frente *não entra na base:* [p=0.2] primeiro a potência, oito, [p=0.2] depois vezes cinco: "
        "[p=0.2] *quarenta.*"),
    dict(id="17", block="vf", text=
        "{t}Sete: [p=0.2] um meio elevado a xis, [p=0.2] *maior que oito,* [p=0.2] vale para *xis menor que menos "
        "três.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque oito é um meio elevado a menos "
        "três, [p=0.2] e dá vontade de escrever xis *maior* que menos três. [p=0.3] {g}Mas base entre zero e um é a "
        "*ladeira descendo:* [p=0.2] a desigualdade *vira.*"),
    dict(id="18", block="vf", text=
        "{t}Oito: [p=0.2] em *cem vezes três elevado a tê, igual a dois mil e setecentos,* [p=0.2] dá para juntar: "
        "[p=0.2] *trezentos* elevado a tê. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque parece só "
        "uma multiplicação. [p=0.3] {g}*Tire a embalagem* primeiro: [p=0.2] divida por cem. [p=0.2] Três elevado a tê "
        "igual a *vinte e sete:* [p=0.2] tê igual a *três.*"),
    dict(id="19", block="vf", text=
        "{t}E nove: [p=0.2] a tabela dá *dez, vinte e quarenta.* [p=0.2] A lei *dez mais dez tê* [p=0.2] acerta o zero "
        "e o um. [p=0.2] Então ela é a certa. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque dois "
        "pontos certos parecem prova. [p=0.3] {g}Mas *teste o terceiro:* [p=0.2] em dois, ela dá trinta, não quarenta. "
        "[p=0.2] A certa é *dez vezes dois elevado a tê.*"),
    dict(id="20", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas. [p=0.2] Em todas, [p=0.2] *escreva o fator e o número de intervalos* antes da conta."),

    # ================= QUESTÃO 1: DEPRECIAÇÃO =================
    dict(id="21", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Um celular custou *dois mil reais.* [p=0.2] Ele perde *vinte por cento* do valor por "
        "ano, [p=0.2] sempre sobre o valor do ano anterior. [p=0.3] {b}O valor depois de *dois anos* é: [p=0.4] {la}A, "
        "[p=0.2] oitenta reais. [p=0.2] {lb}B, [p=0.2] mil e duzentos. [p=0.2] {lc}C, [p=0.2] mil duzentos e oitenta. "
        "[p=0.2] {ld}D, [p=0.2] mil e seiscentos. [p=0.2] {le}E, [p=0.2] dois mil oitocentos e oitenta. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q1", text=
        "{d}O fator é o que sobra: [p=0.2] perdeu vinte, [p=0.2] fica *zero vírgula oito.* [p=0.2] Dois anos: [p=0.2] "
        "*dois intervalos.* [p=0.3] {a}Dois mil vezes zero vírgula oito ao quadrado: [p=0.2] zero vírgula sessenta e "
        "quatro. [p=0.3] {b}*Mil duzentos e oitenta reais.* [p=0.2] {ok}*Letra C!* [p=0.2] {v}Confira: [p=0.2] "
        "perdeu, mas menos que os quarenta por cento \"somados\". [p=0.4] {xa}A A usou o fator *zero vírgula dois.* "
        "[p=0.2] {xb}A B tirou quarenta por cento de uma vez. [p=0.2] {xd}A D parou em *um ano,* [p=0.2] {xe}e a E "
        "*aumentou* o preço."),

    # ================= QUESTÃO 2: MEIA-VIDA =================
    dict(id="23", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Um paciente tem *duzentos e quarenta miligramas* de um remédio no sangue. [p=0.2] A "
        "meia-vida é de *seis horas.* [p=0.3] {b}Depois de *vinte e quatro horas,* [p=0.2] restam: [p=0.4] {la}A, "
        "[p=0.2] sete vírgula cinco miligramas. [p=0.2] {lb}B, [p=0.2] quinze. [p=0.2] {lc}C, [p=0.2] trinta. [p=0.2] "
        "{ld}D, [p=0.2] sessenta. [p=0.2] {le}E, [p=0.2] zero. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="24", block="q2", text=
        "{d}Conte os apitos do relógio: [p=0.2] vinte e quatro dividido por seis, [p=0.2] *quatro meias-vidas.* [p=0.3] "
        "{a}Corte a pizza que sobrou: [p=0.2] cento e vinte, [p=0.2] sessenta, [p=0.2] trinta, [p=0.2] *quinze.* "
        "[p=0.2] {ok}*Letra B!* [p=0.4] {xa}A A contou *cinco* meias-vidas, [p=0.2] {xc}e a C, só *três.* [p=0.2] "
        "{xd}A D dividiu por quatro, [p=0.2] o número de meias-vidas. [p=0.2] {xe}E a E tirou cinquenta por cento duas "
        "vezes do total. [p=0.2] Remédio *não zera:* [p=0.2] é a parede invisível."),

    # ================= QUESTÃO 3: QUAL LEI =================
    dict(id="25", block="q3", text=
        "{t}Questão três. [p=0.3] {a}A quantidade de um poluente num tanque, [p=0.2] em miligramas, [p=0.2] medida a cada "
        "hora, [p=0.2] foi: [p=0.2] *sessenta e quatro, [p=0.15] quarenta e oito, [p=0.15] trinta e seis, [p=0.15] vinte "
        "e sete.* [p=0.3] {b}A lei é: [p=0.4] {la}A, [p=0.2] sessenta e quatro menos dezesseis tê. [p=0.2] {lb}B, "
        "[p=0.2] sessenta e quatro vezes zero vírgula vinte e cinco elevado a tê. [p=0.2] {lc}C, [p=0.2] quarenta e oito "
        "vezes zero vírgula setenta e cinco elevado a tê. [p=0.2] {ld}D, [p=0.2] sessenta e quatro vezes zero vírgula "
        "setenta e cinco, vezes tê. [p=0.2] {le}E, [p=0.2] sessenta e quatro vezes zero vírgula setenta e cinco elevado a "
        "tê. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q3", text=
        "{d}O teste da razão: [p=0.2] quarenta e oito sobre sessenta e quatro, [p=0.2] *zero vírgula setenta e cinco.* "
        "[p=0.2] E de novo, [p=0.2] e de novo. [p=0.2] Exponencial. [p=0.3] {a}Agora o hábito dois: [p=0.2] teste em "
        "zero, um e dois. [p=0.2] {xd}A D dá *zero* no começo. [p=0.2] {xc}A C começa em *quarenta e oito.* [p=0.2] "
        "{xb}A B usou a *taxa,* não o fator: [p=0.2] dá dezesseis. [p=0.3] {b}{xa}A A acerta o zero e o um, [p=0.2] mas "
        "em dois dá *trinta e dois.* [p=0.2] {ok}*Letra E!*"),

    # ================= QUESTÃO 4: EQUAÇÃO COM COEFICIENTE =================
    dict(id="27", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Os peixes de um lago seguem *pê de tê igual a duzentos vezes dois elevado a tê "
        "sobre três,* [p=0.2] com tê em meses. [p=0.3] {b}A população chega a *seis mil e quatrocentos* em: [p=0.4] "
        "{la}A, [p=0.2] cerca de um vírgula sete mês. [p=0.2] {lb}B, [p=0.2] cinco meses. [p=0.2] {lc}C, [p=0.2] "
        "quinze. [p=0.2] {ld}D, [p=0.2] quarenta e oito. [p=0.2] {le}E, [p=0.2] noventa e seis. [p=0.4] {p}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="28", block="q4", text=
        "{d}Tire a embalagem: [p=0.2] seis mil e quatrocentos dividido por duzentos, [p=0.2] *trinta e dois.* [p=0.3] "
        "{a}Trinta e dois é *dois à quinta.* [p=0.2] Duas fotos idênticas: [p=0.2] tê sobre três igual a *cinco.* "
        "[p=0.3] {b}Tê igual a *quinze meses.* [p=0.2] {ok}*Letra C!* [p=0.4] {xa}A A *dividiu* cinco por três. "
        "[p=0.2] {xb}A B esqueceu o *sobre três.* [p=0.2] {xd}A D tratou a potência como *produto,* [p=0.2] {xe}e a E "
        "igualou o expoente ao *valor,* trinta e dois."),

    # ================= QUESTÃO 5: RESFRIAMENTO E INEQUAÇÃO =================
    dict(id="29", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Um forno foi desligado. [p=0.2] A temperatura é *tê igual a vinte, mais cento e "
        "sessenta vezes zero vírgula cinco elevado a tê sobre dez,* [p=0.2] em graus, [p=0.2] com tê em minutos. "
        "[p=0.3] {b}A temperatura fica *acima de quarenta graus:* [p=0.4] {la}A, [p=0.2] por menos de três minutos. "
        "[p=0.2] {lb}B, [p=0.2] por menos de vinte. [p=0.2] {lc}C, [p=0.2] por mais de trinta. [p=0.2] {ld}D, [p=0.2] "
        "por menos de trinta. [p=0.2] {le}E, [p=0.2] sempre, porque nunca cai abaixo de quarenta. [p=0.4] {p}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="30", block="q5", text=
        "{d}Primeiro, *tire os vinte* da cozinha: [p=0.2] cento e sessenta vezes a potência, [p=0.2] maior que *vinte.* "
        "[p=0.3] {a}Divida por cento e sessenta: [p=0.2] a potência é maior que *um oitavo,* [p=0.2] que é zero vírgula "
        "cinco ao cubo. [p=0.3] {b}Base zero vírgula cinco: [p=0.2] *ladeira descendo,* o sinal vira. [p=0.2] Tê sobre "
        "dez *menor* que três: [p=0.2] *menos de trinta minutos.* [p=0.2] {ok}*Letra D!* [p=0.4] {xa}A A esqueceu o "
        "*dividido por dez.* [p=0.2] {xb}A B não tirou os vinte graus. [p=0.2] {xc}A C não inverteu o sinal. [p=0.2] "
        "{xe}E a E confundiu com a *parede invisível:* [p=0.2] ela é *vinte graus,* [p=0.2] a temperatura da cozinha."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="31", block="checklist", text=
        "{t}O checklist. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* para outra pessoa, [p=0.2] "
        "sem consultar nada. [p=0.4] {b}Base, gráfico e assíntota: [p=0.2] episódio um. [p=0.3] {c}Taxa em fator e lei "
        "por dois pontos: [p=0.2] episódio dois. [p=0.3] {d}Duplicação e meia-vida: [p=0.2] episódio três."),
    dict(id="32", block="checklist", text=
        "{a}Afim ou exponencial: [p=0.2] episódio quatro. [p=0.3] {b}Equações, evidência e inequações: [p=0.2] episódio "
        "cinco. [p=0.3] {c}E reconhecer quando precisa de *logaritmo:* [p=0.2] a próxima série. [p=0.4] {d}O que você "
        "*não* marcou, [p=0.2] reveja o episódio correspondente."),

    # ================= META =================
    dict(id="33", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *trinta questões* [p=0.2] {b}e acerte pelo menos *vinte e uma,* [p=0.2] "
        "setenta por cento. [p=0.4] {c}E pelo menos *dez de meia-vida ou duplicação* em contexto."),

    # ================= PONTE (frase do usuário) E CTA =================
    dict(id="34", block="ponte", text=
        "{a}E quando a equação é *dois elevado a xis igual a dez,* [p=0.2] que não fecha em base nenhuma? [p=0.5] {b}O "
        "próximo assunto é *Logaritmos:* [p=0.2] definição, propriedades e equações, [p=0.3] {c}a ferramenta que *tira a "
        "incógnita do expoente.*"),
    dict(id="35", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] {com}E me conte nos "
        "*comentários:* [p=0.2] qual pegadinha te pegou? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo "
        "tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] "
        "para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}A série de função exponencial está completa. "
        "[p=0.2] Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
