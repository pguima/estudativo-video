# Estudativo · MAT-ESP-018 — Volume pelo nível da água (Matemática · Geometria Espacial · Sólidos compostos e razão entre volumes).
# Habilidade: descobrir o volume de uma pedra pelo quanto a água subiu num aquário e prever se o líquido transborda.
# Pré-requisitos: MAT-ESP-009 (nível sobe = volume ÷ área do fundo; camada = prisma; paredes retas), MAT-ESP-017 (somar e subtrair volumes). Usa MAT-ESP-014 (esfera; com π = 3, V = 4r³), MAT-ESP-008 (cilindro), MAT-MED-005 (1 cm³ = 1 mL; 1.000 cm³ = 1 L), MAT-FRA-017 (divisão com resultado decimal). Próxima: MAT-ESP-019.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula.
# Contas: aquário 40 × 25 = 1.000 cm²; sobe 22 − 20 = 2 → 2.000 cm³ = 2 L. Erro: 1.000 · 22 = 22.000 (22 L).
#   Copo r = 4, π = 3: fundo 3·16 = 48 cm²; bolinha r = 3: 4·27 = 108 cm³; 108/48 = 2,25; 12 + 2,25 = 14,25 < 15.
#   Atalho: vazio 48·(15 − 12) = 144 cm³; 108 < 144 cabe; 2·108 = 216 > 144 transborda.
#   Questão: fundo 50 × 30 = 1.500 cm²; sobe 27 − 25 = 2 → 3.000 cm³; ÷ 3 = 1.000 cm³ = 1 L por pedra.
#   Vazio 1.500·(30 − 27) = 4.500 cm³; 4 pedras = 4.000 ≤ 4.500; 5 pedras = 5.000 > 4.500 → mais 4 pedras.
# Visual:
#   s01, s04-s06: aquário (E.paralelepipedo transparente) com água; pedra afunda e a camada que subiu (2 cm) ganha cor, com o fundo 40 × 25.
#   s07-s08: copo (E.cilindro) com água até 12 de 15; E.esfera de raio 3 cai dentro; nível vai a 14,25.
#   s09: a altura 22 inteira riscada em vermelho; só a faixa de 2 cm em verde. s10-s11: palco escuro: espaço vazio (144) contra bolinha (108) e duas bolinhas (216).

