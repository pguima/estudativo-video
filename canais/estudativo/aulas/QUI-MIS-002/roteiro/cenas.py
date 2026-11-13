# Estudativo · QUI-MIS-002 — Substância pura ou mistura (Química · Matéria e Misturas · Matéria, substâncias e estados físicos).
# Habilidade: classificar O₂, H₂O, água com sal e água com óleo em substância simples, substância composta, mistura homogênea
# ou heterogênea, contar as fases de um sistema e dizer por que O₂ e O₃ são alótropos.
# Pré-requisitos: QUI-MIS-001. Próxima: QUI-MIS-003 (estados físicos e mudanças de estado).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Fórmulas letra a letra: O₂ = "ó dois", O₃ = "ó três", H₂O = "agá dois ó", CO₂ = "cê ó dois", H₂ = "agá dois".
# Fatos: água mineral tem sais dissolvidos (é mistura homogênea); ozônio, O₃, tem cheiro forte e, no alto da atmosfera,
# barra parte da luz do Sol que queima a pele; grafite e diamante são formas do carbono. Sal que sobra no fundo vira fase.
# Só MIS-001 está ensinada: sem conta, sem estados físicos (o gelo aparece só como "água congelada", assunto da próxima aula).

TITULO = "Substância pura ou mistura"

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
    dict(id="s01", block="gancho", text="{a}No rótulo está escrito água mineral natural. [p=0.3] Parece a coisa mais pura do mundo. [p=0.3] Mas, para a Química, {b}essa água é uma mistura. [p=0.3] {c}Por quê?"),
    dict(id="s02", block="gancho", text="{a}Nesta aula, você vai separar {b}substância de mistura, [p=0.2] {c}contar as fases de um copo [p=0.2] e entender por que {d}ó dois e ó três são substâncias diferentes."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula passada, você precisa de duas ideias. [p=0.2] {a}Elemento é o tipo de átomo. [p=0.2] E {b}a fórmula diz quais elementos estão lá e quantos átomos de cada um."),
    # substância × mistura
    dict(id="s04", block="pura", text="Imagine que você pudesse olhar a água com uma lupa poderosa, até ver as partículas. [p=0.3] {a}Na água destilada, a de laboratório, sem nada dissolvido, toda molécula é igual: [p=0.1] {b}agá dois ó, agá dois ó, agá dois ó."),
    dict(id="s05", block="pura", text="Quando todas as partículas são do mesmo tipo, o material é uma {a}substância pura. [p=0.3] E ela tem {b}uma fórmula só."),
    dict(id="s06", block="pura", text="{a}Na água mineral, além das moléculas de água, [p=0.1] {b}há partículas de sais dissolvidos. [p=0.3] Dois ou mais tipos de partícula juntos formam uma {c}mistura. [p=0.3] Cada substância que entra na mistura se chama {d}componente."),
    dict(id="s07", block="pura", text="Por isso, {a}o puro do rótulo não é o puro da Química. [p=0.2] O rótulo quer dizer que nada foi acrescentado. [p=0.2] {b}Suco cem por cento natural também é mistura."),
    # simples × composta
    dict(id="s08", block="simples", text="As substâncias puras se dividem em duas. [p=0.2] Olhe {a}o gás oxigênio, ó dois. [p=0.2] Cada molécula tem dois átomos, e eles são do mesmo elemento. [p=0.3] Substância formada por {b}um elemento só é uma substância simples."),
    dict(id="s09", block="simples", text="{a}A água, agá dois ó, tem dois elementos: hidrogênio e oxigênio. [p=0.3] Substância com {b}dois ou mais elementos é uma substância composta. [p=0.3] {c}O gás carbônico, cê ó dois, também é composta."),
    dict(id="s10", block="simples", text="O jeito de saber vem da aula passada: {a}cada letra maiúscula começa um elemento. [p=0.2] {b}Uma maiúscula, como em ó dois e em agá dois, o gás hidrogênio: simples. [p=0.2] {c}Duas ou mais, como em agá dois ó: composta."),
    # homogênea × heterogênea
    dict(id="s11", block="fases", text="As misturas também se dividem em duas. [p=0.2] {a}Mexa sal na água até sumir. [p=0.2] Você não vê onde está o sal: {b}o copo inteiro tem o mesmo aspecto. [p=0.3] Essa é uma {c}mistura homogênea. [p=0.2] {d}O ar e a água mineral também são."),
    dict(id="s12", block="fases", text="{a}Agora ponha óleo na água. [p=0.2] Mesmo depois de mexer, o óleo volta para cima, [p=0.1] e {b}você enxerga a divisa entre os dois. [p=0.3] Essa é uma {c}mistura heterogênea."),
    dict(id="s13", block="fases", text="Cada parte do sistema que tem o mesmo aspecto em todos os pontos se chama {a}fase. [p=0.2] Sistema, aqui, é só o que você está olhando: o conteúdo do copo. [p=0.3] {b}A água com sal tem uma fase. [p=0.2] {c}A água com óleo tem duas. [p=0.3] {d}Homogênea tem uma fase só; heterogênea, duas ou mais."),
    # erro
    dict(id="s14", block="erro", text="O erro mais comum é {a}contar os componentes no lugar das fases. [p=0.3] Num copo com {b}água, sal dissolvido e óleo, [p=0.2] a pessoa conta três coisas e diz {c}três fases."),
    dict(id="s15", block="erro", text="{a}Mas o sal dissolvido não forma uma parte separada: [p=0.1] ele está espalhado na água. [p=0.3] {b}Água com sal é uma fase, [p=0.1] {c}o óleo é outra. [p=0.3] {d}São três componentes e duas fases. [p=0.3] {e}Se sobrasse sal no fundo, aí sim, ele seria mais uma fase."),
    # alótropos
    dict(id="s16", block="alotropia", text="Falta o ó três. [p=0.2] {a}O ozônio, ó três, também é feito só de oxigênio. [p=0.3] {b}Então ó dois e ó três são a mesma coisa? [p=0.3] {c}Não. [p=0.2] O ó dois tem dois átomos por molécula; [p=0.1] {d}o ó três, três."),
    dict(id="s17", block="alotropia", text="E isso muda tudo. [p=0.2] {a}O ó dois não tem cheiro, e é ele que você respira. [p=0.3] {b}O ozônio tem cheiro forte e irrita o pulmão, [p=0.2] mas, {c}lá no alto do céu, barra parte da luz do Sol que queima a pele."),
    dict(id="s18", block="alotropia", text="Quando um mesmo elemento forma substâncias simples diferentes, elas são {a}alótropos. [p=0.3] {b}O carbono tem alótropos famosos: [p=0.1] {c}o grafite, do lápis, [p=0.1] e {d}o diamante. [p=0.3] {e}O que muda é como os átomos se arrumam."),
    # atalho
    dict(id="s19", block="atalho", text="O atalho de prova para classificar qualquer material são {a}duas perguntas. [p=0.3] {b}Primeira: dá para escrever uma fórmula só? [p=0.2] {c}Se dá, é substância; [p=0.1] conte as maiúsculas: {d}uma, simples; mais de uma, composta."),
    dict(id="s20", block="atalho", text="{a}Se não dá, é mistura. [p=0.2] {b}Segunda pergunta: dá para ver partes diferentes, a olho nu ou no microscópio? [p=0.2] {c}Não, homogênea. [p=0.1] {d}Sim, heterogênea."),
    dict(id="s21", block="atalho", text="Funciona porque {a}as perguntas são as próprias definições. [p=0.3] {b}Não compensa quando a prova traz desenho de bolinhas: [p=0.2] aí, {c}conte os tipos de molécula do desenho."),
    # questão
    dict(id="s22", block="questao", text="Hora de testar. [p=0.2] {a}Um copo tem água, sal dissolvido, óleo boiando e areia no fundo. [p=0.3] {b}Quantas fases? [p=0.2] {c}Quantos componentes? [p=0.2] E {d}a mistura é homogênea ou heterogênea?"),
    dict(id="s23", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s24", block="resposta", text="Vamos lá. [p=0.2] Fases: [p=0.1] {a}a água com o sal, que é uma só; [p=0.2] {b}o óleo, em cima; [p=0.2] {c}a areia, embaixo. [p=0.2] {d}Três fases."),
    dict(id="s25", block="resposta", text="Componentes: [p=0.1] {a}água, sal, óleo e areia. [p=0.2] {b}Quatro. [p=0.3] E, como dá para ver partes diferentes, {c}a mistura é heterogênea. [p=0.3] Quem contou o sal como fase {d}chegou a quatro fases."),
    # fechamento
    dict(id="s26", block="fim", text="Resumindo: [p=0.1] {a}substância tem um tipo só de partícula; [p=0.2] {b}mistura tem dois ou mais. [p=0.2] {c}Simples tem um elemento; composta, mais de um. [p=0.2] E {d}cada parte que você distingue no sistema é uma fase."),
    dict(id="s27", block="fim", text="Na próxima aula, você vai ver o que acontece com as partículas quando {a}o gelo derrete e a água ferve: [p=0.2] {b}os estados físicos e as mudanças de estado. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
