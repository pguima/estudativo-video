"""Folha de conferência: o mesmo modelo de capa na cor de cada matéria. Uso: python folha_materias.py"""
import subprocess, sys
from pathlib import Path
RAIZ = Path(__file__).resolve().parents[3]
sys.path.insert(0, str(RAIZ / "_ferramentas"))
import skia
import editorial as E

AMOSTRA = {"Matemática": ("Somar", "frações", "sem errar"), "Português": ("Sujeito", "e verbo", "na prática"),
           "Redação": ("Tese", "forte", "em 2 linhas"), "Literatura": ("Machado", "de Assis", "sem medo"),
           "Inglês": ("Simple", "past", "de vez"), "Espanhol": ("Falsos", "amigos", "na prova"),
           "Artes": ("Semana", "de 22", "explicada"), "Física": ("Leis de", "Newton", "na prática"),
           "Química": ("Tabela", "periódica", "sem decorar"), "Biologia": ("Divisão", "celular", "sem confusão"),
           "História": ("Era", "Vargas", "em resumo"), "Geografia": ("Clima", "do Brasil", "sem decorar"),
           "Filosofia": ("Platão", "e Aristóteles", "sem medo"), "Sociologia": ("Durkheim", "e Marx", "na prova")}
pasta = Path(__file__).parent
quadros = pasta / "_quadros"; quadros.mkdir(exist_ok=True)
s = skia.Surface(E.W, E.H)
lista = []
for i, (m, (a, b, it)) in enumerate(AMOSTRA.items()):
    E.capa_modelo(s.getCanvas(), m, a, b, it)
    f = quadros / f"q{i:02d}.png"; s.makeImageSnapshot().save(str(f), skia.kPNG); lista.append(f)
(quadros / "l.txt").write_text("".join(f"file '{f.name}'\n" for f in lista), encoding="utf-8")
subprocess.run(["ffmpeg", "-v", "error", "-y", "-f", "concat", "-i", str(quadros / "l.txt"), "-vf",
                "scale=480:-1,tile=4x4:padding=8:color=white", "-frames:v", "1", "-q:v", "3", str(pasta / "folha_materias.jpg")], check=True)
for f in quadros.iterdir():
    f.unlink()
quadros.rmdir()
