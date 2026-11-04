"""Som do vídeo 02: trilha por blocos + efeitos presos às cues de cada cena (tempos de audio/tempos.json).
python som.py  → saida/video.mp4 (usa saida/video_mudo.mp4 e audio/narracao.wav)"""
import sys, json
from pathlib import Path
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[2] / "_ferramentas"))
import idioma_antigos as lingua  # noqa: E402
lingua.preparar(globals())
from som_antigos import trilha_secoes, mixar_trilha  # noqa: E402

T = json.loads((lingua.audio(AQUI) / "tempos.json").read_text())
S = {s["id"]: s for s in T["scenes"]}
DUR = T["total"]


def g(sid, cue=None, off=0.0):
    s = S[sid]
    return s["start"] + (s["cues"][cue] if cue else 0.0) + off


# abertura (cenas 01 e 02): holofote piscando, tela acendendo, câmera recuando, Lume pulando
_e = g("02", "a", 0.6)
ABERTURA = [(0.35, "holofote"), (0.44, "faisca"), (0.53, "faisca"), (0.62, "faisca"), (g("01", "b", 0.3), "pop"),
            (g("01", "c", 0.2), "fantasma"), (g("01", "c", 0.6), "pop"), (g("01", "d", 0.4), "pop"), (g("02"), "whoosh"),
            (g("02", None, 0.5), "luz"), (g("02", None, 0.9), "luz"), (_e, "pulo"), (_e + 0.5, "pouso"), (_e + 0.5, "pulo"),
            (_e + 1.0, "pouso"), (_e + 1.0, "pulo"), (_e + 1.5, "pouso"), (g("02", "b"), "brilho"), (g("02", "c", -0.4), "pop")]

