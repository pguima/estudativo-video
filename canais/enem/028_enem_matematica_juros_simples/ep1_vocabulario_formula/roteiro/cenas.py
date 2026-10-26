# Roteiro — Juros Simples, Episódio 1 de 5: o vocabulário do dinheiro e a fórmula J = C · i · t
# Base: Estudos/Enem/estudos/01-matematica/13-juros-simples.html — seções 02 e 03 + Questão 1 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   Juros são o ALUGUEL DO DINHEIRO: quem usa o dinheiro de outra pessoa paga por cada mês de uso.
#   Em juros simples, o aluguel é SEMPRE O MESMO: todo mês sobre o capital inicial, nunca sobre os juros acumulados
#     (a pilha de notas parada e uma moedinha igual caindo a cada mês).
#   A CONTA DE UM MÊS SÓ: calcule os juros de UM período e multiplique pelo número de períodos.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Todos os exemplos têm taxa e tempo na MESMA unidade (conversão = episódio 2).
# Exemplos: o do material (R$ 1.500,00 a 2% a.m. por 6 meses → J 180, M 1.680, fator 1,12), pedido pelo prompt.
#   Nós fazemos (prompt): R$ 800,00 a 3% a.m. por 5 meses → 24 por mês; J = 120; M = 920; fator 1,15.
#   Erro 2 (nosso): 1.500 · 2 · 6 = 18 000 (em vez de 180).
#   Erro 3 (NOSSO, para não entregar as alternativas A e E da Q1): R$ 1.000,00 a 1,5% a.m. por 4 meses →
#   certo 60; com 0,15 → 600; com 0,0015 → 6.
# QUESTÃO 1 (texto idêntico na tela): 2.400 · 0,015 = 36 por mês; × 8 = 288 → C. Erradas (do material): B = juro de um
#   único mês; D = montante (2.400 + 288); E = usou 15% (0,15); A = usou 0,15% (0,0015).
#   Conferência de plausibilidade (NOSSA): 1,5% × 8 = 12% do capital; 12% de 2.400 ≈ 288.
#   Você faz (prompt): o montante → 2.400 + 288 = 2.688 (fator 1 + 0,015 · 8 = 1,12; 2.400 · 1,12 = 2.688).
# Atalhos (verde): "% vira decimal: vírgula duas casas para a esquerda" · "a conta de um mês só" · "M pelo fator 1 + i·t".
# Frases-chave (meio e fim, idênticas): 1. Juros são o aluguel do dinheiro, sempre sobre o capital inicial.
#   2. Juros é o acréscimo; montante é o total. 3. Calcule um período e multiplique pelo tempo.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Juros simples do zero: juros, montante e a fórmula J = C · i · t | Juros Simples Ep. 1"
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
        "{a}*Dois mil e quatrocentos reais* aplicados a *um vírgula cinco por cento ao mês* [p=0.2] por *oito meses.* "
        "[p=0.4] {b}A prova coloca cinco respostas: [p=0.3] {r1}vinte e oito reais e oitenta, [p=0.2] {r2}trinta e seis "
        "reais, [p=0.2] {r3}duzentos e oitenta e oito reais, [p=0.2] {r4}dois mil, seiscentos e oitenta e oito reais "
        "[p=0.2] {r5}e dois mil, oitocentos e oitenta reais. [p=0.5] {c}*Quatro delas* são a conta certa [p=0.2] feita do "
        "*jeito errado.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai saber distinguir *juros* de *montante* [p=0.3] {b}e calcular os dois "
        "[p=0.2] sem errar a *vírgula da taxa.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos da série de Porcentagem. [p=0.3] {a}Por cento quer dizer *dividido por cem.* "
        "[p=0.2] Dois por cento é *zero vírgula zero dois;* [p=0.2] um vírgula cinco por cento é *zero vírgula zero um "
        "cinco.* [p=0.4] {b}E o *fator:* [p=0.2] aumentar doze por cento [p=0.2] é multiplicar por *um vírgula doze.* "
        ""),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Imagine duas situações. [p=0.3] {a}Seu tio diz: [p=0.2] *te empresto mil e quinhentos reais,* [p=0.2] e você "
        "me devolve com *dois por cento a mais por mês.* [p=0.4] {b}E uma loja aluga uma *bicicleta:* [p=0.2] *vinte "
        "reais por dia.* [p=0.2] Ficou três dias? [p=0.2] Paga sessenta. [p=0.4] {c}As duas são a mesma ideia. [p=0.3] "
        "*Juros são o aluguel do dinheiro:* [p=0.2] quem usa o dinheiro de outra pessoa [p=0.2] paga por cada mês de uso."),

    # ================= BLOCO A: AS CINCO PALAVRAS =================
    dict(id="05", block="palavras", text=
        "{t}E quais são as palavras que aparecem em *toda* questão? [p=0.3] São cinco. [p=0.4] {a}*Capital,* [p=0.2] a "
        "letra *C:* [p=0.2] o valor do começo, [p=0.2] o que foi emprestado ou aplicado. [p=0.2] Os mil e quinhentos do "
        "tio. [p=0.4] {b}*Taxa de juros,* [p=0.2] a letra *i:* [p=0.2] a porcentagem cobrada a cada período. [p=0.2] "
        "Dois por cento ao mês. [p=0.4] {c}*Tempo,* [p=0.2] a letra *t:* [p=0.2] quantos períodos o dinheiro fica "
        "emprestado. [p=0.2] Seis meses."),
    dict(id="06", block="palavras", text=
        "{a}*Juros,* [p=0.2] a letra *J:* [p=0.2] o *acréscimo,* [p=0.2] o aluguel pago pelo tempo. [p=0.2] Nesse "
        "empréstimo, [p=0.2] cento e oitenta reais. [p=0.4] {b}E *montante,* [p=0.2] a letra *M:* [p=0.2] o *total* no "
        "fim, [p=0.2] capital *mais* juros. [p=0.2] Mil, seiscentos e oitenta reais."),

    # ================= BLOCO B: JUROS NÃO É MONTANTE =================
    dict(id="07", block="jm", text=
        "{t}E como saber se a questão quer os juros ou o montante? [p=0.4] {a}Pela pergunta. [p=0.3] *Quanto rendeu,* "
        "[p=0.2] *qual o valor dos juros:* [p=0.2] a resposta é *J,* [p=0.2] só o acréscimo. [p=0.4] {b}*Quanto terá,* "
        "[p=0.2] *quanto pagará no total:* [p=0.2] a resposta é *M,* [p=0.2] o total. [p=0.4] {c}E atenção: [p=0.2] o "
        "ENEM coloca *as duas* respostas entre as alternativas. [p=0.2] Sempre."),

    # ================= BLOCO C: AS SIGLAS =================
    dict(id="08", block="siglas", text=
        "{t}E aquelas letrinhas depois da taxa? [p=0.4] {a}Elas dizem o *período:* [p=0.2] o pedaço de tempo em que a "
        "taxa é cobrada uma vez. [p=0.4] {b}*a.d.,* ao dia. [p=0.2] *a.m.,* ao mês. [p=0.2] *a.b.,* ao bimestre. "
        "[p=0.4] {c}*a.t.,* ao trimestre. [p=0.2] *a.s.,* ao semestre. [p=0.2] *a.a.,* ao ano. [p=0.4] {d}Por isso a "
        "taxa nunca anda sozinha: [p=0.2] é sempre *dois por cento ao mês,* [p=0.2] com a unidade junto."),

    # ================= BLOCO D: A DEFINIÇÃO =================
    dict(id="09", block="simples", text=
        "{t}E o que tem de *simples* nos juros simples? [p=0.4] {a}Olhe a pilha de notas: [p=0.2] é o capital, [p=0.2] "
        "mil e quinhentos. [p=0.4] {b}No primeiro mês, [p=0.2] cai uma moedinha de juros: [p=0.2] *trinta reais.* "
        "[p=0.4] {c}No segundo mês, [p=0.2] outra de trinta. [p=0.2] No terceiro, [p=0.2] outra de trinta. [p=0.4] "
        "{d}As moedinhas *nunca crescem.* [p=0.3] Em *juros simples,* [p=0.2] os juros de cada mês são calculados sempre "
        "sobre o *capital inicial.* [p=0.2] O aluguel é sempre o mesmo. [p=0.4] {e}Os juros de um mês *não rendem "
        "juros* no seguinte. [p=0.2] Quando rendem, [p=0.2] são os *juros compostos:* [p=0.2] série própria."),

    # ================= BLOCO E: A FÓRMULA =================
    dict(id="10", block="formula", text=
        "{t}E como vira fórmula? [p=0.4] {a}Cada mês gera o mesmo juro: [p=0.2] o capital *vezes* a taxa, [p=0.2] *C "
        "vezes i.* [p=0.4] {b}São *t* meses: [p=0.2] *t* vezes esse juro. [p=0.4] {c}*J igual a C vezes i vezes t.* "
        "[p=0.2] Capital, [p=0.2] taxa, [p=0.2] tempo."),
    dict(id="11", block="formula", text=
        "{t}E o montante? [p=0.4] {a}É o capital mais os juros: [p=0.2] *M igual a C mais J.* [p=0.4] {b}E dá para "
        "escrever de uma vez: [p=0.2] *M igual a C vezes, abre parênteses, um mais i vezes t.* [p=0.4] {c}O um é o "
        "capital; [p=0.2] o *i vezes t,* [p=0.2] o acréscimo. [p=0.2] É o *fator* da Porcentagem."),

    # ================= BLOCO F: A TAXA DECIMAL =================
    dict(id="12", block="decimal", text=
        "{t}E a taxa entra na fórmula como? [p=0.4] {a}Na *forma decimal:* [p=0.2] a porcentagem dividida por cem. "
        "[p=0.4] {b}Dois por cento [p=0.2] vira *zero vírgula zero dois.* [p=0.2] Um vírgula cinco por cento [p=0.2] "
        "vira *zero vírgula zero um cinco.* [p=0.2] Dezoito por cento [p=0.2] vira *zero vírgula dezoito.* [p=0.4] "
        "{c}Atalho: [p=0.2] tire o símbolo de por cento [p=0.2] e ande com a vírgula *duas casas para a esquerda.* "
        "[p=0.2] Faltou algarismo? [p=0.2] Complete com zero."),

    # ================= BLOCO G: O EXEMPLO COMPLETO =================
    dict(id="13", block="exemplo", text=
        "{t}Agora, o empréstimo do tio, completo. [p=0.4] {a}Capital, [p=0.2] mil e quinhentos. [p=0.2] Taxa, [p=0.2] "
        "dois por cento ao mês, [p=0.2] *zero vírgula zero dois.* [p=0.2] Tempo, [p=0.2] seis meses. [p=0.4] {b}J igual "
        "a mil e quinhentos, [p=0.2] vezes zero vírgula zero dois, [p=0.2] vezes seis: [p=0.2] *cento e oitenta reais.* "
        "[p=0.4] {c}E o montante: [p=0.2] mil e quinhentos mais cento e oitenta, [p=0.2] *mil, seiscentos e oitenta "
        "reais.*"),
    dict(id="14", block="exemplo", text=
        "{t}E pelo fator? [p=0.4] {a}Um mais zero vírgula zero dois vezes seis: [p=0.2] *um vírgula doze.* [p=0.4] "
        "{b}Mil e quinhentos vezes um vírgula doze: [p=0.2] *mil, seiscentos e oitenta.* [p=0.2] O mesmo valor. [p=0.4] "
        "{c}Repare: [p=0.2] seis meses a dois por cento [p=0.2] viraram *um aumento único de doze por cento,* [p=0.2] "
        "igualzinho à Porcentagem."),

    # ================= BLOCO H: A CONTA DE CABEÇA =================
    dict(id="15", block="cabeca", text=
        "{t}Dá para fazer isso sem calculadora? [p=0.4] {a}Dá, [p=0.2] com a *conta de um mês só.* [p=0.4] {b}Primeiro, "
        "os juros de *um* mês: [p=0.2] um por cento de mil e quinhentos é quinze; [p=0.2] dois por cento é *trinta.* "
        "[p=0.4] {c}Depois, [p=0.2] multiplique pelos meses: [p=0.2] trinta vezes seis, [p=0.2] *cento e oitenta.* "
        ""),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}*Oitocentos reais* aplicados a juros simples [p=0.2] de *três por cento ao mês* [p=0.2] "
        "durante *cinco meses.* [p=0.4] {b}Quanto rendem [p=0.2] e quanto vira o total? [p=0.3] *Pause e tente.* "
        "[p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos, [p=0.2] pela conta de um mês só. [p=0.4] {a}Um por cento de oitocentos é oito; [p=0.2] três "
        "por cento é *vinte e quatro reais* por mês. [p=0.4] {b}Cinco meses: [p=0.2] vinte e quatro vezes cinco, "
        "[p=0.2] *J igual a cento e vinte reais.* [p=0.4] {c}O total: [p=0.2] oitocentos mais cento e vinte, [p=0.2] *M "
        "igual a novecentos e vinte reais.* [p=0.4] {d}Pelo fator, [p=0.2] um vírgula quinze: "
        "[p=0.2] oitocentos vezes um vírgula quinze, [p=0.2] novecentos e vinte. [p=0.2] Bateu."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] juros são o aluguel do dinheiro, [p=0.2] sempre sobre "
        "o capital inicial. [p=0.5] {b}Dois: [p=0.2] juros é o acréscimo; [p=0.2] montante é o total. [p=0.5] {c}Três: "
        "[p=0.2] calcule um período e multiplique pelo tempo."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] responder o *montante* quando pedem os *juros,* "
        "[p=0.2] ou o contrário. [p=0.4] {b}Parece certo, [p=0.2] porque a conta está perfeita [p=0.2] e o número está "
        "nas alternativas. [p=0.4] {c}Leia a pergunta de novo: [p=0.2] *rendeu* é J; [p=0.2] *total* é M."),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] usar *dois* em vez de *zero vírgula zero dois.* [p=0.2] Mil e quinhentos vezes dois vezes "
        "seis: [p=0.2] *dezoito mil reais* de juros! [p=0.4] {b}Parece certo, [p=0.2] porque a taxa é mesmo dois por "
        "cento. [p=0.4] {c}Mas o por cento é um *dividido por cem* escondido."),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] errar a vírgula de *um vírgula cinco por cento.* [p=0.2] Mil reais por quatro meses. "
        "[p=0.4] {b}Com zero vírgula *quinze,* [p=0.2] que é quinze por cento, [p=0.2] dá seiscentos. [p=0.2] Com zero "
        "vírgula zero zero *quinze,* [p=0.2] que é zero vírgula quinze por cento, [p=0.2] dá seis. [p=0.4] {c}Parece "
        "certo, [p=0.2] porque os algarismos um e cinco estão lá. [p=0.2] O certo é *zero vírgula zero um cinco:* "
        "[p=0.2] *sessenta reais.*"),

    # ================= QUESTÃO 1 (EU FAÇO) =================
    dict(id="22", block="q1", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.2] É a do começo da aula, "
        "[p=0.2] e eu resolvo com você. [p=0.4] {a}Uma pessoa aplicou *dois mil e quatrocentos reais* [p=0.2] em um "
        "investimento que paga juros simples de *um vírgula cinco por cento ao mês.* [p=0.2] Ao final de *oito meses,* "
        "[p=0.2] o valor dos *juros* recebidos será de: [p=0.4] {qa}A: [p=0.2] vinte e oito reais e oitenta. [p=0.3] "
        "{qb}B: [p=0.2] trinta e seis. [p=0.3] {qc}C: [p=0.2] duzentos e oitenta e oito. [p=0.3] {qd}D: [p=0.2] dois mil, "
        "seiscentos e oitenta e oito. [p=0.3] {qe}E: [p=0.2] dois mil, oitocentos e oitenta reais."),
    dict(id="23", block="q1", text=
        "{t}Primeiro, [p=0.2] uma etiqueta em cada número. [p=0.3] {a}Dois mil e quatrocentos é o *C.* [p=0.2] Um "
        "vírgula cinco por cento ao mês é o *i:* [p=0.2] zero vírgula zero um cinco. [p=0.2] Oito meses é o *t.* "
        "[p=0.2] Taxa e tempo em meses: [p=0.2] tudo certo. [p=0.4] {b}E a pergunta é *os juros:* [p=0.2] quero o *J.* "
        "[p=0.4] {c}Um mês: [p=0.2] um por cento de dois mil e quatrocentos é vinte e quatro; [p=0.2] meio por cento é "
        "doze; [p=0.2] somando, [p=0.2] *trinta e seis.* [p=0.4] {d}Oito meses: [p=0.2] trinta e seis vezes oito, "
        "[p=0.2] *duzentos e oitenta e oito reais.* [p=0.4] {e}Plausível? [p=0.2] Oito meses a um e meio por cento "
        "[p=0.2] dão doze por cento do capital, [p=0.2] e doze por cento de dois mil e quatrocentos é isso mesmo. "
        "[p=0.3] {ok}*Letra C!*"),
    dict(id="24", block="q1", text=
        "{t}E as outras? [p=0.2] Cada uma é a conta certa [p=0.2] feita do jeito errado. [p=0.4] {xb}A B, [p=0.2] trinta "
        "e seis, [p=0.2] é o juro de *um mês só:* [p=0.2] esqueceu de multiplicar pelo tempo. [p=0.4] {xd}A D, [p=0.2] "
        "dois mil, seiscentos e oitenta e oito, [p=0.2] é o *montante:* [p=0.2] mas a pergunta era os juros. [p=0.4] "
        "{xe}A E usou *quinze* por cento, [p=0.2] zero vírgula quinze. [p=0.4] {xa}E a A usou *zero vírgula quinze* por "
        "cento. [p=0.4] {f}Os dois erros de vírgula possíveis [p=0.2] na mesma taxa."),

    # ================= VOCÊ FAZ =================
    dict(id="25", block="voce", text=
        "{t}E agora é *sua.* [p=0.3] {a}Na mesma aplicação, [p=0.2] qual é o *montante?* [p=0.4] {b}*Pause o vídeo e "
        "resolva.* [p=2.0]"),
    dict(id="26", block="voce", text=
        "{t}Conferindo. [p=0.3] {a}Montante é o total: [p=0.2] capital mais juros. [p=0.2] Dois mil e quatrocentos mais "
        "duzentos e oitenta e oito: [p=0.2] *dois mil, seiscentos e oitenta e oito reais.* [p=0.4] {b}Pelo fator, "
        "[p=0.2] um vírgula doze: [p=0.2] dois mil e quatrocentos vezes um vírgula doze, [p=0.2] o mesmo valor. [p=0.4] {c}E repare: [p=0.2] é justamente a alternativa D. "
        "[p=0.2] Ela estava lá esperando quem errasse a pergunta."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="27", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] juros são o aluguel do dinheiro, [p=0.2] sempre "
        "sobre o capital inicial. [p=0.5] {b}Dois: [p=0.2] juros é o acréscimo; [p=0.2] montante é o total. [p=0.5] "
        "{c}Três: [p=0.2] calcule um período e multiplique pelo tempo."),

    # ================= PONTE E CTA =================
    dict(id="28", block="ponte", text=
        "{a}E se a taxa for *dezoito por cento ao ano* [p=0.2] e o prazo, *oito meses?* [p=0.5] {b}Quem faz zero vírgula "
        "dezoito vezes oito [p=0.2] descobre que cinco mil reais renderam *sete mil e duzentos:* [p=0.3] {c}mais que o "
        "próprio capital. [p=0.5] {d}Próximo episódio."),
    dict(id="29", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já confundiu juros com montante? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
