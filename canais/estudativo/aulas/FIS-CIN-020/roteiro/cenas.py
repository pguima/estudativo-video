# Estudativo · FIS-CIN-020 — Correias, engrenagens e eixos (Física · Cinemática · Movimento circular).
# Habilidade: aplicar o atalho de prova: na correia a velocidade linear é igual, no eixo a angular é igual, inclusive na bicicleta com marchas.
# Pré-requisitos: FIS-CIN-019 (ω e v = ω·R), com FIS-CIN-018 (T, f, rpm) já ensinada. Próxima: FIS-CIN-021.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula. π = 3.
# Contas: correia 5 cm a 30 Hz → 15 cm: 30·5/15 = 10 Hz; em rpm: 1800·5/15 = 600 rpm (= 10·60).
# Engrenagem 10 e 30 dentes: 30 Hz → 10 Hz. Bicicleta: coroa 48, catraca 16 → 48/16 = 3 voltas por pedalada;
# 1 pedalada/s → roda 3 Hz; R = 0,3 m: v = 2·3·0,3·3 = 5,4 m/s. Questão: coroa 40, catraca 10 → 4 Hz; v = 2·3·0,3·4 = 7,2 m/s.

TITULO = "Correias, engrenagens e eixos"

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
    dict(id="s01", block="gancho", text="Numa bicicleta de marchas, {a}uma única pedalada [p=0.2] pode fazer a roda dar {b}três voltas. [p=0.3] {c}Como uma volta vira três? [p=0.3] A resposta está {d}na corrente e nas rodas dentadas."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai resolver {b}polias com correia, [p=0.2] {c}engrenagens [p=0.2] e {d}rodas presas no mesmo eixo, [p=0.2] inclusive {e}na bicicleta."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}vê igual a ômega vezes erre, [p=0.2] e {c}ômega igual a dois pi vezes a frequência. [p=0.3] Se faltar alguma, procure no canal."),
    # correia
    dict(id="s04", block="correia", text="Polia é {a}uma roda que gira presa a um eixo. [p=0.2] Duas polias ligadas por {b}uma correia, sem escorregar: [p=0.3] {c}a borda de cada polia anda junto com a correia. [p=0.2] Então {d}a velocidade linear da borda é a mesma nas duas."),
    dict(id="s05", block="correia", text="Mas os raios são diferentes. [p=0.2] {a}Vê igual a ômega vezes erre: [p=0.2] com o mesmo vê, {b}quem tem o raio menor precisa girar mais rápido. [p=0.3] Como ômega é dois pi vezes efe, [p=0.1] o dois pi corta dos dois lados, [p=0.1] e fica {c}efe vezes erre igual nas duas polias."),
    dict(id="s06", block="correia", text="{a}A polia de um motor tem cinco centímetros de raio e gira a trinta hertz. [p=0.2] {b}Ela puxa uma polia de quinze centímetros. [p=0.3] {c}Trinta vezes cinco é igual a efe vezes quinze. [p=0.2] {d}Efe é dez hertz. [p=0.3] {e}A polia três vezes maior gira três vezes mais devagar."),
    # engrenagem
    dict(id="s07", block="engrenagem", text="{a}Engrenagens encostadas funcionam igual: [p=0.2] {b}os dentes de uma empurram os da outra, [p=0.2] e {c}as bordas andam juntas. [p=0.3] A diferença: {d}uma gira para cada lado. [p=0.3] Na prova, o raio às vezes vem {e}como número de dentes: [p=0.2] a engrenagem maior tem mais dentes, na mesma proporção."),
    # eixo
    dict(id="s08", block="eixo", text="Agora, {a}duas rodas presas no mesmo eixo, uma grudada na outra. [p=0.3] Elas dão {b}uma volta juntas, no mesmo tempo. [p=0.2] Aqui, o que é igual é {c}a velocidade angular, [p=0.1] e também a frequência. [p=0.3] {d}A borda da roda maior anda mais rápido, [p=0.2] como a criança na borda do carrossel."),
    # bicicleta
    dict(id="s09", block="bicicleta", text="A bicicleta junta tudo. [p=0.2] {a}O pedal gira a coroa, a roda dentada da frente. [p=0.2] {b}A corrente liga a coroa à catraca, a roda dentada de trás: [p=0.1] é como uma correia. [p=0.2] {c}A catraca está presa no eixo da roda de trás."),
    dict(id="s10", block="bicicleta", text="Coroa de {a}quarenta e oito dentes, catraca de {b}dezesseis. [p=0.3] {c}Na corrente, a borda anda igual: [p=0.2] uma volta da coroa puxa um pedaço de corrente do tamanho de quarenta e oito dentes, [p=0.2] e na catraca de dezesseis isso dá {d}três voltas. [p=0.3] {e}No eixo, a frequência é igual: [p=0.2] {f}a roda também dá três voltas. [p=0.3] {g}Uma pedalada, três voltas da roda."),
    dict(id="s11", block="bicicleta", text="Por isso, {a}coroa grande com catraca pequena é a marcha mais rápida, [p=0.2] e também a mais pesada de pedalar. [p=0.3] {b}Coroa pequena com catraca grande é a marcha leve, [p=0.1] boa para a subida."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que polias ligadas por correia têm a mesma frequência. [p=0.3] Na polia do motor, a pessoa diz {b}trinta hertz para as duas. [p=0.2] {c}Não: na correia, o que é igual é a velocidade da borda. [p=0.3] {d}A frequência só é igual quando as rodas estão no mesmo eixo."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova, em duas linhas. [p=0.2] {a}Correia, corrente ou dente: [p=0.1] {b}velocidade linear igual, [p=0.1] {c}efe vezes erre igual, e a menor gira mais. [p=0.3] {d}Mesmo eixo: [p=0.1] {e}velocidade angular igual, e a maior anda mais rápido na borda."),
    dict(id="s14", block="atalho", text="E um bônus: {a}na conta efe vezes erre, você pode usar rpm e centímetros direto, sem converter, [p=0.2] porque {b}a unidade é a mesma dos dois lados e se cancela. [p=0.3] {c}O motor de trinta hertz faz mil e oitocentas rotações por minuto. [p=0.2] Mil e oitocentos vezes cinco, dividido por quinze: [p=0.1] seiscentas rotações por minuto, [p=0.1] os mesmos dez hertz. [p=0.3] {d}Não compensa quando a questão pede a velocidade em metros por segundo: [p=0.2] aí, passe para hertz e metros."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Uma bicicleta tem coroa de {b}quarenta dentes e catraca de {c}dez. [p=0.2] A roda tem {d}zero vírgula três metro de raio. [p=0.3] {e}O ciclista dá uma pedalada por segundo. [p=0.2] {f}Qual é a velocidade da bicicleta? [p=0.2] Use pi igual a três."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Corrente: quarenta dentes da coroa são quatro voltas da catraca de dez. [p=0.2] {b}Eixo: a roda dá as mesmas quatro voltas, [p=0.1] {c}quatro hertz."),
    dict(id="s18", block="resposta", text="{a}Vê igual a dois pi vezes efe vezes erre: [p=0.1] {b}dois vezes três vezes quatro vezes zero vírgula três, [p=0.1] {c}sete vírgula dois metros por segundo. [p=0.3] {d}Essa é a velocidade da borda da roda, [p=0.1] que, rolando sem escorregar, é a velocidade da bicicleta."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}na correia, velocidade linear igual; [p=0.2] {b}no eixo, velocidade angular igual; [p=0.2] e {c}na bicicleta, os dois, um depois do outro."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai {a}praticar o movimento circular [p=0.2] com {b}questões novas de rotação, polias e bicicleta. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
