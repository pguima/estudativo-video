# Estudativo · MAT-RAZ-017 — Densidade (Matemática · Razão e Proporção).
# Habilidade: calcular a densidade de um objeto e dizer se ele boia na água.
# Pré-requisitos: MAT-MED-005 (volume e litros), MAT-RAZ-015 (taxas). Próxima: MAT-RAZ-018.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso. Letras ditas uma vez (dê, eme, vê) e depois chamadas pelo nome.

TITULO = "Densidade"

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
    dict(id="s01", block="gancho", text="{a}Um tronco de trezentos quilos boia no rio. [p=0.3] {b}Um clipe de papel, que quase não pesa nada, afunda. [p=0.3] Então não é o peso que decide. [p=0.2] {c}É a densidade."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula a densidade de um objeto e diz se ele boia na água, [p=0.2] e ainda leva um {b}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}ler uma taxa, em que a palavra por quer dizer dividido, [p=0.2] e {c}o volume. [p=0.2] Um centímetro cúbico é um cubinho com um centímetro de lado, [p=0.2] e {d}um litro cabe em mil desses cubinhos. [p=0.3] Se faltar alguma, procure no canal."),
    # a ideia
    dict(id="s04", block="ideia", text="Densidade responde: {a}quanta massa cabe em cada pedacinho de volume. [p=0.3] {b}Massa é o que a balança marca, em gramas ou quilos. [p=0.2] {c}Volume é o espaço que o objeto ocupa."),
    dict(id="s05", block="formula", text="A fórmula: {a}densidade igual a massa dividida pelo volume. [p=0.3] Na tela, {b}cada letra é a primeira letra de uma palavra: dê, eme e vê. [p=0.3] Com massa em gramas e volume em centímetros cúbicos, [p=0.2] a unidade é {c}grama por centímetro cúbico."),
    # exemplos
    dict(id="s06", block="exemplos", text="Um bloco de madeira tem {a}seiscentos gramas [p=0.2] e ocupa {b}mil centímetros cúbicos. [p=0.3] {c}Seiscentos dividido por mil: zero vírgula seis grama por centímetro cúbico."),
    dict(id="s07", block="exemplos", text="Uma pedra tem {a}cento e cinquenta gramas [p=0.2] e ocupa {b}sessenta centímetros cúbicos. [p=0.3] {c}Cento e cinquenta dividido por sessenta: dois vírgula cinco gramas por centímetro cúbico. [p=0.3] E dá para isolar a massa, como na velocidade: [p=0.2] {d}massa igual a densidade vezes volume. [p=0.2] Duzentos centímetros cúbicos dessa pedra: {e}dois vírgula cinco vezes duzentos dá quinhentos gramas."),
    # a água
    dict(id="s08", block="agua", text="E a água? [p=0.2] {a}Um litro de água tem um quilo, ou seja, mil gramas, [p=0.2] em {b}mil centímetros cúbicos. [p=0.3] Densidade da água: {c}um grama por centímetro cúbico."),
    dict(id="s09", block="boia", text="A regra é simples. [p=0.2] {a}Densidade menor que a da água: boia. [p=0.2] {b}Maior: afunda. [p=0.3] A madeira, com zero vírgula seis, {c}boia. [p=0.2] A pedra, com dois vírgula cinco, {d}afunda."),
    # do material
    dict(id="s10", block="material", text="E tem mais: {a}a densidade é do material, não do tamanho. [p=0.3] Pegue um bloco de madeira com o dobro do tamanho: [p=0.2] {b}mil e duzentos gramas em dois mil centímetros cúbicos. [p=0.3] {c}Zero vírgula seis de novo. [p=0.2] Pedaço grande ou pequeno, essa madeira boia."),
    # erro
    dict(id="s11", block="erro", text="O erro comum é achar que {a}o mais pesado afunda. [p=0.3] O tronco de trezentos quilos ocupa uns {b}quinhentos litros. [p=0.3] {c}Trezentos dividido por quinhentos: zero vírgula seis quilo por litro. [p=0.3] Como um litro de água tem um quilo, a água tem {d}um quilo por litro. [p=0.2] O tronco boia, mesmo pesado."),
    dict(id="s12", block="erro", text="O clipe é leve, mas é de aço, [p=0.2] {a}bem mais denso que a água. [p=0.2] Por isso afunda. [p=0.3] {b}Não compare pesos: compare densidades."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho, com {a}massa em gramas e volume em centímetros cúbicos: [p=0.2] {b}compare os números. [p=0.3] {c}Massa menor que o volume: boia. [p=0.2] {d}Massa maior: afunda. [p=0.3] Seiscentos gramas em mil centímetros cúbicos: {e}seiscentos é menor, boia. [p=0.3] Vale também com {f}quilos e litros."),
    dict(id="s14", block="atalho", text="Funciona porque a água tem {a}densidade um. [p=0.2] A massa dividida pelo volume só passa de um quando {b}a massa passa o volume. [p=0.3] {c}Não vale em outro líquido, como o óleo: [p=0.2] aí, compare com a densidade desse líquido. [p=0.2] Nem com unidades misturadas, como quilos e centímetros cúbicos: [p=0.2] {d}converta antes para gramas e centímetros cúbicos, ou para quilos e litros."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Uma bola tem quatrocentos e cinquenta gramas [p=0.1] e ocupa quinhentos centímetros cúbicos. [p=0.3] {b}Uma peça de metal tem duzentos e setenta gramas [p=0.1] e ocupa cem centímetros cúbicos. [p=0.3] {c}Qual é a densidade de cada uma? [p=0.2] {d}Quem boia na água?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}A bola: quatrocentos e cinquenta dividido por quinhentos dá [p=0.2] zero vírgula nove grama por centímetro cúbico. [p=0.3] {b}Menor que um: boia. [p=0.3] Pelo atalho, {c}quatrocentos e cinquenta é menor que quinhentos. [p=0.2] Mesma resposta."),
    dict(id="s18", block="resposta", text="{a}A peça de metal: duzentos e setenta dividido por cem dá [p=0.2] dois vírgula sete gramas por centímetro cúbico. [p=0.3] {b}Maior que um: afunda. [p=0.3] Só a bola boia."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}densidade é massa dividida por volume, [p=0.2] {b}é do material, não do tamanho, [p=0.2] e {c}quem tem densidade menor que a da água boia."),
    dict(id="s20", block="fim", text="Na próxima aula, a taxa é a {a}vazão: [p=0.2] quantos litros por minuto saem de uma torneira, [p=0.2] {b}quanto tempo ela leva para encher uma caixa d'água [p=0.2] e {c}o que muda com duas torneiras ligadas juntas. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
