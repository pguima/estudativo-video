"""Teste de animação da abertura (cenas 01 e 02) com a narração da Zephyr.
python teste_abertura.py [--preview T]  → saida/teste_abertura.mp4 (ou um quadro PNG no tempo T)
Tempos tirados do Whisper (audio/takeB/parte_1.wav.words.json)."""
import sys, math, subprocess, wave
from pathlib import Path
import numpy as np
import skia
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[2] / "_ferramentas"))
sys.path.insert(0, str(AQUI.parent / "visual"))
import idioma_antigos as lingua  # noqa: E402
lingua.preparar(globals())  # VIDEO_LANG=en: textos da tela em inglês, marcas da narração em inglês
from antigos import *  # noqa: E402,F403
from estudo import mundo  # noqa: E402

if lingua.LANG == "pt":
    FIM = 27.0
    AUDIO = AQUI / "audio" / "takeB" / "parte_1.wav"
    # marcas da fala (s)
    T_RETANGULO, T_BATERIA, T_ANTIGOS, T_NOS, T_BEMVINDOS, T_LUME, T_VITRINE, T_SOBROU = 4.3, 6.9, 9.1, 14.9, 17.5, 20.4, 23.6, 24.9
else:
    # mesmas marcas, tiradas das cues (tempos.json) e das palavras (palavras.json) da narração traduzida
    import json
    _T = json.loads((lingua.audio(AQUI) / "tempos.json").read_text())
    _c1, _c2 = _T["scenes"][0], _T["scenes"][1]
    _M = json.loads((lingua.audio(AQUI) / "marcas_abertura.json").read_text())
    FIM = _c2["end"]
    AUDIO = lingua.audio(AQUI) / "narracao.wav"
    T_RETANGULO, T_ANTIGOS, T_NOS = _c1["cues"]["b"], _c1["cues"]["c"], _c1["cues"]["d"]
    T_BEMVINDOS, T_LUME, T_VITRINE = (_c2["start"] + _c2["cues"][k] for k in "abc")
    T_BATERIA, T_SOBROU = _M["bateria"], _M["sobrou"]
T_RECUA, T_SALAO, T_ENTRA = T_BEMVINDOS - 0.9, T_BEMVINDOS - 0.5, T_BEMVINDOS + 0.9  # câmera recua, salão acende, Lume entra


def envelope():
    """volume da voz por quadro (0..1), para a boca da Lume"""
    with wave.open(str(AUDIO)) as w:
        sr = w.getframerate()
        x = np.frombuffer(w.readframes(int(sr * FIM)), dtype=np.int16).astype(np.float32)
    n = int(FIM * FPS)
    hop = sr // FPS
    rms = np.array([np.sqrt(np.mean(x[i * hop:(i + 1) * hop] ** 2) + 1e-9) for i in range(n)])
    rms = np.clip((rms / np.percentile(rms, 95)) * 1.1 - 0.12, 0, 1)
    return np.convolve(rms, [0.25, 0.5, 0.25], mode="same")


ENV = envelope()


