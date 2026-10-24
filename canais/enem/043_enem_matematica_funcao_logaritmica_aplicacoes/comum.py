"""Peças comuns da série 043 (28-funcao-logaritmica-aplicacoes): reexporta o comum.py da série 019
(tipografia de potências e raízes no expr, frações do 018, fichas, escada, atalho, selo_teste...).
Peças próprias de cada episódio ficam no visual.py dele."""
import importlib.util
from pathlib import Path

_p = Path(__file__).resolve().parent.parent / "019_enem_matematica_potenciacao" / "comum.py"
_s = importlib.util.spec_from_file_location("comum019", _p); _m = importlib.util.module_from_spec(_s); _s.loader.exec_module(_m)
globals().update({k: v for k, v in vars(_m).items() if not k.startswith("__")})
