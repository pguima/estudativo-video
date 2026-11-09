# Estudativo · FIS-CAL-005 — Trocas de calor no calorímetro (Física · Calor e Termodinâmica · Calorimetria e mudanças de estado).
# Habilidade: usar soma dos calores igual a zero e, quando os dois corpos são da mesma substância, o atalho da média ponderada
# pelas massas para achar a temperatura final.
# Pré-requisitos: FIS-CAL-003 (Q = m·c·ΔT e sinal), MAT-EST-009 (média ponderada). Próxima: FIS-CAL-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita.
# Calor latente (FIS-CAL-004) não está em "Já ensinado": nenhuma troca desta aula muda de estado. O calorímetro é ideal
# (não troca calor com o corpo dos recipientes nem com o ambiente). Metal com c = 0,1 cal/(g·°C), valor redondo de exercício.

TITULO = "Trocas de calor no calorímetro"

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
    dict(id="s01", block="gancho", text="{a}Duzentos gramas de água a oitenta graus [p=0.1] com {b}trezentos gramas de água a vinte. [p=0.3] Muita gente responde {c}cinquenta graus, a média. [p=0.3] {d}Errado. [p=0.2] A mistura fica em {e}quarenta e quatro."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai achar a temperatura final de qualquer mistura assim, [p=0.2] e ainda leva {b}um atalho que resolve de cabeça."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}quê igual a eme cê delta tê, [p=0.1] com quê negativo quando o corpo cede calor; [p=0.2] e {c}a média ponderada, a média com pesos. [p=0.3] Se faltar alguma, procure no canal."),
    # calorímetro
    dict(id="s04", block="calorimetro", text="{a}Um calorímetro é um recipiente isolado, [p=0.1] como uma garrafa térmica. [p=0.3] {b}O calor não entra nem sai dele. [p=0.3] Dentro, {c}o corpo quente cede calor [p=0.1] e {d}o frio recebe, [p=0.2] até os dois chegarem à {e}mesma temperatura: o equilíbrio térmico."),
    dict(id="s05", block="calorimetro", text="Como nada escapa, {a}todo o calor que o quente cede, o frio recebe. [p=0.3] O cedido tem sinal de menos, [p=0.2] o recebido, de mais. [p=0.3] Então, somando o cedido e o recebido, {b}dá zero. [p=0.2] {c}A soma dos calores é igual a zero."),
    # exemplo
    dict(id="s06", block="exemplo", text="Vamos ao gancho. [p=0.2] Chame a temperatura final de {a}tê. [p=0.3] {b}Água quente: duzentos, vezes um, vezes a variação, tê menos oitenta. [p=0.2] {c}Água fria: trezentos, vezes um, vezes a variação, tê menos vinte. [p=0.3] {d}A soma é zero."),
    dict(id="s07", block="exemplo", text="Faça a distributiva: [p=0.2] {a}duzentos tê menos dezesseis mil, [p=0.1] {b}mais trezentos tê menos seis mil, [p=0.1] igual a zero. [p=0.3] {c}Quinhentos tê igual a vinte e dois mil. [p=0.2] {d}Tê igual a quarenta e quatro graus Celsius."),
    dict(id="s08", block="exemplo", text="Repare: {a}quarenta e quatro fica entre vinte e oitenta. [p=0.2] Sempre fica. [p=0.3] E fica {b}mais perto de vinte, [p=0.2] porque {c}tem mais água fria do que quente."),
    # atalho
    dict(id="s09", block="atalho", text="Agora, o atalho: [p=0.2] se os dois corpos são {a}da mesma substância, [p=0.2] a temperatura final é {b}a média ponderada das temperaturas, com as massas como pesos."),
    dict(id="s10", block="atalho", text="{a}Duzentos vezes oitenta dá dezesseis mil. [p=0.2] {b}Trezentos vezes vinte dá seis mil. [p=0.2] {c}A soma dá vinte e dois mil, [p=0.1] {d}que se divide pela massa total, quinhentos: [p=0.2] {e}quarenta e quatro. [p=0.3] Sem equação."),
    dict(id="s11", block="atalho", text="Funciona porque, com o mesmo cê, {a}o calor específico corta dos dois lados. [p=0.3] {b}Não serve com substâncias diferentes, [p=0.2] porque aí o cê não corta. [p=0.2] Nesse caso, use a soma igual a zero."),
    # substâncias diferentes
    dict(id="s12", block="diferentes", text="Veja um caso assim. [p=0.2] {a}Duzentos gramas de um metal a cem graus, [p=0.1] com calor específico {b}zero vírgula um, [p=0.2] caem em {c}cento e oitenta gramas de água a vinte."),
    dict(id="s13", block="diferentes", text="{a}Metal: duzentos, vezes zero vírgula um, vezes a variação, tê menos cem. [p=0.2] {b}Água: cento e oitenta, vezes um, vezes a variação, tê menos vinte. [p=0.3] Fica {c}vinte tê menos dois mil, [p=0.1] mais cento e oitenta tê menos três mil e seiscentos, [p=0.1] igual a zero."),
    dict(id="s14", block="diferentes", text="{a}Duzentos tê igual a cinco mil e seiscentos. [p=0.2] {b}Tê igual a vinte e oito graus. [p=0.3] O metal estava a cem, mas a água quase não esquentou: [p=0.2] {c}o cê da água é dez vezes maior."),
    # erro
    dict(id="s15", block="erro", text="O erro do gancho é {a}a média simples: [p=0.2] {b}oitenta mais vinte, dividido por dois, cinquenta. [p=0.3] Ela só vale {c}com massas iguais da mesma substância. [p=0.3] Com trezentos gramas de água fria e duzentos de quente, [p=0.2] {d}a fria puxa a temperatura para baixo."),
    dict(id="s16", block="erro", text="{a}Com massas iguais, aí sim: [p=0.2] cem gramas a oitenta com cem gramas a vinte dão {b}cinquenta. [p=0.3] Na média ponderada, os pesos são iguais, [p=0.2] e ela vira {c}a média simples. [p=0.3] Ou seja: {d}com a mesma substância, a média ponderada nunca erra; [p=0.1] a simples só acerta com massas iguais."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Num calorímetro, você mistura {a}trezentos gramas de água a noventa graus [p=0.1] com {b}cem gramas de água a dez graus. [p=0.3] {c}Qual é a temperatura final?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Mesma substância, então {a}média ponderada. [p=0.2] {b}Trezentos vezes noventa dá vinte e sete mil. [p=0.2] {c}Cem vezes dez dá mil. [p=0.2] {d}A soma dá vinte e oito mil, [p=0.1] {e}que se divide por quatrocentos: [p=0.2] {f}setenta graus Celsius. [p=0.3] Mais perto de noventa, porque tem mais água quente."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}no calorímetro, a soma dos calores é zero; [p=0.2] {b}mesma substância, média ponderada pelas massas; [p=0.2] e {c}a temperatura final fica entre as duas, mais perto de quem tem mais."),
    dict(id="s21", block="fim", text="Na próxima aula, entra {a}gelo na mistura, [p=0.2] e você vai decidir, {b}antes de qualquer conta, [p=0.1] se ele derrete todo ou não. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
