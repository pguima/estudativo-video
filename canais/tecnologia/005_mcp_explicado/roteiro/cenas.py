# Roteiro — Tecnologia 005: MCP explicado, o "USB-C" das aplicações de IA
# Base: original/fonte_mcp.md (modelcontextprotocol.io + docs do Claude Code, consultados em 15/10/2026)
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa

TITULO = "MCP explicado: o USB-C da inteligência artificial"

# só para a narração provisória (edge-tts); a legenda mantém o texto original
PRONUNCIA = {
    "MCP": "M C P",
    "USB-C": "U S B C",
    "JSON-RPC": "Jêison R P C",
    "HTTP": "H T T P",
    "OAuth": "Ó Auth",
    "VS Code": "V S Code",
    "IA": "I A",
    "IAs": "I As",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "Você tem três aplicativos de IA. [p=0.3] {a}E quer conectar cada um deles [p=0.2] a quatro ferramentas: "
        "[p=0.2] seus arquivos, [p=0.2] o banco de dados, [p=0.2] a agenda [p=0.2] e o GitHub. [p=0.5] "
        "{b}Sem um padrão, [p=0.2] são *doze integrações diferentes,* [p=0.2] cada uma do seu jeito. [p=0.5] "
        "{c}Com um padrão, [p=0.2] são só *sete* peças, [p=0.2] e todas falam a mesma língua."),
    dict(id="02", block="intro", text=
        "{a}Esse padrão é o *MCP,* [p=0.2] o *Model Context Protocol.* [p=0.5] "
        "{b}Um padrão *aberto* [p=0.2] para conectar aplicativos de IA [p=0.2] a sistemas externos. [p=0.4] "
        "{c}Ele foi criado e aberto pela Anthropic [p=0.2] em *novembro de dois mil e vinte e quatro.*"),
    dict(id="03", block="mapa", text=
        "{t}Neste vídeo: [p=0.2] {a}a ideia por trás do MCP, [p=0.2] {b}as três peças da arquitetura, [p=0.2] "
        "{c}o que um servidor oferece, [p=0.2] {d}como a conversa acontece por dentro, [p=0.2] "
        "{e}como usar na prática, [p=0.2] {f}e os cuidados de segurança."),

    # ================= A IDEIA =================
    dict(id="04", block="usbc", text=
        "{t}A própria documentação usa uma comparação. [p=0.3] {a}Pense no MCP [p=0.2] como uma *porta USB-C* "
        "[p=0.2] para aplicativos de IA. [p=0.5] {b}O USB-C padronizou como os aparelhos se conectam. [p=0.3] "
        "{c}O MCP padroniza [p=0.2] como a IA se conecta [p=0.2] a *dados,* [p=0.2] a *ferramentas* [p=0.2] e a *fluxos de trabalho.*"),
    dict(id="05", block="conta", text=
        "{t}E é por isso que a conta muda. [p=0.3] {a}Sem padrão, [p=0.2] cada aplicativo precisa de uma integração "
        "[p=0.2] para cada ferramenta: [p=0.2] *multiplica.* [p=0.5] {b}Com o MCP, [p=0.2] cada ferramenta vira *um servidor,* "
        "[p=0.2] e cada aplicativo aprende a falar MCP *uma vez só:* [p=0.2] *soma.* [p=0.5] "
        "{c}Construa uma vez, [p=0.2] *integre em todo lugar.*"),
    dict(id="06", block="exemplos", text=
        "{t}E o que isso permite? [p=0.3] A documentação dá exemplos. [p=0.4] {a}Um assistente que acessa a sua "
        "*agenda do Google* [p=0.2] e o seu *Notion.* [p=0.4] {b}O Claude Code criando um aplicativo web inteiro [p=0.2] "
        "a partir de um *design do Figma.* [p=0.4] {c}Um chat da empresa [p=0.2] ligado a *vários bancos de dados.* [p=0.4] "
        "{d}E até uma IA criando um modelo no *Blender* [p=0.2] e mandando para a *impressora 3D.*"),

    # ================= ARQUITETURA =================
    dict(id="07", block="pecas", text=
        "{t}Agora, a arquitetura. [p=0.3] São três peças. [p=0.4] {a}O *host* [p=0.2] é o aplicativo de IA: [p=0.2] "
        "o Claude Code, [p=0.2] o Claude Desktop, [p=0.2] o VS Code. [p=0.4] {b}O *servidor* [p=0.2] é o programa "
        "que oferece as ferramentas e os dados. [p=0.4] {c}E o *cliente* [p=0.2] é a ponte: [p=0.2] o host cria "
        "*um cliente para cada servidor,* [p=0.2] {d}cada um com a sua conexão dedicada."),
    dict(id="08", block="transporte", text=
        "{t}E o servidor pode estar em dois lugares. [p=0.3] {a}*Local,* [p=0.2] na sua máquina, [p=0.2] conversando "
        "direto com o aplicativo, [p=0.2] pelo transporte chamado *stdio.* [p=0.5] {b}Ou *remoto,* [p=0.2] na internet, "
        "[p=0.2] pelo transporte *HTTP,* [p=0.2] {c}com autenticação, [p=0.2] de preferência pelo *OAuth,* "
        "[p=0.2] aquele login que abre no navegador."),

    # ================= PRIMITIVOS =================
    dict(id="09", block="primitivos", text=
        "{t}E o que um servidor oferece? [p=0.3] Três coisas, [p=0.2] que o MCP chama de *primitivos.* [p=0.4] "
        "{a}*Tools,* [p=0.2] ferramentas: [p=0.2] funções que a IA pode *executar,* [p=0.2] como consultar um banco "
        "ou chamar uma API. [p=0.4] {b}*Resources,* [p=0.2] recursos: [p=0.2] *dados* para dar contexto, [p=0.2] "
        "como o conteúdo de um arquivo. [p=0.4] {c}E *prompts:* [p=0.2] *modelos prontos* [p=0.2] para estruturar a conversa."),
    dict(id="10", block="banco", text=
        "{t}Um exemplo da documentação: [p=0.2] um servidor de *banco de dados.* [p=0.4] {a}Ele oferece *tools* "
        "para fazer consultas, [p=0.3] {b}um *resource* com o esquema das tabelas, [p=0.3] {c}e um *prompt* [p=0.2] "
        "com exemplos de como usar as ferramentas."),

    # ================= POR DENTRO =================
    dict(id="11", block="conversa", text=
        "{t}E como a conversa acontece por dentro? [p=0.3] {a}As mensagens seguem o formato *JSON-RPC.* [p=0.4] "
        "{b}Primeiro, o cliente pergunta: [p=0.2] *quais ferramentas você tem?* [p=0.2] É o *tools list.* [p=0.4] "
        "{c}O servidor responde com a lista, [p=0.2] o nome, a descrição [p=0.2] e os parâmetros de cada uma. [p=0.4] "
        "{d}Depois, o cliente *chama* uma delas: [p=0.2] {e}por exemplo, o clima em São Francisco. [p=0.3] "
        "{f}E recebe o resultado."),
    dict(id="12", block="fluxo", text=
        "{t}E onde entra a IA nisso? [p=0.3] {a}O aplicativo junta as ferramentas de *todos* os servidores [p=0.2] "
        "e mostra para o modelo. [p=0.4] {b}Quando o modelo decide usar uma, [p=0.2] {c}o aplicativo *encaminha* "
        "o pedido para o servidor certo, [p=0.3] {d}e devolve o resultado para o modelo [p=0.2] continuar a resposta."),
    dict(id="13", block="extras", text=
        "{t}E tem mais dois detalhes. [p=0.3] {a}O servidor pode *avisar* quando a lista de ferramentas muda, "
        "[p=0.2] sem o cliente precisar ficar perguntando. [p=0.4] {b}E o servidor também pode *pedir uma informação* "
        "ou uma *confirmação* ao usuário, [p=0.2] antes de agir."),

    # ================= NA PRÁTICA =================
    dict(id="14", block="suporte", text=
        "{t}E quem fala MCP? [p=0.3] {a1}O *Claude.* [p=0.2] {a2}O *ChatGPT.* [p=0.2] {a3}O *VS Code.* [p=0.2] "
        "{a4}O *Cursor.* [p=0.2] {b}E muitos outros. [p=0.4] {c}Por isso, [p=0.2] quem cria um servidor [p=0.2] "
        "alcança todos esses aplicativos de uma vez."),
    dict(id="15", block="pratica", text=
        "{t}Na prática, [p=0.2] no Claude Code, [p=0.2] {a}adicionar um servidor remoto é um comando. [p=0.3] "
        "{b}Por exemplo, o do *Notion.* [p=0.5] {c}Depois, o comando *barra MCP* [p=0.2] faz o login [p=0.2] "
        "e mostra o status de cada servidor. [p=0.4] {d}E você escolhe o alcance: [p=0.2] só você neste projeto, "
        "[p=0.2] {e}a equipe toda do projeto, [p=0.2] {f}ou você em todos os projetos."),
    dict(id="16", block="canal", text=
        "{t}E você já viu o MCP neste canal. [p=0.3] {a}O *REA,* [p=0.2] do primeiro vídeo, [p=0.2] é um *servidor MCP* "
        "de engenharia reversa. [p=0.4] {b}E o *Claude Code,* [p=0.2] do quarto vídeo, [p=0.2] é um *host.* [p=0.4] "
        "{c}Liga um no outro, [p=0.2] e o agente ganha um poder novo."),

    # ================= SEGURANÇA =================
    dict(id="17", block="seguranca", text=
        "{t}E agora, o cuidado mais importante. [p=0.4] {a}Um servidor MCP *age em seu nome.* [p=0.3] "
        "{b}Então, [p=0.2] *só conecte servidores em que você confia.* [p=0.5] {c}E atenção aos que buscam "
        "*conteúdo externo,* [p=0.2] como páginas da web: [p=0.3] {d}um texto malicioso pode tentar dar ordens à IA. [p=0.3] "
        "Isso se chama *injeção de prompt.* [p=0.5] {e}Por isso o Claude Code pede a sua *aprovação* [p=0.2] "
        "antes de usar os servidores de um projeto."),

    # ================= FECHAMENTO =================
    dict(id="18", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}o MCP é o *USB-C* da IA: [p=0.2] um padrão aberto para conectar aplicativos "
        "a dados e ferramentas. [p=0.4] {b}Host, [p=0.2] cliente [p=0.2] e servidor. [p=0.4] "
        "{c}Tools, [p=0.2] resources [p=0.2] e prompts. [p=0.4] {d}Construa uma vez, [p=0.2] integre em todo lugar. "
        "[p=0.4] {e}E *só conecte o que você confia.*"),
    dict(id="19", block="cta", text=
        "Se esse vídeo te mostrou algo novo, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para não perder as próximas ferramentas. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual ferramenta [p=0.2] você conectaria primeiro [p=0.2] à sua IA? [p=0.5] "
        "{bye}*Até o próximo vídeo.* [p=1.5]"),
]
