"""Som do piloto inteiro: trilha por blocos + efeitos presos às cues de cada cena (tempos de audio/tempos.json).
python som.py  → saida/piloto.mp4 (usa saida/piloto_mudo.mp4 e audio/narracao.wav)"""
import sys, json
from pathlib import Path
AQUI = Path(__file__).resolve().parent
sys.path.insert(0, str(AQUI.parents[2] / "_ferramentas"))
sys.path.insert(0, str(AQUI))
import idioma_antigos as lingua  # noqa: E402
lingua.preparar(globals())  # VIDEO_LANG=en: audio_en/ e saida_en/
from som_antigos import trilha_secoes, mixar_trilha  # noqa: E402
import teste_abertura as abre  # noqa: E402

T = json.loads((lingua.audio(AQUI) / "tempos.json").read_text())
S = {s["id"]: s for s in T["scenes"]}
DUR = T["total"]


def g(sid, cue=None, off=0.0):
    s = S[sid]
    return s["start"] + (s["cues"][cue] if cue else 0.0) + off


# efeitos por cena: (cue, atraso, efeito); toda cena a partir da 03 começa com "transicao"
FX = {
    "03": [("a", 3.0, "pop"), ("b", 0, "brilho"), ("c", 0, "transicao"), ("c", 1.5, "pop"), ("d", 0, "pouso"), ("d", 0.4, "pop")],
    "04": [("b", 2.0, "pop"), ("b", 2.6, "pop"), ("b", 3.2, "pop"), ("b", 3.8, "pop"), ("c", 0.2, "fantasma"), ("c", 2.2, "falha"),
           ("d", 0, "transicao"), ("d", 3.0, "pop"), ("e", 0, "transicao"), ("e", 0.4, "falha"), ("e", 4.0, "pop")],
    "05": [("a", 0.9, "whoosh"), ("a", 1.05, "brilho"), ("b", 0, "pop"), ("b", 0.3, "tique"), ("c", 0, "pop"), ("d", 0, "pop"),
           ("e", 0, "pop")],
    "06": [("a0", 1.4, "pop"), ("a0", 4.5, "pop"), ("a0", 9.0, "bateria"), ("a0", 9.6, "agua"), ("a", 0, "transicao"),
           ("a", 2.0, "pop"), ("b", 1.2, "rachar"), ("b", 3.0, "agua"), ("c", 0.4, "pop"), ("c", 5.0, "rachar"),
           ("d", 0, "transicao"), ("d", 0.3, "pop"), ("d", 0.9, "desabar"), ("d", 2.0, "desabar"), ("d", 3.4, "desabar"),
           ("e", 0, "transicao"), ("e", 2.0, "pop"), ("e", 3.5, "pop")],
    "07": [("a", 0.2, "pop"), ("a", 1.4, "pop"), ("b", 0, "transicao"), ("c", 0.4, "pop"), ("c", 3.0, "transicao"),
           ("c", 3.4, "pop"), ("c", 4.5, "pop"), ("d", 0, "transicao"), ("d", 0.6, "whoosh"), ("e", 0.4, "pop")],
    "08": [("a", 1.2, "pop"), ("b", 0, "transicao"), ("b", 1.0, "broca"), ("b", 1.5, "pop"), ("b", 3.0, "pop"),
           ("c", 0, "transicao"), ("c", 1.2, "pop"), ("d", 0, "pop"), ("d", 1.6, "pop"), ("d", 3.5, "pop"),
           ("e", 0, "transicao"), ("e", 0.3, "pouso"), ("e", 0.5, "pop"), ("e", 2.0, "pop")],
    "09": [("b", 0, "brilho"), ("b", 0.3, "pop"), ("c", 0, "transicao"), ("c", 0.6, "pop"), ("c", 1.8, "pop"), ("c", 3.0, "pop"),
           ("c", 5.0, "rachar"), ("c", 5.4, "pop"), ("d", 0, "transicao"), ("d", 2.2, "pop"), ("d", 3.2, "pop"), ("d", 4.2, "pop"),
           ("e", 0, "brilho"), ("e", 0.5, "pop")],
    "10": [("a", 0.2, "tique"), ("b", 0, "transicao"), ("b", 0.5, "pop"), ("c", 0, "pop"), ("c", 1.0, "pop")],
    "11": [("a", 3.2, "pop"), ("a", 4.2, "pop"), ("b", 0, "transicao"), ("b", 1.0, "pop"), ("b", 1.5, "pop"), ("b", 2.0, "pop"),
           ("c", 0, "transicao"), ("c", 1.5, "rachar"), ("c", 3.0, "rachar"), ("d", 0.2, "pouso"), ("e", 0, "transicao"),
           ("e", 0.5, "fogo"), ("e", 3.6, "pop"), ("e", 4.2, "pop"), ("e", 4.8, "pop"), ("e", 5.4, "pop"), ("f", 0, "brilho"),
           ("f", 0.2, "pop"), ("g", 0, "transicao"), ("g", 0.2, "pop"), ("g", 1.0, "whoosh"), ("g", 2.0, "pop"), ("g", 3.4, "pop")],
    "12": [("b", 0, "transicao"), ("b", 1.0, "brilho"), ("c", -0.2, "pop"), ("c", 0, "brilho"), ("d", 0, "transicao"),
           ("d", 0.3, "pop"), ("d", 4.0, "pop"), ("e", 0, "pop"), ("e", 1.0, "pop"), ("e", 2.0, "pop"), ("f", 0, "transicao"),
           ("f", 0.3, "pop"), ("f", 1.2, "pop"), ("g", 1.2, "carimbo")],
    "13": [("a", 0.5, "whoosh"), ("b", 0, "transicao"), ("b", 0.5, "pop"), ("b", 0.8, "cogumelo"), ("b", 1.3, "cogumelo"),
           ("b", 1.8, "cogumelo"), ("b", 2.3, "cogumelo"), ("b", 3.5, "pop"), ("c", 0, "transicao"), ("c", 0, "agua"),
           ("c", 1.5, "brilho"), ("c", 2.0, "pop"), ("d", 0, "transicao"), ("d", 1.0, "scan"), ("d", 2.5, "pop"), ("e", 0, "pop"),
           ("f", 0, "transicao"), ("f", 0.5, "pop"), ("f", 1.0, "pop"), ("f", 4.5, "pop"), ("g", 0.8, "carimbo")],
    "14": [("a", 0.3, "pop"), ("b", 0, "whoosh"), ("b", 0.3, "pop"), ("b", 2.0, "pop"), ("c", 0, "transicao"), ("c", 1.0, "pop"),
           ("d", 0, "scan"), ("d", 2.6, "pop"), ("e", 3.0, "pop")],
    "15": [("a", 0.3, "whoosh"), ("a", 2.0, "pop"), ("b", 0, "transicao"), ("b", 0.5, "pop"), ("b", 1.5, "pop"), ("c", 1.0, "pop"),
           ("c", 3.0, "pop"), ("d", 0, "transicao"), ("d", 1.0, "brilho"), ("d", 4.0, "falha"), ("d", 4.5, "pop"),
           ("e", 0, "transicao"), ("e", 0.3, "desabar"), ("e", 1.0, "pop"), ("f", 2.0, "maquina"), ("f", 3.1, "maquina"),
           ("f", 4.6, "maquina"), ("g", 0, "transicao"), ("g", 2.5, "pop")],
    "16": [("a", 0, "tique"), ("a", 1.4, "pop"), ("b", 0, "transicao"), ("b", 0.5, "pop"), ("b", 2.5, "pop"), ("c", 0, "transicao"),
           ("c", 0.3, "pop"), ("c", 1.5, "pop"), ("c", 3.9, "pop"), ("d", 0, "whoosh"), ("e", 1.0, "carimbo"), ("f", 0, "transicao"),
           ("f", 1.5, "pop"), ("f", 2.7, "pop"), ("f", 3.9, "pop"), ("g", 0, "transicao"), ("h", 0, "transicao"), ("h", 3.6, "brilho")],
    "17": [("a", 0, "whoosh"), ("b", 0, "transicao"), ("b", 0.3, "pop"), ("b", 2.5, "pop"), ("c", 0, "transicao"), ("c", 0.5, "scan"),
           ("c", 3.0, "pop"), ("d", 0, "transicao"), ("d", 0.5, "brilho"), ("d", 3.5, "pop"), ("e", 0, "transicao"), ("e", 0.3, "radio"),
           ("e", 3.0, "pop")],
    "18": [("b", 0, "brilho"), ("b", 1.0, "pop"), ("c", 0.4, "pop"), ("d", 0, "transicao"), ("d", 0, "pop"), ("d", 2.0, "pop"),
           ("d", 4.0, "pop"), ("e", 0, "whoosh"), ("e", 1.2, "brilho"), ("e2", 0, "transicao"), ("e2", 2.5, "pop"), ("e2", 7.0, "pop"),
           ("e2", 9.0, "brilho"), ("e2", 11.5, "pop"), ("f", 0, "transicao"), ("f", 0.6, "pop"), ("f", 2.3, "whoosh"),
           ("f", 2.8, "pop"), ("g", 0, "transicao"), ("g", 0.3, "pop"), ("g", 2.0, "pop")],
    "19": [("b", 0, "brilho"), ("c", 2.2, "brilho")],
    "20": [("a", 0.4, "pop"), ("a", 1.2, "whoosh"), ("a", 1.8, "maquina"), ("b", 0, "maquina"), ("b", 1.6, "maquina"),
           ("c", 0, "maquina"), ("c", 1.2, "maquina"), ("c", 2.6, "maquina"), ("d", 0, "maquina"), ("d", 1.0, "maquina")],
    "21": [("a", 1.0, "pop"), ("b", -0.2, "transicao"), ("b", 0.6, "pop"), ("c", 0.2, "pop")],
}

