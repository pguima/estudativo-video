# Roteiro — Tecnologia 010: Claude Duet, o agente proativo da Anthropic
# Base: original/fonte_claude_duet.md (anúncio oficial em claude.com, 21/10/2026 + imprensa, consulta em 22/10/2026)
# Tudo que não vem da página oficial está atribuído na fala ("segundo ...").
# Marcações: {cue} animação · *texto* destaque · [p=0.4] pausa

TITULO = "Claude Duet: o agente da Anthropic que trabalha ANTES de você pedir"

VOZ = dict(
    tags=["alegre", "confiante"],
    prompt=("Narre como um apresentador de canal de tecnologia que acabou de ler o anúncio de um produto novo: voz "
            "masculina adulta, grave, segura e entusiasmada, mas precisa e sem exagero de propaganda. Curiosidade "
            "genuína no começo, clareza didática nas explicações e um tom mais sério e cuidadoso na parte de limites e "
            "segurança. Dê ênfase às palavras-chave e aos números. Ritmo natural, sem pressa, respeitando as pausas "
            "entre as frases. Leia apenas o texto, exatamente como está escrito, sem acrescentar, pular nem repetir nada."),
)

PRONUNCIA = {}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="gancho", text=
        "{a}Quantos aplicativos você abre [p=0.2] antes de começar a trabalhar de verdade? [p=0.5] "
        "{b}E-mail, [p=0.2] agenda, [p=0.2] mensagens, [p=0.2] planilha, [p=0.2] fatura atrasada... [p=0.5] "
        "{c}Agora imagine o contrário: [p=0.3] uma IA que olha *tudo isso* por você [p=0.2] e só te chama [p=0.2] "
        "quando alguma coisa *precisa* de você. [p=0.6] "
        "{d}Foi isso que a Anthropic anunciou *ontem,* [p=0.2] vinte e um de outubro: [p=0.3] o *Claude Duet.*"),

    # ================= O QUE É =================
    dict(id="02", block="oque", text=
        "{t}O Claude Duet é um *aplicativo novo,* [p=0.2] separado do app principal do Claude, [p=0.2] onde o Claude "
        "trabalha como um *agente proativo.* [p=0.5] Nas palavras da Anthropic, [p=0.2] {a}ele vem até você com o que "
        "precisa da sua *atenção,* [p=0.3] {b}completa as *tarefas* que você pede, [p=0.3] {c}continua trabalhando "
        "*quando você se afasta,* [p=0.3] {d}e *pergunta antes* de agir em seu nome. [p=0.6] "
        "{e}O foco é *trabalho:* [p=0.2] profissionais [p=0.2] e donos de pequenas empresas. [p=0.4] "
        "{f}E por baixo está o modelo *Claude Opus cinco ponto cinco.*"),

    # ================= COMO FUNCIONA =================
    dict(id="03", block="fluxo", text=
        "{t}Como funciona? [p=0.4] {a}Você conecta os seus *aplicativos.* [p=0.3] O Duet *herda* da sua conta do Claude "
        "[p=0.2] a memória, [p=0.2] as skills [p=0.2] e os apps que você já conectou. [p=0.5] "
        "{b}Ele lê, [p=0.2] organiza [p=0.2] {c}e te manda um *resumo* ou um *alerta.* [p=0.4] "
        "{d}Se for preciso agir, [p=0.2] ele mostra *exatamente* o que vai fazer [p=0.2] e espera a sua *aprovação.* "
        "[p=0.4] {e}Só então vem a *ação.* [p=0.5] "
        "{f}E tudo acontece numa *conversa só,* [p=0.2] por texto ou por voz."),
    dict(id="04", block="ciclo", text=
        "{a}Todo dia de manhã, [p=0.2] ele manda um *brief curto* [p=0.2] com o que mais importa nos seus apps. [p=0.6] "
        "{b}Durante o dia, [p=0.2] o Duet confere as suas contas *a cada poucas horas.* [p=0.4] "
        "{c}Não é o tempo todo, [p=0.2] e a Anthropic explica o motivo: [p=0.2] checar sem parar "
        "*gastaria o limite* do seu plano muito mais rápido. [p=0.5] "
        "{d}Você também pode dizer [p=0.2] *sobre o que* quer ser avisado [p=0.2] e com que *frequência.*"),
    dict(id="05", block="nuvem", text=
        "{a}E aqui está a parte mais interessante: [p=0.3] o Duet tem uma *máquina virtual* na nuvem, [p=0.2] "
        "com um *navegador próprio.* [p=0.5] {b}Ou seja: [p=0.2] o seu notebook [p=0.2] e o seu celular "
        "*podem ficar desligados.* [p=0.5] {c}Você descreve a tarefa numa mensagem curta, [p=0.2] ele decide quais apps "
        "usar e quais passos seguir, [p=0.3] {d}e te *notifica* quando termina [p=0.2] ou quando precisa da sua revisão."),

    # ================= O QUE FAZ =================
    dict(id="06", block="tarefas", text=
        "{t}E que tipo de tarefa? [p=0.4] {a}Desde coisas simples, [p=0.2] como *marcar reuniões,* [p=0.4] "
        "{b}até trabalhos maiores: [p=0.2] *dashboards* com dezenas de ferramentas, [p=0.3] {c}*previsões* financeiras "
        "e de vendas, [p=0.3] {d}*protótipos* [p=0.3] {e}e até *aplicações web.* [p=0.6] "
        "{f}Para isso, ele usa os mais de *seis mil conectores e plugins* do Claude Marketplace."),
    dict(id="07", block="conectores", text=
        "{t}A própria Anthropic dá exemplos. [p=0.4] {a}Achar as mensagens do *Gmail* e do *Slack* que você deixou passar "
        "[p=0.2] e ajudar a responder. [p=0.4] {b}Procurar *faturas em aberto* no QuickBooks ou no Stripe [p=0.2] "
        "e redigir os lembretes. [p=0.4] {c}Preparar a *folha de pagamento* no Gusto. [p=0.4] "
        "{d}Escrever uma *vaga* e, depois que você edita e aprova, [p=0.2] publicar no LinkedIn. [p=0.4] "
        "{e}E até *comprar* coisas para o seu negócio, [p=0.2] com um *cartão virtual,* [p=0.2] para o número do "
        "seu cartão de verdade não ser compartilhado."),

    # ================= EXEMPLOS =================
    dict(id="08", block="casos", text=
        "{t}E como isso fica na prática? [p=0.4] A Anthropic contou casos de quem já testou. [p=0.5] "
        "{a}Uma corretora de imóveis recebeu um alerta [p=0.2] sem ter pedido nada: [p=0.2] uma *visita* estava marcada "
        "na agenda [p=0.2] *no dia errado.* [p=0.6] "
        "{b}O dono de uma rede de restaurantes, [p=0.2] com cerca de *cento e dez funcionários,* [p=0.2] usou o Duet "
        "para revisar *faturas* loja por loja. [p=0.3] Ele resumiu assim: [p=0.2] *não preciso abrir cem abas.* [p=0.6] "
        "{c}E uma estrategista de marca tinha uma call com um possível cliente. [p=0.2] O Duet preparou um resumo [p=0.2] "
        "{d}e percebeu que a call era logo *antes do voo* dela. [p=0.2] Então ofereceu *remarcar.*"),

    # ================= COMO USAR =================
    dict(id="09", block="acesso", text=
        "{t}E como usar? [p=0.4] {a}Por enquanto, [p=0.2] é uma *prévia de pesquisa,* [p=0.2] com *lista de espera.* "
        "[p=0.5] {b}Começou pelos assinantes dos planos *Pro* e *Max,* [p=0.3] {c}e só nos *Estados Unidos.* [p=0.5] "
        "{d}O app existe para *iOS,* [p=0.2] *Android* [p=0.2] e na web, [p=0.2] em claude ponto ai. [p=0.5] "
        "{e}Não tem preço separado: [p=0.2] durante a prévia, [p=0.2] ele está *incluído* no plano, [p=0.2] mas usa os "
        "*mesmos limites* do resto do Claude. [p=0.3] {f}E as checagens em segundo plano [p=0.2] também *contam* nesse limite."),

    # ================= CUIDADOS E LIMITES =================
    dict(id="10", block="aprovacao", text=
        "{t}Agora, [p=0.2] a parte que mais importa num agente assim: [p=0.2] *segurança.* [p=0.6] "
        "{a}Antes de *enviar uma mensagem,* [p=0.2] {b}fazer um *pagamento,* [p=0.2] {c}*assinar* um documento [p=0.2] "
        "{d}ou *apagar* qualquer coisa, [p=0.3] o Duet mostra o que vai fazer [p=0.2] e espera você *aprovar.* [p=0.6] "
        "{e}E algumas coisas são *proibidas* mesmo com a sua aprovação: [p=0.3] {f}*negociar valores mobiliários* "
        "[p=0.2] {g}e *transferir dinheiro* entre contas."),
    dict(id="11", block="sensivel", text=
        "{a}Segundo a Anthropic, [p=0.2] o Duet *nunca vê* diretamente as suas senhas [p=0.2] nem os tokens de login. "
        "[p=0.5] {b}Um *classificador* novo confere cada mensagem [p=0.2] e bloqueia o envio de dados como "
        "*número de cartão de crédito* [p=0.2] e *documento de identidade.* [p=0.5] "
        "{c}Saúde e finanças pessoais [p=0.2] só saem quando você *mandar explicitamente.* [p=0.4] "
        "{d}E você pode *desconectar* qualquer app quando quiser."),
    dict(id="12", block="limites", text=
        "{t}E a própria empresa admite os *limites.* [p=0.4] {a}Ele ainda pode *entender mal* uma conversa [p=0.2] "
        "ou errar o que é *urgente.* [p=0.4] {b}Tarefas pessoais, [p=0.2] como comprar ingressos, [p=0.2] ainda são "
        "*mais fracas.* [p=0.4] {c}Ele ainda *não mostra* o navegador trabalhando. [p=0.4] "
        "{d}E, segundo o desenvolvedor Flavio Copes, [p=0.2] citando a central de ajuda, [p=0.2] o *Microsoft "
        "trezentos e sessenta e cinco* ainda não funciona no Duet."),
    dict(id="13", block="rivais", text=
        "{a}E o Duet não chega sozinho. [p=0.3] Segundo a CNBC, [p=0.2] ele vai disputar espaço com o *Muse,* da Meta, "
        "[p=0.2] {b}e com o *Dots,* da OpenAI. [p=0.5] {c}A Meta mira mais o *consumidor;* [p=0.2] o produto da OpenAI "
        "fica entre empresas e consumidores. [p=0.4] {d}Já a aposta da Anthropic é clara: [p=0.2] *trabalho.*"),

    # ================= RESUMO =================
    dict(id="14", block="resumo", text=
        "{t}Resumindo. [p=0.4] {a}O Claude Duet é um agente *proativo,* [p=0.2] num app próprio. [p=0.4] "
        "{b}Manda um *brief* de manhã [p=0.2] e confere os seus apps a cada poucas horas. [p=0.4] "
        "{c}Trabalha na *nuvem,* [p=0.2] mesmo com tudo desligado. [p=0.4] "
        "{d}*Pede aprovação* antes de enviar, pagar, assinar ou apagar. [p=0.4] "
        "{e}E, por enquanto, [p=0.2] é *prévia* com lista de espera, [p=0.2] para Pro e Max nos Estados Unidos."),

    # ================= CTA + FONTES =================
    dict(id="15", block="cta", text=
        "Se esse vídeo te mostrou algo novo, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal "
        "[p=0.2] {bell}e ative o *sininho,* para não perder as próximas ferramentas. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] você deixaria uma IA cuidar da sua caixa de entrada? [p=0.5] "
        "{bye}*Até o próximo vídeo.* [p=1.0]"),
    dict(id="16", block="fontes", text=
        "{a}As *fontes* deste vídeo [p=0.2] estão na tela [p=0.2] e na descrição. [p=5.0]"),
]
