# Estudativo · MAT-EXP-005 — Inequação exponencial (Matemática · Exponencial e Logaritmo).
# Habilidade: resolver 2ˣ > 8 e (1/2)ˣ > 8, sabendo que o sentido vira quando a base fica entre 0 e 1.
# Pré-requisitos: MAT-EQU-015 (inequação do 1º grau), MAT-EXP-004 (igualar as bases). Próxima: MAT-EXP-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Inequação exponencial"

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
    dict(id="s01", block="gancho", text="{a}Um meio elevado a xis maior que oito. [p=0.3] Muita gente iguala as bases e escreve {b}xis maior que menos três. [p=0.3] Teste xis igual a zero. [p=0.2] {c}Um meio elevado a zero dá um, que não é maior que oito. [p=0.2] O zero não serve. [p=0.2] Mas {d}zero é maior que menos três. [p=0.2] Alguma coisa deu errado."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve inequações com o xis no expoente, sabe quando o sinal vira [p=0.2] e leva um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de três coisas: [p=0.2] {a}igualar as bases, [p=0.2] {b}o gráfico da exponencial, que sobe com base maior que um e desce com base entre zero e um, [p=0.2] e {c}inequação, com a bolinha na reta. [p=0.3] Se faltar alguma, procure no canal."),
    # base maior que um
    dict(id="s04", block="sobe", text="Comece pela fácil: {a}dois elevado a xis maior que oito. [p=0.2] Oito é {b}dois ao cubo. [p=0.2] Fica {c}dois elevado a xis maior que dois ao cubo."),
    dict(id="s05", block="sobe", text="Base dois, maior que um: a curva {a}sempre sobe. [p=0.2] Expoente maior dá resultado maior. [p=0.2] Então {b}o sinal se mantém: xis maior que três. [p=0.3] Na reta, {c}bolinha aberta no três, porque dois ao cubo dá oito, e oito não é maior que oito. [p=0.2] E {d}pinta para a direita."),
    dict(id="s06", block="sobe", text="No gráfico, trace {a}uma linha deitada na altura oito. [p=0.2] A curva fica acima dela {b}à direita do xis três."),
    # base entre zero e um
    dict(id="s07", block="desce", text="Volte à do começo: {a}um meio elevado a xis maior que oito. [p=0.2] Escreva o oito na base um meio. [p=0.2] Expoente negativo vira fração: [p=0.2] {b}um meio elevado a menos três é um dividido por um oitavo, que dá oito. [p=0.3] Fica {c}um meio elevado a xis maior que um meio elevado a menos três."),
    dict(id="s08", block="desce", text="Base um meio, entre zero e um: a curva {a}sempre desce. [p=0.2] Aqui, expoente {b}menor dá resultado maior. [p=0.2] Então {c}o sinal vira: xis menor que menos três."),
    dict(id="s09", block="desce", text="No gráfico, a curva fica acima da linha do oito {a}à esquerda do menos três. [p=0.3] Teste xis igual a menos quatro. [p=0.2] {b}Um meio elevado a menos quatro dá dezesseis, maior que oito. [p=0.2] Bateu. [p=0.2] E o zero fica de fora, como o teste do começo pedia."),
    dict(id="s10", block="desce", text="A regra, depois de igualar as bases: [p=0.2] {a}base maior que um, mantém o sinal. [p=0.2] {b}Base entre zero e um, vira o sinal."),
    # erro
    dict(id="s11", block="erro", text="Agora, cuidado com o erro oposto: {a}virar o sinal sem precisar. [p=0.2] Veja {b}dois elevado a xis menor que um quarto. [p=0.2] Um quarto é {c}dois elevado a menos dois. [p=0.2] A pessoa vê o menos e vira: {d}xis maior que menos dois."),
    dict(id="s12", block="erro", text="Mas quem manda é a base, e {a}a base é dois, maior que um. [p=0.2] O sinal fica: {b}xis menor que menos dois. [p=0.3] Teste xis igual a zero. [p=0.2] Dois elevado a zero dá um, [p=0.2] e {c}esse um não é menor que um quarto. [p=0.2] O zero não serve, e de fato está fora da resposta certa."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}fuja da base fração. [p=0.2] Um meio é dois elevado a menos um. [p=0.2] Então um meio elevado a xis vira {b}dois elevado a menos xis. [p=0.3] Com base dois, o sinal fica: {c}menos xis maior que três. [p=0.2] Multiplique por menos um e vire o sinal, como numa inequação comum: {d}xis menor que menos três."),
    dict(id="s14", block="atalho", text="Funciona porque a base dois nunca vira o sinal, [p=0.2] e a virada aparece sozinha, {a}no menos do expoente. [p=0.3] Não compensa quando o outro lado já está na base fração, [p=0.2] como em {b}um terço elevado a xis menor que um nono. [p=0.2] Um nono é um terço ao quadrado: [p=0.2] vire o sinal direto, e {c}xis maior que dois."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Resolva as duas e diga se a bolinha é aberta ou fechada. [p=0.2] {a}Três elevado a xis mais um, com o xis mais um todo no expoente, maior ou igual a vinte e sete. [p=0.3] E {b}um quinto elevado a xis maior ou igual a vinte e cinco."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Vinte e sete é três ao cubo. [p=0.2] Base três, maior que um: o sinal fica. [p=0.2] {b}Xis mais um maior ou igual a três, [p=0.2] e {c}xis maior ou igual a dois. [p=0.2] Com o igual, {d}bolinha fechada no dois, pintando para a direita."),
    dict(id="s18", block="resposta", text="Na segunda, vinte e cinco é {a}um quinto elevado a menos dois. [p=0.2] Base um quinto, entre zero e um: {b}vira o sinal. [p=0.2] {c}Xis menor ou igual a menos dois, com bolinha fechada, pintando para a esquerda. [p=0.3] Teste xis igual a zero. [p=0.2] Um quinto elevado a zero dá um, [p=0.2] e {d}esse um não chega a vinte e cinco. [p=0.2] O zero fica de fora. Bateu."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}iguale as bases. [p=0.2] {b}Base maior que um mantém o sinal, [p=0.2] e {c}base entre zero e um vira."),
    dict(id="s20", block="fim", text="Na próxima aula, aparece uma equação em que igualar as bases não basta: [p=0.2] {a}quatro elevado a xis, [p=0.2] menos seis vezes dois elevado a xis, [p=0.2] mais oito, igual a zero. [p=0.3] O truque é {b}chamar dois elevado a xis de ípsilon. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
