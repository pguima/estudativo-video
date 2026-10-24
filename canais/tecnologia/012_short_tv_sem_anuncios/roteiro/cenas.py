# Short — Tecnativo 012 (versão em português): o dev que tirou os anúncios da TV dos pais com o Claude Code
# Mesmos ids, blocks e {cues} do cenas_en.py (o Short nasceu em inglês; textos da tela em textos.py).
# Base: original/fonte.md. Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa · números por extenso

TITULO = "Ele deixou uma IA invadir a TV dos pais para acabar com os anúncios"

VOZ = dict(
    tags=["animada", "confiante"],
    prompt=("Narre um Short viral de tecnologia: voz masculina adulta, grave, enérgica e empolgada, como quem conta "
            "para um amigo uma coisa incrível que acabou de ver. Ritmo rápido e energia alta desde a primeira palavra, "
            "sem introdução lenta. Bata forte nas palavras-chave e nos números. Pausas curtas, só onde marcado. Tom "
            "provocador e divertido na pergunta final. Leia apenas o texto, exatamente como está escrito, sem "
            "acrescentar, pular ou repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(gap_bloco=0.0, pad_inicio=0.05, pad_fim=0.9)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Essa TV mostrava *propaganda* [p=0.1] antes de você conseguir abrir a *Netflix.* [p=0.2] "
        "{b}Então ele deixou uma *IA* invadir."),
    dict(id="02", block="post", text=
        "{a}O desenvolvedor *Gathin* deu ao *Claude Code* [p=0.1] uma coisa só: [p=0.1] {b}o *modelo* da TV."),
    dict(id="03", block="hack", text=
        "{a}A IA achou a TV no *Wi-Fi,* [p=0.1] {b}entrou pela *depuração* do Android, [p=0.1] "
        "{c}e desligou *vinte e cinco* apps da Xiaomi: [p=0.1] {d}*anúncios,* rastreamento e conteúdo patrocinado."),
    dict(id="04", block="launcher", text=
        "{a}Depois, escreveu uma *tela inicial* nova. [p=0.2] {b}Antes. [p=0.3] {c}*Depois.* [p=0.2] "
        "{d}Ficou com cara de *Apple TV.*"),
    dict(id="05", block="viral", text=
        "{a}O post passou de *sete vírgula quatro milhões* de visualizações. [p=0.1] {b}O projeto: *vinte e sete mil* "
        "estrelas no GitHub [p=0.1] em *seis dias,* [p=0.1] {c}e *duzentos e cinquenta e dois* modelos de TV."),
    dict(id="06", block="cuidado", text=
        "{a}Nada é apagado, [p=0.1] {b}só *desativado,* [p=0.1] e um comando *desfaz* tudo. [p=0.2] "
        "{c}Só funciona em Android TV e Google TV, [p=0.1] {d}e sim: [p=0.1] pelo menos uma TV *travou de vez.*"),
    dict(id="07", block="final", text=
        "{a}E aí, [p=0.1] você deixaria uma IA mexer na *sua* TV? [p=0.2] {b}Ou prefere continuar vendo *isso?*"),
]
