"""Gera uma trilha ambiente calma (pad sintetizado, livre de direitos).

Uso: python musica.py <proj> [duração_s]
Gera <proj>/audio/trilha.wav (volume já baixo, para ficar sob a narração).
"""
import json, subprocess, sys
from pathlib import Path
import numpy as np

SR = 48000


def note(n):  # MIDI -> Hz
    return 440.0 * 2 ** ((n - 69) / 12)


# Am9 - Fmaj7 - Cmaj7 - Gsus/6 (voicings abertos, região média-grave)
CHORDS = [
    [45, 52, 57, 60, 64, 71],
    [41, 48, 53, 57, 64, 69],
    [36, 48, 52, 55, 59, 64],
    [43, 50, 55, 57, 62, 67],
]
BAR = 9.0  # segundos por acorde


def pad(freqs, dur, rng):
    t = np.arange(int(dur * SR)) / SR
    out = np.zeros_like(t)
    for f in freqs:
        for det in (-0.12, 0.0, 0.13):  # leve desafinação = coro
            ff = f * 2 ** (det / 12)
            ph = rng.uniform(0, 2 * np.pi)
            lfo = 1 + 0.002 * np.sin(2 * np.pi * rng.uniform(0.05, 0.12) * t)
            w = np.sin(2 * np.pi * ff * lfo * t + ph)
            w += 0.18 * np.sin(2 * np.pi * 2 * ff * t + ph)  # um pouco de brilho
            amp = 1.0 / (1 + (f / 400.0))  # graves mais presentes
            out += w * amp
    # envelope com crossfade longo
    a = np.minimum(1, t / 2.5) * np.minimum(1, (dur - t) / 2.5)
    return out * a


def main(proj, dur=None):
    proj = Path(proj)
    if dur is None:
        dur = json.loads((proj / "audio" / "tempos.json").read_text(encoding="utf-8"))["total"] + 2
    rng = np.random.default_rng(3)
    total = np.zeros(int((dur + BAR * 2) * SR))
    k, pos = 0, 0.0
    while pos < dur + BAR:
        seg = pad([note(n) for n in CHORDS[k % 4]], BAR + 2.5, rng)
        i0 = int(pos * SR)
        total[i0:i0 + len(seg)] += seg[: len(total) - i0]
        pos += BAR; k += 1
    total = total[: int(dur * SR)]
    total /= np.max(np.abs(total)) + 1e-9
    fade = np.minimum(1, np.arange(len(total)) / (3 * SR)) * np.minimum(1, (len(total) - np.arange(len(total))) / (4 * SR))
    total *= fade
    raw = proj / "audio" / "trilha.f32"
    (total.astype(np.float32) * 0.5).tofile(raw)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", str(raw),
                    "-af", "lowpass=f=2200,highpass=f=60,aecho=0.8:0.7:120|260:0.25|0.18,"
                           "loudnorm=I=-34:TP=-9:LRA=7", "-ac", "2", "-ar", str(SR),
                    str(proj / "audio" / "trilha.wav")], check=True)
    raw.unlink()
    print("trilha ok", dur)


if __name__ == "__main__":
    main(sys.argv[1], float(sys.argv[2]) if len(sys.argv) > 2 else None)
