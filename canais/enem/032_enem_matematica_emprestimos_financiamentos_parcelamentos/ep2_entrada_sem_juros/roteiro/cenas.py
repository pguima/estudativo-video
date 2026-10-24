# Roteiro — Empréstimos, Financiamentos e Parcelamentos, Episódio 2 de 5: entrada mais uma parcela, a taxa embutida e o
#   falso "sem juros"
# Base: Estudos/Enem/estudos/01-matematica/17-emprestimos-financiamentos-parcelamentos.html — seções 04 e 05, os termos
#   "valor financiado" e "entrada" da seção 02 + Questão 1 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (do prompt):
#   A ENTRADA NÃO VIAJA: é paga hoje, não é emprestada e não paga aluguel.
#   A LOJA TE "EMPRESTA" SÓ O QUE FALTOU PAGAR: valor financiado = à vista − entrada.
#   O "SEM JUROS" COM DESCONTO À VISTA É UM PREÇO COM FANTASIA: o preço real é o à vista; a diferença são juros.
#   (Da série: a LINHA DO TEMPO do episódio 1.)
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Gancho: "parece 5%" é o arredondamento de 100 ÷ 1.900 ≈ 5,3% (e 100 ÷ 2.000 = 5%); o bloco c mostra as duas contas.
# Exemplos do material/prompt: geladeira 1.900 à vista ou 2 × 1.000 (ato + 30 dias) → financiado 900, juros 100,
#   100 ÷ 900 ≈ 11,1% a.m. (é o "eu faço", no bloco b) · denominadores errados 100 ÷ 1.900 ≈ 5,3% e 100 ÷ 2.000 = 5% ·
#   10 × "sem juros" = 1.000 contra 900 à vista → R$ 100,00 de juros embutidos · nós fazemos: 1.100 à vista ou 2 × 600
#   → financiado 500, juros 100 → 20% a.m.
# Atalhos (NOSSOS, verde): "parcela ÷ financiado, tire o 1" (1.000 ÷ 900 = 1,111 → 11,1%) · conferência: a taxa certa
#   é SEMPRE a maior entre as candidatas, porque o financiado é o menor denominador possível.
# QUESTÃO 1 (você faz): 900 − 500 = 400 financiados; paga 500 em 30 dias; juros 100 → 100 ÷ 400 = 25% (E).
#   Erradas (material): A acredita no anúncio; B ÷ 1.000 (total a prazo) = 10%; C ÷ 900 (à vista) ≈ 11,1%;
#   D ÷ 500 (parcela) = 20%. NOSSO (aviso didático): 11,1% e 20% são as respostas da geladeira e do "nós fazemos" —
#   números conhecidos que aqui são distratores.
# Frases-chave (meio e fim, idênticas): 1. A entrada não é financiada: divida os juros só pelo que ficou para depois.
#   2. Taxa embutida = juros ÷ valor financiado. 3. Se existe desconto à vista, o "sem juros" tem juros.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "O \"sem juros\" tem juros: a taxa escondida na entrada + 1 parcela · Matemática ENEM, Empréstimos episódio 2"

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
        "{a}Cem reais de diferença [p=0.2] numa geladeira de *mil e novecentos reais* [p=0.2] parece *cinco por "
        "cento.* [p=0.5] {b}Mas esses cem reais [p=0.2] são o preço de adiar *só novecentos reais* [p=0.2] por um "
        "mês: [p=0.4] {c}*onze vírgula um por cento ao mês.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai descobrir a *taxa escondida* [p=0.2] em qualquer entrada mais uma "
        "parcela [p=0.3] {b}e desmascarar o *sem juros.*"),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Da série de Porcentagem: [p=0.2] que porcentagem a parte representa? "
        "[p=0.2] *Divida pela base.* [p=0.4] {b}Do episódio um: [p=0.2] desenhe a *linha do tempo,* [p=0.2] com cada "
        "pagamento na sua data. [p=0.4] {c}E com *uma parcela só,* [p=0.2] daqui a um período, [p=0.2] juros simples "
        "e compostos dão *o mesmo resultado.* [p=0.2] A conta não depende do regime."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{a}Imagine o cartaz de uma loja de eletrodomésticos: [p=0.2] geladeira, *mil e novecentos reais à vista,* "
        "[p=0.2] ou *duas de mil,* [p=0.2] a primeira no ato. [p=0.4] {b}*Preço à vista* [p=0.2] é quanto você paga "
        "se quitar tudo hoje. [p=0.4] {c}E *entrada* [p=0.2] é a parte paga no ato da compra."),
    dict(id="05", block="concreto", text=
        "{a}Do lado, outro anúncio: [p=0.2] *dez vezes sem juros!* [p=0.4] {b}E, em letra pequenininha: [p=0.2] *ou "
        "novecentos reais à vista.* [p=0.4] {c}Será que é mesmo sem juros? [p=0.2] Guarde essa pergunta."),

    # ================= BLOCO A: O MÉTODO =================
    dict(id="06", block="metodo", text=
        "{t}Onde a loja esconde os juros? [p=0.4] {a}Primeiro: [p=0.2] *a entrada não viaja.* [p=0.2] Ela é paga hoje, "
        "[p=0.2] não é emprestada [p=0.2] e não paga aluguel. [p=0.4] {b}Segundo: [p=0.2] a loja te empresta *só o que "
        "faltou pagar.* [p=0.2] Esse é o *valor financiado:* [p=0.2] o preço à vista *menos a entrada.* [p=0.4] "
        "{c}Terceiro: [p=0.2] a *taxa embutida* é a taxa que ninguém anuncia. [p=0.2] Os juros [p=0.2] *divididos "
        "pelo valor financiado.*"),

    # ================= BLOCO B: A GELADEIRA (EU FAÇO) =================
    dict(id="07", block="geladeira", text=
        "{t}Então, quanto custa adiar a geladeira? [p=0.4] {a}A etiqueta se parte em duas. [p=0.2] Mil reais ficam "
        "*parados no dia de hoje:* [p=0.2] é a entrada. [p=0.4] {b}O financiado: [p=0.2] mil e novecentos menos mil, "
        "[p=0.2] *novecentos.* [p=0.4] {c}Esses novecentos vão até daqui a trinta dias [p=0.2] e voltam como *mil.* "
        "[p=0.2] Juros de *cem reais.* [p=0.4] {d}Cem dividido por novecentos: [p=0.2] *onze vírgula um por cento ao "
        "mês.*"),
    dict(id="08", block="geladeira", text=
        "{t}Tem um atalho? [p=0.3] {a}Tem. [p=0.2] Divida a *parcela pelo financiado:* [p=0.2] mil por novecentos, "
        "[p=0.2] *um vírgula um um um.* [p=0.4] {b}Tire o um: [p=0.2] *onze vírgula um por cento.* [p=0.4] {c}É o "
        "fator, [p=0.2] como na série de Porcentagem."),

    # ================= BLOCO C: OS DENOMINADORES ERRADOS =================
    dict(id="09", block="denominador", text=
        "{t}E por que os cem reais *parecem tão pouco?* [p=0.4] {a}Porque a gente divide pela coisa errada. [p=0.2] "
        "Cem sobre dois mil: [p=0.2] *cinco por cento.* [p=0.2] Cem sobre mil e novecentos: [p=0.2] *cinco vírgula "
        "três.* [p=0.4] {b}Só que ninguém adiou dois mil reais. [p=0.2] Adiou *novecentos.* [p=0.4] {c}Por isso, "
        "[p=0.2] cem sobre novecentos. [p=0.2] Repare: [p=0.2] a taxa certa é sempre a *maior,* [p=0.2] porque o "
        "financiado é o *menor denominador.*"),

    # ================= BLOCO D: O "SEM JUROS" =================
    dict(id="10", block="semjuros", text=
        "{t}E os dez vezes sem juros? [p=0.4] {a}Dez parcelas que somam *mil reais.* [p=0.2] À vista, *novecentos.* "
        "[p=0.4] {b}O preço de verdade é o de *quem paga hoje:* [p=0.2] *novecentos.* [p=0.4] {c}Os outros cem [p=0.2] "
        "são *juros embutidos:* [p=0.2] juros que vêm escondidos dentro do preço cheio."),
    dict(id="11", block="semjuros", text=
        "{t}Então nunca existe sem juros? [p=0.4] {a}Existe, [p=0.2] quando o preço à vista e o total parcelado são "
        "*iguais.* [p=0.4] {b}Mas, se tem *desconto à vista,* [p=0.2] o sem juros é um *preço com fantasia.* [p=0.2] "
        "O preço real é o à vista. [p=0.2] A diferença são juros. [p=0.4] {c}E com *várias parcelas?* [p=0.2] O ENEM "
        "dá um fator pronto, [p=0.2] ou pede só a comparação. [p=0.2] Isso fica para a série de *Comparação de "
        "propostas.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="12", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}*Mil e cem reais* à vista, [p=0.2] ou *duas de seiscentos,* [p=0.2] a primeira no ato "
        "[p=0.2] e a segunda em trinta dias. [p=0.4] {b}Qual é a taxa mensal embutida? [p=0.3] {c}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="13", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Os primeiros seiscentos *não viajam.* [p=0.2] Financiado: [p=0.2] mil e cem menos "
        "seiscentos, [p=0.2] *quinhentos.* [p=0.4] {b}Daqui a um mês, [p=0.2] você paga seiscentos. [p=0.2] Juros de "
        "*cem.* [p=0.4] {c}Cem sobre quinhentos: [p=0.2] *vinte por cento ao mês.* [p=0.2] Bem maior que os cem sobre "
        "mil e cem."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="14", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] a entrada não é financiada: [p=0.2] divida os juros só "
        "pelo que ficou para depois. [p=0.5] {b}Dois: [p=0.2] taxa embutida é igual a juros dividido pelo valor "
        "financiado. [p=0.5] {c}Três: [p=0.2] se existe desconto à vista, o sem juros tem juros."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="15", block="erros", text=
        "{t}Os dois erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] calcular a taxa sobre o *preço total.* [p=0.2] Na "
        "geladeira, [p=0.2] cem sobre dois mil. [p=0.4] {b}Parece certo, [p=0.2] porque dois mil é tudo o que você "
        "paga. [p=0.4] {c}Mas a entrada *não foi emprestada.* [p=0.2] Divida só pelo que ficou para depois."),
    dict(id="16", block="erros", text=
        "{a}Segundo: [p=0.2] *acreditar no sem juros* [p=0.2] quando existe desconto à vista. [p=0.4] {b}Parece certo: "
        "[p=0.2] está escrito no anúncio, [p=0.2] em letra grande. [p=0.4] {c}Mas compare os dois preços. [p=0.2] Se "
        "o à vista é *menor,* [p=0.2] a diferença é juros."),

    # ================= QUESTÃO 1 (VOCÊ FAZ) =================
    dict(id="17", block="q1", text=
        "{t}Agora é com você, [p=0.2] uma questão no estilo do ENEM [p=0.2] do nosso material de estudo. [p=0.4] {a}Uma "
        "loja anuncia um aparelho por *duas de quinhentos reais, sem juros,* [p=0.2] a primeira no ato da compra "
        "[p=0.2] e a segunda trinta dias depois. [p=0.2] À vista, [p=0.2] o mesmo aparelho sai por *novecentos reais.* "
        "[p=0.2] A taxa mensal de juros efetivamente cobrada [p=0.2] de quem escolhe o parcelamento é de: [p=0.4] "
        "{qa}A: [p=0.2] zero por cento, como afirma o anúncio. [p=0.3] {qb}B: [p=0.2] dez por cento. [p=0.3] {qc}C: "
        "[p=0.2] onze vírgula um. [p=0.3] {qd}D: [p=0.2] vinte. [p=0.3] {qe}E: [p=0.2] vinte e cinco por cento. "
        "[p=0.4] {p}*Pause o vídeo e resolva sozinho.* [p=2.5]"),
    dict(id="18", block="q1", text=
        "{t}Vamos conferir. [p=0.3] {a}A primeira parcela é paga no ato: [p=0.2] é a entrada, [p=0.2] *não viaja.* "
        "[p=0.4] {b}Financiado: [p=0.2] novecentos menos quinhentos, [p=0.2] *quatrocentos.* [p=0.2] Daqui a trinta "
        "dias, [p=0.2] você paga quinhentos. [p=0.2] Juros de *cem.* [p=0.4] {c}Cem sobre quatrocentos: [p=0.2] *vinte "
        "e cinco por cento ao mês.* [p=0.3] {ok}*Letra E!*"),
    dict(id="19", block="q1", text=
        "{t}E as pegadinhas? [p=0.3] {xa}A A *acredita no anúncio.* [p=0.2] Mas tem desconto à vista, [p=0.2] então "
        "tem juros. [p=0.4] {xb}A B divide os cem por *mil,* [p=0.2] o total a prazo. [p=0.4] {xc}A C divide por "
        "*novecentos,* [p=0.2] o preço à vista. [p=0.4] {xd}E a D divide por *quinhentos,* [p=0.2] a parcela. [p=0.4] "
        "{c}Todos *maiores* que os quatrocentos emprestados. [p=0.2] E repare: [p=0.2] onze vírgula um e vinte [p=0.2] "
        "foram as respostas dos *outros exemplos.* [p=0.2] Aqui, são armadilhas."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="20", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] a entrada não é financiada: [p=0.2] divida os "
        "juros só pelo que ficou para depois. [p=0.5] {b}Dois: [p=0.2] taxa embutida é igual a juros dividido pelo "
        "valor financiado. [p=0.5] {c}Três: [p=0.2] se existe desconto à vista, o sem juros tem juros."),

    # ================= PONTE E CTA =================
    dict(id="21", block="ponte", text=
        "{a}Num financiamento de *dez mil reais* em cinco parcelas, [p=0.2] a dívida cai *dois mil reais por mês.* "
        "[p=0.4] {b}E os juros, [p=0.2] caem também? [p=0.4] {c}Próximo episódio: [p=0.2] *SAC.*"),
    dict(id="22", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual foi o último sem juros que você viu [p=0.2] que tinha "
        "desconto à vista? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir "
        "os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos "
        "minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
