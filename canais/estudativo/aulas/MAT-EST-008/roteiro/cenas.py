# Estudativo · MAT-EST-008 — Média aritmética (Matemática · Estatística · Médias).
# Habilidade: calcular a média de 6, 7 e 8 (7) e achar a nota que falta para fechar média 7 em 4 provas, usando total = média × quantidade.
# Pré-requisitos: MAT-EQU-013 (montar a equação do problema), MAT-FRA-017 (dividir com resultado decimal; atalho "metade da metade"). Próxima: MAT-EST-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula.
# Dados: 6 + 7 + 8 = 21; 21 ÷ 3 = 7. Caminhada 5 + 8 + 7 + 9 = 29; 29 ÷ 4 = 7,25.
#   Gancho: notas 6, 8, 5; média 7 em 4 provas → total 28; já tem 19; falta 9. Erro: chutar 8 → 27 ÷ 4 = 6,75.
#   Atalho (sobras e faltas em relação à média): −1 +1 −2 = −2 → 7 + 2 = 9.
# Tela (não narradas): distâncias 5, 8, 7, 9 km (s06); vendas 42, 55, 48, 51 (s13).
#   Questão: média 50 em 5 semanas → 250; 42 + 55 + 48 + 51 = 196; falta 54 (−8 +5 −2 +1 = −4).

TITULO = "Média aritmética e a nota que falta"

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
    dict(id="s01", block="gancho", text="{a}Você tirou seis na primeira prova, [p=0.2] oito na segunda [p=0.2] e cinco na terceira. [p=0.2] Precisa fechar {b}média sete nas quatro. [p=0.3] Muita gente acha que {c}um oito na última resolve. [p=0.3] {d}Não resolve. [p=0.2] Precisa de nove."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você calcula qualquer média, acha o valor que falta [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você precisa de {a}duas coisas: [p=0.2] {b}montar uma equação a partir do problema, com o xis no lugar do que você não sabe, [p=0.2] e {c}continuar a divisão depois da vírgula. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é média
    dict(id="s04", block="ideia", text="O que é a média? [p=0.2] Imagine {a}três amigos: um tem seis reais, outro tem sete, e o terceiro tem oito. [p=0.2] {b}Juntando tudo, dá vinte e um reais. [p=0.2] {c}Dividindo por igual, dá sete para cada um. [p=0.3] {d}Sete é a média: o valor que cada um teria se tudo fosse dividido igualmente."),
    dict(id="s05", block="regra", text="A regra: {a}a média aritmética é a soma dividida pela quantidade. [p=0.2] {b}Seis mais sete mais oito dá vinte e um. [p=0.2] São três valores: {c}vinte e um dividido por três dá sete."),
    dict(id="s06", block="regra", text="A média pode dar {a}um número que ninguém tem. [p=0.2] Uma pessoa caminhou durante quatro dias, {b}e a distância de cada dia está na tela. [p=0.2] {c}A soma dá vinte e nove quilômetros. [p=0.2] {d}Vinte e nove dividido por quatro dá sete vírgula vinte e cinco quilômetros por dia. [p=0.3] Nenhum dia teve esse valor. [p=0.2] {e}Mesmo assim, é a média."),
    # total = média × quantidade
    dict(id="s07", block="total", text="Agora, vire a regra ao contrário. [p=0.2] Lembre dos três amigos: {a}sete reais para cada um, e eram três. [p=0.2] Sete vezes três dá vinte e um, o dinheiro todo. [p=0.3] Então {b}a soma é a média vezes a quantidade. [p=0.2] Chame a soma de total. [p=0.2] {c}Total igual a média vezes quantidade. [p=0.2] É essa conta que acha o valor que falta."),
    dict(id="s08", block="total", text="Volte ao gancho. [p=0.2] Média sete em quatro provas pede {a}um total de sete vezes quatro, que dá vinte e oito pontos. [p=0.2] Você já tem {b}seis mais oito mais cinco, que dá dezenove. [p=0.2] Faltam {c}vinte e oito menos dezenove, que dá nove pontos. [p=0.3] {d}A última prova precisa ser nove."),
    dict(id="s09", block="total", text="Pela equação, chega no mesmo. [p=0.2] {a}A última nota é xis. [p=0.2] {b}Seis mais oito mais cinco mais xis, tudo dividido por quatro, igual a sete. [p=0.2] Multiplique os lados por quatro: {c}dezenove mais xis igual a vinte e oito. [p=0.2] {d}Xis igual a nove."),
    # erro
    dict(id="s10", block="erro", text="E o oito do gancho? [p=0.2] É o erro mais comum: {a}chutar uma nota só um pouco acima da média. [p=0.2] Com oito, o total fica {b}dezenove mais oito, que dá vinte e sete. [p=0.2] {c}Vinte e sete dividido por quatro dá seis vírgula setenta e cinco. [p=0.2] {d}Não chega a sete. [p=0.3] A última nota precisa {e}cobrir também o que faltou nas outras provas."),
    # atalho
    dict(id="s11", block="atalho", text="Agora o atalho: {a}compare cada valor com a média que você quer. [p=0.2] A média é sete. [p=0.2] {b}O seis ficou um abaixo. [p=0.2] {c}O oito ficou um acima. [p=0.2] {d}O cinco ficou dois abaixo. [p=0.3] Saldo: {e}faltam dois. [p=0.2] Então a última nota é {f}sete mais dois, que dá nove."),
    dict(id="s12", block="atalho", text="Funciona porque {a}o que sobra numa nota cobre o que falta em outra. [p=0.2] Fechar média sete é deixar {b}sobras e faltas se anulando. [p=0.3] Serve também para conferir a média dos três amigos. [p=0.2] {c}O seis fica um abaixo do sete, [p=0.2] o oito fica um acima, [p=0.2] e eles se anulam. [p=0.3] {d}Não compensa com muitos valores espalhados: [p=0.2] aí, some e divida."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] Um vendedor precisa de {a}média de cinquenta vendas por semana, em cinco semanas. [p=0.2] {b}As vendas das quatro primeiras semanas estão na tela. [p=0.3] {c}Quantas vendas ele precisa fazer na quinta semana?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] O total é média vezes quantidade: {a}cinquenta vezes cinco dá duzentos e cinquenta. [p=0.2] Ele já vendeu {b}quarenta e dois mais cinquenta e cinco mais quarenta e oito mais cinquenta e um, que dá cento e noventa e seis. [p=0.2] {c}Duzentos e cinquenta menos cento e noventa e seis dá cinquenta e quatro vendas."),
    dict(id="s16", block="resposta", text="Pelo atalho: {a}quarenta e dois fica oito abaixo. [p=0.2] Cinquenta e cinco fica cinco acima. [p=0.2] Quarenta e oito fica dois abaixo. [p=0.2] Cinquenta e um fica um acima. [p=0.3] Saldo: {b}faltam quatro. [p=0.2] {c}Cinquenta mais quatro dá cinquenta e quatro. [p=0.2] Bateu."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: {a}média é a soma dividida pela quantidade. [p=0.2] E {b}o total é a média vezes a quantidade: [p=0.2] é ele que acha o valor que falta."),
    dict(id="s18", block="fim", text="Na próxima aula, nem toda nota vale o mesmo: {a}a média ponderada. [p=0.2] Você vai ver por que {b}seis com peso dois e oito com peso três dão sete vírgula dois. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
