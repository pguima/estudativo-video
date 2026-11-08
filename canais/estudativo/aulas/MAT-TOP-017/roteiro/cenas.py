# Estudativo · MAT-TOP-017 — Homotetia: ampliar a partir de um centro (Matemática · Tópicos Avançados · Troncos e transformações geométricas).
# Habilidade: ampliar uma figura pela razão 2 a partir de um ponto e dizer que os comprimentos dobram e a área fica 4 vezes maior.
# Pré-requisitos: MAT-ARE-010 (área vezes k², "cá"), MAT-POL-011 (reflexão, rotação e translação; corredor e elevador). Usa MAT-FUN-001
#   (plano cartesiano) e MAT-ARE-003 (área do triângulo). Próxima: MAT-TOP-018.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Letra k narrada "cá".
# Questão inédita, criada para esta aula. Pares narrados "xis dois, ípsilon um".
# Contas: (1, 1), (3, 1), (1, 2) × 2 → (2, 2), (6, 2), (2, 4); base 2 → 4, altura 1 → 2; áreas 1 → 4.
#   Centro (1, 1), ponto (3, 2): caminho (2, 1) × 2 = (4, 2) → (5, 3). Questão: (2, 1), (4, 1), (2, 3) × 3 → (6, 3), (12, 3), (6, 9);
#   área 2 · 2 / 2 = 2 → 2 · 9 = 18; conferência 6 · 6 / 2 = 18.

TITULO = "Homotetia: ampliar uma figura a partir de um centro"

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
    dict(id="s01", block="gancho", text="Ponha a mão {a}entre uma lanterna e a parede. [p=0.2] A sombra é {b}a mesma mão, só que maior. [p=0.3] Se a sombra tem o dobro do tamanho, a área dela é o dobro? [p=0.2] {c}Não: é quatro vezes maior."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você amplia uma figura a partir de um ponto, [p=0.2] diz o que acontece com os comprimentos e com a área [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}refletir, girar e deslizar mudam a figura de lugar, mas não de tamanho; [p=0.2] e {c}em figuras semelhantes, se os lados são multiplicados por cá, a área é multiplicada por cá ao quadrado. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="definicao", text="A homotetia é {a}a transformação que muda o tamanho. [p=0.2] Ela tem {b}um centro, como a lanterna, [p=0.2] e {c}uma razão, cá, que diz quantas vezes ampliar."),
    dict(id="s05", block="definicao", text="Para ampliar um ponto: [p=0.2] {a}ligue o centro ao ponto, [p=0.2] {b}continue na mesma direção, [p=0.2] e pare quando a distância até o centro {c}ficar cá vezes maior. [p=0.3] Com cá igual a dois, {d}o ponto vai para o dobro da distância."),
    # no plano
    dict(id="s06", block="plano", text="No plano, ponha {a}o centro na origem. [p=0.2] O triângulo tem vértices em {b}xis um, ípsilon um; xis três, ípsilon um; e xis um, ípsilon dois. [p=0.3] Com cá igual a dois, {c}cada coordenada dobra."),
    dict(id="s07", block="plano", text="{a}Xis um, ípsilon um, vai para xis dois, ípsilon dois. [p=0.2] {b}Xis três, ípsilon um, vai para xis seis, ípsilon dois. [p=0.2] {c}Xis um, ípsilon dois, vai para xis dois, ípsilon quatro."),
    dict(id="s08", block="plano", text="Compare os dois triângulos. [p=0.2] {a}A base era dois e virou quatro. [p=0.2] {b}A altura era um e virou dois. [p=0.2] Os comprimentos {c}dobram. [p=0.3] {d}Os ângulos não mudam, [p=0.2] e cada lado novo {e}fica paralelo ao antigo."),
    dict(id="s09", block="plano", text="E a área? [p=0.2] {a}Antes: dois vezes um, dividido por dois, um. [p=0.2] {b}Depois: quatro vezes dois, dividido por dois, quatro. [p=0.3] {c}Cá ao quadrado: dois ao quadrado, quatro vezes maior."),
    # centro fora da origem
    dict(id="s10", block="centro", text="E se o centro não está na origem? [p=0.2] Conte {a}o caminho do centro até o ponto, [p=0.2] {b}multiplique esse caminho por cá, [p=0.2] e {c}ande de novo, a partir do centro."),
    dict(id="s11", block="centro", text="Centro em {a}xis um, ípsilon um; ponto em {b}xis três, ípsilon dois; e cá igual a dois. [p=0.2] Do centro ao ponto: {c}dois para a direita e um para cima. [p=0.2] Dobrando: {d}quatro para a direita e dois para cima. [p=0.2] A partir do centro, chega em {e}xis cinco, ípsilon três."),
    dict(id="s12", block="centro", text="Com {a}cá entre zero e um, a figura encolhe. [p=0.2] {b}Cá igual a um meio deixa os comprimentos pela metade [p=0.2] e {c}a área com um quarto."),
    # erro
    dict(id="s13", block="erro", text="Agora, cuidado com o erro mais comum: [p=0.2] {a}achar que a área dobra junto com os lados. [p=0.2] Um quadradinho de lado um, {b}ampliado com cá igual a dois, [p=0.2] vira um quadrado de lado dois. [p=0.3] {c}Dentro dele cabem quatro quadradinhos, não dois."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho, para achar {a}o centro de uma homotetia já feita: [p=0.2] {b}ligue cada ponto à sua imagem e prolongue. [p=0.2] {c}As retas se cruzam no centro. [p=0.3] E a razão é {d}um lado novo dividido pelo lado antigo correspondente."),
    dict(id="s15", block="atalho", text="Funciona porque cada ponto e a sua imagem {a}estão na mesma reta que passa pelo centro. [p=0.3] {b}Não compensa quando o centro é a origem: [p=0.2] aí, basta ver por quanto as coordenadas foram multiplicadas."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Um triângulo tem vértices em {a}xis dois, ípsilon um; xis quatro, ípsilon um; e xis dois, ípsilon três. [p=0.2] Faça a homotetia de {b}centro na origem e razão três. [p=0.3] {c}Quais são os novos vértices? [p=0.2] E {d}quanto vale a nova área?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Multiplique cada coordenada por três: [p=0.2] {b}xis seis, ípsilon três; [p=0.2] {c}xis doze, ípsilon três; [p=0.2] e {d}xis seis, ípsilon nove."),
    dict(id="s19", block="resposta", text="{a}A área antiga: base dois, altura dois, dividido por dois: dois. [p=0.2] {b}Cá ao quadrado é nove. [p=0.2] {c}Nova área: dois vezes nove, dezoito. [p=0.3] Confira: {d}base seis, altura seis, dividido por dois: dezoito."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}a homotetia amplia ou reduz a partir de um centro; [p=0.2] {b}os comprimentos ficam vezes cá; [p=0.2] e {c}a área fica vezes cá ao quadrado."),
    dict(id="s21", block="fim", text="Na próxima aula, você pratica {a}bases de contagem e algarismos significativos, [p=0.2] {b}troncos e homotetia, em questões novas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
