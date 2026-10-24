# Roteiro — Comparação de Propostas e Tomada de Decisão, Episódio 1 de 5: a regra de ouro, comparar na mesma data
#   (à vista ou a prazo?)
# Base: Estudos/Enem/estudos/01-matematica/18-comparacao-propostas-tomada-decisao.html — seções 02 e 03
#   + Questões 8 e 2 (seção 12).
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Analogias âncora (do prompt):
#   MOEDAS DE PAÍSES DIFERENTES (série de Empréstimos): a DATA FOCAL é o ponto de encontro onde todos fazem o câmbio.
#   TAXA DE OPORTUNIDADE = o que o seu dinheiro faria se ficasse com você (aplicação, ou juro do empréstimo que pegaria).
#   LOJA × APLICAÇÃO: se a loja cobra mais pelo tempo do que a aplicação rende, pague à vista; se cobra menos, parcele.
# Frases do usuário mantidas IGUAIS: gancho, as 3 frases-chave e a ponte. A promessa começa com "Ao final desta aula",
#   como nos outros episódios (o resto da frase é o do prompt).
# Contas (conferidas em Python): 10.000 · 1,21 = 12.100; 11.000 · 1,1 = 12.100; na data zero, 11.000 ÷ 1,1 = 12.100 ÷ 1,21
#   = 10.000. Televisor: 1/1,02 ≈ 0,980; 1/1,02² ≈ 0,961 → 1.000 + 980 + 961 = 2.941 > 2.900 → à vista.
#   NOSSO (bloco e, conferido): taxa embutida do televisor ≈ 3,5% ao mês (1.000/(1+i) + 1.000/(1+i)² = 1.900 → i ≈ 3,49%),
#   maior que os 2% → à vista; com aplicação a 5% ao mês: 1.000 + 952 + 907 = 2.859 < 2.900 → parcelar (a decisão inverte).
#   NOSSO (bloco f): "3.000 à vista ou 3 × 1.000 sem juros", a 2% → parcelado vale ≈ 2.941 hoje < 3.000 → parcelar.
#   Nós fazemos (prompt): 1.050 ÷ 1,03 ≈ 1.019,42 > 1.000 → à vista; taxa 50 ÷ 1.000 = 5% > 3% → à vista.
#   Atalho (NOSSO, verde): o fator de desconto × parcela ≈ "tirar 2%" (1.000 → 980) e a parcela do ATO não viaja.
# QUESTÃO 8 (eu faço; erradas do material, que estão certas): na data de 2 anos, as três valem 12.100 → E.
#   C = compara valores nominais; A = regra geral sem conta; B = decide sem conta; D = erra a conta de uma opção
#   (deixa 11.000 sem levar à data de 2 anos).
# QUESTÃO 2 (você faz; erradas do material, certas): à vista 950; financiado 450; taxa 50 ÷ 450 ≈ 11,1% > 1% → A.
#   D = decisão certa com a taxa errada (5% é o desconto sobre o preço cheio); B = acredita no "sem juros";
#   C = compara R$ 5,00 de rendimento com R$ 50,00 de desconto; E = ignora que o à vista é R$ 950,00.
# Frases-chave (meio e fim, idênticas): 1. Só se comparam valores na mesma data. 2. A taxa que decide é a do seu
#   dinheiro: a taxa de oportunidade. 3. Se a loja cobra mais do que a aplicação rende, pague à vista.
# Cores: azul = definição · roxo = regra/fórmula · amarelo = armadilha · verde = atalho/dica · vermelho = erro.

