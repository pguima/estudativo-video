# Short — Tecnativo English 015: Anthropic (the company behind Claude) filed to go public on the Nasdaq
# Same ids, blocks and {cues} as cenas.py. Source: original/fonte_ipo_anthropic.md (S-1 of Oct 26, 2026 + press).

TITULO = "The company behind Claude lost $80 billion in 6 months and is going public"

VOZ = dict(
    tags=["animada", "confiante"],
    prompt=("Narrate a viral tech and business Short in American English: adult male voice, deep, energetic and excited, "
            "like telling a friend a shocking piece of news you just read. Fast pace and high energy from the very first "
            "word, no slow intro. Hit the keywords and the numbers hard. Short pauses, only where marked. Playful, "
            "provocative tone on the final question. Read only the text, exactly as written, without adding, skipping or "
            "repeating anything."),
)

PRONUNCIA = {}

RITMO = dict(gap_bloco=0.0, pad_inicio=0.05, pad_fim=0.9)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}The company behind *Claude* lost *eighty billion dollars* [p=0.1] in *six months.* [p=0.2] "
        "{b}And it still wants the *biggest debut in stock market history.*"),
    dict(id="02", block="s1", text=
        "{a}On Monday, [p=0.1] *Anthropic* filed the official paperwork [p=0.1] {b}to sell shares on the *Nasdaq.*"),
    dict(id="03", block="receita", text=
        "{a}Look at the revenue: [p=0.1] in twenty twenty-three, *forty-one million* dollars. [p=0.1] "
        "{b}In twenty twenty-five, *four point six billion.* [p=0.1] "
        "{c}And just in the first half of this year: [p=0.1] *sixteen point three billion.*"),
    dict(id="04", block="prejuizo", text=
        "{a}So, [p=0.1] what about the loss? [p=0.2] {b}*Seventy-two billion* of it is *accounting:* [p=0.1] "
        "{c}the company got so valuable [p=0.1] that debt that turns into shares got *pricier* on the books. [p=0.2] "
        "{d}From operations, [p=0.1] the loss was *six hundred ninety-three million.*"),
    dict(id="05", block="recorde", text=
        "{a}US media say it could raise *a hundred billion* dollars, [p=0.1] "
        "{b}beating the *SpaceX* record, [p=0.1] *seventy-five billion,* in June. [p=0.2] "
        "{c}And the stock price isn't even out yet."),
    dict(id="06", block="controle", text=
        "{a}But here's the catch: [p=0.1] the *seven founders* keep *fifty point one percent* of the votes, [p=0.1] "
        "{b}and an *independent trust* elects most of the board."),
    dict(id="07", block="final", text=
        "{a}So: [p=0.1] would you buy a share of the company behind Claude? [p=0.2] {b}Or is it a *bubble?*"),
]
