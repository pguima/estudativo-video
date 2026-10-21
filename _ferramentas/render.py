"""Renderiza o vídeo de um projeto.

python render.py <proj> --stills 12.5,40,90     -> PNGs de prévia em <proj>/trabalho/stills
python render.py <proj> --video [--from 0 --to 60] [--jobs 4] [--retomar]
python render.py <proj> --final                 -> junta segmentos + narração + trilha em <proj>/final
"""
import argparse, importlib.util, json, math, subprocess, sys
from multiprocessing import Pool
from pathlib import Path

sys.path.insert(0, str(Path(__file__).parent))
import motor as M

SEG = 20.0  # segundos por segmento de render

_STATE = {}


def load(proj):
    proj = Path(proj)
    def mod(name, path):
        spec = importlib.util.spec_from_file_location(name, path)
        m = importlib.util.module_from_spec(spec); spec.loader.exec_module(m); return m
    cenas = mod("cenas", proj / "roteiro" / "cenas.py")
    visual = mod("visual", proj / "roteiro" / "visual.py")
    tempos = json.loads((proj / "audio" / "tempos.json").read_text(encoding="utf-8"))
    blk_of = {s["id"]: s["block"] for s in cenas.SCENES}
    scenes = tempos["scenes"]
    C = M.Cues()
    for s in scenes:
        s["block"] = blk_of[s["id"]]
        C[s["id"]] = s["start"]
        C[s["id"] + ".end"] = s["start"] + s["dur"]
        for k, v in s["cues"].items():
            C[f"{s['id']}.{k}"] = s["start"] + v
    blocks = []
    for s in scenes:
        if blocks and blocks[-1]["name"] == s["block"]:
            blocks[-1]["end"] = s["start"] + s["dur"]
        else:
            blocks.append(dict(name=s["block"], start=s["start"], end=s["start"] + s["dur"]))
    total = tempos["total"] + 0.3
    return dict(proj=proj, visual=visual, scenes=scenes, C=C, blocks=blocks, total=total)


def frame(st, c, t):
    # ganchos opcionais do visual.py: BACKGROUND(c, t), CAPTION(c, scene, t), OVERLAY(c, t) (canal tecnologia)
    bg = getattr(st["visual"], "BACKGROUND", None)
    bg(c, t) if bg else M.background(c)
    for b in st["blocks"]:
        if b["start"] - 0.01 <= t < b["end"] + 0.4:
            a = M.ease_io(M.prog(t, b["start"], 0.45)) * (1 - M.ease_io(M.prog(t, b["end"] - 0.05, 0.4)))
            if a <= 0:
                continue
            if a < 1:
                c.saveLayerAlpha(None, int(a * 255))
            st["visual"].BLOCKS[b["name"]](c, t, st["C"], b)
            if a < 1:
                c.restore()
    cap = getattr(st["visual"], "CAPTION", M.draw_caption)
    for s in st["scenes"]:
        if s["start"] <= t < s["start"] + s["dur"]:
            cap(c, s, t)
    ov = getattr(st["visual"], "OVERLAY", None)
    if ov:
        ov(c, t)
    wm = getattr(st["visual"], "MARCA", "")
    if wm:
        M.text(c, wm, M.W / 2, 1052, 20, "semibold", "#C9C9C6")


def _init(proj):
    _STATE.update(load(proj))


def render_seg(args):
    i, f0, f1, out = args
    import skia
    st = _STATE
    surf = skia.Surface(M.W, M.H)
    c = surf.getCanvas()
    ff = subprocess.Popen(["ffmpeg", "-v", "error", "-y", "-f", "rawvideo", "-pix_fmt", "rgba", "-s", f"{M.W}x{M.H}",
                           "-r", str(M.FPS), "-i", "-", "-c:v", "libx264", "-preset", "medium", "-crf", "17",
                           "-pix_fmt", "yuv420p", "-threads", "2", str(out)], stdin=subprocess.PIPE)
    for f in range(f0, f1):
        frame(st, c, f / M.FPS)
        ff.stdin.write(surf.makeImageSnapshot().toarray(colorType=skia.kRGBA_8888_ColorType).tobytes())
    ff.stdin.close(); ff.wait()
    return i


