# Estudativo · FIS-ELE-002 — Lei de Coulomb (Física · Eletricidade · Eletrostática).
# Habilidade: usar F = k·Q1·Q2/d² por proporção, lembrando que dobrar a distância divide a força por 4.
# Pré-requisitos: FIS-ELE-001 (carga, atração e repulsão), FIS-CIN-002 (vetores). Próxima: FIS-ELE-003.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Força e newton: FIS-DIN não está em "Já ensinado"; a FIS-CIN-001 só cita o newton
# como unidade de força, então a aula explica "força = puxão ou empurrão, em newton" na hora. Ação e reação não é citada
# pelo nome (é assunto de Dinâmica): só "as duas cargas sentem forças de mesmo tamanho e sentidos opostos".
# Coulomb publicou a lei em 1785 (século XVIII). k = 9 × 10⁹ N·m²/C² no vácuo (e praticamente no ar).

TITULO = "Lei de Coulomb"

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
    dict(id="s01", block="gancho", text="Duas cargas se atraem com uma força de {a}trinta e seis newtons. [p=0.3] Você {b}dobra a distância entre elas. [p=0.2] Quanto vira a força? [p=0.3] Muita gente responde {c}dezoito. [p=0.3] {d}Errado: vira nove."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai usar a lei de Coulomb [p=0.2] {b}por proporção, [p=0.2] e acertar essa conta {c}quase sem fazer conta."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}cargas de mesmo sinal se repelem, e de sinais opostos se atraem; [p=0.3] e {c}o micro, que vale dez elevado a menos seis. [p=0.3] Se faltar alguma, procure no canal."),
    # a força
    dict(id="s04", block="forca", text="Essa atração ou repulsão é uma {a}força: [p=0.1] um puxão ou um empurrão. [p=0.3] Força se mede em {b}newton, com a letra ene maiúscula. [p=0.3] E ela é um vetor: [p=0.1] {c}aponta ao longo da linha que liga as duas cargas."),
    dict(id="s05", block="forca", text="{a}As duas cargas sentem forças do mesmo tamanho, [p=0.2] {b}em sentidos opostos. [p=0.3] Mesmo que uma carga seja bem maior, [p=0.2] {c}a força na pequena é igual à força na grande."),
    # a fórmula
    dict(id="s06", block="formula", text="Quem mediu essa força foi o francês Charles Coulomb, no século dezoito. [p=0.3] {a}Efe igual a cá vezes quê um vezes quê dois, dividido por dê ao quadrado. [p=0.3] {b}Efe é a força, em newton. [p=0.2] {c}Quê um e quê dois são as cargas, em coulomb. [p=0.2] {d}Dê é a distância entre elas, em metro."),
    dict(id="s07", block="formula", text="{a}Cá é uma constante: no vácuo, o espaço sem ar, e também no ar, vale nove vezes dez elevado a nove, [p=0.2] em newton vezes metro quadrado por coulomb ao quadrado. [p=0.3] {b}Na conta, use as cargas sem o sinal. [p=0.2] O sinal só diz {c}se elas se atraem ou se repelem."),
    dict(id="s08", block="formula", text="Duas cargas de {a}dois e de três microcoulombs estão a {b}três metros uma da outra. [p=0.3] {c}Em cima: nove vezes dois vezes três, cinquenta e quatro. [p=0.2] {d}Nos expoentes, nove menos seis menos seis, menos três. [p=0.3] {e}Embaixo, três ao quadrado, nove. [p=0.2] {f}Cinquenta e quatro dividido por nove, seis: [p=0.1] {g}seis vezes dez elevado a menos três newton."),
    # proporção
    dict(id="s09", block="proporcao", text="Agora, o que mais cai na prova: [p=0.2] {a}a proporção. [p=0.2] A força é {b}diretamente proporcional a cada carga: [p=0.2] {c}dobrou uma carga, a força dobra. [p=0.3] E é {d}inversamente proporcional ao quadrado da distância."),
    dict(id="s10", block="proporcao", text="{a}Dobrou a distância? [p=0.2] Dois ao quadrado é quatro: [p=0.1] {b}a força fica quatro vezes menor. [p=0.3] {c}Triplicou? [p=0.1] Três ao quadrado, nove: [p=0.1] {d}nove vezes menor. [p=0.3] {e}A distância caiu pela metade? [p=0.1] {f}A força fica quatro vezes maior."),
    dict(id="s11", block="proporcao", text="Por isso, no começo da aula, {a}trinta e seis newtons [p=0.1] {b}divididos por quatro [p=0.1] {c}dão nove."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}esquecer o quadrado. [p=0.3] A pessoa pensa: dobrou a distância, a força cai pela metade, [p=0.2] e responde {b}dezoito. [p=0.3] Mas a distância está {c}ao quadrado na fórmula. [p=0.2] {d}Dobrar a distância divide a força por quatro, não por dois."),
    # atalho
    dict(id="s13", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}não refaça a conta inteira. [p=0.3] {b}Multiplique a força pelo que mudou nas cargas, [p=0.2] e {c}divida pelo quadrado do que mudou na distância. [p=0.3] {d}Uma carga vezes dois e a distância vezes três? [p=0.2] {e}A força vai vezes dois, dividido por nove."),
    dict(id="s14", block="atalho", text="Funciona porque {a}cá não muda, [p=0.2] e o resto da fórmula é só multiplicação e divisão. [p=0.3] {b}Não compensa quando a questão não dá uma força de partida: [p=0.2] aí, use a fórmula inteira."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Duas cargas se repelem com {a}quarenta e cinco newtons. [p=0.3] {b}Uma das cargas triplica, [p=0.2] e {c}a distância entre elas também triplica. [p=0.3] {d}Qual é a nova força?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] {a}A carga triplicou: vezes três. [p=0.2] {b}A distância triplicou: dividido por três ao quadrado, nove. [p=0.3] {c}Quarenta e cinco vezes três, cento e trinta e cinco, [p=0.2] {d}dividido por nove: [p=0.1] {e}quinze newtons. [p=0.3] Mais rápido ainda: {f}três nonos é um terço, [p=0.1] e um terço de quarenta e cinco é quinze."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}a força é cá vezes quê um vezes quê dois, dividido por dê ao quadrado; [p=0.2] {b}ela cresce na mesma proporção das cargas; [p=0.2] e {c}dobrar a distância divide a força por quatro."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai ver {a}o campo elétrico, [p=0.2] a região em volta de uma carga onde outra carga sente força, [p=0.2] e {b}as linhas que desenham esse campo. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
