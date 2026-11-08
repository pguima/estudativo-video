# Estudativo · MAT-FAT-009 — Discriminante: quantas raízes a equação tem (Matemática · Fatoração e Equação do 2º Grau).
# Habilidade: dizer sem resolver que x² + 2x + 5 = 0 não tem raiz real, que x² − 6x + 9 = 0 tem raiz dupla e achar k = 4 para x² − 4x + k = 0 ter uma raiz só.
# Pré-requisitos: MAT-FAT-008 (Bhaskara, delta), MAT-POT-016 (raiz de negativo não dá número da reta). Próxima: MAT-FAT-010.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; a letra x se escreve "xis"; o coeficiente a se fala "á".

TITULO = "Discriminante: quantas raízes a equação tem"

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
    dict(id="s01", block="gancho", text="{a}Xis ao quadrado mais dois xis mais cinco igual a zero. [p=0.3] Dá para passar um tempão procurando as raízes. [p=0.2] Mas {b}uma conta de cinco segundos [p=0.2] mostra que {c}nenhum número da reta resolve essa equação."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você diz quantas raízes uma equação tem sem resolver, [p=0.2] e acha o número que falta para ela ter {b}uma raiz só."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}o delta: bê ao quadrado menos quatro vezes á vezes cê. [p=0.2] E um fato da raiz: {b}raiz quadrada de número negativo não dá número da reta. [p=0.3] Se faltar alguma, procure no canal."),
    # ideia
    dict(id="s04", block="ideia", text="Olhe de novo a fórmula de Bhaskara: [p=0.2] {a}menos bê, mais ou menos raiz de delta, dividido por dois á. [p=0.3] Tudo depende do que acontece com {b}a raiz de delta. [p=0.2] Por isso, o delta também se chama {c}discriminante: ele separa os casos."),
    # positivo
    dict(id="s05", block="positivo", text="{a}Delta positivo: a raiz existe e não é zero. [p=0.2] Somar e subtrair dão resultados diferentes: {b}duas raízes diferentes. [p=0.3] Foi o que aconteceu em xis ao quadrado menos cinco xis mais seis: [p=0.2] {c}delta igual a um, raízes dois e três."),
    # zero
    dict(id="s06", block="zero", text="{a}Delta zero: a raiz de zero é zero. [p=0.2] Mais zero e menos zero dão o mesmo: {b}uma raiz só, que se chama raiz dupla. [p=0.3] Veja {c}xis ao quadrado menos seis xis mais nove igual a zero. [p=0.2] {d}Trinta e seis menos trinta e seis: delta zero. [p=0.2] A raiz é {e}seis dividido por dois dá três."),
    dict(id="s07", block="zero", text="Faz sentido: esse é um {a}trinômio quadrado perfeito. [p=0.2] É {b}xis menos três, ao quadrado. [p=0.3] Os dois fatores são o mesmo parêntese, [p=0.2] e {c}os fatores dão a mesma raiz, repetida."),
    # negativo
    dict(id="s08", block="negativo", text="{a}Delta negativo: a raiz de delta não dá número da reta. [p=0.2] Os números da reta se chamam {b}números reais. [p=0.2] Então a equação {c}não tem raiz real. [p=0.3] No gancho: {d}quatro menos vinte, menos dezesseis. [p=0.2] {e}Nenhuma raiz real, e você nem precisou da fórmula inteira."),
    # quadro
    dict(id="s09", block="quadro", text="Em resumo: {a}delta positivo, duas raízes reais. [p=0.2] {b}Delta zero, uma raiz, a dupla. [p=0.2] {c}Delta negativo, nenhuma."),
    # ká
    dict(id="s10", block="k", text="E a questão que inverte o jogo: [p=0.2] {a}para que valor de ká a equação xis ao quadrado menos quatro xis mais ká igual a zero tem uma raiz só? [p=0.3] {b}Ká é um número desconhecido, no lugar do cê."),
    dict(id="s11", block="k", text="Uma raiz só é {a}delta igual a zero. [p=0.2] {b}Bê ao quadrado: dezesseis. [p=0.2] {c}Quatro vezes um vezes ká: quatro ká. [p=0.3] {d}Dezesseis menos quatro ká igual a zero. [p=0.2] Na balança: {e}quatro ká igual a dezesseis, e ká igual a quatro."),
    dict(id="s12", block="k", text="Conferindo: {a}xis ao quadrado menos quatro xis mais quatro é xis menos dois, ao quadrado. [p=0.2] {b}Uma raiz só, o dois."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é achar que {a}delta zero quer dizer nenhuma raiz. [p=0.2] Zero parece nada. [p=0.3] Mas em xis ao quadrado menos seis xis mais nove, {b}o três resolve: nove menos dezoito mais nove, zero. [p=0.2] {c}Delta zero é uma raiz. [p=0.2] Nenhuma raiz é {d}delta negativo."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}se á e cê têm sinais contrários, o delta é positivo, sem conta. [p=0.3] Em {b}dois xis ao quadrado mais sete xis menos três igual a zero, [p=0.2] á é positivo e cê é negativo: {c}duas raízes reais."),
    dict(id="s15", block="atalho", text="Funciona porque {a}á vezes cê fica negativo, [p=0.2] e o menos da fórmula transforma a subtração numa {b}soma. [p=0.2] Bê ao quadrado nunca é negativo, então o delta {c}passa de zero. [p=0.3] {d}Com sinais iguais, o atalho não decide: [p=0.2] aí, calcule o delta."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Sem resolver, diga quantas raízes reais tem cada uma: [p=0.2] {a}xis ao quadrado menos quatro xis mais cinco igual a zero, [p=0.2] e {b}xis ao quadrado mais dez xis mais vinte e cinco igual a zero. [p=0.3] Depois, {c}ache ká para que xis ao quadrado mais seis xis mais ká igual a zero tenha uma raiz só."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Na primeira, {a}dezesseis menos vinte, menos quatro: [p=0.2] {b}nenhuma raiz real. [p=0.3] Na segunda, {c}cem menos cem dá zero: [p=0.2] {d}uma raiz, a dupla: menos dez dividido por dois, menos cinco."),
    dict(id="s19", block="resposta", text="Na última, {a}trinta e seis menos quatro ká igual a zero. [p=0.2] {b}Quatro ká igual a trinta e seis: [p=0.2] {c}ká igual a nove. [p=0.3] E fica {d}xis mais três, ao quadrado."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}calcule só o delta [p=0.2] e {b}olhe o sinal dele."),
    dict(id="s21", block="fim", text="Na próxima aula, o delta é positivo, mas {a}não tem raiz exata, [p=0.2] como em {b}xis, vezes o parêntese xis menos dois, igual a um, [p=0.2] e a resposta fica {c}com raiz. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
