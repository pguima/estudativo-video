"""Capas do Short 015 (ENEM 2025, questão 139) — 1080x1920 (formato de Short), com o visual do vídeo.
python capa.py -> youtube/capa_A_mediana.jpg, capa_B_medidas.jpg, capa_C_ordenar.jpg
Texto importante no miolo (y 400–1500): a grade do canal e o feed cortam as bordas."""
import importlib.util, os, sys
from pathlib import Path
os.environ.setdefault("VIDEO_FORMATO", "vertical")  # antes do import motor
PROJ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJ.parents[3] / "_ferramentas"))
import idioma  # noqa: E402
import skia  # noqa: E402


def visual():
    idioma.definir("pt")
    spec = importlib.util.spec_from_file_location("visual_pt", PROJ / "roteiro" / "visual.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def capa(V, qual, out):
    s = skia.Surface(V.W, V.H); c = s.getCanvas()
    c.drawImage(V.matematica._bg(), 0, 0)
    V.pill(c, "ENEM 2025 · QUESTÃO 139", V.CX, 300, 34, V.AMB, V.BG0, 1, "extrabold")
    if qual == "a":
        V.big(c, "QUAL É A", 480, 1, V.WHITE, 140)
        V.big(c, "MEDIANA?", 640, 1, V.WHITE, 150, hl="MEDIANA?", hl_col=V.CYA)
        c.save(); c.translate(V.CX, 760); c.scale(1.2, 1.2); c.translate(-V.CX, -760)
        V.coluna(c, 1, 1, lambda i, k: dict(borda=V.CYA, glow=1.0, cor_v=V.CYA) if k in (4, 5) else None, y0=760, passo=58)
        c.restore()
    elif qual == "b":
        V.big(c, "MÉDIA, MODA", 480, 1, V.WHITE, 120)
        V.big(c, "OU MEDIANA?", 630, 1, V.WHITE, 120, hl="MEDIANA?", hl_col=V.CYA)
        V.opcoes(c, 860, 1, 99, 0)   # sem marcar a certa: a capa não entrega a resposta
        V.stamp(c, "PEGADINHA DO ENEM", V.CX, 1500, V.RED, 1, 62, rot=-4)
    else:
        V.big(c, "ESQUECEU DE", 480, 1, V.WHITE, 120)
        V.big(c, "ORDENAR?", 630, 1, V.WHITE, 140, hl="ORDENAR?", hl_col=V.RED)
        c.save(); c.translate(V.CX, 760); c.scale(1.2, 1.2); c.translate(-V.CX, -760)
        V.coluna(c, 1, 0, lambda i, k: dict(borda=V.RED, glow=1.0, cor_v=V.RED) if i in (4, 5) else None, y0=760, passo=58)
        c.restore()
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("abc", ("capa_A_mediana.jpg", "capa_B_medidas.jpg", "capa_C_ordenar.jpg")):
        capa(V, qual, pasta / nome)
