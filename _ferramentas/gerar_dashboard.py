"""Gera o painel estático dos vídeos prontos (para subir no subdomínio zproapp.webformas.com.br).

Uso: python3 _ferramentas/gerar_dashboard.py
Saída: dashboard/ na raiz do repositório (index.html + dados.js + capas/) e dashboard.zip para enviar à hospedagem
(Hostinger: Gerenciador de arquivos → public_html do subdomínio → enviar o zip → extrair).

Lê: registro_videos.csv (rode antes _ferramentas/registrar_videos.py), youtube/publicacao.md de cada vídeo,
shorts/shortN_publicacao.md de cada Short, youtube/capa_*.jpg e status_videos.csv (raiz).
status_videos.csv guarda o que muda depois de pronto (status, link do YouTube, data). O painel edita isso no
navegador e tem o botão "Baixar status_videos.csv": salve o arquivo na raiz do repositório e rode este script de novo.
Os .mp4 NÃO vão para o painel (ficam no disco / backup); o painel mostra o caminho de cada arquivo.
"""
import csv, json, re, shutil, subprocess, zipfile
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
OUT = ROOT / "dashboard"
CANAIS = {"enem": "ENEM", "seguridade_social": "Seguridade Social", "tecnologia": "Tecnologia", "trading": "Trading"}
STATUS = ROOT / "status_videos.csv"


def bloco(md, titulo):
    """1º bloco ``` depois do cabeçalho ## que começa com `titulo`"""
    m = re.search(rf"^## {re.escape(titulo)}.*?$(.*?)(?=^## |\Z)", md, re.M | re.S)
    if not m:
        return ""
    b = re.search(r"```\w*\n(.*?)```", m.group(1), re.S)
    return b.group(1).strip() if b else ""


def titulos(md):
    m = re.search(r"^## Título.*?$(.*?)(?=^## |^---|\Z)", md, re.M | re.S)
    out = []
    for ln in (m.group(1) if m else "").splitlines():
        t = re.match(r"\d+\.\s+(.*)", ln.strip())
        if t:
            rec = "recomendado" in t.group(1).lower()
            s = re.sub(r"\s*←.*$", "", t.group(1)).replace("**", "")
            s = re.sub(r"\s*\(com capa [A-Z]\)\s*$", "", s).strip()
            out.append({"t": s, "rec": rec})
    return out


def comentario(md):
    c = bloco(md, "Comentário fixado")
    if c:
        return c
    m = re.search(r"\*\*Comentário fixado:\*\*\s*(.+)", md)
    return m.group(1).strip().strip('"“”') if m else ""


def miniatura(src, dst, w=640):
    if not dst.exists() or dst.stat().st_mtime < src.stat().st_mtime:
        subprocess.run(["ffmpeg", "-v", "error", "-y", "-i", str(src), "-vf", f"scale={w}:-2", "-q:v", "4", str(dst)], check=True)


def ler_status():
    if not STATUS.exists():
        return {}
    with open(STATUS, encoding="utf-8-sig") as f:
        return {(r["projeto"], r["arquivo"]): r for r in csv.DictReader(f, delimiter=";")}


def main():
    (OUT / "capas").mkdir(parents=True, exist_ok=True)
    with open(ROOT / "registro_videos.csv", encoding="utf-8-sig") as f:
        rows = list(csv.DictReader(f, delimiter=";"))
    st = ler_status()
    itens, usadas = [], set()
    for r in rows:
        proj = ROOT / r["projeto"]
        slug = r["projeto"].replace("canais/", "").replace("/", "__")
        it = dict(id=f"{slug}__{r['arquivo'][:-4]}", canal=r["canal"], canalNome=CANAIS.get(r["canal"], r["canal"]),
                  serie=r["serie"], projeto=r["projeto"], tipo="short" if r["tipo"] == "short" else "video",
                  antigo=bool(r["antigo"]), arquivo=r["arquivo"], dur=r["duracao"], seg=float(r["segundos"] or 0),
                  mb=float(r["tamanho_mb"] or 0), data=r["data"], fonte=r["fonte"],
                  caminho=f"{r['projeto']}/{'shorts' if r['tipo'] == 'short' else 'final'}/{r['arquivo']}",
                  titulos=[], desc="", tags="", com="", capas=[])
        if it["tipo"] == "short":
            n = re.match(r"(short\d+)_", r["arquivo"])
            pub = proj / "shorts" / f"{n.group(1)}_publicacao.md" if n else None
            fundo = proj / "shorts" / f"{n.group(1)}_fundo.png" if n else None
        else:
            pub, fundo = proj / "youtube" / "publicacao.md", None
        if pub and pub.exists():
            md = pub.read_text(encoding="utf-8", errors="ignore")
            it.update(titulos=titulos(md), desc=bloco(md, "Descrição"), tags=bloco(md, "Tags"), com=comentario(md))
        if not it["titulos"]:
            it["titulos"] = [{"t": r["titulo_youtube"] or r["titulo_roteiro"] or r["arquivo"], "rec": True}]
        # capas: as do vídeo (recomendada primeiro); Short usa o fundo próprio ou a capa do episódio
        capas = sorted((proj / "youtube").glob("capa_*.jpg"))
        if it["tipo"] == "video" and pub and pub.exists():
            rec = re.search(r"`(capa_[^`]+\.jpg)`\s*\|\s*\*\*Recomendad", md)
            if rec:
                capas.sort(key=lambda p: p.name != rec.group(1))
        fontes_capa = capas if it["tipo"] == "video" else ([fundo] if fundo and fundo.exists() else capas[:1])
        for p in fontes_capa:
            nome = f"{slug}__{p.stem}.jpg"
            if nome not in usadas:
                miniatura(p, OUT / "capas" / nome)
                usadas.add(nome)
            it["capas"].append({"src": f"capas/{nome}", "nome": p.name})
        s = st.get((r["projeto"], r["arquivo"]), {})
        it.update(status=s.get("status") or ("arquivado" if it["antigo"] else "pronto"),
                  link=s.get("link_youtube", ""), publicado=s.get("publicado_em", ""), nota=s.get("nota", ""))
        itens.append(it)
    for p in (OUT / "capas").glob("*.jpg"):      # miniaturas de vídeos que saíram do registro
        if p.name not in usadas:
            p.unlink()
    itens.sort(key=lambda x: (x["data"], x["projeto"], x["arquivo"]), reverse=True)
    (OUT / "dados.js").write_text("window.DADOS = " + json.dumps(itens, ensure_ascii=False) + ";\n", encoding="utf-8")
    shutil.copy(Path(__file__).with_name("dashboard_index.html"), OUT / "index.html")
    if not STATUS.exists():   # cria o arquivo de status com todos "pronto"
        with open(STATUS, "w", newline="", encoding="utf-8-sig") as f:
            w = csv.writer(f, delimiter=";")
            w.writerow(["projeto", "arquivo", "status", "link_youtube", "publicado_em", "nota"])
            for it in itens:
                w.writerow([it["projeto"], it["arquivo"], it["status"], "", "", ""])
    z = ROOT / "dashboard.zip"
    with zipfile.ZipFile(z, "w", zipfile.ZIP_DEFLATED) as zf:
        for p in sorted(OUT.rglob("*")):
            if p.is_file():
                zf.write(p, p.relative_to(OUT))
    print(f"{len(itens)} itens · {len(usadas)} capas · {z} ({z.stat().st_size / 1e6:.1f} MB)")


if __name__ == "__main__":
    main()
