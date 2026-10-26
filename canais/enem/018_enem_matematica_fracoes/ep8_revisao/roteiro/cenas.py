# Roteiro — Frações, Decimais e Dízimas, Episódio 8 de 8: Revisão geral, pegadinhas e treino para o ENEM (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/03-fracoes-decimais-dizimas.html — seções 01, 11 e 13 (+ tabela da seção 10 no jogo).
#   NÃO usa as Questões 1–9 da seção 12. As 5 questões são INÉDITAS (situações hipotéticas, marcadas na tela).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora retomadas (uma frase cada, com o ícone do episódio, ANTES de cobrar):
#   ep1 PIZZA (denominador = em quantas fatias; numerador = quantas você pegou) · "de" = vezes · equivalentes = mesma pizza
#   cortada diferente · ep2 misto = pizzas inteiras e um pedaço · mesmo numerador: pizza para menos gente, fatia maior ·
#   ep3 soma = recortar no mesmo tamanho de fatia (MMC) · ep4 "do restante" = a pizza que encolhe · ep5 decimal = dinheiro
#   (moedas) · ep6 o 10 só aceita 2 e 5 (fita infinita, geratriz = a mãe da dízima) · ep7 três idiomas (três cartas).
# Jogo das 6 conversões (tabela da seção 10): 3/4 = 75% · 0,2 = 1/5 · 1/8 = 12,5% · 2/3 = 0,666… · 5% = 1/20 · 0,375 = 3/8.
# V/F (os 9 erros da seção 11; 6 falsas e 3 verdadeiras): 1 F (1/3 + 1/6) · 2 F (5/6) · 3 F (7 1/2) · 4 F (3/5 > 3/7) ·
#   5 F (0,012) · 6 V (40) · 7 V (racional) · 8 F (6/12 = 1/2 = 0,5) · 9 V (0,999… = 1).
# QUESTÕES INÉDITAS (todas conferidas em Python: uma única correta; cada errada = um erro clássico):
#   Q1 caminhão-pipa 6 000 L, entrega 1/5, depois 2/3 do restante → 6 000 · 4/5 · 1/3 = 1 600 → B.
#      A 800 (tirou 2/3 do TOTAL = somou 1/5 + 2/3 = 13/15) · C 2 000 (esqueceu a 1ª etapa: 1/3 de 6 000) ·
#      D 3 200 (respondeu a 2ª entrega) · E 4 800 (parou na 1ª etapa).
#   Q2 1/3 Matemática + 2/5 Linguagens = 5/15 + 6/15 = 11/15 → C. A 3/8 (termo a termo) · B 2/15 (multiplicou) ·
#      D 4/15 (respondeu o que sobrou) · E 3/15 (trocou o denominador e esqueceu de ajustar os numeradores: 1 + 2 = 3).
#   Q3 Azul 3/4 = 0,75 · Verde 7/10 = 0,7 · Laranja 9/11 = 0,8181… → Laranja, Azul, Verde → E.
#      A Verde, Azul, Laranja (ordem crescente) · B Azul, Verde, Laranja (denominador menor = maior, fora do mesmo numerador) ·
#      C Laranja, Verde, Azul (só os numeradores) · D Azul, Laranja, Verde ("falta menos pedaço", com pedaços de tamanhos
#      diferentes: faltam 1/4, 2/11 e 3/10).
#   Q4 R$ 12,60 de crédito, página a R$ 0,35 → 1 260 ÷ 35 = 36 → D. A 3,6 (= 12,6 ÷ 3,5: andou a vírgula só no divisor) ·
#      B 4,41 (= 12,6 × 0,35: multiplicou) · C 12,25 (= 12,6 − 0,35: subtraiu) · E 360 (= 126 ÷ 0,35: andou só no dividendo).
#   Q5 7 em cada 20 usam bicicleta → 7/20 = 35/100 = 35% → D. A 0,35% (parou no decimal) · B 7% (leu o numerador como %) ·
#      C 13% (20 − 7) · E 65% (o complemento: quem NÃO usa).
# Checklist (seção 13) → episódio para rever: itens 1–3 ep1 · 4–6 ep2 · 7–8 ep3 · 9 ep4 · 10 ep5 · 11–12 ep6 · 13 ep7.
# Meta: 30 questões, pelo menos 21 acertos (70%), priorizando as de duas etapas com "do restante".
# Ponte: Potenciação e radiciação (expoente negativo ficou de fora da série).
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "9 pegadinhas e 5 questões estilo ENEM: revisão geral | Frações Ep. 8"
# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, numa aula de revisão animada, conversando "
            "de perto com um aluno que está treinando para o ENEM: voz calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas de verdadeiro ou falso com suspense, "
            "como num jogo; mostre surpresa nas pegadinhas; comemore os acertos com entusiasmo; dê ênfase forte às "
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
        "{a}Este é o assunto *mais subestimado* do ENEM. [p=0.4] {b}Quase nunca tem questão com o nome dele, [p=0.3] {c}mas ele "
        "está *dentro de dezenas* de outras. [p=0.5] {d}Hoje é a revisão final de frações, decimais e dízimas: [p=0.2] "
        "*nove pegadinhas* [p=0.2] e *cinco questões* no estilo do ENEM."),

    # ================= ONDE A FRAÇÃO APARECE (seção 01) =================
    dict(id="02", block="onde", text=
        "{t}Onde a fração se esconde na prova? [p=0.4] {a}Em probabilidade, [p=0.2] o resultado é sempre uma fração. [p=0.3] "
        "{b}Em porcentagem, [p=0.2] converter é o caminho mais rápido. [p=0.3] {c}Em estatística, [p=0.2] média e gráfico de "
        "setores. [p=0.3] {d}Em razão e proporção, [p=0.2] escala e velocidade. [p=0.3] {e}E na Física e na Química, [p=0.2] "
        "quase toda fórmula *é uma fração.*"),
    dict(id="03", block="onde", text=
        "{t}E quando a questão é *de fração* mesmo, [p=0.2] o formato mais comum é o problema em *duas etapas:* [p=0.4] "
        "{a}gasta-se uma fração de algo, [p=0.3] {b}depois uma fração *do que sobrou.* [p=0.4] {c}Parece simples, [p=0.2] e "
        "derruba muita gente."),

    # ================= ÍNDICE DA REVISÃO: OS 7 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] vamos relembrar tudo em uma frase por episódio. [p=0.4] {a}Episódio um: [p=0.2] a pizza. "
        "[p=0.2] Denominador, em quantas fatias; [p=0.2] numerador, quantas você pegou. [p=0.2] E *de* significa vezes. [p=0.4] "
        "{b}Dois: [p=0.2] o misto é pizzas inteiras e mais um pedaço, [p=0.2] e vira impróprio antes da conta. [p=0.4] "
        "{c}Três: [p=0.2] para somar, [p=0.2] recorte tudo no *mesmo tamanho de fatia.* [p=0.4] {d}Quatro: [p=0.2] a pizza "
        "que *encolhe.*"),
    dict(id="05", block="indice", text=
        "{a}Cinco: [p=0.2] decimal é *dinheiro;* [p=0.2] a vírgula separa reais de centavos. [p=0.4] {b}Seis: [p=0.2] o dez "
        "só aceita *dois e cinco,* [p=0.2] e a dízima tem uma fração mãe, [p=0.2] a geratriz. [p=0.4] {c}E sete: [p=0.2] "
        "fração, decimal e porcentagem são *três idiomas* do mesmo número."),

    # ================= AS DUAS COISAS QUE MAIS RENDEM =================
    dict(id="06", block="rendem", text=
        "{t}E se você só tiver tempo para *duas* coisas, [p=0.2] são estas: [p=0.4] {a}a tabela fração, decimal, porcentagem, "
        "[p=0.2] de cor; [p=0.4] {b}e o cuidado com o *do restante.* [p=0.4] {c}Juntas, [p=0.2] valem mais que toda a teoria "
        "de dízimas."),
    dict(id="07", block="jogo", text=
        "{t}Então, [p=0.2] jogo rápido: [p=0.2] seis conversões. [p=0.4] {a}Três quartos, em porcentagem. [p=0.3] {b}Zero "
        "vírgula dois, em fração. [p=0.3] {c}Um oitavo, em porcentagem. [p=0.3] {d}Dois terços, em decimal. [p=0.3] {e}Cinco "
        "por cento, em fração. [p=0.3] {f}E zero vírgula trezentos e setenta e cinco, em fração. [p=0.4] {p}*Pause e "
        "responda.* [p=2.0]"),
    dict(id="08", block="jogo", text=
        "{t}Conferindo! [p=0.3] {a}Setenta e cinco por cento. [p=0.3] {b}Um quinto. [p=0.3] {c}Doze vírgula cinco por cento. "
        "[p=0.3] {d}Zero vírgula seis, seis, seis, [p=0.2] repetindo. [p=0.3] {e}Um vinte avos. [p=0.3] {f}E três oitavos. "
        "[p=0.4] {g}Atalho para o que não estiver na tabela: [p=0.2] porcentagem vira fração *sobre cem,* [p=0.2] e depois "
        "simplifica."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="09", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.4] {a}São nove frases. [p=0.2] Algumas são pegadinhas, [p=0.2] outras "
        "são verdade. [p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de eu falar."),
    dict(id="10", block="vf", text=
        "{t}Um: [p=0.2] um terço, [p=0.2] e depois um quarto *do restante,* [p=0.2] é um terço mais um quarto. [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque as duas frações parecem do mesmo todo. [p=0.3] {g}Mas a pizza "
        "*encolheu:* [p=0.2] é um terço mais um sexto."),
    dict(id="11", block="vf", text=
        "{t}Dois: [p=0.2] um meio mais um terço [p=0.2] dá dois quintos. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana "
        "porque na multiplicação se faz em cima com em cima. [p=0.3] {g}Na soma, [p=0.2] recorte no mesmo tamanho de fatia: "
        "[p=0.2] *cinco sextos.*"),
    dict(id="12", block="vf", text=
        "{t}Três: [p=0.2] dois e meio vezes três [p=0.2] dá seis e meio. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana "
        "porque parece natural multiplicar só o inteiro. [p=0.3] {g}Vire impróprio antes: [p=0.2] cinco meios vezes três, "
        "[p=0.2] quinze meios, [p=0.2] *sete e meio.*"),
    dict(id="13", block="vf", text=
        "{t}Quatro: [p=0.2] três sétimos é maior que três quintos, [p=0.2] porque sete é maior que cinco. [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque número maior parece fração maior. [p=0.3] {g}Mesmo numerador: [p=0.2] "
        "pizza para menos gente [p=0.2] dá fatia *maior.*"),
    dict(id="14", block="vf", text=
        "{t}Cinco: [p=0.2] zero vírgula três vezes zero vírgula zero quatro [p=0.2] dá zero vírgula doze. [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque três vezes quatro é doze mesmo. [p=0.3] {g}Mas some as casas: [p=0.2] "
        "uma mais duas, [p=0.2] três casas. [p=0.2] *Zero vírgula zero doze.*"),
    dict(id="15", block="vf", text=
        "{t}Seis: [p=0.2] quatro vírgula oito dividido por zero vírgula doze [p=0.2] dá *mais* que quatro vírgula oito. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque a gente aprendeu que dividir diminui. [p=0.3] "
        "{g}Mas quantas moedas de doze centavos cabem em quatro e oitenta? [p=0.2] *Quarenta.*"),
    dict(id="16", block="vf", text=
        "{t}Sete: [p=0.2] toda dízima periódica é um número *racional.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] "
        "{e}Parece falso porque ela nunca termina. [p=0.3] {g}Mas se repete com padrão, [p=0.2] tem fração mãe, [p=0.2] a "
        "geratriz. [p=0.2] Irracional é o que *não* repete."),
    dict(id="17", block="vf", text=
        "{t}Oito: [p=0.2] seis doze avos *não* dá decimal exato, [p=0.2] porque o doze tem o fator três. [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o critério foi usado antes da hora. [p=0.3] {g}Simplifique primeiro: "
        "[p=0.2] um meio. [p=0.2] O dez aceita o dois: [p=0.2] *zero vírgula cinco.*"),
    dict(id="18", block="vf", text=
        "{t}E nove: [p=0.2] zero vírgula nove, nove, nove, [p=0.2] repetindo para sempre, [p=0.2] é *exatamente* um. [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque soa como quase um. [p=0.3] {g}Mas dez xis menos xis "
        "dá nove xis igual a nove: [p=0.2] xis é *um.* [p=0.2] Duas escritas do mesmo número."),
    dict(id="19", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] as cinco questões. "
        "[p=0.2] Todas inéditas, [p=0.2] no estilo do ENEM."),

    # ================= QUESTÃO 1: DO RESTANTE =================
    dict(id="20", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Um caminhão-pipa sai com *seis mil litros* de água. [p=0.3] {b}Na primeira parada, "
        "[p=0.2] entrega *um quinto* da carga. [p=0.3] {c}Na segunda, [p=0.2] entrega *dois terços do que restou.* [p=0.3] "
        "{d}Quantos litros ficam no caminhão? [p=0.4] {la}A, [p=0.2] oitocentos. [p=0.2] {lb}B, [p=0.2] mil e seiscentos. "
        "[p=0.2] {lc}C, [p=0.2] dois mil. [p=0.2] {ld}D, [p=0.2] três mil e duzentos. [p=0.2] {le}E, [p=0.2] quatro mil e "
        "oitocentos. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="21", block="q1", text=
        "{t}Primeira etapa: [p=0.2] um quinto de seis mil, [p=0.2] mil e duzentos. [p=0.2] {a}Restam *quatro mil e oitocentos.* "
        "[p=0.3] {b}A pizza encolheu! [p=0.2] Dois terços de quatro mil e oitocentos: [p=0.2] três mil e duzentos. [p=0.3] "
        "{c}Ficam *mil e seiscentos.* [p=0.2] {ok}*Letra B!* [p=0.3] {g}Atalho: [p=0.2] multiplique o que *fica:* [p=0.2] "
        "quatro quintos, [p=0.2] depois um terço. [p=0.4] {xa}A A tirou dois terços do total. [p=0.2] {xc}A C esqueceu a "
        "primeira parada. [p=0.2] {xd}A D é a segunda entrega. [p=0.2] {xe}E a E parou na primeira etapa."),

    # ================= QUESTÃO 2: SOMA EM CONTEXTO =================
    dict(id="22", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Lucas dedicou *um terço* das horas de estudo da semana a Matemática [p=0.2] {b}e *dois "
        "quintos* a Linguagens. [p=0.3] {c}Que fração das horas foi para essas duas áreas juntas? [p=0.4] {la}A, [p=0.2] três "
        "oitavos. [p=0.2] {lb}B, [p=0.2] dois quinze avos. [p=0.2] {lc}C, [p=0.2] onze quinze avos. [p=0.2] {ld}D, [p=0.2] "
        "quatro quinze avos. [p=0.2] {le}E, [p=0.2] três quinze avos. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="23", block="q2", text=
        "{t}Juntas é somar. [p=0.2] {a}Recorte no mesmo tamanho de fatia: [p=0.2] o MMC de três e cinco é quinze. [p=0.3] "
        "{b}Um terço vira cinco quinze avos. [p=0.2] Dois quintos viram seis quinze avos. [p=0.3] {c}Total: [p=0.2] *onze "
        "quinze avos.* [p=0.2] {ok}*Letra C!* [p=0.4] {xa}A A somou em cima com em cima, [p=0.2] embaixo com embaixo. [p=0.2] "
        "{xb}A B multiplicou. [p=0.2] {xd}A D é o que *sobrou.* [p=0.2] {xe}E a E trocou o denominador, [p=0.2] mas esqueceu "
        "de ajustar os numeradores."),

    # ================= QUESTÃO 3: COMPARAÇÃO =================
    dict(id="24", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Numa gincana, [p=0.2] três equipes completaram estas frações da trilha: [p=0.3] {b}Azul, "
        "[p=0.2] três quartos. [p=0.2] Verde, [p=0.2] sete décimos. [p=0.2] Laranja, [p=0.2] nove onze avos. [p=0.3] {c}Qual "
        "é a ordem, [p=0.2] da que andou mais [p=0.2] para a que andou menos? [p=0.4] {la}A, [p=0.2] Verde, Azul, Laranja. "
        "[p=0.2] {lb}B, [p=0.2] Azul, Verde, Laranja. [p=0.2] {lc}C, [p=0.2] Laranja, Verde, Azul. [p=0.2] {ld}D, [p=0.2] Azul, "
        "Laranja, Verde. [p=0.2] {le}E, [p=0.2] Laranja, Azul, Verde. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="25", block="q3", text=
        "{t}Três frações, [p=0.2] numeradores diferentes: [p=0.2] transforme em decimal. [p=0.3] {a}Três quartos, [p=0.2] zero "
        "vírgula setenta e cinco. [p=0.2] {b}Sete décimos, [p=0.2] zero vírgula sete. [p=0.2] {c}Nove onze avos, [p=0.2] zero "
        "vírgula oitenta e um, [p=0.2] repetindo. [p=0.3] {d}Laranja, Azul, Verde. [p=0.2] {ok}*Letra E!* [p=0.4] {xa}A A é a "
        "ordem ao contrário. [p=0.2] {xb}A B usou a regra do mesmo numerador, [p=0.2] que aqui não vale. [p=0.2] {xc}A C olhou "
        "só os numeradores. [p=0.2] {xd}E a D contou os pedaços que faltam, [p=0.2] mas os pedaços têm *tamanhos diferentes.*"),

    # ================= QUESTÃO 4: DIVISÃO DE DECIMAIS =================
    dict(id="26", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Uma estudante tem *doze reais e sessenta* de crédito de impressão. [p=0.3] {b}Cada "
        "página custa *trinta e cinco centavos.* [p=0.3] {c}Quantas páginas ela consegue imprimir? [p=0.4] {la}A, [p=0.2] três "
        "vírgula seis. [p=0.2] {lb}B, [p=0.2] quatro vírgula quarenta e um. [p=0.2] {lc}C, [p=0.2] doze vírgula vinte e cinco. "
        "[p=0.2] {ld}D, [p=0.2] trinta e seis. [p=0.2] {le}E, [p=0.2] trezentos e sessenta. [p=0.4] {p}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="27", block="q4", text=
        "{t}Quantas vezes trinta e cinco centavos cabem em doze e sessenta? [p=0.3] {a}Iguale as casas [p=0.2] e tire as "
        "vírgulas: [p=0.2] mil duzentos e sessenta dividido por trinta e cinco. [p=0.3] {b}Dá *trinta e seis.* [p=0.2] "
        "{ok}*Letra D!* [p=0.3] {g}Dividir por menos de um faz o número crescer. [p=0.4] {xa}A A andou a vírgula só no "
        "divisor. [p=0.2] {xe}A E, [p=0.2] só no dividendo. [p=0.2] {xb}A B multiplicou. [p=0.2] {xc}E a C subtraiu."),

    # ================= QUESTÃO 5: PORCENTAGEM E COMPLEMENTO =================
    dict(id="28", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Numa pesquisa em um bairro, [p=0.2] *sete em cada vinte* moradores disseram que vão "
        "ao trabalho de bicicleta. [p=0.3] {b}Que porcentagem dos pesquisados usa bicicleta? [p=0.4] {la}A, [p=0.2] zero vírgula "
        "trinta e cinco por cento. [p=0.2] {lb}B, [p=0.2] sete por cento. [p=0.2] {lc}C, [p=0.2] treze por cento. [p=0.2] "
        "{ld}D, [p=0.2] trinta e cinco por cento. [p=0.2] {le}E, [p=0.2] sessenta e cinco por cento. [p=0.4] {p}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="29", block="q5", text=
        "{t}Sete em cada vinte: [p=0.2] sete vinte avos. [p=0.3] {g}Atalho: [p=0.2] vinte vezes cinco é cem. [p=0.2] {a}Então "
        "multiplique em cima e embaixo por cinco: [p=0.2] *trinta e cinco centésimos,* [p=0.2] trinta e cinco por cento. "
        "[p=0.2] {ok}*Letra D!* [p=0.4] {xe}E a pegadinha é a E: [p=0.2] sessenta e cinco por cento é quem *não* usa. [p=0.3] "
        "{xa}A A parou no decimal. [p=0.2] {xb}A B leu o sete como porcentagem. [p=0.2] {xc}E a C fez vinte menos sete."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="30", block="checklist", text=
        "{t}Agora, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* para outra "
        "pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}Os quatro significados, [p=0.2] simplificar pelo MDC [p=0.2] e o "
        "produto cruzado: [p=0.2] episódio um. [p=0.3] {c}Misto, [p=0.2] mesmo numerador [p=0.2] e ordenar em decimal: "
        "[p=0.2] episódio dois. [p=0.3] {d}As quatro operações [p=0.2] e o corte em cruz: [p=0.2] episódio três."),
    dict(id="31", block="checklist", text=
        "{a}O do restante: [p=0.2] episódio quatro. [p=0.3] {b}Contas com decimais: [p=0.2] episódio cinco. [p=0.3] {c}Prever "
        "o decimal exato [p=0.2] e achar a geratriz: [p=0.2] episódio seis. [p=0.3] {d}E a tabela de cor: [p=0.2] episódio "
        "sete. [p=0.4] {e}O que você *não* marcou, [p=0.2] reveja o episódio correspondente."),

    # ================= META =================
    dict(id="32", block="meta", text=
        "{t}E antes de considerar este assunto dominado, [p=0.2] uma meta: [p=0.3] {a}resolva *trinta* questões [p=0.2] {b}e "
        "acerte pelo menos *vinte e uma,* [p=0.2] setenta por cento. [p=0.4] {c}Priorize as de duas etapas, [p=0.2] com o *do "
        "restante.* [p=0.2] São as que separam."),

    # ================= PONTE E CTA =================
    dict(id="33", block="ponte", text=
        "{a}Com este assunto, [p=0.2] a primeira semana de Matemática está *fechada.* [p=0.4] {b}O próximo é *Potenciação e "
        "radiciação.* [p=0.3] {c}E lá entra o *expoente negativo,* [p=0.2] que ficou de fora aqui."),
    dict(id="34", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantas das cinco questões você acertou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de frações está completa. [p=0.2] Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
