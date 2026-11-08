# Estudativo · MAT-EQU-015 — Resolver inequação do 1º grau (Matemática · Equações do 1º Grau).
# Habilidade: resolver −2x < 6, explicar por que o sinal vira e marcar a resposta na reta numérica.
# Pré-requisitos: MAT-EQU-008 (letra dos dois lados), MAT-NUM-015 (reta numérica). Próxima: MAT-EQU-016.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Reta como na MAT-NUM-015: mais à direita é maior.

TITULO = "Resolver inequação do 1º grau"

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
    dict(id="s01", block="gancho", text="{a}Menos dois xis menor que seis. [p=0.3] Muita gente divide por menos dois [p=0.2] e escreve {b}xis menor que menos três. [p=0.3] Teste o zero: [p=0.2] {c}menos dois vezes zero dá zero, e zero é menor que seis. [p=0.2] O zero serve. [p=0.3] Mas {d}zero não é menor que menos três. [p=0.2] Alguma coisa deu errado."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve isso, [p=0.2] entende {b}por que o sinal vira [p=0.2] e marca a resposta {c}na reta."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}resolver equação fazendo o mesmo nos dois lados, [p=0.2] e {c}a reta numérica, onde quem está mais à direita é maior. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="oque", text="Uma {a}inequação é como uma equação, [p=0.2] só que, no lugar do igual, [p=0.2] vem um destes sinais: [p=0.2] {b}maior, [p=0.1] menor, [p=0.2] {c}maior ou igual, [p=0.1] e menor ou igual. [p=0.3] E a resposta {d}não é um número só: [p=0.2] é um monte de números."),
    dict(id="s05", block="oque", text="Veja {a}três xis menos dois, menor ou igual a sete. [p=0.3] Resolve como na balança. [p=0.2] {b}Some dois de cada lado: [p=0.2] {c}três xis menor ou igual a nove. [p=0.2] {d}Divida cada lado por três: [p=0.2] {e}xis menor ou igual a três."),
    dict(id="s06", block="oque", text="Na reta, {a}todo número à esquerda do três serve, [p=0.2] e o próprio três também, [p=0.2] porque ali {b}a conta dá exatamente sete. [p=0.3] Para mostrar que o três entra, [p=0.2] ele ganha uma {c}bolinha fechada, pintada por dentro. [p=0.2] E pintamos {d}a reta para a esquerda."),
    # por que vira
    dict(id="s07", block="porque", text="Até aqui, nada de novo. [p=0.2] O problema aparece com {a}número negativo. [p=0.3] {b}Dois é menor que três. [p=0.2] Ponha um sinal de menos em cada um: [p=0.2] {c}menos dois e menos três."),
    dict(id="s08", block="porque", text="Na reta, {a}menos dois fica mais à direita. [p=0.2] Então {b}menos dois é maior que menos três. [p=0.3] Os números trocaram de posição, [p=0.2] e {c}o sinal de menor virou sinal de maior."),
    dict(id="s09", block="porque", text="Pôr o menos é {a}multiplicar por menos um. [p=0.2] E dividir por negativo faz o mesmo: [p=0.2] {b}seis é menor que nove. [p=0.2] Divida cada um por menos três. [p=0.2] Seis vira menos dois. [p=0.2] Nove vira menos três. [p=0.2] E {c}menos dois é maior que menos três. [p=0.3] A regra: [p=0.2] {d}multiplicou ou dividiu por negativo, vira o sinal. [p=0.2] {e}Somar e tirar não viram: [p=0.2] {f}dois mais dez dá doze. [p=0.2] Três mais dez dá treze. [p=0.2] E doze continua menor que treze. [p=0.2] {g}Multiplicar ou dividir por positivo também não vira: [p=0.2] {h}dois vezes dez dá vinte. [p=0.2] Três vezes dez dá trinta. [p=0.2] E vinte continua menor que trinta."),
    # resolvendo
    dict(id="s10", block="resolver", text="Voltando: {a}menos dois xis menor que seis. [p=0.3] Para soltar o xis, {b}divida cada lado por menos dois. [p=0.2] Dividiu por negativo, {c}vira o sinal: [p=0.2] {d}xis maior que menos três."),
    dict(id="s11", block="resolver", text="Teste o zero de novo: [p=0.2] {a}zero é maior que menos três. [p=0.2] Agora sim, a resposta aceita o zero, [p=0.2] como a inequação original."),
    dict(id="s12", block="resolver", text="Na reta, {a}pintamos tudo à direita do menos três. [p=0.3] E o menos três? [p=0.2] {b}Menos dois vezes menos três dá seis, [p=0.2] e seis {c}não é menor que seis. [p=0.2] Ele fica de fora, [p=0.2] então ganha uma {d}bolinha aberta, vazia por dentro. [p=0.3] {e}Fechada, o número entra. [p=0.2] {f}Aberta, fica de fora."),
    # erro
    dict(id="s13", block="erro", text="Agora, cuidado com o erro oposto: [p=0.2] {a}virar o sinal sem precisar. [p=0.3] Em {b}três xis menor que menos doze, [p=0.2] você divide por três, que é {c}positivo. [p=0.2] Fica {d}xis menor que menos quatro, sem virar. [p=0.3] {e}Quem manda é o número que você usa para dividir, [p=0.2] e não o menos doze do outro lado. [p=0.3] {f}Quem vira escreve xis maior que menos quatro, [p=0.2] e aí o zero entraria. [p=0.2] Só que três vezes zero dá zero, [p=0.2] e zero não é menor que menos doze."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho prometido: [p=0.2] {a}teste um número fácil, como o zero, na inequação original. [p=0.3] {b}Se ele serve lá, tem que servir na resposta. [p=0.2] Se não bater, {c}o sinal está do lado errado."),
    dict(id="s15", block="atalho", text="Funciona porque a resposta é {a}o grupo de números que servem. [p=0.2] Com o sinal do lado errado, ela pega justamente os que não servem. [p=0.3] {b}Não compensa quando a resposta tem o zero bem na fronteira, [p=0.2] como em xis maior que zero: [p=0.2] aí o zero dá o mesmo resultado com o sinal certo e com o errado. [p=0.2] Então, {c}teste um outro número, como o um."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Resolva {a}menos quatro xis mais dois, maior ou igual a dez. [p=0.3] {b}Depois, diga se a bolinha na reta é aberta ou fechada, [p=0.2] e {c}para que lado você pinta."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Tire dois de cada lado: [p=0.2] {b}menos quatro xis maior ou igual a oito. [p=0.3] {c}Divida por menos quatro. [p=0.2] É negativo, {d}vira o sinal: [p=0.2] {e}xis menor ou igual a menos dois."),
    dict(id="s19", block="resposta", text="Como tem o igual, {a}a bolinha no menos dois é fechada. [p=0.2] E {b}pinta para a esquerda. [p=0.3] Testando o zero: [p=0.2] {c}menos quatro vezes zero mais dois dá dois, [p=0.2] e dois não é maior nem igual a dez. [p=0.2] O zero não serve, [p=0.2] e {d}de fato ele está fora da parte pintada. [p=0.2] {e}Bateu."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}resolve como equação, [p=0.2] {b}vira o sinal ao multiplicar ou dividir por negativo [p=0.2] e {c}confere com um número."),
    dict(id="s21", block="fim", text="Na próxima aula, você resolve {a}inequações com duas condições ao mesmo tempo [p=0.2] e descobre {b}a partir de quantos minutos um plano fica mais barato. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
