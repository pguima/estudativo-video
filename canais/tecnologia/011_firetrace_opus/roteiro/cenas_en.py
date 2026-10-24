# Script — Tecnativo English 011: FireTrace, the wildfire analysis prototype made with Claude Opus 5.5
# English version of cenas.py: SAME ids, blocks and {cues} (the visual.py is shared; on-screen text in textos_en.py).
# Base: original/fonte_firetrace.md. Same rule: nothing the author didn't say is invented; "how it's built" is a
# labeled hypothesis. Marks: {cue} animation · *text* highlight · [p=0.4] pause · numbers spelled out (as spoken)

TITULO = "A wildfire command dashboard built with Claude Opus 5.5? What FireTrace shows (and what it doesn't)"

VOZ = dict(
    tags=["alegre", "confiante"],
    prompt=("Narrate like the host of a tech channel showing an impressive project found online: adult male voice, "
            "deep, confident and enthusiastic, but precise and never over the top. Genuine curiosity at the start, "
            "clear teaching tone in the interface tour, and a more serious, careful tone in the real-world and "
            "limitations parts. Stress the key words and the numbers. Natural pace, unhurried, respecting the pauses "
            "between sentences. Read only the text, exactly as written, without adding, skipping or repeating anything."),
)

PRONUNCIA = {}

