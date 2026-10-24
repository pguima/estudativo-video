# Roteiro — Números Complexos, Episódio 4 de 5: forma trigonométrica e De Moivre (multiplicar é girar)
# Base: Estudos/Enem/estudos/01-matematica/36-numeros-complexos.html — seções 07, 08 e 09 + Questões 6 e 7.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na revisão):
#   O ENDEREÇO DO RADAR: a forma trigonométrica é distância (módulo) e direção (argumento).
#   ESTICAR E GIRAR: multiplicar multiplica os módulos e soma os ângulos.
#   OS SINAIS ESCOLHEM O QUADRANTE: o ângulo de referência é só o "tamanho" do ângulo.
#   Retomadas: a MANIVELA de 90° (multiplicar por i, ep. 3) e o RELÓGIO DE QUATRO HORAS (1, i, −1, −i, ep. 1).
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
#   Ressalva: o gancho do usuário já dá a resposta da Questão 7 ("você faz", 16). Mantido; na Q7, o novo é o caminho
#   algébrico e as alternativas erradas.
# Revisão rápida: módulo e plano de Argand-Gauss (ep. 3); o relógio de i (ep. 1); a tabela de seno e cosseno de 30°,
#   45°, 60°, 90°, 180° e 360° mostrada na tela ("isso tem série própria, na Trigonometria").
# Exemplos do prompt e do material: bloco b (√3 + i → 2 e 30°; tabela 1 + i, i, −1), bloco c (−1 + i → 135°), bloco e
#   ((√3 + i)⁶ = −64), bloco f (raízes quartas de 1), nós fazemos (1 − i → √2 e 315°).
# Exemplos NOSSOS (marcados):
#   - bloco d (produto): 2(cos 30° + i sen 30°) · 3(cos 60° + i sen 60°) = 6(cos 90° + i sen 90°) = 6i, e o quociente
#     dos mesmos (1,5 e 30°); vezes i: i(√3 + i) = −1 + √3 i, de 30° para 120°, módulo 2. O material usa i(3 + 2i),
#     que é a Questão 5 do ep. 3.
# Acréscimos NOSSOS (marcados): cenas verdes de ATALHO — "cos = a ÷ ρ, sen = b ÷ ρ: procure na tabela";
#   "o quadrante pelo ângulo de referência: 1º θ = ref, 2º 180° − ref, 3º 180° + ref, 4º 360° − ref";
#   "passou de 360°, tire as voltas inteiras" (405° → 45°).
# QUESTÃO 6 (eu faço): ρ = √(1 + 3) = 2, cos θ = 1/2, sen θ = √3/2, 1º quadrante, θ = 60° (B). Erradas = material e
#   prompt (A esquece a raiz no módulo, 4; C troca seno e cosseno, 30°; D põe no 2º quadrante, 120°; E é o conjugado,
#   300°).
# QUESTÃO 7 (você faz): (√2)⁸ = 16, 8 · 45° = 360° → 16; algébrico (1 + i)² = 2i, (2i)⁴ = 16 · i⁴ = 16 (C).
#   Erradas = material (A i⁴ = −1; B 2i · 4 = 8i; D i⁴ = i; E módulo 2, 2⁸ = 256).
# Erro clássico (prompt): argumento de −1 + i = 45° (é 135°).
# Frases-chave (meio e fim, idênticas): 1. Módulo e argumento: distância e direção. 2. Multiplicar: multiplica os módulos
#   e soma os ângulos. 3. Potência: módulo elevado a n, ângulo vezes n.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "(1 + i) elevado a 8 em uma linha: forma trigonométrica e De Moivre · Matemática ENEM, Complexos episódio 4"

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
        "{a}*Um mais i, elevado a oito:* [p=0.3] oito multiplicações? [p=0.5] {b}Na forma trigonométrica, [p=0.2] raiz "
        "de dois elevado a oito dá *dezesseis* [p=0.3] {c}e oito vezes quarenta e cinco graus dá *trezentos e sessenta "
        "graus,* [p=0.2] uma volta inteira. [p=0.5] {d}A resposta é *dezesseis,* [p=0.2] *em uma linha.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o quarto episódio da série de *Números complexos.* [p=0.4] {a}Ao final, [p=0.2] você vai escrever "
        "um complexo como *distância e ângulo,* [p=0.3] {b}*multiplicar girando* [p=0.3] {c}e calcular *potências "
        "altas* com a fórmula de *De Moivre.*"),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Do episódio três: [p=0.2] *a mais b i* é o ponto *a, b* no plano, "
        "[p=0.2] e o *módulo* é a distância até a origem. [p=0.4] {b}Do episódio um: [p=0.2] o *relógio do i:* "
        "[p=0.2] um, i, menos um, menos i. [p=0.4] {c}E uma *tabela* de seno e cosseno, [p=0.2] que fica na tela. "
        "[p=0.2] Isso tem série própria, [p=0.2] na *Trigonometria.*"),
    dict(id="04", block="tabela", text=
        "{t}Olhe a tabela. [p=0.3] {a}Em *trinta graus,* [p=0.2] o seno é *um meio.* [p=0.4] {b}Em *quarenta e cinco,* "
        "[p=0.2] seno e cosseno são *iguais.* [p=0.4] {c}Em *sessenta,* [p=0.2] o *cosseno* é um meio. [p=0.4] {d}E nos "
        "ângulos redondos, [p=0.2] eles valem *zero, um ou menos um.*"),

    # ================= CONCRETO =================
    dict(id="05", block="concreto", text=
        "{t}Imagine a tela de um *radar.* [p=0.4] {a}Um navio avisa: [p=0.2] *estou a duas milhas, na direção de "
        "sessenta graus.* [p=0.4] {b}O operador marca o ponto. [p=0.4] {c}O mesmo ponto também "
        "pode ser dado por *coordenadas:* [p=0.2] tanto para o lado, tanto para cima. [p=0.4] {d}Duas formas de dar "
        "*o mesmo endereço.*"),

    # ================= BLOCO A: MÓDULO E ARGUMENTO =================
    dict(id="06", block="definicao", text=
        "{t}E um número complexo, [p=0.2] tem endereço de radar? [p=0.4] {a}Tem. [p=0.2] A distância até a origem é o "
        "*módulo,* [p=0.2] a letra grega *rô.* [p=0.4] {b}*Argumento:* [p=0.2] o ângulo que a seta faz com o *eixo "
        "real positivo,* [p=0.2] a letra *teta,* [p=0.2] de zero a trezentos e sessenta graus. [p=0.4] {c}Aí, "
        "[p=0.2] *a é rô vezes cosseno de teta,* [p=0.2] e *b é rô vezes seno de teta.* [p=0.4] {d}*Forma "
        "trigonométrica,* [p=0.2] ou polar: [p=0.2] *z igual a rô, vezes cosseno de teta, mais i seno de teta.*"),

    # ================= BLOCO B: UM EXEMPLO =================
    dict(id="07", block="exemplo", text=
        "{t}Vamos testar com *raiz de três, mais i.* [p=0.4] {a}Marque o ponto: [p=0.2] raiz de três para o lado, "
        "[p=0.2] um para cima. [p=0.2] *Primeiro quadrante.* [p=0.4] {b}Módulo: [p=0.2] raiz de três ao quadrado, mais "
        "um ao quadrado: [p=0.2] raiz de *quatro,* [p=0.2] *dois.* [p=0.4] {c}Cosseno: [p=0.2] a sobre rô. [p=0.2] Seno: "
        "[p=0.2] b sobre rô, *um meio.* [p=0.4] {d}Na tabela, [p=0.2] isso é *trinta graus.* "
        "[p=0.3] z é *dois, vezes cosseno de trinta, mais i seno de trinta.*"),
    dict(id="08", block="tabela07", text=
        "{t}E os outros endereços prontos? [p=0.4] {a}*Um mais i:* [p=0.2] módulo raiz de dois, [p=0.2] *quarenta e "
        "cinco graus.* [p=0.4] {b}*i:* [p=0.2] módulo um, [p=0.2] *noventa graus,* [p=0.2] reto para cima. [p=0.4] "
        "{c}*Menos um:* [p=0.2] módulo um, [p=0.2] *cento e oitenta graus,* [p=0.2] para trás."),
    dict(id="09", block="atalho_tabela", text=
        "{t}Atalho. [p=0.4] {a}Ache o módulo. [p=0.2] Depois, divida: [p=0.2] *a sobre rô* é o cosseno, [p=0.2] *b "
        "sobre rô* é o seno. [p=0.4] {b}Procure o par na tabela, [p=0.2] e o ângulo aparece."),

    # ================= BLOCO C: O QUADRANTE =================
    dict(id="10", block="quadrante", text=
        "{t}E se o ponto estiver do outro lado? [p=0.4] {a}Pegue *menos um, mais i.* [p=0.2] Um para trás, um para "
        "cima: [p=0.2] *segundo quadrante.* [p=0.2] *Quadrante:* [p=0.2] um dos quatro pedaços do plano. [p=0.4] {b}*Ângulo "
        "de referência:* [p=0.2] o ângulo dos números *sem sinal.* [p=0.2] Aqui, *quarenta e cinco graus.* "
        "[p=0.4] {c}Quem escolhe o quadrante são os *sinais.* [p=0.3] {d}No segundo quadrante, [p=0.2] "
        "teta é cento e oitenta, menos quarenta e cinco: [p=0.2] *cento e trinta e cinco graus.*"),
    dict(id="11", block="atalho_quadrante", text=
        "{t}Atalho. [p=0.4] {a}Com o ângulo de referência na mão: [p=0.2] no *primeiro* quadrante, [p=0.2] é ele "
        "mesmo. [p=0.3] {b}No *segundo,* [p=0.2] cento e oitenta *menos* ele. [p=0.3] {c}No *terceiro,* [p=0.2] cento e "
        "oitenta *mais* ele. [p=0.3] {d}No *quarto,* [p=0.2] trezentos e sessenta *menos* ele."),

    # ================= BLOCO D: MULTIPLICAR É GIRAR =================
    dict(id="12", block="produto", text=
        "{t}E por que essa forma vale a pena? [p=0.4] {a}Porque *multiplicar* fica fácil. [p=0.2] *Multiplica os "
        "módulos* e *soma os ângulos.* [p=0.4] {b}Dois, com trinta graus, [p=0.2] vezes três, com sessenta graus: "
        "[p=0.3] {c}módulo *seis,* [p=0.2] ângulo *noventa.* [p=0.2] Deu *seis i.* [p=0.4] {d}A seta *esticou* e "
        "*girou.* [p=0.4] {e}E dividir? [p=0.2] *Divide os módulos* e *subtrai os ângulos.*"),
    dict(id="13", block="vezes_i", text=
        "{t}Lembra da *manivela* do episódio três? [p=0.4] {a}O *i* tem módulo *um* e ângulo *noventa.* [p=0.4] "
        "{b}Então, vezes i: [p=0.2] o módulo fica igual, [p=0.2] e o ângulo ganha *noventa graus.* [p=0.4] {c}Raiz de "
        "três mais i, de trinta graus, [p=0.2] vira *menos um, mais raiz de três i,* [p=0.2] em *cento e vinte.* "
        "[p=0.3] {d}Gira noventa, [p=0.2] *sem esticar.*"),

    # ================= BLOCO E: DE MOIVRE =================
    dict(id="14", block="moivre", text=
        "{t}E elevar a uma potência alta? [p=0.4] {a}Elevar a *n* é multiplicar *n vezes.* [p=0.4] "
        "{b}*Fórmula de De Moivre:* [p=0.2] o módulo vai *elevado a n,* [p=0.2] e o ângulo é *multiplicado por "
        "n.* [p=0.4] {c}Raiz de três mais i, elevado a seis: [p=0.2] módulo dois, elevado a seis: [p=0.2] "
        "*sessenta e quatro.* [p=0.2] Ângulo: [p=0.2] seis vezes trinta, *cento e oitenta.* [p=0.4] {d}Cosseno de cento "
        "e oitenta é menos um, [p=0.2] seno é zero. [p=0.2] Resultado: [p=0.2] *menos sessenta e quatro.*"),
    dict(id="15", block="atalho_voltas", text=
        "{t}Atalho. [p=0.4] {a}Se o ângulo passar de trezentos e sessenta, [p=0.2] *tire as voltas inteiras.* [p=0.4] "
        "{b}Quatrocentos e cinco graus: [p=0.2] tire uma volta, [p=0.2] sobram *quarenta e cinco.*"),

    # ================= BLOCO F: RAÍZES =================
    dict(id="16", block="raizes", text=
        "{t}E o caminho de volta, [p=0.2] as raízes? [p=0.4] {a}*Raízes enésimas:* [p=0.2] os números que, elevados a *n,* "
        "[p=0.2] voltam ao número de partida. [p=0.4] {b}Em uma frase: [p=0.2] todas têm o *mesmo módulo* [p=0.2] e ficam "
        "*igualmente espaçadas,* [p=0.2] nos cantos de um *polígono regular,* [p=0.2] a figura de lados iguais. [p=0.4] {c}As raízes quartas de um: [p=0.2] *um, i, menos um, menos i.* [p=0.2] Um *quadrado.* "
        "[p=0.2] O *relógio* do episódio um."),

    # ================= NÓS FAZEMOS =================
    dict(id="17", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Escreva *um menos i* na forma trigonométrica. [p=0.4] {b}Marque o ponto, [p=0.2] diga "
        "o quadrante [p=0.2] e ache o ângulo. [p=0.4] {c}*Pause e tente.* [p=2.0]"),
    dict(id="18", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Um para o lado, [p=0.2] um para *baixo.* [p=0.2] a positivo, b negativo: "
        "[p=0.2] *quarto quadrante.* [p=0.4] {b}Módulo: [p=0.2] raiz de um mais um, [p=0.2] *raiz de dois.* [p=0.4] "
        "{c}Ângulo de referência: [p=0.2] *quarenta e cinco.* [p=0.2] No quarto, [p=0.2] trezentos e sessenta menos "
        "quarenta e cinco: [p=0.2] *trezentos e quinze graus.* [p=0.4] {d}z é *raiz de dois, vezes cosseno de trezentos "
        "e quinze, mais i seno de trezentos e quinze.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="19", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] módulo e argumento: [p=0.2] distância e direção. "
        "[p=0.5] {b}Dois: [p=0.2] multiplicar: [p=0.2] multiplica os módulos e soma os ângulos. [p=0.5] {c}Três: "
        "[p=0.2] potência: [p=0.2] módulo elevado a n, [p=0.2] ângulo vezes n."),

    # ================= ERRO CLÁSSICO =================
    dict(id="20", block="erros", text=
        "{t}Agora, o erro clássico. [p=0.4] {a}Dizer que o argumento de *menos um, mais i* é *quarenta e cinco graus.* "
        "[p=0.4] {b}Parece certo, [p=0.2] porque a conta com os números *sem sinal* dá mesmo quarenta e cinco. "
        "[p=0.4] {c}Mas quarenta e cinco graus é o endereço de *um mais i,* [p=0.2] no primeiro quadrante. [p=0.2] O "
        "ponto está no *segundo:* [p=0.2] *cento e trinta e cinco graus.*"),

    # ================= QUESTÃO 6: EU FAÇO =================
    dict(id="21", block="q6", text=
        "{t}Agora, [p=0.2] uma questão no estilo do ENEM. [p=0.4] {a}O número complexo *z igual a um, mais raiz de três "
        "i,* [p=0.2] escrito na forma trigonométrica, é: [p=0.3] {qa}A: quatro, cosseno de sessenta, mais i seno de "
        "sessenta. [p=0.2] {qb}B: dois, com sessenta graus. [p=0.2] {qc}C: dois, com trinta. [p=0.2] {qd}D: dois, com "
        "cento e vinte. [p=0.2] {qe}E: dois, com trezentos."),
    dict(id="22", block="q6", text=
        "{t}Essa, [p=0.2] *eu faço.* [p=0.4] {a}Marco o ponto: [p=0.2] um para o lado, raiz de três para cima. "
        "[p=0.2] a e b positivos: [p=0.2] *primeiro quadrante.* [p=0.4] {b}Módulo: [p=0.2] raiz de um mais três, "
        "[p=0.2] raiz de quatro: [p=0.2] *dois.* [p=0.4] {c}Cosseno: [p=0.2] *um meio.* [p=0.2] Seno: [p=0.2] *raiz de "
        "três sobre dois.* [p=0.2] Na tabela: [p=0.2] *sessenta graus.* [p=0.3] {ok}*Letra B!* [p=0.4] {d}Confiro: "
        "[p=0.2] dois vezes um meio dá *um,* [p=0.2] e dois vezes raiz de três sobre dois dá *raiz de três.*"),
    dict(id="23", block="q6", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A esquece a *raiz* no módulo: [p=0.2] parou no quatro. "
        "[p=0.4] {xc}A C *troca seno e cosseno:* [p=0.2] trinta graus é o raiz de três mais i. [p=0.4] {xd}A D põe o "
        "ponto no *segundo quadrante,* [p=0.2] mas a e b são positivos. [p=0.4] {xe}E a E é o *conjugado,* [p=0.2] no "
        "quarto quadrante."),

    # ================= QUESTÃO 7: VOCÊ FAZ =================
    dict(id="24", block="q7", text=
        "{t}Agora, [p=0.2] *você faz.* [p=0.4] {a}O valor de *um mais i, elevado a oito,* [p=0.2] em que i é a "
        "unidade imaginária, é: [p=0.3] {qa}A: menos dezesseis. [p=0.2] {qb}B: oito i. [p=0.2] {qc}C: dezesseis. "
        "[p=0.2] {qd}D: dezesseis i. [p=0.2] {qe}E: duzentos e cinquenta e seis. [p=0.4] {p}*Pause o vídeo e tente.* "
        "[p=2.0]"),
    dict(id="25", block="q7", text=
        "{t}Vamos conferir, [p=0.2] por *dois caminhos.* [p=0.4] {a}De Moivre: [p=0.2] um mais i tem módulo *raiz de "
        "dois* e ângulo *quarenta e cinco.* [p=0.2] Raiz de dois elevado a oito: [p=0.2] *dezesseis.* [p=0.2] Oito "
        "vezes quarenta e cinco: [p=0.2] *trezentos e sessenta,* [p=0.2] uma volta inteira. [p=0.3] {ok}*Dezesseis, letra C!* [p=0.4] {b}Algébrico: [p=0.2] um mais i, ao quadrado, [p=0.2] dá "
        "*dois i,* [p=0.2] porque i ao quadrado é menos um. [p=0.4] {c}Elevado a oito é *dois i, elevado a "
        "quatro:* [p=0.2] dezesseis vezes i a quarta. [p=0.2] E i a quarta é *um:* [p=0.2] *dezesseis.*"),
    dict(id="26", block="q7", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A usa *i a quarta igual a menos um.* [p=0.4] {xb}A B *multiplica* dois i "
        "por quatro, [p=0.2] em vez de elevar à quarta. [p=0.4] {xd}A D usa *i a quarta igual a i.* [p=0.4] {xe}E a E "
        "toma o módulo de um mais i como *dois,* [p=0.2] e não raiz de dois: [p=0.2] dois elevado a oito."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="27", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] módulo e argumento: [p=0.2] distância e "
        "direção. [p=0.5] {b}Dois: [p=0.2] multiplicar: [p=0.2] multiplica os módulos e soma os ângulos. [p=0.5] "
        "{c}Três: [p=0.2] potência: [p=0.2] módulo elevado a n, [p=0.2] ângulo vezes n."),

    # ================= PONTE E CTA =================
    dict(id="28", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] *juntamos tudo,* [p=0.3] {b}caçamos as *pegadinhas* [p=0.3] {c}e "
        "treinamos com *questões inéditas.*"),
    dict(id="29", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha pensado num número complexo como uma seta que gira? "
        "[p=0.5] "
        "{anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no "
        "*Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
