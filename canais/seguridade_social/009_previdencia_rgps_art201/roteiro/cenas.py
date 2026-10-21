# Roteiro — Seguridade Social 009: Previdência Social e RGPS — o art. 201 (Módulo M06)
# Base: Estudos/Seguridade Social/modulos/M06-previdencia-social-rgps-art-201.md
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa

TITULO = "Previdência Social e RGPS: o art. 201 da Constituição"

PRONUNCIA = {
    "INSS": "I N S S",
    "RGPS": "R G P S",
    "RPPS": "R P P S",
    "FAT": "FAT",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "Na saúde, ninguém paga para entrar. [p=0.3] Na assistência, também não. [p=0.4] {a}Mas na *previdência,* [p=0.2] "
        "a regra é outra: [p=0.3] {b}*ninguém entra de graça,* [p=0.3] {c}e *ninguém escolhe não entrar.* [p=0.5] "
        "{d}Hoje, o artigo *duzentos e um* da Constituição, [p=0.2] a última aula da primeira temporada."),

    # ================= CONCEITO =================
    dict(id="02", block="seguro", text=
        "{t}A previdência social é um *seguro.* [p=0.3] Mas um seguro diferente. [p=0.4] {a}No seguro privado, [p=0.2] "
        "você entra *se quiser.* [p=0.3] {b}Na previdência, [p=0.2] quem trabalha entra *por força de lei.* [p=0.5] "
        "{c}E ela é *solidária:* [p=0.2] {d}quem trabalha hoje [p=0.2] paga quem está aposentado hoje."),

    # ================= CAPUT =================
    dict(id="03", block="cfe", text=
        "{t}Agora, o *caput* do artigo duzentos e um. [p=0.3] Decore como um bloco. [p=0.4] {a}A previdência é organizada "
        "no *Regime Geral,* o RGPS, [p=0.3] {l1}de *caráter contributivo,* [p=0.3] {l2}de *filiação obrigatória,* [p=0.3] "
        "{l3}e com *equilíbrio financeiro e atuarial.* [p=0.5] {m}Para decorar: [p=0.2] *C, F, E.* [p=0.2] "
        "Contribui, filia, equilibra."),
    dict(id="04", block="fin_atu", text=
        "{t}E a banca adora perguntar a diferença. [p=0.4] {a}O equilíbrio *financeiro* é o curto prazo: [p=0.2] "
        "o que entra e o que sai *hoje.* [p=0.4] {b}O *atuarial* é o longo prazo: [p=0.2] a projeção, [p=0.2] "
        "com expectativa de vida e natalidade. [p=0.5] {c}E guarde: [p=0.2] esses três atributos são *exclusivos* da previdência. "
        "[p=0.3] Se a questão der isso à saúde ou à assistência, [p=0.2] está *errada.*"),

    # ================= RISCOS =================
    dict(id="05", block="riscos", text=
        "{t}E o que a previdência cobre? [p=0.3] São cinco incisos. [p=0.4] {r1}Um: [p=0.2] *incapacidade,* temporária ou permanente, "
        "[p=0.2] e *idade avançada.* [p=0.3] {r2}Dois: [p=0.2] a *maternidade,* [p=0.2] especialmente a gestante. [p=0.3] "
        "{r3}Três: [p=0.2] o *desemprego involuntário.* [p=0.3] {r4}Quatro: [p=0.2] *salário-família* e *auxílio-reclusão.* "
        "[p=0.3] {r5}Cinco: [p=0.2] a *pensão por morte.* [p=0.4] {m}Para decorar: [p=0.2] *I, M, D, S, M.*"),
    dict(id="06", block="armadilhas", text=
        "{t}E aqui estão duas armadilhas. [p=0.4] {a}O desemprego está no inciso três, [p=0.2] {b}mas o *seguro-desemprego* "
        "*não* é pago pelo INSS. [p=0.3] Ele vem do *FAT,* [p=0.2] o Fundo de Amparo ao Trabalhador. [p=0.5] "
        "{c}E o salário-família e o auxílio-reclusão [p=0.2] são devidos aos *dependentes* [p=0.2] {d}dos segurados de *baixa renda.* "
        "[p=0.4] {e}A banca troca dependentes por segurados, [p=0.2] ou apaga a baixa renda."),

    # ================= PARÁGRAFOS =================
    dict(id="07", block="p1", text=
        "{t}Agora, os parágrafos. [p=0.3] O primeiro *proíbe* critérios diferenciados para conceder benefícios. [p=0.4] "
        "{a}Mas abre *duas* exceções, [p=0.2] e só por *lei complementar.* [p=0.4] {b}Uma: [p=0.2] o segurado *com deficiência,* "
        "[p=0.2] com avaliação *biopsicossocial.* [p=0.4] {c}Duas: [p=0.2] quem tem *efetiva exposição* a agentes nocivos à saúde. "
        "[p=0.4] {d}E repare: [p=0.2] é *vedado* enquadrar por *categoria profissional.* [p=0.3] Não basta a profissão. "
        "[p=0.2] Tem que provar a exposição."),
    dict(id="08", block="p2", text=
        "{t}O parágrafo segundo garante o *piso.* [p=0.4] {a}Nenhum benefício que *substitua* o salário [p=0.2] "
        "terá valor inferior ao salário mínimo. [p=0.5] {b}E a palavra de ouro é *substitua.* [p=0.4] "
        "{c}Benefício que *não* substitui a renda pode ser menor: [p=0.2] {d}o *salário-família* [p=0.2] e o *auxílio-acidente.* "
        "[p=0.4] {e}Então, nenhum benefício abaixo do mínimo? [p=0.3] *Errado.*"),
    dict(id="09", block="p4p6", text=
        "{t}Mais dois parágrafos rápidos. [p=0.4] {a}O parágrafo quarto garante o reajuste para preservar o valor *real.* [p=0.4] "
        "{b}Não confunda com o artigo cento e noventa e quatro, [p=0.2] que garante o valor *nominal.* [p=0.5] "
        "{c}E o parágrafo sexto: [p=0.2] o décimo terceiro dos aposentados tem como base o valor de *dezembro.*"),
    dict(id="10", block="p5", text=
        "{t}E agora, uma das melhores pegadinhas da matéria: [p=0.2] o parágrafo quinto. [p=0.4] {a}Quem participa de *regime próprio,* "
        "[p=0.2] como o servidor efetivo, [p=0.3] {b}*não pode* se filiar ao RGPS como *facultativo.* [p=0.5] "
        "{c}Mas atenção: [p=0.2] se esse servidor tiver *outra atividade* que o RGPS abrange, [p=0.3] {d}ele entra como *obrigatório.* "
        "[p=0.4] {e}Ele não *escolhe* entrar. [p=0.2] Mas, se a atividade o obriga, [p=0.2] ele entra."),
    dict(id="11", block="p7", text=
        "{t}E o parágrafo sétimo traz as idades da aposentadoria, [p=0.2] desde a reforma de dois mil e dezenove. [p=0.4] "
        "{a}Na regra geral: [p=0.2] *sessenta e cinco* anos para o homem, [p=0.2] e *sessenta e dois* para a mulher, "
        "[p=0.2] com tempo mínimo de contribuição. [p=0.5] {b}Para o trabalhador *rural:* [p=0.2] *sessenta* e *cinquenta e cinco.* "
        "[p=0.4] {c}Cinco anos a menos. [p=0.3] É a *equivalência* na prática."),
    dict(id="12", block="p9", text=
        "{t}E o parágrafo nono: [p=0.2] a *contagem recíproca.* [p=0.4] {a}O tempo de contribuição *viaja* com o trabalhador, "
        "[p=0.2] entre o RGPS e o regime próprio. [p=0.4] {b}E os regimes *se compensam financeiramente.* [p=0.3] "
        "Eles acertam as contas entre si."),

    # ================= REGIMES =================
    dict(id="13", block="regimes", text=
        "{t}E onde o RGPS se encaixa? [p=0.3] {a}O *RGPS,* do artigo duzentos e um, [p=0.2] é o regime dos trabalhadores em geral, "
        "[p=0.2] gerido pelo *INSS.* [p=0.4] {b}O *regime próprio,* do artigo *quarenta,* [p=0.2] é o dos servidores efetivos. "
        "[p=0.4] {c}Os dois são públicos e *obrigatórios.* [p=0.4] {d}E a previdência *complementar,* do artigo duzentos e dois, "
        "[p=0.2] é *privada* [p=0.2] e *facultativa.*"),
    dict(id="14", block="servicos", text=
        "{t}E um detalhe que derruba muita gente. [p=0.3] {a}O RGPS paga *benefícios,* em dinheiro, [p=0.2] "
        "{b}mas também presta *serviços.* [p=0.4] E são só *dois:* [p=0.2] {c}o *serviço social* [p=0.2] "
        "{d}e a *reabilitação profissional.* [p=0.5] {e}A banca inventa um terceiro, [p=0.2] como a perícia médica. [p=0.3] Não caia."),

    # ================= PEGADINHAS =================
    dict(id="15", block="pegadinhas", text=
        "{t}Agora, uma rodada de pegadinhas. [p=0.4] {p1}A previdência tem caráter contributivo e filiação *facultativa.* [p=0.3] "
        "{r1}*Errado:* [p=0.2] a filiação é *obrigatória.* [p=0.5] {p2}A aposentadoria exige sessenta e cinco anos para o homem "
        "e *sessenta* para a mulher. [p=0.3] {r2}*Errado:* [p=0.2] são *sessenta e dois.* [p=0.5] "
        "{p3}O parágrafo quarto assegura a preservação do valor *real* dos benefícios. [p=0.3] {r3}*Certo.*"),
    dict(id="16", block="q_piso", text=
        "{t}E uma questão de prova: [p=0.3] {e}nenhum benefício previdenciário terá valor mensal *inferior ao salário mínimo.* "
        "[p=0.6] {r}*Errado!* [p=0.3] {x}O piso vale só para o benefício que *substitui* a renda. [p=0.2] "
        "O salário-família e o auxílio-acidente podem ser menores."),

    # ================= FECHAMENTO =================
    dict(id="17", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}o caput é *C, F, E:* [p=0.2] contributivo, filiação obrigatória e equilíbrio. [p=0.3] "
        "{b}Os riscos: [p=0.2] *I, M, D, S, M.* [p=0.3] {c}Piso de um salário mínimo, [p=0.2] só para benefício *substitutivo.* "
        "[p=0.3] {d}Quem tem regime próprio *não* vira facultativo. [p=0.3] {e}Idades: [p=0.2] *sessenta e cinco* e *sessenta e dois;* "
        "[p=0.2] no rural, *sessenta* e *cinquenta e cinco.* [p=0.3] {f}E os serviços do RGPS são só *dois.*"),
    dict(id="18", block="cta", text=
        "E com isso, [p=0.2] fechamos a *primeira temporada.* [p=0.3] Na próxima aula, [p=0.2] começamos o RGPS por dentro: "
        "[p=0.2] *segurados* e *dependentes.* [p=0.4] Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] "
        "{sub}*inscreva-se* no canal [p=0.2] {bell}e ative o *sininho,* para acompanhar a preparação completa para o INSS. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você sabia que o seguro-desemprego não é pago pelo INSS? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
