# Roteiro — Tecnologia 002: Claude Dashboards, painéis de dados em linguagem natural
# Base: original/fonte_claude_dashboards.md (anúncio de 08/10/2026 + central de ajuda, via coberturas)
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa

TITULO = "Claude Dashboards: o Claude agora cria painéis de dados ao vivo"

# só para a narração provisória (edge-tts); a legenda mantém o texto original
PRONUNCIA = {
    "SQL": "S Q L",
    "BigQuery": "Big Quéri",
    "Redshift": "Red Shift",
    "ClickHouse": "Click Rouse",
    "Snowflake": "Snôu Flêik",
    "Databricks": "Data Bricks",
    "Salesforce": "Sêilsforce",
    "Grafana": "Grafana",
    "PostHog": "Post Rógue",
    "HIPAA": "Ripa",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "Quantas pessoas se cadastraram esta semana, [p=0.2] comparado com o mês passado? [p=0.5] "
        "{a}Numa empresa normal, [p=0.2] essa pergunta vira um *pedido para a equipe de dados,* [p=0.2] {b}uma fila, [p=0.2] "
        "e uma resposta que chega *dias depois.* [p=0.5] {c}E se você pudesse só *perguntar,* [p=0.2] e receber um *painel pronto,* "
        "[p=0.2] que ainda se *atualiza sozinho?*"),
    dict(id="02", block="intro", text=
        "{a}Esse é o *Claude Dashboards,* [p=0.2] o novo recurso da Anthropic. [p=0.5] "
        "{b}Ele foi lançado em *oito de outubro de dois mil e vinte e seis,* [p=0.2] em versão *beta,* [p=0.2] "
        "{c}junto com o *Claude Motion,* [p=0.2] que transforma conteúdo em animações curtas."),
    dict(id="03", block="mapa", text=
        "{t}Neste vídeo: [p=0.2] {a}o que é o Dashboards, [p=0.2] {b}como ele funciona por baixo, [p=0.2] "
        "{c}de onde vêm os dados, [p=0.2] {d}como criar o seu primeiro painel, [p=0.2] {e}como compartilhar, [p=0.2] "
        "{f}e os limites que você precisa conhecer."),

    # ================= O QUE É =================
    dict(id="04", block="oque", text=
        "{t}Primeiro, o que ele é. [p=0.3] {a}O Dashboards é um *modelo de artifact,* [p=0.2] e fica na aba *Artifacts,* "
        "[p=0.2] {b}ao lado do *Docs,* [p=0.2] do *Slides* [p=0.2] e do *Design.* [p=0.5] "
        "{c}Você conecta o Claude aos seus dados, [p=0.2] faz uma pergunta em *linguagem natural,* [p=0.3] "
        "{d}e ele monta um *painel com gráficos,* [p=0.2] que continua *atualizado* quando os dados mudam."),
    dict(id="05", block="diferenca", text=
        "{t}E isso é diferente de pedir um gráfico no chat. [p=0.4] {a}Um gráfico comum é uma *foto:* [p=0.2] "
        "mostra os números daquele momento. [p=0.5] {b}O painel é uma *janela:* [p=0.2] ele está ligado à *fonte de dados,* "
        "[p=0.2] {c}e quando você volta amanhã, [p=0.2] os números são *os de amanhã.*"),

    # ================= COMO FUNCIONA =================
    dict(id="06", block="fluxo", text=
        "{t}Por baixo, o fluxo tem três passos. [p=0.3] {s1}Um: [p=0.2] você *conecta* um banco de dados ou um aplicativo. [p=0.4] "
        "{s2}Dois: [p=0.2] você faz a *pergunta.* [p=0.4] "
        "{s3}Três: [p=0.2] para cada gráfico, [p=0.2] o Claude *escreve uma consulta SQL* [p=0.2] e roda essa consulta "
        "*direto na sua fonte de dados.* [p=0.5] {s4}Não é chute. [p=0.2] É o *número de verdade,* [p=0.2] calculado no seu banco."),
    dict(id="07", block="transparencia", text=
        "{t}E aqui está o ponto mais importante do recurso: [p=0.2] a *transparência.* [p=0.4] "
        "{a}Cada gráfico mostra a *consulta* que gerou o número, [p=0.2] {b}e o horário da *última atualização.* [p=0.5] "
        "{c}Clicou num número e ficou em dúvida? [p=0.2] Você abre a consulta, [p=0.2] {d}ou pede para o Claude *explicar* "
        "o que exatamente está sendo contado. [p=0.4] *Você não precisa confiar às cegas.*"),

    # ================= DADOS =================
    dict(id="08", block="fontes", text=
        "{t}E de onde vêm os dados? [p=0.3] {a}Dos principais *data warehouses* do mercado: [p=0.2] "
        "{a1}Amazon Redshift, [p=0.2] {a2}BigQuery, [p=0.2] {a3}ClickHouse, [p=0.2] {a4}Databricks [p=0.2] {a5}e Snowflake. [p=0.5] "
        "{b}E também dos *aplicativos* que você já conectou ao Claude, [p=0.2] como o *Salesforce.*"),
    dict(id="09", block="levar", text=
        "{t}E quando a análise precisa ir mais fundo, [p=0.2] {a}o painel pode ser levado para ferramentas de análise, "
        "[p=0.2] como *Grafana,* [p=0.2] *Mixpanel,* [p=0.2] *Amplitude,* [p=0.2] *PostHog* e outras. [p=0.4] "
        "{b}Looker, [p=0.2] Tableau [p=0.2] e monday.com [p=0.2] aparecem como *em breve.*"),

    # ================= EXEMPLOS =================
    dict(id="10", block="ex1", text=
        "{t}Agora, na prática. [p=0.3] O primeiro exemplo é o da própria Anthropic: [p=0.3] "
        "{a}compare os *cadastros desta semana* com os do *mês anterior.* [p=0.5] "
        "{b}O Claude escreve a consulta, [p=0.2] {c}monta o gráfico, [p=0.2] {d}e mostra *a variação* logo de cara. "
        "[p=0.4] Aquela pergunta que virava um pedido na fila [p=0.2] *vira uma conversa.*"),
    dict(id="11", block="ex2", text=
        "{t}O segundo: [p=0.2] um painel das *oportunidades de venda* no Salesforce. [p=0.4] "
        "{a}Por exemplo: [p=0.2] funil por etapa, [p=0.2] {b}valor em negociação, [p=0.2] {c}os maiores negócios abertos. [p=0.5] "
        "{d}E daí você continua a conversa: [p=0.2] *adicione um filtro por região,* [p=0.2] "
        "*mostre só o último trimestre.* [p=0.4] {e}O painel muda na sua frente."),

    # ================= COMO USAR =================
    dict(id="12", block="comecar", text=
        "{t}Quer criar o seu? [p=0.3] Existem três caminhos. [p=0.3] {a}Pedir um painel em *qualquer conversa.* [p=0.3] "
        "{b}Clicar em *Output* na caixa de mensagem [p=0.2] e escolher *Dashboards.* [p=0.3] "
        "{c}Ou abrir um *modelo de Dashboards* na aba Artifacts."),
    dict(id="13", block="dica", text=
        "{t}E a dica de ouro, [p=0.2] que vem da própria Anthropic: [p=0.3] {a}diga a *pergunta,* [p=0.2] "
        "*não o tipo de gráfico.* [p=0.5] {b}Em vez de pedir um gráfico de barras com tal coluna, [p=0.3] "
        "{c}pergunte: *quais produtos mais cresceram este mês?* [p=0.4] {d}Deixe o Claude escolher a melhor forma de mostrar."),
    dict(id="14", block="planos", text=
        "{t}Quem pode usar? [p=0.3] {a}O Dashboards está em beta nos *planos pagos.* [p=0.4] "
        "{b}No plano *Enterprise,* [p=0.2] ele vem *desligado:* [p=0.2] {c}o administrador precisa ativar nas configurações "
        "da organização, [p=0.2] na seção *Artifacts.*"),

    # ================= COMPARTILHAR =================
    dict(id="15", block="compartilhar", text=
        "{t}E dá para *compartilhar* o painel com a equipe, [p=0.2] {a}que pode inclusive *editar junto* com o Claude. [p=0.5] "
        "{b}Mas repare num detalhe de segurança: [p=0.2] {c}quem abre o painel usa as *próprias conexões.* [p=0.4] "
        "{d}Se a pessoa não tem acesso àquela fonte de dados, [p=0.2] o gráfico *não aparece* para ela. [p=0.4] "
        "{e}O painel não vaza dado para quem não tem permissão."),

    # ================= LIMITES =================
    dict(id="16", block="limites", text=
        "{t}E agora, os limites. [p=0.4] {a}Primeiro: [p=0.2] é *beta.* [p=0.2] A experiência ainda pode mudar. [p=0.5] "
        "{b}Segundo: [p=0.2] *não existe uma camada semântica.* [p=0.3] Cada gráfico define a métrica na sua própria consulta. "
        "[p=0.4] {c}Então *cliente ativo* pode ter uma definição num painel [p=0.2] e outra no painel do colega. "
        "[p=0.3] {d}Confira a consulta antes de levar o número para a reunião."),
    dict(id="17", block="custos", text=
        "{t}Terceiro: [p=0.2] {a}o uso conta no *limite do seu plano,* [p=0.2] {b}e o processamento no data warehouse "
        "é cobrado *pelo provedor,* à parte. [p=0.5] {c}E se você trabalha com *dados de saúde,* [p=0.2] atenção: "
        "[p=0.2] o recurso *não está coberto* pelo acordo de conformidade de saúde da Anthropic. [p=0.3] Deixe esses dados de fora."),

    # ================= FECHAMENTO =================
    dict(id="18", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}o Claude Dashboards transforma uma *pergunta* em um *painel ao vivo.* [p=0.4] "
        "{b}Cada gráfico é uma *consulta SQL* rodando direto na sua fonte, [p=0.2] {c}com a consulta *à mostra* "
        "e a hora da última atualização. [p=0.4] {d}Conecta aos grandes *data warehouses* e ao Salesforce, [p=0.2] "
        "{e}e respeita a *permissão de cada pessoa.* [p=0.4] {f}Só lembre: [p=0.2] é beta, [p=0.2] e *confira a consulta.*"),
    dict(id="19", block="cta", text=
        "Se esse vídeo te mostrou algo novo, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para não perder as próximas ferramentas. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual *pergunta* você faria primeiro para os seus dados? [p=0.5] "
        "{bye}*Até o próximo vídeo.* [p=1.5]"),
]
