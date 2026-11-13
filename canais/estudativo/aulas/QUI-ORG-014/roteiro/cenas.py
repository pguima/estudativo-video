# Estudativo · QUI-ORG-014 — Isomeria plana (Química · Química Orgânica · Propriedades físicas e isomeria).
# Habilidade: classificar um par de isômeros em cadeia, posição, função, compensação ou tautomeria.
# Pré-requisitos: QUI-ORG-004 (cadeia principal, galhos), QUI-ORG-008 (ácido e éster). Próxima: QUI-ORG-015 (cis-trans, but-2-eno).
# Marcas: {cue} animação · [p=0.2] pausa. Nomes falados: propan-1-ol = "propan um ol"; but-1-eno = "but um eno".
# Fatos: etanol (líquido, 78 °C) × metoximetano (gás, −24 °C), C2H6O; butano × metilpropano C4H10 (cadeia); propan-1-ol × propan-2-ol
# C3H8O (posição); metoxipropano × etoxietano C4H10O (compensação = metameria); etenol ⇌ etanal C2H4O (tautomeria, enol ⇌ carbonila).
# Erro: propano C3H8 × propeno C3H6 não são isômeros. Questão: pentano × dimetilpropano C5H12 (cadeia); propanal × propanona
# C3H6O (função); but-1-eno × but-2-eno C4H8 (posição). Questão inédita, criada para esta aula.

