# Roteiro — Seguridade Social 005: Contrapartida, noventena, imunidade e orçamento (Módulo M03 §5 e §7)
# Base: Estudos/Seguridade Social/modulos/M03-financiamento-e-orcamento-art-195.md
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa

TITULO = "Contrapartida, noventena, imunidade e orçamento da Seguridade Social"

PRONUNCIA = {
    "INSS": "I N S S",
    "RGPS": "R G P S",
    "LDO": "L D O",
    "SUS": "SUS",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "Na aula passada, você viu *de onde vem* o dinheiro da seguridade. [p=0.4] {a}Hoje, os *parágrafos* do artigo cento e noventa e cinco. "
        "[p=0.4] {b}E é exatamente aqui que a banca *derruba muita gente.* [p=0.5] {c}Porque cada parágrafo esconde uma *palavra* ou um *número* "
        "que ela adora trocar."),
    dict(id="02", block="mapa", text=
        "{t}O caminho de hoje: [p=0.3] {a}a regra da *contrapartida,* [p=0.2] {b}as *novas fontes* de custeio, [p=0.2] {c}a *noventena,* "
        "[p=0.2] {d}a *imunidade* das entidades beneficentes, [p=0.2] {e}e o *orçamento* da seguridade."),

    # ================= §5 CONTRAPARTIDA =================
    dict(id="03", block="contra", text=
        "{t}Começando pela frase mais cobrada de toda a matéria, [p=0.2] o parágrafo quinto. [p=0.4] Guarde esta frase: [p=0.3] "
        "{a}nenhum benefício ou serviço da seguridade social poderá ser *criado,* *majorado* ou *estendido* [p=0.2] "
        "{b}sem a correspondente fonte de *custeio total.* [p=0.5] {c}É a regra da *contrapartida,* [p=0.2] ou da *preexistência do custeio.*"),
    dict(id="04", block="verbos", text=
        "{t}Repare nos *três verbos.* [p=0.3] {a}*Criado:* [p=0.2] um benefício novo. [p=0.3] {b}*Majorado:* [p=0.2] um aumento de valor. "
        "[p=0.3] {c}*Estendido:* [p=0.2] mais gente passa a receber. [p=0.5] {x}E a banca ataca de dois jeitos: [p=0.2] tira um dos verbos, "
        "[p=0.2] normalmente o *estendido,* [p=0.2] {y}ou troca custeio *total* por custeio *parcial.* [p=0.3] Nos dois casos: [p=0.2] *errado.*"),

    # ================= §4 COMPETÊNCIA RESIDUAL =================
    dict(id="05", block="residual", text=
        "{t}O parágrafo quarto diz que a lei pode criar *outras fontes* para manter ou expandir a seguridade. [p=0.4] "
        "{a}É a *competência residual.* [p=0.3] E ela segue o artigo cento e cinquenta e quatro, inciso um. [p=0.4] Isso quer dizer três exigências: "
        "[p=0.3] {r1}*lei complementar,* [p=0.2] {r2}*não cumulatividade,* [p=0.2] {r3}e fato gerador e base de cálculo *diferentes* dos que já existem."),
    dict(id="06", block="ouro_lei", text=
        "{t}E aqui está o ponto de ouro. [p=0.3] {a}Fonte que *já está* no artigo cento e noventa e cinco: [p=0.2] basta *lei ordinária.* "
        "[p=0.4] {b}Fonte *nova,* residual: [p=0.2] exige *lei complementar.* [p=0.5] "
        "{q}Questão: [p=0.2] nova fonte para expandir a seguridade pode ser criada por *lei ordinária.* [p=0.4] {r}*Errado!* [p=0.3] "
        "{x}Fonte residual exige lei complementar."),

    # ================= §6 NOVENTENA =================
    dict(id="07", block="noventena", text=
        "{t}Agora, o parágrafo sexto: [p=0.2] a *noventena.* [p=0.4] {a}As contribuições sociais só podem ser exigidas depois de *noventa dias* "
        "da publicação da lei que as criou ou modificou. [p=0.5] {b}E o detalhe que cai: [p=0.2] *não* se aplica a anterioridade *de exercício,* "
        "[p=0.2] aquela que obriga a esperar o ano seguinte."),
    dict(id="08", block="calendario", text=
        "{t}Na prática: [p=0.2] {a}uma contribuição publicada em *primeiro de dezembro* [p=0.3] {b}pode ser cobrada em *primeiro de março.* "
        "[p=0.4] {c}Não precisa esperar o exercício seguinte, [p=0.2] só os noventa dias. [p=0.5] "
        "{x}E a banca troca o número: [p=0.2] *sessenta* dias, [p=0.2] *cento e vinte* dias. [p=0.3] O número certo é *noventa.*"),

    # ================= §7 IMUNIDADE =================
    dict(id="09", block="imune", text=
        "{t}O parágrafo sétimo traz a pegadinha mais elegante da matéria. [p=0.4] {a}O texto diz: [p=0.2] são *isentas* de contribuição "
        "as entidades *beneficentes* de assistência social [p=0.2] que atendam às exigências da lei. [p=0.5] "
        "{b}Mas, como a regra está *na própria Constituição,* [p=0.2] {c}a natureza jurídica é de *imunidade,* [p=0.2] e não de isenção."),
    dict(id="10", block="isen_imun", text=
        "{t}Por quê? [p=0.3] {a}*Isenção* é uma dispensa dada por *lei.* [p=0.3] {b}*Imunidade* é uma proibição de tributar dada pela *Constituição.* "
        "[p=0.5] {c}Então leia o comando da questão: [p=0.2] se ela pede a *literalidade,* [p=0.2] a resposta é *isentas.* [p=0.3] "
        "{d}Se pede a *natureza jurídica,* [p=0.2] é *imunidade.*"),

    # ================= §9 e §11 =================
    dict(id="11", block="ampc", text=
        "{t}Mais dois parágrafos rápidos. [p=0.3] {a}O nono permite *alíquotas diferenciadas* para a empresa por quatro critérios: "
        "[p=0.3] {l1}*atividade* econômica, [p=0.2] {l2}*mão de obra* intensiva, [p=0.2] {l3}*porte* da empresa [p=0.2] "
        "{l4}e *condição* estrutural do mercado de trabalho. [p=0.4] {m}Para decorar: [p=0.2] *A, M, P, C.* [p=0.5] "
        "{x}Mas *base de cálculo* diferenciada, [p=0.2] *só* para receita e lucro. [p=0.2] *Nunca* para a folha."),
    dict(id="12", block="sessenta", text=
        "{t}E o parágrafo onze proíbe *moratória* e *parcelamento* acima de *sessenta meses.* [p=0.4] {a}Remissão e anistia, [p=0.2] "
        "só na forma de *lei complementar.* [p=0.5] {b}Mas atenção: [p=0.2] isso vale *apenas* para duas contribuições: [p=0.2] "
        "{c}a da *folha* de salários [p=0.2] {d}e a do *trabalhador.* [p=0.3] As contribuições *previdenciárias,* em sentido estrito."),

    # ================= ORÇAMENTO =================
    dict(id="13", block="loa", text=
        "{t}Agora, o orçamento. [p=0.3] {a}A lei orçamentária anual, a LOA, tem *três* orçamentos: [p=0.3] {o1}o *fiscal,* "
        "[p=0.2] {o2}o de *investimento* das empresas estatais, [p=0.2] {o3}e o da *seguridade social.* [p=0.4] {m}Para decorar: [p=0.2] *F, I, S.* "
        "[p=0.4] {x}Ou seja: [p=0.2] o orçamento da seguridade é *próprio,* [p=0.2] separado do orçamento fiscal."),
    dict(id="14", block="integrada", text=
        "{t}E quem monta a proposta? [p=0.3] {a}Saúde, previdência e assistência, [p=0.2] de forma *integrada,* [p=0.2] "
        "seguindo as metas da LDO. [p=0.4] {b}Mas fica *assegurada a cada área a gestão de seus recursos.* [p=0.5] "
        "{c}Elaboração *conjunta,* [p=0.2] gestão *separada.* [p=0.4] {d}E as receitas dos Estados, do Distrito Federal e dos Municípios "
        "ficam nos *próprios* orçamentos, [p=0.2] *não* no orçamento da União."),
    dict(id="15", block="vinculo", text=
        "{t}E um ponto que a banca adora. [p=0.3] {a}O dinheiro da contribuição sobre a *folha* e da contribuição do *trabalhador* "
        "[p=0.3] {b}só pode pagar *benefícios do RGPS.* [p=0.4] {c}Não pode custear a saúde, [p=0.2] nem a assistência. [p=0.4] "
        "{x}A integração da seguridade *não* derruba essa vinculação."),

    # ================= PEGADINHAS =================
    dict(id="16", block="pegadinhas", text=
        "{t}Agora, uma rodada de pegadinhas. [p=0.4] {p1}As contribuições sociais respeitam a anterioridade *de exercício.* [p=0.3] "
        "{r1}*Errado:* [p=0.2] só a *noventena.* [p=0.5] {p2}A vedação do parcelamento acima de sessenta meses alcança *todas* as contribuições. "
        "[p=0.3] {r2}*Errado:* [p=0.2] só a da folha e a do trabalhador. [p=0.5] {p3}A Constituição chama de *isentas* as entidades beneficentes. "
        "[p=0.3] {r3}*Certo.* [p=0.2] Essa é a literalidade."),
    dict(id="17", block="q_contra", text=
        "{t}E uma questão de lei seca: [p=0.3] {e}nenhum benefício ou serviço da seguridade social poderá ser criado ou majorado "
        "sem a correspondente fonte de custeio total. [p=0.6] {r}*Errado!* [p=0.3] {x}Faltou o verbo *estendido.*"),

    # ================= FECHAMENTO =================
    dict(id="18", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}criado, majorado ou estendido, [p=0.2] só com custeio *total.* [p=0.3] {b}Fonte nova: [p=0.2] *lei complementar.* "
        "[p=0.3] {c}Noventena: [p=0.2] *noventa dias,* sem anterioridade de exercício. [p=0.3] {d}Entidades beneficentes: [p=0.2] "
        "o texto diz *isentas,* [p=0.2] a natureza é *imunidade.* [p=0.3] {e}Parcelamento: [p=0.2] no máximo *sessenta meses.* [p=0.3] "
        "{f}E a LOA tem três orçamentos: [p=0.2] *F, I, S.*"),
    dict(id="19", block="cta", text=
        "Na próxima aula, a *saúde* na Constituição: [p=0.2] o SUS, suas diretrizes e o que a banca mais cobra. [p=0.4] "
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar a preparação completa para o INSS. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha caído na pegadinha da isenção e da imunidade? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