SCENES = [
    # ================= HOOK =================
    dict(id="01", block="gancho", text=
        "{a}A three-dimensional map [p=0.2] of a mountain range in California. [p=0.3] {b}The fire spreading, [p=0.2] "
        "*hour by hour.* [p=0.4] {c}Six drones in the air, [p=0.2] {d}and a thermal camera flagging a hot spot at "
        "*nine hundred eighty-three degrees.* [p=0.5] {e}It looks like command center software. [p=0.3] "
        "But it's a *prototype,* [p=0.2] and a developer says he built it [p=0.2] with *Claude Opus five point five.*"),

    # ================= THE POST =================
    dict(id="02", block="post", text=
        "{t}The post is from *Dilum Sanjaya,* [p=0.2] a developer who shares AI-made visual demos on X. [p=0.4] "
        "{a}On *October eighth,* [p=0.2] he wrote: [p=0.3] {b}played around with an idea for a *wildfire analysis "
        "tool.* [p=0.3] It visualizes how the fire progresses over time, [p=0.2] tracks *hot spots* with drones "
        "[p=0.2] and monitors *firefighting efforts.* [p=0.3] {c}Made with *Opus five point five.* [p=0.5] "
        "{d}Attached, a video of almost *two minutes,* [p=0.2] with no sound. [p=0.4] "
        "{e}Eight days later, [p=0.2] the official *Claude* account featured the project [p=0.2] in a list of *six* "
        "community creations."),

    # ================= TOUR =================
    dict(id="03", block="incidente", text=
        "{s}Everything you see here is our own *recreation,* [p=0.2] "
        "drawn to explain it. [p=0.5] {a}The app is called *FireTrace:* [p=0.2] wildfire forensic analysis. [p=0.4] "
        "{b}The case is the *Ridgeview* incident, [p=0.2] in the San Gabriel Mountains, California, [p=0.2] from "
        "August fourteenth to eighteenth, twenty twenty-four. [p=0.3] {c}By the looks of it, [p=0.2] a *demo* "
        "scenario. [p=0.5] {d}In the center, a *3D map* of the terrain, [p=0.3] {e}and the fire *perimeter* growing, "
        "[p=0.2] with the time marked on each section, [p=0.2] starting from ignition, at two twenty-six p.m."),
    dict(id="04", block="tempo", text=
        "{a}At the bottom, a *timeline* you play like a video, [p=0.3] {b}with the key events: [p=0.2] "
        "ignition, [p=0.2] rapid growth, [p=0.2] a spot fire, [p=0.2] the fire crossing the ridge [p=0.2] "
        "and containment. [p=0.4] {c}Next to it, charts for *burned area,* [p=0.2] *rate of spread* [p=0.2] and "
        "*elevation profile.* [p=0.4] {d}On the right, *layers* you can toggle: [p=0.2] terrain, [p=0.2] aerial "
        "imagery, [p=0.2] burn scar, [p=0.2] modeled spread [p=0.2] and containment lines. [p=0.4] "
        "{e}And a *weather* panel."),
    dict(id="05", block="drones", text=
        "{t}On the *drones* tab, [p=0.2] six of six are airborne, [p=0.2] each one with a *job.* [p=0.4] "
        "{a}One maps the perimeter, [p=0.2] {b}another circles the most active fire front, [p=0.2] {c}another watches "
        "a spot fire. [p=0.3] {d}There's patrol, [p=0.2] survey [p=0.2] and even a drone just to *relay* "
        "the signal. [p=0.4] {e}Click on one of them, [p=0.2] and the *infrared camera* opens, [p=0.2] with the "
        "telemetry on screen. [p=0.4] {f}And the detections drop into a list: [p=0.2] *hot spot,* "
        "[p=0.2] nine hundred eighty-three degrees Celsius."),
    dict(id="06", block="recursos", text=
        "{t}The third tab shows the *resources* in the field: [p=0.2] *thirteen units.* [p=0.4] {a}Air tankers, [p=0.2] "
        "like a *DC-10* [p=0.2] and a *C-130,* [p=0.3] {b}helicopters [p=0.2] and an air attack plane, [p=0.3] "
        "{c}engines, [p=0.2] ground crews [p=0.2] and a dozer. [p=0.4] {d}There's a log of every *retardant "
        "drop,* [p=0.3] {e}and charts for gallons, [p=0.2] line built [p=0.2] and personnel. [p=0.3] "
        "{f}You can even follow a plane with a *chase* camera."),

    # ================= HOW IT'S BUILT =================
    dict(id="07", block="camadas", text=
        "{t}So how do you build something like this? [p=0.4] {a}First, what we *don't know:* [p=0.2] Dilum didn't say "
        "how long it took, [p=0.2] what he asked the AI, [p=0.2] which libraries he used, [p=0.2] and he didn't publish "
        "the code. [p=0.5] {b}So what follows is how apps like this are *usually* built. [p=0.4] "
        "{c}At the base, a *data* layer: [p=0.2] hourly perimeters, [p=0.2] drone positions, [p=0.2] "
        "retardant drops. [p=0.3] In a prototype, [p=0.2] *simulated* data. [p=0.4] {d}On top of that, the *3D map,* "
        "[p=0.2] typically drawn with *WebGL* [p=0.2] from a digital elevation model of the terrain. [p=0.4] "
        "{e}Then, the *timeline,* [p=0.3] {f}and finally the *panels* and charts."),
    dict(id="08", block="relogio", text=
        "{a}The secret of a dashboard like this is having *a single clock.* [p=0.4] {b}You drag the timeline [p=0.2] "
        "and *everything* updates together: [p=0.3] {c}the perimeter on the map, [p=0.2] {d}the drone positions, "
        "[p=0.2] {e}the charts [p=0.2] and the event list. [p=0.5] {f}That's *a lot of pieces* talking to each other."),

    # ================= OPUS 5.5 =================
    dict(id="09", block="opus", text=
        "{t}And what does this say about *Opus five point five?* [p=0.4] {a}Anthropic released the model on "
        "*September twenty-second.* [p=0.3] {b}According to the company, [p=0.2] it reaches the level of *Claude Fable "
        "five point one* on most work, [p=0.3] {c}at about *forty percent less* than Opus five. [p=0.4] "
        "{d}Anthropic highlights *long-running* tasks, [p=0.3] {e}and cites a test where several models built a game "
        "from a single prompt: [p=0.3] Opus five point five got the top score for *graphics and polish.* "
        "[p=0.5] {f}But a video doesn't show *how many attempts* [p=0.2] or "
        "how much manual tweaking it took."),

    # ================= REAL WORLD =================
    dict(id="10", block="real", text=
        "{t}And in the real world? [p=0.3] This already exists, [p=0.2] with real data. [p=0.4] {a}NASA runs *FIRMS,* "
        "[p=0.2] which delivers satellite-detected fires [p=0.2] within *three hours* of observation. [p=0.4] "
        "{b}In the United States, [p=0.2] planes with *infrared* sensors fly *at night,* [p=0.2] and update the "
        "heat perimeter *once a day.* [p=0.4] {c}The U.S. Forest Service drones [p=0.2] see "
        "through *smoke,* [p=0.2] and, according to the agency, [p=0.2] can find a hot spot *two inches across* "
        "[p=0.2] from nearly *half a mile* away. [p=0.4] {d}And in Brazil, [p=0.2] *INPE* processes over *two hundred* "
        "satellite images a day [p=0.2] to detect *heat spots,* [p=0.2] in its Queimadas program."),
    dict(id="11", block="compara", text=
        "{t}But there's a big gap [p=0.2] between a beautiful prototype [p=0.2] and a firefighting system. [p=0.4] "
        "{a}In the prototype, the data is for *demo;* [p=0.2] in the real world, it comes from *sensors,* satellites "
        "and crews. [p=0.4] {b}In the prototype, delay doesn't matter; [p=0.2] in the real world, *minutes* count. "
        "[p=0.4] {c}And a real system has to be *field-tested* [p=0.3] {d}and have someone *accountable* for the "
        "decisions made with it."),

    # ================= LIMITS =================
    dict(id="12", block="limites", text=
        "{t}And the caveats about this post. [p=0.4] {a}The prototype only exists *on video:* [p=0.2] there's no code "
        "or demo to try. [p=0.4] {b}The author doesn't say whether the data is *real or simulated.* [p=0.4] {c}Made "
        "with Opus five point five is *his word;* [p=0.2] we don't know how much manual work went in. [p=0.4] {d}And "
        "the feature on the Claude account is a *showcase,* [p=0.2] not an independent review."),

    # ================= SUMMARY =================
    dict(id="13", block="resumo", text=
        "{t}To sum up. [p=0.4] {a}FireTrace is a wildfire analysis prototype, [p=0.2] posted by Dilum Sanjaya "
        "on October eighth. [p=0.4] {b}3D map, timeline, drones with thermal cameras and resources in the field, "
        "[p=0.2] all *in sync.* [p=0.4] {c}He says he built it with *Opus five point five,* [p=0.2] but didn't show "
        "how. [p=0.4] {d}The real world already uses satellites, planes and drones, [p=0.2] with *validated* data. "
        "[p=0.4] {e}It's a great *illustrated idea,* [p=0.2] not a ready-made tool."),

    # ================= CTA + SOURCES =================
    dict(id="14", block="cta", text=
        "If this video showed you something new, [p=0.2] {like}leave a *like,* [p=0.2] {sub}*subscribe* to the "
        "channel [p=0.2] {bell}and turn on the *notification bell,* so you don't miss the next tools. [p=0.5] "
        "{com}And tell me in the *comments:* [p=0.2] what tool would you try to build with an AI like this? [p=0.5] "
        "{bye}*See you in the next video.* [p=1.0]"),
    dict(id="15", block="fontes", text=
        "{a}The *sources* for this video [p=0.2] are on screen [p=0.2] and in the description. [p=5.0]"),
]
