# Estudativo · MAT-POL-011 — Reflexão, rotação e translação (Matemática · Geometria Plana: Polígonos e Círculo).
# Habilidade: prever a imagem de uma figura na malha depois de refletir, girar 90° ou deslocar e dizer que o ponto (2, 3) refletido no eixo y vai para (−2, 3).
# Pré-requisitos: MAT-FUN-001 (plano cartesiano, corredor e elevador), MAT-POL-010 (eixo de simetria como espelho). Usa também MAT-ANG-001 (90° = um quarto de volta). Próxima: MAT-POL-012.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Pares narrados como em MAT-FUN-001: "xis dois, ípsilon três".
# Giros sempre "ao contrário do relógio" (o sentido dos quadrantes em MAT-FUN-001), com centro na origem.
# Visual: E.plano com malha; bandeirinha (mastro em pé + pano à direita no alto), com o alto do mastro em (2, 3) marcado por E.ponto.
#   s05-s06: translação de 4 para a direita e 2 para baixo: (2, 3) → (6, 1), bandeira igual.
#   s07-s08: reflexão no eixo y: (2, 3) → (−2, 3), pano virado para a esquerda; segmento tracejado cruzando o eixo em ângulo reto.
#   s09: reflexão no eixo x: (2, 3) → (2, −3).
#   s10-s12: rotação de 90° anti-horária em torno da origem: caminho "2 direita, 3 cima" gira para "2 cima, 3 esquerda": (−3, 2); bandeira deitada.
#   s13: folha girando sobre a mesa × folha virada do avesso.
#   Questão: (4, 1) refletido no eixo x → (4, −1); girado 90° anti-horário → (−1, 4).

