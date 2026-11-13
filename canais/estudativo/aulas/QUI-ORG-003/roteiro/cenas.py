# Estudativo · QUI-ORG-003 — Nome dos hidrocarbonetos: prefixo, infixo e sufixo (Química · Química Orgânica · Cadeias carbônicas e hidrocarbonetos).
# Habilidade: dizer se um composto é alcano, alceno ou alcino, nomear pent-2-eno e reconhecer ciclo-hexano e benzeno.
# Pré-requisitos: QUI-ORG-002 (saturada, insaturada, aromática). Próxima: QUI-ORG-004 (cadeia principal, numerar, 2,3-dimetilbutano).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Nomes falados: pent-2-eno = "pent dois eno"; pent-2-ino = "pent dois ino".
# Fatos: GLP = propano + butano; gasolina e parafina = misturas de hidrocarbonetos; ciclo-hexano é solvente; benzeno C6H6
# (2·6+2 = 14, −2 do anel, −6 das três duplas = 6). Numeração pela ponta mais perto da dupla: pent-2-eno, não pent-3-eno.
# Questão: CH3–CH2–C≡C–CH3 = pent-2-ino (alcino). non/dec: novembro e dezembro eram o 9º e o 10º mês do calendário romano.
# Questão inédita, criada para esta aula.

