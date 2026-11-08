# Estudativo · MAT-EQU-017 — Praticando: problemas e inequações (Matemática · Equações do 1º Grau · prática).
# Habilidade: transformar problemas de texto em equações e inequações e responder com a unidade certa.
# Pré-requisitos: MAT-EQU-013, MAT-EQU-014, MAT-EQU-015, MAT-EQU-016. Próxima: MAT-EQU-018.
# Questões inéditas, criadas para esta aula, com valores inventados. Sistemas ainda não foram ensinados (MAT-EQU-018).

TITULO = "Praticando: problemas e inequações"

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
    dict(id="s01", block="gancho", text="{a}Quatro situações, [p=0.2] criadas para esta aula, com valores inventados. [p=0.3] Em cada uma, {b}pause o vídeo e resolva antes de ver a resposta. [p=0.3] E no fim, {c}responda com a unidade: páginas, meses, horas."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}montar a equação do problema, [p=0.2] {b}achar o empate entre dois planos, [p=0.2] {c}virar o sinal ao multiplicar ou dividir por negativo [p=0.2] e {d}resolver inequação dupla. [p=0.3] Se alguma travar, procure a aula no canal."),
    # situação 1: equação com frações
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Uma pessoa leu {b}metade de um livro no primeiro mês [p=0.2] e {c}um quinto do livro inteiro no segundo. [p=0.2] Ainda {d}faltam sessenta páginas. [p=0.3] {e}Quantas páginas tem o livro?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}O livro inteiro é xis. [p=0.2] O que leu mais o que falta {b}dá o livro todo: [p=0.2] {c}xis sobre dois mais xis sobre cinco mais sessenta, igual a xis. [p=0.3] O MMC de dois e cinco é dez. [p=0.2] {d}Multiplique cada termo por dez, até o sessenta: [p=0.2] {e}cinco xis mais dois xis mais seiscentos, igual a dez xis."),
    dict(id="s06", block="resposta1", text="{a}Sete xis mais seiscentos igual a dez xis. [p=0.2] {b}Tire sete xis de cada lado: [p=0.2] {c}seiscentos igual a três xis. [p=0.2] {d}Xis igual a duzentos. [p=0.3] {e}O livro tem duzentas páginas. [p=0.2] Conferindo: [p=0.2] {f}metade de duzentos é cem. [p=0.2] {g}Um quinto de duzentos é quarenta. [p=0.2] {h}Cem mais quarenta mais sessenta dá duzentos."),
    # atalho
    dict(id="s07", block="atalho", text="Aqui cabe um atalho: {a}ache a fração que falta. [p=0.3] Em décimos, metade é cinco décimos [p=0.2] e um quinto é dois décimos. [p=0.2] Leu {b}sete décimos. [p=0.2] Faltam {c}três décimos, e eles são sessenta páginas. [p=0.2] {d}Um décimo é vinte. [p=0.2] {e}O livro todo, duzentas."),
    dict(id="s08", block="atalho", text="Funciona porque {a}o que falta também é uma fração do total. [p=0.3] {b}Não compensa quando a segunda fração é do que sobrou, [p=0.2] e não do livro inteiro: [p=0.2] aí, {c}monte a equação com calma."),
    # situação 2: empate
    dict(id="s09", block="questao2", text="{a}Situação dois. [p=0.2] A academia A cobra {b}noventa reais de matrícula, [p=0.2] mais sessenta reais por mês. [p=0.3] A academia B {c}não cobra matrícula, [p=0.2] mas cobra setenta e cinco reais por mês. [p=0.3] {d}Em quantos meses o gasto total fica igual? [p=0.2] E {e}depois disso, qual sai mais barata?"),
    dict(id="s10", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s11", block="resposta2", text="Vamos lá. [p=0.2] {a}Os meses viram xis. [p=0.2] {b}Noventa mais sessenta xis, igual a setenta e cinco xis. [p=0.3] {c}Tire sessenta xis de cada lado: [p=0.2] {d}noventa igual a quinze xis. [p=0.2] {e}Xis igual a seis. [p=0.3] {f}Em seis meses, as academias empatam, [p=0.2] com {g}quatrocentos e cinquenta reais cada."),
    dict(id="s12", block="resposta2", text="Depois disso, ganha {a}a de mensalidade menor: [p=0.2] {b}a academia A. [p=0.3] No sétimo mês, {c}A soma quinhentos e dez reais [p=0.2] e {d}B soma quinhentos e vinte e cinco."),
    # situação 3: inequação dupla
    dict(id="s13", block="questao3", text="{a}Situação três. [p=0.2] Resolva {b}um menor ou igual a três xis menos dois, [p=0.2] menor que dez. [p=0.3] {c}Depois, diga como ficam as bolinhas na reta."),
    dict(id="s14", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta3", text="Vamos lá. [p=0.2] {a}Some dois nas três partes: [p=0.2] {b}três menor ou igual a três xis, menor que doze. [p=0.3] {c}Divida as três partes por três, que é positivo: [p=0.2] {d}um menor ou igual a xis, menor que quatro."),
    dict(id="s16", block="resposta3", text="{a}No um, bolinha fechada, porque tem o igual. [p=0.2] {b}No quatro, bolinha aberta. [p=0.2] E {c}pinta só o pedaço entre elas. [p=0.3] Conferindo o um: [p=0.2] {d}três vezes um menos dois dá um, [p=0.2] e um é menor ou igual a um. [p=0.2] {e}Serve."),
    # situação 4: inequação em problema, com sinal virando
    dict(id="s17", block="questao4", text="{a}Última situação, e ela junta tudo. [p=0.2] Uma caixa-d'água tem {b}quinhentos litros [p=0.2] e, com um vazamento, perde {c}vinte litros por hora. [p=0.3] {d}Por quantas horas inteiras, no máximo, ela ainda fica com mais de cento e quarenta litros?"),
    dict(id="s18", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta4", text="Vamos lá. [p=0.2] {a}As horas viram xis. [p=0.2] Depois de xis horas, sobram {b}quinhentos menos vinte xis. [p=0.2] E isso tem que ser {c}maior que cento e quarenta. [p=0.3] {d}Tire quinhentos de cada lado: [p=0.2] {e}menos vinte xis maior que menos trezentos e sessenta."),
    dict(id="s20", block="resposta4", text="{a}Divida por menos vinte. [p=0.2] É negativo, então {b}vira o sinal: [p=0.2] {c}xis menor que dezoito. [p=0.3] Cuidado: {d}com dezoito horas, sobram cento e quarenta litros, [p=0.2] e cento e quarenta não é mais que cento e quarenta. [p=0.3] O maior número inteiro abaixo de dezoito é {e}dezessete. [p=0.2] Resposta: {f}dezessete horas."),
    dict(id="s21", block="resposta4", text="Conferindo: [p=0.2] {a}vinte vezes dezessete dá trezentos e quarenta. [p=0.2] {b}Quinhentos menos trezentos e quarenta dá cento e sessenta litros. [p=0.2] {c}Ainda é mais que cento e quarenta. [p=0.2] {d}Bateu."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}o desconhecido vira xis, [p=0.2] {b}a pergunta decide se é igual, maior ou menor [p=0.2] e {c}a resposta sai com a unidade certa."),
    dict(id="s23", block="fim", text="Na próxima aula, o problema traz {a}duas coisas desconhecidas ao mesmo tempo. [p=0.2] Aí entram {b}duas letras e duas equações: [p=0.2] o {c}sistema, resolvido pelo método da substituição. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
