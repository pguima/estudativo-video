# Roteiro — Seguridade Social 004: Financiamento — as fontes do art. 195 (Módulo M03 §1–4 e §6)
# Base: Estudos/Seguridade Social/modulos/M03-financiamento-e-orcamento-art-195.md
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa

TITULO = "Financiamento da Seguridade Social: as fontes do art. 195"

PRONUNCIA = {
    "INSS": "I N S S",
    "RGPS": "R G P S",
    "RPPS": "R P P S",
    "COFINS": "Cofins",
    "CSLL": "C S L L",
    "ETCI": "E T C I",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "A Seguridade Social paga aposentadorias, mantém o SUS e o BPC. [p=0.4] {a}Mas *de onde vem esse dinheiro?* [p=0.5] "
        "{b}A resposta está no *artigo cento e noventa e cinco* da Constituição. [p=0.4] {c}E ele é a base de toda a parte de *custeio* do edital."),

    # ================= DIRETA x INDIRETA =================
    dict(id="02", block="toda", text=
        "{t}A regra geral: [p=0.2] a seguridade é financiada por *toda a sociedade,* [p=0.2] de forma *direta* e *indireta.* [p=0.5] "
        "{i}*Indireta* é o dinheiro dos *orçamentos públicos:* [p=0.2] da União, dos Estados, do Distrito Federal e dos Municípios, "
        "que vem dos tributos em geral. [p=0.5] {d}*Direta* são as *contribuições sociais,* [p=0.2] pagas especificamente para a seguridade."),
    dict(id="03", block="solid", text=
        "{t}E isso é a *solidariedade* na prática: [p=0.3] {a}quem paga *não é necessariamente* quem recebe. [p=0.4] "
        "{b}E repare nos *quatro* entes: [p=0.2] União, Estados, Distrito Federal *e Municípios.* [p=0.3] "
        "{c}A banca adora tirar os Municípios, [p=0.2] ou dizer *somente a União.*"),

    # ================= AS 4 FONTES =================
    dict(id="04", block="etci", text=
        "{t}Agora, as contribuições sociais. [p=0.3] São *quatro* fontes, uma em cada inciso. [p=0.4] {i1}Um: [p=0.2] do *empregador* e da empresa. "
        "[p=0.3] {i2}Dois: [p=0.2] do *trabalhador* e demais segurados. [p=0.3] {i3}Três: [p=0.2] sobre a receita de *concursos de prognósticos,* "
        "[p=0.2] as loterias. [p=0.3] {i4}Quatro: [p=0.2] do *importador.* [p=0.5] {m}Para decorar: [p=0.2] *E, T, C, I.* "
        "[p=0.2] Empregador, trabalhador, concursos, importador."),

    # ================= INCISO I =================
    dict(id="05", block="emp", text=
        "{t}O inciso um tem *três bases.* [p=0.4] {a}A *folha de salários,* [p=0.2] {b}a *receita ou faturamento,* [p=0.2] {c}e o *lucro.* "
        "[p=0.4] {m}Folha, receita, lucro: [p=0.2] *F, R, L.* [p=0.2] Pense num *farol.* [p=0.5] "
        "{x}Na prática: [p=0.2] sobre a folha, a contribuição patronal; [p=0.2] sobre o faturamento, a COFINS; [p=0.2] e sobre o lucro, a CSLL."),
    dict(id="06", block="folha", text=
        "{t}E aqui está o ponto de ouro da folha de salários. [p=0.3] {a}A contribuição incide sobre o que é pago a *pessoa física* "
        "que presta serviço, [p=0.2] *mesmo sem vínculo de emprego.* [p=0.5] {b}Ou seja: [p=0.2] a empresa também contribui sobre o que paga "
        "a *autônomos* e *avulsos,* [p=0.2] e não só aos empregados. [p=0.4] {c}Mas *não* incide sobre pagamento a *pessoa jurídica.*"),
    dict(id="07", block="q_folha", text=
        "{t}Questão: [p=0.2] {e}a contribuição patronal incide *apenas* sobre a folha de salários dos *empregados.* [p=0.5] "
        "{r}*Errado!* [p=0.3] {x}Ela alcança qualquer pessoa física que preste serviço, [p=0.2] mesmo sem vínculo."),

    # ================= INCISO II =================
    dict(id="08", block="trab", text=
        "{t}O inciso dois é do *trabalhador* e dos demais segurados. [p=0.4] E a Reforma da Previdência trouxe *duas novidades.* [p=0.4] "
        "{a}Primeira: [p=0.2] *alíquotas progressivas,* conforme o salário de contribuição: [p=0.2] quem ganha mais, paga um percentual maior. "
        "[p=0.5] {b}Segunda: [p=0.2] *não incide* contribuição sobre *aposentadoria e pensão* concedidas pelo *RGPS.*"),
    dict(id="09", block="trab", text=
        "{c}E cuidado: [p=0.2] essa não incidência vale para o *RGPS.* [p=0.3] {d}Ela *não* se estende automaticamente "
        "aos servidores públicos, do *RPPS,* [p=0.2] que têm regras próprias."),

    # ================= INCISOS III e IV =================
    dict(id="10", block="loteria", text=
        "{t}O inciso três incide sobre a *receita* dos concursos de prognósticos: [p=0.2] loterias, sorteios e apostas. [p=0.4] "
        "{a}E a pegadinha: [p=0.2] incide sobre a receita *do concurso,* [p=0.2] {b}e *não* sobre o *prêmio* que o apostador ganha. [p=0.5] "
        "{c}E o inciso quatro alcança o *importador* de bens ou serviços do exterior."),

    # ================= LEI 8.212 =================
    dict(id="11", block="lei11", text=
        "{t}Agora, a Lei oito mil, duzentos e doze. [p=0.3] {a}O *artigo onze* diz que, no âmbito federal, o orçamento da seguridade tem *três* tipos de receita: "
        "[p=0.3] {r1}receitas da *União,* [p=0.2] {r2}receitas das *contribuições sociais* [p=0.2] {r3}e receitas de *outras fontes.*"),
    dict(id="12", block="lei11b", text=
        "{t}E a lei lista *cinco* contribuições sociais: [p=0.3] {a1}das *empresas,* sobre a remuneração; [p=0.2] {a2}dos *empregadores domésticos;* "
        "[p=0.2] {a3}dos *trabalhadores;* [p=0.2] {a4}das empresas, sobre *faturamento e lucro;* [p=0.2] {a5}e sobre os *concursos de prognósticos.* "
        "[p=0.5] {x}Repare: [p=0.2] a lei destaca o *empregador doméstico* numa alínea própria. [p=0.3] A Constituição não faz isso. [p=0.2] Isso cai."),
    dict(id="13", block="uniao", text=
        "{t}E o papel da *União?* [p=0.3] {a}Ela contribui com recursos adicionais do Orçamento Fiscal, [p=0.2] fixados na *lei orçamentária anual.* "
        "[p=0.5] {b}E mais: [p=0.2] a União é a *garantidora* do sistema. [p=0.3] {c}Se faltar dinheiro para pagar os benefícios de prestação continuada "
        "da Previdência, [p=0.2] *quem cobre é a União.*"),
    dict(id="14", block="outras", text=
        "{t}E as *outras fontes?* [p=0.3] {a}São receitas como multas, juros e atualização monetária, [p=0.2] {b}receitas patrimoniais e financeiras, "
        "[p=0.2] {c}doações e legados, [p=0.2] {d}e uma parte dos valores de bens apreendidos."),

    # ================= PEGADINHAS =================
    dict(id="15", block="pegadinhas", text=
        "{t}Agora, uma rodada de pegadinhas. [p=0.4] {p1}A seguridade é financiada *somente* pelas contribuições sociais. [p=0.3] "
        "{r1}*Errado:* [p=0.2] também pelos orçamentos públicos, a forma indireta. [p=0.5] {p2}A contribuição sobre loterias incide sobre o *prêmio* do apostador. "
        "[p=0.3] {r2}*Errado:* [p=0.2] incide sobre a *receita* do concurso. [p=0.5] {p3}A empresa contribui também sobre o que paga a autônomos. "
        "[p=0.3] {r3}*Certo.*"),
    dict(id="16", block="q_caput", text=
        "{t}E uma questão de lei seca: [p=0.3] {e}a seguridade será financiada por toda a sociedade, de forma direta e indireta, "
        "mediante recursos dos orçamentos da União, dos Estados, do Distrito Federal e dos Municípios, e das contribuições sociais. [p=0.6] "
        "{r}*Certo!* [p=0.3] {x}É o texto do artigo cento e noventa e cinco, [p=0.2] com os *quatro* entes."),

    # ================= FECHAMENTO =================
    dict(id="17", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}financiamento *direto e indireto,* por toda a sociedade. [p=0.3] {b}Quatro fontes: [p=0.2] *E, T, C, I.* "
        "[p=0.3] {c}Empresa: [p=0.2] folha, receita e lucro, o *farol.* [p=0.3] {d}Folha inclui pessoa física *sem vínculo.* [p=0.3] "
        "{e}Aposentadoria e pensão do RGPS *não* pagam contribuição. [p=0.3] {f}E a União cobre as insuficiências."),
    dict(id="18", block="cta", text=
        "Na próxima aula, os *parágrafos* do artigo cento e noventa e cinco: [p=0.2] a regra da contrapartida, a noventena, "
        "a imunidade das entidades beneficentes e o orçamento da seguridade. [p=0.4] "
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar a preparação completa para o INSS. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já conhecia o macete do farol? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
