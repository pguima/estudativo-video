# Estudativo · MAT-POL-009 — Praticando: polígonos e circunferência (Matemática · Geometria Plana: Polígonos e Círculo · prática).
# Habilidade: resolver questões de quadriláteros, polígonos regulares, voltas de roda e ângulos na circunferência.
# Pré-requisitos: MAT-POL-001 a MAT-POL-008. Próxima: MAT-POL-010.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questões inéditas, criadas para esta aula. Termos e atalhos das aulas da trilha: "volta" = comprimento da circunferência,
#   "a volta é o triplo do diâmetro" (pi = 3), "externo = 360 ÷ lados", "ene vezes ene menos três, dividido por dois",
#   "o arco é a mesma fração da volta que o ângulo central", cordas que se cruzam (pedaço vezes pedaço) e Pitágoras na corda.
# Visual: E.poligono / E.regular / E.circulo / E.angulo.
#   1: paralelogramo com 65° em A (E.angulo); 115°, 65°, 115° em volta.
#   2: decágono regular (E.regular, 10 lados), um vértice com as 7 diagonais; externo de 36°.
#   3: roda de bicicleta raio 35 cm (diâmetro 70), volta 210 cm; 630 m = 63 000 cm; 300 voltas.
#   4: circunferência raio 12, inscrito de 30° e central de 60° abrindo o mesmo arco (E.circulo com arco e setor); volta 72, arco 12.
#   5: corte de um cano, raio 17, água com 9 de profundidade; diâmetro em pé 34 (pedaços 9 e 25) cruzando a superfície
#      (metades 15 e 15); superfície de 30, a 8 do centro (conferência por Pitágoras, 8-15-17).