TITULO = "Isomeria plana"

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
    dict(id="s01", block="gancho", text="{a}O etanol e o metoximetano têm os mesmos átomos, nas mesmas quantidades: [p=0.1] cê dois agá seis ó. [p=0.3] {b}Mas um é o álcool líquido da farmácia, [p=0.1] {c}e o outro é um gás. [p=0.3] {d}Mesma fórmula, substâncias diferentes."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai classificar um par desses em {b}cadeia, [p=0.1] {c}posição, [p=0.1] {d}função, [p=0.1] {e}compensação [p=0.1] {f}ou tautomeria."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar o que já viu nesta trilha: [p=0.2] {a}a cadeia principal e os galhos, [p=0.1] {b}a numeração [p=0.1] e {c}as funções com oxigênio, do álcool ao éster."),
    # isômeros
    dict(id="s04", block="isomero", text="{a}Isômeros são compostos com a mesma fórmula molecular e estruturas diferentes: [p=0.1] {b}os mesmos átomos, montados de outro jeito. [p=0.3] {c}Na isomeria plana, a diferença já aparece no desenho no papel. [p=0.2] {d}São cinco tipos. [p=0.1] Depois de conferir a fórmula, duas perguntas separam todos eles."),
    # função e tautomeria
    dict(id="s05", block="funcao", text="{a}Primeira pergunta: [p=0.1] {b}as duas moléculas são da mesma função? [p=0.2] {c}Se não são, a isomeria é de função. [p=0.3] {d}O etanol é um álcool, e o metoximetano, um éter: [p=0.1] {e}isomeria de função."),
    dict(id="s06", block="funcao", text="{a}A tautomeria é um caso especial da isomeria de função. [p=0.2] {b}Pense num ó agá preso a um carbono de ligação dupla: [p=0.1] {c}isso se chama enol. [p=0.3] {d}O enol não fica parado: [p=0.1] {e}o agá pula para o carbono vizinho, [p=0.1] e a dupla passa para o oxigênio. [p=0.2] {f}Ele vira um aldeído ou uma cetona."),
    dict(id="s07", block="funcao", text="{a}As duas formas vivem num vaivém, uma virando a outra o tempo todo, [p=0.1] e quase tudo fica na forma de aldeído ou cetona. [p=0.2] {b}É o caso do etenol e do etanal. [p=0.3] {c}Isômeros que se transformam um no outro sozinhos: [p=0.1] tautomeria."),
    # mesma função
    dict(id="s08", block="mesma", text="{a}Se a função é a mesma, faça a segunda pergunta: [p=0.1] {b}o que mudou? [p=0.3] {c}Se mudou a cadeia, a maior fila, os galhos, ou se uma é aberta e a outra fechada, [p=0.1] é isomeria de cadeia. [p=0.2] {d}Butano e metilpropano: [p=0.1] {e}a fila de quatro virou uma fila de três com um galho."),
    dict(id="s09", block="mesma", text="{a}Se a cadeia é a mesma, mas um grupo, um galho ou uma dupla mudou de carbono, [p=0.1] é isomeria de posição. [p=0.2] {b}Propan um ol e propan dois ol: [p=0.1] {c}o ó agá passou da ponta para o meio."),
    dict(id="s10", block="mesma", text="{a}E se o que mudou de lugar foi o heteroátomo, como o oxigênio no meio da cadeia? [p=0.2] {b}Aí é compensação, também chamada metameria. [p=0.3] {c}Metoxipropano e etoxietano: [p=0.1] {d}o oxigênio tinha um carbono de um lado e três do outro, [p=0.1] {e}e passou a ter dois de cada lado."),
    # erro comum
    dict(id="s11", block="erro", text="{a}O erro mais comum é chamar de isômeros moléculas com fórmulas diferentes. [p=0.3] {b}Propano e propeno parecem um par, [p=0.1] {c}mas o propano é cê três agá oito, e o propeno, cê três agá seis. [p=0.3] {d}Antes de tudo, confira a fórmula molecular: [p=0.1] se ela muda, não há isomeria."),
    # atalho
    dict(id="s12", block="atalho", text="{a}O atalho é a ordem das perguntas. [p=0.2] {b}A fórmula é a mesma? [p=0.1] Se não for, pare. [p=0.2] {c}A função é a mesma? [p=0.1] Se não for, é função, [p=0.1] ou tautomeria, quando é o enol com o aldeído ou a cetona. [p=0.3] {d}Com a mesma função, [p=0.1] {e}mudou a cadeia: cadeia. [p=0.1] {f}Um grupo mudou de carbono: posição. [p=0.1] {g}O heteroátomo mudou de lugar: compensação."),
    dict(id="s13", block="atalho", text="{a}Funciona porque cada tipo responde a uma pergunta só, sempre na mesma ordem. [p=0.3] {b}O cuidado é com o heteroátomo: [p=0.1] {c}num éter, levar o oxigênio para outro lugar da cadeia é compensação, não posição."),
    # questão
    dict(id="s14", block="questao", text="Hora de testar. [p=0.2] Classifique os três pares. [p=0.2] {a}Pentano e dimetilpropano. [p=0.2] {b}Propanal e propanona. [p=0.2] {c}But um eno e but dois eno."),
    dict(id="s15", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s16", block="resposta", text="{a}Primeiro par: [p=0.1] as duas moléculas têm a fórmula cê cinco agá doze, e são hidrocarbonetos. [p=0.2] {b}Mudou a cadeia: a fila de cinco virou uma fila de três com dois galhos. [p=0.2] {c}Isomeria de cadeia."),
    dict(id="s17", block="resposta", text="{a}Segundo par: [p=0.1] as duas têm a fórmula cê três agá seis ó, [p=0.1] {b}mas uma é aldeído e a outra, cetona. [p=0.2] {c}Isomeria de função."),
    dict(id="s18", block="resposta", text="{a}Terceiro par: [p=0.1] as duas têm a fórmula cê quatro agá oito, e são alcenos de quatro carbonos. [p=0.2] {b}Só a dupla mudou de carbono: [p=0.1] {c}isomeria de posição."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}isômeros têm a mesma fórmula e estruturas diferentes. [p=0.2] {b}Função diferente é isomeria de função, [p=0.1] ou tautomeria, se as formas se transformam uma na outra. [p=0.2] {c}Mesma função: cadeia, posição ou compensação, conforme o que mudou."),
    dict(id="s20", block="fim", text="Na próxima aula, a isomeria sai do papel e vai para o espaço: [p=0.2] {a}você vai ver quando existe a isomeria cis e trans [p=0.1] e {b}reconhecer as duas formas do but dois eno. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
