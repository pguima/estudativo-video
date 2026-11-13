# Estudativo · QUI-AMB-004 — Tratamento de água (Química · Química e Ambiente · Tratamento de água e química verde).
# Habilidade: colocar em ordem coagulação, floculação, decantação, filtração, cloração e fluoretação, dizendo a química de
# cada etapa.
# Pré-requisitos: QUI-MIS-007, QUI-INO-005, QUI-INO-011. Próxima: QUI-AMB-005 (esgoto, DBO e oxigênio dissolvido).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fórmulas faladas: Al₂(SO₄)₃ "sulfato de alumínio", Ca(OH)₂ "hidróxido de cálcio", Al(OH)₃ "á éle ó agá três",
# Cl₂ "cê éle dois", HClO "agá cê éle ó", HCl "agá cê éle".
# Química: Al₂(SO₄)₃ + 3 Ca(OH)₂ → 2 Al(OH)₃ + 3 CaSO₄ (dupla troca; Al(OH)₃ é o precipitado gelatinoso);
# Cl₂ + H₂O → HCl + HClO (o ácido hipocloroso desinfeta); flúor em pequena dose fortalece o esmalte e previne cárie;
# a cal corrige o pH, porque o sulfato de alumínio deixa a água ácida; o filtro tem areia, cascalho e carvão.
# SOL-001 (coloide) e ppm não estão em "Já ensinado": a sujeira fina é "partícula fina demais para decantar".

TITULO = "Tratamento de água"

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
    dict(id="s01", block="gancho", text="{a}A água chega do rio barrenta, com terra, folhas e micróbios. [p=0.3] {b}Horas depois, sai limpa na sua torneira. [p=0.3] {c}No caminho, ela ganha um produto que junta a sujeira, [p=0.1] {d}cloro que mata os germes [p=0.1] {e}e até flúor para os seus dentes."),
    dict(id="s02", block="gancho", text="{a}Nesta aula, você vai pôr em ordem {b}as seis etapas do tratamento [p=0.2] e {c}dizer a química de cada uma."),
    # lembrete
    dict(id="s03", block="lembrete", text="Três lembretes. [p=0.2] {a}Na decantação, o sólido mais denso desce sozinho. [p=0.3] {b}Na dupla troca, pode se formar um precipitado: um sólido que não dissolve. [p=0.3] {c}E pê agá abaixo de sete é ácido."),
    # problema
    dict(id="s04", block="problema", text="O primeiro problema é que {a}boa parte do barro do rio é fina demais. [p=0.3] {b}As partículas são tão pequenas e leves que ficam boiando por dias, sem descer. [p=0.3] {c}Decantar direto não adianta: é preciso juntá-las antes."),
    # coagulação
    dict(id="s05", block="coagula", text="{a}Primeira etapa: coagulação. [p=0.3] {b}A estação de tratamento põe sulfato de alumínio [p=0.1] {c}e cal, que dá hidróxido de cálcio na água. [p=0.3] {d}Os dois fazem uma dupla troca."),
    dict(id="s06", block="coagula", text="{a}Um dos produtos é o hidróxido de alumínio, á éle ó agá três. [p=0.2] {b}Ele não dissolve: é um precipitado gelatinoso, como uma geleia grudenta espalhada na água. [p=0.3] {c}E a cal ainda corrige o pê agá, porque o sulfato de alumínio deixaria a água ácida."),
    # floculação
    dict(id="s07", block="flocula", text="{a}Segunda etapa: floculação. [p=0.3] {b}A água é mexida devagar, por um bom tempo. [p=0.2] {c}A geleia de á éle ó agá três vai grudando nas partículas de barro [p=0.1] {d}e formando flocos cada vez maiores e mais pesados."),
    # decantação e filtração
    dict(id="s08", block="separa", text="{a}Terceira etapa: decantação. [p=0.2] {b}A água entra em tanques enormes e fica quase parada. [p=0.3] {c}Agora os flocos são pesados: descem e formam um lodo no fundo."),
    dict(id="s09", block="separa", text="{a}Quarta etapa: filtração. [p=0.2] {b}A água de cima passa por camadas de areia, cascalho e carvão. [p=0.3] {c}Elas seguram os flocos pequenos que não desceram, [p=0.1] {d}e o carvão ainda ajuda a tirar cheiro e gosto."),
    # cloração e fluoretação
    dict(id="s10", block="protege", text="{a}Quinta etapa: cloração. [p=0.2] A água está limpa, mas ainda pode ter micróbios. [p=0.3] {b}O cloro, cê éle dois, reage com a água [p=0.1] {c}e forma ácido clorídrico e ácido hipocloroso, agá cê éle ó. [p=0.3] {d}É o ácido hipocloroso que mata os germes."),
    dict(id="s11", block="protege", text="{a}Um pouco de cloro fica na água de propósito: [p=0.1] {b}ele protege a água nos quilômetros de cano até a sua casa. [p=0.3] {c}Sexta etapa: fluoretação. [p=0.2] {d}Uma dose pequena de um composto de flúor fortalece o esmalte dos dentes [p=0.1] {e}e diminui as cáries."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho de prova para a ordem são três verbos: {a}juntar, tirar, proteger. [p=0.3] {b}Juntar a sujeira: coagulação e floculação. [p=0.2] {c}Tirar a sujeira: decantação e filtração. [p=0.2] {d}Proteger a água e você: cloração e fluoretação."),
    dict(id="s13", block="atalho", text="Funciona porque {a}cada etapa prepara a próxima. [p=0.2] {b}Sem flocos, nada decanta. [p=0.2] {c}E o cloro vem depois da limpeza porque a sujeira gastaria o cloro antes dos germes. [p=0.3] {d}Algumas estações põem cloro também no começo, mas a prova costuma cobrar a ordem padrão."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}chamar a água tratada de água pura. [p=0.3] {b}Ela é potável, ou seja, boa para beber. [p=0.2] {c}Mas é uma mistura: tem cloro, flúor e sais dissolvidos. [p=0.3] {d}Água pura, para a Química, só tem agá dois ó, e quase não existe na natureza."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] {a}Ponha em ordem: filtração, cloração, floculação, coagulação, fluoretação e decantação. [p=0.3] {b}E diga em qual etapa se forma o á éle ó agá três."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Use os três verbos. [p=0.2] {a}Juntar: coagulação, depois floculação. [p=0.2] {b}Tirar: decantação, depois filtração. [p=0.2] {c}Proteger: cloração, depois fluoretação."),
    dict(id="s18", block="resposta", text="{a}O á éle ó agá três se forma na coagulação, [p=0.1] quando o sulfato de alumínio encontra a cal. [p=0.3] {b}Quem pôs a floculação primeiro esqueceu que, sem o á éle ó agá três, não há o que grude."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}coagular e flocular juntam a sujeira; [p=0.2] {b}decantar e filtrar tiram; [p=0.2] {c}clorar e fluoretar protegem. [p=0.3] {d}Juntar, tirar, proteger."),
    dict(id="s20", block="fim", text="Na próxima aula, a água faz o caminho contrário: [p=0.2] {a}o esgoto, a falta de oxigênio nos rios e uma medida chamada dê bê ó. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
