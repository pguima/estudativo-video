"""Usa uma narração gravada/gerada fora (arquivos de áudio) no lugar do TTS.

Uso: python voz_externa.py <proj> <json_palavras> parte1.wav parte2.wav ...
- json_palavras: saída de transcrever_palavras.py para as mesmas partes (mesma ordem)
- alinha as palavras do roteiro (roteiro/cenas.py) com a transcrição
- insere silêncio onde o roteiro pede pausas longas (animações), e entre blocos
Gera <proj>/audio/narracao.wav e <proj>/audio/tempos.json (substitui os do TTS).
"""
import difflib, importlib.util, json, subprocess, sys
from pathlib import Path
import numpy as np

sys.path.insert(0, str(Path(__file__).parent))
from narracao import parse, norm, SR, decode  # noqa

GAP_PARTES = 0.35       # silêncio entre arquivos
PAUSA_MIN_LONGA = 1.0   # pausas do roteiro >= isso são garantidas no áudio
GAP_BLOCO = 0.9         # respiro mínimo quando muda o bloco visual
PAD_INICIO, PAD_FIM = 0.6, 2.0


NUM = {"0": "zero", "1": "um", "2": "dois", "3": "tres", "4": "quatro", "5": "cinco", "6": "seis", "7": "sete", "8": "oito",
       "9": "nove", "10": "dez", "50": "cinquenta"}


def expand(piece):
    """números do Whisper -> palavras como no roteiro"""
    n = norm(piece)
    if n == "9h30":
        return ["nove", "e", "meia"]
    if n == "50" and "%" in piece:
        return ["cinquenta", "por", "cento"]
    if n in NUM:
        return [NUM[n]]
    return [piece]


