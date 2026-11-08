# Estudativo · MAT-ANG-014 — Praticando: Tales e semelhança (Matemática · Geometria Plana: Ângulos e Triângulos · prática).
# Habilidade: resolver questões de paralelas e de triângulos semelhantes separando as figuras encaixadas.
# Pré-requisitos: MAT-ANG-010, MAT-ANG-011, MAT-ANG-012, MAT-ANG-013. Próxima: MAT-ANG-015.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questões inéditas, criadas para esta aula. Letras narradas como se falam: "á", "bê", "cê", "dê", "eme", "ene".
# Termos das aulas anteriores: "cruz", "está para", "mesma ordem", "fator", "atalho das partes" (bissetriz), "lado inteiro", "lado de frente para o mesmo ângulo".
# Figuras:
#   Q1: três paralelas e duas transversais; pedaços 4 e 6 numa, x e x + 3 na outra (x = 6: 6 e 9).
#   Q2: triângulo com lados 10 e 15 e bissetriz até o lado de 20 (8 junto do 10, 12 junto do 15).
#   Q3: ABC com MN paralelo a BC, M em AB; AM = 6, MN = 8, BC = 12; pergunta MB (AB = 9, MB = 3). Triângulos separados na resposta.
#   Q4: "gravata": AC e BD se cruzam em M, AB paralelo a CD, AB em cima e CD embaixo; AB = 6, CD = 9, AM = 4, MC = x (6). Ângulos opostos pelo vértice em M e alternos internos em A e C.
#   Q5: vara de 1,5 m com sombra de 2 m; torre com sombra de 20 m (15 m).

