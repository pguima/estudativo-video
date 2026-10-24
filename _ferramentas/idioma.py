"""Versões do vídeo em outro idioma (canal Tecnativo English = --lang en). O português continua o padrão e não muda nada.

Cada idioma tem o próprio roteiro, voz, tempos, render, som e publicação, lado a lado com os do português:
    roteiro/cenas_en.py   roteiro em inglês: MESMOS ids, blocks e {cues} do cenas.py (o visual.py é o mesmo)
    roteiro/textos_en.py  TEXTOS = {"texto em português": "texto em inglês"} para os textos da TELA (visual.py e capa.py)
                          (None = ainda sem tradução, fica em português; "" = some na versão traduzida)
    roteiro/textos.py     o contrário, para vídeo que nasceu em inglês (visual.py com textos em inglês, ex.: Short 012):
                          TEXTOS = {"texto em inglês": "texto em português"}, aplicado na versão em português
    audio_en/  trabalho_en/  som_en/  youtube_en/      final/<arquivo>_en.mp4

Os textos da tela não são editados no visual.py: ao carregar o visual.py (e o capa.py), toda string que estiver em
TEXTOS é trocada no código-fonte (AST) antes de executar. Por isso a chave tem que ser a string exatamente como está no
código (num f-string, só o pedaço fixo). Cuidado com string usada em lógica (ex.: nm.startswith("PER")): a troca
vale para o código todo. Textos fixos do canal (CTA etc.) ficam em COMUNS, abaixo.

python idioma.py extrair <proj> [--lang en]    cria/completa roteiro/textos_en.py com os textos da tela ainda sem tradução
python idioma.py faltando <proj> [--lang en]   lista o que falta traduzir
python idioma.py capa <proj> [--lang en]       gera as capas traduzidas em youtube_en/
"""
import ast, importlib.util, os, re, sys
from pathlib import Path
from types import SimpleNamespace

LANG = os.environ.get("VIDEO_LANG", "pt")
TTS = {"en": "en-US"}              # código de idioma do Gemini TTS Studio
WHISPER = {"pt": "pt", "en": "en"}

# textos fixos do canal (tech.py e afins), por idioma
COMUNS = {"en": {
    "CURTIR": "LIKE", "INSCREVA-SE": "SUBSCRIBE", "INSCRITO": "SUBSCRIBED", "SININHO": "BELL",
    "Até o próximo vídeo!": "See you in the next video!",
}}

_TEXTOS = {}  # proj -> dict ativo (para tr())


def definir(lang):
    """chamar antes de importar visual/tech; vale também para os processos filhos (env)"""
    global LANG
    LANG = lang or "pt"
    os.environ["VIDEO_LANG"] = LANG


def pega_lang(argv):
    """tira '--lang xx' de uma lista de argumentos (scripts com argv posicional); devolve (lang, resto)"""
    argv = list(argv)
    lang = LANG
    if "--lang" in argv:
        i = argv.index("--lang")
        lang = argv[i + 1]
        del argv[i:i + 2]
    return lang, argv


def pastas(proj, lang=None):
    proj, lang = Path(proj), lang or LANG
    suf = "" if lang == "pt" else f"_{lang}"
    return SimpleNamespace(lang=lang, sufixo=suf, audio=proj / f"audio{suf}", trabalho=proj / f"trabalho{suf}",
                           som=proj / f"som{suf}", youtube=proj / f"youtube{suf}", final=proj / "final",
                           cenas=proj / "roteiro" / f"cenas{suf}.py", textos=proj / "roteiro" / f"textos{suf}.py")


def arquivo_final(nome, lang=None):
    """tecnologia_011_x.mp4 -> tecnologia_011_x_en.mp4"""
    suf = pastas(".", lang).sufixo
    p = Path(nome)
    return f"{p.stem}{suf}{p.suffix}"


def _mod(name, path):
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(m)
    return m


