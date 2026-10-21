# Roteiro — Seguridade Social 001: Conceito e o tripé (Módulo M01)
# Base: Estudos/Seguridade Social/modulos/M01-conceito-e-estrutura-da-seguridade-social.md
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa

TITULO = "O que é Seguridade Social: o tripé saúde, previdência e assistência"

PRONUNCIA = {
    "INSS": "I N S S",
    "SUS": "SUS",
    "BPC": "B P C",
    "LOAS": "LOAS",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "Se você vai fazer o concurso do INSS, [p=0.2] tudo começa por uma pergunta: [p=0.3] *o que é Seguridade Social?* [p=0.5] "
        "{a}Parece simples. [p=0.3] {b}Mas é exatamente aqui que a banca derruba muita gente, [p=0.2] trocando *uma única palavra* da lei. "
        "[p=0.5] {c}Nesta aula, você vai entender o conceito, o famoso *tripé,* [p=0.2] e as pegadinhas que mais caem."),

    # ================= OS TRÊS RISCOS =================
    dict(id="02", block="riscos", text=
        "{t}Imagine que a vida tem três tipos de risco que podem derrubar uma pessoa. [p=0.4] "
        "{r1}O primeiro: [p=0.2] *ficar doente.* [p=0.2] Alguém precisa cuidar da saúde dela. [p=0.4] "
        "{r2}O segundo: [p=0.2] *perder a capacidade de trabalhar,* por doença, idade ou morte. [p=0.2] Alguém precisa substituir a renda. "
        "[p=0.4] {r3}E o terceiro: [p=0.2] estar na *miséria,* mesmo sem nunca ter contribuído. [p=0.2] Alguém precisa garantir o mínimo."),
    dict(id="03", block="guarda", text=
        "{t}O Estado respondeu a esses três riscos com *três sistemas diferentes:* [p=0.3] {s}a *Saúde,* [p=0.2] {p}a *Previdência Social* "
        "[p=0.2] {a}e a *Assistência Social.* [p=0.4] {g}E colocou os três debaixo de um mesmo guarda-chuva: [p=0.2] a *Seguridade Social.* "
        "[p=0.5] {f}Guarde esta frase: [p=0.2] Seguridade é o *gênero.* [p=0.2] Saúde, Previdência e Assistência são as *espécies.*"),

    # ================= CONCEITO LEGAL =================
    dict(id="04", block="conceito", text=
        "{t}Agora, o conceito que cai na prova, do *artigo cento e noventa e quatro* da Constituição. [p=0.4] "
        "{l1}A seguridade social compreende um *conjunto integrado de ações* [p=0.2] {l2}de iniciativa dos *Poderes Públicos e da sociedade,* "
        "[p=0.2] {l3}destinadas a assegurar os direitos relativos à *saúde,* à *previdência* e à *assistência social.*"),
    dict(id="05", block="nucleos", text=
        "{t}Decore *três núcleos* dessa frase, porque a banca ataca cada um deles. [p=0.4] "
        "{n1}Primeiro: [p=0.2] *conjunto integrado de ações.* [p=0.2] Não é um órgão, [p=0.2] não é o INSS. [p=0.4] "
        "{n2}Segundo: [p=0.2] Poderes Públicos *e da sociedade.* [p=0.2] Não é exclusivo do Estado. [p=0.4] "
        "{n3}Terceiro: [p=0.2] saúde, previdência e assistência. [p=0.2] *Só essas três.* [p=0.2] Educação e moradia não entram."),
    dict(id="06", block="lei", text=
        "{t}E um bônus: [p=0.2] a *Lei oito mil, duzentos e doze,* de mil novecentos e noventa e um, [p=0.2] repete esse mesmo conceito no seu *artigo primeiro.* "
        "[p=0.4] {a}Uma decoreba só serve para *duas fontes.*"),

    # ================= ORGANIZAR x PARTICIPAR =================
    dict(id="07", block="organizar", text=
        "{t}Agora, uma distinção fina que cai *muito.* [p=0.4] {f}A sociedade *financia* a seguridade, [p=0.2] {p}e *participa* da gestão. "
        "[p=0.4] {o}Mas quem *organiza* é *só o Poder Público.* [p=0.4] {fr}Guarde a frase: [p=0.2] "
        "*o Poder Público organiza; a sociedade participa e financia.*"),
    dict(id="08", block="topografia", text=
        "{t}E onde a Seguridade está na Constituição? [p=0.3] {a}No *Título Oito,* [p=0.2] da *Ordem Social.* [p=0.3] "
        "{b}Capítulo Dois, [p=0.2] do artigo cento e noventa e quatro ao duzentos e quatro. [p=0.4] "
        "{x}E cuidado: [p=0.2] *não* é na Ordem Econômica. [p=0.2] Essa é uma pegadinha clássica."),

    # ================= O TRIPÉ =================
    dict(id="09", block="tripe", text=
        "{t}Agora, o coração da aula: [p=0.2] o *tripé.* [p=0.4] {s}A *Saúde* é para *todos,* [p=0.2] e não exige contribuição. "
        "[p=0.2] É o SUS. [p=0.4] {p}A *Previdência* é para *quem contribui:* [p=0.2] tem caráter *contributivo* e filiação *obrigatória.* "
        "[p=0.2] É o INSS. [p=0.4] {a}E a *Assistência* é para *quem dela necessitar,* [p=0.2] *independentemente de contribuição.*"),
    dict(id="10", block="spa", text=
        "{t}Para memorizar, pense num *SPA:* [p=0.3] {s}*S* de saúde, [p=0.2] {p}*P* de previdência, [p=0.2] {a}*A* de assistência. "
        "[p=0.4] {pg}E no SPA, só *um* serviço é pago: [p=0.2] o do meio. [p=0.3] A *Previdência* é a única que exige contribuição."),
    dict(id="11", block="ovelha", text=
        "{t}E repare que a Previdência é a *ovelha diferente.* [p=0.4] {a}Saúde e Assistência *não* exigem contribuição. "
        "[p=0.3] {b}A Previdência exige. [p=0.4] {c}Por isso, sempre que uma questão disser que algo vale para *toda* a Seguridade, "
        "[p=0.2] *teste primeiro na Previdência.* [p=0.2] É ali que a regra costuma quebrar."),

    # ================= GÊNERO x ESPÉCIE =================
    dict(id="12", block="genero", text=
        "{t}E a confusão número um do concurso: [p=0.3] {a}Seguridade Social *não* é sinônimo de Previdência Social. [p=0.4] "
        "{b}Toda Previdência é Seguridade. [p=0.3] {c}Mas nem toda Seguridade é Previdência. [p=0.3] "
        "{d}A Previdência é só *uma parte* do todo."),

    # ================= CASO PRÁTICO =================
    dict(id="13", block="caso", text=
        "{t}Vamos ver isso num caso. [p=0.3] {a}O Marcelo trabalha como ambulante e *nunca contribuiu* para a Previdência. [p=0.4] "
        "{b}Ele quebra o braço e vai ao hospital público. [p=0.3] {q1}Ele tem direito ao atendimento no SUS? [p=0.3] {r1}*Sim.* "
        "[p=0.2] A saúde é universal. [p=0.4] {q2}E ao auxílio por incapacidade do INSS? [p=0.3] {r2}*Não.* [p=0.2] "
        "A previdência é contributiva, e ele não é segurado."),
    dict(id="14", block="caso", text=
        "{q3}E se ele ficasse com um impedimento permanente e vivesse na miséria? [p=0.3] {r3}Aí poderia ter direito ao *BPC,* da Assistência, "
        "[p=0.2] que *independe* de contribuição. [p=0.5] {f}Um único fato, [p=0.2] *três respostas diferentes.* [p=0.3] "
        "É exatamente isso que a banca testa."),

    # ================= PEGADINHAS =================
    dict(id="15", block="pegadinhas", text=
        "{t}Agora, as pegadinhas, [p=0.2] no estilo certo ou errado. [p=0.4] "
        "{p1}A seguridade compreende ações de iniciativa *exclusiva* dos Poderes Públicos. [p=0.3] {r1}*Errado:* [p=0.2] é dos Poderes Públicos *e da sociedade.* "
        "[p=0.5] {p2}Compete ao Poder Público *e à sociedade* organizar a seguridade. [p=0.3] {r2}*Errado:* [p=0.2] organizar é só do Poder Público."),
    dict(id="16", block="pegadinhas2", text=
        "{p3}A seguridade abrange saúde, previdência, assistência *e educação.* [p=0.3] {r3}*Errado:* [p=0.2] educação não entra. [p=0.5] "
        "{p4}A assistência social exige *contribuição prévia.* [p=0.3] {r4}*Errado:* [p=0.2] ela independe de contribuição. [p=0.5] "
        "{p5}A seguridade está no título da *Ordem Econômica.* [p=0.3] {r5}*Errado:* [p=0.2] é na *Ordem Social.*"),

    # ================= QUESTÃO =================
    dict(id="17", block="questao", text=
        "{t}Uma questão de prova. [p=0.3] {e}Certo ou errado: [p=0.2] a seguridade social compreende um conjunto integrado de ações "
        "de iniciativa dos Poderes Públicos, [p=0.2] destinadas a assegurar os direitos relativos à saúde, à previdência e à assistência social. [p=0.6] "
        "{r}*Errado!* [p=0.3] {x}Repare: [p=0.2] a banca *tirou* a expressão *e da sociedade.* [p=0.3] Uma palavra a menos, e a frase fica errada."),

    # ================= RESUMO =================
    dict(id="18", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}Seguridade é o gênero; [p=0.2] saúde, previdência e assistência são as espécies. [p=0.3] "
        "{b}É um conjunto integrado de ações dos Poderes Públicos *e da sociedade.* [p=0.3] {c}Quem *organiza* é o Poder Público. "
        "[p=0.3] {d}Está na Ordem Social, artigos cento e noventa e quatro a duzentos e quatro. [p=0.3] {e}E só a Previdência é contributiva."),
    dict(id="19", block="cta", text=
        "Na próxima aula, você vai aprender os *princípios* da Seguridade Social, [p=0.2] que estão entre os assuntos que mais caem. [p=0.4] "
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar a preparação completa para o INSS. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual pegadinha você já caiu? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
