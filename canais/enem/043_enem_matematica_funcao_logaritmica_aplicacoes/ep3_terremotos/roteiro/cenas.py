# Roteiro — Função logarítmica e aplicações, Episódio 3 de 5: terremotos (amplitude, energia e magnitude de momento)
# Base: Estudos/Enem/estudos/01-matematica/28-funcao-logaritmica-aplicacoes.html — seção 07, o hábito 2 da seção 09
#   + Questões 3 e 8 (seção 12). Só as três fórmulas do material: M = log(A/A₀) · log E = 4,8 + 1,5M ·
#   M_w = (2/3) · log M₀ − 10,7 (M₀ em dina·cm).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   DOIS PLACARES no mesmo terremoto: por grau, a amplitude sobe ×10 e a energia sobe ×32.
#   A CONSTANTE SE CANCELA: o 4,8 está nos dois lados e some.
#   AS ROUPAS: para voltar da magnitude ao momento sísmico, desfaça de fora para dentro, na ordem inversa em que vestiu.
# Frases do usuário mantidas IGUAIS: gancho, promessa e ponte (números falados por extenso). Frases-chave 1 e 3 iguais.
# CORREÇÃO DO PROMPT (frase-chave 2 e bloco c): o prompt diz "divida a diferença pelo coeficiente e eleve 10". Na energia
#   dos sismos o coeficiente MULTIPLICA: log E₇ − log E₅ = 1,5 · (7 − 5) = 3 → 10³ (é a própria resolução da Q3 do
#   material). Dividir daria 10^(2/1,5) ≈ 22, que não é resposta. O vídeo diz: "Na comparação, a constante se cancela:
#   multiplique a diferença pelo coeficiente e eleve 10." (O hábito 1 da seção 09 do material também diz "divida pelo
#   coeficiente (…1,5 na energia dos sismos…)": só vale nos decibéis, onde o 10 está do lado do log. Não usamos o hábito 1.)
# Revisão rápida (prompt): G₂ ÷ G₁ = 10^(E₂ − E₁) (ep. 2), log(A/A₀) = log A − log A₀ (série de Logaritmos),
#   10^1,5 ≈ 31,6 (= 10 · √10).
# Blocos (prompt): a) M = log(A/A₀) · b) log E = 4,8 + 1,5M · c) comparação (4,8 se cancela) · d) M_w com M₀ = 10²⁴ → 5,3
#   (número do material) · e) caminho inverso, partindo do mesmo 5,3 → 10²⁴ (hábito 2 da seção 09) · f) amplitude × energia.
# Nós fazemos (prompt): M₀ = 10²¹ → (2/3) · 21 − 10,7 = 14 − 10,7 = 3,3.
# Erros (prompt): +2 graus com energia ×100; subtrair 10,7 antes de multiplicar. Exemplo NOSSO no erro 2 (marcado), com
#   o 10²⁴ do bloco d e não com a Q8 ("você faz"): (2/3) · (24 − 10,7) ≈ 8,9 em vez de 5,3.
# Acréscimos NOSSOS (marcados): cenas verdes de ATALHO — "a cada dois graus, a energia ganha três zeros" (cena 09) e
#   "dois terços de um número: divida por três e dobre" (cena 11); a conferência da Q8 pelo caminho inverso
#   ((7,3 + 10,7) · 1,5 = 27); a plausibilidade da Q3 (a energia tem que crescer MAIS que a amplitude, que já é 100).
# QUESTÃO 3 ("eu faço"): gabarito C (1 000 vezes). Erradas = material/prompt (A esquece de elevar 10; B é a razão das
#   amplitudes; D eleva ao quadrado a razão das amplitudes; E mantém o 4,8, 10^4,8 ≈ 63 000).
# QUESTÃO 8 ("você faz", com pausa): gabarito A (7,3). Erradas = material/prompt (B subtrai antes, 10,9; C esquece o
#   −10,7, 18,0; D soma 10,7, 28,7; E inverte a fração, 29,8).
# Frases-chave (meio e fim, idênticas): 1. Um grau a mais: amplitude ×10, energia cerca de ×32.
#   2. Na comparação, a constante se cancela: multiplique a diferença pelo coeficiente e eleve 10. (corrigida, ver acima)
#   3. Na fórmula, multiplique primeiro e subtraia depois; para voltar, desfaça de fora para dentro.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Terremotos no ENEM: amplitude ×100, energia ×1 000 · Matemática ENEM, Função logarítmica episódio 3"

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
        "{a}De magnitude *cinco* para *sete,* [p=0.2] o sismógrafo registra uma amplitude *cem vezes maior.* [p=0.5] "
        "{b}Mas a energia liberada [p=0.2] é *mil vezes maior.* [p=0.5] {c}Duas respostas diferentes para a mesma "
        "pergunta, [p=0.3] e as duas *estão nas alternativas.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o terceiro episódio da série de *Função logarítmica.* [p=0.4] {a}Ao final, [p=0.2] você vai comparar "
        "terremotos pela *amplitude* e pela *energia* [p=0.2] sem confundir os fatores, [p=0.4] {b}e calcular uma "
        "*magnitude* por fórmula dada."),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Do episódio dois: [p=0.2] para saber *quantas vezes* uma grandeza é "
        "maior, [p=0.2] eleve *dez à diferença* das leituras. [p=0.4] {b}Da série de Logaritmos: [p=0.2] log de A "
        "sobre A zero [p=0.2] é *log de A menos log de A zero.* [p=0.4] {c}E uma conta que vai aparecer muito: "
        "[p=0.2] *dez elevado a um e meio* [p=0.2] é dez vezes raiz de dez, [p=0.2] cerca de *trinta e um vírgula "
        "seis.*"),

    # ================= CONCRETO =================
    dict(id="04", block="manchete", text=
        "{t}Você já leu esta manchete: [p=0.2] *terremoto de magnitude sete na escala Richter.* [p=0.4] {a}Mas sete "
        "*o quê?* [p=0.4] {b}Tudo começa no *sismógrafo:* [p=0.2] o aparelho que *risca um papel* quando o chão "
        "treme. [p=0.4] {c}A altura dessa onda riscada [p=0.2] é a *amplitude.* [p=0.2] Chão tremendo forte, [p=0.2] "
        "risco alto."),

    # ================= BLOCO A: AMPLITUDE =================
    dict(id="05", block="amplitude", text=
        "{t}Como esse risco vira um número? [p=0.4] {a}Compara-se com uma *amplitude de referência,* [p=0.2] A zero: "
        "[p=0.2] um tremor pequenininho, combinado como padrão. [p=0.4] {b}A *magnitude* é o log dessa comparação: "
        "[p=0.2] *M igual a log de A sobre A zero.* [p=0.4] {c}Por isso, [p=0.2] *um grau a mais* na magnitude "
        "[p=0.2] é uma amplitude *dez vezes maior.*"),

    # ================= BLOCO B: ENERGIA =================
    dict(id="06", block="energia", text=
        "{t}E a força do terremoto? [p=0.4] {a}A *energia liberada* [p=0.2] é o tanto de energia que o tremor solta, "
        "[p=0.2] medida em *joules.* [p=0.4] {b}A fórmula do material: [p=0.2] *log de E igual a quatro vírgula oito "
        "mais um vírgula cinco M.* [p=0.4] {c}Repare no *um vírgula cinco* [p=0.2] multiplicando o M. [p=0.2] É ele "
        "que muda tudo."),
    dict(id="07", block="placares", text=
        "{t}Imagine *dois placares* no mesmo terremoto. [p=0.4] {a}A magnitude sobe de cinco para *seis.* [p=0.2] "
        "Amplitude: [p=0.2] *vezes dez.* [p=0.2] Energia: [p=0.2] dez elevado a um e meio, [p=0.2] *vezes trinta e "
        "dois.* [p=0.4] {b}De seis para *sete:* [p=0.2] de novo vezes dez [p=0.2] e de novo vezes trinta e dois. "
        "[p=0.4] {c}No total, [p=0.2] amplitude *vezes cem,* [p=0.2] energia *vezes mil.* [p=0.2] Dez elevado a "
        "três."),

    # ================= BLOCO C: COMPARAÇÃO =================
    dict(id="08", block="comparacao", text=
        "{t}E como comparar sem calcular cada energia? [p=0.4] {a}Escreva a fórmula para o *sete* [p=0.2] e para o "
        "*cinco,* [p=0.2] e *subtraia.* [p=0.4] {b}O *quatro vírgula oito* está nos dois lados [p=0.2] e *some.* "
        "[p=0.2] A constante se cancela. [p=0.4] {c}Sobra *um vírgula cinco vezes dois,* [p=0.2] três. [p=0.2] "
        "*Multiplique* a diferença pelo coeficiente, [p=0.2] o número que acompanha o M. [p=0.4] {d}E eleve dez: "
        "[p=0.2] *dez ao cubo,* [p=0.2] mil vezes."),
    dict(id="09", block="atalho_zeros", text=
        "{t}Atalho para a prova. [p=0.4] {a}Na energia, [p=0.2] *a cada dois graus,* [p=0.2] o número ganha *três "
        "zeros.* [p=0.4] {b}Dois graus: [p=0.2] vezes mil. [p=0.2] Quatro graus: [p=0.2] vezes *um milhão.* [p=0.4] "
        "{c}Na amplitude, [p=0.2] é um zero por grau."),

    # ================= BLOCO D: MAGNITUDE DE MOMENTO =================
    dict(id="10", block="momento", text=
        "{t}Os sismólogos de hoje usam *outra* escala. [p=0.4] {a}O *momento sísmico,* [p=0.2] M zero, [p=0.2] mede o "
        "tamanho da *ruptura* da rocha, [p=0.2] em *dina centímetro.* [p=0.4] {b}A *magnitude de momento* [p=0.2] sai "
        "dele: [p=0.2] *M w igual a dois terços de log de M zero, menos dez vírgula sete.* [p=0.2] O noticiário "
        "continua dizendo escala Richter. [p=0.4] {c}Com M zero igual a dez elevado a *vinte e quatro:* [p=0.2] o log "
        "é vinte e quatro. [p=0.4] {d}*Primeiro, multiplique:* [p=0.2] dois terços de vinte e quatro, [p=0.2] "
        "*dezesseis.* [p=0.4] {e}*Depois, subtraia:* [p=0.2] dezesseis menos dez vírgula sete, [p=0.2] *cinco vírgula "
        "três.*"),
    dict(id="11", block="atalho_terco", text=
        "{t}Atalho para os dois terços. [p=0.4] {a}*Divida por três* [p=0.2] e *dobre.* [p=0.4] {b}Vinte e quatro "
        "dividido por três, [p=0.2] oito. [p=0.2] Oito dobrado, [p=0.2] *dezesseis.* [p=0.4] {c}E o log de dez "
        "elevado a alguma coisa [p=0.2] é *o próprio expoente.*"),

    # ================= BLOCO E: CAMINHO INVERSO =================
    dict(id="12", block="inverso", text=
        "{t}E se a questão der a magnitude [p=0.2] e pedir o momento sísmico? [p=0.4] {a}Pense nas *roupas:* [p=0.2] "
        "quem se vestiu com camiseta e depois casaco, [p=0.2] tira *primeiro o casaco.* [p=0.4] {b}Desfaça de *fora "
        "para dentro.* [p=0.2] Cinco vírgula três: [p=0.2] *some dez vírgula sete,* [p=0.2] dezesseis. [p=0.4] "
        "{c}*Multiplique por três meios:* [p=0.2] vinte e quatro. [p=0.4] {d}E termine *elevando dez:* [p=0.2] dez "
        "elevado a vinte e quatro. [p=0.2] Voltamos ao começo."),

    # ================= BLOCO F: QUAL DOS DOIS? =================
    dict(id="13", block="qual", text=
        "{t}Então, de cinco para sete: [p=0.2] cem ou mil? [p=0.4] {a}*Depende da pergunta.* [p=0.4] {b}Se o "
        "enunciado fala em *amplitude* [p=0.2] ou no risco do sismógrafo: [p=0.2] *cem.* [p=0.4] {c}Se fala em "
        "*energia:* [p=0.2] *mil.* [p=0.4] {d}*Leia qual das duas* o enunciado pede. [p=0.2] As duas respostas "
        "estão lá."),

    # ================= NÓS FAZEMOS =================
    dict(id="14", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Qual é a magnitude de momento [p=0.2] de um terremoto com *M zero igual a dez elevado "
        "a vinte e um* dina centímetro? [p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="15", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}O log de dez elevado a vinte e um [p=0.2] é *vinte e um.* [p=0.4] {b}Primeiro, "
        "multiplique: [p=0.2] vinte e um dividido por três, sete; [p=0.2] dobrado, *catorze.* [p=0.4] {c}Depois, "
        "subtraia: [p=0.2] catorze menos dez vírgula sete, [p=0.2] *três vírgula três.* [p=0.4] {d}Um tremor fraco, "
        "[p=0.2] e faz sentido: [p=0.2] o expoente vinte e um é menor que o vinte e quatro de antes."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="16", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] um grau a mais: [p=0.2] amplitude vezes dez, [p=0.2] "
        "energia cerca de vezes trinta e dois. [p=0.5] {b}Dois: [p=0.2] na comparação, a constante se cancela: "
        "[p=0.2] multiplique a diferença pelo coeficiente [p=0.2] e eleve dez. [p=0.5] {c}Três: [p=0.2] na fórmula, "
        "multiplique primeiro e subtraia depois; [p=0.2] para voltar, desfaça de fora para dentro."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="17", block="erros", text=
        "{t}Agora, os dois erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] dois graus a mais, [p=0.2] *energia vezes "
        "cem.* [p=0.4] {b}Parece certo, [p=0.2] porque na amplitude é assim: [p=0.2] um zero por grau. [p=0.4] {c}Mas "
        "na energia o fator por grau é *dez elevado a um e meio.* [p=0.2] Dois graus: [p=0.2] *vezes mil.*"),
    dict(id="18", block="erros", text=
        "{a}Segundo: [p=0.2] *subtrair* o dez vírgula sete [p=0.2] *antes* de multiplicar. [p=0.4] {b}Parece certo, "
        "[p=0.2] porque parece que o dois terços [p=0.2] multiplica tudo o que vem depois dele. "
        "[p=0.4] {c}Com o dez elevado a vinte e quatro, [p=0.2] isso dá cerca de *oito vírgula nove,* [p=0.2] e não "
        "cinco vírgula três. [p=0.2] *Multiplique primeiro.*"),

    # ================= QUESTÃO 3 (EU FAÇO) =================
    dict(id="19", block="q3", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] *Eu faço,* você acompanha. [p=0.4] {a}A energia E, em "
        "joules, [p=0.2] liberada por um terremoto de magnitude M [p=0.2] pode ser estimada por *log de E igual a "
        "quatro vírgula oito mais um vírgula cinco M.* [p=0.4] {b}Comparado a um tremor de magnitude *cinco,* [p=0.2] "
        "um terremoto de magnitude *sete* [p=0.2] libera uma energia aproximadamente: [p=0.3] {qa}A: [p=0.2] três "
        "vezes maior. [p=0.2] {qb}B: [p=0.2] cem vezes. [p=0.2] {qc}C: [p=0.2] mil vezes. [p=0.2] {qd}D: [p=0.2] dez "
        "mil vezes. [p=0.2] {qe}E: [p=0.2] sessenta e três mil vezes."),
    dict(id="20", block="q3", text=
        "{t}Que pergunta é essa? [p=0.2] *Quantas vezes,* [p=0.2] e de *energia.* [p=0.4] {a}Subtraio as duas "
        "relações: [p=0.2] o quatro vírgula oito *se cancela.* [p=0.4] {b}Sobra um vírgula cinco vezes sete menos "
        "cinco: [p=0.2] *três.* [p=0.4] {c}Elevo dez: [p=0.2] *dez ao cubo, mil.* [p=0.4] {d}Faz sentido? [p=0.2] A "
        "amplitude já cresce cem vezes, [p=0.2] e a energia tem que crescer *mais.* [p=0.2] Mil é mais que cem. "
        "[p=0.3] {ok}*Letra C!*"),
    dict(id="21", block="q3", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A faz o três [p=0.2] e *esquece de elevar dez.* [p=0.4] {xb}A B é a razão "
        "das *amplitudes,* [p=0.2] dez ao quadrado. [p=0.4] {xd}A D eleva ao quadrado a razão das amplitudes. [p=0.4] "
        "{xe}E a E *mantém o quatro vírgula oito* no expoente: [p=0.2] dez elevado a quatro vírgula oito [p=0.2] dá "
        "cerca de sessenta e três mil. [p=0.2] Mas ele se cancela."),

    # ================= QUESTÃO 8 (VOCÊ FAZ) =================
    dict(id="22", block="q8", text=
        "{t}E esta [p=0.2] *você faz.* [p=0.4] {a}A magnitude de momento é *M w igual a dois terços de log de M zero, "
        "menos dez vírgula sete,* [p=0.2] com M zero em dina centímetro. [p=0.4] {b}Para um terremoto com *M zero "
        "igual a dez elevado a vinte e sete,* [p=0.2] a magnitude é: [p=0.3] {qa}A: [p=0.2] sete vírgula três. "
        "[p=0.2] {qb}B: [p=0.2] dez vírgula nove. [p=0.2] {qc}C: [p=0.2] dezoito. [p=0.2] {qd}D: [p=0.2] vinte e oito "
        "vírgula sete. [p=0.2] {qe}E: [p=0.2] vinte e nove vírgula oito. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="23", block="q8", text=
        "{t}O log de dez elevado a vinte e sete [p=0.2] é *vinte e sete.* [p=0.4] {a}Primeiro, multiplique: [p=0.2] "
        "vinte e sete dividido por três, nove; [p=0.2] dobrado, *dezoito.* [p=0.4] {b}Depois, subtraia: [p=0.2] "
        "dezoito menos dez vírgula sete, [p=0.2] *sete vírgula três.* [p=0.4] {c}Conferindo pelo caminho de volta: "
        "[p=0.2] sete vírgula três mais dez vírgula sete, dezoito; [p=0.2] vezes três meios, *vinte e sete.* [p=0.3] "
        "{ok}*Letra A!*"),
    dict(id="24", block="q8", text=
        "{t}E as outras? [p=0.3] {xb}A B *subtrai antes* de multiplicar. [p=0.4] {xc}A C *esquece* o menos dez "
        "vírgula sete. [p=0.4] {xd}A D *soma* o dez vírgula sete. [p=0.4] {xe}E a E *inverte a fração:* [p=0.2] usa "
        "três meios no lugar de dois terços."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="25", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] um grau a mais: [p=0.2] amplitude vezes dez, "
        "[p=0.2] energia cerca de vezes trinta e dois. [p=0.5] {b}Dois: [p=0.2] na comparação, a constante se "
        "cancela: [p=0.2] multiplique a diferença pelo coeficiente [p=0.2] e eleve dez. [p=0.5] {c}Três: [p=0.2] na "
        "fórmula, multiplique primeiro e subtraia depois; [p=0.2] para voltar, desfaça de fora para dentro."),

    # ================= PONTE E CTA =================
    dict(id="26", block="ponte", text=
        "{a}Duas máquinas de *oitenta decibéis* funcionando juntas [p=0.2] fazem *cento e sessenta?* [p=0.5] {b}Se "
        "fizessem, [p=0.2] uma oficina seria *mais barulhenta que um avião.* [p=0.5] {c}Próximo episódio."),
    dict(id="27", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você teria marcado cem ou mil na questão da energia? [p=0.5] "
        "{anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no "
        "*Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
