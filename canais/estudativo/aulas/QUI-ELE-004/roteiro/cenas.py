# Estudativo · QUI-ELE-004 — Calcular a ddp e prever a reação (Química · Eletroquímica e Radioatividade · Pilhas e corrosão).
# Habilidade: calcular que a pilha de zinco e cobre tem 1,10 V, sabendo o que o volt mede, e dizer pelo potencial se uma reação
# acontece sozinha.
# Pré-requisitos: QUI-ELE-003, MAT-NUM-016, FIS-ELE-004. Próxima: QUI-ELE-005 (pilha alcalina, bateria de chumbo, descarte).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Potenciais padrão de redução (25 °C, 1 mol/L), valores de tabela usados em prova: Mg²⁺/Mg −2,37 · Zn²⁺/Zn −0,76 ·
# Fe²⁺/Fe −0,44 · 2H⁺/H₂ 0,00 · Cu²⁺/Cu +0,34 · Ag⁺/Ag +0,80 V.
# Contas: Zn/Cu: 0,34 − (−0,76) = 1,10 · Zn/Ag: 0,80 − (−0,76) = 1,56 · Fe em Cu²⁺: 0,34 − (−0,44) = 0,78 > 0 ·
# Cu em Zn²⁺: −0,76 − 0,34 = −1,10 < 0 · erro: −0,76 + 0,34 = −0,42 · Mg/Cu: 0,34 − (−2,37) = 2,71 · Ag em Cu²⁺: 0,34 − 0,80 = −0,46.
# "1,10 V" lido "um vírgula dez volt"; o "dá" antes de cada resultado evita que a voz funda números.
# Já ensinado não inclui QUI-ELE-015: nada de coeficientes no cálculo (o erro de multiplicar o potencial fica de fora).

