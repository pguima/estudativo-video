"""Ficha de produção de uma aula: tudo que o roteiro precisa saber, tirado do catálogo.

py ficha_aula.py MAT-FRA-008                  mostra a ficha
py ficha_aula.py MAT-FRA-008 --marcar pronto  registra a situação em producao.csv
py ficha_aula.py --situacao                   resume producao.csv
"""
import argparse
import csv
import datetime
import sys
from collections import Counter
from pathlib import Path

import catalogo_lib as lib

ARQUIVO_PRODUCAO = lib.PASTA / "producao.csv"
COLUNAS_PRODUCAO = ("id", "estado", "data")
ESTADOS = ("roteiro", "voz", "render", "pronto", "publicado")


def ler_producao(caminho=ARQUIVO_PRODUCAO):
    caminho = Path(caminho)
    if not caminho.exists():
        return {}
    return {linha["id"]: linha["estado"] for linha in lib.ler_csv(caminho, COLUNAS_PRODUCAO)}


def marcar(id, estado, caminho=ARQUIVO_PRODUCAO, hoje=None):
    if estado not in ESTADOS:
        raise ValueError(f"estado inválido: {estado} (use {', '.join(ESTADOS)})")
    caminho = Path(caminho)
    linhas = lib.ler_csv(caminho, COLUNAS_PRODUCAO) if caminho.exists() else []
    data = hoje or datetime.date.today().isoformat()
    for linha in linhas:
        if linha["id"] == id:
            linha["estado"], linha["data"] = estado, data
            break
    else:
        linhas.append({"id": id, "estado": estado, "data": data})
    with open(caminho, "w", encoding="utf-8-sig", newline="") as arquivo:
        saida = csv.DictWriter(arquivo, COLUNAS_PRODUCAO, extrasaction="ignore")
        saida.writeheader()
        saida.writerows(linhas)


def cadeia(id, por_id):
    """todos os pré-requisitos, diretos e indiretos, na ordem do curso"""
    vistos, pilha = set(), list(lib.lista(por_id[id]["prereqs"]))
    while pilha:
        atual = pilha.pop()
        if atual not in vistos:
            vistos.add(atual)
            pilha.extend(lib.lista(por_id[atual]["prereqs"]))
    ordem = {aula_id: i for i, aula_id in enumerate(por_id)}
    return [por_id[a] for a in sorted(vistos, key=ordem.get)]


def montar_ficha(cat, id, producao=None):
    por_id = {a["id"]: a for a in cat.aulas}
    if id not in por_id:
        raise KeyError(f"aula não encontrada no catálogo: {id}")
    aula = por_id[id]
    trilha = [a for a in cat.aulas if a["materia"] == aula["materia"] and a["trilha"] == aula["trilha"]]
    i = trilha.index(aula)
    playlists = []
    for p in cat.playlists:
        ids = [a["id"] for a in lib.aulas_da_playlist(p, cat.aulas)]
        if id in ids:
            playlists.append(dict(titulo=p["titulo"], tipo=p["tipo"], posicao=ids.index(id) + 1, total=len(ids)))
    return dict(
        aula=aula,
        diretos=[por_id[a] for a in lib.lista(aula["prereqs"])],
        cadeia=cadeia(id, por_id),
        anterior=trilha[i - 1] if i else None,
        proxima=trilha[i + 1] if i + 1 < len(trilha) else None,
        playlists=playlists,
        producao=producao or {},
    )


def texto_ficha(f):
    a, prod = f["aula"], f["producao"]
    situacao = lambda x: prod.get(x["id"], "não gravada")
    saida = [
        f"{a['id']} · {a['titulo']}",
        f"{a['materia']} · {a['trilha']} · {a['modulo']} · {a['camada']} · {a['tipo']}",
        a["habilidade"],
        f"Provas: {a['provas'].replace(';', ', ')} · busca: {a['termo_busca']}",
        "",
        "Pré-requisitos diretos (pode lembrar e pode usar):",
    ]
    saida += [f"  {x['id']} [{situacao(x)}] {x['titulo']}: {x['habilidade']}" for x in f["diretos"]] or ["  nenhum"]
    saida += ["", f"Já ensinado antes desta aula ({len(f['cadeia'])}; o resto só pode ser citado como assunto de outra aula):"]
    saida += [f"  {x['id']} {x['titulo']}" for x in f["cadeia"]] or ["  nada"]
    saida += ["", "Vizinhas na trilha:"]
    for nome, x in (("anterior", f["anterior"]), ("próxima", f["proxima"])):
        saida.append(f"  {nome}: {x['id']} [{situacao(x)}] {x['titulo']}" if x else f"  {nome}: nenhuma")
    saida += ["", "Playlists:"]
    saida += [f"  {p['titulo']} ({p['tipo']}, {p['posicao']}ª de {p['total']})" for p in f["playlists"]]
    return "\n".join(saida)


def main(argv=None):
    lib.usar_utf8()
    ap = argparse.ArgumentParser(description=__doc__)
    ap.add_argument("id", nargs="?")
    ap.add_argument("--marcar", choices=ESTADOS)
    ap.add_argument("--situacao", action="store_true")
    a = ap.parse_args(argv)
    if a.situacao:
        contagem = Counter(ler_producao().values())
        print(", ".join(f"{e}: {contagem[e]}" for e in ESTADOS))
        return 0
    if not a.id:
        ap.error("informe o id da aula")
    try:
        ficha = montar_ficha(lib.carregar(), a.id, ler_producao())
    except KeyError as erro:
        print(erro.args[0], file=sys.stderr)
        return 1
    if a.marcar:
        marcar(a.id, a.marcar)
        print(f"{a.id}: {a.marcar}")
    else:
        print(texto_ficha(ficha))
    return 0


if __name__ == "__main__":
    sys.exit(main())
