# Estudativo · FIS-MAG-005 — Fluxo e lei de Faraday (Física · Magnetismo · Magnetismo e indução).
# Habilidade: calcular a fem induzida com ε = ΔΦ/Δt e ε = B·L·v e dizer o que muda o fluxo.
# Pré-requisitos: FIS-MAG-004. Próxima: FIS-MAG-006.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.
# Questão inédita, criada para esta aula. Fato do gancho: Michael Faraday, 1831, ímã movido dentro de uma bobina.
# Potencial elétrico e volt (FIS-ELE-004) não estão em "Já ensinado": volt aparece só como "a unidade de tensão, de outra aula".
# O sinal de menos da lei (Lenz) fica para FIS-MAG-006: aqui, só o valor. Φ narrado "fi"; ε narrado "épsilon".

TITULO = "Fluxo e lei de Faraday"

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
    dict(id="s01", block="gancho", text="{a}Em mil oitocentos e trinta e um, Michael Faraday enfiou um ímã numa bobina de fio. [p=0.3] {b}Apareceu corrente, sem pilha nenhuma. [p=0.3] {c}Com o ímã parado lá dentro, a corrente sumiu. [p=0.3] {d}Só o movimento gerava corrente."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai saber o que é fluxo magnético, [p=0.2] {b}o que faz ele mudar [p=0.2] e {c}calcular a tensão elétrica que essa mudança cria."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, lembre {a}duas coisas. [p=0.2] {b}As linhas de campo mostram o campo bê, em tesla. [p=0.3] E {c}a área do retângulo é a base vezes a altura. [p=0.3] Se faltar alguma, procure no canal."),
    # fluxo
    dict(id="s04", block="fluxo", text="Imagine {a}uma espira, um anel de fio, [p=0.2] {b}com linhas de campo passando por dentro dela. [p=0.3] {c}O fluxo magnético mede quanto campo atravessa a espira. [p=0.3] É o fi, [p=0.1] {d}a letra grega que parece um círculo cortado."),
    dict(id="s05", block="fluxo", text="{a}Com o campo atravessando a espira de frente, [p=0.2] {b}fi igual a bê vezes á. [p=0.3] {c}Bê é o campo, em tesla, [p=0.2] e {d}á é a área da espira, em metro quadrado. [p=0.3] {e}A unidade do fluxo é o weber, [p=0.1] que é tesla vezes metro quadrado."),
    dict(id="s06", block="fluxo", text="E se a espira girar? [p=0.2] {a}Deitada ao longo das linhas, nenhuma linha passa por dentro: [p=0.2] {b}o fluxo é zero. [p=0.3] {c}Nas posições do meio, multiplique pelo cosseno do ângulo [p=0.1] entre o campo e a reta em pé sobre a espira."),
    # o que muda
    dict(id="s07", block="muda", text="Então, {a}três coisas mudam o fluxo. [p=0.2] {b}Mudar o campo, como ao aproximar o ímã. [p=0.2] {c}Mudar a área, esticando ou encolhendo a espira. [p=0.2] {d}E mudar o ângulo, girando a espira."),
    # Faraday
    dict(id="s08", block="faraday", text="Agora, a lei de Faraday. [p=0.2] {a}Quando o fluxo muda, aparece uma tensão na espira: [p=0.2] o empurrão que faz a corrente andar. [p=0.3] Ela se chama {b}força eletromotriz, [p=0.1] mas não é uma força: [p=0.2] {c}é medida em volt, a unidade de tensão, que você vê na aula de potencial elétrico."),
    dict(id="s09", block="faraday", text="O valor dela: [p=0.2] {a}épsilon igual a delta fi, dividido por delta tê. [p=0.3] {b}Delta fi é quanto o fluxo mudou, em weber, [p=0.2] e {c}delta tê é em quanto tempo, em segundo. [p=0.3] {d}Mudança rápida, tensão grande. [p=0.2] {e}Numa bobina com ene espiras, multiplique por ene."),
    dict(id="s10", block="faraday", text="Um exemplo. [p=0.2] {a}Uma espira de vinte por dez centímetros: [p=0.1] zero vírgula dois vezes zero vírgula um, [p=0.1] {b}zero vírgula zero dois metro quadrado. [p=0.3] {c}O campo cai de zero vírgula cinco tesla para zero, em zero vírgula um segundo. [p=0.3] {d}O fluxo cai zero vírgula cinco vezes zero vírgula zero dois, [p=0.1] zero vírgula zero um weber. [p=0.3] {e}Dividido por zero vírgula um: zero vírgula um volt."),
    # barra
    dict(id="s11", block="barra", text="Um caso que cai muito: {a}uma barra de metal deslizando sobre dois trilhos, [p=0.2] {b}num campo que fura a folha. [p=0.3] {c}A barra, os trilhos e o fio do fundo formam um retângulo. [p=0.2] {d}Quando a barra anda, a área do retângulo cresce, [p=0.1] e o fluxo também."),
    dict(id="s12", block="barra", text="Em cada segundo, {a}a área cresce o comprimento da barra vezes a velocidade. [p=0.3] Então, {b}épsilon igual a bê vezes éle vezes vê. [p=0.3] {c}Campo de zero vírgula cinco tesla, barra de zero vírgula quatro metro, a cinco metros por segundo: [p=0.2] {d}zero vírgula cinco vezes zero vírgula quatro dá zero vírgula dois, [p=0.1] vezes cinco, [p=0.1] {e}um volt."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que um ímã forte parado dentro da bobina gera corrente. [p=0.3] {b}O fluxo é grande, mas não muda. [p=0.2] {c}Delta fi é zero, [p=0.1] e {d}a tensão também. [p=0.3] {e}O que conta é a mudança, não o tamanho do fluxo."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova. [p=0.2] {a}Antes de qualquer conta, pergunte: o fluxo está mudando? [p=0.3] {b}Se nada muda, a resposta é zero, sem conta. [p=0.3] {c}Se é uma barra andando, use direto bê éle vê."),
    dict(id="s15", block="atalho", text="Funciona porque {a}bê éle vê é o próprio delta fi por delta tê, [p=0.2] já pronto para a barra. [p=0.3] {b}Confira pela unidade: tesla vezes metro vezes metro por segundo [p=0.1] {c}é weber por segundo, que é volt. [p=0.3] {d}Não serve quando o campo ou o ângulo também mudam: [p=0.2] aí, volte para delta fi por delta tê."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Uma bobina tem dez espiras. [p=0.2] {b}Um ímã se aproxima, e o fluxo em cada espira vai de zero vírgula zero dois para zero vírgula zero oito weber, [p=0.1] em zero vírgula dois segundo. [p=0.3] {c}Qual é a tensão induzida? [p=0.3] E mais: {d}e se o ímã parar?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Delta fi é zero vírgula zero oito menos zero vírgula zero dois: [p=0.1] {b}zero vírgula zero seis weber. [p=0.3] {c}Dividido por zero vírgula dois, [p=0.1] zero vírgula três. [p=0.2] {d}Vezes dez espiras: [p=0.1] {e}três volts."),
    dict(id="s19", block="resposta", text="{a}E com o ímã parado, o fluxo para de mudar. [p=0.2] {b}A tensão vai a zero, [p=0.1] mesmo com o ímã lá dentro."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}fi igual a bê vezes á, [p=0.2] {b}campo, área e ângulo mudam o fluxo, [p=0.2] e {c}épsilon é delta fi por delta tê. [p=0.3] Na próxima aula, {d}o sentido dessa corrente, [p=0.2] com a lei de Lenz e o freio magnético."),
    dict(id="s21", block="fim", text="{a}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {b}Bons estudos!"),
]
