# Roteiro — Logaritmos, Episódio 3 de 5: tirando a incógnita do expoente (equações com log e mudança de base)
# Base: Estudos/Enem/estudos/01-matematica/27-logaritmos-propriedades-equacoes.html — seções 05 e 07 + Questões 5, 6, 1 e 8.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   O ELEVADOR: o log é um elevador que traz o expoente para o térreo: aplique log dos dois lados e o t desce multiplicando.
#   O PORÃO: na mudança de base, a base vai para o porão: log_b a = log a ÷ log b.
#   ESTIME ANTES: se 3³ = 27 e 3⁴ = 81, a resposta de 3ᵗ = 50 mora entre 3 e 4.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Blocos a–e = exemplos do prompt/material (2ˣ = 10; log₂ 10 e log₄ 32; log₂ 8 como conferência; 1,05ᵗ = 2; 1 000 · 3ᵗ =
#   50 000 parando em 3ᵗ = 50, como o prompt pede — a Q6 é "nós fazemos" e é resolvida só depois).
# EXEMPLO NOSSO (bloco f, decaimento): o prompt só descreve a ideia; para não adiantar a Q8 ("você faz", com pausa), o bloco
#   usa um celular que perde 25% ao ano: 0,75ᵗ = 0,5; log 0,75 = log 3 − 2 · log 2 = 0,477 − 0,602 = −0,125;
#   t = −0,301 ÷ (−0,125) ≈ 2,4 anos (estimativa: 0,75² ≈ 0,56 e 0,75³ ≈ 0,42).
# DESVIO DO PROMPT (erro 3): o prompt pede o erro "log 0,9 positivo", que é exatamente a conta da Q8 (você faz). O erro usa
#   log 0,6 (log 6 = 0,778; o certo é 0,778 − 1 = −0,222), com o mesmo raciocínio. A Q8 mostra o log 0,9 só depois da pausa.
# Nós fazemos (prompt): 2ˣ = 5, log 2 = 0,30 → log 5 = 1 − 0,30 = 0,70 → x ≈ 2,33 (2² = 4 < 5 < 8 = 2³).
# QUESTÃO 5 ("eu faço"): gabarito C (2,5), pelos dois caminhos. Erradas = material/prompt (A 0,4 inverte a fração; B 2 para na
#   última semana inteira; D 8 divide 32 por 4; E 28 subtrai).
# QUESTÃO 6 ("nós fazemos"): gabarito C (3,54). Erradas = material/prompt (A 0,28 inverte; B 1,22 subtrai os logs; D 16,7
#   divide 50 por 3, linear; E 104 divide 50 por log 3 sem tirar o log de 50).
# QUESTÃO 1 ("você faz", com pausa): gabarito C (≈ 9,1 → 9), conferência pela regra do 72. Erradas = material/prompt (A 0,11
#   inverte; B 0,27 subtrai os logs; D 12,5 juros simples; E 25 divide 2 pela taxa).
# QUESTÃO 8 ("você faz", com pausa): gabarito D (6,5 anos); os dois logs negativos, tempo positivo. Erradas = material/prompt
#   (A 0,15 inverte; B 0,32 usa log 9 = 0,954 no lugar de log 0,9 E deixa o sinal de lado — 0,301 ÷ 0,954 —, como pedem os
#   "Cuidados" do roteiros.md; C 5 perda linear 50% ÷ 10%; E 10 metade confundida com tudo, também linear).
# Acréscimos NOSSOS (marcados): cenas verdes de ATALHO — "estime primeiro: as duas potências inteiras vizinhas" (cena 07),
#   "teste a fração com um caso que você sabe de cabeça: log₂ 8 = 3" (cena 11), "decaimento: menos com menos dá mais; tempo
#   negativo = sinal perdido" (cena 16); a regra do 72 como conferência no bloco d (72 ÷ 5 = 14,4).
# Frases-chave (meio e fim, idênticas): 1. Aplique log dos dois lados e o expoente desce.
#   2. Isole a potência antes de aplicar o log.  3. Na mudança de base, a base vai para baixo.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Equação exponencial com logaritmo do zero: o expoente desce e a mudança de base | Logaritmos Ep. 3"
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
        "{a}Um capital a *cinco por cento ao ano* [p=0.2] demora quanto para *dobrar?* [p=0.5] {b}Em juros simples, "
        "[p=0.2] *vinte anos.* [p=0.4] {c}Em juros compostos, [p=0.2] cerca de *catorze vírgula dois.* [p=0.5] {d}Para "
        "achar esse catorze vírgula dois [p=0.2] você precisa *derrubar um t do expoente.* [p=0.4] {e}Hoje você aprende a "
        "*derrubar.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o terceiro episódio da série de *Logaritmos.* [p=0.4] {a}Ao final, [p=0.2] você vai resolver *qualquer "
        "equação exponencial* [p=0.3] {b}que *não fecha na mesma base,* [p=0.3] {c}com os *logs que o enunciado der.*"),
    dict(id="03", block="prereq", text=
        "{t}Lembretes rápidos. [p=0.3] {a}Do episódio dois: [p=0.2] log de M elevado a k [p=0.2] é *k vezes log de M.* "
        "[p=0.3] {b}O kit: [p=0.2] log de dois, [p=0.2] *zero vírgula trezentos e um;* [p=0.2] log de três, [p=0.2] *zero"
        " vírgula quatrocentos e setenta e sete.* [p=0.3] {c}Ganhar oito por cento [p=0.2] é multiplicar por *um vírgula "
        "zero oito;* [p=0.2] perder dez, [p=0.2] por *zero vírgula nove.* [p=0.3] {d}E de Juros compostos, [p=0.2] a "
        "*regra do setenta e dois.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Perguntas de *tempo.* [p=0.4] {a}Em quantos anos [p=0.2] o meu dinheiro *dobra?* [p=0.3] {b}Em quantas horas "
        "[p=0.2] a cultura chega a *cinquenta mil?* [p=0.3] {c}Quando o equipamento [p=0.2] vale *a metade?* [p=0.4] {d}Nas "
        "três, [p=0.2] a resposta está *no expoente,* [p=0.2] e a base *não fecha.*"),

    # ================= BLOCO A: 2^x = 10 =================
    dict(id="05", block="elev1", text=
        "{t}Dois elevado a x [p=0.2] igual a *dez.* [p=0.3] {a}Dez não é potência de dois: [p=0.2] a mesma base *não "
        "fecha.* [p=0.4] {b}Então a gente *aplica log dos dois lados:* [p=0.2] escreve log na frente de cada lado, [p=0.2] "
        "como o mesmo peso nos dois pratos da balança. [p=0.4] {c}O log é um *elevador* [p=0.2] que traz o expoente *para o "
        "térreo:* [p=0.3] {d}x vezes log de dois [p=0.2] igual a log de dez."),
    dict(id="06", block="grafico", text=
        "{t}Agora, dividir. [p=0.3] {a}Um sobre zero vírgula trezentos e um: [p=0.2] *x é cerca de três vírgula "
        "trinta e dois.* [p=0.4] {b}Faz sentido? [p=0.2] *Estimar* é chutar com critério, [p=0.2] antes da conta. [p=0.3] "
        "{c}Dois ao cubo é oito; [p=0.2] dois elevado a quatro, dezesseis. [p=0.2] O dez *mora entre* os dois. [p=0.4] "
        "{d}No gráfico, [p=0.2] a reta do dez cruza a curva [p=0.2] *entre três e quatro.*"),
    dict(id="07", block="atalho_est", text=
        "{t}Atalho: [p=0.2] *estime primeiro.* [p=0.3] {a}Ache as duas potências *inteiras* que cercam o número. [p=0.3] "
        "{b}A resposta *tem* de cair entre elas. [p=0.3] {c}Saiu fora? [p=0.2] Errou um passo."),

    # ================= BLOCO B: MUDANÇA DE BASE =================
    dict(id="08", block="porao", text=
        "{t}E se o enunciado só der logs na *base dez?* [p=0.4] {a}*Mudança de base* [p=0.2] é reescrever um log de outra "
        "base [p=0.2] como *divisão* de logs decimais. [p=0.4] {b}Log de a na base b [p=0.2] é log de a [p=0.2] *dividido* "
        "por log de b. [p=0.3] {c}A base *vai para o porão.* [p=0.4] {d}Log de dez na base dois: [p=0.2] um sobre zero "
        "vírgula trezentos e um, [p=0.2] *três vírgula trinta e dois,* [p=0.2] a mesma conta de antes."),
    dict(id="09", block="porao2", text=
        "{t}E o porão aceita *qualquer* base. [p=0.3] {a}Log de trinta e dois na base quatro. [p=0.3] {b}Na base dois: "
        "[p=0.2] trinta e dois dá *cinco;* [p=0.2] quatro dá *dois.* [p=0.3] {c}Cinco sobre dois: [p=0.2] *dois vírgula "
        "cinco.*"),

    # ================= BLOCO C: QUEM FICA EM CIMA =================
    dict(id="10", block="emcima", text=
        "{t}Mas quem fica *em cima?* [p=0.4] {a}O *numerador* é o número de cima da fração; [p=0.2] o *denominador,* o de "
        "baixo. [p=0.3] {b}Em cima, o *logaritmando;* [p=0.2] embaixo, a *base.* "
        "[p=0.4] {c}Confira: [p=0.2] log de oito na base dois *tem* de dar três. [p=0.2] Zero vírgula novecentos e três "
        "sobre zero vírgula trezentos e um: [p=0.2] *três.* [p=0.3] {d}Invertida, [p=0.2] daria *um terço.* [p=0.3] {e}Esse é o atalho: [p=0.2] na dúvida, "
        "[p=0.2] monte a fração com um caso que você sabe *de cabeça.*"),
    # ================= BLOCO D: O CAPITAL QUE DOBRA =================
    dict(id="11", block="elev2", text=
        "{t}Agora, [p=0.2] o gancho. [p=0.3] {a}Cinco por cento ao ano: [p=0.2] um vírgula zero cinco elevado a t [p=0.2] "
        "igual a *dois.* [p=0.4] {b}Log dos dois lados, [p=0.2] e o elevador desce o t: [p=0.2] t vezes log de um vírgula "
        "zero cinco [p=0.2] igual a log de dois. [p=0.4] {c}Em cima, [p=0.2] o *log de dois,* o resultado. [p=0.2] Zero "
        "vírgula trezentos e um [p=0.2] sobre zero vírgula zero duzentos e doze: [p=0.2] *cerca de catorze vírgula dois "
        "anos.*"),
    dict(id="12", block="formula", text=
        "{t}Confere? [p=0.3] {a}Em juros simples, [p=0.2] cem dividido por cinco, [p=0.2] *vinte anos;* [p=0.2] os "
        "compostos dobram *antes.* [p=0.4] {b}A regra do setenta e dois: [p=0.2] setenta e dois sobre cinco, [p=0.2] "
        "*catorze vírgula quatro.* [p=0.2] Bem perto. [p=0.4] {c}E é *daqui* que vem a fórmula do tempo [p=0.2] da série "
        "de Juros compostos."),

    # ================= BLOCO E: ISOLE A POTÊNCIA =================
    dict(id="13", block="isolar", text=
        "{t}E com um número *na frente* da potência? [p=0.4] {a}Mil vezes três elevado a t [p=0.2] igual a cinquenta mil. "
        "[p=0.4] {b}*Isolar a potência* [p=0.2] é deixá-la sozinha de um lado. [p=0.2] Divida por mil: [p=0.2] *três "
        "elevado a t igual a cinquenta.* [p=0.4] {c}Log direto também dá, [p=0.2] mas o log de um *produto* vira *soma:* "
        "[p=0.2] *três mais* t vezes log de três."),

    # ================= BLOCO F: DECAIMENTO =================
    dict(id="14", block="decai", text=
        "{t}E quando o valor *cai?* [p=0.4] {a}Um celular perde *vinte e cinco por cento* ao ano. [p=0.2] Quando vale a "
        "metade? [p=0.4] {b}O fator é *menor que um:* [p=0.2] zero vírgula setenta e cinco elevado a t [p=0.2] igual a "
        "zero vírgula cinco. [p=0.4] {c}Número entre zero e um [p=0.2] tem log *negativo:* [p=0.2] log "
        "de zero vírgula setenta e cinco [p=0.2] é *menos zero vírgula cento e vinte e cinco.* [p=0.4] {d}Menos dividido "
        "por menos: [p=0.2] *cerca de dois vírgula quatro anos.* [p=0.2] Positivo."),
    dict(id="15", block="atalho_sinal", text=
        "{t}Atalho para o sinal. [p=0.3] {a}No decaimento, [p=0.2] os *dois* logs são negativos, [p=0.2] e menos com menos"
        " dá *mais.* [p=0.3] {b}Tempo negativo? [p=0.2] Um sinal *se perdeu.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Resolva: [p=0.2] *dois elevado a x igual a cinco,* [p=0.2] com log de dois igual a zero "
        "vírgula trinta. [p=0.4] {b}Dica: [p=0.2] cinco é dez dividido por dois. [p=0.3] {c}*Pause e tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Log de cinco é log de dez menos log de dois: [p=0.2] *zero vírgula setenta.* [p=0.4] "
        "{b}Em cima o cinco, [p=0.2] embaixo a base: [p=0.2] zero vírgula setenta sobre zero vírgula trinta, [p=0.2] "
        "*cerca de dois vírgula trinta e três.* [p=0.4] {c}Confere: [p=0.2] o cinco mora entre o *quatro* e o *oito.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] aplique log dos dois lados e o expoente desce. [p=0.5] "
        "{b}Dois: [p=0.2] isole a potência antes de aplicar o log. [p=0.5] {c}Três: [p=0.2] na mudança de base, a base vai "
        "para baixo."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] log de dez na base dois [p=0.2] virar *log de dois sobre "
        "log de dez.* [p=0.4] {b}Parece certo, [p=0.2] porque o dois aparece *primeiro* na leitura. [p=0.3] {c}Mas a base "
        "vai para o porão: [p=0.2] *log de dez sobre log de dois.*"),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] log de mil vezes três elevado a t [p=0.2] virar *três t vezes log de três.* [p=0.4] {b}Parece "
        "certo, [p=0.2] porque o log desce o expoente, [p=0.2] e parece descer *tudo junto.* [p=0.3] {c}Mas log de produto "
        "é *soma:* [p=0.2] três *mais* t vezes log de três."),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] usar como log de zero vírgula seis [p=0.2] o *zero vírgula setecentos e setenta e oito,* "
        "[p=0.2] que é o log de *seis.* [p=0.4] {b}Parece certo, [p=0.2] porque os algarismos são os mesmos. [p=0.3] {c}Mas"
        " zero vírgula seis é seis sobre dez: [p=0.2] *tire um.* [p=0.2] Fica *negativo,* [p=0.2] menos zero vírgula "
        "duzentos e vinte e dois."),

    # ================= QUESTÃO 5 (EU FAÇO) =================
    dict(id="22", block="q5", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] Esta, [p=0.2] *eu faço.* [p=0.4] {a}A área de uma colônia de "
        "fungos [p=0.2] *quadruplica* a cada semana: [p=0.2] A de t igual a A zero vezes quatro elevado a t. [p=0.3] Em "
        "quantas semanas a área fica *trinta e duas vezes maior?* [p=0.3] {qa}A: [p=0.2] zero vírgula quatro. [p=0.2] "
        "{qb}B: [p=0.2] dois. [p=0.2] {qc}C: [p=0.2] dois vírgula cinco. [p=0.2] {qd}D: [p=0.2] oito. [p=0.2] {qe}E: "
        "[p=0.2] vinte e oito."),
    dict(id="23", block="q5", text=
        "{t}Estime: [p=0.2] em duas semanas, dezesseis vezes; [p=0.2] em três, sessenta e quatro. [p=0.2] Fica *entre dois "
        "e três.* [p=0.4] {a}Mudança de base: [p=0.2] log de trinta e dois sobre log de quatro, [p=0.2] *cinco sobre "
        "dois.* [p=0.3] {b}Ou mesma base: [p=0.2] dois elevado a dois t [p=0.2] igual a dois elevado a cinco. [p=0.3] Os "
        "dois dão *dois vírgula cinco.* [p=0.3] {ok}*Letra C!*"),
    dict(id="24", block="q5", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A *inverte* a fração. [p=0.3] {xb}A B para na última semana *inteira.* [p=0.3] "
        "{xd}A D divide trinta e dois por quatro. [p=0.3] {xe}E a E *subtrai.*"),

    # ================= QUESTÃO 6 (NÓS FAZEMOS) =================
    dict(id="25", block="q6", text=
        "{t}Esta, [p=0.2] *nós fazemos* juntos. [p=0.4] {a}Bactérias: [p=0.2] N de t igual a mil vezes três elevado a t, "
        "[p=0.2] com t em horas. [p=0.2] Log de dois, zero vírgula trinta; [p=0.2] log de três, zero vírgula quarenta e "
        "oito. [p=0.3] Em quantas horas a população chega a *cinquenta mil?* [p=0.3] {qa}A: [p=0.2] zero vírgula vinte e "
        "oito. [p=0.2] {qb}B: [p=0.2] um vírgula vinte e dois. [p=0.2] {qc}C: [p=0.2] três vírgula cinquenta e quatro. "
        "[p=0.2] {qd}D: [p=0.2] dezesseis vírgula sete. [p=0.2] {qe}E: [p=0.2] cento e quatro. [p=0.4] {p}Qual é o "
        "primeiro passo? [p=1.2]"),
    dict(id="26", block="q6", text=
        "{t}*Isolar a potência:* [p=0.2] três elevado a t igual a cinquenta. [p=0.2] Estime: [p=0.2] entre vinte e sete e "
        "oitenta e um, [p=0.2] t fica *entre três e quatro.* [p=0.4] {a}Cinquenta é cem sobre dois: [p=0.2] log de "
        "cinquenta é *um vírgula setenta.* [p=0.3] {b}Em cima o cinquenta, [p=0.2] embaixo o três: [p=0.2] *cerca de três "
        "vírgula cinquenta e quatro.* [p=0.3] {ok}*Letra C!*"),
    dict(id="27", block="q6", text=
        "{t}E as erradas? [p=0.3] {xa}A A *inverte.* [p=0.3] {xb}A B *subtrai* os logs. [p=0.3] {xd}A D divide cinquenta "
        "por três, [p=0.2] como se fosse *linear.* [p=0.3] {xe}E a E esquece de tirar o log *do cinquenta.*"),

    # ================= QUESTÃO 1 (VOCÊ FAZ) =================
    dict(id="28", block="q1", text=
        "{t}Agora, [p=0.2] *você faz.* [p=0.4] {a}Um capital foi aplicado a juros compostos de *oito por cento ao ano.* "
        "[p=0.3] Com log de dois igual a zero vírgula trinta [p=0.2] e log de um vírgula zero oito [p=0.2] igual a zero "
        "vírgula zero trinta e três, [p=0.2] o tempo para *dobrar,* em anos, é cerca de: [p=0.3] {qa}A: [p=0.2] zero vírgula"
        " onze. [p=0.2] {qb}B: [p=0.2] zero vírgula vinte e sete. [p=0.2] {qc}C: [p=0.2] nove. [p=0.2] {qd}D: [p=0.2] doze "
        "vírgula cinco. [p=0.2] {qe}E: [p=0.2] vinte e cinco. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="29", block="q1", text=
        "{t}Vamos conferir. [p=0.3] {a}Um vírgula zero oito elevado a t [p=0.2] igual a dois. [p=0.2] Log dos dois lados, "
        "[p=0.2] e o t desce. [p=0.4] {b}Em cima o log de dois, [p=0.2] embaixo o do fator: [p=0.2] *cerca de nove vírgula"
        " um.* [p=0.3] {c}A regra do setenta e dois confirma: [p=0.2] setenta e dois sobre oito, [p=0.2] *nove.* [p=0.3] "
        "{ok}*Letra C!*"),
    dict(id="30", block="q1", text=
        "{t}E as erradas? [p=0.3] {xa}A A *inverte.* [p=0.3] {xb}A B *subtrai* os logs. [p=0.3] {xd}A D é o tempo em "
        "*juros simples.* [p=0.3] {xe}E a E divide dois pela taxa, [p=0.2] *sem logaritmo.*"),

    # ================= QUESTÃO 8 (VOCÊ FAZ) =================
    dict(id="31", block="q8", text=
        "{t}E a última, [p=0.2] *você faz* também. [p=0.4] {a}Um equipamento perde *dez por cento* ao ano, [p=0.2] sempre "
        "sobre o valor do ano anterior. [p=0.2] Log de dois, zero vírgula trezentos e um; [p=0.2] log de três, zero "
        "vírgula quatrocentos e setenta e sete. [p=0.3] Ele valerá *a metade* em cerca de: [p=0.3] {qa}A: [p=0.2] zero "
        "vírgula quinze ano. [p=0.2] {qb}B: [p=0.2] zero vírgula trinta e dois ano. [p=0.2] {qc}C: [p=0.2] cinco anos. "
        "[p=0.2] {qd}D: [p=0.2] seis vírgula cinco anos. [p=0.2] {qe}E: [p=0.2] dez anos. [p=0.5] {p}*Pause o vídeo e "
        "tente.* [p=2.0]"),
    dict(id="32", block="q8", text=
        "{t}Vamos conferir. [p=0.3] {a}Zero vírgula nove elevado a t [p=0.2] igual a zero vírgula cinco. [p=0.4] {b}Log de"
        " zero vírgula nove [p=0.2] é log de nove menos um: [p=0.2] *menos zero vírgula zero quarenta e seis.* [p=0.3] Log "
        "de zero vírgula cinco: [p=0.2] *menos zero vírgula trezentos e um.* [p=0.4] {c}Dois negativos, [p=0.2] tempo "
        "positivo: [p=0.2] *cerca de seis vírgula cinco anos.* [p=0.3] {ok}*Letra D!*"),
    dict(id="33", block="q8", text=
        "{t}E as erradas? [p=0.3] {xa}A A *inverte.* [p=0.3] {xb}A B usa log de *nove* no lugar de log de zero vírgula "
        "nove, [p=0.2] e larga o sinal. [p=0.3] {xc}A C supõe perda *linear.* [p=0.3] {xe}E a E confunde a metade com "
        "perder *tudo.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="34", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] aplique log dos dois lados e o expoente desce. "
        "[p=0.5] {b}Dois: [p=0.2] isole a potência antes de aplicar o log. [p=0.5] {c}Três: [p=0.2] na mudança de base, a "
        "base vai para baixo."),

    # ================= PONTE E CTA =================
    dict(id="35", block="ponte", text=
        "{a}Log na base dois de x, [p=0.2] mais log na base dois de x menos dois, [p=0.2] igual a três, [p=0.3] {b}tem "
        "*duas raízes* no papel, [p=0.2] mas *só uma vale.* [p=0.4] {c}Qual, [p=0.2] e por quê? [p=0.4] {d}Próximo "
        "episódio."),
    dict(id="36", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual dos três erros clássicos *você* já cometeu? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
