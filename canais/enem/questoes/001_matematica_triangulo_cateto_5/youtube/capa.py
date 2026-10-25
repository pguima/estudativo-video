"""Capas (miniaturas 1920x1080) — Estudativo · Questão de Matemática 001, com o visual da aula (design system de matemática).
python capa.py    -> youtube/capa_A_so_um_lado.jpg, capa_B_produto_notavel.jpg (Estudativo)
                     youtube_en/cover_A_only_one_side.jpg, cover_B_special_product.jpg (Estudativo English)"""
import importlib.util, sys
from pathlib import Path

PROJ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJ.parents[3] / "_ferramentas"))
import idioma  # noqa: E402
import skia  # noqa: E402

IDIOMAS_NO_CODIGO = True   # textos nos dois idiomas aqui mesmo (não usa textos_en.py)
TXT = dict(
    pt=dict(a=("SÓ SABE", "UM LADO?"), b=("PRODUTO", "NOTÁVEL"), b_sub="resolve em 4 passos", inteiros="LADOS INTEIROS",
            marca="ESTUDATIVO · QUESTÃO", pasta="youtube", arq=("capa_A_so_um_lado.jpg", "capa_B_produto_notavel.jpg")),
    en=dict(a=("ONLY ONE", "SIDE?!"), b=("SPECIAL", "PRODUCT"), b_sub="solves it in 4 steps", inteiros="WHOLE-NUMBER SIDES",
            marca="ESTUDATIVO · MATH QUESTION", pasta="youtube_en", arq=("cover_A_only_one_side.jpg", "cover_B_special_product.jpg")),
)


def visual(lang):
    idioma.definir(lang)
    spec = importlib.util.spec_from_file_location(f"visual_{lang}", PROJ / "roteiro" / "visual.py")
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def capa(lang, qual, out):
    V = visual(lang)
    T = TXT[lang]
    s = skia.Surface(V.W, V.H); c = s.getCanvas()
    c.drawImage(V.matematica._bg(), 0, 0)
    w = V.text_w(T["marca"], "extrabold", 30) + 36
    V.pill(c, T["marca"], 70 + w / 2, 90, 30, V.AMB, V.BG0, 1, "extrabold")
    l1, l2 = T[qual]
    if qual == "a":
        V.tri(c, 330, 880, 640, 540, 1, 0, "a = ?", "b = ?", "c = 5", size=96, hl=("c",))
        V.glow_text(c, l1, 1440, 400, 150, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, l2, 1440, 580, 170, "black", V.AMB, 1, glow=0.18)
        V.pill(c, T["inteiros"], 1440, 760, 54, V.MNT, V.BG0, 1)
    else:
        V.glow_text(c, l1, 960, 300, 170, "black", V.WHITE, 1, glow=0.12)
        V.glow_text(c, l2, 960, 480, 190, "black", V.AMB, 1, glow=0.18)
        V.eq(c, [("a² − b² = ", V.WHITE), ("(a + b)", V.CYA), ("(a − b)", V.MNT)], 700, 1, 110, cx=960, maxw=1700, box=V.CYA)
        V.label(c, T["b_sub"], 960, 880, 1, 64, V.INK2, "bold")
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    for lang in ("pt", "en"):
        pasta = PROJ / TXT[lang]["pasta"]
        pasta.mkdir(exist_ok=True)
        for qual, nome in zip("ab", TXT[lang]["arq"]):
            capa(lang, qual, pasta / nome)
