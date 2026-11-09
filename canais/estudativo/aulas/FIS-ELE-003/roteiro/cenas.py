# Estudativo · FIS-ELE-003 — Campo elétrico e linhas de força (Física · Eletricidade · Eletrostática).
# Habilidade: calcular E = F/q e E = k·Q/d² e ler as linhas de força, inclusive no campo uniforme.
# Pré-requisitos: FIS-ELE-002 (lei de Coulomb). Próxima: FIS-ELE-004.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. F = q·E sai de isolar a letra (MAT-EQU-011, em "Já ensinado").
# Contas: 8e-3/2e-6 = 4e3 N/C; 9e9·4e-6/2² = 9e3 N/C; questão: 9e9·2e-6/3² = 2e3 N/C e F = 1e-6·2e3 = 2e-3 N.

TITULO = "Campo elétrico e linhas de força"

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
    dict(id="s01", block="gancho", text="{a}Uma carga sente a força de outra sem encostar nela. [p=0.3] {b}Como ela sabe que a outra está ali? [p=0.3] A resposta da Física é {c}o campo elétrico."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular o campo {b}de dois jeitos [p=0.2] e {c}ler as linhas de força, [p=0.1] inclusive no campo uniforme."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa da {a}lei de Coulomb: [p=0.2] {b}a força é cá vezes quê um vezes quê dois, dividido por dê ao quadrado, [p=0.2] {c}com cá igual a nove vezes dez elevado a nove. [p=0.3] Se faltar, procure no canal."),
    # o campo
    dict(id="s04", block="campo", text="Toda carga muda o espaço em volta dela. [p=0.2] Esse espaço modificado é o {a}campo elétrico. [p=0.3] Ponha ali uma {b}carga pequena de teste, o quê minúsculo, [p=0.2] e ela {c}sente uma força."),
    dict(id="s05", block="campo", text="O campo é {a}a força dividida pela carga de teste: [p=0.2] {b}Ê igual a efe dividido por quê. [p=0.3] {c}Ê maiúsculo é o campo, em newton por coulomb; [p=0.2] {d}efe é a força, em newton; [p=0.2] {e}quê é a carga de teste, em coulomb. [p=0.3] O campo diz {f}quantos newtons cada coulomb sente naquele ponto."),
    dict(id="s06", block="campo", text="Uma carga de teste de {a}dois microcoulombs sente {b}oito vezes dez elevado a menos três newton. [p=0.3] {c}Oito dividido por dois, quatro. [p=0.2] {d}Dividir por dez elevado a menos seis é multiplicar por dez elevado a seis: [p=0.1] menos três mais seis, três. [p=0.2] {e}O campo é quatro vezes dez ao cubo newtons por coulomb."),
    # campo de uma carga
    dict(id="s07", block="carga", text="Dá para calcular o campo direto da carga que o cria. [p=0.2] {a}Troque a força pela lei de Coulomb: [p=0.1] uma das cargas é o próprio quê de teste. [p=0.2] Divida por quê, e {b}o quê de cima corta com o de baixo. [p=0.3] Fica {c}ê igual a cá vezes Q, dividido por dê ao quadrado. [p=0.3] {d}Q maiúsculo é a carga que cria o campo, [p=0.1] e {e}dê é a distância até o ponto."),
    dict(id="s08", block="carga", text="Uma carga de {a}quatro microcoulombs, a {b}dois metros: [p=0.2] {c}nove vezes quatro, trinta e seis, [p=0.1] e nos expoentes, nove menos seis, três. [p=0.2] {d}Dividido por dois ao quadrado, quatro: [p=0.2] {e}nove vezes dez ao cubo newtons por coulomb."),
    dict(id="s09", block="carga", text="O campo é um vetor, e o sentido segue uma regra: [p=0.2] {a}a carga positiva cria campo apontando para longe dela, [p=0.2] {b}a negativa, apontando para ela. [p=0.3] Numa carga de teste positiva, {c}a força tem o sentido do campo; [p=0.2] {d}numa negativa, o sentido oposto."),
    # linhas de força
    dict(id="s10", block="linhas", text="Para desenhar o campo, usamos {a}linhas de força. [p=0.2] {b}Elas saem das cargas positivas e chegam nas negativas. [p=0.3] {c}Em cada ponto, o campo segue a linha, no sentido da seta. [p=0.3] {d}Onde as linhas ficam mais juntas, o campo é mais forte. [p=0.2] E {e}elas nunca se cruzam: [p=0.1] o campo teria duas direções no mesmo ponto."),
    dict(id="s11", block="linhas", text="Um caso especial: {a}duas placas paralelas, uma positiva e outra negativa. [p=0.3] Entre elas, {b}as linhas são retas, paralelas e igualmente espaçadas. [p=0.3] É o {c}campo uniforme: [p=0.1] {d}o mesmo valor, a mesma direção e o mesmo sentido em todos os pontos."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que o campo depende da carga de teste. [p=0.3] {b}Troque a carga de teste por uma com o dobro: [p=0.2] {c}a força dobra, [p=0.1] {d}mas o campo continua o mesmo, [p=0.2] porque ele é a força dividida pela carga. [p=0.3] {e}O campo depende só de quem o cria e da distância."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}o campo de uma carga segue a mesma proporção da lei de Coulomb. [p=0.3] {b}Distância dobrada, campo dividido por quatro. [p=0.2] {c}Distância triplicada, por nove. [p=0.3] E se a questão der o campo e pedir a força, {d}efe é quê vezes ê."),
    dict(id="s14", block="atalho", text="Funciona porque {a}o dê ao quadrado fica embaixo, como na lei de Coulomb. [p=0.3] {b}Não vale no campo uniforme: [p=0.2] lá, o campo é igual em todo ponto, [p=0.1] e a distância não muda nada."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Uma carga de {a}dois microcoulombs cria um campo. [p=0.2] {b}Quanto vale o campo a três metros dela? [p=0.3] {c}E qual é a força numa carga de menos um microcoulomb posta ali: [p=0.2] {d}o valor e o sentido?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}Ê igual a cá vezes Q, dividido por dê ao quadrado. [p=0.2] {b}Nove vezes dois, dezoito, [p=0.1] e nos expoentes, nove menos seis, três. [p=0.2] {c}Dividido por três ao quadrado, nove: [p=0.1] {d}dois vezes dez ao cubo newtons por coulomb."),
    dict(id="s18", block="resposta", text="A força: {a}efe é quê vezes ê. [p=0.2] {b}Um vezes dez elevado a menos seis, vezes dois vezes dez ao cubo: [p=0.2] {c}dois vezes dez elevado a menos três newton. [p=0.3] A carga é negativa, então {d}a força é contrária ao campo: [p=0.2] {e}aponta para a carga que cria o campo. [p=0.2] Faz sentido: sinais opostos se atraem."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}o campo é a força dividida pela carga de teste; [p=0.2] {b}o campo de uma carga é cá vezes Q, dividido por dê ao quadrado; [p=0.2] e {c}as linhas saem do positivo, entram no negativo e ficam juntas onde o campo é forte."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai ver {a}o potencial elétrico [p=0.2] e {b}o trabalho para levar uma carga de um ponto a outro. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
