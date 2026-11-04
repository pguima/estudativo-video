"""Série Top 10 GitHub: lista candidatos do GitHub Trending (mensal) e filtra pelo registro (TOP10_GITHUB.md).

  python3 top10_github.py                         # candidatos: NOVO / ATUALIZADO / REPETIDO
  python3 top10_github.py --registrar EP PASTA    # grava no registro os repositórios de PASTA/original/top10.json
"""
import csv, json, re, sys, urllib.request
from datetime import date
from pathlib import Path

HERE = Path(__file__).parent
REG = HERE / "top10_github_registro.csv"
CAMPOS = ["ep", "data", "pos", "repo", "versao", "estrelas", "ganho_mes", "licenca", "situacao"]


def get(url, raw=False):
    req = urllib.request.Request(url, headers={"User-Agent": "estudativo", "Accept": "application/vnd.github+json"})
    with urllib.request.urlopen(req, timeout=30) as r:
        b = r.read().decode()
    return b if raw else json.loads(b)


def major(v):
    m = re.search(r"\d+", v or "")
    return int(m.group()) if m else None


def registro():
    if not REG.exists():
        return {}
    ult = {}
    for row in csv.DictReader(REG.open(encoding="utf-8")):
        ult[row["repo"].lower()] = row   # a última aparição vale
    return ult


def trending():
    s = get("https://github.com/trending?since=monthly", raw=True)
    out = []
    for a in s.split('<article class="Box-row">')[1:]:
        repo = re.search(r'href="/([^"/]+/[^"/]+)"', a.split("<h2")[1]).group(1)
        g = re.search(r"([\d,]+) stars this month", a)
        out.append((repo, int(g.group(1).replace(",", "")) if g else 0))
    return sorted(out, key=lambda x: -x[1])


def versao(repo):
    try:
        return get(f"https://api.github.com/repos/{repo}/releases/latest").get("tag_name", "")
    except Exception:
        return ""


if __name__ == "__main__":
    if len(sys.argv) > 1 and sys.argv[1] == "--registrar":
        ep, pasta = sys.argv[2], HERE / sys.argv[3]
        novo = not REG.exists()
        with REG.open("a", encoding="utf-8", newline="") as f:
            w = csv.DictWriter(f, CAMPOS)
            if novo:
                w.writeheader()
            for row in json.loads((pasta / "original" / "top10.json").read_text(encoding="utf-8")):
                w.writerow({k: row.get(k, "") for k in CAMPOS} | {"ep": ep, "data": row.get("data") or date.today().isoformat()})
        print("registrado em", REG.name)
        sys.exit()
    reg = registro()
    for repo, ganho in trending():
        r = reg.get(repo.lower())
        v = versao(repo)
        if r is None:
            sit = "NOVO"
        elif major(v) is not None and major(r["versao"]) is not None and major(v) > major(r["versao"]):
            sit = f"ATUALIZADO ({r['versao']} -> {v})"
        else:
            sit = f"REPETIDO (ep {r['ep']}, {r['versao'] or 'sem release'})"
        print(f"{ganho:>7,}  {repo:<45} {v:<22} {sit}")
