# Short 3 — "−3² não é 9" (o erro mais caro da prova)
# Base: final/enem_matematica_conjuntos_ep1_ordem_e_sinais.mp4
#   gancho  07:01.15–07:03.95 ("Essa terceira é o erro mais caro da prova.")
#   trecho  07:05.85–07:45.5  ("Menos três ao quadrado e menos três, entre parênteses, ao quadrado ... Com parênteses, mais nove.")
# Saída: shorts/short3_menos_tres_ao_quadrado.mp4 (1080x1920, 30 fps)
from short_base import gerar, TINTA, VERMELHO

if __name__ == "__main__":
    gerar("short3_menos_tres_ao_quadrado", [(421.15, 423.95), (425.85, 465.5)],
          [("−3² ", TINTA), ("não", VERMELHO), (" é 9", TINTA)],
          [("o erro mais caro da prova", VERMELHO)])
