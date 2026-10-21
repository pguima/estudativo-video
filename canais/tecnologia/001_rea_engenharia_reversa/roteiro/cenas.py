# Roteiro — Tecnologia 001: REA, a engenharia reversa com agentes de IA
# Base: original/fonte_rea.md (github.com/morluto/rea · rea.tools)
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa

TITULO = "REA: engenharia reversa de qualquer programa com agentes de IA"

# só para a narração provisória (edge-tts); a legenda mantém o texto original
PRONUNCIA = {
    "REA": "Réa",
    "MCP": "M C P",
    "MIT": "M I T",
    "DLLs": "D L Ls",
    "npx": "N P X",
    "rea-agents": "réa agents",
    "rea.": "réa.",
    "Ghidra": "Guídra",
    "IDA": "Ida",
    "SQLite": "S Q Lite",
    "Node.js": "Node J S",
    ".NET": "dot net",
    "DX-Ball": "D X Ball",
    "CLI": "C L I",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "Você já viu um recurso num aplicativo e pensou: [p=0.2] *como isso funciona por dentro?* [p=0.5] "
        "{a}O problema é que você *não tem o código-fonte.* [p=0.3] {b}Só tem o programa *compilado.* [p=0.5] "
        "{c}E se um *agente de IA* pudesse abrir esse programa, [p=0.2] achar a lógica [p=0.2] e ainda *reconstruir* o recurso para você?"),
    dict(id="02", block="intro", text=
        "{a}Esse é o *REA,* [p=0.2] de *Reverse Engineer Anything:* [p=0.2] engenharia reversa de qualquer coisa. [p=0.5] "
        "{b}Um projeto de *código aberto,* com licença MIT, [p=0.2] {c}que passou da marca de *duzentas e cinquenta mil estrelas* no GitHub."),
    dict(id="03", block="mapa", text=
        "{t}Neste vídeo: [p=0.2] {a}o que é engenharia reversa, [p=0.2] {b}como o REA conversa com o seu agente, [p=0.2] "
        "{c}o que ele consegue analisar, [p=0.2] {d}três exemplos reais, [p=0.2] {e}como instalar, [p=0.2] {f}e os cuidados legais."),

    # ================= CONCEITO =================
    dict(id="04", block="compila", text=
        "{t}Primeiro, o conceito. [p=0.3] {a}Quando um programa é *compilado,* [p=0.2] o código que o desenvolvedor escreveu "
        "vira *instruções de máquina.* [p=0.4] {b}Os nomes somem. [p=0.2] Os comentários somem. [p=0.5] "
        "{c}*Engenharia reversa* é o caminho de volta: [p=0.2] partir do binário e *descobrir a lógica.*"),
    dict(id="05", block="ferramentas", text=
        "{t}Tradicionalmente, isso exige ferramentas pesadas, [p=0.2] {a}como o *Ghidra,* [p=0.2] {b}o *IDA* [p=0.2] {c}e o *Hopper,* "
        "[p=0.3] {d}e muitas horas lendo *assembly.* [p=0.5] {e}O REA *não substitui* essas ferramentas. [p=0.3] Ele é uma *ponte.*"),

    # ================= COMO FUNCIONA =================
    dict(id="06", block="mcp", text=
        "{t}O REA é um *servidor MCP.* [p=0.3] {a}MCP é o *Model Context Protocol,* [p=0.2] o padrão que permite que agentes de IA "
        "usem *ferramentas externas.* [p=0.5] {b}Assim, o *Claude Code,* [p=0.2] o *Codex,* [p=0.2] o *Cursor* [p=0.2] ou o *Gemini CLI* "
        "[p=0.2] {c}ganham as mãos que faltavam para *inspecionar um programa.*"),
    dict(id="07", block="fluxo", text=
        "{t}O fluxo tem três passos. [p=0.3] {s1}Um: [p=0.2] você *pergunta* sobre um recurso e aponta o programa. [p=0.4] "
        "{s2}Dois: [p=0.2] o agente chama o REA, [p=0.2] que *inspeciona* o alvo e rastreia o código relevante. [p=0.4] "
        "{s3}Três: [p=0.2] o REA devolve as descobertas *com as evidências,* [p=0.2] {s4}e o agente *explica* o comportamento, "
        "[p=0.2] ou escreve e *testa* uma implementação."),
    dict(id="08", block="evidencia", text=
        "{t}E aqui está o ponto mais importante do projeto. [p=0.3] {a}Cada conclusão vem com a *evidência* [p=0.2] e com as *limitações.* "
        "[p=0.5] {b}O REA separa o que ele *encontrou* no programa, [p=0.2] como código, instruções e chamadas, [p=0.2] "
        "{c}da *interpretação* que o agente faz. [p=0.5] {d}Você não precisa confiar no palpite da IA. [p=0.3] *Você vê a prova.*"),

    # ================= O QUE ANALISA =================
    dict(id="09", block="alvos", text=
        "{t}E o que dá para analisar? [p=0.3] Muita coisa. [p=0.3] {a1}Binários nativos, [p=0.2] executáveis e DLLs. [p=0.2] "
        "{a2}Programas em *Go* e *Rust.* [p=0.2] {a3}Aplicativos *JavaScript* e *Electron.* [p=0.2] {a4}Assemblies .NET. [p=0.2] "
        "{a5}Aplicativos *Android.* [p=0.2] {a6}Sites, pelo navegador. [p=0.4] {a7}E até *WebAssembly,* [p=0.2] contratos da *Ethereum,* "
        "[p=0.2] bancos SQLite, [p=0.2] *firmware* [p=0.2] e capturas de rede."),
    dict(id="10", block="local", text=
        "{t}E tudo roda *localmente,* na sua máquina. [p=0.4] {a}A análise estática de JavaScript e de .NET *só lê os arquivos,* "
        "[p=0.2] sem executar o aplicativo. [p=0.4] {b}Só a captura em *tempo de execução* roda o programa, [p=0.2] e com as *suas* permissões."),

    # ================= EXEMPLOS =================
    dict(id="11", block="calc", text=
        "{t}Agora, os exemplos. [p=0.3] O primeiro é a *calculadora do Windows.* [p=0.3] A pergunta: [p=0.2] como funciona o botão de "
        "*porcentagem?* [p=0.5] {a}O REA leu as instruções do binário e achou *duas regras.* [p=0.4] {b}Depois do *mais,* [p=0.2] "
        "a porcentagem é calculada sobre o primeiro número: [p=0.2] {b2}duzentos mais dez por cento dá *duzentos e vinte.* [p=0.5] "
        "{c}Mas depois do *vezes,* [p=0.2] dez por cento vira *zero vírgula um:* [p=0.2] {c2}duzentos vezes dez por cento dá *vinte.* "
        "[p=0.4] {d}A mesma tecla, [p=0.2] *dois comportamentos.*"),
    dict(id="12", block="dino", text=
        "{t}O segundo é o *jogo do dinossauro* do navegador. [p=0.3] Por que ele vai ficando mais rápido? [p=0.5] "
        "{a}A regra recuperada: [p=0.2] a velocidade começa em *seis,* [p=0.2] {b}soma *um milésimo* a cada atualização, [p=0.2] "
        "{c}e trava em *treze.* [p=0.5] {d}Com isso, o agente construiu um *minijogo,* [p=0.2] com um controle para ajustar a velocidade."),
    dict(id="13", block="dxball", text=
        "{t}O terceiro é o mais impressionante: [p=0.2] *DX-Ball,* [p=0.2] um jogo de Windows de *mil novecentos e noventa e seis.* [p=0.5] "
        "{a}O REA rastreou como a *posição da bola* define se o som sai na *esquerda* ou na *direita.* [p=0.5] "
        "{b}A função foi reconstruída em *C,* [p=0.2] {c}passou em *três mil, duzentos e cinco* casos comparados com o original, [p=0.3] "
        "{d}e reproduziu os *sessenta e três bytes* da função compilada."),

    # ================= COMO USAR =================
    dict(id="14", block="instalar", text=
        "{t}Quer testar? [p=0.3] {a}Você precisa do *Node.js,* versão vinte e dois ou mais nova, [p=0.2] e de um *agente de código.* "
        "[p=0.5] {b}No terminal, rode: [p=0.2] *npx rea-agents setup.* [p=0.5] {c}O instalador pergunta quais agentes configurar, "
        "[p=0.2] {d}mostra as mudanças *antes* de aplicar [p=0.2] {e}e faz *backup* da configuração. [p=0.3] {f}Depois, é só reiniciar o agente."),
    dict(id="15", block="prompt", text=
        "{t}E aí você pede em *linguagem natural.* [p=0.3] Por exemplo: [p=0.3] {a}entenda como funciona a busca do aplicativo de notas, "
        "[p=0.2] me mostre as evidências [p=0.2] e construa um recurso parecido. [p=0.5] "
        "{b}Também dá para usar direto pelo terminal, [p=0.2] com o comando *rea.*"),
    dict(id="16", block="licencas", text=
        "{t}Um detalhe: [p=0.2] {a}para a análise profunda de binários nativos, [p=0.2] o REA usa o *Ghidra,* que é gratuito, "
        "[p=0.2] {b}ou o *IDA* e o *Hopper,* que são comerciais. [p=0.4] {c}E o REA *não dá licença* de nenhum deles. [p=0.3] Você precisa ter a sua."),

    # ================= CUIDADOS =================
    dict(id="17", block="legal", text=
        "{t}E agora, o cuidado mais sério. [p=0.4] {a}O REA é feito para *pesquisa legal,* [p=0.2] *educação,* [p=0.2] *interoperabilidade,* "
        "[p=0.2] *preservação* de software [p=0.2] {b}e análise de programas que são *seus,* [p=0.2] ou que você tem *autorização* para examinar. "
        "[p=0.5] {c}Nada de copiar software protegido, [p=0.2] nem *burlar licença.* [p=0.4] "
        "{d}Engenharia reversa é uma ferramenta poderosa, [p=0.2] e *responsabilidade* vem junto."),

    # ================= FECHAMENTO =================
    dict(id="18", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}o REA é um servidor MCP de *código aberto* [p=0.2] que dá ao seu agente de IA o poder da *engenharia reversa.* "
        "[p=0.4] {b}Ele analisa de *binários nativos* a *sites,* [p=0.2] {c}roda *localmente,* [p=0.2] {d}e entrega cada conclusão *com evidência.* "
        "[p=0.4] {e}Serve para entender, aprender e reconstruir, [p=0.2] *sempre com autorização.*"),
    dict(id="19", block="cta", text=
        "Se esse vídeo te mostrou algo novo, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para não perder as próximas ferramentas. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual aplicativo você gostaria de abrir *por dentro?* [p=0.5] "
        "{bye}*Até o próximo vídeo.* [p=1.5]"),
]
