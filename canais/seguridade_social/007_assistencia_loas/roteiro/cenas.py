# Roteiro — Seguridade Social 007: Assistência Social e LOAS (Módulo M05 §1–3)
# Base: Estudos/Seguridade Social/modulos/M05-assistencia-social-loas-bpc.md
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa

TITULO = "Assistência Social e LOAS: arts. 203 e 204 e a Lei 8.742"

PRONUNCIA = {
    "INSS": "I N S S",
    "BPC": "B P C",
    "LOAS": "LOAS",
    "SUAS": "SUAS",
    "CRAS": "CRAS",
    "CREAS": "CREAS",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "Saúde é para todos. [p=0.3] Previdência é para quem contribui. [p=0.4] {a}E a *assistência social?* [p=0.5] "
        "{b}Ela faz uma única pergunta: [p=0.3] *você precisa?* [p=0.5] {c}Hoje, os artigos *duzentos e três* e *duzentos e quatro* "
        "da Constituição [p=0.2] e a *LOAS,* [p=0.2] a Lei oito mil, setecentos e quarenta e dois."),

    # ================= ART. 203 =================
    dict(id="02", block="art203", text=
        "{t}Guarde esta frase, [p=0.2] a mais cobrada de todo o pilar. [p=0.4] {a}A assistência social será prestada "
        "*a quem dela necessitar,* [p=0.3] {b}*independentemente de contribuição* à seguridade social. [p=0.5] "
        "{c}Duas ideias: [p=0.2] exige *necessidade,* [p=0.2] e *não* exige contribuição."),
    dict(id="03", block="objetivos", text=
        "{t}E o artigo duzentos e três traz *seis* objetivos. [p=0.4] {o1}A proteção à *família,* à maternidade, à infância, "
        "à adolescência e à velhice. [p=0.3] {o2}O amparo às crianças e adolescentes *carentes.* [p=0.3] "
        "{o3}A integração ao *mercado de trabalho.* [p=0.3] {o4}A *habilitação e reabilitação* das pessoas com deficiência. "
        "[p=0.3] {o5}A garantia de *um salário mínimo* ao idoso e à pessoa com deficiência. [p=0.3] "
        "{o6}E a redução da *vulnerabilidade socioeconômica,* [p=0.2] incluída em dois mil e vinte e um."),
    dict(id="04", block="inciso5", text=
        "{t}E aqui está o ponto de ouro. [p=0.3] {a}O inciso *cinco* é a base constitucional do *BPC.* [p=0.4] "
        "{b}Mas repare na expressão: [p=0.2] *conforme dispuser a lei.* [p=0.4] {c}Quem fixa os requisitos concretos, [p=0.2] "
        "como a idade e a renda, [p=0.2] é a *LOAS.* [p=0.3] E isso fica para a próxima aula."),

    # ================= ART. 204 =================
    dict(id="05", block="art204", text=
        "{t}O artigo duzentos e quatro trata do *financiamento* e das *diretrizes.* [p=0.4] {a}O dinheiro vem do *orçamento da seguridade,* "
        "[p=0.2] além de outras fontes. [p=0.5] {b}E são *duas* diretrizes: [p=0.2] {d1}a *descentralização* político-administrativa [p=0.2] "
        "{d2}e a *participação da população,* [p=0.2] por meio de organizações representativas."),
    dict(id="06", block="competencias", text=
        "{t}E a descentralização reparte o trabalho. [p=0.3] {a}À *União* cabem a coordenação e as *normas gerais.* [p=0.4] "
        "{b}Aos *Estados* e *Municípios,* [p=0.2] a coordenação e a *execução* dos programas, [p=0.2] {c}junto com as entidades beneficentes. "
        "[p=0.5] {d}E os Estados e o Distrito Federal podem vincular até *zero vírgula cinco por cento* da receita tributária líquida "
        "a programas de inclusão social."),

    # ================= LOAS ART. 1º e 2º =================
    dict(id="07", block="loas1", text=
        "{t}Agora, a LOAS. [p=0.3] O artigo primeiro define a assistência social em quatro núcleos. [p=0.4] "
        "{n1}É *direito do cidadão* e *dever do Estado.* [p=0.3] {n2}É política de seguridade *não contributiva.* [p=0.3] "
        "{n3}Provê os *mínimos sociais.* [p=0.3] {n4}E garante o atendimento às *necessidades básicas.*"),
    dict(id="08", block="pvd", text=
        "{t}O artigo segundo traz os *objetivos* da LOAS. [p=0.3] São três: [p=0.2] {a}a *proteção social,* [p=0.2] "
        "{b}a *vigilância socioassistencial* [p=0.2] {c}e a *defesa de direitos.* [p=0.4] {m}Para decorar: [p=0.2] *P, V, D.*"),

    # ================= PRINCÍPIOS E DIRETRIZES =================
    dict(id="09", block="surid", text=
        "{t}O artigo quarto traz os *princípios.* [p=0.3] São cinco. [p=0.3] {l1}*Supremacia* do atendimento às necessidades sociais "
        "sobre a rentabilidade econômica. [p=0.3] {l2}*Universalização* dos direitos sociais. [p=0.3] {l3}*Respeito* à dignidade do cidadão. "
        "[p=0.3] {l4}*Igualdade* de direitos no acesso. [p=0.3] {l5}E *divulgação* ampla. [p=0.4] {m}Para decorar: [p=0.2] *S, U, R, I, D.*"),
    dict(id="10", block="vexatoria", text=
        "{t}E dentro do respeito à dignidade está a expressão de ouro: [p=0.4] {a}*vedando-se qualquer comprovação vexatória de necessidade.* "
        "[p=0.5] {b}Ou seja: [p=0.2] ninguém pode ser humilhado [p=0.2] para provar que precisa de ajuda. [p=0.3] Isso cai muito."),
    dict(id="11", block="dpp", text=
        "{t}E as *diretrizes* da LOAS, [p=0.2] no artigo quinto. [p=0.3] {a}Descentralização, [p=0.2] {b}participação da população, "
        "[p=0.2] {c}e uma terceira: [p=0.2] a *primazia da responsabilidade do Estado.* [p=0.5] {x}E aqui está a pegadinha. [p=0.3] "
        "Na *Constituição,* as diretrizes são *duas.* [p=0.3] {y}Na *LOAS,* são *três.* [p=0.3] A primazia do Estado *só está na lei.*"),

    # ================= SUAS =================
    dict(id="12", block="suas", text=
        "{t}E quem organiza tudo isso é o *SUAS,* [p=0.2] o Sistema Único de Assistência Social. [p=0.4] "
        "{a}Na proteção social *básica,* está o *CRAS:* [p=0.2] atende famílias vulneráveis, [p=0.2] *antes* de qualquer violação de direitos. "
        "[p=0.5] {b}Na proteção social *especial,* está o *CREAS,* [p=0.2] com *E* de *especializado:* [p=0.2] "
        "{c}atende quando a violação de direitos *já aconteceu.*"),
    dict(id="13", block="eventuais", text=
        "{t}E um detalhe que derruba muita gente. [p=0.3] {a}O *auxílio-natalidade* e o *auxílio-funeral* [p=0.2] "
        "{b}*não* são benefícios previdenciários. [p=0.4] {c}Hoje, eles são *benefícios eventuais* da assistência social, [p=0.2] "
        "{d}pagos em caso de *nascimento,* *morte,* [p=0.2] vulnerabilidade temporária [p=0.2] e calamidade pública."),

    # ================= PEGADINHAS =================
    dict(id="14", block="pegadinhas", text=
        "{t}Agora, uma rodada de pegadinhas. [p=0.4] {p1}A assistência social é prestada a quem dela necessitar, [p=0.2] "
        "*desde que* tenha contribuído. [p=0.3] {r1}*Errado:* [p=0.2] é *independentemente* de contribuição. [p=0.5] "
        "{p2}Auxílio-funeral é benefício *previdenciário.* [p=0.3] {r2}*Errado:* [p=0.2] é benefício *eventual* da assistência. [p=0.5] "
        "{p3}É vedada qualquer comprovação vexatória de necessidade. [p=0.3] {r3}*Certo.*"),
    dict(id="15", block="q_dir", text=
        "{t}E uma questão de prova: [p=0.3] {e}são diretrizes da assistência social, *previstas na Constituição,* "
        "a descentralização, a participação da população e a primazia da responsabilidade do Estado. [p=0.6] "
        "{r}*Errado!* [p=0.3] {x}A Constituição traz *duas.* [p=0.2] A primazia do Estado é da *LOAS.*"),

    # ================= FECHAMENTO =================
    dict(id="16", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}a quem dela necessitar, [p=0.2] *independentemente de contribuição.* [p=0.3] "
        "{b}Seis objetivos na Constituição, [p=0.2] e o inciso cinco é a base do *BPC.* [p=0.3] {c}Objetivos da LOAS: [p=0.2] *P, V, D.* "
        "[p=0.3] {d}Princípios: [p=0.2] *S, U, R, I, D.* [p=0.3] {e}Diretrizes: [p=0.2] *duas* na Constituição, [p=0.2] *três* na LOAS. "
        "[p=0.3] {f}E CRAS previne, [p=0.2] CREAS atua depois da violação."),
    dict(id="17", block="cta", text=
        "Na próxima aula, o tema que *mais cai* deste módulo: [p=0.2] o *BPC* [p=0.2] e o auxílio-inclusão. [p=0.4] "
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar a preparação completa para o INSS. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você sabia que o auxílio-funeral saiu da previdência? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
