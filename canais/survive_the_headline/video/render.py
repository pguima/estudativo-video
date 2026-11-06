"""Renderiza um episódio de Survive the Headline, plano por plano.

    py video/render.py ep01-ai-bubble --check            valida o episódio inteiro, sem imagem
    py video/render.py ep01-ai-bubble --stills           um quadro de cada plano + folhas de contato
    py video/render.py ep01-ai-bubble --jobs 3           vídeo completo, sem áudio
    py video/render.py ep01-ai-bubble --only a,b --jobs 2   refaz só esses planos (id) e remonta

Cada plano vira um mp4 em output/seg/. Se o processo cair, basta rodar de novo:
os planos prontos são pulados.
"""
import argparse, asyncio, json, math, os, subprocess, sys, time
from pathlib import Path
from playwright.async_api import async_playwright

ROOT = Path(__file__).resolve().parent.parent
FPS = 30


def player_url(ep, caps=True):
    return (ROOT / 'video' / 'player.html').as_uri() + f'?ep={ep}&caps={1 if caps else 0}'


async def open_page(browser, ep, caps):
    page = await browser.new_page(viewport={'width': 1920, 'height': 1080})
    errors = []
    page.on('pageerror', lambda e: errors.append(str(e)))
    page.on('console', lambda m: errors.append(m.text) if m.type == 'error' else None)
    await page.goto(player_url(ep, caps))
    try:
        await page.wait_for_function('window.playerReady', timeout=60000)
    except Exception:
        raise SystemExit('player não iniciou: ' + ' | '.join(errors))
    return page, errors


async def run_check(ep):
    async with async_playwright() as p:
        b = await p.chromium.launch()
        page, errors = await open_page(b, ep, True)
        info = await page.evaluate('Player.info()')
        bad = 0
        for s in info:
            r = await page.evaluate("""async i => { try { const {dur} = await Player.prepare(i);
                const n = Math.ceil(dur * 30); for (let f = 0; f < n; f += 15) Player.frame(f / 30);
                return null; } catch (e) { return String(e); } }""", s['i'])
            if r:
                bad += 1
                print(f"ERRO {s['id']}: {r}")
        total = info[-1]['start'] + info[-1]['dur']
        print(f"{len(info)} planos, {total/60:.1f} min, {bad} com erro, {len(errors)} erros de página")
        for e in errors[:5]:
            print('  ', e)
        await b.close()
        return info, bad


