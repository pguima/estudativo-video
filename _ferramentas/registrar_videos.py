"""Gera o registro de TODOS os vídeos criados (todos os canais), para consultar depois do backup.

Uso: python _ferramentas/registrar_videos.py
Saída: REGISTRO_DE_VIDEOS.md (legível, por canal) e registro_videos.csv (planilha), na raiz de videos_canal/.
Lê de cada projeto: final/*.mp4, shorts/*.mp4, roteiro/cenas.py (TITULO e fonte), youtube/publicacao.md (título recomendado)
e youtube/capa_*.jpg. Pode rodar de novo a qualquer momento: sobrescreve os dois arquivos.
"""
import csv, datetime, json, re, subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CANAIS = {"enem": "ENEM (Estudativo)", "seguridade_social": "Seguridade Social / INSS (Estudativo)",
          "tecnologia": "Tecnologia", "trading": "Trading"}


def dur(p):
    r = subprocess.run(["ffprobe", "-v", "error", "-show_entries", "format=duration", "-of", "csv=p=0", str(p)],
                       capture_output=True, text=True)
    try:
        s = float(r.stdout.strip())
        return f"{int(s // 60)}:{int(s % 60):02d}", s
    except ValueError:
        return "?", 0.0


def titulo_roteiro(proj):
    f = proj / "roteiro" / "cenas.py"
    if not f.exists():
        return "", ""
    s = f.read_text(encoding="utf-8", errors="ignore")
    m = re.search(r'^TITULO\s*=\s*"(.*?)"', s, re.M)
    b = re.search(r"^#\s*Base:\s*(.*)$", s, re.M)
    return (m.group(1) if m else ""), (b.group(1).strip() if b else "")


def titulo_publicacao(proj):
    f = proj / "youtube" / "publicacao.md"
    if not f.exists():
        return ""
    for ln in f.read_text(encoding="utf-8", errors="ignore").splitlines():
        if "recomendado" in ln.lower() and "**" in ln:
            m = re.search(r"\*\*(.+?)\*\*", ln)
            if m:
                return m.group(1).strip()
    return ""


rows = []
for mp4 in sorted(ROOT.glob("canais/**/*.mp4")):
    rel = mp4.relative_to(ROOT)
    parts = rel.parts
    if "trabalho" in parts or "original" in parts:
        continue
    if parts[-2] not in ("final", "shorts"):
        continue
    canal = parts[1]
    proj = mp4.parent.parent
    tipo = "short" if parts[-2] == "shorts" else "vídeo"
    antigo = "_antigo" in str(rel)
    serie = parts[2] if len(parts) > 5 else ""
    d, secs = dur(mp4)
    tr, base = titulo_roteiro(proj)
    tp = titulo_publicacao(proj) if tipo == "vídeo" else ""
    capas = ", ".join(sorted(p.name for p in (proj / "youtube").glob("capa_*.jpg"))) if tipo == "vídeo" else ""
    rows.append(dict(canal=canal, serie=serie, projeto=str(proj.relative_to(ROOT)).replace("\\", "/"), tipo=tipo,
                     antigo="sim" if antigo else "", arquivo=mp4.name, duracao=d, segundos=round(secs, 1),
                     tamanho_mb=round(mp4.stat().st_size / 1e6, 1),
                     data=datetime.datetime.fromtimestamp(mp4.stat().st_mtime).strftime("%Y-%m-%d"),
                     titulo_youtube=tp, titulo_roteiro=tr, fonte=base, capas=capas))

with open(ROOT / "registro_videos.csv", "w", newline="", encoding="utf-8-sig") as f:
    w = csv.DictWriter(f, fieldnames=list(rows[0].keys()), delimiter=";")
    w.writeheader(); w.writerows(rows)

hoje = datetime.date.today().strftime("%d/%m/%Y")
out = [f"# Registro de vídeos criados — atualizado em {hoje}", "",
       "Gerado por `_ferramentas/registrar_videos.py` a partir das pastas de cada projeto (pode rodar de novo a qualquer momento).",
       "Planilha com os mesmos dados: `registro_videos.csv` (separador `;`, abre no Excel).", "",
       "Cada projeto guarda: `roteiro/` (cenas.py = roteiro, visual.py = animações), `audio/` (voz e tempos), `youtube/` "
       "(capas + publicacao.md com título, descrição e capítulos) e `final/` (o vídeo pronto). `trabalho/` é só intermediário.", "",
       "## Antes de apagar (depois do backup)", "",
       "| Pode apagar (pesado) | Manter (leve, faz os próximos vídeos funcionarem) |", "|---|---|",
       "| `*/trabalho/` inteiro (segmentos, prévias) | `_ferramentas/`, `ESTILO_COMUM.md`, `LEIA-ME.md`, este registro |",
       "| `*/audio/*.wav` e `*/audio/nova_voz/` (vozes) | `canais/*/ESTILO.md`, `PLANO_*.md`, `PROMPT_AULA_INICIANTE.md` |",
       "| `*/final/*.mp4` e `*/shorts/*.mp4` (vídeos prontos) | `*/roteiro/` (vários `visual.py` importam o de episódios anteriores) |",
       "| | `*/audio/tempos.json`, `*/youtube/`, `*/original/`, `*/assets/`, `*/analise/` |", ""]
tot_v = [r for r in rows if r["tipo"] == "vídeo" and not r["antigo"]]
out += ["## Resumo", "", "| Canal | Vídeos | Shorts | Duração total |", "|---|---|---|---|"]
for k, nome in CANAIS.items():
    v = [r for r in tot_v if r["canal"] == k]
    s = [r for r in rows if r["canal"] == k and r["tipo"] == "short"]
    h = sum(r["segundos"] for r in v)
    out.append(f"| {nome} | {len(v)} | {len(s)} | {int(h // 3600)} h {int(h % 3600 // 60):02d} min |")
h = sum(r["segundos"] for r in tot_v)
out += [f"| **Total** | **{len(tot_v)}** | **{sum(1 for r in rows if r['tipo'] == 'short')}** | **{int(h // 3600)} h {int(h % 3600 // 60):02d} min** |", ""]

for k, nome in CANAIS.items():
    rs = [r for r in rows if r["canal"] == k]
    if not rs:
        continue
    out += [f"## {nome}", "", "| # | Projeto | Título (YouTube recomendado / roteiro) | Duração | Data | Arquivo |", "|---|---|---|---|---|---|"]
    for i, r in enumerate(rs, 1):
        tit = (r["titulo_youtube"] or r["titulo_roteiro"] or "—").replace("|", "·")
        marca = " *(versão antiga)*" if r["antigo"] else ""
        marca += " *(Short)*" if r["tipo"] == "short" else ""
        out.append(f"| {i} | `{r['projeto']}` | {tit}{marca} | {r['duracao']} | {r['data']} | `{r['arquivo']}` |")
    out.append("")

(ROOT / "REGISTRO_DE_VIDEOS.md").write_text("\n".join(out) + "\n", encoding="utf-8")
print(len(rows), "arquivos registrados ·", len(tot_v), "vídeos atuais")
