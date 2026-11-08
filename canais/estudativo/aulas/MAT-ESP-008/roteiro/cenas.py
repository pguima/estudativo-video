# Estudativo · MAT-ESP-008 — Cilindro: área e volume (Matemática · Geometria Espacial · Prismas e cilindros).
# Habilidade: calcular o volume de uma lata de raio 5 cm e altura 10 cm com π = 3 (750 cm³, ou 750 mL) e a área de metal gasta.
# Pré-requisitos: MAT-ESP-007 (volume = área da base · altura), MAT-ARE-008 (A = πr²). Usa MAT-ESP-002 (lateral = retângulo de largura 2πr, "rótulo"), MAT-MED-005 (cm³ = mL), MAT-FAT-002 (fator comum, no atalho). Próxima: MAT-ESP-009.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso.

TITULO = "Cilindro: área e volume"

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
    dict(id="s01", block="gancho", text="{a}Uma lata com cinco centímetros de raio e dez de altura. [p=0.3] Se você {b}dobrar a altura, cabe o dobro. [p=0.2] Fácil. [p=0.3] Mas se {c}dobrar o raio, [p=0.2] cabe {d}quatro vezes o que cabia."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula quanto cabe num cilindro [p=0.2] e quanto material ele gasta, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}o volume do prisma é a área da base vezes a altura; [p=0.2] {c}a área do círculo é pi érre ao quadrado; [p=0.2] e {d}a volta da circunferência mede dois pi érre. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é
    dict(id="s04", block="cilindro", text="{a}O cilindro parece um prisma de base redonda: [p=0.2] {b}dois círculos iguais, a tampa e o fundo, [p=0.2] ligados por {c}uma lateral curva. [p=0.3] Lata, cano, caixa-d'água redonda: [p=0.2] tudo cilindro. [p=0.2] {d}A altura é a distância entre a tampa e o fundo."),
    # volume
    dict(id="s05", block="volume", text="O volume segue a ideia do prisma: [p=0.2] {a}camadas com a forma da base, uma sobre a outra. [p=0.3] {b}Volume é a área da base vezes a altura, [p=0.2] e a base é um círculo. [p=0.2] Na fórmula: {c}vê igual a pi érre ao quadrado vezes agá. [p=0.2] {d}Érre é o raio da tampa, [p=0.1] {e}agá é a altura."),
    dict(id="s06", block="volume", text="Na lata, com {a}pi igual a três: [p=0.2] {b}cinco ao quadrado dá vinte e cinco, [p=0.2] e {c}três vezes vinte e cinco dá setenta e cinco centímetros quadrados de fundo. [p=0.3] {d}Vezes dez dá setecentos e cinquenta centímetros cúbicos."),
    dict(id="s07", block="volume", text="E {a}um centímetro cúbico é um mililitro. [p=0.2] A lata guarda {b}setecentos e cinquenta mililitros: [p=0.2] {c}três quartos de litro."),
    dict(id="s08", block="dobro", text="E o começo da aula? [p=0.2] {a}Dobrando a altura, são vinte camadas de um centímetro, no lugar de dez: [p=0.2] o dobro. [p=0.3] {b}Dobrando o raio, o fundo vira três vezes dez ao quadrado, [p=0.2] que dá trezentos. [p=0.2] É {c}quatro vezes o fundo de antes, [p=0.2] porque o raio entra {d}ao quadrado."),
    # área
    dict(id="s09", block="area", text="E quanto metal? [p=0.2] {a}Abra a lata, como um molde. [p=0.2] Saem {b}dois círculos, a tampa e o fundo, [p=0.2] e {c}a lateral, que desenrola num retângulo, como o rótulo."),
    dict(id="s10", block="area", text="A altura desse retângulo é {a}a altura da lata, dez. [p=0.2] A largura é {b}a volta do círculo, dois pi érre, [p=0.2] porque a lateral dava a volta inteira na tampa. [p=0.3] {c}Duas vezes três vezes cinco dá trinta centímetros."),
    dict(id="s11", block="area", text="{a}Lateral: trinta vezes dez dá trezentos. [p=0.2] {b}Tampa e fundo: duas vezes setenta e cinco dá cento e cinquenta. [p=0.3] {c}Trezentos mais cento e cinquenta dá quatrocentos e cinquenta centímetros quadrados de metal."),
    dict(id="s12", block="area", text="Na fórmula: {a}área total é dois pi érre ao quadrado, das duas bases, [p=0.2] {b}mais dois pi érre agá, da lateral."),
    # erro comum
    dict(id="s13", block="erro", text="O erro mais comum é {a}usar o diâmetro no lugar do raio. [p=0.2] A prova diz: {b}lata de dez centímetros de diâmetro e dez de altura. [p=0.2] Quem põe dez no érre faz {c}três vezes cem vezes dez, e acha três mil. [p=0.3] {d}Quatro vezes o certo, [p=0.2] como dobrar o raio. [p=0.2] {e}Primeiro, divida o diâmetro por dois: raio cinco."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho, para a área total: [p=0.2] {a}dois pi érre, vezes raio mais altura. [p=0.3] {b}Duas vezes três vezes cinco dá trinta. [p=0.2] {c}Cinco mais dez dá quinze. [p=0.2] {d}Trinta vezes quinze dá quatrocentos e cinquenta. [p=0.2] Duas contas pequenas."),
    dict(id="s15", block="atalho", text="Funciona porque {a}dois pi érre aparece nas duas partes: [p=0.2] é {b}o fator comum, colocado em evidência. [p=0.3] {c}Não compensa em copo ou lata sem tampa: [p=0.2] aí só tem um círculo, [p=0.2] e você {d}soma as partes uma a uma."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Uma lata tem {a}raio de quatro centímetros e {b}altura de dez. [p=0.2] {c}Use pi igual a três. [p=0.3] {d}Quantos mililitros cabem nela? [p=0.2] {e}E quanto metal ela gasta, com tampa e fundo?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] Fundo: {a}quatro ao quadrado dá dezesseis, [p=0.2] e {b}três vezes dezesseis dá quarenta e oito centímetros quadrados. [p=0.2] {c}Vezes dez dá quatrocentos e oitenta centímetros cúbicos: [p=0.2] {d}quatrocentos e oitenta mililitros."),
    dict(id="s19", block="resposta", text="No metal, pelo atalho: [p=0.2] {a}duas vezes três vezes quatro dá vinte e quatro. [p=0.2] {b}Quatro mais dez dá catorze. [p=0.2] {c}Vinte e quatro vezes catorze dá trezentos e trinta e seis centímetros quadrados."),
    dict(id="s20", block="resposta", text="Conferindo pelas partes: [p=0.2] {a}a lateral tem vinte e quatro vezes dez, que dá duzentos e quarenta. [p=0.2] {b}Tampa e fundo, duas vezes quarenta e oito, que dá noventa e seis. [p=0.2] {c}Somando, trezentos e trinta e seis. [p=0.2] Bateu."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}volume, pi érre ao quadrado vezes a altura. [p=0.2] {b}Área, dois círculos mais um retângulo de largura dois pi érre."),
    dict(id="s22", block="fim", text="Na próxima aula, você enche uma caixa-d'água: [p=0.2] descobre {a}quanto o nível sobe [p=0.2] e {b}em quanto tempo ela enche, [p=0.2] ligando volume, altura e vazão. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
