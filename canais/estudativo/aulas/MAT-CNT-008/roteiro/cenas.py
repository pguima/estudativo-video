# Estudativo · MAT-CNT-008 — Combinação: quando a ordem não importa (Matemática · Contagem e Probabilidade · Permutações, arranjos e combinações).
# Habilidade: contar as comissões de 3 entre 8 pessoas (56) e dizer por que é o arranjo dividido por 3!.
# Pré-requisitos: MAT-CNT-007 (arranjo, teste da troca), MAT-CNT-004 (fatorial). Próxima: MAT-CNT-009.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; "!" narrado como "fatorial".
# Questões inéditas, criadas para esta aula. Comissões com grupos e "pelo menos um" ficam para MAT-CNT-009.

TITULO = "Combinação: quando a ordem não importa"

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
    dict(id="s01", block="gancho", text="{a}Oito pessoas. [p=0.2] Uma {b}comissão de três. [p=0.3] Quem usa a conta do pódio responde {c}trezentos e trinta e seis. [p=0.3] Mas comissão não tem ouro nem prata. [p=0.2] São só {d}cinquenta e seis."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você conta escolhas em que a ordem não importa, [p=0.2] entende {b}de onde vem a divisão [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}o arranjo: [p=0.2] escolher alguns em uma ordem que importa, [p=0.2] multiplicando {b}descendo do total, um número por lugar. [p=0.3] E {c}o teste da troca. [p=0.3] Se faltar alguma, procure no canal."),
    # teste da troca
    dict(id="s04", block="troca", text="Faça o teste da troca. [p=0.2] Pegue uma comissão: {a}Ana, Bia e Caio. [p=0.2] Troque a ordem: {b}Bia, Caio e Ana. [p=0.3] {c}Continua a mesma comissão: [p=0.2] as mesmas três pessoas, sem cargo. [p=0.2] {d}A ordem não importa."),
    # repetições
    dict(id="s05", block="repetidas", text="Então, de onde saiu o trezentos e trinta e seis? [p=0.2] O arranjo conta {a}cada ordem como um resultado diferente. [p=0.3] Liste as ordens de Ana, Bia e Caio: [p=0.2] {b}são seis. [p=0.2] No arranjo, são {c}seis resultados. [p=0.2] Na comissão, {d}um só."),
    dict(id="s06", block="repetidas", text="Por que seis? [p=0.2] Três pessoas se arrumam em fila de {a}três fatorial jeitos: [p=0.2] {b}três vezes dois vezes um dá seis. [p=0.3] E isso vale para {c}toda comissão: [p=0.2] cada uma aparece seis vezes no arranjo."),
    dict(id="s07", block="repetidas", text="Então {a}divida pelas repetições. [p=0.2] {b}Trezentos e trinta e seis dividido por seis dá cinquenta e seis comissões."),
    # regra
    dict(id="s08", block="regra", text="Escolher alguns {a}sem que a ordem importe [p=0.2] se chama {b}combinação. [p=0.3] A regra: {c}faça o arranjo [p=0.2] e {d}divida pelo fatorial de quantos foram escolhidos."),
    dict(id="s09", block="regra", text="Na fórmula, {a}ene é o total e pê é quantos você escolhe. [p=0.2] {b}Em cima, o arranjo: pê números descendo do ene. [p=0.2] {c}Embaixo, pê fatorial. [p=0.3] Nos livros, ela aparece toda em fatoriais: [p=0.2] {d}ene fatorial dividido por pê fatorial vezes o fatorial de ene menos pê. [p=0.2] É a mesma conta, só que sem cortar."),
    dict(id="s10", block="regra", text="E se você escolher {a}todos os oito? [p=0.2] Embaixo aparece {b}zero fatorial, que vale um. [p=0.2] A conta dá {c}um: [p=0.2] uma comissão só, com todo mundo dentro. [p=0.3] Faz sentido: não sobrou ninguém para escolher."),
    # pizza
    dict(id="s11", block="pizza", text="Mais um exemplo. [p=0.2] Uma pizzaria faz {a}pizza meio a meio, com dois sabores diferentes, [p=0.2] entre {b}cinco sabores. [p=0.3] Calabresa com queijo é a mesma pizza que queijo com calabresa: [p=0.2] {c}combinação. [p=0.3] {d}Cinco vezes quatro dá vinte. [p=0.2] {e}Vinte dividido por dois fatorial dá dez pizzas."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}dividir só pelo número de escolhidos. [p=0.2] A pessoa faz {b}trezentos e trinta e seis dividido por três [p=0.2] e responde {c}cento e doze. [p=0.3] Mas cada comissão não aparece três vezes no arranjo. [p=0.2] Aparece {d}seis vezes: [p=0.2] uma para cada ordem. [p=0.2] {e}Divida por três fatorial, não por três."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: {a}escolher quem entra é o mesmo que escolher quem fica de fora. [p=0.3] Uma comissão de {b}oito pessoas entre dez? [p=0.2] Escolha {c}quem fica de fora: só duas pessoas. [p=0.2] {d}Dez vezes nove dá noventa. [p=0.2] {e}Noventa dividido por dois fatorial dá quarenta e cinco."),
    dict(id="s14", block="atalho", text="Funciona porque {a}cada comissão de oito deixa exatamente duas pessoas de fora, [p=0.2] e cada dupla de fora {b}forma uma comissão só. [p=0.3] Compensa quando {c}você escolhe mais da metade. [p=0.2] {d}Escolhendo menos da metade, faça a conta direto. [p=0.3] Sete pessoas entre nove? [p=0.2] Pense nas duas de fora: [p=0.2] nove vezes oito dividido por dois dá {e}trinta e seis."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Numa turma de {a}onze pessoas, o professor vai formar {b}uma dupla para apresentar um trabalho. [p=0.3] {c}Quantas duplas são possíveis? [p=0.2] E de quantos jeitos você escolhe {d}três livros entre seis para levar numa viagem?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Na dupla, {a}trocar a ordem não muda nada: combinação. [p=0.2] {b}Onze vezes dez dá cento e dez. [p=0.2] {c}Cento e dez dividido por dois fatorial dá cinquenta e cinco duplas."),
    dict(id="s18", block="resposta", text="Nos livros, também {a}não há ordem. [p=0.2] {b}Seis vezes cinco vezes quatro dá cento e vinte. [p=0.2] {c}Cento e vinte dividido por três fatorial, que é seis, [p=0.2] dá {d}vinte jeitos."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}a ordem não importa? É combinação. [p=0.2] {b}Faça o arranjo e divida pelo fatorial de quantos foram escolhidos."),
    dict(id="s20", block="fim", text="Na próxima aula, as comissões ganham regras: [p=0.2] {a}dois homens entre cinco e duas mulheres entre quatro, [p=0.2] e o famoso {b}pelo menos um. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
