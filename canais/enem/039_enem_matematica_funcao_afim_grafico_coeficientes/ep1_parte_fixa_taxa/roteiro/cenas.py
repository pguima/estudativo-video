# Roteiro — Função Afim, Episódio 1 de 5: parte fixa + taxa (o que é função afim e onde você já a viu disfarçada)
# Base: Estudos/Enem/estudos/01-matematica/24-funcao-afim-grafico-coeficientes.html — seção 02 e os trechos
#   "Proporcional só quando b = 0" e "A regra de três que o ENEM quer que você faça" (seção 08) + Questões 2 e 9 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O TÁXI: a bandeirada é o b (você paga mesmo parado) e o taxímetro é o a (quanto sobe a cada quilômetro).
#   OS DISFARCES: na proporção direta a bandeirada era zero (b = 0); no juro simples o capital é a bandeirada
#     e os juros de cada mês são o taxímetro.
#   A BANDEIRADA NÃO DOBRA: regra de três só funciona quando b = 0.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Taxa Δy/Δx e gráfico ficam para os episódios 2 e 3 (aqui o gráfico só é citado: "é sempre uma reta").
# Bloco e (plano 40 + 0,50 por minuto) = mesmos números da Questão 2, que é "eu faço" (repetição permitida, como no prompt).
# Bloco f (mola, 5 kg → 35 cm) = o gancho. A lei L(m) = 20 + 3m NÃO é escrita antes da Questão 9 ("você faz"):
#   o bloco mostra só "3 cm por kg" e o caminho de ida; a Q9 pede o caminho de volta (32 cm → massa).
# Nós fazemos (prompt): S(v) = 1 500 + 0,04v → S(10 000) = 1 900; S(20 000) = 2 300 (não 3 800).
# QUESTÃO 2 ("eu faço", com pausa): gabarito C (R$ 140,00). Erradas = material (D regra de três 2·90 = 180; E 180 + 40 = 220;
#   A esquece a mensalidade, 0,5·200 = 100; B soma à conta antiga a mensalidade, 90 + 40 = 130).
# QUESTÃO 9 ("você faz", com pausa): gabarito B (4 kg). Erradas = material (A regra de três com o total, 32·2/26 ≈ 2,5;
#   D 32 ÷ 3 ≈ 10,7 esquece os 20 cm; E 32 ÷ 2 = 16; C 12 ÷ 2 = 6 usa a massa de referência como taxa).
# Acréscimos NOSSOS (marcados): atalho verde "ache o a e o b pelos NOMES" (cena 07); atalho verde "teste do zero"
#   (cena 13: com x = 0 o y dá zero? só então vale regra de três); atalho verde "tire o fixo, faça a proporção no resto,
#   devolva o fixo" (cena 15). Erro 1 usa o táxi (10 km = R$ 30,00; 20 km = R$ 55,00, não R$ 60,00), para não repetir a Q2.
# Frases-chave (meio e fim, idênticas): 1. a é quanto muda por unidade; b é quanto vale no início.
#   2. Proporcional é o caso especial com b = 0. 3. Com parte fixa, dobrar o x não dobra o y.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Função afim do zero: parte fixa + taxa | Função Afim Ep. 1"
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
        "{a}Uma mola de *vinte centímetros* [p=0.2] passa a medir *vinte e seis centímetros* [p=0.2] com *dois quilos* "
        "pendurados. [p=0.5] {b}Com *cinco quilos,* [p=0.2] a regra de três diz *sessenta e cinco centímetros.* [p=0.4] "
        "{c}A mola real mede *trinta e cinco.* [p=0.5] {d}A regra de três errou por *quase o dobro,* [p=0.3] e o ENEM "
        "sabe disso."),
    dict(id="02", block="promessa", text=
        "{t}Este é o primeiro episódio da série de *Função afim.* [p=0.4] {a}Ao final desta aula, [p=0.2] você vai "
        "*reconhecer uma função afim* em qualquer texto, [p=0.3] {b}dar nome aos *dois números* dela [p=0.3] {c}e saber "
        "quando a *regra de três* funciona [p=0.2] e quando ela te engana."),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Da série de Conceito de Função: [p=0.2] função é uma *máquina,* [p=0.2] "
        "entra o x, [p=0.2] sai o *f de x.* [p=0.4] {b}Da série de Grandezas Proporcionais: [p=0.2] *y igual a k x,* "
        "[p=0.2] a reta que passa pela origem. [p=0.4] {c}E da série de Juros Simples: [p=0.2] o montante, [p=0.2] "
        "*M igual a C mais C vezes i vezes t.* [p=0.3] Só isso."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}O que estas três contas têm em comum? [p=0.4] {a}O *táxi:* [p=0.2] a bandeirada, [p=0.2] e depois um valor "
        "por quilômetro. [p=0.4] {b}O *celular:* [p=0.2] a mensalidade, [p=0.2] e depois um valor por minuto. [p=0.4] "
        "{c}O *salário* do vendedor: [p=0.2] o fixo, [p=0.2] e depois a comissão. [p=0.4] {d}Nas três, [p=0.2] uma "
        "*parte fixa* [p=0.2] e uma parte que *cresce no mesmo ritmo.*"),

    # ================= BLOCO A: O TÁXI E A DEFINIÇÃO =================
    dict(id="05", block="taxi", text=
        "{t}Por que o táxi já cobra antes de sair? [p=0.4] {a}Você entra, [p=0.2] o carro nem andou, [p=0.2] e o "
        "taxímetro já marca *cinco reais.* [p=0.2] É a *bandeirada:* [p=0.2] você paga mesmo parado. [p=0.4] {b}Agora o carro anda. [p=0.2] Um "
        "quilômetro: [p=0.2] *mais dois e cinquenta.* [p=0.2] Outro quilômetro: [p=0.2] mais dois e cinquenta. [p=0.2] Sempre o mesmo "
        "ritmo. [p=0.4] {c}O preço é *cinco,* [p=0.2] mais *dois e cinquenta* vezes os quilômetros."),
    dict(id="06", block="definicao", text=
        "{t}Isso tem nome. [p=0.3] {a}Uma *função afim* [p=0.2] é uma função da forma *f de x igual a a x mais b.* "
        "[p=0.4] {b}O *a* é o *coeficiente angular,* [p=0.2] ou *taxa de variação:* [p=0.2] quanto o resultado muda "
        "a cada unidade de x. [p=0.2] No táxi, [p=0.2] dois e cinquenta *por quilômetro.* [p=0.4] {c}O *b* é o "
        "*coeficiente linear,* [p=0.2] ou *valor inicial:* [p=0.2] quanto vale quando x é zero. [p=0.2] No táxi, "
        "[p=0.2] cinco reais *fixos.* [p=0.4] {d}E o desenho dela [p=0.2] é sempre uma *reta.* [p=0.2] Isso fica para o "
        "episódio três."),
    dict(id="07", block="nomes", text=
        "{t}E como achar o a e o b num texto? [p=0.4] {a}Atalho: [p=0.2] *pelos nomes.* [p=0.4] {b}O *b* aparece como "
        "*fixo,* [p=0.2] *inicial,* [p=0.2] *mensalidade,* [p=0.2] *sem carga.* [p=0.4] {c}O *a* aparece com a "
        "palavrinha *por:* [p=0.2] por quilômetro, [p=0.2] por minuto, [p=0.2] por quilo. [p=0.4] {d}E escreva a "
        "unidade ao lado: [p=0.2] reais fixos, [p=0.2] reais por minuto."),

    # ================= BLOCO B: OS CASOS PARTICULARES =================
    dict(id="08", block="casos", text=
        "{t}E se um dos dois números for zero? [p=0.4] {a}O caso geral é o táxi: [p=0.2] *cinco mais dois e cinquenta "
        "d.* [p=0.4] {b}Se o *b é zero,* [p=0.2] sobra só a x. [p=0.2] Isso é a *função linear.* [p=0.3] Combustível a "
        "seis reais o litro: [p=0.2] *seis L.* [p=0.2] Sem nada fixo. [p=0.4] {c}E se, além disso, [p=0.2] o a for "
        "*um,* [p=0.2] sobra *f de x igual a x:* [p=0.2] a *função identidade.* [p=0.2] Sai exatamente o que entrou."),
    dict(id="09", block="casos", text=
        "{t}E se o *a* for zero? [p=0.4] {a}Aí o x não muda nada. [p=0.2] É a *função constante.* [p=0.4] {b}Uma "
        "mensalidade fixa de *noventa e nove e noventa:* [p=0.2] usou pouco, [p=0.2] usou muito, [p=0.2] paga o "
        "mesmo. [p=0.4] {c}Para a prova, [p=0.2] o que importa é ver a estrutura: [p=0.2] *parte fixa* [p=0.2] mais "
        "*parte proporcional a x.*"),

    # ================= BLOCO C E D: OS DISFARCES =================
    dict(id="10", block="disfarce", text=
        "{t}E você já viu isso antes? [p=0.4] {a}Viu, [p=0.2] *disfarçado.* [p=0.3] Na série de Grandezas "
        "Proporcionais, [p=0.2] *y igual a k x* [p=0.2] era a função *linear:* [p=0.2] uma função afim com a "
        "bandeirada *zero.* [p=0.4] {b}E aquela reta que *não passava pela origem?* [p=0.3] {c}Era uma afim *com "
        "parte fixa.* [p=0.2] O táxi de novo. [p=0.4] {d}Ou "
        "seja: [p=0.2] a proporção direta [p=0.2] é só um *caso especial* da função afim."),
    dict(id="11", block="disfarce", text=
        "{t}E o segundo disfarce? [p=0.4] {a}Na série de Juros Simples: [p=0.2] mil reais a cinco por cento ao mês. "
        "[p=0.2] O montante é *mil, [p=0.2] mais cinquenta vezes t.* [p=0.4] {b}O *b* é mil: [p=0.2] o *capital,* "
        "[p=0.2] a bandeirada. [p=0.3] {c}O *a* é cinquenta: [p=0.2] os *juros de cada mês,* [p=0.2] o taxímetro. "
        "[p=0.4] {d}A mesma estrutura, [p=0.2] com outra roupa."),

    # ================= BLOCO E: PROPORCIONAL SÓ QUANDO b = 0 =================
    dict(id="12", block="dobro", text=
        "{t}Então dobrar o x [p=0.2] sempre dobra o y? [p=0.4] {a}Duas grandezas são *proporcionais* [p=0.2] quando "
        "dobrar uma dobra a outra, [p=0.2] triplicar triplica. [p=0.3] Será que é sempre assim? [p=0.4] Um plano de celular: [p=0.2] *quarenta reais* fixos, "
        "[p=0.2] mais *cinquenta centavos* por minuto. [p=0.4] {b}Cem minutos: [p=0.2] quarenta mais cinquenta, "
        "[p=0.2] *noventa reais.* [p=0.4] {c}Duzentos minutos: [p=0.2] quarenta mais cem, [p=0.2] *cento e quarenta.* "
        "[p=0.4] {d}Dobrou o consumo, [p=0.2] mas a conta *não dobrou:* [p=0.2] dobrar daria cento e oitenta. [p=0.3] "
        "*A bandeirada não dobra.*"),
    dict(id="13", block="zero", text=
        "{t}E como saber se a regra de três vale? [p=0.4] {a}Atalho: [p=0.2] o *teste do zero.* [p=0.4] {b}Pergunte: "
        "[p=0.2] com x igual a zero, [p=0.2] o resultado dá *zero?* [p=0.3] Combustível: [p=0.2] zero litro, [p=0.2] "
        "zero real. [p=0.2] *Pode* regra de três. [p=0.4] {c}Celular: [p=0.2] zero minuto, [p=0.2] *quarenta reais.* "
        "[p=0.2] Tem parte fixa: [p=0.2] *não pode.* [p=0.4] "
        "{d}Dez segundos de teste [p=0.2] que salvam a questão inteira."),

    # ================= BLOCO F: A MOLA =================
    dict(id="14", block="mola", text=
        "{t}E a mola do começo? [p=0.4] {a}Ela tem *vinte centímetros* sem nada pendurado. [p=0.2] Esse é o fixo. "
        "[p=0.4] {b}Com dois quilos, [p=0.2] vai a vinte e seis. [p=0.2] O que cresceu foram *seis centímetros.* "
        "[p=0.2] Isso se chama *alongamento:* [p=0.2] quanto a mola esticou além do tamanho dela. [p=0.4] {c}O "
        "proporcional ao peso [p=0.2] é o *alongamento.* [p=0.2] Seis para dois quilos: [p=0.2] *três centímetros por "
        "quilo.* [p=0.4] {d}Cinco quilos: [p=0.2] *quinze* de alongamento. [p=0.2] Mais os vinte fixos: [p=0.2] "
        "*trinta e cinco.*"),
    dict(id="15", block="tirefixo", text=
        "{t}Guarde a receita. [p=0.3] {a}Atalho: [p=0.2] *tire o fixo, [p=0.2] faça a proporção no resto, [p=0.2] "
        "devolva o fixo.* [p=0.4] {b}A regra de três *pode* entrar, [p=0.2] mas só na parte que cresce. [p=0.4] {c}Essa "
        "é a regra de três que o ENEM *quer* que você faça."),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Um vendedor ganha *mil e quinhentos reais* fixos, [p=0.2] mais *quatro por cento* das "
        "vendas. [p=0.4] {b}Quanto ele recebe [p=0.2] vendendo *dez mil reais?* [p=0.3] {c}E vendendo o dobro, "
        "[p=0.2] vinte mil, [p=0.2] ele recebe *o dobro?* [p=0.4] {d}*Pause e tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}O fixo é o b: [p=0.2] mil e quinhentos. [p=0.2] O a é quatro por cento, [p=0.2] "
        "*zero vírgula zero quatro* por real vendido. [p=0.4] {b}Dez mil: [p=0.2] quatro por cento de dez mil é "
        "*quatrocentos.* [p=0.2] Mil e quinhentos mais quatrocentos: [p=0.2] *mil e novecentos.* [p=0.4] {c}Vinte mil: "
        "[p=0.2] a comissão é *oitocentos.* [p=0.2] Total: [p=0.2] *dois mil e trezentos.* [p=0.4] {d}O dobro seria "
        "três mil e oitocentos. [p=0.2] *Não dobrou:* [p=0.2] o fixo não dobra."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] a é quanto muda por unidade; [p=0.2] b é quanto vale "
        "no início. [p=0.5] {b}Dois: [p=0.2] proporcional é o caso especial com b igual a zero. [p=0.5] {c}Três: "
        "[p=0.2] com parte fixa, [p=0.2] dobrar o x não dobra o y."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os dois erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] usar *regra de três* quando há parte fixa. "
        "[p=0.2] Táxi: [p=0.2] dez quilômetros, trinta reais. [p=0.2] Vinte quilômetros: [p=0.2] *sessenta?* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque mais quilômetro é mais dinheiro, [p=0.2] e a gente associa isso a "
        "proporção. [p=0.4] {c}Mas a bandeirada não dobra. [p=0.2] Cinco mais cinquenta: [p=0.2] *cinquenta e "
        "cinco.*"),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] fazer a proporção com o *comprimento total* da mola. [p=0.2] Vinte e seis para dois "
        "quilos, [p=0.2] logo sessenta e cinco para cinco. [p=0.4] {b}Parece certo, [p=0.2] porque o enunciado só "
        "mostra o comprimento. [p=0.4] {c}Mas o proporcional é o *alongamento.* [p=0.2] Tire os vinte, [p=0.2] faça a "
        "proporção, [p=0.2] devolva os vinte."),

    # ================= QUESTÃO 2 (EU FAÇO) =================
    dict(id="21", block="q2", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] Esta, [p=0.2] eu resolvo com você. [p=0.4] {a}Um plano de "
        "celular cobra uma mensalidade fixa [p=0.2] mais um valor constante por minuto. [p=0.3] Com *cem minutos,* "
        "[p=0.2] a conta foi de *noventa reais;* [p=0.2] a mensalidade é de *quarenta.* [p=0.3] Com *duzentos "
        "minutos,* [p=0.2] a conta será de: [p=0.3] {qa}A: [p=0.2] cem reais. [p=0.2] {qb}B: [p=0.2] cento e trinta. "
        "[p=0.2] {qc}C: [p=0.2] cento e quarenta. [p=0.2] {qd}D: [p=0.2] cento e oitenta. [p=0.2] {qe}E: [p=0.2] "
        "duzentos e vinte. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="22", block="q2", text=
        "{t}Pelos nomes. [p=0.3] {a}*Mensalidade fixa:* [p=0.2] o b, [p=0.2] quarenta reais. [p=0.2] *Por minuto:* "
        "[p=0.2] o a, [p=0.2] que o enunciado não deu. [p=0.4] {b}Os cem minutos custaram noventa menos quarenta, "
        "[p=0.2] *cinquenta reais.* [p=0.2] Cinquenta dividido por cem: [p=0.2] *cinquenta centavos* por minuto. "
        "[p=0.4] {c}Duzentos minutos: [p=0.2] quarenta mais duzentos vezes zero vírgula cinco, [p=0.2] quarenta mais "
        "cem, [p=0.2] *cento e quarenta.* [p=0.3] {d}Conferindo com cem minutos: [p=0.2] quarenta mais cinquenta, "
        "[p=0.2] noventa. [p=0.2] Bate. [p=0.3] {ok}*Letra C!*"),
    dict(id="23", block="q2", text=
        "{t}E as armadilhas? [p=0.3] {xd}A D é a regra de três: [p=0.2] dois vezes noventa, [p=0.2] dobrando também "
        "a mensalidade. [p=0.4] {xe}A E dobra a conta [p=0.2] e soma a mensalidade *de novo.* [p=0.4] {xa}A A esquece "
        "a mensalidade. [p=0.4] {xb}E a B soma à conta antiga a mensalidade, [p=0.2] em vez dos cem minutos a mais."),

    # ================= QUESTÃO 9 (VOCÊ FAZ) =================
    dict(id="24", block="q9", text=
        "{t}E esta é *sua.* [p=0.3] {a}Uma mola tem *vinte centímetros* sem carga. [p=0.2] Com um objeto de *dois "
        "quilos,* [p=0.2] passa a *vinte e seis.* [p=0.3] O alongamento é proporcional à massa. [p=0.3] A massa que "
        "deixa a mola com *trinta e dois centímetros* é: [p=0.3] {qa}A: [p=0.2] cerca de dois e meio quilos. [p=0.2] "
        "{qb}B: [p=0.2] quatro quilos. [p=0.2] {qc}C: [p=0.2] seis quilos. [p=0.2] {qd}D: [p=0.2] cerca de dez "
        "vírgula sete. [p=0.2] {qe}E: [p=0.2] dezesseis quilos. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="25", block="q9", text=
        "{t}Conferindo. [p=0.3] {a}*Sem carga:* [p=0.2] o b, [p=0.2] vinte centímetros. [p=0.2] *Por quilo:* [p=0.2] "
        "seis centímetros para dois quilos, [p=0.2] *três por quilo.* [p=0.4] {b}O comprimento é vinte mais três "
        "vezes a massa. [p=0.2] Vinte mais três m [p=0.2] igual a trinta e dois. [p=0.4] {c}Tire o fixo: [p=0.2] "
        "sobram *doze* de alongamento. [p=0.2] Doze dividido por três: [p=0.2] *quatro quilos.* [p=0.3] {d}Conferindo: "
        "[p=0.2] vinte mais doze, [p=0.2] trinta e dois. [p=0.2] {ok}*Letra B!*"),
    dict(id="26", block="q9", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A faz regra de três com o *comprimento total.* [p=0.4] {xd}A D divide "
        "trinta e dois por três, [p=0.2] esquecendo os vinte iniciais. [p=0.4] {xe}A E divide trinta e dois por "
        "dois. [p=0.4] {xc}E a C divide os doze por dois, [p=0.2] usando a massa de referência como se fosse a taxa."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="27", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] a é quanto muda por unidade; [p=0.2] b é "
        "quanto vale no início. [p=0.5] {b}Dois: [p=0.2] proporcional é o caso especial com b igual a zero. [p=0.5] "
        "{c}Três: [p=0.2] com parte fixa, [p=0.2] dobrar o x não dobra o y."),

    # ================= PONTE E CTA =================
    dict(id="28", block="ponte", text=
        "{a}E quando o enunciado *não diz a taxa?* [p=0.4] {b}Uma vela mede *dezessete centímetros* aos dez minutos "
        "[p=0.2] e *treze centímetros* aos trinta minutos. [p=0.4] {c}Quanto ela derrete por minuto, [p=0.2] e quando "
        "acaba? [p=0.4] {d}Próximo episódio."),
    dict(id="29", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual conta da sua vida tem uma bandeirada escondida? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
