# Roteiro — Comparação de Propostas e Tomada de Decisão, Episódio 5 de 5: Revisão geral, estratégia de prova, pegadinhas
#   e treino para o ENEM (e fechamento do bloco de Matemática Financeira) (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/18-comparacao-propostas-tomada-decisao.html — seções 01, 09, 10, 11 e 13
#   (e 08 só para "onde aparece"). NÃO usa as Questões 1–9 da seção 12 nem questões das séries 13–17.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS.
# Analogias âncora retomadas (uma frase cada, com o ícone do episódio, ANTES de cobrar):
#   ep1 a BANDEIRINHA DA DATA FOCAL (o ponto de encontro do câmbio entre datas) · a TAXA DE OPORTUNIDADE (o que o seu
#   dinheiro faria com você) · LOJA × APLICAÇÃO · ep2 o CRUZAMENTO DAS RETAS · a dívida do fixo paga aos pouquinhos ·
#   no EMPATE ninguém ganha · ep3 o que ENTRA NO BOLSO · o LEÃO do imposto morde só o rendimento · a TARIFA encolhe o
#   que você recebe · ep4 os TIJOLINHOS da margem de contribuição (o muro do custo fixo).
# Fechamento do bloco (seção 10): linha do tempo com os 6 assuntos acendendo + "trabalhe com fatores e respeite as datas".
# V/F (os 9 erros da seção 11, com números NOSSOS; 6 falsas e 3 verdadeiras; conferidos em trabalho/conferir_questoes.py):
#   1 F 5.000 hoje × 5.500 em 1 ano a 10%: "5.500 é melhor" (empatam: 5.500 ÷ 1,1 = 5.000) ·
#   2 V 8.000 hoje vale mais que 8.600 em 1 ano a 10% (8.000 · 1,1 = 8.800) · 3 F "mensalidade menor é sempre mais
#   barato" · 4 F A = 40 + 0,30x, B = 70 + 0,10x: equilíbrio 30 ÷ 0,30 = 100 (é 30 ÷ 0,20 = 150; as duas custam 85) ·
#   5 V empate em 37,5 km → a partir de 38 · 6 F 2.000 a 10% com 15% de IR: imposto 330 (é 15% de 200 = 30) ·
#   7 V 2% ao mês rende mais que 25% ao ano (1,02¹² ≈ 1,268) · 8 F 4.000 a 3% com tarifa de 80 no ato custa 3%
#   (recebe 3.920, paga 4.120: 200 ÷ 3.920 ≈ 5,1%) · 9 F fixo 3.000, custo 10, preço 25: 3.000 ÷ 25 = 120 (margem 15 → 200).
# QUESTÕES INÉDITAS (números e distratores do prompt; conferidas em trabalho/conferir_questoes.py). Gabaritos A, C, E, D, C.
#   Q1 1.940 à vista ou 2 × 1.000 (ato e 30 dias), dinheiro a 2% a.m., 1/1,02 ≈ 0,980 → parcelado hoje ≈ 1.980 > 1.940 →
#      à vista → A. Pela taxa: financiado 940, juros 60 → ≈ 6,4% > 2%. B "só R$ 60 a mais" (compara datas diferentes) ·
#      C decisão certa, taxa errada (60 ÷ 2.000 = 3%: o ato não viaja) · D "tanto faz" (sem conta) · E "parcelar, o dinheiro
#      rende 2%" (não compara com a taxa da loja).
#   Q2 LED 30 + 0,01h × comum 6 + 0,05h → empate 24 ÷ 0,04 = 600 h (as duas a R$ 36,00) → mínimo 601 h → C.
#      A 480 = 24 ÷ 0,05 · B 600 o próprio empate · D 900 = 36 ÷ 0,04 (somou os preços) · E 2.400 = 24 ÷ 0,01.
#      Teste (NOSSO): 601 h → LED 36,01 × comum 36,05.
#   Q3 A 1% a.m. com 20% de IR × B 10,5% a.a. isenta; 1,01¹² ≈ 1,127 → A 12,7% · 0,8 ≈ 10,2% líquidos → B → E.
#      A 12,7% (esqueceu o imposto) · B 12% (proporcional e sem imposto) · C "isenta sempre vence" (decisão certa,
#      motivo errado: generalização) · D "iguais" — NOSSA explicação (o prompt só dá a palavra): decidiu "no olho", sem
#      deixar as duas líquidas no mesmo período.
#   Q4 10.000 por 1 mês a 3%, tarifa 200 + seguro 100 no ato → recebe 9.700, paga 10.300 → 600 ÷ 9.700 ≈ 6,2% → D.
#      A 3% anunciado · B 3,1% = 300 ÷ 9.700 (esqueceu as cobranças no numerador) · C 6% = 600 ÷ 10.000 · E 9% = 3 + 6.
#   Q5 fixo 5.000, peça 12, preço 30 → margem 18 → 5.000 ÷ 18 ≈ 277,8 → 278 → C. A 167 = ÷ 30 (o preço) ·
#      B 277 arredondou para baixo (277 · 18 = 4.986: ainda prejuízo) · D 300 "arredondou para a centena" · E 417 = ÷ 12.
# Atalhos / conferências (verde, NOSSOS): ÷ 1,02 ≈ tirar 2% (Q1) · teste um valor acima do empate (Q2) · líquido =
#   bruto × 0,8 (Q3) · pago ÷ recebido, tire o 1 (Q4) · margem primeiro (Q5).
# Checklist (seção 13) → episódio: data focal, oportunidade, à vista × a prazo: ep1 · planos, equilíbrio, "a partir de":
#   ep2 · taxas no mesmo período, imposto, custo efetivo: ep3 · negócio e meta de lucro: ep4 · fatores e datas e o simulado:
#   o bloco (cada assunto na sua série).
# Meta (material): 20 questões, pelo menos 14 acertos (70%), priorizando planos com equilíbrio e à vista ou a prazo; e o
#   simulado de 20 questões do bloco inteiro.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = ("Revisão de comparação de propostas: 9 pegadinhas, 5 questões e o fechamento da Matemática Financeira · "
          "Matemática ENEM, episódio 5")

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
    "LED": "léd",
}

