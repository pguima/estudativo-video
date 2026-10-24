"""Gera a narração (edge-tts) de um projeto e os tempos de cada palavra/cue.

Uso: python narracao.py <pasta_do_projeto> [--lang en]   (en: roteiro/cenas_en.py → audio_en/, voz americana)
Lê   <proj>/roteiro/cenas.py
Gera <proj>/audio/cenas/*.wav, <proj>/audio/narracao.wav, <proj>/audio/tempos.json
"""
import asyncio, hashlib, json, re, subprocess, sys, unicodedata
from pathlib import Path
import numpy as np
import edge_tts
import idioma

VOZ = "pt-BR-AntonioNeural"
RATE = "-9%"
PITCH = "-12Hz"
VOZES = {"en": ("en-US-AndrewNeural", "-4%", "-6Hz")}  # outros idiomas: (voz, rate, pitch)
SR = 48000
PAUSA_ENTRE_CENAS = 0.75
PAUSA_INICIO = 0.6

TOKEN_RE = re.compile(r"\{(\w+)\}|\[p=([\d.]+)\]|(\S+)")


def norm(w):
    w = unicodedata.normalize("NFKD", w.lower())
    w = "".join(c for c in w if not unicodedata.combining(c))
    return re.sub(r"[^a-z0-9]", "", w)


def parse(text, pron):
    """-> lista de chunks; cada chunk = {pause_before, tokens:[{disp,bold,tts,cues}] , trailing_cues}"""
    chunks = [dict(pause_before=0.0, tokens=[], trailing_cues=[])]
    pending = []
    bold = False
    for m in TOKEN_RE.finditer(text):
        cue, pause, word = m.groups()
        if cue:
            pending.append(cue)
        elif pause:
            chunks[-1]["trailing_cues"] += pending
            pending = []
            chunks.append(dict(pause_before=float(pause), tokens=[], trailing_cues=[]))
        else:
            start_b = word.startswith("*")
            w = word.lstrip("*")
            end_b = w.rstrip(".,:;!?…\"'").endswith("*")
            w = w.replace("*", "")
            if start_b:
                bold = True
            core = re.sub(r"^[^\wÀ-ÿ]+|[^\wÀ-ÿ]+$", "", w)
            tts = w.replace(core, pron[core]) if core in pron else w
            chunks[-1]["tokens"].append(dict(disp=w, bold=bold, tts=tts, cues=pending))
            pending = []
            if end_b:
                bold = False
    chunks[-1]["trailing_cues"] += pending
    return [c for c in chunks if c["tokens"] or c["trailing_cues"] or c["pause_before"]]


async def tts(text, out_mp3):
    c = edge_tts.Communicate(text, VOZ, rate=RATE, pitch=PITCH, boundary="WordBoundary")
    words = []
    with open(out_mp3, "wb") as f:
        async for ch in c.stream():
            if ch["type"] == "audio":
                f.write(ch["data"])
            elif ch["type"] == "WordBoundary":
                words.append((ch["offset"] / 1e7, (ch["offset"] + ch["duration"]) / 1e7, ch["text"]))
    return words


def decode(path):
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(path), "-ac", "1", "-ar", str(SR), "-f", "f32le", "-"],
                         capture_output=True, check=True).stdout
    return np.frombuffer(raw, np.float32)


def trim(a, thr=0.004):
    idx = np.where(np.abs(a) > thr)[0]
    if len(idx) == 0:
        return a, 0.0
    s = max(0, idx[0] - int(0.02 * SR))
    e = min(len(a), idx[-1] + int(0.06 * SR))
    return a[s:e], s / SR


def align(tokens, words):
    """Atribui a cada token o tempo (início, fim) da(s) palavra(s) TTS correspondentes."""
    ptr = 0
    for t in tokens:
        parts = [norm(p) for p in t["tts"].split() if norm(p)]
        t["t0"] = t["t1"] = None
        for p in parts:
            for j in range(ptr, min(ptr + 4, len(words))):
                wn = norm(words[j][2])
                if wn and (wn == p or wn.startswith(p) or p.startswith(wn)):
                    if t["t0"] is None:
                        t["t0"] = words[j][0]
                    t["t1"] = words[j][1]
                    ptr = j + 1
                    break
    # interpola faltantes
    known = [i for i, t in enumerate(tokens) if t["t0"] is not None]
    for i, t in enumerate(tokens):
        if t["t0"] is None:
            prev = max([k for k in known if k < i], default=None)
            nxt = min([k for k in known if k > i], default=None)
            if prev is not None and nxt is not None:
                a, b = tokens[prev]["t1"], tokens[nxt]["t0"]
                f = (i - prev) / (nxt - prev)
                t["t0"] = a + (b - a) * f
            elif prev is not None:
                t["t0"] = tokens[prev]["t1"] + 0.1 * (i - prev)
            else:
                t["t0"] = words[0][0] if words else 0.0
            t["t1"] = t["t0"] + 0.25


