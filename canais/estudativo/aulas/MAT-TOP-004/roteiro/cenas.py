# Estudativo · MAT-TOP-004 — Princípio da casa dos pombos (Matemática · Tópicos Avançados · Binômio, distribuição binomial e casa dos pombos).
# Habilidade: garantir que entre 13 pessoas duas fazem aniversário no mesmo mês e achar quantas pessoas garantem três no mesmo mês (25).
# Pré-requisitos: MAT-CNT-001 (princípio multiplicativo), MAT-NUM-010 (divisão). Próxima: MAT-TOP-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Sem letras: "a letra no lugar de um número" (MAT-EQU-001) não está na ficha,
# então o atalho é dito em palavras ("as casinhas vezes um a menos do que você quer, mais um").

TITULO = "Princípio da casa dos pombos"

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
    dict(id="s01", block="gancho", text="Numa sala com {a}treze pessoas, [p=0.2] eu garanto, sem perguntar nada a ninguém: [p=0.2] {b}pelo menos duas fazem aniversário no mesmo mês. [p=0.3] Não é sorte. [p=0.2] É {c}certeza."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você descobre quantas pessoas ou objetos garantem uma repetição, [p=0.2] e leva um {b}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você só vai precisar de {a}divisão com resto: [p=0.2] por exemplo, {b}treze dividido por doze dá um, e sobra um. [p=0.3] Se faltar, procure no canal."),
    # pombos
    dict(id="s04", block="pombos", text="A ideia vem de {a}pombos e casinhas. [p=0.2] São {b}quatro pombos e só {c}três casinhas. [p=0.3] Coloque um pombo em cada casinha: [p=0.2] {d}sobra um. [p=0.2] Onde quer que ele entre, {e}alguma casinha fica com dois."),
    dict(id="s05", block="pombos", text="Esse é o {a}princípio da casa dos pombos: [p=0.2] {b}se há mais pombos que casinhas, [p=0.2] {c}pelo menos uma casinha recebe dois ou mais. [p=0.3] Ele não diz {d}qual casinha. [p=0.2] Só garante que {e}ela existe."),
    # meses
    dict(id="s06", block="meses", text="Volte aos aniversários. [p=0.2] As casinhas são {a}os doze meses. [p=0.2] Os pombos são {b}as pessoas. [p=0.3] Pense no {c}pior caso, o azar máximo: [p=0.2] doze pessoas {d}podem nascer cada uma num mês diferente. [p=0.3] Mas a décima terceira {e}não tem mês livre: [p=0.2] ela repete algum."),
    dict(id="s07", block="meses", text="Por isso {a}doze pessoas não garantem nada, [p=0.2] e {b}treze garantem. [p=0.3] Dá para ver na divisão: {c}treze dividido por doze dá um, e sobra um. [p=0.2] Cada mês recebe uma pessoa, [p=0.2] e {d}a que sobra entra em algum mês, que fica com duas."),
    dict(id="s08", block="tres", text="E para garantir {a}três pessoas no mesmo mês? [p=0.2] Pior caso: {b}duas pessoas em cada mês, sem passar de duas. [p=0.2] {c}Doze vezes dois dá vinte e quatro pessoas, sem nenhum trio. [p=0.3] A próxima pessoa {d}fecha um trio: [p=0.2] {e}vinte e cinco."),
    dict(id="s09", block="tres", text="Confira na divisão: {a}vinte e cinco dividido por doze dá dois, e sobra um. [p=0.2] Cada mês fica com duas pessoas, [p=0.2] e {b}a que sobra forma um trio."),
    dict(id="s10", block="dias", text="Com os dias do ano, a ideia é a mesma. [p=0.2] Contando o vinte e nove de fevereiro, são {a}trezentos e sessenta e seis dias possíveis. [p=0.3] Então {b}trezentas e sessenta e sete pessoas garantem duas com o mesmo aniversário, dia e mês. [p=0.2] Com {c}trezentas e sessenta e seis, ainda pode não haver repetição."),
    # meias
    dict(id="s11", block="meias", text="O pior caso também resolve {a}a gaveta de meias. [p=0.2] No escuro, você tira meias de uma gaveta com {b}meias pretas, brancas e azuis. [p=0.2] Quantas tirar para garantir {c}um par da mesma cor? [p=0.3] Pior caso: {d}uma de cada cor, três meias. [p=0.2] {e}A quarta repete uma cor: quatro meias."),
    # erro
    dict(id="s12", block="erro", text="O erro comum é {a}multiplicar direto. [p=0.2] Para três no mesmo mês, a pessoa faz {b}doze vezes três e responde trinta e seis. [p=0.3] Trinta e seis até garantem, [p=0.2] mas a pergunta quer {c}o menor número que garante. [p=0.2] Com {d}vinte e cinco, já não tem como escapar do trio. [p=0.2] {e}Encha cada mês só até quase transbordar."),
    # atalho
    dict(id="s13", block="atalho", text="Agora o atalho: [p=0.2] {a}multiplique as casinhas por um a menos do que quantos você quer na mesma casinha, [p=0.2] e {b}some um. [p=0.3] Três no mesmo mês: {c}doze vezes dois, mais um, vinte e cinco. [p=0.2] Par de meias: {d}três vezes um, mais um, quatro."),
    dict(id="s14", block="atalho", text="Funciona porque a multiplicação é {a}o pior caso: [p=0.2] todas as casinhas cheias até quase transbordar. [p=0.3] {b}Não vale quando a pergunta escolhe a casinha. [p=0.2] Para garantir {c}duas meias pretas, [p=0.2] o pior caso é tirar {d}todas as meias das outras cores primeiro."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma gaveta tem {a}cinco meias brancas, cinco pretas e cinco azuis. [p=0.2] No escuro, {b}quantas você precisa tirar para garantir três da mesma cor? [p=0.2] E para garantir {c}duas pretas?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] Três da mesma cor: {a}as casinhas são as três cores. [p=0.2] Pior caso: {b}duas de cada cor, seis meias. [p=0.2] {c}A sétima fecha o trio: sete meias."),
    dict(id="s18", block="resposta", text="Duas pretas: a pergunta {a}escolhe a cor. [p=0.2] Pior caso: {b}as cinco brancas e as cinco azuis, dez meias, [p=0.2] e só depois {c}duas pretas. [p=0.2] {d}Doze meias."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}imagine o pior caso [p=0.2] e {b}some um."),
    dict(id="s20", block="fim", text="Na próxima aula, você conta {a}quantos números de um a cem são múltiplos de dois ou de três, [p=0.2] sem contar nenhum número duas vezes. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
