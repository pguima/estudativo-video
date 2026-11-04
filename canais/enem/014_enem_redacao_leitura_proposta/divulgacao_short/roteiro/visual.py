"""Divulgação da série Leitura da Proposta — short. O desenho fica em ../../divulgacao_visual.py (compartilhado)."""
import sys
from pathlib import Path
PROJ = Path(__file__).resolve().parent.parent
sys.path.insert(0, str(PROJ.parent))
from divulgacao_visual import *  # noqa
import divulgacao_visual as _dv
_dv.setup(PROJ)

ARQUIVO_FINAL = "redacao_leitura_proposta_divulgacao_short.mp4"
SOM = dict(intro=False, ganho_trilha=0.36, lufs=-14, bpm=120, sfx=SFX_short)
