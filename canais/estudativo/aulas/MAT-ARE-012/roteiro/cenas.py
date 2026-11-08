# Estudativo · MAT-ARE-012 — Praticando: círculo, figuras compostas e razão entre áreas (Matemática · Áreas e Perímetros · prática).
# Habilidade: achar regiões sombreadas e comparar áreas de figuras ampliadas sem calcular tudo de novo.
# Pré-requisitos: MAT-ARE-008, MAT-ARE-009, MAT-ARE-010, MAT-ARE-011. Próxima: nenhuma na trilha; a playlist Matemática do Zero segue com MAT-EXP-001.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questões inéditas, criadas para esta aula. Preços hipotéticos. Soma de decimais (MAT-FRA-015) fora da cadeia: π = 3 deixa tudo inteiro.
# Letra k narrada "cá", como em MAT-ARE-010.
# Contas: azulejo 8 × 8 = 64; quatro quartos de raio 4 = 16π = 48; branco 16 cm²; contorno = uma volta 2 · 3 · 4 = 24 cm.
#   Limpador: 2.500π − 100π = 2.400π; 120° = 1/3 → 800π = 2.400 cm². Pizza: 45/30 = 1,5; 1,5² = 2,25 (> 2).
#   Bases: áreas 20 e 30 (2 : 3), lado 15 → 3 por parte → 6 e 9.
# Visual:
#   s03-s07: E.quadrado de lado 8 com um quarto de E.circulo (setor de 90°, raio 4) azul em cada canto; a região branca no meio, contornada só por arcos;
#            os quatro quartos deslizam e montam um círculo inteiro.
#   s08-s11: limpador de para-brisa: setor de coroa de 120°, raios 10 e 50 cm (E.circulo setor, com o furo).
#   s12-s15: pizza média (diâmetro 30) e grande (diâmetro 45), etiquetas R$ 40 e R$ 80; 1,5 × 1,5 = 2,25.
#   s16-s19: E.triangulo com uma linha do vértice até a base de 15; áreas 20 e 30; a base partida em 6 e 9.

