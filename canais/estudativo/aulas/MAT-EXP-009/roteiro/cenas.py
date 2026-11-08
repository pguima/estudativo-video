# Estudativo · MAT-EXP-009 — Propriedades dos logaritmos (Matemática · Exponencial e Logaritmo).
# Habilidade: transformar log(a · b) em soma, log(a/b) em diferença e log a³ em 3 · log a e desmontar log 12 em 2 · log 2 + log 3.
# Pré-requisitos: MAT-EXP-008 (o que é logaritmo), MAT-POT-003 (multiplicar e dividir potências de mesma base). Próxima: MAT-EXP-010.
# Valores de log 2 e log 3 ficam para MAT-EXP-010: aqui só se desmonta. Questão inédita, criada para esta aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Propriedades dos logaritmos"

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
    dict(id="s01", block="gancho", text="{a}O logaritmo de oito na base dois dá três. [p=0.2] {b}O de quatro, na mesma base, dá dois. [p=0.3] E {c}o de trinta e dois, que é oito vezes quatro? [p=0.2] {d}Cinco. [p=0.2] Três mais dois. [p=0.3] Os números se multiplicaram, [p=0.1] e os logaritmos {e}se somaram."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você transforma vezes em mais e dividido em menos, [p=0.2] desmonta logaritmos grandes em pequenos [p=0.2] e leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de duas coisas: [p=0.2] {a}logaritmo é o expoente que falta, [p=0.2] e {b}na mesma base, multiplicar potências soma os expoentes, e dividir subtrai. [p=0.3] Se faltar alguma, procure no canal."),
    # produto
    dict(id="s04", block="produto", text="Por que somou? [p=0.2] Escreva tudo como potência de dois. [p=0.2] {a}Oito é dois ao cubo. [p=0.2] {b}Quatro é dois ao quadrado. [p=0.2] Oito vezes quatro: {c}repete a base e soma os expoentes, e dá dois elevado a cinco. [p=0.3] E o logaritmo {d}é justamente o expoente."),
    dict(id="s05", block="produto", text="A regra: {a}o logaritmo de uma multiplicação é a soma dos logaritmos, [p=0.2] {b}todos na mesma base. [p=0.3] Na tela, com á e bê no lugar de dois números positivos quaisquer: [p=0.2] {c}logaritmo de á vezes bê igual a logaritmo de á mais logaritmo de bê."),
    # divisão
    dict(id="s06", block="divisao", text="Com divisão, é o caminho de volta. [p=0.2] {a}Trinta e dois dividido por quatro dá oito. [p=0.2] Nos logaritmos na base dois: {b}cinco menos dois dá três. [p=0.3] {c}O logaritmo de uma divisão é a diferença dos logaritmos: [p=0.2] {d}o de cima menos o de baixo."),
    # potência
    dict(id="s07", block="potencia", text="E a potência? [p=0.2] {a}Quatro ao cubo é quatro vezes quatro vezes quatro. [p=0.2] Pela regra da multiplicação, {b}some o logaritmo de quatro três vezes. [p=0.3] Na base dois: {c}dois mais dois mais dois dá seis. [p=0.2] Ou seja, {d}três vezes o logaritmo de quatro."),
    dict(id="s08", block="potencia", text="Conferindo: {a}quatro ao cubo dá sessenta e quatro, [p=0.2] e {b}dois elevado a seis também dá sessenta e quatro. [p=0.3] A regra: {c}o expoente de dentro sai para a frente, multiplicando."),
    # desmontar o doze
    dict(id="s09", block="doze", text="Agora, o uso mais pedido: {a}desmontar um logaritmo. [p=0.2] Pegue {b}o logaritmo de doze, com a base dez escondida. [p=0.3] Fatore: {c}doze é dois vezes dois vezes três, [p=0.2] ou {d}dois ao quadrado vezes três."),
    dict(id="s10", block="doze", text="Multiplicação vira soma: {a}logaritmo de dois ao quadrado, mais logaritmo de três. [p=0.2] O expoente sai multiplicando: [p=0.2] {b}duas vezes o logaritmo de dois, mais o logaritmo de três. [p=0.3] A prova costuma dar o valor do logaritmo de dois e do de três, [p=0.2] e aí isso {c}vira número. [p=0.2] Essa conta fica para a próxima aula."),
    # erro
    dict(id="s11", block="erro", text="O erro comum é {a}inventar uma regra para a soma. [p=0.2] Veja {b}o logaritmo, na base dois, de quatro mais quatro, com a soma toda dentro. [p=0.3] A pessoa separa: {c}logaritmo de quatro mais logaritmo de quatro. [p=0.2] Dois mais dois {d}dá quatro."),
    dict(id="s12", block="erro", text="Mas quatro mais quatro é oito, [p=0.2] e {a}o logaritmo de oito na base dois é três. [p=0.3] A regra vale para {b}vezes dentro do logaritmo, e não para mais. [p=0.2] {c}Logaritmo de uma soma não se separa."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, na base dez: {a}os zeros saem somando. [p=0.3] {b}Três mil é três vezes mil. [p=0.2] Então {c}o logaritmo de três mil é o logaritmo de três, mais três. [p=0.2] Os três zeros viram {d}mais três."),
    dict(id="s14", block="atalho", text="Funciona porque {a}multiplicação vira soma, e o logaritmo de mil é três. [p=0.3] Só vale na base dez, [p=0.2] e não compensa quando o número {b}não termina em zero, como doze: [p=0.2] aí, {c}fatore em primos."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Com a base dez, escreva usando só o logaritmo de dois e o de três: [p=0.2] {a}o logaritmo de dezoito [p=0.2] e {b}o logaritmo de três quartos."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Dezoito é dois vezes três ao quadrado. [p=0.2] Vezes vira mais, e o expoente sai multiplicando: [p=0.2] {b}logaritmo de dois, mais duas vezes o logaritmo de três."),
    dict(id="s18", block="resposta", text="Em três quartos, {a}divisão vira menos: logaritmo de três, menos logaritmo de quatro. [p=0.2] Quatro é dois ao quadrado: [p=0.2] {b}logaritmo de três, menos duas vezes o logaritmo de dois."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}vezes vira mais, [p=0.2] {b}dividido vira menos, [p=0.2] e {c}o expoente sai multiplicando."),
    dict(id="s20", block="fim", text="Na próxima aula, as letras viram números. [p=0.2] Com {a}o logaritmo de dois perto de zero vírgula trinta e o de três perto de zero vírgula quarenta e oito, [p=0.2] você calcula {b}o logaritmo de setenta e dois [p=0.2] e {c}troca a base de um logaritmo. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
