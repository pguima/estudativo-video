# Estudativo · MAT-ANG-018 — Relações métricas no triângulo retângulo (Matemática · Geometria Plana: Ângulos e Triângulos).
# Habilidade: achar a altura relativa à hipotenusa com a · h = b · c e h² = m · n, como h = 2,4 no triângulo 3-4-5.
# Pré-requisitos: MAT-ANG-012 (semelhança por dois ângulos, razão entre lados correspondentes), MAT-ANG-015 (Pitágoras). Usa MAT-RAZ-002 (cruz, produto cruzado) e os ternos de MAT-ANG-016. Próxima: MAT-ANG-019.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Letras narradas como se falam: "á", "bê", "cê", "agá", "eme", "ene".
# Visual:
#   Triângulo retângulo com o ângulo reto em cima (vértice A) e a hipotenusa deitada embaixo; altura h de A até a hipotenusa, com quadradinho do reto.
#   Rótulos: hipotenusa a, catetos b (direita) e c (esquerda), pedaços m (sob o cateto c) e n (sob o cateto b). No 3-4-5: c = 3, b = 4, m = 1,8, n = 3,2.
#   s06-s07: o triângulo pequeno da esquerda (c, h, m) e o grande, separados e girados para mostrar os ângulos iguais (reto e o ângulo de baixo à esquerda).
#   s07: correspondência pelo ângulo da frente: h ↔ b, c ↔ a. Proporção h/b = c/a.
#   s10: os dois pequenos lado a lado: h (esq.) ↔ n (dir.), m (esq.) ↔ h (dir.). Proporção h/n = m/h.
#   s13: altura errada caindo no meio (2,5 e 2,5), em vermelho, sobre a certa (1,8 e 3,2).
#   s14: tabela 3-4-5 → 2,4; 6-8-10 → 4,8; 30-40-50 → 24.

