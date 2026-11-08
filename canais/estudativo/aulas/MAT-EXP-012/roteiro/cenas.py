# Estudativo · MAT-EXP-012 — Equações logarítmicas (Matemática · Exponencial e Logaritmo).
# Habilidade: resolver log₂(x − 1) = 3 e log x + log(x − 3) = 1, usando a condição de existência para descartar a raiz falsa.
# Pré-requisitos: MAT-EXP-009 (propriedades), MAT-FAT-008 (Bhaskara), MAT-EQU-015 (inequação do 1º grau). Próxima: MAT-EXP-013.
# MAT-EXP-010 e MAT-EXP-011 fora da ficha: sem valores de log 2 e log 3. Questão inédita, criada para esta aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Equações logarítmicas"

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
    dict(id="s01", block="gancho", text="{a}Logaritmo de xis, mais logaritmo de xis menos três, igual a um, [p=0.2] com o xis menos três todo dentro do segundo logaritmo. [p=0.3] Resolvendo, saem {b}duas respostas: cinco e menos dois. [p=0.3] Mas {c}uma delas é falsa, [p=0.2] e quem não confere marca a alternativa errada."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve equações com o xis dentro do logaritmo, descarta a raiz falsa [p=0.2] e leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de quatro coisas: [p=0.2] {a}ler o logaritmo como potência, [p=0.2] {b}a condição de existência, com o logaritmando positivo, [p=0.2] {c}vezes dentro do logaritmo vira mais fora, [p=0.2] e {d}resolver inequação e equação do segundo grau. [p=0.3] Se faltar alguma, procure no canal."),
    # primeiro exemplo
    dict(id="s04", block="simples", text="Comece por {a}logaritmo de xis menos um, na base dois, igual a três, [p=0.2] com o xis menos um todo dentro. [p=0.3] Antes de tudo, {b}a condição de existência: o logaritmando é positivo. [p=0.2] {c}Xis menos um maior que zero, [p=0.2] então {d}xis maior que um."),
    dict(id="s05", block="simples", text="Depois, leia como potência: {a}dois ao cubo igual a xis menos um. [p=0.2] {b}Oito igual a xis menos um, [p=0.2] e {c}xis igual a nove. [p=0.3] Nove é maior que um: {d}passa na condição. [p=0.2] Conferindo: nove menos um dá oito, [p=0.1] e {e}o logaritmo de oito na base dois é três."),
    # segundo exemplo
    dict(id="s06", block="produto", text="Agora a do começo, com a base dez escondida. [p=0.2] Condição para o primeiro logaritmo: {a}xis maior que zero. [p=0.2] Para o segundo: {b}xis menos três maior que zero, ou seja, xis maior que três. [p=0.3] Para valer as duas condições, {c}xis maior que três."),
    dict(id="s07", block="produto", text="Soma de logaritmos vira {a}o logaritmo do produto: [p=0.2] {b}logaritmo de xis vezes, abre parênteses, xis menos três, fecha parênteses, igual a um. [p=0.3] Leia como potência: {c}dez elevado a um igual a esse produto."),
    dict(id="s08", block="produto", text="Aplique a distributiva: {a}xis ao quadrado, [p=0.1] menos três xis, [p=0.1] igual a dez. [p=0.2] Passe o dez para o outro lado: {b}xis ao quadrado, [p=0.1] menos três xis, [p=0.1] menos dez, [p=0.1] igual a zero. [p=0.3] Delta: {c}nove mais quarenta dá quarenta e nove. [p=0.2] {d}A raiz de quarenta e nove é sete."),
    dict(id="s09", block="produto", text="{a}Com mais: três mais sete dá dez, dividido por dois dá cinco. [p=0.2] {b}Com menos: três menos sete dá menos quatro, dividido por dois dá menos dois."),
    # descarte
    dict(id="s10", block="filtro", text="Falta o filtro. [p=0.2] {a}Cinco é maior que três: fica. [p=0.2] {b}Menos dois não é: descarte. [p=0.3] Com menos dois, {c}o logaritmo de menos dois nem existe. [p=0.3] Resposta: {d}xis igual a cinco. [p=0.3] Conferindo: {e}logaritmo de cinco mais logaritmo de dois é o logaritmo de dez, que dá um. [p=0.2] Bateu."),
    dict(id="s11", block="filtro", text="Por que a raiz falsa apareceu? [p=0.2] No produto, {a}menos dois vezes menos cinco dá dez, positivo. [p=0.3] Juntos, os logaritmos aceitam o menos dois. [p=0.2] Separados, {b}nenhum deles existe. [p=0.2] Por isso a condição se tira {c}da equação original, antes de juntar."),
    # método
    dict(id="s12", block="metodo", text="O método tem {a}quatro passos. [p=0.2] {b}Condição de existência. [p=0.2] {c}Junte tudo num logaritmo só. [p=0.2] {d}Leia como potência e resolva. [p=0.2] {e}Passe as raízes pelo filtro da condição."),
    # erro
    dict(id="s13", block="erro", text="Outro erro comum é {a}juntar somando dentro. [p=0.2] A pessoa escreve {b}o logaritmo de xis mais xis menos três, [p=0.1] ou seja, de dois xis menos três, igual a um. [p=0.3] Dá {c}dois xis menos três igual a dez, [p=0.2] e {d}xis igual a seis vírgula cinco."),
    dict(id="s14", block="erro", text="Confira: a soma vira o logaritmo do produto, [p=0.2] e {a}seis vírgula cinco vezes três vírgula cinco dá vinte e dois vírgula setenta e cinco. [p=0.2] Precisava dar dez. [p=0.3] Soma de logaritmos vira {b}produto dentro, e não soma."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}filtre as alternativas antes de resolver. [p=0.2] Se a condição é {b}xis maior que três, [p=0.2] toda alternativa {c}menor ou igual a três já está fora. [p=0.3] Às vezes, {d}sobra uma só, e você nem precisa resolver."),
    dict(id="s16", block="atalho", text="Funciona porque {a}toda resposta precisa passar na condição. [p=0.3] Não compensa quando {b}todas as alternativas passam no filtro: [p=0.2] aí, {c}resolva a equação."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Resolva, com a base três: [p=0.2] {a}logaritmo de xis mais um, mais logaritmo de xis menos um, igual a um. [p=0.3] {b}Xis mais um fica todo dentro do primeiro logaritmo, [p=0.2] e xis menos um, todo dentro do segundo."),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Condição: {a}xis mais um maior que zero, e xis menos um maior que zero. [p=0.2] Juntando as condições, {b}xis maior que um. [p=0.3] Junte num logaritmo só e leia como potência: [p=0.2] {c}o produto de xis mais um por xis menos um igual a três."),
    dict(id="s20", block="resposta", text="Soma vezes diferença: {a}xis ao quadrado menos um igual a três. [p=0.2] {b}Xis ao quadrado igual a quatro, [p=0.2] e {c}xis igual a dois ou menos dois. [p=0.3] {d}Menos dois não passa no filtro. [p=0.2] Resposta: {e}xis igual a dois."),
    dict(id="s21", block="resposta", text="Conferindo: {a}o logaritmo de três na base três dá um, [p=0.2] e {b}o de um dá zero. [p=0.2] Um mais zero dá um. [p=0.2] Bateu."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}condição de existência primeiro, [p=0.2] {b}junte num logaritmo só e leia como potência, [p=0.2] e {c}descarte quem não passar no filtro."),
    dict(id="s23", block="fim", text="Na próxima aula, o logaritmo vira {a}função. [p=0.2] Você desenha {b}ípsilon igual ao logaritmo de xis na base dois, como o espelho de dois elevado a xis, [p=0.2] e resolve {c}a inequação logaritmo de xis na base dois maior que três. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
