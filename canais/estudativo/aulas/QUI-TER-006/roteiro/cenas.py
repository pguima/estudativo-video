# Estudativo · QUI-TER-006 — Energia de ativação e catalisador (Química · Termoquímica e Cinética · Cinética química).
# Habilidade: achar a energia de ativação em um diagrama e explicar que o catalisador a reduz sem mudar o ΔH, como as enzimas e o
# catalisador do carro.
# Pré-requisitos: QUI-TER-001, QUI-TER-005. Próxima: QUI-TER-007 (lei da velocidade e ordem de reação).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Questão inédita, criada para esta aula.
# Diagramas com valores de marca no eixo (a entalpia absoluta não se mede: o zero é referência), como na QUI-TER-001.
# Exemplo: reagentes 50, topo 130, produtos 10 ⇒ Ea = 80, ΔH = −40. Questão: reagentes 30, produtos 60, topo 100 / 70 ⇒ Ea 70 / 40,
# ΔH = +30. Fatos: a amilase da saliva quebra o amido (sabor adocicado do pão mastigado); o conversor catalítico usa platina,
# paládio e ródio e troca CO por CO₂ (e NOx por N₂).

TITULO = "Energia de ativação e catalisador"

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
    dict(id="s01", block="gancho", text="{a}Uma folha de papel, parada no ar, não pega fogo sozinha, [p=0.1] {b}mesmo que queimar libere muita energia. [p=0.3] {c}Basta um fósforo, e ela queima até o fim. [p=0.3] {d}Para que serve esse empurrão no começo?"),
    dict(id="s02", block="gancho", text="Até o fim da aula, você vai {a}achar a energia de ativação num diagrama [p=0.2] e explicar como {b}o catalisador acelera a reação [p=0.1] {c}sem mudar o delta agá."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você vai usar duas aulas. [p=0.2] {a}Delta agá é chegada menos partida, no diagrama de entalpia. [p=0.2] {b}E só a colisão efetiva forma produto: [p=0.1] a que tem a energia mínima e a posição certa. [p=0.2] Se faltar alguma, procure no canal."),
    # energia de ativação
    dict(id="s04", block="ativacao", text="{a}Aquela energia mínima tem nome: energia de ativação. [p=0.2] {b}Ela é como um morro no caminho entre reagentes e produtos. [p=0.3] {c}Sem energia para subir, a reação não acontece, [p=0.1] {d}mesmo que, no fim, ela libere energia."),
    dict(id="s05", block="ativacao", text="{a}No diagrama, o caminho ganha um morro. [p=0.2] {b}Os reagentes ficam num patamar, [p=0.1] {c}os produtos em outro, [p=0.1] e {d}no topo do morro fica o complexo ativado: [p=0.1] {e}um arranjo instável, no meio da troca de ligações."),
    dict(id="s06", block="ativacao", text="{a}A energia de ativação é a altura do morro, medida a partir dos reagentes. [p=0.2] {b}O delta agá continua sendo chegada menos partida. [p=0.3] {c}No papel, o fósforo dá a energia para subir o morro. [p=0.2] {d}Depois, a própria queima libera calor e empurra o resto da folha."),
    # exemplo resolvido
    dict(id="s07", block="exemplo", text="Veja um diagrama com números. [p=0.2] {a}Reagentes na marca de cinquenta quilojoules. [p=0.1] {b}Topo do morro em cento e trinta. [p=0.1] {c}Produtos em dez. [p=0.3] {d}Energia de ativação: cento e trinta menos cinquenta {e}dá oitenta. [p=0.2] {f}Delta agá: dez menos cinquenta {g}dá menos quarenta. [p=0.1] Exotérmica."),
    dict(id="s08", block="exemplo", text="{a}Morro baixo, mais colisões conseguem subir: [p=0.1] {b}reação rápida. [p=0.2] {c}Morro alto, poucas conseguem: [p=0.1] {d}reação lenta."),
    # catalisador
    dict(id="s09", block="catalisador", text="{a}O catalisador é uma substância que abre um caminho mais baixo. [p=0.2] {b}É um desvio por um morro menor. [p=0.3] {c}Com ele, o morro desce, [p=0.1] {d}mais colisões passam a ser efetivas [p=0.1] {e}e a reação acelera."),
    dict(id="s10", block="catalisador", text="{a}Repare no que não muda. [p=0.2] {b}Reagentes e produtos continuam nos mesmos patamares, [p=0.1] {c}então o delta agá é o mesmo. [p=0.3] {d}E o catalisador sai inteiro no fim: [p=0.1] ele participa, mas não é gasto."),
    dict(id="s11", block="catalisador", text="{a}Seu corpo é cheio de catalisadores: as enzimas. [p=0.2] {b}Na saliva, uma enzima quebra o amido do pão, [p=0.1] e ele fica adocicado na boca. [p=0.3] {c}No carro, o catalisador do escapamento tem metais como platina, paládio e ródio. [p=0.2] {d}Ele acelera a troca do monóxido de carbono, que é tóxico, por gás carbônico."),
    # erro comum
    dict(id="s12", block="erro", text="{a}O erro comum é medir a energia de ativação a partir do zero do eixo. [p=0.2] {b}No exemplo, daria cento e trinta. [p=0.3] {c}Mas a reação começa nos reagentes, [p=0.1] {d}e a subida que ela precisa vencer é só oitenta."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho para ler qualquer diagrama: [p=0.2] {a}energia de ativação é topo menos reagentes. [p=0.2] {b}Delta agá é produtos menos reagentes. [p=0.2] {c}Catalisador só abaixa o topo. [p=0.3] {d}Funciona porque as duas contas partem do mesmo lugar: o patamar dos reagentes."),
    dict(id="s14", block="atalho", text="{a}Cuidado se a questão pedir a reação de volta, dos produtos para os reagentes. [p=0.2] {b}Aí a partida é o patamar dos produtos: [p=0.1] {c}no exemplo, cento e trinta menos dez dá cento e vinte."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] Num diagrama, {a}os reagentes estão na marca de trinta quilojoules [p=0.1] {b}e os produtos, na de sessenta. [p=0.3] {c}O topo do morro fica em cem sem catalisador [p=0.1] {d}e em setenta com catalisador. [p=0.3] {e}Ache a energia de ativação nos dois casos e o delta agá."),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="{a}Sem catalisador: cem menos trinta {b}dá setenta. [p=0.2] {c}Com catalisador: setenta menos trinta {d}dá quarenta. [p=0.3] {e}Delta agá: sessenta menos trinta {f}dá mais trinta. [p=0.1] Endotérmica, {g}com ou sem catalisador."),
    # fechamento
    dict(id="s18", block="fim", text="Resumindo: [p=0.1] {a}energia de ativação é a subida a partir dos reagentes, [p=0.2] {b}e o catalisador abaixa essa subida sem mexer no delta agá."),
    dict(id="s19", block="fim", text="Na próxima aula, você vai {a}escrever a lei da velocidade [p=0.2] e {b}descobrir, numa tabela de experimentos, quanto cada reagente pesa na rapidez. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
