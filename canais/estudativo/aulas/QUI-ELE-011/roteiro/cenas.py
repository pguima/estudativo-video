# Estudativo · QUI-ELE-011 — Emissões alfa, beta e gama (Química · Eletroquímica e Radioatividade · Radioatividade).
# Habilidade: escrever a equação de um decaimento, comparar o poder de penetração das emissões e contar que do ²³⁸U ao ²⁰⁶Pb
# saem 8 alfas e 6 betas.
# Pré-requisitos: QUI-ATO-004, MAT-EQU-008. Próxima: QUI-ELE-012 (meia-vida e datação por carbono-14).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Primeira aula do módulo: guarda a linguagem visual da radioatividade.
# Questão inédita, criada para esta aula. "Já ensinado" não tem a tabela periódica: os números atômicos vêm como dado.
# Fatos: Becquerel (1896) e Marie Curie. α = ⁴₂He (2 p + 2 n): A − 4, Z − 2. β = ⁰₋₁β: um nêutron vira próton + elétron, que sai:
# A igual, Z + 1. γ = onda eletromagnética, sem massa nem carga: não muda A nem Z.
# ²³⁸₉₂U → ⁴₂α + ²³⁴₉₀Th · ²³⁴₉₀Th → ⁰₋₁β + ²³⁴₉₁Pa. Penetração: α para numa folha de papel; β atravessa o papel e para em
# alguns milímetros de alumínio; γ atravessa o alumínio e pede chumbo grosso ou concreto.
# ²³⁸U → ²⁰⁶Pb: ΔA = 32 → 8 α · 92 − 16 = 76 · 82 − 76 = 6 β. Erro (β diminui Z): 76 − 82 = −6, "menos seis betas", impossível.
# Questão: ²³²₉₀Th → ²⁰⁸₈₂Pb: ΔA = 24 → 6 α · 90 − 12 = 78 · 82 − 78 = 4 β.
# Leituras: ²³⁸₉₂U = "urânio duzentos e trinta e oito, com número atômico noventa e dois".

