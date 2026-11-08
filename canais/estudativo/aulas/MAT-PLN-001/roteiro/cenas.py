# Estudativo · MAT-PLN-001 — O que é polinômio: grau, valor e operações (Matemática · Polinômios · Operações e divisão de polinômios).
# Habilidade: dizer que 2x³ − x + 5 tem grau 3, calcular P(2) = 19, somar e multiplicar polinômios e achar a e b em ax + b ≡ 3x − 2.
# Pré-requisitos: MAT-EQU-002 (valor numérico, sempre com parênteses), MAT-FAT-003 (produtos notáveis). Próxima: MAT-PLN-002.
# A notação f(x) (MAT-FUN-003) não está na ficha: P(x) é apresentado do zero. Equação (MAT-EQU-007) também não: a identidade
# é lida termo a termo, sem resolver nada. Questão inédita, criada para esta aula.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis"; a, b, c se falam "á, bê, cê".

TITULO = "O que é polinômio: grau, valor e operações"

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
    dict(id="s01", block="gancho", text="{a}Cinco xis ao quadrado mais xis ao cubo. [p=0.3] Qual é o grau dessa expressão? [p=0.3] Se você disse {b}dois, olhou só o primeiro termo. [p=0.2] Se disse {c}cinco, olhou o número da frente. [p=0.3] O grau é {d}três."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você entende o que é um polinômio, calcula o valor dele, soma e multiplica, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}três coisas: [p=0.2] {b}trocar a letra por um número entre parênteses, [p=0.2] {c}juntar termos semelhantes, com a mesma letra e o mesmo expoente, [p=0.2] e {d}o chuveirinho: cada termo de um parêntese multiplica cada termo do outro. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="oque", text="Um polinômio é {a}uma soma de termos. [p=0.2] Cada termo é {b}um número vezes uma potência de xis, [p=0.2] e o expoente do xis é sempre {c}um número inteiro, sem sinal de menos. [p=0.3] Também pode ter {d}um número sozinho, sem xis."),
    dict(id="s05", block="oque", text="Em {a}dois xis ao cubo menos xis mais cinco, [p=0.2] o número que multiplica cada potência se chama {b}coeficiente. [p=0.2] Repare: {c}menos xis tem coeficiente menos um, escondido. [p=0.3] E {d}o cinco, sem xis, é o termo independente."),
    dict(id="s06", block="oque", text="Já {a}um dividido por xis não é polinômio, [p=0.2] porque {b}o xis está embaixo da fração."),
    # grau
    dict(id="s07", block="grau", text="O {a}grau de um polinômio é o maior expoente do xis. [p=0.2] Em dois xis ao cubo menos xis mais cinco, [p=0.2] o maior expoente é {b}três: grau três. [p=0.3] E no gancho, {c}cinco xis ao quadrado mais xis ao cubo também tem grau três. [p=0.2] {d}A ordem dos termos não importa, [p=0.2] e {e}o número da frente não conta."),
    # valor
    dict(id="s08", block="valor", text="Para dar nome a um polinômio, escreva {a}P de xis igual a ele. [p=0.2] O P é de polinômio, e o xis entre parênteses avisa qual é a letra. [p=0.3] {b}P de dois é o valor do polinômio quando xis vale dois: [p=0.2] o valor numérico que você já sabe calcular."),
    dict(id="s09", block="valor", text="{a}Dois vezes, abre parênteses, dois, fecha parênteses, ao cubo, [p=0.2] menos, abre parênteses, dois, fecha parênteses, mais cinco. [p=0.3] {b}Dois ao cubo dá oito, e dois vezes oito, dezesseis. [p=0.2] {c}Dezesseis menos dois mais cinco: [p=0.2] {d}P de dois é igual a dezenove."),
    # somar
    dict(id="s10", block="somar", text="Somar polinômios é {a}juntar os termos semelhantes. [p=0.2] Some {b}dois xis ao cubo menos xis mais cinco [p=0.2] com {c}xis ao cubo mais quatro xis menos um."),
    dict(id="s11", block="somar", text="{a}Xis ao cubo com xis ao cubo: dois mais um, três xis ao cubo. [p=0.2] {b}Xis com xis: menos um mais quatro, três xis. [p=0.2] {c}Número com número: cinco menos um, quatro. [p=0.3] Resultado: {d}três xis ao cubo mais três xis mais quatro."),
    # multiplicar
    dict(id="s12", block="multiplicar", text="Para multiplicar, {a}use o chuveirinho. [p=0.2] Veja {b}xis mais dois, vezes xis ao quadrado menos três. [p=0.3] {c}Xis vezes xis ao quadrado: xis ao cubo. [p=0.2] {d}Xis vezes menos três: menos três xis. [p=0.2] {e}Dois vezes xis ao quadrado: dois xis ao quadrado. [p=0.2] {f}Dois vezes menos três: menos seis."),
    dict(id="s13", block="multiplicar", text="Em ordem de expoente: {a}xis ao cubo mais dois xis ao quadrado menos três xis menos seis. [p=0.3] Repare no grau: {b}o primeiro tinha grau um, o segundo, grau dois, [p=0.2] e o resultado tem grau três. [p=0.2] {c}Na multiplicação, os graus somam."),
    # identidade
    dict(id="s14", block="identidade", text="Dois polinômios são {a}idênticos quando dão o mesmo valor para qualquer xis. [p=0.2] Isso acontece quando {b}os coeficientes são iguais, termo a termo. [p=0.3] O símbolo é {c}parecido com o de igual, mas com três tracinhos."),
    dict(id="s15", block="identidade", text="Se {a}á xis mais bê é idêntico a três xis menos dois, [p=0.2] compare termo a termo. [p=0.2] {b}O que acompanha o xis: á igual a três. [p=0.2] {c}O número sozinho: bê igual a menos dois."),
    dict(id="s16", block="identidade", text="E se faltar um termo? [p=0.2] Em {a}á xis ao quadrado mais bê xis mais cê, idêntico a quatro xis ao quadrado menos sete, [p=0.2] {b}á vale quatro e cê vale menos sete. [p=0.2] E o bê? [p=0.2] {c}Do lado direito, não tem xis: é como ter zero xis. [p=0.2] {d}Bê igual a zero."),
    # erro
    dict(id="s17", block="erro", text="Cuidado com um erro muito comum na soma: [p=0.2] {a}somar os expoentes. [p=0.2] A pessoa escreve xis ao cubo mais xis ao cubo como {b}dois xis elevado a seis. [p=0.3] Teste com xis igual a dois: [p=0.2] {c}oito mais oito dá dezesseis. [p=0.2] Mas {d}dois elevado a seis é sessenta e quatro, e vezes dois, cento e vinte e oito."),
    dict(id="s18", block="erro", text="{a}Na soma, o expoente fica igual, e só os coeficientes somam. [p=0.2] {b}É na multiplicação que os expoentes somam."),
    # atalho
    dict(id="s19", block="atalho", text="Agora o atalho: {a}P de um é a soma dos coeficientes. [p=0.3] Em dois xis ao cubo menos xis mais cinco, [p=0.2] {b}dois menos um mais cinco: P de um é seis. [p=0.3] Funciona porque {c}um elevado a qualquer expoente dá um: [p=0.2] cada termo vira só o seu coeficiente."),
    dict(id="s20", block="atalho", text="Ele brilha quando o polinômio vem {a}multiplicado e você não quer abrir. [p=0.2] A soma dos coeficientes de {b}xis mais dois, vezes xis ao quadrado menos três: [p=0.2] troque o xis por um, e dá {c}três vezes menos dois, menos seis. [p=0.3] Aberto, dá {d}um mais dois menos três menos seis: menos seis também. [p=0.3] {e}Para outro valor de xis, não tem atalho: faça a conta inteira."),
    # questão
    dict(id="s21", block="questao", text="Hora de testar. [p=0.2] Com {a}P de xis igual a três xis ao quadrado menos cinco xis mais um, [p=0.2] calcule {b}P de menos um [p=0.2] e {c}a soma dos coeficientes."),
    dict(id="s22", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s23", block="resposta", text="Vamos lá. [p=0.2] {a}Três vezes, abre parênteses, menos um, fecha parênteses, ao quadrado, [p=0.2] menos cinco vezes, abre parênteses, menos um, fecha parênteses, mais um. [p=0.3] {b}Menos um ao quadrado dá um: três vezes um, três. [p=0.2] {c}Menos cinco vezes menos um dá mais cinco. [p=0.2] {d}Três mais cinco mais um: P de menos um é nove."),
    dict(id="s24", block="resposta", text="A soma dos coeficientes é {a}P de um: [p=0.2] {b}três menos cinco mais um, menos um. [p=0.3] Sem parênteses no quadrado, o menos um ao quadrado {c}viraria menos um, [p=0.2] e o nove viraria {d}três."),
    # fechamento
    dict(id="s25", block="fim", text="Resumindo: {a}o grau é o maior expoente, [p=0.2] {b}P de um número é trocar o xis por ele, [p=0.2] e {c}somar e multiplicar é o que você já fazia com letras."),
    dict(id="s26", block="fim", text="Na próxima aula, você {a}divide polinômios, [p=0.2] com quociente e resto, [p=0.2] e acha {b}o resto sem dividir. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
