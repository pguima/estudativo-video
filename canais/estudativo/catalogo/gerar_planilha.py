"""Gera a planilha de revisão do catálogo do Estudativo."""
from collections import Counter

from openpyxl import Workbook
from openpyxl.styles import Font

import catalogo_lib as lib
import validar_catalogo as val

CAMPOS_MAPA = ("materia", "trilha", "modulo", "camada", "aulas_estimadas", "provas", "observacao")


def _aba(livro, titulo, cabecalho, linhas):
    aba = livro.create_sheet(titulo)
    aba.append(list(cabecalho))
    for celula in aba[1]:
        celula.font = Font(bold=True)
    for linha in linhas:
        aba.append(list(linha))
    for linha in aba.iter_rows():
        for celula in linha:
            if isinstance(celula.value, str):
                celula.data_type = "s"  # texto como texto: "=..." não vira fórmula no Excel
    aba.freeze_panes = "A2"
    return aba


def _resumo(cat):
    linhas = [("Aulas", len(cat.aulas)), ("Playlists", len(cat.playlists))]
    for camada, total in sorted(Counter(a["camada"] for a in cat.aulas).items()):
        linhas.append((f"Aulas: {camada}", total))
    for materia, total in sorted(Counter(a["materia"] for a in cat.aulas).items()):
        linhas.append((f"Aulas: {materia}", total))
    for tipo, total in sorted(Counter(p["tipo"] for p in cat.playlists).items()):
        linhas.append((f"Playlists: {tipo}", total))
    return linhas


def _ordem_das_playlists(cat):
    for playlist in cat.playlists:
        if val.regra_valida(playlist) is None:
            continue
        for posicao, aula in enumerate(lib.aulas_da_playlist(playlist, cat.aulas), 1):
            yield playlist["titulo"], posicao, aula["id"], aula["titulo"]


def gerar(cat, destino, mapa):
    livro = Workbook()
    livro.remove(livro.active)
    _aba(livro, "Resumo", ("Item", "Total"), _resumo(cat))
    _aba(livro, "Mapa geral", CAMPOS_MAPA, ([m[c] for c in CAMPOS_MAPA] for m in mapa))
    _aba(livro, "Aulas", lib.CAMPOS_AULA, ([a[c] for c in lib.CAMPOS_AULA] for a in cat.aulas))
    _aba(livro, "Playlists", lib.CAMPOS_PLAYLIST, ([p[c] for c in lib.CAMPOS_PLAYLIST] for p in cat.playlists))
    _aba(livro, "Ordem das playlists", ("Playlist", "Posição", "ID", "Aula"), _ordem_das_playlists(cat))
    _aba(
        livro, "Cobertura", ("Área", "Assunto", "Aulas", "Justificativa"),
        ((c["area"], c["assunto"], c["aulas"], c["justificativa"]) for c in cat.cobertura),
    )
    livro.save(destino)


def main():
    lib.usar_utf8()
    arquivo_mapa = lib.PASTA / "mapa_geral.csv"
    mapa = lib.ler_csv(arquivo_mapa) if arquivo_mapa.exists() else []
    destino = lib.PASTA / "revisao_catalogo.xlsx"
    cat = lib.carregar()
    erros, _ = val.validar(cat)
    if erros:
        print(f"ATENÇÃO: catálogo com {len(erros)} erros")
    gerar(cat, destino, mapa)
    print(destino)


if __name__ == "__main__":
    main()
