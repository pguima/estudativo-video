# Estudativo · MAT-FIN-012 — Tabelas SAC e Price (Matemática · Matemática Financeira).
# Habilidade: montar a primeira linha de um financiamento SAC e dizer por que a Price paga mais juros.
# Pré-requisitos: MAT-FIN-001 (juros simples), MAT-FIN-004 (juros compostos). Próxima: MAT-FIN-013.
# Questão inédita, criada para esta aula. A prestação da Price (R$ 1.113,27) vem pronta: a fórmula é assunto de outra aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Tabelas SAC e Price"

VOZ = dict(
    tags=["alegre", "curiosa", "amigavel"],
    prompt=("Narre como um professor de cursinho popular apaixonado pelo que ensina, conversando de perto com um aluno "
            "que passou anos sem estudar: voz masculina, grave, calorosa, acolhedora e MUITO expressiva, com bastante "
            "variação de entonação e emoção verdadeira. Sorria na voz. Faça as perguntas com curiosidade genuína; mostre "
            "surpresa no erro, entusiasmo no atalho e dê ênfase forte às palavras-chave. Ritmo tranquilo, com pausas "
            "naturais entre as ideias. Leia exatamente o texto, sem repetir nem acrescentar nada."),
)

SCENES = [
    # gancho
    dict(id="s01", block="gancho", text="{a}Dois financiamentos de dez mil reais. [p=0.2] {b}Mesma taxa, mesmo prazo. [p=0.3] No fim, um deles cobrou {c}mais juros. [p=0.2] Qual, e por quê?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai montar a primeira linha de um financiamento e saber qual sistema cobra mais juros, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de uma coisa: [p=0.2] {a}os juros de um mês são a taxa vezes o valor devido. [p=0.2] Dois por cento de dez mil dá {b}duzentos reais. [p=0.3] Se faltar, procure no canal."),
    # nomes
    dict(id="s04", block="nomes", text="Num financiamento, cada parcela, a {a}prestação, tem duas partes. [p=0.2] {b}Os juros: o aluguel do dinheiro naquele mês. [p=0.2] E a {c}amortização: o pedaço que de fato abate a dívida."),
    dict(id="s05", block="nomes", text="O que você ainda deve se chama {a}saldo devedor. [p=0.2] E aqui está a regra de ouro: [p=0.2] {b}os juros de cada mês valem sobre o saldo devedor, e não sobre o valor que você pegou."),
    # SAC
    dict(id="s06", block="sac", text="Primeiro sistema: a {a}SAC, sistema de amortização constante. [p=0.2] Constante quer dizer {b}igual todo mês. [p=0.3] Dez mil reais em dez meses: [p=0.2] {c}dez mil dividido por dez dá mil reais de amortização por mês."),
    dict(id="s07", block="sac", text="Monte a primeira linha, com taxa de {a}dois por cento ao mês. [p=0.2] Saldo devedor: {b}dez mil. [p=0.2] Juros: dois por cento de dez mil dá {c}duzentos. [p=0.2] Amortização: {d}mil. [p=0.2] Prestação: mil mais duzentos dá {e}mil e duzentos reais. [p=0.2] Saldo que fica: {f}nove mil."),
    dict(id="s08", block="sac", text="No segundo mês, os juros valem sobre nove mil: {a}cento e oitenta. [p=0.2] Prestação: {b}mil cento e oitenta. [p=0.3] Na SAC, {c}a prestação começa alta e vai caindo."),
    # Price
    dict(id="s09", block="price", text="Segundo sistema: a {a}tabela Price. [p=0.2] Nela, {b}todas as prestações são iguais. [p=0.2] A conta do valor da prestação é assunto de outra aula, [p=0.2] e a prova costuma dar esse valor pronto. [p=0.2] Aqui, cerca de {c}mil cento e treze reais por mês."),
    dict(id="s10", block="price", text="Primeira linha da Price. [p=0.2] Juros: os mesmos {a}duzentos, porque o saldo também é dez mil. [p=0.2] Amortização: o que sobra da prestação, {b}cerca de mil cento e treze menos duzentos dá novecentos e treze. [p=0.2] Saldo que fica: {c}cerca de nove mil e oitenta e sete."),
    dict(id="s11", block="porque", text="Compare o saldo depois do primeiro mês. [p=0.2] Na SAC, {a}nove mil. [p=0.2] Na Price, {b}cerca de nove mil e oitenta e sete. [p=0.3] Na Price, a dívida {c}cai mais devagar no começo. [p=0.2] E como os juros valem sobre o saldo, {d}você paga juros sobre uma dívida maior, por mais tempo."),
    dict(id="s12", block="porque", text="No total, a SAC cobra {a}mil e cem reais de juros: [p=0.2] são os juros de cada mês, de duzentos caindo até vinte, somados. [p=0.3] Na Price, as dez prestações de cerca de mil cento e treze somam cerca de onze mil cento e trinta. [p=0.2] Tirando os dez mil emprestados, {b}cerca de mil cento e trinta de juros."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é calcular os juros {a}sempre sobre o valor que você pegou. [p=0.2] No segundo mês da SAC, a pessoa faz dois por cento de dez mil, e acha {b}duzentos de novo. [p=0.3] Mas você já devolveu mil. [p=0.2] Os juros valem sobre {c}nove mil: cento e oitenta."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho da SAC. [p=0.2] Como o saldo cai mil por mês, {a}os juros caem dois por cento de mil: vinte reais por mês. [p=0.3] Então {b}cada prestação é vinte reais menor que a anterior. [p=0.2] A décima: {c}mil e duzentos menos nove vezes vinte, mil e vinte reais."),
    dict(id="s15", block="atalho", text="Funciona porque {a}a amortização é sempre a mesma. [p=0.2] Não serve na Price, em que a amortização {b}muda todo mês."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Um financiamento de {a}sessenta mil reais, pela SAC, em {b}sessenta meses, a {c}um por cento ao mês. [p=0.3] {d}Monte a primeira linha e diga o valor da segunda prestação."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Amortização: {a}sessenta mil dividido por sessenta dá mil reais. [p=0.2] Juros: um por cento de sessenta mil dá {b}seiscentos. [p=0.2] Prestação: {c}mil e seiscentos. [p=0.2] Saldo que fica: {d}cinquenta e nove mil."),
    dict(id="s19", block="resposta", text="Para a segunda, o atalho: os juros caem {a}um por cento de mil dá dez reais. [p=0.2] Segunda prestação: {b}mil quinhentos e noventa reais. [p=0.2] Confira: um por cento de cinquenta e nove mil é quinhentos e noventa, [p=0.2] {c}mais mil de amortização."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}os juros valem sempre sobre o saldo devedor. [p=0.2] A Price cobra mais porque {b}amortiza menos no começo."),
    dict(id="s21", block="fim", text="Na próxima aula, você vê o outro lado: o dinheiro que rende. [p=0.2] E aprende a descontar {a}o imposto, que vale só sobre o rendimento. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
