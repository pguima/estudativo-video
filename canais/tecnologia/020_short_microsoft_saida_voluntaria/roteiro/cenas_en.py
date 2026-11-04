# Short — Tecnativo English 020: Microsoft offers money to 60,000 employees to leave (because of AI)
# Same ids, blocks and {cues} as cenas.py. Source: original/fonte_microsoft_saida_voluntaria.md.

TITULO = "Microsoft wants to pay 60,000 employees to leave (and AI is why)"

VOZ = dict(
    tags=["animada", "confiante"],
    prompt=("Narrate a viral tech Short in American English: adult male voice, deep, energetic and excited, like telling "
            "a friend about news that just broke. Fast pace and high energy from the very first word, no slow intro. "
            "Hit the keywords and the numbers hard. Short pauses, only where marked. Provocative tone on the final "
            "question. Read only the text, exactly as written, without adding, skipping or repeating anything."),
)

PRONUNCIA = {}

RITMO = dict(gap_bloco=0.0, pad_inicio=0.05, pad_fim=0.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}Microsoft just offered money [p=0.1] to *sixty thousand employees* to leave. [p=0.2] "
        "{b}That's almost *a quarter* of the company."),
    dict(id="02", block="quem", text=
        "{a}The offer covers the U.S., [p=0.1] Canada, [p=0.1] India [p=0.1] and the U.K. [p=0.2] "
        "{b}And it goes all the way up to *vice president.*"),
    dict(id="03", block="pacote", text=
        "{a}The package, according to Business Insider: [p=0.1] one or two *weeks of pay* [p=0.1] for every six "
        "months on the job, [p=0.1] {b}plus stock [p=0.1] and health care for a while."),
    dict(id="04", block="motivo", text=
        "{a}And the reason? [p=0.1] *Artificial intelligence.* [p=0.2] {b}Microsoft plans to spend over *one hundred "
        "seventy billion dollars* this year, [p=0.1] {c}largely on AI *data centers.*"),
    dict(id="05", block="maio", text=
        "{a}Back in May, [p=0.1] it made a similar offer [p=0.1] to about *nine thousand* people. [p=0.2] "
        "{b}This one is almost *seven times* bigger."),
    dict(id="06", block="memo", text=
        "{a}Employees have until *early December* to decide. [p=0.2] {b}And Microsoft's chief people officer wrote: "
        "[p=0.1] {c}*this is new for us.* [p=0.1] *We'll learn from it.*"),
    dict(id="07", block="final", text=
        "{a}So: [p=0.1] if someone offered you money to leave, [p=0.1] would you *take it?* [p=0.2] {b}Or is AI coming "
        "for your job *anyway?*"),
]
