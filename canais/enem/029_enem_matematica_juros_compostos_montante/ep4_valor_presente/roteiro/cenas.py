# Roteiro — Juros Compostos e Montante, Episódio 4 de 5: trazendo valores para hoje (valor presente)
# Base: Estudos/Enem/estudos/01-matematica/14-juros-compostos-montante.html — seção 07 + Questão 3 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (do prompt):
#   O FILME AO CONTRÁRIO: ir para o futuro é multiplicar pelo fator; voltar para hoje é dividir pelo mesmo fator.
#   TIRAR 10% NÃO DESFAZ UM AUMENTO DE 10% (a mesma armadilha de Porcentagem: 100 → 110 → 99).
#   O NÚMERO DE HOJE É SEMPRE MENOR que o de amanhã.
#   (Da série: PENSE EM FATORES, do episódio 1.)
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos (do material/prompt): 1,05² = 1,1025; 11.025 ÷ 1,1025 = 10.000; 11.025 · 0,95² = 9.950,06 (gancho e bloco c).
#   Pré-requisito de Porcentagem (prompt): 1 ÷ 1,25 = 0,80 (o preço que subiu 25%: 125 ÷ 1,25 = 100).
#   Nós fazemos (prompt): 1,1² = 1,21; 4.840 ÷ 1,21 = 4.000; conferência 4.000 · 1,21 = 4.840.
#   Erros (NOSSOS, com os números do exemplo do material, para não entregar a Q3): tirar 5% duas vezes = 9.950,06;
#   fator simples 1 + 0,05 · 2 = 1,10 → 11.025 ÷ 1,1 ≈ 10.022,73; só um período 11.025 ÷ 1,05 = 10.500;
#   multiplicar 11.025 · 1,1025 ≈ 12.155,06 (projetou para o futuro).
#   Atalhos (NOSSOS, verde): "dividir por 1,21 = dividir por 121 e multiplicar por 100" (4.840 ÷ 121 = 40 → 4.000);
#   "na prova, multiplique as alternativas pelo fator: a que vira o valor futuro é a certa".
# QUESTÃO 3 (eu faço; erradas do material, que estão certas): 12.100 ÷ 1,21 = 10.000 (A). B = ÷ 1,20, fator de juros
#   simples (10.083,33); D = desconta só um ano (12.100 ÷ 1,1 = 11.000); C = retira 10% uma vez só (10.890,00);
#   E = multiplica pelo fator (14.641,00).
# Frases-chave (meio e fim, idênticas): 1. Para o futuro, multiplique; para hoje, divida pelo mesmo fator.
#   2. Tirar 10% não desfaz um aumento de 10%. 3. Confira multiplicando de volta.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Quanto aplicar hoje? Valor presente em juros compostos · Matemática ENEM, Juros compostos episódio 4"

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
        "{a}Para ter *onze mil e vinte e cinco reais* daqui a dois anos, [p=0.2] a *cinco por cento ao ano,* [p=0.2] "
        "quanto aplicar *hoje?* [p=0.5] {b}Quem tira cinco por cento duas vezes [p=0.2] chega a *nove mil, novecentos e "
        "cinquenta reais e seis centavos* [p=0.2] e fica devendo. [p=0.5] {c}A resposta certa é redonda: [p=0.2] *dez "
        "mil reais.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai trazer *qualquer valor do futuro* para hoje [p=0.3] {b}com *uma "
        "divisão.*"),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] *M igual a C vezes um mais i, elevado a t.* "
        "[p=0.4] {b}E da série de Porcentagem: "
        "[p=0.2] para voltar ao valor original, [p=0.2] *divida pelo fator.* [p=0.3] Um preço que subiu vinte e cinco "
        "por cento [p=0.2] virou cento e vinte e cinco. [p=0.2] Cento e vinte e cinco dividido por um vírgula vinte e "
        "cinco: [p=0.2] *cem* de novo."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{a}Pense numa família que quer *trocar de carro* [p=0.2] daqui a *dois anos.* [p=0.4] "
        "{b}A pergunta é outra: [p=0.2] quanto ela precisa *depositar hoje,* [p=0.2] "
        "para o dinheiro crescer até lá? [p=0.4] {c}É a conta do episódio um [p=0.2] *ao "
        "contrário.*"),
    dict(id="05", block="concreto", text=
        "{t}Dois nomes para guardar. [p=0.3] {a}*Valor futuro* [p=0.2] é quanto o dinheiro vale *lá na frente.* "
        "[p=0.2] É o montante. [p=0.4] {b}*Valor presente* [p=0.2] é quanto ele vale *hoje.* [p=0.2] É o capital. "
        "[p=0.4] {c}E *trazer para hoje* [p=0.2] é descobrir o valor presente [p=0.2] a partir do valor futuro."),

    # ================= BLOCO A: A FÓRMULA =================
    dict(id="06", block="formula", text=
        "{t}E como se volta no tempo? [p=0.4] {a}Pense num *filme ao contrário.* [p=0.2] Ir para o futuro [p=0.2] é "
        "*multiplicar* pelo fator. [p=0.4] {b}Voltar para hoje [p=0.2] é *dividir* pelo mesmo fator. [p=0.4] {c}Na "
        "fórmula, [p=0.2] você *isola o capital:* [p=0.2] *C igual a M dividido por um mais i, elevado a t.*"),

    # ================= BLOCO B: O EXEMPLO =================
    dict(id="07", block="exemplo", text=
        "{t}Vamos ao gancho. [p=0.3] {a}*M* é onze mil e vinte e cinco. [p=0.2] *i* é cinco por cento. [p=0.2] *t* é "
        "dois anos. [p=0.4] {b}Primeiro o *fator,* [p=0.2] e só depois a divisão. [p=0.2] Um vírgula zero cinco ao "
        "quadrado: [p=0.2] *um vírgula um zero dois cinco.* [p=0.4] {c}Agora divida: [p=0.2] onze mil e vinte e cinco "
        "por um vírgula um zero dois cinco. [p=0.2] *Dez mil reais.*"),

    # ================= BLOCO C: POR QUE NÃO TIRAR 5% =================
    dict(id="08", block="desfaz", text=
        "{t}E por que tirar cinco por cento duas vezes não funciona? [p=0.4] {a}Onze mil e vinte e cinco, [p=0.2] "
        "vezes zero vírgula noventa e cinco, [p=0.2] duas vezes: [p=0.2] *nove mil, novecentos e cinquenta reais e seis "
        "centavos.* [p=0.4] {b}Menos que os dez mil. [p=0.2] A família aplicaria pouco [p=0.2] e *ficaria devendo.*"),
    dict(id="09", block="desfaz", text=
        "{t}O motivo é velho conhecido. [p=0.3] {a}Cem reais com aumento de dez por cento: [p=0.2] *cento e dez.* "
        "[p=0.4] {b}Agora tire dez por cento de cento e dez: [p=0.2] *noventa e nove.* [p=0.2] Não volta para cem! "
        "[p=0.4] {c}Tirar dez por cento não desfaz um aumento de dez por cento, [p=0.2] porque o desconto incide sobre "
        "um valor *maior.*"),

    # ================= BLOCO D: A CONFERÊNCIA =================
    dict(id="10", block="confere", text=
        "{t}E como ter certeza da resposta? [p=0.4] {a}Primeiro: [p=0.2] o número de hoje é sempre *menor* que o de "
        "amanhã. [p=0.2] Se saiu maior, [p=0.2] você multiplicou. [p=0.4] {b}Segundo: [p=0.2] *multiplique de volta.* "
        "[p=0.2] Dez mil vezes um vírgula um zero dois cinco: [p=0.2] *onze mil e vinte e cinco.* [p=0.2] Bateu. "
        "[p=0.4] {c}Atalho de prova: [p=0.2] multiplique as alternativas pelo fator. [p=0.2] A que vira o valor futuro "
        "[p=0.2] é a certa."),

    # ================= BLOCO E: PARA QUE SERVE =================
    dict(id="11", block="serve", text=
        "{t}E para que serve isso? [p=0.4] {a}Para *comparar pagamentos em datas diferentes.* "
        "[p=0.2] Mil reais hoje [p=0.2] e mil reais daqui a um ano [p=0.2] *não valem a mesma coisa.* [p=0.4] {b}Traga "
        "tudo para hoje, [p=0.2] e a comparação fica justa. [p=0.4] {c}Isso volta com força nas séries de "
        "*Empréstimos e financiamentos* [p=0.2] e de *Comparação de propostas.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="12", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Quanto aplicar hoje, [p=0.2] a juros compostos de *dez por cento ao ano,* [p=0.2] para "
        "ter *quatro mil, oitocentos e quarenta reais* [p=0.2] daqui a *dois anos?* [p=0.3] {b}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="13", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}O fator primeiro: [p=0.2] um vírgula um ao quadrado, [p=0.2] *um vírgula vinte e "
        "um.* [p=0.4] {b}Agora a divisão: [p=0.2] quatro mil, oitocentos e quarenta por um vírgula vinte e um. [p=0.2] "
        "Atalho: [p=0.2] divida por *cento e vinte e um,* [p=0.2] que dá quarenta, [p=0.2] e multiplique por cem. "
        "[p=0.2] *Quatro mil reais.* [p=0.4] {c}Confere: [p=0.2] quatro mil vezes um vírgula vinte e um, [p=0.2] "
        "*quatro mil, oitocentos e quarenta.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="14", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] para o futuro, multiplique; [p=0.2] para hoje, divida "
        "pelo mesmo fator. [p=0.5] {b}Dois: [p=0.2] tirar dez por cento não desfaz um aumento de dez por cento. "
        "[p=0.5] {c}Três: [p=0.2] confira multiplicando de volta."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="15", block="erros", text=
        "{t}Agora, os quatro erros clássicos, [p=0.2] com os números do gancho. [p=0.4] {a}Primeiro: [p=0.2] *tirar "
        "cinco por cento* a cada ano. [p=0.4] {b}Parece certo, [p=0.2] porque o dinheiro cresceu cinco por cento por "
        "ano. [p=0.4] {c}Mas o desconto incide sobre um valor maior: [p=0.2] sai nove mil, novecentos e cinquenta. "
        "[p=0.2] Divida pelo fator."),
    dict(id="16", block="erros", text=
        "{a}Segundo: [p=0.2] dividir pelo fator de *juros simples,* [p=0.2] um vírgula dez. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque cinco mais cinco é dez. [p=0.4] {c}Mas aqui os juros são *compostos:* [p=0.2] o fator é um "
        "vírgula um zero dois cinco. [p=0.2] Com um vírgula dez, [p=0.2] sai uns *dez mil e vinte e dois.*"),
    dict(id="17", block="erros", text=
        "{a}Terceiro: [p=0.2] trazer *só um período.* [p=0.4] {b}Parece certo, [p=0.2] porque dividir por um vírgula "
        "zero cinco [p=0.2] já parece voltar no tempo. [p=0.4] {c}Mas são *dois anos:* [p=0.2] o expoente é dois. "
        "[p=0.2] Com um ano só, [p=0.2] sai *dez mil e quinhentos.*"),
    dict(id="18", block="erros", text=
        "{a}Quarto: [p=0.2] *multiplicar* pelo fator em vez de dividir. [p=0.4] {b}Parece certo, [p=0.2] porque é a "
        "fórmula que você decorou. [p=0.4] {c}Mas multiplicar leva para o *futuro:* [p=0.2] sai uns *doze mil, cento "
        "e cinquenta e cinco.* [p=0.2] Maior que o valor futuro: [p=0.2] impossível para o valor de hoje."),

    # ================= QUESTÃO 3 (EU FAÇO) =================
    dict(id="19", block="q3", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.2] É a família do começo. "
        "[p=0.4] {a}Uma família quer ter *doze mil e cem reais* [p=0.2] daqui a *dois anos* [p=0.2] para trocar de "
        "carro. [p=0.2] Ela encontrou uma aplicação [p=0.2] que rende juros compostos de *dez por cento ao ano.* "
        "[p=0.2] O valor que deve ser aplicado hoje, [p=0.2] em um único depósito, é de: [p=0.4] {qa}A: [p=0.2] dez "
        "mil reais. [p=0.3] {qb}B: [p=0.2] dez mil e oitenta e três reais e trinta e três centavos. [p=0.3] {qc}C: "
        "[p=0.2] dez mil, oitocentos e noventa. [p=0.3] {qd}D: [p=0.2] onze mil. [p=0.3] {qe}E: [p=0.2] catorze mil, "
        "seiscentos e quarenta e um. [p=0.4] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="20", block="q3", text=
        "{t}Eu resolvo com você. [p=0.3] {a}É *valor presente:* [p=0.2] o futuro está dado, [p=0.2] o hoje é a "
        "pergunta. [p=0.4] {b}O fator de dois anos: [p=0.2] um vírgula um ao quadrado, [p=0.2] *um vírgula vinte e "
        "um.* [p=0.4] {c}Doze mil e cem dividido por um vírgula vinte e um: [p=0.2] *dez mil reais.* [p=0.4] "
        "{d}Confere: [p=0.2] dez mil vezes um vírgula vinte e um, [p=0.2] doze mil e cem. [p=0.3] {ok}*Letra A!*"),
    dict(id="21", block="q3", text=
        "{t}E as outras? [p=0.3] {xb}A B divide por um vírgula vinte, [p=0.2] o fator de *juros simples.* [p=0.4] "
        "{xd}A D desconta *só um ano.* [p=0.4] {xc}A C tira dez por cento *uma vez só,* [p=0.2] o que nem desfaz o "
        "aumento de um ano. [p=0.4] {xe}E a E *multiplica* pelo fator: [p=0.2] projeta para o futuro."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="22", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] para o futuro, multiplique; [p=0.2] para hoje, "
        "divida pelo mesmo fator. [p=0.5] {b}Dois: [p=0.2] tirar dez por cento não desfaz um aumento de dez por cento. "
        "[p=0.5] {c}Três: [p=0.2] confira multiplicando de volta."),

    # ================= PONTE E CTA =================
    dict(id="23", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos tudo, [p=0.3] {b}caçamos as pegadinhas [p=0.3] {c}e "
        "treinamos com questões no formato do ENEM."),
    dict(id="24", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] para ter mil reais daqui a um ano, a dez por cento, quanto você "
        "aplicaria hoje? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir "
        "os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos "
        "minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
