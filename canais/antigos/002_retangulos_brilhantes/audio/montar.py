"""Monta a narração a partir de um take: narracao.wav (parte 1 + 0,9 s + parte 2), tempos.json (cenas e cues casadas
com as palavras do Whisper) e a legenda saida/legenda_pt.srt.
python audio/montar.py <take>   (precisa de <take>/parte_N.wav.words.json, do conferir.py)"""
import json, re, sys, difflib, wave, subprocess, importlib.util
from pathlib import Path
D = Path(__file__).parent
s = importlib.util.spec_from_file_location("c", D.parent / "roteiro" / "cenas.py")
cenas = importlib.util.module_from_spec(s); s.loader.exec_module(cenas)
take = D / sys.argv[1]
norm = lambda s: re.sub(r"[^\w ]", " ", s.lower().replace("’", "'").replace("'", "")).split()  # noqa: E731
GAP = 0.9


def dur(p):
    w = wave.open(str(p)); return w.getnframes() / w.getframerate()


p1, p2 = take / "parte_1.wav", take / "parte_2.wav"
d1 = dur(p1)
words = []
for p, off in ((p1, 0), (p2, d1 + GAP)):
    for w, a, b in json.load(open(str(p) + ".words.json")):
        for x in norm(w): words.append((x, a + off, b + off))
heard = [w[0] for w in words]

# ---- cenas e cues
exp, tag = [], []
for sc in cenas.SCENES:
    txt = re.sub(r"\[p=[\d.]+\]", "", sc["text"]).replace("*", "")
    first, pend = True, None
    for tok in re.split(r"(\{[^}]*\})", txt):
        if tok.startswith("{"):
            pend = tok[1:-1]; continue
        for w in norm(tok):
            t = []
            if first: t.append(("start", sc["id"])); first = False
            if pend: t.append(("cue", sc["id"], pend)); pend = None
            exp.append(w); tag.append(t)
sm = difflib.SequenceMatcher(None, exp, heard, autojunk=False)
m = {}
for a, b, n in sm.get_matching_blocks():
    for k in range(n): m[a + k] = b + k


def tempo(i):
    if i in m: return words[m[i]][1]
    j = i
    while j < len(exp) and j not in m: j += 1
    k = i
    while k >= 0 and k not in m: k -= 1
    if j < len(exp) and k >= 0:
        tj, tk = words[m[j]][1], words[m[k]][2]; return tk + (tj - tk) * (i - k) / (j - k)
    return words[m[j]][1] if j < len(exp) else words[m[k]][2]


ct = {}
for i, ts in enumerate(tag):
    for x in ts:
        if x[0] == "start": ct.setdefault(x[1], {"start": tempo(i), "cues": {}})
        else: ct[x[1]]["cues"][x[2]] = tempo(i)
total = d1 + GAP + dur(p2)
out = []
for k, sc in enumerate(cenas.SCENES):
    c = ct[sc["id"]]; st = max(0, c["start"] - 0.25) if k else 0.0
    out.append(dict(id=sc["id"], start=round(st, 3), cues={q: round(v - st, 3) for q, v in c["cues"].items()}))
for k in range(len(out)):
    out[k]["end"] = out[k + 1]["start"] if k + 1 < len(out) else round(total + 1.0, 3)
json.dump(dict(scenes=out, total=round(total + 1.0, 3), gap_after_parte1=GAP, d1=d1, take=sys.argv[1]),
          open(D / "tempos.json", "w"), indent=1)
for x in out: print(x["id"], f'{x["start"]:7.2f}-{x["end"]:7.2f}', {k: round(v, 1) for k, v in x["cues"].items()})
print("ratio", round(sm.ratio(), 3), "total", round(total, 1))


# ---- narração inteira
sr = wave.open(str(p1)).getframerate()
subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(p1), "-f", "lavfi", "-t", str(GAP), "-i", f"anullsrc=r={sr}:cl=mono",
                "-i", str(p2), "-filter_complex", "[0][1][2]concat=n=3:v=0:a=1", "-ar", str(sr), str(D / "narracao.wav")], check=True)

# ---- legenda
toks, fim_cena = [], set()
for sc in cenas.SCENES:
    txt = re.sub(r"\s+", " ", re.sub(r"\{[^}]*\}|\[p=[\d.]+\]", "", sc["text"]).replace("*", "")).strip()
    toks += txt.split(" "); fim_cena.add(len(toks) - 1)
exp, own = [], []
for i, tk in enumerate(toks):
    for x in norm(tk): exp.append(x); own.append(i)
sm = difflib.SequenceMatcher(None, exp, heard, autojunk=False)
m = {}
for a, b, n in sm.get_matching_blocks():
    for k in range(n): m[a + k] = b + k


def t_ini(j):
    if j in m: return words[m[j]][1]
    k = j
    while k > 0 and k not in m: k -= 1
    return words[m[k]][2] + 0.05 if k in m else 0.0


def t_fim(j):
    if j in m: return words[m[j]][2]
    k = j
    while k > 0 and k not in m: k -= 1
    return words[m[k]][2] + 0.3 * (j - k) if k in m else 0.5


first, last = {}, {}
for j, i in enumerate(own): first.setdefault(i, j); last[i] = j
blocos, cur = [], []
for i, tk in enumerate(toks):
    cur.append(i); n = len(" ".join(toks[x] for x in cur))
    if (re.search(r"[.!?]$", tk) and n > 12) or (tk.endswith(":") and n > 30) or i in fim_cena or n > 70:
        blocos.append(cur); cur = []
if cur: blocos.append(cur)


def quebra(s):
    if len(s) <= 42: return s
    esp = [k for k, ch in enumerate(s) if ch == " "]; k = min(esp, key=lambda x: abs(x - len(s) // 2)); return s[:k] + "\n" + s[k + 1:]


def ts(t):
    ms = int(round(t * 1000)); return f"{ms // 3600000:02d}:{ms // 60000 % 60:02d}:{ms // 1000 % 60:02d},{ms % 1000:03d}"


cues = []
for b in blocos:
    js = [j for i in b if i in first for j in (first[i], last[i])]
    if js: cues.append([t_ini(min(js)), t_fim(max(js)) + 0.3, " ".join(toks[i] for i in b)])
for k in range(len(cues) - 1): cues[k][1] = min(cues[k][1], cues[k + 1][0] - 0.02)
srt = "\n".join(f"{k + 1}\n{ts(a)} --> {ts(z)}\n{quebra(s)}\n" for k, (a, z, s) in enumerate(cues))
(D.parent / "saida").mkdir(exist_ok=True)
(D.parent / "saida" / "legenda_pt.srt").write_text(srt, encoding="utf-8")
print(len(cues), "legendas; curtas:", sum(1 for c in cues if c[1] - c[0] < 0.7), "; invertidas:", sum(1 for c in cues if c[1] <= c[0]))
