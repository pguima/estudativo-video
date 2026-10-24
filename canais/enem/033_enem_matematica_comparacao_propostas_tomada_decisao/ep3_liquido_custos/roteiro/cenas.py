# Roteiro — Comparação de Propostas e Tomada de Decisão, Episódio 3 de 5: investimentos líquidos e custos escondidos de
#   um empréstimo
# Base: Estudos/Enem/estudos/01-matematica/18-comparacao-propostas-tomada-decisao.html — seções 05 e 06 + Questões 7, 4
#   e 3 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (do prompt):
#   COMPARE O QUE ENTRA NO BOLSO, NÃO O QUE ESTÁ NA VITRINE (rendimento líquido, no mesmo período).
#   O IMPOSTO MORDE SÓ O RENDIMENTO, NÃO O DINHEIRO QUE JÁ ERA SEU (o leão morde só o topo da pilha).
#   A TARIFA NO ATO ENCOLHE O QUE VOCÊ RECEBE, MAS NÃO ENCOLHE O QUE VOCÊ PAGA (o envelope que perde R$ 100,00 na porta).
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Exemplos do material/prompt: 1% a.m. ≈ 12,68% a.a. (1,01¹² ≈ 1,1268) · X 12% com 20% de IR → 9,6% × Y 10% isenta ·
#   R$ 10.000,00 a 12%: rendimento 1.200, IR 240 (não 2.240), resgate 10.960 · empréstimo 5.000 a 4%, tarifa 100 →
#   recebe 4.900, paga 5.200 → 300 ÷ 4.900 ≈ 6,1% · nós fazemos: 2.000 a 5%, tarifa 50 → 150 ÷ 1.950 ≈ 7,7%.
# Taxa real (Taxas Equivalentes, ep. 4) só citada no bloco a, sem conta.
# Atalhos (NOSSOS, verde): líquido = bruto × (1 − alíquota) · custo efetivo pelo fator: pago ÷ recebido, tire o 1
#   (5.200 ÷ 4.900 ≈ 1,061) · 1,06² = 1 + 0,12 + 0,0036 (o "a mais" da capitalização é pequeno, mas decide).
# QUESTÃO 7 (eu faço): E (6,1%). Erradas (material): A 100 ÷ 5.000 = 2% (só a tarifa) · B 4% (a anunciada) ·
#   C 200 ÷ 4.900 ≈ 4,1% (esqueceu a tarifa no numerador) · D 300 ÷ 5.000 = 6% (dividiu pelo contratado).
# QUESTÃO 4 (nós fazemos): D (banco P). P 1,01¹² ≈ 1,127 → ≈ 12,7% · Q 12,5% · R 1,06² = 1,1236 → 12,36% (NÃO 12%).
#   Erradas (material): A e C usam taxas proporcionais (12 · 1% e 2 · 6%) · B: R capitaliza duas vezes, mas 12,36% ainda
#   perde · E: generalização falsa (quem decide é a taxa equivalente, não o período anunciado).
# QUESTÃO 3 (você faz): B (II, R$ 1.000,00). I 1.200 · 0,8 = 960 · II 1.000 · III 1.100 · 0,85 = 935.
#   Erradas (material): C e E usam o rendimento bruto · A e D são líquidos certos de I e III, mas menores que o de II.
# Frases-chave (meio e fim, idênticas): 1. Compare taxas no mesmo período e já líquidas. 2. Imposto incide sobre o
#   rendimento, não sobre o total. 3. Custo efetivo é o que você paga a mais dividido pelo que você recebeu.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = ("4% ao mês que vira 6,1%: rendimento líquido e custo efetivo · Matemática ENEM, Comparação de propostas "
          "episódio 3")

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
    "CET": "cê é tê",
}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="hook", text=
        "{a}Um empréstimo anuncia *quatro por cento ao mês.* [p=0.4] {b}Você paga *seis vírgula um.* [p=0.5] "
        "{c}Ninguém mentiu na taxa: [p=0.3] a diferença estava numa *tarifa de cem reais* [p=0.2] cobrada no ato."),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai comparar aplicações pelo *rendimento líquido* [p=0.3] {b}e calcular "
        "o *custo efetivo* de um empréstimo com tarifas."),
    dict(id="03", block="prereq", text=
        "{t}Três lembretes rápidos. [p=0.3] {a}De Taxas Equivalentes: [p=0.2] para mudar o período de uma taxa, "
        "[p=0.2] *eleve o fator.* [p=0.2] Não multiplique a taxa. [p=0.4] {b}Para tirar a inflação, [p=0.2] *divida os "
        "fatores.* [p=0.4] {c}E de Empréstimos: [p=0.2] taxa embutida [p=0.2] é o que se *pagou a mais,* [p=0.2] "
        "dividido pelo *valor financiado.*"),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{a}Imagine três cartazes de banco, lado a lado. [p=0.3] {b}*Um por cento ao mês.* [p=0.2] *Doze e meio por "
        "cento ao ano.* [p=0.2] *Seis por cento ao semestre.* [p=0.4] {c}Qual paga mais? [p=0.3] Assim, direto, "
        "[p=0.2] não dá para saber."),
    dict(id="05", block="concreto", text=
        "{a}Agora, um extrato de aplicação, [p=0.2] com uma linha chamada *I R retido:* [p=0.2] o imposto que o banco "
        "já descontou. [p=0.4] {b}E um contrato de empréstimo, [p=0.2] com uma *tarifa de cadastro* [p=0.2] tirada "
        "no dia em que o dinheiro sai. [p=0.4] {c}Os três escondem a mesma coisa: [p=0.2] o número da vitrine *não é o "
        "que chega ao seu bolso.*"),

    # ================= BLOCO A: OS TRÊS AJUSTES =================
    dict(id="06", block="ajustes", text=
        "{t}O que fazer antes de comparar? [p=0.4] {a}Três ajustes. [p=0.2] Primeiro: [p=0.2] colocar tudo no *mesmo "
        "período.* [p=0.4] {b}Segundo: [p=0.2] tirar o *imposto.* [p=0.4] {c}Terceiro, [p=0.2] quando a questão pede: "
        "[p=0.2] tirar a *inflação,* [p=0.2] dividindo os fatores, [p=0.2] como em Taxas Equivalentes."),
    dict(id="07", block="ajustes", text=
        "{t}E o mesmo período, na prática? [p=0.4] {a}Um por cento ao mês, [p=0.2] em doze meses, [p=0.2] é um vírgula "
        "zero um *elevado a doze.* [p=0.2] Dá cerca de *um vírgula um dois seis oito.* [p=0.4] {b}Ou seja, [p=0.2] "
        "*doze vírgula seis oito por cento ao ano.* [p=0.4] {c}Mais que os doze e meio do cartaz anual. [p=0.3] A "
        "regra é uma só: [p=0.2] *compare o que entra no bolso, [p=0.2] não o que está na vitrine.*"),

    # ================= BLOCO B: O IMPOSTO =================
    dict(id="08", block="imposto", text=
        "{t}E o imposto, [p=0.2] morde quanto? [p=0.4] {a}*Rendimento bruto* [p=0.2] é o que a aplicação rendeu antes "
        "do imposto. [p=0.4] {b}*Alíquota* [p=0.2] é a porcentagem do imposto. [p=0.2] E o *imposto sobre o "
        "rendimento* [p=0.2] incide só sobre o que rendeu. [p=0.4] {c}O que sobra [p=0.2] é o *rendimento líquido:* "
        "[p=0.2] o que entra de verdade no bolso."),
    dict(id="09", block="imposto", text=
        "{t}Então compare: [p=0.2] qual rende mais? [p=0.4] {a}A aplicação X rende *doze por cento* ao ano, [p=0.2] "
        "com *vinte por cento* de imposto. [p=0.2] A Y rende *dez,* [p=0.2] isenta. [p=0.4] {b}X: [p=0.2] doze vezes "
        "zero vírgula oito, [p=0.2] *nove vírgula seis* líquidos. [p=0.2] Y: [p=0.2] *dez,* [p=0.2] sem desconto. "
        "[p=0.4] {c}*Y rende mais.* [p=0.3] A taxa bruta mais alta [p=0.2] *perdeu* depois do imposto."),
    dict(id="10", block="imposto", text=
        "{t}Tem um atalho? [p=0.3] {a}Tem. [p=0.2] Imposto de vinte por cento [p=0.2] deixa *oitenta* com você. "
        "[p=0.2] Então multiplique a taxa bruta por *zero vírgula oito.* [p=0.4] {b}Com quinze por cento de imposto, "
        "[p=0.2] por *zero vírgula oito cinco.* [p=0.4] {c}Taxa líquida [p=0.2] é igual à bruta [p=0.2] vezes *um "
        "menos a alíquota.*"),

    # ================= BLOCO C: EM REAIS =================
    dict(id="11", block="reais", text=
        "{t}E em reais, [p=0.2] como fica? [p=0.4] {a}Dez mil reais a doze por cento: [p=0.2] o rendimento é *mil e "
        "duzentos.* [p=0.4] {b}O imposto de vinte por cento [p=0.2] *morde só o rendimento:* [p=0.2] *duzentos e "
        "quarenta reais.* [p=0.2] Não dois mil duzentos e quarenta. [p=0.4] {c}Os dez mil já eram seus. [p=0.3] "
        "{d}*Resgate* [p=0.2] é o dinheiro que você tira no fim: [p=0.2] *dez mil novecentos e sessenta.*"),

    # ================= BLOCO D: CUSTOS ESCONDIDOS =================
    dict(id="12", block="escondidos", text=
        "{t}E no empréstimo, [p=0.2] onde o custo se esconde? [p=0.4] {a}Em *tarifas,* [p=0.2] *seguros* [p=0.2] e "
        "*taxas de abertura* [p=0.2] cobradas no ato. [p=0.2] *Tarifa* é um valor fixo cobrado por um serviço. [p=0.4] "
        "{b}O banco entrega cinco mil [p=0.2] e tira cem na porta. [p=0.2] Chegam *quatro mil e novecentos.* [p=0.4] "
        "{c}No fim do mês, [p=0.2] a cobrança é de *cinco mil e duzentos* cheios. [p=0.4] {d}A tarifa no ato *encolhe o "
        "que você recebe,* [p=0.2] mas *não encolhe o que você paga.*"),
    dict(id="13", block="escondidos", text=
        "{t}E como saber o custo de verdade? [p=0.4] {a}O *custo efetivo total,* [p=0.2] o *CET,* [p=0.2] é a taxa "
        "que junta *tudo:* [p=0.2] juros, tarifas e seguros. [p=0.4] {b}E, por lei, [p=0.2] o banco *precisa "
        "informar* esse número."),

    # ================= BLOCO E: A CONTA DO CUSTO EFETIVO =================
    dict(id="14", block="custo", text=
        "{t}Então quanto custou esse empréstimo? [p=0.4] {a}Recebeu *quatro mil e novecentos.* [p=0.2] Pagou *cinco "
        "mil e duzentos.* [p=0.4] {b}Pagou a mais: [p=0.2] *trezentos reais.* [p=0.4] {c}Trezentos dividido por "
        "*quatro mil e novecentos,* [p=0.2] o que você *recebeu:* [p=0.2] cerca de *seis vírgula um por cento* ao "
        "mês. [p=0.4] {d}É a mesma conta da taxa embutida: [p=0.2] a tarifa faz o papel da *entrada.*"),
    dict(id="15", block="custo", text=
        "{t}Tem um atalho aqui também? [p=0.3] {a}Tem. [p=0.2] Divida o que você *pagou* pelo que você *recebeu.* "
        "[p=0.2] Cinco mil e duzentos sobre quatro mil e novecentos: [p=0.2] *um vírgula zero seis um.* [p=0.4] "
        "{b}Tire o um: [p=0.2] *seis vírgula um por cento.* [p=0.4] {c}Repare: [p=0.2] o custo efetivo é sempre "
        "*maior* que a taxa anunciada [p=0.2] quando existe cobrança no ato."),

    # ================= NÓS FAZEMOS =================
    dict(id="16", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}*Dois mil reais* emprestados por um mês, [p=0.2] a *cinco por cento,* [p=0.2] com "
        "*tarifa de cinquenta reais* descontada no ato. [p=0.4] {b}Qual é o custo efetivo? [p=0.3] {c}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="17", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Recebe: [p=0.2] dois mil menos cinquenta, [p=0.2] *mil novecentos e cinquenta.* "
        "[p=0.4] {b}Paga: [p=0.2] dois mil vezes um vírgula zero cinco, [p=0.2] *dois mil e cem.* [p=0.4] {c}A mais: "
        "[p=0.2] *cento e cinquenta.* [p=0.2] Sobre mil novecentos e cinquenta: [p=0.2] cerca de *sete vírgula sete "
        "por cento* no mês. [p=0.3] Bem acima dos cinco anunciados."),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="18", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] compare taxas no mesmo período e já líquidas. "
        "[p=0.5] {b}Dois: [p=0.2] imposto incide sobre o rendimento, não sobre o total. [p=0.5] {c}Três: [p=0.2] "
        "custo efetivo é o que você paga a mais dividido pelo que você recebeu."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="19", block="erros", text=
        "{t}Os três erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] tirar o imposto *do valor total.* [p=0.2] Vinte por "
        "cento de tudo. [p=0.4] {b}Parece certo, [p=0.2] porque o extrato mostra tudo junto. [p=0.4] {c}Mas o imposto "
        "morde *só o rendimento.* [p=0.2] Doze por cento com vinte de imposto [p=0.2] rende *nove vírgula seis* "
        "líquidos."),
    dict(id="20", block="erros", text=
        "{a}Segundo: [p=0.2] comparar taxas de *períodos diferentes* direto. [p=0.4] {b}Parece certo, [p=0.2] porque "
        "doze e meio é um número maior que um. [p=0.4] {c}Mas um por cento ao mês [p=0.2] vira doze vírgula seis oito "
        "ao ano. [p=0.2] *Supera* os doze e meio."),
    dict(id="21", block="erros", text=
        "{a}Terceiro: [p=0.2] *ignorar as tarifas* cobradas no ato. [p=0.4] {b}Parece certo, [p=0.2] porque a taxa "
        "está no contrato, [p=0.2] em letra grande. [p=0.4] {c}Mas a taxa anunciada, sozinha, [p=0.2] *subestima* o "
        "custo. [p=0.2] Divida o que pagou a mais [p=0.2] pelo que recebeu."),

    # ================= QUESTÃO 7 (EU FAÇO) =================
    dict(id="22", block="q7", text=
        "{t}Agora, uma questão no estilo do ENEM [p=0.2] do nosso material de estudo. [p=0.2] Eu faço. [p=0.4] {a}Uma "
        "pessoa tomou *cinco mil reais* emprestados por um mês, [p=0.2] a juros de *quatro por cento* ao mês. "
        "[p=0.2] O banco cobrou uma *tarifa de cem reais,* [p=0.2] descontada na liberação do dinheiro. [p=0.2] O "
        "custo efetivo no mês foi de, aproximadamente: [p=0.4] {qa}A: [p=0.2] dois por cento. [p=0.3] {qb}B: [p=0.2] "
        "quatro. [p=0.3] {qc}C: [p=0.2] quatro vírgula um. [p=0.3] {qd}D: [p=0.2] seis. [p=0.3] {qe}E: [p=0.2] seis "
        "vírgula um por cento."),
    dict(id="23", block="q7", text=
        "{t}É o empréstimo que a gente já fez. [p=0.3] {a}Recebeu quatro mil e novecentos. [p=0.2] Pagou cinco mil e "
        "duzentos. [p=0.4] {b}Trezentos sobre quatro mil e novecentos: [p=0.2] *seis vírgula um.* [p=0.3] {ok}*Letra "
        "E!*"),
    dict(id="24", block="q7", text=
        "{t}Agora, as pegadinhas. [p=0.3] {xb}A B é a *taxa anunciada:* [p=0.2] ignora a tarifa. "
        "[p=0.4] {xa}A A é *só a tarifa,* [p=0.2] cem sobre cinco mil. [p=0.4] {xd}A D soma juros e tarifa, [p=0.2] "
        "mas divide pelos *cinco mil contratados,* [p=0.2] não pelos quatro mil e novecentos recebidos. [p=0.4] "
        "{xc}E a C divide certo, [p=0.2] mas *esquece a tarifa* em cima: [p=0.2] duzentos sobre quatro mil e "
        "novecentos."),

    # ================= QUESTÃO 4 (NÓS FAZEMOS) =================
    dict(id="25", block="q4", text=
        "{t}Próxima: [p=0.2] vamos fazer juntos. [p=0.4] {a}Três bancos, em juros compostos. [p=0.2] O *P* paga *um "
        "por cento ao mês;* [p=0.2] o *Q,* *doze e meio ao ano;* [p=0.2] o *R,* *seis por cento ao semestre.* "
        "[p=0.2] Considere um vírgula zero um elevado a doze [p=0.2] aproximadamente *um vírgula um dois sete.* "
        "[p=0.2] Para aplicar por um ano, a melhor opção é: [p=0.4] {qa}A: [p=0.2] o banco Q, [p=0.2] pois doze e meio "
        "é maior que os doze dos outros dois. [p=0.3] {qb}B: [p=0.2] o banco R, [p=0.2] pois capitaliza duas vezes no "
        "ano. [p=0.3] {qc}C: [p=0.2] qualquer um, [p=0.2] pois as três equivalem a cerca de doze por cento. [p=0.3] "
        "{qd}D: [p=0.2] o banco P, [p=0.2] pois um por cento ao mês equivale a cerca de doze vírgula sete ao ano. "
        "[p=0.3] {qe}E: [p=0.2] o banco Q, [p=0.2] pois uma taxa anual sempre supera uma mensal. [p=0.4] {p}*Pause e "
        "tente.* [p=2.0]"),
    dict(id="26", block="q4", text=
        "{t}Vamos montar a tabela, [p=0.2] tudo *ao ano.* [p=0.4] {a}P: [p=0.2] você já calculou um vírgula zero um "
        "elevado a doze [p=0.2] no episódio um de Taxas Equivalentes. [p=0.2] Agora ele decide entre três bancos: "
        "[p=0.2] *doze vírgula sete.* [p=0.4] {b}Q: [p=0.2] *doze e meio,* [p=0.2] já está no ano. [p=0.4] {c}R: "
        "[p=0.2] dois semestres, [p=0.2] um vírgula zero seis *ao quadrado.* [p=0.2] *Um vírgula um dois três seis:* "
        "[p=0.2] *doze vírgula três seis.* [p=0.4] {d}O maior é o P. [p=0.3] {ok}*Letra D!*"),
    dict(id="27", block="q4", text=
        "{t}Um atalho para o quadrado: [p=0.3] {a}um vírgula zero seis ao quadrado [p=0.2] é *um, [p=0.2] mais doze "
        "centésimos, [p=0.2] mais um pouquinho.* [p=0.4] {b}E as erradas? [p=0.2] {xa}A A [p=0.2] "
        "{xc}e a C usam taxas *proporcionais:* [p=0.2] doze vezes um, [p=0.2] duas vezes seis. [p=0.2] Isso só vale "
        "em juros simples. [p=0.4] {xb}A B tem razão em parte: [p=0.2] R capitaliza, [p=0.2] mas doze vírgula três "
        "seis *ainda perde.* [p=0.4] {xe}E a E generaliza: [p=0.2] quem decide é a taxa equivalente, [p=0.2] não o "
        "período do cartaz."),

    # ================= QUESTÃO 3 (VOCÊ FAZ) =================
    dict(id="28", block="q3", text=
        "{t}Agora é com você. [p=0.4] {a}Uma pessoa vai aplicar *dez mil reais* por um ano. [p=0.2] Opção um: [p=0.2] "
        "*doze por cento,* [p=0.2] com *vinte* de imposto sobre o rendimento. [p=0.2] Opção dois: [p=0.2] *dez por "
        "cento,* isenta. [p=0.2] Opção três: [p=0.2] *onze por cento,* [p=0.2] com *quinze* de imposto. [p=0.2] A de "
        "maior rendimento líquido, e o valor dele, são: [p=0.4] {qa}A: [p=0.2] um, com novecentos e sessenta. [p=0.3] "
        "{qb}B: [p=0.2] dois, com mil. [p=0.3] {qc}C: [p=0.2] um, com mil e duzentos. [p=0.3] {qd}D: [p=0.2] três, com "
        "novecentos e trinta e cinco. [p=0.3] {qe}E: [p=0.2] três, com mil e cem. [p=0.4] {p}*Pause o vídeo e resolva "
        "sozinho.* [p=2.5]"),
    dict(id="29", block="q3", text=
        "{t}Vamos conferir, [p=0.2] em reais e já líquido. [p=0.4] {a}Um: [p=0.2] mil e duzentos vezes zero vírgula "
        "oito, [p=0.2] *novecentos e sessenta.* [p=0.4] {b}Dois: [p=0.2] *mil,* [p=0.2] sem imposto. [p=0.4] {c}Três: "
        "[p=0.2] mil e cem vezes zero vírgula oito cinco, [p=0.2] *novecentos e trinta e cinco.* [p=0.4] {d}A menor "
        "taxa bruta [p=0.2] deu o *maior líquido.* [p=0.3] {ok}*Letra B!*"),
    dict(id="30", block="q3", text=
        "{t}E as armadilhas? [p=0.3] {xc}A C [p=0.2] {xe}e a E usam o rendimento *bruto:* [p=0.2] esqueceram o "
        "imposto. [p=0.4] {xa}A A [p=0.2] {xd}e a D calculam *certo* o líquido de um e de três. [p=0.2] Só que os dois "
        "ficam *abaixo* dos mil da opção dois."),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="31", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] compare taxas no mesmo período e já líquidas. "
        "[p=0.5] {b}Dois: [p=0.2] imposto incide sobre o rendimento, não sobre o total. [p=0.5] {c}Três: [p=0.2] "
        "custo efetivo é o que você paga a mais dividido pelo que você recebeu."),

    # ================= PONTE E CTA =================
    dict(id="32", block="ponte", text=
        "{a}Uma fábrica tem *seis mil reais* de custo fixo por mês, [p=0.2] e cada peça deixa *vinte reais.* [p=0.4] "
        "{b}Quantas peças ela precisa vender [p=0.2] só para *não ter prejuízo?* [p=0.4] {c}Próximo episódio."),
    dict(id="33", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já olhou o CET de um empréstimo [p=0.2] antes de assinar? "
        "[p=0.5] {anki}E tem mais: [p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do "
        "ENEM* no *Anki,* [p=0.2] o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. "
        "[p=0.5] {bye}Bons estudos, e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