TITULO = "Reflexão, rotação e translação"

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
    dict(id="s01", block="gancho", text="{a}O ponto xis dois, ípsilon três, [p=0.2] refletido no eixo ípsilon. [p=0.3] Muita gente responde {b}xis dois, ípsilon menos três. [p=0.2] Errado. [p=0.3] Ele vai para {c}xis menos dois, ípsilon três."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você prevê onde uma figura vai parar depois de {b}espelhar, {c}girar ou {d}deslizar, [p=0.2] e leva um {e}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o plano cartesiano, primeiro o corredor, que é o xis, depois o elevador, que é o ípsilon; [p=0.2] e {c}o eixo de simetria, que funciona como um espelho. [p=0.3] Se faltar alguma, procure no canal."),
    # três movimentos
    dict(id="s04", block="movimentos", text="São {a}três movimentos. [p=0.2] Em todos, a figura {b}não muda de forma nem de tamanho: [p=0.2] só de lugar ou de posição. [p=0.3] Vamos usar {c}uma bandeirinha na malha, [p=0.2] com o alto do mastro em {d}xis dois, ípsilon três."),
    # translação
    dict(id="s05", block="translacao", text="{a}Translação é deslizar a figura, sem girar. [p=0.2] {b}Todos os pontos andam o mesmo tanto, na mesma direção. [p=0.3] Deslize a bandeira {c}quatro para a direita e dois para baixo."),
    dict(id="s06", block="translacao", text="No corredor, {a}dois mais quatro dá seis. [p=0.2] No elevador, {b}três menos dois dá um. [p=0.3] O alto do mastro vai para {c}xis seis, ípsilon um. [p=0.2] E {d}a bandeira continua do mesmo jeito: só mudou de lugar."),
    # reflexão
    dict(id="s07", block="reflexao", text="{a}Reflexão é o espelho. [p=0.2] Cada ponto vai para {b}o outro lado do eixo, na mesma distância, [p=0.2] por um caminho que {c}cruza o eixo em ângulo reto. [p=0.3] É a mesma ideia do eixo de simetria."),
    dict(id="s08", block="reflexao", text="Reflita no {a}eixo ípsilon, o eixo em pé. [p=0.2] O alto do mastro está {b}dois passos à direita dele. [p=0.2] Vai para {c}dois passos à esquerda, na mesma altura: [p=0.2] {d}xis menos dois, ípsilon três. [p=0.3] E a bandeira fica {e}espelhada: o pano, que apontava para a direita, agora aponta para a esquerda."),
    dict(id="s09", block="reflexao", text="No {a}eixo xis, o deitado, é o contrário: [p=0.2] {b}o ponto troca de cima para baixo. [p=0.2] Xis dois, ípsilon três, vai para {c}xis dois, ípsilon menos três."),
    # rotação
    dict(id="s10", block="rotacao", text="{a}Rotação é girar a figura em volta de um ponto, o centro, [p=0.2] como o ponteiro gira em volta do meio do relógio. [p=0.3] Vamos girar {b}noventa graus, um quarto de volta, [p=0.2] {c}ao contrário do relógio, o mesmo sentido da contagem dos quadrantes, [p=0.2] com centro na origem."),
    dict(id="s11", block="rotacao", text="Olhe {a}o caminho da origem até o alto do mastro: [p=0.2] {b}dois passos para a direita, depois três para cima. [p=0.3] Quando a figura gira, o caminho gira junto. [p=0.2] {c}Para a direita vira para cima. [p=0.2] {d}Para cima vira para a esquerda."),
    dict(id="s12", block="rotacao", text="O caminho novo é {a}dois passos para cima e três para a esquerda. [p=0.2] O ponto vai para {b}xis menos três, ípsilon dois. [p=0.3] {c}A bandeira fica deitada, mas não espelhada."),
    # reconhecer
    dict(id="s13", block="reconhecer", text="Como saber se foi reflexão ou rotação? [p=0.2] {a}Rotação é girar a folha sobre a mesa. [p=0.2] {b}Reflexão é virar a folha do avesso. [p=0.3] Se a figura só se encaixa na outra {c}virando do avesso, foi reflexão."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é o do começo: {a}refletir no eixo ípsilon e trocar o sinal do ípsilon. [p=0.3] Mas o eixo ípsilon {b}fica em pé. [p=0.2] Um espelho em pé {c}troca a direita com a esquerda, [p=0.2] e quem diz direita ou esquerda é {d}o xis. [p=0.3] {e}Refletiu no eixo ípsilon, muda o sinal do xis."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho prometido, para girar {a}noventa graus ao contrário do relógio, em volta da origem: [p=0.3] {b}troque os números de lugar [p=0.2] e {c}mude o sinal do que ficou na frente. [p=0.3] {d}Xis dois, ípsilon três. [p=0.2] A troca dá {e}três e dois. [p=0.2] Mudando o sinal do primeiro, {f}xis menos três, ípsilon dois."),
    dict(id="s16", block="atalho", text="Funciona porque {a}o passo para a direita vira passo para cima, [p=0.2] e {b}o passo para cima vira passo para a esquerda, que é negativo. [p=0.3] {c}No sentido do relógio, é o contrário: [p=0.2] o passo para a direita vira passo para baixo, e o passo para cima vira passo para a direita. [p=0.2] Troque os números e mude o sinal do que ficou atrás: [p=0.2] xis dois, ípsilon três, vai para xis três, ípsilon menos dois. [p=0.3] Não compensa se o centro não for a origem. [p=0.2] Aí, {d}gire o caminho na malha, passo a passo."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Pegue o ponto {a}xis quatro, ípsilon um. [p=0.3] {b}Para onde ele vai se for refletido no eixo xis? [p=0.2] {c}E se for girado noventa graus, ao contrário do relógio, em volta da origem?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] O eixo xis {a}está deitado, então o ponto troca de cima para baixo: [p=0.2] {b}muda o sinal do ípsilon. [p=0.2] Fica {c}xis quatro, ípsilon menos um."),
    dict(id="s20", block="resposta", text="No giro, pelo atalho: {a}a troca dá um e quatro. [p=0.2] {b}Muda o sinal do primeiro: [p=0.2] {c}xis menos um, ípsilon quatro. [p=0.3] Pelo caminho: {d}quatro passos para a direita viram quatro para cima, [p=0.2] e {e}um passo para cima vira um para a esquerda. [p=0.2] Bateu."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}translação desliza, [p=0.2] {b}reflexão espelha [p=0.2] e {c}rotação gira em volta de um centro."),
    dict(id="s22", block="fim", text="Na próxima aula, você pratica: [p=0.2] {a}reconhecer o movimento usado numa figura [p=0.2] e resolver questões de {b}malha, espelho e dobradura. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
