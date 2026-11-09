# Estudativo · FIS-OND-007 — Cordas, tubos e ressonância (Física · Ondas e Som · Som e efeito Doppler).
# Habilidade: usar os harmônicos na corda e no tubo aberto, saber que o tubo fechado só tem ímpares e explicar a ressonância.
# Pré-requisitos: FIS-OND-006 (altura, timbre), FIS-OND-004 (interferência). Usa FIS-OND-003 (reflexão). Próxima: FIS-OND-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Corda e tubo aberto: f_n = n·v/(2L), n = 1, 2, 3...; tubo fechado: f_n = n·v/(4L), n ímpar.
# A ponte de Tacoma não é citada (a explicação moderna não é ressonância simples).

TITULO = "Cordas, tubos e ressonância"

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
    dict(id="s01", block="gancho", text="{a}Num violão, todas as cordas têm o mesmo comprimento. [p=0.2] {b}Mesmo assim, cada uma toca uma nota diferente. [p=0.3] {c}E quando você aperta a corda no braço do violão, a nota sobe. [p=0.2] Por quê?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular {b}as frequências de uma corda e de um tubo [p=0.2] e explicar {c}a ressonância."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}duas ondas que se encontram se somam, reforçando ou cancelando; [p=0.2] e {c}frequência maior é som mais agudo. [p=0.3] Se faltar alguma, procure no canal."),
    # onda estacionária
    dict(id="s04", block="estaciona", text="Toque uma corda presa nas duas pontas. [p=0.2] {a}A onda vai até a ponta, [p=0.1] {b}reflete e volta. [p=0.2] {c}A que vai e a que volta se somam. [p=0.3] O resultado é uma onda que parece parada no lugar: {d}a onda estacionária."),
    dict(id="s05", block="estaciona", text="Ela tem {a}pontos que nunca se mexem, os nós, [p=0.2] e {b}pontos que balançam ao máximo, os ventres. [p=0.3] {c}As pontas presas são sempre nós. [p=0.2] {d}Cada trecho entre dois nós mede meio lambda, e se chama fuso."),
    # harmônicos
    dict(id="s06", block="harmonicos", text="O jeito mais simples de vibrar é com {a}um fuso só: [p=0.1] a corda inteira é meio lambda. [p=0.2] Esse é {b}o primeiro harmônico, o fundamental, a nota mais grave. [p=0.3] {c}Com dois fusos, segundo harmônico. [p=0.1] {d}Com três, terceiro. [p=0.2] O número do harmônico é {e}o número de fusos."),
    dict(id="s07", block="harmonicos", text="Daí sai a fórmula: {a}efe ene igual a ene vezes vê, dividido por dois ele. [p=0.3] {b}Ene é o número do harmônico. [p=0.1] {c}Ele é o comprimento da corda, em metros. [p=0.1] {d}Vê é a velocidade da onda na corda, em metros por segundo, [p=0.1] e efe ene sai em hertz. [p=0.3] Ela vem de {e}vê igual a lambda vezes efe: [p=0.1] com ene fusos, lambda vale dois ele dividido por ene."),
    dict(id="s08", block="harmonicos", text="Uma corda de {a}meio metro, com a onda a {b}duzentos metros por segundo. [p=0.2] {c}Dois ele: dois vezes zero vírgula cinco, um metro. [p=0.1] Fundamental: duzentos dividido por um, duzentos hertz. [p=0.3] {d}Os outros são múltiplos: quatrocentos, seiscentos, oitocentos."),
    dict(id="s09", block="harmonicos", text="E o violão do começo? [p=0.2] {a}Apertar a corda encurta o pedaço que vibra: [p=0.1] ele menor, frequência maior, nota mais aguda. [p=0.3] {b}E nas cordas mais grossas, a onda anda mais devagar: [p=0.1] vê menor, nota mais grave."),
    # tubos
    dict(id="s10", block="tubos", text="No tubo, quem vibra é {a}o ar dentro dele, como numa flauta. [p=0.2] {b}No tubo aberto nas duas pontas, a fórmula é a da corda, [p=0.1] com todos os harmônicos. [p=0.3] {c}Num tubo aberto de oitenta e cinco centímetros, com o som a trezentos e quarenta metros por segundo, [p=0.2] {d}o fundamental é trezentos e quarenta dividido por um vírgula sete: duzentos hertz."),
    dict(id="s11", block="tubos", text="{a}No tubo fechado numa ponta, a fórmula muda. [p=0.2] {b}A ponta fechada é nó, [p=0.1] {c}e a aberta é ventre. [p=0.2] {d}No fundamental, cabe só um quarto de lambda, [p=0.1] e o dois ele vira quatro ele. [p=0.3] {e}E só existem os harmônicos ímpares: um, três, cinco."),
    dict(id="s12", block="tubos", text="O mesmo tubo de oitenta e cinco centímetros, {a}fechado numa ponta: [p=0.2] {b}trezentos e quarenta dividido por três vírgula quatro, cem hertz. [p=0.2] {c}Depois, trezentos, quinhentos, setecentos. [p=0.2] {d}Duzentos e quatrocentos não aparecem."),
    # ressonância
    dict(id="s13", block="ressonancia", text="Por fim, {a}a ressonância. [p=0.2] Todo corpo tem as frequências em que vibra sozinho: {b}as frequências naturais. [p=0.3] {c}Se alguém empurra o corpo exatamente numa delas, [p=0.2] cada empurrão soma com o movimento, [p=0.1] e {d}a amplitude cresce muito."),
    dict(id="s14", block="ressonancia", text="É {a}o balanço empurrado no tempo certo. [p=0.2] {b}É a taça que quebra com a nota certa da voz. [p=0.3] {c}E é o próprio violão: [p=0.1] a caixa de madeira e o ar dentro dela vibram junto com a corda, [p=0.1] e o som sai mais forte."),
    # erro
    dict(id="s15", block="erro", text="Cuidado com o erro mais comum: {a}dar ao tubo fechado os harmônicos pares. [p=0.2] Um tubo fechado tem fundamental de cem hertz. [p=0.2] {b}A pessoa diz que ele também soa em duzentos. [p=0.3] {c}Não soa: [p=0.1] com nó numa ponta e ventre na outra, [p=0.1] {d}só cabem números ímpares de quartos de lambda. [p=0.2] {e}Depois do cem, vem o trezentos."),
    # atalho
    dict(id="s16", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}ache o fundamental e multiplique. [p=0.2] {b}Corda e tubo aberto: vezes um, dois, três. [p=0.1] {c}Tubo fechado: vezes um, três, cinco. [p=0.3] {d}E, com o mesmo comprimento, o fundamental do fechado é a metade do fundamental do aberto. [p=0.3] {e}Quando a questão dá o desenho da corda, nem precisa da fórmula: [p=0.1] conte os fusos."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Um tubo fechado numa ponta tem dezessete centímetros. [p=0.2] {b}O som anda a trezentos e quarenta metros por segundo. [p=0.3] {c}Qual é a frequência fundamental? [p=0.2] {d}E o tubo pode ressoar em mil hertz?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Tubo fechado: quatro ele. [p=0.1] {b}Quatro vezes zero vírgula dezessete, zero vírgula sessenta e oito metro. [p=0.2] {c}Trezentos e quarenta dividido por zero vírgula sessenta e oito: quinhentos hertz. [p=0.3] {d}Mil é duas vezes quinhentos, um harmônico par: [p=0.1] {e}não ressoa. [p=0.2] {f}Os próximos são mil e quinhentos e dois mil e quinhentos."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}corda e tubo aberto têm todos os harmônicos de ene vezes vê, dividido por dois ele; [p=0.2] {b}tubo fechado, só os ímpares, com quatro ele; [p=0.2] e {c}ressonância é empurrar na frequência natural."),
    dict(id="s21", block="fim", text="Na próxima aula, a fonte {a}começa a se mexer: [p=0.2] é {b}o efeito Doppler, a sirene que muda de tom quando passa por você. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
