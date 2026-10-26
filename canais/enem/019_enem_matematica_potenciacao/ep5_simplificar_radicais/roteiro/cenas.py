# Roteiro — Potenciação e Radiciação, Episódio 5 de 7: Simplificar radicais e fazer contas com raízes (aula para iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/04-potenciacao-radiciacao.html — seções 07 e 08 (+ Questões 4 e 5 da seção 12).
# Raízes de índices diferentes (√2 · ∛2) ficam para o ep6 (expoente fracionário): aqui só se cita.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   PORTA DA RAIZ: a raiz quadrada é uma porta em que os fatores só saem em DUPLA; cada par sai como UM só; quem está
#   sozinho fica lá dentro (na raiz cúbica, saem em TRIO).
#   FRUTAS: √2 é a "fruta": 5√2 + 2√2 − 3√2 é 5 maçãs + 2 maçãs − 3 maçãs; maçã com laranja não vira "maranja".
# Termos definidos na hora: simplificar, quadrado perfeito, cubo perfeito, coeficiente, radicais semelhantes, forma final.
# Atalhos (verde): "desça a lista dos quadrados perfeitos: o primeiro que divide é o maior" · "confira elevando ao quadrado:
#   (5√2)² = 5² · 2 = 50" · "dupla sai na quadrada, trio na cúbica; quem sobra fica" · "some só os da frente, a fruta fica" ·
#   "mesmo índice: junte tudo numa raiz só".
# DESVIOS do prompt para não entregar as respostas das questões antes da hora (o prompt usava os próprios números das questões):
#   bloco f) usa √12 + √27 = 2√3 + 3√3 = 5√3 (o √50 + √8 − √18 fica para a Questão 5);
#   erro 1 usa √12 + √27 = √39 (somou os radicandos); erro 3 usa √72 = 2√18 (parou antes; forma final 6√2).
#   Teste do erro 2 (2√3 + 3√2 = 5√5), com raízes exatas: 2√9 + 3√4 = 6 + 6 = 12; a "regra" daria 5√13, e √13 > 3, mais de 15.
# QUESTÃO 4 do material (texto idêntico na tela): √180 = √(36 · 5) = 6√5 → B.
#   A (3√20) e D (2√45): valor certo, mas não simplificadas (explicação do material).
#   Explicações NOSSAS: C (9√2): conferindo, 9² · 2 = 162, não 180 · E (18√10): partiu 180 em 18 · 10 e tirou o 18 sem tirar a
#   raiz dele; conferindo, 18² · 10 = 3 240.
# QUESTÃO 5 do material: √50 + √8 − √18 = 5√2 + 2√2 − 3√2 = 4√2 → C.
#   A (√40): somou os radicandos, 50 + 8 − 18 (explicação do material).
#   Explicações NOSSAS: D (10√2) = 5 + 2 + 3, ignorou o sinal de menos · B (2√2) = 5 − 3, esqueceu o √8 ·
#   E (4√10): acertou o 4, mas trocou a fruta; radicais semelhantes conservam o radicando (√2).
# Exercício "nós fazemos": √48 = 4√3 · √75 = 5√3 · soma = 9√3.
# Frases-chave (meio e fim, idênticas):
#   1. Da raiz quadrada, os fatores saem em dupla.
#   2. Só se somam raízes iguais: mesmo índice e mesmo radicando.
#   3. Simplifique antes de dizer que não dá.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "√50 = 5√2: simplificar raízes e somar radicais do zero | Potenciação Ep. 5"
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
        "{a}Você faz a conta, [p=0.2] chega na resposta certa: [p=0.2] *raiz de cinquenta.* [p=0.4] {b}Procura nas "
        "alternativas [p=0.2] e ela *não está lá.* [p=0.5] {c}Muitas vezes ela está, sim. [p=0.3] {d}Só que escrita de um "
        "jeito mais simples: [p=0.2] *cinco raiz de dois.* [p=0.5] {e}Hoje você aprende a *simplificar raízes.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai *simplificar qualquer raiz,* [p=0.3] {b}e saber quando dá, [p=0.2] e quando "
        "*não dá,* [p=0.2] para *somar raízes.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}Fatorar em primos é quebrar um número em multiplicações [p=0.2] até só "
        "sobrar primo: [p=0.2] doze é dois vezes dois vezes três. [p=0.4] {b}Quadrado perfeito é um número que é outro "
        "número ao quadrado: [p=0.2] quatro, [p=0.1] nove, [p=0.1] dezesseis, [p=0.1] vinte e cinco, [p=0.1] trinta e seis. "
        "[p=0.4] {c}E do episódio quatro: [p=0.2] a raiz de um produto [p=0.2] é o produto das raízes."),

    # ================= BLOCO A: MÉTODO 1, O MAIOR QUADRADO PERFEITO =================
    dict(id="04", block="simplificar", text=
        "{t}Primeiro, o que é *simplificar* uma raiz? [p=0.4] {a}É tirar de dentro da raiz [p=0.2] tudo o que consegue sair. "
        "[p=0.4] {b}O número *não muda* de valor: [p=0.2] só fica escrito de um jeito mais simples. [p=0.4] {c}Raiz de "
        "cinquenta [p=0.2] e cinco raiz de dois [p=0.2] são *o mesmo número.*"),
    dict(id="05", block="metodo1", text=
        "{t}E como se faz? [p=0.3] {a}Procure um *quadrado perfeito* [p=0.2] que divida o cinquenta. [p=0.4] {b}Vinte e cinco "
        "divide: [p=0.2] cinquenta é vinte e cinco vezes dois. [p=0.4] {c}Raiz de cinquenta [p=0.2] vira raiz de vinte e cinco, "
        "[p=0.2] vezes raiz de dois. [p=0.4] {d}Raiz de vinte e cinco é cinco. [p=0.3] {e}Resultado: [p=0.2] *cinco raiz de "
        "dois.*"),
    dict(id="06", block="metodo1", text=
        "{t}Esse cinco na frente tem nome: [p=0.2] *coeficiente.* [p=0.3] {a}É o número que fica do lado de fora, [p=0.2] "
        "multiplicando a raiz. [p=0.4] {b}Cinco raiz de dois quer dizer [p=0.2] *cinco vezes* raiz de dois. [p=0.3] O sinal de "
        "vezes só fica escondido."),
    dict(id="07", block="maior", text=
        "{t}Agora, raiz de setenta e dois. [p=0.3] Qual quadrado perfeito divide setenta e dois? [p=0.4] {a}O quatro divide. "
        "[p=0.2] O nove divide. [p=0.2] O trinta e seis também! [p=0.4] {b}Use sempre o *maior:* [p=0.2] setenta e dois é "
        "trinta e seis vezes dois. [p=0.4] {c}Raiz de trinta e seis é seis. [p=0.3] {d}Resultado: [p=0.2] *seis raiz de "
        "dois.*"),
    dict(id="08", block="maior", text=
        "{t}E como achar o maior sem chutar? [p=0.3] {a}Atalho: [p=0.2] *desça a lista* dos quadrados perfeitos. [p=0.4] {b}Cem, "
        "[p=0.1] oitenta e um, [p=0.1] sessenta e quatro, [p=0.1] quarenta e nove, [p=0.1] trinta e seis. [p=0.4] {c}O primeiro "
        "que dividir [p=0.2] é o maior. [p=0.3] {d}Para cento e oitenta: [p=0.2] cem não divide, [p=0.2] oitenta e um não, "
        "[p=0.2] sessenta e quatro não, [p=0.2] quarenta e nove não, [p=0.2] trinta e seis *divide.* [p=0.4] {e}Raiz de cento "
        "e oitenta [p=0.2] é *seis raiz de cinco.*"),
    dict(id="09", block="confere", text=
        "{t}E um segundo atalho, [p=0.2] para conferir: [p=0.2] *eleve ao quadrado.* [p=0.4] {a}Cinco raiz de dois, ao "
        "quadrado, [p=0.2] é cinco ao quadrado [p=0.2] vezes raiz de dois ao quadrado. [p=0.4] {b}O expoente de fora pega os "
        "dois fatores, [p=0.2] lembra do episódio dois? [p=0.4] {c}Cinco ao quadrado é vinte e cinco. [p=0.2] Raiz de dois ao "
        "quadrado é dois, [p=0.2] porque o quadrado desfaz a raiz. [p=0.4] {d}Vinte e cinco vezes dois: [p=0.2] *cinquenta.* "
        "[p=0.3] Voltou ao número de dentro. [p=0.2] Está certo."),

    # ================= BLOCO B: MÉTODO 2, A PORTA DA RAIZ =================
    dict(id="10", block="porta", text=
        "{t}E quando o quadrado perfeito não salta aos olhos? [p=0.4] {a}Fatore em primos. [p=0.3] Cento e oitenta: [p=0.2] "
        "{b}dividido por dois, [p=0.2] noventa. [p=0.2] Por dois, [p=0.2] quarenta e cinco. [p=0.2] Por três, [p=0.2] quinze. "
        "[p=0.2] Por três, [p=0.2] cinco. [p=0.4] {c}Cento e oitenta [p=0.2] é dois, [p=0.1] dois, [p=0.1] três, [p=0.1] três "
        "[p=0.1] e cinco, [p=0.2] tudo multiplicado."),
    dict(id="11", block="porta", text=
        "{t}Agora imagine a raiz como uma *casinha.* [p=0.3] {a}Os fatores ficam lá dentro. [p=0.4] {b}E a porta tem uma regra: "
        "[p=0.2] só sai quem está em *dupla.* [p=0.4] {c}Os dois dois formam uma dupla: [p=0.2] *sai um dois só.* [p=0.4] {d}Os "
        "dois três formam outra: [p=0.2] *sai um três.* [p=0.4] {e}O cinco está sozinho: [p=0.2] *fica dentro.*"),
    dict(id="12", block="porta", text=
        "{t}Lá fora, [p=0.2] quem saiu se multiplica: [p=0.3] {a}dois vezes três, [p=0.2] *seis.* [p=0.4] {b}E dentro ficou o "
        "cinco. [p=0.3] {c}Seis raiz de cinco, [p=0.2] o mesmo resultado do outro método. [p=0.4] {d}Por que a dupla sai como "
        "um só? [p=0.3] Porque raiz de dois vezes dois [p=0.2] é raiz de quatro, [p=0.2] que é *dois.* [p=0.3] Cada dupla é um "
        "quadrado perfeito escondido."),
    dict(id="13", block="porta72", text=
        "{t}Vamos conferir com o setenta e dois. [p=0.3] {a}Setenta e dois [p=0.2] é dois, [p=0.1] dois, [p=0.1] dois, [p=0.1] "
        "três [p=0.1] e três. [p=0.4] {b}Uma dupla de dois sai: [p=0.2] um dois. [p=0.3] {c}A dupla de três sai: [p=0.2] um "
        "três. [p=0.3] {d}Sobrou um dois sozinho, [p=0.2] que fica dentro. [p=0.4] {e}Dois vezes três, [p=0.2] seis, [p=0.2] "
        "raiz de dois: [p=0.2] *seis raiz de dois.* [p=0.3] Bate com o método um."),

    # ================= BLOCO C: RAIZ CÚBICA, SAEM EM TRIO =================
    dict(id="14", block="cubica", text=
        "{t}E na raiz *cúbica?* [p=0.3] {a}A porta fica mais exigente: [p=0.2] só sai quem está em *trio.* [p=0.4] {b}Raiz "
        "cúbica de cinquenta e quatro. [p=0.3] Cinquenta e quatro [p=0.2] é dois, [p=0.1] três, [p=0.1] três [p=0.1] e três. "
        "[p=0.4] {c}O trio de três sai como *um três.* [p=0.3] {d}O dois fica. [p=0.4] {e}Resultado: [p=0.2] *três raiz cúbica "
        "de dois.*"),
    dict(id="15", block="cubica", text=
        "{t}Pelo método um, [p=0.2] você procura um *cubo perfeito:* [p=0.2] um número que é outro ao cubo, [p=0.2] como oito, "
        "[p=0.1] vinte e sete, [p=0.1] sessenta e quatro. [p=0.4] {a}Cinquenta e quatro é vinte e sete vezes dois, [p=0.2] e a "
        "raiz cúbica de vinte e sete é três. [p=0.4] {b}Atalho da porta: [p=0.2] na quadrada sai em *dupla,* [p=0.2] na cúbica "
        "sai em *trio.* [p=0.2] Quem sobra, [p=0.2] fica."),

    # ================= BLOCO D: SOMAR SÓ RADICAIS SEMELHANTES =================
    dict(id="16", block="frutas", text=
        "{t}Agora, somar raízes. [p=0.3] Começa pela feira. [p=0.4] {a}Duas maçãs mais cinco maçãs: [p=0.2] *sete maçãs.* "
        "[p=0.4] {b}E duas maçãs mais três laranjas? [p=0.3] {c}Não viram cinco *maranjas.* [p=0.3] Continuam duas maçãs e três "
        "laranjas. [p=0.4] {d}Só dá para juntar o que é *igual.*"),
    dict(id="17", block="semelhantes", text=
        "{t}Com raiz é igualzinho. [p=0.3] {a}Em duas raiz de três [p=0.2] mais cinco raiz de três, [p=0.2] a raiz de três é a "
        "*fruta.* [p=0.4] {b}Duas frutas mais cinco frutas: [p=0.2] *sete raiz de três.* [p=0.4] {c}Raízes assim, com o *mesmo "
        "índice* e o *mesmo radicando,* [p=0.2] se chamam *radicais semelhantes.* [p=0.4] {d}Atalho: [p=0.2] some só os "
        "coeficientes, [p=0.2] os números da frente. [p=0.2] A fruta fica igual."),
    dict(id="18", block="naosoma", text=
        "{t}E raiz de dois mais raiz de três? [p=0.4] {a}Frutas diferentes. [p=0.2] Não tem o que somar. [p=0.3] {b}A conta já "
        "está na *forma final:* [p=0.2] o jeito mais simples possível de escrever. [p=0.4] {c}E duas raiz de três [p=0.2] mais "
        "três raiz de dois [p=0.2] *nunca* dá cinco raiz de cinco. [p=0.4] {d}Teste com raízes exatas: [p=0.2] duas raiz de "
        "nove, mais três raiz de quatro, [p=0.2] dá seis mais seis, [p=0.2] *doze.* [p=0.3] {e}A regra falsa daria cinco raiz "
        "de treze, [p=0.2] e raiz de treze já passa de três: [p=0.2] mais de *quinze.* [p=0.3] Não confere."),
    dict(id="19", block="antes", text=
        "{t}Mas cuidado: [p=0.2] às vezes as frutas *parecem* diferentes [p=0.2] e não são. [p=0.4] {a}Raiz de doze mais raiz "
        "de vinte e sete. [p=0.3] Parece que não dá. [p=0.4] {b}Simplifique primeiro: [p=0.2] raiz de doze [p=0.2] é *duas* raiz "
        "de três. [p=0.3] {c}Raiz de vinte e sete [p=0.2] é *três* raiz de três. [p=0.4] {d}Agora é a mesma fruta: [p=0.2] dois "
        "mais três, [p=0.2] *cinco raiz de três.* [p=0.4] {e}Simplifique *antes* de dizer que não dá."),

    # ================= BLOCO G: MULTIPLICAR E DIVIDIR COM O MESMO ÍNDICE =================
    dict(id="20", block="multiplicar", text=
        "{t}E multiplicar? [p=0.3] Essa é mais fácil. [p=0.3] {a}Raiz de três vezes raiz de doze: [p=0.2] com o mesmo índice, "
        "[p=0.2] junte tudo numa raiz só. [p=0.4] {b}Raiz de três vezes doze, [p=0.2] raiz de trinta e seis: [p=0.2] *seis.* "
        "[p=0.4] {c}Dividir, [p=0.2] a mesma coisa: [p=0.2] raiz de dezoito dividido por raiz de dois [p=0.2] é raiz de nove, "
        "[p=0.2] *três.* [p=0.4] {d}E se os índices forem diferentes, [p=0.2] como raiz de dois vezes raiz cúbica de dois? "
        "[p=0.3] Isso tem um truque próprio, [p=0.2] no episódio seis."),

    # ================= EXERCÍCIO "NÓS FAZEMOS" =================
    dict(id="21", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Simplifique raiz de quarenta e oito [p=0.3] {b}e raiz de setenta e cinco. [p=0.4] {p}*Pause o "
        "vídeo e calcule.* [p=2.5]"),
    dict(id="22", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Quarenta e oito é dezesseis vezes três: [p=0.2] *quatro raiz de três.* [p=0.4] {b}Setenta "
        "e cinco é vinte e cinco vezes três: [p=0.2] *cinco raiz de três.* [p=0.4] {c}E agora, [p=0.2] *some os dois.* [p=0.3] "
        "Repare: [p=0.2] a fruta é a mesma, raiz de três. [p=0.4] {d}Quatro mais cinco: [p=0.2] *nove raiz de três.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="23", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] da raiz quadrada, os fatores saem em dupla. [p=0.5] {b}Dois: "
        "[p=0.2] só se somam raízes iguais: [p=0.2] mesmo índice e mesmo radicando. [p=0.5] {c}Três: [p=0.2] simplifique antes "
        "de dizer que não dá."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="24", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] somar os radicandos. [p=0.2] Raiz de doze mais raiz de "
        "vinte e sete [p=0.2] virar raiz de trinta e nove. [p=0.4] {b}Parece certo, [p=0.2] porque na multiplicação dá para "
        "juntar numa raiz só. [p=0.4] {c}Mas na soma, não: [p=0.2] simplifique e some as frutas. [p=0.2] Dá cinco raiz de "
        "três."),
    dict(id="25", block="erros", text=
        "{a}Segundo: [p=0.2] duas raiz de três [p=0.2] mais três raiz de dois [p=0.2] igual a cinco raiz de cinco. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque somar o de fora com o de fora e o de dentro com o de dentro [p=0.2] parece "
        "organizado. [p=0.4] {c}Mas são frutas diferentes: [p=0.2] a conta já está pronta."),
    dict(id="26", block="erros", text=
        "{a}Terceiro: [p=0.2] parar no meio. [p=0.2] Raiz de setenta e dois [p=0.2] igual a duas raiz de dezoito. [p=0.4] "
        "{b}Parece certo, [p=0.2] e o *valor* até está certo. [p=0.4] {c}Mas o dezoito ainda tem uma dupla de três dentro. "
        "[p=0.2] A forma final é *seis raiz de dois.*"),

    # ================= QUESTÃO 4 DO MATERIAL =================
    dict(id="27", block="q4", text=
        "{t}Agora, duas questões no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}A forma simplificada de "
        "raiz de cento e oitenta é: [p=0.4] {qa}A: [p=0.2] três raiz de vinte. [p=0.3] {qb}B: [p=0.2] seis raiz de cinco. "
        "[p=0.3] {qc}C: [p=0.2] nove raiz de dois. [p=0.3] {qd}D: [p=0.2] duas raiz de quarenta e cinco. [p=0.3] {qe}E: "
        "[p=0.2] dezoito raiz de dez. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="28", block="q4", text=
        "{t}Vamos resolver. [p=0.3] {a}Desça a lista dos quadrados perfeitos: [p=0.2] o primeiro que divide cento e oitenta "
        "[p=0.2] é o *trinta e seis.* [p=0.4] {b}Cento e oitenta é trinta e seis vezes cinco. [p=0.3] {c}Raiz de trinta e seis "
        "é seis: [p=0.2] *seis raiz de cinco.* [p=0.3] {ok}*Letra B!*"),
    dict(id="29", block="q4", text=
        "{t}E as outras? [p=0.3] {xa}A A e a D têm o *valor certo,* [p=0.2] mas não estão simplificadas: [p=0.2] o vinte e o "
        "quarenta e cinco ainda têm uma dupla dentro. [p=0.2] {xd}A prova sempre quer a forma final. [p=0.4] {xc}A C, nove raiz "
        "de dois: [p=0.2] confira elevando ao quadrado. [p=0.2] Oitenta e um vezes dois dá cento e sessenta e dois, [p=0.2] e não "
        "cento e oitenta. [p=0.4] {xe}A E partiu cento e oitenta em dezoito vezes dez, [p=0.2] e tirou o dezoito sem tirar a "
        "raiz dele."),

    # ================= QUESTÃO 5 DO MATERIAL =================
    dict(id="30", block="q5", text=
        "{t}E a segunda. [p=0.3] {a}O valor de raiz de cinquenta [p=0.2] mais raiz de oito [p=0.2] menos raiz de dezoito é: "
        "[p=0.4] {qa}A: [p=0.2] raiz de quarenta. [p=0.3] {qb}B: [p=0.2] duas raiz de dois. [p=0.3] {qc}C: [p=0.2] quatro raiz "
        "de dois. [p=0.3] {qd}D: [p=0.2] dez raiz de dois. [p=0.3] {qe}E: [p=0.2] quatro raiz de dez. [p=0.5] {p}*Pause o vídeo e "
        "tente.* [p=2.0]"),
    dict(id="31", block="q5", text=
        "{t}Parecem três frutas diferentes. [p=0.3] Simplifique antes. [p=0.4] {a}Raiz de cinquenta [p=0.2] é cinco raiz de "
        "dois. [p=0.3] {b}Raiz de oito, [p=0.2] quatro vezes dois, [p=0.2] é duas raiz de dois. [p=0.3] {c}Raiz de dezoito, "
        "[p=0.2] nove vezes dois, [p=0.2] é três raiz de dois. [p=0.4] {d}Agora é tudo raiz de dois: [p=0.2] cinco mais dois "
        "menos três, [p=0.2] *quatro raiz de dois.* [p=0.3] {ok}*Letra C!*"),
    dict(id="32", block="q5", text=
        "{t}E as outras? [p=0.3] {xa}A A somou os radicandos: [p=0.2] cinquenta mais oito menos dezoito, [p=0.2] quarenta. "
        "[p=0.2] É o erro mais comum aqui. [p=0.4] {xd}A D somou tudo [p=0.2] e ignorou o sinal de menos. [p=0.3] {xb}A B "
        "esqueceu a raiz de oito. [p=0.3] {xe}E a E acertou o quatro, [p=0.2] mas trocou a fruta: [p=0.2] na soma de "
        "semelhantes, [p=0.2] o de dentro *não muda.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="33", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] da raiz quadrada, os fatores saem em dupla. [p=0.5] "
        "{b}Dois: [p=0.2] só se somam raízes iguais: [p=0.2] mesmo índice e mesmo radicando. [p=0.5] {c}Três: [p=0.2] "
        "simplifique antes de dizer que não dá."),

    # ================= PONTE E CTA =================
    dict(id="34", block="ponte", text=
        "{a}E quando a raiz está no *denominador,* [p=0.2] tipo um sobre raiz de dois? [p=0.3] {b}A prova quase sempre quer "
        "*sem raiz embaixo.* [p=0.4] {c}E como multiplicar raiz de dois [p=0.2] por raiz cúbica de dois? [p=0.4] {d}Próximo "
        "episódio: [p=0.2] *dois truques.*"),
    dict(id="35", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quanto deu raiz de quarenta e oito mais raiz de setenta e cinco para você? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
