# Estudativo · QUI-LIG-007 — Polaridade da ligação e da molécula (Química · Ligações Químicas · Polaridade e forças intermoleculares).
# Habilidade: explicar por que CO₂ é apolar e H₂O é polar, mesmo com ligações polares, usando a regra prática dos pares livres.
# Pré-requisitos: QUI-LIG-006, QUI-ATO-011. Próxima: QUI-LIG-008 (semelhante dissolve semelhante).
# Marcas: {cue} animação · [p=0.2] pausa. Questão inédita, criada para esta aula.
# Leituras: Cl₂ = "cê éle dois", HCl = "agá cê éle", CH₃Cl = "cê agá três cê éle", CCl₄ = "cê cê éle quatro", δ = "delta".
# Fatos: eletronegatividade (Pauling) F 4,0 > O 3,4 > Cl 3,2 > N 3,0 > C 2,6 > H 2,2; CO₂ linear e apolar; H₂O angular e polar;
# CH₃Cl polar (ligantes diferentes); CCl₄ tetraédrica e apolar; NH₃ piramidal e polar. Seta do dipolo aponta para o mais
# eletronegativo (convenção do ensino médio brasileiro).

TITULO = "Polaridade da ligação e da molécula"

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
    dict(id="s01", block="gancho", text="{a}Na água e no gás carbônico, {b}todas as ligações são polares. [p=0.3] {c}Mas só a água é uma molécula polar. [p=0.3] {d}Como uma molécula pode ter ligações polares e não ser polar?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai saber {b}quando uma ligação é polar, [p=0.2] {c}quando a molécula inteira é polar, [p=0.2] e vai levar {d}a regra prática dos pares livres, que resolve a maioria das questões."),
    # lembrete
    dict(id="s03", block="lembrete", text="Duas ideias de aulas anteriores. [p=0.2] {a}Eletronegatividade é a força com que um átomo puxa os elétrons de uma ligação. [p=0.2] {b}O flúor é o campeão, seguido do oxigênio. [p=0.3] E {c}a geometria: [p=0.1] {d}o gás carbônico é linear, a água é angular. [p=0.2] Se alguma travar, procure no canal."),
    # ligação apolar e polar
    dict(id="s04", block="ligacao", text="Comece por uma ligação entre átomos iguais, {a}como no gás cloro, cê éle dois. [p=0.2] {b}Os átomos puxam o par com a mesma força: [p=0.1] {c}o par fica no meio. [p=0.2] {d}É uma ligação apolar: sem polos, sem lado positivo ou negativo."),
    dict(id="s05", block="ligacao", text="Com átomos diferentes, {a}como no agá cê éle, a história muda. [p=0.2] {b}O cloro é mais eletronegativo e puxa o par para perto dele. [p=0.3] {c}O lado do cloro fica com um pouco de carga negativa, [p=0.1] e {d}o do hidrogênio, com um pouco de carga positiva. [p=0.3] Essas cargas parciais se escrevem com a letra grega {e}delta: delta mais e delta menos."),
    dict(id="s06", block="ligacao", text="{a}Um polo positivo e um negativo formam um dipolo. [p=0.2] {b}A ligação é polar. [p=0.3] E dá para desenhar esse puxão como {c}uma seta, que aponta para o átomo que puxa mais."),
    # molécula
    dict(id="s07", block="molecula", text="Numa molécula com várias ligações, {a}cada ligação é uma seta puxando. [p=0.2] {b}O que decide é a soma das setas, como num cabo de guerra. [p=0.3] {c}Se as forças se cancelam, a molécula é apolar. [p=0.2] {d}Se sobra puxão para um lado, ela é polar."),
    dict(id="s08", block="molecula", text="{a}No gás carbônico, cada oxigênio puxa elétrons do carbono. [p=0.2] {b}As ligações são polares. [p=0.2] Mas a molécula é linear: [p=0.1] {c}os oxigênios puxam com a mesma força, em sentidos opostos. [p=0.2] {d}Empate no cabo de guerra: a molécula é apolar."),
    dict(id="s09", block="molecula", text="{a}Na água, o oxigênio também puxa os elétrons dos hidrogênios. [p=0.2] Só que a molécula é angular: [p=0.1] {b}as setas apontam para o mesmo lado, o do oxigênio. [p=0.2] {c}Elas não se cancelam: se somam. [p=0.3] {d}A água é polar, [p=0.1] com o lado do oxigênio negativo e o lado dos hidrogênios positivo."),
    # erro
    dict(id="s10", block="erro", text="Cuidado com o erro mais comum: [p=0.2] {a}ligação polar, então molécula polar. [p=0.3] {b}O gás carbônico desmente: ligações polares, molécula apolar. [p=0.2] {c}Quem decide a molécula é a geometria, junto com os átomos que estão nas pontas."),
    # atalho
    dict(id="s11", block="atalho", text="O atalho é a {a}regra prática dos pares livres. [p=0.2] Olhe o átomo central. [p=0.2] {b}Tem par livre? A molécula é polar. [p=0.3] {c}Não tem par livre, e todos os ligantes são iguais? Apolar. [p=0.3] {d}Gás carbônico: carbono sem par livre, dois oxigênios iguais. Apolar. [p=0.2] {e}Água: oxigênio com dois pares livres. Polar. [p=0.3] {f}Molécula de dois átomos não tem central: [p=0.1] átomos iguais, apolar; diferentes, polar."),
    dict(id="s12", block="atalho", text="Funciona porque {a}o par livre deixa um lado diferente do outro, e as setas não se cancelam. [p=0.2] {b}Sem par livre e com ligantes iguais, a forma fica simétrica, e as setas se anulam. [p=0.3] {c}Não compensa se os ligantes forem diferentes, como no cê agá três cê éle: [p=0.1] {d}sem par livre, mas polar, porque o cloro puxa mais que os hidrogênios."),
    # questão
    dict(id="s13", block="questao", text="Hora de testar. [p=0.2] {a}No tetracloreto de carbono, cê cê éle quatro, um carbono preso a quatro cloros, [p=0.1] {b}as ligações entre carbono e cloro são polares. [p=0.2] {c}A molécula é polar ou apolar? [p=0.3] E {d}a amônia, ene agá três?"),
    dict(id="s14", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s15", block="resposta", text="Vamos lá. [p=0.2] {a}No cê cê éle quatro, o carbono faz quatro ligações e fica sem par livre. [p=0.2] {b}Os quatro ligantes são cloros, todos iguais. [p=0.2] {c}Apolar: [p=0.1] {d}as setas apontam para os cantos do tetraedro e se cancelam."),
    dict(id="s16", block="resposta", text="{a}Na amônia, o nitrogênio tem três ligações e um par livre. [p=0.2] {b}Tem par livre: polar. [p=0.2] {c}O nitrogênio puxa mais que o hidrogênio. [p=0.1] As setas apontam para ele, no alto da pirâmide, e a soma não zera."),
    # fechamento
    dict(id="s17", block="fim", text="Resumindo: [p=0.1] {a}a ligação é polar quando junta átomos de eletronegatividades diferentes, [p=0.1] {b}a molécula é polar quando as setas não se cancelam, [p=0.1] e {c}par livre no átomo central quer dizer molécula polar."),
    dict(id="s18", block="fim", text="Na próxima aula, a polaridade decide quem se mistura com quem: [p=0.1] {a}semelhante dissolve semelhante. [p=0.2] Você vai prever se {b}sal, álcool, óleo e iodo se dissolvem na água ou na gasolina. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
