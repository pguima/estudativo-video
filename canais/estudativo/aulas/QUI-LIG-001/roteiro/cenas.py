# Estudativo · QUI-LIG-001 — Regra do octeto e ligação iônica (Química · Ligações Químicas · Ligações iônica, covalente e metálica).
# Habilidade: explicar por que o sódio cede elétron ao cloro e montar a fórmula Al₂O₃ cruzando as cargas dos íons.
# Pré-requisitos: QUI-ATO-006, QUI-ATO-009. Próxima: QUI-LIG-002 (ligação covalente e estrutura de Lewis).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Leituras: Na⁺ = "ene á mais", Cl⁻ = "cê éle menos", Al³⁺ = "á éle três mais", O²⁻ = "ó dois menos", CaF₂ = "cê á éfe dois".
# Fatos: Na (Z 11) = 2, 8, 1; Cl (Z 17) = 2, 8, 7; Al (Z 13) = 2, 8, 3; O (Z 8) = 2, 6; Ca (família 2) → Ca²⁺; F (família 17) → F⁻.
# Um grão de sal (≈ 0,06 mg) tem ≈ 10¹⁸ íons ("bilhões de bilhões"). Contas: 3(+3) + 2(−2) = +5 (erro Al₃O₂); 2(+3) + 3(−2) = 0.

