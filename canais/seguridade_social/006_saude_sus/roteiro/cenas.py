# Roteiro — Seguridade Social 006: Saúde e SUS na Constituição (Módulo M04)
# Base: Estudos/Seguridade Social/modulos/M04-saude.md
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa

TITULO = "Saúde e SUS na Constituição: arts. 196 a 200"

PRONUNCIA = {
    "INSS": "I N S S",
    "RGPS": "R G P S",
    "SUS": "SUS",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "Uma pergunta rápida: [p=0.2] para ser atendido no SUS, [p=0.2] *você precisa ter contribuído* para o INSS? [p=0.6] "
        "{a}*Não.* [p=0.4] {b}E é exatamente essa ideia que a banca testa quando cobra *saúde.* [p=0.4] "
        "{c}Hoje, os artigos *cento e noventa e seis a duzentos* da Constituição."),

    # ================= CONCEITO =================
    dict(id="02", block="aberto", text=
        "{t}A saúde é o pilar *mais aberto* da seguridade. [p=0.4] {a}Ela não pergunta se você *contribuiu.* [p=0.3] "
        "{b}Não pergunta se você é *pobre.* [p=0.3] {c}Não pergunta se você é *filiado* a algum regime. [p=0.5] "
        "{d}Basta ser *pessoa.* [p=0.3] É a *universalidade plena.*"),

    # ================= ART. 196 =================
    dict(id="03", block="art196", text=
        "{t}Agora, o artigo mais cobrado do módulo, [p=0.2] o *cento e noventa e seis.* [p=0.4] Guarde esta frase: [p=0.3] "
        "{a}a saúde é *direito de todos* e *dever do Estado,* [p=0.3] {b}garantido mediante políticas *sociais e econômicas* "
        "[p=0.2] {c}que visem à *redução* do risco de doença e de outros agravos [p=0.3] {d}e ao acesso *universal e igualitário* "
        "[p=0.2] {e}às ações e serviços para sua *promoção, proteção e recuperação.*"),
    dict(id="04", block="desmonte", text=
        "{t}E a banca ataca cada pedaço dessa frase. [p=0.4] {a}*Direito de todos* vira direito dos *contribuintes.* [p=0.3] "
        "{b}*Dever do Estado* vira dever da *família* ou da *sociedade.* [p=0.3] {c}E o mais traiçoeiro: [p=0.2] *redução* do risco vira "
        "*eliminação* do risco. [p=0.4] {d}O texto fala em *redução.* [p=0.2] Nunca em eliminação."),
    dict(id="05", block="ppr", text=
        "{t}Mais dois detalhes. [p=0.3] {a}O acesso é *universal e igualitário.* [p=0.3] {b}A palavra *gratuito* *não* está no texto. "
        "[p=0.5] {c}E as três finalidades: [p=0.2] *promoção,* [p=0.2] *proteção* [p=0.2] e *recuperação.* [p=0.4] "
        "{m}Para decorar: [p=0.2] *P, P, R.*"),

    # ================= ART. 197 =================
    dict(id="06", block="art197", text=
        "{t}O artigo cento e noventa e sete diz que as ações e serviços de saúde são de *relevância pública.* [p=0.4] "
        "{a}Ao Poder Público cabe a *regulamentação,* [p=0.2] a *fiscalização* [p=0.2] e o *controle.* [p=0.2] *R, F, C.* [p=0.5] "
        "{b}Mas a *execução* pode ser direta, [p=0.2] por *terceiros,* [p=0.2] e também por *pessoa física ou jurídica de direito privado.*"),

    # ================= ART. 198 =================
    dict(id="07", block="art198", text=
        "{t}O artigo cento e noventa e oito cria o SUS. [p=0.3] {a}As ações e serviços públicos de saúde integram uma rede "
        "*regionalizada e hierarquizada* [p=0.2] {b}e constituem um *sistema único.* [p=0.3] Daí o nome. [p=0.5] "
        "{c}E são *três* diretrizes: [p=0.2] {d1}*descentralização,* [p=0.2] {d2}*atendimento integral* [p=0.2] "
        "{d3}e *participação da comunidade.* [p=0.4] {m}Para decorar: [p=0.2] *D, A, P.*"),
    dict(id="08", block="dap", text=
        "{t}E cada diretriz tem um complemento que cai. [p=0.4] {a}Descentralização, [p=0.2] com *direção única em cada esfera de governo.* "
        "[p=0.4] {b}Atendimento integral, [p=0.2] com *prioridade* para as atividades *preventivas,* [p=0.2] "
        "*sem prejuízo* dos serviços assistenciais. [p=0.4] {c}E participação da comunidade: [p=0.2] os *conselhos de saúde.*"),
    dict(id="09", block="q_dir", text=
        "{t}Questão: [p=0.2] {e}o SUS tem como diretriz a descentralização, com direção única em *âmbito federal.* [p=0.5] "
        "{r}*Errado!* [p=0.3] {x}A direção é única *em cada esfera de governo.* [p=0.3] Repare que a banca estragou só o final da frase."),

    # ================= ART. 199 =================
    dict(id="10", block="art199", text=
        "{t}O artigo cento e noventa e nove fala da iniciativa privada. [p=0.4] {a}A assistência à saúde é *livre* à iniciativa privada. "
        "[p=0.4] {b}E as instituições privadas podem participar do SUS de forma *complementar,* [p=0.2] por contrato ou convênio, "
        "[p=0.3] {c}com *preferência* para as *filantrópicas* e as *sem fins lucrativos.* [p=0.4] {d}Atenção: [p=0.2] *complementar,* "
        "[p=0.2] e não *suplementar.*"),
    dict(id="11", block="vedacoes", text=
        "{t}E três vedações. [p=0.3] {a}*Recurso público* para auxílio ou subvenção a instituição privada *com fins lucrativos:* "
        "[p=0.2] vedado. [p=0.4] {b}*Capital estrangeiro* na assistência à saúde: [p=0.2] vedado, [p=0.2] *salvo* nos casos previstos em lei. "
        "[p=0.4] {c}E a *comercialização* de órgãos, tecidos e sangue: [p=0.2] vedada, [p=0.2] e aqui *sem nenhuma ressalva.*"),

    # ================= ART. 200 =================
    dict(id="12", block="art200", text=
        "{t}Por fim, o artigo duzentos lista as competências do SUS, [p=0.2] {a}*além de outras atribuições,* nos termos da lei. "
        "[p=0.4] {b}Essa expressão torna o rol *exemplificativo.* [p=0.3] Se a questão disser *taxativo,* [p=0.2] está errada. [p=0.5] "
        "{c}E guarde: [p=0.2] a *saúde do trabalhador* é competência do *SUS.* [p=0.3] {d}No *saneamento básico,* o SUS *participa.* "
        "[p=0.2] {e}E no *meio ambiente,* ele *colabora.*"),

    # ================= CASO E COMPARATIVO =================
    dict(id="13", block="caso", text=
        "{t}Agora, um caso prático. [p=0.3] {a}Roberto é empresário, tem renda alta e tem *plano de saúde* particular. [p=0.3] "
        "{b}Ele procura uma emergência pública. [p=0.5] {c}O atendimento pode ser recusado por causa do plano? [p=0.3] *Não.* [p=0.3] "
        "{d}Pode ser cobrado por causa da renda? [p=0.3] *Também não.* [p=0.4] {e}A saúde é direito de *todos,* [p=0.2] "
        "com acesso universal e igualitário."),
    dict(id="14", block="tripe", text=
        "{t}E compare com os outros pilares. [p=0.3] {a}Na *saúde,* [p=0.2] todos. [p=0.2] Sem contribuição e sem teste de renda. "
        "[p=0.4] {b}Na *assistência,* [p=0.2] quem *dela necessitar.* [p=0.4] {c}E na *previdência,* [p=0.2] quem é *filiado* e *contribui.*"),

    # ================= PEGADINHAS =================
    dict(id="15", block="pegadinhas", text=
        "{t}Agora, uma rodada de pegadinhas. [p=0.4] {p1}O artigo cento e noventa e seis garante acesso universal e *gratuito.* [p=0.3] "
        "{r1}*Errado:* [p=0.2] é universal e *igualitário.* [p=0.5] {p2}As instituições privadas participam do SUS de forma *suplementar.* "
        "[p=0.3] {r2}*Errado:* [p=0.2] é *complementar.* [p=0.5] {p3}Compete ao SUS executar as ações de *saúde do trabalhador.* "
        "[p=0.3] {r3}*Certo.*"),
    dict(id="16", block="q_rol", text=
        "{t}E uma questão de lei seca: [p=0.3] {e}o rol de competências do SUS, no artigo duzentos, é *taxativo,* "
        "não admitindo ampliação por lei. [p=0.6] {r}*Errado!* [p=0.3] {x}*Além de outras atribuições:* [p=0.2] o rol é *exemplificativo.*"),

    # ================= FECHAMENTO =================
    dict(id="17", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}saúde é direito de *todos* e dever do *Estado.* [p=0.3] {b}*Redução* do risco, [p=0.2] nunca eliminação. "
        "[p=0.3] {c}Acesso *universal e igualitário,* [p=0.2] com *P, P, R.* [p=0.3] {d}Diretrizes do SUS: [p=0.2] *D, A, P,* "
        "com direção única *em cada esfera.* [p=0.3] {e}Privados no SUS: [p=0.2] *complementar.* [p=0.3] {f}E o rol do artigo duzentos é *exemplificativo.*"),
    dict(id="18", block="cta", text=
        "Na próxima aula, a *assistência social* e a *LOAS:* [p=0.2] para quem ela é, [p=0.2] seus objetivos e suas diretrizes. [p=0.4] "
        "Se essa aula te ajudou, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para acompanhar a preparação completa para o INSS. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você já tinha caído na pegadinha da *eliminação* do risco? [p=0.5] "
        "{bye}Bons estudos, e *até a próxima aula.* [p=1.5]"),
]
