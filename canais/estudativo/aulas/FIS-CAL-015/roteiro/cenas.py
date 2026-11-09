# Estudativo · FIS-CAL-015 — Carnot: o rendimento máximo (Física · Calor e Termodinâmica · Termodinâmica e máquinas térmicas).
# Habilidade: usar 1 − Tf/Tq em Kelvin para testar se uma máquina é possível.
# Pré-requisitos: FIS-CAL-014 (rendimento τ/Qq = 1 − Qf/Qq). Próxima: FIS-CAL-017 (geladeira e entropia).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Kelvin: T(K) = T(°C) + 273 (QUI-CAL-010, FIS-CAL-001). Sadi Carnot, engenheiro francês, publicou o resultado em 1824.
# O ciclo de Carnot (duas isotérmicas e duas adiabáticas) só é citado; o gráfico dele não é desenhado.

TITULO = "Carnot: o rendimento máximo"

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
    dict(id="s01", block="gancho", text="{a}Um inventor apresenta um motor novo. [p=0.2] A fonte quente dele está a {b}trezentos e vinte e sete graus Celsius; [p=0.2] a fria, a {c}vinte e sete graus. [p=0.2] Ele teria {d}rendimento de sessenta por cento. [p=0.3] {e}Dá para saber se é mentira, sem abrir o motor?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular {b}o rendimento máximo de uma máquina [p=0.2] e {c}testar se ela é possível."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}o rendimento, eta igual a um menos quê frio sobre quê quente; [p=0.2] e {c}passar de Celsius para kelvin: some duzentos e setenta e três. [p=0.3] Se faltar alguma, procure no canal."),
    # Carnot
    dict(id="s04", block="carnot", text="Em mil oitocentos e vinte e quatro, {a}o engenheiro francês Sadi Carnot [p=0.2] fez a pergunta certa: [p=0.2] {b}qual é o melhor rendimento possível entre duas fontes? [p=0.3] {c}Ele mostrou que esse máximo depende só das temperaturas das fontes. [p=0.2] {d}Não importa o combustível nem o tamanho do motor."),
    dict(id="s05", block="carnot", text="A máquina ideal, {a}a máquina de Carnot, [p=0.2] trabalha num ciclo com {b}duas isotérmicas e duas adiabáticas, [p=0.2] sem atrito e sem perdas além do quê frio. [p=0.3] Nela, {c}a razão entre os calores é igual à razão entre as temperaturas."),
    dict(id="s06", block="carnot", text="Então, {a}o rendimento máximo é um menos tê frio sobre tê quente. [p=0.3] {b}Tê frio é a temperatura da fonte fria, [p=0.1] {c}tê quente, a da fonte quente, [p=0.2] {d}as duas em kelvin. [p=0.3] {e}Nenhuma máquina real passa desse valor."),
    # exemplo
    dict(id="s07", block="exemplo", text="Vamos testar o inventor. [p=0.2] {a}Trezentos e vinte e sete mais duzentos e setenta e três: [p=0.1] {b}seiscentos kelvin. [p=0.2] {c}Vinte e sete mais duzentos e setenta e três: [p=0.1] {d}trezentos kelvin."),
    dict(id="s08", block="exemplo", text="{a}Trezentos dividido por seiscentos dá meio. [p=0.2] {b}Um menos meio: [p=0.1] {c}cinquenta por cento. [p=0.3] {d}Nem a máquina ideal passa de cinquenta. [p=0.2] {e}O motor de sessenta por cento é impossível: o inventor está errado."),
    dict(id="s09", block="exemplo", text="O teste é este: [p=0.2] {a}rendimento menor que o de Carnot, a máquina é possível. [p=0.2] {b}Maior, é impossível. [p=0.3] {c}Igual, só a máquina ideal, que não existe na prática."),
    # temperaturas
    dict(id="s10", block="temperaturas", text="A fórmula também mostra {a}como melhorar uma máquina: [p=0.2] {b}fonte quente mais quente, [p=0.1] ou {c}fonte fria mais fria. [p=0.3] {d}Cem por cento só com a fonte fria a zero kelvin, [p=0.2] {e}o zero absoluto, que não dá para atingir. [p=0.3] {f}Por isso, nenhuma máquina chega a cem por cento. [p=0.3] {g}As usinas térmicas modernas, então, trabalham com vapor cada vez mais quente."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}usar graus Celsius. [p=0.3] Com o inventor, ficaria {b}um menos vinte e sete dividido por trezentos e vinte e sete, [p=0.2] {c}cerca de noventa e dois por cento. [p=0.3] {d}E o motor de sessenta pareceria possível. [p=0.3] {e}Em Celsius, o zero não é o zero de verdade, [p=0.2] e a divisão perde o sentido."),
    # atalho
    dict(id="s12", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}escreva o rendimento máximo como a diferença sobre a quente. [p=0.3] {b}Tê quente menos tê frio, dividido por tê quente. [p=0.3] E {c}a diferença é a mesma em Celsius e em kelvin, [p=0.2] porque o duzentos e setenta e três se cancela."),
    dict(id="s13", block="atalho", text="{a}Trezentos e vinte e sete menos vinte e sete: trezentos, [p=0.2] direto dos graus Celsius. [p=0.2] {b}Só a quente vai para kelvin: seiscentos. [p=0.3] {c}Trezentos dividido por seiscentos, cinquenta por cento. [p=0.3] {d}Funciona sempre, [p=0.2] e só não compensa quando a questão já dá as duas temperaturas em kelvin."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Numa usina, a fonte quente está a {a}duzentos e vinte e sete graus Celsius, [p=0.2] e a fria, a {b}vinte e sete graus. [p=0.3] {c}Qual é o rendimento máximo? [p=0.2] E {d}um projeto com quarenta e cinco por cento é possível?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá, com o atalho. [p=0.2] {a}A diferença: duzentos e vinte e sete menos vinte e sete, duzentos. [p=0.2] {b}A quente em kelvin: duzentos e vinte e sete mais duzentos e setenta e três, quinhentos. [p=0.3] {c}Duzentos dividido por quinhentos, [p=0.1] {d}zero vírgula quatro, [p=0.1] {e}quarenta por cento."),
    dict(id="s17", block="resposta", text="{a}Quarenta e cinco é mais que quarenta: [p=0.2] {b}o projeto é impossível. [p=0.3] {c}Pela fórmula completa, dá o mesmo: [p=0.2] um menos trezentos dividido por quinhentos, [p=0.1] um menos zero vírgula seis, [p=0.1] quarenta por cento."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}o rendimento máximo é um menos tê frio sobre tê quente, [p=0.2] {b}sempre em kelvin, [p=0.2] e {c}nenhuma máquina real passa dele."),
    dict(id="s19", block="fim", text="Na próxima aula, a máquina vai {a}rodar ao contrário: [p=0.2] você vai entender {b}a geladeira [p=0.2] e {c}o que mede a entropia. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
