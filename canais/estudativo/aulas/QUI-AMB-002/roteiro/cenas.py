# Estudativo · QUI-AMB-002 — Poluentes do ar e chuva ácida (Química · Química e Ambiente · Combustíveis, poluição e chuva ácida).
# Habilidade: apontar a origem de CO, NOx, SO₂ e material particulado, escrever SO₃ + H₂O → H₂SO₄, explicar por que a chuva
# natural já tem pH perto de 5,6 e o que a chuva ácida faz com o mármore.
# Pré-requisitos: QUI-INO-004, QUI-INO-005, QUI-INO-009, QUI-TER-006. Próxima: QUI-AMB-003 (efeito estufa e ozônio).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fórmulas faladas letra a letra: CO "cê ó", NO "ene ó", NO₂ "ene ó dois", NOx "ene ó xis", SO₂ "ésse ó dois",
# SO₃ "ésse ó três", H₂SO₄ "agá dois ésse ó quatro", H₂CO₃ "agá dois cê ó três", CaCO₃ "cê á cê ó três", pH "pê agá".
# Fatos: chuva natural pH ≈ 5,6 (CO₂ + H₂O ⇌ H₂CO₃); chuva ácida = pH abaixo de 5,6; N₂ + O₂ → 2 NO no motor quente,
# 2 NO + O₂ → 2 NO₂; S + O₂ → SO₂; 2 SO₂ + O₂ → 2 SO₃; NO₂ forma ácido nítrico, HNO₃; mármore = CaCO₃;
# CaCO₃ + H₂SO₄ → CaSO₄ + H₂O + CO₂. AMB-001 e a dupla troca não estão em "Já ensinado": a reação do mármore é mostrada
# como fato, sem classificar.

