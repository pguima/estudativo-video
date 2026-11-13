# Estudativo · QUI-SOL-010 — Osmose e pressão osmótica (Química · Soluções · Propriedades coligativas).
# Habilidade: dizer para que lado a água passa na membrana e explicar por que o sal conserva a carne e como a osmose reversa
# dessaliniza a água.
# Pré-requisitos: QUI-SOL-004. Próxima: QUI-SOL-011 (praticando: propriedades coligativas).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita.
# "Já ensinado" desta aula NÃO tem estados físicos, pressão (Física), pressão de vapor nem crioscopia: pressão é explicada na hora
# ("empurrão"), e "efeito coligativo" não é usado.
# Fatos: membrana semipermeável deixa passar a água e segura o soluto; a água passa do lado menos concentrado para o mais
# concentrado. Pressão osmótica = pressão que impede a osmose; maior na solução mais concentrada. Soro fisiológico 0,9% tem a
# mesma concentração de partículas do sangue (isotônico); hemácia em água pura incha e pode estourar; em água muito salgada, murcha.
# A água do mar tem cerca de 35 g de sais por litro; a osmose reversa a empurra contra uma membrana com pressão de 50 a 80 atm
# (fica fora da fala). Carne-seca e bacalhau: o sal tira a água dos micróbios, que param de se multiplicar.
# Questão: lado A glicose 0,1 mol/L, lado B glicose 0,3 mol/L → a água vai de A para B, o nível de B sobe; pressão em B maior que
# a osmótica inverte (água de B para A).