TITULO = "Nome dos hidrocarbonetos: prefixo, infixo e sufixo"

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
    dict(id="s01", block="gancho", text="{a}Metano, [p=0.1] etano, [p=0.1] propano, [p=0.1] butano. [p=0.3] Com poucas peças, [p=0.1] você dá nome a milhares de moléculas. [p=0.2] {b}O nome de um hidrocarboneto é montado como um código, em três partes."),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai saber se um composto é {b}alcano, alceno ou alcino, [p=0.2] {c}dar nome ao pent dois eno [p=0.2] e {d}reconhecer o ciclo-hexano e o benzeno."),
    # lembrete
    dict(id="s03", block="lembrete", text="Da aula passada: [p=0.2] {a}cadeia sem dupla nem tripla é saturada; [p=0.1] {b}com dupla ou tripla, insaturada. [p=0.2] {c}E o anel de seis carbonos com duplas alternadas é aromático."),
    # hidrocarboneto
    dict(id="s04", block="hidrocarboneto", text="{a}Hidrocarboneto é o composto feito só de carbono e hidrogênio. [p=0.2] {b}O gás de cozinha, a parafina da vela e boa parte da gasolina são misturas deles. [p=0.3] {c}O nome tem três partes: [p=0.1] {d}prefixo, [p=0.1] {e}infixo [p=0.1] {f}e sufixo."),
    # prefixo
    dict(id="s05", block="prefixo", text="{a}O prefixo, no começo, conta os carbonos da cadeia. [p=0.2] {b}Met, como em metano, é um. [p=0.2] {c}Et, como em etano, dois. [p=0.2] {d}Prop, três. [p=0.2] {e}But, de butano, quatro."),
    dict(id="s06", block="prefixo", text="{a}Daí em diante, vêm números do grego e do latim, os mesmos das figuras: [p=0.2] {b}pent é cinco, como no pentágono; [p=0.1] {c}hex, seis; [p=0.1] {d}hept, sete; [p=0.1] {e}oct, oito, como no octógono; [p=0.1] {f}non, nove; [p=0.1] e {g}dec, dez."),
    # infixo e sufixo
    dict(id="s07", block="infixo", text="{a}O infixo, no meio do nome, diz o tipo de ligação entre carbonos. [p=0.2] {b}Com an, como em propano, só há simples. [p=0.2] {c}Com en, como em propeno, há uma dupla. [p=0.2] {d}Com in, como em propino, uma tripla."),
    dict(id="s08", block="infixo", text="{a}E o sufixo, no fim, diz o tipo de composto, que se chama função. [p=0.2] {b}Para hidrocarboneto, é a letra ó. [p=0.3] Juntando as peças: {c}propano tem três carbonos, só com simples. [p=0.2] {d}Eteno tem dois carbonos e uma dupla. [p=0.2] {e}Etino tem dois carbonos e uma tripla."),
    dict(id="s09", block="infixo", text="{a}O infixo também dá o nome da família. [p=0.2] {b}Com an, é alcano. [p=0.2] {c}Com en, alceno. [p=0.2] {d}Com in, alcino."),
    # posição da dupla
    dict(id="s10", block="posicao", text="Com quatro carbonos ou mais, a dupla e a tripla podem estar em lugares diferentes. [p=0.2] {a}Por isso, o nome diz onde elas estão. [p=0.2] {b}Numere a cadeia pela ponta mais perto da dupla ou da tripla. [p=0.2] {c}O número que vai no nome é o do primeiro carbono dela."),
    dict(id="s11", block="posicao", text="{a}Neste bastão de cinco carbonos, a dupla está mais perto da ponta da esquerda. [p=0.2] {b}Numerando por ali, ela fica entre o carbono dois e o três. [p=0.3] {c}Cinco carbonos: pent. [p=0.2] {d}Dupla no carbono dois: dois e en. [p=0.2] {e}Hidrocarboneto: ó. [p=0.2] {f}Pent dois eno."),
    dict(id="s12", block="posicao", text="{a}Em provas mais antigas, ele aparece como dois penteno. [p=0.2] É a mesma molécula, com o número na frente."),
    # anéis
    dict(id="s13", block="aneis", text="{a}Se a cadeia é fechada, o nome ganha ciclo na frente. [p=0.2] {b}Seis carbonos num anel, só com simples: [p=0.1] {c}ciclo-hexano, um solvente."),
    dict(id="s14", block="aneis", text="{a}E o anel aromático de seis carbonos tem nome próprio: [p=0.1] {b}benzeno, cê seis agá seis. [p=0.3] {c}Ele tem três duplas, mas ninguém dá a ele um nome com en: [p=0.1] {d}é benzeno, e pronto."),
    # erro comum
    dict(id="s15", block="erro", text="{a}O erro mais comum é numerar pela ponta errada. [p=0.2] {b}Contando da direita, a dupla do exemplo cai no carbono três: [p=0.1] {c}pent três eno. [p=0.3] {d}Mas a regra pede o menor número possível para a dupla: [p=0.1] {e}pent dois eno é o certo."),
    # atalho
    dict(id="s16", block="atalho", text="{a}O atalho para o infixo: [p=0.1] {b}siga a ordem das vogais: a, é, i. [p=0.2] {c}A primeira vogal é um traço, a simples. [p=0.1] {d}A segunda, dois traços, a dupla. [p=0.1] {e}A terceira, três traços, a tripla."),
    dict(id="s17", block="atalho", text="{a}E, para o prefixo, decore só os quatro primeiros: metano, etano, propano, butano. [p=0.2] {b}Do cinco em diante, pense numa figura: pentágono, hexágono, octógono. [p=0.3] {c}Para nove e dez, que não têm figura famosa, [p=0.1] {d}lembre de novembro e dezembro, que já foram o nono e o décimo mês do ano."),
    # questão
    dict(id="s18", block="questao", text="Hora de testar. [p=0.2] {a}Dê o nome deste hidrocarboneto [p=0.1] {b}e diga se ele é alcano, alceno ou alcino."),
    dict(id="s19", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s20", block="resposta", text="{a}A tripla está mais perto da ponta da direita. [p=0.2] {b}Numere por ali: ela começa no carbono dois. [p=0.3] {c}Cinco carbonos: pent. [p=0.2] {d}Tripla no carbono dois: dois e in. [p=0.2] {e}Hidrocarboneto: ó. [p=0.2] {f}Pent dois ino, [p=0.1] {g}um alcino."),
    # fechamento
    dict(id="s21", block="fim", text="Resumindo: [p=0.1] {a}o prefixo conta os carbonos, [p=0.1] {b}o infixo diz a ligação, [p=0.1] {c}o sufixo diz a função, [p=0.2] e {d}a numeração começa pela ponta mais perto da dupla ou da tripla."),
    dict(id="s22", block="fim", text="Na próxima aula, a cadeia ganha galhos: [p=0.2] você vai {a}achar a cadeia principal, numerar [p=0.1] e chegar a nomes como {b}dois, três, dimetilbutano. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
