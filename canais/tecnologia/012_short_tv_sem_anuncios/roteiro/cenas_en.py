# Short — Tecnativo English 012: the dev who let Claude Code take the ads off his parents' TV (cleanyourtv)
# Short vertical nativo (render.py --vertical --lang en). Base: original/fonte.md. Nada além do que as fontes dizem.
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa · números por extenso (como falados)

TITULO = "He let an AI hack his parents' TV to kill the ads"

VOZ = dict(
    tags=["animada", "confiante"],
    prompt=("Narrate a viral YouTube Short about tech: adult male voice, deep, punchy and excited, like you're telling a "
            "friend something wild you just saw. Fast pace with high energy from the very first word, no slow intro. "
            "Hit the key words and numbers hard. Short, tight pauses only where marked. A playful, slightly "
            "challenging tone on the final question. Read only the text, exactly as written, without adding, skipping "
            "or repeating anything."),
)

PRONUNCIA = {}

# respiros curtos (Short): sem silêncio entre blocos, quase nada no começo
RITMO = dict(gap_bloco=0.0, pad_inicio=0.05, pad_fim=0.9)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}This TV showed an *ad* [p=0.1] before you could even open *Netflix.* [p=0.2] "
        "{b}So he let an *AI* take it over."),
    dict(id="02", block="post", text=
        "{a}Developer *Gathin* gave *Claude Code* [p=0.1] just one thing: [p=0.1] {b}the TV's *model number.*"),
    dict(id="03", block="hack", text=
        "{a}It found the TV on the *Wi-Fi,* [p=0.1] {b}plugged into Android's *debug bridge,* [p=0.1] "
        "{c}and switched off *twenty-five* Xiaomi apps: [p=0.1] {d}*ads,* tracking, sponsored rows."),
    dict(id="04", block="launcher", text=
        "{a}Then it wrote a brand new *home screen.* [p=0.2] {b}Before. [p=0.3] {c}*After.* [p=0.2] "
        "{d}It looks like an *Apple TV* now."),
    dict(id="05", block="viral", text=
        "{a}The post hit *seven point four million* views. [p=0.1] {b}The project: *twenty-seven thousand* GitHub stars "
        "[p=0.1] in *six days,* [p=0.1] {c}and *two hundred fifty-two* TV models."),
    dict(id="06", block="cuidado", text=
        "{a}Nothing gets deleted, [p=0.1] {b}it's all *disabled,* [p=0.1] and one command *undoes* it. [p=0.2] "
        "{c}Android and Google TV only, [p=0.1] {d}and yes, [p=0.1] at least one TV got *bricked.*"),
    dict(id="07", block="final", text=
        "{a}So, [p=0.1] would you let an AI into *your* TV? [p=0.2] {b}Or keep watching *this?*"),
]
