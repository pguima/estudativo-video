# Roteiro — Porcentagem, Episódio 4 de 6: A base mudou — por que aumento e desconto iguais não se anulam, e como voltar
# ao valor original
# Base: Estudos/Enem/estudos/01-matematica/09-porcentagem.html — seções 06 e 07 (+ Questões 4, 9 e 5 da seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora (causa ÚNICA das duas seções): A BASE MUDOU — toda porcentagem é calculada sobre ALGUMA base. O aumento
#   de 20% foi sobre 100 (vale R$ 20); o desconto de 20% foi sobre 120 (vale R$ 24). Mesma taxa, bases diferentes, valores
#   diferentes. Para voltar ao original, a base também é outra → divide-se pelo fator.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte.
# Gancho e bloco a) = a própria Questão 4 ("eu faço"), por desenho do usuário.
# Blocos d) e e): NÃO usam +25% → −20% (é a Questão 5, "você faz"). Usam +50% → desconto de 1/3 ≈ 33,3%
#   (1 ÷ 1,5 = 0,666…; fórmula 50/150 = 1/3). Erro 2 (desfazer +25% com 25%) é corrigido SEM calcular os 20%.
#   Erro 4 (subtrair as taxas) é corrigido com +10% e −20% (0,88 → −12%), sem entregar a Questão 9.
# QUESTÃO 4 (eu faço): 1,20 · 0,80 = 0,96 → 4% menor → A. Conferência: 100 → 120 → 96.
#   Material: o preço não volta ao original (a C, "igual", é a resposta instintiva). Explicações NOSSAS: B (4% maior) = acertou
#   o 4 e errou o sentido; D (20% menor) = olhou só o último desconto; E (40% maior) = somou as duas taxas como aumentos.
# QUESTÃO 9 (nós fazemos): 1,20 · 0,75 = 0,90 → 10% mais barato → C. Conferência: 100 → 120 → 90 (25% de 120 = 30).
#   Material: A (5% mais barato) = subtração ingênua (25 − 20). Explicações NOSSAS: B (5% mais caro) = subtraiu e ainda
#   trocou o sentido; D (10% mais caro) = acertou o 10 e errou o sentido; E (45% mais barato) = somou 20 + 25.
# QUESTÃO 5 (você faz): 1 ÷ 1,25 = 0,80 → desconto de 20% → B. Conferência: 100 → 125 → 100. Fórmula 25/125 = 20%.
#   Material: D (25%) = a resposta instintiva. Explicações NOSSAS: A (15%), C (22,5%) e E (30%) não saem de conta certa;
#   o teste com 100 elimina: 125 · 0,85 = 106,25; 125 · 0,775 = 96,875; 125 · 0,70 = 87,5. Só a B volta a 100.
# Nós fazemos (prompt): R$ 90 depois de 10% de desconto → 90 ÷ 0,9 = R$ 100 (somar 10% a 90 daria 99, errado).
# Exemplos nossos: +50% e −50% → 0,75 (curiosidade da fórmula 1 − x²/10 000); desconto antes do aumento (100 → 80 → 96);
#   +50% desfeito por 1/3; R$ 180 com 20% de desconto daria 144 (prova de que 180 não é o original).
# Atalhos (verde): "a perda é a taxa vezes a taxa, dividido por cem" (20 · 20 ÷ 100 = 4) · "o desconto de volta é o que
#   entrou dividido pelo novo total" · "na ida, multiplique pelo fator; na volta, divida".
# Frases-chave (meio e fim, idênticas): 1. Mesma taxa, base diferente, valor diferente.
#   2. Aumento e desconto iguais sempre terminam abaixo. 3. Para voltar, divida pelo fator.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "A base mudou: por que +20% e −20% não se anulam | Porcentagem Ep. 4"
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
        "{a}Um preço sobe *vinte por cento* [p=0.2] e depois cai *vinte por cento.* [p=0.4] {b}Volta ao valor original? "
        "[p=0.4] {c}Não: [p=0.2] termina *quatro por cento mais barato.* [p=0.5] {d}E isso cai no ENEM [p=0.2] com uma "
        "frequência *impressionante.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai entender *por que* isso acontece [p=0.3] {b}e responder também: [p=0.2] *que "
        "desconto desfaz um aumento,* [p=0.3] {c}e *qual era o preço antes do desconto.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Do episódio dois: [p=0.2] o *fator.* [p=0.2] Aumento de vinte por "
        "cento: [p=0.2] vezes *um vírgula vinte.* [p=0.2] Desconto de vinte por cento: [p=0.2] vezes *zero vírgula "
        "oitenta.* [p=0.4] {b}E do episódio três: [p=0.2] variações em sequência, [p=0.2] *multiplique os fatores.*"),

    # ================= BLOCO A: EM REAIS =================
    dict(id="04", block="loja", text=
        "{t}Imagine uma loja. [p=0.3] {a}Na segunda-feira, [p=0.2] um produto custa *cem reais.* [p=0.3] {b}O preço sobe "
        "vinte por cento: [p=0.2] vinte por cento de cem é *vinte.* [p=0.2] Vai para *cento e vinte.* [p=0.4] {c}Na sexta, "
        "[p=0.2] a loja quer voltar atrás [p=0.2] e dá *vinte por cento de desconto.* [p=0.4] {d}Vinte por cento de quê? "
        "[p=0.3] Do preço de agora: [p=0.2] *cento e vinte.* [p=0.2] Dá *vinte e quatro* reais. [p=0.4] {e}Cento e vinte "
        "menos vinte e quatro: [p=0.2] *noventa e seis.*"),
    dict(id="05", block="loja", text=
        "{t}Não voltou para cem! [p=0.4] {a}Com os fatores, [p=0.2] numa conta só: [p=0.2] um vírgula vinte [p=0.2] vezes "
        "zero vírgula oitenta [p=0.2] *dá zero vírgula noventa e seis.* [p=0.4] {b}O preço final é noventa e seis por cento "
        "do inicial. [p=0.3] {c}Ficou *quatro por cento mais barato.* [p=0.3] Exatamente como no começo da aula."),

    # ================= BLOCO B: A CAUSA =================
    dict(id="06", block="causa", text=
        "{t}Mas por quê? [p=0.3] Os dois eram vinte por cento! [p=0.4] {a}Toda porcentagem é calculada sobre *alguma "
        "coisa.* [p=0.3] Essa coisa se chama *base de cálculo:* [p=0.2] o valor do qual você parte. [p=0.4] {b}O aumento foi "
        "sobre *cem:* [p=0.2] valeu *vinte* reais. [p=0.4] {c}O desconto foi sobre *cento e vinte:* [p=0.2] valeu *vinte e "
        "quatro.* [p=0.4] {d}*A base mudou.* [p=0.3] Mesma taxa, [p=0.2] base diferente, [p=0.2] valor diferente. [p=0.3] "
        "Saiu mais do que entrou."),

    # ================= BLOCO C: A REGRA =================
    dict(id="07", block="regra", text=
        "{t}E se o desconto viesse *primeiro?* [p=0.3] {a}Cem, [p=0.2] menos vinte por cento: [p=0.2] *oitenta.* [p=0.3] "
        "{b}Depois, mais vinte por cento *de oitenta:* [p=0.2] dezesseis. [p=0.2] *Noventa e seis* de novo. [p=0.4] {c}Agora "
        "o aumento é que ficou fraco: [p=0.2] incidiu sobre uma base *menor.* [p=0.4] {d}A regra: [p=0.2] aumento e desconto "
        "do *mesmo* percentual [p=0.2] *sempre* terminam abaixo do original, [p=0.2] em qualquer ordem."),
    dict(id="08", block="regra", text=
        "{t}E quanto se perde? [p=0.3] {a}Uma curiosidade: [p=0.2] existe uma fórmula. [p=0.2] *Um menos x ao quadrado, "
        "[p=0.2] sobre dez mil.* [p=0.3] O x é a taxa, [p=0.2] e x ao quadrado é x vezes x. [p=0.4] {b}Com cinquenta por "
        "cento: [p=0.2] um vírgula cinco vezes zero vírgula cinco [p=0.2] dá *zero vírgula setenta e cinco.* [p=0.3] Perda de "
        "*vinte e cinco por cento!* [p=0.4] {c}O atalho de cabeça: [p=0.2] *a perda é a taxa vezes a taxa, [p=0.2] dividido "
        "por cem.* [p=0.3] Vinte vezes vinte, [p=0.2] quatrocentos, [p=0.2] dividido por cem: [p=0.2] *quatro por cento.*"),

    # ================= BLOCO D: QUE DESCONTO DESFAZ UM AUMENTO =================
    dict(id="09", block="desfaz", text=
        "{t}Agora a pergunta do avesso. [p=0.3] {a}Um preço de cem sobe *cinquenta por cento:* [p=0.2] vai para *cento e "
        "cinquenta.* [p=0.4] {b}Que desconto faz ele voltar a cem? [p=0.3] Cinquenta por cento? [p=0.4] {c}Cinquenta por "
        "cento de cento e cinquenta [p=0.2] é setenta e cinco. [p=0.2] Iria para *setenta e cinco.* [p=0.2] Passou do ponto! "
        "[p=0.4] {d}A base mudou de novo: [p=0.2] agora ela é *cento e cinquenta.*"),
    dict(id="10", block="desfaz", text=
        "{t}O jeito certo: [p=0.2] o aumento foi uma *multiplicação.* [p=0.3] {a}E o que desfaz uma multiplicação? [p=0.3] "
        "*Uma divisão.* [p=0.4] {b}Um dividido por um vírgula cinco [p=0.2] dá *zero vírgula seis seis seis* e por aí vai. "
        "[p=0.4] {c}É o fator de um desconto de *um terço:* [p=0.2] uns *trinta e três por cento.* [p=0.4] {d}Confira: [p=0.2] "
        "um terço de cento e cinquenta [p=0.2] é *cinquenta.* [p=0.2] Cento e cinquenta menos cinquenta: [p=0.2] *cem.* "
        "[p=0.2] Voltou!"),

    # ================= BLOCO E: A FÓRMULA DO RETORNO =================
    dict(id="11", block="formula", text=
        "{t}Isso também tem uma fórmula: [p=0.2] o desconto de *retorno.* [p=0.3] Retorno é voltar ao valor de antes. "
        "[p=0.4] {a}*D igual a x, [p=0.2] sobre cem mais x.* [p=0.3] O x é o aumento. [p=0.3] {b}E o cem mais x? [p=0.2] É o "
        "*preço novo:* [p=0.2] a base nova. [p=0.4] {c}Com cinquenta: [p=0.2] cinquenta sobre cento e cinquenta [p=0.2] *é um "
        "terço.* [p=0.3] Bateu! [p=0.4] {d}Atalho: [p=0.2] *o desconto de volta [p=0.2] é o que entrou, [p=0.2] dividido pelo "
        "novo total.*"),

    # ================= BLOCO F: O PREÇO ANTES DO DESCONTO =================
    dict(id="12", block="antes", text=
        "{t}E o caminho de volta numa compra? [p=0.3] {a}Um produto custa *cento e cinquenta reais,* [p=0.2] *já com vinte "
        "por cento de desconto.* [p=0.3] {b}Qual era o preço de etiqueta: [p=0.2] o *valor original,* [p=0.2] antes do "
        "desconto? [p=0.4] {c}Muita gente soma vinte por cento aos cento e cinquenta: [p=0.2] *cento e oitenta.* [p=0.4] "
        "{d}Teste: [p=0.2] cento e oitenta, [p=0.2] com vinte por cento de desconto, [p=0.2] daria *cento e quarenta e "
        "quatro.* [p=0.3] Não dá cento e cinquenta!"),
    dict(id="13", block="antes", text=
        "{t}O motivo é o mesmo: [p=0.2] *a base mudou.* [p=0.3] {a}Os vinte por cento foram tirados do preço *original,* "
        "[p=0.2] que é *maior* que cento e cinquenta. [p=0.4] {b}Então divida pelo fator: [p=0.2] cento e cinquenta, [p=0.2] "
        "dividido por zero vírgula oitenta, [p=0.2] *cento e oitenta e sete e cinquenta.* [p=0.4] {c}Confira: [p=0.2] vinte "
        "por cento de cento e oitenta e sete e cinquenta [p=0.2] é *trinta e sete e cinquenta.* [p=0.2] Tirando, [p=0.2] "
        "*cento e cinquenta.* [p=0.3] Fechou!"),

    # ================= BLOCO G: A REGRA GERAL =================
    dict(id="14", block="geral", text=
        "{t}Juntando tudo numa regra só. [p=0.3] {a}Na ida, [p=0.2] você *multiplica* pelo fator. [p=0.4] {b}Para voltar, "
        "[p=0.2] você *divide* pelo fator. [p=0.4] {c}Seja para desfazer um aumento, [p=0.2] seja para achar o preço antes "
        "do desconto. [p=0.4] {d}E quando o enunciado não dá o valor, [p=0.2] *comece com cem.* [p=0.3] A resposta já sai em "
        "porcentagem."),

    # ================= NÓS FAZEMOS =================
    dict(id="15", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Um produto custa *noventa reais* [p=0.2] depois de *dez por cento* de desconto. [p=0.4] "
        "{b}Qual era o preço original? [p=0.3] {c}*Pause o vídeo e calcule.* [p=2.0]"),
    dict(id="16", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Desconto de dez por cento: [p=0.2] fator *zero vírgula nove.* [p=0.3] Para voltar, "
        "[p=0.2] divida: [p=0.2] noventa dividido por zero vírgula nove [p=0.2] *é cem.* [p=0.4] {b}Confira: [p=0.2] dez por "
        "cento de cem é dez. [p=0.2] Cem menos dez, [p=0.2] *noventa.* [p=0.3] Fechou! [p=0.4] {c}Quem somou dez por cento aos "
        "noventa [p=0.2] respondeu *noventa e nove.* [p=0.2] Errou."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] mesma taxa, base diferente, valor diferente. [p=0.5] "
        "{b}Dois: [p=0.2] aumento e desconto iguais sempre terminam abaixo. [p=0.5] {c}Três: [p=0.2] para voltar, divida pelo "
        "fator."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="18", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que *mais vinte* e *menos vinte* [p=0.2] "
        "voltam ao original. [p=0.4] {b}Parece certo, [p=0.2] porque os números são iguais. [p=0.4] {c}Mas o desconto é sobre "
        "uma base *maior.* [p=0.3] Termina em noventa e seis."),
    dict(id="19", block="erros", text=
        "{a}Segundo: [p=0.2] achar que o desconto que desfaz um aumento de vinte e cinco por cento [p=0.2] é de *vinte e "
        "cinco.* [p=0.4] {b}Parece certo, [p=0.2] porque desfazer lembra repetir o mesmo número. [p=0.4] {c}Mas o desconto "
        "incide sobre o preço *já aumentado.* [p=0.3] Ele é *menor.* [p=0.2] Para achar, [p=0.2] divida pelo fator."),
    dict(id="20", block="erros", text=
        "{a}Terceiro: [p=0.2] *somar* vinte por cento a um preço com desconto [p=0.2] para achar o original. [p=0.4] "
        "{b}Parece certo, [p=0.2] porque somar parece o contrário de descontar. [p=0.4] {c}Mas o desconto saiu do preço "
        "original, [p=0.2] que é *maior.* [p=0.3] Divida pelo fator."),
    dict(id="21", block="erros", text=
        "{a}Quarto: [p=0.2] *subtrair* as taxas quando uma sobe e a outra desce. [p=0.2] Mais dez e menos vinte, [p=0.2] "
        "menos dez. [p=0.4] {b}Parece certo, [p=0.2] porque uma parece cancelar a outra. [p=0.4] {c}Mas são bases diferentes. "
        "[p=0.3] Multiplique os fatores: [p=0.2] um vírgula dez vezes zero vírgula oitenta [p=0.2] dá zero vírgula oitenta e "
        "oito. [p=0.2] *Menos doze* por cento."),

    # ================= QUESTÃO 4 — EU FAÇO =================
    dict(id="22", block="q4", text=
        "{t}Agora, questões no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.3] A primeira, [p=0.2] *eu faço.* "
        "[p=0.4] {a}O preço de uma mercadoria sofreu um aumento de *vinte por cento* [p=0.2] e, algumas semanas depois, "
        "[p=0.2] um desconto de *vinte por cento* sobre o preço já reajustado. [p=0.4] {b}Em relação ao preço inicial, [p=0.2] "
        "o preço final ficou: [p=0.4] {qa}A: [p=0.2] quatro por cento menor. [p=0.3] {qb}B: [p=0.2] quatro por cento maior. "
        "[p=0.3] {qc}C: [p=0.2] igual. [p=0.3] {qd}D: [p=0.2] vinte por cento menor. [p=0.3] {qe}E: [p=0.2] quarenta por "
        "cento maior."),
    dict(id="23", block="q4", text=
        "{t}É a loja do começo da aula. [p=0.3] {a}Os fatores: [p=0.2] um vírgula vinte vezes zero vírgula oitenta, [p=0.2] "
        "*zero vírgula noventa e seis.* [p=0.4] {b}Com cem: [p=0.2] cento e vinte, [p=0.2] depois *noventa e seis.* [p=0.3] "
        "{ok}*Letra A!* [p=0.2] Quatro por cento menor. [p=0.5] {xc}A C é a resposta instintiva: [p=0.2] esquece que a base "
        "mudou. [p=0.4] {xb}A B acertou o quatro, [p=0.2] mas errou o *sentido.* [p=0.4] {xd}A D olhou só o último "
        "desconto. [p=0.4] {xe}E a E somou as duas taxas, [p=0.2] como se fossem aumentos."),

    # ================= QUESTÃO 9 — NÓS FAZEMOS =================
    dict(id="24", block="q9", text=
        "{t}A segunda, [p=0.2] *nós fazemos.* [p=0.3] {a}O preço de um insumo agrícola subiu *vinte por cento* em um "
        "semestre [p=0.2] e caiu *vinte e cinco por cento* no semestre seguinte, [p=0.2] sempre em relação ao preço vigente. "
        "[p=0.4] {b}Ao final do ano, [p=0.2] em relação ao preço do início do período, [p=0.2] o insumo ficou: [p=0.4] "
        "{qa}A: [p=0.2] cinco por cento mais barato. [p=0.3] {qb}B: [p=0.2] cinco por cento mais caro. [p=0.3] {qc}C: "
        "[p=0.2] dez por cento mais barato. [p=0.3] {qd}D: [p=0.2] dez por cento mais caro. [p=0.3] {qe}E: [p=0.2] quarenta e "
        "cinco por cento mais barato. [p=0.5] {p}*Pause e escreva os dois fatores.* [p=2.0]"),
    dict(id="25", block="q9", text=
        "{t}Juntos: [p=0.2] subiu vinte, [p=0.2] fator *um vírgula vinte.* [p=0.2] Caiu vinte e cinco, [p=0.2] fator *zero "
        "vírgula setenta e cinco.* [p=0.4] {a}Multiplicando: [p=0.2] *zero vírgula noventa.* [p=0.3] Dez por cento mais "
        "barato. [p=0.3] {ok}*Letra C!* [p=0.4] {b}Com cem: [p=0.2] cento e vinte; [p=0.2] vinte e cinco por cento de cento e "
        "vinte é *trinta;* [p=0.2] sobra *noventa.* [p=0.3] A base mudou: [p=0.2] saíram trinta, [p=0.2] e só tinham entrado "
        "vinte. [p=0.5] {xa}A A é a subtração ingênua: [p=0.2] vinte e cinco menos vinte, [p=0.2] cinco. [p=0.4] {xb}A B "
        "subtraiu [p=0.2] e ainda trocou o sentido. [p=0.4] {xd}A D acertou o dez, [p=0.2] mas errou o sentido. [p=0.4] {xe}E "
        "a E somou as duas taxas."),

    # ================= QUESTÃO 5 — VOCÊ FAZ =================
    dict(id="26", block="q5", text=
        "{t}E a última, [p=0.2] *você faz.* [p=0.3] {a}Após um reajuste de *vinte e cinco por cento,* [p=0.2] uma loja "
        "decidiu promover um desconto sobre o novo preço, [p=0.2] de modo que o produto voltasse a custar exatamente o valor "
        "anterior ao reajuste. [p=0.4] {b}O desconto concedido foi de: [p=0.4] {qa}A: [p=0.2] quinze por cento. [p=0.3] {qb}B: "
        "[p=0.2] vinte. [p=0.3] {qc}C: [p=0.2] vinte e dois vírgula cinco. [p=0.3] {qd}D: [p=0.2] vinte e cinco. [p=0.3] "
        "{qe}E: [p=0.2] trinta por cento. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="27", block="q5", text=
        "{t}Vamos conferir. [p=0.3] {a}Para voltar, [p=0.2] divida pelo fator: [p=0.2] um dividido por um vírgula vinte e "
        "cinco [p=0.2] *é zero vírgula oitenta.* [p=0.3] Desconto de *vinte por cento.* [p=0.3] {ok}*Letra B!* [p=0.4] {b}Com "
        "cem: [p=0.2] cento e vinte e cinco; [p=0.2] vinte por cento de cento e vinte e cinco é *vinte e cinco;* [p=0.2] volta "
        "a *cem.* [p=0.4] {c}Pela fórmula: [p=0.2] vinte e cinco sobre cento e vinte e cinco, [p=0.2] *vinte por cento.* "
        "[p=0.5] {xd}A D é a resposta instintiva: [p=0.2] esquece que a base agora é cento e vinte e cinco. [p=0.4] {xa}E "
        "teste as outras com cem: [p=0.2] a A deixa *cento e seis,* [p=0.2] {xc}a C, *noventa e seis* e pouco, [p=0.2] {xe}a "
        "E, *oitenta e sete e meio.* [p=0.3] Só a B volta a cem."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] mesma taxa, base diferente, valor diferente. [p=0.5] "
        "{b}Dois: [p=0.2] aumento e desconto iguais sempre terminam abaixo. [p=0.5] {c}Três: [p=0.2] para voltar, divida pelo "
        "fator."),

    # ================= PONTE E CTA =================
    dict(id="29", block="ponte", text=
        "{a}O desemprego foi de *oito por cento* para *dez por cento.* [p=0.4] {b}Subiu dois por cento? [p=0.4] {c}Esse é o "
        "erro de linguagem *mais comum* da imprensa, [p=0.2] e o ENEM cobra. [p=0.4] {d}Próximo episódio."),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você achava que mais vinte e menos vinte voltavam ao original? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
