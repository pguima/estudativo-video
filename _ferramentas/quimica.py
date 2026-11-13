"""Kit visual de Química do Estudativo: peças animáveis no padrão de editorial.py. Leia só esta docstring para usar.

Uso no visual.py:  import editorial as E;  import quimica as Q;  E.usar("Química", "<Trilha>")  (antes de desenhar).
O símbolo da Química (anel hexagonal com volume, como o benzeno) é E.hexagono(c, cx, cy, r) / E.simbolo(c, cx, cy, r);
capas: E.capa_modelo(c, "Química", ...). A linguagem visual completa (cores por papel, o que vai no palco) está no cabeçalho do
visual.py da QUI-MIS-001: leia antes da primeira aula de uma trilha nova.
Peças com (c, t, t0, ...) entram sozinhas a partir de t0 (crescem, ganham foco, átomos pulam); as sem t são desenhos parados
com a = alfa (embrulhe em E.foco / E.saida para entrar e sair). Coordenadas em pixels (1920x1080, y para baixo).
escuro=True = sobre o palco (E.palco): a tinta vira branco e a cor da matéria vira E.CLARO.

ARMADILHA DE FONTE: a serifada itálica ("i", "s") NÃO tem subscrito, sobrescrito, seta, ⇌, Δ, grego, "²", "₂". Nunca ponha
fórmula química em E.frase com "i": escreva a parte química com Q.formula / Q.formula_em (grotesca "g" ou "b", com o índice e a
carga desenhados como texto menor deslocado). Em E.frase, use só palavras; a fórmula vai ao lado, com Q.formula.

CORES FIXAS
  Q.cor_el("O") → cor do elemento (modelo CPK): H branco, C cinza-escuro, O vermelho, N azul, Cl verde, S amarelo, P laranja,
      Na/K roxo, Fe laranja-escuro, Cu cobre, gases nobres ciano; os outros, rosa. Vale para bolinha, nunca para texto de erro.
  Q.ELETRON (azul) = elétron e par de elétrons.   Q.AGUA = água/solução incolor.   Q.VIDRO = vidraria.   Q.LIGA = vareta.
  E.COR (turquesa) = o que está sendo ensinado: o índice da vez, o núcleo, a seta da reação, a família destacada.
  Vermelho e verde de erro/acerto continuam com risco (E.risco) ou selo (E.selo), porque O e Cl também são vermelho e verde.

TEXTO QUÍMICO (fórmula, íon, equação)
  Escrita: "H2O", "SO4^2-", "Na^+", "Ca(OH)2", "C6H12O6", "2 H2O", "CuSO4·5H2O", "e^-", "^{23}_{11}Na" (isótopo) ou com
  Unicode ("H₂O", "SO₄²⁻"). Número logo depois de símbolo ou de ")" vira índice; número no começo da espécie vira coeficiente;
  "^{...}" ou ⁺⁻ ²... vira carga (empilhada sobre o índice: SO₄²⁻). Estados: "(s)", "(l)", "(g)", "(aq)" saem menores e cinza.
  Setas: "->" ou "→" e "<=>" ou "⇌"; "->{Δ}" põe um rótulo em cima da seta. Separe as espécies com " + ".
  formula(c, s, x, y, size, cor=None, a=1, align="left", estilo="g", cores=None, escuro=False) → largura. y = linha de base.
      cores = {"H": cor} pinta o símbolo e o índice dele; {0: cor} pinta o grupo 0 (veja grupos); {"indice": cor} pinta todos
      os índices; {"coef": cor} os coeficientes; {"carga": cor} as cargas.
  formula_em(c, t, t0, s, x, y, size, ...) — entra com foco.  formula_passo(c, t, t0, s, ..., tg=None, passo=0.25) — grupo a grupo.
  formula_um(c, t, t0, s, t1, x, y, size, quais=None) — em t1 a fórmula ganha o índice 1 que não se escreve, em cinza e numa
      caixa tracejada (as letras da direita abrem espaço). com_um(s) → ("H_{2}S_{1}O_{4}", grupos que ganharam o 1).
      cores={("indice", g): cor} pinta só o índice do grupo g.
  grupos(s, x, y, size, align="left") → [dict(s="H", tipo="el"|"coef"|"par", n=2, x0, x1, cx, topo, base, i)] — a caixa de
      cada símbolo com o índice dele, para caixa pontilhada, seta ou risco em cima de um pedaço da fórmula.
  contar(s) → {"C": 2, "H": 6, "O": 1}: a contagem de verdade (parênteses, coeficiente, hidrato). Use em assert.
  lados(eq) → (contagem dos reagentes, contagem dos produtos): assert lados(eq)[0] == lados(eq)[1] confere o balanceamento.
  equacao(c, t, t0, s, x, y, size, align="center", tl=None, passo=0.45, cores=None) — cada termo (espécie, "+", seta) entra no
      seu instante tl[k]; a seta cresce. Devolve o centro x de cada espécie.  centros(s, x, y, size, align) faz só a conta.
  sob_termos(c, t, s, x, y, size, linhas, tl=None, dy=None, size_l=None, rotulos=None, cores_l=None) — linhas embaixo de cada
      espécie da equação (proporção em mol, massas): linhas = [["2 mol", "1 mol", "2 mol"], ["4 g", "32 g", "36 g"]].
  inventario(c, t, t0, itens, x, y, size=64, tl=None, total=None, nomes=True, escuro=False) — a contagem de uma fórmula em
      linhas: bolinha do elemento + número + nome ("2 carbonos"). itens = [("C", 2), ...] ou contar(s).items(); total = instante
      da linha "= 9 átomos" (soma conferida aqui).
ÁTOMOS E MOLÉCULAS (bola-vareta)
  atomo(c, cx, cy, r, s, a=1, rotulo=True, escuro=False, cor=None) — esfera com volume na cor do elemento e o símbolo dentro.
  atomo_em(c, t, t0, cx, cy, r, s, d=0.5) — pula de tamanho zero até r.
  molecula(c, t, t0, mol, cx, cy, escala=110, passo=0.18, separa=0, rotulos=True, giro=0, a=1, escuro=False, tl=None) → pontos
      dos átomos na tela. mol = nome pronto (Q.MOLECULAS: H2, O2, O3, N2, Cl2, H2O, H2O2, CO, CO2, CH4, NH3, HCl, C2H6O,
      C2H4, C2H6, H2SO4) ou dict(atomos=[("O", x, y), ...], ligacoes=[(i, j, ordem)]) em unidades de ligação (≈ 1).
      Átomos pulam em fila (tl = instante de cada um), varetas surgem quando as duas pontas existem; ordem 2 ou 3 = dupla/tripla.
      separa = 0..1 afasta os átomos do centro e some com as varetas (a molécula se desfaz). molecula_desenho(...) = parada.
  particulas(c, t, x, y, w, h, n, estado="liquido"|"solido"|"gas", tipos=None, r=14, semente=1, a=1, escuro=False) —
      partículas mexendo numa caixa: sólido vibra em grade, líquido escorrega no fundo, gás voa e bate nas paredes.
      tipos = [(cor ou símbolo, fração), ...] para mistura (água + sal...).
ESTRUTURA DO ÁTOMO E TABELA
  bohr(c, t, t0, cx, cy, camadas=[2, 8, 1], r0=110, dr=70, s=None, te=None, gira=0.35, nomes=False, escuro=False) — núcleo na
      cor da matéria, camadas em fio fino, elétrons azuis entrando um a um (te = instante de cada camada); nomes = K, L, M...
  distribuicao(Z) → [("1s", 2), ("2s", 2), ...] na ordem de Pauling (sem as exceções Cr, Cu).  camadas(Z) → [2, 8, 1].
      dist_texto(Z) → "1s^2 2s^2 2p^6 3s^1" (escreva com Q.formula).
  pauling(c, t, t0, x, y, size=58, Z=None, passo=0.35, setas=True, escuro=False) → lista dos subníveis preenchidos. Diagrama
      com as diagonais desenhadas em ordem; com Z, cada subnível ganha o expoente quando a seta passa e o último fica na cor.
  tabela(c, t, t0, x, y, cel=62, periodos=(1, 7), grupos_=(1, 18), familia=None, periodo=None, destaque=(), numeros=True,
      z=False, d=0.9, escuro=False) → pos(s) = centro da célula do símbolo. Recorte da tabela periódica (sem a faixa La–Lu e
      Ac–Lr, que fica como "57–71"/"89–103"); familia = número do grupo (1 a 18) e periodo = 1 a 7 pintam na cor da matéria.
LEWIS, ESTRUTURAL E BASTÃO
  simbolo_lewis(c, s, cx, cy, size, n, a=1, escuro=False) — símbolo com n elétrons de valência em volta (um por lado, depois pares).
  lewis(c, t, t0, atomos, ligacoes, cx, cy, escala=150, size=96, pontos=False, tl=None, tp=None, escuro=False) → pontos.
      atomos = [("O", x, y, [ângulos dos pares livres])], ângulos em graus (0 = direita, 90 = cima). ligacoes = [(i, j, ordem)]
      como traços (fórmula estrutural); pontos=True desenha a ligação como pares de elétrons. Sem pares livres = estrutural plana.
  bastao(c, t, t0, pts, cx, cy, escala=110, duplas=(), triplas=(), rotulos=None, d=1.0, numeros=None, escuro=False) — fórmula de
      linha: pts em unidades (use zigzag(n)), cada vértice é um carbono; rotulos = {i: "OH"} põe o heteroátomo no vértice i;
      duplas = {(i, j)}; numeros = instante em que cada carbono ganha bolinha e número (para contar os C escondidos).
  zigzag(n, ang=30) → n pontos de cadeia em zigue-zague, centrados em 0.
LABORATÓRIO
  bequer(c, t, t0, cx, yb, w=280, h=320, nivel=0.6, cor=Q.AGUA, te=None, d=1.2, graduacao=True, rotulo=None, particulas=None,
      escuro=False) — vidro entra com foco; o líquido enche de 0 até nivel a partir de te (None = já cheio). cor pode ser
      função de t: use muda_cor(t, t1, cor_a, cor_b, d) para o indicador virar. particulas = dict(n, estado, tipos, r).
  erlenmeyer(...) e tubo(c, t, t0, cx, yb, w=96, h=330, ...) — mesmos parâmetros.  gotas(c, t, t0, x, y0, y1, n=3, cor=...,
      intervalo=0.55) — gotas caindo de um conta-gotas (conta_gotas(c, x, y, a, cor) desenha o conta-gotas com a ponta em (x, y)).
  cor_ph(ph) → cor do indicador universal.  cor_indicador(nome, ph) para "fenolftaleina", "tornassol", "metilorange".
  escala_ph(c, t, t0, x, y, w, h=64, marca=None, tm=None, rotulos=True, escuro=False) — faixa de 0 a 14; marca = pH da seta.
GRÁFICOS (sobre F.grafico / E.plano / E.curva: mesma tinta e mesma entrada dos gráficos de Matemática e Física)
  energia(c, t, t0, x, y, w, h, er=60, ep_=20, pico=100, ea=None, dh=None, cat=None, rotulos=("reagentes", "produtos"),
      d=1.4, escuro=False) → Y(e). Caminho da reação: patamar dos reagentes, morro, patamar dos produtos. ea/dh = instante das
      setas de Ea (à esquerda do pico) e ΔH (com o sinal, FORA da caixa: deixe ~240 px livres à direita); cat = pico com
      catalisador (tracejado). Energias em unidades livres. ΔH < 0 sai em azul (exotérmica), ΔH > 0 em âmbar (endotérmica).
  aquecimento(c, t, t0, x, y, w, h, pf, pe, tmin, tmax, faixas=None, minutos=10, rotulos=True, d=2.0, escuro=False) → (X, Y).
      Curva de aquecimento com eixos próprios (sem grade; PF e PE tracejados e escritos no eixo): com faixas=None é substância
      pura (dois patamares); faixas = ((f0, f1), (e0, e1)) faz a mistura (s + l, l + g subindo).
  solubilidade(c, t, t0, x, y, w, h, curvas, tmax=100, smax=120, d=1.2, escuro=False) → P. curvas = [dict(nome="KNO3",
      pts=[(0, 13), (20, 32), ...], cor=None)]: cada curva é a interpolação dos pontos de tabela, com o nome na ponta.
ELETROQUÍMICA
  pilha_daniell(c, t, t0, cx, cy, metais=("Zn", "Cu"), solucoes=("ZnSO4", "CuSO4"), te=None, ddp="1,10 V", polos=True,
      escuro=False) — dois béqueres, placas, fio por cima com o voltímetro, ponte salina e elétrons andando do ânodo (−) para o
      cátodo (+) a partir de te.  eletrons(c, t, t0, pts, vel=150, espaco=130, r=14) — elétrons andando por qualquer fio.
CÁLCULO (como na Matemática: colunas com cabeçalho e a cruz do produto cruzado)
  regra_tres(c, t, t0, cab, linhas, x, y, size=84, tl=None, tcruz=None, tx=None, conta=None, res=None, dx=520, dy=None,
      escuro=False) — cab = ("mol", "massa"), linhas = [("1 mol", "18 g"), ("2 mol", "x")]; "x" sai na cor da matéria; tcruz
      traça a cruz; conta = "x = 2 · 18" aparece em tx; res = "36 g" vai na esfera. Confere a proporção (assert) quando os
      quatro valores são números.
Apoio: muda_cor(t, t1, a, b, d=1.0), seta_reacao(c, x0, x1, y, size, cor, a=1, p=1, eq=False, rotulo=None), NOMES (nome em
português de cada símbolo), RAIO (raio relativo de cada átomo), cor_el(s).

ARMADILHAS JÁ VISTAS
  - Carga sem chave funciona ("SO4^2-", "Na^+"), mas "Na+" sem ^ vira o "+" que separa espécies.
  - Os grupos (grupos, cores={i: ...}) contam coeficiente, símbolo e parêntese, na ordem: em "2 C2H6O", 0 = 2, 1 = C, 2 = H, 3 = O.
  - O "1" que não se escreve não cabe por cima da letra seguinte: use formula_um, que reescreve a fórmula com o 1 (S₁ em H₂SO₄).
  - M.rrect(..., color=None, stroke=...) pinta BRANCO por baixo (motor usa CARD): para só o contorno, desenhe com M.paint(stroke=).
  - molecula(c, t, None, ...) = desenho parado (capas); molecula_desenho faz o mesmo com alfa.
  - Cor de elemento (O vermelho, Cl verde) não é erro/acerto: marque o erro com E.risco ou E.selo.
"""
import math
import random
import re
from fractions import Fraction
from functools import lru_cache

