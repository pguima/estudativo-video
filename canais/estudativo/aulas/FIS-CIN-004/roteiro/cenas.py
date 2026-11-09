# Estudativo · FIS-CIN-004 — Referencial, posição e deslocamento (Física · Cinemática · Movimento uniforme e variado).
# Habilidade: dizer se um corpo está parado ou em movimento conforme o referencial e separar distância percorrida de deslocamento.
# Pré-requisitos: FIS-CIN-001 (escalar e vetorial), MAT-NUM-016 (inteiros). Próxima: FIS-CIN-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. FIS-CIN-002 (soma de vetores) NÃO está em "Já ensinado": tudo em uma reta só.
# O delta é apresentado aqui (MAT-FUN-010 não está na lista). "menos (−20)" narrado com "abre parênteses".

TITULO = "Referencial, posição e deslocamento"

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
    dict(id="s01", block="gancho", text="{a}Você está sentado num ônibus que anda pela avenida. [p=0.3] Você está {b}parado [p=0.1] ou {c}em movimento? [p=0.3] {d}As duas respostas estão certas. [p=0.2] Depende de {e}quem olha."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai dizer se um corpo está parado ou em movimento, [p=0.2] e separar {b}a distância que ele percorre [p=0.1] do {c}deslocamento."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}grandeza vetorial, a que tem direção e sentido; [p=0.2] e {c}subtrair números inteiros, inclusive negativos. [p=0.3] Se faltar alguma, procure no canal."),
    # referencial
    dict(id="s04", block="referencial", text="{a}Para o motorista, você está parado: [p=0.2] a distância entre vocês {b}não muda. [p=0.3] {c}Para quem está na calçada, você passa em movimento: [p=0.2] a distância até essa pessoa {d}muda a cada segundo."),
    dict(id="s05", block="referencial", text="Quem olha se chama {a}referencial: [p=0.2] o corpo usado como base para medir as posições. [p=0.3] {b}Movimento é a posição mudando com o tempo, em relação ao referencial. [p=0.2] {c}Repouso é a posição que não muda. [p=0.3] Por isso, {d}não existe parado sem dizer em relação a quê. [p=0.2] Até a calçada se move, junto com a Terra, que gira."),
    # posição
    dict(id="s06", block="posicao", text="Para medir a posição, a Física usa {a}uma reta com números, como os marcos de uma estrada. [p=0.2] {b}O zero é a origem, e você escolhe onde ele fica. [p=0.2] {c}A posição é o número onde o corpo está, com a unidade: [p=0.1] {d}o carro está no quilômetro trinta. [p=0.3] {e}Do outro lado da origem, a posição é negativa. [p=0.2] {f}A posição se representa pela letra esse."),
    # deslocamento
    dict(id="s07", block="deslocamento", text="{a}Deslocamento é a mudança de posição: [p=0.2] {b}a posição final menos a inicial. [p=0.3] Ele se escreve {c}delta esse. [p=0.2] O triângulo delta quer dizer variação: [p=0.1] {d}final menos inicial. [p=0.3] Um carro vai do {e}quilômetro trinta ao {f}quilômetro oitenta. [p=0.2] {g}Oitenta menos trinta: o deslocamento é de cinquenta quilômetros."),
    dict(id="s08", block="deslocamento", text="E se ele voltar do quilômetro oitenta ao trinta? [p=0.2] {a}Trinta menos oitenta dá menos cinquenta. [p=0.3] {b}O sinal de menos não é erro: [p=0.2] diz que ele andou {c}no sentido em que os números diminuem. [p=0.2] É o sentido do deslocamento, que é uma grandeza vetorial."),
    # distância
    dict(id="s09", block="distancia", text="Agora, {a}a distância percorrida: [p=0.2] é tudo o que o carro andou, {b}somando cada trecho, [p=0.2] como marca o contador de quilômetros do painel, o hodômetro. [p=0.3] Ela {c}nunca é negativa."),
    dict(id="s10", block="distancia", text="Veja a diferença. [p=0.2] O carro sai do {a}quilômetro trinta, [p=0.1] vai até o {b}oitenta [p=0.1] e volta até o {c}cinquenta. [p=0.3] {d}Andou cinquenta na ida e trinta na volta: [p=0.2] {e}distância percorrida, oitenta quilômetros. [p=0.3] Mas o deslocamento só olha o começo e o fim: [p=0.2] {f}cinquenta menos trinta, vinte quilômetros."),
    dict(id="s11", block="distancia", text="{a}Numa volta completa numa pista de atletismo de quatrocentos metros, [p=0.2] o atleta percorre {b}quatrocentos metros, [p=0.2] e o deslocamento é {c}zero: [p=0.2] ele termina onde começou."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: {a}confundir a posição com o quanto o carro andou. [p=0.3] O carro {b}está no quilômetro oitenta. [p=0.2] A pessoa diz que ele {c}andou oitenta quilômetros. [p=0.3] Mas ele saiu do quilômetro trinta: [p=0.2] {d}andou cinquenta. [p=0.2] {e}O quilômetro oitenta é só o endereço."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}para o deslocamento, ignore o caminho: [p=0.2] {b}só final menos inicial. [p=0.3] {c}Para a distância, corte o caminho em cada ponto onde o corpo vira, [p=0.2] e {d}some os trechos, todos positivos."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o deslocamento só depende de onde o corpo começou e de onde terminou. [p=0.3] {b}Não compensa cortar quando o corpo nunca volta: [p=0.2] aí, {c}a distância é o próprio deslocamento, sem o sinal, [p=0.1] e uma conta só resolve as duas."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Numa pista reta, um corredor sai da posição {a}menos vinte metros, [p=0.2] corre até a posição {b}sessenta [p=0.1] e volta até a posição {c}quarenta. [p=0.3] {d}Qual é a distância percorrida? [p=0.2] {e}E o deslocamento?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Ele vira na posição sessenta, então são {a}dois trechos. [p=0.2] {b}Na ida, de menos vinte até sessenta: [p=0.1] oitenta metros. [p=0.2] {c}Na volta, de sessenta até quarenta: vinte metros. [p=0.2] {d}Distância: oitenta mais vinte, cem metros."),
    dict(id="s18", block="resposta", text="O deslocamento só olha o começo e o fim: [p=0.2] {a}quarenta menos, abre parênteses, menos vinte, fecha parênteses. [p=0.2] Tirar uma dívida é ganhar: [p=0.1] {b}quarenta mais vinte, [p=0.1] {c}sessenta metros."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}movimento depende do referencial; [p=0.2] {b}deslocamento é final menos inicial; [p=0.2] {c}distância é a soma de tudo o que se andou."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai escrever numa fórmula {a}a posição de um corpo com velocidade constante: [p=0.2] {b}a função horária do movimento uniforme. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
