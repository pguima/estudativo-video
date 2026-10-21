# Roteiro — ENEM Química 01: Matéria, substâncias puras e misturas
# Base: Estudos/Enem/estudos/02-quimica/01-materia-substancias-misturas.html
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa
# Fórmulas escritas como se fala ("O dois", "H dois O"); na tela aparecem como O₂, H₂O.

TITULO = "Matéria, substâncias e misturas: a curva de aquecimento — Química ENEM do zero"

PRONUNCIA = {
    "ENEM": "Enem",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "Um gráfico simples: [p=0.2] {a}temperatura de um lado, [p=0.2] tempo do outro. [p=0.4] {b}A linha sobe... [p=0.3] "
        "{c}fica *reta* por um tempo... [p=0.3] {d}sobe de novo... [p=0.3] {e}e fica reta outra vez. [p=0.5] "
        "{f}Sem nenhuma análise química, esse desenho diz se o material é *puro* ou se é *mistura.* [p=0.4] "
        "{g}E é a questão mais cobrada deste assunto no ENEM."),
    dict(id="02", block="enem", text=
        "Este é o primeiro assunto de Química, [p=0.2] e ele aparece na prova de quatro jeitos: [p=0.3] {a}a *curva de aquecimento;* "
        "[p=0.2] {b}a contagem de *fases e componentes;* [p=0.2] {c}a classificação de materiais do *dia a dia;* [p=0.2] "
        "{d}e a *alotropia,* principalmente do carbono."),
    dict(id="03", block="mapa", text=
        "Nesta aula: [p=0.2] {a}substância pura e mistura; [p=0.2] {b}fases e componentes; [p=0.2] {c}a curva de aquecimento "
        "e as misturas que enganam o gráfico; [p=0.3] {d}e a alotropia."),

    # ================= MATÉRIA E PROPRIEDADES =================
    dict(id="04", block="materia", text=
        "{t}*Matéria* é tudo o que tem massa e ocupa lugar no espaço. [p=0.4] {g}As propriedades *gerais,* como massa e volume, "
        "[p=0.2] valem para *qualquer* matéria, [p=0.2] e por isso não identificam nada. [p=0.4] {e}Já as propriedades *específicas,* "
        "[p=0.2] como ponto de fusão, ponto de ebulição e densidade, [p=0.2] são a *impressão digital* de cada substância."),
    dict(id="05", block="estado", text=
        "{t}E com o ponto de fusão e o ponto de ebulição, [p=0.2] a temperatura decide o estado físico. [p=0.4] "
        "{s}Abaixo do ponto de fusão: [p=0.2] *sólido.* [p=0.3] {l}Entre os dois: [p=0.2] *líquido.* [p=0.3] {g}Acima do ponto de ebulição: "
        "[p=0.2] *gasoso.* [p=0.4] {h}O mercúrio funde a menos trinta e nove graus e ferve a trezentos e cinquenta e sete. [p=0.3] "
        "Por isso é o único metal *líquido* na temperatura ambiente."),

    # ================= PURA x MISTURA =================
    dict(id="06", block="roteiro", text=
        "{t}Agora, a classificação inteira cabe em *três perguntas.* [p=0.4] {a}Primeira: [p=0.2] há uma ou mais substâncias? "
        "[p=0.2] Uma só é *substância pura;* [p=0.2] mais de uma é *mistura.* [p=0.4] {b}Se for pura: [p=0.2] um ou mais elementos? "
        "[p=0.2] *Simples* ou *composta.* [p=0.4] {c}Se for mistura: [p=0.2] quantas fases? [p=0.2] *Homogênea* ou *heterogênea.*"),
    dict(id="07", block="simples", text=
        "{t}Substância *simples* tem um *único elemento:* [p=0.2] {a}como o gás oxigênio, O dois, [p=0.2] o nitrogênio e o ferro. [p=0.4] "
        "{b}*Composta* tem dois ou mais: [p=0.2] água, gás carbônico, sal de cozinha. [p=0.4] {c}E a pegadinha: [p=0.2] "
        "O dois tem *dois átomos,* [p=0.2] e mesmo assim é *simples.* [p=0.3] {d}O critério é o número de *elementos,* "
        "[p=0.2] nunca o número de átomos."),
    dict(id="08", block="q_simples", text=
        "{t}Questão: [p=0.2] quantas substâncias simples há nesta lista? [p=0.3] {e}O dois, [p=0.2] O três, [p=0.2] H dois O, "
        "[p=0.2] cloreto de sódio, [p=0.2] N dois, [p=0.2] C O dois [p=0.2] e ferro. [p=0.6] {s}Só um elemento: [p=0.2] O dois, O três, N dois e ferro. "
        "[p=0.4] {r}*Quatro.* [p=0.3] {x}Quem tirou o O dois e o N dois por terem dois átomos [p=0.2] marcou *dois,* e errou."),
    dict(id="09", block="misturas", text=
        "{t}E as misturas. [p=0.3] {a}*Homogênea* tem uma única fase: [p=0.2] o ar, [p=0.2] a água com sal dissolvido, [p=0.2] "
        "e até o aço, que é uma solução *sólida.* [p=0.4] {b}*Heterogênea* tem duas ou mais: [p=0.2] água e óleo, [p=0.2] o granito. "
        "[p=0.4] {c}E cuidado: [p=0.2] leite e sangue *parecem* uniformes, [p=0.2] mas ao microscópio mostram fases. [p=0.3] São *heterogêneos.*"),
    dict(id="10", block="gases", text=
        "{t}Uma regra que resolve muita questão: [p=0.2] {a}*toda mistura de gases é homogênea.* [p=0.4] Gases nunca formam camadas. "
        "[p=0.4] {b}E dois enganos do dia a dia: [p=0.2] o ar *não* é substância pura, [p=0.2] é mistura de gases. [p=0.3] "
        "{c}E a água *mineral* também não: [p=0.2] tem sais dissolvidos. [p=0.3] Só a água *destilada* se aproxima de uma substância pura."),

    # ================= FASES E COMPONENTES =================
    dict(id="11", block="fases", text=
        "{t}Agora, a pegadinha preferida do assunto. [p=0.4] {f}*Fase* é cada porção do sistema com aspecto *uniforme.* [p=0.4] "
        "{c}*Componente* é cada *substância* presente. [p=0.4] {x}São dois números *diferentes,* [p=0.2] contados por critérios diferentes. "
        "[p=0.3] E a prova adora perguntar os dois."),
    dict(id="12", block="gelo", text=
        "{t}Exemplo: [p=0.2] {a}um copo com água e *três cubos de gelo.* [p=0.4] {c}Componentes: [p=0.2] gelo e água são a mesma substância. "
        "[p=0.2] *Um.* [p=0.4] {f}Fases: [p=0.2] o líquido, [p=0.2] e o sólido. [p=0.2] *Duas.* [p=0.4] {x}Não são quatro: [p=0.2] "
        "pedaços da mesma substância, no mesmo estado, [p=0.2] contam como *uma só* fase."),
    dict(id="13", block="bronze", text=
        "{t}E o caso que mostra que os números são independentes: [p=0.3] {a}bronze, [p=0.2] água [p=0.2] e areia. [p=0.4] "
        "{f}O bronze é uma liga homogênea de cobre e estanho: [p=0.2] *uma* fase. [p=0.3] Mais a água e a areia: [p=0.2] *três fases.* "
        "[p=0.4] {c}Mas os componentes são cobre, estanho, água e areia: [p=0.2] *quatro.* [p=0.4] {x}Três fases, quatro componentes."),

    # ================= CURVA DE AQUECIMENTO =================
    dict(id="14", block="curva", text=
        "{t}Agora, a curva de aquecimento. [p=0.4] {a}Na substância *pura,* [p=0.2] o gráfico tem *dois patamares.* [p=0.4] "
        "{b}Enquanto ela muda de estado, [p=0.2] toda a energia vai para a mudança, [p=0.2] e a temperatura *não sobe.* [p=0.4] "
        "{c}O primeiro patamar é o ponto de *fusão.* [p=0.3] {d}O segundo, o ponto de *ebulição.*"),
    dict(id="15", block="curva", text=
        "{m}Numa mistura *comum,* [p=0.2] cada componente muda de estado numa temperatura diferente, [p=0.2] e o gráfico *sobe sem parar.* "
        "[p=0.3] Nenhum patamar. [p=0.4] {x}E atenção: [p=0.2] a curva só diz se é *pura* ou *mistura.* [p=0.3] "
        "Ela *não* diz se a substância é simples ou composta."),
    dict(id="16", block="enganam", text=
        "{t}Mas duas misturas *enganam* o gráfico, [p=0.2] com *um* patamar só. [p=0.4] {e}A *eutética* tem patamar na *fusão:* [p=0.2] "
        "como a solda de estanho e chumbo, [p=0.2] que funde a cento e oitenta e três graus. [p=0.4] {a}A *azeotrópica* tem patamar na *ebulição:* "
        "[p=0.2] como o álcool noventa e seis por cento, [p=0.2] que ferve perto de setenta e oito graus. [p=0.4] "
        "{m}Para não trocar: [p=0.2] *eutética* lembra *fundir;* [p=0.2] *azeotrópica* lembra *ferver.* [p=0.3] "
        "{p}E só a substância pura tem os *dois* patamares."),
    dict(id="17", block="q_solda", text=
        "{t}Questão: [p=0.2] {e1}uma liga de solda funde a cento e oitenta e três graus, [p=0.2] com temperatura *constante,* [p=0.3] "
        "{e2}mas ferve ao longo de uma *faixa* de temperatura. [p=0.4] {e3}O que ela é? [p=0.5] {s1}Um patamar só, [p=0.2] e na *fusão.* "
        "[p=0.4] {s2}*Mistura eutética.* [p=0.4] {x}Com dois patamares seria pura; [p=0.2] com o patamar na ebulição, azeotrópica."),

    # ================= ALOTROPIA =================
    dict(id="18", block="alotropia", text=
        "{t}Agora, a *alotropia:* [p=0.2] um mesmo elemento formando substâncias simples *diferentes.* [p=0.4] "
        "{a}O oxigênio forma o O dois, [p=0.2] o gás que a gente respira, [p=0.3] {b}e o O três, o *ozônio,* [p=0.2] "
        "que protege a atmosfera, [p=0.2] mas é tóxico perto do solo. [p=0.4] {c}Mesmo elemento, [p=0.2] substâncias *diferentes.*"),
    dict(id="19", block="carbono", text=
        "{t}E o mais cobrado: [p=0.2] o *carbono.* [p=0.4] {d}No *diamante,* [p=0.2] cada átomo se liga a outros quatro numa rede rígida: "
        "[p=0.2] é o material natural mais *duro.* [p=0.4] {g}No *grafite,* [p=0.2] os átomos formam folhas que *deslizam:* "
        "[p=0.2] ele é macio, e risca o papel. [p=0.4] {n}O *grafeno* é uma única folha, de um átomo de espessura, [p=0.2] "
        "e os *nanotubos* são folhas enroladas. [p=0.4] {x}Mesmo elemento: [p=0.2] a *estrutura* decide a propriedade."),

    # ================= COTIDIANO =================
    dict(id="20", block="cotidiano", text=
        "{t}E os materiais do dia a dia. [p=0.3] {a}Aço, bronze e latão são *ligas:* [p=0.2] misturas homogêneas. [p=0.4] "
        "{b}O ouro *dezoito quilates* tem dezoito partes de ouro em vinte e quatro: [p=0.2] setenta e cinco por cento. [p=0.3] "
        "O resto são outros metais. [p=0.2] *Mistura.* [p=0.4] {c}E o soro fisiológico é água com sal: [p=0.2] mistura homogênea."),
    dict(id="21", block="q_materiais", text=
        "{t}Questão: [p=0.2] qual destes é substância pura? [p=0.3] {e}Água mineral, [p=0.2] ouro dezoito quilates, [p=0.2] gás oxigênio, "
        "[p=0.2] ar filtrado [p=0.2] e granito. [p=0.6] {s1}Água mineral tem sais. [p=0.2] {s2}O ouro dezoito é liga. [p=0.2] "
        "{s3}Filtrar o ar tira partículas, mas não separa os gases. [p=0.2] {s4}E o granito é heterogêneo. [p=0.4] "
        "{r}Só o *gás oxigênio.*"),

    # ================= FECHAMENTO =================
    dict(id="22", block="estrategia", text=
        "{t}Na hora da prova: [p=0.3] {a}para classificar, [p=0.2] use as *três perguntas.* [p=0.3] {b}Diante de um gráfico, [p=0.2] "
        "*conte os patamares.* [p=0.3] {c}E diante de um sistema, [p=0.2] *conte duas vezes:* [p=0.2] primeiro as fases, "
        "[p=0.2] depois os componentes."),
    dict(id="23", block="erros", text=
        "{t}Os erros que mais custam pontos: [p=0.3] {e1}achar que O dois é composto porque tem dois átomos; [p=0.2] "
        "{e2}contar cada cubo de gelo como uma fase; [p=0.2] {e3}achar que temperatura constante prova que é puro; [p=0.2] "
        "{e4}achar que o ar ou a água mineral são puros; [p=0.2] {e5}e achar que a curva diz se é simples ou composta."),
    dict(id="24", block="cta", text=
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar toda a Química do ENEM do zero. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha caído na pegadinha dos *cubos de gelo?* [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
