# Estudativo · MAT-POL-012 — Praticando: simetrias (Matemática · Geometria Plana: Polígonos e Círculo · prática).
# Habilidade: reconhecer a transformação usada numa figura e resolver questões de malha, espelho e dobradura.
# Pré-requisitos: MAT-POL-010 (eixos de simetria e dobraduras), MAT-POL-011 (reflexão, rotação e translação). Usa também MAT-ANG-001 (relógio).
# Última aula da trilha. Próxima na playlist Matemática do Zero: MAT-ARE-001 (perímetro, cerca de 20 m por 35 m).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questões inéditas, criadas para esta aula. Pares narrados como em MAT-FUN-001: "xis um, ípsilon um". Letras: "á", "bê", "cê".
# Termos das aulas anteriores: "girar a folha sobre a mesa" (rotação) × "virar a folha do avesso" (reflexão);
#   atalho do giro de 90° ao contrário do relógio: troca os números e muda o sinal do que ficou na frente.
# Visual: E.plano com malha; bandeirinha (mastro + pano), relógio, folha dobrada.
#   1: bandeira original e três cópias: A deslocada igual (translação), B espelhada com o pano para a esquerda (reflexão),
#      C deitada, girada 90° ao contrário do relógio, sem espelhar (rotação).
#   2: triângulo (1, 1), (4, 1), (1, 3) refletido no eixo y: (−1, 1), (−4, 1), (−1, 3).
#   3: ponto (5, 2) girado 180° em torno da origem, em dois giros de 90°: (−2, 5) e depois (−5, −2).
#   4: relógio no espelho marcando 2 h; eixo do 12 ao 6; hora real 10 h.
#   5: folha quadrada dobrada em quatro; triângulo cortado no canto das dobras, com lados de 2 cm sobre as dobras;
#      aberta: quadrado em pé sobre uma ponta, com 4 cm de ponta a ponta (diagonais), e seus 4 eixos.

