# Estudativo · QUI-ATO-011 — Energia de ionização e eletronegatividade (Química · Átomo e Tabela Periódica · Tabela periódica).
# Habilidade: usar as setas da tabela para dizer qual é mais eletronegativo entre F, O e Cl e quem perde elétron com mais
# facilidade entre Na e Cl.
# Pré-requisitos: QUI-ATO-010. Próxima: QUI-ATO-012 (praticando: tabela periódica).
# Questão inédita, criada para esta aula. A ligação química só é citada (cabo de guerra): é assunto da trilha de Ligações.
# Fatos: a fila escolar é F > O > N > Cl > Br > I > S > C > P > H. Na escala de Pauling, N (3,04) < Cl (3,16) e P (2,19) < H (2,20):
# a fila é a convenção dos livros e vestibulares; a aula só usa F > O > Cl e O > S, que valem em qualquer escala.
# Frase da fila: "Fui Ontem No Clube, Briguei, I Saí Correndo Para o Hospital". Gases nobres ficam fora da escala.
# EI e eletronegatividade crescem para cima e para a direita; Na (3s¹) perde elétron mais fácil que Cl; K mais fácil que Br.

TITULO = "Energia de ionização e eletronegatividade"

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
    dict(id="s01", block="gancho", text="{a}Sódio e cloro, juntos, formam o sal de cozinha. [p=0.3] {b}Para isso, um entrega um elétron, e o outro recebe. [p=0.3] {c}Quem entrega? [p=0.2] {d}A tabela responde, com duas setas."),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai dizer {a}quem perde elétron com mais facilidade [p=0.2] e {b}quem puxa mais os elétrons, [p=0.1] só pela posição na tabela."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula anterior: [p=0.1] {a}o raio cresce para baixo e para a esquerda. [p=0.3] {b}Quanto menor o átomo, [p=0.1] mais perto do núcleo ficam os elétrons de fora."),
    # energia de ionização
    dict(id="s04", block="ionizacao", text="{a}Energia de ionização é a energia para arrancar um elétron de um átomo, [p=0.1] sozinho e no estado gasoso. [p=0.3] {b}Pense num ímã segurando um clipe. [p=0.2] {c}Bem perto do ímã, é difícil puxar. [p=0.1] {d}Mais longe, sai fácil."),
    dict(id="s05", block="ionizacao", text="No átomo pequeno, {a}o elétron de fora fica perto do núcleo, [p=0.1] e é difícil de arrancar. [p=0.3] {b}Por isso, a energia de ionização anda ao contrário do raio: [p=0.2] {c}cresce para cima e para a direita."),
    dict(id="s06", block="ionizacao", text="{a}Sódio e cloro estão no terceiro período. [p=0.2] {b}O sódio, à esquerda, é maior: [p=0.1] {c}tem energia de ionização baixa e perde elétron fácil. [p=0.3] {d}O cloro, à direita, segura bem os seus. [p=0.2] {e}Quem entrega o elétron é o sódio. [p=0.2] {f}Como os dois se juntam depois é assunto de outra aula."),
    # eletronegatividade
    dict(id="s07", block="eneg", text="{a}Eletronegatividade é outra coisa. [p=0.2] {b}É a força com que um átomo puxa os elétrons quando está preso a outro átomo. [p=0.3] Pense num {c}cabo de guerra pelos elétrons: [p=0.1] {d}quem puxa mais é o mais eletronegativo."),
    dict(id="s08", block="eneg", text="{a}Ela também cresce para cima e para a direita. [p=0.3] {c}O campeão é o flúor, no canto de cima, à direita: [p=0.1] {d}o elemento mais eletronegativo de todos."),
    dict(id="s09", block="eneg", text="Compare {a}flúor, oxigênio e cloro. [p=0.2] {b}Oxigênio e flúor estão no segundo período: [p=0.1] {c}o flúor, à direita, ganha. [p=0.3] {d}Flúor e cloro estão na família dezessete: [p=0.1] {e}o flúor, em cima, ganha. [p=0.3] {f}O flúor é o mais eletronegativo dos três."),
    # erro
    dict(id="s10", block="erro", text="O erro comum: [p=0.1] {a}achar que os gases nobres são os mais eletronegativos, [p=0.1] porque estão bem à direita. [p=0.3] {b}Eles quase não se prendem a outros átomos, [p=0.1] então {c}ficam fora dessa escala."),
    # atalho
    dict(id="s11", block="atalho", text="{a}E entre oxigênio e cloro? [p=0.2] {b}Estão em diagonal, e as setas brigam. [p=0.3] Para isso existe {c}a fila de prova, com uma frase para lembrar: [p=0.2] {d}Fui Ontem No Clube, Briguei, í, Saí Correndo Para o Hospital."),
    dict(id="s12", block="atalho", text="{a}Cada inicial é um elemento, na ordem que as provas usam, do mais para o menos eletronegativo: [p=0.2] {b}flúor, oxigênio, nitrogênio, cloro, bromo, iodo, enxofre, carbono, fósforo e hidrogênio. [p=0.3] {c}O oxigênio vem antes do cloro: [p=0.1] {d}é mais eletronegativo."),
    dict(id="s13", block="atalho", text="Funciona porque {a}a fila resolve as diagonais entre esses dez elementos. [p=0.3] {b}Ela não serve para a energia de ionização: [p=0.1] {c}para essa, use as setas."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Ordene flúor, oxigênio e enxofre, do mais para o menos eletronegativo. [p=0.3] E {b}entre potássio e bromo, do quarto período, [p=0.1] {c}quem perde elétron com mais facilidade?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}O flúor está à direita do oxigênio: o flúor ganha. [p=0.2] {b}O oxigênio está em cima do enxofre: o oxigênio ganha. [p=0.2] {c}A ordem é flúor, oxigênio, enxofre. [p=0.3] {d}O potássio, à esquerda, é maior [p=0.1] e tem energia de ionização mais baixa: [p=0.1] {e}é ele que perde elétron mais fácil."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: [p=0.1] {a}energia de ionização e eletronegatividade crescem para cima e para a direita, [p=0.1] {b}ao contrário do raio. [p=0.2] {c}O flúor é o mais eletronegativo, [p=0.1] e {d}os metais da esquerda perdem elétron fácil."),
    dict(id="s18", block="fim", text="Na próxima aula, você pratica {a}a tabela periódica inteira [p=0.1] com {b}questões no estilo da prova. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
