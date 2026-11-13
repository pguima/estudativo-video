# Estudativo · QUI-ORG-001 — O carbono e as fórmulas orgânicas (Química · Química Orgânica · Cadeias carbônicas e hidrocarbonetos).
# Habilidade: usar as 4 ligações do carbono para passar uma fórmula em bastão para a fórmula molecular, contando os hidrogênios escondidos.
# Pré-requisitos: QUI-LIG-002 (Lewis: traço = par compartilhado; simples, dupla, tripla). Próxima: QUI-ORG-002 (classificar carbonos e cadeias).
# Marcas: {cue} animação · [p=0.2] pausa. Números por extenso. Primeira aula da Orgânica: guarda a linguagem visual da trilha (visual.py).
# Fatos: C tem Z = 6 (2 e 4 elétrons por camada) e faz 4 ligações; H faz 1, O faz 2, N faz 3 (aula de Lewis: H₂O, N₂).
# Contas: pentano C5H12 (3+2+2+2+3 = 12; 2·5+2 = 12); but-1-eno C4H8 (2+1+2+3 = 8; 10−2 = 8); erro com a dupla contada como 1: 3+2+2+3 = 10;
# etanol C2H6O (2·2+2 = 6, o O não muda); questão: pent-2-en-1-ol em bastão, C5H10O (3+2+1+1+2 = 9, +1 do OH = 10; 12−2 = 10).
# O pentano é um dos componentes da gasolina. Questão inédita, criada para esta aula.

