# Estudativo · MAT-ESP-021 — Praticando: sólidos compostos e razão entre volumes (Matemática · Geometria Espacial · prática).
# Habilidade: separar um sólido em partes conhecidas e comparar volumes de sólidos ampliados ou encaixados.
# Pré-requisitos: MAT-ESP-017, MAT-ESP-018, MAT-ESP-019, MAT-ESP-020. Usa MAT-MED-005 (1 m³ = 1 000 L), MAT-POR-004 (fator 1,1).
#   Última aula da trilha Geometria Espacial; próxima na playlist Matemática do Zero: MAT-EST-001.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Letra k narrada "cá"; pi narrado "pi".
# Questões inéditas, criadas para esta aula. π = 3 em todas as contas.
# Contas: silo: fundo 3 · 9 = 27; cilindro 27 · 5 = 135; cone 27 · 2 / 3 = 18; total 153 m³ = 153 000 L.
#   Aquário 50 · 20 = 1 000; sobe 26 − 23 = 3 → 3 000 cm³ = 3 L; segunda pedra 26 + 3 = 29 > 28: transborda.
#   Lata: r = 3, h = 3 · 6 = 18; 3 · 9 = 27, · 18 = 486. Bola 27 · 4/3 = 36, · 3 = 108; três bolas 324; vazio 162 = 1/3 de 486.
#   Atalho: lata justa 2πr³, bola 4/3 πr³ → 2/3. Embalagem: 1,1² = 1,21; 1,1³ = 1,331 → 1 331 mL; aumento 33,1%.
# Visual:
#   s03-s06: E.cilindro raio 3, altura 5 com E.cone em cima, altura 2 (silo).
#   s07-s10: aquário (bloco) 50 × 20 × 28 com nível 23 → 26; borda em 28 marcada; segunda pedra levando a 29, água transbordando.
#   s11-s15: E.cilindro com três E.esfera empilhadas; raio e "altura = 3 diâmetros" marcados.
#   s16-s19: duas embalagens semelhantes (bloco), cada medida × 1,1.

