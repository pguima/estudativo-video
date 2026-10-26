# Roteiro — Grandezas Proporcionais, Episódio 5 de 6: Quando dobrar não dobra (quadrática, cúbica e inverso do quadrado)
# Base: Estudos/Enem/estudos/01-matematica/07-grandezas-proporcionais.html — seção 07 (+ Questões 8 e 6 da seção 12).
# A área que quadruplica já apareceu na série de Razão (ep5): aqui, revisão rápida; o foco novo é a tabela completa e o
# INVERSO DO QUADRADO, explicado com a lanterna (a mesma luz espalhada sobre 4 e 9 quadrados).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora:
#   QUADRÁTICA = dobrar o lado de um piso exige 4 vezes mais azulejos (dois de largura × dois de comprimento).
#   CÚBICA = dobrar a aresta de uma caixa cabe 8 vezes mais cubinhos.
#   INVERSO DO QUADRADO = a mesma luz da lanterna se espalha: a uma distância dupla cobre uma área 4 vezes maior,
#   então cada pedacinho recebe 1/4 da luz.
# Exemplo da lanterna (nosso, para não entregar a Questão 6): 36 lux a 1 m → 9 lux a 2 m → 4 lux a 3 m (k = 36).
# Nós fazemos: distância triplica → luz cai a 1/9; lado do cubo triplica → volume × 27.
# QUESTÃO 8 do material (eu faço; texto idêntico na tela): A = L² → (3L)² = 9L² → C. Conferência do material: lado 2 → área 4;
#   lado 6 → área 36; 36 ÷ 4 = 9. A (3) = proporção direta e E (27) = fator do volume (material). Explicações NOSSAS:
#   B (6) = fez 3 × 2 em vez de 3² (o erro clássico da potência); D (12) não sai de conta certa (mistura o ×4 do "dobrou,
#   quadruplicou" com o triplo: 3 × 4).
# QUESTÃO 6 do material (você faz): I = k/d² → 100 = k/4 → k = 400 → 400/25 = 16 lux → B. D (40) = inversa simples,
#   100 · 2 ÷ 5 (material). Explicações NOSSAS: E (250) = tratou como direta, a luz AUMENTOU ao se afastar (absurdo);
#   C (20) = dividiu os 100 lux pela nova distância, 100 ÷ 5; A (10) não sai de conta coerente (10 × 25 = 250, não 400).
#   Plausibilidade: a distância cresceu 2,5 vezes; a luz cai 2,5² = 6,25 vezes: 100 ÷ 6,25 = 16.
# Frases-chave (meio e fim, idênticas): 1. Quadrado: dobrou, quadruplicou. 2. Cubo: dobrou, oito vezes.
#   3. Inverso do quadrado: dobrou a distância, um quarto do efeito.
# Atalhos (verde): "eleve o FATOR ao quadrado: ×2 → ×4; ×3 → ×9; ×10 → ×100" · "no cubo, eleve o fator ao cubo: ×2 → ×8; ×3 → ×27"
#   · "distância ×2 → luz ÷4; ×3 → ÷9" · "o expoente diz quantas vezes o fator se multiplica" · "confira com números pequenos".
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Quando dobrar não dobra: quadrática, cúbica e inverso do quadrado | Grandezas Proporcionais Ep. 5"
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
        "{a}Você se afasta de uma lâmpada [p=0.2] para o *dobro da distância.* [p=0.5] {b}A luz cai pela metade? [p=0.5] "
        "{c}*Não:* [p=0.3] cai para *um quarto.* [p=0.5] {d}E isso vale para *som* [p=0.2] e *gravidade* também."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai saber o que acontece [p=0.2] quando uma grandeza *dobra* [p=0.3] {b}ou "
        "*triplica* [p=0.3] {c}em *qualquer tipo de relação.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Potência é multiplicar um número por ele mesmo. [p=0.3] Dois ao "
        "quadrado: [p=0.2] dois vezes dois, [p=0.2] *quatro.* [p=0.3] Três ao quadrado, [p=0.2] *nove.* [p=0.3] Dois ao "
        "cubo: [p=0.2] dois vezes dois vezes dois, [p=0.2] *oito.* [p=0.5] {b}E o k, [p=0.2] do episódio um: [p=0.2] o "
        "número que não muda. [p=0.3] Na direta, [p=0.2] y igual a k vezes x. [p=0.3] Na inversa, [p=0.2] y igual a k "
        "dividido por x."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Agora, três perguntas da vida real. [p=0.4] {a}Você vai azulejar um piso com o *dobro do lado.* [p=0.2] Precisa "
        "do dobro de azulejos? [p=0.4] {b}Uma caixa com o *dobro da aresta,* [p=0.2] que é a medida de cada borda. [p=0.2] "
        "Cabe o dobro de coisas? [p=0.4] {c}E uma lanterna, [p=0.2] *mais longe* da página. [p=0.2] A luz cai pela metade? "
        "[p=0.5] {d}As três respostas são *não.* [p=0.3] Vamos ver por quê."),

    # ================= BLOCO A: DIRETA (REVISÃO) =================
    dict(id="05", block="direta", text=
        "{t}Primeiro, a velha conhecida. [p=0.3] {a}*Direta:* [p=0.2] y igual a k vezes x. [p=0.4] {b}Arroz a cinco reais o "
        "quilo: [p=0.2] o dobro de quilos, [p=0.2] o *dobro* do preço. [p=0.4] {c}Essa relação também se chama *linear:* "
        "[p=0.2] as duas crescem no mesmo ritmo. [p=0.4] {d}Dobrou, [p=0.2] *dobrou.* [p=0.3] Simples."),

    # ================= BLOCO B: QUADRÁTICA =================
    dict(id="06", block="azulejos", text=
        "{t}Agora o piso. [p=0.3] {a}Um piso quadrado de *um metro* de lado [p=0.2] leva *um* azulejo grande. [p=0.4] "
        "{b}Dobre o lado: [p=0.2] dois metros. [p=0.4] {c}Agora são *dois* azulejos de largura [p=0.3] {d}e *dois* de "
        "comprimento. [p=0.4] {e}Dois vezes dois: [p=0.2] *quatro azulejos.* [p=0.4] O lado dobrou, [p=0.2] a área "
        "*quadruplicou.*"),
    dict(id="07", block="azulejos", text=
        "{t}Isso acontece porque a área é o lado *vezes o lado:* [p=0.3] {a}A igual a L ao quadrado. [p=0.4] {b}Quando a "
        "grandeza aparece elevada ao quadrado, [p=0.2] a relação se chama *quadrática.* [p=0.2] Fórmula: [p=0.2] *y igual a k "
        "vezes x ao quadrado.* [p=0.5] {c}E se o lado *triplicar?* [p=0.3] Três de largura, [p=0.2] três de comprimento: "
        "[p=0.3] {d}*nove* azulejos."),
    dict(id="08", block="azulejos", text=
        "{t}Isso também aparece em Física. [p=0.3] {a}A *energia cinética* [p=0.2] é a energia do movimento. [p=0.3] Ela "
        "depende da velocidade *ao quadrado.* [p=0.4] {b}Dobrou a velocidade do carro? [p=0.2] *Quatro vezes* mais energia "
        "numa batida. [p=0.5] {c}Atalho: [p=0.2] *eleve o fator ao quadrado.* [p=0.3] Dobrou, [p=0.2] vezes quatro. "
        "[p=0.2] Triplicou, [p=0.2] vezes nove. [p=0.2] Vezes dez, [p=0.2] vezes cem."),

    # ================= BLOCO C: CÚBICA =================
    dict(id="09", block="cubinhos", text=
        "{t}E a caixa? [p=0.3] {a}Uma caixa cúbica de *um* metro de aresta [p=0.2] guarda *um* cubinho de um metro. [p=0.4] "
        "{b}Dobre a aresta. [p=0.4] {c}Agora são *dois* de largura, [p=0.2] *dois* de comprimento [p=0.2] {d}e *dois* de "
        "altura. [p=0.4] {e}Dois vezes dois vezes dois: [p=0.2] *oito cubinhos.* [p=0.4] A aresta dobrou, [p=0.2] o volume "
        "ficou *oito vezes* maior."),
    dict(id="10", block="cubinhos", text=
        "{t}O volume é a aresta *ao cubo:* [p=0.2] aresta vezes aresta vezes aresta. [p=0.4] {a}Por isso essa relação se chama "
        "*cúbica:* [p=0.2] *y igual a k vezes x ao cubo.* [p=0.5] {b}E se a aresta triplicar? [p=0.3] Três ao cubo: [p=0.2] "
        "três vezes três vezes três, [p=0.2] *vinte e sete.* [p=0.4] {c}Atalho: [p=0.2] no cubo, [p=0.2] *eleve o fator ao "
        "cubo.* [p=0.3] Dobrou, [p=0.2] vezes oito. [p=0.2] Triplicou, [p=0.2] vezes vinte e sete."),

    # ================= BLOCO D: INVERSA (REVISÃO) =================
    dict(id="11", block="inversa", text=
        "{t}Agora as relações que *descem.* [p=0.3] {a}Primeiro, a *inversa:* [p=0.2] y igual a k dividido por x. [p=0.4] "
        "{b}A viagem de duzentos e quarenta quilômetros: [p=0.2] o dobro da velocidade, [p=0.2] *metade* do tempo. [p=0.4] "
        "{c}Dobrou de um lado, [p=0.2] caiu à metade do outro."),

    # ================= BLOCO E: INVERSO DO QUADRADO (A LANTERNA) =================
    dict(id="12", block="lanterna", text=
        "{t}E a lanterna? [p=0.3] {a}Aponte uma lanterna para uma parede a *um metro.* [p=0.3] A luz forma um quadrado "
        "iluminado. [p=0.4] {b}A *intensidade* da luz [p=0.2] é quanto de luz cai em cada pedacinho da parede. [p=0.3] {c}E ela "
        "se mede em *lux.* [p=0.4] {d}Digamos: [p=0.2] *trinta e seis lux* nesse quadrado."),
    dict(id="13", block="lanterna", text=
        "{t}Agora afaste a parede para *dois metros.* [p=0.4] {a}A luz é a *mesma,* [p=0.2] mas o feixe se abre. [p=0.4] "
        "{b}Ele agora cobre *dois* quadrados de largura [p=0.2] e *dois* de altura: [p=0.2] *quatro quadrados.* [p=0.4] "
        "{c}A mesma luz, [p=0.2] repartida em quatro. [p=0.3] {d}Cada pedacinho recebe *um quarto:* [p=0.3] trinta e seis "
        "dividido por quatro, [p=0.2] *nove lux.*"),
    dict(id="14", block="lanterna", text=
        "{t}E a *três metros?* [p=0.4] {a}Três de largura, [p=0.2] três de altura: [p=0.2] *nove quadrados.* [p=0.4] "
        "{b}Cada um recebe *um nono:* [p=0.3] trinta e seis dividido por nove, [p=0.2] *quatro lux.* [p=0.5] {c}A distância "
        "aparece *ao quadrado* [p=0.2] e *embaixo* da fração: [p=0.3] {d}*y igual a k dividido por x ao quadrado.* [p=0.4] "
        "Isso se chama *inverso do quadrado.*"),
    dict(id="15", block="lanterna", text=
        "{t}E não é só a lanterna. [p=0.3] {a}O *som* de uma caixa no show se espalha do mesmo jeito. [p=0.3] {b}E a "
        "*gravidade,* [p=0.2] a força que puxa os planetas, [p=0.2] também cai com o quadrado da distância. [p=0.5] "
        "{c}Atalho: [p=0.2] distância *vezes dois,* [p=0.2] efeito *dividido por quatro.* [p=0.3] Distância vezes três, "
        "[p=0.2] efeito dividido por nove."),

    # ================= BLOCO F: A REGRA GERAL =================
    dict(id="16", block="regra", text=
        "{t}Agora, a tabela completa. [p=0.4] {a}Direta: [p=0.2] dobrou, [p=0.2] dobra. [p=0.3] {b}Quadrática: [p=0.2] "
        "quadruplica. [p=0.3] {c}Cúbica: [p=0.2] oito vezes. [p=0.3] {d}Inversa: [p=0.2] cai à metade. [p=0.3] {e}Inverso do "
        "quadrado: [p=0.2] cai a um quarto. [p=0.5] {f}A regra por trás de tudo: [p=0.2] *o expoente diz quantas vezes o "
        "fator se multiplica.* [p=0.3] Em cima, [p=0.2] multiplica. [p=0.2] Embaixo, [p=0.2] divide."),

    # ================= NÓS FAZEMOS =================
    dict(id="17", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Se a distância até uma lâmpada *triplica,* [p=0.2] o que acontece com a luz? [p=0.4] {b}E se "
        "o lado de um cubo *triplica,* [p=0.2] o que acontece com o volume? [p=0.4] {c}*Pause o vídeo e pense.* [p=2.0]"),
    dict(id="18", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}A luz é inverso do quadrado: [p=0.2] três ao quadrado é nove, [p=0.2] e fica embaixo. "
        "[p=0.3] A luz cai a *um nono.* [p=0.4] {b}O volume é cúbico: [p=0.2] três ao cubo, [p=0.2] *vinte e sete vezes* maior. "
        "[p=0.4] {c}Na dúvida, [p=0.2] confira com números pequenos: [p=0.2] um cubo de lado um tem volume um. [p=0.2] De lado "
        "três: [p=0.2] vinte e sete."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] quadrado: [p=0.2] dobrou, quadruplicou. [p=0.5] {b}Dois: "
        "[p=0.2] cubo: [p=0.2] dobrou, oito vezes. [p=0.5] {c}Três: [p=0.2] inverso do quadrado: [p=0.2] dobrou a distância, "
        "[p=0.2] um quarto do efeito."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="20", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que dobrar o lado *dobra a área.* [p=0.4] "
        "{b}Parece certo, [p=0.2] porque o lado dobrou, [p=0.2] e a gente pensa que tudo dobra junto. [p=0.4] {c}Mas a área "
        "cresce nas *duas direções:* [p=0.2] dois de largura vezes dois de comprimento. [p=0.2] Vezes quatro."),
    dict(id="21", block="erros", text=
        "{a}Segundo: [p=0.2] achar que dobrar a distância reduz a luz *à metade.* [p=0.4] {b}Parece certo, [p=0.2] porque "
        "\"mais longe, menos luz\" soa como inversa simples. [p=0.4] {c}Mas a luz se espalha em largura *e* em altura: "
        "[p=0.2] cobre quatro quadrados. [p=0.2] Um quarto."),
    dict(id="22", block="erros", text=
        "{a}Terceiro: [p=0.2] ao triplicar, [p=0.2] confundir o fator da *área* com o do *volume.* [p=0.4] {b}Parece certo, "
        "[p=0.2] porque nove e vinte e sete são potências de três. [p=0.4] {c}Mas área é ao quadrado: [p=0.2] *vezes nove.* "
        "[p=0.3] Volume é ao cubo: [p=0.2] *vezes vinte e sete.* [p=0.3] Pergunte: [p=0.2] é piso ou é caixa?"),

    # ================= QUESTÃO 8 DO MATERIAL (EU FAÇO) =================
    dict(id="23", block="q8", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.2] Esta eu faço com você. [p=0.4] "
        "{a}Uma praça tem formato quadrado. [p=0.3] {b}Em um projeto de ampliação, [p=0.2] a medida do lado será "
        "*triplicada.* [p=0.3] {c}A área da praça ampliada, [p=0.2] em relação à área atual, [p=0.2] ficará multiplicada "
        "por: [p=0.4] {qa}A: [p=0.2] três. [p=0.3] {qb}B: [p=0.2] seis. [p=0.3] {qc}C: [p=0.2] nove. [p=0.3] {qd}D: [p=0.2] "
        "doze. [p=0.3] {qe}E: [p=0.2] vinte e sete."),
    dict(id="24", block="q8", text=
        "{t}Vamos resolver. [p=0.3] {a}Área de quadrado: [p=0.2] lado ao quadrado. [p=0.2] *Quadrática.* [p=0.4] {b}O lado "
        "triplicou: [p=0.2] o fator três vai ao quadrado. [p=0.2] Três vezes três, [p=0.2] *nove.* [p=0.3] {ok}*Letra C!* "
        "[p=0.4] {c}Confira com números pequenos: [p=0.2] lado dois, [p=0.2] área quatro. [p=0.3] {d}Lado seis, [p=0.2] área "
        "trinta e seis. [p=0.3] Trinta e seis dividido por quatro: [p=0.2] *nove.* [p=0.2] Confirmado."),
    dict(id="25", block="q8", text=
        "{t}E as outras? [p=0.3] {xa}A A tratou como proporção *direta.* [p=0.4] {xe}A E é o fator do *volume:* [p=0.2] "
        "valeria se a praça fosse um cubo. [p=0.4] {xb}A B fez três vezes dois, [p=0.2] em vez de três ao quadrado. [p=0.4] "
        "{xd}E a D não sai de nenhuma conta certa."),

    # ================= QUESTÃO 6 DO MATERIAL (VOCÊ FAZ) =================
    dict(id="26", block="q6", text=
        "{t}Agora, *você faz.* [p=0.3] Mais uma do material. [p=0.4] {a}A iluminação produzida por uma lâmpada sobre uma "
        "superfície é inversamente proporcional ao *quadrado* da distância entre elas. [p=0.4] {b}A *dois metros* da lâmpada, "
        "[p=0.2] a iluminação medida é de *cem lux.* [p=0.3] {c}A *cinco metros,* [p=0.2] a iluminação será de: [p=0.4] "
        "{qa}A: [p=0.2] dez lux. [p=0.3] {qb}B: [p=0.2] dezesseis lux. [p=0.3] {qc}C: [p=0.2] vinte lux. [p=0.3] {qd}D: "
        "[p=0.2] quarenta lux. [p=0.3] {qe}E: [p=0.2] duzentos e cinquenta lux. [p=0.5] {p}*Pause o vídeo e tente.* "
        "[p=2.5]"),
    dict(id="27", block="q6", text=
        "{t}Vamos conferir. [p=0.3] {a}Inverso do quadrado: [p=0.2] I igual a k dividido pela distância ao quadrado. [p=0.4] "
        "{b}Primeiro o k, [p=0.2] com o par conhecido: [p=0.2] cem igual a k dividido por quatro. [p=0.3] *k igual a "
        "quatrocentos.* [p=0.4] {c}A cinco metros: [p=0.2] quatrocentos dividido por vinte e cinco, [p=0.2] *dezesseis lux.* "
        "[p=0.3] {ok}*Letra B!* [p=0.4] {d}Confira: [p=0.2] a distância cresceu *duas vezes e meia;* [p=0.2] a luz cai duas "
        "e meia ao quadrado, [p=0.2] seis vírgula vinte e cinco vezes. [p=0.3] Cem dividido por seis vírgula vinte e cinco: "
        "[p=0.2] dezesseis."),
    dict(id="28", block="q6", text=
        "{t}E as outras? [p=0.3] {xd}A D tratou como inversa *simples,* [p=0.2] sem o quadrado: [p=0.2] cem vezes dois, "
        "dividido por cinco. [p=0.4] {xe}A E fez a luz *aumentar* ao se afastar: [p=0.2] absurdo. [p=0.4] {xc}A C dividiu os "
        "cem lux pela nova distância. [p=0.4] {xa}E a A não sai de conta coerente."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="29", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] quadrado: [p=0.2] dobrou, quadruplicou. [p=0.5] "
        "{b}Dois: [p=0.2] cubo: [p=0.2] dobrou, oito vezes. [p=0.5] {c}Três: [p=0.2] inverso do quadrado: [p=0.2] dobrou a "
        "distância, [p=0.2] um quarto do efeito."),

    # ================= PONTE E CTA =================
    dict(id="30", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] *juntamos tudo,* [p=0.3] {b}caçamos as *pegadinhas* [p=0.3] {c}e "
        "treinamos com *questões novas.*"),
    dict(id="31", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você achava que a luz caía pela metade? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
