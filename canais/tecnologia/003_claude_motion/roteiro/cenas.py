# Roteiro — Tecnologia 003: Claude Motion, animações feitas com código
# Base: original/fonte_claude_motion.md (anúncio de 08/10/2026 + central de ajuda, via coberturas)
# Marcações: {cue} animação · *texto* destaque · [p=1.5] pausa

TITULO = "Claude Motion: o Claude agora anima o seu conteúdo (sem gerar vídeo)"

# só para a narração provisória (edge-tts); a legenda mantém o texto original
PRONUNCIA = {
    "MP4": "M P quatro",
    "Descript": "Discript",
    "HeyGen": "Rei Guen",
    "Higgsfield": "Rigsfield",
    "invideo": "in vídeo",
    "Runway": "Ran uei",
    "Captions": "Képshans",
    "/motion": "barra motion",
    "HIPAA": "Ripa",
}

SCENES = [
    # ================= ABERTURA =================
    dict(id="01", block="hook", text=
        "Você precisa explicar o resultado do trimestre [p=0.2] em *trinta segundos.* [p=0.5] "
        "{a}Um slide parado [p=0.2] não prende ninguém. [p=0.4] {b}E um vídeo de verdade [p=0.2] pede programa de edição, "
        "[p=0.2] *horas de trabalho* [p=0.2] e alguém que saiba animar. [p=0.5] "
        "{c}E se você só *pedisse,* [p=0.2] e o Claude *animasse* o seu conteúdo?"),
    dict(id="02", block="intro", text=
        "{a}Esse é o *Claude Motion.* [p=0.4] {b}Ele foi lançado em *oito de outubro de dois mil e vinte e seis,* "
        "[p=0.2] em versão *beta,* [p=0.2] junto com o Claude Dashboards. [p=0.5] "
        "{c}Ele transforma o seu material em *animações curtas,* [p=0.2] {d}que você exporta em *MP4.*"),
    dict(id="03", block="mapa", text=
        "{t}Neste vídeo: [p=0.2] {a}o segredo de como ele funciona, [p=0.2] {b}o que dá para fazer, [p=0.2] "
        "{c}como criar a sua primeira animação, [p=0.2] {d}como editar e exportar, [p=0.2] "
        "{e}quem pode usar, [p=0.2] {f}e os limites."),

    # ================= O SEGREDO =================
    dict(id="04", block="segredo", text=
        "{t}Primeiro, o segredo. [p=0.3] {a}O Claude Motion *não usa um modelo de geração de vídeo.* [p=0.5] "
        "{b}Em vez disso, [p=0.2] o Claude *escreve código.* [p=0.4] {c}Um código que anima o *seu* texto, [p=0.2] "
        "os *seus* gráficos, [p=0.2] formas [p=0.2] e imagens. [p=0.4] {d}E o resultado roda [p=0.2] *como um vídeo curto.*"),
    dict(id="05", block="semfake", text=
        "{t}E isso tem uma consequência importante. [p=0.3] {a}Não existe *filmagem gerada.* [p=0.3] "
        "{b}Não existem *pessoas criadas por IA.* [p=0.5] {c}O que aparece na tela [p=0.2] é o *seu conteúdo,* [p=0.2] "
        "em movimento. [p=0.4] {d}Nada de cena inventada [p=0.2] no meio da apresentação da empresa."),
    dict(id="06", block="codigo", text=
        "{t}E tem uma vantagem prática. [p=0.3] {a}Como a animação é *código,* [p=0.2] o texto, os números, "
        "o tempo de cada cena [p=0.2] e a posição de cada elemento [p=0.2] *estão lá, escritos.* [p=0.5] "
        "{b}Quer trocar *um número?* [p=0.2] Troca só ele. [p=0.3] {c}O resto *fica igual.* [p=0.5] "
        "{d}Num vídeo gerado por IA, [p=0.2] uma mudança pequena [p=0.2] pode mudar *a cena inteira.*"),
    dict(id="07", block="meta", text=
        "{t}E uma curiosidade: [p=0.3] {a}os vídeos *deste canal* [p=0.2] são feitos exatamente assim. [p=0.4] "
        "{b}Cada gráfico, [p=0.2] cada painel [p=0.2] e cada legenda que você está vendo agora [p=0.2] "
        "*é código desenhando quadro a quadro.* [p=0.5] {c}O Motion coloca essa ideia [p=0.2] na mão de quem *não programa.*"),

    # ================= O QUE FAZ =================
    dict(id="08", block="exemplos", text=
        "{t}E o que dá para fazer? [p=0.3] A própria Anthropic dá três exemplos. [p=0.4] "
        "{a}Um explicador de *trinta segundos* [p=0.2] a partir do *relatório trimestral.* [p=0.4] "
        "{b}Animar um *gráfico* [p=0.2] do deck da reunião do conselho. [p=0.4] "
        "{c}E um *passo a passo* de boas-vindas [p=0.2] para novos clientes."),

    # ================= COMO USAR =================
    dict(id="09", block="comecar", text=
        "{t}Para criar a sua, [p=0.2] existem três caminhos. [p=0.3] {a}Pedir uma animação em *qualquer conversa,* "
        "[p=0.2] ou digitar *barra motion* na caixa de mensagem. [p=0.4] {b}Clicar em *Output* [p=0.2] e escolher *Motion.* "
        "[p=0.4] {c}Ou abrir um *modelo de Motion* na aba Artifacts, [p=0.2] onde as animações ficam salvas."),
    dict(id="10", block="prompt", text=
        "{t}E como pedir bem? [p=0.3] A dica oficial tem três partes. [p=0.4] {a}Diga *quem vai assistir.* [p=0.3] "
        "{b}Diga *onde vai passar.* [p=0.3] {c}E diga, mais ou menos, *quanto tempo* deve durar. [p=0.5] "
        "{d}E principalmente: [p=0.2] *anexe o material.* [p=0.2] O relatório, os dados, as imagens. [p=0.3] "
        "Assim, a animação usa o *seu* conteúdo, [p=0.2] e não um texto genérico."),
    dict(id="11", block="pedido", text=
        "{t}Por exemplo: [p=0.3] {a}crie uma animação de trinta segundos, [p=0.2] para a reunião geral da empresa, "
        "[p=0.2] {b}mostrando os três principais números do relatório em anexo. [p=0.5] "
        "{c}O Claude monta as cenas, [p=0.2] {d}escreve o código [p=0.2] {e}e mostra a animação *rodando.*"),
    dict(id="12", block="editar", text=
        "{t}Não gostou de alguma coisa? [p=0.3] {a}Peça no chat. [p=0.3] {b}*Deixe a segunda cena mais lenta.* [p=0.4] "
        "{c}*Troque esse número.* [p=0.5] {d}Ou, se preferir, [p=0.2] ajuste direto no *editor.*"),
    dict(id="13", block="exportar", text=
        "{t}Ficou pronta? [p=0.3] {a}Clique em *Export* [p=0.2] e escolha *MP4.* [p=0.5] "
        "{b}A animação começa *privada.* [p=0.3] {c}Para mostrar a alguém, [p=0.2] é só clicar em *Share.*"),
    dict(id="14", block="levar", text=
        "{t}E se precisar de um acabamento maior, [p=0.2] {a}dá para continuar a edição em outras ferramentas: [p=0.2] "
        "{a1}Adobe, [p=0.2] {a2}Descript, [p=0.2] {a3}HeyGen, [p=0.2] {a4}Higgsfield, [p=0.2] {a5}invideo, [p=0.2] "
        "{a6}Luma AI [p=0.2] {a7}e Runway. [p=0.4] {b}Canva e Captions [p=0.2] aparecem como *em breve.*"),

    # ================= PLANOS E LIMITES =================
    dict(id="15", block="planos", text=
        "{t}Agora, quem pode usar. [p=0.3] {a}O Motion está em beta [p=0.2] só nos planos *Team* e *Enterprise.* [p=0.3] "
        "{b}Não está no Free, [p=0.2] no Pro [p=0.2] nem no Max. [p=0.5] {c}No Team, [p=0.2] ele já vem *ligado.* [p=0.3] "
        "{d}No Enterprise, [p=0.2] o administrador precisa ativar [p=0.2] nas configurações da organização, "
        "[p=0.2] na seção *Artifacts.*"),
    dict(id="16", block="uso", text=
        "{t}E ele não tem cobrança separada, [p=0.2] {a}mas conta no *limite de uso* do seu plano. [p=0.4] "
        "{b}Animações mais *longas* [p=0.2] ou mais *complexas* [p=0.2] *consomem mais.*"),
    dict(id="17", block="limites", text=
        "{t}E os limites. [p=0.4] {a}Primeiro: [p=0.2] é *beta.* [p=0.2] O desempenho pode variar. [p=0.4] "
        "{b}Segundo: [p=0.2] ele foi feito para *clipes curtos,* [p=0.2] não para um treinamento de uma hora. [p=0.4] "
        "{c}Terceiro, [p=0.2] e mais importante: [p=0.2] o Motion *explica* o conteúdo, [p=0.2] *mas não confere.* [p=0.3] "
        "{d}Se o número do relatório estiver errado, [p=0.2] ele vai animar o número errado, [p=0.2] *muito bem animado.* "
        "[p=0.4] {e}Revise tudo contra a fonte [p=0.2] antes de publicar."),

    # ================= FECHAMENTO =================
    dict(id="18", block="resumo", text=
        "{t}Resumindo: [p=0.3] {a}o Claude Motion transforma o seu material [p=0.2] em uma *animação curta.* [p=0.4] "
        "{b}Não é vídeo gerado por IA: [p=0.2] é *código* animando o seu conteúdo, [p=0.2] {c}e por isso cada detalhe "
        "*se edita sem refazer o resto.* [p=0.4] {d}Exporta em MP4, [p=0.2] {e}está em beta nos planos Team e Enterprise, "
        "[p=0.3] {f}e a regra de ouro continua valendo: [p=0.2] *confira os números.*"),
    dict(id="19", block="cta", text=
        "Se esse vídeo te mostrou algo novo, [p=0.2] {like}deixe o seu *like,* [p=0.2] {sub}*inscreva-se* no canal [p=0.2] "
        "{bell}e ative o *sininho,* para não perder as próximas ferramentas. [p=0.5] "
        "{com}E me conte nos *comentários:* [p=0.2] que conteúdo do seu trabalho [p=0.2] você transformaria em *animação?* [p=0.5] "
        "{bye}*Até o próximo vídeo.* [p=1.5]"),
]
