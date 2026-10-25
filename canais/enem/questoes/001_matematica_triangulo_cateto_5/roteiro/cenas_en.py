# Estudativo English · Math Question 001 — right triangle, leg c = 5, whole-number sides: find a and b.
# English version of cenas.py (same ids, blocks and cues; same visual.py). Run every tool with --lang en.
# Full lesson, horizontal 1920x1080 (~5 min). Labels follow the original question: a = hypotenuse, b and c = legs.
# Marks: {cue} animation · *text* highlight · [p=0.2] pause


TITULO = "Right triangle with a leg of 5 and whole-number sides: find a and b with Pythagoras and a special product"

VOZ = dict(
    tags=["amigavel", "curiosa", "confiante"],
    prompt=("Narrate in natural American English like a friendly math tutor explaining a problem to a student: adult "
            "male voice, warm, clear and engaging, with lively intonation. Start with energy, no intro. Say the "
            "numbers slowly and clearly, one by one. Ask the questions with genuine curiosity, sound surprised at the "
            "trick and celebrate the result. Respect the pauses between sentences. Read only the text, exactly as "
            "written, without adding, summarizing or repeating anything."),
)

PRONUNCIA = {}

RITMO = dict(pad_inicio=0.0, pad_fim=1.6)

SCENES = [
    dict(id="01", block="gancho", text=
        "{a}A right triangle has one leg equal to *five,* [p=0.2] and all three sides are *whole numbers.* [p=0.3] "
        "{b}How long are the other two sides? [p=0.4] {c}It looks like information is missing, [p=0.2] but it isn't. "
        "[p=0.3] {d}In this lesson, you'll solve it step by step, [p=0.1] using the *Pythagorean theorem* [p=0.1] "
        "and a *special product.*"),
    dict(id="02", block="nomes", text=
        "{a}First, the names. [p=0.2] A right triangle is one with a *right angle,* [p=0.1] ninety degrees. [p=0.3] "
        "{b}The side opposite the right angle is the *hypotenuse,* [p=0.1] and it's always the *longest side.* "
        "[p=0.1] We'll call it *a.* [p=0.3] {c}The other two sides are the *legs:* [p=0.1] *b* and *c.* [p=0.3] "
        "{d}In our problem, [p=0.1] leg c is five."),
    dict(id="03", block="pitagoras", text=
        "{a}The Pythagorean theorem connects all three sides: [p=0.2] *a squared equals b squared plus c squared.* "
        "[p=0.3] {b}For example, [p=0.1] in the three, four, five triangle: [p=0.1] three squared is nine, [p=0.1] "
        "four squared is sixteen, [p=0.1] and nine plus sixteen is twenty-five, [p=0.1] which is five squared. "
        "[p=0.2] Notice: [p=0.1] there, five was the hypotenuse. [p=0.3] {c}In our triangle, [p=0.1] five is a leg. "
        "[p=0.2] {d}So: [p=0.1] *a squared equals b squared plus twenty-five.*"),
    dict(id="04", block="infinitas", text=
        "{a}But this equation has *two unknowns.* [p=0.3] {b}If the sides could be any number, [p=0.1] there would "
        "be *infinitely many answers:* [p=0.2] {c}with b equal to one, [p=0.1] a would be the square root of "
        "twenty-six; [p=0.2] with b equal to two, [p=0.1] the square root of twenty-nine; [p=0.1] and so on. [p=0.3] "
        "{d}The key piece of information is this: [p=0.1] *the sides are whole numbers.*"),
    dict(id="05", block="chute", text=
        "{a}One option is to test: [p=0.1] b equals one, two, three, [p=0.1] until a squared is a *perfect "
        "square.* [p=0.3] {b}It works, [p=0.1] but it's slow, [p=0.1] and it doesn't prove there's no other answer. "
        "[p=0.3] {c}There's a better way, [p=0.1] one that finds *all* the answers at once."),
    dict(id="06", block="isolar", text=
        "{a}Step one: [p=0.1] move b squared to the other side. [p=0.2] {b}It's being added, [p=0.1] so it moves "
        "over as a *subtraction:* [p=0.2] {c}*a squared minus b squared equals twenty-five.* [p=0.3] {d}On the left "
        "we now have a *difference of two squares.* [p=0.2] And that's where the special product comes in."),
    dict(id="07", block="produto", text=
        "{a}Special products are multiplications that show up so often [p=0.1] that it's worth *knowing the result "
        "by heart.* [p=0.3] {b}One of them is the *product of a sum and a difference:* [p=0.2] {c}x plus y, [p=0.1] "
        "times x minus y, [p=0.1] equals *x squared minus y squared.* [p=0.3] {d}You can check it with the "
        "distributive property: [p=0.2] {e}x times x is x squared; [p=0.1] x times minus y is minus x y; [p=0.2] "
        "{f}y times x is plus x y; [p=0.1] and y times minus y is minus y squared. [p=0.3] {g}The middle terms "
        "*cancel out,* [p=0.2] leaving x squared minus y squared."),
    dict(id="08", block="exemplo", text=
        "{a}Here's an example with numbers: [p=0.1] ten plus three, [p=0.1] times ten minus three, [p=0.2] is thirteen "
        "times seven, [p=0.1] which is ninety-one. [p=0.3] {b}And ten squared minus three squared, [p=0.1] a hundred "
        "minus nine, [p=0.1] is also *ninety-one.* [p=0.2] It works!"),
    dict(id="09", block="aplica", text=
        "{a}Now, reading the formula backwards, [p=0.1] with a instead of x and b instead of y: [p=0.2] a squared "
        "minus b squared [p=0.1] equals *a plus b, times a minus b.* [p=0.3] {b}So our equation becomes: [p=0.1] "
        "*a plus b, times a minus b, equals twenty-five.* [p=0.3] {c}Look at what happened: [p=0.1] the difference "
        "of squares turned into a *product of two whole numbers* [p=0.1] that equals twenty-five."),
    dict(id="10", block="divisores", text=
        "{a}Which products of positive whole numbers equal twenty-five? [p=0.3] {b}Only two: [p=0.1] *one times "
        "twenty-five,* [p=0.1] and *five times five.* [p=0.3] {c}Now, an important detail: [p=0.1] since b is "
        "positive, [p=0.1] a plus b is *bigger* than a minus b. [p=0.3] {d}So a plus b is the larger factor, "
        "[p=0.1] and a minus b is the smaller one. [p=0.3] {e}In the five times five case, [p=0.1] both factors "
        "would be equal, [p=0.1] and that only happens if b is zero. [p=0.2] A side of length zero [p=0.1] *is not a "
        "triangle.*"),
    dict(id="11", block="sistema", text=
        "{a}Only one case is left: [p=0.1] a plus b equals *twenty-five,* [p=0.1] and a minus b equals *one.* "
        "[p=0.3] {b}That's a system. [p=0.1] Adding the two equations, [p=0.1] b *cancels out:* [p=0.2] {c}two a "
        "equals twenty-six, [p=0.1] so *a is thirteen.* [p=0.3] {d}Back to the first one: [p=0.1] thirteen plus b "
        "equals twenty-five, [p=0.1] so *b is twelve.*"),
    dict(id="12", block="confere", text=
        "{a}Always check. [p=0.2] Twelve squared is one hundred forty-four, [p=0.1] five squared is twenty-five: "
        "[p=0.1] the sum is one hundred sixty-nine. [p=0.2] {b}And thirteen squared [p=0.1] is also *one hundred "
        "sixty-nine.* [p=0.3] {c}The triangle is *five, twelve, thirteen,* [p=0.1] and it's the *only* answer with "
        "whole-number sides."),
    dict(id="13", block="generaliza", text=
        "{a}And the best part: [p=0.1] the method works for other legs too. [p=0.2] {b}With a leg of seven: [p=0.1] "
        "a plus b, times a minus b, equals forty-nine. [p=0.2] {c}One times forty-nine [p=0.1] gives a equal to "
        "twenty-five [p=0.1] and b equal to twenty-four: [p=0.1] *the seven, twenty-four, twenty-five triangle.* "
        "[p=0.3] {d}Now it's your turn: [p=0.1] try it with a leg of *nine,* [p=0.1] and leave your answer in the "
        "comments. [p=0.2] Hint: [p=0.1] there may be *more than one.*"),
    dict(id="14", block="resumo", text=
        "{a}To sum up the path: [p=0.2] {b}Pythagoras; [p=0.2] {c}isolate the difference of squares; [p=0.2] "
        "{d}apply the special product; [p=0.2] {e}list the divisors; [p=0.2] {f}and solve the system."),
    dict(id="15", block="aulas", text=
        "{a}Every tool you saw in this question [p=0.1] has a *full lesson* here on Estudativo English: [p=0.3] "
        "{b}*the Pythagorean theorem,* [p=0.2] {c}*special products,* [p=0.2] {d}and *systems of equations.* [p=0.3] "
        "{e}If you want to learn each one from scratch, [p=0.1] look for these lessons on the channel. [p=0.4] "
        "{f}And if this question helped, [p=0.1] subscribe to *Estudativo English* [p=0.1] for the next one."),
]
