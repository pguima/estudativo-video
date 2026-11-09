# Estudativo · FIS-ELE-021 — Circuito simples: lei de Pouillet (Física · Eletricidade · Geradores e receptores).
# Habilidade: achar a corrente com i = ε/(R + r) e a condição de potência máxima.
# Pré-requisitos: FIS-ELE-020 (U = ε − r·i, corrente de curto, rendimento U/ε), FIS-ELE-013 (associação mista). Próxima: FIS-ELE-022.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Pouillet sai de R·i = ε − r·i com fator comum (MAT-FAT-002). Potência máxima pela simetria da parábola (MAT-FUN-016):
# Pu = ε·i − r·i² zera em i = 0 e em i_cc = ε/r; o topo fica em i_cc/2, onde U = ε/2 e R = r. Pmax = (ε/2)·(i_cc/2) = ε²/(4r).
# Contas: 12/(5 + 1) = 2 A; U = 5·2 = 10 V; 12/5 = 2,4 (erro do gancho); 10 ∥ 10 = 5 Ω.
#   ε = 12, r = 2: R = 1 → 4 A, 16 W; R = 2 → 3 A, 18 W; R = 4 → 2 A, 16 W; i_cc = 6 A; 144/8 = 18 W.
#   Questão: 12·6/(12 + 6) = 72/18 = 4 Ω; 24/(4 + 2) = 4 A; 24² = 576; 576/8 = 72 W.

