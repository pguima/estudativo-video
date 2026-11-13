# Estudativo · QUI-LIG-010 — Comparar pontos de ebulição (Química · Ligações Químicas · Polaridade e forças intermoleculares).
# Habilidade: ordenar substâncias pelo ponto de ebulição olhando primeiro a força e depois o tamanho e explicar por que a água
# ferve muito acima do H₂S.
# Pré-requisitos: QUI-LIG-009. Próxima: QUI-LIG-011 (gelo que boia e inseto sobre a água).
# Atenção: QUI-MIS-003 (estados físicos) NÃO está em "Já ensinado": "ponto de ebulição" é explicado na hora. Sem "massa molar".
# Marcas: {cue} animação · [p=0.2] pausa. Questão inédita, criada para esta aula.
# PE a 1 atm (°C): CH₄ −161; HCl −85; H₂O 100; H₂S −60; H₂Se −41; H₂Te −2; propano −42; octano 126 (125,6); F₂ −188; HF 20 (19,5).
# Massas: H₂O 18, H₂S 34 (≈ o dobro); elétrons: F₂ 18, HCl 18, HF 10 ("tamanhos parecidos"). Diferença H₂O − H₂S = 160 °C.
# Pela tendência H₂Te → H₂Se → H₂S, a água ferveria perto de −80 °C (valor de livro: −80 a −90 °C; conferir).

TITULO = "Comparar pontos de ebulição"

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
    dict(id="s01", block="gancho", text="{a}O agá dois esse, o gás com cheiro de ovo podre, tem molécula maior e quase duas vezes mais pesada que a da água. [p=0.3] {b}Mesmo assim, ele ferve a sessenta graus negativos. [p=0.2] {c}A água, a cem. [p=0.3] {d}São cento e sessenta graus de diferença, a favor da molécula menor."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}ordenar substâncias pelo ponto de ebulição, [p=0.1] {c}olhando primeiro a força e depois o tamanho. [p=0.2] E vai explicar {d}o caso da água."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula anterior: [p=0.1] {a}a força mais fraca entre moléculas é o dipolo induzido, [p=0.1] {b}a do meio é o dipolo permanente, [p=0.1] e {c}a mais forte, a ligação de hidrogênio, com hidrogênio preso a éfe, ó ou ene. [p=0.2] Se faltar essa aula, procure no canal."),
    # ponto de ebulição
    dict(id="s04", block="ebulicao", text="{a}Ponto de ebulição é a temperatura em que o líquido ferve e vira gás, ou vapor: [p=0.1] as moléculas ficam soltas e afastadas. [p=0.2] {b}Para ferver, as moléculas precisam se soltar umas das outras. [p=0.3] {c}Quanto mais forte a força entre elas, [p=0.1] {d}mais calor é preciso, [p=0.1] e mais alto o ponto de ebulição."),
    # passo 1
    dict(id="s05", block="passo1", text="{a}Primeiro passo: compare o tipo de força. [p=0.3] {b}Metano, cê agá quatro: dipolo induzido. [p=0.1] Ferve a cento e sessenta e um graus negativos. [p=0.3] {c}Agá cê éle: dipolo permanente. [p=0.1] Oitenta e cinco graus negativos. [p=0.3] {d}Água: ligação de hidrogênio. [p=0.1] Cem graus. [p=0.3] {e}A ordem das temperaturas é a ordem das forças."),
    # passo 2
    dict(id="s06", block="passo2", text="{a}Segundo passo, só se a força for a mesma: compare o tamanho. [p=0.2] {b}Molécula maior tem mais elétrons, [p=0.1] e {c}o dipolo induzido fica mais forte. [p=0.3] {d}O metano, de um carbono, ferve a cento e sessenta e um negativos. [p=0.2] {e}O propano, de três carbonos, que vai no gás de cozinha: quarenta e dois negativos. [p=0.2] {f}O octano, de oito carbonos, da gasolina: cento e vinte e seis graus positivos."),
    # a água
    dict(id="s07", block="agua", text="E a água? [p=0.2] {a}Olhe a família do oxigênio: [p=0.1] {b}a água e as moléculas parecidas com ela, com enxofre, selênio ou telúrio no lugar do oxigênio. [p=0.3] {c}Do enxofre ao telúrio, a molécula cresce. [p=0.1] O dipolo induzido, que existe em todas, fica mais forte, e o ponto de ebulição sobe. [p=0.3] {d}Pela tendência, a água ferveria perto de oitenta graus negativos."),
    dict(id="s08", block="agua", text="{a}Mas ela ferve a cem. [p=0.2] {b}Com enxofre, selênio e telúrio, a força principal é o dipolo permanente. [p=0.2] {c}Só a água tem hidrogênio preso a oxigênio: [p=0.1] {d}ligação de hidrogênio, muito mais forte. [p=0.3] {e}É ela que mantém a água líquida no nosso planeta."),
    # erro
    dict(id="s09", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}comparar só pelo tamanho. [p=0.3] {b}Quem faz isso acha que o agá dois esse, maior, ferve acima da água. [p=0.2] {c}O tamanho só desempata quando a força é a mesma."),
    # atalho
    dict(id="s10", block="atalho", text="O atalho cabe numa frase: [p=0.1] {a}força primeiro, tamanho no empate. [p=0.3] Funciona porque {b}a diferença entre os tipos de força é grande, [p=0.1] e a diferença de tamanho entre moléculas parecidas é pequena."),
    dict(id="s11", block="atalho", text="{a}O atalho falha quando os tamanhos são muito diferentes. [p=0.2] {b}O octano só tem dipolo induzido, [p=0.1] mas {c}é tão maior que ferve acima da água. [p=0.3] {d}Na prova, as moléculas comparadas costumam ter tamanho parecido."),
    # questão
    dict(id="s12", block="questao", text="Hora de testar. [p=0.2] Ponha em ordem, {a}do menor para o maior ponto de ebulição: [p=0.2] {b}éfe dois, o gás flúor; [p=0.1] {c}agá cê éle; [p=0.1] {d}e agá éfe, o fluoreto de hidrogênio. [p=0.3] {e}As três moléculas têm tamanhos parecidos."),
    dict(id="s13", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s14", block="resposta", text="Vamos lá, força primeiro. [p=0.2] {a}Éfe dois: átomos iguais, apolar. [p=0.1] Dipolo induzido. [p=0.3] {b}Agá cê éle: polar, e o hidrogênio está preso ao cloro, que não é éfe, ó nem ene. [p=0.1] Dipolo permanente. [p=0.3] {c}Agá éfe: hidrogênio preso ao flúor. [p=0.1] Ligação de hidrogênio."),
    dict(id="s15", block="resposta", text="{a}A ordem: éfe dois, agá cê éle, agá éfe. [p=0.3] Os valores: {b}cento e oitenta e oito graus negativos, [p=0.2] {c}oitenta e cinco graus negativos [p=0.2] e {d}vinte graus positivos. [p=0.3] {e}A molécula mais leve das três ferve mais alto."),
    # fechamento
    dict(id="s16", block="fim", text="Resumindo: [p=0.1] {a}força mais forte, ponto de ebulição mais alto. [p=0.1] {b}Compare a força primeiro, [p=0.1] {c}o tamanho só no empate, [p=0.1] e {d}a água ferve alto pelas ligações de hidrogênio."),
    dict(id="s17", block="fim", text="Na próxima aula, as ligações de hidrogênio explicam {a}por que o gelo boia, [p=0.1] {b}por que um inseto anda sobre a água [p=0.1] e {c}como a água sobe por um tubo fino. [p=0.3] {d}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {e}Bons estudos!"),
]
