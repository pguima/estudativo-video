# Short 1 — "2 + 3 × 4 dá 14 ou 20?" (a fila do pronto-socorro resolvendo a conta)
# Base: final/enem_matematica_conjuntos_ep1_ordem_e_sinais.mp4
#   gancho  00:00.0–00:10.4  ("Quanto dá dois mais três vezes quatro? ... Só uma está certa.")
#   trecho  01:30.45–02:02.0 ("Toda conta tem uma fila de prioridade ... fura a fila.")
# Saída: shorts/short1_14_ou_20.mp4 (1080x1920, 30 fps)
from short_base import gerar, TINTA, VERDE, VERMELHO

if __name__ == "__main__":
    gerar("short1_14_ou_20", [(0.0, 10.4), (90.45, 122.0)],
          [("2 + 3 × 4", TINTA)],
          [("dá ", TINTA), ("14", VERDE), (" ou ", TINTA), ("20", VERMELHO), ("?", TINTA)])
