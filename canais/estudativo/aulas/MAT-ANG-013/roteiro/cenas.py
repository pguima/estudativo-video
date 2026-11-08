# Estudativo · MAT-ANG-013 — Semelhança em problemas: sombras e triângulos encaixados (Matemática · Geometria Plana: Ângulos e Triângulos).
# Habilidade: achar a altura de um prédio pela sombra: um poste de 2 m com sombra de 3 m indica 20 m para um prédio com sombra de 30 m.
# Pré-requisitos: MAT-ANG-012 (semelhança por dois ângulos, lado de frente para o mesmo ângulo, cruz e fator). Próxima: MAT-ANG-014.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas como se falam: "á", "bê", "cê", "eme", "ene".
# MAT-ANG-011 (Tales no triângulo) não está em "Já ensinado": o erro comum não cita pedaço com pedaço como regra.
# Figuras: E.triangulo, E.segmento, E.angulo (ângulo reto e ângulo do raio com o chão).
#   s04-s06: poste de 2 m com sombra de 3 m e prédio com sombra de 30 m (x = 20); raios de sol paralelos, mesma inclinação.
#   s07-s12: ABC com MN paralelo a BC; AM = 3, MB = 6, MN = 4, BC = x (12). s09: os triângulos AMN e ABC desenhados separados, AB = 9.
#   s14: árvore com sombra de 12 m (8 m).
#   Questão: poste com lâmpada; pessoa de 1,60 m a 3 m do poste, sombra de 2 m; chão do triângulo grande = 5 m; lâmpada a 4 m. Erro com 3 m: 2,40 m.