def cenas(proj, lang=None):
    P = pastas(proj, lang)
    if not P.cenas.exists():
        sys.exit(f"falta {P.cenas} (roteiro em '{P.lang}', mesmos ids/blocks/cues do cenas.py)")
    return _mod("cenas", P.cenas)


def textos(proj, lang=None):
    """COMUNS + TEXTOS do projeto; None = sem tradução (o texto continua em português)"""
    P = pastas(proj, lang)
    if P.lang == "pt" and not P.textos.exists():
        return {}
    d = dict(COMUNS.get(P.lang, {}))
    if P.textos.exists():
        d.update({k: v for k, v in _mod("textos", P.textos).TEXTOS.items() if v is not None})
    _TEXTOS[str(Path(proj))] = d
    return d


def tr(s, proj=None):
    """tradução em tempo de execução (tech.py: CTA, despedida)"""
    if LANG == "pt" or not isinstance(s, str):
        return s
    d = COMUNS.get(LANG, {})
    for t in _TEXTOS.values():
        if s in t:
            return t[s]
    return d.get(s, s)


class _Troca(ast.NodeTransformer):
    def __init__(self, d):
        self.d = d

    def visit_Constant(self, node):
        if isinstance(node.value, str) and node.value in self.d:
            return ast.copy_location(ast.Constant(self.d[node.value]), node)
        return node


def carregar(name, path, proj, lang=None, file=None, principal=False):
    """importa um .py (visual.py, capa.py) com os textos traduzidos; em português é um import normal.
    principal=True roda o bloco `if __name__ == "__main__"` (capa.py)"""
    path = Path(path)
    lang = lang or LANG
    spec = importlib.util.spec_from_file_location(name, path)
    m = importlib.util.module_from_spec(spec)
    if lang == "pt" and not pastas(proj, lang).textos.exists():
        spec.loader.exec_module(m)
        return m
    tree = _Troca(textos(proj, lang)).visit(ast.parse(path.read_text(encoding="utf-8"), str(path)))
    m.__file__ = str(file or path)
    if principal:
        m.__name__ = "__main__"
    else:
        sys.modules[name] = m
    exec(compile(ast.fix_missing_locations(tree), str(path), "exec"), m.__dict__)
    return m


# ---------------- textos da tela que faltam traduzir ----------------
_NAO_TEXTO = re.compile(r"^(#[0-9A-Fa-f]{3,8}|\d+(\.\w+)?|[a-z_]+|[\w./-]*\.(py|png|jpg|mp4|wav|svg|ttf)|/\S+|-\S+|\w+@[+-][\d.]+"
                        r"|[\w:=]+=[\w:=]+)$")  # cor, número/cue, peso/alinhamento, arquivo, caminho, flag, efeito, filtro


