# Roteiro — Unidades de Medida e Conversões, Episódio 5 de 5: Revisão geral, pegadinhas e treino para o ENEM (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/10-unidades-conversoes.html — seções 01, 11 e 13.
#   NÃO usa a seção 12 (as 9 questões do material). As 5 questões são INÉDITAS (marcadas na tela).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Gancho: frase do usuário, IDÊNTICA (só acrescenta, depois dela, o que a aula vai ter).
# Analogias âncora retomadas (uma frase cada, com o ícone do episódio, ANTES de cobrar):
#   ep1 a ESCADA de 7 degraus e "unidade menor, número maior" · ep2 área = GRADE 10 × 10, volume = CUBO 10 × 10 × 10,
#   o litro = a CAIXA DE LEITE (enche um cubo de 10 cm), 1 L de água = 1 kg · ep3 o RELÓGIO de 60 em 60 e a unidade
#   composta = fração de DOIS ANDARES · ep4 frações que VALEM 1 e unidades RISCADAS (o que sobra é a resposta).
#   (O ep4 ainda não tinha cenas.py quando este foi escrito: frases tiradas do PLANO_DA_SERIE.md e do prompt.)
# Os três fatos (seção 01): área × 100 e volume × 1 000 por degrau · 1 L = 1 dm³ · o tempo não é decimal.
# Treino-relâmpago (6 conversões, sem repetir exemplos dos eps 1–4):
#   2 m² = 20 000 cm² · 0,3 m³ = 300 dm³ · 2 500 cm³ = 2,5 L · 4 m³ = 4 000 L · 1,2 h = 1 h 12 min · 0,6 h = 36 min.
# V/F (os 9 erros da seção 11; 6 falsas e 3 verdadeiras):
#   1 F (1 m² = 100 cm²; são 10 000) · 2 V (1 m³ = 1 000 000 cm³) · 3 F (1 m³ = 1 litro; são 1 000) ·
#   4 F (2,4 h = 2 h 40; é 2 h 24) · 5 V (km/h → m/s divide por 3,6) · 6 F (1 t = 100 kg; é 1 000) ·
#   7 V (1 ha = 10 000 m²) · 8 F (1,5 kg + 300 g = 301,5; padronize: 1 800 g) ·
#   9 F (g/cm³ → kg/m³ convertendo só o grama; converta os dois: 1,2 g/cm³ = 1 200 kg/m³).
# QUESTÕES INÉDITAS (conferidas em trabalho/conferir_questoes.py: uma única correta; cada errada = um erro clássico):
#   Q1 (Geometria) terreno 250 m × 80 m = 20 000 m² = 2 ha → D. A 0,02 (dividiu por 1 000 000, como se fosse km²) ·
#      B 200 (usou o are, 100 m²) · C 20 (hectare de 1 000 m², erro da seção 11) · E 200 000 000 (multiplicou em vez de
#      dividir: unidade MAIOR tem de dar número MENOR).
#   Q2 (dia a dia) aquário 60 × 30 × 40 cm = 72 000 cm³ = 72 L → E. A 72 000 (tratou cm³ como litro) ·
#      B 7 200 (degrau de 10, como comprimento) · C 720 (degrau de 100, como área) · D 0,072 (calculou em m³ e
#      tratou m³ como litro). Plausível: aquário de 60 cm tem uns 70 litros.
#   Q3 (Física) ônibus a 25 m/s por 216 km: 25 · 3,6 = 90 km/h → 216 ÷ 90 = 2,4 h = 2 h 24 min → C.
#      A 2 h 4 min (leu 0,4 h como 4 min) · B 2 h 40 min (décimo de hora como minuto) · D cerca de 8 h 38 min
#      (não converteu: usou 25 como se fosse km/h, 216 ÷ 25 = 8,64 h) · E cerca de 31 h (3,6 no sentido errado:
#      25 ÷ 3,6 ≈ 6,9 km/h, velocidade de quem anda).
#   Q4 (Química) 12 g de açúcar em 400 mL → 400 mL = 0,4 L → 12 ÷ 0,4 = 30 g/L → B. A 0,03 (não converteu: usou mL
#      como litro) · C 3 (achou que 1 L = 100 mL) · D 4,8 (multiplicou em vez de dividir) · E 300 (andou a vírgula
#      demais: 0,04 L).
#   Q5 (conta de luz) secador de 2 000 W, 15 min por dia, 30 dias: 2 kW · 0,25 h · 30 = 15 kWh → A.
#      B 9 (15 min como 0,15 h: décimo de hora) · C 900 (usou os minutos como horas) · D 15 000 (não passou W para kW) ·
#      E 0,5 (fez só um dia).
# Checklist (seção 13, 13 itens) → episódio: escada nos dois sentidos, conferência de sentido, t/kg/g/mg, padronizar
#   antes de calcular: ep1 · × 100 / × 1 000 por degrau, hectare, 1 L = 1 dm³, 1 L de água = 1 kg: ep2 ·
#   parte decimal × 60, km/h e m/s com o 3,6, unidade composta: ep3 · análise dimensional, fator do enunciado: ep4.
# Meta (material): 30 questões, pelo menos 21 acertos (70%), incluindo Física e Química.
# Ponte (do usuário): Escalas, plantas e mapas.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Revisão de unidades e conversões: 9 pegadinhas e 5 questões estilo ENEM | Unidades de Medida Ep. 5"
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
    # ================= GANCHO (frase do usuário) =================
    dict(id="01", block="hook", text=
        "{a}Este assunto quase nunca é o tema da questão, [p=0.2] mas decide o resultado de *dezenas* delas, [p=0.2] "
        "em Matemática, [p=0.1] Física, [p=0.1] Química e Geografia. [p=0.4] {b}Hoje você confere [p=0.2] se o *erro "
        "silencioso* ainda te pega. [p=0.4] {c}Com um treino, [p=0.2] nove frases [p=0.2] e cinco questões novas."),

    # ================= ONDE A CONVERSÃO DECIDE (seção 01) =================
    dict(id="02", block="onde", text=
        "{t}Por que *silencioso?* [p=0.3] Porque quem troca uma unidade termina a conta normalmente, [p=0.2] acha um "
        "número redondo [p=0.2] e marca a alternativa errada. [p=0.4] {a}Na *Geometria,* [p=0.2] área em metro quadrado "
        "e medida em centímetro. [p=0.3] {b}Na *Física,* [p=0.2] velocidade em quilômetro por hora e tempo em segundos. "
        "[p=0.3] {c}Na *Química,* [p=0.2] gramas por litro com volume em mililitro. [p=0.3] {d}Na *Geografia,* "
        "[p=0.2] hectares e toneladas. [p=0.3] {e}E no *dia a dia:* [p=0.2] receita, conta de água, conta de luz."),

    # ================= ÍNDICE DA REVISÃO: OS 4 ÍCONES =================
    dict(id="03", block="indice", text=
        "{t}Antes de cobrar, [p=0.2] uma frase por episódio. [p=0.4] {a}Um: [p=0.2] a *escada* de sete degraus. "
        "[p=0.2] Cada degrau vale dez, [p=0.2] e *unidade menor, número maior.* [p=0.4] {b}Dois: [p=0.2] na área, "
        "cada degrau é uma *grade* de dez por dez, [p=0.2] cem. [p=0.2] No volume, um *cubo,* [p=0.2] mil. [p=0.2] E o "
        "litro é a *caixa de leite:* [p=0.2] ela enche um cubo de dez centímetros."),
    dict(id="04", block="indice", text=
        "{a}Três: [p=0.2] o *relógio* conta de sessenta em sessenta. [p=0.2] E unidade composta é uma fração de *dois "
        "andares:* [p=0.2] converta os dois. [p=0.4] {b}E quatro: [p=0.2] multiplique por frações que *valem um,* "
        "[p=0.2] e *risque* as unidades iguais. [p=0.2] O que sobra é a resposta."),

    # ================= OS TRÊS FATOS (seção 01) =================
    dict(id="05", block="fatos", text=
        "{t}E se o tempo apertar? [p=0.3] Três fatos resolvem quase tudo. [p=0.4] {a}Um: [p=0.2] área, *cem* por "
        "degrau. [p=0.2] Volume, *mil* por degrau. [p=0.4] {b}Dois: [p=0.2] *um litro é um decímetro cúbico.* [p=0.2] "
        "Daí, um metro cúbico são mil litros. [p=0.4] {c}Três: [p=0.2] o tempo *não é decimal.* [p=0.2] A parte depois "
        "da vírgula, [p=0.2] vezes sessenta."),

    # ================= TREINO-RELÂMPAGO: 6 CONVERSÕES =================
    dict(id="06", block="treino", text=
        "{t}Treino-relâmpago. [p=0.3] Seis conversões. [p=0.4] {b}Dois metros quadrados em centímetros quadrados. "
        "[p=0.3] {c}Zero vírgula três metro cúbico em decímetros cúbicos. [p=0.3] {d}Dois mil e quinhentos centímetros "
        "cúbicos em litros. [p=0.3] {e}Quatro metros cúbicos em litros. [p=0.3] {f}Um vírgula dois hora em horas e "
        "minutos. [p=0.3] {g}E zero vírgula seis hora em minutos. [p=0.4] {p}*Pause e escreva as seis.* [p=2.0]"),
    dict(id="07", block="treino", text=
        "{t}Conferindo! [p=0.3] {b}*Vinte mil* centímetros quadrados: [p=0.2] dois degraus de cem. [p=0.3] {c}*Trezentos* "
        "decímetros cúbicos: [p=0.2] um degrau de mil. [p=0.3] {d}*Dois vírgula cinco* litros: [p=0.2] mil centímetros "
        "cúbicos fazem um litro. [p=0.3] {e}*Quatro mil* litros. [p=0.3] {f}Zero vírgula dois vezes sessenta, doze: "
        "[p=0.2] *uma hora e doze.* [p=0.3] {g}E zero vírgula seis vezes sessenta: [p=0.2] *trinta e seis minutos.* "
        "[p=0.4] {a}Acertou as de tempo? [p=0.2] São as que mais derrubam."),

    # ================= VERDADEIRO OU FALSO: OS 9 ERROS =================
    dict(id="08", block="vf_intro", text=
        "{t}Agora, [p=0.2] *verdadeiro ou falso?* [p=0.3] {a}Nove frases, [p=0.2] dos erros que mais custam pontos. "
        "[p=0.4] {b}Em cada uma, [p=0.2] pause e responda antes de mim."),
    dict(id="09", block="vf", text=
        "{t}Um: [p=0.2] um metro quadrado tem *cem* centímetros quadrados. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* "
        "[p=0.3] {e}Engana porque um metro tem cem centímetros. [p=0.3] {g}Mas a área é uma grade: [p=0.2] cem por "
        "cem, [p=0.2] *dez mil.*"),
    dict(id="10", block="vf", text=
        "{t}Dois: [p=0.2] um metro cúbico tem *um milhão* de centímetros cúbicos. [p=0.3] {p}Pause. [p=1.6] "
        "{r}*Verdadeiro!* [p=0.3] {e}Parece falso porque um milhão parece demais. [p=0.3] {g}Mas é um cubo: [p=0.2] "
        "cem vezes cem vezes cem."),
    dict(id="11", block="vf", text=
        "{t}Três: [p=0.2] um metro cúbico é *um litro.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque "
        "os dois são unidades de volume. [p=0.3] {g}Mas o litro é o *decímetro* cúbico. [p=0.2] Um metro cúbico são "
        "*mil litros,* [p=0.2] uma caixa-d'água."),
    dict(id="12", block="vf", text=
        "{t}Quatro: [p=0.2] dois vírgula quatro horas [p=0.2] são *duas horas e quarenta minutos.* [p=0.3] {p}Pause. "
        "[p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o quatro depois da vírgula parece quarenta. [p=0.3] {g}Mas o "
        "relógio conta de sessenta em sessenta: [p=0.2] zero vírgula quatro vezes sessenta, [p=0.2] *vinte e quatro "
        "minutos.*"),
    dict(id="13", block="vf", text=
        "{t}Cinco: [p=0.2] para passar de quilômetro por hora para metro por segundo, [p=0.2] *divide-se* por três "
        "vírgula seis. [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* [p=0.3] {e}Parece falso porque muita gente "
        "multiplica. [p=0.3] {g}Mas em metro por segundo o número é sempre o *menor.*"),
    dict(id="14", block="vf", text=
        "{t}Seis: [p=0.2] uma tonelada tem *cem* quilos. [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque "
        "cem é um número redondo de quilos. [p=0.3] {g}Mas a tonelada é *um quilo de quilos:* [p=0.2] mil quilos."),
    dict(id="15", block="vf", text=
        "{t}Sete: [p=0.2] um hectare tem *dez mil* metros quadrados. [p=0.3] {p}Pause. [p=1.6] {r}*Verdadeiro!* "
        "[p=0.3] {e}Parece falso porque muita gente lembra de mil. [p=0.3] {g}Mas o hectare é um quadrado de *cem "
        "metros* de lado: [p=0.2] cem vezes cem."),
    dict(id="16", block="vf", text=
        "{t}Oito: [p=0.2] um quilo e meio [p=0.2] mais trezentos gramas [p=0.2] dá *trezentos e um e meio.* [p=0.3] "
        "{p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque a conta fecha, [p=0.2] sem nenhum alarme. [p=0.3] "
        "{g}Padronize antes: [p=0.2] mil e quinhentos gramas mais trezentos, [p=0.2] *mil e oitocentos gramas.*"),
    dict(id="17", block="vf", text=
        "{t}E nove: [p=0.2] para passar de grama por centímetro cúbico [p=0.2] para quilo por metro cúbico, [p=0.2] "
        "basta converter o *grama.* [p=0.3] {p}Pause. [p=1.6] {r}*Falso!* [p=0.3] {e}Engana porque o grama é a unidade "
        "que salta aos olhos. [p=0.3] {g}Mas são *dois andares:* [p=0.2] converta a massa e o volume. [p=0.2] Um "
        "vírgula dois vira *mil e duzentos.*"),
    dict(id="18", block="vf_placar", text=
        "{t}Quantas você acertou? [p=0.3] {a}Seis falsas [p=0.2] e três verdadeiras. [p=0.4] {b}Agora, [p=0.2] as cinco "
        "questões, [p=0.2] todas inéditas, [p=0.2] no estilo do ENEM. [p=0.2] Em todas: [p=0.2] *padronize as "
        "unidades* em voz alta [p=0.2] antes de qualquer conta."),

    # ================= QUESTÃO 1: GEOMETRIA (HECTARES) =================
    dict(id="19", block="q1", text=
        "{t}Questão um, [p=0.2] de Geometria. [p=0.3] {a}Um terreno retangular mede *duzentos e cinquenta metros* "
        "[p=0.2] por *oitenta metros.* [p=0.3] {b}A área desse terreno, [p=0.2] em hectares, [p=0.2] é [p=0.4] {la}A, "
        "[p=0.2] zero vírgula zero dois. [p=0.2] {lb}B, [p=0.2] duzentos. [p=0.2] {lc}C, [p=0.2] vinte. [p=0.2] "
        "{ld}D, [p=0.2] dois. [p=0.2] {le}E, [p=0.2] duzentos milhões. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="20", block="q1", text=
        "{d}Padronizando: [p=0.2] tudo em metros. [p=0.3] {a}Área: [p=0.2] duzentos e cinquenta vezes oitenta, "
        "[p=0.2] *vinte mil* metros quadrados. [p=0.3] {b}Um hectare são dez mil: [p=0.2] vinte mil dividido por dez mil, "
        "[p=0.2] *dois hectares.* [p=0.2] {ok}*Letra D!* [p=0.3] {v}Confere: [p=0.2] dá uns três campos de futebol. "
        "[p=0.4] {xc}A C usou o hectare de mil. [p=0.2] {xb}A B usou o are, [p=0.2] de cem. [p=0.2] {xa}A A dividiu "
        "como se fosse quilômetro quadrado. [p=0.2] {xe}E a E multiplicou: [p=0.2] unidade maior, número *menor.*"),

    # ================= QUESTÃO 2: AQUÁRIO =================
    dict(id="21", block="q2", text=
        "{t}Questão dois, [p=0.2] do dia a dia. [p=0.3] {a}Um aquário tem *sessenta* centímetros de comprimento, "
        "[p=0.2] *trinta* de largura [p=0.2] e *quarenta* de altura. [p=0.3] {b}Cheio, [p=0.2] ele comporta [p=0.4] "
        "{la}A, [p=0.2] setenta e dois mil litros. [p=0.2] {lb}B, [p=0.2] sete mil e duzentos. [p=0.2] {lc}C, "
        "[p=0.2] setecentos e vinte. [p=0.2] {ld}D, [p=0.2] zero vírgula zero setenta e dois. [p=0.2] {le}E, [p=0.2] "
        "setenta e dois. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="22", block="q2", text=
        "{d}Padronizando: [p=0.2] tudo em centímetros. [p=0.3] {a}Volume: [p=0.2] sessenta vezes trinta vezes quarenta, "
        "[p=0.2] *setenta e dois mil* centímetros cúbicos. [p=0.3] {b}A caixa de leite: [p=0.2] mil centímetros "
        "cúbicos fazem um litro. [p=0.2] Então, *setenta e dois litros.* [p=0.2] {ok}*Letra E!* [p=0.3] {v}Confere: "
        "[p=0.2] um aquário desse tamanho leva umas setenta garrafas de um litro. [p=0.4] {xa}A A tratou centímetro "
        "cúbico como litro. [p=0.2] {xd}A D fez em metros e tratou metro cúbico como litro. [p=0.2] {xb}A B e a C "
        "{xc}usaram degraus de dez e de cem, [p=0.2] e no volume o degrau é *mil.*"),

    # ================= QUESTÃO 3: FÍSICA (HORAS DECIMAIS) =================
    dict(id="23", block="q3", text=
        "{t}Questão três, [p=0.2] de Física. [p=0.3] {a}Um ônibus mantém a velocidade de *vinte e cinco metros por "
        "segundo* [p=0.2] numa viagem de *duzentos e dezesseis quilômetros.* [p=0.3] {b}A viagem dura [p=0.4] {la}A, "
        "[p=0.2] duas horas e quatro minutos. [p=0.2] {lb}B, [p=0.2] duas horas e quarenta. [p=0.2] {lc}C, [p=0.2] "
        "duas horas e vinte e quatro. [p=0.2] {ld}D, [p=0.2] cerca de oito horas e trinta e oito. [p=0.2] {le}E, "
        "[p=0.2] cerca de trinta e uma horas. [p=0.4] {p}*Pause e tente.* [p=2.0]"),
    dict(id="24", block="q3", text=
        "{d}Padronizando: [p=0.2] a distância está em quilômetros, [p=0.2] então a velocidade vai para quilômetro por "
        "hora. [p=0.3] {a}Vinte e cinco *vezes* três vírgula seis: [p=0.2] *noventa.* [p=0.3] {b}Duzentos e dezesseis "
        "dividido por noventa: [p=0.2] *dois vírgula quatro* horas. [p=0.3] {c}Zero vírgula quatro vezes sessenta, "
        "[p=0.2] vinte e quatro: [p=0.2] *duas horas e vinte e quatro.* [p=0.2] {ok}*Letra C!* [p=0.4] {xb}A B leu o "
        "décimo como minuto. [p=0.2] {xa}A A leu como quatro minutos. [p=0.2] {xd}A D não converteu os metros por "
        "segundo. [p=0.2] {xe}E a E usou o três vírgula seis ao contrário: [p=0.2] daria um ônibus a passo de gente."),

    # ================= QUESTÃO 4: QUÍMICA (g/L com mL) =================
    dict(id="25", block="q4", text=
        "{t}Questão quatro, [p=0.2] de Química. [p=0.3] {a}Foram dissolvidos *doze gramas* de açúcar [p=0.2] em água, "
        "[p=0.2] formando *quatrocentos mililitros* de solução. [p=0.3] {b}A concentração, [p=0.2] em gramas por "
        "litro, [p=0.2] é [p=0.4] {la}A, [p=0.2] zero vírgula zero três. [p=0.2] {lb}B, [p=0.2] trinta. [p=0.2] "
        "{lc}C, [p=0.2] três. [p=0.2] {ld}D, [p=0.2] quatro vírgula oito. [p=0.2] {le}E, [p=0.2] trezentos. [p=0.4] "
        "{p}*Pause e tente.* [p=2.0]"),
    dict(id="26", block="q4", text=
        "{d}Padronizando: [p=0.2] a resposta pede *litro* embaixo. [p=0.3] {a}Quatrocentos mililitros: [p=0.2] "
        "*zero vírgula quatro* litro. [p=0.3] {b}Doze dividido por zero vírgula quatro: [p=0.2] *trinta gramas por "
        "litro.* [p=0.2] {ok}*Letra B!* [p=0.3] {v}Confere: [p=0.2] num litro inteiro caberiam duas vezes e meia essa "
        "solução, [p=0.2] e doze vezes dois e meio dá trinta. [p=0.4] {xa}A A não converteu o mililitro. [p=0.2] "
        "{xc}A C achou que um litro tem cem mililitros. [p=0.2] {xd}A D multiplicou. [p=0.2] {xe}E a E andou a vírgula "
        "demais."),

    # ================= QUESTÃO 5: CONTA DE LUZ (kWh) =================
    dict(id="27", block="q5", text=
        "{t}E a questão cinco, [p=0.2] da conta de luz. [p=0.3] {a}Um secador de cabelo de *dois mil watts* [p=0.2] "
        "fica ligado *quinze minutos* por dia, [p=0.2] durante *trinta dias.* [p=0.3] {b}O consumo, [p=0.2] em "
        "quilowatt-hora, [p=0.2] é [p=0.4] {la}A, [p=0.2] quinze. [p=0.2] {lb}B, [p=0.2] nove. [p=0.2] {lc}C, [p=0.2] "
        "novecentos. [p=0.2] {ld}D, [p=0.2] quinze mil. [p=0.2] {le}E, [p=0.2] zero vírgula cinco. [p=0.4] {p}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="28", block="q5", text=
        "{d}Padronizando: [p=0.2] quilowatt e hora. [p=0.3] {a}Dois mil watts: [p=0.2] *dois quilowatts.* [p=0.2] "
        "Quinze minutos: [p=0.2] um quarto de hora, [p=0.2] *zero vírgula vinte e cinco.* [p=0.3] {b}Dois vezes zero "
        "vírgula vinte e cinco [p=0.2] vezes trinta: [p=0.2] *quinze quilowatts-hora.* [p=0.2] {ok}*Letra A!* [p=0.4] "
        "{xb}A B escreveu quinze minutos como zero vírgula quinze. [p=0.2] {xc}A C usou os minutos como se fossem "
        "horas. [p=0.2] {xd}A D não passou o watt para quilowatt. [p=0.2] {xe}E a E fez só um dia."),

    # ================= CHECKLIST (seção 13) =================
    dict(id="29", block="checklist", text=
        "{t}Agora, [p=0.2] o checklist de domínio. [p=0.3] {a}Marque só o que você conseguiria *explicar em voz alta* "
        "para outra pessoa, [p=0.2] sem consultar nada. [p=0.4] {b}A escada nos dois sentidos, [p=0.2] a conferência "
        "de sentido, [p=0.2] tonelada, quilo, grama e miligrama, [p=0.2] e padronizar antes de calcular: [p=0.2] "
        "episódio um. [p=0.3] {c}Os degraus de cem e de mil, [p=0.2] o hectare, [p=0.2] o litro como decímetro cúbico "
        "[p=0.2] e o quilo de água: [p=0.2] episódio dois."),
    dict(id="30", block="checklist", text=
        "{a}A parte decimal da hora, [p=0.2] o três vírgula seis [p=0.2] e a unidade composta: [p=0.2] episódio três. "
        "[p=0.3] {b}A análise dimensional [p=0.2] e o fator que o enunciado dá: [p=0.2] episódio quatro. [p=0.4] {c}O "
        "que você *não* marcou, [p=0.2] reveja o episódio correspondente."),

    # ================= META =================
    dict(id="31", block="meta", text=
        "{t}E a meta. [p=0.3] {a}Resolva *trinta questões* [p=0.2] {b}e acerte pelo menos *vinte e uma,* [p=0.2] setenta "
        "por cento. [p=0.4] {c}E inclua questões de *Física* e de *Química:* [p=0.2] lá a conversão aparece no meio "
        "da conta, [p=0.2] sem ninguém avisar."),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}O próximo assunto é *Escalas, plantas e mapas,* [p=0.3] {b}e a escada de unidades vai ser usada o tempo "
        "todo."),
    dict(id="33", block="cta", text=
        "Se essa série te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual pegadinha te pegou? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}A série de unidades e conversões está completa. [p=0.2] Bons estudos, e *até a próxima aula* "
        "aqui no Estudativo. [p=1.5]"),
]