TITULO = "Relações métricas no triângulo retângulo"

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
    dict(id="s01", block="gancho", text="{a}Triângulo retângulo de catetos três e quatro, hipotenusa cinco. [p=0.2] {b}Do ângulo reto, desça uma altura até a hipotenusa. [p=0.3] Quanto ela mede? [p=0.2] Muita gente diz {c}dois e meio. [p=0.2] É {d}dois vírgula quatro."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você acha essa altura com duas relações métricas, [p=0.2] contas rápidas entre as medidas do triângulo, [p=0.2] e leva {b}um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}o teorema de Pitágoras; [p=0.2] {c}triângulos com dois ângulos iguais são semelhantes, com os lados correspondentes proporcionais; [p=0.2] e {d}a proporção, resolvida pela cruz, o produto cruzado. [p=0.3] Se faltar alguma, procure no canal."),
    # nomes
    dict(id="s04", block="nomes", text="Primeiro, os nomes. [p=0.2] {a}Á é a hipotenusa. [p=0.2] {b}Bê e cê são os catetos. [p=0.2] {c}Agá é a altura relativa à hipotenusa: [p=0.2] sai do ângulo reto e chega na hipotenusa em ângulo reto."),
    dict(id="s05", block="nomes", text="Essa altura parte a hipotenusa em {a}dois pedaços, chamados {b}eme e ene. [p=0.2] São as projeções dos catetos: [p=0.2] {c}a sombra que cada cateto deixa sobre a hipotenusa."),
    # semelhança
    dict(id="s06", block="semelhanca", text="A altura cria {a}dois triângulos pequenos dentro do grande. [p=0.2] Cada um tem {b}um ângulo reto [p=0.2] e {c}um ângulo agudo em comum com o grande. [p=0.3] Dois ângulos iguais: [p=0.2] {d}os três triângulos são semelhantes."),
    # relação 1
    dict(id="s07", block="relacao1", text="Compare o pequeno da esquerda com o grande. [p=0.2] Lado correspondente é o que fica de frente para o mesmo ângulo. [p=0.3] {a}A altura fica de frente para o ângulo de baixo, à esquerda. [p=0.2] No grande, de frente para esse ângulo está o cateto bê. [p=0.2] {b}O cateto cê fica de frente para o ângulo reto do pequeno, como a hipotenusa á no grande. [p=0.3] Na mesma ordem: {c}agá está para bê assim como cê está para á."),
    dict(id="s08", block="relacao1", text="Cruz: {a}á vezes agá igual a bê vezes cê. [p=0.3] Em palavras: {b}hipotenusa vezes altura é igual a cateto vezes cateto."),
    dict(id="s09", block="relacao1", text="No triângulo três, quatro e cinco: [p=0.2] {a}cinco vezes agá igual a três vezes quatro, que dá doze. [p=0.2] {b}Divida cada lado da igualdade por cinco: [p=0.2] {c}agá igual a doze quintos. [p=0.2] Doze quintos é o mesmo que vinte e quatro décimos, [p=0.2] que se escreve dois vírgula quatro."),
    # relação 2
    dict(id="s10", block="relacao2", text="Agora, compare {a}os triângulos pequenos entre si. [p=0.2] Os três triângulos têm os mesmos ângulos, [p=0.2] então ache os correspondentes pelo ângulo da frente. [p=0.3] A altura, no da esquerda, e o pedaço ene, no da direita, ficam de frente para ângulos iguais. [p=0.2] O pedaço eme, no da esquerda, e a altura, no da direita, também. [p=0.3] {b}Agá está para ene assim como eme está para agá. [p=0.3] Cruz: {c}agá ao quadrado igual a eme vezes ene. [p=0.2] {d}A altura ao quadrado é o produto dos pedaços."),
    dict(id="s11", block="relacao2", text="Se a altura parte a hipotenusa em {a}quatro e nove: [p=0.2] {b}agá ao quadrado igual a quatro vezes nove, que dá trinta e seis. [p=0.2] {c}A altura é seis."),
    dict(id="s12", block="relacao2", text="No triângulo três, quatro e cinco, os pedaços medem {a}um vírgula oito e três vírgula dois. [p=0.2] {b}Um vírgula oito vezes três vírgula dois dá cinco vírgula setenta e seis. [p=0.2] E {c}dois vírgula quatro ao quadrado também dá cinco vírgula setenta e seis. [p=0.2] As duas relações concordam."),
    # erro
    dict(id="s13", block="erro", text="Voltando ao erro do começo. [p=0.2] Quem diz dois e meio imagina que {a}a altura cai no meio da hipotenusa, [p=0.2] com pedaços {b}de dois e meio cada. [p=0.2] Aí, {c}dois e meio vezes dois e meio dá seis vírgula vinte e cinco, [p=0.2] e a altura sairia dois e meio. [p=0.3] Mas os pedaços são {d}um vírgula oito e três vírgula dois. [p=0.2] A altura só cai no meio {e}quando os catetos são iguais."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho prometido: {a}guarde a altura do triângulo três, quatro e cinco, [p=0.2] que é dois vírgula quatro. [p=0.3] Nos múltiplos, {b}multiplique a altura também. [p=0.2] No seis, oito e dez, {c}a altura dá quatro vírgula oito. [p=0.2] No trinta, quarenta e cinquenta, {d}dá vinte e quatro."),
    dict(id="s15", block="atalho", text="Funciona porque {a}o triângulo ampliado é semelhante ao original: [p=0.2] {b}todas as medidas são multiplicadas pela mesma razão de semelhança, inclusive a altura. [p=0.3] {c}Não compensa fora dos ternos. [p=0.2] Aí, vale {d}hipotenusa vezes altura igual a cateto vezes cateto."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar, com duas perguntas. [p=0.2] {a}Um triângulo retângulo tem catetos nove e doze. [p=0.2] Quanto mede a altura relativa à hipotenusa? [p=0.3] {b}Em outro, essa altura parte a hipotenusa em dois e oito. [p=0.2] Quanto ela mede?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Nove e doze são o terno três, quatro e cinco multiplicado por três, [p=0.2] então {b}a hipotenusa é quinze. [p=0.2] {c}Quinze vezes agá igual a nove vezes doze, que dá cento e oito. [p=0.2] {d}Agá igual a cento e oito quinze avos. [p=0.2] Simplificando por três, dá trinta e seis quintos, [p=0.2] o mesmo que setenta e dois décimos, [p=0.2] que se escreve sete vírgula dois."),
    dict(id="s19", block="resposta", text="Pelo atalho, {a}dois vírgula quatro vezes três dá sete vírgula dois. [p=0.2] E {b}a altura ficou menor que cada cateto, como tem de ser."),
    dict(id="s20", block="resposta", text="Na segunda, só temos os pedaços: [p=0.2] {a}agá ao quadrado igual a dois vezes oito, que dá dezesseis. [p=0.2] {b}A altura é quatro."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}hipotenusa vezes altura é cateto vezes cateto, [p=0.2] e {b}a altura ao quadrado é o produto dos pedaços da hipotenusa."),
    dict(id="s22", block="fim", text="A próxima aula é {a}prática: [p=0.2] você escolhe entre Pitágoras, os atalhos e as relações métricas [p=0.2] para achar {b}medidas em figuras e situações reais. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