def contact_sheets(d, width=640, height=360, cols=4, rows=4):
    from PIL import Image
    files = sorted(d.glob('[0-9]*.jpg'))
    per = cols * rows
    for p in range(0, len(files), per):
        sheet = Image.new('RGB', (width * cols, height * rows))
        for i, f in enumerate(files[p:p + per]):
            sheet.paste(Image.open(f).resize((width, height)), ((i % cols) * width, (i // cols) * height))
        sheet.save(d / f'sheet_{p // per:02d}.png')


async def run_stills(ep, out, only):
    d = out / 'stills'
    d.mkdir(parents=True, exist_ok=True)
    for f in d.glob('*.jpg'):
        f.unlink()
    async with async_playwright() as p:
        b = await p.chromium.launch()
        page, errors = await open_page(b, ep, True)
        info = await page.evaluate('Player.info()')
        for s in info:
            if only and s['id'] not in only:
                continue
            await page.evaluate("""async i => { const {dur} = await Player.prepare(i);
                const end = dur * 0.72; for (let t = 0; t <= end; t += 1/15) Player.frame(t); Player.frame(end); }""", s['i'])
            await page.screenshot(path=str(d / f"{s['i']:03d}_{s['id']}.jpg"), type='jpeg', quality=85)
        await b.close()
        if errors:
            print('erros:', errors[:5])
    if not only:
        contact_sheets(d)
    print('stills em', d)


STALL = 120      # segundos sem progresso antes de desistir do quadro
TENTATIVAS = 3
RECICLAR = 10    # planos por navegador, para a memória não crescer


def log(msg):
    print(time.strftime('%H:%M:%S'), msg, flush=True)


async def render_shot(page, s, tmp):
    dur = await asyncio.wait_for(page.evaluate('async i => (await Player.prepare(i)).dur', s['i']), STALL)
    frames = int(round(dur * FPS))
    ff = subprocess.Popen(['ffmpeg', '-y', '-loglevel', 'error', '-threads', '1', '-f', 'image2pipe', '-framerate', str(FPS), '-c:v', 'mjpeg', '-i', '-',
                           '-c:v', 'libx264', '-preset', 'veryfast', '-crf', '18', '-threads', '2', '-pix_fmt', 'yuv420p', '-r', str(FPS), '-an', str(tmp)],
                          stdin=subprocess.PIPE)
    try:
        for f in range(frames):
            await asyncio.wait_for(page.evaluate('t => Player.frame(t)', f / FPS), STALL)
            shot = await asyncio.wait_for(page.screenshot(type='jpeg', quality=94), STALL)
            # numa thread: um pipe cheio não pode parar os outros workers
            await asyncio.wait_for(asyncio.to_thread(ff.stdin.write, shot), STALL)
        await asyncio.wait_for(asyncio.to_thread(ff.stdin.close), STALL)
        if await asyncio.wait_for(asyncio.to_thread(ff.wait), STALL) != 0:
            raise RuntimeError('ffmpeg falhou')
    except BaseException:
        ff.kill()
        raise
    return frames


async def close_browser(b):
    try:
        await asyncio.wait_for(b.close(), 20)
    except Exception:
        pass


async def worker(n, ep, queue, seg, caps, done, total, t0):
    async with async_playwright() as p:
        b, page, errors, usados = None, None, [], 0
        while True:
            try:
                s = queue.get_nowait()
            except asyncio.QueueEmpty:
                break
            target = seg / f"{s['i']:03d}.mp4"
            tmp = seg / f"{s['i']:03d}.tmp.mp4"
            for tentativa in range(1, TENTATIVAS + 1):
                try:
                    if b is None or usados >= RECICLAR:
                        if b:
                            await close_browser(b)
                        b = await asyncio.wait_for(p.chromium.launch(), STALL)
                        page, errors = await asyncio.wait_for(open_page(b, ep, caps), STALL)
                        usados = 0
                    frames = await render_shot(page, s, tmp)
                    tmp.replace(target)
                    usados += 1
                    break
                except Exception as e:
                    log(f"[{n}] {s['id']} tentativa {tentativa} falhou: {type(e).__name__}: {str(e)[:160]}")
                    if b:
                        await close_browser(b)
                    b = None
            else:
                log(f"[{n}] desistindo em {s['id']}; rode de novo para retomar")
                os._exit(3)
            done[0] += frames
            el = time.time() - t0
            left = (total - done[0]) / max(done[0] / el, 0.1)
            log(f"[{n}] {s['id']} ok · {done[0]}/{total} quadros · faltam ~{left/60:.0f} min")
        if b:
            await close_browser(b)
        if errors:
            log(f'erros: {errors[:5]}')


async def run_full(ep, out, jobs, caps, only):
    seg = out / 'seg'
    seg.mkdir(parents=True, exist_ok=True)
    info, bad = await run_check(ep)
    if bad:
        raise SystemExit('corrija os erros antes de renderizar')
    (out / 'planos.json').write_text(json.dumps(info, ensure_ascii=False, indent=1), encoding='utf8')
    for s in info:
        if only and s['id'] in only:
            (seg / f"{s['i']:03d}.mp4").unlink(missing_ok=True)
    pending = [s for s in info if not (seg / f"{s['i']:03d}.mp4").exists()]
    q = asyncio.Queue()
    for s in pending:
        q.put_nowait(s)
    total = sum(int(round(s['dur'] * FPS)) for s in pending)
    print(f'{len(pending)} planos, {total} quadros', flush=True)
    t0 = time.time()
    await asyncio.gather(*[worker(i, ep, q, seg, caps, DONE, total, t0) for i in range(jobs)])
    lista = out / 'concat.txt'
    lista.write_text(''.join(f"file 'seg/{s['i']:03d}.mp4'\n" for s in info), encoding='utf8')
    final = out / f'{ep}_sem_audio.mp4'
    subprocess.run(['ffmpeg', '-y', '-loglevel', 'error', '-f', 'concat', '-safe', '0', '-i', str(lista), '-c', 'copy', '-movflags', '+faststart', str(final)], check=True)
    print('PRONTO', final, f'{(time.time()-t0)/60:.1f} min', flush=True)


DONE = [0]


def main():
    a = argparse.ArgumentParser()
    a.add_argument('ep')
    a.add_argument('--check', action='store_true')
    a.add_argument('--stills', action='store_true')
    a.add_argument('--jobs', type=int, default=3)
    a.add_argument('--no-caps', action='store_true')
    a.add_argument('--only', default='')
    o = a.parse_args()
    out = ROOT / 'episodes' / o.ep / 'output'
    out.mkdir(parents=True, exist_ok=True)
    only = set(x for x in o.only.split(',') if x)
    if o.check:
        asyncio.run(run_check(o.ep))
    elif o.stills:
        asyncio.run(run_stills(o.ep, out, only))
    else:
        asyncio.run(run_full(o.ep, out, o.jobs, not o.no_caps, only))


if __name__ == '__main__':
    main()
