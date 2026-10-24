"""Gera a voz no Gemini TTS Studio local (http://localhost:3000/api/tts/generate).
Uso: gerar_voz_local.py <proj> <cena_de_corte> [só_a_parte] [--lang en]  — parte 1 = cenas antes do corte, parte 2 = a partir dele.
--lang en: lê roteiro/cenas_en.py e grava em audio_en/nova_voz (voz em inglês americano)."""
import sys, re, json, time, urllib.error, base64, urllib.request, wave, io
from pathlib import Path
import idioma
lang, args = idioma.pega_lang(sys.argv[1:])
sys.argv = [sys.argv[0]] + args
proj, corte = Path(sys.argv[1]), sys.argv[2]
m = idioma.cenas(proj, lang)
limpo = lambda t: re.sub(r"\s+", " ", re.sub(r"\{[^}]*\}|\[p=[\d.]+\]", "", t).replace("*", "")).strip()
p1 = [limpo(sc["text"]) for sc in m.SCENES if sc["id"] < corte]
p2 = [limpo(sc["text"]) for sc in m.SCENES if sc["id"] >= corte]
out = idioma.pastas(proj, lang).audio / "nova_voz"; out.mkdir(parents=True, exist_ok=True)
so = int(sys.argv[3]) if len(sys.argv) > 3 else 0
for n, partes in ((1, p1), (2, p2)):
    if so and n != so:
        continue
    texto = "\n\n".join(partes)
    (out / f"parte_{n}.txt").write_text(texto, encoding="utf-8")
    voz = getattr(m, "VOZ", {})  # opcional no cenas.py: VOZ = dict(tags=[...], prompt="instrução de estilo")
    body = json.dumps(dict(text=texto, language=idioma.TTS.get(lang, "pt-BR"), voiceName="Neno", tags=voz.get("tags", ["alegre"]), accent="neutro",
                           customPrompt=voz.get("prompt", ""), speed=1.0)).encode()
    req = urllib.request.Request("http://localhost:3000/api/tts/generate", data=body, headers={"Content-Type": "application/json"})
    for tent in range(4):  # o servidor às vezes devolve 502 (erro do Gemini): tenta de novo
        try:
            r = json.loads(urllib.request.urlopen(req, timeout=900).read())
            if "lite" in (r.get("modelUsed") or "") and tent < 3:  # fallback do servidor = voz diferente
                print(f"parte {n}: veio {r.get('modelUsed')}, tentando de novo", flush=True); time.sleep(20); continue
            break
        except urllib.error.HTTPError as e:
            print(f"parte {n}: HTTP {e.code} {e.read()[:300]!r} (tentativa {tent + 1})", flush=True)
            if tent == 3: raise
            time.sleep(20)
    if not r.get("success"):
        print("ERRO parte", n, r); sys.exit(1)
    raw = base64.b64decode(r["audioBase64"])
    mime = r.get("mimeType", "")
    dst = out / f"parte_{n}.wav"
    if raw[:4] == b"RIFF":
        dst.write_bytes(raw)
    else:  # PCM cru (audio/L16;rate=24000)
        rate = int(re.search(r"rate=(\d+)", mime).group(1)) if "rate=" in mime else 24000
        with wave.open(str(dst), "wb") as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate); w.writeframes(raw)
    print(f"parte {n}: {len(texto.split())} palavras · {mime} · {r.get('modelUsed')} → {dst}", flush=True)
