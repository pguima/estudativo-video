# Estudativo · MAT-ANG-015 — Teorema de Pitágoras: achar hipotenusa ou cateto (Matemática · Geometria Plana: Ângulos e Triângulos).
# Habilidade: achar a hipotenusa de catetos 6 e 8 (10) e o cateto que falta quando a hipotenusa é 13 e o outro cateto é 5 (12).
# Pré-requisitos: MAT-ANG-005 (triângulo retângulo), MAT-FAT-007 (x² = 49). Usa também MAT-POT-007 (raiz quadrada) e MAT-FAT-015 (soma vezes diferença, no atalho). Próxima: MAT-ANG-016.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas como se falam: "á", "bê", "cê", "xis".
# Visual:
#   s01: caminho em L (6 para a direita, vira em ângulo reto, 8 para cima) e o segmento reto de volta (10), tracejado.
#   s04: E.triangulo retângulo com o quadradinho do reto; catetos e hipotenusa rotulados por nome.
#   s05-s06: triângulo 3-4-5 com um quadrado quadriculado em cada lado (9, 16 e 25 quadradinhos).
#   s08: equilátero de lado 5 (E.marcas_iguais) com 25 + 25 = 50 ≠ 25.
#   s18-s22: poste vertical, cabo de 17 m até o chão a 8 m do pé; altura h.

