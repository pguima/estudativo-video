# Estudativo · QUI-ORG-022 — Esterificação e hidrólise de ésteres (Química · Química Orgânica · Reações orgânicas).
# Habilidade: escrever ácido + álcool → éster + água e o caminho de volta, dando nome ao éster formado.
# Pré-requisitos: QUI-ORG-008. Próxima: QUI-ORG-023 (saponificação e biodiesel).
# Marcas: {cue} animação · [p=0.2] pausa. Fórmulas por extenso; COOH = "cê ó ó agá".
# Fatos: esterificação de Fischer, com ácido forte (H2SO4) como catalisador (catalisador e equilíbrio: outras aulas); a água
# se forma com o OH do ácido e o H do álcool (experiência com oxigênio marcado, 1938). Etanoato de etila: solvente de removedor
# de esmalte e de cola. Butanoato de etila: aroma de abacaxi. Metanoato de etila: aroma lembrando rum e framboesa.
# Ácidos inorgânicos (INO) não estão no "Já ensinado": a aula fala só em "um ácido forte como ajudante".
# Questão inédita: ácido metanoico + etanol → metanoato de etila (HCOOCH2CH3) + água.

TITULO = "Esterificação e hidrólise de ésteres"

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
    dict(id="s01", block="gancho", text="{a}O cheiro de abacaxi de muitas balas não vem do abacaxi. [p=0.3] {b}Vem de uma molécula feita na fábrica, [p=0.2] juntando {c}um ácido com um álcool. [p=0.3] {d}Ela se chama butanoato de etila, e hoje você vai saber fazer e dar nome a ela."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai escrever {b}ácido mais álcool dando éster mais água, [p=0.2] {c}o caminho de volta [p=0.2] e {d}o nome do éster formado. [p=0.2] E ainda leva um {e}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre da aula de funções. [p=0.2] {a}O ácido carboxílico tem o cê ó ó agá. [p=0.2] {b}O álcool tem o ó agá num carbono de ligações simples. [p=0.2] E {c}o éster tem o cê ó ó entre dois carbonos, [p=0.2] com nome terminado em {d}ato de ila, como etanoato de etila."),
    # esterificação
    dict(id="s04", block="ester", text="Na esterificação, {a}um ácido carboxílico reage com um álcool. [p=0.2] {b}Um pouco de ácido sulfúrico ajuda a reação a andar. [p=0.3] {c}Saem duas coisas: o éster [p=0.1] {d}e água."),
    dict(id="s05", block="ester", text="De onde vem a água? [p=0.2] {a}O ó agá sai do ácido. [p=0.2] {b}O hidrogênio sai do ó agá do álcool. [p=0.2] {c}Os dois juntos formam agá dois ó. [p=0.3] {d}O oxigênio que sobrou no álcool se liga ao carbono do ácido, [p=0.2] e {e}nasce a ligação do éster."),
    dict(id="s06", block="ester", text="Com ácido etanoico e etanol: [p=0.2] {a}cê agá três, cê ó ó agá, mais {b}cê agá três, cê agá dois, ó agá, [p=0.2] dão {c}cê agá três, cê ó ó, cê agá dois, cê agá três, [p=0.2] o etanoato de etila, {d}mais água. [p=0.3] {e}É um solvente usado em removedor de esmalte."),
    # nome
    dict(id="s07", block="nome", text="O nome tem duas partes, nesta ordem. [p=0.2] {a}Primeiro, a do ácido: [p=0.1] {b}troque o ico por ato. [p=0.2] {c}Etanoico vira etanoato. [p=0.3] {d}Depois, a do álcool: [p=0.1] {e}troque o anol por ila. [p=0.2] {f}Etanol vira etila. [p=0.3] {g}Juntas, com de no meio: etanoato de etila."),
    # hidrólise
    dict(id="s08", block="volta", text="E o caminho de volta? [p=0.2] {a}Éster mais água dá ácido mais álcool. [p=0.3] É a {b}hidrólise, que quer dizer quebra pela água. [p=0.3] {c}A água quebra a ligação do éster: [p=0.2] {d}o ó agá vai para o lado do ácido, {e}e o hidrogênio vai para o lado do álcool. [p=0.3] {f}A reação vai e volta, e por isso a seta tem duas pontas."),
    # erro
    dict(id="s09", block="erro", text="O erro mais comum é {a}trocar a ordem do nome. [p=0.3] {b}Butanoato de etila vem do ácido butanoico com o etanol: [p=0.1] é o do abacaxi. [p=0.3] {c}Etanoato de butila vem do ácido etanoico com o butanol: [p=0.2] {d}é outra substância, com outro cheiro. [p=0.3] {e}A primeira palavra é sempre a do ácido."),
    # atalho
    dict(id="s10", block="atalho", text="O atalho para escrever o éster: [p=0.2] {a}pegue a fórmula do ácido [p=0.2] e {b}troque o hidrogênio do cê ó ó agá pela cadeia do álcool. [p=0.3] {c}Ácido etanoico com etanol: cê agá três, cê ó ó, e no lugar do agá, cê agá dois, cê agá três. [p=0.3] Funciona porque {d}o éster é o ácido com o grupo do álcool no lugar daquele hidrogênio."),
    dict(id="s11", block="atalho", text="{a}Na volta, faça ao contrário: [p=0.2] {b}corte entre o cê dupla ó e o oxigênio vizinho. [p=0.2] {c}O lado do cê dupla ó ganha um ó agá e vira o ácido. [p=0.2] {d}O oxigênio fica no outro lado, ganha um hidrogênio, e vira o álcool."),
    # questão
    dict(id="s12", block="questao", text="Hora de testar. [p=0.2] O ácido metanoico, {a}agá cê ó ó agá, [p=0.2] reage com o etanol. [p=0.3] {b}Qual é a fórmula do éster? [p=0.2] {c}E qual é o nome dele?"),
    dict(id="s13", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s14", block="resposta", text="Pelo atalho: [p=0.2] {a}troque o hidrogênio do cê ó ó agá pela cadeia do etanol. [p=0.3] {b}Fica agá cê ó ó, cê agá dois, cê agá três, [p=0.2] e {c}sai uma água."),
    dict(id="s15", block="resposta", text="O nome: [p=0.2] {a}metanoico vira metanoato, [p=0.2] {b}etanol vira etila. [p=0.3] {c}Metanoato de etila, [p=0.2] um aroma que lembra rum e framboesa."),
    # fechamento
    dict(id="s16", block="fim", text="Resumindo: [p=0.1] {a}ácido mais álcool dá éster mais água. [p=0.2] {b}A hidrólise é o caminho de volta. [p=0.2] E {c}o nome do éster é ato, do ácido, de ila, do álcool."),
    dict(id="s17", block="fim", text="Na próxima aula, a gordura também é um éster: [p=0.2] {a}com uma base, ela vira sabão, [p=0.2] e {b}com um álcool, vira biodiesel. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
