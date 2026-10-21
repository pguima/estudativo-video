# Short 1 — "O colchete é um braço" (abraça ou empurra o número)
# Base: final/enem_matematica_conjuntos_ep3_intervalos.mp4
#   trecho  00:44.2–00:53.7  ("Uma promoção vale de dois a cinco de março. ... As duas pontas entram.")
#   trecho  00:59.95–01:20.7 ("Quando os dois extremos entram, o intervalo é fechado. ... o dois e o cinco entram.")
#   trecho  01:35.2–01:53.5  ("E se as pontas não entram? ... eles empurram o número.")
# Saída: shorts/short1_colchete_braco.mp4 (1080x1920, 30 fps)
from short_base import gerar, TINTA, AZUL, VERDE, VERMELHO

if __name__ == "__main__":
    gerar("short1_colchete_braco", [(44.2, 53.7), (59.95, 80.7), (95.2, 113.5)],
          [("O colchete é um ", TINTA), ("braço", AZUL)],
          [("abraça", VERDE), (" ou ", TINTA), ("empurra", VERMELHO), ("?", TINTA)])
