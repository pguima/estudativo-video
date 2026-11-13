# Estudativo · QUI-INO-008 — Balancear por tentativas (Química · Funções e Reações Inorgânicas · Reações e balanceamento).
# Habilidade: balancear C₃H₈ + O₂ → CO₂ + H₂O começando por metais e ametais e deixando hidrogênio e oxigênio para o fim.
# Pré-requisitos: QUI-INO-007, MAT-NUM-007. Próxima: QUI-INO-009 (síntese, análise e combustão).
# Primeira aula do módulo Reações e balanceamento. "Já ensinado" NÃO tem ácidos, bases, íons nem tabela periódica: metal e
# ametal são apresentados por exemplos; nenhuma substância é chamada de ácido. Só soma, subtração e multiplicação.
# Fatos: propano C₃H₈ é um dos gases do botijão (GLP = propano + butano). C₃H₈ + 5 O₂ → 3 CO₂ + 4 H₂O (soma 13).
# Ordem "MACHO": metal, ametal, carbono, hidrogênio, oxigênio. H₂O₂ = água oxigenada. 4 Al + 3 O₂ → 2 Al₂O₃.
# Questão inédita: C₂H₆O + 3 O₂ → 2 CO₂ + 3 H₂O (o oxigênio do próprio etanol; soma 9).

