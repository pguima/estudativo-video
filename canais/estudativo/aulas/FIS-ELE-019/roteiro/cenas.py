# Estudativo · FIS-ELE-019 — Chuveiro, lâmpadas e tomada (Física · Eletricidade · Potência elétrica e conta de luz).
# Habilidade: explicar por que o chuveiro no inverno tem menor resistência e prever o brilho de lâmpadas em série e em paralelo.
# Pré-requisitos: FIS-ELE-017 (P = U·i, R·i², U²/R; escolher pelo que é constante), FIS-ELE-012 (paralelo). Próxima: FIS-ELE-020.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# FIS-ELE-010 (segunda lei de Ohm), 013, 014 (casa em paralelo, disjuntor) e 018 (kWh) NÃO estão em "Já ensinado": o pedaço
# menor do fio no inverno é citado como assunto da segunda lei. Brilho = potência dissipada de verdade (lâmpada como resistor fixo).
# Contas: 220² = 48.400; 48.400/22 = 2.200 W; 48.400/11 = 4.400 W. Etiquetas 220 V: R100 = 484 Ω, R25 = 1.936 Ω (4×).
#   Série: 2.420 Ω, i = 1/11 A; U25 = 176 V, U100 = 44 V; P25 = 16 W, P100 = 4 W. Questão: R40 = 1.210 Ω; 1.210/484 = 100/40 = 2,5.

