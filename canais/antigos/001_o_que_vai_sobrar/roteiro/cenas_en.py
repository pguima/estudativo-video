# The Museum of 2526 — Video 01 (pilot): "What Will Be Left of Us in 10,000 Years?"
# Versão em inglês do cenas.py: MESMOS ids, blocks e {cues} (o visual.py é o mesmo; textos da tela em textos_en.py).
# Marcas: {cue} animação · *texto* destaque · [p=0.2] pausa · números por extenso.

TITULO = "What Will Be Left of Us in 10,000 Years?"

VOZ = dict(
    voiceName="Zephyr",
    tags=["curious", "gentle"],
    prompt=("Narrate an animated science documentary: an adult female voice, calm, curious and warm, like a museum "
            "curator who admires what she is showing. The tone of someone sharing a fascinating secret, with light, dry "
            "humor on the ironic lines. Relaxed, unhurried pace, respecting the pauses. Never apocalyptic: even in the "
            "dark parts the voice stays serene. Read only the text, exactly as written, without adding, skipping or "
            "repeating anything."),
)

PRONUNCIA = {}

SCENES = [
    # ── A VITRINE ─────────────────────────────────────────────
    dict(id="01", block="vitrine",
         text=
        "{a}This object was found inside a layer of rock. [p=0.3] "
        "{b}It's a rectangle of glass and metal, [p=0.1] with a dead battery inside. [p=0.3] "
        "{c}The Ancients carried one of these in their pocket [p=0.1] all day long. [p=0.2] "
        "They slept with it right beside them. [p=0.4] "
        "{d}We still don't quite know why."),
    dict(id="02", block="vitrine",
         text=
        "{a}Welcome to the *Museum of the Age of the Ancients.* [p=0.2] "
        "{b}I'm Lume, [p=0.1] the curator. [p=0.3] "
        "{c}And today we're opening the first display case: [p=0.2] *what was left of them.*"),

    # ── O ESTRANHAMENTO ──────────────────────────────────────
    dict(id="03", block="estranhamento",
         text=
        "{a}The Ancients lived between the twentieth and twenty-first centuries. [p=0.2] There were *eight billion* of "
        "them. [p=0.3] "
        "{b}And they made things like no species before them. [p=0.3] "
        "{c}Around *twenty twenty,* [p=0.1] the weight of everything they had built, [p=0.1] "
        "buildings, [p=0.1] roads, [p=0.1] machines, [p=0.2] {d}became equal to the weight of *all living things* on "
        "the planet combined."),
    dict(id="04", block="estranhamento",
         text=
        "{a}And yet, [p=0.1] we know very little about them. [p=0.3] "
        "{b}The Ancients kept almost everything in digital form: [p=0.1] photos, [p=0.1] letters, [p=0.1] books, "
        "[p=0.1] music. [p=0.2] {c}And digital files age badly. [p=0.1] Every time they changed machines, [p=0.1] "
        "a little more became impossible to open. [p=0.3] "
        "{d}In twenty fifteen, [p=0.1] one of the creators of the internet, [p=0.1] Vint Cerf, [p=0.1] warned [p=0.2] "
        "that their era could become a *digital dark age.* [p=0.4] "
        "{e}That's why, here at the museum, [p=0.1] we study the Ancients the way you study ruins: [p=0.2] *by what's "
        "left on the ground.*"),

    # ── A CIÊNCIA: AVANÇAR O RELÓGIO ─────────────────────────
    dict(id="05", block="relogio",
         text=
        "{a}So let's run an experiment. [p=0.2] Imagine the Ancients left the stage [p=0.1] and no one stayed "
        "behind to fix anything. [p=0.3] "
        "{b}Let's move the clock forward. [p=0.3] {c}*A hundred years.* [p=0.3] {d}*A thousand years.* [p=0.3] "
        "{e}*Ten thousand years.*"),
    dict(id="06", block="cem_anos",
         text=
        "{a0}Some things start changing right away. [p=0.2] Beneath New York, [p=0.1] the subway pumps remove "
        "[p=0.1] about *thirteen million gallons* of water every day [p=0.1] that seep in through the tunnel walls. "
        "[p=0.2] With no one to run the pumps, [p=0.1] the tunnels begin to flood. [p=0.3] "
        "{a}In the first hundred years, [p=0.1] what seems strongest falls first: [p=0.2] *reinforced concrete.* "
        "[p=0.3] {b}Inside it there are steel bars. [p=0.1] When water gets in through a crack, [p=0.1] the steel "
        "rusts, [p=0.2] {c}and rust takes up *more space* than the steel did. [p=0.2] "
        "It pushes the concrete from the inside out, [p=0.1] until it breaks. [p=0.3] "
        "{d}Bridges, [p=0.1] overpasses [p=0.1] and skyscrapers give way, [p=0.1] one by one. [p=0.3] "
        "{e}Meanwhile, [p=0.1] Roman concrete buildings, [p=0.1] *with no steel inside,* [p=0.1] "
        "have been standing for about two thousand years."),
    dict(id="07", block="mil_anos",
         text=
        "{a}After *a thousand years,* [p=0.1] the cities have become hills covered in brush. [p=0.3] "
        "{b}The Ancients did try to protect themselves from being forgotten. [p=0.2] {c}In an old coal mine in the "
        "Arctic, [p=0.1] in Svalbard, [p=0.1] they stored data on *photographic film,* [p=0.1] designed to last about "
        "a thousand years. [p=0.4] "
        "{d}But what survives best of a civilization [p=0.1] is almost never what it wanted to keep. [p=0.3] "
        "{e}It's what it *threw away.*"),
    dict(id="08", block="aterro",
         text=
        "{a}And the Ancients threw things away in a very particular way: [p=0.1] in *landfills,* [p=0.1] mountains of "
        "compacted trash covered with dirt. [p=0.3] "
        "{b}In the late nineteen eighties, [p=0.1] an archaeologist from the Ancients themselves, [p=0.1] William "
        "Rathje, [p=0.1] of the University of Arizona, [p=0.1] decided to dig into these landfills [p=0.1] as if they "
        "were ruins. [p=0.3] "
        "{c}He found newspapers from decades earlier [p=0.1] that could still be read. [p=0.2] "
        "{d}And hot dogs that had been buried for about fifteen years [p=0.1] that still *looked like hot dogs.* "
        "[p=0.3] {e}In there it's so dry and packed [p=0.1] that almost nothing rots."),
    dict(id="09", block="ceramica",
         text=
        "{a}Archaeologists have known this for a long time. [p=0.2] The most common find at many digs [p=0.1] isn't "
        "gold or statues. [p=0.3] {b}It's *broken pottery.* [p=0.3] "
        "{c}Fired clay doesn't rot like wood [p=0.1] and doesn't rust like metal. [p=0.2] And nobody reuses a broken "
        "pot: [p=0.1] it goes straight into the trash. [p=0.3] "
        "{d}So, ten thousand years from now, [p=0.1] the Ancients will be remembered by shards of mugs, [p=0.1] of tiles "
        "[p=0.1] and of *toilets.* [p=0.3] {e}Lots [p=0.1] and lots of toilets."),
    dict(id="10", block="dez_mil",
         text=
        "{a}After *ten thousand years,* [p=0.1] some things have barely changed. [p=0.3] "
        "{b}At Mount Rushmore, [p=0.1] in the United States, [p=0.1] the Ancients carved the faces of four presidents "
        "into granite. [p=0.2] {c}By the park geologists' estimate, [p=0.1] the rock loses only about *one inch* "
        "[p=0.1] every ten thousand years. [p=0.3] "
        "{d}The four faces will still be there, [p=0.1] serious, [p=0.1] looking out over a forest [p=0.1] with no one "
        "in it."),
    dict(id="11", block="plastico",
         text=
        "{a}And their trash is still there too. [p=0.2] By twenty fifteen alone, [p=0.1] they had made "
        "more than *eight billion tons of plastic.* [p=0.3] "
        "{b}Of the part that became waste, [p=0.1] *seventy-nine percent* ended up in landfills [p=0.1] or in "
        "nature. [p=0.3] "
        "{c}Plastic doesn't rot like wood. [p=0.1] It just breaks into smaller and smaller pieces. [p=0.3] "
        "{d}And sometimes, [p=0.2] *it turns into stone.* [p=0.3] "
        "{e}In twenty fourteen, [p=0.1] on a beach in Hawaii, [p=0.1] geologists described a new kind of rock: "
        "[p=0.2] plastic melted in campfires, [p=0.1] mixed with sand, [p=0.1] shells [p=0.1] and bits of "
        "lava. [p=0.2] {f}They named it *plastiglomerate.* [p=0.3] "
        "{g}It's heavier than plastic alone. [p=0.1] It sinks, [p=0.1] gets buried [p=0.1] and can enter "
        "the rock record."),
    dict(id="12", block="frango",
         text=
        "{a}Now, [p=0.1] here's a detail that always surprises our visitors. [p=0.3] "
        "{b}The most common fossil of the Ancients [p=0.1] isn't a human bone. [p=0.4] {c}It's a *chicken bone.* [p=0.4] "
        "{d}In twenty eighteen, [p=0.1] British researchers showed that the chicken raised by the Ancients "
        "was a new animal: [p=0.2] {e}at least *twice the size* of a medieval chicken, [p=0.1] with a "
        "skeleton, [p=0.1] bone chemistry [p=0.1] and genetics unlike any of its ancestors. [p=0.3] "
        "{f}And there were about *twenty-three billion* of them alive at the same time. [p=0.4] "
        "{g}To a paleontologist of the future, [p=0.2] this may very well be *the age of the chicken.*"),
    dict(id="13", block="plutonio",
         text=
        "{a}But there's one mark no future scientist will miss. [p=0.3] "
        "{b}Starting in the *nineteen fifties,* [p=0.1] atomic bomb tests spread "
        "*plutonium* across the entire planet. [p=0.2] {c}It fell with the rain [p=0.1] and settled at the bottom of "
        "lakes and seas, [p=0.1] in a thin layer, [p=0.1] all over the world. [p=0.3] "
        "{d}Plutonium two thirty-nine takes about *twenty-four thousand years* to lose half its "
        "radioactivity. [p=0.2] {e}Ten thousand years later, [p=0.1] the layer is still there, [p=0.1] easy to detect. "
        "[p=0.3] "
        "{f}At a lake in Canada, [p=0.1] Crawford Lake, [p=0.1] the Ancients' geologists even proposed this "
        "layer as the start of a new epoch of the Earth: [p=0.2] the *Anthropocene.* [p=0.3] "
        "{g}In twenty twenty-four, [p=0.1] the proposal was rejected. [p=0.3] "
        "The Ancients couldn't even agree on that."),
    dict(id="14", block="ar",
         text=
        "{a}And there's an even subtler mark: [p=0.2] *the air.* [p=0.3] "
        "{b}In Antarctica, [p=0.1] every layer of snow that turned into ice [p=0.1] traps tiny bubbles of the air of "
        "its time. [p=0.3] {c}Before factories, [p=0.1] the air held about *two hundred eighty* parts per million of "
        "carbon dioxide. [p=0.2] {d}In May twenty twenty-five, [p=0.1] the peak went past *four hundred thirty.* "
        "[p=0.3] {e}Whoever drills into the ice from this era [p=0.1] will find, [p=0.1] trapped in bubbles, [p=0.1] "
        "the breath of a civilization in a hurry."),
    dict(id="15", block="aviso",
         text=
        "{a}And there's one message the Ancients wrote to the future *on purpose.* [p=0.3] "
        "{b}They buried their most dangerous nuclear waste in tunnels hundreds of meters deep. [p=0.2] "
        "{c}In Finland, [p=0.1] the first repository of its kind, [p=0.1] called Onkalo, [p=0.1] received a license "
        "to operate in *October twenty twenty-six.* [p=0.3] "
        "{d}But how do you warn someone, [p=0.1] thousands of years from now, [p=0.1] not to dig there? [p=0.2] "
        "No language lasts that long. [p=0.3] "
        "{e}In the United States, [p=0.1] a report from nineteen ninety-three [p=0.1] drafted the text "
        "of just such a warning. [p=0.2] {f}It begins like this: [p=0.4] "
        "*This place is not a place of honor.* [p=0.3] *Nothing valued is here.* [p=0.5] "
        "{g}It's strange and beautiful at the same time: [p=0.2] one of the Ancients' first letters to the future [p=0.1] "
        "was a request [p=0.2] to stay away."),

    # ── O ABISMO ─────────────────────────────────────────────
    dict(id="16", block="abismo",
         text=
        "{a}Now let's go further. [p=0.2] *One million years.* [p=0.4] "
        "{b}The cities have become a layer of compressed rubble. [p=0.1] The plastic has become a dark sheet between "
        "the rocks. [p=0.3] "
        "{c}In twenty eighteen, [p=0.1] two scientists, [p=0.1] Gavin Schmidt, [p=0.1] of NASA, [p=0.1] and Adam "
        "Frank, [p=0.2] asked an uncomfortable question: [p=0.2] {d}if an industrial civilization had existed "
        "on Earth millions of years ago, [p=0.1] would we be able to tell? [p=0.4] "
        "{e}Their answer: [p=0.2] *it wouldn't be easy.* [p=0.3] "
        "{f}Given enough time, [p=0.1] an entire civilization can become just a strange band in the rock: "
        "[p=0.2] a shift in carbon, [p=0.1] traces of plastic, [p=0.1] rare elements, [p=0.2] "
        "{g}that from far away looks like other natural changes in Earth's past. [p=0.5] "
        "{h}Eight billion people. [p=0.3] A century in a hurry. [p=0.3] And in the end, [p=0.2] *a thin band of "
        "different rock.*"),
    dict(id="17", block="longe",
         text=
        "{a}The clearest traces of the Ancients [p=0.1] will be far from here. [p=0.3] "
        "{b}On the Moon, [p=0.1] where there's no wind or rain, [p=0.1] the *astronauts' footprints* could last "
        "millions of years. [p=0.3] "
        "{c}About twenty-two thousand miles up, [p=0.1] dead satellites, [p=0.1] pushed into an orbit "
        "called the *graveyard,* [p=0.1] could keep circling for millions of years. [p=0.3] "
        "{d}Two probes, [p=0.1] the Voyagers, [p=0.1] carry a *golden record* with sounds and images of Earth, [p=0.1] "
        "made to last about *a billion years* among the stars. [p=0.3] "
        "{e}And the Ancients' radio broadcasts [p=0.1] already form a bubble around the Earth [p=0.1] with a "
        "radius of more than *a hundred light-years.*"),

    # ── A VIRADA ─────────────────────────────────────────────
    dict(id="18", block="virada",
         text=
        "{a}But there's one thing the Ancients were slow to realize. [p=0.4] "
        "{b}The layer they would leave behind [p=0.2] *hadn't been written yet.* [p=0.4] "
        "{c}Every layer of rock is just a record of choices. [p=0.2] {d}More plastic [p=0.1] or less. [p=0.2] "
        "More carbon [p=0.1] or less. [p=0.2] More bombs [p=0.1] or less. [p=0.4] "
        "{e}And they started to choose. [p=0.2] "
        "{e2}When they discovered that a gas from refrigerators and spray cans was opening a hole in the ozone "
        "layer, [p=0.1] they signed an agreement, [p=0.1] the *Montreal Protocol,* [p=0.1] in nineteen "
        "eighty-seven. [p=0.2] And the layer began to recover. [p=0.3] "
        "{f}They recorded archives built to last for centuries. [p=0.2] They buried the most dangerous waste "
        "deep underground, [p=0.1] with warnings for whoever came after. [p=0.2] {g}And they started measuring what "
        "they were leaving in the ground, [p=0.2] precisely so they could change it."),
    dict(id="19", block="virada",
         text=
        "{a}The Ancients were brilliant [p=0.1] and completely lost [p=0.1] at the same time. [p=0.4] "
        "{b}But they were the first civilization that *knew* it was turning into rock. [p=0.4] "
        "{c}And that gave them a chance no people before them ever had: [p=0.3] *deciding what would be left.*"),

    # ── A ETIQUETA ───────────────────────────────────────────
    dict(id="20", block="etiqueta",
         text=
        "{a}So, [p=0.1] let's write the label for *object number one.* [p=0.3] "
        "{b}Rectangle of glass and metal. [p=0.2] Twenty-first century. [p=0.4] "
        "{c}*The Ancients kept the whole world in here.* [p=0.3] *Nothing was left in here.* [p=0.3] "
        "{d}*What was left is what they did out there.*"),
    dict(id="21", block="proxima",
         text=
        "{a}In the next display case: [p=0.2] why the Ancients spent hours a day [p=0.1] staring at glowing "
        "rectangles. [p=0.4] "
        "{b}What about you? [p=0.2] What object from your home should go into the museum? [p=0.2] {c}Tell me in the "
        "comments. [p=0.2] I read every one."),
]
