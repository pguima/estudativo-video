# Estudativo · MAT-FRA-013 — Praticando: operações com frações (Matemática · Frações e Decimais · prática).
# Habilidade: resolver contas e problemas com as quatro operações entre frações.
# Pré-requisitos: MAT-FRA-007, MAT-FRA-008, MAT-FRA-009, MAT-FRA-010, MAT-FRA-011, MAT-FRA-012. Próxima: MAT-FRA-014.
# Questões inéditas, criadas para esta aula.

TITULO = "Praticando: operações com frações"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações, [p=0.2] criadas para esta aula, [p=0.2] com as quatro operações entre frações. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Antes de qualquer conta, a pergunta é sempre {a}que operação é essa? [p=0.3] Você vai usar {b}somar com MMC, [p=0.2] {c}multiplicar, [p=0.2] {d}fração do restante, [p=0.2] {e}dividir [p=0.2] e {f}ordem das operações. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: somar e quanto falta
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Uma pessoa pintou {b}dois quintos de uma parede de manhã [p=0.1] e {c}um terço da parede à tarde. [p=0.3] {d}Que fração da parede falta pintar?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] Já pintou {a}dois quintos mais um terço. [p=0.2] Denominadores diferentes, então {b}MMC de cinco e três: quinze. [p=0.3] {c}Seis quinze avos mais cinco quinze avos: {d}onze quinze avos. [p=0.3] Com denominadores pequenos assim, a borboleta também serve: {e}dois vezes três mais um vezes cinco, onze; [p=0.2] {f}cinco vezes três, quinze."),
    dict(id="s06", block="resposta1", text="Mas a pergunta é o que {a}falta. [p=0.2] A parede inteira são {b}quinze quinze avos. [p=0.2] Quinze menos onze: {c}faltam quatro quinze avos. [p=0.3] Quem parou em onze quinze avos fez a conta certa e respondeu outra pergunta."),
    # situação 2: multiplicar
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] Uma empresa tem {b}sessenta funcionários. [p=0.2] {c}Cinco sextos fizeram um curso. [p=0.2] {d}Três décimos de quem fez o curso foram promovidos. [p=0.3] {e}Quantos funcionários foram promovidos?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="Vamos lá. [p=0.2] A palavra de vira vezes: {a}três décimos vezes cinco sextos. [p=0.3] Corte em cruz: {b}três e seis, ficam um e dois. [p=0.2] {c}Cinco e dez, ficam um e dois. [p=0.3] Deu {d}um quarto dos funcionários."),
    dict(id="s10", block="resposta2", text="{a}Sessenta dividido por quatro: quinze funcionários. [p=0.3] Confira: cinco sextos de sessenta, {b}cinquenta. [p=0.2] Três décimos de cinquenta, {c}quinze. [p=0.2] Bateu."),
    # situação 3: fração do restante
    dict(id="s11", block="questao3", text="{a}Situação três. [p=0.2] Um caminhão sai com {b}duzentas e quarenta caixas. [p=0.2] Na primeira parada, descarrega {c}três oitavos. [p=0.2] Na segunda, {d}um quinto do restante. [p=0.3] {e}Quantas caixas continuam no caminhão?"),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] Primeira parada: {a}duzentos e quarenta dividido por oito, trinta. [p=0.2] Vezes três, {b}noventa caixas. [p=0.2] Ficam {c}cento e cinquenta. [p=0.3] Segunda parada: um quinto {d}de cento e cinquenta, não de duzentos e quarenta. [p=0.2] {e}Trinta caixas. [p=0.2] Continuam {f}cento e vinte. [p=0.3] Quem calcula um quinto do total acha {g}quarenta e oito, [p=0.2] e fica com {h}cento e duas caixas. [p=0.2] Errado."),
    # atalho
    dict(id="s14", block="atalho", text="Aqui cabe o atalho: {a}multiplique só as sobras. [p=0.3] Saíram três oitavos: {b}sobram cinco oitavos. [p=0.2] Saiu um quinto do restante: {c}sobram quatro quintos. [p=0.3] {d}Quatro quintos de cinco oitavos: [p=0.2] corte o cinco com o cinco, e o quatro com o oito: {e}um meio. [p=0.2] Metade de duzentos e quarenta: {f}cento e vinte."),
    dict(id="s15", block="atalho", text="Funciona porque {a}cada sobra é uma fração da sobra anterior. [p=0.3] Não compensa se a pergunta for {b}quantas caixas saíram em uma parada: [p=0.2] aí, {c}calcule aquela parada."),
    # situação 4: dividir com número misto
    dict(id="s16", block="questao4", text="{a}Situação quatro. [p=0.2] Uma costureira tem {b}sete metros e meio de tecido. [p=0.2] Cada avental usa {c}três quartos de metro. [p=0.3] {d}Quantos aventais ela consegue fazer?"),
    dict(id="s17", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s18", block="resposta4", text="Vamos lá. [p=0.2] Quantas vezes o avental cabe no tecido? [p=0.2] Isso é {a}dividir. [p=0.3] Misto primeiro: sete inteiros e um meio é {b}quinze meios. [p=0.3] {c}Conserva quinze meios, [p=0.1] {d}vira a segunda: quatro terços, [p=0.1] e multiplica."),
    dict(id="s19", block="resposta4", text="Corte em cruz: {a}quinze e três, ficam cinco e um. [p=0.2] {b}Quatro e dois, ficam dois e um. [p=0.3] {c}Cinco vezes dois: dez aventais. [p=0.3] Confira: {d}dez vezes três quartos, trinta quartos, [p=0.2] que simplifica para {e}quinze meios. [p=0.2] Bateu. [p=0.3] Quem vira a fração errada acha {f}um décimo de avental: [p=0.2] impossível com tanto tecido."),
    # situação 5: expressão com negativa
    dict(id="s20", block="questao5", text="{a}Última situação, e ela é conta pura. [p=0.2] Resolva: {b}menos cinco sextos {c}mais um meio dividido por três quartos."),
    dict(id="s21", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s22", block="resposta5", text="Vamos lá, em blocos. [p=0.2] Dividido vem antes do mais, então {a}separe um meio dividido por três quartos. [p=0.3] Conserva, vira, multiplica: {b}um meio vezes quatro terços. [p=0.2] {c}Corte o quatro com o dois. [p=0.2] Fica {d}dois terços."),
    dict(id="s23", block="resposta5", text="Junte: {a}menos cinco sextos mais dois terços. [p=0.2] MMC de seis e três: seis. [p=0.2] {b}Menos cinco sextos mais quatro sextos. [p=0.3] Devia cinco, pagou quatro, ainda deve um: {c}menos um sexto."),
    # fechamento
    dict(id="s24", block="fim", text="Resumindo: antes da conta, descubra {a}a operação. [p=0.2] {b}Falta é subtrair, [p=0.2] {c}a palavra de é vezes, [p=0.2] {d}quantos cabem é dividir."),
    dict(id="s25", block="fim", text="Na próxima aula, as frações dão lugar aos {a}números decimais: [p=0.2] você vai {b}ler três vírgula vinte e cinco, [p=0.2] {c}comparar números com vírgula [p=0.2] e {d}arredondar. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