TITULO = "Semelhança em problemas: sombras e triângulos encaixados"

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
    dict(id="s01", block="gancho", text="{a}Um poste de dois metros faz uma sombra de três metros. [p=0.3] Na mesma hora, {b}um prédio faz sombra de trinta metros. [p=0.3] Sem subir no prédio, dá para saber a altura dele: {c}vinte metros."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você mede alturas pela sombra, [p=0.2] {b}separa triângulos encaixados [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}dois ângulos iguais garantem triângulos semelhantes, [p=0.2] e {c}lado correspondente é o que fica de frente para o mesmo ângulo. [p=0.3] Se faltar alguma, procure no canal."),
    # sombra
    dict(id="s04", block="sombra", text="Onde estão os triângulos? [p=0.2] {a}O poste em pé, [p=0.1] {b}a sombra no chão [p=0.1] e {c}o raio de sol que liga a ponta do poste à ponta da sombra. [p=0.3] Com {d}o prédio, a mesma coisa."),
    dict(id="s05", block="sombra", text="Cada triângulo tem {a}um ângulo reto, entre o objeto em pé e o chão. [p=0.3] E o sol está tão longe que {b}os raios chegam paralelos. [p=0.2] Então eles batem no chão {c}com a mesma inclinação: [p=0.2] são ângulos correspondentes, iguais. [p=0.3] {d}Dois ângulos iguais: triângulos semelhantes."),
    dict(id="s06", block="sombra", text="{a}Altura está para sombra, em cada triângulo: [p=0.2] {b}dois está para três, assim como xis está para trinta. [p=0.3] Cruz: {c}três xis igual a dois vezes trinta, que dá sessenta. [p=0.2] {d}Xis igual a vinte metros."),
    # encaixados
    dict(id="s07", block="encaixados", text="Nem sempre os triângulos vêm separados. [p=0.2] Às vezes, {a}um está encaixado no outro. [p=0.3] No triângulo á bê cê, {b}o segmento eme ene é paralelo a bê cê. [p=0.2] {c}Á eme mede três, eme bê mede seis, [p=0.2] e {d}eme ene mede quatro. [p=0.2] Quanto mede bê cê?"),
    dict(id="s08", block="encaixados", text="{a}O pequeno, á eme ene, e o grande, á bê cê, têm o mesmo ângulo á. [p=0.2] E {b}o ângulo em eme é igual ao ângulo em bê: [p=0.2] correspondentes, por causa das paralelas. [p=0.3] {c}Dois ângulos iguais: semelhantes."),
    dict(id="s09", block="encaixados", text="O segredo é {a}desenhar os triângulos separados. [p=0.2] No pequeno: {b}lado á eme com três, e lado eme ene com quatro. [p=0.3] No grande, o lado que corresponde ao á eme é {c}o lado á bê inteiro: [p=0.2] três mais seis, que dá nove."),
    dict(id="s10", block="encaixados", text="{a}Três está para nove, assim como quatro está para xis. [p=0.2] Cruz: {b}três xis igual a nove vezes quatro, que dá trinta e seis. [p=0.2] {c}Xis igual a doze."),
    # erro
    dict(id="s11", block="erro", text="O erro mais comum é {a}usar o pedaço no lugar do lado inteiro. [p=0.2] A pessoa monta {b}três está para seis, assim como quatro está para xis, [p=0.2] e acha {c}xis igual a oito."),
    dict(id="s12", block="erro", text="Mas o seis é só {a}o pedaço de baixo, [p=0.2] e não é lado de nenhum dos triângulos. [p=0.3] Para achar o lado paralelo, {b}compare triângulo inteiro com triângulo inteiro."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho prometido, para sombras: [p=0.2] {a}calcule a razão da hora. [p=0.3] O poste tem dois metros de altura e três de sombra: [p=0.2] {b}a altura é dois terços da sombra. [p=0.2] Naquela hora, isso vale {c}para tudo que está em pé."),
    dict(id="s14", block="atalho", text="Prédio com sombra de trinta metros: [p=0.2] {a}trinta dividido por três dá dez; dez vezes dois dá vinte metros. [p=0.3] Árvore com sombra de doze metros: [p=0.2] {b}doze dividido por três dá quatro; quatro vezes dois dá oito metros. [p=0.2] Uma razão, {c}várias respostas."),
    dict(id="s15", block="atalho", text="Funciona porque, {a}no mesmo instante, todos os raios de sol têm a mesma inclinação, [p=0.2] e todos esses triângulos são semelhantes. [p=0.3] {b}Não vale com sombras medidas em horas diferentes: [p=0.2] o sol muda de lugar, e {c}a razão muda junto."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] À noite, {a}um poste com a lâmpada no alto ilumina uma pessoa de um metro e sessenta de altura. [p=0.2] Ela está parada {b}a três metros do poste, [p=0.2] e {c}a sombra dela no chão mede dois metros. [p=0.3] {d}A que altura está a lâmpada?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Aqui a luz sai de um ponto só, a lâmpada, [p=0.2] então {a}a razão da hora não serve. [p=0.3] O raio sai da lâmpada, {b}passa pela cabeça da pessoa e chega na ponta da sombra. [p=0.2] Ficam {c}triângulos encaixados, com o mesmo ângulo na ponta da sombra [p=0.2] e {d}um ângulo reto em cada um: semelhantes."),
    dict(id="s19", block="resposta", text="Separe. [p=0.2] No pequeno: {a}altura de um metro e sessenta, e chão de dois metros. [p=0.2] No grande: altura xis, [p=0.2] e o chão vai da ponta da sombra até o poste: {b}dois mais três, que dá cinco metros."),
    dict(id="s20", block="resposta", text="{a}Um vírgula seis está para dois, assim como xis está para cinco. [p=0.2] Cruz: {b}dois xis igual a um vírgula seis vezes cinco, que dá oito. [p=0.2] {c}Xis igual a quatro metros. [p=0.3] Quem usou só os três metros {d}achou dois metros e quarenta centímetros, e errou."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}objeto em pé e sombra formam triângulos semelhantes, [p=0.2] e {b}em figura encaixada, separe os triângulos e use o lado inteiro."),
    dict(id="s22", block="fim", text="Na próxima aula, você pratica {a}tudo de Tales e semelhança, [p=0.2] em questões com {b}paralelas, bissetriz, sombras e figuras encaixadas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
