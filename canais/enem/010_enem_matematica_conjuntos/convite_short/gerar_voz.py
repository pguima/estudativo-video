# Gera a narração do Short-convite no Gemini TTS Studio local (voz Neno, sotaque neutro).
import json, base64, urllib.request
from pathlib import Path
AQUI = Path(__file__).resolve().parent
texto = (AQUI / "narracao.txt").read_text(encoding="utf-8").strip()
prompt = ("Locutor de chamada de canal educativo no YouTube: animado, caloroso, confiante, voz grave, muito expressivo, "
          "ritmo ágil mas claro, com energia de convite. Leia apenas o texto, sem acrescentar nada.")
body = json.dumps(dict(text=texto, language="pt-BR", voiceName="Neno", tags=["alegre", "animada"], accent="neutro",
                       customPrompt=prompt, speed=1.0)).encode()
req = urllib.request.Request("http://localhost:3000/api/tts/generate", data=body, headers={"Content-Type": "application/json"})
r = json.loads(urllib.request.urlopen(req, timeout=600).read())
raw = base64.b64decode(r["audioBase64"])
dst = AQUI / "audio" / "narracao.wav"
if raw[:4] == b"RIFF":
    dst.write_bytes(raw)
else:
    import wave
    with wave.open(str(dst), "wb") as w:
        w.setnchannels(1); w.setsampwidth(2); w.setframerate(24000); w.writeframes(raw)
print(r.get("modelUsed"), r.get("mimeType"), dst)
