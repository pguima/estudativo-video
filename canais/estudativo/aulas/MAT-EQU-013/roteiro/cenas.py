# Estudativo · MAT-EQU-013 — Montar uma equação a partir do problema (Matemática · Equações do 1º Grau).
# Habilidade: achar três números consecutivos que somam 84 e descobrir o total quando 1/3 + 1/4 do valor mais R$ 10 completam tudo.
# Pré-requisitos: MAT-EQU-001 (linguagem matemática), MAT-EQU-010 (equação com frações). Próxima: MAT-EQU-014.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Sem distributiva com parênteses (MAT-EQU-004 e 009 ainda não vieram).

TITULO = "Montar uma equação a partir do problema"

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
    dict(id="s01", block="gancho", text="{a}Três números seguidos somam oitenta e quatro. [p=0.3] {b}Quais são eles? [p=0.3] Dá para sair chutando. [p=0.2] Mas existe um jeito que {c}nunca falha."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você transforma um problema de texto em equação, [p=0.2] e ainda leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}escrever uma frase com letra, [p=0.2] como o dobro de um número mais três, [p=0.2] e {c}resolver equação com fração, multiplicando tudo pelo MMC. [p=0.3] Se faltar alguma, procure no canal."),
    # método
    dict(id="s04", block="metodo", text="O jeito que nunca falha tem {a}quatro passos."),
    dict(id="s05", block="metodo", text="{a}Passo um: o que você não sabe vira xis. [p=0.2] {b}Passo dois: escreva cada informação usando o xis. [p=0.2] {c}Passo três: ache o que é igual a quê, e monte a equação. [p=0.2] {d}Passo quatro: resolva, responda o que foi pedido e confira no texto."),
    # consecutivos
    dict(id="s06", block="consecutivos", text="Vamos ao primeiro problema. [p=0.2] Números {a}consecutivos são números seguidos, [p=0.2] um logo depois do outro, [p=0.2] como {b}sete [p=0.2] oito [p=0.2] e nove. [p=0.3] Cada um é {c}uma unidade maior que o anterior."),
    dict(id="s07", block="consecutivos", text="{a}Passo um: o primeiro número vira xis. [p=0.2] {b}Passo dois: o seguinte é uma unidade a mais, {c}xis mais um. [p=0.2] O terceiro é {d}xis mais dois."),
    dict(id="s08", block="consecutivos", text="{a}Passo três: a soma deles é igual a oitenta e quatro. [p=0.2] Fica {b}xis, [p=0.3] mais xis mais um, [p=0.3] mais xis mais dois, [p=0.3] igual a oitenta e quatro."),
    dict(id="s09", block="consecutivos", text="{a}Passo quatro: resolver. [p=0.2] Junte os termos semelhantes: [p=0.2] {b}três xis mais três igual a oitenta e quatro. [p=0.3] Na balança, {c}tire três de cada lado: [p=0.2] {d}três xis igual a oitenta e um. [p=0.2] {e}Divida cada lado por três: [p=0.2] {f}xis igual a vinte e sete."),
    dict(id="s10", block="consecutivos", text="A pergunta pede {a}os três números: [p=0.2] {b}vinte e sete [p=0.1] vinte e oito [p=0.1] e vinte e nove. [p=0.3] Conferindo: {c}somados, dão oitenta e quatro. [p=0.2] {d}Bateu."),
    # frações
    dict(id="s11", block="carteira", text="O segundo problema tem fração. [p=0.2] Uma pessoa saiu de casa com um dinheiro na carteira. [p=0.2] Gastou {a}um terço desse dinheiro no almoço [p=0.2] e {b}um quarto desse mesmo dinheiro na passagem. [p=0.2] Ainda {c}sobraram dez reais. [p=0.3] {d}Com quantos reais ela saiu de casa?"),
    dict(id="s12", block="carteira", text="{a}O dinheiro inicial é o xis. [p=0.2] O almoço é {b}um terço de xis, [p=0.2] que se escreve xis sobre três. [p=0.2] A passagem é {c}xis sobre quatro. [p=0.3] E aqui está a ideia que monta a equação: [p=0.2] {d}almoço, mais passagem, mais o que sobrou, [p=0.2] {e}dá o dinheiro todo."),
    dict(id="s13", block="carteira", text="Fica {a}xis sobre três mais xis sobre quatro mais dez, igual a xis. [p=0.3] O MMC de três e quatro é doze. [p=0.2] {b}Multiplique cada termo por doze, até o dez: [p=0.2] {c}quatro xis mais três xis mais cento e vinte, igual a doze xis."),
    dict(id="s14", block="carteira", text="Junte os xis da esquerda: [p=0.2] {a}sete xis mais cento e vinte igual a doze xis. [p=0.3] {b}Tire sete xis de cada lado: [p=0.2] {c}cento e vinte igual a cinco xis. [p=0.2] {d}Divida por cinco: [p=0.2] {e}xis igual a vinte e quatro."),
    dict(id="s15", block="carteira", text="Ela saiu com {a}vinte e quatro reais. [p=0.3] Confira no texto: [p=0.2] {b}um terço de vinte e quatro dá oito. [p=0.2] {c}Um quarto dá seis. [p=0.2] {d}Oito mais seis mais dez dá vinte e quatro. [p=0.2] Fechou o dinheiro todo."),
    # erro
    dict(id="s16", block="erro", text="Agora, cuidado com um erro muito comum: [p=0.2] {a}achar o xis e parar ali. [p=0.3] No primeiro problema, a pessoa responde {b}só vinte e sete. [p=0.3] Mas vinte e sete sozinho {c}não soma oitenta e quatro. [p=0.2] O xis era {d}só o primeiro número. [p=0.3] Sempre volte à pergunta antes de responder."),
    # atalho
    dict(id="s17", block="atalho", text="Agora o atalho prometido: [p=0.2] {a}em três números seguidos, divida a soma por três [p=0.2] e você acha {b}o do meio. [p=0.3] {c}Oitenta e quatro dividido por três dá vinte e oito. [p=0.2] Um a menos e um a mais: [p=0.2] {d}vinte e sete e vinte e nove."),
    dict(id="s18", block="atalho", text="Funciona porque {a}o de baixo tem um a menos e o de cima tem um a mais. [p=0.2] Um compensa o outro. [p=0.3] {b}Não compensa com quatro números seguidos: [p=0.2] aí não existe um número do meio, [p=0.2] e {c}a equação resolve."),
    # questão
    dict(id="s19", block="questao", text="Hora de testar. [p=0.2] Um pai tem {a}o triplo da idade do filho, [p=0.2] ou seja, três vezes a idade dele. [p=0.2] {b}Somadas, as idades dão quarenta e oito anos. [p=0.3] {c}Qual é a idade do pai?"),
    dict(id="s20", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s21", block="resposta", text="Vamos lá. [p=0.2] {a}A idade do filho é xis. [p=0.2] Triplo é três vezes, então {b}o pai tem três xis. [p=0.2] {c}Xis mais três xis igual a quarenta e oito. [p=0.3] {d}Quatro xis igual a quarenta e oito. [p=0.2] Dividindo por quatro: [p=0.2] {e}xis igual a doze."),
    dict(id="s22", block="resposta", text="Cuidado: doze é {a}a idade do filho. [p=0.2] O pai tem {b}três vezes doze, que dá trinta e seis anos. [p=0.3] Conferindo: {c}doze mais trinta e seis dá quarenta e oito. [p=0.2] {d}Bateu."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo: {a}o desconhecido vira xis, [p=0.2] {b}cada informação vira conta [p=0.2] e {c}a resposta é o que a pergunta pede."),
    dict(id="s24", block="fim", text="Na próxima aula, você usa isso para {a}comparar dois planos de celular [p=0.2] e descobrir {b}com quantos minutos eles custam o mesmo. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