# efeitos por cena: (cue, atraso, efeito); toda cena a partir da 03 começa com "transicao"
FX = {
    "03": [("a", 0.5, "pop"), ("a", 1.0, "pop"), ("a", 1.5, "pop"), ("a", 0.6, "tique"), ("b", 0, "transicao"), ("b", 0.4, "tique"),
           ("c", 0, "brilho"), ("c", 1.2, "pop"), ("d", 0, "transicao"), ("d", 1.6, "pop"), ("d", 2.6, "pop")],
    "04": [("a", 0.8, "vibra"), ("a", 1.0, "pop"), ("a", 2.0, "pop"), ("b", 0, "transicao"), ("b", 0.4, "pop"), ("c", 0.2, "scan"),
           ("c", 0.4, "pop"), ("d", 0, "transicao"), ("d", 0.1, "vibra"), ("d", 0.2, "carimbo")],
    "05": [("a", 0.3, "pop"), ("a", 3.0, "pop"), ("b", 0, "transicao"), ("b", 0.3, "pop"), ("c", -0.5, "pop"), ("c", 0.4, "pop")],
    "06": [("a", 0.5, "pop"), ("a", 0.8, "pop"), ("b", 0.2, "brilho"), ("b", 1.4, "pop"), ("b", 1.7, "pop"), ("b", 2.0, "pop"),
           ("b", 2.6, "moeda"), ("b", 3.3, "moeda"), ("b", 4.0, "moeda"), ("c", 0, "transicao"), ("c", 0.4, "tique"),
           ("c", 1.6, "pop"), ("d", 0, "transicao"), ("d", 0.4, "pop"), ("d", 1.2, "moeda"), ("d", 2.2, "moeda")],
    "07": [("a", 0.3, "pop"), ("a", 0.7, "pop"), ("b", 0, "transicao"), ("b", 0.4, "pop"), ("c", 0.3, "tique"), ("c", 1.0, "moeda"),
           ("c", 2.8, "pouso"), ("d", 0, "pop"), ("d", 0.4, "tique"), ("d", 1.4, "moeda"), ("d", 2.9, "moeda"),
           ("d", 4.4, "moeda"), ("d", 5.4, "pop"), ("e", 0, "transicao"), ("e", 0.2, "rolos"), ("e", 0.8, "pop")],
    "08": [("a", 0.8, "brilho"), ("a", 1.0, "pop"), ("b", 0, "transicao"), ("b", 0.3, "pop"), ("b", 1.6, "falha"),
           ("c", 0, "pop"), ("c", 1.0, "falha"), ("d", 0, "transicao"), ("d", 0.6, "pop"), ("e", 0, "pop"), ("e", 1.0, "ding"),
           ("e", 2.0, "brilho"), ("e", 3.2, "pop")],
    "09": [("a", 0.8, "pop"), ("b", 0, "transicao"), ("b", 0.4, "pop"), ("b", 0.6, "rolos"), ("b", 3.0, "rolos"),
           ("b", 5.4, "rolos"), ("b", 7.8, "rolos"), ("b", 10.2, "rolos"), ("c", 0.4, "pop"), ("d", 0, "transicao"),
           ("d", 0.05, "brilho"), ("d", 1.65, "brilho"), ("d", 2.4, "pop"), ("d", 3.0, "pop"), ("d", 3.25, "brilho")],
    "10": [("a", 0.5, "pop"), ("b", 0.4, "whoosh"), ("b", 2.8, "pop"), ("c", -0.2, "falha"), ("c", 0.2, "whoosh"),
           ("c", 1.5, "pop"), ("d", 0.6, "pop")],
    "11": [("a", 0.0, "vibra"), ("a", 0.4, "ding"), ("a", 1.8, "pop"), ("b", 0, "transicao"), ("b", 0.5, "pop"), ("b", 1.5, "ding"),
           ("b", 2.2, "ding"), ("b", 3.0, "pop"), ("c", 0, "pop"), ("c", 0.5, "pop"), ("c", 1.2, "pop"), ("d", 0, "transicao"),
           ("d", 0.1, "pop"), ("d", 1.0, "brilho")],
    "12": [("a", 0.4, "pop"), ("a", 1.4, "tique"), ("b", 0, "transicao"), ("b", 0.3, "tique"), ("c", 0, "transicao"),
           ("c", 0.3, "tique"), ("c", 1.9, "pop"), ("c", 3.5, "pop"), ("d", 0, "transicao"), ("d", 0.7, "pop"), ("d", 1.4, "pop"),
           ("d", 2.1, "pop"), ("d", 2.8, "pop")],
    "13": [("a", 0.3, "whoosh"), ("b", 0, "transicao"), ("b", 0.4, "maquina"), ("d", 0, "transicao"), ("d", 0.3, "falha"),
           ("e", 0, "transicao"), ("e", 0.3, "tique"), ("e", 0.8, "carimbo")],
    "14": [("a", 0.5, "luz"), ("a", 2.2, "brilho"), ("b", 0, "transicao"), ("b", 1.2, "pop"), ("b", 2.0, "falha"),
           ("b", 2.6, "pop"), ("b", 2.8, "maquina"), ("c", 0, "transicao"), ("c", 0.4, "pop"), ("c", 2.6, "brilho"),
           ("d", 0, "transicao"), ("d", 0.3, "pop"), ("d", 0.9, "pop")],
    "15": [("a", 0.3, "whoosh"), ("b", 0.5, "pop"), ("b", 0.6, "brilho"), ("c", 0, "whoosh"), ("c", 0.5, "pop"), ("c", 0.6, "brilho"),
           ("d", 0, "transicao"), ("d", 0.5, "pulo"), ("d", 1.6, "pop")],
    "16": [("a", 1.0, "falha"), ("a", 2.7, "whoosh"), ("a", 3.6, "pouso"), ("b", 0, "transicao"), ("b", 1.6, "pop"), ("b", 2.2, "pop"),
           ("b", 2.8, "pop"), ("b", 3.4, "pop"), ("c", 0, "transicao"), ("c", 0.2, "pop"), ("d", 0.8, "brilho")],
    "17": [("a", 0.6, "falha"), ("a", 1.2, "whoosh"), ("a", 1.8, "maquina"), ("b", 0, "maquina"), ("b", 1.4, "maquina"),
           ("c", 0, "maquina"), ("c", 1.2, "maquina"), ("d", 0, "maquina"), ("d", 1.2, "maquina")],
    "18": [("a", 1.0, "pop"), ("b", -0.2, "transicao"), ("b", 0.6, "pop"), ("c", 0.2, "pop")],
}