SCENES = [
    # ================= GANCHO (frase do usuário) =================
    dict(id="01", block="hook", text=
        "{a}O ENEM adora pôr você no lugar de *quem escolhe.* [p=0.4] {b}E a resposta quase nunca é o *mais barato:* "
        "[p=0.3] {c}é o mais barato *para aquele uso,* [p=0.2] *comparado na mesma data.*"),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}O que a prova cobra? [p=0.4] {a}Pagar *à vista* ou *parcelar.* [p=0.3] {b}Planos com parte *fixa* e parte "
        "*variável.* [p=0.3] {c}Aplicações com *imposto* e períodos diferentes. [p=0.3] {d}*Custos escondidos* num "
        "empréstimo. [p=0.3] {e}E o *ponto de equilíbrio* de um negócio."),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="03", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] uma frase por episódio. [p=0.4] {a}Um: [p=0.2] a *data focal* é o ponto de encontro "
        "do câmbio entre datas. [p=0.2] A *taxa de oportunidade* é o que o seu dinheiro faria com você. [p=0.4] {b}Dois: "
        "[p=0.2] o equilíbrio é o *cruzamento das retas.* [p=0.2] E no empate, [p=0.2] *ninguém ganha.*"),
    dict(id="04", block="indice", text=
        "{a}Três: [p=0.2] compare o que *entra no bolso.* [p=0.2] O leão do imposto morde *só o rendimento,* [p=0.2] e a "
        "tarifa no ato encolhe o que você recebe. [p=0.4] {b}E quatro: [p=0.2] cada venda deixa um *tijolinho* de margem,"
        " [p=0.2] até fechar o muro do custo fixo."),

    # ================= ONDE APARECE =================
    dict(id="05", block="onde", text=
        "{t}E onde isso aparece? [p=0.3] {a}Em *Função afim:* [p=0.2] os planos são retas. [p=0.3] {b}Em *Otimização e "
        "tomada de decisão,* [p=0.2] uma série futura. [p=0.3] {c}No dia a dia: [p=0.2] telefone, locadora, "
        "estacionamento, transporte. [p=0.3] {d}E *nem tudo é dinheiro:* [p=0.2] vale o critério do enunciado."),

    # ================= ESTRATÉGIA: 3 HÁBITOS (seção 09) =================
    dict(id="06", block="habitos", text=
        "{t}Na prova, três hábitos. [p=0.4] {a}Um: [p=0.2] *organize as propostas numa tabela.* [p=0.4] {b}Dois: "
        "[p=0.2] *iguale antes de comparar:* [p=0.2] mesma data, mesmo período, valor líquido. [p=0.4] {c}Três: [p=0.2] "
        "*teste um valor* acima do equilíbrio."),

    # ================= FECHANDO O BLOCO (seção 10) =================
    dict(id="07", block="bloco", text=
        "{t}E este é o *último assunto* de Matemática Financeira. [p=0.4] {a}*Crescimento:* [p=0.2] Juros simples [p=0.2]"
        " e Juros compostos. [p=0.3] {b}*Variações:* [p=0.2] Descontos e lucro. [p=0.3] {c}*Taxas:* [p=0.2] Taxas "
        "equivalentes e inflação. [p=0.3] {d}*Dívidas:* [p=0.2] Empréstimos. [p=0.3] {e}E *Decisões:* [p=0.2] este "
        "assunto."),
    dict(id="08", block="fatores", text=
        "{t}Uma ideia atravessa o bloco inteiro: [p=0.3] *trabalhe com fatores e respeite as datas.* [p=0.4] {a}Mais "
        "vinte por cento: [p=0.2] vezes um vírgula dois. [p=0.3] {b}Menos vinte: [p=0.2] vezes zero vírgula oito. [p=0.3]"
        " {c}Dois períodos a dez: [p=0.2] vezes um vírgula vinte e um. [p=0.3] {d}Tirar a inflação, [p=0.2] {e}ou trazer "
        "uma parcela para hoje: [p=0.2] *divida pelo fator.* [p=0.4] {f}Quase toda pegadinha nasce de *somar* o que se "
        "multiplica, [p=0.2] ou de misturar *datas.*"),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="09", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Pause e responda antes de mim."),
    dict(id="10", block="vf", text=
        "{t}Um: [p=0.2] com o dinheiro rendendo dez por cento ao ano, [p=0.2] receber cinco mil e quinhentos daqui a um ano "
        "[p=0.2] é *melhor* que cinco mil hoje. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque cinco mil "
        "e quinhentos é mais. [p=0.3] {g}Mas leve à mesma data: [p=0.2] cinco mil e quinhentos dividido por um vírgula "
        "um [p=0.2] dá *cinco mil.* [p=0.2] Empatam."),
    dict(id="11", block="vf", text=
        "{t}Dois: [p=0.2] na mesma taxa, [p=0.2] oito mil hoje valem *mais* que oito mil e seiscentos daqui a um ano. "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque oito mil e seiscentos é o maior "
        "número. [p=0.3] {g}Mas oito mil aplicados viram *oito mil e oitocentos.*"),
    dict(id="12", block="vf", text=
        "{t}Três: [p=0.2] o plano com a *mensalidade menor* [p=0.2] é sempre o mais barato. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque é o primeiro número que você vê. [p=0.3] {g}Mas depende do *uso.*"),
    dict(id="13", block="vf", text=
        "{t}Quatro: [p=0.2] plano A, [p=0.2] quarenta reais mais trinta centavos por minuto; [p=0.2] plano B, [p=0.2] "
        "setenta mais dez centavos. [p=0.2] Equilíbrio: [p=0.2] trinta dividido por zero vírgula três, [p=0.2] *cem "
        "minutos.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque trinta é mesmo a diferença dos fixos. "
        "[p=0.3] {g}Mas divida pela *diferença dos preços,* [p=0.2] vinte centavos: [p=0.2] *cento e cinquenta minutos.*"),
    dict(id="14", block="vf", text=
        "{t}Cinco: [p=0.2] se o empate é em trinta e sete vírgula cinco quilômetros, [p=0.2] o outro plano vale a pena *a"
        " partir de trinta e oito.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque vírgula "
        "cinco arredondaria para baixo. [p=0.3] {g}Mas *a partir de* é o inteiro *seguinte.*"),
    dict(id="15", block="vf", text=
        "{t}Seis: [p=0.2] dois mil reais rendem dez por cento, [p=0.2] com quinze por cento de imposto. [p=0.2] O imposto é "
        "de *trezentos e trinta.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque quinze por cento do "
        "total dá isso. [p=0.3] {g}Mas o leão morde só o *rendimento:* [p=0.2] quinze por cento de duzentos, [p=0.2] "
        "*trinta reais.*"),
    dict(id="16", block="vf", text=
        "{t}Sete: [p=0.2] *dois por cento ao mês* rende mais que vinte e cinco por cento ao ano. [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque dois vezes doze dá só vinte e quatro. [p=0.3] {g}Mas "
        "converta por *fator:* [p=0.2] um vírgula zero dois elevado a doze [p=0.2] dá quase *vinte e sete por cento.*"),
    dict(id="17", block="vf", text=
        "{t}Oito: [p=0.2] quatro mil emprestados a três por cento, [p=0.2] com oitenta reais de tarifa no ato. [p=0.2] O "
        "custo é *três por cento.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque três por cento é a taxa"
        " anunciada. [p=0.3] {g}Mas divida pelo que você *recebe:* [p=0.2] duzentos sobre três mil novecentos e vinte, "
        "[p=0.2] *cerca de cinco vírgula um por cento.*"),
    dict(id="18", block="vf", text=
        "{t}E nove: [p=0.2] custo fixo de três mil, [p=0.2] dez reais por unidade, [p=0.2] preço de vinte e cinco. "
        "[p=0.2] O equilíbrio é três mil dividido por vinte e cinco: [p=0.2] *cento e vinte.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque o preço é o que entra no caixa. [p=0.3] {g}Mas "
        "divida pela *margem,* [p=0.2] quinze: [p=0.2] *duzentas unidades.*"),
    dict(id="19", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas, [p=0.2] no estilo do ENEM. [p=0.2] Em todas, [p=0.2] *monte a tabela* antes da conta."),

    # ================= QUESTÃO 1: À VISTA OU A PRAZO =================
    dict(id="20", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Uma geladeira custa *mil novecentos e quarenta* à vista, [p=0.2] ou *duas parcelas de "
        "mil,* [p=0.2] uma no ato e outra em trinta dias. [p=0.2] O dinheiro do comprador rende *dois por cento* "
        "ao mês. [p=0.2] Considere um sobre um vírgula zero dois igual a zero vírgula nove oito. [p=0.3] "
        "{b}A melhor decisão é [p=0.4] {la}A, [p=0.2] à vista: [p=0.2] o parcelado vale hoje uns mil novecentos e "
        "oitenta. [p=0.2] {lb}B, [p=0.2] parcelar: [p=0.2] só sessenta a mais. [p=0.2] {lc}C, [p=0.2] à vista: [p=0.2] "
        "taxa de três por cento. [p=0.2] {ld}D, [p=0.2] tanto faz. [p=0.2] {le}E, [p=0.2] parcelar: [p=0.2] o dinheiro "
        "rende dois por cento. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="21", block="q1", text=
        "{d}A bandeirinha vai em *hoje.* [p=0.2] A parcela do ato não viaja. [p=0.3] {a}A outra, dividida por um vírgula "
        "zero dois, [p=0.2] vira *novecentos e oitenta.* [p=0.3] {b}Mil novecentos e oitenta, [p=0.2] contra mil "
        "novecentos e quarenta: [p=0.2] *à vista.* [p=0.2] {ok}*Letra A!* [p=0.3] {v}Pela taxa: [p=0.2] sessenta sobre "
        "novecentos e quarenta, [p=0.2] *seis vírgula quatro por cento,* [p=0.2] mais que os dois da aplicação. [p=0.4] "
        "{xb}A B comparou datas diferentes. [p=0.2] {xc}A C acertou a decisão, [p=0.2] mas dividiu por dois mil. [p=0.2] "
        "{xd}A D não fez conta, [p=0.2] {xe}e a E não comparou com a loja."),

    # ================= QUESTÃO 2: A LÂMPADA =================
    dict(id="22", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Uma lâmpada LED custa *trinta reais* [p=0.2] e gasta *um centavo* de energia por "
        "hora. [p=0.2] Uma comum custa *seis reais* [p=0.2] e gasta *cinco centavos* por hora. [p=0.3] {b}O número mínimo "
        "de horas inteiras de uso [p=0.2] para que a LED fique *mais barata* é [p=0.4] {la}A, [p=0.2] quatrocentas e "
        "oitenta. [p=0.2] {lb}B, [p=0.2] seiscentas. [p=0.2] {lc}C, [p=0.2] seiscentas e uma. [p=0.2] {ld}D, [p=0.2] "
        "novecentas. [p=0.2] {le}E, [p=0.2] duas mil e quatrocentas. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="23", block="q2", text=
        "{d}Diferença dos fixos: [p=0.2] *vinte e quatro reais.* [p=0.2] Diferença por hora: [p=0.2] *quatro centavos.* "
        "[p=0.3] {a}Vinte e quatro dividido por zero vírgula zero quatro: [p=0.2] *seiscentas horas,* [p=0.2] as duas a "
        "trinta e seis reais. [p=0.3] {b}No empate ninguém ganha: [p=0.2] *seiscentas e uma.* [p=0.2] {ok}*Letra C!* "
        "[p=0.3] {v}Teste: [p=0.2] a LED fica em trinta e seis e um centavo; [p=0.2] a comum, em trinta e seis e cinco. "
        "[p=0.4] {xb}A B parou no empate. [p=0.2] {xa}A A e a E {xe}dividiram por um preço só, [p=0.2] {xd}e a D somou os"
        " preços."),

    # ================= QUESTÃO 3: AS APLICAÇÕES =================
    dict(id="24", block="q3", text=
        "{t}Questão três. [p=0.3] {a}A aplicação A rende *um por cento ao mês,* [p=0.2] com *vinte por cento* de imposto "
        "sobre o rendimento. [p=0.2] A aplicação B rende *dez e meio por cento ao ano,* [p=0.2] *isenta.* [p=0.2] O prazo "
        "é de um ano. [p=0.2] Considere um vírgula zero um elevado a doze igual a um vírgula um dois sete. [p=0.3] "
        "{b}Rende mais [p=0.4] {la}A, [p=0.2] a A, com doze vírgula sete. [p=0.2] {lb}B, [p=0.2] a A, com doze. "
        "[p=0.2] {lc}C, [p=0.2] a B, porque isenta sempre vence. [p=0.2] {ld}D, [p=0.2] as duas rendem o mesmo. "
        "[p=0.2] {le}E, [p=0.2] a B, com dez e meio contra uns dez vírgula dois. "
        "[p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="25", block="q3", text=
        "{d}Iguale antes de comparar: [p=0.2] mesmo período, [p=0.2] e *líquido.* [p=0.3] {a}A em um ano: [p=0.2] *doze "
        "vírgula sete por cento* bruto. [p=0.3] {b}O leão leva vinte por cento do rendimento: [p=0.2] sobram uns *dez "
        "vírgula dois.* [p=0.2] Contra dez e meio: [p=0.2] *ganha a B.* [p=0.2] {ok}*Letra E!* [p=0.4] {xa}A A esqueceu o"
        " imposto. [p=0.2] {xb}A B usou a taxa proporcional. [p=0.2] {xc}A C acertou por um motivo falso: [p=0.2] isenta "
        "nem sempre vence. [p=0.2] {xd}E a D decidiu no olho, [p=0.2] sem igualar."),

    # ================= QUESTÃO 4: CUSTO EFETIVO =================
    dict(id="26", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Um empréstimo de *dez mil reais* por um mês, [p=0.2] a *três por cento,* [p=0.2] "
        "tem *tarifa de duzentos* [p=0.2] e *seguro de cem,* [p=0.2] descontados no ato. [p=0.3] {b}O custo efetivo é de "
        "cerca de [p=0.4] {la}A, [p=0.2] três por cento. [p=0.2] {lb}B, [p=0.2] três vírgula um. [p=0.2] {lc}C, [p=0.2] "
        "seis. [p=0.2] {ld}D, [p=0.2] seis vírgula dois. [p=0.2] {le}E, [p=0.2] nove por cento. [p=0.4] {p}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="27", block="q4", text=
        "{d}A tarifa encolhe o que você *recebe:* [p=0.2] dez mil menos trezentos, [p=0.2] *nove mil e setecentos.* "
        "[p=0.3] {a}Mas não encolhe o que você *paga:* [p=0.2] dez mil e trezentos. [p=0.3] {b}Custo: [p=0.2] seiscentos "
        "sobre nove mil e setecentos, [p=0.2] *cerca de seis vírgula dois por cento.* [p=0.2] {ok}*Letra D!* [p=0.4] "
        "{xa}A A acreditou no anúncio. [p=0.2] {xb}A B esqueceu as cobranças no numerador. [p=0.2] {xc}A C dividiu "
        "pelo contratado, [p=0.2] {xe}e a E somou as taxas."),

    # ================= QUESTÃO 5: LUCRO MÍNIMO =================
    dict(id="28", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Uma oficina tem custo fixo de *cinco mil reais* por mês. [p=0.2] Cada peça custa "
        "*doze reais* para ser feita [p=0.2] e é vendida por *trinta.* [p=0.3] {b}Para ter *lucro,* [p=0.2] o mínimo de "
        "peças vendidas no mês é [p=0.4] {la}A, [p=0.2] cento e sessenta e sete. [p=0.2] {lb}B, [p=0.2] duzentas e "
        "setenta e sete. [p=0.2] {lc}C, [p=0.2] duzentas e setenta e oito. [p=0.2] {ld}D, [p=0.2] trezentas. [p=0.2] "
        "{le}E, [p=0.2] quatrocentas e dezessete. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="29", block="q5", text=
        "{d}Margem primeiro: [p=0.2] trinta menos doze, [p=0.2] um tijolinho de *dezoito reais.* [p=0.3] {a}Cinco mil "
        "dividido por dezoito: [p=0.2] *duzentos e setenta e sete vírgula oito.* [p=0.3] {b}Com duzentas e setenta e sete, "
        "[p=0.2] o muro ainda não fechou. [p=0.2] Lucro, [p=0.2] *a partir de duzentas e setenta e oito.* [p=0.2] "
        "{ok}*Letra C!* [p=0.4] {xb}A B arredondou para baixo. [p=0.2] {xa}A A dividiu pelo preço; [p=0.2] {xe}a E, "
        "pelo custo da peça. [p=0.2] {xd}E a D arredondou para a centena."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="30", block="checklist", text=
        "{t}Agora, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* "
        "para outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}Data focal e à vista ou a prazo: [p=0.2] episódio um. "
        "[p=0.3] {c}Planos e o a partir de: [p=0.2] episódio dois."),
    dict(id="31", block="checklist", text=
        "{a}Aplicações e custo efetivo: [p=0.2] episódio três. [p=0.3] {b}Negócio e meta de lucro: [p=0.2] episódio "
        "quatro. [p=0.3] {c}Fatores e datas: [p=0.2] cada assunto na sua série. [p=0.4] {d}O que você *não* marcou, "
        "[p=0.2] reveja."),

    # ================= META =================
    dict(id="32", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *vinte questões* [p=0.2] {b}e acerte pelo menos *catorze,* [p=0.2] setenta por "
        "cento. [p=0.2] Priorize *planos* [p=0.2] e *à vista ou a prazo.* [p=0.4] {c}E, para fechar o bloco, [p=0.2] um "
        "*simulado de vinte questões* misturando todos os assuntos."),

    # ================= PONTE (frase do usuário) E CTA =================
    dict(id="33", block="ponte", text=
        "{a}Com isso fechamos a Matemática Financeira. [p=0.3] {b}O próximo assunto é *Expressões algébricas e produtos "
        "notáveis,* [p=0.2] que abre o bloco de Álgebra. [p=0.4] {c}Lembra do táxi com seis reais fixos [p=0.2] mais dois "
        "e cinquenta por quilômetro? [p=0.3] {d}Na álgebra, [p=0.2] isso vira *seis mais dois vírgula cinco xis:* "
        "[p=0.3] {e}letras no lugar de números [p=0.2] para escrever uma regra que vale para *qualquer distância.*"),
    dict(id="34", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual pegadinha te pegou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A Matemática Financeira está completa. [p=0.2] Bons estudos, e *até a próxima aula* "
        "aqui no Estudativo. [p=1.5]"),
]