TITULO = "Praticando: polígonos e circunferência"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações com polígonos e circunferência, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}as regras do paralelogramo, [p=0.2] {b}a soma dos ângulos de um polígono, [p=0.2] {c}a volta da circunferência, [p=0.2] {d}o ângulo inscrito [p=0.2] e {e}as cordas que se cruzam. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: paralelogramo
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Um terreno tem a forma de um {b}paralelogramo, [p=0.2] e um dos ângulos mede {c}sessenta e cinco graus. [p=0.3] {d}Quanto medem os outros três ângulos?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] No paralelogramo, {a}ângulos vizinhos somam cento e oitenta. [p=0.2] {b}Cento e oitenta menos sessenta e cinco dá cento e quinze. [p=0.2] E {c}ângulos de frente são iguais. [p=0.3] São {d}dois ângulos de sessenta e cinco graus e dois de cento e quinze. [p=0.3] Conferindo: {e}a soma dá trezentos e sessenta, como em todo quadrilátero."),
    # situação 2: decágono regular
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] O tampo de uma mesa tem a forma de um {b}decágono regular: dez lados iguais e dez ângulos iguais. [p=0.3] {c}Quanto mede cada ângulo interno? [p=0.2] {d}E quantas diagonais ele tem?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá, pelo atalho. [p=0.2] {a}Externo: trezentos e sessenta dividido por dez dá trinta e seis. [p=0.2] {b}Interno: cento e oitenta menos trinta e seis dá cento e quarenta e quatro graus. [p=0.3] Pela soma, dá o mesmo: [p=0.2] {c}dez menos dois dá oito triângulos, e oito vezes cento e oitenta dá mil quatrocentos e quarenta. [p=0.2] {d}Mil quatrocentos e quarenta dividido por dez dá cento e quarenta e quatro."),
    dict(id="s09", block="resposta2", text="Diagonais: {a}de cada vértice saem dez menos três, que dá sete. [p=0.2] {b}Dez vezes sete dá setenta. [p=0.2] Cada diagonal foi contada {c}uma vez em cada ponta, [p=0.2] então {d}setenta dividido por dois dá trinta e cinco diagonais."),
    # situação 3: voltas de roda
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] A roda de uma bicicleta tem {b}raio de trinta e cinco centímetros. [p=0.3] {c}Quantas voltas a roda dá para a bicicleta andar seiscentos e trinta metros? [p=0.2] Use {d}pi igual a três."),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="Vamos lá. [p=0.2] Em uma volta, a bicicleta anda {a}a volta da roda. [p=0.2] Com pi igual a três, {b}a volta é o triplo do diâmetro. [p=0.2] O diâmetro é {c}setenta centímetros, [p=0.2] e {d}setenta vezes três dá duzentos e dez centímetros."),
    dict(id="s13", block="resposta3", text="Agora, {a}a mesma unidade. [p=0.2] Seiscentos e trinta metros, na escada do metro, [p=0.2] são {b}sessenta e três mil centímetros. [p=0.3] {c}Sessenta e três mil dividido por duzentos e dez dá trezentas voltas. [p=0.3] Quem esquece de converter faz {d}seiscentos e trinta dividido por duzentos e dez, [p=0.2] acha {e}três voltas, e em três voltas a bicicleta não anda nem sete metros."),
    # situação 4: inscrito e arco
    dict(id="s14", block="questao4", text="{a}Situação quatro. [p=0.2] Numa circunferência de {b}raio doze centímetros, [p=0.2] um ângulo inscrito de {c}trinta graus abre um arco. [p=0.3] {d}Quanto mede o comprimento desse arco? [p=0.2] Use pi igual a três."),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="Vamos lá. [p=0.2] O inscrito vale a metade do central do mesmo arco, [p=0.2] então {a}o central mede sessenta graus. [p=0.3] A volta inteira: {b}duas vezes três vezes doze dá setenta e dois centímetros."),
    dict(id="s17", block="resposta4", text="Sessenta graus é {a}um sexto da volta. [p=0.2] O arco é a mesma fração: [p=0.2] {b}setenta e dois dividido por seis dá doze centímetros. [p=0.3] Cuidado: quem usa {c}os trinta graus do inscrito direto [p=0.2] acha {d}seis centímetros, a metade do certo. [p=0.2] O arco segue {e}o ângulo central."),
    # situação 5: corda
    dict(id="s18", block="questao5", text="{a}Última situação. [p=0.2] Um cano tem {b}dezessete centímetros de raio por dentro. [p=0.2] Olhando o cano de frente, a água tem {c}nove centímetros de profundidade no ponto mais fundo. [p=0.3] {d}Quanto mede a largura da superfície da água?"),
    dict(id="s19", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta5", text="Vamos lá. [p=0.2] Trace {a}o diâmetro em pé, que passa pelo ponto mais fundo. [p=0.2] Ele sai do centro e chega na superfície em ângulo reto, então {b}corta a superfície ao meio. [p=0.3] Ficam duas cordas que se cruzam. [p=0.2] O diâmetro mede {c}duas vezes dezessete, que dá trinta e quatro. [p=0.2] Os pedaços dele são nove e {d}trinta e quatro menos nove, que dá vinte e cinco."),
    dict(id="s21", block="resposta5", text="Pedaço vezes pedaço: {a}nove vezes vinte e cinco dá duzentos e vinte e cinco. [p=0.2] Na superfície, as metades são iguais, [p=0.2] e {b}quinze vezes quinze dá duzentos e vinte e cinco. [p=0.2] {c}A metade mede quinze, e a superfície inteira mede {d}trinta centímetros. [p=0.3] Conferindo com Pitágoras: o centro fica a {e}dezessete menos nove, que dá oito centímetros da superfície, [p=0.2] e {f}oito ao quadrado mais quinze ao quadrado dá duzentos e oitenta e nove, que é dezessete ao quadrado. [p=0.2] Bateu."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}desenhe a figura, [p=0.2] {b}deixe tudo na mesma unidade [p=0.2] e {c}confira se a resposta faz sentido."),
    dict(id="s23", block="fim", text="Na próxima aula, você começa as simetrias: [p=0.2] {a}a linha que divide uma figura em duas metades que se encaixam, [p=0.2] e {b}o desenho que aparece quando você dobra um papel, corta e abre. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
