# Estudativo · QUI-INO-001 — Ácidos: ionização, nomes e força (Química · Funções e Reações Inorgânicas · Ácidos, bases, sais e óxidos).
# Habilidade: reconhecer um ácido pelo H⁺ em água, escrever a ionização do HCl, dar nome a HCl, H₂SO₄ e HNO₃ e dizer se o
# ácido é forte ou fraco.
# Pré-requisitos: QUI-LIG-002, QUI-LIG-004, QUI-INO-007. Próxima: QUI-INO-002 (bases: dissociação, nomes e força).
# Fórmulas narradas letra a letra: HCl = "agá cê éle", H₂SO₄ = "agá dois ésse ó quatro", HNO₃ = "agá ene ó três",
# H₃PO₄ = "agá três pê ó quatro", HBr = "agá bê erre". H⁺ = "agá mais"; Cl⁻ = "cê éle menos"; H₃O⁺ = "agá três ó mais".
# Fatos: HCl puro (gás ou líquido) não conduz; em água conduz. Svante Arrhenius, químico sueco (Nobel de 1903).
# HCl comercial = ácido muriático. H₂SO₄ = bateria de carro. H₂CO₃ está no refrigerante e se desfaz em CO₂ + H₂O.
# H₃PO₄ = acidulante dos refrigerantes de cola. Força pela convenção dos livros brasileiros: HCl, HBr, HI fortes; HF moderado;
# oxiácidos: O − H ≥ 2 forte, = 1 moderado, = 0 fraco; exceção H₂CO₃ (dá 1, é fraco). Questão inédita.

