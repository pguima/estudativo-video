# Estudativo · QUI-ATO-012 — Praticando: tabela periódica (Química · Átomo e Tabela Periódica · prática).
# Habilidade: localizar elementos e comparar propriedades periódicas em questões de prova.
# Pré-requisitos: QUI-ATO-008 a QUI-ATO-011. Última da trilha; a ponte vai para QUI-LIG-001 (regra do octeto e ligação iônica).
# Questões inéditas, criadas para esta aula.
# Fatos: K (19) = ... 3p⁶ 4s¹ → período 4, família 1, alcalino, metal, K⁺; F (per. 2, fam. 17), Cl (3, 17), S (3, 16) → maior raio S;
# no HCl o cloro puxa mais (fila: Cl antes de H); Li tem energia de ionização maior que Cs; Cs reage com mais violência na água.

TITULO = "Praticando: tabela periódica"

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
    dict(id="s01", block="gancho", text="{a}Quatro questões sobre a tabela periódica, [p=0.1] criadas para esta aula. [p=0.3] Na prova, a tabela vem junto: [p=0.1] {b}ninguém pede para decorar, pede para ler. [p=0.3] Em cada questão, {c}pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar quatro ferramentas: [p=0.2] {a}período e família pela distribuição, [p=0.2] {b}as famílias com nome, [p=0.2] {c}a seta do raio [p=0.2] e {d}a seta da energia de ionização e da eletronegatividade. [p=0.3] Se alguma travar, procure a aula no canal."),
    # questão 1: localizar
    dict(id="s03", block="questao1", text="{a}Questão um. [p=0.2] Um elemento tem a distribuição {b}um esse dois, [p=0.1] dois esse dois, [p=0.1] dois pê seis, [p=0.1] três esse dois, [p=0.1] três pê seis, [p=0.1] quatro esse um. [p=0.3] {c}Em que período e família ele está? [p=0.2] {d}É metal ou ametal? [p=0.2] E {e}qual é a carga do seu íon?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}O maior número de camada é quatro: quarto período. [p=0.2] {b}Na camada quatro há um elétron: família um. [p=0.3] {c}Família um é a dos metais alcalinos: [p=0.1] {d}é um metal. [p=0.2] {e}Perde o único elétron de fora: carga um mais. [p=0.3] Somando tudo, dezenove elétrons: [p=0.1] {f}é o potássio."),
    # questão 2: raio
    dict(id="s06", block="questao2", text="{a}Questão dois. [p=0.2] {b}Flúor e cloro estão na família dezessete. [p=0.1] {c}O enxofre está na família dezesseis, no mesmo período do cloro. [p=0.3] {d}Dos três, qual tem o maior raio?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá, uma comparação de cada vez. [p=0.2] {a}O cloro está embaixo do flúor: [p=0.1] {b}o cloro é maior. [p=0.3] {c}O enxofre está à esquerda do cloro: [p=0.1] {d}o enxofre é maior ainda. [p=0.3] {e}O maior raio é o do enxofre. [p=0.2] Ele fica mais perto do canto de baixo, à esquerda."),
    # atalho
    dict(id="s09", block="atalho", text="Aqui cabe o atalho da trilha: [p=0.1] {a}desenhe duas setas no rascunho. [p=0.3] {b}Uma para baixo e para a esquerda: [p=0.1] {c}o raio cresce para lá. [p=0.3] {d}Outra para cima e para a direita: [p=0.1] {e}energia de ionização e eletronegatividade crescem para lá. [p=0.2] Na eletronegatividade, o campeão é o flúor."),
    dict(id="s10", block="atalho", text="Funciona porque {a}as três propriedades dependem de quão perto do núcleo estão os elétrons de fora. [p=0.3] {b}Só não resolve as diagonais da eletronegatividade: [p=0.1] {c}para elas, use a fila."),
    # questão 3: eletronegatividade
    dict(id="s11", block="questao3", text="{a}Questão três. [p=0.2] No ácido do estômago, {b}um hidrogênio fica preso a um cloro. [p=0.3] {c}Qual dos dois átomos puxa mais os elétrons?"),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="Vamos lá. [p=0.2] {a}O hidrogênio fica no alto, à esquerda, e o cloro mais embaixo, à direita: [p=0.1] {b}é uma diagonal. [p=0.3] Então, vale a fila: [p=0.1] {c}Fui Ontem No Clube, e assim por diante. [p=0.2] {d}O cloro vem bem antes do hidrogênio, que é o último. [p=0.3] {e}Quem puxa mais é o cloro."),
    # questão 4: ionização e reatividade
    dict(id="s14", block="questao4", text="{a}Última questão. [p=0.2] {b}Lítio e césio são metais alcalinos. [p=0.1] {c}O césio fica bem mais embaixo, na mesma coluna. [p=0.3] {d}Qual tem a maior energia de ionização? [p=0.2] E {e}qual reage com mais violência na água?"),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="Vamos lá. [p=0.2] {a}A energia de ionização cresce para cima: [p=0.1] {b}a maior é a do lítio. [p=0.3] {c}O césio é bem maior, e o elétron de fora fica longe do núcleo. [p=0.2] {d}Ele perde esse elétron com muita facilidade, [p=0.1] {e}e por isso reage com mais violência."),
    dict(id="s17", block="resposta4", text="Repare na pegadinha: [p=0.1] {a}energia de ionização alta quer dizer segurar bem o elétron. [p=0.2] {b}Quem segura bem reage menos."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}ache período e família pela distribuição, [p=0.2] {b}use as duas setas [p=0.2] e, {c}nas diagonais, a fila."),
    dict(id="s19", block="fim", text="Na próxima trilha, Ligações Químicas, você conhece {a}a regra do octeto, que explica a troca de elétrons entre sódio e cloro, [p=0.2] e {b}monta a fórmula do óxido de alumínio cruzando as cargas dos íons. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
