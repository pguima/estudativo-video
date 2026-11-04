"""Capas do Short 027 (ENEM 2025, questão 145) — 1080x1920 (formato de Short), com o visual do vídeo.
python capa.py -> youtube/capa_A_homem_que_acessa.jpg, capa_B_nao_e_40.jpg
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
    V.pill(c, "ENEM 2025 · QUESTÃO 145", V.CX, 300, 34, V.AMB, V.BG0, 1, "extrabold")
    if qual == "a":   # os dados e a pergunta: não entrega a resposta
        V.big(c, "QUAL A CHANCE DE SER", 470, 1, V.WHITE, 84)
        V.big(c, "HOMEM QUE ACESSA?", 600, 1, V.WHITE, 104, hl="HOMEM QUE ACESSA?", hl_col=V.CYA)
        V.stat(c, "90%", "acessam redes sociais", 870, V.WHITE, 1, 99, 0)
        V.stat(c, "60%", "de quem acessa são mulheres", 1210, V.AMB, 1, 99, 0)
        V.label(c, "probabilidade sem decoreba", V.CX, 1500, 1, 54, V.AMB, "black")
    else:   # a armadilha: 40/100 riscado
        V.big(c, "NÃO É 40%!", 540, 1, V.RED, 150)
        V.opcao(c, "C", V.CX, 930, 1, V.RED, marca="errado", k=1.5)
        V.stamp(c, "ARMADILHA DO ENEM", V.CX, 1420, V.RED, 1, 62, rot=-4)
    s.makeImageSnapshot().save(str(out), skia.kJPEG, 90)
    print(out)


if __name__ == "__main__":
    V = visual()
    pasta = PROJ / "youtube"
    for qual, nome in zip("ab", ("capa_A_homem_que_acessa.jpg", "capa_B_nao_e_40.jpg")):
        capa(V, qual, pasta / nome)
