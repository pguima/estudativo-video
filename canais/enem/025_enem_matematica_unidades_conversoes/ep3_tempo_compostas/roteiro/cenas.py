# Roteiro — Unidades de Medida e Conversões, Episódio 3 de 5: O tempo não é decimal, e como converter velocidade,
#   densidade e vazão
# Base: Estudos/Enem/estudos/01-matematica/10-unidades-conversoes.html — seções 07 e 08 + Questões 3, 4 e 6.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Só CONVERSÃO de unidades: velocidade, densidade e vazão não são ensinadas como conceito (série própria).
# Analogias âncora (retomadas na revisão):
#   O relógio NÃO é decimal: conta de 60 em 60. Um quarto de hora é 15 minutos, não 25.
#   Unidade composta é uma fração de DOIS ANDARES: km em cima, h embaixo. Converta os dois andares, cada um com sua escada.
#   Em m/s o número é sempre o MENOR, porque 1 metro por segundo já é rápido.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte.
# O gancho já cita as respostas das Q3 (3 h 15) e Q4 (20 m/s), por desenho do usuário: as duas entram como "a prova oficial".
# Exemplos dos blocos (nenhum usa os números das questões nem do exercício): 2,4 h e 2,5 h (tempo) · 90 km/h = 25 m/s ·
#   5 m/s = 18 km/h · 2,7 g/cm³ = 2 700 kg/m³ · 50 L/min = 3 m³/h (pelo 0,06 e pelo caminho seguro: 3 000 L/h).
# Nós fazemos (prompt): 1,75 h = 1 h 45 min · 36 km/h = 10 m/s · 15 m/s = 54 km/h.
# QUESTÃO 3 (eu faço): 0,25 · 60 = 15 → 3 h 15 min → A. Material: B (3 h 25) leu o "25" como minutos.
#   NOSSAS: D (3 h 45) trocou um quarto por três quartos (0,75 h = 45 min); C (3 h 40) e E (3 h 50) não saem de conta nenhuma:
#   0,25 é menos que meia hora, então os minutos têm de ser menos que 30.
# QUESTÃO 4 (nós fazemos): 72 ÷ 3,6 = 20 → B. Material: D (259,2) multiplicou por 3,6.
#   NOSSAS: E (20 000) converteu só o andar de cima (72 000 m) e dividiu por 3,6, esquecendo as horas; A (2) dividiu por 36;
#   C (200) dividiu por 0,36.
# QUESTÃO 6 (você faz): 2 h = 120 min; 15 · 120 = 1 800 L; ÷ 1 000 = 1,8 m³ → B. Conferência pelo 0,06: 15 · 0,06 = 0,9 m³/h,
#   · 2 h = 1,8 m³. Material: E (1 800 m³) parou nos litros e trocou a unidade. NOSSAS: A, C e D são o mesmo 18 com a vírgula em
#   outro lugar (fator 10, 100 ou 10 000 em vez de 1 000). O material diz que 1 800 m³ seria "uma piscina olímpica inteira";
#   uma olímpica tem ≈ 2 500 m³ (50 × 25 × 2) → no vídeo: "quase uma piscina olímpica".
# Atalhos (verde): "cada décimo de hora = 6 min; cada quarto = 15 min" · "÷ 3,6 deixa menor; × 3,6 deixa maior: m/s é sempre o
#   menor" · "na dúvida, padronize o tempo primeiro".
# Frases-chave (meio e fim, idênticas): 1. O relógio conta de 60 em 60. 2. Unidade composta: converta os dois andares.
#   3. Em m/s, o número é sempre o menor.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "O tempo não é decimal: horas, minutos, km/h e m/s | Unidades de Medida Ep. 3"
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
        "{a}Três vírgula vinte e cinco horas [p=0.2] são três horas e vinte e cinco minutos? [p=0.4] {b}Não: [p=0.2] são "
        "*três horas e quinze.* [p=0.5] {c}E setenta e dois quilômetros por hora em metros por segundo [p=0.2] dá "
        "*vinte,* [p=0.2] não duzentos e cinquenta e nove. [p=0.5] {d}Hoje você para de errar as duas."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai converter tempo sem errar [p=0.3] {b}e passar velocidade, densidade e "
        "vazão de uma unidade para outra."),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes rápidos. [p=0.3] {a}A escada do episódio um: [p=0.2] cada degrau vale dez. [p=0.2] "
        "Um quilômetro tem *mil* metros. [p=0.4] {b}Do episódio dois: [p=0.2] um metro cúbico são *mil litros.* [p=0.4] "
        "{c}E da série de Grandezas: [p=0.2] zero vírgula quatro hora [p=0.2] *não* é quarenta minutos. [p=0.2] É "
        "*vinte e quatro.*"),

    # ================= CONCRETO =================
    dict(id="04", block="cotidiano", text=
        "{t}Três cenas do dia a dia. [p=0.3] {a}Um cronômetro marca *três vírgula vinte e cinco horas.* [p=0.2] Quanto é "
        "isso no relógio? [p=0.4] {b}O velocímetro do carro fala em quilômetros por hora. [p=0.2] Mas a placa da prova de "
        "atletismo fala em *metros por segundo.* [p=0.4] {c}E uma torneira aberta solta tantos *litros por minuto.* "
        "[p=0.3] {d}Em todas, [p=0.2] o número só faz sentido na unidade certa."),

    # ================= BLOCO A: SEXAGESIMAL =================
    dict(id="05", block="sexagesimal", text=
        "{t}Por que o tempo derruba tanta gente? [p=0.4] {a}Porque todas as outras unidades andam de dez em dez. [p=0.2] "
        "O tempo, não. [p=0.3] {b}Ele é *sexagesimal:* [p=0.2] conta de *sessenta* em sessenta. [p=0.4] {c}Uma hora tem "
        "sessenta minutos. [p=0.2] Um minuto tem sessenta segundos. [p=0.4] {d}E uma hora tem sessenta vezes sessenta: "
        "[p=0.2] *três mil e seiscentos* segundos."),

    # ================= BLOCO B: DÉCIMO DE HORA =================
    dict(id="06", block="decimo", text=
        "{t}Então, o que fazer com uma hora quebrada, [p=0.2] tipo *dois vírgula quatro horas?* [p=0.4] {a}A parte "
        "inteira já está pronta: [p=0.2] duas horas. [p=0.4] {b}E a parte depois da vírgula [p=0.2] você *multiplica por "
        "sessenta.* [p=0.3] Zero vírgula quatro vezes sessenta: [p=0.2] *vinte e quatro* minutos. [p=0.4] {c}Duas horas e "
        "vinte e quatro minutos. [p=0.3] Não duas e quarenta."),
    dict(id="07", block="decimo", text=
        "{t}Mais um. [p=0.2] *Dois vírgula cinco horas.* [p=0.4] {a}Zero vírgula cinco vezes sessenta: [p=0.2] *trinta.* "
        "[p=0.3] Duas horas e meia, [p=0.2] duas horas e trinta minutos. [p=0.4] {b}Repare: [p=0.2] o *cinco* virou "
        "*trinta.* [p=0.3] Porque meia hora é metade de *sessenta,* [p=0.2] e não metade de cem."),

    # ================= BLOCO C: AS FRAÇÕES DE HORA =================
    dict(id="08", block="relogio", text=
        "{t}E existem frações de hora que vale reconhecer de cara. [p=0.4] {a}Olhe o relógio dividido em quatro. [p=0.3] "
        "{b}Zero vírgula vinte e cinco é *um quarto* de hora: [p=0.2] *quinze* minutos. [p=0.4] {c}Zero vírgula cinco, "
        "[p=0.2] meia hora: [p=0.2] *trinta.* [p=0.4] {d}Zero vírgula setenta e cinco, [p=0.2] três quartos: [p=0.2] "
        "*quarenta e cinco.*"),
    dict(id="09", block="relogio", text=
        "{t}E agora o relógio dividido em dez. [p=0.4] {a}Zero vírgula um hora [p=0.2] é *seis* minutos. [p=0.4] {b}Zero "
        "vírgula dois, [p=0.2] *doze.* [p=0.4] {c}Zero vírgula oito, [p=0.2] *quarenta e oito.* [p=0.4] {d}Atalho: "
        "[p=0.2] *cada décimo de hora vale seis minutos,* [p=0.2] e cada quarto vale quinze. [p=0.3] Um quarto de hora "
        "é quinze minutos, [p=0.2] não vinte e cinco."),

    # ================= BLOCO D: UNIDADE COMPOSTA =================
    dict(id="10", block="composta", text=
        "{t}Agora, uma unidade diferente. [p=0.3] {a}Quilômetro por hora tem *duas* unidades juntas: [p=0.2] uma de "
        "distância, [p=0.2] outra de tempo. [p=0.3] {b}Isso é uma *unidade composta.* [p=0.4] {c}Pense nela como uma "
        "*fração de dois andares.* [p=0.3] Em cima, o *numerador:* [p=0.2] quilômetros. [p=0.3] Embaixo, o "
        "*denominador:* [p=0.2] horas."),
    dict(id="11", block="composta", text=
        "{t}E como converter uma fração de dois andares? [p=0.4] {a}Cada andar desce a *sua própria* escada. [p=0.3] "
        "{b}Em cima, [p=0.2] quilômetro vira metro: [p=0.2] vezes mil. [p=0.4] {c}Embaixo, [p=0.2] hora vira segundo: "
        "[p=0.2] vezes três mil e seiscentos. [p=0.4] {d}A regra: [p=0.2] *converta os dois andares.* [p=0.3] Converter "
        "só um [p=0.2] é o erro mais silencioso desta aula."),

    # ================= BLOCO E: KM/H E M/S =================
    dict(id="12", block="velocidade", text=
        "{t}E de onde vem o famoso *três vírgula seis?* [p=0.4] {a}Um quilômetro por hora [p=0.2] é *mil* metros em *três "
        "mil e seiscentos* segundos. [p=0.4] {b}Mil dividido por três mil e seiscentos: [p=0.2] o mesmo que um dividido "
        "por *três vírgula seis.* [p=0.4] {c}Por isso, [p=0.2] de quilômetro por hora para metro por segundo, [p=0.2] "
        "*divida* por três vírgula seis."),
    dict(id="13", block="velocidade", text=
        "{t}Vamos usar. [p=0.3] {a}Um carro a noventa quilômetros por hora. [p=0.2] Noventa dividido por três vírgula "
        "seis: [p=0.2] *vinte e cinco* metros por segundo. [p=0.4] {b}E o caminho de volta, [p=0.2] de metro por segundo "
        "para quilômetro por hora: [p=0.2] *multiplique* por três vírgula seis. [p=0.4] {c}Um corredor a cinco metros "
        "por segundo: [p=0.2] cinco vezes três vírgula seis, [p=0.2] *dezoito* quilômetros por hora."),
    dict(id="14", block="velocidade", text=
        "{t}E como lembrar se divide ou multiplica? [p=0.4] {a}Olhe o tamanho. [p=0.3] Um metro por segundo já é rápido: "
        "[p=0.2] é uma caminhada apressada. [p=0.4] {b}Então, em metros por segundo, [p=0.2] o número é sempre o "
        "*menor.* [p=0.4] {c}Atalho: [p=0.2] dividir por três vírgula seis *diminui;* [p=0.2] multiplicar *aumenta.* "
        "[p=0.3] O resultado em metros por segundo saiu maior? [p=0.2] Você foi para o lado errado."),

    # ================= BLOCO F: DENSIDADE =================
    dict(id="15", block="densidade", text=
        "{t}E a densidade? [p=0.3] {a}Hoje não vamos estudar o que ela é. [p=0.2] Só trocar a unidade. [p=0.3] {b}Ela "
        "também é uma fração de dois andares: [p=0.2] *gramas* em cima, [p=0.2] *centímetros cúbicos* embaixo. [p=0.4] "
        "{c}Para passar de grama por centímetro cúbico para quilo por metro cúbico, [p=0.2] *multiplique por mil.* "
        "[p=0.4] {d}O alumínio tem dois vírgula sete: [p=0.2] vira *dois mil e setecentos.* [p=0.3] E o porquê desse "
        "mil [p=0.2] fica para o próximo episódio."),

    # ================= BLOCO G: VAZÃO =================
    dict(id="16", block="vazao", text=
        "{t}E a vazão, [p=0.2] os litros por minuto da torneira? [p=0.4] {a}Para passar de litro por minuto [p=0.2] para "
        "metro cúbico por hora, [p=0.2] multiplique por *zero vírgula zero seis.* [p=0.4] {b}Uma bomba de cinquenta "
        "litros por minuto: [p=0.2] cinquenta vezes zero vírgula zero seis, [p=0.2] *três* metros cúbicos por hora."),
    dict(id="17", block="vazao", text=
        "{t}Esqueceu o zero vírgula zero seis? [p=0.3] Sem problema. [p=0.4] {a}O caminho seguro: [p=0.2] *padronize o "
        "tempo primeiro.* [p=0.3] Uma hora tem sessenta minutos: [p=0.2] cinquenta vezes sessenta, [p=0.2] *três mil* "
        "litros por hora. [p=0.4] {b}Depois, os litros: [p=0.2] mil litros é um metro cúbico. [p=0.2] Três mil litros, "
        "[p=0.2] *três* metros cúbicos. [p=0.4] {c}O mesmo resultado, [p=0.2] um andar de cada vez."),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez. [p=0.2] Três conversões. [p=0.3] {a}Um vírgula setenta e cinco horas, [p=0.2] em horas e minutos. "
        "[p=0.3] {b}Trinta e seis quilômetros por hora, [p=0.2] em metros por segundo. [p=0.3] {c}Quinze metros por "
        "segundo, [p=0.2] em quilômetros por hora. [p=0.4] {d}*Pause o vídeo e converta.* [p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Zero vírgula setenta e cinco é três quartos de hora: [p=0.2] quarenta e cinco "
        "minutos. [p=0.2] *Uma hora e quarenta e cinco.* [p=0.4] {b}Trinta e seis dividido por três vírgula seis: [p=0.2] "
        "*dez* metros por segundo. [p=0.2] Menor, como tem que ser. [p=0.4] {c}Quinze vezes três vírgula seis: [p=0.2] "
        "*cinquenta e quatro* quilômetros por hora. [p=0.2] Maior, como tem que ser."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] o relógio conta de sessenta em sessenta. [p=0.5] "
        "{b}Dois: [p=0.2] unidade composta: [p=0.2] converta os dois andares. [p=0.5] {c}Três: [p=0.2] em metros por "
        "segundo, [p=0.2] o número é sempre o menor."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] ler dois vírgula quatro horas como *duas "
        "horas e quarenta.* [p=0.4] {b}Parece certo, [p=0.2] porque o número depois da vírgula parece ser os minutos. "
        "[p=0.4] {c}Mas o relógio conta de sessenta em sessenta: [p=0.2] zero vírgula quatro vezes sessenta, [p=0.2] "
        "*vinte e quatro* minutos."),
    dict(id="22", block="erros", text=
        "{a}Segundo: [p=0.2] *multiplicar* por três vírgula seis para passar de quilômetro por hora para metro por "
        "segundo. [p=0.4] {b}Parece certo, [p=0.2] porque o metro é menor que o quilômetro, [p=0.2] e a gente lembra que "
        "o número cresce. [p=0.4] {c}Mas o segundo também é menor que a hora. [p=0.2] No fim, [p=0.2] *divida.* [p=0.2] "
        "Em metros por segundo, o número é o menor."),
    dict(id="23", block="erros", text=
        "{a}Terceiro: [p=0.2] converter só o andar de cima de uma unidade composta. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque o quilômetro virou metro, [p=0.2] e a conta deu um número. [p=0.4] {c}Mas o andar de baixo continua em "
        "horas. [p=0.2] Converta os *dois* andares."),
    dict(id="24", block="erros", text=
        "{a}Quarto: [p=0.2] parar nos *litros* quando a questão pede *metros cúbicos.* [p=0.4] {b}Parece certo, [p=0.2] "
        "porque a conta já está pronta, [p=0.2] e o número está nas alternativas. [p=0.4] {c}Mas releia a unidade "
        "pedida: [p=0.2] mil litros é um metro cúbico. [p=0.2] *Divida por mil.*"),

    # ================= QUESTÃO 3 (EU FAÇO) =================
    dict(id="25", block="q3", text=
        "{t}Agora, as questões do nosso material, [p=0.2] no estilo do ENEM. [p=0.3] A primeira, [p=0.2] eu faço com "
        "você. [p=0.4] {a}Um percurso foi cronometrado em *três vírgula vinte e cinco horas.* [p=0.3] {b}Esse tempo "
        "corresponde a: [p=0.4] {qa}A: [p=0.2] três horas e quinze minutos. [p=0.3] {qb}B: [p=0.2] três horas e vinte e "
        "cinco. [p=0.3] {qc}C: [p=0.2] três horas e quarenta. [p=0.3] {qd}D: [p=0.2] três horas e quarenta e cinco. "
        "[p=0.3] {qe}E: [p=0.2] três horas e cinquenta."),
    dict(id="26", block="q3", text=
        "{t}A parte inteira já são *três horas.* [p=0.4] {a}A parte decimal, [p=0.2] vezes sessenta: [p=0.2] zero "
        "vírgula vinte e cinco vezes sessenta, [p=0.2] *quinze* minutos. [p=0.3] É um quarto de hora. [p=0.3] {ok}*Letra "
        "A!* [p=0.4] {xb}A B leu o vinte e cinco direto como minutos: [p=0.2] o erro do relógio decimal. [p=0.4] {xd}A D "
        "trocou um quarto por *três quartos.* [p=0.4] {xc}E a C [p=0.2] {xe}e a E caem na conferência: [p=0.2] zero "
        "vírgula vinte e cinco é menos que meia hora, [p=0.2] então os minutos têm que ser menos que trinta."),

    # ================= QUESTÃO 4 (NÓS FAZEMOS) =================
    dict(id="27", block="q4", text=
        "{t}A segunda, [p=0.2] a gente faz junto. [p=0.4] {a}Um veículo trafega a *setenta e dois quilômetros por hora* "
        "em uma rodovia. [p=0.3] {b}Essa velocidade, [p=0.2] expressa em metros por segundo, [p=0.2] é de: [p=0.4] "
        "{qa}A: [p=0.2] dois. [p=0.3] {qb}B: [p=0.2] vinte. [p=0.3] {qc}C: [p=0.2] duzentos. [p=0.3] {qd}D: [p=0.2] "
        "duzentos e cinquenta e nove vírgula dois. [p=0.3] {qe}E: [p=0.2] vinte mil. [p=0.4] {p}Pense comigo: [p=0.2] "
        "divide ou multiplica? [p=1.5]"),
    dict(id="28", block="q4", text=
        "{t}Para metros por segundo, [p=0.2] o número tem que *diminuir:* [p=0.2] *divida* por três vírgula seis. "
        "[p=0.4] {a}Setenta e dois dividido por três vírgula seis: [p=0.2] *vinte.* [p=0.3] {ok}*Letra B!* [p=0.4] "
        "{xd}A D multiplicou por três vírgula seis: [p=0.2] o número cresceu, [p=0.2] e não podia. [p=0.4] {xe}A E "
        "converteu só o andar de cima: [p=0.2] setenta e dois mil metros, [p=0.2] e esqueceu que a hora também vira "
        "segundo. [p=0.4] {xa}A A dividiu por trinta e seis, [p=0.2] {xc}e a C por zero vírgula trinta e seis: [p=0.2] a "
        "vírgula do três vírgula seis no lugar errado."),

    # ================= QUESTÃO 6 (VOCÊ FAZ) =================
    dict(id="29", block="q6", text=
        "{t}A última, [p=0.2] você faz sozinho. [p=0.4] {a}Uma torneira despeja água a uma vazão constante de *quinze "
        "litros por minuto.* [p=0.3] Deixada aberta por *duas horas,* [p=0.2] ela terá despejado um volume de: [p=0.4] "
        "{qa}A: [p=0.2] zero vírgula dezoito metro cúbico. [p=0.3] {qb}B: [p=0.2] um vírgula oito. [p=0.3] {qc}C: [p=0.2] "
        "dezoito. [p=0.3] {qd}D: [p=0.2] cento e oitenta. [p=0.3] {qe}E: [p=0.2] mil e oitocentos metros cúbicos. [p=0.5] "
        "{p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="30", block="q6", text=
        "{t}Vamos resolver. [p=0.3] {a}Primeiro, [p=0.2] *padronize o tempo:* [p=0.2] a vazão está por minuto, [p=0.2] "
        "e duas horas são *cento e vinte* minutos. [p=0.4] {b}Quinze vezes cento e vinte: [p=0.2] *mil e oitocentos "
        "litros.* [p=0.4] {c}Mas a questão pede metros cúbicos. [p=0.2] Divida por mil: [p=0.2] *um vírgula oito* metro "
        "cúbico. [p=0.3] {ok}*Letra B!* [p=0.4] {d}E pelo atalho: [p=0.2] quinze vezes zero vírgula zero seis dá zero "
        "vírgula nove por hora. [p=0.2] Em duas horas, [p=0.2] um vírgula oito. [p=0.2] Confere."),
    dict(id="31", block="q6", text=
        "{t}E as outras? [p=0.3] {xe}A E parou nos litros [p=0.2] e só trocou o nome da unidade. [p=0.3] Mil e oitocentos "
        "metros cúbicos [p=0.2] seria quase uma piscina olímpica inteira! [p=0.4] {xa}A A, [p=0.2] {xc}a C [p=0.2] {xd}e "
        "a D [p=0.2] são o mesmo dezoito, [p=0.2] com a vírgula em outro lugar: [p=0.2] quem errou o *mil* do litro para "
        "o metro cúbico."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="32", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] o relógio conta de sessenta em sessenta. [p=0.5] "
        "{b}Dois: [p=0.2] unidade composta: [p=0.2] converta os dois andares. [p=0.5] {c}Três: [p=0.2] em metros por "
        "segundo, [p=0.2] o número é sempre o menor."),

    # ================= PONTE E CTA =================
    dict(id="33", block="ponte", text=
        "{a}E quando você não lembra o fator, [p=0.2] como o três vírgula seis [p=0.2] ou o mil da densidade? [p=0.4] "
        "{b}Existe um método que *nunca falha* [p=0.2] e se confere sozinho. [p=0.4] {c}Próximo episódio."),
    dict(id="34", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quanto deu um vírgula setenta e cinco hora para você? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
