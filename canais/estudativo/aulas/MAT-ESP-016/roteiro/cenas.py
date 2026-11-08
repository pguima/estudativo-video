# Estudativo · MAT-ESP-016 — Praticando: pirâmides, cones e esfera (Matemática · Geometria Espacial · Esfera · prática).
# Habilidade: escolher a fórmula de cada sólido e resolver questões de casquinha, tenda, bola e reservatório.
# Pré-requisitos: MAT-ESP-011, MAT-ESP-012, MAT-ESP-013, MAT-ESP-014, MAT-ESP-015. Usa MAT-ANG-016 (terno 3-4-5), MAT-MED-005 (1 cm³ = 1 mL; 1.000 cm³ = 1 L; 1 m³ = 1.000 L), MAT-NUM-010 (divisão com resto). Próxima: MAT-ESP-017.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso.
# Questões inéditas, criadas para esta aula. Termos das aulas anteriores: apótema, geratriz, "círculo do meio", hemisfério, atalho do pi igual a três.
# Contas: 1) tenda lado 8, altura 3: apótema da base 4 → apótema 5 (3-4-5); lateral 4·(8·5/2) = 80 m² = 32·5/2; erro com 3: 32·3/2 = 48.
#   2) casquinha r = 3, h = 10, π = 3: r²h = 9·10 = 90 cm³ = 90 mL (= π·9·10/3 = 30π). Erro sem ÷3: 3·9·10 = 270.
#   P) pipoca h = 12: cone r = 4: 16·12 = 192; pirâmide lado 7: 49·(12/3) = 196 → pirâmide, +4 cm³.
#   3) bolinha r = 3, π = 3: 4r³ = 4·27 = 108 cm³; 1.000 ÷ 108 = 9, resto 28 → 9 bolinhas (9·108 = 972).
#   4) hemisfério r = 2, π = 3: esfera 4·8 = 32 m³, metade 16 m³ = 16.000 L; chapa sem tampa: 2 círculos = 2·3·4 = 24 m².
# Visual:
#   s03-s05: E.piramide quadrangular (tenda) com altura 3, apótema da base 4 e apótema 5 em triângulo retângulo.
#   s07-s09: E.cone de cabeça para baixo (casquinha), r = 3, h = 10. s10-s13: E.cone (r = 4) ao lado de E.piramide (lado 7), mesma altura 12; 192 contra 196.
#   s14-s17: E.esfera pequena repetida (bolinhas) ao lado de uma garrafa de 1 L.
#   s18-s21: meia E.esfera de boca para cima (reservatório), r = 2; a casca conta 2 círculos, sem tampa.

