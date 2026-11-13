# Estudativo · QUI-ELE-005 — Pilhas e baterias do dia a dia (Química · Eletroquímica e Radioatividade · Pilhas e corrosão).
# Habilidade: dizer o que oxida e o que reduz na pilha alcalina e na bateria de chumbo, por que uma bateria recarrega e por que
# pilha não vai para o lixo comum.
# Pré-requisitos: QUI-ELE-004. Próxima: QUI-ELE-006 (corrosão: a ferrugem como pilha e o metal de sacrifício).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fatos: alcalina = ânodo de zinco em pó, cátodo de MnO₂, eletrólito KOH (base, daí "alcalina"), 1,5 V, não recarregável.
# Reação simplificada: Zn + 2 MnO₂ → ZnO + Mn₂O₃ (Zn 0 → +2; Mn +4 → +3: 2 Mn × 1 e⁻ = 2 e⁻).
# Chumbo: Pb + PbO₂ + 2 H₂SO₄ → 2 PbSO₄ + 2 H₂O (Pb 0 → +2 no ânodo; Pb +4 → +2 no cátodo); ~2 V por célula, 6 células = 12 V.
# Recarga: corrente de fora força a reação inversa (eletrólise, outra aula); funciona porque o PbSO₄ fica grudado nas placas.
# Íon-lítio: o lítio é o metal mais leve e o que mais fácil perde elétrons. Ni-Cd: Cd + 2 NiOOH + 2 H₂O → Cd(OH)₂ + 2 Ni(OH)₂
# (Cd 0 → +2; Ni +3 → +2). Descarte: metais tóxicos (chumbo, mercúrio, cádmio) e eletrólito corrosivo; no Brasil, a Política
# Nacional de Resíduos Sólidos (Lei 12.305/2010) obriga a logística reversa: pilhas e baterias voltam por pontos de coleta.
# Já ensinado não inclui QUI-ELE-015: as equações vêm prontas, sem pedir balanceamento.