TITULO = "Calcular a ddp e prever a reação"

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
    dict(id="s01", block="gancho", text="{a}A pilha de zinco e cobre marca {b}um vírgula dez volt. [p=0.3] {c}Troque o cobre por prata, e o aparelho pula para {d}um vírgula cinquenta e seis. [p=0.3] {e}Dá para prever esses números sem montar nada?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular {b}a dê dê pê de uma pilha [p=0.1] e dizer, pelo potencial, {c}se uma reação acontece sozinha. [p=0.2] E ainda leva um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de três coisas. [p=0.2] {a}Na pilha, o ânodo se oxida e manda elétrons pelo fio ao cátodo, que se reduz. [p=0.3] {b}Volt é joule por coulomb. [p=0.2] E {c}subtrair um negativo é o mesmo que somar. [p=0.2] Se faltar alguma, procure no canal."),
    # volt
    dict(id="s04", block="volt", text="Comece pelo número do aparelho. [p=0.2] {a}Dê dê pê quer dizer diferença de potencial, a tensão da pilha. [p=0.3] {b}Um vírgula dez volt quer dizer: [p=0.1] {c}cada coulomb de carga que passa pelo fio [p=0.1] {d}leva um vírgula dez joule de energia. [p=0.3] Quanto maior a dê dê pê, mais energia cada carga carrega."),
    # potencial
    dict(id="s05", block="potencial", text="De onde vem esse número? [p=0.2] {a}Cada íon metálico tem uma vontade de receber elétrons e virar metal. [p=0.3] {b}Essa vontade é medida em volt: [p=0.1] {c}o potencial padrão de redução, ê zero, [p=0.1] medido em condições fixas, as da tabela."),
    dict(id="s06", block="potencial", text="Pense numa escada. [p=0.2] {a}No degrau zero fica a referência, o hidrogênio. [p=0.2] {b}Acima dele, o cobre, com mais zero vírgula trinta e quatro, [p=0.1] {c}e a prata, com mais zero vírgula oitenta. [p=0.2] {d}Abaixo, o zinco, com menos zero vírgula setenta e seis. [p=0.3] {e}Quanto mais alto, mais vontade de receber elétrons."),
    dict(id="s07", block="potencial", text="Na pilha, {a}quem tem o potencial maior recebe os elétrons: [p=0.1] se reduz, é o cátodo. [p=0.3] {b}Quem tem o menor se oxida: é o ânodo. [p=0.3] {c}Cobre acima, zinco abaixo: [p=0.1] por isso o zinco se gastava."),
    # dê dê pê
    dict(id="s08", block="ddp", text="{a}A dê dê pê é a distância entre os dois na escada: [p=0.2] {b}o potencial maior menos o menor. [p=0.3] {c}Zero vírgula trinta e quatro, menos o menos zero vírgula setenta e seis. [p=0.3] {d}Subtrair o negativo é somar: [p=0.1] {e}zero vírgula trinta e quatro mais zero vírgula setenta e seis, [p=0.1] {f}dá um vírgula dez volt."),
    dict(id="s09", block="ddp", text="{a}Com a prata no lugar do cobre: [p=0.1] {b}zero vírgula oitenta mais zero vírgula setenta e seis, [p=0.1] {c}dá um vírgula cinquenta e seis. [p=0.3] {d}A prata está mais alta: a distância cresce."),
    # prever
    dict(id="s10", block="prever", text="A mesma escada diz {a}se uma reação acontece sozinha. [p=0.2] {b}Ponha um prego de ferro no sulfato de cobre. [p=0.3] {c}O cobre dois mais está em mais zero vírgula trinta e quatro, [p=0.1] {d}o ferro, em menos zero vírgula quarenta e quatro. [p=0.3] {e}O íon está acima do metal: [p=0.1] {f}ele arranca elétrons do ferro, e a reação acontece."),
    dict(id="s11", block="prever", text="{a}Na conta: potencial de quem recebe menos o de quem perde. [p=0.2] {b}Zero vírgula trinta e quatro mais zero vírgula quarenta e quatro {c}dá zero vírgula setenta e oito. [p=0.3] {d}Positivo: acontece sozinha."),
    dict(id="s12", block="prever", text="{a}E um fio de cobre no sulfato de zinco? [p=0.2] {b}O zinco dois mais teria de receber do cobre: [p=0.1] {c}menos zero vírgula setenta e seis, menos zero vírgula trinta e quatro, [p=0.1] {d}dá menos um vírgula dez. [p=0.3] {e}Negativo: nada acontece."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}somar os potenciais como estão na tabela. [p=0.3] {b}Menos zero vírgula setenta e seis mais zero vírgula trinta e quatro {c}dá menos zero vírgula quarenta e dois. [p=0.3] {d}Numa pilha que funciona, a dê dê pê sai sempre positiva: [p=0.1] {e}o maior menos o menor. [p=0.3] O negativo só aparece quando você testa uma reação que não acontece."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}desenhe a escada, com o maior potencial em cima. [p=0.3] {b}O íon de cima reage com o metal de baixo. [p=0.2] {c}O contrário, nunca. [p=0.3] {d}E quando um potencial é positivo e o outro é negativo, [p=0.1] a dê dê pê é a soma dos números sem o sinal. [p=0.2] O erro era somar com o sinal."),
    dict(id="s15", block="atalho", text="Funciona porque {a}o íon de cima é quem tem mais vontade de receber elétrons. [p=0.3] {b}Não compensa se a tabela da prova der potenciais de oxidação, o contrário dos de redução: [p=0.1] {c}troque o sinal de todos antes."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}O magnésio tem potencial de menos dois vírgula trinta e sete. [p=0.3] {b}Qual é a dê dê pê da pilha de magnésio e cobre, e quem é o ânodo? [p=0.3] {c}E um anel de prata reage com o sulfato de cobre?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Um positivo e um negativo: some os números. [p=0.1] {b}Zero vírgula trinta e quatro mais dois vírgula trinta e sete {c}dá dois vírgula setenta e um volt. [p=0.3] {d}O magnésio está embaixo: se oxida, é o ânodo."),
    dict(id="s19", block="resposta", text="{a}A prata está acima do cobre. [p=0.2] {b}Para reagir, o íon de cobre teria de estar acima do metal, e não está: [p=0.1] {c}zero vírgula trinta e quatro menos zero vírgula oitenta {d}dá menos zero vírgula quarenta e seis. [p=0.2] {e}O anel não reage."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}a dê dê pê é o maior potencial menos o menor; [p=0.1] {b}e o íon de cima reage com o metal de baixo."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai abrir {a}a pilha alcalina e a bateria do carro, [p=0.2] e ver {b}por que uma recarrega e a outra não. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
