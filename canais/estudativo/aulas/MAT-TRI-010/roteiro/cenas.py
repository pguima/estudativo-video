# Estudativo · MAT-TRI-010 — Relação fundamental da trigonometria (Matemática · Trigonometria · Ciclo e funções trigonométricas).
# Habilidade: usar sen²x + cos²x = 1 e tg x = sen x / cos x para achar cos x = 4/5 quando sen x = 3/5 no 1º quadrante.
# Pré-requisitos: MAT-TRI-008 (seno no eixo vertical, cosseno no horizontal, sinais por quadrante). Usa também MAT-ANG-015 (Pitágoras),
#   MAT-FAT-007 (x² = k tem duas raízes), MAT-TRI-001 (tangente = seno ÷ cosseno), MAT-TRI-003 (sen 30° = 1/2, cos 30° = √3/2). Próxima: MAT-TRI-011.
# Questão inédita, criada para esta aula. Seno, cosseno e tangente narrados por extenso; na tela, sen, cos e tg. Ângulo narrado "xis".
# sen²x narrado "seno ao quadrado de xis" (nunca "seno de xis ao quadrado", que seria o ângulo ao quadrado).
# Soma/subtração de frações de denominadores diferentes (MAT-FRA-008) fora da ficha: 1 = 25/25 explicado na hora; 3/5 ÷ 4/5 pelos quintos que se cancelam, como na MAT-TRI-001.
# MAT-TRI-009 (redução) fora da ficha: não usada.
# Contas: ciclo de raio 1, ponto (cos x, sen x), Pitágoras: sen² + cos² = 1 · 30°: 1/4 + 3/4 = 1 · 90°: 1 + 0 = 1.
# Exemplo: sen x = 3/5 · sen² = 9/25 · cos² = 25/25 − 9/25 = 16/25 · cos = ±4/5 → 1º quadrante: 4/5 · tg = 3/4.
# Erro: cos = 1 − sen = 1 − 3/5 = 2/5 · teste: 9/25 + 4/25 = 13/25 (não dá 1).
# Atalho: triângulo 3-4-5 (oposto 3, hipotenusa 5 → adjacente 4); dá só o tamanho, o sinal vem do quadrante.
# Questão: cos x = 8/17, 4º quadrante · 17² − 8² = 289 − 64 = 225 · √225 = 15 · sen = −15/17 · tg = −15/8 · confere: 225/289 + 64/289 = 1.
# Visual (E.circulo, E.plano, E.triangulo, E.angulo):
#   s01: "sen x = 3/5 → cos x = ?"; 2/5 riscado em vermelho, 4/5 em verde.
#   s04-s06: ciclo de raio 1 nos eixos; arco x no 1º quadrante; segmento vertical do ponto até o eixo horizontal; triângulo retângulo
#     destacado com hipotenusa 1 (raio), lado deitado "cos x" e lado em pé "sen x"; depois sen²x + cos²x = 1 grande.
#   s07: notação sen²x = (sen x)², com "≠ sen(x²)".
#   s08: tabelinha de checagem 30° e 90°.
#   s09-s12: conta passo a passo; 4/5 e −4/5 com o 1º quadrante aceso; tg = (3/5)/(4/5) = 3/4.
#   s14: triângulo 3-4-5 (oposto 3, hipotenusa 5, adjacente "?" virando 4).
#   s16-s19: ciclo com o arco no 4º quadrante; triângulo 8-15-17 abaixo do eixo; sinais.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Relação fundamental da trigonometria"

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
    dict(id="s01", block="gancho", text="{a}O seno de um ângulo do primeiro quadrante vale três quintos. [p=0.3] Quanto vale o cosseno? [p=0.2] Muita gente faz {b}um menos três quintos [p=0.2] e responde dois quintos. [p=0.3] {c}A resposta certa é quatro quintos."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha o cosseno pelo seno, e o seno pelo cosseno, [p=0.2] com a relação mais usada da trigonometria [p=0.2] e um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}no ciclo de raio um, o cosseno se lê no eixo horizontal e o seno no eixo vertical; [p=0.2] {c}o teorema de Pitágoras; [p=0.2] e {d}se um número ao quadrado dá nove, ele vale três ou menos três. [p=0.3] Se faltar alguma, procure no canal."),
    # de onde vem
    dict(id="s04", block="ciclo", text="Marque um ângulo xis {a}no ciclo, no primeiro quadrante. [p=0.2] Do ponto do arco, {b}desça uma linha reta até o eixo horizontal. [p=0.3] Apareceu {c}um triângulo retângulo dentro do ciclo."),
    dict(id="s05", block="ciclo", text="E você já conhece os lados dele. [p=0.2] {a}A hipotenusa é o raio: vale um. [p=0.2] {b}O lado deitado é o cosseno de xis. [p=0.2] {c}O lado em pé é o seno de xis."),
    dict(id="s06", block="ciclo", text="Pitágoras diz: a soma dos quadrados dos catetos é o quadrado da hipotenusa. [p=0.3] {a}O seno ao quadrado, mais o cosseno ao quadrado, [p=0.2] dá um ao quadrado, que é um. [p=0.3] Essa é a {b}relação fundamental da trigonometria."),
    dict(id="s07", block="notacao", text="Na prova, ela vem escrita assim: [p=0.2] {a}seno ao quadrado de xis, mais cosseno ao quadrado de xis, igual a um. [p=0.3] {b}O dois colado no nome quer dizer: calcule o seno e eleve o resultado ao quadrado. [p=0.2] {c}Não é o ângulo que vai ao quadrado."),
    dict(id="s08", block="notacao", text="E ela vale em {a}qualquer quadrante: [p=0.2] fora do primeiro, seno e cosseno podem ser negativos, [p=0.2] mas {b}ao quadrado o sinal some. [p=0.3] Teste com trinta graus: [p=0.2] {c}o seno é um meio, e ao quadrado dá um quarto. [p=0.2] {d}O cosseno é raiz de três dividido por dois, e ao quadrado dá três quartos. [p=0.2] {e}Um quarto mais três quartos dá quatro quartos, um inteiro. [p=0.2] Bateu."),
    # exemplo
    dict(id="s09", block="exemplo", text="De volta ao problema do começo. [p=0.2] {a}Seno de xis igual a três quintos, com xis no primeiro quadrante. [p=0.3] {b}Três quintos ao quadrado: três vezes três em cima, cinco vezes cinco embaixo. [p=0.2] Dá {c}nove vinte e cinco avos."),
    dict(id="s10", block="exemplo", text="Então {a}o cosseno ao quadrado é um menos nove vinte e cinco avos. [p=0.3] Para tirar, escreva o um com o mesmo denominador: [p=0.2] {b}um inteiro são vinte e cinco vinte e cinco avos. [p=0.2] {c}Vinte e cinco menos nove dá dezesseis. [p=0.2] O cosseno ao quadrado vale {d}dezesseis vinte e cinco avos."),
    dict(id="s11", block="exemplo", text="Que número, ao quadrado, dá dezesseis vinte e cinco avos? [p=0.2] {a}Quatro quintos, ou menos quatro quintos. [p=0.3] Quem decide é {b}o quadrante. [p=0.2] No primeiro, o ponto fica à direita, e {c}o cosseno é positivo. [p=0.2] {d}Cosseno de xis igual a quatro quintos."),
    dict(id="s12", block="exemplo", text="E a tangente? [p=0.2] Como no triângulo, {a}tangente é o seno dividido pelo cosseno. [p=0.2] {b}Três quintos dividido por quatro quintos: [p=0.2] os quintos se cancelam, [p=0.2] e fica {c}três quartos. [p=0.3] Só não existe quando {d}o cosseno é zero, como em noventa graus."),
    # erro
    dict(id="s13", block="erro", text="O erro mais comum é {a}esquecer os quadrados [p=0.2] e fazer {b}cosseno igual a um menos o seno. [p=0.2] {c}Um menos três quintos dá dois quintos. [p=0.3] Teste: {d}dois quintos ao quadrado dá quatro vinte e cinco avos. [p=0.2] {e}Somando com nove vinte e cinco avos, dá treze vinte e cinco avos, [p=0.2] que nem chega a um. [p=0.3] {f}A relação é entre os quadrados."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: {a}desenhe o triângulo. [p=0.2] Seno três quintos é {b}oposto três e hipotenusa cinco. [p=0.3] É o famoso triângulo de lados três, quatro e cinco: [p=0.2] {c}o cateto que falta é quatro. [p=0.2] {d}Cosseno, quatro quintos. [p=0.2] {e}Tangente, três quartos. [p=0.2] Sem conta de fração."),
    dict(id="s15", block="atalho", text="Funciona porque {a}a relação fundamental é o próprio Pitágoras. [p=0.3] Mas o triângulo só dá {b}o tamanho, nunca o sinal. [p=0.2] {c}Fora do primeiro quadrante, o sinal vem do quadrante. [p=0.3] E se os lados não formarem um trio conhecido, [p=0.2] {d}faça a conta de Pitágoras no papel."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}O cosseno de um ângulo vale oito dezessete avos, [p=0.2] e o ângulo está {b}no quarto quadrante. [p=0.3] {c}Calcule o seno e a tangente desse ângulo."),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá, pelo triângulo. [p=0.2] {a}Cateto deitado oito, hipotenusa dezessete. [p=0.2] O outro cateto: {b}dezessete ao quadrado dá duzentos e oitenta e nove. [p=0.2] {c}Oito ao quadrado dá sessenta e quatro. [p=0.2] {d}A diferença dá duzentos e vinte e cinco, [p=0.2] e {e}a raiz dá quinze."),
    dict(id="s19", block="resposta", text="E o sinal? [p=0.2] No quarto quadrante, o ponto fica {a}abaixo do eixo horizontal: o seno é negativo. [p=0.3] {b}Seno: menos quinze dezessete avos. [p=0.2] {c}Tangente: menos quinze dividido por oito, que dá menos quinze oitavos. [p=0.3] Conferindo: {d}duzentos e vinte e cinco mais sessenta e quatro dá duzentos e oitenta e nove. [p=0.2] Bateu."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}seno ao quadrado mais cosseno ao quadrado dá um. [p=0.2] {b}A conta dá o tamanho, [p=0.2] e {c}o quadrante dá o sinal."),
    dict(id="s21", block="fim", text="Na próxima aula, o seno e o cosseno viram {a}desenho: [p=0.2] você conhece {b}a onda de cada um [p=0.2] e lê o período e a imagem de {c}ípsilon igual a três vezes o seno de xis. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
