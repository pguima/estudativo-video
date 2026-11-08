# Estudativo · MAT-CNT-007 — Arranjo: quando a ordem importa (Matemática · Contagem e Probabilidade · Permutações, arranjos e combinações).
# Habilidade: contar os pódios de 3 entre 8 corredores (336) e testar se trocar a ordem muda o resultado.
# Pré-requisitos: MAT-CNT-005 (permutação simples), MAT-CNT-004 (fatorial e corte de fatoriais), MAT-CNT-001 (casinhas). Próxima: MAT-CNT-008.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso; "!" narrado como "fatorial".
# Questão inédita, criada para esta aula. Combinação (ordem não importa) só é anunciada, fica para MAT-CNT-008.

TITULO = "Arranjo: quando a ordem importa"

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
    dict(id="s01", block="gancho", text="{a}Oito corredores na final. [p=0.2] {b}Ouro, prata e bronze. [p=0.3] Quantos pódios diferentes podem sair? [p=0.3] Não é {c}oito fatorial, que passa de quarenta mil. [p=0.2] São {d}trezentos e trinta e seis."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você conta escolhas em que a ordem importa, [p=0.2] aprende {b}um teste para saber quando ela importa [p=0.2] e leva um {c}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar {a}as casinhas do princípio multiplicativo, [p=0.2] {b}o fatorial [p=0.2] e {c}o corte de fatoriais numa divisão: [p=0.2] oito fatorial dividido por seis fatorial deixa oito vezes sete, que dá cinquenta e seis. [p=0.3] Se faltar alguma, procure no canal."),
    # pódio
    dict(id="s04", block="podio", text="Faça {a}uma casinha para cada lugar do pódio. [p=0.2] No ouro, cabe {b}qualquer um dos oito. [p=0.2] Na prata, {c}sobram sete, [p=0.2] porque quem ganhou o ouro não ganha a prata. [p=0.2] No bronze, {d}sobram seis."),
    dict(id="s05", block="podio", text="{a}Oito vezes sete dá cinquenta e seis. [p=0.2] {b}Vezes seis dá trezentos e trinta e seis pódios."),
    dict(id="s06", block="podio", text="Repare: {a}é a mesma conta da fila, [p=0.2] só que ela {b}para no meio. [p=0.3] Na fila, todos os oito entram, e a conta desce até o um. [p=0.2] No pódio, {c}só três sobem, [p=0.2] então são {d}só três casinhas."),
    # teste da troca
    dict(id="s07", block="troca", text="Mas como saber se a ordem importa? [p=0.2] Faça {a}o teste da troca. [p=0.3] Pegue um resultado: {b}Ana no ouro, Bia na prata, Caio no bronze. [p=0.2] Agora {c}troque Ana e Bia de lugar."),
    dict(id="s08", block="troca", text="Bia com o ouro e Ana com a prata é {a}outro pódio. [p=0.2] Outra foto, outra medalha no peito. [p=0.3] {b}Trocar a ordem mudou o resultado. [p=0.2] Então {c}a ordem importa."),
    dict(id="s09", block="troca", text="Compare com outra situação. [p=0.2] Os mesmos oito corredores, mas agora {a}os três primeiros só ganham vaga na próxima prova. [p=0.3] Ana, Bia e Caio classificados, [p=0.2] ou Bia, Ana e Caio: [p=0.2] {b}é o mesmo grupo. [p=0.3] Aqui, {c}a ordem não importa, e a conta é outra. [p=0.2] Esse caso fica para a próxima aula."),
    # regra
    dict(id="s10", block="regra", text="Escolher {a}só alguns, em uma ordem que importa, [p=0.2] se chama {b}arranjo. [p=0.3] O pódio é um {c}arranjo de oito elementos tomados três a três."),
    dict(id="s11", block="regra", text="Na fórmula, {a}ene é o total [p=0.2] e {b}pê é quantos você escolhe. [p=0.3] O arranjo é {c}ene fatorial dividido pelo fatorial de ene menos pê."),
    dict(id="s12", block="regra", text="De onde vem isso? [p=0.2] {a}Oito fatorial arruma os oito corredores em fila. [p=0.3] Mas a ordem dos {b}cinco que ficaram fora do pódio não interessa. [p=0.2] Por isso, {c}divida por cinco fatorial. [p=0.3] Corte como você já sabe: [p=0.2] {d}sobra oito vezes sete vezes seis, [p=0.2] que dá trezentos e trinta e seis de novo."),
    dict(id="s13", block="regra", text="E se {a}todos entrarem, como numa fila? [p=0.2] Embaixo fica {b}zero fatorial, que vale um. [p=0.3] O arranjo vira {c}o fatorial do total: [p=0.2] é a permutação que você já conhece."),
    # erro
    dict(id="s14", block="erro", text="O erro comum é {a}usar o fatorial do total. [p=0.2] A pessoa pensa em fila, faz {b}oito fatorial [p=0.2] e responde {c}quarenta mil trezentos e vinte. [p=0.3] Isso conta a ordem de chegada {d}dos oito corredores, até o último. [p=0.2] O pódio só olha {e}os três primeiros."),
    # atalho
    dict(id="s15", block="atalho", text="Agora o atalho: {a}o arranjo é uma multiplicação descendo do total, [p=0.2] {b}com tantos números quantos são os lugares. [p=0.3] Três lugares entre oito: {c}três números, descendo do oito. [p=0.3] Dois lugares entre dez? [p=0.2] {d}Dez vezes nove dá noventa."),
    dict(id="s16", block="atalho", text="Funciona porque {a}cada lugar tem uma opção a menos que o anterior, [p=0.2] e a fórmula corta o resto. [p=0.3] {b}Não compensa quando há regra no meio, [p=0.2] como o zero que não pode vir na frente de um número: [p=0.2] aí, volte às casinhas e {c}comece pela mais difícil."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Um clube tem {a}dez sócios [p=0.2] e vai escolher {b}presidente, vice e tesoureiro. [p=0.3] {c}Quantas chapas diferentes são possíveis? [p=0.2] Antes da conta, {d}faça o teste da troca."),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] O teste: {a}Ana presidente e Bia vice [p=0.2] é diferente de {b}Bia presidente e Ana vice. [p=0.2] Os cargos são diferentes, então {c}a ordem importa: é arranjo."),
    dict(id="s20", block="resposta", text="São três cargos: {a}três números descendo do dez. [p=0.2] {b}Dez vezes nove dá noventa. [p=0.2] {c}Noventa vezes oito dá setecentos e vinte chapas."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}escolhe só alguns, e trocar a ordem muda o resultado? [p=0.2] {b}É arranjo: multiplique descendo do total, um número por lugar."),
    dict(id="s22", block="fim", text="Na próxima aula, a ordem {a}deixa de importar: [p=0.2] uma {b}comissão de três pessoas entre oito. [p=0.3] E você vai ver por que a resposta é {c}o arranjo dividido por três fatorial. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
