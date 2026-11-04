# Short — Tecnativo English 019: the first touchscreen Mac (and Steve Jobs said it wouldn't work)
# Same ids, blocks and {cues} as cenas.py. Source: original/fonte_mac_tela_touch.md.

TITULO = "Steve Jobs said it wouldn't work: the first touchscreen Mac is here"

VOZ = dict(
    tags=["animada", "confiante"],
    prompt=("Narrate a viral tech Short in American English: adult male voice, deep, energetic and excited, like telling "
            "a friend about a plot twist that just happened. Fast pace and high energy from the very first word, no slow "
            "intro. Hit the keywords and the numbers hard. Short pauses, only where marked. Provocative tone on the "
            "final question. Read only the text, exactly as written, without adding, skipping or repeating anything."),
)

PRONUNCIA = {}

RITMO = dict(gap_bloco=0.0, pad_inicio=0.05, pad_fim=0.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}In twenty ten, [p=0.1] Steve Jobs said a *touchscreen* laptop [p=0.1] *doesn't work.* [p=0.2] "
        "{b}Sixteen years later, [p=0.1] Apple just launched the *first touchscreen Mac.*"),
    dict(id="02", block="jobs", text=
        "{a}His words: [p=0.1] touch surfaces don't want to be *vertical.* [p=0.2] {b}At first, [p=0.1] you start to "
        "fatigue. [p=0.1] {c}After a while, [p=0.1] *your arm wants to fall off.*"),
    dict(id="03", block="toque", text=
        "{a}Now here's the new MacBook Pro, [p=0.1] with an *OLED* screen [p=0.1] {b}and touch: [p=0.1] scroll with "
        "your finger, [p=0.1] *pinch* to zoom, [p=0.1] {c}and even *draw* right on the display."),
    dict(id="04", block="ilha", text=
        "{a}It also brings the *Dynamic Island,* [p=0.1] that pill from the iPhone, [p=0.1] now at the top of the Mac. "
        "[p=0.2] {b}The keyboard and trackpad *are still there.*"),
    dict(id="05", block="preco", text=
        "{a}Now, the price: [p=0.1] it starts at *two thousand eight hundred ninety-nine dollars.* [p=0.2] {b}That's "
        "*four hundred dollars* more [p=0.1] than the same Mac without touch."),
    dict(id="06", block="data", text=
        "{a}Pre-orders are open, [p=0.1] and it ships *November sixth.* [p=0.2] {b}And if you hate it, [p=0.1] you "
        "can *turn the touch off.*"),
    dict(id="07", block="final", text=
        "{a}So: [p=0.1] was Steve Jobs *wrong?* [p=0.2] {b}Or will you never touch [p=0.1] your laptop screen?"),
]
