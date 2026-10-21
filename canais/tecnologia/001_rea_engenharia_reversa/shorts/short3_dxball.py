# Short 3 — "IA reconstruiu um jogo de 1996 byte a byte" (DX-Ball: 3.205 testes, 63 bytes)
# Base: final/tecnologia_001_rea_engenharia_reversa.mp4
#   gancho  00:00.0–00:18.2  ("Você já viu um recurso num aplicativo ... e ainda reconstruir o recurso para você?")
#   trecho  03:29.9–03:50.9  ("O terceiro é o mais impressionante: DX-Ball ... os sessenta e três bytes da função compilada.")
# Saída: shorts/short3_dxball.mp4 (1080x1920, 30 fps)
from short_base import gerar, BRANCO, MAGENTA, AMBAR

if __name__ == "__main__":
    gerar("short3_dxball", [(0.0, 18.2), (209.9, 230.95)],
          [("IA reconstruiu um jogo", BRANCO)],
          [("de ", BRANCO), ("1996", MAGENTA), (" byte a byte", AMBAR)])
