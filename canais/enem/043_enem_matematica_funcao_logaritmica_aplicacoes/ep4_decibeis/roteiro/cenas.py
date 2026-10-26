# Roteiro — Função Logarítmica, Episódio 4 de 5: Decibéis, por que 80 + 80 não dá 160
# Base: Estudos/Enem/estudos/01-matematica/28-funcao-logaritmica-aplicacoes.html — seção 08 e o hábito 1 da seção 09,
#   mais as Questões 5, 4 e 9 da seção 12. Só a fórmula e os valores do material: β = 10 · log(I/I₀), I₀ = 10⁻¹² W/m²,
#   85 dB (limite trabalhista para 8 h sem proteção), tabela +3 dB ≈ ×2 · +10 ×10 · +20 ×100 · +40 ×10 000.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   UM ZERO A MAIS: cada 10 dB é um zero a mais na intensidade.
#   O 10 COME UM ZERO: o fator 10 da fórmula "come" um zero da diferença — divida por 10 antes de elevar.
#   O BALDE E OS COPOS: intensidades se somam como copos de água num balde; decibéis não, são só a etiqueta do balde.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte (números falados por extenso).
# Revisão rápida: log 10ⁿ = n e 10 · log 2 ≈ 3 (série de Logaritmos); G₂ ÷ G₁ = 10^(E₂ − E₁) (ep. 2); divisão de
#   potências de 10 subtrai expoentes (série de Notação científica).
# Concreto (regra 1): biblioteca, avenida movimentada, britadeira e oficina, só como "do mais baixo ao mais alto",
#   sem os números das questões.
# Blocos = seção 08: 10⁻⁵ W/m² → 10 · log 10⁷ = 70 dB; do limiar da audição ao da dor ×1 trilhão e 0 a 120 dB;
#   85 dB; a tabela; comparar (diferença ÷ 10, eleve 10); decibéis não se somam (2 máquinas de 80 → cerca de 83 dB;
#   10 máquinas → 90 dB, como no gancho).
# Exemplo NOSSO (marcado) no bloco d, para não usar os números da Q4: 90 dB contra 60 dB → 30 ÷ 10 = 3 → 1 000 vezes.
# Nós fazemos (prompt): 10⁻⁶ W/m² → 10⁻⁶ ÷ 10⁻¹² = 10⁶ → 60 dB.
# Erros (prompt): "+1 dB = ×10" (o certo é +10 dB; o exemplo usa só a tabela: dobrar já pede 3 dB) · 80 + 80 = 160.
# Acréscimos NOSSOS (marcados): três cenas verdes de ATALHO — "conte os degraus de dez acima do limiar e ponha um zero"
#   (cena 07), "o 10 come um zero: divida a diferença por 10 antes de elevar" (cena 12) e "fontes iguais: n fontes = n
#   copos; 2 → +3 dB, 10 → +10 dB" (cena 15).
# QUESTÃO 5 ("eu faço"): gabarito C (80 dB). Erradas = prompt/material (A −40 esquece de dividir por I₀; B 8 esquece o
#   fator 10; D 120 usa só o expoente de I₀; E 160 soma os expoentes em módulo, 4 + 12). Comentário: 80 dB está
#   abaixo dos 85 dB, mas perto.
# QUESTÃO 4 ("nós fazemos", com pausa): gabarito D (10 000 vezes). Erradas = material (A 2 divide os níveis; B 4 esquece
#   de elevar 10; C 40 usa a diferença como razão; E 10⁴⁰ esquece de dividir por 10).
# QUESTÃO 9 ("você faz", com pausa): gabarito D (10 máquinas no total). Erradas = material (A 2: dobrar soma só cerca de
#   3 dB, com 2 seriam 73 dB; B 4: supõe 3 dB por máquina extra; C 8: divide 80 por 10; E 11: "10 a mais", esquecendo
#   que a original já conta, com 11 seriam cerca de 80,4 dB).
#   AVISO: a regra "para ganhar 10 dB, dez fontes iguais" vem do gancho e do bloco e do próprio prompt, e é a ideia da
#   Q9. Mantivemos (desenho do usuário); os blocos usam 80 → 90 dB, e a Q9 pede 70 → 80 dB com a contagem total.
# Frases-chave (meio e fim, idênticas): 1. Cada 10 dB a mais, intensidade ×10.
#   2. Para comparar, divida a diferença por 10 e eleve 10 ao resultado.
#   3. Intensidades se somam; decibéis, não: dobrar a intensidade soma cerca de 3 dB.
# Contas conferidas em ../trabalho/conferir_contas.py.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Decibéis do zero: por que 80 + 80 não dá 160 | Função Logarítmica Ep. 4"
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
        "{a}Uma máquina faz *oitenta decibéis.* [p=0.4] {b}Ligue outra igual ao lado. [p=0.3] O barulho vai para *cento "
        "e sessenta decibéis?* [p=0.6] {c}Não: [p=0.2] vai para cerca de *oitenta e três.* [p=0.5] {d}Para chegar a "
        "*noventa decibéis,* [p=0.2] você precisaria de *dez máquinas.*"),
    dict(id="02", block="promessa", text=
        "{t}Este é o quarto episódio da série de *Função logarítmica.* [p=0.4] {a}Ao final, [p=0.2] você vai *calcular "
        "decibéis,* [p=0.3] {b}*comparar dois sons* em quantas vezes [p=0.3] {c}e *somar fontes sonoras* [p=0.2] sem cair "
        "na pegadinha."),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}Da série de Logaritmos: [p=0.2] log de dez elevado a n [p=0.2] é *n.* "
        "[p=0.2] E dez vezes log de dois [p=0.2] dá *cerca de três.* [p=0.4] {b}Do episódio dois: [p=0.2] a razão entre "
        "duas grandezas [p=0.2] é *dez elevado à diferença das leituras.* [p=0.4] {c}E, de Notação científica: [p=0.2] "
        "dividir potências de dez [p=0.2] é *subtrair os expoentes.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Pense em quatro lugares. [p=0.3] {a}Uma *biblioteca,* [p=0.2] quase silêncio. [p=0.3] {b}Uma *avenida "
        "movimentada.* [p=0.3] {c}Uma *britadeira* furando a calçada. [p=0.3] {d}E uma *oficina* cheia de máquinas. "
        "[p=0.4] {e}Cada coisa que faz barulho [p=0.2] é uma *fonte sonora.* [p=0.3] E a pergunta é: [p=0.2] como dar "
        "um número para *quão alto* é cada som?"),
    dict(id="05", block="definicoes", text=
        "{t}Primeiro, três nomes. [p=0.4] {a}*Intensidade sonora* [p=0.2] é a força do som que chega a cada pedaço do "
        "espaço. [p=0.2] Ela se mede em *watt por metro quadrado.* [p=0.4] {b}O *limiar da audição* [p=0.2] é o som mais "
        "fraco que a gente consegue ouvir: [p=0.2] *dez elevado a menos doze* watt por metro quadrado. [p=0.4] {c}E o "
        "*limiar da dor* [p=0.2] é o som tão forte que *dói.*"),

    # ================= BLOCO A: A FÓRMULA =================
    dict(id="06", block="formula", text=
        "{t}E como vira número? [p=0.4] {a}O *nível sonoro* [p=0.2] é a etiqueta do som, [p=0.2] medida em *decibéis.* "
        "[p=0.3] Beta igual a *dez vezes log de I sobre I zero.* [p=0.4] {b}Um som de *dez elevado a menos cinco.* [p=0.3] "
        "Divida pelo limiar: [p=0.2] menos cinco menos menos doze [p=0.2] dá *sete.* [p=0.2] Dez elevado a sete. [p=0.4] "
        "{c}Log disso é sete. [p=0.2] Vezes dez: [p=0.2] *setenta decibéis.*"),
    dict(id="07", block="atalho_db", text=
        "{t}Atalho para calcular decibéis. [p=0.4] {a}Conte quantos *degraus de dez* [p=0.2] a intensidade está acima do "
        "limiar. [p=0.4] {b}De menos doze até menos cinco, [p=0.2] *sete degraus.* [p=0.4] {c}Ponha um *zero* no final: "
        "[p=0.2] *setenta decibéis.*"),

    # ================= BLOCO B: 0 A 120 =================
    dict(id="08", block="escala", text=
        "{t}Por que usar log aqui? [p=0.4] {a}Do limiar da audição ao limiar da dor, [p=0.2] a intensidade cresce *um "
        "trilhão de vezes.* [p=0.4] {b}Mas a escala vai só de *zero a cento e vinte decibéis.* [p=0.3] O log *encolhe* "
        "o trilhão. [p=0.4] {c}E um número para guardar: [p=0.2] as normas trabalhistas brasileiras fixam *oitenta e "
        "cinco decibéis* [p=0.2] como limite para *oito horas* sem proteção."),

    # ================= BLOCO C: A TABELA =================
    dict(id="09", block="tabela", text=
        "{t}O que acontece quando o medidor sobe? [p=0.4] {a}Mais *dez* decibéis: [p=0.2] intensidade *vezes dez.* "
        "[p=0.3] {b}Mais *vinte:* [p=0.2] *vezes cem.* [p=0.3] {c}Mais *quarenta:* [p=0.2] *vezes dez mil.* [p=0.4] "
        "{d}Cada dez decibéis [p=0.2] é *um zero a mais* na intensidade."),
    dict(id="10", block="tabela", text=
        "{t}E mais *três* decibéis? [p=0.4] {a}Dez vezes log de dois [p=0.2] dá cerca de três. [p=0.4] {b}Então mais três "
        "decibéis [p=0.2] é intensidade *vezes dois,* [p=0.2] aproximadamente. [p=0.4] {c}Dobrar o som [p=0.2] soma só "
        "*três* na etiqueta."),

    # ================= BLOCO D: COMPARAR =================
    dict(id="11", block="comparar", text=
        "{t}Um som de *noventa* decibéis [p=0.2] é quantas vezes mais intenso [p=0.2] que um de *sessenta?* [p=0.4] "
        "{a}Primeiro, [p=0.2] a *diferença:* [p=0.2] trinta decibéis. [p=0.4] {b}Agora, *divida por dez,* [p=0.2] o número "
        "que está na frente do log. [p=0.2] Dá *três.* [p=0.4] {c}E eleve dez a isso: [p=0.2] *mil vezes.*"),
    dict(id="12", block="atalho_cmp", text=
        "{t}Atalho para comparar. [p=0.4] {a}É a regra do episódio dois, [p=0.2] com um detalhe: [p=0.2] o *dez* da "
        "fórmula [p=0.2] *come um zero* da diferença. [p=0.4] {b}Trinta vira três. [p=0.2] Quarenta vira quatro. [p=0.4] "
        "{c}Sempre *divida por dez* [p=0.2] *antes* de elevar."),

    # ================= BLOCO E: NÃO SE SOMAM =================
    dict(id="13", block="somar", text=
        "{t}E duas máquinas juntas? [p=0.4] {a}Pense num *balde.* [p=0.2] Cada máquina despeja um *copo* de intensidade. "
        "[p=0.4] {b}Intensidades *se somam,* [p=0.2] como copos de água no balde. [p=0.4] {c}O decibel *não* é a água: "
        "[p=0.2] é só a *etiqueta* do balde. [p=0.4] {d}Dois copos iguais *dobram* a água. [p=0.2] E dobrar soma cerca "
        "de três: [p=0.2] de oitenta para *perto de oitenta e três.*"),
    dict(id="14", block="somar", text=
        "{t}E para a etiqueta subir *dez?* [p=0.4] {a}A intensidade precisa ficar *dez vezes* maior. [p=0.4] {b}Então "
        "são *dez copos.* [p=0.2] Dez fontes iguais. [p=0.4] {c}Só com o *décimo* copo [p=0.2] o medidor sai de oitenta "
        "[p=0.2] e chega a *noventa.*"),
    dict(id="15", block="atalho_som", text=
        "{t}Atalho para fontes iguais. [p=0.4] {a}Conte as fontes como *copos.* [p=0.4] {b}Duas fontes: [p=0.2] *mais "
        "três* decibéis. [p=0.3] {c}Dez fontes: [p=0.2] *mais dez* decibéis. [p=0.4] {d}Nunca some as etiquetas."),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Um som de intensidade *dez elevado a menos seis* watt por metro quadrado [p=0.2] tem "
        "quantos decibéis? [p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Divida pelo limiar: [p=0.2] dez elevado a menos seis, [p=0.2] sobre dez elevado a "
        "menos doze. [p=0.2] Subtraia os expoentes: [p=0.2] *dez elevado a seis.* [p=0.4] {b}Log disso é seis. [p=0.3] "
        "Vezes dez: [p=0.2] *sessenta decibéis.* [p=0.4] {c}Pelo atalho: [p=0.2] seis degraus acima do limiar, [p=0.2] "
        "ponha um zero."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] cada dez decibéis a mais, [p=0.2] intensidade vezes dez. "
        "[p=0.5] {b}Dois: [p=0.2] para comparar, [p=0.2] divida a diferença por dez [p=0.2] e eleve dez ao resultado. "
        "[p=0.5] {c}Três: [p=0.2] intensidades se somam; [p=0.2] decibéis, não: [p=0.2] dobrar a intensidade soma cerca "
        "de três decibéis."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os dois erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que *um* decibel a mais [p=0.2] é "
        "intensidade *vezes dez.* [p=0.4] {b}Parece certo, [p=0.2] porque o log *conta zeros,* [p=0.2] e cada degrau "
        "parece valer um zero. [p=0.4] {c}Mas o dez da fórmula [p=0.2] espalha cada zero por *dez decibéis.* [p=0.2] "
        "Dobrar já pede três. [p=0.2] Vezes dez pede *dez decibéis.*"),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] oitenta mais oitenta [p=0.2] igual a *cento e sessenta.* [p=0.4] {b}Parece certo, [p=0.2] "
        "porque duas máquinas *somam* barulho. [p=0.4] {c}E somam mesmo, [p=0.2] mas somam *intensidade,* [p=0.2] não "
        "etiqueta. [p=0.2] A intensidade dobra, [p=0.2] e o nível vai para *cerca de oitenta e três.*"),

    # ================= QUESTÃO 5 (EU FAÇO) =================
    dict(id="21", block="q5", text=
        "{t}Agora, questões no estilo do ENEM. [p=0.2] Esta, [p=0.2] *eu faço.* [p=0.4] {a}O nível sonoro beta é dado "
        "por dez vezes log de I sobre I zero, [p=0.2] com I zero igual a dez elevado a menos doze. [p=0.3] Perto de uma "
        "*britadeira,* [p=0.2] mediu-se *dez elevado a menos quatro* watt por metro quadrado. [p=0.3] O nível sonoro é: "
        "[p=0.3] {qa}A: [p=0.2] menos quarenta. [p=0.2] {qb}B: [p=0.2] oito. [p=0.2] {qc}C: [p=0.2] oitenta. [p=0.2] "
        "{qd}D: [p=0.2] cento e vinte. [p=0.2] {qe}E: [p=0.2] cento e sessenta decibéis."),
    dict(id="22", block="q5", text=
        "{t}Qual dos cálculos é? [p=0.2] *Calcular decibéis.* [p=0.4] {a}Divida pelo limiar: [p=0.2] menos quatro menos "
        "menos doze [p=0.2] dá *oito.* [p=0.2] Dez elevado a oito. [p=0.4] {b}Log disso é oito. [p=0.2] Vezes dez: "
        "[p=0.2] *oitenta decibéis.* [p=0.3] {ok}*Letra C!* [p=0.4] {c}E repare: [p=0.2] oitenta está *abaixo* dos "
        "oitenta e cinco, [p=0.2] mas bem perto do limite."),
    dict(id="23", block="q5", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A esquece de *dividir por I zero.* [p=0.4] {xb}A B esquece o *dez* da "
        "fórmula. [p=0.4] {xd}A D usa só o *expoente* do limiar: [p=0.2] dez vezes doze. [p=0.4] {xe}E a E *soma* os "
        "expoentes, [p=0.2] quatro mais doze, [p=0.2] em vez de subtrair."),

    # ================= QUESTÃO 4 (NÓS FAZEMOS) =================
    dict(id="24", block="q4", text=
        "{t}Esta, [p=0.2] a gente faz *junto.* [p=0.4] {a}Numa *avenida movimentada,* [p=0.2] mediu-se *oitenta* "
        "decibéis. [p=0.2] Numa *biblioteca,* [p=0.2] *quarenta.* [p=0.3] A intensidade na avenida, [p=0.2] em relação à "
        "da biblioteca, é: [p=0.3] {qa}A: [p=0.2] duas vezes maior. [p=0.2] {qb}B: [p=0.2] quatro vezes. [p=0.2] "
        "{qc}C: [p=0.2] quarenta vezes. [p=0.2] {qd}D: [p=0.2] dez mil vezes. [p=0.2] {qe}E: [p=0.2] dez elevado a "
        "quarenta vezes. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="25", block="q4", text=
        "{t}Vamos juntos. [p=0.2] É *comparar.* [p=0.4] {a}A diferença: [p=0.2] *quarenta* decibéis. [p=0.4] {b}Divida "
        "por dez: [p=0.2] *quatro.* [p=0.4] {c}Eleve dez a quatro: [p=0.2] *dez mil vezes.* [p=0.3] {ok}*Letra D!*"),
    dict(id="26", block="q4", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A *divide* os níveis, [p=0.2] oitenta por quarenta. [p=0.4] {xb}A B para no "
        "quatro [p=0.2] e esquece de *elevar dez.* [p=0.4] {xc}A C usa a *diferença* como resposta. [p=0.4] {xe}E a E "
        "esquece de *dividir por dez.*"),

    # ================= QUESTÃO 9 (VOCÊ FAZ) =================
    dict(id="27", block="q9", text=
        "{t}E esta [p=0.2] *você faz.* [p=0.4] {a}Numa *oficina,* [p=0.2] uma máquina produz *setenta* decibéis. [p=0.3] "
        "O dono quer instalar outras máquinas *idênticas,* [p=0.2] para que *todas juntas* produzam *oitenta.* [p=0.3] "
        "As intensidades de fontes iguais se somam. [p=0.3] O número *total* de máquinas deve ser: [p=0.3] {qa}A: "
        "[p=0.2] duas. [p=0.2] {qb}B: [p=0.2] quatro. [p=0.2] {qc}C: [p=0.2] oito. [p=0.2] {qd}D: [p=0.2] dez. [p=0.2] "
        "{qe}E: [p=0.2] onze. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="28", block="q9", text=
        "{t}Vamos conferir. [p=0.3] {a}De setenta para oitenta, [p=0.2] mais *dez* decibéis. [p=0.4] {b}Mais dez é "
        "intensidade *vezes dez.* [p=0.4] {c}Como os copos se somam, [p=0.2] são *dez máquinas no total.* [p=0.3] "
        "{ok}*Letra D!*"),
    dict(id="29", block="q9", text=
        "{t}E as armadilhas? [p=0.3] {xa}A A acha que dobrar soma dez. [p=0.2] Com duas, [p=0.2] seriam só *setenta e "
        "três.* [p=0.4] {xb}A B supõe que cada máquina extra soma três. [p=0.4] {xc}A C divide *oitenta por dez.* "
        "[p=0.4] {xe}E a E pensa em *dez a mais,* [p=0.2] esquecendo que a primeira *já conta.* [p=0.2] Com onze, "
        "[p=0.2] cerca de *oitenta vírgula quatro.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] cada dez decibéis a mais, [p=0.2] intensidade "
        "vezes dez. [p=0.5] {b}Dois: [p=0.2] para comparar, [p=0.2] divida a diferença por dez [p=0.2] e eleve dez ao "
        "resultado. [p=0.5] {c}Três: [p=0.2] intensidades se somam; [p=0.2] decibéis, não: [p=0.2] dobrar a intensidade "
        "soma cerca de três decibéis."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}No último episódio deste assunto, [p=0.2] juntamos *pH,* [p=0.2] *terremotos* e *decibéis,* [p=0.4] "
        "{b}*caçamos as pegadinhas* [p=0.4] {c}e treinamos com questões de *Química,* [p=0.2] *Física* e *Geografia.*"),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual é o lugar mais barulhento que você frequenta? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
