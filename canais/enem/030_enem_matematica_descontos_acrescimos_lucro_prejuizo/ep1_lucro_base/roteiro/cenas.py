# Roteiro — Descontos, Acréscimos, Lucro e Prejuízo, Episódio 1 de 4: lucro e prejuízo, porcentagem de quê? Margem e preço
# Base: Estudos/Enem/estudos/01-matematica/15-descontos-acrescimos-lucro-prejuizo.html — seções 03, 04 e 05 + Questões 1, 2
#   e 7 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   TODA PORCENTAGEM TEM DONO: antes de calcular, pergunte "por cento DE QUÊ?" (do custo, da venda, da etiqueta).
#   O PREÇO DE VENDA É UMA PIZZA: uma fatia é lucro, o resto paga o custo; a fatia nunca é a pizza inteira (margem < 100%).
#   MARKUP é o que se põe EM CIMA do custo (pode ser 150%, 300%); MARGEM SOBRE A VENDA é o pedaço DENTRO do preço.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos do prompt: 80 → 100 (25% do custo, 20% da venda) · 120 → 90 (prejuízo de 25% do custo, ≈ 33,3% da venda) ·
#   "vender pelo dobro" (100% sobre o custo, 50% sobre a venda) · conversões 0,25 ÷ 1,25 = 0,20 e 0,20 ÷ 0,80 = 0,25 ·
#   custo 72 com 20% (72 · 1,20 = 86,40 sobre o custo; 72 ÷ 0,80 = 90 sobre a venda; 18 ÷ 90 = 20%).
# Exemplo NOSSO no bloco g (imposto e comissão): o prompt usa 510 ÷ 0,85 = 600, que são exatamente os números da Questão 7
#   ("você faz") e entregariam metade da resposta (600 − 90 = 510). Aqui: o revendedor de aplicativo paga 15% de taxa sobre
#   cada venda e quer receber R$ 340,00 → 340 ÷ 0,85 = R$ 400,00 (15% de 400 = 60; 400 − 60 = 340).
# Erro 3 (pontos percentuais) com números NOSSOS, para não entregar a C da Questão 7: custo 100, venda 140 (40% sobre o
#   custo), 10% de imposto sobre a venda (14) → lucro líquido 26 = 26% do custo, não 40 − 10 = 30%.
# Erro 2 usa os números do prompt (custo 60, 25% sobre a venda → 80, não 75), que são os da Questão 2 ("nós fazemos"): mantido
#   como o prompt pede; a Questão 2 refaz o raciocínio com o aluno.
# Nós fazemos (prompt): custo 50, venda 80 → lucro 30; 60% sobre o custo; 37,5% sobre a venda; 0,6 ÷ 1,6 = 0,375.
# QUESTÃO 1 (eu faço): 30 ÷ 120 = 25% → B. Erradas (material e prompt): A 30 ÷ 150 = 20% (base venda); C confunde R$ 30 com
#   30%; D 120 ÷ 150 = 80% (custo/venda); E 150 ÷ 120 = 1,25 lido como 125% (venda/custo).
# QUESTÃO 2 (nós fazemos): 0,75 · V = 60 → V = 80 → C; conferência 20 ÷ 80 = 25%. Erradas (material): A 60 · 0,75 = 45;
#   B 60 · 1,25 = 75 (lucro 15 = 20% de 75); D 60 + 25 = 85; E 60 ÷ 0,25 = 240.
# QUESTÃO 7 (você faz): 15% de 600 = 90; 600 − 90 = 510; 510 − 400 = 110; 110 ÷ 400 = 27,5% → B. Erradas (material):
#   A 110 ÷ 600 ≈ 18%; C 50 − 15 = 35 (pontos de bases diferentes); D 50 · 0,85 = 42,5 (15% sobre a margem); E 50% bruto.
# Atalhos (verde): "invente o custo 100" (converte margens sem fórmula) · "sobre a venda: divida o custo pela fatia que
#   sobra (1 − m)" · "confira em reais: lucro ÷ base".
# Frases-chave (meio e fim, idênticas): 1. Toda porcentagem tem dono: escreva a base antes de calcular.
#   2. Margem sobre o custo, multiplique; margem sobre a venda, divida por 1 − m. 3. Lucro sobre a venda nunca chega a 100%.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Lucro de 25% ou de 20%? A pegadinha da BASE | Descontos e Lucro Ep. 1"
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
        "{a}Comprei por *oitenta reais* [p=0.2] e vendi por *cem reais.* [p=0.4] {b}Lucrei *vinte e cinco por cento* "
        "[p=0.2] ou *vinte por cento?* [p=0.5] {c}As duas respostas estão certas, [p=0.2] e o ENEM coloca as duas nas "
        "alternativas. [p=0.4] {d}Só uma responde à pergunta que ele fez."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai calcular lucro e prejuízo *na base certa* [p=0.3] {b}e formar o preço "
        "de venda para qualquer margem, [p=0.2] {c}sem cair na *armadilha da base.*"),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes da série de Porcentagem. [p=0.3] {a}Que porcentagem a parte representa? [p=0.2] *Divida a "
        "parte pelo todo.* [p=0.4] {b}E o *fator:* [p=0.2] aumentar vinte por cento [p=0.2] é multiplicar por *um "
        "vírgula vinte.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Pense em três balcões. [p=0.3] {a}Uma *mochila* comprada por oitenta [p=0.2] e vendida por cem. [p=0.4] "
        "{b}Uma *artesã* decidindo o preço de uma peça. [p=0.4] {c}Um revendedor de *aplicativo,* [p=0.2] que paga "
        "taxa sobre cada venda. [p=0.4] {d}A pergunta é a mesma: [p=0.2] *quanto eu ganho?*"),

    # ================= BLOCO A: CUSTO, VENDA, LUCRO =================
    dict(id="05", block="definicao", text=
        "{t}Como se mede o ganho? [p=0.4] {a}*Preço de custo* [p=0.2] é quanto o comerciante pagou. [p=0.3] "
        "{b}*Preço de venda* [p=0.2] é quanto o cliente paga. [p=0.4] {c}*Lucro* é a diferença: [p=0.2] venda menos "
        "custo. [p=0.3] Cem menos oitenta: [p=0.2] *vinte reais* de lucro."),
    dict(id="06", block="definicao", text=
        "{t}E se a venda ficar abaixo do custo? [p=0.4] {a}A conta dá negativa: [p=0.2] *prejuízo,* [p=0.2] o "
        "dinheiro que se perdeu. [p=0.4] {b}Em reais, [p=0.2] não há dúvida. [p=0.3] {c}A confusão aparece quando o "
        "lucro vira *porcentagem.*"),

    # ================= BLOCO B: O MESMO LUCRO EM DUAS BASES =================
    dict(id="07", block="base", text=
        "{t}Vinte reais de lucro [p=0.2] são quantos por cento? [p=0.4] {a}*Por cento de quê?* "
        "[p=0.4] {b}Comparando com o *custo,* [p=0.2] vinte dividido por oitenta: [p=0.2] *vinte e cinco por cento "
        "do custo.* [p=0.4] {c}Comparando com a *venda,* [p=0.2] vinte dividido por cem: [p=0.2] *vinte por cento da "
        "venda.* [p=0.4] {d}Um lucro, [p=0.2] duas porcentagens."),
    dict(id="08", block="base", text=
        "{t}Guarde a regra desta aula. [p=0.3] {a}*Toda porcentagem tem dono.* [p=0.2] O dono se chama *base:* "
        "[p=0.2] o valor que fica embaixo, na divisão. [p=0.4] {b}Sem aviso, [p=0.2] a base é o *custo.* [p=0.4] "
        "{c}Mas o ENEM costuma *dizer:* [p=0.2] *do custo* [p=0.2] ou *da venda.*"),

    # ================= BLOCO C: PREJUÍZO TAMBÉM TEM BASE =================
    dict(id="09", block="prejuizo", text=
        "{t}E o prejuízo, [p=0.2] tem dono? [p=0.4] {a}Comprou por *cento e vinte,* [p=0.2] "
        "vendeu por *noventa.* [p=0.2] Prejuízo de *trinta reais.* [p=0.4] {b}Sobre o custo: [p=0.2] trinta dividido "
        "por cento e vinte, [p=0.2] *vinte e cinco por cento.* [p=0.4] {c}Sobre a venda: [p=0.2] trinta dividido por "
        "noventa, [p=0.2] cerca de *trinta e três por cento.* [p=0.4] {d}Salvo aviso, [p=0.2] vale o *custo.*"),

    # ================= BLOCO D: MARKUP × MARGEM SOBRE A VENDA =================
    dict(id="10", block="pizza", text=
        "{t}Quem vende pelo dobro [p=0.2] lucra cem por cento? [p=0.4] {a}Comprou por cinquenta, [p=0.2] vendeu por "
        "cem: [p=0.2] *cem por cento* em cima do custo. [p=0.2] Isso é o *markup:* [p=0.2] o que se põe *em cima* do "
        "custo. [p=0.4] {b}Agora olhe o preço de venda como uma *pizza:* [p=0.2] uma fatia é lucro, [p=0.2] o resto "
        "paga o custo. [p=0.4] {c}Aqui o lucro é *metade* da pizza. [p=0.2] *Cinquenta por cento* de *margem sobre a "
        "venda:* [p=0.2] o pedaço *dentro* do preço."),
    dict(id="11", block="pizza", text=
        "{t}Qual das duas é maior? [p=0.4] {a}A margem sobre a venda é *sempre a menor,* [p=0.2] porque a venda é "
        "maior que o custo. [p=0.4] {b}E a fatia do lucro *nunca* é a pizza inteira: [p=0.2] *nunca chega a cem por "
        "cento.* [p=0.4] {c}Já o markup é uma pilha em cima do custo: [p=0.2] cento e cinquenta, [p=0.2] trezentos por "
        "cento."),

    # ================= BLOCO E: CONVERTER AS MARGENS =================
    dict(id="12", block="converter", text=
        "{t}Dá para passar de uma margem para a outra? [p=0.4] {a}Dá, com as taxas em decimal. [p=0.2] *Sobre a "
        "venda* [p=0.2] é *sobre o custo* [p=0.2] dividido por *um mais* ele. [p=0.2] Zero vírgula vinte e cinco "
        "[p=0.2] dividido por um vírgula vinte e cinco: [p=0.2] *zero vírgula vinte.* [p=0.4] {b}De volta: [p=0.2] "
        "*sobre o custo* [p=0.2] é *sobre a venda* [p=0.2] dividido por *um menos* ela. [p=0.2] Zero vírgula vinte por "
        "zero vírgula oitenta: [p=0.2] *zero vírgula vinte e cinco.*"),
    dict(id="13", block="atalho1", text=
        "{t}Esqueceu a fórmula? [p=0.4] {a}Atalho: [p=0.2] *invente um custo de cem reais.* [p=0.4] {b}Markup de vinte "
        "e cinco por cento: [p=0.2] venda de cento e vinte e cinco, [p=0.2] lucro de vinte e cinco. [p=0.4] {c}Sobre a "
        "venda: [p=0.2] vinte e cinco de cento e vinte e cinco, [p=0.2] *vinte por cento.* [p=0.4] {d}Com cem, [p=0.2] "
        "cabe de cabeça."),

    # ================= BLOCO F: FORMAR O PREÇO =================
    dict(id="14", block="preco", text=
        "{t}Custo de *setenta e dois reais,* [p=0.2] margem de *vinte por cento.* [p=0.2] Qual é o preço? [p=0.4] "
        "{a}Pergunte: [p=0.2] vinte por cento *de quê?* [p=0.4] {b}Se for *sobre o custo,* "
        "[p=0.2] é um acréscimo: [p=0.2] *multiplique* pelo fator. [p=0.2] Setenta e dois vezes um vírgula vinte: "
        "[p=0.2] *oitenta e seis reais e quarenta.*"),
    dict(id="15", block="preco", text=
        "{t}E se for *sobre a venda?* [p=0.4] {a}Volte para a pizza. [p=0.2] Se vinte por cento do preço é lucro, "
        "[p=0.2] os outros *oitenta por cento* são o custo. [p=0.4] {b}Então oitenta por cento do preço [p=0.2] valem "
        "setenta e dois reais. [p=0.2] Para achar o preço, [p=0.2] *divida:* [p=0.2] setenta e dois dividido por zero "
        "vírgula oitenta, [p=0.2] *noventa reais.* [p=0.4] {c}Confira: [p=0.2] lucro de dezoito, [p=0.2] e dezoito "
        "de noventa [p=0.2] é *vinte por cento.*"),
    dict(id="16", block="atalho2", text=
        "{t}Como lembrar qual conta fazer? [p=0.4] {a}Atalho: [p=0.2] *sobre a venda, [p=0.2] divida o custo pela "
        "fatia que sobra:* [p=0.2] *um menos a margem.* [p=0.4] {b}Margem de vinte: [p=0.2] divida por zero vírgula "
        "oitenta. [p=0.2] De vinte e cinco: [p=0.2] por zero vírgula setenta e cinco. [p=0.4] {c}E confira em reais: "
        "[p=0.2] *lucro dividido pela base pedida.*"),

    # ================= BLOCO G: IMPOSTO E COMISSÃO =================
    dict(id="17", block="imposto", text=
        "{t}E o revendedor de aplicativo? [p=0.4] {a}Imposto e comissão sobre a venda [p=0.2] funcionam *do mesmo "
        "jeito.* [p=0.2] *Comissão* é a parte do preço que fica com quem intermediou. [p=0.4] {b}Se *quinze por cento* "
        "do preço vai embora, [p=0.2] ele fica com *oitenta e cinco.* [p=0.4] {c}Para receber *trezentos e quarenta "
        "reais,* [p=0.2] divida por zero vírgula oitenta e cinco: [p=0.2] *quatrocentos reais.* [p=0.4] {d}Confira: "
        "[p=0.2] quinze por cento de quatrocentos é sessenta, [p=0.2] e sobram trezentos e quarenta."),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Um produto custa *cinquenta reais* [p=0.2] e é vendido por *oitenta reais.* [p=0.4] "
        "{b}Qual é o lucro *sobre o custo,* [p=0.2] e qual é o lucro *sobre a venda?* [p=0.4] {c}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Lucro em reais: [p=0.2] oitenta menos cinquenta, [p=0.2] *trinta.* [p=0.4] "
        "{b}Sobre o custo: [p=0.2] trinta dividido por cinquenta, [p=0.2] *sessenta por cento.* [p=0.4] {c}Sobre a "
        "venda: [p=0.2] trinta dividido por oitenta, [p=0.2] *trinta e sete e meio por cento.* [p=0.4] {d}Pela "
        "conversão: [p=0.2] zero vírgula seis por um vírgula seis [p=0.2] dá zero vírgula trezentos e setenta e cinco. "
        "[p=0.2] Bateu."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] toda porcentagem tem dono: [p=0.2] escreva a base "
        "antes de calcular. [p=0.5] {b}Dois: [p=0.2] margem sobre o custo, multiplique; [p=0.2] margem sobre a venda, "
        "divida por um menos m. [p=0.5] {c}Três: [p=0.2] lucro sobre a venda nunca chega a cem por cento."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] pedir o lucro *sobre a venda* [p=0.2] e "
        "dividir pelo *custo.* [p=0.4] {b}Parece certo, [p=0.2] porque o custo é a base de sempre. [p=0.4] {c}Mas "
        "vinte reais numa venda de cem [p=0.2] são *vinte por cento da venda* [p=0.2] e *vinte e cinco do custo.*"),
    dict(id="22", block="erros", text=
        "{a}Segundo: [p=0.2] margem *sobre a venda* [p=0.2] *multiplicando* o custo. [p=0.4] {b}Parece certo: [p=0.2] "
        "sessenta mais vinte e cinco por cento, [p=0.2] setenta e cinco, rapidinho. [p=0.4] {c}Mas o lucro de quinze "
        "é só vinte por cento de setenta e cinco. [p=0.2] *Divida:* [p=0.2] sessenta por zero vírgula setenta e cinco, "
        "[p=0.2] *oitenta.*"),
    dict(id="23", block="erros", text=
        "{a}Terceiro: [p=0.2] descontar o imposto da margem [p=0.2] em *pontos percentuais.* [p=0.4] {b}Parece certo: "
        "[p=0.2] lucro de quarenta, [p=0.2] imposto de dez, [p=0.2] sobram trinta. [p=0.4] {c}Mas o imposto é sobre a "
        "*venda,* [p=0.2] e o lucro, sobre o *custo.* [p=0.2] Custo cem, venda cento e quarenta, imposto de catorze: "
        "[p=0.2] lucro de *vinte e seis por cento.* [p=0.2] *Calcule em reais.*"),
    dict(id="24", block="erros", text=
        "{a}Quarto: [p=0.2] aceitar margem *sobre a venda acima de cem por cento.* [p=0.4] {b}Parece possível, [p=0.2] "
        "porque markup de cento e vinte e cinco existe. [p=0.4] {c}Mas a fatia nunca é maior que a pizza: [p=0.2] "
        "*elimine* antes de qualquer conta."),

    # ================= QUESTÃO 1 (EU FAÇO) =================
    dict(id="25", block="q1", text=
        "{t}Agora, questões no estilo do ENEM. [p=0.2] Esta, [p=0.2] eu resolvo com você. [p=0.4] {a}Um comerciante comprou uma mochila por *cento e vinte reais* [p=0.2] e a vendeu por *cento e "
        "cinquenta.* [p=0.2] O lucro obtido, [p=0.2] *em relação ao preço de custo,* [p=0.2] foi de: [p=0.4] {qa}A: "
        "[p=0.2] vinte por cento. [p=0.3] {qb}B: [p=0.2] vinte e cinco. [p=0.3] {qc}C: [p=0.2] trinta. [p=0.3] {qd}D: "
        "[p=0.2] oitenta. [p=0.3] {qe}E: [p=0.2] cento e vinte e cinco por cento. [p=0.5] {p}*Pause o vídeo e tente.* "
        "[p=2.0]"),
    dict(id="26", block="q1", text=
        "{t}Sublinhe o dono: [p=0.2] *preço de custo.* [p=0.4] {a}Lucro em reais: [p=0.2] "
        "cento e cinquenta menos cento e vinte, [p=0.2] *trinta reais.* [p=0.4] {b}Sobre o custo: [p=0.2] trinta "
        "dividido por cento e vinte, [p=0.2] *vinte e cinco por cento.* [p=0.3] {ok}*Letra B!*"),
    dict(id="27", block="q1", text=
        "{t}E as outras? [p=0.3] {xa}A A dividiu pela *venda:* [p=0.2] base que a questão não pediu. [p=0.4] {xc}A C "
        "confunde *trinta reais* com trinta por cento. [p=0.4] {xd}A D é *custo sobre venda:* [p=0.2] cento e vinte por "
        "cento e cinquenta. [p=0.4] {xe}E a E é *venda sobre custo:* [p=0.2] o fator um vírgula vinte e cinco [p=0.2] "
        "lido como cento e vinte e cinco por cento."),

    # ================= QUESTÃO 2 (NÓS FAZEMOS) =================
    dict(id="28", block="q2", text=
        "{t}Agora, *nós* fazemos. [p=0.3] {a}Uma artesã gasta *sessenta reais* para produzir cada peça. [p=0.2] Ela "
        "quer que o lucro corresponda a *vinte e cinco por cento do preço de venda.* [p=0.2] O preço de venda de cada "
        "peça deve ser: [p=0.4] {qa}A: [p=0.2] quarenta e cinco reais. [p=0.3] {qb}B: [p=0.2] setenta e cinco. "
        "[p=0.3] {qc}C: [p=0.2] oitenta. [p=0.3] {qd}D: [p=0.2] oitenta e cinco. [p=0.3] {qe}E: [p=0.2] duzentos e "
        "quarenta reais. [p=0.5] {p}*Pause e tente.* [p=2.0]"),
    dict(id="29", block="q2", text=
        "{t}Quem é o dono? [p=0.2] *O preço de venda.* [p=0.2] Então é a pizza. [p=0.4] {a}Se vinte e cinco por cento "
        "do preço é lucro, [p=0.2] os outros *setenta e cinco por cento* pagam o custo. [p=0.4] {b}Divida: [p=0.2] "
        "sessenta dividido por zero vírgula setenta e cinco, [p=0.2] *oitenta reais.* [p=0.4] {c}Confira: [p=0.2] "
        "lucro de vinte, [p=0.2] e vinte dividido por oitenta [p=0.2] dá vinte e cinco por cento. [p=0.3] {ok}*Letra "
        "C!*"),
    dict(id="30", block="q2", text=
        "{t}As armadilhas. [p=0.3] {xb}A B somou vinte e cinco por cento *ao custo:* [p=0.2] é o erro número dois. "
        "[p=0.4] {xd}A D somou *vinte e cinco reais.* [p=0.4] {xa}A A multiplicou por zero vírgula setenta e cinco, "
        "[p=0.2] {xe}e a E dividiu por zero vírgula vinte e cinco: [p=0.2] *fatias erradas* da pizza."),

    # ================= QUESTÃO 7 (VOCÊ FAZ) =================
    dict(id="31", block="q7", text=
        "{t}E a última é *sua.* [p=0.3] {a}Um revendedor compra um produto por *quatrocentos reais* [p=0.2] e o vende "
        "por *seiscentos.* [p=0.2] Sobre o preço de venda, [p=0.2] ele paga *dez por cento de imposto* [p=0.2] e *cinco "
        "por cento de comissão* ao vendedor. [p=0.2] O lucro líquido, [p=0.2] *em relação ao preço de custo,* [p=0.2] é "
        "de: [p=0.4] {qa}A: [p=0.2] cerca de dezoito por cento. [p=0.3] {qb}B: [p=0.2] vinte e sete e meio. [p=0.3] "
        "{qc}C: [p=0.2] trinta e cinco. [p=0.3] {qd}D: [p=0.2] quarenta e dois e meio. [p=0.3] {qe}E: [p=0.2] cinquenta "
        "por cento. [p=0.5] {p}*Pause e resolva.* [p=2.5]"),
    dict(id="32", block="q7", text=
        "{t}Conferindo. [p=0.2] *Lucro líquido* é o que sobra no fim. [p=0.4] {a}Imposto e "
        "comissão somam quinze por cento *da venda:* [p=0.2] quinze por cento de seiscentos, [p=0.2] *noventa reais.* "
        "[p=0.4] {b}Ficam seiscentos menos noventa, [p=0.2] *quinhentos e dez.* [p=0.2] Lucro líquido: [p=0.2] "
        "quinhentos e dez menos quatrocentos, [p=0.2] *cento e dez reais.* [p=0.4] {c}Sobre o custo: [p=0.2] cento e "
        "dez dividido por quatrocentos, [p=0.2] *vinte e sete e meio por cento.* [p=0.3] {ok}*Letra B!*"),
    dict(id="33", block="q7", text=
        "{t}E as erradas? [p=0.3] {xc}A C fez cinquenta menos quinze: [p=0.2] pontos de *bases diferentes,* [p=0.2] o "
        "erro número três. [p=0.4] {xa}A A dividiu pela *venda.* [p=0.4] {xe}A E é o lucro *bruto,* [p=0.2] sem "
        "descontar nada. [p=0.4] {xd}E a D tirou quinze por cento *da margem:* [p=0.2] oitenta e cinco por cento de "
        "cinquenta."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="34", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] toda porcentagem tem dono: [p=0.2] escreva a "
        "base antes de calcular. [p=0.5] {b}Dois: [p=0.2] margem sobre o custo, multiplique; [p=0.2] margem sobre a "
        "venda, divida por um menos m. [p=0.5] {c}Três: [p=0.2] lucro sobre a venda nunca chega a cem por cento."),

    # ================= PONTE E CTA =================
    dict(id="35", block="ponte", text=
        "{a}Uma loja dá *vinte por cento* de liquidação, [p=0.2] mais *cinco* no Pix, [p=0.2] e cobra *dez por cento* "
        "de frete. [p=0.5] {b}No fim, [p=0.2] você paga *quinze por cento a menos?* [p=0.5] {c}Próximo episódio."),
    dict(id="36", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já vendeu alguma coisa? [p=0.2] Quanto lucrou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
