# Short 2 — "Por que o infinito é sempre aberto" (proibido para menores de 18)
# Base: final/enem_matematica_conjuntos_ep3_intervalos.mp4
#   trecho  02:29.7–03:08.6  ("E quando não tem ponta do outro lado? ... o lado do infinito é sempre aberto.")
# Saída: shorts/short2_infinito_aberto.mp4 (1080x1920, 30 fps)
from short_base import gerar, TINTA, VERMELHO

if __name__ == "__main__":
    gerar("short2_infinito_aberto", [(149.7, 188.6)],
          [("Infinito com colchete", TINTA)],
          [("fechado? ", TINTA), ("NUNCA", VERMELHO)])