TITULO = "Balancear por tentativas"

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
    dict(id="s01", block="gancho", text="{a}Esta é a queima do propano, um dos gases do botijão. [p=0.3] Do jeito que está, {b}ela tem três carbonos à esquerda {c}e um só à direita. [p=0.3] {d}Dois carbonos sumiram? [p=0.2] Não: a equação é que está desequilibrada."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}balancear essa equação, [p=0.2] {b}numa ordem que evita refazer conta, [p=0.2] e {c}conferir o resultado em segundos."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre de duas coisas. [p=0.2] {a}Numa reação, nenhum átomo some e nenhum aparece: [p=0.1] é a lei de Lavoisier. [p=0.3] E {b}o coeficiente multiplica a molécula inteira: [p=0.1] {c}três cê ó dois têm três carbonos e seis oxigênios."),
    # regra
    dict(id="s04", block="regra", text="{a}Balancear é escolher os coeficientes [p=0.1] {b}até cada elemento ter o mesmo número de átomos dos dois lados. [p=0.3] {c}Você só mexe no número da frente. [p=0.2] {d}O índice, o número pequeno, fica como está."),
    dict(id="s05", block="regra", text="E existe uma ordem que funciona. [p=0.2] {a}Primeiro os metais, como ferro, alumínio e magnésio. [p=0.2] {b}Depois os outros ametais, como enxofre e nitrogênio. [p=0.2] {c}Por fim, carbono, [p=0.1] {d}hidrogênio [p=0.1] {e}e oxigênio. [p=0.3] {f}As iniciais formam a palavra macho."),
    dict(id="s06", block="regra", text="{a}O oxigênio fica por último porque aparece em quase todas as substâncias. [p=0.2] {b}Mexer nele cedo obriga a refazer tudo."),
    dict(id="s07", block="metal", text="Veja a ordem num exemplo curto. [p=0.2] {a}Eme gê, mais agá cê éle, produz eme gê cê éle dois, mais agá dois. [p=0.3] {b}Metal primeiro: um magnésio de cada lado. [p=0.1] Está certo. [p=0.3] {c}Ametal: o cloro. [p=0.1] {d}Um à esquerda, dois à direita: [p=0.1] {e}dois na frente do agá cê éle."),
    dict(id="s08", block="metal", text="{a}Por fim, o hidrogênio: [p=0.1] {b}dois agá cê éle têm dois, e o agá dois tem dois. [p=0.3] {c}Balanceada, e sem refazer nada. [p=0.2] {d}Coeficiente um não se escreve."),
    # exemplo do propano
    dict(id="s09", block="propano", text="Vamos ao propano. [p=0.2] Não há metal nem outro ametal, então {a}comece pelo carbono. [p=0.2] {b}São três à esquerda. [p=0.2] {c}Para ter três à direita, ponha três na frente do cê ó dois."),
    dict(id="s10", block="propano", text="{a}Agora o hidrogênio: oito à esquerda. [p=0.2] {b}Cada água tem dois. [p=0.2] {c}Quatro vezes dois dá oito: [p=0.1] {d}quatro na frente do agá dois ó."),
    dict(id="s11", block="propano", text="{a}Por último, o oxigênio. [p=0.2] Conte à direita: [p=0.1] {b}três moléculas de gás carbônico, com dois cada, seis. [p=0.2] {c}Quatro águas com um cada, quatro. [p=0.2] {d}Seis mais quatro dá dez. [p=0.3] {e}Cada ó dois tem dois oxigênios, e cinco vezes dois dá dez: [p=0.1] {f}cinco na frente do ó dois."),
    dict(id="s12", block="propano", text="{a}Cê três agá oito, mais cinco ó dois, [p=0.1] produz três cê ó dois, mais quatro agá dois ó. [p=0.3] {b}Confira: três carbonos, oito hidrogênios e dez oxigênios de cada lado. [p=0.2] {c}Balanceada."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é {a}mexer no índice para fechar a conta. [p=0.2] Faltou oxigênio? [p=0.1] A pessoa troca {b}agá dois ó por agá dois ó dois. [p=0.3] {c}Isso não é mais água: [p=0.1] {d}é água oxigenada, outra substância. [p=0.2] {e}O índice diz o que a substância é. Só o coeficiente pode mudar."),
    # atalho
    dict(id="s14", block="atalho", text="O atalho de prova: [p=0.2] {a}quando o oxigênio dá ímpar de um lado e vem de dois em dois do outro, [p=0.2] {b}dobre a substância que deu ímpar. [p=0.3] {c}Alumínio mais ó dois produz á éle dois ó três: [p=0.1] {d}três oxigênios, ímpar."),
    dict(id="s15", block="atalho", text="{a}Ponha dois no óxido: [p=0.1] seis oxigênios. [p=0.2] {b}Três ó dois dão seis. [p=0.2] {c}E agora há quatro alumínios à direita: [p=0.1] {d}quatro na frente do alumínio. [p=0.3] Funciona porque {e}ímpar vezes dois sempre dá par. [p=0.2] {f}Não compensa se já der par: [p=0.1] no álcool, por exemplo, desconte antes o oxigênio que ele já traz."),
    # questão
    dict(id="s16", block="questao", text="Hora de testar. [p=0.2] {a}Balanceie a queima do álcool comum: [p=0.1] {b}cê dois agá seis ó, mais ó dois, [p=0.1] {c}produz cê ó dois mais agá dois ó. [p=0.3] {d}Qual é a soma dos coeficientes?"),
    dict(id="s17", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s18", block="resposta", text="Vamos lá. [p=0.2] {a}Carbono: dois à esquerda, dois cê ó dois. [p=0.2] {b}Hidrogênio: seis à esquerda, três águas. [p=0.3] {c}Oxigênio à direita: dois vezes dois, mais três, dá sete."),
    dict(id="s19", block="resposta", text="{a}Cuidado: o álcool já traz um oxigênio. [p=0.2] {b}De um para sete faltam seis, [p=0.1] {c}e seis vêm de três ó dois. [p=0.3] {d}Os coeficientes são um, três, dois e três: [p=0.1] {e}a soma dá nove. [p=0.2] Quem esquece de somar o coeficiente um, que não se escreve, chega a oito."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}só o coeficiente muda, [p=0.1] {b}a ordem é metal, ametal, carbono, hidrogênio e oxigênio, [p=0.1] e {c}no fim você confere elemento por elemento."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai dar nome aos tipos de reação: [p=0.2] {a}síntese, análise e combustão, [p=0.2] {b}e prever o que sai de uma queima. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