TITULO = "O carbono e as fórmulas orgânicas"

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
    dict(id="s01", block="gancho", text="{a}Este zigue-zague é uma molécula inteira. [p=0.3] Não tem nenhuma letra, {b}mas tem cinco carbonos [p=0.1] {c}e doze hidrogênios escondidos. [p=0.3] {d}Onde eles estão?"),
    dict(id="s02", block="gancho", text="{a}Até o fim desta aula, você vai {b}achar cada carbono do desenho, [p=0.2] {c}contar os hidrogênios que ninguém escreveu [p=0.2] e {d}chegar à fórmula da molécula. [p=0.2] E ainda leva {e}um atalho de prova."),
    # lembrete
    dict(id="s03", block="lembrete", text="Você só precisa lembrar da estrutura de Lewis. [p=0.2] {a}Cada traço é uma ligação, um par de elétrons compartilhado. [p=0.2] {b}Dois traços são uma ligação dupla, [p=0.1] {c}três traços, uma tripla. [p=0.3] Se faltar essa aula, procure no canal."),
    # o carbono
    dict(id="s04", block="carbono", text="{a}A Química Orgânica estuda os compostos do carbono. [p=0.2] Eles estão {b}no combustível, {c}na comida {d}e nos remédios. [p=0.3] E tudo começa num número: [p=0.2] {e}quatro."),
    dict(id="s05", block="carbono", text="O carbono tem número atômico seis: [p=0.2] {a}dois elétrons na primeira camada [p=0.1] {b}e quatro na camada de valência. [p=0.3] {c}Cada um desses quatro faz uma ligação. [p=0.2] Por isso, {d}o carbono faz sempre quatro ligações."),
    dict(id="s06", block="carbono", text="{a}Os vizinhos mais comuns também têm o seu número. [p=0.2] {b}O hidrogênio faz uma ligação, [p=0.1] {c}o oxigênio faz duas [p=0.1] {d}e o nitrogênio, três. [p=0.3] Guarde esses números: eles resolvem a aula toda."),
    dict(id="s07", block="carbono", text="{a}As quatro ligações do carbono podem vir de jeitos diferentes. [p=0.2] {b}Quatro simples. [p=0.2] {c}Uma dupla e duas simples. [p=0.2] {d}Duas duplas. [p=0.2] {e}Ou uma tripla e uma simples. [p=0.3] {f}A dupla conta como duas ligações, a tripla como três, [p=0.1] e a soma dá sempre quatro."),
    # três jeitos de escrever
    dict(id="s08", block="formas", text="Veja três jeitos de escrever a mesma molécula: [p=0.2] o álcool comum, {a}cê dois agá seis ó. [p=0.3] {b}A fórmula estrutural mostra todos os átomos e todos os traços. [p=0.2] Confira: {c}cada carbono tem quatro traços, [p=0.1] {d}o oxigênio tem dois [p=0.1] {e}e cada hidrogênio, um."),
    dict(id="s09", block="formas", text="Escrever tudo isso cansa. [p=0.2] Por isso existe {a}a fórmula condensada: [p=0.1] cê agá três, cê agá dois, ó agá. [p=0.3] {b}Os hidrogênios vão junto do seu carbono, com o índice, [p=0.2] e {c}só ficam os traços entre os grupos."),
    dict(id="s10", block="formas", text="{a}E a mais curta de todas é a fórmula em bastão. [p=0.3] {b}Cada ponta sem letra e cada dobra do zigue-zague é um carbono. [p=0.2] {c}Os hidrogênios presos ao carbono não aparecem. [p=0.2] {d}Já os outros átomos, como o oxigênio, são escritos, [p=0.1] {e}com os hidrogênios deles."),
    # contar os hidrogênios
    dict(id="s11", block="contar", text="Como achar os hidrogênios escondidos? [p=0.2] {a}Use o número quatro. [p=0.2] Em cada carbono, {b}conte as ligações que aparecem no desenho. [p=0.2] {c}O que falta para quatro são hidrogênios."),
    dict(id="s12", block="contar", text="Volte ao zigue-zague do começo. [p=0.2] {a}A ponta tem uma ligação desenhada: [p=0.1] faltam três, {b}três hidrogênios. [p=0.3] {c}Cada dobra do meio tem duas: [p=0.1] faltam duas, {d}dois hidrogênios."),
    dict(id="s13", block="contar", text="Somando: [p=0.1] {a}três, mais dois, mais dois, mais dois, mais três, [p=0.1] {b}dá doze hidrogênios. [p=0.3] Com {c}cinco carbonos, a fórmula molecular, a dos símbolos e índices, [p=0.1] é {d}cê cinco agá doze. [p=0.3] {e}É o pentano, um dos componentes da gasolina."),
    # com ligação dupla
    dict(id="s14", block="dupla", text="E se houver uma ligação dupla? [p=0.2] {a}Neste bastão de quatro carbonos, a dupla fica na ponta. [p=0.3] {b}O primeiro carbono tem só a dupla: [p=0.1] duas ligações, dois hidrogênios. [p=0.2] {c}O segundo tem a dupla e uma simples: [p=0.1] três ligações, um hidrogênio. [p=0.2] {d}O terceiro tem duas: dois hidrogênios. [p=0.2] {e}E a última ponta, três."),
    dict(id="s15", block="dupla", text="{a}Dois, mais um, mais dois, mais três, [p=0.1] dá oito. [p=0.2] {b}Cê quatro agá oito."),
    # erro comum
    dict(id="s16", block="erro", text="{a}O erro mais comum é contar a dupla como uma ligação só. [p=0.3] {b}Aí o primeiro carbono parece ter três hidrogênios, [p=0.1] o segundo, dois, [p=0.2] {c}e a conta chega a dez."),
    dict(id="s17", block="erro", text="Mas, {a}com a dupla e mais três hidrogênios, esse carbono teria cinco ligações. [p=0.3] {b}E carbono com cinco ligações não existe. [p=0.3] {c}Confira sempre: em cada carbono, traços mais hidrogênios dão quatro."),
    # atalho
    dict(id="s18", block="atalho", text="{a}O atalho de prova para conferir o total. [p=0.2] {b}Se a cadeia é aberta e só tem ligações simples, [p=0.1] os hidrogênios são o dobro dos carbonos, mais dois. [p=0.3] {c}Cinco carbonos: o dobro é dez, mais dois, doze. [p=0.3] {d}Cada dupla tira dois hidrogênios, e cada tripla tira quatro. [p=0.2] {e}Quatro carbonos com uma dupla: [p=0.1] o dobro é oito, mais dois, dez, [p=0.1] menos dois, oito."),
    dict(id="s19", block="atalho", text="{a}Funciona porque a dupla usa uma ligação a mais de cada um dos seus dois carbonos: [p=0.1] são dois hidrogênios a menos. [p=0.3] {b}O oxigênio, preso por duas simples, não muda a conta: [p=0.1] {c}no álcool, dois carbonos dão seis hidrogênios. [p=0.3] {d}Só não vale se houver nitrogênio na molécula: [p=0.1] aí, conte carbono por carbono."),
    # questão
    dict(id="s20", block="questao", text="Hora de testar. [p=0.2] {a}Este bastão tem uma dupla e termina em ó agá. [p=0.3] {b}Qual é a fórmula molecular?"),
    dict(id="s21", block="questao", text="{a}Pause o vídeo e tente. [p=3.0]"),
    # resposta
    dict(id="s22", block="resposta", text="Comece pelos carbonos: [p=0.1] {a}a ponta da esquerda e as quatro dobras. [p=0.2] {b}O ó agá não é carbono. [p=0.2] {c}São cinco carbonos."),
    dict(id="s23", block="resposta", text="Os hidrogênios, carbono por carbono: [p=0.2] {a}três, [p=0.1] {b}dois, [p=0.1] {c}um, [p=0.1] {d}um, [p=0.1] {e}dois. [p=0.2] {f}E não esqueça o agá escrito no ó agá: mais um. [p=0.3] {g}São dez hidrogênios: [p=0.1] {h}cê cinco agá dez ó."),
    dict(id="s24", block="resposta", text="Pelo atalho: [p=0.1] {a}o dobro de cinco é dez, mais dois, doze. [p=0.2] {b}Menos dois da dupla, dez. [p=0.2] {c}E o oxigênio não muda nada. Confere."),
    # fechamento
    dict(id="s25", block="fim", text="Resumindo: [p=0.1] {a}o carbono faz quatro ligações, [p=0.2] e {b}no bastão, o que falta para quatro são os hidrogênios escondidos."),
    dict(id="s26", block="fim", text="Na próxima aula, você vai {a}classificar cada carbono e cada cadeia: [p=0.2] {b}aberta ou fechada, {c}ramificada, {d}insaturada e outras. [p=0.3] {e}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {f}Bons estudos!"),
]
