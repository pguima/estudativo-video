# Estudativo · MAT-ESP-012 — Pirâmide: altura, apótema e área (Matemática · Geometria Espacial · Pirâmides e cones).
# Habilidade: achar com Pitágoras a apótema de uma pirâmide de base quadrada de lado 6 e altura 4 (5) e somar as faces para a área total (96).
# Pré-requisitos: MAT-ESP-011 (pirâmide, vértice, altura por dentro), MAT-ANG-016 (ternos 3-4-5 e 5-12-13). Usa MAT-ANG-015 (Pitágoras), MAT-ARE-003 (b·h/2), MAT-ESP-007 (atalho perímetro · altura). Próxima: MAT-ESP-013.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Só pirâmide regular de base quadrada.

TITULO = "Pirâmide: altura, apótema e área"

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
    dict(id="s01", block="gancho", text="{a}Uma pirâmide de base quadrada, com {b}lado seis e altura quatro. [p=0.2] Cada face lateral é um triângulo de base seis. [p=0.3] E a altura desse triângulo? [p=0.2] Muita gente diz {c}quatro. [p=0.2] É {d}cinco, [p=0.2] e isso muda a área toda."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha a altura das faces de uma pirâmide [p=0.2] e calcula a área total, [p=0.2] com um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}a altura da pirâmide desce do vértice até a base, em pé, por dentro; [p=0.2] {c}o teorema de Pitágoras; [p=0.2] e {d}os ternos, como três, quatro e cinco. [p=0.3] Se faltar alguma, procure no canal."),
    # apótema
    dict(id="s04", block="apotema", text="{a}A altura de uma face lateral tem nome: [p=0.2] {b}apótema da pirâmide. [p=0.2] Ela sai do vértice e desce {c}pelo meio da face, [p=0.2] até {d}o meio de uma aresta da base."),
    dict(id="s05", block="apotema", text="Então são {a}duas alturas diferentes. [p=0.2] {b}A altura da pirâmide desce por dentro, em pé, até o centro da base. [p=0.2] {c}A apótema desce inclinada, deitada sobre a face. [p=0.3] Por ser inclinada, ela é {d}mais comprida."),
    dict(id="s06", block="triangulo", text="Ligue {a}o centro da base ao meio de uma aresta. [p=0.2] Esse segmento se chama {b}apótema da base, [p=0.2] e no quadrado mede {c}a metade do lado: três."),
    dict(id="s07", block="triangulo", text="Aparece {a}um triângulo retângulo em pé, dentro da pirâmide. [p=0.2] {b}A altura e a apótema da base são os catetos, [p=0.2] e {c}a apótema da pirâmide é a hipotenusa, de frente para o ângulo reto."),
    dict(id="s08", block="triangulo", text="Catetos {a}três e quatro: [p=0.2] é o terno {b}três, quatro e cinco. [p=0.2] {c}A apótema mede cinco. [p=0.3] Por Pitágoras: {d}nove mais dezesseis dá vinte e cinco, [p=0.2] e {e}a raiz de vinte e cinco é cinco."),
    # área
    dict(id="s09", block="area", text="E a área? [p=0.2] {a}Abra a pirâmide como um molde: [p=0.2] {b}um quadrado no meio [p=0.2] e {c}quatro triângulos iguais em volta. [p=0.3] Cada triângulo tem {d}base seis e altura cinco, a apótema. [p=0.2] {e}Seis vezes cinco dividido por dois dá quinze."),
    dict(id="s10", block="area", text="{a}Quatro faces: quatro vezes quinze dá sessenta. [p=0.2] Essa é a área lateral. [p=0.2] {b}Base: seis ao quadrado dá trinta e seis. [p=0.3] {c}Área total: sessenta mais trinta e seis dá noventa e seis."),
    # erro comum
    dict(id="s11", block="erro", text="O erro mais comum é {a}usar a altura da pirâmide na face. [p=0.2] Com quatro no lugar de cinco, {b}cada face dá doze, [p=0.2] {c}as quatro dão quarenta e oito, [p=0.2] e o total cai para {d}oitenta e quatro. [p=0.3] {e}A altura de dentro serve para achar a apótema e para o volume. [p=0.2] Na face, só a apótema."),
    # atalho
    dict(id="s12", block="atalho", text="Agora o atalho, para a área lateral: [p=0.2] {a}perímetro da base vezes a apótema, dividido por dois. [p=0.3] {b}O perímetro é quatro vezes seis, que dá vinte e quatro. [p=0.2] {c}Vinte e quatro vezes cinco dá cento e vinte, [p=0.2] e {d}dividido por dois dá sessenta."),
    dict(id="s13", block="atalho", text="É o atalho do prisma, {a}com o dividido por dois do triângulo. [p=0.2] Funciona porque {b}as faces são triângulos iguais, com a mesma altura: [p=0.2] somar as bases de todas é somar o contorno da base. [p=0.3] {c}Não compensa se as faces forem diferentes, como numa base retangular: [p=0.2] aí, {d}calcule face por face."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Um enfeite de vidro tem forma de {a}pirâmide de base quadrada, [p=0.2] com {b}dez centímetros de lado e {c}doze de altura. [p=0.3] {d}Quanto vidro ele gasta, contando a base?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}A apótema da base é a metade do lado, cinco. [p=0.2] Catetos cinco e doze: [p=0.2] é o terno {b}cinco, doze e treze. [p=0.2] {c}A apótema da pirâmide mede treze."),
    dict(id="s17", block="resposta", text="Pelo atalho, {a}o perímetro é quarenta. [p=0.2] {b}Quarenta vezes treze dá quinhentos e vinte, [p=0.2] e {c}dividido por dois dá duzentos e sessenta. [p=0.3] {d}Base: dez ao quadrado dá cem. [p=0.2] {e}Total: duzentos e sessenta mais cem dá trezentos e sessenta centímetros quadrados de vidro."),
    dict(id="s18", block="resposta", text="Quem usasse a altura doze na face {a}acharia trezentos e quarenta. [p=0.2] {b}Faltariam vinte centímetros quadrados de vidro."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}a apótema é a hipotenusa do triângulo com a altura e a metade do lado. [p=0.2] {b}Área total, a base mais as faces laterais."),
    dict(id="s20", block="fim", text="Na próxima aula, esse mesmo triângulo aparece {a}no cone. [p=0.2] Com {b}raio três e altura quatro, [p=0.2] a geratriz, a linha inclinada do cone, mede {c}cinco. [p=0.2] E você calcula {d}o volume e a área lateral do cone. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
