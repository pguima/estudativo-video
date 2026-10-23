"""Som PADRÃO do canal Tecnologia: trilha eletrônica + efeitos de interface (HUD) nos elementos e transições.
Tudo SINTETIZADO aqui (livre de direitos). O render.py chama sozinho no --final quando o visual.py usa `import tech`.

Uso manual: python3 _ferramentas/som_tech.py <proj>        (gera <proj>/som/trilha.wav e sfx.wav e mixa o final)
            python3 _ferramentas/som_tech.py <proj> --so-som   (só gera os .wav)
Pré-requisitos: audio/tempos.json, audio/narracao.wav e trabalho/video_mudo.mp4 (render.py --video --final).

Trilha: eletrônica "tech" ~112 BPM em ré menor (Dm Bb F C): arpejo pluck em semicolcheias com eco, baixo pulsando
(sidechain do bumbo), pad, bumbo 4/4, palmas no 2 e 4, chimbal. Arranjo pelas cenas: 1ª cena = intro (pad + arpejo
abrindo o filtro), da 2ª cena ao CTA = batida completa, CTA e créditos = sem bumbo, só arpejo/pad e fade-out.

Efeitos (padrão automático, pelos tempos do roteiro):
  - início de cada cena (menos a 1ª) → "whoosh" digital (transição) + "lock" curto do título HUD;
  - cada cue {x} → "pop" de interface (nota varia na escala), bem baixo;
  - CTA: like → clique, sub → clique, bell → sininho, com → notificação, bye → brilho.
Ajustes por vídeo no visual.py (opcional):
  SOM = dict(sfx={"05.c": ["typing@+0.2", "pop@+1.4"], "10.e": "alert", "03.b": None},  # None = sem efeito
             bpm=112, trilha=True)
  SOM = None desliga o som (vídeo só com narração).
  Efeitos: pop, click, whoosh, lock, typing, notif, data, glitch, impact, confirm, alert, deny, bell, shimmer.
"""
import json
import subprocess
import sys
from pathlib import Path
import numpy as np

SR = 48000
G_TRILHA = 0.30   # trilha (~-26 LUFS) ~10 dB abaixo da voz (-16.5) antes do ducking
G_SFX = 0.6


def note(n):
    return 440.0 * 2 ** ((n - 69) / 12)


def lp_fft(x, fc, order=4):
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    X *= 1 / np.sqrt(1 + (f / fc) ** (2 * order))
    return np.fft.irfft(X, len(x))


def hp_fft(x, fc, order=2):
    X = np.fft.rfft(x)
    f = np.fft.rfftfreq(len(x), 1 / SR)
    with np.errstate(divide="ignore"):
        X *= 1 / np.sqrt(1 + (fc / np.maximum(f, 1e-3)) ** (2 * order))
    return np.fft.irfft(X, len(x))


def saw(f, tt):
    return 2 * ((f * tt) % 1.0) - 1


def nrm(x):
    return x / (np.max(np.abs(x)) + 1e-9)


