# Roteiro — Taxas Equivalentes e Inflação, Episódio 2 de 5: taxa nominal × taxa efetiva e taxas acumuladas
# Base: Estudos/Enem/estudos/01-matematica/16-taxas-equivalentes-inflacao.html — seções 04 e 05 + Questão 3 (seção 12)
#   + QUESTÃO NOVA do prompt (financeiras X e Y, 36% ao ano) no "você faz".
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (do prompt):
#   A NOMINAL É O PREÇO DA VITRINE; A EFETIVA É O QUE PASSA NO CAIXA.
#   A NOMINAL SÓ SERVE PARA UMA COISA: DIVIDIR PELO NÚMERO DE CAPITALIZAÇÕES. DEPOIS, CAPITALIZE.
#   FATOR PRIMEIRO, TAXA DEPOIS (a mesma do episódio 1), agora com fatores diferentes, inclusive menores que 1.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Cuidado do roteiros.md seguido: os 2% ao mês são a taxa DO PERÍODO DE CAPITALIZAÇÃO (efetiva ao mês), nunca "a taxa
#   mensal equivalente a 24% ao ano"; a efetiva anual é 1,02^12 − 1 ≈ 26,8%.
# Contas (conferidas em Python): 1,02^12 = 1,2682 · 1,01^12 = 1,1268 · 1,12² = 1,2544 · 1,1 · 1,2 · 0,9 = 1,188 ·
#   100 → 110 → 132 → 118,80 · 1,1² = 1,21 e 1,105² = 1,221 · nós fazemos 1,2 · 0,9 · 1,05 = 1,134 (soma 15%) ·
#   1,09² = 1,1881 · 1,015^12 = 1,1956 · 1,18² = 1,3924 · 1,03^12 = 1,4258.
# Atalhos (NOSSOS, verde): "divida, eleve, tire 1" (bloco b) · capitalização SEMESTRAL: efetiva = nominal + (taxa do
#   semestre)², porque (1 + x)² = 1 + 2x + x² e 2x é a própria nominal (24% + 1,44% = 25,44%; 18% + 0,81% = 18,81%;
#   36% + 3,24% = 39,24%) · taxa média: teste as alternativas elevando (1,1² = 1,21).
# Exemplo NOSSO no bloco d (em reais): 100 → 110 → 132 → 118,80 (a queda de 10% tira R$ 13,20, não R$ 10,00).
# QUESTÃO 3 (eu faço): 18% ÷ 2 = 9% ao semestre; 1,09² = 1,1881 → 18,81% (C). Erradas (material): A taxa do semestre
#   (etapa intermediária) · B nominal tomada pela efetiva · D capitalização mensal (1,015^12 ≈ 1,1956) · E fator sem tirar 1.
# QUESTÃO NOVA (você faz, do prompt): X 18% ao semestre → 1,3924 → 39,24%; Y 3% ao mês → 1,03^12 ≈ 1,426 → ≈ 42,6% (D).
#   Erradas (prompt): A nominal pela efetiva · B efetiva de X certa, mas é a menor · C financeira certa sem capitalizar ·
#   E fator sem tirar 1.
# Frases-chave (meio e fim, idênticas): 1. Taxa nominal: divida pelas capitalizações e capitalize. 2. Taxas em sequência:
#   multiplique os fatores, inclusive os menores que 1. 3. Taxa média por período é a equivalente, não a média das
#   porcentagens.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "24% ao ano que custa 26,8%: taxa nominal × efetiva · Matemática ENEM, Taxas e Inflação episódio 2"

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
        "{a}Dois contratos anunciam exatamente *vinte e quatro por cento ao ano.* [p=0.4] {b}Um custa *vinte e cinco "
        "vírgula quarenta e quatro;* [p=0.3] {c}o outro, *vinte e seis vírgula oito.* [p=0.4] {d}Mesma propaganda, "
        "[p=0.2] *preços diferentes.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai transformar qualquer *taxa nominal em efetiva* [p=0.3] {b}e acumular "
        "taxas de meses diferentes *sem somar porcentagens.*"),
    dict(id="03", block="prereq", text=
        "{t}Dois lembretes rápidos. [p=0.3] {a}Do episódio um: [p=0.2] para trocar o período de uma taxa, [p=0.2] "
        "*eleve o fator.* [p=0.2] Fator primeiro, [p=0.2] taxa depois. [p=0.4] {b}Da série de Porcentagem: [p=0.2] "
        "variações em sequência [p=0.2] *multiplicam os fatores.* [p=0.2] E uma queda de dez por cento [p=0.2] vira o "
        "fator *zero vírgula nove.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{a}Leia a letra miúda de um contrato: [p=0.2] *vinte e quatro por cento ao ano, [p=0.2] capitalizados "
        "mensalmente.* [p=0.4] {b}*Capitalizar* é somar os juros ao saldo, [p=0.2] e a partir daí eles também rendem "
        "juros. [p=0.4] {c}O *período de capitalização* [p=0.2] é de quanto em quanto tempo isso acontece. [p=0.2] Aqui, *todo mês.*"),
    dict(id="05", block="concreto", text=
        "{a}Agora, o extrato de um fundo. [p=0.4] {b}Subiu dez por cento, [p=0.2] subiu vinte, "
        "[p=0.2] *caiu dez.* [p=0.4] {c}Quanto rendeu no total? [p=0.3] Guarde essa pergunta."),

    # ================= BLOCO A: TAXA NOMINAL =================
    dict(id="06", block="nominal", text=
        "{t}Então, quanto custa esse contrato? [p=0.4] {a}Os vinte e quatro por cento são a *taxa nominal:* [p=0.2] "
        "anunciada num período, [p=0.2] o ano, [p=0.2] e capitalizada em outro, [p=0.2] o mês. [p=0.4] {b}A *taxa "
        "efetiva* é a que você *realmente paga* no período. [p=0.4] {c}Pense assim: [p=0.2] a nominal é o *preço da "
        "vitrine;* [p=0.2] a efetiva é o que *passa no caixa.*"),
    dict(id="07", block="nominal", text=
        "{t}E o que fazer com a nominal? [p=0.4] {a}Ela só serve para uma coisa: [p=0.2] *dividir pelo número de "
        "capitalizações.* [p=0.4] {b}Vinte e quatro dividido por doze: [p=0.2] *dois por cento ao mês.* [p=0.4] "
        "{c}Esses dois por cento são *efetivos:* [p=0.2] é o que o banco cobra *a cada mês.* "
        "[p=0.4] {d}E essa é a *única* divisão permitida."),

    # ================= BLOCO B: CAPITALIZE =================
    dict(id="08", block="capitaliza", text=
        "{t}Depois de dividir, [p=0.2] *capitalize.* [p=0.4] {a}Doze meses, [p=0.2] doze fatores de *um vírgula zero "
        "dois,* [p=0.2] um sobre o outro. [p=0.4] {b}Um vírgula zero dois elevado a doze: [p=0.2] cerca de *um vírgula "
        "duzentos e sessenta e oito.* [p=0.4] {c}Tire o um: [p=0.2] *vinte e seis vírgula oito por cento ao ano.* "
        "[p=0.3] Esse é o preço do caixa."),
    dict(id="09", block="capitaliza", text=
        "{a}Atalho de prova: [p=0.2] nominal para efetiva em três passos. [p=0.3] *Divida, [p=0.2] eleve, [p=0.2] tire "
        "um.* [p=0.4] {b}E confira: [p=0.2] a efetiva fica *um pouco acima* da nominal."),

    # ================= BLOCO C: A TABELA =================
    dict(id="10", block="tabela", text=
        "{t}E como dois contratos de vinte e quatro por cento custam diferente? [p=0.4] {a}Doze por cento ao ano, "
        "[p=0.2] capitalizados por mês: [p=0.2] um por cento ao mês, [p=0.2] *cerca de doze vírgula sessenta e oito.* "
        "[p=0.4] {b}Vinte e quatro, [p=0.2] por *semestre:* [p=0.2] doze por cento ao semestre. [p=0.2] Um vírgula doze "
        "ao quadrado, [p=0.2] *vinte e cinco vírgula quarenta e quatro.* [p=0.4] {c}Vinte e quatro, [p=0.2] por *mês:* "
        "[p=0.2] *vinte e seis vírgula oito.* [p=0.2] O gancho, resolvido."),
    dict(id="11", block="tabela", text=
        "{a}A regra: [p=0.2] quanto *mais frequente* a capitalização, [p=0.2] *maior* a efetiva. [p=0.4] {b}Para "
        "comparar propostas, [p=0.2] converta todas para *efetivas no mesmo período.* [p=0.2] A nominal sozinha não "
        "compara nada. [p=0.4] {c}E um atalho para o semestre: [p=0.2] a efetiva é a nominal [p=0.2] *mais o quadrado* "
        "da taxa do semestre. [p=0.2] Vinte e quatro, [p=0.2] mais um vírgula quarenta e quatro."),

    # ================= BLOCO D: TAXAS ACUMULADAS =================
    dict(id="12", block="acumulada", text=
        "{t}E o fundo que subiu e caiu? [p=0.4] {a}Escreva o fator ao lado de cada mês. [p=0.2] Mais dez: [p=0.2] *um "
        "vírgula um.* [p=0.2] Mais vinte: [p=0.2] *um vírgula dois.* [p=0.2] Menos dez: [p=0.2] *zero vírgula nove.* "
        "[p=0.4] {b}Multiplique: [p=0.2] *um vírgula cento e oitenta e oito.* [p=0.4] {c}*Taxa acumulada,* [p=0.2] o "
        "rendimento do período inteiro: [p=0.2] *dezoito vírgula oito por cento.*"),
    dict(id="13", block="acumulada", text=
        "{t}Mas a soma não daria vinte? [p=0.4] {a}Veja em reais. [p=0.2] Cem, [p=0.2] cento e dez, [p=0.2] cento e "
        "trinta e dois. [p=0.4] {b}A queda de dez por cento [p=0.2] incide sobre um valor *já maior.* [p=0.2] Tira "
        "*treze e vinte,* [p=0.2] e não dez. [p=0.4] {c}Sobra *cento e dezoito e oitenta.*"),

    # ================= BLOCO E: TAXA MÉDIA =================
    dict(id="14", block="media", text=
        "{t}E a taxa *média* por mês? [p=0.4] {a}Um investimento rendeu *vinte e um por cento* em dois meses. "
        "[p=0.2] Dá dez e meio por mês? [p=0.4] {b}A *taxa média por período* [p=0.2] é a taxa constante que daria o "
        "mesmo acumulado. [p=0.2] A *equivalente.* [p=0.4] {c}Um vírgula um ao quadrado: [p=0.2] *um "
        "vírgula vinte e um.* [p=0.2] *Dez por cento ao mês.*"),
    dict(id="15", block="media", text=
        "{a}E os dez e meio? [p=0.2] Um vírgula cento e cinco ao quadrado [p=0.2] dá vinte e dois vírgula um. [p=0.2] "
        "*Passa do acumulado.* [p=0.4] {b}Atalho de prova: [p=0.2] para achar a taxa média, [p=0.2] *teste as "
        "alternativas elevando.* [p=0.2] A que volta ao acumulado é a certa."),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Um fundo rendeu *mais vinte por cento,* [p=0.2] depois *menos dez,* [p=0.2] depois "
        "*mais cinco.* [p=0.4] {b}Qual foi o rendimento acumulado? [p=0.3] {c}*Pause e tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Os fatores: [p=0.2] um vírgula dois, [p=0.2] zero vírgula nove, [p=0.2] um vírgula "
        "zero cinco. [p=0.4] {b}Um vírgula dois vezes zero vírgula nove: [p=0.2] um vírgula zero oito. [p=0.2] Vezes um "
        "vírgula zero cinco: [p=0.2] *um vírgula cento e trinta e quatro.* [p=0.4] {c}*Treze vírgula quatro por cento.* "
        "[p=0.2] A soma daria quinze."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] taxa nominal: divida pelas capitalizações e capitalize. "
        "[p=0.5] {b}Dois: [p=0.2] taxas em sequência: multiplique os fatores, inclusive os menores que um. [p=0.5] "
        "{c}Três: [p=0.2] taxa média por período é a equivalente, não a média das porcentagens."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] tomar a *nominal pela efetiva.* [p=0.2] Doze por cento "
        "ao ano, capitalizados por mês, [p=0.2] custam doze. [p=0.4] {b}Parece certo, [p=0.2] porque é o número escrito "
        "no contrato. [p=0.4] {c}Mas é o preço da vitrine. [p=0.2] No caixa: [p=0.2] *cerca de doze vírgula sessenta "
        "e oito.*"),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] *somar taxas* de períodos seguidos. [p=0.2] Dez e vinte por cento [p=0.2] viram trinta. "
        "[p=0.4] {b}Parece certo: [p=0.2] por cento com por cento. [p=0.4] {c}Mas a segunda taxa incide sobre um valor "
        "maior. [p=0.2] Um vírgula um vezes um vírgula dois: [p=0.2] *trinta e dois por cento.*"),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] *esquecer de tirar o um.* [p=0.2] O fator um vírgula duzentos e sessenta e oito [p=0.2] "
        "vira cento e vinte e seis vírgula oito por cento. [p=0.4] {b}Parece certo: [p=0.2] foi o que a conta deu. "
        "[p=0.4] {c}Mas o um é o *seu próprio dinheiro.* [p=0.2] A taxa é o que *passa de um:* [p=0.2] *vinte e seis "
        "vírgula oito.*"),

    # ================= QUESTÃO 3 (EU FAÇO) =================
    dict(id="22", block="q3", text=
        "{t}Agora, uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}Um contrato de "
        "empréstimo informa uma taxa de *dezoito por cento ao ano,* [p=0.2] com *capitalização semestral.* [p=0.2] A "
        "taxa efetiva anual desse contrato é de: [p=0.4] {qa}A: [p=0.2] nove por cento. [p=0.3] {qb}B: [p=0.2] dezoito. "
        "[p=0.3] {qc}C: [p=0.2] dezoito vírgula oitenta e um. [p=0.3] {qd}D: [p=0.2] dezenove vírgula cinquenta e seis. "
        "[p=0.3] {qe}E: [p=0.2] cento e dezoito vírgula oitenta e um. [p=0.4] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="23", block="q3", text=
        "{t}Eu resolvo com você. [p=0.3] {a}Viu a palavra *capitalização?* [p=0.2] Então dezoito é a nominal. "
        "[p=0.4] {b}Divida pelas duas capitalizações: [p=0.2] *nove por cento ao semestre.* [p=0.4] {c}Capitalize: "
        "[p=0.2] um vírgula zero nove ao quadrado, [p=0.2] *um vírgula mil oitocentos e oitenta e um.* [p=0.2] Tire o "
        "um: [p=0.2] *dezoito vírgula oitenta e um.* [p=0.4] {d}Pelo atalho do semestre: "
        "[p=0.2] dezoito, mais nove ao quadrado, zero vírgula oitenta e um. [p=0.3] {ok}*Letra C!*"),
    dict(id="24", block="q3", text=
        "{t}E as outras? [p=0.3] {xa}A A é a taxa do semestre: [p=0.2] *só uma etapa.* [p=0.4] {xb}A B toma a "
        "*nominal pela efetiva.* [p=0.4] {xd}A D capitaliza *por mês,* [p=0.2] um e meio por cento doze vezes. [p=0.2] "
        "Não é o contrato. [p=0.4] {xe}E a E é o fator [p=0.2] *sem tirar o um.*"),

    # ================= QUESTÃO NOVA (VOCÊ FAZ) =================
    dict(id="25", block="qnova", text=
        "{t}Agora é com você. [p=0.4] {a}Duas financeiras anunciam empréstimos com taxa de *trinta e seis por cento ao "
        "ano.* [p=0.2] A financeira X capitaliza os juros *semestralmente;* [p=0.2] a Y, *mensalmente.* [p=0.2] "
        "Considere um vírgula zero três elevado a doze [p=0.2] aproximadamente um vírgula quatrocentos e vinte e seis. "
        "[p=0.2] Qual delas tem o maior custo efetivo anual, [p=0.2] e qual é esse custo? [p=0.4] {qa}A: [p=0.2] as "
        "duas, [p=0.2] pois ambas cobram trinta e seis. [p=0.3] {qb}B: [p=0.2] a X, [p=0.2] com cerca de trinta e nove "
        "vírgula dois. [p=0.3] {qc}C: [p=0.2] a Y, [p=0.2] com trinta e seis. [p=0.3] {qd}D: [p=0.2] a Y, [p=0.2] com "
        "cerca de quarenta e dois vírgula seis. [p=0.3] {qe}E: [p=0.2] a Y, [p=0.2] com cerca de cento e quarenta e "
        "dois vírgula seis. [p=0.4] {p}*Pause o vídeo e resolva sozinho.* [p=2.5]"),
    dict(id="26", block="qnova", text=
        "{t}Vamos conferir. [p=0.3] {a}Na X: [p=0.2] dezoito por cento ao semestre. [p=0.2] Um vírgula dezoito ao "
        "quadrado: [p=0.2] *trinta e nove vírgula vinte e quatro por cento.* [p=0.4] {b}Na Y: [p=0.2] três por cento "
        "ao mês. [p=0.2] Um vírgula zero três elevado a doze: [p=0.2] *cerca de quarenta e dois vírgula seis.* [p=0.4] "
        "{c}Capitalização mais frequente, [p=0.2] efetiva maior. [p=0.3] {ok}*Letra D!*"),
    dict(id="27", block="qnova", text=
        "{t}E as pegadinhas? [p=0.3] {xa}A A toma a *nominal pela efetiva.* [p=0.4] {xb}A B calcula certo a efetiva da "
        "X, [p=0.2] mas ela é a *menor.* [p=0.4] {xc}A C acerta a financeira [p=0.2] e *esquece de capitalizar.* "
        "[p=0.4] {xe}E a E é o fator [p=0.2] *sem tirar o um.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="28", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] taxa nominal: divida pelas capitalizações e "
        "capitalize. [p=0.5] {b}Dois: [p=0.2] taxas em sequência: multiplique os fatores, inclusive os menores que um. "
        "[p=0.5] {c}Três: [p=0.2] taxa média por período é a equivalente, não a média das porcentagens."),

    # ================= PONTE E CTA =================
    dict(id="29", block="ponte", text=
        "{a}Se os preços sobem *vinte e cinco por cento* [p=0.2] e o seu salário fica parado, [p=0.3] {b}você perde "
        "vinte e cinco por cento do poder de compra? [p=0.4] {c}*Não.* [p=0.3] Próximo episódio: [p=0.2] *inflação.*"),
    dict(id="30", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] o seu cartão de crédito mostra a taxa *ao mês* ou *ao ano?* "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um "
        "link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para "
        "revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no "
        "Estudativo. [p=1.5]"),
]
