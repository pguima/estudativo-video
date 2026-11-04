"""Som do Short 002: trilha animada + efeitos nos momentos das animações. Tudo SINTETIZADO (motor de _ferramentas/som_tech.py,
livre de direitos). Trilha em dó maior (C G Am F), 124 BPM, batida desde o 1º segundo; nas contagens ela abaixa e entra o
tique do cronômetro. Os eventos são escritos na linha do tempo do roteiro (as mesmas constantes de render_short.py) e
levados ao tempo real pelas ÂNCORAS da narração.
Uso: python3 som_short.py   (gera som/trilha.wav e som/sfx.wav e mixa final/estudativo_short_002_quantos_quadrados.mp4)
Pré-requisitos: trabalho/video_mudo.mp4 e audio/narracao.wav (python3 render_short.py)."""
import subprocess
import sys
from pathlib import Path
import numpy as np

HERE = Path(__file__).parent
sys.path.insert(0, str(HERE))
sys.argv = sys.argv[:1]
import render_short as R
import som_tech as ST
from som_tech import SR, note, nrm

LUFS = -14
G_TRILHA, G_SFX = 0.32, 2.4


def real(tr):
    """tempo do roteiro -> tempo real do vídeo (inverso de R.roteiro_t)"""
    rs, As = zip(*R._A)
    return float(np.interp(tr, rs, As))


