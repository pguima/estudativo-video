# Estudativo · QUI-LIG-006 — Geometria molecular (Química · Ligações Químicas · Polaridade e forças intermoleculares).
# Habilidade: dizer se CO₂, H₂O, NH₃ e CH₄ são lineares, angulares, piramidais ou tetraédricas contando os pares em volta do átomo central.
# Pré-requisitos: QUI-LIG-002. Próxima: QUI-LIG-007 (polaridade da ligação e da molécula).
# Atenção: só a LIG-002 da trilha está em "Já ensinado" (nada de iônica, metálica ou eletronegatividade).
# Marcas: {cue} animação · [p=0.2] pausa. Questão inédita, criada para esta aula.
# Leituras: CH₄ = "cê agá quatro", NH₃ = "ene agá três", H₂S = "agá dois esse", HCN = "agá cê ene".
# Fatos: ângulos CO₂ 180°, CH₄ 109,5°, NH₃ ≈ 107°, H₂O ≈ 104,5°; H₂S angular (S na família do O, 2 pares livres);
# HCN linear (C com 1 simples + 1 tripla, sem par livre). Trigonal plana = 3 ligantes sem par livre (ex.: metanal, H₂CO).
# Modelo = repulsão dos pares de elétrons da camada de valência (VSEPR), com a analogia dos balões amarrados.

