# Roteiro — Tecnologia 006: Claude Docs, Slides e Design
# Base: original/fonte_docs_slides_design.md (central de ajuda da Anthropic + cobertura do lançamento, 15/10/2026)
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa

TITULO = "Claude Docs, Slides e Design: documento, apresentação e visual na mesma conversa"

# só para a narração provisória (edge-tts); a legenda mantém o texto original
PRONUNCIA = {
    "Docs": "Dócs",
    "Slides": "Isláides",
    "Design": "Dizáin",
    "PowerPoint": "Pauer Póint",
    "Markdown": "Márkdaun",
    "GitHub": "Guit Rub",
    "HTML": "H T M L",
    "PDF": "P D F",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "Um relatório. [p=0.3] {a}Uma apresentação. [p=0.3] {b}E um visual para divulgar. [p=0.5] "
        "{c}Normalmente, [p=0.2] são *três programas,* [p=0.2] três arquivos, [p=0.2] e você copiando de um para o outro. "
        "[p=0.5] {d}E se tudo isso saísse [p=0.2] de *uma conversa só?*"),
    dict(id="02", block="intro", text=
        "{a}Esse é o trio *Claude Docs,* [p=0.2] *Claude Slides* [p=0.2] e *Claude Design.* [p=0.5] "
        "{b}Eles chegaram em beta [p=0.2] em *dezesseis de setembro de dois mil e vinte e seis,* [p=0.3] "
        "{c}e em *oito de outubro* saíram do beta, [p=0.2] *em todos os planos,* [p=0.2] inclusive o *gratuito.* [p=0.5] "
        "{d}Até ali, os usuários já tinham criado [p=0.2] *mais de quarenta e cinco milhões* [p=0.2] de documentos, "
        "apresentações e designs."),
    dict(id="03", block="mapa", text=
        "{t}Neste vídeo: [p=0.2] {a}o que é um artifact, [p=0.2] {b}o Docs, [p=0.2] {c}o Slides, [p=0.2] "
        "{d}o Design e os design systems, [p=0.2] {e}um exemplo completo, [p=0.2] {f}e o que muda para quem usava o site antigo."),

    # ================= ARTIFACTS =================
    dict(id="04", block="artifact", text=
        "{t}Primeiro, o conceito. [p=0.3] {a}Um *artifact* [p=0.2] é tudo o que o Claude cria [p=0.2] "
        "e que você colocaria na frente de alguém: [p=0.3] {b1}um documento, [p=0.2] {b2}uma apresentação, [p=0.2] "
        "{b3}um design, [p=0.2] {b4}um painel. [p=0.5] {c}Tudo fica salvo na aba *Artifacts,* [p=0.2] "
        "{d}e começa *privado,* [p=0.2] só para você."),
    dict(id="05", block="comecar", text=
        "{t}E para começar, [p=0.2] existem três caminhos. [p=0.3] {a}Pedir em *qualquer conversa.* [p=0.3] "
        "{b}Clicar em *Output* na caixa de mensagem [p=0.2] e escolher o modelo. [p=0.3] "
        "{c}Ou abrir o modelo direto na aba *Artifacts.*"),

    # ================= DOCS =================
    dict(id="06", block="docs", text=
        "{t}Agora, o *Claude Docs.* [p=0.3] {a}É um documento de texto, [p=0.2] *colaborativo.* [p=0.4] "
        "{b}O Claude escreve seções, [p=0.2] {c}faz perguntas [p=0.2] {d}e comenta as escolhas, [p=0.3] "
        "{e}enquanto os seus colegas editam o mesmo documento, [p=0.2] *ao mesmo tempo.*"),
    dict(id="07", block="editclaude", text=
        "{t}E tem um recurso muito prático: [p=0.2] {a}você *destaca um trecho,* [p=0.2] {b}clica em *editar com o Claude,* "
        "[p=0.2] {c}e escreve o que quer. [p=0.4] {d}Ele muda *exatamente ali,* [p=0.2] sem mexer no resto do texto."),
    dict(id="08", block="docsshare", text=
        "{t}Para compartilhar, [p=0.2] {a}você escolhe as pessoas [p=0.2] ou a organização inteira, [p=0.3] "
        "{b}e o link abre até no *celular.* [p=0.5] {c}E se precisar do arquivo, [p=0.2] ele exporta para "
        "{c1}*Word,* [p=0.2] {c2}*PDF,* [p=0.2] {c3}*Markdown* [p=0.2] {c4}e *Google Docs.*"),

    # ================= SLIDES =================
    dict(id="09", block="slides", text=
        "{t}Agora, o *Claude Slides.* [p=0.3] {a}Você pede a apresentação na conversa, [p=0.3] "
        "{b}edita *slide por slide,* [p=0.3] {c}e *apresenta direto do Claude,* [p=0.2] sem abrir outro programa."),
    dict(id="10", block="slidesexp", text=
        "{t}E quando precisar levar para fora, [p=0.2] {a}ele exporta em *PowerPoint,* [p=0.2] {b}em *PDF,* [p=0.2] "
        "{c}ou como um arquivo *editável* do *Google Slides.* [p=0.5] {d}E atenção: [p=0.2] ele é diferente do "
        "*Claude para PowerPoint,* [p=0.2] que é um complemento instalado dentro do próprio PowerPoint."),

    # ================= DESIGN =================
    dict(id="11", block="design", text=
        "{t}E o *Claude Design.* [p=0.3] {a}Ele cria peças visuais: [p=0.2] gráficos, [p=0.2] visuais de uma página, "
        "[p=0.2] protótipos. [p=0.4] {b}Você ajusta arrastando os elementos *no próprio canvas,* [p=0.3] "
        "{c}deixa *comentários,* [p=0.2] {d}ou simplesmente pede a mudança ao Claude."),
    dict(id="12", block="designsystem", text=
        "{t}E aqui está o ponto forte: [p=0.2] os *design systems.* [p=0.4] {a}Você ensina ao Claude a identidade da marca: "
        "[p=0.2] {a1}as *cores,* [p=0.2] {a2}as *fontes* [p=0.2] {a3}e os *componentes.* [p=0.5] "
        "{b}Dá para importar de um repositório do GitHub, [p=0.2] de arquivos de design, [p=0.2] ou do seu código. "
        "[p=0.5] {c}E a partir daí, [p=0.2] *todo trabalho novo* [p=0.2] já sai com a cara da sua marca."),
    dict(id="13", block="designexp", text=
        "{t}E o design também sai do Claude. [p=0.3] {a}Em *zip,* [p=0.2] *PDF,* [p=0.2] *PowerPoint,* [p=0.2] "
        "em uma página *HTML,* [p=0.2] {b}ou direto para outra ferramenta."),

    # ================= EXEMPLO =================
    dict(id="14", block="exemplo", text=
        "{t}E o melhor é quando os três trabalham juntos. [p=0.3] Um exemplo da própria Anthropic: [p=0.4] "
        "{a}você pede ao Claude para analisar o funil de vendas da semana, [p=0.3] {b}escrever o relatório no formato "
        "de sempre, [p=0.2] {c}apontar o que atrasou, [p=0.3] {d}e transformar os destaques em *cinco slides.* [p=0.5] "
        "{e}E ainda dá para *agendar* [p=0.2] para repetir toda segunda-feira."),

    # ================= ACESSO E MUDANÇAS =================
    dict(id="15", block="planos", text=
        "{t}E quem pode usar? [p=0.3] {a}*Todos os planos,* [p=0.2] já ligados. [p=0.4] {b}No *Enterprise,* "
        "[p=0.2] eles foram ligados por padrão em *quinze de outubro.* [p=0.5] {c}E no *celular,* [p=0.2] você cria, "
        "vê e edita, [p=0.3] {d}mas a configuração de compartilhamento [p=0.2] se muda no navegador ou no aplicativo do computador."),
    dict(id="16", block="siteantigo", text=
        "{t}E um aviso para quem usava o Claude Design separado, [p=0.2] em *claude ponto ai barra design.* [p=0.4] "
        "{a}Esse site fecha em *quatorze de dezembro de dois mil e vinte e seis.* [p=0.4] {b}Os design systems "
        "dá para *migrar.* [p=0.3] {c}Mas as conversas e os comentários do site antigo [p=0.2] *serão apagados.* "
        "[p=0.4] {d}Então, [p=0.2] *baixe os seus projetos em zip* [p=0.2] antes da data."),
    dict(id="17", block="cuidados", text=
        "{t}E um cuidado de sempre: [p=0.3] {a}o Claude escreve rápido, [p=0.2] mas quem *assina* é você. [p=0.4] "
        "{b}Revise os números e os fatos [p=0.2] antes de mandar para alguém. [p=0.4] "
        "{c}E pense bem antes de compartilhar *fora da empresa.*"),

    # ================= FECHAMENTO =================
    dict(id="18", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}o *Docs* escreve com você, [p=0.2] e com a equipe ao mesmo tempo. [p=0.4] "
        "{b}O *Slides* monta e apresenta. [p=0.4] {c}O *Design* cria os visuais, [p=0.2] com a cara da sua marca. "
        "[p=0.4] {d}Tudo começa numa conversa, [p=0.2] fica na aba Artifacts, [p=0.2] {e}e exporta para os formatos "
        "que você já usa."),
    dict(id="19", block="cta", text=
        "Se esse vídeo te mostrou algo novo, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para não perder as próximas ferramentas. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] qual dos três [p=0.2] você vai testar *primeiro?* [p=0.5] "
        "{bye}*Até o próximo vídeo.* [p=1.5]"),
]