class SomShort(ST.Som):
    def __init__(self):                       # sem tempos.json: a duração vem do render
        self.cfg = dict(bpm=124)
        self.DUR = R.DUR
        self.N = int(self.DUR * SR)
        self.T = np.arange(self.N) / SR
        self.rng = np.random.default_rng(11)
        self.BEAT = 60 / 124
        self.S16 = self.BEAT / 4
        self.BAR = 4 * self.BEAT
        self.t_full = 0.0
        self.t_out = real(R.T_CTA)

    def chord(self, t):
        PROG = [[36, 48, 52, 55, 60], [43, 50, 55, 59, 62], [45, 52, 57, 60, 64], [41, 53, 57, 60, 65]]  # C G Am F
        return PROG[int(t // (2 * self.BAR)) % 4]

    def tick(self, alto=False):
        tt = np.arange(int(0.09 * SR)) / SR
        f = 1760 if alto else 1320
        return (np.sin(2 * np.pi * f * tt) * np.exp(-tt * 70) + 0.5 * np.sin(2 * np.pi * 2 * f * tt) * np.exp(-tt * 120)) * 0.8

    def contagens(self):
        """(início, fim) reais de cada cronômetro"""
        return [(real(N["t_conta"]), real(N["t_conta"] + N["dur_conta"])) for N in (R.N1, R.N2, R.N3)]

    def trilha_short(self):
        st = self.trilha()
        g = np.ones(self.N)
        for a, b in self.contagens():          # contagem: trilha recua para dar espaço ao tique
            g = np.minimum(g, 1 - 0.65 * np.clip(np.minimum((self.T - a + 0.3) / 0.3, (b - self.T) / 0.25), 0, 1))
        return st * g[:, None]

    def plano(self):
        """[(tempo do roteiro, efeito, ganho)]"""
        P = []
        add = lambda t, n, g=1.0: P.append((t, n, g))
        add(0.1, "whoosh"); add(1.3, "alert", 0.9)                                  # quadro + "A MAIORIA ERRA"
        for N in (R.N1, R.N2, R.N3):
            if N is not R.N1:
                add(N["t_hook"] - 0.2, "whoosh"); add(N["t_hook"] + 0.1, "lock")
            for k in range(4):                                                     # opções A B C D
                add(N["t_opc"] + 0.25 * k, f"pop{k}")
            add(N["t_rev"], "whoosh", 0.7)                                         # fim da contagem
            add(N["t_tot"] + 0.9, "confirm", 1.3)                                  # a certa acende
            add(N["t_tot"] + 0.9, "deny", 0.5)                                     # as erradas riscadas
        # nível 1: casas 1x1, depois os 2x2 e os 3x3
        for k in range(12):
            add(R.T_1 + 0.15 + 0.17 * k, f"pop{k}", 0.55)
        for k in range(6):
            add(R.T_2 + 0.15 + 0.62 * k, f"pop{k + 1}", 0.9)
        for k in range(2):
            add(R.T_3 + 0.2 + 1.1 * k, f"pop{k + 3}", 1.0)
        add(R.N1["t_tot"], "impact", 0.35)
        add(R.T_ATALHO - 0.2, "whoosh", 0.8)
        for k in range(3):
            add(R.T_ATALHO + 0.4 + 1.2 * k, f"pop{k}")
        add(R.T_ATALHO + 4.2, "confirm")
        add(R.N3["t_hook"] + 0.5, "alert")                                         # "NÍVEL DIFÍCIL"
        tr = R.N2["t_rev"]
        for k in range(4):
            add(tr + 1.4 * k, f"pop{k}", 0.9)
        tr = R.N3["t_rev"]
        for k in range(8):
            add(tr + 0.4 * k, f"pop{k}", 0.8)
        add(R.N3["t_tot"], "impact", 0.5)
        # final
        add(R.T_CTA - 0.2, "whoosh")
        for k in range(4):
            add(R.T_CTA + 0.4 + 0.2 * k, f"pop{k}")
        add(R.T_CTA + 1.4, "notif"); add(R.T_CTA + 2.6, "shimmer")
        return P

    def sfx_short(self):
        buf = np.zeros((self.N, 2))

        def por(t, sig, g, pan=0.0):
            i0 = int(t * SR)
            if 0 <= i0 < self.N:
                n = min(len(sig), self.N - i0)
                buf[i0:i0 + n, 0] += sig[:n] * g * (1 - max(0, pan))
                buf[i0:i0 + n, 1] += sig[:n] * g * (1 + min(0, pan))
        for n_, (tr, nome, g) in enumerate(self.plano()):
            if nome.startswith("pop"):
                sig, base = self.fx("pop", int(nome[3:])), "pop"
            else:
                sig, base = self.fx(nome), nome
            pan = 0.0 if base in ("whoosh", "impact", "shimmer") else ((n_ % 3) - 1) * 0.2
            por(real(tr), sig, self.GAIN[base] * g, pan)
        for a, b in self.contagens():           # tique a cada segundo (o último mais agudo)
            n = int(round(b - a))
            for j in range(n):
                por(a + j * (b - a) / n, self.tick(j == n - 1), 0.10)
        return np.clip(buf, -1, 1)


def main():
    s = SomShort()
    som = HERE / "som"
    ST.save(som / "trilha.wav", s.trilha_short())
    ST.save(som / "sfx.wav", s.sfx_short())
    F = "aformat=sample_fmts=fltp:sample_rates=48000:channel_layouts=stereo"
    fc = (f"[1:a]{F},asplit=2[v][vk];[2:a]{F},volume={G_TRILHA}[m];"
          f"[m][vk]sidechaincompress=threshold=0.02:ratio=5:attack=40:release=600:makeup=1[md];"
          f"[3:a]{F},volume={G_SFX}[sx];"
          f"[v][md][sx]amix=inputs=3:duration=first:normalize=0,loudnorm=I={LUFS}:TP=-1.0:LRA=9[a]")
    out = HERE / "final" / "estudativo_short_002_quantos_quadrados.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(HERE / "trabalho" / "video_mudo.mp4"), "-i", str(R.NARRACAO),
                    "-i", str(som / "trilha.wav"), "-i", str(som / "sfx.wav"), "-filter_complex", fc, "-map", "0:v",
                    "-map", "[a]", "-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-shortest",
                    "-movflags", "+faststart", str(out)], check=True)
    print("FINAL (com trilha e efeitos):", out)


if __name__ == "__main__":
    main()
