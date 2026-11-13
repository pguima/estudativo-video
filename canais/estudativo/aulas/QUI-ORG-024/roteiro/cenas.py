# Estudativo · QUI-ORG-024 — Praticando: reações orgânicas (Química · Química Orgânica · prática).
# Habilidade: prever o produto e o tipo de reação em processos industriais e do corpo humano.
# Pré-requisitos: QUI-ORG-018 a QUI-ORG-023. Próxima: QUI-ORG-025 (polímeros de adição).
# Questões inéditas, criadas para esta aula. Marcas: {cue} animação · [p=0.2] pausa. Fórmulas por extenso.
# Fatos: margarina = hidrogenação parcial de óleo com níquel; no fígado, a enzima álcool desidrogenase oxida o etanol a etanal
# (acetaldeído), que contribui para o mal-estar da ressaca; nitrobenzeno é matéria-prima da anilina, base de corantes;
# plástico verde: etanol da cana → eteno (desidratação); na digestão, a lipase quebra os ésteres da gordura com água
# (hidrólise), soltando ácidos graxos e glicerol.

TITULO = "Praticando: reações orgânicas"

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
    dict(id="s01", block="gancho", text="{a}Cinco situações, criadas para esta aula, [p=0.2] {b}da fábrica e do corpo humano. [p=0.3] Em cada uma, você diz {c}que reação acontece e o que se forma. [p=0.3] {d}Pause o vídeo e resolva antes de ver a resposta."),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar {a}adição, [p=0.1] {b}substituição, [p=0.1] {c}eliminação, [p=0.1] {d}oxidação [p=0.1] e {e}a esterificação com o caminho de volta, a hidrólise, e a saponificação. [p=0.3] Se alguma travar, procure a aula no canal."),
    # 1: margarina
    dict(id="s03", block="questao1", text="{a}Situação um. [p=0.2] {b}Uma fábrica aquece óleo de soja com gás hidrogênio e níquel, [p=0.2] {c}e o óleo líquido vira uma gordura pastosa. [p=0.3] {d}Que reação é essa, e o que acontece com as ligações duplas?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="{a}Entra agá dois nas duplas, e nada sai. [p=0.2] {b}É uma adição, a hidrogenação. [p=0.3] {c}Parte das duplas vira ligação simples, [p=0.2] e {d}a gordura fica mais firme: é a margarina."),
    # 2: fígado
    dict(id="s06", block="questao2", text="{a}Situação dois. [p=0.2] {b}No fígado, o etanol da bebida vira etanal, [p=0.2] {c}uma das substâncias ligadas ao mal-estar da ressaca. [p=0.3] {d}O etanol é álcool primário. [p=0.2] {e}Que reação é essa, e o que o etanal vira se ela continuar?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="{a}O carbono do ó agá perde hidrogênio e ganha a dupla cê ó: [p=0.2] {b}é uma oxidação. [p=0.3] {c}Álcool primário vira aldeído, o etanal, [p=0.2] e {d}se a oxidação continua, vira ácido etanoico, o ácido acético."),
    # 3: nitração
    dict(id="s09", block="questao3", text="{a}Situação três. [p=0.2] {b}Uma indústria de corantes mistura benzeno com ácido nítrico, [p=0.2] com um pouco de ácido sulfúrico. [p=0.3] {c}Que reação acontece, e qual é o produto orgânico?"),
    dict(id="s10", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s11", block="resposta3", text="{a}O anel do benzeno não abre: [p=0.1] ele troca. [p=0.2] {b}Sai um hidrogênio, entra o grupo nitro. [p=0.3] {c}É uma substituição, a nitração. [p=0.2] {d}O produto é o nitrobenzeno, [p=0.1] {e}e sai água."),
    # atalho
    dict(id="s12", block="atalho", text="Antes das duas últimas, o atalho para dar nome a qualquer reação: [p=0.2] {a}compare o antes e o depois. [p=0.3] {b}Sumiu uma dupla e nada saiu? [p=0.1] Adição. [p=0.2] {c}Apareceu uma dupla e saiu uma molécula pequena? [p=0.1] Eliminação. [p=0.2] {d}Um átomo ou um grupo trocou de lugar com um hidrogênio? [p=0.1] Substituição."),
    dict(id="s13", block="atalho", text="{a}O carbono perdeu hidrogênio e ganhou ligação com oxigênio? [p=0.1] Oxidação. [p=0.2] {b}Apareceu um éster e saiu água? [p=0.1] Esterificação. [p=0.2] {c}O éster quebrou com água? [p=0.1] Hidrólise. [p=0.2] Com uma base, virando sal? [p=0.1] Saponificação. [p=0.3] {d}Funciona porque cada tipo deixa uma marca na fórmula."),
    # 4: plástico verde
    dict(id="s14", block="questao4", text="{a}Situação quatro. [p=0.2] {b}Uma usina aquece o etanol da cana a cerca de cento e setenta graus, com ácido sulfúrico. [p=0.3] {c}Sai um gás que vira plástico, [p=0.2] e sai água. [p=0.3] {d}Que reação é essa, e qual é o gás?"),
    dict(id="s15", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="resposta4", text="{a}Saiu uma molécula pequena, a água, [p=0.2] e {b}apareceu uma dupla entre os carbonos. [p=0.3] {c}É uma eliminação, a desidratação do etanol. [p=0.2] {d}O gás é o eteno, cê agá dois, dupla, cê agá dois."),
    # 5: digestão
    dict(id="s17", block="questao5", text="{a}Situação cinco. [p=0.2] {b}No intestino, uma enzima quebra a gordura da comida com água, [p=0.2] {c}soltando ácidos graxos e glicerol. [p=0.3] {d}Lembre que a gordura é um triéster. [p=0.2] {e}Que reação é essa?"),
    dict(id="s18", block="questao5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s19", block="resposta5", text="{a}O éster quebrou com água, [p=0.2] {b}e saíram um ácido e um álcool: os ácidos graxos e o glicerol. [p=0.3] {c}É uma hidrólise, o caminho de volta da esterificação."),
    # fechamento
    dict(id="s20", block="fim", text="{a}Se você acertou três ou mais, o módulo está firme. [p=0.2] Se não, reveja a aula da reação que travou. [p=0.3] Na próxima aula, a adição faz {b}moléculas gigantes: [p=0.2] {c}os polímeros, como o plástico da sacolinha. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
