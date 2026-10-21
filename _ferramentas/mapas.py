"""Mapas com dados geográficos reais (Natural Earth) desenhados com skia.

Uso no visual.py:
    import mapas
    mapas.draw_world(c, (x, y, w, h), a, proj="equi")      # "equi" | "mercator" | "peters"
    mapas.draw_world(c, rect, a, proj="mercator", lat=(-60, 84), graticule=True)

Dados em _ferramentas/dados/natural_earth/ (domínio público, naturalearthdata.com).
"""
import json
import math
from functools import lru_cache
from pathlib import Path
import skia
from motor import paint

DADOS = Path(__file__).parent / "dados" / "natural_earth"
SEA = "#DBEAFE"
LAND = "#86C18A"
COAST = "#5FA463"


@lru_cache(None)
def _rings(arquivo):
    """lista de anéis [(lon, lat), ...] de um GeoJSON de polígonos"""
    gj = json.loads((DADOS / arquivo).read_text(encoding="utf-8"))
    out = []
    for f in gj["features"]:
        g = f["geometry"]
        polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
        for poly in polys:
            out.append([tuple(p[:2]) for p in poly[0]])
    return tuple(tuple(r) for r in out)


@lru_cache(None)
def _country_rings(nome):
    gj = json.loads((DADOS / "ne_110m_admin_0_countries.geojson").read_text(encoding="utf-8"))
    for f in gj["features"]:
        p = f["properties"]
        if nome in (p.get("NAME"), p.get("NAME_PT"), p.get("ADMIN")):
            g = f["geometry"]
            polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
            return tuple(tuple(tuple(q[:2]) for q in poly[0]) for poly in polys)
    raise KeyError(nome)


# ---------------- projeções (lon, lat em graus -> x, y abstratos; y cresce para o norte) ----------------
def project(lon, lat, proj):
    if proj == "mercator":
        lat = max(-85.0, min(85.0, lat))
        return math.radians(lon), math.log(math.tan(math.pi / 4 + math.radians(lat) / 2))
    if proj == "peters":  # Gall-Peters (equivalente)
        return math.radians(lon), 2 * math.sin(math.radians(lat))
    return math.radians(lon), math.radians(lat)  # equirretangular


def _fit(rect, proj, lon, lat):
    x, y, w, h = rect
    x0, y0 = project(lon[0], lat[0], proj)
    x1, y1 = project(lon[1], lat[1], proj)
    s = min(w / (x1 - x0), h / (y1 - y0))
    ox = x + (w - (x1 - x0) * s) / 2
    oy = y + (h - (y1 - y0) * s) / 2
    return lambda X, Y: (ox + (X - x0) * s, oy + (y1 - Y) * s)


@lru_cache(64)
def _world_path(rect, proj, lon, lat, arquivo):
    to = _fit(rect, proj, lon, lat)
    path = skia.Path()
    for ring in _rings(arquivo):
        if max(p[1] for p in ring) < lat[0]:
            continue  # Antártida fora do recorte
        pts = [to(*project(lo, max(min(la, lat[1]), lat[0]), proj)) for lo, la in ring]
        path.moveTo(*pts[0])
        for q in pts[1:]:
            path.lineTo(*q)
        path.close()
    return path


def world_frame(rect, proj="equi", lon=(-180, 180), lat=(-58, 84)):
    """retângulo efetivamente ocupado pelo mapa dentro de rect"""
    to = _fit(rect, proj, lon, lat)
    (ax, ay), (bx, by) = to(*project(lon[0], lat[1], proj)), to(*project(lon[1], lat[0], proj))
    return ax, ay, bx - ax, by - ay


def to_xy(rect, lonlat, proj="equi", lon=(-180, 180), lat=(-58, 84)):
    """posição na tela de um ponto (lon, lat) no mapa desenhado em rect"""
    return _fit(rect, proj, lon, lat)(*project(lonlat[0], lonlat[1], proj))