def duracao(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                       capture_output=True, text=True)
    try:
        return float(r.stdout.strip())
    except ValueError:
        return -1.0


def main():
    ap = argparse.ArgumentParser()
    ap.add_argument("proj")
    ap.add_argument("--stills")
    ap.add_argument("--video", action="store_true")
    ap.add_argument("--final", action="store_true")
    ap.add_argument("--from", dest="t0", type=float, default=0)
    ap.add_argument("--to", dest="t1", type=float, default=None)
    ap.add_argument("--jobs", type=int, default=4)
    ap.add_argument("--retomar", action="store_true", help="pula segmentos já completos")
    a = ap.parse_args()
    proj = Path(a.proj)
    st = load(proj)
    if a.stills:
        import skia
        out = proj / "trabalho" / "stills"; out.mkdir(parents=True, exist_ok=True)
        surf = skia.Surface(M.W, M.H); c = surf.getCanvas()
        for ts in a.stills.split(","):
            t = float(ts)
            frame(st, c, t)
            surf.makeImageSnapshot().save(str(out / f"t{t:07.2f}.png"), skia.kPNG)
        print("ok", out)
    if a.video:
        segdir = proj / "trabalho" / "segmentos"; segdir.mkdir(parents=True, exist_ok=True)
        t1 = a.t1 if a.t1 is not None else st["total"]
        nseg = math.ceil(st["total"] / SEG)
        jobs = []
        for i in range(nseg):
            s, e = i * SEG, min((i + 1) * SEG, st["total"])
            if e <= a.t0 or s >= t1:
                continue
            out = segdir / f"seg_{i:03d}.mp4"
            if a.retomar and out.exists() and abs(duracao(out) - (e - s)) < 0.1:
                continue  # segmento já completo
            jobs.append((i, round(s * M.FPS), round(e * M.FPS), out))
        print(f"{len(jobs)} segmentos para renderizar", flush=True)
        with Pool(a.jobs, initializer=_init, initargs=(str(proj),)) as pool:
            for i in pool.imap_unordered(render_seg, jobs):
                print(f"segmento {i} pronto ({len(jobs)} no total)", flush=True)
    if a.final:
        finalize(proj, st)


def finalize(proj, st):
    segdir = proj / "trabalho" / "segmentos"
    segs = sorted(segdir.glob("seg_*.mp4"))
    lst = segdir / "lista.txt"
    lst.write_text("".join(f"file '{p.name}'\n" for p in segs), encoding="utf-8")
    video = proj / "trabalho" / "video_mudo.mp4"
    subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-safe", "0", "-i", str(lst), "-c", "copy", str(video)], check=True)
    musica = proj / "audio" / "trilha.wav"
    nome = getattr(st["visual"], "ARQUIVO_FINAL", "video_final.mp4")
    (proj / "final").mkdir(exist_ok=True)
    out = proj / "final" / nome
    cmd = ["ffmpeg", "-v", "error", "-y", "-i", str(video), "-i", str(proj / "audio" / "narracao.wav")]
    if musica.exists():
        cmd += ["-i", str(musica), "-filter_complex",
                "[2:a]volume=1.0[m];[1:a]asplit[v1][v2];[m][v2]sidechaincompress=threshold=0.03:ratio=4:attack=30:release=600[md];"
                "[v1][md]amix=inputs=2:duration=first:normalize=0,alimiter=limit=0.95[a]",
                "-map", "0:v", "-map", "[a]"]
    else:
        cmd += ["-map", "0:v", "-map", "1:a"]
    cmd += ["-c:v", "copy", "-c:a", "aac", "-b:a", "256k", "-ar", "48000", "-shortest", "-movflags", "+faststart", str(out)]
    subprocess.run(cmd, check=True)
    print("FINAL:", out)


if __name__ == "__main__":
    main()
