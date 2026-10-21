# Short 1 — "A IA leu o binário da calculadora do Windows" (o botão de porcentagem tem 2 regras)
# Base: final/tecnologia_001_rea_engenharia_reversa.mp4
#   gancho  00:18.5–00:24.9  ("Esse é o REA, de Reverse Engineer Anything: engenharia reversa de qualquer coisa.")
#   trecho  02:47.4–03:10.9  ("A pergunta: como funciona o botão de porcentagem? ... A mesma tecla, dois comportamentos.")
# Saída: shorts/short1_calculadora.mp4 (1080x1920, 30 fps)
from short_base import gerar, BRANCO, CIANO, MAGENTA

if __name__ == "__main__":
    gerar("short1_calculadora", [(18.45, 24.9), (167.4, 190.95)],
          [("A IA leu o ", BRANCO), ("binário", CIANO)],
          [("da calculadora do Windows", MAGENTA)])
