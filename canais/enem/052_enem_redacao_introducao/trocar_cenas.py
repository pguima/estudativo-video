"""Regrava só algumas cenas no Gemini e emenda no parte_N.wav existente.
Uso: trocar_cenas.py <proj> <id> [id ...]
Usa analise/voz.json (transcrição atual) + audio/nova_voz/parte_N.txt (texto antigo) para achar o trecho de cada cena;
corta no meio dos silêncios entre cenas. Backup: parte_N.wav.antes_midia.bak / parte_N.txt.antes_midia.bak."""
import sys, re, json, time, base64, difflib, io, wave, urllib.request, urllib.error, shutil
from pathlib import Path
import numpy as np
sys.path.insert(0, "/root/work/estudativo-video/_ferramentas")
import idioma

proj = Path(sys.argv[1]); ids = sys.argv[2:]
m = idioma.cenas(proj, "pt")
limpo = lambda t: re.sub(r"\s+", " ", re.sub(r"\{[^}]*\}|\[p=[\d.]+\]", "", t).replace("*", "")).strip()
nv = proj / "audio" / "nova_voz"
voz = json.load(open(proj / "analise" / "voz.json"))
n1 = len((nv / "parte_1.txt").read_text().split("\n\n"))
SC = m.SCENES
tok = lambda s: [w for w in (re.sub(r"[^\wà-ú]", "", x.lower()) for x in s.split()) if w]


def tts(texto):
    v = getattr(m, "VOZ", {})
    body = json.dumps(dict(text=texto, language="pt-BR", voiceName="Neno", tags=v.get("tags", ["alegre"]), accent="neutro",
                           customPrompt=v.get("prompt", ""), speed=1.0)).encode()
    req = urllib.request.Request("http://localhost:3000/api/tts/generate", data=body, headers={"Content-Type": "application/json"})
    for tent in range(6):
        try:
            r = json.loads(urllib.request.urlopen(req, timeout=900).read())
            if "lite" in (r.get("modelUsed") or "") and tent < 5:
                print("  veio lite, de novo", flush=True); time.sleep(20); continue
            break
        except urllib.error.HTTPError as e:
            print("  HTTP", e.code, flush=True); time.sleep(20)
    raw = base64.b64decode(r["audioBase64"])
    if raw[:4] == b"RIFF":
        with wave.open(io.BytesIO(raw)) as w:
            assert w.getframerate() == 24000
            raw = w.readframes(w.getnframes())
    print("  modelo:", r.get("modelUsed"), flush=True)
    return np.frombuffer(raw, np.int16).astype(np.float32)


def trim(a, thr=0.02):
    env = np.abs(a) / 32768
    idx = np.where(env > thr)[0]
    return a[max(0, idx[0] - 240): idx[-1] + 480]


for parte in (1, 2):
    alvo = [i for i, sc in enumerate(SC) if sc["id"] in ids and (i < n1) == (parte == 1)]
    if not alvo:
        continue
    off = 0 if parte == 1 else n1
    txt_p = nv / f"parte_{parte}.txt"; wav_p = nv / f"parte_{parte}.wav"
    paras = txt_p.read_text().split("\n\n")
    with wave.open(str(wav_p)) as w:
        audio = np.frombuffer(w.readframes(w.getnframes()), np.int16).astype(np.float32)
    SR = 24000; dur = len(audio) / SR
    ws = voz[parte - 1]["words"]
    wt = tok(" ".join(x["w"] for x in ws))
    # cada palavra do whisper pode virar >1 token; refaz lista token->palavra
    w_of = [j for j, x in enumerate(ws) for _ in tok(x["w"])]
    pt, p_of = [], []
    for k, p in enumerate(paras):
        t = tok(p); pt += t; p_of += [k] * len(t)
    sm = difflib.SequenceMatcher(None, pt, wt, autojunk=False)
    mp = {}
    for b in sm.get_matching_blocks():
        for d in range(b.size):
            mp[b.a + d] = w_of[b.b + d]
    rng = {}
    for k in range(len(paras)):
        js = [mp[i] for i in range(len(pt)) if p_of[i] == k and i in mp]
        rng[k] = (ws[js[0]]["s"], ws[js[-1]]["e"]) if js else None
    novos = []
    for i in alvo:
        k = i - off
        s, e = rng[k]
        prev_e = rng[k - 1][1] if k > 0 else 0.0
        next_s = rng[k + 1][0] if k + 1 < len(paras) else dur
        c1 = (prev_e + s) / 2 if k > 0 else 0.0
        c2 = (e + next_s) / 2 if k + 1 < len(paras) else dur
        lead, tail = s - c1, next_s - c2 if k + 1 < len(paras) else 0.6
        txt = limpo(SC[i]["text"])
        print(f"cena {SC[i]['id']} (parte {parte}): {c1:.2f}–{c2:.2f}s", flush=True)
        clip = trim(tts(txt))
        old = audio[int(c1 * SR): int(c2 * SR)]
        r_old = np.sqrt(np.mean(old[np.abs(old) > 300] ** 2)); r_new = np.sqrt(np.mean(clip[np.abs(clip) > 300] ** 2))
        clip = clip * (r_old / r_new)
        seg = np.concatenate([np.zeros(int(min(lead, 0.5) * SR)), clip, np.zeros(int(min(e and (c2 - e), 0.6) * SR))])
        novos.append((c1, c2, seg)); paras[k] = txt
    for c1, c2, seg in sorted(novos, reverse=True):
        audio = np.concatenate([audio[: int(c1 * SR)], seg, audio[int(c2 * SR):]])
    for f in (wav_p, txt_p):
        bk = f.with_name(f.name + ".antes_midia.bak")
        if not bk.exists():
            shutil.copy(f, bk)
    with wave.open(str(wav_p), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(SR)
        w.writeframes(np.clip(audio, -32768, 32767).astype(np.int16).tobytes())
    txt_p.write_text("\n\n".join(paras), encoding="utf-8")
    print(f"parte {parte}: {dur:.1f}s → {len(audio) / SR:.1f}s", flush=True)
