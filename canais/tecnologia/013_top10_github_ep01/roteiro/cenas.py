# Roteiro — Tecnologia 013: Top 10 projetos do GitHub · episódio 1 (outubro de 2026)
# Base: original/github_trending_monthly_2026-10-27.html + original/api/*.json (API do GitHub) + README de cada repositório,
# consulta em 27/10/2026. Registro da série: canais/tecnologia/TOP10_GITHUB.md (não repetir projetos).
# Narração: gerada pelo usuário no Gemini TTS (voz Neno) a partir de roteiro/roteiro.txt; o trecho que a voz improvisou
# (uma lista inventada entre o #8 e o #7) foi cortado em analise/editar_parte1.py.
# Marcações: {cue} animação · *texto* destaque · [p=0.4] pausa

TITULO = "Os 10 projetos que mais cresceram no GitHub em outubro de 2026"

PRONUNCIA = {}

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}*Cinquenta e três mil estrelas* em um mês. Foi isso que o projeto número um desta lista ganhou no GitHub. "
        "{b}E ele faz, *de graça* e *no seu computador,* uma coisa pela qual muita gente paga assinatura. "
        "{c}Mas antes de chegar nele, tem *nove projetos* que estão mudando o jeito de programar com IA."),
    dict(id="02", block="criterio", text=
        "{a}O critério é simples: são os dez repositórios que mais ganharam estrelas nos *últimos trinta dias,* "
        "segundo o *GitHub Trending,* {b}consultado em vinte e sete de outubro. "
        "{c}Esta é uma *série:* todo mês tem uma lista nova, {d}e projeto que já apareceu só volta se lançar uma "
        "*versão nova* de verdade. {e}Bora para a contagem."),
    dict(id="03", block="p03", text=
        "{a}Em décimo lugar, um veterano: o *Ghidra,* a ferramenta de engenharia reversa criada pela *NSA,* a agência "
        "de segurança dos Estados Unidos. {b}Ele desmonta e descompila programas já compilados, para você entender o "
        "que um executável faz por dentro, muito usado na análise de *malware.* {c}A versão *doze ponto dois* saiu no "
        "dia vinte e dois de outubro e agora exige o *Java vinte e cinco.* {d}Foram mais de *quinze mil* estrelas no "
        "mês. Licença Apache dois ponto zero."),
    dict(id="04", block="p04", text=
        "{a}Em nono, um curso inteiro de graça: *AI Engineering from Scratch.* {b}São *quinhentas e quarenta e duas* "
        "lições em *vinte* fases, da matemática básica até agentes de IA, com código em Python, TypeScript, Rust e "
        "Julia. {c}A ideia é você implementar as peças por dentro, testar e ver onde elas falham, em vez de só chamar "
        "uma API. {d}*Dezesseis mil e seiscentas* estrelas no mês. Licença MIT."),
    dict(id="05", block="p05", text=
        "{a}Em oitavo, o *Impeccable,* para quem cansou de site feito por IA com cara de site feito por IA: "
        "{b}degradê roxo, tudo em Inter, cartão dentro de cartão. {c}Ele ensina design ao seu agente com *vinte e "
        "quatro* comandos, como polish, audit e critique, e tem *sessenta e duas* regras que detectam esses vícios sem "
        "precisar de IA. {d}*Dezessete mil e quinhentas* estrelas no mês. Licença Apache."),
    dict(id="06", block="p06", text=
        "{a}Em sétimo, o *Agent Reach:* ele dá ao seu agente acesso a lugares onde a busca comum não chega, "
        "{b}como legendas do YouTube, posts do Reddit e do X, issues do GitHub, vagas do LinkedIn e plataformas "
        "chinesas como o Bilibili. {c}Um único comando, *agent-reach,* escolhe o canal certo. "
        "{e}*Cuidado:* o pacote com esse nome no PyPI *não é o oficial;* instale só pelo GitHub. "
        "{d}*Dezoito mil* estrelas no mês. Licença MIT."),
    dict(id="07", block="p07", text=
        "{a}Em sexto, o *HyperFrames,* da HeyGen: {b}você escreve *HTML* e CSS, e ele renderiza um *vídeo MP4.* "
        "{c}Foi feito para agentes: você instala as skills e pede, por exemplo, uma intro de dez segundos com título "
        "e música, e o agente monta tudo. {e}Vem com cerca de *quatrocentos e cinquenta* blocos prontos, como "
        "transições, legendas e gráficos. {d}Quase *vinte mil* estrelas no mês. Licença Apache."),
    dict(id="08", block="p08", text=
        "{a}Em quinto, o *Paperclip.* A frase do próprio projeto resume: {b}se o agente é um *funcionário,* o "
        "Paperclip é a *empresa.* {c}Você define um objetivo, monta um time de agentes, com CEO, engenheiros e "
        "designers, de qualquer fornecedor, {e}e acompanha tarefas, aprovações e *custos* num painel, inclusive com "
        "limite de orçamento. {d}*Vinte e um mil e oitocentas* estrelas no mês. Licença MIT."),
    dict(id="09", block="p09", text=
        "{a}Em quarto, o projeto com mais estrelas da lista no total: quase *duzentas e noventa mil.* {b}O *ECC* "
        "transforma o seu agente num time de engenharia organizado: planeja, testa, implementa, revisa e lembra do que "
        "deu certo. {c}São *setenta e um* agentes, *trezentas e onze* skills e um verificador de segurança, o "
        "AgentShield. {e}Funciona melhor no Claude Code, mas tem adaptações para Codex, Cursor e outros. "
        "{d}*Vinte e três mil* estrelas no mês. Licença MIT."),
    dict(id="10", block="p10", text=
        "{a}No pódio, em terceiro, uma skill da *Cloudflare* que transforma o seu agente num *auditor de segurança.* "
        "{b}Ela roda em *seis fases,* do mapeamento do código até o relatório, {c}e tem uma regra de ouro: o agente "
        "que confere uma falha *nunca é o mesmo* que a encontrou. Foi daqui que nasceu o sistema que a própria "
        "Cloudflare usa para caçar vulnerabilidades. {e}*Importante:* rode em ambiente isolado e só em código que você "
        "tem *autorização* para auditar. {d}*Vinte e seis mil* estrelas no mês. Licença MIT."),
    dict(id="11", block="p11", text=
        "{a}Em segundo, o *Ponytail,* que coloca no seu agente aquele programador sênior que olha cinquenta linhas e "
        "troca por uma. {b}No teste do próprio projeto, feito no Claude Code com o Opus cinco ponto cinco, ele gerou "
        "*cinquenta e três por cento* menos código e gastou *quarenta e cinco por cento* menos tokens. {c}O exemplo: "
        "um seletor de data. Sem ele, *trezentas e trinta e cinco* linhas; com ele, *dez,* usando o que o navegador já "
        "tem. E sem cortar testes nem segurança. {d}*Trinta e um mil e seiscentas* estrelas no mês. Licença MIT."),
    dict(id="12", block="p12", text=
        "{a}E o número um, com *cinquenta e três mil* estrelas em um mês: o *VoiceStudio,* uma alternativa aberta ao "
        "ElevenLabs que roda *no seu computador.* {b}Ele clona voz, cria vozes novas, dubla vídeos, transcreve e gera "
        "audiolivros em *seiscentos e quarenta e seis* idiomas. {c}Tem app para Windows, Mac, Linux e até celular, e "
        "usa a placa de vídeo quando tem. {d}A licença é AGPL, {e}e um aviso sério: clone a voz de alguém *só com "
        "permissão.*"),
    dict(id="13", block="resumo", text=
        "{a}Recapitulando: VoiceStudio, Ponytail, a skill de segurança da Cloudflare, ECC, Paperclip, HyperFrames, "
        "Agent Reach, Impeccable, AI Engineering from Scratch e Ghidra. {b}Repare que *sete dos dez* são feitos para "
        "turbinar *agentes de IA.* {c}É para lá que o GitHub está olhando."),
    dict(id="14", block="cta", text=
        "Se esse vídeo te mostrou algo novo, {like}deixe o seu *like,* {sub}*inscreva-se* no canal {bell}e ative o "
        "*sininho,* para não perder o próximo top dez. {com}E me conte nos *comentários:* qual desses você vai testar "
        "primeiro? {bye}*Até o próximo vídeo.* [p=1.5]"),
]
