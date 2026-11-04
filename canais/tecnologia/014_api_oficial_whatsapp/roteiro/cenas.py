# Roteiro — Tecnologia 014: API oficial do WhatsApp (Meta): custo, configuração e integração com multiatendimento
# Base: original/fonte_api_whatsapp.md (documentação da Meta + tabela oficial em reais de 01/10/2026 + Chatwoot), consulta 29/10/2026.
# Valores da simulação = contas feitas com a tabela oficial (exemplo, não dado de mercado).
# Marcações: {cue} animação · *texto* destaque · [p=0.4] pausa

TITULO = "API oficial do WhatsApp: quanto custa, como configurar e como ligar num multiatendimento"

VOZ = dict(
    tags=["confiante", "amigavel"],
    prompt=("Narre como um apresentador de canal de tecnologia explicando, passo a passo, uma ferramenta para devs e donos "
            "de empresa: voz masculina adulta, grave, segura e entusiasmada, mas precisa e sem exagero de propaganda. "
            "Clareza didática nas explicações, calma nos números e nos preços, falando cada valor devagar, e tom mais "
            "sério na parte de cuidados. Dê ênfase às palavras-chave. Ritmo natural, sem pressa, respeitando as pausas "
            "entre as frases. Leia apenas o texto, exatamente como está escrito, sem acrescentar, pular nem repetir nada."),
)

PRONUNCIA = {}

