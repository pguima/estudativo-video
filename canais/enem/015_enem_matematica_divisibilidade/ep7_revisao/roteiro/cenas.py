# Roteiro — Divisibilidade, Primos, MMC e MDC, Episódio 7 de 7: Revisão geral, pegadinhas e treino para o ENEM
# Base: Estudos/Enem/estudos/01-matematica/02-divisibilidade-primos-mmc-mdc.html — seções 01, 11 e 13.
#   NENHUMA das Questões 1–9 da seção 12.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias da série (relembradas no mapa, cena 04, e no quadro "lembrando" de cada questão):
#   divisores = retângulos de quadradinhos · critério = teste rápido · primos = tijolos · fatoração = receita do número ·
#   contagem de divisores = montar um lanche · MMC = o reencontro · MDC = a maior régua · decisão = repete ou reparte?
# Lidos EXATAMENTE como no material: os dois formatos e os temas de menor frequência (seção 01, cena 03), as regras certas da
#   seção 11 (respostas do V ou F), a instrução e a meta do checklist (seção 13).
# V ou F: os 9 erros da seção 11 viram afirmações; 4 são a regra certa (V) e 5 o erro (F), para o aluno não chutar.
# Questões 1–5: INÉDITAS, situações hipotéticas marcadas na tela "situação elaborada para fins didáticos".
#   Conferidas por script (uma única correta; cada distrator sai do erro atribuído):
#   Q1 código 2 7 x 1 4 divisível por 9 → soma 14 + x → só x = 4 (B). 1 e 7: critério do 3 · 9: confundiu o algarismo com
#      o divisor · "nenhum": não testou.  → B
#   Q2 336 = 2⁴·3·7 → (4+1)(1+1)(1+1) = 20 (E). 4 = expoentes sem +1 · 5 = +1 só no primeiro · 6 = somou os expoentes ·
#      10 = esqueceu o 7 (expoente 1 sozinho).  → E
#   Q3 faróis 12 s e 18 s, 3 min = 180 s, sem contar o agora → MMC 36 → 180 ÷ 36 = 5 (A). 6 = MDC (método trocado) ·
#      10 = dividiu por um farol só · 30 = dividiu pelo MDC · 36 = parou no MMC.  → A
#   Q4 terreno 30 m × 48 m, estacas → MDC 6, perímetro 2·(30+48) = 156 (dica rápida da fórmula na cena 21), 156 ÷ 6 = 26 (C). 6 = parou no MDC · 13 = não dobrou o
#      perímetro · 27 = somou 1 na figura fechada · 240 = MMC (método trocado).  → C
#   Q5 copos em caixas de 8, pratos em caixas de 12, mesma quantidade, caixas fechadas → MMC 24 (D). 3 = nº de caixas de
#      copos · 4 = MDC (método trocado; a régua denuncia: 4 < 12) · 20 = somou · 96 = produto (comum, mas não o menor).  → D
# Atalho do VARAL ÚNICO (pedido do usuário em 22/10): cena 17b (6 e 10 → MMC 30, MDC 2) e usado nas Q3 (12, 18),
#   Q4 (30, 48) e Q5 (8, 12): MMC = todos os primos do varal; MDC = só os primos que dividiram todos juntos.
# Cores: azul = definição · roxo = regra · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Você Cai Nessas 9 Pegadinhas de MMC e MDC? | Divisibilidade Ep. 7"
# Estilo da voz (gerar_voz_local.py): voz Neno, mais emoção, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que tem medo de matemática: voz calorosa, acolhedora e MUITO expressiva, com bastante variação de "
            "entonação e emoção verdadeira. Sorria na voz. Esta é a aula de revisão, com clima de desafio e de jogo: "
            "faça as perguntas com suspense, revele as respostas com entusiasmo, mostre surpresa nas pegadinhas e "
            "comemore os acertos. Nas contas, fale devagar e com clareza, passo a passo. Ritmo didático e tranquilo, "
            "sem pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
    "MMC": "M M C",
    "MDC": "M D C",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Este assunto rende *questão própria* quase todo ano no ENEM, [p=0.3] {b}e o formato é quase sempre *um de dois.* "
        "[p=0.4] {c}Hoje você confere se esse ponto já é seu."),

    # ================= COMO O ENEM COBRA =================
    dict(id="02", block="cobra", text=
        "{t}Primeiro, [p=0.2] um teste de memória. [p=0.3] {a}Quais são os *dois formatos* que mais caem? [p=0.3] "
        "{p}Pause e tente lembrar. [p=2.0]"),
    dict(id="03", block="cobra", text=
        "{a}Um: [p=0.2] coisas que se repetem e voltam a coincidir. [p=0.3] Ônibus, [p=0.2] lâmpadas, [p=0.2] remédios. "
        "[p=0.3] Isso é *MMC,* sempre. [p=0.5] {b}Dois: [p=0.2] repartir em pedaços iguais, [p=0.2] do maior tamanho "
        "possível. [p=0.3] Tábuas, [p=0.2] grupos, [p=0.2] estacas. [p=0.3] Isso é *MDC,* sempre. [p=0.5] {c}Com menor "
        "frequência, [p=0.2] aparecem critérios de divisibilidade em questões de código e senha, [p=0.2] contagem de divisores, "
        "[p=0.2] e fatoração usada como ferramenta."),

    # ================= O MAPA DA SÉRIE =================
    dict(id="04", block="mapa", text=
        "{t}E as imagens da série? [p=0.3] {a}Os divisores são os *retângulos* de quadradinhos, [p=0.2] e o critério é um "
        "*teste rápido.* [p=0.4] {b}Os primos são *tijolos.* [p=0.3] {c}Fatorar é achar a *receita* do número, [p=0.2] e "
        "contar divisores é montar um *lanche.* [p=0.4] {d}O MMC é o *reencontro.* [p=0.3] {e}O MDC é a *maior régua.* "
        "[p=0.4] {f}E na dúvida: [p=0.2] *repete ou reparte?*"),

    # ================= VERDADEIRO OU FALSO =================
    dict(id="05", block="vf", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso.* [p=0.3] Nove frases, [p=0.2] nove pausas. [p=0.4] {q}Primeira: [p=0.2] "
        "o um é primo. [p=0.2] {p}Pause. [p=2.0] {r}*Falso!* [p=0.3] {w}Engana porque o um só é dividido por um e por ele "
        "mesmo. [p=0.3] {k}Mas primo tem exatamente dois divisores. [p=0.2] O um tem só um."),
    dict(id="06", block="vf", text=
        "{q}Segunda: [p=0.2] o dois é primo, [p=0.2] e é o único primo par. [p=0.2] {p}Pause. [p=2.0] {r}*Verdadeiro!* "
        "[p=0.3] {w}Muita gente acha que par não pode ser primo. [p=0.3] {k}Mas os divisores do dois são um e dois: "
        "[p=0.2] exatamente dois."),
    dict(id="07", block="vf", text=
        "{q}Terceira: [p=0.2] no MDC, [p=0.2] você pega o *maior* expoente de cada fator. [p=0.2] {p}Pause. [p=2.0] "
        "{r}*Falso!* [p=0.3] {w}Engana porque no MMC é o maior. [p=0.3] {k}No MDC é o menor: [p=0.2] o divisor comum "
        "precisa caber nos dois. [p=0.2] É a régua que cabe em todas as tábuas."),
    dict(id="08", block="vf", text=
        "{q}Quarta: [p=0.2] no MMC, [p=0.2] entram *todos* os fatores, [p=0.2] com o maior expoente. [p=0.2] {p}Pause. "
        "[p=2.0] {r}*Verdadeiro!* [p=0.3] {w}A pegadinha é usar só os fatores comuns. [p=0.3] {k}Mas o múltiplo comum "
        "precisa conter cada número inteiro, [p=0.2] então nenhum fator pode faltar."),
    dict(id="09", block="vf", text=
        "{q}Quinta: [p=0.2] achou o MMC, [p=0.2] a questão de quantas vezes está respondida. [p=0.2] {p}Pause. [p=2.0] "
        "{r}*Falso!* [p=0.3] {w}Engana porque a conta difícil já foi feita. [p=0.3] {k}Mas se pediram a quantidade num "
        "intervalo, [p=0.2] ainda falta dividir o intervalo pelo MMC."),
    dict(id="10", block="vf", text=
        "{q}Sexta: [p=0.2] dois ao cubo, vezes três ao quadrado, vezes cinco [p=0.2] tem vinte e quatro divisores. [p=0.2] "
        "{p}Pause. [p=2.0] {r}*Verdadeiro!* [p=0.3] {w}Quem multiplica só os expoentes acha seis. [p=0.3] {k}Mas cada "
        "expoente pode valer zero também: [p=0.2] quatro, vezes três, vezes dois, [p=0.2] vinte e quatro. [p=0.2] É o lanche."),
    dict(id="11", block="vf", text=
        "{q}Sétima: [p=0.2] MDC vezes MMC [p=0.2] é igual ao produto dos números, [p=0.2] mesmo com três números. [p=0.2] "
        "{p}Pause. [p=2.0] {r}*Falso!* [p=0.3] {w}Engana porque funciona direitinho com dois. [p=0.3] {k}Mas só vale para "
        "dois: [p=0.2] com três números, a igualdade não se sustenta."),
    dict(id="12", block="vf", text=
        "{q}Oitava: [p=0.2] o zero é divisor de todo número. [p=0.2] {p}Pause. [p=2.0] {r}*Falso!* [p=0.3] {w}Engana "
        "porque o zero aparece em toda tabuada. [p=0.3] {k}Ele é múltiplo de qualquer número, [p=0.2] mas nunca divisor: "
        "[p=0.2] divisão por zero não existe."),
    dict(id="13", block="vf", text=
        "{q}Nona: [p=0.2] uma cerca de vinte e quatro por sessenta metros [p=0.2] tem perímetro de cento e sessenta e oito "
        "metros. [p=0.2] {p}Pause. [p=2.0] {r}*Verdadeiro!* [p=0.3] {w}A pegadinha é somar só vinte e quatro mais sessenta "
        "e parar no oitenta e quatro. [p=0.3] {k}O retângulo tem quatro lados: [p=0.2] duas vezes oitenta e quatro."),

    # ================= QUESTÃO 1: CRITÉRIO =================
    dict(id="14", block="q1", text=
        "{t}Agora, [p=0.2] cinco questões inéditas. [p=0.3] {r}Lembrando: [p=0.2] o critério é um teste rápido; [p=0.2] "
        "para o nove, some os algarismos. [p=0.4] {a}Questão um. [p=0.2] Um cofre abre com o código dois, sete, xis, um, "
        "quatro, [p=0.2] que precisa ser divisível por nove. [p=0.3] Qual é o algarismo xis? [p=0.4] {A}A: um. [p=0.3] "
        "{B}B: quatro. [p=0.3] {C}C: sete. [p=0.3] {D}D: nove. [p=0.3] {E}E: nenhum algarismo serve. [p=0.4] "
        "{p}Pause e tente! [p=2.0]"),
    dict(id="15", block="q1", text=
        "{t}Somando o que já existe: [p=0.2] dois mais sete mais um mais quatro, [p=0.2] catorze. [p=0.3] {s}Catorze mais xis "
        "precisa dar um múltiplo de nove: [p=0.2] dezoito. [p=0.3] Xis é quatro. [p=0.2] {ok}*Letra B!* [p=0.4] {xa}O um e "
        "o sete dão soma quinze e vinte e um: [p=0.2] servem para o três, [p=0.2] não para o nove. [p=0.3] {xd}A D confunde o "
        "algarismo com o divisor. [p=0.3] {xe}E a E não testou."),

    # ================= QUESTÃO 2: CONTAGEM DE DIVISORES =================
    dict(id="16", block="q2", text=
        "{r}Lembrando: [p=0.2] fatorar é achar a receita, [p=0.2] e contar divisores é montar um lanche. [p=0.4] {a}Questão "
        "dois. [p=0.2] Um organizador quer arrumar trezentas e trinta e seis cadeiras em filas iguais, sem sobrar. [p=0.3] "
        "Trezentos e trinta e seis é dois elevado a quatro, vezes três, vezes sete. [p=0.3] Quantas quantidades de cadeiras "
        "por fila são possíveis? [p=0.4] {A}A: quatro. [p=0.3] {B}B: cinco. [p=0.3] {C}C: seis. [p=0.3] {D}D: dez. [p=0.3] "
        "{E}E: vinte. [p=0.4] {p}Pause e tente! [p=2.0]"),
    dict(id="17", block="q2", text=
        "{t}Cada quantidade possível é um divisor. [p=0.3] {s}Some um em cada expoente: [p=0.2] cinco, dois e dois. "
        "[p=0.3] Multiplique: [p=0.2] vinte. [p=0.2] {ok}*Letra E!* [p=0.4] {xa}O quatro multiplica os expoentes sem somar "
        "um. [p=0.3] {xb}O cinco soma um só no primeiro. [p=0.3] {xc}O seis soma os expoentes. [p=0.3] {xd}E o dez esquece o "
        "sete, [p=0.2] que tem expoente um."),

    # ================= O ATALHO DO VARAL ÚNICO =================
    dict(id="17b", block="varal", text=
        "{t}Antes das próximas, [p=0.2] o atalho mais rápido da série. [p=0.3] {a}Fatore *todos os números juntos,* [p=0.2] "
        "num varal só. [p=0.3] {b}Divida pelo menor primo que dividir algum deles; [p=0.2] quem não divide, [p=0.2] desce "
        "igual. [p=0.4] {c}Exemplo: [p=0.2] seis e dez. [p=0.2] Por dois: [p=0.2] três e cinco. [p=0.2] Por três: [p=0.2] "
        "um e cinco. [p=0.2] Por cinco: [p=0.2] um e um. [p=0.4] {d}MMC: [p=0.2] multiplique *todos* os primos do varal. "
        "[p=0.2] Dois vezes três vezes cinco, [p=0.2] trinta. [p=0.4] {e}MDC: [p=0.2] só os primos que dividiram *todos ao "
        "mesmo tempo.* [p=0.2] Aqui, só o dois. [p=0.3] {f}Um varal, [p=0.2] dois resultados."),

    # ================= QUESTÃO 3: MMC E "QUANTAS VEZES" =================
    dict(id="18", block="q3", text=
        "{r}Lembrando: [p=0.2] o MMC é o reencontro. [p=0.4] {a}Questão três. [p=0.2] Dois faróis piscam, [p=0.2] um a cada "
        "doze segundos [p=0.2] e outro a cada dezoito. [p=0.3] Eles piscaram juntos agora. [p=0.3] Quantas vezes vão piscar "
        "juntos nos próximos três minutos, [p=0.2] sem contar o agora? [p=0.4] {A}A: cinco. [p=0.3] {B}B: seis. [p=0.3] "
        "{C}C: dez. [p=0.3] {D}D: trinta. [p=0.3] {E}E: trinta e seis. [p=0.4] {p}Pause e tente! [p=2.0]"),
    dict(id="19", block="q3", text=
        "{d}Repete ou reparte? [p=0.3] Piscam e voltam a coincidir: [p=0.2] *repete,* MMC. [p=0.4] {s}No varal, [p=0.2] "
        "doze e dezoito: [p=0.2] por dois, [p=0.2] por dois, [p=0.2] por três, [p=0.2] por três. [p=0.3] {m}Todos os primos: "
        "[p=0.2] dois vezes dois vezes três vezes três, [p=0.2] trinta e seis segundos. [p=0.3] {g}A régua confere: [p=0.2] "
        "trinta e seis é maior que dezoito. [p=0.4] {u}Três minutos são cento e oitenta segundos. [p=0.2] Cento e oitenta "
        "dividido por trinta e seis: [p=0.2] cinco. [p=0.2] {ok}*Letra A!* [p=0.4] {xe}O trinta e seis parou no MMC. [p=0.3] "
        "{xb}O seis é o MDC: [p=0.2] o dois e o três que dividiram os dois juntos no varal. [p=0.3] {xd}E o trinta dividiu "
        "pelo MDC: [p=0.2] método trocado. [p=0.3] {xc}O dez usou um farol só."),

    # ================= QUESTÃO 4: MDC E QUANTIDADE (ESTACAS) =================
    dict(id="20", block="q4", text=
        "{r}Lembrando: [p=0.2] o MDC é a maior régua. [p=0.4] {a}Questão quatro. [p=0.2] Um terreno retangular de trinta por "
        "quarenta e oito metros vai ser cercado [p=0.2] com estacas igualmente espaçadas, [p=0.2] à maior distância possível, "
        "[p=0.2] com uma estaca em cada canto. [p=0.3] Quantas estacas serão usadas? [p=0.4] {A}A: seis. [p=0.3] {B}B: treze. "
        "[p=0.3] {C}C: vinte e seis. [p=0.3] {D}D: vinte e sete. [p=0.3] {E}E: duzentas e quarenta. [p=0.4] "
        "{p}Pause e tente! [p=2.0]"),
    dict(id="21", block="q4", text=
        "{d}Repete ou reparte? [p=0.3] Os lados são repartidos em espaços iguais: [p=0.2] *reparte,* MDC. [p=0.4] {s}No "
        "varal, [p=0.2] trinta e quarenta e oito: [p=0.2] o dois e o três dividiram os dois juntos. [p=0.3] {m}MDC: "
        "[p=0.2] dois vezes três, [p=0.2] seis metros. [p=0.3] {g}A régua confere: [p=0.2] seis é menor que trinta. [p=0.4] "
        "{pe}E o perímetro? [p=0.2] É a volta inteira: [p=0.2] a soma de todos os lados. [p=0.3] No retângulo, [p=0.2] dois "
        "lados de trinta e dois de quarenta e oito: [p=0.3] {u}duas vezes, [p=0.2] trinta mais quarenta e oito, [p=0.2] cento "
        "e cinquenta e seis metros. [p=0.3] {v}Dividido por seis: [p=0.2] vinte e seis. [p=0.3] Na figura fechada, [p=0.2] "
        "estacas e espaços são iguais. [p=0.2] {ok}*Letra C!* [p=0.4] {xa}O seis parou no MDC. [p=0.3] {xb}O treze não dobrou "
        "o perímetro. [p=0.3] {xd}O vinte e sete somou uma estaca a mais. [p=0.3] {xe}E o duzentos e quarenta usou o MMC: "
        "[p=0.2] todos os primos do varal."),

    # ================= QUESTÃO 5: DECISÃO DISFARÇADA =================
    dict(id="22", block="q5", text=
        "{r}Lembrando: [p=0.2] na dúvida, [p=0.2] repete ou reparte? [p=0.4] {a}Questão cinco. [p=0.2] Uma loja vende copos em "
        "caixas de oito [p=0.2] e pratos em caixas de doze. [p=0.3] Uma pessoa quer comprar a *mesma quantidade* de copos e "
        "de pratos, [p=0.2] só com caixas fechadas, [p=0.2] sem sobrar nenhum. [p=0.3] Qual é a menor quantidade de cada? "
        "[p=0.4] {A}A: três. [p=0.3] {B}B: quatro. [p=0.3] {C}C: vinte. [p=0.3] {D}D: vinte e quatro. [p=0.3] {E}E: noventa e "
        "seis. [p=0.4] {p}Pause e tente! [p=2.0]"),
    dict(id="23", block="q5", text=
        "{d}Sem sobrar parece MDC. [p=0.3] Mas repare: [p=0.2] ninguém está cortando nada. [p=0.3] As caixas vão se *repetindo:* "
        "[p=0.2] oito, dezesseis, vinte e quatro; [p=0.2] doze, vinte e quatro. [p=0.3] {s}*Repete,* MMC. [p=0.3] {v}No varal, "
        "[p=0.2] oito e doze: [p=0.2] por dois, [p=0.2] por dois, [p=0.2] por dois, [p=0.2] por três. [p=0.3] {m}Todos os "
        "primos: [p=0.2] vinte e quatro. [p=0.2] {ok}*Letra D!* [p=0.4] {xb}O quatro é o MDC: [p=0.2] os dois primeiros dois, "
        "[p=0.2] que dividiram os dois juntos. [p=0.2] A régua denuncia: [p=0.2] quatro é menor que doze. [p=0.3] {xa}O três é "
        "o número de caixas de copos. [p=0.3] {xc}O vinte somou. [p=0.3] {xe}E o noventa e seis multiplicou: [p=0.2] é comum, "
        "[p=0.2] mas não é o menor."),

    # ================= CHECKLIST DE DOMÍNIO =================
    dict(id="24", block="dominio", text=
        "{t}Para fechar, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria explicar em voz alta "
        "para outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}O que não marcou, [p=0.2] reveja o episódio "
        "correspondente."),
    dict(id="25", block="dominio", text=
        "{e1}Episódio um: [p=0.2] múltiplo e divisor, [p=0.2] e os critérios do dois, três, quatro, cinco, seis, nove e dez. "
        "[p=0.4] {e2}Episódio dois: [p=0.2] o um e o dois, [p=0.2] os vinte e cinco primos até cem, [p=0.2] e o teste pela "
        "raiz. [p=0.4] {e3}Episódio três: [p=0.2] fatorar, [p=0.2] e contar divisores somando um em cada expoente."),
    dict(id="26", block="dominio", text=
        "{e4}Episódio quatro: [p=0.2] o MMC por fatoração e por decomposição simultânea, [p=0.2] o varal, [p=0.2] e o último "
        "passo do quantas vezes. [p=0.4] {e5}Episódio cinco: [p=0.2] o MDC por fatoração e por Euclides, [p=0.2] e no mesmo "
        "varal, [p=0.2] com os primos que dividiram todos. [p=0.4] {e6}Episódio seis: [p=0.2] decidir entre MMC e MDC, "
        "[p=0.2] a régua, [p=0.2] e o MDC vezes MMC só para dois números."),
    dict(id="27", block="meta", text=
        "{t}E a meta [p=0.2] antes de considerar o assunto dominado: [p=0.3] {a}resolva *trinta questões* [p=0.2] {b}e acerte "
        "pelo menos *vinte e uma,* [p=0.2] setenta por cento. [p=0.4] {c}Priorize as de MMC e MDC contextualizadas: [p=0.2] "
        "são as que caem."),

    # ================= PONTE E CTA =================
    dict(id="28", block="ponte", text=
        "{a}O próximo assunto é *Frações, decimais e dízimas.* [p=0.4] {b}E o MMC que você aprendeu aqui [p=0.2] {c}vai ser "
        "usado para *somar frações.*"),
    dict(id="29", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantas das nove você acertou no verdadeiro ou falso? "
        "[p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
