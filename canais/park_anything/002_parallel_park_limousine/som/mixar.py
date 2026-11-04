"""Som do Park Anything 002 (limusine), todo sintetizado (livre de direitos), a partir do mixar.py do 001: trilha leve
de tutorial, motor V8 macio que acelera quando a limusine anda (limusine não tem bipe de ré nem freio a ar), a batida
no meio-fio na tentativa "de carro", "whoosh" nas cortinas e cliques nos cartões. A narração (audio/narracao.wav), quando existir, entra por cima
com a trilha abaixando sozinha (sidechain). Saída: final/<ARQUIVO_FINAL>, −14 LUFS.
Uso: python som/mixar.py   (depois de render.py <proj> --lang en --video)"""
import subprocess
import sys
from pathlib import Path

import numpy as np

PROJ = Path(__file__).resolve().parents[1]
FERR = PROJ.parents[2] / "_ferramentas"
sys.path[:0] = [str(FERR), str(PROJ / "roteiro")]
import motor  # noqa: E402
import visual as V  # noqa: E402

SR = 48000
rng = np.random.default_rng(3)


def wav(path, x):
    x = np.clip(x, -1, 1)
    st = np.stack([x, x], axis=1) if x.ndim == 1 else x
    pcm = (st * 32767).astype("<i2").tobytes()
    import wave
    with wave.open(str(path), "wb") as w:
        w.setnchannels(2); w.setsampwidth(2); w.setframerate(SR); w.writeframes(pcm)


def lp(x, fc):
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    X *= 1 / np.sqrt(1 + (f / fc) ** 8)
    return np.fft.irfft(X, len(x))


def hp(x, fc):
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    X *= 1 / np.sqrt(1 + (fc / np.maximum(f, 1e-3)) ** 4)
    return np.fft.irfft(X, len(x))


def note(n):
    return 440.0 * 2 ** ((n - 69) / 12)


# ---------------------------------------------------------------- trilha
def trilha(dur):
    n = int(dur * SR)
    out = np.zeros(n)
    bpm = 96
    beat = 60 / bpm
    bar = 4 * beat
    # I – V – vi – IV em Ré maior (acordes abertos)
    prog = [[50, 57, 62, 66, 69], [45, 52, 57, 61, 64], [47, 54, 59, 62, 66], [43, 50, 55, 59, 62]]
    baixo = [38, 33, 35, 31]
    t_all = np.arange(n) / SR

    def ep_note(f, t0, d, vol):
        i0 = int(t0 * SR)
        m = min(n - i0, int(d * SR))
        if m <= 0:
            return
        t = np.arange(m) / SR
        env = np.exp(-t * 2.2) * np.minimum(1, t / 0.006)
        mod = np.sin(2 * np.pi * f * 2.0 * t) * 1.2 * np.exp(-t * 4)
        w = np.sin(2 * np.pi * f * t + mod) * env * (1 + 0.25 * np.sin(2 * np.pi * 4.5 * t))
        out[i0:i0 + m] += w * vol

    k = 0
    t = 0.0
    while t < dur:
        ch = prog[k % 4]
        for j, nn in enumerate(ch):                     # acorde "pianinho" em colcheias suaves
            for b in (0, 1.5, 2.5):
                ep_note(note(nn), t + b * beat + j * 0.012, beat * 1.6, 0.05 / (1 + j * 0.15))
        fb = note(baixo[k % 4])
        for b in (0, 2, 2.5, 3.5):
            i0, m = int((t + b * beat) * SR), int(beat * 0.9 * SR)
            if i0 + m < n:
                tt = np.arange(m) / SR
                out[i0:i0 + m] += 0.16 * np.sin(2 * np.pi * fb * tt) * np.exp(-tt * 3) * np.minimum(1, tt / 0.01)
        for b in range(4):                               # bumbo leve + chimbal
            i0 = int((t + b * beat) * SR)
            if b in (0, 2) and i0 + 9600 < n:
                tt = np.arange(9600) / SR
                out[i0:i0 + 9600] += 0.22 * np.sin(2 * np.pi * (52 + 70 * np.exp(-tt * 30)) * tt) * np.exp(-tt * 9)
            for h in (0.0, 0.5):
                i1 = int((t + (b + h) * beat) * SR)
                if i1 + 2400 < n:
                    out[i1:i1 + 2400] += 0.03 * rng.standard_normal(2400) * np.exp(-np.arange(2400) / SR * 60)
        t += bar
        k += 1
    out = hp(out, 35)
    fade = np.minimum(1, t_all / 2.0) * np.minimum(1, (dur - t_all) / 3.0)
    return out * fade


