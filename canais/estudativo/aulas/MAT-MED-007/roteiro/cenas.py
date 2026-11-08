# Estudativo · MAT-MED-007 — Somar e subtrair horas (Matemática · Medidas e Unidades).
# Habilidade: calcular 3 h 50 min + 2 h 25 min trocando 60 minutos por 1 hora.
# Pré-requisitos: MAT-MED-006 (converter tempo e hora decimal). Próxima: MAT-MED-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Na tela, horas no formato 3 h 50 min.

TITULO = "Somar e subtrair horas"

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
    dict(id="s01", block="gancho", text="{a}Três horas e cinquenta minutos {b}mais duas horas e vinte e cinco minutos. [p=0.3] Somando direto, dá {c}cinco horas e setenta e cinco minutos. [p=0.3] Só que relógio nenhum mostra setenta e cinco minutos."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você soma e subtrai horas sem tropeçar, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}uma coisa: [p=0.2] {b}uma hora tem sessenta minutos. [p=0.2] Por isso, {c}duas horas e quinze minutos são cento e trinta e cinco minutos. [p=0.3] Se faltar essa aula, procure no canal."),
    # somar
    dict(id="s04", block="somar", text="Por que a soma direta não fecha? [p=0.2] Porque minuto {a}não vai até cem. [p=0.3] Ao chegar em {b}sessenta minutos, eles viram {c}uma hora. [p=0.2] É como juntar doze ovos e chamar de uma dúzia."),
    dict(id="s05", block="somar", text="O método tem {a}dois passos. [p=0.3] {b}Passo um: some horas com horas e minutos com minutos. [p=0.2] Três mais dois dá {c}cinco horas. [p=0.2] Cinquenta mais vinte e cinco dá {d}setenta e cinco minutos."),
    dict(id="s06", block="somar", text="{a}Passo dois: se os minutos passarem de sessenta, troque sessenta minutos por uma hora. [p=0.3] Setenta e cinco minutos são {b}sessenta mais quinze. [p=0.2] Os sessenta viram {c}mais uma hora. [p=0.3] Resposta: {d}seis horas e quinze minutos."),
    dict(id="s07", block="somar", text="Dá para conferir pelo caminho da aula anterior: [p=0.2] tudo em minutos. [p=0.2] {a}Duzentos e trinta mais cento e quarenta e cinco, [p=0.2] {b}trezentos e setenta e cinco minutos. [p=0.3] Dividido por sessenta, {c}dá seis e sobram quinze. [p=0.2] {d}Seis horas e quinze minutos de novo."),
    dict(id="s08", block="meianoite", text="E se a soma passar de {a}vinte e quatro horas? [p=0.2] Um plantão começa às {b}vinte e duas horas e trinta minutos [p=0.2] e dura {c}três horas. [p=0.3] Dá {d}vinte e cinco horas e trinta minutos. [p=0.3] Só que o dia tem vinte e quatro horas. [p=0.2] {e}Tire vinte e quatro: [p=0.2] o plantão termina à {f}uma hora e trinta minutos do dia seguinte."),
    # subtrair
    dict(id="s09", block="subtrair", text="Na subtração, a troca é ao contrário. [p=0.2] Uma pessoa entrou no trabalho às {a}duas horas e quarenta minutos da tarde [p=0.2] e saiu às {b}cinco horas e dez minutos. [p=0.3] {c}Quanto tempo ficou lá?"),
    dict(id="s10", block="subtrair", text="A conta é {a}cinco horas e dez minutos, menos duas horas e quarenta minutos. [p=0.3] Dez menos quarenta não dá. [p=0.2] Então {b}desmanche uma hora em sessenta minutos. [p=0.3] Cinco horas e dez minutos viram {c}quatro horas e setenta minutos."),
    dict(id="s11", block="subtrair", text="Agora sim: [p=0.2] {a}setenta menos quarenta dá trinta minutos. [p=0.2] {b}Quatro menos dois dá duas horas. [p=0.3] Ela ficou {c}duas horas e trinta minutos."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}fazer a conta como se fosse número com vírgula. [p=0.3] Na hora de desmanchar, a pessoa {b}empresta cem, em vez de sessenta. [p=0.2] Os dez minutos viram {c}cento e dez, [p=0.2] e a conta dá {d}duas horas e setenta minutos."),
    dict(id="s13", block="erro", text="Isso daria três horas e dez minutos, [p=0.2] {a}quarenta minutos a mais que o certo. [p=0.3] Lembre: {b}uma hora empresta sessenta minutos, nunca cem."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho prometido: {a}complete a hora cheia. [p=0.3] Na soma, três horas e cinquenta minutos {b}precisam de dez minutos para virar quatro horas. [p=0.2] Tire esses dez das duas horas e vinte e cinco. [p=0.2] Sobram {c}duas horas e quinze. [p=0.3] {d}Quatro horas mais duas horas e quinze: seis horas e quinze."),
    dict(id="s15", block="atalho", text="Na subtração, {a}conte para a frente, como o troco no caixa. [p=0.3] De duas e quarenta até as três, {b}são vinte minutos. [p=0.2] Das três até as cinco, {c}são duas horas. [p=0.2] De cinco até cinco e dez, {d}mais dez minutos. [p=0.3] Juntando, {e}duas horas e trinta minutos."),
    dict(id="s16", block="atalho", text="Funciona porque {a}na hora cheia não há troca para fazer. [p=0.3] Não compensa quando são {b}muitas parcelas, como somar o tempo de uma semana inteira. [p=0.2] Aí, {c}some tudo e troque os sessenta no final."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Um ônibus saiu às {a}treze horas e cinquenta minutos [p=0.2] e chegou às {b}dezoito horas e vinte e cinco minutos. [p=0.3] {c}Quanto tempo durou a viagem?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá, pela conta. [p=0.2] Vinte e cinco menos cinquenta não dá. [p=0.2] {a}Desmanche uma hora: dezessete horas e oitenta e cinco minutos. [p=0.3] {b}Oitenta e cinco menos cinquenta dá trinta e cinco. [p=0.2] {c}Dezessete menos treze dá quatro. [p=0.3] {d}Quatro horas e trinta e cinco minutos."),
    dict(id="s20", block="resposta", text="Pelo atalho: [p=0.2] {a}dez minutos até as catorze horas, [p=0.2] {b}quatro horas até as dezoito, [p=0.2] {c}mais vinte e cinco minutos. [p=0.3] Dez mais vinte e cinco dá trinta e cinco minutos: {d}o mesmo resultado, quatro horas e trinta e cinco minutos."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}horas com horas, minutos com minutos, [p=0.2] e {b}a troca é sempre de sessenta."),
    dict(id="s22", block="fim", text="Na próxima aula, você {a}pratica todas as medidas juntas: [p=0.2] {b}comprimento, massa, área, volume e tempo, [p=0.2] com a unidade trocada no meio do problema. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
