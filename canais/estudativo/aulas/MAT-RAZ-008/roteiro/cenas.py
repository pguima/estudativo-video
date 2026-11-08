# Estudativo · MAT-RAZ-008 — Regra de três composta com grandezas diretas (Matemática · Razão e Proporção).
# Habilidade: resolver um caso com máquinas, horas e peças.
# Pré-requisitos: MAT-RAZ-006 (regra de três direta). Próxima: MAT-RAZ-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. O teste do dobro e a regra de três inversa não estão no "Já ensinado": a decisão usa só a definição de direta (MAT-RAZ-004).
# 3 máquinas, 4 h, 120 peças → 5 máquinas, 6 h: 120 ÷ 3 × 5 = 200; 200 ÷ 4 × 6 = 300. Colunas: 120/x = 3/5 · 4/6 = 12/30 = 2/5 → 2x = 600 → x = 300.
# Erro (esquece as horas): 200. Atalho: 3 · 4 = 12; 120 ÷ 12 = 10 por máquina por hora; 5 · 6 = 30; 30 · 10 = 300. Não compensa: 100 ÷ 12 não é exata.
# Questão: 4 costureiras, 6 h, 72 camisetas → 6 costureiras, 5 h: 4 · 6 = 24; 72 ÷ 24 = 3; 6 · 5 = 30; 30 · 3 = 90. Colunas: 72/x = 4/6 · 6/5 = 24/30 = 4/5 → x = 90.

