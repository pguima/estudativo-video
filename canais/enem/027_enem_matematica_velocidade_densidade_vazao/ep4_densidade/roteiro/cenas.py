# Roteiro — Velocidade, Densidade e Vazão, Episódio 4 de 6: densidade — identificar o material e decidir se ele flutua
# Base: Estudos/Enem/estudos/01-matematica/12-velocidade-densidade-vazao.html — seção 05 + Questões 3 e 4 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   Densidade é o quanto de massa está "ESPREMIDO" em cada centímetro cúbico.
#   Densidade é a IMPRESSÃO DIGITAL do material: um prego e um portão de ferro têm a mesma (Química 011).
#   A ÁGUA É A RÉGUA da flutuação: menor que 1 g/cm³ boia, maior que 1 afunda.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte.
# Pré-requisitos: as três perguntas da taxa (ep. 1 desta série: taxa → divida; numerador → multiplique; denominador →
#   divida ao contrário) e, da série de Unidades, 1 mL = 1 cm³, 1 L de água = 1 kg, 1 g/cm³ = 1 000 kg/m³.
# Exemplos NOSSOS (conferidos em Python):
#   prego 3,9 g em 0,5 cm³ = 7,8 g/cm³ · portão 78 kg = 78 000 g em 10 000 cm³ = 7,8 g/cm³;
#   erro 3 (dividir para achar a massa): 200 cm³ de óleo 0,8 → certo 160 g, errado 200 ÷ 0,8 = 250 g
#   (números próprios para não entregar a Questão 4, que é "nós fazemos").
#   erro 2: ferro "7,8 kg/m³" seria 1 m³ (mil litros) de ferro pesando 7,8 kg; o certo é 7 800 kg/m³.
# Nós fazemos (prompt): 27 g em 10 cm³ → 2,7 g/cm³ → alumínio → afunda (2,7 > 1).
# QUESTÃO 3 (texto idêntico na tela): 156 ÷ 20 = 7,8 g/cm³ → ferro → B. 312 g em 40 cm³ = 7,8 (material).
#   Explicação NOSSA das outras (o material só diz que são outros materiais): pelo volume de 20 cm³, alumínio pesaria 54 g,
#   chumbo 226 g, ouro 386 g; e o gelo (E) pesaria 18,4 g, menos que os 20 g de água do mesmo volume.
# QUESTÃO 4 (texto idêntico): m = d · V = 0,92 · 500 = 460 g → C. Conferência de sentido (material): 500 cm³ de água = 500 g;
#   gelo é menos denso, então pesa menos. E (543 g) = dividiu 500 por 0,92 (material). Explicações do prompt:
#   A (0,46 g) e B (46 g) erram a vírgula; D (500 g) usa a densidade da água.
# Você faz (prompt): 1 L de óleo (0,8 g/cm³) = 1 000 cm³ · 0,8 = 800 g.
# Atalhos (verde): o triângulo da densidade (tampe o que você procura) · comparar com 1 (a régua da água) ·
#   "1 L de um material de densidade d pesa d kg" (o mesmo volume de água como referência).
# Frases-chave (meio e fim, idênticas): 1. Densidade é massa sobre volume. 2. A densidade é do material, não da quantidade.
#   3. Menor que a água boia; maior afunda.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Densidade do zero: descubra o material e se ele boia · Matemática ENEM, Velocidade, densidade e vazão ep. 4"

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
        "{a}Um objeto de *cento e cinquenta e seis gramas* [p=0.2] ocupa *vinte centímetros cúbicos.* [p=0.4] {b}Com uma "
        "divisão você descobre que ele é de *ferro,* [p=0.2] e não de alumínio, [p=0.2] chumbo [p=0.2] ou ouro. [p=0.4] "
        "{c}A balança e uma régua [p=0.2] fazem o trabalho de um *laboratório.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, você vai *calcular densidade,* [p=0.3] {b}achar a *massa* a partir do volume [p=0.3] {c}e decidir "
        "se algo *flutua* [p=0.2] só comparando números."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] toda taxa responde a *três perguntas.* "
        "[p=0.2] Quer a taxa? [p=0.2] *Divida.* [p=0.2] Quer o número de cima? [p=0.2] *Multiplique.* [p=0.2] Quer o de "
        "baixo? [p=0.2] *Divida ao contrário.* [p=0.4] {b}E da série de Unidades: [p=0.2] um mililitro é *um centímetro "
        "cúbico,* [p=0.2] e *um litro de água pesa um quilo.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Uma pergunta velha: [p=0.2] o que pesa mais, [p=0.2] um quilo de *chumbo* [p=0.2] ou um quilo de *algodão?* "
        "[p=0.5] {a}Pesam *igual:* [p=0.2] um quilo é um quilo. [p=0.4] {b}Mas olhe o *tamanho* de cada um. [p=0.2] O "
        "chumbo cabe na mão. [p=0.2] O algodão enche um saco enorme. [p=0.4] {c}A mesma massa, [p=0.2] em espaços *muito*"
        " diferentes."),
    dict(id="05", block="concreto", text=
        "{t}E tem mais. [p=0.3] {a}O cubo de *gelo* [p=0.2] fica boiando no copo. [p=0.4] {b}O *óleo* da panela [p=0.2] "
        "fica sempre *por cima* da água. [p=0.4] {c}O que decide quem sobe [p=0.2] e quem desce? [p=0.3] {d}Um número só:"
        " [p=0.2] a *densidade.*"),

    # ================= BLOCO A: DEFINIÇÃO =================
    dict(id="06", block="definicao", text=
        "{a}*Massa* [p=0.2] é a quantidade de matéria, [p=0.2] o que a balança mede: [p=0.2] em gramas ou quilos. [p=0.4]"
        " {b}*Volume* [p=0.2] é o espaço que o objeto ocupa: [p=0.2] em centímetros cúbicos, [p=0.2] ou litros. [p=0.4] "
        "{c}Um *centímetro cúbico* [p=0.2] é um cubinho de um centímetro de lado, [p=0.2] do tamanho de um dado pequeno."),
    dict(id="07", block="definicao", text=
        "{t}E o que é densidade? [p=0.4] {a}*Densidade é massa dividida por volume.* [p=0.2] *d* igual a *m* sobre *V.* "
        "[p=0.4] {b}É o quanto de massa está *espremido* em cada centímetro cúbico. [p=0.4] {c}A unidade conta a "
        "história: [p=0.2] *grama por centímetro cúbico.* [p=0.2] Quantos gramas cabem num cubinho."),
    dict(id="08", block="atalho", text=
        "{t}E se a questão pedir a massa, [p=0.2] ou o volume? [p=0.4] {a}Atalho: [p=0.2] o *triângulo da densidade.* "
        "[p=0.2] Massa em cima; [p=0.2] densidade e volume embaixo. [p=0.4] {b}Tampe com o dedo o que você procura. "
        "[p=0.3] Tampou a densidade? [p=0.2] Sobra *m sobre V.* [p=0.3] {c}Tampou a massa? [p=0.2] Sobra *d vezes V.* "
        "[p=0.3] {d}Tampou o volume? [p=0.2] Sobra *m sobre d.* [p=0.4] {e}As três perguntas da taxa, [p=0.2] num desenho"
        " só."),

    # ================= BLOCO B: IMPRESSÃO DIGITAL =================
    dict(id="09", block="digital", text=
        "{t}Um portão de ferro é *mais denso* que um prego de ferro? [p=0.4] {a}O prego: [p=0.2] *três vírgula nove "
        "gramas* [p=0.2] em *meio centímetro cúbico.* [p=0.2] Dá *sete vírgula oito.* [p=0.4] {b}O portão: [p=0.2] "
        "*setenta e oito quilos,* [p=0.2] em *dez mil centímetros cúbicos.* [p=0.2] Setenta e oito mil gramas dividido "
        "por dez mil: [p=0.2] *sete vírgula oito.* [p=0.4] {c}*Igual.*"),
    dict(id="10", block="digital", text=
        "{t}Por quê? [p=0.3] {a}Porque massa e volume crescem *juntos.* [p=0.4] {b}Densidade é a *impressão digital* do "
        "material, [p=0.2] como você viu em Química: [p=0.2] não depende da quantidade."),

    # ================= BLOCO C: A TABELA =================
    dict(id="11", block="tabela", text=
        "{t}E a impressão digital de cada um? [p=0.4] {a}Do mais leve ao mais pesado: [p=0.3] *óleo,* [p=0.2] zero "
        "vírgula oito. [p=0.2] *Gelo,* [p=0.2] zero vírgula noventa e dois. [p=0.2] *Água,* [p=0.2] um. [p=0.2] *Água do "
        "mar,* [p=0.2] um vírgula zero três. [p=0.4] {b}*Alumínio,* [p=0.2] dois vírgula sete. [p=0.2] *Ferro,* [p=0.2] "
        "sete vírgula oito. [p=0.2] *Chumbo,* [p=0.2] onze vírgula três. [p=0.2] *Ouro,* [p=0.2] dezenove vírgula três."),

    # ================= BLOCO D: FLUTUAÇÃO =================
    dict(id="12", block="flutua", text=
        "{t}E quem boia? [p=0.4] {a}*Flutuar* [p=0.2] é ficar na superfície, [p=0.2] sem ir para o fundo. [p=0.4] {b}A "
        "regra: [p=0.2] *flutua quem tem densidade menor que a do líquido.* [p=0.2] Quem tem densidade maior [p=0.2] "
        "afunda. [p=0.4] {c}Na água, [p=0.2] a régua é o *um.* [p=0.2] Menor que um, [p=0.2] boia. [p=0.2] Maior que um, "
        "[p=0.2] afunda."),
    dict(id="13", block="flutua", text=
        "{t}Vamos jogar tudo num aquário. [p=0.3] {a}O *óleo,* zero vírgula oito: [p=0.2] *boia.* [p=0.4] {b}O *gelo,* "
        "zero vírgula noventa e dois, [p=0.2] também boia, [p=0.2] mas quase todo *submerso:* [p=0.2] abaixo da linha da "
        "água. [p=0.2] Cerca de *noventa e dois por cento* do bloco fica embaixo. [p=0.4] {c}É a *ponta do iceberg.* "
        "[p=0.4] {d}Alumínio, [p=0.2] ferro, [p=0.2] chumbo, [p=0.2] ouro: [p=0.2] todos maiores que um. [p=0.2] "
        "*Afundam.*"),
    dict(id="14", block="atalho", text=
        "{t}Viu o atalho? [p=0.3] {a}Em grama por centímetro cúbico, [p=0.2] a água vale *um.* [p=0.2] Então a flutuação "
        "é só *comparar com um.* [p=0.4] {b}Zero vírgula alguma coisa: [p=0.2] boia. [p=0.2] Um vírgula alguma coisa ou "
        "mais: [p=0.2] afunda."),

    # ================= BLOCO E: A ÁGUA AMARRA TUDO =================
    dict(id="15", block="agua", text=
        "{t}E por que a água vale exatamente um? [p=0.4] {a}Porque *um grama* de água [p=0.2] ocupa *um centímetro "
        "cúbico.* [p=0.4] {b}Daí saem as outras: [p=0.2] *um litro* de água pesa *um quilo,* [p=0.2] e *um metro cúbico* "
        "pesa *uma tonelada.* [p=0.4] {c}E um grama por centímetro cúbico [p=0.2] é igual a *mil quilos por metro "
        "cúbico.*"),
    dict(id="16", block="atalho", text=
        "{t}E isso dá mais um atalho. [p=0.3] {a}Um litro de um material de densidade *d* [p=0.2] pesa *d quilos.* "
        "[p=0.4] {b}Um litro de algo com densidade dois: [p=0.2] dois quilos. [p=0.4] {c}E serve para conferir: [p=0.2] "
        "menos denso que a água, [p=0.2] pesa *menos* que a mesma quantidade de água."),

    # ================= BLOCO F: OUTRA ROUPA =================
    dict(id="17", block="demografica", text=
        "{t}E fora da física? [p=0.3] {a}*Densidade demográfica* [p=0.2] é habitantes por quilômetro quadrado. [p=0.4] "
        "{b}Não é massa, [p=0.2] mas a estrutura é a mesma: [p=0.2] quanto de uma coisa [p=0.2] por unidade de outra. "
        "[p=0.4] {c}A mesma razão, [p=0.2] com outra roupa, [p=0.2] que cai em Geografia."),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Um bloco de *dez centímetros cúbicos* [p=0.2] tem massa de *vinte e sete gramas.* [p=0.2]"
        " Qual é a densidade, [p=0.2] de que material ele é, [p=0.2] e ele boia na água? [p=0.4] {b}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}A pergunta é a taxa: [p=0.2] divida. [p=0.2] Vinte e sete gramas dividido por dez "
        "centímetros cúbicos: [p=0.2] *dois vírgula sete gramas por centímetro cúbico.* [p=0.4] {b}Na tabela, [p=0.2] "
        "dois vírgula sete é o *alumínio.* [p=0.4] {c}E boia? [p=0.2] Compare com um: [p=0.2] dois vírgula sete é maior. "
        "[p=0.2] *Afunda.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] densidade é massa sobre volume. [p=0.5] {b}Dois: [p=0.2]"
        " a densidade é do material, não da quantidade. [p=0.5] {c}Três: [p=0.2] menor que a água boia; [p=0.2] maior "
        "afunda."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que o portão é *mais denso* que o prego. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque o portão é muito mais *pesado.* [p=0.4] {c}Mas ele também é muito "
        "*maior.* [p=0.2] Massa e volume crescem juntos: [p=0.2] a densidade é a mesma, [p=0.2] sete vírgula oito."),
    dict(id="22", block="erros", text=
        "{a}Segundo: [p=0.2] tratar *grama por centímetro cúbico* [p=0.2] e *quilo por metro cúbico* como iguais. [p=0.2]"
        " O ferro com sete vírgula oito quilos por metro cúbico. [p=0.4] {b}Parece certo, [p=0.2] porque o número é o "
        "mesmo. [p=0.4] {c}Mas seria um metro cúbico de ferro, [p=0.2] mil litros, [p=0.2] pesando menos que dois sacos "
        "de arroz. [p=0.2] Para quilo por metro cúbico, [p=0.2] *vezes mil:* [p=0.2] *sete mil e oitocentos.*"),
    dict(id="23", block="erros", text=
        "{a}Terceiro: [p=0.2] *dividir* quando devia *multiplicar* ao procurar a massa. [p=0.2] Duzentos centímetros "
        "cúbicos de óleo, [p=0.2] duzentos dividido por zero vírgula oito: [p=0.2] *duzentos e cinquenta gramas.* [p=0.4]"
        " {b}Parece certo, [p=0.2] porque densidade é uma divisão. [p=0.4] {c}Mas a massa é o número de *cima:* [p=0.2] "
        "multiplique. [p=0.2] Zero vírgula oito vezes duzentos: [p=0.2] *cento e sessenta gramas.*"),

    # ================= QUESTÃO 3 (EU FAÇO) =================
    dict(id="24", block="q3", text=
        "{t}Agora, questões no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.2] Esta, [p=0.2] eu resolvo com "
        "você. [p=0.4] {a}Um objeto *maciço* [p=0.2] tem massa de *cento e cinquenta e seis gramas* [p=0.2] e ocupa um "
        "volume de *vinte centímetros cúbicos.* [p=0.2] Consultando uma tabela de densidades, [p=0.2] conclui-se que esse"
        " objeto é provavelmente de: [p=0.4] {qa}A: [p=0.2] alumínio. [p=0.3] {qb}B: [p=0.2] ferro. [p=0.3] {qc}C: "
        "[p=0.2] chumbo. [p=0.3] {qd}D: [p=0.2] ouro. [p=0.3] {qe}E: [p=0.2] gelo. [p=0.5] {p}*Pause o vídeo e tente.* "
        "[p=2.0]"),
    dict(id="25", block="q3", text=
        "{t}*Maciço* quer dizer [p=0.2] sem buraco por dentro, [p=0.2] sem ar escondido. [p=0.4] {a}A pergunta é a taxa: "
        "[p=0.2] divida. [p=0.2] Cento e cinquenta e seis gramas dividido por vinte centímetros cúbicos: [p=0.2] *sete "
        "vírgula oito gramas por centímetro cúbico.* [p=0.4] {b}Na tabela, [p=0.2] *ferro.* [p=0.4] {c}E repare: [p=0.2] "
        "um pedaço de ferro de trezentos e doze gramas [p=0.2] ocuparia quarenta centímetros cúbicos. [p=0.2] Dobrou "
        "tudo, [p=0.2] e a densidade continua *sete vírgula oito.* [p=0.3] {ok}*Letra B!*"),
    dict(id="26", block="q3", text=
        "{t}E as outras? [p=0.2] São os outros materiais da tabela. [p=0.2] Vinte centímetros cúbicos de cada um "
        "pesariam: [p=0.4] {xa}de alumínio, [p=0.2] *cinquenta e quatro gramas.* [p=0.3] {xc}De chumbo, [p=0.2] *duzentos"
        " e vinte e seis.* [p=0.3] {xd}De ouro, [p=0.2] *trezentos e oitenta e seis.* [p=0.4] {xe}E o gelo? [p=0.2] Vinte"
        " centímetros cúbicos de água pesam vinte gramas. [p=0.2] O gelo é menos denso: [p=0.2] pesaria *menos* de vinte."),

    # ================= QUESTÃO 4 (NÓS FAZEMOS) =================
    dict(id="27", block="q4", text=
        "{t}A próxima, a gente faz junto. [p=0.3] {a}Um bloco de gelo tem volume de *quinhentos centímetros cúbicos.* "
        "[p=0.2] Sabendo que a densidade do gelo é *zero vírgula noventa e dois* grama por centímetro cúbico, [p=0.2] a "
        "massa desse bloco é de: [p=0.4] {qa}A: [p=0.2] zero vírgula quarenta e seis grama. [p=0.3] {qb}B: [p=0.2] "
        "quarenta e seis. [p=0.3] {qc}C: [p=0.2] quatrocentos e sessenta. [p=0.3] {qd}D: [p=0.2] quinhentos. [p=0.3] "
        "{qe}E: [p=0.2] quinhentos e quarenta e três gramas. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="28", block="q4", text=
        "{t}A pergunta é a *massa,* [p=0.2] o número de cima: [p=0.2] multiplique. [p=0.4] {a}Massa é densidade vezes "
        "volume. [p=0.2] Zero vírgula noventa e dois vezes quinhentos: [p=0.2] *quatrocentos e sessenta gramas.* [p=0.4] "
        "{b}Agora, a conferência de sentido. [p=0.2] Quinhentos centímetros cúbicos de *água* [p=0.2] pesariam quinhentos"
        " gramas. [p=0.4] {c}O gelo é *menos* denso que a água, [p=0.2] então tem que pesar *menos* que quinhentos. "
        "[p=0.2] Quatrocentos e sessenta é menos. [p=0.2] Faz sentido. [p=0.3] {ok}*Letra C!*"),
    dict(id="29", block="q4", text=
        "{t}E as erradas? [p=0.3] {xe}A E, [p=0.2] quinhentos e quarenta e três, [p=0.2] *dividiu* quinhentos por zero "
        "vírgula noventa e dois. [p=0.2] E deu *mais* que quinhentos: [p=0.2] a própria conferência denuncia o erro. "
        "[p=0.4] {xa}A A [p=0.2] {xb}e a B [p=0.2] *erraram a vírgula.* [p=0.4] {xd}E a D, [p=0.2] quinhentos, [p=0.2] "
        "usou a densidade da *água.*"),

    # ================= VOCÊ FAZ =================
    dict(id="30", block="vocefaz", text=
        "{t}E esta é *sua.* [p=0.3] {a}*Um litro* de óleo vegetal, [p=0.2] densidade *zero vírgula oito* grama por "
        "centímetro cúbico, [p=0.2] pesa quanto? [p=0.4] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="31", block="vocefaz", text=
        "{t}Conferindo. [p=0.3] {a}Primeiro, a mesma unidade: [p=0.2] um litro são *mil centímetros cúbicos.* [p=0.4] "
        "{b}A pergunta é a massa: [p=0.2] multiplique. [p=0.2] Zero vírgula oito vezes mil: [p=0.2] *oitocentos gramas.* "
        "[p=0.4] {c}Pelo atalho: [p=0.2] um litro de densidade zero vírgula oito [p=0.2] pesa zero vírgula oito quilo. "
        "[p=0.2] Menos que o quilo da água. [p=0.2] Bateu."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="32", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] densidade é massa sobre volume. [p=0.5] {b}Dois: "
        "[p=0.2] a densidade é do material, não da quantidade. [p=0.5] {c}Três: [p=0.2] menor que a água boia; [p=0.2] "
        "maior afunda."),

    # ================= PONTE E CTA =================
    dict(id="33", block="ponte", text=
        "{a}Uma torneira enche um tanque em *seis horas;* [p=0.2] outra, em *três.* [p=0.4] {b}Juntas, enchem em *nove?* "
        "[p=0.3] Em *quatro e meia?* [p=0.4] {c}Nenhuma das duas. [p=0.4] {d}Próximo episódio: [p=0.2] *vazão.*"),
    dict(id="34", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] {com}E me conte nos "
        "*comentários:* [p=0.2] você sabia que o gelo fica noventa e dois por cento embaixo da água? [p=0.5] {anki}E tem "
        "mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no *Anki,* "
        "[p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}Bons "
        "estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
