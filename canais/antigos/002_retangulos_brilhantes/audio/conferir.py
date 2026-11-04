"""Transcreve as partes de um take com Whisper e compara com o roteiro.
python audio/conferir.py <take> [modelo]  → <take>/parte_N.wav.words.json ([palavra, início, fim]) + diferenças"""
import sys, json, re, difflib, subprocess, importlib.util
from pathlib import Path
import numpy as np
from faster_whisper import WhisperModel
D = Path(__file__).parent
take = D / sys.argv[1]
m = WhisperModel(sys.argv[2] if len(sys.argv) > 2 else "small", device="cpu", compute_type="int8")
norm = lambda s: re.sub(r"[^\w ]", " ", s.lower()).split()  # noqa: E731
for n in (1, 2):
    src = take / f"parte_{n}.wav"
    raw = subprocess.run(["ffmpeg", "-v", "error", "-i", str(src), "-ac", "1", "-ar", "16000", "-f", "s16le", "-"], capture_output=True).stdout
    a = np.frombuffer(raw, np.int16).astype(np.float32) / 32768
    segs, _ = m.transcribe(a, language="pt", word_timestamps=True, vad_filter=False,
                           initial_prompt=(take / f"parte_{n}.txt").read_text()[:400])
    words = [[w.word.strip(), round(w.start, 3), round(w.end, 3)] for sg in segs for w in sg.words]
    json.dump(words, open(str(src) + ".words.json", "w"), ensure_ascii=False)
    exp = norm((take / f"parte_{n}.txt").read_text())
    got = [x for w in words for x in norm(w[0])]
    sm = difflib.SequenceMatcher(None, exp, got, autojunk=False)
    print(f"== parte {n}: ratio {sm.ratio():.3f}")
    for op, a1, a2, b1, b2 in sm.get_opcodes():
        if op != "equal":
            t0 = words[min(b1, len(words) - 1)][1] if words else 0
            print(f"  {op:7s} {t0:6.1f}s  roteiro: {' '.join(exp[a1:a2])!r:45s} ouvido: {' '.join(got[b1:b2])!r}")
