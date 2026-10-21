# Roteiro — Tecnologia 004: Claude Code, o agente de programação da Anthropic
# Base: original/fonte_claude_code.md (documentação oficial em code.claude.com, consultada em 15/10/2026)
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa

TITULO = "Claude Code: o agente que programa dentro do seu projeto"

# só para a narração provisória (edge-tts); a legenda mantém o texto original
PRONUNCIA = {
    "CLAUDE.md": "Claude ponto M D",
    "MCP": "M C P",
    "Shift+Tab": "Shift Tab",
    "VS Code": "V S Code",
    "JetBrains": "Jet Brains",
    "Git": "Guit",
    "Jira": "Jira",
    "CI": "C I",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "Imagine digitar no terminal: [p=0.3] {a}*escreva os testes do módulo de login,* [p=0.2] *rode,* "
        "[p=0.2] *e corrija o que falhar.* [p=0.5] {b}E ele simplesmente [p=0.2] *faz.* [p=0.4] "
        "{c}Lê o código, [p=0.2] {d}escreve os testes, [p=0.2] {e}roda, [p=0.2] {f}vê o erro [p=0.2] e corrige. [p=0.3] "
        "Sozinho."),
    dict(id="02", block="intro", text=
        "{a}Esse é o *Claude Code,* [p=0.2] o agente de programação da Anthropic. [p=0.5] "
        "{b}Ele *lê o seu projeto,* [p=0.2] {c}*edita arquivos,* [p=0.2] {d}*roda comandos* [p=0.2] "
        "{e}e se conecta às suas ferramentas de desenvolvimento."),
    dict(id="03", block="mapa", text=
        "{t}Neste vídeo: [p=0.2] {a}o que muda em relação ao chat, [p=0.2] {b}onde ele roda, [p=0.2] "
        "{c}como instalar, [p=0.2] {d}o que pedir, [p=0.2] {e}como ele pede permissão, [p=0.2] "
        "{f}e como deixar ele com a cara do seu projeto."),

    # ================= O QUE É =================
    dict(id="04", block="chat", text=
        "{t}Primeiro, a diferença. [p=0.3] {a}No chat, [p=0.2] você copia o código, [p=0.2] cola, [p=0.2] "
        "pega a resposta [p=0.2] e cola de volta. [p=0.5] {b}Você é a ponte. [p=0.5] "
        "{c}No Claude Code, [p=0.2] ele trabalha *dentro do projeto.* [p=0.3] {d}Ele mesmo abre os arquivos que precisa. "
        "[p=0.3] Você não precisa colar contexto nenhum."),
    dict(id="05", block="loop", text=
        "{t}E ele trabalha em ciclo. [p=0.3] {s1}Você descreve o que quer. [p=0.3] {s2}Ele *planeja* o caminho. [p=0.3] "
        "{s3}*Escreve o código,* [p=0.2] em quantos arquivos forem precisos. [p=0.3] {s4}E *verifica* se funciona, "
        "[p=0.2] rodando os testes. [p=0.4] {s5}Deu erro? [p=0.2] Ele lê o erro [p=0.2] e *volta ao começo do ciclo.*"),
    dict(id="06", block="bastidor", text=
        "{t}E um bastidor: [p=0.3] {a}os vídeos *deste canal* [p=0.2] são montados com o Claude Code. [p=0.4] "
        "{b}O roteiro, [p=0.2] {c}o código de cada animação, [p=0.2] {d}e a renderização [p=0.2] que junta tudo [p=0.2] "
        "no vídeo que você está vendo agora."),

    # ================= ONDE RODA =================
    dict(id="07", block="onde", text=
        "{t}E onde ele roda? [p=0.3] {a1}No *terminal.* [p=0.2] {a2}No *VS Code* [p=0.2] e no Cursor. [p=0.2] "
        "{a3}Nas IDEs da *JetBrains.* [p=0.2] {a4}No *aplicativo* para computador. [p=0.2] {a5}No *navegador.* [p=0.2] "
        "{a6}E até no *celular.* [p=0.5] {b}Todos usam o *mesmo motor.* [p=0.3] Então as suas configurações "
        "[p=0.2] funcionam em qualquer um deles."),
    dict(id="08", block="instalar", text=
        "{t}Para instalar no terminal, [p=0.2] {a}no Mac, no Linux [p=0.2] ou no WSL, [p=0.2] é um comando só. [p=0.4] "
        "{b}No Windows, [p=0.2] tem a versão para o *PowerShell.* [p=0.5] {c}Depois, [p=0.2] é entrar na pasta do projeto "
        "[p=0.2] {d}e digitar *claude.* [p=0.4] {e}Na primeira vez, [p=0.2] ele pede o seu *login.*"),
    dict(id="09", block="planos", text=
        "{t}E precisa de conta? [p=0.3] Precisa. [p=0.3] {a}Funciona com os planos *Pro,* [p=0.2] *Max,* [p=0.2] "
        "*Team* [p=0.2] e *Enterprise* do Claude, [p=0.4] {b}ou com uma conta do *Console,* [p=0.2] pagando pelo uso da API."),

    # ================= O QUE PEDIR =================
    dict(id="10", block="perguntas", text=
        "{t}E o que pedir primeiro? [p=0.3] A própria documentação sugere começar *perguntando.* [p=0.4] "
        "{a}*O que esse projeto faz?* [p=0.3] {b}*Onde está o ponto de entrada?* [p=0.3] {c}*Explique a estrutura de pastas.* "
        "[p=0.5] {d}É o jeito mais rápido de entender um projeto [p=0.2] que você *nunca viu.*"),
    dict(id="11", block="tarefas", text=
        "{t}Depois, você passa tarefas. [p=0.3] {a}Cole uma *mensagem de erro,* [p=0.2] e ele rastreia a causa [p=0.2] "
        "e corrige. [p=0.4] {b}Peça uma *funcionalidade nova.* [p=0.3] {c}Peça *testes* para o código que não tem. "
        "[p=0.4] {d}E até o Git vira conversa: [p=0.2] *faça o commit das minhas mudanças, com uma mensagem descritiva.* "
        "[p=0.3] {e}Ele cria a branch [p=0.2] e abre o *pull request.*"),

    # ================= PERMISSÕES =================
    dict(id="12", block="permissao", text=
        "{t}Mas calma: [p=0.2] ele não sai mexendo em tudo. [p=0.4] {a}No modo *manual,* [p=0.2] ele *para e pergunta* "
        "[p=0.2] antes de editar um arquivo, [p=0.2] rodar um comando [p=0.2] ou acessar a rede. [p=0.5] "
        "{b}E com *Shift Tab,* [p=0.2] você troca de modo a qualquer momento."),
    dict(id="13", block="modos", text=
        "{t}Os modos mais úteis são três. [p=0.3] {a}O modo *plano:* [p=0.2] ele só lê [p=0.2] e te apresenta um plano, "
        "[p=0.2] sem mexer em nada até você aprovar. [p=0.4] {b}O modo que *aceita edições,* [p=0.2] para quando você "
        "está revisando junto. [p=0.4] {c}E o modo *automático,* [p=0.2] em que um *segundo modelo* revisa cada ação "
        "[p=0.2] no seu lugar. [p=0.5] {d}Já pular todas as permissões, [p=0.2] só dentro de um *ambiente isolado.*"),

    # ================= PERSONALIZAR =================
    dict(id="14", block="claudemd", text=
        "{t}E agora, o segredo para ele trabalhar do *seu* jeito: [p=0.2] {a}o arquivo *CLAUDE.md.* [p=0.4] "
        "{b}Ele fica na raiz do projeto, [p=0.2] e o Claude lê esse arquivo [p=0.2] no começo de *toda sessão.* [p=0.4] "
        "{c}Ali você escreve os padrões de código, [p=0.2] as decisões de arquitetura [p=0.2] e as bibliotecas preferidas. "
        "[p=0.4] {d}E ele ainda guarda uma *memória automática* [p=0.2] do que aprende trabalhando."),
    dict(id="15", block="extensoes", text=
        "{t}E dá para ir além. [p=0.3] {a}*Skills* são fluxos que você empacota [p=0.2] e reutiliza, [p=0.2] "
        "como um comando de revisar pull request. [p=0.4] {b}*Hooks* rodam comandos [p=0.2] antes ou depois das ações dele, "
        "[p=0.2] como formatar o código a cada edição. [p=0.4] {c}E o *MCP* conecta ferramentas externas: [p=0.2] "
        "{c1}Google Drive, [p=0.2] {c2}Jira, [p=0.2] {c3}Slack. [p=0.3] {d}O mesmo protocolo [p=0.2] do REA, "
        "[p=0.2] que você viu no primeiro vídeo do canal."),
    dict(id="16", block="avancado", text=
        "{t}E para quem quer automatizar: [p=0.3] {a}ele roda vários *agentes em paralelo,* [p=0.2] cada um numa parte "
        "da tarefa. [p=0.4] {b}Roda em *scripts* e na integração contínua, [p=0.2] recebendo, por exemplo, um log [p=0.2] "
        "para analisar. [p=0.4] {c}E roda *rotinas agendadas* na nuvem, [p=0.2] mesmo com o seu computador desligado."),

    # ================= DICAS E CUIDADOS =================
    dict(id="17", block="dicas", text=
        "{t}Três dicas oficiais para pedir bem. [p=0.3] {a}Seja *específico.* [p=0.2] Em vez de corrigir o bug, "
        "[p=0.2] {a2}*corrija o bug em que o usuário vê uma tela em branco depois de errar a senha.* [p=0.5] "
        "{b}Divida as tarefas grandes *em passos.* [p=0.4] {c}E deixe ele *explorar primeiro,* [p=0.2] antes de mexer no código."),
    dict(id="18", block="cuidados", text=
        "{t}E os cuidados. [p=0.4] {a}*Revise* o que ele muda, [p=0.2] como revisaria o código de um colega. [p=0.4] "
        "{b}Trabalhe com o *Git:* [p=0.2] com commits frequentes, [p=0.2] voltar atrás é fácil. [p=0.4] "
        "{c}Em código sensível, [p=0.2] prefira o modo *manual.* [p=0.4] {d}E lembre que o uso conta no *limite do seu plano.*"),

    # ================= FECHAMENTO =================
    dict(id="19", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}o Claude Code é um agente que trabalha *dentro do seu projeto.* [p=0.4] "
        "{b}Ele lê, [p=0.2] planeja, [p=0.2] edita [p=0.2] e *verifica.* [p=0.4] {c}Roda no terminal, [p=0.2] "
        "nas IDEs, [p=0.2] no aplicativo e no navegador. [p=0.4] {d}Pede permissão, [p=0.2] e você escolhe o modo. "
        "[p=0.4] {e}E com o *CLAUDE.md,* [p=0.2] ele aprende o *seu* jeito de programar."),
    dict(id="20", block="cta", text=
        "Se esse vídeo te mostrou algo novo, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para não perder as próximas ferramentas. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual tarefa chata [p=0.2] você entregaria primeiro [p=0.2] "
        "para o *Claude Code?* [p=0.5] {bye}*Até o próximo vídeo.* [p=1.5]"),
]
