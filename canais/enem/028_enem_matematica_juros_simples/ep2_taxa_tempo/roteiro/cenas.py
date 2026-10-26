# Roteiro — Juros Simples, Episódio 2 de 5: taxa e tempo na mesma unidade (meses, anos, dias e o boleto atrasado)
# Base: Estudos/Enem/estudos/01-matematica/13-juros-simples.html — seções 04 e 08 + Questões 2, 9 e 5 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   TAXA E TEMPO FALAM A MESMA LÍNGUA: taxa mensal conversa com meses, taxa anual conversa com anos
#     (as duas FICHAS com bandeirinha; bandeiras diferentes = fórmula trancada com cadeado amarelo).
#   TRADUZA SÓ UM DOS DOIS: leve a taxa até o tempo OU o tempo até a taxa, nunca os dois (o cadeado abre).
#   A MULTA É O INGRESSO, OS JUROS DE MORA SÃO O TAXÍMETRO: a multa é cobrada uma vez, os juros correm a cada dia.
#   Do episódio 1: juros são o ALUGUEL DO DINHEIRO e "a conta de um mês só".
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos (do prompt/material): 45 dias (R$ 3.000,00 a 24% a.a. → 90 pelos dois caminhos) · 8 meses a 18% a.a. →
#   1,5% a.m. · conta de R$ 450,00 com 10 dias de atraso → 9,00 + 1,50 = R$ 460,50 · erro 2: R$ 1.000,00 a 2% a.m. por
#   2 anos → certo 480; 24% com 24 → 5.760 (12 vezes MAIS); 2% com 2 → 40 (12 vezes MENOS). O material diz "12 vezes menor"
#   nos dois casos; o vídeo mostra os dois sentidos, como o prompt manda.
#   Erro do boleto (NOSSO, com a conta de 450 para não entregar a Q5): mês inteiro → juros 4,50; taxa diária → juros 45.
# Nós fazemos (prompt): R$ 1.200,00 a 36% a.a. por 4 meses → 3% a.m.; um mês 36; quatro meses R$ 144,00.
# QUESTÃO 2 (eu faço): 18% ÷ 12 = 1,5% a.m.; 5.000 · 0,015 = 75 por mês; × 8 = 600 → A. D 7.200 = 18% com 8; E 12.200 =
#   montante dessa conta errada; B 900 = um ano inteiro de juros; C 5.600 = montante certo (a pergunta é pelos juros).
#   Conferência (NOSSA): 8 meses são 2/3 do ano; 2/3 de 900 (um ano) = 600.
# QUESTÃO 9 (nós fazemos): 1 ano e 3 meses = 15 meses; 2% · 15 = 30%; 10.000 · 1,30 = 13.000 → D. E 13.120 = "1,3 ano"
#   (15,6 meses); C 12.400 = só 12 meses; B 10.250 = 2% como taxa anual em 1,25 ano; A 3.000 = só os juros.
# QUESTÃO 5 (você faz): multa 300 · 0,02 = 6,00; juros 300 · 0,01 · 15/30 = 1,50 → 307,50 → D. A 301,50 só os juros;
#   C 306,00 só a multa; B 303,00 mês inteiro de juros e esqueceu a multa; E 351,00 tratou 1% como diária (juros 45).
# Atalhos (verde): "período maior, taxa maior" (a anual é sempre a maior; se encolheu, inverteu) · "dias ÷ 30 = fração do
#   mês: calcule o mês inteiro e pegue a fração" · "converta o que deixa a conta limpa (sem dízima)".
# Frases-chave (meio e fim, idênticas): 1. Taxa e tempo falam a mesma língua. 2. Traduza só um dos dois.
#   3. A multa é o ingresso; os juros de mora são o taxímetro.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Juros simples: taxa ao ano, prazo em meses e o boleto atrasado | Juros Simples Ep. 2"
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
        "{a}*Cinco mil reais* [p=0.2] a *dezoito por cento ao ano,* [p=0.2] durante *oito meses.* [p=0.4] {b}Quem faz "
        "zero vírgula dezoito vezes oito [p=0.2] descobre que o empréstimo rendeu *sete mil e duzentos reais,* [p=0.2] "
        "mais que o próprio capital. [p=0.4] {c}A conta certa dá *seiscentos reais.* [p=0.4] {d}A diferença está numa "
        "única palavra: [p=0.3] *ao ano.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai *igualar taxa e tempo* em qualquer questão, [p=0.2] inclusive com prazo "
        "em *dias,* [p=0.3] {b}e calcular o valor de um *boleto pago com atraso.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes. [p=0.3] {a}Do episódio um: [p=0.2] *J igual a C vezes i vezes t:* [p=0.2] a conta de "
        "*um mês só,* [p=0.2] vezes o número de meses. [p=0.4] {b}Da série de Unidades: [p=0.2] *um ano tem doze meses.* "
        "[p=0.3] {c}Um ano e três meses [p=0.2] são *quinze meses,* [p=0.2] ou um vírgula vinte e cinco ano, [p=0.2] "
        "*nunca* um vírgula três. [p=0.2] Um prazo assim, [p=0.2] com duas unidades juntas, [p=0.2] se chama *prazo "
        "misto.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Pense em duas situações do dia a dia. [p=0.3] {a}A conta de luz paga *atrasada.* [p=0.2] No boleto: [p=0.2] "
        "multa de dois por cento [p=0.2] e juros de um por cento *ao mês.* [p=0.4] {b}E um empréstimo [p=0.2] com *taxa "
        "anual* [p=0.2] para um prazo de poucos *meses.* [p=0.4] {c}A taxa fala de um período, [p=0.2] o tempo fala de "
        "outro. [p=0.2] Dá para fazer a conta assim mesmo?"),

    # ================= BLOCO A: A REGRA =================
    dict(id="05", block="regra", text=
        "{t}Não dá. [p=0.3] {a}*J igual a C vezes i vezes t* [p=0.2] só funciona com a taxa e o tempo [p=0.2] na *mesma "
        "unidade.* [p=0.4] {b}Taxa *mensal* [p=0.2] conversa com *meses;* [p=0.2] taxa *anual,* [p=0.2] com *anos.* "
        "[p=0.4] {c}*Taxa e tempo falam a mesma língua.* [p=0.2] Línguas diferentes, [p=0.2] fórmula *trancada.*"),
    dict(id="06", block="regra", text=
        "{t}E como destrancar? [p=0.3] {a}*Traduza.* [p=0.3] {b}Leve a taxa até a unidade do tempo, [p=0.2] *ou* o tempo "
        "até a unidade da taxa. [p=0.4] {c}Só um dos dois. [p=0.2] *Nunca os dois.*"),

    # ================= BLOCO B: TAXAS PROPORCIONAIS =================
    dict(id="07", block="proporcionais", text=
        "{t}Como se traduz uma taxa? [p=0.4] {a}Em juros simples, [p=0.2] a taxa cresce na *mesma proporção* do tempo: "
        "[p=0.2] dobrou o tempo, [p=0.2] dobra a taxa. [p=0.2] São as *taxas proporcionais.* [p=0.4] {b}Vinte e quatro "
        "por cento *ao ano,* [p=0.2] dividido por doze meses: [p=0.2] *dois por cento ao mês.* [p=0.4] {c}E de volta: "
        "[p=0.2] dois por cento ao mês [p=0.2] são *seis* no trimestre, [p=0.2] *doze* no semestre [p=0.2] e *vinte e "
        "quatro* no ano."),
    dict(id="08", block="aviso", text=
        "{t}Atenção. [p=0.3] {a}Dividir por doze [p=0.2] *só vale em juros simples.* [p=0.4] {b}Em juros compostos, "
        "[p=0.2] dois por cento ao mês *não* é vinte e quatro ao ano. [p=0.2] Isso tem *série própria.*"),

    # ================= BLOCO C: O SENTIDO =================
    dict(id="09", block="sentido", text=
        "{t}E quando multiplicar, [p=0.2] e quando dividir? [p=0.4] {a}Em um ano, [p=0.2] o dinheiro fica alugado *doze "
        "vezes mais* tempo que em um mês. [p=0.2] *Período maior, taxa maior.* [p=0.4] {b}De *mensal* para *anual,* "
        "[p=0.2] *multiplique* por doze. [p=0.4] {c}De *anual* para *mensal,* [p=0.2] *divida.*"),
    dict(id="10", block="atalho_sent", text=
        "{t}Atalho para conferir na hora. [p=0.3] {a}A taxa *anual* [p=0.2] é sempre a *maior* das duas. [p=0.4] {b}Se "
        "dois por cento ao mês [p=0.2] virou uma taxa anual *menor* que dois, [p=0.2] você foi no sentido errado."),

    # ================= BLOCO D: O ANO COMERCIAL =================
    dict(id="11", block="comercial", text=
        "{t}E quando o prazo vem em *dias?* [p=0.4] {a}As questões usam o *ano comercial:* [p=0.2] mês de *trinta dias* "
        "[p=0.2] e ano de *trezentos e sessenta.* [p=0.4] {b}O ano do calendário, [p=0.2] de trezentos e sessenta e "
        "cinco, [p=0.2] é o *ano civil.* [p=0.2] Use *só* quando o enunciado avisar."),

    # ================= BLOCO E: OS 45 DIAS =================
    dict(id="12", block="dias45", text=
        "{t}Um exemplo. [p=0.3] {a}*Três mil reais* [p=0.2] a *vinte e quatro por cento ao ano,* [p=0.2] por *quarenta e "
        "cinco dias.* [p=0.4] {b}Primeiro caminho: [p=0.2] o tempo em *anos.* [p=0.2] Quarenta e cinco dias [p=0.2] são "
        "quarenta e cinco *trezentos e sessenta avos* de ano. [p=0.4] {c}Três mil, [p=0.2] vezes zero vírgula vinte e "
        "quatro, [p=0.2] vezes essa fração: [p=0.2] *noventa reais.*"),
    dict(id="13", block="dias45", text=
        "{t}Segundo caminho: [p=0.2] tudo em *meses.* [p=0.3] {a}*Dois por cento ao mês,* [p=0.2] e quarenta e cinco dias "
        "[p=0.2] são *um mês e meio.* [p=0.4] {b}Um mês: [p=0.2] *sessenta reais.* [p=0.2] Um mês e meio: [p=0.2] "
        "*noventa.* [p=0.4] {c}O *mesmo* resultado."),
    dict(id="14", block="facil", text=
        "{t}Então qual traduzir? [p=0.3] {a}Atalho: [p=0.2] o que deixar a conta *mais limpa.* [p=0.4] {b}Oito meses a "
        "dezoito por cento ao ano. [p=0.2] O tempo em anos [p=0.2] dá oito doze avos: [p=0.2] *zero vírgula seis seis "
        "seis,* [p=0.2] uma dízima. [p=0.4] {c}A taxa em meses: [p=0.2] *um vírgula cinco por cento,* [p=0.2] vezes oito. "
        "[p=0.2] Limpo."),

    # ================= BLOCO F: O BOLETO =================
    dict(id="15", block="boleto_def", text=
        "{t}E o boleto atrasado? [p=0.4] {a}Ele tem duas cobranças. [p=0.2] A *multa:* [p=0.2] uma porcentagem fixa, "
        "[p=0.2] cobrada *uma vez só,* [p=0.2] seja um dia ou vinte de atraso. [p=0.4] {b}E os *juros de mora.* [p=0.2] "
        "Mora quer dizer *atraso:* [p=0.2] uma taxa mensal cobrada na proporção dos *dias.* [p=0.2] O nome técnico é *pro "
        "rata die,* [p=0.2] proporcional ao dia. [p=0.4] {c}Guarde: [p=0.2] a multa é o *ingresso;* [p=0.2] os juros de "
        "mora são o *taxímetro.*"),
    dict(id="16", block="boleto", text=
        "{t}Na prática. [p=0.3] {a}Conta de *quatrocentos e cinquenta reais,* [p=0.2] multa de dois por cento, [p=0.2] "
        "juros de um por cento ao mês, [p=0.2] *dez dias* de atraso. [p=0.4] {b}O ingresso: [p=0.2] *nove reais.* [p=0.4] "
        "{c}O taxímetro: [p=0.2] quatro e cinquenta *por mês.* [p=0.2] Dez dias são *um terço* do mês: [p=0.2] *um e "
        "cinquenta.* [p=0.4] {d}Total: [p=0.2] *quatrocentos e sessenta reais e cinquenta centavos.*"),
    dict(id="17", block="atalho_dias", text=
        "{t}E para os dias, [p=0.2] tem um atalho. [p=0.3] {a}Dias divididos por trinta [p=0.2] dão a *fração do mês.* "
        "[p=0.2] Dez dias, [p=0.2] um terço. [p=0.2] Quinze dias, [p=0.2] *metade.* [p=0.4] {b}Calcule os juros do "
        "*mês inteiro* [p=0.2] e pegue só essa fração."),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}*Mil e duzentos reais* [p=0.2] a juros simples de *trinta e seis por cento ao ano,* "
        "[p=0.2] durante *quatro meses.* [p=0.2] Quanto rendem? [p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Taxa ao ano, [p=0.2] tempo em meses. [p=0.2] Traduza a taxa: [p=0.2] trinta e seis "
        "dividido por doze, [p=0.2] *três por cento ao mês.* [p=0.4] {b}Um mês: [p=0.2] três por cento de mil e "
        "duzentos, [p=0.2] *trinta e seis reais.* [p=0.4] {c}Quatro meses: [p=0.2] *cento e quarenta e quatro reais.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] taxa e tempo falam a mesma língua. [p=0.5] {b}Dois: "
        "[p=0.2] traduza só um dos dois. [p=0.5] {c}Três: [p=0.2] a multa é o ingresso; [p=0.2] os juros de mora são o "
        "taxímetro."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Agora, os erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] usar taxa *anual* com tempo em *meses.* [p=0.2] "
        "Dezoito por cento vezes oito. [p=0.4] {b}Parece certo, [p=0.2] porque os dois números estão ali no enunciado. "
        "[p=0.4] {c}Mas oito *meses* não são oito *anos.* [p=0.2] Iguale as unidades antes."),
    dict(id="22", block="erros", text=
        "{a}Segundo: [p=0.2] converter a taxa *e também* o tempo. [p=0.2] Mil reais a dois por cento ao mês, [p=0.2] por "
        "dois anos. [p=0.4] {b}Parece capricho, [p=0.2] traduzir tudo. [p=0.2] Mas vinte e quatro por cento com vinte e "
        "quatro meses [p=0.2] dá *cinco mil setecentos e sessenta,* [p=0.2] doze vezes *mais.* [p=0.2] E dois por cento "
        "com dois [p=0.2] dá *quarenta,* [p=0.2] doze vezes *menos.* [p=0.4] {c}O certo, [p=0.2] traduzindo só o tempo: "
        "[p=0.2] *quatrocentos e oitenta.*"),
    dict(id="23", block="erros", text=
        "{a}Terceiro: [p=0.2] dividir dois por cento ao mês por doze [p=0.2] para achar a taxa anual. [p=0.4] {b}Parece "
        "certo, [p=0.2] porque o doze sempre aparece na conversão. [p=0.4] {c}Mas período maior, [p=0.2] taxa maior: "
        "[p=0.2] ao ano são *vinte e quatro* por cento."),
    dict(id="24", block="erros", text=
        "{a}Quarto: [p=0.2] ler um ano e três meses [p=0.2] como *um vírgula três* ano. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque com dinheiro e metro a vírgula funciona assim. [p=0.4] {c}Mas são *quinze meses,* [p=0.2] ou um vírgula "
        "vinte e cinco ano."),
    dict(id="25", block="erros", text=
        "{a}Quinto, [p=0.2] no boleto: [p=0.2] esquecer a multa ou os juros, [p=0.2] cobrar o *mês inteiro* por poucos "
        "dias, [p=0.2] ou tratar a taxa mensal como *diária.* [p=0.4] {b}Parece certo, [p=0.2] porque o boleto só mostra "
        "as porcentagens. [p=0.4] {c}O certo: [p=0.2] o ingresso uma vez, [p=0.2] mais o taxímetro só dos dias."),

    # ================= QUESTÃO 2 (EU FAÇO) =================
    dict(id="26", block="q1", text=
        "{t}Agora, questões no estilo do ENEM. [p=0.2] Esta eu resolvo com você. [p=0.4] {a}Um capital de *cinco mil "
        "reais* foi emprestado a juros simples, [p=0.2] à taxa de *dezoito por cento ao ano.* [p=0.2] Os juros devidos "
        "após *oito meses* são de: [p=0.4] {qa}A: [p=0.2] seiscentos reais. [p=0.3] {qb}B: [p=0.2] novecentos. [p=0.3] "
        "{qc}C: [p=0.2] cinco mil e seiscentos. [p=0.3] {qd}D: [p=0.2] sete mil e duzentos. [p=0.3] {qe}E: [p=0.2] doze "
        "mil e duzentos."),
    dict(id="27", block="q1", text=
        "{t}Primeiro, [p=0.2] as unidades. [p=0.2] {a}Taxa *ao ano,* [p=0.2] tempo em *meses.* [p=0.2] Línguas "
        "diferentes. [p=0.4] {b}Traduza a taxa: [p=0.2] dezoito dividido por doze, [p=0.2] um vírgula cinco por cento ao "
        "mês. [p=0.4] {c}Um mês: [p=0.2] *setenta e cinco reais.* [p=0.2] Oito meses: [p=0.2] *seiscentos.* [p=0.4] "
        "{d}Confere? [p=0.2] Um ano renderia novecentos; [p=0.2] oito meses são dois terços disso: [p=0.2] seiscentos. "
        "[p=0.3] {ok}*Letra A!*"),
    dict(id="28", block="q1", text=
        "{t}E as outras? [p=0.3] {xd}A D, [p=0.2] sete mil e duzentos, [p=0.2] usou dezoito por cento com oito, [p=0.2] "
        "como se fossem oito *anos.* [p=0.4] {xe}A E é o *montante* dessa conta errada. [p=0.4] {xb}A B é um *ano "
        "inteiro* de juros. [p=0.4] {xc}E a C é o montante *certo,* [p=0.2] mas a pergunta é pelos *juros.* [p=0.4] {f}E "
        "a ordem de grandeza já derruba a D e a E: [p=0.2] cinco mil reais não rendem mais que eles mesmos [p=0.2] em "
        "oito meses."),

    # ================= QUESTÃO 9 (NÓS FAZEMOS) =================
    dict(id="29", block="q2", text=
        "{t}Esta a gente faz junto. [p=0.3] {a}Um empréstimo de *dez mil reais* a juros simples de *dois por cento ao "
        "mês* [p=0.2] será quitado em um único pagamento [p=0.2] após *um ano e três meses.* [p=0.2] O valor desse "
        "pagamento é: [p=0.4] {qa}A: [p=0.2] três mil reais. [p=0.3] {qb}B: [p=0.2] dez mil duzentos e cinquenta. [p=0.3] "
        "{qc}C: [p=0.2] doze mil e quatrocentos. [p=0.3] {qd}D: [p=0.2] treze mil. [p=0.3] {qe}E: [p=0.2] treze mil cento "
        "e vinte. [p=0.4] {p}Pense comigo: [p=0.2] qual é a unidade da taxa? [p=1.0]"),
    dict(id="30", block="q2", text=
        "{t}A taxa é *mensal.* [p=0.2] {a}Então o tempo vai para meses: [p=0.2] um ano e três meses, [p=0.2] doze mais "
        "três, [p=0.2] *quinze meses.* [p=0.4] {b}Dois por cento por mês, [p=0.2] em quinze meses: [p=0.2] *trinta por "
        "cento* de juros. [p=0.2] Trinta por cento de dez mil: [p=0.2] três mil. [p=0.4] {c}E a pergunta é o "
        "*pagamento:* [p=0.2] capital mais juros, [p=0.2] *treze mil reais.* [p=0.3] {ok}*Letra D!*"),
    dict(id="31", block="q2", text=
        "{t}E as armadilhas? [p=0.3] {xe}A E leu *um vírgula três* ano. [p=0.4] {xc}A C contou só o *ano completo.* "
        "[p=0.4] {xb}A B tratou dois por cento como taxa *anual.* [p=0.4] {xa}E a A [p=0.2] são *só os juros,* [p=0.2] "
        "mas a questão pede o pagamento."),

    # ================= QUESTÃO 5 (VOCÊ FAZ) =================
    dict(id="32", block="q3", text=
        "{t}E esta é *sua.* [p=0.3] {a}Uma conta de *trezentos reais* foi paga com *quinze dias* de atraso. [p=0.2] Multa "
        "de *dois por cento* [p=0.2] e juros de mora de *um por cento ao mês,* [p=0.2] proporcionais aos dias, [p=0.2] "
        "mês de trinta dias. [p=0.2] O valor pago foi de: [p=0.4] {qa}A: [p=0.2] trezentos e um e cinquenta. [p=0.3] "
        "{qb}B: [p=0.2] trezentos e três. [p=0.3] {qc}C: [p=0.2] trezentos e seis. [p=0.3] {qd}D: [p=0.2] trezentos e "
        "sete e cinquenta. [p=0.3] {qe}E: [p=0.2] trezentos e cinquenta e um. [p=0.5] {p}*Pause o vídeo e resolva.* "
        "[p=2.0]"),
    dict(id="33", block="q3", text=
        "{t}Conferindo. [p=0.3] {a}O ingresso: [p=0.2] dois por cento de trezentos, [p=0.2] *seis reais.* [p=0.4] {b}O "
        "taxímetro: [p=0.2] um por cento de trezentos [p=0.2] são três reais por mês. [p=0.2] Quinze dias, [p=0.2] meio "
        "mês: [p=0.2] *um e cinquenta.* [p=0.4] {c}Total: [p=0.2] trezentos, [p=0.2] mais seis, [p=0.2] mais um e "
        "cinquenta: [p=0.2] *trezentos e sete reais e cinquenta centavos.* [p=0.3] {ok}*Letra D!*"),
    dict(id="34", block="q3", text=
        "{t}E as erradas? [p=0.3] {xa}A A cobrou *só os juros.* [p=0.3] {xc}A C, [p=0.2] *só a multa.* [p=0.4] {xb}A B "
        "cobrou o *mês inteiro* de juros [p=0.2] e esqueceu a multa. [p=0.4] {xe}E a E tratou um por cento como taxa "
        "*diária:* [p=0.2] quarenta e cinco de juros, [p=0.2] trinta vezes mais."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="35", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] taxa e tempo falam a mesma língua. [p=0.5] "
        "{b}Dois: [p=0.2] traduza só um dos dois. [p=0.5] {c}Três: [p=0.2] a multa é o ingresso; [p=0.2] os juros de "
        "mora são o taxímetro."),

    # ================= PONTE E CTA =================
    dict(id="36", block="ponte", text=
        "{a}*Mil reais* a *cinco por cento ao mês:* [p=0.3] {b}mil e cinquenta, [p=0.2] mil e cem, [p=0.2] mil cento e "
        "cinquenta... [p=0.4] {c}Se você desenhar esses pontos num gráfico, [p=0.2] que *forma* aparece? [p=0.4] "
        "{d}Próximo episódio."),
    dict(id="37", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha pago um boleto atrasado sem saber a conta? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
