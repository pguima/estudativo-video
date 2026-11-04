# Short — Tecnativo English 017: Reddit is going logged-in only (and Google's AI is to blame)
# Same ids, blocks and {cues} as cenas.py. Source: original/fonte_reddit_login.md (CNBC + 9to5Google, Oct 29, 2026).

TITULO = "Reddit will make you log in to read (and Google's AI is to blame)"

VOZ = dict(
    tags=["animada", "confiante"],
    prompt=("Narrate a viral tech Short in American English: adult male voice, deep, energetic and excited, like telling "
            "a friend news that will change the internet. Fast pace and high energy from the very first word, no slow "
            "intro. Hit the keywords and the numbers hard. Short pauses, only where marked. Provocative tone on the "
            "final question. Read only the text, exactly as written, without adding, skipping or repeating anything."),
)

PRONUNCIA = {}

RITMO = dict(gap_bloco=0.0, pad_inicio=0.05, pad_fim=0.9)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}You know when you search Google [p=0.1] and the best answer is on *Reddit?* [p=0.2] "
        "{b}Soon, [p=0.1] you'll need to *log in* to read it."),
    dict(id="02", block="anuncio", text=
        "{a}Reddit's CEO, *Steve Huffman,* announced it on Thursday: [p=0.1] "
        "{b}the site is going *logged-in only.*"),
    dict(id="03", block="culpado", text=
        "{a}And the reason [p=0.1] is *Google* itself. [p=0.2] {b}With *AI answers* in search, [p=0.1] "
        "{c}people read the summary [p=0.1] and *don't click* through to Reddit."),
    dict(id="04", block="numeros", text=
        "{a}Visits from Google dropped by *more than one million* a week. [p=0.1] "
        "{b}And Reddit's stock fell *more than fifteen percent.*"),
    dict(id="05", block="robos", text=
        "{a}There's another target: [p=0.1] *bots* that copy Reddit [p=0.1] to train AI. [p=0.2] "
        "{b}He says [p=0.1] almost all unauthorized access [p=0.1] comes from people who are *logged out.*"),
    dict(id="06", block="quando", text=
        "{a}Testing starts *later this year,* [p=0.1] in markets *outside the United States.* [p=0.2] "
        "{b}Huffman said he held off as long as he could, [p=0.1] and called it *a sign of the times.*"),
    dict(id="07", block="final", text=
        "{a}So: [p=0.1] would you make an account [p=0.1] just to read Reddit? [p=0.2] {b}Or is the open internet *over?*"),
]
