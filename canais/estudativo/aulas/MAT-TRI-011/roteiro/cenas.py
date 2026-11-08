# Estudativo · MAT-TRI-011 — Gráficos de seno, cosseno e tangente (Matemática · Trigonometria · Ciclo e funções trigonométricas).
# Habilidade: reconhecer a onda de cada gráfico e dizer o período e a imagem de y = 3 sen x.
# Pré-requisitos: MAT-FUN-007 (máximo, zeros, imagem como sombra no eixo y), MAT-TRI-008 (seno no eixo vertical, cosseno no horizontal).
#   Usa também MAT-TRI-007 (radianos; 390° cai no mesmo ponto que 30°), MAT-TRI-001 (tangente = seno ÷ cosseno), MAT-CON-006 (reais). Próxima: MAT-TRI-014.
# Questão inédita, criada para esta aula. Seno, cosseno e tangente por extenso; graus narrados por extenso; π narrado "pi"; π/2 narrado "pi meios", como na MAT-TRI-007.
# Seno: 0° → 0, 90° → 1, 180° → 0, 270° → −1, 360° → 0 · período 2π (360°) · imagem [−1, 1].
# Cosseno: 0° → 1, 90° → 0, 180° → −1, 270° → 0, 360° → 1 · mesma onda, começa no alto · período 2π · imagem [−1, 1].
# Tangente: não existe em 90° e 270° (cos = 0) · galhos · imagem ℝ · período π (180°).
# y = 3 sen x: alturas ×3 (1 → 3, −1 → −3, 0 → 0) · imagem [−3, 3] · período 2π · erro: 3 · 2π = 6π.
# Atalho: y = k sen x ou k cos x, k > 0: imagem [−k, k] (5 cos x → [−5, 5]); não vale para a tangente; número somado ou dentro do parêntese: próxima aula.
# Questão: y = 2 cos x · período 2π · imagem [−2, 2] · x = π: 2 · (−1) = −2 (ponto mais baixo).
# Visual (E.circulo, E.plano, E.curva, E.ponto):
#   s01: ciclo girando à esquerda, altura do ponto "riscando" a onda à direita.
#   s04-s07: plano com eixo x marcado em graus e radianos (0, π/2, π, 3π/2, 2π); tabela do seno; 5 pontos; curva ligando; a onda
#     continuando para os dois lados com um trecho de 2π destacado (período); sombra no eixo y de −1 a 1 (imagem).
#   s08-s09: a curva do cosseno sobre a do seno, em outra cor, começando em (0, 1).
#   s10-s11: gráfico da tangente com galhos e assíntotas tracejadas em π/2 e 3π/2; trecho de π destacado.
#   s12-s13: y = sen x apagada ao fundo e y = 3 sen x por cima, setas verticais esticando; sombra de −3 a 3; mesmo período.
#   s14: "6π" riscado em vermelho.
#   s17-s19: gráfico de y = 2 cos x e o ponto (π, −2).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Gráficos de seno, cosseno e tangente"

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
    dict(id="s01", block="gancho", text="{a}Um ponto gira sem parar no ciclo trigonométrico. [p=0.2] Acompanhe só a altura dele: [p=0.2] sobe, desce, sobe de novo. [p=0.3] Desenhada no papel, essa altura vira {b}uma onda. [p=0.2] É o gráfico do seno."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você reconhece a onda do seno, do cosseno e da tangente, [p=0.2] diz {b}o período e a imagem de cada uma [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}no ciclo, o seno é a altura do ponto, no eixo vertical, e o cosseno se lê no eixo horizontal; [p=0.2] e {c}num gráfico, a imagem são as saídas que aparecem, da menor até a maior: a sombra da curva no eixo ípsilon. [p=0.3] Se faltar alguma, procure no canal."),
    # seno
    dict(id="s04", block="seno", text="No gráfico, {a}o ângulo vai no eixo xis [p=0.2] e {b}o seno dele vai no eixo ípsilon. [p=0.3] Na prova, o eixo xis costuma vir {c}em radianos: [p=0.2] noventa graus é pi meios, [p=0.2] e a volta inteira é dois pi."),
    dict(id="s05", block="seno", text="Pegue os pontos fáceis do ciclo. [p=0.2] {a}Em zero grau, o seno é zero. [p=0.2] {b}Em noventa graus, vale um: o ponto mais alto. [p=0.2] {c}Em cento e oitenta, vale zero de novo. [p=0.2] {d}Em duzentos e setenta, vale menos um. [p=0.2] {e}Em trezentos e sessenta, vale zero, e a volta fecha."),
    dict(id="s06", block="seno", text="Ligue com uma curva suave: [p=0.2] {a}sai do zero, sobe até um, desce até menos um e volta ao zero. [p=0.3] Depois de uma volta, {b}os ângulos caem nos mesmos pontos do ciclo, [p=0.2] como trezentos e noventa graus cai no trinta. [p=0.2] Por isso {c}o desenho se repete para sempre."),
    dict(id="s07", block="seno", text="O pedaço que se repete tem um tamanho: {a}o período. [p=0.2] No seno, uma volta: {b}trezentos e sessenta graus, ou dois pi. [p=0.3] E a imagem, a sombra no eixo ípsilon, [p=0.2] vai {c}de menos um a um."),
    # cosseno
    dict(id="s08", block="cosseno", text="E o cosseno? [p=0.2] {a}Em zero grau, o cosseno vale um. [p=0.2] {b}Em noventa graus, vale zero. [p=0.2] {c}Em cento e oitenta, vale menos um. [p=0.2] {d}Em duzentos e setenta, vale zero. [p=0.2] {e}Em trezentos e sessenta, vale um de novo."),
    dict(id="s09", block="cosseno", text="É {a}a mesma onda, só que começa lá no alto. [p=0.3] {b}O período também é dois pi, [p=0.2] e {c}a imagem também vai de menos um a um."),
    # tangente
    dict(id="s10", block="tangente", text="A tangente é diferente. [p=0.2] Ela é {a}o seno dividido pelo cosseno. [p=0.3] Em noventa graus, {b}o cosseno é zero, [p=0.2] e divisão por zero não existe. [p=0.2] Perto dali, a tangente {c}dispara para cima ou para baixo."),
    dict(id="s11", block="tangente", text="O gráfico vira {a}vários galhos, [p=0.2] separados por {b}linhas tracejadas que a curva nunca toca. [p=0.3] Cada galho vem lá de baixo e sobe sem parar, [p=0.2] passando por todas as alturas: [p=0.2] {c}a imagem são todos os números reais. [p=0.3] E a tangente se repete {d}a cada meia volta: período pi, cento e oitenta graus. [p=0.2] No ponto do outro lado do ciclo, seno e cosseno trocam de sinal juntos, [p=0.2] e a divisão não muda."),
    # y = 3 sen x
    dict(id="s12", block="vezes3", text="E se o seno vier {a}multiplicado por três? [p=0.2] {b}Ípsilon igual a três vezes o seno de xis. [p=0.3] Cada altura da onda {c}triplica: [p=0.2] o um vira três, [p=0.2] o menos um vira menos três, [p=0.2] e o zero continua zero."),
    dict(id="s13", block="vezes3", text="A onda fica {a}mais alta, mas não mais larga. [p=0.3] {b}Imagem: de menos três a três. [p=0.2] {c}Período: continua dois pi, [p=0.2] porque o ângulo ainda precisa de uma volta inteira para se repetir."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}achar que o três mexe no período [p=0.2] e responder {b}três vezes dois pi, que dá seis pi. [p=0.3] Mas o três multiplica {c}a saída, a altura. [p=0.2] {d}A entrada, o ângulo, não muda. [p=0.2] A onda continua se repetindo {e}a cada dois pi."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: [p=0.2] {a}o número positivo na frente do seno ou do cosseno dá a imagem direto. [p=0.3] Ela vai {b}do oposto dele até ele. [p=0.2] Em {c}ípsilon igual a cinco vezes o cosseno de xis, [p=0.2] {d}de menos cinco a cinco."),
    dict(id="s16", block="atalho", text="Funciona porque {a}seno e cosseno nunca passam de um nem ficam abaixo de menos um, [p=0.2] e o número da frente multiplica as duas pontas. [p=0.3] {b}Não serve para a tangente, que não tem teto. [p=0.2] E quando aparece {c}um número somado, ou junto do xis dentro do parêntese, [p=0.2] a onda muda de outro jeito."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Ípsilon igual a duas vezes o cosseno de xis. [p=0.3] {b}Qual é o período? [p=0.2] {c}Qual é a imagem? [p=0.2] E {d}quanto vale ípsilon quando xis é pi, ou seja, cento e oitenta graus?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] O dois só mexe na altura: {a}período dois pi. [p=0.2] Pelo atalho, {b}imagem de menos dois a dois. [p=0.3] Em cento e oitenta graus, {c}o cosseno vale menos um. [p=0.2] {d}Duas vezes menos um dá menos dois: [p=0.2] é {e}o ponto mais baixo da onda."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}seno e cosseno são ondas de período dois pi, com imagem de menos um a um. [p=0.2] {b}A tangente tem galhos e período pi. [p=0.2] {c}O número na frente só estica a altura."),
    dict(id="s21", block="fim", text="Na próxima aula, você {a}mexe na onda de três jeitos: [p=0.2] {b}sobe, estica e aperta. [p=0.2] E lê o máximo, o mínimo e o período de {c}ípsilon igual a um mais duas vezes o cosseno de dois xis. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
