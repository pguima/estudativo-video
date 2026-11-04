# conta os caminhos mais curtos numa grade de ruas (só direita ou baixo): força bruta e pela soma das esquinas
from itertools import product


def forca_bruta(cols, rows):
    return sum(1 for m in product("RD", repeat=cols + rows) if m.count("R") == cols)


def esquinas(cols, rows):
    v = [[1] * (cols + 1) for _ in range(rows + 1)]
    for j in range(1, rows + 1):
        for i in range(1, cols + 1):
            v[j][i] = v[j - 1][i] + v[j][i - 1]
    return v


for cols, rows in ((2, 2), (3, 2), (3, 3)):
    v = esquinas(cols, rows)
    assert v[rows][cols] == forca_bruta(cols, rows)
    print(f"{cols} x {rows}: {forca_bruta(cols, rows)} caminhos · esquinas {v}")
v = esquinas(3, 3)
print("diagonal i+j=3 (linha do triângulo de Pascal):", [v[j][3 - j] for j in range(4)])
