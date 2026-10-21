# Short 3 — "Acima de não é a partir de" (o frete grátis)
# Base: final/enem_matematica_conjuntos_ep3_intervalos.mp4
#   gancho  00:00.0–00:05.26 ("Num gráfico do ENEM, uma bolinha vazia em vez de cheia muda a alternativa correta.")
#   trecho  03:57.3–04:13.6  ("confundir acima de com a partir de. ... A partir de dezoito: o dezoito entra. Bolinha cheia.")
# Saída: shorts/short3_acima_de.mp4 (1080x1920, 30 fps)
from short_base import gerar, TINTA, VERDE, VERMELHO

if __name__ == "__main__":
    gerar("short3_acima_de", [(0.0, 5.26), (237.3, 253.6)],
          [("Frete grátis ", TINTA), ("acima de R$ 100", VERMELHO)],
          [("a compra de 100 ganha?", TINTA)])