def eventos():
    ev = list(ABERTURA)
    for sid, lst in FX.items():
        ev.append((g(sid) + 0.05, "transicao"))
        for cue, off, nome in lst:
            ev.append((g(sid, cue, off), nome))
    return sorted(ev)


def P(**kw):
    return kw


CHEIA = P(pad=0.8, escuro=0.3, arp=0.9, baixo=0.9, kick=0.7, shk=0.8, glock=0.2)


def pontos():
    """intensidade da trilha por bloco (cada mudança leva ~1,5 s)"""
    b = [(0.0, P(pad=0.9, escuro=1.0, glock=1.0)),
         (g("02", None, 0.5), P(pad=0.9, escuro=0.3, arp=1, baixo=1, kick=1, shk=1, glock=0.2)),
         (g("03"), CHEIA),
         (g("04"), P(pad=0.8, escuro=0.4, arp=0.6, baixo=0.5, shk=0.5, glock=0.5)),
         (g("05"), P(pad=0.9, escuro=0.6, arp=0.4, baixo=0.4, glock=0.6)),
         (g("06"), CHEIA),
         (g("07"), P(pad=0.8, escuro=0.3, arp=0.8, baixo=0.8, kick=0.6, shk=1, glock=0.6)),
         (g("08"), P(pad=0.9, escuro=0.5, arp=0.6, baixo=0.6, shk=0.5, glock=0.6)),
         (g("09"), CHEIA),
         (g("11"), P(pad=0.8, escuro=0.3, arp=0.9, baixo=0.9, kick=0.8, shk=1, glock=0.3)),
         (g("12"), P(pad=0.8, escuro=0.4, arp=0.7, baixo=0.6, shk=0.7, glock=0.4)),
         (g("13"), P(pad=0.8, escuro=1.0, baixo=0.4, glock=0.2)),
         (g("13", "e"), P(pad=0.7, escuro=1.0, baixo=0.6, kick=0.4, glock=0.0)),
         (g("14"), P(pad=0.9, escuro=0.5, arp=0.5, baixo=0.5, glock=0.6)),
         (g("14", "b"), P(pad=0.9, escuro=0.2, arp=1, baixo=1, kick=0.8, shk=1, glock=0.4)),
         (g("16"), P(pad=0.9, escuro=0.3, arp=0.6, baixo=0.6, shk=0.4, glock=0.6)),
         (g("17"), P(pad=0.8, escuro=0.4, arp=0.3, baixo=0.3, glock=0.8)),
         (g("18"), P(pad=0.9, escuro=0.1, arp=0.9, baixo=0.9, kick=0.6, shk=0.9, glock=0.4)),
         (DUR - 3.0, P(pad=0.9, escuro=0.1, arp=0.4, baixo=0.3, glock=0.4)),
         (DUR, P())]
    out = []
    for k, (t, d) in enumerate(b):
        if k:
            out.append((max(out[-1][0] + 0.01, t - 1.5), b[k - 1][1]))  # segura o bloco anterior até a transição
        out.append((t, d))
    return out


if __name__ == "__main__":
    out = lingua.saida(AQUI)
    mus = trilha_secoes(DUR, pontos(), sinos=[g("02", "c", 1.6), DUR - 3.4], subidas=[g("02", None, 0.5), g("14", "b")])
    mixar_trilha(out / "video_mudo.mp4", lingua.audio(AQUI) / "narracao.wav", out / "video.mp4", DUR, mus, eventos(),
                 salvar_stems=out)
    print("ok", out / "video.mp4")
