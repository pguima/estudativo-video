# Estudativo · MAT-RAZ-018 — Vazão e torneiras juntas (Matemática · Razão e Proporção).
# Habilidade: calcular em quanto tempo uma torneira de 12,5 L/min enche uma caixa de 1.500 L e o tempo de duas torneiras ligadas.
# Pré-requisitos: MAT-FRA-008 (denominadores diferentes), MAT-MED-005 (volume e litros), MAT-RAZ-015 (taxas e velocidade média). Próxima: MAT-RAZ-025.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Vazão e torneiras juntas"

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
    dict(id="s01", block="gancho", text="Uma torneira enche a caixa-d'água em {a}três horas. [p=0.2] Outra enche a mesma caixa em {b}seis horas. [p=0.3] Ligando as duas juntas, quanto tempo leva? [p=0.3] Se você pensou em {c}quatro horas e meia, [p=0.2] tem um problema."),
    dict(id="s02", block="gancho", text="Com ajuda, a caixa enche {a}mais rápido do que com a torneira rápida sozinha. [p=0.2] Tem que ser menos de três horas. [p=0.3] {b}Até o fim desta aula, você vai acertar esse tempo, [p=0.2] e ainda leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}ler uma taxa, como quilômetro por hora, [p=0.2] {c}saber que um metro cúbico guarda mil litros [p=0.2] e {d}somar frações com denominadores diferentes. [p=0.3] Se faltar alguma, procure no canal."),
    # vazão
    dict(id="s04", block="vazao", text="{a}Vazão é quanto líquido passa por um cano ou torneira {b}a cada unidade de tempo. [p=0.3] Uma torneira de {c}doze vírgula cinco litros por minuto solta doze litros e meio a cada minuto."),
    dict(id="s05", block="vazao", text="É uma taxa, igual à velocidade. [p=0.2] Velocidade é distância dividida pelo tempo. [p=0.2] Vazão é {a}volume dividido pelo tempo. [p=0.3] A palavra {b}por, no meio da unidade, é o sinal da divisão."),
    dict(id="s06", block="vazao", text="Só que a pergunta da prova costuma ser o tempo. [p=0.2] Então isole o tempo, como você faz com a velocidade: [p=0.2] {a}tempo é volume dividido pela vazão."),
    # exemplo
    dict(id="s07", block="exemplo", text="Uma caixa de {a}mil e quinhentos litros, e a torneira de doze vírgula cinco litros por minuto. [p=0.3] {b}Mil e quinhentos dividido por doze vírgula cinco. [p=0.3] Tire a vírgula do divisor, multiplicando cada número por dez. [p=0.2] Fica {c}quinze mil dividido por cento e vinte e cinco."),
    dict(id="s08", block="exemplo", text="Cento e vinte e cinco cabe oito vezes em mil. [p=0.2] Quinze mil são quinze vezes mil, então cabe {a}quinze vezes oito dá cento e vinte vezes. [p=0.3] {b}Cento e vinte minutos. [p=0.2] Divida por sessenta: {c}duas horas para encher a caixa."),
    # duas vazões
    dict(id="s09", block="juntas", text="E com duas torneiras? [p=0.2] Se você sabe a vazão de cada uma, {a}é só somar. [p=0.3] Uma solta {b}trinta litros por minuto. [p=0.2] A outra, {c}vinte. [p=0.2] Juntas, {d}cinquenta litros por minuto."),
    dict(id="s10", block="juntas", text="Na mesma caixa de mil e quinhentos litros: [p=0.2] {a}mil e quinhentos dividido por cinquenta dá {b}trinta minutos. [p=0.3] A mais rápida, sozinha, levaria cinquenta. [p=0.2] Juntas, {c}menos. Faz sentido."),
    # só os tempos
    dict(id="s11", block="tempos", text="Agora o caso do começo: você só conhece {a}os tempos, três horas e seis horas. [p=0.3] Pense no que cada uma faz {b}em uma hora."),
    dict(id="s12", block="tempos", text="A que enche em três horas faz {a}um terço da caixa por hora. [p=0.2] A que enche em seis horas faz {b}um sexto por hora. [p=0.3] Juntas, em uma hora: {c}um terço mais um sexto."),
    dict(id="s13", block="tempos", text="MMC de três e seis: seis. [p=0.2] Um terço vira {a}dois sextos. [p=0.2] Dois sextos mais um sexto, {b}três sextos, [p=0.2] que é {c}um meio. [p=0.3] Metade da caixa por hora. [p=0.2] Então a caixa inteira leva {d}duas horas."),
    # erro comum
    dict(id="s14", block="erro", text="Cuidado com um erro de unidade. [p=0.2] Imagine a caixa medida em metros cúbicos: {a}um vírgula cinco metro cúbico. [p=0.2] A torneira continua em litros por minuto."),
    dict(id="s15", block="erro", text="Quem divide direto, {a}um vírgula cinco por doze vírgula cinco, [p=0.2] acha {b}zero vírgula doze minuto. [p=0.2] Nem dez segundos para encher uma caixa-d'água! [p=0.3] Antes de dividir, ponha tudo na mesma unidade: [p=0.2] {c}um vírgula cinco metro cúbico são mil e quinhentos litros. [p=0.2] Aí sim, {d}cento e vinte minutos."),
    # atalho
    dict(id="s16", block="atalho", text="Agora o atalho prometido, para duas torneiras com os tempos dados: [p=0.2] {a}produto sobre soma. [p=0.3] {b}Três vezes seis dá dezoito. [p=0.2] {c}Três mais seis dá nove. [p=0.2] {d}Dezoito dividido por nove dá duas horas."),
    dict(id="s17", block="atalho", text="Funciona porque é a {a}borboleta das frações. [p=0.2] Em um terço mais um sexto, os números de cima são um. [p=0.2] Então, em cima, a borboleta dá {b}seis mais três, a soma dos tempos. [p=0.2] Embaixo, dá três vezes seis, o produto. [p=0.3] São nove dezoito avos da caixa por hora. [p=0.2] A caixa inteira são dezoito dezoito avos: [p=0.2] {c}dezoito dividido por nove dá duas horas. [p=0.3] O produto dividido pela soma."),
    dict(id="s18", block="atalho", text="Não compensa com {a}três torneiras: aí, some as frações. [p=0.2] E se as vazões forem dadas, {b}some as vazões, que é mais rápido. [p=0.3] Também não confunda com o atalho da ida e volta, da aula de velocidade média em dois trechos. [p=0.2] {c}Lá tem o dobro na frente, porque a viagem tem dois trechos. [p=0.2] Aqui, a caixa é uma só: {d}sem dobro."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Uma torneira enche um tanque em {a}quatro horas. [p=0.2] Outra enche o mesmo tanque em {b}doze horas. [p=0.3] {c}Ligadas juntas, em quanto tempo elas enchem o tanque?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] Em uma hora: {a}um quarto mais um doze avos. [p=0.2] Um quarto vira {b}três doze avos. [p=0.2] Somando, {c}quatro doze avos, que é {d}um terço do tanque por hora. [p=0.3] {e}Três horas. [p=0.3] Pelo atalho: {f}quarenta e oito dividido por dezesseis dá três. [p=0.2] E três é menos que quatro: {g}faz sentido."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}tempo é volume dividido pela vazão, [p=0.2] {b}vazões juntas se somam, [p=0.2] e {c}juntas é sempre mais rápido que a mais rápida sozinha."),
    dict(id="s23", block="fim", text="Na próxima aula, uma torneira pingando, {a}gota a gota. [p=0.2] Quantos litros ela joga fora em um mês? [p=0.2] Você resolve {b}só encaixando as unidades. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
