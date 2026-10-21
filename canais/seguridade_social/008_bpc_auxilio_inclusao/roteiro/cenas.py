# Roteiro — Seguridade Social 008: BPC e auxílio-inclusão (Módulo M05 §4–6)
# Base: Estudos/Seguridade Social/modulos/M05-assistencia-social-loas-bpc.md
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa

TITULO = "BPC e auxílio-inclusão: art. 20 da LOAS e o BPC × benefício previdenciário"

PRONUNCIA = {
    "INSS": "I N S S",
    "BPC": "B P C",
    "LOAS": "LOAS",
    "RGPS": "R G P S",
    "CPF": "C P F",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "Ele é pago pelo *INSS.* [p=0.3] Vale *um salário mínimo* por mês. [p=0.3] {a}E mesmo assim, [p=0.2] *não* é previdência. "
        "[p=0.5] {b}Estou falando do *BPC,* [p=0.2] o benefício de prestação continuada, [p=0.2] o tema que *mais cai* na assistência social. "
        "[p=0.4] {c}Hoje, o artigo *vinte* da LOAS, [p=0.2] o *auxílio-inclusão* [p=0.2] e a comparação que a banca adora: "
        "[p=0.2] BPC contra benefício previdenciário."),

    # ================= CONCEITO =================
    dict(id="02", block="conceito", text=
        "{t}Primeiro, o conceito, [p=0.2] no artigo vinte da LOAS. [p=0.4] {a}O BPC é a garantia de *um salário mínimo mensal* "
        "[p=0.3] {b}à *pessoa com deficiência* [p=0.2] {c}e ao *idoso com sessenta e cinco anos ou mais* [p=0.4] "
        "{d}que comprovem *não possuir meios* de prover a própria manutenção, [p=0.2] *nem* de ser mantido pela família."),
    dict(id="03", block="natureza", text=
        "{t}E aqui está o ponto de ouro. [p=0.3] {a}A natureza do BPC é *assistencial.* [p=0.3] Não é previdenciária. [p=0.4] "
        "{b}Quem *opera* é o INSS, [p=0.2] {c}mas o dinheiro vem da *assistência social,* [p=0.2] e não do fundo do RGPS. [p=0.5] "
        "{d}Guarde esta frase: [p=0.2] *quem paga é o INSS,* [p=0.2] *mas quem manda é a LOAS.*"),

    # ================= REQUISITOS =================
    dict(id="04", block="idade", text=
        "{t}Vamos aos requisitos. [p=0.3] O primeiro é a idade. [p=0.4] {a}O Estatuto do Idoso considera idosa a pessoa com *sessenta* anos. "
        "[p=0.4] {b}Mas para o BPC, [p=0.2] a idade é *sessenta e cinco,* [p=0.2] para homem *e* para mulher. [p=0.5] "
        "{c}A banca troca sessenta por sessenta e cinco o tempo todo. [p=0.3] Não caia nessa."),
    dict(id="05", block="deficiencia", text=
        "{t}O segundo é a deficiência. [p=0.3] E aqui o conceito *não* é só médico. [p=0.4] {a}É preciso um *impedimento,* "
        "[p=0.2] físico, mental, intelectual ou sensorial, [p=0.3] {b}que, *em interação com barreiras,* [p=0.3] "
        "{c}obstrua a *participação plena* na sociedade. [p=0.5] {d}É o modelo *biopsicossocial.* [p=0.3] "
        "{e}Questão que define deficiência só pela doença [p=0.2] está *errada.*"),
    dict(id="06", block="longoprazo", text=
        "{t}E esse impedimento tem que ser de *longo prazo.* [p=0.3] {a}Longo prazo, [p=0.2] para a LOAS, [p=0.2] "
        "é o que produz efeitos por no mínimo *dois anos.* [p=0.5] {b}Por isso, a avaliação é *dupla:* [p=0.2] "
        "{c}*médica* e *social,* [p=0.2] feita por médico perito e por assistente social do INSS."),
    dict(id="07", block="renda", text=
        "{t}O terceiro é a renda. [p=0.3] {a}A renda familiar mensal *por pessoa* [p=0.2] tem que ser *igual ou inferior* "
        "a *um quarto* do salário mínimo. [p=0.5] {b}Essa é a regra geral, [p=0.2] no parágrafo terceiro do artigo vinte. "
        "[p=0.4] {c}A lei também permite *ampliar* esse limite até *meio* salário mínimo, [p=0.2] {d}olhando outros elementos, "
        "[p=0.2] como o grau da deficiência e os gastos com tratamento, [p=0.2] na forma do regulamento."),

    # ================= GRUPO FAMILIAR =================
    dict(id="08", block="familia", text=
        "{t}Mas renda de *quem?* [p=0.3] Do grupo familiar, [p=0.2] e ele tem um rol *fechado.* [p=0.4] "
        "{f1}O próprio requerente. [p=0.2] {f2}O cônjuge ou companheiro. [p=0.2] {f3}Os pais, [p=0.2] e, na falta de um deles, "
        "a madrasta ou o padrasto. [p=0.2] {f4}Os irmãos *solteiros.* [p=0.2] {f5}Os filhos e enteados *solteiros.* [p=0.2] "
        "{f6}E os menores tutelados. [p=0.4] {g}Todos, [p=0.2] *desde que vivam sob o mesmo teto.*"),
    dict(id="09", block="detalhes", text=
        "{t}Três detalhes decidem a questão. [p=0.4] {a}Um: [p=0.2] *solteiros.* [p=0.2] Irmão ou filho *casado* não entra, "
        "[p=0.2] mesmo morando junto. [p=0.4] {b}Dois: [p=0.2] *mesmo teto.* [p=0.2] Quem mora em outra casa não entra. [p=0.4] "
        "{c}Três: [p=0.2] o rol é *fechado.* [p=0.2] {d}*Avós,* netos, tios, sogros e cunhados *não* entram, [p=0.2] "
        "mesmo que vivam na mesma casa."),

    # ================= OS CINCO NÃOS =================
    dict(id="10", block="naos", text=
        "{t}Agora, decore como um bloco: [p=0.2] os *cinco nãos* do BPC. [p=0.4] {n1}*Não* exige contribuição. [p=0.3] "
        "{n2}*Não* exige carência. [p=0.3] {n3}*Não* tem décimo terceiro. [p=0.3] {n4}*Não* gera pensão por morte, [p=0.2] "
        "porque é *personalíssimo.* [p=0.3] {n5}E *não* pode ser acumulado."),
    dict(id="11", block="acumulacao", text=
        "{t}Mas a vedação de acumular tem *duas* exceções. [p=0.4] {a}O BPC pode ser recebido junto com a *assistência médica* "
        "[p=0.3] {b}e com a *pensão especial de natureza indenizatória.* [p=0.5] {c}Só essas duas. [p=0.2] "
        "Qualquer outra hipótese na alternativa, [p=0.2] está *errada.*"),
    dict(id="12", block="revisao", text=
        "{t}E o BPC *não* é vitalício. [p=0.3] {a}Ele é *revisto a cada dois anos,* [p=0.2] no artigo vinte e um. [p=0.3] "
        "{b}Repare: [p=0.2] dois anos de impedimento, [p=0.2] dois anos de revisão. [p=0.2] Mesmo número, [p=0.2] coisas diferentes. "
        "[p=0.5] {c}Ele *cessa* quando as condições são superadas, [p=0.2] ou com a *morte* do beneficiário. [p=0.4] "
        "{d}E se a pessoa com deficiência começar a *trabalhar?* [p=0.3] {e}O benefício é *suspenso,* [p=0.2] e não cancelado. "
        "[p=0.3] A lei *não quer punir* quem tenta trabalhar."),

    # ================= AUXÍLIO-INCLUSÃO =================
    dict(id="13", block="inclusao", text=
        "{t}E é aí que entra o *auxílio-inclusão,* [p=0.2] criado em dois mil e vinte e um, [p=0.2] no artigo vinte e seis A da LOAS. "
        "[p=0.4] {a}Ele é para a pessoa com deficiência *moderada ou grave* [p=0.2] que recebia o BPC [p=0.2] "
        "{b}e *passou a trabalhar,* [p=0.2] com remuneração de até *dois salários mínimos.* [p=0.4] {c}O valor é *metade* do BPC: "
        "[p=0.2] *cinquenta por cento.* [p=0.4] {d}E ele *não* se acumula com o BPC. [p=0.4] "
        "{m}Para decorar: [p=0.2] *metade do BPC para quem passou a trabalhar.*"),

    # ================= COMPARAÇÃO =================
    dict(id="14", block="comparacao", text=
        "{t}Agora, a comparação que *mais cai:* [p=0.2] BPC contra aposentadoria. [p=0.4] {r1}Contribuição, [p=0.2] "
        "carência e qualidade de segurado: [p=0.2] o BPC *não* exige; [p=0.2] a aposentadoria exige. [p=0.4] "
        "{r2}Teste de renda: [p=0.2] o BPC *exige;* [p=0.2] a aposentadoria, não. [p=0.4] {r3}Décimo terceiro e pensão por morte: "
        "[p=0.2] o BPC *não* tem; [p=0.2] a aposentadoria tem. [p=0.4] {r4}E a base: [p=0.2] o BPC vem do artigo *duzentos e três,* "
        "[p=0.2] e a aposentadoria, [p=0.2] do artigo *duzentos e um.*"),

    # ================= PEGADINHAS =================
    dict(id="15", block="pegadinhas", text=
        "{t}Agora, uma rodada de pegadinhas. [p=0.4] {p1}Faz jus ao BPC o idoso com *sessenta* anos ou mais. [p=0.3] "
        "{r1}*Errado:* [p=0.2] são *sessenta e cinco.* [p=0.5] {p2}Integram o grupo familiar os *avós* que vivam sob o mesmo teto. "
        "[p=0.3] {r2}*Errado:* [p=0.2] o rol é fechado. [p=0.5] {p3}O auxílio-inclusão corresponde a *cem por cento* do BPC. "
        "[p=0.3] {r3}*Errado:* [p=0.2] é *metade.*"),
    dict(id="16", block="q_pensao", text=
        "{t}E uma questão de prova: [p=0.3] {e}o BPC corresponde a um salário mínimo, *acrescido do abono anual,* "
        "[p=0.2] e, falecendo o titular, *converte-se em pensão por morte* aos dependentes. [p=0.6] {r}*Errado!* [p=0.3] "
        "{x}Dupla armadilha: [p=0.2] o BPC *não* tem décimo terceiro, [p=0.2] e *não* gera pensão."),

    # ================= FECHAMENTO =================
    dict(id="17", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}o BPC é *assistencial:* [p=0.2] quem paga é o INSS, [p=0.2] quem manda é a LOAS. [p=0.3] "
        "{b}Um salário mínimo, [p=0.2] idoso com *sessenta e cinco,* [p=0.2] ou pessoa com deficiência de *longo prazo.* [p=0.3] "
        "{c}Renda por pessoa de até *um quarto* do salário mínimo, [p=0.2] num grupo familiar *fechado.* [p=0.3] "
        "{d}Os cinco nãos, [p=0.2] e só *duas* exceções na acumulação. [p=0.3] {e}Revisão a cada *dois anos,* [p=0.2] "
        "e trabalho *suspende.* [p=0.3] {f}E o auxílio-inclusão é *metade* do BPC."),
    dict(id="18", block="cta", text=
        "Na próxima aula, [p=0.2] fechamos a temporada com a *previdência social:* [p=0.2] o artigo *duzentos e um* da Constituição. "
        "[p=0.4] Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar a preparação completa para o INSS. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você sabia que o BPC não tem décimo terceiro? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