def candidatos(path):
    """strings do código que parecem texto da tela (ignora docstrings, cores, pesos, cues, nomes de arquivo)"""
    tree = ast.parse(Path(path).read_text(encoding="utf-8"))
    docs = {id(n.body[0].value) for n in ast.walk(tree)
            if isinstance(n, (ast.Module, ast.FunctionDef, ast.ClassDef)) and n.body
            and isinstance(n.body[0], ast.Expr) and isinstance(n.body[0].value, ast.Constant)}
    chaves = set()  # chaves de dicionário de configuração (SOM, C["14.like"]) não são texto
    for n in ast.walk(tree):
        if isinstance(n, ast.Subscript) and isinstance(n.slice, ast.Constant):
            chaves.add(id(n.slice))
    # palavra solta ("trator") só conta como texto quando vai para uma função de texto ou fica numa lista com outros textos
    TXT_FN = {"text", "text_mid", "text_w", "glow_text", "para", "chip", "typed", "head", "pill"}
    solta = set()
    for n in ast.walk(tree):
        fn = getattr(n.func, "id", getattr(n.func, "attr", None)) if isinstance(n, ast.Call) else None
        if fn in TXT_FN:
            i = 0 if fn == "text_w" else 1  # text(c, s, ...) · text_w(s, peso, size)
            solta |= {id(x) for x in n.args[i:i + 1] if isinstance(x, ast.Constant)}

    def e_texto(s, nid):
        if not s.strip() or id(nid) in docs | chaves:
            return False
        if re.search(r"\b\d{1,2}/\d{1,2}/\d{4}\b", s):  # data dd/mm/aaaa
            return True
        if not re.search(r"[A-Za-zÀ-ÿ]", s):
            return False
        return s != s.strip() or not _NAO_TEXTO.match(s) or (re.fullmatch(r"[a-z]+", s) and id(nid) in solta)

    out = []
    for n in ast.walk(tree):
        if isinstance(n, ast.Constant) and isinstance(n.value, str) and e_texto(n.value, n) and n.value not in out:
            out.append(n.value)
    for n in ast.walk(tree):  # tabela [(..., "equipes em solo", ...), (..., "trator", ...)]: a coluna inteira é texto
        if isinstance(n, (ast.Tuple, ast.List)) and n.elts and all(isinstance(x, ast.Tuple) for x in n.elts):
            for col in zip(*[x.elts for x in n.elts]):
                vals = [x.value for x in col if isinstance(x, ast.Constant) and isinstance(x.value, str)]
                if any(v in out and " " in v for v in vals):
                    out += [v for v in vals if re.fullmatch(r"[a-zà-ÿ]+", v) and v not in out]
    return out


def faltando(proj, lang="en"):
    proj = Path(proj)
    d = textos(proj, lang)
    fontes = [proj / "roteiro" / "visual.py", proj / "youtube" / "capa.py"]
    return [s for f in fontes if f.exists() for s in candidatos(f) if s not in d]


def extrair(proj, lang="en"):
    P = pastas(proj, lang)
    novos = faltando(proj, lang)
    vazios = []
    if P.textos.exists():
        vazios = [k for k, v in _mod("textos", P.textos).TEXTOS.items() if v is None]
        corpo = P.textos.read_text(encoding="utf-8").rstrip()
        assert corpo.endswith("}"), f"{P.textos}: TEXTOS = {{...}} precisa ser a última coisa do arquivo"
        corpo = corpo[:-1].rstrip()
    else:
        corpo = (f'"""Textos da TELA em {lang} (visual.py e capa.py). Chave = string exatamente como está no código;\n'
                 f'None = ainda sem tradução (fica em português); "" = some. Ver _ferramentas/idioma.py."""\n\nTEXTOS = {{')
    novos = [s for s in novos if s not in vazios]
    if novos:
        corpo += "\n" + "".join(f"    {s!r}: None,\n" for s in novos)
    P.textos.write_text(corpo.rstrip() + "\n}\n", encoding="utf-8")
    print(f"{P.textos}: {len(novos)} textos novos, {len(vazios) + len(novos)} sem tradução")


def capa(proj, lang="en"):
    """roda o youtube/capa.py com visual e textos traduzidos, salvando em youtube_<lang>/"""
    definir(lang)
    P = pastas(proj, lang)
    P.youtube.mkdir(exist_ok=True)
    sys.path.insert(0, str(Path(__file__).parent))
    sys.path.insert(0, str(proj / "roteiro"))
    carregar("visual", proj / "roteiro" / "visual.py", proj, lang)  # o capa.py faz `import visual`
    carregar("capa", proj / "youtube" / "capa.py", proj, lang, file=P.youtube / "capa.py", principal=True)


if __name__ == "__main__":
    lang, args = pega_lang(sys.argv[1:])
    lang = lang if "--lang" in sys.argv else "en"  # --lang pt: vídeo que nasceu em inglês (roteiro/textos.py)
    cmd, proj = args[0], Path(args[1])
    if cmd == "extrair":
        extrair(proj, lang)
    elif cmd == "faltando":
        f = faltando(proj, lang)
        print("\n".join(repr(s) for s in f) or "tudo traduzido")
    elif cmd == "capa":
        capa(proj, lang)
