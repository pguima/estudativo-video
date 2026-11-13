# Estudativo · QUI-ORG-017 — Praticando: propriedades e isomeria (Química · Química Orgânica · prática).
# Habilidade: prever propriedades e identificar isômeros em questões com remédios e alimentos.
# Pré-requisitos: QUI-ORG-012, QUI-ORG-013, QUI-ORG-014, QUI-ORG-015, QUI-ORG-016. Próxima: QUI-ORG-018 (reações de adição).
# Questões inéditas, criadas para esta aula. Marcas: {cue} animação · [p=0.2] pausa. Fórmulas e nomes por extenso.
# Fatos (CRC/PubChem): pentano ferve a 36 °C (72 g/mol), butan-1-ol a 118 °C (74), ácido propanoico a 141 °C (74);
# etanol 78 °C, metoximetano −24 °C (os dois C2H6O). Vitamina C (C6H8O6) tem quatro OH e dissolve em água; vitamina A
# (retinol, C20H30O) tem um OH numa cadeia longa e dissolve em gordura. Ácido oleico (azeite) = cis; ácido elaídico = trans,
# o mesmo C18H34O2 (gordura trans). Ibuprofeno: um carbono quiral (o CH preso ao anel, ao CH3 e ao COOH): 2 isômeros ópticos.