TITULO = "Praticando: simetrias"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações de simetria, [p=0.2] criadas para esta aula. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}eixos de simetria, [p=0.2] {b}dobraduras [p=0.2] e {c}os três movimentos: translação, reflexão e rotação. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: reconhecer
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Na tela, uma bandeirinha e {b}três cópias dela: á, bê e cê. [p=0.3] {c}Que movimento levou a bandeira original até cada cópia?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}A cópia á está do mesmo jeito, só em outro lugar: translação. [p=0.3] {b}A cópia bê tem o pano virado para o outro lado. [p=0.2] Ela só se encaixa na original {c}virando a folha do avesso: reflexão. [p=0.3] {d}A cópia cê está deitada, [p=0.2] mas se encaixa {e}girando a folha sobre a mesa: rotação."),
    # situação 2: reflexão na malha
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] Um triângulo tem vértices em {b}xis um, ípsilon um. [p=0.2] {c}Xis quatro, ípsilon um. [p=0.2] E {d}xis um, ípsilon três. [p=0.3] {e}Onde ficam os vértices depois de refletir o triângulo no eixo ípsilon?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] O eixo ípsilon fica em pé, então {a}muda o sinal do xis, e o ípsilon fica. [p=0.3] {b}Xis menos um, ípsilon um. [p=0.2] {c}Xis menos quatro, ípsilon um. [p=0.2] {d}Xis menos um, ípsilon três. [p=0.3] O triângulo, que apontava para a direita, {e}agora aponta para a esquerda: espelhado."),
    # situação 3: rotação de meia volta
    dict(id="s09", block="questao3", text="{a}Situação três. [p=0.2] O ponto {b}xis cinco, ípsilon dois, [p=0.2] gira {c}meia volta, cento e oitenta graus, em volta da origem. [p=0.3] {d}Para onde ele vai?"),
    dict(id="s10", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s11", block="resposta3", text="Vamos lá. [p=0.2] Meia volta são {a}dois quartos de volta. [p=0.2] Use o atalho do giro duas vezes. [p=0.3] {b}Primeiro giro: troca e muda o sinal do primeiro. [p=0.2] Dá {c}xis menos dois, ípsilon cinco."),
    dict(id="s12", block="resposta3", text="{a}Segundo giro: a troca dá cinco e menos dois. [p=0.2] Muda o sinal do primeiro: [p=0.2] {b}xis menos cinco, ípsilon menos dois. [p=0.3] Repare: {c}na meia volta, cada número troca de sinal e fica no mesmo lugar. [p=0.2] Vale guardar."),
    # situação 4: relógio no espelho
    dict(id="s13", block="questao4", text="{a}Situação quatro. [p=0.2] Um relógio de ponteiros, visto {b}num espelho, [p=0.2] parece marcar {c}duas horas em ponto. [p=0.3] {d}Que horas são de verdade?"),
    dict(id="s14", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta4", text="Vamos lá. [p=0.2] O espelho fica em pé, então {a}o eixo é a linha do doze ao seis. [p=0.2] {b}O doze e o seis ficam no lugar, [p=0.2] e {c}a direita troca com a esquerda. [p=0.3] No espelho, o ponteiro das horas está {d}duas horas à direita do doze. [p=0.2] De verdade, ele está {e}duas horas à esquerda: no dez. [p=0.2] São {f}dez horas."),
    dict(id="s16", block="resposta4", text="Atalho para hora cheia: {a}doze menos a hora do espelho. [p=0.2] {b}Doze menos dois dá dez. [p=0.3] Funciona porque {c}cada hora troca com a que fica do outro lado do eixo, à mesma distância do doze. [p=0.2] Com minutos quebrados, {d}o ponteiro dos minutos também se espelha, e a conta muda."),
    # situação 5: dobradura
    dict(id="s17", block="questao5", text="{a}Última situação. [p=0.2] Uma folha quadrada é {b}dobrada ao meio, [p=0.2] e {c}de novo ao meio, no outro sentido. [p=0.3] No canto onde as dobras se encontram, você corta {d}um triângulo com um lado em cada dobra, [p=0.2] e esses lados medem {e}dois centímetros cada. [p=0.3] {f}Que figura aparece ao abrir, e quantos eixos de simetria ela tem?"),
    dict(id="s18", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta5", text="Vamos lá. [p=0.2] O canto das dobras é {a}o centro da folha. [p=0.2] Cada dobra espelha o corte, [p=0.2] então aparecem {b}quatro triângulos iguais em volta do centro. [p=0.3] Como o corte encosta nas dobras, eles {c}se juntam numa figura só."),
    dict(id="s20", block="resposta5", text="Cada triângulo tem {a}o canto reto no centro e dois lados de dois centímetros: é isósceles. [p=0.2] Cento e oitenta menos noventa dá noventa, [p=0.2] e noventa dividido por dois dá quarenta e cinco graus em cada um dos outros cantos. [p=0.3] Na figura aberta, cada ponta junta dois desses cantos, e quarenta e cinco mais quarenta e cinco dá noventa. [p=0.2] Quatro lados iguais e quatro cantos retos: {b}um quadrado em pé sobre uma ponta, [p=0.2] com {c}dois mais dois, que dá quatro centímetros de uma ponta à outra. [p=0.3] Quadrado: {d}quatro eixos de simetria. [p=0.2] Inclusive as próprias dobras."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}dobra é espelho, [p=0.2] {b}eixo em pé muda o sinal do xis, eixo deitado muda o do ípsilon, [p=0.2] e, {c}para reconhecer o movimento, gire sobre a mesa ou vire do avesso."),
    dict(id="s22", block="fim", text="Com isso, você fecha a trilha de polígonos e circunferência. [p=0.2] Na próxima aula, começam {a}as áreas e os perímetros, [p=0.2] pelo contorno de uma figura: [p=0.2] {b}quantos metros de cerca contornam um terreno de vinte por trinta e cinco metros. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
