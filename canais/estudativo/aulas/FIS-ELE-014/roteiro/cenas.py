# Estudativo · FIS-ELE-014 — Curto-circuito, fusível e choque (Física · Eletricidade · Corrente, Ohm e circuitos).
# Habilidade: achar o curto num circuito e explicar por que a casa é ligada em paralelo, para que serve o disjuntor
#   e o que torna o choque perigoso.
# Pré-requisitos: FIS-ELE-013 (reduzir circuito, letra em cada nó). Próxima: FIS-ELE-015.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# O calor da corrente (efeito Joule, FIS-ELE-017) não está em "Já ensinado": citado como assunto de outra aula.
# Valores do corpo (ordens de grandeza usuais dos livros): pele seca ≈ 100.000 Ω, molhada ≈ 1.000 Ω; uns 10 mA já travam
#   o músculo (não se consegue soltar); perto de 100 mA a corrente pode desregular o coração. Tomadas de 127 V e 220 V.
# Contas: 4 + 2 = 6 Ω; 12/6 = 2 A; 12/2 = 6 A = 3·2; 127/1.000 = 0,127 A = 127 mA; 127/100.000 = 0,00127 A ≈ 1,3 mA.
#   Questão: 3·4 = 12 Ω; 12/12 = 1 A; 2·4 = 8 Ω; 12/8 = 1,5 A.