def draw_world(c, rect, a=1.0, proj="equi", lon=(-180, 180), lat=(-58, 84), sea=SEA, land=LAND, coast=COAST,
               graticule=False, grat_step=30, frame=True, arquivo="ne_50m_land.geojson", radius=18):
    if a <= 0:
        return
    rect = tuple(float(v) for v in rect)
    fx, fy, fw, fh = world_frame(rect, proj, lon, lat)
    c.save()
    c.clipRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(fx, fy, fw, fh), radius, radius), True)
    c.drawRect(skia.Rect.MakeXYWH(fx, fy, fw, fh), paint(sea, a))
    if graticule:
        to = _fit(rect, proj, lon, lat)
        pg = paint("#93C5FD", a, stroke=1.5)
        for L in range(-180, 181, grat_step):
            (x0, y0), (x1, y1) = to(*project(L, lat[0], proj)), to(*project(L, lat[1], proj))
            c.drawLine(x0, y0, x1, y1, pg)
        for L in range(-90, 91, grat_step):
            if lat[0] <= L <= lat[1]:
                (x0, y0), (x1, y1) = to(*project(lon[0], L, proj)), to(*project(lon[1], L, proj))
                c.drawLine(x0, y0, x1, y1, pg)
    path = _world_path(rect, proj, tuple(lon), tuple(lat), arquivo)
    c.drawPath(path, paint(land, a))
    c.drawPath(path, paint(coast, a, stroke=1.4))
    c.restore()
    if frame:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(fx, fy, fw, fh), radius, radius), paint("#3A3A3C", a, stroke=3))


@lru_cache(None)
def continent_rings(nome):
    """todos os países de um continente (propriedade CONTINENT do Natural Earth, ex.: 'Africa')"""
    gj = json.loads((DADOS / "ne_110m_admin_0_countries.geojson").read_text(encoding="utf-8"))
    out = []
    for f in gj["features"]:
        if f["properties"].get("CONTINENT") == nome:
            g = f["geometry"]
            polys = g["coordinates"] if g["type"] == "MultiPolygon" else [g["coordinates"]]
            out += [tuple(tuple(q[:2]) for q in poly[0]) for poly in polys]
    return tuple(out)


def draw_country_on(c, nome, rect, a=1.0, fill="#F59E0B", stroke="#B45309", proj="equi", lon=(-180, 180), lat=(-58, 84)):
    """destaca um país por cima de um draw_world com o mesmo rect/proj/lon/lat"""
    if a <= 0:
        return
    to = _fit(tuple(float(v) for v in rect), proj, lon, lat)
    path = skia.Path()
    for r in _country_rings(nome):
        q = [to(*project(lo, la, proj)) for lo, la in r]
        path.moveTo(*q[0])
        for p in q[1:]:
            path.lineTo(*p)
        path.close()
    c.drawPath(path, paint(fill, a))
    c.drawPath(path, paint(stroke, a, stroke=2))


# ---------------- "tamanho real": mover um país pela esfera e reprojetar ----------------
def _xyz(lon, lat):
    l, p = math.radians(lon), math.radians(lat)
    return (math.cos(p) * math.cos(l), math.cos(p) * math.sin(l), math.sin(p))


def _lonlat(v):
    x, y, z = v
    return math.degrees(math.atan2(y, x)), math.degrees(math.asin(max(-1.0, min(1.0, z))))


def moved_rings(nome, alvo, f=1.0):
    """anéis do país girados sobre a esfera para que o centro vá até alvo=(lon, lat); f em [0,1] anima o caminho.
    Reprojetado na Mercator, o país muda de tamanho como no site The True Size."""
    rings = _country_rings(nome)
    vs = [_xyz(lo, la) for r in rings for lo, la in r]
    cx, cy, cz = (sum(v[i] for v in vs) for i in range(3))
    n = math.sqrt(cx * cx + cy * cy + cz * cz)
    c = (cx / n, cy / n, cz / n)
    t = _xyz(*alvo)
    k = (c[1] * t[2] - c[2] * t[1], c[2] * t[0] - c[0] * t[2], c[0] * t[1] - c[1] * t[0])
    kn = math.sqrt(sum(q * q for q in k)) or 1.0
    k = tuple(q / kn for q in k)
    th = math.acos(max(-1.0, min(1.0, sum(c[i] * t[i] for i in range(3))))) * f
    ct, st = math.cos(th), math.sin(th)

    def rot(v):
        kv = sum(k[i] * v[i] for i in range(3))
        kxv = (k[1] * v[2] - k[2] * v[1], k[2] * v[0] - k[0] * v[2], k[0] * v[1] - k[1] * v[0])
        return tuple(v[i] * ct + kxv[i] * st + k[i] * kv * (1 - ct) for i in range(3))
    return [[_lonlat(rot(_xyz(lo, la))) for lo, la in r] for r in rings]


