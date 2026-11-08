# Estudativo · MAT-EXP-011 — Achar o expoente: equação exponencial com log (Matemática · Exponencial e Logaritmo).
# Habilidade: descobrir que 1,1ᵗ = 2 dá t ≈ 7,3 e em quantos meses uma aplicação dobra, fechando o que ficou pendente em juros compostos.
# Pré-requisitos: MAT-EXP-010 (log 2, log 3 e mudança de base), MAT-FIN-004 (juros compostos), MAT-FRA-018 (dividir por decimal). Próxima: MAT-EXP-012.
# Valores dados como no enunciado: log 2 ≈ 0,30, log 1,1 ≈ 0,041, log 1,02 ≈ 0,0086, log 3 ≈ 0,48, log 1,03 ≈ 0,013.
# MAT-FIN-006 (regra do 72) fora da ficha: não citada. Questão inédita, criada para esta aula; taxa de 3% ao mês dita como exemplo.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Achar o expoente: equação exponencial com logaritmo"

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
    dict(id="s01", block="gancho", text="{a}Mil reais, a dez por cento ao ano, em juros compostos. [p=0.2] {b}Em quantos anos viram dois mil? [p=0.3] Com potências, você só chega perto. [p=0.2] {c}Um vírgula um elevado a sete dá cerca de um vírgula noventa e cinco. [p=0.2] {d}Elevado a oito, dá cerca de dois vírgula catorze. [p=0.3] Dobra entre o sétimo e o oitavo ano, mas onde?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha esse expoente com logaritmo, [p=0.2] e ele {b}dá cerca de sete vírgula três anos. [p=0.3] E leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de três coisas: [p=0.2] {a}a fórmula dos juros compostos, montante igual a capital vezes o fator elevado ao tempo, [p=0.2] {b}o expoente que sai do logaritmo multiplicando, [p=0.2] e {c}dividir por um número com vírgula. [p=0.3] Se faltar alguma, procure no canal."),
    # montar e isolar
    dict(id="s04", block="isolar", text="Monte a equação: {a}mil vezes um vírgula um elevado a tê igual a dois mil. [p=0.3] Primeiro, {b}isole a potência: divida cada lado por mil. [p=0.2] Fica {c}um vírgula um elevado a tê igual a dois."),
    dict(id="s05", block="isolar", text="Dá para igualar as bases? [p=0.2] {a}Não: dois não é potência de um vírgula um. [p=0.3] A saída é {b}tirar o logaritmo na base dez de cada lado. [p=0.2] Números iguais têm logaritmos iguais."),
    dict(id="s06", block="isolar", text="O expoente sai multiplicando: [p=0.2] {a}tê vezes logaritmo de um vírgula um igual a logaritmo de dois. [p=0.3] Divida pelo logaritmo de um vírgula um: [p=0.2] {b}tê igual a logaritmo de dois dividido por logaritmo de um vírgula um. [p=0.2] O tê {c}desceu do expoente."),
    # conta
    dict(id="s07", block="conta", text="O logaritmo de dois é cerca de {a}zero vírgula trinta. [p=0.2] O de um vírgula um não sai de dois e três, [p=0.2] então a prova dá o valor, {b}que é cerca de zero vírgula zero quarenta e um. [p=0.3] {c}Zero vírgula trinta dividido por zero vírgula zero quarenta e um. [p=0.2] Ande três casas: {d}trezentos dividido por quarenta e um {e}dá cerca de sete vírgula três anos."),
    dict(id="s08", block="conta", text="Bate com as potências: {a}entre sete e oito. [p=0.2] O logaritmo mostra {b}o ponto certo dentro desse intervalo."),
    # método
    dict(id="s09", block="metodo", text="O método tem {a}três passos. [p=0.2] {b}Isole a potência. [p=0.2] {c}Tire o logaritmo de cada lado, e o expoente sai multiplicando. [p=0.2] {d}Divida."),
    # em meses
    dict(id="s10", block="meses", text="E em meses? [p=0.2] Uma aplicação rende {a}dois por cento ao mês. [p=0.2] Dobrar é {b}um vírgula zero dois elevado a tê igual a dois, com tê em meses. [p=0.3] A prova dá {c}o logaritmo de um vírgula zero dois, que é cerca de zero vírgula zero zero oitenta e seis."),
    dict(id="s11", block="meses", text="{a}Tê igual a zero vírgula trinta dividido por zero vírgula zero zero oitenta e seis. [p=0.2] Ande quatro casas: {b}três mil dividido por oitenta e seis {c}dá cerca de trinta e cinco meses. [p=0.2] Quase três anos."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}tratar o expoente como multiplicação. [p=0.2] A pessoa lê um vírgula um vezes tê igual a dois, [p=0.2] e faz {b}dois dividido por um vírgula um, que dá cerca de um vírgula oito anos."),
    dict(id="s13", block="erro", text="Confira na fórmula: em dois anos, {a}mil reais viram só mil duzentos e dez. [p=0.2] Em menos de dois anos, menos ainda. [p=0.2] Longe de dois mil. [p=0.3] O tê está {b}no expoente, e sai de lá com logaritmo."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}o capital não importa. [p=0.2] Para dobrar, o de cima é sempre {b}o logaritmo de dois. [p=0.2] Para triplicar, {c}o logaritmo de três. [p=0.3] Só muda o de baixo: {d}o logaritmo do fator. [p=0.2] Mil reais ou um milhão, a dez por cento ao ano, {e}dobram no mesmo tempo."),
    dict(id="s15", block="atalho", text="Funciona porque, ao isolar a potência, {a}o capital some na divisão. [p=0.3] Não compensa quando a prova {b}dá a tabela de potências e só pergunta em que ano o dinheiro passa do dobro: [p=0.2] aí, {c}basta olhar a tabela."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Cinco mil reais rendem três por cento ao mês, em juros compostos, [p=0.1] uma taxa alta, só de exemplo. [p=0.3] {b}Em quantos meses viram quinze mil? [p=0.3] Use {c}logaritmo de três igual a zero vírgula quarenta e oito [p=0.1] e {d}logaritmo de um vírgula zero três igual a zero vírgula zero treze."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Cinco mil vezes um vírgula zero três elevado a tê igual a quinze mil. [p=0.2] Isole: {b}um vírgula zero três elevado a tê igual a três. [p=0.3] Logaritmo de cada lado: {c}tê igual a logaritmo de três dividido por logaritmo de um vírgula zero três."),
    dict(id="s19", block="resposta", text="{a}Zero vírgula quarenta e oito dividido por zero vírgula zero treze. [p=0.2] Ande três casas: {b}quatrocentos e oitenta dividido por treze {c}dá cerca de trinta e sete meses. [p=0.2] Pouco mais de três anos."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}isole a potência, [p=0.2] {b}tire o logaritmo de cada lado [p=0.2] e {c}divida."),
    dict(id="s21", block="fim", text="Na próxima aula, o xis vai {a}para dentro do logaritmo: [p=0.2] o logaritmo de xis menos um, na base dois, igual a três. [p=0.3] E aparece {b}uma raiz falsa, que precisa ser descartada. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