TITULO = "Poluentes do ar e chuva ácida"

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
    dict(id="s01", block="gancho", text="{a}Toda chuva é ácida. [p=0.3] {b}Até a chuva sem poluição nenhuma [p=0.1] tem pê agá perto de cinco vírgula seis, {c}abaixo do sete da água pura. [p=0.3] {d}Então, o que é a tal chuva ácida?"),
    dict(id="s02", block="gancho", text="{a}Nesta aula, você vai descobrir {b}de onde vem cada poluente do ar, [p=0.2] {c}como a chuva vira ácido [p=0.2] e {d}por que as estátuas de mármore estão se desgastando."),
    # lembrete
    dict(id="s03", block="lembrete", text="Três lembretes. [p=0.2] {a}Pê agá abaixo de sete é ácido. [p=0.2] {b}Óxido ácido mais água forma um ácido. [p=0.3] {c}E a combustão incompleta, com pouco oxigênio, solta cê ó, o monóxido de carbono."),
    # poluentes
    dict(id="s04", block="poluentes", text="São quatro poluentes principais, cada um com uma origem. [p=0.3] {a}O primeiro é o cê ó. [p=0.2] {b}Ele sai da queima com pouco oxigênio: motor desregulado, fogão a lenha em lugar fechado. [p=0.3] {c}No sangue, o cê ó toma o lugar do oxigênio. [p=0.2] E, como não tem cheiro nem cor, mata sem ninguém perceber."),
    dict(id="s05", block="poluentes", text="{a}O segundo são os ene ó xis: o ene ó e o ene ó dois. [p=0.2] {b}E aqui vem a surpresa: [p=0.1] o nitrogênio não vem do combustível. [p=0.3] {c}Vem do próprio ar. [p=0.2] {d}No motor quentíssimo, o nitrogênio e o oxigênio do ar reagem [p=0.1] {e}e formam ene ó, que depois vira ene ó dois."),
    dict(id="s06", block="poluentes", text="{a}O terceiro é o ésse ó dois. [p=0.2] {b}O enxofre vem como impureza no carvão e no óleo diesel. [p=0.3] {c}Na queima, enxofre mais oxigênio dá ésse ó dois."),
    dict(id="s07", block="poluentes", text="{a}O quarto é o material particulado: [p=0.1] {b}fuligem e poeira tão finas que entram fundo no pulmão. [p=0.3] {c}Sai da queima incompleta, do diesel e das queimadas."),
    dict(id="s08", block="poluentes", text="{a}O catalisador do escapamento ataca os dois primeiros. [p=0.3] {b}Ele transforma o cê ó e os ene ó xis em cê ó dois e nitrogênio, gases bem menos perigosos para a saúde."),
    # chuva natural
    dict(id="s09", block="chuva", text="Agora, a chuva. [p=0.2] {a}O ar sempre teve cê ó dois, que é um óxido ácido. [p=0.3] {b}A gota de chuva dissolve um pouco dele [p=0.1] {c}e forma o ácido carbônico, agá dois cê ó três. [p=0.3] {d}É um ácido fraco, e deixa a chuva com pê agá perto de cinco vírgula seis. [p=0.3] {e}Isso é natural."),
    dict(id="s10", block="chuva", text="{a}Chuva ácida é a que fica abaixo de cinco vírgula seis. [p=0.3] {b}E quem a empurra para baixo são os poluentes: [p=0.1] {c}o ésse ó dois e os ene ó xis."),
    # SO3
    dict(id="s11", block="sulfurico", text="O caminho do enxofre tem dois passos. [p=0.2] {a}No ar, o ésse ó dois ganha mais oxigênio e vira ésse ó três. [p=0.3] {b}O ésse ó três encontra a água da chuva: [p=0.1] {c}ésse ó três mais agá dois ó dá agá dois ésse ó quatro, [p=0.2] {d}o ácido sulfúrico, um ácido forte."),
    dict(id="s12", block="sulfurico", text="{a}Com os ene ó xis, a história é parecida: [p=0.1] {b}o ene ó dois reage com a água e o oxigênio [p=0.1] e forma {c}ácido nítrico, agá ene ó três, também forte."),
    # mármore
    dict(id="s13", block="marmore", text="E o mármore? [p=0.2] {a}Ele é feito de carbonato de cálcio, cê á cê ó três. [p=0.3] {b}O ácido sulfúrico da chuva reage com o carbonato: [p=0.1] {c}forma sulfato de cálcio, água e cê ó dois, que escapa como gás."),
    dict(id="s14", block="marmore", text="{a}Gota a gota, ano a ano, a estátua vai perdendo o nariz, os dedos e os detalhes. [p=0.3] {b}A chuva ácida também ataca lagos, florestas e o metal dos carros e das pontes."),
    # atalho
    dict(id="s15", block="atalho", text="O atalho de prova para achar o ácido de um óxido: [p=0.1] {a}some a água à fórmula, átomo por átomo. [p=0.3] {b}Esse ó três mais agá dois ó: [p=0.1] {c}junta os dois agás, o ésse e os quatro ós: agá dois ésse ó quatro. [p=0.3] {d}Com cê ó dois e água, sai agá dois cê ó três."),
    dict(id="s16", block="atalho", text="Funciona porque {a}nessas reações os átomos não somem: só se juntam. [p=0.3] {b}Não compensa com o ene ó dois: [p=0.1] a soma direta não dá um ácido de verdade, [p=0.1] e a reação é mais complicada. [p=0.2] {c}E o cê ó não forma ácido nenhum: é um óxido neutro."),
    # erro
    dict(id="s17", block="erro", text="O erro mais comum é {a}pôr a culpa da chuva ácida no cê ó dois. [p=0.3] {b}O cê ó dois é o que deixa a chuva natural em cinco vírgula seis. [p=0.3] {c}Quem leva a chuva para baixo disso são os ácidos fortes, [p=0.1] {d}que vêm do ésse ó dois e dos ene ó xis."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] {a}Numa cidade com usinas a carvão, as estátuas de mármore se desgastam rápido. [p=0.3] {b}Primeiro: qual gás, saído do carvão, é o principal culpado? [p=0.2] {c}Segundo: escreva a reação do ésse ó três com a água. [p=0.2] {d}Terceiro: a chuva da cidade tem pê agá quatro vírgula cinco, e a da serra ao lado, cinco vírgula seis. [p=0.1] Qual é chuva ácida?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s20", block="resposta", text="{a}Primeiro: o ésse ó dois, do enxofre que vem no carvão. [p=0.3] {b}Segundo: ésse ó três mais agá dois ó [p=0.1] dá agá dois ésse ó quatro."),
    dict(id="s21", block="resposta", text="{a}Terceiro: a chuva ácida é a da cidade, com quatro vírgula cinco. [p=0.3] {b}A da serra está em cinco vírgula seis, o normal. [p=0.3] {c}Quem respondeu que as duas são ácidas porque estão abaixo de sete [p=0.1] {d}esqueceu que até a chuva limpa já é um pouco ácida."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: [p=0.1] {a}cê ó vem da queima com pouco oxigênio; [p=0.2] {b}ene ó xis, do ar aquecido no motor; [p=0.2] {c}ésse ó dois, do enxofre do combustível; [p=0.2] e {d}chuva ácida é a que fica abaixo de cinco vírgula seis."),
    dict(id="s23", block="fim", text="Na próxima aula, dois problemas que todo mundo confunde: [p=0.2] {a}o efeito estufa e o buraco na camada de ozônio. [p=0.3] {b}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {c}Bons estudos!"),
]
