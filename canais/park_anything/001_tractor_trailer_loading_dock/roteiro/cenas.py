# Park Anything · 001 — How to Back a Tractor-Trailer into a Loading Dock | Step-by-Step
# Canal novo (estratégia: claude.ai/artifact/AAVvjE3E7saq4iyFQJgHYC, vídeo 1 da lista). Inglês, horizontal 1920x1080,
# ~2 min, animação 3D (câmera aérea em 3/4) com a manobra simulada pela cinemática real (roteiro/manobra.py).
# Técnica e fontes (citadas na descrição):
#  - ré e curva para o lado do motorista sempre que possível; ré devagar, na marcha à ré mais baixa; usar ajudante:
#    manual de CDL da Geórgia (DDS, "Backing Safely");
#  - mão embaixo do volante, mover a mão para o lado em que a carreta deve ir: Manitoba MELT, lição 7;
#  - contraesterçar perto de 45°, não passar de 45° para não "fechar" (jackknife): CDL Study Buddy (alley dock);
#  - objetivo do exercício: parar o mais perto possível do fundo sem passar: roteiro do examinador de Michigan;
#  - pull-ups contam pontos no exame (Geórgia, Basic Vehicle Control Skills Test).
# Marcas: {cue} animação · *texto* ênfase · [p=0.3] pausa.

IDIOMA = "en"

TITULO = "How to Back a Tractor-Trailer into a Loading Dock | Step-by-Step"

VOZ = dict(
    tags=["calm", "clear", "confident"],
    prompt=("Narrate a calm, friendly driving tutorial in American English: adult male voice, warm and confident, like an "
            "experienced driving instructor sitting next to the student. Short sentences, steady pace, clear diction. "
            "Slow down slightly on each instruction and on the reference points. Respect the pauses. Read only the text, "
            "exactly as written, without adding, summarizing or repeating anything."),
)

PRONUNCIA = {}

RITMO = dict(pad_inicio=0.4, pad_fim=1.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}This is a fifty-three-foot trailer. [p=0.3] {b}And this is a dock door, [p=0.1] just a little wider than "
        "the trailer. [p=0.4] {c}Your job is to put one into the other, [p=0.2] *backwards.* [p=0.4] {d}Here's how "
        "truck drivers do it, [p=0.1] step by step."),
    dict(id="02", block="regra", text=
        "{a}First, [p=0.1] the one rule that makes backing a trailer easy. [p=0.3] {b}Put your hand at the *bottom* of "
        "the steering wheel. [p=0.3] {c}Now move your hand toward the side where you want the trailer to go. [p=0.3] "
        "{d}Hand left, [p=0.2] trailer left."),
    dict(id="03", block="preparo", text=
        "{a}Step one: [p=0.1] the setup. [p=0.3] {b}Drive past the dock with the doors on your *left,* [p=0.1] the "
        "driver's side. [p=0.3] {c}That way, you can see the trailer through your own window, [p=0.1] not only in the "
        "mirror. [p=0.3] {d}Stop when the back of the trailer is well past your door. [p=0.2] It needs room to swing."),
    dict(id="04", block="virar", text=
        "{a}Step two: [p=0.1] turn toward the dock. [p=0.3] {b}Hand at the bottom, [p=0.1] move it to the left. "
        "[p=0.3] {c}Back up slowly, [p=0.1] in your lowest reverse gear. [p=0.3] {d}Watch the rear of the trailer start "
        "swinging toward the door."),
    dict(id="05", block="angulo", text=
        "{a}Step three: [p=0.1] watch the angle. [p=0.3] {b}When the trailer gets close to *forty-five degrees* from "
        "the tractor, [p=0.2] {c}start turning the wheel back the other way. [p=0.3] {d}Let the angle keep growing, "
        "[p=0.1] and you're heading for a *jackknife.*"),
    dict(id="06", block="seguir", text=
        "{a}Step four: [p=0.1] follow the trailer. [p=0.3] {b}Now the tractor swings around behind it. [p=0.3] {c}Use "
        "small moves on the wheel. [p=0.2] {d}If the trailer starts to drift, [p=0.1] fix it early, [p=0.1] with a "
        "small correction."),
    dict(id="07", block="endireitar", text=
        "{a}Step five: [p=0.1] straighten out. [p=0.3] {b}When the tractor and the trailer line up, [p=0.1] center "
        "the wheel, [p=0.2] {c}and back straight in."),
    dict(id="08", block="pullup", text=
        "{a}Angle getting too sharp? [p=0.3] {b}Stop. [p=0.2] Pull forward to straighten out, [p=0.1] and try again. "
        "[p=0.3] {c}That's called a *pull-up.* [p=0.2] {d}On the CDL test, [p=0.1] pull-ups can cost you points, "
        "[p=0.1] so set up well, [p=0.1] and you'll need fewer of them."),
    dict(id="09", block="goal", text=
        "{a}Step six: [p=0.1] get out and look. [p=0.3] {b}Drivers call it *GOAL:* [p=0.2] Get Out And Look. [p=0.3] "
        "{c}Then back in slowly, [p=0.1] {d}and stop as close as you can to the dock, [p=0.1] without hitting it."),
    dict(id="10", block="resumo", text=
        "{a}So, [p=0.1] one more time. [p=0.2] {b}Dock on the driver's side. [p=0.2] {c}Turn toward the dock. [p=0.2] "
        "{d}Counter-steer near forty-five degrees. [p=0.2] {e}Follow the trailer. [p=0.2] {f}Straighten out. [p=0.2] "
        "{g}And get out and look."),
    dict(id="11", block="final", text=
        "{a}Next on Park Anything: [p=0.1] parallel parking a *limousine.* [p=0.3] {b}Are you a truck driver? [p=0.1] "
        "Tell us what we missed in the comments. [p=0.3] {c}And subscribe, [p=0.1] if you want to see what we park "
        "next."),
]
