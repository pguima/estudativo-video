"""Preenche (ou refaz) duração e tempos dos capítulos em youtube/publicacao.md a partir de audio/tempos.json.
Uso: python tempos_publicacao.py <pasta_aula> [...]   (rode de qualquer lugar)
Capítulo k = início do k-ésimo bloco (o 1º vira 0:00). Se o número de capítulos não bater com o de blocos,
avisa e não mexe: ligue cada capítulo à cena certa à mão."""
import json, re, sys, pathlib
def mmss(t): t = int(round(t)); return f"{t//60}:{t%60:02d}"
CAP = re.compile(r'^(\[TEMPO\]|\d+:\d\d) ')
for i in sys.argv[1:]:
    A = pathlib.Path(i); d = json.load(open(A/'audio/tempos.json', encoding='utf8'))
    starts, seen = [], set()
    for s in d['scenes']:
        if s['block'] not in seen: seen.add(s['block']); starts.append(s['start'])
    starts[0] = 0
    P = A/'youtube/publicacao.md'; L = P.read_text(encoding='utf8').split('\n')
    try: c0 = next(k for k, l in enumerate(L) if 'Capítulos' in l)
    except StopIteration: print(i, 'sem seção de capítulos'); continue
    idx = []
    for k in range(c0+1, len(L)):
        if CAP.match(L[k]): idx.append(k)
        elif idx: break
    if len(idx) != len(starts): print(i, 'NÃO BATE: capítulos', len(idx), 'blocos', len(starts)); continue
    for k, t in zip(idx, starts): L[k] = CAP.sub(mmss(t) + ' ', L[k], 1)
    txt = '\n'.join(L).replace('[DURAÇÃO]', mmss(d['total']))
    txt = re.sub(r'(\*\*Arquivo:\*\*[^\n]*?· )\d+:\d\d( ·)', lambda m: m.group(1)+mmss(d['total'])+m.group(2), txt, count=1)
    P.write_text(txt, encoding='utf8'); print(i, mmss(d['total']), 'ok')
