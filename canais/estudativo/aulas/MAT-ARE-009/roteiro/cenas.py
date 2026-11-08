# Estudativo · MAT-ARE-009 — Figuras compostas: somar e subtrair áreas (Matemática · Áreas e Perímetros).
# Habilidade: achar a área e o perímetro de um retângulo com um semicírculo em cima e a área sombreada numa malha, cortando em pedaços conhecidos.
# Pré-requisitos: MAT-ARE-004 (áreas de quadriláteros e triângulos), MAT-ARE-008 (A = πr²). Usa MAT-POL-004 (volta 2πr) e MAT-ARE-001 (perímetro). Próxima: MAT-ARE-010.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Soma de decimais (MAT-FRA-015) fora da cadeia: π = 3 deixa tudo inteiro.
# "Catetos" (MAT-ANG-015) fora da cadeia: diz-se "lados do ângulo reto", como em MAT-ARE-003.
# Contas: portão 4 × 3 = 12; semicírculo r = 2: 4π/2 = 2π = 6 → 18 m². Contorno 4 + 3 + 3 + 2π (meia volta) = 16 m; erro 14 + 6 = 20.
#   Malha: retângulo 6 × 4 = 24; quadrilátero com vértices (2,0), (6,3), (4,4), (0,1); cantos 1 + 6 + 1 + 6 = 14; sombreado 10 (conferido pela fórmula do cadarço).
#   Piscina 10 × 6 = 60; dois semicírculos r = 3 → 9π = 27 → 87 m². Borda 10 + 10 + 2π · 3 = 20 + 18 = 38 m.
# Visual:
#   s01, s05-s08, s13: portão = E.retangulo 4 × 3 com meio E.circulo de diâmetro 4 em cima; a linha do corte tracejada;
#                      o contorno traçado na cor da matéria; no erro, a linha de dentro em vermelho.
#   s04: dois ícones: tesoura (cortar e somar) e moldura (completar e subtrair).
#   s09-s12: malha quadriculada 6 × 4 (como E.grade de MAT-ARE-002) com o quadrilátero sombreado; retângulo em volta; os quatro triângulos dos cantos
#            com os lados do ângulo reto contados (2 e 1, 4 e 3, 1 e 2, 4 e 3).
#   s16-s19: piscina = E.retangulo 10 × 6 com meio círculo em cada ponta; os dois meios se juntam num círculo inteiro de raio 3; a borda traçada.

