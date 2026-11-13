# Estudativo · QUI-LIG-003 — Ligação metálica e ligas (Química · Ligações Químicas · Ligações iônica, covalente e metálica).
# Habilidade: explicar pelo mar de elétrons por que o cobre conduz eletricidade e pode ser dobrado e dizer do que são feitos o bronze e o aço.
# Pré-requisitos: QUI-ATO-009. Próxima: QUI-LIG-004 (qual é a ligação e o que ela explica).
# Atenção: LIG-001 e LIG-002 NÃO estão em "Já ensinado": íon positivo vem da ATO-004/ATO-009; nada de iônica ou covalente.
# Marcas: {cue} animação · [p=0.2] pausa. Questão inédita, criada para esta aula.
# Fatos: bronze = cobre + estanho (sinos, estátuas, medalhas); aço = ferro + pouco carbono (até ≈ 2 %); o carbono fica nos vãos
# entre os átomos de ferro, o estanho toma o lugar de átomos de cobre: os dois "têm outro tamanho" e travam o escorregar.
# Ouro das joias (18 quilates) leva cobre (e prata); o átomo de cobre é menor que o de ouro. Corrente = carga andando num sentido.

TITULO = "Ligação metálica e ligas"

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
    dict(id="s01", block="gancho", text="{a}Pegue um fio de cobre e dobre: [p=0.1] {b}ele entorta, mas não quebra. [p=0.3] {c}Ligue as pontas numa pilha, e a corrente elétrica passa. [p=0.3] {d}As duas coisas têm a mesma explicação, e ela está nos elétrons."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai explicar isso pelo {b}mar de elétrons [p=0.2] e saber {c}do que são feitos o bronze e o aço. [p=0.2] E leva um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula de famílias, uma ideia só: [p=0.2] {a}os metais têm poucos elétrons na última camada, de um a três, [p=0.2] e {b}perdem esses elétrons com facilidade. [p=0.2] {c}O átomo que perde elétrons vira um íon positivo. [p=0.2] Se faltar essa aula, procure no canal."),
    # mar de elétrons
    dict(id="s04", block="mar", text="Num pedaço de cobre, há bilhões de bilhões de átomos juntos. [p=0.2] {a}Cada átomo solta os elétrons da última camada. [p=0.3] {b}O que fica no lugar são íons positivos, arrumados em fileiras. [p=0.3] {c}E os elétrons soltos passeiam pelo metal inteiro, [p=0.1] sem dono. [p=0.3] É o {d}mar de elétrons."),
    dict(id="s05", block="mar", text="{a}Os íons positivos e o mar negativo se atraem. [p=0.2] {b}Essa atração é a ligação metálica. [p=0.3] {c}O mar de elétrons funciona como uma cola, [p=0.1] que segura todos os íons ao mesmo tempo."),
    # conduz
    dict(id="s06", block="conduz", text="Por que o metal conduz eletricidade? [p=0.2] {a}Corrente elétrica é carga andando num sentido só. [p=0.3] No metal, {b}os elétrons já estão soltos. [p=0.2] {c}Ligue a pilha, e eles passam a andar todos para o mesmo lado. [p=0.3] {d}Pelo mesmo motivo, o metal conduz calor: [p=0.1] os elétrons soltos levam o calor de um ponto ao outro do metal."),
    # dobra
    dict(id="s07", block="dobra", text="E por que dobra sem quebrar? [p=0.2] {a}Dobre ou bata no metal, e as fileiras de íons escorregam umas sobre as outras. [p=0.3] {b}O mar de elétrons vai junto e continua colando. [p=0.3] Por isso o metal vira {c}lâmina, como o papel-alumínio, [p=0.1] e {d}fio, como o de cobre. [p=0.2] {e}Ser maleável é virar lâmina; [p=0.1] ser dúctil é virar fio."),
    # ligas
    dict(id="s08", block="ligas", text="Metal puro nem sempre é o melhor. [p=0.2] {a}Liga metálica é um metal misturado com outro elemento, [p=0.1] derretidos juntos e depois resfriados até ficarem sólidos. [p=0.3] {b}O bronze é cobre com estanho. [p=0.2] {c}É mais duro que o cobre puro: [p=0.1] serve para sinos, estátuas e medalhas."),
    dict(id="s09", block="ligas", text="{a}O aço é ferro com uma pitada de carbono. [p=0.2] {b}Fica bem mais resistente que o ferro puro: [p=0.1] vai em vigas, pregos e ferramentas. [p=0.3] {c}Repare: o carbono nem é metal, e a liga existe do mesmo jeito."),
    dict(id="s10", block="ligas", text="Por que a liga é mais dura? [p=0.2] {a}Os átomos do outro elemento têm outro tamanho. [p=0.2] {b}Eles ficam no meio das fileiras, como pedras num trilho, [p=0.1] {c}e atrapalham o escorregar. [p=0.3] {d}Fileira que escorrega menos é metal que entorta menos."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro comum: [p=0.2] {a}achar que o bronze é um elemento novo. [p=0.3] {b}Procure na tabela periódica: não há bronze. [p=0.2] {c}Liga é uma mistura: [p=0.1] o cobre e o estanho estão juntos, e cada um continua lá. [p=0.2] {d}A receita pode até mudar, com mais ou menos estanho."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho de prova: [p=0.2] {a}viu propriedade de metal, conduzir ou dobrar? [p=0.1] {b}A resposta passa pelos elétrons livres, o mar de elétrons. [p=0.3] Funciona porque {c}os elétrons livres explicam as duas coisas: [p=0.1] carga que anda e cola que acompanha. [p=0.3] {d}Não compensa quando a pergunta é por que a liga é mais dura: [p=0.1] {e}aí, a resposta são os átomos de outro tamanho."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] {a}O ouro puro é tão mole que uma joia feita só dele entorta e arranha fácil. [p=0.2] {b}Por isso, o ouro das joias leva cobre misturado. [p=0.3] {c}Por que a mistura deixa a joia mais dura? [p=0.2] E {d}ela continua conduzindo eletricidade?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] {a}A joia é uma liga: ouro com cobre. [p=0.2] {b}O átomo de cobre é menor que o de ouro [p=0.1] e {c}trava as fileiras. [p=0.2] Sem escorregar tanto, {d}a joia entorta menos. [p=0.3] E {e}conduz, sim: [p=0.1] {f}os dois são metais, e o mar de elétrons continua lá."),
    # fechamento
    dict(id="s16", block="fim", text="Resumindo: [p=0.1] {a}no metal, os íons positivos ficam em fileiras, [p=0.1] presos por um mar de elétrons soltos. [p=0.2] {b}Os elétrons que andam explicam a condução, [p=0.1] {c}as fileiras que escorregam explicam o dobrar, [p=0.1] e {d}a liga mistura átomos de outro tamanho para endurecer."),
    dict(id="s17", block="fim", text="Na próxima aula, você junta {a}as três ligações: iônica, covalente e metálica. [p=0.2] Vai dizer {b}qual é a do sal, a da água e a do ferro, [p=0.1] e {c}prever quem conduz eletricidade e quem só derrete em temperatura alta. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
