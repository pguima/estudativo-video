"""Gera a narração no Gemini TTS Studio local (http://localhost:3000/api/tts/generate).

    py video/voz.py ep01-ai-bubble --corte ads              narrador em 2 partes + falas
    py video/voz.py ep01-ai-bubble --corte ads --so parte_2 só esse arquivo
    py video/voz.py ep01-ai-bubble --corte ads --so dan-no  só essa fala

Lê os textos de output/planos.json (planos com `who` são falas de personagem e têm voz própria).
Grava em episodes/<ep>/audio/. Arquivo que já existe é pulado. Resposta do modelo lite não é salva:
a voz sai diferente, e o certo é esperar a cota do modelo principal voltar.
"""
import argparse
import base64
import json
import re
import sys
import time
import urllib.error
import urllib.request
import wave
from pathlib import Path

URL = 'http://localhost:3000/api/tts/generate'
ROOT = Path(__file__).resolve().parents[1]

NARRADOR = dict(voiceName='Neno', tags=['dramatica', 'confiante'], customPrompt=(
    'Narrate like the host of a gripping animated documentary: adult male voice, deep and authoritative, '
    'tense and serious, with real suspense in the build-ups and a heavy, quiet weight on the bad news. '
    'Warm and human when talking about the family. Never cheerful, never over the top. Stress the key words '
    'and the numbers. Unhurried pace, with a clear pause between paragraphs. '
    'Read only the text, exactly as written, without adding, skipping or repeating anything.'))
LER = ' Say only this line, exactly as written, and nothing else.'
ELENCO = {
    'dan': dict(voiceName='Fenrir', tags=['confiante'], customPrompt='A working-class American dad in his early forties, a warm, slightly rough voice, stubborn and trying to sound sure of himself.' + LER),
    'mia': dict(voiceName='Kore', tags=['calma'], customPrompt='An American mom in her late thirties, a nurse, gentle and steady, hiding her own worry to comfort her child.' + LER),
    'bea': dict(voiceName='Aoede', tags=['curiosa'], customPrompt='A small eight-year-old American girl, a high, soft, innocent child voice, quietly scared and asking in a small voice.' + LER),
}


def pedir(texto, cfg, dst):
    body = json.dumps(dict(text=texto, language='en-US', accent='neutro', speed=1.0, **cfg)).encode()
    req = urllib.request.Request(URL, data=body, headers={'Content-Type': 'application/json'})
    for tent in range(4):
        try:
            r = json.loads(urllib.request.urlopen(req, timeout=900).read())
            break
        except urllib.error.HTTPError as e:
            print(f'{dst.name}: HTTP {e.code} {e.read()[:300]!r} (tentativa {tent + 1})', flush=True)
            if tent == 3:
                return False
            time.sleep(25)
    if not r.get('success'):
        print('ERRO', dst.name, str(r)[:300], flush=True)
        return False
    if 'lite' in (r.get('modelUsed') or ''):
        print(f"{dst.name}: veio {r['modelUsed']}, nada salvo", flush=True)
        return False
    raw = base64.b64decode(r['audioBase64'])
    if raw[:4] == b'RIFF':
        dst.write_bytes(raw)
    else:
        mime = r.get('mimeType', '')
        rate = int(re.search(r'rate=(\d+)', mime).group(1)) if 'rate=' in mime else 24000
        with wave.open(str(dst), 'wb') as w:
            w.setnchannels(1); w.setsampwidth(2); w.setframerate(rate); w.writeframes(raw)
    print(f"{dst.name}: {len(texto.split())} palavras · {r.get('modelUsed')}", flush=True)
    return True


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument('ep'); ap.add_argument('--corte', required=True); ap.add_argument('--so', default='')
    a = ap.parse_args()
    base = ROOT / 'episodes' / a.ep
    planos = json.loads((base / 'output' / 'planos.json').read_text(encoding='utf8'))
    out = base / 'audio'; out.mkdir(exist_ok=True)
    corte = next(s['i'] for s in planos if s['id'] == a.corte)
    nar = [s for s in planos if s['n'] and not s['who']]
    tarefas = [('parte_1', '\n\n'.join(s['n'] for s in nar if s['i'] < corte), NARRADOR),
               ('parte_2', '\n\n'.join(s['n'] for s in nar if s['i'] >= corte), NARRADOR)]
    tarefas += [(s['id'], s['n'], ELENCO[s['who']]) for s in planos if s['who']]
    falhas = 0
    for nome, texto, cfg in tarefas:
        dst = out / f'{nome}.wav'
        if (a.so and a.so != nome) or (dst.exists() and not a.so):
            continue
        (out / f'{nome}.txt').write_text(texto, encoding='utf8')
        falhas += not pedir(texto, cfg, dst)
    print('falhas:', falhas, flush=True)
    sys.exit(3 if falhas else 0)


main()
