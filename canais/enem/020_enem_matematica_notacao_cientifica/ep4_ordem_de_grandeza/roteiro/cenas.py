# Roteiro — Notação Científica e Ordem de Grandeza, Episódio 4 de 6: Ordem de grandeza e a "conta de guardanapo"
# Base: Estudos/Enem/estudos/01-matematica/05-notacao-cientifica-ordem-grandeza.html — seções 06 e 10 (+ Questões 5 e 9 da seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   CASA DE POTÊNCIA DE 10: ordem de grandeza é a "casa" de potência de 10 mais próxima; não diz o valor, diz a ESCALA.
#   RÉGUA DE MULTIPLICAR: o meio do caminho entre 1 e 10, andando MULTIPLICANDO, é 3,16 (√10): 1 →×3,16→ 3,16 →×3,16→ 10.
#     Com 5 os passos ficam desiguais (×5 e depois ×2). "Perto" na escala é perto em VEZES, não em distância.
#   CONTA DE GUARDANAPO: arredonde cada fator para um algarismo significativo e acerte a escala.
# TROCAS DE EXEMPLO (para não entregar respostas):
#   - o gancho do prompt usava 720 000 = 7,2 · 10⁵, que é exatamente a Questão 5 → trocado por 850 000 = 8,5 · 10⁵ (mesma ideia);
#   - a tabela da seção 06 traz 7,2 · 10⁵ (Q5) e 9,8 · 10⁻⁴ (nós fazemos) → na tela: 2,3 · 10⁵, 8,5 · 10⁵, 5 · 10⁻⁸ e 1,1 · 10¹².
# Exemplos nossos: 400 000 (perto em vezes: 4 × 100 000, e 1 000 000 é só 2,5 × 400 000); cabelo × vírus (3 ordens ≈ 1000 vezes);
#   população mundial ≈ 8 · 10⁹ → ordem 10¹⁰ (8 ≥ 3,16). Valores das escalas: aproximados (tabela da seção 10).
# Nós fazemos: 2,9 · 10⁴ → 10⁴ · 3,5 · 10⁴ → 10⁵ · 9,8 · 10⁻⁴ → 10⁻³.
# Guardanapo (material): 4,7 · 10³ × 8,2 · 10⁵ ≈ 5 × 8 · 10⁸ = 40 · 10⁸ = 4 · 10⁹; exato 3,854 · 10⁹ (erro < 4%).
# QUESTÃO 5 do material (texto idêntico na tela): 7,2 · 10⁵ → 7,2 ≥ 3,16 → 10⁶ → C.
#   B (10⁵): repetiu o expoente escrito; E (7 · 10⁵) nem é potência de 10 (explicações do material).
#   NOSSAS: A (10⁴) e D (10⁷) — a ordem só pode ser o expoente escrito (10⁵) ou o seguinte (10⁶); nenhum erro de critério leva a elas.
# QUESTÃO 9 do material (texto idêntico na tela): 1,2 · 10⁶ × 1,5 · 10² = 1,8 · 10⁸ → B.
#   Estimativa: 1 × 2 = 2 → 2 · 10⁸, ordem 10⁸ → só B e C (ambas ordem 10⁸) ficam; a conta exata (1,2 × 1,5 = 1,8) decide.
#   D (1,8 · 10¹²): multiplicou os expoentes; E (8 · 10³): dividiu em vez de multiplicar (explicações do material).
#   NOSSAS: C (2,7 · 10⁸): somou 1,2 + 1,5 em vez de multiplicar; A (1,8 · 10⁷): expoente errado — daria só 15 litros por pessoa.
# Frases-chave (meio e fim, idênticas):
#   1. Ordem de grandeza é a potência de 10 mais próxima.
#   2. Coeficiente a partir de 3,16: sobe uma ordem.
#   3. Alternativas em escalas diferentes? Estime.
# Atalhos (verde): "até 3 fica, de 4 para cima sobe; entre 3 e 4, compare com 3,16" · "cada ordem de diferença = × 10" ·
#   "a ordem é o expoente escrito ou o seguinte, nunca outro" · "olhe as alternativas antes de calcular".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Ordem de grandeza: por que 7 · 10⁵ é ordem 10⁶ (o critério do 3,16) | Notação Científica Ep. 4"
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
        "{a}Qual é a ordem de grandeza de *oitocentos e cinquenta mil?* [p=0.5] {b}Quase todo mundo responde *dez elevado "
        "a cinco,* [p=0.2] porque está escrito oito vírgula cinco vezes dez elevado a cinco. [p=0.5] {c}A resposta é *dez "
        "elevado a seis.* [p=0.4] {d}E muitas questões do ENEM se resolvem em *quinze segundos* [p=0.2] só com isso."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai achar a ordem de grandeza pelo *critério certo,* [p=0.3] {b}e usar a "
        "*estimativa* para eliminar alternativas [p=0.2] sem fazer a conta inteira."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Na forma exata da notação científica, [p=0.2] o número da frente, "
        "[p=0.2] o *coeficiente,* [p=0.2] tem um único algarismo antes da vírgula, [p=0.2] diferente de zero. [p=0.4] "
        "{b}E para multiplicar, [p=0.2] você multiplica os coeficientes [p=0.2] e *soma* os expoentes. [p=0.3] {c}Se o "
        "coeficiente passar de dez, [p=0.2] a gangorra conserta: [p=0.2] quarenta vezes dez elevado a seis [p=0.2] vira "
        "quatro vezes dez elevado a sete."),

    # ================= CONCRETO: ESCALAS =================
    dict(id="04", block="escala", text=
        "{t}Olhe esses números. [p=0.3] {a}A espessura de um fio de cabelo. [p=0.3] {b}O tamanho de um vírus. [p=0.3] "
        "{c}A população do Brasil. [p=0.3] {d}A distância da Terra ao Sol. [p=0.5] {e}Para comparar coisas tão "
        "diferentes, [p=0.2] o valor exato quase não importa. [p=0.3] {f}O que importa é a *escala:* [p=0.2] o tamanho "
        "aproximado, [p=0.2] na casa dos milhares, dos milhões, dos bilhões."),

    # ================= BLOCO A: DEFINIÇÃO =================
    dict(id="05", block="definicao", text=
        "{t}E como se mede a escala de um número? [p=0.4] {a}Com a *ordem de grandeza:* [p=0.2] a potência de dez *mais "
        "próxima* do número. [p=0.4] {b}Pense nas potências de dez como *casas* numa rua: [p=0.2] dez, [p=0.2] cem, "
        "[p=0.2] mil, [p=0.2] dez mil. [p=0.4] {c}A ordem de grandeza diz em que casa o número *mora.* [p=0.4] {d}Ela não "
        "diz o valor exato. [p=0.2] Diz a escala."),

    # ================= BLOCO B: A INTUIÇÃO =================
    dict(id="06", block="intuicao", text=
        "{t}Voltando ao gancho: [p=0.2] oitocentos e cinquenta mil. [p=0.4] {a}Ele fica entre *cem mil,* [p=0.2] que é "
        "dez elevado a cinco, [p=0.2] e *um milhão,* [p=0.2] que é dez elevado a seis. [p=0.4] {b}De qual dos dois ele está "
        "mais perto? [p=0.5] {c}Faltam só cento e cinquenta mil [p=0.2] para chegar a um milhão. [p=0.4] {d}Ele mora na "
        "casa do *milhão:* [p=0.2] ordem dez elevado a seis. [p=0.4] {e}O expoente escrito era cinco, [p=0.2] mas a "
        "resposta é seis."),

    # ================= BLOCO C: O CRITÉRIO =================
    dict(id="07", block="criterio", text=
        "{t}E existe uma regra para não depender do olho? [p=0.4] {a}Existe. [p=0.2] Escreva o número em notação "
        "científica [p=0.2] e olhe o *coeficiente.* [p=0.4] {b}Se ele for *menor que três vírgula dezesseis,* [p=0.2] a "
        "ordem é o próprio dez elevado a n. [p=0.4] {c}Se for *três vírgula dezesseis ou mais,* [p=0.2] a ordem *sobe um:* "
        "[p=0.2] dez elevado a n mais um."),
    dict(id="08", block="criterio", text=
        "{t}Testando. [p=0.3] {a}Dois vírgula três vezes dez elevado a cinco: [p=0.2] dois vírgula três é menor que três "
        "vírgula dezesseis, [p=0.2] fica *dez elevado a cinco.* [p=0.4] {b}Oito vírgula cinco vezes dez elevado a cinco: "
        "[p=0.2] passou, [p=0.2] sobe para *dez elevado a seis.* [p=0.4] {c}Um vírgula um vezes dez elevado a doze: [p=0.2] "
        "fica *dez elevado a doze.* [p=0.4] {d}E com expoente negativo? [p=0.2] Cinco vezes dez elevado a menos oito. "
        "[p=0.3] {e}Cinco passou, [p=0.2] então soma um ao expoente: [p=0.2] menos oito mais um, [p=0.2] *menos sete.*"),

    # ================= BLOCO D: POR QUE 3,16 =================
    dict(id="09", block="regua", text=
        "{t}Mas por que três vírgula dezesseis? [p=0.3] Por que não *cinco,* [p=0.2] que é a metade do caminho até dez? "
        "[p=0.5] {a}Porque, entre as potências de dez, [p=0.2] a gente anda *multiplicando,* [p=0.2] não somando. [p=0.4] "
        "{b}De um para cinco, [p=0.2] você multiplicou por *cinco.* [p=0.3] {c}De cinco para dez, [p=0.2] só por *dois.* "
        "[p=0.4] {d}Passos diferentes: [p=0.2] o cinco não está no meio."),
    dict(id="10", block="regua", text=
        "{t}O meio de verdade é o número que, [p=0.2] multiplicado por ele mesmo, [p=0.2] dá dez. [p=0.4] {a}Esse número "
        "tem nome: [p=0.2] *raiz de dez,* [p=0.2] mais ou menos *três vírgula dezesseis.* [p=0.4] {b}De um para três "
        "vírgula dezesseis, [p=0.2] um passo de vezes três vírgula dezesseis. [p=0.3] {c}De três vírgula dezesseis para "
        "dez, [p=0.2] *outro passo igual.* [p=0.4] {d}Confere: [p=0.2] três vírgula dezesseis vezes três vírgula dezesseis "
        "dá quase *dez.*"),
    dict(id="11", block="regua", text=
        "{t}Veja a diferença num caso real: [p=0.2] *quatrocentos mil.* [p=0.4] {a}Em distância, [p=0.2] ele parece mais "
        "perto de cem mil. [p=0.4] {b}Mas em *vezes:* [p=0.2] ele já é *quatro vezes* cem mil, [p=0.3] {c}e um milhão é só "
        "*duas vezes e meia* quatrocentos mil. [p=0.4] {d}Na escala, [p=0.2] perto é perto *em vezes.* [p=0.3] Ordem dez "
        "elevado a seis, [p=0.2] porque quatro passou de três vírgula dezesseis."),
    dict(id="12", block="regua", text=
        "{t}E um atalho para não fazer conta: [p=0.3] {a}coeficiente *até três,* [p=0.2] fica. [p=0.3] {b}De *quatro para "
        "cima,* [p=0.2] sobe. [p=0.4] {c}Só entre três e quatro [p=0.2] você precisa comparar com o três vírgula dezesseis "
        "de verdade."),

    # ================= BLOCO E: DIFERENÇA DE ORDENS =================
    dict(id="13", block="ordens", text=
        "{t}E para que serve saber a ordem? [p=0.3] Para *comparar.* [p=0.4] {a}Um fio de cabelo tem ordem dez elevado a "
        "menos quatro metro. [p=0.3] {b}Um vírus, [p=0.2] dez elevado a menos sete. [p=0.4] {c}São *três ordens* de "
        "diferença. [p=0.3] {d}Cada ordem é um vezes dez: [p=0.2] dez, [p=0.2] vezes dez, [p=0.2] vezes dez. [p=0.3] "
        "{e}O cabelo é cerca de *mil vezes* mais grosso que o vírus."),

    # ================= NÓS FAZEMOS =================
    dict(id="14", block="exercicio", text=
        "{t}Sua vez. [p=0.3] Dê a ordem de grandeza de três números. [p=0.3] {a}Dois vírgula nove vezes dez elevado a "
        "quatro. [p=0.3] {b}Três vírgula cinco vezes dez elevado a quatro. [p=0.3] {c}E nove vírgula oito vezes dez elevado "
        "a menos quatro. [p=0.4] {e}*Pause o vídeo e responda.* [p=2.0]"),
    dict(id="15", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Dois vírgula nove é menor que três vírgula dezesseis: [p=0.2] *dez elevado a "
        "quatro.* [p=0.4] {b}Três vírgula cinco passou, [p=0.2] por pouco: [p=0.2] *dez elevado a cinco.* [p=0.4] {c}Nove "
        "vírgula oito passou: [p=0.2] menos quatro mais um, [p=0.2] *dez elevado a menos três.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="16", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] ordem de grandeza é a potência de dez mais próxima. "
        "[p=0.5] {b}Dois: [p=0.2] coeficiente a partir de três vírgula dezesseis: [p=0.2] sobe uma ordem. [p=0.5] {c}Três: "
        "[p=0.2] alternativas em escalas diferentes? [p=0.2] Estime."),

    # ================= BLOCO F: A CONTA DE GUARDANAPO =================
    dict(id="17", block="guardanapo", text=
        "{t}E o que é *estimar?* [p=0.4] {a}É fazer uma conta *aproximada,* [p=0.2] de propósito, [p=0.2] só para acertar a "
        "escala. [p=0.4] {b}Sabe aquela conta rápida que alguém rabisca num guardanapo de bar? [p=0.3] É isso. [p=0.4] "
        "{c}O método: [p=0.2] arredonde cada coeficiente para *um algarismo só,* [p=0.2] multiplique de cabeça [p=0.2] e "
        "some os expoentes."),
    dict(id="18", block="guardanapo", text=
        "{t}Exemplo: [p=0.2] quatro vírgula sete vezes dez elevado a três, [p=0.2] vezes oito vírgula dois vezes dez "
        "elevado a cinco. [p=0.4] {a}Quatro vírgula sete arredonda para *cinco.* [p=0.3] {b}Oito vírgula dois, [p=0.2] para "
        "*oito.* [p=0.3] {c}Cinco vezes oito, [p=0.2] *quarenta.* [p=0.3] {d}Três mais cinco, [p=0.2] *oito* no expoente. "
        "[p=0.4] {e}Quarenta vezes dez elevado a oito: [p=0.2] a gangorra deixa *quatro vezes dez elevado a nove.*"),
    dict(id="19", block="guardanapo", text=
        "{t}E a conta exata? [p=0.3] {a}Três vírgula oito cinco quatro vezes dez elevado a nove. [p=0.4] {b}O guardanapo "
        "errou *menos de quatro por cento.* [p=0.4] {c}E acertou o mais importante: [p=0.2] a escala, [p=0.2] *dez elevado "
        "a nove.*"),

    # ================= BLOCO G: QUANDO USAR =================
    dict(id="20", block="quando", text=
        "{t}E quando vale estimar? [p=0.4] {a}*Olhe as alternativas antes de calcular.* [p=0.4] {b}Se elas estão em "
        "escalas diferentes, [p=0.2] tipo dez elevado a seis, [p=0.2] dez elevado a oito, [p=0.2] dez elevado a dez, "
        "[p=0.3] a estimativa resolve. [p=0.4] {c}Se estão todas na *mesma* potência, [p=0.2] e só o coeficiente muda, "
        "[p=0.3] aí a conta precisa ser *exata.*"),

    # ================= BLOCO H: ESCALAS PARA TER NA CABEÇA =================
    dict(id="21", block="zoom", text=
        "{t}Agora, uma viagem de escala, [p=0.2] do muito pequeno ao muito grande. [p=0.2] Valores aproximados. [p=0.4] "
        "{a}Um átomo: [p=0.2] dez elevado a menos dez metro. [p=0.3] {b}Um vírus: [p=0.2] dez elevado a menos sete. "
        "[p=0.3] {c}Uma célula: [p=0.2] dez elevado a menos cinco. [p=0.3] {d}Um fio de cabelo: [p=0.2] dez elevado a menos "
        "quatro."),
    dict(id="22", block="zoom", text=
        "{a}O raio da Terra: [p=0.2] uns seis vírgula quatro vezes dez elevado a seis metros. [p=0.3] Seis vírgula quatro "
        "passou, [p=0.2] ordem *dez elevado a sete.* [p=0.4] {b}Da Terra ao Sol: [p=0.2] dez elevado a onze. [p=0.4] {c}E "
        "gente? [p=0.2] O Brasil: [p=0.2] uns duzentos milhões, [p=0.2] ordem dez elevado a oito. [p=0.4] {d}O mundo: "
        "[p=0.2] uns *oito bilhões.* [p=0.3] Oito passou de três vírgula dezesseis: [p=0.2] ordem *dez elevado a dez.*"),

    # ================= ERROS CLÁSSICOS =================
    dict(id="23", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] repetir o expoente escrito como ordem de grandeza. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque o expoente está ali, [p=0.2] prontinho. [p=0.4] {c}Mas antes compare o "
        "coeficiente com três vírgula dezesseis: [p=0.2] a partir dele, [p=0.2] sobe um."),
    dict(id="24", block="erros", text=
        "{a}Segundo: [p=0.2] usar o *cinco* como ponto de corte. [p=0.4] {b}Parece certo, [p=0.2] porque cinco é a metade "
        "de dez, [p=0.2] e é assim que a gente arredonda. [p=0.4] {c}Mas na escala se anda multiplicando: [p=0.2] o meio é "
        "três vírgula dezesseis."),
    dict(id="25", block="erros", text=
        "{a}Terceiro: [p=0.2] fazer a conta exata [p=0.2] quando a estimativa já resolvia. [p=0.4] {b}Parece mais seguro, "
        "[p=0.2] fazer tudo certinho. [p=0.4] {c}Mas custa minutos que faltam no fim da prova. [p=0.2] Alternativas em "
        "escalas diferentes? [p=0.2] Estime."),

    # ================= QUESTÃO 5 DO MATERIAL =================
    dict(id="26", block="questao5", text=
        "{t}Agora, questões no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}Um estudo estima em *sete "
        "vírgula dois vezes dez elevado a cinco* [p=0.2] o número de árvores de uma reserva florestal. [p=0.3] A ordem de "
        "grandeza dessa quantidade é: [p=0.4] {qa}A: [p=0.2] dez elevado a quatro. [p=0.3] {qb}B: [p=0.2] dez elevado a "
        "cinco. [p=0.3] {qc}C: [p=0.2] dez elevado a seis. [p=0.3] {qd}D: [p=0.2] dez elevado a sete. [p=0.3] {qe}E: "
        "[p=0.2] sete vezes dez elevado a cinco. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="27", block="questao5", text=
        "{t}Vamos resolver. [p=0.3] {a}O coeficiente é sete vírgula dois. [p=0.3] {b}Sete vírgula dois é maior que três "
        "vírgula dezesseis: [p=0.2] *sobe uma ordem.* [p=0.4] {c}Dez elevado a cinco vira *dez elevado a seis.* [p=0.3] "
        "{ok}*Letra C!* [p=0.4] {d}E faz sentido: [p=0.2] setecentos e vinte mil [p=0.2] está muito mais perto de um milhão "
        "[p=0.2] do que de cem mil."),
    dict(id="28", block="questao5", text=
        "{t}E as outras? [p=0.3] {xb}A B é a armadilha da aula: [p=0.2] repetiu o expoente escrito. [p=0.4] {xe}A E nem é "
        "uma potência de dez. [p=0.4] {xa}E a A e a D caem com um atalho: [p=0.2] a ordem é o expoente escrito [p=0.2] "
        "{xd}*ou o seguinte,* [p=0.2] nunca outro. [p=0.3] Só a B ou a C podiam estar certas."),

    # ================= QUESTÃO 9 DO MATERIAL =================
    dict(id="29", block="questao9", text=
        "{t}Mais uma. [p=0.3] {a}Uma cidade com *um vírgula dois vezes dez elevado a seis* habitantes [p=0.2] registra "
        "consumo médio de *um vírgula cinco vezes dez elevado a dois* litros de água [p=0.2] por pessoa por dia. [p=0.3] O "
        "consumo diário total da cidade, [p=0.2] em litros, [p=0.2] é de aproximadamente: [p=0.4] {qa}A: [p=0.2] um vírgula "
        "oito vezes dez elevado a sete. [p=0.3] {qb}B: [p=0.2] um vírgula oito vezes dez elevado a oito. [p=0.3] {qc}C: "
        "[p=0.2] dois vírgula sete vezes dez elevado a oito. [p=0.3] {qd}D: [p=0.2] um vírgula oito vezes dez elevado a "
        "doze. [p=0.3] {qe}E: [p=0.2] oito vezes dez elevado a três. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="30", block="questao9", text=
        "{t}Primeiro, o guardanapo. [p=0.3] {a}Consumo total é o consumo de cada pessoa *vezes* o número de pessoas. "
        "[p=0.4] {b}Um vírgula dois arredonda para *um.* [p=0.3] Um vírgula cinco, [p=0.2] para *dois.* [p=0.3] {c}Um vezes "
        "dois, [p=0.2] dois. [p=0.2] Seis mais dois, [p=0.2] oito. [p=0.2] Uns *dois vezes dez elevado a oito.* [p=0.4] "
        "{d}Escala dez elevado a oito. [p=0.3] {xa}A está na escala sete, [p=0.2] {xd}a D na doze, [p=0.2] {xe}a E na "
        "quatro. [p=0.4] {e}Sobraram só a *B* e a *C.*"),
    dict(id="31", block="questao9", text=
        "{t}Agora a conta exata decide. [p=0.3] {a}Um vírgula dois vezes um vírgula cinco: [p=0.2] *um vírgula oito.* "
        "[p=0.4] {b}Um vírgula oito vezes dez elevado a oito: [p=0.2] cento e oitenta milhões de litros por dia. [p=0.3] "
        "{ok}*Letra B!* [p=0.4] {xc}A C somou um vírgula dois mais um vírgula cinco, [p=0.2] em vez de multiplicar. "
        "[p=0.4] {f}A D multiplicou os expoentes, [p=0.2] a E dividiu, [p=0.2] e a A daria só quinze litros por pessoa."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="32", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] ordem de grandeza é a potência de dez mais próxima. "
        "[p=0.5] {b}Dois: [p=0.2] coeficiente a partir de três vírgula dezesseis: [p=0.2] sobe uma ordem. [p=0.5] {c}Três: "
        "[p=0.2] alternativas em escalas diferentes? [p=0.2] Estime."),

    # ================= PONTE E CTA =================
    dict(id="33", block="ponte", text=
        "{a}Mega, [p=0.2] giga, [p=0.2] nano, [p=0.2] micro: [p=0.2] os prefixos são *potências de dez disfarçadas.* "
        "[p=0.4] {b}E existe uma armadilha na conversão de *área* e *volume* [p=0.2] que é um dos erros mais caros da prova. "
        "[p=0.4] {c}Próximo episódio."),
    dict(id="34", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você também usava o cinco como ponto de corte? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