import skia

import editorial as E
import fisica as F
import motor as M
from editorial import W, H, TINTA, TINTA2, CINZA, FIO, PAPEL, ep, prog, lerp, ease_io, ease_out, ease_back, clamp, mix, hexc
from editorial import foco, centro, escreve, larg

BR = "#FFFFFF"
ELETRON = "#1F6FEB"   # elétron e par de elétrons (o mesmo azul da carga negativa na Física)
AGUA = "#BFE3F2"      # água / solução incolor
VIDRO = "#5B6470"     # contorno da vidraria
LIGA = "#B9BCC2"      # vareta da ligação
NEUTRON = "#9AA0A8"

COR_EL = {
    "H": "#F7F7F5", "C": "#3A3B40", "O": "#E5322D", "N": "#2F64D6", "F": "#8FD14F", "Cl": "#2DB24A", "Br": "#9E2A1E",
    "I": "#6B2FA0", "S": "#F0C419", "P": "#F28C28", "Na": "#8E59D9", "K": "#7A3FC2", "Li": "#B57EDC", "Mg": "#2E8B57",
    "Ca": "#3D9B5B", "Fe": "#D9732A", "Cu": "#C87533", "Zn": "#7D8AA6", "Al": "#A8B0BA", "Ag": "#C0C0C8", "Au": "#E6B422",
    "Pb": "#575C66", "Hg": "#B8B8C8", "He": "#4FC9D9", "Ne": "#4FC9D9", "Ar": "#4FC9D9", "Kr": "#4FC9D9", "Xe": "#4FC9D9",
    "B": "#F4A6A0", "Si": "#C9A878", "Co": "#3F5FBF", "Ni": "#5FA05F", "Mn": "#9C7AC7", "Cr": "#8A99C7", "Ba": "#2FA36B",
    "Sn": "#8C93A0", "U": "#2E8B57",
}
RAIO = {"H": 0.62, "C": 0.84, "N": 0.82, "O": 0.8, "F": 0.74, "Cl": 0.98, "Br": 1.05, "I": 1.15, "S": 1.0, "P": 1.0,
        "Na": 1.15, "K": 1.3, "Li": 1.0, "Mg": 1.1, "Ca": 1.2, "Fe": 1.0, "Cu": 1.0, "He": 0.6, "Ne": 0.7}
NOMES = {"H": "hidrogênio", "He": "hélio", "Li": "lítio", "C": "carbono", "N": "nitrogênio", "O": "oxigênio", "F": "flúor",
         "Ne": "neônio", "Na": "sódio", "Mg": "magnésio", "Al": "alumínio", "Si": "silício", "P": "fósforo", "S": "enxofre",
         "Cl": "cloro", "Ar": "argônio", "K": "potássio", "Ca": "cálcio", "Fe": "ferro", "Cu": "cobre", "Zn": "zinco",
         "Br": "bromo", "Ag": "prata", "I": "iodo", "Au": "ouro", "Hg": "mercúrio", "Pb": "chumbo", "Co": "cobalto",
         "Ni": "níquel", "Mn": "manganês", "Cr": "cromo", "Ba": "bário", "Sn": "estanho", "U": "urânio", "B": "boro"}


def _borda_rr(c, x, y, w, h, r, cor, a, largura=3):
    if a > 0:
        c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), r, r), M.paint(cor, a, stroke=largura))


def cor_el(s):
    return COR_EL.get(s, "#E070C0")


def _tinta(escuro):
    return BR if escuro else TINTA


def _cor(escuro):
    return E.CLARO if escuro else E.COR_TEXTO


def muda_cor(t, t1, a, b, d=1.0):
    """cor que vira de a para b a partir de t1, em d segundos (indicador mudando)"""
    return mix(a, b, ease_io(prog(t, t1, d)))


def _resolve_cor(cor, t):
    return cor(t) if callable(cor) else cor


# =====================================================================================================================
# texto químico
# =====================================================================================================================
_SUBS, _SUPS = "₀₁₂₃₄₅₆₇₈₉", "⁰¹²³⁴⁵⁶⁷⁸⁹"
_ESTADOS = re.compile(r"\((s|l|g|aq|v)\)")


def _normaliza(s):
    """Unicode (H₂O, SO₄²⁻) → escrita do kit (H_{2}O, SO_{4}^{2-}); -> e <=> viram → e ⇌"""
    out, i = [], 0
    while i < len(s):
        ch = s[i]
        if ch in _SUBS or ch == "ₙ":
            buf = ""
            while i < len(s) and (s[i] in _SUBS or s[i] == "ₙ"):
                buf += str(_SUBS.index(s[i])) if s[i] in _SUBS else "n"
                i += 1
            out.append("_{" + buf + "}")
        elif ch in _SUPS or ch in "⁺⁻":
            buf = ""
            while i < len(s) and (s[i] in _SUPS or s[i] in "⁺⁻"):
                buf += str(_SUPS.index(s[i])) if s[i] in _SUPS else ("+" if s[i] == "⁺" else "-")
                i += 1
            out.append("^{" + buf + "}")
        else:
            out.append(ch)
            i += 1
    return "".join(out).replace("<=>", "⇌").replace("->", "→")


def _chave(s, i):
    """s[i] == "{": devolve (conteúdo, posição depois do })"""
    j = s.index("}", i)
    return s[i + 1:j], j + 1


@lru_cache(None)
def _tokens(s):
    """lista de (tipo, valor): el, sub, sup, presub, presup, coef, est, txt, mais, esp, seta, eq"""
    s = _normaliza(s)
    toks, i, inicio = [], 0, True
    while i < len(s):
        ch = s[i]
        if ch == " ":
            toks.append(("esp", " "))
            inicio, i = True, i + 1
        elif ch in "→⇌":
            rot, i = None, i + 1
            if i < len(s) and s[i] == "{":
                rot, i = _chave(s, i)
            toks.append(("seta" if ch == "→" else "eq", rot))
            inicio = True
        elif ch in "_^":
            if s[i + 1] == "{":
                v, i = _chave(s, i + 1)
            else:
                m = re.compile(r"\d*[+\-−]|\d+|.").match(s, i + 1)
                v, i = m.group(0), m.end()
            k = "sub" if ch == "_" else "sup"
            toks.append((("pre" + k) if inicio else k, v))
        elif ch.isupper():
            j = i + 1
            if j < len(s) and s[j].islower():
                j += 1
            toks.append(("el", s[i:j]))
            inicio, i = False, j
        elif ch.isdigit():
            j = i
            while j < len(s) and (s[j].isdigit() or (s[j] == "," and inicio and j + 1 < len(s) and s[j + 1].isdigit())):
                j += 1
            toks.append(("coef" if inicio else "sub", s[i:j]))
            i = j
        elif ch == "(" and _ESTADOS.match(s, i):
            m = _ESTADOS.match(s, i)
            toks.append(("est", m.group(0)))
            i = m.end()
        elif ch == "+":
            toks.append(("mais", "+"))
            inicio, i = True, i + 1
        elif ch == "·":
            toks.append(("txt", "·"))
            inicio, i = True, i + 1
        else:
            toks.append(("txt", ch))
            inicio = ch in "(["
            if ch in ")]":
                inicio = False
            i += 1
    return tuple(toks)


def _carga(v):
    return v.replace("-", "−")


def _larg_seta(rot, size):
    return max(size * 1.5, (larg(rot, "b", size * 0.42) + size * 0.5) if rot else 0)


@lru_cache(None)
def _layout(s, size, estilo="g"):
    """itens posicionados a partir de x = 0: dict(k, s, x, w, size, dy, grupo, termo). Devolve (itens, largura, grupos)"""
    toks = _tokens(s)
    itens, grupos = [], []
    x, termo, grupo = 0.0, 0, -1
    ss, dys = size * 0.6, size * 0.25    # índice
    sp, dyp = size * 0.56, -size * 0.52  # carga
    ultimo_sub = None
    pre = []
    ap = E.APERTO[estilo] * size

    def novo_grupo(tipo, txt, x0):
        grupos.append(dict(s=txt, tipo=tipo, n=1, x0=x0, x1=x0, termo=termo, i=len(grupos)))
        return len(grupos) - 1

    for n_, (k, v) in enumerate(toks):
        prox = toks[n_ + 1] if n_ + 1 < len(toks) else ("", "")
        if k == "esp":
            x += size * 0.24
            ultimo_sub = None
        elif k in ("seta", "eq"):
            x += size * 0.12
            termo += 1
            w = _larg_seta(v, size)
            itens.append(dict(k=k, s=v, x=x, w=w, size=size, dy=0, grupo=-1, termo=termo))
            x += w + size * 0.12
            termo += 1
            ultimo_sub = None
        elif k == "mais":
            termo += 1
            w = larg("+", estilo, size)
            itens.append(dict(k="mais", s="+", x=x + size * 0.04, w=w, size=size, dy=0, grupo=-1, termo=termo))
            x += w + size * 0.08
            termo += 1
            ultimo_sub = None
        elif k in ("presub", "presup"):
            pre.append((k, v))
        elif k == "el":
            if pre:  # isótopo: massa em cima, número atômico embaixo, alinhados à direita
                wp = max(larg(v_, estilo, ss) for _, v_ in pre)
                for k_, v_ in pre:
                    w_ = larg(v_, estilo, ss)
                    itens.append(dict(k="pre", s=v_, x=x + wp - w_, w=w_, size=ss, dy=dyp if k_ == "presup" else dys + size * 0.02,
                                      grupo=len(grupos), termo=termo))
                x += wp + size * 0.05
                pre = []
            grupo = novo_grupo("el", v, x)
            w = larg(v, estilo, size)
            itens.append(dict(k="el", s=v, x=x, w=w, size=size, dy=0, grupo=grupo, termo=termo))
            x += w + ap + size * 0.02
            grupos[grupo]["x1"] = x - ap
            ultimo_sub = None
        elif k == "sub":
            w = larg(v, estilo, ss)
            it = dict(k="sub", s=v, x=x, w=w, size=ss, dy=dys, grupo=grupo, termo=termo)
            itens.append(it)
            x += w + size * 0.03
            if grupo >= 0:
                grupos[grupo]["x1"] = x
                if v.isdigit():
                    grupos[grupo]["n"] = int(v)
            ultimo_sub = it
        elif k == "sup":
            v = _carga(v)
            w = larg(v, estilo, sp)
            if ultimo_sub is not None:  # carga empilhada sobre o índice
                x0 = ultimo_sub["x"]
                itens.append(dict(k="sup", s=v, x=x0, w=w, size=sp, dy=dyp, grupo=grupo, termo=termo))
                x = max(x, x0 + w + size * 0.03)
            else:
                x += size * 0.05
                itens.append(dict(k="sup", s=v, x=x, w=w, size=sp, dy=dyp, grupo=grupo, termo=termo))
                x += w + size * 0.03
            if grupo >= 0:
                grupos[grupo]["x1"] = x
            ultimo_sub = None
        elif k == "coef":
            g = novo_grupo("coef", v, x)
            w = larg(v, estilo, size)
            itens.append(dict(k="coef", s=v, x=x, w=w, size=size, dy=0, grupo=g, termo=termo))
            folga = 0.0 if prox[0] == "txt" and prox[1].islower() else size * 0.1
            x += w + folga
            grupos[g]["x1"] = x - folga
            grupos[g]["n"] = v
            ultimo_sub = None
        elif k == "est":
            se = size * 0.52
            w = larg(v, estilo if estilo != "g" else "b", se)
            itens.append(dict(k="est", s=v, x=x + size * 0.05, w=w, size=se, dy=0, grupo=-1, termo=termo))
            x += w + size * 0.08
            ultimo_sub = None
        else:  # txt: parênteses, colchetes, ponto do hidrato, letras soltas (e⁻, 1s²)
            w = larg(v, estilo, size)
            tipo = "par" if v in "([" else None
            g = novo_grupo("par", v, x) if tipo else grupo
            itens.append(dict(k="txt", s=v, x=x, w=w, size=size, dy=0, grupo=g, termo=termo))
            x += w + ap + size * 0.03
            if v.islower() and not tipo:
                grupo = g
            ultimo_sub = None
    largura = x
    for g in grupos:
        g["topo"], g["base"] = -size * 0.76, size * 0.36
    return tuple(itens), largura, tuple(tuple(sorted(g.items())) for g in grupos)


def _x0(w, x, align):
    return x - w / 2 if align == "center" else x - w if align == "right" else x