def quadro(c, t, fecha=True):
    f = min(int(t * FPS), len(ENV) - 1)
    # holofote central acende piscando
    if t < 0.35:
        luz = 0.0
    elif t < 0.9:
        luz = [0, 0.7, 0.15, 0.9, 0.4, 1.0][min(5, int((t - 0.35) / 0.09))]
    else:
        luz = 1.0
    st = dict(luz=luz, salao=ease_io(prog(t, T_SALAO, 1.8)))
    st["titulo_a"] = 1 - prog(t, T_SOBROU - 0.2, 0.5)
    st["raiox"] = ep(t, T_RETANGULO, 0.5) * (1 - prog(t, T_ANTIGOS - 0.3, 0.5))
    st["bateria"] = ep(t, T_BATERIA, 0.3) * (1 - prog(t, T_ANTIGOS - 0.3, 0.5))
    fant = ep(t, T_ANTIGOS + 0.3, 0.6) * (1 - prog(t, T_NOS - 0.2, 0.4))
    if T_NOS - 0.6 < t < T_NOS - 0.2:  # falha antes de apagar
        fant *= 0.4 + 0.6 * (int(t * 30) % 2)
    st["tela"] = fant
    # câmera: aproxima devagar na vitrine e depois recua mostrando o salão
    u = ease_io(prog(t, T_RECUA, 2.6))
    zoom = lerp(lerp(2.55, 2.85, t / T_RECUA) if t < T_RECUA else 2.85, 1.0, u)
    cx, cy = 960, lerp(520, 560, u)
    st["zoom"] = zoom
    # a Lume entra pulando pela esquerda
    if t > T_ENTRA:
        te = t - T_ENTRA
        d = 1.5
        k = clamp(te / d)
        x = lerp(-180, 640, ease_out(k) if k < 1 else 1)
        salto = 0.0 if k >= 1 else abs(math.sin(k * math.pi * 3)) * 70 * (1 - k * 0.5)
        p = dict(face=1, look=(0.3, 0.0), smile=0.7)
        sq = -0.08 if salto > 20 else 0.0
        sq += 0.12 * mola(t, T_ENTRA + d, 2.6, 5.0)
        p["squash"] = sq
        p["sway"] = 0.5 * mola(t, T_ENTRA + d, 1.8, 2.5) - (0.35 if salto > 20 else 0)
        # aceno no "Eu sou a Lume"
        if T_LUME <= t < T_LUME + 1.6:
            a = ep(t, T_LUME, 0.25) * (1 - prog(t, T_LUME + 1.3, 0.3))
            p["arm_r"] = lerp(0.15, 2.6 + 0.3 * math.sin((t - T_LUME) * 14), a)
            p["lid"] = 0.15 * a
            p["smile"] = 1.0
        # apresenta a vitrine
        if t >= T_VITRINE - 0.4:
            a = ep(t, T_VITRINE - 0.4, 0.5)
            p["look"] = (lerp(0.3, 1.0, a), lerp(0, -0.35, a))
            p["arm_r"] = lerp(0.15, 2.0, a)
            p["brow"] = 0.6 * a
            p["tilt"] = 0.06 * a
        fala = float(ENV[f]) * 0.85 if t > T_BEMVINDOS else 0.0
        st["lume"] = (x, 880 - salto, 1.25, lume_viva(t, p, fala))
    c.save()
    camera(c, cx, cy, zoom)
    mundo(c, t, st)
    # etiquetas em pílula (no mundo, junto da peça)
    sai = 1 - prog(t, T_ANTIGOS - 0.3, 0.4)
    rotulo(c, "VIDRO E METAL", 850, 420, SKY, ep(t, T_RETANGULO + 0.3, 0.35) * sai, size=12)
    rotulo(c, "BATERIA: 0%", 1078, 476, CORAL, ep(t, T_BATERIA + 0.2, 0.35) * sai, size=12)
    c.restore()
    # logo no fim
    logo(c, W / 2, 175, 0.72, ep(t, T_SOBROU + 0.2, 0.8))
    vinheta(c, lerp(0.85, 0.6, u))
    # abre do preto e fecha no preto
    a = 1 - prog(t, 0.0, 0.3) + (prog(t, FIM - 0.5, 0.5) if fecha else 0.0)
    if a > 0:
        c.drawRect(skia.Rect.MakeWH(W, H), paint("#000000", clamp(a)))


def eventos():
    """efeitos de cada momento da animação (também usados no som do piloto inteiro)"""
    e = T_ENTRA
    return [(0.35, "holofote"), (0.44, "faisca"), (0.53, "faisca"), (0.62, "faisca"),
            (T_RETANGULO, "scan"), (T_RETANGULO + 0.3, "pop"), (T_BATERIA, "bateria"), (T_BATERIA + 0.2, "pop"),
            (T_ANTIGOS + 0.3, "fantasma"), (T_NOS - 0.6, "falha"), (T_RECUA - 0.2, "whoosh"), (T_SALAO + 0.1, "luz"),
            (T_SALAO + 0.5, "luz"), (e, "pulo"), (e + 0.5, "pouso"), (e + 0.5, "pulo"), (e + 1.0, "pouso"), (e + 1.0, "pulo"),
            (e + 1.5, "pouso"), (T_LUME, "brilho"), (T_VITRINE - 0.4, "pop")]


def som(mudo, final):
    """trilha de museu + efeitos em cada momento da animação"""
    from som_antigos import mixar
    mixar(mudo, AUDIO, final, FIM, revela=T_SALAO, fim=T_SOBROU + 0.2, eventos=eventos(), salvar_stems=lingua.saida(AQUI))


def main():
    out = lingua.saida(AQUI)
    out.mkdir(exist_ok=True)
    surf = skia.Surface(W, H)
    c = surf.getCanvas()
    if "--preview" in sys.argv:
        for ts in sys.argv[sys.argv.index("--preview") + 1:]:
            c.clear(hexc(INK))
            quadro(c, float(ts))
            surf.makeImageSnapshot().save(str(out / f"prev_{ts}.png"), skia.kPNG)
        return
    mudo = out / "teste_abertura_mudo.mp4"
    if "--so-som" in sys.argv:
        som(mudo, out / "teste_abertura.mp4")
        return
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{W}x{H}",
                           "-r", str(FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "18",
                           "-pix_fmt", "yuv420p", str(mudo)], stdin=subprocess.PIPE)
    n = int(FIM * FPS)
    for i in range(n):
        c.clear(hexc(INK))
        quadro(c, i / FPS)
        ff.stdin.write(surf.makeImageSnapshot().toarray(colorType=skia.kRGBA_8888_ColorType).tobytes())
        if i % 150 == 0:
            print(f"{i}/{n}", flush=True)
    ff.stdin.close()
    ff.wait()
    final = out / "teste_abertura.mp4"
    som(mudo, final)
    print("ok", final)


if __name__ == "__main__":
    main()
