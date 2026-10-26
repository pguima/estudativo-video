# Roteiro — Unidades de Medida e Conversões, Episódio 4 de 5: Análise dimensional, o método que nunca falha, e as unidades
#   de fora do sistema métrico
# Base: Estudos/Enem/estudos/01-matematica/10-unidades-conversoes.html — seções 09 e 10 + Questões 5 e 8.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na revisão):
#   Uma fração de conversão vale 1, como trocar uma nota de 100 por dez de 10: muda a forma, não o valor.
#   As unidades se cancelam como números numa fração: risque km com km, h com h; o que sobra é a resposta.
#   O método se confere sozinho: se não sobrou a unidade que você queria, alguma fração está de cabeça para baixo.
#   kWh é ENERGIA, não potência: potência × tempo, como litros = vazão × tempo.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte.
# Exemplos dos blocos: 72 km/h → 20 m/s (exemplo do material; a Q4 com esse número já foi do ep3) · versão errada
#   72 km/h · (1 km/1 000 m) → nada cancela · alumínio 2,7 g/cm³ → 2 700 kg/m³ (o porquê do × 1 000 prometido no ep3) ·
#   milha: 10 mi · 1,6 km/mi = 16 km · chuveiro de 5 kW por 12 min = 1 kWh (do material). Nenhum usa 0,8 g/cm³ (Q5) nem
#   50 polegadas (Q8).
# Nós fazemos (prompt): 18 km/h = 5 m/s · TV de 40 polegadas = 40 · 2,54 = 101,6 cm.
# QUESTÃO 5: 0,8 · (1 kg/1 000 g) · (1 000 000 cm³/1 m³) = 800 kg/m³ → D. Conferência pela água: 1 g/cm³ = 1 000 kg/m³;
#   o óleo é menos denso e dá menos que 1 000: coerente (boia na água). O material não explica as erradas. NOSSAS:
#   A (0,0008) converteu só o andar de cima (g → kg) e esqueceu o cm³ · E (800 000) converteu só o andar de baixo e esqueceu
#   o g · B (0,8) não converteu nada · C (80) usou o fator do comprimento (100) em vez do volume.
# QUESTÃO 8: 50 · 2,54 = 127 cm → C. Material: A (19,7) dividiu em vez de multiplicar. NOSSAS: B (52,5) somou 50 + 2,5 ·
#   D (254) usou 100 polegadas · E (1 270) deu a resposta em milímetros (127 cm = 1 270 mm), mas a pergunta é em centímetros.
# Atalhos (verde): "a unidade que você quer eliminar vai no andar oposto" · "a polegada é maior que o centímetro: o número em
#   cm tem de crescer" · "kWh = kW × horas: minutos viram hora antes (12 min = 0,2 h)".
# Frases-chave (meio e fim, idênticas): 1. Multiplique por frações que valem 1. 2. Risque as unidades; o que sobra é a
#   resposta. 3. Unidade de fora? A prova te dá o fator: use-o.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Análise dimensional: converta sem decorar fatores | Unidades de Medida Ep. 4"
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
        "{a}Esqueceu o três vírgula seis? [p=0.3] {b}Não lembra se multiplica ou divide? [p=0.5] {c}Existe um método que "
        "*dispensa decorar fatores* [p=0.2] {d}e ainda *avisa* quando você errou."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai converter qualquer unidade composta [p=0.2] deixando as unidades se "
        "cancelarem, [p=0.3] {b}e usar qualquer fator que o enunciado der."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Do episódio três: [p=0.2] quilômetro por hora é uma fração de dois "
        "andares, [p=0.2] e de quilômetro por hora para metro por segundo [p=0.2] se divide por *três vírgula seis.* "
        "[p=0.4] {b}E da série de Frações: [p=0.2] um número igual em cima e embaixo *se cancela.* [p=0.3] Seis sobre "
        "seis [p=0.2] vale *um.*"),

    # ================= CONCRETO =================
    dict(id="04", block="cotidiano", text=
        "{t}Primeiro, uma troca de dinheiro. [p=0.3] {a}Você entrega uma nota de *cem reais* [p=0.2] e recebe *dez notas "
        "de dez.* [p=0.4] {b}Ficou mais rico? [p=0.3] Não. [p=0.2] Mudou a *forma,* [p=0.2] não o *valor.* [p=0.5] {c}E repare nas unidades estrangeiras do dia a dia: [p=0.2] a TV em *polegadas,* "
        "[p=0.2] a altitude do avião em *pés,* [p=0.2] o chuveiro e a conta de luz em *quilowatt* [p=0.2] e "
        "*quilowatt-hora.*"),

    # ================= BLOCO A: A FRAÇÃO QUE VALE 1 =================
    dict(id="05", block="vale1", text=
        "{t}Qual é a ideia por trás da troca de notas? [p=0.4] {a}Olhe esta fração: [p=0.2] *mil metros* em cima, [p=0.2] "
        "*um quilômetro* embaixo. [p=0.4] {b}Mil metros e um quilômetro são a *mesma* distância. [p=0.3] Então essa "
        "fração vale *um.* [p=0.4] {c}Ela se chama *fração de conversão:* [p=0.2] uma fração que vale um, [p=0.2] com "
        "unidades diferentes em cima e embaixo. [p=0.4] {d}E multiplicar por um [p=0.2] não muda o valor de nada."),
    dict(id="06", block="vale1", text=
        "{t}E o que acontece com as unidades? [p=0.4] {a}Elas se comportam como números numa fração. [p=0.3] Se aparece "
        "quilômetro em cima e quilômetro embaixo, [p=0.2] eles *se cancelam:* [p=0.2] você *risca* os dois. [p=0.4] {b}Esse "
        "método se chama *análise dimensional:* [p=0.2] converter multiplicando por frações que valem um, [p=0.2] e "
        "deixar as unidades se riscarem."),

    # ================= BLOCO B: EU FAÇO 72 KM/H =================
    dict(id="07", block="cadeia", text=
        "{t}Vamos fazer juntos, [p=0.2] devagar. [p=0.3] Setenta e dois quilômetros por hora, [p=0.2] em metros por "
        "segundo. [p=0.4] {a}Escreva setenta e dois quilômetros em cima, [p=0.2] hora embaixo. [p=0.4] {b}Primeiro, "
        "quero me livrar do *quilômetro,* [p=0.2] que está em cima. [p=0.3] Então multiplico por uma fração com "
        "quilômetro *embaixo:* [p=0.2] mil metros sobre um quilômetro. [p=0.4] {c}Quilômetro em cima, quilômetro "
        "embaixo: [p=0.2] *risca.*"),
    dict(id="08", block="cadeia", text=
        "{t}Agora, a *hora,* [p=0.2] que está embaixo. [p=0.3] {a}Multiplico por uma fração com hora *em cima:* [p=0.2] "
        "uma hora sobre três mil e seiscentos segundos. [p=0.4] {b}Hora embaixo, hora em cima: [p=0.2] *risca.* [p=0.4] "
        "{c}O que sobrou? [p=0.2] *Metro* em cima, [p=0.2] *segundo* embaixo. [p=0.2] Exatamente o que eu queria. [p=0.4] "
        "{d}A conta: [p=0.2] setenta e dois vezes mil, [p=0.2] dividido por três mil e seiscentos: [p=0.2] *vinte* "
        "metros por segundo."),

    # ================= BLOCO C: O MÉTODO SE CONFERE SOZINHO =================
    dict(id="09", block="confere", text=
        "{t}E por que esse método é tão confiável? [p=0.4] {a}Veja o que acontece se eu montar uma fração *de cabeça para "
        "baixo:* [p=0.2] um quilômetro sobre mil metros. [p=0.4] {b}Quilômetro em cima [p=0.2] e quilômetro em cima de "
        "novo. [p=0.3] *Nada se cancela.* [p=0.4] {c}Sobra quilômetro ao quadrado sobre metro e hora: [p=0.2] sem sentido. [p=0.4] {d}É o aviso: [p=0.2] *alguma fração está de cabeça para baixo.* [p=0.3] Você descobre o erro "
        "*antes* de fazer qualquer conta."),
    dict(id="10", block="confere", text=
        "{t}E como montar certo de primeira? [p=0.4] {a}Atalho: [p=0.2] a unidade que você quer *eliminar* [p=0.2] vai no "
        "*andar oposto.* [p=0.4] {b}Quilômetro está em cima? [p=0.2] A fração leva quilômetro embaixo. [p=0.3] Hora está "
        "embaixo? [p=0.2] A fração leva hora em cima."),

    # ================= BLOCO D: TRÊS OU MAIS UNIDADES =================
    dict(id="11", block="densidade", text=
        "{t}Quando esse método vale ouro? [p=0.4] {a}Quando a unidade mistura várias coisas. [p=0.4] {b}Lembra do alumínio do episódio passado? [p=0.2] *Dois vírgula sete gramas por centímetro "
        "cúbico,* [p=0.2] em quilos por metro cúbico. [p=0.4] {c}Para eliminar o grama: [p=0.2] um quilo sobre mil gramas. "
        "[p=0.4] {d}Para eliminar o centímetro cúbico: [p=0.2] *um milhão* de centímetros cúbicos sobre um metro cúbico, "
        "[p=0.2] o cubo de cubinhos do episódio dois."),
    dict(id="12", block="densidade", text=
        "{t}Risca grama com grama. [p=0.2] Risca centímetro cúbico com centímetro cúbico. [p=0.4] {a}Sobra quilo sobre "
        "metro cúbico. [p=0.4] {b}E a conta: [p=0.2] dois vírgula sete, [p=0.2] vezes um milhão, [p=0.2] dividido por "
        "mil. [p=0.3] *Dois mil e setecentos.* [p=0.4] {c}Aí está o porquê daquele *vezes mil:* [p=0.2] um milhão "
        "dividido por mil."),

    # ================= BLOCO E: UNIDADES DE FORA =================
    dict(id="13", block="fora", text=
        "{t}E as unidades que não são do sistema métrico? [p=0.4] {a}Elas vêm de outros países. [p=0.4] {b}A *polegada* vale dois vírgula cinquenta e quatro centímetros. [p=0.2] O *pé,* "
        "[p=0.2] uns trinta centímetros e meio. [p=0.2] A *milha,* [p=0.2] um vírgula seis quilômetro. [p=0.4] {c}A "
        "*libra,* [p=0.2] uns quarenta e cinco centésimos de quilo. [p=0.2] O *galão,* [p=0.2] quase três litros e oito "
        "décimos. [p=0.4] {d}E a *caloria,* [p=0.2] que mede energia, [p=0.2] vale uns quatro *joules,* [p=0.2] a "
        "unidade oficial de energia."),
    dict(id="14", block="fora", text=
        "{t}Precisa decorar essa tabela? [p=0.3] *Não.* [p=0.4] {a}O ponto importante é este: [p=0.2] a prova *sempre* "
        "te dá o fator. [p=0.3] A habilidade é *usar.* [p=0.4] {b}Uma corrida de *dez milhas,* [p=0.2] com uma milha "
        "igual a um vírgula seis quilômetro. [p=0.3] Dez milhas, [p=0.2] vezes um vírgula seis quilômetro sobre uma "
        "milha. [p=0.3] Risca a milha: [p=0.2] *dezesseis quilômetros.*"),

    # ================= BLOCO F: CONFERÊNCIA DE SENTIDO =================
    dict(id="15", block="sentido", text=
        "{t}E como saber se multiplica ou divide pelo fator? [p=0.4] {a}Pense no tamanho. [p=0.3] Uma polegada é "
        "*maior* que um centímetro: [p=0.2] cabem dois centímetros e meio dentro dela. [p=0.4] {b}Então, passando de "
        "polegada para centímetro, [p=0.2] o número tem que *crescer.* [p=0.4] {c}Atalho: [p=0.2] de unidade grande para "
        "pequena, [p=0.2] o número cresce. [p=0.2] Se diminuiu, [p=0.2] você dividiu quando devia multiplicar."),

    # ================= BLOCO G: O QUILOWATT-HORA =================
    dict(id="16", block="kwh", text=
        "{t}E o quilowatt-hora da conta de luz? [p=0.4] {a}Primeiro, duas palavras. [p=0.3] *Potência* é a rapidez com "
        "que um aparelho gasta energia. [p=0.2] Ela é medida em *quilowatt.* [p=0.4] {b}*Energia* é o total que ele "
        "gastou. [p=0.3] {c}E o quilowatt-hora é energia: [p=0.2] um aparelho de um quilowatt [p=0.2] ligado por uma "
        "hora. [p=0.4] {d}Como os litros da torneira são vazão vezes tempo, [p=0.2] quilowatt-hora é *potência vezes tempo.*"),
    dict(id="17", block="kwh", text=
        "{t}Um exemplo. [p=0.3] {a}Um chuveiro de *cinco quilowatts,* [p=0.2] ligado por *doze minutos.* [p=0.4] {b}Doze "
        "minutos em horas: [p=0.2] doze sobre sessenta, [p=0.2] *zero vírgula dois* hora. [p=0.4] {c}Cinco quilowatts "
        "vezes zero vírgula dois hora: [p=0.2] *um quilowatt-hora.* [p=0.4] {d}Atalho: [p=0.2] quilowatt-hora é "
        "quilowatt vezes *horas.* [p=0.2] Minutos viram hora antes."),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez. [p=0.2] Duas conversões. [p=0.3] {a}Por análise dimensional: [p=0.2] *dezoito quilômetros por hora* "
        "em metros por segundo. [p=0.4] {b}E uma TV de *quarenta polegadas:* [p=0.2] quantos centímetros tem a "
        "diagonal? [p=0.2] Uma polegada vale dois vírgula cinquenta e quatro centímetros. [p=0.4] {c}*Pause o vídeo e "
        "converta.* [p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Dezoito, [p=0.2] vezes mil metros sobre um quilômetro, [p=0.2] vezes uma hora "
        "sobre três mil e seiscentos segundos. [p=0.3] Risca quilômetro, [p=0.2] risca hora: [p=0.2] *cinco* metros por "
        "segundo. [p=0.4] {b}Quarenta vezes dois vírgula cinquenta e quatro: [p=0.2] *cento e um vírgula seis* "
        "centímetros. [p=0.3] Cresceu, [p=0.2] como tinha que ser."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] multiplique por frações que valem um. [p=0.5] {b}Dois: "
        "[p=0.2] risque as unidades; [p=0.2] o que sobra é a resposta. [p=0.5] {c}Três: [p=0.2] unidade de fora? [p=0.2] "
        "A prova te dá o fator: [p=0.2] use-o."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Agora, os quatro erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] montar a fração de conversão *de cabeça para "
        "baixo.* [p=0.4] {b}Parece certo, [p=0.2] porque os números são os mesmos, [p=0.2] mil e um. [p=0.4] {c}Mas as "
        "unidades não se cancelam. [p=0.2] Confira: [p=0.2] a unidade a eliminar vai no andar oposto."),
    dict(id="22", block="erros", text=
        "{a}Segundo: [p=0.2] converter *só o numerador.* [p=0.2] Passar grama por centímetro cúbico para quilo por metro "
        "cúbico [p=0.2] mudando só o grama. [p=0.4] {b}Parece certo, [p=0.2] porque o quilo apareceu. [p=0.4] {c}Mas o centímetro cúbico continua lá. [p=0.2] Os *dois* andares mudam."),
    dict(id="23", block="erros", text=
        "{a}Terceiro: [p=0.2] *dividir* pelo fator da polegada [p=0.2] em vez de multiplicar. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque dividir parece o caminho natural. [p=0.4] {c}Mas a polegada é maior "
        "que o centímetro: [p=0.2] o número em centímetros tem que *crescer.*"),
    dict(id="24", block="erros", text=
        "{a}Quarto: [p=0.2] achar que quilowatt-hora é *potência.* [p=0.4] {b}Parece certo, [p=0.2] porque tem quilowatt "
        "no nome. [p=0.4] {c}Mas o hora no final muda tudo: [p=0.2] é potência *vezes tempo.* [p=0.2] Quilowatt-hora é "
        "*energia.*"),

    # ================= QUESTÃO 5 =================
    dict(id="25", block="q5", text=
        "{t}Agora, as questões do material. [p=0.4] {a}Um óleo vegetal tem densidade "
        "de *zero vírgula oito grama por centímetro cúbico.* [p=0.3] {b}Essa densidade, [p=0.2] expressa em quilogramas "
        "por metro cúbico, [p=0.2] corresponde a: [p=0.4] {qa}A: [p=0.2] zero vírgula zero zero zero oito. [p=0.3] "
        "{qb}B: [p=0.2] zero vírgula oito. [p=0.3] {qc}C: [p=0.2] oitenta. [p=0.3] {qd}D: [p=0.2] oitocentos. [p=0.3] "
        "{qe}E: [p=0.2] oitocentos mil. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="26", block="q5", text=
        "{t}Vamos resolver, [p=0.2] riscando. [p=0.3] {a}Zero vírgula oito, [p=0.2] vezes um quilo sobre mil gramas: "
        "[p=0.2] risca o grama. [p=0.4] {b}Vezes um milhão de centímetros cúbicos sobre um metro cúbico: [p=0.2] risca o "
        "centímetro cúbico. [p=0.4] {c}Zero vírgula oito vezes um milhão, [p=0.2] dividido por mil: [p=0.2] "
        "*oitocentos* quilos por metro cúbico. [p=0.3] {ok}*Letra D!* [p=0.4] {d}Conferência pela água: [p=0.2] um "
        "grama por centímetro cúbico [p=0.2] são mil quilos por metro cúbico. [p=0.3] O óleo é *menos* denso, [p=0.2] e "
        "deu menos que mil. [p=0.2] Coerente: [p=0.2] é por isso que ele boia."),
    dict(id="27", block="q5", text=
        "{t}E as outras? [p=0.3] {xa}A A converteu *só o andar de cima:* [p=0.2] o grama virou quilo, [p=0.2] e o "
        "centímetro cúbico ficou. [p=0.4] {xe}A E fez o contrário: [p=0.2] *só o andar de baixo.* [p=0.4] {xb}A B não "
        "converteu nada. [p=0.4] {xc}E a C usou o fator do comprimento, [p=0.2] cem, [p=0.2] num volume."),

    # ================= QUESTÃO 8 =================
    dict(id="28", block="q8", text=
        "{t}A última. [p=0.3] {a}Uma televisão é anunciada como tendo *cinquenta polegadas* de diagonal. [p=0.3] "
        "{b}Considerando que uma polegada equivale a dois vírgula cinquenta e quatro centímetros, [p=0.2] a diagonal "
        "dessa televisão mede, em centímetros: [p=0.4] {qa}A: [p=0.2] dezenove vírgula sete. [p=0.3] {qb}B: [p=0.2] "
        "cinquenta e dois vírgula cinco. [p=0.3] {qc}C: [p=0.2] cento e vinte e sete. [p=0.3] {qd}D: [p=0.2] duzentos e "
        "cinquenta e quatro. [p=0.3] {qe}E: [p=0.2] mil duzentos e setenta. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="29", block="q8", text=
        "{t}O enunciado já te deu o fator. [p=0.3] {a}Cinquenta polegadas, [p=0.2] vezes dois vírgula cinquenta e quatro "
        "centímetros sobre uma polegada. [p=0.3] Risca a polegada. [p=0.4] {b}Cinquenta vezes dois vírgula cinquenta e "
        "quatro: [p=0.2] *cento e vinte e sete* centímetros. [p=0.3] {ok}*Letra C!* [p=0.3] Uma TV grande: [p=0.2] plausível. [p=0.4] {xa}A A *dividiu:* [p=0.2] o número diminuiu, [p=0.2] e não "
        "podia. [p=0.4] {xb}A B somou. [p=0.3] {xd}A D usou cem polegadas. [p=0.3] {xe}E a E deu a resposta em "
        "*milímetros,* [p=0.2] mas a pergunta é em centímetros."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] multiplique por frações que valem um. [p=0.5] "
        "{b}Dois: [p=0.2] risque as unidades; [p=0.2] o que sobra é a resposta. [p=0.5] {c}Três: [p=0.2] unidade de "
        "fora? [p=0.2] A prova te dá o fator: [p=0.2] use-o."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos tudo, [p=0.2] {b}caçamos as pegadinhas [p=0.2] {c}e "
        "treinamos com questões de Matemática, Física e Química."),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] quantos centímetros tem a diagonal da sua TV? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
