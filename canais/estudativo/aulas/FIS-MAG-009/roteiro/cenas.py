# Estudativo · FIS-MAG-009 — Como uma usina gera eletricidade (Física · Magnetismo · Usinas e matriz elétrica).
# Habilidade: seguir a cadeia de energia em hidrelétrica, termelétrica e nuclear até o gerador, tratando o reator só como
# fonte de calor, com o aviso de que fissão vem depois, e calcular a potência de uma queda d'água.
# Pré-requisitos: FIS-MAG-005, FIS-ENE-002, FIS-ENE-005, FIS-CAL-014. Próxima: FIS-MAG-010.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Lenz, transformador e potencial elétrico (FIS-MAG-006, 007, FIS-ELE-004) não estão
# em "Já ensinado": a aula não fala de volt nem de transformador. P = d·Z·g·h com d da água = 1.000 kg/m³ e g = 10 m/s².

TITULO = "Como uma usina gera eletricidade"

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
    dict(id="s01", block="gancho", text="{a}Hidrelétrica, {b}termelétrica {c}e usina nuclear parecem muito diferentes. [p=0.3] Mas, lá dentro, {d}as três terminam na mesma máquina: [p=0.2] {e}um eixo girando num gerador."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai seguir o caminho da energia em cada usina [p=0.2] e {b}calcular a potência de uma queda d'água."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre {a}duas coisas. [p=0.2] {b}Fluxo mudando numa bobina cria corrente, pela lei de Faraday. [p=0.3] E {c}potência é energia dividida pelo tempo, em watt, [p=0.1] e rendimento é a parte útil dividida pelo total. [p=0.3] Se faltar alguma, procure no canal."),
    # gerador
    dict(id="s04", block="gerador", text="Comece pelo gerador. [p=0.2] {a}É um ímã que gira dentro de bobinas, [p=0.2] preso num eixo. [p=0.3] {b}Girando, o ímã muda o fluxo nas bobinas o tempo todo, [p=0.2] e {c}aparece corrente, pela lei de Faraday. [p=0.3] {d}O norte e o sul do ímã passam, um depois do outro, pela bobina, [p=0.1] e a corrente vai e volta: [p=0.1] é alternada."),
    dict(id="s05", block="gerador", text="{a}É o motor elétrico ao contrário. [p=0.2] {b}No motor, a corrente faz girar. [p=0.2] {c}No gerador, o giro faz a corrente. [p=0.3] {d}Então, toda usina dessas só precisa de uma coisa: [p=0.2] {e}algo que empurre uma turbina, uma roda com pás, ligada ao eixo."),
    # hidrelétrica
    dict(id="s06", block="hidro", text="{a}Na hidrelétrica, quem empurra é a água. [p=0.2] {b}Parada lá no alto da represa, ela tem energia potencial gravitacional. [p=0.3] {c}Descendo pelo tubo, ela ganha velocidade: [p=0.1] energia cinética. [p=0.3] {d}A água bate nas pás e gira a turbina, [p=0.2] e {e}o gerador transforma esse giro em energia elétrica."),
    # termelétrica
    dict(id="s07", block="termo", text="{a}Na termelétrica, quem empurra é o vapor. [p=0.2] {b}Queima-se carvão, gás ou bagaço de cana: [p=0.2] a energia química vira calor. [p=0.3] {c}O calor ferve a água, [p=0.2] e {d}o vapor sai com força e gira a turbina. [p=0.3] {e}Depois, o vapor é resfriado, vira água e volta para ferver de novo."),
    dict(id="s08", block="termo", text="A termelétrica é {a}uma máquina térmica. [p=0.2] Pela segunda lei, {b}nenhuma máquina transforma todo o calor em trabalho: [p=0.2] {c}uma boa parte sempre sai para o ambiente, [p=0.1] na água de resfriamento. [p=0.3] {d}Por isso, o rendimento fica bem abaixo de cem por cento."),
    # nuclear
    dict(id="s09", block="nuclear", text="{a}E a usina nuclear? [p=0.2] {b}Ela é uma termelétrica. [p=0.3] {c}O reator faz o papel do fogo: [p=0.2] {d}ele só aquece a água. [p=0.3] {e}Daí em diante, é igual: vapor, turbina e gerador. [p=0.3] {f}Como o reator produz esse calor é assunto de outra aula, a da fissão nuclear."),
    # potência
    dict(id="s10", block="queda", text="Agora, a conta que mais cai: [p=0.2] {a}a potência de uma queda d'água. [p=0.3] {b}Uma massa eme que desce uma altura agá libera a energia potencial: eme gê agá. [p=0.3] {c}Em cada segundo, desce uma massa de água igual à densidade vezes a vazão, [p=0.2] que é o volume por segundo."),
    dict(id="s11", block="queda", text="Junte tudo: [p=0.2] {a}pê igual a dê, vezes zê, vezes gê, vezes agá. [p=0.3] {b}Dê é a densidade da água, mil quilogramas por metro cúbico. [p=0.2] {c}Zê é a vazão, em metro cúbico por segundo. [p=0.2] {d}Gê é a gravidade, dez metros por segundo ao quadrado. [p=0.2] {e}E agá é a altura da queda, em metro. [p=0.3] {f}A potência sai em watt."),
    dict(id="s12", block="queda", text="Um exemplo. [p=0.2] {a}Vazão de cem metros cúbicos por segundo, [p=0.1] queda de cinquenta metros. [p=0.3] {b}Mil vezes cem vezes dez vezes cinquenta: [p=0.2] {c}cinquenta milhões de watts, [p=0.1] cinquenta megawatts. [p=0.3] {d}Com rendimento de noventa por cento, [p=0.1] {e}saem quarenta e cinco megawatts de energia elétrica."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que a usina nuclear tira eletricidade direto do átomo. [p=0.3] {b}O núcleo do átomo só dá calor. [p=0.2] {c}Quem gera a eletricidade é o mesmo conjunto de sempre: [p=0.1] {d}vapor, turbina e gerador. [p=0.3] {e}Na prova, a cadeia da nuclear é quase igual à da termelétrica a carvão."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova. [p=0.2] Para a água, {a}densidade vezes gravidade dá mil vezes dez: [p=0.1] {b}dez mil. [p=0.3] Então, {c}a potência, em watt, é dez mil vezes a vazão vezes a altura. [p=0.3] {d}Cem metros cúbicos por segundo e cinquenta metros: [p=0.1] {e}dez mil vezes cinco mil, cinquenta milhões de watts, na hora."),
    dict(id="s15", block="atalho", text="Funciona porque {a}dê vezes gê é sempre o mesmo número para a água. [p=0.3] {b}Não serve se a questão usar gravidade de nove vírgula oito, [p=0.2] ou {c}outro líquido."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Uma pequena hidrelétrica tem vazão de vinte metros cúbicos por segundo [p=0.1] e queda de trinta metros. [p=0.3] {b}O rendimento é de noventa por cento. [p=0.3] {c}Qual é a potência elétrica?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Vinte vezes trinta, seiscentos. [p=0.2] {b}Dez mil vezes seiscentos: [p=0.1] {c}seis milhões de watts, seis megawatts. [p=0.3] {d}Noventa por cento disso: [p=0.1] {e}cinco vírgula quatro megawatts."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: {a}toda usina dessas gira uma turbina presa a um gerador, [p=0.2] {b}a nuclear é uma termelétrica, [p=0.2] e {c}a potência da queda é dê zê gê agá. [p=0.3] Na próxima aula, {d}o vento e o sol, [p=0.2] e por que eles não geram o tempo todo."),
    dict(id="s20", block="fim", text="{a}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {b}Bons estudos!"),
]
