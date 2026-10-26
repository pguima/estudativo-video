# Roteiro — Divisão Proporcional, Episódio 2 de 5: Divisão inversa, inverter o valor, não a ordem
# Base: Estudos/Enem/estudos/01-matematica/08-divisao-proporcional.html — seção 05 (+ Questões 2 e 8 da seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   Inverter é virar a FRAÇÃO de cabeça para baixo (2 vira 1/2), não virar a FILA de trás para frente (2, 3, 4 não vira 4, 3, 2).
#   O MMC tira as frações do caminho: multiplicar todos os pesos pelo mesmo número não muda a divisão, só deixa os
#   pacotinhos inteiros (os pacotinhos do episódio 1).
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte.
# Exemplo do bloco c) = a própria Questão 2 (R$ 2 600 inversamente a 2, 3 e 4), por desenho do usuário: a Q2 é o "eu faço"
#   e entra como a versão oficial (enunciado do material, resolução curta, conferências e alternativas).
#   Nenhum bloco usa os números da Questão 8 (2, 3, 6 e R$ 4 200), que é o "você faz".
# Partes quebradas da armadilha (pesos 4, 3, 2): 2 600 ÷ 9 = 288,88…; partes ≈ 1 155,56 · 866,67 · 577,78 (valores CERTOS;
#   o material escreve 1 155 e 866, truncados, que somam 2 599 — ver PLANO_DA_SERIE.md).
# Nós fazemos (prompt): inversamente a 3, 4 e 6 → inversos 1/3, 1/4, 1/6 → MMC 12 → pesos 4, 3, 2 (NÃO é 6, 4, 3, a fila virada).
# QUESTÃO 2 do material (texto idêntico na tela): pesos 6, 4, 3 → soma 13 → k = 200 → 1 200 · 800 · 600 → maior = 1 200 → D.
#   O material não explica as erradas; explicações NOSSAS: A (600) = a MENOR parte (respondeu a parte errada);
#   B (800) = a parte do meio; E (1 300) = metade do total, como se o de número 2 levasse "a metade";
#   C (1 100) não sai de nenhuma conta certa (quem vira a fila chega a ≈ 1 155,56, número quebrado, que nem está nas alternativas).
# QUESTÃO 8 do material: inversos 1/2, 1/3, 1/6 → MMC 6 → pesos 3, 2, 1 → soma 6 → k = 700 → 2 100 · 1 400 · 700 →
#   funcionário com 3 faltas = 1 400 → C. Material: conferência de sentido (2 faltas leva 2 100; 6 faltas leva 700).
#   Explicações NOSSAS: A (700) = a parte de quem teve 6 faltas; E (2 100) = a parte de quem teve 2 faltas (as duas respondem
#   a parte errada); B (1 050) e D (1 800) não saem de nenhuma conta certa e não fecham a soma com as outras partes.
# Atalhos (verde): "peso = MMC ÷ número" (12 ÷ 2 = 6, 12 ÷ 3 = 4, 12 ÷ 4 = 3) · "número quebrado = sinal de caminho errado" ·
#   "duas conferências: a soma fecha? o menor número levou a maior parte?".
# Frases-chave (meio e fim, idênticas): 1. Inversa: troque cada número pelo seu inverso.
#   2. Multiplique pelo MMC e as frações somem. 3. Inverter o valor, não a ordem.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Divisão inversamente proporcional: inverta o valor, não a ordem | Divisão Proporcional Ep. 2"
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
    "MMC": "M M C",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Dividir *inversamente* a dois, três e quatro. [p=0.4] {b}Muita gente usa os pesos *quatro, três e dois:* [p=0.3] "
        "parece óbvio [p=0.2] {c}e está *errado.* [p=0.4] {d}As partes saem com *números quebrados,* [p=0.3] {e}e esse já é o "
        "*sinal do erro.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai fazer qualquer divisão inversa [p=0.2] *sem frações* [p=0.3] {b}e sem cair "
        "na armadilha da *ordem invertida.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] some os pesos, [p=0.2] divida o total, [p=0.2] "
        "e cada *pacotinho* vale k. [p=0.4] {b}Da série de Frações: [p=0.2] o *inverso* de um número [p=0.2] é ele virado de "
        "cabeça para baixo. [p=0.2] O inverso de dois é *um meio.* [p=0.4] {c}E da série de Divisibilidade: [p=0.2] o *MMC* "
        "é o menor número que todos dividem certinho. [p=0.2] O MMC de dois, três e quatro é *doze.*"),

    # ================= CONCRETO: MENOS É MAIS =================
    dict(id="04", block="menos", text=
        "{t}Pense num *bônus* de fim de ano. [p=0.3] {a}Ana faltou *duas* vezes, [p=0.2] Bruno *três,* [p=0.2] Caio "
        "*quatro.* [p=0.4] {b}Quem merece mais? [p=0.3] {c}A Ana, [p=0.2] que faltou *menos.* [p=0.4] {d}Aqui, [p=0.2] menos "
        "é mais: [p=0.2] o *menor* número leva a *maior* parte. [p=0.4] {e}O mesmo vale para um prêmio por menos erros, "
        "[p=0.2] ou um rateio para quem usou menos tempo."),
    dict(id="05", block="menos", text=
        "{t}Isso tem nome: [p=0.2] divisão *inversamente proporcional.* [p=0.4] {a}Quanto *maior* o número de alguém, "
        "[p=0.2] {b}*menor* a parte que ele recebe. [p=0.4] {c}E agora a pergunta que vale a aula: [p=0.2] *quais são os "
        "pesos?*"),

    # ================= BLOCO A: A REGRA =================
    dict(id="06", block="regra", text=
        "{t}A regra é uma só. [p=0.3] {a}Dividir *inversamente* a dois, três e quatro [p=0.3] {b}é dividir *diretamente* aos "
        "*inversos:* [p=0.3] {c}*um meio, um terço e um quarto.* [p=0.4] {d}Cada número vira de cabeça para baixo. [p=0.3] "
        "Inverter é virar a *fração,* [p=0.2] não a fila."),
    dict(id="07", block="regra", text=
        "{t}E por que funciona? [p=0.3] {a}Compare os inversos. [p=0.3] Um meio é *metade* de uma pizza. [p=0.2] Um quarto, "
        "[p=0.2] só *um quarto.* [p=0.4] {b}O menor número, [p=0.2] o dois, [p=0.2] virou o *maior* pedaço. [p=0.4] {c}Virar de "
        "cabeça para baixo [p=0.2] já coloca quem faltou menos [p=0.2] *na frente.*"),

    # ================= BLOCO B: O ATALHO DO MMC =================
    dict(id="08", block="mmc", text=
        "{t}Só que pesos em fração [p=0.2] dão trabalho. [p=0.4] {a}Lembra dos pacotinhos? [p=0.2] Multiplicar *todos* os pesos "
        "pelo *mesmo número* [p=0.2] não muda a divisão: [p=0.3] {b}só deixa os pacotinhos *inteiros.* [p=0.4] {c}E o número "
        "certo é o *MMC* dos de baixo. [p=0.2] Dois, três e quatro: [p=0.2] *doze.*"),
    dict(id="09", block="mmc", text=
        "{a}Um meio vezes doze: [p=0.2] *seis.* [p=0.3] {b}Um terço vezes doze: [p=0.2] *quatro.* [p=0.3] {c}Um quarto vezes "
        "doze: [p=0.2] *três.* [p=0.4] {d}Pesos *seis, quatro e três.* [p=0.2] Inteiros, [p=0.2] sem nenhuma fração. [p=0.4] "
        "{e}Atalho: [p=0.2] *o peso é o MMC dividido pelo número.* [p=0.3] Doze dividido por dois, [p=0.2] seis. [p=0.2] Por "
        "três, [p=0.2] quatro. [p=0.2] Por quatro, [p=0.2] três."),

    # ================= BLOCO C: DAÍ EM DIANTE, DIRETA =================
    dict(id="10", block="direta", text=
        "{t}Daí em diante, [p=0.2] é a divisão *direta* do episódio um. [p=0.4] {a}O bônus é de *dois mil e seiscentos reais.* "
        "[p=0.4] {b}Some os pesos: [p=0.2] seis mais quatro mais três, [p=0.2] *treze* pacotinhos. [p=0.4] {c}Divida o total: "
        "[p=0.2] dois mil e seiscentos dividido por treze, [p=0.2] *duzentos.* [p=0.2] Esse é o k. [p=0.4] {d}Ana: [p=0.2] seis "
        "vezes duzentos, [p=0.2] *mil e duzentos.* [p=0.3] Bruno: [p=0.2] *oitocentos.* [p=0.3] Caio: [p=0.2] *seiscentos.*"),

    # ================= BLOCO E: AS DUAS CONFERÊNCIAS =================
    dict(id="11", block="confere", text=
        "{t}E agora, [p=0.2] as *duas conferências.* [p=0.4] {a}Primeira: [p=0.2] a soma dá o total? [p=0.3] Mil e duzentos, "
        "[p=0.2] mais oitocentos, [p=0.2] mais seiscentos: [p=0.2] *dois mil e seiscentos.* [p=0.2] Fecha! [p=0.4] {b}Segunda: "
        "[p=0.2] o *menor número* recebeu a *maior parte?* [p=0.3] A Ana, [p=0.2] com duas faltas, [p=0.2] levou mil e "
        "duzentos. [p=0.2] *Sim!* [p=0.4] {c}Passou nas duas, [p=0.2] pode marcar."),

    # ================= BLOCO D: A ARMADILHA DA FILA =================
    dict(id="12", block="armadilha", text=
        "{t}E se você tivesse *virado a fila?* [p=0.3] {a}Pesos *quatro, três e dois.* [p=0.4] {b}Soma, [p=0.2] *nove.* [p=0.3] "
        "{c}Dois mil e seiscentos dividido por nove: [p=0.2] *duzentos e oitenta e oito vírgula oito, oito, oito...* [p=0.3] "
        "não acaba. [p=0.4] {d}As partes saem mais ou menos *mil cento e cinquenta e cinco e cinquenta e seis,* [p=0.2] "
        "*oitocentos e sessenta e seis e sessenta e sete,* [p=0.2] *quinhentos e setenta e sete e setenta e oito.*"),
    dict(id="13", block="armadilha", text=
        "{t}Repare no que aconteceu. [p=0.3] {a}A fila virada até acerta *quem* recebe mais. [p=0.4] {b}Mas erra *quanto.* "
        "[p=0.3] Um meio dividido por um terço dá *uma vez e meia:* [p=0.2] a Ana tem que receber uma vez e meia o Bruno. "
        "[p=0.4] {c}Com quatro e três, [p=0.2] ela recebe só *uma vez e um terço.* [p=0.2] A conta ficou torta. [p=0.4] "
        "{d}Atalho: [p=0.2] *número quebrado é sinal de caminho errado.* [p=0.3] Pare e confira os pesos."),

    # ================= NÓS FAZEMOS =================
    dict(id="14", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Quais são os *pesos* [p=0.2] para dividir inversamente a *três, quatro e seis?* [p=0.4] {b}Só os "
        "pesos, [p=0.2] sem o dinheiro. [p=0.3] {c}*Pause o vídeo e calcule.* [p=2.0]"),
    dict(id="15", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Os inversos: [p=0.2] *um terço, um quarto e um sexto.* [p=0.4] {b}O MMC de três, quatro "
        "e seis: [p=0.2] *doze.* [p=0.4] {c}Doze dividido por três, [p=0.2] *quatro.* [p=0.2] Por quatro, [p=0.2] *três.* "
        "[p=0.2] Por seis, [p=0.2] *dois.* [p=0.3] Pesos *quatro, três e dois.* [p=0.4] {d}E repare: [p=0.2] *não* é seis, "
        "quatro e três, [p=0.2] que seria a fila virada."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="16", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] inversa, [p=0.2] troque cada número pelo seu inverso. [p=0.5] "
        "{b}Dois: [p=0.2] multiplique pelo MMC e as frações somem. [p=0.5] {c}Três: [p=0.2] inverter o valor, [p=0.2] não a "
        "ordem."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="17", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] usar os *próprios números* como pesos: [p=0.2] dois, "
        "três e quatro. [p=0.4] {b}Parece certo, [p=0.2] porque é assim na divisão direta. [p=0.4] {c}Mas aí quem faltou mais "
        "ganha mais. [p=0.3] Na inversa, [p=0.2] use os *inversos.*"),
    dict(id="18", block="erros", text=
        "{a}Segundo: [p=0.2] inverter a *ordem* em vez dos valores. [p=0.4] {b}Parece certo, [p=0.2] porque a palavra é "
        "inversa, [p=0.2] e a fila de trás para frente parece inversa. [p=0.4] {c}Mas inverter é virar cada número de cabeça "
        "para baixo. [p=0.3] Dois, três e quatro viram *seis, quatro e três.*"),
    dict(id="19", block="erros", text=
        "{a}Terceiro: [p=0.2] esquecer de conferir se o *menor número* levou a *maior parte.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque a soma fechou. [p=0.4] {c}Mas a soma fecha até com os pesos errados. [p=0.3] Só a segunda conferência "
        "pega a troca."),

    # ================= QUESTÃO 2 DO MATERIAL (EU FAÇO) =================
    dict(id="20", block="q2", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.3] Essa eu faço com você. "
        "[p=0.4] {a}Uma quantia de *dois mil e seiscentos reais* será repartida entre três funcionários [p=0.2] em partes "
        "*inversamente proporcionais* aos números dois, três e quatro. [p=0.4] {b}A *maior parte* corresponde a: [p=0.4] "
        "{qa}A: [p=0.2] seiscentos reais. [p=0.3] {qb}B: [p=0.2] oitocentos. [p=0.3] {qc}C: [p=0.2] mil e cem. [p=0.3] "
        "{qd}D: [p=0.2] mil e duzentos. [p=0.3] {qe}E: [p=0.2] mil e trezentos."),
    dict(id="21", block="q2", text=
        "{t}É o nosso bônus! [p=0.3] {a}Inversos: [p=0.2] um meio, um terço, um quarto. [p=0.3] O MMC é doze: [p=0.2] pesos "
        "*seis, quatro e três.* [p=0.4] {b}Soma treze, [p=0.2] k igual a *duzentos.* [p=0.4] {c}Partes: [p=0.2] mil e duzentos, "
        "[p=0.2] oitocentos [p=0.2] e seiscentos. [p=0.4] {d}A soma fecha, [p=0.2] e o menor número levou a maior parte. "
        "[p=0.3] {ok}*Letra D!* [p=0.2] Mil e duzentos."),
    dict(id="22", block="q2", text=
        "{t}E as outras? [p=0.3] {xa}A A é a *menor* parte: [p=0.2] calculou certo [p=0.2] e respondeu a parte errada. [p=0.4] "
        "{xb}A B é a parte do *meio.* [p=0.4] {xe}A E é a *metade* do total, [p=0.2] como se o dois mandasse dividir por dois. "
        "[p=0.4] {xc}E a C não sai de nenhuma conta certa."),

    # ================= QUESTÃO 8 DO MATERIAL (VOCÊ FAZ) =================
    dict(id="23", block="q8", text=
        "{t}Agora é com você. [p=0.3] {a}Uma empresa distribuirá um bônus de *quatro mil e duzentos reais* entre três "
        "funcionários, [p=0.2] em partes *inversamente proporcionais* ao número de faltas de cada um no semestre: [p=0.2] "
        "*duas, três e seis* faltas. [p=0.4] {b}O funcionário com *três faltas* receberá: [p=0.4] {qa}A: [p=0.2] setecentos "
        "reais. [p=0.3] {qb}B: [p=0.2] mil e cinquenta. [p=0.3] {qc}C: [p=0.2] mil e quatrocentos. [p=0.3] {qd}D: [p=0.2] mil "
        "e oitocentos. [p=0.3] {qe}E: [p=0.2] dois mil e cem. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="24", block="q8", text=
        "{t}Vamos resolver. [p=0.3] {a}Inversos: [p=0.2] um meio, um terço e um sexto. [p=0.3] O MMC de dois, três e seis é "
        "*seis.* [p=0.4] {b}Seis dividido por dois, [p=0.2] *três.* [p=0.2] Por três, [p=0.2] *dois.* [p=0.2] Por seis, "
        "[p=0.2] *um.* [p=0.4] {c}Soma seis, [p=0.2] k igual a quatro mil e duzentos dividido por seis: [p=0.2] *setecentos.* "
        "[p=0.4] {d}Quem teve três faltas tem peso dois: [p=0.2] dois vezes setecentos, [p=0.2] *mil e quatrocentos.* [p=0.3] "
        "{ok}*Letra C!*"),
    dict(id="25", block="q8", text=
        "{t}As duas conferências. [p=0.3] {a}Partes: [p=0.2] dois mil e cem, [p=0.2] mil e quatrocentos, [p=0.2] setecentos. "
        "[p=0.2] Somam *quatro mil e duzentos.* [p=0.2] Fecha! [p=0.4] {b}Quem faltou menos levou mais. [p=0.2] *Certo!* "
        "[p=0.4] {xa}A A é a parte de quem faltou seis vezes, [p=0.2] {xe}e a E, [p=0.2] de quem faltou duas: [p=0.2] partes "
        "erradas. [p=0.4] {xb}A B [p=0.2] {xd}e a D não saem de nenhuma conta certa."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="26", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] inversa, [p=0.2] troque cada número pelo seu inverso. "
        "[p=0.5] {b}Dois: [p=0.2] multiplique pelo MMC e as frações somem. [p=0.5] {c}Três: [p=0.2] inverter o valor, [p=0.2] "
        "não a ordem."),

    # ================= PONTE E CTA =================
    dict(id="27", block="ponte", text=
        "{a}E quando a divisão depende de *dois critérios* ao mesmo tempo, [p=0.2] como pessoas e dias trabalhados? [p=0.4] "
        "{b}O instinto manda *somar,* [p=0.3] {c}e a resposta certa manda *multiplicar.* [p=0.4] {d}Próximo episódio."),
    dict(id="28", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha virado a fila em vez dos números? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
