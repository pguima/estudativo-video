import sys, json, subprocess, numpy as np
from faster_whisper import WhisperModel
m = WhisperModel("small", device="cpu", compute_type="int8")
out = []
for src in sys.argv[2:]:
    raw = subprocess.run(["ffmpeg","-v","error","-i",src,"-ac","1","-ar","16000","-f","s16le","-"],capture_output=True).stdout
    a = np.frombuffer(raw, np.int16).astype(np.float32)/32768
    segs, _ = m.transcribe(a, language="pt", word_timestamps=True, vad_filter=False)
    words = [dict(w=w.word.strip(), s=round(w.start,3), e=round(w.end,3)) for sg in segs for w in sg.words]
    out.append(dict(file=src, dur=len(a)/16000, words=words))
    print(src, len(words), flush=True)
json.dump(out, open(sys.argv[1],"w",encoding="utf-8"), ensure_ascii=False)
