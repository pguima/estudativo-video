# Estudativo · FIS-DIN-001 — Força resultante e primeira lei: inércia (Física · Dinâmica · Leis de Newton).
# Habilidade: somar as forças sobre um corpo e explicar por que ele segue parado ou em linha reta quando a resultante é zero,
# como no cinto de segurança.
# Pré-requisitos: FIS-CIN-002 (somar vetores), FIS-CIN-005 (movimento uniforme). Próxima: FIS-DIN-002.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Primeira aula da trilha de Dinâmica: o cabeçalho do visual.py guarda a linguagem visual das forças.
# Aceleração (FIS-CIN-007) e F = m·a (FIS-DIN-002) não estão em "Já ensinado": a aula fala só em "mudar a velocidade" e deixa
# a conta para a próxima. Atrito é citado como assunto de outra aula. Newton é dito como a unidade; a definição fica na próxima.

TITULO = "Força resultante e primeira lei: inércia"

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
    dict(id="s01", block="gancho", text="{a}O ônibus freia de repente [p=0.2] e você {b}é jogado para a frente. [p=0.3] Mas repare: {c}ninguém empurrou você. [p=0.3] Então, o que aconteceu?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}somar as forças sobre um corpo [p=0.2] e explicar por que ele {c}continua parado ou em linha reta, [p=0.2] como no {d}cinto de segurança."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}somar vetores, que você já fez com o barco no rio; [p=0.2] e o {c}movimento uniforme, em linha reta e com a mesma velocidade o tempo todo. [p=0.3] Se faltar alguma, procure no canal."),
    # força
    dict(id="s04", block="forca", text="{a}Força é um empurrão ou um puxão. [p=0.3] E ela é {b}vetorial: [p=0.2] tem módulo, direção e sentido. [p=0.3] Empurrar uma porta {c}para dentro ou {d}para fora dá resultados opostos."),
    dict(id="s05", block="forca", text="A unidade de força no esse i é o {a}newton, de símbolo {b}ene maiúsculo. [p=0.3] Para ter uma ideia, {c}segurar um saco de um quilo de arroz pede uns dez newtons. [p=0.2] De onde vem esse número, você vê na aula de peso."),
    # resultante
    dict(id="s06", block="resultante", text="Quase sempre, {a}várias forças agem no mesmo corpo. [p=0.2] Somar todas elas, como vetores, dá a {b}força resultante. [p=0.3] É ela que decide o que acontece com o corpo."),
    dict(id="s07", block="resultante", text="{a}Duas pessoas empurram um carro para a frente: [p=0.2] {b}duzentos newtons [p=0.1] e {c}cento e cinquenta newtons. [p=0.2] Mesmo sentido, {d}soma: [p=0.1] trezentos e cinquenta newtons para a frente."),
    dict(id="s08", block="resultante", text="{a}No cabo de guerra, [p=0.2] um time puxa com {b}trezentos newtons para a direita, [p=0.2] e o outro, com {c}duzentos para a esquerda. [p=0.2] Sentidos opostos, {d}subtrai: [p=0.2] {e}cem newtons, no sentido do maior, para a direita."),
    dict(id="s09", block="resultante", text="E se os times empatam, {a}trezentos contra trezentos? [p=0.3] A resultante é {b}zero. [p=0.2] As forças existem, [p=0.1] mas {c}uma cancela a outra."),
    # primeira lei
    dict(id="s10", block="inercia", text="Agora vem a {a}primeira lei de Newton. [p=0.3] Se a força resultante é zero, [p=0.2] o corpo {b}mantém o que estava fazendo. [p=0.3] {c}Parado, continua parado. [p=0.2] {d}Em movimento, continua em linha reta, com a mesma velocidade: [p=0.2] o movimento uniforme."),
    dict(id="s11", block="inercia", text="Essa tendência de manter o movimento se chama {a}inércia. [p=0.3] Para {b}mudar a velocidade, seja o valor, seja a direção, [p=0.2] é preciso uma {c}resultante diferente de zero. [p=0.3] E {d}quanto maior a massa, maior a inércia: [p=0.2] um caminhão vazio é mais fácil de empurrar que um cheio."),
    dict(id="s12", block="inercia", text="Volte ao ônibus. [p=0.2] {a}O freio faz força no ônibus, [p=0.2] e o ônibus para. [p=0.3] Mas {b}em você, na horizontal, nenhuma força segura. [p=0.2] Seu corpo {c}continua para a frente, por inércia. [p=0.3] Você não foi jogado: [p=0.1] {d}o ônibus é que parou embaixo de você."),
    dict(id="s13", block="inercia", text="É aí que entra o {a}cinto de segurança. [p=0.2] Ele faz a {b}força para trás que muda a sua velocidade junto com a do carro, [p=0.2] em vez de {c}você parar no painel."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com o erro mais comum: [p=0.2] achar que {a}corpo em movimento precisa de força resultante para a frente. [p=0.3] {b}Um carro a oitenta quilômetros por hora, em linha reta, sem mudar a velocidade. [p=0.2] Qual é a resultante?"),
    dict(id="s15", block="erro", text="Uma força empurra o carro para a frente, [p=0.2] e {a}o ar e o atrito seguram para trás, [p=0.2] o atrito é assunto de outra aula. [p=0.3] Velocidade constante em linha reta é {b}resultante zero: [p=0.2] {c}as forças para a frente empatam com as forças para trás."),
    # atalho
    dict(id="s16", block="atalho", text="Agora, o atalho de prova. [p=0.2] Leu {a}parado, [p=0.1] {b}em equilíbrio [p=0.1] ou {c}velocidade constante? [p=0.3] Escreva na hora: {d}resultante zero. [p=0.3] E nas forças em uma linha, {e}a soma de um lado é igual à soma do outro."),
    dict(id="s17", block="atalho", text="Funciona porque {a}resultante zero é exatamente o que mantém parado ou em movimento uniforme. [p=0.3] {b}Não compensa quando há forças inclinadas: [p=0.2] aí, primeiro é preciso decompor, assunto de outra aula."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Num cabo de guerra, {a}um time puxa para a esquerda com duas forças: duzentos e cinquenta newtons e duzentos newtons. [p=0.3] O outro puxa para a direita com {b}trezentos newtons [p=0.1] e {c}uma força que falta descobrir. [p=0.3] {d}A corda não sai do lugar. [p=0.2] {e}Quanto vale essa força?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] A corda está parada: {a}resultante zero. [p=0.2] Então, {b}esquerda igual à direita. [p=0.3] Na esquerda, {c}duzentos e cinquenta mais duzentos: quatrocentos e cinquenta. [p=0.2] Na direita, {d}trezentos mais a força que falta. [p=0.3] {e}A força vale cento e cinquenta newtons."),
    dict(id="s21", block="resposta", text="E se a corda {a}andasse para a esquerda com velocidade constante? [p=0.3] {b}A resposta seria a mesma: [p=0.2] velocidade constante também é {c}resultante zero."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}some as forças como vetores para achar a resultante. [p=0.2] {b}Resultante zero: o corpo fica parado ou segue em linha reta com a mesma velocidade. [p=0.2] {c}Isso é inércia."),
    dict(id="s23", block="fim", text="Na próxima aula, a resultante deixa de ser zero: [p=0.2] você vai calcular {a}quanto a velocidade muda com a segunda lei de Newton, [p=0.2] {b}força igual a massa vezes aceleração. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
