# Estudativo · MAT-FRA-009 — Multiplicar frações (Matemática · Frações e Decimais).
# Habilidade: calcular 2/3 × 5/7 entendendo que 'de' vira vezes, e 4/9 × 3/8 cortando em cruz antes da conta.
# Pré-requisitos: MAT-FRA-002 (fração de uma quantidade), MAT-FRA-003 (equivalentes e simplificação). Próxima: MAT-FRA-010.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Soma de frações não está na ficha: citada só como assunto de outra aula.

TITULO = "Multiplicar frações"

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
    dict(id="s01", block="gancho", text="Multiplicar sempre aumenta, certo? [p=0.3] Então olhe: {a}um meio vezes um quarto. [p=0.3] O resultado é {b}um oitavo. [p=0.3] {c}Menor que um meio, e menor que um quarto."),
    dict(id="s02", block="gancho", text="Não é erro. [p=0.2] Entre frações, o {a}vezes quer dizer pegar uma parte, [p=0.2] e ele se esconde em uma palavrinha: {b}de."),
    dict(id="s03", block="gancho", text="{a}Até o fim desta aula, você vai multiplicar quaisquer frações, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s04", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}calcular a fração de uma quantidade [p=0.2] e {c}simplificar, dividindo o numerador, o número de cima, e o denominador, o de baixo, pelo mesmo número. [p=0.3] Se faltar alguma, procure a aula no canal."),
    # de vira vezes
    dict(id="s05", block="de", text="Comece por algo conhecido: {a}dois quintos de trinta. [p=0.3] Divide pelo de baixo: {b}seis. [p=0.2] Multiplica pelo de cima: {c}doze."),
    dict(id="s06", block="de", text="Você pegou uma parte de trinta. [p=0.2] Em matemática, esse {a}de vira {b}vezes: [p=0.3] {c}dois quintos de trinta é dois quintos vezes trinta. [p=0.3] Confira: o número inteiro multiplica só o de cima. [p=0.2] {d}Dois vezes trinta, sessenta quintos. [p=0.2] O traço é divisão: {e}sessenta dividido por cinco, doze. [p=0.2] O mesmo resultado. [p=0.3] E se a quantidade for outra fração?"),
    # grade
    dict(id="s07", block="grade", text="{a}Dois terços de cinco sétimos. [p=0.3] Pegue uma barra de chocolate e corte em {b}sete colunas iguais. [p=0.2] {c}Pinte cinco: [p=0.2] cinco sétimos da barra."),
    dict(id="s08", block="grade", text="Para pegar dois terços dessa parte pintada, corte a barra na horizontal, {a}em três faixas iguais, [p=0.2] e {b}marque duas."),
    dict(id="s09", block="grade", text="A barra virou uma grade: {a}três vezes sete, vinte e um quadradinhos. [p=0.3] Os que estão pintados e marcados são {b}dois vezes cinco, dez. [p=0.3] {c}Dez vinte e um avos da barra."),
    # regra
    dict(id="s10", block="regra", text="Olhe de onde vieram os números. [p=0.2] {a}Em cima, dois vezes cinco. [p=0.2] {b}Embaixo, três vezes sete. [p=0.3] Pegar parte de uma parte deu uma multiplicação: por isso o de vira vezes. [p=0.3] Essa é a regra inteira: {c}multiplica os de cima, {d}multiplica os de baixo."),
    dict(id="s11", block="regra", text="Repare que você não precisou igualar os denominadores. [p=0.2] Isso é exigência da soma, assunto de outra aula. [p=0.3] Na multiplicação, {a}a própria conta cria o pedaço novo: [p=0.2] aqui, {b}o vinte e um avos."),
    dict(id="s12", block="regra", text="E aquele um meio vezes um quarto? [p=0.2] {a}Um vezes um, um. [p=0.2] {b}Dois vezes quatro, oito. [p=0.3] É {c}a metade de um quarto. [p=0.2] Pegar só uma parte de um pedaço dá menos que o pedaço. [p=0.2] Por isso {d}diminuiu."),
    # treino
    dict(id="s13", block="treino", text="Vamos treinar. [p=0.2] Sobraram {a}dois quintos de uma pizza, e você comeu {b}três quartos disso. [p=0.3] Disso quer dizer de dois quintos, então é vezes. [p=0.3] {c}Três vezes dois, seis. [p=0.2] {d}Quatro vezes cinco, vinte. [p=0.2] {e}Seis vinte avos. [p=0.3] Seis e vinte são pares: {f}divida em cima e embaixo por dois. [p=0.2] Você comeu {g}três décimos da pizza."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com um erro muito comum: {a}repetir o de baixo. [p=0.2] Em {b}dois sétimos vezes três sétimos, a pessoa escreve {c}seis sétimos."),
    dict(id="s15", block="erro", text="Mas dois sétimos de três sétimos é só uma parte de três sétimos. [p=0.2] Tem que dar {a}menos que três sétimos, [p=0.2] e seis sétimos é o dobro. [p=0.3] O de baixo também multiplica: {b}sete vezes sete, quarenta e nove. [p=0.2] {c}Seis quarenta e nove avos."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho prometido: {a}cortar em cruz. [p=0.3] Veja {b}quatro nonos vezes três oitavos. [p=0.2] Direto, dá {c}doze setenta e dois avos, [p=0.2] e ainda falta simplificar."),
    dict(id="s17", block="atalho", text="Antes de multiplicar, olhe na diagonal. [p=0.2] {a}Quatro e oito: divida por quatro, ficam {b}um e dois. [p=0.3] {c}Três e nove: divida por três, ficam {d}um e três. [p=0.3] Em cima, um vezes um. [p=0.2] Embaixo, três vezes dois. [p=0.2] {e}Um sexto. [p=0.3] O mesmo valor de {f}doze setenta e dois avos, com muito menos trabalho."),
    dict(id="s18", block="atalho", text="Funciona porque é {a}simplificar antes da conta. [p=0.2] No fim, todos os de cima se multiplicam em uma linha, e todos os de baixo em outra. [p=0.2] Então, tanto faz de qual fração vem cada número: você pode dividir um de cima e um de baixo pelo mesmo valor. [p=0.3] Não compensa quando {b}a diagonal não tem divisor comum, como em dois terços vezes cinco sétimos. [p=0.2] E {c}só vale na multiplicação."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] {a}Cinco oitavos de um terreno estão plantados. [p=0.2] {b}Dois quintos da parte plantada são de milho. [p=0.3] {c}Que fração do terreno inteiro tem milho?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] Dois quintos {a}de cinco oitavos: a palavra de vira {b}vezes. [p=0.3] Corte em cruz: {c}cinco e cinco, ficam um e um. [p=0.2] {d}Dois e oito: divida por dois, ficam um e quatro. [p=0.3] Em cima, um vezes um. [p=0.1] Embaixo, um vezes quatro. [p=0.2] {e}Um quarto do terreno tem milho."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}a palavra de vira vezes, [p=0.2] {b}multiplica em cima, {c}multiplica embaixo, [p=0.2] e {d}corta em cruz antes, se der."),
    dict(id="s23", block="fim", text="Na próxima aula, você usa isso em um problema que derruba muita gente: [p=0.2] {a}gastar um terço do dinheiro [p=0.1] e depois {b}um quarto do que sobrou. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