TITULO = "Geometria molecular"

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
    dict(id="s01", block="gancho", text="{a}Agá dois ó e cê ó dois. [p=0.2] Nas duas moléculas, {b}há um átomo no meio, preso a dois outros. [p=0.3] {c}Mas a molécula de água é dobrada, [p=0.1] e {d}a de gás carbônico é reta. [p=0.3] {e}Quem dobra a água é algo que nem aparece na fórmula."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai dizer se uma molécula é {b}linear, angular, piramidal ou tetraédrica, [p=0.2] {c}contando os pares de elétrons em volta do átomo do meio. [p=0.2] E leva um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai precisar da {a}estrutura de Lewis. [p=0.2] {b}Cada traço é um par de elétrons compartilhado, [p=0.1] e a ligação pode ser simples, dupla ou tripla. [p=0.3] {c}Os pares livres são os que sobram no átomo, fora das ligações. [p=0.2] Se faltar essa aula, procure no canal."),
    # átomo central e repulsão
    dict(id="s04", block="repulsao", text="Comece achando o {a}átomo central: [p=0.1] aquele que se liga aos outros. [p=0.2] {b}Na água, é o oxigênio. [p=0.1] {c}No gás carbônico, o carbono. [p=0.3] {d}A forma da molécula depende do que está em volta dele."),
    dict(id="s05", block="repulsao", text="{a}Pares de elétrons têm carga negativa, [p=0.1] e cargas iguais se repelem. [p=0.3] Então, {b}os pares em volta do átomo central se afastam o máximo que podem. [p=0.3] Pense em {c}balões amarrados pelo nó. [p=0.2] {d}Dois balões ficam em lados opostos. [p=0.2] {e}Três formam um triângulo. [p=0.2] {f}Quatro apontam para os cantos de um tetraedro, [p=0.1] uma figura de quatro faces triangulares, com o nó bem no meio."),
    dict(id="s06", block="repulsao", text="Chame de {a}região cada direção, em volta do átomo central, onde há elétrons. [p=0.2] {b}Cada ligação vale uma região, seja simples, dupla ou tripla. [p=0.2] E {c}cada par livre também vale uma."),
    # as quatro formas
    dict(id="s07", block="formas", text="{a}No gás carbônico, o carbono tem duas ligações duplas e nenhum par livre. [p=0.2] {b}Duas regiões: lados opostos. [p=0.2] {c}A molécula é linear, com ângulo de cento e oitenta graus."),
    dict(id="s08", block="formas", text="{a}No metano, cê agá quatro, o carbono tem quatro ligações simples. [p=0.2] {b}Quatro regiões: os hidrogênios vão para os cantos de um tetraedro. [p=0.2] {c}A molécula é tetraédrica, com ângulos de cento e nove graus e meio."),
    dict(id="s09", block="formas", text="{a}Na amônia, ene agá três, o nitrogênio tem três ligações {b}e um par livre. [p=0.2] {c}São quatro regiões de novo, arrumadas como no tetraedro. [p=0.3] Mas o nome da forma {d}só olha os átomos. [p=0.1] {e}O par livre empurra, mas não aparece. [p=0.2] {f}O nitrogênio fica no topo, e os três hidrogênios formam a base: [p=0.1] uma pirâmide. [p=0.1] A amônia é piramidal."),
    dict(id="s10", block="formas", text="{a}Na água, o oxigênio tem duas ligações e dois pares livres. [p=0.2] {b}Quatro regiões outra vez. [p=0.2] {c}Tire os pares livres da vista, e sobram três átomos em forma de vê: [p=0.1] {d}a água é angular, com cerca de cento e quatro graus e meio."),
    # erro
    dict(id="s11", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}desenhar a água reta, como o gás carbônico, [p=0.1] porque as fórmulas parecem iguais. [p=0.3] {b}O que muda são os pares livres. [p=0.2] {c}O carbono do gás carbônico não tem nenhum. [p=0.1] {d}O oxigênio da água tem dois, e eles empurram os hidrogênios para baixo. [p=0.2] {e}Sem desenhar Lewis, você erra a forma."),
    # atalho
    dict(id="s12", block="atalho", text="O atalho de prova: [p=0.1] {a}olhe só o átomo central e conte {b}os ligantes, que são os átomos presos a ele, [p=0.1] e {c}os pares livres. [p=0.3] {d}Dois ligantes, sem par livre: linear. [p=0.2] {e}Dois ligantes com par livre: angular. [p=0.2] {f}Três ligantes sem par livre: trigonal plana, um triângulo achatado. [p=0.2] {g}Três ligantes e um par livre: piramidal. [p=0.2] {h}Quatro ligantes: tetraédrica."),
    dict(id="s13", block="atalho", text="Funciona porque {a}os pares livres ocupam espaço, mas o nome só conta os átomos. [p=0.3] E {b}uma molécula de dois átomos, como agá cê éle ou ó dois, é sempre linear: [p=0.1] {c}nem precisa contar."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] {a}Qual é a geometria do agá dois esse, o gás com cheiro de ovo podre? [p=0.2] {b}O enxofre é da mesma família do oxigênio. [p=0.3] E {c}a do agá cê ene, o ácido cianídrico?"),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="Vamos lá. [p=0.2] {a}O enxofre, como o oxigênio, tem seis elétrons de valência. [p=0.2] {b}Duas ligações com os hidrogênios usam dois deles. [p=0.1] Sobram quatro: dois pares livres. [p=0.3] {c}Dois ligantes com par livre: angular, como a água."),
    dict(id="s17", block="resposta", text="{a}No agá cê ene, o central é o carbono: [p=0.1] {b}uma ligação simples com o hidrogênio e uma tripla com o nitrogênio. [p=0.2] {c}Nenhum par livre no carbono. [p=0.2] {d}Duas regiões, dois ligantes: linear. [p=0.3] {e}Quem conta cada traço da tripla como uma região chega a quatro e chuta tetraédrica. [p=0.1] Errado: a tripla vale uma região só."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}os pares em volta do átomo central se afastam ao máximo, [p=0.1] {b}cada ligação ou par livre vale uma região, [p=0.1] e {c}o nome da forma só olha os átomos."),
    dict(id="s19", block="fim", text="Na próxima aula, a forma decide outra coisa: {a}a polaridade. [p=0.2] Você vai ver por que {b}o gás carbônico é apolar e a água é polar, [p=0.1] mesmo com ligações polares nas duas. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
