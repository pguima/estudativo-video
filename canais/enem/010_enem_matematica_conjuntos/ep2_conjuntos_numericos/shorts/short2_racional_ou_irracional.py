# Short 2 — "Racional ou irracional? O teste da forma decimal" (acaba, repete ou nenhum dos dois)
# Base: final/enem_matematica_conjuntos_ep2_conjuntos_numericos.mp4
#   trecho  05:21.4–05:41.6  ("esse número é racional ou irracional? ... Três quartos ... É racional.")
#   trecho  05:41.9–05:49.7  ("Um terço ... Isso se chama dízima periódica.")
#   trecho  05:53.2–05:57.3  ("Também é racional: toda dízima periódica tem uma fração que a gera.")
#   trecho  06:00.6–06:15.4  ("E a raiz de dois ... Nem acaba nem repete, irracional.")
# Saída: shorts/short2_racional_ou_irracional.mp4 (1080x1920, 30 fps)
from short_base import gerar, TINTA, AZUL, VERDE, VERMELHO

if __name__ == "__main__":
    gerar("short2_racional_ou_irracional", [(321.4, 341.6), (341.9, 349.65), (353.2, 357.3), (360.6, 375.4)],
          [("Racional", VERDE), (" ou ", TINTA), ("irracional", VERMELHO), ("?", TINTA)],
          [("o teste em 3 perguntas", TINTA)])
