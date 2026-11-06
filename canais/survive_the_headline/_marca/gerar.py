"""Imagens do canal Survive the Headline para configurar o YouTube, geradas por arte.html:
- avatar_800.png        foto do perfil (800x800; o YouTube recorta em círculo)
- banner_2560x1440.jpg  banner (só o centro de 1235x338 aparece em todo aparelho)
- banner_guia.png       o banner com as áreas desenhadas (para conferir, não enviar)
- marca_dagua_150.png   marca d'água dos vídeos (150x150, fundo transparente)
- logo_horizontal.png   logo para outros usos (fundo transparente)
Uso: py _marca/gerar.py"""
import asyncio
from pathlib import Path

from PIL import Image
from playwright.async_api import async_playwright

AQUI = Path(__file__).resolve().parent
ARTES = [('avatar', 800, 800, ''), ('marca', 800, 800, ''), ('logo', 1500, 460, ''),
         ('banner', 2560, 1440, ''), ('banner', 2560, 1440, '&guia=1')]


async def main():
    async with async_playwright() as p:
        b = await p.chromium.launch()
        for art, w, h, extra in ARTES:
            pg = await b.new_page(viewport={'width': w, 'height': h})
            pg.on('pageerror', lambda e: print('ERRO', e))
            pg.on('console', lambda m: print(m.text) if m.type == 'error' else None)
            await pg.goto((AQUI / 'arte.html').as_uri() + f'?art={art}{extra}')
            await pg.wait_for_function('window.ok', timeout=60000)
            await pg.wait_for_timeout(800)
            nome = AQUI / f"_{art}{'_guia' if extra else ''}.png"
            await pg.locator('#art').screenshot(path=str(nome), omit_background=True)
            await pg.close()
        await b.close()
    Image.open(AQUI / '_avatar.png').convert('RGB').save(AQUI / 'avatar_800.png', optimize=True)
    Image.open(AQUI / '_marca.png').resize((150, 150), Image.LANCZOS).save(AQUI / 'marca_dagua_150.png', optimize=True)
    Image.open(AQUI / '_logo.png').save(AQUI / 'logo_horizontal.png', optimize=True)
    Image.open(AQUI / '_banner.png').convert('RGB').save(AQUI / 'banner_2560x1440.jpg', quality=92, optimize=True)
    Image.open(AQUI / '_banner_guia.png').convert('RGB').resize((1280, 720), Image.LANCZOS).save(AQUI / 'banner_guia.png', optimize=True)
    for f in AQUI.glob('_*.png'):
        f.unlink()


asyncio.run(main())
