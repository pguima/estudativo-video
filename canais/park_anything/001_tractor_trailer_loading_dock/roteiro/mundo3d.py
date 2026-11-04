"""Mini-motor 3D do Park Anything (skia + numpy, sem GPU): câmera em perspectiva, recorte no plano próximo, faces com
luz do sol (difusa + ambiente + gradiente de oclusão na base), sombras suaves projetadas no chão e decalques
(texto/imagem) aplicados em faces com perspectiva. Mundo em metros: X leste, Y norte, Z para cima.

Uso no visual.py:
    cam = Camera(eye, alvo, fov)           # graus
    cena = Cena(cam)
    cena.chao(poligono_xy, cor)            # camadas do chão, na ordem
    cena.caixa(centro, tam, yaw, cor)      # objetos sólidos (ordenados por profundidade no desenho)
    cena.desenhar(c)"""
import math
from functools import lru_cache
import numpy as np
import skia
from motor import hexc, paint

W, H = 1920, 1080
SOL = np.array([-0.42, -0.55, 0.72])          # direção PARA o sol (vem do sudoeste, alto)
SOL = SOL / np.linalg.norm(SOL)
SOMBRA_DIR = -SOL                               # raios do sol (para baixo)
NEAR = 0.3


def _rgb(h):
    h = h.lstrip("#")
    return np.array([int(h[i:i + 2], 16) for i in (0, 2, 4)], float)


def _hex(v):
    v = np.clip(v, 0, 255)
    return "#%02X%02X%02X" % tuple(int(x) for x in v)


def tom(cor, k):
    """cor multiplicada por k (k > 1 clareia em direção ao branco)"""
    v = _rgb(cor)
    if k <= 1:
        return _hex(v * k)
    return _hex(v + (255 - v) * min(1, k - 1))


def mistura(c1, c2, u):
    return _hex(_rgb(c1) * (1 - u) + _rgb(c2) * u)


class Camera:
    def __init__(self, eye, alvo, fov=40.0, roll=0.0):
        self.e = np.array(eye, float)
        a = np.array(alvo, float)
        f = a - self.e
        f /= np.linalg.norm(f)
        up = np.array([0, 0, 1.0])
        r = np.cross(f, up)
        if np.linalg.norm(r) < 1e-6:
            r = np.array([1.0, 0, 0])
        r /= np.linalg.norm(r)
        u = np.cross(r, f)
        if roll:
            cr, sr = math.cos(roll), math.sin(roll)
            r, u = r * cr + u * sr, -r * sr + u * cr
        self.f, self.r, self.u = f, r, u
        self.F = (H / 2) / math.tan(math.radians(fov) / 2)

    def cam(self, P):
        """mundo → câmera (x direita, y cima, z profundidade); P: (n, 3)"""
        d = np.asarray(P, float) - self.e
        return np.stack([d @ self.r, d @ self.u, d @ self.f], axis=-1)

    def tela(self, Pc):
        Pc = np.asarray(Pc, float)
        z = np.maximum(Pc[..., 2], 1e-6)
        return np.stack([W / 2 + self.F * Pc[..., 0] / z, H / 2 - self.F * Pc[..., 1] / z], axis=-1)

    def proj(self, P):
        """mundo → tela (sem recorte); devolve (xy, z)"""
        Pc = self.cam(np.atleast_2d(P))
        return self.tela(Pc), Pc[:, 2]


def _recorta(Pc):
    """Sutherland-Hodgman no plano z = NEAR (coordenadas de câmera)"""
    out = []
    n = len(Pc)
    for i in range(n):
        a, b = Pc[i], Pc[(i + 1) % n]
        ia, ib = a[2] >= NEAR, b[2] >= NEAR
        if ia:
            out.append(a)
        if ia != ib:
            t = (NEAR - a[2]) / (b[2] - a[2])
            out.append(a + (b - a) * t)
    return np.array(out) if len(out) >= 3 else None


def _path(xy):
    p = skia.Path()
    p.moveTo(*xy[0])
    for q in xy[1:]:
        p.lineTo(*q)
    p.close()
    return p


def _hull(pts):
    pts = sorted(set(map(tuple, np.round(pts, 4))))
    if len(pts) < 3:
        return np.array(pts)

    def cross(o, a, b):
        return (a[0] - o[0]) * (b[1] - o[1]) - (a[1] - o[1]) * (b[0] - o[0])
    lo, up = [], []
    for p in pts:
        while len(lo) >= 2 and cross(lo[-2], lo[-1], p) <= 0:
            lo.pop()
        lo.append(p)
    for p in reversed(pts):
        while len(up) >= 2 and cross(up[-2], up[-1], p) <= 0:
            up.pop()
        up.append(p)
    return np.array(lo[:-1] + up[:-1])


def rotz(yaw):
    c, s = math.cos(yaw), math.sin(yaw)
    return np.array([[c, -s, 0], [s, c, 0], [0, 0, 1.0]])