TITULO = ("À vista ou parcelado? A regra de ouro para comparar propostas · Matemática ENEM, Comparação de propostas "
          "episódio 1")

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
        "{a}*Dez mil reais* hoje, [p=0.2] *onze mil* daqui a um ano [p=0.2] ou *doze mil e cem* daqui a dois anos. "
        "[p=0.4] {b}Qual você escolhe? [p=0.5] {c}Se você respondeu *o maior,* [p=0.2] caiu na pegadinha. [p=0.4] "
        "{d}Com o dinheiro rendendo *dez por cento ao ano,* [p=0.2] os três valem *exatamente o mesmo.*"),
    dict(id="02", block="promessa", text=
        "{a}Ao final desta aula, [p=0.2] você vai decidir entre *pagar à vista ou parcelar,* [p=0.3] {b}e entre "
        "*valores em datas diferentes,* [p=0.3] {c}sem cair no *maior número.*"),
    dict(id="03", block="prereq", text=
        "{t}Um lembrete rápido, [p=0.2] da série de Empréstimos. [p=0.3] {a}Para levar um valor ao *futuro,* [p=0.2] "
        "*multiplique* por um mais i, [p=0.2] elevado ao número de períodos. [p=0.2] Para trazer ao *presente,* "
        "[p=0.2] *divida.* [p=0.2] E cada parcela viaja pelo *seu* prazo. [p=0.4] {b}E a *taxa embutida:* [p=0.2] "
        "juros divididos pelo *valor financiado,* [p=0.2] o que você ficou devendo."),

    # ================= CONCRETO =================
    dict(id="04", block="concreto", text=
        "{a}Uma loja anuncia um televisor: [p=0.2] *dois mil e novecentos reais à vista,* [p=0.2] ou *três vezes de "
        "mil.* [p=0.4] {b}Cada jeito de pagar [p=0.2] é uma *proposta:* [p=0.2] uma oferta, com valores e datas. "
        "[p=0.4] {c}E você tem o dinheiro guardado, [p=0.2] rendendo *dois por cento ao mês.* [p=0.2] Qual proposta "
        "é melhor?"),
    dict(id="05", block="concreto", text=
        "{t}Outra cena. [p=0.3] {a}Você ganhou um sorteio. [p=0.2] Pode receber o prêmio *hoje* [p=0.2] ou *daqui a "
        "dois anos,* [p=0.2] um pouco maior. [p=0.4] {b}As duas perguntas [p=0.2] têm a *mesma* regra por trás."),

    # ================= BLOCO A: A REGRA DE OURO =================
    dict(id="06", block="regra", text=
        "{t}Dá para comparar dez mil de hoje [p=0.2] com doze mil e cem de daqui a dois anos? [p=0.5] {a}Do jeito "
        "que estão, *não.* [p=0.4] {b}Valores em datas diferentes [p=0.2] são *moedas de países diferentes.* [p=0.2] "
        "Não se somam, [p=0.2] e também *não se comparam.* [p=0.4] {c}Primeiro, [p=0.2] todo mundo faz o *câmbio* "
        "[p=0.2] para a mesma data."),
    dict(id="07", block="regra", text=
        "{t}Essa data tem nome: [p=0.2] *data focal.* [p=0.4] {a}É o *ponto de encontro* [p=0.2] onde você leva "
        "todos os valores [p=0.2] antes de comparar. [p=0.4] {b}Lá, cada valor vira o seu *valor equivalente:* "
        "[p=0.2] quanto ele vale naquela data. [p=0.4] {c}Finque uma *bandeirinha* na data focal. [p=0.2] Leve tudo "
        "até ela. [p=0.2] *Só então compare.*"),

    # ================= BLOCO B: QUALQUER DATA FOCAL =================
    dict(id="08", block="focal", text=
        "{t}E qual data escolher? [p=0.4] {a}*Qualquer uma.* [p=0.2] Veja o sorteio, [p=0.2] a dez por cento ao ano. "
        "[p=0.4] {b}Com a bandeirinha *hoje:* [p=0.2] onze mil, dividido por um vírgula um, [p=0.2] é *dez mil.* "
        "[p=0.2] Doze mil e cem, [p=0.2] dividido por um vírgula vinte e um, [p=0.2] *dez mil.* [p=0.4] {c}Com a "
        "bandeirinha *daqui a dois anos:* [p=0.2] os três viram *doze mil e cem.*"),
    dict(id="09", block="focal", text=
        "{t}Mudou a data, [p=0.2] mudou a conclusão? [p=0.4] {a}*Não.* [p=0.2] Trocar de data [p=0.2] multiplica "
        "*todos* os valores [p=0.2] pelo *mesmo fator.* [p=0.4] {b}Quem era maior, [p=0.2] continua maior. [p=0.2] "
        "{c}Então escolha a data [p=0.2] que deixa a conta *mais "
        "simples.*"),

    # ================= BLOCO C: TAXA DE OPORTUNIDADE =================
    dict(id="10", block="taxa", text=
        "{t}E qual taxa usar no câmbio? [p=0.4] {a}A *taxa de oportunidade:* [p=0.2] o que o seu dinheiro faria [p=0.2] "
        "*se ficasse com você.* [p=0.4] {b}Se você tem o dinheiro, [p=0.2] é o quanto ele *renderia* na aplicação. "
        "[p=0.4] {c}Se não tem, [p=0.2] é o *juro* que você pagaria [p=0.2] para pegar emprestado."),
    dict(id="11", block="taxa", text=
        "{t}E de onde vem esse número? [p=0.4] {a}Do *enunciado.* [p=0.2] Ele *sempre* informa. [p=0.4] {b}Sem essa "
        "taxa, [p=0.2] a comparação *não está definida.* [p=0.4] "
        "{c}Por isso, [p=0.2] antes de qualquer conta, [p=0.2] *grife a taxa* no enunciado."),

    # ================= BLOCO D: À VISTA OU A PRAZO =================
    dict(id="12", block="tv", text=
        "{t}Voltando ao televisor. [p=0.3] {a}Linha do tempo: [p=0.2] uma parcela de mil *no ato,* [p=0.2] outra em "
        "*trinta dias,* [p=0.2] outra em *sessenta.* [p=0.4] {b}Bandeirinha no dia da compra: [p=0.2] *hoje.* "
        "[p=0.4] {c}Para trazer cada parcela, [p=0.2] use o *fator de desconto:* [p=0.2] um dividido pelo fator. "
        "[p=0.2] Um mês a dois por cento: [p=0.2] *zero vírgula novecentos e oitenta.* [p=0.2] Dois meses: [p=0.2] "
        "*zero vírgula novecentos e sessenta e um.*"),
    dict(id="13", block="tv", text=
        "{t}Agora, as moedinhas viajam. [p=0.3] {a}A do ato [p=0.2] *já está hoje:* [p=0.2] mil. [p=0.4] {b}A de "
        "trinta dias [p=0.2] encolhe para *novecentos e oitenta.* [p=0.2] A de sessenta, [p=0.2] para *novecentos e "
        "sessenta e um.* [p=0.4] {c}Somando: [p=0.2] *dois mil, novecentos e quarenta e um.* [p=0.2] Esse é o *valor "
        "hoje do parcelado.* [p=0.4] {d}Ele é *maior* que os dois mil e novecentos à vista. [p=0.2] *Pague à vista.*"),
    dict(id="14", block="tv", text=
        "{t}Um atalho para essa viagem. [p=0.3] {a}Multiplicar mil por zero vírgula novecentos e oitenta [p=0.2] é "
        "*tirar dois por cento:* [p=0.2] vinte reais. [p=0.4] {b}E a parcela *do ato* [p=0.2] nunca viaja: [p=0.2] ela "
        "já nasce na data focal. [p=0.4] {c}Conferência: [p=0.2] o valor hoje do parcelado [p=0.2] é sempre *menor* "
        "que a soma das parcelas."),

    # ================= BLOCO E: PELA TAXA EMBUTIDA =================
    dict(id="15", block="embutida", text=
        "{t}Existe outro caminho? [p=0.4] {a}Existe: [p=0.2] comparar *taxas.* [p=0.2] Pense numa disputa: [p=0.2] "
        "*loja contra aplicação.* [p=0.4] {b}Nesse parcelado, [p=0.2] a loja cobra uns *três e meio por cento ao "
        "mês* [p=0.2] pelo tempo. [p=0.2] A aplicação rende *dois.* [p=0.4] {c}A loja cobra *mais* do que a aplicação "
        "rende: [p=0.2] *pague à vista.* [p=0.2] Mesma decisão."),
    dict(id="16", block="embutida", text=
        "{t}E se a aplicação rendesse bem mais? [p=0.4] {a}Digamos, [p=0.2] *cinco por cento ao mês.* [p=0.4] "
        "{b}Aí as parcelas encolhem mais: [p=0.2] mil, [p=0.2] novecentos e cinquenta e dois, [p=0.2] novecentos e "
        "sete. [p=0.2] Total: [p=0.2] uns *dois mil, oitocentos e cinquenta e nove.* [p=0.4] {c}Abaixo dos dois mil "
        "e novecentos. [p=0.2] Agora a loja cobra *menos:* [p=0.2] *parcele* [p=0.2] e deixe o dinheiro trabalhando."),

    # ================= BLOCO F: "SEM JUROS" =================
    dict(id="17", block="semjuros", text=
        "{t}E o famoso *sem juros?* [p=0.4] {a}Imagine: [p=0.2] *três mil à vista* [p=0.2] ou *três de mil,* [p=0.2] "
        "sem desconto nenhum. [p=0.2] Tanto faz? [p=0.4] {b}*Não.* [p=0.2] A dois por cento, [p=0.2] as três de mil "
        "valem hoje uns *dois mil, novecentos e quarenta e um.* [p=0.4] {c}Menos que os três mil. [p=0.2] Você paga o "
        "mesmo valor, [p=0.2] só que *mais tarde,* [p=0.2] e o dinheiro rende enquanto isso. [p=0.2] *Parcele.*"),

    # ================= NÓS FAZEMOS =================
    dict(id="18", block="exercicio", text=
        "{t}Sua vez. [p=0.3] {a}Um produto custa *mil reais à vista* [p=0.2] ou *mil e cinquenta* daqui a um mês. "
        "[p=0.2] Seu dinheiro rende *três por cento ao mês.* [p=0.2] O que compensa? [p=0.3] {b}*Pause e tente.* "
        "[p=2.0]"),
    dict(id="19", block="exercicio", text=
        "{t}Vamos juntos. [p=0.3] {a}Bandeirinha *hoje.* [p=0.2] Mil e cinquenta, [p=0.2] dividido por um vírgula "
        "zero três: [p=0.2] uns *mil e dezenove e quarenta e dois.* [p=0.2] Mais que os mil à vista. [p=0.4] {b}Pelo "
        "caminho da taxa: [p=0.2] a loja cobra cinquenta sobre mil, [p=0.2] *cinco por cento ao mês.* [p=0.2] A "
        "aplicação rende três. [p=0.4] {c}Os dois caminhos dizem o mesmo: [p=0.2] *pague à vista.*"),

    # ================= MINI-RECAPITULAÇÃO =================
    dict(id="20", block="recap", text=
        "{t}Vamos guardar em três frases. [p=0.5] {a}Um: [p=0.2] só se comparam valores na mesma data. [p=0.5] "
        "{b}Dois: [p=0.2] a taxa que decide é a do seu dinheiro: [p=0.2] a taxa de oportunidade. [p=0.5] {c}Três: "
        "[p=0.2] se a loja cobra mais do que a aplicação rende, [p=0.2] pague à vista."),

    # ================= ERROS CLÁSSICOS =================
    dict(id="21", block="erros", text=
        "{t}Agora, os dois erros clássicos. [p=0.4] {a}Primeiro: [p=0.2] *comparar valores de datas diferentes.* "
        "[p=0.4] {b}Parece certo, [p=0.2] porque são todos em reais. [p=0.4] {c}Mas são reais de *datas* "
        "diferentes. [p=0.2] A dez por cento ao ano, [p=0.2] dez mil hoje e doze mil e cem em dois anos [p=0.2] *se "
        "equivalem.*"),
    dict(id="22", block="erros", text=
        "{a}Segundo: [p=0.2] *escolher pelo maior número.* [p=0.4] {b}Parece certo, [p=0.2] porque mais dinheiro é "
        "melhor. [p=0.4] {c}Mas o maior número [p=0.2] costuma estar na data *mais distante,* [p=0.2] e lá ele vale "
        "menos. [p=0.2] Primeiro a data focal, [p=0.2] depois a comparação."),

    # ================= QUESTÃO 8 (EU FAÇO) =================
    dict(id="23", block="q8", text=
        "{t}Agora, questões no estilo do ENEM. [p=0.4] {a}O ganhador de um sorteio pode escolher entre três formas de "
        "receber o prêmio: [p=0.2] *dez mil reais hoje;* [p=0.2] *onze mil* daqui a um ano; [p=0.2] ou *doze mil e "
        "cem* daqui a dois anos. [p=0.2] Ele aplicaria o dinheiro a *dez por cento ao ano,* [p=0.2] no regime de "
        "juros compostos. [p=0.2] Do ponto de vista financeiro: [p=0.4] {qa}A: [p=0.2] receber hoje é melhor, "
        "[p=0.2] pois dinheiro disponível hoje sempre vale mais. [p=0.3] {qb}B: [p=0.2] receber em um ano é melhor, "
        "[p=0.2] pois evita esperar dois anos e paga mil reais a mais. [p=0.3] {qc}C: [p=0.2] receber em dois anos é "
        "melhor, [p=0.2] pois é o maior valor. [p=0.3] {qd}D: [p=0.2] receber hoje e receber em dois anos são "
        "equivalentes, [p=0.2] mas receber em um ano é pior. [p=0.3] {qe}E: [p=0.2] as três opções são "
        "equivalentes."),
    dict(id="24", block="q8", text=
        "{t}Eu resolvo. [p=0.3] {a}Na série de Juros Compostos, [p=0.2] você viu que doze mil e cem daqui a dois anos "
        "[p=0.2] valem dez mil hoje. [p=0.2] Agora a pergunta é de *decisão.* [p=0.4] {b}Bandeirinha em *dois anos.* "
        "[p=0.2] Os dez mil viajam dois anos: [p=0.2] vezes um vírgula vinte e um, [p=0.2] *doze mil e cem.* [p=0.4] "
        "{c}Os onze mil viajam um ano: [p=0.2] vezes um vírgula um, [p=0.2] *doze mil e cem.* [p=0.2] E o terceiro "
        "*já está lá.* [p=0.4] {d}Três valores iguais na mesma data. [p=0.3] {ok}*Letra E!*"),
    dict(id="25", block="q8", text=
        "{t}E as outras? [p=0.3] {xc}A C compara os números *sem levar à mesma data.* [p=0.4] {xa}A A usa uma regra "
        "geral, [p=0.2] *sem conta;* [p=0.2] aqui o tempo foi compensado na medida certa. [p=0.4] {xb}A B também "
        "decide *sem fazer conta.* [p=0.4] {xd}E a D *erra a conta* de uma opção: [p=0.2] deixa os onze mil parados, "
        "[p=0.2] sem levar até os dois anos."),

    # ================= QUESTÃO 2 (VOCÊ FAZ) =================
    dict(id="26", block="q2", text=
        "{t}Agora é com você. [p=0.3] {a}Uma loja vende um produto por *mil reais* em *duas parcelas de quinhentos,* "
        "[p=0.2] uma no ato e outra em trinta dias, [p=0.2] ou com *cinco por cento de desconto à vista.* [p=0.2] Um "
        "cliente tem o dinheiro aplicado [p=0.2] num investimento que rende *um por cento ao mês.* [p=0.2] A decisão "
        "mais vantajosa para ele é: [p=0.4] {qa}A: [p=0.2] pagar à vista, [p=0.2] pois o parcelamento embute juros "
        "de cerca de onze vírgula um por cento ao mês, [p=0.2] bem acima do um por cento da aplicação. [p=0.3] "
        "{qb}B: [p=0.2] parcelar, [p=0.2] pois o anúncio não menciona juros [p=0.2] e o dinheiro continua rendendo. "
        "[p=0.3] {qc}C: [p=0.2] parcelar, [p=0.2] pois quinhentos reais aplicados por um mês rendem cinco reais, "
        "[p=0.2] o que compensa o desconto. [p=0.3] {qd}D: [p=0.2] pagar à vista, [p=0.2] pois o parcelamento "
        "embute juros de cinco por cento ao mês. [p=0.3] {qe}E: [p=0.2] escolher qualquer opção, [p=0.2] pois o "
        "total pago é de mil reais nos dois casos. [p=0.4] {p}*Pause o vídeo e resolva sozinho.* [p=2.5]"),
    dict(id="27", block="q2", text=
        "{t}Confira. [p=0.3] {a}À vista: [p=0.2] mil menos cinco por cento, [p=0.2] *novecentos e cinquenta.* "
        "[p=0.4] {b}No parcelado, [p=0.2] a primeira parcela é *entrada.* [p=0.2] Fica financiado novecentos e "
        "cinquenta menos quinhentos: [p=0.2] *quatrocentos e cinquenta.* [p=0.4] {c}Em trinta dias você paga "
        "quinhentos. [p=0.2] Juros de cinquenta, [p=0.2] sobre quatrocentos e cinquenta: [p=0.2] uns *onze vírgula "
        "um por cento ao mês.* [p=0.4] {d}Loja: onze. [p=0.2] Aplicação: um. [p=0.2] Pague à vista. [p=0.3] {ok}*Letra "
        "A!*"),
    dict(id="28", block="q2", text=
        "{t}E as armadilhas? [p=0.3] {xd}A D chega à decisão certa [p=0.2] com a *taxa errada:* [p=0.2] cinco por "
        "cento é o desconto sobre o preço cheio, [p=0.2] não a taxa sobre o que foi financiado. [p=0.4] {xc}A C "
        "compara *cinco reais* de rendimento [p=0.2] com *cinquenta* de desconto. [p=0.4] {xb}A B acredita no *sem "
        "juros* do anúncio. [p=0.4] {xe}E a E esquece que o preço à vista [p=0.2] é *novecentos e cinquenta.*"),

    # ================= RECAPITULAÇÃO FINAL =================
    dict(id="29", block="recap", text=
        "{t}Para fechar, as mesmas três frases. [p=0.5] {a}Um: [p=0.2] só se comparam valores na mesma data. [p=0.5] "
        "{b}Dois: [p=0.2] a taxa que decide é a do seu dinheiro: [p=0.2] a taxa de oportunidade. [p=0.5] {c}Três: "
        "[p=0.2] se a loja cobra mais do que a aplicação rende, [p=0.2] pague à vista."),

    # ================= PONTE E CTA =================
    dict(id="30", block="ponte", text=
        "{a}Plano A: [p=0.2] *cinquenta reais* mais *cinquenta centavos* por minuto. [p=0.4] {b}Plano B: [p=0.2] "
        "*oitenta reais* mais *vinte centavos* por minuto. [p=0.4] {c}Qual é melhor? [p=0.3] A resposta certa começa "
        "com *depende.* [p=0.3] Próximo episódio."),
    dict(id="31", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no *Estudativo* [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar *toda a Matemática do ENEM do zero.* [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você costuma pagar à vista ou parcelar? [p=0.5] {anki}E tem mais: "
        "[p=0.2] na *descrição* deste vídeo tem um link para você adquirir os *flashcards do ENEM* no *Anki,* [p=0.2] "
        "o aplicativo de revisão, [p=0.2] para revisar tudo isso em poucos minutos por dia. [p=0.5] {bye}Bons estudos, "
        "e *até a próxima aula* aqui no Estudativo. [p=1.5]"),
]