TITULO = "Praticando: pirâmides, cones e esfera"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações do dia a dia, [p=0.2] criadas para esta aula: [p=0.2] uma tenda, uma casquinha, pacotes de pipoca, bolinhas e um reservatório. [p=0.3] Em cada uma, o primeiro passo é {b}reconhecer o sólido. [p=0.2] Depois, {c}pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}três famílias de fórmulas. [p=0.2] {b}Pirâmide e cone: área da base vezes altura, dividido por três. [p=0.2] {c}Apótema e geratriz: Pitágoras, com a altura em pé. [p=0.2] {d}Esfera: quatro pi érre ao quadrado de área, [p=0.2] e quatro pi érre ao cubo, dividido por três, de volume. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: tenda (pirâmide, área)
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Uma tenda de festa tem forma de {b}pirâmide de base quadrada, [p=0.2] com {c}oito metros de lado e {d}três metros de altura. [p=0.3] {e}Quantos metros quadrados de lona cobrem as quatro paredes, sem o chão?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] As paredes são {a}quatro triângulos, [p=0.2] e a altura de cada um é {b}a apótema da pirâmide, não a altura da tenda. [p=0.3] {c}A apótema da base é a metade do lado, quatro. [p=0.2] Catetos três e quatro: {d}a apótema mede cinco."),
    dict(id="s06", block="resposta1", text="Pelo atalho, {a}o perímetro é trinta e dois. [p=0.2] {b}Trinta e dois vezes cinco dá cento e sessenta, [p=0.2] e {c}dividido por dois dá oitenta metros quadrados de lona. [p=0.3] Quem usasse a altura três na parede {d}acharia quarenta e oito, [p=0.2] e {e}faltaria lona."),
    # situação 2: casquinha (cone, volume)
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Uma casquinha de sorvete tem forma de {b}cone, [p=0.2] com {c}três centímetros de raio e {d}dez de altura. [p=0.2] {e}Use pi igual a três. [p=0.3] {f}Quantos mililitros de sorvete cabem dentro, até a borda?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Cone é {a}um terço do cilindro. [p=0.2] Com pi igual a três, {b}o três do pi cancela o dividido por três: [p=0.2] sobra {c}érre ao quadrado vezes agá. [p=0.3] {d}Três ao quadrado dá nove, [p=0.2] e {e}nove vezes dez dá noventa centímetros cúbicos. [p=0.2] Cabem {f}noventa mililitros. [p=0.3] Quem esquece o terço acha {g}duzentos e setenta, o triplo."),
    # situação 3: pipoca (cone contra pirâmide)
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] Dois pacotes de pipoca têm {b}a mesma altura, doze centímetros. [p=0.2] Um é {c}um cone de quatro centímetros de raio. [p=0.2] O outro é {d}uma pirâmide de base quadrada, com sete centímetros de lado. [p=0.2] {e}Use pi igual a três. [p=0.3] {f}Qual cabe mais pipoca?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="{a}Cone e pirâmide são um terço do sólido de mesma base e mesma altura. [p=0.2] Cone, pelo atalho do pi: {b}quatro ao quadrado dá dezesseis, [p=0.2] e {c}dezesseis vezes doze dá cento e noventa e dois. [p=0.3] Pirâmide, dividindo por três primeiro: {d}sete ao quadrado dá quarenta e nove, [p=0.2] {e}doze dividido por três dá quatro, [p=0.2] e {f}quarenta e nove vezes quatro dá cento e noventa e seis."),
    dict(id="s13", block="resposta3", text="{a}A pirâmide cabe mais, quatro centímetros cúbicos a mais. [p=0.3] E olhe que a boca do cone tem {b}oito centímetros de largura, mais que o lado sete. [p=0.2] No olho, você chutaria o cone. [p=0.2] {c}A conta decide."),
    # situação 4: bolinhas (esfera, volume)
    dict(id="s14", block="questao4", text="{a}Situação quatro. [p=0.2] Uma fábrica tem {b}um litro de borracha [p=0.2] e faz {c}bolinhas maciças de três centímetros de raio. [p=0.2] {d}Use pi igual a três. [p=0.3] {e}Quantas bolinhas inteiras ela consegue fazer?"),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="Vamos lá. [p=0.2] Bolinha é {a}esfera. [p=0.2] Com pi igual a três, o volume vira {b}quatro érre ao cubo. [p=0.2] {c}Três ao cubo dá vinte e sete, [p=0.2] e {d}quatro vezes vinte e sete dá cento e oito centímetros cúbicos por bolinha."),
    dict(id="s17", block="resposta4", text="{a}Um litro são mil centímetros cúbicos. [p=0.2] {b}Mil dividido por cento e oito dá nove, [p=0.2] e {c}sobram vinte e oito. [p=0.3] Vinte e oito não fazem outra bolinha. [p=0.2] Resposta: {d}nove bolinhas."),
    # situação 5: reservatório (hemisfério)
    dict(id="s18", block="questao5", text="{a}Última situação. [p=0.2] Um reservatório tem forma de {b}meia esfera, com a boca para cima e sem tampa, [p=0.2] e {c}dois metros de raio. [p=0.2] {d}Use pi igual a três. [p=0.3] {e}Quantos litros ele guarda? [p=0.2] {f}E quantos metros quadrados de chapa formam a casca?"),
    dict(id="s19", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta5", text="Vamos lá. [p=0.2] Meia esfera é {a}o hemisfério. [p=0.2] Esfera inteira, pelo atalho: {b}quatro vezes dois ao cubo, que dá trinta e dois. [p=0.2] {c}Metade dá dezesseis metros cúbicos. [p=0.2] {d}Cada metro cúbico guarda mil litros: [p=0.2] {e}dezesseis mil litros."),
    dict(id="s21", block="resposta5", text="Agora a chapa. [p=0.2] Conte círculos: {a}a meia casca vale dois círculos do meio. [p=0.2] E aqui {b}não tem tampa, então não entra o terceiro. [p=0.3] {c}Um círculo: três vezes dois ao quadrado dá doze. [p=0.2] {d}Dois círculos dão vinte e quatro metros quadrados de chapa."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}reconheça o sólido, [p=0.2] {b}veja se a pergunta quer o espaço de dentro ou a casca, [p=0.2] e {c}confira se a altura é a de dentro ou a inclinada."),
    dict(id="s23", block="fim", text="Na próxima aula, você junta sólidos: [p=0.2] {a}um silo feito de cilindro com um cone em cima [p=0.2] e {b}uma peça com um furo cilíndrico. [p=0.2] É só {c}somar e subtrair volumes. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