TITULO = "Osmose e pressão osmótica"

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
    dict(id="s01", block="gancho", text="{a}A carne-seca dura meses fora da geladeira. [p=0.3] {b}Quem protege a carne é o sal, [p=0.1] {c}mas ele não envenena os micróbios. [p=0.3] {d}Ele tira a água de dentro deles."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai saber {b}para que lado a água passa numa película, [p=0.2] {c}por que o sal conserva a carne [p=0.2] e {d}como se tira o sal da água do mar."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre: [p=0.1] {a}a água é o solvente, e o sal ou o açúcar dissolvido é o soluto. [p=0.3] E {b}quanto mais mol de soluto por litro, mais concentrada é a solução."),
    # membrana
    dict(id="s04", block="membrana", text="{a}Imagine uma película com furinhos minúsculos. [p=0.2] {b}As partículas de água, pequenas, passam pelos furos. [p=0.2] {c}As de soluto, maiores, ficam do lado em que estão. [p=0.3] {d}Essa película se chama membrana semipermeável: [p=0.1] {e}deixa passar só uma parte."),
    dict(id="s05", block="membrana", text="{a}A membrana das células do seu corpo funciona parecido. [p=0.2] {b}E também o papel-celofane e certos plásticos de laboratório."),
    # osmose
    dict(id="s06", block="osmose", text="{a}Ponha a membrana no meio de um tubo dobrado em forma de U. [p=0.2] {b}De um lado, água pura. [p=0.1] {c}Do outro, água com sal. [p=0.3] {d}Com o tempo, a água passa para o lado salgado, [p=0.1] {e}e o nível dele sobe."),
    dict(id="s07", block="osmose", text="{a}Essa passagem da água pela membrana se chama osmose. [p=0.3] {b}O sentido é sempre o mesmo: [p=0.1] {c}do lado menos concentrado para o mais concentrado. [p=0.3] {d}A água vai diluir o lado que tem mais soluto."),
    # pressão osmótica
    dict(id="s08", block="pressao", text="{a}Dá para impedir a osmose. [p=0.2] {b}Empurre o lado salgado com um êmbolo, como o de uma seringa. [p=0.3] {c}Pressão é esse empurrão espalhado pela superfície. [p=0.3] {d}A pressão mínima que segura a água no lugar se chama pressão osmótica."),
    dict(id="s09", block="pressao", text="{a}Quanto mais concentrada a solução, mais a água quer entrar, [p=0.2] {b}e maior é a pressão osmótica."),
    # células
    dict(id="s10", block="celulas", text="{a}Pense numa célula do sangue, a hemácia. [p=0.2] {b}Em água pura, a água entra nela, que incha e pode estourar. [p=0.3] {c}Em água muito salgada, a água sai, e ela murcha. [p=0.3] {d}No soro fisiológico, com zero vírgula nove por cento de sal, nada muda: [p=0.1] {e}a concentração é a mesma do sangue."),
    dict(id="s11", block="celulas", text="Os nomes: [p=0.1] {a}a solução em volta da célula com a mesma concentração é isotônica. [p=0.2] {b}Mais concentrada, hipertônica. [p=0.2] {c}Menos concentrada, hipotônica."),
    # carne
    dict(id="s12", block="carne", text="{a}Agora, a carne-seca. [p=0.2] {b}O sal deixa o lado de fora dos micróbios muito concentrado. [p=0.3] {c}A água sai deles por osmose, [p=0.1] {d}e, sem água, eles não se multiplicam. [p=0.3] {e}O doce em calda funciona igual, com açúcar no lugar do sal."),
    # osmose reversa
    dict(id="s13", block="reversa", text="E a água do mar? [p=0.2] {a}Empurre o lado salgado com uma pressão maior que a osmótica. [p=0.3] {b}A água passa ao contrário: do salgado para o lado puro. [p=0.2] {c}O sal fica para trás. [p=0.3] {d}Isso é a osmose reversa, [p=0.1] {e}usada para tirar o sal da água do mar e em muitos purificadores de casa."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum: [p=0.2] {a}achar que, na osmose, é o sal que atravessa a membrana. [p=0.3] {b}A pessoa diz que o sal entra na célula e a faz murchar. [p=0.3] {c}Mas a membrana segura o soluto. [p=0.2] {d}Quem atravessa é a água: [p=0.1] {e}ela sai da célula para o lado mais concentrado."),
    # atalho
    dict(id="s15", block="atalho", text="O atalho de prova: [p=0.2] {a}a água corre atrás do soluto. [p=0.3] {b}Ache o lado com mais partículas dissolvidas: [p=0.1] {c}é para lá que a água vai, e é lá que o nível sobe. [p=0.3] {d}Com pressão maior que a osmótica, ela volta."),
    dict(id="s16", block="atalho", text="Funciona porque {a}só a água passa, e ela passa até diluir o lado concentrado. [p=0.3] {b}Compare as concentrações em mol por litro, não em gramas. [p=0.3] {c}E o atalho não basta quando o soluto é um sal: [p=0.1] na água, ele se divide em pedaços, e contar esses pedaços é assunto de outra aula."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Um tubo dobrado em U tem uma membrana semipermeável no meio. [p=0.2] {b}No lado A, glicose com zero vírgula um mol por litro. [p=0.2] {c}No lado B, glicose com zero vírgula três. [p=0.3] {d}Para que lado a água passa, e qual nível sobe? [p=0.2] {e}E o que acontece se você empurrar o lado B com pressão maior que a necessária para segurar a água?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="{a}O lado B tem mais soluto. [p=0.2] {b}A água corre atrás dele: [p=0.1] {c}passa de A para B, e o nível de B sobe. [p=0.3] {d}Empurrando B com mais força que isso, o fluxo se inverte: [p=0.1] {e}a água passa de B para A. [p=0.2] É a osmose reversa."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}na osmose, a água atravessa a membrana do lado menos concentrado para o mais concentrado; [p=0.2] {b}a pressão osmótica é o empurrão que impede isso; [p=0.1] e {c}empurrar com mais força inverte o sentido."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai {a}praticar todo o módulo: [p=0.2] {b}ferver, congelar e osmose, em situações do dia a dia. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
