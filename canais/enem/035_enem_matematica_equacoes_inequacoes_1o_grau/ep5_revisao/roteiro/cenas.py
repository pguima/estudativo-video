# Roteiro — Equações e Inequações do 1º Grau, Episódio 5 de 5: Revisão geral, estratégia de prova, pegadinhas e treino
#   (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/20-equacoes-inequacoes-1o-grau.html — seções 01, 09, 10, 11 e 13.
#   NÃO usa a seção 12 (as 9 questões do material). As 5 questões são INÉDITAS (marcadas na tela).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho e ponte: frases do usuário, IDÊNTICAS (o gancho só acrescenta, depois dela, o que a aula vai ter).
# Analogias âncora retomadas (com o ícone do episódio, ANTES de cobrar):
#   ep1 a BALANÇA equilibrada · "passa dividindo com o PRÓPRIO SINAL" · o traço da fração é um PARÊNTESE DISFARÇADO ·
#   ep2 a ETIQUETA do x · o TEMPO PASSA PARA TODOS · a RAIZ NÃO É A RESPOSTA ·
#   ep3 a reta no ESPELHO · bolinha aberta = PORTA FECHADA ·
#   ep4 a CORRIDA dos dois planos · NO EMPATE NINGUÉM É MAIS BARATO.
#   (O ep4 foi escrito em paralelo: as analogias dele vêm do prompt do vídeo 4 e do vídeo 5.)
# O que a prova cobra (seção 01): planos, frações de um total, médias e notas, misturas, isolar uma variável numa fórmula;
#   três hábitos: nomear a incógnita, inverter o sinal com negativo, ler o que a pergunta pede.
# Onde aparece (seção 10): Financeira 2 000(1 + 0,02t) = 2 480 → 1,24 = 1 + 0,02t → t = 12 meses (série de Juros
#   simples) · MUV 30 = 10 + 4t → t = 5 s · termometria 86 = 1,8C + 32 → C = 30 °C. Só "isolar a incógnita".
# Estratégia (seção 09): substituir as alternativas · conferir antes de marcar (na inequação, um número de dentro e um de
#   fora) · reler a pergunta depois de achar o x.
# V/F (os 9 erros da seção 11, com números nossos; 6 falsas e 3 verdadeiras — as verdadeiras são as versões CERTAS dos
#   erros 2, 7 e 9): 1 F −2x > −6 dá x > 3 (é x < 3) · 2 V −3(x − 4) = −3x + 12 · 3 F −(x − 4)/3 = (−x − 4)/3 (o menos
#   pega o numerador inteiro: −x + 4) · 4 F −2x = 10 → x = 5 (x = −5) · 5 F n > 800 → o menor inteiro é 800 (é 801) ·
#   6 F "daqui a 4 anos o pai terá o triplo do filho" → p + 4 = 3f (os dois ganham 4) · 7 V 1/3 + 1/4 = 7/12 · 8 F em 40 L
#   com 10 L de álcool, + 10 L de álcool dá 20/40 (é 20/50) · 9 V o valor de x costuma estar entre as alternativas como
#   armadilha.
# QUESTÕES INÉDITAS (conferidas em trabalho/conferir_questoes.py: uma única correta, conferida por substituição;
#   cada errada = um erro clássico; explicações das erradas são NOSSAS):
#   Q1 (locadora) A: R$ 80,00 + R$ 0,50/km · B: R$ 50,00 + R$ 0,80/km. 80 + 0,5k = 50 + 0,8k → 30 = 0,3k → k = 100 km
#      (R$ 130,00 nos dois); passeio de 150 km: A 155 × B 170 → A compensa → B. A "30 km · A" (parou no 30 = 0,3k) ·
#      C "100 km · B" (inverteu: depois do empate vence a menor tarifa por km) · D "130 km · B" (custo do empate tomado
#      como distância) · E "155 km · A" (custo de A no passeio tomado como distância).
#   Q2 (caixa d'água) 2 000 L, perde 70 L por hora; alarme quando tiver MENOS de 600 L; horas completas, no mínimo:
#      2 000 − 70t < 600 → −70t < −1 400 → t > 20 → 21 h → D. A 9 (600 ÷ 70: usou só o limite) · B 19 (não inverteu:
#      t < 20) · C 20 (o empate: 600 L ainda não é "menos de") · E 29 (2 000 ÷ 70: esvaziar a caixa). Teste: t = 21 → 530 L.
#   Q3 (idades) soma hoje 50; há 5 anos a mãe tinha o quádruplo da filha; idade ATUAL da mãe: f = filha hoje;
#      (50 − f) − 5 = 4(f − 5) → 45 − f = 4f − 20 → f = 13 → mãe 37 → C. A 13 (respondeu o x) · B 32 (a mãe há 5 anos) ·
#      D 40 (ignorou os 5 anos) · E 41 (tirou 5 anos só da mãe). Conferência: 32 = 4 · 8.
#   Q4 (nota) prova peso 1, nota 4,0; trabalho peso 2; média ≥ 6,0: (4 + 2T)/3 ≥ 6 → 2T ≥ 14 → T ≥ 7 → B. A 6,0 (a própria
#      média) · C 8,0 (média simples) · D 10,0 (trocou os pesos) · E 14,0 (esqueceu de dividir pelo peso 2).
#      Teste: 7 dá média 6 (serve); 6 dá 5,33 (não serve).
#   Q5 (Física, MUV) v = v₀ + at; de 12 m/s a 30 m/s com a = 1,5 m/s²: 30 = 12 + 1,5t → 18 = 1,5t → t = 12 s → A.
#      B 18 (parou na variação da velocidade) · C 20 (ignorou a velocidade inicial) · D 27 (multiplicou por 1,5) ·
#      E 28 (somou a velocidade inicial).
# Gabaritos: B, D, C, B, A.
# Checklist (seção 13) → episódio: resolver, parênteses, frações, 0x = k: ep1 · montar a equação, idades, misturas: ep2 ·
#   inequações, intervalos, menor inteiro: ep3 · ponto de equilíbrio: ep4 · conferir e reler: este episódio.
# Meta (prompt e material): 30 questões, pelo menos 21 acertos (70%), metade de comparação de planos e de inequações com
#   resposta inteira.
# Ponte (do usuário): Equação do 2º grau e fórmula de Bhaskara.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de equações e inequações do 1º grau: 9 pegadinhas e 5 questões estilo ENEM · Matemática ENEM, Álgebra episódio 5"

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
        "{a}No ENEM, [p=0.2] a equação do primeiro grau *quase nunca vem pronta.* [p=0.4] {b}Ela vem escondida num "
        "*plano de celular,* [p=0.2] numa *nota de escola* [p=0.2] ou numa *mistura.* [p=0.4] {c}Hoje você treina a "
        "*desmontar o disfarce.* [p=0.4] {d}Nove frases de verdadeiro ou falso [p=0.2] e cinco questões novas."),

    # ================= O QUE A PROVA COBRA (seção 01) =================
    dict(id="02", block="cobra", text=
        "{t}E onde a equação se esconde? [p=0.4] {a}Em *planos e tarifas:* [p=0.2] uma parte fixa mais uma parte por "
        "unidade. [p=0.3] {b}Em *frações de um total,* [p=0.2] como um salário. [p=0.3] {c}Em *médias e notas.* [p=0.3] "
        "{d}Em *misturas.* [p=0.3] {e}E em *fórmulas* de Física e de dinheiro, [p=0.2] em que você isola uma letra."),
    dict(id="03", block="tres", text=
        "{t}E três hábitos rendem mais que todos. [p=0.4] {a}Um: [p=0.2] *nomear a incógnita,* [p=0.2] com unidade. "
        "[p=0.3] {b}Dois: [p=0.2] *inverter o sinal* da desigualdade [p=0.2] quando multiplicar ou dividir por "
        "negativo. [p=0.3] {c}Três: [p=0.2] *ler o que a pergunta pede.* [p=0.2] Muitas vezes, [p=0.2] o xis não é a "
        "resposta."),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="04", block="indice", text=
        "{t}Antes, [p=0.2] relembre cada episódio. [p=0.4] {a}Um: [p=0.2] a equação é uma *balança equilibrada:* "
        "[p=0.2] faça a mesma coisa nos dois pratos. [p=0.3] O que multiplica [p=0.2] *passa dividindo, com o próprio "
        "sinal.* [p=0.2] E o traço da fração [p=0.2] é um *parêntese disfarçado.* [p=0.4] {b}Dois: [p=0.2] cole a "
        "*etiqueta do xis.* [p=0.2] Nas idades, [p=0.2] *o tempo passa para todos.* [p=0.2] E a *raiz não é a resposta.*"),
    dict(id="05", block="indice", text=
        "{a}Três: [p=0.2] multiplicar por negativo [p=0.2] é olhar a reta *no espelho:* [p=0.2] o sinal vira. [p=0.3] E a "
        "bolinha aberta [p=0.2] é *porta fechada.* [p=0.4] {b}Quatro: [p=0.2] a *corrida dos dois planos.* [p=0.2] E *no "
        "empate, ninguém é mais barato.*"),

    # ================= ONDE APARECE (seção 10) =================
    dict(id="06", block="onde", text=
        "{t}E isso aparece fora da Álgebra? [p=0.4] {a}Na *Matemática Financeira:* [p=0.2] dois mil reais a dois por "
        "cento ao mês [p=0.2] viram dois mil quatrocentos e oitenta. [p=0.2] Um vírgula vinte e quatro [p=0.2] é igual a "
        "um mais zero vírgula zero dois tê. [p=0.2] *Doze meses.* [p=0.2] Tem série própria, a de Juros simples."),
    dict(id="07", block="onde", text=
        "{b}Na *Física,* [p=0.2] de dez para trinta metros por segundo, [p=0.2] acelerando quatro: [p=0.2] trinta igual a "
        "dez mais quatro tê. [p=0.2] *Cinco segundos.* [p=0.3] {c}E no termômetro: [p=0.2] oitenta e seis graus "
        "Fahrenheit [p=0.2] dão *trinta graus Celsius.* [p=0.4] {d}Em todas, [p=0.2] a fórmula é uma equação do primeiro "
        "grau. [p=0.2] É só *isolar a incógnita.*"),

    # ================= ESTRATÉGIA: 3 HÁBITOS (seção 09) =================
    dict(id="08", block="habitos", text=
        "{t}Na prova, [p=0.2] mais três hábitos. [p=0.4] {a}Um: [p=0.2] montagem confusa? [p=0.2] *Substitua as "
        "alternativas* no enunciado. [p=0.3] {b}Dois: [p=0.2] *confira antes de marcar.* [p=0.2] Na inequação, [p=0.2] "
        "teste um número *de dentro* [p=0.2] e um *de fora.* [p=0.3] {c}Três: [p=0.2] achou o xis? [p=0.2] *Releia a "
        "pergunta.*"),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="09", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="10", block="vf", text=
        "{t}Um: [p=0.2] menos dois xis maior que menos seis [p=0.2] dá *xis maior que três.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque a conta do número está certa. [p=0.3] {g}Mas dividiu por *negativo:* "
        "[p=0.2] a reta vai *para o espelho* e o sinal vira. [p=0.2] *Xis menor que três.*"),
    dict(id="11", block="vf", text=
        "{t}Dois: [p=0.2] menos três, vezes xis menos quatro, [p=0.2] é igual a *menos três xis mais doze.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque muita gente escreve *menos doze.* [p=0.3] "
        "{g}Mas *menos vezes menos dá mais.* [p=0.2] O menos três multiplica os *dois* termos."),
    dict(id="12", block="vf", text=
        "{t}Três: [p=0.2] menos, xis menos quatro sobre três, [p=0.2] é igual a *menos xis menos quatro,* sobre três. "
        "[p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o quatro parece longe do menos. [p=0.3] {g}Mas o "
        "traço da fração é um *parêntese disfarçado.* [p=0.2] O menos pega o numerador inteiro: [p=0.2] *menos xis mais "
        "quatro.*"),
    dict(id="13", block="vf", text=
        "{t}Quatro: [p=0.2] menos dois xis igual a dez [p=0.2] dá *xis igual a cinco.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Falso!* [p=0.3] {e}Engana porque dez dividido por dois é cinco. [p=0.3] {g}Mas o menos dois *passa dividindo "
        "com o próprio sinal.* [p=0.2] *Xis igual a menos cinco.*"),
    dict(id="14", block="vf", text=
        "{t}Cinco: [p=0.2] se ene é maior que oitocentos, [p=0.2] o menor inteiro é *oitocentos.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o oitocentos é o número que apareceu na conta. [p=0.3] {g}Mas "
        "*maior que* é estrito: [p=0.2] porta fechada no oitocentos. [p=0.2] *Oitocentos e um.*"),
    dict(id="15", block="vf", text=
        "{t}Seis: [p=0.2] \"daqui a quatro anos, o pai terá o triplo da idade do filho\" [p=0.2] vira *pê mais quatro "
        "igual a três efe.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o pai é quem aparece "
        "primeiro. [p=0.3] {g}Mas *o tempo passa para todos.* [p=0.2] Pê mais quatro [p=0.2] igual a três vezes *efe "
        "mais quatro.*"),
    dict(id="16", block="vf", text=
        "{t}Sete: [p=0.2] um terço mais um quarto [p=0.2] é igual a *sete doze avos.* [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Verdadeiro!* [p=0.3] {e}Parece falso porque a tentação é somar em cima e embaixo: [p=0.2] dois sétimos. "
        "[p=0.3] {g}Mas frações se somam pelo *MMC:* [p=0.2] quatro doze avos mais três doze avos."),
    dict(id="17", block="vf", text=
        "{t}Oito: [p=0.2] um tanque tem quarenta litros, [p=0.2] dez de álcool. [p=0.2] Pondo mais dez litros de álcool, "
        "[p=0.2] a concentração fica *vinte sobre quarenta.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana "
        "porque a gente só lembra do álcool que entrou. [p=0.3] {g}Mas o *volume total também cresce:* [p=0.2] *vinte "
        "sobre cinquenta.*"),
    dict(id="18", block="vf", text=
        "{t}E nove: [p=0.2] o valor do xis [p=0.2] costuma aparecer nas alternativas *como armadilha.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque achar o xis dá sensação de missão cumprida. [p=0.3] "
        "{g}Mas *a raiz não é a resposta:* [p=0.2] releia a pergunta."),
    dict(id="19", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] cinco "
        "questões inéditas. [p=0.2] Em todas, [p=0.2] *cole a etiqueta do xis* [p=0.2] e confira no final."),

    # ================= QUESTÃO 1: PONTO DE EQUILÍBRIO (LOCADORA) =================
    dict(id="20", block="q1", text=
        "{t}Questão um. [p=0.3] {a}Uma locadora tem dois planos por dia. [p=0.2] Plano A: [p=0.2] *oitenta reais* mais "
        "*cinquenta centavos* por quilômetro. [p=0.2] Plano B: [p=0.2] *cinquenta reais* mais *oitenta centavos* por "
        "quilômetro. [p=0.3] {b}Os planos empatam em quantos quilômetros, [p=0.2] e qual compensa num passeio de *cento e "
        "cinquenta?* [p=0.4] {la}A, [p=0.2] trinta, e o A. [p=0.2] {lb}B, [p=0.2] cem, e o A. [p=0.2] {lc}C, [p=0.2] cem, "
        "e o B. [p=0.2] {ld}D, [p=0.2] cento e trinta, e o B. [p=0.2] {le}E, [p=0.2] cento e cinquenta e cinco, e o A. "
        "[p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="21", block="q1", text=
        "{d}Etiqueta: [p=0.2] *ká é a distância, em quilômetros.* [p=0.3] {a}Iguale os planos: [p=0.2] oitenta mais "
        "meio ká [p=0.2] igual a cinquenta mais zero vírgula oito ká. [p=0.3] {b}Trinta igual a zero vírgula três ká: "
        "[p=0.2] *ká igual a cem.* [p=0.2] Os dois custam cento e trinta. [p=0.3] {c}Com cento e cinquenta: [p=0.2] A "
        "custa cento e cinquenta e cinco, [p=0.2] B custa cento e setenta. [p=0.2] {ok}*Letra B!* [p=0.4] {xa}A A parou no "
        "trinta. [p=0.2] {xc}A C inverteu: [p=0.2] depois do empate, vence a *menor tarifa por quilômetro.* [p=0.2] "
        "{xd}A D e {xe}a E deram um *preço* no lugar da distância."),

    # ================= QUESTÃO 2: "A PARTIR DE QUANTAS" (CAIXA D'ÁGUA) =================
    dict(id="22", block="q2", text=
        "{t}Questão dois. [p=0.3] {a}Uma caixa d'água tem *dois mil litros* [p=0.2] e perde *setenta litros por hora.* "
        "[p=0.2] Um alarme toca quando ela tiver *menos de seiscentos litros.* [p=0.3] {b}Depois de quantas horas "
        "completas, no mínimo, [p=0.2] o alarme já estará tocando? [p=0.4] {la}A, [p=0.2] nove. [p=0.2] {lb}B, [p=0.2] "
        "dezenove. [p=0.2] {lc}C, [p=0.2] vinte. [p=0.2] {ld}D, [p=0.2] vinte e um. [p=0.2] {le}E, [p=0.2] vinte e nove. "
        "[p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="23", block="q2", text=
        "{d}Etiqueta: [p=0.2] *tê é o tempo, em horas.* [p=0.3] {a}Dois mil menos setenta tê [p=0.2] *menor que* "
        "seiscentos. [p=0.3] {b}Menos setenta tê, menor que menos mil e quatrocentos. [p=0.2] Divido por negativo: "
        "[p=0.2] *o sinal vira.* [p=0.2] Tê maior que vinte. [p=0.3] {c}Em vinte horas, [p=0.2] ficam seiscentos: "
        "[p=0.2] *ainda não é menos de.* [p=0.2] {ok}*Vinte e uma. Letra D!* [p=0.3] {v}Confira: [p=0.2] em vinte e uma "
        "horas, [p=0.2] quinhentos e trinta litros. [p=0.4] {xb}A B não inverteu o sinal. [p=0.2] {xc}A C parou no "
        "empate. [p=0.2] {xa}A A usou só os seiscentos, [p=0.2] {xe}e a E esvaziou a caixa."),

    # ================= QUESTÃO 3: IDADES ("HÁ 5 ANOS") =================
    dict(id="24", block="q3", text=
        "{t}Questão três. [p=0.3] {a}Hoje, [p=0.2] a soma das idades de uma mãe e de sua filha é *cinquenta anos.* "
        "[p=0.2] *Há cinco anos,* [p=0.2] a mãe tinha o *quádruplo* da idade da filha. [p=0.3] {b}Hoje, [p=0.2] a idade da "
        "*mãe* é [p=0.4] {la}A, [p=0.2] treze anos. [p=0.2] {lb}B, [p=0.2] trinta e dois. [p=0.2] {lc}C, [p=0.2] trinta e "
        "sete. [p=0.2] {ld}D, [p=0.2] quarenta. [p=0.2] {le}E, [p=0.2] quarenta e um. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="25", block="q3", text=
        "{d}Etiqueta: [p=0.2] *efe é a idade da filha hoje.* [p=0.2] A mãe tem cinquenta menos efe. [p=0.3] {a}Há cinco "
        "anos, [p=0.2] *as duas* tinham cinco a menos. [p=0.2] Quarenta e cinco menos efe [p=0.2] igual a quatro vezes efe "
        "menos cinco. [p=0.3] {b}Sessenta e cinco igual a cinco efe: [p=0.2] *a filha tem treze.* [p=0.3] {c}Mas a "
        "pergunta é a *mãe:* [p=0.2] trinta e sete. [p=0.2] {ok}*Letra C!* [p=0.3] {v}Há cinco anos: [p=0.2] trinta e "
        "dois e oito. [p=0.2] Fecha. [p=0.4] {xa}A A respondeu o xis. [p=0.2] {xb}A B deu a mãe de cinco anos atrás. "
        "[p=0.2] {xd}A D ignorou os cinco anos, [p=0.2] {xe}e a E tirou cinco anos *só da mãe.*"),

    # ================= QUESTÃO 4: NOTA MÍNIMA (MÉDIA PONDERADA) =================
    dict(id="26", block="q4", text=
        "{t}Questão quatro. [p=0.3] {a}Numa escola, [p=0.2] a prova tem *peso um* [p=0.2] e o trabalho tem *peso dois.* "
        "[p=0.2] Para passar, [p=0.2] a média tem que ser *no mínimo seis.* [p=0.2] Um aluno tirou *quatro* na prova. "
        "[p=0.3] {b}A menor nota que ele precisa no trabalho é [p=0.4] {la}A, [p=0.2] seis. [p=0.2] {lb}B, [p=0.2] sete. "
        "[p=0.2] {lc}C, [p=0.2] oito. [p=0.2] {ld}D, [p=0.2] dez. [p=0.2] {le}E, [p=0.2] catorze. [p=0.4] {p}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="27", block="q4", text=
        "{d}Etiqueta: [p=0.2] *tê é a nota do trabalho.* [p=0.3] {a}Média ponderada: [p=0.2] cada nota vezes o seu peso, "
        "[p=0.2] dividido pela soma dos pesos. [p=0.2] Quatro mais dois tê, [p=0.2] sobre três, [p=0.2] maior ou igual a "
        "seis. [p=0.3] {b}Quatro mais dois tê, maior ou igual a dezoito. [p=0.2] Dois tê, maior ou igual a catorze: "
        "[p=0.2] *tê maior ou igual a sete.* [p=0.2] {ok}*Letra B!* [p=0.3] {v}Com sete, [p=0.2] a média é seis: "
        "[p=0.2] passa. [p=0.4] {xc}A C fez média simples. [p=0.2] {xd}A D trocou os pesos. [p=0.2] {xe}A E esqueceu de "
        "dividir por dois, [p=0.2] {xa}e a A achou que bastava tirar a própria média."),

    # ================= QUESTÃO 5: ISOLAR A INCÓGNITA (FÍSICA) =================
    dict(id="28", block="q5", text=
        "{t}E a questão cinco. [p=0.3] {a}Na Física, [p=0.2] a velocidade é *vê igual a vê zero mais a tê.* [p=0.2] Um "
        "carro está a *doze metros por segundo* [p=0.2] e acelera *um vírgula cinco* metro por segundo, a cada segundo, "
        "[p=0.2] até chegar a *trinta.* [p=0.3] {b}O tempo, em segundos, é [p=0.4] {la}A, [p=0.2] doze. [p=0.2] {lb}B, "
        "[p=0.2] dezoito. [p=0.2] {lc}C, [p=0.2] vinte. [p=0.2] {ld}D, [p=0.2] vinte e sete. [p=0.2] {le}E, [p=0.2] vinte "
        "e oito. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="29", block="q5", text=
        "{d}É só *isolar o tê.* [p=0.3] {a}Trinta igual a doze mais um vírgula cinco tê. [p=0.3] {b}O doze passa "
        "subtraindo: [p=0.2] dezoito igual a um vírgula cinco tê. [p=0.2] O um vírgula cinco passa dividindo: [p=0.2] "
        "*tê igual a doze.* [p=0.2] {ok}*Letra A!* [p=0.3] {v}Confira: [p=0.2] doze mais dezoito, [p=0.2] trinta. "
        "[p=0.4] {xb}A B parou no dezoito. [p=0.2] {xc}A C esqueceu a velocidade inicial. [p=0.2] {xd}A D multiplicou, "
        "[p=0.2] {xe}e a E somou o doze."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="30", block="checklist", text=
        "{t}O checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* "
        "para outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}Resolver, [p=0.2] parênteses, [p=0.2] frações "
        "[p=0.2] e o zero xis: [p=0.2] episódio um. [p=0.3] {c}Montar a equação, [p=0.2] idades [p=0.2] e misturas: "
        "[p=0.2] episódio dois."),
    dict(id="31", block="checklist", text=
        "{a}Inequações, [p=0.2] intervalos [p=0.2] e o menor inteiro: [p=0.2] episódio três. [p=0.3] {b}Ponto de "
        "equilíbrio: [p=0.2] episódio quatro. [p=0.3] {c}E conferir e reler: [p=0.2] *este* episódio. [p=0.4] {d}O que "
        "você *não* marcou, [p=0.2] reveja o episódio correspondente."),

    # ================= META =================
    dict(id="32", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *trinta questões* [p=0.2] {b}e acerte pelo menos *vinte e uma,* [p=0.2] setenta "
        "por cento. [p=0.4] {c}E metade delas [p=0.2] de *comparação de planos* [p=0.2] e de *inequações com resposta "
        "inteira.*"),

    # ================= PONTE E CTA =================
    dict(id="33", block="ponte", text=
        "{a}O próximo assunto é *Equação do segundo grau e fórmula de Bhaskara,* [p=0.3] {b}quando o xis aparece *ao "
        "quadrado* [p=0.2] e a equação pode ter *duas respostas.*"),
    dict(id="34", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual pegadinha te pegou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de equações e inequações do primeiro grau está completa. [p=0.2] Bons estudos, e *até a próxima aula* "
        "aqui no Estudativo. [p=1.5]"),
]