class Face:
    __slots__ = ("P", "cor", "alfa", "n", "luz", "deco", "ao", "brilho", "z", "camada", "vies")

    def __init__(self, P, cor, alfa=1.0, luz=True, deco=None, ao=0.0, brilho=0.0, camada=2, vies=0.0):
        self.camada = camada
        self.vies = vies      # metros somados à distância na ordenação (rodas: desenhar antes da carroceria)
        self.P = np.asarray(P, float)
        self.cor, self.alfa, self.luz, self.deco, self.ao, self.brilho = cor, alfa, luz, deco, ao, brilho
        a, b, c = self.P[0], self.P[1], self.P[2]
        n = np.cross(b - a, c - a)
        nn = np.linalg.norm(n)
        self.n = n / nn if nn > 1e-9 else np.array([0, 0, 1.0])


class Cena:
    def __init__(self, cam):
        self.cam = cam
        self.camadas_chao = []     # (P (n,3) ou função, cor, alfa)
        self.faces = []
        self.sombras = []          # pontos 3D cujo fecho convexo projetado vira sombra
        self.sobre_chao = []       # callbacks (c, cam) desenhados depois do chão e das sombras
        self.por_cima = []         # callbacks desenhados depois dos sólidos

    # ---------------- construção
    def chao(self, xy, cor, alfa=1.0, z=0.0):
        xy = np.asarray(xy, float)
        self.camadas_chao.append((np.column_stack([xy, np.full(len(xy), z)]), cor, alfa))

    def face(self, P, cor, **kw):
        self.faces.append(Face(P, cor, **kw))

    def caixa(self, centro, tam, yaw, cor, base=None, sombra=True, cores=None, alfa=1.0, ao=0.18, deco=None, R=None, O=None,
              camada=2):
        """camada: 0 prédio, 1 peças presas na parede, 2 o resto (ordenado por distância). caixa: centro (x, y, z do centro), tam (comprimento em x local, largura y, altura z), yaw;
        R/O opcionais: rotação/origem extra (peças no referencial de um veículo). cores: dict por face
        (topo, frente, tras, esq, dir, baixo). deco: dict face -> callback(c, quad_tela)"""
        cx, cy, cz = centro
        lx, ly, lz = tam[0] / 2, tam[1] / 2, tam[2] / 2
        V = np.array([[sx * lx, sy * ly, sz * lz] for sx in (-1, 1) for sy in (-1, 1) for sz in (-1, 1)])
        V = V @ rotz(yaw).T + np.array([cx, cy, cz])
        if R is not None:
            V = V @ R.T + O
        # índices: (sx, sy, sz) → 4*ix + 2*iy + iz
        idx = lambda sx, sy, sz: 4 * (sx > 0) + 2 * (sy > 0) + (sz > 0)
        # faces verticais na ordem (inf-esq, inf-dir, sup-dir, sup-esq) vistas de fora; normal para fora
        quads = {
            "topo": [idx(-1, -1, 1), idx(1, -1, 1), idx(1, 1, 1), idx(-1, 1, 1)],
            "frente": [idx(1, -1, -1), idx(1, 1, -1), idx(1, 1, 1), idx(1, -1, 1)],
            "tras": [idx(-1, 1, -1), idx(-1, -1, -1), idx(-1, -1, 1), idx(-1, 1, 1)],
            "esq": [idx(1, 1, -1), idx(-1, 1, -1), idx(-1, 1, 1), idx(1, 1, 1)],
            "dir": [idx(-1, -1, -1), idx(1, -1, -1), idx(1, -1, 1), idx(-1, -1, 1)],
        }
        for k, q in quads.items():
            cor_k = (cores or {}).get(k, cor)
            if cor_k is None:
                continue
            self.faces.append(Face(V[q], cor_k, alfa=alfa, ao=0 if k == "topo" else ao, deco=(deco or {}).get(k), camada=camada))
        if sombra:
            self.sombras.append(V)
        return V

    def cilindro(self, centro, raio, larg, eixo_yaw, cor, R=None, O=None, n=12, cor_tampa=None, sombra=False, eixo="y", vies=0.0):
        """cilindro deitado (roda): eixo ao longo de y local (girado por eixo_yaw); centro em z = raio"""
        cx, cy, cz = centro
        ang = np.linspace(0, 2 * math.pi, n, endpoint=False)
        ring = np.stack([np.cos(ang) * raio, np.zeros(n), np.sin(ang) * raio], axis=1)
        A = ring + [0, -larg / 2, 0]
        B = ring + [0, larg / 2, 0]
        Rz = rotz(eixo_yaw)
        A = A @ Rz.T + [cx, cy, cz]
        B = B @ Rz.T + [cx, cy, cz]
        if R is not None:
            A, B = A @ R.T + O, B @ R.T + O
        for i in range(n):
            j = (i + 1) % n
            self.faces.append(Face([A[i], B[i], B[j], A[j]], cor, ao=0.0, vies=vies))
        self.faces.append(Face(A, cor_tampa or cor, ao=0.0, vies=vies))
        self.faces.append(Face(B[::-1], cor_tampa or cor, ao=0.0, vies=vies))
        if sombra:
            self.sombras.append(np.vstack([A, B]))

    # ---------------- desenho
    def _poli_tela(self, P):
        Pc = self.cam.cam(P)
        Pc = _recorta(Pc)
        if Pc is None:
            return None
        return self.cam.tela(Pc)

    def desenhar(self, c):
        cam = self.cam
        for P, cor, alfa in self.camadas_chao:
            xy = self._poli_tela(P)
            if xy is not None:
                c.drawPath(_path(xy), paint(cor, alfa))
        # sombras numa camada única (sem escurecer duas vezes onde se sobrepõem)
        if self.sombras:
            lay = skia.Paint(Color=skia.ColorSetARGB(int(255 * 0.34), 0, 0, 0))
            c.saveLayer(None, lay)
            pb = skia.Paint(AntiAlias=True, Color=skia.ColorSetARGB(255, 18, 22, 30))
            esc = max(1.0, cam.F / 1400)
            pb.setMaskFilter(skia.MaskFilter.MakeBlur(skia.kNormal_BlurStyle, 2.2 * esc))
            for V in self.sombras:
                t = V[:, 2] / -SOMBRA_DIR[2]
                G = V + SOMBRA_DIR * t[:, None]
                G[:, 2] = 0.01
                hull = _hull(G[:, :2])
                if len(hull) < 3:
                    continue
                xy = self._poli_tela(np.column_stack([hull, np.full(len(hull), 0.01)]))
                if xy is not None:
                    c.drawPath(_path(xy), pb)
            c.restore()
        for fn in self.sobre_chao:
            fn(c, cam)
        # sólidos: culling + pintor
        itens = []
        for f in self.faces:
            cen = f.P.mean(axis=0)
            if np.dot(f.n, cam.e - cen) <= 0:
                continue
            Pc = cam.cam(f.P)
            if (Pc[:, 2] < NEAR).all():
                continue
            itens.append((f.camada, float(np.linalg.norm(cen - cam.e)) + f.vies, f, Pc))
        itens.sort(key=lambda it: (it[0], -it[1]))
        for _, _, f, Pc in itens:
            Pr = _recorta(Pc) if (Pc[:, 2] < NEAR).any() else Pc
            if Pr is None:
                continue
            xy = cam.tela(Pr)
            k = 1.0
            if f.luz:
                dif = max(0.0, float(np.dot(f.n, SOL)))
                k = 0.62 + 0.5 * dif + 0.08 * f.n[2]
            cor = tom(f.cor, k)
            path = _path(xy)
            p = paint(cor, f.alfa)
            if f.ao > 0 and len(xy) >= 3:
                zs = f.P[:, 2]
                lo, hi = int(np.argmin(zs)), int(np.argmax(zs))
                if zs[hi] - zs[lo] > 0.05:
                    y0, y1 = xy[hi], xy[lo]
                    sh = skia.GradientShader.MakeLinear(
                        [skia.Point(*y0), skia.Point(*y1)],
                        [hexc(cor, f.alfa), hexc(tom(cor, 1 - f.ao), f.alfa)])
                    p.setShader(sh)
            c.drawPath(path, p)
            if f.deco and Pr is Pc:
                P0, P1, P2, P3 = f.P

                def P(u, v, P0=P0, P1=P1, P2=P2, P3=P3):
                    bot = P0 + (P1 - P0) * u
                    top = P3 + (P2 - P3) * u
                    return cam.tela(cam.cam(bot + (top - bot) * v))
                f.deco(c, P, f)
        for fn in self.por_cima:
            fn(c, cam)


