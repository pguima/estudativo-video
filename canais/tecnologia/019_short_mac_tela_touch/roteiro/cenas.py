# Short — Tecnativo 019: o primeiro Mac com tela touch (e o Steve Jobs dizia que não funcionava)
# Base: original/fonte_mac_tela_touch.md (Apple Newsroom 28/10, MacRumors 28/10, Tecnoblog/TechTudo 28–29/10/2026;
# Steve Jobs, "Back to the Mac", 20/10/2010). Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa · números por
# extenso (viram algarismos na legenda, ver NUMEROS no visual.py)

TITULO = "Steve Jobs dizia que não funcionava: chegou o primeiro Mac com tela touch"

VOZ = dict(
    tags=["animada", "confiante"],
    prompt=("Narre um Short viral de tecnologia: voz masculina adulta, grave, enérgica e empolgada, como quem conta para "
            "um amigo uma virada que acabou de acontecer. Ritmo rápido e energia alta desde a primeira palavra, sem "
            "introdução lenta. Bata forte nas palavras-chave e nos números. Pausas curtas, só onde marcado. Tom "
            "provocador na pergunta final. Leia apenas o texto, exatamente como está escrito, sem acrescentar, pular ou "
            "repetir nada."),
)

PRONUNCIA = {}

RITMO = dict(gap_bloco=0.0, pad_inicio=0.05, pad_fim=0.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Em dois mil e dez, [p=0.1] Steve Jobs disse que tela *touch* em notebook [p=0.1] *não funciona.* [p=0.2] "
        "{b}Dezesseis anos depois, [p=0.1] a Apple lançou o *primeiro Mac com tela touch.*"),
    dict(id="02", block="jobs", text=
        "{a}O argumento dele: [p=0.1] tela touch não foi feita para ficar *de pé.* [p=0.2] {b}No começo, [p=0.1] o "
        "braço cansa. [p=0.1] {c}Depois de um tempo, [p=0.1] *parece que vai cair.*"),
    dict(id="03", block="toque", text=
        "{a}Agora chegou o novo MacBook Pro, [p=0.1] com tela *OLED* [p=0.1] {b}e toque: [p=0.1] rolar com o dedo, "
        "[p=0.1] dar *zoom* com a pinça, [p=0.1] {c}e até *desenhar* direto na tela."),
    dict(id="04", block="ilha", text=
        "{a}E veio junto a *Dynamic Island,* [p=0.1] aquela ilha do iPhone, [p=0.1] agora no topo da tela do Mac. "
        "[p=0.2] {b}O teclado e o trackpad *continuam lá.*"),
    dict(id="05", block="preco", text=
        "{a}Agora, a conta: [p=0.1] nos Estados Unidos, [p=0.1] a partir de *dois mil oitocentos e noventa e nove "
        "dólares.* [p=0.2] {b}No Brasil, [p=0.1] a partir de *trinta e quatro mil novecentos e noventa e nove reais.*"),
    dict(id="06", block="data", text=
        "{a}A pré-venda já começou, [p=0.1] e as entregas nos Estados Unidos começam em *seis de novembro.* [p=0.2] "
        "{b}Aqui, [p=0.1] a Apple ainda *não deu data.*"),
    dict(id="07", block="final", text=
        "{a}E aí: [p=0.1] o Steve Jobs estava *errado?* [p=0.2] {b}Ou você nunca vai encostar o dedo [p=0.1] na tela "
        "do notebook?"),
]