# ---------------------------------------------------------------- efeitos
def motor_diesel(dur, vel_frames):
    """ronco do diesel: harmônicos de ~28 Hz com ruído; o giro e o volume sobem com a velocidade"""
    n = int(dur * SR)
    t = np.arange(n) / SR
    fps = motor.FPS
    v = np.interp(t, np.arange(len(vel_frames)) / fps, np.abs(vel_frames))
    v = np.convolve(v, np.ones(SR // 3) / (SR // 3), mode="same")
    rpm = 1 + 0.55 * np.clip(v / 1.5, 0, 1.6)
    f0 = 38.0 * rpm
    ph = 2 * np.pi * np.cumsum(f0) / SR
    x = np.zeros(n)
    for h, a in ((1, 0.6), (2, 0.9), (3, 0.5), (4, 0.35), (6, 0.2)):
        x += a * np.sin(h * ph)
    x *= 1 + 0.35 * np.sin(ph * 0.5)                   # "batida" dos cilindros
    ruido = lp(rng.standard_normal(n), 900) * 0.25
    x = lp(x + ruido, 700)
    vol = 0.035 + 0.05 * np.clip(v / 1.5, 0, 1.4)
    return x / (np.abs(x).max() + 1e-9) * vol


def bipe_re(dur, vel_frames):
    n = int(dur * SR)
    t = np.arange(n) / SR
    fps = motor.FPS
    v = np.interp(t, np.arange(len(vel_frames)) / fps, vel_frames)
    ativo = v > 0.05                                    # s crescendo = de ré
    x = np.zeros(n)
    # bipe de 1,1 kHz, 0,5 s ligado / 0,5 s desligado, a partir de cada início de ré
    inicio = None
    for i in range(0, n, 480):
        if ativo[i] and inicio is None:
            inicio = t[i]
        if not ativo[i]:
            inicio = None
        if inicio is not None and ((t[i] - inicio) % 1.0) < 0.5:
            seg = slice(i, min(n, i + 480))
            tt = t[seg]
            x[seg] = np.sign(np.sin(2 * np.pi * 1100 * tt)) * 0.6 + np.sin(2 * np.pi * 1100 * tt) * 0.4
    x = lp(x, 3500)
    # eco curto do pátio
    d = int(0.09 * SR)
    y = x.copy()
    y[d:] += 0.35 * x[:-d]
    return y * 0.06


def freio_ar(dur, vel_frames):
    n = int(dur * SR)
    x = np.zeros(n)
    fps = motor.FPS
    v = np.abs(vel_frames)
    movendo = False
    for i in range(1, len(v)):
        if v[i] > 0.15:
            movendo = True
        if movendo and v[i] < 0.01:
            movendo = False
            i0 = int(i / fps * SR)
            m = int(0.9 * SR)
            if i0 + m < n:
                tt = np.arange(m) / SR
                s = hp(rng.standard_normal(m), 2500) * np.exp(-tt * 4.5) * np.minimum(1, tt / 0.01)
                x[i0:i0 + m] += s * 0.10
    return x


def batida(dur, tc):
    """pneu raspando no meio-fio + baque"""
    n = int(dur * SR)
    x = np.zeros(n)
    i0, m = int(tc * SR), int(0.6 * SR)
    if i0 + m < n:
        tt = np.arange(m) / SR
        baque = np.sin(2 * np.pi * (70 + 60 * np.exp(-tt * 25)) * tt) * np.exp(-tt * 9)
        raspa = lp(rng.standard_normal(m), 2500) * np.exp(-tt * 7) * 0.5
        x[i0:i0 + m] = (baque + raspa) * 0.32
    return x


def whoosh(dur, tempos):
    n = int(dur * SR)
    x = np.zeros(n)
    for tc in tempos:
        i0 = int((tc - 0.45) * SR)
        m = int(0.9 * SR)
        if i0 < 0 or i0 + m > n:
            continue
        tt = np.arange(m) / SR
        env = np.sin(np.pi * tt / 0.9) ** 2
        s = lp(rng.standard_normal(m), 1800) * env
        x[i0:i0 + m] += s * 0.22
    return x


def cliques(dur, tempos):
    n = int(dur * SR)
    x = np.zeros(n)
    for tc in tempos:
        i0 = int(tc * SR)
        m = int(0.12 * SR)
        if i0 < 0 or i0 + m > n:
            continue
        tt = np.arange(m) / SR
        x[i0:i0 + m] += 0.10 * np.sin(2 * np.pi * (900 + 600 * np.exp(-tt * 40)) * tt) * np.exp(-tt * 45)
    return x


# ---------------------------------------------------------------- mistura
def main():
    K = V.K
    dur = K("total") + 0.5
    ts, s, dx, d_show, vel, _modo = V._tabela()
    # o deslocamento para a frente do preparo também move o motor
    vtot = vel.copy()
    vdx = np.gradient(dx, ts)
    vtot_mot = np.abs(vtot) + np.abs(vdx)
    som = PROJ / "som"
    musica = trilha(dur)
    fx = (motor_diesel(dur, vtot_mot) + batida(dur, K("03.c") + 0.25)
          + whoosh(dur, [K("02"), K("05"), K("11")])
          + cliques(dur, [K(f"{i:02d}.a") + 0.3 for i in range(1, 13)] + [K("05.c") + 0.3, K("06.c") + 0.2, K("07.b") + 0.2,
                                                                          K("09.b") + 0.3, K("10.b")]))
    wav(som / "trilha.wav", musica)
    wav(som / "sfx.wav", fx)
    nome = V.ARQUIVO_FINAL
    out = PROJ / "final" / nome
    out.parent.mkdir(exist_ok=True)
    segdir = PROJ / "trabalho" / "segmentos"
    lst = segdir / "lista.txt"
    lst.write_text("".join(f"file '{q.name}'\n" for q in sorted(segdir.glob("seg_*.mp4"))), encoding="utf-8")
    video = PROJ / "trabalho" / "video_mudo.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(video)],
                   check=True)
    voz = PROJ / "audio" / "narracao.wav"
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", str(video), "-i", str(som / "trilha.wav"), "-i", str(som / "sfx.wav")]
    if voz.exists():
        cmd += ["-i", str(voz), "-filter_complex",
                "[3:a]aresample=48000,aformat=sample_fmts=fltp:channel_layouts=stereo,asplit[v1][v2];"
                "[1:a]aformat=sample_fmts=fltp:channel_layouts=stereo,volume=0.55[m];[m][v2]sidechaincompress=threshold=0.02:ratio=6:attack=40:release=700[md];"
                "[2:a]aformat=sample_fmts=fltp:channel_layouts=stereo,volume=0.9[fx];[v1][md][fx]amix=inputs=3:duration=first:normalize=0,"
                "loudnorm=I=-14:TP=-1.0:LRA=11[a]"]
    else:
        cmd += ["-filter_complex",
                "[1:a]volume=0.9[m];[2:a]volume=1.0[fx];[m][fx]amix=inputs=2:duration=first:normalize=0,"
                "loudnorm=I=-16:TP=-1.0:LRA=11[a]"]
    cmd += ["-map", "0:v", "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-shortest",
            "-movflags", "+faststart", str(out)]
    subprocess.run(cmd, check=True)
    print("FINAL:", out)


if __name__ == "__main__":
    main()
