# Estudativo · QUI-ORG-028 — Praticando: polímeros (Química · Química Orgânica · prática). Última aula da trilha.
# Habilidade: identificar monômeros, tipo de polímero e destino dos plásticos em questões de prova.
# Pré-requisitos: QUI-ORG-025, QUI-ORG-026, QUI-ORG-027. Próxima: nenhuma (fim da trilha de Química Orgânica).
# Questões inéditas, criadas para esta aula. Marcas: {cue} animação · [p=0.2] pausa. Fórmulas por extenso.
# Fatos: PVC = [–CH2–CHCl–]n, monômero cloreto de vinila CH2=CHCl. Kevlar (DuPont, 1965, Stephanie Kwolek) = poliamida de
# ácido tereftálico com 1,4-diaminobenzeno, usada em coletes à prova de bala; sai água (na indústria, HCl, com cloreto de
# ácido: fica fora da aula). Copo de isopor (PS, código 6) e garrafa PET (código 1): termoplásticos; tomada de baquelite:
# termofixo. Amido e celulose: glicose; o corpo humano digere o amido; a celulose é a fibra que passa sem ser digerida.

TITULO = "Praticando: polímeros"

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
    dict(id="s01", block="gancho", text="{a}Quatro situações, criadas para esta aula, [p=0.2] {b}com plásticos, fibras e comida. [p=0.3] Em cada uma, {c}pause o vídeo e resolva antes de ver a resposta. [p=0.3] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}polímero de adição, [p=0.2] {b}polímero de condensação [p=0.2] e {c}termoplástico e termofixo. [p=0.3] Se alguma travar, procure a aula no canal."),
    # 1: PVC
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] O cano de pê vê cê tem esta unidade: [p=0.2] {b}cê agá dois, cê agá com cloro, entre colchetes, com o ene. [p=0.3] {c}Qual é o monômero, [p=0.1] e {d}que tipo de polímero é esse?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="{a}Na unidade, não há éster nem amida: [p=0.1] {b}é polímero de adição. [p=0.3] Pelo atalho, {c}devolva a dupla entre os dois carbonos: [p=0.2] {d}cê agá dois, dupla, cê agá com cloro, [p=0.2] {e}o cloreto de vinila."),
    # 2: Kevlar
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] {b}O kevlar, a fibra dos coletes à prova de bala, [p=0.2] tem um cê ó ene agá que se repete, entre anéis de benzeno. [p=0.3] {c}Que tipo de polímero é, [p=0.1] {d}que grupo é esse [p=0.1] {e}que molécula sai quando ele se forma, [p=0.1] e de que monômeros ele vem?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="{a}O cê ó ligado ao ene agá é uma amida: [p=0.2] {b}o kevlar é uma poliamida, como o náilon. [p=0.3] {c}É polímero de condensação, [p=0.1] {d}e a cada amida formada sai uma água. [p=0.3] {e}Os monômeros: o ácido tereftálico, o mesmo do PET, com cê ó ó agá nas duas pontas, [p=0.2] e uma amina com ene agá dois nas duas pontas de um anel."),
    # atalho
    dict(id="s09", block="atalho", text="Antes das duas últimas, o atalho que resolve quase toda questão de polímero: [p=0.2] {a}olhe a unidade que se repete. [p=0.3] {b}A cadeia principal é só de carbonos? [p=0.1] Adição: devolva a dupla. [p=0.3] {c}Tem oxigênio ou nitrogênio ligando as unidades, como no éster, na amida ou entre as glicoses? [p=0.1] Condensação: corte ali e devolva a água."),
    dict(id="s10", block="atalho", text="{a}E para o destino do plástico, uma pergunta só: [p=0.2] {b}amolece no calor? [p=0.2] {c}Então é termoplástico, e recicla por fusão."),
    # 3: lixo
    dict(id="s11", block="questao3", text="{a}Situação três. [p=0.2] Na esteira da reciclagem passam {b}um copo de isopor, [p=0.2] {c}uma garrafa PET [p=0.2] e {d}uma tomada velha de baquelite. [p=0.3] {e}Quais podem ser derretidos e moldados de novo?"),
    dict(id="s12", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s13", block="resposta3", text="{a}O isopor é poliestireno, [p=0.1] número seis: [p=0.1] termoplástico. [p=0.2] {b}O PET, número um: [p=0.1] termoplástico. [p=0.3] {c}Os dois amolecem no calor e se reciclam por fusão. [p=0.3] {d}A baquelite é termofixo: [p=0.1] {e}não amolece, e fica de fora."),
    # 4: amido e celulose
    dict(id="s14", block="questao4", text="{a}Situação quatro. [p=0.2] {b}O arroz tem amido. [p=0.1] {c}A folha de alface tem celulose. [p=0.3] {d}Os dois são polímeros do mesmo monômero. [p=0.2] {e}Qual é esse monômero, [p=0.1] e {f}qual dos dois o nosso corpo digere?"),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="{a}O monômero dos dois é a glicose. [p=0.3] {b}O corpo digere o amido, e a glicose vira energia. [p=0.2] {c}A celulose, ligada de outro jeito, passa sem ser digerida: [p=0.2] {d}é a fibra da alimentação."),
    # fechamento
    dict(id="s17", block="fim", text="{a}Se você acertou três ou mais, o módulo de polímeros está firme. [p=0.2] Se não, reveja a aula da questão que travou. [p=0.3] {b}Com esta aula, você fechou a trilha de Química Orgânica, [p=0.2] {c}das fórmulas do carbono até os plásticos. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
