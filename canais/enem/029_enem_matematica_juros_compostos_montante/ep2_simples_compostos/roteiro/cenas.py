# Roteiro — Juros Compostos e Montante, Episódio 2 de 5: simples × compostos (reta e curva, PA e PG)
# Base: Estudos/Enem/estudos/01-matematica/14-juros-compostos-montante.html — seções 04 e 08 + Questões 4, 8 e 9 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora:
#   A RETA é uma escada de DEGRAUS IGUAIS; a CURVA é uma escada em que cada degrau é 10% MAIS ALTO que o anterior.
#   O CRUZAMENTO em t = 1: antes de um período, a reta fica por cima; depois, a curva dispara.
#   DOBRAR, DOBRAR, DOBRAR: três duplicações multiplicam por 8, não por 3.
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte.
# PG e função exponencial: só reconhecer "multiplica pelo mesmo fator" + "têm séries próprias". Decaimento: só citado.
# Taxa equivalente (dividir a taxa por 12) NÃO aparece: tem série própria.
# Exemplos:
#   Bloco a/b (material): R$ 100,00 a 10% a.a. → simples 110, 120, 130... · compostos 110, 121, 133,10 · 10 anos: 200 × 259.
#   Bloco c (material): meio ano 1,05 × √1,1 ≈ 1,0488 · 1 ano 1,10 × 1,10 · 2 anos 1,20 × 1,21.
#   Bloco f (material): dobra a cada 7 anos → 21 anos = 3 duplicações = × 8.
#   Bloco g (material): perde 20% ao ano → V0 · 0,8^t (só citado).
#   Nós fazemos (prompt): R$ 1.000,00 a 20% a.a. por 2 anos → simples 1,40 (1.400) · compostos 1,44 (1.440).
#   Erro 2 (NOSSO, para não entregar a Q8): R$ 1.000,00 por 2 anos, simples a 11% a.a. (1,22) × compostos a 10% a.a. (1,21):
#     o composto perde para uma taxa simples um pouco maior.
#   Erro 3 (NOSSO): R$ 1.000,00 que dobra a cada 5 anos, 15 anos → × 8 = R$ 8.000,00 (errado: × 3 = R$ 3.000,00).
# QUESTÃO 4 (eu faço): C. Erradas (material): A = crença comum (só vale a partir do 1º período); B = ignora que os regimes
#   são diferentes; D = inverte as faixas; E = vale só para prazos menores que um mês.
# QUESTÃO 8 (nós fazemos): I 50.000 · 0,22 · 2 = 22.000 · II 50.000 · (1,44 − 1) = 22.000 → E. Erradas (material): A calcula a
#   II como simples (50.000 · 0,20 · 2 = 20.000); B inverte a comparação errada da A; C e D = regra geral sem conta.
# QUESTÃO 9 (você faz): 21 ÷ 7 = 3 duplicações → 5.000 · 2³ = 40.000 → D. Erradas (material): A × 3 (15.000); B soma 5.000 por
#   período (20.000); C × 2 · 3 (30.000); E soma o capital de novo (45.000).
# Atalhos (verde): "o prazo decide" (< 1, = 1, > 1 período) · "n duplicações = × 2ⁿ" · "a diferença no 2º período = juros
#   sobre os juros do 1º".
# Frases-chave (meio e fim, idênticas): 1. Simples soma; composto multiplica. 2. Antes de um período, o simples rende mais;
#   depois, o composto. 3. Cada duplicação multiplica por 2: três duplicações, vezes 8.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.
# Cores dos regimes no gráfico (pedido do prompt): reta (simples) = AZUL · curva (compostos) = ROXO.