TITULO = "Circuito simples: lei de Pouillet"

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
    dict(id="s01", block="gancho", text="{a}Uma bateria de doze volts, ligada a um resistor de cinco ohms. [p=0.2] {b}Doze dividido por cinco, dois vírgula quatro ampères? [p=0.3] {c}Não: passam só dois. [p=0.2] {d}Faltou a resistência que fica dentro da bateria: um ohm."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai achar a corrente de um circuito com uma fração só, [p=0.2] e {b}descobrir qual resistor recebe a maior potência."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}nos polos do gerador, u igual a épsilon menos erre pequeno vezes i; [p=0.2] e {c}reduzir resistores em série e em paralelo até um só. [p=0.3] Se faltar alguma, procure no canal."),
    # a lei
    dict(id="s04", block="lei", text="Ligue {a}o gerador a um resistor, erre grande. [p=0.2] {b}A tensão nos polos do gerador é a mesma tensão do resistor. [p=0.3] {c}Para o gerador, ela é épsilon menos erre pequeno vezes i; [p=0.2] {d}para o resistor, erre grande vezes i."),
    dict(id="s05", block="lei", text="{a}Iguale as duas: [p=0.1] erre grande vezes i é igual a épsilon menos erre pequeno vezes i. [p=0.3] {b}Passe o erre pequeno vezes i para o outro lado, [p=0.1] {c}coloque o i em evidência, [p=0.2] e sai {d}a lei de Pouillet: [p=0.1] {e}i igual a épsilon dividido por erre grande mais erre pequeno."),
    dict(id="s06", block="lei", text="{a}Leia assim: a força eletromotriz empurra a corrente {b}por todas as resistências da volta, [p=0.1] {c}a de fora e a de dentro, em série."),
    # exemplos
    dict(id="s07", block="exemplo", text="No gancho: {a}doze dividido por cinco mais um, [p=0.1] {b}doze dividido por seis, [p=0.1] {c}dois ampères. [p=0.3] {d}Nos polos, erre grande vezes i: [p=0.1] cinco vezes dois, {e}dez volts."),
    dict(id="s08", block="exemplo", text="{a}Com vários resistores fora, reduza primeiro. [p=0.2] {b}Dois resistores de dez ohms em paralelo: [p=0.1] {c}dez dividido por dois, cinco ohms. [p=0.2] {d}Aí, é o mesmo circuito: dois ampères."),
    # potência máxima
    dict(id="s09", block="maxima", text="Agora, a potência que chega ao resistor de fora: [p=0.2] {a}a potência útil do gerador. [p=0.3] Pegue {b}um gerador de doze volts e dois ohms internos, [p=0.1] e {c}troque o resistor de fora."),
    dict(id="s10", block="maxima", text="{a}Com um ohm fora: [p=0.1] a corrente é quatro ampères, [p=0.1] e a potência, um ohm vezes quatro ao quadrado: dezesseis watts. [p=0.3] {b}Com dois ohms: [p=0.1] três ampères, [p=0.1] dois ohms vezes nove: dezoito watts. [p=0.3] {c}Com quatro ohms: [p=0.1] dois ampères, [p=0.1] quatro ohms vezes quatro: dezesseis watts de novo."),
    dict(id="s11", block="maxima", text="{a}O máximo veio no meio, [p=0.2] {b}quando a resistência de fora é igual à de dentro. [p=0.3] {c}Erre grande igual a erre pequeno: [p=0.1] {d}é a condição de potência máxima."),
    dict(id="s12", block="parabola", text="Por quê? [p=0.2] {a}A potência útil é u vezes i: [p=0.1] {b}épsilon vezes i, menos erre pequeno vezes i ao quadrado. [p=0.3] {c}É uma parábola de boca para baixo, [p=0.1] {d}que vale zero sem corrente e na corrente de curto. [p=0.3] {e}A parábola é simétrica: o topo fica no meio, [p=0.1] {f}na metade da corrente de curto."),
    dict(id="s13", block="parabola", text="{a}Com metade da corrente de curto, [p=0.1] {b}a perda interna é metade de épsilon, [p=0.1] {c}e os polos ficam com a outra metade. [p=0.3] {d}Por isso, na potência máxima, o rendimento é cinquenta por cento."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que um resistor menor sempre recebe mais potência. [p=0.3] {b}Com um ohm, a corrente subiu, mas a potência caiu para dezesseis watts. [p=0.2] {c}Abaixo de erre pequeno, a maior parte da tensão se perde dentro do gerador."),
    # atalho
    dict(id="s15", block="atalho", text="Agora, o atalho da potência máxima: [p=0.2] {a}erre grande igual a erre pequeno, [p=0.1] {b}u igual a metade de épsilon, [p=0.2] {c}e a potência máxima é metade de épsilon vezes metade da corrente de curto: [p=0.1] {d}épsilon ao quadrado dividido por quatro erre pequeno. [p=0.3] {e}Doze ao quadrado, cento e quarenta e quatro, dividido por oito: [p=0.1] {f}dezoito watts, sem tabela."),
    dict(id="s16", block="atalho", text="Funciona porque {a}é o topo da parábola, já calculado. [p=0.2] {b}Mas potência máxima não é rendimento máximo: [p=0.1] {c}metade da energia vira calor no gerador. [p=0.3] {d}Se a questão pedir o maior rendimento, o atalho não serve."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Um gerador de vinte e quatro volts, com dois ohms internos, [p=0.1] alimenta {b}doze ohms e seis ohms em paralelo. [p=0.3] {c}Qual é a corrente no gerador? [p=0.2] {d}E qual resistor de fora daria a potência máxima, e de quanto?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}Paralelo, produto pela soma: setenta e dois dividido por dezoito, [p=0.1] {b}quatro ohms. [p=0.3] {c}Pouillet: vinte e quatro dividido por quatro mais dois, [p=0.1] {d}quatro ampères."),
    dict(id="s20", block="resposta", text="{a}Potência máxima com o resistor de fora igual a dois ohms. [p=0.2] {b}Vinte e quatro ao quadrado, quinhentos e setenta e seis, [p=0.1] dividido por quatro vezes dois, oito: [p=0.1] {c}setenta e dois watts."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: {a}a corrente é épsilon dividido pela soma de todas as resistências da volta; [p=0.2] {b}e a potência máxima sai com a resistência de fora igual à de dentro, [p=0.1] com rendimento de cinquenta por cento."),
    dict(id="s22", block="fim", text="Na próxima aula, {a}o motor, que recebe energia elétrica e devolve movimento, [p=0.2] e {b}o que acontece quando você junta várias pilhas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
