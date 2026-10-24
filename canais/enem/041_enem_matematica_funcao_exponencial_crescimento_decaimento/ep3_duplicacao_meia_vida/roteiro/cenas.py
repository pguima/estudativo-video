# Roteiro — Função Exponencial, Episódio 3 de 6: duplicação e meia-vida, conte os intervalos
# Base: Estudos/Enem/estudos/01-matematica/26-funcao-exponencial-crescimento-decaimento.html — seção 05 + Questões 1, 2 e 8.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O RELÓGIO QUE APITA: o expoente é um contador de intervalos — quantas vezes o relógio apitou desde o começo.
#   A PIZZA QUE SOBROU: meia-vida corta a pizza que SOBROU, não a pizza inteira (metade, depois metade da metade).
#   DOBRAS SE MULTIPLICAM: 6 dobras são ×64, não ×12.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Q₀ · aᵗ é revisão do episódio 2; progressão geométrica só citada (série própria); a Questão 7 fica para o episódio 5.
# Exemplos dos blocos (prompt): 1 000 bactérias, dobra a cada 30 min, 3 h → 6 duplicações → 64 000 · césio-137 (≈ 30 anos):
#   90 anos → 3 meias-vidas → 1/8 · barras 100% → 50% → 25% → 12,5% · caminho inverso com o césio: 1/8 → 3 meias-vidas →
#   90 anos; 1/16 → 4 meias-vidas → 120 anos (o césio, NÃO o carbono-14 da Q8, que é "você faz").
# Nós fazemos (prompt): 120 g, meia-vida 10 anos, 30 anos → 3 meias-vidas → 120 → 60 → 30 → 15 g.
# Erros (prompt): 2 meias-vidas ⇒ 0% (certo 25%) · 6 dobras ⇒ ×12 (certo ×64) · contar o instante inicial (7 em vez de 6):
#   os três usam os números dos blocos (1 000 bactérias: 7 apitos dariam 128 000), não os das questões.
# QUESTÃO 1 ("eu faço"): D, 32 000. Erradas = material (A 3 000 = 500 · 6 linear; B 6 000 = 500 · 2 · 6; C 16 000 conta
#   5 duplicações; E 64 000 conta 7, o instante inicial como duplicação).
# QUESTÃO 2 ("nós fazemos", pausa): B, 5 mg. Erradas = material (A 2,5 uma a mais; C 10 para na terceira; D 20 divide 80
#   por 4; E 40 aplica uma só).
# QUESTÃO 8 ("você faz", pausa): D, 22 920 anos. Erradas = material (A 1 432,5 divide a meia-vida por 4; B e C contam 2 e
#   3 meias-vidas; E 91 680 trata o 16 como número de meias-vidas).
# Acréscimos NOSSOS (marcados): duas cenas verdes de ATALHO — "converta, divida, conte os apitos" com a escadinha das
#   dobras 2, 4, 8, 16, 32, 64 (cena 07) e "o denominador conta os cortes: divida por 2 até chegar a 1" (cena 12); e as
#   conferências de plausibilidade (32 000 fica entre 16 000 e 64 000; 5 mg é menos que 80; fração pequena = muitos anos).
# Frases-chave (meio e fim, idênticas): 1. Primeiro conte os intervalos, depois escreva a potência.
#   2. Cada meia-vida corta pela metade o que existe naquele momento.
#   3. Duplicações se multiplicam: 6 dobras são ×64, não ×12.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Duplicação e meia-vida do zero: conte os intervalos · Matemática ENEM, Exponencial episódio 3"

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
        "{a}Um material radioativo *perde metade* a cada trinta anos. [p=0.5] {b}Depois de sessenta anos, [p=0.2] "
        "*acabou?* [p=0.4] {c}Não: [p=0.2] ainda resta *um quarto.* [p=0.4] {d}Depois de noventa, [p=0.2] *um oitavo.* "
        "[p=0.4] {e}Ele *nunca chega a zero.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o terceiro episódio da série de *Função exponencial.* [p=0.4] {a}Ao final, [p=0.2] você vai resolver "
        "*qualquer questão* de *dobra a cada* [p=0.2] {b}ou de *meia-vida* [p=0.3] {c}*contando intervalos,* [p=0.2] sem "
        "fórmula decorada."),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Do episódio dois: [p=0.2] a lei *Q zero vezes a elevado a t.* [p=0.2] Q "
        "zero é o valor do começo; [p=0.2] a é o fator. [p=0.4] {b}Da série de Potenciação: [p=0.2] dois elevado a seis "
        "[p=0.2] é *sessenta e quatro.* [p=0.4] {c}E um meio elevado a quatro [p=0.2] é *um dezesseis avos.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Três cenas reais. [p=0.4] {a}Num laboratório, [p=0.2] uma cultura de *bactérias* [p=0.2] dobra de tempos em "
        "tempos. [p=0.4] {b}No seu corpo, [p=0.2] um *remédio* vai saindo do sangue, [p=0.2] metade de cada vez. [p=0.4] "
        "{c}E em *Goiânia,* em mil novecentos e oitenta e sete, [p=0.2] o *césio-cento e trinta e sete* de um aparelho "
        "abandonado [p=0.2] causou o maior acidente radioativo do Brasil. [p=0.4] {d}As três seguem a *mesma conta.*"),

    # ================= BLOCO A: DUPLICAÇÃO =================
    dict(id="05", block="duplicacao", text=
        "{t}Como escrever uma coisa que *dobra a cada* tanto tempo? [p=0.4] {a}*Tempo de duplicação* [p=0.2] é o tempo "
        "que a quantidade leva para *dobrar.* [p=0.2] Vamos chamar de *T.* [p=0.4] {b}A lei fica: [p=0.2] Q zero vezes "
        "*dois* [p=0.2] elevado a *t sobre T.* [p=0.4] {c}E esse expoente, [p=0.2] t sobre T, [p=0.2] é um *contador:* "
        "[p=0.2] quantas vezes o relógio *apitou* desde o começo. [p=0.4] {d}Se T é trinta minutos [p=0.2] e passaram noventa, "
        "[p=0.2] o relógio apitou *três* vezes."),

    # ================= BLOCO B: O EXEMPLO DAS BACTÉRIAS =================
    dict(id="06", block="bacterias", text=
        "{t}Mil bactérias dobram a cada *trinta minutos.* [p=0.2] Quantas haverá depois de *três horas?* [p=0.4] {a}Primeiro, "
        "[p=0.2] a *mesma unidade:* [p=0.2] três horas são *cento e oitenta minutos.* [p=0.4] {b}Agora, [p=0.2] conte os "
        "apitos: [p=0.2] cento e oitenta dividido por trinta [p=0.2] dá *seis.* [p=0.4] {c}A cada apito, [p=0.2] dobra: "
        "[p=0.2] dois mil, quatro mil, oito mil, [p=0.2] dezesseis, trinta e dois, [p=0.2] *sessenta e quatro mil.* "
        "[p=0.4] {d}Na fórmula: [p=0.2] mil vezes dois elevado a seis, [p=0.2] mil vezes sessenta e quatro. [p=0.4] {e}Repare: [p=0.2] o tempo "
        "passou *seis* intervalos, [p=0.2] e a população ficou *sessenta e quatro* vezes maior."),
    dict(id="07", block="atalho_dup", text=
        "{t}Atalho para qualquer *dobra a cada.* [p=0.4] {a}Um: [p=0.2] *converta* o tempo para a unidade do intervalo. "
        "[p=0.3] {b}Dois: [p=0.2] *divida* e conte os apitos. [p=0.3] {c}Três: [p=0.2] *dobre* de cabeça, [p=0.2] um "
        "apito de cada vez: [p=0.2] dois, quatro, oito, dezesseis, trinta e dois, sessenta e quatro. [p=0.4] {d}Seis "
        "apitos, [p=0.2] *vezes sessenta e quatro.*"),

    # ================= BLOCO C: MEIA-VIDA =================
    dict(id="08", block="meiavida", text=
        "{t}E o caminho contrário, [p=0.2] o que *some* pela metade? [p=0.4] {a}Um *isótopo radioativo* [p=0.2] é uma "
        "versão instável de um elemento, [p=0.2] que vai se desfazendo sozinha. [p=0.2] Esse desfazer se chama "
        "*decaimento.* [p=0.4] {b}*Meia-vida* [p=0.2] é o tempo para restar *metade* da quantidade. [p=0.4] {c}A lei: "
        "[p=0.2] Q zero vezes *um meio* [p=0.2] elevado a *t sobre T.* [p=0.3] É o que acontece com o remédio: [p=0.2] depois "
        "de uma meia-vida, [p=0.2] sobra metade da dose no sangue. [p=0.3] O mesmo contador de apitos, [p=0.2] agora "
        "*dividindo* por dois."),

    # ================= BLOCO D: CÉSIO =================
    dict(id="09", block="cesio", text=
        "{t}O césio-cento e trinta e sete [p=0.2] tem meia-vida de *cerca de trinta anos.* [p=0.2] Quanto resta depois de "
        "*noventa?* [p=0.4] {a}Conte os apitos: [p=0.2] noventa dividido por trinta, [p=0.2] *três* meias-vidas. [p=0.4] "
        "{b}Agora a potência: [p=0.2] um meio elevado a três [p=0.2] é *um oitavo.* [p=0.4] {c}Resta *um oitavo* do césio "
        "inicial. [p=0.2] Pouco, [p=0.2] mas *não é zero.* [p=0.4] {d}E em sessenta anos? [p=0.2] Duas meias-vidas: [p=0.2] *um "
        "quarto,* [p=0.2] como no começo da aula."),

    # ================= BLOCO E: AS BARRAS E A PIZZA =================
    dict(id="10", block="barras", text=
        "{t}Por que nunca chega a zero? [p=0.4] {a}Comece com *cem por cento.* [p=0.3] {b}Uma meia-vida: [p=0.2] "
        "*cinquenta.* [p=0.3] {c}Outra: [p=0.2] metade de cinquenta, [p=0.2] *vinte e cinco.* [p=0.3] Outra: [p=0.2] *doze "
        "e meio.* [p=0.4] {d}Pense numa *pizza.* [p=0.2] Cada meia-vida corta pela metade a pizza que *sobrou,* [p=0.2] e "
        "não a pizza inteira. [p=0.4] {e}Metade de um pedaço [p=0.2] *ainda é um pedaço.* [p=0.4] {f}No gráfico, [p=0.2] a curva desce e *gruda* no eixo, [p=0.2] sem tocar: "
        "[p=0.2] é a parede invisível do episódio um."),

    # ================= BLOCO F: O CAMINHO INVERSO =================
    dict(id="11", block="inverso", text=
        "{t}E se a questão der a *fração que resta* [p=0.2] e perguntar o *tempo?* [p=0.4] {a}Resta *um oitavo* do césio. "
        "[p=0.2] Um oitavo é um meio elevado a *três:* [p=0.2] três meias-vidas. [p=0.4] {b}Cada uma dura trinta anos: "
        "[p=0.2] três vezes trinta, [p=0.2] *noventa anos.* [p=0.4] {c}Resta *um dezesseis avos?* [p=0.2] Um meio elevado "
        "a *quatro:* [p=0.2] quatro meias-vidas, [p=0.2] *cento e vinte anos.*"),
    dict(id="12", block="atalho_inv", text=
        "{t}Atalho para achar quantas meias-vidas passaram. [p=0.4] {a}Pegue o *denominador* da fração. [p=0.3] {b}Divida "
        "por dois [p=0.2] até chegar a *um,* [p=0.2] contando os cortes: [p=0.2] dezesseis, oito, quatro, dois, um. "
        "[p=0.4] {c}*Quatro cortes,* [p=0.2] quatro meias-vidas. [p=0.3] Com o oito: [p=0.2] quatro, dois, um, [p=0.2] "
        "*três* cortes. [p=0.4] {d}Depois, [p=0.2] *multiplique* pela duração de "
        "cada uma."),

    # ================= BLOCO G: SÓ CITAR A PG =================
    dict(id="13", block="pg", text=
        "{t}Um detalhe para o futuro. [p=0.4] {a}Os valores a cada apito, [p=0.2] mil, dois mil, quatro mil, oito mil, "
        "[p=0.2] formam uma *progressão geométrica:* [p=0.2] uma lista em que cada número é o anterior vezes o mesmo "
        "fator. [p=0.4] {b}Ela tem *série própria.* [p=0.2] Aqui, [p=0.2] basta contar os apitos."),

    # ================= NÓS FAZEMOS =================
    dict(id="14", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Uma amostra de *cento e vinte gramas* [p=0.2] tem meia-vida de *dez anos.* [p=0.3] Quanto "
        "resta depois de *trinta anos?* [p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="15", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Conte os apitos: [p=0.2] trinta dividido por dez, [p=0.2] *três* meias-vidas. "
        "[p=0.4] {b}Corte a pizza que sobrou: [p=0.2] cento e vinte, [p=0.2] sessenta, [p=0.2] trinta, [p=0.2] *quinze "
        "gramas.* [p=0.4] {c}Conferindo: [p=0.2] cento e vinte vezes um oitavo [p=0.2] também dá quinze. [p=0.4] {d}E faz sentido: [p=0.2] quinze gramas é "
        "bem menos que cento e vinte, [p=0.2] e *ainda não é zero.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="16", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] primeiro conte os intervalos, [p=0.2] depois escreva a "
        "potência. [p=0.5] {b}Dois: [p=0.2] cada meia-vida corta pela metade [p=0.2] o que existe naquele momento. "
        "[p=0.5] {c}Três: [p=0.2] duplicações se multiplicam: [p=0.2] seis dobras são vezes sessenta e quatro, [p=0.2] não "
        "vezes doze."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="17", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *duas meias-vidas* [p=0.2] e não sobra *nada.* "
        "[p=0.4] {b}Parece certo, [p=0.2] porque metade mais metade [p=0.2] dá um inteiro. [p=0.4] {c}Mas a segunda "
        "metade é metade do que *sobrou:* [p=0.2] cem, cinquenta, [p=0.2] *vinte e cinco por cento.*"),
    dict(id="18", block="erros", text=
        "{a}Segundo: [p=0.2] dobrou *seis vezes,* [p=0.2] então ficou *doze vezes* maior. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque dobrar é vezes dois, [p=0.2] e seis vezes dois dá doze. [p=0.4] {c}Mas cada dobra age sobre o "
        "resultado da anterior: [p=0.2] dois vezes dois vezes dois, [p=0.2] seis vezes. [p=0.2] *Vezes sessenta e "
        "quatro.*"),
    dict(id="19", block="erros", text=
        "{a}Terceiro: [p=0.2] contar o *começo* como um apito. [p=0.3] Nas mil bactérias, [p=0.2] *sete* duplicações, "
        "[p=0.2] e cento e vinte e oito mil. [p=0.4] {b}Parece certo, [p=0.2] porque a lista dos instantes, [p=0.2] zero, "
        "trinta, sessenta, até cento e oitenta, [p=0.2] tem *sete* números. [p=0.4] {c}Mas o relógio só apita quando um intervalo *termina:* "
        "[p=0.2] cento e oitenta dividido por trinta, [p=0.2] *seis* apitos."),

    # ================= QUESTÃO 1 (EU FAÇO) =================
    dict(id="20", block="q1", text=
        "{t}Agora, questões no estilo do ENEM. [p=0.2] Esta primeira, [p=0.2] *eu faço* com você olhando. [p=0.4] {a}Uma "
        "cultura começa com *quinhentas bactérias,* [p=0.2] e a população *dobra a cada vinte minutos.* [p=0.3] O número de "
        "bactérias *duas horas* depois será: [p=0.3] {qa}A: [p=0.2] três mil. [p=0.2] {qb}B: [p=0.2] seis mil. [p=0.2] "
        "{qc}C: [p=0.2] dezesseis mil. [p=0.2] {qd}D: [p=0.2] trinta e dois mil. [p=0.2] {qe}E: [p=0.2] sessenta e quatro "
        "mil."),
    dict(id="21", block="q1", text=
        "{t}É um *dobra a cada.* [p=0.3] {a}Converta: [p=0.2] duas horas são *cento e vinte minutos.* [p=0.4] {b}Conte os "
        "apitos: [p=0.2] cento e vinte dividido por vinte, [p=0.2] *seis.* [p=0.4] {c}Potência: [p=0.2] quinhentos vezes "
        "dois elevado a seis, [p=0.2] quinhentos vezes sessenta e quatro, [p=0.2] *trinta e dois mil.* [p=0.4] {d}Faz "
        "sentido? [p=0.2] Cresceu muito, [p=0.2] como uma exponencial deve crescer. [p=0.3] Dezesseis mil seria um apito a menos; [p=0.2] sessenta e quatro "
        "mil, um a mais. [p=0.2] O trinta e dois mil fica *no lugar certo.* [p=0.3] {ok}*Letra D!*"),
    dict(id="22", block="q1", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A faz quinhentos vezes seis: [p=0.2] *soma* quinhentos a cada apito, [p=0.2] "
        "como se fosse linear. [p=0.4] {xb}A B faz quinhentos vezes dois vezes seis: [p=0.2] *soma* as dobras. [p=0.4] "
        "{xc}A C conta só *cinco* apitos. [p=0.4] {xe}E a E conta *sete,* [p=0.2] o começo como um apito."),

    # ================= QUESTÃO 2 (NÓS FAZEMOS) =================
    dict(id="23", block="q2", text=
        "{t}A próxima, [p=0.2] a gente resolve *junto.* [p=0.4] {a}O *iodo-cento e trinta e um,* [p=0.2] usado em exames da "
        "tireoide, [p=0.2] tem meia-vida de *oito dias.* [p=0.3] Um laboratório recebeu *oitenta miligramas.* [p=0.3] Depois "
        "de *trinta e dois dias,* [p=0.2] restam: [p=0.3] {qa}A: [p=0.2] dois vírgula cinco miligramas. [p=0.2] {qb}B: "
        "[p=0.2] cinco. [p=0.2] {qc}C: [p=0.2] dez. [p=0.2] {qd}D: [p=0.2] vinte. [p=0.2] {qe}E: [p=0.2] quarenta. [p=0.5] "
        "{p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="24", block="q2", text=
        "{t}Vamos juntos. [p=0.3] {a}As unidades já combinam: [p=0.2] dias e dias. [p=0.3] Conte os apitos: [p=0.2] trinta "
        "e dois dividido por oito, [p=0.2] *quatro* meias-vidas. [p=0.4] {b}Corte o que sobrou: [p=0.2] oitenta, "
        "[p=0.2] quarenta, [p=0.2] vinte, [p=0.2] dez, [p=0.2] *cinco.* [p=0.4] {c}Na potência: [p=0.2] oitenta vezes um "
        "dezesseis avos, [p=0.2] *cinco miligramas.* [p=0.3] Faz sentido? [p=0.2] Cinco é bem menos que oitenta, [p=0.2] e "
        "ainda é mais que zero. [p=0.3] {ok}*Letra B!*"),
    dict(id="25", block="q2", text=
        "{t}E as outras? [p=0.3] {xa}A A corta *uma vez a mais.* [p=0.4] {xc}A C *para* na terceira. [p=0.4] {xd}A D "
        "divide oitenta por *quatro,* [p=0.2] o número de meias-vidas, [p=0.2] em vez de dividir por dezesseis. [p=0.4] "
        "{xe}E a E corta *uma vez só.*"),

    # ================= QUESTÃO 8 (VOCÊ FAZ) =================
    dict(id="26", block="q8", text=
        "{t}A última é *com você.* [p=0.4] {a}O *carbono-catorze* [p=0.2] tem meia-vida de cerca de *cinco mil, "
        "setecentos e trinta anos.* [p=0.3] A *datação por carbono-catorze* [p=0.2] usa isso para descobrir a idade de "
        "restos de seres vivos. [p=0.3] Um pedaço de madeira tem *um dezesseis avos* [p=0.2] do carbono-catorze de uma "
        "madeira viva. [p=0.3] A idade dele, em anos, é: [p=0.3] {qa}A: [p=0.2] mil, quatrocentos e trinta e dois vírgula "
        "cinco. [p=0.2] {qb}B: [p=0.2] onze mil, quatrocentos e sessenta. [p=0.2] {qc}C: [p=0.2] dezessete mil, cento e "
        "noventa. [p=0.2] {qd}D: [p=0.2] vinte e dois mil, novecentos e vinte. [p=0.2] {qe}E: [p=0.2] noventa e um mil, "
        "seiscentos e oitenta. [p=0.5] {p}*Pause o vídeo e tente sozinho.* [p=2.5]"),
    dict(id="27", block="q8", text=
        "{t}Confira. [p=0.3] {a}É o caminho *inverso:* [p=0.2] deram a fração, [p=0.2] pedem o tempo. [p=0.4] {b}Os "
        "cortes do dezesseis: [p=0.2] oito, quatro, dois, um. [p=0.2] *Quatro* meias-vidas. [p=0.3] Repare na ordem: [p=0.2] primeiro os intervalos, [p=0.2] depois a conta. "
        "[p=0.4] {c}Quatro vezes cinco "
        "mil, setecentos e trinta: [p=0.2] *vinte e dois mil, novecentos e vinte anos.* [p=0.4] {d}Faz sentido? [p=0.2] "
        "Sobrou pouquinho, [p=0.2] então passou *muito* tempo. [p=0.3] {ok}*Letra D!*"),
    dict(id="28", block="q8", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A *divide* a meia-vida por quatro, [p=0.2] em vez de multiplicar. [p=0.4] "
        "{xb}A B conta só *duas* meias-vidas. [p=0.3] {xc}A C, *três.* [p=0.4] {xe}E a E multiplica por *dezesseis:* "
        "[p=0.2] trata o denominador como número de meias-vidas. [p=0.3] Dezesseis meias-vidas [p=0.2] deixariam uma "
        "fração *minúscula* do carbono."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="29", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] primeiro conte os intervalos, [p=0.2] depois "
        "escreva a potência. [p=0.5] {b}Dois: [p=0.2] cada meia-vida corta pela metade [p=0.2] o que existe naquele "
        "momento. [p=0.5] {c}Três: [p=0.2] duplicações se multiplicam: [p=0.2] seis dobras são vezes sessenta e quatro, "
        "[p=0.2] não vezes doze."),

    # ================= PONTE E CTA =================
    dict(id="30", block="ponte", text=
        "{a}O perfil *A* ganha *trezentos seguidores* por semana. [p=0.4] {b}O perfil *B* só *dobra,* [p=0.2] mas começa "
        "com *cem.* [p=0.4] {c}Quem vence, [p=0.2] e *quando?* [p=0.4] {d}Próximo episódio."),
    dict(id="31", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha ouvido falar do *césio de Goiânia?* "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
