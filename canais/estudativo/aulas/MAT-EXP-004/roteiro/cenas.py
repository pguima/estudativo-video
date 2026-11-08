# Estudativo · MAT-EXP-004 — Equação exponencial: igualar as bases (Matemática · Exponencial e Logaritmo).
# Habilidade: resolver 2^(x+1) = 32 e 9ˣ = 27, escrevendo tudo na mesma base e igualando os expoentes.
# Pré-requisitos: MAT-EQU-010 (equação com frações), MAT-EXP-001 (função exponencial), MAT-POT-004 (potência de potência). Próxima: MAT-EXP-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Equação exponencial: igualar as bases"

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
    dict(id="s01", block="gancho", text="{a}Nove elevado a xis igual a vinte e sete. [p=0.3] Teste: {b}nove elevado a um dá nove. [p=0.2] {c}Ao quadrado dá oitenta e um. [p=0.2] Passou direto. [p=0.3] Nenhum número inteiro serve, [p=0.2] e mesmo assim {d}a resposta sai exata, em poucas linhas."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve equações com o xis no expoente, escrevendo tudo na mesma base, [p=0.2] e leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de três coisas: [p=0.2] {a}escrever um número como potência, como sessenta e quatro igual a dois elevado a seis, [p=0.2] {b}potência de potência, que multiplica os expoentes, [p=0.2] e {c}resolver equação, inclusive com fração. [p=0.3] Se faltar alguma, procure no canal."),
    # ideia
    dict(id="s04", block="ideia", text="Comece por {a}dois elevado a xis igual a trinta e dois. [p=0.2] Trinta e dois é {b}dois elevado a cinco. [p=0.3] Fica {c}dois elevado a xis igual a dois elevado a cinco. [p=0.2] Com a mesma base em cada lado, os expoentes são iguais, e {d}xis é igual a cinco."),
    dict(id="s05", block="ideia", text="Por que dá para igualar os expoentes? [p=0.2] Lembre do gráfico de dois elevado a xis: {a}ele sempre sobe. [p=0.2] Então {b}cada saída vem de uma entrada só. [p=0.3] Se a saída é trinta e dois, a entrada só pode ser {c}cinco. [p=0.3] Com base entre zero e um, a curva sempre desce, e vale o mesmo."),
    # método
    dict(id="s06", block="metodo", text="O método tem {a}três passos. [p=0.2] {b}Passo um: escreva cada lado como potência da mesma base. [p=0.2] {c}Passo dois: iguale os expoentes. [p=0.2] {d}Passo três: resolva a equação que sobrou."),
    dict(id="s07", block="metodo", text="Veja {a}dois elevado a xis mais um, com o xis mais um todo no expoente, igual a trinta e dois. [p=0.3] Trinta e dois é {b}dois elevado a cinco. [p=0.2] Iguale os expoentes: {c}xis mais um igual a cinco. [p=0.2] Tire um de cada lado: {d}xis igual a quatro. [p=0.3] Conferindo: quatro mais um dá cinco, [p=0.2] e {e}dois elevado a cinco dá trinta e dois."),
    # nove elevado a xis
    dict(id="s08", block="nove", text="Voltando ao começo: {a}nove elevado a xis igual a vinte e sete. [p=0.3] Vinte e sete não é potência inteira de nove. [p=0.2] Mas nove e vinte e sete são potências de {b}três. [p=0.2] {c}Nove é três ao quadrado. [p=0.2] {d}Vinte e sete é três ao cubo."),
    dict(id="s09", block="nove", text="O lado esquerdo fica {a}três ao quadrado, tudo elevado a xis. [p=0.2] Potência de potência multiplica os expoentes: {b}três elevado a dois xis. [p=0.3] Agora, {c}três elevado a dois xis igual a três ao cubo. [p=0.2] Iguale: {d}dois xis igual a três. [p=0.2] Divida cada lado por dois. [p=0.2] {e}Xis igual a três dividido por dois, ou um vírgula cinco."),
    dict(id="s10", block="nove", text="Confira com o expoente em fração. [p=0.2] O de baixo é a raiz: {a}raiz de nove dá três. [p=0.2] O de cima é a potência: {b}três ao cubo dá vinte e sete. [p=0.2] Bateu."),
    # fração do outro lado
    dict(id="s11", block="fracao", text="E se o outro lado for fração? [p=0.2] {a}Dois elevado a xis igual a um oitavo. [p=0.2] Um oitavo é um dividido por dois ao cubo, [p=0.2] ou seja, {b}dois elevado a menos três. [p=0.2] Então {c}xis igual a menos três."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}dividir os números da equação. [p=0.2] Em nove elevado a xis igual a vinte e sete, a pessoa faz {b}vinte e sete dividido por nove, que dá três, [p=0.2] e responde {c}xis igual a três."),
    dict(id="s13", block="erro", text="Mas {a}nove ao cubo dá setecentos e vinte e nove, bem longe de vinte e sete. [p=0.3] O xis está no expoente. [p=0.2] Ele só sai de lá {b}igualando as bases."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}desça até o primo. [p=0.2] Não enxergou a base comum? [p=0.2] {b}Fatore os números. [p=0.2] Nove e vinte e sete só têm o primo três. [p=0.2] Quatro e trinta e dois só têm o primo dois. [p=0.3] Quando sobra um primo só, ele é {c}a base que serve para cada lado."),
    dict(id="s15", block="atalho", text="Funciona porque a fatoração mostra {a}de que a base é feita. [p=0.3] Com mais de um primo, a base junta todos eles. [p=0.2] {b}Seis é dois vezes três. [p=0.2] Trinta e seis tem os mesmos primos, e é seis ao quadrado. [p=0.3] Não compensa quando um lado tem um primo que o outro não tem, como em {c}dois elevado a xis igual a dez. [p=0.2] Dez tem o primo cinco, que o dois não tem. [p=0.2] Essa equação pede {d}logaritmo, assunto de outra aula."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Resolva as duas. [p=0.2] {a}Quatro elevado a xis menos um, com o xis menos um todo no expoente, igual a sessenta e quatro. [p=0.3] E {b}vinte e sete elevado a xis igual a nove."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Na primeira, o primo é dois. [p=0.2] {a}Quatro é dois ao quadrado, e sessenta e quatro é dois elevado a seis. [p=0.2] Potência de potência multiplica os expoentes: [p=0.2] o lado esquerdo fica com expoente {b}dois vezes, abre parênteses, xis menos um, fecha parênteses. [p=0.2] Iguale esse expoente a seis. [p=0.2] Divida cada lado por dois. [p=0.2] {c}Xis menos um igual a três. [p=0.2] {d}Xis igual a quatro."),
    dict(id="s19", block="resposta", text="Quem viu que {a}sessenta e quatro é quatro ao cubo chega mais rápido: [p=0.2] xis menos um igual a três, direto."),
    dict(id="s20", block="resposta", text="Na segunda, o primo é três. [p=0.2] {a}Vinte e sete é três ao cubo, e nove é três ao quadrado. [p=0.2] Fica {b}três elevado a três xis igual a três ao quadrado. [p=0.2] {c}Três xis igual a dois, [p=0.2] e {d}xis igual a dois terços. [p=0.3] Conferindo: {e}raiz cúbica de vinte e sete dá três, e três ao quadrado dá nove."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}mesma base dos dois lados, [p=0.2] {b}expoentes iguais, [p=0.2] e {c}resolva a equação que sobra."),
    dict(id="s22", block="fim", text="Na próxima aula, no lugar do igual entram {a}o maior e o menor: [p=0.2] dois elevado a xis maior que oito, e um meio elevado a xis maior que oito. [p=0.3] E você descobre {b}quando o sinal vira. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