# ---------------- decalques em perspectiva
def matriz_quad(src_wh, quad):
    """matriz que leva o retângulo (0,0)-(w,h) da imagem para o quadrilátero da tela (4 pontos na ordem
    sup-esq, sup-dir, inf-dir, inf-esq)"""
    w, h = src_wh
    m = skia.Matrix()
    src = [skia.Point(0, 0), skia.Point(w, 0), skia.Point(w, h), skia.Point(0, h)]
    dst = [skia.Point(float(x), float(y)) for x, y in quad]
    m.setPolyToPoly(src, dst)
    return m


def decalque(c, img, quad, alfa=1.0):
    m = matriz_quad((img.width(), img.height()), quad)
    c.save()
    c.concat(m)
    c.drawImage(img, 0, 0, skia.SamplingOptions(skia.FilterMode.kLinear, skia.MipmapMode.kLinear), paint("#FFFFFF", alfa))
    c.restore()


def linha3d(c, cam, P, cor, larg, alfa=1.0, cap=True, dash=None):
    """polilinha 3D (recortada) com espessura em pixels"""
    Pc = cam.cam(np.asarray(P, float))
    pts = []
    path = skia.Path()
    started = False
    for i in range(len(Pc)):
        if Pc[i, 2] >= NEAR:
            q = cam.tela(Pc[i])
            if not started:
                path.moveTo(*q)
                started = True
            else:
                path.lineTo(*q)
        else:
            started = False
    p = paint(cor, alfa, stroke=larg)
    p.setStrokeJoin(skia.Paint.kRound_Join)
    if cap:
        p.setStrokeCap(skia.Paint.kRound_Cap)
    if dash:
        p.setPathEffect(skia.DashPathEffect.Make(dash, 0))
    c.drawPath(path, p)
