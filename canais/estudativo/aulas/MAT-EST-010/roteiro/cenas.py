# Estudativo · MAT-EST-010 — Média geométrica e harmônica (Matemática · Estatística · Médias).
# Habilidade: calcular a média geométrica de 4 e 9 (6) e usar a harmônica em velocidades: 40 e 60 km/h dão 48 km/h.
# Pré-requisitos: MAT-EST-008 (média aritmética), MAT-POT-016 (raiz cúbica), MAT-RAZ-024 (velocidade média em dois trechos; atalho "dobro do produto dividido pela soma"). Próxima: MAT-EST-011.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Listas de números só na tela (vírgula entre números funde a leitura da voz).
# Contas: (4 + 9)/2 = 6,5; 6,5 + 6,5 = 13; 4 × 9 = 36; √36 = 6. 2 × 4 × 8 = 64; ∛64 = 4.
#   Bactérias: ×2 e ×8 → ×16; aritmética 5 (5 × 5 = 25); geométrica √16 = 4 (4 × 4 = 16).
#   Velocidade: 1 km a 60 km/h = 1 min; a 40 km/h = 1,5 min; média 1,25 min = 1 min 15 s; 60/1,25 = 48.
#   Harmônica: 1/40 + 1/60 = 5/120 = 1/24; 2 ÷ (1/24) = 48. Atalho: 2 × 40 × 60 = 4 800; 4 800/100 = 48.
#   Ordem: H = 48 < G = √2 400 ≈ 48,99 < A = 50.
#   Questão: 3 × 12 = 36, √36 = 6. Ladeira: 2 × 12 × 24 = 576; 12 + 24 = 36; 576/36 = 16 < 18 (aritmética).
# Visual:
#   s01: "4 e 9" com três resultados: 6,5 · 6 · e um velocímetro 40/60 → 48.
#   s04-s05: duas barras 4 e 9 viram duas barras iguais de 6,5 (soma 13); "4 × 9 = 36" vira "6 × 6 = 36" e "√36 = 6".
#   s06: 2 · 4 · 8 na tela; ∛64 = 4; fórmula geral (raiz de índice n do produto).
#   s07-s08: frasco de bactérias ×2, ×8 = ×16; ×5 ×5 = 25 em vermelho; ×4 ×4 = 16 em verde.
#   s09-s11: estrada de ida e volta; relógio "1 min/km" e "1,5 min/km"; fórmula H = n ÷ (1/x₁ + 1/x₂ + ...).
#   s14: régua (E.reta) com H < G < A para 40 e 60.