async def main(proj):
    proj = Path(proj)
    P = idioma.pastas(proj)
    mod = idioma.cenas(proj)
    outdir = P.audio / "cenas"; outdir.mkdir(parents=True, exist_ok=True)
    cache = P.audio / "cache"; cache.mkdir(exist_ok=True)

    full = [np.zeros(int(PAUSA_INICIO * SR), np.float32)]
    cursor = PAUSA_INICIO
    result = []
    for sc in mod.SCENES:
        chunks = parse(sc["text"], getattr(mod, "PRONUNCIA", {}))
        sc_audio = []
        t = 0.0
        tokens_out, cues = [], {}
        for ci, ch in enumerate(chunks):
            if ch["pause_before"]:
                sc_audio.append(np.zeros(int(ch["pause_before"] * SR), np.float32)); t += ch["pause_before"]
            if ch["tokens"]:
                text = " ".join(tk["tts"] for tk in ch["tokens"])
                key = re.sub(r"[^\w]+", "_", norm(text))[:60] + "_" + hashlib.md5(f"{text}|{VOZ}|{RATE}|{PITCH}".encode()).hexdigest()[:10]
                mp3 = cache / f"{sc['id']}_{ci}_{key}.mp3"
                wj = mp3.with_suffix(".json")
                if mp3.exists() and wj.exists():
                    words = json.loads(wj.read_text(encoding="utf-8"))
                else:
                    words = await tts(text, mp3)
                    wj.write_text(json.dumps(words, ensure_ascii=False), encoding="utf-8")
                a, off = trim(decode(mp3))
                words = [(w0 - off, w1 - off, s) for w0, w1, s in words]
                align(ch["tokens"], words)
                for tk in ch["tokens"]:
                    tk["t0"] += t; tk["t1"] += t
                    for c in tk["cues"]:
                        cues[c] = tk["t0"]
                    tokens_out.append(dict(disp=tk["disp"], bold=tk["bold"], t0=round(tk["t0"], 3), t1=round(tk["t1"], 3)))
                sc_audio.append(a); t += len(a) / SR
            for c in ch["trailing_cues"]:
                cues[c] = t
        tail = PAUSA_ENTRE_CENAS
        sc_audio.append(np.zeros(int(tail * SR), np.float32)); t += tail
        a = np.concatenate(sc_audio)
        dur = len(a) / SR
        full.append(a)
        result.append(dict(id=sc["id"], block=sc["block"], start=round(cursor, 3), dur=round(dur, 3),
                           tokens=tokens_out, cues={k: round(v, 3) for k, v in cues.items()}))
        print(f"cena {sc['id']:>3} {sc['block']:<10} {dur:6.2f}s  cues={list(cues)}")
        cursor += dur
    audio = np.concatenate(full)
    raw = P.audio / "narracao_bruta.f32"
    audio.astype(np.float32).tofile(raw)
    # tratamento: mais grave/encorpada, compressão suave, loudness de YouTube
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", str(raw),
                    "-af", "bass=g=4:f=110,equalizer=f=250:t=q:w=1:g=1,equalizer=f=3200:t=q:w=1:g=1.5,"
                           "acompressor=threshold=-20dB:ratio=2.5:attack=8:release=120,"
                           "aecho=0.8:0.85:28:0.06,loudnorm=I=-16:TP=-1.5:LRA=9",
                    "-ar", str(SR), str(P.audio / "narracao.wav")], check=True)
    raw.unlink()
    (P.audio / "tempos.json").write_text(json.dumps(dict(total=round(cursor, 3), scenes=result),
                                                          ensure_ascii=False, indent=1), encoding="utf-8")
    print(f"TOTAL {cursor/60:.2f} min")


if __name__ == "__main__":
    lang, args = idioma.pega_lang(sys.argv[1:])
    idioma.definir(lang)
    if lang in VOZES:
        VOZ, RATE, PITCH = VOZES[lang]
    asyncio.run(main(args[0]))