def seta_reacao(c, x0, x1, y, size, cor, a=1.0, p=1.0, eq=False, rotulo=None, escuro=False):
    """seta da reação de x0 a x1 na altura do meio da letra (y = linha de base); eq=True = duas meias-setas ⇌"""
    if a <= 0 or p <= 0:
        return
    ym = y - size * 0.3
    lw = max(4, size * 0.065)
    k = size * 0.22
    xe = lerp(x0, x1, p)
    if not eq:
        M.line(c, x0, ym, xe - k * 0.6, ym, cor, a, lw, cap_round=True)
        F._cabeca(c, xe, ym, 1, 0, k, cor, a)
    else:
        g = size * 0.1
        M.line(c, x0, ym - g, xe - lw, ym - g, cor, a, lw, cap_round=True)
        path = skia.Path(); path.moveTo(xe, ym - g); path.lineTo(xe - k, ym - g - k * 0.6); path.lineTo(xe - k, ym - g); path.close()
        c.drawPath(path, M.paint(cor, a))
        xs = lerp(x1, x0, p)
        M.line(c, xs + lw, ym + g, x1, ym + g, cor, a, lw, cap_round=True)
        path = skia.Path(); path.moveTo(xs, ym + g); path.lineTo(xs + k, ym + g + k * 0.6); path.lineTo(xs + k, ym + g); path.close()
        c.drawPath(path, M.paint(cor, a))
    if rotulo and p >= 1:
        sr = size * 0.42
        E.formula(c, rotulo, (x0 + x1) / 2, ym - size * 0.28, sr, E._est(rotulo, "b"), cor, a, "center")


def _cor_item(it, cor, cores, escuro):
    if not cores:
        return cor if it["k"] != "est" else (E.CLARO if escuro else CINZA)
    g = it["grupo"]
    if it["k"] == "sub" and ("indice", g) in cores:
        return cores[("indice", g)]
    if it["k"] == "sub" and "indice" in cores:
        return cores["indice"]
    if it["k"] == "coef" and "coef" in cores:
        return cores["coef"]
    if it["k"] == "sup" and "carga" in cores:
        return cores["carga"]
    if g in cores:
        return cores[g]
    if it["k"] == "el" and it["s"] in cores:
        return cores[it["s"]]
    return cor if it["k"] != "est" else (E.CLARO if escuro else CINZA)


def _pinta(c, itens, x0, y, estilo, cor, a, cores, escuro, so=None, p_seta=1.0, cor_seta=None):
    simb = {it["grupo"]: it["s"] for it in itens if it["k"] == "el"}
    for it in itens:
        if so is not None and not so(it):
            continue
        k = it["k"]
        if k in ("seta", "eq"):
            seta_reacao(c, x0 + it["x"], x0 + it["x"] + it["w"], y, it["size"], cor_seta or cor, a, p_seta, k == "eq", it["s"], escuro)
            continue
        cr = _cor_item(it, cor, cores, escuro)
        if cores and k in ("sub", "sup") and cr == cor and it["grupo"] in simb and simb[it["grupo"]] in cores:
            if not (k == "sub" and "indice" in cores) and not (k == "sup" and "carga" in cores):
                cr = cores[simb[it["grupo"]]]
        est = estilo if k != "est" else ("b" if estilo == "g" else estilo)
        escreve(c, it["s"], x0 + it["x"], y + it["dy"], it["size"], est, cr, a)


def formula(c, s, x, y, size, cor=None, a=1.0, align="left", estilo="g", cores=None, escuro=False):
    """fórmula química (ou equação) numa linha; y = linha de base. Devolve a largura. Veja a escrita na docstring do módulo"""
    itens, w, _ = _layout(s, float(size), estilo)
    if c is not None and a > 0:
        _pinta(c, itens, _x0(w, x, align), y, estilo, cor or _tinta(escuro), a, cores, escuro)
    return w


def formula_em(c, t, t0, s, x, y, size, cor=None, align="left", estilo="g", cores=None, escuro=False, d=0.5):
    foco(c, t, t0, d, lambda a: formula(c, s, x, y, size, cor, a, align, estilo, cores, escuro))


def grupos(s, x, y, size, align="left", estilo="g"):
    """caixa de cada grupo (símbolo + índice, coeficiente, parêntese) já na tela"""
    _, w, gs = _layout(s, float(size), estilo)
    x0 = _x0(w, x, align)
    out = []
    for g in gs:
        g = dict(g)
        g["x0"] += x0
        g["x1"] += x0
        g["cx"] = (g["x0"] + g["x1"]) / 2
        g["topo"] += y
        g["base"] += y
        out.append(g)
    return out


def com_um(s, quais=None):
    """a mesma fórmula com o índice 1 escrito depois de cada símbolo sem índice (ou só nos grupos de quais).
    Devolve (texto, grupos que ganharam o 1)"""
    toks = _tokens(s)
    out, ganhou, g = [], [], -1
    for n, (k, v) in enumerate(toks):
        if k in ("presub", "presup"):
            out.append(("_" if k == "presub" else "^") + "{" + v + "}")
            continue
        out.append({"sub": "_{" + v + "}", "sup": "^{" + v + "}", "esp": " ", "seta": "→" + ("{" + v + "}" if v else ""),
                    "eq": "⇌" + ("{" + v + "}" if v else ""), "mais": "+"}.get(k, v))
        if k in ("el", "coef") or (k == "txt" and v in "(["):
            g += 1
        if k == "el":
            prox = toks[n + 1][0] if n + 1 < len(toks) else ""
            if prox != "sub" and (quais is None or g in quais):
                out.append("_{1}")
                ganhou.append(g)
    return "".join(out), ganhou


def formula_um(c, t, t0, s, t1, x, y, size, quais=None, align="left", cores=None, escuro=False, cor_um=None, caixa=True):
    """o índice que não se escreve: a fórmula s entra em t0 e, em t1, ganha o "1" em cinza (numa caixa tracejada) depois de cada
    símbolo sem índice (ou só nos grupos de quais). As letras da direita abrem espaço para ele. Devolve os grupos em uso"""
    s1, ganhou = com_um(s, quais)
    cor_um = cor_um or (E.CLARO if escuro else CINZA)
    if t < t1:
        formula_em(c, t, t0, s, x, y, size, None, align, "g", cores, escuro)
        return grupos(s, x, y, size, align)
    k = ease_io(prog(t, t1, 0.4))
    c1 = dict(cores or {})
    for g in ganhou:
        c1[("indice", g)] = cor_um
    G = grupos(s1, x, y, size, align)
    formula(c, s1, x, y, size, None, 1.0, align, "g", c1, escuro) if k >= 1 else None
    if k < 1:  # troca suave: a velha some enquanto a nova entra
        formula(c, s, x, y, size, None, 1 - k, align, "g", cores, escuro)
        formula(c, s1, x, y, size, None, k, align, "g", c1, escuro)
    if caixa:
        itens, w, _ = _layout(s1, float(size), "g")
        x0 = _x0(w, x, align)
        for it in itens:
            if it["k"] == "sub" and it["grupo"] in ganhou:
                pt = M.paint(cor_um, k, stroke=max(3, size * 0.014))
                pt.setPathEffect(skia.DashPathEffect.Make([8, 6], 0))
                c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x0 + it["x"] - size * 0.05, y - size * 0.24, it["w"] + size * 0.1, size * 0.57),
                                                  size * 0.05, size * 0.05), pt)
    return G


def formula_passo(c, t, t0, s, x, y, size, cor=None, align="left", estilo="g", cores=None, escuro=False, tg=None, passo=0.25):
    """a fórmula entra grupo a grupo (símbolo com o índice dele); tg = instante de cada grupo"""
    itens, w, gs = _layout(s, float(size), estilo)
    x0 = _x0(w, x, align)
    n = max(1, len(gs))
    for gi in range(-1, n):
        ti = (tg[gi] if tg and gi < len(tg) else t0 + max(gi, 0) * passo) if gi >= 0 else t0
        foco(c, t, ti, 0.45, lambda a, gi=gi: _pinta(c, itens, x0, y, estilo, cor or _tinta(escuro), a, cores, escuro,
                                                      so=lambda it: it["grupo"] == gi))
    return w


def _especies(s):
    """separa a equação em lados e espécies (texto normalizado, sem estados)"""
    s = _normaliza(s)
    s = _ESTADOS.sub("", s)
    lados_ = re.split(r"→(?:\{[^}]*\})?|⇌(?:\{[^}]*\})?", s)
    out = []
    for lado in lados_:
        sem_carga = re.sub(r"\^\{[^}]*\}|\^.", "", lado)
        out.append([p.strip() for p in sem_carga.split("+") if p.strip()])
    return out


def _conta_parte(f):
    """conta uma fórmula sem coeficiente (pode ter parênteses e colchetes)"""
    tot, pilha, i = {}, [{}], 0
    while i < len(f):
        ch = f[i]
        if ch in "([":
            pilha.append({})
            i += 1
        elif ch in ")]":
            i += 1
            j = i
            while j < len(f) and f[j].isdigit():
                j += 1
            k = int(f[i:j]) if j > i else 1
            i = j
            dentro = pilha.pop()
            for el, n in dentro.items():
                pilha[-1][el] = pilha[-1].get(el, 0) + n * k
        elif ch.isupper():
            j = i + 1
            if j < len(f) and f[j].islower():
                j += 1
            el = f[i:j]
            i = j
            while j < len(f) and f[j].isdigit():
                j += 1
            k = int(f[i:j]) if j > i else 1
            i = j
            pilha[-1][el] = pilha[-1].get(el, 0) + k
        else:
            i += 1
    for el, n in pilha[0].items():
        tot[el] = tot.get(el, 0) + n
    return tot


def contar(s):
    """{elemento: número de átomos} de uma espécie, com coeficiente, parênteses e hidrato ("CuSO4·5H2O")"""
    s = _normaliza(s)
    s = _ESTADOS.sub("", s)
    s = re.sub(r"^\s*(\^\{[^}]*\}|_\{[^}]*\})+", "", s)  # isótopo
    s = re.sub(r"\^\{[^}]*\}|\^.", "", s).replace("_{", "").replace("}", "").replace(" ", "")
    tot = {}
    for parte in s.split("·"):
        m = re.match(r"(\d+)", parte)
        k = int(m.group(1)) if m else 1
        for el, n in _conta_parte(parte[m.end():] if m else parte).items():
            tot[el] = tot.get(el, 0) + n * k
    return tot


def lados(eq):
    """(contagem dos reagentes, contagem dos produtos): iguais quando a equação está balanceada"""
    out = []
    for lado in _especies(eq):
        tot = {}
        for sp in lado:
            for el, n in contar(sp).items():
                tot[el] = tot.get(el, 0) + n
        out.append(tot)
    return tuple(out)


def centros(s, x, y, size, align="center", estilo="g"):
    """centro x de cada espécie da equação (sem o + e a seta)"""
    itens, w, _ = _layout(s, float(size), estilo)
    x0 = _x0(w, x, align)
    por = {}
    for it in itens:
        if it["k"] in ("mais", "seta", "eq"):
            continue
        a, b = por.get(it["termo"], (1e9, -1e9))
        por[it["termo"]] = (min(a, it["x"]), max(b, it["x"] + it["w"]))
    return [x0 + (a + b) / 2 for _, (a, b) in sorted(por.items())]


def equacao(c, t, t0, s, x, y, size, align="center", tl=None, passo=0.45, cor=None, estilo="g", cores=None, escuro=False,
            cor_seta=None, d_seta=0.6):
    """equação em que cada termo (espécie, +, seta) entra no seu instante tl[k]; a seta cresce. Devolve os centros das espécies"""
    itens, w, _ = _layout(s, float(size), estilo)
    x0 = _x0(w, x, align)
    nt = max(it["termo"] for it in itens) + 1 if itens else 0
    cor = cor or _tinta(escuro)
    for k in range(nt):
        tk = tl[k] if tl and k < len(tl) else t0 + k * passo
        setas = [it for it in itens if it["termo"] == k and it["k"] in ("seta", "eq")]
        if setas:
            p = ease_out(prog(t, tk, d_seta))
            if p > 0:
                _pinta(c, itens, x0, y, estilo, cor, 1.0, cores, escuro, so=lambda it, k=k: it["termo"] == k, p_seta=p,
                       cor_seta=cor_seta or (E.CLARO if escuro else E.COR))
        else:
            foco(c, t, tk, 0.5, lambda a, k=k: _pinta(c, itens, x0, y, estilo, cor, a, cores, escuro, so=lambda it: it["termo"] == k))
    return centros(s, x, y, size, align, estilo)


def sob_termos(c, t, s, x, y, size, linhas, tl=None, dy=None, size_l=None, rotulos=None, cores_l=None, align="center",
               estilo="g", escuro=False, x_rotulo=None):
    """linhas de valores embaixo de cada espécie (mol, massa, volume). linhas = [[texto por espécie], ...]; tl = instante de cada
    linha (ou lista de listas, um por célula); rotulos = nome de cada linha, à esquerda"""
    cs = centros(s, x, y, size, align, estilo)
    size_l = size_l or size * 0.62
    dy = dy or size_l * 1.6
    tinta = _tinta(escuro)
    for i, lin in enumerate(linhas):
        yy = y + size * 0.55 + size_l * 1.1 + i * dy
        for j, (cx, txt) in enumerate(zip(cs, lin)):
            if not txt:
                continue
            ti = tl[i][j] if tl and isinstance(tl[i], (list, tuple)) else (tl[i] if tl else 0)
            cr = (cores_l[i] if cores_l else None) or tinta
            foco(c, t, ti, 0.45, lambda a, cx=cx, txt=txt, cr=cr, yy=yy: E.formula(c, txt, cx, yy, size_l, "b", cr, a, "center"))
        if rotulos and rotulos[i]:
            ti = tl[i][0] if tl and isinstance(tl[i], (list, tuple)) else (tl[i] if tl else 0)
            xr = x_rotulo if x_rotulo is not None else cs[0] - size * 1.6
            foco(c, t, ti, 0.45, lambda a, i=i, yy=yy: escreve(c, rotulos[i], xr - larg(rotulos[i], "i", size_l * 0.9), yy,
                                                              size_l * 0.9, "i", E.CLARO if escuro else TINTA2, a))
    return cs