TITULO = "Figuras compostas: somar e subtrair áreas"

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
    dict(id="s01", block="gancho", text="{a}Um portão tem a parte de baixo retangular, [p=0.2] com {b}quatro metros de largura e três de altura, [p=0.2] e {c}meio círculo em cima. [p=0.3] Para contornar o portão com uma fita de luz, [p=0.2] muita gente {d}soma os quatro lados do retângulo e ainda o arco. [p=0.3] Só que {e}um desses lados nem fica na borda."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha a área e o contorno de figuras montadas com pedaços, [p=0.2] e ainda leva um {b}atalho de prova para malha quadriculada."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}as áreas do retângulo, do triângulo e do círculo, pi érre ao quadrado; [p=0.2] {c}a volta da circunferência, dois pi érre; [p=0.2] e {d}perímetro é a medida da borda, a volta inteira. [p=0.3] Se faltar alguma, procure no canal."),
    # estratégia
    dict(id="s04", block="ideia", text="Figura composta é {a}uma figura feita de pedaços que você já conhece. [p=0.2] Há {b}dois caminhos: [p=0.2] {c}cortar em pedaços e somar, [p=0.2] ou {d}completar uma figura maior e tirar o que sobra."),
    # portão: área
    dict(id="s05", block="portao", text="No portão, corte na linha {a}entre o retângulo e o arco. [p=0.3] {b}Retângulo: quatro vezes três dá doze metros quadrados. [p=0.2] {c}Meio círculo: o diâmetro é quatro, então o raio é dois. [p=0.2] {d}Pi vezes dois ao quadrado dá quatro pi, [p=0.2] e a metade dá {e}dois pi."),
    dict(id="s06", block="portao", text="Área total: {a}doze mais dois pi metros quadrados. [p=0.3] Com {b}pi igual a três, o dois pi fica dois vezes três, que dá seis, [p=0.2] e a área é {c}dezoito metros quadrados."),
    # portão: contorno
    dict(id="s07", block="contorno", text="E o contorno? [p=0.2] Ande pela borda. [p=0.2] {a}Embaixo, quatro. [p=0.2] {b}Nas laterais, três e três. [p=0.2] Em cima, {c}o arco, que é meia volta. [p=0.3] A volta inteira de raio dois mede {d}dois vezes pi vezes dois, que dá quatro pi. [p=0.2] {e}Meia volta dá dois pi, [p=0.2] que com pi igual a três dá seis metros."),
    dict(id="s08", block="contorno", text="{a}Quatro mais três mais três mais seis dá dezesseis metros. [p=0.3] {b}A linha do corte não entra. [p=0.2] Ela fica {c}dentro do portão, [p=0.2] e quem anda pela borda nunca passa por ela."),
    # malha
    dict(id="s09", block="malha", text="O outro caminho aparece numa {a}malha de quadradinhos de um centímetro. [p=0.2] A figura sombreada é {b}um quadrilátero torto, [p=0.2] com um vértice em cada lado de {c}um retângulo de seis por quatro."),
    dict(id="s10", block="malha", text="Cortar essa figura é difícil. [p=0.2] Então {a}complete o retângulo em volta: [p=0.2] {b}seis vezes quatro dá vinte e quatro centímetros quadrados. [p=0.3] O que fica de fora são {c}quatro triângulos com ângulo reto, um em cada canto."),
    dict(id="s11", block="malha", text="Os lados do ângulo reto {a}se contam na malha. [p=0.2] {b}Dois e um: dois vezes um, dividido por dois, dá um. [p=0.2] {c}Quatro e três: quatro vezes três, dividido por dois, dá seis. [p=0.2] Nos outros cantos, {d}mais um e mais seis. [p=0.3] Os cantos somam {e}catorze."),
    dict(id="s12", block="malha", text="{a}Vinte e quatro menos catorze dá dez. [p=0.2] {b}A área sombreada é de dez centímetros quadrados."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é o do portão: {a}pôr a linha de dentro no contorno. [p=0.2] A pessoa soma {b}os quatro lados do retângulo, catorze, [p=0.2] e {c}catorze mais o arco de seis dá vinte metros. [p=0.3] Sobram quatro metros de fita. [p=0.2] Na área, o corte não muda nada. [p=0.2] {d}No contorno, só entra o que fica do lado de fora."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho, para malha: {a}retângulo em volta, menos os cantos. [p=0.3] Funciona porque {b}os cantos são triângulos com o ângulo reto na própria malha, [p=0.2] e os lados deles {c}se contam em quadradinhos, sem régua."),
    dict(id="s15", block="atalho", text="{a}Não compensa quando a figura já é feita de quadradinhos inteiros ou de retângulos: [p=0.2] aí, {b}conte ou some direto."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Uma piscina tem uma parte retangular de {a}dez metros por seis metros [p=0.2] e {b}meio círculo em cada ponta, encostado no lado de seis metros. [p=0.3] {c}Qual é a área da superfície da água? [p=0.2] {d}E quantos metros tem a borda de pedra em volta? [p=0.2] {e}Use pi igual a três."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Retângulo: dez vezes seis dá sessenta. [p=0.3] Cada meio círculo tem diâmetro seis, então {b}raio três. [p=0.2] E aqui vem o truque: {c}duas metades iguais formam um círculo inteiro. [p=0.2] {d}Pi vezes três ao quadrado dá nove pi, [p=0.2] {e}que com pi igual a três dá vinte e sete."),
    dict(id="s19", block="resposta", text="Área: {a}sessenta mais vinte e sete dá oitenta e sete metros quadrados. [p=0.3] Na borda, {b}os lados de seis metros ficam dentro: não entram. [p=0.2] Entram {c}os lados compridos, que somam vinte, [p=0.2] e {d}os arcos das pontas, que juntos são uma volta inteira. [p=0.2] {e}Duas vezes três vezes três dá dezoito. [p=0.3] {f}Vinte mais dezoito dá trinta e oito metros de borda."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}corte em pedaços conhecidos e some, [p=0.2] {b}ou complete e tire o que sobra. [p=0.2] E {c}no contorno, só a borda de fora."),
    dict(id="s21", block="fim", text="Na próxima aula, você amplia figuras [p=0.2] e descobre por que {a}aumentar cada lado em vinte por cento [p=0.2] aumenta a área em {b}quarenta e quatro por cento. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