class Som:
    def __init__(self, proj, cfg=None):
        self.proj = Path(proj)
        self.cfg = cfg or {}
        d = json.loads((self.proj / "audio" / "tempos.json").read_text(encoding="utf-8"))
        self.scenes = d["scenes"]
        self.C = {}
        for s in self.scenes:
            self.C[s["id"]] = s["start"]
            for k, v in s["cues"].items():
                self.C[f"{s['id']}.{k}"] = s["start"] + v
        self.DUR = d["total"] + 0.3
        self.N = int(self.DUR * SR)
        self.T = np.arange(self.N) / SR
        self.rng = np.random.default_rng(7)
        self.BEAT = 60 / self.cfg.get("bpm", 112)
        self.S16 = self.BEAT / 4
        self.BAR = 4 * self.BEAT
        # seções: intro = 1ª cena; fim = cena do CTA (ou as 2 últimas)
        ids = [s["id"] for s in self.scenes]
        cta = [s for s in self.scenes if "like" in s["cues"]]
        self.t_full = self.scenes[1]["start"] if len(ids) > 1 else 2.0
        self.t_out = cta[0]["start"] if cta else self.scenes[max(1, len(ids) - 2)]["start"]

    # ------------------------------------------------------------ utilidades
    def add(self, out, t, sig):
        i0 = int(t * SR)
        if 0 <= i0 < self.N:
            n = min(len(sig), self.N - i0)
            out[i0:i0 + n] += sig[:n]

    def env(self, points):
        ts, vs = zip(*points)
        return np.interp(self.T, ts, vs)

    def chord(self, t):
        PROG = [[38, 50, 53, 57, 62], [34, 46, 50, 53, 58], [41, 53, 57, 60, 65], [36, 48, 52, 55, 60]]  # Dm Bb F C
        return PROG[int(t // (2 * self.BAR)) % 4]

    # ------------------------------------------------------------ trilha
    def arp(self):
        out = np.zeros(self.N)
        L = int(0.22 * SR); tt = np.arange(L) / SR
        order = [0, 1, 2, 3, 2, 1, 3, 2, 0, 2, 3, 1, 2, 3, 1, 2]
        for i in range(int(self.DUR / self.S16) + 1):
            t = i * self.S16
            ch = self.chord(t)
            f = note(ch[1 + order[i % 16] % 4] + 12)
            w = 0.6 * saw(f, tt) + 0.4 * np.sign(np.sin(2 * np.pi * f * tt))
            self.add(out, t, w * np.exp(-tt * 16) * np.minimum(1, tt / 0.002) * (1.0 if i % 4 == 0 else 0.7))
        # filtro "abrindo" ao longo do vídeo (aprox.: mistura de duas versões filtradas)
        dark, bright = lp_fft(out, 900, 2), lp_fft(out, 3800, 2)
        k = self.env([(0, 0.0), (self.t_full, 0.7), (self.t_out, 1.0), (self.DUR, 0.5)])
        x = dark * (1 - k) + bright * k
        d = int(3 * self.S16 * SR)   # eco em colcheia pontuada
        echo = np.concatenate([np.zeros(d), x[:-d]])
        m = np.max(np.abs(x)) + 1e-9
        return x / m, echo / m

    def bass(self):
        out = np.zeros(self.N)
        L = int(self.BEAT / 2 * 0.95 * SR); tt = np.arange(L) / SR
        for i in range(int(self.DUR / (self.BEAT / 2)) + 1):
            t = i * self.BEAT / 2
            f = note(self.chord(t)[0])
            s = saw(f, tt) + 0.8 * np.sin(2 * np.pi * f / 2 * tt)
            self.add(out, t, s * np.minimum(1, tt / 0.004) * np.exp(-tt * 3))
        return nrm(lp_fft(out, 420, 3))

    def pad(self):
        out = np.zeros(self.N)
        seg = 2 * self.BAR
        for k in range(int(self.DUR / seg) + 1):
            t0 = k * seg
            ch = self.chord(t0 + 0.01)
            n = int((seg + 1.0) * SR); tt = np.arange(n) / SR
            s = sum(saw(note(m) * 2 ** (d / 12), tt + self.rng.uniform(0, 1)) for m in ch[1:] for d in (-0.08, 0.08))
            a = np.minimum(1, tt / 0.8) * np.minimum(1, np.maximum(0, seg + 1.0 - tt) / 1.0)
            self.add(out, t0, s * a)
        return nrm(lp_fft(out, 1100, 3))

    def drums(self):
        N, B = self.N, self.BEAT
        kick, clap, hat = np.zeros(N), np.zeros(N), np.zeros(N)
        L = int(0.28 * SR); tt = np.arange(L) / SR
        k = np.sin(2 * np.pi * np.cumsum(50 + 120 * np.exp(-tt * 45)) / SR) * np.exp(-tt * 12)
        Lc = int(0.2 * SR); tc = np.arange(Lc) / SR
        burst = sum(np.exp(-np.maximum(0, tc - o) * 60) * (tc >= o) for o in (0, 0.012, 0.024))
        cl = lp_fft(hp_fft(self.rng.normal(0, 1, Lc), 900), 5000) * burst
        Lh = int(0.035 * SR); th = np.arange(Lh) / SR
        pump = np.ones(N)                       # "sidechain": baixo e pad abaixam em cada bumbo
        Lp = int(0.3 * SR); pp = 1 - 0.65 * np.exp(-np.arange(Lp) / SR * 14)
        for b in range(int(self.DUR / B) + 1):
            t = b * B
            self.add(kick, t, k)
            i0 = int(t * SR)
            if i0 < N:
                n = min(Lp, N - i0)
                pump[i0:i0 + n] = np.minimum(pump[i0:i0 + n], pp[:n])
            if b % 4 in (1, 3):
                self.add(clap, t, cl)
            self.add(hat, t + B / 2, self.rng.normal(0, 1, Lh) * np.exp(-th * 120))
            self.add(hat, t + B / 4, self.rng.normal(0, 1, Lh) * np.exp(-th * 200) * 0.35)
            self.add(hat, t + 3 * B / 4, self.rng.normal(0, 1, Lh) * np.exp(-th * 200) * 0.35)
        return nrm(kick), nrm(clap), nrm(hp_fft(hat, 7000)), pump

    def trilha(self):
        arp, echo = self.arp()
        bass, pad = self.bass(), self.pad()
        kick, clap, hat, pump = self.drums()
        f, o, D = self.t_full, self.t_out, self.DUR
        g_arp = self.env([(0, 0), (1.0, 0.7), (f, 0.8), (o, 0.9), (D - 6, 0.7), (D, 0)])
        g_pad = self.env([(0, 0), (1.5, 0.9), (f, 0.7), (o, 0.9), (D - 6, 0.9), (D, 0)])
        g_bass = self.env([(0, 0), (f - 0.5, 0), (f, 1.0), (o - 0.3, 1.0), (o + 0.5, 0.3), (D - 6, 0.2), (D, 0)])
        g_kick = self.env([(0, 0), (f - 0.05, 0), (f, 1.0), (o - 0.3, 1.0), (o, 0), (D, 0)])
        g_clap = self.env([(0, 0), (f + 2 * self.BAR, 0), (f + 2 * self.BAR + 0.1, 1.0), (o - 0.3, 1.0), (o, 0), (D, 0)])
        g_hat = self.env([(0, 0), (f - 0.05, 0), (f, 1.0), (o, 0.6), (D - 6, 0.4), (D, 0)])
        bed = 0.40 * bass * g_bass + 0.26 * pad * g_pad
        bed *= np.where(g_kick > 0.1, pump, 1.0)
        mono = 0.28 * arp * g_arp + bed + 0.62 * kick * g_kick + 0.26 * clap * g_clap + 0.08 * hat * g_hat
        left = mono + 0.18 * echo * g_arp
        right = mono - 0.06 * arp * g_arp + 0.10 * np.concatenate([np.zeros(int(0.15 * SR)), echo[:-int(0.15 * SR)]]) * g_arp
        st = np.stack([left, right], 1)
        return st / (np.max(np.abs(st)) + 1e-9) * 0.9

    # ------------------------------------------------------------ efeitos
    def fx(self, nome, i=0):
        r, tt_ = self.rng, lambda d: np.arange(int(d * SR)) / SR
        if nome == "pop":
            scale = [76, 79, 81, 83, 86, 88]
            tt = tt_(0.12); f = note(scale[i % len(scale)])
            return np.sin(2 * np.pi * f * tt * (1 + 0.15 * np.exp(-tt * 60))) * np.exp(-tt * 38) * 0.6
        if nome == "click":
            tt = tt_(0.05)
            return (np.sin(2 * np.pi * 2200 * tt) * np.exp(-tt * 260) + r.normal(0, 0.4, len(tt)) * np.exp(-tt * 500)) * 0.7
        if nome == "lock":
            tt = tt_(0.18)
            a = np.sin(2 * np.pi * note(93) * tt) * np.exp(-tt * 40) * (tt < 0.06)
            b = np.sin(2 * np.pi * note(100) * (tt - 0.06)) * np.exp(-np.maximum(0, tt - 0.06) * 30) * (tt >= 0.06)
            return (a + b) * 0.35
        if nome == "whoosh":
            d = 0.7; tt = tt_(d)
            x = r.normal(0, 1, len(tt)) * np.sin(np.pi * tt / d) ** 2
            sweep = np.sin(2 * np.pi * np.cumsum(300 + 2200 * (tt / d) ** 2) / SR) * np.sin(np.pi * tt / d) ** 3 * 0.25
            return lp_fft(hp_fft(x, 500), 3000) * 0.5 + sweep
        if nome == "typing":
            d = 1.3; L = int(d * SR); out = np.zeros(L); t = 0.0
            while t < d - 0.05:
                n = int(0.018 * SR); i0 = int(t * SR)
                out[i0:i0 + n] += r.normal(0, 1, n) * np.exp(-np.arange(n) / SR * 400) * r.uniform(0.5, 1)
                t += 1 / 16 * r.uniform(0.6, 1.4)
            return hp_fft(out, 2500) * 0.6
        if nome == "notif":
            tt = tt_(0.6)
            a = np.sin(2 * np.pi * note(83) * tt) * np.exp(-tt * 9) * (tt < 0.3)
            b = np.sin(2 * np.pi * note(88) * (tt - 0.11)) * np.exp(-np.maximum(0, tt - 0.11) * 7) * (tt >= 0.11)
            return (a + b) * 0.5
        if nome == "data":
            d = 1.2; L = int(d * SR); out = np.zeros(L); t = 0.0
            while t < d - 0.06:
                n = int(r.uniform(0.02, 0.05) * SR); tt = np.arange(n) / SR; i0 = int(t * SR)
                out[i0:i0 + n] += np.sign(np.sin(2 * np.pi * r.choice([1200, 1500, 1800, 2400, 3000]) * tt)) * np.hanning(n) * 0.4
                t += r.uniform(0.04, 0.11)
            return lp_fft(out, 5000) * np.linspace(1, 0.3, L)
        if nome == "glitch":
            d = 0.6; L = int(d * SR); out = np.zeros(L); t = 0.0
            while t < d - 0.08:
                n = int(r.uniform(0.03, 0.08) * SR); i0 = int(t * SR); hold = r.integers(20, 80)
                x = np.round(np.repeat(r.normal(0, 1, n // hold + 1), hold)[:n] * 3) / 3
                out[i0:i0 + n] += x * np.hanning(n); t += r.uniform(0.07, 0.16)
            return lp_fft(out, 4000) * 0.6
        if nome == "impact":
            tt = tt_(2.2)
            boom = np.sin(2 * np.pi * np.cumsum(40 + 90 * np.exp(-tt * 14)) / SR) * np.exp(-tt * 2.2)
            shine = sum(np.sin(2 * np.pi * note(m) * tt) for m in (74, 81, 86)) * np.exp(-tt * 1.8) * 0.12
            rise = lp_fft(r.normal(0, 1, len(tt)), 2500) * np.exp(-tt * 6) * 0.3
            return nrm(boom + shine + rise)
        if nome == "confirm":
            tt = tt_(0.35)
            a = np.sin(2 * np.pi * note(81) * tt) * np.exp(-tt * 18) * (tt < 0.12)
            b = np.sin(2 * np.pi * note(88) * (tt - 0.08)) * np.exp(-np.maximum(0, tt - 0.08) * 12) * (tt >= 0.08)
            return (a + b) * 0.5
        if nome == "alert":
            tt = tt_(0.4)
            return np.sin(2 * np.pi * note(72) * tt) * np.sign(np.sin(2 * np.pi * 7 * tt)).clip(0) \
                * np.exp(-tt * 6) * 0.35 + np.sin(2 * np.pi * note(79) * tt) * np.exp(-tt * 10) * 0.15
        if nome == "deny":
            tt = tt_(0.3)
            x = saw(note(52), tt) + saw(note(53), tt)
            return lp_fft(x, 1400, 2) * np.exp(-tt * 9) * 0.25
        if nome == "bell":
            tt = tt_(3.0)
            s = sum(a * np.sin(2 * np.pi * note(m) * tt) * np.exp(-tt * d) for m, a, d in ((84, 1, 1.5), (91, .5, 2), (96, .3, 2.6)))
            return nrm(s) * np.minimum(1, tt / 0.005) * 0.7
        if nome == "shimmer":
            tt = tt_(2.5)
            s = sum(np.sin(2 * np.pi * note(m) * tt) * np.exp(-np.maximum(0, tt - k * 0.07) * 2.2) * (tt >= k * 0.07)
                    for k, m in enumerate((86, 89, 93, 98)))
            return nrm(s) * 0.5
        raise ValueError(f"efeito desconhecido: {nome}")

    GAIN = dict(pop=0.07, click=0.10, lock=0.08, whoosh=0.13, typing=0.09, notif=0.09, data=0.05, glitch=0.10,
                impact=0.45, confirm=0.09, alert=0.09, deny=0.10, bell=0.16, shimmer=0.12)

    def sfx(self):
        buf = np.zeros((self.N, 2))
        plano = {}                                  # tempo → [(nome, pan)]
        for j, s in enumerate(self.scenes):
            if j > 0:
                plano.setdefault(s["start"] - 0.25, []).append("whoosh")
                if "t" in s["cues"]:
                    plano.setdefault(s["start"] + 0.35, []).append("lock")
            for k in s["cues"]:
                cue = f"{s['id']}.{k}"
                padrao = dict(like="click", sub="click", bell="bell", com="notif", bye="shimmer").get(k, "pop")
                if k == "t":
                    continue
                plano.setdefault(cue, []).append(padrao)
        # ajustes do visual.py substituem o padrão da cue
        extra = self.cfg.get("sfx", {})
        plano = {k: v for k, v in plano.items() if k not in extra}
        for cue, v in extra.items():
            if v:
                plano[cue] = [v] if isinstance(v, str) else list(v)
        n_pop = 0
        for chave, itens in plano.items():
            base = chave if isinstance(chave, float) else self.C[chave]
            for it in itens:
                nome, _, off = it.partition("@")
                t = base + (float(off) if off else 0.0)
                sig = self.fx(nome, n_pop)
                n_pop += nome == "pop"
                pan = 0.0 if nome in ("whoosh", "impact", "bell", "shimmer") else ((n_pop % 3) - 1) * 0.25
                i0 = int(t * SR)
                if not 0 <= i0 < self.N:
                    continue
                n = min(len(sig), self.N - i0)
                g = self.GAIN[nome]
                buf[i0:i0 + n, 0] += sig[:n] * g * (1 - max(0, pan))
                buf[i0:i0 + n, 1] += sig[:n] * g * (1 + min(0, pan))
        return np.clip(buf, -1, 1)


def save(path, st):
    path.parent.mkdir(exist_ok=True)
    raw = path.with_suffix(".f32")
    st.astype(np.float32).tofile(raw)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "2", "-i", str(raw), str(path)], check=True)
    raw.unlink()


def gerar(proj, cfg=None):
    s = Som(proj, cfg)
    som = Path(proj) / "som"
    if s.cfg.get("trilha", True):
        save(som / "trilha.wav", s.trilha())
    save(som / "sfx.wav", s.sfx())


def mixar(proj, out):
    """vídeo mudo + narração + trilha (ducking pela voz) + efeitos → out"""
    proj = Path(proj)
    som = proj / "som"
    F = "aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo"
    ins = ["-i", str(proj / "trabalho" / "video_mudo.mp4"), "-i", str(proj / "audio" / "narracao.wav")]
    if (som / "trilha.wav").exists():
        ins += ["-i", str(som / "trilha.wav"), "-i", str(som / "sfx.wav")]
        fc = (f"[1:a]{F},asplit=2[v][vk];[2:a]{F},volume={G_TRILHA}[m];"
              f"[m][vk]sidechaincompress=threshold=0.02:ratio=5:attack=40:release=700:makeup=1[md];"
              f"[3:a]{F},volume={G_SFX}[sx];"
              f"[v][md][sx]amix=inputs=3:duration=first:normalize=0,alimiter=limit=0.93:level=false[a]")
    else:
        ins += ["-i", str(som / "sfx.wav")]
        fc = f"[1:a]{F}[v];[2:a]{F},volume={G_SFX}[sx];[v][sx]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.93:level=false[a]"
    subprocess.run(["ffmpeg", "-v", "error", "-y", *ins, "-filter_complex", fc, "-map", "0:v", "-map", "[a]", "-c:v", "copy",
                    "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-shortest", "-movflags", "+faststart", str(out)], check=True)
    print("FINAL (com som tech):", out)


def cfg_do_visual(proj):
    sys.path.insert(0, str(Path(__file__).resolve().parent))
    sys.path.insert(0, str(Path(proj) / "roteiro"))
    import importlib
    vis = importlib.import_module("visual")
    return vis, getattr(vis, "SOM", {})


if __name__ == "__main__":
    proj = Path(sys.argv[1]).resolve()
    vis, cfg = cfg_do_visual(proj)
    if cfg is None:
        sys.exit("SOM = None no visual.py: vídeo sem som")
    gerar(proj, cfg)
    if "--so-som" not in sys.argv:
        mixar(proj, proj / "final" / getattr(vis, "ARQUIVO_FINAL", "video_final.mp4"))
