import sys, json, subprocess, numpy as np
from faster_whisper import WhisperModel
src, out = sys.argv[1], sys.argv[2]
raw = subprocess.run(["ffmpeg","-v","error","-i",src,"-ac","1","-ar","16000","-f","s16le","-"],capture_output=True).stdout
audio = np.frombuffer(raw, np.int16).astype(np.float32)/32768
m = WhisperModel("small", device="cpu", compute_type="int8")
segs, info = m.transcribe(audio, vad_filter=True, word_timestamps=False)
res = [{"start": round(s.start,2), "end": round(s.end,2), "text": s.text.strip()} for s in segs]
json.dump({"lang": info.language, "segments": res}, open(out,"w",encoding="utf-8"), ensure_ascii=False, indent=1)
print(info.language, len(res))
