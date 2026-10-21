# Short 3 — "√9 é irracional? Não!" (ter raiz não é ser irracional)
# Base: final/enem_matematica_conjuntos_ep2_conjuntos_numericos.mp4
#   trecho  06:45.6–07:22.2  ("Então todo número com raiz é irracional? Não. ... Raiz de quadrado perfeito dá número certinho: é racional.")
# Saída: shorts/short3_raiz_de_nove.mp4 (1080x1920, 30 fps)
from short_base import gerar, TINTA, VERDE, VERMELHO

if __name__ == "__main__":
    gerar("short3_raiz_de_nove", [(405.6, 442.2)],
          [("√9 é irracional?", TINTA)],
          [("NÃO!", VERMELHO), (" É racional", VERDE)])
