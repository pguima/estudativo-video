import sys, importlib.util
from pathlib import Path
sys.path.insert(0, "C:/Users/Paulo/Documents/Claude/videos_canal/_ferramentas")
import skia, motor
motor.set_theme("claro")
from motor import *
s = importlib.util.spec_from_file_location("k", Path(__file__).resolve().parents[2] / "comum.py"); K = importlib.util.module_from_spec(s); s.loader.exec_module(K)
casos = ["2^5 = 32", "2^{-3} = 1/8", "10^{-8}", "a^{m+n}", "(-3)^2 = 9", "-3^2 = -9", "(2/3)^{-2} = (3/2)^2 = 9/4",
         "(2·10^{-2})^3 = 2^3 · 10^{-6}", "2^{3^2} = 2^9", "2^{1/2} · 2^{1/3} = 2^{5/6}", "√{50} = 5√{2}", "√[3]{54} = 3√[3]{2}",
         "√{a·b} = √{a} · √{b}", "√{√[3]{64}} = √[6]{64} = 2", "6/√{5}-√{2} = 2√{5} + 2√{2}", "1/2 + 1/3 = 5/6", "2|3/4 = 11/4",
         "√{x^2} = |x|", "(2^5·4^3)/8^2 = 2^{11}/2^6", "a^{-n} = 1/a^n", "√[n]{a^m} = a^{m/n}", "√{9+16} ≠ √{9} + √{16}"]
surf = skia.Surface(W, H); c = surf.getCanvas(); background(c)
for i, s_ in enumerate(casos):
    col, row = divmod(i, 11)
    x, y = 80 + col * 920, 70 + row * 92
    line(c, x, y, x + 800, y, "#E0B0B0", 1, 1)
    K.expr(c, s_, x, y, 46, align="left")
surf.makeImageSnapshot().save(str(Path(__file__).parent / "folha.png"), skia.kPNG)