# abertura: os mesmos efeitos do teste
ABERTURA = abre.eventos()


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
         (abre.T_SALAO, P(pad=0.9, escuro=0.3, arp=1, baixo=1, kick=1, shk=1, glock=0.2)),
         (g("03"), CHEIA),
         (g("04"), P(pad=0.8, escuro=0.4, arp=0.6, baixo=0.5, shk=0.5, glock=0.5)),
         (g("05"), P(pad=0.9, escuro=0.6, arp=0.4, baixo=0.4, glock=0.6)),
         (g("05", "e"), P(pad=0.9, escuro=0.2, arp=1, baixo=1, kick=0.9, shk=1, glock=0.3)),
         (g("06", "a"), CHEIA),
         (g("09"), P(pad=0.8, escuro=0.2, arp=0.8, baixo=0.8, kick=0.6, shk=1, glock=0.6)),
         (g("11"), CHEIA),
         (g("13"), P(pad=0.9, escuro=0.7, arp=0.5, baixo=0.7, shk=0.4, glock=0.2)),
         (g("14"), P(pad=0.9, escuro=0.5, arp=0.6, baixo=0.6, shk=0.5, glock=0.4)),
         (g("15"), P(pad=0.9, escuro=0.8, arp=0.3, baixo=0.4, glock=0.6)),
         (g("16"), P(pad=0.7, escuro=1.0, baixo=0.3, glock=0.3)),
         (g("16", "h"), P(pad=0.6, escuro=1.0, glock=0.5)),
         (g("17"), P(pad=0.8, escuro=0.4, arp=0.4, glock=0.9)),
         (g("18"), P(pad=0.8, escuro=0.4, arp=0.5, baixo=0.5, glock=0.5)),
         (g("18", "e"), P(pad=0.9, escuro=0.0, arp=1, baixo=1, kick=0.8, shk=1, glock=0.4)),
         (g("19"), P(pad=0.9, escuro=0.2, arp=0.6, baixo=0.6, shk=0.4, glock=0.6)),
         (g("20"), P(pad=0.8, escuro=0.4, arp=0.3, baixo=0.3, glock=0.8)),
         (g("21"), P(pad=0.9, escuro=0.1, arp=0.9, baixo=0.9, kick=0.6, shk=0.9, glock=0.4)),
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
    mus = trilha_secoes(DUR, pontos(), sinos=[abre.T_SOBROU + 0.2, DUR - 3.4], subidas=[abre.T_SALAO, g("05", "e"), g("18", "e")])
    mixar_trilha(out / "piloto_mudo.mp4", lingua.audio(AQUI) / "narracao.wav", out / "piloto.mp4", DUR, mus, eventos(),
                 salvar_stems=out)
    print("ok", out / "piloto.mp4")