def _plural(nome, n):
    if n == 1:
        return nome
    if nome.endswith("ão"):
        return nome[:-2] + "ões"
    return nome + "s"


def inventario(c, t, t0, itens, x, y, size=64, tl=None, total=None, nomes=True, escuro=False, dy=None, cor_n=None):
    """a contagem de uma fórmula: uma linha por elemento (bolinha + número + nome). Devolve o y da linha do total"""
    itens = list(itens)
    dy = dy or size * 1.55
    tinta = _tinta(escuro)
    r = size * 0.48
    for i, (el, n) in enumerate(itens):
        ti = tl[i] if tl else t0 + i * 0.5
        yy = y + i * dy

        def lin(a, el=el, n=n, yy=yy):
            atomo(c, x + r, yy - size * 0.33, r, el, a, escuro=escuro)
            escreve(c, str(n), x + 2 * r + size * 0.35, yy, size, "g", cor_n or _cor(escuro), a)
            if nomes:
                escreve(c, _plural(NOMES.get(el, el), n), x + 2 * r + size * 0.35 + larg(str(n), "g", size) + size * 0.25, yy,
                        size * 0.92, "i", tinta, a)
        foco(c, t, ti, 0.45, lin)
    yt = y + len(itens) * dy + size * 0.1
    if total is not None:
        soma = sum(n for _, n in itens)
        q = ep(t, total, 0.4)
        if q > 0:
            M.line(c, x, yt - size * 1.0, x + size * 6.5, yt - size * 1.0, tinta, q, 4, progress=ease_out(prog(t, total, 0.4)))
        foco(c, t, total + 0.2, 0.45, lambda a: (escreve(c, str(soma), x + 2 * r + size * 0.35, yt + size * 0.15, size, "g", _cor(escuro), a),
                                                escreve(c, "átomos" if soma != 1 else "átomo", x + 2 * r + size * 0.35 + larg(str(soma), "g", size) + size * 0.25,
                                                        yt + size * 0.15, size * 0.92, "i", tinta, a)))
    return yt


# =====================================================================================================================
# átomos e moléculas
# =====================================================================================================================
def atomo(c, cx, cy, r, s, a=1.0, rotulo=True, escuro=False, cor=None):
    """esfera com volume na cor do elemento e o símbolo dentro"""
    if a <= 0 or r <= 0:
        return
    cr = cor or cor_el(s)
    E.bola(c, cx, cy, r, cr, a)
    if M.lum(cr) > 0.85 and not escuro:  # o hidrogênio branco precisa de contorno sobre o papel
        c.drawCircle(cx, cy, r - 1.5, M.paint("#B8B8B2", a, stroke=3))
    if rotulo and r >= 16:
        size = r * (1.0 if len(s) == 1 else 0.8)
        centro(c, s, cx, cy + size * 0.36, size, "g", M.on(cr), a)


def atomo_em(c, t, t0, cx, cy, r, s, d=0.5, rotulo=True, escuro=False, cor=None):
    k = ease_back(prog(t, t0, d))
    if k > 0:
        atomo(c, cx, cy, r * k, s, min(1.0, prog(t, t0, d * 0.5)), rotulo, escuro, cor)


def _m(*at):
    return [(s, x, y) for s, x, y in at]


MOLECULAS = {
    "H2": dict(atomos=_m(("H", -0.42, 0), ("H", 0.42, 0)), ligacoes=[(0, 1, 1)]),
    "O2": dict(atomos=_m(("O", -0.58, 0), ("O", 0.58, 0)), ligacoes=[(0, 1, 2)]),
    "N2": dict(atomos=_m(("N", -0.58, 0), ("N", 0.58, 0)), ligacoes=[(0, 1, 3)]),
    "Cl2": dict(atomos=_m(("Cl", -0.68, 0), ("Cl", 0.68, 0)), ligacoes=[(0, 1, 1)]),
    "HCl": dict(atomos=_m(("H", -0.62, 0), ("Cl", 0.55, 0)), ligacoes=[(0, 1, 1)]),
    "O3": dict(atomos=_m(("O", 0, -0.32), ("O", -0.95, 0.3), ("O", 0.95, 0.3)), ligacoes=[(0, 1, 2), (0, 2, 1)]),
    "H2O": dict(atomos=_m(("O", 0, -0.18), ("H", -0.8, 0.44), ("H", 0.8, 0.44)), ligacoes=[(0, 1, 1), (0, 2, 1)]),
    "H2O2": dict(atomos=_m(("O", -0.55, 0), ("O", 0.55, 0), ("H", -1.1, -0.75), ("H", 1.1, 0.75)), ligacoes=[(0, 1, 1), (0, 2, 1), (1, 3, 1)]),
    "CO": dict(atomos=_m(("C", -0.58, 0), ("O", 0.58, 0)), ligacoes=[(0, 1, 3)]),
    "CO2": dict(atomos=_m(("O", -1.15, 0), ("C", 0, 0), ("O", 1.15, 0)), ligacoes=[(0, 1, 2), (1, 2, 2)]),
    "CH4": dict(atomos=_m(("H", 0.32, -0.62), ("C", 0, 0), ("H", 0, -1.02), ("H", -0.92, 0.42), ("H", 0.92, 0.42), ("H", 0.12, 0.92))[1:],
                ligacoes=[(0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1)]),
    "NH3": dict(atomos=_m(("N", 0, -0.2), ("H", -0.9, 0.3), ("H", 0.9, 0.3), ("H", 0, 0.78)), ligacoes=[(0, 1, 1), (0, 2, 1), (0, 3, 1)]),
    "C2H6O": dict(atomos=_m(("C", -1.2, 0.35), ("C", 0, -0.35), ("O", 1.2, 0.35), ("H", -2.1, -0.08), ("H", -1.5, 1.28),
                            ("H", -0.62, 1.15), ("H", -0.38, -1.3), ("H", 0.46, -1.26), ("H", 2.06, -0.08)),
                  ligacoes=[(0, 1, 1), (1, 2, 1), (0, 3, 1), (0, 4, 1), (0, 5, 1), (1, 6, 1), (1, 7, 1), (2, 8, 1)]),
    "C2H4": dict(atomos=_m(("C", -0.62, 0), ("C", 0.62, 0), ("H", -1.15, -0.85), ("H", -1.15, 0.85), ("H", 1.15, -0.85), ("H", 1.15, 0.85)),
                 ligacoes=[(0, 1, 2), (0, 2, 1), (0, 3, 1), (1, 4, 1), (1, 5, 1)]),
    "C2H6": dict(atomos=_m(("C", -0.7, 0), ("C", 0.7, 0), ("H", -1.2, -0.85), ("H", -1.6, 0.25), ("H", -0.9, 0.95), ("H", 1.2, 0.85),
                           ("H", 1.6, -0.25), ("H", 0.9, -0.95)),
                 ligacoes=[(0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1), (1, 5, 1), (1, 6, 1), (1, 7, 1)]),
    "H2SO4": dict(atomos=_m(("S", 0, 0), ("O", 0, -1.12), ("O", 0, 1.12), ("O", -1.12, 0), ("O", 1.12, 0), ("H", -1.85, -0.55), ("H", 1.85, 0.55)),
                  ligacoes=[(0, 1, 2), (0, 2, 2), (0, 3, 1), (0, 4, 1), (3, 5, 1), (4, 6, 1)]),
}
MOLECULAS["CH4O"] = dict(atomos=_m(("C", -0.6, 0), ("O", 0.65, 0), ("H", -1.0, -0.92), ("H", -1.5, 0.25), ("H", -0.75, 1.0), ("H", 1.25, -0.72)),
                         ligacoes=[(0, 1, 1), (0, 2, 1), (0, 3, 1), (0, 4, 1), (1, 5, 1)])


def _mol(mol):
    return MOLECULAS[mol] if isinstance(mol, str) else mol


def _vareta(c, A, B, ordem, lw, a, escuro):
    ux, uy = E._uni(*A, *B)
    nx, ny = -uy, ux
    offs = {1: (0,), 2: (-0.62, 0.62), 3: (-1.15, 0, 1.15)}[ordem]
    k = lw * (0.78 if ordem > 1 else 1.0)
    for o in offs:
        dx, dy = nx * o * lw * 1.05, ny * o * lw * 1.05
        M.line(c, A[0] + dx, A[1] + dy, B[0] + dx, B[1] + dy, "#8A8D94" if not escuro else "#5A5D66", a, k + 3)
        M.line(c, A[0] + dx, A[1] + dy, B[0] + dx, B[1] + dy, LIGA if not escuro else "#9A9DA6", a, k)
        M.line(c, A[0] + dx - nx * k * 0.18, A[1] + dy - ny * k * 0.18, B[0] + dx - nx * k * 0.18, B[1] + dy - ny * k * 0.18, "#FFFFFF", 0.45 * a, k * 0.25)


def _pontos_mol(m, cx, cy, escala, giro, separa):
    g = math.radians(giro)
    pts = []
    mx = sum(x for _, x, _ in m["atomos"]) / len(m["atomos"])
    my = sum(y for _, _, y in m["atomos"]) / len(m["atomos"])
    for s, x, y in m["atomos"]:
        x, y = x - mx, y - my
        x, y = x * math.cos(g) - y * math.sin(g), x * math.sin(g) + y * math.cos(g)
        k = 1 + 1.3 * ease_io(clamp(separa))
        pts.append((cx + x * escala * k, cy + y * escala * k))
    return pts


def molecula(c, t, t0, mol, cx, cy, escala=110, passo=0.18, separa=0.0, rotulos=True, giro=0.0, a=1.0, escuro=False, tl=None,
             r=None, d=0.45):
    """molécula bola-vareta: átomos pulam em fila, varetas surgem quando as duas pontas já estão lá. Devolve os pontos na tela"""
    m = _mol(mol)
    pts = _pontos_mol(m, cx, cy, escala, giro, separa)
    if t0 is None or a <= 0:
        if t0 is None:
            molecula_desenho(c, mol, cx, cy, escala, a, separa, rotulos, giro, escuro, r)
        return pts
    rb = r or escala * 0.4
    ts = [tl[i] if tl else t0 + i * passo for i in range(len(pts))]
    av = a * (1 - clamp(separa * 1.6))
    lw = rb * 0.32
    for i, j, o in m["ligacoes"]:
        tv = max(ts[i], ts[j]) + d * 0.5
        q = ep(t, tv, 0.3)
        if q > 0 and av > 0:
            A, B = pts[i], pts[j]
            mxy = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
            p = ease_out(prog(t, tv, 0.3))
            _vareta(c, (lerp(mxy[0], A[0], p), lerp(mxy[1], A[1], p)), (lerp(mxy[0], B[0], p), lerp(mxy[1], B[1], p)), o, lw, q * av, escuro)
    for (s, _, _), P, ti in zip(m["atomos"], pts, ts):
        k = ease_back(prog(t, ti, d))
        if k > 0:
            atomo(c, P[0], P[1], rb * RAIO.get(s, 0.95) * k, s, a * min(1.0, prog(t, ti, d * 0.5)), rotulos, escuro)
    return pts


def molecula_desenho(c, mol, cx, cy, escala=110, a=1.0, separa=0.0, rotulos=True, giro=0.0, escuro=False, r=None):
    """a molécula parada, inteira"""
    m = _mol(mol)
    pts = _pontos_mol(m, cx, cy, escala, giro, separa)
    if a <= 0:
        return pts
    rb = r or escala * 0.4
    av = a * (1 - clamp(separa * 1.6))
    if av > 0:
        for i, j, o in m["ligacoes"]:
            _vareta(c, pts[i], pts[j], o, rb * 0.32, av, escuro)
    for (s, _, _), P in zip(m["atomos"], pts):
        atomo(c, P[0], P[1], rb * RAIO.get(s, 0.95), s, a, rotulos, escuro)
    return pts


def _tri(u):
    """onda triangular de 0 a 1 (bate e volta)"""
    u = u % 2.0
    return u if u < 1 else 2 - u


