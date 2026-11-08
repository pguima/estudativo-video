# Estudativo · MAT-FAT-008 — Fórmula de Bhaskara (Matemática · Fatoração e Equação do 2º Grau).
# Habilidade: resolver x² − 5x + 6 = 0 e −x² + 2x + 3 = 0 calculando Δ primeiro, com parênteses nos números negativos.
# Pré-requisitos: MAT-EQU-002 (valor numérico com parênteses), MAT-FAT-007 (a, b e c; incompleta). Próxima: MAT-FAT-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis"; o coeficiente a se fala "á".

TITULO = "Fórmula de Bhaskara"

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
    dict(id="s01", block="gancho", text="{a}Xis ao quadrado menos cinco xis mais seis igual a zero. [p=0.3] Não dá para isolar o xis ao quadrado, [p=0.2] e {b}não tem fator comum. [p=0.3] Para essa, existe {c}uma fórmula que resolve qualquer equação do segundo grau."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você usa a fórmula de Bhaskara [p=0.2] sem tropeçar no {b}sinal de menos."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}duas coisas: [p=0.2] {b}apontar á, bê e cê, com o sinal junto, [p=0.2] e {c}trocar a letra por um número entre parênteses. [p=0.3] Se faltar alguma, procure no canal."),
    # a fórmula
    dict(id="s04", block="formula", text="A fórmula tem {a}duas etapas. [p=0.2] Primeiro, um número com nome de letra grega, {b}delta, escrito como um triângulo. [p=0.3] {c}Delta é igual a bê ao quadrado, menos quatro vezes á vezes cê."),
    dict(id="s05", block="formula", text="Depois, {a}xis é igual a menos bê, mais ou menos raiz de delta, [p=0.2] tudo dividido por {b}dois á. [p=0.3] O {c}mais ou menos quer dizer: faça a conta duas vezes, uma com mais e outra com menos. [p=0.2] É daí que saem {d}as duas raízes."),
    dict(id="s06", block="formula", text="De onde ela vem? [p=0.2] Ela sai de {a}transformar a equação num trinômio quadrado perfeito, [p=0.2] como os que você fatorou. [p=0.3] Na prova, ninguém pede essa conta: {b}pede que você saiba usar a fórmula."),
    # exemplo 1
    dict(id="s07", block="exemplo1", text="No exemplo: {a}á vale um, bê vale menos cinco, cê vale seis. [p=0.3] Delta: {b}abre parênteses, menos cinco, fecha parênteses, ao quadrado, dá vinte e cinco. [p=0.2] {c}Quatro vezes um vezes seis dá vinte e quatro. [p=0.2] {d}Vinte e cinco menos vinte e quatro: delta igual a um."),
    dict(id="s08", block="exemplo1", text="A raiz de um é um. [p=0.2] {a}Menos bê é o oposto de menos cinco: mais cinco. [p=0.2] Embaixo, {b}dois vezes um dá dois. [p=0.3] {c}Com mais: cinco mais um dá seis, dividido por dois dá três. [p=0.2] {d}Com menos: cinco menos um dá quatro, dividido por dois dá dois."),
    dict(id="s09", block="exemplo1", text="Conferindo o três: {a}nove menos quinze mais seis, zero. [p=0.2] O dois: {b}quatro menos dez mais seis, zero. [p=0.2] Bateu."),
    # exemplo 2
    dict(id="s10", block="exemplo2", text="Agora com {a}á negativo: [p=0.2] menos xis ao quadrado mais dois xis mais três igual a zero. [p=0.3] Sem número escrito na frente do xis ao quadrado, o á vale {b}menos um. [p=0.2] {c}Bê vale dois, e cê vale três."),
    dict(id="s11", block="exemplo2", text="Delta: {a}dois ao quadrado, quatro. [p=0.2] Depois, {b}quatro vezes, abre parênteses, menos um, fecha parênteses, vezes três: menos doze. [p=0.3] {c}Quatro menos, abre parênteses, menos doze, fecha parênteses: [p=0.2] tirar uma dívida é ganhar, então {d}quatro mais doze dá dezesseis."),
    dict(id="s12", block="exemplo2", text="A raiz de dezesseis é quatro. [p=0.2] {a}Menos bê: menos dois. [p=0.2] Embaixo: {b}dois vezes menos um, menos dois. [p=0.3] {c}Com mais: menos dois mais quatro dá dois, e dois dividido por menos dois dá menos um. [p=0.2] {d}Com menos: menos dois menos quatro dá menos seis, e menos seis dividido por menos dois dá três."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum está no delta: [p=0.2] {a}usar o á sem o sinal. [p=0.2] A pessoa faz {b}quatro vezes um vezes três, doze, [p=0.2] e o delta sai {c}quatro menos doze: menos oito. [p=0.3] Aí a conta trava, porque {d}nenhum número vezes ele mesmo dá menos oito. [p=0.3] O sinal faz parte do coeficiente: {e}ponha cada um entre parênteses."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}deixe o á positivo antes de começar. [p=0.2] Multiplique a equação inteira por menos um: [p=0.2] {b}xis ao quadrado menos dois xis menos três igual a zero. [p=0.3] {c}Delta: quatro mais doze dá dezesseis. [p=0.2] {d}Dois mais quatro dá seis, dividido por dois dá três. [p=0.2] {e}Dois menos quatro, menos dois, dividido por dois, menos um. [p=0.2] As mesmas raízes."),
    dict(id="s15", block="atalho", text="Funciona porque é a balança: {a}zero vezes menos um continua zero, [p=0.2] então a equação muda de cara, mas não de raízes. [p=0.3] E embaixo fica {b}um número positivo, sem divisão por negativo. [p=0.3] {c}Não compensa quando o á já é positivo: [p=0.2] aí, vá direto para o delta."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Resolva {a}dois xis ao quadrado menos três xis menos dois igual a zero. [p=0.2] Calcule {b}o delta primeiro."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Á vale dois, bê vale menos três, cê vale menos dois. [p=0.3] Delta: {b}abre parênteses, menos três, fecha parênteses, ao quadrado, nove. [p=0.2] {c}Quatro vezes dois vezes, abre parênteses, menos dois, fecha parênteses: menos dezesseis. [p=0.2] {d}Nove menos, abre parênteses, menos dezesseis, fecha parênteses: nove mais dezesseis, delta igual a vinte e cinco."),
    dict(id="s19", block="resposta", text="A raiz é cinco. [p=0.2] Menos bê é {a}três, e embaixo, {b}dois vezes dois dá quatro. [p=0.3] {c}Com mais: oito dividido por quatro dá dois. [p=0.2] {d}Com menos: menos dois dividido por quatro, menos dois quartos, [p=0.2] que simplifica para {e}menos um meio."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}aponte á, bê e cê com o sinal, [p=0.2] {b}calcule o delta primeiro, com parênteses, [p=0.2] e {c}faça a conta com mais e com menos."),
    dict(id="s21", block="fim", text="Na próxima aula, você descobre {a}quantas raízes uma equação tem sem resolver, [p=0.2] só olhando {b}o sinal do delta. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