TITULO = "Média geométrica e harmônica"

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
    dict(id="s01", block="gancho", text="{a}Quatro e nove. [p=0.2] A média que você conhece dá {b}seis vírgula cinco. [p=0.3] Mas existe outra média desses mesmos números que dá {c}seis, redondo. [p=0.3] E uma terceira explica por que {d}quarenta e sessenta quilômetros por hora dão quarenta e oito."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você sabe qual média usar em cada situação [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}três coisas: [p=0.2] {b}a média aritmética, que é a soma dividida pela quantidade; [p=0.2] {c}a raiz quadrada e a raiz cúbica; [p=0.2] e {d}a velocidade média, que é a distância total dividida pelo tempo total. [p=0.3] Se faltar alguma, procure no canal."),
    # a ideia de toda média
    dict(id="s04", block="ideia", text="Toda média faz a mesma coisa: [p=0.2] {a}troca vários números por um só, repetido. [p=0.3] E guarda alguma coisa dos números originais. [p=0.2] A aritmética guarda {b}a soma. [p=0.2] Quatro mais nove dá treze, [p=0.2] e {c}seis vírgula cinco mais seis vírgula cinco também dá treze."),
    # geométrica
    dict(id="s05", block="geometrica", text="A {a}média geométrica guarda o produto. [p=0.2] {b}Quatro vezes nove dá trinta e seis. [p=0.3] Que número, vezes ele mesmo, dá trinta e seis? [p=0.2] {c}Seis. [p=0.3] Ou seja: [p=0.2] {d}a média geométrica de dois números é a raiz quadrada do produto deles."),
    dict(id="s06", block="geometrica", text="Com três números, entra a raiz cúbica. [p=0.2] Veja {a}os três números na tela. [p=0.2] {b}O produto deles dá sessenta e quatro. [p=0.2] {c}A raiz cúbica de sessenta e quatro dá quatro, [p=0.2] porque quatro vezes quatro vezes quatro dá sessenta e quatro. [p=0.3] {d}A regra: multiplique todos e tire a raiz com o índice igual à quantidade de números."),
    dict(id="s07", block="crescimento", text="E onde ela aparece? [p=0.2] Quando os números {a}multiplicam. [p=0.2] Uma cultura de bactérias {b}dobrou no primeiro dia [p=0.2] e {c}ficou oito vezes maior no segundo. [p=0.3] No fim, {d}ficou dezesseis vezes maior."),
    dict(id="s08", block="crescimento", text="Qual foi o crescimento médio por dia? [p=0.2] Pela aritmética, {a}dois mais oito dá dez, que dividido por dois dá cinco. [p=0.2] Mas {b}cinco vezes cinco dá vinte e cinco, não dezesseis. [p=0.3] Pela geométrica, {c}a raiz quadrada de dezesseis dá quatro. [p=0.2] {d}Quatro vezes quatro dá dezesseis. [p=0.2] Essa é a média que guarda o efeito total."),
    # harmônica
    dict(id="s09", block="harmonica", text="A {a}média harmônica é a das velocidades em trechos de mesma distância. [p=0.2] Um carro vai a {b}quarenta quilômetros por hora [p=0.2] e volta pelo mesmo caminho a {c}sessenta. [p=0.3] Você já viu que a média da viagem {d}dá quarenta e oito, não cinquenta. [p=0.3] Se fosse o mesmo tempo em cada velocidade, aí sim valeria a aritmética."),
    dict(id="s10", block="harmonica", text="Pense em {a}minutos por quilômetro. [p=0.2] A sessenta por hora, {b}cada quilômetro leva um minuto. [p=0.2] A quarenta, {c}leva um minuto e meio. [p=0.3] A média dá {d}um minuto e quinze segundos por quilômetro. [p=0.2] Em decimal, isso dá um vírgula vinte e cinco minutos. [p=0.3] Uma hora tem sessenta minutos, [p=0.2] e {e}sessenta dividido por um vírgula vinte e cinco dá quarenta e oito quilômetros."),
    dict(id="s11", block="harmonica", text="Esse é o segredo da harmônica: [p=0.2] ela {a}faz a média dos inversos e depois inverte de volta. [p=0.2] O inverso de quarenta é {b}um quarenta avos: a fração virada de cabeça para baixo. [p=0.3] A média dos inversos é a soma deles dividida pela quantidade. [p=0.2] Virando de cabeça para baixo, fica a fórmula: {c}a quantidade de números, dividida pela soma dos inversos. [p=0.3] {d}Um quarenta avos mais um sessenta avos dá um vinte e quatro avos. [p=0.2] {e}Dois dividido por um vinte e quatro avos dá quarenta e oito."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é usar {a}a média aritmética para tudo. [p=0.2] Nas velocidades, ela dá {b}cinquenta, [p=0.2] e o carro não fez isso. [p=0.3] Ele passou {c}mais tempo no trecho lento, [p=0.2] então a média fica {d}mais perto do quarenta."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, que você já usou nas velocidades: [p=0.2] com {a}dois valores e a mesma distância, [p=0.2] {b}o dobro do produto, dividido pela soma. [p=0.3] {c}Duas vezes quarenta vezes sessenta dá quatro mil e oitocentos. [p=0.2] Quarenta mais sessenta dá cem. [p=0.2] {d}Quatro mil e oitocentos dividido por cem dá quarenta e oito."),
    dict(id="s14", block="atalho", text="Funciona porque é {a}a fórmula da harmônica já simplificada para dois números. [p=0.2] {b}Com três números ou mais, não vale: [p=0.2] aí, use a soma dos inversos. [p=0.3] E uma conferência rápida: [p=0.2] com números diferentes, {c}a harmônica é a menor, a geométrica fica no meio e a aritmética é a maior."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Item um: qual é a média geométrica de três e doze? [p=0.3] {b}Item dois: um ciclista sobe uma ladeira a doze quilômetros por hora [p=0.2] e desce pelo mesmo caminho a vinte e quatro. [p=0.2] {c}Qual é a velocidade média da subida e da descida?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Três vezes doze dá trinta e seis. [p=0.2] {b}A raiz quadrada de trinta e seis dá seis. [p=0.3] Na ladeira, a distância é a mesma na subida e na descida: {c}é a harmônica. [p=0.2] {d}Duas vezes doze vezes vinte e quatro dá quinhentos e setenta e seis. [p=0.2] {e}Doze mais vinte e quatro dá trinta e seis. [p=0.2] {f}Quinhentos e setenta e seis dividido por trinta e seis dá dezesseis quilômetros por hora."),
    dict(id="s18", block="resposta", text="Confira: [p=0.2] {a}dezesseis é menor que dezoito, a média aritmética. [p=0.2] Faz sentido, porque {b}a subida demora mais."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}a aritmética guarda a soma, [p=0.2] {b}a geométrica guarda o produto [p=0.2] e {c}a harmônica acerta a média das velocidades em distâncias iguais."),
    dict(id="s20", block="fim", text="Na próxima aula, duas medidas quase sem conta: [p=0.2] {a}a mediana, o valor do meio da lista em ordem, [p=0.2] e {b}a moda, o valor que mais aparece. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
