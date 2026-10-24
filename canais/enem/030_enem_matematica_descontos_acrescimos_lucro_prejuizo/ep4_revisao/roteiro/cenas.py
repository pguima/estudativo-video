# Roteiro — Descontos, Acréscimos, Lucro e Prejuízo, Episódio 4 de 4: Revisão geral, estratégia de prova, pegadinhas e treino
# Base: Estudos/Enem/estudos/01-matematica/15-descontos-acrescimos-lucro-prejuizo.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (Questões 1 a 9) nem a questão nova do ep2 (etiqueta de R$ 300,00). As 5 questões são INÉDITAS.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (o gancho só acrescenta, depois delas, o que a aula vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 TODA PORCENTAGEM TEM DONO · o preço de venda é uma PIZZA (a fatia do lucro nunca é a pizza inteira) ·
#     MARKUP em cima do custo × MARGEM dentro do preço ·
#   ep2 os CARIMBOS que se multiplicam · o desconto efetivo é a CONTA DO CAIXA · o PRÉDIO das faixas ·
#   ep3 a RÉGUA DO CUSTO · o CUSTO VALE 100.
#   (Os eps 1–3 foram escritos em paralelo: as frases vêm dos prompts e dos cabeçalhos dos cenas.py deles.)
# O que a prova cobra (seção 01): lucro e prejuízo em reais e em %, sobre o custo ou a venda · preço para uma margem ·
#   descontos e acréscimos encadeados · promoções traduzidas em desconto · descontos por faixa.
# Onde aparece (seção 10): Humanas (imposto embutido: % do preço final ou do preço sem imposto?) · gráficos (variação sobre
#   qual valor) · Matemática Financeira (à vista e "sem juros": séries de Empréstimos e de Comparação de propostas) ·
#   funções definidas por partes (faixas: série própria).
# Estratégia (seção 09): base ao lado de cada % · preço de 100 · desconfie da soma de % · confira em reais.
# V/F (os 9 erros da seção 11, com números NOSSOS; 6 falsas e 3 verdadeiras):
#   1 F (lucro de R$ 20 numa venda de R$ 100 = 25% da venda; é 20% da venda e 25% do custo) ·
#   2 V (custo R$ 90 com 25% sobre a venda → R$ 120: 90 ÷ 0,75; o erro daria 90 · 1,25 = 112,50) ·
#   3 F (20% e depois 10% = 30%; é 0,8 · 0,9 = 0,72 → 28%) ·
#   4 V (paguei R$ 72 depois de 20% → o preço era R$ 90: 72 ÷ 0,8; o erro daria 72 · 1,2 = 86,40) ·
#   5 F ("50% na segunda" = 50% de desconto; é 25% sobre o par) ·
#   6 F (faixas: a taxa mais alta vale para a compra inteira; cada faixa com a sua taxa) ·
#   7 F (duas peças a R$ 240 cada, +20% e −20% sobre o custo, empatam; custos 200 e 300 → 500 × 480: prejuízo de R$ 20) ·
#   8 F (lucro de 50% sobre o custo e imposto de 10% sobre a venda deixam 40%; custo 100 → venda 150 → imposto 15 →
#        sobra 135: 35% do custo) ·
#   9 V (margem sobre a venda nunca passa de 100%: o lucro é uma fatia do preço).
# QUESTÕES INÉDITAS (conferidas em trabalho/conferir_questoes.py: uma única correta; cada errada = um erro clássico):
#   Q1 (sacola) custo R$ 150, venda R$ 200, lucro sobre a VENDA → 50 ÷ 200 = 25% → B.
#      A ≈ 33,3% (dividiu pelo custo) · C 50% (leu R$ 50 como 50%) · D 75% (custo ÷ venda) · E ≈ 133% (venda ÷ custo).
#   Q2 (bolo no aplicativo) quer R$ 45 líquidos, o app fica com 25% do preço de venda → 45 ÷ 0,75 = R$ 60,00 → E.
#      A 56,25 (45 · 1,25: 25% sobre o custo) · B 70 (somou 25 reais) · C 33,75 (45 · 0,75) · D 180 (45 ÷ 0,25: dividiu
#      pela fatia do app). Conferência em reais: 25% de 60 = 15; 60 − 15 = 45.
#   Q3 (4 unidades de R$ 20,00) I "leve 4, pague 3" (paga 60: 25%) · II "segunda com 30%" (dois pares de 34 = 68: 15%) ·
#      III "20% em tudo" (64: 20%) → a I, 25% → C. A a II, 30% (leu 30% na segunda como 30% sobre tudo) ·
#      B a I, ≈ 33% (grátis ÷ pagas: 1 ÷ 3, base errada) · D a II, 60% (somou os 30% das duas segundas unidades) ·
#      E a I, 75% (leu a fração paga, 3/4, como desconto).
#   Q4 (prédio das faixas) nada até R$ 100 · 10% de 100 a 300 · 20% acima de 300 · compra de R$ 450 →
#      0 + 20 + 30 = 50 → paga R$ 400,00 → A. B 360 (20% sobre tudo) · C 315 (30% sobre tudo: somou as taxas) ·
#      D 420 (só a faixa mais alta) · E 380 (20% sobre tudo o que passa de 100).
#   Q5 (etiqueta remarcada) +80% sobre o custo e liquidação de 40% sobre a etiqueta → 1,8 · 0,6 = 1,08 → lucro de 8% sobre
#      o custo → D. A 40% (80 − 40) · B 48% (80 · 0,6: desconto só sobre a margem) · C 108% (leu o fator) ·
#      E prejuízo de 8% (achou que desconto grande dá prejuízo). Conferência: custo 100 → 180 → 108.
# Gabaritos: B, E, C, A, D.
# Checklist (seção 13, 13 itens) → episódio (como o prompt indica): bases, L = V − C, margem e formação de preço, imposto
#   e comissão: ep1 · fatores, preço original, promoções e faixas: ep2 · remarcações e lucro/prejuízo cruzados: ep3 ·
#   o último item (Taxas equivalentes) é a ponte.
# Meta (material): 20 questões, pelo menos 14 acertos (70%), misturando duas bases (lucro sobre o custo e imposto sobre a venda).
# Ponte (do usuário): Taxas equivalentes e inflação.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = ("Revisão de descontos, lucro e prejuízo: 9 pegadinhas e 5 questões estilo ENEM · Matemática ENEM, "
          "Descontos episódio 4")

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
    # ================= GANCHO (frases do usuário) =================
    dict(id="01", block="hook", text=
        "{a}Quase todo erro deste assunto [p=0.2] é a *conta certa* [p=0.2] feita sobre a *base errada.* [p=0.4] "
        "{b}Hoje você treina a única pergunta que importa: [p=0.3] {c}*porcentagem de quê?* [p=0.4] {d}Nove frases de "
        "verdadeiro ou falso [p=0.2] e cinco questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E o que a prova cobra? [p=0.4] {a}Lucro e prejuízo, [p=0.2] em reais e em porcentagem, [p=0.2] sobre o "
        "*custo* ou sobre a *venda.* [p=0.3] {b}O preço de venda para uma *margem.* [p=0.3] {c}Descontos e acréscimos "
        "*encadeados.* [p=0.3] {d}Promoções que precisam virar *desconto.* [p=0.3] {e}E descontos *por faixa.*"),

    # ================= ÍNDICE DA REVISÃO: OS 3 ÍCONES =================
    dict(id="03", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] vamos relembrar cada episódio. [p=0.4] {a}Um: [p=0.2] toda porcentagem *tem dono.* "
        "[p=0.3] O preço de venda é uma *pizza:* [p=0.2] a fatia do lucro [p=0.2] nunca é a pizza inteira. [p=0.3] O "
        "*markup* vai *em cima* do custo; [p=0.2] a *margem* fica *dentro* do preço. [p=0.4] {b}Dois: [p=0.2] cada desconto "
        "é um *carimbo,* [p=0.2] e carimbos se *multiplicam.* [p=0.3] O desconto efetivo é a *conta do caixa.* [p=0.2] E "
        "as faixas são os *andares de um prédio.*"),
    dict(id="04", block="indice", text=
        "{a}Três: [p=0.2] a *régua do custo.* [p=0.2] Comece no custo, [p=0.2] multiplique os fatores, [p=0.2] e veja se "
        "passou de um. [p=0.3] E, quando a questão só fala em porcentagem, [p=0.2] o *custo vale cem.*"),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="05", block="onde", text=
        "{t}E onde mais isso aparece? [p=0.4] {a}Em *Ciências Humanas:* [p=0.2] o imposto embutido no preço [p=0.2] é "
        "porcentagem do preço *final,* [p=0.2] ou do preço *sem* imposto? [p=0.3] {b}Nos *gráficos* de reportagem: "
        "[p=0.2] a variação foi calculada sobre *qual valor?* [p=0.3] {c}Na *Matemática Financeira:* [p=0.2] o desconto à "
        "vista [p=0.2] e o parcelado sem juros [p=0.2] voltam em Empréstimos [p=0.2] e em Comparação de propostas. [p=0.3] "
        "{d}E as faixas [p=0.2] são *funções definidas por partes,* [p=0.2] com série própria."),

    # ================= ESTRATÉGIA: 4 HÁBITOS (seção 09) =================
    dict(id="06", block="habitos", text=
        "{t}Na prova, [p=0.2] quatro hábitos. [p=0.4] {a}Um: [p=0.2] escreva a *base* ao lado de cada porcentagem. "
        "[p=0.2] Do custo, [p=0.2] da venda, [p=0.2] da etiqueta. [p=0.3] {b}Dois: [p=0.2] se só aparecem porcentagens, "
        "[p=0.2] trabalhe com um *preço de cem.* [p=0.3] {c}Três: [p=0.2] *desconfie da soma* de porcentagens de bases "
        "diferentes. [p=0.3] {d}Quatro: [p=0.2] no fim, [p=0.2] *confira em reais.*"),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="07", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="08", block="vf", text=
        "{t}Um: [p=0.2] vinte reais de lucro [p=0.2] numa venda de cem [p=0.2] são *vinte e cinco por cento da venda.* "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque vinte e cinco por cento aparece mesmo, [p=0.2] "
        "*do custo.* [p=0.3] {g}A porcentagem tem dono: [p=0.2] vinte dividido por *cem,* [p=0.2] *vinte por cento* da "
        "venda."),
    dict(id="09", block="vf", text=
        "{t}Dois: [p=0.2] custo de noventa reais, [p=0.2] margem de vinte e cinco por cento *sobre a venda:* [p=0.2] o "
        "preço é *cento e vinte.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque a mão vai "
        "direto para noventa vezes um vírgula vinte e cinco. [p=0.3] {g}Mas a margem é a fatia *dentro* da pizza: "
        "[p=0.2] noventa *dividido* por zero vírgula setenta e cinco."),
    dict(id="10", block="vf", text=
        "{t}Três: [p=0.2] vinte por cento de desconto, [p=0.2] e depois mais dez, [p=0.2] dão *trinta por cento.* "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque vinte mais dez dá trinta. [p=0.3] {g}Mas "
        "carimbos se *multiplicam:* [p=0.2] zero vírgula oito vezes zero vírgula nove, [p=0.2] *zero vírgula setenta e "
        "dois.* [p=0.2] Vinte e oito por cento."),
    dict(id="11", block="vf", text=
        "{t}Quatro: [p=0.2] paguei setenta e dois reais [p=0.2] depois de vinte por cento de desconto. [p=0.2] O preço "
        "era *noventa.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque muita gente devolve os "
        "vinte por cento [p=0.2] e acha oitenta e seis e quarenta. [p=0.3] {g}Para voltar, [p=0.2] *divida pelo fator:* "
        "[p=0.2] setenta e dois dividido por zero vírgula oito."),
    dict(id="12", block="vf", text=
        "{t}Cinco: [p=0.2] *segunda unidade com cinquenta por cento* [p=0.2] é um desconto de *cinquenta por cento.* "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o cartaz grita cinquenta. [p=0.3] {g}Faça a "
        "conta do caixa: [p=0.2] você leva duas [p=0.2] e paga uma e meia. [p=0.2] *Vinte e cinco por cento* no par."),
    dict(id="13", block="vf", text=
        "{t}Seis: [p=0.2] num desconto por faixas, [p=0.2] a taxa da faixa *mais alta* [p=0.2] vale para a compra "
        "*inteira.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque é assim que a gente fala: [p=0.2] "
        "\"comprei na faixa dos vinte\". [p=0.3] {g}No prédio, [p=0.2] cada andar tem a *sua* taxa. [p=0.2] Só a parte "
        "dentro da faixa recebe aquela taxa."),
    dict(id="14", block="vf", text=
        "{t}Sete: [p=0.2] duas peças vendidas por duzentos e quarenta reais cada, [p=0.2] uma com vinte por cento de "
        "lucro [p=0.2] e outra com vinte de prejuízo. [p=0.2] *Empatou.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] "
        "{e}Engana porque mais vinte e menos vinte parecem se anular. [p=0.3] {g}Mas os custos são *diferentes:* "
        "[p=0.2] duzentos e trezentos. [p=0.2] Pagou quinhentos, [p=0.2] recebeu quatrocentos e oitenta: [p=0.2] "
        "*prejuízo.*"),
    dict(id="15", block="vf", text=
        "{t}Oito: [p=0.2] lucro de cinquenta por cento sobre o custo, [p=0.2] e imposto de dez por cento sobre a venda. "
        "[p=0.2] Sobra lucro de *quarenta por cento.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque "
        "cinquenta menos dez dá quarenta. [p=0.3] {g}Mas as bases são diferentes: [p=0.2] *calcule em reais.* [p=0.2] "
        "Custo cem, [p=0.2] venda cento e cinquenta, [p=0.2] imposto quinze. [p=0.2] Sobra *trinta e cinco* por cento."),
    dict(id="16", block="vf", text=
        "{t}E nove: [p=0.2] uma margem sobre a *venda* [p=0.2] nunca passa de *cem por cento.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque markup de duzentos por cento existe. [p=0.3] {g}Mas "
        "markup vai em cima do custo. [p=0.2] A margem é uma fatia da pizza, [p=0.2] e a fatia *nunca* é a pizza "
        "inteira. [p=0.2] Viu mais de cem? [p=0.2] *Elimine.*"),
    dict(id="17", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] as cinco "
        "questões, [p=0.2] todas inéditas. [p=0.2] Em todas, [p=0.2] comece perguntando: [p=0.2] *de quê?*"),

    # ================= QUESTÃO 1: LUCRO SOBRE A VENDA =================
    dict(id="18", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Uma loja compra uma bolsa por *cento e cinquenta reais* [p=0.2] e vende por "
        "*duzentos.* [p=0.3] {b}O lucro, [p=0.2] em porcentagem *do preço de venda,* [p=0.2] é de [p=0.4] {la}A, "
        "[p=0.2] cerca de trinta e três vírgula três. [p=0.2] {lb}B, [p=0.2] vinte e cinco. [p=0.2] {lc}C, [p=0.2] "
        "cinquenta. [p=0.2] {ld}D, [p=0.2] setenta e cinco. [p=0.2] {le}E, [p=0.2] cerca de cento e trinta e três. "
        "[p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="19", block="q1", text=
        "{d}De quê? [p=0.2] *Da venda.* [p=0.3] {a}Lucro em reais: [p=0.2] duzentos menos cento e cinquenta, [p=0.2] "
        "*cinquenta.* [p=0.3] {b}Dividido pela venda: [p=0.2] cinquenta sobre duzentos, [p=0.2] *vinte e cinco por "
        "cento.* [p=0.2] {ok}*Letra B!* [p=0.4] {xa}A A dividiu pelo *custo.* [p=0.2] {xc}A C leu cinquenta reais como "
        "cinquenta por cento. [p=0.2] {xd}A D é custo sobre venda, [p=0.2] {xe}e a E, venda sobre custo."),

    # ================= QUESTÃO 2: PREÇO COM TAXA SOBRE A VENDA =================
    dict(id="20", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Uma doceira quer receber *quarenta e cinco reais* líquidos por bolo. [p=0.2] O "
        "aplicativo de entrega fica com *vinte e cinco por cento do preço de venda.* [p=0.3] {b}O bolo deve custar [p=0.4] "
        "{la}A, [p=0.2] cinquenta e seis e vinte e cinco. [p=0.2] {lb}B, [p=0.2] setenta. [p=0.2] {lc}C, [p=0.2] trinta e "
        "três e setenta e cinco. [p=0.2] {ld}D, [p=0.2] cento e oitenta. [p=0.2] {le}E, [p=0.2] sessenta reais. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="21", block="q2", text=
        "{d}De quê? [p=0.2] Do preço *de venda:* [p=0.2] a fatia do aplicativo está *dentro* da pizza. [p=0.3] {a}Sobram "
        "*setenta e cinco por cento* para a doceira. [p=0.3] {b}Quarenta e cinco *dividido* por zero vírgula setenta e "
        "cinco: [p=0.2] *sessenta reais.* [p=0.2] {ok}*Letra E!* [p=0.3] {v}Confira em reais: [p=0.2] vinte e cinco por "
        "cento de sessenta, [p=0.2] quinze. [p=0.2] Sessenta menos quinze, [p=0.2] quarenta e cinco. [p=0.4] {xa}A A "
        "multiplicou, [p=0.2] como se fosse sobre o custo. [p=0.2] {xb}A B somou vinte e cinco reais. [p=0.2] {xc}A C "
        "tirou a taxa dos quarenta e cinco, [p=0.2] {xd}e a D dividiu pela fatia do aplicativo."),

    # ================= QUESTÃO 3: COMPARAR PROMOÇÕES =================
    dict(id="22", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Você vai levar *quatro unidades* de um produto de *vinte reais.* [p=0.2] Promoção "
        "um: [p=0.2] *leve quatro, pague três.* [p=0.2] Promoção dois: [p=0.2] *segunda unidade com trinta por cento.* "
        "[p=0.2] Promoção três: [p=0.2] *vinte por cento em tudo.* [p=0.3] {b}O maior desconto efetivo é o da [p=0.4] "
        "{la}A, [p=0.2] dois, trinta por cento. [p=0.2] {lb}B, [p=0.2] um, cerca de trinta e três. [p=0.2] {lc}C, [p=0.2] "
        "um, vinte e cinco. [p=0.2] {ld}D, [p=0.2] dois, sessenta. [p=0.2] {le}E, [p=0.2] um, setenta e cinco. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="23", block="q3", text=
        "{d}A conta do caixa: [p=0.2] quanto você *paga* pelos oitenta reais que leva. [p=0.3] {a}Promoção um: [p=0.2] "
        "*sessenta.* [p=0.2] Vinte e cinco por cento. [p=0.3] {b}Promoção dois: [p=0.2] dois pares de trinta e quatro, "
        "[p=0.2] *sessenta e oito.* [p=0.2] Quinze por cento. [p=0.3] {c}Promoção três: [p=0.2] *sessenta e quatro.* "
        "[p=0.2] Vinte por cento. [p=0.2] {ok}*Letra C!* [p=0.4] {xa}A A leu trinta na segunda como trinta em tudo. "
        "[p=0.2] {xd}A D somou os dois trinta. [p=0.2] {xb}A B dividiu o grátis pelas *pagas,* [p=0.2] {xe}e a E leu "
        "três quartos como desconto."),

    # ================= QUESTÃO 4: DESCONTO POR FAIXA =================
    dict(id="24", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Uma loja dá desconto por faixa: [p=0.2] *nada* até cem reais, [p=0.2] *dez por "
        "cento* entre cem e trezentos, [p=0.2] e *vinte por cento* acima de trezentos. [p=0.3] {b}Numa compra de "
        "*quatrocentos e cinquenta reais,* [p=0.2] o cliente paga [p=0.4] {la}A, [p=0.2] quatrocentos. [p=0.2] {lb}B, "
        "[p=0.2] trezentos e sessenta. [p=0.2] {lc}C, [p=0.2] trezentos e quinze. [p=0.2] {ld}D, [p=0.2] quatrocentos e "
        "vinte. [p=0.2] {le}E, [p=0.2] trezentos e oitenta. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="25", block="q4", text=
        "{d}O prédio: [p=0.2] cada andar com a *sua* taxa. [p=0.3] {a}Os primeiros cem: [p=0.2] *zero.* [p=0.2] De cem a "
        "trezentos, [p=0.2] dez por cento de duzentos: [p=0.2] *vinte.* [p=0.3] {b}Acima de trezentos, [p=0.2] vinte por "
        "cento de cento e cinquenta: [p=0.2] *trinta.* [p=0.3] {c}Desconto de cinquenta. [p=0.2] Paga *quatrocentos.* "
        "[p=0.2] {ok}*Letra A!* [p=0.4] {xb}A B usou vinte por cento em tudo, [p=0.2] {xc}e a C, trinta: [p=0.2] somou "
        "as taxas. [p=0.2] {xd}A D só descontou o último andar, [p=0.2] {xe}e a E pôs vinte em tudo o que passa de cem."),

    # ================= QUESTÃO 5: REMARCAÇÃO E LIQUIDAÇÃO =================
    dict(id="26", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Uma loja põe na etiqueta *oitenta por cento sobre o custo.* [p=0.2] Na "
        "liquidação, [p=0.2] dá *quarenta por cento* de desconto sobre a etiqueta. [p=0.3] {b}Em relação ao custo, a loja "
        "teve [p=0.4] {la}A, [p=0.2] lucro de quarenta por cento. [p=0.2] {lb}B, [p=0.2] lucro de quarenta e oito. "
        "[p=0.2] {lc}C, [p=0.2] lucro de cento e oito. [p=0.2] {ld}D, [p=0.2] lucro de oito. [p=0.2] {le}E, [p=0.2] "
        "prejuízo de oito. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="27", block="q5", text=
        "{d}Só porcentagens? [p=0.2] O custo vale *cem.* [p=0.3] {a}Etiqueta: [p=0.2] cem vezes um vírgula oito, "
        "[p=0.2] *cento e oitenta.* [p=0.3] {b}Liquidação: [p=0.2] cento e oitenta vezes zero vírgula seis, [p=0.2] "
        "*cento e oito.* [p=0.3] {c}Na régua do custo, [p=0.2] passou de cem por *oito:* [p=0.2] lucro de oito por "
        "cento. [p=0.2] {ok}*Letra D!* [p=0.4] {xa}A A subtraiu as porcentagens. [p=0.2] {xb}A B descontou só a margem. "
        "[p=0.2] {xc}A C leu o fator, [p=0.2] {xe}e a E achou que desconto grande dá prejuízo."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="28", block="checklist", text=
        "{t}Agora, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* "
        "para outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}Bases, [p=0.2] lucro e prejuízo, [p=0.2] margem "
        "[p=0.2] e formação de preço: [p=0.2] episódio um. [p=0.3] {c}Fatores, [p=0.2] preço original, [p=0.2] promoções "
        "[p=0.2] e faixas: [p=0.2] episódio dois."),
    dict(id="29", block="checklist", text=
        "{a}Remarcações [p=0.2] e lucro e prejuízo cruzados: [p=0.2] episódio três. [p=0.4] {c}O que você *não* marcou, "
        "[p=0.2] reveja o episódio correspondente."),

    # ================= META =================
    dict(id="30", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *vinte questões* de lucro, prejuízo e descontos [p=0.2] {b}e acerte pelo menos "
        "*catorze,* [p=0.2] setenta por cento. [p=0.4] {c}Escolha questões que *misturem duas bases:* [p=0.2] lucro sobre "
        "o custo [p=0.2] e imposto sobre a venda, [p=0.2] por exemplo."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}O próximo assunto é *Taxas equivalentes e inflação:* [p=0.3] {b}por que dez por cento ao mês [p=0.2] *não* é "
        "cento e vinte por cento ao ano, [p=0.3] {c}e por que render dez por cento [p=0.2] num ano de inflação de dez por "
        "cento [p=0.3] {d}não deixa ninguém *mais rico.*"),
    dict(id="32", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual pegadinha te pegou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de descontos, lucro e prejuízo está completa. [p=0.2] Bons estudos, e *até a próxima aula* "
        "aqui no Estudativo. [p=1.5]"),
]