TITULO = "Curto-circuito, fusível e choque"

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
    dict(id="s01", block="gancho", text="{a}Um passarinho pousa num fio desencapado da rua [p=0.2] e {b}não sente nada. [p=0.3] {c}Uma pessoa encosta o dedo num fio da tomada [p=0.1] e {d}leva um choque. [p=0.3] Qual é a diferença?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai achar um curto-circuito [p=0.2] e entender {b}o disjuntor, [p=0.1] {c}a ligação da casa [p=0.1] e {d}o perigo do choque."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}a tensão u é a resistência erre vezes a corrente i; [p=0.2] e {c}reduzir um circuito com série e paralelo, [p=0.1] dando uma letra a cada nó. [p=0.3] Se faltar alguma, procure no canal."),
    # curto
    dict(id="s04", block="curto", text="{a}Curto-circuito é um fio, sem resistor, ligando dois pontos do circuito que tinham tensão entre eles. [p=0.3] {b}A resistência desse fio é praticamente zero. [p=0.2] {c}Então, a tensão entre esses dois pontos é zero vezes a corrente: [p=0.1] zero."),
    dict(id="s05", block="curto", text="E, se a tensão nas pontas de um resistor é zero, {a}a corrente nele também é zero. [p=0.3] {b}O resistor em curto sai do circuito: [p=0.2] é como se não existisse. [p=0.3] Com as letras: {c}as duas pontas do fio recebem a mesma letra, [p=0.1] e {d}o resistor que ficou com as duas pontas na mesma letra some."),
    dict(id="s06", block="curto", text="Exemplo. [p=0.2] Uma pilha de {a}doze volts, com {b}quatro ohms e dois ohms em série. [p=0.2] {c}Seis ohms: dois ampères. [p=0.3] {d}Agora, um fio liga as pontas do resistor de quatro ohms. [p=0.2] {e}Ele sai do circuito, [p=0.1] e sobra só o de dois: [p=0.1] {f}doze dividido por dois, seis ampères. [p=0.3] {g}A corrente ficou três vezes maior."),
    dict(id="s07", block="curto", text="No pior caso, {a}um fio liga direto os dois polos da pilha. [p=0.2] A resistência cai quase a zero, [p=0.1] e {b}a corrente fica enorme. [p=0.3] {c}Corrente grande esquenta os fios: [p=0.1] pode derreter a capa e começar um incêndio. [p=0.2] {d}Esse calor da corrente é assunto de outra aula."),
    # proteção e casa
    dict(id="s08", block="casa", text="Para isso existem {a}o fusível e o disjuntor. [p=0.2] Eles ficam {b}em série, no começo do circuito, [p=0.1] para que toda a corrente passe por eles. [p=0.3] {c}Se a corrente passa do limite, [p=0.1] o fio fino do fusível {d}derrete, [p=0.1] ou o disjuntor {e}desarma. [p=0.2] {f}O circuito abre, e a corrente para."),
    dict(id="s09", block="casa", text="E a casa é ligada {a}em paralelo. [p=0.2] Cada aparelho fica {b}num ramo entre os mesmos dois fios que vêm da rua, [p=0.2] então {c}todos recebem a mesma tensão, [p=0.1] cento e vinte e sete ou duzentos e vinte volts. [p=0.3] E {d}desligar um aparelho não desliga os outros."),
    dict(id="s10", block="casa", text="{a}Em série, a tensão se dividiria, [p=0.1] e um aparelho desligado cortaria todos. [p=0.3] Só que cada ramo novo em paralelo {b}diminui a equivalente e aumenta a corrente total. [p=0.2] {c}Por isso, muita coisa ligada ao mesmo tempo desarma o disjuntor."),
    # choque
    dict(id="s11", block="choque", text="Agora, o choque. [p=0.2] {a}O que machuca é a corrente que atravessa o corpo. [p=0.3] {b}E ela só passa se houver tensão entre dois pontos do corpo, [p=0.2] como {c}a mão no fio e o pé no chão."),
    dict(id="s12", block="choque", text="Por isso, o passarinho escapa: [p=0.2] {a}as duas patas estão no mesmo fio, [p=0.1] quase no mesmo ponto. [p=0.2] {b}Sem tensão entre elas, não passa corrente pelo corpo. [p=0.3] {c}Se a asa encostasse em outro fio, aí, sim, levaria choque."),
    dict(id="s13", block="choque", text="{a}A resistência do corpo muda muito. [p=0.2] Com {b}a pele seca, ela fica perto de cem mil ohms; [p=0.2] {c}molhada, cai para uns mil ohms. [p=0.3] Na tomada de cento e vinte e sete volts, com a pele molhada, [p=0.1] {d}a corrente é cento e vinte e sete dividido por mil: [p=0.2] {e}cento e vinte e sete milésimos de ampère."),
    dict(id="s14", block="choque", text="{a}Uns dez milésimos de ampère já travam os músculos: [p=0.1] a pessoa não consegue soltar. [p=0.2] {b}Perto de cem milésimos, a corrente pode desregular o coração. [p=0.3] {c}Com a pele molhada, os cento e vinte e sete passam dos dois limites. [p=0.2] {d}Com a pele seca, seria pouco mais de um milésimo. [p=0.3] {e}Por isso, nunca mexa em eletricidade com a mão molhada."),
    # erro
    dict(id="s15", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}o fusível vive queimando, [p=0.1] e a pessoa {b}troca por um que aguenta mais corrente. [p=0.3] {c}O fusível para de queimar, [p=0.1] mas {d}o problema continua: [p=0.2] agora, a corrente alta passa pelos fios {e}sem proteção nenhuma. [p=0.2] O certo é descobrir a causa."),
    # atalho
    dict(id="s16", block="atalho", text="Agora, o atalho para achar o curto: [p=0.2] {a}procure um fio sem resistor ligando dois pontos. [p=0.3] {b}Dê a mesma letra às duas pontas dele, [p=0.2] e {c}apague todo resistor que ficou com as duas pontas na mesma letra. [p=0.3] {d}Sobra um circuito mais simples, e você resolve como sempre. [p=0.3] {e}Não confunda: fio com uma lâmpada ou um resistor no meio não é curto."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] Uma bateria de {a}doze volts liga em série {b}três lâmpadas iguais, de quatro ohms cada. [p=0.3] {c}Um fio liga as duas pontas de uma das lâmpadas. [p=0.3] {d}O que acontece com essa lâmpada, [p=0.1] e {e}qual é a corrente nas outras?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] Antes: {a}doze ohms, [p=0.1] doze dividido por doze, um ampère. [p=0.3] {b}Com o fio, a lâmpada em curto fica sem tensão: [p=0.1] {c}ela apaga. [p=0.3] {d}Sobram duas de quatro ohms: oito ohms. [p=0.2] {e}Doze dividido por oito: um vírgula cinco ampère nas outras duas. [p=0.3] {f}A corrente aumentou, porque a resistência total diminuiu."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: {a}fio sem resistor é curto, e o que ele liga sai do circuito; [p=0.2] {b}fusível e disjuntor, em série, abrem o circuito quando a corrente passa do limite; [p=0.2] {c}a casa é em paralelo, para cada aparelho ter a mesma tensão; [p=0.2] e {d}o choque é a corrente que passa pelo corpo."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai {a}medir corrente e tensão com o amperímetro e o voltímetro, [p=0.2] e {b}achar um resistor desconhecido na ponte de Wheatstone. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