SCENES = [
    # ================= GANCHO =================
    dict(id="01", block="gancho", text=
        "{a}Um celular, [p=0.2] um número de WhatsApp [p=0.2] e cinco pessoas tentando atender ao mesmo tempo. [p=0.5] "
        "{b}Ou pior: [p=0.2] uma ferramenta *não oficial* [p=0.2] que imita o WhatsApp Web [p=0.2] e pode parar a "
        "qualquer momento. [p=0.5] {c}Existe um caminho oficial: [p=0.2] a *API do WhatsApp,* da própria Meta. [p=0.5] "
        "{d}Neste vídeo: [p=0.2] *quanto custa,* [p=0.2] *como configurar* [p=0.2] e como ligar ela num sistema de "
        "*multiatendimento.*"),

    # ================= O QUE É =================
    dict(id="02", block="oque", text=
        "{t}Primeiro, o que é. [p=0.4] {a}A *Cloud API* faz parte da Plataforma WhatsApp Business. [p=0.3] Ela roda "
        "*nos servidores da Meta:* [p=0.2] você não instala nada. [p=0.5] {b}Para *enviar,* [p=0.2] o seu sistema faz uma "
        "chamada HTTP. [p=0.4] {c}Para *receber,* [p=0.2] a Meta avisa o seu servidor por um *webhook:* [p=0.2] mensagem "
        "nova, [p=0.2] entregue, [p=0.2] lida. [p=0.5] {d}E a Meta *não cobra mensalidade* pela Cloud API. [p=0.3] "
        "Você paga *por mensagem.*"),

    # ================= REGRAS: JANELA E MODELOS =================
    dict(id="03", block="janela", text=
        "{t}E para entender o preço, [p=0.2] você precisa de duas regras. [p=0.5] {a}Regra um: [p=0.2] quando o cliente "
        "manda uma mensagem, [p=0.2] abre uma *janela de vinte e quatro horas.* [p=0.4] Dentro dela, [p=0.2] você responde "
        "com *texto livre.* [p=0.5] {b}Regra dois: [p=0.2] fora da janela, [p=0.2] só com um *modelo aprovado* pela Meta, "
        "[p=0.2] o famoso template. [p=0.5] {c}E todo modelo tem uma *categoria:* [p=0.3] {d}*marketing,* [p=0.2] "
        "{e}*utilidade,* [p=0.2] como confirmação de pedido, [p=0.3] {f}e *autenticação,* [p=0.2] o código de login."),

    # ================= CUSTO =================
    dict(id="04", block="precos", text=
        "{t}Agora, os preços. [p=0.4] Estes são da *tabela oficial da Meta* em reais, [p=0.2] válida desde primeiro de "
        "outubro de dois mil e vinte e seis, [p=0.2] para números do Brasil. [p=0.5] {a}Mensagem de *marketing:* [p=0.2] "
        "trinta e dois centavos. [p=0.4] {b}*Utilidade:* [p=0.2] três centavos e meio. [p=0.4] {c}*Autenticação:* [p=0.2] "
        "também três centavos e meio. [p=0.5] {d}E o que o *cliente* manda para você [p=0.2] é *grátis.*"),
    dict(id="05", block="servico", text=
        "{a}E aqui tem uma mudança importante. [p=0.3] Desde primeiro de outubro, [p=0.2] as *respostas de atendimento* "
        "dentro da janela [p=0.2] *passaram a ser cobradas.* [p=0.5] {b}Cada número tem *mil mensagens de serviço "
        "grátis* por mês. [p=0.4] {c}Da mensagem mil e um em diante, [p=0.2] três centavos e meio cada. [p=0.5] "
        "{d}E a Meta já avisou: [p=0.2] sem forma de pagamento cadastrada, [p=0.2] essas mensagens podem *parar de ser "
        "entregues.*"),
    dict(id="06", block="simulacao", text=
        "{t}Vamos fazer uma conta de exemplo. [p=0.4] Uma loja, num mês. [p=0.5] {a}Duas mil mensagens de marketing: "
        "[p=0.2] *seiscentos e quarenta e três reais e quarenta centavos.* [p=0.5] {b}Cinco mil confirmações de pedido, "
        "[p=0.2] na categoria utilidade: [p=0.2] *cento e setenta e cinco reais.* [p=0.5] {c}Três mil respostas de "
        "atendimento: [p=0.2] mil são grátis, [p=0.2] e as outras duas mil saem por *setenta reais.* [p=0.5] "
        "{d}Total: [p=0.2] *oitocentos e oitenta e oito reais e quarenta centavos.* [p=0.4] {e}Repare: [p=0.2] quase "
        "tudo vem do *marketing.*"),
    dict(id="07", block="detalhes", text=
        "{t}Mais quatro detalhes de custo. [p=0.4] {a}Utilidade e autenticação ficam *mais baratas com volume,* [p=0.2] "
        "com desconto de cinco a vinte e cinco por cento; [p=0.2] marketing, não. [p=0.4] {b}Conversa que começa num "
        "anúncio de *clique para o WhatsApp* [p=0.2] tem as respostas grátis [p=0.2] por até sete dias. [p=0.4] "
        "{c}Desde julho, [p=0.2] dá para pagar *em reais.* [p=0.4] {d}E, se você usar uma plataforma ou um parceiro da "
        "Meta, [p=0.2] *a mensalidade deles é à parte.*"),

    # ================= CONFIGURAÇÃO =================
    dict(id="08", block="config1", text=
        "{t}Agora, a configuração. [p=0.4] {a}Passo um: [p=0.2] um *portfólio empresarial* da Meta, [p=0.2] o antigo "
        "Business Manager. [p=0.4] {b}Passo dois: [p=0.2] no *Meta for Developers,* [p=0.2] crie um app com o caso de uso "
        "*conectar-se com clientes pelo WhatsApp.* [p=0.5] {c}Passo três: [p=0.2] a Meta te dá um *número de teste* "
        "[p=0.2] e um token temporário, [p=0.2] para mandar a primeira mensagem na hora. [p=0.5] {d}Passo quatro: [p=0.2] "
        "o *número de verdade.* [p=0.3] Ele *não pode estar ativo* no aplicativo do WhatsApp: [p=0.2] precisa ser apagado "
        "de lá antes, [p=0.2] e ganha um *nome de exibição* [p=0.2] e um *PIN* de duas etapas."),
    dict(id="09", block="config2", text=
        "{a}Passo cinco: [p=0.2] o *token permanente.* [p=0.3] Nas configurações do negócio, [p=0.2] crie um *usuário do "
        "sistema,* [p=0.2] dê acesso ao app e à conta do WhatsApp, [p=0.2] e gere o token com as permissões *de "
        "mensagens* e *de gerenciamento.* [p=0.5] {b}Passo seis: [p=0.2] o *webhook.* [p=0.2] Uma URL com HTTPS, "
        "[p=0.2] um token de verificação que você inventa, [p=0.2] e a assinatura do campo *messages.* [p=0.5] "
        "{c}Passo sete: [p=0.2] *forma de pagamento.* [p=0.4] {d}E passo oito: [p=0.2] *verifique a empresa.* [p=0.3] "
        "{e}O limite começa em *duzentos e cinquenta* contatos por dia [p=0.2] fora da janela, [p=0.2] e sobe para "
        "*dois mil* depois da verificação."),
    dict(id="10", block="codigo", text=
        "{t}E como fica no código? [p=0.4] {a}Para enviar, [p=0.2] um *POST* no endereço da Graph API, [p=0.2] com o "
        "*ID do número* no caminho [p=0.2] e o token no cabeçalho. [p=0.5] {b}No corpo, [p=0.2] o produto, [p=0.2] o "
        "destinatário, [p=0.2] o tipo [p=0.2] e o texto. [p=0.5] {c}A resposta traz o *ID da mensagem.* [p=0.4] "
        "{d}E, quando o cliente responde, [p=0.2] a Meta faz o caminho inverso: [p=0.2] manda um *JSON* para o seu "
        "webhook, [p=0.2] com o número, [p=0.2] o nome [p=0.2] e o texto."),

    # ================= MULTIATENDIMENTO =================
    dict(id="11", block="arquitetura", text=
        "{t}E onde entra o multiatendimento? [p=0.4] {a}O cliente manda a mensagem. [p=0.3] {b}A Meta entrega no "
        "*webhook* do seu sistema. [p=0.4] {c}O sistema coloca a conversa numa *fila* [p=0.2] e *distribui* entre os "
        "atendentes, [p=0.2] por equipe, [p=0.2] etiqueta [p=0.2] ou rodízio. [p=0.5] {d}O atendente responde no "
        "painel, [p=0.2] {e}e o sistema faz o POST de volta para a API. [p=0.5] {f}Resultado: [p=0.2] *um número só,* "
        "[p=0.2] *vários atendentes,* [p=0.2] cada um no seu computador."),
    dict(id="12", block="chatwoot", text=
        "{t}Um exemplo prático: [p=0.2] o *Chatwoot,* [p=0.2] uma plataforma de atendimento de *código aberto.* "
        "[p=0.5] {a}Em configurações, [p=0.2] caixas de entrada, [p=0.2] você adiciona um canal *WhatsApp Cloud.* "
        "[p=0.4] {b}Ele pede três coisas: [p=0.2] o *ID do número,* [p=0.2] o *ID da conta do WhatsApp Business* "
        "[p=0.2] e o *token permanente.* [p=0.5] {c}Aí o próprio Chatwoot *confere o acesso* [p=0.2] e *configura o "
        "webhook* na Meta. [p=0.4] {d}Depois, é só adicionar os atendentes."),
    dict(id="13", block="operacao", text=
        "{t}Três dicas para o dia a dia. [p=0.4] {a}Primeira: [p=0.2] no painel, [p=0.2] a *janela de vinte e quatro "
        "horas* continua valendo. [p=0.3] Passou do prazo, [p=0.2] o atendente precisa mandar um *modelo.* [p=0.5] "
        "{b}Segunda: [p=0.2] o token precisa da permissão *de gerenciamento,* [p=0.2] senão os modelos não aparecem "
        "no painel. [p=0.5] {c}Terceira: [p=0.2] se você não quer largar o aplicativo *WhatsApp Business* no celular, "
        "[p=0.2] existe a *coexistência:* [p=0.2] o mesmo número no app e na API, [p=0.2] com até *seis meses* de "
        "histórico. [p=0.3] {d}Mas ela é ativada pelo fluxo de cadastro de um *parceiro,* [p=0.2] não pela "
        "configuração manual."),

    # ================= CUIDADOS =================
    dict(id="14", block="cuidados", text=
        "{t}E alguns cuidados. [p=0.4] {a}Para mandar mensagem primeiro, [p=0.2] você precisa do *consentimento* da "
        "pessoa. [p=0.4] {b}Modelo mal avaliado [p=0.2] *derruba a qualidade* do número [p=0.2] e trava o aumento do "
        "limite. [p=0.4] {c}O *token* é a chave da sua conta: [p=0.2] fica no servidor, [p=0.2] *nunca* no front-end. "
        "[p=0.4] {d}E valide a *assinatura* de cada webhook, [p=0.2] para ter certeza de que veio da Meta."),

    # ================= RESUMO =================
    dict(id="15", block="resumo", text=
        "{t}Resumindo. [p=0.4] {a}A Cloud API é *oficial,* [p=0.2] hospedada pela Meta [p=0.2] e sem mensalidade. "
        "[p=0.4] {b}Você paga *por mensagem:* [p=0.2] marketing trinta e dois centavos, [p=0.2] o resto três e meio. "
        "[p=0.4] {c}Mil respostas de atendimento grátis por mês, [p=0.2] por número. [p=0.4] {d}Configuração: [p=0.2] "
        "app, [p=0.2] número, [p=0.2] token permanente [p=0.2] e webhook. [p=0.4] {e}E o multiatendimento é um sistema "
        "*no meio,* [p=0.2] com um número e vários atendentes."),

    # ================= CTA + FONTES =================
    dict(id="16", block="cta", text=
        "Se esse vídeo te mostrou algo novo, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal "
        "[p=0.2] {bell}e ative o *sininho,* para não perder as próximas ferramentas. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual sistema de atendimento você usa com o WhatsApp? [p=0.5] "
        "{bye}*Até o próximo vídeo.* [p=1.0]"),
    dict(id="17", block="fontes", text=
        "{a}As *fontes* deste vídeo [p=0.2] estão na tela [p=0.2] e na descrição. [p=5.0]"),
]
