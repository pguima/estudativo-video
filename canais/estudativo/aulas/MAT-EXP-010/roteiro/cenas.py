# Estudativo · MAT-EXP-010 — Usar log 2, log 3 e mudança de base (Matemática · Exponencial e Logaritmo).
# Habilidade: calcular log 72, log 5 = 1 − log 2 e log₂ 5 = log 5 / log 2 a partir de log 2 ≈ 0,30 e log 3 ≈ 0,48.
# Pré-requisitos: MAT-EXP-009 (propriedades dos logaritmos). Próxima: MAT-EXP-011.
# Valores aproximados, como os enunciados costumam dar. Mudança de base justificada tirando o logaritmo dos dois lados (método da MAT-EXP-011).
# Questão inédita, criada para esta aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Usar log 2, log 3 e mudança de base"

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
    dict(id="s01", block="gancho", text="Quanto é {a}o logaritmo de setenta e dois? [p=0.2] Sem calculadora. [p=0.3] Com {b}dois valores que a prova costuma dar, [p=0.2] a resposta sai em três linhas [p=0.2] e {c}dá cerca de um vírgula oitenta e seis."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula logaritmos a partir do logaritmo de dois e do de três, [p=0.2] troca a base de um logaritmo [p=0.2] e leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de duas coisas: [p=0.2] {a}as propriedades: vezes vira mais, dividido vira menos e o expoente sai multiplicando, [p=0.2] e {b}a base dez escondida, em que o logaritmo de mil dá três. [p=0.3] Se faltar alguma, procure no canal."),
    # os valores
    dict(id="s04", block="valores", text="Os valores são estes, com a base dez. [p=0.2] {a}O logaritmo de dois vale cerca de zero vírgula trinta. [p=0.2] {b}O logaritmo de três vale cerca de zero vírgula quarenta e oito. [p=0.3] Ou seja, {c}dez elevado a zero vírgula trinta dá quase dois. [p=0.3] São aproximações, e o enunciado costuma dar esses valores."),
    # setenta e dois
    dict(id="s05", block="setenta", text="Comece por {a}setenta e dois. [p=0.2] Fatore: {b}oito vezes nove, [p=0.2] ou {c}dois ao cubo vezes três ao quadrado. [p=0.3] Pelas propriedades: {d}três vezes o logaritmo de dois, mais duas vezes o logaritmo de três."),
    dict(id="s06", block="setenta", text="{a}Três vezes zero vírgula trinta dá zero vírgula noventa. [p=0.2] {b}Duas vezes zero vírgula quarenta e oito dá zero vírgula noventa e seis. [p=0.2] A soma {c}dá um vírgula oitenta e seis. [p=0.3] Faz sentido: setenta e dois fica entre dez e cem, [p=0.2] então o logaritmo fica {d}entre um e dois."),
    # cinco
    dict(id="s07", block="cinco", text="E {a}o logaritmo de cinco? [p=0.2] Cinco é primo, e não é dois nem três. [p=0.2] O truque é ver {b}cinco como dez dividido por dois. [p=0.3] Divisão vira menos: {c}logaritmo de dez menos logaritmo de dois. [p=0.2] O logaritmo de dez, na base dez, é {d}um. [p=0.2] Então {e}um menos zero vírgula trinta dá zero vírgula setenta."),
    # mudança de base
    dict(id="s08", block="base", text="Agora, outra base: {a}o logaritmo de cinco na base dois. [p=0.2] A prova só deu valores na base dez. [p=0.3] Para isso existe a {b}mudança de base: [p=0.2] {c}o logaritmo de cinco na base dois é o logaritmo de cinco dividido pelo logaritmo de dois, [p=0.2] {d}com o de cima e o de baixo na base dez."),
    dict(id="s09", block="base", text="De onde vem? [p=0.2] Chame o resultado de xis: {a}dois elevado a xis igual a cinco. [p=0.2] Números iguais têm logaritmos iguais, [p=0.1] então {b}tire o logaritmo na base dez de cada lado. [p=0.3] O expoente sai multiplicando: {c}xis vezes logaritmo de dois igual a logaritmo de cinco. [p=0.2] {d}Divida pelo logaritmo de dois, e aí está a fórmula."),
    dict(id="s10", block="base", text="Na conta: {a}zero vírgula setenta dividido por zero vírgula trinta. [p=0.2] Tire a vírgula: {b}setenta dividido por trinta {c}dá cerca de dois vírgula trinta e três. [p=0.3] Confira: {d}dois ao quadrado dá quatro, e dois ao cubo dá oito. [p=0.2] Cinco fica no meio, então o expoente fica {e}entre dois e três. [p=0.2] Bateu."),
    # erro
    dict(id="s11", block="erro", text="O erro comum é {a}trocar a divisão por subtração. [p=0.2] A pessoa lembra que divisão vira menos, [p=0.2] e faz {b}zero vírgula setenta menos zero vírgula trinta, que dá zero vírgula quarenta."),
    dict(id="s12", block="erro", text="Mas zero vírgula quarenta é menor que um, [p=0.2] e {a}dois elevado a um número menor que um dá menos que dois. [p=0.2] Longe de cinco. [p=0.3] Divisão vira menos {b}dentro do logaritmo. [p=0.2] Na mudança de base, {c}é um logaritmo dividido pelo outro."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}dois e cinco fecham dez. [p=0.3] {b}Logaritmo de dois mais logaritmo de cinco dá um. [p=0.2] Sabendo um deles, {c}o outro é o que falta para chegar a um. [p=0.3] E com os zeros somando: {d}o logaritmo de cinquenta dá um vírgula setenta."),
    dict(id="s14", block="atalho", text="Funciona porque {a}dois vezes cinco dá dez, e o logaritmo de dez é um. [p=0.3] Não compensa com primos como {b}sete: [p=0.2] ele não sai de dois, três e dez. [p=0.2] Nesse caso, {c}a prova precisa dar o valor."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Com {a}logaritmo de dois igual a zero vírgula trinta e logaritmo de três igual a zero vírgula quarenta e oito, [p=0.2] calcule {b}o logaritmo de quinze [p=0.2] e {c}o logaritmo de três na base dois."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Quinze é três vezes cinco: [p=0.2] {b}logaritmo de três mais logaritmo de cinco. [p=0.2] O de cinco é um menos zero vírgula trinta, que {c}dá zero vírgula setenta. [p=0.2] {d}Zero vírgula quarenta e oito mais zero vírgula setenta dá um vírgula dezoito."),
    dict(id="s18", block="resposta", text="Na segunda, mudança de base: {a}zero vírgula quarenta e oito dividido por zero vírgula trinta. [p=0.2] {b}Quarenta e oito dividido por trinta dá um vírgula seis. [p=0.3] Confira: três fica entre dois e quatro, [p=0.2] então o expoente fica {c}entre um e dois. [p=0.2] Bateu."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}fatore e use o logaritmo de dois e o de três. [p=0.2] {b}Cinco é dez dividido por dois. [p=0.2] E {c}para trocar a base, divida um logaritmo pelo outro."),
    dict(id="s20", block="fim", text="Na próxima aula, isso fecha uma conta que ficou pendente nos juros compostos: [p=0.2] {a}em quanto tempo um dinheiro dobra. [p=0.3] Você vai achar o tê de {b}um vírgula um elevado a tê igual a dois. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
