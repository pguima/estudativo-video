# Roteiro — Função Afim: gráfico, coeficientes e aplicações, Episódio 5 de 5: Revisão geral, estratégia de prova,
#   pegadinhas e treino (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/24-funcao-afim-grafico-coeficientes.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (as 9 questões do material). As 5 questões são INÉDITAS (marcadas na tela).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (o gancho só acrescenta, depois delas, o que a aula vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 a BANDEIRADA (b) e o TAXÍMETRO (a) · "você já viu isso DISFARÇADO" (proporção direta = b zero; juros simples)
#       · a BANDEIRADA NÃO DOBRA (ícone: o taxímetro) ·
#   ep2 Δy SOBRE Δx · o b é a FOTO NO INSTANTE ZERO · o zero é a HORA EM QUE ACABA (ícone: a vela) ·
#   ep3 a ESCADA da reta · DOIS PREGOS seguram a régua (ícone: a escada da reta) ·
#   ep4 LUCRO ZERO NÃO É LUCRO · QUEM LARGA NA FRENTE e QUEM GANHA NO FIM (ícone: o gráfico do equilíbrio).
#   O ep. 4 ainda estava em produção quando esta revisão foi escrita: as analogias dele vêm do prompt do vídeo 5.
# O que a prova cobra (seção 01): tarifas e planos · variação constante no tempo · custo, receita e lucro · leitura de
#   gráfico · proporcional ou não. O que mais rende: a = quanto muda por unidade; b = quanto vale quando x = 0.
# Onde aparece (seção 10): MU s = s0 + vt (a = velocidade) · MUV v = v0 + at (a aceleração é a taxa) · termometria
#   F = 1,8C + 32 · juros simples M = C + C·i·t (série de Juros Simples) · PA an = a1 + (n − 1)r (função afim nos naturais,
#   série própria). Equação da reta e coeficiente angular em Geometria Analítica: só a ponte.
# Estratégia (seção 09): ache b e a pelos nomes · desconfie da regra de três · atenção ao ponto de partida do tempo ·
#   confira a lei com um ponto conhecido.
# V/F (os 9 erros da seção 11, com números NOSSOS, sem as Q1–Q9; 6 falsas e 3 verdadeiras — as verdadeiras são as versões
#   CERTAS dos erros 2, 5 e 8):
#   1 F academia R$ 50 + R$ 80/mês: 3 meses = 290, então 6 meses = 580 (é 50 + 480 = 530) ·
#   2 V reta por (1, 5) e (3, 11): taxa = (11 − 5)/(3 − 1) = 3 ·
#   3 F tanque com 340 L às 2 h e 300 L às 4 h: valor inicial 340 L (taxa −20 L/h → b = 380 L) ·
#   4 F f(x) = 2x − 8 corta o eixo x em −8 (−8 é onde corta o eixo y; o zero é 8 ÷ 2 = 4) ·
#   5 V celular de R$ 2.000 que perde R$ 300 por ano: V(t) = 2 000 − 300t ·
#   6 F C = 900 + 6x, R = 10x: o lucro começa em 225 peças (225 é o equilíbrio, lucro zero; o lucro começa em 226) ·
#   7 F vela com 12 cm aos 20 min, perdendo 0,3 cm/min: acaba 40 min depois de acesa (acaba 40 min depois DAQUELE
#     instante: 60 min desde que foi acesa; b = 12 + 6 = 18 cm, 18 ÷ 0,3 = 60) ·
#   8 V reta que corta o eixo vertical em 4 e sobe 3 a cada 1 para a direita: y = 3x + 4 ·
#   9 F a reta que PARECE mais inclinada tem a maior taxa (com eixos em escalas diferentes, só Δy/Δx decide).
# QUESTÕES INÉDITAS (conferidas em trabalho/conferir_questoes.py: uma única correta; cada errada = um erro clássico; as
#   explicações das erradas são NOSSAS):
#   Q1 (tabela começa depois do zero; "quando acaba?") caixa d'água, t em horas desde que começou a esvaziar:
#      t = 2 → 1 560 L · t = 6 → 1 080 L · t = 10 → 600 L. Taxa −480/4 = −120 L/h; b = 1 560 + 2·120 = 1 800 L;
#      zero 1 800 ÷ 120 = 15 h → D. A 5 h (600 ÷ 120: contou a partir da última medição) · B 11 h (voltou o filme com o
#      sinal trocado: 1 560 − 240 = 1 320) · C 13 h (primeiro dado como b: 1 560 ÷ 120) · E 17 h (voltou 4 h em vez de 2:
#      1 560 + 480 = 2 040).
#   Q2 (regra de três com parte fixa) conta de água: taxa fixa R$ 30,00; 12 m³ → R$ 84,00; a = 54 ÷ 12 = R$ 4,50/m³;
#      24 m³ → 30 + 108 = R$ 138,00 → C. A 108 (esqueceu a taxa fixa) · B 114 (somou outra taxa fixa à conta antiga) ·
#      D 168 (regra de três: 2 · 84) · E 198 (regra de três e ainda somou a taxa fixa).
#   Q3 (lucro mínimo) confeitaria: custo fixo R$ 4.500,00/mês, R$ 18,00 por bolo, venda a R$ 30,00. L = 12x − 4 500;
#      equilíbrio 375 (lucro zero) → mínimo para lucro 376 → E. A 94 (somou 30 + 18: 4 500 ÷ 48 ≈ 93,75) · B 150 (dividiu
#      pelo preço, esqueceu o custo do bolo) · C 250 (dividiu pelo custo do bolo) · D 375 (o equilíbrio: lucro zero).
#   Q4 (gráfico com dois pontos) a reta passa por (1, 5) e (4, 11): a = 6/3 = 2; b = 5 − 2 = 3 → y = 2x + 3 → A.
#      B y = 3x + 2 (trocou a e b) · C y = 2x + 5 (primeiro dado como b) · D y = 0,5x + 4,5 (fração invertida, Δx/Δy) ·
#      E y = −2x + 7 (sinal errado). B, D e E passam pelo (1, 5): só o SEGUNDO ponto as elimina (dois pregos).
#   Q5 (dois planos, um por dois pontos) A: R$ 20 + R$ 0,50/min. B afim: 40 min → R$ 50; 100 min → R$ 74 →
#      a = 24/60 = R$ 0,40/min; b = 50 − 16 = R$ 34 → 20 + 0,5x = 34 + 0,4x → x = 140 (empate, R$ 90) → B mais barato a
#      partir de 141 min → D. A 28 (14 ÷ 0,5: dividiu pela taxa de A) · B 35 (14 ÷ 0,4: dividiu pela taxa de B) ·
#      C 140 (o empate) · E 300 (primeiro dado como b: fixo de B = 50).
# Gabaritos: D, C, E, A, D.
# Checklist (seção 13) → episódio (como o prompt pede): estrutura e proporcional × afim → ep1 · taxa, b, zero e
#   extrapolação → ep2 · gráfico e lei por dois pontos → ep3 · sinal, lucro e planos → ep4 · leis de outras áreas → esta
#   revisão.
# Meta (prompt e material): 30 questões, pelo menos 21 acertos (70%), com pelo menos dez em que a lei é montada a partir
#   de um gráfico ou de uma tabela.
# Ponte (do usuário): Função quadrática.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de função afim: 9 pegadinhas e 5 questões estilo ENEM · Matemática ENEM, Função afim episódio 5"

