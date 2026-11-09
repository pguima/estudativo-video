# Estudativo · FIS-ELE-013 — Associação mista de resistores (Física · Eletricidade · Corrente, Ohm e circuitos).
# Habilidade: reduzir um circuito passo a passo até um único resistor e voltar achando cada corrente.
# Pré-requisitos: FIS-ELE-012 (paralelo: produto pela soma, R/n, mesma tensão). Próxima: FIS-ELE-014.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Atalho: letra em cada nó (fio ideal = mesma letra, porque U = 0·i = 0). Soma das correntes no nó vem do paralelo (FIS-ELE-012);
#   as leis de Kirchhoff (FIS-ELE-024) não são citadas.
# Contas: 6·3/9 = 2 Ω; 4 + 2 = 6 Ω; 18/6 = 3 A; 4·3 = 12 V; 2·3 = 6 V; 12 + 6 = 18; 6/6 = 1 A; 6/3 = 2 A; 1 + 2 = 3.
#   Erro: 18/6 = 3 A, 18/3 = 6 A, 9 A ≠ 3 A. Questão: 12/2 = 6 Ω; 6 + 4 = 10 Ω; 30/10 = 3 A; 6·3 = 18 V; 18/12 = 1,5 A; 1,5·2 = 3.

TITULO = "Associação mista de resistores"

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
    dict(id="s01", block="gancho", text="{a}Um circuito cheio de resistores parece um labirinto. [p=0.3] {b}Mas ele se desfaz com duas peças que você já conhece: [p=0.2] {c}série [p=0.1] e {d}paralelo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai reduzir um circuito a um único resistor [p=0.2] e {b}voltar, achando a corrente em cada um."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}em série, a corrente é a mesma e as resistências somam; [p=0.2] {c}em paralelo, a tensão é a mesma, e a equivalente sai pelo produto pela soma, [p=0.1] ou pelo valor dividido pela quantidade, para iguais. [p=0.3] Se faltar alguma, procure no canal."),
    # reconhecer
    dict(id="s04", block="reconhecer", text="O primeiro passo é {a}reconhecer cada grupo. [p=0.2] {b}Dois resistores estão em série quando nenhum fio sai do ponto entre eles: [p=0.2] a corrente que passa por um é obrigada a passar pelo outro. [p=0.3] {c}Estão em paralelo quando ligam os mesmos dois nós, [p=0.2] os pontos onde a corrente se divide."),
    # reduzir
    dict(id="s05", block="reduzir", text="Veja este circuito. [p=0.2] Uma pilha de {a}dezoito volts, [p=0.1] {b}um resistor de quatro ohms, [p=0.2] e, depois dele, {c}seis ohms e três ohms em paralelo, entre os mesmos dois nós."),
    dict(id="s06", block="reduzir", text="{a}Comece pelo paralelo. [p=0.2] {b}Seis vezes três, dezoito; [p=0.1] seis mais três, nove; [p=0.1] {c}dezoito dividido por nove, dois ohms. [p=0.3] {d}Redesenhe, com um só resistor de dois ohms no lugar dos dois. [p=0.3] {e}Sobram quatro e dois em série: [p=0.1] {f}a equivalente é seis ohms."),
    dict(id="s07", block="reduzir", text="{a}A corrente que sai da pilha é dezoito dividido por seis: [p=0.1] {b}três ampères."),
    # voltar
    dict(id="s08", block="voltar", text="Agora, {a}o caminho de volta. [p=0.2] {b}Os três ampères passam inteiros pelo resistor de quatro ohms, que está em série: [p=0.2] {c}a tensão nele é quatro vezes três, doze volts. [p=0.3] {d}O paralelo equivale a dois ohms, e também recebe os três ampères: [p=0.1] {e}dois vezes três, seis volts nele. [p=0.2] Doze mais seis, os dezoito da pilha."),
    dict(id="s09", block="voltar", text="Esses seis volts são {a}os mesmos nos dois ramos. [p=0.2] {b}No de seis ohms: seis dividido por seis, um ampère. [p=0.2] {c}No de três: seis dividido por três, dois ampères. [p=0.3] {d}Um mais dois, três: [p=0.1] a corrente que chegou ao nó."),
    # erro
    dict(id="s10", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}usar a tensão da pilha no paralelo. [p=0.3] A pessoa faz {b}dezoito dividido por seis, três ampères, [p=0.1] e {c}dezoito dividido por três, seis ampères."),
    dict(id="s11", block="erro", text="{a}Nove ampères nos ramos, se só três saem da pilha? [p=0.2] {b}Impossível. [p=0.3] {c}Doze dos dezoito volts ficaram no resistor de quatro ohms, antes do paralelo."),
    # atalho
    dict(id="s12", block="atalho", text="Agora, o atalho para circuitos confusos: [p=0.2] {a}dê uma letra a cada nó. [p=0.3] {b}Um fio sem resistor não muda a letra: [p=0.1] as duas pontas dele recebem a mesma. [p=0.3] {c}Resistores com o mesmo par de letras estão em paralelo, [p=0.2] {d}não importa como foram desenhados. [p=0.3] {e}Dois resistores desenhados um embaixo do outro, [p=0.1] com as pontas nas letras á e bê, [p=0.1] estão em paralelo, mesmo parecendo outra coisa."),
    dict(id="s13", block="atalho", text="Funciona porque {a}a resistência de um fio é praticamente zero: [p=0.2] a tensão nele é zero vezes a corrente, zero. [p=0.2] {b}As duas pontas são, na prática, o mesmo ponto. [p=0.3] {c}Não compensa em circuitos pequenos, em que a série e o paralelo já estão à vista."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Uma fonte de {a}trinta volts liga {b}um resistor de quatro ohms [p=0.2] em série com {c}dois resistores de doze ohms em paralelo. [p=0.3] {d}Qual é a corrente em cada resistor de doze ohms?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Dois de doze em paralelo: doze dividido por dois, seis ohms. [p=0.2] {b}Em série com quatro: dez ohms. [p=0.2] {c}Corrente total: trinta dividido por dez, três ampères."),
    dict(id="s17", block="resposta", text="Agora, a volta. [p=0.2] {a}No paralelo, seis vezes três, dezoito volts. [p=0.2] {b}Em cada resistor de doze ohms, dezoito dividido por doze: [p=0.1] {c}um vírgula cinco ampère. [p=0.3] {d}As duas correntes são iguais, porque os ramos são iguais, [p=0.1] e somam os três ampères."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: {a}reduza um grupo de cada vez, redesenhando; [p=0.2] {b}ache a corrente total; [p=0.2] e {c}volte: na série, a corrente passa inteira, [p=0.1] e, no paralelo, a tensão é a mesma."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai ver o que acontece quando um fio {a}liga dois pontos sem resistor nenhum: [p=0.2] {b}o curto-circuito, [p=0.1] e como {c}o disjuntor protege a sua casa. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
