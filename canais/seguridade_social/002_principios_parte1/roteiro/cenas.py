# Roteiro — Seguridade Social 002: Princípios (parte 1) — incisos I a III do art. 194 (Módulo M02 §1–4)
# Base: Estudos/Seguridade Social/modulos/M02-principios-e-objetivos-art-194.md
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa

TITULO = "Princípios da Seguridade Social (parte 1): universalidade, uniformidade e seletividade"

PRONUNCIA = {
    "INSS": "I N S S",
    "BPC": "B P C",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "Este é o assunto *mais cobrado* de toda a Seguridade Social: [p=0.3] {a}os *sete princípios* do artigo cento e noventa e quatro. "
        "[p=0.5] {b}E a banca adora pegar o candidato numa troca sutil, [p=0.2] {c}como *cobertura* e *atendimento,* [p=0.2] "
        "ou *igualdade* e *equivalência.* [p=0.5] {d}Nesta aula, a primeira parte: [p=0.2] os incisos *um, dois e três.*"),

    # ================= VISÃO GERAL =================
    dict(id="02", block="lista", text=
        "{t}O parágrafo único do artigo cento e noventa e quatro diz que o Poder Público vai organizar a seguridade "
        "com base em *sete objetivos.* [p=0.4] {i1}Um: universalidade. [p=0.2] {i2}Dois: uniformidade e equivalência. [p=0.2] "
        "{i3}Três: seletividade e distributividade. [p=0.2] {i4}Quatro: irredutibilidade. [p=0.2] {i5}Cinco: equidade no custeio. "
        "[p=0.2] {i6}Seis: diversidade da base de financiamento. [p=0.2] {i7}E sete: caráter democrático e descentralizado."),
    dict(id="03", block="mnemonico", text=
        "{t}Para decorar a ordem, use esta frase: [p=0.3] {f}*Um Universo Seleto Irredutível Equilibra Diversas Comunidades.* "
        "[p=0.5] {l}Cada palavra começa com a letra de um princípio, na ordem certa."),
    dict(id="04", block="nome", text=
        "{t}E um detalhe de nomenclatura que cai: [p=0.3] {cf}a Constituição chama esses itens de *objetivos.* [p=0.3] "
        "{lei}Já a Lei oito mil, duzentos e doze chama de *princípios e diretrizes.* [p=0.4] {x}Os dois nomes estão certos."),

    dict(id="04b", block="corte", text=
        "{t}E um corte que resolve metade das questões: [p=0.3] {p}os incisos um, dois, três e quatro falam da *prestação,* "
        "[p=0.2] ou seja, do que a pessoa *recebe.* [p=0.4] {c}Só o *cinco* e o *seis* falam de *custeio:* [p=0.2] de onde vem o dinheiro. "
        "[p=0.4] {g}E o *sete* fala da *gestão:* [p=0.2] quem manda. [p=0.4] {x}Se a questão fala de dinheiro *entrando,* [p=0.2] "
        "só pode ser o cinco ou o seis."),

    # ================= INCISO I =================
    dict(id="05", block="univ", text=
        "{t}Inciso um: [p=0.2] *universalidade da cobertura e do atendimento.* [p=0.4] {d}Repare que são *duas* universalidades no mesmo inciso. "
        "[p=0.4] {c}A *cobertura* fala dos *riscos:* [p=0.2] doença, velhice, morte, maternidade. [p=0.4] "
        "{a}O *atendimento* fala das *pessoas:* [p=0.2] o trabalhador urbano, o rural, o doméstico, o autônomo."),
    dict(id="06", block="univ", text=
        "{m}Para nunca mais confundir: [p=0.2] *cobertura é coisa;* [p=0.2] *atendimento é alguém.* [p=0.4] "
        "{o}A cobertura é *objetiva.* [p=0.2] {s}O atendimento é *subjetivo.*"),
    dict(id="07", block="absoluta", text=
        "{t}E atenção: [p=0.2] a universalidade *não é absoluta.* [p=0.4] {a}Ela é um *objetivo* a ser perseguido, [p=0.2] "
        "e convive com o caráter *contributivo* da Previdência. [p=0.4] {b}Ou seja: [p=0.2] por causa da universalidade, "
        "qualquer pessoa recebe benefício previdenciário sem contribuir? [p=0.3] {c}*Errado.*"),
    dict(id="07b", block="contra", text=
        "{t}E como seria uma *violação* da universalidade? [p=0.3] {a}Imagine uma lei que excluísse os trabalhadores rurais "
        "da proteção na velhice. [p=0.4] {b}Isso feriria a universalidade do *atendimento,* [p=0.2] porque deixaria um grupo de *pessoas* de fora."),
    dict(id="08", block="q_univ", text=
        "{t}Questão: [p=0.2] {e}a universalidade da cobertura diz respeito às *pessoas* alcançadas pela proteção, [p=0.2] "
        "e a do atendimento se refere aos *riscos* protegidos. [p=0.5] {r}*Errado!* [p=0.3] {x}A banca *inverteu.* [p=0.2] "
        "Cobertura é risco; atendimento é pessoa."),

    # ================= INCISO II =================
    dict(id="09", block="unif", text=
        "{t}Inciso dois: [p=0.2] *uniformidade e equivalência* dos benefícios e serviços às populações *urbanas e rurais.* [p=0.4] "
        "{u}A *uniformidade* garante os *mesmos tipos* de benefício para o urbano e o rural. [p=0.3] É o aspecto *qualitativo.* [p=0.4] "
        "{e}A *equivalência* garante *valores equivalentes.* [p=0.3] É o aspecto *quantitativo.*"),
    dict(id="10", block="unif", text=
        "{m}Uma imagem para lembrar: [p=0.2] *uniforme é roupa igual,* [p=0.2] ou seja, o *tipo.* [p=0.3] "
        "{e}*Equivalência é troco:* [p=0.2] o *valor.*"),
    dict(id="11", block="equiv", text=
        "{t}E aqui está o ponto que decide a questão: [p=0.3] {a}*equivalência não é igualdade.* [p=0.4] "
        "{b}A Constituição permite tratar o rural de forma diferente quando há justificativa. [p=0.4] "
        "{c}O maior exemplo: [p=0.2] o trabalhador rural se aposenta com *cinco anos a menos* de idade: [p=0.2] "
        "{d}sessenta anos o homem, [p=0.2] e cinquenta e cinco a mulher. [p=0.4] {e}Se a regra fosse igualdade absoluta, isso seria inconstitucional."),
    dict(id="12", block="q_unif", text=
        "{t}Questão: [p=0.2] {e}em razão da uniformidade e equivalência, é *vedado* à Constituição estabelecer idade reduzida "
        "para a aposentadoria do trabalhador rural. [p=0.5] {r}*Errado!* [p=0.3] {x}A própria Constituição fixa essa idade reduzida. "
        "[p=0.2] Equivalência admite diferença justificada."),

    # ================= INCISO III =================
    dict(id="13", block="sel", text=
        "{t}Inciso três: [p=0.2] *seletividade e distributividade* na prestação dos benefícios e serviços. [p=0.4] "
        "{s}A *seletividade* escolhe *o quê:* [p=0.2] quais prestações vão existir. [p=0.4] "
        "{d}A *distributividade* escolhe *para quem:* [p=0.2] atender primeiro quem mais precisa. [p=0.4] "
        "{m}Guarde: [p=0.2] *seleciona o quê, distribui para quem.*"),
    dict(id="14", block="sel_ex", text=
        "{t}Exemplos concretos: [p=0.3] {a}o *salário-família* e o *auxílio-reclusão* só são pagos a dependentes de segurado de *baixa renda.* "
        "[p=0.3] Isso é seletividade. [p=0.4] {b}E o *BPC,* pago a idosos e pessoas com deficiência em situação de miséria, "
        "[p=0.2] distribui renda a quem mais precisa. [p=0.4] {c}Por isso a distributividade tem caráter *redistributivo de renda.*"),
    dict(id="15", block="tensao", text=
        "{t}E a banca adora esta pergunta: [p=0.2] *universalidade e seletividade são incompatíveis?* [p=0.5] "
        "{u}A universalidade é o *ideal:* [p=0.2] proteger todos, contra tudo. [p=0.3] {s}A seletividade é o *limite realista:* "
        "[p=0.2] os recursos são finitos. [p=0.4] {r}Elas *não* se contradizem. [p=0.2] A seletividade é o que torna a universalidade *viável.*"),
    dict(id="16", block="q_sel", text=
        "{t}Questão: [p=0.2] {e}a restrição do salário-família aos dependentes de segurados de baixa renda é manifestação direta de qual objetivo? "
        "[p=0.5] {r}*Seletividade e distributividade.* [p=0.3] {x}O legislador *selecionou* a prestação [p=0.2] e a *distribuiu* para quem mais precisa."),

    dict(id="16b", block="pegadinhas", text=
        "{t}Agora, uma rodada rápida de pegadinhas. [p=0.4] {p1}A seletividade define *a quem* serão prestados os benefícios. "
        "[p=0.3] {r1}*Errado:* [p=0.2] isso é distributividade. [p=0.4] {p2}O princípio impõe *igualdade* de valores entre urbanos e rurais. "
        "[p=0.3] {r2}*Errado:* [p=0.2] é *equivalência.* [p=0.4] {p3}A universalidade do atendimento tem caráter *subjetivo.* "
        "[p=0.3] {r3}*Certo:* [p=0.2] ela alcança as pessoas."),

    # ================= FECHAMENTO =================
    dict(id="17", block="resumo", text=
        "{t}Resumindo os três primeiros: [p=0.3] {a}universalidade: [p=0.2] cobertura é *risco,* atendimento é *pessoa,* "
        "e não é absoluta. [p=0.3] {b}Uniformidade é o *tipo;* [p=0.2] equivalência é o *valor,* e não significa igualdade. [p=0.3] "
        "{c}Seletividade escolhe *o quê;* [p=0.2] distributividade escolhe *para quem.*"),
    dict(id="18", block="cta", text=
        "Na próxima aula, a *parte dois:* [p=0.2] irredutibilidade, equidade, diversidade da base de financiamento e a gestão quadripartite. "
        "[p=0.4] Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar a preparação completa para o INSS. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual desses três princípios você mais confunde? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
