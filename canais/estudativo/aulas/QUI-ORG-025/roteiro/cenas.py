# Estudativo · QUI-ORG-025 — Polímeros de adição (Química · Química Orgânica · Polímeros).
# Habilidade: achar o monômero de polietileno, PVC, teflon e isopor e escrever a sua cadeia repetida.
# Pré-requisitos: QUI-ORG-018. Próxima: QUI-ORG-026 (polímeros de condensação: PET e náilon).
# Primeira aula do módulo Polímeros: o visual.py guarda a linguagem visual dos polímeros. Questão inédita (polipropileno).
# Marcas: {cue} animação · [p=0.2] pausa. Fórmulas por extenso; n = "ene".
# Fatos: polietileno (sacolas, frascos), PVC = poli(cloreto de vinila), monômero CH2=CHCl (canos, fios); teflon =
# politetrafluoroetileno, monômero CF2=CF2 (frigideira antiaderente); isopor = poliestireno expandido, monômero estireno
# CH2=CH–C6H5. Uma cadeia de polietileno tem de milhares a centenas de milhares de unidades.
# Nomes de haletos não foram ensinados: cloreto de vinila e tetrafluoroeteno entram como nome comercial, sem regra.

TITULO = "Polímeros de adição"

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
    dict(id="s01", block="gancho", text="{a}O plástico da sacolinha de supermercado é feito de fios invisíveis, {b}e cada fio é uma molécula só. [p=0.3] {c}Uma molécula gigante, feita de milhares de pedaços iguais, presos um no outro. [p=0.3] {d}E o pedaço que se repete vem do eteno."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}achar o monômero do polietileno, do pê vê cê, do teflon e do isopor, [p=0.2] e {c}escrever a cadeia que se repete. [p=0.2] E ainda leva um {d}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre da aula de adição: [p=0.2] {a}uma das ligações da dupla se abre, [p=0.2] e {b}cada carbono fica com uma vaga para uma nova ligação."),
    # o que é polímero
    dict(id="s04", block="poli", text="{a}Polímero vem do grego: poli quer dizer muitos, [p=0.2] {b}e mero quer dizer parte. [p=0.3] {c}É uma molécula enorme, feita de uma unidade que se repete. [p=0.3] {d}A molécula pequena de partida se chama monômero: [p=0.2] {e}uma parte só."),
    # polietileno
    dict(id="s05", block="pe", text="Veja o eteno, {a}cê agá dois, dupla, cê agá dois. [p=0.3] {b}A dupla se abre, [p=0.2] e {c}as duas vagas se ligam aos etenos vizinhos, [p=0.2] {d}que também abriram as suas. [p=0.3] {e}Um puxa o outro, e a cadeia cresce."),
    dict(id="s06", block="pe", text="Para não escrever milhares de carbonos, {a}a cadeia vai entre colchetes: [p=0.2] {b}cê agá dois, cê agá dois, [p=0.2] com {c}um ene pequeno do lado, que diz quantas vezes a unidade se repete. [p=0.3] {d}É o polietileno, das sacolas e dos frascos de xampu. [p=0.3] {e}Como nada sai na reação, ele é um polímero de adição."),
    # outros
    dict(id="s07", block="outros", text="Troque um hidrogênio do eteno por outro átomo, e muda o plástico. [p=0.3] {a}Com um cloro, o monômero é o cloreto de vinila, [p=0.2] {b}e o polímero é o pê vê cê, dos canos. [p=0.3] {c}Com os quatro hidrogênios trocados por flúor, [p=0.2] o monômero é {d}cê éfe dois, dupla, cê éfe dois, e sai o teflon, da frigideira que não gruda."),
    dict(id="s08", block="outros", text="{a}E com um anel de benzeno no lugar de um hidrogênio, o monômero é o estireno. [p=0.2] {b}O polímero é o poliestireno. [p=0.3] {c}Cheio de bolhas de gás, ele vira o isopor."),
    # erro
    dict(id="s09", block="erro", text="O erro mais comum é {a}deixar a dupla dentro do colchete. [p=0.3] {b}Se a dupla ficasse, cada carbono da cadeia teria cinco ligações, [p=0.2] e {c}o carbono só faz quatro. [p=0.3] {d}No polímero de adição, a unidade que se repete tem só ligações simples."),
    # atalho
    dict(id="s10", block="atalho", text="O atalho de prova, nos dois sentidos. [p=0.2] {a}Do monômero para o polímero: [p=0.1] {b}apague uma das ligações da dupla, [p=0.1] {c}ponha um traço em cada ponta, [p=0.1] {d}feche os colchetes e escreva o ene. [p=0.3] {e}Do polímero para o monômero: [p=0.1] {f}pegue a unidade de dois carbonos e devolva a dupla entre eles."),
    dict(id="s11", block="atalho", text="{a}Só não use o atalho quando a unidade tiver oxigênio ou nitrogênio ligando as partes da cadeia: [p=0.2] {b}aí é outro tipo de polímero, assunto da próxima aula."),
    # questão
    dict(id="s12", block="questao", text="Hora de testar. [p=0.2] {a}O polipropileno, dos potes de margarina, tem esta unidade: [p=0.2] {b}cê agá dois, cê agá com um cê agá três pendurado, entre colchetes, com o ene. [p=0.3] {c}Qual é o monômero?"),
    dict(id="s13", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s14", block="resposta", text="Pelo atalho: [p=0.2] {a}tire os colchetes e o ene, [p=0.2] {b}e devolva a dupla entre os dois carbonos da unidade. [p=0.3] {c}Fica cê agá dois, dupla, cê agá, cê agá três: [p=0.2] {d}o propeno."),
    # fechamento
    dict(id="s15", block="fim", text="Resumindo: [p=0.1] {a}o polímero é uma molécula gigante, feita de um monômero que se repete. [p=0.2] {b}No polímero de adição, a dupla do monômero abre e nada sai. [p=0.2] {c}Eteno dá polietileno, cloreto de vinila dá pê vê cê, [p=0.1] {d}e estireno dá o isopor."),
    dict(id="s16", block="fim", text="Na próxima aula, polímeros que nascem {a}soltando água a cada ligação: [p=0.2] {b}o PET das garrafas e o náilon. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