TITULO = "Teorema de Pitágoras: achar hipotenusa ou cateto"

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
    dict(id="s01", block="gancho", text="{a}Você anda seis metros em linha reta, [p=0.2] {b}vira em ângulo reto [p=0.2] e anda mais oito. [p=0.3] {c}A que distância ficou do ponto de partida? [p=0.3] Não é {d}catorze. [p=0.2] É {e}dez."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha qualquer lado de um triângulo retângulo [p=0.2] conhecendo os outros, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}triângulo retângulo é o que tem um ângulo reto, de noventa graus; [p=0.2] {c}raiz quadrada é o número que, vezes ele mesmo, dá o de dentro; [p=0.2] e {d}em xis ao quadrado igual a cem, xis vale dez ou menos dez. [p=0.3] Se faltar alguma, procure no canal."),
    # nomes
    dict(id="s04", block="nomes", text="Primeiro, os nomes. [p=0.2] Os lados que formam o ângulo reto são {a}os catetos. [p=0.3] O lado de frente para o ângulo reto é {b}a hipotenusa. [p=0.2] Ela é {c}o lado mais comprido, e você já vai ver por quê."),
    # lajotas
    dict(id="s05", block="lajotas", text="Pegue um triângulo retângulo de catetos {a}três e quatro [p=0.2] e hipotenusa {b}cinco. [p=0.3] Em cada lado, monte {c}um piso quadrado de lajotas."),
    dict(id="s06", block="lajotas", text="No primeiro cateto, {a}três vezes três dá nove lajotas. [p=0.2] No segundo, {b}quatro vezes quatro dá dezesseis. [p=0.2] Na hipotenusa, {c}cinco vezes cinco dá vinte e cinco. [p=0.3] Repare: {d}nove mais dezesseis dá vinte e cinco."),
    # regra
    dict(id="s07", block="regra", text="Esse é o {a}teorema de Pitágoras, [p=0.2] e ele vale para todo triângulo retângulo: [p=0.2] {b}a hipotenusa ao quadrado é igual à soma dos quadrados dos catetos. [p=0.3] Na fórmula, {c}á ao quadrado igual a bê ao quadrado mais cê ao quadrado. [p=0.2] {d}O á é a hipotenusa. [p=0.2] {e}Bê e cê são os catetos."),
    dict(id="s08", block="regra", text="Só vale com ângulo reto. [p=0.2] Num triângulo com {a}os três lados iguais a cinco, [p=0.2] {b}vinte e cinco mais vinte e cinco dá cinquenta, [p=0.2] que não é o quadrado do terceiro lado. [p=0.3] E como o quadrado da hipotenusa é uma soma de dois quadrados, [p=0.2] {c}ela passa de cada cateto: é sempre o maior lado."),
    # hipotenusa
    dict(id="s09", block="hipotenusa", text="Vamos achar {a}a hipotenusa do começo, com catetos seis e oito. [p=0.2] {b}Seis ao quadrado dá trinta e seis. [p=0.2] {c}Oito ao quadrado dá sessenta e quatro. [p=0.2] {d}Somando, dá cem."),
    dict(id="s10", block="hipotenusa", text="{a}Á ao quadrado igual a cem. [p=0.2] A equação aceita dez e menos dez, [p=0.2] mas {b}medida não é negativa. [p=0.2] {c}A hipotenusa mede dez. [p=0.3] O caminho reto é {d}mais curto que os catorze da volta."),
    # cateto
    dict(id="s11", block="cateto", text="E quando falta {a}um cateto? [p=0.2] Hipotenusa {b}treze, um cateto {c}cinco. [p=0.3] Monte a fórmula com o treze sozinho de um lado: [p=0.2] {d}treze ao quadrado igual a cinco ao quadrado mais xis ao quadrado. [p=0.2] {e}Cento e sessenta e nove igual a vinte e cinco mais xis ao quadrado."),
    dict(id="s12", block="cateto", text="{a}Tire vinte e cinco de cada lado da igualdade: [p=0.2] {b}xis ao quadrado igual a cento e quarenta e quatro. [p=0.2] {c}Xis igual a doze. [p=0.3] Conferindo: {d}vinte e cinco mais cento e quarenta e quatro dá cento e sessenta e nove. [p=0.2] Bateu."),
    dict(id="s13", block="cateto", text="Então, {a}para achar a hipotenusa, some os quadrados dos catetos. [p=0.2] {b}Para achar um cateto, tire o quadrado do cateto conhecido do quadrado da hipotenusa. [p=0.2] Nos dois casos, {c}tire a raiz no fim."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}somar quando falta um cateto. [p=0.2] A pessoa faz {b}cento e sessenta e nove mais vinte e cinco, que dá cento e noventa e quatro. [p=0.3] {c}Treze ao quadrado dá cento e sessenta e nove. [p=0.2] Catorze ao quadrado dá cento e noventa e seis. [p=0.2] Então a raiz de cento e noventa e quatro fica {d}entre treze e catorze."),
    dict(id="s15", block="erro", text="Um cateto {a}maior que a hipotenusa? [p=0.2] Impossível. [p=0.3] Antes de terminar, confira: [p=0.2] {b}a hipotenusa tem de ser o maior lado, [p=0.2] e {c}o cateto tem de ficar menor que ela."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho, para achar cateto: [p=0.2] {a}em vez de dois quadrados, uma soma e uma diferença. [p=0.3] {b}Treze mais cinco dá dezoito. [p=0.2] {c}Treze menos cinco dá oito. [p=0.2] {d}Dezoito vezes oito dá cento e quarenta e quatro. [p=0.2] A raiz dá {e}doze."),
    dict(id="s17", block="atalho", text="Funciona porque {a}treze ao quadrado menos cinco ao quadrado é uma diferença de dois quadrados, [p=0.2] e ela é {b}a soma vezes a diferença. [p=0.3] Brilha com números grandes e próximos. [p=0.2] Hipotenusa vinte e cinco, cateto vinte e quatro: [p=0.2] {c}quarenta e nove vezes um dá quarenta e nove, [p=0.2] e o outro cateto é {d}sete. [p=0.3] {e}Não serve para a hipotenusa: lá, os quadrados se somam."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Um poste está {a}em pé, em ângulo reto com o chão. [p=0.2] Um cabo esticado vai do alto dele até o chão, [p=0.2] mede {b}dezessete metros [p=0.2] e está preso a {c}oito metros do pé do poste. [p=0.3] {d}Qual a altura do poste?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] O cabo fica de frente para o ângulo reto: {a}é a hipotenusa. [p=0.2] A altura é {b}um cateto, então é subtração."),
    dict(id="s21", block="resposta", text="{a}Dezessete ao quadrado dá duzentos e oitenta e nove. [p=0.2] {b}Oito ao quadrado dá sessenta e quatro. [p=0.2] {c}Duzentos e oitenta e nove menos sessenta e quatro dá duzentos e vinte e cinco. [p=0.2] {d}A raiz de duzentos e vinte e cinco é quinze: [p=0.2] o poste tem {e}quinze metros."),
    dict(id="s22", block="resposta", text="Pelo atalho, mais rápido: [p=0.2] {a}dezessete mais oito dá vinte e cinco, [p=0.2] {b}dezessete menos oito dá nove, [p=0.2] e {c}vinte e cinco vezes nove dá duzentos e vinte e cinco. [p=0.3] Mesmo resultado, e {d}quinze é menor que dezessete. [p=0.2] Bateu."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}a hipotenusa ao quadrado é a soma dos quadrados dos catetos. [p=0.2] {b}Para a hipotenusa, some. [p=0.2] {c}Para um cateto, subtraia."),
    dict(id="s24", block="fim", text="Na próxima aula, você conhece {a}trios de números que aparecem tanto que dá para reconhecer sem conta, [p=0.2] como {b}três, quatro e cinco, [p=0.2] e resolve {c}o problema da escada encostada na parede. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