TITULO = "Volume pelo nível da água"

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
    dict(id="s01", block="gancho", text="{a}Uma pedra toda torta. [p=0.2] Não é cubo, não é cilindro, não é esfera: [p=0.2] {b}nenhuma fórmula serve. [p=0.3] Mas mergulhe a pedra num aquário [p=0.2] e {c}a água sobe. [p=0.2] Essa subida conta o volume da pedra."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você mede o volume de qualquer objeto com água [p=0.2] e prevê se o líquido transborda, [p=0.2] com um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}o volume do prisma e do cilindro é a área da base vezes a altura; [p=0.2] {c}o quanto o nível sobe é o volume dividido pela área do fundo; [p=0.2] e {d}um centímetro cúbico é um mililitro, e mil deles fazem um litro. [p=0.3] Se faltar alguma, procure no canal."),
    # a ideia
    dict(id="s04", block="ideia", text="Por que a água sobe? [p=0.2] {a}A pedra e a água não cabem no mesmo lugar. [p=0.2] A pedra afundada {b}empurra a água para cima, [p=0.2] e a água empurrada tem {c}exatamente o volume da pedra."),
    dict(id="s05", block="ideia", text="A água que subiu forma {a}uma camada com a forma do fundo: um prisma. [p=0.3] Então, {b}volume da pedra igual à área do fundo vezes o quanto a água subiu. [p=0.3] Só um cuidado: {c}o objeto precisa ficar inteiro dentro da água. [p=0.2] Se ele boia, só a parte de baixo empurra água."),
    dict(id="s06", block="pedra", text="Um aquário tem {a}fundo de quarenta por vinte e cinco centímetros. [p=0.2] {b}Quarenta vezes vinte e cinco dá mil centímetros quadrados. [p=0.3] Com a pedra, a água vai {c}de vinte para vinte e dois centímetros: [p=0.2] {d}subiu dois. [p=0.2] {e}Mil vezes dois dá dois mil centímetros cúbicos. [p=0.2] A pedra tem {f}dois litros."),
    # transbordar
    dict(id="s07", block="copo", text="Agora a outra pergunta: {a}vai transbordar? [p=0.2] Um copo em forma de cilindro tem {b}quatro centímetros de raio e quinze de altura, [p=0.2] com {c}água até doze centímetros. [p=0.2] Você põe dentro {d}uma bolinha maciça de três centímetros de raio. [p=0.2] {e}Use pi igual a três."),
    dict(id="s08", block="copo", text="{a}Fundo do copo: quatro ao quadrado dá dezesseis, [p=0.2] e três vezes dezesseis dá quarenta e oito centímetros quadrados. [p=0.2] {b}Bolinha, com pi igual a três: quatro érre ao cubo. [p=0.2] Três ao cubo dá vinte e sete, [p=0.2] e quatro vezes vinte e sete dá cento e oito centímetros cúbicos. [p=0.3] {c}Cento e oito dividido por quarenta e oito dá dois vírgula vinte e cinco. [p=0.2] A água sobe {d}dois vírgula vinte e cinco centímetros [p=0.2] e chega a {e}catorze vírgula vinte e cinco. [p=0.2] {f}Fica abaixo dos quinze: não transborda."),
    # erro comum
    dict(id="s09", block="erro", text="O erro mais comum é {a}usar a altura final da água no lugar da subida. [p=0.2] No aquário, a pessoa faz {b}mil vezes vinte e dois, [p=0.2] e acha que a pedra tem {c}vinte e dois litros. [p=0.3] Mas esse é o volume da água junto com a pedra. [p=0.2] {d}Só a subida é a pedra: [p=0.2] {e}altura final menos altura inicial."),
    # atalho
    dict(id="s10", block="atalho", text="Agora o atalho, para saber se transborda: {a}compare volumes, sem dividir nada. [p=0.3] {b}O espaço vazio em cima da água é um cilindro de três centímetros de altura: [p=0.2] {c}quarenta e oito vezes três dá cento e quarenta e quatro. [p=0.2] {d}A bolinha tem cento e oito: cabe. [p=0.3] {e}Duas bolinhas teriam duzentos e dezesseis: [p=0.2] passa de cento e quarenta e quatro, e {f}transborda."),
    dict(id="s11", block="atalho", text="Funciona porque {a}o espaço vazio é o volume que ainda cabe no copo. [p=0.2] Se o objeto cabe nele, {b}a água não passa da borda. [p=0.3] {c}Não compensa quando a prova pede a altura nova da água: [p=0.2] aí, {d}divida pela área do fundo do mesmo jeito."),
    # questão
    dict(id="s12", block="questao", text="Hora de testar. [p=0.2] Um aquário tem {a}fundo de cinquenta por trinta centímetros [p=0.2] e {b}trinta de altura. [p=0.2] A água está {c}a vinte e cinco centímetros. [p=0.2] Você afunda {d}três pedras iguais, e a água sobe para vinte e sete. [p=0.3] {e}Qual o volume de cada pedra? [p=0.2] {f}E quantas pedras iguais ainda cabem sem transbordar?"),
    dict(id="s13", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s14", block="resposta", text="Vamos lá. [p=0.2] {a}Fundo: cinquenta vezes trinta dá mil e quinhentos centímetros quadrados. [p=0.2] {b}Subida: vinte e sete menos vinte e cinco dá dois. [p=0.2] {c}Mil e quinhentos vezes dois dá três mil centímetros cúbicos, [p=0.2] e isso são as três pedras. [p=0.2] {d}Três mil dividido por três dá mil: [p=0.2] {e}cada pedra tem um litro."),
    dict(id="s15", block="resposta", text="Para a segunda pergunta, use o atalho. [p=0.2] {a}Faltam três centímetros até a borda. [p=0.2] {b}Mil e quinhentos vezes três dá quatro mil e quinhentos centímetros cúbicos de espaço vazio. [p=0.3] {c}Quatro pedras somam quatro mil: cabem. [p=0.2] {d}Cinco somariam cinco mil: transborda. [p=0.3] Resposta: {e}mais quatro pedras."),
    # fechamento
    dict(id="s16", block="fim", text="Resumindo: {a}o volume do objeto é a área do fundo vezes a subida da água, [p=0.2] e {b}para saber se transborda, compare o objeto com o espaço vazio."),
    dict(id="s17", block="fim", text="Na próxima aula, você põe um sólido dentro de outro: [p=0.2] {a}uma esfera dentro de um cubo de aresta seis tem raio três, [p=0.2] e {b}um cone cabe dentro de um cilindro. [p=0.2] Você liga as medidas e acha {c}o volume que sobra. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
