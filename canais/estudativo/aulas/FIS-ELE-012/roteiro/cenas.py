# Estudativo · FIS-ELE-012 — Resistores em paralelo (Física · Eletricidade · Corrente, Ohm e circuitos).
# Habilidade: calcular a equivalente com os atalhos do produto pela soma e de R/n para resistores iguais.
# Pré-requisitos: FIS-ELE-011 (série: corrente igual, Req = soma), MAT-EQU-010 (frações com MMC). Próxima: FIS-ELE-013.
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# 1/Req = 1/R1 + 1/R2 sai de i = U/R1 + U/R2 e i = U/Req. "Nó" é definido aqui. Letras lidas como "erre um" etc.
# Contas: 1/3 + 1/6 = 2/6 + 1/6 = 3/6 = 1/2 → 2 Ω (erro: 1/2 Ω); 12/3 = 4 A, 12/6 = 2 A, 4 + 2 = 6 = 12/2;
#   3·6/(3+6) = 18/9 = 2; 12/3 = 4 Ω (três de 12 Ω). Questão: 4·12/(4+12) = 48/16 = 3 Ω; 12/3 = 4 A; 12/4 = 3 A, 12/12 = 1 A.

TITULO = "Resistores em paralelo"

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
    dict(id="s01", block="gancho", text="{a}Ligue mais um resistor num circuito [p=0.2] e {b}a resistência total diminui. [p=0.3] Parece errado, [p=0.1] mas é o que acontece {c}em paralelo."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular a resistência equivalente em paralelo, [p=0.2] com {b}dois atalhos que resolvem quase toda questão."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}em série, a corrente é a mesma e a equivalente é a soma; [p=0.2] e {c}somar frações com denominadores diferentes, usando o mínimo múltiplo comum. [p=0.3] Se faltar alguma, procure no canal."),
    # o que é paralelo
    dict(id="s04", block="paralelo", text="Em paralelo, {a}cada resistor fica num caminho separado, [p=0.2] e {b}todos ligam os mesmos dois pontos. [p=0.3] Um ponto onde a corrente se divide se chama {c}nó, [p=0.2] e cada caminho entre dois nós é {d}um ramo."),
    dict(id="s05", block="paralelo", text="Daí saem duas regras. [p=0.2] {a}Primeira: a tensão é a mesma em todos os ramos, [p=0.2] porque todos estão ligados aos mesmos dois pontos. [p=0.3] {b}Segunda: a corrente total é a soma das correntes dos ramos."),
    dict(id="s06", block="paralelo", text="Por que a equivalente diminui? [p=0.2] Pense num {a}pedágio. [p=0.2] {b}Abrir mais uma cabine não deixa a passagem mais difícil: [p=0.2] {c}passa mais carro no mesmo tempo. [p=0.3] {d}Cada ramo novo é mais um caminho para a corrente."),
    # a conta
    dict(id="s07", block="conta", text="A conta sai da lei de Ohm. [p=0.2] A corrente em cada ramo é {a}a tensão dividida pela resistência dele. [p=0.3] Somando os ramos, sai a regra: [p=0.2] {b}um dividido pela equivalente é igual a um dividido por erre um, [p=0.1] mais um dividido por erre dois, [p=0.1] e assim por diante."),
    dict(id="s08", block="conta", text="Exemplo: {a}três ohms e seis ohms em paralelo. [p=0.2] {b}Um terço mais um sexto. [p=0.2] {c}O mínimo múltiplo comum é seis: [p=0.1] dois sextos mais um sexto, {d}três sextos, [p=0.1] que é {e}um meio. [p=0.3] Um dividido pela equivalente vale um meio, [p=0.1] então {f}a equivalente vale dois ohms."),
    dict(id="s09", block="conta", text="Repare: {a}dois ohms é menos que o menor resistor, o de três. [p=0.3] {b}Em paralelo, a equivalente é sempre menor que o menor resistor. [p=0.2] Use isso para conferir a resposta."),
    dict(id="s10", block="conta", text="E as correntes? [p=0.2] Com {a}doze volts nos dois: [p=0.2] {b}no de três ohms, doze dividido por três, quatro ampères; [p=0.2] {c}no de seis, dois ampères. [p=0.3] {d}A menor resistência leva a maior corrente. [p=0.2] E {e}quatro mais dois, seis ampères, [p=0.1] é o mesmo que doze dividido pela equivalente."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}parar no um meio e responder meio ohm. [p=0.3] {b}Esse um meio é um dividido pela equivalente. [p=0.2] {c}Falta virar a fração: [p=0.1] {d}a equivalente é dois ohms. [p=0.3] {e}Na prova, o meio ohm costuma estar nas alternativas, esperando quem esquece de virar."),
    # atalho
    dict(id="s12", block="atalho", text="Agora, os atalhos. [p=0.2] {a}Para dois resistores: produto pela soma. [p=0.3] {b}Três vezes seis, dezoito; [p=0.1] {c}três mais seis, nove. [p=0.2] {d}Dezoito dividido por nove: dois ohms. [p=0.2] O mesmo resultado, sem fração."),
    dict(id="s13", block="atalho", text="{a}Para resistores iguais: divida o valor de um deles pela quantidade. [p=0.3] {b}Três resistores de doze ohms: [p=0.1] doze dividido por três, [p=0.1] {c}quatro ohms. [p=0.3] Os dois funcionam porque {d}são a soma de frações já feita, pronta para usar. [p=0.3] {e}O produto pela soma não vale para três de uma vez: [p=0.2] junte dois, e depois junte o terceiro. [p=0.3] {f}Seis, três e dois ohms: [p=0.1] seis com três dá dois; [p=0.1] {g}dois com dois dá um ohm."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Uma pilha de {a}doze volts liga em paralelo {b}quatro ohms e doze ohms. [p=0.3] {c}Qual é a resistência equivalente, [p=0.1] e {d}qual é a corrente que sai da pilha?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}Produto pela soma: quatro vezes doze, quarenta e oito; [p=0.1] quatro mais doze, dezesseis. [p=0.2] {b}Quarenta e oito dividido por dezesseis: [p=0.1] {c}três ohms. [p=0.2] Menor que quatro: confere. [p=0.3] {d}A corrente total é doze dividido por três: [p=0.1] {e}quatro ampères."),
    dict(id="s17", block="resposta", text="{a}Conferindo pelos ramos: [p=0.2] {b}doze dividido por quatro, três ampères; [p=0.1] {c}doze dividido por doze, um ampère. [p=0.2] {d}Três mais um, quatro."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: em paralelo, {a}a tensão é a mesma, [p=0.2] {b}a corrente se divide, [p=0.2] e {c}a equivalente é menor que o menor resistor: [p=0.2] {d}produto pela soma para dois, e o valor dividido pela quantidade para iguais."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai juntar série e paralelo {a}no mesmo circuito, [p=0.2] e {b}reduzir tudo, passo a passo, até um único resistor. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
