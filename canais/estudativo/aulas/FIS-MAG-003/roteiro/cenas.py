# Estudativo · FIS-MAG-003 — Força magnética sobre uma carga (Física · Magnetismo · Magnetismo e indução).
# Habilidade: usar F = q·v·B·sen θ, achar o sentido com a regra da mão e o raio da curva da carga.
# Pré-requisitos: FIS-MAG-001, FIS-DIN-010, MAT-TRI-003. Próxima: FIS-MAG-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. FIS-MAG-002 (símbolos de campo saindo e entrando) não está em "Já ensinado":
# os símbolos são explicados de novo aqui. Corrente elétrica também não está: a aula fala só de carga em movimento.
# Regra da mão direita espalmada (o "tapa"): polegar = v, quatro dedos = B, palma = F na carga positiva; negativa, costas da mão.

TITULO = "Força magnética sobre uma carga"

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
    dict(id="s01", block="gancho", text="{a}O Sol joga no espaço uma chuva de partículas com carga. [p=0.3] {b}Quando ela chega perto da Terra, [p=0.1] o campo magnético do planeta {c}guia as partículas, pelas linhas de campo, até as regiões dos polos. [p=0.3] {d}É de lá que vem a aurora boreal."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular essa força, [p=0.2] {b}achar o sentido dela com a mão [p=0.2] e {c}descobrir o raio da curva que a carga faz."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre {a}duas coisas. [p=0.2] {b}No movimento em círculo, a força para o centro vale massa vezes vê ao quadrado, dividido pelo raio. [p=0.3] E {c}o seno de noventa graus é um, [p=0.1] e o de trinta é meio. [p=0.3] Se faltar alguma, procure no canal."),
    # quando existe
    dict(id="s04", block="quando", text="Um ímã {a}não faz força numa carga parada. [p=0.3] A força magnética só aparece com {b}carga em movimento, [p=0.2] e {c}depende do ângulo entre a velocidade e o campo."),
    dict(id="s05", block="quando", text="{a}Se a carga anda na mesma direção do campo, [p=0.2] a força é zero. [p=0.3] {b}Se ela corta o campo de lado, em noventa graus, [p=0.2] a força é a maior possível."),
    # fórmula
    dict(id="s06", block="formula", text="A fórmula junta tudo isso. [p=0.2] {a}Efe igual a quê, vezes vê, vezes bê, vezes seno de teta. [p=0.3] {b}Quê é a carga, em coulomb. [p=0.2] {c}Vê é a velocidade, em metro por segundo. [p=0.2] {d}Bê é o campo, em tesla. [p=0.2] {e}E teta é o ângulo entre a velocidade e o campo."),
    dict(id="s07", block="formula", text="Um exemplo. [p=0.2] {a}Carga de dois vezes dez a menos seis coulomb, [p=0.1] a quatro vezes dez ao cubo metros por segundo, [p=0.1] num campo de zero vírgula cinco tesla, [p=0.1] com ângulo de trinta graus. [p=0.3] {b}Dois vezes quatro dá oito, [p=0.1] e dez a menos seis vezes dez ao cubo dá dez a menos três. [p=0.2] {c}Vezes zero vírgula cinco, [p=0.1] vezes o seno de trinta, que é meio: [p=0.2] {d}dois vezes dez a menos três newton."),
    # sentido
    dict(id="s08", block="sentido", text="E o sentido? [p=0.2] A força é {a}perpendicular à velocidade e ao campo ao mesmo tempo. [p=0.3] Para achar qual, use {b}a mão direita aberta, [p=0.2] como quem vai dar um tapa."),
    dict(id="s09", block="sentido", text="{a}O polegar aponta a velocidade. [p=0.2] {b}Os outros quatro dedos apontam o campo. [p=0.2] {c}A palma empurra para o lado da força. [p=0.3] Isso vale para a carga positiva. [p=0.2] {d}Na carga negativa, a força é para o lado das costas da mão."),
    dict(id="s10", block="sentido", text="Na prova, o campo costuma {a}furar a folha. [p=0.2] {b}Um ponto num círculo é o campo saindo da folha, para você. [p=0.2] {c}Um xis num círculo é o campo entrando na folha."),
    # curva
    dict(id="s11", block="curva", text="Agora, o mais bonito. [p=0.2] Como a força é sempre perpendicular à velocidade, [p=0.2] {a}ela não acelera nem freia a carga: [p=0.2] {b}só muda a direção. [p=0.3] Com a velocidade em noventa graus com o campo, [p=0.2] {c}a carga faz um círculo, [p=0.1] e a força magnética é a força para o centro."),
    dict(id="s12", block="curva", text="Então, {a}iguale as duas: [p=0.2] quê vê bê igual a eme vê ao quadrado, dividido por erre. [p=0.3] {b}Corte um vê de cada lado [p=0.1] e isole o raio: [p=0.2] {c}erre igual a eme vê, dividido por quê bê."),
    dict(id="s13", block="curva", text="Na mesma carga do exemplo, com massa de cinco vezes dez a menos dez quilogramas e ângulo de noventa graus: [p=0.3] {a}em cima, cinco vezes dez a menos dez, vezes quatro vezes dez ao cubo, [p=0.1] dois vezes dez a menos seis. [p=0.3] {b}Embaixo, dois vezes dez a menos seis, vezes zero vírgula cinco, [p=0.1] dez a menos seis. [p=0.3] {c}O raio é dois metros."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que a força magnética deixa a carga mais rápida. [p=0.3] {b}Ela empurra sempre de lado, [p=0.2] como a corda de quem gira uma pedra. [p=0.3] {c}A velocidade muda de direção, [p=0.1] mas o valor dela fica igual."),
    # atalho
    dict(id="s15", block="atalho", text="Agora, o atalho de prova. [p=0.2] {a}Não decore a fórmula do raio: [p=0.2] {b}iguale a força magnética à força para o centro [p=0.1] e corte um vê. [p=0.3] {c}E leia como proporção: [p=0.2] {d}mais massa ou mais velocidade, curva mais aberta. [p=0.2] {e}Mais carga ou mais campo, curva mais fechada."),
    dict(id="s16", block="atalho", text="E antes de qualquer conta, {a}olhe o ângulo. [p=0.2] {b}Velocidade na direção do campo, força zero, [p=0.2] e a carga segue reta. [p=0.3] {c}O atalho do raio só vale com o ângulo de noventa graus."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Um elétron entra num campo que entra na folha, [p=0.2] {b}andando para a direita. [p=0.3] {c}Para que lado aponta a força quando ele entra? [p=0.3] E mais: {d}se a velocidade dobrar, o que acontece com o raio da curva?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Polegar para a direita, [p=0.1] {b}dedos entrando na folha. [p=0.3] {c}A palma fica virada para cima. [p=0.2] {d}Mas o elétron é negativo: [p=0.1] a força é para o lado das costas. [p=0.3] {e}Para baixo."),
    dict(id="s20", block="resposta", text="{a}Erre igual a eme vê, dividido por quê bê. [p=0.2] {b}A velocidade está em cima: [p=0.1] {c}dobrou a velocidade, o raio dobra. [p=0.3] {d}A curva fica duas vezes mais aberta."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}efe igual a quê vê bê seno de teta, [p=0.2] {b}o sentido sai da mão do tapa, [p=0.2] e {c}a força para o centro dá o raio. [p=0.3] Na próxima aula, {d}a mesma força num fio com corrente, [p=0.2] e {e}como ela faz um motor girar."),
    dict(id="s22", block="fim", text="{a}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {b}Bons estudos!"),
]
