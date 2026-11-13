# Estudativo · QUI-ORG-011 — Praticando: achar as funções em moléculas reais (Química · Química Orgânica · Funções orgânicas).
# Habilidade: marcar todas as funções de moléculas como aspirina, adrenalina e penicilina.
# Pré-requisitos: QUI-ORG-006 a 010. Próxima: QUI-ORG-012 (ponto de ebulição dos orgânicos).
# Marcas: {cue} animação · [p=0.2] pausa. Prática: 5 questões inéditas, criadas para esta aula, sobre moléculas reais.
# Q1 vanilina (4-hidróxi-3-metoxibenzaldeído): aldeído, fenol, éter. Q2 aspirina (ácido acetilsalicílico): ácido carboxílico
# e éster (o O do éster encosta no anel, mas não tem H: não é fenol). Q3 adrenalina: 2 OH no anel (fenol), OH na cadeia (álcool),
# NH–CH3 (amina secundária). Q4 penicilina G: 2 amidas (cadeia lateral e anel de 4 átomos, o anel betalactâmico), ácido carboxílico,
# tioéter (S entre carbonos; "tio" foi ensinado na QUI-ORG-010). O anel betalactâmico impede a bactéria de montar a parede.

TITULO = "Praticando: achar as funções em moléculas reais"

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
    dict(id="s01", block="gancho", text="{a}Um comprimido para dor, [p=0.1] {b}o hormônio do susto [p=0.1] {c}e o primeiro antibiótico descoberto. [p=0.3] Na prova, eles vêm desenhados, [p=0.1] {d}e a pergunta é quase sempre a mesma: [p=0.1] quais funções estão aí?"),
    # lembrete
    dict(id="s02", block="lembrete", text="Você vai usar as funções das últimas cinco aulas. [p=0.2] {a}O método é um só: [p=0.1] {b}ache cada átomo que não é carbono nem hidrogênio [p=0.1] {c}e olhe os vizinhos dele. [p=0.3] Se faltar alguma aula, procure no canal. [p=0.2] {d}Em cada questão, pause e tente antes da resposta."),
    # questão 1
    dict(id="s03", block="q1", text="{a}Questão um, para aquecer. [p=0.2] {b}A vanilina dá o sabor de baunilha. [p=0.2] {c}Ela tem três grupos com oxigênio. [p=0.2] {d}Quais são as funções?"),
    dict(id="s04", block="q1", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s05", block="r1", text="{a}No alto, um carbono na ponta, com dupla com oxigênio e um agá: [p=0.1] aldeído. [p=0.3] {b}Embaixo, um ó agá direto no anel: [p=0.1] fenol. [p=0.3] {c}E, ao lado, um oxigênio entre o anel e um cê agá três: [p=0.1] éter. [p=0.3] {d}Aldeído, fenol e éter."),
    # questão 2
    dict(id="s06", block="q2", text="{a}Questão dois. [p=0.2] {b}A aspirina, o ácido acetilsalicílico. [p=0.3] {c}Quais são as duas funções com oxigênio?"),
    dict(id="s07", block="q2", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s08", block="r2", text="{a}Primeiro grupo: [p=0.1] carbonila com ó agá. [p=0.1] {b}Ácido carboxílico. [p=0.3] {c}Segundo grupo: [p=0.1] carbonila com um oxigênio simples, que se prende ao anel. [p=0.2] {d}Esse oxigênio tem carbono dos dois lados: [p=0.1] {e}éster."),
    dict(id="s09", block="r2", text="{a}A pegadinha: [p=0.1] o oxigênio do éster encosta no anel, [p=0.1] e muita gente marca fenol. [p=0.3] {b}Mas fenol precisa de ó agá. [p=0.2] {c}Aqui, o oxigênio não tem agá."),
    # questão 3
    dict(id="s10", block="q3", text="{a}Questão três. [p=0.2] {b}A adrenalina é o hormônio que acelera o coração no susto. [p=0.3] {c}Ela tem três oxigênios e um nitrogênio. [p=0.2] {d}Marque todas as funções."),
    dict(id="s11", block="q3", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s12", block="r3", text="{a}Os dois ó agá presos ao anel: [p=0.1] fenol. [p=0.3] {b}O ó agá da cadeia, num carbono só com simples: [p=0.1] álcool. [p=0.3] {c}E o nitrogênio, com um agá e dois carbonos, sem carbonila do lado: [p=0.1] amina."),
    dict(id="s13", block="r3", text="{a}Fenol, álcool e amina. [p=0.2] {b}Repare: no papel, os ó agá parecem iguais, [p=0.1] mas a função muda por causa do vizinho."),
    # questão 4
    dict(id="s14", block="q4", text="{a}Questão quatro. [p=0.2] {b}O cloranfenicol é um antibiótico antigo, usado até hoje em colírio. [p=0.3] {c}Ele tem cloro, nitrogênio e oxigênio. [p=0.2] {d}Quais funções aparecem?"),
    dict(id="s15", block="q4", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s16", block="r4", text="{a}Preso ao anel, o grupo ene ó dois: [p=0.1] nitrocomposto. [p=0.3] {b}Na cadeia, dois ó agá em carbonos só com simples: [p=0.1] dois álcoois. [p=0.3] {c}O nitrogênio de baixo está colado numa carbonila: [p=0.1] amida. [p=0.3] {d}E os dois cloros presos ao mesmo carbono: [p=0.1] haleto."),
    dict(id="s17", block="r4", text="{a}Nitrocomposto, álcool, amida e haleto. [p=0.2] {b}Aqui, o nitrogênio aparece duas vezes, [p=0.1] em funções diferentes: [p=0.1] um com dois oxigênios, o outro ao lado da carbonila."),
    # questão 5
    dict(id="s18", block="q5", text="{a}Questão cinco, a mais difícil. [p=0.2] {b}A penicilina, descoberta em mil novecentos e vinte e oito. [p=0.3] {c}Ela tem oxigênio, nitrogênio e enxofre. [p=0.2] {d}Quais funções aparecem?"),
    dict(id="s19", block="q5", text="{a}Pause o vídeo e tente. [p=3.0]"),
    dict(id="s20", block="r5", text="{a}Comece pelos nitrogênios. [p=0.2] {b}O de cima está colado numa carbonila: [p=0.1] amida. [p=0.3] {c}O do anel de quatro átomos também tem uma carbonila ao lado: [p=0.1] outra amida."),
    dict(id="s21", block="r5", text="{a}À direita, a carbonila com ó agá: [p=0.1] ácido carboxílico. [p=0.3] {b}E o enxofre, entre dois carbonos, [p=0.1] faz o papel do oxigênio do éter: [p=0.1] {c}é um tioéter, o atalho da aula passada."),
    dict(id="s22", block="r5", text="{a}Duas amidas, um ácido carboxílico e um tioéter. [p=0.3] {b}E a amida do anel de quatro átomos é a parte que impede a bactéria de montar a parede que protege a sua célula."),
    # fechamento
    dict(id="s23", block="fim", text="Resumindo o método: [p=0.1] {a}ache cada átomo que não é carbono nem hidrogênio, [p=0.1] {b}olhe os vizinhos [p=0.1] e {c}dê o nome da função. [p=0.3] {d}E cuidado com os pares parecidos: [p=0.1] fenol e álcool, [p=0.1] amida e amina, [p=0.1] éster e éter."),
    dict(id="s24", block="fim", text="Na próxima aula, começa outro módulo: [p=0.2] {a}por que o álcool e o ácido fervem bem acima do hidrocarboneto [p=0.1] e {b}por que os galhos baixam o ponto de ebulição. [p=0.3] {c}Inscreva-se para seguir o curso do começo ao fim. [p=0.2] {d}Bons estudos!"),
]
