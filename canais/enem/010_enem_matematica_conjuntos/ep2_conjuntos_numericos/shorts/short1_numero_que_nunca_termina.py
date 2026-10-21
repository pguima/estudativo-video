# Short 1 — "O número que nunca termina" (a diagonal do quadrado e a raiz de dois)
# Base: final/enem_matematica_conjuntos_ep2_conjuntos_numericos.mp4
#   gancho  00:00.0–00:04.9  ("Existe um número que nunca termina e nunca se repete.")
#   trecho  03:01.2–03:43.3  ("Será que fração resolve tudo? ... decimais infinitos, que não se repetem.")
# Saída: shorts/short1_numero_que_nunca_termina.mp4 (1080x1920, 30 fps)
from short_base import gerar, TINTA, AZUL, VERMELHO

if __name__ == "__main__":
    gerar("short1_numero_que_nunca_termina", [(0.0, 4.87), (181.2, 223.3)],
          [("O número que", TINTA)],
          [("NUNCA", VERMELHO), (" termina", TINTA)])
