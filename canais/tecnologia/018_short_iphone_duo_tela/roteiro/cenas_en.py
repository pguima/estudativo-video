# Short — Tecnativo English 018: the foldable iPhone (iPhone Duo) screen is cracking
# Same ids, blocks and {cues} as cenas.py. Source: original/fonte_iphone_duo_tela.md (CNBC Oct 26, iFixit Oct 25, Fortune Oct 27, 2026).

TITULO = "The foldable iPhone's screen is cracking (and the fix costs half the phone)"

VOZ = dict(
    tags=["animada", "confiante"],
    prompt=("Narrate a viral tech Short in American English: adult male voice, deep, energetic and excited, like telling "
            "a friend about a controversy that just blew up. Fast pace and high energy from the very first word, no slow "
            "intro. Hit the keywords and the numbers hard. Short pauses, only where marked. Provocative tone on the "
            "final question. Read only the text, exactly as written, without adding, skipping or repeating anything."),
)

PRONUNCIA = {}

RITMO = dict(gap_bloco=0.0, pad_inicio=0.05, pad_fim=0.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}The first *foldable* iPhone costs almost *two thousand dollars.* [p=0.2] "
        "{b}And some owners are watching the screen *crack* [p=0.1] within hours."),
    dict(id="02", block="relatos", text=
        "{a}The iPhone Duo hit stores on Friday. [p=0.1] {b}Then came the reports: [p=0.1] you open the "
        "phone, [p=0.1] hear a *crunch,* [p=0.1] {c}and a *white line* shows up on the screen."),
    dict(id="03", block="apple", text=
        "{a}Apple confirmed the issue, [p=0.1] on a *small number* of units. [p=0.2] "
        "{b}If yours is affected, [p=0.1] you get a *replacement* under warranty."),
    dict(id="04", block="causa", text=
        "{a}The cause? [p=0.1] iFixit *tore it down.* [p=0.1] {b}The breaks show up near the *hinge,* "
        "[p=0.1] {c}where a support bar may be *pressing on the screen.* [p=0.1] But that's still a *theory.*"),
    dict(id="05", block="conta", text=
        "{a}Now, the painful part: [p=0.1] out of warranty, [p=0.1] a new inner screen costs "
        "*nine hundred ninety-nine dollars.* [p=0.2] {b}*Half* the price of the phone."),
    dict(id="06", block="areia", text=
        "{a}Nobody knows how many phones are affected, [p=0.1] and there are even *fake photos* out there. [p=0.2] "
        "{b}But iFixit's CEO warned: [p=0.1] a *grain of sand* [p=0.1] can kill this screen."),
    dict(id="07", block="final", text=
        "{a}So: [p=0.1] would you pay that [p=0.1] for a phone that folds? [p=0.2] {b}Or will you wait for the *second generation?*"),
]
