# Roteiro — Função Modular e Funções por Partes, Episódio 2 de 5: faixas progressivas (cada parte paga a taxa da sua
#   faixa)
# Base: Estudos/Enem/estudos/01-matematica/29-funcao-modular-funcoes-por-partes.html — seção 08 + Questões 7 e 1 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (do prompt):
#   A ESCADA DE CAIXINHAS: o valor sobe uma escada de caixinhas; cada caixinha só cobra pelo pedaço que cabe dentro dela.
#   O ALARME: "parte", "excedente", "que ultrapassar" é o alarme do progressivo.
#   O TROCO: a parcela a deduzir é o troco: cobra-se a alíquota maior sobre tudo e devolve-se o que foi cobrado a mais.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos do material/prompt: lucro de R$ 7.000,00 fatiado em 2.000 + 3.000 + 2.000 → 0 + 300 + 400 = 700 (blocos b, c,
#   e; é a Q7, "eu faço") · 20% sobre tudo = 1.400 · T(x) = 300 + 0,2(x − 5.000) · 0,2x − 700 · nós fazemos (isento até
#   1.000; 5% até 3.000; 15% acima; lucro 4.000) → 100 + 150 = 250; 15% sobre tudo = 600.
# Exemplos NOSSOS (conferidos em trabalho/conferir_contas.py):
#   bloco d (faixa única): até 20 m³, R$ 5,00 por m³; quem consome MAIS de 20 m³ paga R$ 8,00 por m³ no consumo todo →
#     20 m³ = R$ 100,00 e 21 m³ = R$ 168,00 (o salto). Números diferentes da Q1, para não adiantar a "você faz".
#   bloco e: de onde vem o 700 → 20% cobrados sobre os 2.000 isentos (400) + 10% a mais nos 3.000 do meio (300).
#   nós fazemos, conferência pela parcela: 0,15 · 1.000 + 0,10 · 2.000 = 350 → 600 − 350 = 250.
#   erros clássicos com os números do nós fazemos (já resolvido), para não gastar antes as alternativas da Q7:
#     1) 15% sobre tudo = 600 · 2) sem a isenção (5% desde o zero) = 150 + 150 = 300 · 3) sem a faixa do meio (15% sobre
#     tudo o que passa de 1.000) = 450.
#   CTA: lucro de R$ 9.000,00 → 300 + 0,2 · 4.000 = 1.100.
# Atalhos (NOSSOS, verde): "escreva o tamanho da fatia antes da taxa" · "acumulado até a fronteira + taxa × o que passou"
#   · "alíquota maior × tudo − parcela a deduzir" · "confira: a taxa efetiva fica abaixo da maior alíquota".
# QUESTÃO 7 (eu faço): 0 + 300 + 400 = 700 (B); conferência 1.400 − 700 = 700. Erradas (material): A = 10% de 5.000 = 500
#   (para na faixa do meio) · C = 10% desde o zero + 400 = 900 (sem a isenção) · D = 20% de tudo que passa de 2.000 =
#   1.000 · E = 20% do lucro inteiro = 1.400.
# QUESTÃO 1 (você faz): 40 + 10 · 6 + 6 · 9 = 154 (B). Erradas (prompt/material): A = 40 + 16 · 6 = 136 (esquece a 3ª
#   faixa) · C = 26 · 6 = 156 · D = 40 + 16 · 9 = 184 · E = 26 · 9 = 234.
# Frases-chave (meio e fim, idênticas): 1. Cada fatia paga a taxa da sua caixinha. 2. "Parte", "excedente", "que
#   ultrapassar": é progressivo. 3. Parcela a deduzir: cobra tudo na taxa maior e devolve o excesso.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Imposto progressivo e conta de água por faixas: cada parte paga a sua taxa | Função Modular Ep. 2"
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
        "{a}Lucro de *sete mil reais,* [p=0.2] taxa de *até vinte por cento.* [p=0.4] {b}Quem multiplica sete mil por "
        "zero vírgula vinte [p=0.2] paga *mil e quatrocentos reais.* [p=0.4] {c}A conta certa dá *setecentos reais:* "
        "[p=0.2] *metade.* [p=0.4] {d}A diferença está numa *palavra* do enunciado."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai calcular qualquer imposto ou tarifa progressiva *faixa por faixa* "
        "[p=0.3] {b}e conferir pelo atalho da *parcela a deduzir.*"),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Da série de Porcentagem: [p=0.2] *dez por cento é multiplicar por zero "
        "vírgula dez.* [p=0.4] {b}E do episódio um: [p=0.2] numa função por partes, [p=0.2] primeiro você *localiza "
        "a faixa,* [p=0.2] depois calcula."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Imagine os sete mil reais como uma *barra.* [p=0.4] {a}Agora a gente *corta* essa barra em três fatias: "
        "[p=0.2] *dois mil,* [p=0.2] *três mil* [p=0.2] e *dois mil.* [p=0.4] {b}Cada fatia cai na sua *caixinha,* "
        "[p=0.2] e cada caixinha tem a *sua taxa.* [p=0.4] {c}Você já viu isso disfarçado de desconto numa loja; "
        "[p=0.2] agora é *imposto e conta de água.*"),

    # ================= BLOCO A: O QUE É PROGRESSIVO =================
    dict(id="05", block="termos", text=
        "{t}Primeiro, as palavras. [p=0.4] {a}*Alíquota* é a porcentagem cobrada. [p=0.2] Dez por cento, vinte por "
        "cento. [p=0.4] {b}*Isento* é quem *não paga nada* naquela faixa. [p=0.4] {c}E *excedente,* [p=0.2] ou *a "
        "parte que ultrapassar,* [p=0.2] é só o pedaço que *passou* do limite."),
    dict(id="06", block="termos", text=
        "{t}E o que é cobrança *progressiva?* [p=0.4] {a}É quando a alíquota maior incide *só sobre a parte que passa* "
        "do limite. [p=0.2] *Não* sobre o valor todo. [p=0.4] {b}O valor sobe uma *escada de caixinhas:* [p=0.2] cada "
        "caixinha só cobra pelo pedaço que *cabe dentro dela.*"),

    # ================= BLOCO B: FATIANDO OS 7.000 =================
    dict(id="07", block="fatias", text=
        "{t}Vamos fatiar os sete mil. [p=0.3] {a}Até *dois mil:* [p=0.2] isento. [p=0.2] A primeira fatia tem dois mil, "
        "[p=0.2] e paga *zero.* [p=0.4] {b}De dois mil a cinco mil: [p=0.2] a fatia tem *três mil.* [p=0.2] Dez por "
        "cento de três mil: [p=0.2] *trezentos.* [p=0.4] {c}De cinco mil a sete mil: [p=0.2] a fatia tem *dois mil.* "
        "[p=0.2] Vinte por cento de dois mil: [p=0.2] *quatrocentos.* [p=0.4] {d}Somando: [p=0.2] zero mais trezentos "
        "mais quatrocentos: [p=0.2] *setecentos reais.*"),
    dict(id="08", block="fatias", text=
        "{t}E o jeito errado? [p=0.3] {a}A barra *inteira* cai na caixinha de vinte por cento: [p=0.2] *mil e "
        "quatrocentos.* [p=0.4] {b}O *dobro* do certo. [p=0.4] {c}Atalho: [p=0.2] *escreva o tamanho de cada fatia* "
        "antes de aplicar a taxa dela."),

    # ================= BLOCO C: A LEI DA ÚLTIMA FAIXA =================
    dict(id="09", block="lei", text=
        "{t}E para *qualquer* lucro acima de cinco mil? [p=0.4] {a}A lei fica: [p=0.2] *T de x igual a trezentos, "
        "mais zero vírgula dois vezes x menos cinco mil.* [p=0.4] {b}O *trezentos* é o imposto acumulado até a "
        "fronteira. [p=0.2] É a mesma ideia do episódio um: [p=0.2] *parte de onde a anterior parou.* [p=0.4] {c}E *x "
        "menos cinco mil* [p=0.2] é o pedaço que passou. [p=0.2] Com sete mil: [p=0.2] trezentos mais quatrocentos, "
        "[p=0.2] *setecentos.*"),

    # ================= BLOCO D: PROGRESSIVA × FAIXA ÚNICA =================
    dict(id="10", block="unica", text=
        "{t}Toda tabela de faixas é progressiva? [p=0.4] {a}*Não.* [p=0.2] Procure a palavra *parte,* *excedente* ou "
        "*que ultrapassar.* [p=0.2] Ela é o *alarme* do progressivo. [p=0.4] {b}Agora leia esta: [p=0.2] até vinte "
        "metros cúbicos, cinco reais por metro cúbico; [p=0.2] *quem consome mais de vinte paga oito reais por metro "
        "cúbico.* [p=0.4] {c}Não tem *excedente.* [p=0.2] Então os oito reais valem para o *consumo inteiro.*"),
    dict(id="11", block="unica", text=
        "{t}Veja o que acontece na fronteira. [p=0.4] {a}Vinte metros cúbicos: [p=0.2] vinte vezes cinco, [p=0.2] "
        "*cem reais.* [p=0.4] {b}Vinte e um: [p=0.2] vinte e um vezes oito, [p=0.2] *cento e sessenta e oito.* "
        "[p=0.4] {c}Um metro cúbico a mais [p=0.2] e a conta *salta* sessenta e oito reais. [p=0.2] No gráfico, um "
        "*degrau.* [p=0.2] No progressivo, a linha só *muda de inclinação.*"),

    # ================= BLOCO E: PARCELA A DEDUZIR =================
    dict(id="12", block="parcela", text=
        "{t}E existe um jeito *mais rápido?* [p=0.4] {a}As tabelas reais trazem a *parcela a deduzir:* [p=0.2] um "
        "valor fixo que você *subtrai* no fim. [p=0.4] {b}Para lucros acima de cinco mil: [p=0.2] *zero vírgula dois "
        "vezes x, menos setecentos.* [p=0.4] {c}Com sete mil: [p=0.2] mil e quatrocentos menos setecentos: [p=0.2] "
        "*setecentos.* [p=0.2] O mesmo resultado!"),
    dict(id="13", block="parcela", text=
        "{t}E de onde sai esse setecentos? [p=0.4] {a}A parcela a deduzir é o *troco.* [p=0.2] Cobra-se a alíquota "
        "maior sobre tudo [p=0.2] e devolve-se o que foi cobrado *a mais.* [p=0.4] {b}Cobrou vinte por cento sobre os "
        "dois mil isentos: [p=0.2] *quatrocentos* a mais. [p=0.4] {c}E dez por cento a mais nos três mil do meio: "
        "[p=0.2] *trezentos.* [p=0.2] Troco: [p=0.2] *setecentos.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="14", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Até *mil reais* é isento. [p=0.2] A parte entre mil e *três mil* paga *cinco por "
        "cento.* [p=0.2] A parte acima de três mil paga *quinze por cento.* [p=0.4] {b}Quanto paga quem lucrou "
        "*quatro mil reais?* [p=0.3] {c}*Pause e tente.* [p=2.0]"),
    dict(id="15", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Fatias: [p=0.2] *mil* isento, [p=0.2] *dois mil* a cinco por cento, [p=0.2] *mil* "
        "a quinze por cento. [p=0.4] {b}Zero, [p=0.2] mais *cem,* [p=0.2] mais *cento e cinquenta:* [p=0.2] *duzentos "
        "e cinquenta reais.* [p=0.4] {c}Quem aplica quinze por cento sobre tudo [p=0.2] acha *seiscentos.* [p=0.4] "
        "{d}Confira pelo troco: [p=0.2] seiscentos, menos trezentos e cinquenta: [p=0.2] *duzentos e cinquenta.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="16", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] cada fatia paga a taxa da sua caixinha. [p=0.5] "
        "{b}Dois: [p=0.2] parte, excedente, que ultrapassar: [p=0.2] é progressivo. [p=0.5] {c}Três: [p=0.2] parcela a "
        "deduzir: [p=0.2] cobra tudo na taxa maior e devolve o excesso."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="17", block="erros", text=
        "{t}Os três erros clássicos, [p=0.2] com os números do exercício. [p=0.4] {a}Primeiro: [p=0.2] aplicar a taxa "
        "da última faixa *sobre o valor todo.* [p=0.2] Quinze por cento de quatro mil: [p=0.2] seiscentos. [p=0.4] "
        "{b}Parece certo: [p=0.2] o lucro está *na* faixa dos quinze por cento. [p=0.4] {c}Mas só o pedaço *acima de "
        "três mil* mora nela. [p=0.2] O certo é duzentos e cinquenta."),
    dict(id="18", block="erros", text=
        "{a}Segundo: [p=0.2] *esquecer a faixa isenta.* [p=0.2] Cobrar cinco por cento desde o zero: [p=0.2] "
        "trezentos. [p=0.4] {b}Parece certo: [p=0.2] a primeira taxa que aparece na tabela é cinco por cento. [p=0.4] "
        "{c}Mas o primeiro mil *não paga nada.* [p=0.2] A fatia dos cinco por cento tem *dois mil,* não três."),
    dict(id="19", block="erros", text=
        "{a}Terceiro: [p=0.2] *esquecer a faixa do meio.* [p=0.2] Pular do isento direto para os quinze por cento: "
        "[p=0.2] quatrocentos e cinquenta. [p=0.4] {b}Parece certo: [p=0.2] a conta fica mais curta. [p=0.4] {c}Mas "
        "toda faixa entre o zero e o seu valor [p=0.2] *tem a sua fatia.* [p=0.2] Escada não pula degrau."),

    # ================= QUESTÃO 7 (EU FAÇO) =================
    dict(id="20", block="q7", text=
        "{t}Agora uma questão do nosso material de estudo, [p=0.2] e eu faço com você. [p=0.4] {a}Um município cobra "
        "uma taxa mensal sobre o lucro: [p=0.2] a parte até *dois mil reais* é isenta; [p=0.2] a parte entre dois mil "
        "e *cinco mil* paga *dez por cento;* [p=0.2] a parte que exceder cinco mil paga *vinte por cento.* [p=0.2] Um "
        "negócio lucrou *sete mil reais.* [p=0.2] Quanto paga? [p=0.4] {qa}A: [p=0.2] quinhentos. [p=0.3] {qb}B: "
        "[p=0.2] setecentos. [p=0.3] {qc}C: [p=0.2] novecentos. [p=0.3] {qd}D: [p=0.2] mil. [p=0.3] {qe}E: [p=0.2] mil "
        "e quatrocentos."),
    dict(id="21", block="q7", text=
        "{t}Procure o alarme: [p=0.2] *a parte, que exceder.* [p=0.2] É progressivo. [p=0.4] {a}Fatias: [p=0.2] dois "
        "mil isentos, [p=0.2] três mil a dez por cento, [p=0.2] dois mil a vinte. [p=0.4] {b}Zero mais trezentos mais "
        "quatrocentos: [p=0.2] *setecentos.* [p=0.4] {c}Confira pelo troco: [p=0.2] mil e quatrocentos menos "
        "setecentos: [p=0.2] *setecentos.* [p=0.3] {ok}*Letra B!*"),
    dict(id="22", block="q7", text=
        "{t}E as pegadinhas? [p=0.3] {xe}A E cobra vinte por cento do *lucro inteiro.* [p=0.4] {xa}A A cobra dez por "
        "cento de cinco mil [p=0.2] e *para aí:* [p=0.2] esquece a última faixa. [p=0.4] {xc}A C cobra dez por cento "
        "*desde o zero:* [p=0.2] esquece a isenção. [p=0.4] {xd}E a D cobra vinte por cento de *tudo o que passa de "
        "dois mil:* [p=0.2] esquece a faixa do meio."),

    # ================= QUESTÃO 1 (VOCÊ FAZ) =================
    dict(id="23", block="q1", text=
        "{t}Agora é com você. [p=0.4] {a}Uma companhia cobra a água assim: [p=0.2] tarifa mínima de *quarenta reais* "
        "até *dez metros cúbicos;* [p=0.2] *seis reais* por metro cúbico que exceder dez, até vinte; [p=0.2] e *nove "
        "reais* por metro cúbico que exceder vinte. [p=0.2] Uma casa consumiu *vinte e seis metros cúbicos.* [p=0.2] "
        "A conta foi de: [p=0.4] {qa}A: [p=0.2] cento e trinta e seis. [p=0.3] {qb}B: [p=0.2] cento e cinquenta e "
        "quatro. [p=0.3] {qc}C: [p=0.2] cento e cinquenta e seis. [p=0.3] {qd}D: [p=0.2] cento e oitenta e quatro. "
        "[p=0.3] {qe}E: [p=0.2] duzentos e trinta e quatro. [p=0.4] {p}*Pause o vídeo e resolva sozinho.* [p=2.5]"),
    dict(id="24", block="q1", text=
        "{t}Vamos conferir. [p=0.3] {a}O alarme está lá: [p=0.2] *que exceder.* [p=0.2] Fatias: [p=0.2] os primeiros "
        "dez na tarifa mínima; [p=0.2] de dez a vinte, *dez* metros cúbicos; [p=0.2] de vinte a vinte e seis, *seis.* "
        "[p=0.4] {b}Quarenta, [p=0.2] mais dez vezes seis, *sessenta,* [p=0.2] mais seis vezes nove, *cinquenta e "
        "quatro.* [p=0.4] {c}Total: [p=0.2] *cento e cinquenta e quatro reais.* [p=0.3] {ok}*Letra B!*"),
    dict(id="25", block="q1", text=
        "{t}E as erradas? [p=0.3] {xa}A A cobra os dezesseis acima de dez todos a seis: [p=0.2] *esquece a terceira "
        "faixa.* [p=0.4] {xd}A D cobra os dezesseis todos a *nove.* [p=0.4] {xc}A C multiplica o consumo todo por "
        "seis. [p=0.4] {xe}E a E aplica nove reais *a tudo,* [p=0.2] como se a última faixa valesse para o consumo "
        "inteiro."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="26", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] cada fatia paga a taxa da sua caixinha. [p=0.5] "
        "{b}Dois: [p=0.2] parte, excedente, que ultrapassar: [p=0.2] é progressivo. [p=0.5] {c}Três: [p=0.2] parcela "
        "a deduzir: [p=0.2] cobra tudo na taxa maior e devolve o excesso."),

    # ================= PONTE E CTA =================
    dict(id="27", block="ponte", text=
        "{a}Existe uma função por partes tão famosa [p=0.2] que ganhou um símbolo próprio: [p=0.2] *duas barrinhas.* "
        "[p=0.4] {b}Quanto vale *módulo de menos sete?* [p=0.3] {c}E por que o gráfico dela tem a forma de um *V?* "
        "[p=0.3] Próximo episódio."),
    dict(id="28", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] naquela taxa do município, [p=0.2] quanto paga quem lucrou *nove "
        "mil reais?* [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os "
        "*flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos "
        "minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