def particulas(c, t, x, y, w, h, n, estado="liquido", tipos=None, r=14, semente=1, a=1.0, escuro=False, rotulos=False):
    """partículas mexendo na caixa (x, y, w, h): sólido vibra em grade, líquido escorrega no fundo, gás voa e bate nas paredes"""
    if a <= 0 or n <= 0:
        return
    rnd = random.Random(semente)
    tipos = tipos or [(E.COR, 1.0)]
    seq = []
    for cor, f in tipos:
        seq += [cor] * max(1, round(n * f))
    seq = (seq * (n // max(1, len(seq)) + 1))[:n]
    rnd.shuffle(seq)
    if estado == "solido":
        cols = max(1, min(n, int(w // (2.25 * r))))
        gx = min(2.25 * r, w / cols)
        x0 = x + (w - gx * (cols - 1)) / 2
    for i, cor in enumerate(seq):
        f1, f2, f3 = rnd.random(), rnd.random(), rnd.random() * math.tau
        if estado == "solido":
            col, lin = i % cols, i // cols
            px = x0 + col * gx + 2.2 * math.sin(t * 13 + f3)
            py = y + h - r - lin * gx * 0.93 + 2.2 * math.cos(t * 11 + f3 * 1.7)
        elif estado == "gas":
            vx, vy = 90 + 120 * f1, 80 + 120 * f2
            px = x + r + (w - 2 * r) * _tri(f1 * 2 + t * vx / max(1, w - 2 * r))
            py = y + r + (h - 2 * r) * _tri(f2 * 2 + t * vy / max(1, h - 2 * r))
        else:
            fundo = min(h, (n * (2.2 * r) ** 2) / max(w, 1) * 1.15)
            px = x + r + (w - 2 * r) * _tri(f1 * 2 + t * (0.02 + 0.03 * f2))
            py = y + h - r - (fundo - 2 * r) * (0.5 + 0.5 * math.sin(f3 + t * (0.6 + f2)))
            px += 4 * math.sin(t * 2.3 + f3)
        if isinstance(cor, str) and (cor in COR_EL or (cor[:1].isupper() and len(cor) <= 2)):
            atomo(c, px, py, r * RAIO.get(cor, 0.9) / 0.9, cor, a, rotulos, escuro)
        else:
            E.bola(c, px, py, r, cor, a)


# =====================================================================================================================
# estrutura do átomo e tabela periódica
# =====================================================================================================================
_ORDEM = ["1s", "2s", "2p", "3s", "3p", "4s", "3d", "4p", "5s", "4d", "5p", "6s", "4f", "5d", "6p", "7s", "5f", "6d", "7p"]
_CAP = dict(s=2, p=6, d=10, f=14)


def distribuicao(Z):
    """[("1s", 2), ("2s", 2), ...] na ordem do diagrama de Pauling (sem as exceções, como Cr e Cu)"""
    out, resta = [], Z
    for sub in _ORDEM:
        if resta <= 0:
            break
        k = min(resta, _CAP[sub[1]])
        out.append((sub, k))
        resta -= k
    assert sum(k for _, k in out) == Z
    return out


def camadas(Z):
    """elétrons por camada (K, L, M, ...) a partir da distribuição"""
    por = {}
    for sub, k in distribuicao(Z):
        por[int(sub[0])] = por.get(int(sub[0]), 0) + k
    return [por.get(n, 0) for n in range(1, max(por) + 1)]


def dist_texto(Z):
    return " ".join(f"{s}^{k}" for s, k in distribuicao(Z))


def bohr(c, t, t0, cx, cy, camadas_=(2, 8, 1), r0=110, dr=70, s=None, te=None, gira=0.35, nomes=False, escuro=False,
         r_nucleo=None, r_e=13, cor_e=None, passo_e=0.08):
    """modelo de camadas: núcleo na cor da matéria, camadas finas e elétrons azuis entrando um a um (te = instante de cada camada)"""
    if t < t0:
        return
    tinta = _tinta(escuro)
    rn = r_nucleo or r0 * 0.42
    k = ease_back(prog(t, t0, 0.5))
    E.bola(c, cx, cy, rn * k, E.COR, min(1, prog(t, t0, 0.3)))
    if s:
        foco(c, t, t0 + 0.2, 0.4, lambda a: centro(c, s, cx, cy + rn * 0.36, rn * (0.95 if len(s) == 1 else 0.78), "g", E.SOBRE, a))
    for i, n in enumerate(camadas_):
        ti = te[i] if te else t0 + 0.5 + i * 0.6
        R = r0 + i * dr
        q = ep(t, ti - 0.3, 0.5)
        if q > 0:
            c.drawArc(skia.Rect.MakeXYWH(cx - R, cy - R, 2 * R, 2 * R), -90, 360 * ease_io(prog(t, ti - 0.3, 0.5)), False,
                      M.paint(TINTA2 if not escuro else "#8A8D99", 0.7 * q, stroke=3))
            if nomes:
                foco(c, t, ti, 0.4, lambda a, i=i, R=R: E.formula(c, "KLMNOPQ"[i], cx + R * 0.71 + 14, cy - R * 0.71 - 8, 40, "b", tinta, a))
        for j in range(n):
            tj = ti + j * passo_e
            kk = ease_back(prog(t, tj, 0.35))
            if kk <= 0:
                continue
            ang = -math.pi / 2 + math.tau * j / n + (t - t0) * gira / (1 + i * 0.4)
            ex, ey = cx + R * math.cos(ang), cy + R * math.sin(ang)
            E.bola(c, ex, ey, r_e * kk, cor_e or ELETRON, 1.0)


def pauling(c, t, t0, x, y, size=58, Z=None, passo=0.35, setas=True, escuro=False, dx=None, dy=None, cor_seta=None):
    """diagrama de Pauling em (x, y) = canto de cima à esquerda; com Z, cada subnível ganha o expoente quando a seta passa"""
    dx, dy = dx or size * 2.3, dy or size * 1.3
    tinta = _tinta(escuro)
    linhas = [["1s"], ["2s", "2p"], ["3s", "3p", "3d"], ["4s", "4p", "4d", "4f"], ["5s", "5p", "5d", "5f"], ["6s", "6p", "6d"], ["7s", "7p"]]
    pos = {}
    for i, lin in enumerate(linhas):
        for j, sub in enumerate(lin):
            pos[sub] = (x + j * dx + size * 0.6, y + i * dy + size * 0.5)
    cheio = dict(distribuicao(Z)) if Z else {}
    # diagonais: mesma soma n + l, do canto de cima à direita para baixo à esquerda
    diags = {}
    for sub in _ORDEM:
        nl = int(sub[0]) + "spdf".index(sub[1])
        diags.setdefault(nl, []).append(sub)
    t1 = t0 + 0.8
    feitos, tsub = [], {}
    for k, (nl, subs) in enumerate(sorted(diags.items())):
        tk = t1 + k * passo
        if Z and not any(s_ in cheio for s_ in subs):
            break
        if setas:
            A, B = pos[subs[0]], pos[subs[-1]]
            ext = size * 0.75
            ux, uy = E._uni(*A, *B) if subs[0] != subs[-1] else (-0.6, 0.8)
            P0 = (A[0] - ux * ext, A[1] - uy * ext)
            P1 = (B[0] + ux * ext, B[1] + uy * ext)
            p = ease_out(prog(t, tk, passo * 0.9))
            if p > 0:
                F.seta(c, *P0, *P1, cor_seta or (E.CLARO if escuro else E.COR), 0.55, 4, size * 0.3, p)
        for s_ in subs:
            tsub[s_] = tk + passo * 0.5
            if s_ in cheio:
                feitos.append(s_)
    for i, lin in enumerate(linhas):
        foco(c, t, t0 + i * 0.08, 0.4, lambda a, lin=lin: [E.formula(c, sub, pos[sub][0], pos[sub][1] + size * 0.36, size, "b", tinta, a, "center")
                                                          for sub in lin])
    if Z:
        ult = feitos[-1] if feitos else None
        for s_ in feitos:
            e_ = cheio[s_]
            px, py = pos[s_]
            w = E.formula(None, s_, 0, 0, size, "b", a=0)
            cr = _cor(escuro) if s_ == ult else tinta
            foco(c, t, tsub[s_], 0.35, lambda a, px=px, py=py, w=w, e_=e_, cr=cr: escreve(c, str(e_), px + w / 2 + size * 0.04, py - size * 0.12, size * 0.6, "g", cr, a))
    return feitos


_SIMBOLOS = ("H He Li Be B C N O F Ne Na Mg Al Si P S Cl Ar K Ca Sc Ti V Cr Mn Fe Co Ni Cu Zn Ga Ge As Se Br Kr Rb Sr Y Zr Nb Mo "
             "Tc Ru Rh Pd Ag Cd In Sn Sb Te I Xe Cs Ba La Ce Pr Nd Pm Sm Eu Gd Tb Dy Ho Er Tm Yb Lu Hf Ta W Re Os Ir Pt Au Hg Tl Pb "
             "Bi Po At Rn Fr Ra Ac Th Pa U Np Pu Am Cm Bk Cf Es Fm Md No Lr Rf Db Sg Bh Hs Mt Ds Rg Cn Nh Fl Mc Lv Ts Og").split()
assert len(_SIMBOLOS) == 118


@lru_cache(None)
def _posicoes():
    """símbolo → (Z, período, grupo); lantanídeos e actinídeos ficam com grupo None"""
    out = {}
    for z, s in enumerate(_SIMBOLOS, 1):
        if z <= 2:
            per, g = 1, (1 if z == 1 else 18)
        elif z <= 18:
            per = 2 if z <= 10 else 3
            i = z - (3 if per == 2 else 11)
            g = i + 1 if i < 2 else i + 11
        elif z <= 54:
            per = 4 if z <= 36 else 5
            g = z - (19 if per == 4 else 37) + 1
        else:
            per = 6 if z <= 86 else 7
            base = 55 if per == 6 else 87
            i = z - base
            if i < 2:
                g = i + 1
            elif i < 17:
                g = None  # La–Lu / Ac–Lr
            else:
                g = i - 17 + 4
        out[s] = (z, per, g)
    return out


def tabela(c, t, t0, x, y, cel=62, periodos=(1, 7), grupos_=(1, 18), familia=None, periodo=None, destaque=(), numeros=True,
           z=False, d=0.9, escuro=False, cor=None, gap=4):
    """recorte da tabela periódica em (x, y) = canto de cima à esquerda das células; devolve pos(símbolo) → centro da célula"""
    P = _posicoes()
    p0, p1 = periodos
    g0, g1 = grupos_
    cor = cor or E.COR
    tinta = _tinta(escuro)

    def pos(s):
        _, per, g = P[s]
        return x + (g - g0) * cel + cel / 2, y + (per - p0) * cel + cel / 2

    for s, (zz, per, g) in P.items():
        if not (p0 <= per <= p1):
            continue
        if g is None:
            if s not in ("La", "Ac") or not (g0 <= 3 <= g1):
                continue
            g, rot = 3, ("57–71" if s == "La" else "89–103")
        else:
            rot = s
            if not (g0 <= g <= g1):
                continue
        ti = t0 + ((g - g0) + (per - p0)) * d / 22
        q = ep(t, ti, 0.35)
        if q <= 0:
            continue
        cx, cy = x + (g - g0) * cel + cel / 2, y + (per - p0) * cel + cel / 2
        marcado = s in destaque or (familia == g) or (periodo == per)
        fundo = cor if marcado else ("#FFFFFF" if not escuro else "#22232B")
        M.rrect(c, cx - cel / 2 + gap / 2, cy - cel / 2 + gap / 2, cel - gap, cel - gap, cel * 0.12, fundo, q)
        if not marcado:
            _borda_rr(c, cx - cel / 2 + gap / 2, cy - cel / 2 + gap / 2, cel - gap, cel - gap, cel * 0.12, FIO if not escuro else "#3A3B46", q, 2)
        ct = E.SOBRE if marcado else tinta
        if rot == s:
            sz = cel * (0.42 if len(s) <= 2 else 0.34)
            centro(c, s, cx, cy + sz * 0.36 + (cel * 0.08 if z else 0), sz, "b", ct, q)
            if z:
                centro(c, str(zz), cx, cy - cel * 0.2, cel * 0.2, "m", ct, q * 0.85)
        else:
            centro(c, rot, cx, cy + cel * 0.07, cel * 0.2, "b", ct, q * 0.8)
    if numeros:
        for g in range(g0, g1 + 1):
            foco(c, t, t0 + 0.2, 0.4, lambda a, g=g: centro(c, str(g), x + (g - g0) * cel + cel / 2, y - cel * 0.25, cel * 0.3, "b", TINTA2 if not escuro else E.CLARO, a))
        for per in range(p0, p1 + 1):
            foco(c, t, t0 + 0.2, 0.4, lambda a, per=per: centro(c, str(per), x - cel * 0.4, y + (per - p0) * cel + cel / 2 + cel * 0.11,
                                                                cel * 0.3, "b", TINTA2 if not escuro else E.CLARO, a))
    return pos


# =====================================================================================================================
# Lewis, estrutural e bastão
# =====================================================================================================================
def _par(c, cx, cy, ang, dist, r, cor, a, n=2):
    """par (ou elétron sozinho) de elétrons na direção ang (graus, 90 = cima), a dist px do centro"""
    g = math.radians(ang)
    ux, uy = math.cos(g), -math.sin(g)
    nx, ny = -uy, ux
    px, py = cx + ux * dist, cy + uy * dist
    if n == 1:
        c.drawCircle(px, py, r, M.paint(cor, a))
    else:
        for s in (-1, 1):
            c.drawCircle(px + nx * r * 1.5 * s, py + ny * r * 1.5 * s, r, M.paint(cor, a))


def simbolo_lewis(c, s, cx, cy, size, n, a=1.0, escuro=False, cor=None, cor_e=None):
    """símbolo de Lewis: o elemento com n elétrons de valência em volta (um por lado, depois em pares)"""
    if a <= 0:
        return
    centro(c, s, cx, cy + size * 0.36, size, "g", cor or _tinta(escuro), a)
    lados_ = (90, 0, 270, 180)
    w = larg(s, "g", size)
    for i, ang in enumerate(lados_):
        k = (n // 4) + (1 if i < n % 4 else 0)
        if k:
            dist = (w / 2 + size * 0.22) if ang in (0, 180) else size * 0.62
            _par(c, cx, cy, ang, dist, size * 0.075, cor_e or ELETRON, a, k)


def lewis(c, t, t0, atomos, ligacoes, cx, cy, escala=150, size=96, pontos=False, tl=None, tp=None, escuro=False, passo=0.2,
          cores=None, cor_e=None):
    """estrutura de Lewis / fórmula estrutural plana. atomos = [("O", x, y[, [ângulos dos pares livres]])] em unidades de
    ligação; ligacoes = [(i, j, ordem)]. pontos=True mostra a ligação como pares de elétrons. tl = instante de cada átomo,
    tp = instante dos pares livres. Devolve os pontos na tela"""
    tinta = _tinta(escuro)
    pts = [(cx + a_[1] * escala, cy + a_[2] * escala) for a_ in atomos]
    ts = [tl[i] if tl else t0 + i * passo for i in range(len(atomos))]
    for i, j, o in ligacoes:
        tv = max(ts[i], ts[j]) + 0.25
        p = ease_out(prog(t, tv, 0.4))
        if p <= 0:
            continue
        A, B = pts[i], pts[j]
        ux, uy = E._uni(*A, *B)
        nx, ny = -uy, ux
        ra, rb = larg(atomos[i][0], "g", size) / 2 + size * 0.18, larg(atomos[j][0], "g", size) / 2 + size * 0.18
        ra, rb = max(ra, size * 0.5), max(rb, size * 0.5)
        A2, B2 = (A[0] + ux * ra, A[1] + uy * ra), (B[0] - ux * rb, B[1] - uy * rb)
        offs = {1: (0,), 2: (-0.5, 0.5), 3: (-1, 0, 1)}[o]
        g = size * 0.16
        for k in offs:
            if pontos:
                mx, my = (A2[0] + B2[0]) / 2 + nx * k * g * 1.4, (A2[1] + B2[1]) / 2 + ny * k * g * 1.4
                for s_ in (-1, 1):
                    c.drawCircle(mx + ux * size * 0.11 * s_, my + uy * size * 0.11 * s_, size * 0.075, M.paint(cor_e or ELETRON, p))
            else:
                M.line(c, A2[0] + nx * k * g, A2[1] + ny * k * g, B2[0] + nx * k * g, B2[1] + ny * k * g, tinta, 1.0, max(4, size * 0.07),
                       progress=p)
    for i, at in enumerate(atomos):
        s = at[0]
        cr = (cores or {}).get(s, tinta)
        foco(c, t, ts[i], 0.4, lambda a, s=s, i=i, cr=cr: centro(c, s, pts[i][0], pts[i][1] + size * 0.36, size, "g", cr, a))
        if len(at) > 3 and at[3]:
            tq = tp if tp is not None else ts[i] + 0.4
            q = ep(t, tq, 0.4)
            if q > 0:
                w = larg(s, "g", size)
                for ang in at[3]:
                    hor = abs(math.cos(math.radians(ang)))
                    dist = lerp(size * 0.62, w / 2 + size * 0.22, hor)
                    _par(c, *pts[i], ang, dist, size * 0.075, cor_e or ELETRON, q)
    return pts


def zigzag(n, ang=30):
    """n pontos de uma cadeia em zigue-zague (unidades de ligação), centrados na origem"""
    g = math.radians(ang)
    dx, dy = math.cos(g), math.sin(g)
    pts = [(i * dx, (dy / 2) * (1 if i % 2 else -1)) for i in range(n)]
    mx = sum(p[0] for p in pts) / n
    return [(x - mx, y) for x, y in pts]


def bastao(c, t, t0, pts, cx, cy, escala=110, duplas=(), triplas=(), rotulos=None, d=1.0, numeros=None, escuro=False,
           ligacoes=None, largura=7, size=None, passo_n=0.3):
    """fórmula de linha (bastão): cada vértice é um carbono. pts em unidades; ligacoes = [(i, j)] (padrão: em fila).
    rotulos = {i: "OH"} troca o vértice pelo heteroátomo; numeros = instante em que os carbonos ganham bolinha e número"""
    tinta = _tinta(escuro)
    P = [(cx + x * escala, cy + y * escala) for x, y in pts]
    ligs = ligacoes or [(i, i + 1) for i in range(len(P) - 1)]
    rotulos = rotulos or {}
    size = size or escala * 0.5
    n = len(ligs)
    duplas, triplas = {tuple(sorted(x)) for x in duplas}, {tuple(sorted(x)) for x in triplas}
    for k, (i, j) in enumerate(ligs):
        tk = t0 + d * k / max(1, n)
        p = ease_io(prog(t, tk, d / max(1, n) * 1.2))
        if p <= 0:
            continue
        A, B = P[i], P[j]
        ux, uy = E._uni(*A, *B)
        L = math.dist(A, B)
        ca = size * 0.55 if i in rotulos else 0
        cb = size * 0.55 if j in rotulos else 0
        A2 = (A[0] + ux * ca, A[1] + uy * ca)
        B2 = (B[0] - ux * cb, B[1] - uy * cb)
        M.line(c, *A2, *B2, tinta, 1.0, largura, progress=p)
        key = tuple(sorted((i, j)))
        if key in duplas or key in triplas:
            # segunda linha por dentro, mais curta (o lado de dentro é o do centro da molécula)
            mx_, my_ = sum(q[0] for q in P) / len(P), sum(q[1] for q in P) / len(P)
            nx, ny = -uy, ux
            mid = ((A[0] + B[0]) / 2, (A[1] + B[1]) / 2)
            if (mx_ - mid[0]) * nx + (my_ - mid[1]) * ny < 0:
                nx, ny = -nx, -ny
            if len(P) == 2:
                nx, ny = -uy, ux
            offs = [1] if key in duplas else [1, -1]
            for o in offs:
                g = largura * 2.6 * o
                enc = L * 0.14
                M.line(c, A2[0] + nx * g + ux * enc, A2[1] + ny * g + uy * enc, B2[0] + nx * g - ux * enc, B2[1] + ny * g - uy * enc,
                       tinta, 1.0, largura, progress=p)
    for i, s in rotulos.items():
        ti = t0 + d * max(0, i - 1) / max(1, n)
        foco(c, t, ti + 0.2, 0.4, lambda a, i=i, s=s: formula(c, s, P[i][0], P[i][1] + size * 0.36, size, cor_el(s[0]) if s[0] in "ONSPF" else
                                                             (_tinta(escuro) if s[0] != "C" else tinta), a, "center",
                                                             cores=None))
    if numeros is not None:
        k = 0
        for i in range(len(P)):
            if i in rotulos:
                continue
            ti = numeros + k * passo_n
            k += 1
            q = ease_back(prog(t, ti, 0.4))
            if q > 0:
                E.bola(c, P[i][0], P[i][1], size * 0.42 * q, E.COR)
                foco(c, t, ti + 0.1, 0.3, lambda a, i=i, k=k: centro(c, str(k), P[i][0], P[i][1] + size * 0.17, size * 0.46, "g", E.SOBRE, a))
    return P


# =====================================================================================================================
# laboratório
# =====================================================================================================================
def _copo_path(kind, cx, yb, w, h):
    """contorno do vidro (aberto em cima) e região interna; yb = fundo"""
    p = skia.Path()
    if kind == "bequer":
        r = w * 0.06
        x0, x1, yt = cx - w / 2, cx + w / 2, yb - h
        p.moveTo(x0 - w * 0.05, yt); p.lineTo(x0, yt + w * 0.05); p.lineTo(x0, yb - r)
        p.quadTo(x0, yb, x0 + r, yb); p.lineTo(x1 - r, yb); p.quadTo(x1, yb, x1, yb - r); p.lineTo(x1, yt)
        dentro = skia.Path()
        dentro.addRRect(skia.RRect.MakeRectXY(skia.Rect.MakeLTRB(x0, yt, x1, yb), r, r))
        return p, dentro, (yt, yb)
    if kind == "erlenmeyer":
        gw = w * 0.26
        yt, yg = yb - h, yb - h * 0.62
        x0, x1 = cx - w / 2, cx + w / 2
        r = w * 0.06
        p.moveTo(cx - gw / 2 - w * 0.03, yt); p.lineTo(cx - gw / 2, yt + w * 0.03); p.lineTo(cx - gw / 2, yg)
        p.lineTo(x0 + r * 0.3, yb - r); p.quadTo(x0, yb, x0 + r * 1.5, yb); p.lineTo(x1 - r * 1.5, yb); p.quadTo(x1, yb, x1 - r * 0.3, yb - r)
        p.lineTo(cx + gw / 2, yg); p.lineTo(cx + gw / 2, yt + w * 0.03); p.lineTo(cx + gw / 2 + w * 0.03, yt)
        dentro = skia.Path()
        dentro.moveTo(cx - gw / 2, yt); dentro.lineTo(cx - gw / 2, yg); dentro.lineTo(x0 + r * 0.3, yb - r); dentro.quadTo(x0, yb, x0 + r * 1.5, yb)
        dentro.lineTo(x1 - r * 1.5, yb); dentro.quadTo(x1, yb, x1 - r * 0.3, yb - r); dentro.lineTo(cx + gw / 2, yg); dentro.lineTo(cx + gw / 2, yt); dentro.close()
        return p, dentro, (yt, yb)
    # tubo de ensaio: fundo redondo
    x0, x1, yt = cx - w / 2, cx + w / 2, yb - h
    p.moveTo(x0 - w * 0.08, yt); p.lineTo(x0, yt + w * 0.06); p.lineTo(x0, yb - w / 2)
    p.arcTo(skia.Rect.MakeLTRB(x0, yb - w, x1, yb), 180, -180, False); p.lineTo(x1, yt + w * 0.06); p.lineTo(x1 + w * 0.08, yt)
    dentro = skia.Path()
    dentro.moveTo(x0, yt); dentro.lineTo(x0, yb - w / 2); dentro.arcTo(skia.Rect.MakeLTRB(x0, yb - w, x1, yb), 180, -180, False)
    dentro.lineTo(x1, yt); dentro.close()
    return p, dentro, (yt, yb)


def _frasco(kind, c, t, t0, cx, yb, w, h, nivel, cor, te, d, graduacao, rotulo, particulas_, escuro, a_max=1.0):
    if t < t0:
        return
    contorno, dentro, (yt, yb_) = _copo_path(kind, cx, yb, w, h)
    q = ep(t, t0, 0.5) * a_max
    cor = _resolve_cor(cor, t)
    # vidro: véu claro e contorno
    c.drawPath(dentro, M.paint("#FFFFFF" if not escuro else "#2A2C36", 0.45 * q))
    nv = nivel * (ease_io(prog(t, te, d)) if te is not None else 1.0)
    if nv > 0:
        yl = yb_ - (yb_ - yt) * nv
        c.save()
        c.clipPath(dentro, skia.ClipOp.kIntersect, True)
        pt = skia.Paint(AntiAlias=True)
        pt.setShader(skia.GradientShader.MakeLinear([skia.Point(0, yl), skia.Point(0, yb_)],
                                                    [hexc(mix(cor, "#FFFFFF", 0.15), 0.92 * q), hexc(mix(cor, "#000000", 0.12), 0.95 * q)]))
        onda_ = 4 * math.sin(t * 3) * (1 - ep(t, (te or t0) + d, 0.8)) if te is not None else 0
        liq = skia.Path()
        liq.moveTo(cx - w, yl + onda_); liq.quadTo(cx, yl - onda_, cx + w, yl + onda_); liq.lineTo(cx + w, yb_ + 5); liq.lineTo(cx - w, yb_ + 5); liq.close()
        c.drawPath(liq, pt)
        M.line(c, cx - w, yl + onda_, cx + w, yl + onda_, mix(cor, "#FFFFFF", 0.55), q, 4)
        if particulas_:
            pd = dict(particulas_)
            nn = pd.pop("n", 20)
            gw = w * (0.26 if kind == "erlenmeyer" else 1.0)
            larg_l = w * 0.86 if kind != "erlenmeyer" else w * 0.7
            particulas(c, t, cx - larg_l / 2, yl + 8, larg_l, yb_ - yl - 12, nn, pd.pop("estado", "gas"), pd.pop("tipos", None),
                       pd.pop("r", 10), pd.pop("semente", 3), q, escuro)
        c.restore()
    vidro = VIDRO if not escuro else "#B8BCC8"
    pv = M.paint(vidro, q, stroke=5)
    pv.setStrokeJoin(skia.Paint.kRound_Join)
    pv.setStrokeCap(skia.Paint.kRound_Cap)
    c.drawPath(contorno, pv)
    # brilho
    M.line(c, cx - w * 0.36, yt + h * 0.18, cx - w * 0.36, yt + h * 0.55 if kind != "erlenmeyer" else yt + h * 0.32, "#FFFFFF", 0.7 * q, max(4, w * 0.03))
    if graduacao and kind == "bequer":
        for i in range(1, 5):
            yy = yb_ - (yb_ - yt) * i / 5.5
            M.line(c, cx + w / 2 - w * (0.16 if i % 2 == 0 else 0.1), yy, cx + w / 2 - 6, yy, vidro, 0.6 * q, 3)
    if rotulo:
        foco(c, t, t0 + 0.3, 0.4, lambda a: formula(c, rotulo, cx, yb + 64, 46, _tinta(escuro), a, "center", "b"))


def bequer(c, t, t0, cx, yb, w=280, h=320, nivel=0.6, cor=AGUA, te=None, d=1.2, graduacao=True, rotulo=None, particulas=None, escuro=False):
    _frasco("bequer", c, t, t0, cx, yb, w, h, nivel, cor, te, d, graduacao, rotulo, particulas, escuro)


def erlenmeyer(c, t, t0, cx, yb, w=300, h=340, nivel=0.35, cor=AGUA, te=None, d=1.2, graduacao=False, rotulo=None, particulas=None, escuro=False):
    _frasco("erlenmeyer", c, t, t0, cx, yb, w, h, nivel, cor, te, d, graduacao, rotulo, particulas, escuro)


def tubo(c, t, t0, cx, yb, w=96, h=330, nivel=0.5, cor=AGUA, te=None, d=1.0, graduacao=False, rotulo=None, particulas=None, escuro=False):
    _frasco("tubo", c, t, t0, cx, yb, w, h, nivel, cor, te, d, graduacao, rotulo, particulas, escuro)


def conta_gotas(c, x, y, a=1.0, cor=None, h=210, escuro=False):
    """conta-gotas com a ponta em (x, y), apontado para baixo"""
    if a <= 0:
        return
    vidro = VIDRO if not escuro else "#B8BCC8"
    M.rrect(c, x - 16, y - h, 32, h * 0.7, 10, "#FFFFFF" if not escuro else "#2A2C36", 0.6 * a)
    if cor:
        M.rrect(c, x - 12, y - h * 0.55, 24, h * 0.25, 8, cor, 0.9 * a)
    _borda_rr(c, x - 16, y - h, 32, h * 0.7, 10, vidro, a, 4)
    p = skia.Path(); p.moveTo(x - 10, y - h * 0.3); p.lineTo(x - 3, y); p.lineTo(x + 3, y); p.lineTo(x + 10, y - h * 0.3); p.close()
    c.drawPath(p, M.paint(vidro, a))
    M.rrect(c, x - 26, y - h - 70, 52, 82, 24, TINTA2 if not escuro else "#8A8D99", a)


def gotas(c, t, t0, x, y0, y1, n=3, cor=None, intervalo=0.55, r=13, escuro=False):
    """gotas caindo de (x, y0) até y1, uma a cada intervalo; ao bater, abre uma onda e some"""
    cor = cor or E.COR
    for i in range(n):
        ti = t0 + i * intervalo
        u = prog(t, ti, 0.45)
        if u <= 0:
            continue
        if u < 1:
            yy = lerp(y0, y1, u * u)
            p = skia.Path()
            p.moveTo(x, yy - r * 1.9); p.quadTo(x + r * 1.1, yy - r * 0.3, x, yy + r); p.quadTo(x - r * 1.1, yy - r * 0.3, x, yy - r * 1.9)
            c.drawPath(p, M.paint(cor, 0.95))
        else:
            v = prog(t, ti + 0.45, 0.5)
            if v < 1:
                c.drawOval(skia.Rect.MakeLTRB(x - r * 4 * v, y1 - r * 0.8 * v, x + r * 4 * v, y1 + r * 0.8 * v), M.paint(cor, 0.7 * (1 - v), stroke=3))


_PH = [(0, "#D7263D"), (2, "#F46036"), (4, "#F6AE2D"), (6, "#C5D86D"), (7, "#2FA84F"), (8, "#1B998B"), (10, "#2E86AB"), (12, "#3D348B"), (14, "#5B2A86")]


def cor_ph(ph):
    """cor do indicador universal para o pH"""
    ph = clamp(ph, 0, 14)
    for (a, ca), (b, cb) in zip(_PH, _PH[1:]):
        if ph <= b:
            return mix(ca, cb, (ph - a) / (b - a))
    return _PH[-1][1]


def cor_indicador(nome, ph):
    if nome == "fenolftaleina":
        return mix(AGUA, "#E5399A", clamp((ph - 8.2) / 1.8))
    if nome == "tornassol":
        return "#D7263D" if ph < 4.5 else ("#7A4FB5" if ph < 8.3 else "#2E5EAA")
    if nome == "metilorange":
        return mix("#D7263D", "#F6AE2D", clamp((ph - 3.1) / 1.3))
    return cor_ph(ph)


def escala_ph(c, t, t0, x, y, w, h=64, marca=None, tm=None, rotulos=True, escuro=False, size=40):
    """faixa de pH de 0 a 14 que se pinta da esquerda para a direita; marca = pH apontado (em tm)"""
    p = ease_io(prog(t, t0, 0.9))
    if p <= 0:
        return
    tinta = _tinta(escuro)
    c.save()
    c.clipRect(skia.Rect.MakeXYWH(x - 2, y - 2, w * p + 4, h + 4))
    pt = skia.Paint(AntiAlias=True)
    pt.setShader(skia.GradientShader.MakeLinear([skia.Point(x, 0), skia.Point(x + w, 0)], [hexc(cr) for _, cr in _PH], [v / 14 for v, _ in _PH]))
    c.drawRRect(skia.RRect.MakeRectXY(skia.Rect.MakeXYWH(x, y, w, h), h / 2, h / 2), pt)
    c.restore()
    X = lambda v: x + h / 2 + (w - h) * clamp(v / 14)
    for v in range(0, 15):
        q = ep(t, t0 + v * 0.05, 0.3)
        if q > 0 and v % (1 if w > 1000 else 2) == 0:
            centro(c, str(v), X(v), y + h + size * 1.15, size, "b", tinta, q)
    if rotulos:
        for txt, v in (("ácido", 2.5), ("neutro", 7), ("básico", 11.5)):
            foco(c, t, t0 + 0.6, 0.4, lambda a, txt=txt, v=v: centro(c, txt, X(v), y + h + size * 2.5, size * 1.05, "i", tinta, a))
    if marca is not None:
        v = marca(t) if callable(marca) else marca
        q = ep(t, tm if tm is not None else t0 + 0.8, 0.4)
        if q > 0:
            F._cabeca(c, X(v), y - 8, 0, 1, 36, tinta, q)


# =====================================================================================================================
# gráficos
# =====================================================================================================================
def _suave(u):
    return 0.5 - 0.5 * math.cos(math.pi * clamp(u))


def _eixos(c, t, t0, x, y, w, h, nome_y, nome_x, size, escuro):
    """eixos em L com seta e o nome de cada um (sem números)"""
    tinta = _tinta(escuro)
    q = ep(t, t0, 0.4)
    if q <= 0:
        return
    F.seta(c, x, y + h, x, y - 30, tinta, q, 5, 24, ease_out(prog(t, t0, 0.5)))
    F.seta(c, x, y + h, x + w + 30, y + h, tinta, q, 5, 24, ease_out(prog(t, t0, 0.5)))
    foco(c, t, t0 + 0.3, 0.4, lambda a: (escreve(c, nome_y, x + 24, y - 10, size, "i", tinta, a),
                                         escreve(c, nome_x, x + w - larg(nome_x, "i", size), y + h + size * 1.3, size, "i", tinta, a)))


def energia(c, t, t0, x, y, w, h, er=60, ep_=20, pico=100, ea=None, dh=None, cat=None, rotulos=("reagentes", "produtos"),
            d=1.4, escuro=False, emax=None, size=46, sinal=True):
    """gráfico de energia da reação na caixa (x, y, w, h); deixe ~240 px livres à direita para a seta do ΔH.
    er, ep_, pico em unidades livres; ea/dh = instantes das setas; cat = pico com catalisador (tracejado). Devolve Y(e) → pixel"""
    tinta = _tinta(escuro)
    emax = emax or max(pico, er, ep_, cat or 0) * 1.15
    if t < t0:
        return None
    _eixos(c, t, t0, x, y, w, h, "energia", "caminho da reação", size, escuro)
    oy = y + h
    Y = lambda e: oy - h * e / emax

    def curva(u, top):
        if u < 0.22:
            return er
        if u < 0.5:
            return er + (top - er) * _suave((u - 0.22) / 0.28)
        if u < 0.78:
            return top + (ep_ - top) * _suave((u - 0.5) / 0.28)
        return ep_
    X = lambda u: x + w * 0.02 + w * 0.96 * u
    pts = [(X(u / 200), Y(curva(u / 200, pico))) for u in range(201)]
    F.poli(c, pts, ease_io(prog(t, t0 + 0.4, d)), _cor(escuro), 1.0, 8)
    if cat is not None and t >= t0 + 0.4 + d:
        ptc = [(X(u / 200), Y(curva(u / 200, cat))) for u in range(201)]
        F.poli(c, ptc, ease_io(prog(t, t0 + 0.6 + d, d)), tinta, 0.8, 6, dash=E.TRACO)
    foco(c, t, t0 + 0.6, 0.4, lambda a: escreve(c, rotulos[0], x + 20, Y(er) - size * 0.55, size, "i", tinta, a))
    foco(c, t, t0 + 0.4 + d * 0.9, 0.4, lambda a: centro(c, rotulos[1], X(0.9), Y(ep_) - size * 0.55, size, "i", tinta, a))
    xm = X(0.5)
    tr = TINTA2 if not escuro else "#8A8D99"
    if ea is not None:
        p = ep(t, ea, 0.4)
        if p > 0:
            M.line(c, X(0.22), Y(er), xm + 20, Y(er), tr, 0.7 * p, 3, dash=[10, 8])
            F.seta(c, xm, Y(er), xm, Y(pico) + 6, _cor(escuro), p, 6, 22, ease_out(prog(t, ea, 0.5)))
            foco(c, t, ea + 0.3, 0.4, lambda a: E.pilula(c, "Ea", xm - size * 1.1, (Y(er) + Y(pico)) / 2, size * 0.9, "g", fundo=E.COR, cor=E.SOBRE, a=a))
    if dh is not None:
        p = ep(t, dh, 0.4)
        if p > 0:
            xd = x + w + 70
            M.line(c, X(0.78), Y(er), xd + 14, Y(er), tr, 0.7 * p, 3, dash=[10, 8])
            M.line(c, X(0.98), Y(ep_), xd + 14, Y(ep_), tr, 0.7 * p, 3, dash=[10, 8])
            F.seta(c, xd, Y(er), xd, Y(ep_) + (6 if ep_ < er else -6), ELETRON if ep_ < er else "#E8A317", p, 6, 22, ease_out(prog(t, dh, 0.5)))
            s_ = ("ΔH < 0" if ep_ < er else "ΔH > 0") if sinal else "ΔH"
            foco(c, t, dh + 0.3, 0.4, lambda a: E.formula(c, s_, xd + 20, (Y(er) + Y(ep_)) / 2 + size * 0.36, size, "g", tinta, a))
    return Y


def aquecimento(c, t, t0, x, y, w, h, pf, pe, tmin, tmax, faixas=None, minutos=10, rotulos=True, d=2.0, escuro=False,
                size=40, cor=None, valores=True):
    """curva de aquecimento (temperatura × tempo) na caixa (x, y, w, h). Sem faixas, dois patamares (substância pura);
    faixas = ((f0, f1), (e0, e1)) faz a fusão e a ebulição subirem (mistura). Linhas tracejadas marcam PF e PE no eixo.
    Devolve (X, Y): tempo → pixel e temperatura → pixel"""
    if t < t0:
        return None
    tinta = _tinta(escuro)
    _eixos(c, t, t0, x, y, w, h, "temperatura (°C)", "tempo", size, escuro)
    (f0, f1), (e0, e1) = faixas if faixas else ((pf, pf), (pe, pe))
    seg = minutos / 5
    nos = [(0, tmin), (seg, f0), (2 * seg, f1), (3 * seg, e0), (4 * seg, e1), (5 * seg, tmax)]
    lo, hi = tmin - (tmax - tmin) * 0.08, tmax + (tmax - tmin) * 0.05
    X = lambda m: x + w * 0.03 + w * 0.92 * m / minutos
    Y = lambda T: y + h - h * (T - lo) / (hi - lo)
    pts = []
    for (xa, ya), (xb, yb) in zip(nos, nos[1:]):
        for k in range(30):
            u = k / 30
            pts.append((X(lerp(xa, xb, u)), Y(lerp(ya, yb, u))))
    pts.append((X(nos[-1][0]), Y(nos[-1][1])))
    tc = t0 + 0.6
    F.poli(c, pts, ease_io(prog(t, tc, d)), cor or _cor(escuro), 1.0, 8)
    if valores:
        for i, (T, rot) in enumerate(((pf, "PF") if not faixas else (f0, ""), (pe, "PE") if not faixas else (e0, ""))):
            ti = tc + d * (0.2 + 0.4 * i)
            q = ep(t, ti, 0.4)
            if q > 0:
                M.line(c, x, Y(T), X(nos[1 + 2 * i][0]), Y(T), TINTA2 if not escuro else "#8A8D99", 0.7 * q, 3, dash=[10, 8])
                txt = E._num(T)
                foco(c, t, ti, 0.4, lambda a, txt=txt, T=T: escreve(c, txt, x - 16 - larg(txt, "b", size), Y(T) + size * 0.36, size, "b", tinta, a))
    if rotulos:
        nomes = ("sólido", "fusão" if not faixas else "s + l", "líquido", "ebulição" if not faixas else "l + g", "gás")
        for i, s_ in enumerate(nomes):
            (xa, ya), (xb, yb) = nos[i], nos[i + 1]
            ti = tc + d * (i + 0.6) / 5
            plat = i in (1, 3)
            mx, my = X((xa + xb) / 2), Y((ya + yb) / 2)
            if plat:
                foco(c, t, ti, 0.4, lambda a, s_=s_, mx=mx, my=my: centro(c, s_, mx, my + size * 1.3, size * 1.05, "b", _cor(escuro), a))
            else:
                # do lado de cima e à esquerda do trecho que sobe
                ux, uy = E._uni(X(xa), Y(ya), X(xb), Y(yb))
                nx, ny = uy, -ux
                if ny > 0:
                    nx, ny = -nx, -ny
                wl = larg(s_, "i", size * 1.05)
                px = max(x + 16 + wl / 2, mx + nx * size * 1.3 - wl * 0.25)
                py = my + ny * size * 1.0
                foco(c, t, ti, 0.4, lambda a, s_=s_, px=px, py=py: centro(c, s_, px, py + size * 0.36, size * 1.05, "i", tinta, a))
    return X, Y


def _interp(pts):
    """interpolação cúbica monótona (Fritsch-Carlson): curva suave que não inventa máximos entre os pontos de tabela"""
    xs, ys = [p[0] for p in pts], [p[1] for p in pts]
    n = len(pts)
    if n < 3:
        return lambda v: lerp(ys[0], ys[-1], clamp((v - xs[0]) / (xs[-1] - xs[0])))
    dl = [(ys[i + 1] - ys[i]) / (xs[i + 1] - xs[i]) for i in range(n - 1)]
    m = [dl[0]] + [(0 if dl[i - 1] * dl[i] <= 0 else (dl[i - 1] + dl[i]) / 2) for i in range(1, n - 1)] + [dl[-1]]
    for i in range(n - 1):
        if dl[i] == 0:
            m[i] = m[i + 1] = 0
        else:
            a_, b_ = m[i] / dl[i], m[i + 1] / dl[i]
            r = a_ * a_ + b_ * b_
            if r > 9:
                k = 3 / math.sqrt(r)
                m[i], m[i + 1] = k * a_ * dl[i], k * b_ * dl[i]

    def f(v):
        if v <= xs[0]:
            return ys[0]
        for i in range(n - 1):
            if v <= xs[i + 1]:
                hh = xs[i + 1] - xs[i]
                u = (v - xs[i]) / hh
                h00, h10, h01, h11 = 2 * u ** 3 - 3 * u ** 2 + 1, u ** 3 - 2 * u ** 2 + u, -2 * u ** 3 + 3 * u ** 2, u ** 3 - u ** 2
                return h00 * ys[i] + h10 * hh * m[i] + h01 * ys[i + 1] + h11 * hh * m[i + 1]
        return ys[-1]
    return f


def solubilidade(c, t, t0, x, y, w, h, curvas, tmax=100, smax=120, d=1.2, escuro=False, passo=20, passo_y=20, size=36):
    """curvas de solubilidade (g de soluto em 100 g de água × temperatura), sobre F.grafico. curvas = [dict(nome, pts, cor, t)];
    cada curva passa pelos pontos de tabela, suave, com o nome na ponta. Devolve o plano P (P.x, P.y)"""
    P = F.grafico(c, t, t0, x, y, w, h, 0, tmax, 0, smax, "T (°C)", "S (g/100 g de água)", passo=passo, passo_y=passo_y, size=size,
                  escuro=escuro, grade=True)
    for i, cv in enumerate(curvas):
        f = _interp(cv["pts"])
        ti = cv.get("t", t0 + 0.6 + i * 0.5)
        cr = cv.get("cor") or (_cor(escuro) if i == 0 else [TINTA2 if not escuro else BR, "#E8A317", ELETRON][(i - 1) % 3])
        E.curva(c, t, ti, P, f, cv["pts"][0][0], cv["pts"][-1][0], d, cr, 7)
        xe, ye = cv["pts"][-1]
        foco(c, t, ti + d, 0.4, lambda a, cv=cv, xe=xe, ye=ye, cr=cr: formula(c, cv["nome"], P.x(xe) + 14, P.y(ye) + 14, size * 1.05, cr, a, "left", "b"))
    return P


# =====================================================================================================================
# eletroquímica
# =====================================================================================================================
def eletrons(c, t, t0, pts, vel=150, espaco=130, r=14, cor=None, a=1.0, rotulo=True):
    """elétrons (bolinhas azuis com −) andando pela polilinha pts a partir de t0"""
    if t < t0 or a <= 0:
        return
    comp = [math.dist(pts[i], pts[i + 1]) for i in range(len(pts) - 1)]
    L = sum(comp)
    q = ep(t, t0, 0.4) * a
    off = ((t - t0) * vel) % espaco
    s = off
    while s < L:
        rest, k = s, 0
        while k < len(comp) - 1 and rest > comp[k]:
            rest -= comp[k]
            k += 1
        f = rest / comp[k] if comp[k] else 0
        px, py = lerp(pts[k][0], pts[k + 1][0], f), lerp(pts[k][1], pts[k + 1][1], f)
        E.bola(c, px, py, r, cor or ELETRON, q)
        if rotulo:
            M.line(c, px - r * 0.45, py, px + r * 0.45, py, "#FFFFFF", q, max(2.5, r * 0.16))
        s += espaco


def pilha_daniell(c, t, t0, cx, cy, metais=("Zn", "Cu"), solucoes=("ZnSO4", "CuSO4"), te=None, ddp="1,10 V", polos=True,
                  escuro=False, w=1100, cores_sol=("#D6E4EE", "#6FA8DC")):
    """pilha de Daniell centrada em cx, com o fundo dos béqueres em cy + 220. te = instante em que os elétrons começam a andar"""
    tinta = _tinta(escuro)
    yb = cy + 220
    xa, xc = cx - w * 0.32, cx + w * 0.32
    bw, bh = w * 0.28, 300
    bequer(c, t, t0, xa, yb, bw, bh, 0.7, cores_sol[0], escuro=escuro, graduacao=False)
    bequer(c, t, t0 + 0.2, xc, yb, bw, bh, 0.7, cores_sol[1], escuro=escuro, graduacao=False)
    cm = {"Zn": "#8C96A8", "Cu": "#C87533", "Ag": "#C0C0C8", "Fe": "#7A7F88", "Mg": "#B8BCC4", "Al": "#B5BCC6", "Ni": "#9AA49A", "Pb": "#5E636D"}
    ytop = yb - bh - 90
    for i, (xm, met) in enumerate(((xa, metais[0]), (xc, metais[1]))):
        q = ep(t, t0 + 0.5 + i * 0.2, 0.4)
        if q > 0:
            M.rrect(c, xm - 22, ytop, 44, bh * 0.95, 8, cm.get(met, "#9AA0A8"), q)
            _borda_rr(c, xm - 22, ytop, 44, bh * 0.95, 8, mix(cm.get(met, "#9AA0A8"), "#000000", 0.35), q, 3)
            formula(c, met, xm, ytop - 22, 44, tinta, q, "center", "g")
        foco(c, t, t0 + 0.8 + i * 0.2, 0.4, lambda a, xm=xm, s=solucoes[i]: formula(c, s, xm, yb + 62, 42, tinta, a, "center", "b"))
    # ponte salina
    q = ep(t, t0 + 1.0, 0.5)
    if q > 0:
        yp = yb - bh * 0.62
        p = skia.Path()
        p.moveTo(xa + bw * 0.25, yb - bh * 0.3); p.lineTo(xa + bw * 0.25, yp); p.quadTo(cx, yp - 140, xc - bw * 0.25, yp); p.lineTo(xc - bw * 0.25, yb - bh * 0.3)
        c.drawPath(p, M.paint("#E9E3D0" if not escuro else "#5A5646", q, stroke=46))
        c.drawPath(p, M.paint(VIDRO if not escuro else "#B8BCC8", q * 0.6, stroke=4))
        foco(c, t, t0 + 1.2, 0.4, lambda a: centro(c, "ponte salina", cx, yp - 64, 36, "i", tinta, a))
    # fio e voltímetro
    yf = ytop - 130
    yt2 = ytop - 70
    fio = [(xa, yt2), (xa, yf), (cx - 70, yf)]
    fio2 = [(cx + 70, yf), (xc, yf), (xc, yt2)]
    for xm in (xa, xc):
        if t >= t0 + 1.2:
            M.line(c, xm, ytop, xm, ytop - 8, tinta, ep(t, t0 + 1.2, 0.3), 6)
    F.fio(c, t, t0 + 1.2, fio, 0.5, tinta, 6, escuro)
    F.fio(c, t, t0 + 1.4, fio2, 0.5, tinta, 6, escuro)
    q = ep(t, t0 + 1.5, 0.4)
    if q > 0:
        E.bola(c, cx, yf, 70, "#22232B" if not escuro else "#3A3B46", q)
        c.drawCircle(cx, yf, 70, M.paint(E.COR, q, stroke=5))
        centro(c, ddp, cx, yf + 14, 36, "g", BR, q)
    if te is not None:
        eletrons(c, t, te, fio + [(cx - 70, yf)], 130, 120, 13)
        eletrons(c, t, te + (math.dist(fio[0], fio[1]) + math.dist(fio[1], fio[2]) + 140) / 130, fio2, 130, 120, 13)
        foco(c, t, te, 0.4, lambda a: E.pilula(c, "e⁻", cx, yf - 120, 44, "g", fundo=ELETRON, a=a))
    if polos:
        foco(c, t, t0 + 1.8, 0.4, lambda a: (E.pilula(c, "ânodo  −", xa - 250, ytop + 40, 40, "g", fundo=TINTA, a=a),
                                             E.pilula(c, "cátodo  +", xc + 250, ytop + 40, 40, "g", fundo=E.COR, a=a)))


# =====================================================================================================================
# cálculo
# =====================================================================================================================
def _valor(s):
    """primeiro número de um texto pt-BR ("1.000,5 g" → 1000.5); None se não houver"""
    m = re.search(r"[0-9][0-9.]*(,[0-9]+)?", s.replace(" ", "") if s.count(" ") > 3 else s)
    if not m:
        return None
    return Fraction(m.group(0).replace(".", "").replace(",", "."))


def regra_tres(c, t, t0, cab, linhas, x, y, size=84, tl=None, tcruz=None, tx=None, conta=None, res=None, dx=520, dy=None,
               escuro=False, cor_x=None, tres=None, x_res=None):
    """regra de três em colunas: cab = (cabeçalho 1, cabeçalho 2); linhas = [(a, b), (c, "x")]; tl = instante de cada linha;
    tcruz = cruz do produto cruzado; conta = texto da conta (E.formula) em tx; res = resultado na esfera em tres"""
    tinta = _tinta(escuro)
    dy = dy or size * 1.5
    x1, x2 = x, x + dx
    if len(linhas) == 2:
        vals = [_valor(v) if v not in ("x", "?") else None for lin in linhas for v in lin]
        if res is not None and sum(v is None for v in vals) == 1:
            rv = _valor(res)
            i = vals.index(None)
            vals[i] = rv
            a_, b_, c_, d_ = vals
            assert a_ * d_ == b_ * c_, f"regra de três não fecha: {linhas} → {res}"
    foco(c, t, t0, 0.45, lambda a: (centro(c, cab[0], x1, y, size * 0.6, "i", TINTA2 if not escuro else E.CLARO, a),
                                    centro(c, cab[1], x2, y, size * 0.6, "i", TINTA2 if not escuro else E.CLARO, a)))
    q = ep(t, t0, 0.4)
    if q > 0:
        M.line(c, x1 - size * 1.6, y + size * 0.3, x2 + size * 1.6, y + size * 0.3, TINTA2 if not escuro else E.CLARO, 0.7 * q, 3)
    ys = []
    for i, lin in enumerate(linhas):
        yy = y + size * 0.4 + (i + 1) * dy
        ys.append(yy)
        ti = tl[i] if tl else t0 + 0.5 + i * 0.6
        for j, v in enumerate(lin):
            xx = (x1, x2)[j]
            ehx = v in ("x", "?")
            cr = (cor_x or _cor(escuro)) if ehx else tinta
            foco(c, t, ti + j * 0.2, 0.45, lambda a, v=v, xx=xx, yy=yy, cr=cr: formula(c, v, xx, yy, size, cr, a, "center"))
    if tcruz is not None and len(ys) == 2:
        p = ease_out(prog(t, tcruz, 0.6))
        if p > 0:
            k = size * 0.32
            wl = [formula(None, lin[0], 0, 0, size) / 2 + size * 0.3 for lin in linhas]
            wr = [formula(None, lin[1], 0, 0, size) / 2 + size * 0.3 for lin in linhas]
            M.line(c, x1 + wl[0], ys[0] - k, x2 - wr[1], ys[1] - k, _cor(escuro), 1.0, 6, progress=p)
            M.line(c, x1 + wl[1], ys[1] - k, x2 - wr[0], ys[0] - k, _cor(escuro), 1.0, 6, progress=p)
    yc = ys[-1] + dy * 1.1
    if conta:
        E.formula_em(c, t, tx if tx is not None else (tcruz or t0) + 0.8, conta, (x1 + x2) / 2, yc, size * 0.85, "g", tinta, "center")
    if res:
        tr = tres if tres is not None else (tx or tcruz or t0) + 1.2
        xr = x_res if x_res is not None else x2 + formula(None, linhas[-1][1], 0, 0, size) / 2 + size * 1.8
        k = ease_back(prog(t, tr, 0.5))
        if k > 0:
            wr = E.formula(None, res, 0, 0, size * 0.62, "g", a=0)
            E.bola(c, xr, ys[-1] - size * 0.32, max(size * 0.95, wr * 0.62) * k, E.COR)
            foco(c, t, tr + 0.1, 0.4, lambda a: E.formula(c, res, xr, ys[-1] - size * 0.32 + size * 0.22, size * 0.62, "g", E.SOBRE, a, "center"))
    return ys
