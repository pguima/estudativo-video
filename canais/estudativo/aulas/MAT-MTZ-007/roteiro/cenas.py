# Estudativo · MAT-MTZ-007 — Discutir um sistema: uma, infinitas ou nenhuma solução (Matemática · Matrizes e Sistemas).
# Habilidade: classificar um sistema pelo escalonamento, achar o valor de k que o deixa sem solução e ver cada equação 3x3 como um plano no espaço.
# Pré-requisitos: MAT-ESP-004 (retas e planos no espaço), MAT-MTZ-006 (escalonamento). Próxima: MAT-MTZ-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Matrizes e determinantes não estão na ficha: a discussão é só pelo escalonamento.
# Letras narradas "xis", "ípsilon", "zê" e "cá".

TITULO = "Discutir um sistema: uma, infinitas ou nenhuma solução"

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
    dict(id="s01", block="gancho", text="Até agora, todo sistema teve {a}uma resposta só. [p=0.3] Mas escalone este, e no fim aparece {b}zero igual a dois. [p=0.3] Não é erro de conta: [p=0.2] {c}esse sistema não tem solução nenhuma."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você descobre se um sistema tem uma, infinitas ou nenhuma solução, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre {a}duas coisas: [p=0.2] {b}escalonar é tirar uma letra por vez até o sistema virar escada, [p=0.2] e {c}o plano é como uma folha sem bordas, que se estende para todos os lados. [p=0.3] Se faltar alguma, procure no canal."),
    # os três casos
    dict(id="s04", block="casos", text="Ao escalonar, olhe {a}a última linha da escada. [p=0.2] Ela conta tudo. [p=0.3] {b}Sobrou uma letra com número, como três zê igual a seis? [p=0.2] Há uma solução só, [p=0.2] e o sistema é {c}possível e determinado."),
    dict(id="s05", block="casos", text="{a}Virou zero igual a zero? [p=0.2] Essa linha é sempre verdade e não diz nada. [p=0.2] Sobram {b}menos equações do que letras, [p=0.2] e o sistema tem {c}infinitas soluções: é possível e indeterminado."),
    dict(id="s06", block="casos", text="{a}Virou zero igual a um número que não é zero, como zero igual a dois? [p=0.2] É uma mentira. [p=0.2] {b}Nenhum trio resolve, [p=0.2] e o sistema é {c}impossível."),
    # exemplo
    dict(id="s07", block="exemplo", text="Veja: [p=0.2] {a}xis mais ípsilon mais zê igual a três; [p=0.2] {b}xis mais dois ípsilon mais dois zê igual a cinco; [p=0.2] {c}dois xis mais três ípsilon mais três zê igual a dez."),
    dict(id="s08", block="exemplo", text="{a}Segunda menos primeira: ípsilon mais zê igual a dois. [p=0.2] {b}Terceira menos duas vezes a primeira: ípsilon mais zê igual a quatro. [p=0.3] {c}Uma menos a outra: zero igual a dois. [p=0.3] {d}Impossível: ípsilon mais zê não pode dar dois e quatro ao mesmo tempo."),
    dict(id="s09", block="exemplo", text="Agora troque o dez por {a}oito. [p=0.2] A terceira menos duas vezes a primeira dá {b}ípsilon mais zê igual a dois, igual à de cima. [p=0.2] {c}Sobra zero igual a zero: infinitas soluções. [p=0.3] Por exemplo, {d}um, um, um, [p=0.2] ou {e}um, dois, zero."),
    # o k
    dict(id="s10", block="valork", text="E o valor de {a}cá que deixa o sistema sem solução? [p=0.2] Pegue o sistema da aula anterior {b}com um cá no lugar do dois da última equação. [p=0.3] {c}Segunda menos primeira: ípsilon igual a dois. [p=0.2] {d}Terceira menos primeira: cá zê menos zê, igual a três."),
    dict(id="s11", block="valork", text="Junte os zês: {a}cá menos um, vezes zê, igual a três. [p=0.3] Se {b}cá for um, fica zero vezes zê igual a três: [p=0.2] {c}zero igual a três, impossível. [p=0.3] Com {d}qualquer outro cá, sai um valor só para zê."),
    # planos
    dict(id="s12", block="planos", text="E por que existem três casos? [p=0.2] Cada equação com três letras é {a}um plano no espaço. [p=0.2] A solução é o ponto que está {b}nos três planos ao mesmo tempo."),
    dict(id="s13", block="planos", text="{a}Uma solução: os três planos se cruzam num ponto só, [p=0.2] como o chão e duas paredes no canto da sala. [p=0.3] {b}Infinitas: os três passam pela mesma reta, [p=0.2] como as páginas de um livro, presas na lombada. [p=0.3] {c}Nenhuma: não há ponto comum, [p=0.2] como o chão e o teto, que nunca se encontram."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}ler zero igual a zero como se a resposta fosse zero. [p=0.3] Zero igual a zero {b}não dá valor para letra nenhuma: [p=0.2] diz que {c}sobram infinitas soluções."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: [p=0.2] {a}veja se o lado das letras de uma equação é o dobro do de outra. [p=0.3] Em {b}xis mais ípsilon mais zê igual a três [p=0.2] e {c}dois xis mais dois ípsilon mais dois zê igual a sete, [p=0.2] as letras dobraram, [p=0.2] mas {d}o dobro de três é seis, e não sete. [p=0.2] {e}Impossível, sem escalonar nada."),
    dict(id="s16", block="atalho", text="Funciona porque, se o lado das letras dobra, [p=0.2] {a}o número do outro lado tem que dobrar junto. [p=0.3] {b}Se ele também dobrar, as duas equações dizem a mesma coisa, [p=0.2] e o atalho não decide sozinho: escalone."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Classifique o sistema: [p=0.2] {b}xis mais ípsilon mais zê igual a dois; [p=0.2] {c}xis menos ípsilon mais zê igual a zero; [p=0.2] {d}dois xis mais dois zê igual a dois."),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Segunda menos primeira: menos dois ípsilon igual a menos dois. [p=0.3] {b}Terceira menos duas vezes a primeira: menos dois ípsilon igual a dois menos quatro, menos dois. [p=0.3] {c}As duas sobras são iguais, [p=0.2] e uma menos a outra dá {d}zero igual a zero."),
    dict(id="s20", block="resposta", text="O sistema é {a}possível e indeterminado: infinitas soluções. [p=0.3] Por exemplo, {b}um, um, zero, [p=0.2] e {c}zero, um, um. [p=0.3] No espaço, {d}três planos passando pela mesma reta."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: olhe a última linha da escada. [p=0.2] {a}Letra com número: uma solução. [p=0.2] {b}Zero igual a zero: infinitas. [p=0.2] {c}Zero igual a outro número: nenhuma."),
    dict(id="s22", block="fim", text="Na próxima aula, você escreve o sistema {a}como multiplicação de matrizes [p=0.2] e resolve com {b}a regra de Cramer, usando determinantes. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
