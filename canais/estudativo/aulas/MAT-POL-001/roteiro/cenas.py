# Estudativo · MAT-POL-001 — Quadriláteros: paralelogramo, retângulo, losango e trapézio (Matemática · Geometria Plana: Polígonos e Círculo).
# Habilidade: dizer o que vale para lados, ângulos e diagonais de cada quadrilátero e achar os outros ângulos de um paralelogramo com um ângulo de 70°.
# Pré-requisitos: MAT-ANG-007 (congruência, ALA), MAT-ANG-003 (paralelas e transversal). Próxima: MAT-POL-002.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa. Números por extenso.

TITULO = "Quadriláteros: paralelogramo, retângulo, losango e trapézio"

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
    dict(id="s01", block="gancho", text="{a}Um quadrado é um retângulo? [p=0.3] Muita gente responde {b}que não. [p=0.3] Mas é. [p=0.2] E ele também é {c}um losango. [p=0.3] Parece pegadinha, [p=0.1] mas é só saber o que cada nome exige."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você sabe o que vale para lados, ângulos e diagonais de cada quadrilátero, [p=0.2] {b}acha os ângulos de um paralelogramo [p=0.2] e leva um {c}atalho de prova."),
    # o que precisa saber
    dict(id="s03", block="lembrete", text="Para acompanhar, você precisa de {a}duas coisas: [p=0.2] {b}com paralelas cortadas por uma transversal, agudo com agudo é igual, e agudo com obtuso soma cento e oitenta, [p=0.2] e {c}triângulos congruentes são cópias um do outro, como no caso ângulo, lado, ângulo. [p=0.3] Se faltar alguma, procure no canal."),
    # quadrilátero
    dict(id="s04", block="quadri", text="{a}Quadrilátero é toda figura fechada com quatro lados. [p=0.2] Os cantos são {b}os vértices: á, bê, cê e dê, em volta da figura. [p=0.3] O segmento que liga {c}vértices que não são vizinhos, como á e cê, [p=0.1] é {d}uma diagonal. [p=0.2] Todo quadrilátero tem {e}duas diagonais: á cê e bê dê."),
    dict(id="s05", block="quadri", text="Os nomes especiais dependem de {a}quantos pares de lados paralelos ele tem. [p=0.3] {b}Só um par de lados paralelos: trapézio. [p=0.2] Os lados paralelos se chamam {c}bases. [p=0.3] {d}Dois pares de lados paralelos: paralelogramo."),
    # paralelogramo
    dict(id="s06", block="paralelo", text="O paralelogramo é a base de todo o resto. [p=0.2] Trace {a}a diagonal á cê. [p=0.2] Ela corta os lados paralelos como uma transversal, [p=0.2] e aparecem {b}ângulos alternos internos iguais, os do zê."),
    dict(id="s07", block="paralelo", text="Assim, {a}os triângulos á bê cê e cê dê á são congruentes, [p=0.2] pelo caso {b}ângulo, lado, ângulo, [p=0.2] com a diagonal como {c}lado comum. [p=0.3] Um é cópia do outro, [p=0.2] e daí saem as regras do paralelogramo."),
    dict(id="s08", block="paralelo", text="{a}Lados opostos são iguais. [p=0.2] {b}Ângulos opostos são iguais. [p=0.2] {c}Ângulos vizinhos somam cento e oitenta, [p=0.2] pela regra da transversal. [p=0.3] E {d}as diagonais se cortam ao meio: [p=0.2] o cruzamento fica no meio de cada uma."),
    # exemplo do setenta
    dict(id="s09", block="setenta", text="Vamos usar. [p=0.2] Um paralelogramo tem {a}ângulo de setenta graus em á. [p=0.3] {b}O ângulo em cê, oposto, também mede setenta. [p=0.2] {c}Em bê, vizinho do á: cento e oitenta menos setenta dá cento e dez. [p=0.2] {d}Em dê, oposto ao bê: cento e dez."),
    dict(id="s10", block="setenta", text="Conferindo: {a}setenta mais cento e dez dá cento e oitenta, [p=0.2] em cada par de vizinhos. [p=0.2] Bateu."),
    # especiais
    dict(id="s11", block="especiais", text="Agora os paralelogramos especiais. [p=0.2] Eles herdam tudo isso e {a}ganham uma regra a mais. [p=0.3] {b}Retângulo: quatro ângulos retos. [p=0.2] O que ele ganha: {c}diagonais do mesmo tamanho."),
    dict(id="s12", block="especiais", text="{a}Losango: quatro lados iguais. [p=0.2] Os ângulos podem não ser retos. [p=0.2] O que ele ganha: {b}diagonais perpendiculares, [p=0.1] que se cruzam em ângulo reto."),
    dict(id="s13", block="especiais", text="{a}Quadrado: quatro lados iguais e quatro ângulos retos. [p=0.2] Ele é {b}retângulo e losango ao mesmo tempo, [p=0.2] por isso {c}ganha tudo: diagonais iguais e perpendiculares. [p=0.3] Era o gancho: {d}todo quadrado é retângulo, [p=0.2] mas nem todo retângulo é quadrado."),
    # trapézio
    dict(id="s14", block="trapezio", text="E o trapézio, com um par só de lados paralelos? [p=0.2] Ele não segue as regras do paralelogramo. [p=0.3] Quando os lados que não são bases têm o mesmo tamanho, [p=0.1] é {a}o trapézio isósceles: [p=0.2] {b}os ângulos de cada base são iguais [p=0.2] e {c}as diagonais também. [p=0.3] Quando um lado faz ângulo reto com as bases, [p=0.1] é {d}o trapézio retângulo."),
    # erro
    dict(id="s15", block="erro", text="Cuidado com o erro mais comum: {a}achar que todo losango tem diagonais iguais. [p=0.3] {b}Achate um losango. [p=0.2] Uma diagonal fica {c}comprida, e a outra, curta. [p=0.3] Diagonais iguais são do {d}retângulo. [p=0.2] As do losango são {e}perpendiculares."),
    # atalho
    dict(id="s16", block="atalho", text="E o atalho prometido, para os ângulos do paralelogramo: [p=0.2] {a}só existem duas medidas. [p=0.3] {b}O ângulo que você conhece, [p=0.2] e {c}cento e oitenta menos ele. [p=0.3] {d}De frente, iguais. [p=0.2] {e}Lado a lado, somam cento e oitenta."),
    dict(id="s17", block="atalho", text="Funciona porque {a}cada lado é uma transversal entre paralelas: [p=0.2] a mesma regra do agudo e do obtuso. [p=0.3] {b}Não vale em quadrilátero sem lados paralelos. [p=0.2] E, no trapézio, {c}só somam cento e oitenta os ângulos de um mesmo lado que liga as bases."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] Num paralelogramo, ângulos vizinhos medem {a}três xis menos dez [p=0.2] e {b}xis mais cinquenta. [p=0.3] {c}Quanto mede cada ângulo do paralelogramo?"),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="resposta", text="Vamos lá. [p=0.2] Vizinhos {a}somam cento e oitenta: [p=0.2] {b}três xis menos dez mais xis mais cinquenta igual a cento e oitenta. [p=0.2] {c}Juntando: quatro xis mais quarenta igual a cento e oitenta. [p=0.2] {d}Tire quarenta: quatro xis igual a cento e quarenta. [p=0.2] {e}Divida por quatro: xis igual a trinta e cinco."),
    dict(id="s21", block="resposta", text="{a}Três vezes trinta e cinco dá cento e cinco, menos dez dá noventa e cinco graus. [p=0.2] {b}Trinta e cinco mais cinquenta dá oitenta e cinco graus. [p=0.2] Conferindo: noventa e cinco mais oitenta e cinco dá cento e oitenta. [p=0.3] Pelo atalho, os ângulos de frente são cópias: [p=0.2] {c}um par de ângulos de noventa e cinco graus [p=0.2] e um par de oitenta e cinco. [p=0.3] Quem iguala as expressões, como se fossem opostos, [p=0.1] acha {d}ângulos de oitenta graus, que não fecham cento e oitenta com o vizinho."),
    # fechamento
    dict(id="s22", block="fim", text="Resumindo: {a}o paralelogramo tem lados e ângulos opostos iguais e diagonais que se cortam ao meio. [p=0.2] {b}O retângulo ganha diagonais iguais; [p=0.2] {c}o losango, perpendiculares; [p=0.2] {d}o quadrado, tudo."),
    dict(id="s23", block="fim", text="Na próxima aula, você descobre {a}quanto somam os ângulos de qualquer polígono, [p=0.2] cortando a figura em triângulos, [p=0.2] e {b}quantas diagonais ele tem. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
