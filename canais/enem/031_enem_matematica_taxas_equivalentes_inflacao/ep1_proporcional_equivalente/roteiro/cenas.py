# Roteiro — Taxas Equivalentes e Inflação, Episódio 1 de 5: proporcional × equivalente, como trocar o período de uma taxa
# Base: Estudos/Enem/estudos/01-matematica/16-taxas-equivalentes-inflacao.html — seções 02 e 03 + Questões 1, 2 e 9 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   Taxas equivalentes são o MESMO DESTINO por caminhos diferentes: mesmo capital, mesmo prazo, mesmo montante no fim.
#   FATOR PRIMEIRO, TAXA DEPOIS: taxa vira fator (1 + i), a conta é com o fator, no fim tira o 1 (a tesoura corta o "1,").
#   A proporcional segue a RETA (soma 2% por mês); a equivalente segue a CURVA (multiplica por 1,02). A diferença é o juro
#   sobre juro.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# DESVIO DO PROMPT (regra de exemplos): o bloco d e o erro 2 pediam 44% a.a. → 20% a.s. (proporcional 22%), que é a resposta
#   da Questão 9, a "você faz". O vídeo usa 69% ao ano → 1,69 = 1,3² → 30% ao semestre (proporcional 34,5%; 1,345² ≈ 1,809,
#   quase 81% no ano). A Q9 continua com os 44% do material e é resolvida por raiz (1,2² = 1,44 → 20% a.s.).
# Atalhos (verde): "dois períodos: dobre a taxa e some o quadrado" ((1 + i)² = 1 + 2i + i²: 10% → 20 + 1 = 21%;
#   20% → 40 + 4 = 44%) · "na volta, teste o fator ao quadrado" (1,1² = 1,21; 1,2² = 1,44; 1,3² = 1,69) ·
#   conferência de plausibilidade (a equivalente do período LONGO fica um pouco ACIMA da proporcional; a do CURTO, abaixo).
# Nós fazemos (prompt): 3% a.m. → 1,03² = 1,0609 → 6,09% ao bimestre (atalho: 6 + 0,09).
# QUESTÃO 1 (texto idêntico na tela): 1,01¹² ≈ 1,1268 → 12,68% → D. Erradas do material: B (12%) proporcional;
#   C (12,12%) = 1,01 × 12; E (112,68%) fator sem tirar o 1; A (1,27%) vírgula deslocada.
# QUESTÃO 2 (texto idêntico): (1 + i)³ = 1,331 → 1,1 → 10% → C. Erradas do material: D (11,03%) = 33,1 ÷ 3 proporcional;
#   A (1,10%) confunde o fator 1,10 com a taxa; B (3,31%) vírgula deslocada de 33,1; E repete a trimestral.
# QUESTÃO 9 (texto idêntico): 1,2² = 1,44 → 20% ao semestre → E. Erradas do material: todas proporcionais
#   (44 ÷ 12 = 3,67; 44 ÷ 4 = 11; 44 ÷ 3 = 14,67; 44 ÷ 2 = 22); a D dá 1,22² ≈ 1,488, quase 49% no ano.
#   Conferido em Python: as quatro, capitalizadas, passam de 44% (1,0367¹² ≈ 1,541; 1,11⁴ ≈ 1,518; 1,1467³ ≈ 1,508).
# Exemplo do bloco b (nosso, conferido): R$ 100 a 2% a.m. por 12 meses → R$ 126,82; a 26,8% a.a. → R$ 126,80 (mesmo destino);
#   a 24% a.a. → R$ 124,00 (outro destino).
# Frases-chave (meio e fim, idênticas): 1. Taxa equivalente: eleve o fator, não multiplique a taxa.
#   2. Do período longo para o curto: raiz do fator, nunca divisão. 3. No fim, tire o 1 do fator.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Taxa equivalente do zero: 10% ao mês NÃO é 120% ao ano | Taxas e Inflação Ep. 1"
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
        "{a}Dez por cento ao mês [p=0.2] dá quanto ao ano? [p=0.5] {b}Se você disse *cento e vinte por cento,* [p=0.2] "
        "errou por quase *cem pontos:* [p=0.3] {c}dá cerca de *duzentos e quatorze por cento.* [p=0.5] {d}É assim que "
        "o *rotativo do cartão* [p=0.2] vira uma taxa anual de *três dígitos.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai converter qualquer taxa composta [p=0.2] de *mensal para anual* "
        "[p=0.2] {b}e de *anual para semestral,* [p=0.3] {c}sem multiplicar nem dividir pelo número de períodos."),
    dict(id="03", block="prereq", text=
        "{t}Antes, dois lembretes rápidos. [p=0.3] {a}Da série de Juros Simples: [p=0.2] dois por cento ao mês "
        "[p=0.2] viram *vinte e quatro por cento ao ano.* [p=0.4] {b}Da série de Juros Compostos: [p=0.2] *M igual a "
        "C vezes um mais i, elevado a t.* [p=0.4] {c}E duas potências: [p=0.2] um vírgula um ao quadrado, [p=0.2] *um "
        "vírgula vinte e um;* [p=0.2] ao cubo, [p=0.2] *um vírgula trezentos e trinta e um.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Imagine duas propagandas de banco. [p=0.3] {a}Uma diz: [p=0.2] *dois por cento ao mês.* [p=0.4] {b}A outra: "
        "[p=0.2] *vinte e seis vírgula oito por cento ao ano.* [p=0.4] {c}Qual rende mais? [p=0.5] {d}Surpresa: "
        "[p=0.2] *é a mesma coisa.* [p=0.4] {e}E a fatura do cartão faz o truque contrário: [p=0.2] anuncia uma taxa "
        "*de um dígito ao mês,* [p=0.2] que parece pequena."),
    dict(id="05", block="definicao", text=
        "{t}Primeiro, as palavras. [p=0.3] {a}*Taxa* é a porcentagem que o dinheiro cresce [p=0.2] {b}num *período:* "
        "[p=0.2] o tempo em que ela vale. [p=0.4] {c}*A.m.* [p=0.2] é ao mês; [p=0.2] *a.s.,* [p=0.2] ao semestre, "
        "seis meses; [p=0.2] *a.a.,* [p=0.2] ao ano. [p=0.4] {d}Hoje: [p=0.2] trocar o período de uma taxa."),

    # ================= BLOCO A: DUAS FORMAS =================
    dict(id="06", block="formas", text=
        "{t}Como se troca o período? [p=0.3] Existem *dois jeitos.* [p=0.4] {a}O primeiro é a *taxa proporcional:* "
        "[p=0.2] multiplica ou divide pelo número de períodos. [p=0.2] Dois ao mês, [p=0.2] vinte e quatro ao ano. "
        "[p=0.4] {b}Ela é a certa nos *juros simples:* [p=0.2] o regime em que os juros são calculados sempre sobre o "
        "valor do começo."),
    dict(id="07", block="formas", text=
        "{t}O segundo é a *taxa equivalente.* [p=0.4] {a}Ela é a certa nos *juros compostos:* [p=0.2] os juros de "
        "cada mês [p=0.2] *também rendem juros.* [p=0.4] {b}No gráfico, [p=0.2] a proporcional segue a *reta:* "
        "[p=0.2] soma dois por cento por mês, [p=0.2] até vinte e quatro. [p=0.4] {c}A equivalente segue a *curva:* "
        "[p=0.2] multiplica por um vírgula zero dois, [p=0.2] até *vinte e seis vírgula oito.* [p=0.4] {d}A faixa "
        "entre as duas [p=0.2] é o *juro sobre juro.*"),

    # ================= BLOCO B: DEFINIÇÃO =================
    dict(id="08", block="mesmo", text=
        "{t}Mas o que quer dizer *equivalente?* [p=0.4] {a}Mesmo *capital,* [p=0.2] mesmo *prazo,* [p=0.2] mesmo "
        "*montante* no fim. [p=0.3] Mesmo destino, [p=0.2] caminhos diferentes. [p=0.4] {b}Cem reais a dois por cento "
        "ao mês, [p=0.2] por doze meses: [p=0.2] cerca de *cento e vinte e seis e oitenta.* [p=0.3] {c}A vinte e seis "
        "vírgula oito ao ano: [p=0.2] *o mesmo valor.* [p=0.4] {d}A vinte e quatro ao ano: [p=0.2] só *cento e vinte "
        "e quatro.* [p=0.2] Outro destino: [p=0.2] não é equivalente."),

    # ================= BLOCO C: O FATOR E A FÓRMULA =================
    dict(id="09", block="fator", text=
        "{t}E como chegar aos vinte e seis vírgula oito? [p=0.4] {a}Com o *fator:* [p=0.2] *um mais a taxa,* em "
        "decimal. [p=0.4] {b}Dois por cento [p=0.2] vira *um vírgula zero dois.* [p=0.2] Quarenta e quatro por cento, "
        "[p=0.2] *um vírgula quarenta e quatro.* [p=0.4] {c}A regra de ouro: [p=0.2] *fator primeiro, taxa depois.* "
        "[p=0.3] A conta é com o fator; [p=0.2] no fim, [p=0.2] *tire o um.*"),
    dict(id="10", block="formula", text=
        "{t}A conta é esta. [p=0.3] {a}Se o período longo tem *n* períodos curtos, [p=0.2] o fator longo é o fator "
        "curto *elevado a n.* [p=0.4] {b}Dez por cento ao mês, [p=0.2] num *bimestre,* dois meses: [p=0.2] um vírgula "
        "um ao quadrado, [p=0.2] *um vírgula vinte e um.* [p=0.2] *Vinte e um por cento,* [p=0.2] não vinte. [p=0.4] "
        "{c}Num *trimestre,* três meses: [p=0.2] ao cubo, [p=0.2] *um vírgula trezentos e trinta e um.* [p=0.2] "
        "*Trinta e três vírgula um,* [p=0.2] não trinta."),
    dict(id="11", block="formula", text=
        "{t}Mais três que caem muito. [p=0.3] {a}Vinte por cento ao semestre, [p=0.2] ao quadrado: [p=0.2] *quarenta "
        "e quatro por cento ao ano.* [p=0.4] {b}Um por cento ao mês, [p=0.2] elevado a doze: [p=0.2] *doze vírgula "
        "sessenta e oito.* [p=0.4] {c}Dois por cento ao mês, [p=0.2] elevado a doze: [p=0.2] *vinte e seis vírgula "
        "oito.* [p=0.4] {d}Potência de doze, [p=0.2] o *ENEM dá* no enunciado."),
    dict(id="12", block="atalho", text=
        "{t}E quando são só *dois* períodos? [p=0.3] Tem atalho. [p=0.4] {a}*Dobre a taxa [p=0.2] e some o quadrado "
        "dela.* [p=0.4] {b}Dez por cento: [p=0.2] dobro, vinte; [p=0.2] quadrado, um. [p=0.2] *Vinte e um.* [p=0.4] "
        "{c}Vinte por cento: [p=0.2] dobro, quarenta; [p=0.2] quadrado, quatro. [p=0.2] *Quarenta e quatro.* [p=0.4] "
        "{d}O quadrado é exatamente o *juro sobre juro.*"),

    # ================= BLOCO D: O CAMINHO INVERSO =================
    dict(id="13", block="raiz", text=
        "{t}E o caminho contrário? [p=0.2] Do ano para o semestre? [p=0.4] {a}O contrário de elevar ao quadrado [p=0.2] "
        "é tirar a *raiz:* [p=0.2] achar o número que, multiplicado por ele mesmo, [p=0.2] dá o fator. [p=0.4] "
        "{b}Sessenta e nove por cento ao ano: [p=0.2] fator *um vírgula sessenta e nove.* [p=0.2] Que número vezes ele "
        "mesmo dá isso? [p=0.3] *Um vírgula três.* [p=0.4] {c}Tira o um: [p=0.2] *trinta por cento ao semestre.*"),
    dict(id="14", block="raiz", text=
        "{t}E se você dividisse por dois? [p=0.4] {a}Daria *trinta e quatro e meio* ao semestre. [p=0.4] {b}Mas um "
        "vírgula trezentos e quarenta e cinco ao quadrado [p=0.2] dá quase *um vírgula oitenta e um:* [p=0.2] oitenta "
        "e um por cento no ano, [p=0.2] *não sessenta e nove.* [p=0.4] {c}Atalho da volta: [p=0.2] *teste o fator ao "
        "quadrado.* [p=0.2] Um vírgula um, [p=0.2] um vírgula dois, [p=0.2] um vírgula três: [p=0.2] quadrados que "
        "você reconhece."),

    # ================= BLOCO E: O EFEITO CRESCE =================
    dict(id="15", block="efeito", text=
        "{t}E a diferença é sempre pequena? [p=0.4] {a}Com taxa pequena, [p=0.2] fica perto: [p=0.2] um por cento ao "
        "mês [p=0.2] dá doze proporcional [p=0.2] contra *doze vírgula sessenta e oito.* [p=0.4] {b}Com taxa alta, "
        "[p=0.2] *explode.* [p=0.3] Um vírgula um elevado a doze [p=0.2] dá cerca de *três vírgula quatorze.* [p=0.4] "
        "{c}Tira o um: [p=0.2] *duzentos e quatorze por cento ao ano,* [p=0.2] não cento e vinte. [p=0.4] {d}É o "
        "rotativo do cartão."),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Três por cento ao mês, [p=0.2] em juros compostos, [p=0.2] equivale a quanto ao "
        "*bimestre?* [p=0.4] {b}*Pause e tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Fator primeiro: [p=0.2] *um vírgula zero três,* [p=0.2] ao quadrado, [p=0.2] "
        "porque são dois meses. [p=0.4] {b}Dá *um vírgula zero seis zero nove.* [p=0.4] {c}Tira o um: [p=0.2] *seis "
        "vírgula zero nove por cento ao bimestre,* [p=0.2] não seis. [p=0.4] {d}Pelo atalho: [p=0.2] dobro, seis; "
        "[p=0.2] quadrado, zero vírgula zero nove. [p=0.2] Bateu."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] taxa equivalente: [p=0.2] eleve o fator, [p=0.2] não "
        "multiplique a taxa. [p=0.5] {b}Dois: [p=0.2] do período longo para o curto: [p=0.2] raiz do fator, [p=0.2] "
        "nunca divisão. [p=0.5] {c}Três: [p=0.2] no fim, [p=0.2] tire o um do fator."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *dois por cento ao mês é vinte e quatro ao "
        "ano,* [p=0.2] em juros compostos. [p=0.4] {b}Parece certo, [p=0.2] porque foi assim que você aprendeu nos juros "
        "simples. [p=0.4] {c}Mas, nos compostos, [p=0.2] eleve o fator: [p=0.2] *vinte e seis vírgula oito.*"),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] *dividir* a taxa anual pelo número de períodos. [p=0.2] Sessenta e nove ao ano, [p=0.2] "
        "trinta e quatro e meio ao semestre. [p=0.4] {b}Parece certo, [p=0.2] porque dividir é o caminho de volta da "
        "multiplicação. [p=0.4] {c}Mas a volta de uma *potência* é a *raiz:* [p=0.2] trinta por cento ao semestre."),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] *esquecer de tirar o um* do fator: [p=0.2] *cento e vinte e seis vírgula oito por "
        "cento.* [p=0.4] {b}Parece certo, [p=0.2] porque o número está ali, prontinho. [p=0.4] {c}Mas o um é o "
        "*dinheiro que você já tinha.* [p=0.2] Só o que passa dele é taxa: [p=0.2] vinte e seis vírgula oito."),

    # ================= QUESTÃO 1 (EU FAÇO) =================
    dict(id="22", block="q1", text=
        "{t}Agora, questões no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.2] Esta primeira, [p=0.2] eu "
        "resolvo com você. [p=0.4] {a}Uma aplicação rende *um por cento ao mês* [p=0.2] no regime de juros compostos. "
        "[p=0.2] Considere um vírgula zero um elevado a doze [p=0.2] aproximadamente igual a *um vírgula um dois seis "
        "oito.* [p=0.2] A taxa anual equivalente é, aproximadamente: [p=0.4] {qa}A: [p=0.2] um vírgula vinte e sete "
        "por cento. [p=0.3] {qb}B: [p=0.2] doze. [p=0.3] {qc}C: [p=0.2] doze vírgula doze. [p=0.3] {qd}D: [p=0.2] doze "
        "vírgula sessenta e oito. [p=0.3] {qe}E: [p=0.2] cento e doze vírgula sessenta e oito por cento."),
    dict(id="23", block="q1", text=
        "{t}Fator primeiro. [p=0.3] {a}Um por cento [p=0.2] vira *um vírgula zero um.* [p=0.2] Um ano tem doze meses: "
        "[p=0.2] *elevado a doze.* [p=0.4] {b}O enunciado já deu: [p=0.2] *um vírgula um dois seis oito.* [p=0.4] {c}Tira "
        "o um: [p=0.2] *doze vírgula sessenta e oito por cento.* [p=0.4] {d}Plausível? [p=0.2] Um pouco *acima* dos "
        "doze da proporcional, [p=0.2] como tem que ser. [p=0.3] {ok}*Letra D!*"),
    dict(id="24", block="q1", text=
        "{t}E as outras? [p=0.3] {xb}A B, [p=0.2] doze, [p=0.2] é a *proporcional:* [p=0.2] certa só nos juros simples. "
        "[p=0.4] {xe}A E [p=0.2] esqueceu de *tirar o um.* [p=0.4] {xc}A C [p=0.2] multiplicou o fator *por doze,* "
        "[p=0.2] em vez de elevar. [p=0.4] {xa}E a A [p=0.2] *deslocou a vírgula.*"),

    # ================= QUESTÃO 2 (NÓS FAZEMOS) =================
    dict(id="25", block="q2", text=
        "{t}A próxima, a gente faz junto. [p=0.3] {a}Um investimento rendeu *trinta e três vírgula um por cento* em um "
        "*trimestre,* [p=0.2] no regime de juros compostos, [p=0.2] com a mesma taxa em cada mês. [p=0.2] A taxa mensal "
        "foi de: [p=0.4] {qa}A: [p=0.2] um vírgula dez por cento. [p=0.3] {qb}B: [p=0.2] três vírgula trinta e um. "
        "[p=0.3] {qc}C: [p=0.2] dez. [p=0.3] {qd}D: [p=0.2] onze vírgula zero três. [p=0.3] {qe}E: [p=0.2] trinta e "
        "três vírgula dez por cento. [p=0.5] {p}Do longo para o curto: [p=0.2] *pause e tente.* [p=2.0]"),
    dict(id="26", block="q2", text=
        "{t}Fator do trimestre: [p=0.2] *um vírgula trezentos e trinta e um.* [p=0.4] {a}Trimestre são três meses: "
        "[p=0.2] o fator mensal, *ao cubo,* [p=0.2] dá um vírgula trezentos e trinta e um. [p=0.4] {b}Você conhece esse "
        "número: [p=0.2] um vírgula um vezes um vírgula um vezes um vírgula um. [p=0.4] {c}Fator mensal, [p=0.2] *um "
        "vírgula um.* [p=0.2] Tira o um: [p=0.2] *dez por cento ao mês.* [p=0.4] {d}Plausível? [p=0.2] Um pouco abaixo "
        "dos onze da divisão. [p=0.3] {ok}*Letra C!*"),
    dict(id="27", block="q2", text=
        "{t}E as erradas? [p=0.3] {xd}A D, [p=0.2] onze vírgula zero três, [p=0.2] *dividiu por três:* [p=0.2] é a "
        "proporcional. [p=0.4] {xa}A A [p=0.2] confundiu o *fator* um vírgula dez com a taxa. [p=0.4] {xb}A B [p=0.2] "
        "deslocou a vírgula do trinta e três vírgula um. [p=0.4] {xe}E a E [p=0.2] repetiu a taxa do trimestre [p=0.2] "
        "como se fosse do mês."),

    # ================= QUESTÃO 9 (VOCÊ FAZ) =================
    dict(id="28", block="q9", text=
        "{t}E esta é *sua.* [p=0.3] {a}Um fundo rende *quarenta e quatro por cento ao ano* [p=0.2] no regime de juros "
        "compostos. [p=0.2] Qual das taxas a seguir, [p=0.2] no mesmo regime, [p=0.2] é *equivalente* à desse fundo? "
        "[p=0.4] {qa}A: [p=0.2] três vírgula sessenta e sete por cento ao mês. [p=0.3] {qb}B: [p=0.2] onze por cento "
        "ao trimestre. [p=0.3] {qc}C: [p=0.2] quatorze vírgula sessenta e sete ao quadrimestre, [p=0.2] que são quatro "
        "meses. [p=0.3] {qd}D: [p=0.2] vinte e dois ao semestre. [p=0.3] {qe}E: [p=0.2] vinte por cento ao semestre. "
        "[p=0.5] {p}*Pause o vídeo e resolva.* [p=2.0]"),
    dict(id="29", block="q9", text=
        "{t}Conferindo. [p=0.3] {a}Um ano tem *dois semestres.* [p=0.2] Fator do ano: [p=0.2] *um vírgula quarenta e "
        "quatro.* [p=0.4] {b}Raiz: [p=0.2] que número vezes ele mesmo dá um vírgula quarenta e quatro? [p=0.3] *Um "
        "vírgula dois.* [p=0.4] {c}Tira o um: [p=0.2] *vinte por cento ao semestre.* [p=0.2] Atalho para conferir: "
        "[p=0.2] dobro, quarenta, [p=0.2] mais o quadrado, quatro. [p=0.2] Quarenta e quatro. [p=0.3] {ok}*Letra E!*"),
    dict(id="30", block="q9", text=
        "{t}E repare nas outras quatro. [p=0.3] {xa}Quarenta e quatro dividido por doze, [p=0.2] {xb}por quatro, "
        "[p=0.2] {xc}por três, [p=0.2] {xd}por dois. [p=0.4] {a}*Todas proporcionais,* [p=0.2] e todas rendem *mais* "
        "que quarenta e quatro no ano. [p=0.2] A D dá quase *quarenta e nove.* [p=0.4] {b}A questão premia [p=0.2] "
        "quem *desconfia da divisão.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="31", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] taxa equivalente: [p=0.2] eleve o fator, [p=0.2] "
        "não multiplique a taxa. [p=0.5] {b}Dois: [p=0.2] do período longo para o curto: [p=0.2] raiz do fator, [p=0.2] "
        "nunca divisão. [p=0.5] {c}Três: [p=0.2] no fim, [p=0.2] tire o um do fator."),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}Um contrato diz: [p=0.2] *vinte e quatro por cento ao ano, [p=0.2] capitalizados mensalmente.* [p=0.5] "
        "{b}Você paga vinte e quatro por cento ao ano? [p=0.4] {c}*Não.* [p=0.4] {d}Próximo episódio."),
    dict(id="33", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha caído na conta do vinte e quatro por cento? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
