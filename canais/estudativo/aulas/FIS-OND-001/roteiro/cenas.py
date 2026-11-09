# Estudativo · FIS-OND-001 — Oscilações: pêndulo e mola (Física · Ondas e Som · Ondas e seus fenômenos).
# Habilidade: usar T = 2π·√(L/g) e T = 2π·√(m/k), sabendo que a massa não muda o período do pêndulo.
# Pré-requisitos: FIS-CIN-018 (período e frequência), FIS-DIN-005 (lei de Hooke), MAT-POT-007 (raiz quadrada). Próxima: FIS-OND-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Primeira aula da trilha Ondas e Som: guarda a linguagem visual da trilha (veja o visual.py). Questão inédita, criada para esta aula.
# π não está em "Já ensinado" (MAT-POL-004 vem depois): é apresentado como número fixo, perto de 3,14, e a prova manda usar 3.
# Raiz de decimal (MAT-POT-016) também não: cada raiz é conferida elevando ao quadrado (0,2 × 0,2 = 0,04), com MAT-FRA-016.

TITULO = "Oscilações: pêndulo e mola"

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
    dict(id="s01", block="gancho", text="{a}Duas bolas presas em fios do mesmo comprimento: [p=0.2] {b}uma de um quilograma, [p=0.1] {c}a outra de dez. [p=0.3] Solte as duas. [p=0.2] {d}Qual vai e volta mais depressa? [p=0.3] {e}Nenhuma. [p=0.2] As duas levam o mesmo tempo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular o tempo do vai e volta {b}no pêndulo [p=0.1] e {c}na mola, [p=0.2] e saber o que muda esse tempo e o que não muda."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o período, tê, que é o tempo de uma volta completa, em segundos; [p=0.2] e {c}a força da mola, efe igual a cá vezes xis. [p=0.3] Se faltar alguma, procure no canal."),
    # oscilação
    dict(id="s04", block="oscilar", text="Um corpo que vai e volta, sempre pelo mesmo caminho, {a}está oscilando. [p=0.2] Ele passa por {b}um ponto do meio, onde ficaria parado se ninguém mexesse: [p=0.2] {c}a posição de equilíbrio. [p=0.3] E o maior afastamento desse ponto se chama {d}amplitude."),
    dict(id="s05", block="oscilar", text="{a}Ir até um lado, voltar, ir até o outro e voltar ao começo: [p=0.2] isso é uma oscilação completa. [p=0.2] O tempo dela é {b}o período, o mesmo tê das voltas de uma roda. [p=0.3] Quando a força sempre puxa o corpo de volta para o meio, [p=0.1] e cresce na mesma proporção do afastamento, [p=0.2] o nome é {c}movimento harmônico simples."),
    # pêndulo
    dict(id="s06", block="pendulo", text="Comece pelo {a}pêndulo: uma bolinha presa num fio. [p=0.2] Tire do meio e solte. [p=0.2] {b}O peso puxa a bolinha de volta, [p=0.2] ela passa do ponto [p=0.1] e {c}sobe do outro lado."),
    dict(id="s07", block="pendulo", text="O período do pêndulo é {a}tê igual a dois pi vezes a raiz de ele dividido por gê. [p=0.3] {b}Ele é o comprimento do fio, em metros. [p=0.2] {c}Gê é a aceleração da gravidade, dez metros por segundo ao quadrado. [p=0.3] E {d}pi é um número fixo, perto de três vírgula catorze. [p=0.2] De onde ele vem é assunto da aula de circunferência. [p=0.2] {e}Muitas provas mandam usar pi igual a três."),
    dict(id="s08", block="pendulo", text="Repare no que {a}não está na fórmula: [p=0.2] {b}a massa. [p=0.2] Bola leve ou pesada, mesmo fio, mesmo período. [p=0.3] É o mesmo motivo de, na queda livre, a bola leve e a pesada caírem juntas: [p=0.2] {c}a bola pesada é puxada com mais força, [p=0.1] mas também é mais difícil de mover. [p=0.2] Uma coisa compensa a outra. [p=0.3] {d}E a amplitude também não entra, desde que a abertura seja pequena."),
    dict(id="s09", block="pendulo", text="Um pêndulo de {a}quarenta centímetros, [p=0.1] zero vírgula quatro metro. [p=0.2] {b}Zero vírgula quatro dividido por dez: zero vírgula zero quatro. [p=0.2] {c}A raiz é zero vírgula dois, [p=0.1] porque zero vírgula dois vezes zero vírgula dois dá zero vírgula zero quatro. [p=0.3] {d}Dois vezes três vezes zero vírgula dois: [p=0.1] {e}um vírgula dois segundo."),
    # mola
    dict(id="s10", block="mola", text="Agora, {a}a mola: um bloco preso numa mola, num chão liso. [p=0.2] Puxe e solte. [p=0.2] {b}A mola puxa o bloco de volta, [p=0.2] ele passa do meio, {c}aperta a mola, [p=0.2] e ela empurra de novo."),
    dict(id="s11", block="mola", text="O período da mola é {a}tê igual a dois pi vezes a raiz de eme dividido por cá. [p=0.3] {b}Eme é a massa do bloco, em quilogramas. [p=0.2] {c}Cá é a constante da mola, em newtons por metro: [p=0.1] mola dura, cá grande. [p=0.3] Aqui, {d}a massa entra: [p=0.1] bloco de mais massa é mais difícil de mover, [p=0.1] e a força da mola não cresce por causa disso. [p=0.3] {e}E a gravidade não entra: [p=0.1] deitada ou pendurada, a mola tem o mesmo período."),
    dict(id="s12", block="mola", text="Um bloco de {a}meio quilograma, numa mola de {b}cinquenta newtons por metro. [p=0.2] {c}Zero vírgula cinco dividido por cinquenta: zero vírgula zero um. [p=0.2] {d}A raiz é zero vírgula um. [p=0.2] {e}Dois vezes três vezes zero vírgula um: [p=0.1] {f}zero vírgula seis segundo."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}dobrar o fio e achar que o período dobra. [p=0.3] O comprimento está {b}dentro da raiz. [p=0.2] Para o período dobrar, {c}o fio precisa ficar quatro vezes maior. [p=0.3] Teste com {d}um vírgula seis metro, quatro vezes o pêndulo de antes. [p=0.2] {e}Um vírgula seis dividido por dez, zero vírgula dezesseis, [p=0.1] raiz zero vírgula quatro. [p=0.2] {f}Seis vezes zero vírgula quatro: dois vírgula quatro segundos, [p=0.1] o dobro de um vírgula dois."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}o período anda com a raiz. [p=0.3] {b}Quatro vezes o comprimento, ou quatro vezes a massa na mola: [p=0.1] dobro do período. [p=0.2] {c}Nove vezes: triplo. [p=0.3] Funciona porque a raiz de quatro é dois, e a raiz de nove é três. [p=0.2] {d}Não compensa quando a conta não é um quadrado, como o dobro do fio: [p=0.1] aí, faça a conta."),
    dict(id="s15", block="atalho", text="E mais um: [p=0.2] {a}pi vezes pi é quase dez, o valor de gê. [p=0.3] Por isso, na Terra, {b}o período do pêndulo é quase duas vezes a raiz do comprimento. [p=0.3] {c}Fio de um metro: cerca de dois segundos. [p=0.2] {d}Fio de quatro metros: cerca de quatro. [p=0.2] É só uma estimativa: se a prova mandar usar pi igual a três, faça a conta."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Um bloco de nove quilogramas oscila preso a uma mola de cem newtons por metro. [p=0.2] {b}Use pi igual a três. [p=0.3] {c}Qual é o período? [p=0.2] {d}E se o bloco for trocado por um de trinta e seis quilogramas?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Nove dividido por cem: zero vírgula zero nove. [p=0.2] {b}A raiz é zero vírgula três, [p=0.1] porque zero vírgula três vezes zero vírgula três dá zero vírgula zero nove. [p=0.2] {c}Dois vezes três vezes zero vírgula três: [p=0.1] {d}um vírgula oito segundo."),
    dict(id="s19", block="resposta", text="Com trinta e seis quilogramas, {a}a massa ficou quatro vezes maior. [p=0.2] Pelo atalho, {b}o período dobra: [p=0.1] {c}três vírgula seis segundos. [p=0.3] Na conta: {d}trinta e seis dividido por cem, zero vírgula trinta e seis, [p=0.1] raiz zero vírgula seis, [p=0.1] e seis vezes zero vírgula seis, [p=0.1] {e}os mesmos três vírgula seis."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}no pêndulo, entram o fio e a gravidade, e a massa não entra; [p=0.2] {b}na mola, entram a massa e o cá, e a gravidade não entra; [p=0.2] {c}quatro vezes mais dentro da raiz, período em dobro."),
    dict(id="s21", block="fim", text="Na próxima aula, esse vai e volta {a}viaja: [p=0.2] você vai conhecer {b}as ondas [p=0.1] e a equação {c}vê igual a lambda vezes efe. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