TITULO = "Praticando: Tales e semelhança"

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
    dict(id="s01", block="gancho", text="{a}Cinco questões, criadas para esta aula, [p=0.2] com tudo de Tales e semelhança. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}Tales, com as frações na mesma ordem, [p=0.2] {b}o teorema da bissetriz, [p=0.2] {c}semelhança por dois ângulos [p=0.2] e {d}o lado inteiro nas figuras encaixadas. [p=0.3] Se alguma travar, procure a aula no canal."),
    # questão 1: Tales com expressão
    dict(id="s03", block="questao1", text="{a}Questão um. [p=0.2] Três retas paralelas cortam duas transversais. [p=0.2] Numa transversal, os pedaços medem {b}quatro e seis. [p=0.2] Na outra, {c}xis e xis mais três. [p=0.3] {d}Quanto vale xis?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Mesma ordem nas frações: [p=0.2] {a}quatro está para seis, assim como xis está para xis mais três. [p=0.3] Cruz: {b}quatro vezes, abre parênteses, xis mais três, igual a seis xis. [p=0.2] Distribuindo: {c}quatro xis mais doze igual a seis xis."),
    dict(id="s06", block="resposta1", text="{a}Tire quatro xis de cada lado: doze igual a dois xis. [p=0.2] {b}Xis igual a seis. [p=0.3] Os pedaços da segunda transversal medem {c}seis e nove. [p=0.2] Conferindo: {d}quatro sextos e seis nonos, simplificados, dão dois terços. [p=0.2] Bateu."),
    # questão 2: bissetriz
    dict(id="s07", block="questao2", text="{a}Questão dois. [p=0.2] Num triângulo, {b}dois lados medem dez e quinze centímetros. [p=0.2] A bissetriz do ângulo entre eles corta {c}o lado da frente, que mede vinte centímetros. [p=0.3] {d}Quanto mede cada pedaço?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá, pelo atalho das partes. [p=0.2] {a}Dez e quinze, divididos por cinco, ficam dois e três. [p=0.2] O lado de vinte tem {b}cinco partes, e vinte dividido por cinco dá quatro. [p=0.3] {c}Junto do lado de dez ficam duas partes, que dão oito centímetros. [p=0.2] {d}Junto do lado de quinze ficam três partes, que dão doze centímetros."),
    dict(id="s10", block="resposta2", text="Quem respondeu {a}dez e dez esqueceu que a bissetriz divide o ângulo ao meio, não o lado. [p=0.3] E quem pôs {b}o doze junto do lado de dez ligou o pedaço ao lado errado. [p=0.2] {c}O pedaço maior fica junto do lado maior."),
    # questão 3: encaixados
    dict(id="s11", block="questao3", text="{a}Questão três. [p=0.2] No triângulo á bê cê, {b}o segmento eme ene é paralelo a bê cê, com eme no lado á bê. [p=0.3] {c}Á eme mede seis centímetros, eme ene mede oito, [p=0.2] e bê cê mede doze. [p=0.3] {d}Quanto mede eme bê?"),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] Separe os triângulos: {a}á eme ene e á bê cê. [p=0.2] Eles têm {b}o ângulo á em comum, e os ângulos em eme e em bê são correspondentes: semelhantes. [p=0.3] Use o lado inteiro: {c}seis está para á bê, assim como oito está para doze."),
    dict(id="s14", block="resposta3", text="Cruz: {a}oito vezes á bê igual a seis vezes doze, que dá setenta e dois. [p=0.2] {b}Á bê igual a nove. [p=0.3] Mas a pergunta é {c}eme bê, só o pedaço: [p=0.2] {d}nove menos seis dá três centímetros. [p=0.3] Quem parou no nove {e}respondeu o lado inteiro."),
    # questão 4: gravata
    dict(id="s15", block="questao4", text="{a}Questão quatro. [p=0.2] Os segmentos {b}á cê e bê dê se cruzam no ponto eme, [p=0.2] e {c}á bê é paralelo a cê dê. [p=0.3] {d}Á bê mede seis, cê dê mede nove e á eme mede quatro. [p=0.2] {e}Quanto mede eme cê?"),
    dict(id="s16", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta4", text="Vamos lá. [p=0.2] Os triângulos {a}á eme bê e cê eme dê têm ângulos opostos pelo vértice, no eme. [p=0.2] E {b}o ângulo em á é alterno interno do ângulo em cê. [p=0.3] Dois ângulos iguais: {c}semelhantes, mas um está de cabeça para baixo."),
    dict(id="s18", block="resposta4", text="A ordem vem dos ângulos: {a}á combina com cê, e bê com dê. [p=0.2] Então {b}á eme combina com cê eme, e á bê com cê dê. [p=0.3] {c}Quatro está para xis, assim como seis está para nove. [p=0.2] Cruz: {d}seis xis igual a quatro vezes nove, que dá trinta e seis. [p=0.2] {e}Xis igual a seis."),
    dict(id="s19", block="resposta4", text="Faz sentido: {a}o triângulo de baixo é o maior, [p=0.2] e {b}eme cê, com seis, é maior que á eme, com quatro."),
    # questão 5: sombra
    dict(id="s20", block="questao5", text="{a}Última questão. [p=0.2] Numa tarde de sol, {b}uma vara de um metro e meio faz sombra de dois metros. [p=0.2] No mesmo instante, {c}uma torre faz sombra de vinte metros. [p=0.3] {d}Qual é a altura da torre?"),
    dict(id="s21", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="resposta5", text="Vamos lá. [p=0.2] Altura está para sombra: [p=0.2] {a}um vírgula cinco está para dois, assim como xis está para vinte. [p=0.2] Cruz: {b}dois xis igual a um vírgula cinco vezes vinte, que dá trinta. [p=0.2] {c}Xis igual a quinze metros."),
    # atalho
    dict(id="s23", block="atalho", text="Pelo fator, sai mais rápido: {a}vinte é dez vezes dois. [p=0.2] Então a altura é {b}dez vezes um metro e meio, que dá quinze metros. [p=0.3] Funciona porque {c}semelhança multiplica todos os lados pelo mesmo número. [p=0.2] Não compensa quando {d}a sombra grande não é múltiplo da pequena: [p=0.2] aí, vá de cruz."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: {a}monte as frações sempre na mesma ordem, [p=0.2] {b}siga os ângulos para achar os lados correspondentes [p=0.2] e {c}separe as figuras encaixadas, usando o lado inteiro."),
    dict(id="s25", block="fim", text="Na próxima aula, começa uma parte nova: [p=0.2] {a}o Teorema de Pitágoras. [p=0.2] Num triângulo retângulo, você acha {b}o lado maior quando os outros medem seis e oito, [p=0.2] e {c}um lado menor quando o maior mede treze e o outro, cinco. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