def draw_rings_on(c, rings, rect, a=1.0, fill="#F59E0B", stroke="#B45309", proj="equi", lon=(-180, 180), lat=(-58, 84)):
    if a <= 0:
        return
    to = _fit(tuple(float(v) for v in rect), proj, lon, lat)
    path = skia.Path()
    for r in rings:
        q = [to(*project(lo, la, proj)) for lo, la in r]
        path.moveTo(*q[0])
        for p in q[1:]:
            path.lineTo(*p)
        path.close()
    c.drawPath(path, paint(fill, a))
    c.drawPath(path, paint(stroke, a, stroke=2))


def tissot(c, rect, centro, raio_graus, a=1.0, fill="#E5484D", proj="equi", lon=(-180, 180), lat=(-58, 84), n=72):
    """círculo de mesmo tamanho REAL na Terra, desenhado na projeção (mostra quanto ela estica ali)"""
    if a <= 0:
        return
    to = _fit(tuple(float(v) for v in rect), proj, lon, lat)
    lo0, la0 = math.radians(centro[0]), math.radians(centro[1])
    d = math.radians(raio_graus)
    path = skia.Path()
    for i in range(n + 1):
        b = 2 * math.pi * i / n
        la = math.asin(math.sin(la0) * math.cos(d) + math.cos(la0) * math.sin(d) * math.cos(b))
        lo = lo0 + math.atan2(math.sin(b) * math.sin(d) * math.cos(la0), math.cos(d) - math.sin(la0) * math.sin(la))
        x, y = to(*project(math.degrees(lo), math.degrees(la), proj))
        (path.moveTo if i == 0 else path.lineTo)(x, y)
    path.close()
    c.drawPath(path, paint(fill, a * 0.55))
    c.drawPath(path, paint(fill, a, stroke=2.5))


# ---------------- globo (projeção ortográfica: a Terra vista do espaço) ----------------
def globe_xy(lon, lat, cx, cy, r, lon0=0.0, lat0=0.0):
    """(x, y, visível) de um ponto no globo centrado em (lon0, lat0)"""
    l, p, p0 = math.radians(lon - lon0), math.radians(lat), math.radians(lat0)
    x = r * math.cos(p) * math.sin(l)
    y = r * (math.cos(p0) * math.sin(p) - math.sin(p0) * math.cos(p) * math.cos(l))
    vis = math.sin(p0) * math.sin(p) + math.cos(p0) * math.cos(p) * math.cos(l) >= 0
    return cx + x, cy - y, vis


def _globe_poly(pts, cx, cy, r, lon0, lat0, close):
    """pontos do lado de trás são empurrados para a borda do disco (dá contorno aceitável)"""
    path, first = skia.Path(), True
    for lo, la in pts:
        x, y, vis = globe_xy(lo, la, cx, cy, r, lon0, lat0)
        if not vis:
            dx, dy = x - cx, y - cy
            d = math.hypot(dx, dy) or 1.0
            x, y = cx + dx / d * r, cy + dy / d * r
        (path.moveTo if first else path.lineTo)(x, y)
        first = False
    if close:
        path.close()
    return path


def _vec(lon, lat, lon0, lat0):
    """ponto na esfera em coordenadas da câmera: x para a direita, y para cima, z para quem olha"""
    l, p, p0 = math.radians(lon - lon0), math.radians(lat), math.radians(lat0)
    return (math.cos(p) * math.sin(l),
            math.cos(p0) * math.sin(p) - math.sin(p0) * math.cos(p) * math.cos(l),
            math.sin(p0) * math.sin(p) + math.cos(p0) * math.cos(p) * math.cos(l))


