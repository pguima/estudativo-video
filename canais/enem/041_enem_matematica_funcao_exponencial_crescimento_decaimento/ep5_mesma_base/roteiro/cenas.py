# Roteiro — Função Exponencial, Episódio 5 de 6: equações e inequações exponenciais, mesma base
# Base: Estudos/Enem/estudos/01-matematica/26-funcao-exponencial-crescimento-decaimento.html — seções 07 e 08 + Questões 4 e 7.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   AS FOTOS IDÊNTICAS: duas potências de mesma base iguais são duas fotos idênticas do mesmo objeto → expoentes iguais.
#   TIRE A EMBALAGEM: isole a potência (divida pelo número da frente) antes de comparar.
#   A LADEIRA: base entre 0 e 1 é uma ladeira descendo; mais alto = mais para trás (menor x) → a desigualdade vira.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Equações que não fecham (2ˣ = 10): só a promessa do logaritmo (próxima série).
# ORDEM: blocos a–f, depois o "nós fazemos" (8ˣ = 32) e a mini-recapitulação (as 3 frases já ensinadas), e o bloco g
#   (contexto) abre a parte 2, antes dos erros e das questões.
# DESVIO DO PROMPT: o bloco g pedia o remédio de 400 mg/L que cai à metade a cada 4 h e fica acima de 50 mg/L (t < 12 h),
#   que é exatamente a Questão 7 ("você faz", com pausa) e entregaria a resposta. O bloco g usa um exemplo NOSSO com o
#   mesmo raciocínio: o cloro da piscina, 8 mg/L, cai à metade a cada 3 h, age enquanto está acima de 1 mg/L →
#   8 · (1/2)^(t/3) > 1 → (1/2)^(t/3) > (1/2)³ → t/3 < 3 → t < 9 h. O gancho e o bloco c usam a Q4 ("eu faço"), como o
#   prompt pede. A abertura concreta só PERGUNTA "quando o remédio cai a 50?", sem dados.
# Nós fazemos (prompt): 8ˣ = 32 → 2^(3x) = 2⁵ → x = 5/3.
# Erros (prompt): coeficiente na frente (1 000 · 3ᵗ = 81 000: divida antes → t = 4) · (1/3)ˣ > 9 ⇒ x > −2 (certo x < −2) ·
#   2^(x+1) tratado como 2ˣ + 1 (certo 2 · 2ˣ; no exemplo do bloco d o erro dá 2ˣ = 11,5, que não fecha).
# QUESTÃO 4 ("eu faço"): gabarito B (8 anos). Erradas = material/prompt (A 4 esquece a divisão do expoente; C 27 divide
#   81 por 3; D 54 trata o expoente como produto; E 162 iguala o expoente ao valor).
# QUESTÃO 7 ("você faz", com pausa): gabarito C (12 h), pelos dois caminhos. Erradas = material/prompt (A 7 h queda linear;
#   B 8 h para em 100; D 16 h uma meia-vida a mais; E 32 h trata o 8 como número de meias-vidas, quando 8 = 2³).
# Acréscimos NOSSOS (marcados): cenas verdes de ATALHO — "traduza cada número para a menor base" (cena 09), "confira
#   devolvendo o valor na equação" (cena 11), "um pacote mais dois pacotes" (cena 13), "base entre 0 e 1: vire o sinal;
#   na dúvida, teste um número" (cena 20); a estimativa 2³ < 10 < 2⁴ no bloco e.
# Frases-chave (meio e fim, idênticas): 1. Mesma base dos dois lados: iguale os expoentes.
#   2. Isole a potência antes de comparar expoentes.  3. Base entre 0 e 1 inverte a desigualdade.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Equação exponencial do zero: mesma base e a desigualdade que vira | Função Exponencial Ep. 5"
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
        "{a}*Mil vezes três elevado a t sobre dois* [p=0.2] *igual a oitenta e um mil.* [p=0.5] {b}Quem compara os "
        "expoentes direto [p=0.2] *se perde.* [p=0.5] {c}Quem *divide por mil* primeiro [p=0.2] chega a três elevado a t "
        "sobre dois [p=0.2] igual a *três elevado a quatro* [p=0.3] {d}e resolve de cabeça: [p=0.3] *t igual a oito.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o quinto episódio da série de *Função exponencial.* [p=0.4] {a}Ao final, [p=0.2] você vai resolver "
        "*equações e inequações exponenciais* [p=0.3] {b}pondo tudo na *mesma base,* [p=0.3] {c}e saber *quando a "
        "desigualdade vira.*"),
    dict(id="03", block="prereq", text=
        "{t}Lembretes rápidos, da série de Potenciação. [p=0.3] {a}Quatro, oito e trinta e dois: [p=0.2] dois elevado a "
        "dois, três e cinco. [p=0.4] {b}Nove, vinte e sete e oitenta e um: [p=0.2] três elevado a dois, três e quatro. "
        "[p=0.4] {c}Um oitavo é dois elevado a *menos três.* [p=0.4] {d}Potência de potência *multiplica* os expoentes. "
        "[p=0.4] {e}E do episódio um: [p=0.2] base maior que um *sobe;* [p=0.2] entre zero e um, *desce.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Perguntas de verdade. [p=0.4] {a}*Quando* a população de aves de uma reserva [p=0.2] chega a *oitenta e um "
        "mil?* [p=0.4] {b}*Quando* um remédio no sangue [p=0.2] cai a *cinquenta miligramas por litro?* [p=0.4] {c}Nas "
        "duas, [p=0.2] o que a gente procura [p=0.2] está *no expoente.* [p=0.4] {d}Uma *equação exponencial* [p=0.2] é "
        "isso: [p=0.2] uma equação com a incógnita *no expoente.*"),

    # ================= BLOCO A: A IDEIA =================
    dict(id="05", block="ideia", text=
        "{t}Como tirar o x lá de cima? [p=0.4] {a}Escreva os dois lados como potências da *mesma base:* [p=0.2] o mesmo "
        "número sendo multiplicado. [p=0.4] {b}Duas potências de mesma base iguais [p=0.2] são *duas fotos idênticas* do "
        "mesmo objeto: [p=0.3] os expoentes *também* são iguais. [p=0.4] {c}Isso vale porque a exponencial é *injetora:* "
        "[p=0.2] x diferentes dão potências *diferentes.*"),

    # ================= BLOCO B: A TABELA =================
    dict(id="06", block="tab1", text=
        "{t}Primeiro exemplo. [p=0.3] {a}Dois elevado a x mais um [p=0.2] igual a *trinta e dois.* [p=0.4] {b}Trinta e "
        "dois é dois elevado a *cinco.* [p=0.4] {c}Mesma base, [p=0.2] fotos idênticas: [p=0.2] x mais um [p=0.2] igual a "
        "cinco. [p=0.3] {d}*x igual a quatro.*"),
    dict(id="07", block="tab2", text=
        "{t}E quando as bases são *diferentes?* [p=0.4] {a}Nove elevado a x [p=0.2] igual a *vinte e sete.* [p=0.4] "
        "{b}Nove e vinte e sete são *filhos do três.* [p=0.3] Nove é três ao quadrado; [p=0.2] vinte e sete, três ao cubo. "
        "[p=0.4] {c}Três ao quadrado, elevado a x, [p=0.2] vira três elevado a *dois x.* [p=0.4] {d}Então dois x [p=0.2] "
        "igual a três, [p=0.2] e *x igual a três meios.*"),
    dict(id="08", block="tab3", text=
        "{t}E com fração? [p=0.4] {a}Quatro elevado a x [p=0.2] igual a *um oitavo.* [p=0.4] {b}Quatro é dois ao quadrado. "
        "[p=0.2] E um oitavo [p=0.2] é dois elevado a *menos três.* [p=0.4] {c}Dois elevado a dois x [p=0.2] igual a dois "
        "elevado a menos três. [p=0.4] {d}*x igual a menos três meios.* [p=0.3] Negativo, [p=0.2] porque o resultado é "
        "menor que um."),
    dict(id="09", block="atalho_base", text=
        "{t}Atalho para achar a base. [p=0.4] {a}Pergunte: [p=0.2] qual é o *menor número* que gera os dois lados? "
        "[p=0.4] {b}Quatro, oito, dezesseis, trinta e dois: [p=0.2] o *dois.* [p=0.3] Nove, vinte e sete, oitenta e um: "
        "[p=0.2] o *três.* [p=0.4] {c}Traduza *cada* número para essa base [p=0.2] antes de qualquer conta."),

    # ================= BLOCO C: ISOLE A POTÊNCIA =================
    dict(id="10", block="isolar", text=
        "{t}E se tiver um número *na frente* da potência? [p=0.4] {a}Mil vezes três elevado a t sobre dois [p=0.2] igual "
        "a oitenta e um mil. [p=0.4] {b}*Isolar a potência* [p=0.2] é deixá-la *sozinha* de um lado, [p=0.2] como quem "
        "*tira a embalagem* antes de comparar dois produtos. [p=0.4] {c}Divida por mil: [p=0.2] três elevado a t sobre "
        "dois [p=0.2] igual a *oitenta e um.* [p=0.4] {d}A pergunta em voz alta: [p=0.2] *cada lado é uma potência só, da"
        " mesma base?* [p=0.3] Sim: [p=0.2] três elevado a quatro. [p=0.4] {e}t sobre dois igual a quatro, [p=0.2] *t "
        "igual a oito.*"),
    dict(id="11", block="atalho_conf", text=
        "{t}Atalho para não errar: [p=0.2] *confira.* [p=0.4] {a}Devolva o oito: [p=0.2] oito sobre dois é quatro, "
        "[p=0.2] três elevado a quatro é oitenta e um. [p=0.4] {b}Vezes mil: [p=0.2] *oitenta e um mil.* [p=0.3] Bateu."),

    # ================= BLOCO D: DUAS POTÊNCIAS SOMADAS =================
    dict(id="12", block="evidencia", text=
        "{t}E com *duas potências somadas?* [p=0.4] {a}Dois elevado a x, [p=0.2] mais dois elevado a x mais um, [p=0.2] "
        "igual a *vinte e quatro.* [p=0.4] {b}O segredo: [p=0.2] dois elevado a x mais um [p=0.2] é *dois vezes* dois "
        "elevado a x. [p=0.4] {c}*Colocar em evidência* [p=0.2] é pôr o que se repete para fora de um parêntese: [p=0.2] "
        "dois elevado a x, [p=0.2] vezes um mais dois. [p=0.4] {d}Então dois elevado a x [p=0.2] igual a *oito,* [p=0.2] "
        "e *x igual a três.*"),
    dict(id="13", block="atalho_pacote", text=
        "{t}Atalho para enxergar isso. [p=0.4] {a}Chame dois elevado a x de *um pacote.* [p=0.3] {b}O dois elevado a x "
        "mais um [p=0.2] são *dois pacotes.* [p=0.4] {c}*Três pacotes* valem vinte e quatro: [p=0.2] cada um vale oito."),

    # ================= BLOCO E: QUANDO NÃO FECHA =================
    dict(id="14", block="naofecha", text=
        "{t}E se a base *não fecha?* [p=0.4] {a}Dois elevado a x [p=0.2] igual a *dez.* [p=0.4] {b}Dois ao cubo é oito; "
        "[p=0.2] dois elevado a quatro, dezesseis. [p=0.3] O x fica *entre três e quatro.* [p=0.4] {c}O valor exato "
        "[p=0.2] pede o *logaritmo,* [p=0.2] a *próxima série.*"),

    # ================= BLOCO F: INEQUAÇÕES =================
    dict(id="15", block="ineq1", text=
        "{t}E quando, em vez de *igual,* [p=0.2] aparece *maior* ou *menor?* [p=0.4] {a}Isso é uma *inequação:* [p=0.2] a"
        " resposta é uma *faixa.* [p=0.4] {b}E o *sentido da desigualdade* [p=0.2] diz se o sinal é de maior ou de menor."
        " [p=0.4] {c}Dois elevado a x [p=0.2] maior que dezesseis, [p=0.2] que é dois elevado a quatro. [p=0.4] {d}Base "
        "*maior que um:* [p=0.2] o sentido *se mantém.* [p=0.3] *x maior que quatro.*"),
    dict(id="16", block="ineq2", text=
        "{t}Agora, com base *entre zero e um.* [p=0.4] {a}Um terço elevado a x [p=0.2] maior que *nove.* [p=0.4] {b}Nove é "
        "um terço elevado a *menos dois:* [p=0.2] o expoente negativo inverte a fração. [p=0.4] {c}E aqui [p=0.2] o sinal "
        "*vira:* [p=0.3] *x menor que menos dois.*"),
    dict(id="17", block="ladeira", text=
        "{t}Por que o sinal vira? [p=0.4] {a}O gráfico de um terço elevado a x [p=0.2] é uma *ladeira descendo.* [p=0.4] "
        "{b}Quanto *mais alto* o valor, [p=0.2] *mais para trás* você está: [p=0.2] menor x. [p=0.4] {c}Para ficar "
        "*acima* do nove, [p=0.2] você tem de estar *à esquerda* do menos dois. [p=0.4] {d}Teste: [p=0.2] x igual a menos"
        " três dá *vinte e sete,* [p=0.2] maior que nove. [p=0.2] Confere."),
    dict(id="18", block="atalho_sinal", text=
        "{t}Atalho para nunca esquecer. [p=0.4] {a}Antes de comparar os expoentes, [p=0.2] *olhe a base.* [p=0.4] "
        "{b}Maior que um: [p=0.2] *copie* o sinal. [p=0.3] Entre zero e um: [p=0.2] *vire* o sinal. [p=0.4] {c}Na dúvida,"
        " [p=0.2] *teste um número* da sua resposta."),

    # ================= NÓS FAZEMOS =================
    dict(id="19", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Resolva: [p=0.2] *oito elevado a x [p=0.2] igual a trinta e dois.* [p=0.4] {b}Dica: "
        "[p=0.2] ache a menor base dos dois. [p=0.3] {c}*Pause e tente.* [p=2.0]"),
    dict(id="20", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Oito e trinta e dois são *filhos do dois:* [p=0.2] dois ao cubo [p=0.2] e dois "
        "elevado a cinco. [p=0.4] {b}Dois elevado a três x [p=0.2] igual a dois elevado a cinco. [p=0.4] {c}Três x igual "
        "a cinco: [p=0.2] *x igual a cinco terços.* [p=0.3] Fração também é resposta."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="21", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] mesma base dos dois lados: [p=0.2] iguale os expoentes. "
        "[p=0.5] {b}Dois: [p=0.2] isole a potência antes de comparar expoentes. [p=0.5] {c}Três: [p=0.2] base entre zero e "
        "um inverte a desigualdade."),

    # ================= BLOCO G: EM CONTEXTO =================
    dict(id="22", block="contexto", text=
        "{t}E numa situação real? [p=0.4] {a}O cloro de uma piscina [p=0.2] começa em *oito miligramas por litro* [p=0.2]"
        " e cai *à metade* a cada *três horas.* [p=0.3] Ele age enquanto está *acima de um.* [p=0.4] {b}A inequação: "
        "[p=0.2] oito vezes um meio elevado a t sobre três [p=0.2] *maior que um.* [p=0.4] {c}Divida por oito: [p=0.2] um"
        " oitavo é *um meio ao cubo.* [p=0.4] {d}Base entre zero e um: [p=0.2] o sinal *vira.* [p=0.3] t sobre três menor"
        " que três, [p=0.2] *t menor que nove horas.*"),

    # ================= ERROS CLÁSSICOS =================
    dict(id="23", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] igualar expoentes com um número *na frente,* "
        "[p=0.2] em mil vezes três elevado a t igual a oitenta e um mil. [p=0.4] {b}Parece certo, [p=0.2] porque a "
        "potência de três *está ali,* [p=0.2] pedindo comparação. [p=0.4] {c}Mas o mil é a embalagem. [p=0.2] *Divida por"
        " mil antes:* [p=0.2] três elevado a t igual a oitenta e um, [p=0.2] t igual a quatro."),
    dict(id="24", block="erros", text=
        "{a}Segundo: [p=0.2] um terço elevado a x maior que nove [p=0.2] virar *x maior que menos dois.* [p=0.4] {b}Parece "
        "certo, [p=0.2] porque em todas as outras contas [p=0.2] o sinal foi *copiado.* [p=0.4] {c}Mas a base está entre "
        "zero e um: [p=0.2] a ladeira desce, [p=0.2] e o sinal *vira.* [p=0.3] *x menor que menos dois.*"),
    dict(id="25", block="erros", text=
        "{a}Terceiro: [p=0.2] ler dois elevado a x mais um [p=0.2] como *dois elevado a x, mais um.* [p=0.4] {b}Parece "
        "certo, [p=0.2] porque o mais um *está escrito ali.* [p=0.2] Só que ele está *no expoente.* [p=0.4] {c}É *dois "
        "vezes* dois elevado a x: [p=0.2] um pacote a mais, [p=0.2] não uma unidade a mais."),

    # ================= QUESTÃO 4 (EU FAÇO) =================
    dict(id="26", block="q4", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.2] Esta, [p=0.2] *eu faço.* [p=0.4] {a}Um estudo projetou que a "
        "população de uma espécie de ave numa reserva, [p=0.2] t anos depois de um programa de proteção, [p=0.2] seria P "
        "de t [p=0.2] igual a mil vezes três elevado a t sobre dois. [p=0.3] Segundo esse modelo, [p=0.2] a população "
        "atingirá oitenta e um mil aves após: [p=0.3] {qa}A: [p=0.2] quatro anos. [p=0.2] {qb}B: [p=0.2] oito anos. "
        "[p=0.2] {qc}C: [p=0.2] vinte e sete anos. [p=0.2] {qd}D: [p=0.2] cinquenta e quatro anos. [p=0.2] {qe}E: [p=0.2]"
        " cento e sessenta e dois anos."),
    dict(id="27", block="q4", text=
        "{t}Qual dos casos é este? [p=0.3] Uma *equação,* [p=0.2] com número na frente. [p=0.4] {a}Tire a embalagem: "
        "[p=0.2] divida por mil. [p=0.2] Três elevado a t sobre dois [p=0.2] igual a oitenta e um. [p=0.4] {b}Cada lado é"
        " uma potência só, da mesma base? [p=0.2] Sim: [p=0.2] três elevado a quatro. [p=0.4] {c}t sobre dois igual a "
        "quatro, [p=0.2] *t igual a oito anos.* [p=0.3] {ok}*Letra B!*"),
    dict(id="28", block="q4", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A resolve três elevado a t igual a oitenta e um, [p=0.2] *esquecendo* de dividir "
        "o expoente por dois. [p=0.4] {xc}A C divide oitenta e um por três, [p=0.2] como se fosse três vezes t. [p=0.4] "
        "{xd}A D trata o expoente como *produto:* [p=0.2] três vezes t sobre dois igual a oitenta e um. [p=0.4] {xe}E a E "
        "iguala o expoente *ao valor:* [p=0.2] t sobre dois igual a oitenta e um."),

    # ================= QUESTÃO 7 (VOCÊ FAZ) =================
    dict(id="29", block="q7", text=
        "{t}E esta [p=0.2] *você faz.* [p=0.4] {a}Logo após a aplicação de um medicamento, [p=0.2] a concentração dele no "
        "sangue [p=0.2] é de *quatrocentos miligramas por litro.* [p=0.3] A partir daí, [p=0.2] ela cai *pela metade* a "
        "cada *quatro horas.* [p=0.3] O médico orientou uma nova dose [p=0.2] quando a concentração atingir *cinquenta.* "
        "[p=0.3] A nova dose deve ser dada, após a primeira, em: [p=0.3] {qa}A: [p=0.2] sete horas. [p=0.2] {qb}B: [p=0.2] "
        "oito horas. [p=0.2] {qc}C: [p=0.2] doze horas. [p=0.2] {qd}D: [p=0.2] dezesseis horas. [p=0.2] {qe}E: [p=0.2] "
        "trinta e duas horas. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="30", block="q7", text=
        "{t}Vamos conferir, [p=0.2] por *dois caminhos.* [p=0.4] {a}Contando as metades: [p=0.2] quatrocentos, duzentos, "
        "cem, cinquenta. [p=0.2] *Três* meias-vidas, [p=0.2] três vezes quatro, [p=0.2] *doze horas.* [p=0.4] {b}Pela "
        "equação: [p=0.2] quatrocentos vezes um meio elevado a t sobre quatro [p=0.2] igual a cinquenta. [p=0.3] Divida por "
        "quatrocentos: [p=0.2] um oitavo, [p=0.2] que é um meio ao cubo. [p=0.4] {c}t sobre quatro igual a três, [p=0.2] "
        "*t igual a doze.* [p=0.3] Os dois caminhos batem. [p=0.3] {ok}*Letra C!*"),
    dict(id="31", block="q7", text=
        "{t}E as erradas? [p=0.3] {xa}A A supõe queda *linear:* [p=0.2] se caiu duzentos em quatro horas, [p=0.2] cairia "
        "cinquenta por hora. [p=0.4] {xb}A B para em *cem,* [p=0.2] com duas meias-vidas. [p=0.4] {xd}A D aplica uma "
        "meia-vida *a mais,* [p=0.2] e chega a vinte e cinco. [p=0.4] {xe}E a E divide quatrocentos por cinquenta, [p=0.2] "
        "acha *oito,* [p=0.2] e trata o oito como número de meias-vidas. [p=0.3] Mas oito é dois ao cubo: [p=0.2] *três* "
        "meias-vidas."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="32", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] mesma base dos dois lados: [p=0.2] iguale os "
        "expoentes. [p=0.5] {b}Dois: [p=0.2] isole a potência antes de comparar expoentes. [p=0.5] {c}Três: [p=0.2] base "
        "entre zero e um inverte a desigualdade."),

    # ================= PONTE E CTA =================
    dict(id="33", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos *tudo,* [p=0.3] {b}caçamos as *pegadinhas* [p=0.3] {c}e "
        "treinamos com questões que misturam *Biologia, Química e Física.*"),
    dict(id="34", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual dos três erros clássicos *você* já cometeu? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
