# Estudativo · QUI-LIG-012 — Praticando: polaridade e forças intermoleculares (Química · Ligações Químicas · prática).
# Habilidade: prever solubilidade e ponto de ebulição a partir da estrutura da molécula.
# Pré-requisitos: QUI-LIG-006 a QUI-LIG-011. Próxima no curso: QUI-INO-007 (ler uma equação: conservação das massas).
# Questões inéditas, criadas para esta aula. Leituras: CCl₄ = "cê cê éle quatro", CHCl₃ = "cê agá cê éle três", C₂H₆O = "cê dois agá seis ó".
# Fatos: CH₄ e CHCl₃ tetraédricos; CH₄ apolar, CHCl₃ polar; vitamina C (C₆H₈O₆, quatro O–H) hidrossolúvel, perde-se na água
# do cozimento; vitamina A (retinol, C₂₀H₃₀O, um O–H para 20 carbonos) lipossolúvel, absorvida com gordura;
# PE etanol 78 °C, éter dimetílico −24 °C (mesma fórmula C₂H₆O); éter: O angular com pares livres → polar (dipolo permanente);
# Q4: I₂ apolar → cor vai para o óleo; PE Br₂ 59 °C (58,8), I₂ 184 °C: mesma força (dipolo induzido), I₂ maior.

TITULO = "Praticando: polaridade e forças intermoleculares"

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
    dict(id="s01", block="gancho", text="{a}Quatro questões, criadas para esta aula, [p=0.2] sobre {b}forma, polaridade e forças entre moléculas. [p=0.3] Em cada uma, {c}pause o vídeo e resolva antes de ver a resposta. [p=0.2] Errar aqui não custa nada, e ensina mais do que só assistir."),
    # lembrete
    dict(id="s02", block="lembrete", text="O caminho é quase sempre o mesmo: [p=0.2] {a}desenhe a estrutura de Lewis, [p=0.1] {b}ache a geometria, [p=0.1] {c}decida se é polar [p=0.1] e {d}descubra a força entre as moléculas. [p=0.3] {e}Daí saem a solubilidade e o ponto de ebulição. [p=0.2] Se alguma etapa travar, procure a aula no canal."),
    # questão 1
    dict(id="s03", block="questao1", text="{a}Questão um. [p=0.2] {b}O metano, cê agá quatro, é o principal gás do gás natural. [p=0.1] {c}O clorofórmio, cê agá cê éle três, já foi muito usado como solvente. [p=0.3] {d}Qual é a geometria de cada um, e quem é polar?"),
    dict(id="s04", block="questao1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="resposta1", text="Vamos lá. [p=0.2] {a}Nas duas moléculas, o carbono faz quatro ligações simples e não tem par livre: [p=0.1] {b}quatro ligantes, tetraédrica. [p=0.3] {c}No metano, os ligantes são iguais, e as setas se cancelam. [p=0.1] Apolar. [p=0.3] {d}No clorofórmio, um dos ligantes é hidrogênio, e três são cloros. [p=0.1] {e}Os cloros puxam mais de um lado, e sobra puxão. [p=0.1] Polar."),
    # questão 2
    dict(id="s06", block="questao2", text="{a}Questão dois. [p=0.2] {b}A vitamina C tem vários grupos ó agá, um oxigênio preso a um hidrogênio, como na água. [p=0.2] {c}A vitamina A é quase toda de carbono e hidrogênio, com um ó agá só. [p=0.3] {d}Qual delas se perde na água em que o legume é cozido? [p=0.2] E {e}por que a vitamina A é mais bem aproveitada quando a refeição tem um pouco de gordura?"),
    dict(id="s07", block="questao2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="resposta2", text="Vamos lá. [p=0.2] {a}Muitos ó agá: a vitamina C é polar. [p=0.1] {b}Ela se dissolve na água do cozimento, e vai embora com ela. [p=0.3] {c}A vitamina A tem um ó agá para vinte carbonos: [p=0.1] {d}a parte apolar vence. [p=0.2] {e}Ela se dissolve na gordura, que também é apolar: [p=0.1] semelhante dissolve semelhante."),
    # questão 3
    dict(id="s09", block="questao3", text="{a}Questão três. [p=0.2] {b}O etanol e o éter dimetílico têm a mesma fórmula, cê dois agá seis ó. [p=0.3] {c}No etanol, o oxigênio está preso a um hidrogênio. [p=0.1] {d}No éter, ele fica entre dois carbonos. [p=0.3] {e}Qual ferve mais alto, e por quê?"),
    dict(id="s10", block="questao3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s11", block="resposta3", text="Vamos lá, força primeiro. [p=0.2] {a}Etanol: hidrogênio preso a oxigênio. [p=0.1] Ligação de hidrogênio. [p=0.3] {b}Éter: nenhum hidrogênio no oxigênio. [p=0.1] {c}Mas o oxigênio tem pares livres e fica num ângulo: a molécula é polar. [p=0.1] Dipolo permanente. [p=0.3] {d}Mesmo tamanho, força diferente: o etanol ferve mais alto. [p=0.2] {e}Setenta e oito graus, contra vinte e quatro negativos do éter."),
    # atalho
    dict(id="s12", block="atalho", text="Aqui cabe um atalho. [p=0.2] {a}Fórmula igual não diz qual ferve mais alto: [p=0.1] {b}olhe a estrutura e procure ó agá, ene agá ou agá éfe. [p=0.3] {c}Achou? Ligação de hidrogênio, ponto de ebulição mais alto. [p=0.3] Funciona porque, {d}com o mesmo tamanho, quem decide é a força. [p=0.2] {e}Não compensa se os tamanhos forem muito diferentes: [p=0.1] aí, o tamanho também pesa."),
    # questão 4
    dict(id="s13", block="questao4", text="{a}Última questão. [p=0.2] {b}Ponha um pouco de iodo, i dois, num copo com água e uma camada de óleo por cima, e agite. [p=0.3] {c}Em qual camada a cor do iodo fica? [p=0.2] E {d}quem ferve mais alto: o iodo ou o bromo, bê érre dois, da mesma família?"),
    dict(id="s14", block="questao4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s15", block="resposta4", text="Vamos lá. [p=0.2] {a}Iodo: átomos iguais, molécula apolar. [p=0.1] {b}Semelhante dissolve semelhante: a cor vai para o óleo, que também é apolar. [p=0.3] {c}Para ferver, os dois têm a mesma força: dipolo induzido. [p=0.2] {d}Empate na força, desempate no tamanho: o iodo é maior. [p=0.2] {e}O iodo ferve a cento e oitenta e quatro graus; [p=0.1] o bromo, a cinquenta e nove."),
    # fechamento
    dict(id="s16", block="fim", text="Resumindo: [p=0.1] {a}da estrutura sai a forma, [p=0.1] {b}da forma sai a polaridade, [p=0.1] {c}da polaridade saem a solubilidade e a força, [p=0.1] e {d}da força sai o ponto de ebulição."),
    dict(id="s17", block="fim", text="Com isso, você fecha a trilha de ligações químicas. [p=0.2] Na próxima aula do curso, {a}as reações começam: [p=0.1] {b}você vai ler uma equação química e ver que a massa se conserva. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
