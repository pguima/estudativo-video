# Estudativo · FIS-MAG-004 — Força sobre um fio e motor elétrico (Física · Magnetismo · Magnetismo e indução).
# Habilidade: usar F = B·i·L·sen θ e explicar como essa força faz o motor girar.
# Pré-requisitos: FIS-MAG-002, FIS-MAG-003. Próxima: FIS-MAG-005.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Atalho: q·v = i·L (i = q/Δt e L = v·Δt), então F = B·i·L sai de F = q·v·B.
# Sentido da corrente: o convencional (o das cargas positivas), como na FIS-ELE-008. Mão do tapa: polegar = corrente.

TITULO = "Força sobre um fio e motor elétrico"

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
    dict(id="s01", block="gancho", text="{a}O ventilador, {b}o liquidificador {c}e o carro elétrico giram pelo mesmo motivo: [p=0.3] {d}um fio com corrente, dentro de um campo magnético, é empurrado."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular essa força [p=0.2] e {b}entender como ela faz um motor girar sem parar."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre {a}duas coisas. [p=0.2] {b}Uma carga andando num campo sente força efe igual a quê vê bê seno de teta, [p=0.2] com o sentido dado pela mão do tapa. [p=0.3] E {c}corrente é carga em movimento, em ampère. [p=0.3] Se faltar alguma, procure no canal."),
    # do q·v ao i·L
    dict(id="s04", block="fio", text="Então pense: [p=0.2] {a}um fio com corrente é uma fila de cargas andando. [p=0.3] {b}Se o fio está num campo, cada carga sente uma forcinha, [p=0.2] e {c}o fio inteiro é empurrado."),
    dict(id="s05", block="fio", text="A fórmula fica assim: [p=0.2] {a}efe igual a bê, vezes i, vezes éle, vezes seno de teta. [p=0.3] {b}Bê é o campo, em tesla. [p=0.2] {c}I é a corrente, em ampère. [p=0.2] {d}Éle é o comprimento do fio dentro do campo, em metro. [p=0.2] {e}E teta é o ângulo entre o fio e o campo."),
    dict(id="s06", block="fio", text="Para o sentido, {a}a mesma mão do tapa. [p=0.2] {b}O polegar aponta a corrente, [p=0.2] {c}os dedos apontam o campo, [p=0.2] e {d}a palma empurra para o lado da força."),
    # exemplo
    dict(id="s07", block="exemplo", text="Um exemplo. [p=0.2] {a}Campo de zero vírgula cinco tesla, [p=0.1] corrente de quatro ampères, [p=0.1] vinte centímetros de fio dentro do campo, [p=0.1] em noventa graus. [p=0.3] {b}Passe os centímetros para metro: zero vírgula dois. [p=0.3] {c}Zero vírgula cinco vezes quatro dá dois, [p=0.2] vezes zero vírgula dois, [p=0.1] {d}zero vírgula quatro newton."),
    dict(id="s08", block="exemplo", text="{a}Incline o fio até trinta graus com o campo. [p=0.2] {b}O seno de trinta é meio, [p=0.1] e {c}a força cai para zero vírgula dois newton. [p=0.3] {d}Fio na mesma direção do campo, força zero."),
    # motor
    dict(id="s09", block="motor", text="Agora, o motor. [p=0.2] {a}Coloque uma espira retangular entre os polos de um ímã. [p=0.3] Olhando a espira de lado, [p=0.2] {b}num lado a corrente sai da folha, [p=0.1] e {c}no outro ela entra."),
    dict(id="s10", block="motor", text="Correntes opostas, {a}forças opostas: [p=0.2] {b}um lado é empurrado para cima, [p=0.1] {c}o outro para baixo. [p=0.3] Duas forças assim, em lados opostos, {d}fazem a espira girar, [p=0.1] como as mãos girando um volante."),
    dict(id="s11", block="motor", text="Só que, depois de meia volta, os lados trocam de lugar, [p=0.2] e {a}as forças passariam a girar a espira para trás. [p=0.3] Por isso, existe {b}o comutador: [p=0.2] um anel partido que {c}inverte a corrente a cada meia volta. [p=0.3] {d}Assim, o giro segue sempre no mesmo sentido."),
    dict(id="s12", block="motor", text="{a}No motor de verdade, são centenas de voltas de fio, [p=0.2] e {b}a força soma em cada uma. [p=0.3] {c}A energia elétrica vira movimento."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}usar o comprimento do fio inteiro. [p=0.3] {b}Um fio de dois metros, com só dez centímetros entre os polos do ímã. [p=0.3] {c}Fora do campo, não há força. [p=0.2] {d}O éle da fórmula é zero vírgula um metro."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova. [p=0.2] {a}Você não precisa decorar duas fórmulas. [p=0.3] {b}Corrente é carga dividida pelo tempo, [p=0.1] e {c}comprimento é velocidade vezes tempo. [p=0.3] {d}Multiplique os dois, e o tempo corta: [p=0.2] {e}i vezes éle é igual a quê vezes vê."),
    dict(id="s15", block="atalho", text="Então, {a}na fórmula da carga, troque quê vê por i éle. [p=0.3] {b}Efe igual a quê vê bê vira efe igual a bê i éle. [p=0.3] {c}E a mão é a mesma, com o polegar na corrente. [p=0.3] {d}Num feixe de cargas soltas, sem fio, use a fórmula da carga."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Um fio de cinquenta centímetros está todo dentro de um campo de zero vírgula três tesla, [p=0.2] {b}que entra na folha. [p=0.3] {c}Ele leva dois ampères para a direita. [p=0.3] {d}Qual é a força, e para que lado ela aponta?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Cinquenta centímetros são zero vírgula cinco metro. [p=0.3] {b}O fio está deitado na folha, e o campo fura a folha: [p=0.2] noventa graus, seno igual a um. [p=0.3] {c}Zero vírgula três vezes dois, zero vírgula seis, [p=0.2] vezes zero vírgula cinco: [p=0.1] {d}zero vírgula três newton."),
    dict(id="s19", block="resposta", text="E o sentido: [p=0.2] {a}polegar para a direita, [p=0.1] {b}dedos entrando na folha. [p=0.3] {c}A palma fica virada para cima. [p=0.2] {d}A força aponta para cima."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}efe igual a bê i éle seno de teta, [p=0.2] {b}só conta o fio dentro do campo, [p=0.2] e {c}forças opostas nos dois lados da espira fazem o motor girar. [p=0.3] Na próxima aula, o caminho de volta: [p=0.2] {d}movimento e campo gerando corrente."),
    dict(id="s21", block="fim", text="{a}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {b}Bons estudos!"),
]
