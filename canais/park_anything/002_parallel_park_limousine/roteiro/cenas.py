# Park Anything · 002 — How to Parallel Park a Limousine | Step-by-Step
# Vídeo 2 da estratégia (claude.ai/artifact/AAVvjE3E7saq4iyFQJgHYC): baliza (tema do 2º maior vídeo do Zed) com um
# veículo absurdo. Inglês, 1920x1080, animação 3D no motor do canal (001), manobra simulada em roteiro/manobra.py.
# Fontes (descrição do vídeo):
#  - California DMV, Driver's Handbook, Parallel parking: vaga pelo menos 3 pés maior que o veículo; ~2 pés do carro
#    ao lado; para-choques alinhados; ~45°; terminar a até 18 pol. do meio-fio; pode precisar ir e voltar.
#  - Manitoba Public Insurance, Driver's Handbook, Parallel parking: 1 m do carro B, para-choques traseiros
#    alinhados, 45°, rodas retas até a frente passar B, volante todo para o outro lado, ajustar para a frente.
#  - Limusine: Lincoln Town Car (entre-eixos 117,7 pol.) esticada 120 pol., 28 pés; esterço do carro de série.
#  - O que é da simulação (dito como tal na narração; o nariz sai 1,7 m para a faixa no passo 2): o jeito de carro bate no meio-fio; a versão da limusine usa
#    ~4 pés de folga e ~20°; a vaga mínima foi ~40 pés; o círculo de giro é ~2× o de um carro (entre-eixos 2×).
# Marcas: {cue} animação · *texto* ênfase · [p=0.3] pausa.

IDIOMA = "en"

TITULO = "How to Parallel Park a Limousine | Step-by-Step"

VOZ = dict(
    tags=["calm", "clear", "confident", "playful"],
    prompt=("Narrate a calm, friendly driving tutorial in American English: adult male voice, warm and confident, like an "
            "experienced driving instructor, with a touch of playful curiosity in the hook. Short sentences, steady pace, "
            "clear diction. Slow down slightly on each instruction and on the numbers. Respect the pauses. Read only the "
            "text, exactly as written, without adding, summarizing or repeating anything."),
)

PRONUNCIA = {}

RITMO = dict(pad_inicio=0.4, pad_fim=1.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}This is a twenty-eight-foot stretch limousine. [p=0.3] {b}And this is the parking space. [p=0.4] {c}Can you "
        "parallel park it, [p=0.1] in *one go?* [p=0.4] {d}Let's find out, [p=0.1] step by step."),
    dict(id="02", block="regra", text=
        "{a}First, [p=0.1] the rule for a normal car. [p=0.3] {b}California's driver handbook says: [p=0.1] find a space "
        "at least *three feet* longer than your vehicle. [p=0.3] {c}For this limo, [p=0.1] that's thirty-one feet. "
        "[p=0.2] Let's try the classic method."),
    dict(id="03", block="falha", text=
        "{a}About two feet from the car in front, [p=0.1] turn the wheel all the way, [p=0.1] and back in at "
        "forty-five degrees. [p=0.4] {b}And... [p=0.3] {c}the long rear end hits the *curb* [p=0.1] before you even get "
        "there."),
    dict(id="04", block="porque", text=
        "{a}Why? [p=0.3] {b}A limo's wheels are about *twice* as far apart as a car's, [p=0.1] {c}so it turns in a "
        "circle about twice as wide. [p=0.3] {d}And everything behind the rear wheels [p=0.1] swings toward the curb."),
    dict(id="05", block="passo1", text=
        "{a}So here's the limo version. [p=0.3] {b}Step one: [p=0.1] pull up next to the car in front, [p=0.1] about "
        "*four feet* away. [p=0.3] {c}Stop when your rear bumpers line up."),
    dict(id="06", block="passo2", text=
        "{a}Step two: [p=0.1] check your mirrors and your blind spot. [p=0.3] {b}Turn the wheel all the way toward the "
        "curb, [p=0.1] and back up slowly. [p=0.3] {c}Watch the nose: [p=0.1] it swings out into the lane. [p=0.3] {d}Stop "
        "turning at about *twenty degrees,* [p=0.1] not forty-five."),
    dict(id="07", block="passo3", text=
        "{a}Step three: [p=0.1] straighten the wheel and keep backing, [p=0.2] {b}until the front corner of the limo is "
        "past the other car's rear bumper."),
    dict(id="08", block="passo4", text=
        "{a}Step four: [p=0.1] turn the wheel all the way the other way, [p=0.1] and keep backing slowly, [p=0.2] {b}until "
        "the limo is straight."),
    dict(id="09", block="passo5", text=
        "{a}Step five: [p=0.1] pull forward to center it in the space, [p=0.2] {b}no more than *eighteen inches* from the "
        "curb."),
    dict(id="10", block="espaco", text=
        "{a}In our simulation, [p=0.1] this only worked with a space of about *forty feet.* [p=0.3] {b}That's twelve feet "
        "more than the limo, [p=0.1] not three. [p=0.3] {c}So if the space looks tight, [p=0.1] keep driving."),
    dict(id="11", block="resumo", text=
        "{a}So, [p=0.1] one more time. [p=0.2] {b}Four feet out, [p=0.1] bumpers lined up. [p=0.2] {c}Back in to twenty "
        "degrees. [p=0.2] {d}Straighten. [p=0.2] {e}Swing the other way. [p=0.2] {f}And pull forward."),
    dict(id="12", block="final", text=
        "{a}Next on Park Anything: [p=0.1] backing a *boat trailer* down a ramp. [p=0.3] {b}Are you a chauffeur? "
        "[p=0.1] Tell us your secret in the comments. [p=0.3] {c}And subscribe, [p=0.1] if you want to see what we park "
        "next."),
]
