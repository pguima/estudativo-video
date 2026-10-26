# Roteiro — Equações e Inequações do 1º Grau, Episódio 4 de 5: comparar planos, o ponto de equilíbrio e a partir de quando compensa.
# Base: Estudos/Enem/estudos/01-matematica/20-equacoes-inequacoes-1o-grau.html — seção 08 + Questões 1 e 2 da seção 12.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   A CORRIDA de dois planos: quem tem a taxa fixa menor LARGA NA FRENTE; quem tem o preço por unidade menor CORRE MAIS
#   RÁPIDO e ultrapassa no ponto de equilíbrio.
#   O ATALHO DA DIFERENÇA: diferença das taxas fixas ÷ diferença dos preços por unidade.
#   NO EMPATE NINGUÉM É MAIS BARATO: "mais barato" começa no número seguinte.
# Frases do usuário mantidas IGUAIS: gancho, promessa ("Ao final, ..."), as 3 frases-chave e a ponte.
# Exemplos (todos conferidos em Python):
#   Locadoras (prompt e material): A = 90 + 0,5x · B = 60 + 0,8x. 50 km: A 115, B 100 · 200 km: A 190, B 220 ·
#   100 km: 140 e 140 · 101 km: A 140,50, B 140,80. Equação 30 = 0,3x → 100 · inequação 0,3x < 30 → x < 100.
#   Atalho: (90 − 60) ÷ (0,80 − 0,50) = 30 ÷ 0,3 = 100.
#   Nós fazemos (prompt): 12 + 3h × 4 + 5h → 8 ÷ 2 = 4 h (R$ 24 nos dois); 6 h: A 30, B 34 → A compensa.
# Desvio do prompt (regra de exemplos): o erro 1 pede "responder 800 quando se pede 801", que é a resposta da Questão 2
#   ("você faz"). O erro 1 usa as locadoras (A mais barata a partir de 101 km, não 100). Os erros 2 e 3 também usam as
#   locadoras: 30 ÷ 0,8 = 37,5 km (A 108,75 × B 90, não empata; dito sem os valores) e o sinal trocado 90 + 60 = 0,3x → 500 km (A 340 × B 460).
# QUESTÃO 1 (eu faço, texto idêntico): 50 + 0,4x = 20 + 0,6x → 30 = 0,2x → 150 (D); conferência 110 e 110.
#   Erradas (do material e do prompt): A 30 ÷ 1 (soma das tarifas) · B 30 ÷ 0,6 (tarifa do Beta só) · C 70 ÷ 1 (somou
#   mensalidades e tarifas) · E 70 ÷ 0,2 = 350 (sinal trocado ao passar o 20).
# QUESTÃO 2 (você faz, texto idêntico): 120 + 0,35n < 0,5n → 120 < 0,15n → n > 800 → 801 (E). Conferência 800: 400 e 400;
#   801: P 400,35, Q 400,50. Erradas (do material): D = empate · A 120 ÷ 0,50 = 240 · B 120 ÷ 0,35 ≈ 343 · C 120 ÷ 0,25 = 480.
# Acréscimos nossos (verde): o atalho da diferença (seção 08), "confira os DOIS planos no número achado", e "sem taxa fixa, a
#   diferença das taxas é a própria taxa" (Q2). O gráfico aparece só como ilustração, citando a série de Função afim.
# Frases-chave (meio e fim, idênticas): 1. Taxa fixa menor ganha no começo; preço por unidade menor ganha no fim.
#   2. Equilíbrio = diferença das taxas ÷ diferença dos preços. 3. No empate ninguém é mais barato.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Qual plano compensa? O ponto de equilíbrio em uma linha | Equações do 1º Grau Ep. 4"
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
        "{a}A gráfica P cobra *cento e vinte reais* de taxa [p=0.2] e *trinta e cinco centavos* por cartaz. [p=0.4] {b}A Q "
        "*não cobra taxa* [p=0.2] e cobra *cinquenta centavos.* [p=0.4] {c}Com *oitocentos* cartazes, [p=0.2] as duas custam "
        "*quatrocentos reais.* [p=0.4] {d}Então a partir de quantos cartazes [p=0.2] P é mais barata? [p=0.4] {e}*Não é "
        "oitocentos.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai achar o *ponto de equilíbrio* em uma linha [p=0.3] {b}e dizer qual plano *compensa* "
        "[p=0.2] antes e depois dele."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] equação se resolve fazendo *a mesma coisa nos "
        "dois lados.* [p=0.4] {b}Do episódio três: [p=0.2] numa inequação, [p=0.2] se a "
        "resposta precisa ser *inteira,* [p=0.2] x maior que oitenta e dois vírgula cinco [p=0.2] vira *oitenta e três.*"),

    # ================= CONCRETO: AS LOCADORAS =================
    dict(id="04", block="locadoras", text=
        "{t}Você vai alugar um carro por um dia. [p=0.3] {a}A locadora A cobra *noventa reais* pela diária [p=0.2] mais "
        "*cinquenta centavos* por quilômetro. [p=0.4] {b}A locadora B cobra *sessenta reais* [p=0.2] mais *oitenta "
        "centavos* por quilômetro. [p=0.4] {c}A diária é a *taxa fixa:* [p=0.2] você paga mesmo sem sair do lugar. [p=0.3] "
        "{d}E o valor por quilômetro é o *preço por unidade:* [p=0.2] cobrado a cada quilômetro."),
    dict(id="05", block="locadoras", text=
        "{t}Qual é mais barata? [p=0.4] {a}Para *cinquenta quilômetros:* [p=0.2] A dá noventa mais vinte e cinco, [p=0.2] "
        "*cento e quinze.* [p=0.2] B dá sessenta mais quarenta, [p=0.2] *cem.* [p=0.2] B ganha. [p=0.4] {b}Para *duzentos "
        "quilômetros:* [p=0.2] A dá noventa mais cem, [p=0.2] *cento e noventa.* [p=0.2] B dá sessenta mais cento e "
        "sessenta, [p=0.2] *duzentos e vinte.* [p=0.2] Agora A ganha. [p=0.4] {c}Virou no meio do caminho. [p=0.2] "
        "*Onde?*"),

    # ================= A CORRIDA =================
    dict(id="06", block="corrida", text=
        "{t}Pense numa *corrida.* [p=0.3] {a}B tem a taxa fixa menor: [p=0.2] ela *larga na frente.* [p=0.4] {b}A tem o "
        "preço por quilômetro menor: [p=0.2] ela *corre mais rápido.* [p=0.4] {c}Em algum ponto, [p=0.2] A "
        "*ultrapassa.* [p=0.4] {d}Esse ponto, [p=0.2] onde os dois custam *exatamente o mesmo,* [p=0.2] é o *ponto de "
        "equilíbrio.* [p=0.3] {e}E um plano *compensa* [p=0.2] quando custa *menos* que o outro."),

    # ================= BLOCO A: EQUAÇÃO =================
    dict(id="07", block="equacao", text=
        "{t}Como achar o empate? [p=0.4] {a}Custos iguais: [p=0.2] *noventa mais zero vírgula cinco x [p=0.2] igual a "
        "sessenta mais zero vírgula oito x.* [p=0.4] {b}Tire sessenta dos dois lados [p=0.2] e tire zero vírgula cinco x: "
        "[p=0.2] *trinta igual a zero vírgula três x.* [p=0.4] {c}Divida por zero vírgula três: [p=0.2] *x igual a cem "
        "quilômetros.* [p=0.4] {d}Agora confira *os dois planos:* [p=0.2] A, noventa mais cinquenta, *cento e quarenta.* "
        "[p=0.2] B, sessenta mais oitenta, *cento e quarenta.* [p=0.2] Empate."),

    # ================= BLOCO B: INEQUAÇÃO =================
    dict(id="08", block="inequacao", text=
        "{t}E quando B é mais barata? [p=0.4] {a}Troque o igual pelo *menor que.* "
        "[p=0.4] {b}As mesmas contas: [p=0.2] zero vírgula três x "
        "menor que trinta, [p=0.2] *x menor que cem.* [p=0.4] {c}E no quilômetro cem? [p=0.2] Os dois custam cento e "
        "quarenta. [p=0.2] *No empate ninguém é mais barato.* [p=0.4] {d}Então A só fica mais barata [p=0.2] *depois* de "
        "cem: [p=0.2] contando quilômetros inteiros, [p=0.2] a partir de *cento e um.*"),

    # ================= BLOCO C: A LEITURA =================
    dict(id="09", block="leitura", text=
        "{t}O que isso quer dizer? [p=0.4] {a}*Antes* de cem quilômetros, [p=0.2] pesa mais a *taxa fixa,* [p=0.2] e B "
        "ganha. [p=0.4] {b}*Depois* de cem, [p=0.2] pesa mais o *preço por quilômetro,* [p=0.2] e A ganha. [p=0.4] {c}No "
        "gráfico, [p=0.2] são duas retas que *se cruzam* no cem. [p=0.2] Esse gráfico [p=0.2] fica para a série de "
        "*Função afim.*"),

    # ================= BLOCO D: O ATALHO =================
    dict(id="10", block="atalho", text=
        "{t}Dá para achar o cem *em uma linha?* [p=0.4] {a}Dá. [p=0.2] B larga *trinta reais* na frente: [p=0.2] noventa "
        "menos sessenta. [p=0.4] {b}E A tira *trinta centavos* dessa vantagem a cada quilômetro: [p=0.2] oitenta menos "
        "cinquenta. [p=0.4] {c}Quantos quilômetros para tirar trinta reais, [p=0.2] de trinta em trinta centavos? [p=0.2] "
        "*Trinta dividido por zero vírgula três:* [p=0.2] *cem.* [p=0.4] {d}O atalho: [p=0.2] *diferença das taxas fixas,* "
        "[p=0.2] dividida pela *diferença dos preços por unidade.*"),

    # ================= BLOCO E: MESMA TARIFA =================
    dict(id="11", block="mesmatarifa", text=
        "{t}E se os dois cobrarem *o mesmo* por unidade? [p=0.4] {a}Aí ninguém corre mais rápido: [p=0.2] quem largou na "
        "frente [p=0.2] *fica na frente.* [p=0.4] {b}Na conta, [p=0.2] o x some, [p=0.2] como na Questão seis do "
        "episódio um. [p=0.4] {c}No atalho, [p=0.2] a diferença dos preços dá "
        "*zero,* [p=0.2] e não se divide por zero. [p=0.2] *Nunca empatam.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="12", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}O estacionamento A cobra *doze reais* de entrada [p=0.2] mais *três reais* por hora. "
        "[p=0.3] {b}O B cobra *quatro reais* de entrada [p=0.2] mais *cinco reais* por hora. [p=0.4] {c}Em quantas horas "
        "eles empatam, [p=0.2] e qual compensa para *seis horas?* [p=0.4] {d}*Pause e tente.* [p=2.0]"),
    dict(id="13", block="exercicio", text=
        "{t}Pelo atalho. [p=0.3] {a}Diferença das entradas: [p=0.2] doze menos quatro, [p=0.2] "
        "*oito.* [p=0.2] Diferença dos preços por hora: [p=0.2] cinco menos três, [p=0.2] *dois.* [p=0.2] Oito dividido por "
        "dois: [p=0.2] *quatro horas.* [p=0.4] {b}Confira os dois: [p=0.2] A, doze mais doze, *vinte e quatro.* [p=0.2] B, "
        "quatro mais vinte, *vinte e quatro.* [p=0.4] {c}Para seis horas: [p=0.2] A dá *trinta,* [p=0.2] B dá *trinta e "
        "quatro.* [p=0.2] *A compensa.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="14", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] taxa fixa menor ganha no começo; [p=0.2] preço por unidade "
        "menor ganha no fim. [p=0.5] {b}Dois: [p=0.2] equilíbrio é a diferença das taxas, [p=0.2] dividida pela diferença "
        "dos preços. [p=0.5] {c}Três: [p=0.2] no empate ninguém é mais barato."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="15", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] perguntam a partir de quantos quilômetros A é "
        "*mais barata,* [p=0.2] e a pessoa responde *cem.* [p=0.4] {b}Parece certo, [p=0.2] porque o cem é o número que a "
        "conta deu. [p=0.4] {c}Mas no cem os dois custam cento e quarenta. [p=0.2] Mais barata, [p=0.2] *só a partir de "
        "cento e um.*"),
    dict(id="16", block="erros", text=
        "{a}Segundo: [p=0.2] dividir os trinta reais [p=0.2] pelo preço de *um plano só,* [p=0.2] ou pela *soma* dos preços. "
        "[p=0.4] {b}Parece certo, [p=0.2] porque os números estão no enunciado. [p=0.4] {c}Mas o que fecha a distância [p=0.2] é a *diferença* de velocidade. [p=0.2] Trinta por zero "
        "vírgula oito dá trinta e sete e meio, [p=0.2] e lá A e B *não empatam.*"),
    dict(id="17", block="erros", text=
        "{a}Terceiro: [p=0.2] passar o sessenta para o outro lado *somando:* [p=0.2] noventa *mais* sessenta [p=0.2] igual "
        "a zero vírgula três x. [p=0.4] {b}Parece certo, [p=0.2] porque parece só mudar de lugar. "
        "[p=0.4] {c}Mas quem soma [p=0.2] *passa subtraindo:* [p=0.2] noventa *menos* sessenta. [p=0.2] Com o erro, [p=0.2] "
        "sai *quinhentos,* [p=0.2] e a conferência denuncia: [p=0.2] trezentos e quarenta contra quatrocentos e sessenta."),

    # ================= QUESTÃO 1 (EU FAÇO) =================
    dict(id="18", block="q1", text=
        "{t}Questão do ENEM, [p=0.2] do nosso material. [p=0.2] Eu resolvo. [p=0.4] {a}Uma operadora "
        "oferece dois planos de telefonia. [p=0.2] No plano Alfa, [p=0.2] paga-se uma mensalidade de *cinquenta reais* "
        "[p=0.2] mais *quarenta centavos* por minuto de ligação. [p=0.3] No plano Beta, [p=0.2] a mensalidade é de *vinte "
        "reais* [p=0.2] e o minuto custa *sessenta centavos.* [p=0.3] O número de minutos mensais [p=0.2] para o qual os "
        "dois planos custam o mesmo valor é: [p=0.4] {qa}A: trinta. [p=0.2] {qb}B: cinquenta. [p=0.2] {qc}C: setenta. "
        "[p=0.2] {qd}D: cento e cinquenta. [p=0.2] {qe}E: trezentos e cinquenta. [p=0.4] {p}*Pause o vídeo e tente.* "
        "[p=2.0]"),
    dict(id="19", block="q1", text=
        "{t}*O mesmo valor:* [p=0.2] é o empate, [p=0.2] uma equação. [p=0.4] {a}Cinquenta "
        "mais zero vírgula quatro x [p=0.2] igual a vinte mais zero vírgula seis x. [p=0.2] Trinta igual a zero vírgula "
        "dois x. [p=0.2] *x igual a cento e cinquenta.* [p=0.4] {b}Pelo atalho: [p=0.2] cinquenta menos vinte, *trinta;* "
        "[p=0.2] sessenta menos quarenta centavos, *vinte centavos.* [p=0.2] Trinta por zero vírgula dois: [p=0.2] *cento e "
        "cinquenta.* [p=0.4] {c}Confira os dois: [p=0.2] cinquenta mais sessenta, *cento e dez.* [p=0.2] Vinte mais "
        "noventa, *cento e dez.* [p=0.3] {ok}*Letra D!*"),
    dict(id="20", block="q1", text=
        "{t}E as erradas? [p=0.3] {xa}A A dividiu os trinta pela *soma* das tarifas: [p=0.2] trinta por um. [p=0.4] {xb}A B "
        "dividiu pela tarifa do *Beta só:* [p=0.2] trinta por zero vírgula seis. [p=0.4] {xc}A C *somou* mensalidades e "
        "tarifas: [p=0.2] setenta por um. [p=0.4] {xe}E a E errou o sinal ao passar o vinte: [p=0.2] setenta por zero vírgula "
        "dois."),

    # ================= QUESTÃO 2 (VOCÊ FAZ) =================
    dict(id="21", block="q2", text=
        "{t}Agora é com você: [p=0.2] a gráfica do começo. [p=0.4] {a}A gráfica P cobra *cento e vinte reais* de taxa de "
        "arte [p=0.2] mais *trinta e cinco centavos* por cartaz impresso. [p=0.3] A gráfica Q não cobra taxa, [p=0.2] mas "
        "cobra *cinquenta centavos* por cartaz. [p=0.3] O *menor* número de cartazes [p=0.2] para o qual a gráfica P fica "
        "*mais barata* que a Q é: [p=0.4] {qa}A: duzentos e quarenta. [p=0.2] {qb}B: trezentos e quarenta e três. [p=0.2] "
        "{qc}C: quatrocentos e oitenta. [p=0.2] {qd}D: oitocentos. [p=0.2] {qe}E: oitocentos e um. [p=0.4] {p}*Pause o "
        "vídeo e resolva.* [p=2.0]"),
    dict(id="22", block="q2", text=
        "{t}*Mais barata:* [p=0.2] inequação. [p=0.4] {a}Cento e vinte mais zero vírgula trinta e "
        "cinco n [p=0.2] *menor que* zero vírgula cinco n. [p=0.2] Cento e vinte menor que zero vírgula quinze n. [p=0.2] "
        "*n maior que oitocentos.* [p=0.4] {b}Pelo atalho: [p=0.2] Q não tem taxa, [p=0.2] então a diferença das taxas é o "
        "próprio cento e vinte. [p=0.2] Cento e vinte por quinze centavos: [p=0.2] *oitocentos.* [p=0.4] {c}Com oitocentos, "
        "[p=0.2] as duas custam quatrocentos. [p=0.2] *Empate.* [p=0.2] Com oitocentos e um, [p=0.2] P custa quatrocentos e "
        "trinta e cinco centavos; [p=0.2] Q, quatrocentos e cinquenta. [p=0.3] {ok}*Letra E!*"),
    dict(id="23", block="q2", text=
        "{t}E as erradas? [p=0.3] {xd}A D é *o empate:* [p=0.2] no empate ninguém é mais barato. [p=0.4] {xa}A A dividiu "
        "cento e vinte por *cinquenta centavos,* [p=0.2] o preço de uma gráfica só. [p=0.4] {xb}A B dividiu por *trinta e "
        "cinco centavos,* [p=0.2] o preço da outra. [p=0.4] {xc}E a C errou a subtração: [p=0.2] usou *vinte e cinco* "
        "centavos [p=0.2] no lugar de quinze."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="24", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] taxa fixa menor ganha no começo; [p=0.2] preço por "
        "unidade menor ganha no fim. [p=0.5] {b}Dois: [p=0.2] equilíbrio é a diferença das taxas, [p=0.2] dividida pela "
        "diferença dos preços. [p=0.5] {c}Três: [p=0.2] no empate ninguém é mais barato."),

    # ================= PONTE E CTA =================
    dict(id="25", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos tudo, [p=0.3] {b}caçamos as pegadinhas [p=0.3] {c}e vemos "
        "estas equações aparecendo *na Física* [p=0.2] e *nos juros.*"),
    dict(id="26", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual plano você já escolheu sem fazer essa conta? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
