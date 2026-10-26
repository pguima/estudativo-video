# Roteiro — Progressão Aritmética, Episódio 4 de 5: a PA disfarçada (juros simples, calendário, SAC)
# Base: Estudos/Enem/estudos/01-matematica/31-progressao-aritmetica.html — seção 08 + Questão 7 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (do prompt):
#   A ESCADA DE DEGRAUS IGUAIS (a mesma do episódio 1): juros simples sobem sempre o mesmo degrau, C · i.
#   O TERMO ZERO É O CHÃO: o dinheiro aplicado HOJE ainda não subiu nenhum degrau.
#   A SEMANA É UMA PA DE RAZÃO 7.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Revisões sem reensinar: Juros Simples (J = C · i · t, M = C + J) e SAC (série de Empréstimos: R$ 10.000,00 a 4% em
#   5 parcelas, amortização R$ 2.000,00 → juros 400, 320, 240, 160, 80; total (400 + 80) · 5 ÷ 2 = 1.200).
# Exemplos do material/prompt: tabela da seção 08 (juros R$ 60 ao mês para R$ 2.000 a 3%) · calendário: dia 3 segunda →
#   3, 10, 17, 24, 31 · nós fazemos: dia 4 terça → dia 29: 25 dias = 3 · 7 + 4 → sábado.
# Exemplos NOSSOS (conferidos em Python, trabalho/conferir_contas.py): bloco b, mês 5 → 2.000 + 5 · 60 = 2.300 (não é a
#   Q7) · bloco c, dia 3 segunda → dia 20: 17 dias = 2 · 7 + 3 → quinta · erro 1 com o gancho (R$ 1.000 a 3%): mês 6 =
#   1.180 (certo) × 1.150 (errado, é o mês 5) · erro 3: juros do SAC tratados como constantes, 400 · 5 = 2.000 contra
#   1.200 · CTA: dia 1 domingo → dia 30: 29 = 4 · 7 + 1 → segunda.
# Atalhos (NOSSOS, verde): "montante = chão + n degraus" · "conte as diferenças, não os dias: o resto diz quantos dias
#   andar" · "na dúvida, teste o mês 1: tem que dar capital + um juro".
# QUESTÃO 7 (você faz): 2.000 + 60n = 3.080 → n = 18 (B). Erradas (material): A = parte de 2.060 e esquece o + 1
#   ((3.080 − 2.060) ÷ 60 = 17) · C = 2.000 como termo 1, 2.000 + (n − 1) · 60 → 19 · D = juro de R$ 30 ao mês (1.080 ÷ 30
#   = 36) · E = divide o montante inteiro por 60 (3.080 ÷ 60 ≈ 51).
# Frases-chave (meio e fim, idênticas): 1. Aumento constante é PA, mesmo sem o nome. 2. Juros simples: o capital é o
#   termo zero. 3. A semana é uma PA de razão 7: olhe o resto da divisão.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "A PA escondida: juros simples, calendário e financiamentos | PA Ep. 4"
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
        "{a}Você já estudou PA sem saber: [p=0.3] na série de Juros Simples, [p=0.2] os montantes de *mil reais* a "
        "*três por cento ao mês* eram [p=0.2] {b}mil e trinta, [p=0.2] mil e sessenta, [p=0.2] mil e noventa... "
        "[p=0.4] {c}*Degraus de trinta reais.* [p=0.4] {d}Hoje você reconhece a *PA escondida* em qualquer enunciado."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai identificar a PA em *juros simples,* [p=0.2] *calendários,* [p=0.2] "
        "*depreciação,* [p=0.2] *treinos* e *financiamentos,* [p=0.3] {b}e não errar o *mês um.*"),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Da série de Juros Simples: [p=0.2] o dinheiro aplicado é o *capital;* "
        "[p=0.2] a *taxa* diz quanto ele rende por mês. [p=0.2] Juro é *capital vezes taxa vezes tempo,* [p=0.2] e o "
        "*montante* é capital mais juro. [p=0.4] {b}E do episódio um: [p=0.2] o termo de posição *n* é o primeiro "
        "termo *mais n menos um* razões."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Olhe três papéis do dia a dia. [p=0.4] {a}Um *extrato* de aplicação. [p=0.3] {b}Uma folha de "
        "*calendário.* [p=0.3] {c}E um *boleto de financiamento* que diminui todo mês. [p=0.4] {d}Os três escondem a "
        "mesma coisa: [p=0.2] *um aumento ou uma queda sempre igual.*"),

    # ================= BLOCO A: ONDE A PA SE ESCONDE =================
    dict(id="05", block="tabela", text=
        "{t}Onde mais a PA se esconde? [p=0.4] {a}Nos *juros simples:* [p=0.2] o juro de cada mês é o mesmo. [p=0.3] "
        "{b}Na *depreciação linear:* [p=0.2] o carro perde o *mesmo valor* todo ano. [p=0.2] A razão é *negativa.* "
        "[p=0.3] {c}No *calendário:* [p=0.2] a semana se repete a cada *sete dias.* [p=0.3] {d}No *treino "
        "progressivo,* [p=0.2] que aumenta a mesma distância por dia. [p=0.3] {e}E nas *figuras* que ganham sempre as "
        "mesmas peças."),

    # ================= BLOCO B: JUROS SIMPLES, O TERMO ZERO =================
    dict(id="06", block="juros", text=
        "{t}Onde fica o *chão* dessa escada? [p=0.4] {a}*Dois mil reais* a três por cento ao mês. [p=0.2] O degrau é "
        "*capital vezes taxa:* [p=0.2] *sessenta reais.* [p=0.4] {b}No dia da aplicação, [p=0.2] o dinheiro ainda não "
        "subiu nenhum degrau: [p=0.2] *dois mil, no chão.* [p=0.4] {c}Esse é o *termo zero:* [p=0.2] o valor no "
        "instante da aplicação, [p=0.2] *antes* do primeiro mês."),
    dict(id="07", block="juros", text=
        "{t}E o fim do mês um? [p=0.4] {a}Já subiu *um degrau:* [p=0.2] dois mil e sessenta. [p=0.2] Mês dois, [p=0.2] "
        "dois degraus. [p=0.4] {b}Então o montante do mês *n* é o chão *mais n degraus:* [p=0.2] *dois mil mais "
        "sessenta vezes n.* [p=0.4] {c}Mês cinco: [p=0.2] dois mil mais trezentos, [p=0.2] *dois mil e trezentos.* "
        "[p=0.3] Atalho: [p=0.2] *montante é o chão mais n degraus.*"),

    # ================= BLOCO C: CALENDÁRIO =================
    dict(id="08", block="calendario", text=
        "{t}E o calendário, o que tem de PA? [p=0.4] {a}Se o dia *três* é uma segunda-feira, [p=0.2] a próxima "
        "segunda é o dia *dez.* [p=0.3] {b}Depois *dezessete,* [p=0.2] *vinte e quatro,* [p=0.2] *trinta e um.* "
        "[p=0.4] {c}A semana é uma *PA de razão sete.*"),
    dict(id="09", block="calendario", text=
        "{t}E uma data mais longe? [p=0.4] {a}Dia três é segunda. [p=0.2] Que dia é o *vinte?* [p=0.3] Conte a "
        "*distância:* [p=0.2] vinte menos três, [p=0.2] *dezessete dias.* [p=0.4] {b}Divida por sete: [p=0.2] duas "
        "semanas inteiras, [p=0.2] e *sobram três.* [p=0.3] As semanas inteiras voltam para a segunda. [p=0.4] "
        "{c}Segunda mais três dias: [p=0.2] *quinta-feira.* [p=0.3] Atalho: [p=0.2] *o resto diz quantos dias "
        "andar.*"),

    # ================= BLOCO D: SAC (SÓ CITADO) =================
    dict(id="10", block="sac", text=
        "{t}E o boleto que diminui? [p=0.4] {a}Na série de Empréstimos você viu o *SAC.* [p=0.2] Cada parcela abate a "
        "mesma *amortização:* [p=0.2] a parte que paga a dívida em si. [p=0.4] {b}Como a dívida cai sempre igual, "
        "[p=0.2] os juros caem em PA: [p=0.2] *quatrocentos, trezentos e vinte, duzentos e quarenta, cento e "
        "sessenta, oitenta.* [p=0.4] {c}Razão *menos oitenta.*"),

    # ================= BLOCO E: PONTE COM A FUNÇÃO AFIM =================
    dict(id="11", block="afim", text=
        "{t}E por que tudo isso parece uma *reta?* [p=0.4] {a}Porque PA é *função afim* nos números naturais. "
        "[p=0.3] {b}A razão é a *taxa de variação.* [p=0.2] O termo zero é o *valor inicial.* [p=0.4] {c}Montante "
        "de juros simples: [p=0.2] *pontos alinhados numa reta,* [p=0.2] como na série de Função Afim."),

    # ================= NÓS FAZEMOS =================
    dict(id="12", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Num mês, [p=0.2] o dia *quatro* é uma *terça-feira.* [p=0.3] {b}Que dia da semana é o "
        "dia *vinte e nove?* [p=0.3] {c}*Pause e tente.* [p=2.0]"),
    dict(id="13", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Distância: [p=0.2] vinte e nove menos quatro, [p=0.2] *vinte e cinco dias.* "
        "[p=0.4] {b}Divida por sete: [p=0.2] *três* semanas inteiras, [p=0.2] e *sobram quatro.* [p=0.4] {c}Terça "
        "mais quatro dias: [p=0.2] quarta, quinta, sexta, [p=0.2] *sábado!*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="14", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] aumento constante é PA, mesmo sem o nome. [p=0.5] "
        "{b}Dois: [p=0.2] juros simples: o capital é o termo zero. [p=0.5] {c}Três: [p=0.2] a semana é uma PA de "
        "razão sete: olhe o resto da divisão."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="15", block="erros", text=
        "{t}Os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] tratar o capital como *termo um* [p=0.2] e usar "
        "*n menos um* degraus. [p=0.2] Mil reais a três por cento, mês seis: [p=0.2] sai *mil cento e cinquenta.* "
        "[p=0.4] {b}Parece certo: [p=0.2] é a fórmula do episódio um. [p=0.4] {c}Mas o capital é o *chão,* o mês "
        "zero. [p=0.2] No mês seis já são seis degraus: [p=0.2] *mil cento e oitenta.*"),
    dict(id="16", block="erros", text=
        "{a}Segundo: [p=0.2] contar o *próprio dia de partida.* [p=0.2] Do dia quatro ao vinte e nove, [p=0.2] contar "
        "*vinte e seis* dias. [p=0.4] {b}Parece certo: [p=0.2] o dia quatro está ali, no calendário. [p=0.4] {c}Mas "
        "você *já está* nele. [p=0.2] O que conta são os *saltos:* [p=0.2] *vinte e cinco.*"),
    dict(id="17", block="erros", text=
        "{a}Terceiro: [p=0.2] achar que os juros do SAC são *sempre iguais.* [p=0.2] Quatrocentos vezes cinco, [p=0.2] "
        "*dois mil.* [p=0.4] {b}Parece certo: [p=0.2] a amortização é constante. [p=0.4] {c}Mas os juros caem junto "
        "com a dívida. [p=0.2] A soma da PA dá *mil e duzentos.*"),

    # ================= QUESTÃO 7 (VOCÊ FAZ) =================
    dict(id="18", block="q7", text=
        "{t}Agora é com você, [p=0.2] numa questão do nosso material de estudo. [p=0.4] {a}Um capital de *dois mil "
        "reais* foi aplicado a juros simples de *três por cento ao mês.* [p=0.2] Os montantes ao fim de cada mês "
        "formam uma PA. [p=0.2] O montante atinge *três mil e oitenta reais* ao fim do mês de número: [p=0.4] "
        "{qa}A: [p=0.2] dezessete. [p=0.3] {qb}B: [p=0.2] dezoito. [p=0.3] {qc}C: [p=0.2] dezenove. [p=0.3] {qd}D: "
        "[p=0.2] trinta e seis. [p=0.3] {qe}E: [p=0.2] cinquenta e um. [p=0.4] {p}*Pause o vídeo e resolva "
        "sozinho.* [p=2.5]"),
    dict(id="19", block="q7", text=
        "{t}Vamos conferir. [p=0.3] {a}Primeiro, o que é o mês zero? [p=0.2] O dia da aplicação: [p=0.2] *dois mil, "
        "no chão.* [p=0.4] {b}Degrau: [p=0.2] três por cento de dois mil, [p=0.2] *sessenta.* [p=0.2] Dois mil mais "
        "sessenta vezes n [p=0.2] igual a três mil e oitenta. [p=0.4] {c}Sessenta vezes n dá *mil e oitenta.* "
        "[p=0.2] n igual a *dezoito.* [p=0.3] {d}Confira: [p=0.2] dezoito meses de sessenta reais, [p=0.2] mil e "
        "oitenta de juros. [p=0.3] {ok}*Letra B!*"),
    dict(id="20", block="q7", text=
        "{t}E as pegadinhas? [p=0.3] {xc}A C chama os dois mil de *termo um* [p=0.2] e usa n menos um: [p=0.2] chega "
        "a dezenove. [p=0.4] {xa}A A parte de dois mil e sessenta [p=0.2] e *esquece de somar um.* [p=0.4] {xd}A D "
        "usa juro de *trinta* por mês. [p=0.4] {xe}E a E divide o *montante inteiro* por sessenta."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="21", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] aumento constante é PA, mesmo sem o nome. "
        "[p=0.5] {b}Dois: [p=0.2] juros simples: o capital é o termo zero. [p=0.5] {c}Três: [p=0.2] a semana é uma "
        "PA de razão sete: olhe o resto da divisão."),

    # ================= PONTE E CTA =================
    dict(id="22", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos tudo, [p=0.3] {b}caçamos as pegadinhas [p=0.3] {c}e "
        "treinamos para o ENEM."),
    dict(id="23", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] se o dia primeiro de um mês é domingo, [p=0.2] que dia da semana "
        "é o dia trinta? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir "
        "os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos "
        "minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