TITULO = "Chuveiro, lâmpadas e tomada"

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
    dict(id="s01", block="gancho", text="{a}No inverno, você gira a chave do chuveiro para a posição quente. [p=0.2] Parece lógico que, para esquentar mais, {b}a resistência aumente. [p=0.3] {c}É o contrário: [p=0.2] {d}no inverno, a resistência do chuveiro é menor."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai explicar o chuveiro [p=0.2] e {b}prever qual lâmpada brilha mais, [p=0.1] em série e em paralelo."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}as fórmulas da potência, pê igual a erre vezes i ao quadrado e pê igual a u ao quadrado dividido por erre; [p=0.2] e {c}que em série a corrente é a mesma, e em paralelo, a tensão. [p=0.3] Se faltar alguma, procure no canal."),
    # tomada e chuveiro
    dict(id="s04", block="chuveiro", text="Comece pela tomada. [p=0.2] {a}Ela entrega sempre a mesma tensão, [p=0.1] {b}duzentos e vinte volts, por exemplo, [p=0.1] seja qual for o aparelho. [p=0.3] {c}Com a tensão fixa, a fórmula certa é pê igual a u ao quadrado dividido por erre. [p=0.2] {d}A resistência está embaixo: [p=0.1] {e}menos resistência, mais potência."),
    dict(id="s05", block="chuveiro", text="No chuveiro, {a}mais potência é mais calor na água. [p=0.2] {b}Na posição verão, a resistência é de vinte e dois ohms. [p=0.2] {c}Duzentos e vinte ao quadrado, quarenta e oito mil e quatrocentos, [p=0.1] dividido por vinte e dois: [p=0.1] {d}dois mil e duzentos watts."),
    dict(id="s06", block="chuveiro", text="{a}Na posição inverno, a resistência cai pela metade: onze ohms. [p=0.2] {b}Quarenta e oito mil e quatrocentos dividido por onze: [p=0.1] {c}quatro mil e quatrocentos watts, o dobro. [p=0.3] {d}Com a tensão fixa, potência e resistência são inversamente proporcionais."),
    dict(id="s07", block="chuveiro", text="E como a chave muda a resistência? [p=0.2] {a}Na posição inverno, a corrente passa por um pedaço menor do fio que esquenta. [p=0.2] {b}Fio mais curto, resistência menor. [p=0.3] {c}O porquê do comprimento é assunto da aula da segunda lei de Ohm."),
    # lâmpadas: a etiqueta
    dict(id="s08", block="etiqueta", text="Agora, as lâmpadas. [p=0.2] {a}O brilho depende da potência que a lâmpada recebe de verdade. [p=0.2] Aqui, a resistência de cada lâmpada fica fixa. [p=0.3] {b}A etiqueta, como cem watts e duzentos e vinte volts, [p=0.1] diz a potência {c}só quando ela está ligada nessa tensão."),
    dict(id="s09", block="etiqueta", text="Da etiqueta sai a resistência. [p=0.2] Compare duas lâmpadas de duzentos e vinte volts: [p=0.1] {a}uma de cem watts [p=0.1] e {b}uma de vinte e cinco. [p=0.3] {c}Com a mesma tensão, a de menor potência tem a maior resistência: [p=0.2] {d}um quarto da potência, quatro vezes a resistência."),
    # paralelo e série
    dict(id="s10", block="ligacoes", text="{a}Ligue as duas em paralelo, na tomada. [p=0.2] {b}Cada uma recebe os duzentos e vinte volts da etiqueta. [p=0.3] {c}A de cem watts brilha mais: [p=0.1] {d}cem contra vinte e cinco."),
    dict(id="s11", block="ligacoes", text="{a}Agora, em série. [p=0.2] {b}A corrente é a mesma nas duas: [p=0.1] use pê igual a erre vezes i ao quadrado. [p=0.3] {c}Quem tem mais resistência recebe mais potência. [p=0.2] {d}A de vinte e cinco watts brilha mais, [p=0.1] {e}quatro vezes mais que a de cem."),
    dict(id="s12", block="ligacoes", text="Fazendo a conta inteira: [p=0.2] em série, as resistências somam dois mil quatrocentos e vinte ohms, [p=0.1] e a corrente é um onze avos de ampère. [p=0.3] {a}A de vinte e cinco recebe dezesseis watts, [p=0.1] {b}e a de cem, só quatro. [p=0.3] {c}As duas ficam abaixo da etiqueta, [p=0.1] porque dividem os duzentos e vinte volts entre si."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que a lâmpada de maior potência sempre brilha mais. [p=0.3] {b}Os cem watts da etiqueta só valem com duzentos e vinte volts nela. [p=0.2] {c}Em série, ela fica com só quarenta e quatro volts, [p=0.1] e {d}recebe quatro watts."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho, para etiquetas com a mesma tensão. [p=0.2] {a}Em paralelo, brilha mais a de maior potência. [p=0.2] {b}Em série, brilha mais a de menor potência. [p=0.3] {c}E quantas vezes mais? [p=0.1] {d}Nos dois casos, é a razão entre as etiquetas: [p=0.1] cem dividido por vinte e cinco, quatro."),
    dict(id="s15", block="atalho", text="Funciona porque {a}a etiqueta com mais watts esconde uma resistência menor. [p=0.2] {b}Com a tensão fixa, a menor resistência ganha; [p=0.1] {c}com a corrente fixa, a maior. [p=0.3] {d}Não vale se as etiquetas tiverem tensões diferentes: [p=0.1] aí, calcule a resistência de cada uma."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] Duas lâmpadas de duzentos e vinte volts: [p=0.1] {a}uma de quarenta watts [p=0.1] e {b}outra de cem. [p=0.3] {c}Ligadas em série na tomada de duzentos e vinte, qual brilha mais, [p=0.1] e {d}quantas vezes mais?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Em série, a corrente é a mesma: [p=0.1] {b}brilha mais a de maior resistência, que é a de menor potência na etiqueta. [p=0.3] {c}A de quarenta watts brilha mais."),
    dict(id="s19", block="resposta", text="{a}Quantas vezes? [p=0.1] Cem dividido por quarenta: [p=0.1] {b}duas vezes e meia. [p=0.3] {c}Confira pelas resistências: [p=0.1] {d}a de quarenta tem mil duzentos e dez ohms, [p=0.1] {e}a de cem, quatrocentos e oitenta e quatro. [p=0.2] {f}Mil duzentos e dez dividido por quatrocentos e oitenta e quatro: duas vezes e meia."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}na tomada, a tensão é fixa, e menos resistência é mais potência: [p=0.1] por isso o chuveiro no inverno tem a menor. [p=0.2] {b}Em paralelo, brilha a lâmpada de maior potência; [p=0.1] {c}em série, a de menor."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai abrir a pilha por dentro: [p=0.2] {a}a força eletromotriz [p=0.1] e {b}a tensão que se perde dentro do próprio gerador. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