TITULO = "Juros simples × compostos: reta, curva e quem rende mais · Matemática ENEM, Juros compostos episódio 2"

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
        "{a}Um banco oferece duas modalidades de empréstimo [p=0.2] com a *mesma taxa* de *dez por cento ao mês,* "
        "[p=0.3] {b}uma *simples* [p=0.2] e uma *composta.* [p=0.4] {c}Quase todo mundo diz: [p=0.2] *a composta é "
        "sempre mais cara.* [p=0.5] {d}Para um empréstimo de *quinze dias,* [p=0.3] *é o contrário.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, você vai saber *qual regime rende mais* em cada prazo, [p=0.3] {b}reconhecer *a reta e a "
        "curva* [p=0.3] {c}e calcular *duplicações sucessivas.*"),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Da série de juros simples: [p=0.2] *M igual a C vezes, abre "
        "parênteses, um mais i vezes t.* [p=0.2] No gráfico, [p=0.2] uma *reta.* [p=0.4] {b}Do episódio 1: [p=0.2] em juros compostos, [p=0.2] *M igual a C "
        "vezes um mais i, elevado a t.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Agora, duas cenas da vida real. [p=0.3] {a}Um cliente, no banco, [p=0.2] olha as duas propostas com a "
        "mesma taxa [p=0.2] e pergunta: [p=0.2] *qual é a mais barata?* [p=0.5] {b}E uma propaganda diz: [p=0.2] "
        "*este investimento dobra a cada sete anos.* [p=0.5] "
        "{c}Guarde essas duas cenas. [p=0.2] Elas voltam."),

    # ================= BLOCO A: SOMA × MULTIPLICA =================
    dict(id="05", block="tabela", text=
        "{t}Qual é a diferença de verdade entre os dois? [p=0.4] {a}Nos juros *simples,* [p=0.2] os juros são "
        "calculados sempre sobre o *capital inicial.* [p=0.2] Cada mês *soma* o mesmo valor, [p=0.2] *C vezes i.* "
        "[p=0.4] {b}Nos *compostos,* [p=0.2] os juros são calculados sobre o *saldo anterior.* [p=0.2] Cada mês "
        "*multiplica* por *um mais i.* [p=0.4] {c}Pense em duas escadas. [p=0.2] A dos simples tem *degraus "
        "iguais.* [p=0.3] {d}A dos compostos, [p=0.2] a dez por cento, [p=0.2] tem cada degrau *dez por cento mais "
        "alto* que o anterior."),
    dict(id="06", block="tabela", text=
        "{t}E como comparar os dois numa conta só? [p=0.4] {a}Olhe só o *fator,* [p=0.2] o número que multiplica o "
        "capital. [p=0.4] {b}Nos simples: [p=0.2] *um mais i vezes t.* [p=0.4] {c}Nos compostos: [p=0.2] *um mais i, "
        "elevado a t.* [p=0.4] {d}Quem tiver o *fator maior* [p=0.2] rende mais."),

    # ================= BLOCO B: O GRÁFICO =================
    dict(id="07", block="grafico", text=
        "{t}E no desenho, como fica? [p=0.4] {a}Cem reais a *dez por cento ao ano,* [p=0.2] nos dois regimes. [p=0.4] "
        "{b}Os simples formam uma *reta,* [p=0.2] em azul: [p=0.2] sobe sempre dez. [p=0.4] {c}Os compostos formam uma "
        "*curva exponencial,* [p=0.2] em roxo: [p=0.2] uma linha que sobe *cada vez mais rápido.* [p=0.4] {d}Em dez anos: [p=0.2] *duzentos* na reta, [p=0.2] *duzentos e "
        "cinquenta e nove* na curva."),
    dict(id="08", block="grafico", text=
        "{t}Mas olhe o começo com uma lupa. [p=0.4] {a}As duas partem do *mesmo ponto,* [p=0.2] os cem reais. [p=0.4] "
        "{b}Entre zero e um ano, [p=0.2] a reta fica *ligeiramente acima* da curva. [p=0.4] {c}Em *um ano* exato, [p=0.2] elas se *encontram.* [p=0.4] {d}É o *cruzamento:* [p=0.2] antes de "
        "um período, [p=0.2] a reta fica por cima; [p=0.2] depois, [p=0.2] a curva dispara."),

    # ================= BLOCO C: O PRAZO DECIDE =================
    dict(id="09", block="prazo", text=
        "{t}Então quem rende mais? [p=0.4] {a}Depende do *prazo.* [p=0.2] Vamos comparar os fatores. [p=0.4] "
        "{b}*Meio ano:* [p=0.2] nos simples, [p=0.2] um mais zero vírgula um vezes meio, [p=0.2] *um vírgula zero "
        "cinco.* [p=0.2] Nos compostos, [p=0.2] o número que, multiplicado por ele mesmo, dá um vírgula um: [p=0.2] "
        "cerca de *um vírgula zero quatro oito oito.* [p=0.2] *Simples ganha.* [p=0.4] {c}*Um ano:* [p=0.2] um "
        "vírgula dez nos dois. [p=0.2] *Empate.* [p=0.4] {d}*Dois anos:* [p=0.2] um vírgula vinte contra *um vírgula "
        "vinte e um.* [p=0.2] *Composto ganha,* [p=0.2] e a vantagem só aumenta."),
    dict(id="10", block="prazo", text=
        "{t}O atalho para nunca errar. [p=0.3] {a}Prazo *menor* que um período: [p=0.2] *simples* rende mais. "
        "[p=0.4] {b}Exatamente *um* período: [p=0.2] *empate.* [p=0.4] {c}Prazo *maior* que um período: [p=0.2] "
        "*compostos* rendem mais."),

    # ================= BLOCO D: JUROS DE MORA =================
    dict(id="11", block="mora", text=
        "{t}E por que isso importa no mundo real? [p=0.4] {a}Lembra dos *juros de mora,* [p=0.2] a multa por dia de "
        "atraso, [p=0.2] da série de juros simples? [p=0.4] {b}Atraso de poucos dias [p=0.2] é uma *fração de mês.* "
        "[p=0.2] E em frações de mês, [p=0.2] a cobrança *simples* é a *maior* das duas. [p=0.4] {c}Por isso a mora "
        "de poucos dias [p=0.2] é cobrada em *juros simples.* [p=0.2] E o empréstimo de quinze dias do gancho [p=0.2] "
        "era *mais caro no simples.*"),

    # ================= BLOCO E: PG E EXPONENCIAL =================
    dict(id="12", block="pg", text=
        "{t}E a lista dos montantes compostos, [p=0.2] tem nome? [p=0.4] {a}Cem reais a dez por cento: [p=0.2] *cento "
        "e dez, [p=0.2] cento e vinte e um, [p=0.2] cento e trinta e três e dez centavos.* [p=0.4] {b}Cada número é o "
        "anterior *vezes um vírgula um.* [p=0.2] Uma lista em que se *multiplica* sempre pelo mesmo número [p=0.2] se "
        "chama *progressão geométrica,* [p=0.2] ou *PG.* [p=0.4] {c}Esse número é a *razão da PG:* [p=0.2] aqui, "
        "[p=0.2] *um mais i.* [p=0.4] {d}E a curva é uma *função exponencial.* [p=0.2] PG e exponencial têm *séries "
        "próprias.*"),

    # ================= BLOCO F: TEMPO DE DUPLICAÇÃO =================
    dict(id="13", block="dobra", text=
        "{t}E o investimento que dobra a cada sete anos? [p=0.4] {a}O tempo que o dinheiro leva para dobrar [p=0.2] "
        "se chama *tempo de duplicação.* [p=0.2] Na curva, [p=0.2] ele é *sempre o mesmo.* [p=0.4] {b}Em sete anos, "
        "[p=0.2] dobra: [p=0.2] *vezes dois.* [p=0.2] Nos sete seguintes, [p=0.2] dobra de novo: [p=0.2] *vezes "
        "quatro.* [p=0.2] Mais sete: [p=0.2] *vezes oito.* [p=0.4] {c}Dobrar, dobrar, dobrar: [p=0.2] *três "
        "duplicações multiplicam por oito,* [p=0.2] *não por três.*"),
    dict(id="14", block="dobra", text=
        "{t}O atalho. [p=0.3] {a}Conte as duplicações: [p=0.2] o prazo dividido pelo tempo de dobrar. [p=0.4] "
        "{b}Depois, [p=0.2] eleve *dois* a esse número. [p=0.2] Uma, vezes dois; [p=0.2] duas, vezes quatro; [p=0.2] "
        "três, vezes oito; [p=0.2] quatro, vezes dezesseis."),

    # ================= BLOCO G: DECAIMENTO =================
    dict(id="15", block="decai", text=
        "{t}E se o fator for *menor* que um? [p=0.4] {a}Aí o valor *encolhe* a cada período: [p=0.2] isso se chama "
        "*decaimento.* [p=0.4] {b}Um carro que perde *vinte por cento* do valor ao ano [p=0.2] fica, a cada ano, com "
        "*oitenta por cento:* [p=0.2] vale *V vezes zero vírgula oito, elevado a t,* [p=0.2] com V o valor inicial. [p=0.4] {c}Também tem série própria."),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}*Mil reais* a *vinte por cento ao ano,* [p=0.2] por *dois anos.* [p=0.4] {b}Quanto dá "
        "em juros *simples,* [p=0.2] e quanto em juros *compostos?* [p=0.3] *Pause e tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos, [p=0.2] fator ao lado de fator. [p=0.4] {a}Simples: [p=0.2] um mais zero vírgula dois vezes "
        "dois, [p=0.2] *um vírgula quarenta.* [p=0.2] Montante: [p=0.2] *mil e quatrocentos reais.* [p=0.4] "
        "{b}Compostos: [p=0.2] um vírgula dois ao quadrado, [p=0.2] *um vírgula quarenta e quatro.* [p=0.2] Montante: "
        "[p=0.2] *mil, quatrocentos e quarenta reais.* [p=0.4] {c}Dois anos, [p=0.2] mais que um período: [p=0.2] "
        "*composto ganha:* [p=0.2] os quarenta reais a mais são *juros sobre os juros.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] simples soma; composto multiplica. [p=0.5] {b}Dois: "
        "[p=0.2] antes de um período, o simples rende mais; depois, o composto. [p=0.5] {c}Três: [p=0.2] cada "
        "duplicação multiplica por dois: três duplicações, vezes oito."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] achar que juros compostos *sempre* rendem "
        "mais. [p=0.4] {b}Parece certo, [p=0.2] porque no longo prazo a curva dispara [p=0.2] e é isso que todo mundo "
        "vê. [p=0.4] {c}Mas antes do primeiro período, [p=0.2] o *simples* rende mais. [p=0.2] O composto só passa "
        "*depois* do cruzamento."),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] decidir pela *regra geral,* sem fazer a conta. [p=0.2] Simples a *onze por cento* ao ano "
        "[p=0.2] contra compostos a *dez,* [p=0.2] por dois anos. [p=0.4] {b}Parece certo, [p=0.2] porque as regras gerais são verdadeiras quando *o resto é igual.* "
        "[p=0.4] {c}Mas aqui as taxas são diferentes. [p=0.2] Faça a conta: [p=0.2] *um vírgula vinte e dois* contra "
        "*um vírgula vinte e um.* [p=0.2] O simples ganha."),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] *multiplicar* pelo número de duplicações. [p=0.2] Mil reais que dobram a cada cinco "
        "anos, [p=0.2] em quinze anos: [p=0.2] *três mil?* [p=0.4] {b}Parece certo, [p=0.2] porque são *três* "
        "períodos. [p=0.4] {c}Mas cada período *dobra* o anterior: [p=0.2] dois, quatro, oito. [p=0.2] *Oito mil "
        "reais.* [p=0.2] Dois *elevado* a três, [p=0.2] não dois vezes três."),

    # ================= QUESTÃO 4 (EU FAÇO) =================
    dict(id="22", block="q4", text=
        "{t}Uma questão do nosso material, [p=0.2] no estilo do ENEM. [p=0.2] Eu resolvo com você. "
        "[p=0.4] {a}Um banco oferece duas modalidades de empréstimo [p=0.2] com a mesma taxa de *dez por cento ao "
        "mês:* [p=0.2] uma a juros simples [p=0.2] e outra a juros compostos. [p=0.2] Comparando o valor a pagar ao "
        "final do prazo, [p=0.2] conclui-se que: [p=0.4] {qa}A: [p=0.2] a de juros compostos é *sempre* mais cara. "
        "[p=0.3] {qb}B: [p=0.2] as duas custam *sempre o mesmo,* [p=0.2] porque a taxa é a mesma. [p=0.3] {qc}C: "
        "[p=0.2] para prazos *menores* que um mês, [p=0.2] a simples é mais cara; [p=0.2] para *maiores,* [p=0.2] a "
        "composta. [p=0.3] {qd}D: [p=0.2] para prazos menores que um mês, [p=0.2] a composta é mais cara; [p=0.2] para "
        "maiores, [p=0.2] a simples. [p=0.3] {qe}E: [p=0.2] a de juros simples é *sempre* mais cara. [p=0.4] {c}*Pause "
        "o vídeo* [p=0.2] e tente. [p=2.0]"),
    dict(id="23", block="q4", text=
        "{t}Fator ao lado de fator. [p=0.3] {a}*Meio mês:* [p=0.2] simples, *um vírgula zero cinco;* [p=0.2] "
        "compostos, cerca de *um vírgula zero quatro nove.* [p=0.2] O simples cobra mais. [p=0.4] {b}*Um mês:* [p=0.2] "
        "um vírgula dez nos dois. [p=0.2] Empate. [p=0.4] {c}*Dois meses:* [p=0.2] um vírgula vinte contra *um vírgula "
        "vinte e um.* [p=0.2] O composto cobra mais. [p=0.4] {d}É o cruzamento da reta com a curva. [p=0.3] {ok}*Letra "
        "C!*"),
    dict(id="24", block="q4", text=
        "{t}E as outras? [p=0.4] {xa}A A é a *crença comum:* [p=0.2] só vale a partir do primeiro período. [p=0.4] "
        "{xb}A B ignora que os regimes são *diferentes:* [p=0.2] a mesma taxa não dá o mesmo valor. [p=0.4] {xd}A D "
        "*inverte as faixas.* [p=0.4] {xe}E a E só vale para prazos *menores* que um mês."),

    # ================= QUESTÃO 8 (NÓS FAZEMOS) =================
    dict(id="25", block="q8", text=
        "{t}Agora, [p=0.2] *nós fazemos* juntos. [p=0.3] {a}Um investidor tem *cinquenta mil reais* [p=0.2] para "
        "aplicar por *dois anos.* [p=0.2] Proposta um: [p=0.2] juros *simples* de *vinte e dois por cento ao ano.* "
        "[p=0.2] Proposta dois: [p=0.2] juros *compostos* de *vinte por cento ao ano.* [p=0.2] Sobre os juros ao final "
        "dos dois anos: [p=0.4] {qa}A: [p=0.2] a um rende *dois mil reais* a mais que a dois. [p=0.3] {qb}B: [p=0.2] a "
        "dois rende dois mil reais a mais que a um. [p=0.3] {qc}C: [p=0.2] a um rende mais, [p=0.2] porque sua taxa é "
        "maior. [p=0.3] {qd}D: [p=0.2] a dois rende mais, [p=0.2] porque compostos sempre superam os simples. [p=0.3] "
        "{qe}E: [p=0.2] as duas rendem *exatamente o mesmo.* [p=0.4] {c}*Pause o vídeo* [p=0.2] e tente. [p=2.0]"),
    dict(id="26", block="q8", text=
        "{t}Vamos juntos. [p=0.3] {a}Proposta um, simples: [p=0.2] cinquenta mil vezes zero vírgula vinte e dois, "
        "vezes dois: [p=0.2] *vinte e dois mil reais.* [p=0.4] {b}Proposta dois, compostos: [p=0.2] o fator é um "
        "vírgula dois ao quadrado, [p=0.2] um vírgula quarenta e quatro. [p=0.2] Os juros são a parte que passa de "
        "um: [p=0.2] *zero vírgula quarenta e quatro.* [p=0.2] Cinquenta mil vezes isso: [p=0.2] *vinte e dois mil "
        "reais.* [p=0.4] {c}*Empate!* [p=0.2] A taxa maior da um [p=0.2] compensa exatamente os juros sobre juros da "
        "dois. [p=0.3] {ok}*Letra E!*"),
    dict(id="27", block="q8", text=
        "{t}E as erradas? [p=0.4] {xa}A A calcula a proposta dois *como se fosse simples:* [p=0.2] cinquenta mil vezes "
        "zero vírgula dois vezes dois, [p=0.2] vinte mil. [p=0.4] {xb}A B *inverte* essa comparação errada. [p=0.4] "
        "{xc}A C e a D [p=0.2] decidem pela *regra geral,* [p=0.2] sem fazer a conta."),

    # ================= QUESTÃO 9 (VOCÊ FAZ) =================
    dict(id="28", block="q9", text=
        "{t}E agora, [p=0.2] é *você* quem faz. [p=0.3] {a}Numa aplicação a juros compostos, [p=0.2] o saldo *dobra a "
        "cada sete anos.* [p=0.2] Uma pessoa depositou *cinco mil reais* [p=0.2] e não fez retiradas. [p=0.2] Após "
        "*vinte e um anos,* [p=0.2] o saldo será de: [p=0.4] {qa}A: [p=0.2] quinze mil reais. [p=0.2] {qb}B: [p=0.2] "
        "vinte mil. [p=0.2] {qc}C: [p=0.2] trinta mil. [p=0.2] {qd}D: [p=0.2] quarenta mil. [p=0.2] {qe}E: [p=0.2] "
        "quarenta e cinco mil. [p=0.4] {c}*Pause o vídeo* [p=0.2] e tente. [p=2.0]"),
    dict(id="29", block="q9", text=
        "{t}Conferindo. [p=0.3] {a}Vinte e um dividido por sete: [p=0.2] *três duplicações.* [p=0.4] {b}Cinco mil, "
        "[p=0.2] dez mil, [p=0.2] vinte mil, [p=0.2] *quarenta mil.* [p=0.2] Cinco mil vezes *oito.* [p=0.3] {ok}*Letra D!*"),
    dict(id="30", block="q9", text=
        "{t}E as erradas? [p=0.4] {xa}A A multiplica por *três,* [p=0.2] o número de períodos. [p=0.4] {xb}A B *soma* "
        "cinco mil por período, [p=0.2] como em juros simples. [p=0.4] {xc}A C multiplica por *dois vezes três.* "
        "[p=0.4] {xe}E a E soma o capital *de novo* ao montante, [p=0.2] que já o contém."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="31", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] simples soma; composto multiplica. [p=0.5] "
        "{b}Dois: [p=0.2] antes de um período, o simples rende mais; depois, o composto. [p=0.5] {c}Três: [p=0.2] cada "
        "duplicação multiplica por dois: três duplicações, vezes oito."),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}A prova não deixa você calcular *um vírgula zero cinco elevado a doze* na mão. [p=0.4] {b}Ela dá uma "
        "pista, [p=0.2] tipo: [p=0.2] *um vírgula zero cinco elevado a seis [p=0.2] é mais ou menos um vírgula trinta "
        "e quatro.* [p=0.4] {c}O que fazer com ela? [p=0.3] *Próximo episódio.*"),
    dict(id="33", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você também achava que juros compostos sempre rendem mais? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