def _globe_clip(ring, cx, cy, r, lon0, lat0):
    """recorta um polígono pela metade visível do globo; trechos escondidos viram arcos na borda (horizonte)"""
    V = [_vec(lo, la, lon0, lat0) for lo, la in ring]
    n = len(V)
    vis = [v[2] >= 0 for v in V]
    if not any(vis):
        return None
    scr = lambda v: (cx + r * v[0], cy - r * v[1])
    path = skia.Path()
    if all(vis):
        path.moveTo(*scr(V[0]))
        for v in V[1:]:
            path.lineTo(*scr(v))
        path.close()
        return path

    def horizonte(p, q):
        t = p[2] / (p[2] - q[2])
        x, y = p[0] + (q[0] - p[0]) * t, p[1] + (q[1] - p[1]) * t
        d = math.hypot(x, y) or 1.0
        return x / d, y / d

    s = next(i for i in range(n) if vis[i] and not vis[i - 1])  # começa logo após uma entrada
    path.moveTo(*scr(V[s]))
    saida = None
    for k in range(1, n + 1):
        i, j = (s + k - 1) % n, (s + k) % n
        if vis[i] and vis[j]:
            path.lineTo(*scr(V[j]))
        elif vis[i] and not vis[j]:
            saida = horizonte(V[i], V[j])
            path.lineTo(cx + r * saida[0], cy - r * saida[1])
        elif not vis[i] and vis[j]:
            ent = horizonte(V[j], V[i])
            a0, a1 = math.atan2(saida[1], saida[0]), math.atan2(ent[1], ent[0])
            d = (a1 - a0 + math.pi) % (2 * math.pi) - math.pi  # menor arco ao longo do horizonte
            for m in range(1, max(2, int(abs(d) / 0.05))):
                ang = a0 + d * m / max(2, int(abs(d) / 0.05))
                path.lineTo(cx + r * math.cos(ang), cy - r * math.sin(ang))
            path.lineTo(cx + r * ent[0], cy - r * ent[1])
            path.lineTo(*scr(V[j]))
    path.close()
    return path


def globe_line(c, cx, cy, r, col, a, w, lon0=0.0, lat0=0.0, lat=None, lon=None, n=120):
    """desenha só a parte visível de um paralelo (lat=...) ou de um meridiano (lon=...)"""
    if a <= 0:
        return
    pts = [(lo, lat) for lo in (i * 360 / n - 180 for i in range(n + 1))] if lat is not None else \
          [(lon, la) for la in (i * 180 / n - 90 for i in range(n + 1))]
    pp = paint(col, a, stroke=w, cap_round=True)
    prev = None
    for lo, la in pts:
        x, y, vis = globe_xy(lo, la, cx, cy, r, lon0, lat0)
        if vis and prev is not None:
            c.drawLine(prev[0], prev[1], x, y, pp)
        prev = (x, y) if vis else None


def draw_globe(c, cx, cy, r, a=1.0, lon0=0.0, lat0=15.0, land=LAND, sea=SEA, coast=COAST, grat_lats=(-60, -30, 0, 30, 60),
               grat_lons=tuple(range(-180, 180, 30)), grat_col="#93C5FD", outline="#3A3A3C"):
    if a <= 0:
        return
    c.drawCircle(cx, cy, r, paint(sea, a))
    c.save()
    clip = skia.Path(); clip.addCircle(cx, cy, r)
    c.clipPath(clip, skia.ClipOp.kIntersect, True)
    for ring in _rings("ne_110m_land.geojson"):
        if lat0 > -30 and max(p[1] for p in ring) < -60:
            continue  # Antártida: quase sempre atrás, e o recorte dela no horizonte é instável
        path = _globe_clip(ring, cx, cy, r, lon0, lat0)
        if path is None:
            continue
        c.drawPath(path, paint(land, a))
        c.drawPath(path, paint(coast, a, stroke=1.2))
    c.restore()
    for L in grat_lats:
        globe_line(c, cx, cy, r, grat_col, a * 0.9, 1.6, lon0, lat0, lat=L)
    for L in grat_lons:
        globe_line(c, cx, cy, r, grat_col, a * 0.9, 1.6, lon0, lat0, lon=L)
    c.drawCircle(cx, cy, r, paint(outline, a, stroke=4))


def draw_country(c, nome, rect, a=1.0, fill=LAND, stroke=COAST, proj="equi", pad=0.06):
    """um país sozinho, ajustado ao retângulo (ex.: 'Brazil', 'Greenland')"""
    if a <= 0:
        return
    rings = _country_rings(nome)
    pts = [project(lo, la, proj) for r in rings for lo, la in r]
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    x, y, w, h = rect
    sx, sy = (max(xs) - min(xs)), (max(ys) - min(ys))
    s = min(w * (1 - 2 * pad) / sx, h * (1 - 2 * pad) / sy)
    ox, oy = x + (w - sx * s) / 2, y + (h - sy * s) / 2
    path = skia.Path()
    for r in rings:
        q = [(ox + (project(lo, la, proj)[0] - min(xs)) * s, oy + (max(ys) - project(lo, la, proj)[1]) * s) for lo, la in r]
        path.moveTo(*q[0])
        for p in q[1:]:
            path.lineTo(*p)
        path.close()
    c.drawPath(path, paint(fill, a))
    c.drawPath(path, paint(stroke, a, stroke=2))
