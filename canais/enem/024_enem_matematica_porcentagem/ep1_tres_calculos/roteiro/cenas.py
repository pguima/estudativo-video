# Roteiro — Porcentagem, Episódio 1 de 6: Os três cálculos básicos de porcentagem e a conta de cabeça
# Base: Estudos/Enem/estudos/01-matematica/09-porcentagem.html — seções 02 e 03 (esta só em revisão relâmpago) + Questão 1.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O TRIÂNGULO da porcentagem: PARTE em cima; TOTAL e TAXA embaixo. Tape com o dedo o que você quer achar.
#   O denominador é sempre de ONDE VOCÊ PARTIU (o todo, ou o valor inicial).
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte.
# Exemplos: blocos a) e b) usam os do material (15% de 200 = 30; 30 ÷ 200 = 15%). O bloco c) do prompt (45 ÷ 0,15 = 300) é a
#   própria Questão 1; foi trocado por 18 ÷ 0,15 = 120 (conferência: 15% de 120 = 18), para a Q1 continuar sendo "pause e tente".
# Revisão relâmpago da seção 03 (série de Frações): só 25% = ÷ 4; 20% = ÷ 5; 12,5% = ÷ 8, exemplos com 200 (50; 40; 25).
# Nós fazemos (prompt): 10% de 350 = 35 · 5% de 80 = 4 · 15% de 60 = 6 + 3 = 9 · 25% de 48 = 48 ÷ 4 = 12.
# QUESTÃO 1 do material (texto idêntico na tela): pergunta do 3º tipo; 45 ÷ 0,15 = 300; conferência 15% de 300 = 45 → D.
#   Material: E (675) = multiplicou 45 por 15 em vez de dividir por 0,15.
#   Explicações NOSSAS: A (60) = somou 45 + 15, juntou os dois números do enunciado; B (150) e C (270) caem na conferência:
#   15% de 150 = 22,5 e 15% de 270 = 40,5, nenhum dá 45.
# Atalhos (verde): "qual das três? 'x% DE' → multiplica · 'que parte representa' → parte ÷ total · 'é x% de QUANTO' → divide" ·
#   "confira voltando ao enunciado" · "10%: vírgula uma casa; 1%: duas; 5%: metade dos 10%; 15% = 10% + 5%" ·
#   "25% = ÷ 4 · 20% = ÷ 5 · 12,5% = ÷ 8".
# Frases-chave (meio e fim, idênticas): 1. Três perguntas: a parte, a taxa ou o total.
#   2. O denominador é sempre de onde você partiu. 3. 10% é andar a vírgula uma casa.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Porcentagem do zero: os três cálculos básicos e a conta de cabeça | Porcentagem Ep. 1"
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
        "{a}Porcentagem não é um assunto entre outros: [p=0.3] {b}é uma *língua* que atravessa a prova inteira, [p=0.2] "
        "de Matemática a Biologia e Geografia. [p=0.5] {c}E toda questão dela começa com uma de apenas *três perguntas.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai reconhecer qual das três perguntas a questão está fazendo [p=0.3] "
        "{b}e calcular *dez, cinco, quinze e um por cento* de cabeça."),
    dict(id="03", block="prereq", text=
        "{t}Antes, um lembrete rápido da série de Frações. [p=0.3] {a}*Por cento* quer dizer *a cada cem.* [p=0.3] "
        "Quinze por cento é quinze de cada cem: [p=0.2] *quinze sobre cem.* [p=0.4] {b}E dá para escrever com vírgula: "
        "[p=0.2] é só dividir por cem, [p=0.2] andando a vírgula duas casas. [p=0.3] Quinze por cento [p=0.2] vira "
        "*zero vírgula quinze.* [p=0.3] {c}Essa é a *forma decimal.*"),

    # ================= CONCRETO: TRÊS SITUAÇÕES =================
    dict(id="04", block="cotidiano", text=
        "{t}Três cenas do dia a dia. [p=0.3] {a}No restaurante, [p=0.2] a conta veio com *dez por cento* de gorjeta. [p=0.2] "
        "Quanto é isso, em reais? [p=0.4] {b}Na prova, [p=0.2] você acertou *dezoito* de *vinte* questões. [p=0.2] Que "
        "porcentagem é essa? [p=0.4] {c}Na loja, [p=0.2] o gerente vendeu uma parte do estoque [p=0.2] e sabe quanto ela "
        "representa. [p=0.2] Quantas peças havia no começo?"),
    dict(id="05", block="cotidiano", text=
        "{t}Repare nas três peças de toda conta de porcentagem. [p=0.3] {a}O *total* é o todo, [p=0.2] o valor de "
        "referência: [p=0.2] de onde a conta parte. [p=0.4] {b}A *parte* é um pedaço desse todo. [p=0.4] {c}E a *taxa* é "
        "a porcentagem, [p=0.2] o *por cento.* [p=0.4] {d}Em cada cena falta *uma* das três. [p=0.3] E é aí que nascem as "
        "três perguntas."),

    # ================= BLOCO A: PERGUNTA 1 =================
    dict(id="06", block="p1", text=
        "{t}Pergunta um: [p=0.2] *quanto é* quinze por cento *de* duzentos? [p=0.4] {a}Aqui você tem o total e a taxa, "
        "[p=0.2] e quer a parte. [p=0.4] {b}Troque a taxa pela forma decimal: [p=0.2] zero vírgula quinze. [p=0.3] {c}E "
        "*multiplique:* [p=0.2] zero vírgula quinze vezes duzentos [p=0.2] dá *trinta.* [p=0.4] {d}Por que multiplicar? "
        "[p=0.2] Porque é quinze de cada cem, [p=0.2] e duzentos tem *dois* cens: [p=0.2] quinze mais quinze, trinta."),

    # ================= BLOCO B: PERGUNTA 2 =================
    dict(id="07", block="p2", text=
        "{t}Pergunta dois: [p=0.2] trinta, [p=0.2] de um total de duzentos, [p=0.2] *que porcentagem* representa? [p=0.4] "
        "{a}Agora você tem a parte e o total, [p=0.2] e quer a taxa. [p=0.4] {b}*Divida* a parte pelo total: [p=0.2] trinta "
        "dividido por duzentos [p=0.2] dá *zero vírgula quinze.* [p=0.4] {c}Volte para a porcentagem [p=0.2] andando a "
        "vírgula duas casas para a direita: [p=0.2] *quinze por cento.*"),

    # ================= BLOCO C: PERGUNTA 3 =================
    dict(id="08", block="p3", text=
        "{t}Pergunta três: [p=0.2] dezoito é quinze por cento *de quanto?* [p=0.4] {a}Agora você tem a parte e a taxa, "
        "[p=0.2] e quer o *total.* [p=0.4] {b}*Divida* a parte pela forma decimal: [p=0.2] dezoito dividido por zero vírgula "
        "quinze [p=0.2] dá *cento e vinte.* [p=0.4] {c}E confira voltando ao enunciado: [p=0.2] quinze por cento de cento e "
        "vinte [p=0.2] é *dezoito?* [p=0.3] Dez por cento é doze, [p=0.2] cinco por cento é seis: [p=0.2] *dezoito.* "
        "[p=0.2] Fecha!"),

    # ================= BLOCO D: O TRIÂNGULO =================
    dict(id="09", block="triangulo", text=
        "{t}E agora, [p=0.2] um desenho que junta as três. [p=0.4] {a}O *triângulo* da porcentagem: [p=0.2] *parte* em cima. "
        "[p=0.3] *Total* e *taxa* embaixo. [p=0.4] {b}Tape com o dedo o que você quer achar. [p=0.3] {c}Tapou a parte? "
        "[p=0.2] Sobra total *vezes* taxa. [p=0.4] {d}Tapou a taxa? [p=0.2] Sobra parte *dividido* pelo total. [p=0.4] "
        "{e}Tapou o total? [p=0.2] Sobra parte *dividido* pela taxa."),
    dict(id="10", block="triangulo", text=
        "{t}Na prova, [p=0.2] as palavras do enunciado entregam qual peça está faltando. [p=0.4] {a}Atalho: [p=0.2] "
        "*tantos por cento de* alguma coisa? [p=0.2] Multiplique. [p=0.4] {b}*Que parte representa?* [p=0.2] Divida a parte "
        "pelo total. [p=0.4] {c}*É tantos por cento de quanto?* [p=0.2] Divida pela taxa. [p=0.4] {d}E no fim, [p=0.2] "
        "sempre volte ao enunciado para conferir."),

    # ================= BLOCO E: O DENOMINADOR =================
    dict(id="11", block="denominador", text=
        "{t}Agora, o erro que mais derruba. [p=0.3] {a}Um preço sobe de *quarenta* para *cinquenta* reais. [p=0.2] Quanto "
        "por cento subiu? [p=0.4] {b}Isso é uma *variação percentual:* [p=0.2] quanto a mudança representa do valor que "
        "você tinha. [p=0.4] {c}A diferença é dez. [p=0.2] E você partiu de quarenta: [p=0.2] dez dividido por quarenta, "
        "[p=0.2] *vinte e cinco por cento.*"),
    dict(id="12", block="denominador", text=
        "{t}E se o preço *cair* de cinquenta para quarenta? [p=0.4] {a}A diferença é a mesma: [p=0.2] dez. [p=0.3] {b}Mas "
        "agora você partiu de *cinquenta:* [p=0.2] dez dividido por cinquenta, [p=0.2] *vinte por cento.* [p=0.4] {c}Mesma "
        "diferença, [p=0.2] *bases* diferentes. [p=0.4] {d}A regra: [p=0.2] o denominador é sempre de onde você partiu."),

    # ================= BLOCO F: CONTA DE CABEÇA =================
    dict(id="13", block="mental", text=
        "{t}E dá para fazer de cabeça? [p=0.3] Dá! [p=0.3] {a}Dez por cento é dividir por dez: [p=0.2] é só andar a "
        "vírgula *uma casa* para a esquerda. [p=0.3] Dez por cento de duzentos e quarenta: [p=0.2] *vinte e quatro.* "
        "[p=0.4] {b}Um por cento é dividir por cem: [p=0.2] *duas casas.* [p=0.3] Um por cento de duzentos e quarenta: "
        "[p=0.2] *dois vírgula quatro.*"),
    dict(id="14", block="mental", text=
        "{t}E daí sai o resto. [p=0.3] {a}Cinco por cento [p=0.2] é a *metade* dos dez por cento. [p=0.3] A metade de "
        "vinte e quatro: [p=0.2] *doze.* [p=0.4] {b}E quinze por cento [p=0.2] é dez mais cinco: [p=0.2] vinte e quatro "
        "mais doze, [p=0.2] *trinta e seis.* [p=0.4] {c}Atalho: [p=0.2] *ache os dez por cento primeiro.* [p=0.2] Todo o "
        "resto se monta a partir dele."),

    # ================= BLOCO G: REVISÃO RELÂMPAGO DAS FRAÇÕES =================
    dict(id="15", block="fracoes", text=
        "{t}E uma revisão relâmpago da série de Frações. [p=0.3] {a}*Vinte e cinco por cento* é um quarto: [p=0.2] é "
        "*dividir por quatro.* [p=0.2] Vinte e cinco por cento de duzentos: [p=0.2] cinquenta. [p=0.4] {b}*Vinte por "
        "cento* é um quinto: [p=0.2] divida por cinco. [p=0.2] Quarenta. [p=0.4] {c}E *doze e meio por cento* é um oitavo: "
        "[p=0.2] divida por oito. [p=0.2] Vinte e cinco."),

    # ================= NÓS FAZEMOS (JOGO) =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez, [p=0.2] em ritmo de jogo. [p=0.3] Quatro contas de cabeça. [p=0.3] {a}Dez por cento de trezentos e "
        "cinquenta. [p=0.3] {b}Cinco por cento de oitenta. [p=0.3] {c}Quinze por cento de sessenta. [p=0.3] {d}Vinte e "
        "cinco por cento de quarenta e oito. [p=0.4] {e}*Pause o vídeo e calcule.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Dez por cento de trezentos e cinquenta: [p=0.2] vírgula uma casa, [p=0.2] *trinta "
        "e cinco.* [p=0.4] {b}Cinco por cento de oitenta: [p=0.2] dez por cento é oito, [p=0.2] a metade, [p=0.2] "
        "*quatro.* [p=0.4] {c}Quinze por cento de sessenta: [p=0.2] seis mais três, [p=0.2] *nove.* [p=0.4] {d}Vinte e "
        "cinco por cento de quarenta e oito: [p=0.2] dividido por quatro, [p=0.2] *doze.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] três perguntas: [p=0.2] a parte, a taxa ou o total. "
        "[p=0.5] {b}Dois: [p=0.2] o denominador é sempre de onde você partiu. [p=0.5] {c}Três: [p=0.2] dez por cento é "
        "andar a vírgula uma casa."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] usar o *valor final* como denominador numa "
        "variação. [p=0.4] {b}Parece certo, [p=0.2] porque o valor final é o mais recente, [p=0.2] o que está na sua "
        "frente. [p=0.4] {c}Mas a variação se mede a partir de onde você *partiu:* [p=0.2] o valor inicial vai embaixo."),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] *multiplicar* quando deveria *dividir* para achar o total. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque multiplicar foi o que você fez na primeira pergunta. [p=0.4] {c}Mas, quando falta o total, [p=0.2] tape o "
        "total no triângulo: [p=0.2] sobra parte *dividido* pela taxa. [p=0.3] E confira: [p=0.2] o total tem que ser maior "
        "que a parte."),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] achar que subir de quarenta para cinquenta [p=0.2] e cair de cinquenta para quarenta [p=0.2] "
        "são a *mesma porcentagem.* [p=0.4] {b}Parece certo, [p=0.2] porque a diferença é a mesma: [p=0.2] dez. [p=0.4] "
        "{c}Mas as bases são diferentes: [p=0.2] subir é *vinte e cinco* por cento, [p=0.2] cair é *vinte.*"),

    # ================= QUESTÃO 1 DO MATERIAL =================
    dict(id="22", block="q1", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}Uma loja vendeu "
        "*quarenta e cinco* unidades de um produto em um dia, [p=0.2] o que corresponde a *quinze por cento* de todo o "
        "estoque disponível. [p=0.4] {b}O estoque inicial dessa loja era de: [p=0.4] {qa}A: [p=0.2] sessenta unidades. "
        "[p=0.3] {qb}B: [p=0.2] cento e cinquenta. [p=0.3] {qc}C: [p=0.2] duzentas e setenta. [p=0.3] {qd}D: [p=0.2] "
        "trezentas. [p=0.3] {qe}E: [p=0.2] seiscentas e setenta e cinco. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="23", block="q1", text=
        "{t}Vamos resolver. [p=0.3] {a}Primeiro: [p=0.2] qual das três perguntas? [p=0.3] Temos a parte, [p=0.2] quarenta "
        "e cinco, [p=0.2] e a taxa, [p=0.2] quinze por cento. [p=0.3] Falta o *total.* [p=0.2] É a pergunta três. [p=0.4] "
        "{b}Tape o total: [p=0.2] parte dividido pela taxa. [p=0.3] Quarenta e cinco dividido por zero vírgula quinze [p=0.2] "
        "dá *trezentos.* [p=0.4] {c}Confira: [p=0.2] quinze por cento de trezentos. [p=0.2] Dez por cento é trinta, "
        "[p=0.2] cinco por cento é quinze: [p=0.2] *quarenta e cinco.* [p=0.2] Fecha! [p=0.3] {ok}*Letra D!*"),
    dict(id="24", block="q1", text=
        "{t}E as outras? [p=0.3] {xe}A E, [p=0.2] seiscentas e setenta e cinco, [p=0.2] é de quem *multiplicou* quarenta e "
        "cinco por quinze, [p=0.2] em vez de dividir. [p=0.4] {xa}A A juntou os dois números do enunciado: [p=0.2] "
        "quarenta e cinco mais quinze. [p=0.4] {xb}A B [p=0.2] {xc}e a C caem na conferência: [p=0.2] quinze por cento "
        "delas não dá quarenta e cinco."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="25", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] três perguntas: [p=0.2] a parte, a taxa ou o total. "
        "[p=0.5] {b}Dois: [p=0.2] o denominador é sempre de onde você partiu. [p=0.5] {c}Três: [p=0.2] dez por cento é "
        "andar a vírgula uma casa."),

    # ================= PONTE E CTA =================
    dict(id="26", block="ponte", text=
        "{a}E para *aumentar* ou dar *desconto?* [p=0.3] {b}Muita gente calcula a parte e depois soma. [p=0.4] {c}Existe "
        "um jeito com *uma multiplicação só,* [p=0.2] e ele é a chave de todo este assunto. [p=0.4] {d}Próximo episódio."),
    dict(id="27", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quanto deu quinze por cento de sessenta para você? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
