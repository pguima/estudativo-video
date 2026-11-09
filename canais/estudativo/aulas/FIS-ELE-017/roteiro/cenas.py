# Estudativo · FIS-ELE-017 — Potência elétrica e efeito Joule (Física · Eletricidade · Potência elétrica e conta de luz).
# Habilidade: usar P = U·i, P = R·i² e P = U²/R e escolher a fórmula pelo que é constante.
# Pré-requisitos: FIS-ELE-009 (U = R·i), FIS-ENE-002 (P = τ/Δt, watt). Próxima: FIS-ELE-018.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# FIS-ELE-010 a 016 (segunda lei, série, paralelo, curto, fusível) NÃO estão em "Já ensinado": a aula não usa associação.
# P = U·i sai de τ = q·U (FIS-ELE-004) e i = Q/Δt (FIS-ELE-008). Resistência tratada como constante (aviso no atalho).
# Contas: 4.400/220 = 20 A; 220/20 = 11 Ω; 11·20² = 11·400 = 4.400; 220² = 48.400; 48.400/11 = 4.400.
#   Erro: 20²/10 = 40 W; 20²/20 = 20 W. Atalho: 100 W em 220 V → 110 V: 100/4 = 25 W.
#   Questão: 1.100/220 = 5 A; 220/5 = 44 Ω; 1.100/4 = 275 W; 110² = 12.100; 12.100/44 = 275.