# Estilo da voz (gerar_voz_local.py): voz Neno, expressiva, sem acelerar
VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, numa aula de revisão animada, conversando "
            "de perto com um aluno que está treinando para o ENEM: voz calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas de verdadeiro ou falso com suspense, "
            "como num jogo; mostre surpresa nas pegadinhas; comemore os acertos com entusiasmo; dê ênfase forte às "
            "palavras-chave. Nas contas, fale devagar e com clareza, passo a passo. Ritmo didático e tranquilo, sem "
            "pressa, respeitando as pausas entre as frases. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, resumir nem repetir nada."),
)

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= GANCHO (frase do usuário) =================
    dict(id="01", block="hook", text=
        "{a}A função afim é a função *mais cobrada do ENEM.* [p=0.4] {b}E quase toda questão dela [p=0.2] vira uma "
        "*conta de uma linha* [p=0.2] quando você responde duas perguntas: [p=0.3] {c}*quanto vale no início* [p=0.2] "
        "e *quanto muda por unidade.* [p=0.4] {d}Hoje: [p=0.2] nove frases de verdadeiro ou falso [p=0.2] e cinco "
        "questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E o que a prova pede? [p=0.4] {a}*Tarifas e planos.* [p=0.3] {b}*Variação constante no tempo:* [p=0.2] a "
        "vela, o tanque. [p=0.3] {c}*Custo, receita e lucro.* [p=0.3] {d}*Leitura de gráfico.* [p=0.3] {e}E: [p=0.2] "
        "*é proporcional ou não?*"),
    dict(id="03", block="rende", text=
        "{t}E o que mais rende? [p=0.4] {a}Dar nome aos coeficientes. [p=0.3] {b}O *a* é *quanto muda por unidade:* "
        "[p=0.3] {c}O *bê* é *quanto vale quando xis é zero.* [p=0.4] {d}Pronto: [p=0.2] *uma linha* de conta."),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] relembre cada episódio. [p=0.4] {a}Um: [p=0.2] o *táxi.* [p=0.2] A *bandeirada* é "
        "o bê, [p=0.2] o *taxímetro* é o a. [p=0.2] Você já viu isso *disfarçado,* [p=0.2] na proporção e nos juros "
        "simples. [p=0.2] E a *bandeirada não dobra.* [p=0.4] {b}Dois: [p=0.2] a *vela.* [p=0.2] A taxa é *delta "
        "ípsilon sobre delta xis;* [p=0.2] o bê é a *foto no instante zero;* [p=0.2] e o zero é a *hora em que acaba.*"),
    dict(id="05", block="indice", text=
        "{a}Três: [p=0.2] a *escada da reta,* [p=0.2] e os *dois pregos* que seguram a régua. [p=0.4] {b}Quatro: "
        "[p=0.2] o gráfico do equilíbrio. [p=0.2] *Lucro zero não é lucro;* [p=0.2] e tem *quem larga na frente* "
        "[p=0.2] e *quem ganha no fim.*"),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="06", block="onde", text=
        "{t}E as outras provas? [p=0.4] {a}No *movimento uniforme,* [p=0.2] o a é a *velocidade.* [p=0.3] {b}No "
        "uniformemente variado, [p=0.2] a *aceleração* é a taxa. [p=0.3] {c}Na termometria, [p=0.2] éfe igual a um "
        "vírgula oito cê mais trinta e dois."),
    dict(id="07", block="onde", text=
        "{d}Nos *juros simples,* [p=0.2] o capital é o bê [p=0.2] e os juros do mês, o a. [p=0.3] {e}E a *progressão "
        "aritmética* [p=0.2] é uma função afim nos naturais, [p=0.2] com série própria. [p=0.4] {f}Em todas, [p=0.2] "
        "as mesmas duas perguntas."),

    # ================= ESTRATÉGIA: 4 HÁBITOS (seção 09) =================
    dict(id="08", block="habitos", text=
        "{t}E na hora da prova? [p=0.2] Quatro hábitos. [p=0.4] {a}Um: [p=0.2] *ache o bê e o a pelos nomes.* [p=0.2] "
        "\"Fixo\", \"inicial\": [p=0.2] é o bê. [p=0.2] \"Por quilômetro\", \"a cada hora\": [p=0.2] é o a. [p=0.3] "
        "{b}Dois: [p=0.2] *desconfie da regra de três.* [p=0.2] Tem parte fixa? [p=0.2] Ela está errada."),
    dict(id="09", block="habitos", text=
        "{c}Três: [p=0.2] *atenção ao ponto de partida do tempo.* [p=0.2] A tabela começa depois do zero? [p=0.2] "
        "Volte o filme. [p=0.3] {d}Quatro: [p=0.2] *confira a lei com um ponto conhecido.*"),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="10", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="11", block="vf", text=
        "{t}Um: [p=0.2] uma academia cobra cinquenta reais de matrícula [p=0.2] e oitenta por mês. [p=0.2] Três meses "
        "custam duzentos e noventa; [p=0.2] então seis meses custam *quinhentos e oitenta.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque a regra de três dobra tudo. [p=0.3] {g}Mas a *matrícula não dobra:* "
        "[p=0.2] cinquenta mais quatrocentos e oitenta, [p=0.2] *quinhentos e trinta.*"),
    dict(id="12", block="vf", text=
        "{t}Dois: [p=0.2] uma reta passa por um, cinco [p=0.2] e por três, onze. [p=0.2] A taxa é *onze menos cinco, "
        "sobre três menos um:* [p=0.2] três. [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque "
        "muita gente divide ao contrário. [p=0.3] {g}Mas a taxa é *delta ípsilon sobre delta xis:* [p=0.2] a saída "
        "fica em cima."),
    dict(id="13", block="vf", text=
        "{t}Três: [p=0.2] um tanque tem trezentos e quarenta litros às duas horas [p=0.2] e trezentos às quatro. "
        "[p=0.2] O valor inicial é *trezentos e quarenta.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana "
        "porque é o primeiro número da tabela. [p=0.3] {g}Mas o bê é a *foto no instante zero.* [p=0.2] Perde vinte "
        "por hora: [p=0.2] volte duas horas, [p=0.2] *trezentos e oitenta.*"),
    dict(id="14", block="vf", text=
        "{t}Quatro: [p=0.2] o gráfico de éfe de xis igual a dois xis menos oito [p=0.2] corta o eixo xis *no menos "
        "oito.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o menos oito é o número sozinho. "
        "[p=0.3] {g}Mas o bê é onde corta o eixo *ípsilon.* [p=0.2] O zero é *menos bê sobre a:* [p=0.2] oito dividido "
        "por dois, [p=0.2] *quatro.*"),
    dict(id="15", block="vf", text=
        "{t}Cinco: [p=0.2] um celular custou dois mil reais [p=0.2] e perde trezentos por ano. [p=0.2] A lei é *vê de "
        "tê igual a dois mil menos trezentos tê.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso "
        "porque a gente se acostumou com o *mais.* [p=0.3] {g}Mas o que *diminui* tem taxa negativa: [p=0.2] escreva o "
        "*menos* na lei."),
    dict(id="16", block="vf", text=
        "{t}Seis: [p=0.2] custo novecentos mais seis xis; [p=0.2] receita dez xis. [p=0.2] O lucro *começa* em "
        "duzentas e vinte e cinco peças. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque é o resultado "
        "da conta. [p=0.3] {g}Mas ali é o *equilíbrio:* [p=0.2] *lucro zero não é lucro.* [p=0.2] O lucro começa em "
        "*duzentos e vinte e seis.*"),
    dict(id="17", block="vf", text=
        "{t}Sete: [p=0.2] uma vela tem doze centímetros aos vinte minutos [p=0.2] e perde zero vírgula três por "
        "minuto. [p=0.2] Ela acaba *quarenta minutos depois de acesa.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] "
        "{e}Engana porque doze dividido por zero vírgula três dá quarenta. [p=0.3] {g}Mas são quarenta *depois daquele "
        "instante.* [p=0.2] Desde acesa, [p=0.2] *sessenta.*"),
    dict(id="18", block="vf", text=
        "{t}Oito: [p=0.2] uma reta corta o eixo vertical no quatro [p=0.2] e sobe três a cada um para a direita. "
        "[p=0.2] A lei é *ípsilon igual a três xis mais quatro.* [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] "
        "{e}Parece falso porque o quatro aparece primeiro. [p=0.3] {g}Mas *onde nasce* é o bê; [p=0.2] *quanto sobe "
        "por degrau* é o a."),
    dict(id="19", block="vf", text=
        "{t}E nove: [p=0.2] dois gráficos lado a lado. [p=0.2] A reta que *parece* mais inclinada [p=0.2] tem a *maior "
        "taxa.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o olho compara desenhos. [p=0.3] {g}Mas "
        "se os eixos têm *escalas diferentes,* [p=0.2] só a conta decide: [p=0.2] *delta ípsilon sobre delta xis.*"),
    dict(id="20", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas. [p=0.2] Em todas, [p=0.2] anote na margem: [p=0.2] *o início e a taxa.*"),

    # ================= QUESTÃO 1: TABELA QUE COMEÇA DEPOIS DO ZERO =================
    dict(id="21", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Uma caixa d'água começou a esvaziar a uma taxa constante. [p=0.2] Duas horas "
        "depois, tinha *mil quinhentos e sessenta litros;* [p=0.2] seis horas depois, *mil e oitenta;* [p=0.2] dez "
        "horas depois, *seiscentos.* [p=0.3] {b}Contando desde o início, [p=0.2] ela fica vazia depois de: [p=0.4] "
        "{la}A, [p=0.2] cinco horas. [p=0.2] {lb}B, [p=0.2] onze. [p=0.2] {lc}C, [p=0.2] treze. [p=0.2] {ld}D, [p=0.2] "
        "quinze. [p=0.2] {le}E, [p=0.2] dezessete. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q1", text=
        "{d}A taxa: [p=0.2] em quatro horas, [p=0.2] perdeu quatrocentos e oitenta litros. [p=0.2] *Menos cento e "
        "vinte litros por hora.* [p=0.3] {a}A tabela começa nas duas horas: [p=0.2] volte o filme. [p=0.2] Mil "
        "quinhentos e sessenta mais duzentos e quarenta: [p=0.2] *bê igual a mil e oitocentos.* [p=0.3] {b}O zero: "
        "[p=0.2] mil e oitocentos dividido por cento e vinte, [p=0.2] *quinze horas.* [p=0.2] {ok}*Letra D!* [p=0.2] "
        "{v}Confira: [p=0.2] às seis horas, [p=0.2] mil e oitenta. [p=0.4] {xc}A C tomou o primeiro dado como bê. "
        "[p=0.2] {xa}A A contou da *última* medição. [p=0.2] {xb}A B voltou com o *sinal trocado.* [p=0.2] {xe}E a E "
        "voltou quatro horas, [p=0.2] não duas."),

    # ================= QUESTÃO 2: A REGRA DE TRÊS COM PARTE FIXA =================
    dict(id="23", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}A conta de água tem uma *taxa fixa de trinta reais* [p=0.2] mais um valor por "
        "metro cúbico. [p=0.2] Num mês de *doze metros cúbicos,* [p=0.2] veio *oitenta e quatro reais.* [p=0.3] {b}Se "
        "o consumo *dobrar,* [p=0.2] a conta será de: [p=0.4] {la}A, [p=0.2] cento e oito reais. [p=0.2] {lb}B, "
        "[p=0.2] cento e catorze. [p=0.2] {lc}C, [p=0.2] cento e trinta e oito. [p=0.2] {ld}D, [p=0.2] cento e "
        "sessenta e oito. [p=0.2] {le}E, [p=0.2] cento e noventa e oito. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="24", block="q2", text=
        "{d}Tem parte fixa: [p=0.2] *nada de regra de três.* [p=0.3] {a}Tire o fixo: [p=0.2] oitenta e quatro menos "
        "trinta, [p=0.2] cinquenta e quatro, [p=0.2] em doze metros cúbicos. [p=0.2] *Quatro e cinquenta por metro "
        "cúbico.* [p=0.3] {b}Vinte e quatro metros cúbicos: [p=0.2] trinta mais cento e oito, [p=0.2] *cento e trinta "
        "e oito.* [p=0.2] {ok}*Letra C!* [p=0.4] {xd}A D é a regra de três: [p=0.2] dobrou a taxa fixa junto. [p=0.2] "
        "{xe}A E ainda somou mais trinta. [p=0.2] {xa}A A esqueceu a taxa fixa. [p=0.2] {xb}E a B somou outra taxa "
        "fixa à conta antiga."),

    # ================= QUESTÃO 3: O LUCRO MÍNIMO =================
    dict(id="25", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Uma confeitaria tem *custo fixo de quatro mil e quinhentos reais* por mês. "
        "[p=0.2] Cada bolo custa *dezoito* para fazer [p=0.2] e é vendido por *trinta.* [p=0.3] {b}O número mínimo de "
        "bolos por mês para ter *lucro* é: [p=0.4] {la}A, [p=0.2] noventa e quatro. [p=0.2] {lb}B, [p=0.2] cento e "
        "cinquenta. [p=0.2] {lc}C, [p=0.2] duzentos e cinquenta. [p=0.2] {ld}D, [p=0.2] trezentos e setenta e cinco. "
        "[p=0.2] {le}E, [p=0.2] trezentos e setenta e seis. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q3", text=
        "{d}Cada bolo deixa trinta menos dezoito: [p=0.2] *doze reais por bolo.* [p=0.3] {a}Lucro igual a doze xis "
        "menos quatro mil e quinhentos. [p=0.2] Zera em *trezentos e setenta e cinco.* [p=0.3] {b}Mas *lucro zero não "
        "é lucro.* [p=0.2] O primeiro com lucro: [p=0.2] *trezentos e setenta e seis.* [p=0.2] {ok}*Letra E!* [p=0.4] "
        "{xd}A D parou no equilíbrio. [p=0.2] {xb}A B dividiu pelo preço [p=0.2] {xc}e a C, pelo custo do bolo. "
        "[p=0.2] {xa}E a A *somou* os dois, [p=0.2] em vez de subtrair."),

    # ================= QUESTÃO 4: A LEI A PARTIR DO GRÁFICO =================
    dict(id="27", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}O gráfico de uma função afim [p=0.2] passa pelos pontos *um, cinco* [p=0.2] e "
        "*quatro, onze.* [p=0.3] {b}A lei da função é: [p=0.4] {la}A, [p=0.2] dois xis mais três. [p=0.2] {lb}B, "
        "[p=0.2] três xis mais dois. [p=0.2] {lc}C, [p=0.2] dois xis mais cinco. [p=0.2] {ld}D, [p=0.2] zero vírgula "
        "cinco xis mais quatro vírgula cinco. [p=0.2] {le}E, [p=0.2] menos dois xis mais sete. [p=0.4] {p}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="28", block="q4", text=
        "{d}A taxa: [p=0.2] onze menos cinco, [p=0.2] sobre quatro menos um. [p=0.2] *Seis sobre três, dois.* [p=0.3] "
        "{a}Desça um degrau a partir do um, cinco: [p=0.2] *bê igual a três.* [p=0.3] {b}Ípsilon igual a dois xis mais "
        "três. [p=0.2] {ok}*Letra A!* [p=0.2] {v}Confira o segundo prego: [p=0.2] dois vezes quatro mais três, [p=0.2] "
        "onze. [p=0.4] {xb}Pegadinha: [p=0.2] B, D e E *também passam pelo um, cinco.* [p=0.2] A B trocou a e bê; "
        "[p=0.2] {xd}a D inverteu a fração; [p=0.2] {xe}a E errou o sinal. [p=0.2] {xc}E a C tomou o cinco como bê."),

    # ================= QUESTÃO 5: DOIS PLANOS, UM POR DOIS PONTOS =================
    dict(id="29", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}O plano A cobra *vinte reais* mais *cinquenta centavos por minuto.* [p=0.2] "
        "No plano B, [p=0.2] *quarenta minutos custam cinquenta reais* [p=0.2] e *cem minutos, setenta e quatro.* "
        "[p=0.3] {b}O plano B fica mais barato a partir de quantos minutos inteiros? [p=0.4] {la}A, [p=0.2] vinte e "
        "oito. [p=0.2] {lb}B, [p=0.2] trinta e cinco. [p=0.2] {lc}C, [p=0.2] cento e quarenta. [p=0.2] {ld}D, [p=0.2] "
        "cento e quarenta e um. [p=0.2] {le}E, [p=0.2] trezentos. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="30", block="q5", text=
        "{d}A lei do B: [p=0.2] vinte e quatro reais em sessenta minutos: [p=0.2] *quarenta centavos por minuto.* "
        "[p=0.2] Fixo: [p=0.2] cinquenta menos dezesseis, [p=0.2] *trinta e quatro.* [p=0.3] {a}Iguale: [p=0.2] vinte "
        "mais zero vírgula cinco xis [p=0.2] igual a trinta e quatro mais zero vírgula quatro xis. [p=0.2] *Xis igual "
        "a cento e quarenta.* [p=0.3] {b}Ali, empate: [p=0.2] noventa reais nos dois. [p=0.2] Mais barato, [p=0.2] só "
        "no *cento e quarenta e um.* [p=0.2] {ok}*Letra D!* [p=0.4] {xc}A C parou no empate. [p=0.2] {xe}A E tomou o "
        "primeiro dado como fixo. [p=0.2] {xa}A A e {xb}a B dividiram por uma taxa só, [p=0.2] e não pela diferença."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="31", block="checklist", text=
        "{t}O checklist. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta,* [p=0.2] sem consultar "
        "nada. [p=0.4] {b}Estrutura e proporcional ou afim: [p=0.2] episódio um. [p=0.3] {c}Taxa, bê, zero e "
        "extrapolação: [p=0.2] episódio dois."),
    dict(id="32", block="checklist", text=
        "{a}Gráfico e lei por dois pontos: [p=0.2] episódio três. [p=0.3] {b}Sinal, lucro e planos: [p=0.2] episódio "
        "quatro. [p=0.3] {c}As leis de outras áreas: [p=0.2] esta revisão. [p=0.4] {d}O que você *não* marcou, [p=0.2] "
        "reveja o episódio correspondente."),

    # ================= META =================
    dict(id="33", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *trinta questões* [p=0.2] {b}e acerte pelo menos *vinte e uma,* [p=0.2] "
        "setenta por cento. [p=0.4] {c}E pelo menos *dez* em que você monta a lei [p=0.2] a partir de um *gráfico* ou "
        "de uma *tabela.*"),

    # ================= PONTE E CTA =================
    dict(id="34", block="ponte", text=
        "{a}O próximo assunto é *Função quadrática:* [p=0.2] vértice, raízes, máximo e mínimo, [p=0.3] {b}em que a "
        "taxa de variação *deixa de ser constante* [p=0.3] {c}e a reta *vira curva.*"),
    dict(id="35", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] {com}E me conte nos "
        "*comentários:* [p=0.2] qual pegadinha te pegou? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo "
        "tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] "
        "para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}A série de função afim está completa. [p=0.2] "
        "Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]

