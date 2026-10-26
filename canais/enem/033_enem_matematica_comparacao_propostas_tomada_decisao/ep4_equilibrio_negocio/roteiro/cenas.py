# Roteiro — Comparação de Propostas e Tomada de Decisão, Episódio 4 de 5: ponto de equilíbrio de um negócio e meta de
#   lucro
# Base: Estudos/Enem/estudos/01-matematica/18-comparacao-propostas-tomada-decisao.html — seção 07 + Questão 5 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (do prompt):
#   O TIJOLINHO: cada unidade vendida paga um tijolinho do custo fixo (o MURO); o tijolinho é a margem de contribuição.
#   O PREÇO NÃO É TODO SEU: primeiro sai o custo da própria unidade; só o que sobra ataca o custo fixo.
#   O MESMO CRUZAMENTO DO EPISÓDIO 2: de um lado, prejuízo; do outro, lucro (placar que vira de vermelho para verde).
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos do material/prompt: fixo 6.000, variável 15, preço 35 → margem 20 → 6.000 ÷ 20 = 300 (eu faço, bloco d), com a
#   conferência 300 · 20 − 6.000 = 0 · 6.000 ÷ 35 ≈ 172 (bloco e) · nós fazemos (food truck): 3.600, 8, 23 → margem 15 →
#   240 lanches; (3.600 + 1.500) ÷ 15 = 340.
# Exemplos NOSSOS (conferidos em Python): bloco d, 299 peças → prejuízo de R$ 20,00 e 301 → lucro de R$ 20,00 · bloco e,
#   172 peças deixam 172 · 20 = 3.440 → prejuízo de R$ 2.560,00 · bloco f, meta de R$ 1.000,00 → 7.000 ÷ 20 = 350 (não é a
#   Q5, que usa R$ 2.000,00) e meta de R$ 1.010,00 → 350,5 → 351 (com 350, o lucro é só R$ 1.000,00) · erro 2: custo fixo
#   R$ 5.000,00 e margem R$ 30,00 → 166,67 → 167 (com 166, prejuízo de R$ 20,00) · CTA: preço R$ 45,00 → 6.000 ÷ 30 = 200.
# Atalhos (NOSSOS, verde): "margem primeiro, divisão depois" · "corte o mesmo zero dos dois" (6.000 ÷ 20 = 600 ÷ 2) ·
#   "no mínimo + resultado quebrado: suba para o próximo inteiro" · "confira: quantidade × margem − fixo = lucro".
# QUESTÃO 5 (você faz): 20q = 6.000 + 2.000 → 400 peças (D); conferência 400 · 20 − 6.000 = 2.000. Erradas (material):
#   A = 2.000 ÷ 20 = 100 (esquece o fixo) · B = 8.000 ÷ 35 ≈ 228,6 → 229 (divide pelo preço) · C = 300 (o equilíbrio,
#   esquece a meta) · E = 8.000 ÷ 15 ≈ 533,3 → 534 (divide pelo custo de produção).
# Frases-chave (meio e fim, idênticas): 1. Divida o custo fixo pela margem, não pelo preço. 2. A meta de lucro entra junto
#   com o custo fixo. 3. "No mínimo" com resultado quebrado: arredonde para cima.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Quantas peças para empatar? Ponto de equilíbrio e meta de lucro | Comparar Propostas Ep. 4"
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
        "{a}Custo fixo de *seis mil reais,* [p=0.2] peça vendida a *trinta e cinco reais.* [p=0.4] {b}Bastam *cento e "
        "setenta e duas* peças para pagar as contas? [p=0.5] {c}Não: [p=0.2] são *trezentas.* [p=0.4] {d}Cada peça "
        "também custa *quinze reais* para ser feita."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai calcular quantas unidades um negócio precisa vender [p=0.2] *para "
        "empatar* [p=0.3] {b}e *para bater uma meta de lucro.*"),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Da série de Descontos e lucro: [p=0.2] *lucro é venda menos custo.* "
        "[p=0.4] {b}E do episódio dois: [p=0.2] o *ponto de equilíbrio* é onde as duas contas *empatam.* [p=0.2] "
        "Antes dele, uma ganha; [p=0.2] depois, a outra."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{a}Pense numa *pequena fábrica de peças.* [p=0.4] {b}Todo mês chegam o *aluguel* e os *salários,* [p=0.2] "
        "venda ela uma peça ou mil. [p=0.4] {c}E cada peça fabricada [p=0.2] gasta *matéria-prima.*"),

    # ================= BLOCO A: FIXO × VARIÁVEL =================
    dict(id="05", block="custos", text=
        "{t}Que conta é qual? [p=0.4] {a}*Custo fixo* é o que você paga *mesmo sem produzir:* [p=0.2] aluguel, "
        "salários. [p=0.2] Aqui, *seis mil reais* por mês. [p=0.4] {b}*Custo variável por unidade* é o que *cada peça* "
        "gasta para existir. [p=0.2] Aqui, *quinze reais.*"),

    # ================= BLOCO B: MARGEM DE CONTRIBUIÇÃO =================
    dict(id="06", block="margem", text=
        "{t}Vendeu uma peça por trinta e cinco. [p=0.2] Quanto disso é seu? [p=0.4] {a}*Não é tudo.* [p=0.2] O preço "
        "não é todo seu: [p=0.2] primeiro saem os *quinze* da própria peça. [p=0.4] {b}Sobram *vinte reais.* [p=0.4] "
        "{c}Essa sobra tem nome: [p=0.2] *margem de contribuição.* [p=0.2] É *preço menos custo variável,* [p=0.2] o "
        "que cada unidade deixa para pagar o fixo."),
    dict(id="07", block="margem", text=
        "{t}Agora imagine o custo fixo como um *muro de seis mil reais.* [p=0.4] {a}Cada peça vendida [p=0.2] entra com "
        "trinta e cinco. [p=0.2] *Quinze voltam* para a matéria-prima. [p=0.4] {b}E um *tijolinho de vinte* vai para o "
        "muro. [p=0.4] {c}O tijolinho [p=0.2] *é a margem de contribuição.*"),

    # ================= BLOCO C: A FÓRMULA DO LUCRO =================
    dict(id="08", block="formula", text=
        "{t}E como fica o lucro do mês? [p=0.4] {a}Margem *vezes* a quantidade vendida, [p=0.2] *menos* o custo fixo. "
        "[p=0.4] {b}Quantidade a gente chama de *q.* [p=0.2] Lucro igual a *vinte vezes q, menos seis mil.* [p=0.4] "
        "{c}Atalho: [p=0.2] *margem primeiro, divisão depois.*"),

    # ================= BLOCO D: EQUILÍBRIO (EU FAÇO) =================
    dict(id="09", block="equilibrio", text=
        "{t}Quantas peças para *empatar?* [p=0.3] Eu faço com você. [p=0.4] {a}Empatar é *lucro zero.* [p=0.2] Os "
        "tijolinhos precisam fechar o muro: [p=0.2] *seis mil dividido por vinte.* [p=0.4] {b}Atalho: [p=0.2] corte o "
        "mesmo zero dos dois. [p=0.2] Seiscentos dividido por dois: [p=0.2] *trezentas peças por mês.* [p=0.4] {c}No "
        "tijolinho trezentos, [p=0.2] o muro fecha."),
    dict(id="10", block="equilibrio", text=
        "{t}Sempre confira o lucro. [p=0.3] {a}Trezentas vezes vinte, [p=0.2] seis mil. [p=0.2] Menos seis mil: [p=0.2] "
        "*zero.* [p=0.4] {b}Com duzentas e noventa e nove, [p=0.2] *vinte reais de prejuízo.* [p=0.2] Com trezentas e "
        "uma, [p=0.2] *vinte de lucro.* [p=0.4] {c}É o mesmo cruzamento do episódio dois: [p=0.2] de um lado, "
        "*prejuízo;* [p=0.2] do outro, *lucro.*"),

    # ================= BLOCO E: DIVIDIR PELO PREÇO =================
    dict(id="11", block="preco", text=
        "{t}E as cento e setenta e duas do começo? [p=0.4] {a}Saem de *seis mil dividido por trinta e cinco.* [p=0.4] "
        "{b}Venda essas peças e veja: [p=0.2] cada uma deixa só vinte. [p=0.2] Dá *três mil, quatrocentos e quarenta.* "
        "[p=0.4] {c}*Prejuízo de dois mil, quinhentos e sessenta reais.* [p=0.2] A conta esqueceu que cada peça "
        "*também custa.*"),

    # ================= BLOCO F: META DE LUCRO =================
    dict(id="12", block="meta", text=
        "{t}E se o dono quiser *lucrar mil reais?* [p=0.4] {a}A meta é *mais um pedaço de muro.* [p=0.2] Ela entra "
        "*junto com o custo fixo:* [p=0.2] seis mil mais mil, [p=0.2] *sete mil.* [p=0.4] {b}Sete mil dividido por "
        "vinte: [p=0.2] *trezentas e cinquenta peças.* [p=0.4] {c}Confira: [p=0.2] trezentas e cinquenta vezes vinte, "
        "[p=0.2] sete mil. [p=0.2] Menos seis mil: [p=0.2] *mil de lucro.*"),
    dict(id="13", block="meta", text=
        "{t}E se a divisão *não der exata?* [p=0.4] {a}Meta de mil e dez reais: [p=0.2] *trezentos e cinquenta "
        "vírgula cinco.* [p=0.4] {b}Ninguém vende meia peça. [p=0.2] E com trezentas e cinquenta, [p=0.2] o lucro é "
        "só mil. [p=0.2] *Não bate a meta.* [p=0.4] {c}Atalho: [p=0.2] *no mínimo* com resultado quebrado, [p=0.2] "
        "*suba para o próximo inteiro.* [p=0.2] Trezentas e cinquenta e uma."),

    # ================= NÓS FAZEMOS =================
    dict(id="14", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Um *food truck* tem custo fixo de *três mil e seiscentos reais* por mês. [p=0.2] Cada "
        "lanche custa *oito reais* para ser feito [p=0.2] e é vendido por *vinte e três.* [p=0.4] {b}Quantos lanches "
        "para *empatar?* [p=0.2] E para *lucrar mil e quinhentos?* [p=0.3] {c}*Pause e tente.* [p=2.0]"),
    dict(id="15", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Margem primeiro: [p=0.2] vinte e três menos oito, [p=0.2] *quinze.* [p=0.4] "
        "{b}Empate: [p=0.2] três mil e seiscentos dividido por quinze: [p=0.2] *duzentos e quarenta lanches.* [p=0.4] "
        "{c}Meta: [p=0.2] três mil e seiscentos *mais* mil e quinhentos, [p=0.2] cinco mil e cem. [p=0.2] Dividido "
        "por quinze: [p=0.2] *trezentos e quarenta lanches.* [p=0.4] {d}Confira: [p=0.2] trezentos e quarenta vezes "
        "quinze, [p=0.2] cinco mil e cem. [p=0.2] Menos o fixo: [p=0.2] *mil e quinhentos.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="16", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] divida o custo fixo pela margem, não pelo preço. "
        "[p=0.5] {b}Dois: [p=0.2] a meta de lucro entra junto com o custo fixo. [p=0.5] {c}Três: [p=0.2] no mínimo "
        "com resultado quebrado: [p=0.2] arredonde para cima."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="17", block="erros", text=
        "{t}Os dois erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar o equilíbrio *dividindo pelo preço.* [p=0.4] "
        "{b}Parece certo: [p=0.2] o dinheiro que entra é o preço. [p=0.4] {c}Mas parte dele *volta* para fazer a "
        "própria peça. [p=0.2] Quem paga o fixo é *preço menos custo variável.*"),
    dict(id="18", block="erros", text=
        "{a}Segundo: [p=0.2] *arredondar para baixo* uma quantidade mínima. [p=0.2] Fixo de cinco mil, [p=0.2] "
        "margem de trinta: [p=0.2] *cento e sessenta e seis vírgula sete.* [p=0.4] {b}Parece certo: [p=0.2] é a regra "
        "de arredondar da escola. [p=0.4] {c}Mas com cento e sessenta e seis, [p=0.2] ainda há *vinte reais de "
        "prejuízo.* [p=0.2] O mínimo é *cento e sessenta e sete.*"),

    # ================= QUESTÃO 5 (VOCÊ FAZ) =================
    dict(id="19", block="q5", text=
        "{t}Agora é com você, [p=0.2] numa questão do nosso material de estudo. [p=0.4] {a}Uma pequena fábrica tem "
        "custo fixo mensal de *seis mil reais.* [p=0.2] Cada peça custa *quinze reais* para ser produzida [p=0.2] e é "
        "vendida por *trinta e cinco.* [p=0.2] Para obter lucro de *dois mil reais* em um mês, [p=0.2] a fábrica "
        "precisa produzir e vender, *no mínimo:* [p=0.4] {qa}A: [p=0.2] cem peças. [p=0.3] {qb}B: [p=0.2] duzentas e "
        "vinte e nove. [p=0.3] {qc}C: [p=0.2] trezentas. [p=0.3] {qd}D: [p=0.2] quatrocentas. [p=0.3] {qe}E: [p=0.2] "
        "quinhentas e trinta e quatro. [p=0.4] {p}*Pause o vídeo e resolva sozinho.* [p=2.5]"),
    dict(id="20", block="q5", text=
        "{t}Vamos conferir. [p=0.3] {a}Margem: [p=0.2] trinta e cinco menos quinze, [p=0.2] *vinte.* [p=0.4] {b}A "
        "meta entra junto com o fixo: [p=0.2] seis mil mais dois mil, [p=0.2] *oito mil.* [p=0.2] Dividido por vinte: "
        "[p=0.2] *quatrocentas peças.* [p=0.4] {c}Confira: [p=0.2] quatrocentas vezes vinte, [p=0.2] oito mil, "
        "[p=0.2] menos seis mil, [p=0.2] *dois mil de lucro.* [p=0.3] {ok}*Letra D!*"),
    dict(id="21", block="q5", text=
        "{t}E as pegadinhas? [p=0.3] {xc}A C é o *equilíbrio:* [p=0.2] esquece a meta. [p=0.4] {xa}A A divide *só o "
        "lucro* pela margem: [p=0.2] esquece o fixo. [p=0.4] {xb}A B divide oito mil *pelo preço.* [p=0.4] {xe}E a E "
        "divide pelo *custo de produção.* [p=0.4] {c}As duas últimas ainda arredondam para cima, [p=0.2] para parecer "
        "cuidadosas."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="22", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] divida o custo fixo pela margem, não pelo "
        "preço. [p=0.5] {b}Dois: [p=0.2] a meta de lucro entra junto com o custo fixo. [p=0.5] {c}Três: [p=0.2] no "
        "mínimo com resultado quebrado: [p=0.2] arredonde para cima."),

    # ================= PONTE E CTA =================
    dict(id="23", block="ponte", text=
        "{a}No último episódio, [p=0.2] juntamos este assunto [p=0.3] {b}e fechamos todo o bloco de Matemática "
        "Financeira, [p=0.3] {c}com pegadinhas e questões inéditas."),
    dict(id="24", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] se a fábrica vendesse cada peça por quarenta e cinco reais, "
        "[p=0.2] quantas peças para empatar? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um "
        "link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para "
        "revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no "
        "Estudativo. [p=1.5]"),
]
