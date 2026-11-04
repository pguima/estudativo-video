"""Gera a narração em inglês (Zephyr, en-US) em duas partes: parte 1 = cenas 01–11, parte 2 = cenas 12–21.
python audio_en/gerar_voz.py <take>  → audio_en/<take>/parte_N.wav + .txt"""
import sys, re, json, time, base64, wave, urllib.request, urllib.error, importlib.util
from pathlib import Path
D = Path(__file__).parent
s = importlib.util.spec_from_file_location("c", D.parent / "roteiro" / "cenas_en.py")
m = importlib.util.module_from_spec(s); s.loader.exec_module(m)
limpo = lambda t: re.sub(r"\s+", " ", re.sub(r"\{[^}]*\}|\[p=[\d.]+\]", "", t).replace("*", "")).strip()  # noqa: E731
take = D / sys.argv[1]
take.mkdir(exist_ok=True)
partes = {1: [x for x in m.SCENES if int(x["id"]) <= 11], 2: [x for x in m.SCENES if int(x["id"]) > 11]}
for n, cenas in partes.items():
    texto = "\n\n".join(limpo(x["text"]) for x in cenas)
    (take / f"parte_{n}.txt").write_text(texto, encoding="utf-8")
    body = json.dumps(dict(text=texto, language="en-US", voiceName=m.VOZ["voiceName"], tags=m.VOZ["tags"],
                           customPrompt=m.VOZ["prompt"], speed=1.0)).encode()
    req = urllib.request.Request("http://localhost:3000/api/tts/generate", data=body, headers={"Content-Type": "application/json"})
    for tent in range(8):
        try:
            r = json.loads(urllib.request.urlopen(req, timeout=1200).read())
            if "lite" in (r.get("modelUsed") or "") and tent < 7:
                print(n, "veio", r.get("modelUsed"), "- esperando", flush=True); time.sleep(90); continue
            break
        except Exception as e:
            print(n, "erro", e, flush=True); time.sleep(90)
    raw = base64.b64decode(r["audioBase64"]); mime = r.get("mimeType", "")
    dst = take / f"parte_{n}.wav"
    if raw[:4] == b"RIFF": dst.write_bytes(raw)
    else:
        rate = int(re.search(r"rate=(\d+)", mime).group(1)) if "rate=" in mime else 24000
        with wave.open(str(dst), "wb") as w: w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate); w.writeframes(raw)
    print(n, r.get("modelUsed"), dst, flush=True)
