# Estudativo · QUI-ORG-008 — Ácido carboxílico e éster (Química · Química Orgânica · Funções orgânicas).
# Habilidade: reconhecer COOH e COO, nomear ácido etanoico e etanoato de etila e dizer por que ésteres dão aroma às frutas.
# Pré-requisitos: QUI-ORG-007 (carbonila, aldeído). Próxima: QUI-ORG-009 (amina, amida e nitrila).
# Marcas: {cue} animação · [p=0.2] pausa. COOH = "cê ó ó agá"; COO = "cê ó ó".
# Fatos: ácido etanoico = ácido acético (vinagre, 4 a 6%); ácido metanoico = fórmico (formiga); etanoato de etila: cheiro frutado,
# usado em removedor de esmalte; ésteres de banana (etanoato de isoamila), abacaxi (butanoato de etila), laranja (etanoato de octila);
# frutas produzem ésteres ao amadurecer; ésteres pequenos são voláteis (o porquê, forças intermoleculares, fica para outra aula);
# a esterificação (ácido + álcool) fica para outra aula. Questão: ácido propanoico CH3–CH2–COOH; etanoato de metila CH3–COO–CH3.
# Questão inédita, criada para esta aula.

TITULO = "Ácido carboxílico e éster"

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
    dict(id="s01", block="gancho", text="{a}O vinagre é azedo [p=0.1] {b}e a banana é perfumada. [p=0.3] {c}Por trás dos dois, há quase o mesmo grupo de átomos. [p=0.2] {d}A diferença está no que ocupa o lugar de um agá."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai reconhecer {b}o grupo do ácido e {c}o do éster, [p=0.2] dar nome ao {d}ácido etanoico e ao {e}etanoato de etila, [p=0.2] e entender {f}por que o éster tem cheiro de fruta."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula passada: [p=0.2] {a}a carbonila é o cê, dupla, ó. [p=0.2] {b}Na ponta, com agá, ela forma o aldeído. [p=0.2] {c}E, da aula de álcool, fenol e éter: [p=0.1] o éter é um oxigênio entre dois carbonos."),
    # ácido carboxílico
    dict(id="s04", block="acido", text="{a}Troque o agá do aldeído por um ó agá. [p=0.2] {b}No mesmo carbono, ficam a carbonila e o ó agá: [p=0.1] {c}é o grupo carboxila, cê ó ó agá. [p=0.3] {d}Quem tem esse grupo é um ácido carboxílico."),
    dict(id="s05", block="acido", text="{a}O nome começa com a palavra ácido, [p=0.1] e o ó do fim vira oico. [p=0.3] {b}Dois carbonos: [p=0.1] {c}ácido etanoico. [p=0.2] {d}É o ácido acético, que deixa o vinagre azedo. [p=0.3] {e}Com um carbono só, é o ácido metanoico, o da picada da formiga."),
    # éster
    dict(id="s06", block="ester", text="{a}Agora, troque o agá do ó agá por um carbono. [p=0.2] {b}Fica cê ó ó, com uma cadeia de cada lado. [p=0.3] {c}É o éster. [p=0.2] {d}Ele se forma de um ácido com um álcool, [p=0.1] mas essa reação fica para outra aula."),
    dict(id="s07", block="ester", text="{a}O nome do éster tem duas partes. [p=0.2] {b}O lado da carbonila vem do ácido, com oico trocado por ato: [p=0.1] {c}de ácido etanoico, etanoato. [p=0.3] {d}O lado do outro oxigênio leva o prefixo dos seus carbonos, mais ila: [p=0.1] {e}dois carbonos, et mais ila, etila. [p=0.3] {f}Etanoato de etila."),
    # aroma
    dict(id="s08", block="aroma", text="{a}O etanoato de etila tem cheiro de fruta e aparece no removedor de esmalte. [p=0.3] {b}Outros ésteres dão o aroma da banana, [p=0.1] {c}do abacaxi [p=0.1] {d}e da laranja. [p=0.2] {e}As frutas fabricam esses ésteres quando amadurecem."),
    dict(id="s09", block="aroma", text="{a}Mas por que eles têm cheiro? [p=0.2] {b}Para você sentir um cheiro, as moléculas precisam sair do líquido e chegar ao nariz. [p=0.3] {c}Os ésteres pequenos evaporam com muita facilidade, [p=0.1] {d}e o nariz é muito sensível a eles. [p=0.3] {e}Por que eles evaporam tão fácil é assunto de outra aula, a das forças entre moléculas."),
    # erro comum
    dict(id="s10", block="erro", text="{a}O erro mais comum é trocar éster por éter, [p=0.1] porque os nomes são quase iguais. [p=0.3] {b}O éter é cê, ó, cê: [p=0.1] um oxigênio só, entre carbonos. [p=0.2] {c}O éster tem a carbonila colada: [p=0.1] cê ó ó, dois oxigênios."),
    # atalho
    dict(id="s11", block="atalho", text="{a}O atalho: [p=0.1] no carbono da carbonila, ache o segundo oxigênio. [p=0.2] {b}Com agá, é ácido. [p=0.2] {c}Com carbono, é éster. [p=0.3] {d}E, para dar o nome do éster, corte no oxigênio simples: [p=0.1] {e}o lado da carbonila é o ato, [p=0.1] {f}o outro lado é o ila."),
    dict(id="s12", block="atalho", text="{a}Funciona porque o éster é o ácido com um carbono no lugar do agá: [p=0.1] a parte que veio do ácido guarda a carbonila. [p=0.3] {b}Cuidado quando o éster vem escrito ao contrário, com o oxigênio simples à esquerda: [p=0.1] {c}procure primeiro a carbonila, e o resto se encaixa."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] {a}Diga a função de cada molécula, ácido ou éster, [p=0.2] {b}e dê o nome de cada uma."),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s15", block="resposta", text="{a}A primeira tem a carbonila com ó agá: ácido. [p=0.2] {b}São três carbonos: [p=0.1] {c}ácido propanoico."),
    dict(id="s16", block="resposta", text="{a}A segunda tem a carbonila e um ó com carbono: éster. [p=0.2] {b}Corte no oxigênio simples. [p=0.1] {c}O lado da carbonila tem dois carbonos: etanoato. [p=0.2] {d}O outro lado tem um: metila. [p=0.2] {e}Etanoato de metila."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: [p=0.1] {a}cê ó ó agá é o ácido, com oico. [p=0.2] {b}Cê ó ó com carbono dos dois lados é o éster, com ato e ila. [p=0.2] {c}E os ésteres pequenos evaporam fácil, por isso têm cheiro."),
    dict(id="s18", block="fim", text="Na próxima aula, entra o nitrogênio: [p=0.2] {a}amina, amida e nitrila, [p=0.1] e {b}a amida escondida num remédio. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