TITULO = "Regra do octeto e ligação iônica"

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
    dict(id="s01", block="gancho", text="{a}O sódio é um metal que reage com violência na água. [p=0.2] {b}O cloro é um gás venenoso. [p=0.3] {c}Juntos, viram o sal do seu feijão. [p=0.3] {d}O que acontece entre eles?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai explicar {b}por que o sódio entrega um elétron ao cloro, [p=0.2] e montar fórmulas como a do {c}óxido de alumínio, á éle dois ó três, [p=0.1] cruzando as cargas. [p=0.2] E ainda leva um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai precisar de três ideias de aulas anteriores. [p=0.2] {a}A camada de valência é a última camada de elétrons do átomo. [p=0.2] {b}Os gases nobres quase não reagem. [p=0.1] Eles têm oito elétrons nessa camada; [p=0.1] só o hélio tem dois. [p=0.2] E {c}os metais tendem a perder elétrons e virar íons positivos; [p=0.1] {d}os ametais, a ganhar e virar íons negativos. [p=0.2] Se alguma travar, procure no canal."),
    # octeto
    dict(id="s04", block="octeto", text="Por que os gases nobres ficam quietos? [p=0.2] {a}Oito elétrons na última camada é uma arrumação estável. [p=0.3] Os outros átomos tendem a chegar lá: [p=0.1] {b}perdendo, ganhando ou dividindo elétrons, [p=0.1] e dividir é assunto da próxima aula. [p=0.3] Essa tendência se chama {c}regra do octeto, [p=0.1] porque octeto quer dizer grupo de oito. [p=0.3] {d}Átomos bem pequenos, como o hidrogênio, se contentam com dois, como o hélio. [p=0.2] {e}A regra tem exceções, que ficam para outra aula."),
    # sódio e cloro
    dict(id="s05", block="troca", text="Veja o sódio, {a}número atômico onze. [p=0.2] Os elétrons ficam {b}dois, oito, um. [p=0.3] Só {c}um elétron na última camada. [p=0.2] Ganhar sete daria muito trabalho. [p=0.2] {d}Perder um é fácil: [p=0.1] {e}a camada de baixo, com oito, vira a última."),
    dict(id="s06", block="troca", text="E o cloro, {a}número atômico dezessete: [p=0.2] {b}dois, oito, sete. [p=0.3] {c}Falta um para os oito. [p=0.3] Quando eles se encontram, {d}o elétron do sódio passa para o cloro. [p=0.3] Cada um fica com {e}oito na última camada."),
    dict(id="s07", block="troca", text="Só que a conta de cargas mudou. [p=0.2] O sódio tem onze prótons e ficou com dez elétrons: [p=0.1] {a}sobra uma carga positiva. [p=0.2] Virou o íon {b}ene á mais. [p=0.3] O cloro tem dezessete prótons e ficou com dezoito elétrons: [p=0.1] {c}sobra uma negativa. [p=0.2] Virou {d}cê éle menos."),
    # ligação iônica
    dict(id="s08", block="ionica", text="{a}Cargas opostas se atraem. [p=0.2] {b}Essa atração entre íons positivos e negativos é a ligação iônica. [p=0.3] Ela acontece entre {c}um metal, que perde elétrons, [p=0.1] e {d}um ametal, que ganha."),
    dict(id="s09", block="ionica", text="E o sal não forma moléculas. [p=0.2] {a}Cada ene á mais fica cercado de cê éle menos. [p=0.1] E cada cê éle menos, de ene á mais. [p=0.2] É uma pilha arrumada, chamada {b}retículo cristalino. [p=0.2] Num grãozinho de sal, são {c}bilhões de bilhões de íons. [p=0.3] Por isso, a fórmula {d}ene á cê éle não conta uma molécula: [p=0.1] {e}ela diz a proporção, um sódio para cada cloro."),
    # cargas diferentes: Al₂O₃
    dict(id="s10", block="cargas", text="E se as cargas forem diferentes? [p=0.2] {a}O alumínio, da família treze, tem três elétrons na última camada e perde os três: [p=0.1] {b}á éle três mais. [p=0.3] {c}O oxigênio, da família dezesseis, tem seis e ganha dois: [p=0.1] {d}ó dois menos."),
    dict(id="s11", block="cargas", text="O composto inteiro precisa ter {a}carga total zero: [p=0.1] o positivo cancela o negativo. [p=0.3] {b}Um alumínio e um oxigênio dão mais três e menos dois: [p=0.1] sobra mais um. [p=0.3] {c}Dois alumínios: três mais três, mais seis. [p=0.2] {d}Três oxigênios: dois mais dois mais dois, menos seis. [p=0.3] Zerou: {e}á éle dois ó três."),
    # erro
    dict(id="s12", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}usar a carga de cada íon como o índice dele mesmo, [p=0.1] e escrever á éle três ó dois. [p=0.3] Confira as cargas: {b}três alumínios, três mais três mais três, dão mais nove. [p=0.1] {c}Dois oxigênios, menos quatro. [p=0.2] {d}Sobra mais cinco: não zerou, está errado."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho de prova é {a}cruzar as cargas: [p=0.2] {b}o número da carga de um vira o índice do outro, sem o sinal. [p=0.3] {c}O três do alumínio desce para o oxigênio, [p=0.1] {d}o dois do oxigênio desce para o alumínio: [p=0.1] {e}á éle dois ó três."),
    dict(id="s14", block="atalho", text="Funciona porque {a}cada lado chega ao mesmo seis: [p=0.1] seis positivos dos alumínios, seis negativos dos oxigênios. [p=0.3] {b}Depois de cruzar, simplifique, se der. [p=0.2] {c}Magnésio dois mais com ó dois menos: cruzando, sai eme gê dois ó dois. [p=0.2] {d}A fórmula iônica usa a menor proporção: eme gê ó, um para um. [p=0.2] Com cargas do mesmo tamanho, nem precisa cruzar."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}O cálcio é da família dois. [p=0.2] {b}O flúor é da família dezessete. [p=0.3] {c}Que íon cada um forma? [p=0.2] E {d}qual é a fórmula do composto entre eles?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Vamos lá. [p=0.2] O cálcio tem {a}dois elétrons na última camada e perde esse par: [p=0.1] cê á dois mais. [p=0.2] {b}O flúor tem sete e ganha um: [p=0.1] éfe menos. [p=0.3] {c}Cruzando: o dois do cálcio desce para o flúor, [p=0.1] o um do flúor desce para o cálcio, [p=0.1] e o um não se escreve. [p=0.2] {d}Cê á éfe dois."),
    dict(id="s18", block="resposta", text="Confira: {a}um cálcio dá mais dois, [p=0.1] {b}dois flúores dão menos dois. [p=0.2] {c}Zero. [p=0.3] Quem escreveu {d}cê á dois éfe usou as cargas sem cruzar."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}os átomos buscam oito elétrons na última camada, [p=0.1] {b}o metal perde, o ametal ganha, [p=0.1] {c}os íons opostos se atraem, [p=0.1] e {d}a fórmula sai cruzando as cargas."),
    dict(id="s20", block="fim", text="Na próxima aula, {a}dois ametais se encontram, e ambos querem ganhar elétrons. [p=0.2] A saída é {b}dividir: a ligação covalente, [p=0.1] desenhada na {c}estrutura de Lewis. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
