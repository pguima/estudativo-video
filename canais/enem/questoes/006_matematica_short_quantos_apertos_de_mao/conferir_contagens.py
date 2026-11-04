# conta os apertos de mão (cada par de pessoas uma vez): força bruta e pela fórmula n × (n − 1) ÷ 2
from itertools import combinations

for n in (4, 5, 10):
    pares = len(list(combinations(range(n), 2)))
    assert pares == n * (n - 1) // 2 == sum(range(n))
    print(f"{n} pessoas: {pares} apertos · {n} × {n - 1} = {n * (n - 1)} (cada aperto contado 2 vezes) · soma {' + '.join(str(k) for k in range(n - 1, 0, -1))}")