TITULO = "Pilhas e baterias do dia a dia"

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
    dict(id="s01", block="gancho", text="{a}A pilha do controle remoto acaba e vai para o lixo. [p=0.3] {b}A bateria do carro, não: [p=0.1] o próprio carro a recarrega, por anos. [p=0.3] {c}As duas são pilhas. [p=0.2] {d}O que muda por dentro?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai dizer {b}o que se oxida e o que se reduz [p=0.1] na pilha alcalina e na bateria de chumbo, [p=0.2] {c}por que uma recarrega [p=0.1] e {d}por que pilha não vai para o lixo comum. [p=0.2] E ainda leva um {e}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de duas coisas. [p=0.2] {a}Toda pilha tem um ânodo, que se oxida e manda elétrons pelo fio, [p=0.1] {b}e um cátodo, que recebe e se reduz. [p=0.3] E {c}calcular o Nox pela soma que fecha em zero. [p=0.2] Se faltar alguma, procure no canal."),
    # alcalina
    dict(id="s04", block="alcalina", text="Abra uma pilha alcalina, dessas de controle remoto. [p=0.2] {a}No miolo, há zinco em pó. [p=0.2] {b}Em volta, uma pasta escura de dióxido de manganês, {c}eme ene ó dois. [p=0.3] {d}No meio, uma base forte, o hidróxido de potássio: [p=0.1] é a base que dá o nome, alcalina."),
    dict(id="s05", block="alcalina", text="Quem se oxida? [p=0.2] {a}O zinco começa como metal, com Nox zero, [p=0.1] {b}e termina como óxido de zinco, com mais dois. [p=0.2] {c}Subiu: o zinco se oxida, é o ânodo, o polo negativo."),
    dict(id="s06", block="alcalina", text="{a}No dióxido de manganês, dois oxigênios dão menos quatro: [p=0.1] {b}o manganês é mais quatro. [p=0.3] {c}Ele termina num óxido em que vale mais três. [p=0.2] {d}Desceu: o manganês se reduz, é o cátodo, o polo positivo. [p=0.3] {e}A pilha dá um vírgula cinco volt."),
    # chumbo
    dict(id="s07", block="chumbo", text="Agora, a bateria do carro. [p=0.2] {a}Por dentro, placas de chumbo mergulhadas em ácido sulfúrico. [p=0.3] {b}Umas placas são de chumbo metálico, com Nox zero. [p=0.2] {c}As outras são de dióxido de chumbo, pê bê ó dois, [p=0.1] {d}com o chumbo em mais quatro."),
    dict(id="s08", block="chumbo", text="Quando a bateria trabalha, {a}as duas placas viram o mesmo sal, o sulfato de chumbo, [p=0.1] com o chumbo em mais dois. [p=0.3] {b}O chumbo metálico sobe de zero para mais dois: [p=0.1] se oxida, é o ânodo. [p=0.2] {c}O do dióxido desce de mais quatro para mais dois: [p=0.1] se reduz, é o cátodo, o polo positivo."),
    dict(id="s09", block="chumbo", text="{a}Cada célula da bateria dá cerca de dois volts. [p=0.2] {b}A bateria tem seis células, uma atrás da outra: [p=0.1] {c}seis vezes dois, doze volts."),
    # recarga
    dict(id="s10", block="recarga", text="E por que essa recarrega? [p=0.2] {a}O sulfato de chumbo que se forma fica grudado nas placas. [p=0.3] {b}Com o motor ligado, o alternador, movido pelo motor, manda uma corrente que empurra os elétrons ao contrário, [p=0.1] {c}e a reação anda para trás: [p=0.1] {d}volta a ter chumbo e dióxido de chumbo. [p=0.3] {e}Forçar uma reação com corrente é assunto de outra aula, a de eletrólise."),
    dict(id="s11", block="recarga", text="{a}Na alcalina, os produtos mudam de forma e não voltam ao lugar: [p=0.1] {b}forçar a recarga pode vazar ou esquentar. [p=0.3] {c}A bateria do celular, de íon-lítio, também recarrega. [p=0.2] {d}O lítio é o metal mais leve e fica lá embaixo na escada de potenciais: [p=0.1] muita energia em pouco peso."),
    # descarte
    dict(id="s12", block="descarte", text="E o lixo? [p=0.2] {a}Pilhas e baterias podem ter metais tóxicos, como chumbo, mercúrio e cádmio, [p=0.1] {b}e líquidos que corroem. [p=0.3] {c}No lixo comum, a carcaça se rompe, [p=0.1] {d}e os metais vão para o solo e a água."),
    dict(id="s13", block="descarte", text="{a}Por isso, a lei brasileira obriga a logística reversa: [p=0.2] {b}pilhas e baterias voltam por pontos de coleta, em lojas e mercados, [p=0.1] {c}até o fabricante, que recicla ou dá o destino certo."),
    # erro
    dict(id="s14", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}achar que a bateria guarda eletricidade, como um balde de elétrons. [p=0.3] {b}Ela guarda reagentes químicos. [p=0.2] {c}A energia só vira corrente quando a reação acontece. [p=0.2] {d}Bateria descarregada é bateria sem reagente, não sem elétron."),
    # atalho
    dict(id="s15", block="atalho", text="Agora, o atalho de prova: [p=0.2] {a}numa pilha com metal e óxido, [p=0.1] {b}o metal puro, de Nox zero, é o ânodo. [p=0.2] {c}O óxido, com o Nox alto, é o cátodo. [p=0.3] {d}Zinco e dióxido de manganês; [p=0.1] {e}chumbo e dióxido de chumbo."),
    dict(id="s16", block="atalho", text="Funciona porque {a}o metal puro só pode perder elétrons, [p=0.1] {b}e, nessas pilhas, o Nox alto do óxido desce. [p=0.3] {c}Não compensa quando quem se reduz é um íon da solução, como na pilha de Daniell: [p=0.1] aí, use a escada de potenciais."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}Na pilha recarregável de níquel e cádmio, [p=0.1] {b}o cádmio metálico vira hidróxido de cádmio, com Nox mais dois, [p=0.2] {c}e o níquel vai de mais três para mais dois. [p=0.3] {d}Quem se oxida, quem é o cátodo, [p=0.1] {e}e por que ela não vai para o lixo comum?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}O cádmio sobe de zero para mais dois: [p=0.1] se oxida, é o ânodo. [p=0.3] {b}O níquel desce de mais três para mais dois: [p=0.1] se reduz, é o cátodo. [p=0.3] {c}E o cádmio é um metal tóxico: [p=0.1] {d}essa pilha vai para o ponto de coleta."),
    # fechamento
    dict(id="s20", block="fim", text="Resumindo: [p=0.1] {a}na pilha de metal e óxido, o metal puro se oxida e o óxido se reduz; [p=0.1] {b}a bateria recarrega quando a corrente de fora consegue desfazer a reação; [p=0.1] {c}e pilha vai para a coleta, não para o lixo."),
    dict(id="s21", block="fim", text="Na próxima aula, você vai ver {a}uma pilha que ninguém quer: a ferrugem, [p=0.2] e {b}como um pedaço de zinco protege o casco de um navio. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
