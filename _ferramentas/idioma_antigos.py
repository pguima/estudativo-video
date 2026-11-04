"""Versões em outro idioma dos episódios de Nós, os Antigos (VIDEO_LANG=en → canal "The Museum of 2526").
O português continua o padrão e não muda nada.

Os scripts do episódio (visual.py, teste_abertura.py, som.py) chamam, logo depois de ajustar o sys.path:
    import idioma_antigos as lingua
    lingua.preparar(globals())
Em outro idioma isso faz duas coisas:
- troca os textos da TELA no código-fonte (AST) de antigos.py, estudo.py, teste_abertura.py, visual.py e youtube.py,
  usando roteiro/textos_<lang>.py: TEXTOS = {"texto em português": "texto traduzido"} (a chave é a string exatamente
  como está no código; num f-string, só o pedaço fixo);
- o script aberto direto na linha de comando roda a versão traduzida de si mesmo.
Pastas: lingua.audio(AQUI) → audio/ ou audio_en/ · lingua.saida(AQUI) → saida/ ou saida_en/

VIDEO_LANG=en python visual.py --render --partes 4   → saida_en/piloto_mudo.mp4
"""
import ast, importlib.abc, importlib.machinery, importlib.util, os, sys
from pathlib import Path

LANG = os.environ.get("VIDEO_LANG", "pt")
SUF = "" if LANG == "pt" else f"_{LANG}"
TRADUZ = {"antigos", "estudo", "teste_abertura", "visual", "youtube"}

# textos fixos do canal, por idioma (logo, placa do salão, vitrine)
COMUNS = {"en": {
    "NÓS, OS ": "THE MUSEUM ", "ANTIGOS": "OF 2526",
    "MUSEU DA ERA DOS ANTIGOS · ANO 2526": "THE AGE OF THE ANCIENTS · CURATED BY LUME",
    "ALA 01 · O QUE SOBROU": "WING 01 · WHAT WAS LEFT",
    "PEÇA Nº 001 · c. 2026 d.C.": "OBJECT NO. 001 · c. 2026 CE",
}}

_textos = None


def audio(aqui):
    return Path(aqui) / f"audio{SUF}"


def saida(aqui):
    return Path(aqui) / f"saida{SUF}"


def roteiro(aqui):
    return Path(aqui) / "roteiro" / f"cenas{SUF}.py"


def textos(proj):
    global _textos
    if _textos is None:
        _textos = dict(COMUNS.get(LANG, {}))
        f = Path(proj) / "roteiro" / f"textos{SUF}.py"
        if f.exists():
            spec = importlib.util.spec_from_file_location("textos_lang", f)
            m = importlib.util.module_from_spec(spec)
            spec.loader.exec_module(m)
            _textos.update({k: v for k, v in m.TEXTOS.items() if v is not None})
    return _textos


class _Troca(ast.NodeTransformer):
    def __init__(self, d):
        self.d = d

    def visit_Constant(self, node):
        if isinstance(node.value, str) and node.value in self.d:
            return ast.copy_location(ast.Constant(self.d[node.value]), node)
        return node


def _codigo(path, proj):
    tree = _Troca(textos(proj)).visit(ast.parse(Path(path).read_text(encoding="utf-8"), str(path)))
    return compile(ast.fix_missing_locations(tree), str(path), "exec")


class _Gancho(importlib.abc.MetaPathFinder, importlib.abc.Loader):
    def __init__(self, proj):
        self.proj = proj

    def find_spec(self, name, path=None, target=None):
        if name not in TRADUZ:
            return None
        spec = importlib.machinery.PathFinder.find_spec(name, path)
        if spec is None or not spec.origin:
            return None
        return importlib.util.spec_from_file_location(name, spec.origin, loader=self)

    def create_module(self, spec):
        return None

    def exec_module(self, m):
        m.__dict__["_TRADUZIDO"] = True
        exec(_codigo(m.__spec__.origin, self.proj), m.__dict__)


def preparar(g, proj=None):
    """chamar no topo do script do episódio, com globals(); proj = pasta do episódio (padrão: a do script)"""
    if LANG == "pt" or g.get("_TRADUZIDO"):
        return
    proj = Path(proj or Path(g["__file__"]).resolve().parent)
    if not any(isinstance(x, _Gancho) for x in sys.meta_path):
        sys.meta_path.insert(0, _Gancho(proj))
    if g.get("__name__") == "__main__":
        novo = {"__name__": "__main__", "__file__": g["__file__"], "_TRADUZIDO": True, "__builtins__": __builtins__}
        exec(_codigo(g["__file__"], proj), novo)
        sys.exit(0)
