# Roteiro — Porcentagem, Episódio 3 de 6: Variações sucessivas, multiplicar os fatores, nunca somar as porcentagens
# Base: Estudos/Enem/estudos/01-matematica/09-porcentagem.html — seção 05 (+ Questões 3 e 6 da seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   BOLA DE NEVE: o segundo aumento incide sobre a bola que já cresceu, por isso vale mais em reais.
#   CORRENTE de máquinas de fator: o preço passa por uma máquina, depois pela outra; multiplique as máquinas (ep. 2).
# Frases do usuário mantidas IGUAIS: gancho, promessa, as 3 frases-chave e a ponte.
# Gancho e blocos b) (salário 10% + 20%) e e) (30% off + 10% no caixa) = as próprias Questões 3 e 6, por desenho do usuário.
#   As questões entram como "a prova oficial": enunciado do material, pausa, resolução curta pelos fatores, conferência em
#   reais e foco nas alternativas erradas.
# Juros compostos: só citados (a mesma variação repetida vira potência: 1,10³ = 1,331). Sem fórmula de juros.
# QUESTÃO 3 do material (texto idêntico na tela): 1,10 · 1,20 = 1,32 → +32% → C. Conferência: 1 000 → 1 100 → 1 320.
#   Material: B (30%) = soma ingênua. Explicações NOSSAS: A (15%) = a média das duas taxas; E (200%) = multiplicou as
#   taxas (10 × 20 = 200); D (33%) não sai das contas deste enunciado (lembra o 33,1% de TRÊS aumentos de 10%).
# QUESTÃO 6 do material: 0,70 · 0,90 = 0,63 → paga 63% → desconto 37% → B. Conferência: 100 → 70 → 63.
#   Material: C (40%) = soma das taxas; E (63%) = confundiu o que se PAGA com o que se DESCONTA. Explicações NOSSAS:
#   A (33%) = aplicou os 10% sobre o desconto (30 + 3); D (43%) não sai de conta certa (descontos somados nunca passam de 40%).
# Nós fazemos (prompt): +50% e depois +50% → 1,5 · 1,5 = 2,25 → +125% (100 → 150 → 225).
# Atalhos (verde): "× 1,10 é somar 10% do próprio número" (1,20 + 0,12 = 1,32) · "depois do 1, a parte que entrou" ·
#   "o fator de desconto é o que você PAGA; o desconto é 1 menos ele".
# Frases-chave (meio e fim, idênticas): 1. Variações em sequência: multiplique os fatores.
#   2. A segunda variação incide sobre o valor já alterado. 3. A ordem não muda o resultado.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Variações sucessivas: multiplique os fatores, nunca some as porcentagens | Porcentagem Ep. 3"
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
        "{a}Seu salário sobe *dez por cento* em janeiro [p=0.2] e *vinte por cento* em julho. [p=0.4] {b}Subiu trinta por "
        "cento no ano? [p=0.4] {c}Não: [p=0.2] subiu *trinta e dois.* [p=0.5] {d}E com descontos, [p=0.2] acontece o "
        "contrário: [p=0.3] {e}trinta por cento mais dez por cento [p=0.2] *não dão quarenta.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai resolver *qualquer sequência* de aumentos e descontos [p=0.3] {b}com uma "
        "*única conta.*"),
    dict(id="03", block="prereq", text=
        "{t}Antes, um lembrete rápido do episódio dois: [p=0.2] o *fator.* [p=0.4] {a}Aumento de dez por cento: [p=0.2] "
        "fator *um vírgula dez.* [p=0.3] O um é o que você já tinha. [p=0.4] {b}Desconto de trinta por cento: [p=0.2] fator "
        "*zero vírgula setenta.* [p=0.3] Sobra setenta por cento. [p=0.4] {c}Uma multiplicação [p=0.2] e o preço novo sai "
        "pronto."),

    # ================= BLOCO B: EM REAIS, MÊS A MÊS =================
    dict(id="04", block="salario", text=
        "{t}Vamos fazer em reais, [p=0.2] sem pressa. [p=0.3] {a}O salário é de *mil reais.* [p=0.4] {b}Em janeiro, sobe dez "
        "por cento: [p=0.2] dez por cento de mil é *cem.* [p=0.2] Vai para *mil e cem.* [p=0.4] {c}Em julho, sobe vinte por "
        "cento. [p=0.3] Vinte por cento *de quê?* [p=0.3] {d}Do salário de agora: [p=0.2] *mil e cem.* [p=0.2] Vinte por "
        "cento de mil e cem [p=0.2] é *duzentos e vinte.* [p=0.4] {e}Salário final: [p=0.2] *mil trezentos e vinte reais.*"),
    dict(id="05", block="salario", text=
        "{t}Quanto subiu no ano? [p=0.3] {a}De mil para mil trezentos e vinte: [p=0.2] *trezentos e vinte* a mais. [p=0.4] "
        "{b}Trezentos e vinte de mil [p=0.2] é *trinta e dois por cento.* [p=0.4] {c}Esse é o aumento *acumulado:* [p=0.2] o "
        "total, [p=0.2] somando o efeito de todos os aumentos."),

    # ================= BLOCO A: A REGRA =================
    dict(id="06", block="regra", text=
        "{t}Isso tem nome: [p=0.2] *variação sucessiva.* [p=0.3] É uma mudança [p=0.2] *depois* da outra. [p=0.4] {a}E a regra "
        "é uma só: [p=0.3] {b}*multiplique os fatores,* [p=0.3] {c}*nunca some as porcentagens.*"),
    dict(id="07", block="regra", text=
        "{t}Veja com os fatores. [p=0.3] {a}O salário passa pela primeira máquina: [p=0.2] *vezes um vírgula dez.* [p=0.4] "
        "{b}Depois, pela segunda: [p=0.2] *vezes um vírgula vinte.* [p=0.4] {c}É uma *corrente* de máquinas. [p=0.3] Junte as "
        "duas numa só: [p=0.2] um vírgula dez vezes um vírgula vinte [p=0.2] *dá um vírgula trinta e dois.* [p=0.4] {d}O um é o "
        "que já existia. [p=0.2] O zero vírgula trinta e dois [p=0.2] é o que entrou: [p=0.2] *trinta e dois por cento.* "
        "[p=0.3] O mesmo resultado das contas em reais."),
    dict(id="08", block="regra", text=
        "{t}E como fazer essa conta de cabeça? [p=0.3] {a}Multiplicar por um vírgula dez [p=0.2] é *somar dez por cento do "
        "próprio número.* [p=0.4] {b}Um vírgula vinte, [p=0.2] mais dez por cento dele, [p=0.2] que é zero vírgula doze: "
        "[p=0.2] *um vírgula trinta e dois.* [p=0.4] {c}Sem armar conta nenhuma."),

    # ================= BLOCO C: POR QUE NÃO DÁ 30% =================
    dict(id="09", block="bola", text=
        "{t}Mas por que não deu trinta por cento? [p=0.4] {a}Pense numa *bola de neve.* [p=0.3] O primeiro aumento [p=0.2] "
        "cresce a bola: [p=0.2] *mil* vira *mil e cem.* [p=0.4] {b}O segundo aumento [p=0.2] incide sobre a bola que *já "
        "cresceu.* [p=0.3] Os vinte por cento são de mil e cem, [p=0.2] *não de mil.* [p=0.4] {c}Por isso valem *duzentos e "
        "vinte* reais, [p=0.2] e não duzentos. [p=0.4] {d}Esses *vinte reais* a mais [p=0.2] são os dois por cento que a soma "
        "esquece."),

    # ================= BLOCO D: A ORDEM NÃO IMPORTA =================
    dict(id="10", block="ordem", text=
        "{t}E se os aumentos viessem ao contrário? [p=0.3] Primeiro vinte, [p=0.2] depois dez? [p=0.4] {a}Mil, [p=0.2] mais "
        "vinte por cento: [p=0.2] *mil e duzentos.* [p=0.3] {b}Mais dez por cento de mil e duzentos, [p=0.2] que é cento e "
        "vinte: [p=0.2] *mil trezentos e vinte.* [p=0.4] {c}O mesmo valor! [p=0.4] {d}Um vírgula vinte vezes um vírgula dez "
        "[p=0.2] é igual a um vírgula dez vezes um vírgula vinte. [p=0.3] Na multiplicação, [p=0.2] a ordem não muda o "
        "resultado: [p=0.2] ela é *comutativa.*"),

    # ================= BLOCO E: DESCONTOS CUMULATIVOS =================
    dict(id="11", block="descontos", text=
        "{t}Agora, os descontos. [p=0.3] {a}Uma loja anuncia: [p=0.2] *trinta por cento off* em tudo, [p=0.3] {b}e mais *dez "
        "por cento* no caixa. [p=0.4] {c}Descontos *cumulativos:* [p=0.2] um aplicado em cima do outro. [p=0.4] {d}Uma blusa "
        "de *cem reais.* [p=0.2] Com trinta por cento a menos, [p=0.2] vai para *setenta.* [p=0.4] {e}No caixa, [p=0.2] dez "
        "por cento de *setenta:* [p=0.2] sete reais. [p=0.3] Você paga *sessenta e três.*"),
    dict(id="12", block="descontos", text=
        "{t}Com os fatores: [p=0.3] {a}zero vírgula setenta [p=0.2] vezes zero vírgula noventa [p=0.2] *dá zero vírgula "
        "sessenta e três.* [p=0.4] {b}Você *paga* sessenta e três por cento do preço. [p=0.4] {c}Então o desconto foi de cem "
        "menos sessenta e três: [p=0.2] *trinta e sete por cento.* [p=0.4] {d}Menos que a soma. [p=0.3] É a bola de neve ao "
        "contrário: [p=0.2] o segundo desconto incide sobre um preço que *já encolheu.*"),
    dict(id="13", block="descontos", text=
        "{t}E aqui mora uma pegadinha. [p=0.3] {a}O zero vírgula sessenta e três [p=0.2] é o que você *paga.* [p=0.4] {b}O "
        "desconto [p=0.2] é *um menos* esse número: [p=0.2] trinta e sete. [p=0.4] {c}Atalho: [p=0.2] *o fator de desconto é o "
        "que fica no seu bolso para pagar.* [p=0.3] Sempre confira se a questão pede o que se paga [p=0.2] ou o que se "
        "desconta."),

    # ================= BLOCO F: A MESMA VARIAÇÃO REPETIDA =================
    dict(id="14", block="potencia", text=
        "{t}E se a *mesma* variação se repete? [p=0.3] {a}Três aumentos de dez por cento, [p=0.2] um depois do outro. "
        "[p=0.4] {b}Um vírgula dez, [p=0.2] vezes um vírgula dez, [p=0.2] vezes um vírgula dez. [p=0.4] {c}Multiplicar o "
        "mesmo número várias vezes [p=0.2] é uma *potência:* [p=0.3] o número pequeno lá em cima [p=0.2] diz quantas vezes ele "
        "se multiplica. [p=0.4] {d}Um vírgula dez ao cubo [p=0.2] dá *um vírgula trezentos e trinta e um.* [p=0.3] Aumento "
        "de *trinta e três vírgula um por cento,* [p=0.2] e não trinta. [p=0.4] {e}Essa é a porta de entrada dos *juros "
        "compostos,* [p=0.2] que vão ter uma série só deles."),

    # ================= NÓS FAZEMOS =================
    dict(id="15", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Um preço sobe *cinquenta por cento,* [p=0.2] e depois mais *cinquenta por cento.* [p=0.4] "
        "{b}Qual foi o aumento *total?* [p=0.3] {c}*Pause o vídeo e calcule.* [p=2.0]"),
    dict(id="16", block="exercicio", text=
        "{t}Vamos conferir. [p=0.3] {a}Os fatores: [p=0.2] um vírgula cinco [p=0.2] vezes um vírgula cinco [p=0.2] *dá dois "
        "vírgula vinte e cinco.* [p=0.4] {b}O um é o que existia. [p=0.2] O resto, [p=0.2] um vírgula vinte e cinco, [p=0.2] é "
        "*cento e vinte e cinco por cento* de aumento. [p=0.4] {c}Em reais: [p=0.2] cem vira cento e cinquenta, [p=0.2] e "
        "cento e cinquenta vira *duzentos e vinte e cinco.* [p=0.4] {d}Quem somou [p=0.2] respondeu cem por cento. [p=0.2] "
        "Errou por *vinte e cinco.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="17", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] variações em sequência: [p=0.2] multiplique os fatores. "
        "[p=0.5] {b}Dois: [p=0.2] a segunda variação incide sobre o valor já alterado. [p=0.5] {c}Três: [p=0.2] a ordem não "
        "muda o resultado."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="18", block="erros", text=
        "{t}Agora, os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *somar* as porcentagens. [p=0.2] Mais dez e mais "
        "vinte, [p=0.2] mais trinta. [p=0.4] {b}Parece certo, [p=0.2] porque somar é o que a gente faz com tudo. [p=0.4] "
        "{c}Mas o segundo aumento é calculado sobre o valor *já aumentado.* [p=0.3] Multiplique os fatores: [p=0.2] *trinta e "
        "dois.*"),
    dict(id="19", block="erros", text=
        "{a}Segundo: [p=0.2] *somar os descontos.* [p=0.2] Trinta e dez, [p=0.2] quarenta. [p=0.4] {b}Parece certo, [p=0.2] "
        "porque a placa mostra dois números com por cento. [p=0.4] {c}Mas o desconto do caixa é sobre um preço *menor.* "
        "[p=0.3] O desconto total é de *trinta e sete.*"),
    dict(id="20", block="erros", text=
        "{a}Terceiro: [p=0.2] confundir o que se *paga* [p=0.2] com o que se *desconta.* [p=0.4] {b}Parece certo, [p=0.2] "
        "porque o sessenta e três sai direto da conta. [p=0.4] {c}Mas o sessenta e três é o que você *paga.* [p=0.3] O "
        "desconto é cem menos sessenta e três: [p=0.2] *trinta e sete.*"),

    # ================= QUESTÃO 3 DO MATERIAL =================
    dict(id="21", block="q3", text=
        "{t}Agora, a prova oficial: [p=0.2] uma questão no estilo do ENEM, [p=0.2] do nosso material de estudo. [p=0.4] {a}O "
        "salário de um funcionário recebeu um reajuste de *dez por cento* em janeiro [p=0.2] e outro de *vinte por cento* em "
        "julho, [p=0.2] ambos aplicados sobre o valor vigente na data. [p=0.4] {b}O aumento *acumulado* no ano foi de: [p=0.4] "
        "{qa}A: [p=0.2] quinze por cento. [p=0.3] {qb}B: [p=0.2] trinta. [p=0.3] {qc}C: [p=0.2] trinta e dois. [p=0.3] {qd}D: "
        "[p=0.2] trinta e três. [p=0.3] {qe}E: [p=0.2] duzentos por cento. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="22", block="q3", text=
        "{t}É o salário do começo da aula. [p=0.3] {a}Os fatores: [p=0.2] um vírgula dez vezes um vírgula vinte, [p=0.2] *um "
        "vírgula trinta e dois.* [p=0.4] {b}Conferindo em reais: [p=0.2] mil, [p=0.2] mil e cem, [p=0.2] mil trezentos e "
        "vinte. [p=0.3] {ok}*Letra C!* [p=0.2] Trinta e dois por cento. [p=0.5] {xb}A B é a *soma* ingênua das taxas. "
        "[p=0.4] {xa}A A é a *média* das duas taxas. [p=0.4] {xe}A E *multiplicou as taxas:* [p=0.2] dez vezes vinte, "
        "[p=0.2] duzentos. [p=0.4] {xd}E a D não sai das contas deste enunciado: [p=0.2] lembra o aumento de *três* "
        "aumentos de dez por cento."),

    # ================= QUESTÃO 6 DO MATERIAL =================
    dict(id="23", block="q6", text=
        "{t}E a segunda. [p=0.3] {a}Uma loja anuncia *trinta por cento* de desconto em toda a coleção [p=0.2] e oferece "
        "ainda *dez por cento* adicionais de abatimento no caixa, [p=0.2] aplicados sobre o valor já reduzido. [p=0.4] {b}O "
        "*desconto total* obtido pelo cliente é de: [p=0.4] {qa}A: [p=0.2] trinta e três por cento. [p=0.3] {qb}B: [p=0.2] "
        "trinta e sete. [p=0.3] {qc}C: [p=0.2] quarenta. [p=0.3] {qd}D: [p=0.2] quarenta e três. [p=0.3] {qe}E: [p=0.2] "
        "sessenta e três. [p=0.5] {p}*Pause o vídeo e tente.* [p=2.0]"),
    dict(id="24", block="q6", text=
        "{t}Vamos resolver. [p=0.3] {a}Zero vírgula setenta [p=0.2] vezes zero vírgula noventa: [p=0.2] *zero vírgula "
        "sessenta e três.* [p=0.4] {b}O cliente paga sessenta e três por cento. [p=0.3] O desconto é de *trinta e sete.* "
        "[p=0.3] {ok}*Letra B!* [p=0.4] {c}Em reais: [p=0.2] cem, [p=0.2] setenta, [p=0.2] sessenta e três. [p=0.5] {xe}A E "
        "é a pegadinha: [p=0.2] sessenta e três é o que se *paga,* [p=0.2] não o que se desconta. [p=0.4] {xc}A C *somou* "
        "as taxas. [p=0.4] {xa}A A aplicou os dez por cento sobre o próprio desconto: [p=0.2] trinta mais três. [p=0.4] "
        "{xd}E a D não sai de conta certa: [p=0.2] dois descontos em sequência [p=0.2] nunca passam da soma."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="25", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] variações em sequência: [p=0.2] multiplique os "
        "fatores. [p=0.5] {b}Dois: [p=0.2] a segunda variação incide sobre o valor já alterado. [p=0.5] {c}Três: [p=0.2] a "
        "ordem não muda o resultado."),

    # ================= PONTE E CTA =================
    dict(id="26", block="ponte", text=
        "{a}E se o preço sobe *vinte por cento* [p=0.2] e depois cai *vinte por cento?* [p=0.4] {b}Volta ao original? "
        "[p=0.3] *Não.* [p=0.4] {c}E o motivo é o mesmo que derruba a pergunta: [p=0.2] *que desconto desfaz um aumento.* "
        "[p=0.4] {d}Próximo episódio."),
    dict(id="27", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha somado dois descontos? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* "
        "no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
