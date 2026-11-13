# Estudativo · QUI-ELE-012 — Meia-vida e datação por carbono-14 (Química · Eletroquímica e Radioatividade · Radioatividade).
# Habilidade: calcular que restam 10 mg de 80 mg após 3 meias-vidas, achar o tempo decorrido e estimar a idade de um fóssil
# pelo carbono-14.
# Pré-requisitos: QUI-ELE-011, MAT-EXP-003. Próxima: QUI-ELE-013 (fissão e fusão nuclear).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fatos: iodo-131, usado em exames e no tratamento da tireoide, tem meia-vida de cerca de 8 dias. Carbono-14: meia-vida de
# 5.730 anos; formado na atmosfera; decai por beta a nitrogênio-14 (¹⁴₆C → ⁰₋₁β + ¹⁴₇N). Ser vivo repõe C-14 ao comer e
# respirar; morto, para de repor. Limite prático da datação: cerca de 50 mil anos. Dinossauros (há mais de 66 milhões de anos)
# são datados por outros isótopos, nas rochas.
# Contas: 80 → 40 → 20 → 10: 3 meias-vidas · 3 × 8 = 24 dias · 1/4 = 2 meias-vidas: 2 × 5.730 = 11.460 anos ·
# questão: 12,5% = 1/8 = 3 meias-vidas: 3 × 5.730 = 17.190 anos · erro: "metade + metade = tudo" em 2 meias-vidas.

