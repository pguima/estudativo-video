# Roteiro — Tecnologia 007: Remotion (vídeos com React)
# Base: original/fonte_remotion.md (README, site e docs oficiais, consultados em 17/10/2026)
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa

TITULO = "Remotion: crie vídeos com código React (e com agentes de IA)"

# só para a narração provisória (edge-tts); a legenda mantém o texto original
PRONUNCIA = {
    "Remotion": "Rimôuchon",
    "React": "Riéct",
    "GitHub": "Guit Rub",
    "Lambda": "Lâmbda",
    "Studio": "Istúdio",
    "Node": "Nôud",
    "MP4": "M P 4",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "Imagine que você precisa de *mil vídeos.* [p=0.3] {a}Um para cada cliente, [p=0.2] com o nome dele, "
        "[p=0.2] e os números dele. [p=0.5] {b}No editor de vídeo, [p=0.2] isso são *semanas* de trabalho. [p=0.5] "
        "{c}Agora imagine que o vídeo é *código:* [p=0.3] {d}você troca um dado, [p=0.2] e sai um vídeo novo."),
    dict(id="02", block="intro", text=
        "{a}Essa é a ideia do *Remotion.* [p=0.3] {b}O lema dele é: [p=0.2] *faça vídeos programando, com React.* [p=0.5] "
        "{c}O projeto está no GitHub, [p=0.2] com mais de *sessenta e quatro mil estrelas,* [p=0.3] "
        "{d}mais de *trezentos contribuidores,* [p=0.3] {e}e mais de *cinco milhões de instalações* por mês."),
    dict(id="03", block="mapa", text=
        "{t}Neste vídeo: [p=0.2] {a}a ideia por trás, [p=0.2] {b}como se anima com código, [p=0.2] "
        "{c}como começar e renderizar, [p=0.2] {d}vídeos a partir de dados, [p=0.2] {e}o Remotion com agentes de IA, "
        "[p=0.2] {f}e a licença, [p=0.2] que tem um detalhe importante."),

    # ================= A IDEIA =================
    dict(id="04", block="ideia", text=
        "{t}A ideia é simples. [p=0.3] {a}Um vídeo [p=0.2] é uma sequência de *quadros.* [p=0.4] "
        "{b}O Remotion te entrega o *número do quadro* [p=0.2] e uma tela em branco. [p=0.4] "
        "{c}E você desenha essa tela [p=0.2] com *React,* [p=0.2] do mesmo jeito que monta uma página na web. [p=0.5] "
        "{d}Mudou o número do quadro, [p=0.2] o desenho muda. [p=0.3] E isso, [p=0.2] em sequência, [p=0.2] *é a animação.*"),
    dict(id="05", block="composicao", text=
        "{t}Todo vídeo começa com uma *composição.* [p=0.3] {a}Ela diz a *largura* [p=0.2] e a *altura,* [p=0.2] "
        "por exemplo, [p=0.2] mil novecentos e vinte por mil e oitenta. [p=0.4] {b}Quantos quadros por segundo: [p=0.2] *trinta.* "
        "[p=0.4] {c}E quantos quadros no total: [p=0.2] *cento e cinquenta.* [p=0.5] "
        "{d}Cento e cinquenta quadros, [p=0.2] a trinta por segundo, [p=0.2] dão *cinco segundos* de vídeo."),

    # ================= ANIMAR =================
    dict(id="06", block="animar", text=
        "{t}E como se anima? [p=0.3] {a}Dentro do componente, [p=0.2] você pega o quadro atual [p=0.2] com o "
        "*use current frame.* [p=0.4] {b}Depois, [p=0.2] o *interpolate* transforma esse número em outro: [p=0.3] "
        "{c}por exemplo, [p=0.2] do quadro zero ao trinta, [p=0.2] a opacidade vai de *zero a um.* [p=0.5] "
        "{d}Pronto: [p=0.2] o título *aparece suavemente* [p=0.2] no primeiro segundo."),
    dict(id="07", block="spring", text=
        "{t}E tem mais ferramentas. [p=0.3] {a}O *spring* cria um movimento de mola, [p=0.2] mais natural. [p=0.4] "
        "{b}A *Sequence* coloca cada cena [p=0.2] no seu lugar da linha do tempo. [p=0.4] "
        "{c}E existem componentes prontos para *texto,* [p=0.2] *imagem,* [p=0.2] *vídeo* [p=0.2] e *áudio.*"),

    # ================= COMEÇAR E RENDERIZAR =================
    dict(id="08", block="comecar", text=
        "{t}Para começar, [p=0.2] você precisa do *Node ponto js* instalado. [p=0.4] {a}Aí é um comando só: "
        "[p=0.2] *npx create video arroba latest.* [p=0.5] {b}Ele cria o projeto [p=0.2] a partir de um modelo. [p=0.4] "
        "{c}E o *Remotion Studio* abre no navegador, [p=0.2] {d}com a prévia do vídeo [p=0.2] e a linha do tempo."),
    dict(id="09", block="render", text=
        "{t}E para gerar o arquivo final? [p=0.3] {a}No Studio, [p=0.2] é um botão: [p=0.2] *Render.* [p=0.4] "
        "{b}No terminal, [p=0.2] *npx remotion render.* [p=0.5] {c}E em escala, [p=0.2] dá para renderizar num servidor, "
        "[p=0.2] {d}na *AWS Lambda,* [p=0.2] {e}ou no *GitHub Actions.* [p=0.5] "
        "{f}Além de vídeo, [p=0.2] ele exporta *áudio,* [p=0.2] *imagem,* [p=0.2] e até *GIF.*"),

    # ================= DADOS =================
    dict(id="10", block="dados", text=
        "{t}E aqui está o poder de verdade. [p=0.3] {a}Como o vídeo é código, [p=0.2] ele pode ler *dados.* [p=0.4] "
        "{b}Uma planilha, [p=0.2] uma API, [p=0.2] um banco de dados. [p=0.5] {c}Lembra dos mil clientes? [p=0.3] "
        "{d}É um modelo só, [p=0.2] e *mil renderizações,* [p=0.2] {e}cada uma com o nome [p=0.2] e os números de cada cliente. "
        "[p=0.5] {f}Relatórios em vídeo, [p=0.2] retrospectivas do ano, [p=0.2] legendas automáticas: [p=0.2] tudo isso sai assim."),

    # ================= IA =================
    dict(id="11", block="ia", text=
        "{t}E agora, [p=0.2] a parte que está bombando: [p=0.2] *agentes de IA.* [p=0.4] {a}O Remotion mantém um pacote "
        "de *Agent Skills,* [p=0.2] com as boas práticas para trabalhar em projetos Remotion. [p=0.4] "
        "{b}Você instala com *npx skills add remotion dev barra skills.* [p=0.5] "
        "{c}E elas servem para o *Claude Code,* [p=0.2] o *Codex,* [p=0.2] o *Cursor* [p=0.2] e outros."),
    dict(id="12", block="fluxoia", text=
        "{t}O fluxo fica assim: [p=0.3] {a}você *descreve* o vídeo [p=0.2] em português. [p=0.4] "
        "{b}O agente *escreve o código* React. [p=0.4] {c}Você confere no *Studio,* [p=0.2] pede ajustes, [p=0.4] "
        "{d}e no fim, [p=0.2] *renderiza o MP4.* [p=0.5] {e}A dica dos próprios guias: [p=0.2] vá *uma cena por vez,* "
        "[p=0.2] em vez de pedir o vídeo inteiro de uma vez."),

    # ================= LICENÇA =================
    dict(id="13", block="licenca", text=
        "{t}E agora, [p=0.2] o detalhe importante: [p=0.2] a *licença.* [p=0.4] {a}O código está aberto no GitHub, "
        "[p=0.2] mas o Remotion *não é open source tradicional.* [p=0.5] {b}Ele é *gratuito* para pessoas, [p=0.2] "
        "organizações sem fins lucrativos, [p=0.2] e empresas de *até três pessoas,* [p=0.2] {c}inclusive com *uso comercial.* "
        "[p=0.5] {d}A partir de *quatro pessoas,* [p=0.2] a empresa precisa de uma *licença paga.*"),
    dict(id="14", block="precos", text=
        "{t}E quanto custa? [p=0.3] {a}No site, [p=0.2] o plano para criadores sai a *vinte e cinco dólares* por mês, "
        "[p=0.2] por pessoa. [p=0.4] {b}Para automação, [p=0.2] *um centavo de dólar* por renderização, [p=0.2] "
        "com mínimo de cem dólares por mês. [p=0.5] {c}E uma regra que vale para todos: [p=0.2] você *não pode revender* "
        "o código do Remotion [p=0.2] como se fosse um produto seu."),

    # ================= CUIDADOS =================
    dict(id="15", block="cuidados", text=
        "{t}Antes de começar, [p=0.2] três cuidados. [p=0.3] {a}Você precisa de uma noção de *JavaScript e React,* "
        "[p=0.2] ou de um agente fazendo isso com você. [p=0.4] {b}Revise o código que a IA escreve, [p=0.2] "
        "*antes de renderizar em lote.* [p=0.4] {c}E se for usar numa empresa, [p=0.2] *confira a licença* primeiro."),

    # ================= FECHAMENTO =================
    dict(id="16", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}no *Remotion,* [p=0.2] o vídeo é um componente *React.* [p=0.4] "
        "{b}Cada quadro é um número, [p=0.2] e a animação é *código.* [p=0.4] {c}Com dados, [p=0.2] um modelo vira "
        "*mil vídeos.* [p=0.4] {d}Com agentes de IA, [p=0.2] você descreve [p=0.2] e eles programam. [p=0.4] "
        "{e}E é grátis para pessoas e equipes de até três."),
    dict(id="17", block="cta", text=
        "Se esse vídeo te mostrou algo novo, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para não perder as próximas ferramentas. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] que vídeo você criaria [p=0.2] *com código?* [p=0.5] "
        "{bye}*Até o próximo vídeo.* [p=1.5]"),
]