TITULO = "Potência elétrica e efeito Joule"

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
    dict(id="s01", block="gancho", text="{a}Na etiqueta de um chuveiro está escrito: [p=0.1] {b}duzentos e vinte volts, [p=0.1] {c}quatro mil e quatrocentos watts. [p=0.3] {d}Só com esses dois números, dá para saber a corrente que passa nele [p=0.1] e {e}a resistência dele."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai usar as três fórmulas da potência elétrica [p=0.2] e {b}escolher a certa pelo que não muda."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}três coisas: [p=0.2] {b}potência é energia dividida pelo tempo, em watt; [p=0.2] {c}a energia de uma carga que atravessa uma tensão é a carga vezes a tensão; [p=0.2] e {d}a tensão é a resistência vezes a corrente. [p=0.3] Se faltar alguma, procure no canal."),
    # P = U·i
    dict(id="s04", block="pui", text="De onde vem a potência elétrica? [p=0.2] {a}A energia que as cargas trocam é a carga vezes a tensão. [p=0.3] {b}Divida pelo tempo, para ter a potência. [p=0.2] {c}E a carga dividida pelo tempo é a corrente. [p=0.3] Sobra {d}pê igual a u vezes i: [p=0.2] {e}potência é tensão vezes corrente. [p=0.2] {f}Volt vezes ampère dá watt."),
    dict(id="s05", block="pui", text="De volta ao chuveiro. [p=0.2] {a}Quatro mil e quatrocentos é igual a duzentos e vinte vezes a corrente. [p=0.2] {b}A corrente é quatro mil e quatrocentos dividido por duzentos e vinte: [p=0.1] {c}vinte ampères. [p=0.3] {d}E a resistência, pela lei de Ohm: [p=0.1] duzentos e vinte dividido por vinte, {e}onze ohms."),
    # efeito Joule
    dict(id="s06", block="joule", text="{a}No chuveiro, essa energia vira calor. [p=0.2] É o {b}efeito Joule: [p=0.1] {c}a corrente esquenta tudo o que tem resistência. [p=0.3] {d}Ferro de passar, torradeira, secador de cabelo: [p=0.1] todos aquecem pelo efeito Joule. [p=0.2] E {e}é por isso que uma lâmpada antiga, de filamento, fica tão quente."),
    dict(id="s07", block="joule", text="Num resistor, troque a tensão por erre vezes i: [p=0.2] {a}pê igual a erre vezes i ao quadrado. [p=0.3] Ou troque a corrente por u dividido por erre: [p=0.2] {b}pê igual a u ao quadrado, dividido por erre. [p=0.3] {c}É a mesma potência, escrita de três jeitos."),
    dict(id="s08", block="joule", text="Confira no chuveiro. [p=0.2] {a}Onze vezes vinte ao quadrado: [p=0.1] onze vezes quatrocentos, {b}quatro mil e quatrocentos. [p=0.3] {c}Duzentos e vinte ao quadrado, quarenta e oito mil e quatrocentos, [p=0.1] dividido por onze: {d}quatro mil e quatrocentos de novo."),
    # escolher
    dict(id="s09", block="escolher", text="Qual usar? [p=0.2] {a}Escolha pelo que não muda. [p=0.3] {b}Resistores com a mesma corrente, um atrás do outro no mesmo fio: [p=0.1] use erre vezes i ao quadrado, [p=0.1] e {c}a maior resistência esquenta mais. [p=0.3] {d}Resistores com a mesma tensão, como na tomada: [p=0.1] use u ao quadrado dividido por erre, [p=0.1] e {e}a menor resistência esquenta mais."),
    # erro
    dict(id="s10", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que mais resistência sempre esquenta mais. [p=0.3] Ligue, um de cada vez, {b}um resistor de dez ohms e outro de vinte ohms [p=0.1] numa fonte de {c}vinte volts."),
    dict(id="s11", block="erro", text="{a}No de dez: vinte ao quadrado, quatrocentos, dividido por dez: quarenta watts. [p=0.2] {b}No de vinte: quatrocentos dividido por vinte, vinte watts. [p=0.3] {c}Com a tensão fixa, a menor resistência deixa passar mais corrente, [p=0.1] e {d}esquenta mais."),
    # atalho
    dict(id="s12", block="atalho", text="Agora, o atalho: [p=0.2] {a}o mesmo aparelho, ligado numa tensão diferente. [p=0.3] Uma lâmpada de {b}cem watts, feita para duzentos e vinte volts, [p=0.1] é ligada em {c}cento e dez. [p=0.3] {d}A resistência dela não muda: use u ao quadrado dividido por erre. [p=0.2] {e}Tensão pela metade, potência dividida por dois ao quadrado, quatro. [p=0.2] {f}Vinte e cinco watts."),
    dict(id="s13", block="atalho", text="Funciona porque {a}a tensão está em cima e ao quadrado, e a resistência fica fixa: [p=0.2] {b}o fator da tensão vai ao quadrado. [p=0.3] {c}Não vale se a questão disser que a resistência muda com o aquecimento: [p=0.2] aí, use os valores que ela der."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Um ferro de passar tem na etiqueta {a}mil e cem watts e duzentos e vinte volts. [p=0.3] {b}Qual é a corrente, [p=0.1] {c}qual é a resistência, [p=0.2] e {d}qual seria a potência dele ligado em cento e dez volts?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Corrente: mil e cem dividido por duzentos e vinte, [p=0.1] {b}cinco ampères. [p=0.2] {c}Resistência: duzentos e vinte dividido por cinco, [p=0.1] {d}quarenta e quatro ohms."),
    dict(id="s17", block="resposta", text="{a}Em cento e dez volts, a tensão cai pela metade, [p=0.1] e a potência cai para um quarto: [p=0.2] {b}mil e cem dividido por quatro, [p=0.1] {c}duzentos e setenta e cinco watts. [p=0.3] {d}Confira: cento e dez ao quadrado, doze mil e cem, [p=0.1] dividido por quarenta e quatro: duzentos e setenta e cinco. [p=0.3] {e}Quem dividiu só por dois achou quinhentos e cinquenta: esqueceu o quadrado."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}pê igual a u vezes i, em qualquer aparelho; [p=0.2] {b}num resistor, também erre vezes i ao quadrado [p=0.1] e u ao quadrado dividido por erre; [p=0.2] e {c}escolha a fórmula pelo que não muda."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai transformar potência e tempo em {a}quilowatt-hora [p=0.2] e calcular {b}quanto cada aparelho pesa na conta de luz. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
