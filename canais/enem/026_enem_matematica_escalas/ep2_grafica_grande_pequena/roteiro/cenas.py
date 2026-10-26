# Roteiro — Escalas, Plantas e Mapas, Episódio 2 de 4: escala gráfica × numérica e escala grande × pequena
# Base: Estudos/Enem/estudos/01-matematica/11-escalas-plantas-mapas.html — seções 03 e 04 + Questões 8 e 4.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Revisão com foco em Matemática da Cartografia ep. 1 (012): mesma analogia do ZOOM DO CELULAR
#   (zoom aproximado = escala grande, ruas · zoom afastado = escala pequena, só o contorno do país).
# Analogias âncora:
#   A BARRA GRÁFICA é uma régua que VIAJA com o mapa: amplie a cópia e a régua cresce junto; o número impresso fica para trás.
#   Escala como FRAÇÃO: 1/10 000 é maior que 1/10 000 000, como 1/2 é maior que 1/20.
# Frases do usuário mantidas IGUAIS: gancho, promessa (com "Ao final desta aula"), as 3 frases-chave e a ponte.
# Exemplos: a Questão 8 (barra de 4 cm = 10 km) tem "pause e tente", então o bloco c usa um exemplo NOSSO:
#   barra de 3 cm = 6 km → 600 000 cm → 3 / 600 000 = 1 / 200 000 (atalho: 6 km ÷ 3 cm = 2 km por cm → põe 5 zeros → 200 000).
#   Fotocópia: 1 : 50 000 reduzido à metade → 1 : 100 000 (material) · ampliado ao dobro → 1 : 25 000 (NOSSO).
#   Nós fazemos (prompt): barra de 2 cm = 5 km → 500 000 cm → 1 : 250 000 (mesmo resultado da Q8, com dados diferentes).
# QUESTÃO 8 (material): 10 km = 1 000 000 cm → 4 / 1 000 000 = 1 / 250 000 → C. Explicações NOSSAS das erradas:
#   A (1 : 2 500) = parou nos metros (4 / 10 000) · B (1 : 25 000) = usou 100 000 cm (um zero a menos) ·
#   D (1 : 400 000) = multiplicou 4 × 100 000 em vez de dividir · E (1 : 2 500 000) = um zero a mais (10 000 000 cm).
# QUESTÃO 4 (material): ruas de um bairro, mais detalhe = menor denominador → A (1 : 10 000; 1 cm = 100 m).
#   Material: em 1 : 10 000 000, 1 cm = 100 km e o bairro vira um ponto. NOSSO: E é a de quem acha que número maior é escala maior.
# Atalhos (verde): "ampliou: divida o denominador; reduziu: multiplique" · "km por cm, depois cinco zeros" ·
#   "na dúvida, leia como fração".
# Frases-chave (meio e fim, idênticas): 1. A barra gráfica viaja com o mapa; o número não. 2. Escala grande: zoom aproximado,
#   mais detalhe. 3. Denominador menor, escala maior.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Escala gráfica e escala numérica: o que sobrevive à fotocópia | Escalas Ep. 2"
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
        "{a}Um mapa *um para cinquenta mil* [p=0.2] reduzido à metade na fotocópia [p=0.2] continua dizendo um para "
        "cinquenta mil, [p=0.3] {b}mas agora está *errado.* [p=0.5] {c}E uma barrinha desenhada no canto [p=0.2] continua "
        "*certa.* [p=0.5] {d}Por quê?"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai converter uma *escala gráfica* em *numérica* [p=0.3] {b}e escolher o "
        "*mapa certo* para cada situação."),
    dict(id="03", block="prereq", text=
        "{t}Se você viu a aula de Cartografia, [p=0.2] isto é uma revisão com foco em Matemática. [p=0.4] {a}Do "
        "episódio passado, [p=0.2] dois lembretes. [p=0.3] Toda questão de escala pede uma de três coisas: [p=0.2] a medida "
        "*real,* [p=0.2] a medida no *desenho,* [p=0.2] ou a própria *escala.* [p=0.4] {b}E de centímetro para quilômetro "
        "[p=0.2] você divide por *cem mil:* [p=0.2] corta cinco zeros."),

    # ================= CONCRETO =================
    dict(id="04", block="celular", text=
        "{t}Abra o mapa do celular, [p=0.2] na sua cabeça. [p=0.4] {a}Aproxime o zoom: [p=0.2] aparecem as ruas "
        "e as casas. [p=0.4] {b}Afaste: [p=0.2] as ruas somem, [p=0.2] e só cabe o *contorno do país.* "
        "[p=0.4] {c}E repare no cantinho da tela: [p=0.2] tem uma *barrinha* com uma distância escrita, [p=0.2] que muda "
        "junto com o zoom."),

    # ================= BLOCO A: NUMÉRICA × GRÁFICA =================
    dict(id="05", block="tipos", text=
        "{t}Dois jeitos de escrever uma escala. [p=0.4] {a}A *escala numérica* [p=0.2] é a escala escrita com "
        "números, [p=0.2] como um para cinquenta mil. [p=0.3] Vantagem: [p=0.2] é *direta* para calcular. [p=0.4] {b}A "
        "*escala gráfica* [p=0.2] é uma *barra graduada:* [p=0.2] um tracinho desenhado no mapa, [p=0.2] com as distâncias "
        "marcadas em cima. [p=0.3] Vantagem: [p=0.2] continua valendo em *qualquer* ampliação. [p=0.4] {c}Limitações: "
        "[p=0.2] a numérica falha se o mapa muda de tamanho; [p=0.2] a gráfica exige *régua.*"),

    # ================= BLOCO B: A FOTOCÓPIA =================
    dict(id="06", block="copia", text=
        "{t}Por que o número fica errado na fotocópia? [p=0.4] {a}No mapa original, [p=0.2] "
        "um para cinquenta mil, [p=0.2] *um centímetro* vale cinquenta mil centímetros: [p=0.2] *meio quilômetro.* [p=0.4] "
        "{b}Reduza a cópia à metade. [p=0.2] Aquele centímetro encolhe para *meio centímetro,* [p=0.2] mas continua "
        "valendo meio quilômetro. [p=0.4] {c}Então um centímetro inteiro da cópia [p=0.2] vale *um quilômetro:* [p=0.2] "
        "cem mil centímetros. [p=0.4] {d}A escala de verdade virou *um para cem mil.*"),
    dict(id="07", block="copia", text=
        "{t}E a barrinha? [p=0.3] {a}Ela foi *encolhida junto* com o resto do mapa. [p=0.4] {b}E se você *ampliar* a "
        "cópia para o dobro? [p=0.2] O mapa cresce, [p=0.2] e a barra cresce junto: [p=0.2] *continua certa.* [p=0.4] "
        "{c}O número impresso fica igual: [p=0.2] *agora está errado.* [p=0.4] {d}A barra gráfica é uma *régua que viaja* "
        "com o mapa. [p=0.2] O número fica para trás."),
    dict(id="08", block="copia", text=
        "{t}Dá para corrigir o número? [p=0.3] {a}Atalho: [p=0.2] *ampliou, divida o denominador;* [p=0.2] "
        "*reduziu, multiplique.* [p=0.4] {b}Ampliou duas vezes o um para cinquenta mil? [p=0.2] Cinquenta mil dividido "
        "por dois: [p=0.2] *um para vinte e cinco mil.* [p=0.4] {c}Reduziu à metade? [p=0.2] Vezes dois: [p=0.2] *um para "
        "cem mil.*"),

    # ================= BLOCO C: CONVERTER GRÁFICA EM NUMÉRICA =================
    dict(id="09", block="converter", text=
        "{t}Agora, o novo: [p=0.2] como transformar a barrinha em número? [p=0.4] {a}Um mapa traz uma barra de "
        "*três centímetros,* [p=0.2] com *seis quilômetros* escritos em cima. [p=0.4] {b}Passo um: [p=0.2] meça a barra "
        "com a régua: [p=0.2] três centímetros. [p=0.4] {c}Passo dois: [p=0.2] passe o real para a *mesma unidade,* "
        "[p=0.2] centímetros. [p=0.2] Seis quilômetros, [p=0.2] vezes cem mil: [p=0.2] "
        "*seiscentos mil centímetros.* [p=0.4] {d}Passo três: [p=0.2] monte a escala, [p=0.2] desenho sobre real: "
        "[p=0.2] três sobre seiscentos mil."),
    dict(id="10", block="converter", text=
        "{t}Falta deixar o número de cima igual a *um.* [p=0.4] {a}Divida em cima e embaixo por *três:* [p=0.2] três "
        "dividido por três, [p=0.2] um. [p=0.2] Seiscentos mil dividido por três, [p=0.2] duzentos mil. [p=0.4] {b}Escala: "
        "[p=0.2] *um para duzentos mil.* [p=0.4] {c}Atalho, [p=0.2] o caminho de volta dos cinco zeros: [p=0.2] seis "
        "quilômetros em três centímetros [p=0.2] são *dois quilômetros por centímetro.* [p=0.2] Ponha cinco zeros no dois: "
        "[p=0.2] *duzentos mil.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="11", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Uma barra de *dois centímetros* vale *cinco quilômetros.* [p=0.3] Qual é a escala "
        "numérica? [p=0.4] {b}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="12", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Cinco quilômetros [p=0.2] são cinco mil metros, [p=0.2] *quinhentos mil "
        "centímetros.* [p=0.4] {b}Desenho sobre real: [p=0.2] dois sobre quinhentos mil. [p=0.3] Divida os dois por dois: "
        "[p=0.2] *um para duzentos e cinquenta mil.* [p=0.4] {c}Pelo atalho: [p=0.2] dois vírgula cinco quilômetros por centímetro, "
        "[p=0.2] mais cinco zeros: [p=0.2] duzentos e cinquenta mil. [p=0.2] Bateu."),

    # ================= BLOCO D: ESCALA GRANDE × PEQUENA =================
    dict(id="13", block="zoom", text=
        "{t}Agora: [p=0.2] escala grande ou pequena? [p=0.4] {a}Volte ao celular. [p=0.2] No "
        "bairro, [p=0.2] o canto da tela diz algo como *um para cinco mil.* [p=0.4] {b}Afaste até o país inteiro: [p=0.2] "
        "*um para vinte milhões.* [p=0.4] {c}*Escala grande* [p=0.2] é o zoom aproximado: [p=0.2] dá para ver as ruas. "
        "[p=0.3] *Escala pequena* [p=0.2] é o zoom afastado: [p=0.2] só cabe o contorno do país."),
    dict(id="14", block="zoom", text=
        "{t}O que muda? [p=0.3] {a}O *detalhe:* [p=0.2] o quanto de coisa pequena dá para enxergar no mapa, "
        "[p=0.2] como uma rua ou uma casa. [p=0.4] {b}Escala grande: [p=0.2] *mais* detalhe, [p=0.2] *menos* território. "
        "[p=0.4] {c}Escala pequena: [p=0.2] *menos* detalhe, [p=0.2] *mais* território. [p=0.4] {d}E a regra que parece "
        "invertida: [p=0.2] *denominador menor, [p=0.2] escala maior.*"),

    # ================= BLOCO E: O RACIOCÍNIO DA FRAÇÃO =================
    dict(id="15", block="fracao", text=
        "{t}Parece invertido? [p=0.2] Não é. [p=0.3] {a}Leia a escala como *fração:* [p=0.2] um sobre dez mil, [p=0.2] "
        "e um sobre dez milhões. [p=0.4] {b}Qual é maior, [p=0.2] um meio ou um vinte avos? [p=0.3] Metade de uma pizza "
        "[p=0.2] é muito mais que um pedacinho de vinte. [p=0.4] {c}Com a escala é igual: [p=0.2] *um sobre dez mil é "
        "maior* que um sobre dez milhões. [p=0.4] {d}Atalho: [p=0.2] na dúvida, [p=0.2] *leia como fração.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="16", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] a barra gráfica viaja com o mapa; [p=0.2] o número não. "
        "[p=0.5] {b}Dois: [p=0.2] escala grande: [p=0.2] zoom aproximado, [p=0.2] mais detalhe. [p=0.5] {c}Três: [p=0.2] "
        "denominador menor, [p=0.2] escala maior."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="17", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que um para duzentos e cinquenta mil "
        "[p=0.2] é *maior* que um para cinquenta mil. [p=0.4] {b}Parece certo, [p=0.2] porque duzentos e cinquenta mil é "
        "um número maior. [p=0.4] {c}Mas ele está *embaixo* da fração. [p=0.2] Denominador maior, [p=0.2] escala "
        "*menor.*"),
    dict(id="18", block="erros", text=
        "{a}Segundo: [p=0.2] confiar na escala numérica [p=0.2] de um mapa *ampliado* ou *reduzido.* [p=0.4] {b}Parece "
        "certo, [p=0.2] porque o número está impresso ali, [p=0.2] com cara de oficial. [p=0.4] {c}Mas ele não mudou "
        "junto com o papel. [p=0.2] Use a *barra gráfica.*"),
    dict(id="19", block="erros", text=
        "{a}Terceiro: [p=0.2] converter a barra *sem igualar as unidades.* [p=0.2] Barra de quatro centímetros, [p=0.2] "
        "dez quilômetros: [p=0.2] quatro para dez. [p=0.4] {b}Parece certo, [p=0.2] porque os dois números estão "
        "escritos ali, [p=0.2] prontinhos. [p=0.4] {c}Mas um é centímetro [p=0.2] e o outro é quilômetro. [p=0.2] Passe tudo "
        "para *centímetros* antes."),

    # ================= QUESTÃO 8 DO MATERIAL =================
    dict(id="20", block="q8", text=
        "{t}Agora, questões do nosso material, [p=0.2] no estilo do ENEM. [p=0.4] {a}Em um mapa, [p=0.2] a escala "
        "gráfica é uma barra de *quatro centímetros,* [p=0.2] correspondente a *dez quilômetros* no terreno. [p=0.4] {b}A "
        "escala numérica desse mapa é: [p=0.4] {qa}A: [p=0.2] um para dois mil e quinhentos. [p=0.3] {qb}B: [p=0.2] um para "
        "vinte e cinco mil. [p=0.3] {qc}C: [p=0.2] um para duzentos e cinquenta mil. [p=0.3] {qd}D: [p=0.2] um para "
        "quatrocentos mil. [p=0.3] {qe}E: [p=0.2] um para dois milhões e quinhentos mil. [p=0.5] {p}*Pause o vídeo e "
        "tente.* [p=2.0]"),
    dict(id="21", block="q8", text=
        "{t}Vamos resolver. [p=0.3] {a}Dez quilômetros: [p=0.2] dez mil metros, [p=0.2] *um milhão de centímetros.* "
        "[p=0.4] {b}Desenho sobre real: [p=0.2] quatro sobre um milhão. [p=0.2] Divida os dois por quatro: [p=0.2] *um "
        "para duzentos e cinquenta mil.* [p=0.4] {c}Confira pelo atalho: [p=0.2] em um para duzentos e cinquenta mil, "
        "[p=0.2] cada centímetro vale dois vírgula cinco quilômetros. [p=0.2] Quatro centímetros, [p=0.2] dez quilômetros. "
        "[p=0.3] {ok}*Letra C!*"),
    dict(id="22", block="q8", text=
        "{t}E as outras? [p=0.3] {xa}A A [p=0.2] parou nos *metros:* [p=0.2] quatro sobre dez mil. [p=0.4] {xb}A B usou "
        "cem mil centímetros: [p=0.2] *um zero a menos.* [p=0.4] {xe}A E usou dez milhões: [p=0.2] *um zero a mais.* "
        "[p=0.4] {xd}E a D *multiplicou* quatro por cem mil, [p=0.2] em vez de dividir."),

    # ================= QUESTÃO 4 DO MATERIAL =================
    dict(id="23", block="q4", text=
        "{t}Próxima. [p=0.3] {a}Um estudante precisa de um mapa que mostre, [p=0.2] com o *maior nível de detalhe "
        "possível,* [p=0.2] as *ruas de um bairro.* [p=0.3] {b}Ele deve escolher a escala: [p=0.4] {qa}A: [p=0.2] um para "
        "dez mil. [p=0.3] {qb}B: [p=0.2] um para cem mil. [p=0.3] {qc}C: [p=0.2] um para quinhentos mil. [p=0.3] "
        "{qd}D: [p=0.2] um para um milhão. [p=0.3] {qe}E: [p=0.2] um para dez milhões. [p=0.5] {p}*Pause o vídeo e "
        "tente.* [p=2.0]"),
    dict(id="24", block="q4", text=
        "{t}Vamos lá. [p=0.3] {a}Mais detalhe [p=0.2] é escala *maior,* [p=0.2] zoom aproximado. [p=0.2] E escala maior "
        "[p=0.2] é *denominador menor:* [p=0.2] dez mil. [p=0.4] {b}Confira: [p=0.2] em um para dez mil, [p=0.2] cada "
        "centímetro vale *cem metros.* [p=0.2] Dá para ver quadras e ruas. [p=0.3] {ok}*Letra A!* [p=0.4] {xe}A E é a "
        "pegadinha: [p=0.2] quem acha que número maior é escala maior. [p=0.2] Em um para dez milhões, [p=0.2] cada "
        "centímetro vale *cem quilômetros,* [p=0.2] e o bairro vira um pontinho. [p=0.4] {xb}As outras: [p=0.2] zoom afastado demais."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="25", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] a barra gráfica viaja com o mapa; [p=0.2] o número "
        "não. [p=0.5] {b}Dois: [p=0.2] escala grande: [p=0.2] zoom aproximado, [p=0.2] mais detalhe. [p=0.5] {c}Três: "
        "[p=0.2] denominador menor, [p=0.2] escala maior."),

    # ================= PONTE E CTA =================
    dict(id="26", block="ponte", text=
        "{a}Numa planta *um para duzentos,* [p=0.2] um centímetro quadrado do papel [p=0.2] vale quanto na vida real? "
        "[p=0.5] {b}Se você respondeu duzentos centímetros quadrados, [p=0.2] errou por um fator de *duzentos.* [p=0.4] "
        "{c}Próximo episódio: [p=0.2] plantas e maquetes."),
    dict(id="27", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha reparado na barrinha do mapa do celular? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
