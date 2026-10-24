# Roteiro — Notação Científica e Ordem de Grandeza, Episódio 3 de 6: Somar em notação científica (a que derruba) e comparar
# grandezas (aula para iniciantes).
# Base: Estudos/Enem/estudos/01-matematica/05-notacao-cientifica-ordem-grandeza.html — seções 05 e 08 (+ Questões 4 e 7 da seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   NOTAS DE VALORES DIFERENTES: 10⁵ e 10⁴ são notas diferentes; antes de somar, troque tudo pela MESMA nota
#     (8 notas de R$ 10 = 0,8 de uma nota de R$ 100).
#   QUANTAS LUAS CABEM NA TERRA: "quantas vezes maior" = divisão; "quanto maior" = quanto sobra = subtração.
#   (do ep2) a GANGORRA: coeficiente ÷ 10, expoente + 1 → mesmo valor (8 · 10⁴ = 0,8 · 10⁵).
# Gancho: 3 · 10⁵ + 8 · 10⁴ = 3,8 · 10⁵ (não 11 · 10⁹ nem 11 · 10⁵).
# Exemplo do material: 3 · 10⁵ + 8 · 10⁴ + 2 · 10⁴ = 3 · 10⁵ + 0,8 · 10⁵ + 0,2 · 10⁵ = 4 · 10⁵.
# Nós fazemos: 5 · 10³ + 2 · 10² = 5 · 10³ + 0,2 · 10³ = 5,2 · 10³ (confere: 5 000 + 200 = 5 200).
# Comparar (exemplos NOSSOS, para não entregar a Q7 antes da hora): 6 · 10⁵ ÷ 2 · 10³ = 3 · 10² = 300 vezes;
#   6 · 10⁵ − 2 · 10³ = 6 · 10⁵ − 0,02 · 10⁵ = 5,98 · 10⁵. Erro 4 (nosso): 8 · 10⁹ ÷ 2 · 10⁶ = 4 · 10³ = 4 000 vezes, não "3 vezes".
# QUESTÃO 4 do material (texto idêntico na tela): 4 · 10⁵ → C.
#   Material: "A e E somaram os coeficientes sem igualar os expoentes; B e D somaram os expoentes".
#   Detalhe NOSSO: E (13 · 10⁵) somou 3 + 8 + 2 = 13 direto; A (1,3 · 10⁴) somou 13 e ainda andou a vírgula sem subir o
#   expoente (13 · 10⁴ seria 1,3 · 10⁵); D (4 · 10¹³) igualou certo mas somou os expoentes 5 + 4 + 4 = 13; B (1,3 · 10¹³)
#   cometeu os dois erros.
# QUESTÃO 7 do material (texto idêntico na tela): 6 · 10²⁴ ÷ 7,5 · 10²² = 0,8 · 10² = 80 → B.
#   Conferência por ordem de grandeza (material): expoentes diferem em 2 → perto de 100; coeficiente de cima menor → um
#   pouco abaixo de 100.
#   D (2 vezes): subtraiu os expoentes e parou (material). Explicações NOSSAS: E (100) olhou só os expoentes e ignorou os
#   coeficientes; A (8) usou 10¹ no lugar de 10²; C (800) fez 6 ÷ 7,5 = 8, perdendo a vírgula do 0,8.
# Frases-chave (meio e fim, idênticas):
#   1. Para somar, primeiro o mesmo expoente.
#   2. Iguale sempre pelo maior expoente.
#   3. "Quantas vezes" divide; "quanto" subtrai.
# Atalhos (verde): "a diferença dos expoentes diz quantas casas a vírgula anda" · "converta o menor para o maior: o
#   coeficiente fica menor que 1" · "confira com o número por extenso" · "a pergunta é em VEZES ou na UNIDADE?".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "3 · 10⁵ + 8 · 10⁴ NÃO é 11 · 10⁵: somar em notação científica · Matemática ENEM, Notação Científica ep. 3"

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
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Três vezes dez elevado a cinco, [p=0.2] *mais* oito vezes dez elevado a quatro. [p=0.5] {b}Metade das pessoas "
        "responde *onze vezes dez elevado a nove.* [p=0.4] {c}A outra metade, [p=0.2] *onze vezes dez elevado a cinco.* "
        "[p=0.5] {d}As duas *erraram.* [p=0.4] {e}É aqui que se separa quem *estudou* [p=0.2] de quem *decorou.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai *somar* números em notação científica sem errar, [p=0.4] {b}e vai saber "
        "quando *dividir* [p=0.2] e quando *subtrair* [p=0.2] numa comparação."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes do episódio passado. [p=0.3] {a}A *gangorra:* [p=0.2] se o número da frente fica dez "
        "vezes *menor,* [p=0.2] o expoente *sobe* um, [p=0.2] e o valor não muda. [p=0.3] {b}Oito vezes dez elevado a "
        "quatro [p=0.2] é o mesmo que zero vírgula oito vezes dez elevado a cinco. [p=0.4] {c}E para *dividir:* [p=0.2] "
        "divide os números da frente [p=0.2] e *subtrai* os expoentes."),

    # ================= BLOCO B (concreto): AS NOTAS DE VALORES DIFERENTES =================
    dict(id="04", block="notas", text=
        "{t}Começando pelo dinheiro. [p=0.3] {a}Você tem *três* notas de cem reais. [p=0.3] {b}E ganha *oito* notas de dez. "
        "[p=0.4] {c}Agora você tem *onze notas de cem?* [p=0.5] {d}Claro que não! [p=0.3] {e}Você tem trezentos [p=0.2] "
        "mais oitenta: [p=0.2] *trezentos e oitenta reais.*"),
    dict(id="05", block="notas", text=
        "{t}Com medidas é igual. [p=0.3] {a}Dois metros mais cinquenta centímetros [p=0.2] não dão *cinquenta e dois "
        "metros.* [p=0.4] {b}Primeiro converte: [p=0.2] {c}*dois metros e meio.*"),
    dict(id="06", block="notas", text=
        "{t}E na notação científica? [p=0.3] {a}Dez elevado a cinco é *cem mil.* [p=0.3] {b}Dez elevado a quatro é *dez mil.* "
        "[p=0.4] {c}São *notas de valores diferentes.*"),

    # ================= BLOCO A: A CONDIÇÃO =================
    dict(id="07", block="condicao", text=
        "{t}Então, a regra. [p=0.3] {a}Para *somar* ou *subtrair* em notação científica, [p=0.2] os números precisam ter "
        "o *mesmo expoente.* [p=0.5] {b}Se não tiverem, [p=0.2] você *iguala os expoentes* primeiro. [p=0.4] {c}Igualar os "
        "expoentes é reescrever um dos números [p=0.2] para ele ficar com o mesmo expoente do outro, [p=0.2] *sem mudar o "
        "valor.* [p=0.4] {d}É trocar tudo pela *mesma nota.*"),

    # ================= BLOCO C: COMO IGUALAR =================
    dict(id="08", block="igualar", text=
        "{t}Como trocar as oito notas de dez mil? [p=0.4] {a}Pense no dinheiro: [p=0.2] oito notas de dez reais [p=0.2] "
        "são oitenta reais, [p=0.2] ou seja, [p=0.2] *zero vírgula oito* de uma nota de cem. [p=0.5] {b}Na notação, [p=0.2] "
        "é a gangorra: [p=0.2] o oito fica dez vezes menor, [p=0.2] *zero vírgula oito,* [p=0.3] {c}e o expoente sobe de "
        "quatro para *cinco.* [p=0.4] {d}Oito vezes dez elevado a quatro [p=0.2] vira zero vírgula oito vezes dez elevado "
        "a cinco."),
    dict(id="09", block="igualar", text=
        "{t}Agora, o exemplo completo do material. [p=0.3] {a}Três vezes dez elevado a cinco, [p=0.2] mais oito vezes dez "
        "elevado a quatro, [p=0.2] mais dois vezes dez elevado a quatro. [p=0.4] {b}O oito vira *zero vírgula oito,* "
        "[p=0.2] {c}e o dois vira *zero vírgula dois,* [p=0.2] os dois com dez elevado a cinco. [p=0.4] {d}Agora sim, "
        "mesma nota: [p=0.2] três, [p=0.2] mais zero vírgula oito, [p=0.2] mais zero vírgula dois: [p=0.2] *quatro.* "
        "[p=0.4] {e}Resposta: [p=0.2] *quatro vezes dez elevado a cinco.*"),
    dict(id="10", block="igualar", text=
        "{t}E o gancho do começo? [p=0.3] {a}Três vezes dez elevado a cinco, [p=0.2] mais zero vírgula oito vezes dez "
        "elevado a cinco: [p=0.3] {b}*três vírgula oito vezes dez elevado a cinco.* [p=0.4] {c}Por extenso: [p=0.2] "
        "trezentos mil mais oitenta mil, [p=0.2] *trezentos e oitenta mil.*"),
    dict(id="11", block="igualar", text=
        "{t}Um atalho para não se perder. [p=0.3] {a}*A diferença dos expoentes [p=0.2] diz quantas casas a vírgula "
        "anda.* [p=0.4] {b}De dez elevado a quatro para dez elevado a cinco: [p=0.2] diferença de *um,* [p=0.2] a vírgula "
        "anda uma casa para a esquerda. [p=0.3] {c}Oito vira *zero vírgula oito.*"),

    # ================= BLOCO D: A REGRA DE BOLSO =================
    dict(id="12", block="bolso", text=
        "{t}Por que subir o *menor,* [p=0.2] e não descer o maior? [p=0.4] {a}Descer também dá certo, [p=0.2] mas o três vira "
        "*trinta,* [p=0.2] trinta mais oito dá *trinta e oito,* [p=0.3] {b}e você precisa de mais uma gangorra no final. "
        "[p=0.4] {c}Por isso, a regra de bolso: [p=0.2] *iguale sempre pelo maior expoente.* [p=0.4] {d}Os números convertidos "
        "ficam *menores que um,* [p=0.2] fáceis de somar de cabeça, [p=0.2] e o resultado já sai na forma certa."),

    # ================= NÓS FAZEMOS =================
    dict(id="13", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Cinco vezes dez elevado a três, [p=0.2] *mais* dois vezes dez elevado a dois. [p=0.4] "
        "{b}*Pause o vídeo e calcule.* [p=2.0]"),
    dict(id="14", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}O maior expoente é *três.* [p=0.3] {b}O dois vezes dez elevado a dois [p=0.2] vira "
        "*zero vírgula dois* vezes dez elevado a três. [p=0.4] {c}Cinco mais zero vírgula dois: [p=0.2] *cinco vírgula "
        "dois vezes dez elevado a três.* [p=0.4] {d}Confira por extenso: [p=0.2] cinco mil mais duzentos, [p=0.2] *cinco "
        "mil e duzentos.* [p=0.2] Bateu!"),

    # ================= BLOCO E: QUANTAS VEZES MAIOR =================
    dict(id="15", block="vezes", text=
        "{t}Agora, outra coisa que a prova adora: [p=0.2] *comparar.* [p=0.4] {a}Comparar duas grandezas, "
        "[p=0.2] e grandeza é qualquer coisa que dá para medir: [p=0.2] massa, [p=0.2] distância, [p=0.2] dinheiro. "
        "[p=0.5] {b}Pense em quantas *Luas* cabem dentro da Terra. [p=0.4] {c}Essa pergunta não é *quanto sobra.* "
        "[p=0.2] {d}É *quantas vezes* uma cabe na outra: [p=0.2] uma *divisão.*"),
    dict(id="16", block="vezes", text=
        "{t}Um exemplo. [p=0.3] {a}Uma empresa fatura seis vezes dez elevado a cinco reais. [p=0.2] {b}Outra, [p=0.2] dois "
        "vezes dez elevado a três. [p=0.4] {c}Quantas vezes a primeira é maior? [p=0.4] {d}Divide os números da frente: "
        "[p=0.2] seis dividido por dois, [p=0.2] *três.* [p=0.3] {e}Subtrai os expoentes: [p=0.2] cinco menos três, "
        "[p=0.2] *dois.* [p=0.4] {f}Três vezes dez elevado a dois: [p=0.2] *trezentas vezes.* [p=0.4] {g}Esse resultado "
        "de uma divisão que compara se chama *razão.*"),

    # ================= BLOCO F: QUANTO MAIOR =================
    dict(id="17", block="quanto", text=
        "{t}E se a pergunta fosse *quanto* a primeira fatura a mais? [p=0.4] {a}Aí é a *diferença:* [p=0.2] o resultado "
        "de uma *subtração,* [p=0.2] na mesma unidade, [p=0.2] em reais. [p=0.4] {b}E a subtração, "
        "[p=0.2] como a soma, [p=0.2] precisa *igualar os expoentes* antes. [p=0.4] {c}Dois vezes dez elevado a três [p=0.2] vira zero vírgula "
        "zero dois vezes dez elevado a cinco: [p=0.2] duas casas, [p=0.2] porque a diferença dos expoentes é dois. [p=0.4] "
        "{d}Seis menos zero vírgula zero dois: [p=0.2] *cinco vírgula nove oito vezes dez elevado a cinco reais.*"),
    dict(id="18", block="quanto", text=
        "{t}O atalho para não confundir: [p=0.3] {a}olhe a *resposta* que a pergunta quer. [p=0.4] {b}Se é em *vezes,* "
        "[p=0.2] divide. [p=0.3] {c}Se é na *unidade,* [p=0.2] em reais, [p=0.2] quilos, [p=0.2] metros, [p=0.2] subtrai."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] para somar, [p=0.2] primeiro o mesmo expoente. [p=0.5] "
        "{b}Dois: [p=0.2] iguale sempre pelo maior expoente. [p=0.5] {c}Três: [p=0.2] *quantas vezes* divide; [p=0.2] "
        "*quanto* subtrai."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] somar os números da frente sem igualar, "
        "[p=0.2] e escrever *treze vezes dez elevado a cinco.* [p=0.4] {b}Parece certo, [p=0.2] porque somar três, oito "
        "e dois [p=0.2] é uma conta normal. [p=0.4] {c}Mas são notas diferentes: [p=0.2] iguale primeiro, [p=0.2] e dá "
        "*quatro vezes dez elevado a cinco.*"),
    dict(id="21", block="erros", text=
        "{a}Segundo: [p=0.2] *somar os expoentes* numa soma. [p=0.4] {b}Parece certo, [p=0.2] porque na multiplicação "
        "a gente soma expoentes, [p=0.2] e a regra fica na cabeça. [p=0.4] {c}Mas somar expoentes *só vale no produto.* "
        "[p=0.2] Numa adição, [p=0.2] primeiro você iguala."),
    dict(id="22", block="erros", text=
        "{a}Terceiro: [p=0.2] responder *quantas vezes maior* com uma subtração. [p=0.4] {b}Parece certo, [p=0.2] porque "
        "a palavra *maior* lembra diferença. [p=0.4] {c}Mas *vezes* pede divisão: [p=0.2] quantas Luas cabem na Terra."),
    dict(id="23", block="erros", text=
        "{a}Quarto: [p=0.2] parar na diferença dos expoentes. [p=0.3] Oito vezes dez elevado a nove, [p=0.2] dividido "
        "por dois vezes dez elevado a seis: [p=0.2] *três vezes maior?* [p=0.4] {b}Parece certo, [p=0.2] porque nove menos "
        "seis dá três, [p=0.2] e o três estava na conta. [p=0.4] {c}Mas o três é o *expoente:* [p=0.2] quatro vezes dez "
        "elevado a três, [p=0.2] *quatro mil vezes.*"),

    # ================= QUESTÃO 4 DO MATERIAL =================
    dict(id="24", block="q4", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}Três municípios vizinhos "
        "têm, [p=0.2] respectivamente, [p=0.2] três vezes dez elevado a cinco, [p=0.2] oito vezes dez elevado a quatro "
        "[p=0.2] e dois vezes dez elevado a quatro habitantes. [p=0.3] A população total da região é: [p=0.4] {qa}A: [p=0.2] "
        "um vírgula três vezes dez elevado a quatro. [p=0.3] {qb}B: [p=0.2] um vírgula três vezes dez elevado a treze. "
        "[p=0.3] {qc}C: [p=0.2] quatro vezes dez elevado a cinco. [p=0.3] {qd}D: [p=0.2] quatro vezes dez elevado a treze. "
        "[p=0.3] {qe}E: [p=0.2] treze vezes dez elevado a cinco. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="25", block="q4", text=
        "{t}Vamos resolver. [p=0.3] {a}Soma pede o *mesmo expoente.* [p=0.3] O maior é cinco. [p=0.4] {b}Oito vezes dez "
        "elevado a quatro vira zero vírgula oito vezes dez elevado a cinco. [p=0.3] {c}Dois vezes dez elevado a quatro vira "
        "zero vírgula dois. [p=0.4] {d}Três, [p=0.2] mais zero vírgula oito, [p=0.2] mais zero vírgula dois: [p=0.2] "
        "*quatro vezes dez elevado a cinco.* [p=0.3] {e}São *quatrocentos mil* habitantes. [p=0.3] {ok}*Letra C!*"),
    dict(id="26", block="q4", text=
        "{t}E as outras? [p=0.3] {xe}A E somou três, oito e dois [p=0.2] sem igualar: [p=0.2] *treze.* [p=0.4] {xa}A A fez "
        "a mesma soma, [p=0.2] e ainda mexeu na vírgula sem mexer no expoente. [p=0.4] {xd}A D igualou certo, [p=0.2] mas "
        "*somou os expoentes:* [p=0.2] cinco mais quatro mais quatro, [p=0.2] treze. [p=0.4] {xb}E a B cometeu os dois "
        "erros de uma vez."),

    # ================= QUESTÃO 7 DO MATERIAL =================
    dict(id="27", block="q7", text=
        "{t}Mais uma do material, [p=0.2] agora de comparação. [p=0.4] {a}A massa da Terra é de aproximadamente seis vezes "
        "dez elevado a vinte e quatro quilos, [p=0.2] e a da Lua, [p=0.2] sete vírgula cinco vezes dez elevado a vinte e "
        "dois quilos. [p=0.3] A massa da Terra é maior que a da Lua em cerca de: [p=0.4] {qa}A: [p=0.2] oito vezes. [p=0.3] "
        "{qb}B: [p=0.2] oitenta vezes. [p=0.3] {qc}C: [p=0.2] oitocentas vezes. [p=0.3] {qd}D: [p=0.2] duas vezes. [p=0.3] "
        "{qe}E: [p=0.2] cem vezes. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="28", block="q7", text=
        "{t}A resposta vem em *vezes:* [p=0.2] é *divisão.* [p=0.4] {a}Os números da frente: [p=0.2] seis dividido por "
        "sete vírgula cinco. [p=0.3] Tire a vírgula dos dois: [p=0.2] sessenta dividido por setenta e cinco, [p=0.2] *zero "
        "vírgula oito.* [p=0.4] {b}Os expoentes: [p=0.2] vinte e quatro menos vinte e dois, [p=0.2] *dois.* [p=0.4] {c}Zero "
        "vírgula oito vezes dez elevado a dois: [p=0.2] zero vírgula oito vezes cem, [p=0.2] {d}*oitenta.* [p=0.4] {e}Cabem "
        "umas oitenta Luas na massa da Terra. [p=0.3] {ok}*Letra B!*"),
    dict(id="29", block="q7", text=
        "{t}E dá para conferir sem conta. [p=0.4] {a}Os expoentes diferem em *dois:* [p=0.2] isso sugere umas "
        "*cem vezes.* [p=0.4] {b}Mas o número de cima, [p=0.2] o seis, [p=0.2] é *menor* que o de baixo, [p=0.2] o sete "
        "vírgula cinco. [p=0.3] {c}Então o resultado fica *um pouco abaixo de cem.* [p=0.3] {d}Oitenta é coerente."),
    dict(id="30", block="q7", text=
        "{t}E as outras? [p=0.3] {xd}A D é o erro quatro: [p=0.2] subtraiu os expoentes [p=0.2] e *parou no dois.* [p=0.4] "
        "{xe}A E olhou só os expoentes [p=0.2] e esqueceu os números da frente. [p=0.4] {xc}A C perdeu a vírgula: [p=0.2] "
        "fez seis dividido por sete vírgula cinco igual a *oito.* [p=0.4] {xa}E a A multiplicou por dez, [p=0.2] em vez "
        "de cem."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="31", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] para somar, [p=0.2] primeiro o mesmo expoente. "
        "[p=0.5] {b}Dois: [p=0.2] iguale sempre pelo maior expoente. [p=0.5] {c}Três: [p=0.2] *quantas vezes* divide; "
        "[p=0.2] *quanto* subtrai."),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}Muitas vezes você nem precisa da conta exata: [p=0.2] basta saber a *escala.* [p=0.4] {b}Isso se chama *ordem "
        "de grandeza,* [p=0.3] {c}e o critério *não* é o expoente escrito. [p=0.4] {d}Próximo episódio."),
    dict(id="33", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você também somava os expoentes numa soma? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