def main(proj, wjson, parts):
    proj = Path(proj)
    spec = importlib.util.spec_from_file_location("cenas", proj / "roteiro" / "cenas.py")
    mod = importlib.util.module_from_spec(spec); spec.loader.exec_module(mod)
    trans = json.loads(Path(wjson).read_text(encoding="utf-8"))

    # 1) áudio contínuo + palavras reconhecidas em tempo global
    audio, rec, off = [], [], 0.0
    for k, p in enumerate(parts):
        a = decode(p)
        audio.append(a)
        for w in trans[k]["words"]:
            pieces = [x for piece in w["w"].split() for x in expand(piece)]
            for q, piece in enumerate(pieces):
                if norm(piece):
                    d = (w["e"] - w["s"]) / len(pieces)
                    rec.append(dict(n=norm(piece), s=w["s"] + off + q * d, e=w["s"] + off + (q + 1) * d))
        off += len(a) / SR
        audio.append(np.zeros(int(GAP_PARTES * SR), np.float32)); off += GAP_PARTES
    audio = np.concatenate(audio)

    # alerta: a voz gerada (Gemini/vozgen) às vezes lê um trecho duas vezes
    for k, p in enumerate(trans):
        sents, cur, seen = [], [], {}
        for w in p["words"]:
            cur.append(norm(w["w"]))
            if w["w"].rstrip().endswith((".", "?", "!")):
                sents.append((" ".join(x for x in cur if x), w["s"])); cur = []
        for frase, ts in sents:
            if len(frase.split()) >= 5 and frase in seen:
                print(f"⚠️  ATENÇÃO: frase repetida na parte {k + 1} ({seen[frase]:.1f}s e {ts:.1f}s): '{frase[:60]}'"
                      " — a voz pode ter lido um trecho duas vezes; corte a repetição antes de renderizar.")
            seen.setdefault(frase, ts)

    # 2) tokens do roteiro
    toks = []  # dict(scene, block, disp, bold, cues, trailing, pause_before)
    for sc in mod.SCENES:
        for ci, ch in enumerate(parse(sc["text"], {})):
            first = True
            for tk in ch["tokens"]:
                toks.append(dict(scene=sc["id"], block=sc["block"], disp=tk["disp"], bold=tk["bold"], cues=tk["cues"],
                                 pause_before=ch["pause_before"] if first else 0.0, trailing=[]))
                first = False
            if ch["trailing_cues"]:
                if toks and toks[-1]["scene"] == sc["id"]:
                    toks[-1]["trailing"] += ch["trailing_cues"]
            if not ch["tokens"] and ch["pause_before"] and toks and toks[-1]["scene"] == sc["id"]:
                toks[-1]["pause_after_extra"] = toks[-1].get("pause_after_extra", 0) + ch["pause_before"]
    # pausa antes do token i vira "pausa depois" do token i-1
    for i in range(1, len(toks)):
        toks[i - 1]["pause_after"] = toks[i]["pause_before"] + toks[i - 1].get("pause_after_extra", 0)
    toks[-1]["pause_after"] = toks[-1].get("pause_after_extra", 0)

    # 3) alinhamento (palavra a palavra; tokens com várias palavras usam a primeira/última)
    sw, owner = [], []
    for i, t in enumerate(toks):
        for piece in t["disp"].split():
            if norm(piece):
                sw.append(norm(piece)); owner.append(i)
    sm = difflib.SequenceMatcher(None, sw, [r["n"] for r in rec], autojunk=False)
    for t in toks:
        t["t0"] = t["t1"] = None
    for op, i1, i2, j1, j2 in sm.get_opcodes():
        if op == "delete" or (op == "replace" and (i2 - i1) > 3 * (j2 - j1) + 2):
            continue
        if op == "insert":
            continue
        for k in range(i2 - i1):
            jj = j1 + (k if op == "equal" else int(k * (j2 - j1) / (i2 - i1)))
            t = toks[owner[i1 + k]]; r = rec[jj]
            if t["t0"] is None:
                t["t0"] = r["s"]
            t["t1"] = max(r["e"], t["t1"] or 0)
    matched = sum(t["t0"] is not None for t in toks)
    # interpola não encontrados (ex.: números escritos por extenso)
    known = [i for i, t in enumerate(toks) if t["t0"] is not None]
    for i, t in enumerate(toks):
        if t["t0"] is None:
            pv = max([k for k in known if k < i], default=None)
            nx = min([k for k in known if k > i], default=None)
            a = toks[pv]["t1"] if pv is not None else 0.0
            b = toks[nx]["t0"] if nx is not None else a + 0.4
            f = (i - (pv if pv is not None else -1)) / ((nx if nx is not None else len(toks)) - (pv if pv is not None else -1))
            t["t0"] = a + (b - a) * f
            t["t1"] = t["t0"] + 0.2
    print(f"palavras alinhadas: {matched}/{len(toks)}")

    # 4) silêncios extras (pausas longas do roteiro e troca de bloco)
    inserts = []  # (posição no áudio original, segundos)
    for i in range(len(toks) - 1):
        a, b = toks[i], toks[i + 1]
        gap = b["t0"] - a["t1"]
        want = a["pause_after"] if a["pause_after"] >= PAUSA_MIN_LONGA else 0.0
        if a["block"] != b["block"]:
            want = max(want, GAP_BLOCO)
        if want > 0 and want > gap:
            # corta no meio do silêncio entre as palavras
            inserts.append(((a["t1"] + b["t0"]) / 2, want - max(gap, 0)))
    pieces, last, shift = [np.zeros(int(PAD_INICIO * SR), np.float32)], 0, []
    acc = PAD_INICIO
    for pos, extra in inserts:
        cut = int(pos * SR)
        pieces.append(audio[last:cut]); pieces.append(np.zeros(int(extra * SR), np.float32))
        last = cut
        shift.append((pos, extra))
    pieces.append(audio[last:])
    pieces.append(np.zeros(int(PAD_FIM * SR), np.float32))
    new = np.concatenate(pieces)

    def mp(t):
        return t + PAD_INICIO + sum(e for p, e in shift if p <= t)

    for t in toks:
        t["T0"], t["T1"] = mp(t["t0"]), mp(t["t1"])

    # 5) cenas
    ids = [s["id"] for s in mod.SCENES]
    by = {i: [t for t in toks if t["scene"] == i] for i in ids}
    scenes, prev_end = [], 0.0
    for k, sid in enumerate(ids):
        ts = by[sid]
        start = PAD_INICIO if k == 0 else max(prev_end, ts[0]["T0"] - 0.35)
        if k + 1 < len(ids):
            nxt = by[ids[k + 1]][0]["T0"]
            end = max(ts[-1]["T1"] + 0.1, min(nxt - 0.35, ts[-1]["T1"] + 1.5))
            end = max(end, start + 0.5)
        else:
            end = len(new) / SR
        cues = {}
        for i, t in enumerate(ts):
            for c in t["cues"]:
                cues[c] = round(t["T0"] - start, 3)
            for c in t["trailing"]:
                cues[c] = round(t["T1"] - start, 3)
        scenes.append(dict(id=sid, block=ts[0]["block"], start=round(start, 3), dur=round(end - start, 3),
                           tokens=[dict(disp=t["disp"], bold=t["bold"], t0=round(t["T0"] - start, 3),
                                        t1=round(t["T1"] - start, 3)) for t in ts],
                           cues=cues))
        prev_end = end
    # fecha buracos entre cenas
    for a, b in zip(scenes, scenes[1:]):
        a["dur"] = round(b["start"] - a["start"], 3)
    total = len(new) / SR
    raw = proj / "audio" / "narracao_bruta.f32"
    new.astype(np.float32).tofile(raw)
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "f32le", "-ar", str(SR), "-ac", "1", "-i", str(raw),
                    "-af", "loudnorm=I=-16:TP=-1.5:LRA=11", "-ar", str(SR), str(proj / "audio" / "narracao.wav")], check=True)
    raw.unlink()
    (proj / "audio" / "tempos.json").write_text(json.dumps(dict(total=round(total, 3), scenes=scenes), ensure_ascii=False,
                                                          indent=1), encoding="utf-8")
    print(f"silêncios inseridos: {len(inserts)}  total: {total/60:.2f} min")


if __name__ == "__main__":
    main(sys.argv[1], sys.argv[2], sys.argv[3:])