TITULO = "Emissões alfa, beta e gama"

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
    dict(id="s01", block="gancho", text="{a}O urânio leva bilhões de anos para virar chumbo. [p=0.3] {b}No caminho, o núcleo dele cospe partículas, uma de cada vez. [p=0.3] {c}Dá para contar quantas, [p=0.1] {d}com uma conta de trinta segundos."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai escrever {b}a equação de um decaimento, [p=0.2] {c}comparar quanto cada emissão atravessa [p=0.1] e {d}contar as partículas do urânio ao chumbo. [p=0.2] E ainda leva um {e}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de duas coisas. [p=0.2] {a}No núcleo, há prótons e nêutrons: [p=0.1] {b}o número atômico conta os prótons, {c}e o número de massa conta prótons mais nêutrons. [p=0.2] Aqui, vou chamar o número de massa só de massa. [p=0.3] E {d}resolver uma equação simples. [p=0.2] Se faltar alguma, procure no canal."),
    # radioatividade
    dict(id="s04", block="ideia", text="Alguns núcleos são instáveis, [p=0.1] com prótons e nêutrons demais, ou na proporção errada. [p=0.3] {a}Para ficar estáveis, eles soltam partículas ou energia. [p=0.2] {b}Isso é a radioatividade, [p=0.1] estudada por Becquerel e por Marie Curie no fim do século dezenove. [p=0.3] {c}Quando o núcleo solta algo e vira outro, se diz que ele decaiu."),
    dict(id="s05", block="ideia", text="{a}Para escrever o núcleo, a prova usa o símbolo com dois números. [p=0.2] {b}Em cima, a massa. [p=0.1] {c}Embaixo, o número atômico. [p=0.3] {d}Urânio duzentos e trinta e oito, com número atômico noventa e dois."),
    # alfa
    dict(id="s06", block="alfa", text="{a}A primeira emissão é a alfa. [p=0.2] {b}Ela é um pacote de dois prótons e dois nêutrons, [p=0.1] {c}igual ao núcleo do hélio. [p=0.3] {d}Massa quatro, número atômico dois."),
    dict(id="s07", block="alfa", text="{a}O urânio duzentos e trinta e oito solta uma alfa. [p=0.2] {b}A massa cai quatro: duzentos e trinta e quatro. [p=0.2] {c}O número atômico cai dois: noventa. [p=0.3] {d}Com noventa prótons, já é outro elemento: o tório. [p=0.3] {e}Repare: em cima, duzentos e trinta e oito é duzentos e trinta e quatro mais quatro. [p=0.2] Embaixo, noventa e dois é noventa mais dois. [p=0.2] As somas fecham."),
    # beta
    dict(id="s08", block="beta", text="{a}A segunda é a beta. [p=0.2] {b}Dentro do núcleo, um nêutron vira um próton e um elétron, [p=0.1] {c}e o elétron é atirado para fora. [p=0.3] {d}Por isso, a beta tem massa zero e carga menos um."),
    dict(id="s09", block="beta", text="{a}O tório duzentos e trinta e quatro solta uma beta. [p=0.2] {b}A massa não muda: [p=0.1] trocou um nêutron por um próton. [p=0.2] {c}O número atômico sobe um: noventa e um. [p=0.3] {d}Virou o protactínio."),
    # gama
    dict(id="s10", block="gama", text="{a}A terceira é a gama. [p=0.2] {b}Ela não é partícula: é uma onda, como a luz, só que com muito mais energia. [p=0.3] {c}Sem massa e sem carga, [p=0.1] {d}ela não muda nem a massa nem o número atômico. [p=0.2] {e}Costuma sair junto com uma alfa ou uma beta."),
    # penetração
    dict(id="s11", block="penetra", text="E qual atravessa mais? [p=0.2] {a}A alfa é grande e lenta: [p=0.1] {b}para numa folha de papel, ou na pele. [p=0.3] {c}A beta passa o papel, [p=0.1] {d}mas para em alguns milímetros de alumínio. [p=0.3] {e}A gama atravessa os dois, [p=0.1] {f}e só uma parede grossa de chumbo ou de concreto segura a maior parte."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que a beta diminui o número atômico, só porque ela é negativa. [p=0.3] {b}É o contrário. [p=0.2] {c}A beta sai porque um nêutron virou próton. [p=0.2] {d}O núcleo fica com um próton a mais: [p=0.1] {e}o número atômico sobe."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho: [p=0.2] do urânio duzentos e trinta e oito, com número atômico noventa e dois, [p=0.1] {a}até o chumbo duzentos e seis, com número atômico oitenta e dois. [p=0.3] {b}Conte as alfas pela massa, porque só a alfa mexe nela. [p=0.2] {c}A massa caiu trinta e dois. [p=0.1] {d}Trinta e dois dividido por quatro: [p=0.1] {e}oito alfas."),
    dict(id="s14", block="atalho", text="{a}Oito alfas tiram dezesseis prótons: [p=0.1] {b}noventa e dois menos dezesseis dá setenta e seis. [p=0.3] {c}Mas o chumbo tem oitenta e dois. [p=0.2] {d}Faltam seis, [p=0.1] e quem sobe o número atômico é a beta: {e}seis betas."),
    dict(id="s15", block="atalho", text="Funciona porque {a}a beta não mexe na massa, [p=0.1] então a massa conta só as alfas. [p=0.3] {b}Não compensa se a questão citar outra partícula, além da alfa e da beta: [p=0.1] {c}aí, monte as duas somas, a de cima e a de baixo. [p=0.2] E se a massa não cair num múltiplo de quatro, confira os dados."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}O tório duzentos e trinta e dois, com número atômico noventa, [p=0.1] {b}vira chumbo duzentos e oito, com número atômico oitenta e dois. [p=0.3] {c}Quantas alfas e quantas betas saem?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}A massa caiu de duzentos e trinta e dois para duzentos e oito: vinte e quatro. [p=0.2] {b}Vinte e quatro dividido por quatro: seis alfas. [p=0.3] {c}Seis alfas tiram doze prótons: [p=0.1] noventa menos doze dá setenta e oito. [p=0.2] {d}Até oitenta e dois, faltam quatro: [p=0.1] {e}quatro betas."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}a alfa tira quatro da massa e dois do número atômico; [p=0.1] {b}a beta sobe o número atômico em um; [p=0.1] {c}a gama não muda nada e é a que mais atravessa."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai ver {a}quanto tempo um material leva para perder metade dos núcleos, a meia-vida, [p=0.2] e {b}como ela diz a idade de um fóssil. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
