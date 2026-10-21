# Short 2 — "Por que o jogo do dinossauro fica mais rápido?" (a regra recuperada do navegador)
# Base: final/tecnologia_001_rea_engenharia_reversa.mp4
#   gancho  00:18.5–00:31.7  ("Esse é o REA ... passou da marca de duzentas e cinquenta mil estrelas no GitHub.")
#   trecho  03:11.4–03:28.6  ("O segundo é o jogo do dinossauro do navegador. ... com um controle para ajustar a velocidade.")
# Saída: shorts/short2_dinossauro.mp4 (1080x1920, 30 fps)
from short_base import gerar, BRANCO, VERDE

if __name__ == "__main__":
    gerar("short2_dinossauro", [(18.45, 31.65), (191.4, 208.6)],
          [("Por que o ", BRANCO), ("dinossauro", VERDE)],
          [("fica mais rápido?", BRANCO)])
