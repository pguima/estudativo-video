# Roteiro — Taxas Equivalentes e Inflação, Episódio 3 de 5: inflação, inflação acumulada e poder de compra
# Base: Estudos/Enem/estudos/01-matematica/16-taxas-equivalentes-inflacao.html — seções 06 e 07 (SEM "Deflacionar", que
#   fica para o episódio 4) + Questão 5 (seção 12) + QUESTÃO NOVA do prompt (no lugar da Questão 4 do material, que repete
#   a Questão 3 da série de Porcentagem).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (do prompt):
#   A ESCADA ROLANTE DE PREÇOS: se ela fica mais lenta, os preços continuam subindo, só que mais devagar; preço descendo
#     (a escada invertida) é deflação.
#   PODER DE COMPRA É UMA DIVISÃO: o mesmo dinheiro dividido pelo fator dos preços.
#   FATOR PRIMEIRO, TAXA DEPOIS (a mesma dos episódios 1 e 2): inflações se acumulam multiplicando fatores.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos do material/prompt: cesta 500 → 540 (1,08 → 8%) · 5% e 4% → 1,092 (9,2%) · inflação de 8% para 4% ·
#   tabela 25% → 0,80 / 100% → 0,50 / 10% → ≈ 0,909 · nós fazemos: 60% → 1 ÷ 1,6 = 0,625 → perda de 37,5%.
#   O carrinho de 100 itens de R$ 1,00 (→ R$ 1,25, sobram 80) é a animação principal pedida no prompt, com 25%; ele
#   repete os números da Questão 5 ("você faz") por desenho do próprio prompt. Por isso a Questão 5 é apresentada como
#   "agora você faz sozinho o caminho"; o que ela traz de novo são os distratores (E = o que restou; D = 100 − 25).
# Exemplos NOSSOS: a nota de R$ 100,00 (cena 05) só "compra cada vez menos" (sem conta) · erro 1 com 10% e 10% (1,21 → 21%, não
#   20%) · erro 2 com a inflação de 100% do gancho (tira
#   metade), em vez dos 25%, para não repetir pela terceira vez a conta da Questão 5 antes dela.
# Atalhos (NOSSOS, verde): "fator − 1 = taxa" (bloco a) · "acumulada de duas: a + b + a·b/100" (bloco b: 5 + 4 + 0,2 =
#   9,2; na questão nova 25 + 20 + 5 = 50) · "perda = π ÷ (1 + π)": 25/125 = 20%, 100/200 = 50%, 60/160 = 37,5%
#   (bloco d e nós fazemos). Todos conferidos em Python (trabalho/conferir_contas.py).
# QUESTÃO NOVA (eu faço): 1,25 · 1,20 = 1,50 → 50% (D); R$ 100 → 125 → 150. Erradas (do prompt): A 25 − 20 = 5 (diferença);
#   B (25 + 20)/2 = 22,5 (média); C 25 + 20 = 45 (soma); E lê o fator 1,50 como 150%. Plausibilidade (NOSSA): a acumulada de
#   duas altas fica ACIMA da soma (45), porque a segunda alta incide sobre preço que já subiu.
# QUESTÃO 5 (você faz): 1 ÷ 1,25 = 0,80 → perda de 20% (B). Erradas (material): C iguala a perda à inflação; E é o que
#   restou (80%), não o que se perdeu; D é 100 − 25, que mistura as duas coisas; A é a metade de 25, sem fundamento.
#   Conferência: 100 unidades de R$ 1,00 → R$ 1,25 cada → 80 unidades. Plausibilidade: a perda (20%) fica ABAIXO da
#   inflação (25%).
# Frases-chave (meio e fim, idênticas): 1. Inflação se acumula multiplicando fatores. 2. Poder de compra: divida pelo
#   fator da inflação. 3. Inflação caindo não é preço caindo.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Inflação de 100% e o dinheiro vira pó? Inflação acumulada e poder de compra · Matemática ENEM, Taxas e Inflação episódio 3"

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
    "IPCA": "í-pê-cê-á",
    "IBGE": "í-bê-gê-é",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Se os preços dobram, [p=0.2] *inflação de cem por cento,* [p=0.3] {b}o seu dinheiro *vira pó?* [p=0.5] "
        "{c}Não: [p=0.2] ele passa a comprar *metade.* [p=0.4] {d}A perda é de *cinquenta por cento,* [p=0.2] não de cem "
        "por cento."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai calcular *inflação acumulada* [p=0.3] {b}e a *perda de poder de "
        "compra* [p=0.2] sem confundir as duas."),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Variação percentual: [p=0.2] *novo dividido pelo antigo,* [p=0.2] menos "
        "um. [p=0.4] {b}E da série de Porcentagem: [p=0.2] para *voltar ao valor original,* [p=0.2] *divida pelo "
        "fator.* [p=0.2] Subir vinte e cinco por cento e descer vinte [p=0.2] volta ao ponto de partida."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{a}Pense na sua *cesta de compras* do supermercado. [p=0.4] {b}No começo do ano, [p=0.2] ela custava "
        "*quinhentos reais.* [p=0.3] {c}No fim do ano, [p=0.2] a *mesma cesta* [p=0.2] custava *quinhentos e quarenta.* "
        "[p=0.4] {d}Você não comprou nada a mais. [p=0.2] Só ficou *mais caro.*"),
    dict(id="05", block="concreto", text=
        "{a}Agora pense numa *nota de cem reais* guardada na gaveta. [p=0.4] {b}Ela continua sendo cem reais. [p=0.3] "
        "{c}Mas, ano após ano, [p=0.2] ela compra *cada vez menos coisas.* [p=0.4] {d}É isso que a gente vai medir hoje."),

    # ================= BLOCO A: INFLAÇÃO E ÍNDICE =================
    dict(id="06", block="indice", text=
        "{t}Mas como se mede isso? [p=0.4] {a}*Inflação* é o aumento geral dos preços [p=0.2] num período. [p=0.4] "
        "{b}Ela é medida por um *índice de preços:* [p=0.2] uma conta que acompanha o custo de uma *cesta fixa,* "
        "[p=0.2] sempre os mesmos produtos e serviços. [p=0.4] {c}No Brasil, [p=0.2] o índice oficial é o *IPCA,* "
        "[p=0.2] calculado pelo *IBGE,* [p=0.2] o instituto oficial de estatística do país."),
    dict(id="07", block="indice", text=
        "{t}E a nossa cesta? [p=0.3] {a}Quinhentos e quarenta dividido por quinhentos: [p=0.2] *um vírgula zero oito.* "
        "[p=0.4] {b}Esse é o *fator.* [p=0.2] Tire o um: [p=0.2] *inflação de oito por cento.* [p=0.4] {c}Atalho: "
        "[p=0.2] *fator primeiro, taxa depois.* [p=0.2] A taxa é o fator *menos um.*"),

    # ================= BLOCO B: INFLAÇÃO ACUMULADA =================
    dict(id="08", block="acumulada", text=
        "{t}E se forem *dois anos* de inflação? [p=0.4] {a}*Inflação acumulada* é a alta total dos preços [p=0.2] "
        "somando vários períodos em sequência. [p=0.4] {b}Cinco por cento num ano, [p=0.2] quatro no outro. [p=0.2] "
        "Nove por cento? [p=0.4] {c}Multiplique os fatores: [p=0.2] um vírgula zero cinco [p=0.2] vezes um vírgula zero "
        "quatro. [p=0.2] *Um vírgula zero nove dois.* [p=0.4] {d}*Nove vírgula dois por cento,* [p=0.2] não nove."),
    dict(id="09", block="acumulada", text=
        "{t}De onde vem esse *zero vírgula dois* a mais? [p=0.4] {a}No segundo ano, [p=0.2] os quatro por cento "
        "incidem sobre um preço [p=0.2] *que já tinha subido.* [p=0.4] {b}Atalho para duas taxas: [p=0.2] *some as "
        "duas* [p=0.2] e acrescente *o produto dividido por cem.* [p=0.2] Cinco mais quatro, [p=0.2] mais vinte "
        "dividido por cem: [p=0.2] *nove vírgula dois.*"),

    # ================= BLOCO C: INFLAÇÃO CAINDO =================
    dict(id="10", block="escada", text=
        "{t}A inflação caiu de oito para quatro por cento. [p=0.2] Os preços *caíram?* [p=0.5] {a}Pense numa *escada "
        "rolante de preços.* [p=0.4] {b}Com oito por cento, [p=0.2] ela sobe rápido. [p=0.3] {c}Com quatro, [p=0.2] "
        "ela fica *mais lenta.* [p=0.4] {d}Mas continua *subindo.* [p=0.2] Os preços sobem, [p=0.2] só que mais "
        "devagar."),
    dict(id="11", block="escada", text=
        "{t}E quando o preço desce de verdade? [p=0.4] {a}Aí a escada *inverte o sentido.* [p=0.2] Isso é *deflação:* "
        "[p=0.2] uma inflação negativa, [p=0.2] com os preços caindo. [p=0.4] {b}Cuidado nos gráficos da prova. [p=0.2] "
        "*Um gráfico de taxas descendo* [p=0.2] não é um gráfico de *preços descendo.*"),

    # ================= BLOCO D: PODER DE COMPRA =================
    dict(id="12", block="poder", text=
        "{t}E o seu dinheiro, [p=0.2] quanto ele perde? [p=0.4] {a}*Poder de compra* é quanto o seu dinheiro consegue "
        "comprar. [p=0.4] {b}Um carrinho com *cem itens de um real.* [p=0.2] Cem reais enchem o carrinho. [p=0.4] "
        "{c}Vem uma inflação de vinte e cinco por cento: [p=0.2] cada item passa a custar *um real e vinte e cinco.* "
        "[p=0.4] {d}Com os mesmos cem reais, [p=0.2] *saem vinte itens.* [p=0.2] Sobram *oitenta.* [p=0.4] {e}A perda "
        "é de *vinte por cento,* [p=0.2] não de vinte e cinco."),
    dict(id="13", block="poder", text=
        "{t}Qual é a conta? [p=0.4] {a}Poder de compra é uma *divisão:* [p=0.2] o mesmo dinheiro [p=0.2] dividido "
        "pelo *fator dos preços.* [p=0.4] {b}Um dividido por um vírgula vinte e cinco: [p=0.2] *zero vírgula oito.* "
        "[p=0.2] *Restou* oitenta por cento. [p=0.2] *Perdeu* vinte. [p=0.4] {c}Inflação de cem por cento: [p=0.2] um "
        "dividido por dois, [p=0.2] *metade.* [p=0.2] Perda de cinquenta. [p=0.4] {d}Inflação de dez: [p=0.2] um "
        "dividido por um vírgula um, [p=0.2] cerca de *zero vírgula nove zero nove.* [p=0.2] Perda de *nove vírgula "
        "um* por cento."),
    dict(id="14", block="poder", text=
        "{t}Tem um caminho mais curto? [p=0.4] {a}Atalho: [p=0.2] a perda é a *inflação dividida pelo fator.* [p=0.4] "
        "{b}Vinte e cinco sobre cento e vinte e cinco: [p=0.2] *vinte por cento.* [p=0.2] Cem sobre duzentos: [p=0.2] "
        "*cinquenta.* [p=0.4] {c}E sempre diga em voz alta: [p=0.2] a questão quer o que se *perdeu,* [p=0.2] ou o que "
        "*restou?*"),

    # ================= BLOCO E: POR QUE A PERDA É MENOR =================
    dict(id="15", block="menor", text=
        "{t}Por que a perda é *menor* que a inflação? [p=0.4] {a}É a mesma conta de *voltar ao valor original.* "
        "[p=0.4] {b}Subir vinte e cinco por cento [p=0.2] e depois descer vinte [p=0.2] volta ao começo. [p=0.4] "
        "{c}A inflação é medida sobre o preço *antigo,* [p=0.2] que é menor. [p=0.2] A perda é medida sobre o preço "
        "*novo,* [p=0.2] que é maior. [p=0.4] {d}Base maior, [p=0.2] porcentagem menor."),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Num período de *inflação de sessenta por cento,* [p=0.2] um salário ficou "
        "*congelado.* [p=0.4] {b}Quanto ele perdeu de poder de compra? [p=0.3] {c}*Pause e tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}O fator é *um vírgula seis.* [p=0.2] Um dividido por um vírgula seis: [p=0.2] "
        "*zero vírgula seis dois cinco.* [p=0.4] {b}Restou sessenta e dois e meio por cento. [p=0.2] *Perdeu trinta e "
        "sete e meio.* [p=0.4] {c}Pelo atalho: [p=0.2] sessenta sobre cento e sessenta, [p=0.2] *trinta e sete e meio.* "
        "[p=0.2] Abaixo dos sessenta da inflação: [p=0.2] *faz sentido.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] inflação se acumula multiplicando fatores. [p=0.5] "
        "{b}Dois: [p=0.2] poder de compra: [p=0.2] divida pelo fator da inflação. [p=0.5] {c}Três: [p=0.2] inflação "
        "caindo não é preço caindo."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *somar inflações.* [p=0.2] Dez por cento e dez por "
        "cento, [p=0.2] vinte por cento. [p=0.4] {b}Parece certo, [p=0.2] porque as duas são porcentagens, [p=0.2] uma "
        "depois da outra. [p=0.4] {c}Mas a segunda incide sobre preço que *já subiu.* [p=0.2] Um vírgula um ao "
        "quadrado: [p=0.2] *vinte e um por cento.*"),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] *perda igual à inflação.* [p=0.2] Inflação de cem por cento, [p=0.2] perda de cem por "
        "cento. [p=0.4] {b}Parece certo: [p=0.2] o preço subiu cem, [p=0.2] o dinheiro perdeu cem. [p=0.4] {c}Mas o "
        "dinheiro ainda compra *metade.* [p=0.2] *Divida pelo fator:* [p=0.2] a perda é de cinquenta."),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] inflação de oito caiu para quatro, [p=0.2] então *os preços caíram.* [p=0.4] {b}Parece "
        "certo: [p=0.2] o número desceu. [p=0.4] {c}Mas desceu a *velocidade* da escada. [p=0.2] Os preços *continuam "
        "subindo.* [p=0.2] Preço caindo só com *deflação.*"),

    # ================= QUESTÃO NOVA (EU FAÇO) =================
    dict(id="22", block="qnova", text=
        "{t}Agora, uma questão no estilo do ENEM. [p=0.4] {a}Em um país, [p=0.2] a inflação foi de *vinte e cinco por "
        "cento* em um ano [p=0.2] e de *vinte por cento* no ano seguinte. [p=0.2] A inflação acumulada nesses dois anos "
        "foi de: [p=0.4] {qa}A: [p=0.2] cinco por cento. [p=0.3] {qb}B: [p=0.2] vinte e dois vírgula cinco. [p=0.3] "
        "{qc}C: [p=0.2] quarenta e cinco. [p=0.3] {qd}D: [p=0.2] cinquenta. [p=0.3] {qe}E: [p=0.2] cento e cinquenta "
        "por cento. [p=0.4] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="23", block="qnova", text=
        "{t}Eu resolvo com você. [p=0.3] {a}A pergunta é *acumulada:* [p=0.2] multiplique os fatores. [p=0.2] Um "
        "vírgula vinte e cinco [p=0.2] vezes um vírgula vinte. [p=0.2] *Um vírgula cinco.* [p=0.2] *Cinquenta por "
        "cento.* [p=0.4] {b}Confira com um produto de cem reais: [p=0.2] vai a *cento e vinte e cinco,* [p=0.2] e depois "
        "a *cento e cinquenta.* [p=0.4] {c}Faz sentido: [p=0.2] ficou *acima da soma,* [p=0.2] porque os vinte por "
        "cento incidem sobre um preço que já subiu. [p=0.3] {ok}*Letra D!*"),
    dict(id="24", block="qnova", text=
        "{t}E as outras? [p=0.3] {xa}A A é a *diferença* entre as taxas. [p=0.4] {xb}A B é a *média* das taxas. [p=0.4] "
        "{xc}A C *soma* as taxas, [p=0.2] o erro clássico. [p=0.4] {xe}E a E escreve o *fator* um vírgula cinco [p=0.2] "
        "como se fosse cento e cinquenta por cento."),

    # ================= QUESTÃO 5 (VOCÊ FAZ) =================
    dict(id="25", block="q5", text=
        "{t}Agora é com você, [p=0.2] sozinho, [p=0.2] o caminho do carrinho. [p=0.4] {a}Durante um período, [p=0.2] os "
        "preços de uma cidade subiram, em média, [p=0.2] *vinte e cinco por cento,* [p=0.2] enquanto o salário de um "
        "trabalhador *permaneceu o mesmo.* [p=0.2] Em relação ao início do período, [p=0.2] o poder de compra desse "
        "salário diminuiu: [p=0.4] {qa}A: [p=0.2] doze vírgula cinco por cento. [p=0.3] {qb}B: [p=0.2] vinte. [p=0.3] "
        "{qc}C: [p=0.2] vinte e cinco. [p=0.3] {qd}D: [p=0.2] setenta e cinco. [p=0.3] {qe}E: [p=0.2] oitenta por "
        "cento. [p=0.4] {p}*Pause o vídeo e resolva sozinho.* [p=2.5]"),
    dict(id="26", block="q5", text=
        "{t}Vamos conferir. [p=0.3] {a}Divida pelo fator: [p=0.2] um dividido por um vírgula vinte e cinco, [p=0.2] "
        "*zero vírgula oito.* [p=0.2] O salário compra oitenta por cento do que comprava. [p=0.4] {b}A pergunta é o "
        "que *diminuiu:* [p=0.2] *vinte por cento.* [p=0.4] {c}Com cem reais, [p=0.2] eram cem unidades de um real. "
        "[p=0.2] Agora, [p=0.2] *oitenta.* [p=0.2] E a perda ficou abaixo da inflação. [p=0.3] {ok}*Letra B!*"),
    dict(id="27", block="q5", text=
        "{t}E as pegadinhas? [p=0.3] {xc}A C iguala a *perda à inflação.* [p=0.4] {xe}A E é o que *restou,* [p=0.2] não "
        "o que se perdeu. [p=0.4] {xd}A D faz cem menos vinte e cinco, [p=0.2] e *mistura as duas coisas.* [p=0.4] "
        "{xa}E a A é a metade de vinte e cinco, [p=0.2] *sem nenhum fundamento.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] inflação se acumula multiplicando fatores. "
        "[p=0.5] {b}Dois: [p=0.2] poder de compra: [p=0.2] divida pelo fator da inflação. [p=0.5] {c}Três: [p=0.2] "
        "inflação caindo não é preço caindo."),

    # ================= PONTE E CTA =================
    dict(id="29", block="ponte", text=
        "{a}Seu dinheiro rendeu *vinte e seis por cento* [p=0.2] num ano de inflação de *vinte por cento.* [p=0.4] "
        "{b}Você ficou *seis por cento mais rico?* [p=0.5] {c}Próximo episódio: [p=0.2] *taxa real.*"),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] com inflação de cinquenta por cento, [p=0.2] quanto um salário "
        "congelado perde de poder de compra? [p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um "
        "link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para "
        "revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no "
        "Estudativo. [p=1.5]"),
]