TITULO = "Praticando: sólidos compostos e razão entre volumes"

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
    dict(id="s01", block="gancho", text="{a}Quatro situações, [p=0.2] criadas para esta aula, [p=0.2] para fechar a geometria espacial. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}quatro ferramentas: [p=0.2] {b}separar um sólido em partes conhecidas; [p=0.2] {c}medir um volume pela água que sobe; [p=0.2] {d}achar a medida que liga um sólido ao outro; [p=0.2] e {e}multiplicar o volume por cá ao cubo. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: silo
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Um silo é {b}um cilindro de três metros de raio e cinco de altura, [p=0.2] com {c}um telhado em forma de cone, de dois metros de altura, sobre a mesma base. [p=0.3] {d}Use pi igual a três. [p=0.2] {e}Quantos litros cabem no silo?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Separe em {a}duas peças conhecidas. [p=0.2] Cilindro e cone usam o mesmo fundo: {b}três ao quadrado dá nove, e três vezes nove dá vinte e sete metros quadrados. [p=0.3] {c}Cilindro: vinte e sete vezes cinco dá cento e trinta e cinco. [p=0.2] {d}Cone: vinte e sete vezes dois dá cinquenta e quatro, e dividido por três dá dezoito."),
    dict(id="s06", block="resposta1", text="{a}Cento e trinta e cinco mais dezoito dá cento e cinquenta e três metros cúbicos. [p=0.3] Como {b}um metro cúbico tem mil litros, [p=0.2] cabem {c}cento e cinquenta e três mil litros."),
    # situação 2: nível da água
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Um aquário tem {b}fundo de cinquenta centímetros por vinte [p=0.2] e {c}vinte e oito de altura. [p=0.2] A água está em vinte e três centímetros. [p=0.3] Uma pedra afundada faz a água subir para {d}vinte e seis. [p=0.2] {e}Qual é o volume da pedra? [p=0.2] E {f}uma segunda pedra igual cabe sem a água transbordar?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] O volume da pedra é {a}o volume da água que subiu. [p=0.2] Subiu {b}três centímetros. [p=0.2] {c}Cinquenta vezes vinte dá mil, [p=0.2] e {d}mil vezes três dá três mil centímetros cúbicos: três litros."),
    dict(id="s10", block="resposta2", text="A segunda pedra sobe mais {a}três centímetros: [p=0.2] {b}vinte e seis mais três dá vinte e nove. [p=0.2] O aquário tem só {c}vinte e oito de altura. [p=0.2] {d}A água transborda."),
    # situação 3: bolas na lata
    dict(id="s11", block="questao3", text="{a}Situação três. [p=0.2] {b}Três bolas de três centímetros de raio vão numa lata cilíndrica, [p=0.2] uma sobre a outra, {c}encostando no fundo, na tampa e na parede. [p=0.3] Com pi igual a três, {d}quanto da lata fica vazio?"),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] Primeiro, as frases que ligam as medidas. [p=0.2] {a}O raio da lata é o raio da bola: três. [p=0.2] {b}A altura da lata é de três diâmetros: três vezes seis dá dezoito."),
    dict(id="s14", block="resposta3", text="{a}Lata: três vezes nove dá vinte e sete de fundo, [p=0.2] e vezes dezoito dá quatrocentos e oitenta e seis. [p=0.3] {b}Uma bola: três ao cubo dá vinte e sete, [p=0.2] quatro terços disso dá trinta e seis, [p=0.2] e vezes três dá cento e oito. [p=0.2] {c}Três bolas dão trezentos e vinte e quatro."),
    dict(id="s15", block="resposta3", text="Vazio: {a}quatrocentos e oitenta e seis menos trezentos e vinte e quatro dá cento e sessenta e dois centímetros cúbicos. [p=0.3] {b}É um terço da lata."),
    # atalho
    dict(id="s16", block="atalho", text="E aqui cabe um atalho, que vem da aula da esfera: {a}bola em lata justa ocupa dois terços da lata, e sobra um terço. [p=0.3] Numa lata justa para uma bola, {b}a altura é dois raios. [p=0.2] A lata tem pi érre ao quadrado de fundo, vezes dois érre de altura: {c}dois pi érre ao cubo. [p=0.2] A bola tem {d}quatro pi érre ao cubo, dividido por três. [p=0.2] {e}Dois terços de dois dá quatro terços: [p=0.2] a bola é dois terços da lata, com qualquer valor de pi."),
    dict(id="s17", block="atalho", text="Com três bolas, {a}a lata tem três vezes a altura e guarda três vezes mais: [p=0.2] {b}continua dois terços. [p=0.3] {c}Não compensa quando as bolas não encostam na parede, [p=0.2] numa lata mais larga. [p=0.2] Aí, {d}faça as duas contas."),
    # situação 4: ampliação
    dict(id="s18", block="questao4", text="{a}Situação quatro. [p=0.2] Uma embalagem de {b}um litro vai ganhar uma versão maior e semelhante, [p=0.2] com {c}cada medida dez por cento maior. [p=0.3] {d}Quantos mililitros cabem na nova? [p=0.2] E {e}de quantos por cento aumenta o volume?"),
    dict(id="s19", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta4", text="Vamos lá. [p=0.2] Aumentar dez por cento é {a}multiplicar por um vírgula um. [p=0.2] Esse é o cá. [p=0.3] Volume: {b}um vírgula um ao cubo. [p=0.2] {c}Um vírgula um vezes um vírgula um dá um vírgula vinte e um. [p=0.2] {d}Vezes um vírgula um de novo dá um vírgula trezentos e trinta e um."),
    dict(id="s21", block="resposta4", text="Um litro tem mil mililitros: {a}mil vezes um vírgula trezentos e trinta e um dá mil trezentos e trinta e um mililitros. [p=0.2] O que passa de um é o aumento: [p=0.2] o volume aumenta {b}trinta e três vírgula um por cento, [p=0.2] {c}bem mais que os dez por cento de cada medida. [p=0.3] Medidas um pouco maiores, {d}volume bem maior."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}separe em partes conhecidas, [p=0.2] {b}escreva a frase que liga as medidas [p=0.2] e, em sólidos semelhantes, {c}multiplique o volume por cá ao cubo."),
    dict(id="s23", block="fim", text="Com isso, você fecha {a}a geometria espacial. [p=0.2] Na próxima aula, começa {b}a estatística: [p=0.2] quando uma pesquisa ouve todo mundo e quando ouve {c}só uma parte, [p=0.2] os tipos de dado [p=0.2] e como montar {d}uma amostra que respeita cada grupo. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
