# Estudativo · QUI-ORG-018 — Reações de adição (Química · Química Orgânica · Reações orgânicas).
# Habilidade: escrever a adição de H2 e de HBr em um alceno, usar a regra de Markovnikov e explicar como o óleo vira margarina.
# Pré-requisitos: QUI-ORG-003. Próxima: QUI-ORG-019 (substituição: cloração de alcano e nitração do benzeno).
# Primeira aula do módulo Reações orgânicas: o visual.py guarda a linguagem visual das reações. Questão inédita.
# Marcas: {cue} animação · [p=0.2] pausa. Fórmulas por extenso: CH2=CH2 = "cê agá dois, dupla, cê agá dois".
# Fatos: hidrogenação com catalisador de níquel (na indústria, cerca de 150 a 200 °C); óleo vegetal tem cadeias com várias duplas;
# com menos duplas, a gordura fica sólida ou pastosa. Markovnikov (1870): o H vai para o carbono da dupla com mais hidrogênios.
# Nome de haleto (2-bromopropano) não foi ensinado: a aula diz "o bromo no carbono do meio". Catalisador: outra aula.

TITULO = "Reações de adição"

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
    dict(id="s01", block="gancho", text="{a}O óleo de soja é líquido. [p=0.2] {b}A margarina é pastosa. [p=0.3] Boa parte dessa diferença vem de {c}hidrogênio entrando nas ligações duplas do óleo. [p=0.3] {d}Esse encaixe tem nome: reação de adição."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}escrever a adição de agá dois e de agá bromo num alceno, [p=0.2] {c}usar a regra de Markóvnikov [p=0.2] e {d}explicar a margarina. [p=0.2] E ainda leva um {e}atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Lembre da aula de hidrocarbonetos: [p=0.2] {a}alceno tem uma ligação dupla entre carbonos, [p=0.2] e {b}o carbono faz sempre quatro ligações. [p=0.3] {c}A dupla conta como duas ligações."),
    # o que é adição
    dict(id="s04", block="adicao", text="Pense numa porta de duas folhas. [p=0.2] {a}Fechada, as folhas ficam presas uma na outra. [p=0.2] {b}Aberta, cada folha fica com um lado livre. [p=0.3] {c}A ligação dupla é parecida: [p=0.2] uma das duas ligações pode se abrir, {d}e cada carbono ganha uma vaga para um átomo novo."),
    dict(id="s05", block="adicao", text="Na adição, {a}duas moléculas viram uma só. [p=0.2] {b}A dupla vira simples, [p=0.2] {c}cada carbono da dupla recebe um pedaço da outra molécula, [p=0.2] e {d}nada sai."),
    # hidrogenação
    dict(id="s06", block="h2", text="O exemplo mais simples é o eteno, {a}cê agá dois, dupla, cê agá dois. [p=0.3] {b}Junte agá dois, com um metal como o níquel ajudando a reação. [p=0.3] {c}A dupla se abre, [p=0.2] {d}um hidrogênio vai para cada carbono, [p=0.2] e sai {e}o etano: cê agá três, cê agá três."),
    dict(id="s07", block="h2", text="Essa adição de hidrogênio se chama {a}hidrogenação. [p=0.3] {b}Confira os átomos: [p=0.2] antes, dois carbonos e seis hidrogênios, {c}contando os dois do agá dois. [p=0.2] Depois, {d}os mesmos dois carbonos e seis hidrogênios."),
    # margarina
    dict(id="s08", block="margarina", text="{a}O óleo vegetal tem moléculas compridas, com várias ligações duplas. [p=0.3] {b}Na fábrica, o óleo aquecido recebe hidrogênio, com níquel. [p=0.3] {c}Parte das duplas vira simples, [p=0.2] e {d}o óleo líquido vira uma gordura pastosa: [p=0.2] {e}a base da margarina."),
    # HBr e Markovnikov
    dict(id="s09", block="markov", text="Agora, troque o agá dois por {a}agá bromo, o brometo de hidrogênio. [p=0.3] {b}No eteno, tanto faz: [p=0.2] {c}o hidrogênio vai para um carbono e o bromo para o outro, [p=0.2] e os dois carbonos são iguais."),
    dict(id="s10", block="markov", text="Mas no propeno, {a}cê agá dois, dupla, cê agá, cê agá três, [p=0.2] os carbonos da dupla {b}são diferentes. [p=0.3] {c}O bromo vai para a ponta ou para o meio?"),
    dict(id="s11", block="markov", text="Quem responde é a {a}regra de Markóvnikov: [p=0.2] {b}o hidrogênio vai para o carbono da dupla que já tem mais hidrogênios. [p=0.3] {c}O cê agá dois tem dois, o cê agá tem um. [p=0.2] {d}Então o hidrogênio vai para o cê agá dois, [p=0.2] e {e}o bromo fica no carbono do meio."),
    # erro
    dict(id="s12", block="erro", text="O erro mais comum é {a}inverter a regra: [p=0.2] {b}pôr o hidrogênio no carbono com menos hidrogênios. [p=0.3] {c}Aí o bromo iria para a ponta, [p=0.2] e {d}esse produto sai em pouca quantidade: [p=0.1] o principal, que a prova cobra, tem o bromo no meio."),
    # atalho
    dict(id="s13", block="atalho", text="O atalho para não inverter: [p=0.2] {a}quem tem mais hidrogênio ganha mais hidrogênio. [p=0.3] É como dizer que {b}o rico fica mais rico. [p=0.3] O motivo vem do caminho da reação, que é mais fácil assim, [p=0.2] e esse detalhe fica para outra aula."),
    dict(id="s14", block="atalho", text="{a}Não perca tempo com a regra quando os dois átomos que entram são iguais, como no agá dois, [p=0.2] {b}ou quando a molécula é igual dos dois lados da dupla, como o eteno ou o but dois eno. [p=0.3] {c}Aí, qualquer lado dá o mesmo produto."),
    # questão
    dict(id="s15", block="questao", text="Hora de testar. [p=0.2] O but um eno é {a}cê agá dois, dupla, cê agá, cê agá dois, cê agá três. [p=0.3] {b}Na adição de agá bromo, em que carbono fica o bromo? [p=0.2] {c}E o que sai da adição de agá dois?"),
    dict(id="s16", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s17", block="resposta", text="Olhe os carbonos da dupla. [p=0.2] {a}O carbono um tem dois hidrogênios, [p=0.1] {b}o carbono dois tem um. [p=0.3] Quem tem mais ganha mais: [p=0.2] {c}o hidrogênio vai para o carbono um, [p=0.2] e {d}o bromo fica no carbono dois."),
    dict(id="s18", block="resposta", text="{a}Com agá dois, a regra nem entra: [p=0.2] um hidrogênio em cada carbono, [p=0.2] {b}e sai o butano, cê quatro agá dez."),
    # fechamento
    dict(id="s19", block="fim", text="Resumindo: [p=0.1] {a}na adição, a dupla se abre e duas moléculas viram uma. [p=0.2] {b}Com agá dois, é a hidrogenação da margarina. [p=0.2] {c}Com agá bromo, o hidrogênio vai para o carbono que já tem mais hidrogênios."),
    dict(id="s20", block="fim", text="Na próxima aula, a reação de substituição, [p=0.2] em que {a}um hidrogênio sai para outro átomo entrar no lugar, [p=0.2] como {b}o cloro num alcano. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