TITULO = "Praticando: círculo, figuras compostas e razão entre áreas"

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
    dict(id="s01", block="gancho", text="{a}Quatro situações, criadas para esta aula, [p=0.2] com {b}círculos, figuras recortadas e ampliações. [p=0.3] Em cada uma, {c}pause o vídeo e resolva antes de ver a resposta. [p=0.3] O segredo de hoje é {d}não fazer conta à toa."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar: [p=0.2] {a}a área do círculo, pi érre ao quadrado, e a volta, dois pi érre; [p=0.2] {b}o setor como fração do círculo; [p=0.2] {c}somar e tirar pedaços; [p=0.2] {d}área vezes cá ao quadrado nas ampliações; [p=0.2] e {e}a razão das bases nos triângulos de mesma altura. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: azulejo
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Um azulejo quadrado tem {b}oito centímetros de lado. [p=0.2] Em cada canto, há {c}um quarto de círculo de raio quatro, com o centro no próprio canto, pintado de azul. [p=0.3] {d}Qual é a área da parte branca, no meio? [p=0.2] {e}E quanto mede o contorno dela? [p=0.2] Use pi igual a três."),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}Quatro quartos de círculo com o mesmo raio formam um círculo inteiro. [p=0.2] {b}Pi vezes quatro ao quadrado dá dezesseis pi, [p=0.2] {c}que com pi igual a três dá quarenta e oito. [p=0.3] {d}No azulejo, oito vezes oito dá sessenta e quatro. [p=0.2] {e}Sessenta e quatro menos quarenta e oito dá dezesseis centímetros quadrados de branco."),
    dict(id="s06", block="resposta1", text="O contorno do branco é feito só de {a}arcos: quatro quartos de volta. [p=0.2] Juntos, {b}uma volta inteira de raio quatro. [p=0.2] {c}Duas vezes três vezes quatro dá vinte e quatro centímetros. [p=0.3] {d}Os lados do quadrado não entram: eles ficam na borda do azul."),
    # atalho
    dict(id="s07", block="atalho", text="Esse é o atalho do dia: {a}junte os pedaços de círculo em círculos inteiros. [p=0.2] {b}Quatro quartos, um círculo. [p=0.2] {c}Duas metades, um círculo. [p=0.3] Funciona porque {d}os ângulos dos pedaços somam a volta inteira, trezentos e sessenta graus. [p=0.2] {e}Não compensa com raios diferentes: [p=0.2] aí, {f}calcule cada pedaço."),
    # situação 2: limpador
    dict(id="s08", block="questao2", text="{a}Situação dois. [p=0.2] A haste de um limpador de para-brisa gira presa num ponto. [p=0.2] A borracha vai de {b}dez centímetros até cinquenta centímetros desse ponto, [p=0.2] e a haste gira {c}cento e vinte graus. [p=0.3] {d}Que área de vidro a borracha limpa? [p=0.2] Use pi igual a três."),
    dict(id="s09", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s10", block="resposta2", text="Vamos lá. [p=0.2] A região limpa é {a}um pedaço de coroa, entre os raios dez e cinquenta. [p=0.2] {b}Fora: pi vezes cinquenta ao quadrado dá dois mil e quinhentos pi. [p=0.2] {c}Dentro: pi vezes dez ao quadrado dá cem pi. [p=0.2] {d}A coroa inteira tem dois mil e quatrocentos pi."),
    dict(id="s11", block="resposta2", text="{a}Cento e vinte graus é um terço da volta. [p=0.2] {b}Um terço de dois mil e quatrocentos pi dá oitocentos pi, [p=0.2] que com pi igual a três fica {c}oitocentos vezes três, e dá dois mil e quatrocentos centímetros quadrados. [p=0.3] Quem esquece o furo calcula {d}o setor inteiro de raio cinquenta, [p=0.2] e conta {e}vidro que a borracha nem toca."),
    # situação 3: pizza
    dict(id="s12", block="questao3", text="{a}Situação três. [p=0.2] Uma pizzaria vende a pizza média, com {b}trinta centímetros de diâmetro, por quarenta reais, [p=0.2] e a grande, com {c}quarenta e cinco centímetros, por oitenta reais. [p=0.3] A grande custa o dobro. [p=0.2] {d}Ela tem mais ou menos que o dobro de pizza?"),
    dict(id="s13", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="resposta3", text="Vamos lá. [p=0.2] Círculos são {a}sempre semelhantes. [p=0.2] {b}Quarenta e cinco dividido por trinta dá um vírgula cinco: [p=0.2] essa é a razão de semelhança. [p=0.3] A área vai vezes {c}um vírgula cinco ao quadrado. [p=0.2] Sem a vírgula, {d}quinze vezes quinze dá duzentos e vinte e cinco. [p=0.2] Com duas casas, {e}dois vírgula vinte e cinco."),
    dict(id="s15", block="resposta3", text="A grande tem {a}dois vírgula vinte e cinco vezes a área da média: [p=0.2] {b}mais que o dobro de pizza, pelo dobro do preço. [p=0.2] {c}A grande compensa. [p=0.3] E nem foi preciso calcular {d}a área de pizza nenhuma."),
    # situação 4: razão das bases
    dict(id="s16", block="questao4", text="{a}Última situação. [p=0.2] Uma linha sai de um vértice de um triângulo e chega no lado da frente, [p=0.2] que mede {b}quinze centímetros. [p=0.3] Ela divide o triângulo em {c}um pedaço de vinte e outro de trinta centímetros quadrados. [p=0.3] {d}Em que medidas ela divide o lado de quinze?"),
    dict(id="s17", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta4", text="Vamos lá. [p=0.2] Os pedaços têm {a}o mesmo vértice e as bases na mesma reta: mesma altura. [p=0.2] Então {b}as bases seguem a razão das áreas: [p=0.2] {c}vinte para trinta, ou dois para três. [p=0.3] Aqui nada vai ao quadrado: {d}os triângulos não são semelhantes, só têm a mesma altura."),
    dict(id="s19", block="resposta4", text="{a}Dois mais três dá cinco partes. [p=0.2] {b}Quinze dividido por cinco dá três por parte. [p=0.2] {c}Duas partes dão seis centímetros. [p=0.2] {d}Três partes dão nove centímetros. [p=0.3] Conferindo: {e}seis mais nove dá quinze. [p=0.2] Bateu."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}junte os pedaços de círculo, [p=0.2] {b}tire o que não faz parte, [p=0.2] {c}na ampliação, área vezes cá ao quadrado, [p=0.2] e {d}com a mesma altura, razão das bases."),
    dict(id="s21", block="fim", text="Com esta aula, você {a}fecha a trilha de áreas e perímetros. [p=0.3] Na próxima, começa {b}a função exponencial, em que o xis vai para o expoente, [p=0.2] como em {c}dois elevado a xis. [p=0.2] Você vai traçar {d}uma curva que sobe cada vez mais rápido, e outra que desce. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