TITULO = "Ácidos: ionização, nomes e força"

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
    dict(id="s01", block="gancho", text="{a}Ácido clorídrico puro, sem água, {b}não conduz eletricidade: [p=0.2] a lâmpada fica apagada. [p=0.3] {c}Jogue esse ácido na água, e a lâmpada acende. [p=0.3] {d}O que a água fez com ele?"),
    dict(id="s02", block="gancho", text="Até o fim desta aula, você vai {a}reconhecer um ácido, [p=0.2] {b}escrever o que acontece com ele na água, [p=0.2] {c}dar nome aos ácidos mais famosos [p=0.2] e {d}dizer se um ácido é forte ou fraco."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre de duas coisas. [p=0.2] {a}Íon é um átomo com carga elétrica: [p=0.1] perdeu elétron, fica positivo; [p=0.1] ganhou, fica negativo. [p=0.3] E {b}uma substância só conduz eletricidade quando tem íons soltos, que podem andar."),
    # ionização
    dict(id="s04", block="ionizacao", text="O ácido clorídrico é o {a}agá cê éle. [p=0.2] Na molécula, {b}o hidrogênio e o cloro dividem um par de elétrons: [p=0.1] é uma ligação covalente. [p=0.3] {c}Não há íons ali. [p=0.2] Por isso, puro, ele não conduz."),
    dict(id="s05", block="ionizacao", text="Na água, a molécula se parte de um jeito especial. [p=0.2] {a}O cloro fica com o par de elétrons {b}e vira o íon cê éle menos, o cloreto. [p=0.3] {c}O hidrogênio sai sem elétron nenhum: [p=0.1] {d}vira agá mais, que é só um próton."),
    dict(id="s06", block="ionizacao", text="Então, {a}agá cê éle, na água, {b}produz o íon agá mais {c}e o íon cê éle menos. [p=0.3] Os íons {d}nasceram no contato com a água. [p=0.2] Isso se chama {e}ionização. [p=0.3] E, com íons soltos, a lâmpada acende."),
    dict(id="s07", block="ionizacao", text="Um detalhe. [p=0.2] {a}O agá mais não fica sozinho: ele se prende a uma molécula de água [p=0.1] e forma {b}o hidrônio, agá três ó mais. [p=0.3] {c}Nas provas, as duas formas de escrever valem."),
    # definição
    dict(id="s08", block="definicao", text="Daí vem a definição do químico sueco Arrhenius: [p=0.2] {a}ácido é a substância que, na água, solta agá mais como único íon positivo. [p=0.3] Por isso, {b}na fórmula de um ácido, o agá vem na frente: [p=0.2] {c}agá cê éle, [p=0.1] {d}agá dois ésse ó quatro, [p=0.1] {e}agá ene ó três. [p=0.3] A água também tem agá, mas quase não solta íons: não é ácido."),
    # nomes
    dict(id="s09", block="nomes", text="Os nomes seguem duas regras. [p=0.2] {a}Ácido sem oxigênio termina em ídrico. [p=0.2] {b}Agá cê éle é o ácido clorídrico, do cloro, [p=0.1] {c}vendido em loja de material de construção como ácido muriático."),
    dict(id="s10", block="nomes", text="{a}Os ácidos com oxigênio mais comuns terminam em ico. [p=0.2] {b}Agá dois ésse ó quatro é o ácido sulfúrico, do enxofre, [p=0.1] o da bateria de carro. [p=0.2] {c}Agá ene ó três é o ácido nítrico, do nitrogênio. [p=0.2] E {d}agá dois cê ó três é o ácido carbônico, do carbono, que está no refrigerante. [p=0.2] Os que terminam em oso ficam para outra aula."),
    # força
    dict(id="s11", block="forca", text="E a força? [p=0.2] {a}Ácido forte é o que se ioniza quase todo: [p=0.1] de cada cem moléculas na água, quase todas viram íons. [p=0.3] {b}No ácido fraco, só umas poucas se partem, [p=0.1] e o resto fica inteiro."),
    dict(id="s12", block="forca", text="Para os ácidos sem oxigênio, decore três fortes: [p=0.2] {a}o clorídrico, o bromídrico e o iodídrico. [p=0.3] {b}O fluorídrico é moderado. [p=0.2] {c}Os outros são fracos."),
    # erro
    dict(id="s13", block="erro", text="O erro comum é {a}achar que, quanto mais hidrogênios, mais forte o ácido. [p=0.3] {b}O agá ene ó três tem um agá só, {c}e é forte. [p=0.2] {d}O agá dois cê ó três tem dois, {e}e é fraco. [p=0.3] Quem decide é outra conta."),
    # atalho
    dict(id="s14", block="atalho", text="Para os ácidos com oxigênio, o atalho de prova: [p=0.2] {a}conte os oxigênios e tire os hidrogênios. [p=0.3] {b}Deu dois ou mais, é forte. [p=0.2] {c}Deu um, moderado. [p=0.2] {d}Deu zero, fraco."),
    dict(id="s15", block="atalho", text="{a}No agá dois ésse ó quatro, quatro menos dois dá dois: [p=0.1] {b}forte. [p=0.3] {c}No agá ene ó três, três menos um dá dois: [p=0.1] {d}forte também."),
    dict(id="s16", block="atalho", text="Funciona porque {a}os oxigênios que sobram facilitam a saída do agá mais. [p=0.3] {b}A exceção famosa é o ácido carbônico: [p=0.1] {c}a conta dá um, moderado, [p=0.1] mas ele é {d}fraco, porque se desfaz em gás carbônico e água. [p=0.2] {e}É o gás que escapa quando você abre o refrigerante."),
    # questão
    dict(id="s17", block="questao", text="Hora de testar. [p=0.2] {a}O ácido fosfórico, agá três pê ó quatro, está nos refrigerantes de cola. [p=0.2] {b}Ele é forte, moderado ou fraco? [p=0.3] E {c}escreva a ionização do ácido bromídrico, agá bê erre. [p=0.2] {d}Ele é forte ou fraco?"),
    dict(id="s18", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s19", block="resposta", text="Vamos lá. [p=0.2] {a}O fosfórico tem oxigênio: use o atalho. [p=0.2] {b}Quatro oxigênios menos três hidrogênios dá um: [p=0.1] {c}moderado."),
    dict(id="s20", block="resposta", text="{a}O agá bê erre, na água, [p=0.1] {b}produz o íon agá mais {c}e o íon bê erre menos, o brometo. [p=0.3] E {d}ele é um dos três fortes sem oxigênio: [p=0.1] {e}é forte."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: [p=0.1] {a}ácido solta agá mais na água, [p=0.1] {b}ídrico é sem oxigênio, ico é com oxigênio, [p=0.1] e {c}a força sai dos oxigênios menos os hidrogênios."),
    dict(id="s22", block="fim", text="Na próxima aula, você conhece o outro lado: {a}as bases, [p=0.2] {b}que soltam na água o íon ó agá menos. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
