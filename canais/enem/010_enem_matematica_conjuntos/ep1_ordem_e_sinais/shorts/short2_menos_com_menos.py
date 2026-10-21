# Short 2 — "Por que menos com menos dá mais" (as dívidas canceladas)
# Base: final/enem_matematica_conjuntos_ep1_ordem_e_sinais.mp4
#   trecho  04:23.6–05:03.5 ("E na multiplicação, o que acontece com os sinais? ... Menos doze dividido por menos quatro, mais três.")
# Saída: shorts/short2_menos_com_menos.mp4 (1080x1920, 30 fps)
from short_base import gerar, TINTA, VERDE

if __name__ == "__main__":
    gerar("short2_menos_com_menos", [(263.6, 303.5)],
          [("Menos com menos", TINTA)],
          [("dá ", TINTA), ("MAIS", VERDE), ("? Por quê?", TINTA)])