TITULO = "Meia-vida e datação por carbono-14"

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
    dict(id="s01", block="gancho", text="{a}Um osso encontrado numa caverna tem um quarto do carbono catorze que tinha quando o animal era vivo. [p=0.3] {b}Só com essa informação, dá para dizer a idade dele: [p=0.2] {c}cerca de onze mil e quinhentos anos. [p=0.3] {d}Como?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai calcular {b}quanto resta de um material radioativo, [p=0.2] {c}quanto tempo passou [p=0.1] e {d}a idade de um fóssil. [p=0.2] E ainda leva um {e}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de duas coisas. [p=0.2] {a}Um núcleo radioativo decai: solta uma alfa ou uma beta e vira outro elemento. [p=0.3] E {b}meia-vida é o tempo para uma quantidade cair pela metade, [p=0.1] {c}como os oitenta miligramas de remédio que viravam dez. [p=0.2] Se faltar alguma, procure no canal."),
    # meia-vida radioativa
    dict(id="s04", block="ideia", text="{a}Numa amostra radioativa, os núcleos não decaem todos juntos. [p=0.2] {b}Cada um decai numa hora que ninguém prevê. [p=0.3] {c}Mas, com bilhões de núcleos, o grupo tem um ritmo fixo: [p=0.1] {d}depois de um certo tempo, metade já decaiu. [p=0.3] {e}Esse tempo é a meia-vida do material."),
    dict(id="s05", block="ideia", text="{a}A meia-vida não muda com o calor, com a pressão, nem com o tamanho da amostra. [p=0.2] {b}É uma marca de cada isótopo. [p=0.3] {c}O iodo cento e trinta e um, usado em exames da tireoide, tem meia-vida de cerca de oito dias."),
    # conta
    dict(id="s06", block="conta", text="{a}Comece com oitenta miligramas de iodo cento e trinta e um. [p=0.2] {b}Depois de oito dias, sobram quarenta. [p=0.2] {c}Mais oito dias, vinte. [p=0.2] {d}Mais oito dias, sobram dez miligramas. [p=0.3] {e}Cada meia-vida corta a metade do que sobrou, não da quantidade inicial."),
    dict(id="s07", block="conta", text="{a}De oitenta a dez, foram três metades: [p=0.1] {b}três meias-vidas. [p=0.2] {c}Três vezes oito {d}dá vinte e quatro dias. [p=0.3] {e}Assim se acha o tempo: [p=0.1] conte as metades e multiplique pela meia-vida."),
    # gráfico
    dict(id="s08", block="grafico", text="{a}No gráfico da massa pelo tempo, a curva cai rápido no começo [p=0.1] {b}e cada vez mais devagar. [p=0.3] {c}A cada oito dias, a altura cai pela metade. [p=0.2] {d}Na conta, ela nunca chega a zero: [p=0.1] sempre sobra a metade de alguma coisa."),
    # carbono-14
    dict(id="s09", block="c14", text="Agora, o fóssil. [p=0.2] {a}No ar, uma parte pequena do carbono é carbono catorze, radioativo. [p=0.3] {b}As plantas absorvem esse carbono do ar, e os animais comem as plantas: [p=0.1] {c}a proporção dentro deles fica igual à do ar."),
    dict(id="s10", block="c14", text="{a}Quando o ser vivo morre, para de repor. [p=0.2] {b}O carbono catorze vai decaindo, por beta, e vira nitrogênio. [p=0.3] {c}A meia-vida dele é de cinco mil setecentos e trinta anos. [p=0.3] {d}Quanto menos carbono catorze sobrou, mais tempo passou desde a morte."),
    dict(id="s11", block="c14", text="Volte ao osso. [p=0.2] {a}Um quarto do original. [p=0.1] {b}O inteiro vira um meio, e o meio vira um quarto: [p=0.1] {c}duas metades, duas meias-vidas. [p=0.3] {d}Duas vezes cinco mil setecentos e trinta {e}dá onze mil quatrocentos e sessenta anos."),
    dict(id="s12", block="c14", text="{a}O método funciona até cerca de cinquenta mil anos. [p=0.2] {b}Depois disso, sobra carbono catorze de menos para medir. [p=0.3] {c}Por isso, osso de dinossauro, com mais de sessenta e seis milhões de anos, [p=0.1] {d}é datado por outros isótopos, nas rochas em volta."),
    # erro
    dict(id="s13", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que, em duas meias-vidas, acaba tudo. [p=0.3] {b}Metade na primeira, a outra metade na segunda: zero. [p=0.3] {c}Mas a segunda meia-vida corta a metade do que sobrou. [p=0.2] {d}Sobra um quarto, não nada."),
    # atalho
    dict(id="s14", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}transforme o que sobrou em fração. [p=0.2] {b}Um meio é uma meia-vida. [p=0.1] {c}Um quarto, duas. [p=0.1] {d}Um oitavo, três. [p=0.1] {e}Um dezesseis avos, quatro. [p=0.3] {f}Cada meia-vida dobra o número de baixo."),
    dict(id="s15", block="atalho", text="{a}E se a prova der porcentagem? [p=0.2] {b}Cinquenta por cento é um meio. [p=0.1] {c}Vinte e cinco por cento é um quarto. [p=0.1] {d}Doze e meio por cento é um oitavo. [p=0.3] Funciona porque {e}cada meia-vida multiplica por um meio. [p=0.3] {f}Não compensa quando a fração não é metade de metade, como um terço: [p=0.1] {g}aí, a conta pede logaritmo, assunto de outra aula. [p=0.2] Na prova, quase sempre vem um meio, um quarto ou um oitavo."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Um pedaço de madeira de uma canoa antiga tem doze vírgula cinco por cento do carbono catorze de uma árvore viva. [p=0.3] {b}A meia-vida é de cinco mil setecentos e trinta anos. [p=0.2] {c}Qual é a idade da canoa?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Doze vírgula cinco por cento é um oitavo. [p=0.2] {b}Cem vira cinquenta, que vira vinte e cinco, que vira doze e meio: [p=0.1] {c}três meias-vidas. [p=0.3] {d}Três vezes cinco mil setecentos e trinta {e}dá dezessete mil cento e noventa anos."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}cada meia-vida corta pela metade o que sobrou; [p=0.1] {b}conte as metades e multiplique pela meia-vida para achar o tempo; [p=0.1] {c}e o carbono catorze data o que já foi vivo."),
    dict(id="s20", block="fim", text="Na próxima aula, você vai ver {a}núcleos que se partem e núcleos que se juntam: [p=0.2] {b}a fissão da usina nuclear e a fusão que acende as estrelas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