TITULO = "Praticando: propriedades e isomeria"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações, criadas para esta aula, [p=0.2] com {b}substâncias do dia a dia, remédios e alimentos. [p=0.3] Em cada uma, {c}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}ponto de ebulição, [p=0.2] {b}semelhante dissolve semelhante, [p=0.2] {c}isomeria plana, [p=0.2] {d}cis e trans [p=0.2] e {e}carbono quiral. [p=0.3] Se alguma travar, procure a aula no canal."),
    # 1: ponto de ebulição
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] Três substâncias com moléculas de massa parecida: [p=0.2] {b}o pentano, um hidrocarboneto, [p=0.2] {c}o butan um ol, um álcool, [p=0.2] e {d}o ácido propanoico. [p=0.3] {e}Coloque as três em ordem, do menor para o maior ponto de ebulição."),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="{a}O pentano só tem carbono e hidrogênio: [p=0.1] as atrações entre as moléculas são fracas. [p=0.2] {b}Ferve a trinta e seis graus. [p=0.3] {c}O álcool faz ligação de hidrogênio pelo ó agá: [p=0.1] {d}cento e dezoito graus. [p=0.3] {e}O ácido faz ainda mais ligações de hidrogênio, pelo cê ó ó agá: [p=0.1] as moléculas se prendem aos pares. [p=0.2] {f}Cento e quarenta e um graus."),
    dict(id="s06", block="resposta1", text="{a}Ordem: pentano, álcool, ácido. [p=0.3] Com massas parecidas, {b}quem manda é o tipo de atração entre as moléculas."),
    # 2: solubilidade
    dict(id="s07", block="questao2", text="{a}Situação dois. [p=0.2] {b}A vitamina C tem quatro grupos ó agá numa molécula pequena. [p=0.2] {c}A vitamina A tem um ó agá só, na ponta de uma cadeia longa de carbonos. [p=0.3] {d}Qual se dissolve em água, e qual precisa de gordura para ser absorvida?"),
    dict(id="s08", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s09", block="resposta2", text="{a}Semelhante dissolve semelhante. [p=0.2] {b}Os muitos ó agá deixam a vitamina C polar, como a água: [p=0.1] {c}ela se dissolve em água. [p=0.3] {d}Na vitamina A, a cadeia longa de carbono pesa mais que o único ó agá: [p=0.2] a molécula é quase toda apolar, {e}e se dissolve em gordura."),
    # 3: isomeria plana
    dict(id="s10", block="questao3", text="{a}Situação três. [p=0.2] {b}O etanol da bebida e {c}o metoximetano, um gás usado em alguns aerossóis, [p=0.2] têm a mesma fórmula, {d}cê dois agá seis ó. [p=0.3] {e}Que tipo de isomeria é essa? [p=0.2] {f}E qual dos dois ferve a uma temperatura mais alta?"),
    dict(id="s11", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="resposta3", text="{a}O etanol é álcool: [p=0.1] tem o ó agá. [p=0.2] {b}O metoximetano é éter: [p=0.1] o oxigênio fica entre dois carbonos. [p=0.3] Mesma fórmula, funções diferentes: {c}isomeria de função. [p=0.3] {d}E quem ferve mais alto é o etanol, que faz ligação de hidrogênio: [p=0.1] {e}setenta e oito graus, [p=0.1] {f}contra menos vinte e quatro do éter."),
    # atalho
    dict(id="s13", block="atalho", text="Antes das duas últimas, o atalho para qualquer questão de isomeria: [p=0.2] três perguntas, nesta ordem. [p=0.3] {a}Primeira: a fórmula molecular é a mesma? [p=0.1] Se não for, nem são isômeros. [p=0.3] {b}Segunda: os átomos estão ligados em ordem diferente? [p=0.1] Então é isomeria plana. [p=0.3] {c}Terceira: as ligações são as mesmas e só muda a posição no espaço? [p=0.1] {d}Aí é cis e trans, ou óptica."),
    dict(id="s14", block="atalho", text="Funciona porque cada pergunta elimina um grupo inteiro de respostas. [p=0.3] {a}Só não compensa quando a questão já diz o tipo: [p=0.2] aí vá direto à regra dele."),
    # 4: cis e trans
    dict(id="s15", block="questao4", text="{a}Situação quatro. [p=0.2] {b}O ácido oleico, do azeite, [p=0.2] e {c}o ácido elaídico, de muitas gorduras industrializadas, [p=0.2] têm a mesma fórmula e as mesmas ligações. [p=0.3] {d}No oleico, as duas partes da cadeia ficam do mesmo lado da dupla. [p=0.2] {e}No elaídico, em lados opostos. [p=0.3] {f}Que isomeria é essa, e qual dos dois forma a gordura trans?"),
    dict(id="s16", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s17", block="resposta4", text="Mesmas ligações, posição diferente em volta de uma dupla: [p=0.2] {a}isomeria cis e trans. [p=0.3] {b}Cadeia do mesmo lado é cis: o oleico, do azeite. [p=0.2] {c}Em lados opostos é trans: o elaídico. [p=0.3] {d}É ele que forma a gordura trans."),
    # 5: carbono quiral
    dict(id="s18", block="questao5", text="{a}Situação cinco. [p=0.2] Na tela está {b}o ibuprofeno, um remédio para dor. [p=0.3] {c}Quantos carbonos quirais ele tem, [p=0.2] e {d}quantos isômeros ópticos existem?"),
    dict(id="s19", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta5", text="Use o atalho da aula de carbono quiral: [p=0.2] {a}risque os carbonos do anel e o do cê ó ó agá, que têm ligação dupla, [p=0.2] {b}e os cê agá três e o cê agá dois, que têm hidrogênios iguais. [p=0.3] {c}Este cê agá preso a dois cê agá três também sai: dois ligantes iguais."),
    dict(id="s21", block="resposta5", text="{a}Sobra um carbono: [p=0.1] ele tem {b}hidrogênio, cê agá três, cê ó ó agá e o anel. [p=0.2] {c}Quatro ligantes diferentes: [p=0.1] um carbono quiral. [p=0.3] Dois elevado a um, {d}dois isômeros ópticos."),
    # fechamento
    dict(id="s22", block="fim", text="{a}Se você acertou três ou mais, o módulo está firme. [p=0.2] Se não, reveja a aula da questão que travou. [p=0.3] Na próxima aula, começam as reações orgânicas: [p=0.2] {b}a reação de adição, que transforma {c}óleo em margarina. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
