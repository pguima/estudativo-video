# Roteiro — Seguridade Social 003: Princípios (parte 2) — incisos IV a VII do art. 194 (Módulo M02 §5–10)
# Base: Estudos/Seguridade Social/modulos/M02-principios-e-objetivos-art-194.md
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa

TITULO = "Princípios da Seguridade Social (parte 2): irredutibilidade, equidade, diversidade e gestão quadripartite"

PRONUNCIA = {
    "INSS": "I N S S",
    "RGPS": "R G P S",
    "RAT": "RAT",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "Na aula passada, você aprendeu os três primeiros princípios da Seguridade Social. [p=0.4] "
        "{a}Hoje, os quatro últimos: [p=0.2] {b}irredutibilidade, [p=0.2] {c}equidade, [p=0.2] {d}diversidade da base de financiamento [p=0.2] "
        "{e}e a gestão quadripartite. [p=0.5] {f}E cuidado: [p=0.2] aqui estão algumas das pegadinhas *mais perigosas* da matéria."),
    dict(id="02", block="lembrete", text=
        "{t}Só para relembrar o corte da aula passada: [p=0.3] {p}o inciso *quatro* ainda fala da *prestação,* [p=0.2] do que a pessoa recebe. "
        "[p=0.4] {c}O *cinco* e o *seis* falam do *custeio,* [p=0.2] de onde vem o dinheiro. [p=0.4] {g}E o *sete* fala da *gestão.*"),

    # ================= INCISO IV =================
    dict(id="03", block="irred", text=
        "{t}Inciso quatro: [p=0.2] *irredutibilidade do valor dos benefícios.* [p=0.4] {a}A ideia é simples: [p=0.2] "
        "depois de concedido, o valor do benefício *não pode cair.* [p=0.4] {b}Uma aposentadoria de três mil reais "
        "não pode virar dois mil e setecentos por um ato da administração."),
    dict(id="04", block="nominal", text=
        "{t}Mas aqui está o ponto que decide a questão: [p=0.2] *nominal ou real?* [p=0.5] "
        "{n}A irredutibilidade do artigo cento e noventa e quatro garante o valor *nominal:* [p=0.2] o número não pode diminuir. "
        "[p=0.2] E vale para *toda* a seguridade. [p=0.5] {r}Já a garantia do valor *real,* [p=0.2] ou seja, do *poder de compra,* "
        "com reajuste, [p=0.2] vem de *outro* artigo: [p=0.2] o *duzentos e um,* parágrafo quarto. [p=0.2] E é específica do *RGPS.*"),
    dict(id="05", block="nominal", text=
        "{x}E um detalhe: [p=0.2] não existe direito adquirido a um *índice específico* de reajuste. [p=0.3] "
        "{y}O que a lei garante é preservar o valor real, [p=0.2] pelos critérios que a própria lei define."),
    dict(id="06", block="piso", text=
        "{t}Agora, uma das *melhores pegadinhas* da matéria: [p=0.3] o piso de *um salário mínimo.* [p=0.4] "
        "{a}A Constituição diz que nenhum benefício que *substitua* o salário do segurado pode ser menor que o salário mínimo. "
        "[p=0.5] {b}Repare na palavra: [p=0.2] *substitua.* [p=0.4] {c}Por isso, o *salário-família* e o *auxílio-acidente* "
        "*podem* ser menores que o salário mínimo. [p=0.3] {d}Eles não substituem a renda: [p=0.2] são *complementares.*"),
    dict(id="07", block="q_piso", text=
        "{t}Questão: [p=0.2] {e}por força da irredutibilidade, o auxílio-acidente não pode ser fixado em valor *inferior* ao salário mínimo. "
        "[p=0.5] {r}*Errado!* [p=0.3] {x}O piso só vale para benefícios que *substituem* a renda. [p=0.2] "
        "O auxílio-acidente é *indenizatório.*"),

    # ================= INCISO V =================
    dict(id="08", block="equid", text=
        "{t}Inciso cinco: [p=0.2] *equidade na forma de participação no custeio.* [p=0.4] {a}Cada um contribui "
        "na medida da sua *capacidade econômica* [p=0.2] {b}e do *risco* que gera. [p=0.5] "
        "{c}E de novo: [p=0.2] *equidade não é igualdade.* [p=0.3] {i}Igualdade seria todo mundo pagar o mesmo. "
        "[p=0.3] {e}Equidade é cada um pagar conforme pode."),
    dict(id="09", block="equid_ex", text=
        "{t}Dois exemplos. [p=0.3] {a}Capacidade: [p=0.2] quem ganha mais paga alíquotas maiores. [p=0.4] "
        "{b}Risco: [p=0.2] uma mineradora, com alto risco de acidente, recolhe um percentual maior para o seguro de acidente do trabalho "
        "[p=0.2] do que um escritório de contabilidade. [p=0.5] {c}E a Constituição *autoriza* alíquotas diferenciadas "
        "conforme a atividade econômica, [p=0.2] o uso intensivo de mão de obra, [p=0.2] o *porte da empresa* [p=0.2] "
        "e a condição do mercado de trabalho."),
    dict(id="10", block="q_equid", text=
        "{t}Questão: [p=0.2] {e}alíquotas diferenciadas para a empresa em razão do seu *porte* afrontam a equidade no custeio. "
        "[p=0.5] {r}*Errado!* [p=0.3] {x}Elas *concretizam* a equidade, [p=0.2] e são autorizadas pela própria Constituição."),

    # ================= INCISO VI =================
    dict(id="11", block="divers", text=
        "{t}Inciso seis: [p=0.2] *diversidade da base de financiamento.* [p=0.4] {a}A seguridade não pode depender de *uma única* fonte. "
        "[p=0.4] {b}Imagine se todo o dinheiro viesse só da folha de salários. [p=0.2] {c}Uma crise de desemprego quebraria o sistema."),
    dict(id="12", block="fontes", text=
        "{t}Por isso, ela é financiada por muitas fontes ao mesmo tempo: [p=0.3] {f1}a folha de salários, [p=0.2] {f2}o faturamento "
        "e o lucro das empresas, [p=0.2] {f3}a contribuição dos trabalhadores, [p=0.2] {f4}a receita das loterias [p=0.2] {f5}e a importação. "
        "[p=0.4] {o}Além dos orçamentos da União, dos Estados, do Distrito Federal e dos Municípios."),
    dict(id="13", block="ec103", text=
        "{t}E a Reforma da Previdência, a Emenda Constitucional cento e três, acrescentou *duas exigências* a esse inciso. [p=0.4] "
        "{a}Primeira: [p=0.2] receitas e despesas de saúde, previdência e assistência devem ser identificadas em *rubricas contábeis específicas* para cada área. "
        "[p=0.4] {b}Segunda: [p=0.2] fica *preservado o caráter contributivo* da previdência. [p=0.4] {c}Esse trecho é novo, [p=0.2] e as questões recentes cobram exatamente ele."),
    dict(id="14", block="exclusiv", text=
        "{t}E guarde a frase que é *sempre errada:* [p=0.3] {e}a seguridade social é financiada *exclusivamente* pelas contribuições dos *trabalhadores.* "
        "[p=0.5] {x1}Dois erros: [p=0.2] *exclusivamente* nega a diversidade, [p=0.3] {x2}e *dos trabalhadores* esquece as empresas, "
        "as loterias, a importação [p=0.2] e os orçamentos públicos."),

    # ================= INCISO VII =================
    dict(id="15", block="gestao", text=
        "{t}E o último: [p=0.2] inciso sete, [p=0.2] *caráter democrático e descentralizado da administração.* [p=0.4] "
        "{d}*Democrático,* porque a sociedade participa das decisões. [p=0.3] {s}*Descentralizado,* porque a administração é distribuída "
        "entre os entes e órgãos, [p=0.2] e não concentrada num só lugar."),
    dict(id="16", block="quadri", text=
        "{t}E essa participação se dá pela *gestão quadripartite,* [p=0.2] nos órgãos colegiados. [p=0.4] São *quatro* atores: "
        "[p=0.3] {a1}os *trabalhadores,* [p=0.2] {a2}os *empregadores,* [p=0.2] {a3}os *aposentados* [p=0.2] {a4}e o *Governo.* [p=0.5] "
        "{m}Para lembrar: [p=0.2] T, E, A, G. [p=0.2] *Tê, é, á, gê.*"),
    dict(id="17", block="falso", text=
        "{t}E a banca adora colocar um *quinto ator falso:* [p=0.3] {f1}sindicatos, [p=0.2] {f2}Ministério Público, [p=0.2] "
        "{f3}usuários, [p=0.2] {f4}servidores do INSS. [p=0.4] {x}Nenhum deles faz parte. [p=0.3] "
        "{y}E se a questão disser que a gestão é *tripartite,* [p=0.2] também está errada: [p=0.2] esqueceu os aposentados."),
    dict(id="18", block="lei", text=
        "{t}E um detalhe fino: [p=0.2] a Lei oito mil, duzentos e doze fala em participação de *trabalhadores, empresários e aposentados.* "
        "[p=0.4] {a}Mas a Constituição fala em gestão *quadripartite,* [p=0.2] *com o Governo.* [p=0.4] "
        "{b}Se a questão pedir *nos termos da Constituição,* [p=0.2] a resposta são os quatro."),
    dict(id="19", block="q_quadri", text=
        "{t}Questão: [p=0.2] {e}integram a gestão quadripartite, nos termos da Constituição: [p=0.4] {a}trabalhadores, empregadores, "
        "servidores públicos e Governo? [p=0.3] {b}Ou trabalhadores, empregadores, *aposentados* e Governo? [p=0.5] "
        "{r}A segunda. [p=0.2] *Trabalhadores, empregadores, aposentados e Governo.*"),

    # ================= FECHAMENTO =================
    dict(id="20", block="sintese", text=
        "{t}Agora, os *sete* princípios num quadro só. [p=0.4] {i1}Universalidade: [p=0.2] cobertura é risco, atendimento é pessoa. "
        "[p=0.3] {i2}Uniformidade é o tipo; equivalência, o valor. [p=0.3] {i3}Seletividade escolhe o quê; distributividade, para quem. "
        "[p=0.3] {i4}Irredutibilidade: o valor nominal não cai. [p=0.3] {i5}Equidade: cada um paga conforme pode. "
        "[p=0.3] {i6}Diversidade: várias fontes de dinheiro. [p=0.3] {i7}E a gestão quadripartite: [p=0.2] T, E, A, G."),
    dict(id="21", block="cta", text=
        "Na próxima aula, você vai aprender como a Seguridade é *financiada:* [p=0.2] as fontes do artigo cento e noventa e cinco. "
        "[p=0.4] Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar a preparação completa para o INSS. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já sabia que o auxílio-acidente pode ser menor que o salário mínimo? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
