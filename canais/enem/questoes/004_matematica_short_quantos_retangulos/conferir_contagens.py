# conta retângulos numa grade (força bruta: 4 cantos que sejam pontos da grade e lados sobre linhas desenhadas)
from itertools import combinations


def conta(cols, rows, so_quadrados=False):
    n = 0
    for x0, x1 in combinations(range(cols + 1), 2):
        for y0, y1 in combinations(range(rows + 1), 2):
            if not so_quadrados or x1 - x0 == y1 - y0:
                n += 1
    return n


print("faixa 4 pedaços:", conta(4, 1), "· 3 colunas x 2 andares:", conta(3, 2), "· grade 3x3:", conta(3, 3),
      "(só quadrados:", conta(3, 3, True), ")")