TITULO = "Regra de três composta com grandezas diretas"

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
    dict(id="s01", block="gancho", text="{a}Três máquinas, trabalhando quatro horas, fazem cento e vinte peças. [p=0.3] {b}Cinco máquinas, trabalhando seis horas, fazem quantas? [p=0.3] Muita gente responde {c}duzentas. [p=0.2] Faltou uma grandeza na conta."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você resolve regra de três com três grandezas ou mais, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre de {a}duas coisas: [p=0.2] {b}grandezas diretamente proporcionais, em que dobrar uma dobra a outra, [p=0.2] e {c}a regra de três direta, com a tabela e o produto cruzado. [p=0.3] Se faltar alguma, procure no canal."),
    # uma mudança de cada vez
    dict(id="s04", block="ideia", text="Quando três grandezas mudam juntas, o segredo é {a}mudar uma de cada vez. [p=0.3] Primeiro, só as máquinas. [p=0.2] As horas ficam paradas em quatro."),
    dict(id="s05", block="ideia", text="{a}Três máquinas fazem cento e vinte peças. [p=0.2] Uma máquina faz {b}cento e vinte dividido por três dá quarenta. [p=0.2] Cinco máquinas fazem {c}quarenta vezes cinco, duzentas peças. [p=0.3] Era aqui que a resposta errada parava."),
    dict(id="s06", block="ideia", text="Agora mudam as horas. [p=0.2] {a}Em quatro horas, as cinco máquinas fazem duzentas peças. [p=0.2] Em uma hora, {b}duzentos dividido por quatro dá cinquenta. [p=0.2] Em seis horas, {c}cinquenta vezes seis, trezentas peças."),
    dict(id="s07", block="ideia", text="Resposta: {a}trezentas peças. [p=0.3] Mais máquinas, mais peças. [p=0.2] Mais horas, mais peças. [p=0.2] {b}As duas mudanças empurram o resultado para cima."),
    # método das colunas
    dict(id="s08", block="metodo", text="Na prova, dá para fazer tudo de uma vez com {a}as colunas. [p=0.3] Uma coluna para cada grandeza: [p=0.2] {b}máquinas, três e cinco. [p=0.2] {c}Horas, quatro e seis. [p=0.2] {d}Peças, cento e vinte e xis."),
    dict(id="s09", block="metodo", text="Agora compare {a}cada coluna com a coluna do xis, uma de cada vez, [p=0.2] como se as outras estivessem paradas. [p=0.3] {b}Dobrando as máquinas, dobram as peças: direta. [p=0.2] {c}Dobrando as horas, dobram as peças: direta."),
    dict(id="s10", block="metodo", text="Com tudo direto, a montagem é: [p=0.2] {a}a fração do xis igual à multiplicação das outras frações. [p=0.3] {b}Cento e vinte dividido por xis [p=0.1] igual a {c}três quintos vezes quatro sextos."),
    dict(id="s11", block="metodo", text="{a}Três vezes quatro dá doze. [p=0.2] {b}Cinco vezes seis dá trinta. [p=0.2] Doze trinta avos, simplificando por seis, vira {c}dois quintos. [p=0.3] Produto cruzado: {d}dois vezes xis igual a cento e vinte vezes cinco, seiscentos. [p=0.2] {e}Xis igual a trezentos."),
    dict(id="s12", block="metodo", text="Por que multiplicar as frações? [p=0.2] Volte à conta de uma de cada vez. [p=0.2] {a}Dividir por três e multiplicar por cinco é multiplicar por cinco terços. [p=0.2] Dividir por quatro e multiplicar por seis é multiplicar por seis quartos. [p=0.3] {b}As frações das colunas são essas mesmas mudanças, de cabeça para baixo, [p=0.2] porque em todas o valor antigo fica em cima, como o cento e vinte na fração do xis. [p=0.3] E as mudanças se acumulam, uma em cima da outra: por isso se multiplicam."),
    # erro comum
    dict(id="s13", block="erro", text="O erro comum é o do começo: {a}fazer uma regra de três simples e esquecer uma coluna. [p=0.3] Com só as máquinas, sai {b}duzentas peças. [p=0.2] Mas as máquinas trabalharam {c}seis horas. [p=0.2] Não foram quatro. [p=0.3] Antes de calcular, {d}conte as colunas e confira se todas entraram na conta."),
    # atalho
    dict(id="s14", block="atalho", text="Agora o atalho: [p=0.2] {a}descubra o que uma máquina faz em uma hora. [p=0.3] {b}Três máquinas por quatro horas são doze horas de máquina. [p=0.2] {c}Cento e vinte dividido por doze dá dez peças por hora de máquina."),
    dict(id="s15", block="atalho", text="Na nova situação, {a}cinco máquinas por seis horas são trinta horas de máquina. [p=0.2] {b}Trinta vezes dez, trezentas peças. [p=0.3] Funciona porque, com tudo direto, {c}cada máquina, em cada hora, faz o mesmo tanto de peças."),
    dict(id="s16", block="atalho", text="{a}Não compensa quando a divisão não dá exata. [p=0.2] Com {b}cem peças em doze horas de máquina, [p=0.2] a divisão não fecha, e sobra número quebrado. [p=0.3] Aí, {c}vá pelas colunas."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Quatro costureiras, trabalhando seis horas, fazem setenta e duas camisetas. [p=0.3] {b}Quantas camisetas seis costureiras fazem trabalhando cinco horas, no mesmo ritmo?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Pelo atalho: {a}quatro costureiras por seis horas são vinte e quatro horas de trabalho. [p=0.2] {b}Setenta e dois dividido por vinte e quatro dá três camisetas por hora de costureira."),
    dict(id="s20", block="resposta", text="Agora, {a}seis costureiras por cinco horas, trinta horas de trabalho. [p=0.2] {b}Trinta vezes três: noventa camisetas. [p=0.3] Pelas colunas, {c}setenta e dois dividido por xis igual a quatro sextos vezes seis quintos, [p=0.2] que dá {d}quatro quintos. [p=0.2] O produto cruzado chega nas {e}mesmas noventa."),
    dict(id="s21", block="resposta", text="Repare: {a}as costureiras aumentaram e as horas diminuíram. [p=0.3] Mesmo assim, {b}as duas são diretas. [p=0.2] Direta não quer dizer que tudo sobe. [p=0.2] Quer dizer que {c}cada uma, sozinha, puxa as peças para o mesmo lado que ela vai."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}uma coluna para cada grandeza, [p=0.2] {b}compare cada uma com a do xis [p=0.2] e {c}multiplique as frações."),
    dict(id="s23", block="fim", text="Na próxima aula, entra {a}uma grandeza inversa: [p=0.2] {b}operários, horas por dia e dias para levantar um muro. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
