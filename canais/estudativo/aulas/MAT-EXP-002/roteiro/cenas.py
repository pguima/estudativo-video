# Estudativo · MAT-EXP-002 — Crescimento e decaimento: somar ou multiplicar (Matemática · Exponencial e Logaritmo).
# Habilidade: modelar uma população que cresce 3% ao ano como P = P₀ · 1,03ᵗ e um carro que perde 10% ao ano e decidir por uma tabela se o modelo é afim ou exponencial.
# Pré-requisitos: MAT-EXP-001 (função exponencial), MAT-FUN-009 (função afim), MAT-POR-004 (fatores de aumento e de desconto). Próxima: MAT-EXP-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Crescimento e decaimento: somar ou multiplicar"

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
    dict(id="s01", block="gancho", text="Duas cidades começam com {a}dez mil habitantes. [p=0.2] A primeira ganha {b}trezentas pessoas por ano. [p=0.2] A segunda cresce {c}três por cento ao ano. [p=0.3] No primeiro ano, as cidades chegam a {d}dez mil e trezentos. [p=0.2] Parece a mesma coisa."),
    dict(id="s02", block="gancho", text="Em cinquenta anos, a primeira chega a {a}vinte e cinco mil. [p=0.2] A segunda passa de {b}quarenta e três mil. [p=0.3] {c}Até o fim desta aula, você entende essa diferença, monta a lei de cada uma e leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de três coisas: [p=0.2] {a}função afim, que muda sempre o mesmo valor a cada passo, [p=0.2] {b}fator de aumento e de desconto, [p=0.2] e {c}a função exponencial, com o xis no expoente. [p=0.3] Se faltar alguma, procure no canal."),
    # somar: afim
    dict(id="s04", block="somar", text="Na primeira cidade, cada ano {a}soma trezentos. [p=0.2] {b}Dez mil. [p=0.1] Dez mil e trezentos. [p=0.1] Dez mil e seiscentos. [p=0.3] É a função afim: {c}pê igual a dez mil mais trezentos vezes tê, [p=0.2] com tê em anos. [p=0.2] O gráfico é {d}uma reta."),
    # multiplicar: exponencial
    dict(id="s05", block="multiplicar", text="Na segunda, cada ano {a}soma três por cento do que já existe. [p=0.3] Somar três por cento é multiplicar pelo fator {b}um vírgula zero três. [p=0.3] {c}Em um ano, dez mil vezes um vírgula zero três dá dez mil e trezentos. [p=0.2] {d}Em dois anos, vezes um vírgula zero três de novo dá dez mil seiscentos e nove."),
    dict(id="s06", block="multiplicar", text="Os três por cento do segundo ano valem sobre uma população maior, [p=0.2] então o salto cresce: {a}trezentos, depois trezentos e nove. [p=0.3] Em tê anos, o fator se repete tê vezes. [p=0.2] O mesmo número multiplicado várias vezes é {b}uma potência."),
    dict(id="s07", block="multiplicar", text="A lei fica {a}pê igual a pê zero vezes um vírgula zero três elevado a tê. [p=0.3] {b}Pê é a população no ano tê. [p=0.2] {c}Pê zero é a população do começo, no ano zero. [p=0.2] E {d}o fator vai na base, com o tempo no expoente. [p=0.3] Base maior que um: {e}a curva sobe."),
    # decaimento
    dict(id="s08", block="carro", text="E no caminho contrário? [p=0.2] Um carro de {a}cinquenta mil reais perde dez por cento do valor a cada ano. [p=0.3] Tirar dez por cento é multiplicar pelo fator de desconto {b}zero vírgula nove."),
    dict(id="s09", block="carro", text="{a}Em um ano, cinquenta mil vezes zero vírgula nove dá quarenta e cinco mil. [p=0.2] {b}Em dois anos, vezes zero vírgula nove de novo dá quarenta mil e quinhentos. [p=0.2] {c}Em três anos, dá trinta e seis mil quatrocentos e cinquenta. [p=0.3] A lei: {d}vê igual a cinquenta mil vezes zero vírgula nove elevado a tê. [p=0.3] Base entre zero e um: {e}a curva desce. [p=0.2] Isso se chama decaimento."),
    # teste da tabela
    dict(id="s10", block="teste", text="E quando a prova dá só uma tabela? [p=0.2] Com o tempo andando de um em um, faça dois testes. [p=0.3] {a}Subtraia cada valor do anterior. [p=0.2] Se a diferença for sempre a mesma, {b}é afim: o modelo soma."),
    dict(id="s11", block="teste", text="{a}Divida cada valor pelo anterior. [p=0.2] Se a divisão der sempre o mesmo número, {b}é exponencial: o modelo multiplica. [p=0.3] E esse número é {c}o fator. [p=0.2] No carro, quarenta e cinco mil dividido por cinquenta mil dá {d}zero vírgula nove."),
    # erro
    dict(id="s12", block="erro", text="Agora, cuidado com um erro muito comum. [p=0.2] O carro perde dez por cento por ano. [p=0.2] Então, em {a}dez anos, perde cem por cento [p=0.2] e {b}vale zero. [p=0.3] Será?"),
    dict(id="s13", block="erro", text="Não. [p=0.2] Cada ano tira dez por cento {a}do que sobrou, e o que sobra é cada vez menor. [p=0.3] Na calculadora, depois de dez anos, o carro ainda vale cerca de {b}dezessete mil e quatrocentos reais. [p=0.3] Como você viu no gráfico, a exponencial {c}nunca chega a zero."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}olhe os saltos. [p=0.3] Saltos iguais, {b}é afim. [p=0.2] Saltos que crescem ou encolhem, {c}desconfie de exponencial, e só então divida."),
    dict(id="s15", block="atalho", text="Funciona porque no afim se soma {a}sempre o mesmo valor. [p=0.2] Na exponencial, se soma {b}uma porcentagem de um valor que muda. [p=0.3] Não compensa com taxa pequena e números arredondados: [p=0.2] os saltos parecem iguais. [p=0.2] Aí, {c}faça a divisão."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Dois perfis começam com {a}mil seguidores. [p=0.2] Mês a mês, o perfil á tem: [p=0.1] {b}mil. [p=0.1] Mil e cem. [p=0.1] Mil duzentos e dez. [p=0.1] Mil trezentos e trinta e um. [p=0.3] O perfil bê tem: [p=0.1] {c}mil. [p=0.1] Mil e cem. [p=0.1] Mil e duzentos. [p=0.1] Mil e trezentos. [p=0.3] {d}Qual é exponencial? Escreva a lei de cada um."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] No perfil bê, os saltos são {a}sempre cem. [p=0.2] É afim: {b}ésse igual a mil mais cem vezes tê, com tê em meses."),
    dict(id="s19", block="resposta", text="No perfil á, os saltos crescem: [p=0.1] {a}cem. [p=0.1] Depois cento e dez. [p=0.1] Depois cento e vinte e um. [p=0.3] Divida: {b}mil e cem dividido por mil dá um vírgula um. [p=0.2] {c}Mil duzentos e dez dividido por mil e cem também. [p=0.3] É exponencial, com fator um vírgula um. [p=0.2] Isso é {d}dez por cento ao mês. [p=0.2] A lei: {e}ésse igual a mil vezes um vírgula um elevado a tê."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}somar o mesmo valor é afim. [p=0.2] {b}Multiplicar pelo mesmo fator é exponencial, com o fator na base e o tempo no expoente."),
    dict(id="s21", block="fim", text="Na próxima aula, o tempo é medido de outro jeito: {a}quanto leva para dobrar, ou para cair pela metade. [p=0.3] Você vai calcular {b}quanto resta de um remédio depois de três meias-vidas e contar bactérias que dobram a cada vinte minutos. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
