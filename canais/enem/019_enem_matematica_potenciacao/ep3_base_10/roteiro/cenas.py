# Roteiro — Potenciação e Radiciação, Episódio 3 de 7: Potências de base 10, a base mais usada da prova (iniciantes)
# Base: Estudos/Enem/estudos/01-matematica/04-potenciacao-radiciacao.html — seção 04 (+ Questões 2 e 9 da seção 12).
# NÃO ensina a forma exata da notação científica (série própria): só potências de 10 e as propriedades 1, 2, 3 e 4.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogia âncora: o expoente do 10 é um CONTADOR DE ZEROS: 10ⁿ = 1 seguido de n zeros; 10⁻ⁿ = n casas depois da vírgula,
#   com o 1 na última. Liga com a ESCADA do ep. 1 (agora cada degrau para baixo divide por 10).
# Exemplos: 10¹ = 10 · 10² = 100 · 10³ = 1 000 · 10⁶ = 1 000 000 · 10⁻¹ = 0,1 · 10⁻² = 0,01 · 10⁻³ = 0,001 ·
#   10⁶ · 10⁻³ = 10³ (o gancho: 1 000 000 × 0,001 = 1 000) · (3·10⁵)(2·10⁻⁸) = 6·10⁻³ · (9·10⁷) ÷ (3·10⁴) = 3·10³ ·
#   (2·10⁻²)³ = 2³·10⁻⁶ (exemplo do prompt; a Questão 9 retoma a conta com contexto).
# Nós fazemos: 10⁴ · 10⁻⁶ = 10⁻² · (4·10⁸) ÷ (2·10³) = 2·10⁵.
# QUESTÃO 2 do material (texto idêntico na tela): 7,2·10⁹ ÷ 1,2·10⁶ = 6·10³ → B.
#   E (8,64·10¹⁵): multiplicou em vez de dividir (explicação do material).
#   Explicações NOSSAS: D (8,4·10³) somou 7,2 + 1,2 · A (6·10²) e C (6·10⁴) erraram a conta dos expoentes (um zero a menos
#   ou a mais); a prova real: 6·10³ × 1,2·10⁶ = 7,2·10⁹.
# QUESTÃO 9 do material (texto idêntico na tela): (2·10⁻²)³ = 2³·10⁻⁶ = 8·10⁻⁶ → B.
#   D (2·10⁻⁶) elevou só o 10 · A (6·10⁻⁶) fez 2·3 = 6 (as duas do material).
#   Explicações NOSSAS: C (8·10⁻⁵) somou −2 + (−3) em vez de multiplicar · E (6·10⁻²) multiplicou a aresta por 3.
# Frases-chave (meio e fim, idênticas):
#   1. O expoente do 10 conta os zeros.
#   2. Multiplicou: soma os expoentes. Dividiu: subtrai.
#   3. O expoente de fora pega todos os fatores de dentro.
# Atalhos (verde): "mil = 10³, milhão = 10⁶, bilhão = 10⁹" · "negativo: o 1 é a última casa" · "números com números,
#   potências com potências" · "por habitante, por pessoa, por unidade = dividir" · "de fora entra em todos".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Potências de 10: 1 000 000 × 0,001 de cabeça em 3 segundos · Matemática ENEM, episódio 3"

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
    "kWh": "quilowatt-hora",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Quanto é *um milhão* [p=0.2] vezes *zero vírgula zero zero um?* [p=0.6] {b}Parece conta de calculadora. "
        "[p=0.4] {c}Mas com potências de dez, [p=0.2] você responde *de cabeça,* [p=0.2] em três segundos: [p=0.3] "
        "{d}é só *somar dois números.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai *ler* potências de dez [p=0.2] {b}e *multiplicar e dividir* essas "
        "potências [p=0.2] *de cabeça.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, três lembretes. [p=0.3] {a}Multiplicou potências de mesma base? [p=0.2] *Soma* os expoentes. [p=0.3] Dividiu? [p=0.2] *Subtrai.* [p=0.4] {b}Potência de potência: [p=0.2] *multiplica* "
        "os expoentes. [p=0.4] {c}E o expoente negativo [p=0.2] não deixa negativo: [p=0.2] ele manda *inverter.*"),

    # ================= CONCRETO: ZEROS DEMAIS =================
    dict(id="04", block="zeros", text=
        "{t}Pense nos números do noticiário. [p=0.3] {a}O Brasil tem uns *duzentos milhões* de pessoas. [p=0.3] {b}Um vírus "
        "mede uns *zero vírgula zero zero zero zero zero zero um* metro. [p=0.3] {c}A luz de uma cidade, [p=0.2] bilhões. "
        "[p=0.4] {d}Zeros demais: [p=0.2] chato e fácil de errar. [p=0.3] {e}Por isso a prova usa *potências de dez.*"),

    # ================= BLOCO A: O CONTADOR DE ZEROS =================
    dict(id="05", block="zeros", text=
        "{t}*Potência de dez* é o dez multiplicado por ele mesmo. [p=0.4] {a}Dez elevado a um: [p=0.2] *dez.* [p=0.3] "
        "{b}Dez elevado a dois: [p=0.2] dez vezes dez, [p=0.2] *cem.* [p=0.3] {c}Dez elevado a três: [p=0.2] *mil.* "
        "[p=0.4] {d}Repare: [p=0.2] o expoente é *exatamente* o número de zeros. [p=0.4] {e}Dez elevado a seis: [p=0.2] "
        "um, [p=0.2] seguido de *seis zeros,* [p=0.2] um milhão."),
    dict(id="06", block="zeros", text=
        "{t}O expoente do dez é um *contador de zeros.* [p=0.4] {a}Atalho: [p=0.2] guarde três nomes. [p=0.3] {b}*mil* "
        "tem três zeros, [p=0.2] dez elevado a três. [p=0.3] {c}*Milhão,* seis zeros, [p=0.2] dez elevado a seis. [p=0.3] "
        "{d}*Bilhão,* nove zeros, [p=0.2] dez elevado a nove."),

    # ================= BLOCO B: OS NEGATIVOS =================
    dict(id="07", block="decimais", text=
        "{t}E o expoente *negativo?* [p=0.3] Lembra da escada do episódio um? [p=0.4] {a}Agora cada degrau para baixo "
        "[p=0.2] divide por *dez.* [p=0.3] {b}Mil, [p=0.2] cem, [p=0.2] dez, [p=0.2] *um.* "
        "[p=0.4] {c}Mais um degrau: [p=0.2] dez elevado a menos um, [p=0.2] *zero vírgula um.* [p=0.3] {d}Menos dois: "
        "[p=0.2] *zero vírgula zero um.* [p=0.3] {e}Menos três: [p=0.2] *zero vírgula zero zero um.*"),
    dict(id="08", block="decimais", text=
        "{t}Cada algarismo depois da vírgula [p=0.2] ocupa uma *casa decimal.* [p=0.4] {a}E o contador funciona: "
        "[p=0.2] dez elevado a menos três [p=0.2] tem *três casas* depois da vírgula. [p=0.4] {b}Cuidado: "
        "[p=0.2] não são três zeros. [p=0.2] São dois zeros [p=0.2] e o um. [p=0.4] {c}Atalho: [p=0.2] o *um* sempre "
        "ocupa a *última* casa."),

    # ================= BLOCO C: MULTIPLICAR =================
    dict(id="09", block="multiplicar", text=
        "{t}Como se multiplica? [p=0.3] {a}Dez mil vezes cem: [p=0.2] quatro zeros [p=0.2] mais dois, [p=0.2] *seis "
        "zeros.* [p=0.4] {b}Em potência: [p=0.2] dez elevado a quatro, [p=0.2] vezes dez "
        "elevado a dois, [p=0.2] *dez elevado a seis.* [p=0.4] {c}É a regra da mesma base: [p=0.2] multiplicou, [p=0.2] "
        "*soma os expoentes.*"),
    dict(id="10", block="multiplicar", text=
        "{t}E agora, a conta do começo. [p=0.4] {a}Um milhão é dez elevado a seis. [p=0.3] {b}Zero vírgula zero zero um "
        "é dez elevado a *menos três.* [p=0.4] {c}Soma os expoentes: [p=0.2] seis mais menos três [p=0.2] é seis menos "
        "três, [p=0.2] *três.* [p=0.4] {d}Dez elevado a três: [p=0.2] *mil.* [p=0.3] Três segundos!"),
    dict(id="11", block="multiplicar", text=
        "{t}E com um número na frente do dez? [p=0.3] {a}Três vezes dez elevado a cinco, [p=0.2] vezes dois vezes dez "
        "elevado a menos oito. [p=0.4] {b}Os números da frente se multiplicam: [p=0.2] três vezes dois, "
        "[p=0.2] *seis.* [p=0.3] {c}Os expoentes se somam: [p=0.2] cinco mais menos oito, [p=0.2] *menos três.* [p=0.4] "
        "{d}Seis vezes dez elevado a menos três. [p=0.4] {e}Atalho: [p=0.2] *números com números,* [p=0.2] *potências "
        "com potências.*"),

    # ================= BLOCO D: DIVIDIR =================
    dict(id="12", block="dividir", text=
        "{t}E a divisão? [p=0.3] {a}Nove vezes dez elevado a sete, [p=0.2] dividido por três vezes dez elevado a "
        "quatro. [p=0.4] {b}Os números da frente se *dividem:* [p=0.2] nove dividido por três, [p=0.2] *três.* [p=0.3] "
        "{c}Os expoentes se *subtraem:* [p=0.2] sete menos quatro, [p=0.2] *três.* [p=0.4] {d}Três vezes dez elevado a "
        "três: [p=0.2] *três mil.*"),

    # ================= BLOCO E: ELEVAR =================
    dict(id="13", block="elevar", text=
        "{t}E quando a conta inteira vem elevada? [p=0.3] {a}Dois vezes dez elevado a menos dois, [p=0.2] *ao cubo.* "
        "[p=0.4] {b}O expoente de fora age nos *dois* fatores: [p=0.3] {c}no dois, [p=0.2] que vira dois ao "
        "cubo, [p=0.3] {d}e no dez, [p=0.2] que vira dez elevado a menos dois vezes três, [p=0.2] *menos seis.* [p=0.4] "
        "{e}Atalho: [p=0.2] o expoente de fora [p=0.2] *entra em todo mundo* de dentro."),

    # ================= NÓS FAZEMOS =================
    dict(id="14", block="exercicio", text=
        "{t}Sua vez. [p=0.3] Duas contas. [p=0.3] {a}Dez elevado a quatro, [p=0.2] vezes dez elevado a menos seis. "
        "[p=0.4] {b}Quatro vezes dez elevado a oito, [p=0.2] dividido por dois vezes dez elevado a três. [p=0.4] "
        "{c}*Pause o vídeo e calcule.* [p=2.0]"),
    dict(id="15", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Multiplicou: [p=0.2] soma. [p=0.2] Quatro mais menos seis: [p=0.2] dez elevado a "
        "*menos dois.* [p=0.4] {b}Dividiu: [p=0.2] quatro dividido por dois, [p=0.2] *dois;* "
        "[p=0.2] oito menos três, [p=0.2] *cinco.* [p=0.2] Dois vezes dez elevado a cinco."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="16", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] o expoente do dez conta os zeros. [p=0.5] {b}Dois: "
        "[p=0.2] multiplicou, [p=0.2] soma os expoentes. [p=0.2] Dividiu, [p=0.2] subtrai. [p=0.5] {c}Três: [p=0.2] o "
        "expoente de fora pega todos os fatores de dentro."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="17", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] a pergunta é *por habitante,* [p=0.2] e a "
        "pessoa *multiplica.* [p=0.4] {b}Parece certo, [p=0.2] porque multiplicar parece o natural. [p=0.4] {c}Mas por "
        "habitante é *repartir:* [p=0.2] o total dividido pelas pessoas."),
    dict(id="18", block="erros", text=
        "{a}Segundo: [p=0.2] elevar *só o dez* [p=0.2] e esquecer o número da frente. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque o dez é quem tem expoente. [p=0.4] {c}Mas o expoente de fora pega *todos* os fatores."),
    dict(id="19", block="erros", text=
        "{a}Terceiro: [p=0.2] dois ao cubo virar *seis.* [p=0.4] {b}Parece certo, [p=0.2] porque dois vezes três dá "
        "seis. [p=0.4] {c}Mas lembre da folha dobrada: [p=0.2] dois vezes dois vezes dois, [p=0.2] *oito.*"),

    # ================= QUESTÃO 2 DO MATERIAL =================
    dict(id="20", block="q2", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}Uma cidade consome "
        "sete vírgula dois vezes dez elevado a nove [p=0.2] quilowatts-hora de energia elétrica por ano, [p=0.3] e tem um "
        "vírgula dois vezes dez elevado a seis habitantes. [p=0.4] {k}Quilowatt-hora [p=0.2] é a unidade que aparece na "
        "sua conta de luz. [p=0.4] {b}O consumo médio anual *por habitante,* [p=0.2] em quilowatt-hora, [p=0.2] é de: "
        "[p=0.4] {qa}A: [p=0.2] seis vezes dez elevado a dois. [p=0.3] {qb}B: [p=0.2] seis vezes dez elevado a três. "
        "[p=0.3] {qc}C: [p=0.2] seis vezes dez elevado a quatro. [p=0.3] {qd}D: [p=0.2] oito vírgula quatro vezes dez "
        "elevado a três. [p=0.3] {qe}E: [p=0.2] oito vírgula sessenta e quatro vezes dez elevado a quinze. [p=0.5] "
        "{p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="21", block="q2", text=
        "{t}Vamos resolver. [p=0.3] {a}*Por habitante* é repartir: [p=0.2] é uma *divisão.* [p=0.4] {b}Os números da "
        "frente: [p=0.2] sete vírgula dois dividido por um vírgula dois. [p=0.3] É o mesmo que setenta e dois dividido "
        "por doze: [p=0.2] *seis.* [p=0.4] {c}Os expoentes: [p=0.2] nove menos seis, [p=0.2] *três.* [p=0.4] {d}Seis "
        "vezes dez elevado a três: [p=0.2] seis mil por pessoa. [p=0.3] {ok}*Letra B!*"),
    dict(id="22", block="q2", text=
        "{t}E as outras? [p=0.3] {xe}A E *multiplicou* em vez de dividir. [p=0.4] {xd}A D *somou* os números da frente. "
        "[p=0.4] {xa}{xc}A A e a C erraram a conta dos expoentes. [p=0.4] {pr}Prova real: [p=0.2] seis mil vezes um "
        "vírgula dois milhão [p=0.2] dá os sete vírgula dois bilhões."),

    # ================= QUESTÃO 9 DO MATERIAL =================
    dict(id="23", block="q9", text=
        "{t}Mais uma do material. [p=0.4] {a}Um cubo tem aresta medindo dois vezes dez elevado a menos dois metro. "
        "[p=0.4] {k}*Aresta* é cada lado do cubo. [p=0.3] {v}E o *volume,* [p=0.2] o espaço lá dentro, [p=0.2] é aresta "
        "vezes aresta vezes aresta: [p=0.2] a aresta *ao cubo.* [p=0.4] {b}O volume desse cubo, [p=0.2] em metros "
        "cúbicos, é: [p=0.4] {qa}A: [p=0.2] seis vezes dez elevado a menos seis. [p=0.3] {qb}B: [p=0.2] oito vezes dez "
        "elevado a menos seis. [p=0.3] {qc}C: [p=0.2] oito vezes dez elevado a menos cinco. [p=0.3] {qd}D: [p=0.2] dois "
        "vezes dez elevado a menos seis. [p=0.3] {qe}E: [p=0.2] seis vezes dez elevado a menos dois. [p=0.5] "
        "{p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="24", block="q9", text=
        "{t}Vamos resolver. [p=0.3] {a}Volume é a aresta ao cubo. [p=0.3] {b}E o expoente de fora entra em todo mundo. "
        "[p=0.3] {c}Dois ao cubo: [p=0.2] dois, "
        "[p=0.2] quatro, [p=0.2] *oito.* [p=0.4] {d}Dez elevado a menos dois, [p=0.2] ao cubo: [p=0.2] menos dois vezes "
        "três, [p=0.2] *menos seis.* [p=0.4] {e}Oito vezes dez elevado a menos seis metro cúbico. [p=0.3] {ok}*Letra B!*"),
    dict(id="25", block="q9", text=
        "{t}E as outras? [p=0.3] {xd}A D elevou *só o dez.* [p=0.4] {xa}A A fez dois vezes três, [p=0.2] seis. [p=0.4] "
        "{xc}A C *somou* menos dois com menos três, [p=0.2] em vez de multiplicar. [p=0.4] {xe}E a E multiplicou a aresta "
        "por três."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="26", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] o expoente do dez conta os zeros. [p=0.5] "
        "{b}Dois: [p=0.2] multiplicou, [p=0.2] soma os expoentes. [p=0.2] Dividiu, [p=0.2] subtrai. [p=0.5] {c}Três: "
        "[p=0.2] o expoente de fora pega todos os fatores de dentro."),

    # ================= PONTE E CTA =================
    dict(id="27", block="ponte", text=
        "{a}Potência é o caminho de *ida.* [p=0.3] {b}E o caminho de volta? [p=0.3] {c}Se nove ao quadrado é oitenta e "
        "um, [p=0.2] *quem desfaz isso?* [p=0.4] {d}Próximo episódio: [p=0.2] *a raiz.*"),
    dict(id="28", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você fez a conta do milhão de cabeça? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
