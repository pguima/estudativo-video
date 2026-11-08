# Estudativo · MAT-TOP-002 — Binômio de Newton (Matemática · Tópicos Avançados · Binômio, distribuição binomial e casa dos pombos).
# Habilidade: expandir (x + 2)⁴ com o triângulo de Pascal e achar o coeficiente de x², 24, pelo termo geral.
# Pré-requisitos: MAT-FAT-015 (cubo da soma pelo chuveirinho), MAT-TOP-001 (binomiais e triângulo de Pascal). Próxima: MAT-TOP-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Leitura de parênteses como na MAT-FAT-015 ("abre parênteses, xis mais dois, fecha parênteses").
# Sem binômio com sinal de menos: potência de negativo (MAT-POT-002) não está na ficha desta aula.

TITULO = "Binômio de Newton"

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
    dict(id="s01", block="gancho", text="{a}Abre parênteses, xis mais dois, fecha parênteses, elevado a quatro. [p=0.3] Pelo chuveirinho, são {b}quatro parênteses multiplicados, [p=0.2] e muita conta para errar. [p=0.3] Com {c}uma linha do triângulo de Pascal, [p=0.2] {d}você escreve a resposta direto."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você abre uma soma de dois termos elevada a quatro, a cinco, a seis, [p=0.2] acha {b}um termo sozinho [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}duas coisas: [p=0.2] {b}o triângulo de Pascal, em que cada número é a soma dos dois de cima, [p=0.2] e {c}o cubo da soma: xis mais um, ao cubo, dá xis ao cubo mais três xis ao quadrado mais três xis mais um. [p=0.3] Se faltar alguma, procure no canal."),
    # o padrão
    dict(id="s04", block="padrao", text="Binômio é {a}uma soma de dois termos, como á mais bê. [p=0.2] Repare no número da frente de cada termo, o {b}coeficiente. [p=0.3] {c}Á mais bê, ao quadrado: um, dois, um. [p=0.2] {d}Ao cubo: um, três, três, um. [p=0.3] {e}São as linhas dois e três do triângulo de Pascal."),
    dict(id="s05", block="padrao", text="Por que o triângulo aparece? [p=0.2] No cubo, você multiplica {a}três parênteses iguais. [p=0.2] Cada termo da resposta {b}pega uma letra de cada parêntese. [p=0.3] Para formar á ao quadrado vezes bê, {c}o bê vem de um dos três parênteses: [p=0.2] {d}três jeitos de escolher. [p=0.2] Por isso o três na frente: {e}é o binomial de três sobre um."),
    dict(id="s06", block="padrao", text="A regra para á mais bê, elevado a ene: [p=0.2] {a}os coeficientes vêm da linha ene. [p=0.2] {b}O expoente do á começa em ene e desce de um em um. [p=0.2] {c}O expoente do bê começa em zero e sobe. [p=0.3] Em cada termo, {d}os dois expoentes somam ene."),
    # exemplo
    dict(id="s07", block="exemplo", text="Agora, {a}xis mais dois, elevado a quatro. [p=0.2] Aqui, {b}á é xis e bê é dois. [p=0.2] A linha quatro é {c}um, quatro, seis, quatro, um."),
    dict(id="s08", block="exemplo", text="{a}Um vezes xis elevado a quatro: xis elevado a quatro. [p=0.2] {b}Quatro vezes xis ao cubo vezes dois: oito xis ao cubo. [p=0.2] {c}Seis vezes xis ao quadrado vezes dois ao quadrado, que é quatro: [p=0.2] vinte e quatro xis ao quadrado."),
    dict(id="s09", block="exemplo", text="{a}Quatro vezes xis vezes dois ao cubo, que é oito: trinta e dois xis. [p=0.2] {b}Um vezes dois elevado a quatro: dezesseis. [p=0.3] {c}Pronto, sem multiplicar nenhum parêntese."),
    # termo geral
    dict(id="s10", block="termo", text="E se a prova pedir {a}só o coeficiente de xis ao quadrado? [p=0.2] Não precisa abrir tudo. [p=0.3] Use o {b}termo geral: [p=0.2] {c}o binomial de ene sobre cá, [p=0.2] vezes {d}á elevado a, abre parênteses, ene menos cá, fecha parênteses, [p=0.2] vezes {e}bê elevado a cá. [p=0.3] {f}Cá é quantas vezes o bê foi escolhido."),
    dict(id="s11", block="termo", text="Para ter xis ao quadrado, {a}o expoente do xis, quatro menos cá, tem que dar dois. [p=0.2] Então {b}cá vale dois. [p=0.3] {c}Binomial de quatro sobre dois é seis. [p=0.2] {d}Dois ao quadrado é quatro. [p=0.2] {e}Seis vezes quatro: vinte e quatro."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}copiar só o número do triângulo. [p=0.2] A pessoa vê o seis na linha quatro e responde {b}seis xis ao quadrado. [p=0.3] Esqueceu que o dois {c}também entra, elevado ao quadrado. [p=0.2] {d}Seis vezes quatro dá vinte e quatro. [p=0.2] Quando o bê não é um, {e}ele muda os coeficientes."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, para conferir a conta: [p=0.2] {a}troque o xis por um. [p=0.2] {b}Um mais dois dá três, e três elevado a quatro dá oitenta e um. [p=0.3] Do outro lado, {c}um mais oito mais vinte e quatro mais trinta e dois mais dezesseis [p=0.2] também dá {d}oitenta e um. [p=0.2] Bateu."),
    dict(id="s14", block="atalho", text="Funciona porque, com xis igual a um, {a}todo xis vira um, e sobra a soma dos coeficientes. [p=0.3] Se der diferente, {b}tem erro em algum termo. [p=0.2] {c}Mas a soma não acha um coeficiente sozinho: [p=0.2] para isso, use o termo geral."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Em {a}xis mais três, elevado a cinco, [p=0.2] {b}qual é o coeficiente de xis ao cubo? [p=0.2] E {c}quanto dá a soma de todos os coeficientes?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] O expoente do xis é {a}cinco menos cá. [p=0.2] Para dar três, {b}cá vale dois. [p=0.3] {c}Binomial de cinco sobre dois é dez. [p=0.2] {d}Três ao quadrado é nove. [p=0.2] {e}Dez vezes nove: noventa. [p=0.2] O termo é {f}noventa xis ao cubo."),
    dict(id="s18", block="resposta", text="E a soma: troque o xis por um. [p=0.2] {a}Um mais três dá quatro. [p=0.2] {b}Quatro elevado a cinco dá mil e vinte e quatro."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}os coeficientes vêm do triângulo, [p=0.2] {b}os expoentes trocam de um em um, [p=0.2] e {c}o segundo termo entra elevado, com o número dele."),
    dict(id="s20", block="fim", text="Na próxima aula, o mesmo binomial calcula {a}chances: [p=0.2] por exemplo, a de sair {b}exatamente duas caras em cinco lançamentos de uma moeda. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
