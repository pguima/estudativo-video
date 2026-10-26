# Roteiro — Sistemas de Equações Lineares, Episódio 2 de 5: o método da adição e quando a pergunta já é a soma.
# Base: Estudos/Enem/estudos/01-matematica/22-sistemas-equacoes-lineares.html — seção 05 + Questões 4 e 7.
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (retomadas na série):
#   Somar equações é JUNTAR DUAS NOTAS FISCAIS: soma-se o que foi comprado e soma-se o que foi pago.
#   Coeficientes opostos se anulam como +2 e −2 numa BALANÇA: a incógnita some.
#   Multiplicar a equação é COMPRAR O MESMO PEDIDO 3 VEZES: tudo triplica, inclusive o valor pago.
#   Antes de resolver, olhe o que foi pedido: às vezes a SACOLA já é a resposta.
# Frases do usuário mantidas IGUAIS: gancho, promessa ("Ao final, ..."), as 3 frases-chave e a ponte.
# Exemplos (todos conferidos em Python):
#   Bloco a: 3x + 2y = 16 e 5x − 2y = 16 → 8x = 32 → x = 4 → 12 + 2y = 16 → y = 2; conferência 20 − 4 = 16.
#   Bloco b: 2x + 3y = 12 (× 3) e 3x + 2y = 13 (× 2) → 6x + 9y = 36 e 6x + 4y = 26 → subtraindo, 5y = 10 → y = 2 → x = 3;
#     conferência 9 + 4 = 13. Bloco d: somando sem multiplicar, 5x + 5y = 25 → x + y = 5 (3 + 2 = 5).
#   Erro 1 (só o lado esquerdo): 6x + 9y = 12 com 6x + 4y = 26 dá 5y = −14 → y = −2,8 (absurdo).
#   Erro 2 (exemplo nosso, para não reaproveitar a Q7): 3 pães + 1 café = R$ 13,00 e 1 pão + 3 cafés = R$ 11,00;
#     pede pão + café. Somando: 4p + 4c = 24 → R$ 6,00. Resolver tudo dá pão R$ 3,50 e café R$ 2,50 (mais longo).
#   Erro 3: somar 6x + 9y = 36 e 6x + 4y = 26 dá 12x + 13y = 62 (nada some); coeficientes IGUAIS pedem subtração.
# Nós fazemos (prompt): x + 2y = 11 e 3x − 2y = 1 → 4x = 12 → x = 3 → 2y = 8 → y = 4; conferência 9 − 8 = 1.
# QUESTÃO 4 (eu faço; texto idêntico): a + b = 60 e 30a + 45b = 40 · 60 = 2 400. × 30: 30a + 30b = 1 800; subtraindo:
#   15b = 600 → b = 40 kg (caro), a = 20 kg (barato) → B. Substituição do material: 15a = 300. Conferência 600 + 1 800.
#   Erradas (material): D 40 é o café caro; C 30 supõe partes iguais (preço médio 37,50, não 40); A 10 usa 40 − 30 como
#   quantidade; E 50 é 60 − 10.
# QUESTÃO 7 (você faz; texto idêntico): somando, 3S + 3J = 57 → S + J = 19 → C. Subtraindo, S − J = 5 → S = 12, J = 7.
#   Erradas (material): A 7 é o suco; B 12 é o sanduíche; E 57 é a sacola inteira (três de cada); D 28,50 divide 57 por 2.
#   OBSERVAÇÃO: o gancho e a cena concreta do prompt já entregam os R$ 19,00 (desenho do próprio prompt, mantido). Na Q7
#   o aluno refaz o caminho sozinho; o que é novo ali são os preços separados e as alternativas erradas.
# Atalhos (verde): olhe a coluna antes (sinais opostos → some; iguais → subtraia) · multiplique cruzado (cada equação
#   pelo coeficiente da outra) · coeficientes trocados (2 e 3 / 3 e 2) → some e divida: sai x + y direto.
# Frases-chave (meio e fim, idênticas): 1. Some as equações para uma incógnita sumir. 2. Multiplicou? Multiplique a
#   equação inteira. 3. Antes de resolver, olhe o que foi pedido.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = "Sistemas lineares: o método da adição e o truque da soma | Sistemas Lineares Ep. 2"
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
        "{a}Dois sanduíches e um suco: [p=0.2] *trinta e um reais.* [p=0.4] {b}Um sanduíche e dois sucos: [p=0.2] *vinte e "
        "seis reais.* [p=0.5] {c}Quanto custam um sanduíche e um suco juntos? [p=0.6] {d}*Dezenove reais,* [p=0.3] {e}e "
        "você vai descobrir isso *sem calcular o preço de nenhum dos dois.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final, [p=0.2] você vai resolver sistemas *pela adição* [p=0.3] {b}e reconhecer quando a pergunta sai "
        "*somando as equações.*"),
    dict(id="03", block="prereq", text=
        "{t}Um lembrete do episódio um. [p=0.3] {a}Um *sistema* são duas equações que valem *ao mesmo tempo,* [p=0.2] "
        "cada uma no molde *quantidade vezes valor, igual ao total.* [p=0.4] {b}E a resposta só está certa se *bater "
        "nas duas.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{t}Como chegar nos dezenove? [p=0.4] {a}Pegue as duas notas fiscais. [p=0.3] {b}Junte as compras numa *sacola "
        "só.* [p=0.4] {c}Dentro dela: [p=0.2] *três sanduíches* e *três sucos.* [p=0.3] {d}Total pago: [p=0.2] trinta e "
        "um mais vinte e seis, [p=0.2] *cinquenta e sete.* [p=0.5] {e}Três combos, cinquenta e sete. [p=0.2] Um combo: "
        "[p=0.2] dividido por três, [p=0.2] *dezenove.*"),

    # ================= BLOCO A: COEFICIENTES OPOSTOS =================
    dict(id="05", block="opostos", text=
        "{t}Isso tem nome? [p=0.4] {a}Tem: [p=0.2] *método da adição,* [p=0.2] somar as duas equações, lado com lado. "
        "[p=0.4] {b}É *juntar duas notas fiscais:* [p=0.2] soma-se o que foi comprado [p=0.2] e soma-se o que foi pago. "
        "[p=0.4] {c}O objetivo: [p=0.2] *eliminar uma incógnita,* [p=0.2] fazer uma letra desaparecer."),
    dict(id="06", block="opostos", text=
        "{t}E quando uma letra desaparece? [p=0.4] {a}*Três x mais dois y, igual a dezesseis,* [p=0.2] e *cinco x menos "
        "dois y, igual a dezesseis.* [p=0.4] {b}O número que multiplica a letra é o *coeficiente.* [p=0.4] {c}O y tem "
        "*mais dois* e *menos dois:* [p=0.2] *coeficientes opostos.* [p=0.4] {d}Eles se anulam como numa balança: "
        "[p=0.2] *o y some.*"),
    dict(id="07", block="opostos", text=
        "{t}Somando lado com lado. [p=0.4] {a}Três x mais cinco x: [p=0.2] *oito x.* [p=0.2] Mais dois y menos dois y: "
        "[p=0.2] *zero.* [p=0.2] Dezesseis mais dezesseis: [p=0.2] *trinta e dois.* [p=0.4] {b}Oito x igual a trinta e "
        "dois: [p=0.2] *x igual a quatro.* [p=0.4] {c}Agora volte numa equação: [p=0.2] doze, mais dois y, igual a "
        "dezesseis. [p=0.2] *y igual a dois.* [p=0.4] {d}Confere na outra: [p=0.2] vinte menos quatro, [p=0.2] "
        "*dezesseis.* [p=0.3] {ok}*Bateu!*"),
    dict(id="08", block="opostos", text=
        "{t}Atalho: [p=0.2] *olhe a coluna antes.* [p=0.4] {a}x embaixo de x, [p=0.2] y embaixo de y. [p=0.4] {b}Sinais "
        "*opostos?* [p=0.2] *Some.* [p=0.3] {c}Números *iguais,* mesmo sinal? [p=0.2] *Subtraia.* [p=0.4] {d}Nos dois "
        "casos, a letra some."),

    # ================= BLOCO B: MULTIPLICANDO ANTES =================
    dict(id="09", block="multiplicar", text=
        "{t}E se nenhuma coluna se anula? [p=0.4] {a}*Dois x mais três y, igual a doze,* [p=0.2] e *três x mais dois y, "
        "igual a treze.* [p=0.4] {b}Antes de somar, a gente *multiplica uma equação.* [p=0.4] {c}É *comprar o mesmo "
        "pedido três vezes:* [p=0.2] tudo triplica, [p=0.2] inclusive o valor pago."),
    dict(id="10", block="multiplicar", text=
        "{t}Vamos igualar o x. [p=0.4] {a}A primeira, vezes *três:* [p=0.2] seis x, mais nove y, igual a *trinta e "
        "seis.* [p=0.4] {b}A segunda, vezes *dois:* [p=0.2] seis x, mais quatro y, igual a *vinte e seis.* [p=0.4] "
        "{c}Seis x e seis x, iguais: [p=0.2] *subtraia.* [p=0.2] *Cinco y igual a dez,* [p=0.2] *y igual a dois.* "
        "[p=0.4] {d}Na primeira: [p=0.2] dois x, mais seis, igual a doze: [p=0.2] *x igual a três.* [p=0.4] {e}Na "
        "segunda: [p=0.2] nove mais quatro, *treze.* [p=0.3] {ok}*Bateu!*"),

    # ================= BLOCO C: A EQUAÇÃO INTEIRA =================
    dict(id="11", block="inteira", text=
        "{t}O cuidado: [p=0.4] {a}o vezes três abraça a equação *inteira,* [p=0.2] como um laço. [p=0.4] {b}Dois x vira "
        "seis x, [p=0.2] três y vira nove y, [p=0.3] {c}e o doze vira *trinta e seis.* [p=0.4] {d}Quem compra três "
        "vezes [p=0.2] *paga três vezes.*"),
    dict(id="12", block="inteira", text=
        "{t}Atalho: [p=0.2] *multiplique cruzado.* [p=0.4] {a}O x tem dois numa equação e três na outra. [p=0.4] "
        "{b}Cada equação vai vezes o número *da outra.* [p=0.4] {c}Os dois viram *seis x.* [p=0.2] Sempre dá certo."),

    # ================= BLOCO D: A PERGUNTA É A SOMA =================
    dict(id="13", block="soma", text=
        "{t}E se a pergunta fosse outra? [p=0.4] {a}Nesse mesmo sistema, [p=0.2] e se pedissem só *x mais y?* [p=0.4] "
        "{b}Some *sem multiplicar nada.* [p=0.4] {c}Cinco x, [p=0.2] cinco y, [p=0.2] vinte e cinco. [p=0.4] {d}Divida "
        "por cinco: [p=0.2] *x mais y igual a cinco.* [p=0.4] {e}Em *uma linha.* [p=0.2] E bate: [p=0.2] três mais "
        "dois."),
    dict(id="14", block="soma", text=
        "{t}Atalho: [p=0.2] *coeficientes trocados.* [p=0.4] {a}Dois e três numa equação, [p=0.2] três e dois na outra. "
        "[p=0.4] {b}Somando, x e y ficam com o *mesmo* coeficiente. [p=0.4] {c}É só dividir: [p=0.2] às vezes *a sacola "
        "já é a resposta.*"),

    # ================= BLOCO E: QUAL MÉTODO =================
    dict(id="15", block="escolha", text=
        "{t}Então, substituição ou adição? [p=0.4] {a}Alguma letra está *sozinha,* com coeficiente um? [p=0.2] "
        "*Substituição,* do episódio um. [p=0.4] {b}Coeficientes *opostos,* ou fáceis de igualar? [p=0.2] *Adição.* "
        "[p=0.4] {c}A pergunta é *x mais y?* [p=0.2] *Some antes de tudo.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Resolva: [p=0.2] *x mais dois y, igual a onze,* [p=0.2] e *três x menos dois y, igual a "
        "um.* [p=0.3] {p}*Pause e tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Coluna do y: [p=0.2] mais dois e menos dois. [p=0.2] *Some.* [p=0.4] {b}*Quatro x "
        "igual a doze,* [p=0.2] *x igual a três.* [p=0.4] {c}Na primeira: [p=0.2] três, mais dois y, igual a onze: "
        "[p=0.2] *y igual a quatro.* [p=0.4] {d}Na segunda: [p=0.2] nove menos oito, [p=0.2] *um.* [p=0.3] {ok}*Bateu!*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Três frases para guardar. [p=0.5] {a}Um: [p=0.2] some as equações para uma incógnita sumir. [p=0.5] {b}Dois: "
        "[p=0.2] multiplicou? [p=0.2] Multiplique a equação inteira. [p=0.5] {c}Três: [p=0.2] antes de resolver, olhe o "
        "que foi pedido."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{a}Erro número um: [p=0.2] multiplicar *só o lado esquerdo:* [p=0.2] seis x mais nove y, *igual a doze.* "
        "[p=0.4] {b}Parece certo porque o olho fica nas letras. [p=0.4] {c}Correção: [p=0.2] o laço vai até o lado "
        "direito: [p=0.2] *trinta e seis.* [p=0.2] Com o doze, o y sairia negativo: [p=0.2] um preço de *menos dois e "
        "oitenta.*"),
    dict(id="20", block="erros", text=
        "{a}Erro número dois: [p=0.2] resolver *tudo* quando a pergunta é a soma. [p=0.4] {a2}Três pães e um café, "
        "[p=0.2] treze reais; [p=0.2] um pão e três cafés, [p=0.2] onze. [p=0.2] Quanto custa um de cada? [p=0.4] "
        "{b}Parece certo porque é o caminho de sempre. [p=0.2] Mas sai três e cinquenta e dois e cinquenta: [p=0.2] "
        "conta longa. [p=0.4] {c}Correção: [p=0.2] some. [p=0.2] Quatro de cada, vinte e quatro. [p=0.2] Um de cada: "
        "[p=0.2] *seis reais.*"),
    dict(id="21", block="erros", text=
        "{a}Erro número três: [p=0.2] *somar* quando devia *subtrair.* [p=0.4] {a2}Seis x mais nove y, [p=0.2] mais "
        "seis x mais quatro y: [p=0.2] doze x mais treze y. [p=0.2] Nada some. [p=0.4] {b}Parece certo porque o método "
        "se chama *adição.* [p=0.4] {c}Correção: [p=0.2] coeficientes *iguais* pedem *subtração.* [p=0.2] Sobra cinco y "
        "igual a dez."),

    # ================= QUESTÃO 4 (EU FAÇO) =================
    dict(id="22", block="q4", text=
        "{t}Hora de questão, [p=0.2] e essa eu faço. [p=0.3] {a}Um comerciante mistura um café de *trinta reais o "
        "quilograma* [p=0.2] com outro de *quarenta e cinco reais o quilograma* [p=0.2] e obtém *sessenta quilos* de um "
        "blend que vende a *quarenta reais o quilograma,* [p=0.2] sem ganho nem perda em relação ao custo dos cafés. "
        "[p=0.2] A quantidade usada do café *mais barato* foi de: [p=0.4] {qa}A: [p=0.2] dez quilos. [p=0.3] {qb}B: "
        "[p=0.2] vinte quilos. [p=0.3] {qc}C: [p=0.2] trinta quilos. [p=0.3] {qd}D: [p=0.2] quarenta quilos. [p=0.3] {qe}E: "
        "[p=0.2] cinquenta quilos."),
    dict(id="23", block="q4", text=
        "{t}Primeiro, as etiquetas. [p=0.3] {a}*a* é o café barato, [p=0.2] em quilos. [p=0.2] *b* é o café caro, [p=0.2] "
        "em quilos. [p=0.4] {b}Equação das quantidades: [p=0.2] *a mais b, igual a sessenta.* [p=0.4] {c}Equação do "
        "dinheiro: [p=0.2] *trinta a, mais quarenta e cinco b,* [p=0.2] igual a quarenta vezes sessenta: [p=0.2] *dois mil "
        "e quatrocentos.*"),
    dict(id="24", block="q4", text=
        "{t}Agora a adição. [p=0.4] {a}A primeira vezes *trinta,* [p=0.2] inteira: [p=0.2] trinta a, mais trinta b, "
        "igual a *mil e oitocentos.* [p=0.4] {b}Coluna do a igual: [p=0.2] *subtraia.* [p=0.4] {c}*Quinze b igual a "
        "seiscentos:* [p=0.2] *b igual a quarenta.* [p=0.2] E a, sessenta menos quarenta: [p=0.2] *vinte.* [p=0.4] "
        "{d}Pela substituição do episódio um, [p=0.2] sai *quinze a igual a trezentos:* [p=0.2] mesmo lugar."),
    dict(id="25", block="q4", text=
        "{t}Confere e responde. [p=0.4] {a}Vinte vezes trinta, [p=0.2] seiscentos. [p=0.2] Quarenta vezes quarenta e cinco, "
        "[p=0.2] mil e oitocentos. [p=0.2] Somando: [p=0.2] *dois mil e quatrocentos.* [p=0.3] {ok}*Bateu!* [p=0.4] {b}E o "
        "que foi pedido? [p=0.2] O café *mais barato:* [p=0.2] o a. [p=0.2] *Vinte quilos,* [p=0.2] *letra B.*"),
    dict(id="26", block="q4", text=
        "{t}E as erradas? [p=0.3] {xd}A D, quarenta, [p=0.2] é o café *caro:* [p=0.2] respondeu a letra errada. [p=0.4] "
        "{xc}A C supõe *partes iguais:* [p=0.2] o preço médio seria trinta e sete e cinquenta, [p=0.2] não quarenta. "
        "[p=0.4] {xa}A A usou quarenta menos trinta [p=0.2] como quantidade. [p=0.4] {xe}E a E é sessenta menos dez."),

    # ================= QUESTÃO 7 (VOCÊ FAZ) =================
    dict(id="27", block="q7", text=
        "{t}Agora é com você. [p=0.3] {a}Em uma lanchonete, [p=0.2] *dois sanduíches e um suco* custam *trinta e um "
        "reais,* [p=0.2] e *um sanduíche e dois sucos* custam *vinte e seis reais.* [p=0.2] Todos os sanduíches têm o mesmo "
        "preço, assim como os sucos. [p=0.2] Quanto custam, *juntos,* um sanduíche e um suco? [p=0.4] {qa}A: [p=0.2] sete "
        "reais. [p=0.3] {qb}B: [p=0.2] doze reais. [p=0.3] {qc}C: [p=0.2] dezenove reais. [p=0.3] {qd}D: [p=0.2] vinte e "
        "oito e cinquenta. [p=0.3] {qe}E: [p=0.2] cinquenta e sete reais. [p=0.4] {p}*Pause e resolva.* [p=2.0]"),
    dict(id="28", block="q7", text=
        "{t}Conferindo. [p=0.3] {a}A pergunta é a *soma.* [p=0.2] Some: [p=0.2] *três S mais três J, igual a cinquenta "
        "e sete.* [p=0.4] {b}Divida por três: [p=0.2] *S mais J igual a dezenove.* [p=0.3] {ok}*Letra C!* [p=0.4] {c}E "
        "os preços? [p=0.2] Subtraindo, S menos J, igual a cinco: [p=0.2] sanduíche *doze,* [p=0.2] suco *sete.* "
        "[p=0.4] {d}Confere: [p=0.2] vinte e quatro mais sete, [p=0.2] *trinta e um.*"),
    dict(id="29", block="q7", text=
        "{t}E as erradas? [p=0.3] {xa}A A é o preço do *suco.* [p=0.3] {xb}A B é o do *sanduíche:* [p=0.2] respostas certas "
        "para perguntas que *não foram feitas.* [p=0.4] {xe}A E é a sacola inteira, [p=0.2] com *três* de cada. [p=0.4] "
        "{xd}E a D dividiu cinquenta e sete por *dois,* [p=0.2] como se cada item aparecesse duas vezes."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="30", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] some as equações para uma incógnita sumir. [p=0.5] "
        "{b}Dois: [p=0.2] multiplicou? [p=0.2] Multiplique a equação inteira. [p=0.5] {c}Três: [p=0.2] antes de resolver, "
        "olhe o que foi pedido."),

    # ================= PONTE E CTA =================
    dict(id="31", block="ponte", text=
        "{a}E quando a conta termina em *zero igual a dois?* [p=0.4] {b}Você errou alguma coisa [p=0.2] ou o sistema está "
        "*te dizendo algo?* [p=0.5] {c}Próximo episódio: [p=0.2] as três posições de duas retas."),
    dict(id="32", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] {com}E me conte nos "
        "*comentários:* [p=0.2] você já resolveu um sistema inteiro quando a pergunta era só a soma? [p=0.5] {anki}E tem "
        "mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no *Anki,* "
        "[p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}Bons "
        "estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
